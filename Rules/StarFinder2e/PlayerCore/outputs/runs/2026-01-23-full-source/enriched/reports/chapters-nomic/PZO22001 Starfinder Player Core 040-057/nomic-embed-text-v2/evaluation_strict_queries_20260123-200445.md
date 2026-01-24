# RulesLawyer Evaluation Report: nomic-embed-text-v2

## Summary
- Run ID: `None`
- Ruleset ID: `None`
- Document ID: `None`
- Chunk source: `enriched`
- Chunk count: `714`
- Query count: `150`
- Evaluated queries: `150`
- Coverage: `1.0000`
- MRR: `0.9101`
- hit@1: `0.8600`
- hit@3: `0.9600`
- hit@5: `0.9867`
- hit@10: `1.0000`
- Embeddings reused: `False`
- Graph boost: `0.05` (depth=2, top_k=50, source=top, seed_top_n=3, same_kind_only=False, decay=0.4)

## Timings (ms)
- Embedding (chunks): `10715`
- Embedding (queries): `2790`
- Evaluation (strict): `94`
- Evaluation (expanded): `0`
- Total: `18033`

### Timing Estimates (ms)
- Evaluation (strict): `180`
- Evaluation (expanded): `None`
- Total: `13685`

## Query Details
### Query 0
- Text: What is the rule about CHAPTER 2: ANCESTRIES &  BACKGROUNDS?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/1/SectionHeader/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/1/SectionHeader/1', 'PZO22001 Starfinder Player Core 040-057::/page/9/Text/51', 'PZO22001 Starfinder Player Core 040-057::/page/17/Text/56']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/1/SectionHeader/1` | 0.859395 | CHAPTER 2: ANCESTRIES &  BACKGROUNDS |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/9/Text/51` | 0.753670 | **ANCESTRIES & ** **BACKGROUNDS** |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/17/Text/56` | 0.753670 | **ANCESTRIES & ** **BACKGROUNDS** |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/11/Text/31` | 0.723670 | **ANCESTRIES & ** **BACKGROUNDS** |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/7/Text/31` | 0.723670 | **ANCESTRIES & ** **BACKGROUNDS** |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/37` | 0.723670 | **ANCESTRIES & ** **BACKGROUNDS** |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/13/Text/62` | 0.723670 | **ANCESTRIES & ** **BACKGROUNDS** |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/66` | 0.723670 | **ANCESTRIES & ** **BACKGROUNDS** |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/31` | 0.723670 | **ANCESTRIES & ** **BACKGROUNDS** |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/15/Text/32` | 0.723670 | **ANCESTRIES & ** **BACKGROUNDS** |

### Query 1
- Text: What is the rule about Starfinder contains as many species as there are stars in the sky. This section details a wide variety of  new and updated ancestries that are prevalent in the Starfinder setting. It also provides details on the  use of languages in Starfinder, from within the core of the Pact Worlds to countless planets beyond!?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/1/Text/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/1/Text/2', 'PZO22001 Starfinder Player Core 040-057::/page/12/Text/2', 'PZO22001 Starfinder Player Core 040-057::/page/1/ListItem/11']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/2` | 1.000875 | Starfinder contains as many species as there are stars in the sky. This section details a wide variety of  new and updated ancestries that are prevalent in the Starfinder setting. It also provides det |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/12/Text/2` | 0.593210 | Humans were the most common ancestry on Golarion before  that world disappeared, and they've since spread to the stars  thanks to their versatility. Select a general feat of your choice  for which you |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/1/ListItem/11` | 0.586565 | **Languages**, starting on page 97, let your character  communicate with people and creatures of the galaxy. |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/25` | 0.544002 | This tells you the languages that members of the ancestry  speak at 1st level. If your Intelligence modifier is +1 or higher,  you can select more languages from a list given here. More  about languag |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/6` | 0.510391 | A character has one ancestry and one background, both of  which you select during character creation. You'll also select  a number of languages for your character. Once chosen, your  ancestry and back |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/11/Text/14` | 0.493370 | Human societies are as varied as the worlds they thrive on.  While the Azlanti Star Empire seeks to recapture an imagined  era of glory by isolating and idealizing an ancient culture from  lost Golari |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/11/Text/24` | 0.489221 | Your ancestors lived on Golarion, and though the precise  circumstances of their survival are lost to the Gap, you strongly  identify with the lost planet's cultures. You become trained in  Golarion L |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/11/Text/9` | 0.480179 | Human ambition has created empires throughout the stars. The  Pact Worlds have many human residents, while the expansion  of the Azlanti Star Empire presents a more sinister expression  of humanity's |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/1/ListItem/8` | 0.477948 | **Ancestries** express the lineage your character hails from.  Within ancestries are heritages—subgroups that have  unique characteristics. An ancestry provides attribute  boosts (and perhaps attribut |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/6/Text/11` | 0.473647 | Additional languages equal to your Intelligence  modifier (if it's positive). Choose from the list  of common languages and any other languages  to which you have access (such as the languages  preval |

### Query 2
- Text: What is the rule about A character has one ancestry and one background, both of  which you select during character creation. You'll also select  a number of languages for your character. Once chosen, your  ancestry and background can't be changed.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/1/Text/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/1/Text/6', 'PZO22001 Starfinder Player Core 040-057::/page/1/Text/34', 'PZO22001 Starfinder Player Core 040-057::/page/1/Text/31']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/6` | 0.973391 | A character has one ancestry and one background, both of  which you select during character creation. You'll also select  a number of languages for your character. Once chosen, your  ancestry and back |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/34` | 0.704550 | As a starting character, you can choose from only 1stlevel ancestry feats, but later choices can be made from any  feat of your level or lower. These feats also sometimes list  prerequisites, which ar |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/31` | 0.690093 | You select a heritage at 1st level to reflect abilities common  among those of your ancestry in the environment where  you were born or grew up. You have only one heritage and  can't change it later. |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/23` | 0.613898 | **Alternate** **Ancestry** **Boosts:** Because of the wide variety of  people within any ancestry, you can *always* choose to take two  free boosts to represent your character, even if the ancestry  n |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/12/Text/4` | 0.601349 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As a human, you choose from among the  following anc |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/21` | 0.596545 | When creating a character of this ancestry, you apply attribute |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/33` | 0.592500 | This section presents ancestry feats, which allow you to  customize your character. You gain your first ancestry feat  at 1st level, and you gain another at 5th level, 9th level, 13th  level, and 17th |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/1/ListItem/8` | 0.571847 | **Ancestries** express the lineage your character hails from.  Within ancestries are heritages—subgroups that have  unique characteristics. An ancestry provides attribute  boosts (and perhaps attribut |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/4/Text/5` | 0.558725 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As an android, you choose from among  the following |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/25` | 0.558687 | This tells you the languages that members of the ancestry  speak at 1st level. If your Intelligence modifier is +1 or higher,  you can select more languages from a list given here. More  about languag |

### Query 3
- Text: Summarize This chapter is divided into four parts.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/1/Text/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/1/Text/7', 'PZO22001 Starfinder Player Core 040-057::/page/1/SectionHeader/1', 'PZO22001 Starfinder Player Core 040-057::/page/14/Text/17']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/7` | 0.983261 | This chapter is divided into four parts. |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/1/SectionHeader/1` | 0.425866 | CHAPTER 2: ANCESTRIES &  BACKGROUNDS |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/14/Text/17` | 0.397566 | You have four arms, which allows you to wield and hold up to four hands' worth of |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/13` | 0.352910 | Each entry includes details about the ancestry and presents  the rules elements described below. |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/12/Text/4` | 0.340885 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As a human, you choose from among the  following anc |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/17/SectionHeader/35` | 0.330632 | **DISCIPLE OF THE CYCLE** **FEAT 13** |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/16/Text/7` | 0.314933 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As a kasatha, you choose from among  the following a |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/14/SectionHeader/16` | 0.311765 | FOUR-ARMED |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/4/Text/5` | 0.307704 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As an android, you choose from among  the following |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/1/ListItem/8` | 0.304396 | **Ancestries** express the lineage your character hails from.  Within ancestries are heritages—subgroups that have  unique characteristics. An ancestry provides attribute  boosts (and perhaps attribut |

### Query 4
- Text: What is the rule about **Ancestries** express the lineage your character hails from.  Within ancestries are heritages—subgroups that have  unique characteristics. An ancestry provides attribute  boosts (and perhaps attribute flaws), Hit Points, ancestry  feats, and sometimes additional abilities.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/1/ListItem/8']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/1/ListItem/8', 'PZO22001 Starfinder Player Core 040-057::/page/1/Text/23', 'PZO22001 Starfinder Player Core 040-057::/page/1/Text/21']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/1/ListItem/8` | 0.999964 | **Ancestries** express the lineage your character hails from.  Within ancestries are heritages—subgroups that have  unique characteristics. An ancestry provides attribute  boosts (and perhaps attribut |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/23` | 0.699851 | **Alternate** **Ancestry** **Boosts:** Because of the wide variety of  people within any ancestry, you can *always* choose to take two  free boosts to represent your character, even if the ancestry  n |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/21` | 0.697241 | When creating a character of this ancestry, you apply attribute |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/29` | 0.652141 | Any other entries in the sidebar represent abilities, senses,  and other qualities all members of the ancestry manifest.  These are omitted for ancestries with no special rules. |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/31` | 0.646279 | You select a heritage at 1st level to reflect abilities common  among those of your ancestry in the environment where  you were born or grew up. You have only one heritage and  can't change it later. |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/22` | 0.644337 | boosts to increase some attribute modifiers, and possibly  attribute flaws to decrease others (depending on the ancestry).  For more about attribute boosts and flaws, see page 23. |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/33` | 0.630815 | This section presents ancestry feats, which allow you to  customize your character. You gain your first ancestry feat  at 1st level, and you gain another at 5th level, 9th level, 13th  level, and 17th |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/6` | 0.615237 | A character has one ancestry and one background, both of  which you select during character creation. You'll also select  a number of languages for your character. Once chosen, your  ancestry and back |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/34` | 0.609450 | As a starting character, you can choose from only 1stlevel ancestry feats, but later choices can be made from any  feat of your level or lower. These feats also sometimes list  prerequisites, which ar |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/12/Text/4` | 0.599175 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As a human, you choose from among the  following anc |

### Query 5
- Text: What is the rule about **Versatile** **heritages**, starting on page 82, are heritage  options available to all ancestries for extra customization,  such as characters with more unique or unusual origins.  These are selected instead of a standard heritage.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/1/ListItem/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/1/ListItem/9', 'PZO22001 Starfinder Player Core 040-057::/page/1/Text/48', 'PZO22001 Starfinder Player Core 040-057::/page/5/Text/77']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/1/ListItem/9` | 0.973997 | **Versatile** **heritages**, starting on page 82, are heritage  options available to all ancestries for extra customization,  such as characters with more unique or unusual origins.  These are selecte |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/48` | 0.662022 | **Versatile ** **Heritages** |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/77` | 0.662022 | **Versatile ** **Heritages** |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/15/Text/43` | 0.620022 | **Versatile ** **Heritages** |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/7/Text/41` | 0.620022 | **Versatile ** **Heritages** |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/11/Text/40` | 0.620022 | **Versatile ** **Heritages** |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/13/Text/72` | 0.620022 | **Versatile ** **Heritages** |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/31` | 0.601468 | You select a heritage at 1st level to reflect abilities common  among those of your ancestry in the environment where  you were born or grew up. You have only one heritage and  can't change it later. |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/23` | 0.598657 | **Alternate** **Ancestry** **Boosts:** Because of the wide variety of  people within any ancestry, you can *always* choose to take two  free boosts to represent your character, even if the ancestry  n |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/6` | 0.579931 | A character has one ancestry and one background, both of  which you select during character creation. You'll also select  a number of languages for your character. Once chosen, your  ancestry and back |

### Query 6
- Text: What is the rule about **Backgrounds**, starting on page 92, describe training  or environments your character experienced before  becoming an adventurer. Your character's background  provides attribute boosts, skill training, and a skill feat.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/1/ListItem/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/1/ListItem/10', 'PZO22001 Starfinder Player Core 040-057::/page/1/Text/6', 'PZO22001 Starfinder Player Core 040-057::/page/1/ListItem/8']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/1/ListItem/10` | 0.972674 | **Backgrounds**, starting on page 92, describe training  or environments your character experienced before  becoming an adventurer. Your character's background  provides attribute boosts, skill traini |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/6` | 0.617345 | A character has one ancestry and one background, both of  which you select during character creation. You'll also select  a number of languages for your character. Once chosen, your  ancestry and back |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/1/ListItem/8` | 0.598725 | **Ancestries** express the lineage your character hails from.  Within ancestries are heritages—subgroups that have  unique characteristics. An ancestry provides attribute  boosts (and perhaps attribut |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/4/Text/10` | 0.540986 | You have a keen interest in the origins of your people. You  gain the trained proficiency rank in Crafting and Thievery. If  you would automatically become trained in one of those skills  (from your b |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/17/Text/70` | 0.539340 | **Backgrounds** |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/80` | 0.539340 | **Backgrounds** |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/7/Text/44` | 0.539340 | **Backgrounds** |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/13/Text/75` | 0.539340 | **Backgrounds** |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/44` | 0.539340 | **Backgrounds** |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/51` | 0.539340 | **Backgrounds** |

### Query 7
- Text: What is the rule about **Languages**, starting on page 97, let your character  communicate with people and creatures of the galaxy.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/1/ListItem/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/1/ListItem/11', 'PZO22001 Starfinder Player Core 040-057::/page/6/Text/17', 'PZO22001 Starfinder Player Core 040-057::/page/1/Text/2']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/1/ListItem/11` | 0.947013 | **Languages**, starting on page 97, let your character  communicate with people and creatures of the galaxy. |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/6/Text/17` | 0.635287 | You can communicate mentally with creatures within  30 feet. You can communicate only with creatures  that share a language with you. This doesn't give you  any access to their thoughts, and it commun |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/2` | 0.529833 | Starfinder contains as many species as there are stars in the sky. This section details a wide variety of  new and updated ancestries that are prevalent in the Starfinder setting. It also provides det |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/6` | 0.484102 | A character has one ancestry and one background, both of  which you select during character creation. You'll also select  a number of languages for your character. Once chosen, your  ancestry and back |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/2/Text/10` | 0.470244 | Additional languages equal to 1 + your Intelligence modifier (if it's positive). Choose from the list of common languages and any other languages to which you have access (such as the languages preval |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/6/Text/11` | 0.468563 | Additional languages equal to your Intelligence  modifier (if it's positive). Choose from the list  of common languages and any other languages  to which you have access (such as the languages  preval |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/25` | 0.467390 | This tells you the languages that members of the ancestry  speak at 1st level. If your Intelligence modifier is +1 or higher,  you can select more languages from a list given here. More  about languag |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/10/Text/8` | 0.466409 | Additional languages equal to 1 + your Intelligence modifier (if it's positive). Choose from the list of common languages and any other languages to which you have access (such as the languages preval |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/7/Text/45` | 0.466394 | **Languages** |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/11/Text/44` | 0.466394 | **Languages** |

### Query 8
- Text: Summarize ANCESTRY ENTRIES
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/1/SectionHeader/12']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/1/SectionHeader/12', 'PZO22001 Starfinder Player Core 040-057::/page/1/SectionHeader/32', 'PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/3']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/1/SectionHeader/12` | 1.001449 | ANCESTRY ENTRIES |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/1/SectionHeader/32` | 0.667642 | ANCESTRY FEATS |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/3` | 0.655045 | HUMAN ANCESTRY FEATS |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/4/SectionHeader/4` | 0.594110 | ANDROID ANCESTRY  FEATS |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/1/SectionHeader/1` | 0.547405 | CHAPTER 2: ANCESTRIES &  BACKGROUNDS |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/11/Text/31` | 0.522521 | **ANCESTRIES & ** **BACKGROUNDS** |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/17/Text/56` | 0.522521 | **ANCESTRIES & ** **BACKGROUNDS** |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/9/Text/51` | 0.522521 | **ANCESTRIES & ** **BACKGROUNDS** |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/31` | 0.522521 | **ANCESTRIES & ** **BACKGROUNDS** |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/66` | 0.522521 | **ANCESTRIES & ** **BACKGROUNDS** |

### Query 9
- Text: What is the rule about Each entry includes details about the ancestry and presents  the rules elements described below.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/1/Text/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/1/Text/13', 'PZO22001 Starfinder Player Core 040-057::/page/1/Text/29', 'PZO22001 Starfinder Player Core 040-057::/page/1/Text/21']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/13` | 0.921381 | Each entry includes details about the ancestry and presents  the rules elements described below. |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/29` | 0.673663 | Any other entries in the sidebar represent abilities, senses,  and other qualities all members of the ancestry manifest.  These are omitted for ancestries with no special rules. |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/21` | 0.606631 | When creating a character of this ancestry, you apply attribute |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/1/ListItem/8` | 0.561538 | **Ancestries** express the lineage your character hails from.  Within ancestries are heritages—subgroups that have  unique characteristics. An ancestry provides attribute  boosts (and perhaps attribut |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/12/Text/4` | 0.552549 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As a human, you choose from among the  following anc |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/34` | 0.545075 | As a starting character, you can choose from only 1stlevel ancestry feats, but later choices can be made from any  feat of your level or lower. These feats also sometimes list  prerequisites, which ar |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/6` | 0.543526 | A character has one ancestry and one background, both of  which you select during character creation. You'll also select  a number of languages for your character. Once chosen, your  ancestry and back |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/31` | 0.519303 | You select a heritage at 1st level to reflect abilities common  among those of your ancestry in the environment where  you were born or grew up. You have only one heritage and  can't change it later. |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/33` | 0.513800 | This section presents ancestry feats, which allow you to  customize your character. You gain your first ancestry feat  at 1st level, and you gain another at 5th level, 9th level, 13th  level, and 17th |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/4/Text/5` | 0.506410 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As an android, you choose from among  the following |

### Query 10
- Text: What is the rule about HIT POINTS?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/1/SectionHeader/14']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/1/SectionHeader/14', 'PZO22001 Starfinder Player Core 040-057::/page/9/Text/33', 'PZO22001 Starfinder Player Core 040-057::/page/13/Text/59']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/1/SectionHeader/14` | 0.872808 | HIT POINTS |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/9/Text/33` | 0.471591 | You tweak your anatomy and bodily systems to metabolize  pharmaceuticals more efficiently. Regain additional Hit Points  equal to half your level when you restore Hit Points to yourself  using a consu |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/13/Text/59` | 0.449338 | You return from the brink of death, hauling yourself back  to consciousness through exhaustion and pain. If you have  the dying or unconscious conditions, you lose the dying and  unconscious condition |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/42` | 0.370867 | Your nanites are programmed to automatically revive you.  You are restored to 1 Hit Point, lose the dying and unconscious  conditions, and can act normally on this turn. You gain or  increase the woun |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/9/Text/1` | 0.361774 | **Trigger** An enemy scores a critical hit against you with a  Strike. |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/9/Text/2` | 0.340329 | Your anatomy adjusts to distribute damage from vital areas.  The triggering attack deals only the damage it would deal on a  hit (typically normal damage instead of double damage). Any  other effects |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/9/ListItem/41` | 0.302418 | You occupy the target's space and can't take actions  with the move trait. If the target moves, you move with  them. |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/17/Text/1` | 0.299241 | At 5th level, whenever you get a critical hit with one of  these weapons, you get its critical specialization effect. |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/9/ListItem/42` | 0.295413 | For each Speed you possess, compare it to that of your  target. If your Speed is faster, or they lack that Speed,  they gain your Speed. |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/9` | 0.293267 | You were created to fight other synthetic creatures. When  you roll a critical hit against a creature with the tech trait, the  target becomes glitching 1. |

### Query 11
- Text: What is the rule about This tells you how many HP your PC gains from their ancestry  at 1st level. You'll add the HP from your character's class  (including their Constitution modifier) to this number. For more  on calculating HP, see Step 7: Record Class Details (page 21).?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/1/Text/15']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/1/Text/15', 'PZO22001 Starfinder Player Core 040-057::/page/12/Text/4', 'PZO22001 Starfinder Player Core 040-057::/page/1/Text/33']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/15` | 0.993457 | This tells you how many HP your PC gains from their ancestry  at 1st level. You'll add the HP from your character's class  (including their Constitution modifier) to this number. For more  on calculat |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/12/Text/4` | 0.665054 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As a human, you choose from among the  following anc |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/33` | 0.659534 | This section presents ancestry feats, which allow you to  customize your character. You gain your first ancestry feat  at 1st level, and you gain another at 5th level, 9th level, 13th  level, and 17th |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/8/Text/4` | 0.558627 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th,  9th, 13th, and 17th level). As a barathu, you choose from  among the following a |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/4/Text/5` | 0.558595 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As an android, you choose from among  the following |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/21` | 0.554306 | When creating a character of this ancestry, you apply attribute |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/25` | 0.547406 | This tells you the languages that members of the ancestry  speak at 1st level. If your Intelligence modifier is +1 or higher,  you can select more languages from a list given here. More  about languag |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/31` | 0.540381 | You select a heritage at 1st level to reflect abilities common  among those of your ancestry in the environment where  you were born or grew up. You have only one heritage and  can't change it later. |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/16/Text/7` | 0.539198 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As a kasatha, you choose from among  the following a |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/34` | 0.537692 | As a starting character, you can choose from only 1stlevel ancestry feats, but later choices can be made from any  feat of your level or lower. These feats also sometimes list  prerequisites, which ar |

### Query 12
- Text: Summarize SIZE
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/1/SectionHeader/16']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/1/SectionHeader/16', 'PZO22001 Starfinder Player Core 040-057::/page/1/Text/17', 'PZO22001 Starfinder Player Core 040-057::/page/6/Text/7']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/1/SectionHeader/16` | 0.866280 | SIZE |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/17` | 0.457519 | This tells you the physical size of members of the ancestry.  Medium corresponds roughly to the height and weight range  of a human adult, and Small is roughly half that. |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/6/Text/7` | 0.413371 | SIZE: MEDIUM SPEED: 5 FEET (HOVER);  FLY 20 FEET |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/2/Text/5` | 0.367439 | SIZE: MEDIUM SPEED: 25 FEET |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/10/Text/5` | 0.367439 | SIZE: MEDIUM SPEED: 25 FEET |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/14/Text/7` | 0.367439 | SIZE: MEDIUM SPEED: 25 FEET |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/9/ListItem/40` | 0.363219 | If the target is Medium or smaller, their size increases  to Large and their reach increases to 10 feet. |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/11/Text/16` | 0.324808 | **Sample Names:** Akif, Alezandaru, Amare, Baolo, Belor,  Darilian, Hadzi, Hai Minh, Hiriko, Iolana, Jokug, Korva, Morvius,  Navasi, Pao, Pasara, Raziya, Revhi, Sahba, Seoni, Sephia, Signe,  Valeros, |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/15/SectionHeader/11` | 0.321400 | PHYSICAL DESCRIPTION |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/7/SectionHeader/11` | 0.321400 | PHYSICAL DESCRIPTION |

