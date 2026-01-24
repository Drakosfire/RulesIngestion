# RulesLawyer Evaluation Report: nomic-embed-text-v2

## Summary
- Run ID: `None`
- Ruleset ID: `None`
- Document ID: `None`
- Chunk source: `enriched`
- Chunk count: `1059`
- Query count: `108`
- Evaluated queries: `108`
- Coverage: `1.0000`
- MRR: `0.8949`
- hit@1: `0.8333`
- hit@3: `0.9537`
- hit@5: `1.0000`
- hit@10: `1.0000`
- Embeddings reused: `False`
- Graph boost: `0.05` (depth=2, top_k=50, source=top, seed_top_n=3, same_kind_only=False, decay=0.4)

### Expanded Gold Metrics
- Coverage: `1.0000`
- MRR: `0.9057`
- hit@1: `0.8519`
- hit@3: `0.9537`
- hit@5: `1.0000`
- hit@10: `1.0000`

### Expanded Gold Expansion Stats
- Queries with additions: `108`
- Avg added per query: `2.11`
- Max added: `7`
- Addition reasons:
  - graph_depth_1: `228`

### Expanded Gold Delta (Expanded - Strict)
- Coverage Δ: `0.0000`
- MRR Δ: `0.0108`
- hit@1 Δ: `0.0185`
- hit@3 Δ: `0.0000`
- hit@5 Δ: `0.0000`
- hit@10 Δ: `0.0000`

## Timings (ms)
- Embedding (chunks): `12300`
- Embedding (queries): `3278`
- Evaluation (strict): `114`
- Evaluation (expanded): `82`
- Total: `20129`

### Timing Estimates (ms)
- Evaluation (strict): `151`
- Evaluation (expanded): `118`
- Total: `15847`

## Query Details
### Query 0
- Text: Summarize MAGIC ITEMS
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/1', 'PZO22001 Starfinder Player Core 282-293::/page/4/SectionHeader/55', 'PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/21']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/1', 'PZO22001 Starfinder Player Core 282-293::/page/0/Text/2']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/0/Text/2` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/1` | 0.945710 | MAGIC ITEMS |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/4/SectionHeader/55` | 0.898785 | **MAGIC ITEMS** |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/21` | 0.878616 | SPECIFIC MAGIC ITEMS |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/9/Text/52` | 0.835567 | **Magic Items** |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/7/Text/76` | 0.835567 | **Magic Items** |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/61` | 0.835567 | **Magic Items** |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/3/Text/47` | 0.835567 | **Magic Items** |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/6` | 0.798043 | INVESTING MAGIC ITEMS |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/11/Text/38` | 0.682162 | **Magic Items** **Augmentations** |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/5/Text/16` | 0.617207 | **Grenades** **Magic Items** |

### Query 1
- Text: What is the rule about From orbiting crystals imbued with power to gravity-defying equipment and hardlight devices, magic  items are popular accessories for adventurers and collectors. Engineers have developed fascinating  new fusions of magic and technology, often called magitech or hybrid tech, while artisans have  revived magical crafting techniques from eras long past. Shopping for new magic gear is as simple  as searching the infosphere, visiting a corporate storefront, or browsing an antique mall. Curiosity  shops and flea markets are full of everything from knockoffs of the latest cutting-edge inventions to  precious relics preserved from the ancient past, if you know where to look.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/0/Text/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/0/Text/2', 'PZO22001 Starfinder Player Core 282-293::/page/0/Text/4', 'PZO22001 Starfinder Player Core 282-293::/page/0/Text/5']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/0/Text/2', 'PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/1', 'PZO22001 Starfinder Player Core 282-293::/page/0/Text/4']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/1` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/0/Text/4` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/2` | 1.000489 | From orbiting crystals imbued with power to gravity-defying equipment and hardlight devices, magic  items are popular accessories for adventurers and collectors. Engineers have developed fascinating |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/4` | 0.796908 | Technology and magic are everywhere in the galaxy.  While some magic equipment have gone unchanged for  thousands of years, the integration of technology to  improve the functionality or cost of many |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/5` | 0.630867 | The tables on pages 286–287 list level, price, Bulk,  and hands entries for a wide variety of magic and hybrid  items. Each item has its own rules for how it functions:  some require bespoke activatio |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/6` | 0.591782 | INVESTING MAGIC ITEMS |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/1` | 0.580322 | MAGIC ITEMS |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/9/Text/25` | 0.561255 | Magitech augmentations are a combination of cybernetic and  magical components, created with special-made elements  like mystically charged crystals, starmetal alloys, and runeengraved microchips. Mag |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/21` | 0.549459 | SPECIFIC MAGIC ITEMS |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/2/Text/6` | 0.546094 | **Tech:** Items with the tech trait can be crafted by  anyone, but if they're level 1 or higher, they require  the Tech Crafting feat (page 229) to craft. If a tech  item also has the magical trait, t |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/4/SectionHeader/55` | 0.535527 | **MAGIC ITEMS** |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/7` | 0.532984 | Certain magic and hybrid items convey their benefits only  when worn and invested using the Invest an Item activity,  connecting them to a specific PC. A PC can benefit from  no more than 10 invested |

### Query 2
- Text: What is the rule about Technology and magic are everywhere in the galaxy.  While some magic equipment have gone unchanged for  thousands of years, the integration of technology to  improve the functionality or cost of many popular items  has given rise to hybrid items, which have both the magical  and tech traits.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/0/Text/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/0/Text/4', 'PZO22001 Starfinder Player Core 282-293::/page/0/Text/2', 'PZO22001 Starfinder Player Core 282-293::/page/2/Text/6']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/0/Text/4', 'PZO22001 Starfinder Player Core 282-293::/page/0/Text/2', 'PZO22001 Starfinder Player Core 282-293::/page/0/Text/5']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/0/Text/2` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/0/Text/5` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/4` | 0.982558 | Technology and magic are everywhere in the galaxy.  While some magic equipment have gone unchanged for  thousands of years, the integration of technology to  improve the functionality or cost of many |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/2` | 0.729811 | From orbiting crystals imbued with power to gravity-defying equipment and hardlight devices, magic  items are popular accessories for adventurers and collectors. Engineers have developed fascinating |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/2/Text/6` | 0.680020 | **Tech:** Items with the tech trait can be crafted by  anyone, but if they're level 1 or higher, they require  the Tech Crafting feat (page 229) to craft. If a tech  item also has the magical trait, t |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/5` | 0.613876 | The tables on pages 286–287 list level, price, Bulk,  and hands entries for a wide variety of magic and hybrid  items. Each item has its own rules for how it functions:  some require bespoke activatio |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/7` | 0.569310 | Certain magic and hybrid items convey their benefits only  when worn and invested using the Invest an Item activity,  connecting them to a specific PC. A PC can benefit from  no more than 10 invested |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/4/SectionHeader/24` | 0.549099 | **MAGICAL** **TECH** |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/9/Text/25` | 0.543690 | Magitech augmentations are a combination of cybernetic and  magical components, created with special-made elements  like mystically charged crystals, starmetal alloys, and runeengraved microchips. Mag |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/2/Text/5` | 0.530855 | **Magical:** Items with the magical trait can be crafted  only if a player has the Magical Crafting feat (page 224). |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/2/Text/16` | 0.521589 | **INVESTED** **MAGICAL** **TECH** |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/2/Text/23` | 0.521589 | **INVESTED** **MAGICAL** **TECH** |

### Query 3
- Text: What is the rule about The tables on pages 286–287 list level, price, Bulk,  and hands entries for a wide variety of magic and hybrid  items. Each item has its own rules for how it functions:  some require bespoke activations, while others function  automatically, such as by granting constant item bonuses  or other benefits when worn or held.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/0/Text/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/0/Text/5', 'PZO22001 Starfinder Player Core 282-293::/page/0/Text/12', 'PZO22001 Starfinder Player Core 282-293::/page/0/Text/7']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/0/Text/5', 'PZO22001 Starfinder Player Core 282-293::/page/0/Text/4', 'PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/6']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/0/Text/4` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/6` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/5` | 0.989073 | The tables on pages 286–287 list level, price, Bulk,  and hands entries for a wide variety of magic and hybrid  items. Each item has its own rules for how it functions:  some require bespoke activatio |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/12` | 0.631588 | While some items function automatically and grant constant  benefits, others produce effects only when properly used. An  activation lists the number of actions it takes and any traits  of the activat |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/7` | 0.580881 | Certain magic and hybrid items convey their benefits only  when worn and invested using the Invest an Item activity,  connecting them to a specific PC. A PC can benefit from  no more than 10 invested |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/2/Text/6` | 0.529422 | **Tech:** Items with the tech trait can be crafted by  anyone, but if they're level 1 or higher, they require  the Tech Crafting feat (page 229) to craft. If a tech  item also has the magical trait, t |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/4` | 0.521466 | Technology and magic are everywhere in the galaxy.  While some magic equipment have gone unchanged for  thousands of years, the integration of technology to  improve the functionality or cost of many |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/20` | 0.490864 | If the activation entry for an item lists "Cast a Spell" after  "Activate", you must use the same action as casting the spell  to Activate the Item, unless noted otherwise. You must have  a spellcasti |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/2/Text/5` | 0.487376 | **Magical:** Items with the magical trait can be crafted  only if a player has the Magical Crafting feat (page 224). |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/9` | 0.478245 | You invest your energy in an item with the invested trait  as you don it. This process requires 1 or more Interact  actions, usually taking the same amount of time it takes to  don the item. Once you' |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/16` | 0.473634 | If the activation entry for an item has the manipulate trait,  you can activate it only if you're holding the item or touching  it with a free hand. |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/5/Table/2` | 0.473524 | ItemLevelPriceBulkHandsGlow up spell amp, advanced91,100L1Diva's microphone, tactical109,500L1Hardlight handwraps, superior1010,005——Resist energy spell amp, tactical101,800L15th-rank spell chip1115,0 |

### Query 4
- Text: Summarize INVESTING MAGIC ITEMS
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/6', 'PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/1', 'PZO22001 Starfinder Player Core 282-293::/page/4/SectionHeader/55']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/6', 'PZO22001 Starfinder Player Core 282-293::/page/0/Text/7', 'PZO22001 Starfinder Player Core 282-293::/page/0/Text/5']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/0/Text/7` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/0/Text/5` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/6` | 0.999163 | INVESTING MAGIC ITEMS |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/1` | 0.787101 | MAGIC ITEMS |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/4/SectionHeader/55` | 0.736949 | **MAGIC ITEMS** |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/21` | 0.689670 | SPECIFIC MAGIC ITEMS |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/9/Text/52` | 0.663991 | **Magic Items** |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/61` | 0.663991 | **Magic Items** |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/7/Text/76` | 0.663991 | **Magic Items** |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/3/Text/47` | 0.663991 | **Magic Items** |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/7` | 0.653084 | Certain magic and hybrid items convey their benefits only  when worn and invested using the Invest an Item activity,  connecting them to a specific PC. A PC can benefit from  no more than 10 invested |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/21` | 0.587755 | **INVESTED** **MAGICAL** **TECH** |

### Query 5
- Text: What is the rule about Certain magic and hybrid items convey their benefits only  when worn and invested using the Invest an Item activity,  connecting them to a specific PC. A PC can benefit from  no more than 10 invested magic items each day. A PC can  still gain the mundane benefits of a magic item without  investiture.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/0/Text/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/0/Text/7', 'PZO22001 Starfinder Player Core 282-293::/page/2/Text/4', 'PZO22001 Starfinder Player Core 282-293::/page/0/Text/9']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/0/Text/7', 'PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/8', 'PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/6']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/8` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/6` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/7` | 1.003834 | Certain magic and hybrid items convey their benefits only  when worn and invested using the Invest an Item activity,  connecting them to a specific PC. A PC can benefit from  no more than 10 invested |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/2/Text/4` | 0.787474 | **Invested:** A PC can wear only 10 magical items that  have the invested trait. A character can still gain any  normal benefit from using a physical item without  investing it, such as using a *progr |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/9` | 0.672346 | You invest your energy in an item with the invested trait  as you don it. This process requires 1 or more Interact  actions, usually taking the same amount of time it takes to  don the item. Once you' |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/10` | 0.625090 | You can invest no more than 10 items per day. If you  remove an invested item, it loses its investiture. The item still  counts against your daily limit after it loses its investiture.  You reset the |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/6` | 0.581299 | INVESTING MAGIC ITEMS |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/14` | 0.570976 | You can Activate an Item with the invested trait only if it's  invested by you. |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/5` | 0.564790 | The tables on pages 286–287 list level, price, Bulk,  and hands entries for a wide variety of magic and hybrid  items. Each item has its own rules for how it functions:  some require bespoke activatio |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/4` | 0.508260 | Technology and magic are everywhere in the galaxy.  While some magic equipment have gone unchanged for  thousands of years, the integration of technology to  improve the functionality or cost of many |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/2/Text/6` | 0.508259 | **Tech:** Items with the tech trait can be crafted by  anyone, but if they're level 1 or higher, they require  the Tech Crafting feat (page 229) to craft. If a tech  item also has the magical trait, t |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/18` | 0.505239 | Some items can be activated only a certain number of times  per day, resetting during your daily preparations. You retain  the constant benefits of these items even when the activation  requirements o |

### Query 6
- Text: Summarize **INVEST AN ITEM**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/8']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/8', 'PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/13', 'PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/6']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/8', 'PZO22001 Starfinder Player Core 282-293::/page/0/Text/7', 'PZO22001 Starfinder Player Core 282-293::/page/0/Text/9']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/0/Text/7` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/0/Text/9` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/8` | 0.960194 | **INVEST AN ITEM** |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/13` | 0.647553 | ACTIVATING INVESTED ITEMS |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/6` | 0.605947 | INVESTING MAGIC ITEMS |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/7` | 0.510741 | Certain magic and hybrid items convey their benefits only  when worn and invested using the Invest an Item activity,  connecting them to a specific PC. A PC can benefit from  no more than 10 invested |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/14` | 0.501840 | You can Activate an Item with the invested trait only if it's  invested by you. |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/9` | 0.499836 | You invest your energy in an item with the invested trait  as you don it. This process requires 1 or more Interact  actions, usually taking the same amount of time it takes to  don the item. Once you' |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/10` | 0.483682 | You can invest no more than 10 items per day. If you  remove an invested item, it loses its investiture. The item still  counts against your daily limit after it loses its investiture.  You reset the |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/21` | 0.461356 | **INVESTED** **MAGICAL** **TECH** |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/3/Text/6` | 0.461356 | **INVESTED** **MAGICAL** **TECH** |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/3/Text/15` | 0.461356 | **INVESTED** **MAGICAL** **TECH** |

### Query 7
- Text: What is the rule about You invest your energy in an item with the invested trait  as you don it. This process requires 1 or more Interact  actions, usually taking the same amount of time it takes to  don the item. Once you've Invested the Item, you benefit  from its constant magical abilities as long as you meet its  other requirements (for most invested items, the only other  requirement is that you must be wearing the item). This  investiture lasts until you remove the item.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/0/Text/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/0/Text/9', 'PZO22001 Starfinder Player Core 282-293::/page/2/Text/4', 'PZO22001 Starfinder Player Core 282-293::/page/0/Text/14']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/0/Text/9', 'PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/8', 'PZO22001 Starfinder Player Core 282-293::/page/0/Text/10']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/8` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/0/Text/10` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/9` | 0.983263 | You invest your energy in an item with the invested trait  as you don it. This process requires 1 or more Interact  actions, usually taking the same amount of time it takes to  don the item. Once you' |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/2/Text/4` | 0.728282 | **Invested:** A PC can wear only 10 magical items that  have the invested trait. A character can still gain any  normal benefit from using a physical item without  investing it, such as using a *progr |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/14` | 0.699907 | You can Activate an Item with the invested trait only if it's  invested by you. |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/7` | 0.651779 | Certain magic and hybrid items convey their benefits only  when worn and invested using the Invest an Item activity,  connecting them to a specific PC. A PC can benefit from  no more than 10 invested |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/10` | 0.598841 | You can invest no more than 10 items per day. If you  remove an invested item, it loses its investiture. The item still  counts against your daily limit after it loses its investiture.  You reset the |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/12` | 0.561795 | While some items function automatically and grant constant  benefits, others produce effects only when properly used. An  activation lists the number of actions it takes and any traits  of the activat |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/11/Text/12` | 0.555830 | **Activate—Irresistible Idea** [two-actions] (concentrate) **Frequency** once per hour; **Effect** You manipulate your cosmetics to  influence a creature as a 4th-rank *suggestion* (DC 38). |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/20` | 0.541373 | If the activation entry for an item lists "Cast a Spell" after  "Activate", you must use the same action as casting the spell  to Activate the Item, unless noted otherwise. You must have  a spellcasti |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/2/Text/5` | 0.537835 | **Magical:** Items with the magical trait can be crafted  only if a player has the Magical Crafting feat (page 224). |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/16` | 0.536595 | If the activation entry for an item has the manipulate trait,  you can activate it only if you're holding the item or touching  it with a free hand. |

### Query 8
- Text: Summarize You can invest no more than 10 items per day. If you  remove an invested item, it loses its investiture. The item still  counts against your daily limit after it loses its investiture.  You reset the limit during your daily preparations, at which  point you Invest your Items anew. If you're still wearing  items you had invested the previous day, you can typically  keep them invested on the new day, but they still count  against your limit.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/0/Text/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/0/Text/10', 'PZO22001 Starfinder Player Core 282-293::/page/0/Text/7', 'PZO22001 Starfinder Player Core 282-293::/page/2/Text/4']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/0/Text/10', 'PZO22001 Starfinder Player Core 282-293::/page/0/Text/9', 'PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/11']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/0/Text/9` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/11` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/10` | 1.045297 | You can invest no more than 10 items per day. If you  remove an invested item, it loses its investiture. The item still  counts against your daily limit after it loses its investiture.  You reset the |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/7` | 0.656357 | Certain magic and hybrid items convey their benefits only  when worn and invested using the Invest an Item activity,  connecting them to a specific PC. A PC can benefit from  no more than 10 invested |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/2/Text/4` | 0.612973 | **Invested:** A PC can wear only 10 magical items that  have the invested trait. A character can still gain any  normal benefit from using a physical item without  investing it, such as using a *progr |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/9` | 0.552620 | You invest your energy in an item with the invested trait  as you don it. This process requires 1 or more Interact  actions, usually taking the same amount of time it takes to  don the item. Once you' |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/18` | 0.549915 | Some items can be activated only a certain number of times  per day, resetting during your daily preparations. You retain  the constant benefits of these items even when the activation  requirements o |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/14` | 0.514996 | You can Activate an Item with the invested trait only if it's  invested by you. |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/8` | 0.449323 | **INVEST AN ITEM** |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/13` | 0.448285 | ACTIVATING INVESTED ITEMS |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/6/Text/8` | 0.446413 | You're limited to four implanted augmentations. A surgeon  implanting an augmentation in your body must remove one  of your existing augmentations (see below) if you're already  at the limit. You can |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/6` | 0.404516 | INVESTING MAGIC ITEMS |

### Query 9
- Text: What is the rule about ACTIVATING ITEMS?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/11', 'PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/13', 'PZO22001 Starfinder Player Core 282-293::/page/0/Text/12']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/11', 'PZO22001 Starfinder Player Core 282-293::/page/0/Text/12', 'PZO22001 Starfinder Player Core 282-293::/page/0/Text/10']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/0/Text/12` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/0/Text/10` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/11` | 0.853689 | ACTIVATING ITEMS |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/13` | 0.713204 | ACTIVATING INVESTED ITEMS |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/12` | 0.628348 | While some items function automatically and grant constant  benefits, others produce effects only when properly used. An  activation lists the number of actions it takes and any traits  of the activat |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/20` | 0.561800 | If the activation entry for an item lists "Cast a Spell" after  "Activate", you must use the same action as casting the spell  to Activate the Item, unless noted otherwise. You must have  a spellcasti |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/14` | 0.554078 | You can Activate an Item with the invested trait only if it's  invested by you. |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/18` | 0.536857 | Some items can be activated only a certain number of times  per day, resetting during your daily preparations. You retain  the constant benefits of these items even when the activation  requirements o |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/15` | 0.526934 | MANIPULATE ACTIVATIONS |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/16` | 0.510863 | If the activation entry for an item has the manipulate trait,  you can activate it only if you're holding the item or touching  it with a free hand. |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/6/SectionHeader/11` | 0.482681 | ACTIVATING AUGMENTATIONS |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/17` | 0.468213 | LIMITED ACTIVATIONS |

### Query 10
- Text: What is the rule about While some items function automatically and grant constant  benefits, others produce effects only when properly used. An  activation lists the number of actions it takes and any traits  of the activation and its effect. This information appears in  the item's Activate entry.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/0/Text/12']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/0/Text/12', 'PZO22001 Starfinder Player Core 282-293::/page/0/Text/20', 'PZO22001 Starfinder Player Core 282-293::/page/6/Text/12']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/0/Text/12', 'PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/13', 'PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/11']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/13` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/11` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/12` | 0.995241 | While some items function automatically and grant constant  benefits, others produce effects only when properly used. An  activation lists the number of actions it takes and any traits  of the activat |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/20` | 0.701182 | If the activation entry for an item lists "Cast a Spell" after  "Activate", you must use the same action as casting the spell  to Activate the Item, unless noted otherwise. You must have  a spellcasti |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/6/Text/12` | 0.666424 | Many augmentations work continuously. Augmentations  with an Activate entry usually require you to concentrate or  Interact to gain an additional boost or ability. Once activated,  an augmentation oft |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/16` | 0.603211 | If the activation entry for an item has the manipulate trait,  you can activate it only if you're holding the item or touching  it with a free hand. |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/8/Text/40` | 0.598186 | **Activate—Draw** [one-action] (manipulate) **Effect** You Interact to draw  an item concealed in your hideaway limb. |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/4/Text/6` | 0.587318 | **Activate—Inject** [one-action] (manipulate) **Effect** You Cast the Spell at  the indicated rank. |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/5` | 0.585436 | The tables on pages 286–287 list level, price, Bulk,  and hands entries for a wide variety of magic and hybrid  items. Each item has its own rules for how it functions:  some require bespoke activatio |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/9` | 0.578646 | You invest your energy in an item with the invested trait  as you don it. This process requires 1 or more Interact  actions, usually taking the same amount of time it takes to  don the item. Once you' |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/18` | 0.578405 | Some items can be activated only a certain number of times  per day, resetting during your daily preparations. You retain  the constant benefits of these items even when the activation  requirements o |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/14` | 0.575938 | You can Activate an Item with the invested trait only if it's  invested by you. |

### Query 11
- Text: What is the rule about ACTIVATING INVESTED ITEMS?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/13', 'PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/11', 'PZO22001 Starfinder Player Core 282-293::/page/0/Text/14']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/13', 'PZO22001 Starfinder Player Core 282-293::/page/0/Text/14', 'PZO22001 Starfinder Player Core 282-293::/page/0/Text/12']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/0/Text/14` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/0/Text/12` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/13` | 0.899295 | ACTIVATING INVESTED ITEMS |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/11` | 0.716861 | ACTIVATING ITEMS |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/14` | 0.703222 | You can Activate an Item with the invested trait only if it's  invested by you. |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/12` | 0.539169 | While some items function automatically and grant constant  benefits, others produce effects only when properly used. An  activation lists the number of actions it takes and any traits  of the activat |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/10` | 0.530924 | You can invest no more than 10 items per day. If you  remove an invested item, it loses its investiture. The item still  counts against your daily limit after it loses its investiture.  You reset the |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/9` | 0.524176 | You invest your energy in an item with the invested trait  as you don it. This process requires 1 or more Interact  actions, usually taking the same amount of time it takes to  don the item. Once you' |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/7` | 0.507746 | Certain magic and hybrid items convey their benefits only  when worn and invested using the Invest an Item activity,  connecting them to a specific PC. A PC can benefit from  no more than 10 invested |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/8` | 0.501582 | **INVEST AN ITEM** |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/15` | 0.489140 | MANIPULATE ACTIVATIONS |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/20` | 0.485310 | If the activation entry for an item lists "Cast a Spell" after  "Activate", you must use the same action as casting the spell  to Activate the Item, unless noted otherwise. You must have  a spellcasti |

