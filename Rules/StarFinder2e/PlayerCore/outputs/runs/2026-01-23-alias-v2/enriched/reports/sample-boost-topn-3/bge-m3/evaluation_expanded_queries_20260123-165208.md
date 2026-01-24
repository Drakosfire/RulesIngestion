# RulesLawyer Evaluation Report: bge-m3

## Summary
- Run ID: `None`
- Ruleset ID: `None`
- Document ID: `None`
- Chunk source: `enriched`
- Chunk count: `1390`
- Query count: `150`
- Evaluated queries: `150`
- Coverage: `1.0000`
- MRR: `0.8576`
- hit@1: `0.8133`
- hit@3: `0.8867`
- hit@5: `0.9067`
- hit@10: `0.9400`
- Embeddings reused: `False`
- Graph boost: `0.05` (depth=2, top_k=50, source=top, seed_top_n=3, same_kind_only=False, decay=0.4)

### Expanded Gold Metrics
- Coverage: `1.0000`
- MRR: `0.8839`
- hit@1: `0.8400`
- hit@3: `0.9133`
- hit@5: `0.9333`
- hit@10: `0.9667`

### Expanded Gold Expansion Stats
- Queries with additions: `150`
- Avg added per query: `2.41`
- Max added: `11`
- Addition reasons:
  - graph_depth_1: `362`

### Expanded Gold Delta (Expanded - Strict)
- Coverage Δ: `0.0000`
- MRR Δ: `0.0262`
- hit@1 Δ: `0.0267`
- hit@3 Δ: `0.0267`
- hit@5 Δ: `0.0267`
- hit@10 Δ: `0.0267`

## Timings (ms)
- Embedding: `55358`
- Evaluation: `133`

## Query Details
### Query 0
- Text: What is the rule about CHAPTER 7: SPELLS?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0', 'PZO22001 Starfinder Player Core 294-329::/page/16/SectionHeader/5', 'PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/1']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/1']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/1` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0` | 0.904519 | CHAPTER 7: SPELLS |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/16/SectionHeader/5` | 0.716278 | OCCULT 7TH-RANK SPELLS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/1` | 0.706794 | SPELLS |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/18/SectionHeader/34` | 0.651216 | PRIMAL 7TH-RANK SPELLS |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/10/SectionHeader/57` | 0.644854 | ARCANE 7TH-RANK SPELLS |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/13/SectionHeader/11` | 0.635402 | DIVINE 7TH-RANK SPELLS |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/74` | 0.607134 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/83` | 0.607134 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/61` | 0.607134 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/80` | 0.607134 | **SPELLS** |

### Query 1
- Text: What is the rule about Whether it comes in the form of eldritch artifacts, otherworldly beings, or witchwarpers altering  reality with strange spells, magic brings fantasy and wonder to Starfinder. This chapter explains how  spells work and how spellcasters prepare and cast their spells.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/1', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/4', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/7']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/1', 'PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/3']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/3` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/1` | 1.000487 | Whether it comes in the form of eldritch artifacts, otherworldly beings, or witchwarpers altering  reality with strange spells, magic brings fantasy and wonder to Starfinder. This chapter explains how |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/4` | 0.704919 | With special gestures and utterances, a spellcaster can  call forth mystic energies, warp the mind, protect themself  against danger, or even create something from nothing.  Each class has its own met |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/7` | 0.704388 | Arcane spellcasters use logic and  rationality to categorize the magic inherent  in the world around them. Because of its far-reaching  approach, the arcane tradition has the broadest spell  list, tho |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/3` | 0.671486 | Even with the widespread presence of technology,  spellcasters can be found in every corner of the galaxy.  Some spellcasters draw magic from other realities, some  from their mystical connections to |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/8` | 0.655629 | If you're a prepared spellcaster—such as a technomancer  (see *Starfinder Tech Core*)—you must spend time each day  preparing spells for that day. At the start of your daily  preparations, you select |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/4` | 0.654715 | Spellcasting creates obvious sensory manifestations, such  as bright lights, crackling sounds, and sharp smells from the  gathering magic. Nearly all spells manifest a spell signature—a  colorful, glo |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/3` | 0.654653 | Your class determines which tradition of magic your spells use. In some cases, such as when a mystic gains spells from  their connection or when a witchwarper learns spells from their paradox, you mig |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/16` | 0.625082 | Both prepared and spontaneous spellcasters can cast a spell  at a higher spell rank than that listed for the spell. This is  called heightening the spell. A prepared spellcaster can  heighten a spell |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/3` | 0.623915 | The casting of a spell can range from a simple word of magical  might that creates a fleeting effect to a complex process  taking hours to cast and producing a long-term impact.  Casting a spell requi |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/2` | 0.620741 | The grand variety of spells includes those in the following pages and far more. Taught at magical  academies, drawn from other worlds, bestowed by mystical connections, and granted by all manner of  u |

### Query 2
- Text: What is the rule about Even with the widespread presence of technology,  spellcasters can be found in every corner of the galaxy.  Some spellcasters draw magic from other realities, some  from their mystical connections to cosmic forces, and  others rewrite the underlying code of the universe to cast  their spells.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/3']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/3', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/7', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/4']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/3', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/4', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/1']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/4` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/1` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/3` | 0.969672 | Even with the widespread presence of technology,  spellcasters can be found in every corner of the galaxy.  Some spellcasters draw magic from other realities, some  from their mystical connections to |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/7` | 0.734450 | Arcane spellcasters use logic and  rationality to categorize the magic inherent  in the world around them. Because of its far-reaching  approach, the arcane tradition has the broadest spell  list, tho |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/4` | 0.726869 | With special gestures and utterances, a spellcaster can  call forth mystic energies, warp the mind, protect themself  against danger, or even create something from nothing.  Each class has its own met |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/1` | 0.656304 | Whether it comes in the form of eldritch artifacts, otherworldly beings, or witchwarpers altering  reality with strange spells, magic brings fantasy and wonder to Starfinder. This chapter explains how |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/2` | 0.644256 | The grand variety of spells includes those in the following pages and far more. Taught at magical  academies, drawn from other worlds, bestowed by mystical connections, and granted by all manner of  u |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/3` | 0.637051 | Your class determines which tradition of magic your spells use. In some cases, such as when a mystic gains spells from  their connection or when a witchwarper learns spells from their paradox, you mig |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/3` | 0.635440 | The casting of a spell can range from a simple word of magical  might that creates a fleeting effect to a complex process  taking hours to cast and producing a long-term impact.  Casting a spell requi |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/12` | 0.630023 | After Triune's Signal connected cultures across the  Universe, the peoples of the galaxy have learned more  than ever before about the Universe's composition  thanks to science and technology. As tech |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/4` | 0.625724 | Spellcasting creates obvious sensory manifestations, such  as bright lights, crackling sounds, and sharp smells from the  gathering magic. Nearly all spells manifest a spell signature—a  colorful, glo |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/11` | 0.622487 | beyond the Universe. Mystics connected with the cosmic  forces of healing and shadows are divine spellcasters. |

### Query 3
- Text: What is the rule about With special gestures and utterances, a spellcaster can  call forth mystic energies, warp the mind, protect themself  against danger, or even create something from nothing.  Each class has its own method of learning, preparing,  and casting spells, and every individual spell produces a  specific effect, so learning new spells gives a spellcaster  an increasing array of options to accomplish their goals.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/4', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/3', 'PZO22001 Starfinder Player Core 294-329::/page/4/Text/4']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/4', 'PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/5', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/3']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/5` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/3` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/4` | 0.965533 | With special gestures and utterances, a spellcaster can  call forth mystic energies, warp the mind, protect themself  against danger, or even create something from nothing.  Each class has its own met |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/3` | 0.761513 | Your class determines which tradition of magic your spells use. In some cases, such as when a mystic gains spells from  their connection or when a witchwarper learns spells from their paradox, you mig |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/4` | 0.743722 | Spellcasting creates obvious sensory manifestations, such  as bright lights, crackling sounds, and sharp smells from the  gathering magic. Nearly all spells manifest a spell signature—a  colorful, glo |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/3` | 0.708987 | The casting of a spell can range from a simple word of magical  might that creates a fleeting effect to a complex process  taking hours to cast and producing a long-term impact.  Casting a spell requi |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/3` | 0.706973 | Even with the widespread presence of technology,  spellcasters can be found in every corner of the galaxy.  Some spellcasters draw magic from other realities, some  from their mystical connections to |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/6` | 0.668930 | Characters of spellcasting classes can cast a number of spells  each day; the spells you can cast in a day are referred to as  spell slots. At 1st level, a character has only a small number  of 1st-ra |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/21` | 0.668351 | If you get focus spells from a class or other source that  doesn't grant spellcasting ability, the ability that gives you  focus spells also provides your proficiency for your spell  attack modifier a |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/5` | 0.664388 | Spells can vary in how many actions they take, as shown in  the spell's stat block. You cast cantrips, spells from spell slots,  and focus spells using the same process, but must expend the  spell whe |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/14` | 0.660219 | If you're a spontaneous spellcaster—such as a mystic—you  choose which spell from your spell repertoire that you're  using a spell slot for at the moment you decide to cast it. This  provides you with |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/16` | 0.659381 | Both prepared and spontaneous spellcasters can cast a spell  at a higher spell rank than that listed for the spell. This is  called heightening the spell. A prepared spellcaster can  heighten a spell |

### Query 4
- Text: What is the rule about SPELL SLOTS?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/5', 'PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/1', 'PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/23']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/5', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/4', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/6']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/4` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/6` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/5` | 0.858990 | SPELL SLOTS |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/1` | 0.659501 | SPELLS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/23` | 0.646041 | SPELL ATTACKS |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/13` | 0.583730 | SUSTAINING SPELLS |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0` | 0.580034 | CHAPTER 7: SPELLS |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/7/SectionHeader/3` | 0.557830 | IDENTIFYING SPELLS |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/8/SectionHeader/1` | 0.552791 | SPELL LISTS |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/88` | 0.551476 | **Spells** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/76` | 0.551476 | **Spells** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/38` | 0.551476 | **Spells** |

### Query 5
- Text: What is the rule about Characters of spellcasting classes can cast a number of spells  each day; the spells you can cast in a day are referred to as  spell slots. At 1st level, a character has only a small number  of 1st-rank spell slots per day, but as you advance in level, you  gain more spell slots of higher rank. A spell's rank indicates  its overall power, from 1 to 10.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/6', 'PZO22001 Starfinder Player Core 294-329::/page/4/Text/5', 'PZO22001 Starfinder Player Core 294-329::/page/4/Text/1']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/6', 'PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/5', 'PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/7']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/5` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/7` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/6` | 1.010703 | Characters of spellcasting classes can cast a number of spells  each day; the spells you can cast in a day are referred to as  spell slots. At 1st level, a character has only a small number  of 1st-ra |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/5` | 0.772714 | Spells can vary in how many actions they take, as shown in  the spell's stat block. You cast cantrips, spells from spell slots,  and focus spells using the same process, but must expend the  spell whe |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/1` | 0.765790 | You can't use your spell slots to cast your innate spells, but  you might have an innate spell and also be able to prepare  or cast the same spell through your class. You also can't  heighten innate s |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/26` | 0.718465 | Certain spells are natural to your character, typically coming  from your ancestry or a magic item. They're called innate  spells. Innate spells don't let you qualify for abilities that  require you t |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/1` | 0.700308 | so long as they know the spell at that rank (see Heightened  Spontaneous Spells below). When you heighten your spell,  the spell's rank increases to match the higher rank of the  spell slot you've pre |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/14` | 0.691553 | If you're a spontaneous spellcaster—such as a mystic—you  choose which spell from your spell repertoire that you're  using a spell slot for at the moment you decide to cast it. This  provides you with |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/10` | 0.682676 | The title of a cantrip's stat block says "Cantrip" instead of  "Spell", and the spell has the cantrip trait. Casting a cantrip  doesn't use up your spell slots; you can cast a cantrip at will,  any nu |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/4` | 0.681685 | Sometimes you need to identify a spell, especially if its  effects aren't obvious right away. If you notice a spell  being cast, and you have that spell in your repertoire  or prepared it that day (ev |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/6` | 0.680734 | Many spontaneous spellcasting classes provide abilities  like the signature spells class feature, which allows you to  cast a limited number of spells as heightened versions even if  you know the spel |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/8` | 0.673077 | If you're a prepared spellcaster—such as a technomancer  (see *Starfinder Tech Core*)—you must spend time each day  preparing spells for that day. At the start of your daily  preparations, you select |

### Query 6
- Text: What is the rule about PREPARED SPELLS?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/7', 'PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/1', 'PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/7', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/8', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/6']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/8` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/6` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/7` | 0.828217 | PREPARED SPELLS |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/1` | 0.646275 | SPELLS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0` | 0.641811 | CHAPTER 7: SPELLS |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/13` | 0.598398 | SUSTAINING SPELLS |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/15` | 0.595534 | HEIGHTENED SPELLS |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/7/SectionHeader/3` | 0.573412 | IDENTIFYING SPELLS |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/5` | 0.569091 | SPELL SLOTS |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/16/SectionHeader/57` | 0.551362 | PRIMAL 1ST-RANK SPELLS |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/65` | 0.549179 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/27/Text/68` | 0.549179 | **SPELLS** |

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
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/8` | 0.996219 | If you're a prepared spellcaster—such as a technomancer  (see *Starfinder Tech Core*)—you must spend time each day  preparing spells for that day. At the start of your daily  preparations, you select |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/9` | 0.745000 | Each prepared spell is expended after a single casting,  so if you want to cast a particular spell more than once in  a day, you need to prepare that spell multiple times. The  exception to this rule |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/10` | 0.735306 | You might gain an ability that allows you to swap  prepared spells or perform other aspects of preparing spells  at different times throughout the day, but only your daily  preparation counts for the |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/6` | 0.666852 | Characters of spellcasting classes can cast a number of spells  each day; the spells you can cast in a day are referred to as  spell slots. At 1st level, a character has only a small number  of 1st-ra |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/6/Text/16` | 0.660172 | If a spell's duration says it lasts until your next daily  preparations, on the next day you can refrain from preparing  a new spell in that spell's slot. (If you are a spontaneous caster,  you can in |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/14` | 0.656155 | If you're a spontaneous spellcaster—such as a mystic—you  choose which spell from your spell repertoire that you're  using a spell slot for at the moment you decide to cast it. This  provides you with |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/21` | 0.655566 | **CONTINGENCY** **SPELL 7**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane  **Cast** 10 minutes **Duration** until your next daily preparations  You prepare a spell that will trigger later. Wh |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/26` | 0.645773 | Certain spells are natural to your character, typically coming  from your ancestry or a magic item. They're called innate  spells. Innate spells don't let you qualify for abilities that  require you t |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/3` | 0.643661 | Your class determines which tradition of magic your spells use. In some cases, such as when a mystic gains spells from  their connection or when a witchwarper learns spells from their paradox, you mig |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/4` | 0.640806 | Sometimes you need to identify a spell, especially if its  effects aren't obvious right away. If you notice a spell  being cast, and you have that spell in your repertoire  or prepared it that day (ev |

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
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/9` | 1.030242 | Each prepared spell is expended after a single casting,  so if you want to cast a particular spell more than once in  a day, you need to prepare that spell multiple times. The  exception to this rule |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/10` | 0.855906 | The title of a cantrip's stat block says "Cantrip" instead of  "Spell", and the spell has the cantrip trait. Casting a cantrip  doesn't use up your spell slots; you can cast a cantrip at will,  any nu |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/5` | 0.805661 | Spells can vary in how many actions they take, as shown in  the spell's stat block. You cast cantrips, spells from spell slots,  and focus spells using the same process, but must expend the  spell whe |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/26` | 0.737915 | Certain spells are natural to your character, typically coming  from your ancestry or a magic item. They're called innate  spells. Innate spells don't let you qualify for abilities that  require you t |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/10` | 0.719177 | You might gain an ability that allows you to swap  prepared spells or perform other aspects of preparing spells  at different times throughout the day, but only your daily  preparation counts for the |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/8` | 0.695187 | If you're a prepared spellcaster—such as a technomancer  (see *Starfinder Tech Core*)—you must spend time each day  preparing spells for that day. At the start of your daily  preparations, you select |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/6/Text/16` | 0.694716 | If a spell's duration says it lasts until your next daily  preparations, on the next day you can refrain from preparing  a new spell in that spell's slot. (If you are a spontaneous caster,  you can in |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/17` | 0.682153 | Each spell uses the following format. Entries appear only  when applicable, so not all spells will have every entry  described here. The spell's name line also lists the type  of spell if it's a cantr |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/22` | 0.676755 | **Cast** Spells that take longer than a single turn to cast include  this entry to list the time required, such as "1 minute." If  the spell has a cost, locus, requirements, or a trigger, that  inform |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/21` | 0.667551 | **CONTINGENCY** **SPELL 7**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane  **Cast** 10 minutes **Duration** until your next daily preparations  You prepare a spell that will trigger later. Wh |

### Query 9
- Text: What is the rule about You might gain an ability that allows you to swap  prepared spells or perform other aspects of preparing spells  at different times throughout the day, but only your daily  preparation counts for the purpose of effects that last until  the next time you prepare spells.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/10', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/9', 'PZO22001 Starfinder Player Core 294-329::/page/6/Text/16']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/10', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/9', 'PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/11']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/9` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/11` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/10` | 0.960837 | You might gain an ability that allows you to swap  prepared spells or perform other aspects of preparing spells  at different times throughout the day, but only your daily  preparation counts for the |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/9` | 0.772246 | Each prepared spell is expended after a single casting,  so if you want to cast a particular spell more than once in  a day, you need to prepare that spell multiple times. The  exception to this rule |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/6/Text/16` | 0.723584 | If a spell's duration says it lasts until your next daily  preparations, on the next day you can refrain from preparing  a new spell in that spell's slot. (If you are a spontaneous caster,  you can in |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/8` | 0.683472 | If you're a prepared spellcaster—such as a technomancer  (see *Starfinder Tech Core*)—you must spend time each day  preparing spells for that day. At the start of your daily  preparations, you select |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/26` | 0.635346 | Certain spells are natural to your character, typically coming  from your ancestry or a magic item. They're called innate  spells. Innate spells don't let you qualify for abilities that  require you t |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/14` | 0.627483 | If you're a spontaneous spellcaster—such as a mystic—you  choose which spell from your spell repertoire that you're  using a spell slot for at the moment you decide to cast it. This  provides you with |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/3` | 0.626100 | Your class determines which tradition of magic your spells use. In some cases, such as when a mystic gains spells from  their connection or when a witchwarper learns spells from their paradox, you mig |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/6` | 0.624862 | Characters of spellcasting classes can cast a number of spells  each day; the spells you can cast in a day are referred to as  spell slots. At 1st level, a character has only a small number  of 1st-ra |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/6/Text/14` | 0.614479 | If the spell's duration is "sustained," it lasts until the end of  your next turn unless you use the Sustain action (page 411)  on that turn to extend the duration of that spell. |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/6/Text/4` | 0.612031 | Many spellcasters can gain access to spellshape  actions, typically by selecting spellshape feats.  Spellshape actions tweak the properties of your  spells. You must use a spellshape action directly |

### Query 10
- Text: What is the rule about **SPELLCASTING IN STARFINDER**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/11', 'PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/2', 'PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/21']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/11', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/12', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/10']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/12` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/10` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/11` | 0.864402 | **SPELLCASTING IN STARFINDER** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/2` | 0.634243 | CASTING SPELLS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/21` | 0.612569 | SPELLCASTERS WITH FOCUS  SPELLS |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/20` | 0.548823 | NON-SPELLCASTERS WITH  FOCUS SPELLS |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/5` | 0.529279 | SPELL SLOTS |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/3` | 0.515968 | **SPELLSHAPE** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/1` | 0.508799 | Whether it comes in the form of eldritch artifacts, otherworldly beings, or witchwarpers altering  reality with strange spells, magic brings fantasy and wonder to Starfinder. This chapter explains how |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/10/Text/50` | 0.498277 | **Scrying**U Spy on a creature you choose. |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/68` | 0.498277 | **Scrying**U Spy on a creature you choose. |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/83` | 0.496889 | **SPELLS** |

### Query 11
- Text: What is the rule about After Triune's Signal connected cultures across the  Universe, the peoples of the galaxy have learned more  than ever before about the Universe's composition  thanks to science and technology. As technology  improves and creates mass-market marvels rivaling  what was once only possible for a powerful spellcaster,  magic is more static, with arcane universities,  occult societies, and religious orders preserving  ancient techniques and tomes into the modern  era. Many specialty tech items incorporate hybrid  magitechnology, and most spellcasters carry a backup  gun or other tech gear on them for when they run  out of spells. Magic and technology coexist, but most  spellcasters use analog spellcasting, and blending the  two together to create a hybrid item requires training.  Only a few spellcasters mix magic with technology they're seen as mavericks by most established magical  institutions. Technomancers and spellcasters who  have learned to command machines or connect with  computers using magic blaze a trail few have explored.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/12']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/12', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/3', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/3']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/12', 'PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/13', 'PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/11']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/13` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/11` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/12` | 0.973560 | After Triune's Signal connected cultures across the  Universe, the peoples of the galaxy have learned more  than ever before about the Universe's composition  thanks to science and technology. As tech |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/3` | 0.641306 | Even with the widespread presence of technology,  spellcasters can be found in every corner of the galaxy.  Some spellcasters draw magic from other realities, some  from their mystical connections to |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/3` | 0.632077 | Your class determines which tradition of magic your spells use. In some cases, such as when a mystic gains spells from  their connection or when a witchwarper learns spells from their paradox, you mig |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/7` | 0.589796 | Arcane spellcasters use logic and  rationality to categorize the magic inherent  in the world around them. Because of its far-reaching  approach, the arcane tradition has the broadest spell  list, tho |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/4` | 0.556846 | With special gestures and utterances, a spellcaster can  call forth mystic energies, warp the mind, protect themself  against danger, or even create something from nothing.  Each class has its own met |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/8` | 0.550186 | If you're a prepared spellcaster—such as a technomancer  (see *Starfinder Tech Core*)—you must spend time each day  preparing spells for that day. At the start of your daily  preparations, you select |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/11` | 0.547997 | beyond the Universe. Mystics connected with the cosmic  forces of healing and shadows are divine spellcasters. |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/17` | 0.543336 | Magic with the illusion trait creates false sensory stimuli.  Sometimes illusions allow creatures a chance to disbelieve  the spell, which lets the creature ignore the spell if it succeeds  at doing s |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/2` | 0.542726 | The grand variety of spells includes those in the following pages and far more. Taught at magical  academies, drawn from other worlds, bestowed by mystical connections, and granted by all manner of  u |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/18` | 0.537977 | An instinctual connection to and faith in the  world, the cycle of day and night, the turning  of the seasons, and the natural selection of predator and  prey drive the primal tradition. Mystics conne |

### Query 12
- Text: What is the rule about SPONTANEOUS SPELLS?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/13', 'PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/13', 'PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/5']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/13', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/12', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/14']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/12` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/14` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/13` | 0.800037 | SPONTANEOUS SPELLS |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/13` | 0.632768 | SUSTAINING SPELLS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/5` | 0.604383 | SPELL SLOTS |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0` | 0.561410 | CHAPTER 7: SPELLS |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/1` | 0.550703 | SPELLS |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/12` | 0.544548 | FOCUS SPELLS |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/4` | 0.538001 | Heightened Spontaneous Spells |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/23` | 0.530274 | SPELL ATTACKS |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/26` | 0.529491 | Certain spells are natural to your character, typically coming  from your ancestry or a magic item. They're called innate  spells. Innate spells don't let you qualify for abilities that  require you t |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/7/SectionHeader/16` | 0.529396 | READING SPELLS |

### Query 13
- Text: What is the rule about If you're a spontaneous spellcaster—such as a mystic—you  choose which spell from your spell repertoire that you're  using a spell slot for at the moment you decide to cast it. This  provides you with more freedom in your spellcasting, but you  have fewer spells in your spell repertoire, as determined by  your character level and class. When you make your daily  preparations, all your spell slots are refreshed, but you don't  get to change the spells in your repertoire.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/14']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/14', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/3', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/26']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/14', 'PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/13', 'PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/15']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/13` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/15` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/14` | 1.001622 | If you're a spontaneous spellcaster—such as a mystic—you  choose which spell from your spell repertoire that you're  using a spell slot for at the moment you decide to cast it. This  provides you with |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/3` | 0.794969 | Your class determines which tradition of magic your spells use. In some cases, such as when a mystic gains spells from  their connection or when a witchwarper learns spells from their paradox, you mig |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/26` | 0.751307 | Certain spells are natural to your character, typically coming  from your ancestry or a magic item. They're called innate  spells. Innate spells don't let you qualify for abilities that  require you t |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/5` | 0.702811 | If you're a spontaneous spellcaster, you must know a spell at  the specific rank that you want to cast it in order to heighten  it. You can add a spell to your spell repertoire at more than  a single |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/7` | 0.701433 | As a spontaneous caster, you can also choose to cast  a lower-rank spell using a higher-rank spell slot without  heightening it or knowing it at a higher rank. This casts the  spell at the rank you kn |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/6/Text/16` | 0.696610 | If a spell's duration says it lasts until your next daily  preparations, on the next day you can refrain from preparing  a new spell in that spell's slot. (If you are a spontaneous caster,  you can in |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/1` | 0.688910 | You can't use your spell slots to cast your innate spells, but  you might have an innate spell and also be able to prepare  or cast the same spell through your class. You also can't  heighten innate s |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/6` | 0.679871 | Characters of spellcasting classes can cast a number of spells  each day; the spells you can cast in a day are referred to as  spell slots. At 1st level, a character has only a small number  of 1st-ra |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/21` | 0.678651 | If you get focus spells from a class or other source that  doesn't grant spellcasting ability, the ability that gives you  focus spells also provides your proficiency for your spell  attack modifier a |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/16` | 0.673082 | Both prepared and spontaneous spellcasters can cast a spell  at a higher spell rank than that listed for the spell. This is  called heightening the spell. A prepared spellcaster can  heighten a spell |

### Query 14
- Text: What is the rule about HEIGHTENED SPELLS?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/15']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/15', 'PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/13', 'PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/4']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/15', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/14', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/16']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/14` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/16` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/15` | 0.837925 | HEIGHTENED SPELLS |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/13` | 0.661323 | SUSTAINING SPELLS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/4` | 0.618971 | Heightened Spontaneous Spells |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0` | 0.568898 | CHAPTER 7: SPELLS |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/7` | 0.564829 | PREPARED SPELLS |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/7/SectionHeader/3` | 0.561844 | IDENTIFYING SPELLS |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/1` | 0.557979 | SPELLS |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/12` | 0.539954 | FOCUS SPELLS |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/7/SectionHeader/16` | 0.533790 | READING SPELLS |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/1` | 0.531040 | so long as they know the spell at that rank (see Heightened  Spontaneous Spells below). When you heighten your spell,  the spell's rank increases to match the higher rank of the  spell slot you've pre |

### Query 15
- Text: What is the rule about Both prepared and spontaneous spellcasters can cast a spell  at a higher spell rank than that listed for the spell. This is  called heightening the spell. A prepared spellcaster can  heighten a spell by preparing it in a higher-rank slot than  its normal spell rank, while a spontaneous spellcaster can  heighten a spell by casting it using a higher-rank spell slot,?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/16']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/16', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/1', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/5']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/16', 'PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/15', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/18']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/15` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/18` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/16` | 0.989088 | Both prepared and spontaneous spellcasters can cast a spell  at a higher spell rank than that listed for the spell. This is  called heightening the spell. A prepared spellcaster can  heighten a spell |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/1` | 0.838928 | so long as they know the spell at that rank (see Heightened  Spontaneous Spells below). When you heighten your spell,  the spell's rank increases to match the higher rank of the  spell slot you've pre |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/5` | 0.794402 | If you're a spontaneous spellcaster, you must know a spell at  the specific rank that you want to cast it in order to heighten  it. You can add a spell to your spell repertoire at more than  a single |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/7` | 0.737440 | As a spontaneous caster, you can also choose to cast  a lower-rank spell using a higher-rank spell slot without  heightening it or knowing it at a higher rank. This casts the  spell at the rank you kn |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/1` | 0.714130 | You can't use your spell slots to cast your innate spells, but  you might have an innate spell and also be able to prepare  or cast the same spell through your class. You also can't  heighten innate s |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/2` | 0.711912 | In addition, many spells have additional specific benefits  when they are heightened, such as increased damage. These  extra benefits are described at the end of the spell's stat  block. Some heighten |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/14` | 0.688784 | If you're a spontaneous spellcaster—such as a mystic—you  choose which spell from your spell repertoire that you're  using a spell slot for at the moment you decide to cast it. This  provides you with |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/4` | 0.687050 | Sometimes you need to identify a spell, especially if its  effects aren't obvious right away. If you notice a spell  being cast, and you have that spell in your repertoire  or prepared it that day (ev |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/11` | 0.661110 | A cantrip is always automatically heightened to half your  level, rounded up. For a typical spellcaster, this means its  rank is equal to the highest rank of spell slot you have. |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/26` | 0.658312 | Certain spells are natural to your character, typically coming  from your ancestry or a magic item. They're called innate  spells. Innate spells don't let you qualify for abilities that  require you t |

### Query 16
- Text: Summarize **INTRODUCTION**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/18']
- Expected found: `True`
- Expected rank: `14`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/9/Text/80', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/30', 'PZO22001 Starfinder Player Core 294-329::/page/11/Text/77']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/18', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/16', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/19']
- Expanded expected found: `True`
- Expanded expected rank: `14`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/16` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/19` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/80` | 0.913367 | **INTRODUCTION** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/30` | 0.913367 | **INTRODUCTION** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/77` | 0.913367 | **INTRODUCTION** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/28` | 0.871367 | **INTRODUCTION** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/20` | 0.871367 | **INTRODUCTION** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/68` | 0.871367 | **INTRODUCTION** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/59` | 0.871367 | **INTRODUCTION** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/54` | 0.871367 | **INTRODUCTION** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/55` | 0.871367 | **INTRODUCTION** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/27/Text/62` | 0.871367 | **INTRODUCTION** |