### Query 13
- Text: Summarize This tells you the physical size of members of the ancestry.  Medium corresponds roughly to the height and weight range  of a human adult, and Small is roughly half that.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/1/Text/17']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/1/Text/17', 'PZO22001 Starfinder Player Core 040-057::/page/1/ListItem/8', 'PZO22001 Starfinder Player Core 040-057::/page/9/ListItem/40']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/17` | 1.043461 | This tells you the physical size of members of the ancestry.  Medium corresponds roughly to the height and weight range  of a human adult, and Small is roughly half that. |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/1/ListItem/8` | 0.498529 | **Ancestries** express the lineage your character hails from.  Within ancestries are heritages—subgroups that have  unique characteristics. An ancestry provides attribute  boosts (and perhaps attribut |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/9/ListItem/40` | 0.495365 | If the target is Medium or smaller, their size increases  to Large and their reach increases to 10 feet. |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/11/Text/12` | 0.453313 | Humans' physical characteristics vary based on their lineage  and home world. Humans have a wide variety of skin and hair  colors, body types, and facial features. Some environments  produce distinct |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/12/Text/4` | 0.439854 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As a human, you choose from among the  following anc |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/12/Text/2` | 0.432281 | Humans were the most common ancestry on Golarion before  that world disappeared, and they've since spread to the stars  thanks to their versatility. Select a general feat of your choice  for which you |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/19` | 0.431449 | This entry lists how far a member of the ancestry can move  each time they spend an action (such as Stride) to do so. |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/31` | 0.431080 | You select a heritage at 1st level to reflect abilities common  among those of your ancestry in the environment where  you were born or grew up. You have only one heritage and  can't change it later. |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/11/Text/22` | 0.423165 | Humans don't have significant physiological differences  defined by their lineage. Instead, their heritages reveal their  potential as a people. In many cases, these heritages might  represent offshoo |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/15` | 0.422451 | This tells you how many HP your PC gains from their ancestry  at 1st level. You'll add the HP from your character's class  (including their Constitution modifier) to this number. For more  on calculat |

### Query 14
- Text: Summarize SPEED
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/1/SectionHeader/18']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/1/SectionHeader/18', 'PZO22001 Starfinder Player Core 040-057::/page/10/Text/5', 'PZO22001 Starfinder Player Core 040-057::/page/14/Text/7']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/1/SectionHeader/18` | 0.888855 | SPEED |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/10/Text/5` | 0.584567 | SIZE: MEDIUM SPEED: 25 FEET |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/14/Text/7` | 0.584567 | SIZE: MEDIUM SPEED: 25 FEET |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/2/Text/5` | 0.542567 | SIZE: MEDIUM SPEED: 25 FEET |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/6/Text/7` | 0.472055 | SIZE: MEDIUM SPEED: 5 FEET (HOVER);  FLY 20 FEET |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/9/ListItem/42` | 0.456783 | For each Speed you possess, compare it to that of your  target. If your Speed is faster, or they lack that Speed,  they gain your Speed. |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/9/Text/13` | 0.339768 | You gain a +10-foot circumstance bonus to all your Speeds  until the start of your next turn. Then you Stride. |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/17/Text/75` | 0.331021 | **EQUIPMENT** **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/13/Text/80` | 0.331021 | **EQUIPMENT** **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/85` | 0.331021 | **EQUIPMENT** **SPELLS** |

### Query 15
- Text: What is the rule about This entry lists how far a member of the ancestry can move  each time they spend an action (such as Stride) to do so.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/1/Text/19']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/1/Text/19', 'PZO22001 Starfinder Player Core 040-057::/page/1/Text/13', 'PZO22001 Starfinder Player Core 040-057::/page/12/Text/4']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/19` | 0.950121 | This entry lists how far a member of the ancestry can move  each time they spend an action (such as Stride) to do so. |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/13` | 0.589109 | Each entry includes details about the ancestry and presents  the rules elements described below. |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/12/Text/4` | 0.556198 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As a human, you choose from among the  following anc |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/9/Text/13` | 0.491295 | You gain a +10-foot circumstance bonus to all your Speeds  until the start of your next turn. Then you Stride. |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/29` | 0.474940 | Any other entries in the sidebar represent abilities, senses,  and other qualities all members of the ancestry manifest.  These are omitted for ancestries with no special rules. |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/33` | 0.466408 | This section presents ancestry feats, which allow you to  customize your character. You gain your first ancestry feat  at 1st level, and you gain another at 5th level, 9th level, 13th  level, and 17th |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/34` | 0.466376 | As a starting character, you can choose from only 1stlevel ancestry feats, but later choices can be made from any  feat of your level or lower. These feats also sometimes list  prerequisites, which ar |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/4/Text/5` | 0.463761 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As an android, you choose from among  the following |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/9/ListItem/41` | 0.454286 | You occupy the target's space and can't take actions  with the move trait. If the target moves, you move with  them. |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/8/Text/4` | 0.451718 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th,  9th, 13th, and 17th level). As a barathu, you choose from  among the following a |

### Query 16
- Text: Summarize ATTRIBUTE BOOSTS & FLAWS
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/1/SectionHeader/20']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/1/SectionHeader/20', 'PZO22001 Starfinder Player Core 040-057::/page/10/Text/6', 'PZO22001 Starfinder Player Core 040-057::/page/1/Text/22']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/1/SectionHeader/20` | 0.985615 | ATTRIBUTE BOOSTS & FLAWS |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/10/Text/6` | 0.681151 | ATTRIBUTE BOOSTS Two free attribute boosts |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/22` | 0.640909 | boosts to increase some attribute modifiers, and possibly  attribute flaws to decrease others (depending on the ancestry).  For more about attribute boosts and flaws, see page 23. |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/6/Text/8` | 0.553482 | ATTRIBUTE  BOOSTS Constitution Wisdom Free |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/14/Text/8` | 0.539284 | ATTRIBUTE BOOSTS Strength Wisdom Free |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/14/Text/9` | 0.533347 | ATTRIBUTE FLAW Charisma |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/2/Text/7` | 0.533347 | ATTRIBUTE FLAW Charisma |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/2/Text/6` | 0.479587 | ATTRIBUTE BOOSTS Dexterity Intelligence Free |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/6/Text/9` | 0.475701 | ATTRIBUTE FLAW Dexterity |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/23` | 0.442536 | **Alternate** **Ancestry** **Boosts:** Because of the wide variety of  people within any ancestry, you can *always* choose to take two  free boosts to represent your character, even if the ancestry  n |

### Query 17
- Text: What is the rule about When creating a character of this ancestry, you apply attribute?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/1/Text/21']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/1/Text/21', 'PZO22001 Starfinder Player Core 040-057::/page/1/Text/6', 'PZO22001 Starfinder Player Core 040-057::/page/1/ListItem/8']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/21` | 0.964909 | When creating a character of this ancestry, you apply attribute |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/6` | 0.656836 | A character has one ancestry and one background, both of  which you select during character creation. You'll also select  a number of languages for your character. Once chosen, your  ancestry and back |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/1/ListItem/8` | 0.638496 | **Ancestries** express the lineage your character hails from.  Within ancestries are heritages—subgroups that have  unique characteristics. An ancestry provides attribute  boosts (and perhaps attribut |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/22` | 0.596136 | boosts to increase some attribute modifiers, and possibly  attribute flaws to decrease others (depending on the ancestry).  For more about attribute boosts and flaws, see page 23. |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/33` | 0.576450 | This section presents ancestry feats, which allow you to  customize your character. You gain your first ancestry feat  at 1st level, and you gain another at 5th level, 9th level, 13th  level, and 17th |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/12/Text/4` | 0.574062 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As a human, you choose from among the  following anc |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/34` | 0.564312 | As a starting character, you can choose from only 1stlevel ancestry feats, but later choices can be made from any  feat of your level or lower. These feats also sometimes list  prerequisites, which ar |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/29` | 0.553188 | Any other entries in the sidebar represent abilities, senses,  and other qualities all members of the ancestry manifest.  These are omitted for ancestries with no special rules. |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/13` | 0.552344 | Each entry includes details about the ancestry and presents  the rules elements described below. |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/31` | 0.537763 | You select a heritage at 1st level to reflect abilities common  among those of your ancestry in the environment where  you were born or grew up. You have only one heritage and  can't change it later. |

### Query 18
- Text: What is the rule about boosts to increase some attribute modifiers, and possibly  attribute flaws to decrease others (depending on the ancestry).  For more about attribute boosts and flaws, see page 23.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/1/Text/22']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/1/Text/22', 'PZO22001 Starfinder Player Core 040-057::/page/1/Text/23', 'PZO22001 Starfinder Player Core 040-057::/page/1/Text/21']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/22` | 0.975350 | boosts to increase some attribute modifiers, and possibly  attribute flaws to decrease others (depending on the ancestry).  For more about attribute boosts and flaws, see page 23. |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/23` | 0.683597 | **Alternate** **Ancestry** **Boosts:** Because of the wide variety of  people within any ancestry, you can *always* choose to take two  free boosts to represent your character, even if the ancestry  n |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/21` | 0.627994 | When creating a character of this ancestry, you apply attribute |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/10/Text/6` | 0.571019 | ATTRIBUTE BOOSTS Two free attribute boosts |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/1/ListItem/8` | 0.561973 | **Ancestries** express the lineage your character hails from.  Within ancestries are heritages—subgroups that have  unique characteristics. An ancestry provides attribute  boosts (and perhaps attribut |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/33` | 0.533362 | This section presents ancestry feats, which allow you to  customize your character. You gain your first ancestry feat  at 1st level, and you gain another at 5th level, 9th level, 13th  level, and 17th |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/15` | 0.525722 | This tells you how many HP your PC gains from their ancestry  at 1st level. You'll add the HP from your character's class  (including their Constitution modifier) to this number. For more  on calculat |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/12/Text/4` | 0.519140 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As a human, you choose from among the  following anc |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/29` | 0.513440 | Any other entries in the sidebar represent abilities, senses,  and other qualities all members of the ancestry manifest.  These are omitted for ancestries with no special rules. |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/9/Text/48` | 0.489777 | You've cataloged the genetic code from countless ancestries  you've encountered, and you can draw upon any of them  to enhance and evolve your body. Increase the number of  ancestries you can select w |

### Query 19
- Text: What is the rule about **Alternate** **Ancestry** **Boosts:** Because of the wide variety of  people within any ancestry, you can *always* choose to take two  free boosts to represent your character, even if the ancestry  normally has three boosts and a flaw.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/1/Text/23']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/1/Text/23', 'PZO22001 Starfinder Player Core 040-057::/page/1/Text/22', 'PZO22001 Starfinder Player Core 040-057::/page/1/Text/6']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/23` | 0.979704 | **Alternate** **Ancestry** **Boosts:** Because of the wide variety of  people within any ancestry, you can *always* choose to take two  free boosts to represent your character, even if the ancestry  n |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/22` | 0.712560 | boosts to increase some attribute modifiers, and possibly  attribute flaws to decrease others (depending on the ancestry).  For more about attribute boosts and flaws, see page 23. |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/6` | 0.671160 | A character has one ancestry and one background, both of  which you select during character creation. You'll also select  a number of languages for your character. Once chosen, your  ancestry and back |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/1/ListItem/8` | 0.623060 | **Ancestries** express the lineage your character hails from.  Within ancestries are heritages—subgroups that have  unique characteristics. An ancestry provides attribute  boosts (and perhaps attribut |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/12/Text/4` | 0.591540 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As a human, you choose from among the  following anc |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/21` | 0.569344 | When creating a character of this ancestry, you apply attribute |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/31` | 0.568390 | You select a heritage at 1st level to reflect abilities common  among those of your ancestry in the environment where  you were born or grew up. You have only one heritage and  can't change it later. |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/29` | 0.567525 | Any other entries in the sidebar represent abilities, senses,  and other qualities all members of the ancestry manifest.  These are omitted for ancestries with no special rules. |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/34` | 0.565247 | As a starting character, you can choose from only 1stlevel ancestry feats, but later choices can be made from any  feat of your level or lower. These feats also sometimes list  prerequisites, which ar |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/33` | 0.564510 | This section presents ancestry feats, which allow you to  customize your character. You gain your first ancestry feat  at 1st level, and you gain another at 5th level, 9th level, 13th  level, and 17th |

### Query 20
- Text: Summarize LANGUAGES
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/1/SectionHeader/24']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/2/SectionHeader/8', 'PZO22001 Starfinder Player Core 040-057::/page/1/SectionHeader/24', 'PZO22001 Starfinder Player Core 040-057::/page/14/SectionHeader/10']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/2/SectionHeader/8` | 0.859840 | LANGUAGES |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/1/SectionHeader/24` | 0.859840 | LANGUAGES |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/14/SectionHeader/10` | 0.859840 | LANGUAGES |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/81` | 0.663449 | **Languages** |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/15/Text/47` | 0.663449 | **Languages** |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/9/Text/66` | 0.663449 | **Languages** |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/11/Text/44` | 0.663449 | **Languages** |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/17/Text/71` | 0.663449 | **Languages** |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/13/Text/76` | 0.663449 | **Languages** |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/45` | 0.663449 | **Languages** |

### Query 21
- Text: What is the rule about This tells you the languages that members of the ancestry  speak at 1st level. If your Intelligence modifier is +1 or higher,  you can select more languages from a list given here. More  about languages can be found on page 97.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/1/Text/25']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/1/Text/25', 'PZO22001 Starfinder Player Core 040-057::/page/2/Text/10', 'PZO22001 Starfinder Player Core 040-057::/page/10/Text/8']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/25` | 0.969372 | This tells you the languages that members of the ancestry  speak at 1st level. If your Intelligence modifier is +1 or higher,  you can select more languages from a list given here. More  about languag |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/2/Text/10` | 0.787782 | Additional languages equal to 1 + your Intelligence modifier (if it's positive). Choose from the list of common languages and any other languages to which you have access (such as the languages preval |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/10/Text/8` | 0.787318 | Additional languages equal to 1 + your Intelligence modifier (if it's positive). Choose from the list of common languages and any other languages to which you have access (such as the languages preval |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/6/Text/11` | 0.733272 | Additional languages equal to your Intelligence  modifier (if it's positive). Choose from the list  of common languages and any other languages  to which you have access (such as the languages  preval |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/14/Text/13` | 0.731708 | Additional languages equal to your Intelligence modifier (if it's positive). Choose from the list of common languages and any other languages to which you have access (such as the languages prevalent |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/6` | 0.620312 | A character has one ancestry and one background, both of  which you select during character creation. You'll also select  a number of languages for your character. Once chosen, your  ancestry and back |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/31` | 0.605655 | You select a heritage at 1st level to reflect abilities common  among those of your ancestry in the environment where  you were born or grew up. You have only one heritage and  can't change it later. |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/15` | 0.573249 | This tells you how many HP your PC gains from their ancestry  at 1st level. You'll add the HP from your character's class  (including their Constitution modifier) to this number. For more  on calculat |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/34` | 0.572128 | As a starting character, you can choose from only 1stlevel ancestry feats, but later choices can be made from any  feat of your level or lower. These feats also sometimes list  prerequisites, which ar |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/12/Text/4` | 0.565804 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As a human, you choose from among the  following anc |

### Query 22
- Text: What is the rule about TRAITS?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/1/SectionHeader/26']
- Expected found: `True`
- Expected rank: `5`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/10/SectionHeader/9', 'PZO22001 Starfinder Player Core 040-057::/page/6/SectionHeader/12', 'PZO22001 Starfinder Player Core 040-057::/page/2/SectionHeader/11']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/10/SectionHeader/9` | 0.800446 | TRAITS |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/6/SectionHeader/12` | 0.800446 | TRAITS |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/2/SectionHeader/11` | 0.800446 | TRAITS |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/14/SectionHeader/14` | 0.770446 | TRAITS |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/1/SectionHeader/26` | 0.770446 | TRAITS |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/1/ListItem/8` | 0.424186 | **Ancestries** express the lineage your character hails from.  Within ancestries are heritages—subgroups that have  unique characteristics. An ancestry provides attribute  boosts (and perhaps attribut |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/31` | 0.422797 | You select a heritage at 1st level to reflect abilities common  among those of your ancestry in the environment where  you were born or grew up. You have only one heritage and  can't change it later. |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/34` | 0.404170 | As a starting character, you can choose from only 1stlevel ancestry feats, but later choices can be made from any  feat of your level or lower. These feats also sometimes list  prerequisites, which ar |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/29` | 0.402900 | Any other entries in the sidebar represent abilities, senses,  and other qualities all members of the ancestry manifest.  These are omitted for ancestries with no special rules. |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/9/ListItem/41` | 0.402577 | You occupy the target's space and can't take actions  with the move trait. If the target moves, you move with  them. |

### Query 23
- Text: What is the rule about These descriptors have no mechanical benefit, but they're  important for determining how certain spells, effects, and  other aspects of the game interact with your character.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/1/Text/27']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/1/Text/27', 'PZO22001 Starfinder Player Core 040-057::/page/12/Text/25', 'PZO22001 Starfinder Player Core 040-057::/page/1/ListItem/8']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/27` | 0.983290 | These descriptors have no mechanical benefit, but they're  important for determining how certain spells, effects, and  other aspects of the game interact with your character. |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/12/Text/25` | 0.526370 | Your adaptability manifests in your mastery of a range of  useful abilities. You gain a 1st-level general feat. You must  meet the feat's prerequisites, but if you select this feat during  character c |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/1/ListItem/8` | 0.506685 | **Ancestries** express the lineage your character hails from.  Within ancestries are heritages—subgroups that have  unique characteristics. An ancestry provides attribute  boosts (and perhaps attribut |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/5/ListItem/62` | 0.460375 | You can't speak, Cast Spells, use manipulate actions  requiring your hands, Activate magic items, or make any  Strikes with your normal body. |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/22` | 0.459079 | boosts to increase some attribute modifiers, and possibly  attribute flaws to decrease others (depending on the ancestry).  For more about attribute boosts and flaws, see page 23. |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/17/Text/5` | 0.458783 | **Trigger** You fail an Acrobatics check or Reflex saving throw. You have an almost supernatural control of your movements,  which can sometimes save you in dangerous situations. You  can reroll the t |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/13/Text/1` | 0.448736 | ysoki) or that's common in another culture. You gain access  to that weapon, and for the purpose of proficiency, you treat  it as a simple weapon. |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/9/Text/2` | 0.446421 | Your anatomy adjusts to distribute damage from vital areas.  The triggering attack deals only the damage it would deal on a  hit (typically normal damage instead of double damage). Any  other effects |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/17/Text/43` | 0.441227 | **Redirect** **Energy** [reaction] **Trigger** You take cold damage or fire  damage and are holding a melee weapon; **Effect** You tap  into the harmful energy directed at you and redirect its  essenc |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/14/Text/18` | 0.441019 | weapons and equipment. At any time, one pair of hands is designated as your active hands. You can change this designation from one pair of hands to another by taking the Switch Hands action, which is |

### Query 24
- Text: Summarize SPECIAL ABILITIES
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/1/SectionHeader/28']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/1/SectionHeader/28', 'PZO22001 Starfinder Player Core 040-057::/page/12/Text/25', 'PZO22001 Starfinder Player Core 040-057::/page/1/Text/53']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/1/SectionHeader/28` | 0.982729 | SPECIAL ABILITIES |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/12/Text/25` | 0.437590 | Your adaptability manifests in your mastery of a range of  useful abilities. You gain a 1st-level general feat. You must  meet the feat's prerequisites, but if you select this feat during  character c |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/53` | 0.432466 | **SKILLS** |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/13/Text/78` | 0.390466 | **SKILLS** |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/83` | 0.390466 | **SKILLS** |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/17/Text/73` | 0.390466 | **SKILLS** |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/11/Text/46` | 0.383939 | **SKILLS** **FEATS** |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/9/Text/68` | 0.383939 | **SKILLS** **FEATS** |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/15/Text/49` | 0.383939 | **SKILLS** **FEATS** |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/7/Text/47` | 0.383939 | **SKILLS** **FEATS** |

### Query 25
- Text: Summarize Any other entries in the sidebar represent abilities, senses,  and other qualities all members of the ancestry manifest.  These are omitted for ancestries with no special rules.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/1/Text/29']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/1/Text/29', 'PZO22001 Starfinder Player Core 040-057::/page/1/ListItem/8', 'PZO22001 Starfinder Player Core 040-057::/page/1/Text/13']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/29` | 1.040491 | Any other entries in the sidebar represent abilities, senses,  and other qualities all members of the ancestry manifest.  These are omitted for ancestries with no special rules. |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/1/ListItem/8` | 0.694440 | **Ancestries** express the lineage your character hails from.  Within ancestries are heritages—subgroups that have  unique characteristics. An ancestry provides attribute  boosts (and perhaps attribut |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/13` | 0.682570 | Each entry includes details about the ancestry and presents  the rules elements described below. |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/1/ListItem/9` | 0.573164 | **Versatile** **heritages**, starting on page 82, are heritage  options available to all ancestries for extra customization,  such as characters with more unique or unusual origins.  These are selecte |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/23` | 0.572285 | **Alternate** **Ancestry** **Boosts:** Because of the wide variety of  people within any ancestry, you can *always* choose to take two  free boosts to represent your character, even if the ancestry  n |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/31` | 0.568771 | You select a heritage at 1st level to reflect abilities common  among those of your ancestry in the environment where  you were born or grew up. You have only one heritage and  can't change it later. |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/21` | 0.550763 | When creating a character of this ancestry, you apply attribute |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/22` | 0.545607 | boosts to increase some attribute modifiers, and possibly  attribute flaws to decrease others (depending on the ancestry).  For more about attribute boosts and flaws, see page 23. |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/25` | 0.542687 | This tells you the languages that members of the ancestry  speak at 1st level. If your Intelligence modifier is +1 or higher,  you can select more languages from a list given here. More  about languag |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/6` | 0.541028 | A character has one ancestry and one background, both of  which you select during character creation. You'll also select  a number of languages for your character. Once chosen, your  ancestry and back |

### Query 26
- Text: Summarize HERITAGES
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/1/SectionHeader/30']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/1/SectionHeader/30', 'PZO22001 Starfinder Player Core 040-057::/page/11/SectionHeader/21', 'PZO22001 Starfinder Player Core 040-057::/page/3/Text/42']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/1/SectionHeader/30` | 0.898370 | HERITAGES |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/11/SectionHeader/21` | 0.768619 | HUMAN HERITAGES |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/42` | 0.677354 | **Heritages** |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/9/Text/62` | 0.635354 | **Heritages** |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/3/SectionHeader/21` | 0.627884 | ANDROID HERITAGES |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/7/Text/41` | 0.576328 | **Versatile ** **Heritages** |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/11/Text/40` | 0.576328 | **Versatile ** **Heritages** |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/13/Text/72` | 0.576328 | **Versatile ** **Heritages** |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/48` | 0.576328 | **Versatile ** **Heritages** |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/15/Text/43` | 0.576328 | **Versatile ** **Heritages** |

### Query 27
- Text: Summarize You select a heritage at 1st level to reflect abilities common  among those of your ancestry in the environment where  you were born or grew up. You have only one heritage and  can't change it later. A heritage isn't the same as a culture  or ethnicity, though some cultures or ethnicities might have  more or fewer members from a particular heritage.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/1/Text/31']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/1/Text/31', 'PZO22001 Starfinder Player Core 040-057::/page/1/Text/6', 'PZO22001 Starfinder Player Core 040-057::/page/1/ListItem/8']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/31` | 1.040897 | You select a heritage at 1st level to reflect abilities common  among those of your ancestry in the environment where  you were born or grew up. You have only one heritage and  can't change it later. |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/6` | 0.684375 | A character has one ancestry and one background, both of  which you select during character creation. You'll also select  a number of languages for your character. Once chosen, your  ancestry and back |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/1/ListItem/8` | 0.674553 | **Ancestries** express the lineage your character hails from.  Within ancestries are heritages—subgroups that have  unique characteristics. An ancestry provides attribute  boosts (and perhaps attribut |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/11/Text/22` | 0.624220 | Humans don't have significant physiological differences  defined by their lineage. Instead, their heritages reveal their  potential as a people. In many cases, these heritages might  represent offshoo |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/25` | 0.613805 | This tells you the languages that members of the ancestry  speak at 1st level. If your Intelligence modifier is +1 or higher,  you can select more languages from a list given here. More  about languag |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/12/Text/4` | 0.612498 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As a human, you choose from among the  following anc |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/34` | 0.611070 | As a starting character, you can choose from only 1stlevel ancestry feats, but later choices can be made from any  feat of your level or lower. These feats also sometimes list  prerequisites, which ar |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/15/Text/23` | 0.590213 | A kasatha's heritage might be influenced by the environs their  ancestors inhabited on Kasath, the lineage they were born into,  or their progenitors' role in their peoples' interstellar migration.  C |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/1/ListItem/9` | 0.567845 | **Versatile** **heritages**, starting on page 82, are heritage  options available to all ancestries for extra customization,  such as characters with more unique or unusual origins.  These are selecte |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/29` | 0.562188 | Any other entries in the sidebar represent abilities, senses,  and other qualities all members of the ancestry manifest.  These are omitted for ancestries with no special rules. |

### Query 28
- Text: What is the rule about ANCESTRY FEATS?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/1/SectionHeader/32']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/1/SectionHeader/32', 'PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/3', 'PZO22001 Starfinder Player Core 040-057::/page/4/SectionHeader/4']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/1/SectionHeader/32` | 0.898806 | ANCESTRY FEATS |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/3` | 0.797330 | HUMAN ANCESTRY FEATS |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/4/SectionHeader/4` | 0.756674 | ANDROID ANCESTRY  FEATS |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/16/SectionHeader/6` | 0.685057 | KASATHA ANCESTRY  FEATS |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/8/SectionHeader/3` | 0.676826 | BARATHU ANCESTRY  FEATS |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/1/SectionHeader/12` | 0.559981 | ANCESTRY ENTRIES |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/12/Text/4` | 0.519831 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As a human, you choose from among the  following anc |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/4/Text/5` | 0.469398 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As an android, you choose from among  the following |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/8/Text/4` | 0.465860 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th,  9th, 13th, and 17th level). As a barathu, you choose from  among the following a |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/33` | 0.465065 | This section presents ancestry feats, which allow you to  customize your character. You gain your first ancestry feat  at 1st level, and you gain another at 5th level, 9th level, 13th  level, and 17th |

### Query 29
- Text: What is the rule about This section presents ancestry feats, which allow you to  customize your character. You gain your first ancestry feat  at 1st level, and you gain another at 5th level, 9th level, 13th  level, and 17th level, as indicated in the class advancement  table in the descriptions of each class.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/1/Text/33']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/1/Text/33', 'PZO22001 Starfinder Player Core 040-057::/page/12/Text/4', 'PZO22001 Starfinder Player Core 040-057::/page/4/Text/5']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/33` | 0.950707 | This section presents ancestry feats, which allow you to  customize your character. You gain your first ancestry feat  at 1st level, and you gain another at 5th level, 9th level, 13th  level, and 17th |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/12/Text/4` | 0.870132 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As a human, you choose from among the  following anc |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/4/Text/5` | 0.793643 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As an android, you choose from among  the following |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/34` | 0.755569 | As a starting character, you can choose from only 1stlevel ancestry feats, but later choices can be made from any  feat of your level or lower. These feats also sometimes list  prerequisites, which ar |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/8/Text/4` | 0.744884 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th,  9th, 13th, and 17th level). As a barathu, you choose from  among the following a |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/16/Text/7` | 0.726938 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As a kasatha, you choose from among  the following a |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/15` | 0.625778 | This tells you how many HP your PC gains from their ancestry  at 1st level. You'll add the HP from your character's class  (including their Constitution modifier) to this number. For more  on calculat |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/9/Text/18` | 0.622132 | You sample the genetics of creatures and people you've  made contact with and mimic them. When you take this feat,  select up to three different ancestries with which you've had  significant contact. |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/9/Text/48` | 0.616082 | You've cataloged the genetic code from countless ancestries  you've encountered, and you can draw upon any of them  to enhance and evolve your body. Increase the number of  ancestries you can select w |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/12/Text/25` | 0.610409 | Your adaptability manifests in your mastery of a range of  useful abilities. You gain a 1st-level general feat. You must  meet the feat's prerequisites, but if you select this feat during  character c |