### Query 12
- Text: What is the rule about You can Activate an Item with the invested trait only if it's  invested by you.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/0/Text/14']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/0/Text/14', 'PZO22001 Starfinder Player Core 282-293::/page/0/Text/9', 'PZO22001 Starfinder Player Core 282-293::/page/0/Text/16']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/0/Text/14', 'PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/15', 'PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/13']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/15` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/13` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/14` | 0.974624 | You can Activate an Item with the invested trait only if it's  invested by you. |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/9` | 0.678601 | You invest your energy in an item with the invested trait  as you don it. This process requires 1 or more Interact  actions, usually taking the same amount of time it takes to  don the item. Once you' |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/16` | 0.669641 | If the activation entry for an item has the manipulate trait,  you can activate it only if you're holding the item or touching  it with a free hand. |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/2/Text/4` | 0.584765 | **Invested:** A PC can wear only 10 magical items that  have the invested trait. A character can still gain any  normal benefit from using a physical item without  investing it, such as using a *progr |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/20` | 0.567932 | If the activation entry for an item lists "Cast a Spell" after  "Activate", you must use the same action as casting the spell  to Activate the Item, unless noted otherwise. You must have  a spellcasti |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/13` | 0.567639 | ACTIVATING INVESTED ITEMS |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/12` | 0.543882 | While some items function automatically and grant constant  benefits, others produce effects only when properly used. An  activation lists the number of actions it takes and any traits  of the activat |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/10` | 0.532301 | You can invest no more than 10 items per day. If you  remove an invested item, it loses its investiture. The item still  counts against your daily limit after it loses its investiture.  You reset the |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/7` | 0.529696 | Certain magic and hybrid items convey their benefits only  when worn and invested using the Invest an Item activity,  connecting them to a specific PC. A PC can benefit from  no more than 10 invested |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/8/Text/43` | 0.491346 | When you use Draw, if the item can be activated or otherwise  used with a single action, you can use the item as part of the  same action. For example, you Interact to draw a weapon, then  Strike with |

### Query 13
- Text: What is the rule about MANIPULATE ACTIVATIONS?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/15']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/15', 'PZO22001 Starfinder Player Core 282-293::/page/0/Text/16', 'PZO22001 Starfinder Player Core 282-293::/page/8/Text/40']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/15', 'PZO22001 Starfinder Player Core 282-293::/page/0/Text/16', 'PZO22001 Starfinder Player Core 282-293::/page/0/Text/14']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/0/Text/16` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/0/Text/14` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/15` | 0.899133 | MANIPULATE ACTIVATIONS |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/16` | 0.618739 | If the activation entry for an item has the manipulate trait,  you can activate it only if you're holding the item or touching  it with a free hand. |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/8/Text/40` | 0.577169 | **Activate—Draw** [one-action] (manipulate) **Effect** You Interact to draw  an item concealed in your hideaway limb. |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/17` | 0.516614 | LIMITED ACTIVATIONS |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/12` | 0.506644 | While some items function automatically and grant constant  benefits, others produce effects only when properly used. An  activation lists the number of actions it takes and any traits  of the activat |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/4/Text/6` | 0.495304 | **Activate—Inject** [one-action] (manipulate) **Effect** You Cast the Spell at  the indicated rank. |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/3/Text/30` | 0.490966 | **Activate—Install Grenade** [one-action] (manipulate) You install a  commercial, tactical, or advanced grenade in the shell.  You can store one grenade in the shell at a time, and you  can Interact t |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/11/Text/12` | 0.467707 | **Activate—Irresistible Idea** [two-actions] (concentrate) **Frequency** once per hour; **Effect** You manipulate your cosmetics to  influence a creature as a 4th-rank *suggestion* (DC 38). |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/11` | 0.466211 | ACTIVATING ITEMS |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/34` | 0.465877 | **Activate—Gravity Alteration** [one-action] (manipulate) **Effect** You treat  gravity as being one step higher or lower (for example,  zero-g becomes low gravity, low gravity becomes standard,  stan |

### Query 14
- Text: What is the rule about If the activation entry for an item has the manipulate trait,  you can activate it only if you're holding the item or touching  it with a free hand.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/0/Text/16']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/0/Text/16', 'PZO22001 Starfinder Player Core 282-293::/page/0/Text/14', 'PZO22001 Starfinder Player Core 282-293::/page/0/Text/12']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/0/Text/16', 'PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/15', 'PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/17']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/15` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/17` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/16` | 1.004406 | If the activation entry for an item has the manipulate trait,  you can activate it only if you're holding the item or touching  it with a free hand. |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/14` | 0.682519 | You can Activate an Item with the invested trait only if it's  invested by you. |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/12` | 0.630466 | While some items function automatically and grant constant  benefits, others produce effects only when properly used. An  activation lists the number of actions it takes and any traits  of the activat |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/20` | 0.575056 | If the activation entry for an item lists "Cast a Spell" after  "Activate", you must use the same action as casting the spell  to Activate the Item, unless noted otherwise. You must have  a spellcasti |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/8/Text/40` | 0.566327 | **Activate—Draw** [one-action] (manipulate) **Effect** You Interact to draw  an item concealed in your hideaway limb. |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/9` | 0.533954 | You invest your energy in an item with the invested trait  as you don it. This process requires 1 or more Interact  actions, usually taking the same amount of time it takes to  don the item. Once you' |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/8/Text/43` | 0.529187 | When you use Draw, if the item can be activated or otherwise  used with a single action, you can use the item as part of the  same action. For example, you Interact to draw a weapon, then  Strike with |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/15` | 0.508534 | MANIPULATE ACTIVATIONS |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/4/Text/6` | 0.494012 | **Activate—Inject** [one-action] (manipulate) **Effect** You Cast the Spell at  the indicated rank. |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/2/Text/5` | 0.493446 | **Magical:** Items with the magical trait can be crafted  only if a player has the Magical Crafting feat (page 224). |

### Query 15
- Text: What is the rule about LIMITED ACTIVATIONS?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/17']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/17', 'PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/15', 'PZO22001 Starfinder Player Core 282-293::/page/0/Text/18']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/17', 'PZO22001 Starfinder Player Core 282-293::/page/0/Text/16', 'PZO22001 Starfinder Player Core 282-293::/page/0/Text/18']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/0/Text/16` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/0/Text/18` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/17` | 0.871464 | LIMITED ACTIVATIONS |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/15` | 0.500069 | MANIPULATE ACTIVATIONS |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/18` | 0.460695 | Some items can be activated only a certain number of times  per day, resetting during your daily preparations. You retain  the constant benefits of these items even when the activation  requirements o |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/10` | 0.395032 | You can invest no more than 10 items per day. If you  remove an invested item, it loses its investiture. The item still  counts against your daily limit after it loses its investiture.  You reset the |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/14` | 0.388856 | You can Activate an Item with the invested trait only if it's  invested by you. |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/16` | 0.381595 | If the activation entry for an item has the manipulate trait,  you can activate it only if you're holding the item or touching  it with a free hand. |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/6/Text/12` | 0.378180 | Many augmentations work continuously. Augmentations  with an Activate entry usually require you to concentrate or  Interact to gain an additional boost or ability. Once activated,  an augmentation oft |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/11` | 0.377777 | ACTIVATING ITEMS |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/7/Text/59` | 0.377532 | **Activate—Accelerate** [free-action] **Frequency** once per 10 minutes;  **Trigger** You Climb, Stride, or Swim; **Effect** You increase  your Speed by 20 feet for the triggering action. |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/12` | 0.374760 | While some items function automatically and grant constant  benefits, others produce effects only when properly used. An  activation lists the number of actions it takes and any traits  of the activat |

### Query 16
- Text: What is the rule about Some items can be activated only a certain number of times  per day, resetting during your daily preparations. You retain  the constant benefits of these items even when the activation  requirements of these items can no longer be met.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/0/Text/18']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/0/Text/18', 'PZO22001 Starfinder Player Core 282-293::/page/0/Text/10', 'PZO22001 Starfinder Player Core 282-293::/page/0/Text/12']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/0/Text/18', 'PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/19', 'PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/17']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/19` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/17` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/18` | 0.981376 | Some items can be activated only a certain number of times  per day, resetting during your daily preparations. You retain  the constant benefits of these items even when the activation  requirements o |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/10` | 0.619974 | You can invest no more than 10 items per day. If you  remove an invested item, it loses its investiture. The item still  counts against your daily limit after it loses its investiture.  You reset the |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/12` | 0.606484 | While some items function automatically and grant constant  benefits, others produce effects only when properly used. An  activation lists the number of actions it takes and any traits  of the activat |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/6/Text/12` | 0.522857 | Many augmentations work continuously. Augmentations  with an Activate entry usually require you to concentrate or  Interact to gain an additional boost or ability. Once activated,  an augmentation oft |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/7` | 0.516125 | Certain magic and hybrid items convey their benefits only  when worn and invested using the Invest an Item activity,  connecting them to a specific PC. A PC can benefit from  no more than 10 invested |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/10/Text/22` | 0.512717 | **Activate—Regenerate** [two-actions] (concentrate) **Frequency** once  per day; **Effect** You gain the effects of a 4th-rank *genetic* *regeneration* spell. |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/10/Text/37` | 0.492889 | **Activate—Life Buffer **[one-action] (manipulate) **Frequency** once per day;  **Effect** You gain 50 temporary Hit Points, which last for 1 hour. |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/2/Text/3` | 0.465632 | **Consumable:** Items with the consumable trait can  be used only once. Most manufacturers design these  items so the container, syringe, or other remaining  materials can't be easily reused to protec |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/20` | 0.464057 | If the activation entry for an item lists "Cast a Spell" after  "Activate", you must use the same action as casting the spell  to Activate the Item, unless noted otherwise. You must have  a spellcasti |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/10/Text/42` | 0.463735 | **Activate—Access Database** [one-action] (concentrate) **Frequency** once  per hour; **Effect** Immediately attempt three checks to  Recall Knowledge about related topics, selecting each topic  after |

### Query 17
- Text: What is the rule about CAST A SPELL?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/19']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/19', 'PZO22001 Starfinder Player Core 282-293::/page/5/Text/18', 'PZO22001 Starfinder Player Core 282-293::/page/11/Text/39']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/19', 'PZO22001 Starfinder Player Core 282-293::/page/0/Text/20', 'PZO22001 Starfinder Player Core 282-293::/page/0/Text/18']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/0/Text/20` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/0/Text/18` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/19` | 0.843833 | CAST A SPELL |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/5/Text/18` | 0.576816 | **SPELLS** |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/11/Text/39` | 0.576816 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/9/Text/54` | 0.534816 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/63` | 0.534816 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/7/Text/78` | 0.534816 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/3/Text/49` | 0.534816 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/20` | 0.447595 | If the activation entry for an item lists "Cast a Spell" after  "Activate", you must use the same action as casting the spell  to Activate the Item, unless noted otherwise. You must have  a spellcasti |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/4/Text/26` | 0.445781 | These chips can be installed in comm units and other  computers to allow the device to cast spells. Each device  can have only one *spell chip*. Casting a spell from a *spell chip* requires holding th |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/4/Text/43` | 0.434980 | These latticed gemstones are suspended in a silicon casing  and encoded with the magical script necessary to cast  a single, specific spell. Casting a spell from a *spell gem* requires holding the gem |

### Query 18
- Text: What is the rule about If the activation entry for an item lists "Cast a Spell" after  "Activate", you must use the same action as casting the spell  to Activate the Item, unless noted otherwise. You must have  a spellcasting class feature to Activate an Item with this  activation. All the normal traits of the spell apply when you  cast it by Activating an Item.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/0/Text/20']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/0/Text/20', 'PZO22001 Starfinder Player Core 282-293::/page/4/Text/44', 'PZO22001 Starfinder Player Core 282-293::/page/0/Text/12']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/0/Text/20', 'PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/19', 'PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/21']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/19` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/21` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/20` | 1.015550 | If the activation entry for an item lists "Cast a Spell" after  "Activate", you must use the same action as casting the spell  to Activate the Item, unless noted otherwise. You must have  a spellcasti |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/4/Text/44` | 0.741315 | **Activate **Cast a Spell; **Effect** You Cast the Spell at the  indicated rank. |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/12` | 0.684435 | While some items function automatically and grant constant  benefits, others produce effects only when properly used. An  activation lists the number of actions it takes and any traits  of the activat |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/4/Text/6` | 0.637601 | **Activate—Inject** [one-action] (manipulate) **Effect** You Cast the Spell at  the indicated rank. |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/4/Text/29` | 0.607387 | **Activate **Cast a Spell; **Frequency** once per day, plus  overclock; **Effect** You Cast the Spell at the indicated  rank. |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/4/Text/43` | 0.601995 | These latticed gemstones are suspended in a silicon casing  and encoded with the magical script necessary to cast  a single, specific spell. Casting a spell from a *spell gem* requires holding the gem |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/14` | 0.566760 | You can Activate an Item with the invested trait only if it's  invested by you. |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/16` | 0.565860 | If the activation entry for an item has the manipulate trait,  you can activate it only if you're holding the item or touching  it with a free hand. |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/4/Text/26` | 0.562762 | These chips can be installed in comm units and other  computers to allow the device to cast spells. Each device  can have only one *spell chip*. Casting a spell from a *spell chip* requires holding th |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/9` | 0.524883 | You invest your energy in an item with the invested trait  as you don it. This process requires 1 or more Interact  actions, usually taking the same amount of time it takes to  don the item. Once you' |

### Query 19
- Text: Summarize SPECIFIC MAGIC ITEMS
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/21']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/21', 'PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/1', 'PZO22001 Starfinder Player Core 282-293::/page/4/SectionHeader/55']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/21', 'PZO22001 Starfinder Player Core 282-293::/page/0/Text/22', 'PZO22001 Starfinder Player Core 282-293::/page/0/Text/20']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/0/Text/22` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/0/Text/20` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/21` | 0.987585 | SPECIFIC MAGIC ITEMS |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/1` | 0.836908 | MAGIC ITEMS |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/4/SectionHeader/55` | 0.773042 | **MAGIC ITEMS** |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/7/Text/76` | 0.726568 | **Magic Items** |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/61` | 0.726568 | **Magic Items** |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/9/Text/52` | 0.726568 | **Magic Items** |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/3/Text/47` | 0.726568 | **Magic Items** |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/6` | 0.695621 | INVESTING MAGIC ITEMS |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/11/Text/38` | 0.609354 | **Magic Items** **Augmentations** |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/2` | 0.570731 | From orbiting crystals imbued with power to gravity-defying equipment and hardlight devices, magic  items are popular accessories for adventurers and collectors. Engineers have developed fascinating |

### Query 20
- Text: Summarize **AEON STONE** **ITEM 5+**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/0/Text/22']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/0/Text/22', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/3', 'PZO22001 Starfinder Player Core 282-293::/page/5/TableCell/1388']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/0/Text/22', 'PZO22001 Starfinder Player Core 282-293::/page/0/Text/24', 'PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/21']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/0/Text/24` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/21` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/22` | 1.026135 | **AEON STONE** **ITEM 5+** |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/3` | 0.581020 | There are various types of *aeon stones*, each with a  different appearance and magical effect. Each *aeon stone* also  gains a resonant power when slotted into specific items, such  as weapons with t |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/5/TableCell/1388` | 0.577720 | Aeon stone, guiding U |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/5/TableCell/1203` | 0.532773 | Aeon stone, uplifting U |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/5/TableCell/1248` | 0.517269 | Aeon stone, life givingU |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/5/TableCell/1403` | 0.510035 | Aeon stone, navigating U |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/5/TableCell/1348` | 0.483944 | Aeon stone, projecting U |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/2` | 0.396284 | When you invest one of these precisely shaped crystals,  the stone orbits your head (or another visible part of your  anatomy if you don't have a head) instead of being worn on  your body. You can sto |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/4/SectionHeader/1` | 0.394908 | **SPELL AMPOULE** **ITEM 1+** |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/26` | 0.386090 | Staple items within the Azlanti Star Empire, these gemstones  are popular status symbols for adventurers and wealthy  collectors. Despite their myriad forms and functions, |

### Query 21
- Text: Summarize **UNCOMMON** **INVESTED** **MAGICAL**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/0/Text/24']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/0/Text/24', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/21', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/31']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/0/Text/24', 'PZO22001 Starfinder Player Core 282-293::/page/0/Text/22', 'PZO22001 Starfinder Player Core 282-293::/page/0/Text/25']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/0/Text/22` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/0/Text/25` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/24` | 0.993610 | **UNCOMMON** **INVESTED** **MAGICAL** |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/21` | 0.802664 | **INVESTED** **MAGICAL** **TECH** |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/31` | 0.802664 | **INVESTED** **MAGICAL** **TECH** |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/2/Text/23` | 0.760664 | **INVESTED** **MAGICAL** **TECH** |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/2/Text/16` | 0.760664 | **INVESTED** **MAGICAL** **TECH** |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/3/Text/15` | 0.760664 | **INVESTED** **MAGICAL** **TECH** |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/42` | 0.760664 | **INVESTED** **MAGICAL** **TECH** |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/3/Text/6` | 0.760664 | **INVESTED** **MAGICAL** **TECH** |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/4/SectionHeader/24` | 0.593011 | **MAGICAL** **TECH** |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/4/SectionHeader/3` | 0.556250 | **CONSUMABLE** **MAGICAL** |

### Query 22
- Text: Summarize **Usage** worn; **Bulk **—
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/0/Text/25']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/0/Text/25', 'PZO22001 Starfinder Player Core 282-293::/page/2/Text/37', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/32']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/0/Text/25', 'PZO22001 Starfinder Player Core 282-293::/page/0/Text/26', 'PZO22001 Starfinder Player Core 282-293::/page/0/Text/24']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/0/Text/26` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/0/Text/24` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/25` | 1.007724 | **Usage** worn; **Bulk **— |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/2/Text/37` | 1.007724 | **Usage** worn; **Bulk **— |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/32` | 0.955176 | **Usage** worn garment; **Bulk **1 |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/2/Text/24` | 0.861553 | **Usage** worn gloves; **Bulk **— |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/2/Text/18` | 0.774923 | **Usage** worn armbands or gloves; **Bulk **L |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/22` | 0.766863 | **Usage** worn eyepiece; **Bulk **— |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/4/SectionHeader/25` | 0.713804 | **Usage** installed in computer or comm unit; **Bulk **– |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/3/Text/28` | 0.691966 | **Usage** held in 1 hand; **Bulk **1 |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/3/Text/7` | 0.678126 | **Usage** held in 2 hands; **Bulk **L |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/43` | 0.675447 | **Usage** held in 1 hand; **Bulk **L |

### Query 23
- Text: Summarize Staple items within the Azlanti Star Empire, these gemstones  are popular status symbols for adventurers and wealthy  collectors. Despite their myriad forms and functions,
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/0/Text/26']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/0/Text/26', 'PZO22001 Starfinder Player Core 282-293::/page/0/Text/2', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/3']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/0/Text/26', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/1', 'PZO22001 Starfinder Player Core 282-293::/page/0/Text/25']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/1` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/0/Text/25` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/26` | 1.039946 | Staple items within the Azlanti Star Empire, these gemstones  are popular status symbols for adventurers and wealthy  collectors. Despite their myriad forms and functions, |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/2` | 0.500554 | From orbiting crystals imbued with power to gravity-defying equipment and hardlight devices, magic  items are popular accessories for adventurers and collectors. Engineers have developed fascinating |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/3` | 0.494168 | There are various types of *aeon stones*, each with a  different appearance and magical effect. Each *aeon stone* also  gains a resonant power when slotted into specific items, such  as weapons with t |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/1` | 0.456501 | these stones are purportedly all fragments of crystal tools  used by otherworldly entities to build the Universe in  ancient times. |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/4` | 0.446926 | Technology and magic are everywhere in the galaxy.  While some magic equipment have gone unchanged for  thousands of years, the integration of technology to  improve the functionality or cost of many |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/4/Text/43` | 0.431817 | These latticed gemstones are suspended in a silicon casing  and encoded with the magical script necessary to cast  a single, specific spell. Casting a spell from a *spell gem* requires holding the gem |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/5/TableCell/1198` | 0.407222 | 3rd-rank spell gem |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/5/TableCell/1148` | 0.402769 | 2nd-rank spell gem |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/5` | 0.402513 | The tables on pages 286–287 list level, price, Bulk,  and hands entries for a wide variety of magic and hybrid  items. Each item has its own rules for how it functions:  some require bespoke activatio |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/5/TableCell/1418` | 0.398601 | 9th-rank spell gem |

### Query 24
- Text: Summarize these stones are purportedly all fragments of crystal tools  used by otherworldly entities to build the Universe in  ancient times.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/1', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/3', 'PZO22001 Starfinder Player Core 282-293::/page/0/Text/26']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/1', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/2', 'PZO22001 Starfinder Player Core 282-293::/page/0/Text/26']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/2` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/0/Text/26` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/1` | 1.035694 | these stones are purportedly all fragments of crystal tools  used by otherworldly entities to build the Universe in  ancient times. |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/3` | 0.577434 | There are various types of *aeon stones*, each with a  different appearance and magical effect. Each *aeon stone* also  gains a resonant power when slotted into specific items, such  as weapons with t |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/26` | 0.485852 | Staple items within the Azlanti Star Empire, these gemstones  are popular status symbols for adventurers and wealthy  collectors. Despite their myriad forms and functions, |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/2` | 0.443387 | When you invest one of these precisely shaped crystals,  the stone orbits your head (or another visible part of your  anatomy if you don't have a head) instead of being worn on  your body. You can sto |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/5/TableCell/1388` | 0.441618 | Aeon stone, guiding U |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/5/TableCell/1348` | 0.440355 | Aeon stone, projecting U |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/2` | 0.426238 | From orbiting crystals imbued with power to gravity-defying equipment and hardlight devices, magic  items are popular accessories for adventurers and collectors. Engineers have developed fascinating |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/5/TableCell/1403` | 0.407270 | Aeon stone, navigating U |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/4` | 0.398002 | Technology and magic are everywhere in the galaxy.  While some magic equipment have gone unchanged for  thousands of years, the integration of technology to  improve the functionality or cost of many |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/5/TableCell/1248` | 0.385081 | Aeon stone, life givingU |

### Query 25
- Text: What is the rule about When you invest one of these precisely shaped crystals,  the stone orbits your head (or another visible part of your  anatomy if you don't have a head) instead of being worn on  your body. You can stow an *aeon stone* with an Interact action,  and an orbiting stone can be snatched out of the air with a  successful Disarm action against you. A stowed or removed  stone remains invested, but its effects are suppressed until  you return it to orbit your head again.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/2', 'PZO22001 Starfinder Player Core 282-293::/page/0/Text/9', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/3']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/2', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/3', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/1']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/3` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/1` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/2` | 0.988601 | When you invest one of these precisely shaped crystals,  the stone orbits your head (or another visible part of your  anatomy if you don't have a head) instead of being worn on  your body. You can sto |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/9` | 0.620098 | You invest your energy in an item with the invested trait  as you don it. This process requires 1 or more Interact  actions, usually taking the same amount of time it takes to  don the item. Once you' |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/3` | 0.545012 | There are various types of *aeon stones*, each with a  different appearance and magical effect. Each *aeon stone* also  gains a resonant power when slotted into specific items, such  as weapons with t |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/14` | 0.482614 | You can Activate an Item with the invested trait only if it's  invested by you. |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/2/Text/4` | 0.477336 | **Invested:** A PC can wear only 10 magical items that  have the invested trait. A character can still gain any  normal benefit from using a physical item without  investing it, such as using a *progr |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/8/Text/40` | 0.471402 | **Activate—Draw** [one-action] (manipulate) **Effect** You Interact to draw  an item concealed in your hideaway limb. |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/2/Text/39` | 0.446530 | You can Interact with the *null* *space* *chamber* to stow  items in it or remove them. The *null* *space* *chamber* can be  opened and closed only from the outside. When a *null* *space* *chamber* is |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/4/Text/6` | 0.441656 | **Activate—Inject** [one-action] (manipulate) **Effect** You Cast the Spell at  the indicated rank. |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/34` | 0.438328 | **Activate—Gravity Alteration** [one-action] (manipulate) **Effect** You treat  gravity as being one step higher or lower (for example,  zero-g becomes low gravity, low gravity becomes standard,  stan |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/10` | 0.437632 | You can invest no more than 10 items per day. If you  remove an invested item, it loses its investiture. The item still  counts against your daily limit after it loses its investiture.  You reset the |

### Query 26
- Text: What is the rule about There are various types of *aeon stones*, each with a  different appearance and magical effect. Each *aeon stone* also  gains a resonant power when slotted into specific items, such  as weapons with the aeon trait or antique magical devices  called *wayfinders*.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/3']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/3', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/2', 'PZO22001 Starfinder Player Core 282-293::/page/0/Text/4']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/3', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/2', 'PZO22001 Starfinder Player Core 282-293::/page/1/SectionHeader/4']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/2` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/1/SectionHeader/4` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/3` | 0.988044 | There are various types of *aeon stones*, each with a  different appearance and magical effect. Each *aeon stone* also  gains a resonant power when slotted into specific items, such  as weapons with t |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/2` | 0.582463 | When you invest one of these precisely shaped crystals,  the stone orbits your head (or another visible part of your  anatomy if you don't have a head) instead of being worn on  your body. You can sto |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/4` | 0.567532 | Technology and magic are everywhere in the galaxy.  While some magic equipment have gone unchanged for  thousands of years, the integration of technology to  improve the functionality or cost of many |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/5/TableCell/1388` | 0.501454 | Aeon stone, guiding U |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/1` | 0.500434 | these stones are purportedly all fragments of crystal tools  used by otherworldly entities to build the Universe in  ancient times. |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/2/Text/5` | 0.482408 | **Magical:** Items with the magical trait can be crafted  only if a player has the Magical Crafting feat (page 224). |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/5/TableCell/1403` | 0.481736 | Aeon stone, navigating U |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/2` | 0.475708 | From orbiting crystals imbued with power to gravity-defying equipment and hardlight devices, magic  items are popular accessories for adventurers and collectors. Engineers have developed fascinating |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/22` | 0.473746 | **AEON STONE** **ITEM 5+** |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/5/TableCell/1203` | 0.465044 | Aeon stone, uplifting U |

