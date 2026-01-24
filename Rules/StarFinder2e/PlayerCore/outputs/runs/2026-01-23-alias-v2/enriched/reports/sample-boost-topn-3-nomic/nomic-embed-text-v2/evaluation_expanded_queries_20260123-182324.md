# RulesLawyer Evaluation Report: nomic-embed-text-v2

## Summary
- Run ID: `None`
- Ruleset ID: `None`
- Document ID: `None`
- Chunk source: `enriched`
- Chunk count: `1390`
- Query count: `150`
- Evaluated queries: `150`
- Coverage: `1.0000`
- MRR: `0.8115`
- hit@1: `0.7333`
- hit@3: `0.8667`
- hit@5: `0.8933`
- hit@10: `0.9400`
- Embeddings reused: `False`
- Graph boost: `0.05` (depth=2, top_k=50, source=top, seed_top_n=3, same_kind_only=False, decay=0.4)

### Expanded Gold Metrics
- Coverage: `1.0000`
- MRR: `0.8331`
- hit@1: `0.7600`
- hit@3: `0.8867`
- hit@5: `0.9133`
- hit@10: `0.9533`

### Expanded Gold Expansion Stats
- Queries with additions: `150`
- Avg added per query: `2.41`
- Max added: `11`
- Addition reasons:
  - graph_depth_1: `362`

### Expanded Gold Delta (Expanded - Strict)
- Coverage Δ: `0.0000`
- MRR Δ: `0.0217`
- hit@1 Δ: `0.0267`
- hit@3 Δ: `0.0200`
- hit@5 Δ: `0.0200`
- hit@10 Δ: `0.0133`

## Timings (ms)
- Embedding: `25494`
- Evaluation: `310`

## Query Details
### Query 0
- Text: What is the rule about CHAPTER 7: SPELLS?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0', 'PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/1', 'PZO22001 Starfinder Player Core 294-329::/page/7/SectionHeader/3']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/1']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/1` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0` | 0.907264 | CHAPTER 7: SPELLS |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/1` | 0.749153 | SPELLS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/7/SectionHeader/3` | 0.730902 | IDENTIFYING SPELLS |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/86` | 0.665201 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/80` | 0.665201 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/59` | 0.665201 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/61` | 0.665201 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/74` | 0.665201 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/26` | 0.665201 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/24` | 0.665201 | **SPELLS** |

### Query 1
- Text: What is the rule about Whether it comes in the form of eldritch artifacts, otherworldly beings, or witchwarpers altering  reality with strange spells, magic brings fantasy and wonder to Starfinder. This chapter explains how  spells work and how spellcasters prepare and cast their spells.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/1', 'PZO22001 Starfinder Player Core 294-329::/page/19/Text/2', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/3']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/1', 'PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/3']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/3` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/1` | 0.998123 | Whether it comes in the form of eldritch artifacts, otherworldly beings, or witchwarpers altering  reality with strange spells, magic brings fantasy and wonder to Starfinder. This chapter explains how |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/2` | 0.681171 | The grand variety of spells includes those in the following pages and far more. Taught at magical  academies, drawn from other worlds, bestowed by mystical connections, and granted by all manner of  u |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/3` | 0.681091 | Even with the widespread presence of technology,  spellcasters can be found in every corner of the galaxy.  Some spellcasters draw magic from other realities, some  from their mystical connections to |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/4` | 0.630860 | With special gestures and utterances, a spellcaster can  call forth mystic energies, warp the mind, protect themself  against danger, or even create something from nothing.  Each class has its own met |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/4` | 0.594492 | Spellcasting creates obvious sensory manifestations, such  as bright lights, crackling sounds, and sharp smells from the  gathering magic. Nearly all spells manifest a spell signature—a  colorful, glo |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/7` | 0.594456 | Arcane spellcasters use logic and  rationality to categorize the magic inherent  in the world around them. Because of its far-reaching  approach, the arcane tradition has the broadest spell  list, tho |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/8` | 0.577893 | If you're a prepared spellcaster—such as a technomancer  (see *Starfinder Tech Core*)—you must spend time each day  preparing spells for that day. At the start of your daily  preparations, you select |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/3` | 0.575253 | Your class determines which tradition of magic your spells use. In some cases, such as when a mystic gains spells from  their connection or when a witchwarper learns spells from their paradox, you mig |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/12` | 0.561706 | After Triune's Signal connected cultures across the  Universe, the peoples of the galaxy have learned more  than ever before about the Universe's composition  thanks to science and technology. As tech |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/26` | 0.560128 | Certain spells are natural to your character, typically coming  from your ancestry or a magic item. They're called innate  spells. Innate spells don't let you qualify for abilities that  require you t |

### Query 2
- Text: What is the rule about Even with the widespread presence of technology,  spellcasters can be found in every corner of the galaxy.  Some spellcasters draw magic from other realities, some  from their mystical connections to cosmic forces, and  others rewrite the underlying code of the universe to cast  their spells.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/3']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/3', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/12', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/7']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/3', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/4', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/1']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/4` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/1` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/3` | 0.970359 | Even with the widespread presence of technology,  spellcasters can be found in every corner of the galaxy.  Some spellcasters draw magic from other realities, some  from their mystical connections to |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/12` | 0.685328 | After Triune's Signal connected cultures across the  Universe, the peoples of the galaxy have learned more  than ever before about the Universe's composition  thanks to science and technology. As tech |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/7` | 0.675839 | Arcane spellcasters use logic and  rationality to categorize the magic inherent  in the world around them. Because of its far-reaching  approach, the arcane tradition has the broadest spell  list, tho |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/1` | 0.639719 | Whether it comes in the form of eldritch artifacts, otherworldly beings, or witchwarpers altering  reality with strange spells, magic brings fantasy and wonder to Starfinder. This chapter explains how |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/4` | 0.637604 | With special gestures and utterances, a spellcaster can  call forth mystic energies, warp the mind, protect themself  against danger, or even create something from nothing.  Each class has its own met |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/2` | 0.620290 | The grand variety of spells includes those in the following pages and far more. Taught at magical  academies, drawn from other worlds, bestowed by mystical connections, and granted by all manner of  u |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/11` | 0.609529 | beyond the Universe. Mystics connected with the cosmic  forces of healing and shadows are divine spellcasters. |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/15` | 0.571518 | systematic way. Witchwarpers touched by the Gap or  alternate timelines, as well as mystics who are psychically  linked to the Akashic Record, are occult spellcasters. |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/2` | 0.570282 | Spellcasters cast spells from one of four different spell lists, each representing a different magical tradition: arcane,  divine, occult, and primal. |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/4` | 0.538057 | Spellcasting creates obvious sensory manifestations, such  as bright lights, crackling sounds, and sharp smells from the  gathering magic. Nearly all spells manifest a spell signature—a  colorful, glo |

### Query 3
- Text: What is the rule about With special gestures and utterances, a spellcaster can  call forth mystic energies, warp the mind, protect themself  against danger, or even create something from nothing.  Each class has its own method of learning, preparing,  and casting spells, and every individual spell produces a  specific effect, so learning new spells gives a spellcaster  an increasing array of options to accomplish their goals.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/4', 'PZO22001 Starfinder Player Core 294-329::/page/4/Text/4', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/1']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/4', 'PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/5', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/3']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/5` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/3` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/4` | 0.965482 | With special gestures and utterances, a spellcaster can  call forth mystic energies, warp the mind, protect themself  against danger, or even create something from nothing.  Each class has its own met |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/4` | 0.650699 | Spellcasting creates obvious sensory manifestations, such  as bright lights, crackling sounds, and sharp smells from the  gathering magic. Nearly all spells manifest a spell signature—a  colorful, glo |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/1` | 0.642817 | Whether it comes in the form of eldritch artifacts, otherworldly beings, or witchwarpers altering  reality with strange spells, magic brings fantasy and wonder to Starfinder. This chapter explains how |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/3` | 0.600950 | Even with the widespread presence of technology,  spellcasters can be found in every corner of the galaxy.  Some spellcasters draw magic from other realities, some  from their mystical connections to |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/2` | 0.598326 | The grand variety of spells includes those in the following pages and far more. Taught at magical  academies, drawn from other worlds, bestowed by mystical connections, and granted by all manner of  u |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/7` | 0.593198 | Arcane spellcasters use logic and  rationality to categorize the magic inherent  in the world around them. Because of its far-reaching  approach, the arcane tradition has the broadest spell  list, tho |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/3` | 0.592539 | Your class determines which tradition of magic your spells use. In some cases, such as when a mystic gains spells from  their connection or when a witchwarper learns spells from their paradox, you mig |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/8` | 0.571583 | If you're a prepared spellcaster—such as a technomancer  (see *Starfinder Tech Core*)—you must spend time each day  preparing spells for that day. At the start of your daily  preparations, you select |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/22` | 0.570492 | If you are a spellcaster, your focus spells are the same tradition  of spell as the class that gave you the focus spell. A mystic's |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/16` | 0.566723 | Both prepared and spontaneous spellcasters can cast a spell  at a higher spell rank than that listed for the spell. This is  called heightening the spell. A prepared spellcaster can  heighten a spell |

### Query 4
- Text: What is the rule about SPELL SLOTS?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/5', 'PZO22001 Starfinder Player Core 294-329::/page/7/SectionHeader/3', 'PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/5', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/6', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/4']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/6` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/4` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/5` | 0.891913 | SPELL SLOTS |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/7/SectionHeader/3` | 0.666848 | IDENTIFYING SPELLS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0` | 0.664156 | CHAPTER 7: SPELLS |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/1` | 0.618555 | SPELLS |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/8/SectionHeader/1` | 0.597848 | SPELL LISTS |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/59` | 0.586621 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/83` | 0.586621 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/86` | 0.586621 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/80` | 0.586621 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/26` | 0.586621 | **SPELLS** |

### Query 5
- Text: What is the rule about Characters of spellcasting classes can cast a number of spells  each day; the spells you can cast in a day are referred to as  spell slots. At 1st level, a character has only a small number  of 1st-rank spell slots per day, but as you advance in level, you  gain more spell slots of higher rank. A spell's rank indicates  its overall power, from 1 to 10.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/6', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/8', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/10']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/6', 'PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/5', 'PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/7']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/5` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/7` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/6` | 0.985210 | Characters of spellcasting classes can cast a number of spells  each day; the spells you can cast in a day are referred to as  spell slots. At 1st level, a character has only a small number  of 1st-ra |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/8` | 0.702971 | If you're a prepared spellcaster—such as a technomancer  (see *Starfinder Tech Core*)—you must spend time each day  preparing spells for that day. At the start of your daily  preparations, you select |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/10` | 0.679402 | The title of a cantrip's stat block says "Cantrip" instead of  "Spell", and the spell has the cantrip trait. Casting a cantrip  doesn't use up your spell slots; you can cast a cantrip at will,  any nu |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/9` | 0.637965 | Each prepared spell is expended after a single casting,  so if you want to cast a particular spell more than once in  a day, you need to prepare that spell multiple times. The  exception to this rule |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/5` | 0.629564 | Spells can vary in how many actions they take, as shown in  the spell's stat block. You cast cantrips, spells from spell slots,  and focus spells using the same process, but must expend the  spell whe |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/1` | 0.628149 | You can't use your spell slots to cast your innate spells, but  you might have an innate spell and also be able to prepare  or cast the same spell through your class. You also can't  heighten innate s |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/14` | 0.616997 | If you're a spontaneous spellcaster—such as a mystic—you  choose which spell from your spell repertoire that you're  using a spell slot for at the moment you decide to cast it. This  provides you with |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/11` | 0.608987 | A cantrip is always automatically heightened to half your  level, rounded up. For a typical spellcaster, this means its  rank is equal to the highest rank of spell slot you have. |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/16` | 0.605762 | Both prepared and spontaneous spellcasters can cast a spell  at a higher spell rank than that listed for the spell. This is  called heightening the spell. A prepared spellcaster can  heighten a spell |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/4` | 0.601446 | Sometimes you need to identify a spell, especially if its  effects aren't obvious right away. If you notice a spell  being cast, and you have that spell in your repertoire  or prepared it that day (ev |

### Query 6
- Text: What is the rule about PREPARED SPELLS?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/7', 'PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/1', 'PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/7', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/6', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/8']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/6` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/8` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/7` | 0.888103 | PREPARED SPELLS |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/1` | 0.707713 | SPELLS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0` | 0.694237 | CHAPTER 7: SPELLS |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/7/SectionHeader/3` | 0.626360 | IDENTIFYING SPELLS |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/15` | 0.608860 | HEIGHTENED SPELLS |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/13` | 0.600763 | SUSTAINING SPELLS |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/61` | 0.598921 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/86` | 0.598921 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/74` | 0.598921 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/24` | 0.598921 | **SPELLS** |

### Query 7
- Text: What is the rule about If you're a prepared spellcaster—such as a technomancer  (see *Starfinder Tech Core*)—you must spend time each day  preparing spells for that day. At the start of your daily  preparations, you select a number of spells of different  spell ranks, determined by your character level and class.  Your spells remain prepared until you cast them or until you  prepare spells again.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/8']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/8', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/9', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/10']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/8', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/9', 'PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/7']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/9` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/7` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/8` | 0.984632 | If you're a prepared spellcaster—such as a technomancer  (see *Starfinder Tech Core*)—you must spend time each day  preparing spells for that day. At the start of your daily  preparations, you select |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/9` | 0.732903 | Each prepared spell is expended after a single casting,  so if you want to cast a particular spell more than once in  a day, you need to prepare that spell multiple times. The  exception to this rule |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/10` | 0.718825 | You might gain an ability that allows you to swap  prepared spells or perform other aspects of preparing spells  at different times throughout the day, but only your daily  preparation counts for the |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/6` | 0.655712 | Characters of spellcasting classes can cast a number of spells  each day; the spells you can cast in a day are referred to as  spell slots. At 1st level, a character has only a small number  of 1st-ra |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/14` | 0.634996 | If you're a spontaneous spellcaster—such as a mystic—you  choose which spell from your spell repertoire that you're  using a spell slot for at the moment you decide to cast it. This  provides you with |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/6/Text/16` | 0.621399 | If a spell's duration says it lasts until your next daily  preparations, on the next day you can refrain from preparing  a new spell in that spell's slot. (If you are a spontaneous caster,  you can in |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/4` | 0.574996 | Sometimes you need to identify a spell, especially if its  effects aren't obvious right away. If you notice a spell  being cast, and you have that spell in your repertoire  or prepared it that day (ev |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/5` | 0.569602 | If you're a spontaneous spellcaster, you must know a spell at  the specific rank that you want to cast it in order to heighten  it. You can add a spell to your spell repertoire at more than  a single |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/10` | 0.558082 | The title of a cantrip's stat block says "Cantrip" instead of  "Spell", and the spell has the cantrip trait. Casting a cantrip  doesn't use up your spell slots; you can cast a cantrip at will,  any nu |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/5` | 0.554777 | Spells can vary in how many actions they take, as shown in  the spell's stat block. You cast cantrips, spells from spell slots,  and focus spells using the same process, but must expend the  spell whe |

### Query 8
- Text: What is the rule about Each prepared spell is expended after a single casting,  so if you want to cast a particular spell more than once in  a day, you need to prepare that spell multiple times. The  exception to this rule is for spells with the cantrip trait; once  you prepare a cantrip, you can cast it as many times as you  want until the next time you prepare spells. See page 296  for more information on cantrips.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/9', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/10', 'PZO22001 Starfinder Player Core 294-329::/page/4/Text/5']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/9', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/10', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/8']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/10` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/8` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/9` | 1.020796 | Each prepared spell is expended after a single casting,  so if you want to cast a particular spell more than once in  a day, you need to prepare that spell multiple times. The  exception to this rule |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/10` | 0.806210 | The title of a cantrip's stat block says "Cantrip" instead of  "Spell", and the spell has the cantrip trait. Casting a cantrip  doesn't use up your spell slots; you can cast a cantrip at will,  any nu |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/5` | 0.714085 | Spells can vary in how many actions they take, as shown in  the spell's stat block. You cast cantrips, spells from spell slots,  and focus spells using the same process, but must expend the  spell whe |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/10` | 0.682016 | You might gain an ability that allows you to swap  prepared spells or perform other aspects of preparing spells  at different times throughout the day, but only your daily  preparation counts for the |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/8` | 0.654407 | If you're a prepared spellcaster—such as a technomancer  (see *Starfinder Tech Core*)—you must spend time each day  preparing spells for that day. At the start of your daily  preparations, you select |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/6/Text/16` | 0.644937 | If a spell's duration says it lasts until your next daily  preparations, on the next day you can refrain from preparing  a new spell in that spell's slot. (If you are a spontaneous caster,  you can in |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/26` | 0.600851 | Certain spells are natural to your character, typically coming  from your ancestry or a magic item. They're called innate  spells. Innate spells don't let you qualify for abilities that  require you t |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/11` | 0.590176 | A cantrip is always automatically heightened to half your  level, rounded up. For a typical spellcaster, this means its  rank is equal to the highest rank of spell slot you have. |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/6` | 0.582623 | Characters of spellcasting classes can cast a number of spells  each day; the spells you can cast in a day are referred to as  spell slots. At 1st level, a character has only a small number  of 1st-ra |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/9` | 0.563667 | A cantrip is a special type of spell that's weaker than other  spells but can be used with greater freedom and flexibility. |

### Query 9
- Text: What is the rule about You might gain an ability that allows you to swap  prepared spells or perform other aspects of preparing spells  at different times throughout the day, but only your daily  preparation counts for the purpose of effects that last until  the next time you prepare spells.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/10', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/9', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/8']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/10', 'PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/11', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/9']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/11` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/9` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/10` | 0.984815 | You might gain an ability that allows you to swap  prepared spells or perform other aspects of preparing spells  at different times throughout the day, but only your daily  preparation counts for the |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/9` | 0.736775 | Each prepared spell is expended after a single casting,  so if you want to cast a particular spell more than once in  a day, you need to prepare that spell multiple times. The  exception to this rule |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/8` | 0.690775 | If you're a prepared spellcaster—such as a technomancer  (see *Starfinder Tech Core*)—you must spend time each day  preparing spells for that day. At the start of your daily  preparations, you select |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/6/Text/16` | 0.611214 | If a spell's duration says it lasts until your next daily  preparations, on the next day you can refrain from preparing  a new spell in that spell's slot. (If you are a spontaneous caster,  you can in |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/10` | 0.564077 | The title of a cantrip's stat block says "Cantrip" instead of  "Spell", and the spell has the cantrip trait. Casting a cantrip  doesn't use up your spell slots; you can cast a cantrip at will,  any nu |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/14` | 0.562375 | If you're a spontaneous spellcaster—such as a mystic—you  choose which spell from your spell repertoire that you're  using a spell slot for at the moment you decide to cast it. This  provides you with |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/5` | 0.560000 | Spells can vary in how many actions they take, as shown in  the spell's stat block. You cast cantrips, spells from spell slots,  and focus spells using the same process, but must expend the  spell whe |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/6` | 0.551213 | Characters of spellcasting classes can cast a number of spells  each day; the spells you can cast in a day are referred to as  spell slots. At 1st level, a character has only a small number  of 1st-ra |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/1` | 0.547321 | You can't use your spell slots to cast your innate spells, but  you might have an innate spell and also be able to prepare  or cast the same spell through your class. You also can't  heighten innate s |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/4` | 0.537365 | Sometimes you need to identify a spell, especially if its  effects aren't obvious right away. If you notice a spell  being cast, and you have that spell in your repertoire  or prepared it that day (ev |

### Query 10
- Text: What is the rule about **SPELLCASTING IN STARFINDER**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/11', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/8', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/1']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/11', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/10', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/12']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/10` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/12` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/11` | 0.938624 | **SPELLCASTING IN STARFINDER** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/8` | 0.497729 | If you're a prepared spellcaster—such as a technomancer  (see *Starfinder Tech Core*)—you must spend time each day  preparing spells for that day. At the start of your daily  preparations, you select |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/1` | 0.471585 | Whether it comes in the form of eldritch artifacts, otherworldly beings, or witchwarpers altering  reality with strange spells, magic brings fantasy and wonder to Starfinder. This chapter explains how |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/19` | 0.412766 | **SPELL NAME **[one-action] **SPELL (RANK)** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/16` | 0.412620 | Both prepared and spontaneous spellcasters can cast a spell  at a higher spell rank than that listed for the spell. This is  called heightening the spell. A prepared spellcaster can  heighten a spell |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/6` | 0.399305 | Characters of spellcasting classes can cast a number of spells  each day; the spells you can cast in a day are referred to as  spell slots. At 1st level, a character has only a small number  of 1st-ra |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/5` | 0.394482 | If you're a spontaneous spellcaster, you must know a spell at  the specific rank that you want to cast it in order to heighten  it. You can add a spell to your spell repertoire at more than  a single |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/10` | 0.388500 | Some spells take minutes or hours to cast. You can't use  other actions or reactions while casting such a spell, |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/5` | 0.385748 | Spells can vary in how many actions they take, as shown in  the spell's stat block. You cast cantrips, spells from spell slots,  and focus spells using the same process, but must expend the  spell whe |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/2` | 0.382631 | CASTING SPELLS |

### Query 11
- Text: What is the rule about After Triune's Signal connected cultures across the  Universe, the peoples of the galaxy have learned more  than ever before about the Universe's composition  thanks to science and technology. As technology  improves and creates mass-market marvels rivaling  what was once only possible for a powerful spellcaster,  magic is more static, with arcane universities,  occult societies, and religious orders preserving  ancient techniques and tomes into the modern  era. Many specialty tech items incorporate hybrid  magitechnology, and most spellcasters carry a backup  gun or other tech gear on them for when they run  out of spells. Magic and technology coexist, but most  spellcasters use analog spellcasting, and blending the  two together to create a hybrid item requires training.  Only a few spellcasters mix magic with technology they're seen as mavericks by most established magical  institutions. Technomancers and spellcasters who  have learned to command machines or connect with  computers using magic blaze a trail few have explored.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/12']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/12', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/3', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/7']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/12', 'PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/11', 'PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/13']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/11` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/13` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/12` | 1.010676 | After Triune's Signal connected cultures across the  Universe, the peoples of the galaxy have learned more  than ever before about the Universe's composition  thanks to science and technology. As tech |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/3` | 0.676642 | Even with the widespread presence of technology,  spellcasters can be found in every corner of the galaxy.  Some spellcasters draw magic from other realities, some  from their mystical connections to |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/7` | 0.606622 | Arcane spellcasters use logic and  rationality to categorize the magic inherent  in the world around them. Because of its far-reaching  approach, the arcane tradition has the broadest spell  list, tho |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/4` | 0.571962 | With special gestures and utterances, a spellcaster can  call forth mystic energies, warp the mind, protect themself  against danger, or even create something from nothing.  Each class has its own met |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/1` | 0.554140 | Whether it comes in the form of eldritch artifacts, otherworldly beings, or witchwarpers altering  reality with strange spells, magic brings fantasy and wonder to Starfinder. This chapter explains how |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/3` | 0.516582 | Your class determines which tradition of magic your spells use. In some cases, such as when a mystic gains spells from  their connection or when a witchwarper learns spells from their paradox, you mig |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/4` | 0.503036 | Spellcasting creates obvious sensory manifestations, such  as bright lights, crackling sounds, and sharp smells from the  gathering magic. Nearly all spells manifest a spell signature—a  colorful, glo |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/29` | 0.501736 | **CONTROL MACHINE **[two-actions] **SPELL 5**  **UNCOMMON** **CONCENTRATE** **INCAPACITATION** **MANIPULATE**  **Traditions** arcane, occult  **Range **30 feet;** Targets** 1 creature or hazard with t |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/2` | 0.500434 | The grand variety of spells includes those in the following pages and far more. Taught at magical  academies, drawn from other worlds, bestowed by mystical connections, and granted by all manner of  u |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/15` | 0.499073 | systematic way. Witchwarpers touched by the Gap or  alternate timelines, as well as mystics who are psychically  linked to the Akashic Record, are occult spellcasters. |

### Query 12
- Text: What is the rule about SPONTANEOUS SPELLS?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/13', 'PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0', 'PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/1']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/13', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/14', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/12']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/14` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/12` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/13` | 0.894232 | SPONTANEOUS SPELLS |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0` | 0.674220 | CHAPTER 7: SPELLS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/1` | 0.671473 | SPELLS |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/7/SectionHeader/3` | 0.625160 | IDENTIFYING SPELLS |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/1` | 0.609799 | **SUBTLE SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/86` | 0.570030 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/59` | 0.570030 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/86` | 0.570030 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/83` | 0.570030 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/80` | 0.570030 | **SPELLS** |