### Query 30
- Text: What is the rule about As a starting character, you can choose from only 1stlevel ancestry feats, but later choices can be made from any  feat of your level or lower. These feats also sometimes list  prerequisites, which are conditions that your character must  fulfill to select that feat.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/1/Text/34']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/1/Text/34', 'PZO22001 Starfinder Player Core 040-057::/page/12/Text/4', 'PZO22001 Starfinder Player Core 040-057::/page/1/Text/33']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/34` | 0.997665 | As a starting character, you can choose from only 1stlevel ancestry feats, but later choices can be made from any  feat of your level or lower. These feats also sometimes list  prerequisites, which ar |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/12/Text/4` | 0.768001 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As a human, you choose from among the  following anc |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/33` | 0.748110 | This section presents ancestry feats, which allow you to  customize your character. You gain your first ancestry feat  at 1st level, and you gain another at 5th level, 9th level, 13th  level, and 17th |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/12/Text/25` | 0.674044 | Your adaptability manifests in your mastery of a range of  useful abilities. You gain a 1st-level general feat. You must  meet the feat's prerequisites, but if you select this feat during  character c |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/6` | 0.654155 | A character has one ancestry and one background, both of  which you select during character creation. You'll also select  a number of languages for your character. Once chosen, your  ancestry and back |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/4/Text/5` | 0.650552 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As an android, you choose from among  the following |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/8/Text/4` | 0.645613 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th,  9th, 13th, and 17th level). As a barathu, you choose from  among the following a |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/16/Text/7` | 0.625395 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As a kasatha, you choose from among  the following a |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/12/Text/30` | 0.613049 | You were raised to be ambitious and always reach for the  stars, leading you to progress quickly in your chosen field. You  gain a 1st-level class feat for your class. You must meet the  prerequisites |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/9/Text/18` | 0.609423 | You sample the genetics of creatures and people you've  made contact with and mimic them. When you take this feat,  select up to three different ancestries with which you've had  significant contact. |

### Query 31
- Text: Summarize **INTRODUCTION**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/1/Text/36']
- Expected found: `True`
- Expected rank: `8`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/9/Text/50', 'PZO22001 Starfinder Player Core 040-057::/page/11/Text/30', 'PZO22001 Starfinder Player Core 040-057::/page/7/Text/30']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/9/Text/50` | 0.880541 | **INTRODUCTION** |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/11/Text/30` | 0.880541 | **INTRODUCTION** |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/7/Text/30` | 0.880541 | **INTRODUCTION** |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/15/Text/31` | 0.838541 | **INTRODUCTION** |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/17/Text/55` | 0.838541 | **INTRODUCTION** |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/13/Text/61` | 0.838541 | **INTRODUCTION** |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/65` | 0.838541 | **INTRODUCTION** |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/36` | 0.838541 | **INTRODUCTION** |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/30` | 0.838541 | **INTRODUCTION** |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/81` | 0.460996 | **Languages** |

### Query 32
- Text: What is the rule about **ANCESTRIES & ** **BACKGROUNDS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/1/Text/37']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/1/Text/37', 'PZO22001 Starfinder Player Core 040-057::/page/17/Text/56', 'PZO22001 Starfinder Player Core 040-057::/page/3/Text/31']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/37` | 0.920820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/17/Text/56` | 0.920820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/31` | 0.920820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/66` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/7/Text/31` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/15/Text/32` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/9/Text/51` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/13/Text/62` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/11/Text/31` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/1/SectionHeader/1` | 0.795553 | CHAPTER 2: ANCESTRIES &  BACKGROUNDS |

### Query 33
- Text: Summarize **Android**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/1/Text/38']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/1/Text/38', 'PZO22001 Starfinder Player Core 040-057::/page/5/Text/67', 'PZO22001 Starfinder Player Core 040-057::/page/11/Text/32']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/38` | 0.780963 | **Android** |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/67` | 0.780963 | **Android** |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/11/Text/32` | 0.780963 | **Android** |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/7/Text/32` | 0.738963 | **Android** |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/9/Text/52` | 0.738963 | **Android** |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/32` | 0.738963 | **Android** |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/13/Text/63` | 0.738963 | **Android** |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/17/Text/57` | 0.738963 | **Android** |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/15/Text/33` | 0.738963 | **Android** |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/4` | 0.610088 | **ANDROID** |

### Query 34
- Text: Summarize **Barathu**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/1/Text/39']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/1/Text/39', 'PZO22001 Starfinder Player Core 040-057::/page/17/Text/58', 'PZO22001 Starfinder Player Core 040-057::/page/3/Text/33']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/39` | 0.983851 | **Barathu** |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/17/Text/58` | 0.983851 | **Barathu** |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/33` | 0.983851 | **Barathu** |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/68` | 0.941851 | **Barathu** |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/7/Text/33` | 0.941851 | **Barathu** |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/9/Text/53` | 0.941851 | **Barathu** |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/15/Text/34` | 0.941851 | **Barathu** |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/13/Text/64` | 0.842102 | **Barathu** **Human** |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/11/Text/33` | 0.842102 | **Barathu** **Human** |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/6/SectionHeader/1` | 0.785783 | BARATHU |

### Query 35
- Text: Summarize **Human**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/1/Text/40']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/1/Text/40', 'PZO22001 Starfinder Player Core 040-057::/page/17/Text/59', 'PZO22001 Starfinder Player Core 040-057::/page/3/Text/34']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/40` | 0.918191 | **Human** |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/17/Text/59` | 0.918191 | **Human** |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/34` | 0.918191 | **Human** |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/69` | 0.876191 | **Human** |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/15/Text/35` | 0.876191 | **Human** |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/9/Text/54` | 0.876191 | **Human** |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/7/Text/34` | 0.876191 | **Human** |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/12/Text/8` | 0.796262 | **HUMAN** |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/12/Text/29` | 0.796262 | **HUMAN** |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/12/Text/37` | 0.796262 | **HUMAN** |

### Query 36
- Text: Summarize **Kasatha**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/1/Text/41']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/1/Text/41', 'PZO22001 Starfinder Player Core 040-057::/page/17/Text/60', 'PZO22001 Starfinder Player Core 040-057::/page/3/Text/35']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/41` | 0.982519 | **Kasatha** |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/17/Text/60` | 0.982519 | **Kasatha** |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/35` | 0.982519 | **Kasatha** |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/70` | 0.940519 | **Kasatha** |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/7/Text/35` | 0.940519 | **Kasatha** |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/9/Text/55` | 0.940519 | **Kasatha** |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/11/Text/34` | 0.940519 | **Kasatha** |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/15/Text/36` | 0.940519 | **Kasatha** |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/13/Text/65` | 0.940519 | **Kasatha** |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/14/Text/11` | 0.827868 | Common, Kasatha |

### Query 37
- Text: Summarize **Lashunta**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/1/Text/42']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/1/Text/42', 'PZO22001 Starfinder Player Core 040-057::/page/17/Text/61', 'PZO22001 Starfinder Player Core 040-057::/page/5/Text/71']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/42` | 0.972315 | **Lashunta** |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/17/Text/61` | 0.972315 | **Lashunta** |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/71` | 0.972315 | **Lashunta** |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/36` | 0.930315 | **Lashunta** |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/11/Text/35` | 0.930315 | **Lashunta** |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/15/Text/37` | 0.930315 | **Lashunta** |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/9/Text/56` | 0.930315 | **Lashunta** |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/7/Text/36` | 0.930315 | **Lashunta** |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/13/Text/66` | 0.930315 | **Lashunta** |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/37` | 0.356718 | **Pahtra** **Shirren** |

### Query 38
- Text: Summarize **Pahtra**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/1/Text/43']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/1/Text/43', 'PZO22001 Starfinder Player Core 040-057::/page/9/Text/57', 'PZO22001 Starfinder Player Core 040-057::/page/7/Text/37']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/43` | 0.983397 | **Pahtra** |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/9/Text/57` | 0.983397 | **Pahtra** |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/7/Text/37` | 0.983397 | **Pahtra** |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/17/Text/62` | 0.941397 | **Pahtra** |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/72` | 0.941397 | **Pahtra** |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/15/Text/38` | 0.941397 | **Pahtra** |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/13/Text/67` | 0.941397 | **Pahtra** |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/11/Text/36` | 0.774525 | **Pahtra** **Shirren** |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/37` | 0.774525 | **Pahtra** **Shirren** |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/8/SectionHeader/36` | 0.443282 | **BARATHU** |

### Query 39
- Text: Summarize **Shirren**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/1/Text/44']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/1/Text/44', 'PZO22001 Starfinder Player Core 040-057::/page/5/Text/73', 'PZO22001 Starfinder Player Core 040-057::/page/17/Text/63']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/44` | 0.983425 | **Shirren** |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/73` | 0.983425 | **Shirren** |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/17/Text/63` | 0.983425 | **Shirren** |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/15/Text/39` | 0.941425 | **Shirren** |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/13/Text/68` | 0.941425 | **Shirren** |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/9/Text/58` | 0.772777 | **Shirren** **Skittermander** |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/7/Text/38` | 0.772777 | **Shirren** **Skittermander** |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/11/Text/36` | 0.731976 | **Pahtra** **Shirren** |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/37` | 0.731976 | **Pahtra** **Shirren** |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/42` | 0.312734 | **Heritages** |

### Query 40
- Text: Summarize **Skittermander**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/1/Text/45']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/11/Text/37', 'PZO22001 Starfinder Player Core 040-057::/page/3/Text/38', 'PZO22001 Starfinder Player Core 040-057::/page/1/Text/45']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/11/Text/37` | 0.984124 | **Skittermander** |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/38` | 0.984124 | **Skittermander** |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/45` | 0.984124 | **Skittermander** |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/15/Text/40` | 0.942124 | **Skittermander** |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/74` | 0.942124 | **Skittermander** |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/13/Text/69` | 0.942124 | **Skittermander** |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/17/Text/64` | 0.942124 | **Skittermander** |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/9/Text/58` | 0.746064 | **Shirren** **Skittermander** |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/7/Text/38` | 0.746064 | **Shirren** **Skittermander** |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/8/SectionHeader/20` | 0.358654 | **DERMAL SPIKES** **FEAT 1** |

### Query 41
- Text: Summarize **Vesk**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/1/Text/46']
- Expected found: `True`
- Expected rank: `9`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/15/Text/41', 'PZO22001 Starfinder Player Core 040-057::/page/11/Text/38', 'PZO22001 Starfinder Player Core 040-057::/page/17/Text/65']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/15/Text/41` | 0.943397 | **Vesk** |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/11/Text/38` | 0.943397 | **Vesk** |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/17/Text/65` | 0.943397 | **Vesk** |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/9/Text/59` | 0.901397 | **Vesk** |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/13/Text/70` | 0.901397 | **Vesk** |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/75` | 0.901397 | **Vesk** |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/39` | 0.901397 | **Vesk** |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/7/Text/39` | 0.901397 | **Vesk** |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/46` | 0.901397 | **Vesk** |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/12/Text/38` | 0.413352 | You've familiarized yourself with a particular weapon,  potentially from another ancestry or culture. Choose  an uncommon simple or martial weapon with a trait  corresponding to an ancestry (such as k |

### Query 42
- Text: Summarize **Ysoki**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/1/Text/47']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/17/Text/66', 'PZO22001 Starfinder Player Core 040-057::/page/1/Text/47', 'PZO22001 Starfinder Player Core 040-057::/page/5/Text/76']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/17/Text/66` | 0.934336 | **Ysoki** |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/47` | 0.934336 | **Ysoki** |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/76` | 0.934336 | **Ysoki** |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/7/Text/40` | 0.892336 | **Ysoki** |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/9/Text/60` | 0.892336 | **Ysoki** |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/11/Text/39` | 0.892336 | **Ysoki** |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/13/Text/71` | 0.892336 | **Ysoki** |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/15/Text/42` | 0.892336 | **Ysoki** |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/40` | 0.892336 | **Ysoki** |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/13/Text/1` | 0.426633 | ysoki) or that's common in another culture. You gain access  to that weapon, and for the purpose of proficiency, you treat  it as a simple weapon. |

### Query 43
- Text: Summarize **Versatile ** **Heritages**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/1/Text/48']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/13/Text/72', 'PZO22001 Starfinder Player Core 040-057::/page/1/Text/48', 'PZO22001 Starfinder Player Core 040-057::/page/11/Text/40']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/13/Text/72` | 0.959353 | **Versatile ** **Heritages** |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/48` | 0.959353 | **Versatile ** **Heritages** |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/11/Text/40` | 0.959353 | **Versatile ** **Heritages** |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/7/Text/41` | 0.917353 | **Versatile ** **Heritages** |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/77` | 0.917353 | **Versatile ** **Heritages** |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/15/Text/43` | 0.917353 | **Versatile ** **Heritages** |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/42` | 0.753445 | **Heritages** |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/9/Text/62` | 0.753445 | **Heritages** |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/1/ListItem/9` | 0.670254 | **Versatile** **heritages**, starting on page 82, are heritage  options available to all ancestries for extra customization,  such as characters with more unique or unusual origins.  These are selecte |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/9/Text/61` | 0.628755 | **Versatile ** |

### Query 44
- Text: Summarize **Borai**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/1/Text/49']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/1/Text/49', 'PZO22001 Starfinder Player Core 040-057::/page/11/Text/41', 'PZO22001 Starfinder Player Core 040-057::/page/13/Text/73']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/49` | 0.983112 | **Borai** |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/13/Text/73` | 0.983112 | **Borai** |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/11/Text/41` | 0.983112 | **Borai** |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/78` | 0.941112 | **Borai** |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/7/Text/42` | 0.941112 | **Borai** |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/15/Text/44` | 0.941112 | **Borai** |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/17/Text/68` | 0.857213 | **Heritages** **Borai** |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/43` | 0.728343 | **Borai** **Prismeni** |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/9/Text/63` | 0.728343 | **Borai** **Prismeni** |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/39` | 0.447974 | **Barathu** |

### Query 45
- Text: Summarize **Prismeni**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/1/Text/50']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/1/Text/50', 'PZO22001 Starfinder Player Core 040-057::/page/7/Text/43', 'PZO22001 Starfinder Player Core 040-057::/page/13/Text/74']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/50` | 0.966478 | **Prismeni** |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/7/Text/43` | 0.966478 | **Prismeni** |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/13/Text/74` | 0.966478 | **Prismeni** |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/15/Text/45` | 0.924478 | **Prismeni** |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/79` | 0.924478 | **Prismeni** |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/11/Text/42` | 0.924478 | **Prismeni** |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/17/Text/69` | 0.924478 | **Prismeni** |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/9/Text/63` | 0.716730 | **Borai** **Prismeni** |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/43` | 0.716730 | **Borai** **Prismeni** |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/7/Text/38` | 0.353978 | **Shirren** **Skittermander** |

### Query 46
- Text: What is the rule about **Backgrounds**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/1/Text/51']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/1/Text/51', 'PZO22001 Starfinder Player Core 040-057::/page/5/Text/80', 'PZO22001 Starfinder Player Core 040-057::/page/3/Text/44']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/51` | 0.796516 | **Backgrounds** |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/80` | 0.796516 | **Backgrounds** |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/44` | 0.796516 | **Backgrounds** |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/7/Text/44` | 0.754516 | **Backgrounds** |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/15/Text/46` | 0.754516 | **Backgrounds** |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/9/Text/65` | 0.754516 | **Backgrounds** |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/13/Text/75` | 0.754516 | **Backgrounds** |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/11/Text/43` | 0.754516 | **Backgrounds** |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/17/Text/70` | 0.754516 | **Backgrounds** |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/1/ListItem/10` | 0.567373 | **Backgrounds**, starting on page 92, describe training  or environments your character experienced before  becoming an adventurer. Your character's background  provides attribute boosts, skill traini |

### Query 47
- Text: Summarize **Languages** **CLASSES**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/1/Text/52']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/1/Text/52', 'PZO22001 Starfinder Player Core 040-057::/page/15/Text/48', 'PZO22001 Starfinder Player Core 040-057::/page/9/Text/67']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/52` | 0.953496 | **Languages** **CLASSES** |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/15/Text/48` | 0.768334 | **CLASSES** |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/9/Text/67` | 0.768334 | **CLASSES** |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/17/Text/72` | 0.738334 | **CLASSES** |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/82` | 0.738334 | **CLASSES** |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/7/Text/46` | 0.738334 | **CLASSES** |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/46` | 0.738334 | **CLASSES** |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/13/Text/77` | 0.738334 | **CLASSES** |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/11/Text/45` | 0.738334 | **CLASSES** |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/9/Text/66` | 0.713682 | **Languages** |

### Query 48
- Text: What is the rule about **SKILLS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/1/Text/53']
- Expected found: `True`
- Expected rank: `4`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/5/Text/83', 'PZO22001 Starfinder Player Core 040-057::/page/17/Text/73', 'PZO22001 Starfinder Player Core 040-057::/page/13/Text/78']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/83` | 0.864442 | **SKILLS** |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/17/Text/73` | 0.864442 | **SKILLS** |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/13/Text/78` | 0.864442 | **SKILLS** |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/53` | 0.822442 | **SKILLS** |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/7/Text/47` | 0.651094 | **SKILLS** **FEATS** |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/11/Text/46` | 0.651094 | **SKILLS** **FEATS** |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/9/Text/68` | 0.651094 | **SKILLS** **FEATS** |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/47` | 0.651094 | **SKILLS** **FEATS** |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/15/Text/49` | 0.651094 | **SKILLS** **FEATS** |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/31` | 0.541891 | **NATURAL SKILL** **FEAT 1** |

### Query 49
- Text: What is the rule about **FEATS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/1/Text/54']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/17/Text/74', 'PZO22001 Starfinder Player Core 040-057::/page/1/Text/54', 'PZO22001 Starfinder Player Core 040-057::/page/13/Text/79']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/17/Text/74` | 0.871817 | **FEATS** |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/54` | 0.871817 | **FEATS** |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/13/Text/79` | 0.871817 | **FEATS** |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/84` | 0.829817 | **FEATS** |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/7/Text/47` | 0.653037 | **SKILLS** **FEATS** |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/47` | 0.653037 | **SKILLS** **FEATS** |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/9/Text/68` | 0.653037 | **SKILLS** **FEATS** |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/15/Text/49` | 0.653037 | **SKILLS** **FEATS** |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/11/Text/46` | 0.653037 | **SKILLS** **FEATS** |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/1/SectionHeader/32` | 0.447366 | ANCESTRY FEATS |

### Query 50
- Text: Summarize **EQUIPMENT**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/1/Text/55']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/1/Text/55', 'PZO22001 Starfinder Player Core 040-057::/page/3/Text/48', 'PZO22001 Starfinder Player Core 040-057::/page/15/Text/50']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/55` | 0.944726 | **EQUIPMENT** |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/48` | 0.944726 | **EQUIPMENT** |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/15/Text/50` | 0.944726 | **EQUIPMENT** |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/11/Text/47` | 0.902726 | **EQUIPMENT** |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/7/Text/48` | 0.902726 | **EQUIPMENT** |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/9/Text/69` | 0.902726 | **EQUIPMENT** |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/85` | 0.578761 | **EQUIPMENT** **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/13/Text/80` | 0.578761 | **EQUIPMENT** **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/17/Text/75` | 0.578761 | **EQUIPMENT** **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/7/Text/30` | 0.385549 | **INTRODUCTION** |

### Query 51
- Text: What is the rule about **SPELLS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/1/Text/56']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/9/Text/70', 'PZO22001 Starfinder Player Core 040-057::/page/1/Text/56', 'PZO22001 Starfinder Player Core 040-057::/page/15/Text/51']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/9/Text/70` | 0.889304 | **SPELLS** |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/56` | 0.889304 | **SPELLS** |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/15/Text/51` | 0.889304 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/49` | 0.847304 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/11/Text/48` | 0.847304 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/7/Text/49` | 0.847304 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/13/Text/80` | 0.759411 | **EQUIPMENT** **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/85` | 0.759411 | **EQUIPMENT** **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/17/Text/75` | 0.759411 | **EQUIPMENT** **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/17/Text/73` | 0.388254 | **SKILLS** |

### Query 52
- Text: Summarize **PLAYING THE ** **GAME**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/1/Text/57']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/1/Text/57', 'PZO22001 Starfinder Player Core 040-057::/page/3/Text/50', 'PZO22001 Starfinder Player Core 040-057::/page/9/Text/71']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/57` | 0.965000 | **PLAYING THE ** **GAME** |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/50` | 0.965000 | **PLAYING THE ** **GAME** |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/9/Text/71` | 0.965000 | **PLAYING THE ** **GAME** |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/13/Text/81` | 0.923000 | **PLAYING THE ** **GAME** |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/86` | 0.923000 | **PLAYING THE ** **GAME** |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/11/Text/49` | 0.923000 | **PLAYING THE ** **GAME** |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/7/Text/50` | 0.923000 | **PLAYING THE ** **GAME** |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/15/Text/52` | 0.923000 | **PLAYING THE ** **GAME** |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/17/Text/76` | 0.811006 | **PLAYING THE ** |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/17/Text/81` | 0.663024 | **GAME** |

### Query 53
- Text: Summarize **CONDITIONS ** **APPENDIX**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/1/Text/58']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/11/Text/50', 'PZO22001 Starfinder Player Core 040-057::/page/9/Text/72', 'PZO22001 Starfinder Player Core 040-057::/page/1/Text/58']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/11/Text/50` | 0.983499 | **CONDITIONS ** **APPENDIX** |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/9/Text/72` | 0.983499 | **CONDITIONS ** **APPENDIX** |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/58` | 0.983499 | **CONDITIONS ** **APPENDIX** |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/15/Text/53` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/13/Text/82` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/51` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/7/Text/51` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/87` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/17/Text/77` | 0.645203 | **CONDITIONS ** |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/17/Text/78` | 0.576258 | **APPENDIX** **GLOSSARY & ** **INDEX** |

### Query 54
- Text: Summarize **GLOSSARY & ** **INDEX**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/1/Text/59']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/3/Text/52', 'PZO22001 Starfinder Player Core 040-057::/page/1/Text/59', 'PZO22001 Starfinder Player Core 040-057::/page/5/Text/88']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/52` | 0.993465 | **GLOSSARY & ** **INDEX** |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/59` | 0.993465 | **GLOSSARY & ** **INDEX** |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/88` | 0.993465 | **GLOSSARY & ** **INDEX** |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/15/Text/54` | 0.951465 | **GLOSSARY & ** **INDEX** |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/9/Text/73` | 0.951465 | **GLOSSARY & ** **INDEX** |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/13/Text/83` | 0.951465 | **GLOSSARY & ** **INDEX** |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/11/Text/51` | 0.951465 | **GLOSSARY & ** **INDEX** |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/7/Text/52` | 0.951465 | **GLOSSARY & ** **INDEX** |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/17/Text/78` | 0.856301 | **APPENDIX** **GLOSSARY & ** **INDEX** |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/52` | 0.398029 | **Languages** **CLASSES** |

### Query 55
- Text: Summarize STARFINDER
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/2/SectionHeader/0']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/10/SectionHeader/0', 'PZO22001 Starfinder Player Core 040-057::/page/2/SectionHeader/0', 'PZO22001 Starfinder Player Core 040-057::/page/14/Text/0']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/10/SectionHeader/0` | 0.949716 | STARFINDER |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/2/SectionHeader/0` | 0.949716 | STARFINDER |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/14/Text/0` | 0.885572 | **STARFINDER ** |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/2` | 0.528668 | Starfinder contains as many species as there are stars in the sky. This section details a wide variety of  new and updated ancestries that are prevalent in the Starfinder setting. It also provides det |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/9/Text/58` | 0.336935 | **Shirren** **Skittermander** |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/7/Text/38` | 0.336935 | **Shirren** **Skittermander** |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/15/Text/40` | 0.302397 | **Skittermander** |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/11/Text/37` | 0.302397 | **Skittermander** |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/45` | 0.302397 | **Skittermander** |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/74` | 0.302397 | **Skittermander** |

### Query 56
- Text: Summarize ANDROID
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/2/SectionHeader/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/2/SectionHeader/1', 'PZO22001 Starfinder Player Core 040-057::/page/5/Text/39', 'PZO22001 Starfinder Player Core 040-057::/page/5/Text/45']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/2/SectionHeader/1` | 0.861453 | ANDROID |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/45` | 0.778598 | **ANDROID** |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/39` | 0.778598 | **ANDROID** |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/33` | 0.736598 | **ANDROID** |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/4/Text/9` | 0.736598 | **ANDROID** |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/4/Text/27` | 0.736598 | **ANDROID** |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/4` | 0.736598 | **ANDROID** |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/4/Text/36` | 0.736598 | **ANDROID** |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/8` | 0.736598 | **ANDROID** |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/4/Text/19` | 0.736598 | **ANDROID** |

### Query 57
- Text: What is the rule about Androids first emerged as synthetic beings crafted by many technologically advanced civilizations throughout the galaxy. The first androids were created by humanoid peoples in their own images, but after the technology that animated the living constructs spread, androids began displaying a fantastic diversity of forms. Androids in the Pact Worlds were originally designed as servants, but today androids and other robotic beings stand as equals to organic ancestries under the Pact. Some androids have formed their own independent communities, while most integrate seamlessly into Pact Worlds societies. Unlike many other technological constructs, androids are more than intricate synthetic organs and complex programming, and each possesses their own soul.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/2/Text/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/2/Text/2', 'PZO22001 Starfinder Player Core 040-057::/page/3/Text/12', 'PZO22001 Starfinder Player Core 040-057::/page/3/Text/9']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/2/Text/2` | 0.991131 | Androids first emerged as synthetic beings crafted by many technologically advanced civilizations throughout the galaxy. The first androids were created by humanoid peoples in their own images, but af |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/12` | 0.774945 | Androids are biomechanical constructs who typically  resemble humanoids with glowing circuitry. Most were  created in specialized birthing sites called foundries.  Older variants of androids, such as |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/9` | 0.755585 | Androids thrive in nearly any environment and exist as part  of countless cultures, meaning they can be found almost  anywhere in the galaxy. Many androids are curious about their  origins, traveling |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/14` | 0.652040 | Androids tend to be cautious when visiting new places and  meeting new people. Once comfortable, androids can form  tight bonds of friendship and kinship, adopting found families,  and choosing entire |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/17` | 0.626486 | Androids hold a variety of religious and philosophical  views, with individuals sometimes collecting beliefs and  practices through decades of lived experiences. With a  similar perspective to elves a |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/18` | 0.614768 | shorter lifespans. Many androids are patient in achieving  their goals and might create plans that span decades or  centuries, hoping they will be alive to experience the results.  Elder androids who |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/22` | 0.592201 | An android's heritage often reflects the purpose for which  they were originally created or how they've adapted their  body to best suit their present life. Choose one of the  following android herita |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/10` | 0.580756 | If you want to roleplay a synthetic character on a journey  of self-discovery, you should play an android. |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/24` | 0.541359 | Your body wasn't created in the image of a biological creature;  a powerful artificial intelligence created you to interface with  other machines. Your physiology is nearly identical to other  android |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/4/Text/5` | 0.489640 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As an android, you choose from among  the following |

### Query 58
- Text: Summarize SIZE: MEDIUM SPEED: 25 FEET
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/2/Text/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/2/Text/5', 'PZO22001 Starfinder Player Core 040-057::/page/14/Text/7', 'PZO22001 Starfinder Player Core 040-057::/page/10/Text/5']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/2/Text/5` | 1.022251 | SIZE: MEDIUM SPEED: 25 FEET |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/14/Text/7` | 1.022251 | SIZE: MEDIUM SPEED: 25 FEET |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/10/Text/5` | 1.022251 | SIZE: MEDIUM SPEED: 25 FEET |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/6/Text/7` | 0.741500 | SIZE: MEDIUM SPEED: 5 FEET (HOVER);  FLY 20 FEET |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/1/SectionHeader/18` | 0.531604 | SPEED |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/1/SectionHeader/16` | 0.391086 | SIZE |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/8/Text/9` | 0.337062 | You grow sturdy lower limbs that allow you to walk on land.  Increase your Speed to 20 feet. Additionally, you gain the  Adaptive Locomotion action. |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/13/Text/79` | 0.335293 | **FEATS** |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/84` | 0.335293 | **FEATS** |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/54` | 0.335293 | **FEATS** |

