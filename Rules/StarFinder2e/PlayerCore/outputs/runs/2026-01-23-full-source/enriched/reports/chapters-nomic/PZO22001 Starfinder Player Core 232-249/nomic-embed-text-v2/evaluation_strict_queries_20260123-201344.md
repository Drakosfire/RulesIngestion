# RulesLawyer Evaluation Report: nomic-embed-text-v2

## Summary
- Run ID: `None`
- Ruleset ID: `None`
- Document ID: `None`
- Chunk source: `enriched`
- Chunk count: `1526`
- Query count: `121`
- Evaluated queries: `121`
- Coverage: `1.0000`
- MRR: `0.7517`
- hit@1: `0.6777`
- hit@3: `0.7851`
- hit@5: `0.8512`
- hit@10: `0.9256`
- Embeddings reused: `False`
- Graph boost: `0.05` (depth=2, top_k=50, source=top, seed_top_n=3, same_kind_only=False, decay=0.4)

## Timings (ms)
- Embedding (chunks): `16970`
- Embedding (queries): `3070`
- Evaluation (strict): `121`
- Evaluation (expanded): `0`
- Total: `24584`

### Timing Estimates (ms)
- Evaluation (strict): `121`
- Evaluation (expanded): `None`
- Total: `20161`

## Query Details
### Query 0
- Text: Summarize CHAPTER 6: EQUIPMENT
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/1/SectionHeader/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/1/SectionHeader/1', 'PZO22001 Starfinder Player Core 232-249::/page/11/Text/47', 'PZO22001 Starfinder Player Core 232-249::/page/7/Text/18']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/1/SectionHeader/1` | 1.014202 | CHAPTER 6: EQUIPMENT |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/11/Text/47` | 0.786040 | **EQUIPMENT** |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/7/Text/18` | 0.786040 | **EQUIPMENT** |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/13/Text/39` | 0.744040 | **EQUIPMENT** |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/28` | 0.744040 | **EQUIPMENT** |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/17/Text/6` | 0.744040 | **EQUIPMENT** |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/5/Text/26` | 0.744040 | **EQUIPMENT** |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/15/Text/16` | 0.744040 | **EQUIPMENT** |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/4/SectionHeader/5` | 0.679235 | IMPROVING EQUIPMENT |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/4/SectionHeader/11` | 0.679235 | IMPROVING EQUIPMENT |

### Query 1
- Text: What is the rule about To make your mark on the galaxy, you'll need to have the right equipment, including armor, weapons,  augmentation, and other gear. This chapter presents the various equipment that you can purchase  during character creation. You can usually find these items for sale in most cities and other large  settlements.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/1/Text/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/1/Text/2', 'PZO22001 Starfinder Player Core 232-249::/page/1/Text/7', 'PZO22001 Starfinder Player Core 232-249::/page/4/Text/6']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/2` | 1.015774 | To make your mark on the galaxy, you'll need to have the right equipment, including armor, weapons,  augmentation, and other gear. This chapter presents the various equipment that you can purchase  du |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/7` | 0.670921 | Once you've purchased your starting items, there are three  main ways to gain new items and equipment: you can find  them during an adventure, make them using the Crafting  skill, or purchase them fro |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/4/Text/6` | 0.647961 | Most types of armor, shields, and weapons in Starfinder come in a variety of grades. Each grade represents an improved version of that piece of equipment and should be sought after once your character |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/6/Text/2` | 0.603841 | Tech gear represents a variety of different consumer and specialized equipment used throughout the  galaxy. Depending on the situation, your character will need all sorts of items both while exploring |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/4/Text/8` | 0.570143 | Equipment typically comes in seven grades: commercial, tactical, advanced, superior, elite, ultimate, and paragon. While most armor, shields, and weapons can exist in any grade from commercial to para |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/6` | 0.541300 | Your character starts out with 150 credits to spend on any  common items from this chapter. Credits are a galactic  currency used to barter and trade for goods in the Starfinder  setting. Items with a |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/1/SectionHeader/1` | 0.518111 | CHAPTER 6: EQUIPMENT |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/8/Text/10` | 0.509764 | **Maker's** **Toolkit:** You need a maker's toolkit to create items  from UPBs with the Craft skill. A tactical maker's toolkit gives  you a +1 item bonus to the check. |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/9/Text/7` | 0.503996 | Some medical items have the tech trait. Some also have the  consumable trait, which means that the item is used up once  activated. Rules for creating medical items are found in the Craft  activity on |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/7` | 0.496304 | Each item has an item level, which represents the item's  complexity and any magic or technology used in its  construction. Simpler items with a lower level are easier to  construct, and you can't Cra |

### Query 2
- Text: What is the rule about Your character starts out with 150 credits to spend on any  common items from this chapter. Credits are a galactic  currency used to barter and trade for goods in the Starfinder  setting. Items with an uncommon rarity can be purchased  only if you have special access from abilities you selected  during character creation or your GM gives you permission  to purchase them.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/1/Text/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/1/Text/6', 'PZO22001 Starfinder Player Core 232-249::/page/1/Text/9', 'PZO22001 Starfinder Player Core 232-249::/page/1/Text/14']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/6` | 0.972575 | Your character starts out with 150 credits to spend on any  common items from this chapter. Credits are a galactic  currency used to barter and trade for goods in the Starfinder  setting. Items with a |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/9` | 0.662096 | The basic currency of the Pact Worlds (and Starfinder overall)  is the credit. Interplanetary business is conducted through  the trade of credits standardized by the strenuous banking  regulations of |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/14` | 0.593067 | Your character starts with 150 credits. |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/2` | 0.517146 | To make your mark on the galaxy, you'll need to have the right equipment, including armor, weapons,  augmentation, and other gear. This chapter presents the various equipment that you can purchase  du |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/5` | 0.515482 | Characters can use UPBs in place of credits for crafting  items using maker's kits; in fact, they're necessary for the use  of certain tools. |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/7` | 0.513005 | Each item has an item level, which represents the item's  complexity and any magic or technology used in its  construction. Simpler items with a lower level are easier to  construct, and you can't Cra |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/12` | 0.506300 | Most people in Starfinder keep their wealth on a protected  item known as a credstick. These devices are often flat and  roughly the size of a human finger. They range in dimensions  and quality, but |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/17` | 0.504203 | Individuals in the Pact Worlds often carry credsticks,  and other civilizations that interact with the Pact often turn  local funds into credits and thus carry them to spend their  converted currency. |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/1` | 0.498608 | An item with a Price of "—" can't be purchased. An item with  a Price of 0 is normally free, but its value could be higher  based on the materials used to create it. Most items can be  sold for half t |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/4/Text/6` | 0.493317 | Most types of armor, shields, and weapons in Starfinder come in a variety of grades. Each grade represents an improved version of that piece of equipment and should be sought after once your character |

### Query 3
- Text: What is the rule about Once you've purchased your starting items, there are three  main ways to gain new items and equipment: you can find  them during an adventure, make them using the Crafting  skill, or purchase them from a vendor.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/1/Text/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/1/Text/7', 'PZO22001 Starfinder Player Core 232-249::/page/4/Text/13', 'PZO22001 Starfinder Player Core 232-249::/page/1/Text/2']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/7` | 0.972322 | Once you've purchased your starting items, there are three  main ways to gain new items and equipment: you can find  them during an adventure, make them using the Crafting  skill, or purchase them fro |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/4/Text/13` | 0.647698 | materials using the same process as the Craft activity, except as noted here. The original item provides raw materials equal to its price. The DC of the Crafting check to improve an item is determined |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/2` | 0.635670 | To make your mark on the galaxy, you'll need to have the right equipment, including armor, weapons,  augmentation, and other gear. This chapter presents the various equipment that you can purchase  du |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/4/Text/14` | 0.562808 | If you have the formula for the item you can improve an item by supplying UPB equal to half the difference between the two items, but you must work multiple days to reduce the materials needed to comp |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/5/Text/16` | 0.555796 | Price and the item's Craft DC. You must  meet any requirements to Craft the item,  except you don't need to have access to the item |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/9/Text/7` | 0.538826 | Some medical items have the tech trait. Some also have the  consumable trait, which means that the item is used up once  activated. Rules for creating medical items are found in the Craft  activity on |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/5/Text/11` | 0.524368 | If you have a formula, you can Craft a copy of it using  the Crafting skill. You can also Craft a formula by reverse  engineering it from an item you possess. Use the formula's |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/8/Text/10` | 0.522859 | **Maker's** **Toolkit:** You need a maker's toolkit to create items  from UPBs with the Craft skill. A tactical maker's toolkit gives  you a +1 item bonus to the check. |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/6` | 0.519104 | Your character starts out with 150 credits to spend on any  common items from this chapter. Credits are a galactic  currency used to barter and trade for goods in the Starfinder  setting. Items with a |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/7` | 0.508637 | Each item has an item level, which represents the item's  complexity and any magic or technology used in its  construction. Simpler items with a lower level are easier to  construct, and you can't Cra |

### Query 4
- Text: Summarize CREDITS AND CURRENCY
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/1/SectionHeader/8']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/1/SectionHeader/8', 'PZO22001 Starfinder Player Core 232-249::/page/1/SectionHeader/13', 'PZO22001 Starfinder Player Core 232-249::/page/1/SectionHeader/18']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/1/SectionHeader/8` | 0.978045 | CREDITS AND CURRENCY |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/1/SectionHeader/13` | 0.685524 | **CREDITS** |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/1/SectionHeader/18` | 0.599775 | OTHER CURRENCY |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/9` | 0.500833 | The basic currency of the Pact Worlds (and Starfinder overall)  is the credit. Interplanetary business is conducted through  the trade of credits standardized by the strenuous banking  regulations of |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/10` | 0.484777 | Pact credits themselves are a combination of both digital  and physical currency assets. One person might contain all  their credits on a digital datacrypt that's safeguarded by the  most rigorous of |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/17` | 0.424967 | Individuals in the Pact Worlds often carry credsticks,  and other civilizations that interact with the Pact often turn  local funds into credits and thus carry them to spend their  converted currency. |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/6` | 0.421786 | Your character starts out with 150 credits to spend on any  common items from this chapter. Credits are a galactic  currency used to barter and trade for goods in the Starfinder  setting. Items with a |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/16` | 0.418577 | Credsticks aren't gateways to the entirety of one's wealth,  and larger stores of credits are often kept secured in banks,  personal vaults, or secure databases. Instead, a credstick  is a safe and an |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/5/TableCell/527` | 0.402960 | 1,000 credits |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/11/TableCell/869` | 0.402960 | 1,000 credits |

### Query 5
- Text: What is the rule about The basic currency of the Pact Worlds (and Starfinder overall)  is the credit. Interplanetary business is conducted through  the trade of credits standardized by the strenuous banking  regulations of various interstellar powers and organizations,  like the Church of Abadar. Though not every civilization uses  the Pact credit as its basis of currency, many have converted  over. In cases where a civilization hasn't converted over, there  are often agreements in place to determine the relative worth  of a credit compared to local currency. Except when dealing  with completely hostile civilizations or undiscovered regions  of space, the Pact credit is usable in almost any circumstance.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/1/Text/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/1/Text/9', 'PZO22001 Starfinder Player Core 232-249::/page/1/Text/6', 'PZO22001 Starfinder Player Core 232-249::/page/1/Text/17']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/9` | 1.007105 | The basic currency of the Pact Worlds (and Starfinder overall)  is the credit. Interplanetary business is conducted through  the trade of credits standardized by the strenuous banking  regulations of |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/6` | 0.712442 | Your character starts out with 150 credits to spend on any  common items from this chapter. Credits are a galactic  currency used to barter and trade for goods in the Starfinder  setting. Items with a |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/17` | 0.675336 | Individuals in the Pact Worlds often carry credsticks,  and other civilizations that interact with the Pact often turn  local funds into credits and thus carry them to spend their  converted currency. |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/10` | 0.632381 | Pact credits themselves are a combination of both digital  and physical currency assets. One person might contain all  their credits on a digital datacrypt that's safeguarded by the  most rigorous of |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/12` | 0.533477 | Most people in Starfinder keep their wealth on a protected  item known as a credstick. These devices are often flat and  roughly the size of a human finger. They range in dimensions  and quality, but |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/19` | 0.484987 | Art objects, gems, raw materials (such as those used for the  Craft activity), and relics of long-dead cultures can be used  much like currency: you can sell them for the same Price you  can buy them. |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/1/SectionHeader/8` | 0.475502 | CREDITS AND CURRENCY |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/9/Text/6` | 0.456188 | The items listed on the following table are the most widely  available medical items in the Pact Worlds. Medical items aren't  magical. They instead use the properties of chemicals and the  latest adv |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/16` | 0.454600 | Credsticks aren't gateways to the entirety of one's wealth,  and larger stores of credits are often kept secured in banks,  personal vaults, or secure databases. Instead, a credstick  is a safe and an |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/5` | 0.440397 | Characters can use UPBs in place of credits for crafting  items using maker's kits; in fact, they're necessary for the use  of certain tools. |

### Query 6
- Text: What is the rule about Pact credits themselves are a combination of both digital  and physical currency assets. One person might contain all  their credits on a digital datacrypt that's safeguarded by the  most rigorous of protections and authenticated by reputable  banking institutions. Another person might keep their wealth  on privately minted plastic chips that have been magically  enhanced to contain a specific aura that can be authenticated  by any basic device capable of scanning currency.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/1/Text/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/1/Text/10', 'PZO22001 Starfinder Player Core 232-249::/page/1/Text/17', 'PZO22001 Starfinder Player Core 232-249::/page/1/Text/9']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/10` | 1.002473 | Pact credits themselves are a combination of both digital  and physical currency assets. One person might contain all  their credits on a digital datacrypt that's safeguarded by the  most rigorous of |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/17` | 0.651875 | Individuals in the Pact Worlds often carry credsticks,  and other civilizations that interact with the Pact often turn  local funds into credits and thus carry them to spend their  converted currency. |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/9` | 0.640817 | The basic currency of the Pact Worlds (and Starfinder overall)  is the credit. Interplanetary business is conducted through  the trade of credits standardized by the strenuous banking  regulations of |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/16` | 0.572571 | Credsticks aren't gateways to the entirety of one's wealth,  and larger stores of credits are often kept secured in banks,  personal vaults, or secure databases. Instead, a credstick  is a safe and an |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/12` | 0.527236 | Most people in Starfinder keep their wealth on a protected  item known as a credstick. These devices are often flat and  roughly the size of a human finger. They range in dimensions  and quality, but |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/15` | 0.489800 | is necessary, they can require audio or biometric imprints  in order to activate. Some advanced credsticks even have a  magical component that might require a mental password or  the recitation of a s |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/1/SectionHeader/8` | 0.462736 | CREDITS AND CURRENCY |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/4` | 0.447750 | UPBs are so common that they're used as currency in  many major settlements and trade hubs. While credsticks are  a more convenient and secure way to carry value, UPBs have  the advantage of direct ut |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/9/Text/6` | 0.447231 | The items listed on the following table are the most widely  available medical items in the Pact Worlds. Medical items aren't  magical. They instead use the properties of chemicals and the  latest adv |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/19` | 0.436354 | Art objects, gems, raw materials (such as those used for the  Craft activity), and relics of long-dead cultures can be used  much like currency: you can sell them for the same Price you  can buy them. |

### Query 7
- Text: Summarize CREDSTICKS
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/1/SectionHeader/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/1/SectionHeader/11', 'PZO22001 Starfinder Player Core 232-249::/page/1/Text/16', 'PZO22001 Starfinder Player Core 232-249::/page/1/Text/17']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/1/SectionHeader/11` | 0.952764 | CREDSTICKS |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/16` | 0.546404 | Credsticks aren't gateways to the entirety of one's wealth,  and larger stores of credits are often kept secured in banks,  personal vaults, or secure databases. Instead, a credstick  is a safe and an |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/17` | 0.522192 | Individuals in the Pact Worlds often carry credsticks,  and other civilizations that interact with the Pact often turn  local funds into credits and thus carry them to spend their  converted currency. |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/15` | 0.465690 | is necessary, they can require audio or biometric imprints  in order to activate. Some advanced credsticks even have a  magical component that might require a mental password or  the recitation of a s |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/12` | 0.447098 | Most people in Starfinder keep their wealth on a protected  item known as a credstick. These devices are often flat and  roughly the size of a human finger. They range in dimensions  and quality, but |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/4` | 0.385734 | UPBs are so common that they're used as currency in  many major settlements and trade hubs. While credsticks are  a more convenient and secure way to carry value, UPBs have  the advantage of direct ut |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/1/SectionHeader/13` | 0.382827 | **CREDITS** |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/1/SectionHeader/8` | 0.335434 | CREDITS AND CURRENCY |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/3/Text/34` | 0.315333 | Shields |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/10` | 0.297025 | Pact credits themselves are a combination of both digital  and physical currency assets. One person might contain all  their credits on a digital datacrypt that's safeguarded by the  most rigorous of |

### Query 8
- Text: What is the rule about Most people in Starfinder keep their wealth on a protected  item known as a credstick. These devices are often flat and  roughly the size of a human finger. They range in dimensions  and quality, but at the end of the day, they're just a means of  conveniently carrying and spending money. Usage of these  devices is determined by the owner, and a credstick can  accept or spend funds with as simple an action as tapping it  near a suitable banking device. When more rigorous security?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/1/Text/12']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/1/Text/12', 'PZO22001 Starfinder Player Core 232-249::/page/1/Text/16', 'PZO22001 Starfinder Player Core 232-249::/page/1/Text/17']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/12` | 1.005166 | Most people in Starfinder keep their wealth on a protected  item known as a credstick. These devices are often flat and  roughly the size of a human finger. They range in dimensions  and quality, but |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/16` | 0.786899 | Credsticks aren't gateways to the entirety of one's wealth,  and larger stores of credits are often kept secured in banks,  personal vaults, or secure databases. Instead, a credstick  is a safe and an |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/17` | 0.734374 | Individuals in the Pact Worlds often carry credsticks,  and other civilizations that interact with the Pact often turn  local funds into credits and thus carry them to spend their  converted currency. |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/15` | 0.652537 | is necessary, they can require audio or biometric imprints  in order to activate. Some advanced credsticks even have a  magical component that might require a mental password or  the recitation of a s |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/4` | 0.602535 | UPBs are so common that they're used as currency in  many major settlements and trade hubs. While credsticks are  a more convenient and secure way to carry value, UPBs have  the advantage of direct ut |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/10` | 0.554381 | Pact credits themselves are a combination of both digital  and physical currency assets. One person might contain all  their credits on a digital datacrypt that's safeguarded by the  most rigorous of |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/6` | 0.544518 | Your character starts out with 150 credits to spend on any  common items from this chapter. Credits are a galactic  currency used to barter and trade for goods in the Starfinder  setting. Items with a |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/9` | 0.531322 | The basic currency of the Pact Worlds (and Starfinder overall)  is the credit. Interplanetary business is conducted through  the trade of credits standardized by the strenuous banking  regulations of |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/4/Text/6` | 0.502832 | Most types of armor, shields, and weapons in Starfinder come in a variety of grades. Each grade represents an improved version of that piece of equipment and should be sought after once your character |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/5/Text/9` | 0.424163 | Formulas are formalized instructions for making items. Their  primary purpose is to reduce the time it takes you to start the  Craft activity, which is helpful for items you'll make frequently.  You c |

### Query 9
- Text: Summarize **CREDITS**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/1/SectionHeader/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/1/SectionHeader/13', 'PZO22001 Starfinder Player Core 232-249::/page/1/SectionHeader/8', 'PZO22001 Starfinder Player Core 232-249::/page/16/TableCell/393']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/1/SectionHeader/13` | 0.951747 | **CREDITS** |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/1/SectionHeader/8` | 0.683447 | CREDITS AND CURRENCY |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/16/TableCell/393` | 0.525318 | 700,000 credits |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/5/Table/19` | 0.478847 | LevelPriceLevelPrice0*5 credits11700 credits110 credits121,000 credits220 credits131,500 credits330 credits142,250 credits450 credits153,250 credits580 credits165,000 credits6130 credits177,500 credit |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/11/TableCell/866` | 0.477547 | 1,300 credits |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/10/Text/49` | 0.474548 | **Price **100 credits |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/11/Text/27` | 0.468171 | **Price **30 credits |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/10/Text/42` | 0.468170 | **Price **30 credits |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/5/TableCell/531` | 0.467668 | 1,500 credits |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/16/TableCell/386` | 0.465992 | 240,000 credits |

### Query 10
- Text: What is the rule about Your character starts with 150 credits.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/1/Text/14']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/1/Text/14', 'PZO22001 Starfinder Player Core 232-249::/page/1/Text/6', 'PZO22001 Starfinder Player Core 232-249::/page/5/TableCell/537']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/14` | 0.917330 | Your character starts with 150 credits. |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/6` | 0.603037 | Your character starts out with 150 credits to spend on any  common items from this chapter. Credits are a galactic  currency used to barter and trade for goods in the Starfinder  setting. Items with a |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/5/TableCell/537` | 0.516433 | 50 credits |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/5/TableCell/549` | 0.464465 | 180 credits |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/11/TableCell/885` | 0.464465 | 180 credits |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/10/Text/7` | 0.462740 | **Type **elite; **Level **15; **Price **13,000 credits |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/10/Text/49` | 0.458988 | **Price **100 credits |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/16/TableCell/372` | 0.454922 | 14,000 credits |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/5/TableCell/531` | 0.454816 | 1,500 credits |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/5/TableCell/545` | 0.452292 | 130 credits |

### Query 11
- Text: What is the rule about is necessary, they can require audio or biometric imprints  in order to activate. Some advanced credsticks even have a  magical component that might require a mental password or  the recitation of a specific spell to access stored funds.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/1/Text/15']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/1/Text/15', 'PZO22001 Starfinder Player Core 232-249::/page/1/Text/12', 'PZO22001 Starfinder Player Core 232-249::/page/1/Text/16']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/15` | 0.989248 | is necessary, they can require audio or biometric imprints  in order to activate. Some advanced credsticks even have a  magical component that might require a mental password or  the recitation of a s |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/12` | 0.636952 | Most people in Starfinder keep their wealth on a protected  item known as a credstick. These devices are often flat and  roughly the size of a human finger. They range in dimensions  and quality, but |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/16` | 0.631412 | Credsticks aren't gateways to the entirety of one's wealth,  and larger stores of credits are often kept secured in banks,  personal vaults, or secure databases. Instead, a credstick  is a safe and an |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/17` | 0.554580 | Individuals in the Pact Worlds often carry credsticks,  and other civilizations that interact with the Pact often turn  local funds into credits and thus carry them to spend their  converted currency. |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/10` | 0.499208 | Pact credits themselves are a combination of both digital  and physical currency assets. One person might contain all  their credits on a digital datacrypt that's safeguarded by the  most rigorous of |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/4` | 0.482139 | UPBs are so common that they're used as currency in  many major settlements and trade hubs. While credsticks are  a more convenient and secure way to carry value, UPBs have  the advantage of direct ut |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/8/Text/2` | 0.422260 | **Holoskin:** A holographic projector mounted to a belt or  limb strap can be activated as an Interact action. It can be  programmed to project the appearance of another creature  of the same size cat |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/8/Text/14` | 0.422010 | **Musical** **Instrument:** All but the most traditional instruments  use modern technology to amplify their sound, provide musical  accompaniment, or connect wirelessly to other instruments.  Handhel |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/5` | 0.415476 | Characters can use UPBs in place of credits for crafting  items using maker's kits; in fact, they're necessary for the use  of certain tools. |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/8/Text/1` | 0.410240 | toolkit to access a computer without using a user interface, but  this requires physical contact with the computer or contact via  an infosphere or a similar linked network. A tactical hacking  toolki |