### Query 13
- Text: What is the rule about If you're a spontaneous spellcaster—such as a mystic—you  choose which spell from your spell repertoire that you're  using a spell slot for at the moment you decide to cast it. This  provides you with more freedom in your spellcasting, but you  have fewer spells in your spell repertoire, as determined by  your character level and class. When you make your daily  preparations, all your spell slots are refreshed, but you don't  get to change the spells in your repertoire.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/14']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/14', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/7', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/3']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/14', 'PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/15', 'PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/13']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/15` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/13` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/14` | 0.991800 | If you're a spontaneous spellcaster—such as a mystic—you  choose which spell from your spell repertoire that you're  using a spell slot for at the moment you decide to cast it. This  provides you with |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/7` | 0.702411 | As a spontaneous caster, you can also choose to cast  a lower-rank spell using a higher-rank spell slot without  heightening it or knowing it at a higher rank. This casts the  spell at the rank you kn |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/3` | 0.692759 | Your class determines which tradition of magic your spells use. In some cases, such as when a mystic gains spells from  their connection or when a witchwarper learns spells from their paradox, you mig |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/5` | 0.639582 | If you're a spontaneous spellcaster, you must know a spell at  the specific rank that you want to cast it in order to heighten  it. You can add a spell to your spell repertoire at more than  a single |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/8` | 0.619784 | If you're a prepared spellcaster—such as a technomancer  (see *Starfinder Tech Core*)—you must spend time each day  preparing spells for that day. At the start of your daily  preparations, you select |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/6/Text/16` | 0.616352 | If a spell's duration says it lasts until your next daily  preparations, on the next day you can refrain from preparing  a new spell in that spell's slot. (If you are a spontaneous caster,  you can in |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/1` | 0.604048 | You can't use your spell slots to cast your innate spells, but  you might have an innate spell and also be able to prepare  or cast the same spell through your class. You also can't  heighten innate s |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/6` | 0.599138 | Characters of spellcasting classes can cast a number of spells  each day; the spells you can cast in a day are referred to as  spell slots. At 1st level, a character has only a small number  of 1st-ra |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/9` | 0.598762 | Each prepared spell is expended after a single casting,  so if you want to cast a particular spell more than once in  a day, you need to prepare that spell multiple times. The  exception to this rule |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/10` | 0.587727 | The title of a cantrip's stat block says "Cantrip" instead of  "Spell", and the spell has the cantrip trait. Casting a cantrip  doesn't use up your spell slots; you can cast a cantrip at will,  any nu |

### Query 14
- Text: What is the rule about HEIGHTENED SPELLS?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/15']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/15', 'PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0', 'PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/1']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/15', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/14', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/16']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/14` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/16` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/15` | 0.890131 | HEIGHTENED SPELLS |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0` | 0.634623 | CHAPTER 7: SPELLS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/1` | 0.632736 | SPELLS |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/7/SectionHeader/3` | 0.578821 | IDENTIFYING SPELLS |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/7` | 0.575687 | PREPARED SPELLS |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/13` | 0.535059 | SUSTAINING SPELLS |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/13` | 0.527279 | SPONTANEOUS SPELLS |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/80` | 0.526299 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/60` | 0.526299 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/27/Text/68` | 0.526299 | **SPELLS** |

### Query 15
- Text: What is the rule about Both prepared and spontaneous spellcasters can cast a spell  at a higher spell rank than that listed for the spell. This is  called heightening the spell. A prepared spellcaster can  heighten a spell by preparing it in a higher-rank slot than  its normal spell rank, while a spontaneous spellcaster can  heighten a spell by casting it using a higher-rank spell slot,?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/16']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/16', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/1', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/7']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/16', 'PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/15', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/18']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/15` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/18` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/16` | 1.003339 | Both prepared and spontaneous spellcasters can cast a spell  at a higher spell rank than that listed for the spell. This is  called heightening the spell. A prepared spellcaster can  heighten a spell |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/1` | 0.828360 | so long as they know the spell at that rank (see Heightened  Spontaneous Spells below). When you heighten your spell,  the spell's rank increases to match the higher rank of the  spell slot you've pre |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/7` | 0.749708 | As a spontaneous caster, you can also choose to cast  a lower-rank spell using a higher-rank spell slot without  heightening it or knowing it at a higher rank. This casts the  spell at the rank you kn |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/5` | 0.678898 | If you're a spontaneous spellcaster, you must know a spell at  the specific rank that you want to cast it in order to heighten  it. You can add a spell to your spell repertoire at more than  a single |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/2` | 0.670108 | In addition, many spells have additional specific benefits  when they are heightened, such as increased damage. These  extra benefits are described at the end of the spell's stat  block. Some heighten |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/6` | 0.648744 | Many spontaneous spellcasting classes provide abilities  like the signature spells class feature, which allows you to  cast a limited number of spells as heightened versions even if  you know the spel |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/1` | 0.648206 | You can't use your spell slots to cast your innate spells, but  you might have an innate spell and also be able to prepare  or cast the same spell through your class. You also can't  heighten innate s |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/3` | 0.646939 | Other heightened entries give a number after a plus sign,  indicating that heightening grants extra advantages over  multiple ranks. The listed effect applies for every increment  of ranks by which th |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/11` | 0.619888 | A cantrip is always automatically heightened to half your  level, rounded up. For a typical spellcaster, this means its  rank is equal to the highest rank of spell slot you have. |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/4` | 0.614974 | Sometimes you need to identify a spell, especially if its  effects aren't obvious right away. If you notice a spell  being cast, and you have that spell in your repertoire  or prepared it that day (ev |

### Query 16
- Text: Summarize **INTRODUCTION**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/18']
- Expected found: `True`
- Expected rank: `6`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/30', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/20', 'PZO22001 Starfinder Player Core 294-329::/page/7/Text/28']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/18', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/19', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/16']
- Expanded expected found: `True`
- Expanded expected rank: `6`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/19` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/16` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/30` | 0.880541 | **INTRODUCTION** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/20` | 0.880541 | **INTRODUCTION** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/28` | 0.880541 | **INTRODUCTION** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/68` | 0.838541 | **INTRODUCTION** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/77` | 0.838541 | **INTRODUCTION** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/18` | 0.838541 | **INTRODUCTION** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/55` | 0.838541 | **INTRODUCTION** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/74` | 0.838541 | **INTRODUCTION** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/80` | 0.838541 | **INTRODUCTION** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/23/Text/38` | 0.838541 | **INTRODUCTION** |

### Query 17
- Text: What is the rule about **ANCESTRIES & ** **BACKGROUNDS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/19']
- Expected found: `True`
- Expected rank: `15`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/31', 'PZO22001 Starfinder Player Core 294-329::/page/23/Text/39', 'PZO22001 Starfinder Player Core 294-329::/page/35/Text/63']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/19', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/20', 'PZO22001 Starfinder Player Core 294-329::/page/17/Text/81', 'PZO22001 Starfinder Player Core 294-329::/page/29/Text/60', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/31', 'PZO22001 Starfinder Player Core 294-329::/page/31/Text/55', 'PZO22001 Starfinder Player Core 294-329::/page/11/Text/78', 'PZO22001 Starfinder Player Core 294-329::/page/33/Text/56', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/18', 'PZO22001 Starfinder Player Core 294-329::/page/13/Text/69', 'PZO22001 Starfinder Player Core 294-329::/page/23/Text/39', 'PZO22001 Starfinder Player Core 294-329::/page/35/Text/63']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/20` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/17/Text/81` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/29/Text/60` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/31` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/31/Text/55` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/11/Text/78` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/33/Text/56` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/18` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/13/Text/69` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/23/Text/39` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/35/Text/63` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/31` | 0.920820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/23/Text/39` | 0.920820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/63` | 0.920820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/81` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/78` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/56` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/29` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/21` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/69` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/54` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |

### Query 18
- Text: Summarize **CLASSES**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/20']
- Expected found: `True`
- Expected rank: `14`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/35/Text/64', 'PZO22001 Starfinder Player Core 294-329::/page/27/Text/64', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/32']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/20', 'PZO22001 Starfinder Player Core 294-329::/page/15/Text/76', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/21', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/32', 'PZO22001 Starfinder Player Core 294-329::/page/19/Text/55', 'PZO22001 Starfinder Player Core 294-329::/page/33/Text/57', 'PZO22001 Starfinder Player Core 294-329::/page/23/Text/40', 'PZO22001 Starfinder Player Core 294-329::/page/13/Text/70', 'PZO22001 Starfinder Player Core 294-329::/page/17/Text/82', 'PZO22001 Starfinder Player Core 294-329::/page/29/Text/61', 'PZO22001 Starfinder Player Core 294-329::/page/11/Text/79', 'PZO22001 Starfinder Player Core 294-329::/page/27/Text/64']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/15/Text/76` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/21` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/32` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/19/Text/55` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/33/Text/57` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/23/Text/40` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/13/Text/70` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/17/Text/82` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/29/Text/61` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/11/Text/79` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/27/Text/64` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/64` | 0.940061 | **CLASSES** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/27/Text/64` | 0.940061 | **CLASSES** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/32` | 0.940061 | **CLASSES** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/82` | 0.910061 | **CLASSES** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/57` | 0.910061 | **CLASSES** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/70` | 0.910061 | **CLASSES** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/76` | 0.910061 | **CLASSES** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/30` | 0.910061 | **CLASSES** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/22` | 0.910061 | **CLASSES** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/23/Text/40` | 0.910061 | **CLASSES** |

### Query 19
- Text: What is the rule about **SKILLS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/21']
- Expected found: `True`
- Expected rank: `5`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/35/Text/65', 'PZO22001 Starfinder Player Core 294-329::/page/17/Text/83', 'PZO22001 Starfinder Player Core 294-329::/page/33/Text/58']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/21', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/20', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/22']
- Expanded expected found: `True`
- Expanded expected rank: `5`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/20` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/22` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/65` | 0.864442 | **SKILLS** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/83` | 0.864442 | **SKILLS** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/58` | 0.864442 | **SKILLS** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/27/Text/65` | 0.822442 | **SKILLS** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/21` | 0.822442 | **SKILLS** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/83` | 0.822442 | **SKILLS** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/80` | 0.822442 | **SKILLS** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/71` | 0.822442 | **SKILLS** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/57` | 0.822442 | **SKILLS** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/62` | 0.822442 | **SKILLS** |

### Query 20
- Text: What is the rule about **FEATS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/22']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/22', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/34', 'PZO22001 Starfinder Player Core 294-329::/page/33/Text/59']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/22', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/23', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/21']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/23` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/21` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/22` | 0.871817 | **FEATS** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/34` | 0.871817 | **FEATS** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/59` | 0.871817 | **FEATS** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/84` | 0.829817 | **FEATS** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/81` | 0.829817 | **FEATS** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/78` | 0.829817 | **FEATS** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/84` | 0.829817 | **FEATS** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/24` | 0.829817 | **FEATS** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/32` | 0.829817 | **FEATS** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/72` | 0.829817 | **FEATS** |

### Query 21
- Text: Summarize **EQUIPMENT**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/23']
- Expected found: `True`
- Expected rank: `6`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/35', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/25', 'PZO22001 Starfinder Player Core 294-329::/page/9/Text/85']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/23', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/22', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/24']
- Expanded expected found: `True`
- Expanded expected rank: `6`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/22` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/24` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/35` | 0.944726 | **EQUIPMENT** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/25` | 0.944726 | **EQUIPMENT** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/85` | 0.944726 | **EQUIPMENT** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/60` | 0.902726 | **EQUIPMENT** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/82` | 0.902726 | **EQUIPMENT** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/23` | 0.902726 | **EQUIPMENT** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/59` | 0.902726 | **EQUIPMENT** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/85` | 0.902726 | **EQUIPMENT** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/58` | 0.902726 | **EQUIPMENT** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/79` | 0.902726 | **EQUIPMENT** |

### Query 22
- Text: What is the rule about **SPELLS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/24']
- Expected found: `True`
- Expected rank: `9`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/17/Text/86', 'PZO22001 Starfinder Player Core 294-329::/page/15/Text/80', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/26']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/24', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/25', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/23']
- Expanded expected found: `True`
- Expanded expected rank: `9`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/25` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/23` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/86` | 0.889304 | **SPELLS** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/80` | 0.889304 | **SPELLS** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/26` | 0.889304 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/74` | 0.847304 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/68` | 0.847304 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/59` | 0.847304 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/61` | 0.847304 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/83` | 0.847304 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/24` | 0.847304 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/86` | 0.847304 | **SPELLS** |

### Query 23
- Text: What is the rule about **Spell Lists**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/25']
- Expected found: `True`
- Expected rank: `7`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/15/Text/81', 'PZO22001 Starfinder Player Core 294-329::/page/11/Text/84', 'PZO22001 Starfinder Player Core 294-329::/page/13/Text/75']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/25', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/26', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/24']
- Expanded expected found: `True`
- Expanded expected rank: `7`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/26` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/24` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/81` | 0.890837 | **Spell Lists** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/84` | 0.890837 | **Spell Lists** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/75` | 0.890837 | **Spell Lists** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/60` | 0.848837 | **Spell Lists** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/61` | 0.848837 | **Spell Lists** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/27` | 0.848837 | **Spell Lists** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/25` | 0.848837 | **Spell Lists** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/69` | 0.848837 | **Spell Lists** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/27/Text/69` | 0.848837 | **Spell Lists** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/23/Text/44` | 0.848837 | **Spell Lists** |

### Query 24
- Text: What is the rule about **Spells**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/26']
- Expected found: `True`
- Expected rank: `8`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/17/Text/88', 'PZO22001 Starfinder Player Core 294-329::/page/33/Text/63', 'PZO22001 Starfinder Player Core 294-329::/page/19/Text/61']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/26', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/25', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/27']
- Expanded expected found: `True`
- Expanded expected rank: `8`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/25` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/27` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/88` | 0.798799 | **Spells** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/63` | 0.798799 | **Spells** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/61` | 0.798799 | **Spells** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/88` | 0.756799 | **Spells** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/38` | 0.756799 | **Spells** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/85` | 0.756799 | **Spells** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/62` | 0.756799 | **Spells** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/26` | 0.756799 | **Spells** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/35` | 0.756799 | **Spells** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/67` | 0.756799 | **Spells** |

### Query 25
- Text: What is the rule about **Focus Spells**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/27']
- Expected found: `True`
- Expected rank: `11`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/19/Text/62', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/39', 'PZO22001 Starfinder Player Core 294-329::/page/9/Text/89']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/27', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/26', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/28']
- Expanded expected found: `True`
- Expanded expected rank: `11`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/26` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/28` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/62` | 0.926221 | **Focus Spells** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/39` | 0.926221 | **Focus Spells** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/89` | 0.926221 | **Focus Spells** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/86` | 0.884221 | **Focus Spells** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/89` | 0.884221 | **Focus Spells** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/29` | 0.884221 | **Focus Spells** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/64` | 0.884221 | **Focus Spells** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/23/Text/46` | 0.884221 | **Focus Spells** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/36` | 0.884221 | **Focus Spells** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/27/Text/71` | 0.884221 | **Focus Spells** |

### Query 26
- Text: Summarize **Rituals**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/28']
- Expected found: `True`
- Expected rank: `5`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/17/Text/90', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/30', 'PZO22001 Starfinder Player Core 294-329::/page/31/Text/64']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/28', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/29', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/27']
- Expanded expected found: `True`
- Expanded expected rank: `5`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/29` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/27` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/90` | 0.971114 | **Rituals** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/30` | 0.971114 | **Rituals** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/64` | 0.971114 | **Rituals** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/23/Text/47` | 0.929114 | **Rituals** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/28` | 0.929114 | **Rituals** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/65` | 0.929113 | **Rituals** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/84` | 0.929113 | **Rituals** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/40` | 0.929113 | **Rituals** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/78` | 0.929113 | **Rituals** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/37` | 0.929113 | **Rituals** |

### Query 27
- Text: Summarize **PLAYING THE ** **GAME**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/29']
- Expected found: `True`
- Expected rank: `5`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/27/Text/73', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/31', 'PZO22001 Starfinder Player Core 294-329::/page/7/Text/38']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/29', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/28', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/30']
- Expanded expected found: `True`
- Expanded expected rank: `5`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/28` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/30` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/27/Text/73` | 0.965000 | **PLAYING THE ** **GAME** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/38` | 0.965000 | **PLAYING THE ** **GAME** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/31` | 0.965000 | **PLAYING THE ** **GAME** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/79` | 0.923000 | **PLAYING THE ** **GAME** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/29` | 0.923000 | **PLAYING THE ** **GAME** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/88` | 0.923000 | **PLAYING THE ** **GAME** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/91` | 0.923000 | **PLAYING THE ** **GAME** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/64` | 0.923000 | **PLAYING THE ** **GAME** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/70` | 0.923000 | **PLAYING THE ** **GAME** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/91` | 0.923000 | **PLAYING THE ** **GAME** |

### Query 28
- Text: Summarize **CONDITIONS **
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/30']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/33/Text/67', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/30', 'PZO22001 Starfinder Player Core 294-329::/page/35/Text/74']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/30', 'PZO22001 Starfinder Player Core 294-329::/page/19/Text/65', 'PZO22001 Starfinder Player Core 294-329::/page/15/Text/86', 'PZO22001 Starfinder Player Core 294-329::/page/29/Text/71', 'PZO22001 Starfinder Player Core 294-329::/page/17/Text/92', 'PZO22001 Starfinder Player Core 294-329::/page/13/Text/80', 'PZO22001 Starfinder Player Core 294-329::/page/31/Text/66', 'PZO22001 Starfinder Player Core 294-329::/page/27/Text/74', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/42', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/31', 'PZO22001 Starfinder Player Core 294-329::/page/33/Text/67', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/29']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/19/Text/65` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/15/Text/86` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/29/Text/71` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/17/Text/92` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/13/Text/80` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/31/Text/66` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/27/Text/74` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/42` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/31` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/33/Text/67` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/29` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/67` | 0.894175 | **CONDITIONS ** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/30` | 0.894175 | **CONDITIONS ** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/74` | 0.894175 | **CONDITIONS ** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/27/Text/74` | 0.636199 | **CONDITIONS ** **APPENDIX** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/39` | 0.636199 | **CONDITIONS ** **APPENDIX** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/42` | 0.636199 | **CONDITIONS ** **APPENDIX** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/23/Text/49` | 0.636199 | **CONDITIONS ** **APPENDIX** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/92` | 0.636199 | **CONDITIONS ** **APPENDIX** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/86` | 0.636199 | **CONDITIONS ** **APPENDIX** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/65` | 0.636199 | **CONDITIONS ** **APPENDIX** |

### Query 29
- Text: Summarize **APPENDIX**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/31']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/31', 'PZO22001 Starfinder Player Core 294-329::/page/35/Text/75', 'PZO22001 Starfinder Player Core 294-329::/page/27/Text/74']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/31', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/32', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/30']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/32` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/30` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/31` | 0.975025 | **APPENDIX** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/75` | 0.975025 | **APPENDIX** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/27/Text/74` | 0.849313 | **CONDITIONS ** **APPENDIX** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/89` | 0.819313 | **CONDITIONS ** **APPENDIX** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/39` | 0.819313 | **CONDITIONS ** **APPENDIX** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/92` | 0.819313 | **CONDITIONS ** **APPENDIX** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/86` | 0.819313 | **CONDITIONS ** **APPENDIX** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/80` | 0.819313 | **CONDITIONS ** **APPENDIX** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/32` | 0.819313 | **CONDITIONS ** **APPENDIX** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/71` | 0.819313 | **CONDITIONS ** **APPENDIX** |

### Query 30
- Text: Summarize **GLOSSARY & ** **INDEX**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/32']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/35/Text/76', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/32', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/33']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/32', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/1', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/31']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/2/Text/1` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/31` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/76` | 0.993465 | **GLOSSARY & ** **INDEX** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/32` | 0.993465 | **GLOSSARY & ** **INDEX** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/33` | 0.993465 | **GLOSSARY & ** **INDEX** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/43` | 0.951465 | **GLOSSARY & ** **INDEX** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/90` | 0.951465 | **GLOSSARY & ** **INDEX** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/81` | 0.951465 | **GLOSSARY & ** **INDEX** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/93` | 0.951465 | **GLOSSARY & ** **INDEX** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/23/Text/50` | 0.951465 | **GLOSSARY & ** **INDEX** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/67` | 0.951465 | **GLOSSARY & ** **INDEX** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/66` | 0.951465 | **GLOSSARY & ** **INDEX** |

### Query 31
- Text: What is the rule about so long as they know the spell at that rank (see Heightened  Spontaneous Spells below). When you heighten your spell,  the spell's rank increases to match the higher rank of the  spell slot you've prepared it in or used to cast it. This is useful  for any spell, because some effects, such as counteracting,  depend on the spell's rank.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/1', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/16', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/7']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/1', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/2', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/32']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/2/Text/2` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/32` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/1` | 0.989271 | so long as they know the spell at that rank (see Heightened  Spontaneous Spells below). When you heighten your spell,  the spell's rank increases to match the higher rank of the  spell slot you've pre |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/16` | 0.812321 | Both prepared and spontaneous spellcasters can cast a spell  at a higher spell rank than that listed for the spell. This is  called heightening the spell. A prepared spellcaster can  heighten a spell |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/7` | 0.791159 | As a spontaneous caster, you can also choose to cast  a lower-rank spell using a higher-rank spell slot without  heightening it or knowing it at a higher rank. This casts the  spell at the rank you kn |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/4` | 0.744134 | Sometimes you need to identify a spell, especially if its  effects aren't obvious right away. If you notice a spell  being cast, and you have that spell in your repertoire  or prepared it that day (ev |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/2` | 0.732668 | In addition, many spells have additional specific benefits  when they are heightened, such as increased damage. These  extra benefits are described at the end of the spell's stat  block. Some heighten |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/26` | 0.720670 | **Heightened** (rank) If the spell has special effects when  heightened (page 295), those effects appear at the end  of the stat block. |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/3` | 0.701151 | Other heightened entries give a number after a plus sign,  indicating that heightening grants extra advantages over  multiple ranks. The listed effect applies for every increment  of ranks by which th |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/5` | 0.673422 | If you're a spontaneous spellcaster, you must know a spell at  the specific rank that you want to cast it in order to heighten  it. You can add a spell to your spell repertoire at more than  a single |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/1` | 0.650779 | You can't use your spell slots to cast your innate spells, but  you might have an innate spell and also be able to prepare  or cast the same spell through your class. You also can't  heighten innate s |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/11` | 0.644806 | A cantrip is always automatically heightened to half your  level, rounded up. For a typical spellcaster, this means its  rank is equal to the highest rank of spell slot you have. |

### Query 32
- Text: What is the rule about In addition, many spells have additional specific benefits  when they are heightened, such as increased damage. These  extra benefits are described at the end of the spell's stat  block. Some heightened entries specify one or more ranks  at which the spell must be prepared or cast to gain these  extra advantages. Each of these heightened entries states  specifically which aspects of the spell change at the given  rank. Read the heightened entry only for the spell rank you're  using or preparing; if its benefits are meant to include any of  the effects of a lower-rank heightened entry, those benefits  will be included in the entry.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/2', 'PZO22001 Starfinder Player Core 294-329::/page/7/Text/26', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/3']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/2', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/3', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/1']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/2/Text/3` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/2/Text/1` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/2` | 1.008375 | In addition, many spells have additional specific benefits  when they are heightened, such as increased damage. These  extra benefits are described at the end of the spell's stat  block. Some heighten |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/26` | 0.808216 | **Heightened** (rank) If the spell has special effects when  heightened (page 295), those effects appear at the end  of the stat block. |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/3` | 0.805728 | Other heightened entries give a number after a plus sign,  indicating that heightening grants extra advantages over  multiple ranks. The listed effect applies for every increment  of ranks by which th |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/1` | 0.747808 | so long as they know the spell at that rank (see Heightened  Spontaneous Spells below). When you heighten your spell,  the spell's rank increases to match the higher rank of the  spell slot you've pre |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/16` | 0.659327 | Both prepared and spontaneous spellcasters can cast a spell  at a higher spell rank than that listed for the spell. This is  called heightening the spell. A prepared spellcaster can  heighten a spell |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/4` | 0.655736 | Sometimes you need to identify a spell, especially if its  effects aren't obvious right away. If you notice a spell  being cast, and you have that spell in your repertoire  or prepared it that day (ev |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/1` | 0.626078 | You can't use your spell slots to cast your innate spells, but  you might have an innate spell and also be able to prepare  or cast the same spell through your class. You also can't  heighten innate s |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/7` | 0.608808 | As a spontaneous caster, you can also choose to cast  a lower-rank spell using a higher-rank spell slot without  heightening it or knowing it at a higher rank. This casts the  spell at the rank you kn |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/5` | 0.606978 | If you're a spontaneous spellcaster, you must know a spell at  the specific rank that you want to cast it in order to heighten  it. You can add a spell to your spell repertoire at more than  a single |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/17` | 0.583691 | Each spell uses the following format. Entries appear only  when applicable, so not all spells will have every entry  described here. The spell's name line also lists the type  of spell if it's a cantr |

### Query 33
- Text: What is the rule about Other heightened entries give a number after a plus sign,  indicating that heightening grants extra advantages over  multiple ranks. The listed effect applies for every increment  of ranks by which the spell is heightened above its lowest  spell rank, and the benefit is cumulative. For example, *slice * *reality* says "**Heightened (+1)** The damage increases by 1d8."  Because *slice reality* deals 7d8 void damage at 6th rank, a  7th-rank *slice reality* would deal 8d8 void damage, an 8thrank spell would deal 9d8 void damage, and so on.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/3']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/3', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/2', 'PZO22001 Starfinder Player Core 294-329::/page/7/Text/26']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/3', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/2', 'PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/4']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/2/Text/2` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/4` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/3` | 1.009775 | Other heightened entries give a number after a plus sign,  indicating that heightening grants extra advantages over  multiple ranks. The listed effect applies for every increment  of ranks by which th |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/2` | 0.797571 | In addition, many spells have additional specific benefits  when they are heightened, such as increased damage. These  extra benefits are described at the end of the spell's stat  block. Some heighten |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/26` | 0.780649 | **Heightened** (rank) If the spell has special effects when  heightened (page 295), those effects appear at the end  of the stat block. |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/1` | 0.704672 | so long as they know the spell at that rank (see Heightened  Spontaneous Spells below). When you heighten your spell,  the spell's rank increases to match the higher rank of the  spell slot you've pre |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/16` | 0.643081 | Both prepared and spontaneous spellcasters can cast a spell  at a higher spell rank than that listed for the spell. This is  called heightening the spell. A prepared spellcaster can  heighten a spell |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/34` | 0.626107 | **Heightened (+1)** The damage increases by 2d6 (or by 2d8 if  the target is a divine spellcaster). |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/32/Text/17` | 0.593027 | **Heightened (+1)** The damage increases by 1d6 and persistent  damage increases by 1d6. |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/7` | 0.572623 | As a spontaneous caster, you can also choose to cast  a lower-rank spell using a higher-rank spell slot without  heightening it or knowing it at a higher rank. This casts the  spell at the rank you kn |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/5` | 0.568295 | If you're a spontaneous spellcaster, you must know a spell at  the specific rank that you want to cast it in order to heighten  it. You can add a spell to your spell repertoire at more than  a single |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/11` | 0.565134 | A cantrip is always automatically heightened to half your  level, rounded up. For a typical spellcaster, this means its  rank is equal to the highest rank of spell slot you have. |