### Query 59
- Text: Summarize ATTRIBUTE BOOSTS Dexterity Intelligence Free
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/2/Text/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/2/Text/6', 'PZO22001 Starfinder Player Core 040-057::/page/6/Text/9', 'PZO22001 Starfinder Player Core 040-057::/page/14/Text/8']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/2/Text/6` | 1.014510 | ATTRIBUTE BOOSTS Dexterity Intelligence Free |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/6/Text/9` | 0.677009 | ATTRIBUTE FLAW Dexterity |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/14/Text/8` | 0.676197 | ATTRIBUTE BOOSTS Strength Wisdom Free |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/6/Text/8` | 0.638498 | ATTRIBUTE  BOOSTS Constitution Wisdom Free |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/10/Text/6` | 0.606624 | ATTRIBUTE BOOSTS Two free attribute boosts |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/1/SectionHeader/20` | 0.499498 | ATTRIBUTE BOOSTS & FLAWS |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/22` | 0.415162 | boosts to increase some attribute modifiers, and possibly  attribute flaws to decrease others (depending on the ancestry).  For more about attribute boosts and flaws, see page 23. |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/23` | 0.399824 | **Alternate** **Ancestry** **Boosts:** Because of the wide variety of  people within any ancestry, you can *always* choose to take two  free boosts to represent your character, even if the ancestry  n |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/6/Text/11` | 0.347513 | Additional languages equal to your Intelligence  modifier (if it's positive). Choose from the list  of common languages and any other languages  to which you have access (such as the languages  preval |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/14/Text/13` | 0.345909 | Additional languages equal to your Intelligence modifier (if it's positive). Choose from the list of common languages and any other languages to which you have access (such as the languages prevalent |

### Query 60
- Text: Summarize ATTRIBUTE FLAW
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/2/Text/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/2/Text/7', 'PZO22001 Starfinder Player Core 040-057::/page/14/Text/9', 'PZO22001 Starfinder Player Core 040-057::/page/1/SectionHeader/20']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/2/Text/7` | 0.704470 | ATTRIBUTE FLAW Charisma |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/14/Text/9` | 0.704470 | ATTRIBUTE FLAW Charisma |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/1/SectionHeader/20` | 0.689677 | ATTRIBUTE BOOSTS & FLAWS |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/6/Text/9` | 0.642466 | ATTRIBUTE FLAW Dexterity |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/22` | 0.464110 | boosts to increase some attribute modifiers, and possibly  attribute flaws to decrease others (depending on the ancestry).  For more about attribute boosts and flaws, see page 23. |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/10/Text/6` | 0.426385 | ATTRIBUTE BOOSTS Two free attribute boosts |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/14/Text/8` | 0.371325 | ATTRIBUTE BOOSTS Strength Wisdom Free |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/21` | 0.353932 | When creating a character of this ancestry, you apply attribute |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/13/SectionHeader/4` | 0.353762 | **ADAPTIVE ADEPT** **FEAT 5** |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/6/Text/8` | 0.346311 | ATTRIBUTE  BOOSTS Constitution Wisdom Free |

### Query 61
- Text: Summarize LANGUAGES
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/2/SectionHeader/8']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/2/SectionHeader/8', 'PZO22001 Starfinder Player Core 040-057::/page/1/SectionHeader/24', 'PZO22001 Starfinder Player Core 040-057::/page/14/SectionHeader/10']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/2/SectionHeader/8` | 0.859840 | LANGUAGES |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/1/SectionHeader/24` | 0.859840 | LANGUAGES |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/14/SectionHeader/10` | 0.859840 | LANGUAGES |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/81` | 0.663449 | **Languages** |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/15/Text/47` | 0.663449 | **Languages** |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/9/Text/66` | 0.663449 | **Languages** |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/11/Text/44` | 0.663449 | **Languages** |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/17/Text/71` | 0.663449 | **Languages** |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/13/Text/76` | 0.663449 | **Languages** |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/45` | 0.663449 | **Languages** |

### Query 62
- Text: Summarize Common
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/2/SectionHeader/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/2/SectionHeader/9', 'PZO22001 Starfinder Player Core 040-057::/page/10/SectionHeader/7', 'PZO22001 Starfinder Player Core 040-057::/page/6/SectionHeader/10']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/2/SectionHeader/9` | 0.841358 | Common |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/10/SectionHeader/7` | 0.743413 | LANGUAGES Common |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/6/SectionHeader/10` | 0.534134 | LANGUAGES Brethedan, Common |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/14/Text/11` | 0.414585 | Common, Kasatha |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/2/Text/10` | 0.347867 | Additional languages equal to 1 + your Intelligence modifier (if it's positive). Choose from the list of common languages and any other languages to which you have access (such as the languages preval |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/10/Text/8` | 0.346997 | Additional languages equal to 1 + your Intelligence modifier (if it's positive). Choose from the list of common languages and any other languages to which you have access (such as the languages preval |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/6/Text/11` | 0.328529 | Additional languages equal to your Intelligence  modifier (if it's positive). Choose from the list  of common languages and any other languages  to which you have access (such as the languages  preval |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/14/Text/13` | 0.315767 | Additional languages equal to your Intelligence modifier (if it's positive). Choose from the list of common languages and any other languages to which you have access (such as the languages prevalent |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/9/SectionHeader/35` | 0.315356 | **COMBINE **[two-actions] **FEAT 17** |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/15/Text/20` | 0.298430 | **Popular Edicts** cover your mouth in public, establish your own  customs, honor your traditions, maintain balance |

### Query 63
- Text: What is the rule about Additional languages equal to 1 + your Intelligence modifier (if it's positive). Choose from the list of common languages and any other languages to which you have access (such as the languages prevalent on your home world).?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/2/Text/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/2/Text/10', 'PZO22001 Starfinder Player Core 040-057::/page/10/Text/8', 'PZO22001 Starfinder Player Core 040-057::/page/6/Text/11']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/2/Text/10` | 0.963820 | Additional languages equal to 1 + your Intelligence modifier (if it's positive). Choose from the list of common languages and any other languages to which you have access (such as the languages preval |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/10/Text/8` | 0.963516 | Additional languages equal to 1 + your Intelligence modifier (if it's positive). Choose from the list of common languages and any other languages to which you have access (such as the languages preval |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/6/Text/11` | 0.946345 | Additional languages equal to your Intelligence  modifier (if it's positive). Choose from the list  of common languages and any other languages  to which you have access (such as the languages  preval |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/14/Text/13` | 0.903441 | Additional languages equal to your Intelligence modifier (if it's positive). Choose from the list of common languages and any other languages to which you have access (such as the languages prevalent |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/25` | 0.741868 | This tells you the languages that members of the ancestry  speak at 1st level. If your Intelligence modifier is +1 or higher,  you can select more languages from a list given here. More  about languag |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/6` | 0.560874 | A character has one ancestry and one background, both of  which you select during character creation. You'll also select  a number of languages for your character. Once chosen, your  ancestry and back |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/31` | 0.529967 | You select a heritage at 1st level to reflect abilities common  among those of your ancestry in the environment where  you were born or grew up. You have only one heritage and  can't change it later. |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/22` | 0.492414 | boosts to increase some attribute modifiers, and possibly  attribute flaws to decrease others (depending on the ancestry).  For more about attribute boosts and flaws, see page 23. |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/29` | 0.469847 | Any other entries in the sidebar represent abilities, senses,  and other qualities all members of the ancestry manifest.  These are omitted for ancestries with no special rules. |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/15` | 0.461926 | This tells you how many HP your PC gains from their ancestry  at 1st level. You'll add the HP from your character's class  (including their Constitution modifier) to this number. For more  on calculat |

### Query 64
- Text: What is the rule about TRAITS?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/2/SectionHeader/11']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/10/SectionHeader/9', 'PZO22001 Starfinder Player Core 040-057::/page/6/SectionHeader/12', 'PZO22001 Starfinder Player Core 040-057::/page/2/SectionHeader/11']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/10/SectionHeader/9` | 0.800446 | TRAITS |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/6/SectionHeader/12` | 0.800446 | TRAITS |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/2/SectionHeader/11` | 0.800446 | TRAITS |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/14/SectionHeader/14` | 0.770446 | TRAITS |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/1/SectionHeader/26` | 0.770446 | TRAITS |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/1/ListItem/8` | 0.424186 | **Ancestries** express the lineage your character hails from.  Within ancestries are heritages—subgroups that have  unique characteristics. An ancestry provides attribute  boosts (and perhaps attribut |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/31` | 0.422797 | You select a heritage at 1st level to reflect abilities common  among those of your ancestry in the environment where  you were born or grew up. You have only one heritage and  can't change it later. |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/34` | 0.404170 | As a starting character, you can choose from only 1stlevel ancestry feats, but later choices can be made from any  feat of your level or lower. These feats also sometimes list  prerequisites, which ar |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/29` | 0.402900 | Any other entries in the sidebar represent abilities, senses,  and other qualities all members of the ancestry manifest.  These are omitted for ancestries with no special rules. |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/9/ListItem/41` | 0.402577 | You occupy the target's space and can't take actions  with the move trait. If the target moves, you move with  them. |

### Query 65
- Text: Summarize ANDROID HUMANOID
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/2/Text/12']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/2/Text/12', 'PZO22001 Starfinder Player Core 040-057::/page/10/Text/10', 'PZO22001 Starfinder Player Core 040-057::/page/2/SectionHeader/1']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/2/Text/12` | 0.964402 | ANDROID HUMANOID |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/10/Text/10` | 0.756825 | HUMAN HUMANOID |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/2/SectionHeader/1` | 0.734964 | ANDROID |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/4/Text/36` | 0.605932 | **ANDROID** |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/4/Text/15` | 0.605932 | **ANDROID** |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/4/Text/32` | 0.605932 | **ANDROID** |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/4/Text/19` | 0.605932 | **ANDROID** |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/4/Text/23` | 0.605932 | **ANDROID** |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/22` | 0.605932 | **ANDROID** |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/33` | 0.605932 | **ANDROID** |

### Query 66
- Text: Summarize **LOW-LIGHT VISION **
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/2/SectionHeader/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/2/SectionHeader/13', 'PZO22001 Starfinder Player Core 040-057::/page/4/SectionHeader/30', 'PZO22001 Starfinder Player Core 040-057::/page/8/SectionHeader/16']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/2/SectionHeader/13` | 0.989287 | **LOW-LIGHT VISION ** |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/4/SectionHeader/30` | 0.473539 | **NIGHTVISION ADAPTATION** **FEAT 1** |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/8/SectionHeader/16` | 0.448456 | **DARKVISION ADAPTATION** **FEAT 1** |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/4/Text/33` | 0.403965 | The nanites in your ocular processors have adapted to  darkness, enhancing your ability to see in the dark. You gain  darkvision. |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/8/Text/19` | 0.368465 | You've explored the darkest regions of space and found ways  to adapt. You gain darkvision. |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/2/Text/14` | 0.352576 | You can see in dim light as though it were bright light, and you ignore the concealed condition due to dim light. |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/9/ListItem/43` | 0.308853 | Your body shields the target from harm, granting them  greater cover, though you don't gain cover. Your body  doesn't obscure the target's vision or block line of  sight. |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/36` | 0.302258 | **INTRODUCTION** |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/7/Text/30` | 0.302258 | **INTRODUCTION** |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/9/Text/50` | 0.302258 | **INTRODUCTION** |

### Query 67
- Text: Summarize You can see in dim light as though it were bright light, and you ignore the concealed condition due to dim light.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/2/Text/14']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/2/Text/14', 'PZO22001 Starfinder Player Core 040-057::/page/4/Text/33', 'PZO22001 Starfinder Player Core 040-057::/page/9/ListItem/43']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/2/Text/14` | 1.038897 | You can see in dim light as though it were bright light, and you ignore the concealed condition due to dim light. |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/4/Text/33` | 0.539104 | The nanites in your ocular processors have adapted to  darkness, enhancing your ability to see in the dark. You gain  darkvision. |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/9/ListItem/43` | 0.489711 | Your body shields the target from harm, granting them  greater cover, though you don't gain cover. Your body  doesn't obscure the target's vision or block line of  sight. |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/17/Text/20` | 0.391232 | Your masked face prevents others from scrutinizing your  appearance, and you've learned to leverage this uncertainty  to your advantage in social situations. While your mouth is  covered, increase the |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/2/SectionHeader/13` | 0.372702 | **LOW-LIGHT VISION ** |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/8/Text/19` | 0.355442 | You've explored the darkest regions of space and found ways  to adapt. You gain darkvision. |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/13/Text/59` | 0.345850 | You return from the brink of death, hauling yourself back  to consciousness through exhaustion and pain. If you have  the dying or unconscious conditions, you lose the dying and  unconscious condition |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/7/ListItem/8` | 0.340993 | Struggle to recognize you because of your frequently  changing appearance. |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/16/Text/12` | 0.321701 | You maintain a calm demeanor even when facing mortal  peril. When frightened, at the end of your  turn, reduce your frightened condition by  2 instead of 1. |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/5/ListItem/58` | 0.321647 | You're immune to the grabbed, prone, and restrained  conditions. |

### Query 68
- Text: Summarize CONSTRUCTED
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/2/SectionHeader/15']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/2/SectionHeader/15', 'PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/6', 'PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/12']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/2/SectionHeader/15` | 0.941252 | CONSTRUCTED |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/6` | 0.368492 | **ADAPTED AUGMENTATIONS** **FEAT 1** |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/12` | 0.360448 | **ADAPTED CANTRIP** **FEAT 1** |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/27` | 0.273033 | **ANDROID** **CONCENTRATE** |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/4/SectionHeader/34` | 0.265066 | **QUICKENED PROCESSOR** **FEAT 1** |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/7/Text/28` | 0.259479 | Your body is a living laboratory, allowing you to ingest raw  materials and refine them into useful medicines and other  products. You become trained in Crafting (or another skill of  your choice if y |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/5/SectionHeader/43` | 0.258293 | **SYNTHETIC SPEECH** **FEAT 13** |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/2/Text/16` | 0.245815 | Your synthetic body resists ailments better than that of a purely biological organism. You gain a +1 circumstance bonus to saving throws against diseases, poisons, and radiation. You always have basic |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/5/ListItem/58` | 0.244966 | You're immune to the grabbed, prone, and restrained  conditions. |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/17/Text/18` | 0.243543 | **MASKED** **FEAT 5** |

### Query 69
- Text: What is the rule about Your synthetic body resists ailments better than that of a purely biological organism. You gain a +1 circumstance bonus to saving throws against diseases, poisons, and radiation. You always have basic environmental protections (page 268).?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/2/Text/16']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/2/Text/16', 'PZO22001 Starfinder Player Core 040-057::/page/9/Text/6', 'PZO22001 Starfinder Player Core 040-057::/page/9/ListItem/43']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/2/Text/16` | 1.000759 | Your synthetic body resists ailments better than that of a purely biological organism. You gain a +1 circumstance bonus to saving throws against diseases, poisons, and radiation. You always have basic |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/9/Text/6` | 0.554991 | You modify your body's genetics to resist certain damage  types. You gain resistance to acid, bludgeoning, cold,  electricity, fire, piercing, poison, slashing, or sonic damage  equal to half your lev |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/9/ListItem/43` | 0.533105 | Your body shields the target from harm, granting them  greater cover, though you don't gain cover. Your body  doesn't obscure the target's vision or block line of  sight. |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/5/ListItem/58` | 0.454570 | You're immune to the grabbed, prone, and restrained  conditions. |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/8/Text/33` | 0.447315 | Through careful experimentation and selective adaptation,  you've manipulated your immune system and internal  chemistry to better fight off illness and infection. You gain the  Fast Recovery skill fe |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/9` | 0.444733 | You were created to fight other synthetic creatures. When  you roll a critical hit against a creature with the tech trait, the  target becomes glitching 1. |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/4/Text/3` | 0.442355 | Many souls have inhabited your synthetic body before you,  and you might incorporate a number into your name to honor  them. You might know your body's history and work toward a  goal bequeathed to yo |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/13/Text/59` | 0.428700 | You return from the brink of death, hauling yourself back  to consciousness through exhaustion and pain. If you have  the dying or unconscious conditions, you lose the dying and  unconscious condition |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/42` | 0.425869 | Your nanites are programmed to automatically revive you.  You are restored to 1 Hit Point, lose the dying and unconscious  conditions, and can act normally on this turn. You gain or  increase the woun |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/6/Text/15` | 0.422813 | You can reshape and adjust your body to adapt to  new situations. You can retrain an ancestry feat in  1 day of downtime, rather than in 1 week. You can  retrain any ancestry feat, even lineage feats. |

### Query 70
- Text: Summarize Try to avoid others taking advantage of you.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/3/ListItem/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/3/ListItem/2', 'PZO22001 Starfinder Player Core 040-057::/page/11/ListItem/4', 'PZO22001 Starfinder Player Core 040-057::/page/11/ListItem/2']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/3/ListItem/2` | 0.999861 | Try to avoid others taking advantage of you. |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/11/ListItem/4` | 0.496704 | Cherish your relationships with family and friends. |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/11/ListItem/2` | 0.493132 | Strive to achieve greatness, either for personal gain or  on behalf of a cause. |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/11/ListItem/7` | 0.443423 | Distrust your motivations, fearing you seek only  power or wealth. |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/5/ListItem/60` | 0.425455 | You can occupy the same space as other creatures and  must do so to use your damaging ability. |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/15/ListItem/7` | 0.423125 | Go to you for advice and expect you to provide  guidance and wisdom. |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/52` | 0.417929 | You refuse to surrender your autonomy and have erected  mental bulwarks and technological protocols to safeguard  your mind and memories. Whenever you attempt a Will save  against a spell or effect th |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/15/Text/20` | 0.415649 | **Popular Edicts** cover your mouth in public, establish your own  customs, honor your traditions, maintain balance |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/13/Text/17` | 0.412859 | Your utter confidence in your own abilities helps you push  yourself to reach your desired goals. Roll the triggering check  or save twice and use the better result. |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/17/Text/20` | 0.400551 | Your masked face prevents others from scrutinizing your  appearance, and you've learned to leverage this uncertainty  to your advantage in social situations. While your mouth is  covered, increase the |

### Query 71
- Text: Summarize Seek to understand your purpose in the wider galaxy.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/3/ListItem/3']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/3/ListItem/3', 'PZO22001 Starfinder Player Core 040-057::/page/1/ListItem/11', 'PZO22001 Starfinder Player Core 040-057::/page/15/ListItem/2']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/3/ListItem/3` | 1.012806 | Seek to understand your purpose in the wider galaxy. |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/1/ListItem/11` | 0.570314 | **Languages**, starting on page 97, let your character  communicate with people and creatures of the galaxy. |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/15/ListItem/2` | 0.557831 | Seek to maintain balance and harmony between  yourself and others, as well as among cosmic forces. |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/8/Text/19` | 0.509091 | You've explored the darkest regions of space and found ways  to adapt. You gain darkvision. |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/11/ListItem/3` | 0.500131 | Yearn to explore and experience the cosmos. |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/16/Text/3` | 0.490481 | You choose to travel abroad, leaving your birthplace to  embark on a journey through the wider cosmos. During  your daily preparations, you can study a particular ancestry,  faction, philosophy, or re |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/9` | 0.464284 | Androids thrive in nearly any environment and exist as part  of countless cultures, meaning they can be found almost  anywhere in the galaxy. Many androids are curious about their  origins, traveling |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/10/Text/2` | 0.458504 | Humans are known for their ability to adapt and thrive in the most challenging situations, including the mysterious loss of their home world, Golarion. Ambitious, creative, and endlessly curious, huma |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/11/Text/19` | 0.448480 | **Popular Edicts** devote yourself to a greater cause, explore the  cosmos, strive for greatness |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/12/Text/30` | 0.437404 | You were raised to be ambitious and always reach for the  stars, leading you to progress quickly in your chosen field. You  gain a 1st-level class feat for your class. You must meet the  prerequisites |

### Query 72
- Text: Summarize Judge others based on how they treat service workers,  blue-collar laborers, fans, or pets.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/3/ListItem/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/3/ListItem/4', 'PZO22001 Starfinder Player Core 040-057::/page/3/ListItem/8', 'PZO22001 Starfinder Player Core 040-057::/page/15/Text/21']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/3/ListItem/4` | 1.032502 | Judge others based on how they treat service workers,  blue-collar laborers, fans, or pets. |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/3/ListItem/8` | 0.486242 | Have some level of guilt for their ancestors' use of  your species as laborers. |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/15/Text/21` | 0.389324 | **Popular Anathema** disrespect or belittle the traditions of  others, disrespect your elders |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/15/Text/20` | 0.351484 | **Popular Edicts** cover your mouth in public, establish your own  customs, honor your traditions, maintain balance |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/11/Text/12` | 0.344612 | Humans' physical characteristics vary based on their lineage  and home world. Humans have a wide variety of skin and hair  colors, body types, and facial features. Some environments  produce distinct |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/13/Text/22` | 0.342222 | You've developed a soul-deep bond with your comrades. If  you're at least an expert in the skill you're Aiding, when you  roll a failure or critical failure to Aid a skill check, you get a  success in |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/11/ListItem/6` | 0.336981 | Respect your flexibility and usual open-mindedness. |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/11/ListItem/8` | 0.334165 | Aren't sure what to expect from you and are hesitant  to assume your intentions. |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/13/Text/26` | 0.327333 | **Trigger** You attempt a check using a skill you're untrained in. |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/27` | 0.324828 | These descriptors have no mechanical benefit, but they're  important for determining how certain spells, effects, and  other aspects of the game interact with your character. |

### Query 73
- Text: Summarize OTHERS PROBABLY...
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/3/SectionHeader/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/3/SectionHeader/5', 'PZO22001 Starfinder Player Core 040-057::/page/11/SectionHeader/5', 'PZO22001 Starfinder Player Core 040-057::/page/15/SectionHeader/5']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/3/SectionHeader/5` | 0.892334 | OTHERS PROBABLY... |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/11/SectionHeader/5` | 0.892334 | OTHERS PROBABLY... |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/15/SectionHeader/5` | 0.892334 | OTHERS PROBABLY... |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/7/SectionHeader/5` | 0.850334 | OTHERS PROBABLY... |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/23` | 0.336983 | **Alternate** **Ancestry** **Boosts:** Because of the wide variety of  people within any ancestry, you can *always* choose to take two  free boosts to represent your character, even if the ancestry  n |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/13/Text/62` | 0.304825 | **ANCESTRIES & ** **BACKGROUNDS** |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/11/Text/31` | 0.304825 | **ANCESTRIES & ** **BACKGROUNDS** |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/66` | 0.304825 | **ANCESTRIES & ** **BACKGROUNDS** |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/15/Text/32` | 0.304825 | **ANCESTRIES & ** **BACKGROUNDS** |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/31` | 0.304825 | **ANCESTRIES & ** **BACKGROUNDS** |

### Query 74
- Text: Summarize Have trouble parsing your emotions or understanding  when you express them.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/3/ListItem/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/3/ListItem/6', 'PZO22001 Starfinder Player Core 040-057::/page/4/Text/16', 'PZO22001 Starfinder Player Core 040-057::/page/11/ListItem/8']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/3/ListItem/6` | 1.023991 | Have trouble parsing your emotions or understanding  when you express them. |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/4/Text/16` | 0.466282 | Your inhibited or malfunctioning emotional processors  make it difficult for you to feel strong emotions. You gain  a +1 circumstance bonus to saving throws against emotion  effects. If you roll a suc |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/11/ListItem/8` | 0.444524 | Aren't sure what to expect from you and are hesitant  to assume your intentions. |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/6/Text/17` | 0.382737 | You can communicate mentally with creatures within  30 feet. You can communicate only with creatures  that share a language with you. This doesn't give you  any access to their thoughts, and it commun |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/7/ListItem/8` | 0.342970 | Struggle to recognize you because of your frequently  changing appearance. |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/5/ListItem/62` | 0.334700 | You can't speak, Cast Spells, use manipulate actions  requiring your hands, Activate magic items, or make any  Strikes with your normal body. |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/52` | 0.327055 | You refuse to surrender your autonomy and have erected  mental bulwarks and technological protocols to safeguard  your mind and memories. Whenever you attempt a Will save  against a spell or effect th |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/5/ListItem/63` | 0.314840 | You don't gain the swarm mind ability, so you're still  affected normally by mental effects. |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/14/Text/13` | 0.314742 | Additional languages equal to your Intelligence modifier (if it's positive). Choose from the list of common languages and any other languages to which you have access (such as the languages prevalent |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/10/Text/8` | 0.314523 | Additional languages equal to 1 + your Intelligence modifier (if it's positive). Choose from the list of common languages and any other languages to which you have access (such as the languages preval |

### Query 75
- Text: What is the rule about Secretly covet your lack of aging.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/3/ListItem/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/3/ListItem/7', 'PZO22001 Starfinder Player Core 040-057::/page/16/Text/5', 'PZO22001 Starfinder Player Core 040-057::/page/4/Text/3']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/3/ListItem/7` | 0.853945 | Secretly covet your lack of aging. |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/16/Text/5` | 0.402413 | You're undergoing your Tempering, a coming-of-age ritual  during which a kasatha rejects the formal traditions of their  family and experiences other customs and traditions. You  might be one of the U |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/4/Text/3` | 0.378129 | Many souls have inhabited your synthetic body before you,  and you might incorporate a number into your name to honor  them. You might know your body's history and work toward a  goal bequeathed to yo |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/12/Text/21` | 0.333962 | The short human lifespan lends perspective and has taught  you from a young age to set aside differences and work with  others to achieve greatness. You gain a +4 circumstance bonus  on checks to Aid. |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/9/ListItem/43` | 0.318432 | Your body shields the target from harm, granting them  greater cover, though you don't gain cover. Your body  doesn't obscure the target's vision or block line of  sight. |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/17/Text/20` | 0.316901 | Your masked face prevents others from scrutinizing your  appearance, and you've learned to leverage this uncertainty  to your advantage in social situations. While your mouth is  covered, increase the |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/52` | 0.314018 | You refuse to surrender your autonomy and have erected  mental bulwarks and technological protocols to safeguard  your mind and memories. Whenever you attempt a Will save  against a spell or effect th |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/15/ListItem/4` | 0.310540 | Keep your mouth hidden with a scarf or mask while in  public. |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/13/Text/27` | 0.305042 | A stroke of brilliance gives you a major advantage with a skill  despite your inexperience. You gain a +4 circumstance bonus  to the triggering skill check. |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/3/ListItem/2` | 0.304043 | Try to avoid others taking advantage of you. |

### Query 76
- Text: Summarize Have some level of guilt for their ancestors' use of  your species as laborers.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/3/ListItem/8']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/3/ListItem/8', 'PZO22001 Starfinder Player Core 040-057::/page/3/ListItem/4', 'PZO22001 Starfinder Player Core 040-057::/page/12/Text/2']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/3/ListItem/8` | 1.033435 | Have some level of guilt for their ancestors' use of  your species as laborers. |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/3/ListItem/4` | 0.519658 | Judge others based on how they treat service workers,  blue-collar laborers, fans, or pets. |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/12/Text/2` | 0.485799 | Humans were the most common ancestry on Golarion before  that world disappeared, and they've since spread to the stars  thanks to their versatility. Select a general feat of your choice  for which you |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/12/Text/4` | 0.412553 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As a human, you choose from among the  following anc |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/11/Text/24` | 0.411553 | Your ancestors lived on Golarion, and though the precise  circumstances of their survival are lost to the Gap, you strongly  identify with the lost planet's cultures. You become trained in  Golarion L |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/31` | 0.407024 | You select a heritage at 1st level to reflect abilities common  among those of your ancestry in the environment where  you were born or grew up. You have only one heritage and  can't change it later. |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/11/Text/22` | 0.405835 | Humans don't have significant physiological differences  defined by their lineage. Instead, their heritages reveal their  potential as a people. In many cases, these heritages might  represent offshoo |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/9/Text/18` | 0.395133 | You sample the genetics of creatures and people you've  made contact with and mimic them. When you take this feat,  select up to three different ancestries with which you've had  significant contact. |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/15/Text/21` | 0.394884 | **Popular Anathema** disrespect or belittle the traditions of  others, disrespect your elders |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/15/Text/23` | 0.387003 | A kasatha's heritage might be influenced by the environs their  ancestors inhabited on Kasath, the lineage they were born into,  or their progenitors' role in their peoples' interstellar migration.  C |

### Query 77
- Text: What is the rule about Androids thrive in nearly any environment and exist as part  of countless cultures, meaning they can be found almost  anywhere in the galaxy. Many androids are curious about their  origins, traveling alone or with others in search of answers to  a variety of metaphysical and material questions about their  identities and the greater cosmos. Androids are diverse, with  few individuals sharing the exact same appearance, despite  their manufactured state.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/3/Text/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/3/Text/9', 'PZO22001 Starfinder Player Core 040-057::/page/2/Text/2', 'PZO22001 Starfinder Player Core 040-057::/page/3/Text/14']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/9` | 0.999763 | Androids thrive in nearly any environment and exist as part  of countless cultures, meaning they can be found almost  anywhere in the galaxy. Many androids are curious about their  origins, traveling |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/2/Text/2` | 0.739379 | Androids first emerged as synthetic beings crafted by many technologically advanced civilizations throughout the galaxy. The first androids were created by humanoid peoples in their own images, but af |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/14` | 0.717423 | Androids tend to be cautious when visiting new places and  meeting new people. Once comfortable, androids can form  tight bonds of friendship and kinship, adopting found families,  and choosing entire |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/17` | 0.672891 | Androids hold a variety of religious and philosophical  views, with individuals sometimes collecting beliefs and  practices through decades of lived experiences. With a  similar perspective to elves a |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/12` | 0.665967 | Androids are biomechanical constructs who typically  resemble humanoids with glowing circuitry. Most were  created in specialized birthing sites called foundries.  Older variants of androids, such as |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/18` | 0.621165 | shorter lifespans. Many androids are patient in achieving  their goals and might create plans that span decades or  centuries, hoping they will be alive to experience the results.  Elder androids who |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/22` | 0.598425 | An android's heritage often reflects the purpose for which  they were originally created or how they've adapted their  body to best suit their present life. Choose one of the  following android herita |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/10/Text/2` | 0.581571 | Humans are known for their ability to adapt and thrive in the most challenging situations, including the mysterious loss of their home world, Golarion. Ambitious, creative, and endlessly curious, huma |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/10` | 0.542576 | If you want to roleplay a synthetic character on a journey  of self-discovery, you should play an android. |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/4/Text/5` | 0.503961 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As an android, you choose from among  the following |

### Query 78
- Text: What is the rule about If you want to roleplay a synthetic character on a journey  of self-discovery, you should play an android.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/3/Text/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/3/Text/10', 'PZO22001 Starfinder Player Core 040-057::/page/4/Text/24', 'PZO22001 Starfinder Player Core 040-057::/page/4/Text/5']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/10` | 0.925111 | If you want to roleplay a synthetic character on a journey  of self-discovery, you should play an android. |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/4/Text/24` | 0.561347 | You retain instincts and fragmentary memories from the  androids who previously occupied your body or from ancient  programming embedded in your system. During your daily  preparations, you can tap in |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/4/Text/5` | 0.556816 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As an android, you choose from among  the following |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/2/Text/2` | 0.500923 | Androids first emerged as synthetic beings crafted by many technologically advanced civilizations throughout the galaxy. The first androids were created by humanoid peoples in their own images, but af |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/24` | 0.497870 | Your body wasn't created in the image of a biological creature;  a powerful artificial intelligence created you to interface with  other machines. Your physiology is nearly identical to other  android |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/14` | 0.487053 | Androids tend to be cautious when visiting new places and  meeting new people. Once comfortable, androids can form  tight bonds of friendship and kinship, adopting found families,  and choosing entire |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/12` | 0.484887 | Androids are biomechanical constructs who typically  resemble humanoids with glowing circuitry. Most were  created in specialized birthing sites called foundries.  Older variants of androids, such as |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/11/Text/10` | 0.475962 | If you want an adaptable character who can become just  about anything, you should play a human. |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/9` | 0.473052 | Androids thrive in nearly any environment and exist as part  of countless cultures, meaning they can be found almost  anywhere in the galaxy. Many androids are curious about their  origins, traveling |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/18` | 0.463287 | shorter lifespans. Many androids are patient in achieving  their goals and might create plans that span decades or  centuries, hoping they will be alive to experience the results.  Elder androids who |

### Query 79
- Text: Summarize PHYSICAL DESCRIPTION
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/3/SectionHeader/11']
- Expected found: `True`
- Expected rank: `4`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/7/SectionHeader/11', 'PZO22001 Starfinder Player Core 040-057::/page/15/SectionHeader/11', 'PZO22001 Starfinder Player Core 040-057::/page/11/SectionHeader/11']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/7/SectionHeader/11` | 0.971851 | PHYSICAL DESCRIPTION |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/11/SectionHeader/11` | 0.971851 | PHYSICAL DESCRIPTION |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/15/SectionHeader/11` | 0.971851 | PHYSICAL DESCRIPTION |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/3/SectionHeader/11` | 0.929851 | PHYSICAL DESCRIPTION |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/65` | 0.335394 | **INTRODUCTION** |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/30` | 0.335394 | **INTRODUCTION** |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/15/Text/31` | 0.335394 | **INTRODUCTION** |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/11/Text/30` | 0.335394 | **INTRODUCTION** |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/9/Text/50` | 0.335394 | **INTRODUCTION** |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/36` | 0.335394 | **INTRODUCTION** |

### Query 80
- Text: Summarize Androids are biomechanical constructs who typically  resemble humanoids with glowing circuitry. Most were  created in specialized birthing sites called foundries.  Older variants of androids, such as androids on Golarion,  were primarily biological, but androids in the modern era  usually incorporate more technological components and  synthetic elements into their bodies. Androids need to eat  and sleep, but they don't reproduce, don't age, and have no  innate concept of gender—though many express humanoid  gender identities or shift fluidly between them. Most  androids voluntarily release their bodies after a century or  so, allowing new souls to inhabit them in a process called  renewal.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/3/Text/12']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/3/Text/12', 'PZO22001 Starfinder Player Core 040-057::/page/2/Text/2', 'PZO22001 Starfinder Player Core 040-057::/page/3/Text/9']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/12` | 1.044424 | Androids are biomechanical constructs who typically  resemble humanoids with glowing circuitry. Most were  created in specialized birthing sites called foundries.  Older variants of androids, such as |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/2/Text/2` | 0.814643 | Androids first emerged as synthetic beings crafted by many technologically advanced civilizations throughout the galaxy. The first androids were created by humanoid peoples in their own images, but af |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/9` | 0.758331 | Androids thrive in nearly any environment and exist as part  of countless cultures, meaning they can be found almost  anywhere in the galaxy. Many androids are curious about their  origins, traveling |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/18` | 0.705543 | shorter lifespans. Many androids are patient in achieving  their goals and might create plans that span decades or  centuries, hoping they will be alive to experience the results.  Elder androids who |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/14` | 0.668051 | Androids tend to be cautious when visiting new places and  meeting new people. Once comfortable, androids can form  tight bonds of friendship and kinship, adopting found families,  and choosing entire |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/17` | 0.645511 | Androids hold a variety of religious and philosophical  views, with individuals sometimes collecting beliefs and  practices through decades of lived experiences. With a  similar perspective to elves a |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/22` | 0.609779 | An android's heritage often reflects the purpose for which  they were originally created or how they've adapted their  body to best suit their present life. Choose one of the  following android herita |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/24` | 0.609488 | Your body wasn't created in the image of a biological creature;  a powerful artificial intelligence created you to interface with  other machines. Your physiology is nearly identical to other  android |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/10` | 0.565241 | If you want to roleplay a synthetic character on a journey  of self-discovery, you should play an android. |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/4/Text/24` | 0.491143 | You retain instincts and fragmentary memories from the  androids who previously occupied your body or from ancient  programming embedded in your system. During your daily  preparations, you can tap in |

### Query 81
- Text: Summarize SOCIETY
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/3/SectionHeader/13']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/7/SectionHeader/13', 'PZO22001 Starfinder Player Core 040-057::/page/11/SectionHeader/13', 'PZO22001 Starfinder Player Core 040-057::/page/3/SectionHeader/13']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/7/SectionHeader/13` | 0.897896 | SOCIETY |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/11/SectionHeader/13` | 0.897896 | SOCIETY |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/3/SectionHeader/13` | 0.897896 | SOCIETY |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/15/SectionHeader/14` | 0.855896 | SOCIETY |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/11/Text/14` | 0.418846 | Human societies are as varied as the worlds they thrive on.  While the Azlanti Star Empire seeks to recapture an imagined  era of glory by isolating and idealizing an ancient culture from  lost Golari |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/11/Text/18` | 0.340952 | Humans often believe in the structures they've established,  and many adhere to the ideals of the Pact or follow the  laws of other regions or organizations, like the Azlanti Star  Empire or the Free |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/16/Text/5` | 0.330792 | You're undergoing your Tempering, a coming-of-age ritual  during which a kasatha rejects the formal traditions of their  family and experiences other customs and traditions. You  might be one of the U |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/11/Text/9` | 0.322763 | Human ambition has created empires throughout the stars. The  Pact Worlds have many human residents, while the expansion  of the Azlanti Star Empire presents a more sinister expression  of humanity's |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/52` | 0.314547 | **Languages** **CLASSES** |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/11/ListItem/4` | 0.304852 | Cherish your relationships with family and friends. |

### Query 82
- Text: What is the rule about Androids tend to be cautious when visiting new places and  meeting new people. Once comfortable, androids can form  tight bonds of friendship and kinship, adopting found families,  and choosing entire neighborhoods and communities as their  home, rather than remaining confined by the boundaries  formed by walls. Androids often go out of their way to help  one another and their chosen families and communities,  and most hesitate to destroy the body of another android,  knowing that to do so ends not only one life, but erases the  countless other souls who could one day inhabit that body.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/3/Text/14']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/3/Text/14', 'PZO22001 Starfinder Player Core 040-057::/page/3/Text/9', 'PZO22001 Starfinder Player Core 040-057::/page/3/Text/18']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/14` | 1.008500 | Androids tend to be cautious when visiting new places and  meeting new people. Once comfortable, androids can form  tight bonds of friendship and kinship, adopting found families,  and choosing entire |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/9` | 0.691096 | Androids thrive in nearly any environment and exist as part  of countless cultures, meaning they can be found almost  anywhere in the galaxy. Many androids are curious about their  origins, traveling |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/18` | 0.673762 | shorter lifespans. Many androids are patient in achieving  their goals and might create plans that span decades or  centuries, hoping they will be alive to experience the results.  Elder androids who |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/12` | 0.617402 | Androids are biomechanical constructs who typically  resemble humanoids with glowing circuitry. Most were  created in specialized birthing sites called foundries.  Older variants of androids, such as |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/2/Text/2` | 0.608066 | Androids first emerged as synthetic beings crafted by many technologically advanced civilizations throughout the galaxy. The first androids were created by humanoid peoples in their own images, but af |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/17` | 0.604051 | Androids hold a variety of religious and philosophical  views, with individuals sometimes collecting beliefs and  practices through decades of lived experiences. With a  similar perspective to elves a |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/10` | 0.539933 | If you want to roleplay a synthetic character on a journey  of self-discovery, you should play an android. |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/22` | 0.514496 | An android's heritage often reflects the purpose for which  they were originally created or how they've adapted their  body to best suit their present life. Choose one of the  following android herita |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/4/Text/5` | 0.493599 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As an android, you choose from among  the following |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/24` | 0.470093 | Your body wasn't created in the image of a biological creature;  a powerful artificial intelligence created you to interface with  other machines. Your physiology is nearly identical to other  android |