### Query 12
- Text: What is the rule about Credsticks aren't gateways to the entirety of one's wealth,  and larger stores of credits are often kept secured in banks,  personal vaults, or secure databases. Instead, a credstick  is a safe and anonymous means of moving credits around  without being traced. Adventurers and common citizens  alike often keep a credstick on their person to handle any  purchases they might be called upon to make, while also only  keeping just enough credits on them that losing the credstick  wouldn't result in bankruptcy.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/1/Text/16']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/1/Text/16', 'PZO22001 Starfinder Player Core 232-249::/page/1/Text/12', 'PZO22001 Starfinder Player Core 232-249::/page/1/Text/17']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/16` | 1.016374 | Credsticks aren't gateways to the entirety of one's wealth,  and larger stores of credits are often kept secured in banks,  personal vaults, or secure databases. Instead, a credstick  is a safe and an |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/12` | 0.782393 | Most people in Starfinder keep their wealth on a protected  item known as a credstick. These devices are often flat and  roughly the size of a human finger. They range in dimensions  and quality, but |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/17` | 0.781507 | Individuals in the Pact Worlds often carry credsticks,  and other civilizations that interact with the Pact often turn  local funds into credits and thus carry them to spend their  converted currency. |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/15` | 0.656781 | is necessary, they can require audio or biometric imprints  in order to activate. Some advanced credsticks even have a  magical component that might require a mental password or  the recitation of a s |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/4` | 0.626130 | UPBs are so common that they're used as currency in  many major settlements and trade hubs. While credsticks are  a more convenient and secure way to carry value, UPBs have  the advantage of direct ut |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/10` | 0.601558 | Pact credits themselves are a combination of both digital  and physical currency assets. One person might contain all  their credits on a digital datacrypt that's safeguarded by the  most rigorous of |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/1/SectionHeader/11` | 0.504444 | CREDSTICKS |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/9` | 0.433531 | The basic currency of the Pact Worlds (and Starfinder overall)  is the credit. Interplanetary business is conducted through  the trade of credits standardized by the strenuous banking  regulations of |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/6` | 0.419568 | Your character starts out with 150 credits to spend on any  common items from this chapter. Credits are a galactic  currency used to barter and trade for goods in the Starfinder  setting. Items with a |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/1/SectionHeader/8` | 0.402859 | CREDITS AND CURRENCY |

### Query 13
- Text: What is the rule about Individuals in the Pact Worlds often carry credsticks,  and other civilizations that interact with the Pact often turn  local funds into credits and thus carry them to spend their  converted currency. Sometimes a person might carry several  credsticks, dedicating each one to a different use, or simply  trading the stick away if they want to make a purchase of  a predefined amount. If ever the number of credsticks on a  person becomes too cumbersome, it's easy enough to move  the funds between individual sticks and discard emptied  sticks to save on space, however a credstick always has a  negligible bulk.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/1/Text/17']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/1/Text/17', 'PZO22001 Starfinder Player Core 232-249::/page/1/Text/16', 'PZO22001 Starfinder Player Core 232-249::/page/1/Text/12']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/17` | 0.988163 | Individuals in the Pact Worlds often carry credsticks,  and other civilizations that interact with the Pact often turn  local funds into credits and thus carry them to spend their  converted currency. |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/16` | 0.733135 | Credsticks aren't gateways to the entirety of one's wealth,  and larger stores of credits are often kept secured in banks,  personal vaults, or secure databases. Instead, a credstick  is a safe and an |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/12` | 0.700388 | Most people in Starfinder keep their wealth on a protected  item known as a credstick. These devices are often flat and  roughly the size of a human finger. They range in dimensions  and quality, but |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/10` | 0.619897 | Pact credits themselves are a combination of both digital  and physical currency assets. One person might contain all  their credits on a digital datacrypt that's safeguarded by the  most rigorous of |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/9` | 0.593092 | The basic currency of the Pact Worlds (and Starfinder overall)  is the credit. Interplanetary business is conducted through  the trade of credits standardized by the strenuous banking  regulations of |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/4` | 0.587914 | UPBs are so common that they're used as currency in  many major settlements and trade hubs. While credsticks are  a more convenient and secure way to carry value, UPBs have  the advantage of direct ut |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/15` | 0.550485 | is necessary, they can require audio or biometric imprints  in order to activate. Some advanced credsticks even have a  magical component that might require a mental password or  the recitation of a s |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/6` | 0.506863 | Your character starts out with 150 credits to spend on any  common items from this chapter. Credits are a galactic  currency used to barter and trade for goods in the Starfinder  setting. Items with a |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/3/Text/18` | 0.466357 | For example, a doshko sized for a Medium creature has a Price of 20 credits and 1 Bulk, so one made for a Huge creature is 80 credits and 4 Bulk. One made for a Tiny creature still costs 20 credits (d |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/19` | 0.456892 | Art objects, gems, raw materials (such as those used for the  Craft activity), and relics of long-dead cultures can be used  much like currency: you can sell them for the same Price you  can buy them. |

### Query 14
- Text: Summarize OTHER CURRENCY
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/1/SectionHeader/18']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/1/SectionHeader/18', 'PZO22001 Starfinder Player Core 232-249::/page/1/SectionHeader/8', 'PZO22001 Starfinder Player Core 232-249::/page/11/SectionHeader/22']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/1/SectionHeader/18` | 0.954113 | OTHER CURRENCY |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/1/SectionHeader/8` | 0.599280 | CREDITS AND CURRENCY |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/11/SectionHeader/22` | 0.443153 | OTHER CONSUMABLES |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/19` | 0.402197 | Art objects, gems, raw materials (such as those used for the  Craft activity), and relics of long-dead cultures can be used  much like currency: you can sell them for the same Price you  can buy them. |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/21` | 0.388853 | Most items in the following tables have a Price, which is the  amount of currency it typically takes to purchase that item. |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/3/Text/14` | 0.362243 | Creatures of sizes other than Small, Medium, or Large need items appropriate to their size. These items have different Bulk and possibly a different Price. The Differently Sized Items table provides t |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/9` | 0.349949 | The basic currency of the Pact Worlds (and Starfinder overall)  is the credit. Interplanetary business is conducted through  the trade of credits standardized by the strenuous banking  regulations of |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/17` | 0.344442 | Individuals in the Pact Worlds often carry credsticks,  and other civilizations that interact with the Pact often turn  local funds into credits and thus carry them to spend their  converted currency. |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/6/Text/11` | 0.314391 | These items follow special rules or require more detail. |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/10` | 0.302192 | Pact credits themselves are a combination of both digital  and physical currency assets. One person might contain all  their credits on a digital datacrypt that's safeguarded by the  most rigorous of |

### Query 15
- Text: What is the rule about Art objects, gems, raw materials (such as those used for the  Craft activity), and relics of long-dead cultures can be used  much like currency: you can sell them for the same Price you  can buy them.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/1/Text/19']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/1/Text/19', 'PZO22001 Starfinder Player Core 232-249::/page/2/Text/1', 'PZO22001 Starfinder Player Core 232-249::/page/3/Text/19']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/19` | 0.975946 | Art objects, gems, raw materials (such as those used for the  Craft activity), and relics of long-dead cultures can be used  much like currency: you can sell them for the same Price you  can buy them. |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/1` | 0.725465 | An item with a Price of "—" can't be purchased. An item with  a Price of 0 is normally free, but its value could be higher  based on the materials used to create it. Most items can be  sold for half t |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/3/Text/19` | 0.545997 | Higher-level magic and tech items that cost significantly more than 8 times the cost of a mundane item use their listed Price regardless of size. Precious materials, however, have a Price based on the |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/4/Text/13` | 0.502103 | materials using the same process as the Craft activity, except as noted here. The original item provides raw materials equal to its price. The DC of the Crafting check to improve an item is determined |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/5/Text/6` | 0.467872 | Improvised or of dubious make, shoddy items are never  available for purchase except in the most desperate of  communities. When available, a shoddy item usually costs  half the Price of a standard it |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/21` | 0.465902 | Most items in the following tables have a Price, which is the  amount of currency it typically takes to purchase that item. |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/6` | 0.456625 | Your character starts out with 150 credits to spend on any  common items from this chapter. Credits are a galactic  currency used to barter and trade for goods in the Starfinder  setting. Items with a |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/17` | 0.455154 | Individuals in the Pact Worlds often carry credsticks,  and other civilizations that interact with the Pact often turn  local funds into credits and thus carry them to spend their  converted currency. |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/5/Text/16` | 0.446421 | Price and the item's Craft DC. You must  meet any requirements to Craft the item,  except you don't need to have access to the item |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/5/Text/11` | 0.440354 | If you have a formula, you can Craft a copy of it using  the Crafting skill. You can also Craft a formula by reverse  engineering it from an item you possess. Use the formula's |

### Query 16
- Text: Summarize PRICE
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/1/SectionHeader/20']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/1/SectionHeader/20', 'PZO22001 Starfinder Player Core 232-249::/page/11/TableCell/744', 'PZO22001 Starfinder Player Core 232-249::/page/16/TableCell/34']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/1/SectionHeader/20` | 0.824247 | PRICE |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/11/TableCell/744` | 0.699215 | Price |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/16/TableCell/34` | 0.699215 | Price |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/9/TableCell/1107` | 0.657215 | Price |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/5/TableCell/519` | 0.657215 | Price |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/16/TableCell/67` | 0.657215 | Price |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/16/TableCell/259` | 0.657215 | Price |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/11/TableCell/759` | 0.657214 | Price |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/277` | 0.657214 | Price |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/9/TableCell/902` | 0.657214 | Price |

### Query 17
- Text: Summarize Most items in the following tables have a Price, which is the  amount of currency it typically takes to purchase that item.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/1/Text/21']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/1/Text/21', 'PZO22001 Starfinder Player Core 232-249::/page/2/Text/1', 'PZO22001 Starfinder Player Core 232-249::/page/5/Text/10']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/21` | 1.031845 | Most items in the following tables have a Price, which is the  amount of currency it typically takes to purchase that item. |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/1` | 0.618106 | An item with a Price of "—" can't be purchased. An item with  a Price of 0 is normally free, but its value could be higher  based on the materials used to create it. Most items can be  sold for half t |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/5/Text/10` | 0.608311 | For the Price listed on the table, you can buy a common  formula. A purchased formula is a virtual file downloaded  onto a computer containing the schematics and print-ready  3D models of the item. Pa |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/3/Text/19` | 0.566076 | Higher-level magic and tech items that cost significantly more than 8 times the cost of a mundane item use their listed Price regardless of size. Precious materials, however, have a Price based on the |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/6/Text/5` | 0.563335 | The tables starting on page 240 list the Price and Bulk entries  for a wide variety of gear you can use to kit out your character.  Any item with a number after it in parentheses indicates that  the i |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/3/Text/14` | 0.561603 | Creatures of sizes other than Small, Medium, or Large need items appropriate to their size. These items have different Bulk and possibly a different Price. The Differently Sized Items table provides t |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/19` | 0.500463 | Art objects, gems, raw materials (such as those used for the  Craft activity), and relics of long-dead cultures can be used  much like currency: you can sell them for the same Price you  can buy them. |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/6` | 0.455229 | Your character starts out with 150 credits to spend on any  common items from this chapter. Credits are a galactic  currency used to barter and trade for goods in the Starfinder  setting. Items with a |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/5/Text/6` | 0.432131 | Improvised or of dubious make, shoddy items are never  available for purchase except in the most desperate of  communities. When available, a shoddy item usually costs  half the Price of a standard it |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/4/Text/13` | 0.425071 | materials using the same process as the Craft activity, except as noted here. The original item provides raw materials equal to its price. The DC of the Crafting check to improve an item is determined |

### Query 18
- Text: Summarize **INTRODUCTION**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/1/Text/23']
- Expected found: `True`
- Expected rank: `8`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/13/Text/34', 'PZO22001 Starfinder Player Core 232-249::/page/15/Text/11', 'PZO22001 Starfinder Player Core 232-249::/page/11/Text/43']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/13/Text/34` | 0.880541 | **INTRODUCTION** |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/15/Text/11` | 0.880541 | **INTRODUCTION** |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/11/Text/43` | 0.880541 | **INTRODUCTION** |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/9/Text/18` | 0.838541 | **INTRODUCTION** |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/7/Text/14` | 0.838541 | **INTRODUCTION** |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/5/Text/22` | 0.838541 | **INTRODUCTION** |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/17/Text/2` | 0.838541 | **INTRODUCTION** |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/23` | 0.838541 | **INTRODUCTION** |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/17/Text/7` | 0.799846 | **Introduction** |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/5/Text/27` | 0.799846 | **Introduction** |

### Query 19
- Text: What is the rule about **ANCESTRIES & ** **BACKGROUNDS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/1/Text/24']
- Expected found: `True`
- Expected rank: `6`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/15/Text/12', 'PZO22001 Starfinder Player Core 232-249::/page/13/Text/35', 'PZO22001 Starfinder Player Core 232-249::/page/7/Text/15']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/15/Text/12` | 0.920820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/13/Text/35` | 0.920820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/7/Text/15` | 0.920820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/5/Text/23` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/9/Text/19` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/24` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/17/Text/3` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/11/Text/44` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/3/Text/26` | 0.822421 | ANCESTRIES & BACKGROUNDS |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/15/Text/28` | 0.390721 | **CONDITIONS ** |

### Query 20
- Text: Summarize **CLASSES**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/1/Text/25']
- Expected found: `True`
- Expected rank: `7`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/15/Text/13', 'PZO22001 Starfinder Player Core 232-249::/page/11/Text/45', 'PZO22001 Starfinder Player Core 232-249::/page/5/Text/24']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/15/Text/13` | 0.940061 | **CLASSES** |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/5/Text/24` | 0.940061 | **CLASSES** |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/11/Text/45` | 0.940061 | **CLASSES** |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/13/Text/36` | 0.910061 | **CLASSES** |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/7/Text/16` | 0.910061 | **CLASSES** |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/17/Text/4` | 0.910061 | **CLASSES** |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/25` | 0.910061 | **CLASSES** |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/3/Text/27` | 0.763091 | CLASSES |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/9/Text/20` | 0.719499 | **CLASSES** **SKILLS** |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/12/SectionHeader/4` | 0.467480 | ARMOR CLASS |

### Query 21
- Text: What is the rule about **SKILLS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/1/Text/26']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/15/Text/14', 'PZO22001 Starfinder Player Core 232-249::/page/1/Text/26', 'PZO22001 Starfinder Player Core 232-249::/page/13/Text/37']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/15/Text/14` | 0.864442 | **SKILLS** |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/26` | 0.864442 | **SKILLS** |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/13/Text/37` | 0.864442 | **SKILLS** |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/9/Text/20` | 0.738936 | **CLASSES** **SKILLS** |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/3/Text/28` | 0.712079 | SKILLS |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/5/Text/25` | 0.651094 | **SKILLS** **FEATS** |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/11/Text/46` | 0.651094 | **SKILLS** **FEATS** |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/7/Text/17` | 0.651094 | **SKILLS** **FEATS** |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/17/Text/5` | 0.651094 | **SKILLS** **FEATS** |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/13/Text/10` | 0.439756 | While wearing your armor, you take this penalty to  Strength- and Dexterity-based skill checks, except for  those that have the attack trait. If you meet the armor's  Strength threshold (see Strength |

### Query 22
- Text: What is the rule about **FEATS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/1/Text/27']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/13/Text/38', 'PZO22001 Starfinder Player Core 232-249::/page/15/Text/15', 'PZO22001 Starfinder Player Core 232-249::/page/1/Text/27']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/13/Text/38` | 0.871817 | **FEATS** |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/15/Text/15` | 0.871817 | **FEATS** |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/27` | 0.871817 | **FEATS** |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/9/Text/21` | 0.702296 | **FEATS** **EQUIPMENT** |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/7/Text/17` | 0.653037 | **SKILLS** **FEATS** |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/11/Text/46` | 0.653037 | **SKILLS** **FEATS** |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/17/Text/5` | 0.653037 | **SKILLS** **FEATS** |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/5/Text/25` | 0.653037 | **SKILLS** **FEATS** |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/3/Text/29` | 0.411931 | FEATS <u>Equipme</u>nt |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/6/Text/11` | 0.328370 | These items follow special rules or require more detail. |

### Query 23
- Text: Summarize **EQUIPMENT**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/1/Text/28']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/1/Text/28', 'PZO22001 Starfinder Player Core 232-249::/page/7/Text/18', 'PZO22001 Starfinder Player Core 232-249::/page/5/Text/26']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/28` | 0.944726 | **EQUIPMENT** |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/7/Text/18` | 0.944726 | **EQUIPMENT** |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/5/Text/26` | 0.944726 | **EQUIPMENT** |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/11/Text/47` | 0.902726 | **EQUIPMENT** |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/13/Text/39` | 0.902726 | **EQUIPMENT** |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/17/Text/6` | 0.902726 | **EQUIPMENT** |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/15/Text/16` | 0.902726 | **EQUIPMENT** |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/1/SectionHeader/1` | 0.829789 | CHAPTER 6: EQUIPMENT |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/4/SectionHeader/7` | 0.715403 | **GRADES OF EQUIPMENT ** |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/4/SectionHeader/11` | 0.691522 | IMPROVING EQUIPMENT |

### Query 24
- Text: Summarize **Introduction**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/1/Text/29']
- Expected found: `True`
- Expected rank: `7`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/5/Text/27', 'PZO22001 Starfinder Player Core 232-249::/page/17/Text/7', 'PZO22001 Starfinder Player Core 232-249::/page/15/Text/17']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/5/Text/27` | 0.868286 | **Introduction** |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/17/Text/7` | 0.868286 | **Introduction** |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/15/Text/17` | 0.868286 | **Introduction** |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/13/Text/40` | 0.826286 | **Introduction** |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/7/Text/19` | 0.826286 | **Introduction** |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/11/Text/48` | 0.826286 | **Introduction** |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/29` | 0.826286 | **Introduction** |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/9/Text/23` | 0.826286 | **Introduction** |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/13/Text/34` | 0.767385 | **INTRODUCTION** |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/15/Text/11` | 0.767385 | **INTRODUCTION** |

### Query 25
- Text: Summarize **Tech Gear**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/1/Text/31']
- Expected found: `True`
- Expected rank: `8`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/13/Text/41', 'PZO22001 Starfinder Player Core 232-249::/page/5/Text/28', 'PZO22001 Starfinder Player Core 232-249::/page/17/Text/9']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/13/Text/41` | 0.945693 | **Tech Gear** |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/5/Text/28` | 0.945693 | **Tech Gear** |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/17/Text/9` | 0.945693 | **Tech Gear** |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/15/Text/18` | 0.903693 | **Tech Gear** |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/11/Text/49` | 0.903693 | **Tech Gear** |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/7/Text/21` | 0.903693 | **Tech Gear** |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/9/Text/24` | 0.903693 | **Tech Gear** |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/31` | 0.903693 | **Tech Gear** |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/3/Text/32` | 0.792214 | Tech Gear |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/6/SectionHeader/1` | 0.707475 | TECH GEAR |

### Query 26
- Text: Summarize **Armor**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/1/Text/32']
- Expected found: `True`
- Expected rank: `7`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/15/Text/19', 'PZO22001 Starfinder Player Core 232-249::/page/5/Text/29', 'PZO22001 Starfinder Player Core 232-249::/page/7/Text/22']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/15/Text/19` | 0.943498 | **Armor** |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/5/Text/29` | 0.943498 | **Armor** |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/7/Text/22` | 0.943498 | **Armor** |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/9/Text/25` | 0.901498 | **Armor** |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/11/Text/50` | 0.901498 | **Armor** |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/17/Text/10` | 0.901498 | **Armor** |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/32` | 0.901498 | **Armor** |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/13/Text/42` | 0.901498 | **Armor** |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/5/Text/32` | 0.886051 | **Armor ** |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/9/Text/27` | 0.886051 | **Armor ** |

### Query 27
- Text: Summarize **Shields**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/1/Text/33']
- Expected found: `True`
- Expected rank: `5`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/17/Text/11', 'PZO22001 Starfinder Player Core 232-249::/page/11/Text/51', 'PZO22001 Starfinder Player Core 232-249::/page/13/Text/43']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/17/Text/11` | 0.978985 | **Shields** |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/11/Text/51` | 0.978985 | **Shields** |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/13/Text/43` | 0.978985 | **Shields** |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/7/Text/23` | 0.936985 | **Shields** |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/33` | 0.936985 | **Shields** |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/5/Text/30` | 0.936985 | **Shields** |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/9/Text/26` | 0.789608 | **Shields** **Weapons** |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/3/Text/34` | 0.689197 | Shields |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/318` | 0.434341 | Detach a shield or item strapped to you |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/13/Text/44` | 0.420611 | **Weapons** |

### Query 28
- Text: Summarize **Weapons**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/1/Text/35']
- Expected found: `True`
- Expected rank: `5`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/17/Text/12', 'PZO22001 Starfinder Player Core 232-249::/page/7/Text/24', 'PZO22001 Starfinder Player Core 232-249::/page/5/Text/31']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/5/Text/31` | 0.929773 | **Weapons** |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/17/Text/12` | 0.929773 | **Weapons** |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/7/Text/24` | 0.929773 | **Weapons** |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/13/Text/44` | 0.887773 | **Weapons** |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/35` | 0.887773 | **Weapons** |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/11/Text/52` | 0.887773 | **Weapons** |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/7/Text/26` | 0.796067 | **Weapon ** |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/17/Text/14` | 0.796067 | **Weapon ** |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/17/Text/16` | 0.788850 | **Ammunition & ** **Weapons** |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/3/Text/35` | 0.772803 | Weapons |

### Query 29
- Text: Summarize **Armor ** **Upgrades**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/1/Text/36']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/17/Text/13', 'PZO22001 Starfinder Player Core 232-249::/page/13/Text/45', 'PZO22001 Starfinder Player Core 232-249::/page/1/Text/36']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/17/Text/13` | 0.988451 | **Armor ** **Upgrades** |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/13/Text/45` | 0.988451 | **Armor ** **Upgrades** |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/36` | 0.988451 | **Armor ** **Upgrades** |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/11/Text/53` | 0.946451 | **Armor ** **Upgrades** |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/7/Text/25` | 0.946451 | **Armor ** **Upgrades** |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/16/SectionHeader/9` | 0.798757 | **ARMOR IMPROVEMENTS ** |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/15/Text/19` | 0.727173 | **Armor** |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/17/Text/10` | 0.727173 | **Armor** |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/7/Text/22` | 0.727173 | **Armor** |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/32` | 0.727173 | **Armor** |

### Query 30
- Text: Summarize **Weapon ** **Upgrades**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/1/Text/37']
- Expected found: `True`
- Expected rank: `4`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/9/Text/28', 'PZO22001 Starfinder Player Core 232-249::/page/13/Text/46', 'PZO22001 Starfinder Player Core 232-249::/page/5/Text/34']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/9/Text/28` | 0.976575 | **Upgrades** **Weapon ** **Upgrades** |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/13/Text/46` | 0.973000 | **Weapon ** **Upgrades** |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/5/Text/34` | 0.973000 | **Weapon ** **Upgrades** |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/37` | 0.931000 | **Weapon ** **Upgrades** |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/11/Text/54` | 0.931000 | **Weapon ** **Upgrades** |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/3/Text/37` | 0.808581 | Weapon Upgrades |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/5/Text/33` | 0.739874 | **Upgrades** |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/13/Text/45` | 0.701684 | **Armor ** **Upgrades** |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/11/Text/53` | 0.689684 | **Armor ** **Upgrades** |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/7/Text/25` | 0.689684 | **Armor ** **Upgrades** |

### Query 31
- Text: Summarize **Precious ** **Ammunition & **
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/1/Text/38']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/1/Text/38', 'PZO22001 Starfinder Player Core 232-249::/page/5/Text/35', 'PZO22001 Starfinder Player Core 232-249::/page/13/Text/47']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/38` | 1.004748 | **Precious ** **Ammunition & ** |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/5/Text/35` | 0.970164 | **Precious ** **Ammunition & ** **Weapons** |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/13/Text/47` | 0.970164 | **Precious ** **Ammunition & ** **Weapons** |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/11/Text/55` | 0.928164 | **Precious ** **Ammunition & ** **Weapons** |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/9/Text/29` | 0.928164 | **Precious ** **Ammunition & ** **Weapons** |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/7/Text/27` | 0.859505 | **Upgrades** **Precious ** **Ammunition & ** |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/3/Text/38` | 0.825001 | Precious Ammunition & Weapons |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/15/Text/23` | 0.771062 | **Ammunition & ** |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/17/Text/16` | 0.730218 | **Ammunition & ** **Weapons** |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/17/Text/15` | 0.610595 | **Upgrades** **Precious ** |

### Query 32
- Text: Summarize **Weapons** **Grenades**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/1/Text/39']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/7/Text/28', 'PZO22001 Starfinder Player Core 232-249::/page/1/Text/39', 'PZO22001 Starfinder Player Core 232-249::/page/9/Text/30']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/7/Text/28` | 0.988183 | **Weapons** **Grenades** |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/39` | 0.988183 | **Weapons** **Grenades** |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/9/Text/30` | 0.769183 | **Grenades** |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/5/Text/36` | 0.727183 | **Grenades** |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/13/Text/48` | 0.727183 | **Grenades** |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/11/Text/56` | 0.727183 | **Grenades** |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/17/Text/17` | 0.717664 | **Grenades** **Magic Items** |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/35` | 0.687388 | **Weapons** |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/13/Text/44` | 0.687388 | **Weapons** |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/17/Text/12` | 0.687388 | **Weapons** |

### Query 33
- Text: Summarize **Magic Items**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/1/Text/40']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/1/Text/40', 'PZO22001 Starfinder Player Core 232-249::/page/7/Text/29', 'PZO22001 Starfinder Player Core 232-249::/page/11/Text/57']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/40` | 0.963309 | **Magic Items** |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/7/Text/29` | 0.963309 | **Magic Items** |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/11/Text/57` | 0.963309 | **Magic Items** |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/9/Text/31` | 0.921309 | **Magic Items** |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/13/Text/49` | 0.921309 | **Magic Items** |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/5/Text/37` | 0.749950 | **Magic Items** **Augmentations** |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/17/Text/17` | 0.667549 | **Grenades** **Magic Items** |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/3/Text/40` | 0.612955 | Magic Items  Augmentations |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/11/SectionHeader/30` | 0.570996 | **MEDICAL ITEMS** |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/9/Text/6` | 0.513117 | The items listed on the following table are the most widely  available medical items in the Pact Worlds. Medical items aren't  magical. They instead use the properties of chemicals and the  latest adv |

### Query 34
- Text: Summarize **Augmentations**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/1/Text/41']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/1/Text/41', 'PZO22001 Starfinder Player Core 232-249::/page/13/Text/50', 'PZO22001 Starfinder Player Core 232-249::/page/9/Text/32']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/41` | 0.964521 | **Augmentations** |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/9/Text/32` | 0.964521 | **Augmentations** |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/13/Text/50` | 0.964521 | **Augmentations** |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/11/Text/58` | 0.922521 | **Augmentations** |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/7/Text/30` | 0.922521 | **Augmentations** |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/17/Text/18` | 0.922521 | **Augmentations** |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/15/Text/26` | 0.922521 | **Augmentations** |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/5/Text/37` | 0.725584 | **Magic Items** **Augmentations** |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/3/Text/40` | 0.698840 | Magic Items  Augmentations |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/5/Text/33` | 0.609185 | **Upgrades** |

### Query 35
- Text: What is the rule about **SPELLS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/1/Text/42']
- Expected found: `True`
- Expected rank: `4`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/17/Text/19', 'PZO22001 Starfinder Player Core 232-249::/page/13/Text/51', 'PZO22001 Starfinder Player Core 232-249::/page/7/Text/31']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/17/Text/19` | 0.889304 | **SPELLS** |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/13/Text/51` | 0.889304 | **SPELLS** |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/7/Text/31` | 0.889304 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/42` | 0.847304 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/5/Text/38` | 0.847304 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/11/Text/59` | 0.847304 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/9/Text/33` | 0.847304 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/3/Text/41` | 0.776591 | SPELLS |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/11/SectionHeader/39` | 0.441994 | **SPELLCASTING SERVICES** |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/11/SectionHeader/37` | 0.437976 | SPELLCASTING |

### Query 36
- Text: Summarize **PLAYING THE ** **GAME**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/1/Text/43']
- Expected found: `True`
- Expected rank: `7`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/17/Text/20', 'PZO22001 Starfinder Player Core 232-249::/page/7/Text/32', 'PZO22001 Starfinder Player Core 232-249::/page/13/Text/52']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/17/Text/20` | 0.965000 | **PLAYING THE ** **GAME** |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/13/Text/52` | 0.965000 | **PLAYING THE ** **GAME** |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/7/Text/32` | 0.965000 | **PLAYING THE ** **GAME** |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/5/Text/39` | 0.923000 | **PLAYING THE ** **GAME** |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/11/Text/60` | 0.923000 | **PLAYING THE ** **GAME** |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/9/Text/34` | 0.923000 | **PLAYING THE ** **GAME** |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/43` | 0.923000 | **PLAYING THE ** **GAME** |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/15/Text/27` | 0.811006 | **PLAYING THE ** |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/3/Text/42` | 0.749688 | PLAYING THE GAME |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/9/Text/18` | 0.418586 | **INTRODUCTION** |

### Query 37
- Text: Summarize **CONDITIONS ** **APPENDIX**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/1/Text/44']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/1/Text/44', 'PZO22001 Starfinder Player Core 232-249::/page/13/Text/53', 'PZO22001 Starfinder Player Core 232-249::/page/11/Text/61']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/44` | 0.983499 | **CONDITIONS ** **APPENDIX** |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/13/Text/53` | 0.983499 | **CONDITIONS ** **APPENDIX** |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/11/Text/61` | 0.983499 | **CONDITIONS ** **APPENDIX** |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/9/Text/35` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/5/Text/40` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/17/Text/21` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/3/Text/43` | 0.806516 | CONDITIONS Appendix |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/15/Text/28` | 0.645203 | **CONDITIONS ** |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/7/Text/33` | 0.645203 | **CONDITIONS ** |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/9/Text/19` | 0.416141 | **ANCESTRIES & ** **BACKGROUNDS** |

### Query 38
- Text: Summarize **GLOSSARY & ** **INDEX**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/1/Text/45']
- Expected found: `True`
- Expected rank: `7`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/13/Text/54', 'PZO22001 Starfinder Player Core 232-249::/page/9/Text/36', 'PZO22001 Starfinder Player Core 232-249::/page/17/Text/22']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/13/Text/54` | 0.993465 | **GLOSSARY & ** **INDEX** |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/9/Text/36` | 0.993465 | **GLOSSARY & ** **INDEX** |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/17/Text/22` | 0.993465 | **GLOSSARY & ** **INDEX** |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/7/Text/34` | 0.951465 | **GLOSSARY & ** **INDEX** |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/11/Text/62` | 0.951465 | **GLOSSARY & ** **INDEX** |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/5/Text/41` | 0.951465 | **GLOSSARY & ** **INDEX** |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/45` | 0.951465 | **GLOSSARY & ** **INDEX** |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/3/Text/44` | 0.825490 | GLOSSARY & INDEX |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/15/Text/29` | 0.804819 | **GLOSSARY & ** |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/11/Text/45` | 0.385404 | **CLASSES** |

### Query 39
- Text: What is the rule about An item with a Price of "—" can't be purchased. An item with  a Price of 0 is normally free, but its value could be higher  based on the materials used to create it. Most items can be  sold for half their Price, but coins, gems, art objects, and raw  materials (such as components for the Craft activity) can be  exchanged for their full Price.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/2/Text/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/2/Text/1', 'PZO22001 Starfinder Player Core 232-249::/page/1/Text/19', 'PZO22001 Starfinder Player Core 232-249::/page/4/Text/13']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/1` | 1.006961 | An item with a Price of "—" can't be purchased. An item with  a Price of 0 is normally free, but its value could be higher  based on the materials used to create it. Most items can be  sold for half t |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/19` | 0.688328 | Art objects, gems, raw materials (such as those used for the  Craft activity), and relics of long-dead cultures can be used  much like currency: you can sell them for the same Price you  can buy them. |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/4/Text/13` | 0.605176 | materials using the same process as the Craft activity, except as noted here. The original item provides raw materials equal to its price. The DC of the Crafting check to improve an item is determined |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/3/Text/19` | 0.546248 | Higher-level magic and tech items that cost significantly more than 8 times the cost of a mundane item use their listed Price regardless of size. Precious materials, however, have a Price based on the |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/5/Text/6` | 0.544982 | Improvised or of dubious make, shoddy items are never  available for purchase except in the most desperate of  communities. When available, a shoddy item usually costs  half the Price of a standard it |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/21` | 0.543821 | Most items in the following tables have a Price, which is the  amount of currency it typically takes to purchase that item. |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/4/Text/14` | 0.519586 | If you have the formula for the item you can improve an item by supplying UPB equal to half the difference between the two items, but you must work multiple days to reduce the materials needed to comp |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/5/Text/16` | 0.516773 | Price and the item's Craft DC. You must  meet any requirements to Craft the item,  except you don't need to have access to the item |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/5/Text/20` | 0.507857 | *Formulas for all 0-level common items from this chapter  can be purchased collectively in a maker's app. |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/5/Text/10` | 0.481637 | For the Price listed on the table, you can buy a common  formula. A purchased formula is a virtual file downloaded  onto a computer containing the schematics and print-ready  3D models of the item. Pa |

### Query 40
- Text: Summarize UNIVERSAL POLYMER  BASE (UPB)
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/2/SectionHeader/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/2/SectionHeader/2', 'PZO22001 Starfinder Player Core 232-249::/page/2/Text/3', 'PZO22001 Starfinder Player Core 232-249::/page/16/TableCell/111']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/2/SectionHeader/2` | 1.018881 | UNIVERSAL POLYMER  BASE (UPB) |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/3` | 0.799185 | A universal polymer base, or UPB, is a tiny multifunction  component, not much larger than a grain of rice. Used in  the crafting of most common galactic goods, UPBs can be  configured to act as a bra |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/16/TableCell/111` | 0.506898 | Polymer |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/14/TableCell/458` | 0.464898 | Polymer |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/16/TableCell/171` | 0.464898 | Polymer |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/16/TableCell/147` | 0.464898 | Polymer |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/5` | 0.443864 | Characters can use UPBs in place of credits for crafting  items using maker's kits; in fact, they're necessary for the use  of certain tools. |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/4` | 0.434212 | UPBs are so common that they're used as currency in  many major settlements and trade hubs. While credsticks are  a more convenient and secure way to carry value, UPBs have  the advantage of direct ut |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/5/Text/44` | 0.433020 | reducing the cost by 175 UPBs. |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/16/TableCell/383` | 0.392497 | Ultimate |

### Query 41
- Text: What is the rule about A universal polymer base, or UPB, is a tiny multifunction  component, not much larger than a grain of rice. Used in  the crafting of most common galactic goods, UPBs can be  configured to act as a brace, capacitor, circuit, diode, fastener,  insulator, lens, modulator, pipe, resistor, and dozens of other  constituent parts. UPBs can even be spun out into fabric,  broken down into component chemicals, reconstituted into  new chemicals, or supplemented with base materials (such  as dirt or sand) to form massive braces or walls. The right  combination of hundreds or even thousands of UPBs can  create everything from a comm unit to a laser weapon to  powered armor. In their raw form, UPBs have a bulk of 1 per  1,000 UPBs.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/2/Text/3']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/2/Text/3', 'PZO22001 Starfinder Player Core 232-249::/page/2/SectionHeader/2', 'PZO22001 Starfinder Player Core 232-249::/page/2/Text/5']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/3` | 1.007072 | A universal polymer base, or UPB, is a tiny multifunction  component, not much larger than a grain of rice. Used in  the crafting of most common galactic goods, UPBs can be  configured to act as a bra |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/2/SectionHeader/2` | 0.766315 | UNIVERSAL POLYMER  BASE (UPB) |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/5` | 0.634980 | Characters can use UPBs in place of credits for crafting  items using maker's kits; in fact, they're necessary for the use  of certain tools. |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/4` | 0.554061 | UPBs are so common that they're used as currency in  many major settlements and trade hubs. While credsticks are  a more convenient and secure way to carry value, UPBs have  the advantage of direct ut |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/4/Text/14` | 0.489840 | If you have the formula for the item you can improve an item by supplying UPB equal to half the difference between the two items, but you must work multiple days to reduce the materials needed to comp |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/8/Text/10` | 0.481281 | **Maker's** **Toolkit:** You need a maker's toolkit to create items  from UPBs with the Craft skill. A tactical maker's toolkit gives  you a +1 item bonus to the check. |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/4/Text/12` | 0.455435 | A character who is trained or better in Crafting can improve an item using the original item and UPBs (page 234) as raw |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/5/Text/14` | 0.413244 | For example, if Chk Chk wanted to improve his  commercial painglaive into a tactical painglaive the DC  would be 16 and it would cost 350 UPBs to complete  in 1 day. If he uses a formula, he can spend |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/3/Text/18` | 0.405659 | For example, a doshko sized for a Medium creature has a Price of 20 credits and 1 Bulk, so one made for a Huge creature is 80 credits and 4 Bulk. One made for a Tiny creature still costs 20 credits (d |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/13/Text/32` | 0.403780 | **Tech:** This armor incorporates electronics, computer  systems, integrated power sources, and a comm unit. |

### Query 42
- Text: What is the rule about UPBs are so common that they're used as currency in  many major settlements and trade hubs. While credsticks are  a more convenient and secure way to carry value, UPBs have  the advantage of direct utility and untraceability.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/2/Text/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/2/Text/4', 'PZO22001 Starfinder Player Core 232-249::/page/1/Text/17', 'PZO22001 Starfinder Player Core 232-249::/page/1/Text/16']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/4` | 1.009693 | UPBs are so common that they're used as currency in  many major settlements and trade hubs. While credsticks are  a more convenient and secure way to carry value, UPBs have  the advantage of direct ut |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/17` | 0.675502 | Individuals in the Pact Worlds often carry credsticks,  and other civilizations that interact with the Pact often turn  local funds into credits and thus carry them to spend their  converted currency. |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/16` | 0.665874 | Credsticks aren't gateways to the entirety of one's wealth,  and larger stores of credits are often kept secured in banks,  personal vaults, or secure databases. Instead, a credstick  is a safe and an |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/5` | 0.602533 | Characters can use UPBs in place of credits for crafting  items using maker's kits; in fact, they're necessary for the use  of certain tools. |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/12` | 0.594157 | Most people in Starfinder keep their wealth on a protected  item known as a credstick. These devices are often flat and  roughly the size of a human finger. They range in dimensions  and quality, but |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/3` | 0.537474 | A universal polymer base, or UPB, is a tiny multifunction  component, not much larger than a grain of rice. Used in  the crafting of most common galactic goods, UPBs can be  configured to act as a bra |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/15` | 0.535695 | is necessary, they can require audio or biometric imprints  in order to activate. Some advanced credsticks even have a  magical component that might require a mental password or  the recitation of a s |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/10` | 0.473088 | Pact credits themselves are a combination of both digital  and physical currency assets. One person might contain all  their credits on a digital datacrypt that's safeguarded by the  most rigorous of |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/19` | 0.471247 | Art objects, gems, raw materials (such as those used for the  Craft activity), and relics of long-dead cultures can be used  much like currency: you can sell them for the same Price you  can buy them. |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/2/SectionHeader/2` | 0.430531 | UNIVERSAL POLYMER  BASE (UPB) |

### Query 43
- Text: What is the rule about Characters can use UPBs in place of credits for crafting  items using maker's kits; in fact, they're necessary for the use  of certain tools.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/2/Text/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/2/Text/5', 'PZO22001 Starfinder Player Core 232-249::/page/8/Text/10', 'PZO22001 Starfinder Player Core 232-249::/page/4/Text/12']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/5` | 0.989302 | Characters can use UPBs in place of credits for crafting  items using maker's kits; in fact, they're necessary for the use  of certain tools. |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/8/Text/10` | 0.693237 | **Maker's** **Toolkit:** You need a maker's toolkit to create items  from UPBs with the Craft skill. A tactical maker's toolkit gives  you a +1 item bonus to the check. |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/4/Text/12` | 0.646850 | A character who is trained or better in Crafting can improve an item using the original item and UPBs (page 234) as raw |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/4/Text/14` | 0.585685 | If you have the formula for the item you can improve an item by supplying UPB equal to half the difference between the two items, but you must work multiple days to reduce the materials needed to comp |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/4` | 0.531748 | UPBs are so common that they're used as currency in  many major settlements and trade hubs. While credsticks are  a more convenient and secure way to carry value, UPBs have  the advantage of direct ut |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/3` | 0.506722 | A universal polymer base, or UPB, is a tiny multifunction  component, not much larger than a grain of rice. Used in  the crafting of most common galactic goods, UPBs can be  configured to act as a bra |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/6` | 0.505018 | Your character starts out with 150 credits to spend on any  common items from this chapter. Credits are a galactic  currency used to barter and trade for goods in the Starfinder  setting. Items with a |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/7` | 0.505004 | Each item has an item level, which represents the item's  complexity and any magic or technology used in its  construction. Simpler items with a lower level are easier to  construct, and you can't Cra |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/5/Text/15` | 0.503090 | At any time, Chk Chk can  stop upgrading his weapon  and use it at whatever grade he  achieved in the Crafting process,  keeping track of whatever UPBs  he's invested up to that point for  future Craf |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/4/Text/13` | 0.497955 | materials using the same process as the Craft activity, except as noted here. The original item provides raw materials equal to its price. The DC of the Crafting check to improve an item is determined |

### Query 44
- Text: Summarize ITEM LEVEL
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/2/SectionHeader/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/2/SectionHeader/6', 'PZO22001 Starfinder Player Core 232-249::/page/16/TableCell/33', 'PZO22001 Starfinder Player Core 232-249::/page/16/TableCell/258']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/2/SectionHeader/6` | 0.949353 | ITEM LEVEL |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/16/TableCell/33` | 0.829648 | Item Level |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/16/TableCell/258` | 0.829648 | Item Level |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/16/TableCell/186` | 0.787648 | Item Level |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/16/TableCell/66` | 0.787648 | Item Level |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/11/TableCell/743` | 0.595015 | Level |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/9/TableCell/901` | 0.595015 | Level |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/5/TableCell/516` | 0.595015 | Level |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/5/TableCell/518` | 0.595015 | Level |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/8/TableCell/437` | 0.595015 | Level |

### Query 45
- Text: What is the rule about Each item has an item level, which represents the item's  complexity and any magic or technology used in its  construction. Simpler items with a lower level are easier to  construct, and you can't Craft items that have a higher level  than your own (page 197). If an item's level isn't listed, its  level is 0. While characters can use items of any level, GMs  should keep in mind that allowing characters access to items  far above their current level may have a negative impact on  the game.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/2/Text/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/2/Text/7', 'PZO22001 Starfinder Player Core 232-249::/page/4/Text/14', 'PZO22001 Starfinder Player Core 232-249::/page/5/Text/17']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/7` | 1.005931 | Each item has an item level, which represents the item's  complexity and any magic or technology used in its  construction. Simpler items with a lower level are easier to  construct, and you can't Cra |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/4/Text/14` | 0.572983 | If you have the formula for the item you can improve an item by supplying UPB equal to half the difference between the two items, but you must work multiple days to reduce the materials needed to comp |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/5/Text/17` | 0.572090 | or meet any special Craft Requirements listed in the  item's stat block unless the GM determines otherwise. |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/16/TableCell/258` | 0.528197 | Item Level |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/16/TableCell/186` | 0.528197 | Item Level |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/16/TableCell/66` | 0.528197 | Item Level |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/16/TableCell/33` | 0.528197 | Item Level |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/5/Text/16` | 0.523777 | Price and the item's Craft DC. You must  meet any requirements to Craft the item,  except you don't need to have access to the item |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/4/Text/9` | 0.507385 | Armor, shields, and weapons (pages 244, 250, and 253 respectively) are typically listed using their lowest available grade, usually commercial. Each grade beyond the first provides the equipment with |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/3/Text/6` | 0.504385 | These rules for Bulk limits come up most often when a group tries to load up a mount or vehicle. The rules for items of different sizes tend to come into play when the characters defeat a big creature |

### Query 46
- Text: Summarize CARRYING AND USING  ITEMS
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/2/SectionHeader/8']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/2/SectionHeader/8', 'PZO22001 Starfinder Player Core 232-249::/page/2/Text/9', 'PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/309']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/2/SectionHeader/8` | 0.991872 | CARRYING AND USING  ITEMS |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/9` | 0.603238 | A character carries items in three ways: held, worn, and  stowed. Held items are in your hands; a character typically  has two hands, allowing them to hold an item in each hand  or a single two-handed |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/309` | 0.553512 | Draw or put away a worn item, swap one item for another, or pick up an item1 |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/11` | 0.503088 | Equipment on page 235 lists some ways that you might  change the items you're holding or carrying, and the number  of hands you need to do so. |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/3/Text/21` | 0.486959 | Some abilities require you to wield an item, typically a weapon. You're wielding an item any time you're holding it in the number of hands needed to use it effectively. When wielding an item, you're n |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/6/Text/9` | 0.486105 | You can make a set of tools (such as a maker's toolkit or medkit)  easier to use by wearing it. This allows you to draw and replace  the tools as part of the action that uses them. You can wear up  to |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/6/Text/22` | 0.460581 | **Containers:** Containers include backpacks, briefcases, duffel  bags, and handbags. A container holds up to 4 Bulk and the  first 2 Bulk of those items don't count against your Bulk limits.  If you' |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/6/Text/7` | 0.449602 | This lists how many hands it takes to use the item effectively.  Most items that require two hands can be carried in only one  hand, but you must spend an Interact action to change your grip  in order |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/1/SectionHeader/1` | 0.447543 | CHAPTER 6: EQUIPMENT |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/3/SectionHeader/4` | 0.447512 | ITEMS AND SIZES |

### Query 47
- Text: What is the rule about A character carries items in three ways: held, worn, and  stowed. Held items are in your hands; a character typically  has two hands, allowing them to hold an item in each hand  or a single two-handed item using both hands. Worn items  are tucked into pockets, belt pouches, bandoliers, weapon  sheaths, and so forth, and they can be retrieved and returned  relatively quickly. Stowed items are in a backpack or a similar  container, and they're more difficult to access.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/2/Text/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/2/Text/9', 'PZO22001 Starfinder Player Core 232-249::/page/3/Text/21', 'PZO22001 Starfinder Player Core 232-249::/page/6/Text/7']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/9` | 0.985809 | A character carries items in three ways: held, worn, and  stowed. Held items are in your hands; a character typically  has two hands, allowing them to hold an item in each hand  or a single two-handed |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/3/Text/21` | 0.648106 | Some abilities require you to wield an item, typically a weapon. You're wielding an item any time you're holding it in the number of hands needed to use it effectively. When wielding an item, you're n |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/6/Text/7` | 0.629775 | This lists how many hands it takes to use the item effectively.  Most items that require two hands can be carried in only one  hand, but you must spend an Interact action to change your grip  in order |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/11` | 0.544861 | Equipment on page 235 lists some ways that you might  change the items you're holding or carrying, and the number  of hands you need to do so. |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/6/Text/22` | 0.533195 | **Containers:** Containers include backpacks, briefcases, duffel  bags, and handbags. A container holds up to 4 Bulk and the  first 2 Bulk of those items don't count against your Bulk limits.  If you' |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/3/Table/23` | 0.527394 | ChangeHandsActionDraw or put away a worn item, swap one item for another, or pick up an item11 or 2InteractPass an item to or take an item from a willing creature21 or 2InteractDrop an item to the gro |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/2/SectionHeader/8` | 0.526490 | CARRYING AND USING  ITEMS |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/4/ListItem/3` | 0.514855 | 2 A creature must have a hand free for someone to pass an item to them, and they might then need to change their grip if they receive an item requiring two hands to wield or use. |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/4/Table/1` | 0.509097 | ChangeHandsActionChange your grip by removing a hand from an item2ReleaseChange your grip by adding a hand to an item2InteractRetrieve an item from a backpack3, sack, or similar container2Interact |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/7` | 0.509070 | Each item has an item level, which represents the item's  complexity and any magic or technology used in its  construction. Simpler items with a lower level are easier to  construct, and you can't Cra |