### Query 34
- Text: What is the rule about Heightened Spontaneous Spells?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/4', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/16', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/1']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/4', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/3', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/5']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/2/Text/3` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/2/Text/5` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/4` | 0.917330 | Heightened Spontaneous Spells |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/16` | 0.723674 | Both prepared and spontaneous spellcasters can cast a spell  at a higher spell rank than that listed for the spell. This is  called heightening the spell. A prepared spellcaster can  heighten a spell |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/1` | 0.706322 | so long as they know the spell at that rank (see Heightened  Spontaneous Spells below). When you heighten your spell,  the spell's rank increases to match the higher rank of the  spell slot you've pre |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/26` | 0.583138 | **Heightened** (rank) If the spell has special effects when  heightened (page 295), those effects appear at the end  of the stat block. |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/3` | 0.545572 | Other heightened entries give a number after a plus sign,  indicating that heightening grants extra advantages over  multiple ranks. The listed effect applies for every increment  of ranks by which th |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/7` | 0.535127 | As a spontaneous caster, you can also choose to cast  a lower-rank spell using a higher-rank spell slot without  heightening it or knowing it at a higher rank. This casts the  spell at the rank you kn |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/6` | 0.534855 | Many spontaneous spellcasting classes provide abilities  like the signature spells class feature, which allows you to  cast a limited number of spells as heightened versions even if  you know the spel |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/2` | 0.528378 | In addition, many spells have additional specific benefits  when they are heightened, such as increased damage. These  extra benefits are described at the end of the spell's stat  block. Some heighten |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/30/Text/1` | 0.525068 | **Heightened (5th)** The spell's range is touch and it targets  1 willing creature. The duration is until your next daily  preparations. |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/22/Text/3` | 0.512171 | **Heightened (5th)** Your battle form is Huge and your attacks  have 15-foot reach. You instead gain 20 temporary HP, AC  = 18 + your level, attack modifier +18, damage bonus +7  and double the number |

### Query 35
- Text: What is the rule about If you're a spontaneous spellcaster, you must know a spell at  the specific rank that you want to cast it in order to heighten  it. You can add a spell to your spell repertoire at more than  a single rank so that you have more options when casting it.  For example, if you added *skyfire wings* to your repertoire as  a 3rd-rank spell and again as a 7th-rank spell, you could cast  it as a 3rd-rank or a 7th-rank spell; however, you couldn't cast  it as a 5th-rank spell.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/5', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/7', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/16']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/5', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/6', 'PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/4']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/2/Text/6` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/4` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/5` | 0.988516 | If you're a spontaneous spellcaster, you must know a spell at  the specific rank that you want to cast it in order to heighten  it. You can add a spell to your spell repertoire at more than  a single |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/7` | 0.782273 | As a spontaneous caster, you can also choose to cast  a lower-rank spell using a higher-rank spell slot without  heightening it or knowing it at a higher rank. This casts the  spell at the rank you kn |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/16` | 0.738916 | Both prepared and spontaneous spellcasters can cast a spell  at a higher spell rank than that listed for the spell. This is  called heightening the spell. A prepared spellcaster can  heighten a spell |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/1` | 0.678631 | so long as they know the spell at that rank (see Heightened  Spontaneous Spells below). When you heighten your spell,  the spell's rank increases to match the higher rank of the  spell slot you've pre |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/1` | 0.676876 | You can't use your spell slots to cast your innate spells, but  you might have an innate spell and also be able to prepare  or cast the same spell through your class. You also can't  heighten innate s |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/14` | 0.668403 | If you're a spontaneous spellcaster—such as a mystic—you  choose which spell from your spell repertoire that you're  using a spell slot for at the moment you decide to cast it. This  provides you with |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/4` | 0.657374 | Sometimes you need to identify a spell, especially if its  effects aren't obvious right away. If you notice a spell  being cast, and you have that spell in your repertoire  or prepared it that day (ev |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/9` | 0.626678 | Each prepared spell is expended after a single casting,  so if you want to cast a particular spell more than once in  a day, you need to prepare that spell multiple times. The  exception to this rule |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/6` | 0.623503 | Many spontaneous spellcasting classes provide abilities  like the signature spells class feature, which allows you to  cast a limited number of spells as heightened versions even if  you know the spel |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/28` | 0.617643 | If you have an innate spell, you can cast it even if it's not of  a spell rank you can normally cast. This is especially common  for monsters. |

### Query 36
- Text: What is the rule about Many spontaneous spellcasting classes provide abilities  like the signature spells class feature, which allows you to  cast a limited number of spells as heightened versions even if  you know the spell at only a single rank.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/6', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/16', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/5']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/6', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/5', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/7']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/2/Text/5` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/2/Text/7` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/6` | 0.975070 | Many spontaneous spellcasting classes provide abilities  like the signature spells class feature, which allows you to  cast a limited number of spells as heightened versions even if  you know the spel |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/16` | 0.732832 | Both prepared and spontaneous spellcasters can cast a spell  at a higher spell rank than that listed for the spell. This is  called heightening the spell. A prepared spellcaster can  heighten a spell |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/5` | 0.679629 | If you're a spontaneous spellcaster, you must know a spell at  the specific rank that you want to cast it in order to heighten  it. You can add a spell to your spell repertoire at more than  a single |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/7` | 0.632478 | As a spontaneous caster, you can also choose to cast  a lower-rank spell using a higher-rank spell slot without  heightening it or knowing it at a higher rank. This casts the  spell at the rank you kn |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/1` | 0.623298 | You can't use your spell slots to cast your innate spells, but  you might have an innate spell and also be able to prepare  or cast the same spell through your class. You also can't  heighten innate s |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/1` | 0.604927 | so long as they know the spell at that rank (see Heightened  Spontaneous Spells below). When you heighten your spell,  the spell's rank increases to match the higher rank of the  spell slot you've pre |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/14` | 0.585027 | If you're a spontaneous spellcaster—such as a mystic—you  choose which spell from your spell repertoire that you're  using a spell slot for at the moment you decide to cast it. This  provides you with |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/4` | 0.577369 | Heightened Spontaneous Spells |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/6` | 0.575410 | Characters of spellcasting classes can cast a number of spells  each day; the spells you can cast in a day are referred to as  spell slots. At 1st level, a character has only a small number  of 1st-ra |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/3` | 0.565788 | Other heightened entries give a number after a plus sign,  indicating that heightening grants extra advantages over  multiple ranks. The listed effect applies for every increment  of ranks by which th |

### Query 37
- Text: What is the rule about As a spontaneous caster, you can also choose to cast  a lower-rank spell using a higher-rank spell slot without  heightening it or knowing it at a higher rank. This casts the  spell at the rank you know the spell, not the rank of the  higher slot. The spell doesn't have any heightened effects,  so it's usually not a very efficient use of your magic outside  of highly specific circumstances. For instance, if your party  was having trouble with an invisible enemy, and you had  *revealing light* in your repertoire but had already spent all  of your 2nd-rank spell slots, it might be worth it to use a  3rd-rank spell slot to cast the spell, even though it'd have no  heightened benefit.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/7', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/5', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/1']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/7', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/6', 'PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/8']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/2/Text/6` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/8` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/7` | 1.006613 | As a spontaneous caster, you can also choose to cast  a lower-rank spell using a higher-rank spell slot without  heightening it or knowing it at a higher rank. This casts the  spell at the rank you kn |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/5` | 0.780662 | If you're a spontaneous spellcaster, you must know a spell at  the specific rank that you want to cast it in order to heighten  it. You can add a spell to your spell repertoire at more than  a single |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/1` | 0.778462 | so long as they know the spell at that rank (see Heightened  Spontaneous Spells below). When you heighten your spell,  the spell's rank increases to match the higher rank of the  spell slot you've pre |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/16` | 0.717234 | Both prepared and spontaneous spellcasters can cast a spell  at a higher spell rank than that listed for the spell. This is  called heightening the spell. A prepared spellcaster can  heighten a spell |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/14` | 0.697257 | If you're a spontaneous spellcaster—such as a mystic—you  choose which spell from your spell repertoire that you're  using a spell slot for at the moment you decide to cast it. This  provides you with |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/1` | 0.677907 | You can't use your spell slots to cast your innate spells, but  you might have an innate spell and also be able to prepare  or cast the same spell through your class. You also can't  heighten innate s |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/4` | 0.647380 | Sometimes you need to identify a spell, especially if its  effects aren't obvious right away. If you notice a spell  being cast, and you have that spell in your repertoire  or prepared it that day (ev |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/6` | 0.610175 | Many spontaneous spellcasting classes provide abilities  like the signature spells class feature, which allows you to  cast a limited number of spells as heightened versions even if  you know the spel |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/2` | 0.609093 | In addition, many spells have additional specific benefits  when they are heightened, such as increased damage. These  extra benefits are described at the end of the spell's stat  block. Some heighten |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/28` | 0.604542 | If you have an innate spell, you can cast it even if it's not of  a spell rank you can normally cast. This is especially common  for monsters. |

### Query 38
- Text: Summarize CANTRIPS
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/8']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/8', 'PZO22001 Starfinder Player Core 294-329::/page/8/SectionHeader/6', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/9']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/8', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/9', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/7']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/2/Text/9` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/2/Text/7` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/8` | 0.951945 | CANTRIPS |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/8/SectionHeader/6` | 0.756051 | ARCANE CANTRIPS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/9` | 0.535718 | A cantrip is a special type of spell that's weaker than other  spells but can be used with greater freedom and flexibility. |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/10` | 0.379250 | The title of a cantrip's stat block says "Cantrip" instead of  "Spell", and the spell has the cantrip trait. Casting a cantrip  doesn't use up your spell slots; you can cast a cantrip at will,  any nu |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/8/Text/2` | 0.370159 | These lists include the spells for each tradition, including cantrips. (Focus spells appear on pages 375–380.)  A superscript "H" indicates a spell has extra effects when heightened, and a spell whose |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/28` | 0.366967 | **ADHERE **[one-action] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult, primal  **Range **touch; **Targets** 1 held or unattended object or a 5-footsquare sur |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/11` | 0.365149 | A cantrip is always automatically heightened to half your  level, rounded up. For a typical spellcaster, this means its  rank is equal to the highest rank of spell slot you have. |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/17` | 0.347697 | Each spell uses the following format. Entries appear only  when applicable, so not all spells will have every entry  described here. The spell's name line also lists the type  of spell if it's a cantr |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/41` | 0.341680 | **ANALYZE TARGET **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **DETECTION** **MANIPULATE**  **Traditions** arcane, divine, occult, primal **Range **30 feet; **Targets** 1 creature  **Dur |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/19` | 0.339178 | **CAUSTIC BLAST **[two-actions] **CANTRIP 1**  **ACID** **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal  **Range **30 feet; **Area** 5-foot burst  **Defense** basic Reflex  Y |

### Query 39
- Text: What is the rule about A cantrip is a special type of spell that's weaker than other  spells but can be used with greater freedom and flexibility.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/9', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/10', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/11']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/9', 'PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/8', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/10']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/8` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/2/Text/10` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/9` | 0.967053 | A cantrip is a special type of spell that's weaker than other  spells but can be used with greater freedom and flexibility. |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/10` | 0.723219 | The title of a cantrip's stat block says "Cantrip" instead of  "Spell", and the spell has the cantrip trait. Casting a cantrip  doesn't use up your spell slots; you can cast a cantrip at will,  any nu |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/11` | 0.658584 | A cantrip is always automatically heightened to half your  level, rounded up. For a typical spellcaster, this means its  rank is equal to the highest rank of spell slot you have. |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/9` | 0.607336 | Each prepared spell is expended after a single casting,  so if you want to cast a particular spell more than once in  a day, you need to prepare that spell multiple times. The  exception to this rule |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/17` | 0.563677 | Each spell uses the following format. Entries appear only  when applicable, so not all spells will have every entry  described here. The spell's name line also lists the type  of spell if it's a cantr |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/26` | 0.537211 | Certain spells are natural to your character, typically coming  from your ancestry or a magic item. They're called innate  spells. Innate spells don't let you qualify for abilities that  require you t |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/2` | 0.529926 | In rare cases, a spell might have you make some other  type of attack, such as a weapon Strike. Such attacks use the  normal rules and attack bonus for that type of attack. |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/5` | 0.529305 | Spells can vary in how many actions they take, as shown in  the spell's stat block. You cast cantrips, spells from spell slots,  and focus spells using the same process, but must expend the  spell whe |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/8/Text/2` | 0.527210 | These lists include the spells for each tradition, including cantrips. (Focus spells appear on pages 375–380.)  A superscript "H" indicates a spell has extra effects when heightened, and a spell whose |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/14` | 0.460409 | Focus spells are automatically heightened to half your level  rounded up, just like cantrips are. You can't cast a focus spell  if its minimum rank is greater than half your level rounded  up, even if |

### Query 40
- Text: What is the rule about The title of a cantrip's stat block says "Cantrip" instead of  "Spell", and the spell has the cantrip trait. Casting a cantrip  doesn't use up your spell slots; you can cast a cantrip at will,  any number of times per day. If you're a prepared caster, you  can prepare a specific number of cantrips each day. You can't  prepare a cantrip in a spell slot.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/10', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/9', 'PZO22001 Starfinder Player Core 294-329::/page/4/Text/5']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/10', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/11', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/9']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/2/Text/11` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/2/Text/9` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/10` | 1.005414 | The title of a cantrip's stat block says "Cantrip" instead of  "Spell", and the spell has the cantrip trait. Casting a cantrip  doesn't use up your spell slots; you can cast a cantrip at will,  any nu |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/9` | 0.826803 | Each prepared spell is expended after a single casting,  so if you want to cast a particular spell more than once in  a day, you need to prepare that spell multiple times. The  exception to this rule |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/5` | 0.758035 | Spells can vary in how many actions they take, as shown in  the spell's stat block. You cast cantrips, spells from spell slots,  and focus spells using the same process, but must expend the  spell whe |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/26` | 0.662688 | Certain spells are natural to your character, typically coming  from your ancestry or a magic item. They're called innate  spells. Innate spells don't let you qualify for abilities that  require you t |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/11` | 0.660045 | A cantrip is always automatically heightened to half your  level, rounded up. For a typical spellcaster, this means its  rank is equal to the highest rank of spell slot you have. |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/6` | 0.644050 | Characters of spellcasting classes can cast a number of spells  each day; the spells you can cast in a day are referred to as  spell slots. At 1st level, a character has only a small number  of 1st-ra |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/17` | 0.633851 | Each spell uses the following format. Entries appear only  when applicable, so not all spells will have every entry  described here. The spell's name line also lists the type  of spell if it's a cantr |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/1` | 0.612034 | You can't use your spell slots to cast your innate spells, but  you might have an innate spell and also be able to prepare  or cast the same spell through your class. You also can't  heighten innate s |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/9` | 0.610942 | A cantrip is a special type of spell that's weaker than other  spells but can be used with greater freedom and flexibility. |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/14` | 0.605976 | If you're a spontaneous spellcaster—such as a mystic—you  choose which spell from your spell repertoire that you're  using a spell slot for at the moment you decide to cast it. This  provides you with |

### Query 41
- Text: What is the rule about A cantrip is always automatically heightened to half your  level, rounded up. For a typical spellcaster, this means its  rank is equal to the highest rank of spell slot you have.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/11', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/14', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/10']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/11', 'PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/12', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/10']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/12` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/2/Text/10` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/11` | 1.002053 | A cantrip is always automatically heightened to half your  level, rounded up. For a typical spellcaster, this means its  rank is equal to the highest rank of spell slot you have. |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/14` | 0.742872 | Focus spells are automatically heightened to half your level  rounded up, just like cantrips are. You can't cast a focus spell  if its minimum rank is greater than half your level rounded  up, even if |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/10` | 0.686094 | The title of a cantrip's stat block says "Cantrip" instead of  "Spell", and the spell has the cantrip trait. Casting a cantrip  doesn't use up your spell slots; you can cast a cantrip at will,  any nu |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/1` | 0.641290 | so long as they know the spell at that rank (see Heightened  Spontaneous Spells below). When you heighten your spell,  the spell's rank increases to match the higher rank of the  spell slot you've pre |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/16` | 0.612442 | Both prepared and spontaneous spellcasters can cast a spell  at a higher spell rank than that listed for the spell. This is  called heightening the spell. A prepared spellcaster can  heighten a spell |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/9` | 0.586452 | Each prepared spell is expended after a single casting,  so if you want to cast a particular spell more than once in  a day, you need to prepare that spell multiple times. The  exception to this rule |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/26` | 0.585785 | **Heightened** (rank) If the spell has special effects when  heightened (page 295), those effects appear at the end  of the stat block. |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/3` | 0.580064 | Other heightened entries give a number after a plus sign,  indicating that heightening grants extra advantages over  multiple ranks. The listed effect applies for every increment  of ranks by which th |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/5` | 0.568402 | If you're a spontaneous spellcaster, you must know a spell at  the specific rank that you want to cast it in order to heighten  it. You can add a spell to your spell repertoire at more than  a single |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/2` | 0.556369 | In addition, many spells have additional specific benefits  when they are heightened, such as increased damage. These  extra benefits are described at the end of the spell's stat  block. Some heighten |

### Query 42
- Text: What is the rule about FOCUS SPELLS?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/12']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/12', 'PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/20', 'PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/21']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/12', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/13', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/11']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/2/Text/13` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/2/Text/11` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/12` | 0.905808 | FOCUS SPELLS |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/20` | 0.770076 | NON-SPELLCASTERS WITH  FOCUS SPELLS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/21` | 0.764073 | SPELLCASTERS WITH FOCUS  SPELLS |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/1` | 0.599590 | SPELLS |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0` | 0.589353 | CHAPTER 7: SPELLS |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/39` | 0.585351 | **Focus Spells** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/36` | 0.585351 | **Focus Spells** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/86` | 0.585351 | **Focus Spells** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/77` | 0.585351 | **Focus Spells** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/83` | 0.585351 | **Focus Spells** |

### Query 43
- Text: What is the rule about Focus spells are a special type of spell attained directly from  a specific source, such as a field of study, connection to a  mystical force, or exposure to an alternate reality. You can  learn focus spells only through special class features or feats,  rather than choosing them from a spell list. Furthermore, you  cast focus spells using a special pool of Focus Points—you can't  prepare a focus spell in a spell slot or use your spell slots to  cast focus spells; similarly, you can't spend your Focus Points  to cast spells that aren't focus spells. Even some classes that  don't normally grant spellcasting can grant focus spells. The  title of a focus spell's stat block says "Focus" instead of "Spell",  and the spell has the focus trait.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/13', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/21', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/15']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/13', 'PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/12', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/14']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/12` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/2/Text/14` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/13` | 0.999717 | Focus spells are a special type of spell attained directly from  a specific source, such as a field of study, connection to a  mystical force, or exposure to an alternate reality. You can  learn focus |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/21` | 0.872553 | If you get focus spells from a class or other source that  doesn't grant spellcasting ability, the ability that gives you  focus spells also provides your proficiency for your spell  attack modifier a |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/15` | 0.776929 | Casting any of your focus spells costs you 1 Focus Point.  You automatically gain a focus pool the first time you gain an  ability that gives you a focus spell. The maximum number of  points in your p |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/5` | 0.723295 | Spells can vary in how many actions they take, as shown in  the spell's stat block. You cast cantrips, spells from spell slots,  and focus spells using the same process, but must expend the  spell whe |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/22` | 0.718178 | If you are a spellcaster, your focus spells are the same tradition  of spell as the class that gave you the focus spell. A mystic's |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/23` | 0.706389 | It's possible, especially through archetypes, to gain focus  spells from more than one source. If this happens, you  have just one focus pool, counting all your focus spells to  determine the points i |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/14` | 0.655669 | Focus spells are automatically heightened to half your level  rounded up, just like cantrips are. You can't cast a focus spell  if its minimum rank is greater than half your level rounded  up, even if |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/36` | 0.635524 | **Focus Spells** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/77` | 0.635524 | **Focus Spells** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/89` | 0.635524 | **Focus Spells** |

### Query 44
- Text: What is the rule about Focus spells are automatically heightened to half your level  rounded up, just like cantrips are. You can't cast a focus spell  if its minimum rank is greater than half your level rounded  up, even if you somehow gain access to it.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/14']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/14', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/11', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/15']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/14', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/15', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/13']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/2/Text/15` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/2/Text/13` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/14` | 1.011691 | Focus spells are automatically heightened to half your level  rounded up, just like cantrips are. You can't cast a focus spell  if its minimum rank is greater than half your level rounded  up, even if |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/11` | 0.726496 | A cantrip is always automatically heightened to half your  level, rounded up. For a typical spellcaster, this means its  rank is equal to the highest rank of spell slot you have. |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/15` | 0.670748 | Casting any of your focus spells costs you 1 Focus Point.  You automatically gain a focus pool the first time you gain an  ability that gives you a focus spell. The maximum number of  points in your p |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/21` | 0.618968 | If you get focus spells from a class or other source that  doesn't grant spellcasting ability, the ability that gives you  focus spells also provides your proficiency for your spell  attack modifier a |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/13` | 0.597427 | Focus spells are a special type of spell attained directly from  a specific source, such as a field of study, connection to a  mystical force, or exposure to an alternate reality. You can  learn focus |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/5` | 0.582509 | Spells can vary in how many actions they take, as shown in  the spell's stat block. You cast cantrips, spells from spell slots,  and focus spells using the same process, but must expend the  spell whe |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/1` | 0.533589 | so long as they know the spell at that rank (see Heightened  Spontaneous Spells below). When you heighten your spell,  the spell's rank increases to match the higher rank of the  spell slot you've pre |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/10` | 0.528692 | The title of a cantrip's stat block says "Cantrip" instead of  "Spell", and the spell has the cantrip trait. Casting a cantrip  doesn't use up your spell slots; you can cast a cantrip at will,  any nu |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/23` | 0.518544 | It's possible, especially through archetypes, to gain focus  spells from more than one source. If this happens, you  have just one focus pool, counting all your focus spells to  determine the points i |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/22` | 0.512763 | If you are a spellcaster, your focus spells are the same tradition  of spell as the class that gave you the focus spell. A mystic's |

### Query 45
- Text: What is the rule about Casting any of your focus spells costs you 1 Focus Point.  You automatically gain a focus pool the first time you gain an  ability that gives you a focus spell. The maximum number of  points in your pool is equal to the number of focus spells you  know or 3, whichever is lower. This counts only spells that  require Focus Points to cast.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/15']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/15', 'PZO22001 Starfinder Player Core 294-329::/page/4/Text/5', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/13']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/15', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/16', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/14']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/2/Text/16` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/2/Text/14` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/15` | 0.988210 | Casting any of your focus spells costs you 1 Focus Point.  You automatically gain a focus pool the first time you gain an  ability that gives you a focus spell. The maximum number of  points in your p |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/5` | 0.747785 | Spells can vary in how many actions they take, as shown in  the spell's stat block. You cast cantrips, spells from spell slots,  and focus spells using the same process, but must expend the  spell whe |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/13` | 0.729098 | Focus spells are a special type of spell attained directly from  a specific source, such as a field of study, connection to a  mystical force, or exposure to an alternate reality. You can  learn focus |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/23` | 0.685936 | It's possible, especially through archetypes, to gain focus  spells from more than one source. If this happens, you  have just one focus pool, counting all your focus spells to  determine the points i |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/21` | 0.674744 | If you get focus spells from a class or other source that  doesn't grant spellcasting ability, the ability that gives you  focus spells also provides your proficiency for your spell  attack modifier a |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/14` | 0.669402 | Focus spells are automatically heightened to half your level  rounded up, just like cantrips are. You can't cast a focus spell  if its minimum rank is greater than half your level rounded  up, even if |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/20` | 0.587437 | You spend 10 minutes performing deeds to restore your  magical connection. This restores 1 Focus Point to your focus  pool. The deeds you need to perform are specified in the class  or ability that gi |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/16` | 0.581538 | You replenish all the Focus Points in your pool during your  daily preparations. You can also use the Refocus activity to  pray, study, meditate, or otherwise reattune yourself to the  source of your |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/22` | 0.570209 | If you are a spellcaster, your focus spells are the same tradition  of spell as the class that gave you the focus spell. A mystic's |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/19` | 0.568789 | **Requirements** You have a focus pool. |

### Query 46
- Text: What is the rule about You replenish all the Focus Points in your pool during your  daily preparations. You can also use the Refocus activity to  pray, study, meditate, or otherwise reattune yourself to the  source of your focus magic and regain 1 Focus Point. You can  Refocus multiple times to regain multiple points, up to your  pool's maximum.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/16']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/16', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/23', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/20']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/16', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/15', 'PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/17']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/2/Text/15` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/17` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/16` | 0.998731 | You replenish all the Focus Points in your pool during your  daily preparations. You can also use the Refocus activity to  pray, study, meditate, or otherwise reattune yourself to the  source of your |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/23` | 0.757889 | It's possible, especially through archetypes, to gain focus  spells from more than one source. If this happens, you  have just one focus pool, counting all your focus spells to  determine the points i |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/20` | 0.691465 | You spend 10 minutes performing deeds to restore your  magical connection. This restores 1 Focus Point to your focus  pool. The deeds you need to perform are specified in the class  or ability that gi |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/15` | 0.647015 | Casting any of your focus spells costs you 1 Focus Point.  You automatically gain a focus pool the first time you gain an  ability that gives you a focus spell. The maximum number of  points in your p |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/19` | 0.585373 | **Requirements** You have a focus pool. |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/32/SectionHeader/18` | 0.547245 | **DIVINE INSPIRATION **[two-actions] **SPELL 8**  **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** divine  **Range **touch;** Targets** 1 willing creature  You infuse a target with spiritual |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/5` | 0.509893 | Spells can vary in how many actions they take, as shown in  the spell's stat block. You cast cantrips, spells from spell slots,  and focus spells using the same process, but must expend the  spell whe |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/13` | 0.505351 | Focus spells are a special type of spell attained directly from  a specific source, such as a field of study, connection to a  mystical force, or exposure to an alternate reality. You can  learn focus |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/72` | 0.493859 | **Focus Spells** **Rituals** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/10` | 0.486105 | You might gain an ability that allows you to swap  prepared spells or perform other aspects of preparing spells  at different times throughout the day, but only your daily  preparation counts for the |

### Query 47
- Text: Summarize **REFOCUS**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/17']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/17', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/16', 'PZO22001 Starfinder Player Core 294-329::/page/35/Text/75']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/17', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/16', 'PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/18']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/2/Text/16` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/18` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/17` | 0.975786 | **REFOCUS** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/16` | 0.509780 | You replenish all the Focus Points in your pool during your  daily preparations. You can also use the Refocus activity to  pray, study, meditate, or otherwise reattune yourself to the  source of your |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/75` | 0.400144 | **APPENDIX** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/31` | 0.358144 | **APPENDIX** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/18` | 0.356769 | **INTRODUCTION** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/20` | 0.356769 | **INTRODUCTION** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/53` | 0.356769 | **INTRODUCTION** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/80` | 0.356769 | **INTRODUCTION** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/55` | 0.356769 | **INTRODUCTION** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/62` | 0.356769 | **INTRODUCTION** |

### Query 48
- Text: Summarize **CONCENTRATE** **EXPLORATION**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/18']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/18', 'PZO22001 Starfinder Player Core 294-329::/page/29/SectionHeader/9', 'PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/54']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/18', 'PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/17', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/19']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/17` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/2/Text/19` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/18` | 0.997153 | **CONCENTRATE** **EXPLORATION** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/29/SectionHeader/9` | 0.521821 | **CREATE WATER **[two-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE** **WATER**  **Traditions** arcane, divine, primal  **Range **0 feet |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/54` | 0.478493 | **CLEAR MIND **[two-actions] **SPELL 2**  **CONCENTRATE** **HEALING** **MANIPULATE** **MENTAL**  **Traditions** divine, occult, primal  **Range **touch; **Targets** 1 willing creature  You drive menta |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/30/Text/49` | 0.434830 | **DETECT POISON **[two-actions] **SPELL 1**  **UNCOMMON** **CONCENTRATE** **DETECTION** **MANIPULATE**  **Traditions** divine, primal  **Range **30 feet;** Targets** 1 object or creature  You detect w |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/28/Text/11` | 0.427909 | **CONFUSION **[two-actions] **SPELL 4**  **CONCENTRATE** **EMOTION** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult **Range **30 feet;** Targets** 1 creature **Defense** Will; **Duration** 1 |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/41` | 0.423781 | **ANALYZE TARGET **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **DETECTION** **MANIPULATE**  **Traditions** arcane, divine, occult, primal **Range **30 feet; **Targets** 1 creature  **Dur |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/29` | 0.422933 | **Analyze** **Target**H Gather data about a target's basic physiology. **Daze**H Cloud a creature's mind and possibly stun it. |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/42` | 0.422933 | **Analyze** **Target**H Gather data about a target's basic physiology. **Daze**H Cloud a creature's mind and possibly stun it. |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/4` | 0.422893 | **AIR BUBBLE **[reaction] **SPELL 1**  **AIR** **CONCENTRATE**  **Traditions** arcane, divine, primal  **Trigger** A creature within range enters an environment where  it can't breathe.  **Range **60 |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/35/SectionHeader/32` | 0.417239 | **ENFEEBLE **[two-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, occult  **Range **30 feet;** Targets** 1 creature  **Defense** Fortitude; **Duration** varies  Yo |

### Query 49
- Text: Summarize **Requirements** You have a focus pool.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/19']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/19', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/15', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/16']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/19', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/20', 'PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/18']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/2/Text/20` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/18` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/19` | 1.017178 | **Requirements** You have a focus pool. |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/15` | 0.682162 | Casting any of your focus spells costs you 1 Focus Point.  You automatically gain a focus pool the first time you gain an  ability that gives you a focus spell. The maximum number of  points in your p |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/16` | 0.630299 | You replenish all the Focus Points in your pool during your  daily preparations. You can also use the Refocus activity to  pray, study, meditate, or otherwise reattune yourself to the  source of your |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/20` | 0.549547 | You spend 10 minutes performing deeds to restore your  magical connection. This restores 1 Focus Point to your focus  pool. The deeds you need to perform are specified in the class  or ability that gi |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/23` | 0.535819 | It's possible, especially through archetypes, to gain focus  spells from more than one source. If this happens, you  have just one focus pool, counting all your focus spells to  determine the points i |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/36` | 0.511661 | **Focus Spells** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/77` | 0.511661 | **Focus Spells** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/64` | 0.511661 | **Focus Spells** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/27` | 0.511661 | **Focus Spells** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/39` | 0.511661 | **Focus Spells** |