### Query 83
- Text: What is the rule about Androids hold a variety of religious and philosophical  views, with individuals sometimes collecting beliefs and  practices through decades of lived experiences. With a  similar perspective to elves and other long-lived species,  androids tend to view reality differently than beings with?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/3/Text/17']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/3/Text/17', 'PZO22001 Starfinder Player Core 040-057::/page/3/Text/9', 'PZO22001 Starfinder Player Core 040-057::/page/3/Text/18']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/17` | 0.997961 | Androids hold a variety of religious and philosophical  views, with individuals sometimes collecting beliefs and  practices through decades of lived experiences. With a  similar perspective to elves a |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/9` | 0.721730 | Androids thrive in nearly any environment and exist as part  of countless cultures, meaning they can be found almost  anywhere in the galaxy. Many androids are curious about their  origins, traveling |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/18` | 0.700455 | shorter lifespans. Many androids are patient in achieving  their goals and might create plans that span decades or  centuries, hoping they will be alive to experience the results.  Elder androids who |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/14` | 0.622858 | Androids tend to be cautious when visiting new places and  meeting new people. Once comfortable, androids can form  tight bonds of friendship and kinship, adopting found families,  and choosing entire |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/2/Text/2` | 0.618390 | Androids first emerged as synthetic beings crafted by many technologically advanced civilizations throughout the galaxy. The first androids were created by humanoid peoples in their own images, but af |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/12` | 0.617595 | Androids are biomechanical constructs who typically  resemble humanoids with glowing circuitry. Most were  created in specialized birthing sites called foundries.  Older variants of androids, such as |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/22` | 0.541342 | An android's heritage often reflects the purpose for which  they were originally created or how they've adapted their  body to best suit their present life. Choose one of the  following android herita |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/10` | 0.500728 | If you want to roleplay a synthetic character on a journey  of self-discovery, you should play an android. |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/24` | 0.480928 | Your body wasn't created in the image of a biological creature;  a powerful artificial intelligence created you to interface with  other machines. Your physiology is nearly identical to other  android |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/11/Text/18` | 0.480674 | Humans often believe in the structures they've established,  and many adhere to the ideals of the Pact or follow the  laws of other regions or organizations, like the Azlanti Star  Empire or the Free |

### Query 84
- Text: What is the rule about shorter lifespans. Many androids are patient in achieving  their goals and might create plans that span decades or  centuries, hoping they will be alive to experience the results.  Elder androids who voluntarily pass on to the next part of  their cycle sometimes bequeath their goals to the next soul  to inhabit their body.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/3/Text/18']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/3/Text/18', 'PZO22001 Starfinder Player Core 040-057::/page/3/Text/12', 'PZO22001 Starfinder Player Core 040-057::/page/3/Text/14']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/18` | 0.987215 | shorter lifespans. Many androids are patient in achieving  their goals and might create plans that span decades or  centuries, hoping they will be alive to experience the results.  Elder androids who |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/12` | 0.676560 | Androids are biomechanical constructs who typically  resemble humanoids with glowing circuitry. Most were  created in specialized birthing sites called foundries.  Older variants of androids, such as |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/14` | 0.656472 | Androids tend to be cautious when visiting new places and  meeting new people. Once comfortable, androids can form  tight bonds of friendship and kinship, adopting found families,  and choosing entire |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/17` | 0.617617 | Androids hold a variety of religious and philosophical  views, with individuals sometimes collecting beliefs and  practices through decades of lived experiences. With a  similar perspective to elves a |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/9` | 0.548409 | Androids thrive in nearly any environment and exist as part  of countless cultures, meaning they can be found almost  anywhere in the galaxy. Many androids are curious about their  origins, traveling |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/2/Text/2` | 0.541202 | Androids first emerged as synthetic beings crafted by many technologically advanced civilizations throughout the galaxy. The first androids were created by humanoid peoples in their own images, but af |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/4/Text/24` | 0.516904 | You retain instincts and fragmentary memories from the  androids who previously occupied your body or from ancient  programming embedded in your system. During your daily  preparations, you can tap in |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/22` | 0.512308 | An android's heritage often reflects the purpose for which  they were originally created or how they've adapted their  body to best suit their present life. Choose one of the  following android herita |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/10` | 0.479848 | If you want to roleplay a synthetic character on a journey  of self-discovery, you should play an android. |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/4/Text/5` | 0.475931 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As an android, you choose from among  the following |

### Query 85
- Text: What is the rule about **Popular Edicts** discover your origins, help others achieve  long-term goals, plan for the future?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/3/Text/19']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/3/Text/19', 'PZO22001 Starfinder Player Core 040-057::/page/11/Text/19', 'PZO22001 Starfinder Player Core 040-057::/page/7/Text/18']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/19` | 0.964092 | **Popular Edicts** discover your origins, help others achieve  long-term goals, plan for the future |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/11/Text/19` | 0.771703 | **Popular Edicts** devote yourself to a greater cause, explore the  cosmos, strive for greatness |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/7/Text/18` | 0.738471 | **Popular Edicts** adapt to new situations, change your body into  the shape you choose, work together to solve problems |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/15/Text/20` | 0.632004 | **Popular Edicts** cover your mouth in public, establish your own  customs, honor your traditions, maintain balance |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/16/Text/3` | 0.456132 | You choose to travel abroad, leaving your birthplace to  embark on a journey through the wider cosmos. During  your daily preparations, you can study a particular ancestry,  faction, philosophy, or re |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/7/Text/19` | 0.454322 | **Popular Anathema** tackle problems on your own |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/12/Text/21` | 0.420749 | The short human lifespan lends perspective and has taught  you from a young age to set aside differences and work with  others to achieve greatness. You gain a +4 circumstance bonus  on checks to Aid. |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/11/Text/18` | 0.411787 | Humans often believe in the structures they've established,  and many adhere to the ideals of the Pact or follow the  laws of other regions or organizations, like the Azlanti Star  Empire or the Free |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/8/Text/14` | 0.409114 | From your upbringing, you've learned the ways of your people  while also seeking to expand your own mind in the fields of  creation. You gain the trained proficiency rank in Crafting and  Medicine. If |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/4/Text/10` | 0.407215 | You have a keen interest in the origins of your people. You  gain the trained proficiency rank in Crafting and Thievery. If  you would automatically become trained in one of those skills  (from your b |

### Query 86
- Text: What is the rule about Your body wasn't created in the image of a biological creature;  a powerful artificial intelligence created you to interface with  other machines. Your physiology is nearly identical to other  androids, but uncanny details give away your non-standard  origins (for example, you might have impossibly symmetrical  features, extra fingers, or double pupils). You become trained  in Computers, and you gain the Phreaker skill feat.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/3/Text/24']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/3/Text/24', 'PZO22001 Starfinder Player Core 040-057::/page/4/Text/24', 'PZO22001 Starfinder Player Core 040-057::/page/3/Text/12']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/24` | 0.994083 | Your body wasn't created in the image of a biological creature;  a powerful artificial intelligence created you to interface with  other machines. Your physiology is nearly identical to other  android |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/4/Text/24` | 0.640834 | You retain instincts and fragmentary memories from the  androids who previously occupied your body or from ancient  programming embedded in your system. During your daily  preparations, you can tap in |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/12` | 0.630201 | Androids are biomechanical constructs who typically  resemble humanoids with glowing circuitry. Most were  created in specialized birthing sites called foundries.  Older variants of androids, such as |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/28` | 0.552774 | Your body was modified to network seamlessly with other tech  creatures. You gain shortwave, allowing you to communicate  wirelessly with any creatures within 30 feet, as long as  they have shortwave |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/4/Text/5` | 0.541145 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As an android, you choose from among  the following |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/4/Text/3` | 0.537965 | Many souls have inhabited your synthetic body before you,  and you might incorporate a number into your name to honor  them. You might know your body's history and work toward a  goal bequeathed to yo |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/10` | 0.537911 | If you want to roleplay a synthetic character on a journey  of self-discovery, you should play an android. |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/2/Text/2` | 0.537410 | Androids first emerged as synthetic beings crafted by many technologically advanced civilizations throughout the galaxy. The first androids were created by humanoid peoples in their own images, but af |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/8/Text/14` | 0.512739 | From your upbringing, you've learned the ways of your people  while also seeking to expand your own mind in the fields of  creation. You gain the trained proficiency rank in Crafting and  Medicine. If |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/9` | 0.505298 | Androids thrive in nearly any environment and exist as part  of countless cultures, meaning they can be found almost  anywhere in the galaxy. Many androids are curious about their  origins, traveling |

### Query 87
- Text: What is the rule about You or your previous iterations have modified your body to be  compatible with armor upgrades, enabling you to personally  customize your body and its capabilities. Your body has one  armor upgrade slot that you can use to install armor upgrades  and that doesn't count toward your armor's total number of  upgrades. You can install and uninstall armor upgrades into  your personal upgrade slot using the Install Upgrade activity.  Choose one common armor upgrade with an item level of 1  or less. You begin with this armor upgrade already installed  in your upgrade slot (you don't need to pay the credits to  purchase this starting upgrade).?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/3/Text/26']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/3/Text/26', 'PZO22001 Starfinder Player Core 040-057::/page/12/Text/11', 'PZO22001 Starfinder Player Core 040-057::/page/8/Text/28']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/26` | 0.993013 | You or your previous iterations have modified your body to be  compatible with armor upgrades, enabling you to personally  customize your body and its capabilities. Your body has one  armor upgrade sl |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/12/Text/11` | 0.650883 | edge augmentations into your body. Choose one common  augmentation with an item level of 1 or less. You begin with this  augmentation already installed in your body (you don't need to  pay the credits |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/8/Text/28` | 0.514864 | You've adapted more of your tendrils and limbs with complex  musculature and cellular structures, improving articulation  and fine motor skills. Increase your number of arms by two.  At any time, one |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/12/Text/25` | 0.461783 | Your adaptability manifests in your mastery of a range of  useful abilities. You gain a 1st-level general feat. You must  meet the feat's prerequisites, but if you select this feat during  character c |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/9/Text/48` | 0.454257 | You've cataloged the genetic code from countless ancestries  you've encountered, and you can draw upon any of them  to enhance and evolve your body. Increase the number of  ancestries you can select w |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/33` | 0.437918 | This section presents ancestry feats, which allow you to  customize your character. You gain your first ancestry feat  at 1st level, and you gain another at 5th level, 9th level, 13th  level, and 17th |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/34` | 0.436629 | As a starting character, you can choose from only 1stlevel ancestry feats, but later choices can be made from any  feat of your level or lower. These feats also sometimes list  prerequisites, which ar |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/14/Text/18` | 0.433088 | weapons and equipment. At any time, one pair of hands is designated as your active hands. You can change this designation from one pair of hands to another by taking the Switch Hands action, which is |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/12/Text/30` | 0.430694 | You were raised to be ambitious and always reach for the  stars, leading you to progress quickly in your chosen field. You  gain a 1st-level class feat for your class. You must meet the  prerequisites |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/13/Text/7` | 0.424957 | You've continued adapting your magic to blend your class's  tradition with your adapted tradition. Choose a cantrip or  1st-rank spell from the same magical tradition as your cantrip  from Adapted Can |

### Query 88
- Text: What is the rule about Your body was modified to network seamlessly with other tech  creatures. You gain shortwave, allowing you to communicate  wirelessly with any creatures within 30 feet, as long as  they have shortwave or are a construct with the tech trait.  This doesn't give any special access to their thoughts or  programming and communicates no more information than  normal speech would. You can attempt Computers checks?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/3/Text/28']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/3/Text/28', 'PZO22001 Starfinder Player Core 040-057::/page/6/Text/17', 'PZO22001 Starfinder Player Core 040-057::/page/3/Text/24']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/28` | 1.009398 | Your body was modified to network seamlessly with other tech  creatures. You gain shortwave, allowing you to communicate  wirelessly with any creatures within 30 feet, as long as  they have shortwave |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/6/Text/17` | 0.748996 | You can communicate mentally with creatures within  30 feet. You can communicate only with creatures  that share a language with you. This doesn't give you  any access to their thoughts, and it commun |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/24` | 0.523326 | Your body wasn't created in the image of a biological creature;  a powerful artificial intelligence created you to interface with  other machines. Your physiology is nearly identical to other  android |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/9/Text/39` | 0.460551 | You temporarily merge your body with that of an adjacent  willing creature, overlaying yourself atop them to better  shield them from harm. This transformation lasts for 10  minutes. You can Dismiss t |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/9/ListItem/41` | 0.447665 | You occupy the target's space and can't take actions  with the move trait. If the target moves, you move with  them. |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/9/ListItem/43` | 0.444607 | Your body shields the target from harm, granting them  greater cover, though you don't gain cover. Your body  doesn't obscure the target's vision or block line of  sight. |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/9` | 0.434898 | You were created to fight other synthetic creatures. When  you roll a critical hit against a creature with the tech trait, the  target becomes glitching 1. |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/5/ListItem/60` | 0.434813 | You can occupy the same space as other creatures and  must do so to use your damaging ability. |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/1/ListItem/11` | 0.416414 | **Languages**, starting on page 97, let your character  communicate with people and creatures of the galaxy. |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/47` | 0.413104 | You can cast *speak with computers* once per day as a 4thrank arcane innate spell. |

### Query 89
- Text: What is the rule about **ANCESTRIES & ** **BACKGROUNDS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/3/Text/31']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/1/Text/37', 'PZO22001 Starfinder Player Core 040-057::/page/17/Text/56', 'PZO22001 Starfinder Player Core 040-057::/page/3/Text/31']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/37` | 0.920820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/17/Text/56` | 0.920820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/31` | 0.920820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/66` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/7/Text/31` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/15/Text/32` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/9/Text/51` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/13/Text/62` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/11/Text/31` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/1/SectionHeader/1` | 0.795553 | CHAPTER 2: ANCESTRIES &  BACKGROUNDS |

### Query 90
- Text: What is the rule about **Backgrounds**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/3/Text/44']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/1/Text/51', 'PZO22001 Starfinder Player Core 040-057::/page/5/Text/80', 'PZO22001 Starfinder Player Core 040-057::/page/3/Text/44']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/51` | 0.796516 | **Backgrounds** |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/80` | 0.796516 | **Backgrounds** |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/44` | 0.796516 | **Backgrounds** |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/7/Text/44` | 0.754516 | **Backgrounds** |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/15/Text/46` | 0.754516 | **Backgrounds** |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/9/Text/65` | 0.754516 | **Backgrounds** |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/13/Text/75` | 0.754516 | **Backgrounds** |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/11/Text/43` | 0.754516 | **Backgrounds** |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/17/Text/70` | 0.754516 | **Backgrounds** |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/1/ListItem/10` | 0.567373 | **Backgrounds**, starting on page 92, describe training  or environments your character experienced before  becoming an adventurer. Your character's background  provides attribute boosts, skill traini |

### Query 91
- Text: What is the rule about **SKILLS** **FEATS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/3/Text/47']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/11/Text/46', 'PZO22001 Starfinder Player Core 040-057::/page/15/Text/49', 'PZO22001 Starfinder Player Core 040-057::/page/3/Text/47']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/47` | 0.909736 | **SKILLS** **FEATS** |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/11/Text/46` | 0.909736 | **SKILLS** **FEATS** |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/15/Text/49` | 0.909736 | **SKILLS** **FEATS** |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/7/Text/47` | 0.867736 | **SKILLS** **FEATS** |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/9/Text/68` | 0.867736 | **SKILLS** **FEATS** |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/17/Text/73` | 0.656535 | **SKILLS** |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/13/Text/78` | 0.656535 | **SKILLS** |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/53` | 0.656535 | **SKILLS** |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/83` | 0.656535 | **SKILLS** |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/54` | 0.613813 | **FEATS** |