### Query 17
- Text: What is the rule about **ANCESTRIES & ** **BACKGROUNDS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/19']
- Expected found: `True`
- Expected rank: `15`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/7/Text/29', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/21', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/31']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/19', 'PZO22001 Starfinder Player Core 294-329::/page/27/Text/63', 'PZO22001 Starfinder Player Core 294-329::/page/17/Text/81', 'PZO22001 Starfinder Player Core 294-329::/page/13/Text/69', 'PZO22001 Starfinder Player Core 294-329::/page/15/Text/75', 'PZO22001 Starfinder Player Core 294-329::/page/23/Text/39', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/18', 'PZO22001 Starfinder Player Core 294-329::/page/33/Text/56', 'PZO22001 Starfinder Player Core 294-329::/page/35/Text/63', 'PZO22001 Starfinder Player Core 294-329::/page/29/Text/60', 'PZO22001 Starfinder Player Core 294-329::/page/31/Text/55', 'PZO22001 Starfinder Player Core 294-329::/page/19/Text/54']
- Expanded expected found: `True`
- Expanded expected rank: `4`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/27/Text/63` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/17/Text/81` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/13/Text/69` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/15/Text/75` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/23/Text/39` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/18` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/33/Text/56` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/35/Text/63` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/29/Text/60` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/31/Text/55` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/19/Text/54` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/29` | 0.830013 | **ANCESTRIES & ** **BACKGROUNDS** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/21` | 0.830013 | **ANCESTRIES & ** **BACKGROUNDS** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/31` | 0.830013 | **ANCESTRIES & ** **BACKGROUNDS** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/55` | 0.800013 | **ANCESTRIES & ** **BACKGROUNDS** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/27/Text/63` | 0.800013 | **ANCESTRIES & ** **BACKGROUNDS** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/60` | 0.800013 | **ANCESTRIES & ** **BACKGROUNDS** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/78` | 0.800013 | **ANCESTRIES & ** **BACKGROUNDS** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/56` | 0.800013 | **ANCESTRIES & ** **BACKGROUNDS** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/69` | 0.800013 | **ANCESTRIES & ** **BACKGROUNDS** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/81` | 0.800013 | **ANCESTRIES & ** **BACKGROUNDS** |

### Query 18
- Text: Summarize **CLASSES**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/20']
- Expected found: `True`
- Expected rank: `15`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/11/Text/79', 'PZO22001 Starfinder Player Core 294-329::/page/7/Text/30', 'PZO22001 Starfinder Player Core 294-329::/page/23/Text/40']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/20', 'PZO22001 Starfinder Player Core 294-329::/page/17/Text/82', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/32', 'PZO22001 Starfinder Player Core 294-329::/page/31/Text/56', 'PZO22001 Starfinder Player Core 294-329::/page/27/Text/64', 'PZO22001 Starfinder Player Core 294-329::/page/23/Text/40', 'PZO22001 Starfinder Player Core 294-329::/page/15/Text/76', 'PZO22001 Starfinder Player Core 294-329::/page/33/Text/57', 'PZO22001 Starfinder Player Core 294-329::/page/11/Text/79', 'PZO22001 Starfinder Player Core 294-329::/page/19/Text/55', 'PZO22001 Starfinder Player Core 294-329::/page/13/Text/70', 'PZO22001 Starfinder Player Core 294-329::/page/35/Text/64']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/17/Text/82` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/32` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/31/Text/56` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/27/Text/64` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/23/Text/40` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/15/Text/76` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/33/Text/57` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/11/Text/79` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/19/Text/55` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/13/Text/70` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/35/Text/64` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/79` | 0.866254 | **CLASSES** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/30` | 0.866254 | **CLASSES** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/23/Text/40` | 0.866254 | **CLASSES** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/61` | 0.836254 | **CLASSES** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/56` | 0.836254 | **CLASSES** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/82` | 0.836254 | **CLASSES** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/64` | 0.836254 | **CLASSES** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/70` | 0.836254 | **CLASSES** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/27/Text/64` | 0.836254 | **CLASSES** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/76` | 0.836254 | **CLASSES** |

### Query 19
- Text: What is the rule about **SKILLS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/21']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/21', 'PZO22001 Starfinder Player Core 294-329::/page/7/Text/31', 'PZO22001 Starfinder Player Core 294-329::/page/23/Text/41']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/21', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/22', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/20']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/22` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/20` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/21` | 0.777771 | **SKILLS** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/31` | 0.777771 | **SKILLS** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/23/Text/41` | 0.777771 | **SKILLS** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/23` | 0.735771 | **SKILLS** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/58` | 0.735771 | **SKILLS** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/83` | 0.735771 | **SKILLS** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/83` | 0.735771 | **SKILLS** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/71` | 0.735771 | **SKILLS** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/77` | 0.735771 | **SKILLS** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/57` | 0.735771 | **SKILLS** |

### Query 20
- Text: What is the rule about **FEATS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/22']
- Expected found: `True`
- Expected rank: `10`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/35/Text/66', 'PZO22001 Starfinder Player Core 294-329::/page/17/Text/84', 'PZO22001 Starfinder Player Core 294-329::/page/13/Text/72']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/22', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/23', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/21']
- Expanded expected found: `True`
- Expanded expected rank: `10`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/23` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/21` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/66` | 0.735680 | **FEATS** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/72` | 0.735680 | **FEATS** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/84` | 0.735680 | **FEATS** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/78` | 0.693680 | **FEATS** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/59` | 0.693680 | **FEATS** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/34` | 0.693680 | **FEATS** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/58` | 0.693680 | **FEATS** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/32` | 0.693680 | **FEATS** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/23/Text/42` | 0.693680 | **FEATS** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/22` | 0.693680 | **FEATS** |

### Query 21
- Text: Summarize **EQUIPMENT**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/23']
- Expected found: `True`
- Expected rank: `10`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/33/Text/60', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/35', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/25']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/23', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/24', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/22']
- Expanded expected found: `True`
- Expanded expected rank: `10`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/24` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/22` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/60` | 0.915652 | **EQUIPMENT** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/35` | 0.915652 | **EQUIPMENT** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/25` | 0.915652 | **EQUIPMENT** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/82` | 0.873652 | **EQUIPMENT** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/85` | 0.873652 | **EQUIPMENT** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/85` | 0.873652 | **EQUIPMENT** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/79` | 0.873652 | **EQUIPMENT** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/64` | 0.873652 | **EQUIPMENT** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/73` | 0.873652 | **EQUIPMENT** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/23` | 0.873652 | **EQUIPMENT** |

### Query 22
- Text: What is the rule about **SPELLS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/24']
- Expected found: `True`
- Expected rank: `11`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/33/Text/61', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/36', 'PZO22001 Starfinder Player Core 294-329::/page/17/Text/86']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/24', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/23', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/25']
- Expanded expected found: `True`
- Expanded expected rank: `11`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/23` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/25` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/86` | 0.806592 | **SPELLS** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/61` | 0.806592 | **SPELLS** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/36` | 0.806592 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/80` | 0.764592 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/74` | 0.764592 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/83` | 0.764592 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/60` | 0.764592 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/86` | 0.764592 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/26` | 0.764592 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/27/Text/68` | 0.764592 | **SPELLS** |

### Query 23
- Text: What is the rule about **Spell Lists**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/25']
- Expected found: `True`
- Expected rank: `11`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/19/Text/60', 'PZO22001 Starfinder Player Core 294-329::/page/23/Text/44', 'PZO22001 Starfinder Player Core 294-329::/page/17/Text/87']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/25', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/26', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/24']
- Expanded expected found: `True`
- Expanded expected rank: `11`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/26` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/24` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/60` | 0.782608 | **Spell Lists** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/23/Text/44` | 0.782608 | **Spell Lists** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/87` | 0.782608 | **Spell Lists** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/81` | 0.740608 | **Spell Lists** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/75` | 0.740608 | **Spell Lists** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/62` | 0.740608 | **Spell Lists** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/27/Text/69` | 0.740608 | **Spell Lists** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/27` | 0.740608 | **Spell Lists** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/61` | 0.740608 | **Spell Lists** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/66` | 0.740608 | **Spell Lists** |

### Query 24
- Text: What is the rule about **Spells**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/26']
- Expected found: `True`
- Expected rank: `7`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/38', 'PZO22001 Starfinder Player Core 294-329::/page/11/Text/85', 'PZO22001 Starfinder Player Core 294-329::/page/13/Text/76']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/26', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/25', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/27']
- Expanded expected found: `True`
- Expanded expected rank: `7`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/25` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/27` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/38` | 0.801543 | **Spells** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/76` | 0.801543 | **Spells** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/85` | 0.801543 | **Spells** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/62` | 0.759543 | **Spells** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/82` | 0.759543 | **Spells** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/70` | 0.759543 | **Spells** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/26` | 0.759543 | **Spells** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/23/Text/45` | 0.759543 | **Spells** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/67` | 0.759543 | **Spells** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/28` | 0.759543 | **Spells** |

### Query 25
- Text: What is the rule about **Focus Spells**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/27']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/27', 'PZO22001 Starfinder Player Core 294-329::/page/19/Text/62', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/39']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/27', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/26', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/28']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/26` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/28` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/27` | 0.849140 | **Focus Spells** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/62` | 0.849140 | **Focus Spells** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/39` | 0.849140 | **Focus Spells** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/77` | 0.807140 | **Focus Spells** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/29` | 0.807140 | **Focus Spells** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/83` | 0.807140 | **Focus Spells** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/89` | 0.807140 | **Focus Spells** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/23/Text/46` | 0.807140 | **Focus Spells** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/68` | 0.807140 | **Focus Spells** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/86` | 0.807140 | **Focus Spells** |

### Query 26
- Text: Summarize **Rituals**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/28']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/5/Text/30', 'PZO22001 Starfinder Player Core 294-329::/page/23/Text/47', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/28']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/28', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/27', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/29']
- Expanded expected found: `True`
- Expanded expected rank: `3`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/27` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/29` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/30` | 0.889916 | **Rituals** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/23/Text/47` | 0.889916 | **Rituals** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/28` | 0.889916 | **Rituals** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/64` | 0.847916 | **Rituals** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/90` | 0.847916 | **Rituals** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/87` | 0.847916 | **Rituals** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/90` | 0.847916 | **Rituals** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/84` | 0.847916 | **Rituals** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/78` | 0.847916 | **Rituals** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/65` | 0.847916 | **Rituals** |

### Query 27
- Text: Summarize **PLAYING THE ** **GAME**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/29']
- Expected found: `True`
- Expected rank: `12`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/41', 'PZO22001 Starfinder Player Core 294-329::/page/9/Text/91', 'PZO22001 Starfinder Player Core 294-329::/page/7/Text/38']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/29', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/30', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/28']
- Expanded expected found: `True`
- Expanded expected rank: `12`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/30` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/28` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/41` | 0.938833 | **PLAYING THE ** **GAME** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/91` | 0.938833 | **PLAYING THE ** **GAME** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/38` | 0.938833 | **PLAYING THE ** **GAME** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/66` | 0.896833 | **PLAYING THE ** **GAME** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/31` | 0.896833 | **PLAYING THE ** **GAME** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/65` | 0.896833 | **PLAYING THE ** **GAME** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/79` | 0.896833 | **PLAYING THE ** **GAME** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/70` | 0.896833 | **PLAYING THE ** **GAME** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/88` | 0.896833 | **PLAYING THE ** **GAME** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/64` | 0.896833 | **PLAYING THE ** **GAME** |

### Query 28
- Text: Summarize **CONDITIONS **
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/30']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/33/Text/67', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/30', 'PZO22001 Starfinder Player Core 294-329::/page/35/Text/74']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/30', 'PZO22001 Starfinder Player Core 294-329::/page/35/Text/74', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/31', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/42', 'PZO22001 Starfinder Player Core 294-329::/page/13/Text/80', 'PZO22001 Starfinder Player Core 294-329::/page/17/Text/92', 'PZO22001 Starfinder Player Core 294-329::/page/19/Text/65', 'PZO22001 Starfinder Player Core 294-329::/page/31/Text/66', 'PZO22001 Starfinder Player Core 294-329::/page/29/Text/71', 'PZO22001 Starfinder Player Core 294-329::/page/15/Text/86', 'PZO22001 Starfinder Player Core 294-329::/page/23/Text/49', 'PZO22001 Starfinder Player Core 294-329::/page/27/Text/74']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/35/Text/74` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/31` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/42` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/13/Text/80` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/17/Text/92` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/19/Text/65` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/31/Text/66` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/29/Text/71` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/15/Text/86` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/23/Text/49` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/27/Text/74` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/67` | 0.880718 | **CONDITIONS ** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/30` | 0.880718 | **CONDITIONS ** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/74` | 0.880718 | **CONDITIONS ** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/32` | 0.763212 | **CONDITIONS ** **APPENDIX** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/39` | 0.763212 | **CONDITIONS ** **APPENDIX** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/89` | 0.763212 | **CONDITIONS ** **APPENDIX** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/80` | 0.763212 | **CONDITIONS ** **APPENDIX** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/86` | 0.763212 | **CONDITIONS ** **APPENDIX** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/92` | 0.763212 | **CONDITIONS ** **APPENDIX** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/66` | 0.763212 | **CONDITIONS ** **APPENDIX** |

### Query 29
- Text: Summarize **APPENDIX**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/31']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/31', 'PZO22001 Starfinder Player Core 294-329::/page/35/Text/75', 'PZO22001 Starfinder Player Core 294-329::/page/33/Text/68']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/31', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/30', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/32']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/30` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/32` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/31` | 0.929192 | **APPENDIX** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/75` | 0.929192 | **APPENDIX** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/68` | 0.828418 | **APPENDIX** **GLOSSARY & ** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/27/Text/74` | 0.782460 | **CONDITIONS ** **APPENDIX** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/39` | 0.782459 | **CONDITIONS ** **APPENDIX** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/32` | 0.782459 | **CONDITIONS ** **APPENDIX** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/80` | 0.782459 | **CONDITIONS ** **APPENDIX** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/92` | 0.782459 | **CONDITIONS ** **APPENDIX** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/42` | 0.782459 | **CONDITIONS ** **APPENDIX** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/65` | 0.782459 | **CONDITIONS ** **APPENDIX** |

### Query 30
- Text: Summarize **GLOSSARY & ** **INDEX**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/32']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/32', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/43', 'PZO22001 Starfinder Player Core 294-329::/page/9/Text/93']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/32', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/31', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/1']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/31` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/2/Text/1` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/32` | 0.929439 | **GLOSSARY & ** **INDEX** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/43` | 0.929439 | **GLOSSARY & ** **INDEX** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/93` | 0.929439 | **GLOSSARY & ** **INDEX** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/90` | 0.887439 | **GLOSSARY & ** **INDEX** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/40` | 0.887439 | **GLOSSARY & ** **INDEX** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/33` | 0.887439 | **GLOSSARY & ** **INDEX** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/93` | 0.887439 | **GLOSSARY & ** **INDEX** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/66` | 0.887439 | **GLOSSARY & ** **INDEX** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/87` | 0.887439 | **GLOSSARY & ** **INDEX** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/81` | 0.887439 | **GLOSSARY & ** **INDEX** |

### Query 31
- Text: What is the rule about so long as they know the spell at that rank (see Heightened  Spontaneous Spells below). When you heighten your spell,  the spell's rank increases to match the higher rank of the  spell slot you've prepared it in or used to cast it. This is useful  for any spell, because some effects, such as counteracting,  depend on the spell's rank.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/1', 'PZO22001 Starfinder Player Core 294-329::/page/7/Text/4', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/16']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/1', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/32', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/2']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/32` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/2/Text/2` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/1` | 0.993246 | so long as they know the spell at that rank (see Heightened  Spontaneous Spells below). When you heighten your spell,  the spell's rank increases to match the higher rank of the  spell slot you've pre |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/4` | 0.834415 | Sometimes you need to identify a spell, especially if its  effects aren't obvious right away. If you notice a spell  being cast, and you have that spell in your repertoire  or prepared it that day (ev |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/16` | 0.825979 | Both prepared and spontaneous spellcasters can cast a spell  at a higher spell rank than that listed for the spell. This is  called heightening the spell. A prepared spellcaster can  heighten a spell |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/2` | 0.791710 | In addition, many spells have additional specific benefits  when they are heightened, such as increased damage. These  extra benefits are described at the end of the spell's stat  block. Some heighten |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/7` | 0.743721 | As a spontaneous caster, you can also choose to cast  a lower-rank spell using a higher-rank spell slot without  heightening it or knowing it at a higher rank. This casts the  spell at the rank you kn |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/5` | 0.728758 | If you're a spontaneous spellcaster, you must know a spell at  the specific rank that you want to cast it in order to heighten  it. You can add a spell to your spell repertoire at more than  a single |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/1` | 0.726697 | You can't use your spell slots to cast your innate spells, but  you might have an innate spell and also be able to prepare  or cast the same spell through your class. You also can't  heighten innate s |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/3` | 0.718067 | Other heightened entries give a number after a plus sign,  indicating that heightening grants extra advantages over  multiple ranks. The listed effect applies for every increment  of ranks by which th |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/11` | 0.705730 | A cantrip is always automatically heightened to half your  level, rounded up. For a typical spellcaster, this means its  rank is equal to the highest rank of spell slot you have. |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/26` | 0.702330 | **Heightened** (rank) If the spell has special effects when  heightened (page 295), those effects appear at the end  of the stat block. |

### Query 32
- Text: What is the rule about In addition, many spells have additional specific benefits  when they are heightened, such as increased damage. These  extra benefits are described at the end of the spell's stat  block. Some heightened entries specify one or more ranks  at which the spell must be prepared or cast to gain these  extra advantages. Each of these heightened entries states  specifically which aspects of the spell change at the given  rank. Read the heightened entry only for the spell rank you're  using or preparing; if its benefits are meant to include any of  the effects of a lower-rank heightened entry, those benefits  will be included in the entry.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/2', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/3', 'PZO22001 Starfinder Player Core 294-329::/page/7/Text/26']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/2', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/3', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/1']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/2/Text/3` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/2/Text/1` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/2` | 1.017063 | In addition, many spells have additional specific benefits  when they are heightened, such as increased damage. These  extra benefits are described at the end of the spell's stat  block. Some heighten |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/3` | 0.848524 | Other heightened entries give a number after a plus sign,  indicating that heightening grants extra advantages over  multiple ranks. The listed effect applies for every increment  of ranks by which th |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/26` | 0.834863 | **Heightened** (rank) If the spell has special effects when  heightened (page 295), those effects appear at the end  of the stat block. |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/1` | 0.801339 | so long as they know the spell at that rank (see Heightened  Spontaneous Spells below). When you heighten your spell,  the spell's rank increases to match the higher rank of the  spell slot you've pre |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/4` | 0.715842 | Sometimes you need to identify a spell, especially if its  effects aren't obvious right away. If you notice a spell  being cast, and you have that spell in your repertoire  or prepared it that day (ev |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/16` | 0.705437 | Both prepared and spontaneous spellcasters can cast a spell  at a higher spell rank than that listed for the spell. This is  called heightening the spell. A prepared spellcaster can  heighten a spell |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/1` | 0.679069 | You can't use your spell slots to cast your innate spells, but  you might have an innate spell and also be able to prepare  or cast the same spell through your class. You also can't  heighten innate s |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/8/Text/2` | 0.675024 | These lists include the spells for each tradition, including cantrips. (Focus spells appear on pages 375–380.)  A superscript "H" indicates a spell has extra effects when heightened, and a spell whose |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/5` | 0.663595 | If you're a spontaneous spellcaster, you must know a spell at  the specific rank that you want to cast it in order to heighten  it. You can add a spell to your spell repertoire at more than  a single |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/17` | 0.657483 | Each spell uses the following format. Entries appear only  when applicable, so not all spells will have every entry  described here. The spell's name line also lists the type  of spell if it's a cantr |

### Query 33
- Text: What is the rule about Other heightened entries give a number after a plus sign,  indicating that heightening grants extra advantages over  multiple ranks. The listed effect applies for every increment  of ranks by which the spell is heightened above its lowest  spell rank, and the benefit is cumulative. For example, *slice * *reality* says "**Heightened (+1)** The damage increases by 1d8."  Because *slice reality* deals 7d8 void damage at 6th rank, a  7th-rank *slice reality* would deal 8d8 void damage, an 8thrank spell would deal 9d8 void damage, and so on.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/3']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/3', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/2', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/1']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/3', 'PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/4', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/2']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/4` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/2/Text/2` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/3` | 1.011019 | Other heightened entries give a number after a plus sign,  indicating that heightening grants extra advantages over  multiple ranks. The listed effect applies for every increment  of ranks by which th |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/2` | 0.836461 | In addition, many spells have additional specific benefits  when they are heightened, such as increased damage. These  extra benefits are described at the end of the spell's stat  block. Some heighten |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/1` | 0.759375 | so long as they know the spell at that rank (see Heightened  Spontaneous Spells below). When you heighten your spell,  the spell's rank increases to match the higher rank of the  spell slot you've pre |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/26` | 0.680338 | **Heightened** (rank) If the spell has special effects when  heightened (page 295), those effects appear at the end  of the stat block. |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/32/Text/17` | 0.673093 | **Heightened (+1)** The damage increases by 1d6 and persistent  damage increases by 1d6. |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/34` | 0.666905 | **Heightened (+1)** The damage increases by 2d6 (or by 2d8 if  the target is a divine spellcaster). |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/15` | 0.652761 | **Heightened (+1)** The damage increases by 1d8 and the ice's Hit  Points increase by 5. |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/22/Text/22` | 0.652761 | **Heightened (+1)** The damage increases by 1d8 and the ice's  Hit Points increase by 5. |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/34/Text/37` | 0.643077 | **Heightened (+1)** The damage increases by 1d12. |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/32/Text/43` | 0.639292 | **Heightened (+1)** The damage increases by 1d10. |

### Query 34
- Text: What is the rule about Heightened Spontaneous Spells?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/4', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/1', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/16']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/4', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/3', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/5']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/2/Text/3` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/2/Text/5` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/4` | 0.828581 | Heightened Spontaneous Spells |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/1` | 0.652719 | so long as they know the spell at that rank (see Heightened  Spontaneous Spells below). When you heighten your spell,  the spell's rank increases to match the higher rank of the  spell slot you've pre |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/16` | 0.633876 | Both prepared and spontaneous spellcasters can cast a spell  at a higher spell rank than that listed for the spell. This is  called heightening the spell. A prepared spellcaster can  heighten a spell |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/15` | 0.593243 | HEIGHTENED SPELLS |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/5` | 0.561113 | If you're a spontaneous spellcaster, you must know a spell at  the specific rank that you want to cast it in order to heighten  it. You can add a spell to your spell repertoire at more than  a single |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/8/Text/2` | 0.558177 | These lists include the spells for each tradition, including cantrips. (Focus spells appear on pages 375–380.)  A superscript "H" indicates a spell has extra effects when heightened, and a spell whose |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/26` | 0.557538 | Certain spells are natural to your character, typically coming  from your ancestry or a magic item. They're called innate  spells. Innate spells don't let you qualify for abilities that  require you t |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/35/SectionHeader/14` | 0.550452 | **EMBED MESSAGE **[two-actions] **SPELL 2**  **CONCENTRATE** **ILLUSION** **MANIPULATE**  **Traditions** arcane, occult  **Range **touch; **Targets** 1 object or willing creature  **Duration** unlimit |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/13` | 0.547381 | SPONTANEOUS SPELLS |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/30/Text/1` | 0.542869 | **Heightened (5th)** The spell's range is touch and it targets  1 willing creature. The duration is until your next daily  preparations. |

### Query 35
- Text: What is the rule about If you're a spontaneous spellcaster, you must know a spell at  the specific rank that you want to cast it in order to heighten  it. You can add a spell to your spell repertoire at more than  a single rank so that you have more options when casting it.  For example, if you added *skyfire wings* to your repertoire as  a 3rd-rank spell and again as a 7th-rank spell, you could cast  it as a 3rd-rank or a 7th-rank spell; however, you couldn't cast  it as a 5th-rank spell.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/5', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/7', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/16']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/5', 'PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/4', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/6']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/4` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/2/Text/6` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/5` | 1.009828 | If you're a spontaneous spellcaster, you must know a spell at  the specific rank that you want to cast it in order to heighten  it. You can add a spell to your spell repertoire at more than  a single |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/7` | 0.796132 | As a spontaneous caster, you can also choose to cast  a lower-rank spell using a higher-rank spell slot without  heightening it or knowing it at a higher rank. This casts the  spell at the rank you kn |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/16` | 0.785139 | Both prepared and spontaneous spellcasters can cast a spell  at a higher spell rank than that listed for the spell. This is  called heightening the spell. A prepared spellcaster can  heighten a spell |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/1` | 0.740317 | so long as they know the spell at that rank (see Heightened  Spontaneous Spells below). When you heighten your spell,  the spell's rank increases to match the higher rank of the  spell slot you've pre |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/4` | 0.725242 | Sometimes you need to identify a spell, especially if its  effects aren't obvious right away. If you notice a spell  being cast, and you have that spell in your repertoire  or prepared it that day (ev |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/1` | 0.711798 | You can't use your spell slots to cast your innate spells, but  you might have an innate spell and also be able to prepare  or cast the same spell through your class. You also can't  heighten innate s |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/6` | 0.695117 | Many spontaneous spellcasting classes provide abilities  like the signature spells class feature, which allows you to  cast a limited number of spells as heightened versions even if  you know the spel |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/14` | 0.686460 | If you're a spontaneous spellcaster—such as a mystic—you  choose which spell from your spell repertoire that you're  using a spell slot for at the moment you decide to cast it. This  provides you with |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/26` | 0.685873 | Certain spells are natural to your character, typically coming  from your ancestry or a magic item. They're called innate  spells. Innate spells don't let you qualify for abilities that  require you t |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/3` | 0.684756 | Your class determines which tradition of magic your spells use. In some cases, such as when a mystic gains spells from  their connection or when a witchwarper learns spells from their paradox, you mig |

### Query 36
- Text: What is the rule about Many spontaneous spellcasting classes provide abilities  like the signature spells class feature, which allows you to  cast a limited number of spells as heightened versions even if  you know the spell at only a single rank.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/6', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/5', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/6']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/6', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/7', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/5']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/2/Text/7` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/2/Text/5` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/6` | 0.949527 | Many spontaneous spellcasting classes provide abilities  like the signature spells class feature, which allows you to  cast a limited number of spells as heightened versions even if  you know the spel |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/5` | 0.730751 | If you're a spontaneous spellcaster, you must know a spell at  the specific rank that you want to cast it in order to heighten  it. You can add a spell to your spell repertoire at more than  a single |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/6` | 0.713938 | Characters of spellcasting classes can cast a number of spells  each day; the spells you can cast in a day are referred to as  spell slots. At 1st level, a character has only a small number  of 1st-ra |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/1` | 0.671725 | You can't use your spell slots to cast your innate spells, but  you might have an innate spell and also be able to prepare  or cast the same spell through your class. You also can't  heighten innate s |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/1` | 0.670453 | so long as they know the spell at that rank (see Heightened  Spontaneous Spells below). When you heighten your spell,  the spell's rank increases to match the higher rank of the  spell slot you've pre |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/7` | 0.653762 | As a spontaneous caster, you can also choose to cast  a lower-rank spell using a higher-rank spell slot without  heightening it or knowing it at a higher rank. This casts the  spell at the rank you kn |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/28` | 0.652883 | If you have an innate spell, you can cast it even if it's not of  a spell rank you can normally cast. This is especially common  for monsters. |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/26` | 0.640761 | Certain spells are natural to your character, typically coming  from your ancestry or a magic item. They're called innate  spells. Innate spells don't let you qualify for abilities that  require you t |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/3` | 0.639845 | Your class determines which tradition of magic your spells use. In some cases, such as when a mystic gains spells from  their connection or when a witchwarper learns spells from their paradox, you mig |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/16` | 0.637949 | Both prepared and spontaneous spellcasters can cast a spell  at a higher spell rank than that listed for the spell. This is  called heightening the spell. A prepared spellcaster can  heighten a spell |

### Query 37
- Text: What is the rule about As a spontaneous caster, you can also choose to cast  a lower-rank spell using a higher-rank spell slot without  heightening it or knowing it at a higher rank. This casts the  spell at the rank you know the spell, not the rank of the  higher slot. The spell doesn't have any heightened effects,  so it's usually not a very efficient use of your magic outside  of highly specific circumstances. For instance, if your party  was having trouble with an invisible enemy, and you had  *revealing light* in your repertoire but had already spent all  of your 2nd-rank spell slots, it might be worth it to use a  3rd-rank spell slot to cast the spell, even though it'd have no  heightened benefit.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/7', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/1', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/5']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/7', 'PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/8', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/6']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/8` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/2/Text/6` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/7` | 1.020270 | As a spontaneous caster, you can also choose to cast  a lower-rank spell using a higher-rank spell slot without  heightening it or knowing it at a higher rank. This casts the  spell at the rank you kn |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/1` | 0.812307 | so long as they know the spell at that rank (see Heightened  Spontaneous Spells below). When you heighten your spell,  the spell's rank increases to match the higher rank of the  spell slot you've pre |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/5` | 0.805187 | If you're a spontaneous spellcaster, you must know a spell at  the specific rank that you want to cast it in order to heighten  it. You can add a spell to your spell repertoire at more than  a single |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/16` | 0.740986 | Both prepared and spontaneous spellcasters can cast a spell  at a higher spell rank than that listed for the spell. This is  called heightening the spell. A prepared spellcaster can  heighten a spell |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/1` | 0.730087 | You can't use your spell slots to cast your innate spells, but  you might have an innate spell and also be able to prepare  or cast the same spell through your class. You also can't  heighten innate s |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/4` | 0.723560 | Sometimes you need to identify a spell, especially if its  effects aren't obvious right away. If you notice a spell  being cast, and you have that spell in your repertoire  or prepared it that day (ev |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/28` | 0.707493 | If you have an innate spell, you can cast it even if it's not of  a spell rank you can normally cast. This is especially common  for monsters. |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/14` | 0.705251 | If you're a spontaneous spellcaster—such as a mystic—you  choose which spell from your spell repertoire that you're  using a spell slot for at the moment you decide to cast it. This  provides you with |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/2` | 0.680904 | In addition, many spells have additional specific benefits  when they are heightened, such as increased damage. These  extra benefits are described at the end of the spell's stat  block. Some heighten |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/3` | 0.661417 | Your class determines which tradition of magic your spells use. In some cases, such as when a mystic gains spells from  their connection or when a witchwarper learns spells from their paradox, you mig |

### Query 38
- Text: Summarize CANTRIPS
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/8']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/8', 'PZO22001 Starfinder Player Core 294-329::/page/8/SectionHeader/6', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/9']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/8', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/7', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/9']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/2/Text/7` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/2/Text/9` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/8` | 0.842251 | CANTRIPS |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/8/SectionHeader/6` | 0.679872 | ARCANE CANTRIPS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/9` | 0.535715 | A cantrip is a special type of spell that's weaker than other  spells but can be used with greater freedom and flexibility. |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/10` | 0.491762 | The title of a cantrip's stat block says "Cantrip" instead of  "Spell", and the spell has the cantrip trait. Casting a cantrip  doesn't use up your spell slots; you can cast a cantrip at will,  any nu |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/7/SectionHeader/6` | 0.489891 | COUNTERACTING |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/14/Text/74` | 0.476938 | insight about a topic. |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/1` | 0.475028 | **SUBTLE SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/31` | 0.474003 | **APPENDIX** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/75` | 0.474003 | **APPENDIX** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/11` | 0.473850 | A cantrip is always automatically heightened to half your  level, rounded up. For a typical spellcaster, this means its  rank is equal to the highest rank of spell slot you have. |