### Query 48
- Text: What is the rule about Drawing a worn item or changing how you're carrying an  item usually requires you to use an Interact action (though to  drop an item, you use the Release action instead). Changing?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/2/Text/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/2/Text/10', 'PZO22001 Starfinder Player Core 232-249::/page/3/Table/23', 'PZO22001 Starfinder Player Core 232-249::/page/2/Text/12']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/10` | 0.989640 | Drawing a worn item or changing how you're carrying an  item usually requires you to use an Interact action (though to  drop an item, you use the Release action instead). Changing |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/3/Table/23` | 0.737129 | ChangeHandsActionDraw or put away a worn item, swap one item for another, or pick up an item11 or 2InteractPass an item to or take an item from a willing creature21 or 2InteractDrop an item to the gro |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/12` | 0.733292 | Many ways of using items require you to spend multiple  actions. For example, drinking a serum worn at your belt  requires using an Interact action to draw it and then using  a second action to drink |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/309` | 0.636658 | Draw or put away a worn item, swap one item for another, or pick up an item1 |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/6/Text/9` | 0.621356 | You can make a set of tools (such as a maker's toolkit or medkit)  easier to use by wearing it. This allows you to draw and replace  the tools as part of the action that uses them. You can wear up  to |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/4/Table/1` | 0.601056 | ChangeHandsActionChange your grip by removing a hand from an item2ReleaseChange your grip by adding a hand to an item2InteractRetrieve an item from a backpack3, sack, or similar container2Interact |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/6/Text/7` | 0.564004 | This lists how many hands it takes to use the item effectively.  Most items that require two hands can be carried in only one  hand, but you must spend an Interact action to change your grip  in order |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/3/Text/21` | 0.538791 | Some abilities require you to wield an item, typically a weapon. You're wielding an item any time you're holding it in the number of hands needed to use it effectively. When wielding an item, you're n |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/4/ListItem/4` | 0.530715 | 3 Retrieving an item stowed in your own backpack requires first taking off the backpack with a separate Interact action. |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/11` | 0.512339 | Equipment on page 235 lists some ways that you might  change the items you're holding or carrying, and the number  of hands you need to do so. |