### Query 92
- Text: What is the rule about **SPELLS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/3/Text/49']
- Expected found: `True`
- Expected rank: `4`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/9/Text/70', 'PZO22001 Starfinder Player Core 040-057::/page/1/Text/56', 'PZO22001 Starfinder Player Core 040-057::/page/15/Text/51']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/9/Text/70` | 0.889304 | **SPELLS** |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/56` | 0.889304 | **SPELLS** |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/15/Text/51` | 0.889304 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/49` | 0.847304 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/11/Text/48` | 0.847304 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/7/Text/49` | 0.847304 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/13/Text/80` | 0.759411 | **EQUIPMENT** **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/85` | 0.759411 | **EQUIPMENT** **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/17/Text/75` | 0.759411 | **EQUIPMENT** **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/17/Text/73` | 0.388254 | **SKILLS** |

### Query 93
- Text: What is the rule about to Hack systems, Combat Hack (page 217), create a Digital  Diversion (page 218), Disable a Device, or Pick a Lock without  a hacker's toolkit or free hand at a range of 30 feet.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/4/Text/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/4/Text/1', 'PZO22001 Starfinder Player Core 040-057::/page/3/Text/28', 'PZO22001 Starfinder Player Core 040-057::/page/4/Text/20']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/4/Text/1` | 0.951893 | to Hack systems, Combat Hack (page 217), create a Digital  Diversion (page 218), Disable a Device, or Pick a Lock without  a hacker's toolkit or free hand at a range of 30 feet. |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/28` | 0.483492 | Your body was modified to network seamlessly with other tech  creatures. You gain shortwave, allowing you to communicate  wirelessly with any creatures within 30 feet, as long as  they have shortwave |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/4/Text/20` | 0.439284 | You can hide a small object of up to light Bulk inside a hollow  cavity on one of your forearms. It takes 3 Interact actions to  store an object in this way. You gain a +4 circumstance bonus  to the D |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/5/ListItem/62` | 0.393224 | You can't speak, Cast Spells, use manipulate actions  requiring your hands, Activate magic items, or make any  Strikes with your normal body. |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/14/Text/18` | 0.391943 | weapons and equipment. At any time, one pair of hands is designated as your active hands. You can change this designation from one pair of hands to another by taking the Switch Hands action, which is |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/8/Text/28` | 0.360090 | You've adapted more of your tendrils and limbs with complex  musculature and cellular structures, improving articulation  and fine motor skills. Increase your number of arms by two.  At any time, one |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/9/ListItem/43` | 0.357356 | Your body shields the target from harm, granting them  greater cover, though you don't gain cover. Your body  doesn't obscure the target's vision or block line of  sight. |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/8/Text/23` | 0.348815 | Spiky protrusions jut from your body, which you can use to  wound your attackers. Your Fortitude DC against Athletics  checks to Grapple or Shove you increases by 1. Additionally,  you gain the Pierci |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/42` | 0.347511 | Your nanites are programmed to automatically revive you.  You are restored to 1 Hit Point, lose the dying and unconscious  conditions, and can act normally on this turn. You gain or  increase the woun |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/17/Text/5` | 0.345923 | **Trigger** You fail an Acrobatics check or Reflex saving throw. You have an almost supernatural control of your movements,  which can sometimes save you in dangerous situations. You  can reroll the t |

### Query 94
- Text: What is the rule about Many souls have inhabited your synthetic body before you,  and you might incorporate a number into your name to honor  them. You might know your body's history and work toward a  goal bequeathed to you by a departed soul, or you might seek  to learn the mystery of a forgotten legacy. Muscle memory  hints at your body's past, and people you've never met  sometimes recognize your face. The first time in a day that  you lose the dying condition, you don't gain the wounded  condition. You become trained in a skill of your choice that  has the Recall Knowledge action, and you gain the Dubious  Knowledge skill feat.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/4/Text/3']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/4/Text/3', 'PZO22001 Starfinder Player Core 040-057::/page/4/Text/24', 'PZO22001 Starfinder Player Core 040-057::/page/8/Text/14']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/4/Text/3` | 1.008514 | Many souls have inhabited your synthetic body before you,  and you might incorporate a number into your name to honor  them. You might know your body's history and work toward a  goal bequeathed to yo |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/4/Text/24` | 0.638472 | You retain instincts and fragmentary memories from the  androids who previously occupied your body or from ancient  programming embedded in your system. During your daily  preparations, you can tap in |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/8/Text/14` | 0.580136 | From your upbringing, you've learned the ways of your people  while also seeking to expand your own mind in the fields of  creation. You gain the trained proficiency rank in Crafting and  Medicine. If |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/13/Text/59` | 0.537698 | You return from the brink of death, hauling yourself back  to consciousness through exhaustion and pain. If you have  the dying or unconscious conditions, you lose the dying and  unconscious condition |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/17/Text/29` | 0.534915 | You've cataloged countless customs, histories, and traditions.  You can cast *hypercognition* once per day as a 3rd-rank occult  innate spell. You can use your modifier for the Lore skill  you chose f |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/9/Text/18` | 0.529646 | You sample the genetics of creatures and people you've  made contact with and mimic them. When you take this feat,  select up to three different ancestries with which you've had  significant contact. |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/16/Text/3` | 0.528108 | You choose to travel abroad, leaving your birthplace to  embark on a journey through the wider cosmos. During  your daily preparations, you can study a particular ancestry,  faction, philosophy, or re |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/42` | 0.526424 | Your nanites are programmed to automatically revive you.  You are restored to 1 Hit Point, lose the dying and unconscious  conditions, and can act normally on this turn. You gain or  increase the woun |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/17/Text/13` | 0.521733 | You become trained in a Lore skill of your choice. You can  spend 10 minutes checking your notes or research materials  to Recall Knowledge about a piece of history with any Lore  skill in which you a |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/6/Text/15` | 0.509628 | You can reshape and adjust your body to adapt to  new situations. You can retrain an ancestry feat in  1 day of downtime, rather than in 1 week. You can  retrain any ancestry feat, even lineage feats. |

### Query 95
- Text: What is the rule about ANDROID ANCESTRY  FEATS?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/4/SectionHeader/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/4/SectionHeader/4', 'PZO22001 Starfinder Player Core 040-057::/page/1/SectionHeader/32', 'PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/3']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/4/SectionHeader/4` | 0.932330 | ANDROID ANCESTRY  FEATS |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/1/SectionHeader/32` | 0.744140 | ANCESTRY FEATS |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/3` | 0.676001 | HUMAN ANCESTRY FEATS |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/4/Text/5` | 0.599919 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As an android, you choose from among  the following |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/16/SectionHeader/6` | 0.575072 | KASATHA ANCESTRY  FEATS |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/8/SectionHeader/3` | 0.552958 | BARATHU ANCESTRY  FEATS |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/2/SectionHeader/1` | 0.513481 | ANDROID |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/3/SectionHeader/21` | 0.492615 | ANDROID HERITAGES |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/1/SectionHeader/12` | 0.479994 | ANCESTRY ENTRIES |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/12/Text/4` | 0.460766 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As a human, you choose from among the  following anc |

### Query 96
- Text: What is the rule about At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As an android, you choose from among  the following ancestry feats.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/4/Text/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/4/Text/5', 'PZO22001 Starfinder Player Core 040-057::/page/12/Text/4', 'PZO22001 Starfinder Player Core 040-057::/page/16/Text/7']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/4/Text/5` | 0.968522 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As an android, you choose from among  the following |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/12/Text/4` | 0.906460 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As a human, you choose from among the  following anc |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/16/Text/7` | 0.817941 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As a kasatha, you choose from among  the following a |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/8/Text/4` | 0.767228 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th,  9th, 13th, and 17th level). As a barathu, you choose from  among the following a |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/33` | 0.737958 | This section presents ancestry feats, which allow you to  customize your character. You gain your first ancestry feat  at 1st level, and you gain another at 5th level, 9th level, 13th  level, and 17th |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/34` | 0.695315 | As a starting character, you can choose from only 1stlevel ancestry feats, but later choices can be made from any  feat of your level or lower. These feats also sometimes list  prerequisites, which ar |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/9/Text/18` | 0.649962 | You sample the genetics of creatures and people you've  made contact with and mimic them. When you take this feat,  select up to three different ancestries with which you've had  significant contact. |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/9/Text/48` | 0.592240 | You've cataloged the genetic code from countless ancestries  you've encountered, and you can draw upon any of them  to enhance and evolve your body. Increase the number of  ancestries you can select w |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/4/Text/24` | 0.574123 | You retain instincts and fragmentary memories from the  androids who previously occupied your body or from ancient  programming embedded in your system. During your daily  preparations, you can tap in |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/6` | 0.573003 | A character has one ancestry and one background, both of  which you select during character creation. You'll also select  a number of languages for your character. Once chosen, your  ancestry and back |

### Query 97
- Text: What are the requirements for **ANDROID LORE** **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/4/SectionHeader/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/4/SectionHeader/7', 'PZO22001 Starfinder Player Core 040-057::/page/5/Text/12', 'PZO22001 Starfinder Player Core 040-057::/page/4/Text/27']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/4/SectionHeader/7` | 0.909151 | **ANDROID LORE** **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/4/Text/27` | 0.599509 | **ANDROID** |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/12` | 0.599509 | **ANDROID** |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/4/Text/9` | 0.569509 | **ANDROID** |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/39` | 0.557509 | **ANDROID** |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/4/Text/19` | 0.557509 | **ANDROID** |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/4/Text/23` | 0.557509 | **ANDROID** |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/22` | 0.557509 | **ANDROID** |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/4/Text/32` | 0.557509 | **ANDROID** |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/18` | 0.557509 | **ANDROID** |

### Query 98
- Text: What is the rule about You have a keen interest in the origins of your people. You  gain the trained proficiency rank in Crafting and Thievery. If  you would automatically become trained in one of those skills  (from your background or class, for example), you instead  become trained in a skill of your choice.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/4/Text/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/4/Text/10', 'PZO22001 Starfinder Player Core 040-057::/page/8/Text/14', 'PZO22001 Starfinder Player Core 040-057::/page/16/Text/21']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/4/Text/10` | 0.998884 | You have a keen interest in the origins of your people. You  gain the trained proficiency rank in Crafting and Thievery. If  you would automatically become trained in one of those skills  (from your b |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/8/Text/14` | 0.867181 | From your upbringing, you've learned the ways of your people  while also seeking to expand your own mind in the fields of  creation. You gain the trained proficiency rank in Crafting and  Medicine. If |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/16/Text/21` | 0.732086 | You've studied the kasathan traditions of balance  and harmony. You gain the trained proficiency  rank in Diplomacy and Society. If you would  automatically become trained in one of those skills  (fro |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/12/Text/34` | 0.629790 | Your ingenuity allows you to learn a wide variety of skills. You  gain the trained proficiency rank in two skills of your choice. |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/11/Text/26` | 0.573504 | Your ingenuity allows you to train in a wide variety of skills.  You become trained in one skill of your choice. At 5th level, you  become an expert in the chosen skill. |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/16/Text/3` | 0.563326 | You choose to travel abroad, leaving your birthplace to  embark on a journey through the wider cosmos. During  your daily preparations, you can study a particular ancestry,  faction, philosophy, or re |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/13/Text/2` | 0.549056 | If you're trained in all martial weapons, you can instead  choose an uncommon advanced weapon that has an ancestry's  trait or is common in another culture. You gain access to that  weapon and have fa |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/4/Text/24` | 0.541824 | You retain instincts and fragmentary memories from the  androids who previously occupied your body or from ancient  programming embedded in your system. During your daily  preparations, you can tap in |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/17/Text/13` | 0.528999 | You become trained in a Lore skill of your choice. You can  spend 10 minutes checking your notes or research materials  to Recall Knowledge about a piece of history with any Lore  skill in which you a |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/12/Text/30` | 0.520844 | You were raised to be ambitious and always reach for the  stars, leading you to progress quickly in your chosen field. You  gain a 1st-level class feat for your class. You must meet the  prerequisites |

### Query 99
- Text: What is the rule about You also gain the Additional Lore general feat for Android  Lore.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/4/Text/12']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/4/Text/12', 'PZO22001 Starfinder Player Core 040-057::/page/8/Text/15', 'PZO22001 Starfinder Player Core 040-057::/page/16/Text/22']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/4/Text/12` | 0.950063 | You also gain the Additional Lore general feat for Android  Lore. |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/8/Text/15` | 0.748387 | You also gain the Additional Lore general feat for Barathu  Lore. |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/16/Text/22` | 0.736196 | You also gain the Additional Lore general feat for  Kasatha Lore. |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/4/Text/5` | 0.624386 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As an android, you choose from among  the following |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/4/Text/24` | 0.510205 | You retain instincts and fragmentary memories from the  androids who previously occupied your body or from ancient  programming embedded in your system. During your daily  preparations, you can tap in |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/12/Text/4` | 0.504254 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As a human, you choose from among the  following anc |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/16/Text/3` | 0.487614 | You choose to travel abroad, leaving your birthplace to  embark on a journey through the wider cosmos. During  your daily preparations, you can study a particular ancestry,  faction, philosophy, or re |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/4/SectionHeader/7` | 0.482720 | **ANDROID LORE** **FEAT 1** |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/11/Text/28` | 0.471797 | You have grown up in a big city and are accustomed to the  press and pull of the largest crowds, the electric buzz and  tangle of streets, or the dense nature of vertical living on a  station or megap |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/17/Text/13` | 0.468176 | You become trained in a Lore skill of your choice. You can  spend 10 minutes checking your notes or research materials  to Recall Knowledge about a piece of history with any Lore  skill in which you a |

### Query 100
- Text: What are the requirements for **EMOTIONLESS** **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/4/SectionHeader/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/4/SectionHeader/13', 'PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/22', 'PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/31']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/4/SectionHeader/13` | 0.871831 | **EMOTIONLESS** **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/22` | 0.520098 | **GENERAL TRAINING** **FEAT 1** |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/31` | 0.512384 | **NATURAL SKILL** **FEAT 1** |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/15/Text/49` | 0.437584 | **SKILLS** **FEATS** |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/7/Text/47` | 0.437584 | **SKILLS** **FEATS** |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/47` | 0.437584 | **SKILLS** **FEATS** |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/9/Text/68` | 0.437584 | **SKILLS** **FEATS** |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/11/Text/46` | 0.437584 | **SKILLS** **FEATS** |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/13/Text/79` | 0.428144 | **FEATS** |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/54` | 0.428144 | **FEATS** |

### Query 101
- Text: What is the rule about Your inhibited or malfunctioning emotional processors  make it difficult for you to feel strong emotions. You gain  a +1 circumstance bonus to saving throws against emotion  effects. If you roll a success on a saving throw against an  emotion effect, you get a critical success instead.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/4/Text/16']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/4/Text/16', 'PZO22001 Starfinder Player Core 040-057::/page/17/Text/5', 'PZO22001 Starfinder Player Core 040-057::/page/17/Text/33']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/4/Text/16` | 1.006719 | Your inhibited or malfunctioning emotional processors  make it difficult for you to feel strong emotions. You gain  a +1 circumstance bonus to saving throws against emotion  effects. If you roll a suc |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/17/Text/5` | 0.577110 | **Trigger** You fail an Acrobatics check or Reflex saving throw. You have an almost supernatural control of your movements,  which can sometimes save you in dangerous situations. You  can reroll the t |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/17/Text/33` | 0.563049 | You are in tune with your surroundings and can instinctively  sense when danger is near. You gain a +2 circumstance bonus  to Perception checks for initiative rolls. If your initiative roll  result is |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/16/Text/1` | 0.500663 | of lengthy space travel. For you, the *Idari* is the only home  you've ever known. When you roll a success on a saving  throw against an emotion effect, you get a critical success  instead. |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/52` | 0.496305 | You refuse to surrender your autonomy and have erected  mental bulwarks and technological protocols to safeguard  your mind and memories. Whenever you attempt a Will save  against a spell or effect th |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/9` | 0.474827 | You were created to fight other synthetic creatures. When  you roll a critical hit against a creature with the tech trait, the  target becomes glitching 1. |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/13/Text/27` | 0.468997 | A stroke of brilliance gives you a major advantage with a skill  despite your inexperience. You gain a +4 circumstance bonus  to the triggering skill check. |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/13/Text/16` | 0.462046 | **Trigger** You're about to attempt a saving throw or skill check. |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/13/Text/22` | 0.461711 | You've developed a soul-deep bond with your comrades. If  you're at least an expert in the skill you're Aiding, when you  roll a failure or critical failure to Aid a skill check, you get a  success in |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/14` | 0.461522 | Your nanites augment your defenses. You can choose to  activate Nanite Surge when you attempt a saving throw  instead of when you attempt a skill action. If you do, you gain  a +2 status bonus to the |

### Query 102
- Text: What are the requirements for **INTERNAL COMPARTMENT** **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/4/SectionHeader/17']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/4/SectionHeader/17', 'PZO22001 Starfinder Player Core 040-057::/page/9/SectionHeader/30', 'PZO22001 Starfinder Player Core 040-057::/page/5/SectionHeader/16']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/4/SectionHeader/17` | 0.864023 | **INTERNAL COMPARTMENT** **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/9/SectionHeader/30` | 0.511687 | **INTERNAL CHEMISTRY** **FEAT 13** |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/5/SectionHeader/16` | 0.498879 | **INTERNAL RESPIRATOR** **FEAT 9** |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/22` | 0.432204 | **GENERAL TRAINING** **FEAT 1** |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/31` | 0.418908 | **NATURAL SKILL** **FEAT 1** |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/13/SectionHeader/38` | 0.386413 | **INNER WELLSPRING **[one-action] **FEAT 13** |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/27` | 0.372769 | **NATURAL AMBITION** **FEAT 1** |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/4/SectionHeader/30` | 0.370413 | **NIGHTVISION ADAPTATION** **FEAT 1** |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/13/Text/41` | 0.364200 | **Prerequisites** focus pool |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/9/Text/8` | 0.360683 | **VENT GAS **[one-action] **FEAT 5** |

### Query 103
- Text: What are the requirements for **MEMORY RECOVERY** **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/4/SectionHeader/21']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/4/SectionHeader/21', 'PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/22', 'PZO22001 Starfinder Player Core 040-057::/page/5/SectionHeader/49']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/4/SectionHeader/21` | 0.854204 | **MEMORY RECOVERY** **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/22` | 0.534638 | **GENERAL TRAINING** **FEAT 1** |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/5/SectionHeader/49` | 0.508614 | **MEMORY MATRIX** **FEAT 17** |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/31` | 0.460889 | **NATURAL SKILL** **FEAT 1** |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/5/SectionHeader/25` | 0.458120 | **REPAIR MODULE **[one-action] **FEAT 9** |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/4/SectionHeader/34` | 0.446188 | **QUICKENED PROCESSOR** **FEAT 1** |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/16/SectionHeader/13` | 0.435238 | **CREW MEMBER **[reaction] **FEAT 1** |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/12/Text/25` | 0.431802 | Your adaptability manifests in your mastery of a range of  useful abilities. You gain a 1st-level general feat. You must  meet the feat's prerequisites, but if you select this feat during  character c |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/4/Text/24` | 0.420810 | You retain instincts and fragmentary memories from the  androids who previously occupied your body or from ancient  programming embedded in your system. During your daily  preparations, you can tap in |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/5/SectionHeader/37` | 0.418566 | **REVIVIFICATION PROTOCOL **[free-action] **FEAT 13** |

### Query 104
- Text: What are the requirements for **NANITE SURGE **[reaction] **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/4/SectionHeader/25']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/4/SectionHeader/25', 'PZO22001 Starfinder Player Core 040-057::/page/5/Text/23', 'PZO22001 Starfinder Player Core 040-057::/page/5/Text/13']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/4/SectionHeader/25` | 0.887844 | **NANITE SURGE **[reaction] **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/23` | 0.820797 | **Prerequisites** Nanite Surge |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/13` | 0.820797 | **Prerequisites** Nanite Surge |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/34` | 0.778797 | **Prerequisites** Nanite Surge |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/5/SectionHeader/53` | 0.575953 | **NANITE FORM **[two-actions] **FEAT 17** |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/24` | 0.545953 | Nanites augment your attacks. You can choose to activate  Nanite Surge when you attempt an attack roll, instead of  when you attempt a skill action. If you do, you gain a +1  status bonus to the trigg |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/14` | 0.540297 | Your nanites augment your defenses. You can choose to  activate Nanite Surge when you attempt a saving throw  instead of when you attempt a skill action. If you do, you gain  a +2 status bonus to the |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/36` | 0.476244 | body's efficiency more often. You can use Nanite Surge with a  frequency of once per 10 minutes, rather than once per hour. |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/17/Text/2` | 0.462339 | **NATURAL GRACE **[free-action] **FEAT 1** |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/5/SectionHeader/31` | 0.458718 | **CONSISTENT SURGE** **FEAT 13** |

### Query 105
- Text: What are the requirements for **NIGHTVISION ADAPTATION** **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/4/SectionHeader/30']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/4/SectionHeader/30', 'PZO22001 Starfinder Player Core 040-057::/page/8/SectionHeader/16', 'PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/6']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/4/SectionHeader/30` | 0.935720 | **NIGHTVISION ADAPTATION** **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/8/SectionHeader/16` | 0.779419 | **DARKVISION ADAPTATION** **FEAT 1** |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/6` | 0.518951 | **ADAPTED AUGMENTATIONS** **FEAT 1** |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/31` | 0.454739 | **NATURAL SKILL** **FEAT 1** |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/13/SectionHeader/4` | 0.451958 | **ADAPTIVE ADEPT** **FEAT 5** |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/27` | 0.446617 | **NATURAL AMBITION** **FEAT 1** |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/12` | 0.441970 | **ADAPTED CANTRIP** **FEAT 1** |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/12/Text/25` | 0.439303 | Your adaptability manifests in your mastery of a range of  useful abilities. You gain a 1st-level general feat. You must  meet the feat's prerequisites, but if you select this feat during  character c |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/8/SectionHeader/6` | 0.429143 | **ADAPTABLE LIMBS** **FEAT 1** |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/22` | 0.424493 | **GENERAL TRAINING** **FEAT 1** |

### Query 106
- Text: What are the requirements for **QUICKENED PROCESSOR** **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/4/SectionHeader/34']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/4/SectionHeader/34', 'PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/31', 'PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/22']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/4/SectionHeader/34` | 0.914449 | **QUICKENED PROCESSOR** **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/31` | 0.456704 | **NATURAL SKILL** **FEAT 1** |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/22` | 0.454077 | **GENERAL TRAINING** **FEAT 1** |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/13/Text/52` | 0.410704 | **Requirements** Confident Actualization |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/4/SectionHeader/7` | 0.386506 | **ANDROID LORE** **FEAT 1** |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/16/SectionHeader/13` | 0.383137 | **CREW MEMBER **[reaction] **FEAT 1** |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/9/SectionHeader/47` | 0.383062 | **Prerequisites** Convergent Evolution |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/4/SectionHeader/21` | 0.380841 | **MEMORY RECOVERY** **FEAT 1** |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/8/SectionHeader/16` | 0.373815 | **DARKVISION ADAPTATION** **FEAT 1** |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/5/SectionHeader/2` | 0.369487 | **ADVANCED TARGETING SYSTEM** **FEAT 5** |

### Query 107
- Text: What are the requirements for **ADVANCED TARGETING SYSTEM** **FEAT 5**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/5/SectionHeader/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/5/SectionHeader/2', 'PZO22001 Starfinder Player Core 040-057::/page/13/SectionHeader/4', 'PZO22001 Starfinder Player Core 040-057::/page/13/SectionHeader/33']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/5/SectionHeader/2` | 0.933181 | **ADVANCED TARGETING SYSTEM** **FEAT 5** |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/13/SectionHeader/4` | 0.557344 | **ADAPTIVE ADEPT** **FEAT 5** |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/13/SectionHeader/33` | 0.553186 | **ADVANCED GENERAL TRAINING** **FEAT 13** |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/5/SectionHeader/6` | 0.433648 | **MACHINE SABOTEUR** **FEAT 5** |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/17/Text/18` | 0.420682 | **MASKED** **FEAT 5** |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/13/SectionHeader/8` | 0.415365 | **CLEVER IMPROVISER** **FEAT 5** |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/13/SectionHeader/12` | 0.403179 | **CONFIDENT ACTUALIZATION **[free-action] **FEAT 5** |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/6` | 0.393108 | **ADAPTED AUGMENTATIONS** **FEAT 1** |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/22` | 0.389560 | **GENERAL TRAINING** **FEAT 1** |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/8/SectionHeader/16` | 0.384261 | **DARKVISION ADAPTATION** **FEAT 1** |

### Query 108
- Text: What are the requirements for **MACHINE SABOTEUR** **FEAT 5**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/5/SectionHeader/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/5/SectionHeader/6', 'PZO22001 Starfinder Player Core 040-057::/page/5/SectionHeader/10', 'PZO22001 Starfinder Player Core 040-057::/page/17/Text/18']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/5/SectionHeader/6` | 0.908832 | **MACHINE SABOTEUR** **FEAT 5** |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/5/SectionHeader/10` | 0.580038 | **PROTECTIVE SUBROUTINE** **FEAT 5** |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/17/Text/18` | 0.563133 | **MASKED** **FEAT 5** |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/13/SectionHeader/8` | 0.481566 | **CLEVER IMPROVISER** **FEAT 5** |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/13/SectionHeader/4` | 0.460689 | **ADAPTIVE ADEPT** **FEAT 5** |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/5/SectionHeader/2` | 0.452635 | **ADVANCED TARGETING SYSTEM** **FEAT 5** |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/13/SectionHeader/12` | 0.440898 | **CONFIDENT ACTUALIZATION **[free-action] **FEAT 5** |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/9/SectionHeader/3` | 0.427666 | **MOLECULAR MODIFICATION** **FEAT 5** |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/17/Text/11` | 0.426030 | **HISTORIAN** **FEAT 5** |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/17/SectionHeader/7` | 0.411555 | **DOUBLE DRAW **[one-action] **FEAT 5** |

### Query 109
- Text: What are the requirements for **PROTECTIVE SUBROUTINE** **FEAT 5**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/5/SectionHeader/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/5/SectionHeader/10', 'PZO22001 Starfinder Player Core 040-057::/page/5/SectionHeader/20', 'PZO22001 Starfinder Player Core 040-057::/page/5/SectionHeader/6']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/5/SectionHeader/10` | 0.929281 | **PROTECTIVE SUBROUTINE** **FEAT 5** |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/5/SectionHeader/20` | 0.627941 | **OFFENSIVE SUBROUTINE** **FEAT 9** |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/5/SectionHeader/6` | 0.529428 | **MACHINE SABOTEUR** **FEAT 5** |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/13/SectionHeader/4` | 0.458302 | **ADAPTIVE ADEPT** **FEAT 5** |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/17/Text/18` | 0.450697 | **MASKED** **FEAT 5** |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/13/SectionHeader/8` | 0.450681 | **CLEVER IMPROVISER** **FEAT 5** |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/13/SectionHeader/12` | 0.432779 | **CONFIDENT ACTUALIZATION **[free-action] **FEAT 5** |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/17/Text/11` | 0.427864 | **HISTORIAN** **FEAT 5** |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/9/Text/8` | 0.404155 | **VENT GAS **[one-action] **FEAT 5** |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/9/SectionHeader/3` | 0.402948 | **MOLECULAR MODIFICATION** **FEAT 5** |