### Query 39
- Text: What is the rule about A cantrip is a special type of spell that's weaker than other  spells but can be used with greater freedom and flexibility.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/9', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/9', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/10']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/9', 'PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/8', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/10']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/8` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/2/Text/10` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/9` | 0.951696 | A cantrip is a special type of spell that's weaker than other  spells but can be used with greater freedom and flexibility. |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/9` | 0.696548 | Each prepared spell is expended after a single casting,  so if you want to cast a particular spell more than once in  a day, you need to prepare that spell multiple times. The  exception to this rule |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/10` | 0.679511 | The title of a cantrip's stat block says "Cantrip" instead of  "Spell", and the spell has the cantrip trait. Casting a cantrip  doesn't use up your spell slots; you can cast a cantrip at will,  any nu |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/11` | 0.613791 | A cantrip is always automatically heightened to half your  level, rounded up. For a typical spellcaster, this means its  rank is equal to the highest rank of spell slot you have. |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/8/Text/2` | 0.605731 | These lists include the spells for each tradition, including cantrips. (Focus spells appear on pages 375–380.)  A superscript "H" indicates a spell has extra effects when heightened, and a spell whose |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/26` | 0.598506 | Certain spells are natural to your character, typically coming  from your ancestry or a magic item. They're called innate  spells. Innate spells don't let you qualify for abilities that  require you t |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/17` | 0.591812 | Each spell uses the following format. Entries appear only  when applicable, so not all spells will have every entry  described here. The spell's name line also lists the type  of spell if it's a cantr |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/14` | 0.578366 | Focus spells are automatically heightened to half your level  rounded up, just like cantrips are. You can't cast a focus spell  if its minimum rank is greater than half your level rounded  up, even if |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/2` | 0.576865 | In rare cases, a spell might have you make some other  type of attack, such as a weapon Strike. Such attacks use the  normal rules and attack bonus for that type of attack. |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/5` | 0.572526 | Spells can vary in how many actions they take, as shown in  the spell's stat block. You cast cantrips, spells from spell slots,  and focus spells using the same process, but must expend the  spell whe |

### Query 40
- Text: What is the rule about The title of a cantrip's stat block says "Cantrip" instead of  "Spell", and the spell has the cantrip trait. Casting a cantrip  doesn't use up your spell slots; you can cast a cantrip at will,  any number of times per day. If you're a prepared caster, you  can prepare a specific number of cantrips each day. You can't  prepare a cantrip in a spell slot.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/10', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/9', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/26']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/10', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/11', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/9']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/2/Text/11` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/2/Text/9` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/10` | 1.021436 | The title of a cantrip's stat block says "Cantrip" instead of  "Spell", and the spell has the cantrip trait. Casting a cantrip  doesn't use up your spell slots; you can cast a cantrip at will,  any nu |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/9` | 0.858159 | Each prepared spell is expended after a single casting,  so if you want to cast a particular spell more than once in  a day, you need to prepare that spell multiple times. The  exception to this rule |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/26` | 0.780862 | Certain spells are natural to your character, typically coming  from your ancestry or a magic item. They're called innate  spells. Innate spells don't let you qualify for abilities that  require you t |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/5` | 0.738049 | Spells can vary in how many actions they take, as shown in  the spell's stat block. You cast cantrips, spells from spell slots,  and focus spells using the same process, but must expend the  spell whe |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/17` | 0.685553 | Each spell uses the following format. Entries appear only  when applicable, so not all spells will have every entry  described here. The spell's name line also lists the type  of spell if it's a cantr |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/6` | 0.681534 | Characters of spellcasting classes can cast a number of spells  each day; the spells you can cast in a day are referred to as  spell slots. At 1st level, a character has only a small number  of 1st-ra |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/9` | 0.669950 | A cantrip is a special type of spell that's weaker than other  spells but can be used with greater freedom and flexibility. |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/11` | 0.668470 | A cantrip is always automatically heightened to half your  level, rounded up. For a typical spellcaster, this means its  rank is equal to the highest rank of spell slot you have. |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/14` | 0.666984 | If you're a spontaneous spellcaster—such as a mystic—you  choose which spell from your spell repertoire that you're  using a spell slot for at the moment you decide to cast it. This  provides you with |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/1` | 0.653084 | You can't use your spell slots to cast your innate spells, but  you might have an innate spell and also be able to prepare  or cast the same spell through your class. You also can't  heighten innate s |

### Query 41
- Text: What is the rule about A cantrip is always automatically heightened to half your  level, rounded up. For a typical spellcaster, this means its  rank is equal to the highest rank of spell slot you have.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/11', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/14', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/26']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/11', 'PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/12', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/10']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/12` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/2/Text/10` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/11` | 0.985015 | A cantrip is always automatically heightened to half your  level, rounded up. For a typical spellcaster, this means its  rank is equal to the highest rank of spell slot you have. |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/14` | 0.797923 | Focus spells are automatically heightened to half your level  rounded up, just like cantrips are. You can't cast a focus spell  if its minimum rank is greater than half your level rounded  up, even if |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/26` | 0.742762 | Certain spells are natural to your character, typically coming  from your ancestry or a magic item. They're called innate  spells. Innate spells don't let you qualify for abilities that  require you t |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/1` | 0.684737 | so long as they know the spell at that rank (see Heightened  Spontaneous Spells below). When you heighten your spell,  the spell's rank increases to match the higher rank of the  spell slot you've pre |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/16` | 0.649067 | Both prepared and spontaneous spellcasters can cast a spell  at a higher spell rank than that listed for the spell. This is  called heightening the spell. A prepared spellcaster can  heighten a spell |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/10` | 0.635113 | The title of a cantrip's stat block says "Cantrip" instead of  "Spell", and the spell has the cantrip trait. Casting a cantrip  doesn't use up your spell slots; you can cast a cantrip at will,  any nu |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/5` | 0.625087 | If you're a spontaneous spellcaster, you must know a spell at  the specific rank that you want to cast it in order to heighten  it. You can add a spell to your spell repertoire at more than  a single |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/17` | 0.622566 | Each spell uses the following format. Entries appear only  when applicable, so not all spells will have every entry  described here. The spell's name line also lists the type  of spell if it's a cantr |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/4` | 0.610825 | Sometimes you need to identify a spell, especially if its  effects aren't obvious right away. If you notice a spell  being cast, and you have that spell in your repertoire  or prepared it that day (ev |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/9` | 0.598519 | Each prepared spell is expended after a single casting,  so if you want to cast a particular spell more than once in  a day, you need to prepare that spell multiple times. The  exception to this rule |

### Query 42
- Text: What is the rule about FOCUS SPELLS?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/12']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/12', 'PZO22001 Starfinder Player Core 294-329::/page/13/Text/77', 'PZO22001 Starfinder Player Core 294-329::/page/11/Text/86']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/12', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/13', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/11']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/2/Text/13` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/2/Text/11` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/12` | 0.802596 | FOCUS SPELLS |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/77` | 0.693257 | **Focus Spells** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/86` | 0.693257 | **Focus Spells** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/89` | 0.651257 | **Focus Spells** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/64` | 0.651257 | **Focus Spells** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/83` | 0.651257 | **Focus Spells** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/62` | 0.651257 | **Focus Spells** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/68` | 0.651257 | **Focus Spells** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/63` | 0.651257 | **Focus Spells** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/39` | 0.651257 | **Focus Spells** |

### Query 43
- Text: What is the rule about Focus spells are a special type of spell attained directly from  a specific source, such as a field of study, connection to a  mystical force, or exposure to an alternate reality. You can  learn focus spells only through special class features or feats,  rather than choosing them from a spell list. Furthermore, you  cast focus spells using a special pool of Focus Points—you can't  prepare a focus spell in a spell slot or use your spell slots to  cast focus spells; similarly, you can't spend your Focus Points  to cast spells that aren't focus spells. Even some classes that  don't normally grant spellcasting can grant focus spells. The  title of a focus spell's stat block says "Focus" instead of "Spell",  and the spell has the focus trait.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/13', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/21', 'PZO22001 Starfinder Player Core 294-329::/page/4/Text/5']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/13', 'PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/12', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/14']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/12` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/2/Text/14` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/13` | 1.015476 | Focus spells are a special type of spell attained directly from  a specific source, such as a field of study, connection to a  mystical force, or exposure to an alternate reality. You can  learn focus |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/21` | 0.877564 | If you get focus spells from a class or other source that  doesn't grant spellcasting ability, the ability that gives you  focus spells also provides your proficiency for your spell  attack modifier a |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/5` | 0.808719 | Spells can vary in how many actions they take, as shown in  the spell's stat block. You cast cantrips, spells from spell slots,  and focus spells using the same process, but must expend the  spell whe |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/23` | 0.760230 | It's possible, especially through archetypes, to gain focus  spells from more than one source. If this happens, you  have just one focus pool, counting all your focus spells to  determine the points i |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/14` | 0.738377 | Focus spells are automatically heightened to half your level  rounded up, just like cantrips are. You can't cast a focus spell  if its minimum rank is greater than half your level rounded  up, even if |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/15` | 0.737543 | Casting any of your focus spells costs you 1 Focus Point.  You automatically gain a focus pool the first time you gain an  ability that gives you a focus spell. The maximum number of  points in your p |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/22` | 0.725145 | If you are a spellcaster, your focus spells are the same tradition  of spell as the class that gave you the focus spell. A mystic's |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/3` | 0.705728 | Your class determines which tradition of magic your spells use. In some cases, such as when a mystic gains spells from  their connection or when a witchwarper learns spells from their paradox, you mig |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/1` | 0.705047 | You can't use your spell slots to cast your innate spells, but  you might have an innate spell and also be able to prepare  or cast the same spell through your class. You also can't  heighten innate s |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/21` | 0.696572 | Some spells allow you to target a creature, an object, or  something more specific. The target must be within the  spell's range, and you must be able to see it (or otherwise  perceive it with a preci |

### Query 44
- Text: What is the rule about Focus spells are automatically heightened to half your level  rounded up, just like cantrips are. You can't cast a focus spell  if its minimum rank is greater than half your level rounded  up, even if you somehow gain access to it.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/14']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/14', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/11', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/1']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/14', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/13', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/15']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/2/Text/13` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/2/Text/15` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/14` | 0.975382 | Focus spells are automatically heightened to half your level  rounded up, just like cantrips are. You can't cast a focus spell  if its minimum rank is greater than half your level rounded  up, even if |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/11` | 0.790449 | A cantrip is always automatically heightened to half your  level, rounded up. For a typical spellcaster, this means its  rank is equal to the highest rank of spell slot you have. |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/1` | 0.695367 | so long as they know the spell at that rank (see Heightened  Spontaneous Spells below). When you heighten your spell,  the spell's rank increases to match the higher rank of the  spell slot you've pre |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/13` | 0.663763 | Focus spells are a special type of spell attained directly from  a specific source, such as a field of study, connection to a  mystical force, or exposure to an alternate reality. You can  learn focus |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/15` | 0.652486 | Casting any of your focus spells costs you 1 Focus Point.  You automatically gain a focus pool the first time you gain an  ability that gives you a focus spell. The maximum number of  points in your p |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/17` | 0.636393 | Each spell uses the following format. Entries appear only  when applicable, so not all spells will have every entry  described here. The spell's name line also lists the type  of spell if it's a cantr |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/26` | 0.629385 | Certain spells are natural to your character, typically coming  from your ancestry or a magic item. They're called innate  spells. Innate spells don't let you qualify for abilities that  require you t |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/2` | 0.619117 | In addition, many spells have additional specific benefits  when they are heightened, such as increased damage. These  extra benefits are described at the end of the spell's stat  block. Some heighten |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/5` | 0.617624 | Spells can vary in how many actions they take, as shown in  the spell's stat block. You cast cantrips, spells from spell slots,  and focus spells using the same process, but must expend the  spell whe |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/5` | 0.613269 | If you're a spontaneous spellcaster, you must know a spell at  the specific rank that you want to cast it in order to heighten  it. You can add a spell to your spell repertoire at more than  a single |

### Query 45
- Text: What is the rule about Casting any of your focus spells costs you 1 Focus Point.  You automatically gain a focus pool the first time you gain an  ability that gives you a focus spell. The maximum number of  points in your pool is equal to the number of focus spells you  know or 3, whichever is lower. This counts only spells that  require Focus Points to cast.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/15']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/15', 'PZO22001 Starfinder Player Core 294-329::/page/4/Text/5', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/23']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/15', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/16', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/14']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/2/Text/16` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/2/Text/14` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/15` | 1.007599 | Casting any of your focus spells costs you 1 Focus Point.  You automatically gain a focus pool the first time you gain an  ability that gives you a focus spell. The maximum number of  points in your p |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/5` | 0.798869 | Spells can vary in how many actions they take, as shown in  the spell's stat block. You cast cantrips, spells from spell slots,  and focus spells using the same process, but must expend the  spell whe |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/23` | 0.795824 | It's possible, especially through archetypes, to gain focus  spells from more than one source. If this happens, you  have just one focus pool, counting all your focus spells to  determine the points i |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/13` | 0.719419 | Focus spells are a special type of spell attained directly from  a specific source, such as a field of study, connection to a  mystical force, or exposure to an alternate reality. You can  learn focus |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/14` | 0.707931 | Focus spells are automatically heightened to half your level  rounded up, just like cantrips are. You can't cast a focus spell  if its minimum rank is greater than half your level rounded  up, even if |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/21` | 0.700107 | If you get focus spells from a class or other source that  doesn't grant spellcasting ability, the ability that gives you  focus spells also provides your proficiency for your spell  attack modifier a |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/6` | 0.682479 | Characters of spellcasting classes can cast a number of spells  each day; the spells you can cast in a day are referred to as  spell slots. At 1st level, a character has only a small number  of 1st-ra |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/16` | 0.664374 | You replenish all the Focus Points in your pool during your  daily preparations. You can also use the Refocus activity to  pray, study, meditate, or otherwise reattune yourself to the  source of your |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/7` | 0.660403 | Some spells require you to pay a cost or provide a locus. If the  spell lists a **cost**, you must have the listed money, valuable  materials, or other resources to cast the spell (such as gems or  ma |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/9` | 0.654403 | Each prepared spell is expended after a single casting,  so if you want to cast a particular spell more than once in  a day, you need to prepare that spell multiple times. The  exception to this rule |

### Query 46
- Text: What is the rule about You replenish all the Focus Points in your pool during your  daily preparations. You can also use the Refocus activity to  pray, study, meditate, or otherwise reattune yourself to the  source of your focus magic and regain 1 Focus Point. You can  Refocus multiple times to regain multiple points, up to your  pool's maximum.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/16']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/16', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/23', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/15']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/16', 'PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/17', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/15']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/17` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/2/Text/15` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/16` | 0.982992 | You replenish all the Focus Points in your pool during your  daily preparations. You can also use the Refocus activity to  pray, study, meditate, or otherwise reattune yourself to the  source of your |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/23` | 0.805121 | It's possible, especially through archetypes, to gain focus  spells from more than one source. If this happens, you  have just one focus pool, counting all your focus spells to  determine the points i |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/15` | 0.725815 | Casting any of your focus spells costs you 1 Focus Point.  You automatically gain a focus pool the first time you gain an  ability that gives you a focus spell. The maximum number of  points in your p |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/20` | 0.659128 | You spend 10 minutes performing deeds to restore your  magical connection. This restores 1 Focus Point to your focus  pool. The deeds you need to perform are specified in the class  or ability that gi |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/19` | 0.652872 | **Requirements** You have a focus pool. |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/32/SectionHeader/18` | 0.648547 | **DIVINE INSPIRATION **[two-actions] **SPELL 8**  **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** divine  **Range **touch;** Targets** 1 willing creature  You infuse a target with spiritual |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/5` | 0.617207 | Spells can vary in how many actions they take, as shown in  the spell's stat block. You cast cantrips, spells from spell slots,  and focus spells using the same process, but must expend the  spell whe |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/9` | 0.605094 | Each prepared spell is expended after a single casting,  so if you want to cast a particular spell more than once in  a day, you need to prepare that spell multiple times. The  exception to this rule |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/14` | 0.595302 | Focus spells are automatically heightened to half your level  rounded up, just like cantrips are. You can't cast a focus spell  if its minimum rank is greater than half your level rounded  up, even if |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/13` | 0.591924 | Focus spells are a special type of spell attained directly from  a specific source, such as a field of study, connection to a  mystical force, or exposure to an alternate reality. You can  learn focus |

### Query 47
- Text: Summarize **REFOCUS**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/17']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/17', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/39', 'PZO22001 Starfinder Player Core 294-329::/page/7/Text/36']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/17', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/16', 'PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/18']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/2/Text/16` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/18` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/17` | 0.897040 | **REFOCUS** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/39` | 0.696410 | **Focus Spells** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/36` | 0.696410 | **Focus Spells** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/29` | 0.654410 | **Focus Spells** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/64` | 0.654410 | **Focus Spells** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/89` | 0.654410 | **Focus Spells** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/63` | 0.654410 | **Focus Spells** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/89` | 0.654410 | **Focus Spells** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/27` | 0.654410 | **Focus Spells** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/83` | 0.654410 | **Focus Spells** |

### Query 48
- Text: Summarize **CONCENTRATE** **EXPLORATION**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/18']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/18', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/39', 'PZO22001 Starfinder Player Core 294-329::/page/33/Text/64']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/18', 'PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/17', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/19']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/17` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/2/Text/19` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/18` | 0.948322 | **CONCENTRATE** **EXPLORATION** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/39` | 0.705564 | **Focus Spells** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/64` | 0.705564 | **Focus Spells** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/29` | 0.663564 | **Focus Spells** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/89` | 0.663564 | **Focus Spells** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/68` | 0.663564 | **Focus Spells** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/63` | 0.663564 | **Focus Spells** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/36` | 0.663564 | **Focus Spells** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/23/Text/46` | 0.663564 | **Focus Spells** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/89` | 0.663564 | **Focus Spells** |

### Query 49
- Text: Summarize **Requirements** You have a focus pool.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/19']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/19', 'PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/12', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/16']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/19', 'PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/18', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/20']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/18` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/2/Text/20` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/19` | 1.016705 | **Requirements** You have a focus pool. |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/12` | 0.736685 | FOCUS SPELLS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/16` | 0.729593 | You replenish all the Focus Points in your pool during your  daily preparations. You can also use the Refocus activity to  pray, study, meditate, or otherwise reattune yourself to the  source of your |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/15` | 0.696769 | Casting any of your focus spells costs you 1 Focus Point.  You automatically gain a focus pool the first time you gain an  ability that gives you a focus spell. The maximum number of  points in your p |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/86` | 0.659013 | **Focus Spells** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/89` | 0.659013 | **Focus Spells** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/89` | 0.659013 | **Focus Spells** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/64` | 0.659013 | **Focus Spells** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/29` | 0.659013 | **Focus Spells** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/63` | 0.659013 | **Focus Spells** |

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
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/20` | 1.010213 | You spend 10 minutes performing deeds to restore your  magical connection. This restores 1 Focus Point to your focus  pool. The deeds you need to perform are specified in the class  or ability that gi |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/23` | 0.714019 | It's possible, especially through archetypes, to gain focus  spells from more than one source. If this happens, you  have just one focus pool, counting all your focus spells to  determine the points i |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/16` | 0.700355 | You replenish all the Focus Points in your pool during your  daily preparations. You can also use the Refocus activity to  pray, study, meditate, or otherwise reattune yourself to the  source of your |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/13` | 0.654580 | Focus spells are a special type of spell attained directly from  a specific source, such as a field of study, connection to a  mystical force, or exposure to an alternate reality. You can  learn focus |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/22` | 0.648096 | If you are a spellcaster, your focus spells are the same tradition  of spell as the class that gave you the focus spell. A mystic's |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/21` | 0.647519 | If you get focus spells from a class or other source that  doesn't grant spellcasting ability, the ability that gives you  focus spells also provides your proficiency for your spell  attack modifier a |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/15` | 0.643241 | Casting any of your focus spells costs you 1 Focus Point.  You automatically gain a focus pool the first time you gain an  ability that gives you a focus spell. The maximum number of  points in your p |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/31/SectionHeader/47` | 0.641460 | **DISPEL MAGIC **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, occult, primal  **Range **120 feet;** Targets** 1 spell effect or unattended magic  item  You |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/32/SectionHeader/18` | 0.639194 | **DIVINE INSPIRATION **[two-actions] **SPELL 8**  **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** divine  **Range **touch;** Targets** 1 willing creature  You infuse a target with spiritual |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/5` | 0.634523 | Spells can vary in how many actions they take, as shown in  the spell's stat block. You cast cantrips, spells from spell slots,  and focus spells using the same process, but must expend the  spell whe |

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
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/21` | 0.850856 | SPELLCASTERS WITH FOCUS  SPELLS |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/20` | 0.787819 | NON-SPELLCASTERS WITH  FOCUS SPELLS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/12` | 0.680038 | FOCUS SPELLS |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/22` | 0.567423 | If you are a spellcaster, your focus spells are the same tradition  of spell as the class that gave you the focus spell. A mystic's |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/27` | 0.562165 | **Focus Spells** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/77` | 0.562165 | **Focus Spells** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/83` | 0.562165 | **Focus Spells** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/27/Text/71` | 0.562165 | **Focus Spells** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/89` | 0.562165 | **Focus Spells** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/39` | 0.562165 | **Focus Spells** |

### Query 52
- Text: What is the rule about If you are a spellcaster, your focus spells are the same tradition  of spell as the class that gave you the focus spell. A mystic's?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/22']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/22', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/21', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/3']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/22', 'PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/21', 'PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/1']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/21` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/1` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/22` | 0.996064 | If you are a spellcaster, your focus spells are the same tradition  of spell as the class that gave you the focus spell. A mystic's |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/21` | 0.800492 | If you get focus spells from a class or other source that  doesn't grant spellcasting ability, the ability that gives you  focus spells also provides your proficiency for your spell  attack modifier a |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/3` | 0.788923 | Your class determines which tradition of magic your spells use. In some cases, such as when a mystic gains spells from  their connection or when a witchwarper learns spells from their paradox, you mig |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/13` | 0.706364 | Focus spells are a special type of spell attained directly from  a specific source, such as a field of study, connection to a  mystical force, or exposure to an alternate reality. You can  learn focus |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/14` | 0.678847 | If you're a spontaneous spellcaster—such as a mystic—you  choose which spell from your spell repertoire that you're  using a spell slot for at the moment you decide to cast it. This  provides you with |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/5` | 0.665842 | Spells can vary in how many actions they take, as shown in  the spell's stat block. You cast cantrips, spells from spell slots,  and focus spells using the same process, but must expend the  spell whe |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/4` | 0.653519 | With special gestures and utterances, a spellcaster can  call forth mystic energies, warp the mind, protect themself  against danger, or even create something from nothing.  Each class has its own met |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/4` | 0.645739 | Spellcasting creates obvious sensory manifestations, such  as bright lights, crackling sounds, and sharp smells from the  gathering magic. Nearly all spells manifest a spell signature—a  colorful, glo |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/26` | 0.645581 | Certain spells are natural to your character, typically coming  from your ancestry or a magic item. They're called innate  spells. Innate spells don't let you qualify for abilities that  require you t |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/23` | 0.638793 | It's possible, especially through archetypes, to gain focus  spells from more than one source. If this happens, you  have just one focus pool, counting all your focus spells to  determine the points i |

### Query 53
- Text: Summarize **MAGICAL TRADITIONS**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/1', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/40', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/30']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/1', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/2', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/22']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/2` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/2/Text/22` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/1` | 0.898082 | **MAGICAL TRADITIONS** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/40` | 0.721920 | **Rituals** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/30` | 0.721920 | **Rituals** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/65` | 0.679920 | **Rituals** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/87` | 0.679920 | **Rituals** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/90` | 0.679920 | **Rituals** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/37` | 0.679920 | **Rituals** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/64` | 0.679920 | **Rituals** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/23/Text/47` | 0.679920 | **Rituals** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/63` | 0.679920 | **Rituals** |

### Query 54
- Text: What is the rule about Spellcasters cast spells from one of four different spell lists, each representing a different magical tradition: arcane,  divine, occult, and primal.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/2', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/3', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/7']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/2', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/3', 'PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/1']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/3` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/1` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/2` | 0.889798 | Spellcasters cast spells from one of four different spell lists, each representing a different magical tradition: arcane,  divine, occult, and primal. |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/3` | 0.657303 | Your class determines which tradition of magic your spells use. In some cases, such as when a mystic gains spells from  their connection or when a witchwarper learns spells from their paradox, you mig |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/7` | 0.634029 | Arcane spellcasters use logic and  rationality to categorize the magic inherent  in the world around them. Because of its far-reaching  approach, the arcane tradition has the broadest spell  list, tho |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/18` | 0.564264 | An instinctual connection to and faith in the  world, the cycle of day and night, the turning  of the seasons, and the natural selection of predator and  prey drive the primal tradition. Mystics conne |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/26` | 0.549592 | Certain spells are natural to your character, typically coming  from your ancestry or a magic item. They're called innate  spells. Innate spells don't let you qualify for abilities that  require you t |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/33/ListItem/20` | 0.545246 | **Tradition Resistance** If the dragon's magical tradition  matches that of your *dragon form* spell, you gain the  listed ability. **Arcane** resistance 5 against damage from  spells; **divine** resi |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/8/Text/2` | 0.544355 | These lists include the spells for each tradition, including cantrips. (Focus spells appear on pages 375–380.)  A superscript "H" indicates a spell has extra effects when heightened, and a spell whose |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/15` | 0.540051 | **CREATION** **SPELL 4**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal  **Cast** 1 minute **Range **0 feet  **Duration** 1 hour  You conjure a temporary object from magical energy. It |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/31/SectionHeader/28` | 0.533566 | **DISGUISE MAGIC** **SPELL 1**  **CONCENTRATE** **ILLUSION** **MANIPULATE**  **Traditions** arcane, occult  **Cast** 1 minute  **Range **30 feet; **Targets** 1 item or spell effect  **Duration** until |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/14` | 0.531479 | If you're a spontaneous spellcaster—such as a mystic—you  choose which spell from your spell repertoire that you're  using a spell slot for at the moment you decide to cast it. This  provides you with |