### Query 50
- Text: What is the rule about You spend 10 minutes performing deeds to restore your  magical connection. This restores 1 Focus Point to your focus  pool. The deeds you need to perform are specified in the class  or ability that gives you your focus spells. These deeds can  usually overlap with other tasks that relate to the source  of your focus spells. For instance, a witchwarper with focus  points from their paradox can usually Refocus while using  their paradox skill.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/20']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/20', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/23', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/16']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/20', 'PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/21', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/19']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/21` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/2/Text/19` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/20` | 0.995092 | You spend 10 minutes performing deeds to restore your  magical connection. This restores 1 Focus Point to your focus  pool. The deeds you need to perform are specified in the class  or ability that gi |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/23` | 0.720785 | It's possible, especially through archetypes, to gain focus  spells from more than one source. If this happens, you  have just one focus pool, counting all your focus spells to  determine the points i |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/16` | 0.697014 | You replenish all the Focus Points in your pool during your  daily preparations. You can also use the Refocus activity to  pray, study, meditate, or otherwise reattune yourself to the  source of your |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/15` | 0.664361 | Casting any of your focus spells costs you 1 Focus Point.  You automatically gain a focus pool the first time you gain an  ability that gives you a focus spell. The maximum number of  points in your p |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/13` | 0.621699 | Focus spells are a special type of spell attained directly from  a specific source, such as a field of study, connection to a  mystical force, or exposure to an alternate reality. You can  learn focus |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/21` | 0.595618 | If you get focus spells from a class or other source that  doesn't grant spellcasting ability, the ability that gives you  focus spells also provides your proficiency for your spell  attack modifier a |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/5` | 0.584212 | Spells can vary in how many actions they take, as shown in  the spell's stat block. You cast cantrips, spells from spell slots,  and focus spells using the same process, but must expend the  spell whe |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/22` | 0.575380 | If you are a spellcaster, your focus spells are the same tradition  of spell as the class that gave you the focus spell. A mystic's |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/24` | 0.571197 | spells and precog warp spells, your mystic spells would  remain divine and the witchwarper spells occult. Similarly,  you need to use the attribute modifier determined by the  source of the focus spel |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/14` | 0.532373 | Focus spells are automatically heightened to half your level  rounded up, just like cantrips are. You can't cast a focus spell  if its minimum rank is greater than half your level rounded  up, even if |

### Query 51
- Text: What is the rule about SPELLCASTERS WITH FOCUS  SPELLS?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/21']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/21', 'PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/20', 'PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/12']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/21', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/22', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/20']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/2/Text/22` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/2/Text/20` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/21` | 0.911459 | SPELLCASTERS WITH FOCUS  SPELLS |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/20` | 0.901290 | NON-SPELLCASTERS WITH  FOCUS SPELLS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/12` | 0.749811 | FOCUS SPELLS |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0` | 0.527192 | CHAPTER 7: SPELLS |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/2` | 0.526463 | CASTING SPELLS |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/21` | 0.523803 | If you get focus spells from a class or other source that  doesn't grant spellcasting ability, the ability that gives you  focus spells also provides your proficiency for your spell  attack modifier a |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/7/SectionHeader/3` | 0.521143 | IDENTIFYING SPELLS |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/36` | 0.512783 | **Focus Spells** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/86` | 0.512783 | **Focus Spells** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/63` | 0.512783 | **Focus Spells** |

### Query 52
- Text: What is the rule about If you are a spellcaster, your focus spells are the same tradition  of spell as the class that gave you the focus spell. A mystic's?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/22']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/22', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/21', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/13']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/22', 'PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/21', 'PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/1']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/21` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/1` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/22` | 0.993789 | If you are a spellcaster, your focus spells are the same tradition  of spell as the class that gave you the focus spell. A mystic's |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/21` | 0.743136 | If you get focus spells from a class or other source that  doesn't grant spellcasting ability, the ability that gives you  focus spells also provides your proficiency for your spell  attack modifier a |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/13` | 0.706512 | Focus spells are a special type of spell attained directly from  a specific source, such as a field of study, connection to a  mystical force, or exposure to an alternate reality. You can  learn focus |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/3` | 0.634007 | Your class determines which tradition of magic your spells use. In some cases, such as when a mystic gains spells from  their connection or when a witchwarper learns spells from their paradox, you mig |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/5` | 0.595428 | Spells can vary in how many actions they take, as shown in  the spell's stat block. You cast cantrips, spells from spell slots,  and focus spells using the same process, but must expend the  spell whe |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/23` | 0.587783 | It's possible, especially through archetypes, to gain focus  spells from more than one source. If this happens, you  have just one focus pool, counting all your focus spells to  determine the points i |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/24` | 0.587713 | spells and precog warp spells, your mystic spells would  remain divine and the witchwarper spells occult. Similarly,  you need to use the attribute modifier determined by the  source of the focus spel |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/15` | 0.566035 | Casting any of your focus spells costs you 1 Focus Point.  You automatically gain a focus pool the first time you gain an  ability that gives you a focus spell. The maximum number of  points in your p |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/14` | 0.559704 | If you're a spontaneous spellcaster—such as a mystic—you  choose which spell from your spell repertoire that you're  using a spell slot for at the moment you decide to cast it. This  provides you with |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/83` | 0.541326 | **Focus Spells** |

### Query 53
- Text: Summarize **MAGICAL TRADITIONS**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/1', 'PZO22001 Starfinder Player Core 294-329::/page/7/Text/21', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/4']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/1', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/2', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/22']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/2` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/2/Text/22` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/1` | 0.994464 | **MAGICAL TRADITIONS** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/21` | 0.724783 | **Tradition** This entry lists the magical traditions the spell  belongs to. Some feats or other abilities might add a  spell to your spell list even if you don't follow the listed  traditions. |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/4` | 0.637170 | Some types of magic, such as that of most magic items, don't belong to any single tradition. These have the magical  trait instead of a tradition trait. |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/40` | 0.520356 | **Rituals** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/30` | 0.520356 | **Rituals** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/64` | 0.520356 | **Rituals** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/90` | 0.520356 | **Rituals** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/65` | 0.520356 | **Rituals** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/37` | 0.520356 | **Rituals** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/63` | 0.520356 | **Rituals** |

### Query 54
- Text: What is the rule about Spellcasters cast spells from one of four different spell lists, each representing a different magical tradition: arcane,  divine, occult, and primal.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/2', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/3', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/7']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/2', 'PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/1', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/3']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/1` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/3` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/2` | 0.958193 | Spellcasters cast spells from one of four different spell lists, each representing a different magical tradition: arcane,  divine, occult, and primal. |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/3` | 0.703649 | Your class determines which tradition of magic your spells use. In some cases, such as when a mystic gains spells from  their connection or when a witchwarper learns spells from their paradox, you mig |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/7` | 0.653608 | Arcane spellcasters use logic and  rationality to categorize the magic inherent  in the world around them. Because of its far-reaching  approach, the arcane tradition has the broadest spell  list, tho |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/6` | 0.564239 | Characters of spellcasting classes can cast a number of spells  each day; the spells you can cast in a day are referred to as  spell slots. At 1st level, a character has only a small number  of 1st-ra |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/15` | 0.563690 | systematic way. Witchwarpers touched by the Gap or  alternate timelines, as well as mystics who are psychically  linked to the Akashic Record, are occult spellcasters. |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/5` | 0.556011 | Spells can vary in how many actions they take, as shown in  the spell's stat block. You cast cantrips, spells from spell slots,  and focus spells using the same process, but must expend the  spell whe |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/21` | 0.541734 | **Tradition** This entry lists the magical traditions the spell  belongs to. Some feats or other abilities might add a  spell to your spell list even if you don't follow the listed  traditions. |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/4` | 0.535953 | With special gestures and utterances, a spellcaster can  call forth mystic energies, warp the mind, protect themself  against danger, or even create something from nothing.  Each class has its own met |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/4` | 0.526007 | Spellcasting creates obvious sensory manifestations, such  as bright lights, crackling sounds, and sharp smells from the  gathering magic. Nearly all spells manifest a spell signature—a  colorful, glo |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/28` | 0.519807 | If you have an innate spell, you can cast it even if it's not of  a spell rank you can normally cast. This is especially common  for monsters. |

### Query 55
- Text: What is the rule about Your class determines which tradition of magic your spells use. In some cases, such as when a mystic gains spells from  their connection or when a witchwarper learns spells from their paradox, you might be able to cast one or more select  spells from a different spell list than the list you normally cast from; for instance, mystics with the elemental connection  can conjure a *spiritual guardian*, perhaps in the form of a nature deity's attendant or servitor. In these cases, the spell  uses your magic tradition, not the list the spell normally comes from. When you cast a spell, add your tradition's trait to  the spell.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/3']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/3', 'PZO22001 Starfinder Player Core 294-329::/page/7/Text/21', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/4']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/3', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/2', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/4']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/2` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/4` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/3` | 1.008803 | Your class determines which tradition of magic your spells use. In some cases, such as when a mystic gains spells from  their connection or when a witchwarper learns spells from their paradox, you mig |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/21` | 0.743995 | **Tradition** This entry lists the magical traditions the spell  belongs to. Some feats or other abilities might add a  spell to your spell list even if you don't follow the listed  traditions. |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/4` | 0.686749 | Some types of magic, such as that of most magic items, don't belong to any single tradition. These have the magical  trait instead of a tradition trait. |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/22` | 0.624921 | If you are a spellcaster, your focus spells are the same tradition  of spell as the class that gave you the focus spell. A mystic's |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/14` | 0.623054 | If you're a spontaneous spellcaster—such as a mystic—you  choose which spell from your spell repertoire that you're  using a spell slot for at the moment you decide to cast it. This  provides you with |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/2` | 0.608544 | Spellcasters cast spells from one of four different spell lists, each representing a different magical tradition: arcane,  divine, occult, and primal. |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/1` | 0.590159 | You can't use your spell slots to cast your innate spells, but  you might have an innate spell and also be able to prepare  or cast the same spell through your class. You also can't  heighten innate s |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/28` | 0.582541 | If you have an innate spell, you can cast it even if it's not of  a spell rank you can normally cast. This is especially common  for monsters. |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/4` | 0.573735 | Sometimes you need to identify a spell, especially if its  effects aren't obvious right away. If you notice a spell  being cast, and you have that spell in your repertoire  or prepared it that day (ev |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/24` | 0.558869 | spells and precog warp spells, your mystic spells would  remain divine and the witchwarper spells occult. Similarly,  you need to use the attribute modifier determined by the  source of the focus spel |

### Query 56
- Text: What is the rule about Some types of magic, such as that of most magic items, don't belong to any single tradition. These have the magical  trait instead of a tradition trait.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/4', 'PZO22001 Starfinder Player Core 294-329::/page/7/Text/21', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/3']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/4', 'PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/6', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/3']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/6` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/3` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/4` | 0.980162 | Some types of magic, such as that of most magic items, don't belong to any single tradition. These have the magical  trait instead of a tradition trait. |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/21` | 0.722592 | **Tradition** This entry lists the magical traditions the spell  belongs to. Some feats or other abilities might add a  spell to your spell list even if you don't follow the listed  traditions. |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/3` | 0.681242 | Your class determines which tradition of magic your spells use. In some cases, such as when a mystic gains spells from  their connection or when a witchwarper learns spells from their paradox, you mig |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/1` | 0.582384 | **MAGICAL TRADITIONS** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/4` | 0.533505 | Non-magical light always shines in non-magical darkness  and always fails to shine in magical darkness. Magical light  always shines in non-magical darkness but shines in magical  darkness only if the |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/33/ListItem/20` | 0.527750 | **Tradition Resistance** If the dragon's magical tradition  matches that of your *dragon form* spell, you gain the  listed ability. **Arcane** resistance 5 against damage from  spells; **divine** resi |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/14` | 0.510334 | These effects completely transform the target into a new  form. A target can't be under the effect of more than  one polymorph at a time. If it comes under the effect of  another, the second effect at |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/2` | 0.490169 | In rare cases, a spell might have you make some other  type of attack, such as a weapon Strike. Such attacks use the  normal rules and attack bonus for that type of attack. |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/22` | 0.484059 | If you are a spellcaster, your focus spells are the same tradition  of spell as the class that gave you the focus spell. A mystic's |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/12` | 0.478861 | Spells that slightly alter a creature's form have the morph trait.  Any Strikes specifically granted by a magical morph effect also  gain the magical trait. You can be affected by multiple morph  spel |

### Query 57
- Text: Summarize **Arcane**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/6', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/7', 'PZO22001 Starfinder Player Core 294-329::/page/8/SectionHeader/5']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/6', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/7', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/4']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/7` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/4` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/6` | 0.950064 | **Arcane** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/7` | 0.513430 | Arcane spellcasters use logic and  rationality to categorize the magic inherent  in the world around them. Because of its far-reaching  approach, the arcane tradition has the broadest spell  list, tho |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/8/SectionHeader/5` | 0.513079 | ARCANE SPELLS |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/34/SectionHeader/38` | 0.470207 | **ELECTRIC ARC **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **ELECTRICITY** **MANIPULATE**  **Traditions** arcane, primal  **Range **30 feet; **Targets** 1 or 2 creatures  **Defense** ba |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/31/SectionHeader/19` | 0.461462 | **DISCHARGE **[two-actions] **SPELL 3**  **CONCENTRATE** **ELECTRICITY** **MANIPULATE**  **Traditions** arcane, primal  **Range **30 feet;** Targets** 1 creature or object with the tech  trait  **Defe |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/22/Text/11` | 0.444738 | **ARCTIC RIFT **[two-actions] **SPELL 8**  **COLD** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal  **Area** 120-foot line  **Defense** Fortitude  A jagged crack opens in the air, deali |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/11/SectionHeader/20` | 0.441484 | ARCANE 10TH-RANK SPELLS |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/9/SectionHeader/71` | 0.439305 | ARCANE 4TH-RANK SPELLS |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/9/SectionHeader/4` | 0.439147 | ARCANE 2ND-RANK SPELLS |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/33/ListItem/20` | 0.431942 | **Tradition Resistance** If the dragon's magical tradition  matches that of your *dragon form* spell, you gain the  listed ability. **Arcane** resistance 5 against damage from  spells; **divine** resi |

### Query 58
- Text: What is the rule about Arcane spellcasters use logic and  rationality to categorize the magic inherent  in the world around them. Because of its far-reaching  approach, the arcane tradition has the broadest spell  list, though it's generally poor at affecting the spirit or  the soul. Witchwarpers who analyze probability and  spellcasters who draw magic from the underlying code  of the Universe are practitioners of arcane magic.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/7', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/2', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/15']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/7', 'PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/9', 'PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/6']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/9` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/6` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/7` | 1.008890 | Arcane spellcasters use logic and  rationality to categorize the magic inherent  in the world around them. Because of its far-reaching  approach, the arcane tradition has the broadest spell  list, tho |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/2` | 0.674191 | Spellcasters cast spells from one of four different spell lists, each representing a different magical tradition: arcane,  divine, occult, and primal. |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/15` | 0.668287 | systematic way. Witchwarpers touched by the Gap or  alternate timelines, as well as mystics who are psychically  linked to the Akashic Record, are occult spellcasters. |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/3` | 0.615950 | Even with the widespread presence of technology,  spellcasters can be found in every corner of the galaxy.  Some spellcasters draw magic from other realities, some  from their mystical connections to |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/4` | 0.599225 | With special gestures and utterances, a spellcaster can  call forth mystic energies, warp the mind, protect themself  against danger, or even create something from nothing.  Each class has its own met |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/3` | 0.589125 | Your class determines which tradition of magic your spells use. In some cases, such as when a mystic gains spells from  their connection or when a witchwarper learns spells from their paradox, you mig |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/1` | 0.571675 | Whether it comes in the form of eldritch artifacts, otherworldly beings, or witchwarpers altering  reality with strange spells, magic brings fantasy and wonder to Starfinder. This chapter explains how |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/12` | 0.563689 | After Triune's Signal connected cultures across the  Universe, the peoples of the galaxy have learned more  than ever before about the Universe's composition  thanks to science and technology. As tech |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/2` | 0.560218 | The grand variety of spells includes those in the following pages and far more. Taught at magical  academies, drawn from other worlds, bestowed by mystical connections, and granted by all manner of  u |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/14` | 0.541431 | The practitioners of occult traditions seek  to understand the unexplainable, categorize  the bizarre, and otherwise access the ephemeral in a |

### Query 59
- Text: Summarize **Divine**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/9', 'PZO22001 Starfinder Player Core 294-329::/page/12/Text/57', 'PZO22001 Starfinder Player Core 294-329::/page/32/SectionHeader/7']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/9', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/7', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/10']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/7` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/10` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/9` | 0.922058 | **Divine** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/12/Text/57` | 0.563926 | **Divine Immolation**H Call divine fire from the sky. |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/32/SectionHeader/7` | 0.559177 | **DIVINE IMMOLATION **[two-actions] **SPELL 5**  **CONCENTRATE** **FIRE** **MANIPULATE** **SANCTIFIED** **SPIRIT**  **Traditions** divine  **Range **120 feet;** Area** 20-foot burst  **Defense** Refle |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/32/SectionHeader/24` | 0.509729 | **DIVINE LANCE **[two-actions] **CANTRIP 1**  **ATTACK** **CANTRIP** **CONCENTRATE** **MANIPULATE** **SANCTIFIED** **SPIRIT**  **Traditions** divine  **Range **60 feet; **Targets** 1 creature  **Defen |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/32/SectionHeader/32` | 0.497716 | **DIVINE WRATH **[two-actions] **SPELL 4**  **CONCENTRATE** **MANIPULATE** **SANCTIFIED** **SPIRIT**  **Traditions** divine  **Range **120 feet;** Area** 20-foot burst  **Defense** Fortitude  You chan |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/32/SectionHeader/18` | 0.485827 | **DIVINE INSPIRATION **[two-actions] **SPELL 8**  **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** divine  **Range **touch;** Targets** 1 willing creature  You infuse a target with spiritual |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/12/Text/42` | 0.475587 | **Dispelling Globe**U Counteract magic that enters this sphere. **Divine Wrath**H Damage and hinder creatures opposing your  deity's will. |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/16/Text/43` | 0.464475 | **Guidance** Divine guidance improves one roll. |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/31` | 0.446931 | **Divine Lance**H Throw divine energy that deals spirit damage. **Eldritch** **Lance**H Unleash eldritch mental damage on a target. |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/10` | 0.445217 | The power of the divine is steeped in faith,  the unseen, and belief in a power source from |

### Query 60
- Text: Summarize The power of the divine is steeped in faith,  the unseen, and belief in a power source from
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/10', 'PZO22001 Starfinder Player Core 294-329::/page/13/Text/22', 'PZO22001 Starfinder Player Core 294-329::/page/29/Text/22']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/10', 'PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/9', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/11']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/9` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/11` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/10` | 1.030988 | The power of the divine is steeped in faith,  the unseen, and belief in a power source from |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/22` | 0.522265 | **Divine Inspiration** Spiritual energy recovers a creature's  expended spell. |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/22` | 0.521492 | **CRISIS OF FAITH **[two-actions] **SPELL 3**  **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** divine  **Range **30 feet;** Targets** 1 creature  **Defense** Will  You assault the target's f |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/18` | 0.432620 | An instinctual connection to and faith in the  world, the cycle of day and night, the turning  of the seasons, and the natural selection of predator and  prey drive the primal tradition. Mystics conne |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/9` | 0.426416 | **Divine** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/32/SectionHeader/18` | 0.419106 | **DIVINE INSPIRATION **[two-actions] **SPELL 8**  **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** divine  **Range **touch;** Targets** 1 willing creature  You infuse a target with spiritual |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/12/Text/57` | 0.415482 | **Divine Immolation**H Call divine fire from the sky. |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/14/Text/51` | 0.414739 | **See the Unseen**H Reveal invisible creatures to your sight. |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/12/Text/12` | 0.414739 | **See the Unseen**H Reveal invisible creatures to your sight. |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/32/SectionHeader/55` | 0.411852 | **DOMINATE **[two-actions] **SPELL 6**  **UNCOMMON** **CONCENTRATE** **INCAPACITATION** **MANIPULATE** **MENTAL**  **Traditions** arcane, divine, occult  **Range **30 feet;** Targets** 1 creature  **D |

### Query 61
- Text: What is the rule about beyond the Universe. Mystics connected with the cosmic  forces of healing and shadows are divine spellcasters.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/11', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/3', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/15']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/11', 'PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/13', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/10']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/13` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/10` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/11` | 0.977953 | beyond the Universe. Mystics connected with the cosmic  forces of healing and shadows are divine spellcasters. |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/3` | 0.656783 | Even with the widespread presence of technology,  spellcasters can be found in every corner of the galaxy.  Some spellcasters draw magic from other realities, some  from their mystical connections to |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/15` | 0.638439 | systematic way. Witchwarpers touched by the Gap or  alternate timelines, as well as mystics who are psychically  linked to the Akashic Record, are occult spellcasters. |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/18` | 0.574392 | An instinctual connection to and faith in the  world, the cycle of day and night, the turning  of the seasons, and the natural selection of predator and  prey drive the primal tradition. Mystics conne |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/4` | 0.536983 | With special gestures and utterances, a spellcaster can  call forth mystic energies, warp the mind, protect themself  against danger, or even create something from nothing.  Each class has its own met |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/12` | 0.508607 | After Triune's Signal connected cultures across the  Universe, the peoples of the galaxy have learned more  than ever before about the Universe's composition  thanks to science and technology. As tech |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/7` | 0.503072 | Arcane spellcasters use logic and  rationality to categorize the magic inherent  in the world around them. Because of its far-reaching  approach, the arcane tradition has the broadest spell  list, tho |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/1` | 0.492925 | Whether it comes in the form of eldritch artifacts, otherworldly beings, or witchwarpers altering  reality with strange spells, magic brings fantasy and wonder to Starfinder. This chapter explains how |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/24` | 0.492892 | spells and precog warp spells, your mystic spells would  remain divine and the witchwarper spells occult. Similarly,  you need to use the attribute modifier determined by the  source of the focus spel |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/22` | 0.488790 | If you are a spellcaster, your focus spells are the same tradition  of spell as the class that gave you the focus spell. A mystic's |

### Query 62
- Text: Summarize **Occult**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/13', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/14', 'PZO22001 Starfinder Player Core 294-329::/page/31/SectionHeader/28']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/13', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/14', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/11']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/14` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/11` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/13` | 0.941838 | **Occult** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/14` | 0.519033 | The practitioners of occult traditions seek  to understand the unexplainable, categorize  the bizarre, and otherwise access the ephemeral in a |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/31/SectionHeader/28` | 0.489473 | **DISGUISE MAGIC** **SPELL 1**  **CONCENTRATE** **ILLUSION** **MANIPULATE**  **Traditions** arcane, occult  **Cast** 1 minute  **Range **30 feet; **Targets** 1 item or spell effect  **Duration** until |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/10/Text/5` | 0.447060 | **Outcast's Curse** Curse a creature to be off-putting and abrasive. **Peaceful Bubble**U Opaque bubble prevents detection, dreams,  perception, and scrying. |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/15` | 0.446759 | systematic way. Witchwarpers touched by the Gap or  alternate timelines, as well as mystics who are psychically  linked to the Akashic Record, are occult spellcasters. |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/31/SectionHeader/19` | 0.429394 | **DISCHARGE **[two-actions] **SPELL 3**  **CONCENTRATE** **ELECTRICITY** **MANIPULATE**  **Traditions** arcane, primal  **Range **30 feet;** Targets** 1 creature or object with the tech  trait  **Defe |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/28/Text/11` | 0.419337 | **CONFUSION **[two-actions] **SPELL 4**  **CONCENTRATE** **EMOTION** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult **Range **30 feet;** Targets** 1 creature **Defense** Will; **Duration** 1 |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/29/SectionHeader/51` | 0.409515 | **DARKVISION **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, occult, primal  **Duration** 1 hour  You grant yourself supernatural sight in areas of darkness |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/51` | 0.405847 | **Read Aura**H Detect if an object is magical. |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/8/Text/19` | 0.405847 | **Read Aura**H Detect if an object is magical. |

### Query 63
- Text: What is the rule about The practitioners of occult traditions seek  to understand the unexplainable, categorize  the bizarre, and otherwise access the ephemeral in a?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/14']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/14', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/7', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/15']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/14', 'PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/13', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/15']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/13` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/15` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/14` | 0.978242 | The practitioners of occult traditions seek  to understand the unexplainable, categorize  the bizarre, and otherwise access the ephemeral in a |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/7` | 0.580221 | Arcane spellcasters use logic and  rationality to categorize the magic inherent  in the world around them. Because of its far-reaching  approach, the arcane tradition has the broadest spell  list, tho |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/15` | 0.552548 | systematic way. Witchwarpers touched by the Gap or  alternate timelines, as well as mystics who are psychically  linked to the Akashic Record, are occult spellcasters. |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/3` | 0.457729 | Your class determines which tradition of magic your spells use. In some cases, such as when a mystic gains spells from  their connection or when a witchwarper learns spells from their paradox, you mig |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/4` | 0.453388 | Some types of magic, such as that of most magic items, don't belong to any single tradition. These have the magical  trait instead of a tradition trait. |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/2` | 0.451164 | The grand variety of spells includes those in the following pages and far more. Taught at magical  academies, drawn from other worlds, bestowed by mystical connections, and granted by all manner of  u |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/2` | 0.447912 | Spellcasters cast spells from one of four different spell lists, each representing a different magical tradition: arcane,  divine, occult, and primal. |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/1` | 0.443893 | **MAGICAL TRADITIONS** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/18` | 0.436094 | If a creature engages with an illusion in a way that would  prove it's not what it seems, the creature might know that an  illusion is present, but it still can't ignore the illusion without  successf |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/21` | 0.432318 | **Tradition** This entry lists the magical traditions the spell  belongs to. Some feats or other abilities might add a  spell to your spell list even if you don't follow the listed  traditions. |

### Query 64
- Text: What is the rule about systematic way. Witchwarpers touched by the Gap or  alternate timelines, as well as mystics who are psychically  linked to the Akashic Record, are occult spellcasters.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/15']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/15', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/7', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/2']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/15', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/14', 'PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/17']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/14` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/17` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/15` | 0.940006 | systematic way. Witchwarpers touched by the Gap or  alternate timelines, as well as mystics who are psychically  linked to the Akashic Record, are occult spellcasters. |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/7` | 0.647910 | Arcane spellcasters use logic and  rationality to categorize the magic inherent  in the world around them. Because of its far-reaching  approach, the arcane tradition has the broadest spell  list, tho |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/2` | 0.592012 | Spellcasters cast spells from one of four different spell lists, each representing a different magical tradition: arcane,  divine, occult, and primal. |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/3` | 0.558316 | Your class determines which tradition of magic your spells use. In some cases, such as when a mystic gains spells from  their connection or when a witchwarper learns spells from their paradox, you mig |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/24` | 0.535762 | spells and precog warp spells, your mystic spells would  remain divine and the witchwarper spells occult. Similarly,  you need to use the attribute modifier determined by the  source of the focus spel |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/14` | 0.522830 | The practitioners of occult traditions seek  to understand the unexplainable, categorize  the bizarre, and otherwise access the ephemeral in a |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/22` | 0.516581 | If you are a spellcaster, your focus spells are the same tradition  of spell as the class that gave you the focus spell. A mystic's |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/11` | 0.516439 | beyond the Universe. Mystics connected with the cosmic  forces of healing and shadows are divine spellcasters. |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/18` | 0.508232 | An instinctual connection to and faith in the  world, the cycle of day and night, the turning  of the seasons, and the natural selection of predator and  prey drive the primal tradition. Mystics conne |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/19` | 0.498578 | are determined by their connection, and a witchwarper's are  determined by their paradox. |