### Query 27
- Text: Summarize **Type **guiding; **Level **15; **Price **61,000 credits
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/SectionHeader/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/1/SectionHeader/4', 'PZO22001 Starfinder Player Core 282-293::/page/1/SectionHeader/10', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/27']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/SectionHeader/4', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/3', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/5']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/3` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/5` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/1/SectionHeader/4` | 1.039783 | **Type **guiding; **Level **15; **Price **61,000 credits |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/1/SectionHeader/10` | 0.777308 | **Type **navigating; **Level **16; **Price **95,000 credits |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/27` | 0.767082 | **Type **advanced; **Level **15; **Price **55,555 credits |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/3/Text/11` | 0.675729 | **Type **tactical; **Level **15; **Price **66,666 credits |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/3/Text/22` | 0.675272 | **Type **advanced; **Level **14; **Price **38,550 credits |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/7/Text/17` | 0.641413 | **Type **tactical; **Level **14; **Price **35,000 credits |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/3/Text/3` | 0.640012 | **Type **superior; **Level **13; **Price **24,000 credits; **Capacity** 150  Bulk |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/4/Text/52` | 0.622500 | **Type ***8th-rank spell gem*; **Level **15; **Price **13,000 credits |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/9/Text/13` | 0.620648 | **Type **advanced; **Level **12; **Price **16,000 credits Increase the item bonus to 15-feet. |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/8/Text/6` | 0.615211 | **Type **tactical; **Level **5; **Price **1,600 credits |

### Query 28
- Text: Summarize This gold star glitters with joyful energy. Its resonant power  allows you to cast *guidance* as an occult innate cantrip.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/5', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/11', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/15']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/5', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/6', 'PZO22001 Starfinder Player Core 282-293::/page/1/SectionHeader/4']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/6` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/1/SectionHeader/4` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/5` | 1.043237 | This gold star glitters with joyful energy. Its resonant power  allows you to cast *guidance* as an occult innate cantrip. |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/11` | 0.688203 | This deep purple helicoid prism guides your innate sense of  direction in even the emptiest reaches of space. You gain a  +2 item bonus to Piloting checks to Navigate. The resonant  power allows you t |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/15` | 0.610264 | The resonant power allows you to cast *mind skewer* as a  1st-rank occult innate spell once per day. |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/9` | 0.554486 | The resonant power allows you to cast *life* *seal* as a divine  innate spell once per day. |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/17` | 0.514911 | This deep-blue prism with cloudy inclusions is light as a  feather. Its resonant power gives you a +1 item bonus to  Acrobatics checks. |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/3` | 0.457723 | There are various types of *aeon stones*, each with a  different appearance and magical effect. Each *aeon stone* also  gains a resonant power when slotted into specific items, such  as weapons with t |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/44` | 0.447785 | This ostentatious crystal microphone is embellished with  glimmering jewels and delicate lights that pulse in time  to music. It functions as both a microphone and speaker,  amplifying your voice loud |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/4/Text/43` | 0.443753 | These latticed gemstones are suspended in a silicon casing  and encoded with the magical script necessary to cast  a single, specific spell. Casting a spell from a *spell gem* requires holding the gem |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/3/Text/26` | 0.433360 | **GRENADE** **MAGICAL** **TECH** |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/14` | 0.423971 | This opalescent sapphire cone grants you a limited form  of projected empathy with a range of 100 feet that can be  roughly understood by creatures regardless of language  and includes a type and inte |

### Query 29
- Text: What is the rule about **Activate—Cosmic Luck** [reaction] (concentrate, fortune) **Frequency** once per day; **Trigger** You critically fail an attack roll,  saving throw, or skill check; **Effect** You change the critical  failure into a failure.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/6', 'PZO22001 Starfinder Player Core 282-293::/page/10/Text/48', 'PZO22001 Starfinder Player Core 282-293::/page/11/Text/12']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/6', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/5', 'PZO22001 Starfinder Player Core 282-293::/page/1/SectionHeader/7']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/5` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/1/SectionHeader/7` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/6` | 0.945045 | **Activate—Cosmic Luck** [reaction] (concentrate, fortune) **Frequency** once per day; **Trigger** You critically fail an attack roll,  saving throw, or skill check; **Effect** You change the critical |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/10/Text/48` | 0.759707 | **Activate—Reground in Reality** [reaction] (concentrate, fortune)  **Frequency** once per hour; **Trigger** You fail a saving throw  against a magical effect; **Effect** You can reroll the save and |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/11/Text/12` | 0.661650 | **Activate—Irresistible Idea** [two-actions] (concentrate) **Frequency** once per hour; **Effect** You manipulate your cosmetics to  influence a creature as a 4th-rank *suggestion* (DC 38). |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/10/Text/22` | 0.591242 | **Activate—Regenerate** [two-actions] (concentrate) **Frequency** once  per day; **Effect** You gain the effects of a 4th-rank *genetic* *regeneration* spell. |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/11/Text/2` | 0.581149 | **Activate—Engage Hypernerves** [free-action] (concentrate) **Frequency** once per day; **Trigger** One of your reactions triggers, but  you have no remaining reactions to spend; **Effect** You gain |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/9/Text/30` | 0.574587 | **Activate—Cloak** [one-action] (concentrate) **Frequency** once per day;  **Effect** You gain the effects of 2nd-rank *invisibility* for  1 minute or until you spend an action, which has the  concent |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/10/Text/17` | 0.558175 | **Activate—Gaze** [two-actions] (concentrate, incapacitation, mental,  visual) As commercial, but increase the DC to 20 and the  creature becomes helpful on a critical failure. |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/10/Text/12` | 0.554963 | **Activate—Gaze** [two-actions] (concentrate, mental, visual) **Frequency** once per day; **Effect** You focus your eyes on a creature that  can see you within 30 feet. The creature attempts a DC 17 |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/3/Text/9` | 0.552304 | **Activate—Painful Memory** [two-actions] (manipulate) **Frequency** once per day; **Effect** You recite a poem of utter anguish  to spread your misery to another creature, casting a 3rdrank *share* * |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/4/Text/6` | 0.544362 | **Activate—Inject** [one-action] (manipulate) **Effect** You Cast the Spell at  the indicated rank. |

### Query 30
- Text: Summarize **Type **life-giving; **Level **7; **Price **3,500 credits
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/SectionHeader/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/1/SectionHeader/7', 'PZO22001 Starfinder Player Core 282-293::/page/6/Text/22', 'PZO22001 Starfinder Player Core 282-293::/page/8/Text/23']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/SectionHeader/7', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/8', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/6']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/8` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/6` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/1/SectionHeader/7` | 1.041527 | **Type **life-giving; **Level **7; **Price **3,500 credits |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/6/Text/22` | 0.748542 | **Type **advanced; **Level **7; **Price **3,300 credits |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/8/Text/23` | 0.741748 | **Type **advanced; **Level **7; **Price **3,240 credits |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/7/Text/28` | 0.631726 | **Type **advanced; **Level **9; **Price **7,000 credits |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/3/Text/10` | 0.621633 | **Type **commercial; **Level **7; **Price **3,333 credits |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/8/Text/15` | 0.597281 | **Type **advanced; **Level **8; **Price **4,200 credits |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/10/Text/20` | 0.590015 | **Price **6,500 credits |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/1/SectionHeader/16` | 0.589681 | **Type **uplifting; **Level **5; **Price **1,600 credits |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/7/Text/16` | 0.581756 | **Type **commercial; **Level **8; **Price **3,450 credits |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/4/Text/32` | 0.580893 | **Type ***3rd-rank spell chip*; **Level **7; **Price **3,600 credits |

### Query 31
- Text: What is the rule about This nacreous, tapered cylinder provides a breath of air  when you need it most. You can hold your breath for twice  as long, and you gain a +1 item bonus to saves against  inhaled poisons.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/8']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/8', 'PZO22001 Starfinder Player Core 282-293::/page/10/Text/36', 'PZO22001 Starfinder Player Core 282-293::/page/2/Text/39']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/8', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/9', 'PZO22001 Starfinder Player Core 282-293::/page/1/SectionHeader/7']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/9` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/1/SectionHeader/7` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/8` | 0.977823 | This nacreous, tapered cylinder provides a breath of air  when you need it most. You can hold your breath for twice  as long, and you gain a +1 item bonus to saves against  inhaled poisons. |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/10/Text/36` | 0.478958 | This extra organ assimilates with and enhances your circulatory  and immune systems. When you succeed at a Fortitude save  against an ongoing disease or poison, you recover completely,  regardless of |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/2/Text/39` | 0.469715 | You can Interact with the *null* *space* *chamber* to stow  items in it or remove them. The *null* *space* *chamber* can be  opened and closed only from the outside. When a *null* *space* *chamber* is |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/7/Text/15` | 0.427226 | Your skin is biologically engineered to protect your entire  body, including your brain, from harmful effects. You gain a  +1 item bonus to saving throws. |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/6/Text/31` | 0.415383 | Oxygen-filtering nodules line the outside of your lungs. If you  breathe in water, the gill sheath filters the oxygen into your  lungs. This allows you to breathe underwater or in the air.  You exhale |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/6/Text/18` | 0.413548 | With cutting edge surgery, you're implanted with an  magical gland modified to function for a creature of your  ancestry at the back of your throat. Choose your breath  weapon's damage type when the o |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/2/Text/3` | 0.407447 | **Consumable:** Items with the consumable trait can  be used only once. Most manufacturers design these  items so the container, syringe, or other remaining  materials can't be easily reused to protec |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/6/Text/19` | 0.390167 | **Activate—Exhale** [one-action] (manipulate) **Frequency** once per  10 minutes; **Effect** Each creature in a 15-foot cone takes  damage with a basic Reflex save. The damage depends on the  augmenta |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/10/Text/37` | 0.385995 | **Activate—Life Buffer **[one-action] (manipulate) **Frequency** once per day;  **Effect** You gain 50 temporary Hit Points, which last for 1 hour. |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/3/Text/1` | 0.384742 | 10 minutes' worth of air for every Bulk left in its capacity.  An item inside the *null* *space* *chamber* provides no benefits  unless it's retrieved first. Connecting the *null space chamber* to a c |

### Query 32
- Text: What is the rule about The resonant power allows you to cast *life* *seal* as a divine  innate spell once per day.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/9', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/15', 'PZO22001 Starfinder Player Core 282-293::/page/4/Text/29']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/9', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/8', 'PZO22001 Starfinder Player Core 282-293::/page/1/SectionHeader/10']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/8` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/1/SectionHeader/10` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/9` | 0.985282 | The resonant power allows you to cast *life* *seal* as a divine  innate spell once per day. |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/15` | 0.729156 | The resonant power allows you to cast *mind skewer* as a  1st-rank occult innate spell once per day. |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/4/Text/29` | 0.592192 | **Activate **Cast a Spell; **Frequency** once per day, plus  overclock; **Effect** You Cast the Spell at the indicated  rank. |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/5` | 0.491826 | This gold star glitters with joyful energy. Its resonant power  allows you to cast *guidance* as an occult innate cantrip. |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/10/Text/22` | 0.480057 | **Activate—Regenerate** [two-actions] (concentrate) **Frequency** once  per day; **Effect** You gain the effects of a 4th-rank *genetic* *regeneration* spell. |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/4/Text/43` | 0.468086 | These latticed gemstones are suspended in a silicon casing  and encoded with the magical script necessary to cast  a single, specific spell. Casting a spell from a *spell gem* requires holding the gem |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/4/Text/44` | 0.441744 | **Activate **Cast a Spell; **Effect** You Cast the Spell at the  indicated rank. |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/4/Text/28` | 0.438299 | Attempting to use a *spell chip* more than once per day  requires overclocking it. Cast the Spell again, then roll  a DC 10 flat check. On a success, the *spell chip* is broken.  On a failure, the *sp |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/20` | 0.419003 | If the activation entry for an item lists "Cast a Spell" after  "Activate", you must use the same action as casting the spell  to Activate the Item, unless noted otherwise. You must have  a spellcasti |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/18` | 0.414556 | Some items can be activated only a certain number of times  per day, resetting during your daily preparations. You retain  the constant benefits of these items even when the activation  requirements o |

### Query 33
- Text: Summarize **Type **navigating; **Level **16; **Price **95,000 credits
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/SectionHeader/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/1/SectionHeader/10', 'PZO22001 Starfinder Player Core 282-293::/page/1/SectionHeader/4', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/27']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/SectionHeader/10', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/11', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/9']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/11` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/9` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/1/SectionHeader/10` | 1.039680 | **Type **navigating; **Level **16; **Price **95,000 credits |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/1/SectionHeader/4` | 0.778847 | **Type **guiding; **Level **15; **Price **61,000 credits |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/27` | 0.686592 | **Type **advanced; **Level **15; **Price **55,555 credits |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/38` | 0.640869 | **Type **advanced; **Level **18; **Price **220,600 credits |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/3/Text/22` | 0.633492 | **Type **advanced; **Level **14; **Price **38,550 credits |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/7/Text/19` | 0.629420 | **Type **advanced; **Level **20; **Price **495,000 credits |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/7/Text/28` | 0.626408 | **Type **advanced; **Level **9; **Price **7,000 credits |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/2/Text/12` | 0.624577 | **Type **advanced; **Level **18; **Price **190,400 credits |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/8/Text/25` | 0.597095 | **Type **superior; **Level **10; **Price **9,000 credits |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/3/Text/3` | 0.591273 | **Type **superior; **Level **13; **Price **24,000 credits; **Capacity** 150  Bulk |

### Query 34
- Text: What is the rule about This deep purple helicoid prism guides your innate sense of  direction in even the emptiest reaches of space. You gain a  +2 item bonus to Piloting checks to Navigate. The resonant  power allows you to cast *seek* *the* *stars* as a divine innate  cantrip.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/11', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/5', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/17']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/11', 'PZO22001 Starfinder Player Core 282-293::/page/1/SectionHeader/10', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/12']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/1/SectionHeader/10` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/12` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/11` | 0.994068 | This deep purple helicoid prism guides your innate sense of  direction in even the emptiest reaches of space. You gain a  +2 item bonus to Piloting checks to Navigate. The resonant  power allows you t |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/5` | 0.680625 | This gold star glitters with joyful energy. Its resonant power  allows you to cast *guidance* as an occult innate cantrip. |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/17` | 0.625612 | This deep-blue prism with cloudy inclusions is light as a  feather. Its resonant power gives you a +1 item bonus to  Acrobatics checks. |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/9` | 0.479843 | The resonant power allows you to cast *life* *seal* as a divine  innate spell once per day. |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/15` | 0.466249 | The resonant power allows you to cast *mind skewer* as a  1st-rank occult innate spell once per day. |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/12` | 0.456273 | **Activate—Navigate** [one-action] (concentrate) **Frequency** once per day;  **Effect** You concentrate on a Drift beacon you've visited  before and mentally chart a course for that location. You  im |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/10/Text/47` | 0.443710 | This augmentation opens your mind to the underlying cosmic  truths of the universe. When you get this augmentation, you  either increase your Wisdom modifier by 1 or increase it to  +4, whichever woul |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/9/Text/29` | 0.414322 | Many of your pores are replaced with magically regulated  and directed holographic projectors that synchronize  when activated to automatically match your surroundings,  rendering you invisible. |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/2/Text/4` | 0.408470 | **Invested:** A PC can wear only 10 magical items that  have the invested trait. A character can still gain any  normal benefit from using a physical item without  investing it, such as using a *progr |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/23` | 0.407606 | Worn as a contact lens, spectacles, or other eyewear, these  magically treated lenses project a special data display that  uses virtual intelligence and rapid eye tracking to quickly  cycle through in |