### Query 55
- Text: What is the rule about Your class determines which tradition of magic your spells use. In some cases, such as when a mystic gains spells from  their connection or when a witchwarper learns spells from their paradox, you might be able to cast one or more select  spells from a different spell list than the list you normally cast from; for instance, mystics with the elemental connection  can conjure a *spiritual guardian*, perhaps in the form of a nature deity's attendant or servitor. In these cases, the spell  uses your magic tradition, not the list the spell normally comes from. When you cast a spell, add your tradition's trait to  the spell.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/3']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/3', 'PZO22001 Starfinder Player Core 294-329::/page/7/Text/21', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/22']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/3', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/2', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/4']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/2` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/4` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/3` | 1.025930 | Your class determines which tradition of magic your spells use. In some cases, such as when a mystic gains spells from  their connection or when a witchwarper learns spells from their paradox, you mig |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/21` | 0.794753 | **Tradition** This entry lists the magical traditions the spell  belongs to. Some feats or other abilities might add a  spell to your spell list even if you don't follow the listed  traditions. |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/22` | 0.786503 | If you are a spellcaster, your focus spells are the same tradition  of spell as the class that gave you the focus spell. A mystic's |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/14` | 0.735684 | If you're a spontaneous spellcaster—such as a mystic—you  choose which spell from your spell repertoire that you're  using a spell slot for at the moment you decide to cast it. This  provides you with |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/26` | 0.716083 | Certain spells are natural to your character, typically coming  from your ancestry or a magic item. They're called innate  spells. Innate spells don't let you qualify for abilities that  require you t |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/21` | 0.711005 | If you get focus spells from a class or other source that  doesn't grant spellcasting ability, the ability that gives you  focus spells also provides your proficiency for your spell  attack modifier a |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/1` | 0.706838 | You can't use your spell slots to cast your innate spells, but  you might have an innate spell and also be able to prepare  or cast the same spell through your class. You also can't  heighten innate s |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/4` | 0.700701 | With special gestures and utterances, a spellcaster can  call forth mystic energies, warp the mind, protect themself  against danger, or even create something from nothing.  Each class has its own met |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/5` | 0.699451 | Spells can vary in how many actions they take, as shown in  the spell's stat block. You cast cantrips, spells from spell slots,  and focus spells using the same process, but must expend the  spell whe |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/4` | 0.692180 | Sometimes you need to identify a spell, especially if its  effects aren't obvious right away. If you notice a spell  being cast, and you have that spell in your repertoire  or prepared it that day (ev |

### Query 56
- Text: What is the rule about Some types of magic, such as that of most magic items, don't belong to any single tradition. These have the magical  trait instead of a tradition trait.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/4', 'PZO22001 Starfinder Player Core 294-329::/page/7/Text/21', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/3']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/4', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/3', 'PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/6']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/3` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/6` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/4` | 0.926644 | Some types of magic, such as that of most magic items, don't belong to any single tradition. These have the magical  trait instead of a tradition trait. |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/21` | 0.691635 | **Tradition** This entry lists the magical traditions the spell  belongs to. Some feats or other abilities might add a  spell to your spell list even if you don't follow the listed  traditions. |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/3` | 0.674527 | Your class determines which tradition of magic your spells use. In some cases, such as when a mystic gains spells from  their connection or when a witchwarper learns spells from their paradox, you mig |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/6/Text/6` | 0.571761 | Spells that affect multiple creatures in an area can have  both an Area entry and a Targets entry. A spell that has an  area but no targets listed usually affects all creatures in the  area indiscrimi |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/4` | 0.565109 | Non-magical light always shines in non-magical darkness  and always fails to shine in magical darkness. Magical light  always shines in non-magical darkness but shines in magical  darkness only if the |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/26` | 0.562710 | Certain spells are natural to your character, typically coming  from your ancestry or a magic item. They're called innate  spells. Innate spells don't let you qualify for abilities that  require you t |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/28` | 0.557993 | If you have an innate spell, you can cast it even if it's not of  a spell rank you can normally cast. This is especially common  for monsters. |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/6/Text/2` | 0.556132 | A spell with the subtle trait can be cast  without incantations and doesn't have obvious  manifestations. Most of these spells enhance your  subterfuge or stealth, such as *invisibility*. Some  abilit |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/12` | 0.552213 | Spells that slightly alter a creature's form have the morph trait.  Any Strikes specifically granted by a magical morph effect also  gain the magical trait. You can be affected by multiple morph  spel |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/33/ListItem/20` | 0.551552 | **Tradition Resistance** If the dragon's magical tradition  matches that of your *dragon form* spell, you gain the  listed ability. **Arcane** resistance 5 against damage from  spells; **divine** resi |

### Query 57
- Text: Summarize **Arcane**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/6', 'PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/1', 'PZO22001 Starfinder Player Core 294-329::/page/8/Text/27']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/6', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/7', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/4']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/7` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/4` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/6` | 0.864568 | **Arcane** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/1` | 0.606128 | **SUBTLE SPELLS** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/8/Text/27` | 0.603141 | ARCANE 1ST-RANK SPELLS |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/79` | 0.556628 | **GAME** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/8` | 0.556432 | **Summoned** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/3` | 0.556234 | **SPELLSHAPE** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/13` | 0.551776 | **Occult** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/35` | 0.541799 | **EQUIPMENT** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/60` | 0.541799 | **EQUIPMENT** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/85` | 0.541799 | **EQUIPMENT** |

### Query 58
- Text: What is the rule about Arcane spellcasters use logic and  rationality to categorize the magic inherent  in the world around them. Because of its far-reaching  approach, the arcane tradition has the broadest spell  list, though it's generally poor at affecting the spirit or  the soul. Witchwarpers who analyze probability and  spellcasters who draw magic from the underlying code  of the Universe are practitioners of arcane magic.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/7', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/2', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/3']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/7', 'PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/9', 'PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/6']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/9` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/6` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/7` | 1.005577 | Arcane spellcasters use logic and  rationality to categorize the magic inherent  in the world around them. Because of its far-reaching  approach, the arcane tradition has the broadest spell  list, tho |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/2` | 0.691819 | Spellcasters cast spells from one of four different spell lists, each representing a different magical tradition: arcane,  divine, occult, and primal. |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/3` | 0.688762 | Even with the widespread presence of technology,  spellcasters can be found in every corner of the galaxy.  Some spellcasters draw magic from other realities, some  from their mystical connections to |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/3` | 0.653211 | Your class determines which tradition of magic your spells use. In some cases, such as when a mystic gains spells from  their connection or when a witchwarper learns spells from their paradox, you mig |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/15` | 0.619405 | systematic way. Witchwarpers touched by the Gap or  alternate timelines, as well as mystics who are psychically  linked to the Akashic Record, are occult spellcasters. |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/1` | 0.609729 | Whether it comes in the form of eldritch artifacts, otherworldly beings, or witchwarpers altering  reality with strange spells, magic brings fantasy and wonder to Starfinder. This chapter explains how |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/4` | 0.606975 | With special gestures and utterances, a spellcaster can  call forth mystic energies, warp the mind, protect themself  against danger, or even create something from nothing.  Each class has its own met |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/18` | 0.605866 | An instinctual connection to and faith in the  world, the cycle of day and night, the turning  of the seasons, and the natural selection of predator and  prey drive the primal tradition. Mystics conne |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/14` | 0.578419 | The practitioners of occult traditions seek  to understand the unexplainable, categorize  the bizarre, and otherwise access the ephemeral in a |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/4` | 0.578299 | Spellcasting creates obvious sensory manifestations, such  as bright lights, crackling sounds, and sharp smells from the  gathering magic. Nearly all spells manifest a spell signature—a  colorful, glo |

### Query 59
- Text: Summarize **Divine**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/9', 'PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/1', 'PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/8']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/9', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/7', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/10']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/7` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/10` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/9` | 0.857907 | **Divine** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/1` | 0.622090 | **SUBTLE SPELLS** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/8` | 0.619070 | **Summoned** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/13` | 0.571413 | **Occult** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/11/SectionHeader/45` | 0.567440 | DIVINE 1ST-RANK SPELLS |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/33` | 0.560886 | **GLOSSARY & ** **INDEX** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/20` | 0.555251 | **TRAITS** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/79` | 0.554681 | **GAME** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/27/Text/78` | 0.551413 | **INDEX** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/71` | 0.551413 | **INDEX** |

### Query 60
- Text: Summarize The power of the divine is steeped in faith,  the unseen, and belief in a power source from
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/10', 'PZO22001 Starfinder Player Core 294-329::/page/13/Text/22', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/11']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/10', 'PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/9', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/11']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/9` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/11` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/10` | 0.987089 | The power of the divine is steeped in faith,  the unseen, and belief in a power source from |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/22` | 0.654988 | **Divine Inspiration** Spiritual energy recovers a creature's  expended spell. |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/11` | 0.619134 | beyond the Universe. Mystics connected with the cosmic  forces of healing and shadows are divine spellcasters. |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/18` | 0.573604 | An instinctual connection to and faith in the  world, the cycle of day and night, the turning  of the seasons, and the natural selection of predator and  prey drive the primal tradition. Mystics conne |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/16/Text/43` | 0.573108 | **Guidance** Divine guidance improves one roll. |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/10/Text/53` | 0.546023 | **Truesight** See through illusions and physical transformations. **Vampiric Exsanguination**H Draw blood and life force from |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/32/SectionHeader/18` | 0.544356 | **DIVINE INSPIRATION **[two-actions] **SPELL 8**  **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** divine  **Range **touch;** Targets** 1 willing creature  You infuse a target with spiritual |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/12/Text/57` | 0.541353 | **Divine Immolation**H Call divine fire from the sky. |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/14/Text/65` | 0.536918 | **Clairaudience** Hear through an invisible magical sensor. |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/45` | 0.536918 | **Clairaudience** Hear through an invisible magical sensor. |

### Query 61
- Text: What is the rule about beyond the Universe. Mystics connected with the cosmic  forces of healing and shadows are divine spellcasters.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/11', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/18', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/12']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/11', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/10', 'PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/13']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/10` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/13` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/11` | 0.854248 | beyond the Universe. Mystics connected with the cosmic  forces of healing and shadows are divine spellcasters. |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/18` | 0.571904 | An instinctual connection to and faith in the  world, the cycle of day and night, the turning  of the seasons, and the natural selection of predator and  prey drive the primal tradition. Mystics conne |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/12` | 0.561670 | After Triune's Signal connected cultures across the  Universe, the peoples of the galaxy have learned more  than ever before about the Universe's composition  thanks to science and technology. As tech |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/3` | 0.518271 | Even with the widespread presence of technology,  spellcasters can be found in every corner of the galaxy.  Some spellcasters draw magic from other realities, some  from their mystical connections to |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/7` | 0.514074 | Arcane spellcasters use logic and  rationality to categorize the magic inherent  in the world around them. Because of its far-reaching  approach, the arcane tradition has the broadest spell  list, tho |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/10` | 0.513753 | The power of the divine is steeped in faith,  the unseen, and belief in a power source from |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/15` | 0.509710 | systematic way. Witchwarpers touched by the Gap or  alternate timelines, as well as mystics who are psychically  linked to the Akashic Record, are occult spellcasters. |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/3` | 0.505519 | Your class determines which tradition of magic your spells use. In some cases, such as when a mystic gains spells from  their connection or when a witchwarper learns spells from their paradox, you mig |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/22` | 0.504105 | If you are a spellcaster, your focus spells are the same tradition  of spell as the class that gave you the focus spell. A mystic's |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/19` | 0.491283 | are determined by their connection, and a witchwarper's are  determined by their paradox. |

### Query 62
- Text: Summarize **Occult**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/13', 'PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/1', 'PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/8']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/13', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/11', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/14']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/11` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/14` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/13` | 0.865280 | **Occult** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/1` | 0.682540 | **SUBTLE SPELLS** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/8` | 0.642814 | **Summoned** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/3` | 0.596109 | **Darkness and Light** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/30` | 0.593112 | **Rituals** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/84` | 0.593112 | **Rituals** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/40` | 0.593112 | **Rituals** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/90` | 0.593112 | **Rituals** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/65` | 0.593112 | **Rituals** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/37` | 0.593112 | **Rituals** |

### Query 63
- Text: What is the rule about The practitioners of occult traditions seek  to understand the unexplainable, categorize  the bizarre, and otherwise access the ephemeral in a?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/14']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/14', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/7', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/15']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/14', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/15', 'PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/13']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/15` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/13` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/14` | 0.949293 | The practitioners of occult traditions seek  to understand the unexplainable, categorize  the bizarre, and otherwise access the ephemeral in a |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/7` | 0.630738 | Arcane spellcasters use logic and  rationality to categorize the magic inherent  in the world around them. Because of its far-reaching  approach, the arcane tradition has the broadest spell  list, tho |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/15` | 0.625381 | systematic way. Witchwarpers touched by the Gap or  alternate timelines, as well as mystics who are psychically  linked to the Akashic Record, are occult spellcasters. |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/18` | 0.537911 | An instinctual connection to and faith in the  world, the cycle of day and night, the turning  of the seasons, and the natural selection of predator and  prey drive the primal tradition. Mystics conne |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/14/Text/74` | 0.527271 | insight about a topic. |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/11` | 0.523366 | beyond the Universe. Mystics connected with the cosmic  forces of healing and shadows are divine spellcasters. |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/19` | 0.515662 | are determined by their connection, and a witchwarper's are  determined by their paradox. |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/3` | 0.515259 | Your class determines which tradition of magic your spells use. In some cases, such as when a mystic gains spells from  their connection or when a witchwarper learns spells from their paradox, you mig |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/30/Text/40` | 0.515064 | **DETECT MAGIC **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **DETECTION** **MANIPULATE**  **Traditions** arcane, divine, occult, primal  **Area** 30-foot emanation  You send out a pulse |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/5` | 0.510863 | **Disappearance** Make a creature invisible, silent, and  undetectable by special senses. |

### Query 64
- Text: What is the rule about systematic way. Witchwarpers touched by the Gap or  alternate timelines, as well as mystics who are psychically  linked to the Akashic Record, are occult spellcasters.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/15']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/15', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/7', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/19']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/15', 'PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/17', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/14']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/17` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/14` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/15` | 0.921515 | systematic way. Witchwarpers touched by the Gap or  alternate timelines, as well as mystics who are psychically  linked to the Akashic Record, are occult spellcasters. |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/7` | 0.631763 | Arcane spellcasters use logic and  rationality to categorize the magic inherent  in the world around them. Because of its far-reaching  approach, the arcane tradition has the broadest spell  list, tho |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/19` | 0.613198 | are determined by their connection, and a witchwarper's are  determined by their paradox. |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/24` | 0.544036 | spells and precog warp spells, your mystic spells would  remain divine and the witchwarper spells occult. Similarly,  you need to use the attribute modifier determined by the  source of the focus spel |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/14` | 0.538327 | The practitioners of occult traditions seek  to understand the unexplainable, categorize  the bizarre, and otherwise access the ephemeral in a |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/11` | 0.531566 | beyond the Universe. Mystics connected with the cosmic  forces of healing and shadows are divine spellcasters. |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/22` | 0.525955 | If you are a spellcaster, your focus spells are the same tradition  of spell as the class that gave you the focus spell. A mystic's |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/3` | 0.515654 | Your class determines which tradition of magic your spells use. In some cases, such as when a mystic gains spells from  their connection or when a witchwarper learns spells from their paradox, you mig |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/18` | 0.507809 | An instinctual connection to and faith in the  world, the cycle of day and night, the turning  of the seasons, and the natural selection of predator and  prey drive the primal tradition. Mystics conne |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/2` | 0.506094 | Spellcasters cast spells from one of four different spell lists, each representing a different magical tradition: arcane,  divine, occult, and primal. |

### Query 65
- Text: Summarize **Primal**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/17']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/17', 'PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/1', 'PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/8']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/17', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/15', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/18']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/15` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/18` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/17` | 0.854029 | **Primal** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/1` | 0.741390 | **SUBTLE SPELLS** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/8` | 0.734544 | **Summoned** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/28` | 0.650258 | **INTRODUCTION** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/20` | 0.650258 | **INTRODUCTION** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/30` | 0.650258 | **INTRODUCTION** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/74` | 0.650258 | **INTRODUCTION** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/68` | 0.650258 | **INTRODUCTION** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/77` | 0.650258 | **INTRODUCTION** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/55` | 0.650258 | **INTRODUCTION** |

### Query 66
- Text: What is the rule about An instinctual connection to and faith in the  world, the cycle of day and night, the turning  of the seasons, and the natural selection of predator and  prey drive the primal tradition. Mystics connected to  the primordial elements and underlying rhythms of the  cosmos are primal spellcasters.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/18']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/18', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/3', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/26']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/18', 'PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/17', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/19']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/17` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/19` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/18` | 0.971215 | An instinctual connection to and faith in the  world, the cycle of day and night, the turning  of the seasons, and the natural selection of predator and  prey drive the primal tradition. Mystics conne |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/3` | 0.652633 | Your class determines which tradition of magic your spells use. In some cases, such as when a mystic gains spells from  their connection or when a witchwarper learns spells from their paradox, you mig |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/26` | 0.642719 | Certain spells are natural to your character, typically coming  from your ancestry or a magic item. They're called innate  spells. Innate spells don't let you qualify for abilities that  require you t |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/7` | 0.578921 | Arcane spellcasters use logic and  rationality to categorize the magic inherent  in the world around them. Because of its far-reaching  approach, the arcane tradition has the broadest spell  list, tho |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/2` | 0.572874 | Spellcasters cast spells from one of four different spell lists, each representing a different magical tradition: arcane,  divine, occult, and primal. |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/11` | 0.565419 | beyond the Universe. Mystics connected with the cosmic  forces of healing and shadows are divine spellcasters. |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/22` | 0.551966 | If you are a spellcaster, your focus spells are the same tradition  of spell as the class that gave you the focus spell. A mystic's |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/19` | 0.542637 | are determined by their connection, and a witchwarper's are  determined by their paradox. |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/33/ListItem/20` | 0.539333 | **Tradition Resistance** If the dragon's magical tradition  matches that of your *dragon form* spell, you gain the  listed ability. **Arcane** resistance 5 against damage from  spells; **divine** resi |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/21` | 0.534563 | **Tradition** This entry lists the magical traditions the spell  belongs to. Some feats or other abilities might add a  spell to your spell list even if you don't follow the listed  traditions. |

### Query 67
- Text: Summarize are determined by their connection, and a witchwarper's are  determined by their paradox.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/19']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/19', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/24', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/7']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/19', 'PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/20', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/18']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/20` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/18` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/19` | 0.979260 | are determined by their connection, and a witchwarper's are  determined by their paradox. |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/24` | 0.662300 | spells and precog warp spells, your mystic spells would  remain divine and the witchwarper spells occult. Similarly,  you need to use the attribute modifier determined by the  source of the focus spel |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/7` | 0.652315 | Arcane spellcasters use logic and  rationality to categorize the magic inherent  in the world around them. Because of its far-reaching  approach, the arcane tradition has the broadest spell  list, tho |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/15` | 0.610109 | systematic way. Witchwarpers touched by the Gap or  alternate timelines, as well as mystics who are psychically  linked to the Akashic Record, are occult spellcasters. |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/1` | 0.584365 | Whether it comes in the form of eldritch artifacts, otherworldly beings, or witchwarpers altering  reality with strange spells, magic brings fantasy and wonder to Starfinder. This chapter explains how |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/20` | 0.575149 | You spend 10 minutes performing deeds to restore your  magical connection. This restores 1 Focus Point to your focus  pool. The deeds you need to perform are specified in the class  or ability that gi |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/11` | 0.575032 | beyond the Universe. Mystics connected with the cosmic  forces of healing and shadows are divine spellcasters. |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/4` | 0.569447 | Spellcasting creates obvious sensory manifestations, such  as bright lights, crackling sounds, and sharp smells from the  gathering magic. Nearly all spells manifest a spell signature—a  colorful, glo |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/3` | 0.565981 | Your class determines which tradition of magic your spells use. In some cases, such as when a mystic gains spells from  their connection or when a witchwarper learns spells from their paradox, you mig |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/14/Text/74` | 0.560959 | insight about a topic. |

### Query 68
- Text: What is the rule about NON-SPELLCASTERS WITH  FOCUS SPELLS?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/20']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/20', 'PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/21', 'PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/12']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/20', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/19', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/21']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/19` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/21` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/20` | 0.872212 | NON-SPELLCASTERS WITH  FOCUS SPELLS |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/21` | 0.777302 | SPELLCASTERS WITH FOCUS  SPELLS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/12` | 0.635847 | FOCUS SPELLS |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/21` | 0.538412 | If you get focus spells from a class or other source that  doesn't grant spellcasting ability, the ability that gives you  focus spells also provides your proficiency for your spell  attack modifier a |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/5` | 0.524367 | SPELL SLOTS |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/13` | 0.519105 | Focus spells are a special type of spell attained directly from  a specific source, such as a field of study, connection to a  mystical force, or exposure to an alternate reality. You can  learn focus |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/13` | 0.515715 | SUSTAINING SPELLS |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/68` | 0.515280 | **Focus Spells** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/27/Text/71` | 0.515280 | **Focus Spells** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/27` | 0.515280 | **Focus Spells** |

### Query 69
- Text: Summarize FOCUS POINTS FROM MULTIPLE  SOURCES
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/22']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/22', 'PZO22001 Starfinder Player Core 294-329::/page/14/Text/74', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/29']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/22', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/23', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/21']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/23` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/21` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/22` | 0.956768 | FOCUS POINTS FROM MULTIPLE  SOURCES |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/14/Text/74` | 0.653259 | insight about a topic. |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/29` | 0.635211 | **Focus Spells** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/64` | 0.593211 | **Focus Spells** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/36` | 0.593211 | **Focus Spells** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/89` | 0.593211 | **Focus Spells** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/23/Text/46` | 0.593211 | **Focus Spells** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/27/Text/71` | 0.593211 | **Focus Spells** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/68` | 0.593211 | **Focus Spells** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/77` | 0.593211 | **Focus Spells** |

### Query 70
- Text: Summarize **INTRODUCTION**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/30']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/9/Text/80', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/30', 'PZO22001 Starfinder Player Core 294-329::/page/11/Text/77']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/30', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/28', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/31']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/28` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/31` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/80` | 0.913367 | **INTRODUCTION** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/30` | 0.913367 | **INTRODUCTION** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/77` | 0.913367 | **INTRODUCTION** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/28` | 0.871367 | **INTRODUCTION** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/20` | 0.871367 | **INTRODUCTION** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/68` | 0.871367 | **INTRODUCTION** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/59` | 0.871367 | **INTRODUCTION** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/54` | 0.871367 | **INTRODUCTION** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/55` | 0.871367 | **INTRODUCTION** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/27/Text/62` | 0.871367 | **INTRODUCTION** |

### Query 71
- Text: Summarize **CLASSES**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/32']
- Expected found: `True`
- Expected rank: `13`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/11/Text/79', 'PZO22001 Starfinder Player Core 294-329::/page/7/Text/30', 'PZO22001 Starfinder Player Core 294-329::/page/23/Text/40']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/32', 'PZO22001 Starfinder Player Core 294-329::/page/17/Text/82', 'PZO22001 Starfinder Player Core 294-329::/page/27/Text/64', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/33', 'PZO22001 Starfinder Player Core 294-329::/page/7/Text/30', 'PZO22001 Starfinder Player Core 294-329::/page/13/Text/70', 'PZO22001 Starfinder Player Core 294-329::/page/35/Text/64', 'PZO22001 Starfinder Player Core 294-329::/page/29/Text/61', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/31', 'PZO22001 Starfinder Player Core 294-329::/page/23/Text/40', 'PZO22001 Starfinder Player Core 294-329::/page/33/Text/57', 'PZO22001 Starfinder Player Core 294-329::/page/11/Text/79']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/17/Text/82` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/27/Text/64` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/33` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/7/Text/30` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/13/Text/70` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/35/Text/64` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/29/Text/61` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/31` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/23/Text/40` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/33/Text/57` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/11/Text/79` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/79` | 0.866254 | **CLASSES** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/30` | 0.866254 | **CLASSES** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/23/Text/40` | 0.866254 | **CLASSES** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/61` | 0.836254 | **CLASSES** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/56` | 0.836254 | **CLASSES** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/82` | 0.836254 | **CLASSES** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/64` | 0.836254 | **CLASSES** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/70` | 0.836254 | **CLASSES** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/27/Text/64` | 0.836254 | **CLASSES** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/76` | 0.836254 | **CLASSES** |

### Query 72
- Text: Summarize **EQUIPMENT**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/35']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/33/Text/60', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/35', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/25']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/35', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/34', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/36']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/34` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/36` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/60` | 0.915652 | **EQUIPMENT** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/35` | 0.915652 | **EQUIPMENT** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/25` | 0.915652 | **EQUIPMENT** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/82` | 0.873652 | **EQUIPMENT** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/85` | 0.873652 | **EQUIPMENT** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/85` | 0.873652 | **EQUIPMENT** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/79` | 0.873652 | **EQUIPMENT** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/64` | 0.873652 | **EQUIPMENT** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/73` | 0.873652 | **EQUIPMENT** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/23` | 0.873652 | **EQUIPMENT** |

### Query 73
- Text: Summarize **Rituals**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/40']
- Expected found: `True`
- Expected rank: `12`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/5/Text/30', 'PZO22001 Starfinder Player Core 294-329::/page/23/Text/47', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/28']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/40', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/39', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/41']
- Expanded expected found: `True`
- Expanded expected rank: `12`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/39` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/41` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/30` | 0.889916 | **Rituals** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/23/Text/47` | 0.889916 | **Rituals** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/28` | 0.889916 | **Rituals** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/64` | 0.847916 | **Rituals** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/90` | 0.847916 | **Rituals** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/87` | 0.847916 | **Rituals** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/90` | 0.847916 | **Rituals** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/84` | 0.847916 | **Rituals** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/78` | 0.847916 | **Rituals** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/65` | 0.847916 | **Rituals** |

### Query 74
- Text: Summarize **PLAYING THE ** **GAME**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/41']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/41', 'PZO22001 Starfinder Player Core 294-329::/page/9/Text/91', 'PZO22001 Starfinder Player Core 294-329::/page/7/Text/38']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/41', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/40', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/42']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/40` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/42` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/41` | 0.938833 | **PLAYING THE ** **GAME** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/91` | 0.938833 | **PLAYING THE ** **GAME** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/38` | 0.938833 | **PLAYING THE ** **GAME** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/66` | 0.896833 | **PLAYING THE ** **GAME** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/31` | 0.896833 | **PLAYING THE ** **GAME** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/65` | 0.896833 | **PLAYING THE ** **GAME** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/79` | 0.896833 | **PLAYING THE ** **GAME** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/70` | 0.896833 | **PLAYING THE ** **GAME** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/88` | 0.896833 | **PLAYING THE ** **GAME** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/64` | 0.896833 | **PLAYING THE ** **GAME** |

### Query 75
- Text: Summarize **CONDITIONS ** **APPENDIX**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/42']
- Expected found: `True`
- Expected rank: `5`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/27/Text/74', 'PZO22001 Starfinder Player Core 294-329::/page/7/Text/39', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/32']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/42', 'PZO22001 Starfinder Player Core 294-329::/page/13/Text/80', 'PZO22001 Starfinder Player Core 294-329::/page/31/Text/66', 'PZO22001 Starfinder Player Core 294-329::/page/27/Text/74', 'PZO22001 Starfinder Player Core 294-329::/page/33/Text/67', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/32', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/41', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/43', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/30', 'PZO22001 Starfinder Player Core 294-329::/page/29/Text/71', 'PZO22001 Starfinder Player Core 294-329::/page/23/Text/49', 'PZO22001 Starfinder Player Core 294-329::/page/35/Text/74']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/13/Text/80` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/31/Text/66` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/27/Text/74` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/33/Text/67` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/5/Text/32` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/41` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/43` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/30` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/29/Text/71` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/23/Text/49` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/35/Text/74` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/27/Text/74` | 0.950802 | **CONDITIONS ** **APPENDIX** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/39` | 0.950802 | **CONDITIONS ** **APPENDIX** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/32` | 0.950802 | **CONDITIONS ** **APPENDIX** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/89` | 0.920802 | **CONDITIONS ** **APPENDIX** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/42` | 0.920802 | **CONDITIONS ** **APPENDIX** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/80` | 0.920802 | **CONDITIONS ** **APPENDIX** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/66` | 0.920802 | **CONDITIONS ** **APPENDIX** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/86` | 0.920802 | **CONDITIONS ** **APPENDIX** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/92` | 0.920802 | **CONDITIONS ** **APPENDIX** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/92` | 0.920802 | **CONDITIONS ** **APPENDIX** |

### Query 76
- Text: Summarize **GLOSSARY & ** **INDEX**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/43']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/32', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/43', 'PZO22001 Starfinder Player Core 294-329::/page/9/Text/93']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/43', 'PZO22001 Starfinder Player Core 294-329::/page/4/Text/1', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/42']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/4/Text/1` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/42` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/32` | 0.929439 | **GLOSSARY & ** **INDEX** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/43` | 0.929439 | **GLOSSARY & ** **INDEX** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/93` | 0.929439 | **GLOSSARY & ** **INDEX** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/90` | 0.887439 | **GLOSSARY & ** **INDEX** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/40` | 0.887439 | **GLOSSARY & ** **INDEX** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/33` | 0.887439 | **GLOSSARY & ** **INDEX** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/93` | 0.887439 | **GLOSSARY & ** **INDEX** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/66` | 0.887439 | **GLOSSARY & ** **INDEX** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/87` | 0.887439 | **GLOSSARY & ** **INDEX** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/81` | 0.887439 | **GLOSSARY & ** **INDEX** |

### Query 77
- Text: Summarize COSTS AND LOCI
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/6', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/32', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/43']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/6', 'PZO22001 Starfinder Player Core 294-329::/page/4/Text/7', 'PZO22001 Starfinder Player Core 294-329::/page/4/Text/5']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/4/Text/7` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/4/Text/5` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/6` | 0.921624 | COSTS AND LOCI |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/32` | 0.521823 | **GLOSSARY & ** **INDEX** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/43` | 0.521823 | **GLOSSARY & ** **INDEX** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/33` | 0.479823 | **GLOSSARY & ** **INDEX** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/81` | 0.479823 | **GLOSSARY & ** **INDEX** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/90` | 0.479823 | **GLOSSARY & ** **INDEX** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/93` | 0.479823 | **GLOSSARY & ** **INDEX** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/40` | 0.479823 | **GLOSSARY & ** **INDEX** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/87` | 0.479823 | **GLOSSARY & ** **INDEX** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/23/Text/50` | 0.479823 | **GLOSSARY & ** **INDEX** |

### Query 78
- Text: Summarize LONG CASTING TIMES
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/9', 'PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/15', 'PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/2']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/9', 'PZO22001 Starfinder Player Core 294-329::/page/4/Text/10', 'PZO22001 Starfinder Player Core 294-329::/page/4/Text/8']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/4/Text/10` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/4/Text/8` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/9` | 0.866559 | LONG CASTING TIMES |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/15` | 0.732872 | LONG DURATIONS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/2` | 0.641742 | CASTING SPELLS |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/21` | 0.567502 | SPELLCASTERS WITH FOCUS  SPELLS |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/9` | 0.558353 | DURATIONS |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/22` | 0.541037 | FOCUS POINTS FROM MULTIPLE  SOURCES |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/1` | 0.537685 | **SUBTLE SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/11` | 0.533544 | **SPELLCASTING IN STARFINDER** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/8/SectionHeader/1` | 0.528853 | SPELL LISTS |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/73` | 0.517245 | **PLAYING THE ** |