### Query 65
- Text: Summarize **Primal**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/17']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/17', 'PZO22001 Starfinder Player Core 294-329::/page/16/SectionHeader/57', 'PZO22001 Starfinder Player Core 294-329::/page/17/SectionHeader/17']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/17', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/18', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/15']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/18` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/15` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/17` | 0.934700 | **Primal** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/16/SectionHeader/57` | 0.545838 | PRIMAL 1ST-RANK SPELLS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/17/SectionHeader/17` | 0.524619 | PRIMAL 2ND-RANK SPELLS |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/18/SectionHeader/64` | 0.463515 | PRIMAL 10TH-RANK SPELLS |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/17/SectionHeader/71` | 0.456888 | PRIMAL 4TH-RANK SPELLS |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/17/SectionHeader/49` | 0.455157 | PRIMAL 3RD-RANK SPELLS |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/18/SectionHeader/7` | 0.446420 | PRIMAL 5TH-RANK SPELLS |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/18/SectionHeader/24` | 0.443581 | PRIMAL 6TH-RANK SPELLS |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/18/SectionHeader/56` | 0.443297 | PRIMAL 9TH-RANK SPELLS |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/18/SectionHeader/34` | 0.428909 | PRIMAL 7TH-RANK SPELLS |

### Query 66
- Text: What is the rule about An instinctual connection to and faith in the  world, the cycle of day and night, the turning  of the seasons, and the natural selection of predator and  prey drive the primal tradition. Mystics connected to  the primordial elements and underlying rhythms of the  cosmos are primal spellcasters.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/18']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/18', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/11', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/3']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/18', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/19', 'PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/17']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/19` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/17` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/18` | 1.003244 | An instinctual connection to and faith in the  world, the cycle of day and night, the turning  of the seasons, and the natural selection of predator and  prey drive the primal tradition. Mystics conne |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/11` | 0.614251 | beyond the Universe. Mystics connected with the cosmic  forces of healing and shadows are divine spellcasters. |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/3` | 0.602282 | Your class determines which tradition of magic your spells use. In some cases, such as when a mystic gains spells from  their connection or when a witchwarper learns spells from their paradox, you mig |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/2` | 0.552141 | Spellcasters cast spells from one of four different spell lists, each representing a different magical tradition: arcane,  divine, occult, and primal. |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/15` | 0.543382 | systematic way. Witchwarpers touched by the Gap or  alternate timelines, as well as mystics who are psychically  linked to the Akashic Record, are occult spellcasters. |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/21` | 0.508926 | **Tradition** This entry lists the magical traditions the spell  belongs to. Some feats or other abilities might add a  spell to your spell list even if you don't follow the listed  traditions. |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/7` | 0.493037 | Arcane spellcasters use logic and  rationality to categorize the magic inherent  in the world around them. Because of its far-reaching  approach, the arcane tradition has the broadest spell  list, tho |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/3` | 0.476555 | Even with the widespread presence of technology,  spellcasters can be found in every corner of the galaxy.  Some spellcasters draw magic from other realities, some  from their mystical connections to |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/22` | 0.471913 | If you are a spellcaster, your focus spells are the same tradition  of spell as the class that gave you the focus spell. A mystic's |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/19` | 0.471877 | are determined by their connection, and a witchwarper's are  determined by their paradox. |

### Query 67
- Text: Summarize are determined by their connection, and a witchwarper's are  determined by their paradox.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/19']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/19', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/3', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/15']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/19', 'PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/20', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/18']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/20` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/18` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/19` | 0.979823 | are determined by their connection, and a witchwarper's are  determined by their paradox. |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/3` | 0.544516 | Your class determines which tradition of magic your spells use. In some cases, such as when a mystic gains spells from  their connection or when a witchwarper learns spells from their paradox, you mig |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/15` | 0.530582 | systematic way. Witchwarpers touched by the Gap or  alternate timelines, as well as mystics who are psychically  linked to the Akashic Record, are occult spellcasters. |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/20` | 0.471268 | You spend 10 minutes performing deeds to restore your  magical connection. This restores 1 Focus Point to your focus  pool. The deeds you need to perform are specified in the class  or ability that gi |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/24` | 0.464225 | spells and precog warp spells, your mystic spells would  remain divine and the witchwarper spells occult. Similarly,  you need to use the attribute modifier determined by the  source of the focus spel |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/7` | 0.452202 | Arcane spellcasters use logic and  rationality to categorize the magic inherent  in the world around them. Because of its far-reaching  approach, the arcane tradition has the broadest spell  list, tho |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/44` | 0.422039 | **Status**H Keep track of a willing creature's location and well-being. **Summon Elemental**H Conjure an elemental to fight on your  behalf. |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/69` | 0.418162 | **Spirit Link**H Continually transfer your health to someone else. **Summon Undead**H Conjure an undead to fight on your behalf. |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/18` | 0.405500 | An instinctual connection to and faith in the  world, the cycle of day and night, the turning  of the seasons, and the natural selection of predator and  prey drive the primal tradition. Mystics conne |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/22` | 0.403013 | If you are a spellcaster, your focus spells are the same tradition  of spell as the class that gave you the focus spell. A mystic's |

### Query 68
- Text: What is the rule about NON-SPELLCASTERS WITH  FOCUS SPELLS?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/20']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/20', 'PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/21', 'PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/12']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/20', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/21', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/19']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/21` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/19` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/20` | 0.948632 | NON-SPELLCASTERS WITH  FOCUS SPELLS |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/21` | 0.855122 | SPELLCASTERS WITH FOCUS  SPELLS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/12` | 0.714323 | FOCUS SPELLS |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/21` | 0.528358 | If you get focus spells from a class or other source that  doesn't grant spellcasting ability, the ability that gives you  focus spells also provides your proficiency for your spell  attack modifier a |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0` | 0.493573 | CHAPTER 7: SPELLS |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/2` | 0.492723 | CASTING SPELLS |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/22` | 0.485429 | If you are a spellcaster, your focus spells are the same tradition  of spell as the class that gave you the focus spell. A mystic's |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/7/SectionHeader/3` | 0.483130 | IDENTIFYING SPELLS |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/86` | 0.479974 | **Focus Spells** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/36` | 0.479974 | **Focus Spells** |

### Query 69
- Text: Summarize FOCUS POINTS FROM MULTIPLE  SOURCES
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/22']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/22', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/23', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/15']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/22', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/21', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/23']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/21` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/23` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/22` | 1.015229 | FOCUS POINTS FROM MULTIPLE  SOURCES |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/23` | 0.665470 | It's possible, especially through archetypes, to gain focus  spells from more than one source. If this happens, you  have just one focus pool, counting all your focus spells to  determine the points i |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/15` | 0.514168 | Casting any of your focus spells costs you 1 Focus Point.  You automatically gain a focus pool the first time you gain an  ability that gives you a focus spell. The maximum number of  points in your p |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/36` | 0.466362 | **Focus Spells** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/39` | 0.466362 | **Focus Spells** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/77` | 0.466362 | **Focus Spells** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/89` | 0.466362 | **Focus Spells** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/64` | 0.466362 | **Focus Spells** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/68` | 0.466362 | **Focus Spells** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/29` | 0.466362 | **Focus Spells** |

### Query 70
- Text: Summarize **INTRODUCTION**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/30']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/30', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/20', 'PZO22001 Starfinder Player Core 294-329::/page/7/Text/28']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/30', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/28', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/31']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/28` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/31` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/30` | 0.880541 | **INTRODUCTION** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/20` | 0.880541 | **INTRODUCTION** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/28` | 0.880541 | **INTRODUCTION** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/68` | 0.838541 | **INTRODUCTION** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/77` | 0.838541 | **INTRODUCTION** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/18` | 0.838541 | **INTRODUCTION** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/55` | 0.838541 | **INTRODUCTION** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/74` | 0.838541 | **INTRODUCTION** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/80` | 0.838541 | **INTRODUCTION** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/23/Text/38` | 0.838541 | **INTRODUCTION** |

### Query 71
- Text: Summarize **CLASSES**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/32']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/35/Text/64', 'PZO22001 Starfinder Player Core 294-329::/page/27/Text/64', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/32']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/32', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/33', 'PZO22001 Starfinder Player Core 294-329::/page/23/Text/40', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/22', 'PZO22001 Starfinder Player Core 294-329::/page/9/Text/82', 'PZO22001 Starfinder Player Core 294-329::/page/29/Text/61', 'PZO22001 Starfinder Player Core 294-329::/page/27/Text/64', 'PZO22001 Starfinder Player Core 294-329::/page/15/Text/76', 'PZO22001 Starfinder Player Core 294-329::/page/33/Text/57', 'PZO22001 Starfinder Player Core 294-329::/page/19/Text/55', 'PZO22001 Starfinder Player Core 294-329::/page/35/Text/64', 'PZO22001 Starfinder Player Core 294-329::/page/31/Text/56']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/33` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/23/Text/40` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/5/Text/22` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/9/Text/82` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/29/Text/61` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/27/Text/64` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/15/Text/76` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/33/Text/57` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/19/Text/55` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/35/Text/64` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/31/Text/56` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/64` | 0.940061 | **CLASSES** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/27/Text/64` | 0.940061 | **CLASSES** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/32` | 0.940061 | **CLASSES** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/82` | 0.910061 | **CLASSES** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/57` | 0.910061 | **CLASSES** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/70` | 0.910061 | **CLASSES** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/76` | 0.910061 | **CLASSES** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/30` | 0.910061 | **CLASSES** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/22` | 0.910061 | **CLASSES** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/23/Text/40` | 0.910061 | **CLASSES** |

### Query 72
- Text: Summarize **EQUIPMENT**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/35']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/35', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/25', 'PZO22001 Starfinder Player Core 294-329::/page/9/Text/85']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/35', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/36', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/34']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/36` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/34` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/35` | 0.944726 | **EQUIPMENT** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/25` | 0.944726 | **EQUIPMENT** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/85` | 0.944726 | **EQUIPMENT** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/60` | 0.902726 | **EQUIPMENT** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/82` | 0.902726 | **EQUIPMENT** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/23` | 0.902726 | **EQUIPMENT** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/59` | 0.902726 | **EQUIPMENT** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/85` | 0.902726 | **EQUIPMENT** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/58` | 0.902726 | **EQUIPMENT** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/79` | 0.902726 | **EQUIPMENT** |

### Query 73
- Text: Summarize **Rituals**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/40']
- Expected found: `True`
- Expected rank: `8`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/17/Text/90', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/30', 'PZO22001 Starfinder Player Core 294-329::/page/31/Text/64']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/40', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/39', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/41']
- Expanded expected found: `True`
- Expanded expected rank: `8`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/39` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/41` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/90` | 0.971114 | **Rituals** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/30` | 0.971114 | **Rituals** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/64` | 0.971114 | **Rituals** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/23/Text/47` | 0.929114 | **Rituals** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/28` | 0.929114 | **Rituals** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/65` | 0.929113 | **Rituals** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/84` | 0.929113 | **Rituals** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/40` | 0.929113 | **Rituals** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/78` | 0.929113 | **Rituals** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/37` | 0.929113 | **Rituals** |

### Query 74
- Text: Summarize **PLAYING THE ** **GAME**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/41']
- Expected found: `True`
- Expected rank: `14`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/27/Text/73', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/31', 'PZO22001 Starfinder Player Core 294-329::/page/7/Text/38']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/41', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/42', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/40']
- Expanded expected found: `True`
- Expanded expected rank: `14`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/42` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/40` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/27/Text/73` | 0.965000 | **PLAYING THE ** **GAME** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/38` | 0.965000 | **PLAYING THE ** **GAME** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/31` | 0.965000 | **PLAYING THE ** **GAME** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/79` | 0.923000 | **PLAYING THE ** **GAME** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/29` | 0.923000 | **PLAYING THE ** **GAME** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/88` | 0.923000 | **PLAYING THE ** **GAME** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/91` | 0.923000 | **PLAYING THE ** **GAME** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/64` | 0.923000 | **PLAYING THE ** **GAME** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/70` | 0.923000 | **PLAYING THE ** **GAME** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/91` | 0.923000 | **PLAYING THE ** **GAME** |

### Query 75
- Text: Summarize **CONDITIONS ** **APPENDIX**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/42']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/42', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/32', 'PZO22001 Starfinder Player Core 294-329::/page/15/Text/86']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/42', 'PZO22001 Starfinder Player Core 294-329::/page/29/Text/71', 'PZO22001 Starfinder Player Core 294-329::/page/13/Text/80', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/43', 'PZO22001 Starfinder Player Core 294-329::/page/23/Text/49', 'PZO22001 Starfinder Player Core 294-329::/page/7/Text/39', 'PZO22001 Starfinder Player Core 294-329::/page/15/Text/86', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/41', 'PZO22001 Starfinder Player Core 294-329::/page/11/Text/89', 'PZO22001 Starfinder Player Core 294-329::/page/9/Text/92', 'PZO22001 Starfinder Player Core 294-329::/page/27/Text/74', 'PZO22001 Starfinder Player Core 294-329::/page/33/Text/67']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/29/Text/71` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/13/Text/80` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/43` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/23/Text/49` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/7/Text/39` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/15/Text/86` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/41` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/11/Text/89` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/9/Text/92` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/27/Text/74` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/33/Text/67` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/42` | 0.983499 | **CONDITIONS ** **APPENDIX** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/32` | 0.983499 | **CONDITIONS ** **APPENDIX** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/86` | 0.983499 | **CONDITIONS ** **APPENDIX** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/80` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/92` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/39` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/89` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/23/Text/49` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/65` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/92` | 0.953498 | **CONDITIONS ** **APPENDIX** |

### Query 76
- Text: Summarize **GLOSSARY & ** **INDEX**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/43']
- Expected found: `True`
- Expected rank: `4`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/35/Text/76', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/32', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/33']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/43', 'PZO22001 Starfinder Player Core 294-329::/page/4/Text/1', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/42']
- Expanded expected found: `True`
- Expanded expected rank: `4`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/4/Text/1` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/42` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/76` | 0.993465 | **GLOSSARY & ** **INDEX** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/32` | 0.993465 | **GLOSSARY & ** **INDEX** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/33` | 0.993465 | **GLOSSARY & ** **INDEX** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/43` | 0.951465 | **GLOSSARY & ** **INDEX** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/90` | 0.951465 | **GLOSSARY & ** **INDEX** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/81` | 0.951465 | **GLOSSARY & ** **INDEX** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/93` | 0.951465 | **GLOSSARY & ** **INDEX** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/23/Text/50` | 0.951465 | **GLOSSARY & ** **INDEX** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/67` | 0.951465 | **GLOSSARY & ** **INDEX** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/66` | 0.951465 | **GLOSSARY & ** **INDEX** |

### Query 77
- Text: Summarize COSTS AND LOCI
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/6', 'PZO22001 Starfinder Player Core 294-329::/page/4/Text/8', 'PZO22001 Starfinder Player Core 294-329::/page/4/Text/7']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/6', 'PZO22001 Starfinder Player Core 294-329::/page/4/Text/7', 'PZO22001 Starfinder Player Core 294-329::/page/4/Text/5']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/4/Text/7` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/4/Text/5` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/6` | 0.980991 | COSTS AND LOCI |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/8` | 0.490833 | A **locus** is an object that funnels or directs the magical  energy of the spell but is not consumed in its casting. As part  of Casting the Spell, you retrieve the locus (if necessary, and  if you h |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/7` | 0.480629 | Some spells require you to pay a cost or provide a locus. If the  spell lists a **cost**, you must have the listed money, valuable  materials, or other resources to cast the spell (such as gems or  ma |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/22` | 0.311188 | **Cast** Spells that take longer than a single turn to cast include  this entry to list the time required, such as "1 minute." If  the spell has a cost, locus, requirements, or a trigger, that  inform |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/12/Text/34` | 0.290671 | **Locate**H, U Learn the direction to an object. |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/59` | 0.290671 | **Locate**H, U Learn the direction to an object. |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/3` | 0.262026 | **Darkness and Light** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/81` | 0.261209 | **ANCESTRIES & ** **BACKGROUNDS** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/54` | 0.261209 | **ANCESTRIES & ** **BACKGROUNDS** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/31` | 0.261209 | **ANCESTRIES & ** **BACKGROUNDS** |

### Query 78
- Text: Summarize LONG CASTING TIMES
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/9', 'PZO22001 Starfinder Player Core 294-329::/page/7/Text/22', 'PZO22001 Starfinder Player Core 294-329::/page/4/Text/10']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/9', 'PZO22001 Starfinder Player Core 294-329::/page/4/Text/8', 'PZO22001 Starfinder Player Core 294-329::/page/4/Text/10']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/4/Text/8` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/4/Text/10` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/9` | 0.987460 | LONG CASTING TIMES |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/22` | 0.527075 | **Cast** Spells that take longer than a single turn to cast include  this entry to list the time required, such as "1 minute." If  the spell has a cost, locus, requirements, or a trigger, that  inform |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/10` | 0.503703 | Some spells take minutes or hours to cast. You can't use  other actions or reactions while casting such a spell, |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/3` | 0.442115 | The casting of a spell can range from a simple word of magical  might that creates a fleeting effect to a complex process  taking hours to cast and producing a long-term impact.  Casting a spell requi |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/2` | 0.420595 | CASTING SPELLS |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/15` | 0.379742 | LONG DURATIONS |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/11` | 0.345645 | though at the GM's discretion, you might be able to speak  a few sentences. As with other activities that take a long  time, these spells have the exploration trait, and you can't  cast them in an enc |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/6/Text/16` | 0.334767 | If a spell's duration says it lasts until your next daily  preparations, on the next day you can refrain from preparing  a new spell in that spell's slot. (If you are a spontaneous caster,  you can in |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/6/Text/12` | 0.318404 | If a spell's caster dies or is incapacitated during the spell's  duration, the spell remains in effect until its duration ends,  using the caster's initiative order. |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/11` | 0.312148 | **SPELLCASTING IN STARFINDER** |

### Query 79
- Text: Summarize RANGES, AREAS, AND  TARGETS
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/14']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/14', 'PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/20', 'PZO22001 Starfinder Player Core 294-329::/page/7/Text/23']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/14', 'PZO22001 Starfinder Player Core 294-329::/page/4/Text/15', 'PZO22001 Starfinder Player Core 294-329::/page/4/Text/13']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/4/Text/15` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/4/Text/13` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/14` | 0.989453 | RANGES, AREAS, AND  TARGETS |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/20` | 0.635018 | TARGETS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/23` | 0.628653 | **Range, Area, and Targets** This entry lists the range of the  spell, the area it affects, and the targets it can affect, if  any. If none of these entries are present, the spell affects  only the ca |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/16` | 0.528309 | TOUCH RANGE |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/18` | 0.513607 | AREAS |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/15` | 0.503060 | Spells with a range can affect targets, create areas, or make  things appear only within that range. Most spell ranges are  measured in feet, though some can stretch over miles, reach  anywhere on the |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/16/Text/38` | 0.455388 | **Analyze** **Target**H Gather data about a target's basic physiology. **Caustic Blast**H Fling a glob of acid that splashes a small area. |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/8/Text/8` | 0.455388 | **Analyze** **Target**H Gather data about a target's basic physiology. **Caustic Blast**H Fling a glob of acid that splashes a small area. |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/42` | 0.453372 | **Analyze** **Target**H Gather data about a target's basic physiology. **Daze**H Cloud a creature's mind and possibly stun it. |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/29` | 0.453372 | **Analyze** **Target**H Gather data about a target's basic physiology. **Daze**H Cloud a creature's mind and possibly stun it. |

### Query 80
- Text: Summarize TOUCH RANGE
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/16']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/16', 'PZO22001 Starfinder Player Core 294-329::/page/4/Text/17', 'PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/14']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/16', 'PZO22001 Starfinder Player Core 294-329::/page/4/Text/15', 'PZO22001 Starfinder Player Core 294-329::/page/4/Text/17']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/4/Text/15` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/4/Text/17` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/16` | 0.977209 | TOUCH RANGE |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/17` | 0.585659 | A spell with a touch range requires you to physically touch  the target. You use your unarmed reach to determine  whether you can touch the creature. You can usually touch  them automatically, though |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/14` | 0.548030 | RANGES, AREAS, AND  TARGETS |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/15` | 0.399553 | Spells with a range can affect targets, create areas, or make  things appear only within that range. Most spell ranges are  measured in feet, though some can stretch over miles, reach  anywhere on the |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/28` | 0.384840 | **ADHERE **[one-action] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult, primal  **Range **touch; **Targets** 1 held or unattended object or a 5-footsquare sur |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/23` | 0.384587 | **Range, Area, and Targets** This entry lists the range of the  spell, the area it affects, and the targets it can affect, if  any. If none of these entries are present, the spell affects  only the ca |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/30/Text/1` | 0.383528 | **Heightened (5th)** The spell's range is touch and it targets  1 willing creature. The duration is until your next daily  preparations. |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/14/Text/54` | 0.362746 | **Skim** **Data** Touch an object to get the gist of the data in it. |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/35` | 0.362746 | **Skim** **Data** Touch an object to get the gist of the data in it. |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/35/SectionHeader/52` | 0.362589 | **ENHANCE WEAPON **[two-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, occult, primal  **Range **touch; **Targets** 1 weapon that is unattended or  wielded by a w |

### Query 81
- Text: Summarize AREAS
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/18']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/18', 'PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/14', 'PZO22001 Starfinder Player Core 294-329::/page/4/Text/19']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/18', 'PZO22001 Starfinder Player Core 294-329::/page/4/Text/19', 'PZO22001 Starfinder Player Core 294-329::/page/4/Text/17']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/4/Text/19` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/4/Text/17` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/18` | 0.891151 | AREAS |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/14` | 0.595143 | RANGES, AREAS, AND  TARGETS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/19` | 0.450945 | Sometimes a spell has an area, which can be a burst, cone,  emanation, or line (pages 420–421). If the spell originates  from your position, the spell has only an area; if you can  cause the spell's a |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/39` | 0.398253 | **Scan** **Environment**H Scan nearby terrain and get an inherent  understanding of it. |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/16/Text/50` | 0.398253 | **Scan** **Environment**H Scan nearby terrain and get an inherent  understanding of it. |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/23` | 0.363227 | **Range, Area, and Targets** This entry lists the range of the  spell, the area it affects, and the targets it can affect, if  any. If none of these entries are present, the spell affects  only the ca |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/71` | 0.343100 | **INDEX** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/27/Text/78` | 0.343100 | **INDEX** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/16/Text/46` | 0.342659 | **Measure**H You get measurements of creatures you can observe  in the area. |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/8/Text/17` | 0.342659 | **Measure**H You get measurements of creatures you can  observe in the area. |

### Query 82
- Text: Summarize TARGETS
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/20']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/20', 'PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/14', 'PZO22001 Starfinder Player Core 294-329::/page/16/Text/15']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/20', 'PZO22001 Starfinder Player Core 294-329::/page/4/Text/19', 'PZO22001 Starfinder Player Core 294-329::/page/4/Text/21']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/4/Text/19` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/4/Text/21` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/20` | 0.902316 | TARGETS |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/14` | 0.691995 | RANGES, AREAS, AND  TARGETS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/16/Text/15` | 0.521294 | **True Target** Make multiple attacks against a creature  especially accurate. |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/10/Text/68` | 0.479294 | **True Target** Make multiple attacks against a creature  especially accurate. |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/41` | 0.442727 | **ANALYZE TARGET **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **DETECTION** **MANIPULATE**  **Traditions** arcane, divine, occult, primal **Range **30 feet; **Targets** 1 creature  **Dur |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/16/Text/60` | 0.438973 | **Ant Haul** Target can carry more. |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/8/Text/30` | 0.438973 | **Ant Haul** Target can carry more. |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/12/Text/45` | 0.433178 | **Genetic** **Regeneration**H The target regenerates. |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/77` | 0.433178 | **Genetic** **Regeneration**H The target regenerates. |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/29` | 0.431608 | **Analyze** **Target**H Gather data about a target's basic physiology. **Daze**H Cloud a creature's mind and possibly stun it. |

### Query 83
- Text: Summarize **Darkness and Light**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/3']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/3', 'PZO22001 Starfinder Player Core 294-329::/page/9/Text/10', 'PZO22001 Starfinder Player Core 294-329::/page/17/Text/25']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/3', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/4', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/2']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/5/Text/4` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/5/Text/2` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/3` | 0.972844 | **Darkness and Light** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/10` | 0.653476 | **Darkness**H Suppress all light in an area. |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/25` | 0.653476 | **Darkness**H Suppress all light in an area. |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/12/Text/1` | 0.611476 | **Darkness**H Suppress all light in an area. |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/14/Text/31` | 0.611476 | **Darkness**H Suppress all light in an area. |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/29/SectionHeader/44` | 0.552221 | **DARKNESS **[three-actions] **SPELL 2**  **CONCENTRATE** **DARKNESS** **MANIPULATE**  **Traditions** arcane, divine, occult, primal **Range **120 feet;** Area** 20-foot burst  **Duration** 1 minute |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/11` | 0.545829 | **Darkvision**H See in the dark. |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/26` | 0.545829 | **Darkvision**H See in the dark. |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/14/Text/32` | 0.533829 | **Darkvision**H See in the dark. |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/12/Text/2` | 0.533829 | **Darkvision**H See in the dark. |

### Query 84
- Text: Summarize **Minion**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/5', 'PZO22001 Starfinder Player Core 294-329::/page/14/Text/17', 'PZO22001 Starfinder Player Core 294-329::/page/8/Text/57']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/5', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/6', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/4']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/5/Text/6` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/5/Text/4` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/5` | 0.951904 | **Minion** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/14/Text/17` | 0.611073 | **Phantasmal Minion **Create a creature of force to perform  minor tasks. |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/8/Text/57` | 0.611073 | **Phantasmal Minion **Create a creature of force to perform  minor tasks. |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/6` | 0.575828 | Minions are creatures that directly serve another creature.  Your minion acts on your turn in combat, once per turn, when  you spend an action to issue it commands. For a companion,  you Command it; f |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/7` | 0.525946 | A minion has only 2 actions and 0 reactions per turn,  though certain conditions (such as slowed or quickened)  or abilities might give them additional actions or a reaction.  Alterations to a minion' |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/13` | 0.423224 | **BIND UNDEAD **[two-actions] **SPELL 3**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, occult  **Range **30 feet; **Targets** 1 mindless undead creature with a  level no greater tha |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/9` | 0.411029 | A creature called by a spell or effect gains the summoned  trait. A summoned creature can't summon other creatures,  create things of value, or cast spells that require a cost. It  has the minion trai |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/40` | 0.388629 | **Shatter**H Shatter an object with a high-frequency sonic attack. **Shrink**H Reduce a willing creature to Tiny size. |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/34` | 0.384461 | **Shrink**H Reduce a willing creature to Tiny size. |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/8` | 0.361284 | **Summoned** |

### Query 85
- Text: Summarize **Summoned**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/8']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/8', 'PZO22001 Starfinder Player Core 294-329::/page/8/Text/62', 'PZO22001 Starfinder Player Core 294-329::/page/28/Text/1']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/8', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/9', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/7']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/5/Text/9` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/5/Text/7` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/8` | 0.893372 | **Summoned** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/8/Text/62` | 0.521000 | **Summon Construct**H Conjure a construct to fight on your behalf. **Summon** **Robot**H Summon a robot to fight for you. |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/28/Text/1` | 0.489149 | **Heightened (6th)** Add doomed to the list of conditions. **Heightened (8th)** Add stunned to the list of conditions. |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/8/Text/63` | 0.445092 | **Summon Undead**H Conjure an undead to fight on your behalf. **Supercharge** **Weapon**H Increase the damage done by the next  attack of a weapon. |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/8/Text/61` | 0.438512 | **Summon Animal**H Conjure an animal to fight for you. |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/44` | 0.433752 | **Status**H Keep track of a willing creature's location and well-being. **Summon Elemental**H Conjure an elemental to fight on your  behalf. |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/37` | 0.429480 | **Summon Elemental**H Conjure an elemental to fight on your  behalf. |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/11` | 0.426512 | **Summon Animal**H Conjure an animal to fight for you. |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/12/Text/65` | 0.422825 | **Summon Monitor**H Conjure a planar monitor to fight on your  behalf. |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/12/Text/64` | 0.422149 | **Summon Fiend**H Conjure a fiend to fight on your behalf. |

### Query 86
- Text: Summarize **Morph**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/11', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/12', 'PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/13']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/11', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/12', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/10']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/5/Text/12` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/5/Text/10` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/11` | 0.970082 | **Morph** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/12` | 0.543659 | Spells that slightly alter a creature's form have the morph trait.  Any Strikes specifically granted by a magical morph effect also  gain the magical trait. You can be affected by multiple morph  spel |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/13` | 0.498794 | **Polymorph** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/33` | 0.448391 | **Humanoid Form**H Take the shape of a humanoid. |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/22` | 0.448391 | **Humanoid Form**H Take the shape of a humanoid. |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/14/Text/41` | 0.448391 | **Humanoid Form**H Take the shape of a humanoid. |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/18/Text/62` | 0.426461 | **Metamorphosis** Fluidly change between different forms. |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/17` | 0.426461 | **Metamorphosis** Fluidly change between different forms. |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/39` | 0.403119 | **Shape Wood **Transform unworked wood into a shape of your  choice. |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/33` | 0.396316 | **See the Unseen**H Reveal invisible creatures to your sight. **Shape Wood** Transform unworked wood into a shape of your  choice. |

### Query 87
- Text: Summarize **Polymorph**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/13', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/14', 'PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/11']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/13', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/12', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/14']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/5/Text/12` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/5/Text/14` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/13` | 0.998193 | **Polymorph** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/14` | 0.563985 | These effects completely transform the target into a new  form. A target can't be under the effect of more than  one polymorph at a time. If it comes under the effect of  another, the second effect at |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/11` | 0.513959 | **Morph** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/15` | 0.475373 | If you take on a battle form with a polymorph spell, the  special statistics can be adjusted only by circumstance  bonuses, status bonuses, and penalties. Unless otherwise  noted, the battle form prev |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/12` | 0.459290 | Spells that slightly alter a creature's form have the morph trait.  Any Strikes specifically granted by a magical morph effect also  gain the magical trait. You can be affected by multiple morph  spel |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/29/SectionHeader/35` | 0.443185 | **CURSED METAMORPHOSIS **[two-actions] **SPELL 6**  **CONCENTRATE** **CURSE** **INCAPACITATION** **MANIPULATE** **POLYMORPH**  **Traditions** arcane, occult, primal **Range **30 feet;** Targets** 1 cr |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/3` | 0.405574 | **SPELLSHAPE** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/18/Text/62` | 0.400333 | **Metamorphosis** Fluidly change between different forms. |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/17` | 0.400333 | **Metamorphosis** Fluidly change between different forms. |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/34/SectionHeader/53` | 0.394814 | **ELEMENTAL FORM **[two-actions] **SPELL 5**  **CONCENTRATE** **MANIPULATE** **POLYMORPH**  **Traditions** arcane, primal  **Duration** 1 minute  You call upon the power of the planes to transform int |