### Query 35
- Text: What is the rule about **Activate—Navigate** [one-action] (concentrate) **Frequency** once per day;  **Effect** You concentrate on a Drift beacon you've visited  before and mentally chart a course for that location. You  immediately know which direction to travel to reach your  destination, and your journey takes 1 day less if you're  piloting the ship.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/12']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/12', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/18', 'PZO22001 Starfinder Player Core 282-293::/page/9/Text/30']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/12', 'PZO22001 Starfinder Player Core 282-293::/page/1/SectionHeader/13', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/11']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/1/SectionHeader/13` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/11` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/12` | 0.966563 | **Activate—Navigate** [one-action] (concentrate) **Frequency** once per day;  **Effect** You concentrate on a Drift beacon you've visited  before and mentally chart a course for that location. You  im |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/18` | 0.659912 | **Activate—Fly Free** [two-actions] (concentrate) **Frequency** once per  day; **Effect** You gain a fly Speed for 1 minute equal to your  Speed or 20 feet, whichever is greater. |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/9/Text/30` | 0.645384 | **Activate—Cloak** [one-action] (concentrate) **Frequency** once per day;  **Effect** You gain the effects of 2nd-rank *invisibility* for  1 minute or until you spend an action, which has the  concent |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/11/Text/12` | 0.600545 | **Activate—Irresistible Idea** [two-actions] (concentrate) **Frequency** once per hour; **Effect** You manipulate your cosmetics to  influence a creature as a 4th-rank *suggestion* (DC 38). |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/10/Text/48` | 0.586040 | **Activate—Reground in Reality** [reaction] (concentrate, fortune)  **Frequency** once per hour; **Trigger** You fail a saving throw  against a magical effect; **Effect** You can reroll the save and |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/10/Text/42` | 0.584663 | **Activate—Access Database** [one-action] (concentrate) **Frequency** once  per hour; **Effect** Immediately attempt three checks to  Recall Knowledge about related topics, selecting each topic  after |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/11/Text/2` | 0.580677 | **Activate—Engage Hypernerves** [free-action] (concentrate) **Frequency** once per day; **Trigger** One of your reactions triggers, but  you have no remaining reactions to spend; **Effect** You gain |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/10/Text/12` | 0.576697 | **Activate—Gaze** [two-actions] (concentrate, mental, visual) **Frequency** once per day; **Effect** You focus your eyes on a creature that  can see you within 30 feet. The creature attempts a DC 17 |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/7/Text/59` | 0.559996 | **Activate—Accelerate** [free-action] **Frequency** once per 10 minutes;  **Trigger** You Climb, Stride, or Swim; **Effect** You increase  your Speed by 20 feet for the triggering action. |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/6` | 0.555899 | **Activate—Cosmic Luck** [reaction] (concentrate, fortune) **Frequency** once per day; **Trigger** You critically fail an attack roll,  saving throw, or skill check; **Effect** You change the critical |

### Query 36
- Text: Summarize **Type **projecting; **Level **13; **Price **22,000 credits
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/SectionHeader/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/1/SectionHeader/13', 'PZO22001 Starfinder Player Core 282-293::/page/7/Text/30', 'PZO22001 Starfinder Player Core 282-293::/page/9/Text/34']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/SectionHeader/13', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/14', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/12']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/14` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/12` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/1/SectionHeader/13` | 1.038201 | **Type **projecting; **Level **13; **Price **22,000 credits |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/7/Text/30` | 0.769548 | **Type **superior; **Level **12; **Price **20,000 credits |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/9/Text/34` | 0.760698 | **Type **advanced; **Level **12; **Price **20,000 credits |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/8/Text/47` | 0.679348 | **Price **12,000 credits |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/3/Text/3` | 0.656666 | **Type **superior; **Level **13; **Price **24,000 credits; **Capacity** 150  Bulk |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/3/Text/22` | 0.656137 | **Type **advanced; **Level **14; **Price **38,550 credits |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/36` | 0.650990 | **Type **tactical; **Level **12; **Price **16,500 credits |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/7/Text/47` | 0.648160 | **Price **13,000 credits |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/38` | 0.628297 | **Type **advanced; **Level **18; **Price **220,600 credits |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/7/Text/19` | 0.622330 | **Type **advanced; **Level **20; **Price **495,000 credits |

### Query 37
- Text: What is the rule about This opalescent sapphire cone grants you a limited form  of projected empathy with a range of 100 feet that can be  roughly understood by creatures regardless of language  and includes a type and intensity of emotion, such as "mild  anger," "intense joy," or "deep sadness." When you Sense the  Motive of a creature within 30 feet, you detect the presence  or absence of thoughts from the creature as though you cast  the 1-action version of *detect* *thoughts*.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/14']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/14', 'PZO22001 Starfinder Player Core 282-293::/page/6/Text/19', 'PZO22001 Starfinder Player Core 282-293::/page/10/Text/12']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/14', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/15', 'PZO22001 Starfinder Player Core 282-293::/page/1/SectionHeader/13']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/15` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/1/SectionHeader/13` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/14` | 0.995945 | This opalescent sapphire cone grants you a limited form  of projected empathy with a range of 100 feet that can be  roughly understood by creatures regardless of language  and includes a type and inte |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/6/Text/19` | 0.562779 | **Activate—Exhale** [one-action] (manipulate) **Frequency** once per  10 minutes; **Effect** Each creature in a 15-foot cone takes  damage with a basic Reflex save. The damage depends on the  augmenta |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/10/Text/12` | 0.550490 | **Activate—Gaze** [two-actions] (concentrate, mental, visual) **Frequency** once per day; **Effect** You focus your eyes on a creature that  can see you within 30 feet. The creature attempts a DC 17 |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/10/Text/15` | 0.481303 | **Critical Failure** The creature is fascinated for as long as it  can see you. Taking a hostile action against the creature  ends the effect. |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/10/Text/27` | 0.467136 | A rune-carved device of treated alloys and crystal the size of  a pebble is implanted into your brain's communication center.  You gain limited telepathy (page 58) to a range of 30 feet. |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/3/Text/9` | 0.448379 | **Activate—Painful Memory** [two-actions] (manipulate) **Frequency** once per day; **Effect** You recite a poem of utter anguish  to spread your misery to another creature, casting a 3rdrank *share* * |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/7/Text/41` | 0.443703 | This soft purple fungus attaches to your vocal cords  and extends fine filaments into portions of your brain.  You can ask questions of, receive answers from, and use  the Diplomacy skill with animals |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/4/Text/15` | 0.437799 | **Type ***feline* *senses spell amp*; **Level **7; **Price **530 credits;  **Effect** 3rd-rank *feline* *senses* spell |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/9` | 0.424009 | You invest your energy in an item with the invested trait  as you don it. This process requires 1 or more Interact  actions, usually taking the same amount of time it takes to  don the item. Once you' |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/11/Text/7` | 0.412163 | **Activate—Strength of the Colossi** [one-action] (manipulate) **Frequency** once per day; **Effect** You temporarily become as destructive  and powerful as a colossus. For 1 hour, your melee Strikes |

### Query 38
- Text: What is the rule about The resonant power allows you to cast *mind skewer* as a  1st-rank occult innate spell once per day.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/15']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/15', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/9', 'PZO22001 Starfinder Player Core 282-293::/page/4/Text/29']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/15', 'PZO22001 Starfinder Player Core 282-293::/page/1/SectionHeader/16', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/14']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/1/SectionHeader/16` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/14` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/15` | 0.982549 | The resonant power allows you to cast *mind skewer* as a  1st-rank occult innate spell once per day. |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/9` | 0.729968 | The resonant power allows you to cast *life* *seal* as a divine  innate spell once per day. |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/4/Text/29` | 0.586101 | **Activate **Cast a Spell; **Frequency** once per day, plus  overclock; **Effect** You Cast the Spell at the indicated  rank. |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/5` | 0.501024 | This gold star glitters with joyful energy. Its resonant power  allows you to cast *guidance* as an occult innate cantrip. |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/10/Text/22` | 0.446485 | **Activate—Regenerate** [two-actions] (concentrate) **Frequency** once  per day; **Effect** You gain the effects of a 4th-rank *genetic* *regeneration* spell. |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/4/Text/28` | 0.434469 | Attempting to use a *spell chip* more than once per day  requires overclocking it. Cast the Spell again, then roll  a DC 10 flat check. On a success, the *spell chip* is broken.  On a failure, the *sp |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/4/Text/43` | 0.431090 | These latticed gemstones are suspended in a silicon casing  and encoded with the magical script necessary to cast  a single, specific spell. Casting a spell from a *spell gem* requires holding the gem |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/4/Text/44` | 0.421121 | **Activate **Cast a Spell; **Effect** You Cast the Spell at the  indicated rank. |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/4/TableCell/841` | 0.419088 | 1st-rank spell gem |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/5/TableCell/1143` | 0.411417 | 1st-rank spell chip |

### Query 39
- Text: Summarize **Type **uplifting; **Level **5; **Price **1,600 credits
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/SectionHeader/16']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/1/SectionHeader/16', 'PZO22001 Starfinder Player Core 282-293::/page/8/Text/6', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/27']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/SectionHeader/16', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/15', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/17']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/15` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/17` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/1/SectionHeader/16` | 1.041854 | **Type **uplifting; **Level **5; **Price **1,600 credits |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/8/Text/6` | 0.735789 | **Type **tactical; **Level **5; **Price **1,600 credits |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/27` | 0.699512 | **Type **advanced; **Level **15; **Price **55,555 credits |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/8/Text/42` | 0.642328 | **Type **tactical; **Level **5; **Price **1,400 credits |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/38` | 0.633662 | **Type **advanced; **Level **18; **Price **220,600 credits |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/8/Text/5` | 0.626617 | **Type **commercial; **Level **3; **Price **600 credits |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/35` | 0.619030 | **Type **commercial; **Level **6; **Price **2,100 credits |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/8/Text/15` | 0.618215 | **Type **advanced; **Level **8; **Price **4,200 credits |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/2/Text/27` | 0.617979 | **Type **commercial; **Level **0; **Price **5 credits; **Upgrades** 1 |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/6/Text/22` | 0.617870 | **Type **advanced; **Level **7; **Price **3,300 credits |

### Query 40
- Text: What is the rule about This deep-blue prism with cloudy inclusions is light as a  feather. Its resonant power gives you a +1 item bonus to  Acrobatics checks.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/17']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/17', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/11', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/5']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/17', 'PZO22001 Starfinder Player Core 282-293::/page/1/SectionHeader/16', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/18']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/1/SectionHeader/16` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/18` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/17` | 0.987943 | This deep-blue prism with cloudy inclusions is light as a  feather. Its resonant power gives you a +1 item bonus to  Acrobatics checks. |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/11` | 0.594958 | This deep purple helicoid prism guides your innate sense of  direction in even the emptiest reaches of space. You gain a  +2 item bonus to Piloting checks to Navigate. The resonant  power allows you t |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/5` | 0.536452 | This gold star glitters with joyful energy. Its resonant power  allows you to cast *guidance* as an occult innate cantrip. |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/33` | 0.471813 | This convoluted web of synthweave straps is worn as a  fashion statement in some subcultures but has a useful  application in extreme environments. You gain a +1 item  bonus to Acrobatics checks, and |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/11/Text/1` | 0.466337 | This augmentation enhances your muscles and nervous system  to dramatically improve your flexibility and reaction time. You  gain a +3 item bonus to Acrobatics checks. When you get this  augmentation, |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/5/Table/1` | 0.429465 | ItemLevelPriceBulkHandsGlow up spell amp,commercial150L1Reusable grenade shell18011Hardlight handwraps, tactical2355——Jump spell amp260L11st-rank spell chip3600——2nd-rank spell gem3120——Akashic lens, |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/11/Text/6` | 0.412368 | This augmentation keeps your muscles in peak condition. You  gain a +3 item bonus to Athletics checks. When you get this  augmentation, you either increase your Strength modifier by 1  or increase it |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/5/Table/2` | 0.411876 | ItemLevelPriceBulkHandsGlow up spell amp, advanced91,100L1Diva's microphone, tactical109,500L1Hardlight handwraps, superior1010,005——Resist energy spell amp, tactical101,800L15th-rank spell chip1115,0 |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/8/Text/39` | 0.407432 | When the compartment is closed, the seam in your limb is  difficult to detect. You gain a +1 item bonus to Stealth checks to  Conceal an Object in a hideaway limb. Though this compartment  can foil a |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/14` | 0.407153 | This opalescent sapphire cone grants you a limited form  of projected empathy with a range of 100 feet that can be  roughly understood by creatures regardless of language  and includes a type and inte |

### Query 41
- Text: What is the rule about **Activate—Fly Free** [two-actions] (concentrate) **Frequency** once per  day; **Effect** You gain a fly Speed for 1 minute equal to your  Speed or 20 feet, whichever is greater.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/18']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/18', 'PZO22001 Starfinder Player Core 282-293::/page/7/Text/59', 'PZO22001 Starfinder Player Core 282-293::/page/11/Text/12']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/18', 'PZO22001 Starfinder Player Core 282-293::/page/1/SectionHeader/19', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/17']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/1/SectionHeader/19` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/17` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/18` | 0.950262 | **Activate—Fly Free** [two-actions] (concentrate) **Frequency** once per  day; **Effect** You gain a fly Speed for 1 minute equal to your  Speed or 20 feet, whichever is greater. |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/7/Text/59` | 0.738451 | **Activate—Accelerate** [free-action] **Frequency** once per 10 minutes;  **Trigger** You Climb, Stride, or Swim; **Effect** You increase  your Speed by 20 feet for the triggering action. |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/11/Text/12` | 0.675712 | **Activate—Irresistible Idea** [two-actions] (concentrate) **Frequency** once per hour; **Effect** You manipulate your cosmetics to  influence a creature as a 4th-rank *suggestion* (DC 38). |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/12` | 0.616605 | **Activate—Navigate** [one-action] (concentrate) **Frequency** once per day;  **Effect** You concentrate on a Drift beacon you've visited  before and mentally chart a course for that location. You  im |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/10/Text/22` | 0.603411 | **Activate—Regenerate** [two-actions] (concentrate) **Frequency** once  per day; **Effect** You gain the effects of a 4th-rank *genetic* *regeneration* spell. |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/11/Text/2` | 0.602926 | **Activate—Engage Hypernerves** [free-action] (concentrate) **Frequency** once per day; **Trigger** One of your reactions triggers, but  you have no remaining reactions to spend; **Effect** You gain |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/9/Text/30` | 0.580423 | **Activate—Cloak** [one-action] (concentrate) **Frequency** once per day;  **Effect** You gain the effects of 2nd-rank *invisibility* for  1 minute or until you spend an action, which has the  concent |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/10/Text/48` | 0.580420 | **Activate—Reground in Reality** [reaction] (concentrate, fortune)  **Frequency** once per hour; **Trigger** You fail a saving throw  against a magical effect; **Effect** You can reroll the save and |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/10/Text/37` | 0.574379 | **Activate—Life Buffer **[one-action] (manipulate) **Frequency** once per day;  **Effect** You gain 50 temporary Hit Points, which last for 1 hour. |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/10/Text/12` | 0.558038 | **Activate—Gaze** [two-actions] (concentrate, mental, visual) **Frequency** once per day; **Effect** You focus your eyes on a creature that  can see you within 30 feet. The creature attempts a DC 17 |

### Query 42
- Text: Summarize **AKASHIC LENS** **ITEM 3+**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/SectionHeader/19']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/1/SectionHeader/19', 'PZO22001 Starfinder Player Core 282-293::/page/5/TableCell/1393', 'PZO22001 Starfinder Player Core 282-293::/page/5/TableCell/1153']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/SectionHeader/19', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/18', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/21']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/18` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/21` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/1/SectionHeader/19` | 1.023756 | **AKASHIC LENS** **ITEM 3+** |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/5/TableCell/1393` | 0.666025 | Akashic lens, advanced |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/5/TableCell/1153` | 0.627514 | Akashic lens, commercial |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/5/TableCell/1283` | 0.578874 | Akashic lens, tactical |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/24` | 0.477938 | **Activate—Database Scan** [two-actions] (concentrate) **Frequency** once  per 10 minutes; **Effect** The lens casts a 1st-rank *Akashic* *download* that uses the lens instead of a comm unit. |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/28` | 0.474664 | The item bonus is +2, and the *Akashic* *download* spell is 4th  rank. |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/26` | 0.471309 | **Type **tactical; **Level **9; **Price **5,555 credits The *Akashic* *download* spell is 3rd rank. |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/10/SectionHeader/7` | 0.449439 | **PSYCHOACTIVE EYES** **AUGMENTATION 3+** |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/8/SectionHeader/1` | 0.420873 | **DARKVISION CAPACITORS** **AUGMENTATION 3+** |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/7/SectionHeader/21` | 0.419299 | **ULTRALIGHT WINGS** **AUGMENTATION 3+** |

### Query 43
- Text: Summarize **INVESTED** **MAGICAL** **TECH**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/21']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/21', 'PZO22001 Starfinder Player Core 282-293::/page/3/Text/15', 'PZO22001 Starfinder Player Core 282-293::/page/2/Text/16']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/21', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/22', 'PZO22001 Starfinder Player Core 282-293::/page/1/SectionHeader/19']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/22` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/1/SectionHeader/19` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/21` | 1.002080 | **INVESTED** **MAGICAL** **TECH** |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/3/Text/15` | 1.002080 | **INVESTED** **MAGICAL** **TECH** |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/2/Text/16` | 1.002080 | **INVESTED** **MAGICAL** **TECH** |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/42` | 0.960080 | **INVESTED** **MAGICAL** **TECH** |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/31` | 0.960080 | **INVESTED** **MAGICAL** **TECH** |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/3/Text/6` | 0.960080 | **INVESTED** **MAGICAL** **TECH** |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/2/Text/23` | 0.960080 | **INVESTED** **MAGICAL** **TECH** |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/4/SectionHeader/24` | 0.784007 | **MAGICAL** **TECH** |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/24` | 0.773278 | **UNCOMMON** **INVESTED** **MAGICAL** |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/10/Text/25` | 0.685266 | **MAGICAL** **MAGITECH** |

### Query 44
- Text: Summarize **Usage** worn eyepiece; **Bulk **—
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/22']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/22', 'PZO22001 Starfinder Player Core 282-293::/page/2/Text/37', 'PZO22001 Starfinder Player Core 282-293::/page/0/Text/25']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/22', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/23', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/21']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/23` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/21` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/22` | 1.027695 | **Usage** worn eyepiece; **Bulk **— |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/2/Text/37` | 0.829399 | **Usage** worn; **Bulk **— |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/25` | 0.829399 | **Usage** worn; **Bulk **— |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/32` | 0.734230 | **Usage** worn garment; **Bulk **1 |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/2/Text/24` | 0.701288 | **Usage** worn gloves; **Bulk **— |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/2/Text/18` | 0.633281 | **Usage** worn armbands or gloves; **Bulk **L |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/4/SectionHeader/25` | 0.613975 | **Usage** installed in computer or comm unit; **Bulk **– |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/3/Text/28` | 0.599702 | **Usage** held in 1 hand; **Bulk **1 |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/4/SectionHeader/4` | 0.580852 | **Usage** held in 1 hand; **Bulk **L |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/43` | 0.580852 | **Usage** held in 1 hand; **Bulk **L |

### Query 45
- Text: What is the rule about Worn as a contact lens, spectacles, or other eyewear, these  magically treated lenses project a special data display that  uses virtual intelligence and rapid eye tracking to quickly  cycle through information until you find what you seek. It  grants you a +1 item bonus to Recall Knowledge checks with  the skill chosen when you use Database Scan.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/23']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/23', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/24', 'PZO22001 Starfinder Player Core 282-293::/page/7/Text/53']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/23', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/22', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/24']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/22` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/24` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/23` | 0.984119 | Worn as a contact lens, spectacles, or other eyewear, these  magically treated lenses project a special data display that  uses virtual intelligence and rapid eye tracking to quickly  cycle through in |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/24` | 0.598078 | **Activate—Database Scan** [two-actions] (concentrate) **Frequency** once  per 10 minutes; **Effect** The lens casts a 1st-rank *Akashic* *download* that uses the lens instead of a comm unit. |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/7/Text/53` | 0.591191 | An artificial eye lens microscopically wired into your  brain automatically tracks a database of associated  names and faces as you meet or interact with individuals.  After you've learned someone's n |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/2/Text/19` | 0.505136 | This magitech interface is a sophisticated pair of linked  bracers, wristbands, gloves, or other garments suitable to  the part of a creature's anatomy it uses to wield weapons.  One of the paired enh |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/10/Text/41` | 0.458103 | A miniature supercomputer augments your brain's ability  to process information. You gain a +3 item bonus to checks  to Recall Knowledge with any skill. When you get this  augmentation, you either inc |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/10/Text/42` | 0.441076 | **Activate—Access Database** [one-action] (concentrate) **Frequency** once  per hour; **Effect** Immediately attempt three checks to  Recall Knowledge about related topics, selecting each topic  after |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/9/Text/6` | 0.438541 | These sheets of reflective material, implanted in your  visual organs, enhance your vision without changing your  appearance. You gain low-light vision and a +1 item bonus to  Perception checks to See |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/10/Text/10` | 0.428070 | Your irises are injected with psychoactive dyes that cause  a signature kaleidoscopic effect, or your eyes have been  completely replaced with delicate magitech devices. You  can activate these dyes t |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/22` | 0.427307 | **Usage** worn eyepiece; **Bulk **— |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/8/Text/7` | 0.426424 | These upgraded capacitors include a wide-spectrum ocular  implant that allows you to see infrared and ultraviolet light,  including the lasers from other darkvision capacitors. You  gain darkvision an |

### Query 46
- Text: What is the rule about **Activate—Database Scan** [two-actions] (concentrate) **Frequency** once  per 10 minutes; **Effect** The lens casts a 1st-rank *Akashic* *download* that uses the lens instead of a comm unit.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/24']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/24', 'PZO22001 Starfinder Player Core 282-293::/page/10/Text/42', 'PZO22001 Starfinder Player Core 282-293::/page/9/Text/30']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/24', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/23', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/25']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/23` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/25` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/24` | 0.945405 | **Activate—Database Scan** [two-actions] (concentrate) **Frequency** once  per 10 minutes; **Effect** The lens casts a 1st-rank *Akashic* *download* that uses the lens instead of a comm unit. |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/10/Text/42` | 0.664623 | **Activate—Access Database** [one-action] (concentrate) **Frequency** once  per hour; **Effect** Immediately attempt three checks to  Recall Knowledge about related topics, selecting each topic  after |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/9/Text/30` | 0.628085 | **Activate—Cloak** [one-action] (concentrate) **Frequency** once per day;  **Effect** You gain the effects of 2nd-rank *invisibility* for  1 minute or until you spend an action, which has the  concent |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/11/Text/12` | 0.584031 | **Activate—Irresistible Idea** [two-actions] (concentrate) **Frequency** once per hour; **Effect** You manipulate your cosmetics to  influence a creature as a 4th-rank *suggestion* (DC 38). |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/10/Text/22` | 0.546397 | **Activate—Regenerate** [two-actions] (concentrate) **Frequency** once  per day; **Effect** You gain the effects of a 4th-rank *genetic* *regeneration* spell. |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/3/Text/9` | 0.545910 | **Activate—Painful Memory** [two-actions] (manipulate) **Frequency** once per day; **Effect** You recite a poem of utter anguish  to spread your misery to another creature, casting a 3rdrank *share* * |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/12` | 0.544608 | **Activate—Navigate** [one-action] (concentrate) **Frequency** once per day;  **Effect** You concentrate on a Drift beacon you've visited  before and mentally chart a course for that location. You  im |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/4/Text/6` | 0.539099 | **Activate—Inject** [one-action] (manipulate) **Effect** You Cast the Spell at  the indicated rank. |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/10/Text/48` | 0.538906 | **Activate—Reground in Reality** [reaction] (concentrate, fortune)  **Frequency** once per hour; **Trigger** You fail a saving throw  against a magical effect; **Effect** You can reroll the save and |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/2/Text/8` | 0.537031 | **Activate—Grand Finale** [two-actions] (auditory) **Frequency** once per  10 minutes; **Effect** Your song reaches an eardrum-bursting  climax as you cast a 1st-rank *sonic* *scream* originating  fro |

### Query 47
- Text: Summarize **Type **commercial; **Level **3; **Price **555 credits
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/25']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/25', 'PZO22001 Starfinder Player Core 282-293::/page/3/Text/19', 'PZO22001 Starfinder Player Core 282-293::/page/8/Text/5']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/25', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/24', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/26']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/24` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/26` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/25` | 1.038060 | **Type **commercial; **Level **3; **Price **555 credits |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/3/Text/19` | 0.987602 | **Type **commercial; **Level **3; **Price **550 credits |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/8/Text/5` | 0.923426 | **Type **commercial; **Level **3; **Price **600 credits |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/7/Text/25` | 0.881426 | **Type **commercial; **Level **3; **Price **600 credits |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/10/Text/11` | 0.853837 | **Type **commercial;** Level **3; **Price **500 credits |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/9/Text/31` | 0.849350 | **Type **commercial; **Level **8; **Price **5,000 credits |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/3/Text/10` | 0.841281 | **Type **commercial; **Level **7; **Price **3,333 credits |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/8/Text/21` | 0.839333 | **Type **commercial; **Level **1; **Price **180 credits |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/2/Text/9` | 0.839315 | **Type **commercial; **Level **4; **Price **750 credits |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/7/Text/16` | 0.834789 | **Type **commercial; **Level **8; **Price **3,450 credits |

### Query 48
- Text: What is the rule about **Type **tactical; **Level **9; **Price **5,555 credits The *Akashic* *download* spell is 3rd rank.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/26']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/26', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/28', 'PZO22001 Starfinder Player Core 282-293::/page/4/Text/20']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/26', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/25', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/27']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/25` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/27` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/26` | 0.961178 | **Type **tactical; **Level **9; **Price **5,555 credits The *Akashic* *download* spell is 3rd rank. |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/28` | 0.755960 | The item bonus is +2, and the *Akashic* *download* spell is 4th  rank. |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/4/Text/20` | 0.644248 | **Type ***tactical* *cairn* *form* *spell* *amp*; **Level **11; **Price **3,200  credits; **Effect** 6th-rank *cairn* *form* spell |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/4/Text/19` | 0.586158 | **Type ***tactical* *resist* *energy* *spell* *amp*; **Level **10; **Price **1,800  credits; **Effect** 4th-rank *resist energy* spell |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/4/Text/12` | 0.580450 | **Type ***tactical* *glow* *up* *spell* *amp*; **Level **5; **Price **210 credits;  **Effect** 3rd-rank *glow* *up* spell |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/2/Text/10` | 0.580287 | **Type **tactical; **Level **10; **Price **9,500 credits |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/3/Text/20` | 0.578111 | **Type **tactical; **Level **8; **Price **4,550 credits |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/3/Text/11` | 0.567787 | **Type **tactical; **Level **15; **Price **66,666 credits |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/8/Text/42` | 0.566696 | **Type **tactical; **Level **5; **Price **1,400 credits |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/4/Text/47` | 0.561971 | **Type ***3rd-rank spell gem*; **Level **5; **Price **300 credits |

### Query 49
- Text: Summarize **Type **advanced; **Level **15; **Price **55,555 credits
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/27']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/27', 'PZO22001 Starfinder Player Core 282-293::/page/3/Text/22', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/38']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/27', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/26', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/28']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/26` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/28` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/27` | 1.038837 | **Type **advanced; **Level **15; **Price **55,555 credits |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/3/Text/22` | 0.908118 | **Type **advanced; **Level **14; **Price **38,550 credits |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/38` | 0.831523 | **Type **advanced; **Level **18; **Price **220,600 credits |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/7/Text/19` | 0.771722 | **Type **advanced; **Level **20; **Price **495,000 credits |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/3/Text/11` | 0.761688 | **Type **tactical; **Level **15; **Price **66,666 credits |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/2/Text/12` | 0.760937 | **Type **advanced; **Level **18; **Price **190,400 credits |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/8/Text/15` | 0.734745 | **Type **advanced; **Level **8; **Price **4,200 credits |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/1/SectionHeader/4` | 0.734065 | **Type **guiding; **Level **15; **Price **61,000 credits |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/6/Text/22` | 0.730055 | **Type **advanced; **Level **7; **Price **3,300 credits |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/8/Text/23` | 0.726286 | **Type **advanced; **Level **7; **Price **3,240 credits |

### Query 50
- Text: What is the rule about The item bonus is +2, and the *Akashic* *download* spell is 4th  rank.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/28']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/28', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/26', 'PZO22001 Starfinder Player Core 282-293::/page/3/Text/12']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/28', 'PZO22001 Starfinder Player Core 282-293::/page/1/SectionHeader/29', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/27']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/1/SectionHeader/29` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/27` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/28` | 0.929111 | The item bonus is +2, and the *Akashic* *download* spell is 4th  rank. |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/26` | 0.749167 | **Type **tactical; **Level **9; **Price **5,555 credits The *Akashic* *download* spell is 3rd rank. |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/3/Text/12` | 0.617528 | The item bonus is +2, and the *share* *pain* spell is 7th rank  (DC 34). |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/3/Text/21` | 0.563644 | The item bonus is +2, and the *lock* spell is 3rd rank (DC 25). |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/3/Text/23` | 0.562703 | The item bonus is +3, and the *lock* spell is 7th rank (DC 35). |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/2/Text/11` | 0.559708 | The item bonus is +2, and the *sonic* *scream* spell is 4th rank  (DC 27). |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/2/Text/13` | 0.527805 | The item bonus is +3, and the *sonic* *scream* spell is 8th rank  (DC 38). |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/5/TableCell/1233` | 0.491137 | 4th-rank spell gem |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/4/Text/48` | 0.486085 | **Type*** 4th-rank spell gem*; **Level **7; **Price **700 credits |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/10/Text/29` | 0.478962 | When you get an augmentation with the apex trait, it improves  one of your attributes, either increasing the attribute's modifier  by 1 or to a total of +4, whichever would give you a higher score. |

### Query 51
- Text: Summarize **ANTIGRAV HARNESS** **ITEM 6+**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/SectionHeader/29']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/1/SectionHeader/29', 'PZO22001 Starfinder Player Core 282-293::/page/5/TableCell/1423', 'PZO22001 Starfinder Player Core 282-293::/page/5/TableCell/1218']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/SectionHeader/29', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/31', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/28']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/31` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/28` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/1/SectionHeader/29` | 1.022858 | **ANTIGRAV HARNESS** **ITEM 6+** |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/5/TableCell/1423` | 0.646801 | Antigrav harness, advanced |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/5/TableCell/1218` | 0.598138 | Antigrav harness, commercial |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/5/TableCell/1338` | 0.551824 | Antigrav harness, tactical |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/2/SectionHeader/21` | 0.458820 | **HARDLIGHT HANDWRAPS** **ITEM 2+** |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/3/SectionHeader/13` | 0.372146 | **PROGRAMMER'S PLUSHIE** **ITEM 3+** |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/2/SectionHeader/14` | 0.370914 | **DUO-ENHANCERS** **ITEM 3** |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/3/SectionHeader/4` | 0.370603 | **PAIN JOURNAL** **ITEM 7+** |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/4/Text/14` | 0.365000 | **Type ***commercial* *resist* *energy* *spell* *amp*; **Level **6; **Price **450  credits; **Effect** 2nd-rank *resist energy* spell |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/5/Table/2` | 0.359711 | ItemLevelPriceBulkHandsGlow up spell amp, advanced91,100L1Diva's microphone, tactical109,500L1Hardlight handwraps, superior1010,005——Resist energy spell amp, tactical101,800L15th-rank spell chip1115,0 |

### Query 52
- Text: Summarize **INVESTED** **MAGICAL** **TECH**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/31']
- Expected found: `True`
- Expected rank: `5`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/21', 'PZO22001 Starfinder Player Core 282-293::/page/3/Text/15', 'PZO22001 Starfinder Player Core 282-293::/page/2/Text/16']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/31', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/32', 'PZO22001 Starfinder Player Core 282-293::/page/1/SectionHeader/29']
- Expanded expected found: `True`
- Expanded expected rank: `5`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/32` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/1/SectionHeader/29` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/21` | 1.002080 | **INVESTED** **MAGICAL** **TECH** |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/3/Text/15` | 1.002080 | **INVESTED** **MAGICAL** **TECH** |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/2/Text/16` | 1.002080 | **INVESTED** **MAGICAL** **TECH** |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/42` | 0.960080 | **INVESTED** **MAGICAL** **TECH** |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/31` | 0.960080 | **INVESTED** **MAGICAL** **TECH** |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/3/Text/6` | 0.960080 | **INVESTED** **MAGICAL** **TECH** |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/2/Text/23` | 0.960080 | **INVESTED** **MAGICAL** **TECH** |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/4/SectionHeader/24` | 0.784007 | **MAGICAL** **TECH** |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/24` | 0.773278 | **UNCOMMON** **INVESTED** **MAGICAL** |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/10/Text/25` | 0.685266 | **MAGICAL** **MAGITECH** |

### Query 53
- Text: Summarize **Usage** worn garment; **Bulk **1
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/32']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/32', 'PZO22001 Starfinder Player Core 282-293::/page/2/Text/37', 'PZO22001 Starfinder Player Core 282-293::/page/0/Text/25']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/32', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/31', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/33']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/31` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/33` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/32` | 1.025657 | **Usage** worn garment; **Bulk **1 |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/2/Text/37` | 0.904800 | **Usage** worn; **Bulk **— |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/25` | 0.904800 | **Usage** worn; **Bulk **— |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/2/Text/24` | 0.822719 | **Usage** worn gloves; **Bulk **— |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/2/Text/18` | 0.762830 | **Usage** worn armbands or gloves; **Bulk **L |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/22` | 0.677807 | **Usage** worn eyepiece; **Bulk **— |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/4/SectionHeader/25` | 0.648146 | **Usage** installed in computer or comm unit; **Bulk **– |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/3/Text/28` | 0.640441 | **Usage** held in 1 hand; **Bulk **1 |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/3/Text/16` | 0.627823 | **Usage** held, stowed, or within arm's reach; **Bulk **L |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/43` | 0.613332 | **Usage** held in 1 hand; **Bulk **L |