### Query 79
- Text: Summarize RANGES, AREAS, AND  TARGETS
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/14']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/14', 'PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/20', 'PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/16']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/14', 'PZO22001 Starfinder Player Core 294-329::/page/4/Text/13', 'PZO22001 Starfinder Player Core 294-329::/page/4/Text/15']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/4/Text/13` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/4/Text/15` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/14` | 0.925952 | RANGES, AREAS, AND  TARGETS |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/20` | 0.702411 | TARGETS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/16` | 0.648479 | TOUCH RANGE |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/22` | 0.605442 | FOCUS POINTS FROM MULTIPLE  SOURCES |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/23` | 0.604180 | **Range, Area, and Targets** This entry lists the range of the  spell, the area it affects, and the targets it can affect, if  any. If none of these entries are present, the spell affects  only the ca |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/41` | 0.589768 | **ANALYZE TARGET **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **DETECTION** **MANIPULATE**  **Traditions** arcane, divine, occult, primal **Range **30 feet; **Targets** 1 creature  **Dur |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/14/Text/74` | 0.583321 | insight about a topic. |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/16/Text/38` | 0.569813 | **Analyze** **Target**H Gather data about a target's basic physiology. **Caustic Blast**H Fling a glob of acid that splashes a small area. |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/8/Text/8` | 0.569813 | **Analyze** **Target**H Gather data about a target's basic physiology. **Caustic Blast**H Fling a glob of acid that splashes a small area. |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/23/ListItem/14` | 0.565237 | slashing; **Ranged **[one-action] hearth blaze (fire, range 120 feet),  **Damage **6d6+3 fire. |

### Query 80
- Text: Summarize TOUCH RANGE
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/16']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/16', 'PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/14', 'PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/28']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/16', 'PZO22001 Starfinder Player Core 294-329::/page/4/Text/17', 'PZO22001 Starfinder Player Core 294-329::/page/4/Text/15']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/4/Text/17` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/4/Text/15` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/16` | 0.935916 | TOUCH RANGE |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/14` | 0.668447 | RANGES, AREAS, AND  TARGETS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/28` | 0.632695 | **ADHERE **[one-action] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult, primal  **Range **touch; **Targets** 1 held or unattended object or a 5-footsquare sur |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/17` | 0.571230 | A spell with a touch range requires you to physically touch  the target. You use your unarmed reach to determine  whether you can touch the creature. You can usually touch  them automatically, though |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/14/Text/74` | 0.561407 | insight about a topic. |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/19/ListItem/45` | 0.545209 | Low-light vision. |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/22` | 0.543757 | FOCUS POINTS FROM MULTIPLE  SOURCES |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/35/SectionHeader/14` | 0.539725 | **EMBED MESSAGE **[two-actions] **SPELL 2**  **CONCENTRATE** **ILLUSION** **MANIPULATE**  **Traditions** arcane, occult  **Range **touch; **Targets** 1 object or willing creature  **Duration** unlimit |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/15` | 0.530996 | Spells with a range can affect targets, create areas, or make  things appear only within that range. Most spell ranges are  measured in feet, though some can stretch over miles, reach  anywhere on the |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/35` | 0.530246 | **Skim** **Data** Touch an object to get the gist of the data in it. |

### Query 81
- Text: Summarize AREAS
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/18']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/18', 'PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/22', 'PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/14']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/18', 'PZO22001 Starfinder Player Core 294-329::/page/4/Text/17', 'PZO22001 Starfinder Player Core 294-329::/page/4/Text/19']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/4/Text/17` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/4/Text/19` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/18` | 0.786930 | AREAS |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/22` | 0.633377 | FOCUS POINTS FROM MULTIPLE  SOURCES |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/14` | 0.618725 | RANGES, AREAS, AND  TARGETS |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/14/Text/74` | 0.572139 | insight about a topic. |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/7/SectionHeader/6` | 0.562759 | COUNTERACTING |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/8` | 0.552468 | **Summoned** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/48` | 0.541603 | **Bane** Weaken enemies' attacks in an aura around you. |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/61` | 0.541603 | **Bane** Weaken enemies' attacks in an aura around you. |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/20` | 0.533251 | TARGETS |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/1` | 0.532771 | **SUBTLE SPELLS** |

### Query 82
- Text: Summarize TARGETS
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/20']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/20', 'PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/22', 'PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/14']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/20', 'PZO22001 Starfinder Player Core 294-329::/page/4/Text/21', 'PZO22001 Starfinder Player Core 294-329::/page/4/Text/19']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/4/Text/21` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/4/Text/19` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/20` | 0.819956 | TARGETS |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/22` | 0.672032 | FOCUS POINTS FROM MULTIPLE  SOURCES |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/14` | 0.670988 | RANGES, AREAS, AND  TARGETS |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/42` | 0.586946 | **Analyze** **Target**H Gather data about a target's basic physiology. **Daze**H Cloud a creature's mind and possibly stun it. |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/29` | 0.586946 | **Analyze** **Target**H Gather data about a target's basic physiology. **Daze**H Cloud a creature's mind and possibly stun it. |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/83` | 0.579400 | **Focus Spells** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/39` | 0.579400 | **Focus Spells** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/36` | 0.579400 | **Focus Spells** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/89` | 0.579400 | **Focus Spells** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/63` | 0.579400 | **Focus Spells** |

### Query 83
- Text: Summarize **Darkness and Light**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/3']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/3', 'PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/13', 'PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/8']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/3', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/4', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/2']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/5/Text/4` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/5/Text/2` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/3` | 0.864769 | **Darkness and Light** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/13` | 0.619843 | **Occult** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/8` | 0.613011 | **Summoned** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/19/ListItem/45` | 0.566831 | Low-light vision. |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/80` | 0.565701 | **INTRODUCTION** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/62` | 0.565700 | **INTRODUCTION** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/20` | 0.565700 | **INTRODUCTION** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/74` | 0.565700 | **INTRODUCTION** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/28` | 0.565700 | **INTRODUCTION** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/77` | 0.565700 | **INTRODUCTION** |

### Query 84
- Text: Summarize **Minion**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/5', 'PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/8', 'PZO22001 Starfinder Player Core 294-329::/page/14/Text/17']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/5', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/6', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/4']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/5/Text/6` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/5/Text/4` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/5` | 0.858882 | **Minion** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/8` | 0.623420 | **Summoned** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/14/Text/17` | 0.617114 | **Phantasmal Minion **Create a creature of force to perform  minor tasks. |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/8/Text/57` | 0.575114 | **Phantasmal Minion **Create a creature of force to perform  minor tasks. |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/79` | 0.556332 | **GAME** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/34` | 0.552114 | **Shrink**H Reduce a willing creature to Tiny size. |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/9` | 0.548824 | **Divine** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/6` | 0.548466 | **Arcane** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/7` | 0.547771 | A minion has only 2 actions and 0 reactions per turn,  though certain conditions (such as slowed or quickened)  or abilities might give them additional actions or a reaction.  Alterations to a minion' |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/20` | 0.543383 | **TRAITS** |

### Query 85
- Text: Summarize **Summoned**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/8']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/8', 'PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/1', 'PZO22001 Starfinder Player Core 294-329::/page/35/Text/79']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/8', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/9', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/7']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/5/Text/9` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/5/Text/7` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/8` | 0.927061 | **Summoned** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/1` | 0.763911 | **SUBTLE SPELLS** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/79` | 0.706363 | **GAME** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/37` | 0.664048 | **Spell Lists** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/62` | 0.664048 | **Spell Lists** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/87` | 0.664048 | **Spell Lists** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/34` | 0.664048 | **Spell Lists** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/84` | 0.664048 | **Spell Lists** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/27` | 0.664048 | **Spell Lists** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/81` | 0.664048 | **Spell Lists** |

### Query 86
- Text: Summarize **Morph**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/11', 'PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/8', 'PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/13']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/11', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/10', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/12']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/5/Text/10` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/5/Text/12` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/11` | 0.879467 | **Morph** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/8` | 0.676426 | **Summoned** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/13` | 0.646977 | **Polymorph** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/3` | 0.593929 | **SPELLSHAPE** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/1` | 0.587749 | **SUBTLE SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/80` | 0.571801 | **INTRODUCTION** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/20` | 0.571801 | **INTRODUCTION** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/18` | 0.571801 | **INTRODUCTION** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/80` | 0.571801 | **INTRODUCTION** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/68` | 0.571801 | **INTRODUCTION** |

### Query 87
- Text: Summarize **Polymorph**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/13', 'PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/3', 'PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/8']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/13', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/14', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/12']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/5/Text/14` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/5/Text/12` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/13` | 0.886981 | **Polymorph** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/3` | 0.660740 | **SPELLSHAPE** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/8` | 0.660083 | **Summoned** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/11` | 0.611521 | **Morph** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/1` | 0.561675 | **SUBTLE SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/79` | 0.553185 | **GAME** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/16` | 0.545548 | **Illusions** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/13` | 0.544130 | **Occult** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/73` | 0.541918 | **PLAYING THE ** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/5` | 0.538644 | **Minion** |

### Query 88
- Text: Summarize **Illusions**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/16']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/16', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/30', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/20']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/16', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/15', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/17']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/5/Text/15` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/5/Text/17` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/16` | 0.922764 | **Illusions** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/30` | 0.707975 | **INTRODUCTION** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/20` | 0.707975 | **INTRODUCTION** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/77` | 0.665975 | **INTRODUCTION** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/55` | 0.665975 | **INTRODUCTION** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/28` | 0.665975 | **INTRODUCTION** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/80` | 0.665975 | **INTRODUCTION** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/59` | 0.665975 | **INTRODUCTION** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/62` | 0.665975 | **INTRODUCTION** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/18` | 0.665975 | **INTRODUCTION** |

### Query 89
- Text: Summarize If a creature engages with an illusion in a way that would  prove it's not what it seems, the creature might know that an  illusion is present, but it still can't ignore the illusion without  successfully disbelieving it. Disbelieving a visual illusion makes  it and those things it blocks seem hazy and indistinct, which  might block vision enough to leave the other side concealed.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/5/Text/18']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/5/Text/18', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/17', 'PZO22001 Starfinder Player Core 294-329::/page/7/Text/13']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/5/Text/18', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/20', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/17']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/5/Text/20` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/5/Text/17` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/18` | 1.019996 | If a creature engages with an illusion in a way that would  prove it's not what it seems, the creature might know that an  illusion is present, but it still can't ignore the illusion without  successf |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/17` | 0.798623 | Magic with the illusion trait creates false sensory stimuli.  Sometimes illusions allow creatures a chance to disbelieve  the spell, which lets the creature ignore the spell if it succeeds  at doing s |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/13` | 0.751315 | Disguises and illusions fool the spell as long as they  appear to match its parameters. For a spell to detect  something visually, the spell's origin point must have line of  sight. Darkness doesn't p |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/46` | 0.693409 | **Hallucination**H Cause a creature to believe one thing is  another, to notice something that isn't there, or to be  unable to detect something. |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/10/Text/20` | 0.693409 | **Hallucination**H Cause a creature to believe one thing is  another, to notice something that isn't there, or to be  unable to detect something. |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/8/Text/49` | 0.676311 | **Illusory Disguise**H Make yourself look like a different creature. **Illusory Object**H Form a convincing illusion of an object. |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/14/Text/42` | 0.672123 | **Illusory Creature**H Form a convincing illusion of a creature. |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/23` | 0.672123 | **Illusory Creature**H Form a convincing illusion of a creature. |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/2` | 0.661116 | **Failure** The creature is fascinated by the display and  frightened 2 (even if the fascination ends). |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/12` | 0.656053 | might be the presence of a type of creature, such as "creatures  with six or more tentacles," or it could be an observed action,  such as "whenever someone enters the spell's area." |

### Query 90
- Text: Summarize **INTRODUCTION**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/5/Text/20']
- Expected found: `True`
- Expected rank: `5`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/9/Text/80', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/30', 'PZO22001 Starfinder Player Core 294-329::/page/11/Text/77']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/5/Text/20', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/21', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/18']
- Expanded expected found: `True`
- Expanded expected rank: `5`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/5/Text/21` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/5/Text/18` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/80` | 0.913367 | **INTRODUCTION** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/30` | 0.913367 | **INTRODUCTION** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/77` | 0.913367 | **INTRODUCTION** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/28` | 0.871367 | **INTRODUCTION** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/20` | 0.871367 | **INTRODUCTION** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/68` | 0.871367 | **INTRODUCTION** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/59` | 0.871367 | **INTRODUCTION** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/54` | 0.871367 | **INTRODUCTION** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/55` | 0.871367 | **INTRODUCTION** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/27/Text/62` | 0.871367 | **INTRODUCTION** |

### Query 91
- Text: Summarize **CLASSES**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/5/Text/22']
- Expected found: `True`
- Expected rank: `14`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/11/Text/79', 'PZO22001 Starfinder Player Core 294-329::/page/7/Text/30', 'PZO22001 Starfinder Player Core 294-329::/page/23/Text/40']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/5/Text/22', 'PZO22001 Starfinder Player Core 294-329::/page/17/Text/82', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/32', 'PZO22001 Starfinder Player Core 294-329::/page/31/Text/56', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/23', 'PZO22001 Starfinder Player Core 294-329::/page/27/Text/64', 'PZO22001 Starfinder Player Core 294-329::/page/23/Text/40', 'PZO22001 Starfinder Player Core 294-329::/page/7/Text/30', 'PZO22001 Starfinder Player Core 294-329::/page/15/Text/76', 'PZO22001 Starfinder Player Core 294-329::/page/33/Text/57', 'PZO22001 Starfinder Player Core 294-329::/page/11/Text/79', 'PZO22001 Starfinder Player Core 294-329::/page/19/Text/55']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/17/Text/82` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/32` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/31/Text/56` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/5/Text/23` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/27/Text/64` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/23/Text/40` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/7/Text/30` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/15/Text/76` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/33/Text/57` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/11/Text/79` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/19/Text/55` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/79` | 0.866254 | **CLASSES** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/30` | 0.866254 | **CLASSES** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/23/Text/40` | 0.866254 | **CLASSES** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/61` | 0.836254 | **CLASSES** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/56` | 0.836254 | **CLASSES** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/82` | 0.836254 | **CLASSES** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/64` | 0.836254 | **CLASSES** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/70` | 0.836254 | **CLASSES** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/27/Text/64` | 0.836254 | **CLASSES** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/76` | 0.836254 | **CLASSES** |

### Query 92
- Text: Summarize **EQUIPMENT**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/5/Text/25']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/33/Text/60', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/35', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/25']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/5/Text/25', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/24', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/26']
- Expanded expected found: `True`
- Expanded expected rank: `3`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/5/Text/24` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/5/Text/26` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/60` | 0.915652 | **EQUIPMENT** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/35` | 0.915652 | **EQUIPMENT** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/25` | 0.915652 | **EQUIPMENT** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/82` | 0.873652 | **EQUIPMENT** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/85` | 0.873652 | **EQUIPMENT** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/85` | 0.873652 | **EQUIPMENT** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/79` | 0.873652 | **EQUIPMENT** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/64` | 0.873652 | **EQUIPMENT** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/73` | 0.873652 | **EQUIPMENT** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/23` | 0.873652 | **EQUIPMENT** |

### Query 93
- Text: Summarize **Rituals**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/5/Text/30']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/5/Text/30', 'PZO22001 Starfinder Player Core 294-329::/page/23/Text/47', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/28']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/5/Text/30', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/29', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/31']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/5/Text/29` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/5/Text/31` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/30` | 0.889916 | **Rituals** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/23/Text/47` | 0.889916 | **Rituals** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/28` | 0.889916 | **Rituals** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/64` | 0.847916 | **Rituals** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/90` | 0.847916 | **Rituals** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/87` | 0.847916 | **Rituals** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/90` | 0.847916 | **Rituals** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/84` | 0.847916 | **Rituals** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/78` | 0.847916 | **Rituals** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/65` | 0.847916 | **Rituals** |

### Query 94
- Text: Summarize **PLAYING THE ** **GAME**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/5/Text/31']
- Expected found: `True`
- Expected rank: `5`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/41', 'PZO22001 Starfinder Player Core 294-329::/page/9/Text/91', 'PZO22001 Starfinder Player Core 294-329::/page/7/Text/38']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/5/Text/31', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/32', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/30']
- Expanded expected found: `True`
- Expanded expected rank: `5`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/5/Text/32` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/5/Text/30` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/41` | 0.938833 | **PLAYING THE ** **GAME** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/91` | 0.938833 | **PLAYING THE ** **GAME** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/38` | 0.938833 | **PLAYING THE ** **GAME** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/66` | 0.896833 | **PLAYING THE ** **GAME** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/31` | 0.896833 | **PLAYING THE ** **GAME** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/65` | 0.896833 | **PLAYING THE ** **GAME** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/79` | 0.896833 | **PLAYING THE ** **GAME** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/70` | 0.896833 | **PLAYING THE ** **GAME** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/88` | 0.896833 | **PLAYING THE ** **GAME** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/64` | 0.896833 | **PLAYING THE ** **GAME** |

### Query 95
- Text: Summarize **CONDITIONS ** **APPENDIX**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/5/Text/32']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/27/Text/74', 'PZO22001 Starfinder Player Core 294-329::/page/7/Text/39', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/32']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/5/Text/32', 'PZO22001 Starfinder Player Core 294-329::/page/35/Text/74', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/31', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/33', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/42', 'PZO22001 Starfinder Player Core 294-329::/page/9/Text/92', 'PZO22001 Starfinder Player Core 294-329::/page/13/Text/80', 'PZO22001 Starfinder Player Core 294-329::/page/7/Text/39', 'PZO22001 Starfinder Player Core 294-329::/page/17/Text/92', 'PZO22001 Starfinder Player Core 294-329::/page/19/Text/65', 'PZO22001 Starfinder Player Core 294-329::/page/31/Text/66', 'PZO22001 Starfinder Player Core 294-329::/page/29/Text/71']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/35/Text/74` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/5/Text/31` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/5/Text/33` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/42` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/9/Text/92` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/13/Text/80` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/7/Text/39` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/17/Text/92` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/19/Text/65` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/31/Text/66` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/29/Text/71` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/27/Text/74` | 0.950802 | **CONDITIONS ** **APPENDIX** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/39` | 0.950802 | **CONDITIONS ** **APPENDIX** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/32` | 0.950802 | **CONDITIONS ** **APPENDIX** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/89` | 0.920802 | **CONDITIONS ** **APPENDIX** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/42` | 0.920802 | **CONDITIONS ** **APPENDIX** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/80` | 0.920802 | **CONDITIONS ** **APPENDIX** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/66` | 0.920802 | **CONDITIONS ** **APPENDIX** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/86` | 0.920802 | **CONDITIONS ** **APPENDIX** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/92` | 0.920802 | **CONDITIONS ** **APPENDIX** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/92` | 0.920802 | **CONDITIONS ** **APPENDIX** |

### Query 96
- Text: Summarize **GLOSSARY & ** **INDEX**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/5/Text/33']
- Expected found: `True`
- Expected rank: `6`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/32', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/43', 'PZO22001 Starfinder Player Core 294-329::/page/9/Text/93']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/5/Text/33', 'PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/1', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/32']
- Expanded expected found: `True`
- Expanded expected rank: `6`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/1` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/5/Text/32` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/32` | 0.929439 | **GLOSSARY & ** **INDEX** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/43` | 0.929439 | **GLOSSARY & ** **INDEX** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/93` | 0.929439 | **GLOSSARY & ** **INDEX** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/90` | 0.887439 | **GLOSSARY & ** **INDEX** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/40` | 0.887439 | **GLOSSARY & ** **INDEX** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/33` | 0.887439 | **GLOSSARY & ** **INDEX** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/93` | 0.887439 | **GLOSSARY & ** **INDEX** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/66` | 0.887439 | **GLOSSARY & ** **INDEX** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/87` | 0.887439 | **GLOSSARY & ** **INDEX** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/81` | 0.887439 | **GLOSSARY & ** **INDEX** |

### Query 97
- Text: Summarize LINE OF EFFECT
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/7', 'PZO22001 Starfinder Player Core 294-329::/page/14/Text/74', 'PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/1']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/7', 'PZO22001 Starfinder Player Core 294-329::/page/6/Text/8', 'PZO22001 Starfinder Player Core 294-329::/page/6/Text/6']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/6/Text/8` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/6/Text/6` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/7` | 0.893147 | LINE OF EFFECT |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/14/Text/74` | 0.612539 | insight about a topic. |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/1` | 0.596336 | **SUBTLE SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/25` | 0.550657 | A horizontal line follows defense and duration, and the  effects of the spell are described after this line. This section  might also detail the possible results of a saving throw:  critical success, |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/13` | 0.542803 | SPONTANEOUS SPELLS |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/22` | 0.536078 | FOCUS POINTS FROM MULTIPLE  SOURCES |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/19/ListItem/45` | 0.531353 | Low-light vision. |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/15` | 0.520184 | LONG DURATIONS |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/14` | 0.519180 | RANGES, AREAS, AND  TARGETS |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/20` | 0.518311 | TARGETS |

### Query 98
- Text: Summarize DURATIONS
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/9', 'PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/15', 'PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/1']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/9', 'PZO22001 Starfinder Player Core 294-329::/page/6/Text/8', 'PZO22001 Starfinder Player Core 294-329::/page/6/Text/10']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/6/Text/8` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/6/Text/10` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/9` | 0.806102 | DURATIONS |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/15` | 0.775048 | LONG DURATIONS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/1` | 0.629098 | **SUBTLE SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/8/Text/53` | 0.571332 | **Mindlink** Mentally impart 10 minutes worth of information  in an instant. |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/14/Text/14` | 0.570439 | **Mindlink** Mentally impart 10 minutes' worth of information  in an instant. |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/14/Text/74` | 0.569121 | insight about a topic. |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/30` | 0.558285 | **INTRODUCTION** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/20` | 0.558285 | **INTRODUCTION** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/55` | 0.558285 | **INTRODUCTION** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/74` | 0.558285 | **INTRODUCTION** |

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
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/15` | 0.884685 | LONG DURATIONS |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/9` | 0.783631 | DURATIONS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/9` | 0.673337 | LONG CASTING TIMES |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/22` | 0.573493 | FOCUS POINTS FROM MULTIPLE  SOURCES |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/1` | 0.568954 | **SUBTLE SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/14/Text/74` | 0.557157 | insight about a topic. |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/80` | 0.548292 | **INTRODUCTION** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/30` | 0.548292 | **INTRODUCTION** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/80` | 0.548292 | **INTRODUCTION** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/53` | 0.548292 | **INTRODUCTION** |

### Query 100
- Text: What does **ABSOLUTE ZERO **[two-actions] **SPELL 7** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/4']
- Expected found: `True`
- Expected rank: `6`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0', 'PZO22001 Starfinder Player Core 294-329::/page/16/SectionHeader/5', 'PZO22001 Starfinder Player Core 294-329::/page/18/Text/35']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/4', 'PZO22001 Starfinder Player Core 294-329::/page/19/Text/2', 'PZO22001 Starfinder Player Core 294-329::/page/19/Text/11']
- Expanded expected found: `True`
- Expanded expected rank: `6`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/19/Text/2` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/19/Text/11` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0` | 0.644164 | CHAPTER 7: SPELLS |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/16/SectionHeader/5` | 0.625816 | OCCULT 7TH-RANK SPELLS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/18/Text/35` | 0.613405 | **Absolute** **Zero**H Flash freeze and slow creatures. |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/10/Text/58` | 0.571405 | **Absolute** **Zero**H Flash freeze and slow creatures. |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/31/SectionHeader/12` | 0.570625 | **DISAPPEARANCE **[two-actions] **SPELL 8**  **ILLUSION** **MANIPULATE** **SUBTLE**  **Traditions** arcane, occult  **Range **touch; **Targets** 1 creature  **Duration** 10 minutes  You shroud a creat |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/4` | 0.566429 | **ABSOLUTE ZERO **[two-actions] **SPELL 7**  **COLD** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal  **Range **500 feet; **Area** 30-foot burst  **Defense** Fortitude  A swirling vorte |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/18/SectionHeader/34` | 0.562011 | PRIMAL 7TH-RANK SPELLS |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/30/Text/15` | 0.557101 | **DEATH SENTENCE **[two-actions] **SPELL 7**  **AUDITORY** **CONCENTRATE** **DEATH** **INCAPACITATION** **SPIRIT**  **Traditions** divine, primal  **Range **30 feet;** Targets** 1 creature  **Defense* |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/34/SectionHeader/6` | 0.553834 | **ECLIPSE BURST **[two-actions] **SPELL 7**  **COLD** **CONCENTRATE** **DARKNESS** **MANIPULATE** **VOID**  **Traditions** arcane, divine, primal **Range **500 feet;** Area** 60-foot burst  **Defense* |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/10/SectionHeader/57` | 0.552998 | ARCANE 7TH-RANK SPELLS |

### Query 101
- Text: What does **ACID GRIP **[two-actions] **SPELL 2** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/16']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/16', 'PZO22001 Starfinder Player Core 294-329::/page/9/SectionHeader/4', 'PZO22001 Starfinder Player Core 294-329::/page/14/SectionHeader/25']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/16', 'PZO22001 Starfinder Player Core 294-329::/page/19/Text/23', 'PZO22001 Starfinder Player Core 294-329::/page/19/Text/15']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/19/Text/23` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/19/Text/15` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/16` | 0.690187 | **ACID GRIP **[two-actions] **SPELL 2**  **ACID** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal  **Range **120 feet;** Targets** 1 creature  **Defense** Reflex  An ephemeral, taloned h |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/9/SectionHeader/4` | 0.627322 | ARCANE 2ND-RANK SPELLS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/14/SectionHeader/25` | 0.616441 | OCCULT 2ND-RANK SPELLS |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/19` | 0.546143 | **CAUSTIC BLAST **[two-actions] **CANTRIP 1**  **ACID** **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal  **Range **30 feet; **Area** 5-foot burst  **Defense** basic Reflex  Y |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/17/SectionHeader/17` | 0.543332 | PRIMAL 2ND-RANK SPELLS |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/5` | 0.541267 | **Acid Grip**H Move and harm foes with a hand of acid. |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/11/SectionHeader/71` | 0.538755 | DIVINE 2ND-RANK SPELLS |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/27` | 0.537821 | **CAUSTIC CONVERSION **[two-actions] **SPELL 2**  **ACID** **ATTACK** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal  **Range **120 feet;** Targets** 1 creature  **Defense** AC  You lau |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/18` | 0.529267 | **Acid Grip**H Move and harm foes with a hand of acid. |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/31/SectionHeader/47` | 0.517919 | **DISPEL MAGIC **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, occult, primal  **Range **120 feet;** Targets** 1 spell effect or unattended magic  item  You |

### Query 102
- Text: What does **ADHERE **[one-action] **CANTRIP 1** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/28']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/28', 'PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/41', 'PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/19']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/28', 'PZO22001 Starfinder Player Core 294-329::/page/19/Text/27', 'PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/36']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/19/Text/27` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/36` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/28` | 0.757033 | **ADHERE **[one-action] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult, primal  **Range **touch; **Targets** 1 held or unattended object or a 5-footsquare sur |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/41` | 0.624693 | **ANALYZE TARGET **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **DETECTION** **MANIPULATE**  **Traditions** arcane, divine, occult, primal **Range **30 feet; **Targets** 1 creature  **Dur |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/19` | 0.612819 | **CAUSTIC BLAST **[two-actions] **CANTRIP 1**  **ACID** **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal  **Range **30 feet; **Area** 5-foot burst  **Defense** basic Reflex  Y |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/30/Text/2` | 0.568812 | **DAZE **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **MANIPULATE** **MENTAL** **NONLETHAL**  **Traditions** arcane, divine, occult **Range **60 feet; **Targets** 1 creature **Defense** W |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/34/SectionHeader/38` | 0.556885 | **ELECTRIC ARC **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **ELECTRICITY** **MANIPULATE**  **Traditions** arcane, primal  **Range **30 feet; **Targets** 1 or 2 creatures  **Defense** ba |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/32/SectionHeader/24` | 0.547724 | **DIVINE LANCE **[two-actions] **CANTRIP 1**  **ATTACK** **CANTRIP** **CONCENTRATE** **MANIPULATE** **SANCTIFIED** **SPIRIT**  **Traditions** divine  **Range **60 feet; **Targets** 1 creature  **Defen |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/30/Text/40` | 0.542630 | **DETECT MAGIC **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **DETECTION** **MANIPULATE**  **Traditions** arcane, divine, occult, primal  **Area** 30-foot emanation  You send out a pulse |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/34/SectionHeader/18` | 0.536232 | **ELDRITCH LANCE **[two-actions] **CANTRIP 1**  **ATTACK** **CANTRIP** **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** divine, occult  **Range **30 feet; **Targets** 1 creature  **Defense** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/16/Text/37` | 0.527467 | **Adhere** Bond two objects together or charge a surface with  adhesive magic. |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/8/Text/7` | 0.527467 | **Adhere** Bond two objects together or charge a surface with  adhesive magic. |

### Query 103
- Text: What does **AERIAL FORM **[two-actions] **SPELL 4** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/36']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/36', 'PZO22001 Starfinder Player Core 294-329::/page/9/SectionHeader/71', 'PZO22001 Starfinder Player Core 294-329::/page/34/SectionHeader/53']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/36', 'PZO22001 Starfinder Player Core 294-329::/page/19/ListItem/45', 'PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/28']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/19/ListItem/45` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/28` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/36` | 0.693908 | **AERIAL FORM **[two-actions] **SPELL 4**  **CONCENTRATE** **MANIPULATE** **POLYMORPH**  **Traditions** arcane, primal  **Duration** 1 minute  You harness your mastery of the sky to reshape your body |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/9/SectionHeader/71` | 0.638850 | ARCANE 4TH-RANK SPELLS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/34/SectionHeader/53` | 0.627936 | **ELEMENTAL FORM **[two-actions] **SPELL 5**  **CONCENTRATE** **MANIPULATE** **POLYMORPH**  **Traditions** arcane, primal  **Duration** 1 minute  You call upon the power of the planes to transform int |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/15/SectionHeader/17` | 0.577329 | OCCULT 4TH-RANK SPELLS |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/32/SectionHeader/1` | 0.571259 | **DISPELLING GLOBE **[two-actions] **SPELL 4**  **UNCOMMON** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, occult  **Area** 10-foot burst centered on one corner of your space **Durati |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/17/SectionHeader/71` | 0.571236 | PRIMAL 4TH-RANK SPELLS |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/33/SectionHeader/36` | 0.565677 | **EARTHBIND **[two-actions] **SPELL 3**  **CONCENTRATE** **EARTH** **MANIPULATE**  **Traditions** arcane, primal  **Range **120 feet;** Targets** 1 flying creature  **Defense** Fortitude; **Duration** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/23` | 0.560370 | SPELL ATTACKS |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/28/Text/11` | 0.555441 | **CONFUSION **[two-actions] **SPELL 4**  **CONCENTRATE** **EMOTION** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult **Range **30 feet;** Targets** 1 creature **Defense** Will; **Duration** 1 |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/12/SectionHeader/40` | 0.544975 | DIVINE 4TH-RANK SPELLS |