### Query 88
- Text: Summarize **Illusions**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/16']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/16', 'PZO22001 Starfinder Player Core 294-329::/page/8/Text/49', 'PZO22001 Starfinder Player Core 294-329::/page/14/Text/10']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/16', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/17', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/15']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/5/Text/17` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/5/Text/15` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/16` | 0.972017 | **Illusions** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/8/Text/49` | 0.577655 | **Illusory Disguise**H Make yourself look like a different creature. **Illusory Object**H Form a convincing illusion of an object. |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/14/Text/10` | 0.571637 | **Illusory Object**H Form a convincing illusion of an object. |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/23` | 0.510529 | **Illusory Creature**H Form a convincing illusion of a creature. |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/14/Text/42` | 0.510529 | **Illusory Creature**H Form a convincing illusion of a creature. |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/10/Text/22` | 0.510166 | **Illusory Scene**H Create an imaginary scene containing  multiple creatures and objects. |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/47` | 0.510166 | **Illusory Scene**H Create an imaginary scene containing  multiple creatures and objects. |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/8/Text/11` | 0.477819 | **Figment** Create a simple auditory or visual illusion. |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/14/Text/9` | 0.452880 | **Illusory Disguise**H Make yourself look like a different creature. |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/17` | 0.450590 | Magic with the illusion trait creates false sensory stimuli.  Sometimes illusions allow creatures a chance to disbelieve  the spell, which lets the creature ignore the spell if it succeeds  at doing s |

### Query 89
- Text: Summarize If a creature engages with an illusion in a way that would  prove it's not what it seems, the creature might know that an  illusion is present, but it still can't ignore the illusion without  successfully disbelieving it. Disbelieving a visual illusion makes  it and those things it blocks seem hazy and indistinct, which  might block vision enough to leave the other side concealed.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/5/Text/18']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/5/Text/18', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/17', 'PZO22001 Starfinder Player Core 294-329::/page/7/Text/13']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/5/Text/18', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/17', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/20']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/5/Text/17` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/5/Text/20` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/18` | 1.042885 | If a creature engages with an illusion in a way that would  prove it's not what it seems, the creature might know that an  illusion is present, but it still can't ignore the illusion without  successf |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/17` | 0.750692 | Magic with the illusion trait creates false sensory stimuli.  Sometimes illusions allow creatures a chance to disbelieve  the spell, which lets the creature ignore the spell if it succeeds  at doing s |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/13` | 0.641056 | Disguises and illusions fool the spell as long as they  appear to match its parameters. For a spell to detect  something visually, the spell's origin point must have line of  sight. Darkness doesn't p |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/8/Text/49` | 0.559727 | **Illusory Disguise**H Make yourself look like a different creature. **Illusory Object**H Form a convincing illusion of an object. |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/14/Text/42` | 0.548678 | **Illusory Creature**H Form a convincing illusion of a creature. |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/23` | 0.548678 | **Illusory Creature**H Form a convincing illusion of a creature. |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/21` | 0.519594 | Some spells allow you to target a creature, an object, or  something more specific. The target must be within the  spell's range, and you must be able to see it (or otherwise  perceive it with a preci |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/14/Text/43` | 0.516165 | **Invisibility**H A creature can't be seen until it attacks. |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/26` | 0.516165 | **Invisibility**H A creature can't be seen until it attacks. |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/46` | 0.515582 | **Hallucination**H Cause a creature to believe one thing is  another, to notice something that isn't there, or to be  unable to detect something. |

### Query 90
- Text: Summarize **INTRODUCTION**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/5/Text/20']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/30', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/20', 'PZO22001 Starfinder Player Core 294-329::/page/7/Text/28']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/5/Text/20', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/18', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/21']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/5/Text/18` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/5/Text/21` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/30` | 0.880541 | **INTRODUCTION** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/20` | 0.880541 | **INTRODUCTION** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/28` | 0.880541 | **INTRODUCTION** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/68` | 0.838541 | **INTRODUCTION** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/77` | 0.838541 | **INTRODUCTION** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/18` | 0.838541 | **INTRODUCTION** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/55` | 0.838541 | **INTRODUCTION** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/74` | 0.838541 | **INTRODUCTION** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/80` | 0.838541 | **INTRODUCTION** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/23/Text/38` | 0.838541 | **INTRODUCTION** |

### Query 91
- Text: Summarize **CLASSES**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/5/Text/22']
- Expected found: `True`
- Expected rank: `9`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/35/Text/64', 'PZO22001 Starfinder Player Core 294-329::/page/27/Text/64', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/32']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/5/Text/22', 'PZO22001 Starfinder Player Core 294-329::/page/15/Text/76', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/32', 'PZO22001 Starfinder Player Core 294-329::/page/33/Text/57', 'PZO22001 Starfinder Player Core 294-329::/page/19/Text/55', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/23', 'PZO22001 Starfinder Player Core 294-329::/page/23/Text/40', 'PZO22001 Starfinder Player Core 294-329::/page/13/Text/70', 'PZO22001 Starfinder Player Core 294-329::/page/17/Text/82', 'PZO22001 Starfinder Player Core 294-329::/page/29/Text/61', 'PZO22001 Starfinder Player Core 294-329::/page/9/Text/82', 'PZO22001 Starfinder Player Core 294-329::/page/11/Text/79']
- Expanded expected found: `True`
- Expanded expected rank: `3`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/15/Text/76` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/32` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/33/Text/57` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/19/Text/55` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/5/Text/23` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/23/Text/40` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/13/Text/70` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/17/Text/82` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/29/Text/61` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/9/Text/82` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/11/Text/79` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/64` | 0.940061 | **CLASSES** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/27/Text/64` | 0.940061 | **CLASSES** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/32` | 0.940061 | **CLASSES** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/82` | 0.910061 | **CLASSES** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/57` | 0.910061 | **CLASSES** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/70` | 0.910061 | **CLASSES** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/76` | 0.910061 | **CLASSES** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/30` | 0.910061 | **CLASSES** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/22` | 0.910061 | **CLASSES** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/23/Text/40` | 0.910061 | **CLASSES** |

### Query 92
- Text: Summarize **EQUIPMENT**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/5/Text/25']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/35', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/25', 'PZO22001 Starfinder Player Core 294-329::/page/9/Text/85']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/5/Text/25', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/24', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/26']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/5/Text/24` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/5/Text/26` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/35` | 0.944726 | **EQUIPMENT** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/25` | 0.944726 | **EQUIPMENT** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/85` | 0.944726 | **EQUIPMENT** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/60` | 0.902726 | **EQUIPMENT** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/82` | 0.902726 | **EQUIPMENT** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/23` | 0.902726 | **EQUIPMENT** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/59` | 0.902726 | **EQUIPMENT** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/85` | 0.902726 | **EQUIPMENT** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/58` | 0.902726 | **EQUIPMENT** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/79` | 0.902726 | **EQUIPMENT** |

### Query 93
- Text: Summarize **Rituals**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/5/Text/30']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/17/Text/90', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/30', 'PZO22001 Starfinder Player Core 294-329::/page/31/Text/64']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/5/Text/30', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/29', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/31']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/5/Text/29` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/5/Text/31` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/90` | 0.971114 | **Rituals** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/30` | 0.971114 | **Rituals** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/64` | 0.971114 | **Rituals** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/23/Text/47` | 0.929114 | **Rituals** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/28` | 0.929114 | **Rituals** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/65` | 0.929113 | **Rituals** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/84` | 0.929113 | **Rituals** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/40` | 0.929113 | **Rituals** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/78` | 0.929113 | **Rituals** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/37` | 0.929113 | **Rituals** |

### Query 94
- Text: Summarize **PLAYING THE ** **GAME**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/5/Text/31']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/27/Text/73', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/31', 'PZO22001 Starfinder Player Core 294-329::/page/7/Text/38']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/5/Text/31', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/32', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/30']
- Expanded expected found: `True`
- Expanded expected rank: `3`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/5/Text/32` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/5/Text/30` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/27/Text/73` | 0.965000 | **PLAYING THE ** **GAME** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/38` | 0.965000 | **PLAYING THE ** **GAME** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/31` | 0.965000 | **PLAYING THE ** **GAME** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/79` | 0.923000 | **PLAYING THE ** **GAME** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/29` | 0.923000 | **PLAYING THE ** **GAME** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/88` | 0.923000 | **PLAYING THE ** **GAME** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/91` | 0.923000 | **PLAYING THE ** **GAME** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/64` | 0.923000 | **PLAYING THE ** **GAME** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/70` | 0.923000 | **PLAYING THE ** **GAME** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/91` | 0.923000 | **PLAYING THE ** **GAME** |

### Query 95
- Text: Summarize **CONDITIONS ** **APPENDIX**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/5/Text/32']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/42', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/32', 'PZO22001 Starfinder Player Core 294-329::/page/15/Text/86']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/5/Text/32', 'PZO22001 Starfinder Player Core 294-329::/page/19/Text/65', 'PZO22001 Starfinder Player Core 294-329::/page/15/Text/86', 'PZO22001 Starfinder Player Core 294-329::/page/29/Text/71', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/31', 'PZO22001 Starfinder Player Core 294-329::/page/17/Text/92', 'PZO22001 Starfinder Player Core 294-329::/page/13/Text/80', 'PZO22001 Starfinder Player Core 294-329::/page/31/Text/66', 'PZO22001 Starfinder Player Core 294-329::/page/27/Text/74', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/42', 'PZO22001 Starfinder Player Core 294-329::/page/33/Text/67', 'PZO22001 Starfinder Player Core 294-329::/page/11/Text/89']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/19/Text/65` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/15/Text/86` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/29/Text/71` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/5/Text/31` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/17/Text/92` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/13/Text/80` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/31/Text/66` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/27/Text/74` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/42` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/33/Text/67` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/11/Text/89` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/42` | 0.983499 | **CONDITIONS ** **APPENDIX** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/32` | 0.983499 | **CONDITIONS ** **APPENDIX** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/86` | 0.983499 | **CONDITIONS ** **APPENDIX** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/80` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/92` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/39` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/89` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/23/Text/49` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/65` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/92` | 0.953498 | **CONDITIONS ** **APPENDIX** |

### Query 96
- Text: Summarize **GLOSSARY & ** **INDEX**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/5/Text/33']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/35/Text/76', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/32', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/33']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/5/Text/33', 'PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/1', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/32']
- Expanded expected found: `True`
- Expanded expected rank: `3`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/1` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/5/Text/32` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/76` | 0.993465 | **GLOSSARY & ** **INDEX** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/32` | 0.993465 | **GLOSSARY & ** **INDEX** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/33` | 0.993465 | **GLOSSARY & ** **INDEX** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/43` | 0.951465 | **GLOSSARY & ** **INDEX** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/90` | 0.951465 | **GLOSSARY & ** **INDEX** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/81` | 0.951465 | **GLOSSARY & ** **INDEX** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/93` | 0.951465 | **GLOSSARY & ** **INDEX** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/23/Text/50` | 0.951465 | **GLOSSARY & ** **INDEX** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/67` | 0.951465 | **GLOSSARY & ** **INDEX** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/66` | 0.951465 | **GLOSSARY & ** **INDEX** |

### Query 97
- Text: Summarize LINE OF EFFECT
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/7', 'PZO22001 Starfinder Player Core 294-329::/page/6/Text/8', 'PZO22001 Starfinder Player Core 294-329::/page/7/Text/25']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/7', 'PZO22001 Starfinder Player Core 294-329::/page/6/Text/8', 'PZO22001 Starfinder Player Core 294-329::/page/6/Text/6']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/6/Text/8` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/6/Text/6` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/7` | 0.981036 | LINE OF EFFECT |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/6/Text/8` | 0.515224 | You usually need an unobstructed path to the target of  a spell, the origin point of an area, or the place where you  create something with a spell. More information on line of  effect can be found on |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/25` | 0.479329 | A horizontal line follows defense and duration, and the  effects of the spell are described after this line. This section  might also detail the possible results of a saving throw:  critical success, |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/23` | 0.370005 | **Range, Area, and Targets** This entry lists the range of the  spell, the area it affects, and the targets it can affect, if  any. If none of these entries are present, the spell affects  only the ca |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/35/SectionHeader/32` | 0.358584 | **ENFEEBLE **[two-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, occult  **Range **30 feet;** Targets** 1 creature  **Defense** Fortitude; **Duration** varies  Yo |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/30/Text/8` | 0.357977 | **DEAFNESS **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, occult, primal **Range **30 feet;** Targets** 1 creature  **Defense** Fortitude  The target loses |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/26` | 0.354290 | **Heightened** (rank) If the spell has special effects when  heightened (page 295), those effects appear at the end  of the stat block. |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/34/SectionHeader/38` | 0.350889 | **ELECTRIC ARC **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **ELECTRICITY** **MANIPULATE**  **Traditions** arcane, primal  **Range **30 feet; **Targets** 1 or 2 creatures  **Defense** ba |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/44` | 0.345143 | **CHAIN LIGHTNING **[two-actions] **SPELL 6**  **CONCENTRATE** **ELECTRICITY** **MANIPULATE**  **Traditions** arcane, primal  **Range **500 feet;** Targets** 1 creature, plus any number of  additional |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/36` | 0.344552 | **BLINDNESS **[two-actions] **SPELL 3**  **CONCENTRATE** **INCAPACITATION** **MANIPULATE**  **Traditions** arcane, divine, occult, primal  **Range **30 feet;** Targets** 1 creature  **Defense** Fortit |

### Query 98
- Text: Summarize DURATIONS
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/9', 'PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/15', 'PZO22001 Starfinder Player Core 294-329::/page/15/Text/84']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/9', 'PZO22001 Starfinder Player Core 294-329::/page/6/Text/8', 'PZO22001 Starfinder Player Core 294-329::/page/6/Text/10']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/6/Text/8` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/6/Text/10` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/9` | 0.955575 | DURATIONS |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/15` | 0.762010 | LONG DURATIONS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/84` | 0.411006 | **Rituals** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/65` | 0.369006 | **Rituals** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/78` | 0.369006 | **Rituals** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/87` | 0.369006 | **Rituals** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/63` | 0.369006 | **Rituals** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/90` | 0.369006 | **Rituals** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/27/Text/72` | 0.369006 | **Rituals** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/40` | 0.369006 | **Rituals** |

### Query 99
- Text: Summarize LONG DURATIONS
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/15']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/15', 'PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/9', 'PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/9']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/15', 'PZO22001 Starfinder Player Core 294-329::/page/6/Text/16', 'PZO22001 Starfinder Player Core 294-329::/page/6/Text/14']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/6/Text/16` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/6/Text/14` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/15` | 0.990267 | LONG DURATIONS |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/9` | 0.740634 | DURATIONS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/9` | 0.402992 | LONG CASTING TIMES |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/6/Text/14` | 0.363230 | If the spell's duration is "sustained," it lasts until the end of  your next turn unless you use the Sustain action (page 411)  on that turn to extend the duration of that spell. |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/6/Text/10` | 0.362155 | The duration of a spell is how long the spell effect lasts. Spells  that last for more than an instant have a Duration entry. A  spell might last until the start or end of a turn, for some  number of |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/24` | 0.323139 | **Defense and Duration** If a spell allows the target to attempt  a saving throw or use their AC to defend against it, the  type of defense appears here (see page 300 for details).  A Duration entry a |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/25` | 0.315375 | A horizontal line follows defense and duration, and the  effects of the spell are described after this line. This section  might also detail the possible results of a saving throw:  critical success, |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/32/SectionHeader/55` | 0.288249 | **DOMINATE **[two-actions] **SPELL 6**  **UNCOMMON** **CONCENTRATE** **INCAPACITATION** **MANIPULATE** **MENTAL**  **Traditions** arcane, divine, occult  **Range **30 feet;** Targets** 1 creature  **D |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/59` | 0.278530 | **Truespeech**H, U Let a creature understand and speak all languages. **Wave of Despair**H Drive creatures in an area to despair. |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/6/Text/16` | 0.275953 | If a spell's duration says it lasts until your next daily  preparations, on the next day you can refrain from preparing  a new spell in that spell's slot. (If you are a spontaneous caster,  you can in |

### Query 100
- Text: What does **ABSOLUTE ZERO **[two-actions] **SPELL 7** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/4', 'PZO22001 Starfinder Player Core 294-329::/page/7/Text/19', 'PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/4', 'PZO22001 Starfinder Player Core 294-329::/page/19/Text/2', 'PZO22001 Starfinder Player Core 294-329::/page/19/Text/11']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/19/Text/2` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/19/Text/11` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/4` | 0.611576 | **ABSOLUTE ZERO **[two-actions] **SPELL 7**  **COLD** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal  **Range **500 feet; **Area** 30-foot burst  **Defense** Fortitude  A swirling vorte |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/19` | 0.606223 | **SPELL NAME **[one-action] **SPELL (RANK)** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0` | 0.536207 | CHAPTER 7: SPELLS |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/36` | 0.480443 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/27/Text/68` | 0.480443 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/60` | 0.480443 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/83` | 0.480443 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/59` | 0.480443 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/80` | 0.480443 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/26` | 0.480443 | **SPELLS** |

### Query 101
- Text: What does **ACID GRIP **[two-actions] **SPELL 2** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/16']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/16', 'PZO22001 Starfinder Player Core 294-329::/page/7/Text/19', 'PZO22001 Starfinder Player Core 294-329::/page/17/Text/18']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/16', 'PZO22001 Starfinder Player Core 294-329::/page/19/Text/23', 'PZO22001 Starfinder Player Core 294-329::/page/19/Text/15']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/19/Text/23` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/19/Text/15` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/16` | 0.664102 | **ACID GRIP **[two-actions] **SPELL 2**  **ACID** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal  **Range **120 feet;** Targets** 1 creature  **Defense** Reflex  An ephemeral, taloned h |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/19` | 0.636205 | **SPELL NAME **[one-action] **SPELL (RANK)** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/18` | 0.579615 | **Acid Grip**H Move and harm foes with a hand of acid. |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/5` | 0.537615 | **Acid Grip**H Move and harm foes with a hand of acid. |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/61` | 0.532444 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/80` | 0.532444 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/68` | 0.532444 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/86` | 0.532444 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/65` | 0.532444 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/24` | 0.532444 | **SPELLS** |

### Query 102
- Text: What does **ADHERE **[one-action] **CANTRIP 1** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/28']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/28', 'PZO22001 Starfinder Player Core 294-329::/page/30/Text/2', 'PZO22001 Starfinder Player Core 294-329::/page/34/SectionHeader/38']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/28', 'PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/36', 'PZO22001 Starfinder Player Core 294-329::/page/19/Text/27']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/36` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/19/Text/27` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/28` | 0.693506 | **ADHERE **[one-action] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult, primal  **Range **touch; **Targets** 1 held or unattended object or a 5-footsquare sur |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/30/Text/2` | 0.520934 | **DAZE **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **MANIPULATE** **MENTAL** **NONLETHAL**  **Traditions** arcane, divine, occult **Range **60 feet; **Targets** 1 creature **Defense** W |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/34/SectionHeader/38` | 0.511561 | **ELECTRIC ARC **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **ELECTRICITY** **MANIPULATE**  **Traditions** arcane, primal  **Range **30 feet; **Targets** 1 or 2 creatures  **Defense** ba |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/41` | 0.459024 | **ANALYZE TARGET **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **DETECTION** **MANIPULATE**  **Traditions** arcane, divine, occult, primal **Range **30 feet; **Targets** 1 creature  **Dur |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/30/Text/40` | 0.457849 | **DETECT MAGIC **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **DETECTION** **MANIPULATE**  **Traditions** arcane, divine, occult, primal  **Area** 30-foot emanation  You send out a pulse |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/19` | 0.457142 | **CAUSTIC BLAST **[two-actions] **CANTRIP 1**  **ACID** **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal  **Range **30 feet; **Area** 5-foot burst  **Defense** basic Reflex  Y |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/32/SectionHeader/24` | 0.450363 | **DIVINE LANCE **[two-actions] **CANTRIP 1**  **ATTACK** **CANTRIP** **CONCENTRATE** **MANIPULATE** **SANCTIFIED** **SPIRIT**  **Traditions** divine  **Range **60 feet; **Targets** 1 creature  **Defen |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/31/SectionHeader/19` | 0.426767 | **DISCHARGE **[two-actions] **SPELL 3**  **CONCENTRATE** **ELECTRICITY** **MANIPULATE**  **Traditions** arcane, primal  **Range **30 feet;** Targets** 1 creature or object with the tech  trait  **Defe |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/34/SectionHeader/18` | 0.426344 | **ELDRITCH LANCE **[two-actions] **CANTRIP 1**  **ATTACK** **CANTRIP** **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** divine, occult  **Range **30 feet; **Targets** 1 creature  **Defense** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/30/Text/23` | 0.422226 | **DELETE **[two-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult  **Range **30 feet;** Targets** 1 dataset or tech item with the  tracking trait  You delete data fro |

### Query 103
- Text: What does **AERIAL FORM **[two-actions] **SPELL 4** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/36']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/7/Text/19', 'PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/36', 'PZO22001 Starfinder Player Core 294-329::/page/35/Text/68']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/36', 'PZO22001 Starfinder Player Core 294-329::/page/19/ListItem/45', 'PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/28']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/19/ListItem/45` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/28` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/19` | 0.620686 | **SPELL NAME **[one-action] **SPELL (RANK)** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/36` | 0.583761 | **AERIAL FORM **[two-actions] **SPELL 4**  **CONCENTRATE** **MANIPULATE** **POLYMORPH**  **Traditions** arcane, primal  **Duration** 1 minute  You harness your mastery of the sky to reshape your body |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/68` | 0.536622 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/61` | 0.494622 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/24` | 0.494622 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/26` | 0.494622 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/80` | 0.494622 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/74` | 0.494622 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/59` | 0.494622 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/83` | 0.494622 | **SPELLS** |

### Query 104
- Text: What does **AIR BUBBLE **[reaction] **SPELL 1** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/4', 'PZO22001 Starfinder Player Core 294-329::/page/11/Text/46', 'PZO22001 Starfinder Player Core 294-329::/page/16/Text/58']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/4', 'PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/12', 'PZO22001 Starfinder Player Core 294-329::/page/20/Text/3']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/12` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/20/Text/3` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/4` | 0.676879 | **AIR BUBBLE **[reaction] **SPELL 1**  **AIR** **CONCENTRATE**  **Traditions** arcane, divine, primal  **Trigger** A creature within range enters an environment where  it can't breathe.  **Range **60 |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/46` | 0.649056 | **Air Bubble** React to create air for a creature to breathe. |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/16/Text/58` | 0.649056 | **Air Bubble** React to create air for a creature to breathe. |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/8/Text/28` | 0.607056 | **Air Bubble** React to create air for a creature to breathe. |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/19` | 0.557746 | **SPELL NAME **[one-action] **SPELL (RANK)** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/1` | 0.524836 | **SUBTLE SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/33` | 0.514657 | **EQUIPMENT** **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/23/Text/43` | 0.514657 | **EQUIPMENT** **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/24` | 0.505060 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/26` | 0.505060 | **SPELLS** |

### Query 105
- Text: What does **AKASHIC DOWNLOAD **[three-actions] **SPELL 1** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/12']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/12', 'PZO22001 Starfinder Player Core 294-329::/page/7/Text/19', 'PZO22001 Starfinder Player Core 294-329::/page/13/Text/59']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/12', 'PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/21', 'PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/4']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/21` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/4` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/12` | 0.655324 | **AKASHIC DOWNLOAD **[three-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE**  **Traditions** occult  **Requirements** You have a comm unit or computer, used as  a locus.  **Duration** 1 day  You e |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/19` | 0.628805 | **SPELL NAME **[one-action] **SPELL (RANK)** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/59` | 0.551927 | **Akashic** **Download**H Consult the Akashic Record for info on  a topic. |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/83` | 0.480715 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/74` | 0.480715 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/80` | 0.480715 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/61` | 0.480715 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/24` | 0.480715 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/68` | 0.480715 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/86` | 0.480715 | **SPELLS** |

### Query 106
- Text: What does **AKASHIC REVIVAL** **SPELL 8** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/21']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/21', 'PZO22001 Starfinder Player Core 294-329::/page/13/SectionHeader/21', 'PZO22001 Starfinder Player Core 294-329::/page/18/SectionHeader/48']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/21', 'PZO22001 Starfinder Player Core 294-329::/page/20/Text/33', 'PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/12']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/20/Text/33` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/12` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/21` | 0.600851 | **AKASHIC REVIVAL** **SPELL 8**  **CONCENTRATE** **MANIPULATE**  **Traditions** occult **Cast** 10 minutes  **Range** touch; **Targets** 1 willing creature  **Duration** 1 day  You dispatch perfect do |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/13/SectionHeader/21` | 0.541025 | DIVINE 8TH-RANK SPELLS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/18/SectionHeader/48` | 0.540009 | PRIMAL 8TH-RANK SPELLS |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/16/SectionHeader/17` | 0.494578 | OCCULT 8TH-RANK SPELLS |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/11/SectionHeader/2` | 0.477704 | ARCANE 8TH-RANK SPELLS |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/33` | 0.475693 | **EQUIPMENT** **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/23/Text/43` | 0.475693 | **EQUIPMENT** **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0` | 0.471000 | CHAPTER 7: SPELLS |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/19` | 0.466542 | **SPELL NAME **[one-action] **SPELL (RANK)** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/26` | 0.462467 | **SPELLS** |