### Query 54
- Text: What is the rule about This convoluted web of synthweave straps is worn as a  fashion statement in some subcultures but has a useful  application in extreme environments. You gain a +1 item  bonus to Acrobatics checks, and you aren't off-guard or  clumsy while untethered in zero-g.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/33']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/33', 'PZO22001 Starfinder Player Core 282-293::/page/2/Text/19', 'PZO22001 Starfinder Player Core 282-293::/page/2/Text/4']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/33', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/34', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/32']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/34` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/32` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/33` | 0.989037 | This convoluted web of synthweave straps is worn as a  fashion statement in some subcultures but has a useful  application in extreme environments. You gain a +1 item  bonus to Acrobatics checks, and |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/2/Text/19` | 0.529120 | This magitech interface is a sophisticated pair of linked  bracers, wristbands, gloves, or other garments suitable to  the part of a creature's anatomy it uses to wield weapons.  One of the paired enh |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/2/Text/4` | 0.512419 | **Invested:** A PC can wear only 10 magical items that  have the invested trait. A character can still gain any  normal benefit from using a physical item without  investing it, such as using a *progr |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/17` | 0.462264 | This deep-blue prism with cloudy inclusions is light as a  feather. Its resonant power gives you a +1 item bonus to  Acrobatics checks. |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/2/Text/25` | 0.453433 | These handwraps can be customized to shine in any color in  the visible spectrum when used, and some manufacturers  offer custom firmware that modifies their appearance to  manifest as a claw, oversiz |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/8/Text/39` | 0.449965 | When the compartment is closed, the seam in your limb is  difficult to detect. You gain a +1 item bonus to Stealth checks to  Conceal an Object in a hideaway limb. Though this compartment  can foil a |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/6/Text/2` | 0.449900 | Many explorers and mercenaries modify their bodies with technological or biological gear called  augmentations. These modifications to your body give you special abilities and bonuses. Once  installed |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/11/Text/1` | 0.446566 | This augmentation enhances your muscles and nervous system  to dramatically improve your flexibility and reaction time. You  gain a +3 item bonus to Acrobatics checks. When you get this  augmentation, |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/11/Text/6` | 0.439848 | This augmentation keeps your muscles in peak condition. You  gain a +3 item bonus to Athletics checks. When you get this  augmentation, you either increase your Strength modifier by 1  or increase it |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/8/Text/38` | 0.434832 | You can conceal items inside a hidden compartment in one of  your limbs (such as an arm, leg, or tail) and protect them with  a passcode. The compartment holds items of negligible Bulk  and items of l |

### Query 55
- Text: What is the rule about **Activate—Gravity Alteration** [one-action] (manipulate) **Effect** You treat  gravity as being one step higher or lower (for example,  zero-g becomes low gravity, low gravity becomes standard,  standard gravity becomes high gravity, and high gravity  becomes extreme gravity, or vice versa). This only affects  you, your gear, and your movement and lasts until the end  of your next turn.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/34']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/34', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/39', 'PZO22001 Starfinder Player Core 282-293::/page/8/Text/40']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/34', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/33', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/35']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/33` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/35` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/34` | 0.970594 | **Activate—Gravity Alteration** [one-action] (manipulate) **Effect** You treat  gravity as being one step higher or lower (for example,  zero-g becomes low gravity, low gravity becomes standard,  stan |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/39` | 0.647925 | The item bonus is +3, and Gravity Alteration lasts 1 minute  and can lower or raise the gravity level by up to two steps. |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/8/Text/40` | 0.642471 | **Activate—Draw** [one-action] (manipulate) **Effect** You Interact to draw  an item concealed in your hideaway limb. |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/4/Text/6` | 0.566932 | **Activate—Inject** [one-action] (manipulate) **Effect** You Cast the Spell at  the indicated rank. |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/7/Text/59` | 0.562499 | **Activate—Accelerate** [free-action] **Frequency** once per 10 minutes;  **Trigger** You Climb, Stride, or Swim; **Effect** You increase  your Speed by 20 feet for the triggering action. |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/12` | 0.551409 | While some items function automatically and grant constant  benefits, others produce effects only when properly used. An  activation lists the number of actions it takes and any traits  of the activat |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/3/Text/30` | 0.539653 | **Activate—Install Grenade** [one-action] (manipulate) You install a  commercial, tactical, or advanced grenade in the shell.  You can store one grenade in the shell at a time, and you  can Interact t |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/11/Text/12` | 0.536950 | **Activate—Irresistible Idea** [two-actions] (concentrate) **Frequency** once per hour; **Effect** You manipulate your cosmetics to  influence a creature as a 4th-rank *suggestion* (DC 38). |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/6/Text/19` | 0.534477 | **Activate—Exhale** [one-action] (manipulate) **Frequency** once per  10 minutes; **Effect** Each creature in a 15-foot cone takes  damage with a basic Reflex save. The damage depends on the  augmenta |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/6/Text/12` | 0.533365 | Many augmentations work continuously. Augmentations  with an Activate entry usually require you to concentrate or  Interact to gain an additional boost or ability. Once activated,  an augmentation oft |

### Query 56
- Text: Summarize **Type **commercial; **Level **6; **Price **2,100 credits
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/35']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/35', 'PZO22001 Starfinder Player Core 282-293::/page/8/Text/12', 'PZO22001 Starfinder Player Core 282-293::/page/7/Text/25']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/35', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/36', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/34']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/36` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/34` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/35` | 1.040646 | **Type **commercial; **Level **6; **Price **2,100 credits |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/8/Text/12` | 0.893086 | **Type **commercial; **Level **1; **Price **100 credits |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/7/Text/25` | 0.875570 | **Type **commercial; **Level **3; **Price **600 credits |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/8/Text/5` | 0.833570 | **Type **commercial; **Level **3; **Price **600 credits |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/7/Text/16` | 0.824644 | **Type **commercial; **Level **8; **Price **3,450 credits |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/3/Text/10` | 0.815421 | **Type **commercial; **Level **7; **Price **3,333 credits |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/8/Text/21` | 0.810108 | **Type **commercial; **Level **1; **Price **180 credits |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/8/Text/41` | 0.802514 | **Type **commercial; **Level **1; **Price **140 credits |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/2/Text/9` | 0.799536 | **Type **commercial; **Level **4; **Price **750 credits |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/25` | 0.798437 | **Type **commercial; **Level **3; **Price **555 credits |

### Query 57
- Text: What is the rule about **Type **tactical; **Level **12; **Price **16,500 credits?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/36']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/36', 'PZO22001 Starfinder Player Core 282-293::/page/7/Text/26', 'PZO22001 Starfinder Player Core 282-293::/page/3/Text/11']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/36', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/37', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/35']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/37` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/35` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/36` | 0.901430 | **Type **tactical; **Level **12; **Price **16,500 credits |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/7/Text/26` | 0.801560 | **Type **tactical; **Level **6; **Price **2,500 credits |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/3/Text/11` | 0.788177 | **Type **tactical; **Level **15; **Price **66,666 credits |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/8/Text/6` | 0.741744 | **Type **tactical; **Level **5; **Price **1,600 credits |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/7/Text/17` | 0.732972 | **Type **tactical; **Level **14; **Price **35,000 credits |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/10/Text/16` | 0.725114 | **Type **tactical;** Level **6; **Price **2,250 credits |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/8/Text/42` | 0.718369 | **Type **tactical; **Level **5; **Price **1,400 credits |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/3/Text/20` | 0.717703 | **Type **tactical; **Level **8; **Price **4,550 credits |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/2/Text/10` | 0.711798 | **Type **tactical; **Level **10; **Price **9,500 credits |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/8/Text/13` | 0.655489 | **Type **tactical; **Level **4; **Price **750 credits |

### Query 58
- Text: Summarize The item bonus is +2, and Gravity Alteration lasts 1 minute.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/37']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/37', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/39', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/34']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/37', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/36', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/38']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/36` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/38` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/37` | 1.034092 | The item bonus is +2, and Gravity Alteration lasts 1 minute. |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/39` | 0.948981 | The item bonus is +3, and Gravity Alteration lasts 1 minute  and can lower or raise the gravity level by up to two steps. |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/34` | 0.599666 | **Activate—Gravity Alteration** [one-action] (manipulate) **Effect** You treat  gravity as being one step higher or lower (for example,  zero-g becomes low gravity, low gravity becomes standard,  stan |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/7/Text/31` | 0.511037 | The fly Speed is 60 feet, and the item bonus is +2. |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/7/Text/29` | 0.508383 | The fly Speed is 40 feet, and the item bonus is +2. |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/10/Text/37` | 0.476651 | **Activate—Life Buffer **[one-action] (manipulate) **Frequency** once per day;  **Effect** You gain 50 temporary Hit Points, which last for 1 hour. |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/7/Text/20` | 0.474580 | The item bonus to saving throws is +3. |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/11/Text/1` | 0.473854 | This augmentation enhances your muscles and nervous system  to dramatically improve your flexibility and reaction time. You  gain a +3 item bonus to Acrobatics checks. When you get this  augmentation, |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/7/Text/18` | 0.469440 | The item bonus to saving throws is +2. |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/11/Text/38` | 0.463771 | **Magic Items** **Augmentations** |

### Query 59
- Text: Summarize **Type **advanced; **Level **18; **Price **220,600 credits
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/38']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/38', 'PZO22001 Starfinder Player Core 282-293::/page/2/Text/12', 'PZO22001 Starfinder Player Core 282-293::/page/7/Text/19']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/38', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/37', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/39']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/37` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/39` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/38` | 1.039515 | **Type **advanced; **Level **18; **Price **220,600 credits |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/2/Text/12` | 0.976895 | **Type **advanced; **Level **18; **Price **190,400 credits |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/7/Text/19` | 0.872153 | **Type **advanced; **Level **20; **Price **495,000 credits |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/8/Text/15` | 0.819801 | **Type **advanced; **Level **8; **Price **4,200 credits |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/9/Text/34` | 0.802054 | **Type **advanced; **Level **12; **Price **20,000 credits |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/3/Text/22` | 0.801986 | **Type **advanced; **Level **14; **Price **38,550 credits |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/27` | 0.798606 | **Type **advanced; **Level **15; **Price **55,555 credits |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/8/Text/23` | 0.759284 | **Type **advanced; **Level **7; **Price **3,240 credits |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/6/Text/22` | 0.755252 | **Type **advanced; **Level **7; **Price **3,300 credits |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/7/Text/28` | 0.746016 | **Type **advanced; **Level **9; **Price **7,000 credits |

### Query 60
- Text: Summarize The item bonus is +3, and Gravity Alteration lasts 1 minute  and can lower or raise the gravity level by up to two steps.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/39']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/39', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/37', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/34']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/39', 'PZO22001 Starfinder Player Core 282-293::/page/1/SectionHeader/40', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/38']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/1/SectionHeader/40` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/38` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/39` | 1.039347 | The item bonus is +3, and Gravity Alteration lasts 1 minute  and can lower or raise the gravity level by up to two steps. |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/37` | 0.942157 | The item bonus is +2, and Gravity Alteration lasts 1 minute. |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/34` | 0.689634 | **Activate—Gravity Alteration** [one-action] (manipulate) **Effect** You treat  gravity as being one step higher or lower (for example,  zero-g becomes low gravity, low gravity becomes standard,  stan |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/11/Text/1` | 0.547639 | This augmentation enhances your muscles and nervous system  to dramatically improve your flexibility and reaction time. You  gain a +3 item bonus to Acrobatics checks. When you get this  augmentation, |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/7/Text/31` | 0.547010 | The fly Speed is 60 feet, and the item bonus is +2. |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/7/Text/29` | 0.542317 | The fly Speed is 40 feet, and the item bonus is +2. |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/10/Text/47` | 0.522487 | This augmentation opens your mind to the underlying cosmic  truths of the universe. When you get this augmentation, you  either increase your Wisdom modifier by 1 or increase it to  +4, whichever woul |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/11/Text/6` | 0.521650 | This augmentation keeps your muscles in peak condition. You  gain a +3 item bonus to Athletics checks. When you get this  augmentation, you either increase your Strength modifier by 1  or increase it |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/9/Text/13` | 0.504345 | **Type **advanced; **Level **12; **Price **16,000 credits Increase the item bonus to 15-feet. |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/9/Text/12` | 0.503695 | **Type **tactical; **Level **8; **Price **4,000 credits Increase the item bonus to 10-feet. |

### Query 61
- Text: Summarize **DIVA'S MICROPHONE** **ITEM 4+**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/SectionHeader/40']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/1/SectionHeader/40', 'PZO22001 Starfinder Player Core 282-293::/page/5/TableCell/1428', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/44']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/SectionHeader/40', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/42', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/39']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/42` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/39` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/1/SectionHeader/40` | 1.026075 | **DIVA'S MICROPHONE** **ITEM 4+** |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/5/TableCell/1428` | 0.655280 | Diva's microphone, advanced |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/44` | 0.634786 | This ostentatious crystal microphone is embellished with  glimmering jewels and delicate lights that pulse in time  to music. It functions as both a microphone and speaker,  amplifying your voice loud |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/5/TableCell/1303` | 0.553953 | Diva's microphone, tactical |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/5/TableCell/1173` | 0.549511 | Diva's microphone, commercial |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/5/Table/2` | 0.449639 | ItemLevelPriceBulkHandsGlow up spell amp, advanced91,100L1Diva's microphone, tactical109,500L1Hardlight handwraps, superior1010,005——Resist energy spell amp, tactical101,800L15th-rank spell chip1115,0 |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/4/SectionHeader/22` | 0.404245 | **SPELL CHIP** **ITEM 1+** |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/5/Table/1` | 0.400744 | ItemLevelPriceBulkHandsGlow up spell amp,commercial150L1Reusable grenade shell18011Hardlight handwraps, tactical2355——Jump spell amp260L11st-rank spell chip3600——2nd-rank spell gem3120——Akashic lens, |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/4/SectionHeader/55` | 0.383750 | **MAGIC ITEMS** |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/11/Table/17` | 0.373555 | ItemLevelPriceAutorecognition lens05Hearing aid05Prosthetic limb05Datajack, commercial1100Dermal plating, commercial1180Hideaway limb, commercial1140Retinal reflectors1200Vocal modulator190Darkvision |

### Query 62
- Text: Summarize **INVESTED** **MAGICAL** **TECH**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/42']
- Expected found: `True`
- Expected rank: `4`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/21', 'PZO22001 Starfinder Player Core 282-293::/page/3/Text/15', 'PZO22001 Starfinder Player Core 282-293::/page/2/Text/16']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/42', 'PZO22001 Starfinder Player Core 282-293::/page/1/SectionHeader/40', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/43']
- Expanded expected found: `True`
- Expanded expected rank: `4`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/1/SectionHeader/40` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/43` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/21` | 1.002080 | **INVESTED** **MAGICAL** **TECH** |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/3/Text/15` | 1.002080 | **INVESTED** **MAGICAL** **TECH** |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/2/Text/16` | 1.002080 | **INVESTED** **MAGICAL** **TECH** |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/42` | 0.960080 | **INVESTED** **MAGICAL** **TECH** |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/31` | 0.960080 | **INVESTED** **MAGICAL** **TECH** |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/3/Text/6` | 0.960080 | **INVESTED** **MAGICAL** **TECH** |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/2/Text/23` | 0.960080 | **INVESTED** **MAGICAL** **TECH** |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/4/SectionHeader/24` | 0.784007 | **MAGICAL** **TECH** |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/24` | 0.773278 | **UNCOMMON** **INVESTED** **MAGICAL** |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/10/Text/25` | 0.685266 | **MAGICAL** **MAGITECH** |

### Query 63
- Text: Summarize **Usage** held in 1 hand; **Bulk **L
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/43']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/43', 'PZO22001 Starfinder Player Core 282-293::/page/4/SectionHeader/4', 'PZO22001 Starfinder Player Core 282-293::/page/4/SectionHeader/42']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/43', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/42', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/44']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/42` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/44` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/43` | 1.023826 | **Usage** held in 1 hand; **Bulk **L |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/4/SectionHeader/4` | 1.023826 | **Usage** held in 1 hand; **Bulk **L |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/4/SectionHeader/42` | 1.023826 | **Usage** held in 1 hand; **Bulk **L |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/3/Text/28` | 0.956714 | **Usage** held in 1 hand; **Bulk **1 |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/3/Text/7` | 0.917230 | **Usage** held in 2 hands; **Bulk **L |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/3/Text/16` | 0.799462 | **Usage** held, stowed, or within arm's reach; **Bulk **L |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/25` | 0.679820 | **Usage** worn; **Bulk **— |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/2/Text/37` | 0.679820 | **Usage** worn; **Bulk **— |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/2/Text/24` | 0.676504 | **Usage** worn gloves; **Bulk **— |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/2/Text/18` | 0.674203 | **Usage** worn armbands or gloves; **Bulk **L |

### Query 64
- Text: Summarize This ostentatious crystal microphone is embellished with  glimmering jewels and delicate lights that pulse in time  to music. It functions as both a microphone and speaker,  amplifying your voice loud enough for you to be heard  clearly by all listeners up to 500 feet away, even if other  ambient noise would otherwise block the sound. This  doesn't increase the range or area of other auditory or  linguistic effects, and physical barriers such as walls still  block or muffle your voice as normal. The *diva's microphone*
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/44']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/44', 'PZO22001 Starfinder Player Core 282-293::/page/5/TableCell/1428', 'PZO22001 Starfinder Player Core 282-293::/page/5/TableCell/1303']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/44', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/43', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/46']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/43` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/46` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/44` | 1.044236 | This ostentatious crystal microphone is embellished with  glimmering jewels and delicate lights that pulse in time  to music. It functions as both a microphone and speaker,  amplifying your voice loud |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/5/TableCell/1428` | 0.726615 | Diva's microphone, advanced |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/5/TableCell/1303` | 0.683932 | Diva's microphone, tactical |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/5/TableCell/1173` | 0.602656 | Diva's microphone, commercial |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/1/SectionHeader/40` | 0.584502 | **DIVA'S MICROPHONE** **ITEM 4+** |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/9/Text/23` | 0.528403 | A voice amplifier greatly increases the volume of your voice.  You can switch a voice amplifier on or off by spending an action,  which has the concentrate trait. While active, a voice amplifier  gran |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/9/Text/18` | 0.525400 | A series of miniature actuators and dynamic hyper-resonant  chambers reshape your voice box. A vocal modulator allows  you to change the pitch, timbre, and tone of your voice so you  can imitate accen |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/11/TableCell/821` | 0.479071 | Voice amplifier |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/7/Text/41` | 0.466115 | This soft purple fungus attaches to your vocal cords  and extends fine filaments into portions of your brain.  You can ask questions of, receive answers from, and use  the Diplomacy skill with animals |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/5` | 0.457944 | This gold star glitters with joyful energy. Its resonant power  allows you to cast *guidance* as an occult innate cantrip. |

### Query 65
- Text: Summarize **INTRODUCTION**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/46']
- Expected found: `True`
- Expected rank: `5`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/11/Text/23', 'PZO22001 Starfinder Player Core 282-293::/page/3/Text/32', 'PZO22001 Starfinder Player Core 282-293::/page/7/Text/61']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/46', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/47', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/44']
- Expanded expected found: `True`
- Expanded expected rank: `5`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/47` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/44` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/11/Text/23` | 0.880541 | **INTRODUCTION** |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/3/Text/32` | 0.880541 | **INTRODUCTION** |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/7/Text/61` | 0.880541 | **INTRODUCTION** |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/9/Text/36` | 0.838541 | **INTRODUCTION** |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/46` | 0.838541 | **INTRODUCTION** |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/5/Text/8` | 0.799846 | **Introduction** |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/7/Text/66` | 0.799846 | **Introduction** |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/3/Text/38` | 0.799846 | **Introduction** |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/52` | 0.799846 | **Introduction** |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/11/Text/28` | 0.799846 | **Introduction** |

### Query 66
- Text: What is the rule about **ANCESTRIES & ** **BACKGROUNDS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/47']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/47', 'PZO22001 Starfinder Player Core 282-293::/page/11/Text/24', 'PZO22001 Starfinder Player Core 282-293::/page/7/Text/62']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/47', 'PZO22001 Starfinder Player Core 282-293::/page/11/Text/24', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/46', 'PZO22001 Starfinder Player Core 282-293::/page/7/Text/62', 'PZO22001 Starfinder Player Core 282-293::/page/9/Text/37', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/48', 'PZO22001 Starfinder Player Core 282-293::/page/3/Text/33']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/11/Text/24` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/46` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/7/Text/62` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/9/Text/37` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/48` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/3/Text/33` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/47` | 0.920820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/11/Text/24` | 0.920820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/7/Text/62` | 0.920820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/3/Text/33` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/9/Text/37` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/5/Text/4` | 0.672101 | **INTRODUCTION** **ANCESTRIES & ** |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/5/Text/5` | 0.527382 | **BACKGROUNDS** **CLASSES** |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/11/Text/41` | 0.343180 | **CONDITIONS ** **APPENDIX** |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/65` | 0.343180 | **CONDITIONS ** **APPENDIX** |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/3/Text/51` | 0.343180 | **CONDITIONS ** **APPENDIX** |

### Query 67
- Text: Summarize **CLASSES**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/48']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/3/Text/34', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/48', 'PZO22001 Starfinder Player Core 282-293::/page/7/Text/63']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/48', 'PZO22001 Starfinder Player Core 282-293::/page/7/Text/63', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/49', 'PZO22001 Starfinder Player Core 282-293::/page/11/Text/25', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/47', 'PZO22001 Starfinder Player Core 282-293::/page/3/Text/34', 'PZO22001 Starfinder Player Core 282-293::/page/9/Text/38']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/7/Text/63` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/49` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/11/Text/25` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/47` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/3/Text/34` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/9/Text/38` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/3/Text/34` | 0.940061 | **CLASSES** |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/48` | 0.940061 | **CLASSES** |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/7/Text/63` | 0.940061 | **CLASSES** |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/11/Text/25` | 0.910061 | **CLASSES** |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/9/Text/38` | 0.910061 | **CLASSES** |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/5/Text/5` | 0.784512 | **BACKGROUNDS** **CLASSES** |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/52` | 0.442356 | **Introduction** |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/5/Text/8` | 0.442356 | **Introduction** |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/3/Text/38` | 0.442356 | **Introduction** |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/7/Text/66` | 0.442356 | **Introduction** |

### Query 68
- Text: What is the rule about **SKILLS** **FEATS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/49']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/49', 'PZO22001 Starfinder Player Core 282-293::/page/7/Text/64', 'PZO22001 Starfinder Player Core 282-293::/page/5/Text/6']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/49', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/50', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/48']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/50` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/48` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/49` | 0.909736 | **SKILLS** **FEATS** |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/7/Text/64` | 0.909736 | **SKILLS** **FEATS** |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/5/Text/6` | 0.909736 | **SKILLS** **FEATS** |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/11/Text/26` | 0.867736 | **SKILLS** **FEATS** |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/3/Text/35` | 0.867736 | **SKILLS** **FEATS** |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/9/Text/39` | 0.656535 | **SKILLS** |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/9/Text/40` | 0.540172 | **FEATS** **EQUIPMENT** |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/2/Text/5` | 0.376842 | **Magical:** Items with the magical trait can be crafted  only if a player has the Magical Crafting feat (page 224). |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/2/Text/6` | 0.366080 | **Tech:** Items with the tech trait can be crafted by  anyone, but if they're level 1 or higher, they require  the Tech Crafting feat (page 229) to craft. If a tech  item also has the magical trait, t |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/5/Text/5` | 0.361863 | **BACKGROUNDS** **CLASSES** |