### Query 49
- Text: Summarize Equipment on page 235 lists some ways that you might  change the items you're holding or carrying, and the number  of hands you need to do so.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/2/Text/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/2/Text/11', 'PZO22001 Starfinder Player Core 232-249::/page/6/Text/7', 'PZO22001 Starfinder Player Core 232-249::/page/9/Text/3']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/11` | 1.021531 | Equipment on page 235 lists some ways that you might  change the items you're holding or carrying, and the number  of hands you need to do so. |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/6/Text/7` | 0.673438 | This lists how many hands it takes to use the item effectively.  Most items that require two hands can be carried in only one  hand, but you must spend an Interact action to change your grip  in order |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/9/Text/3` | 0.670546 | *You can use a toolkit with 1 hand if you're wearing it or 2  if you're holding it. See page 238 for details. |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/4/Table/1` | 0.593861 | ChangeHandsActionChange your grip by removing a hand from an item2ReleaseChange your grip by adding a hand to an item2InteractRetrieve an item from a backpack3, sack, or similar container2Interact |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/3/Text/21` | 0.567718 | Some abilities require you to wield an item, typically a weapon. You're wielding an item any time you're holding it in the number of hands needed to use it effectively. When wielding an item, you're n |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/4/TableCell/192` | 0.564008 | Change your grip by adding a hand to an item |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/9` | 0.556738 | A character carries items in three ways: held, worn, and  stowed. Held items are in your hands; a character typically  has two hands, allowing them to hold an item in each hand  or a single two-handed |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/4/ListItem/2` | 0.554990 | 1 If you retrieve a two-handed item with only one hand, you still need to change your grip before you can wield or use it |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/3/Table/23` | 0.552263 | ChangeHandsActionDraw or put away a worn item, swap one item for another, or pick up an item11 or 2InteractPass an item to or take an item from a willing creature21 or 2InteractDrop an item to the gro |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/4/TableCell/189` | 0.540120 | Change your grip by removing a hand from an item |

### Query 50
- Text: What is the rule about Many ways of using items require you to spend multiple  actions. For example, drinking a serum worn at your belt  requires using an Interact action to draw it and then using  a second action to drink it as described in its Activate entry  (page 242).?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/2/Text/12']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/2/Text/12', 'PZO22001 Starfinder Player Core 232-249::/page/2/Text/10', 'PZO22001 Starfinder Player Core 232-249::/page/6/Text/7']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/12` | 1.002496 | Many ways of using items require you to spend multiple  actions. For example, drinking a serum worn at your belt  requires using an Interact action to draw it and then using  a second action to drink |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/10` | 0.709794 | Drawing a worn item or changing how you're carrying an  item usually requires you to use an Interact action (though to  drop an item, you use the Release action instead). Changing |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/6/Text/7` | 0.659747 | This lists how many hands it takes to use the item effectively.  Most items that require two hands can be carried in only one  hand, but you must spend an Interact action to change your grip  in order |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/6/Text/9` | 0.593534 | You can make a set of tools (such as a maker's toolkit or medkit)  easier to use by wearing it. This allows you to draw and replace  the tools as part of the action that uses them. You can wear up  to |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/10/Text/32` | 0.591179 | These are pharmaceutical serums; they're technological, or  hybrid in some cases, but can be crafted using a laboratory and  don't incorporate significant magic. You can activate a serum  with an Inte |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/3/Table/23` | 0.563617 | ChangeHandsActionDraw or put away a worn item, swap one item for another, or pick up an item11 or 2InteractPass an item to or take an item from a willing creature21 or 2InteractDrop an item to the gro |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/4/Table/1` | 0.550819 | ChangeHandsActionChange your grip by removing a hand from an item2ReleaseChange your grip by adding a hand to an item2InteractRetrieve an item from a backpack3, sack, or similar container2Interact |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/9/Text/7` | 0.540781 | Some medical items have the tech trait. Some also have the  consumable trait, which means that the item is used up once  activated. Rules for creating medical items are found in the Craft  activity on |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/3/Text/21` | 0.540130 | Some abilities require you to wield an item, typically a weapon. You're wielding an item any time you're holding it in the number of hands needed to use it effectively. When wielding an item, you're n |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/4/ListItem/4` | 0.514621 | 3 Retrieving an item stowed in your own backpack requires first taking off the backpack with a separate Interact action. |

### Query 51
- Text: Summarize BULK
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/2/SectionHeader/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/2/SectionHeader/13', 'PZO22001 Starfinder Player Core 232-249::/page/13/SectionHeader/15', 'PZO22001 Starfinder Player Core 232-249::/page/16/TableCell/193']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/2/SectionHeader/13` | 0.937179 | BULK |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/13/SectionHeader/15` | 0.937179 | BULK |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/16/TableCell/193` | 0.778299 | Bulk |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/11/TableCell/745` | 0.736299 | Bulk |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/2/TableCell/338` | 0.736299 | Bulk |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/16/TableCell/73` | 0.736299 | Bulk |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/9/TableCell/903` | 0.736299 | Bulk |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/8/TableCell/439` | 0.736299 | Bulk |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/16/TableCell/39` | 0.736299 | Bulk |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/16/TableCell/265` | 0.736299 | Bulk |

### Query 52
- Text: What is the rule about Carrying especially heavy or unwieldy items can make it  more difficult for you to move, as can overloading yourself  with too much gear. The Bulk value of an item reflects how  difficult the item is to handle, representing its size, weight,  and general awkwardness. If you have a high Strength  modifier, you usually don't need to worry about Bulk unless  you're carrying numerous substantial items.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/2/Text/14']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/2/Text/14', 'PZO22001 Starfinder Player Core 232-249::/page/2/Text/16', 'PZO22001 Starfinder Player Core 232-249::/page/2/Text/20']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/14` | 1.005580 | Carrying especially heavy or unwieldy items can make it  more difficult for you to move, as can overloading yourself  with too much gear. The Bulk value of an item reflects how  difficult the item is |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/16` | 0.776647 | You can carry an amount of Bulk equal to 5 plus your  Strength modifier without penalty; if you carry more, you  gain the encumbered condition. You can't hold or carry more  Bulk than 10 plus your Str |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/20` | 0.710413 | As a general rule, an item that weighs 5 to 10 pounds is 1  Bulk, an item weighing less than a few ounces is negligible,  and anything in between is light. Particularly awkward or  unwieldy items migh |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/3/Text/6` | 0.633331 | These rules for Bulk limits come up most often when a group tries to load up a mount or vehicle. The rules for items of different sizes tend to come into play when the characters defeat a big creature |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/18` | 0.585472 | Items can have a number to indicate their Bulk value, or  they can be light (indicated by an L) or negligible (indicated  by a —) for the purpose of determining Bulk. For instance,  defiance series ar |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/3/Text/9` | 0.584506 | As shown in the Bulk Conversions table, Large or larger creatures are less encumbered by bulky items than Small or Medium creatures, while Tiny creatures become overburdened more quickly. A Large crea |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/3/Text/5` | 0.576968 | The Bulk rules in this chapter are for Small, Medium, and Large creatures, as most ancestries are these sizes; however, other uncommon or rare ancestries might be larger or smaller and require items s |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/22` | 0.575346 | You might need to know the Bulk of a creature, especially if  you need to carry someone off the battlefield. The following  table lists the typical Bulk of a creature based on its size,  but the GM mi |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/3/Text/3` | 0.570015 | In some situations, you might drag an object or creature rather than carry it. If you're dragging something, treat its Bulk as half. Typically, you can drag one thing at a time, you must use both hand |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/13/Text/16` | 0.549565 | This entry gives the armor's Bulk, assuming you're wearing  the armor and distributing its weight across your body. A  suit of armor that's carried usually has 1 more Bulk than  what's listed here (or |

### Query 53
- Text: Summarize Bulk Limits
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/2/SectionHeader/15']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/2/SectionHeader/15', 'PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/249', 'PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/265']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/2/SectionHeader/15` | 0.961380 | Bulk Limits |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/249` | 0.929889 | Bulk Limit |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/265` | 0.929889 | Bulk Limit |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/9/TableCell/903` | 0.662776 | Bulk |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/2/TableCell/338` | 0.662776 | Bulk |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/11/TableCell/745` | 0.662776 | Bulk |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/16/TableCell/73` | 0.662776 | Bulk |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/11/TableCell/760` | 0.662776 | Bulk |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/9/TableCell/1108` | 0.662776 | Bulk |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/16/TableCell/193` | 0.662776 | Bulk |

### Query 54
- Text: What is the rule about You can carry an amount of Bulk equal to 5 plus your  Strength modifier without penalty; if you carry more, you  gain the encumbered condition. You can't hold or carry more  Bulk than 10 plus your Strength modifier.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/2/Text/16']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/2/Text/16', 'PZO22001 Starfinder Player Core 232-249::/page/2/Text/14', 'PZO22001 Starfinder Player Core 232-249::/page/3/Text/6']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/16` | 1.003585 | You can carry an amount of Bulk equal to 5 plus your  Strength modifier without penalty; if you carry more, you  gain the encumbered condition. You can't hold or carry more  Bulk than 10 plus your Str |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/14` | 0.727218 | Carrying especially heavy or unwieldy items can make it  more difficult for you to move, as can overloading yourself  with too much gear. The Bulk value of an item reflects how  difficult the item is |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/3/Text/6` | 0.632606 | These rules for Bulk limits come up most often when a group tries to load up a mount or vehicle. The rules for items of different sizes tend to come into play when the characters defeat a big creature |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/13/Text/14` | 0.584676 | This entry indicates the Strength modifier at which you are  strong enough to overcome some of the armor's penalties.  If your Strength modifier is equal to or greater than this  value, you no longer |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/13/Text/16` | 0.578602 | This entry gives the armor's Bulk, assuming you're wearing  the armor and distributing its weight across your body. A  suit of armor that's carried usually has 1 more Bulk than  what's listed here (or |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/18` | 0.576795 | Items can have a number to indicate their Bulk value, or  they can be light (indicated by an L) or negligible (indicated  by a —) for the purpose of determining Bulk. For instance,  defiance series ar |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/20` | 0.564732 | As a general rule, an item that weighs 5 to 10 pounds is 1  Bulk, an item weighing less than a few ounces is negligible,  and anything in between is light. Particularly awkward or  unwieldy items migh |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/3/Text/5` | 0.551557 | The Bulk rules in this chapter are for Small, Medium, and Large creatures, as most ancestries are these sizes; however, other uncommon or rare ancestries might be larger or smaller and require items s |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/6/Text/22` | 0.536952 | **Containers:** Containers include backpacks, briefcases, duffel  bags, and handbags. A container holds up to 4 Bulk and the  first 2 Bulk of those items don't count against your Bulk limits.  If you' |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/3/Text/9` | 0.536435 | As shown in the Bulk Conversions table, Large or larger creatures are less encumbered by bulky items than Small or Medium creatures, while Tiny creatures become overburdened more quickly. A Large crea |

### Query 55
- Text: Summarize Bulk Values
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/2/SectionHeader/17']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/2/SectionHeader/17', 'PZO22001 Starfinder Player Core 232-249::/page/2/TableCell/338', 'PZO22001 Starfinder Player Core 232-249::/page/16/TableCell/265']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/2/SectionHeader/17` | 0.909562 | Bulk Values |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/2/TableCell/338` | 0.726844 | Bulk |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/16/TableCell/265` | 0.726844 | Bulk |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/9/TableCell/903` | 0.684844 | Bulk |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/278` | 0.684844 | Bulk |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/11/TableCell/760` | 0.684844 | Bulk |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/16/TableCell/193` | 0.684844 | Bulk |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/237` | 0.684844 | Bulk |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/9/TableCell/1108` | 0.684844 | Bulk |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/8/TableCell/439` | 0.684844 | Bulk |

### Query 56
- Text: What is the rule about Items can have a number to indicate their Bulk value, or  they can be light (indicated by an L) or negligible (indicated  by a —) for the purpose of determining Bulk. For instance,  defiance series armor is 3 Bulk, a dueling sword is 1 Bulk, a  knife or *spell gem* is light, and a credstick is negligible. Ten  light items count as 1 Bulk, and you round down fractions  (so 9 light items count as 0 Bulk, and 11 light items count  as 1 Bulk). Items of negligible Bulk don't count toward Bulk  unless you try to carry vast numbers of them, as determined  by the GM.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/2/Text/18']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/2/Text/18', 'PZO22001 Starfinder Player Core 232-249::/page/2/Text/20', 'PZO22001 Starfinder Player Core 232-249::/page/3/Text/9']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/18` | 1.004728 | Items can have a number to indicate their Bulk value, or  they can be light (indicated by an L) or negligible (indicated  by a —) for the purpose of determining Bulk. For instance,  defiance series ar |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/20` | 0.750111 | As a general rule, an item that weighs 5 to 10 pounds is 1  Bulk, an item weighing less than a few ounces is negligible,  and anything in between is light. Particularly awkward or  unwieldy items migh |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/3/Text/9` | 0.691326 | As shown in the Bulk Conversions table, Large or larger creatures are less encumbered by bulky items than Small or Medium creatures, while Tiny creatures become overburdened more quickly. A Large crea |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/13/Text/16` | 0.628511 | This entry gives the armor's Bulk, assuming you're wearing  the armor and distributing its weight across your body. A  suit of armor that's carried usually has 1 more Bulk than  what's listed here (or |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/3/Text/17` | 0.624212 | * An item that would have its Bulk reduced below 1 has light Bulk. |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/3/Text/6` | 0.600024 | These rules for Bulk limits come up most often when a group tries to load up a mount or vehicle. The rules for items of different sizes tend to come into play when the characters defeat a big creature |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/14` | 0.590369 | Carrying especially heavy or unwieldy items can make it  more difficult for you to move, as can overloading yourself  with too much gear. The Bulk value of an item reflects how  difficult the item is |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/3/Text/5` | 0.585235 | The Bulk rules in this chapter are for Small, Medium, and Large creatures, as most ancestries are these sizes; however, other uncommon or rare ancestries might be larger or smaller and require items s |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/16` | 0.572049 | You can carry an amount of Bulk equal to 5 plus your  Strength modifier without penalty; if you carry more, you  gain the encumbered condition. You can't hold or carry more  Bulk than 10 plus your Str |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/22` | 0.564528 | You might need to know the Bulk of a creature, especially if  you need to carry someone off the battlefield. The following  table lists the typical Bulk of a creature based on its size,  but the GM mi |

### Query 57
- Text: Summarize Estimating an Item's Bulk
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/2/SectionHeader/19']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/2/SectionHeader/19', 'PZO22001 Starfinder Player Core 232-249::/page/2/Text/18', 'PZO22001 Starfinder Player Core 232-249::/page/9/TableCell/903']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/2/SectionHeader/19` | 0.979435 | Estimating an Item's Bulk |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/18` | 0.606738 | Items can have a number to indicate their Bulk value, or  they can be light (indicated by an L) or negligible (indicated  by a —) for the purpose of determining Bulk. For instance,  defiance series ar |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/9/TableCell/903` | 0.598502 | Bulk |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/2/SectionHeader/17` | 0.559610 | Bulk Values |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/16/TableCell/73` | 0.556502 | Bulk |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/11/TableCell/745` | 0.556502 | Bulk |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/16/TableCell/193` | 0.556502 | Bulk |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/2/TableCell/338` | 0.556502 | Bulk |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/9/TableCell/1108` | 0.556501 | Bulk |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/237` | 0.556501 | Bulk |

### Query 58
- Text: Summarize As a general rule, an item that weighs 5 to 10 pounds is 1  Bulk, an item weighing less than a few ounces is negligible,  and anything in between is light. Particularly awkward or  unwieldy items might have higher Bulk values. For example,  a 10-foot pole isn't heavy, but its length makes it difficult for  you to move while you have one on your person, so its Bulk is  1. Items made for larger or smaller creatures have greater or  lesser Bulk, as described on page 235.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/2/Text/20']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/2/Text/20', 'PZO22001 Starfinder Player Core 232-249::/page/2/Text/18', 'PZO22001 Starfinder Player Core 232-249::/page/3/Text/9']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/20` | 1.046190 | As a general rule, an item that weighs 5 to 10 pounds is 1  Bulk, an item weighing less than a few ounces is negligible,  and anything in between is light. Particularly awkward or  unwieldy items migh |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/18` | 0.773757 | Items can have a number to indicate their Bulk value, or  they can be light (indicated by an L) or negligible (indicated  by a —) for the purpose of determining Bulk. For instance,  defiance series ar |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/3/Text/9` | 0.762396 | As shown in the Bulk Conversions table, Large or larger creatures are less encumbered by bulky items than Small or Medium creatures, while Tiny creatures become overburdened more quickly. A Large crea |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/3/Text/5` | 0.702808 | The Bulk rules in this chapter are for Small, Medium, and Large creatures, as most ancestries are these sizes; however, other uncommon or rare ancestries might be larger or smaller and require items s |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/14` | 0.691014 | Carrying especially heavy or unwieldy items can make it  more difficult for you to move, as can overloading yourself  with too much gear. The Bulk value of an item reflects how  difficult the item is |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/22` | 0.675257 | You might need to know the Bulk of a creature, especially if  you need to carry someone off the battlefield. The following  table lists the typical Bulk of a creature based on its size,  but the GM mi |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/3/Text/14` | 0.649852 | Creatures of sizes other than Small, Medium, or Large need items appropriate to their size. These items have different Bulk and possibly a different Price. The Differently Sized Items table provides t |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/13/Text/16` | 0.617149 | This entry gives the armor's Bulk, assuming you're wearing  the armor and distributing its weight across your body. A  suit of armor that's carried usually has 1 more Bulk than  what's listed here (or |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/3/Text/17` | 0.616910 | * An item that would have its Bulk reduced below 1 has light Bulk. |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/3/Text/6` | 0.608838 | These rules for Bulk limits come up most often when a group tries to load up a mount or vehicle. The rules for items of different sizes tend to come into play when the characters defeat a big creature |

### Query 59
- Text: Summarize Bulk of Creatures
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/2/SectionHeader/21']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/2/SectionHeader/21', 'PZO22001 Starfinder Player Core 232-249::/page/2/Text/22', 'PZO22001 Starfinder Player Core 232-249::/page/2/TableCell/337']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/2/SectionHeader/21` | 0.936097 | Bulk of Creatures |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/22` | 0.687460 | You might need to know the Bulk of a creature, especially if  you need to carry someone off the battlefield. The following  table lists the typical Bulk of a creature based on its size,  but the GM mi |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/2/TableCell/337` | 0.655000 | Size Of Creature |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/236` | 0.613000 | Size Of Creature |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/2/TableCell/338` | 0.610050 | Bulk |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/2/SectionHeader/23` | 0.598298 | **BULK OF CREATURES** |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/9/TableCell/903` | 0.598051 | Bulk |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/9/TableCell/1108` | 0.598050 | Bulk |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/237` | 0.598050 | Bulk |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/16/TableCell/73` | 0.598050 | Bulk |