### Query 104
- Text: What does **AIR BUBBLE **[reaction] **SPELL 1** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/4', 'PZO22001 Starfinder Player Core 294-329::/page/8/Text/28', 'PZO22001 Starfinder Player Core 294-329::/page/16/Text/58']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/4', 'PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/12', 'PZO22001 Starfinder Player Core 294-329::/page/20/Text/3']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/12` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/20/Text/3` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/4` | 0.777191 | **AIR BUBBLE **[reaction] **SPELL 1**  **AIR** **CONCENTRATE**  **Traditions** arcane, divine, primal  **Trigger** A creature within range enters an environment where  it can't breathe.  **Range **60 |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/16/Text/58` | 0.675026 | **Air Bubble** React to create air for a creature to breathe. |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/8/Text/28` | 0.675026 | **Air Bubble** React to create air for a creature to breathe. |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/46` | 0.633026 | **Air Bubble** React to create air for a creature to breathe. |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/23` | 0.581657 | SPELL ATTACKS |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0` | 0.580138 | CHAPTER 7: SPELLS |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/16/SectionHeader/57` | 0.572877 | PRIMAL 1ST-RANK SPELLS |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/19` | 0.565462 | **SPELL NAME **[one-action] **SPELL (RANK)** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/32/SectionHeader/1` | 0.559437 | **DISPELLING GLOBE **[two-actions] **SPELL 4**  **UNCOMMON** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, occult  **Area** 10-foot burst centered on one corner of your space **Durati |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/22/Text/23` | 0.558003 | **ATOMIC BLAST **[three-actions] **SPELL 9**  **CONCENTRATE** **FIRE** **MANIPULATE** **RADIATION**  **Traditions** arcane, primal  **Range **500 feet;** Area** 100-foot burst **Defense** Reflex; **Du |

### Query 105
- Text: What does **AKASHIC DOWNLOAD **[three-actions] **SPELL 1** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/12']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/12', 'PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/21', 'PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/23']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/12', 'PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/4', 'PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/21']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/4` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/21` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/12` | 0.731708 | **AKASHIC DOWNLOAD **[three-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE**  **Traditions** occult  **Requirements** You have a comm unit or computer, used as  a locus.  **Duration** 1 day  You e |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/21` | 0.617365 | **AKASHIC REVIVAL** **SPELL 8**  **CONCENTRATE** **MANIPULATE**  **Traditions** occult **Cast** 10 minutes  **Range** touch; **Targets** 1 willing creature  **Duration** 1 day  You dispatch perfect do |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/23` | 0.609263 | SPELL ATTACKS |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/19` | 0.538019 | **SPELL NAME **[one-action] **SPELL (RANK)** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/13/SectionHeader/58` | 0.526276 | OCCULT 1ST-RANK SPELLS |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/17/SectionHeader/49` | 0.524283 | PRIMAL 3RD-RANK SPELLS |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/14/SectionHeader/62` | 0.522589 | OCCULT 3RD-RANK SPELLS |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/27/Text/73` | 0.520022 | **PLAYING THE ** **GAME** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/91` | 0.520022 | **PLAYING THE ** **GAME** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/70` | 0.520022 | **PLAYING THE ** **GAME** |

### Query 106
- Text: What does **AKASHIC REVIVAL** **SPELL 8** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/21']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/21', 'PZO22001 Starfinder Player Core 294-329::/page/16/SectionHeader/17', 'PZO22001 Starfinder Player Core 294-329::/page/11/SectionHeader/2']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/21', 'PZO22001 Starfinder Player Core 294-329::/page/20/Text/33', 'PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/12']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/20/Text/33` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/12` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/21` | 0.714738 | **AKASHIC REVIVAL** **SPELL 8**  **CONCENTRATE** **MANIPULATE**  **Traditions** occult **Cast** 10 minutes  **Range** touch; **Targets** 1 willing creature  **Duration** 1 day  You dispatch perfect do |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/16/SectionHeader/17` | 0.675474 | OCCULT 8TH-RANK SPELLS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/11/SectionHeader/2` | 0.649642 | ARCANE 8TH-RANK SPELLS |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/18/SectionHeader/48` | 0.589660 | PRIMAL 8TH-RANK SPELLS |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/13/SectionHeader/21` | 0.586348 | DIVINE 8TH-RANK SPELLS |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/12` | 0.550819 | **AKASHIC DOWNLOAD **[three-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE**  **Traditions** occult  **Requirements** You have a comm unit or computer, used as  a locus.  **Duration** 1 day  You e |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/32/SectionHeader/18` | 0.550721 | **DIVINE INSPIRATION **[two-actions] **SPELL 8**  **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** divine  **Range **touch;** Targets** 1 willing creature  You infuse a target with spiritual |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0` | 0.542177 | CHAPTER 7: SPELLS |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/16/SectionHeader/24` | 0.527707 | OCCULT 9TH-RANK SPELLS |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/16/Text/18` | 0.524053 | **Akashic** **Revival** Create a record of your body in case you die. **Disappearance** Make a creature invisible, silent, and  undetectable by special senses. |

### Query 107
- Text: What does **ALARM** **SPELL 1** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/20/Text/33']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/20/Text/33', 'PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0', 'PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/23']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/20/Text/33', 'PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/21', 'PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/41']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/21` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/41` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/20/Text/33` | 0.696332 | **ALARM** **SPELL 1**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, occult, primal  **Cast** 10 minutes  **Range **touch; **Area** 20-foot burst  **Duration** 8 hours  You ward an ar |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0` | 0.659550 | CHAPTER 7: SPELLS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/23` | 0.643204 | SPELL ATTACKS |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/26` | 0.596449 | **Spells** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/62` | 0.596449 | **Spells** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/35` | 0.596449 | **Spells** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/28` | 0.596449 | **Spells** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/63` | 0.596449 | **Spells** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/23/Text/45` | 0.596449 | **Spells** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/61` | 0.596449 | **Spells** |

### Query 108
- Text: What does **ANALYZE TARGET **[two-actions] **CANTRIP 1** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/41']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/41', 'PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/28', 'PZO22001 Starfinder Player Core 294-329::/page/30/Text/2']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/41', 'PZO22001 Starfinder Player Core 294-329::/page/20/Text/33', 'PZO22001 Starfinder Player Core 294-329::/page/21/SectionHeader/4']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/20/Text/33` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/21/SectionHeader/4` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/41` | 0.738168 | **ANALYZE TARGET **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **DETECTION** **MANIPULATE**  **Traditions** arcane, divine, occult, primal **Range **30 feet; **Targets** 1 creature  **Dur |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/28` | 0.646691 | **ADHERE **[one-action] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult, primal  **Range **touch; **Targets** 1 held or unattended object or a 5-footsquare sur |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/30/Text/2` | 0.646444 | **DAZE **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **MANIPULATE** **MENTAL** **NONLETHAL**  **Traditions** arcane, divine, occult **Range **60 feet; **Targets** 1 creature **Defense** W |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/20` | 0.602494 | TARGETS |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/19` | 0.598437 | **CAUSTIC BLAST **[two-actions] **CANTRIP 1**  **ACID** **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal  **Range **30 feet; **Area** 5-foot burst  **Defense** basic Reflex  Y |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/32/SectionHeader/24` | 0.597308 | **DIVINE LANCE **[two-actions] **CANTRIP 1**  **ATTACK** **CANTRIP** **CONCENTRATE** **MANIPULATE** **SANCTIFIED** **SPIRIT**  **Traditions** divine  **Range **60 feet; **Targets** 1 creature  **Defen |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/34/SectionHeader/38` | 0.590370 | **ELECTRIC ARC **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **ELECTRICITY** **MANIPULATE**  **Traditions** arcane, primal  **Range **30 feet; **Targets** 1 or 2 creatures  **Defense** ba |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/34/SectionHeader/18` | 0.586816 | **ELDRITCH LANCE **[two-actions] **CANTRIP 1**  **ATTACK** **CANTRIP** **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** divine, occult  **Range **30 feet; **Targets** 1 creature  **Defense** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/29` | 0.567898 | **Analyze** **Target**H Gather data about a target's basic physiology. **Daze**H Cloud a creature's mind and possibly stun it. |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/42` | 0.567898 | **Analyze** **Target**H Gather data about a target's basic physiology. **Daze**H Cloud a creature's mind and possibly stun it. |

### Query 109
- Text: What does **ANIMAL FORM **[two-actions] **SPELL 2** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/21/SectionHeader/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/21/SectionHeader/4', 'PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/36', 'PZO22001 Starfinder Player Core 294-329::/page/9/SectionHeader/4']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/21/SectionHeader/4', 'PZO22001 Starfinder Player Core 294-329::/page/21/ListItem/13', 'PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/41']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/21/ListItem/13` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/41` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/21/SectionHeader/4` | 0.698918 | **ANIMAL FORM **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE** **POLYMORPH**  **Traditions** primal  **Duration** 1 minute  You call upon primal energy to transform yourself into a  Medium |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/36` | 0.657123 | **AERIAL FORM **[two-actions] **SPELL 4**  **CONCENTRATE** **MANIPULATE** **POLYMORPH**  **Traditions** arcane, primal  **Duration** 1 minute  You harness your mastery of the sky to reshape your body |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/9/SectionHeader/4` | 0.630871 | ARCANE 2ND-RANK SPELLS |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/17/SectionHeader/17` | 0.586646 | PRIMAL 2ND-RANK SPELLS |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/25/Text/11` | 0.586352 | **CALM **[two-actions] **SPELL 2**  **CONCENTRATE** **EMOTION** **INCAPACITATION** **MANIPULATE** **MENTAL**  **Traditions** divine, occult  **Range **120 feet;** Area** 10-foot burst  **Defense** Wil |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/30/Text/49` | 0.584970 | **DETECT POISON **[two-actions] **SPELL 1**  **UNCOMMON** **CONCENTRATE** **DETECTION** **MANIPULATE**  **Traditions** divine, primal  **Range **30 feet;** Targets** 1 object or creature  You detect w |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/11/SectionHeader/71` | 0.580774 | DIVINE 2ND-RANK SPELLS |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/14/SectionHeader/25` | 0.578800 | OCCULT 2ND-RANK SPELLS |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/47` | 0.571093 | **BLUR **[two-actions] **SPELL 2**  **CONCENTRATE** **ILLUSION** **MANIPULATE** **VISUAL**  **Traditions** arcane, occult  **Range **touch;** Targets** 1 creature  **Duration** 1 minute  The target's |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/33/SectionHeader/36` | 0.562535 | **EARTHBIND **[two-actions] **SPELL 3**  **CONCENTRATE** **EARTH** **MANIPULATE**  **Traditions** arcane, primal  **Range **120 feet;** Targets** 1 flying creature  **Defense** Fortitude; **Duration** |

### Query 110
- Text: What does **ANT HAUL **[two-actions] **SPELL 1** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/22/Text/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/22/Text/4', 'PZO22001 Starfinder Player Core 294-329::/page/16/Text/60', 'PZO22001 Starfinder Player Core 294-329::/page/8/Text/30']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/22/Text/4', 'PZO22001 Starfinder Player Core 294-329::/page/22/Text/11', 'PZO22001 Starfinder Player Core 294-329::/page/22/Text/3']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/22/Text/11` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/22/Text/3` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/22/Text/4` | 0.759731 | **ANT HAUL **[two-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal **Range **touch; **Targets** 1 creature  **Duration** 8 hours  You reinforce the target's musculos |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/16/Text/60` | 0.650846 | **Ant Haul** Target can carry more. |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/8/Text/30` | 0.650846 | **Ant Haul** Target can carry more. |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/23` | 0.604210 | SPELL ATTACKS |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/52` | 0.581711 | **CHARM **[two-actions] **SPELL 1**  **CONCENTRATE** **EMOTION** **INCAPACITATION** **MANIPULATE** **MENTAL** **SUBTLE**  **Traditions** arcane, occult, primal **Range **30 feet;** Targets** 1 creatur |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/19` | 0.567286 | **SPELL NAME **[one-action] **SPELL (RANK)** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/33/SectionHeader/36` | 0.562084 | **EARTHBIND **[two-actions] **SPELL 3**  **CONCENTRATE** **EARTH** **MANIPULATE**  **Traditions** arcane, primal  **Range **120 feet;** Targets** 1 flying creature  **Defense** Fortitude; **Duration** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/35/SectionHeader/32` | 0.561750 | **ENFEEBLE **[two-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, occult  **Range **30 feet;** Targets** 1 creature  **Defense** Fortitude; **Duration** varies  Yo |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0` | 0.559300 | CHAPTER 7: SPELLS |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/28/Text/11` | 0.559286 | **CONFUSION **[two-actions] **SPELL 4**  **CONCENTRATE** **EMOTION** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult **Range **30 feet;** Targets** 1 creature **Defense** Will; **Duration** 1 |

### Query 111
- Text: What does **ARCTIC RIFT **[two-actions] **SPELL 8** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/22/Text/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/22/Text/11', 'PZO22001 Starfinder Player Core 294-329::/page/16/SectionHeader/17', 'PZO22001 Starfinder Player Core 294-329::/page/11/SectionHeader/2']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/22/Text/11', 'PZO22001 Starfinder Player Core 294-329::/page/22/Text/4', 'PZO22001 Starfinder Player Core 294-329::/page/22/Text/18']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/22/Text/4` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/22/Text/18` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/22/Text/11` | 0.687337 | **ARCTIC RIFT **[two-actions] **SPELL 8**  **COLD** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal  **Area** 120-foot line  **Defense** Fortitude  A jagged crack opens in the air, deali |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/16/SectionHeader/17` | 0.670987 | OCCULT 8TH-RANK SPELLS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/11/SectionHeader/2` | 0.666849 | ARCANE 8TH-RANK SPELLS |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/33/SectionHeader/47` | 0.586921 | **EARTHQUAKE **[two-actions] **SPELL 8**  **CONCENTRATE** **EARTH** **MANIPULATE**  **Traditions** arcane, primal  **Range **500 feet;** Area** 60-foot burst  **Duration** 1 round  You shake the groun |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/18/SectionHeader/48` | 0.577243 | PRIMAL 8TH-RANK SPELLS |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/13/SectionHeader/21` | 0.573750 | DIVINE 8TH-RANK SPELLS |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/23` | 0.562059 | SPELL ATTACKS |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/32/SectionHeader/18` | 0.537546 | **DIVINE INSPIRATION **[two-actions] **SPELL 8**  **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** divine  **Range **touch;** Targets** 1 willing creature  You infuse a target with spiritual |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/33/SectionHeader/36` | 0.535966 | **EARTHBIND **[two-actions] **SPELL 3**  **CONCENTRATE** **EARTH** **MANIPULATE**  **Traditions** arcane, primal  **Range **120 feet;** Targets** 1 flying creature  **Defense** Fortitude; **Duration** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/11/SectionHeader/11` | 0.531633 | ARCANE 9TH-RANK SPELLS |

### Query 112
- Text: What does **ATOMIC BLAST **[three-actions] **SPELL 9** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/22/Text/23']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/22/Text/23', 'PZO22001 Starfinder Player Core 294-329::/page/16/SectionHeader/24', 'PZO22001 Starfinder Player Core 294-329::/page/11/SectionHeader/11']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/22/Text/23', 'PZO22001 Starfinder Player Core 294-329::/page/22/Text/33', 'PZO22001 Starfinder Player Core 294-329::/page/22/Text/22']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/22/Text/33` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/22/Text/22` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/22/Text/23` | 0.750915 | **ATOMIC BLAST **[three-actions] **SPELL 9**  **CONCENTRATE** **FIRE** **MANIPULATE** **RADIATION**  **Traditions** arcane, primal  **Range **500 feet;** Area** 100-foot burst **Defense** Reflex; **Du |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/16/SectionHeader/24` | 0.655848 | OCCULT 9TH-RANK SPELLS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/11/SectionHeader/11` | 0.643575 | ARCANE 9TH-RANK SPELLS |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/18/SectionHeader/56` | 0.575695 | PRIMAL 9TH-RANK SPELLS |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/23` | 0.571933 | SPELL ATTACKS |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/9/SectionHeader/42` | 0.556092 | ARCANE 3RD-RANK SPELLS |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/20` | 0.550577 | **BLAZING BOLT **[one-action]** TO **[three-actions] **SPELL 2**  **ATTACK** **CONCENTRATE** **FIRE** **MANIPULATE**  **Traditions** arcane, primal  **Range **60 feet; **Targets** 1 or more creatures |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/14/SectionHeader/62` | 0.550557 | OCCULT 3RD-RANK SPELLS |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/13/SectionHeader/28` | 0.548078 | DIVINE 9TH-RANK SPELLS |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/25/SectionHeader/4` | 0.546022 | **CALL COSMOS **[two-actions] **SPELL 9**  **COLD** **CONCENTRATE** **FIRE** **MANIPULATE**  **Traditions** divine, primal  **Range **500 feet;** Area** 20-foot radius, 40-foot tall cylinder **Defense |

### Query 113
- Text: What does **AUGURY** **SPELL 2** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/22/Text/33']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/14/SectionHeader/25', 'PZO22001 Starfinder Player Core 294-329::/page/22/Text/33', 'PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/23']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/22/Text/33', 'PZO22001 Starfinder Player Core 294-329::/page/22/Text/23', 'PZO22001 Starfinder Player Core 294-329::/page/22/Text/40']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/22/Text/23` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/22/Text/40` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/14/SectionHeader/25` | 0.634735 | OCCULT 2ND-RANK SPELLS |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/22/Text/33` | 0.624518 | **AUGURY** **SPELL 2**  **CONCENTRATE** **MANIPULATE** **PREDICTION**  **Traditions** divine, occult  **Cast** 10 minutes  You gain a vague glimpse of the future. During the casting  of this spell, as |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/23` | 0.608812 | SPELL ATTACKS |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0` | 0.561188 | CHAPTER 7: SPELLS |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/9/SectionHeader/4` | 0.549283 | ARCANE 2ND-RANK SPELLS |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/12` | 0.539458 | FOCUS SPELLS |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/1` | 0.532935 | SPELLS |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/17/SectionHeader/17` | 0.518632 | PRIMAL 2ND-RANK SPELLS |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/16/SectionHeader/17` | 0.516364 | OCCULT 8TH-RANK SPELLS |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/11/SectionHeader/71` | 0.515503 | DIVINE 2ND-RANK SPELLS |

### Query 114
- Text: What does **AVATAR **[two-actions] **SPELL 10** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/22/Text/40']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/11/SectionHeader/20', 'PZO22001 Starfinder Player Core 294-329::/page/16/SectionHeader/29', 'PZO22001 Starfinder Player Core 294-329::/page/22/Text/40']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/22/Text/40', 'PZO22001 Starfinder Player Core 294-329::/page/22/Text/33', 'PZO22001 Starfinder Player Core 294-329::/page/22/ListItem/48']
- Expanded expected found: `True`
- Expanded expected rank: `3`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/22/Text/33` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/22/ListItem/48` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/11/SectionHeader/20` | 0.656907 | ARCANE 10TH-RANK SPELLS |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/16/SectionHeader/29` | 0.648125 | OCCULT 10TH-RANK SPELLS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/22/Text/40` | 0.646873 | **AVATAR **[two-actions] **SPELL 10**  **CONCENTRATE** **MANIPULATE** **POLYMORPH**  **Traditions** divine **Duration** 1 minute  You transform into an avatar of your deity, assuming a Huge  battle fo |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/23` | 0.591783 | SPELL ATTACKS |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/13/SectionHeader/33` | 0.581221 | DIVINE 10TH-RANK SPELLS |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/29` | 0.579457 | **CONTROL MACHINE **[two-actions] **SPELL 5**  **UNCOMMON** **CONCENTRATE** **INCAPACITATION** **MANIPULATE**  **Traditions** arcane, occult  **Range **30 feet;** Targets** 1 creature or hazard with t |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/18/SectionHeader/64` | 0.568215 | PRIMAL 10TH-RANK SPELLS |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/31/SectionHeader/12` | 0.567341 | **DISAPPEARANCE **[two-actions] **SPELL 8**  **ILLUSION** **MANIPULATE** **SUBTLE**  **Traditions** arcane, occult  **Range **touch; **Targets** 1 creature  **Duration** 10 minutes  You shroud a creat |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/30/Text/32` | 0.564753 | **DESICCATE **[two-actions] **SPELL 8**  **CONCENTRATE** **MANIPULATE** **VOID**  **Traditions** arcane, primal  **Range **500 feet;** Targets** any number of living creatures  **Defense** basic Forti |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/31/SectionHeader/47` | 0.557866 | **DISPEL MAGIC **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, occult, primal  **Range **120 feet;** Targets** 1 spell effect or unattended magic  item  You |

### Query 115
- Text: What does **BANE **[two-actions] **SPELL 1** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/23/SectionHeader/20']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/23/SectionHeader/20', 'PZO22001 Starfinder Player Core 294-329::/page/7/Text/19', 'PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/23']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/23/SectionHeader/20', 'PZO22001 Starfinder Player Core 294-329::/page/23/ListItem/19', 'PZO22001 Starfinder Player Core 294-329::/page/23/SectionHeader/26']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/23/ListItem/19` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/23/SectionHeader/26` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/23/SectionHeader/20` | 0.687597 | **BANE **[two-actions] **SPELL 1**  **AURA** **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** divine, occult **Area** 10-foot emanation  **Defense** Will; **Duration** 1 minute  You fill the |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/19` | 0.680727 | **SPELL NAME **[one-action] **SPELL (RANK)** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/23` | 0.650888 | SPELL ATTACKS |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/29` | 0.597307 | **BLESS **[two-actions] **SPELL 1**  **AURA** **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** divine, occult  **Area** 15-foot emanation  **Duration** 1 minute  Blessings from beyond help yo |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/35/SectionHeader/32` | 0.582425 | **ENFEEBLE **[two-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, occult  **Range **30 feet;** Targets** 1 creature  **Defense** Fortitude; **Duration** varies  Yo |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/23/SectionHeader/26` | 0.577868 | **BANISHMENT **[two-actions] **SPELL 5**  **CONCENTRATE** **INCAPACITATION** **MANIPULATE**  **Traditions** arcane, divine, occult, primal  **Range **30 feet; **Targets** 1 creature that isn't on its |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0` | 0.576063 | CHAPTER 7: SPELLS |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/8/Text/27` | 0.574719 | ARCANE 1ST-RANK SPELLS |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/36` | 0.571005 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/59` | 0.571005 | **SPELLS** |

### Query 116
- Text: What does **BANISHMENT **[two-actions] **SPELL 5** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/23/SectionHeader/26']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/23/SectionHeader/26', 'PZO22001 Starfinder Player Core 294-329::/page/18/SectionHeader/7', 'PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/29']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/23/SectionHeader/26', 'PZO22001 Starfinder Player Core 294-329::/page/23/SectionHeader/20', 'PZO22001 Starfinder Player Core 294-329::/page/23/Text/38']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/23/SectionHeader/20` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/23/Text/38` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/23/SectionHeader/26` | 0.738083 | **BANISHMENT **[two-actions] **SPELL 5**  **CONCENTRATE** **INCAPACITATION** **MANIPULATE**  **Traditions** arcane, divine, occult, primal  **Range **30 feet; **Targets** 1 creature that isn't on its |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/18/SectionHeader/7` | 0.619117 | PRIMAL 5TH-RANK SPELLS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/29` | 0.616166 | **CONTROL MACHINE **[two-actions] **SPELL 5**  **UNCOMMON** **CONCENTRATE** **INCAPACITATION** **MANIPULATE**  **Traditions** arcane, occult  **Range **30 feet;** Targets** 1 creature or hazard with t |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/18/Text/8` | 0.581046 | **Banishment**H Send a creature back to its home plane. |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/15/SectionHeader/40` | 0.573724 | OCCULT 5TH-RANK SPELLS |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/10/Text/16` | 0.569046 | **Banishment**H Send a creature back to its home plane. |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/12/Text/55` | 0.569046 | **Banishment**H Send a creature back to its home plane. |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/41` | 0.569046 | **Banishment**H Send a creature back to its home plane. |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/10/SectionHeader/15` | 0.568222 | ARCANE 5TH-RANK SPELLS |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/23` | 0.566732 | SPELL ATTACKS |

### Query 117
- Text: What does **BATTLE SONATA **[two-actions] **SPELL 4** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/1', 'PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/23', 'PZO22001 Starfinder Player Core 294-329::/page/15/SectionHeader/17']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/1', 'PZO22001 Starfinder Player Core 294-329::/page/24/Text/8', 'PZO22001 Starfinder Player Core 294-329::/page/23/Text/50']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/24/Text/8` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/23/Text/50` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/1` | 0.704106 | **BATTLE SONATA **[two-actions] **SPELL 4**  **CONCENTRATE** **MANIPULATE** **SONIC**  **Traditions** divine, occult  **Area** 15-foot cone  **Defense** Will  This spell was composed by pahtra battle |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/23` | 0.637205 | SPELL ATTACKS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/15/SectionHeader/17` | 0.627697 | OCCULT 4TH-RANK SPELLS |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/9/SectionHeader/71` | 0.567794 | ARCANE 4TH-RANK SPELLS |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/28/Text/11` | 0.564791 | **CONFUSION **[two-actions] **SPELL 4**  **CONCENTRATE** **EMOTION** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult **Range **30 feet;** Targets** 1 creature **Defense** Will; **Duration** 1 |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/32/SectionHeader/1` | 0.550688 | **DISPELLING GLOBE **[two-actions] **SPELL 4**  **UNCOMMON** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, occult  **Area** 10-foot burst centered on one corner of your space **Durati |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/17/SectionHeader/71` | 0.547679 | PRIMAL 4TH-RANK SPELLS |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/54` | 0.543516 | **CLEAR MIND **[two-actions] **SPELL 2**  **CONCENTRATE** **HEALING** **MANIPULATE** **MENTAL**  **Traditions** divine, occult, primal  **Range **touch; **Targets** 1 willing creature  You drive menta |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/20` | 0.542807 | **BLAZING BOLT **[one-action]** TO **[three-actions] **SPELL 2**  **ATTACK** **CONCENTRATE** **FIRE** **MANIPULATE**  **Traditions** arcane, primal  **Range **60 feet; **Targets** 1 or more creatures |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/12/SectionHeader/40` | 0.542749 | DIVINE 4TH-RANK SPELLS |

### Query 118
- Text: What does **BIND UNDEAD **[two-actions] **SPELL 3** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/13', 'PZO22001 Starfinder Player Core 294-329::/page/33/SectionHeader/36', 'PZO22001 Starfinder Player Core 294-329::/page/14/Text/63']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/13', 'PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/20', 'PZO22001 Starfinder Player Core 294-329::/page/24/Text/12']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/20` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/24/Text/12` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/13` | 0.705847 | **BIND UNDEAD **[two-actions] **SPELL 3**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, occult  **Range **30 feet; **Targets** 1 mindless undead creature with a  level no greater tha |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/33/SectionHeader/36` | 0.640424 | **EARTHBIND **[two-actions] **SPELL 3**  **CONCENTRATE** **EARTH** **MANIPULATE**  **Traditions** arcane, primal  **Range **120 feet;** Targets** 1 flying creature  **Defense** Fortitude; **Duration** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/14/Text/63` | 0.640419 | **Bind Undead** Take control of a mindless undead. |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/12/Text/23` | 0.598419 | **Bind Undead** Take control of a mindless undead. |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/43` | 0.598419 | **Bind Undead** Take control of a mindless undead. |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/36` | 0.584953 | **BLINDNESS **[two-actions] **SPELL 3**  **CONCENTRATE** **INCAPACITATION** **MANIPULATE**  **Traditions** arcane, divine, occult, primal  **Range **30 feet;** Targets** 1 creature  **Defense** Fortit |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/23` | 0.579867 | SPELL ATTACKS |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/14/SectionHeader/62` | 0.577290 | OCCULT 3RD-RANK SPELLS |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/8/Text/63` | 0.546565 | **Summon Undead**H Conjure an undead to fight on your behalf. **Supercharge** **Weapon**H Increase the damage done by the next  attack of a weapon. |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/14/Text/24` | 0.540576 | **Summon Undead**H Conjure an undead to fight on your behalf. **Sure Strike** Your next attack is especially accurate. |

### Query 119
- Text: What does **BLAZING BOLT **[one-action]** TO **[three-actions] **SPELL 2** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/20']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/20', 'PZO22001 Starfinder Player Core 294-329::/page/9/Text/6', 'PZO22001 Starfinder Player Core 294-329::/page/17/Text/20']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/20', 'PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/29', 'PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/13']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/29` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/13` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/20` | 0.742657 | **BLAZING BOLT **[one-action]** TO **[three-actions] **SPELL 2**  **ATTACK** **CONCENTRATE** **FIRE** **MANIPULATE**  **Traditions** arcane, primal  **Range **60 feet; **Targets** 1 or more creatures |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/6` | 0.659580 | **Blazing Bolt**H Fire one to three flaming bolts at different foes. |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/20` | 0.659580 | **Blazing Bolt**H Fire one to three flaming bolts at different foes. |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/23` | 0.583382 | SPELL ATTACKS |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/22/Text/23` | 0.579465 | **ATOMIC BLAST **[three-actions] **SPELL 9**  **CONCENTRATE** **FIRE** **MANIPULATE** **RADIATION**  **Traditions** arcane, primal  **Range **500 feet;** Area** 100-foot burst **Defense** Reflex; **Du |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/29` | 0.562095 | **BLESS **[two-actions] **SPELL 1**  **AURA** **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** divine, occult  **Area** 15-foot emanation  **Duration** 1 minute  Blessings from beyond help yo |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/5` | 0.560326 | SPELL SLOTS |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/28/Text/11` | 0.559256 | **CONFUSION **[two-actions] **SPELL 4**  **CONCENTRATE** **EMOTION** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult **Range **30 feet;** Targets** 1 creature **Defense** Will; **Duration** 1 |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/33/SectionHeader/36` | 0.558423 | **EARTHBIND **[two-actions] **SPELL 3**  **CONCENTRATE** **EARTH** **MANIPULATE**  **Traditions** arcane, primal  **Range **120 feet;** Targets** 1 flying creature  **Defense** Fortitude; **Duration** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/36` | 0.556948 | **BLINDNESS **[two-actions] **SPELL 3**  **CONCENTRATE** **INCAPACITATION** **MANIPULATE**  **Traditions** arcane, divine, occult, primal  **Range **30 feet;** Targets** 1 creature  **Defense** Fortit |

### Query 120
- Text: What does **BLESS **[two-actions] **SPELL 1** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/29']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/29', 'PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0', 'PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/1']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/29', 'PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/36', 'PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/20']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/36` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/20` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/29` | 0.737202 | **BLESS **[two-actions] **SPELL 1**  **AURA** **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** divine, occult  **Area** 15-foot emanation  **Duration** 1 minute  Blessings from beyond help yo |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0` | 0.665029 | CHAPTER 7: SPELLS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/1` | 0.659367 | SPELLS |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/61` | 0.611170 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/86` | 0.611170 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/59` | 0.611170 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/26` | 0.611170 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/80` | 0.611170 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/86` | 0.611170 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/74` | 0.611170 | **SPELLS** |

### Query 121
- Text: What does **BLINDNESS **[two-actions] **SPELL 3** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/36']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/36', 'PZO22001 Starfinder Player Core 294-329::/page/29/SectionHeader/51', 'PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/6']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/36', 'PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/47', 'PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/29']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/47` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/29` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/36` | 0.683193 | **BLINDNESS **[two-actions] **SPELL 3**  **CONCENTRATE** **INCAPACITATION** **MANIPULATE**  **Traditions** arcane, divine, occult, primal  **Range **30 feet;** Targets** 1 creature  **Defense** Fortit |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/29/SectionHeader/51` | 0.612182 | **DARKVISION **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, occult, primal  **Duration** 1 hour  You grant yourself supernatural sight in areas of darkness |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/6` | 0.608009 | **CHILLING DARKNESS **[two-actions] **SPELL 3**  **ATTACK** **COLD** **CONCENTRATE** **DARKNESS** **MANIPULATE** **UNHOLY**  **Traditions** divine  **Range **120 feet;** Targets** 1 creature  **Defens |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/30/Text/8` | 0.564116 | **DEAFNESS **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, occult, primal **Range **30 feet;** Targets** 1 creature  **Defense** Fortitude  The target loses |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/34/SectionHeader/46` | 0.562706 | **ELECTROTETHER **[two-actions] **SPELL 3**  **ATTACK** **CONCENTRATE** **ELECTRICITY** **MANIPULATE**  **Traditions** arcane, divine, occult, primal **Range **30 feet; **Targets** up to two creatures |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/23` | 0.561698 | SPELL ATTACKS |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/9/SectionHeader/42` | 0.559665 | ARCANE 3RD-RANK SPELLS |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/28/Text/11` | 0.557258 | **CONFUSION **[two-actions] **SPELL 4**  **CONCENTRATE** **EMOTION** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult **Range **30 feet;** Targets** 1 creature **Defense** Will; **Duration** 1 |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/33/SectionHeader/36` | 0.556742 | **EARTHBIND **[two-actions] **SPELL 3**  **CONCENTRATE** **EARTH** **MANIPULATE**  **Traditions** arcane, primal  **Range **120 feet;** Targets** 1 flying creature  **Defense** Fortitude; **Duration** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/13` | 0.554571 | **BIND UNDEAD **[two-actions] **SPELL 3**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, occult  **Range **30 feet; **Targets** 1 mindless undead creature with a  level no greater tha |

### Query 122
- Text: What does **BLUR **[two-actions] **SPELL 2** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/47']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/47', 'PZO22001 Starfinder Player Core 294-329::/page/14/SectionHeader/25', 'PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/23']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/47', 'PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/36', 'PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/54']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/36` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/54` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/47` | 0.647777 | **BLUR **[two-actions] **SPELL 2**  **CONCENTRATE** **ILLUSION** **MANIPULATE** **VISUAL**  **Traditions** arcane, occult  **Range **touch;** Targets** 1 creature  **Duration** 1 minute  The target's |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/14/SectionHeader/25` | 0.641789 | OCCULT 2ND-RANK SPELLS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/23` | 0.627667 | SPELL ATTACKS |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0` | 0.577146 | CHAPTER 7: SPELLS |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/17/SectionHeader/17` | 0.575263 | PRIMAL 2ND-RANK SPELLS |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/5` | 0.570122 | SPELL SLOTS |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/28/Text/11` | 0.566992 | **CONFUSION **[two-actions] **SPELL 4**  **CONCENTRATE** **EMOTION** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult **Range **30 feet;** Targets** 1 creature **Defense** Will; **Duration** 1 |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/54` | 0.558271 | **CLEAR MIND **[two-actions] **SPELL 2**  **CONCENTRATE** **HEALING** **MANIPULATE** **MENTAL**  **Traditions** divine, occult, primal  **Range **touch; **Targets** 1 willing creature  You drive menta |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/1` | 0.556881 | SPELLS |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/19` | 0.556816 | **SPELL NAME **[one-action] **SPELL (RANK)** |