### Query 69
- Text: Summarize **EQUIPMENT**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/50']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/50', 'PZO22001 Starfinder Player Core 282-293::/page/3/Text/36', 'PZO22001 Starfinder Player Core 282-293::/page/7/Text/65']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/50', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/49', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/52']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/49` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/52` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/50` | 0.944726 | **EQUIPMENT** |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/3/Text/36` | 0.944726 | **EQUIPMENT** |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/7/Text/65` | 0.944726 | **EQUIPMENT** |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/5/Text/7` | 0.902726 | **EQUIPMENT** |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/11/Text/27` | 0.902726 | **EQUIPMENT** |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/9/Text/40` | 0.627947 | **FEATS** **EQUIPMENT** |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/9/Text/50` | 0.538149 | **Ammunition & ** **Weapons** |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/9/Text/46` | 0.538083 | **Weapons** |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/3/Text/42` | 0.538083 | **Weapons** |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/7/Text/71` | 0.538083 | **Weapons** |

### Query 70
- Text: Summarize **Introduction**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/52']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/52', 'PZO22001 Starfinder Player Core 282-293::/page/3/Text/38', 'PZO22001 Starfinder Player Core 282-293::/page/5/Text/8']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/52', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/50', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/53']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/50` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/53` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/52` | 0.868286 | **Introduction** |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/3/Text/38` | 0.868286 | **Introduction** |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/5/Text/8` | 0.868286 | **Introduction** |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/7/Text/66` | 0.826286 | **Introduction** |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/9/Text/42` | 0.826286 | **Introduction** |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/11/Text/28` | 0.826286 | **Introduction** |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/46` | 0.767385 | **INTRODUCTION** |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/3/Text/32` | 0.767385 | **INTRODUCTION** |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/11/Text/23` | 0.767385 | **INTRODUCTION** |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/9/Text/36` | 0.767385 | **INTRODUCTION** |

### Query 71
- Text: Summarize **Tech Gear**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/53']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/5/Text/9', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/53', 'PZO22001 Starfinder Player Core 282-293::/page/3/Text/39']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/53', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/52', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/54']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/52` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/54` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/5/Text/9` | 0.945693 | **Tech Gear** |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/53` | 0.945693 | **Tech Gear** |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/3/Text/39` | 0.945693 | **Tech Gear** |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/9/Text/43` | 0.903693 | **Tech Gear** |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/7/Text/67` | 0.903693 | **Tech Gear** |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/11/Text/30` | 0.768038 | **Tech Gear** **Armor** |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/8/Text/19` | 0.585901 | **TECH** |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/8/Text/32` | 0.585901 | **TECH** |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/8/Text/3` | 0.585901 | **TECH** |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/7/Text/46` | 0.585901 | **TECH** |

### Query 72
- Text: Summarize **Armor**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/54']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/9/Text/44', 'PZO22001 Starfinder Player Core 282-293::/page/7/Text/69', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/54']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/54', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/55', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/53']
- Expanded expected found: `True`
- Expanded expected rank: `3`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/55` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/53` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/9/Text/44` | 0.943498 | **Armor** |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/7/Text/69` | 0.943498 | **Armor** |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/54` | 0.943498 | **Armor** |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/3/Text/40` | 0.901498 | **Armor** |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/5/Text/10` | 0.901498 | **Armor** |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/11/Text/33` | 0.886051 | **Armor ** |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/5/Text/12` | 0.820831 | **Weapons** **Armor ** |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/56` | 0.820831 | **Weapons** **Armor ** |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/11/Text/30` | 0.747449 | **Tech Gear** **Armor** |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/7/Text/72` | 0.737226 | **Armor ** **Upgrades** |

### Query 73
- Text: Summarize **Shields**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/55']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/7/Text/70', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/55', 'PZO22001 Starfinder Player Core 282-293::/page/3/Text/41']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/55', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/54', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/56']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/54` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/56` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/7/Text/70` | 0.978985 | **Shields** |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/55` | 0.978985 | **Shields** |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/3/Text/41` | 0.978985 | **Shields** |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/9/Text/45` | 0.936985 | **Shields** |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/5/Text/11` | 0.936985 | **Shields** |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/11/Text/32` | 0.789608 | **Shields** **Weapons** |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/11/TableCell/788` | 0.464609 | Shielding skin, advanced |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/11/TableCell/776` | 0.426883 | Shielding skin, tactical |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/3/Text/42` | 0.420611 | **Weapons** |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/7/Text/71` | 0.420611 | **Weapons** |

### Query 74
- Text: Summarize **Weapons** **Armor **
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/56']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/5/Text/12', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/56', 'PZO22001 Starfinder Player Core 282-293::/page/9/Text/50']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/56', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/55', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/57']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/55` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/57` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/5/Text/12` | 0.971434 | **Weapons** **Armor ** |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/56` | 0.971434 | **Weapons** **Armor ** |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/9/Text/50` | 0.807118 | **Ammunition & ** **Weapons** |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/9/Text/46` | 0.750176 | **Weapons** |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/7/Text/71` | 0.750176 | **Weapons** |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/3/Text/42` | 0.750176 | **Weapons** |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/11/Text/30` | 0.728872 | **Tech Gear** **Armor** |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/5/Text/10` | 0.702249 | **Armor** |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/54` | 0.702249 | **Armor** |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/9/Text/44` | 0.702249 | **Armor** |

### Query 75
- Text: Summarize **Upgrades**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/57']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/5/Text/13', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/57', 'PZO22001 Starfinder Player Core 282-293::/page/11/Text/34']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/57', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/58', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/56']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/58` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/56` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/5/Text/13` | 0.931560 | **Upgrades** |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/57` | 0.931560 | **Upgrades** |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/11/Text/34` | 0.931560 | **Upgrades** |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/58` | 0.781527 | **Weapon ** **Upgrades** |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/5/Text/14` | 0.781527 | **Weapon ** **Upgrades** |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/11/Text/35` | 0.781527 | **Weapon ** **Upgrades** |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/7/Text/73` | 0.769527 | **Weapon ** **Upgrades** |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/3/Text/44` | 0.769527 | **Weapon ** **Upgrades** |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/9/Text/47` | 0.695708 | **Armor ** **Upgrades** |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/3/Text/43` | 0.695708 | **Armor ** **Upgrades** |

### Query 76
- Text: Summarize **Weapon ** **Upgrades**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/58']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/7/Text/73', 'PZO22001 Starfinder Player Core 282-293::/page/5/Text/14', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/58']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/58', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/57', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/59']
- Expanded expected found: `True`
- Expanded expected rank: `3`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/57` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/59` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/7/Text/73` | 0.973000 | **Weapon ** **Upgrades** |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/5/Text/14` | 0.973000 | **Weapon ** **Upgrades** |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/58` | 0.973000 | **Weapon ** **Upgrades** |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/3/Text/44` | 0.931000 | **Weapon ** **Upgrades** |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/11/Text/35` | 0.931000 | **Weapon ** **Upgrades** |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/5/Text/13` | 0.739874 | **Upgrades** |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/57` | 0.739874 | **Upgrades** |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/11/Text/34` | 0.727874 | **Upgrades** |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/7/Text/72` | 0.701684 | **Armor ** **Upgrades** |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/3/Text/43` | 0.689684 | **Armor ** **Upgrades** |

### Query 77
- Text: Summarize **Precious ** **Ammunition & ** **Weapons**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/59']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/5/Text/15', 'PZO22001 Starfinder Player Core 282-293::/page/7/Text/74', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/59']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/59', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/60', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/58']
- Expanded expected found: `True`
- Expanded expected rank: `3`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/60` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/58` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/5/Text/15` | 0.999510 | **Precious ** **Ammunition & ** **Weapons** |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/7/Text/74` | 0.999510 | **Precious ** **Ammunition & ** **Weapons** |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/59` | 0.999510 | **Precious ** **Ammunition & ** **Weapons** |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/11/Text/36` | 0.957510 | **Precious ** **Ammunition & ** **Weapons** |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/3/Text/45` | 0.900678 | **Precious ** **Ammunition & ** |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/9/Text/50` | 0.776087 | **Ammunition & ** **Weapons** |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/7/Text/71` | 0.656914 | **Weapons** |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/3/Text/42` | 0.656914 | **Weapons** |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/9/Text/46` | 0.656914 | **Weapons** |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/56` | 0.637220 | **Weapons** **Armor ** |

### Query 78
- Text: Summarize **Grenades**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/60']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/9/Text/51', 'PZO22001 Starfinder Player Core 282-293::/page/11/Text/37', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/60']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/60', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/61', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/59']
- Expanded expected found: `True`
- Expanded expected rank: `3`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/61` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/59` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/9/Text/51` | 0.977096 | **Grenades** |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/11/Text/37` | 0.977096 | **Grenades** |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/60` | 0.977096 | **Grenades** |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/7/Text/75` | 0.935096 | **Grenades** |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/3/Text/46` | 0.820354 | **Weapons** **Grenades** |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/5/Text/16` | 0.712512 | **Grenades** **Magic Items** |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/3/SectionHeader/24` | 0.530754 | **REUSABLE GRENADE SHELL** **ITEM 1** |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/3/Text/26` | 0.529836 | **GRENADE** **MAGICAL** **TECH** |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/3/Text/30` | 0.442808 | **Activate—Install Grenade** [one-action] (manipulate) You install a  commercial, tactical, or advanced grenade in the shell.  You can store one grenade in the shell at a time, and you  can Interact t |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/5/TableCell/1128` | 0.439519 | Reusable grenade shell |

### Query 79
- Text: Summarize **Magic Items**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/61']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/7/Text/76', 'PZO22001 Starfinder Player Core 282-293::/page/9/Text/52', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/61']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/61', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/60', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/62']
- Expanded expected found: `True`
- Expanded expected rank: `3`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/60` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/62` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/7/Text/76` | 0.963309 | **Magic Items** |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/9/Text/52` | 0.963309 | **Magic Items** |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/61` | 0.963309 | **Magic Items** |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/3/Text/47` | 0.921309 | **Magic Items** |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/4/SectionHeader/55` | 0.866645 | **MAGIC ITEMS** |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/1` | 0.825571 | MAGIC ITEMS |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/21` | 0.761782 | SPECIFIC MAGIC ITEMS |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/11/Text/38` | 0.749950 | **Magic Items** **Augmentations** |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/6` | 0.713189 | INVESTING MAGIC ITEMS |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/5/Text/16` | 0.667549 | **Grenades** **Magic Items** |

### Query 80
- Text: Summarize **Augmentations**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/62']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/5/Text/17', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/62', 'PZO22001 Starfinder Player Core 282-293::/page/9/Text/53']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/62', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/61', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/63']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/61` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/63` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/5/Text/17` | 0.964521 | **Augmentations** |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/62` | 0.964521 | **Augmentations** |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/9/Text/53` | 0.964521 | **Augmentations** |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/3/Text/48` | 0.922521 | **Augmentations** |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/7/Text/77` | 0.922521 | **Augmentations** |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/6/SectionHeader/1` | 0.740774 | AUGMENTATIONS |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/11/Text/38` | 0.725584 | **Magic Items** **Augmentations** |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/6/SectionHeader/11` | 0.688884 | ACTIVATING AUGMENTATIONS |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/8/SectionHeader/9` | 0.644018 | **DATAJACK** **AUGMENTATION 1+** |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/9/SectionHeader/19` | 0.622122 | **VOICE AMPLIFIER** **AUGMENTATION 3** |

### Query 81
- Text: What is the rule about **SPELLS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/63']
- Expected found: `True`
- Expected rank: `4`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/9/Text/54', 'PZO22001 Starfinder Player Core 282-293::/page/11/Text/39', 'PZO22001 Starfinder Player Core 282-293::/page/5/Text/18']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/63', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/62', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/64']
- Expanded expected found: `True`
- Expanded expected rank: `4`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/62` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/64` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/9/Text/54` | 0.889304 | **SPELLS** |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/11/Text/39` | 0.889304 | **SPELLS** |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/5/Text/18` | 0.889304 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/63` | 0.847304 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/7/Text/78` | 0.847304 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/3/Text/49` | 0.847304 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/19` | 0.605599 | CAST A SPELL |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/4/SectionHeader/39` | 0.535480 | **SPELL GEM** **ITEM 1+** |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/4/SectionHeader/22` | 0.502746 | **SPELL CHIP** **ITEM 1+** |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/4/SectionHeader/1` | 0.491707 | **SPELL AMPOULE** **ITEM 1+** |

### Query 82
- Text: Summarize **PLAYING THE ** **GAME**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/64']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/64', 'PZO22001 Starfinder Player Core 282-293::/page/3/Text/50', 'PZO22001 Starfinder Player Core 282-293::/page/9/Text/55']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/64', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/63', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/65']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/63` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/65` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/64` | 0.965000 | **PLAYING THE ** **GAME** |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/3/Text/50` | 0.965000 | **PLAYING THE ** **GAME** |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/9/Text/55` | 0.965000 | **PLAYING THE ** **GAME** |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/7/Text/79` | 0.923000 | **PLAYING THE ** **GAME** |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/5/Text/19` | 0.923000 | **PLAYING THE ** **GAME** |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/11/Text/40` | 0.923000 | **PLAYING THE ** **GAME** |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/2/Text/8` | 0.434386 | **Activate—Grand Finale** [two-actions] (auditory) **Frequency** once per  10 minutes; **Effect** Your song reaches an eardrum-bursting  climax as you cast a 1st-rank *sonic* *scream* originating  fro |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/11/Text/23` | 0.418586 | **INTRODUCTION** |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/3/Text/32` | 0.418586 | **INTRODUCTION** |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/46` | 0.418586 | **INTRODUCTION** |

### Query 83
- Text: Summarize **CONDITIONS ** **APPENDIX**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/65']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/5/Text/20', 'PZO22001 Starfinder Player Core 282-293::/page/7/Text/80', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/65']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/65', 'PZO22001 Starfinder Player Core 282-293::/page/5/Text/20', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/64', 'PZO22001 Starfinder Player Core 282-293::/page/7/Text/80', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/66', 'PZO22001 Starfinder Player Core 282-293::/page/3/Text/51', 'PZO22001 Starfinder Player Core 282-293::/page/9/Text/56', 'PZO22001 Starfinder Player Core 282-293::/page/11/Text/41']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/5/Text/20` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/64` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/7/Text/80` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/66` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/3/Text/51` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/9/Text/56` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/11/Text/41` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/5/Text/20` | 0.983499 | **CONDITIONS ** **APPENDIX** |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/7/Text/80` | 0.983499 | **CONDITIONS ** **APPENDIX** |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/65` | 0.983498 | **CONDITIONS ** **APPENDIX** |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/9/Text/56` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/3/Text/51` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/11/Text/41` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/11/Text/9` | 0.430486 | **APEX** |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/10/Text/45` | 0.430486 | **APEX** |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/10/Text/34` | 0.430486 | **APEX** |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/11/Text/4` | 0.430486 | **APEX** |

### Query 84
- Text: Summarize **GLOSSARY & ** **INDEX**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/66']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/11/Text/42', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/66', 'PZO22001 Starfinder Player Core 282-293::/page/5/Text/21']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/1/Text/66', 'PZO22001 Starfinder Player Core 282-293::/page/2/SectionHeader/1', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/65']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/2/SectionHeader/1` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/65` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/11/Text/42` | 0.993465 | **GLOSSARY & ** **INDEX** |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/66` | 0.993465 | **GLOSSARY & ** **INDEX** |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/5/Text/21` | 0.993465 | **GLOSSARY & ** **INDEX** |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/9/Text/57` | 0.951465 | **GLOSSARY & ** **INDEX** |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/7/Text/81` | 0.951465 | **GLOSSARY & ** **INDEX** |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/3/Text/52` | 0.832530 | **GLOSSARY & ** **INDEX** **CHARACTER ** |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/11/Text/25` | 0.385404 | **CLASSES** |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/7/Text/63` | 0.385404 | **CLASSES** |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/3/Text/34` | 0.385404 | **CLASSES** |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/48` | 0.385404 | **CLASSES** |

### Query 85
- Text: What is the rule about **ITEM TRAITS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/2/SectionHeader/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/2/SectionHeader/1', 'PZO22001 Starfinder Player Core 282-293::/page/2/Text/2', 'PZO22001 Starfinder Player Core 282-293::/page/2/Text/4']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/2/SectionHeader/1', 'PZO22001 Starfinder Player Core 282-293::/page/2/Text/2', 'PZO22001 Starfinder Player Core 282-293::/page/1/Text/66']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/2/Text/2` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/1/Text/66` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/2/SectionHeader/1` | 0.866364 | **ITEM TRAITS** |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/2/Text/2` | 0.709701 | The following traits apply to items. |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/2/Text/4` | 0.522696 | **Invested:** A PC can wear only 10 magical items that  have the invested trait. A character can still gain any  normal benefit from using a physical item without  investing it, such as using a *progr |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/2/Text/5` | 0.480162 | **Magical:** Items with the magical trait can be crafted  only if a player has the Magical Crafting feat (page 224). |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/2/Text/6` | 0.476889 | **Tech:** Items with the tech trait can be crafted by  anyone, but if they're level 1 or higher, they require  the Tech Crafting feat (page 229) to craft. If a tech  item also has the magical trait, t |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/14` | 0.465556 | You can Activate an Item with the invested trait only if it's  invested by you. |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/2/Text/3` | 0.440537 | **Consumable:** Items with the consumable trait can  be used only once. Most manufacturers design these  items so the container, syringe, or other remaining  materials can't be easily reused to protec |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/4/SectionHeader/55` | 0.432914 | **MAGIC ITEMS** |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/9/Text/52` | 0.425276 | **Magic Items** |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/61` | 0.425276 | **Magic Items** |

### Query 86
- Text: What is the rule about The following traits apply to items.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/2/Text/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/2/Text/2', 'PZO22001 Starfinder Player Core 282-293::/page/2/SectionHeader/1', 'PZO22001 Starfinder Player Core 282-293::/page/2/Text/5']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/2/Text/2', 'PZO22001 Starfinder Player Core 282-293::/page/2/SectionHeader/1', 'PZO22001 Starfinder Player Core 282-293::/page/2/Text/3']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/2/SectionHeader/1` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/2/Text/3` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/2/Text/2` | 0.913818 | The following traits apply to items. |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/2/SectionHeader/1` | 0.616291 | **ITEM TRAITS** |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/2/Text/5` | 0.560648 | **Magical:** Items with the magical trait can be crafted  only if a player has the Magical Crafting feat (page 224). |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/2/Text/4` | 0.525458 | **Invested:** A PC can wear only 10 magical items that  have the invested trait. A character can still gain any  normal benefit from using a physical item without  investing it, such as using a *progr |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/2/Text/6` | 0.518486 | **Tech:** Items with the tech trait can be crafted by  anyone, but if they're level 1 or higher, they require  the Tech Crafting feat (page 229) to craft. If a tech  item also has the magical trait, t |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/14` | 0.513014 | You can Activate an Item with the invested trait only if it's  invested by you. |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/9` | 0.488951 | You invest your energy in an item with the invested trait  as you don it. This process requires 1 or more Interact  actions, usually taking the same amount of time it takes to  don the item. Once you' |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/2/Text/3` | 0.488838 | **Consumable:** Items with the consumable trait can  be used only once. Most manufacturers design these  items so the container, syringe, or other remaining  materials can't be easily reused to protec |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/12` | 0.465776 | While some items function automatically and grant constant  benefits, others produce effects only when properly used. An  activation lists the number of actions it takes and any traits  of the activat |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/16` | 0.461582 | If the activation entry for an item has the manipulate trait,  you can activate it only if you're holding the item or touching  it with a free hand. |

### Query 87
- Text: What is the rule about **Consumable:** Items with the consumable trait can  be used only once. Most manufacturers design these  items so the container, syringe, or other remaining  materials can't be easily reused to protect their  proprietary crafts.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/2/Text/3']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/2/Text/3', 'PZO22001 Starfinder Player Core 282-293::/page/4/SectionHeader/41', 'PZO22001 Starfinder Player Core 282-293::/page/4/SectionHeader/3']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/2/Text/3', 'PZO22001 Starfinder Player Core 282-293::/page/2/Text/2', 'PZO22001 Starfinder Player Core 282-293::/page/2/Text/4']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/2/Text/2` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/2/Text/4` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/2/Text/3` | 0.990236 | **Consumable:** Items with the consumable trait can  be used only once. Most manufacturers design these  items so the container, syringe, or other remaining  materials can't be easily reused to protec |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/4/SectionHeader/41` | 0.549628 | **CONSUMABLE** **MAGICAL** |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/4/SectionHeader/3` | 0.549628 | **CONSUMABLE** **MAGICAL** |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/2/Text/4` | 0.492063 | **Invested:** A PC can wear only 10 magical items that  have the invested trait. A character can still gain any  normal benefit from using a physical item without  investing it, such as using a *progr |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/2/Text/5` | 0.486310 | **Magical:** Items with the magical trait can be crafted  only if a player has the Magical Crafting feat (page 224). |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/2/Text/6` | 0.456978 | **Tech:** Items with the tech trait can be crafted by  anyone, but if they're level 1 or higher, they require  the Tech Crafting feat (page 229) to craft. If a tech  item also has the magical trait, t |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/14` | 0.452293 | You can Activate an Item with the invested trait only if it's  invested by you. |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/18` | 0.447498 | Some items can be activated only a certain number of times  per day, resetting during your daily preparations. You retain  the constant benefits of these items even when the activation  requirements o |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/2/Text/2` | 0.440967 | The following traits apply to items. |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/9` | 0.439868 | You invest your energy in an item with the invested trait  as you don it. This process requires 1 or more Interact  actions, usually taking the same amount of time it takes to  don the item. Once you' |