### Query 60
- Text: What is the rule about You might need to know the Bulk of a creature, especially if  you need to carry someone off the battlefield. The following  table lists the typical Bulk of a creature based on its size,  but the GM might adjust this number. Constructs or many  creatures with the Tech trait weigh more.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/2/Text/22']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/2/Text/22', 'PZO22001 Starfinder Player Core 232-249::/page/3/Text/5', 'PZO22001 Starfinder Player Core 232-249::/page/2/Text/20']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/22` | 1.003240 | You might need to know the Bulk of a creature, especially if  you need to carry someone off the battlefield. The following  table lists the typical Bulk of a creature based on its size,  but the GM mi |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/3/Text/5` | 0.744848 | The Bulk rules in this chapter are for Small, Medium, and Large creatures, as most ancestries are these sizes; however, other uncommon or rare ancestries might be larger or smaller and require items s |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/20` | 0.711813 | As a general rule, an item that weighs 5 to 10 pounds is 1  Bulk, an item weighing less than a few ounces is negligible,  and anything in between is light. Particularly awkward or  unwieldy items migh |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/3/Text/6` | 0.679052 | These rules for Bulk limits come up most often when a group tries to load up a mount or vehicle. The rules for items of different sizes tend to come into play when the characters defeat a big creature |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/3/Text/18` | 0.667451 | For example, a doshko sized for a Medium creature has a Price of 20 credits and 1 Bulk, so one made for a Huge creature is 80 credits and 4 Bulk. One made for a Tiny creature still costs 20 credits (d |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/3/Text/9` | 0.661467 | As shown in the Bulk Conversions table, Large or larger creatures are less encumbered by bulky items than Small or Medium creatures, while Tiny creatures become overburdened more quickly. A Large crea |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/13/Text/16` | 0.646344 | This entry gives the armor's Bulk, assuming you're wearing  the armor and distributing its weight across your body. A  suit of armor that's carried usually has 1 more Bulk than  what's listed here (or |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/14` | 0.608773 | Carrying especially heavy or unwieldy items can make it  more difficult for you to move, as can overloading yourself  with too much gear. The Bulk value of an item reflects how  difficult the item is |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/18` | 0.598720 | Items can have a number to indicate their Bulk value, or  they can be light (indicated by an L) or negligible (indicated  by a —) for the purpose of determining Bulk. For instance,  defiance series ar |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/3/Text/14` | 0.588258 | Creatures of sizes other than Small, Medium, or Large need items appropriate to their size. These items have different Bulk and possibly a different Price. The Differently Sized Items table provides t |

### Query 61
- Text: Summarize **BULK OF CREATURES**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/2/SectionHeader/23']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/2/SectionHeader/23', 'PZO22001 Starfinder Player Core 232-249::/page/2/SectionHeader/21', 'PZO22001 Starfinder Player Core 232-249::/page/3/SectionHeader/10']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/2/SectionHeader/23` | 0.991454 | **BULK OF CREATURES** |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/2/SectionHeader/21` | 0.722882 | Bulk of Creatures |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/3/SectionHeader/10` | 0.580224 | **BULK CONVERSIONS ** |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/2/Table/24` | 0.508006 | Size Of CreatureBulkTiny1 |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/13/SectionHeader/15` | 0.502866 | BULK |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/2/SectionHeader/13` | 0.502866 | BULK |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/11/TableCell/745` | 0.487224 | Bulk |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/9/TableCell/903` | 0.487224 | Bulk |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/278` | 0.487224 | Bulk |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/16/TableCell/193` | 0.487224 | Bulk |

### Query 62
- Text: Lookup values for Size Of CreatureBulkTiny1
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/2/Table/24']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/2/Table/24', 'PZO22001 Starfinder Player Core 232-249::/page/3/Table/1', 'PZO22001 Starfinder Player Core 232-249::/page/3/Table/16']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/2/Table/24` | 0.951754 | Size Of CreatureBulkTiny1 |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/3/Table/1` | 0.743920 | Size Of CreatureBulkSmall3Medium6Large12Huge24Gargantuan48 |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/3/Table/16` | 0.673080 | Creature SizePriceBulkLight BecomesNegligible BecomesTinyStandardHalf*_-Small or Med.StandardStandardL-LargeStandard×21 BulkLHuge×4×42 Bulk1 BulkGargantuan×8×84 Bulk2 Bulk |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/2/TableCell/337` | 0.639249 | Size Of Creature |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/236` | 0.639249 | Size Of Creature |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/276` | 0.624428 | Creature Size |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/264` | 0.612428 | Creature Size |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/248` | 0.612428 | Creature Size |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/3/Table/11` | 0.601315 | Creature SizeBulk LimitTreats as LightTreats as NegligibleTinyHalf-noneSmall or Med.StandardL-Large×21 BulkL |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/22` | 0.591587 | You might need to know the Bulk of a creature, especially if  you need to carry someone off the battlefield. The following  table lists the typical Bulk of a creature based on its size,  but the GM mi |

### Query 63
- Text: Summarize Size Of Creature
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/2/TableCell/337']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/2/TableCell/337', 'PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/236', 'PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/264']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/2/TableCell/337` | 0.939625 | Size Of Creature |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/236` | 0.939625 | Size Of Creature |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/264` | 0.910555 | Creature Size |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/276` | 0.868555 | Creature Size |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/248` | 0.868555 | Creature Size |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/2/SectionHeader/21` | 0.658788 | Bulk of Creatures |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/3/Table/1` | 0.634990 | Size Of CreatureBulkSmall3Medium6Large12Huge24Gargantuan48 |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/2/Table/24` | 0.624177 | Size Of CreatureBulkTiny1 |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/22` | 0.607530 | You might need to know the Bulk of a creature, especially if  you need to carry someone off the battlefield. The following  table lists the typical Bulk of a creature based on its size,  but the GM mi |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/3/Text/14` | 0.551310 | Creatures of sizes other than Small, Medium, or Large need items appropriate to their size. These items have different Bulk and possibly a different Price. The Differently Sized Items table provides t |

### Query 64
- Text: Summarize Bulk
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/2/TableCell/338']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/11/TableCell/745', 'PZO22001 Starfinder Player Core 232-249::/page/2/TableCell/338', 'PZO22001 Starfinder Player Core 232-249::/page/9/TableCell/903']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/11/TableCell/745` | 0.845513 | Bulk |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/2/TableCell/338` | 0.845513 | Bulk |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/9/TableCell/903` | 0.845513 | Bulk |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/16/TableCell/73` | 0.803513 | Bulk |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/278` | 0.803513 | Bulk |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/237` | 0.803513 | Bulk |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/8/TableCell/439` | 0.803513 | Bulk |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/16/TableCell/193` | 0.803513 | Bulk |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/16/TableCell/265` | 0.803513 | Bulk |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/16/TableCell/39` | 0.803513 | Bulk |

### Query 65
- Text: Summarize Tiny
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/2/TableCell/339']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/2/TableCell/339', 'PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/252', 'PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/281']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/2/TableCell/339` | 0.890088 | Tiny |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/252` | 0.890088 | Tiny |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/281` | 0.890088 | Tiny |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/238` | 0.533334 | Small |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/2/Table/24` | 0.410822 | Size Of CreatureBulkTiny1 |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/286` | 0.395762 | Small or Med. |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/256` | 0.395762 | Small or Med. |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/3/Text/9` | 0.393597 | As shown in the Bulk Conversions table, Large or larger creatures are less encumbered by bulky items than Small or Medium creatures, while Tiny creatures become overburdened more quickly. A Large crea |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/10/Text/17` | 0.331292 | This tiny cylinder contains specialized nanites. Different  types have different effects. |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/11/TableCell/864` | 0.316621 | Fine |

### Query 66
- Text: Summarize 1
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/2/TableCell/340']
- Expected found: `True`
- Expected rank: `30`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/16/TableCell/55', 'PZO22001 Starfinder Player Core 232-249::/page/11/TableCell/811', 'PZO22001 Starfinder Player Core 232-249::/page/16/TableCell/321']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/16/TableCell/55` | 0.669108 | 1 |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/11/TableCell/811` | 0.669108 | 1 |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/16/TableCell/321` | 0.669108 | 1 |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/11/TableCell/776` | 0.627108 | 1 |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/9/TableCell/1103` | 0.627108 | 1 |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/11/TableCell/766` | 0.627108 | 1 |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/16/TableCell/254` | 0.627108 | 1 |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/9/TableCell/1149` | 0.627108 | 1 |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/9/TableCell/931` | 0.627108 | 1 |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/16/TableCell/241` | 0.627108 | 1 |

### Query 67
- Text: Lookup values for Size Of CreatureBulkSmall3Medium6Large12Huge24Gargantuan48
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/3/Table/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/3/Table/1', 'PZO22001 Starfinder Player Core 232-249::/page/3/Table/16', 'PZO22001 Starfinder Player Core 232-249::/page/2/Table/24']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/3/Table/1` | 0.981054 | Size Of CreatureBulkSmall3Medium6Large12Huge24Gargantuan48 |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/3/Table/16` | 0.768294 | Creature SizePriceBulkLight BecomesNegligible BecomesTinyStandardHalf*_-Small or Med.StandardStandardL-LargeStandard×21 BulkLHuge×4×42 Bulk1 BulkGargantuan×8×84 Bulk2 Bulk |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/2/Table/24` | 0.748664 | Size Of CreatureBulkTiny1 |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/3/Table/12` | 0.689727 | Creature SizeBulk LimitTreats as LightTreats as NegligibleHuge×42 Bulk1 BulkGargantuan×84 Bulk2 Bulk |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/236` | 0.649325 | Size Of Creature |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/2/TableCell/337` | 0.649325 | Size Of Creature |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/3/Table/11` | 0.642816 | Creature SizeBulk LimitTreats as LightTreats as NegligibleTinyHalf-noneSmall or Med.StandardL-Large×21 BulkL |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/276` | 0.623805 | Creature Size |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/264` | 0.611805 | Creature Size |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/248` | 0.611805 | Creature Size |

### Query 68
- Text: Summarize Size Of Creature
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/236']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/2/TableCell/337', 'PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/236', 'PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/264']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/2/TableCell/337` | 0.939625 | Size Of Creature |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/236` | 0.939625 | Size Of Creature |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/264` | 0.910555 | Creature Size |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/276` | 0.868555 | Creature Size |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/248` | 0.868555 | Creature Size |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/2/SectionHeader/21` | 0.658788 | Bulk of Creatures |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/3/Table/1` | 0.634990 | Size Of CreatureBulkSmall3Medium6Large12Huge24Gargantuan48 |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/2/Table/24` | 0.624177 | Size Of CreatureBulkTiny1 |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/22` | 0.607530 | You might need to know the Bulk of a creature, especially if  you need to carry someone off the battlefield. The following  table lists the typical Bulk of a creature based on its size,  but the GM mi |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/3/Text/14` | 0.551310 | Creatures of sizes other than Small, Medium, or Large need items appropriate to their size. These items have different Bulk and possibly a different Price. The Differently Sized Items table provides t |

### Query 69
- Text: Summarize Bulk
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/237']
- Expected found: `True`
- Expected rank: `4`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/16/TableCell/73', 'PZO22001 Starfinder Player Core 232-249::/page/9/TableCell/1108', 'PZO22001 Starfinder Player Core 232-249::/page/8/TableCell/439']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/16/TableCell/73` | 0.845513 | Bulk |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/9/TableCell/1108` | 0.845513 | Bulk |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/8/TableCell/439` | 0.845513 | Bulk |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/237` | 0.803513 | Bulk |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/11/TableCell/760` | 0.803513 | Bulk |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/9/TableCell/903` | 0.803513 | Bulk |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/278` | 0.803513 | Bulk |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/16/TableCell/265` | 0.803513 | Bulk |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/16/TableCell/39` | 0.803513 | Bulk |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/2/TableCell/338` | 0.803513 | Bulk |

### Query 70
- Text: Summarize Small
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/238']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/238', 'PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/256', 'PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/286']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/238` | 0.802352 | Small |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/256` | 0.594295 | Small or Med. |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/286` | 0.594295 | Small or Med. |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/2/TableCell/339` | 0.505059 | Tiny |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/281` | 0.505059 | Tiny |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/252` | 0.505059 | Tiny |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/3/Text/14` | 0.375191 | Creatures of sizes other than Small, Medium, or Large need items appropriate to their size. These items have different Bulk and possibly a different Price. The Differently Sized Items table provides t |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/242` | 0.374583 | Large |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/291` | 0.374583 | Large |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/260` | 0.374583 | Large |

### Query 71
- Text: Summarize 3
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/239']
- Expected found: `True`
- Expected rank: `22`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/9/TableCell/1166', 'PZO22001 Starfinder Player Core 232-249::/page/14/TableCell/459', 'PZO22001 Starfinder Player Core 232-249::/page/9/TableCell/1126']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/9/TableCell/1166` | 0.731895 | 3 |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/14/TableCell/459` | 0.731895 | 3 |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/9/TableCell/1126` | 0.731895 | 3 |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/9/TableCell/941` | 0.689895 | 3 |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/9/TableCell/926` | 0.689895 | 3 |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/9/TableCell/971` | 0.689895 | 3 |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/9/TableCell/976` | 0.689895 | 3 |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/16/TableCell/81` | 0.689895 | 3 |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/9/TableCell/1156` | 0.689895 | 3 |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/9/TableCell/1021` | 0.689895 | 3 |

### Query 72
- Text: Summarize Medium
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/240']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/240', 'PZO22001 Starfinder Player Core 232-249::/page/16/SectionHeader/5', 'PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/286']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/240` | 0.796743 | Medium |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/16/SectionHeader/5` | 0.523245 | **MEDIUM ARMOR ** |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/286` | 0.397166 | Small or Med. |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/256` | 0.355166 | Small or Med. |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/283` | 0.347256 | Half* |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/253` | 0.345986 | Half |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/14/Text/12` | 0.337267 | 1 + the armor's resilience value for medium armor, or 2 + the  armor's resilience value for heavy armor. |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/287` | 0.320748 | Standard |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/14/TableCell/430` | 0.318144 | Material |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/292` | 0.308748 | Standard |

### Query 73
- Text: Summarize 6
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/241']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/11/TableCell/808', 'PZO22001 Starfinder Player Core 232-249::/page/5/TableCell/544', 'PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/241']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/11/TableCell/808` | 0.783525 | 6 |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/5/TableCell/544` | 0.783525 | 6 |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/241` | 0.783525 | 6 |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/14/TableCell/461` | 0.741525 | 6 |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/11/TableCell/878` | 0.627172 | 6th |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/16/TableCell/332` | 0.581237 | +6 |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/16/TableCell/308` | 0.581237 | +6 |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/16/TableCell/272` | 0.581237 | +6 |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/14/TableCell/447` | 0.496931 | 7 |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/5/TableCell/548` | 0.496931 | 7 |

### Query 74
- Text: Summarize Large
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/242']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/291', 'PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/260', 'PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/242']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/291` | 0.758356 | Large |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/260` | 0.758356 | Large |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/242` | 0.758356 | Large |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/296` | 0.461130 | Huge |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/244` | 0.461130 | Huge |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/268` | 0.461130 | Huge |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/3/Text/14` | 0.385776 | Creatures of sizes other than Small, Medium, or Large need items appropriate to their size. These items have different Bulk and possibly a different Price. The Differently Sized Items table provides t |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/3/Text/9` | 0.374595 | As shown in the Bulk Conversions table, Large or larger creatures are less encumbered by bulky items than Small or Medium creatures, while Tiny creatures become overburdened more quickly. A Large crea |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/3/Text/5` | 0.364644 | The Bulk rules in this chapter are for Small, Medium, and Large creatures, as most ancestries are these sizes; however, other uncommon or rare ancestries might be larger or smaller and require items s |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/238` | 0.357427 | Small |

### Query 75
- Text: Summarize 12
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/243']
- Expected found: `True`
- Expected rank: `5`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/9/TableCell/986', 'PZO22001 Starfinder Player Core 232-249::/page/11/TableCell/828', 'PZO22001 Starfinder Player Core 232-249::/page/14/TableCell/460']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/9/TableCell/986` | 0.783360 | 12 |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/11/TableCell/828` | 0.783360 | 12 |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/14/TableCell/460` | 0.783360 | 12 |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/5/TableCell/526` | 0.741360 | 12 |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/243` | 0.741360 | 12 |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/11/TableCell/823` | 0.524768 | 13 |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/5/TableCell/530` | 0.524768 | 13 |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/16/TableCell/370` | 0.515039 | 11 |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/5/TableCell/522` | 0.515039 | 11 |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/5/TableCell/542` | 0.423140 | 16 |

### Query 76
- Text: Summarize Huge
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/244']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/296', 'PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/268', 'PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/244']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/296` | 0.905764 | Huge |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/268` | 0.905764 | Huge |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/244` | 0.905764 | Huge |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/242` | 0.582018 | Large |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/260` | 0.582018 | Large |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/291` | 0.582018 | Large |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/3/Text/9` | 0.397022 | As shown in the Bulk Conversions table, Large or larger creatures are less encumbered by bulky items than Small or Medium creatures, while Tiny creatures become overburdened more quickly. A Large crea |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/9/TableCell/903` | 0.359354 | Bulk |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/2/TableCell/338` | 0.359354 | Bulk |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/11/TableCell/745` | 0.359354 | Bulk |

### Query 77
- Text: Summarize 24
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/245']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/245', 'PZO22001 Starfinder Player Core 232-249::/page/16/TableCell/139', 'PZO22001 Starfinder Player Core 232-249::/page/16/TableCell/199']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/245` | 0.779105 | 24 |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/16/TableCell/139` | 0.560118 | 25 |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/16/TableCell/199` | 0.560118 | 25 |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/247` | 0.444445 | 48 |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/14/TableCell/448` | 0.441044 | 28 |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/5/TableCell/550` | 0.400517 | 18 |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/16/TableCell/384` | 0.400517 | 18 |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/14/TableCell/441` | 0.400517 | 18 |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/14/TableCell/457` | 0.400516 | 18 |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/5/TableCell/558` | 0.381228 | 20 |

### Query 78
- Text: Summarize Gargantuan
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/246']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/246', 'PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/272', 'PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/301']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/246` | 0.899851 | Gargantuan |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/272` | 0.899851 | Gargantuan |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/301` | 0.899851 | Gargantuan |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/3/Table/12` | 0.430865 | Creature SizeBulk LimitTreats as LightTreats as NegligibleHuge×42 Bulk1 BulkGargantuan×84 Bulk2 Bulk |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/3/Table/1` | 0.379109 | Size Of CreatureBulkSmall3Medium6Large12Huge24Gargantuan48 |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/16/TableCell/390` | 0.313727 | Paragon |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/3/Table/16` | 0.307000 | Creature SizePriceBulkLight BecomesNegligible BecomesTinyStandardHalf*_-Small or Med.StandardStandardL-LargeStandard×21 BulkLHuge×4×42 Bulk1 BulkGargantuan×8×84 Bulk2 Bulk |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/3/Text/31` | 0.271641 | Introduction |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/3/SectionHeader/4` | 0.261668 | ITEMS AND SIZES |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/17/Text/7` | 0.260156 | **Introduction** |