### Query 123
- Text: What does **BREATH OF LIFE **[reaction] **SPELL 5** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/54']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/54', 'PZO22001 Starfinder Player Core 294-329::/page/15/SectionHeader/40', 'PZO22001 Starfinder Player Core 294-329::/page/10/SectionHeader/15']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/54', 'PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/62', 'PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/47']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/62` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/47` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/54` | 0.713561 | **BREATH OF LIFE **[reaction] **SPELL 5**  **CONCENTRATE** **HEALING** **VITALITY**  **Traditions** divine  **Trigger** A living creature within range would die.  **Range **60 feet;** Targets** the tr |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/15/SectionHeader/40` | 0.649628 | OCCULT 5TH-RANK SPELLS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/10/SectionHeader/15` | 0.637239 | ARCANE 5TH-RANK SPELLS |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/12/Text/56` | 0.591682 | **Breath of Life**H React to revive a character at the moment of  its death. |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0` | 0.573746 | CHAPTER 7: SPELLS |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/4` | 0.571603 | **AIR BUBBLE **[reaction] **SPELL 1**  **AIR** **CONCENTRATE**  **Traditions** arcane, divine, primal  **Trigger** A creature within range enters an environment where  it can't breathe.  **Range **60 |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/18/SectionHeader/7` | 0.571482 | PRIMAL 5TH-RANK SPELLS |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/12/SectionHeader/54` | 0.559675 | DIVINE 5TH-RANK SPELLS |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/62` | 0.546423 | **BREATHE FIRE **[two-actions] **SPELL 1**  **CONCENTRATE** **FIRE** **MANIPULATE**  **Traditions** arcane, primal  **Area** 15-foot cone  **Defense** basic Reflex  A gout of flame sprays from your mo |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/46` | 0.541393 | **Air Bubble** React to create air for a creature to breathe. |

### Query 124
- Text: What does **BREATHE FIRE **[two-actions] **SPELL 1** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/62']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/4', 'PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/62', 'PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/23']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/62', 'PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/54', 'PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/70']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/54` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/70` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/4` | 0.668109 | **AIR BUBBLE **[reaction] **SPELL 1**  **AIR** **CONCENTRATE**  **Traditions** arcane, divine, primal  **Trigger** A creature within range enters an environment where  it can't breathe.  **Range **60 |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/62` | 0.661258 | **BREATHE FIRE **[two-actions] **SPELL 1**  **CONCENTRATE** **FIRE** **MANIPULATE**  **Traditions** arcane, primal  **Area** 15-foot cone  **Defense** basic Reflex  A gout of flame sprays from your mo |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/23` | 0.630981 | SPELL ATTACKS |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/54` | 0.591512 | **BREATH OF LIFE **[reaction] **SPELL 5**  **CONCENTRATE** **HEALING** **VITALITY**  **Traditions** divine  **Trigger** A living creature within range would die.  **Range **60 feet;** Targets** the tr |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/19` | 0.588413 | **SPELL NAME **[one-action] **SPELL (RANK)** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0` | 0.587587 | CHAPTER 7: SPELLS |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/20` | 0.578418 | **BLAZING BOLT **[one-action]** TO **[three-actions] **SPELL 2**  **ATTACK** **CONCENTRATE** **FIRE** **MANIPULATE**  **Traditions** arcane, primal  **Range **60 feet; **Targets** 1 or more creatures |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/8/Text/31` | 0.575700 | **Breathe Fire**H Release a small cone of flame from your mouth. **Cellular** **Stimulant**H Stimulate the target's body for a short  while at the expense of future energy. |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/36` | 0.574853 | **CELLULAR STIMULANT **[one-action] **SPELL 1**  **CONCENTRATE** **MANIPULATE** **VITALITY**  **Traditions** arcane, primal  **Range **120 feet;** Targets** 1 willing living creature that isn't  fatig |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/12` | 0.571502 | FOCUS SPELLS |

### Query 125
- Text: What does **CAIRN FORM **[one-action] **SPELL 4** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/70']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/70', 'PZO22001 Starfinder Player Core 294-329::/page/9/SectionHeader/71', 'PZO22001 Starfinder Player Core 294-329::/page/17/SectionHeader/71']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/70', 'PZO22001 Starfinder Player Core 294-329::/page/25/SectionHeader/4', 'PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/62']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/25/SectionHeader/4` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/62` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/70` | 0.700572 | **CAIRN FORM **[one-action] **SPELL 4**  **CONCENTRATE** **EARTH** **MANIPULATE** **MORPH**  **Traditions** arcane, primal  **Range **touch;** Targets** 1 creature  **Duration** 1 minute  Your target' |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/9/SectionHeader/71` | 0.640599 | ARCANE 4TH-RANK SPELLS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/17/SectionHeader/71` | 0.638038 | PRIMAL 4TH-RANK SPELLS |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/19` | 0.593319 | **SPELL NAME **[one-action] **SPELL (RANK)** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/15/SectionHeader/17` | 0.573628 | OCCULT 4TH-RANK SPELLS |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/36` | 0.564772 | **AERIAL FORM **[two-actions] **SPELL 4**  **CONCENTRATE** **MANIPULATE** **POLYMORPH**  **Traditions** arcane, primal  **Duration** 1 minute  You harness your mastery of the sky to reshape your body |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/12/SectionHeader/40` | 0.560398 | DIVINE 4TH-RANK SPELLS |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/36` | 0.559753 | **CELLULAR STIMULANT **[one-action] **SPELL 1**  **CONCENTRATE** **MANIPULATE** **VITALITY**  **Traditions** arcane, primal  **Range **120 feet;** Targets** 1 willing living creature that isn't  fatig |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/28/Text/11` | 0.558550 | **CONFUSION **[two-actions] **SPELL 4**  **CONCENTRATE** **EMOTION** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult **Range **30 feet;** Targets** 1 creature **Defense** Will; **Duration** 1 |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/52` | 0.554473 | **CHARM **[two-actions] **SPELL 1**  **CONCENTRATE** **EMOTION** **INCAPACITATION** **MANIPULATE** **MENTAL** **SUBTLE**  **Traditions** arcane, occult, primal **Range **30 feet;** Targets** 1 creatur |

### Query 126
- Text: What does **CALL COSMOS **[two-actions] **SPELL 9** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/25/SectionHeader/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/25/SectionHeader/4', 'PZO22001 Starfinder Player Core 294-329::/page/16/SectionHeader/24', 'PZO22001 Starfinder Player Core 294-329::/page/13/SectionHeader/28']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/25/SectionHeader/4', 'PZO22001 Starfinder Player Core 294-329::/page/25/Text/11', 'PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/70']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/25/Text/11` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/70` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/25/SectionHeader/4` | 0.717823 | **CALL COSMOS **[two-actions] **SPELL 9**  **COLD** **CONCENTRATE** **FIRE** **MANIPULATE**  **Traditions** divine, primal  **Range **500 feet;** Area** 20-foot radius, 40-foot tall cylinder **Defense |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/16/SectionHeader/24` | 0.672257 | OCCULT 9TH-RANK SPELLS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/13/SectionHeader/28` | 0.633766 | DIVINE 9TH-RANK SPELLS |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/18/SectionHeader/56` | 0.589609 | PRIMAL 9TH-RANK SPELLS |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/11/SectionHeader/11` | 0.588810 | ARCANE 9TH-RANK SPELLS |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/29` | 0.577811 | **Call** **Cosmos**H Call down a column of cosmic matter to burn  and freeze. |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0` | 0.574735 | CHAPTER 7: SPELLS |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/18/Text/58` | 0.565811 | **Call** **Cosmos**H Call down a column of cosmic matter to burn  and freeze. |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/23` | 0.563811 | SPELL ATTACKS |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/12` | 0.554484 | FOCUS SPELLS |

### Query 127
- Text: What does **CALM **[two-actions] **SPELL 2** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/25/Text/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/25/Text/11', 'PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/54', 'PZO22001 Starfinder Player Core 294-329::/page/14/Text/28']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/25/Text/11', 'PZO22001 Starfinder Player Core 294-329::/page/25/SectionHeader/4', 'PZO22001 Starfinder Player Core 294-329::/page/25/SectionHeader/21']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/25/SectionHeader/4` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/25/SectionHeader/21` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/25/Text/11` | 0.717641 | **CALM **[two-actions] **SPELL 2**  **CONCENTRATE** **EMOTION** **INCAPACITATION** **MANIPULATE** **MENTAL**  **Traditions** divine, occult  **Range **120 feet;** Area** 10-foot burst  **Defense** Wil |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/54` | 0.657747 | **CLEAR MIND **[two-actions] **SPELL 2**  **CONCENTRATE** **HEALING** **MANIPULATE** **MENTAL**  **Traditions** divine, occult, primal  **Range **touch; **Targets** 1 willing creature  You drive menta |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/14/Text/28` | 0.646984 | **Calm** Suppress strong emotions and hostility. |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/52` | 0.602132 | **CHARM **[two-actions] **SPELL 1**  **CONCENTRATE** **EMOTION** **INCAPACITATION** **MANIPULATE** **MENTAL** **SUBTLE**  **Traditions** arcane, occult, primal **Range **30 feet;** Targets** 1 creatur |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/14/SectionHeader/25` | 0.588741 | OCCULT 2ND-RANK SPELLS |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/28/Text/11` | 0.587060 | **CONFUSION **[two-actions] **SPELL 4**  **CONCENTRATE** **EMOTION** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult **Range **30 feet;** Targets** 1 creature **Defense** Will; **Duration** 1 |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0` | 0.582778 | CHAPTER 7: SPELLS |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/31/SectionHeader/47` | 0.574429 | **DISPEL MAGIC **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, occult, primal  **Range **120 feet;** Targets** 1 spell effect or unattended magic  item  You |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/39` | 0.567038 | **CLEANSE AFFLICTION **[two-actions] **SPELL 2**  **CONCENTRATE** **HEALING** **MANIPULATE**  **Traditions** divine, occult, primal  **Range **touch; **Targets** 1 willing creature  Gentle restorative |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/17/SectionHeader/17` | 0.564441 | PRIMAL 2ND-RANK SPELLS |

### Query 128
- Text: What does **CARCINIZATION **[two-actions] **SPELL 5** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/25/SectionHeader/21']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/25/SectionHeader/21', 'PZO22001 Starfinder Player Core 294-329::/page/10/SectionHeader/15', 'PZO22001 Starfinder Player Core 294-329::/page/15/SectionHeader/40']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/25/SectionHeader/21', 'PZO22001 Starfinder Player Core 294-329::/page/25/Text/11', 'PZO22001 Starfinder Player Core 294-329::/page/26/Text/4']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/25/Text/11` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/26/Text/4` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/25/SectionHeader/21` | 0.678038 | **CARCINIZATION **[two-actions] **SPELL 5**  **INCAPACITATION** **MANIPULATE** **POLYMORPH**  **Traditions** primal  **Range **30 feet;** Targets** 1 creature  **Defense** Fortitude; **Duration** 1 mi |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/10/SectionHeader/15` | 0.620017 | ARCANE 5TH-RANK SPELLS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/15/SectionHeader/40` | 0.609313 | OCCULT 5TH-RANK SPELLS |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/23/SectionHeader/26` | 0.555668 | **BANISHMENT **[two-actions] **SPELL 5**  **CONCENTRATE** **INCAPACITATION** **MANIPULATE**  **Traditions** arcane, divine, occult, primal  **Range **30 feet; **Targets** 1 creature that isn't on its |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/18/SectionHeader/7` | 0.553963 | PRIMAL 5TH-RANK SPELLS |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/12/SectionHeader/54` | 0.552452 | DIVINE 5TH-RANK SPELLS |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/29` | 0.549971 | **CONTROL MACHINE **[two-actions] **SPELL 5**  **UNCOMMON** **CONCENTRATE** **INCAPACITATION** **MANIPULATE**  **Traditions** arcane, occult  **Range **30 feet;** Targets** 1 creature or hazard with t |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/22/Text/23` | 0.544200 | **ATOMIC BLAST **[three-actions] **SPELL 9**  **CONCENTRATE** **FIRE** **MANIPULATE** **RADIATION**  **Traditions** arcane, primal  **Range **500 feet;** Area** 100-foot burst **Defense** Reflex; **Du |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/39` | 0.524349 | **CLEANSE AFFLICTION **[two-actions] **SPELL 2**  **CONCENTRATE** **HEALING** **MANIPULATE**  **Traditions** divine, occult, primal  **Range **touch; **Targets** 1 willing creature  Gentle restorative |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/18/Text/9` | 0.517558 | **Carcinization** Transform a target into a crab. |

### Query 129
- Text: What does **CATACLYSM **[two-actions] **SPELL 10** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/5', 'PZO22001 Starfinder Player Core 294-329::/page/16/SectionHeader/29', 'PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/29']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/5', 'PZO22001 Starfinder Player Core 294-329::/page/26/Text/4', 'PZO22001 Starfinder Player Core 294-329::/page/26/ListItem/17']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/26/Text/4` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/26/ListItem/17` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/5` | 0.687211 | **CATACLYSM **[two-actions] **SPELL 10**  **ACID** **AIR** **COLD** **CONCENTRATE** **EARTH** **ELECTRICITY** **FIRE** **MANIPULATE** **WATER**  **Traditions** arcane, primal  **Range **1,000 feet;** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/16/SectionHeader/29` | 0.649490 | OCCULT 10TH-RANK SPELLS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/29` | 0.630418 | **CONTROL MACHINE **[two-actions] **SPELL 5**  **UNCOMMON** **CONCENTRATE** **INCAPACITATION** **MANIPULATE**  **Traditions** arcane, occult  **Range **30 feet;** Targets** 1 creature or hazard with t |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/22/Text/23` | 0.572563 | **ATOMIC BLAST **[three-actions] **SPELL 9**  **CONCENTRATE** **FIRE** **MANIPULATE** **RADIATION**  **Traditions** arcane, primal  **Range **500 feet;** Area** 100-foot burst **Defense** Reflex; **Du |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/32/SectionHeader/55` | 0.566588 | **DOMINATE **[two-actions] **SPELL 6**  **UNCOMMON** **CONCENTRATE** **INCAPACITATION** **MANIPULATE** **MENTAL**  **Traditions** arcane, divine, occult  **Range **30 feet;** Targets** 1 creature  **D |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/23/SectionHeader/26` | 0.563784 | **BANISHMENT **[two-actions] **SPELL 5**  **CONCENTRATE** **INCAPACITATION** **MANIPULATE**  **Traditions** arcane, divine, occult, primal  **Range **30 feet; **Targets** 1 creature that isn't on its |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/25/Text/11` | 0.563586 | **CALM **[two-actions] **SPELL 2**  **CONCENTRATE** **EMOTION** **INCAPACITATION** **MANIPULATE** **MENTAL**  **Traditions** divine, occult  **Range **120 feet;** Area** 10-foot burst  **Defense** Wil |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/28/Text/11` | 0.556090 | **CONFUSION **[two-actions] **SPELL 4**  **CONCENTRATE** **EMOTION** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult **Range **30 feet;** Targets** 1 creature **Defense** Will; **Duration** 1 |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/11/SectionHeader/20` | 0.555564 | ARCANE 10TH-RANK SPELLS |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/33/SectionHeader/47` | 0.554985 | **EARTHQUAKE **[two-actions] **SPELL 8**  **CONCENTRATE** **EARTH** **MANIPULATE**  **Traditions** arcane, primal  **Range **500 feet;** Area** 60-foot burst  **Duration** 1 round  You shake the groun |

### Query 130
- Text: What does **CAUSTIC BLAST **[two-actions] **CANTRIP 1** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/19']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/19', 'PZO22001 Starfinder Player Core 294-329::/page/32/SectionHeader/24', 'PZO22001 Starfinder Player Core 294-329::/page/34/SectionHeader/38']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/19', 'PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/27', 'PZO22001 Starfinder Player Core 294-329::/page/26/ListItem/18']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/27` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/26/ListItem/18` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/19` | 0.764380 | **CAUSTIC BLAST **[two-actions] **CANTRIP 1**  **ACID** **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal  **Range **30 feet; **Area** 5-foot burst  **Defense** basic Reflex  Y |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/32/SectionHeader/24` | 0.648890 | **DIVINE LANCE **[two-actions] **CANTRIP 1**  **ATTACK** **CANTRIP** **CONCENTRATE** **MANIPULATE** **SANCTIFIED** **SPIRIT**  **Traditions** divine  **Range **60 feet; **Targets** 1 creature  **Defen |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/34/SectionHeader/38` | 0.632188 | **ELECTRIC ARC **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **ELECTRICITY** **MANIPULATE**  **Traditions** arcane, primal  **Range **30 feet; **Targets** 1 or 2 creatures  **Defense** ba |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/30/Text/2` | 0.585864 | **DAZE **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **MANIPULATE** **MENTAL** **NONLETHAL**  **Traditions** arcane, divine, occult **Range **60 feet; **Targets** 1 creature **Defense** W |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/41` | 0.584325 | **ANALYZE TARGET **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **DETECTION** **MANIPULATE**  **Traditions** arcane, divine, occult, primal **Range **30 feet; **Targets** 1 creature  **Dur |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/34/SectionHeader/18` | 0.580083 | **ELDRITCH LANCE **[two-actions] **CANTRIP 1**  **ATTACK** **CANTRIP** **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** divine, occult  **Range **30 feet; **Targets** 1 creature  **Defense** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/27` | 0.573001 | **CAUSTIC CONVERSION **[two-actions] **SPELL 2**  **ACID** **ATTACK** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal  **Range **120 feet;** Targets** 1 creature  **Defense** AC  You lau |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/8/Text/8` | 0.567873 | **Analyze** **Target**H Gather data about a target's basic physiology. **Caustic Blast**H Fling a glob of acid that splashes a small area. |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/16/Text/38` | 0.567873 | **Analyze** **Target**H Gather data about a target's basic physiology. **Caustic Blast**H Fling a glob of acid that splashes a small area. |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/22/Text/23` | 0.563828 | **ATOMIC BLAST **[three-actions] **SPELL 9**  **CONCENTRATE** **FIRE** **MANIPULATE** **RADIATION**  **Traditions** arcane, primal  **Range **500 feet;** Area** 100-foot burst **Defense** Reflex; **Du |

### Query 131
- Text: What does **CAUSTIC CONVERSION **[two-actions] **SPELL 2** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/27']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/27', 'PZO22001 Starfinder Player Core 294-329::/page/14/SectionHeader/25', 'PZO22001 Starfinder Player Core 294-329::/page/29/SectionHeader/35']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/27', 'PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/36', 'PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/19']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/36` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/19` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/27` | 0.668197 | **CAUSTIC CONVERSION **[two-actions] **SPELL 2**  **ACID** **ATTACK** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal  **Range **120 feet;** Targets** 1 creature  **Defense** AC  You lau |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/14/SectionHeader/25` | 0.654356 | OCCULT 2ND-RANK SPELLS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/29/SectionHeader/35` | 0.628454 | **CURSED METAMORPHOSIS **[two-actions] **SPELL 6**  **CONCENTRATE** **CURSE** **INCAPACITATION** **MANIPULATE** **POLYMORPH**  **Traditions** arcane, occult, primal **Range **30 feet;** Targets** 1 cr |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/17/SectionHeader/17` | 0.583586 | PRIMAL 2ND-RANK SPELLS |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0` | 0.579774 | CHAPTER 7: SPELLS |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/28/Text/11` | 0.578175 | **CONFUSION **[two-actions] **SPELL 4**  **CONCENTRATE** **EMOTION** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult **Range **30 feet;** Targets** 1 creature **Defense** Will; **Duration** 1 |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/47` | 0.571924 | **CLEANSE CUISINE **[two-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE**  **Traditions** divine, primal  **Range **10 feet;** Area** 1 cubic foot  You transform all food and beverages in the area |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/23` | 0.570147 | SPELL ATTACKS |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/9/SectionHeader/4` | 0.564503 | ARCANE 2ND-RANK SPELLS |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/25/Text/11` | 0.563584 | **CALM **[two-actions] **SPELL 2**  **CONCENTRATE** **EMOTION** **INCAPACITATION** **MANIPULATE** **MENTAL**  **Traditions** divine, occult  **Range **120 feet;** Area** 10-foot burst  **Defense** Wil |

### Query 132
- Text: What does **CELLULAR STIMULANT **[one-action] **SPELL 1** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/36']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/36', 'PZO22001 Starfinder Player Core 294-329::/page/16/Text/62', 'PZO22001 Starfinder Player Core 294-329::/page/7/Text/19']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/36', 'PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/44', 'PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/27']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/44` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/27` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/36` | 0.753186 | **CELLULAR STIMULANT **[one-action] **SPELL 1**  **CONCENTRATE** **MANIPULATE** **VITALITY**  **Traditions** arcane, primal  **Range **120 feet;** Targets** 1 willing living creature that isn't  fatig |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/16/Text/62` | 0.655020 | **Cellular** **Stimulant**H Stimulate the target's body for a short  while at the expense of future energy. |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/19` | 0.654799 | **SPELL NAME **[one-action] **SPELL (RANK)** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/13/SectionHeader/58` | 0.581371 | OCCULT 1ST-RANK SPELLS |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/4` | 0.575189 | **AIR BUBBLE **[reaction] **SPELL 1**  **AIR** **CONCENTRATE**  **Traditions** arcane, divine, primal  **Trigger** A creature within range enters an environment where  it can't breathe.  **Range **60 |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/13` | 0.574413 | SUSTAINING SPELLS |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/23` | 0.570228 | SPELL ATTACKS |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/16/SectionHeader/57` | 0.568380 | PRIMAL 1ST-RANK SPELLS |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/23/Text/43` | 0.563554 | **EQUIPMENT** **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/33` | 0.563554 | **EQUIPMENT** **SPELLS** |

### Query 133
- Text: What does **CHAIN LIGHTNING **[two-actions] **SPELL 6** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/44']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/44', 'PZO22001 Starfinder Player Core 294-329::/page/15/SectionHeader/60', 'PZO22001 Starfinder Player Core 294-329::/page/12/SectionHeader/67']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/44', 'PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/36', 'PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/52']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/36` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/52` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/44` | 0.740091 | **CHAIN LIGHTNING **[two-actions] **SPELL 6**  **CONCENTRATE** **ELECTRICITY** **MANIPULATE**  **Traditions** arcane, primal  **Range **500 feet;** Targets** 1 creature, plus any number of  additional |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/15/SectionHeader/60` | 0.647762 | OCCULT 6TH-RANK SPELLS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/12/SectionHeader/67` | 0.630526 | DIVINE 6TH-RANK SPELLS |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/10/SectionHeader/35` | 0.585594 | ARCANE 6TH-RANK SPELLS |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/18/SectionHeader/24` | 0.576948 | PRIMAL 6TH-RANK SPELLS |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/23` | 0.573540 | SPELL ATTACKS |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/6` | 0.569762 | **CHILLING DARKNESS **[two-actions] **SPELL 3**  **ATTACK** **COLD** **CONCENTRATE** **DARKNESS** **MANIPULATE** **UNHOLY**  **Traditions** divine  **Range **120 feet;** Targets** 1 creature  **Defens |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/32/SectionHeader/55` | 0.567227 | **DOMINATE **[two-actions] **SPELL 6**  **UNCOMMON** **CONCENTRATE** **INCAPACITATION** **MANIPULATE** **MENTAL**  **Traditions** arcane, divine, occult  **Range **30 feet;** Targets** 1 creature  **D |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/20` | 0.564227 | **BLAZING BOLT **[one-action]** TO **[three-actions] **SPELL 2**  **ATTACK** **CONCENTRATE** **FIRE** **MANIPULATE**  **Traditions** arcane, primal  **Range **60 feet; **Targets** 1 or more creatures |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/19` | 0.562471 | **SPELL NAME **[one-action] **SPELL (RANK)** |