### Query 110
- Text: What are the requirements for **Prerequisites** Nanite Surge?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/5/Text/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/5/Text/13', 'PZO22001 Starfinder Player Core 040-057::/page/5/Text/34', 'PZO22001 Starfinder Player Core 040-057::/page/5/Text/23']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/13` | 0.969553 | **Prerequisites** Nanite Surge |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/34` | 0.969553 | **Prerequisites** Nanite Surge |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/23` | 0.969553 | **Prerequisites** Nanite Surge |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/4/SectionHeader/25` | 0.631529 | **NANITE SURGE **[reaction] **FEAT 1** |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/24` | 0.575110 | Nanites augment your attacks. You can choose to activate  Nanite Surge when you attempt an attack roll, instead of  when you attempt a skill action. If you do, you gain a +1  status bonus to the trigg |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/14` | 0.561378 | Your nanites augment your defenses. You can choose to  activate Nanite Surge when you attempt a saving throw  instead of when you attempt a skill action. If you do, you gain  a +2 status bonus to the |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/36` | 0.546847 | body's efficiency more often. You can use Nanite Surge with a  frequency of once per 10 minutes, rather than once per hour. |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/17/Text/52` | 0.480707 | **Prerequisites** Natural Grace |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/35` | 0.449090 | Your nanites are incredibly effective, capable of improving your |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/9/SectionHeader/47` | 0.424977 | **Prerequisites** Convergent Evolution |

### Query 111
- Text: What are the requirements for **INTERNAL RESPIRATOR** **FEAT 9**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/5/SectionHeader/16']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/5/SectionHeader/16', 'PZO22001 Starfinder Player Core 040-057::/page/13/SectionHeader/28', 'PZO22001 Starfinder Player Core 040-057::/page/5/SectionHeader/20']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/5/SectionHeader/16` | 0.906064 | **INTERNAL RESPIRATOR** **FEAT 9** |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/13/SectionHeader/28` | 0.549436 | **MULTITALENTED** **FEAT 9** |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/5/SectionHeader/20` | 0.528330 | **OFFENSIVE SUBROUTINE** **FEAT 9** |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/13/SectionHeader/23` | 0.485219 | **INCREDIBLE IMPROVISATION **[free-action] **FEAT 9** |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/5/SectionHeader/25` | 0.476215 | **REPAIR MODULE **[one-action] **FEAT 9** |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/4/SectionHeader/17` | 0.452533 | **INTERNAL COMPARTMENT** **FEAT 1** |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/9/SectionHeader/19` | 0.446733 | **EXPANSIVE VERSE** **FEAT 9** |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/13/SectionHeader/19` | 0.446675 | **COOPERATIVE SOUL** **FEAT 9** |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/17/Text/26` | 0.433301 | **HISTORY BUFF** **FEAT 9** |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/17/SectionHeader/30` | 0.432999 | **UNCANNY AWARENESS** **FEAT 9** |

### Query 112
- Text: What are the requirements for **OFFENSIVE SUBROUTINE** **FEAT 9**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/5/SectionHeader/20']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/5/SectionHeader/20', 'PZO22001 Starfinder Player Core 040-057::/page/5/SectionHeader/10', 'PZO22001 Starfinder Player Core 040-057::/page/9/SectionHeader/19']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/5/SectionHeader/20` | 0.926112 | **OFFENSIVE SUBROUTINE** **FEAT 9** |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/5/SectionHeader/10` | 0.676181 | **PROTECTIVE SUBROUTINE** **FEAT 5** |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/9/SectionHeader/19` | 0.571888 | **EXPANSIVE VERSE** **FEAT 9** |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/13/SectionHeader/28` | 0.488378 | **MULTITALENTED** **FEAT 9** |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/5/SectionHeader/16` | 0.468284 | **INTERNAL RESPIRATOR** **FEAT 9** |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/17/Text/26` | 0.467710 | **HISTORY BUFF** **FEAT 9** |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/13/SectionHeader/23` | 0.466039 | **INCREDIBLE IMPROVISATION **[free-action] **FEAT 9** |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/13/SectionHeader/19` | 0.444815 | **COOPERATIVE SOUL** **FEAT 9** |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/17/SectionHeader/30` | 0.437480 | **UNCANNY AWARENESS** **FEAT 9** |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/9/SectionHeader/15` | 0.430402 | **CONVERGENT EVOLUTION** **FEAT 9** |

### Query 113
- Text: What are the requirements for **Prerequisites** Nanite Surge?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/5/Text/23']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/5/Text/13', 'PZO22001 Starfinder Player Core 040-057::/page/5/Text/34', 'PZO22001 Starfinder Player Core 040-057::/page/5/Text/23']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/13` | 0.969553 | **Prerequisites** Nanite Surge |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/34` | 0.969553 | **Prerequisites** Nanite Surge |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/23` | 0.969553 | **Prerequisites** Nanite Surge |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/4/SectionHeader/25` | 0.631529 | **NANITE SURGE **[reaction] **FEAT 1** |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/24` | 0.575110 | Nanites augment your attacks. You can choose to activate  Nanite Surge when you attempt an attack roll, instead of  when you attempt a skill action. If you do, you gain a +1  status bonus to the trigg |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/14` | 0.561378 | Your nanites augment your defenses. You can choose to  activate Nanite Surge when you attempt a saving throw  instead of when you attempt a skill action. If you do, you gain  a +2 status bonus to the |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/36` | 0.546847 | body's efficiency more often. You can use Nanite Surge with a  frequency of once per 10 minutes, rather than once per hour. |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/17/Text/52` | 0.480707 | **Prerequisites** Natural Grace |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/35` | 0.449090 | Your nanites are incredibly effective, capable of improving your |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/9/SectionHeader/47` | 0.424977 | **Prerequisites** Convergent Evolution |

### Query 114
- Text: What are the requirements for **REPAIR MODULE **[one-action] **FEAT 9**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/5/SectionHeader/25']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/5/SectionHeader/25', 'PZO22001 Starfinder Player Core 040-057::/page/13/SectionHeader/23', 'PZO22001 Starfinder Player Core 040-057::/page/5/SectionHeader/16']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/5/SectionHeader/25` | 0.947802 | **REPAIR MODULE **[one-action] **FEAT 9** |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/13/SectionHeader/23` | 0.556380 | **INCREDIBLE IMPROVISATION **[free-action] **FEAT 9** |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/5/SectionHeader/16` | 0.544392 | **INTERNAL RESPIRATOR** **FEAT 9** |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/4/SectionHeader/21` | 0.490995 | **MEMORY RECOVERY** **FEAT 1** |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/17/SectionHeader/7` | 0.473877 | **DOUBLE DRAW **[one-action] **FEAT 5** |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/9/Text/8` | 0.465997 | **VENT GAS **[one-action] **FEAT 5** |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/13/SectionHeader/28` | 0.464622 | **MULTITALENTED** **FEAT 9** |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/5/SectionHeader/37` | 0.457560 | **REVIVIFICATION PROTOCOL **[free-action] **FEAT 13** |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/5/SectionHeader/20` | 0.438361 | **OFFENSIVE SUBROUTINE** **FEAT 9** |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/13/SectionHeader/19` | 0.437118 | **COOPERATIVE SOUL** **FEAT 9** |

### Query 115
- Text: What are the requirements for **CONSISTENT SURGE** **FEAT 13**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/5/SectionHeader/31']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/5/SectionHeader/31', 'PZO22001 Starfinder Player Core 040-057::/page/13/SectionHeader/33', 'PZO22001 Starfinder Player Core 040-057::/page/5/Text/13']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/5/SectionHeader/31` | 0.908610 | **CONSISTENT SURGE** **FEAT 13** |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/13/SectionHeader/33` | 0.563492 | **ADVANCED GENERAL TRAINING** **FEAT 13** |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/13` | 0.555163 | **Prerequisites** Nanite Surge |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/34` | 0.513163 | **Prerequisites** Nanite Surge |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/23` | 0.513163 | **Prerequisites** Nanite Surge |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/5/SectionHeader/43` | 0.503565 | **SYNTHETIC SPEECH** **FEAT 13** |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/13/SectionHeader/44` | 0.495767 | **STUBBORN PERSISTENCE** **FEAT 13** |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/17/SectionHeader/35` | 0.491764 | **DISCIPLE OF THE CYCLE** **FEAT 13** |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/13/Text/52` | 0.465681 | **Requirements** Confident Actualization |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/9/SectionHeader/47` | 0.454859 | **Prerequisites** Convergent Evolution |

### Query 116
- Text: What are the requirements for **Prerequisites** Nanite Surge?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/5/Text/34']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/5/Text/13', 'PZO22001 Starfinder Player Core 040-057::/page/5/Text/34', 'PZO22001 Starfinder Player Core 040-057::/page/5/Text/23']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/13` | 0.969553 | **Prerequisites** Nanite Surge |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/34` | 0.969553 | **Prerequisites** Nanite Surge |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/23` | 0.969553 | **Prerequisites** Nanite Surge |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/4/SectionHeader/25` | 0.631529 | **NANITE SURGE **[reaction] **FEAT 1** |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/24` | 0.575110 | Nanites augment your attacks. You can choose to activate  Nanite Surge when you attempt an attack roll, instead of  when you attempt a skill action. If you do, you gain a +1  status bonus to the trigg |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/14` | 0.561378 | Your nanites augment your defenses. You can choose to  activate Nanite Surge when you attempt a saving throw  instead of when you attempt a skill action. If you do, you gain  a +2 status bonus to the |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/36` | 0.546847 | body's efficiency more often. You can use Nanite Surge with a  frequency of once per 10 minutes, rather than once per hour. |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/17/Text/52` | 0.480707 | **Prerequisites** Natural Grace |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/35` | 0.449090 | Your nanites are incredibly effective, capable of improving your |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/9/SectionHeader/47` | 0.424977 | **Prerequisites** Convergent Evolution |

### Query 117
- Text: What are the requirements for **REVIVIFICATION PROTOCOL **[free-action] **FEAT 13**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/5/SectionHeader/37']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/5/SectionHeader/37', 'PZO22001 Starfinder Player Core 040-057::/page/17/SectionHeader/35', 'PZO22001 Starfinder Player Core 040-057::/page/13/SectionHeader/23']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/5/SectionHeader/37` | 0.953908 | **REVIVIFICATION PROTOCOL **[free-action] **FEAT 13** |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/17/SectionHeader/35` | 0.531375 | **DISCIPLE OF THE CYCLE** **FEAT 13** |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/13/SectionHeader/23` | 0.508797 | **INCREDIBLE IMPROVISATION **[free-action] **FEAT 9** |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/13/SectionHeader/33` | 0.454830 | **ADVANCED GENERAL TRAINING** **FEAT 13** |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/13/SectionHeader/12` | 0.453157 | **CONFIDENT ACTUALIZATION **[free-action] **FEAT 5** |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/13/SectionHeader/38` | 0.451914 | **INNER WELLSPRING **[one-action] **FEAT 13** |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/9/SectionHeader/25` | 0.436707 | **CORROSIVE VENTING** **FEAT 13** |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/9/SectionHeader/30` | 0.427647 | **INTERNAL CHEMISTRY** **FEAT 13** |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/5/SectionHeader/31` | 0.415986 | **CONSISTENT SURGE** **FEAT 13** |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/5/SectionHeader/43` | 0.413950 | **SYNTHETIC SPEECH** **FEAT 13** |

### Query 118
- Text: What are the requirements for **SYNTHETIC SPEECH** **FEAT 13**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/5/SectionHeader/43']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/5/SectionHeader/43', 'PZO22001 Starfinder Player Core 040-057::/page/17/SectionHeader/35', 'PZO22001 Starfinder Player Core 040-057::/page/9/SectionHeader/30']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/5/SectionHeader/43` | 0.905396 | **SYNTHETIC SPEECH** **FEAT 13** |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/17/SectionHeader/35` | 0.596632 | **DISCIPLE OF THE CYCLE** **FEAT 13** |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/9/SectionHeader/30` | 0.553487 | **INTERNAL CHEMISTRY** **FEAT 13** |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/13/SectionHeader/33` | 0.510797 | **ADVANCED GENERAL TRAINING** **FEAT 13** |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/5/SectionHeader/31` | 0.489983 | **CONSISTENT SURGE** **FEAT 13** |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/17/SectionHeader/39` | 0.451198 | **PERFECTLY BALANCED** **FEAT 13** |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/13/SectionHeader/44` | 0.442852 | **STUBBORN PERSISTENCE** **FEAT 13** |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/5/SectionHeader/37` | 0.428607 | **REVIVIFICATION PROTOCOL **[free-action] **FEAT 13** |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/17/SectionHeader/34` | 0.426826 | 13TH LEVEL |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/22` | 0.418290 | **GENERAL TRAINING** **FEAT 1** |

### Query 119
- Text: What are the requirements for **Prerequisites** artificial scion android or networked android  heritage?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/5/Text/46']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/5/Text/46', 'PZO22001 Starfinder Player Core 040-057::/page/3/SectionHeader/23', 'PZO22001 Starfinder Player Core 040-057::/page/3/SectionHeader/27']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/46` | 0.957247 | **Prerequisites** artificial scion android or networked android  heritage |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/3/SectionHeader/23` | 0.622269 | ARTIFICIAL SCION ANDROID |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/3/SectionHeader/27` | 0.581871 | NETWORKED ANDROID |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/22` | 0.533696 | An android's heritage often reflects the purpose for which  they were originally created or how they've adapted their  body to best suit their present life. Choose one of the  following android herita |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/3/SectionHeader/21` | 0.521838 | ANDROID HERITAGES |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/4/Text/5` | 0.493402 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As an android, you choose from among  the following |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/7/Text/32` | 0.452165 | **Android** |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/38` | 0.452165 | **Android** |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/15/Text/33` | 0.452165 | **Android** |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/67` | 0.452165 | **Android** |

### Query 120
- Text: What are the requirements for **MEMORY MATRIX** **FEAT 17**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/5/SectionHeader/49']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/5/SectionHeader/49', 'PZO22001 Starfinder Player Core 040-057::/page/9/SectionHeader/44', 'PZO22001 Starfinder Player Core 040-057::/page/13/SectionHeader/49']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/5/SectionHeader/49` | 0.896492 | **MEMORY MATRIX** **FEAT 17** |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/9/SectionHeader/44` | 0.570697 | **MANIFOLD EVOLUTION** **FEAT 17** |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/13/SectionHeader/49` | 0.517440 | **PERSISTENT CONFIDENCE** **FEAT 17** |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/4/SectionHeader/21` | 0.471486 | **MEMORY RECOVERY** **FEAT 1** |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/17/SectionHeader/45` | 0.466802 | **CLEANSE SPIRIT** **FEAT 17** |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/9/SectionHeader/35` | 0.461547 | **COMBINE **[two-actions] **FEAT 17** |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/5/SectionHeader/48` | 0.448532 | 17TH LEVEL |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/13/SectionHeader/48` | 0.448532 | 17TH LEVEL |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/5/SectionHeader/53` | 0.443477 | **NANITE FORM **[two-actions] **FEAT 17** |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/17/SectionHeader/49` | 0.442053 | **RELIABLE GRACE** **FEAT 17** |

### Query 121
- Text: What are the requirements for **NANITE FORM **[two-actions] **FEAT 17**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/5/SectionHeader/53']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/5/SectionHeader/53', 'PZO22001 Starfinder Player Core 040-057::/page/9/SectionHeader/35', 'PZO22001 Starfinder Player Core 040-057::/page/5/Text/23']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/5/SectionHeader/53` | 0.938194 | **NANITE FORM **[two-actions] **FEAT 17** |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/9/SectionHeader/35` | 0.645205 | **COMBINE **[two-actions] **FEAT 17** |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/23` | 0.582264 | **Prerequisites** Nanite Surge |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/34` | 0.540264 | **Prerequisites** Nanite Surge |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/13` | 0.540264 | **Prerequisites** Nanite Surge |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/4/SectionHeader/25` | 0.534679 | **NANITE SURGE **[reaction] **FEAT 1** |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/9/SectionHeader/44` | 0.464673 | **MANIFOLD EVOLUTION** **FEAT 17** |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/5/SectionHeader/49` | 0.455101 | **MEMORY MATRIX** **FEAT 17** |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/17/SectionHeader/45` | 0.445225 | **CLEANSE SPIRIT** **FEAT 17** |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/24` | 0.429484 | Nanites augment your attacks. You can choose to activate  Nanite Surge when you attempt an attack roll, instead of  when you attempt a skill action. If you do, you gain a +1  status bonus to the trigg |

### Query 122
- Text: What are the requirements for **ADAPTABLE LIMBS** **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/8/SectionHeader/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/8/SectionHeader/6', 'PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/6', 'PZO22001 Starfinder Player Core 040-057::/page/13/SectionHeader/4']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/8/SectionHeader/6` | 0.920111 | **ADAPTABLE LIMBS** **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/6` | 0.563495 | **ADAPTED AUGMENTATIONS** **FEAT 1** |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/13/SectionHeader/4` | 0.562347 | **ADAPTIVE ADEPT** **FEAT 5** |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/8/SectionHeader/16` | 0.508608 | **DARKVISION ADAPTATION** **FEAT 1** |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/4/SectionHeader/30` | 0.484137 | **NIGHTVISION ADAPTATION** **FEAT 1** |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/12` | 0.482524 | **ADAPTED CANTRIP** **FEAT 1** |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/12/Text/25` | 0.470768 | Your adaptability manifests in your mastery of a range of  useful abilities. You gain a 1st-level general feat. You must  meet the feat's prerequisites, but if you select this feat during  character c |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/6/SectionHeader/14` | 0.428287 | GENETIC ADAPTATION |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/31` | 0.418046 | **NATURAL SKILL** **FEAT 1** |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/13/Text/36` | 0.413040 | Over the course of adventuring, your adaptability has let you  pick up numerous useful abilities. You gain a general feat of  7th level or lower. You must meet the feat's prerequisites. |

### Query 123
- Text: What are the requirements for **BARATHU LORE** **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/8/SectionHeader/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/8/SectionHeader/11', 'PZO22001 Starfinder Player Core 040-057::/page/16/SectionHeader/18', 'PZO22001 Starfinder Player Core 040-057::/page/8/SectionHeader/13']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/8/SectionHeader/11` | 0.878122 | **BARATHU LORE** **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/16/SectionHeader/18` | 0.669297 | **KASATHA LORE** **FEAT 1** |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/8/SectionHeader/13` | 0.636614 | **BARATHU** |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/8/SectionHeader/8` | 0.594614 | **BARATHU** |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/8/SectionHeader/18` | 0.594614 | **BARATHU** |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/8/SectionHeader/32` | 0.594614 | **BARATHU** |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/8/SectionHeader/36` | 0.594614 | **BARATHU** |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/8/SectionHeader/22` | 0.594614 | **BARATHU** |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/8/SectionHeader/27` | 0.594614 | **BARATHU** |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/9/SectionHeader/46` | 0.594614 | **BARATHU** |

### Query 124
- Text: What are the requirements for **DARKVISION ADAPTATION** **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/8/SectionHeader/16']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/8/SectionHeader/16', 'PZO22001 Starfinder Player Core 040-057::/page/4/SectionHeader/30', 'PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/6']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/8/SectionHeader/16` | 0.927363 | **DARKVISION ADAPTATION** **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/4/SectionHeader/30` | 0.775333 | **NIGHTVISION ADAPTATION** **FEAT 1** |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/6` | 0.580156 | **ADAPTED AUGMENTATIONS** **FEAT 1** |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/13/SectionHeader/4` | 0.511401 | **ADAPTIVE ADEPT** **FEAT 5** |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/12` | 0.481254 | **ADAPTED CANTRIP** **FEAT 1** |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/12/Text/25` | 0.470159 | Your adaptability manifests in your mastery of a range of  useful abilities. You gain a 1st-level general feat. You must  meet the feat's prerequisites, but if you select this feat during  character c |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/8/Text/19` | 0.452916 | You've explored the darkest regions of space and found ways  to adapt. You gain darkvision. |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/4/Text/33` | 0.438517 | The nanites in your ocular processors have adapted to  darkness, enhancing your ability to see in the dark. You gain  darkvision. |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/8/SectionHeader/6` | 0.436441 | **ADAPTABLE LIMBS** **FEAT 1** |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/6/SectionHeader/14` | 0.434294 | GENETIC ADAPTATION |

### Query 125
- Text: What are the requirements for **DERMAL SPIKES** **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/8/SectionHeader/20']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/8/SectionHeader/20', 'PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/31', 'PZO22001 Starfinder Player Core 040-057::/page/7/Text/47']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/8/SectionHeader/20` | 0.886752 | **DERMAL SPIKES** **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/31` | 0.487645 | **NATURAL SKILL** **FEAT 1** |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/7/Text/47` | 0.452721 | **SKILLS** **FEATS** |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/47` | 0.410721 | **SKILLS** **FEATS** |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/11/Text/46` | 0.410721 | **SKILLS** **FEATS** |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/9/Text/68` | 0.410721 | **SKILLS** **FEATS** |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/15/Text/49` | 0.410721 | **SKILLS** **FEATS** |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/22` | 0.389961 | **GENERAL TRAINING** **FEAT 1** |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/8/Text/24` | 0.349943 | **Piercing Spikes** [reaction] **Trigger** You become grabbed by a  creature; **Effect** You twist and thrash your body around,  dealing 1d4 plus your Strength modifier piercing damage  to the trigger |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/34` | 0.349169 | As a starting character, you can choose from only 1stlevel ancestry feats, but later choices can be made from any  feat of your level or lower. These feats also sometimes list  prerequisites, which ar |

### Query 126
- Text: What are the requirements for **GRASPING TENDRILS** **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/8/SectionHeader/25']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/8/SectionHeader/25', 'PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/22', 'PZO22001 Starfinder Player Core 040-057::/page/8/SectionHeader/34']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/8/SectionHeader/25` | 0.910017 | **GRASPING TENDRILS** **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/22` | 0.487667 | **GENERAL TRAINING** **FEAT 1** |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/8/SectionHeader/34` | 0.462565 | **TENTACLE WHIP** **FEAT 1** |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/17/Text/52` | 0.386447 | **Prerequisites** Natural Grace |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/31` | 0.383263 | **NATURAL SKILL** **FEAT 1** |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/12/Text/25` | 0.378555 | Your adaptability manifests in your mastery of a range of  useful abilities. You gain a 1st-level general feat. You must  meet the feat's prerequisites, but if you select this feat during  character c |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/17/Text/2` | 0.360586 | **NATURAL GRACE **[free-action] **FEAT 1** |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/12` | 0.349463 | **ADAPTED CANTRIP** **FEAT 1** |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/9/Text/28` | 0.344119 | **Prerequisites** Vent Gas |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/9/Text/68` | 0.341365 | **SKILLS** **FEATS** |

### Query 127
- Text: What are the requirements for **METABOLIC MANIPULATION** **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/8/SectionHeader/30']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/8/SectionHeader/30', 'PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/22', 'PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/31']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/8/SectionHeader/30` | 0.895375 | **METABOLIC MANIPULATION** **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/22` | 0.544046 | **GENERAL TRAINING** **FEAT 1** |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/31` | 0.524211 | **NATURAL SKILL** **FEAT 1** |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/9/SectionHeader/3` | 0.481270 | **MOLECULAR MODIFICATION** **FEAT 5** |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/27` | 0.435067 | **NATURAL AMBITION** **FEAT 1** |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/15/Text/49` | 0.407527 | **SKILLS** **FEATS** |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/11/Text/46` | 0.407527 | **SKILLS** **FEATS** |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/9/Text/68` | 0.407527 | **SKILLS** **FEATS** |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/47` | 0.407527 | **SKILLS** **FEATS** |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/7/Text/47` | 0.407527 | **SKILLS** **FEATS** |

### Query 128
- Text: What are the requirements for **TENTACLE WHIP** **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/8/SectionHeader/34']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/8/SectionHeader/34', 'PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/22', 'PZO22001 Starfinder Player Core 040-057::/page/8/Text/37']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/8/SectionHeader/34` | 0.883682 | **TENTACLE WHIP** **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/22` | 0.494949 | **GENERAL TRAINING** **FEAT 1** |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/8/Text/37` | 0.482322 | You grow a tentacle that can lash out like a whip. You  gain a tentacle unarmed attack that deals 1d6 bludgeoning  damage. Your tentacle is in the brawling weapon group and  has the barathu, finesse, |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/31` | 0.417041 | **NATURAL SKILL** **FEAT 1** |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/8/SectionHeader/25` | 0.410538 | **GRASPING TENDRILS** **FEAT 1** |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/35` | 0.375733 | **UNCONVENTIONAL WEAPONRY** **FEAT 1** |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/12` | 0.375624 | **ADAPTED CANTRIP** **FEAT 1** |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/12/Text/25` | 0.345462 | Your adaptability manifests in your mastery of a range of  useful abilities. You gain a 1st-level general feat. You must  meet the feat's prerequisites, but if you select this feat during  character c |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/9/Text/28` | 0.343958 | **Prerequisites** Vent Gas |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/7/Text/47` | 0.341719 | **SKILLS** **FEATS** |

### Query 129
- Text: What are the requirements for **FLUID ANATOMY **[reaction] **FEAT 5**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/8/SectionHeader/39']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/8/SectionHeader/39', 'PZO22001 Starfinder Player Core 040-057::/page/9/SectionHeader/3', 'PZO22001 Starfinder Player Core 040-057::/page/9/Text/8']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/8/SectionHeader/39` | 0.905941 | **FLUID ANATOMY **[reaction] **FEAT 5** |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/9/SectionHeader/3` | 0.528812 | **MOLECULAR MODIFICATION** **FEAT 5** |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/9/Text/8` | 0.517131 | **VENT GAS **[one-action] **FEAT 5** |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/13/SectionHeader/12` | 0.453675 | **CONFIDENT ACTUALIZATION **[free-action] **FEAT 5** |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/17/SectionHeader/7` | 0.453270 | **DOUBLE DRAW **[one-action] **FEAT 5** |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/17/Text/11` | 0.435190 | **HISTORIAN** **FEAT 5** |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/17/Text/18` | 0.430600 | **MASKED** **FEAT 5** |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/5/SectionHeader/10` | 0.419713 | **PROTECTIVE SUBROUTINE** **FEAT 5** |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/13/SectionHeader/4` | 0.415423 | **ADAPTIVE ADEPT** **FEAT 5** |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/9/SectionHeader/30` | 0.407892 | **INTERNAL CHEMISTRY** **FEAT 13** |