### Query 107
- Text: What does **ALARM** **SPELL 1** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/20/Text/33']
- Expected found: `True`
- Expected rank: `20`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/7/Text/19', 'PZO22001 Starfinder Player Core 294-329::/page/11/Text/83', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/36']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/20/Text/33', 'PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/21', 'PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/41']
- Expanded expected found: `True`
- Expanded expected rank: `20`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/21` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/41` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/19` | 0.652616 | **SPELL NAME **[one-action] **SPELL (RANK)** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/36` | 0.641200 | **SPELLS** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/83` | 0.641200 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/74` | 0.599200 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/80` | 0.599200 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/61` | 0.599200 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/86` | 0.599200 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/65` | 0.599200 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/68` | 0.599200 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/86` | 0.599200 | **SPELLS** |

### Query 108
- Text: What does **ANALYZE TARGET **[two-actions] **CANTRIP 1** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/41']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/41', 'PZO22001 Starfinder Player Core 294-329::/page/11/Text/29', 'PZO22001 Starfinder Player Core 294-329::/page/13/Text/42']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/41', 'PZO22001 Starfinder Player Core 294-329::/page/21/SectionHeader/4', 'PZO22001 Starfinder Player Core 294-329::/page/20/Text/33']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/21/SectionHeader/4` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/20/Text/33` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/41` | 0.718348 | **ANALYZE TARGET **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **DETECTION** **MANIPULATE**  **Traditions** arcane, divine, occult, primal **Range **30 feet; **Targets** 1 creature  **Dur |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/29` | 0.565686 | **Analyze** **Target**H Gather data about a target's basic physiology. **Daze**H Cloud a creature's mind and possibly stun it. |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/42` | 0.565686 | **Analyze** **Target**H Gather data about a target's basic physiology. **Daze**H Cloud a creature's mind and possibly stun it. |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/28` | 0.509231 | **ADHERE **[one-action] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult, primal  **Range **touch; **Targets** 1 held or unattended object or a 5-footsquare sur |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/30/Text/2` | 0.490033 | **DAZE **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **MANIPULATE** **MENTAL** **NONLETHAL**  **Traditions** arcane, divine, occult **Range **60 feet; **Targets** 1 creature **Defense** W |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/16/Text/15` | 0.487970 | **True Target** Make multiple attacks against a creature  especially accurate. |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/10/Text/68` | 0.487970 | **True Target** Make multiple attacks against a creature  especially accurate. |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/32/SectionHeader/24` | 0.487815 | **DIVINE LANCE **[two-actions] **CANTRIP 1**  **ATTACK** **CANTRIP** **CONCENTRATE** **MANIPULATE** **SANCTIFIED** **SPIRIT**  **Traditions** divine  **Range **60 feet; **Targets** 1 creature  **Defen |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/20` | 0.487417 | TARGETS |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/34/SectionHeader/38` | 0.487415 | **ELECTRIC ARC **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **ELECTRICITY** **MANIPULATE**  **Traditions** arcane, primal  **Range **30 feet; **Targets** 1 or 2 creatures  **Defense** ba |

### Query 109
- Text: What does **ANIMAL FORM **[two-actions] **SPELL 2** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/21/SectionHeader/4']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/7/Text/19', 'PZO22001 Starfinder Player Core 294-329::/page/21/SectionHeader/4', 'PZO22001 Starfinder Player Core 294-329::/page/15/Text/80']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/21/SectionHeader/4', 'PZO22001 Starfinder Player Core 294-329::/page/21/ListItem/13', 'PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/41']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/21/ListItem/13` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/41` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/19` | 0.644005 | **SPELL NAME **[one-action] **SPELL (RANK)** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/21/SectionHeader/4` | 0.633387 | **ANIMAL FORM **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE** **POLYMORPH**  **Traditions** primal  **Duration** 1 minute  You call upon primal energy to transform yourself into a  Medium |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/80` | 0.575290 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/27/Text/68` | 0.533290 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/59` | 0.533290 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/26` | 0.533290 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/36` | 0.533290 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/60` | 0.533290 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/83` | 0.533290 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/24` | 0.533290 | **SPELLS** |

### Query 110
- Text: What does **ANT HAUL **[two-actions] **SPELL 1** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/22/Text/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/22/Text/4', 'PZO22001 Starfinder Player Core 294-329::/page/7/Text/19', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/36']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/22/Text/4', 'PZO22001 Starfinder Player Core 294-329::/page/22/Text/3', 'PZO22001 Starfinder Player Core 294-329::/page/22/Text/11']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/22/Text/3` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/22/Text/11` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/22/Text/4` | 0.734145 | **ANT HAUL **[two-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal **Range **touch; **Targets** 1 creature  **Duration** 8 hours  You reinforce the target's musculos |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/19` | 0.655184 | **SPELL NAME **[one-action] **SPELL (RANK)** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/36` | 0.572120 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/24` | 0.530120 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/68` | 0.530120 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/61` | 0.530120 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/26` | 0.530120 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/86` | 0.530120 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/74` | 0.530120 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/27/Text/68` | 0.530120 | **SPELLS** |

### Query 111
- Text: What does **ARCTIC RIFT **[two-actions] **SPELL 8** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/22/Text/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/22/Text/11', 'PZO22001 Starfinder Player Core 294-329::/page/7/Text/19', 'PZO22001 Starfinder Player Core 294-329::/page/33/SectionHeader/47']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/22/Text/11', 'PZO22001 Starfinder Player Core 294-329::/page/22/Text/4', 'PZO22001 Starfinder Player Core 294-329::/page/22/Text/18']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/22/Text/4` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/22/Text/18` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/22/Text/11` | 0.681094 | **ARCTIC RIFT **[two-actions] **SPELL 8**  **COLD** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal  **Area** 120-foot line  **Defense** Fortitude  A jagged crack opens in the air, deali |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/19` | 0.600664 | **SPELL NAME **[one-action] **SPELL (RANK)** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/33/SectionHeader/47` | 0.533311 | **EARTHQUAKE **[two-actions] **SPELL 8**  **CONCENTRATE** **EARTH** **MANIPULATE**  **Traditions** arcane, primal  **Range **500 feet;** Area** 60-foot burst  **Duration** 1 round  You shake the groun |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/16` | 0.473508 | **ACID GRIP **[two-actions] **SPELL 2**  **ACID** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal  **Range **120 feet;** Targets** 1 creature  **Defense** Reflex  An ephemeral, taloned h |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/23/Text/43` | 0.473197 | **EQUIPMENT** **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/33` | 0.473197 | **EQUIPMENT** **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0` | 0.464455 | CHAPTER 7: SPELLS |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/16/SectionHeader/17` | 0.461810 | OCCULT 8TH-RANK SPELLS |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/33/SectionHeader/36` | 0.460837 | **EARTHBIND **[two-actions] **SPELL 3**  **CONCENTRATE** **EARTH** **MANIPULATE**  **Traditions** arcane, primal  **Range **120 feet;** Targets** 1 flying creature  **Defense** Fortitude; **Duration** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/11/SectionHeader/2` | 0.460087 | ARCANE 8TH-RANK SPELLS |

### Query 112
- Text: What does **ATOMIC BLAST **[three-actions] **SPELL 9** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/22/Text/23']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/22/Text/23', 'PZO22001 Starfinder Player Core 294-329::/page/11/Text/12', 'PZO22001 Starfinder Player Core 294-329::/page/18/Text/57']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/22/Text/23', 'PZO22001 Starfinder Player Core 294-329::/page/22/Text/33', 'PZO22001 Starfinder Player Core 294-329::/page/22/Text/22']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/22/Text/33` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/22/Text/22` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/22/Text/23` | 0.724786 | **ATOMIC BLAST **[three-actions] **SPELL 9**  **CONCENTRATE** **FIRE** **MANIPULATE** **RADIATION**  **Traditions** arcane, primal  **Range **500 feet;** Area** 100-foot burst **Defense** Reflex; **Du |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/12` | 0.620402 | **Atomic** **Blast** Create a nuclear explosion with fallout. |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/18/Text/57` | 0.620402 | **Atomic** **Blast** Create a nuclear explosion with fallout. |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/19` | 0.568311 | **SPELL NAME **[one-action] **SPELL (RANK)** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/60` | 0.516973 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/36` | 0.516973 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/27/Text/68` | 0.516973 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/61` | 0.516973 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/59` | 0.516973 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/86` | 0.516973 | **SPELLS** |

### Query 113
- Text: What does **AUGURY** **SPELL 2** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/22/Text/33']
- Expected found: `True`
- Expected rank: `17`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/17/Text/86', 'PZO22001 Starfinder Player Core 294-329::/page/15/Text/80', 'PZO22001 Starfinder Player Core 294-329::/page/35/Text/68']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/22/Text/33', 'PZO22001 Starfinder Player Core 294-329::/page/22/Text/40', 'PZO22001 Starfinder Player Core 294-329::/page/22/Text/23']
- Expanded expected found: `True`
- Expanded expected rank: `17`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/22/Text/40` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/22/Text/23` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/86` | 0.612193 | **SPELLS** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/80` | 0.612193 | **SPELLS** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/68` | 0.612193 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/83` | 0.570193 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/86` | 0.570193 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/24` | 0.570193 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/61` | 0.570193 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/59` | 0.570193 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/26` | 0.570193 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/74` | 0.570193 | **SPELLS** |

### Query 114
- Text: What does **AVATAR **[two-actions] **SPELL 10** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/22/Text/40']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/7/Text/19', 'PZO22001 Starfinder Player Core 294-329::/page/22/Text/40', 'PZO22001 Starfinder Player Core 294-329::/page/13/Text/34']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/22/Text/40', 'PZO22001 Starfinder Player Core 294-329::/page/22/ListItem/48', 'PZO22001 Starfinder Player Core 294-329::/page/22/Text/33']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/22/ListItem/48` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/22/Text/33` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/19` | 0.603001 | **SPELL NAME **[one-action] **SPELL (RANK)** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/22/Text/40` | 0.598109 | **AVATAR **[two-actions] **SPELL 10**  **CONCENTRATE** **MANIPULATE** **POLYMORPH**  **Traditions** divine **Duration** 1 minute  You transform into an avatar of your deity, assuming a Huge  battle fo |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/34` | 0.539535 | **Avatar** Transform into a battle form with benefits determined  by your deity. |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/33` | 0.482758 | **EQUIPMENT** **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/23/Text/43` | 0.482758 | **EQUIPMENT** **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/74` | 0.479034 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/68` | 0.479034 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/61` | 0.479034 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/59` | 0.479034 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/65` | 0.479034 | **SPELLS** |

### Query 115
- Text: What does **BANE **[two-actions] **SPELL 1** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/23/SectionHeader/20']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/7/Text/19', 'PZO22001 Starfinder Player Core 294-329::/page/23/SectionHeader/20', 'PZO22001 Starfinder Player Core 294-329::/page/11/Text/48']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/23/SectionHeader/20', 'PZO22001 Starfinder Player Core 294-329::/page/23/SectionHeader/26', 'PZO22001 Starfinder Player Core 294-329::/page/23/ListItem/19']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/23/SectionHeader/26` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/23/ListItem/19` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/19` | 0.678455 | **SPELL NAME **[one-action] **SPELL (RANK)** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/23/SectionHeader/20` | 0.662660 | **BANE **[two-actions] **SPELL 1**  **AURA** **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** divine, occult **Area** 10-foot emanation  **Defense** Will; **Duration** 1 minute  You fill the |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/48` | 0.563858 | **Bane** Weaken enemies' attacks in an aura around you. |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/61` | 0.521858 | **Bane** Weaken enemies' attacks in an aura around you. |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/74` | 0.505927 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/61` | 0.505927 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/36` | 0.505927 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/86` | 0.505927 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/60` | 0.505927 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/65` | 0.505927 | **SPELLS** |

### Query 116
- Text: What does **BANISHMENT **[two-actions] **SPELL 5** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/23/SectionHeader/26']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/23/SectionHeader/26', 'PZO22001 Starfinder Player Core 294-329::/page/7/Text/19', 'PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/29']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/23/SectionHeader/26', 'PZO22001 Starfinder Player Core 294-329::/page/23/SectionHeader/20', 'PZO22001 Starfinder Player Core 294-329::/page/23/Text/38']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/23/SectionHeader/20` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/23/Text/38` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/23/SectionHeader/26` | 0.644755 | **BANISHMENT **[two-actions] **SPELL 5**  **CONCENTRATE** **INCAPACITATION** **MANIPULATE**  **Traditions** arcane, divine, occult, primal  **Range **30 feet; **Targets** 1 creature that isn't on its |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/19` | 0.589346 | **SPELL NAME **[one-action] **SPELL (RANK)** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/29` | 0.518064 | **CONTROL MACHINE **[two-actions] **SPELL 5**  **UNCOMMON** **CONCENTRATE** **INCAPACITATION** **MANIPULATE**  **Traditions** arcane, occult  **Range **30 feet;** Targets** 1 creature or hazard with t |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/36` | 0.471171 | **BLINDNESS **[two-actions] **SPELL 3**  **CONCENTRATE** **INCAPACITATION** **MANIPULATE**  **Traditions** arcane, divine, occult, primal  **Range **30 feet;** Targets** 1 creature  **Defense** Fortit |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/83` | 0.466541 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/74` | 0.466541 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/26` | 0.466541 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/61` | 0.466541 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/68` | 0.466541 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/24` | 0.466541 | **SPELLS** |

### Query 117
- Text: What does **BATTLE SONATA **[two-actions] **SPELL 4** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/1', 'PZO22001 Starfinder Player Core 294-329::/page/7/Text/19', 'PZO22001 Starfinder Player Core 294-329::/page/7/Text/33']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/1', 'PZO22001 Starfinder Player Core 294-329::/page/24/Text/8', 'PZO22001 Starfinder Player Core 294-329::/page/23/Text/50']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/24/Text/8` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/23/Text/50` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/1` | 0.673785 | **BATTLE SONATA **[two-actions] **SPELL 4**  **CONCENTRATE** **MANIPULATE** **SONIC**  **Traditions** divine, occult  **Area** 15-foot cone  **Defense** Will  This spell was composed by pahtra battle |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/19` | 0.643943 | **SPELL NAME **[one-action] **SPELL (RANK)** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/33` | 0.548409 | **EQUIPMENT** **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/23/Text/43` | 0.506409 | **EQUIPMENT** **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/80` | 0.498297 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/61` | 0.498297 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/86` | 0.498297 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/74` | 0.498297 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/24` | 0.498297 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/26` | 0.498297 | **SPELLS** |

### Query 118
- Text: What does **BIND UNDEAD **[two-actions] **SPELL 3** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/13', 'PZO22001 Starfinder Player Core 294-329::/page/7/Text/19', 'PZO22001 Starfinder Player Core 294-329::/page/33/Text/61']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/13', 'PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/20', 'PZO22001 Starfinder Player Core 294-329::/page/24/Text/12']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/20` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/24/Text/12` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/13` | 0.654784 | **BIND UNDEAD **[two-actions] **SPELL 3**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, occult  **Range **30 feet; **Targets** 1 mindless undead creature with a  level no greater tha |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/19` | 0.645153 | **SPELL NAME **[one-action] **SPELL (RANK)** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/61` | 0.553008 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/26` | 0.511008 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/24` | 0.511008 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/80` | 0.511008 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/68` | 0.511008 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/83` | 0.511008 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/59` | 0.511008 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/86` | 0.511008 | **SPELLS** |

### Query 119
- Text: What does **BLAZING BOLT **[one-action]** TO **[three-actions] **SPELL 2** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/20']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/20', 'PZO22001 Starfinder Player Core 294-329::/page/7/Text/19', 'PZO22001 Starfinder Player Core 294-329::/page/9/Text/6']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/20', 'PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/13', 'PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/29']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/13` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/29` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/20` | 0.710547 | **BLAZING BOLT **[one-action]** TO **[three-actions] **SPELL 2**  **ATTACK** **CONCENTRATE** **FIRE** **MANIPULATE**  **Traditions** arcane, primal  **Range **60 feet; **Targets** 1 or more creatures |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/19` | 0.650123 | **SPELL NAME **[one-action] **SPELL (RANK)** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/6` | 0.571266 | **Blazing Bolt**H Fire one to three flaming bolts at different foes. |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/20` | 0.529266 | **Blazing Bolt**H Fire one to three flaming bolts at different foes. |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/36` | 0.504320 | **BLINDNESS **[two-actions] **SPELL 3**  **CONCENTRATE** **INCAPACITATION** **MANIPULATE**  **Traditions** arcane, divine, occult, primal  **Range **30 feet;** Targets** 1 creature  **Defense** Fortit |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/29` | 0.504196 | **BLESS **[two-actions] **SPELL 1**  **AURA** **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** divine, occult  **Area** 15-foot emanation  **Duration** 1 minute  Blessings from beyond help yo |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/22/Text/23` | 0.492604 | **ATOMIC BLAST **[three-actions] **SPELL 9**  **CONCENTRATE** **FIRE** **MANIPULATE** **RADIATION**  **Traditions** arcane, primal  **Range **500 feet;** Area** 100-foot burst **Defense** Reflex; **Du |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/47` | 0.488152 | **BLUR **[two-actions] **SPELL 2**  **CONCENTRATE** **ILLUSION** **MANIPULATE** **VISUAL**  **Traditions** arcane, occult  **Range **touch;** Targets** 1 creature  **Duration** 1 minute  The target's |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/31/SectionHeader/19` | 0.482473 | **DISCHARGE **[two-actions] **SPELL 3**  **CONCENTRATE** **ELECTRICITY** **MANIPULATE**  **Traditions** arcane, primal  **Range **30 feet;** Targets** 1 creature or object with the tech  trait  **Defe |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/32/SectionHeader/1` | 0.477418 | **DISPELLING GLOBE **[two-actions] **SPELL 4**  **UNCOMMON** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, occult  **Area** 10-foot burst centered on one corner of your space **Durati |

### Query 120
- Text: What does **BLESS **[two-actions] **SPELL 1** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/29']
- Expected found: `True`
- Expected rank: `16`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/7/Text/19', 'PZO22001 Starfinder Player Core 294-329::/page/33/Text/61', 'PZO22001 Starfinder Player Core 294-329::/page/11/Text/83']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/29', 'PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/20', 'PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/36']
- Expanded expected found: `True`
- Expanded expected rank: `16`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/20` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/36` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/19` | 0.678604 | **SPELL NAME **[one-action] **SPELL (RANK)** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/83` | 0.642740 | **SPELLS** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/61` | 0.642740 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/36` | 0.600740 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/74` | 0.600740 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/60` | 0.600740 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/59` | 0.600740 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/86` | 0.600740 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/80` | 0.600740 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/27/Text/68` | 0.600740 | **SPELLS** |

### Query 121
- Text: What does **BLINDNESS **[two-actions] **SPELL 3** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/36']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/7/Text/19', 'PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/36', 'PZO22001 Starfinder Player Core 294-329::/page/19/Text/59']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/36', 'PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/47', 'PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/29']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/47` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/29` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/19` | 0.665801 | **SPELL NAME **[one-action] **SPELL (RANK)** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/36` | 0.657003 | **BLINDNESS **[two-actions] **SPELL 3**  **CONCENTRATE** **INCAPACITATION** **MANIPULATE**  **Traditions** arcane, divine, occult, primal  **Range **30 feet;** Targets** 1 creature  **Defense** Fortit |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/59` | 0.620847 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/61` | 0.578847 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/74` | 0.578847 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/80` | 0.578847 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/26` | 0.578847 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/68` | 0.578847 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/24` | 0.578847 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/86` | 0.578847 | **SPELLS** |

### Query 122
- Text: What does **BLUR **[two-actions] **SPELL 2** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/47']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/7/Text/19', 'PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/47', 'PZO22001 Starfinder Player Core 294-329::/page/15/Text/80']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/47', 'PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/54', 'PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/36']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/54` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/36` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/19` | 0.621182 | **SPELL NAME **[one-action] **SPELL (RANK)** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/47` | 0.617676 | **BLUR **[two-actions] **SPELL 2**  **CONCENTRATE** **ILLUSION** **MANIPULATE** **VISUAL**  **Traditions** arcane, occult  **Range **touch;** Targets** 1 creature  **Duration** 1 minute  The target's |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/80` | 0.543595 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/61` | 0.501595 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/36` | 0.501595 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/60` | 0.501595 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/83` | 0.501595 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/24` | 0.501595 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/27/Text/68` | 0.501595 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/26` | 0.501595 | **SPELLS** |

### Query 123
- Text: What does **BREATH OF LIFE **[reaction] **SPELL 5** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/54']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/54', 'PZO22001 Starfinder Player Core 294-329::/page/12/Text/56', 'PZO22001 Starfinder Player Core 294-329::/page/7/Text/19']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/54', 'PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/62', 'PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/47']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/62` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/47` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/54` | 0.672825 | **BREATH OF LIFE **[reaction] **SPELL 5**  **CONCENTRATE** **HEALING** **VITALITY**  **Traditions** divine  **Trigger** A living creature within range would die.  **Range **60 feet;** Targets** the tr |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/12/Text/56` | 0.568750 | **Breath of Life**H React to revive a character at the moment of  its death. |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/19` | 0.559458 | **SPELL NAME **[one-action] **SPELL (RANK)** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/61` | 0.479170 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/59` | 0.479170 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/83` | 0.479170 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/86` | 0.479170 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/26` | 0.479170 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/68` | 0.479170 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/80` | 0.479170 | **SPELLS** |

### Query 124
- Text: What does **BREATHE FIRE **[two-actions] **SPELL 1** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/62']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/62', 'PZO22001 Starfinder Player Core 294-329::/page/7/Text/19', 'PZO22001 Starfinder Player Core 294-329::/page/8/Text/31']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/62', 'PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/70', 'PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/54']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/70` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/54` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/62` | 0.694161 | **BREATHE FIRE **[two-actions] **SPELL 1**  **CONCENTRATE** **FIRE** **MANIPULATE**  **Traditions** arcane, primal  **Area** 15-foot cone  **Defense** basic Reflex  A gout of flame sprays from your mo |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/19` | 0.646592 | **SPELL NAME **[one-action] **SPELL (RANK)** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/8/Text/31` | 0.589891 | **Breathe Fire**H Release a small cone of flame from your mouth. **Cellular** **Stimulant**H Stimulate the target's body for a short  while at the expense of future energy. |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/16/Text/61` | 0.516957 | **Breathe Fire**H Release a small cone of flame from your mouth. |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/60` | 0.514418 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/36` | 0.514418 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/27/Text/68` | 0.514418 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/61` | 0.514418 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/68` | 0.514418 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/26` | 0.514418 | **SPELLS** |

### Query 125
- Text: What does **CAIRN FORM **[one-action] **SPELL 4** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/70']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/7/Text/19', 'PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/70', 'PZO22001 Starfinder Player Core 294-329::/page/17/Text/86']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/70', 'PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/62', 'PZO22001 Starfinder Player Core 294-329::/page/25/SectionHeader/4']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/62` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/25/SectionHeader/4` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/19` | 0.654566 | **SPELL NAME **[one-action] **SPELL (RANK)** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/70` | 0.653175 | **CAIRN FORM **[one-action] **SPELL 4**  **CONCENTRATE** **EARTH** **MANIPULATE** **MORPH**  **Traditions** arcane, primal  **Range **touch;** Targets** 1 creature  **Duration** 1 minute  Your target' |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/86` | 0.526815 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/80` | 0.484815 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/61` | 0.484815 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/26` | 0.484815 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/59` | 0.484815 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/74` | 0.484815 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/68` | 0.484815 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/24` | 0.484815 | **SPELLS** |

### Query 126
- Text: What does **CALL COSMOS **[two-actions] **SPELL 9** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/25/SectionHeader/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/25/SectionHeader/4', 'PZO22001 Starfinder Player Core 294-329::/page/7/Text/19', 'PZO22001 Starfinder Player Core 294-329::/page/13/Text/29']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/25/SectionHeader/4', 'PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/70', 'PZO22001 Starfinder Player Core 294-329::/page/25/Text/11']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/70` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/25/Text/11` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/25/SectionHeader/4` | 0.716617 | **CALL COSMOS **[two-actions] **SPELL 9**  **COLD** **CONCENTRATE** **FIRE** **MANIPULATE**  **Traditions** divine, primal  **Range **500 feet;** Area** 20-foot radius, 40-foot tall cylinder **Defense |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/19` | 0.594899 | **SPELL NAME **[one-action] **SPELL (RANK)** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/29` | 0.542157 | **Call** **Cosmos**H Call down a column of cosmic matter to burn  and freeze. |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/18/Text/58` | 0.500157 | **Call** **Cosmos**H Call down a column of cosmic matter to burn  and freeze. |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/25/Text/11` | 0.493020 | **CALM **[two-actions] **SPELL 2**  **CONCENTRATE** **EMOTION** **INCAPACITATION** **MANIPULATE** **MENTAL**  **Traditions** divine, occult  **Range **120 feet;** Area** 10-foot burst  **Defense** Wil |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/32/SectionHeader/66` | 0.479830 | **DOOM SCROLL **[two-actions] **SPELL 2**  **CONCENTRATE** **INCAPACITATION** **MANIPULATE** **VISUAL**  **Traditions** arcane, divine, occult **Range **60 feet; **Area** 15-foot burst  **Defense** Wi |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/33` | 0.471280 | **EQUIPMENT** **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/23/Text/43` | 0.471280 | **EQUIPMENT** **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/61` | 0.468117 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/86` | 0.468117 | **SPELLS** |

### Query 127
- Text: What does **CALM **[two-actions] **SPELL 2** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/25/Text/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/25/Text/11', 'PZO22001 Starfinder Player Core 294-329::/page/7/Text/19', 'PZO22001 Starfinder Player Core 294-329::/page/19/Text/59']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/25/Text/11', 'PZO22001 Starfinder Player Core 294-329::/page/25/SectionHeader/4', 'PZO22001 Starfinder Player Core 294-329::/page/25/SectionHeader/21']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/25/SectionHeader/4` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/25/SectionHeader/21` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/25/Text/11` | 0.645679 | **CALM **[two-actions] **SPELL 2**  **CONCENTRATE** **EMOTION** **INCAPACITATION** **MANIPULATE** **MENTAL**  **Traditions** divine, occult  **Range **120 feet;** Area** 10-foot burst  **Defense** Wil |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/19` | 0.630078 | **SPELL NAME **[one-action] **SPELL (RANK)** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/59` | 0.553804 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/36` | 0.511804 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/60` | 0.511804 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/86` | 0.511804 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/80` | 0.511804 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/24` | 0.511804 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/65` | 0.511804 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/27/Text/68` | 0.511804 | **SPELLS** |