### Query 79
- Text: What is the rule about In some situations, you might drag an object or creature rather than carry it. If you're dragging something, treat its Bulk as half. Typically, you can drag one thing at a time, you must use both hands to do so, and you drag slowly—roughly 50 feet per minute—unless you have some means to speed it up. Use the total Bulk of what you're dragging, so if you have a sack laden with goods, use the sum of all the Bulk in it instead of an individual item within.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/3/Text/3']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/3/Text/3', 'PZO22001 Starfinder Player Core 232-249::/page/2/Text/14', 'PZO22001 Starfinder Player Core 232-249::/page/2/Text/20']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/3/Text/3` | 0.980047 | In some situations, you might drag an object or creature rather than carry it. If you're dragging something, treat its Bulk as half. Typically, you can drag one thing at a time, you must use both hand |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/14` | 0.651686 | Carrying especially heavy or unwieldy items can make it  more difficult for you to move, as can overloading yourself  with too much gear. The Bulk value of an item reflects how  difficult the item is |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/20` | 0.650495 | As a general rule, an item that weighs 5 to 10 pounds is 1  Bulk, an item weighing less than a few ounces is negligible,  and anything in between is light. Particularly awkward or  unwieldy items migh |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/3/Text/9` | 0.590155 | As shown in the Bulk Conversions table, Large or larger creatures are less encumbered by bulky items than Small or Medium creatures, while Tiny creatures become overburdened more quickly. A Large crea |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/18` | 0.578943 | Items can have a number to indicate their Bulk value, or  they can be light (indicated by an L) or negligible (indicated  by a —) for the purpose of determining Bulk. For instance,  defiance series ar |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/3/Text/6` | 0.575469 | These rules for Bulk limits come up most often when a group tries to load up a mount or vehicle. The rules for items of different sizes tend to come into play when the characters defeat a big creature |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/16` | 0.547527 | You can carry an amount of Bulk equal to 5 plus your  Strength modifier without penalty; if you carry more, you  gain the encumbered condition. You can't hold or carry more  Bulk than 10 plus your Str |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/6/Text/7` | 0.546039 | This lists how many hands it takes to use the item effectively.  Most items that require two hands can be carried in only one  hand, but you must spend an Interact action to change your grip  in order |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/22` | 0.544923 | You might need to know the Bulk of a creature, especially if  you need to carry someone off the battlefield. The following  table lists the typical Bulk of a creature based on its size,  but the GM mi |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/13/Text/16` | 0.543378 | This entry gives the armor's Bulk, assuming you're wearing  the armor and distributing its weight across your body. A  suit of armor that's carried usually has 1 more Bulk than  what's listed here (or |

### Query 80
- Text: What is the rule about These rules for Bulk limits come up most often when a group tries to load up a mount or vehicle. The rules for items of different sizes tend to come into play when the characters defeat a big creature that has gear, since usually the only creatures of other sizes are creatures under the GM's control.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/3/Text/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/3/Text/6', 'PZO22001 Starfinder Player Core 232-249::/page/3/Text/5', 'PZO22001 Starfinder Player Core 232-249::/page/2/Text/22']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/3/Text/6` | 1.017593 | These rules for Bulk limits come up most often when a group tries to load up a mount or vehicle. The rules for items of different sizes tend to come into play when the characters defeat a big creature |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/3/Text/5` | 0.703747 | The Bulk rules in this chapter are for Small, Medium, and Large creatures, as most ancestries are these sizes; however, other uncommon or rare ancestries might be larger or smaller and require items s |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/22` | 0.670520 | You might need to know the Bulk of a creature, especially if  you need to carry someone off the battlefield. The following  table lists the typical Bulk of a creature based on its size,  but the GM mi |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/3/Text/9` | 0.611741 | As shown in the Bulk Conversions table, Large or larger creatures are less encumbered by bulky items than Small or Medium creatures, while Tiny creatures become overburdened more quickly. A Large crea |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/20` | 0.594744 | As a general rule, an item that weighs 5 to 10 pounds is 1  Bulk, an item weighing less than a few ounces is negligible,  and anything in between is light. Particularly awkward or  unwieldy items migh |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/3/Text/18` | 0.582865 | For example, a doshko sized for a Medium creature has a Price of 20 credits and 1 Bulk, so one made for a Huge creature is 80 credits and 4 Bulk. One made for a Tiny creature still costs 20 credits (d |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/14` | 0.581312 | Carrying especially heavy or unwieldy items can make it  more difficult for you to move, as can overloading yourself  with too much gear. The Bulk value of an item reflects how  difficult the item is |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/3/Text/14` | 0.568662 | Creatures of sizes other than Small, Medium, or Large need items appropriate to their size. These items have different Bulk and possibly a different Price. The Differently Sized Items table provides t |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/3/Text/7` | 0.562684 | In most cases, Small or Medium creatures can wield a Large weapon, though it's unwieldy, giving them the clumsy 1 condition, and the larger size is canceled by the difficulty of swinging the weapon, s |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/18` | 0.558786 | Items can have a number to indicate their Bulk value, or  they can be light (indicated by an L) or negligible (indicated  by a —) for the purpose of determining Bulk. For instance,  defiance series ar |

### Query 81
- Text: Lookup values for Creature
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/3/Table/11']
- Expected found: `True`
- Expected rank: `23`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/236', 'PZO22001 Starfinder Player Core 232-249::/page/2/TableCell/337', 'PZO22001 Starfinder Player Core 232-249::/page/2/SectionHeader/21']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/236` | 0.695212 | Size Of Creature |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/2/TableCell/337` | 0.695212 | Size Of Creature |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/2/SectionHeader/21` | 0.615345 | Bulk of Creatures |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/248` | 0.567646 | Creature Size |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/276` | 0.567646 | Creature Size |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/264` | 0.567646 | Creature Size |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/22` | 0.491978 | You might need to know the Bulk of a creature, especially if  you need to carry someone off the battlefield. The following  table lists the typical Bulk of a creature based on its size,  but the GM mi |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/3/Table/1` | 0.480040 | Size Of CreatureBulkSmall3Medium6Large12Huge24Gargantuan48 |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/2/Table/24` | 0.474948 | Size Of CreatureBulkTiny1 |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/3/Text/14` | 0.431099 | Creatures of sizes other than Small, Medium, or Large need items appropriate to their size. These items have different Bulk and possibly a different Price. The Differently Sized Items table provides t |

### Query 82
- Text: Lookup values for Creature
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/3/Table/12']
- Expected found: `True`
- Expected rank: `14`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/236', 'PZO22001 Starfinder Player Core 232-249::/page/2/TableCell/337', 'PZO22001 Starfinder Player Core 232-249::/page/2/SectionHeader/21']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/236` | 0.695212 | Size Of Creature |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/2/TableCell/337` | 0.695212 | Size Of Creature |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/2/SectionHeader/21` | 0.615345 | Bulk of Creatures |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/248` | 0.567646 | Creature Size |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/276` | 0.567646 | Creature Size |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/264` | 0.567646 | Creature Size |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/22` | 0.491978 | You might need to know the Bulk of a creature, especially if  you need to carry someone off the battlefield. The following  table lists the typical Bulk of a creature based on its size,  but the GM mi |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/3/Table/1` | 0.480040 | Size Of CreatureBulkSmall3Medium6Large12Huge24Gargantuan48 |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/2/Table/24` | 0.474948 | Size Of CreatureBulkTiny1 |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/3/Text/14` | 0.431099 | Creatures of sizes other than Small, Medium, or Large need items appropriate to their size. These items have different Bulk and possibly a different Price. The Differently Sized Items table provides t |

### Query 83
- Text: Lookup values for Creature
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/3/Table/16']
- Expected found: `True`
- Expected rank: `12`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/236', 'PZO22001 Starfinder Player Core 232-249::/page/2/TableCell/337', 'PZO22001 Starfinder Player Core 232-249::/page/2/SectionHeader/21']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/236` | 0.695212 | Size Of Creature |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/2/TableCell/337` | 0.695212 | Size Of Creature |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/2/SectionHeader/21` | 0.615345 | Bulk of Creatures |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/248` | 0.567646 | Creature Size |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/276` | 0.567646 | Creature Size |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/264` | 0.567646 | Creature Size |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/22` | 0.491978 | You might need to know the Bulk of a creature, especially if  you need to carry someone off the battlefield. The following  table lists the typical Bulk of a creature based on its size,  but the GM mi |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/3/Table/1` | 0.480040 | Size Of CreatureBulkSmall3Medium6Large12Huge24Gargantuan48 |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/2/Table/24` | 0.474948 | Size Of CreatureBulkTiny1 |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/3/Text/14` | 0.431099 | Creatures of sizes other than Small, Medium, or Large need items appropriate to their size. These items have different Bulk and possibly a different Price. The Differently Sized Items table provides t |

### Query 84
- Text: What is the rule about For example, a doshko sized for a Medium creature has a Price of 20 credits and 1 Bulk, so one made for a Huge creature is 80 credits and 4 Bulk. One made for a Tiny creature still costs 20 credits (due to its intricacy) and has 1/2 Bulk (rounding down to light Bulk). Because the way that a creature treats Bulk and the Bulk of gear sized for it scale the same way, Tiny or Large (or larger) creatures can usually wear and carry about the same amount of gear as a Medium creature.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/3/Text/18']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/3/Text/18', 'PZO22001 Starfinder Player Core 232-249::/page/3/Text/9', 'PZO22001 Starfinder Player Core 232-249::/page/3/Text/5']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/3/Text/18` | 0.985248 | For example, a doshko sized for a Medium creature has a Price of 20 credits and 1 Bulk, so one made for a Huge creature is 80 credits and 4 Bulk. One made for a Tiny creature still costs 20 credits (d |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/3/Text/9` | 0.733655 | As shown in the Bulk Conversions table, Large or larger creatures are less encumbered by bulky items than Small or Medium creatures, while Tiny creatures become overburdened more quickly. A Large crea |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/3/Text/5` | 0.723600 | The Bulk rules in this chapter are for Small, Medium, and Large creatures, as most ancestries are these sizes; however, other uncommon or rare ancestries might be larger or smaller and require items s |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/3/Text/6` | 0.647664 | These rules for Bulk limits come up most often when a group tries to load up a mount or vehicle. The rules for items of different sizes tend to come into play when the characters defeat a big creature |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/22` | 0.645728 | You might need to know the Bulk of a creature, especially if  you need to carry someone off the battlefield. The following  table lists the typical Bulk of a creature based on its size,  but the GM mi |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/3/Text/14` | 0.627081 | Creatures of sizes other than Small, Medium, or Large need items appropriate to their size. These items have different Bulk and possibly a different Price. The Differently Sized Items table provides t |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/20` | 0.607755 | As a general rule, an item that weighs 5 to 10 pounds is 1  Bulk, an item weighing less than a few ounces is negligible,  and anything in between is light. Particularly awkward or  unwieldy items migh |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/3/Text/7` | 0.592831 | In most cases, Small or Medium creatures can wield a Large weapon, though it's unwieldy, giving them the clumsy 1 condition, and the larger size is canceled by the difficulty of swinging the weapon, s |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/13/Text/16` | 0.590775 | This entry gives the armor's Bulk, assuming you're wearing  the armor and distributing its weight across your body. A  suit of armor that's carried usually has 1 more Bulk than  what's listed here (or |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/3/Text/19` | 0.578811 | Higher-level magic and tech items that cost significantly more than 8 times the cost of a mundane item use their listed Price regardless of size. Precious materials, however, have a Price based on the |

### Query 85
- Text: Lookup values for ChangeHandsActionDraw or put away a worn item, swap one item for another, or pick up an item11 or 2InteractPass an item to or take an item from a willing creature21 or 2InteractDrop an item to the ground1 or 2ReleaseDetach a shield or item strapped to you1Interact
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/3/Table/23']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/3/Table/23', 'PZO22001 Starfinder Player Core 232-249::/page/4/Table/1', 'PZO22001 Starfinder Player Core 232-249::/page/2/Text/10']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/3/Table/23` | 1.003897 | ChangeHandsActionDraw or put away a worn item, swap one item for another, or pick up an item11 or 2InteractPass an item to or take an item from a willing creature21 or 2InteractDrop an item to the gro |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/4/Table/1` | 0.809225 | ChangeHandsActionChange your grip by removing a hand from an item2ReleaseChange your grip by adding a hand to an item2InteractRetrieve an item from a backpack3, sack, or similar container2Interact |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/10` | 0.759761 | Drawing a worn item or changing how you're carrying an  item usually requires you to use an Interact action (though to  drop an item, you use the Release action instead). Changing |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/309` | 0.717541 | Draw or put away a worn item, swap one item for another, or pick up an item1 |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/6/Text/7` | 0.577472 | This lists how many hands it takes to use the item effectively.  Most items that require two hands can be carried in only one  hand, but you must spend an Interact action to change your grip  in order |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/312` | 0.574637 | Pass an item to or take an item from a willing creature2 |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/12` | 0.568163 | Many ways of using items require you to spend multiple  actions. For example, drinking a serum worn at your belt  requires using an Interact action to draw it and then using  a second action to drink |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/11` | 0.566047 | Equipment on page 235 lists some ways that you might  change the items you're holding or carrying, and the number  of hands you need to do so. |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/6/Text/9` | 0.532769 | You can make a set of tools (such as a maker's toolkit or medkit)  easier to use by wearing it. This allows you to draw and replace  the tools as part of the action that uses them. You can wear up  to |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/4/TableCell/189` | 0.526980 | Change your grip by removing a hand from an item |

### Query 86
- Text: What is the rule about Action?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/308']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/4/TableCell/188', 'PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/308', 'PZO22001 Starfinder Player Core 232-249::/page/2/Text/12']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/4/TableCell/188` | 0.694714 | Action |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/308` | 0.694714 | Action |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/12` | 0.550792 | Many ways of using items require you to spend multiple  actions. For example, drinking a serum worn at your belt  requires using an Interact action to draw it and then using  a second action to drink |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/10` | 0.433918 | Drawing a worn item or changing how you're carrying an  item usually requires you to use an Interact action (though to  drop an item, you use the Release action instead). Changing |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/10/Text/44` | 0.419878 | **Activate **[one-action] (manipulate) |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/9/Text/13` | 0.419878 | **Activate **[one-action] (manipulate) |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/11/SectionHeader/1` | 0.419878 | **Activate **[one-action] (manipulate) |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/10/Text/37` | 0.419878 | **Activate **[one-action] (manipulate) |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/10/Text/16` | 0.419878 | **Activate **[one-action] (manipulate) |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/3/Table/23` | 0.401755 | ChangeHandsActionDraw or put away a worn item, swap one item for another, or pick up an item11 or 2InteractPass an item to or take an item from a willing creature21 or 2InteractDrop an item to the gro |

### Query 87
- Text: What is the rule about Interact?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/311']
- Expected found: `True`
- Expected rank: `4`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/4/TableCell/194', 'PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/320', 'PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/314']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/320` | 0.785436 | Interact |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/4/TableCell/194` | 0.785436 | Interact |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/314` | 0.785436 | Interact |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/311` | 0.743436 | Interact |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/4/TableCell/197` | 0.743436 | Interact |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/10` | 0.519357 | Drawing a worn item or changing how you're carrying an  item usually requires you to use an Interact action (though to  drop an item, you use the Release action instead). Changing |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/12` | 0.514350 | Many ways of using items require you to spend multiple  actions. For example, drinking a serum worn at your belt  requires using an Interact action to draw it and then using  a second action to drink |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/10/Text/32` | 0.438788 | These are pharmaceutical serums; they're technological, or  hybrid in some cases, but can be crafted using a laboratory and  don't incorporate significant magic. You can activate a serum  with an Inte |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/6/Text/7` | 0.415564 | This lists how many hands it takes to use the item effectively.  Most items that require two hands can be carried in only one  hand, but you must spend an Interact action to change your grip  in order |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/4/ListItem/4` | 0.412919 | 3 Retrieving an item stowed in your own backpack requires first taking off the backpack with a separate Interact action. |

### Query 88
- Text: What is the rule about Interact?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/314']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/4/TableCell/194', 'PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/320', 'PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/314']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/320` | 0.785436 | Interact |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/4/TableCell/194` | 0.785436 | Interact |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/314` | 0.785436 | Interact |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/311` | 0.743436 | Interact |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/4/TableCell/197` | 0.743436 | Interact |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/10` | 0.519357 | Drawing a worn item or changing how you're carrying an  item usually requires you to use an Interact action (though to  drop an item, you use the Release action instead). Changing |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/12` | 0.514350 | Many ways of using items require you to spend multiple  actions. For example, drinking a serum worn at your belt  requires using an Interact action to draw it and then using  a second action to drink |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/10/Text/32` | 0.438788 | These are pharmaceutical serums; they're technological, or  hybrid in some cases, but can be crafted using a laboratory and  don't incorporate significant magic. You can activate a serum  with an Inte |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/6/Text/7` | 0.415564 | This lists how many hands it takes to use the item effectively.  Most items that require two hands can be carried in only one  hand, but you must spend an Interact action to change your grip  in order |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/4/ListItem/4` | 0.412919 | 3 Retrieving an item stowed in your own backpack requires first taking off the backpack with a separate Interact action. |

### Query 89
- Text: What is the rule about Detach a shield or item strapped to you?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/318']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/318', 'PZO22001 Starfinder Player Core 232-249::/page/3/Table/23', 'PZO22001 Starfinder Player Core 232-249::/page/4/Text/16']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/318` | 0.942830 | Detach a shield or item strapped to you |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/3/Table/23` | 0.561440 | ChangeHandsActionDraw or put away a worn item, swap one item for another, or pick up an item11 or 2InteractPass an item to or take an item from a willing creature21 or 2InteractDrop an item to the gro |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/4/Text/16` | 0.516715 | An item can be broken or destroyed if it takes enough damage. Every item has a **Hardness** value. Each time an item takes damage, reduce any damage the item takes by its Hardness. The rest of the dam |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/3/Text/34` | 0.466225 | Shields |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/315` | 0.457832 | Drop an item to the ground |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/9/Text/26` | 0.442627 | **Shields** **Weapons** |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/10` | 0.418606 | Drawing a worn item or changing how you're carrying an  item usually requires you to use an Interact action (though to  drop an item, you use the Release action instead). Changing |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/5/Text/3` | 0.416423 | A broken item still imposes penalties and limitations  normally incurred by carrying, holding, or wearing it. For  example, broken armor would still impose its Dexterity  modifier cap, check penalty, |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/13/Text/8` | 0.415617 | This number is the maximum amount of your Dexterity  modifier that can apply to your AC while you are wearing  a given suit of armor. For example, if you have a Dexterity  modifier of +4 and you are w |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/309` | 0.413954 | Draw or put away a worn item, swap one item for another, or pick up an item1 |

### Query 90
- Text: What is the rule about Interact?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/320']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/4/TableCell/194', 'PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/320', 'PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/314']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/320` | 0.785436 | Interact |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/4/TableCell/194` | 0.785436 | Interact |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/314` | 0.785436 | Interact |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/311` | 0.743436 | Interact |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/4/TableCell/197` | 0.743436 | Interact |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/10` | 0.519357 | Drawing a worn item or changing how you're carrying an  item usually requires you to use an Interact action (though to  drop an item, you use the Release action instead). Changing |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/12` | 0.514350 | Many ways of using items require you to spend multiple  actions. For example, drinking a serum worn at your belt  requires using an Interact action to draw it and then using  a second action to drink |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/10/Text/32` | 0.438788 | These are pharmaceutical serums; they're technological, or  hybrid in some cases, but can be crafted using a laboratory and  don't incorporate significant magic. You can activate a serum  with an Inte |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/6/Text/7` | 0.415564 | This lists how many hands it takes to use the item effectively.  Most items that require two hands can be carried in only one  hand, but you must spend an Interact action to change your grip  in order |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/4/ListItem/4` | 0.412919 | 3 Retrieving an item stowed in your own backpack requires first taking off the backpack with a separate Interact action. |

### Query 91
- Text: What is the rule about ANCESTRIES &?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/3/Text/26']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/3/Text/26', 'PZO22001 Starfinder Player Core 232-249::/page/13/Text/35', 'PZO22001 Starfinder Player Core 232-249::/page/1/Text/24']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/3/Text/26` | 0.728250 | ANCESTRIES & BACKGROUNDS |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/13/Text/35` | 0.727003 | **ANCESTRIES & ** **BACKGROUNDS** |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/24` | 0.727003 | **ANCESTRIES & ** **BACKGROUNDS** |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/5/Text/23` | 0.697003 | **ANCESTRIES & ** **BACKGROUNDS** |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/15/Text/12` | 0.697003 | **ANCESTRIES & ** **BACKGROUNDS** |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/11/Text/44` | 0.697003 | **ANCESTRIES & ** **BACKGROUNDS** |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/7/Text/15` | 0.697003 | **ANCESTRIES & ** **BACKGROUNDS** |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/9/Text/19` | 0.697003 | **ANCESTRIES & ** **BACKGROUNDS** |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/17/Text/3` | 0.697003 | **ANCESTRIES & ** **BACKGROUNDS** |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/3/Text/5` | 0.396210 | The Bulk rules in this chapter are for Small, Medium, and Large creatures, as most ancestries are these sizes; however, other uncommon or rare ancestries might be larger or smaller and require items s |

### Query 92
- Text: What is the rule about SKILLS?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/3/Text/28']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/3/Text/28', 'PZO22001 Starfinder Player Core 232-249::/page/1/Text/26', 'PZO22001 Starfinder Player Core 232-249::/page/15/Text/14']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/3/Text/28` | 0.790208 | SKILLS |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/15/Text/14` | 0.692425 | **SKILLS** |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/26` | 0.692425 | **SKILLS** |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/13/Text/37` | 0.650425 | **SKILLS** |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/9/Text/20` | 0.574916 | **CLASSES** **SKILLS** |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/5/Text/25` | 0.517296 | **SKILLS** **FEATS** |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/7/Text/17` | 0.517296 | **SKILLS** **FEATS** |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/11/Text/46` | 0.517296 | **SKILLS** **FEATS** |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/17/Text/5` | 0.517296 | **SKILLS** **FEATS** |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/13/Text/10` | 0.398382 | While wearing your armor, you take this penalty to  Strength- and Dexterity-based skill checks, except for  those that have the attack trait. If you meet the armor's  Strength threshold (see Strength |

### Query 93
- Text: What is the rule about FEATS <u>Equipme</u>nt?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/3/Text/29']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/3/Text/29', 'PZO22001 Starfinder Player Core 232-249::/page/9/Text/21', 'PZO22001 Starfinder Player Core 232-249::/page/13/Text/38']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/3/Text/29` | 0.844179 | FEATS <u>Equipme</u>nt |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/9/Text/21` | 0.713736 | **FEATS** **EQUIPMENT** |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/13/Text/38` | 0.603207 | **FEATS** |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/27` | 0.561207 | **FEATS** |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/15/Text/15` | 0.561207 | **FEATS** |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/11/Text/46` | 0.481600 | **SKILLS** **FEATS** |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/7/Text/17` | 0.481600 | **SKILLS** **FEATS** |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/17/Text/5` | 0.481600 | **SKILLS** **FEATS** |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/5/Text/25` | 0.481600 | **SKILLS** **FEATS** |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/1/SectionHeader/1` | 0.429535 | CHAPTER 6: EQUIPMENT |

### Query 94
- Text: What is the rule about SPELLS?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/3/Text/41']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/3/Text/41', 'PZO22001 Starfinder Player Core 232-249::/page/17/Text/19', 'PZO22001 Starfinder Player Core 232-249::/page/9/Text/33']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/3/Text/41` | 0.844517 | SPELLS |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/17/Text/19` | 0.796446 | **SPELLS** |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/9/Text/33` | 0.796446 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/42` | 0.754446 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/11/Text/59` | 0.754446 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/5/Text/38` | 0.754446 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/7/Text/31` | 0.754446 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/13/Text/51` | 0.754446 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/11/SectionHeader/37` | 0.452038 | SPELLCASTING |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/11/SectionHeader/39` | 0.388976 | **SPELLCASTING SERVICES** |

### Query 95
- Text: What is the rule about CHARACTER Sheet?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/3/Text/45']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/3/Text/45', 'PZO22001 Starfinder Player Core 232-249::/page/15/Text/30', 'PZO22001 Starfinder Player Core 232-249::/page/7/Text/35']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/3/Text/45` | 0.845173 | CHARACTER Sheet |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/15/Text/30` | 0.525346 | **CHARACTER ** |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/7/Text/35` | 0.525346 | **CHARACTER ** |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/7` | 0.429171 | Each item has an item level, which represents the item's  complexity and any magic or technology used in its  construction. Simpler items with a lower level are easier to  construct, and you can't Cra |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/9` | 0.404013 | A character carries items in three ways: held, worn, and  stowed. Held items are in your hands; a character typically  has two hands, allowing them to hold an item in each hand  or a single two-handed |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/6/Text/11` | 0.386512 | These items follow special rules or require more detail. |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/6/Text/5` | 0.364313 | The tables starting on page 240 list the Price and Bulk entries  for a wide variety of gear you can use to kit out your character.  Any item with a number after it in parentheses indicates that  the i |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/5` | 0.354375 | Characters can use UPBs in place of credits for crafting  items using maker's kits; in fact, they're necessary for the use  of certain tools. |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/4/Text/12` | 0.353633 | A character who is trained or better in Crafting can improve an item using the original item and UPBs (page 234) as raw |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/3/Text/6` | 0.349604 | These rules for Bulk limits come up most often when a group tries to load up a mount or vehicle. The rules for items of different sizes tend to come into play when the characters defeat a big creature |

### Query 96
- Text: Lookup values for ChangeHandsActionChange your grip by removing a hand from an item2ReleaseChange your grip by adding a hand to an item2InteractRetrieve an item from a backpack3, sack, or similar container2Interact
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/4/Table/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/4/Table/1', 'PZO22001 Starfinder Player Core 232-249::/page/3/Table/23', 'PZO22001 Starfinder Player Core 232-249::/page/4/TableCell/189']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/4/Table/1` | 0.994371 | ChangeHandsActionChange your grip by removing a hand from an item2ReleaseChange your grip by adding a hand to an item2InteractRetrieve an item from a backpack3, sack, or similar container2Interact |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/3/Table/23` | 0.810135 | ChangeHandsActionDraw or put away a worn item, swap one item for another, or pick up an item11 or 2InteractPass an item to or take an item from a willing creature21 or 2InteractDrop an item to the gro |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/4/TableCell/189` | 0.729589 | Change your grip by removing a hand from an item |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/4/TableCell/192` | 0.668850 | Change your grip by adding a hand to an item |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/10` | 0.642999 | Drawing a worn item or changing how you're carrying an  item usually requires you to use an Interact action (though to  drop an item, you use the Release action instead). Changing |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/6/Text/7` | 0.628981 | This lists how many hands it takes to use the item effectively.  Most items that require two hands can be carried in only one  hand, but you must spend an Interact action to change your grip  in order |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/11` | 0.602716 | Equipment on page 235 lists some ways that you might  change the items you're holding or carrying, and the number  of hands you need to do so. |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/4/ListItem/2` | 0.582725 | 1 If you retrieve a two-handed item with only one hand, you still need to change your grip before you can wield or use it |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/4/ListItem/4` | 0.561485 | 3 Retrieving an item stowed in your own backpack requires first taking off the backpack with a separate Interact action. |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/309` | 0.556182 | Draw or put away a worn item, swap one item for another, or pick up an item1 |