### Query 88
- Text: What is the rule about **Invested:** A PC can wear only 10 magical items that  have the invested trait. A character can still gain any  normal benefit from using a physical item without  investing it, such as using a *programmer's plushie* as  a makeshift pillow.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/2/Text/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/2/Text/4', 'PZO22001 Starfinder Player Core 282-293::/page/0/Text/7', 'PZO22001 Starfinder Player Core 282-293::/page/0/Text/9']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/2/Text/4', 'PZO22001 Starfinder Player Core 282-293::/page/2/Text/3', 'PZO22001 Starfinder Player Core 282-293::/page/2/Text/5']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/2/Text/3` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/2/Text/5` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/2/Text/4` | 0.992090 | **Invested:** A PC can wear only 10 magical items that  have the invested trait. A character can still gain any  normal benefit from using a physical item without  investing it, such as using a *progr |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/7` | 0.771643 | Certain magic and hybrid items convey their benefits only  when worn and invested using the Invest an Item activity,  connecting them to a specific PC. A PC can benefit from  no more than 10 invested |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/9` | 0.701115 | You invest your energy in an item with the invested trait  as you don it. This process requires 1 or more Interact  actions, usually taking the same amount of time it takes to  don the item. Once you' |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/10` | 0.618434 | You can invest no more than 10 items per day. If you  remove an invested item, it loses its investiture. The item still  counts against your daily limit after it loses its investiture.  You reset the |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/14` | 0.601189 | You can Activate an Item with the invested trait only if it's  invested by you. |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/2/Text/5` | 0.522638 | **Magical:** Items with the magical trait can be crafted  only if a player has the Magical Crafting feat (page 224). |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/6` | 0.513414 | INVESTING MAGIC ITEMS |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/2/Text/6` | 0.479798 | **Tech:** Items with the tech trait can be crafted by  anyone, but if they're level 1 or higher, they require  the Tech Crafting feat (page 229) to craft. If a tech  item also has the magical trait, t |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/2/Text/3` | 0.473965 | **Consumable:** Items with the consumable trait can  be used only once. Most manufacturers design these  items so the container, syringe, or other remaining  materials can't be easily reused to protec |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/3/Text/6` | 0.467264 | **INVESTED** **MAGICAL** **TECH** |

### Query 89
- Text: What is the rule about **Magical:** Items with the magical trait can be crafted  only if a player has the Magical Crafting feat (page 224).?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/2/Text/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/2/Text/5', 'PZO22001 Starfinder Player Core 282-293::/page/2/Text/6', 'PZO22001 Starfinder Player Core 282-293::/page/2/Text/4']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/2/Text/5', 'PZO22001 Starfinder Player Core 282-293::/page/2/Text/4', 'PZO22001 Starfinder Player Core 282-293::/page/2/Text/6']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/2/Text/4` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/2/Text/6` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/2/Text/5` | 0.972028 | **Magical:** Items with the magical trait can be crafted  only if a player has the Magical Crafting feat (page 224). |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/2/Text/6` | 0.799676 | **Tech:** Items with the tech trait can be crafted by  anyone, but if they're level 1 or higher, they require  the Tech Crafting feat (page 229) to craft. If a tech  item also has the magical trait, t |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/2/Text/4` | 0.600063 | **Invested:** A PC can wear only 10 magical items that  have the invested trait. A character can still gain any  normal benefit from using a physical item without  investing it, such as using a *progr |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/3/Text/47` | 0.516573 | **Magic Items** |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/61` | 0.516573 | **Magic Items** |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/7/Text/76` | 0.516573 | **Magic Items** |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/9/Text/52` | 0.516573 | **Magic Items** |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/20` | 0.502996 | If the activation entry for an item lists "Cast a Spell" after  "Activate", you must use the same action as casting the spell  to Activate the Item, unless noted otherwise. You must have  a spellcasti |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/4/SectionHeader/55` | 0.491588 | **MAGIC ITEMS** |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/9` | 0.490193 | You invest your energy in an item with the invested trait  as you don it. This process requires 1 or more Interact  actions, usually taking the same amount of time it takes to  don the item. Once you' |

### Query 90
- Text: What is the rule about **Tech:** Items with the tech trait can be crafted by  anyone, but if they're level 1 or higher, they require  the Tech Crafting feat (page 229) to craft. If a tech  item also has the magical trait, they are hybrid items  and require the Magical Crafting feat (page 224) to  craft. A level 1 or higher hybrid item requires both the  Magical Crafting and Tech Crafting feats to craft.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/2/Text/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/2/Text/6', 'PZO22001 Starfinder Player Core 282-293::/page/2/Text/5', 'PZO22001 Starfinder Player Core 282-293::/page/0/Text/4']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/2/Text/6', 'PZO22001 Starfinder Player Core 282-293::/page/2/Text/7', 'PZO22001 Starfinder Player Core 282-293::/page/2/Text/5']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/2/Text/7` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/2/Text/5` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/2/Text/6` | 0.981113 | **Tech:** Items with the tech trait can be crafted by  anyone, but if they're level 1 or higher, they require  the Tech Crafting feat (page 229) to craft. If a tech  item also has the magical trait, t |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/2/Text/5` | 0.796127 | **Magical:** Items with the magical trait can be crafted  only if a player has the Magical Crafting feat (page 224). |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/4` | 0.611328 | Technology and magic are everywhere in the galaxy.  While some magic equipment have gone unchanged for  thousands of years, the integration of technology to  improve the functionality or cost of many |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/5` | 0.544232 | The tables on pages 286–287 list level, price, Bulk,  and hands entries for a wide variety of magic and hybrid  items. Each item has its own rules for how it functions:  some require bespoke activatio |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/2/Text/4` | 0.532042 | **Invested:** A PC can wear only 10 magical items that  have the invested trait. A character can still gain any  normal benefit from using a physical item without  investing it, such as using a *progr |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/9` | 0.496819 | You invest your energy in an item with the invested trait  as you don it. This process requires 1 or more Interact  actions, usually taking the same amount of time it takes to  don the item. Once you' |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/7` | 0.492743 | Certain magic and hybrid items convey their benefits only  when worn and invested using the Invest an Item activity,  connecting them to a specific PC. A PC can benefit from  no more than 10 invested |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/10/Text/32` | 0.489171 | Apex augmentations can be biotech, cybernetics, or magitech.  Add the appropriate trait to the item upon crafting or purchasing. |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/20` | 0.478351 | If the activation entry for an item lists "Cast a Spell" after  "Activate", you must use the same action as casting the spell  to Activate the Item, unless noted otherwise. You must have  a spellcasti |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/2` | 0.461050 | From orbiting crystals imbued with power to gravity-defying equipment and hardlight devices, magic  items are popular accessories for adventurers and collectors. Engineers have developed fascinating |

### Query 91
- Text: What is the rule about grants a +1 item bonus to Performance checks attempted  with it.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/2/Text/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/2/Text/7', 'PZO22001 Starfinder Player Core 282-293::/page/8/Text/14', 'PZO22001 Starfinder Player Core 282-293::/page/8/Text/16']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/2/Text/7', 'PZO22001 Starfinder Player Core 282-293::/page/2/Text/6', 'PZO22001 Starfinder Player Core 282-293::/page/2/Text/8']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/2/Text/6` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/2/Text/8` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/2/Text/7` | 0.916099 | grants a +1 item bonus to Performance checks attempted  with it. |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/8/Text/14` | 0.621638 | You gain a +1 item bonus to Computers checks when accessing  a system with a tactical datajack. |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/8/Text/16` | 0.604075 | You gain a +2 item bonus to Computers checks when  accessing a system with an advanced datajack. |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/11/Text/6` | 0.513111 | This augmentation keeps your muscles in peak condition. You  gain a +3 item bonus to Athletics checks. When you get this  augmentation, you either increase your Strength modifier by 1  or increase it |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/7/Text/20` | 0.457484 | The item bonus to saving throws is +3. |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/7/Text/18` | 0.448208 | The item bonus to saving throws is +2. |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/10/Text/29` | 0.447647 | When you get an augmentation with the apex trait, it improves  one of your attributes, either increasing the attribute's modifier  by 1 or to a total of +4, whichever would give you a higher score. |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/3/Text/12` | 0.427592 | The item bonus is +2, and the *share* *pain* spell is 7th rank  (DC 34). |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/7` | 0.425565 | Certain magic and hybrid items convey their benefits only  when worn and invested using the Invest an Item activity,  connecting them to a specific PC. A PC can benefit from  no more than 10 invested |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/10/Text/41` | 0.423030 | A miniature supercomputer augments your brain's ability  to process information. You gain a +3 item bonus to checks  to Recall Knowledge with any skill. When you get this  augmentation, you either inc |

### Query 92
- Text: What is the rule about **Activate—Grand Finale** [two-actions] (auditory) **Frequency** once per  10 minutes; **Effect** Your song reaches an eardrum-bursting  climax as you cast a 1st-rank *sonic* *scream* originating  from your space (DC 18).?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/2/Text/8']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/2/Text/8', 'PZO22001 Starfinder Player Core 282-293::/page/11/Text/12', 'PZO22001 Starfinder Player Core 282-293::/page/3/Text/9']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/2/Text/8', 'PZO22001 Starfinder Player Core 282-293::/page/2/Text/9', 'PZO22001 Starfinder Player Core 282-293::/page/2/Text/7']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/2/Text/9` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/2/Text/7` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/2/Text/8` | 0.962362 | **Activate—Grand Finale** [two-actions] (auditory) **Frequency** once per  10 minutes; **Effect** Your song reaches an eardrum-bursting  climax as you cast a 1st-rank *sonic* *scream* originating  fro |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/11/Text/12` | 0.644074 | **Activate—Irresistible Idea** [two-actions] (concentrate) **Frequency** once per hour; **Effect** You manipulate your cosmetics to  influence a creature as a 4th-rank *suggestion* (DC 38). |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/3/Text/9` | 0.619039 | **Activate—Painful Memory** [two-actions] (manipulate) **Frequency** once per day; **Effect** You recite a poem of utter anguish  to spread your misery to another creature, casting a 3rdrank *share* * |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/10/Text/48` | 0.576269 | **Activate—Reground in Reality** [reaction] (concentrate, fortune)  **Frequency** once per hour; **Trigger** You fail a saving throw  against a magical effect; **Effect** You can reroll the save and |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/7/Text/59` | 0.569782 | **Activate—Accelerate** [free-action] **Frequency** once per 10 minutes;  **Trigger** You Climb, Stride, or Swim; **Effect** You increase  your Speed by 20 feet for the triggering action. |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/10/Text/22` | 0.551821 | **Activate—Regenerate** [two-actions] (concentrate) **Frequency** once  per day; **Effect** You gain the effects of a 4th-rank *genetic* *regeneration* spell. |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/6/Text/19` | 0.543182 | **Activate—Exhale** [one-action] (manipulate) **Frequency** once per  10 minutes; **Effect** Each creature in a 15-foot cone takes  damage with a basic Reflex save. The damage depends on the  augmenta |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/6` | 0.538710 | **Activate—Cosmic Luck** [reaction] (concentrate, fortune) **Frequency** once per day; **Trigger** You critically fail an attack roll,  saving throw, or skill check; **Effect** You change the critical |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/4/Text/6` | 0.533716 | **Activate—Inject** [one-action] (manipulate) **Effect** You Cast the Spell at  the indicated rank. |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/24` | 0.530108 | **Activate—Database Scan** [two-actions] (concentrate) **Frequency** once  per 10 minutes; **Effect** The lens casts a 1st-rank *Akashic* *download* that uses the lens instead of a comm unit. |

### Query 93
- Text: Summarize **Type **commercial; **Level **4; **Price **750 credits
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/2/Text/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/2/Text/9', 'PZO22001 Starfinder Player Core 282-293::/page/9/Text/11', 'PZO22001 Starfinder Player Core 282-293::/page/7/Text/16']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/2/Text/9', 'PZO22001 Starfinder Player Core 282-293::/page/2/Text/8', 'PZO22001 Starfinder Player Core 282-293::/page/2/Text/10']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/2/Text/8` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/2/Text/10` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/2/Text/9` | 1.038642 | **Type **commercial; **Level **4; **Price **750 credits |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/9/Text/11` | 0.927967 | **Type **commercial; **Level **4; **Price **800 credits |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/7/Text/16` | 0.895240 | **Type **commercial; **Level **8; **Price **3,450 credits |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/3/Text/10` | 0.842033 | **Type **commercial; **Level **7; **Price **3,333 credits |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/8/Text/12` | 0.839657 | **Type **commercial; **Level **1; **Price **100 credits |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/3/Text/19` | 0.839522 | **Type **commercial; **Level **3; **Price **550 credits |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/25` | 0.836336 | **Type **commercial; **Level **3; **Price **555 credits |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/8/Text/21` | 0.833392 | **Type **commercial; **Level **1; **Price **180 credits |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/9/Text/31` | 0.832910 | **Type **commercial; **Level **8; **Price **5,000 credits |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/8/Text/41` | 0.829572 | **Type **commercial; **Level **1; **Price **140 credits |

### Query 94
- Text: What is the rule about **Type **tactical; **Level **10; **Price **9,500 credits?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/2/Text/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/2/Text/10', 'PZO22001 Starfinder Player Core 282-293::/page/9/Text/32', 'PZO22001 Starfinder Player Core 282-293::/page/8/Text/6']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/2/Text/10', 'PZO22001 Starfinder Player Core 282-293::/page/2/Text/9', 'PZO22001 Starfinder Player Core 282-293::/page/2/Text/11']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/2/Text/9` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/2/Text/11` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/2/Text/10` | 0.902113 | **Type **tactical; **Level **10; **Price **9,500 credits |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/9/Text/32` | 0.850931 | **Type **tactical; **Level **10; **Price **10,000 credits |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/8/Text/6` | 0.771380 | **Type **tactical; **Level **5; **Price **1,600 credits |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/8/Text/42` | 0.727207 | **Type **tactical; **Level **5; **Price **1,400 credits |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/36` | 0.725375 | **Type **tactical; **Level **12; **Price **16,500 credits |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/3/Text/20` | 0.720513 | **Type **tactical; **Level **8; **Price **4,550 credits |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/7/Text/26` | 0.715958 | **Type **tactical; **Level **6; **Price **2,500 credits |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/3/Text/11` | 0.706074 | **Type **tactical; **Level **15; **Price **66,666 credits |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/9/Text/12` | 0.690350 | **Type **tactical; **Level **8; **Price **4,000 credits Increase the item bonus to 10-feet. |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/10/Text/16` | 0.688918 | **Type **tactical;** Level **6; **Price **2,250 credits |

### Query 95
- Text: What is the rule about The item bonus is +2, and the *sonic* *scream* spell is 4th rank  (DC 27).?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/2/Text/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/2/Text/11', 'PZO22001 Starfinder Player Core 282-293::/page/2/Text/13', 'PZO22001 Starfinder Player Core 282-293::/page/3/Text/12']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/2/Text/11', 'PZO22001 Starfinder Player Core 282-293::/page/2/Text/12', 'PZO22001 Starfinder Player Core 282-293::/page/2/Text/10']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/2/Text/12` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/2/Text/10` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/2/Text/11` | 0.947934 | The item bonus is +2, and the *sonic* *scream* spell is 4th rank  (DC 27). |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/2/Text/13` | 0.903101 | The item bonus is +3, and the *sonic* *scream* spell is 8th rank  (DC 38). |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/3/Text/12` | 0.664992 | The item bonus is +2, and the *share* *pain* spell is 7th rank  (DC 34). |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/3/Text/21` | 0.611954 | The item bonus is +2, and the *lock* spell is 3rd rank (DC 25). |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/3/Text/23` | 0.600291 | The item bonus is +3, and the *lock* spell is 7th rank (DC 35). |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/28` | 0.573795 | The item bonus is +2, and the *Akashic* *download* spell is 4th  rank. |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/4/Text/7` | 0.487924 | **Type ***cellular* *stimulant* *spell amp*; **Level **1; **Price **30 credits;  **Effect** 1st-rank *cellular* *stimulant* spell (DC 15) |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/4/Text/16` | 0.484974 | **Type ***commercial* *cairn* *form* *spell* *amp*; **Level **7; **Price **720  credits; **Effect** 4th-rank *cairn* *form* spell |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/4/Text/10` | 0.484122 | **Type ***shrink* *spell* *amp*; **Level **3; **Price **120 credits; **Effect** 2ndrank *shrink* spell |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/4/Text/48` | 0.479528 | **Type*** 4th-rank spell gem*; **Level **7; **Price **700 credits |

### Query 96
- Text: What is the rule about The item bonus is +3, and the *sonic* *scream* spell is 8th rank  (DC 38).?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/2/Text/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/2/Text/13', 'PZO22001 Starfinder Player Core 282-293::/page/2/Text/11', 'PZO22001 Starfinder Player Core 282-293::/page/3/Text/12']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/2/Text/13', 'PZO22001 Starfinder Player Core 282-293::/page/2/Text/12', 'PZO22001 Starfinder Player Core 282-293::/page/2/SectionHeader/14']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/2/Text/12` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/2/SectionHeader/14` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/2/Text/13` | 0.942987 | The item bonus is +3, and the *sonic* *scream* spell is 8th rank  (DC 38). |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/2/Text/11` | 0.900291 | The item bonus is +2, and the *sonic* *scream* spell is 4th rank  (DC 27). |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/3/Text/12` | 0.647963 | The item bonus is +2, and the *share* *pain* spell is 7th rank  (DC 34). |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/3/Text/23` | 0.598504 | The item bonus is +3, and the *lock* spell is 7th rank (DC 35). |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/3/Text/21` | 0.591287 | The item bonus is +2, and the *lock* spell is 3rd rank (DC 25). |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/28` | 0.540364 | The item bonus is +2, and the *Akashic* *download* spell is 4th  rank. |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/4/Text/7` | 0.495104 | **Type ***cellular* *stimulant* *spell amp*; **Level **1; **Price **30 credits;  **Effect** 1st-rank *cellular* *stimulant* spell (DC 15) |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/4/Text/20` | 0.483002 | **Type ***tactical* *cairn* *form* *spell* *amp*; **Level **11; **Price **3,200  credits; **Effect** 6th-rank *cairn* *form* spell |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/4/Text/10` | 0.481570 | **Type ***shrink* *spell* *amp*; **Level **3; **Price **120 credits; **Effect** 2ndrank *shrink* spell |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/4/Text/16` | 0.473340 | **Type ***commercial* *cairn* *form* *spell* *amp*; **Level **7; **Price **720  credits; **Effect** 4th-rank *cairn* *form* spell |

### Query 97
- Text: What is the rule about This magitech interface is a sophisticated pair of linked  bracers, wristbands, gloves, or other garments suitable to  the part of a creature's anatomy it uses to wield weapons.  One of the paired enhancers includes a screen that displays  data about the weapons the wearer is wielding, and the  other enhancer contains magical crystals. When you wield  a weapon in the hand wearing the display, the weapon's  grade (such as tactical) is replicated onto the weapon you're  wielding in the hand with the crystal enhancer, but only for  purposes of determining the weapon's extra damage dice  and tracking trait (which adds an item bonus to attack rolls).  Any other properties of the weapon, such as its damage  type, ammo, or upgrades, aren't replicated.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/2/Text/19']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/2/Text/19', 'PZO22001 Starfinder Player Core 282-293::/page/2/Text/20', 'PZO22001 Starfinder Player Core 282-293::/page/9/Text/25']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/2/Text/19', 'PZO22001 Starfinder Player Core 282-293::/page/2/Text/20', 'PZO22001 Starfinder Player Core 282-293::/page/2/Text/18']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/2/Text/20` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/2/Text/18` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/2/Text/19` | 0.965572 | This magitech interface is a sophisticated pair of linked  bracers, wristbands, gloves, or other garments suitable to  the part of a creature's anatomy it uses to wield weapons.  One of the paired enh |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/2/Text/20` | 0.661107 | The replication functions only if you wear both enhancers,  and it ends as soon as you cease wielding a weapon in one  of your hands. Consequently, the benefit doesn't apply to  thrown attacks or if y |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/9/Text/25` | 0.599059 | Magitech augmentations are a combination of cybernetic and  magical components, created with special-made elements  like mystically charged crystals, starmetal alloys, and runeengraved microchips. Mag |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/10/Text/32` | 0.520324 | Apex augmentations can be biotech, cybernetics, or magitech.  Add the appropriate trait to the item upon crafting or purchasing. |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/2/Text/5` | 0.509549 | **Magical:** Items with the magical trait can be crafted  only if a player has the Magical Crafting feat (page 224). |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/2/Text/6` | 0.498272 | **Tech:** Items with the tech trait can be crafted by  anyone, but if they're level 1 or higher, they require  the Tech Crafting feat (page 229) to craft. If a tech  item also has the magical trait, t |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/2/Text/4` | 0.493580 | **Invested:** A PC can wear only 10 magical items that  have the invested trait. A character can still gain any  normal benefit from using a physical item without  investing it, such as using a *progr |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/6/Text/2` | 0.491441 | Many explorers and mercenaries modify their bodies with technological or biological gear called  augmentations. These modifications to your body give you special abilities and bonuses. Once  installed |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/5` | 0.481998 | The tables on pages 286–287 list level, price, Bulk,  and hands entries for a wide variety of magic and hybrid  items. Each item has its own rules for how it functions:  some require bespoke activatio |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/2/Text/26` | 0.475038 | Higher-level *hardlight* *handwraps* also apply the tracking  trait and increase the damage dice of your unarmed attacks.  For example, *advanced* *hardlight* *handwraps* increase your  unarmed attack |

### Query 98
- Text: What is the rule about The replication functions only if you wear both enhancers,  and it ends as soon as you cease wielding a weapon in one  of your hands. Consequently, the benefit doesn't apply to  thrown attacks or if you're holding a weapon but not wielding  it (such as holding in one hand a weapon that requires two  hands to wield, or holding a weapon in non-active hands).?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/2/Text/20']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/2/Text/20', 'PZO22001 Starfinder Player Core 282-293::/page/2/Text/19', 'PZO22001 Starfinder Player Core 282-293::/page/0/Text/16']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/2/Text/20', 'PZO22001 Starfinder Player Core 282-293::/page/2/SectionHeader/21', 'PZO22001 Starfinder Player Core 282-293::/page/2/Text/19']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/2/SectionHeader/21` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/2/Text/19` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/2/Text/20` | 1.007694 | The replication functions only if you wear both enhancers,  and it ends as soon as you cease wielding a weapon in one  of your hands. Consequently, the benefit doesn't apply to  thrown attacks or if y |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/2/Text/19` | 0.591354 | This magitech interface is a sophisticated pair of linked  bracers, wristbands, gloves, or other garments suitable to  the part of a creature's anatomy it uses to wield weapons.  One of the paired enh |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/16` | 0.547665 | If the activation entry for an item has the manipulate trait,  you can activate it only if you're holding the item or touching  it with a free hand. |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/8/Text/43` | 0.484839 | When you use Draw, if the item can be activated or otherwise  used with a single action, you can use the item as part of the  same action. For example, you Interact to draw a weapon, then  Strike with |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/6/Text/12` | 0.466651 | Many augmentations work continuously. Augmentations  with an Activate entry usually require you to concentrate or  Interact to gain an additional boost or ability. Once activated,  an augmentation oft |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/8/Text/40` | 0.449748 | **Activate—Draw** [one-action] (manipulate) **Effect** You Interact to draw  an item concealed in your hideaway limb. |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/10/Text/31` | 0.449573 | You can only gain an attribute increase from one apex  augmentation, though you do gain any other effects or abilities  of other installed apex augmentations If you have multiple  apex augmentations, |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/12` | 0.443020 | While some items function automatically and grant constant  benefits, others produce effects only when properly used. An  activation lists the number of actions it takes and any traits  of the activat |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/0/Text/20` | 0.436843 | If the activation entry for an item lists "Cast a Spell" after  "Activate", you must use the same action as casting the spell  to Activate the Item, unless noted otherwise. You must have  a spellcasti |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/4/Text/6` | 0.432124 | **Activate—Inject** [one-action] (manipulate) **Effect** You Cast the Spell at  the indicated rank. |