### Query 134
- Text: What does **CHARM **[two-actions] **SPELL 1** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/52']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/52', 'PZO22001 Starfinder Player Core 294-329::/page/7/Text/19', 'PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/54']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/52', 'PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/44', 'PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/6']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/44` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/6` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/52` | 0.713890 | **CHARM **[two-actions] **SPELL 1**  **CONCENTRATE** **EMOTION** **INCAPACITATION** **MANIPULATE** **MENTAL** **SUBTLE**  **Traditions** arcane, occult, primal **Range **30 feet;** Targets** 1 creatur |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/19` | 0.663822 | **SPELL NAME **[one-action] **SPELL (RANK)** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/54` | 0.621995 | **CLEAR MIND **[two-actions] **SPELL 2**  **CONCENTRATE** **HEALING** **MANIPULATE** **MENTAL**  **Traditions** divine, occult, primal  **Range **touch; **Targets** 1 willing creature  You drive menta |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/25/Text/11` | 0.579432 | **CALM **[two-actions] **SPELL 2**  **CONCENTRATE** **EMOTION** **INCAPACITATION** **MANIPULATE** **MENTAL**  **Traditions** divine, occult  **Range **120 feet;** Area** 10-foot burst  **Defense** Wil |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/33/SectionHeader/22` | 0.577705 | **DREAM OF HOME **[two-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** divine, occult  **Range **30 feet; **Targets** 1 creature  **Defense** Will; **Duration** sustain |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/23` | 0.574909 | SPELL ATTACKS |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0` | 0.574433 | CHAPTER 7: SPELLS |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/28/Text/2` | 0.570885 | **COMMAND **[two-actions] **SPELL 1**  **AUDITORY** **CONCENTRATE** **LINGUISTIC** **MANIPULATE** **MENTAL**  **Traditions** arcane, divine, occult **Range **30 feet;** Targets** 1 creature  **Defense |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/47` | 0.563787 | **BLUR **[two-actions] **SPELL 2**  **CONCENTRATE** **ILLUSION** **MANIPULATE** **VISUAL**  **Traditions** arcane, occult  **Range **touch;** Targets** 1 creature  **Duration** 1 minute  The target's |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/33` | 0.563296 | **EQUIPMENT** **SPELLS** |

### Query 135
- Text: What does **CHILLING DARKNESS **[two-actions] **SPELL 3** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/6', 'PZO22001 Starfinder Player Core 294-329::/page/29/SectionHeader/51', 'PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/36']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/6', 'PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/17', 'PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/52']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/17` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/52` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/6` | 0.730003 | **CHILLING DARKNESS **[two-actions] **SPELL 3**  **ATTACK** **COLD** **CONCENTRATE** **DARKNESS** **MANIPULATE** **UNHOLY**  **Traditions** divine  **Range **120 feet;** Targets** 1 creature  **Defens |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/29/SectionHeader/51` | 0.629152 | **DARKVISION **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, occult, primal  **Duration** 1 hour  You grant yourself supernatural sight in areas of darkness |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/36` | 0.627407 | **BLINDNESS **[two-actions] **SPELL 3**  **CONCENTRATE** **INCAPACITATION** **MANIPULATE**  **Traditions** arcane, divine, occult, primal  **Range **30 feet;** Targets** 1 creature  **Defense** Fortit |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/12/SectionHeader/22` | 0.572763 | DIVINE 3RD-RANK SPELLS |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/14/SectionHeader/62` | 0.571244 | OCCULT 3RD-RANK SPELLS |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/23` | 0.569371 | SPELL ATTACKS |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0` | 0.568356 | CHAPTER 7: SPELLS |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/12/Text/25` | 0.563054 | **Chilling Darkness**H Ray of unholy darkness deals cold  damage, dispels light, and harms holy targets. |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/29/SectionHeader/44` | 0.559970 | **DARKNESS **[three-actions] **SPELL 2**  **CONCENTRATE** **DARKNESS** **MANIPULATE**  **Traditions** arcane, divine, occult, primal **Range **120 feet;** Area** 20-foot burst  **Duration** 1 minute |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/23/Text/43` | 0.557944 | **EQUIPMENT** **SPELLS** |

### Query 136
- Text: What does **CHRONO PUSH **[two-actions] **SPELL 5** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/17']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/17', 'PZO22001 Starfinder Player Core 294-329::/page/15/Text/42', 'PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/29']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/17', 'PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/24', 'PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/6']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/24` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/6` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/17` | 0.756896 | **CHRONO PUSH **[two-actions] **SPELL 5**  **ATTACK** **CONCENTRATE** **FORCE** **MANIPULATE**  **Traditions** occult  **Range **500 feet;** Targets** 1 creature **Defense** AC and basic Reflex  You p |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/42` | 0.642211 | **Chrono** **Push ** H Push a target away and damage creatures  nearby. |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/29` | 0.624176 | **CONTROL MACHINE **[two-actions] **SPELL 5**  **UNCOMMON** **CONCENTRATE** **INCAPACITATION** **MANIPULATE**  **Traditions** arcane, occult  **Range **30 feet;** Targets** 1 creature or hazard with t |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/15/SectionHeader/40` | 0.581145 | OCCULT 5TH-RANK SPELLS |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/10/SectionHeader/15` | 0.568511 | ARCANE 5TH-RANK SPELLS |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/18/SectionHeader/7` | 0.563598 | PRIMAL 5TH-RANK SPELLS |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/23` | 0.555006 | SPELL ATTACKS |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/23/SectionHeader/26` | 0.552381 | **BANISHMENT **[two-actions] **SPELL 5**  **CONCENTRATE** **INCAPACITATION** **MANIPULATE**  **Traditions** arcane, divine, occult, primal  **Range **30 feet; **Targets** 1 creature that isn't on its |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/12/SectionHeader/54` | 0.544668 | DIVINE 5TH-RANK SPELLS |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/28/Text/11` | 0.543159 | **CONFUSION **[two-actions] **SPELL 4**  **CONCENTRATE** **EMOTION** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult **Range **30 feet;** Targets** 1 creature **Defense** Will; **Duration** 1 |

### Query 137
- Text: What does **CLAIRAUDIENCE** **SPELL 3** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/24']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/24', 'PZO22001 Starfinder Player Core 294-329::/page/14/SectionHeader/62', 'PZO22001 Starfinder Player Core 294-329::/page/14/Text/65']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/24', 'PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/31', 'PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/17']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/31` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/17` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/24` | 0.688953 | **CLAIRAUDIENCE** **SPELL 3**  **CONCENTRATE** **MANIPULATE** **SCRYING**  **Traditions** arcane, occult  **Cast** 1 minute **Range **500 feet  **Duration** 10 minutes  You create an invisible floatin |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/14/SectionHeader/62` | 0.659142 | OCCULT 3RD-RANK SPELLS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/14/Text/65` | 0.630175 | **Clairaudience** Hear through an invisible magical sensor. |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/45` | 0.588175 | **Clairaudience** Hear through an invisible magical sensor. |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/9/SectionHeader/42` | 0.579414 | ARCANE 3RD-RANK SPELLS |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/31` | 0.574821 | **CLAIRVOYANCE** **SPELL 4**  **CONCENTRATE** **MANIPULATE** **SCRYING**  **Traditions** arcane, occult  **Cast** 1 minute  **Range **500 feet  **Duration** 10 minutes  You create an invisible floatin |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/12/SectionHeader/22` | 0.572789 | DIVINE 3RD-RANK SPELLS |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/17/SectionHeader/49` | 0.570582 | PRIMAL 3RD-RANK SPELLS |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0` | 0.566218 | CHAPTER 7: SPELLS |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/7/SectionHeader/3` | 0.551743 | IDENTIFYING SPELLS |

### Query 138
- Text: What does **CLAIRVOYANCE** **SPELL 4** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/31']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/31', 'PZO22001 Starfinder Player Core 294-329::/page/15/SectionHeader/17', 'PZO22001 Starfinder Player Core 294-329::/page/12/SectionHeader/40']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/31', 'PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/24', 'PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/39']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/24` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/39` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/31` | 0.660064 | **CLAIRVOYANCE** **SPELL 4**  **CONCENTRATE** **MANIPULATE** **SCRYING**  **Traditions** arcane, occult  **Cast** 1 minute  **Range **500 feet  **Duration** 10 minutes  You create an invisible floatin |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/15/SectionHeader/17` | 0.633076 | OCCULT 4TH-RANK SPELLS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/12/SectionHeader/40` | 0.622659 | DIVINE 4TH-RANK SPELLS |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/9/SectionHeader/71` | 0.572596 | ARCANE 4TH-RANK SPELLS |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/17/SectionHeader/71` | 0.557710 | PRIMAL 4TH-RANK SPELLS |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/7/SectionHeader/3` | 0.552371 | IDENTIFYING SPELLS |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0` | 0.550975 | CHAPTER 7: SPELLS |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/28/Text/11` | 0.549786 | **CONFUSION **[two-actions] **SPELL 4**  **CONCENTRATE** **EMOTION** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult **Range **30 feet;** Targets** 1 creature **Defense** Will; **Duration** 1 |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/1` | 0.539999 | SPELLS |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/33` | 0.535819 | **EQUIPMENT** **SPELLS** |

### Query 139
- Text: What does **CLEANSE AFFLICTION **[two-actions] **SPELL 2** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/39']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/39', 'PZO22001 Starfinder Player Core 294-329::/page/9/SectionHeader/4', 'PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/54']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/39', 'PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/47', 'PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/31']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/47` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/31` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/39` | 0.749348 | **CLEANSE AFFLICTION **[two-actions] **SPELL 2**  **CONCENTRATE** **HEALING** **MANIPULATE**  **Traditions** divine, occult, primal  **Range **touch; **Targets** 1 willing creature  Gentle restorative |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/9/SectionHeader/4` | 0.661976 | ARCANE 2ND-RANK SPELLS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/54` | 0.641543 | **CLEAR MIND **[two-actions] **SPELL 2**  **CONCENTRATE** **HEALING** **MANIPULATE** **MENTAL**  **Traditions** divine, occult, primal  **Range **touch; **Targets** 1 willing creature  You drive menta |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/47` | 0.599836 | **CLEANSE CUISINE **[two-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE**  **Traditions** divine, primal  **Range **10 feet;** Area** 1 cubic foot  You transform all food and beverages in the area |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/14/SectionHeader/25` | 0.585763 | OCCULT 2ND-RANK SPELLS |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/11/SectionHeader/71` | 0.576363 | DIVINE 2ND-RANK SPELLS |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/31/SectionHeader/47` | 0.565401 | **DISPEL MAGIC **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, occult, primal  **Range **120 feet;** Targets** 1 spell effect or unattended magic  item  You |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/17/SectionHeader/17` | 0.560670 | PRIMAL 2ND-RANK SPELLS |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0` | 0.552631 | CHAPTER 7: SPELLS |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/23` | 0.549180 | SPELL ATTACKS |

### Query 140
- Text: What does **CLEANSE CUISINE **[two-actions] **SPELL 1** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/47']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/47', 'PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/39', 'PZO22001 Starfinder Player Core 294-329::/page/16/Text/64']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/47', 'PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/54', 'PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/39']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/54` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/39` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/47` | 0.769090 | **CLEANSE CUISINE **[two-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE**  **Traditions** divine, primal  **Range **10 feet;** Area** 1 cubic foot  You transform all food and beverages in the area |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/39` | 0.678648 | **CLEANSE AFFLICTION **[two-actions] **SPELL 2**  **CONCENTRATE** **HEALING** **MANIPULATE**  **Traditions** divine, occult, primal  **Range **touch; **Targets** 1 willing creature  Gentle restorative |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/16/Text/64` | 0.633377 | **Cleanse** **Cuisine**H Make food and drink safe and delicious. |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/54` | 0.591478 | **CLEAR MIND **[two-actions] **SPELL 2**  **CONCENTRATE** **HEALING** **MANIPULATE** **MENTAL**  **Traditions** divine, occult, primal  **Range **touch; **Targets** 1 willing creature  You drive menta |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/50` | 0.572299 | **Cleanse Cuisine**H Make food and drink safe and delicious. |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/19` | 0.557521 | **SPELL NAME **[one-action] **SPELL (RANK)** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/7` | 0.554498 | PREPARED SPELLS |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/30/Text/49` | 0.553690 | **DETECT POISON **[two-actions] **SPELL 1**  **UNCOMMON** **CONCENTRATE** **DETECTION** **MANIPULATE**  **Traditions** divine, primal  **Range **30 feet;** Targets** 1 object or creature  You detect w |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/1` | 0.550978 | SPELLS |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/29/SectionHeader/9` | 0.550457 | **CREATE WATER **[two-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE** **WATER**  **Traditions** arcane, divine, primal  **Range **0 feet |

### Query 141
- Text: What does **CLEAR MIND **[two-actions] **SPELL 2** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/54']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/54', 'PZO22001 Starfinder Player Core 294-329::/page/31/SectionHeader/5', 'PZO22001 Starfinder Player Core 294-329::/page/28/Text/11']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/54', 'PZO22001 Starfinder Player Core 294-329::/page/27/Text/62', 'PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/47']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/27/Text/62` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/47` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/54` | 0.746473 | **CLEAR MIND **[two-actions] **SPELL 2**  **CONCENTRATE** **HEALING** **MANIPULATE** **MENTAL**  **Traditions** divine, occult, primal  **Range **touch; **Targets** 1 willing creature  You drive menta |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/31/SectionHeader/5` | 0.627303 | **DETECT THOUGHTS **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** divine, occult **Area** 30-foot emanation  **Defense** Will  You sense the presence of thinking |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/28/Text/11` | 0.627283 | **CONFUSION **[two-actions] **SPELL 4**  **CONCENTRATE** **EMOTION** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult **Range **30 feet;** Targets** 1 creature **Defense** Will; **Duration** 1 |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/39` | 0.584520 | **CLEANSE AFFLICTION **[two-actions] **SPELL 2**  **CONCENTRATE** **HEALING** **MANIPULATE**  **Traditions** divine, occult, primal  **Range **touch; **Targets** 1 willing creature  Gentle restorative |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/47` | 0.577765 | **CLEANSE CUISINE **[two-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE**  **Traditions** divine, primal  **Range **10 feet;** Area** 1 cubic foot  You transform all food and beverages in the area |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/32/SectionHeader/18` | 0.573014 | **DIVINE INSPIRATION **[two-actions] **SPELL 8**  **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** divine  **Range **touch;** Targets** 1 willing creature  You infuse a target with spiritual |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/31/SectionHeader/47` | 0.568344 | **DISPEL MAGIC **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, occult, primal  **Range **120 feet;** Targets** 1 spell effect or unattended magic  item  You |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/14/SectionHeader/25` | 0.568208 | OCCULT 2ND-RANK SPELLS |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/25/Text/11` | 0.567208 | **CALM **[two-actions] **SPELL 2**  **CONCENTRATE** **EMOTION** **INCAPACITATION** **MANIPULATE** **MENTAL**  **Traditions** divine, occult  **Range **120 feet;** Area** 10-foot burst  **Defense** Wil |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/30/Text/8` | 0.563546 | **DEAFNESS **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, occult, primal **Range **30 feet;** Targets** 1 creature  **Defense** Fortitude  The target loses |

### Query 142
- Text: What does **COMMAND **[two-actions] **SPELL 1** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/28/Text/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/28/Text/2', 'PZO22001 Starfinder Player Core 294-329::/page/7/Text/19', 'PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/29']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/28/Text/2', 'PZO22001 Starfinder Player Core 294-329::/page/28/Text/7', 'PZO22001 Starfinder Player Core 294-329::/page/28/Text/1']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/28/Text/7` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/28/Text/1` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/28/Text/2` | 0.711935 | **COMMAND **[two-actions] **SPELL 1**  **AUDITORY** **CONCENTRATE** **LINGUISTIC** **MANIPULATE** **MENTAL**  **Traditions** arcane, divine, occult **Range **30 feet;** Targets** 1 creature  **Defense |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/19` | 0.667414 | **SPELL NAME **[one-action] **SPELL (RANK)** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/29` | 0.653674 | **CONTROL MACHINE **[two-actions] **SPELL 5**  **UNCOMMON** **CONCENTRATE** **INCAPACITATION** **MANIPULATE**  **Traditions** arcane, occult  **Range **30 feet;** Targets** 1 creature or hazard with t |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/23` | 0.610558 | SPELL ATTACKS |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/30/Text/49` | 0.610333 | **DETECT POISON **[two-actions] **SPELL 1**  **UNCOMMON** **CONCENTRATE** **DETECTION** **MANIPULATE**  **Traditions** divine, primal  **Range **30 feet;** Targets** 1 object or creature  You detect w |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/31/SectionHeader/47` | 0.605240 | **DISPEL MAGIC **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, occult, primal  **Range **120 feet;** Targets** 1 spell effect or unattended magic  item  You |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/32/SectionHeader/55` | 0.604807 | **DOMINATE **[two-actions] **SPELL 6**  **UNCOMMON** **CONCENTRATE** **INCAPACITATION** **MANIPULATE** **MENTAL**  **Traditions** arcane, divine, occult  **Range **30 feet;** Targets** 1 creature  **D |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/36` | 0.598189 | **CELLULAR STIMULANT **[one-action] **SPELL 1**  **CONCENTRATE** **MANIPULATE** **VITALITY**  **Traditions** arcane, primal  **Range **120 feet;** Targets** 1 willing living creature that isn't  fatig |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/28/Text/11` | 0.596685 | **CONFUSION **[two-actions] **SPELL 4**  **CONCENTRATE** **EMOTION** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult **Range **30 feet;** Targets** 1 creature **Defense** Will; **Duration** 1 |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/35/SectionHeader/32` | 0.594713 | **ENFEEBLE **[two-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, occult  **Range **30 feet;** Targets** 1 creature  **Defense** Fortitude; **Duration** varies  Yo |

### Query 143
- Text: What does **CONFUSION **[two-actions] **SPELL 4** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/28/Text/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/28/Text/11', 'PZO22001 Starfinder Player Core 294-329::/page/15/SectionHeader/17', 'PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/54']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/28/Text/11', 'PZO22001 Starfinder Player Core 294-329::/page/28/Text/10', 'PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/21']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/28/Text/10` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/21` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/28/Text/11` | 0.757882 | **CONFUSION **[two-actions] **SPELL 4**  **CONCENTRATE** **EMOTION** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult **Range **30 feet;** Targets** 1 creature **Defense** Will; **Duration** 1 |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/15/SectionHeader/17` | 0.630514 | OCCULT 4TH-RANK SPELLS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/54` | 0.629458 | **CLEAR MIND **[two-actions] **SPELL 2**  **CONCENTRATE** **HEALING** **MANIPULATE** **MENTAL**  **Traditions** divine, occult, primal  **Range **touch; **Targets** 1 willing creature  You drive menta |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/30/Text/49` | 0.577593 | **DETECT POISON **[two-actions] **SPELL 1**  **UNCOMMON** **CONCENTRATE** **DETECTION** **MANIPULATE**  **Traditions** divine, primal  **Range **30 feet;** Targets** 1 object or creature  You detect w |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/12` | 0.577461 | FOCUS SPELLS |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/32/SectionHeader/1` | 0.576938 | **DISPELLING GLOBE **[two-actions] **SPELL 4**  **UNCOMMON** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, occult  **Area** 10-foot burst centered on one corner of your space **Durati |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0` | 0.575745 | CHAPTER 7: SPELLS |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/35/SectionHeader/14` | 0.570431 | **EMBED MESSAGE **[two-actions] **SPELL 2**  **CONCENTRATE** **ILLUSION** **MANIPULATE**  **Traditions** arcane, occult  **Range **touch; **Targets** 1 object or willing creature  **Duration** unlimit |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/31/SectionHeader/12` | 0.568634 | **DISAPPEARANCE **[two-actions] **SPELL 8**  **ILLUSION** **MANIPULATE** **SUBTLE**  **Traditions** arcane, occult  **Range **touch; **Targets** 1 creature  **Duration** 10 minutes  You shroud a creat |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/39` | 0.567580 | **CLEANSE AFFLICTION **[two-actions] **SPELL 2**  **CONCENTRATE** **HEALING** **MANIPULATE**  **Traditions** divine, occult, primal  **Range **touch; **Targets** 1 willing creature  Gentle restorative |

### Query 144
- Text: What does **CONTINGENCY** **SPELL 7** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/21']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0', 'PZO22001 Starfinder Player Core 294-329::/page/16/SectionHeader/5', 'PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/21']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/21', 'PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/29', 'PZO22001 Starfinder Player Core 294-329::/page/28/Text/11']
- Expanded expected found: `True`
- Expanded expected rank: `3`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/29` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/28/Text/11` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0` | 0.734025 | CHAPTER 7: SPELLS |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/16/SectionHeader/5` | 0.683367 | OCCULT 7TH-RANK SPELLS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/21` | 0.676083 | **CONTINGENCY** **SPELL 7**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane  **Cast** 10 minutes **Duration** until your next daily preparations  You prepare a spell that will trigger later. Wh |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/10/SectionHeader/57` | 0.598781 | ARCANE 7TH-RANK SPELLS |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/18/SectionHeader/34` | 0.589418 | PRIMAL 7TH-RANK SPELLS |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/13/SectionHeader/11` | 0.581568 | DIVINE 7TH-RANK SPELLS |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/7/SectionHeader/3` | 0.568832 | IDENTIFYING SPELLS |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/13` | 0.567111 | SUSTAINING SPELLS |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/28/Text/11` | 0.563082 | **CONFUSION **[two-actions] **SPELL 4**  **CONCENTRATE** **EMOTION** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult **Range **30 feet;** Targets** 1 creature **Defense** Will; **Duration** 1 |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/1` | 0.560976 | SPELLS |

### Query 145
- Text: What does **CONTROL MACHINE **[two-actions] **SPELL 5** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/29']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/29', 'PZO22001 Starfinder Player Core 294-329::/page/15/SectionHeader/40', 'PZO22001 Starfinder Player Core 294-329::/page/10/SectionHeader/15']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/29', 'PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/39', 'PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/21']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/39` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/21` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/29` | 0.740624 | **CONTROL MACHINE **[two-actions] **SPELL 5**  **UNCOMMON** **CONCENTRATE** **INCAPACITATION** **MANIPULATE**  **Traditions** arcane, occult  **Range **30 feet;** Targets** 1 creature or hazard with t |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/15/SectionHeader/40` | 0.657344 | OCCULT 5TH-RANK SPELLS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/10/SectionHeader/15` | 0.631703 | ARCANE 5TH-RANK SPELLS |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/18/SectionHeader/7` | 0.585844 | PRIMAL 5TH-RANK SPELLS |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/32/SectionHeader/55` | 0.572026 | **DOMINATE **[two-actions] **SPELL 6**  **UNCOMMON** **CONCENTRATE** **INCAPACITATION** **MANIPULATE** **MENTAL**  **Traditions** arcane, divine, occult  **Range **30 feet;** Targets** 1 creature  **D |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/12/SectionHeader/54` | 0.568713 | DIVINE 5TH-RANK SPELLS |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/19` | 0.567135 | **SPELL NAME **[one-action] **SPELL (RANK)** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/31/SectionHeader/47` | 0.565248 | **DISPEL MAGIC **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, occult, primal  **Range **120 feet;** Targets** 1 spell effect or unattended magic  item  You |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/28/Text/11` | 0.563843 | **CONFUSION **[two-actions] **SPELL 4**  **CONCENTRATE** **EMOTION** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult **Range **30 feet;** Targets** 1 creature **Defense** Will; **Duration** 1 |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/23/SectionHeader/26` | 0.563294 | **BANISHMENT **[two-actions] **SPELL 5**  **CONCENTRATE** **INCAPACITATION** **MANIPULATE**  **Traditions** arcane, divine, occult, primal  **Range **30 feet; **Targets** 1 creature that isn't on its |

### Query 146
- Text: What does **CORROSIVE HAZE **[two-actions] **SPELL 6** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/39']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/39', 'PZO22001 Starfinder Player Core 294-329::/page/15/SectionHeader/60', 'PZO22001 Starfinder Player Core 294-329::/page/10/SectionHeader/35']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/39', 'PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/47', 'PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/29']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/47` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/29` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/39` | 0.719762 | **CORROSIVE HAZE **[two-actions] **SPELL 6**  **ACID** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal  **Range **120 feet;** Area** 20-foot burst  **Defense** basic Fortitude; **Duratio |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/15/SectionHeader/60` | 0.621053 | OCCULT 6TH-RANK SPELLS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/10/SectionHeader/35` | 0.616681 | ARCANE 6TH-RANK SPELLS |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/29/SectionHeader/35` | 0.551627 | **CURSED METAMORPHOSIS **[two-actions] **SPELL 6**  **CONCENTRATE** **CURSE** **INCAPACITATION** **MANIPULATE** **POLYMORPH**  **Traditions** arcane, occult, primal **Range **30 feet;** Targets** 1 cr |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/12/SectionHeader/67` | 0.551109 | DIVINE 6TH-RANK SPELLS |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/20` | 0.540395 | **BLAZING BOLT **[one-action]** TO **[three-actions] **SPELL 2**  **ATTACK** **CONCENTRATE** **FIRE** **MANIPULATE**  **Traditions** arcane, primal  **Range **60 feet; **Targets** 1 or more creatures |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/32/SectionHeader/55` | 0.538347 | **DOMINATE **[two-actions] **SPELL 6**  **UNCOMMON** **CONCENTRATE** **INCAPACITATION** **MANIPULATE** **MENTAL**  **Traditions** arcane, divine, occult  **Range **30 feet;** Targets** 1 creature  **D |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/18/SectionHeader/24` | 0.537868 | PRIMAL 6TH-RANK SPELLS |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/31/SectionHeader/38` | 0.537112 | **DISINTEGRATE **[two-actions] **SPELL 6**  **ATTACK** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane  **Range **120 feet;** Targets** 1 creature, unattended object, or  force construct  **Defe |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/34/SectionHeader/6` | 0.536265 | **ECLIPSE BURST **[two-actions] **SPELL 7**  **COLD** **CONCENTRATE** **DARKNESS** **MANIPULATE** **VOID**  **Traditions** arcane, divine, primal **Range **500 feet;** Area** 60-foot burst  **Defense* |

### Query 147
- Text: What does **COZY CRASHPAD** **SPELL 3** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/47']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/47', 'PZO22001 Starfinder Player Core 294-329::/page/14/SectionHeader/62', 'PZO22001 Starfinder Player Core 294-329::/page/9/SectionHeader/42']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/47', 'PZO22001 Starfinder Player Core 294-329::/page/29/Text/2', 'PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/39']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/29/Text/2` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/39` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/47` | 0.675401 | **COZY CRASHPAD** **SPELL 3**  **CONCENTRATE** **MANIPULATE** **METAL**  **Traditions** arcane, occult  **Cast** 1 minute  **Range **30 feet  **Duration** 12 hours  You shape a shack 20 feet on each s |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/14/SectionHeader/62` | 0.633162 | OCCULT 3RD-RANK SPELLS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/9/SectionHeader/42` | 0.609547 | ARCANE 3RD-RANK SPELLS |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/17/SectionHeader/49` | 0.563460 | PRIMAL 3RD-RANK SPELLS |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/12/SectionHeader/22` | 0.547093 | DIVINE 3RD-RANK SPELLS |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/33` | 0.540163 | **EQUIPMENT** **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/23/Text/43` | 0.540163 | **EQUIPMENT** **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/13` | 0.537427 | SUSTAINING SPELLS |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/12` | 0.524278 | FOCUS SPELLS |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0` | 0.523367 | CHAPTER 7: SPELLS |

### Query 148
- Text: What does **CREATE FOOD** **SPELL 2** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/29/Text/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/29/Text/2', 'PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0', 'PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/47']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/29/Text/2', 'PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/47', 'PZO22001 Starfinder Player Core 294-329::/page/29/SectionHeader/9']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/47` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/29/SectionHeader/9` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/2` | 0.661702 | **CREATE FOOD** **SPELL 2**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, primal  **Cast** 1 hour  **Range **30 feet  You create enough food to feed six Medium creatures for a  day. |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0` | 0.614033 | CHAPTER 7: SPELLS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/47` | 0.609651 | **CLEANSE CUISINE **[two-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE**  **Traditions** divine, primal  **Range **10 feet;** Area** 1 cubic foot  You transform all food and beverages in the area |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/14/SectionHeader/25` | 0.557706 | OCCULT 2ND-RANK SPELLS |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/75` | 0.557216 | **Create Food**H Feed multiple creatures with conjured food. |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/9` | 0.557216 | **Create Food**H Feed multiple creatures with conjured food. |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/24` | 0.557216 | **Create Food**H Feed multiple creatures with conjured food. |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/23` | 0.555790 | SPELL ATTACKS |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/17/SectionHeader/17` | 0.549660 | PRIMAL 2ND-RANK SPELLS |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/29/SectionHeader/9` | 0.545730 | **CREATE WATER **[two-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE** **WATER**  **Traditions** arcane, divine, primal  **Range **0 feet |

### Query 149
- Text: What does **CREATE WATER **[two-actions] **SPELL 1** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/29/SectionHeader/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/29/SectionHeader/9', 'PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/47', 'PZO22001 Starfinder Player Core 294-329::/page/7/Text/19']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/29/SectionHeader/9', 'PZO22001 Starfinder Player Core 294-329::/page/29/Text/14', 'PZO22001 Starfinder Player Core 294-329::/page/29/Text/2']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/29/Text/14` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/29/Text/2` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/29/SectionHeader/9` | 0.782075 | **CREATE WATER **[two-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE** **WATER**  **Traditions** arcane, divine, primal  **Range **0 feet |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/47` | 0.654891 | **CLEANSE CUISINE **[two-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE**  **Traditions** divine, primal  **Range **10 feet;** Area** 1 cubic foot  You transform all food and beverages in the area |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/19` | 0.638668 | **SPELL NAME **[one-action] **SPELL (RANK)** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/23` | 0.590712 | SPELL ATTACKS |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/16/Text/65` | 0.581766 | **Create Water** Conjure 2 gallons of water. |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/8/Text/34` | 0.581766 | **Create Water** Conjure 2 gallons of water. |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/52` | 0.581766 | **Create Water** Conjure 2 gallons of water. |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/52` | 0.577631 | **CHARM **[two-actions] **SPELL 1**  **CONCENTRATE** **EMOTION** **INCAPACITATION** **MANIPULATE** **MENTAL** **SUBTLE**  **Traditions** arcane, occult, primal **Range **30 feet;** Targets** 1 creatur |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/54` | 0.576487 | **CLEAR MIND **[two-actions] **SPELL 2**  **CONCENTRATE** **HEALING** **MANIPULATE** **MENTAL**  **Traditions** divine, occult, primal  **Range **touch; **Targets** 1 willing creature  You drive menta |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/28/Text/11` | 0.575153 | **CONFUSION **[two-actions] **SPELL 4**  **CONCENTRATE** **EMOTION** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult **Range **30 feet;** Targets** 1 creature **Defense** Will; **Duration** 1 |