### Query 97
- Text: What is the rule about Action?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/4/TableCell/188']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/4/TableCell/188', 'PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/308', 'PZO22001 Starfinder Player Core 232-249::/page/2/Text/12']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/4/TableCell/188` | 0.694714 | Action |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/308` | 0.694714 | Action |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/12` | 0.550792 | Many ways of using items require you to spend multiple  actions. For example, drinking a serum worn at your belt  requires using an Interact action to draw it and then using  a second action to drink |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/10` | 0.433918 | Drawing a worn item or changing how you're carrying an  item usually requires you to use an Interact action (though to  drop an item, you use the Release action instead). Changing |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/10/Text/44` | 0.419878 | **Activate **[one-action] (manipulate) |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/9/Text/13` | 0.419878 | **Activate **[one-action] (manipulate) |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/11/SectionHeader/1` | 0.419878 | **Activate **[one-action] (manipulate) |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/10/Text/37` | 0.419878 | **Activate **[one-action] (manipulate) |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/10/Text/16` | 0.419878 | **Activate **[one-action] (manipulate) |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/3/Table/23` | 0.401755 | ChangeHandsActionDraw or put away a worn item, swap one item for another, or pick up an item11 or 2InteractPass an item to or take an item from a willing creature21 or 2InteractDrop an item to the gro |

### Query 98
- Text: What is the rule about Interact?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/4/TableCell/194']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/4/TableCell/194', 'PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/320', 'PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/314']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/320` | 0.785436 | Interact |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/4/TableCell/194` | 0.785436 | Interact |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/314` | 0.785436 | Interact |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/311` | 0.743436 | Interact |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/4/TableCell/197` | 0.743436 | Interact |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/10` | 0.519357 | Drawing a worn item or changing how you're carrying an  item usually requires you to use an Interact action (though to  drop an item, you use the Release action instead). Changing |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/12` | 0.514350 | Many ways of using items require you to spend multiple  actions. For example, drinking a serum worn at your belt  requires using an Interact action to draw it and then using  a second action to drink |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/10/Text/32` | 0.438788 | These are pharmaceutical serums; they're technological, or  hybrid in some cases, but can be crafted using a laboratory and  don't incorporate significant magic. You can activate a serum  with an Inte |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/6/Text/7` | 0.415564 | This lists how many hands it takes to use the item effectively.  Most items that require two hands can be carried in only one  hand, but you must spend an Interact action to change your grip  in order |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/4/ListItem/4` | 0.412919 | 3 Retrieving an item stowed in your own backpack requires first taking off the backpack with a separate Interact action. |

### Query 99
- Text: What is the rule about Retrieve an item from a backpack3, sack, or similar container?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/4/TableCell/195']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/4/TableCell/195', 'PZO22001 Starfinder Player Core 232-249::/page/4/ListItem/4', 'PZO22001 Starfinder Player Core 232-249::/page/4/Table/1']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/4/TableCell/195` | 0.926030 | Retrieve an item from a backpack3, sack, or similar container |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/4/ListItem/4` | 0.654407 | 3 Retrieving an item stowed in your own backpack requires first taking off the backpack with a separate Interact action. |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/4/Table/1` | 0.560195 | ChangeHandsActionChange your grip by removing a hand from an item2ReleaseChange your grip by adding a hand to an item2InteractRetrieve an item from a backpack3, sack, or similar container2Interact |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/6/Text/22` | 0.447683 | **Containers:** Containers include backpacks, briefcases, duffel  bags, and handbags. A container holds up to 4 Bulk and the  first 2 Bulk of those items don't count against your Bulk limits.  If you' |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/309` | 0.435397 | Draw or put away a worn item, swap one item for another, or pick up an item1 |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/9` | 0.429201 | A character carries items in three ways: held, worn, and  stowed. Held items are in your hands; a character typically  has two hands, allowing them to hold an item in each hand  or a single two-handed |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/312` | 0.419555 | Pass an item to or take an item from a willing creature2 |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/3/Text/6` | 0.417533 | These rules for Bulk limits come up most often when a group tries to load up a mount or vehicle. The rules for items of different sizes tend to come into play when the characters defeat a big creature |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/7` | 0.403568 | Once you've purchased your starting items, there are three  main ways to gain new items and equipment: you can find  them during an adventure, make them using the Crafting  skill, or purchase them fro |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/6/Text/11` | 0.400749 | These items follow special rules or require more detail. |

### Query 100
- Text: What is the rule about Interact?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/4/TableCell/197']
- Expected found: `True`
- Expected rank: `5`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/4/TableCell/194', 'PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/320', 'PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/314']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/320` | 0.785436 | Interact |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/4/TableCell/194` | 0.785436 | Interact |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/314` | 0.785436 | Interact |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/311` | 0.743436 | Interact |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/4/TableCell/197` | 0.743436 | Interact |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/10` | 0.519357 | Drawing a worn item or changing how you're carrying an  item usually requires you to use an Interact action (though to  drop an item, you use the Release action instead). Changing |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/12` | 0.514350 | Many ways of using items require you to spend multiple  actions. For example, drinking a serum worn at your belt  requires using an Interact action to draw it and then using  a second action to drink |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/10/Text/32` | 0.438788 | These are pharmaceutical serums; they're technological, or  hybrid in some cases, but can be crafted using a laboratory and  don't incorporate significant magic. You can activate a serum  with an Inte |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/6/Text/7` | 0.415564 | This lists how many hands it takes to use the item effectively.  Most items that require two hands can be carried in only one  hand, but you must spend an Interact action to change your grip  in order |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/4/ListItem/4` | 0.412919 | 3 Retrieving an item stowed in your own backpack requires first taking off the backpack with a separate Interact action. |

### Query 101
- Text: What is the rule about 2 A creature must have a hand free for someone to pass an item to them, and they might then need to change their grip if they receive an item requiring two hands to wield or use.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/4/ListItem/3']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/4/ListItem/3', 'PZO22001 Starfinder Player Core 232-249::/page/4/ListItem/2', 'PZO22001 Starfinder Player Core 232-249::/page/6/Text/7']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/4/ListItem/3` | 0.970733 | 2 A creature must have a hand free for someone to pass an item to them, and they might then need to change their grip if they receive an item requiring two hands to wield or use. |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/4/ListItem/2` | 0.753573 | 1 If you retrieve a two-handed item with only one hand, you still need to change your grip before you can wield or use it |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/6/Text/7` | 0.678868 | This lists how many hands it takes to use the item effectively.  Most items that require two hands can be carried in only one  hand, but you must spend an Interact action to change your grip  in order |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/312` | 0.609504 | Pass an item to or take an item from a willing creature2 |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/3/Text/21` | 0.569946 | Some abilities require you to wield an item, typically a weapon. You're wielding an item any time you're holding it in the number of hands needed to use it effectively. When wielding an item, you're n |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/4/Table/1` | 0.539528 | ChangeHandsActionChange your grip by removing a hand from an item2ReleaseChange your grip by adding a hand to an item2InteractRetrieve an item from a backpack3, sack, or similar container2Interact |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/3/Table/23` | 0.533970 | ChangeHandsActionDraw or put away a worn item, swap one item for another, or pick up an item11 or 2InteractPass an item to or take an item from a willing creature21 or 2InteractDrop an item to the gro |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/4/TableCell/192` | 0.520705 | Change your grip by adding a hand to an item |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/4/TableCell/189` | 0.519529 | Change your grip by removing a hand from an item |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/11` | 0.511952 | Equipment on page 235 lists some ways that you might  change the items you're holding or carrying, and the number  of hands you need to do so. |

### Query 102
- Text: What is the rule about 3 Retrieving an item stowed in your own backpack requires first taking off the backpack with a separate Interact action.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/4/ListItem/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/4/ListItem/4', 'PZO22001 Starfinder Player Core 232-249::/page/4/TableCell/195', 'PZO22001 Starfinder Player Core 232-249::/page/4/Table/1']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/4/ListItem/4` | 0.957493 | 3 Retrieving an item stowed in your own backpack requires first taking off the backpack with a separate Interact action. |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/4/TableCell/195` | 0.668302 | Retrieve an item from a backpack3, sack, or similar container |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/4/Table/1` | 0.617046 | ChangeHandsActionChange your grip by removing a hand from an item2ReleaseChange your grip by adding a hand to an item2InteractRetrieve an item from a backpack3, sack, or similar container2Interact |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/12` | 0.565807 | Many ways of using items require you to spend multiple  actions. For example, drinking a serum worn at your belt  requires using an Interact action to draw it and then using  a second action to drink |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/10` | 0.559811 | Drawing a worn item or changing how you're carrying an  item usually requires you to use an Interact action (though to  drop an item, you use the Release action instead). Changing |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/3/Table/23` | 0.518646 | ChangeHandsActionDraw or put away a worn item, swap one item for another, or pick up an item11 or 2InteractPass an item to or take an item from a willing creature21 or 2InteractDrop an item to the gro |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/6/Text/7` | 0.478034 | This lists how many hands it takes to use the item effectively.  Most items that require two hands can be carried in only one  hand, but you must spend an Interact action to change your grip  in order |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/9` | 0.477473 | A character carries items in three ways: held, worn, and  stowed. Held items are in your hands; a character typically  has two hands, allowing them to hold an item in each hand  or a single two-handed |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/309` | 0.451431 | Draw or put away a worn item, swap one item for another, or pick up an item1 |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/6/Text/9` | 0.435786 | You can make a set of tools (such as a maker's toolkit or medkit)  easier to use by wearing it. This allows you to draw and replace  the tools as part of the action that uses them. You can wear up  to |

### Query 103
- Text: What is the rule about Most types of armor, shields, and weapons in Starfinder come in a variety of grades. Each grade represents an improved version of that piece of equipment and should be sought after once your character reaches the appropriate level. While higher-level versions of equipment are available on the open market, many adventurers prefer going through the effort of upgrading their existing gear rather than buying new.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/4/Text/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/4/Text/6', 'PZO22001 Starfinder Player Core 232-249::/page/4/Text/8', 'PZO22001 Starfinder Player Core 232-249::/page/4/Text/10']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/4/Text/6` | 0.999200 | Most types of armor, shields, and weapons in Starfinder come in a variety of grades. Each grade represents an improved version of that piece of equipment and should be sought after once your character |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/4/Text/8` | 0.746585 | Equipment typically comes in seven grades: commercial, tactical, advanced, superior, elite, ultimate, and paragon. While most armor, shields, and weapons can exist in any grade from commercial to para |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/4/Text/10` | 0.658304 | Armor, shields and weapons gain more upgrade slots as they improve. Higher grades of armor add more AC and gains the resilient trait, improving the saving throws of their wielder by the listed value. |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/4/Text/9` | 0.618540 | Armor, shields, and weapons (pages 244, 250, and 253 respectively) are typically listed using their lowest available grade, usually commercial. Each grade beyond the first provides the equipment with |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/2` | 0.595123 | To make your mark on the galaxy, you'll need to have the right equipment, including armor, weapons,  augmentation, and other gear. This chapter presents the various equipment that you can purchase  du |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/7` | 0.560391 | Each item has an item level, which represents the item's  complexity and any magic or technology used in its  construction. Simpler items with a lower level are easier to  construct, and you can't Cra |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/4/Text/18` | 0.547372 | An item's Hardness, Hit Points, and Broken Threshold usually depend on the material the item is made of. Information on materials appears in *Starfinder GM Core*. |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/6/Text/2` | 0.542845 | Tech gear represents a variety of different consumer and specialized equipment used throughout the  galaxy. Depending on the situation, your character will need all sorts of items both while exploring |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/7` | 0.541860 | Once you've purchased your starting items, there are three  main ways to gain new items and equipment: you can find  them during an adventure, make them using the Crafting  skill, or purchase them fro |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/6` | 0.532043 | Your character starts out with 150 credits to spend on any  common items from this chapter. Credits are a galactic  currency used to barter and trade for goods in the Starfinder  setting. Items with a |

### Query 104
- Text: What is the rule about Equipment typically comes in seven grades: commercial, tactical, advanced, superior, elite, ultimate, and paragon. While most armor, shields, and weapons can exist in any grade from commercial to paragon, some equipment doesn't exist at certain grades and must be initially purchased or crafted at a higher grade. Equipment other than armor, weapons, and shields only exist at grades specifically listed in the item and cannot be improved to a higher grade if it's not listed.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/4/Text/8']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/4/Text/8', 'PZO22001 Starfinder Player Core 232-249::/page/4/Text/9', 'PZO22001 Starfinder Player Core 232-249::/page/4/Text/6']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/4/Text/8` | 0.999069 | Equipment typically comes in seven grades: commercial, tactical, advanced, superior, elite, ultimate, and paragon. While most armor, shields, and weapons can exist in any grade from commercial to para |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/4/Text/9` | 0.777145 | Armor, shields, and weapons (pages 244, 250, and 253 respectively) are typically listed using their lowest available grade, usually commercial. Each grade beyond the first provides the equipment with |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/4/Text/6` | 0.713517 | Most types of armor, shields, and weapons in Starfinder come in a variety of grades. Each grade represents an improved version of that piece of equipment and should be sought after once your character |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/4/SectionHeader/7` | 0.581119 | **GRADES OF EQUIPMENT ** |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/4/Text/10` | 0.557550 | Armor, shields and weapons gain more upgrade slots as they improve. Higher grades of armor add more AC and gains the resilient trait, improving the saving throws of their wielder by the listed value. |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/7` | 0.552172 | Each item has an item level, which represents the item's  complexity and any magic or technology used in its  construction. Simpler items with a lower level are easier to  construct, and you can't Cra |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/2` | 0.533819 | To make your mark on the galaxy, you'll need to have the right equipment, including armor, weapons,  augmentation, and other gear. This chapter presents the various equipment that you can purchase  du |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/4/Text/14` | 0.531108 | If you have the formula for the item you can improve an item by supplying UPB equal to half the difference between the two items, but you must work multiple days to reduce the materials needed to comp |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/13/Text/20` | 0.529380 | Each type of clothing and armor belongs to an armor  group, which classifies it with other armor of similar a  type, material, and construction. Some abilities reference  armor groups, typically to gr |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/5/Text/13` | 0.505419 | While you may attempt to improve an item directly  from commercial to paragon in 1 day, doing so makes  the DC of the Crafting attempt significantly higher and  thus results in a higher likelihood of |