### Query 130
- Text: What are the requirements for **MOLECULAR MODIFICATION** **FEAT 5**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/9/SectionHeader/3']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/9/SectionHeader/3', 'PZO22001 Starfinder Player Core 040-057::/page/13/SectionHeader/8', 'PZO22001 Starfinder Player Core 040-057::/page/13/SectionHeader/12']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/9/SectionHeader/3` | 0.922393 | **MOLECULAR MODIFICATION** **FEAT 5** |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/13/SectionHeader/8` | 0.558489 | **CLEVER IMPROVISER** **FEAT 5** |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/13/SectionHeader/12` | 0.552213 | **CONFIDENT ACTUALIZATION **[free-action] **FEAT 5** |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/17/Text/18` | 0.488639 | **MASKED** **FEAT 5** |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/13/SectionHeader/4` | 0.479349 | **ADAPTIVE ADEPT** **FEAT 5** |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/8/SectionHeader/39` | 0.465047 | **FLUID ANATOMY **[reaction] **FEAT 5** |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/8/SectionHeader/30` | 0.449644 | **METABOLIC MANIPULATION** **FEAT 1** |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/5/SectionHeader/6` | 0.444525 | **MACHINE SABOTEUR** **FEAT 5** |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/5/SectionHeader/10` | 0.434117 | **PROTECTIVE SUBROUTINE** **FEAT 5** |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/17/Text/11` | 0.421686 | **HISTORIAN** **FEAT 5** |

### Query 131
- Text: What are the requirements for **VENT GAS **[one-action] **FEAT 5**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/9/Text/8']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/9/Text/8', 'PZO22001 Starfinder Player Core 040-057::/page/9/Text/28', 'PZO22001 Starfinder Player Core 040-057::/page/17/SectionHeader/7']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/9/Text/8` | 0.906806 | **VENT GAS **[one-action] **FEAT 5** |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/9/Text/28` | 0.730207 | **Prerequisites** Vent Gas |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/17/SectionHeader/7` | 0.592795 | **DOUBLE DRAW **[one-action] **FEAT 5** |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/13/SectionHeader/12` | 0.486057 | **CONFIDENT ACTUALIZATION **[free-action] **FEAT 5** |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/9/Text/12` | 0.483669 | You vent gas to propel yourself forward. All squares in a  5-foot emanation become filled with gas. All creatures in  the gas become concealed, and all creatures outside the gas  become concealed to c |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/8/SectionHeader/39` | 0.477465 | **FLUID ANATOMY **[reaction] **FEAT 5** |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/9/Text/29` | 0.476057 | You can control causticity as you vent your gases. When you  Vent Gas, increase the area of your emanation to 10 feet. You  can choose to make the gas you vent caustic. If you do, any  non-barathu cre |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/17/Text/18` | 0.457783 | **MASKED** **FEAT 5** |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/5/SectionHeader/10` | 0.443772 | **PROTECTIVE SUBROUTINE** **FEAT 5** |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/5/SectionHeader/25` | 0.439718 | **REPAIR MODULE **[one-action] **FEAT 9** |

### Query 132
- Text: What are the requirements for **CONVERGENT EVOLUTION** **FEAT 9**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/9/SectionHeader/15']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/9/SectionHeader/15', 'PZO22001 Starfinder Player Core 040-057::/page/9/SectionHeader/47', 'PZO22001 Starfinder Player Core 040-057::/page/9/SectionHeader/19']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/9/SectionHeader/15` | 0.900712 | **CONVERGENT EVOLUTION** **FEAT 9** |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/9/SectionHeader/47` | 0.800773 | **Prerequisites** Convergent Evolution |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/9/SectionHeader/19` | 0.572696 | **EXPANSIVE VERSE** **FEAT 9** |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/13/SectionHeader/19` | 0.511429 | **COOPERATIVE SOUL** **FEAT 9** |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/13/SectionHeader/28` | 0.500357 | **MULTITALENTED** **FEAT 9** |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/13/SectionHeader/23` | 0.493560 | **INCREDIBLE IMPROVISATION **[free-action] **FEAT 9** |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/9/SectionHeader/44` | 0.478911 | **MANIFOLD EVOLUTION** **FEAT 17** |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/9/Text/48` | 0.473898 | You've cataloged the genetic code from countless ancestries  you've encountered, and you can draw upon any of them  to enhance and evolve your body. Increase the number of  ancestries you can select w |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/13/Text/52` | 0.462954 | **Requirements** Confident Actualization |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/5/SectionHeader/20` | 0.446889 | **OFFENSIVE SUBROUTINE** **FEAT 9** |

### Query 133
- Text: What are the requirements for **EXPANSIVE VERSE** **FEAT 9**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/9/SectionHeader/19']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/9/SectionHeader/19', 'PZO22001 Starfinder Player Core 040-057::/page/9/SectionHeader/15', 'PZO22001 Starfinder Player Core 040-057::/page/5/SectionHeader/20']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/9/SectionHeader/19` | 0.915522 | **EXPANSIVE VERSE** **FEAT 9** |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/9/SectionHeader/15` | 0.557825 | **CONVERGENT EVOLUTION** **FEAT 9** |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/5/SectionHeader/20` | 0.553290 | **OFFENSIVE SUBROUTINE** **FEAT 9** |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/13/SectionHeader/23` | 0.500836 | **INCREDIBLE IMPROVISATION **[free-action] **FEAT 9** |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/13/SectionHeader/19` | 0.479694 | **COOPERATIVE SOUL** **FEAT 9** |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/13/SectionHeader/28` | 0.476229 | **MULTITALENTED** **FEAT 9** |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/17/Text/26` | 0.464848 | **HISTORY BUFF** **FEAT 9** |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/17/SectionHeader/30` | 0.451268 | **UNCANNY AWARENESS** **FEAT 9** |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/5/SectionHeader/16` | 0.446172 | **INTERNAL RESPIRATOR** **FEAT 9** |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/5/SectionHeader/25` | 0.407559 | **REPAIR MODULE **[one-action] **FEAT 9** |

### Query 134
- Text: What are the requirements for **Prerequisites** dreamer barathu heritage?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/9/SectionHeader/22']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/9/SectionHeader/22', 'PZO22001 Starfinder Player Core 040-057::/page/7/SectionHeader/22', 'PZO22001 Starfinder Player Core 040-057::/page/7/Text/21']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/9/SectionHeader/22` | 0.959694 | **Prerequisites** dreamer barathu heritage |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/7/SectionHeader/22` | 0.657150 | DREAMER BARATHU |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/7/Text/21` | 0.634202 | Choose one of the following barathu heritages at 1st level. |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/7/SectionHeader/20` | 0.581247 | BARATHU HERITAGES |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/8/Text/4` | 0.527578 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th,  9th, 13th, and 17th level). As a barathu, you choose from  among the following a |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/9/SectionHeader/21` | 0.498198 | **BARATHU** |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/8/SectionHeader/8` | 0.486198 | **BARATHU** |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/9/SectionHeader/32` | 0.486198 | **BARATHU** |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/8/SectionHeader/18` | 0.486198 | **BARATHU** |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/8/SectionHeader/22` | 0.486198 | **BARATHU** |

### Query 135
- Text: What are the requirements for **CORROSIVE VENTING** **FEAT 13**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/9/SectionHeader/25']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/9/SectionHeader/25', 'PZO22001 Starfinder Player Core 040-057::/page/13/SectionHeader/33', 'PZO22001 Starfinder Player Core 040-057::/page/17/SectionHeader/35']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/9/SectionHeader/25` | 0.907520 | **CORROSIVE VENTING** **FEAT 13** |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/13/SectionHeader/33` | 0.527201 | **ADVANCED GENERAL TRAINING** **FEAT 13** |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/17/SectionHeader/35` | 0.513370 | **DISCIPLE OF THE CYCLE** **FEAT 13** |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/5/SectionHeader/37` | 0.456758 | **REVIVIFICATION PROTOCOL **[free-action] **FEAT 13** |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/9/SectionHeader/30` | 0.448635 | **INTERNAL CHEMISTRY** **FEAT 13** |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/5/SectionHeader/31` | 0.442338 | **CONSISTENT SURGE** **FEAT 13** |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/13/SectionHeader/32` | 0.426468 | 13TH LEVEL |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/17/SectionHeader/34` | 0.426468 | 13TH LEVEL |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/9/SectionHeader/24` | 0.426468 | 13TH LEVEL |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/5/SectionHeader/43` | 0.425088 | **SYNTHETIC SPEECH** **FEAT 13** |

### Query 136
- Text: What are the requirements for **Prerequisites** Vent Gas?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/9/Text/28']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/9/Text/28', 'PZO22001 Starfinder Player Core 040-057::/page/9/Text/8', 'PZO22001 Starfinder Player Core 040-057::/page/17/Text/52']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/9/Text/28` | 0.949796 | **Prerequisites** Vent Gas |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/9/Text/8` | 0.576753 | **VENT GAS **[one-action] **FEAT 5** |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/17/Text/52` | 0.493142 | **Prerequisites** Natural Grace |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/9/Text/29` | 0.462630 | You can control causticity as you vent your gases. When you  Vent Gas, increase the area of your emanation to 10 feet. You  can choose to make the gas you vent caustic. If you do, any  non-barathu cre |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/9/Text/12` | 0.427825 | You vent gas to propel yourself forward. All squares in a  5-foot emanation become filled with gas. All creatures in  the gas become concealed, and all creatures outside the gas  become concealed to c |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/17/Text/28` | 0.377885 | **Prerequisites** Historian |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/13` | 0.358180 | **Prerequisites** Nanite Surge |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/23` | 0.358180 | **Prerequisites** Nanite Surge |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/34` | 0.358180 | **Prerequisites** Nanite Surge |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/9/SectionHeader/47` | 0.357291 | **Prerequisites** Convergent Evolution |

### Query 137
- Text: What are the requirements for **INTERNAL CHEMISTRY** **FEAT 13**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/9/SectionHeader/30']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/9/SectionHeader/30', 'PZO22001 Starfinder Player Core 040-057::/page/13/SectionHeader/33', 'PZO22001 Starfinder Player Core 040-057::/page/5/SectionHeader/43']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/9/SectionHeader/30` | 0.895031 | **INTERNAL CHEMISTRY** **FEAT 13** |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/13/SectionHeader/33` | 0.570750 | **ADVANCED GENERAL TRAINING** **FEAT 13** |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/5/SectionHeader/43` | 0.557586 | **SYNTHETIC SPEECH** **FEAT 13** |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/17/SectionHeader/35` | 0.512759 | **DISCIPLE OF THE CYCLE** **FEAT 13** |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/13/SectionHeader/38` | 0.486076 | **INNER WELLSPRING **[one-action] **FEAT 13** |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/13/SectionHeader/32` | 0.455771 | 13TH LEVEL |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/17/SectionHeader/34` | 0.443771 | 13TH LEVEL |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/5/SectionHeader/30` | 0.443771 | 13TH LEVEL |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/9/SectionHeader/24` | 0.443771 | 13TH LEVEL |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/9/SectionHeader/25` | 0.441917 | **CORROSIVE VENTING** **FEAT 13** |

### Query 138
- Text: What are the requirements for **COMBINE **[two-actions] **FEAT 17**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/9/SectionHeader/35']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/9/SectionHeader/35', 'PZO22001 Starfinder Player Core 040-057::/page/5/SectionHeader/53', 'PZO22001 Starfinder Player Core 040-057::/page/5/SectionHeader/49']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/9/SectionHeader/35` | 0.921195 | **COMBINE **[two-actions] **FEAT 17** |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/5/SectionHeader/53` | 0.655964 | **NANITE FORM **[two-actions] **FEAT 17** |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/5/SectionHeader/49` | 0.548235 | **MEMORY MATRIX** **FEAT 17** |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/9/SectionHeader/44` | 0.484861 | **MANIFOLD EVOLUTION** **FEAT 17** |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/17/SectionHeader/45` | 0.471315 | **CLEANSE SPIRIT** **FEAT 17** |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/17/SectionHeader/49` | 0.468075 | **RELIABLE GRACE** **FEAT 17** |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/13/SectionHeader/49` | 0.464907 | **PERSISTENT CONFIDENCE** **FEAT 17** |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/17/SectionHeader/7` | 0.455455 | **DOUBLE DRAW **[one-action] **FEAT 5** |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/13/SectionHeader/12` | 0.419297 | **CONFIDENT ACTUALIZATION **[free-action] **FEAT 5** |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/9/Text/8` | 0.416265 | **VENT GAS **[one-action] **FEAT 5** |

### Query 139
- Text: What are the requirements for **MANIFOLD EVOLUTION** **FEAT 17**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/9/SectionHeader/44']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/9/SectionHeader/44', 'PZO22001 Starfinder Player Core 040-057::/page/5/SectionHeader/49', 'PZO22001 Starfinder Player Core 040-057::/page/9/SectionHeader/47']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/9/SectionHeader/44` | 0.903668 | **MANIFOLD EVOLUTION** **FEAT 17** |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/5/SectionHeader/49` | 0.559860 | **MEMORY MATRIX** **FEAT 17** |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/9/SectionHeader/47` | 0.529098 | **Prerequisites** Convergent Evolution |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/9/SectionHeader/15` | 0.475349 | **CONVERGENT EVOLUTION** **FEAT 9** |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/13/SectionHeader/49` | 0.466907 | **PERSISTENT CONFIDENCE** **FEAT 17** |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/5/SectionHeader/53` | 0.445618 | **NANITE FORM **[two-actions] **FEAT 17** |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/9/SectionHeader/35` | 0.442512 | **COMBINE **[two-actions] **FEAT 17** |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/5/SectionHeader/48` | 0.440706 | 17TH LEVEL |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/17/SectionHeader/45` | 0.437694 | **CLEANSE SPIRIT** **FEAT 17** |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/17/SectionHeader/49` | 0.432824 | **RELIABLE GRACE** **FEAT 17** |

### Query 140
- Text: What are the requirements for **Prerequisites** Convergent Evolution?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/9/SectionHeader/47']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/9/SectionHeader/47', 'PZO22001 Starfinder Player Core 040-057::/page/9/SectionHeader/15', 'PZO22001 Starfinder Player Core 040-057::/page/13/Text/52']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/9/SectionHeader/47` | 0.963281 | **Prerequisites** Convergent Evolution |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/9/SectionHeader/15` | 0.629626 | **CONVERGENT EVOLUTION** **FEAT 9** |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/13/Text/52` | 0.558477 | **Requirements** Confident Actualization |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/9/Text/48` | 0.472652 | You've cataloged the genetic code from countless ancestries  you've encountered, and you can draw upon any of them  to enhance and evolve your body. Increase the number of  ancestries you can select w |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/13/SectionHeader/21` | 0.440668 | **Prerequisites** Cooperative Nature |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/17/Text/28` | 0.435883 | **Prerequisites** Historian |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/17/Text/52` | 0.429402 | **Prerequisites** Natural Grace |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/13` | 0.422017 | **Prerequisites** Nanite Surge |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/34` | 0.422017 | **Prerequisites** Nanite Surge |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/23` | 0.422017 | **Prerequisites** Nanite Surge |

### Query 141
- Text: What are the requirements for **ADAPTED AUGMENTATIONS** **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/6', 'PZO22001 Starfinder Player Core 040-057::/page/8/SectionHeader/16', 'PZO22001 Starfinder Player Core 040-057::/page/13/SectionHeader/4']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/6` | 0.914040 | **ADAPTED AUGMENTATIONS** **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/8/SectionHeader/16` | 0.654719 | **DARKVISION ADAPTATION** **FEAT 1** |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/13/SectionHeader/4` | 0.607357 | **ADAPTIVE ADEPT** **FEAT 5** |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/4/SectionHeader/30` | 0.554442 | **NIGHTVISION ADAPTATION** **FEAT 1** |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/12` | 0.546306 | **ADAPTED CANTRIP** **FEAT 1** |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/8/SectionHeader/6` | 0.513010 | **ADAPTABLE LIMBS** **FEAT 1** |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/12/Text/25` | 0.453146 | Your adaptability manifests in your mastery of a range of  useful abilities. You gain a 1st-level general feat. You must  meet the feat's prerequisites, but if you select this feat during  character c |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/6/SectionHeader/14` | 0.429571 | GENETIC ADAPTATION |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/5/SectionHeader/2` | 0.422388 | **ADVANCED TARGETING SYSTEM** **FEAT 5** |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/27` | 0.418339 | **NATURAL AMBITION** **FEAT 1** |

### Query 142
- Text: What are the requirements for **ADAPTED CANTRIP** **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/12']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/12', 'PZO22001 Starfinder Player Core 040-057::/page/13/SectionHeader/4', 'PZO22001 Starfinder Player Core 040-057::/page/8/SectionHeader/16']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/12` | 0.913736 | **ADAPTED CANTRIP** **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/13/SectionHeader/4` | 0.592086 | **ADAPTIVE ADEPT** **FEAT 5** |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/8/SectionHeader/16` | 0.568330 | **DARKVISION ADAPTATION** **FEAT 1** |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/6` | 0.518700 | **ADAPTED AUGMENTATIONS** **FEAT 1** |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/13/Text/6` | 0.504330 | **Prerequisites** Adapted Cantrip, can cast 3rd-rank spells |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/4/SectionHeader/30` | 0.488915 | **NIGHTVISION ADAPTATION** **FEAT 1** |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/8/SectionHeader/6` | 0.453057 | **ADAPTABLE LIMBS** **FEAT 1** |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/12/Text/25` | 0.446598 | Your adaptability manifests in your mastery of a range of  useful abilities. You gain a 1st-level general feat. You must  meet the feat's prerequisites, but if you select this feat during  character c |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/22` | 0.434996 | **GENERAL TRAINING** **FEAT 1** |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/13/Text/7` | 0.419925 | You've continued adapting your magic to blend your class's  tradition with your adapted tradition. Choose a cantrip or  1st-rank spell from the same magical tradition as your cantrip  from Adapted Can |

### Query 143
- Text: What are the requirements for **Prerequisites** spellcasting class feature?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/12/Text/15']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/12/Text/15', 'PZO22001 Starfinder Player Core 040-057::/page/12/Text/30', 'PZO22001 Starfinder Player Core 040-057::/page/1/Text/52']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/12/Text/15` | 0.947238 | **Prerequisites** spellcasting class feature |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/12/Text/30` | 0.471940 | You were raised to be ambitious and always reach for the  stars, leading you to progress quickly in your chosen field. You  gain a 1st-level class feat for your class. You must meet the  prerequisites |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/52` | 0.465370 | **Languages** **CLASSES** |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/34` | 0.413298 | As a starting character, you can choose from only 1stlevel ancestry feats, but later choices can be made from any  feat of your level or lower. These feats also sometimes list  prerequisites, which ar |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/15/Text/48` | 0.410402 | **CLASSES** |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/17/Text/72` | 0.410402 | **CLASSES** |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/5/Text/82` | 0.410402 | **CLASSES** |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/9/Text/67` | 0.410401 | **CLASSES** |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/13/Text/77` | 0.410401 | **CLASSES** |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/46` | 0.410401 | **CLASSES** |

### Query 144
- Text: What are the requirements for **COOPERATIVE NATURE** **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/18']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/18', 'PZO22001 Starfinder Player Core 040-057::/page/13/SectionHeader/21', 'PZO22001 Starfinder Player Core 040-057::/page/13/SectionHeader/19']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/18` | 0.888972 | **COOPERATIVE NATURE** **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/13/SectionHeader/21` | 0.846867 | **Prerequisites** Cooperative Nature |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/13/SectionHeader/19` | 0.583262 | **COOPERATIVE SOUL** **FEAT 9** |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/31` | 0.473341 | **NATURAL SKILL** **FEAT 1** |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/27` | 0.464716 | **NATURAL AMBITION** **FEAT 1** |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/22` | 0.455235 | **GENERAL TRAINING** **FEAT 1** |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/17/Text/52` | 0.431342 | **Prerequisites** Natural Grace |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/9/SectionHeader/47` | 0.387982 | **Prerequisites** Convergent Evolution |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/4/SectionHeader/34` | 0.379161 | **QUICKENED PROCESSOR** **FEAT 1** |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/17/Text/2` | 0.375073 | **NATURAL GRACE **[free-action] **FEAT 1** |

### Query 145
- Text: What are the requirements for **GENERAL TRAINING** **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/22']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/22', 'PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/31', 'PZO22001 Starfinder Player Core 040-057::/page/13/SectionHeader/33']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/22` | 0.920034 | **GENERAL TRAINING** **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/31` | 0.638008 | **NATURAL SKILL** **FEAT 1** |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/13/SectionHeader/33` | 0.612714 | **ADVANCED GENERAL TRAINING** **FEAT 13** |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/15/Text/49` | 0.479503 | **SKILLS** **FEATS** |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/47` | 0.479503 | **SKILLS** **FEATS** |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/11/Text/46` | 0.479503 | **SKILLS** **FEATS** |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/7/Text/47` | 0.479503 | **SKILLS** **FEATS** |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/9/Text/68` | 0.479503 | **SKILLS** **FEATS** |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/12/Text/25` | 0.454679 | Your adaptability manifests in your mastery of a range of  useful abilities. You gain a 1st-level general feat. You must  meet the feat's prerequisites, but if you select this feat during  character c |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/27` | 0.416313 | **NATURAL AMBITION** **FEAT 1** |

### Query 146
- Text: What are the requirements for **NATURAL AMBITION** **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/27']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/27', 'PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/31', 'PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/22']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/27` | 0.894979 | **NATURAL AMBITION** **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/31` | 0.695982 | **NATURAL SKILL** **FEAT 1** |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/22` | 0.579139 | **GENERAL TRAINING** **FEAT 1** |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/17/Text/2` | 0.514529 | **NATURAL GRACE **[free-action] **FEAT 1** |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/17/Text/52` | 0.488066 | **Prerequisites** Natural Grace |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/4/SectionHeader/30` | 0.480071 | **NIGHTVISION ADAPTATION** **FEAT 1** |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/18` | 0.457562 | **COOPERATIVE NATURE** **FEAT 1** |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/8/SectionHeader/16` | 0.436378 | **DARKVISION ADAPTATION** **FEAT 1** |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/12/Text/30` | 0.425284 | You were raised to be ambitious and always reach for the  stars, leading you to progress quickly in your chosen field. You  gain a 1st-level class feat for your class. You must meet the  prerequisites |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/12/Text/25` | 0.410279 | Your adaptability manifests in your mastery of a range of  useful abilities. You gain a 1st-level general feat. You must  meet the feat's prerequisites, but if you select this feat during  character c |

### Query 147
- Text: What are the requirements for **NATURAL SKILL** **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/31']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/31', 'PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/22', 'PZO22001 Starfinder Player Core 040-057::/page/3/Text/47']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/31` | 0.904216 | **NATURAL SKILL** **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/22` | 0.678749 | **GENERAL TRAINING** **FEAT 1** |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/3/Text/47` | 0.631766 | **SKILLS** **FEATS** |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/7/Text/47` | 0.589766 | **SKILLS** **FEATS** |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/9/Text/68` | 0.589766 | **SKILLS** **FEATS** |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/15/Text/49` | 0.589766 | **SKILLS** **FEATS** |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/11/Text/46` | 0.589766 | **SKILLS** **FEATS** |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/27` | 0.576902 | **NATURAL AMBITION** **FEAT 1** |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/17/Text/2` | 0.510686 | **NATURAL GRACE **[free-action] **FEAT 1** |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/17/Text/52` | 0.462670 | **Prerequisites** Natural Grace |

### Query 148
- Text: What are the requirements for **UNCONVENTIONAL WEAPONRY** **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/35']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/35', 'PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/22', 'PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/31']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/35` | 0.852300 | **UNCONVENTIONAL WEAPONRY** **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/22` | 0.504004 | **GENERAL TRAINING** **FEAT 1** |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/31` | 0.482276 | **NATURAL SKILL** **FEAT 1** |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/17/SectionHeader/30` | 0.408033 | **UNCANNY AWARENESS** **FEAT 9** |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/1/Text/34` | 0.402856 | As a starting character, you can choose from only 1stlevel ancestry feats, but later choices can be made from any  feat of your level or lower. These feats also sometimes list  prerequisites, which ar |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/13/Text/2` | 0.401716 | If you're trained in all martial weapons, you can instead  choose an uncommon advanced weapon that has an ancestry's  trait or is common in another culture. You gain access to that  weapon and have fa |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/16/SectionHeader/23` | 0.397750 | **KASATHAN WEAPON FAMILIARITY** **FEAT 1** |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/12/Text/25` | 0.392003 | Your adaptability manifests in your mastery of a range of  useful abilities. You gain a 1st-level general feat. You must  meet the feat's prerequisites, but if you select this feat during  character c |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/13/Text/1` | 0.387000 | ysoki) or that's common in another culture. You gain access  to that weapon, and for the purpose of proficiency, you treat  it as a simple weapon. |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/12/Text/38` | 0.378123 | You've familiarized yourself with a particular weapon,  potentially from another ancestry or culture. Choose  an uncommon simple or martial weapon with a trait  corresponding to an ancestry (such as k |

### Query 149
- Text: What are the requirements for **ADAPTIVE ADEPT** **FEAT 5**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 040-057::/page/13/SectionHeader/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 040-057::/page/13/SectionHeader/4', 'PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/6', 'PZO22001 Starfinder Player Core 040-057::/page/8/SectionHeader/16']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 040-057::/page/13/SectionHeader/4` | 0.925225 | **ADAPTIVE ADEPT** **FEAT 5** |
| 2 | `PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/6` | 0.591715 | **ADAPTED AUGMENTATIONS** **FEAT 1** |
| 3 | `PZO22001 Starfinder Player Core 040-057::/page/8/SectionHeader/16` | 0.577756 | **DARKVISION ADAPTATION** **FEAT 1** |
| 4 | `PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/12` | 0.530214 | **ADAPTED CANTRIP** **FEAT 1** |
| 5 | `PZO22001 Starfinder Player Core 040-057::/page/5/SectionHeader/2` | 0.511039 | **ADVANCED TARGETING SYSTEM** **FEAT 5** |
| 6 | `PZO22001 Starfinder Player Core 040-057::/page/13/SectionHeader/8` | 0.484865 | **CLEVER IMPROVISER** **FEAT 5** |
| 7 | `PZO22001 Starfinder Player Core 040-057::/page/12/Text/25` | 0.479546 | Your adaptability manifests in your mastery of a range of  useful abilities. You gain a 1st-level general feat. You must  meet the feat's prerequisites, but if you select this feat during  character c |
| 8 | `PZO22001 Starfinder Player Core 040-057::/page/4/SectionHeader/30` | 0.478077 | **NIGHTVISION ADAPTATION** **FEAT 1** |
| 9 | `PZO22001 Starfinder Player Core 040-057::/page/8/SectionHeader/6` | 0.460459 | **ADAPTABLE LIMBS** **FEAT 1** |
| 10 | `PZO22001 Starfinder Player Core 040-057::/page/13/Text/36` | 0.455310 | Over the course of adventuring, your adaptability has let you  pick up numerous useful abilities. You gain a general feat of  7th level or lower. You must meet the feat's prerequisites. |