### Query 128
- Text: What does **CARCINIZATION **[two-actions] **SPELL 5** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/25/SectionHeader/21']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/25/SectionHeader/21', 'PZO22001 Starfinder Player Core 294-329::/page/18/Text/9', 'PZO22001 Starfinder Player Core 294-329::/page/7/Text/19']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/25/SectionHeader/21', 'PZO22001 Starfinder Player Core 294-329::/page/26/Text/4', 'PZO22001 Starfinder Player Core 294-329::/page/25/Text/11']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/26/Text/4` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/25/Text/11` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/25/SectionHeader/21` | 0.611717 | **CARCINIZATION **[two-actions] **SPELL 5**  **INCAPACITATION** **MANIPULATE** **POLYMORPH**  **Traditions** primal  **Range **30 feet;** Targets** 1 creature  **Defense** Fortitude; **Duration** 1 mi |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/18/Text/9` | 0.556185 | **Carcinization** Transform a target into a crab. |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/19` | 0.546504 | **SPELL NAME **[one-action] **SPELL (RANK)** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/29` | 0.484790 | **CONTROL MACHINE **[two-actions] **SPELL 5**  **UNCOMMON** **CONCENTRATE** **INCAPACITATION** **MANIPULATE**  **Traditions** arcane, occult  **Range **30 feet;** Targets** 1 creature or hazard with t |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/23/SectionHeader/26` | 0.469124 | **BANISHMENT **[two-actions] **SPELL 5**  **CONCENTRATE** **INCAPACITATION** **MANIPULATE**  **Traditions** arcane, divine, occult, primal  **Range **30 feet; **Targets** 1 creature that isn't on its |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/25/Text/11` | 0.467704 | **CALM **[two-actions] **SPELL 2**  **CONCENTRATE** **EMOTION** **INCAPACITATION** **MANIPULATE** **MENTAL**  **Traditions** divine, occult  **Range **120 feet;** Area** 10-foot burst  **Defense** Wil |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/29/SectionHeader/35` | 0.460787 | **CURSED METAMORPHOSIS **[two-actions] **SPELL 6**  **CONCENTRATE** **CURSE** **INCAPACITATION** **MANIPULATE** **POLYMORPH**  **Traditions** arcane, occult, primal **Range **30 feet;** Targets** 1 cr |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/34/SectionHeader/53` | 0.442704 | **ELEMENTAL FORM **[two-actions] **SPELL 5**  **CONCENTRATE** **MANIPULATE** **POLYMORPH**  **Traditions** arcane, primal  **Duration** 1 minute  You call upon the power of the planes to transform int |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/70` | 0.439359 | **CAIRN FORM **[one-action] **SPELL 4**  **CONCENTRATE** **EARTH** **MANIPULATE** **MORPH**  **Traditions** arcane, primal  **Range **touch;** Targets** 1 creature  **Duration** 1 minute  Your target' |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/28/Text/11` | 0.439351 | **CONFUSION **[two-actions] **SPELL 4**  **CONCENTRATE** **EMOTION** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult **Range **30 feet;** Targets** 1 creature **Defense** Will; **Duration** 1 |

### Query 129
- Text: What does **CATACLYSM **[two-actions] **SPELL 10** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/5', 'PZO22001 Starfinder Player Core 294-329::/page/7/Text/19', 'PZO22001 Starfinder Player Core 294-329::/page/35/Text/68']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/5', 'PZO22001 Starfinder Player Core 294-329::/page/26/Text/4', 'PZO22001 Starfinder Player Core 294-329::/page/26/ListItem/17']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/26/Text/4` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/26/ListItem/17` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/5` | 0.663845 | **CATACLYSM **[two-actions] **SPELL 10**  **ACID** **AIR** **COLD** **CONCENTRATE** **EARTH** **ELECTRICITY** **FIRE** **MANIPULATE** **WATER**  **Traditions** arcane, primal  **Range **1,000 feet;** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/19` | 0.514084 | **SPELL NAME **[one-action] **SPELL (RANK)** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/68` | 0.505901 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/80` | 0.463901 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/83` | 0.463901 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/86` | 0.463901 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/74` | 0.463901 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/59` | 0.463901 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/24` | 0.463901 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/61` | 0.463901 | **SPELLS** |

### Query 130
- Text: What does **CAUSTIC BLAST **[two-actions] **CANTRIP 1** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/19']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/19', 'PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/27', 'PZO22001 Starfinder Player Core 294-329::/page/16/Text/38']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/19', 'PZO22001 Starfinder Player Core 294-329::/page/26/ListItem/18', 'PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/27']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/26/ListItem/18` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/27` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/19` | 0.780861 | **CAUSTIC BLAST **[two-actions] **CANTRIP 1**  **ACID** **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal  **Range **30 feet; **Area** 5-foot burst  **Defense** basic Reflex  Y |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/27` | 0.590965 | **CAUSTIC CONVERSION **[two-actions] **SPELL 2**  **ACID** **ATTACK** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal  **Range **120 feet;** Targets** 1 creature  **Defense** AC  You lau |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/16/Text/38` | 0.566609 | **Analyze** **Target**H Gather data about a target's basic physiology. **Caustic Blast**H Fling a glob of acid that splashes a small area. |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/8/Text/8` | 0.524609 | **Analyze** **Target**H Gather data about a target's basic physiology. **Caustic Blast**H Fling a glob of acid that splashes a small area. |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/22/Text/23` | 0.510270 | **ATOMIC BLAST **[three-actions] **SPELL 9**  **CONCENTRATE** **FIRE** **MANIPULATE** **RADIATION**  **Traditions** arcane, primal  **Range **500 feet;** Area** 100-foot burst **Defense** Reflex; **Du |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/30/Text/2` | 0.498361 | **DAZE **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **MANIPULATE** **MENTAL** **NONLETHAL**  **Traditions** arcane, divine, occult **Range **60 feet; **Targets** 1 creature **Defense** W |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/25/Text/11` | 0.489235 | **CALM **[two-actions] **SPELL 2**  **CONCENTRATE** **EMOTION** **INCAPACITATION** **MANIPULATE** **MENTAL**  **Traditions** divine, occult  **Range **120 feet;** Area** 10-foot burst  **Defense** Wil |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/18/Text/57` | 0.487872 | **Atomic** **Blast** Create a nuclear explosion with fallout. |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/12` | 0.487872 | **Atomic** **Blast** Create a nuclear explosion with fallout. |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/41` | 0.480501 | **ANALYZE TARGET **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **DETECTION** **MANIPULATE**  **Traditions** arcane, divine, occult, primal **Range **30 feet; **Targets** 1 creature  **Dur |

### Query 131
- Text: What does **CAUSTIC CONVERSION **[two-actions] **SPELL 2** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/27']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/27', 'PZO22001 Starfinder Player Core 294-329::/page/7/Text/19', 'PZO22001 Starfinder Player Core 294-329::/page/9/Text/8']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/27', 'PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/19', 'PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/36']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/19` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/36` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/27` | 0.664513 | **CAUSTIC CONVERSION **[two-actions] **SPELL 2**  **ACID** **ATTACK** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal  **Range **120 feet;** Targets** 1 creature  **Defense** AC  You lau |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/19` | 0.552614 | **SPELL NAME **[one-action] **SPELL (RANK)** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/8` | 0.546154 | **Caustic** **Conversion**H Send nanites to dissolve your target. |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/21` | 0.504154 | **Caustic** **Conversion**H Send nanites to dissolve your target. |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/19` | 0.499831 | **CAUSTIC BLAST **[two-actions] **CANTRIP 1**  **ACID** **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal  **Range **30 feet; **Area** 5-foot burst  **Defense** basic Reflex  Y |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/28/Text/11` | 0.486005 | **CONFUSION **[two-actions] **SPELL 4**  **CONCENTRATE** **EMOTION** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult **Range **30 feet;** Targets** 1 creature **Defense** Will; **Duration** 1 |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/29/SectionHeader/35` | 0.474842 | **CURSED METAMORPHOSIS **[two-actions] **SPELL 6**  **CONCENTRATE** **CURSE** **INCAPACITATION** **MANIPULATE** **POLYMORPH**  **Traditions** arcane, occult, primal **Range **30 feet;** Targets** 1 cr |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/68` | 0.469266 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/59` | 0.469266 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/65` | 0.469266 | **SPELLS** |

### Query 132
- Text: What does **CELLULAR STIMULANT **[one-action] **SPELL 1** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/36']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/36', 'PZO22001 Starfinder Player Core 294-329::/page/16/Text/62', 'PZO22001 Starfinder Player Core 294-329::/page/7/Text/19']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/36', 'PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/27', 'PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/44']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/27` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/44` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/36` | 0.702581 | **CELLULAR STIMULANT **[one-action] **SPELL 1**  **CONCENTRATE** **MANIPULATE** **VITALITY**  **Traditions** arcane, primal  **Range **120 feet;** Targets** 1 willing living creature that isn't  fatig |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/16/Text/62` | 0.632259 | **Cellular** **Stimulant**H Stimulate the target's body for a short  while at the expense of future energy. |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/19` | 0.620439 | **SPELL NAME **[one-action] **SPELL (RANK)** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/33` | 0.483837 | **EQUIPMENT** **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/23/Text/43` | 0.483837 | **EQUIPMENT** **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/61` | 0.481679 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/59` | 0.481679 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/36` | 0.481679 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/83` | 0.481679 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/86` | 0.481679 | **SPELLS** |

### Query 133
- Text: What does **CHAIN LIGHTNING **[two-actions] **SPELL 6** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/44']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/44', 'PZO22001 Starfinder Player Core 294-329::/page/10/Text/36', 'PZO22001 Starfinder Player Core 294-329::/page/18/Text/25']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/44', 'PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/52', 'PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/36']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/52` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/36` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/44` | 0.756240 | **CHAIN LIGHTNING **[two-actions] **SPELL 6**  **CONCENTRATE** **ELECTRICITY** **MANIPULATE**  **Traditions** arcane, primal  **Range **500 feet;** Targets** 1 creature, plus any number of  additional |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/10/Text/36` | 0.587369 | **Chain Lightning**H An arc of lightning jumps from creature to  creature. |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/18/Text/25` | 0.587369 | **Chain Lightning**H An arc of lightning jumps from creature to  creature. |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/19` | 0.538415 | **SPELL NAME **[one-action] **SPELL (RANK)** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/74` | 0.466438 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/83` | 0.466438 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/60` | 0.466438 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/26` | 0.466438 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/65` | 0.466438 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/86` | 0.466438 | **SPELLS** |

### Query 134
- Text: What does **CHARM **[two-actions] **SPELL 1** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/52']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/52', 'PZO22001 Starfinder Player Core 294-329::/page/7/Text/19', 'PZO22001 Starfinder Player Core 294-329::/page/27/Text/68']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/52', 'PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/6', 'PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/44']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/6` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/44` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/52` | 0.651221 | **CHARM **[two-actions] **SPELL 1**  **CONCENTRATE** **EMOTION** **INCAPACITATION** **MANIPULATE** **MENTAL** **SUBTLE**  **Traditions** arcane, occult, primal **Range **30 feet;** Targets** 1 creatur |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/19` | 0.646610 | **SPELL NAME **[one-action] **SPELL (RANK)** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/27/Text/68` | 0.538692 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/60` | 0.496692 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/36` | 0.496692 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/65` | 0.496692 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/86` | 0.496692 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/26` | 0.496691 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/68` | 0.496691 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/24` | 0.496691 | **SPELLS** |

### Query 135
- Text: What does **CHILLING DARKNESS **[two-actions] **SPELL 3** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/6', 'PZO22001 Starfinder Player Core 294-329::/page/12/Text/25', 'PZO22001 Starfinder Player Core 294-329::/page/7/Text/19']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/6', 'PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/17', 'PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/52']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/17` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/52` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/6` | 0.696213 | **CHILLING DARKNESS **[two-actions] **SPELL 3**  **ATTACK** **COLD** **CONCENTRATE** **DARKNESS** **MANIPULATE** **UNHOLY**  **Traditions** divine  **Range **120 feet;** Targets** 1 creature  **Defens |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/12/Text/25` | 0.607544 | **Chilling Darkness**H Ray of unholy darkness deals cold  damage, dispels light, and harms holy targets. |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/19` | 0.606076 | **SPELL NAME **[one-action] **SPELL (RANK)** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/29/SectionHeader/44` | 0.548425 | **DARKNESS **[three-actions] **SPELL 2**  **CONCENTRATE** **DARKNESS** **MANIPULATE**  **Traditions** arcane, divine, occult, primal **Range **120 feet;** Area** 20-foot burst  **Duration** 1 minute |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/83` | 0.525798 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/86` | 0.525798 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/74` | 0.525798 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/80` | 0.525798 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/26` | 0.525798 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/61` | 0.525798 | **SPELLS** |

### Query 136
- Text: What does **CHRONO PUSH **[two-actions] **SPELL 5** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/17']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/17', 'PZO22001 Starfinder Player Core 294-329::/page/15/Text/42', 'PZO22001 Starfinder Player Core 294-329::/page/7/Text/19']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/17', 'PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/6', 'PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/24']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/6` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/24` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/17` | 0.728147 | **CHRONO PUSH **[two-actions] **SPELL 5**  **ATTACK** **CONCENTRATE** **FORCE** **MANIPULATE**  **Traditions** occult  **Range **500 feet;** Targets** 1 creature **Defense** AC and basic Reflex  You p |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/42` | 0.632036 | **Chrono** **Push ** H Push a target away and damage creatures  nearby. |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/19` | 0.583065 | **SPELL NAME **[one-action] **SPELL (RANK)** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/80` | 0.463753 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/59` | 0.463753 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/65` | 0.463753 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/24` | 0.463753 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/61` | 0.463753 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/86` | 0.463753 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/86` | 0.463753 | **SPELLS** |

### Query 137
- Text: What does **CLAIRAUDIENCE** **SPELL 3** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/24']
- Expected found: `True`
- Expected rank: `17`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/23/Text/43', 'PZO22001 Starfinder Player Core 294-329::/page/7/Text/33', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/26']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/24', 'PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/31', 'PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/17']
- Expanded expected found: `True`
- Expanded expected rank: `17`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/31` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/17` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/23/Text/43` | 0.565497 | **EQUIPMENT** **SPELLS** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/33` | 0.565497 | **EQUIPMENT** **SPELLS** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/26` | 0.560423 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/61` | 0.518423 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/36` | 0.518423 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/60` | 0.518423 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/74` | 0.518423 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/65` | 0.518423 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/80` | 0.518423 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/68` | 0.518423 | **SPELLS** |

### Query 138
- Text: What does **CLAIRVOYANCE** **SPELL 4** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/31']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/7/Text/19', 'PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/31', 'PZO22001 Starfinder Player Core 294-329::/page/7/Text/33']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/31', 'PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/24', 'PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/39']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/24` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/39` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/19` | 0.503402 | **SPELL NAME **[one-action] **SPELL (RANK)** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/31` | 0.503017 | **CLAIRVOYANCE** **SPELL 4**  **CONCENTRATE** **MANIPULATE** **SCRYING**  **Traditions** arcane, occult  **Cast** 1 minute  **Range **500 feet  **Duration** 10 minutes  You create an invisible floatin |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/33` | 0.485973 | **EQUIPMENT** **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/23/Text/43` | 0.443973 | **EQUIPMENT** **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/83` | 0.439637 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/59` | 0.439637 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/86` | 0.439637 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/80` | 0.439637 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/68` | 0.439637 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/74` | 0.439637 | **SPELLS** |

### Query 139
- Text: What does **CLEANSE AFFLICTION **[two-actions] **SPELL 2** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/39']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/39', 'PZO22001 Starfinder Player Core 294-329::/page/7/Text/19', 'PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/47']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/39', 'PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/31', 'PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/47']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/31` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/47` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/39` | 0.643021 | **CLEANSE AFFLICTION **[two-actions] **SPELL 2**  **CONCENTRATE** **HEALING** **MANIPULATE**  **Traditions** divine, occult, primal  **Range **touch; **Targets** 1 willing creature  Gentle restorative |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/19` | 0.588089 | **SPELL NAME **[one-action] **SPELL (RANK)** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/47` | 0.543071 | **CLEANSE CUISINE **[two-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE**  **Traditions** divine, primal  **Range **10 feet;** Area** 1 cubic foot  You transform all food and beverages in the area |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/54` | 0.489010 | **CLEAR MIND **[two-actions] **SPELL 2**  **CONCENTRATE** **HEALING** **MANIPULATE** **MENTAL**  **Traditions** divine, occult, primal  **Range **touch; **Targets** 1 willing creature  You drive menta |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/73` | 0.487689 | **Cleanse Affliction**H Treat a curse, disease, or poison. |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/14/Text/29` | 0.487689 | **Cleanse Affliction**H Treat a curse, disease, or poison. |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/22` | 0.487689 | **Cleanse Affliction**H Treat a curse, disease, or poison. |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/61` | 0.477775 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/86` | 0.477775 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/27/Text/68` | 0.477775 | **SPELLS** |

### Query 140
- Text: What does **CLEANSE CUISINE **[two-actions] **SPELL 1** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/47']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/47', 'PZO22001 Starfinder Player Core 294-329::/page/7/Text/19', 'PZO22001 Starfinder Player Core 294-329::/page/35/Text/68']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/47', 'PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/54', 'PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/39']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/54` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/39` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/47` | 0.727317 | **CLEANSE CUISINE **[two-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE**  **Traditions** divine, primal  **Range **10 feet;** Area** 1 cubic foot  You transform all food and beverages in the area |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/19` | 0.617251 | **SPELL NAME **[one-action] **SPELL (RANK)** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/68` | 0.527683 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/39` | 0.490174 | **CLEANSE AFFLICTION **[two-actions] **SPELL 2**  **CONCENTRATE** **HEALING** **MANIPULATE**  **Traditions** divine, occult, primal  **Range **touch; **Targets** 1 willing creature  Gentle restorative |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/54` | 0.489111 | **CLEAR MIND **[two-actions] **SPELL 2**  **CONCENTRATE** **HEALING** **MANIPULATE** **MENTAL**  **Traditions** divine, occult, primal  **Range **touch; **Targets** 1 willing creature  You drive menta |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/61` | 0.485683 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/80` | 0.485683 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/86` | 0.485683 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/83` | 0.485683 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/59` | 0.485683 | **SPELLS** |

### Query 141
- Text: What does **CLEAR MIND **[two-actions] **SPELL 2** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/54']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/54', 'PZO22001 Starfinder Player Core 294-329::/page/7/Text/19', 'PZO22001 Starfinder Player Core 294-329::/page/9/Text/86']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/54', 'PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/47', 'PZO22001 Starfinder Player Core 294-329::/page/27/Text/62']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/47` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/27/Text/62` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/54` | 0.641298 | **CLEAR MIND **[two-actions] **SPELL 2**  **CONCENTRATE** **HEALING** **MANIPULATE** **MENTAL**  **Traditions** divine, occult, primal  **Range **touch; **Targets** 1 willing creature  You drive menta |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/19` | 0.638796 | **SPELL NAME **[one-action] **SPELL (RANK)** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/86` | 0.580567 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/36` | 0.538567 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/61` | 0.538567 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/83` | 0.538567 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/65` | 0.538567 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/26` | 0.538567 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/68` | 0.538567 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/59` | 0.538567 | **SPELLS** |

### Query 142
- Text: What does **COMMAND **[two-actions] **SPELL 1** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/28/Text/2']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/7/Text/19', 'PZO22001 Starfinder Player Core 294-329::/page/28/Text/2', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/36']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/28/Text/2', 'PZO22001 Starfinder Player Core 294-329::/page/28/Text/7', 'PZO22001 Starfinder Player Core 294-329::/page/28/Text/1']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/28/Text/7` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/28/Text/1` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/19` | 0.686155 | **SPELL NAME **[one-action] **SPELL (RANK)** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/28/Text/2` | 0.656918 | **COMMAND **[two-actions] **SPELL 1**  **AUDITORY** **CONCENTRATE** **LINGUISTIC** **MANIPULATE** **MENTAL**  **Traditions** arcane, divine, occult **Range **30 feet;** Targets** 1 creature  **Defense |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/36` | 0.557568 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/59` | 0.515568 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/24` | 0.515568 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/68` | 0.515568 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/74` | 0.515568 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/80` | 0.515568 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/86` | 0.515568 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/61` | 0.515568 | **SPELLS** |

### Query 143
- Text: What does **CONFUSION **[two-actions] **SPELL 4** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/28/Text/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/28/Text/11', 'PZO22001 Starfinder Player Core 294-329::/page/7/Text/19', 'PZO22001 Starfinder Player Core 294-329::/page/29/SectionHeader/35']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/28/Text/11', 'PZO22001 Starfinder Player Core 294-329::/page/28/Text/10', 'PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/21']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/28/Text/10` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/21` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/28/Text/11` | 0.700819 | **CONFUSION **[two-actions] **SPELL 4**  **CONCENTRATE** **EMOTION** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult **Range **30 feet;** Targets** 1 creature **Defense** Will; **Duration** 1 |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/19` | 0.606446 | **SPELL NAME **[one-action] **SPELL (RANK)** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/29/SectionHeader/35` | 0.541015 | **CURSED METAMORPHOSIS **[two-actions] **SPELL 6**  **CONCENTRATE** **CURSE** **INCAPACITATION** **MANIPULATE** **POLYMORPH**  **Traditions** arcane, occult, primal **Range **30 feet;** Targets** 1 cr |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/80` | 0.489935 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/68` | 0.489935 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/86` | 0.489935 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/74` | 0.489935 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/59` | 0.489935 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/24` | 0.489935 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/26` | 0.489935 | **SPELLS** |

### Query 144
- Text: What does **CONTINGENCY** **SPELL 7** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/21']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0', 'PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/21', 'PZO22001 Starfinder Player Core 294-329::/page/18/SectionHeader/34']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/21', 'PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/29', 'PZO22001 Starfinder Player Core 294-329::/page/28/Text/11']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/29` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/28/Text/11` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0` | 0.567271 | CHAPTER 7: SPELLS |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/21` | 0.549478 | **CONTINGENCY** **SPELL 7**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane  **Cast** 10 minutes **Duration** until your next daily preparations  You prepare a spell that will trigger later. Wh |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/18/SectionHeader/34` | 0.532421 | PRIMAL 7TH-RANK SPELLS |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/33` | 0.479167 | **EQUIPMENT** **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/23/Text/43` | 0.479167 | **EQUIPMENT** **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/83` | 0.478974 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/65` | 0.478974 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/86` | 0.478974 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/74` | 0.478974 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/68` | 0.478974 | **SPELLS** |

### Query 145
- Text: What does **CONTROL MACHINE **[two-actions] **SPELL 5** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/29']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/29', 'PZO22001 Starfinder Player Core 294-329::/page/7/Text/19', 'PZO22001 Starfinder Player Core 294-329::/page/7/Text/33']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/29', 'PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/21', 'PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/39']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/21` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/39` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/29` | 0.663522 | **CONTROL MACHINE **[two-actions] **SPELL 5**  **UNCOMMON** **CONCENTRATE** **INCAPACITATION** **MANIPULATE**  **Traditions** arcane, occult  **Range **30 feet;** Targets** 1 creature or hazard with t |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/19` | 0.614512 | **SPELL NAME **[one-action] **SPELL (RANK)** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/33` | 0.565409 | **EQUIPMENT** **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/23/Text/43` | 0.523409 | **EQUIPMENT** **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/10/Text/17` | 0.492557 | **Control** **Machine**H, U Temporarily take control of a machine. |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/43` | 0.492557 | **Control** **Machine**H, U Temporarily take control of a machine. |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/68` | 0.475036 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/83` | 0.475036 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/59` | 0.475036 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/61` | 0.475036 | **SPELLS** |

### Query 146
- Text: What does **CORROSIVE HAZE **[two-actions] **SPELL 6** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/39']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/39', 'PZO22001 Starfinder Player Core 294-329::/page/10/Text/37', 'PZO22001 Starfinder Player Core 294-329::/page/18/Text/26']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/39', 'PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/29', 'PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/47']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/29` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/47` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/39` | 0.668481 | **CORROSIVE HAZE **[two-actions] **SPELL 6**  **ACID** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal  **Range **120 feet;** Area** 20-foot burst  **Defense** basic Fortitude; **Duratio |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/10/Text/37` | 0.596982 | **Corrosive** **Haze**H Create a cloud of corrosive nanites. |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/18/Text/26` | 0.596982 | **Corrosive** **Haze**H Create a cloud of corrosive nanites. |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/19` | 0.492703 | **SPELL NAME **[one-action] **SPELL (RANK)** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/42` | 0.438519 | **Analyze** **Target**H Gather data about a target's basic physiology. **Daze**H Cloud a creature's mind and possibly stun it. |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/29` | 0.438519 | **Analyze** **Target**H Gather data about a target's basic physiology. **Daze**H Cloud a creature's mind and possibly stun it. |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/33` | 0.428986 | **EQUIPMENT** **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/23/Text/43` | 0.428986 | **EQUIPMENT** **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/80` | 0.428927 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/68` | 0.428927 | **SPELLS** |

### Query 147
- Text: What does **COZY CRASHPAD** **SPELL 3** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/47']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/7/Text/33', 'PZO22001 Starfinder Player Core 294-329::/page/23/Text/43', 'PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/47']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/47', 'PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/39', 'PZO22001 Starfinder Player Core 294-329::/page/29/Text/2']
- Expanded expected found: `True`
- Expanded expected rank: `3`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/39` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/29/Text/2` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/33` | 0.585735 | **EQUIPMENT** **SPELLS** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/23/Text/43` | 0.585735 | **EQUIPMENT** **SPELLS** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/47` | 0.556446 | **COZY CRASHPAD** **SPELL 3**  **CONCENTRATE** **MANIPULATE** **METAL**  **Traditions** arcane, occult  **Cast** 1 minute  **Range **30 feet  **Duration** 12 hours  You shape a shack 20 feet on each s |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/19` | 0.511015 | **SPELL NAME **[one-action] **SPELL (RANK)** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/36` | 0.500266 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/27/Text/68` | 0.500266 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/60` | 0.500266 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/68` | 0.500266 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/80` | 0.500266 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/65` | 0.500266 | **SPELLS** |

### Query 148
- Text: What does **CREATE FOOD** **SPELL 2** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/29/Text/2']
- Expected found: `True`
- Expected rank: `17`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/19/Text/59', 'PZO22001 Starfinder Player Core 294-329::/page/13/Text/74', 'PZO22001 Starfinder Player Core 294-329::/page/33/Text/61']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/29/Text/2', 'PZO22001 Starfinder Player Core 294-329::/page/29/SectionHeader/9', 'PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/47']
- Expanded expected found: `True`
- Expanded expected rank: `17`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/29/SectionHeader/9` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/47` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/59` | 0.589078 | **SPELLS** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/74` | 0.589078 | **SPELLS** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/61` | 0.589078 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/26` | 0.547078 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/83` | 0.547078 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/80` | 0.547078 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/86` | 0.547078 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/65` | 0.547078 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/68` | 0.547078 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/24` | 0.547078 | **SPELLS** |

### Query 149
- Text: What does **CREATE WATER **[two-actions] **SPELL 1** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/29/SectionHeader/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/29/SectionHeader/9', 'PZO22001 Starfinder Player Core 294-329::/page/7/Text/19', 'PZO22001 Starfinder Player Core 294-329::/page/35/Text/68']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/29/SectionHeader/9', 'PZO22001 Starfinder Player Core 294-329::/page/29/Text/2', 'PZO22001 Starfinder Player Core 294-329::/page/29/Text/14']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/29/Text/2` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/29/Text/14` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/29/SectionHeader/9` | 0.750462 | **CREATE WATER **[two-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE** **WATER**  **Traditions** arcane, divine, primal  **Range **0 feet |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/19` | 0.612507 | **SPELL NAME **[one-action] **SPELL (RANK)** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/68` | 0.527620 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/59` | 0.485620 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/86` | 0.485620 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/61` | 0.485620 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/83` | 0.485620 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/24` | 0.485620 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/80` | 0.485620 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/74` | 0.485620 | **SPELLS** |