### Query 105
- Text: What is the rule about Armor, shields, and weapons (pages 244, 250, and 253 respectively) are typically listed using their lowest available grade, usually commercial. Each grade beyond the first provides the equipment with additional statistics as given in the tables listed for the appropriate item. Equipment listed with multiple grades in their entry do not use these charts and instead use the statistics listed for each grade in their description.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/4/Text/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/4/Text/9', 'PZO22001 Starfinder Player Core 232-249::/page/4/Text/8', 'PZO22001 Starfinder Player Core 232-249::/page/13/Text/2']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/4/Text/9` | 1.007781 | Armor, shields, and weapons (pages 244, 250, and 253 respectively) are typically listed using their lowest available grade, usually commercial. Each grade beyond the first provides the equipment with |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/4/Text/8` | 0.730275 | Equipment typically comes in seven grades: commercial, tactical, advanced, superior, elite, ultimate, and paragon. While most armor, shields, and weapons can exist in any grade from commercial to para |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/13/Text/2` | 0.623428 | The Armor table (page 248) provides the statistics for  the various forms of protection without wearing armor  and for suits of armor that can be purchased and worn,  organized by category. The column |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/4/Text/6` | 0.553594 | Most types of armor, shields, and weapons in Starfinder come in a variety of grades. Each grade represents an improved version of that piece of equipment and should be sought after once your character |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/4/Text/10` | 0.545891 | Armor, shields and weapons gain more upgrade slots as they improve. Higher grades of armor add more AC and gains the resilient trait, improving the saving throws of their wielder by the listed value. |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/2/Text/7` | 0.538456 | Each item has an item level, which represents the item's  complexity and any magic or technology used in its  construction. Simpler items with a lower level are easier to  construct, and you can't Cra |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/6/Text/5` | 0.523987 | The tables starting on page 240 list the Price and Bulk entries  for a wide variety of gear you can use to kit out your character.  Any item with a number after it in parentheses indicates that  the i |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/13/Text/20` | 0.520499 | Each type of clothing and armor belongs to an armor  group, which classifies it with other armor of similar a  type, material, and construction. Some abilities reference  armor groups, typically to gr |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/14/Text/2` | 0.497625 | Your armor's statistics are based on the materials  they're composed of and the means of construction their armor group. It's not likely your armor will take  damage, as explained in Item Damage on pa |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/13/Text/4` | 0.484291 | The armor's category—unarmored, light armor, medium  armor, or heavy armor—indicates which proficiency bonus  you use while wearing the armor. |

### Query 106
- Text: What is the rule about Armor, shields and weapons gain more upgrade slots as they improve. Higher grades of armor add more AC and gains the resilient trait, improving the saving throws of their wielder by the listed value. Higher grades of weapons have improved damage dice and gain the tracking trait, improving their attack rolls by the listed value. Higher grades of shields have increased Hardness, Hit Points, and BT.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/4/Text/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/4/Text/10', 'PZO22001 Starfinder Player Core 232-249::/page/4/Text/6', 'PZO22001 Starfinder Player Core 232-249::/page/4/Text/9']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/4/Text/10` | 0.966961 | Armor, shields and weapons gain more upgrade slots as they improve. Higher grades of armor add more AC and gains the resilient trait, improving the saving throws of their wielder by the listed value. |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/4/Text/6` | 0.641856 | Most types of armor, shields, and weapons in Starfinder come in a variety of grades. Each grade represents an improved version of that piece of equipment and should be sought after once your character |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/4/Text/9` | 0.623180 | Armor, shields, and weapons (pages 244, 250, and 253 respectively) are typically listed using their lowest available grade, usually commercial. Each grade beyond the first provides the equipment with |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/4/Text/8` | 0.584998 | Equipment typically comes in seven grades: commercial, tactical, advanced, superior, elite, ultimate, and paragon. While most armor, shields, and weapons can exist in any grade from commercial to para |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/13/Text/31` | 0.562928 | **Resilient:** This armor has been developed with several  integrated recalibration and defensive systems. While  wearing this armor, you gain an item bonus to saving  throws equal to the listed value |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/13/Text/18` | 0.551325 | Armor can be customized with upgrades, which include  technological armor modifications and magic armor  fusions. This indicates how many upgrades the armor can  Install. |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/12/Text/2` | 0.542591 | Armor increases your character's defenses, but some medium or heavy armor can hamper movement.  If you want to increase your character's defense beyond the protection their armor provides, they  can u |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/12/Text/5` | 0.536781 | Your **Armor** **Class** (**AC**) measures how well you can defend  against attacks. When a creature attacks you, your Armor  Class is the DC for that attack roll. |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/16/Table/8` | 0.535500 | Armor (Commercial)Item LevelPriceAC BonusCheck PenaltySpeed PenaltyStrengthBulkUpgradesGroupArmor TraitsAegis Series0300+60-3-10+330PlateBulwark, techDefiance Series0200+51-3-10+331PlateTechHidden Sol |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/14/Text/5` | 0.532786 | Certain class features can grant you additional benefits with  certain armors. This is called an armor specialization effect.  The exact effect depends on which armor group your armor  belongs to, as |

### Query 107
- Text: Lookup values for LevelPriceLevelPrice0*5 credits11700 credits110 credits121,000 credits220 credits131,500 credits330 credits142,250 credits450 credits153,250 credits580 credits165,000 credits6130 credits177,500 credits7180 credits1812,000 credits8250 credits1920,000 credits9350 credits2035,000 credits10500 credits
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/5/Table/19']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/5/Table/19', 'PZO22001 Starfinder Player Core 232-249::/page/16/Table/10', 'PZO22001 Starfinder Player Core 232-249::/page/11/Table/40']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/5/Table/19` | 1.003427 | LevelPriceLevelPrice0*5 credits11700 credits110 credits121,000 credits220 credits131,500 credits330 credits142,250 credits450 credits153,250 credits580 credits165,000 credits6130 credits177,500 credit |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/16/Table/10` | 0.744297 | GradeLevelImprovement PriceTotal PriceUpgradesAC Bonus IncreaseTraitsCommercial0---+0_Tactical5+1,600 credits1,600 credits+1+1_Advanced8+3,400 credits5,000 credits+1+1Resilient +1Superior11+9,000 cred |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/11/Table/40` | 0.669772 | Spell RankPrice*Spell RankPrice*1st30 credits6th1,600 credits2nd70 credits7th3,600 credits3rd180 credits8th7,200 credits4th400 credits9th18,000 credits5th800 credits |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/10/Text/3` | 0.623500 | **Type **advanced; **Level **9; **Price **1,500 credits |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/10/Text/24` | 0.594851 | **Type **superior; **Level **10; **Price **2,000 credits |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/10/Text/5` | 0.591716 | **Type **superior; **Level **13; **Price **6,000 credits |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/10/Text/22` | 0.591714 | **Type **advanced; **Level **6; **Price **500 credits |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/10/Text/9` | 0.590708 | **Type **ultimate; **Level **19; **Price **80,000 credits |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/10/Text/27` | 0.590095 | **Type **elite; **Level **12; **Price **3,500 credits |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/10/Text/18` | 0.588132 | **Type **commercial; **Level **1; **Price **40 credits |

### Query 108
- Text: Lookup values for ItemLevelPriceBulkHandsArchaic text010L1Autograppler,
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/8/Table/22']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/8/Table/22', 'PZO22001 Starfinder Player Core 232-249::/page/9/Table/2', 'PZO22001 Starfinder Player Core 232-249::/page/11/Table/32']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/8/Table/22` | 0.811322 | ItemLevelPriceBulkHandsArchaic text010L1Autograppler, commercial010——Autograppler, tacticalT2250——Cable line, commercial (50 Feet)02L— |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/9/Table/2` | 0.556141 | ItemLevelPriceBulkHandsMicrogogglesT2250L—MicrophoneT08L1Musical instrument, commercial (Handheld)0812Musical instrument, tactical (Handheld)350012Musical instrument, commercial (Heavy)020162Musical i |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/11/Table/32` | 0.547044 | ItemLevelPriceBulkHandsMedpatch, commercial130L1Sprayflesh130L1Bone serum250L1Infiltrator serum250L1Shimmerstone serum250L1Commando serum3100L1Hypopen, tactical3120L1Sharpshooter serum, commercial4140 |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/9/Table/1` | 0.498462 | ItemLevelPriceBulkHandsCable line, tactical (50 Feet)2150L—Camping kit03022Chemalyzer1150L1Climbing kit, commercial0512Climbing kit, tactical34012Comm unitT17L1Container, ordinary01——Container, design |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/11/Table/31` | 0.476475 | ItemLevelPriceBulkHandsCelebrity serum130L—Hypopen, commercial140L— |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/8/TableCell/441` | 0.456549 | Archaic text |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/6/Text/12` | 0.450190 | **Archaic** **Text:** This book could be a religious text, a collection  of ancient recipes, a romance novel, or vintage mechanical  schematics. |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/8/TableCell/451` | 0.448133 | Autograppler, tacticalT |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/16/Table/8` | 0.442709 | Armor (Commercial)Item LevelPriceAC BonusCheck PenaltySpeed PenaltyStrengthBulkUpgradesGroupArmor TraitsAegis Series0300+60-3-10+330PlateBulwark, techDefiance Series0200+51-3-10+331PlateTechHidden Sol |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/10/Text/15` | 0.439791 | **Usage** held in 1 hand; **Bulk **L |

### Query 109
- Text: Lookup values for ItemLevelPriceBulkHandsCable line, tactical
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/9/Table/1']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/8/Table/22', 'PZO22001 Starfinder Player Core 232-249::/page/9/Table/1', 'PZO22001 Starfinder Player Core 232-249::/page/9/TableCell/905']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/8/Table/22` | 0.754337 | ItemLevelPriceBulkHandsArchaic text010L1Autograppler, commercial010——Autograppler, tacticalT2250——Cable line, commercial (50 Feet)02L— |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/9/Table/1` | 0.715215 | ItemLevelPriceBulkHandsCable line, tactical (50 Feet)2150L—Camping kit03022Chemalyzer1150L1Climbing kit, commercial0512Climbing kit, tactical34012Comm unitT17L1Container, ordinary01——Container, design |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/9/TableCell/905` | 0.644399 | Cable line, tactical (50 Feet) |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/9/Table/2` | 0.555500 | ItemLevelPriceBulkHandsMicrogogglesT2250L—MicrophoneT08L1Musical instrument, commercial (Handheld)0812Musical instrument, tactical (Handheld)350012Musical instrument, commercial (Heavy)020162Musical i |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/11/Table/32` | 0.492913 | ItemLevelPriceBulkHandsMedpatch, commercial130L1Sprayflesh130L1Bone serum250L1Infiltrator serum250L1Shimmerstone serum250L1Commando serum3100L1Hypopen, tactical3120L1Sharpshooter serum, commercial4140 |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/16/Table/8` | 0.470835 | Armor (Commercial)Item LevelPriceAC BonusCheck PenaltySpeed PenaltyStrengthBulkUpgradesGroupArmor TraitsAegis Series0300+60-3-10+330PlateBulwark, techDefiance Series0200+51-3-10+331PlateTechHidden Sol |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/6/Text/14` | 0.463383 | **Cable** **Line:** This industrial cable is typically made of highdurability plastic coated in metal. A commercial cable line is |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/16/Table/4` | 0.461661 | Armor (Commercial)Item LevelPriceAC BonusDex CapCheck PenaltySpeed PenaltyStrengthBulkUpgradesGroupArmor TraitsAbadarcorp Travel Suit010+13__+0L2ClothExposed, techArmored Coat020+22-1_+211LeatherComfo |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/6/Text/15` | 0.460601 | coated in titanium alloy, while a tactical cable line is coated in  adamantine alloy. |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/8/TableCell/456` | 0.455885 | Cable line, commercial (50 Feet) |

### Query 110
- Text: Lookup values for ItemLevelPriceBulkHandsMicrogogglesT2250L—MicrophoneT08L1Musical instrument,
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/9/Table/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/9/Table/2', 'PZO22001 Starfinder Player Core 232-249::/page/8/Table/22', 'PZO22001 Starfinder Player Core 232-249::/page/9/Table/1']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/9/Table/2` | 0.888820 | ItemLevelPriceBulkHandsMicrogogglesT2250L—MicrophoneT08L1Musical instrument, commercial (Handheld)0812Musical instrument, tactical (Handheld)350012Musical instrument, commercial (Heavy)020162Musical i |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/8/Table/22` | 0.641811 | ItemLevelPriceBulkHandsArchaic text010L1Autograppler, commercial010——Autograppler, tacticalT2250——Cable line, commercial (50 Feet)02L— |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/9/Table/1` | 0.612955 | ItemLevelPriceBulkHandsCable line, tactical (50 Feet)2150L—Camping kit03022Chemalyzer1150L1Climbing kit, commercial0512Climbing kit, tactical34012Comm unitT17L1Container, ordinary01——Container, design |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/9/TableCell/1110` | 0.522986 | MicrogogglesT |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/9/TableCell/1120` | 0.518010 | Musical instrument, commercial (Handheld) |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/9/TableCell/1125` | 0.513794 | Musical instrument, tactical (Handheld) |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/11/Table/32` | 0.464889 | ItemLevelPriceBulkHandsMedpatch, commercial130L1Sprayflesh130L1Bone serum250L1Infiltrator serum250L1Shimmerstone serum250L1Commando serum3100L1Hypopen, tactical3120L1Sharpshooter serum, commercial4140 |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/11/Table/31` | 0.452686 | ItemLevelPriceBulkHandsCelebrity serum130L—Hypopen, commercial140L— |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/8/Text/14` | 0.450477 | **Musical** **Instrument:** All but the most traditional instruments  use modern technology to amplify their sound, provide musical  accompaniment, or connect wirelessly to other instruments.  Handhel |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/9/TableCell/1115` | 0.447522 | MicrophoneT |

### Query 111
- Text: Lookup values for ItemLevelPriceBulkHandsCelebrity serum130L—Hypopen, commercial140L—
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/11/Table/31']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/11/Table/31', 'PZO22001 Starfinder Player Core 232-249::/page/11/Table/32', 'PZO22001 Starfinder Player Core 232-249::/page/9/Table/1']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/11/Table/31` | 1.027360 | ItemLevelPriceBulkHandsCelebrity serum130L—Hypopen, commercial140L— |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/11/Table/32` | 0.777125 | ItemLevelPriceBulkHandsMedpatch, commercial130L1Sprayflesh130L1Bone serum250L1Infiltrator serum250L1Shimmerstone serum250L1Commando serum3100L1Hypopen, tactical3120L1Sharpshooter serum, commercial4140 |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/9/Table/1` | 0.555069 | ItemLevelPriceBulkHandsCable line, tactical (50 Feet)2150L—Camping kit03022Chemalyzer1150L1Climbing kit, commercial0512Climbing kit, tactical34012Comm unitT17L1Container, ordinary01——Container, design |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/9/Table/2` | 0.499473 | ItemLevelPriceBulkHandsMicrogogglesT2250L—MicrophoneT08L1Musical instrument, commercial (Handheld)0812Musical instrument, tactical (Handheld)350012Musical instrument, commercial (Heavy)020162Musical i |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/11/TableCell/747` | 0.495934 | Celebrity serum |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/8/Table/22` | 0.487011 | ItemLevelPriceBulkHandsArchaic text010L1Autograppler, commercial010——Autograppler, tacticalT2250——Cable line, commercial (50 Feet)02L— |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/11/TableCell/752` | 0.483356 | Hypopen, commercial |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/3/Table/16` | 0.477129 | Creature SizePriceBulkLight BecomesNegligible BecomesTinyStandardHalf*_-Small or Med.StandardStandardL-LargeStandard×21 BulkLHuge×4×42 Bulk1 BulkGargantuan×8×84 Bulk2 Bulk |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/10/SectionHeader/39` | 0.472139 | **CELEBRITY SERUM** **ITEM 1** |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/3/Table/11` | 0.466415 | Creature SizeBulk LimitTreats as LightTreats as NegligibleTinyHalf-noneSmall or Med.StandardL-Large×21 BulkL |

### Query 112
- Text: Lookup values for ItemLevelPriceBulkHandsMedpatch, commercial130L1Sprayflesh130L1Bone serum250L1Infiltrator serum250L1Shimmerstone serum250L1Commando serum3100L1Hypopen, tactical3120L1Sharpshooter serum,
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/11/Table/32']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/11/Table/32', 'PZO22001 Starfinder Player Core 232-249::/page/11/Table/31', 'PZO22001 Starfinder Player Core 232-249::/page/9/Table/1']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/11/Table/32` | 0.999623 | ItemLevelPriceBulkHandsMedpatch, commercial130L1Sprayflesh130L1Bone serum250L1Infiltrator serum250L1Shimmerstone serum250L1Commando serum3100L1Hypopen, tactical3120L1Sharpshooter serum, commercial4140 |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/11/Table/31` | 0.758956 | ItemLevelPriceBulkHandsCelebrity serum130L—Hypopen, commercial140L— |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/9/Table/1` | 0.680129 | ItemLevelPriceBulkHandsCable line, tactical (50 Feet)2150L—Camping kit03022Chemalyzer1150L1Climbing kit, commercial0512Climbing kit, tactical34012Comm unitT17L1Container, ordinary01——Container, design |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/9/Table/2` | 0.556012 | ItemLevelPriceBulkHandsMicrogogglesT2250L—MicrophoneT08L1Musical instrument, commercial (Handheld)0812Musical instrument, tactical (Handheld)350012Musical instrument, commercial (Heavy)020162Musical i |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/8/Table/22` | 0.541996 | ItemLevelPriceBulkHandsArchaic text010L1Autograppler, commercial010——Autograppler, tacticalT2250——Cable line, commercial (50 Feet)02L— |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/11/TableCell/837` | 0.526338 | Sharpshooter serum, tactical |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/11/TableCell/797` | 0.504369 | Sharpshooter serum, commercial |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/16/Table/6` | 0.483327 | Armor (Commercial)Item LevelPriceAC BonusCheck PenaltySpeed PenaltyStrengthBulkUpgradesGroupArmor TraitsDefrex Hide025+32-2-5+221LeatherTechFreebooter Armor065+41-2-5+321PlateTechShotalashu Armor040+3 |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/16/Table/8` | 0.476316 | Armor (Commercial)Item LevelPriceAC BonusCheck PenaltySpeed PenaltyStrengthBulkUpgradesGroupArmor TraitsAegis Series0300+60-3-10+330PlateBulwark, techDefiance Series0200+51-3-10+331PlateTechHidden Sol |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/9/Text/10` | 0.465785 | **MEDPATCH** **ITEM 1+** |

### Query 113
- Text: Lookup values for Standard of
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/11/Table/36']
- Expected found: `True`
- Expected rank: `8`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/282', 'PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/287', 'PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/292']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/282` | 0.706293 | Standard |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/292` | 0.706293 | Standard |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/287` | 0.706293 | Standard |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/288` | 0.676293 | Standard |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/257` | 0.664293 | Standard |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/11/TableCell/852` | 0.600252 | Standard of Living |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/2/SectionHeader/17` | 0.405035 | Bulk Values |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/11/Table/36` | 0.393167 | Standard of LivingWeekMonthYearSubsistenceno costno costno costComfortable10 credits40 credits400 creditsFine300 credits1,300 credits16,000 creditsExtravagant1,000 credits4,300 credits52,000 credits |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/3/Table/16` | 0.372739 | Creature SizePriceBulkLight BecomesNegligible BecomesTinyStandardHalf*_-Small or Med.StandardStandardL-LargeStandard×21 BulkLHuge×4×42 Bulk1 BulkGargantuan×8×84 Bulk2 Bulk |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/16/TableCell/66` | 0.324819 | Item Level |

### Query 114
- Text: Lookup values for Spell RankPrice*Spell RankPrice*1st30 credits6th1,600 credits2nd70 credits7th3,600 credits3rd180 credits8th7,200 credits4th400 credits9th18,000 credits5th800 credits
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/11/Table/40']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/11/Table/40', 'PZO22001 Starfinder Player Core 232-249::/page/5/Table/19', 'PZO22001 Starfinder Player Core 232-249::/page/11/TableCell/874']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/11/Table/40` | 1.004983 | Spell RankPrice*Spell RankPrice*1st30 credits6th1,600 credits2nd70 credits7th3,600 credits3rd180 credits8th7,200 credits4th400 credits9th18,000 credits5th800 credits |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/5/Table/19` | 0.685039 | LevelPriceLevelPrice0*5 credits11700 credits110 credits121,000 credits220 credits131,500 credits330 credits142,250 credits450 credits153,250 credits580 credits165,000 credits6130 credits177,500 credit |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/11/TableCell/874` | 0.683469 | Spell Rank |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/11/TableCell/872` | 0.653469 | Spell Rank |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/16/Table/10` | 0.529535 | GradeLevelImprovement PriceTotal PriceUpgradesAC Bonus IncreaseTraitsCommercial0---+0_Tactical5+1,600 credits1,600 credits+1+1_Advanced8+3,400 credits5,000 credits+1+1Resilient +1Superior11+9,000 cred |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/10/Text/27` | 0.467669 | **Type **elite; **Level **12; **Price **3,500 credits |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/16/Table/8` | 0.467276 | Armor (Commercial)Item LevelPriceAC BonusCheck PenaltySpeed PenaltyStrengthBulkUpgradesGroupArmor TraitsAegis Series0300+60-3-10+330PlateBulwark, techDefiance Series0200+51-3-10+331PlateTechHidden Sol |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/10/Text/7` | 0.465250 | **Type **elite; **Level **15; **Price **13,000 credits |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/10/Text/29` | 0.455213 | **Type **ultimate; **Level **14; **Price **7,000 credits |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/10/Text/3` | 0.451834 | **Type **advanced; **Level **9; **Price **1,500 credits |

### Query 115
- Text: Lookup values for MaterialHardnessHPBTCeramic52010Chain93618Cloth142Composite72814Leather4168Plate93618Polymer3126
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/14/Table/3']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/14/Table/3', 'PZO22001 Starfinder Player Core 232-249::/page/16/Table/6', 'PZO22001 Starfinder Player Core 232-249::/page/16/Table/4']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/14/Table/3` | 0.991638 | MaterialHardnessHPBTCeramic52010Chain93618Cloth142Composite72814Leather4168Plate93618Polymer3126 |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/16/Table/6` | 0.573439 | Armor (Commercial)Item LevelPriceAC BonusCheck PenaltySpeed PenaltyStrengthBulkUpgradesGroupArmor TraitsDefrex Hide025+32-2-5+221LeatherTechFreebooter Armor065+41-2-5+321PlateTechShotalashu Armor040+3 |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/16/Table/4` | 0.560237 | Armor (Commercial)Item LevelPriceAC BonusDex CapCheck PenaltySpeed PenaltyStrengthBulkUpgradesGroupArmor TraitsAbadarcorp Travel Suit010+13__+0L2ClothExposed, techArmored Coat020+22-1_+211LeatherComfo |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/16/Table/8` | 0.488809 | Armor (Commercial)Item LevelPriceAC BonusCheck PenaltySpeed PenaltyStrengthBulkUpgradesGroupArmor TraitsAegis Series0300+60-3-10+330PlateBulwark, techDefiance Series0200+51-3-10+331PlateTechHidden Sol |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/4/Text/18` | 0.479673 | An item's Hardness, Hit Points, and Broken Threshold usually depend on the material the item is made of. Information on materials appears in *Starfinder GM Core*. |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/14/TableCell/430` | 0.442645 | Material |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/9/Table/1` | 0.440056 | ItemLevelPriceBulkHandsCable line, tactical (50 Feet)2150L—Camping kit03022Chemalyzer1150L1Climbing kit, commercial0512Climbing kit, tactical34012Comm unitT17L1Container, ordinary01——Container, design |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/14/Text/6` | 0.429520 | **Ceramic:** Delicate yet sturdy, treated ceramic plating  is common on spacesuits. It resists heat and other  environmental hazards and is lightweight enough to fit into.  You gain resistance to acid |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/5/Table/19` | 0.412116 | LevelPriceLevelPrice0*5 credits11700 credits110 credits121,000 credits220 credits131,500 credits330 credits142,250 credits450 credits153,250 credits580 credits165,000 credits6130 credits177,500 credit |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/14/Text/10` | 0.409926 | **Plate:** The sturdy plate provides no purchase for a cutting  edge. You gain resistance to slashing damage equal to 1 +  the armor's resilience value for medium armor, or 2 + the  armor's resilience |

### Query 116
- Text: Lookup values for ArmorItem
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/16/Table/2']
- Expected found: `True`
- Expected rank: `19`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/13/SectionHeader/1', 'PZO22001 Starfinder Player Core 232-249::/page/14/SectionHeader/13', 'PZO22001 Starfinder Player Core 232-249::/page/16/Table/6']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/13/SectionHeader/1` | 0.596497 | ARMOR STATISTICS |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/14/SectionHeader/13` | 0.587154 | ARMOR DESCRIPTIONS |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/16/Table/6` | 0.580191 | Armor (Commercial)Item LevelPriceAC BonusCheck PenaltySpeed PenaltyStrengthBulkUpgradesGroupArmor TraitsDefrex Hide025+32-2-5+221LeatherTechFreebooter Armor065+41-2-5+321PlateTechShotalashu Armor040+3 |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/13/Text/6` | 0.531174 | This number is the item bonus you add for the armor when  determining Armor Class. |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/3/Text/33` | 0.529242 | Armor |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/16/TableCell/32` | 0.529242 | Armor |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/11/Text/50` | 0.519309 | **Armor** |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/1/Text/32` | 0.519309 | **Armor** |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/17/Text/10` | 0.519309 | **Armor** |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/13/Text/42` | 0.519309 | **Armor** |

### Query 117
- Text: Lookup values for Armor
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/16/Table/4']
- Expected found: `True`
- Expected rank: `42`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/3/Text/33', 'PZO22001 Starfinder Player Core 232-249::/page/16/TableCell/32', 'PZO22001 Starfinder Player Core 232-249::/page/13/SectionHeader/1']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/3/Text/33` | 0.714719 | Armor |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/16/TableCell/32` | 0.714719 | Armor |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/13/SectionHeader/1` | 0.692786 | ARMOR STATISTICS |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/14/SectionHeader/13` | 0.636828 | ARMOR DESCRIPTIONS |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/9/Text/25` | 0.629257 | **Armor** |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/15/Text/19` | 0.629257 | **Armor** |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/7/Text/22` | 0.629257 | **Armor** |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/11/Text/50` | 0.629257 | **Armor** |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/13/Text/42` | 0.629257 | **Armor** |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/5/Text/29` | 0.629257 | **Armor** |

### Query 118
- Text: Lookup values for Armor
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/16/Table/6']
- Expected found: `True`
- Expected rank: `35`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/3/Text/33', 'PZO22001 Starfinder Player Core 232-249::/page/16/TableCell/32', 'PZO22001 Starfinder Player Core 232-249::/page/13/SectionHeader/1']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/3/Text/33` | 0.714719 | Armor |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/16/TableCell/32` | 0.714719 | Armor |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/13/SectionHeader/1` | 0.692786 | ARMOR STATISTICS |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/14/SectionHeader/13` | 0.636828 | ARMOR DESCRIPTIONS |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/9/Text/25` | 0.629257 | **Armor** |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/15/Text/19` | 0.629257 | **Armor** |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/7/Text/22` | 0.629257 | **Armor** |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/11/Text/50` | 0.629257 | **Armor** |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/13/Text/42` | 0.629257 | **Armor** |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/5/Text/29` | 0.629257 | **Armor** |

### Query 119
- Text: Lookup values for Armor
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/16/Table/8']
- Expected found: `True`
- Expected rank: `44`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/3/Text/33', 'PZO22001 Starfinder Player Core 232-249::/page/16/TableCell/32', 'PZO22001 Starfinder Player Core 232-249::/page/13/SectionHeader/1']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/3/Text/33` | 0.714719 | Armor |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/16/TableCell/32` | 0.714719 | Armor |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/13/SectionHeader/1` | 0.692786 | ARMOR STATISTICS |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/14/SectionHeader/13` | 0.636828 | ARMOR DESCRIPTIONS |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/9/Text/25` | 0.629257 | **Armor** |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/15/Text/19` | 0.629257 | **Armor** |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/7/Text/22` | 0.629257 | **Armor** |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/11/Text/50` | 0.629257 | **Armor** |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/13/Text/42` | 0.629257 | **Armor** |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/5/Text/29` | 0.629257 | **Armor** |

### Query 120
- Text: Lookup values for GradeLevelImprovement PriceTotal PriceUpgradesAC Bonus IncreaseTraitsCommercial0---+0_Tactical5+1,600 credits1,600 credits+1+1_Advanced8+3,400 credits5,000 credits+1+1Resilient +1Superior11+9,000 credits14,000 credits+2+2Resilient +1Elite14+31,000 credits45,000 credits+2+2Resilient +2Ultimate18+195,000 credits240,000 credits+3+3Resilient +2Paragon20+460,000 credits700,000 credits+3+3Resilient +3
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 232-249::/page/16/Table/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 232-249::/page/16/Table/10', 'PZO22001 Starfinder Player Core 232-249::/page/5/Table/19', 'PZO22001 Starfinder Player Core 232-249::/page/10/Text/3']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 232-249::/page/16/Table/10` | 1.015796 | GradeLevelImprovement PriceTotal PriceUpgradesAC Bonus IncreaseTraitsCommercial0---+0_Tactical5+1,600 credits1,600 credits+1+1_Advanced8+3,400 credits5,000 credits+1+1Resilient +1Superior11+9,000 cred |
| 2 | `PZO22001 Starfinder Player Core 232-249::/page/5/Table/19` | 0.757222 | LevelPriceLevelPrice0*5 credits11700 credits110 credits121,000 credits220 credits131,500 credits330 credits142,250 credits450 credits153,250 credits580 credits165,000 credits6130 credits177,500 credit |
| 3 | `PZO22001 Starfinder Player Core 232-249::/page/10/Text/3` | 0.611494 | **Type **advanced; **Level **9; **Price **1,500 credits |
| 4 | `PZO22001 Starfinder Player Core 232-249::/page/10/Text/22` | 0.560434 | **Type **advanced; **Level **6; **Price **500 credits |
| 5 | `PZO22001 Starfinder Player Core 232-249::/page/16/Table/8` | 0.557566 | Armor (Commercial)Item LevelPriceAC BonusCheck PenaltySpeed PenaltyStrengthBulkUpgradesGroupArmor TraitsAegis Series0300+60-3-10+330PlateBulwark, techDefiance Series0200+51-3-10+331PlateTechHidden Sol |
| 6 | `PZO22001 Starfinder Player Core 232-249::/page/10/Text/18` | 0.555447 | **Type **commercial; **Level **1; **Price **40 credits |
| 7 | `PZO22001 Starfinder Player Core 232-249::/page/16/Table/4` | 0.554622 | Armor (Commercial)Item LevelPriceAC BonusDex CapCheck PenaltySpeed PenaltyStrengthBulkUpgradesGroupArmor TraitsAbadarcorp Travel Suit010+13__+0L2ClothExposed, techArmored Coat020+22-1_+211LeatherComfo |
| 8 | `PZO22001 Starfinder Player Core 232-249::/page/16/Table/6` | 0.549994 | Armor (Commercial)Item LevelPriceAC BonusCheck PenaltySpeed PenaltyStrengthBulkUpgradesGroupArmor TraitsDefrex Hide025+32-2-5+221LeatherTechFreebooter Armor065+41-2-5+321PlateTechShotalashu Armor040+3 |
| 9 | `PZO22001 Starfinder Player Core 232-249::/page/10/Text/7` | 0.543269 | **Type **elite; **Level **15; **Price **13,000 credits |
| 10 | `PZO22001 Starfinder Player Core 232-249::/page/11/Text/20` | 0.542163 | **Type **commercial; **Level **4; **Price **140 credits |