### Query 99
- Text: What is the rule about These handwraps can be customized to shine in any color in  the visible spectrum when used, and some manufacturers  offer custom firmware that modifies their appearance to  manifest as a claw, oversized fist, or hammerhead. They  can even be worn in alternate ways on other parts of the  body. These handwraps enhance your unarmed attacks as  if they were manufactured weapons, allowing you to add  an upgrade to your unarmed attacks. Treat the handwraps  as melee weapons in the brawling group with light Bulk for  these purposes.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/2/Text/25']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/2/Text/25', 'PZO22001 Starfinder Player Core 282-293::/page/2/Text/26', 'PZO22001 Starfinder Player Core 282-293::/page/5/TableCell/1133']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/2/Text/25', 'PZO22001 Starfinder Player Core 282-293::/page/2/Text/26', 'PZO22001 Starfinder Player Core 282-293::/page/2/Text/24']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/2/Text/26` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/2/Text/24` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/2/Text/25` | 1.006334 | These handwraps can be customized to shine in any color in  the visible spectrum when used, and some manufacturers  offer custom firmware that modifies their appearance to  manifest as a claw, oversiz |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/2/Text/26` | 0.691597 | Higher-level *hardlight* *handwraps* also apply the tracking  trait and increase the damage dice of your unarmed attacks.  For example, *advanced* *hardlight* *handwraps* increase your  unarmed attack |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/5/TableCell/1133` | 0.597494 | Hardlight handwraps, tactical |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/5/TableCell/1178` | 0.522054 | Hardlight handwraps, advanced |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/5/TableCell/1408` | 0.520428 | Hardlight handwraps, ultimate |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/5/TableCell/1308` | 0.510032 | Hardlight handwraps, superior |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/6/Text/2` | 0.508983 | Many explorers and mercenaries modify their bodies with technological or biological gear called  augmentations. These modifications to your body give you special abilities and bonuses. Once  installed |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/2/Text/19` | 0.503541 | This magitech interface is a sophisticated pair of linked  bracers, wristbands, gloves, or other garments suitable to  the part of a creature's anatomy it uses to wield weapons.  One of the paired enh |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/1/Text/33` | 0.499309 | This convoluted web of synthweave straps is worn as a  fashion statement in some subcultures but has a useful  application in extreme environments. You gain a +1 item  bonus to Acrobatics checks, and |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/5/TableCell/1343` | 0.495650 | Hardlight handwraps, elite |

### Query 100
- Text: Lookup values for ItemLevelPriceBulkHandsHardlight handwraps,
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/4/Table/56']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/4/Table/56', 'PZO22001 Starfinder Player Core 282-293::/page/5/TableCell/1178', 'PZO22001 Starfinder Player Core 282-293::/page/2/SectionHeader/21']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/4/Table/56', 'PZO22001 Starfinder Player Core 282-293::/page/4/TableCell/831', 'PZO22001 Starfinder Player Core 282-293::/page/4/SectionHeader/55']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/4/TableCell/831` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/4/SectionHeader/55` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/4/Table/56` | 0.758778 | ItemLevelPriceBulkHandsHardlight handwraps, commercial05——1st-rank spell gem140——Cellular stimulant spell amp130L1 |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/5/TableCell/1178` | 0.692030 | Hardlight handwraps, advanced |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/2/SectionHeader/21` | 0.682689 | **HARDLIGHT HANDWRAPS** **ITEM 2+** |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/5/TableCell/1308` | 0.632411 | Hardlight handwraps, superior |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/5/TableCell/1408` | 0.629368 | Hardlight handwraps, ultimate |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/5/TableCell/1343` | 0.614698 | Hardlight handwraps, elite |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/4/TableCell/836` | 0.610834 | Hardlight handwraps, commercial |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/5/Table/2` | 0.608243 | ItemLevelPriceBulkHandsGlow up spell amp, advanced91,100L1Diva's microphone, tactical109,500L1Hardlight handwraps, superior1010,005——Resist energy spell amp, tactical101,800L15th-rank spell chip1115,0 |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/5/TableCell/1133` | 0.607738 | Hardlight handwraps, tactical |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/5/Table/1` | 0.579990 | ItemLevelPriceBulkHandsGlow up spell amp,commercial150L1Reusable grenade shell18011Hardlight handwraps, tactical2355——Jump spell amp260L11st-rank spell chip3600——2nd-rank spell gem3120——Akashic lens, |

### Query 101
- Text: Lookup values for ItemLevelPriceBulkHandsGlow up spell amp,commercial150L1Reusable grenade
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/5/Table/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/5/Table/1', 'PZO22001 Starfinder Player Core 282-293::/page/4/Table/56', 'PZO22001 Starfinder Player Core 282-293::/page/5/Table/2']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/5/Table/1', 'PZO22001 Starfinder Player Core 282-293::/page/5/SectionHeader/0', 'PZO22001 Starfinder Player Core 282-293::/page/5/TableCell/1113']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/5/SectionHeader/0` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/5/TableCell/1113` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/5/Table/1` | 0.785625 | ItemLevelPriceBulkHandsGlow up spell amp,commercial150L1Reusable grenade shell18011Hardlight handwraps, tactical2355——Jump spell amp260L11st-rank spell chip3600——2nd-rank spell gem3120——Akashic lens, |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/4/Table/56` | 0.678012 | ItemLevelPriceBulkHandsHardlight handwraps, commercial05——1st-rank spell gem140——Cellular stimulant spell amp130L1 |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/5/Table/2` | 0.666681 | ItemLevelPriceBulkHandsGlow up spell amp, advanced91,100L1Diva's microphone, tactical109,500L1Hardlight handwraps, superior1010,005——Resist energy spell amp, tactical101,800L15th-rank spell chip1115,0 |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/5/TableCell/1208` | 0.589901 | Glow up spell amp, tactical |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/5/TableCell/1118` | 0.581986 | Glow up spell amp, |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/5/TableCell/1298` | 0.576638 | Glow up spell amp, advanced |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/4/Text/8` | 0.539297 | **Type ***commercial* *glow* *up* *spell* *amp*; **Level **1; **Price **50 credits;  **Effect** 1st-rank *glow* *up* spell |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/4/Text/12` | 0.489656 | **Type ***tactical* *glow* *up* *spell* *amp*; **Level **5; **Price **210 credits;  **Effect** 3rd-rank *glow* *up* spell |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/5/TableCell/1223` | 0.482379 | Resist energy spell amp, commercial |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/4/Text/18` | 0.472279 | **Type ***advanced* *glow* *up* *spell* *amp*; **Level **9; **Price **1,100  credits; **Effect** 5th-rank *glow* *up* spell |

### Query 102
- Text: Lookup values for ItemLevelPriceBulkHandsGlow up spell amp,
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/5/Table/2']
- Expected found: `True`
- Expected rank: `4`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/5/Table/1', 'PZO22001 Starfinder Player Core 282-293::/page/5/TableCell/1118', 'PZO22001 Starfinder Player Core 282-293::/page/5/TableCell/1298']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/5/Table/2', 'PZO22001 Starfinder Player Core 282-293::/page/5/TableCell/1293', 'PZO22001 Starfinder Player Core 282-293::/page/5/TableCell/1287']
- Expanded expected found: `True`
- Expanded expected rank: `4`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/5/TableCell/1293` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/5/TableCell/1287` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/5/Table/1` | 0.761172 | ItemLevelPriceBulkHandsGlow up spell amp,commercial150L1Reusable grenade shell18011Hardlight handwraps, tactical2355——Jump spell amp260L11st-rank spell chip3600——2nd-rank spell gem3120——Akashic lens, |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/5/TableCell/1118` | 0.759940 | Glow up spell amp, |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/5/TableCell/1298` | 0.730894 | Glow up spell amp, advanced |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/5/Table/2` | 0.663638 | ItemLevelPriceBulkHandsGlow up spell amp, advanced91,100L1Diva's microphone, tactical109,500L1Hardlight handwraps, superior1010,005——Resist energy spell amp, tactical101,800L15th-rank spell chip1115,0 |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/4/Table/56` | 0.639953 | ItemLevelPriceBulkHandsHardlight handwraps, commercial05——1st-rank spell gem140——Cellular stimulant spell amp130L1 |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/5/TableCell/1208` | 0.635310 | Glow up spell amp, tactical |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/4/Text/18` | 0.562876 | **Type ***advanced* *glow* *up* *spell* *amp*; **Level **9; **Price **1,100  credits; **Effect** 5th-rank *glow* *up* spell |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/4/Text/8` | 0.561953 | **Type ***commercial* *glow* *up* *spell* *amp*; **Level **1; **Price **50 credits;  **Effect** 1st-rank *glow* *up* spell |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/4/Text/12` | 0.538259 | **Type ***tactical* *glow* *up* *spell* *amp*; **Level **5; **Price **210 credits;  **Effect** 3rd-rank *glow* *up* spell |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/5/TableCell/1168` | 0.523445 | Shrink spell amp |

### Query 103
- Text: Lookup values for ItemLevelPriceDragon gland, commercial1150Gill sheath1200Dragon gland, tactical2300Photosynthetic skin2300Venom spur2320Wildwise graft2250Ultralight wings, commercial3600Laser eye4770Ultralight wings, tactical62,500Dragon gland, advanced73,300Shielding skin, commercial83,450Ultralight wings, advanced97,000Dragon gland, superior1218,200Ultralight wings, superior1220,000Shielding skin, tactical1435,000Dragon gland, elite17135,000
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/11/Table/14']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/11/Table/14', 'PZO22001 Starfinder Player Core 282-293::/page/11/Table/15', 'PZO22001 Starfinder Player Core 282-293::/page/11/Table/17']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/11/Table/14', 'PZO22001 Starfinder Player Core 282-293::/page/11/TableCell/731', 'PZO22001 Starfinder Player Core 282-293::/page/11/SectionHeader/13']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/11/TableCell/731` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/11/SectionHeader/13` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/11/Table/14` | 1.035616 | ItemLevelPriceDragon gland, commercial1150Gill sheath1200Dragon gland, tactical2300Photosynthetic skin2300Venom spur2320Wildwise graft2250Ultralight wings, commercial3600Laser eye4770Ultralight wings, |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/11/Table/15` | 0.788569 | ItemLevelPriceDragon gland, ultimate20610,000Shielding skin, advanced20495,000 |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/11/Table/17` | 0.715935 | ItemLevelPriceAutorecognition lens05Hearing aid05Prosthetic limb05Datajack, commercial1100Dermal plating, commercial1180Hideaway limb, commercial1140Retinal reflectors1200Vocal modulator190Darkvision |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/11/Table/19` | 0.636827 | ItemLevelPriceMoodskin035Telepathy node1200Psychoactive eyes, commercial3500Psychoactive eyes, tactical62,250Cloaking skin, commercial85,000Regenerative rune splice96,500Cloaking skin, tactical1010,00 |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/5/Table/2` | 0.620853 | ItemLevelPriceBulkHandsGlow up spell amp, advanced91,100L1Diva's microphone, tactical109,500L1Hardlight handwraps, superior1010,005——Resist energy spell amp, tactical101,800L15th-rank spell chip1115,0 |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/5/Table/1` | 0.606544 | ItemLevelPriceBulkHandsGlow up spell amp,commercial150L1Reusable grenade shell18011Hardlight handwraps, tactical2355——Jump spell amp260L11st-rank spell chip3600——2nd-rank spell gem3120——Akashic lens, |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/11/TableCell/761` | 0.523411 | Dragon gland, advanced |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/11/TableCell/740` | 0.518685 | Dragon gland, tactical |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/11/Table/21` | 0.515190 | ItemLevelPriceArtificial immortalizer17150,000Cognition accelerator17150,000Cosmic connector17150,000Hypernerves17150,000Muscle invigorator17150,000Presence intensifier17150,000 |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/3/Text/2` | 0.499961 | **Type **commercial; **Level **4; **Price **750 credits; **Capacity** 25 Bulk **Type **tactical; **Level **7; **Price **3,000 credits; **Capacity** 50 Bulk **Type **advanced; **Level **11; **Price **1 |

### Query 104
- Text: Lookup values for ItemLevelPriceDragon gland, ultimate20610,000Shielding skin, advanced20495,000
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/11/Table/15']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/11/Table/15', 'PZO22001 Starfinder Player Core 282-293::/page/11/Table/14', 'PZO22001 Starfinder Player Core 282-293::/page/11/TableCell/785']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/11/Table/15', 'PZO22001 Starfinder Player Core 282-293::/page/11/TableCell/782', 'PZO22001 Starfinder Player Core 282-293::/page/11/TableCell/781']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/11/TableCell/782` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/11/TableCell/781` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/11/Table/15` | 1.025254 | ItemLevelPriceDragon gland, ultimate20610,000Shielding skin, advanced20495,000 |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/11/Table/14` | 0.801426 | ItemLevelPriceDragon gland, commercial1150Gill sheath1200Dragon gland, tactical2300Photosynthetic skin2300Venom spur2320Wildwise graft2250Ultralight wings, commercial3600Laser eye4770Ultralight wings, |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/11/TableCell/785` | 0.648845 | Dragon gland, ultimate |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/11/TableCell/761` | 0.598436 | Dragon gland, advanced |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/5/Table/2` | 0.580170 | ItemLevelPriceBulkHandsGlow up spell amp, advanced91,100L1Diva's microphone, tactical109,500L1Hardlight handwraps, superior1010,005——Resist energy spell amp, tactical101,800L15th-rank spell chip1115,0 |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/11/TableCell/788` | 0.563973 | Shielding skin, advanced |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/11/Table/19` | 0.559699 | ItemLevelPriceMoodskin035Telepathy node1200Psychoactive eyes, commercial3500Psychoactive eyes, tactical62,250Cloaking skin, commercial85,000Regenerative rune splice96,500Cloaking skin, tactical1010,00 |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/11/Table/17` | 0.521453 | ItemLevelPriceAutorecognition lens05Hearing aid05Prosthetic limb05Datajack, commercial1100Dermal plating, commercial1180Hideaway limb, commercial1140Retinal reflectors1200Vocal modulator190Darkvision |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/8/Text/28` | 0.516738 | **Type **ultimate; **Level **16; **Price **90,000 credits The dermal plating has Hardness 30. |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/6/Text/26` | 0.513798 | **Type **ultimate; **Level **20; **Price **610,000 credits The damage is 14d6 and the DC is 43. |

### Query 105
- Text: Lookup values for ItemLevelPriceAutorecognition lens05Hearing aid05Prosthetic limb05Datajack, commercial1100Dermal plating, commercial1180Hideaway limb, commercial1140Retinal reflectors1200Vocal modulator190Darkvision capacitors, commercial3600Voice amplifier3500Datajack, tactical4750Dermal plating, tactical4900Speed suspension, commercial4800Cardiac accelerator51,300Darkvision capacitors, tactical51,600Hideaway limb, tactical51,400Dermal plating, advanced73,240Datajack, advanced84,200Speed suspension, tactical84,000Dermal plating, superior109,000Autodreamer1113,000Nano-optics node1112,000Speed suspension, advanced1216,000Dermal plating, elite1327,000Dermal plating, ultimate1690,000Dermal plating, paragon19360,000
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/11/Table/17']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/11/Table/17', 'PZO22001 Starfinder Player Core 282-293::/page/11/Table/14', 'PZO22001 Starfinder Player Core 282-293::/page/11/Table/19']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/11/Table/17', 'PZO22001 Starfinder Player Core 282-293::/page/11/SectionHeader/16', 'PZO22001 Starfinder Player Core 282-293::/page/11/TableCell/791']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/11/SectionHeader/16` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/11/TableCell/791` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/11/Table/17` | 1.040572 | ItemLevelPriceAutorecognition lens05Hearing aid05Prosthetic limb05Datajack, commercial1100Dermal plating, commercial1180Hideaway limb, commercial1140Retinal reflectors1200Vocal modulator190Darkvision |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/11/Table/14` | 0.712195 | ItemLevelPriceDragon gland, commercial1150Gill sheath1200Dragon gland, tactical2300Photosynthetic skin2300Venom spur2320Wildwise graft2250Ultralight wings, commercial3600Laser eye4770Ultralight wings, |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/11/Table/19` | 0.654646 | ItemLevelPriceMoodskin035Telepathy node1200Psychoactive eyes, commercial3500Psychoactive eyes, tactical62,250Cloaking skin, commercial85,000Regenerative rune splice96,500Cloaking skin, tactical1010,00 |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/11/Table/21` | 0.609496 | ItemLevelPriceArtificial immortalizer17150,000Cognition accelerator17150,000Cosmic connector17150,000Hypernerves17150,000Muscle invigorator17150,000Presence intensifier17150,000 |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/5/Table/1` | 0.605578 | ItemLevelPriceBulkHandsGlow up spell amp,commercial150L1Reusable grenade shell18011Hardlight handwraps, tactical2355——Jump spell amp260L11st-rank spell chip3600——2nd-rank spell gem3120——Akashic lens, |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/5/Table/2` | 0.602943 | ItemLevelPriceBulkHandsGlow up spell amp, advanced91,100L1Diva's microphone, tactical109,500L1Hardlight handwraps, superior1010,005——Resist energy spell amp, tactical101,800L15th-rank spell chip1115,0 |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/8/Text/22` | 0.511374 | **Type **tactical; **Level **4; **Price **900 credits The dermal plating has Hardness 10. |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/11/Table/15` | 0.495839 | ItemLevelPriceDragon gland, ultimate20610,000Shielding skin, advanced20495,000 |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/3/Text/2` | 0.491507 | **Type **commercial; **Level **4; **Price **750 credits; **Capacity** 25 Bulk **Type **tactical; **Level **7; **Price **3,000 credits; **Capacity** 50 Bulk **Type **advanced; **Level **11; **Price **1 |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/4/Table/56` | 0.488896 | ItemLevelPriceBulkHandsHardlight handwraps, commercial05——1st-rank spell gem140——Cellular stimulant spell amp130L1 |

### Query 106
- Text: Lookup values for ItemLevelPriceMoodskin035Telepathy node1200Psychoactive eyes, commercial3500Psychoactive eyes, tactical62,250Cloaking skin, commercial85,000Regenerative rune splice96,500Cloaking skin, tactical1010,000Cloaking skin, advanced1220,000
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/11/Table/19']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/11/Table/19', 'PZO22001 Starfinder Player Core 282-293::/page/11/Table/14', 'PZO22001 Starfinder Player Core 282-293::/page/11/Table/17']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/11/Table/19', 'PZO22001 Starfinder Player Core 282-293::/page/11/TableCell/872', 'PZO22001 Starfinder Player Core 282-293::/page/11/SectionHeader/18']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/11/TableCell/872` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/11/SectionHeader/18` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/11/Table/19` | 1.036992 | ItemLevelPriceMoodskin035Telepathy node1200Psychoactive eyes, commercial3500Psychoactive eyes, tactical62,250Cloaking skin, commercial85,000Regenerative rune splice96,500Cloaking skin, tactical1010,00 |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/11/Table/14` | 0.680015 | ItemLevelPriceDragon gland, commercial1150Gill sheath1200Dragon gland, tactical2300Photosynthetic skin2300Venom spur2320Wildwise graft2250Ultralight wings, commercial3600Laser eye4770Ultralight wings, |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/11/Table/17` | 0.666550 | ItemLevelPriceAutorecognition lens05Hearing aid05Prosthetic limb05Datajack, commercial1100Dermal plating, commercial1180Hideaway limb, commercial1140Retinal reflectors1200Vocal modulator190Darkvision |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/11/Table/21` | 0.565957 | ItemLevelPriceArtificial immortalizer17150,000Cognition accelerator17150,000Cosmic connector17150,000Hypernerves17150,000Muscle invigorator17150,000Presence intensifier17150,000 |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/5/Table/1` | 0.555205 | ItemLevelPriceBulkHandsGlow up spell amp,commercial150L1Reusable grenade shell18011Hardlight handwraps, tactical2355——Jump spell amp260L11st-rank spell chip3600——2nd-rank spell gem3120——Akashic lens, |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/5/Table/2` | 0.551791 | ItemLevelPriceBulkHandsGlow up spell amp, advanced91,100L1Diva's microphone, tactical109,500L1Hardlight handwraps, superior1010,005——Resist energy spell amp, tactical101,800L15th-rank spell chip1115,0 |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/11/Table/15` | 0.541973 | ItemLevelPriceDragon gland, ultimate20610,000Shielding skin, advanced20495,000 |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/3/Text/2` | 0.492400 | **Type **commercial; **Level **4; **Price **750 credits; **Capacity** 25 Bulk **Type **tactical; **Level **7; **Price **3,000 credits; **Capacity** 50 Bulk **Type **advanced; **Level **11; **Price **1 |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/8/Text/22` | 0.485816 | **Type **tactical; **Level **4; **Price **900 credits The dermal plating has Hardness 10. |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/11/TableCell/884` | 0.474602 | Psychoactive eyes, tactical |

### Query 107
- Text: Lookup values for ItemLevelPriceArtificial immortalizer17150,000Cognition accelerator17150,000Cosmic connector17150,000Hypernerves17150,000Muscle invigorator17150,000Presence intensifier17150,000
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/11/Table/21']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 282-293::/page/11/Table/21', 'PZO22001 Starfinder Player Core 282-293::/page/11/Table/17', 'PZO22001 Starfinder Player Core 282-293::/page/11/Table/19']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 282-293::/page/11/Table/21', 'PZO22001 Starfinder Player Core 282-293::/page/11/TableCell/899', 'PZO22001 Starfinder Player Core 282-293::/page/11/SectionHeader/20']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 282-293::/page/11/TableCell/899` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 282-293::/page/11/SectionHeader/20` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 282-293::/page/11/Table/21` | 1.030115 | ItemLevelPriceArtificial immortalizer17150,000Cognition accelerator17150,000Cosmic connector17150,000Hypernerves17150,000Muscle invigorator17150,000Presence intensifier17150,000 |
| 2 | `PZO22001 Starfinder Player Core 282-293::/page/11/Table/17` | 0.659743 | ItemLevelPriceAutorecognition lens05Hearing aid05Prosthetic limb05Datajack, commercial1100Dermal plating, commercial1180Hideaway limb, commercial1140Retinal reflectors1200Vocal modulator190Darkvision |
| 3 | `PZO22001 Starfinder Player Core 282-293::/page/11/Table/19` | 0.605089 | ItemLevelPriceMoodskin035Telepathy node1200Psychoactive eyes, commercial3500Psychoactive eyes, tactical62,250Cloaking skin, commercial85,000Regenerative rune splice96,500Cloaking skin, tactical1010,00 |
| 4 | `PZO22001 Starfinder Player Core 282-293::/page/5/Table/1` | 0.560480 | ItemLevelPriceBulkHandsGlow up spell amp,commercial150L1Reusable grenade shell18011Hardlight handwraps, tactical2355——Jump spell amp260L11st-rank spell chip3600——2nd-rank spell gem3120——Akashic lens, |
| 5 | `PZO22001 Starfinder Player Core 282-293::/page/5/Table/2` | 0.546643 | ItemLevelPriceBulkHandsGlow up spell amp, advanced91,100L1Diva's microphone, tactical109,500L1Hardlight handwraps, superior1010,005——Resist energy spell amp, tactical101,800L15th-rank spell chip1115,0 |
| 6 | `PZO22001 Starfinder Player Core 282-293::/page/11/Table/14` | 0.520579 | ItemLevelPriceDragon gland, commercial1150Gill sheath1200Dragon gland, tactical2300Photosynthetic skin2300Venom spur2320Wildwise graft2250Ultralight wings, commercial3600Laser eye4770Ultralight wings, |
| 7 | `PZO22001 Starfinder Player Core 282-293::/page/3/Text/2` | 0.492808 | **Type **commercial; **Level **4; **Price **750 credits; **Capacity** 25 Bulk **Type **tactical; **Level **7; **Price **3,000 credits; **Capacity** 50 Bulk **Type **advanced; **Level **11; **Price **1 |
| 8 | `PZO22001 Starfinder Player Core 282-293::/page/11/Table/15` | 0.492042 | ItemLevelPriceDragon gland, ultimate20610,000Shielding skin, advanced20495,000 |
| 9 | `PZO22001 Starfinder Player Core 282-293::/page/11/TableCell/902` | 0.485983 | Artificial immortalizer |
| 10 | `PZO22001 Starfinder Player Core 282-293::/page/10/SectionHeader/43` | 0.483731 | **COSMIC CONNECTOR** **AUGMENTATION 17** |
