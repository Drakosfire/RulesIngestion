# RulesLawyer Evaluation Report: nomic-embed-text-v2

## Summary
- Run ID: `None`
- Ruleset ID: `None`
- Document ID: `None`
- Chunk source: `enriched`
- Chunk count: `1242`
- Query count: `108`
- Evaluated queries: `108`
- Coverage: `1.0000`
- MRR: `0.8965`
- hit@1: `0.8704`
- hit@3: `0.9074`
- hit@5: `0.9167`
- hit@10: `0.9537`
- Embeddings reused: `False`
- Graph boost: `0.05` (depth=2, top_k=50, source=top, seed_top_n=3, same_kind_only=False, decay=0.4)

### Expanded Gold Metrics
- Coverage: `1.0000`
- MRR: `0.9043`
- hit@1: `0.8796`
- hit@3: `0.9167`
- hit@5: `0.9259`
- hit@10: `0.9537`

### Expanded Gold Expansion Stats
- Queries with additions: `108`
- Avg added per query: `2.04`
- Max added: `7`
- Addition reasons:
  - graph_depth_1: `220`

### Expanded Gold Delta (Expanded - Strict)
- Coverage Δ: `0.0000`
- MRR Δ: `0.0077`
- hit@1 Δ: `0.0093`
- hit@3 Δ: `0.0093`
- hit@5 Δ: `0.0093`
- hit@10 Δ: `0.0000`

## Timings (ms)
- Embedding (chunks): `15928`
- Embedding (queries): `2855`
- Evaluation (strict): `119`
- Evaluation (expanded): `139`
- Total: `23407`

### Timing Estimates (ms)
- Evaluation (strict): `216`
- Evaluation (expanded): `291`
- Total: `19290`

## Query Details
### Query 0
- Text: Summarize ARMOR UPGRADES
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/0/SectionHeader/1']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/1/SectionHeader/3', 'PZO22001 Starfinder Player Core 268-281::/page/0/SectionHeader/1', 'PZO22001 Starfinder Player Core 268-281::/page/3/SectionHeader/2']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/0/SectionHeader/1', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/3']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/0/Text/3` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/1/SectionHeader/3` | 0.984246 | ARMOR UPGRADES |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/0/SectionHeader/1` | 0.984246 | ARMOR UPGRADES |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/3/SectionHeader/2` | 0.949297 | **ARMOR UPGRADES** |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/0/SectionHeader/8` | 0.875564 | ACTIVATING ARMOR UPGRADES |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/0/SectionHeader/10` | 0.868654 | LIMITED ARMOR UPGRADES |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/5/Text/78` | 0.852911 | **Armor ** **Upgrades** |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/77` | 0.852910 | **Armor ** **Upgrades** |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/7/Text/39` | 0.852910 | **Armor ** **Upgrades** |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/3/Text/11` | 0.852910 | **Armor ** **Upgrades** |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/11/Text/50` | 0.852910 | **Armor ** **Upgrades** |

### Query 1
- Text: What is the rule about You can personalize armor by purchasing and installing armor  upgrades. Armor upgrades are installed into the upgrade slots  of armor; one armor upgrade occupies one armor upgrade slot.  The number of upgrade slots a specific suit of armor has is noted  under that armor's description. You can install an armor upgrade  with the Install Upgrade activity, which takes 10 minutes to  perform. Unlike many other types of equipment, armor upgrades  run on kinetic energy created by your body's motion, and they  don't need external batteries. They function only when installed  in armor you're wearing properly.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/3']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/3', 'PZO22001 Starfinder Player Core 268-281::/page/4/Text/3', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/7']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/3', 'PZO22001 Starfinder Player Core 268-281::/page/0/SectionHeader/4', 'PZO22001 Starfinder Player Core 268-281::/page/0/SectionHeader/1']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/0/SectionHeader/4` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/0/SectionHeader/1` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/3` | 1.000413 | You can personalize armor by purchasing and installing armor  upgrades. Armor upgrades are installed into the upgrade slots  of armor; one armor upgrade occupies one armor upgrade slot.  The number of |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/4/Text/3` | 0.793917 | You can personalize weapons by purchasing and installing  weapon upgrades, found on the Weapon Upgrades table  (page 277). Technological weapon upgrades are called  weapon modifications, while hybrid |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/7` | 0.710214 | You spend 10 minutes installing an upgrade into a suit of armor  or weapon, placing it into an empty upgrade slot. You can also  use this activity to uninstall an upgrade. You can't install more  upgr |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/11` | 0.636032 | Some armor upgrades that have special activations and benefits  can be activated only a limited number of times per day, as  described in the armor upgrade. This limit is independent of any  costs for |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/9` | 0.620698 | Most upgrades grant their benefits continually so long as  you're properly wearing the armor they're installed in. Others  produce their effects only when used properly in the moment  by spending acti |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/0/SectionHeader/8` | 0.576328 | ACTIVATING ARMOR UPGRADES |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/23` | 0.570384 | **Activate—Glamerize!** [one-action] (manipulate) **Effect** You instantly  change the appearance of your armor to any set of normal  clothes or any other type of light or heavy armor. This  upgrade i |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/0/SectionHeader/1` | 0.569086 | ARMOR UPGRADES |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/7/Text/39` | 0.567010 | **Armor ** **Upgrades** |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/11/Text/50` | 0.567010 | **Armor ** **Upgrades** |

### Query 2
- Text: Summarize **INSTALL UPGRADE**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/0/SectionHeader/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/0/SectionHeader/4', 'PZO22001 Starfinder Player Core 268-281::/page/9/Text/34', 'PZO22001 Starfinder Player Core 268-281::/page/13/Text/50']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/0/SectionHeader/4', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/3', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/5']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/0/Text/3` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/0/Text/5` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/0/SectionHeader/4` | 0.990312 | **INSTALL UPGRADE** |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/9/Text/34` | 0.715916 | **Upgrades** |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/13/Text/50` | 0.715916 | **Upgrades** |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/9/SectionHeader/17` | 0.626849 | **WEAPON UPGRADES** |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/13/Text/51` | 0.574997 | **Weapon ** **Upgrades** |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/9/Text/35` | 0.574997 | **Weapon ** **Upgrades** |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/3/SectionHeader/2` | 0.570921 | **ARMOR UPGRADES** |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/11/Text/51` | 0.562998 | **Weapon ** **Upgrades** |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/3/Text/12` | 0.562998 | **Weapon ** **Upgrades** |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/5/Text/79` | 0.562998 | **Weapon ** **Upgrades** |

### Query 3
- Text: Summarize **EXPLORATION** **MANIPULATE**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/5', 'PZO22001 Starfinder Player Core 268-281::/page/2/Text/2', 'PZO22001 Starfinder Player Core 268-281::/page/2/Text/29']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/5', 'PZO22001 Starfinder Player Core 268-281::/page/0/SectionHeader/4', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/6']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/0/SectionHeader/4` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/0/Text/6` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/5` | 0.993621 | **EXPLORATION** **MANIPULATE** |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/2` | 0.519290 | **Activate—Raise Force Field** [one-action] (manipulate) **Frequency** three  times per day; **Effect** Your force field becomes active. It  remains active for 1 minute or until it's reduced to 0 Hit |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/29` | 0.500614 | **Activate—Fly** [one-action] (manipulate) **Effect** You activate a jetpack to  gain a fly Speed of 20 feet. This effect lasts for 1 minute or  until you Dismiss it. You can use an action to Fly 0 fe |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/7/Text/9` | 0.457046 | **Activate—See the Truth**[two-actions] (manipulate) **Frequency** once per  day; **Effect** For the next 10 minutes, while looking through  the scope, you can see invisible creatures as though they |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/58` | 0.456462 | **Activate—Defensive Detonation **[one-action] (manipulate) **Requirements** You have a stored grenade; **Effect** You detonate the grenade  stored in the explosive defense unit. The explosion is cent |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/39` | 0.432115 | **Activate—Jump** [one-action] (manipulate) **Frequency** once per round;  **Effect** You activate the jump jets to get a quick boost. You  Fly up to 20 feet with a maximum height of 10 feet, or  you |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/55` | 0.418592 | **Activate—Thrust** [one-action] (move) **Requirements** You're in a zero-g  environment; **Effect** You move 5 feet in any direction you  choose. You begin to float in that direction. |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/4/Text/18` | 0.404345 | **Activate—Autoattack** [two-actions] (concentrate, manipulate) **Effect** You Release the weapon and it glides through the air,  fighting on its own against the last enemy you attacked, or  the neare |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/57` | 0.393660 | **Activate—Store Grenade** [two-actions] (manipulate) **Effect** You place a  grenade inside a reinforced compartment in the explosive  defense unit. You can Interact to retrieve the grenade  normally |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/32` | 0.392185 | **Activate—Bend Light **[one-action] (manipulate) **Frequency** once per day;  **Effect** You become invisible for 1 minute, gaining the effects  of a 2nd-rank *invisibility* spell. |

### Query 4
- Text: What is the rule about **Requirements** You must use a repair toolkit.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/6', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/7', 'PZO22001 Starfinder Player Core 268-281::/page/3/Text/8']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/6', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/7', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/5']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/0/Text/7` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/0/Text/5` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/6` | 0.861334 | **Requirements** You must use a repair toolkit. |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/7` | 0.536796 | You spend 10 minutes installing an upgrade into a suit of armor  or weapon, placing it into an empty upgrade slot. You can also  use this activity to uninstall an upgrade. You can't install more  upgr |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/3/Text/8` | 0.411720 | **EQUIPMENT** **Introduction** |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/11/Text/43` | 0.357844 | **EQUIPMENT** |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/9/Text/28` | 0.357844 | **EQUIPMENT** |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/71` | 0.357844 | **EQUIPMENT** |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/7/Text/33` | 0.357844 | **EQUIPMENT** |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/13/Text/43` | 0.357844 | **EQUIPMENT** |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/5/Text/71` | 0.357844 | **EQUIPMENT** |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/2/SectionHeader/50` | 0.353614 | **MANEUVERING UNIT** **UPGRADE 4+** |

### Query 5
- Text: What is the rule about You spend 10 minutes installing an upgrade into a suit of armor  or weapon, placing it into an empty upgrade slot. You can also  use this activity to uninstall an upgrade. You can't install more  upgrades than there are upgrade slots. Installing or uninstalling  an upgrade requires using a repair toolkit with two hands.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/7', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/3', 'PZO22001 Starfinder Player Core 268-281::/page/4/Text/9']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/7', 'PZO22001 Starfinder Player Core 268-281::/page/0/SectionHeader/8', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/6']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/0/SectionHeader/8` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/0/Text/6` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/7` | 0.985844 | You spend 10 minutes installing an upgrade into a suit of armor  or weapon, placing it into an empty upgrade slot. You can also  use this activity to uninstall an upgrade. You can't install more  upgr |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/3` | 0.675366 | You can personalize armor by purchasing and installing armor  upgrades. Armor upgrades are installed into the upgrade slots  of armor; one armor upgrade occupies one armor upgrade slot.  The number of |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/4/Text/9` | 0.663862 | Some upgrades attach to or upgrade a specific part of a  weapon. A weapon can only have one such upgrade at a time.  These will always be designated in the upgrade's usage entry,  such as "installed i |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/4/Text/3` | 0.601532 | You can personalize weapons by purchasing and installing  weapon upgrades, found on the Weapon Upgrades table  (page 277). Technological weapon upgrades are called  weapon modifications, while hybrid |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/11` | 0.591045 | Some armor upgrades that have special activations and benefits  can be activated only a limited number of times per day, as  described in the armor upgrade. This limit is independent of any  costs for |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/4/Text/7` | 0.571571 | Some weapon upgrades that have special activations and  abilities can be activated only a limited number of times  per day, as described in the weapon upgrade. This limit is  independent of any costs |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/9` | 0.566959 | Most upgrades grant their benefits continually so long as  you're properly wearing the armor they're installed in. Others  produce their effects only when used properly in the moment  by spending acti |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/4/Text/5` | 0.558876 | Most upgrades grant their benefits continually so long as  you're wielding the weapon they're installed in. Others  produce their effects only when used properly in the moment  by spending actions. An |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/6` | 0.521754 | **Requirements** You must use a repair toolkit. |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/57` | 0.488982 | **Activate—Store Grenade** [two-actions] (manipulate) **Effect** You place a  grenade inside a reinforced compartment in the explosive  defense unit. You can Interact to retrieve the grenade  normally |

### Query 6
- Text: What is the rule about ACTIVATING ARMOR UPGRADES?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/0/SectionHeader/8']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/0/SectionHeader/8', 'PZO22001 Starfinder Player Core 268-281::/page/0/SectionHeader/1', 'PZO22001 Starfinder Player Core 268-281::/page/1/SectionHeader/3']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/0/SectionHeader/8', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/9', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/7']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/0/Text/9` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/0/Text/7` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/0/SectionHeader/8` | 0.848656 | ACTIVATING ARMOR UPGRADES |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/0/SectionHeader/1` | 0.719129 | ARMOR UPGRADES |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/1/SectionHeader/3` | 0.719129 | ARMOR UPGRADES |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/3/SectionHeader/2` | 0.661292 | **ARMOR UPGRADES** |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/9` | 0.651111 | Most upgrades grant their benefits continually so long as  you're properly wearing the armor they're installed in. Others  produce their effects only when used properly in the moment  by spending acti |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/0/SectionHeader/10` | 0.635976 | LIMITED ARMOR UPGRADES |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/4/SectionHeader/4` | 0.621095 | ACTIVATING WEAPON UPGRADES |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/3` | 0.620779 | You can personalize armor by purchasing and installing armor  upgrades. Armor upgrades are installed into the upgrade slots  of armor; one armor upgrade occupies one armor upgrade slot.  The number of |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/11` | 0.607338 | Some armor upgrades that have special activations and benefits  can be activated only a limited number of times per day, as  described in the armor upgrade. This limit is independent of any  costs for |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/11/Text/50` | 0.582548 | **Armor ** **Upgrades** |

### Query 7
- Text: What is the rule about Most upgrades grant their benefits continually so long as  you're properly wearing the armor they're installed in. Others  produce their effects only when used properly in the moment  by spending actions. An activation lists the number of actions  it takes and any traits for the activation and its effects. This  information appears in the item's Activate entry.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/9', 'PZO22001 Starfinder Player Core 268-281::/page/4/Text/5', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/11']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/9', 'PZO22001 Starfinder Player Core 268-281::/page/0/SectionHeader/10', 'PZO22001 Starfinder Player Core 268-281::/page/0/SectionHeader/8']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/0/SectionHeader/10` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/0/SectionHeader/8` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/9` | 1.004904 | Most upgrades grant their benefits continually so long as  you're properly wearing the armor they're installed in. Others  produce their effects only when used properly in the moment  by spending acti |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/4/Text/5` | 0.950186 | Most upgrades grant their benefits continually so long as  you're wielding the weapon they're installed in. Others  produce their effects only when used properly in the moment  by spending actions. An |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/11` | 0.695708 | Some armor upgrades that have special activations and benefits  can be activated only a limited number of times per day, as  described in the armor upgrade. This limit is independent of any  costs for |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/4/Text/9` | 0.609936 | Some upgrades attach to or upgrade a specific part of a  weapon. A weapon can only have one such upgrade at a time.  These will always be designated in the upgrade's usage entry,  such as "installed i |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/4/Text/7` | 0.596782 | Some weapon upgrades that have special activations and  abilities can be activated only a limited number of times  per day, as described in the weapon upgrade. This limit is  independent of any costs |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/57` | 0.572532 | **Activate—Store Grenade** [two-actions] (manipulate) **Effect** You place a  grenade inside a reinforced compartment in the explosive  defense unit. You can Interact to retrieve the grenade  normally |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/3` | 0.571985 | You can personalize armor by purchasing and installing armor  upgrades. Armor upgrades are installed into the upgrade slots  of armor; one armor upgrade occupies one armor upgrade slot.  The number of |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/20` | 0.569216 | **Activate—Adapt** [reaction] **Frequency** once per 10 minutes; **Trigger** You  take acid, cold, electricity, or fire damage; **Effect** Your *energy * *shielding* upgrade changes to the triggering |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/23` | 0.561896 | **Activate—Glamerize!** [one-action] (manipulate) **Effect** You instantly  change the appearance of your armor to any set of normal  clothes or any other type of light or heavy armor. This  upgrade i |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/7` | 0.542605 | You spend 10 minutes installing an upgrade into a suit of armor  or weapon, placing it into an empty upgrade slot. You can also  use this activity to uninstall an upgrade. You can't install more  upgr |

### Query 8
- Text: Summarize LIMITED ARMOR UPGRADES
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/0/SectionHeader/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/0/SectionHeader/10', 'PZO22001 Starfinder Player Core 268-281::/page/1/SectionHeader/3', 'PZO22001 Starfinder Player Core 268-281::/page/0/SectionHeader/1']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/0/SectionHeader/10', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/11', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/9']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/0/Text/11` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/0/Text/9` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/0/SectionHeader/10` | 1.001472 | LIMITED ARMOR UPGRADES |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/1/SectionHeader/3` | 0.843569 | ARMOR UPGRADES |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/0/SectionHeader/1` | 0.843569 | ARMOR UPGRADES |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/3/SectionHeader/2` | 0.772874 | **ARMOR UPGRADES** |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/0/SectionHeader/8` | 0.744924 | ACTIVATING ARMOR UPGRADES |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/4/SectionHeader/6` | 0.737452 | LIMITED WEAPON UPGRADES |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/11/Text/50` | 0.733700 | **Armor ** **Upgrades** |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/7/Text/39` | 0.733700 | **Armor ** **Upgrades** |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/3/Text/11` | 0.733700 | **Armor ** **Upgrades** |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/77` | 0.733700 | **Armor ** **Upgrades** |

### Query 9
- Text: What is the rule about Some armor upgrades that have special activations and benefits  can be activated only a limited number of times per day, as  described in the armor upgrade. This limit is independent of any  costs for activating the upgrade. This limit resets during your  daily preparations. The limit is inherent to the armor upgrade, so  if an ability that can be used only once per day is used, it doesn't  refresh if the armor upgrade is uninstalled and reinstalled or is  installed in another suit of armor, or if another creature tries to  activate the upgrade. Similarly, armor has innate safety overrides  that prevent you from installing a duplicate of an armor upgrade  you've already used the limited action of and from trying to use  that action again.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/11', 'PZO22001 Starfinder Player Core 268-281::/page/4/Text/7', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/9']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/11', 'PZO22001 Starfinder Player Core 268-281::/page/0/SectionHeader/10', 'PZO22001 Starfinder Player Core 268-281::/page/0/SectionHeader/12']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/0/SectionHeader/10` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/0/SectionHeader/12` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/11` | 1.023126 | Some armor upgrades that have special activations and benefits  can be activated only a limited number of times per day, as  described in the armor upgrade. This limit is independent of any  costs for |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/4/Text/7` | 0.908532 | Some weapon upgrades that have special activations and  abilities can be activated only a limited number of times  per day, as described in the weapon upgrade. This limit is  independent of any costs |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/9` | 0.660037 | Most upgrades grant their benefits continually so long as  you're properly wearing the armor they're installed in. Others  produce their effects only when used properly in the moment  by spending acti |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/4/Text/5` | 0.563856 | Most upgrades grant their benefits continually so long as  you're wielding the weapon they're installed in. Others  produce their effects only when used properly in the moment  by spending actions. An |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/3` | 0.562178 | You can personalize armor by purchasing and installing armor  upgrades. Armor upgrades are installed into the upgrade slots  of armor; one armor upgrade occupies one armor upgrade slot.  The number of |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/7` | 0.552801 | You spend 10 minutes installing an upgrade into a suit of armor  or weapon, placing it into an empty upgrade slot. You can also  use this activity to uninstall an upgrade. You can't install more  upgr |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/4/Text/9` | 0.546421 | Some upgrades attach to or upgrade a specific part of a  weapon. A weapon can only have one such upgrade at a time.  These will always be designated in the upgrade's usage entry,  such as "installed i |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/20` | 0.526258 | **Activate—Adapt** [reaction] **Frequency** once per 10 minutes; **Trigger** You  take acid, cold, electricity, or fire damage; **Effect** Your *energy * *shielding* upgrade changes to the triggering |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/0/SectionHeader/10` | 0.514332 | LIMITED ARMOR UPGRADES |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/0/SectionHeader/8` | 0.494171 | ACTIVATING ARMOR UPGRADES |

### Query 10
- Text: Summarize ENVIRONMENTAL  PROTECTION UPGRADES
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/0/SectionHeader/12']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/0/SectionHeader/12', 'PZO22001 Starfinder Player Core 268-281::/page/0/SectionHeader/14', 'PZO22001 Starfinder Player Core 268-281::/page/3/SectionHeader/5']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/0/SectionHeader/12', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/11', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/13']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/0/Text/11` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/0/Text/13` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/0/SectionHeader/12` | 1.014456 | ENVIRONMENTAL  PROTECTION UPGRADES |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/0/SectionHeader/14` | 0.786069 | **BASIC ENVIRONMENTAL PROTECTION** **UPGRADE 0** |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/3/SectionHeader/5` | 0.768235 | **ENVIRONMENTAL PROTECTIONS** |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/3/TableCell/760` | 0.564454 | Basic environmental protection |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/13/Text/50` | 0.562721 | **Upgrades** |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/9/Text/34` | 0.562721 | **Upgrades** |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/0/SectionHeader/4` | 0.555622 | **INSTALL UPGRADE** |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/1/SectionHeader/3` | 0.549783 | ARMOR UPGRADES |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/0/SectionHeader/1` | 0.549783 | ARMOR UPGRADES |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/24` | 0.541015 | This armor upgrade supplements your armor's environmental  protections and filters out common contaminants, including  protection from most toxic atmospheres (*GM Core* 97). |

### Query 11
- Text: What is the rule about Environmental protections are crucial tools for explorers and  combatants alike, allowing any species to operate in hostile  conditions ill-suited for its survival. These items function as long  as the armor's environmental protections (page 244) are active  and can quickly recharge while a character is resting as other  functions in an armor enter sleep mode.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/13', 'PZO22001 Starfinder Player Core 268-281::/page/3/SectionHeader/5', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/24']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/13', 'PZO22001 Starfinder Player Core 268-281::/page/0/SectionHeader/14', 'PZO22001 Starfinder Player Core 268-281::/page/0/SectionHeader/12']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/0/SectionHeader/14` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/0/SectionHeader/12` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/13` | 1.005686 | Environmental protections are crucial tools for explorers and  combatants alike, allowing any species to operate in hostile  conditions ill-suited for its survival. These items function as long  as th |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/3/SectionHeader/5` | 0.596072 | **ENVIRONMENTAL PROTECTIONS** |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/24` | 0.557426 | This armor upgrade supplements your armor's environmental  protections and filters out common contaminants, including  protection from most toxic atmospheres (*GM Core* 97). |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/3/TableCell/760` | 0.506968 | Basic environmental protection |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/11` | 0.505183 | Some armor upgrades that have special activations and benefits  can be activated only a limited number of times per day, as  described in the armor upgrade. This limit is independent of any  costs for |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/46` | 0.497987 | This armor is specially treated with insulation to protect against  a specific type of damage. You gain resistance 5 to acid, cold,  electricity, or fire. The crafter chooses the damage type when  cre |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/9` | 0.494429 | Most upgrades grant their benefits continually so long as  you're properly wearing the armor they're installed in. Others  produce their effects only when used properly in the moment  by spending acti |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/19` | 0.490487 | This upgrade protects the user against the effects of space as  well as thick and thin atmospheres. This armor loses the exposed  trait for as long as the upgrade is installed. |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/49` | 0.485825 | This armor upgrade regulates heat, protecting you from extreme  temperatures. You're protected from mild cold and mild heat. |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/20` | 0.459032 | **Activate—Adapt** [reaction] **Frequency** once per 10 minutes; **Trigger** You  take acid, cold, electricity, or fire damage; **Effect** Your *energy * *shielding* upgrade changes to the triggering |

### Query 12
- Text: Summarize **BASIC ENVIRONMENTAL PROTECTION** **UPGRADE 0**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/0/SectionHeader/14']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/0/SectionHeader/14', 'PZO22001 Starfinder Player Core 268-281::/page/0/SectionHeader/12', 'PZO22001 Starfinder Player Core 268-281::/page/3/SectionHeader/5']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/0/SectionHeader/14', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/16', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/13']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/0/Text/16` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/0/Text/13` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/0/SectionHeader/14` | 1.018668 | **BASIC ENVIRONMENTAL PROTECTION** **UPGRADE 0** |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/0/SectionHeader/12` | 0.762214 | ENVIRONMENTAL  PROTECTION UPGRADES |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/3/SectionHeader/5` | 0.736407 | **ENVIRONMENTAL PROTECTIONS** |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/3/TableCell/760` | 0.645774 | Basic environmental protection |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/4/Text/28` | 0.547339 | **BIPOD** **UPGRADE 0+** |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/0/SectionHeader/4` | 0.502742 | **INSTALL UPGRADE** |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/1/SectionHeader/42` | 0.502175 | **ENERGY SHIELDING** **UPGRADE 8+** |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/9/Text/34` | 0.494031 | **Upgrades** |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/13/Text/50` | 0.494031 | **Upgrades** |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/24` | 0.490256 | This armor upgrade supplements your armor's environmental  protections and filters out common contaminants, including  protection from most toxic atmospheres (*GM Core* 97). |

### Query 13
- Text: Summarize **TECH**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/16']
- Expected found: `True`
- Expected rank: `11`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/1/Text/23', 'PZO22001 Starfinder Player Core 268-281::/page/1/Text/38', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/47']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/16', 'PZO22001 Starfinder Player Core 268-281::/page/0/SectionHeader/14', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/17']
- Expanded expected found: `True`
- Expanded expected rank: `11`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/0/SectionHeader/14` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/0/Text/17` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/23` | 0.917628 | **TECH** |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/38` | 0.917628 | **TECH** |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/47` | 0.917628 | **TECH** |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/65` | 0.875628 | **TECH** |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/53` | 0.875628 | **TECH** |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/52` | 0.875628 | **TECH** |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/6` | 0.875628 | **TECH** |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/61` | 0.875628 | **TECH** |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/35` | 0.875628 | **TECH** |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/6/Text/50` | 0.875628 | **TECH** |

### Query 14
- Text: Summarize **Price **10 credits
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/17']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/17', 'PZO22001 Starfinder Player Core 268-281::/page/13/Text/31', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/30']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/17', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/18', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/16']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/0/Text/18` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/0/Text/16` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/17` | 0.998706 | **Price **10 credits |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/13/Text/31` | 0.838120 | **Type **superior; **Level **10; **Price **10,110 credits |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/30` | 0.794870 | **Type **superior; **Level **10; **Price **24,100 credits |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/12/Text/23` | 0.750934 | **Type **commercial; **Level **0; **Price **10 credits |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/6/Text/37` | 0.750933 | **Type **commercial; **Level **0; **Price **10 credits |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/7/Text/23` | 0.743711 | **Type **advanced; **Level **10; **Price **8,200 credits |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/42` | 0.734451 | **Type **advanced; **Level **10; **Price **22,100 credits |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/34` | 0.699742 | **Type **tactical; **Level **10; **Price **10,000 credits |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/8/Text/4` | 0.692472 | **Price **100 credits |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/20` | 0.692472 | **Price **100 credits |

### Query 15
- Text: What is the rule about **Usage** installed in armor with the exposed trait; **Bulk **L?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/18']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/18', 'PZO22001 Starfinder Player Core 268-281::/page/1/Text/30', 'PZO22001 Starfinder Player Core 268-281::/page/1/SectionHeader/40']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/18', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/19', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/17']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/0/Text/19` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/0/Text/17` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/18` | 0.942870 | **Usage** installed in armor with the exposed trait; **Bulk **L |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/30` | 0.822059 | **Usage** installed in armor; **Bulk **L |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/1/SectionHeader/40` | 0.822059 | **Usage** installed in armor; **Bulk **L |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/45` | 0.780059 | **Usage** installed in armor; **Bulk **L |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/53` | 0.780059 | **Usage** installed in armor; **Bulk **L |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/21` | 0.780059 | **Usage** installed in armor; **Bulk **L |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/55` | 0.780059 | **Usage** installed in armor; **Bulk **L |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/27` | 0.780059 | **Usage** installed in armor; **Bulk **L |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/48` | 0.780059 | **Usage** installed in armor; **Bulk **L |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/66` | 0.780059 | **Usage** installed in armor; **Bulk **L |

### Query 16
- Text: What is the rule about This upgrade protects the user against the effects of space as  well as thick and thin atmospheres. This armor loses the exposed  trait for as long as the upgrade is installed.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/19']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/19', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/49', 'PZO22001 Starfinder Player Core 268-281::/page/1/Text/46']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/19', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/18', 'PZO22001 Starfinder Player Core 268-281::/page/0/SectionHeader/20']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/0/Text/18` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/0/SectionHeader/20` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/19` | 0.956177 | This upgrade protects the user against the effects of space as  well as thick and thin atmospheres. This armor loses the exposed  trait for as long as the upgrade is installed. |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/49` | 0.671678 | This armor upgrade regulates heat, protecting you from extreme  temperatures. You're protected from mild cold and mild heat. |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/46` | 0.646834 | This armor is specially treated with insulation to protect against  a specific type of damage. You gain resistance 5 to acid, cold,  electricity, or fire. The crafter chooses the damage type when  cre |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/24` | 0.589803 | This armor upgrade supplements your armor's environmental  protections and filters out common contaminants, including  protection from most toxic atmospheres (*GM Core* 97). |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/38` | 0.576376 | A layer of treated lead lines your armor with integrated radiation  sensors networked into your comm unit. While you're wearing  armor with this upgrade, you gain resistance 2 to poison damage  from r |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/9` | 0.551865 | Most upgrades grant their benefits continually so long as  you're properly wearing the armor they're installed in. Others  produce their effects only when used properly in the moment  by spending acti |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/18` | 0.547546 | **Usage** installed in armor with the exposed trait; **Bulk **L |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/11` | 0.542547 | Some armor upgrades that have special activations and benefits  can be activated only a limited number of times per day, as  described in the armor upgrade. This limit is independent of any  costs for |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/7/Text/39` | 0.534104 | **Armor ** **Upgrades** |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/3/Text/11` | 0.534104 | **Armor ** **Upgrades** |

### Query 17
- Text: Summarize **FILTERED REBREATHER** **UPGRADE 0+**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/0/SectionHeader/20']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/0/SectionHeader/20', 'PZO22001 Starfinder Player Core 268-281::/page/6/Text/34', 'PZO22001 Starfinder Player Core 268-281::/page/4/Text/28']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/0/SectionHeader/20', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/22', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/19']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/0/Text/22` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/0/Text/19` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/0/SectionHeader/20` | 1.023497 | **FILTERED REBREATHER** **UPGRADE 0+** |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/6/Text/34` | 0.621669 | **SILENCER** **UPGRADE 0+** |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/4/Text/28` | 0.604340 | **BIPOD** **UPGRADE 0+** |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/41` | 0.535016 | **LOAD LIFTER** **UPGRADE 2+** |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/60` | 0.504111 | **FORCE FIELD** **UPGRADE 1+** |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/9/Text/34` | 0.503740 | **Upgrades** |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/13/Text/50` | 0.503740 | **Upgrades** |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/0/SectionHeader/4` | 0.484673 | **INSTALL UPGRADE** |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/13/Text/51` | 0.483054 | **Weapon ** **Upgrades** |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/3/Text/12` | 0.483054 | **Weapon ** **Upgrades** |

### Query 18
- Text: Summarize **TECH**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/22']
- Expected found: `True`
- Expected rank: `23`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/1/Text/23', 'PZO22001 Starfinder Player Core 268-281::/page/1/Text/38', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/47']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/22', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/23', 'PZO22001 Starfinder Player Core 268-281::/page/0/SectionHeader/20']
- Expanded expected found: `True`
- Expanded expected rank: `23`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/0/Text/23` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/0/SectionHeader/20` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/23` | 0.917628 | **TECH** |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/38` | 0.917628 | **TECH** |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/47` | 0.917628 | **TECH** |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/65` | 0.875628 | **TECH** |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/53` | 0.875628 | **TECH** |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/52` | 0.875628 | **TECH** |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/6` | 0.875628 | **TECH** |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/61` | 0.875628 | **TECH** |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/35` | 0.875628 | **TECH** |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/6/Text/50` | 0.875628 | **TECH** |

### Query 19
- Text: Summarize **Usage** installed in armor; **Bulk **L
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/23']
- Expected found: `True`
- Expected rank: `11`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/1/Text/55', 'PZO22001 Starfinder Player Core 268-281::/page/1/Text/45', 'PZO22001 Starfinder Player Core 268-281::/page/1/Text/30']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/23', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/22', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/24']
- Expanded expected found: `True`
- Expanded expected rank: `11`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/0/Text/22` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/0/Text/24` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/55` | 1.025812 | **Usage** installed in armor; **Bulk **L |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/45` | 1.025812 | **Usage** installed in armor; **Bulk **L |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/30` | 1.025812 | **Usage** installed in armor; **Bulk **L |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/1/SectionHeader/40` | 0.983812 | **Usage** installed in armor; **Bulk **L |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/25` | 0.983812 | **Usage** installed in armor; **Bulk **L |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/53` | 0.983812 | **Usage** installed in armor; **Bulk **L |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/21` | 0.983812 | **Usage** installed in armor; **Bulk **L |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/27` | 0.983812 | **Usage** installed in armor; **Bulk **L |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/7` | 0.983812 | **Usage** installed in armor; **Bulk **L |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/43` | 0.983812 | **Usage** installed in armor; **Bulk **L |

### Query 20
- Text: Summarize This armor upgrade supplements your armor's environmental  protections and filters out common contaminants, including  protection from most toxic atmospheres (*GM Core* 97).
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/24']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/24', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/19', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/49']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/24', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/25', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/23']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/0/Text/25` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/0/Text/23` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/24` | 1.041638 | This armor upgrade supplements your armor's environmental  protections and filters out common contaminants, including  protection from most toxic atmospheres (*GM Core* 97). |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/19` | 0.717290 | This upgrade protects the user against the effects of space as  well as thick and thin atmospheres. This armor loses the exposed  trait for as long as the upgrade is installed. |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/49` | 0.662847 | This armor upgrade regulates heat, protecting you from extreme  temperatures. You're protected from mild cold and mild heat. |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/38` | 0.600457 | A layer of treated lead lines your armor with integrated radiation  sensors networked into your comm unit. While you're wearing  armor with this upgrade, you gain resistance 2 to poison damage  from r |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/13` | 0.590627 | Environmental protections are crucial tools for explorers and  combatants alike, allowing any species to operate in hostile  conditions ill-suited for its survival. These items function as long  as th |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/46` | 0.576522 | This armor is specially treated with insulation to protect against  a specific type of damage. You gain resistance 5 to acid, cold,  electricity, or fire. The crafter chooses the damage type when  cre |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/3/Text/11` | 0.560473 | **Armor ** **Upgrades** |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/5/Text/78` | 0.560473 | **Armor ** **Upgrades** |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/11/Text/50` | 0.560473 | **Armor ** **Upgrades** |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/77` | 0.560473 | **Armor ** **Upgrades** |

### Query 21
- Text: Summarize **Type **commercial; **Level **1; **Price **5 credits
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/25']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/25', 'PZO22001 Starfinder Player Core 268-281::/page/1/Text/9', 'PZO22001 Starfinder Player Core 268-281::/page/6/Text/53']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/25', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/26', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/24']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/0/Text/26` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/0/Text/24` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/25` | 1.035769 | **Type **commercial; **Level **1; **Price **5 credits |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/9` | 0.945902 | **Type **commercial; **Level **5; **Price **500 credits |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/6/Text/53` | 0.935325 | **Type **commercial; **Level **1; **Price **150 credits |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/5/Text/36` | 0.891560 | **Type **commercial; **Level **8; **Price **5,000 credits |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/5/Text/12` | 0.891560 | **Type **commercial; **Level **8; **Price **5,000 credits |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/5/Text/44` | 0.891560 | **Type **commercial; **Level **8; **Price **5,000 credits |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/6/Text/2` | 0.891560 | **Type **commercial; **Level **8; **Price **5,000 credits |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/6/Text/29` | 0.891560 | **Type **commercial; **Level **8; **Price **5,000 credits |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/33` | 0.891560 | **Type **commercial; **Level **8; **Price **5,000 credits |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/30` | 0.887206 | **Type **commercial; **Level **5; **Price **1,600 credits |

### Query 22
- Text: What is the rule about **Type **tactical; **Level **1; **Price **150 credits?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/26']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/26', 'PZO22001 Starfinder Player Core 268-281::/page/5/Text/3', 'PZO22001 Starfinder Player Core 268-281::/page/5/Text/13']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/26', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/25', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/27']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/0/Text/25` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/0/Text/27` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/26` | 0.891034 | **Type **tactical; **Level **1; **Price **150 credits |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/5/Text/3` | 0.822897 | **Type **tactical; **Level **1; **Price **100 credits |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/5/Text/13` | 0.777939 | **Type **tactical; **Level **15; **Price **65,000 credits |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/6/Text/30` | 0.735940 | **Type **tactical; **Level **15; **Price **65,000 credits |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/6/Text/3` | 0.735940 | **Type **tactical; **Level **15; **Price **65,000 credits |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/5/Text/37` | 0.735940 | **Type **tactical; **Level **15; **Price **65,000 credits |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/5/Text/45` | 0.735940 | **Type **tactical; **Level **15; **Price **65,000 credits |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/7/Text/21` | 0.725399 | **Type **tactical; **Level **2; **Price **250 credits |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/40` | 0.719249 | **Type **tactical; **Level **6; **Price **2,150 credits |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/13/Text/29` | 0.715453 | **Type **tactical; **Level **2; **Price **410 credits |

### Query 23
- Text: Summarize You gain a +1 status bonus to Fortitude saves against  inhaled effects.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/27']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/27', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/33', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/31']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/27', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/26', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/28']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/0/Text/26` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/0/Text/28` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/27` | 1.039994 | You gain a +1 status bonus to Fortitude saves against  inhaled effects. |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/33` | 0.633639 | The status bonus is +4. |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/31` | 0.630255 | The status bonus is +3. |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/29` | 0.584179 | The status bonus is +2. |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/38` | 0.520898 | A layer of treated lead lines your armor with integrated radiation  sensors networked into your comm unit. While you're wearing  armor with this upgrade, you gain resistance 2 to poison damage  from r |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/12/Text/22` | 0.500711 | A flash grenade unleashes a blast of bright light that requires  creatures in the radius to attempt a Fortitude save. |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/41` | 0.499189 | The resistance is 4, and the status bonus is +2. |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/43` | 0.496396 | The resistance is 8, and the status bonus is +3. |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/11` | 0.482755 | The item bonus is +2. |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/13` | 0.481546 | The item bonus is +3. |

### Query 24
- Text: Summarize **Type **advanced; **Level **6; **Price **2,550 credits
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/28']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/28', 'PZO22001 Starfinder Player Core 268-281::/page/2/Text/48', 'PZO22001 Starfinder Player Core 268-281::/page/7/Text/23']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/28', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/29', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/27']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/0/Text/29` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/0/Text/27` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/28` | 1.037397 | **Type **advanced; **Level **6; **Price **2,550 credits |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/48` | 0.954995 | **Type **advanced; **Level **6; **Price **2,100 credits |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/7/Text/23` | 0.837576 | **Type **advanced; **Level **10; **Price **8,200 credits |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/6/Text/56` | 0.790228 | **Type **advanced; **Level **9; **Price **8,000 credits |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/8/Text/49` | 0.789983 | **Type **advanced; **Level **12; **Price **18,900 credits |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/42` | 0.778468 | **Type **advanced; **Level **10; **Price **22,100 credits |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/59` | 0.775245 | **Type **advanced; **Level **11; **Price **13,400 credits |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/5/Text/5` | 0.765083 | **Type **advanced; **Level **2; **Price **450 credits |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/8/Text/21` | 0.759691 | **Type **advanced; **Level **19; **Price **310,650 credits |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/6/Text/46` | 0.754508 | **Type **tactical; **Level **6; **Price **2,600 credits |

### Query 25
- Text: Summarize The status bonus is +2.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/29']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/29', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/33', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/31']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/29', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/28', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/30']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/0/Text/28` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/0/Text/30` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/29` | 1.015867 | The status bonus is +2. |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/33` | 0.979966 | The status bonus is +4. |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/31` | 0.978739 | The status bonus is +3. |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/11` | 0.796848 | The item bonus is +2. |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/13` | 0.749226 | The item bonus is +3. |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/41` | 0.713665 | The resistance is 4, and the status bonus is +2. |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/43` | 0.705693 | The resistance is 8, and the status bonus is +3. |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/27` | 0.552694 | You gain a +1 status bonus to Fortitude saves against  inhaled effects. |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/44` | 0.547424 | **Type **superior; **Level **14; **Price **35,000 credits The resistance is 12, and the status bonus is +4. |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/7/Text/12` | 0.480340 | The item bonus is +2. When you activate See the Truth,  you see the truth of the world. The GM rolls a secret  counteract check with a +20 counteract modifier and  a counteract rank of 7 against any i |

### Query 26
- Text: Summarize **Type **superior; **Level **10; **Price **24,100 credits
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/30']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/30', 'PZO22001 Starfinder Player Core 268-281::/page/13/Text/31', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/42']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/30', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/31', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/29']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/0/Text/31` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/0/Text/29` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/30` | 1.037053 | **Type **superior; **Level **10; **Price **24,100 credits |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/13/Text/31` | 0.962683 | **Type **superior; **Level **10; **Price **10,110 credits |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/42` | 0.889536 | **Type **advanced; **Level **10; **Price **22,100 credits |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/7/Text/23` | 0.801165 | **Type **advanced; **Level **10; **Price **8,200 credits |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/61` | 0.781340 | **Type **superior; **Level **15; **Price **64,400 credits |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/8/Text/51` | 0.764743 | **Type **superior; **Level **15; **Price **61,400 credits |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/9` | 0.761903 | **Type **superior; **Level **10; **Price **10,000 credits; **Bulk **L |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/1` | 0.760140 | **Type **superior; **Level **14; **Price **37,800 credits |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/7/Text/25` | 0.742329 | **Type **superior; **Level **16; **Price **79,000 credits |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/12/Text/23` | 0.737121 | **Type **commercial; **Level **0; **Price **10 credits |

### Query 27
- Text: Summarize The status bonus is +3.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/31']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/31', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/33', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/29']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/31', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/30', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/32']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/0/Text/30` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/0/Text/32` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/31` | 1.020388 | The status bonus is +3. |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/33` | 0.994027 | The status bonus is +4. |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/29` | 0.985631 | The status bonus is +2. |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/13` | 0.805371 | The item bonus is +3. |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/11` | 0.774366 | The item bonus is +2. |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/43` | 0.712858 | The resistance is 8, and the status bonus is +3. |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/41` | 0.708680 | The resistance is 4, and the status bonus is +2. |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/44` | 0.553490 | **Type **superior; **Level **14; **Price **35,000 credits The resistance is 12, and the status bonus is +4. |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/27` | 0.552961 | You gain a +1 status bonus to Fortitude saves against  inhaled effects. |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/8/Text/31` | 0.512045 | **Type ***+3 weapon potency*; **Level **16; **Price **89,350 credits The item bonus to attack rolls is +3, and the weapon or flare  can benefit from three orbital crystals. |

### Query 28
- Text: Summarize **Type **elite; **Level **14; **Price **40,000 credits
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/32']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/32', 'PZO22001 Starfinder Player Core 268-281::/page/1/Text/1', 'PZO22001 Starfinder Player Core 268-281::/page/9/Text/2']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/32', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/33', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/31']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/0/Text/33` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/0/Text/31` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/32` | 1.038909 | **Type **elite; **Level **14; **Price **40,000 credits |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/1` | 0.831970 | **Type **superior; **Level **14; **Price **37,800 credits |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/9/Text/2` | 0.770993 | **Type **tactical; **Level **14; **Price **45,000 credits |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/9/Text/9` | 0.728993 | **Type **tactical; **Level **14; **Price **45,000 credits |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/61` | 0.712215 | **Type **superior; **Level **15; **Price **64,400 credits |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/12` | 0.710186 | **Type **advanced; **Level **17; **Price **140,000 credits |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/8/Text/51` | 0.691684 | **Type **superior; **Level **15; **Price **61,400 credits |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/11` | 0.686202 | **Type **elite; **Level **13; **Price **30,000 credits; **Bulk **1 |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/7/Text/25` | 0.682514 | **Type **superior; **Level **16; **Price **79,000 credits |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/5/Text/58` | 0.670506 | **Type **commercial; **Level **11; **Price **14,000 credits |

### Query 29
- Text: Summarize The status bonus is +4.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/33']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/33', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/31', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/29']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/33', 'PZO22001 Starfinder Player Core 268-281::/page/0/SectionHeader/34', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/32']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/0/SectionHeader/34` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/0/Text/32` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/33` | 1.017620 | The status bonus is +4. |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/31` | 0.993735 | The status bonus is +3. |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/29` | 0.986743 | The status bonus is +2. |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/11` | 0.773569 | The item bonus is +2. |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/13` | 0.772606 | The item bonus is +3. |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/41` | 0.736844 | The resistance is 4, and the status bonus is +2. |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/43` | 0.710249 | The resistance is 8, and the status bonus is +3. |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/44` | 0.557828 | **Type **superior; **Level **14; **Price **35,000 credits The resistance is 12, and the status bonus is +4. |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/27` | 0.557266 | You gain a +1 status bonus to Fortitude saves against  inhaled effects. |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/8/Text/31` | 0.483232 | **Type ***+3 weapon potency*; **Level **16; **Price **89,350 credits The item bonus to attack rolls is +3, and the weapon or flare  can benefit from three orbital crystals. |

### Query 30
- Text: Summarize **RADIATION BUFFER** **UPGRADE 1+**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/0/SectionHeader/34']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/0/SectionHeader/34', 'PZO22001 Starfinder Player Core 268-281::/page/3/TableCell/792', 'PZO22001 Starfinder Player Core 268-281::/page/3/TableCell/804']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/0/SectionHeader/34', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/33', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/36']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/0/Text/33` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/0/Text/36` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/0/SectionHeader/34` | 1.023144 | **RADIATION BUFFER** **UPGRADE 1+** |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/3/TableCell/792` | 0.702748 | Radiation buffer, advanced |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/3/TableCell/804` | 0.688341 | Radiation buffer, superior |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/3/TableCell/768` | 0.586082 | Radiation buffer, commercial |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/60` | 0.563184 | **FORCE FIELD** **UPGRADE 1+** |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/9/Text/34` | 0.537490 | **Upgrades** |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/13/Text/50` | 0.537490 | **Upgrades** |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/3/TableCell/780` | 0.534476 | Radiation buffer, tactical |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/1/SectionHeader/42` | 0.524714 | **ENERGY SHIELDING** **UPGRADE 8+** |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/6/SectionHeader/48` | 0.520804 | **SNIPER'S SCOPE** **UPGRADE 1+** |

### Query 31
- Text: Summarize **TECH**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/36']
- Expected found: `True`
- Expected rank: `20`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/1/Text/23', 'PZO22001 Starfinder Player Core 268-281::/page/1/Text/38', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/47']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/36', 'PZO22001 Starfinder Player Core 268-281::/page/0/SectionHeader/34', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/37']
- Expanded expected found: `True`
- Expanded expected rank: `20`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/0/SectionHeader/34` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/0/Text/37` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/23` | 0.917628 | **TECH** |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/38` | 0.917628 | **TECH** |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/47` | 0.917628 | **TECH** |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/65` | 0.875628 | **TECH** |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/53` | 0.875628 | **TECH** |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/52` | 0.875628 | **TECH** |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/6` | 0.875628 | **TECH** |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/61` | 0.875628 | **TECH** |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/35` | 0.875628 | **TECH** |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/6/Text/50` | 0.875628 | **TECH** |

### Query 32
- Text: Summarize **Usage** installed in armor; **Bulk **1
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/37']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/37', 'PZO22001 Starfinder Player Core 268-281::/page/2/Text/27', 'PZO22001 Starfinder Player Core 268-281::/page/1/Text/55']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/37', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/38', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/36']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/0/Text/38` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/0/Text/36` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/37` | 1.026567 | **Usage** installed in armor; **Bulk **1 |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/55` | 0.980967 | **Usage** installed in armor; **Bulk **L |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/27` | 0.980967 | **Usage** installed in armor; **Bulk **L |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/43` | 0.938967 | **Usage** installed in armor; **Bulk **L |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/37` | 0.938967 | **Usage** installed in armor; **Bulk **L |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/21` | 0.938967 | **Usage** installed in armor; **Bulk **L |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/66` | 0.938967 | **Usage** installed in armor; **Bulk **L |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/53` | 0.938967 | **Usage** installed in armor; **Bulk **L |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/1/SectionHeader/40` | 0.938967 | **Usage** installed in armor; **Bulk **L |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/48` | 0.938967 | **Usage** installed in armor; **Bulk **L |

### Query 33
- Text: What is the rule about A layer of treated lead lines your armor with integrated radiation  sensors networked into your comm unit. While you're wearing  armor with this upgrade, you gain resistance 2 to poison damage  from radiation effects and a +1 status bonus to Fortitude saves  against radiation.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/38']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/38', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/19', 'PZO22001 Starfinder Player Core 268-281::/page/1/Text/46']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/38', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/39', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/37']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/0/Text/39` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/0/Text/37` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/38` | 0.976840 | A layer of treated lead lines your armor with integrated radiation  sensors networked into your comm unit. While you're wearing  armor with this upgrade, you gain resistance 2 to poison damage  from r |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/19` | 0.618140 | This upgrade protects the user against the effects of space as  well as thick and thin atmospheres. This armor loses the exposed  trait for as long as the upgrade is installed. |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/46` | 0.605228 | This armor is specially treated with insulation to protect against  a specific type of damage. You gain resistance 5 to acid, cold,  electricity, or fire. The crafter chooses the damage type when  cre |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/24` | 0.512752 | This armor upgrade supplements your armor's environmental  protections and filters out common contaminants, including  protection from most toxic atmospheres (*GM Core* 97). |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/19` | 0.497695 | This device changes the chemical composition of the insulation  installed on your armor, reacting to different types of energy. |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/49` | 0.481978 | This armor upgrade regulates heat, protecting you from extreme  temperatures. You're protected from mild cold and mild heat. |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/27` | 0.480903 | You gain a +1 status bonus to Fortitude saves against  inhaled effects. |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/9` | 0.474404 | Most upgrades grant their benefits continually so long as  you're properly wearing the armor they're installed in. Others  produce their effects only when used properly in the moment  by spending acti |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/20` | 0.462943 | **Activate—Adapt** [reaction] **Frequency** once per 10 minutes; **Trigger** You  take acid, cold, electricity, or fire damage; **Effect** Your *energy * *shielding* upgrade changes to the triggering |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/3` | 0.462395 | You can personalize armor by purchasing and installing armor  upgrades. Armor upgrades are installed into the upgrade slots  of armor; one armor upgrade occupies one armor upgrade slot.  The number of |

### Query 34
- Text: Summarize **Type **commercial; **Level **1; **Price **130 credits
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/39']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/39', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/50', 'PZO22001 Starfinder Player Core 268-281::/page/6/Text/53']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/39', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/38', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/40']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/0/Text/38` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/0/Text/40` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/39` | 1.037180 | **Type **commercial; **Level **1; **Price **130 credits |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/50` | 0.954325 | **Type **commercial; **Level **1; **Price **120 credits |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/6/Text/53` | 0.951947 | **Type **commercial; **Level **1; **Price **150 credits |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/25` | 0.872470 | **Type **commercial; **Level **1; **Price **5 credits |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/13/Text/28` | 0.863362 | **Type **commercial; **Level **0; **Price **110 credits |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/5/Text/2` | 0.850207 | **Type **commercial; **Level **0; **Price **2 credits |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/45` | 0.831588 | **Type **commercial; **Level **2; **Price **550 credits |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/12/Text/23` | 0.830472 | **Type **commercial; **Level **0; **Price **10 credits |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/6/Text/37` | 0.830472 | **Type **commercial; **Level **0; **Price **10 credits |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/7/Text/19` | 0.830439 | **Type **commercial; **Level **0; **Price **50 credits |

### Query 35
- Text: What is the rule about **Type **tactical; **Level **6; **Price **2,150 credits?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/40']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/40', 'PZO22001 Starfinder Player Core 268-281::/page/6/Text/46', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/51']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/40', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/39', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/41']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/0/Text/39` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/0/Text/41` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/40` | 0.910825 | **Type **tactical; **Level **6; **Price **2,150 credits |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/6/Text/46` | 0.872709 | **Type **tactical; **Level **6; **Price **2,600 credits |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/51` | 0.848345 | **Type **tactical; **Level **6; **Price **1,800 credits |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/8/Text/47` | 0.773015 | **Type **tactical; **Level **9; **Price **6,600 credits |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/10` | 0.769016 | **Type **tactical; **Level **9; **Price **6,500 credits |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/5/Text/37` | 0.758469 | **Type **tactical; **Level **15; **Price **65,000 credits |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/5/Text/13` | 0.758469 | **Type **tactical; **Level **15; **Price **65,000 credits |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/6/Text/30` | 0.758469 | **Type **tactical; **Level **15; **Price **65,000 credits |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/6/Text/3` | 0.758469 | **Type **tactical; **Level **15; **Price **65,000 credits |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/5/Text/45` | 0.758469 | **Type **tactical; **Level **15; **Price **65,000 credits |

### Query 36
- Text: Summarize The resistance is 4, and the status bonus is +2.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/41']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/41', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/43', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/44']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/41', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/42', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/40']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/0/Text/42` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/0/Text/40` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/41` | 1.033006 | The resistance is 4, and the status bonus is +2. |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/43` | 0.967650 | The resistance is 8, and the status bonus is +3. |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/44` | 0.795498 | **Type **superior; **Level **14; **Price **35,000 credits The resistance is 12, and the status bonus is +4. |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/33` | 0.716933 | The status bonus is +4. |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/29` | 0.701684 | The status bonus is +2. |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/31` | 0.693845 | The status bonus is +3. |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/49` | 0.590725 | You gain resistance 10 to the specified damage type. |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/11` | 0.576973 | The item bonus is +2. |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/50` | 0.562246 | **Type **advanced; **Level **18; **Price **202,200 credits You gain resistance 15 to the specified damage type. |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/13` | 0.560321 | The item bonus is +3. |

### Query 37
- Text: Summarize **Type **advanced; **Level **10; **Price **22,100 credits
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/42']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/42', 'PZO22001 Starfinder Player Core 268-281::/page/7/Text/23', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/30']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/42', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/41', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/43']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/0/Text/41` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/0/Text/43` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/42` | 1.039158 | **Type **advanced; **Level **10; **Price **22,100 credits |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/7/Text/23` | 0.948585 | **Type **advanced; **Level **10; **Price **8,200 credits |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/30` | 0.897445 | **Type **superior; **Level **10; **Price **24,100 credits |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/13/Text/31` | 0.846300 | **Type **superior; **Level **10; **Price **10,110 credits |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/59` | 0.820568 | **Type **advanced; **Level **11; **Price **13,400 credits |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/48` | 0.814123 | **Type **advanced; **Level **6; **Price **2,100 credits |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/4/Text/25` | 0.810198 | **Type **advanced; **Level **20; **Price **700,000 credits |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/8/Text/49` | 0.804339 | **Type **advanced; **Level **12; **Price **18,900 credits |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/28` | 0.785361 | **Type **advanced; **Level **6; **Price **2,550 credits |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/8/Text/21` | 0.784676 | **Type **advanced; **Level **19; **Price **310,650 credits |

### Query 38
- Text: Summarize The resistance is 8, and the status bonus is +3.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/43']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/43', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/41', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/44']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/43', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/42', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/44']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/0/Text/42` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/0/Text/44` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/43` | 1.034572 | The resistance is 8, and the status bonus is +3. |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/41` | 0.964595 | The resistance is 4, and the status bonus is +2. |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/44` | 0.783325 | **Type **superior; **Level **14; **Price **35,000 credits The resistance is 12, and the status bonus is +4. |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/31` | 0.697548 | The status bonus is +3. |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/33` | 0.692124 | The status bonus is +4. |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/29` | 0.691306 | The status bonus is +2. |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/49` | 0.595749 | You gain resistance 10 to the specified damage type. |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/50` | 0.589635 | **Type **advanced; **Level **18; **Price **202,200 credits You gain resistance 15 to the specified damage type. |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/11` | 0.570702 | The item bonus is +2. |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/13` | 0.569071 | The item bonus is +3. |

### Query 39
- Text: Summarize **Type **superior; **Level **14; **Price **35,000 credits The resistance is 12, and the status bonus is +4.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/44']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/44', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/41', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/43']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/44', 'PZO22001 Starfinder Player Core 268-281::/page/0/SectionHeader/45', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/43']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/0/SectionHeader/45` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/0/Text/43` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/44` | 1.043581 | **Type **superior; **Level **14; **Price **35,000 credits The resistance is 12, and the status bonus is +4. |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/41` | 0.784440 | The resistance is 4, and the status bonus is +2. |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/43` | 0.772112 | The resistance is 8, and the status bonus is +3. |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/50` | 0.723259 | **Type **advanced; **Level **18; **Price **202,200 credits You gain resistance 15 to the specified damage type. |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/1` | 0.719055 | **Type **superior; **Level **14; **Price **37,800 credits |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/61` | 0.706100 | **Type **superior; **Level **15; **Price **64,400 credits |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/8/Text/51` | 0.693652 | **Type **superior; **Level **15; **Price **61,400 credits |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/7/Text/25` | 0.684500 | **Type **superior; **Level **16; **Price **79,000 credits |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/7/Text/2` | 0.678061 | **Type **superior; **Level **17; **Price **160,000 credits |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/32` | 0.651576 | **Type **elite; **Level **14; **Price **40,000 credits |

### Query 40
- Text: What is the rule about **THERMAL CAPACITOR** **UPGRADE 1+**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/0/SectionHeader/45']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/0/SectionHeader/45', 'PZO22001 Starfinder Player Core 268-281::/page/3/TableCell/796', 'PZO22001 Starfinder Player Core 268-281::/page/3/TableCell/808']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/0/SectionHeader/45', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/47', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/44']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/0/Text/47` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/0/Text/44` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/0/SectionHeader/45` | 0.936789 | **THERMAL CAPACITOR** **UPGRADE 1+** |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/3/TableCell/796` | 0.661026 | Thermal capacitor, advanced |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/3/TableCell/808` | 0.635928 | Thermal capacitor, superior |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/3/TableCell/772` | 0.559302 | Thermal capacitor, commercial |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/3/TableCell/784` | 0.555439 | Thermal capacitor, tactical |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/0/SectionHeader/34` | 0.468887 | **RADIATION BUFFER** **UPGRADE 1+** |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/60` | 0.460309 | **FORCE FIELD** **UPGRADE 1+** |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/2/SectionHeader/17` | 0.445142 | **GLAMER PROJECTOR** **UPGRADE 1** |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/3/SectionHeader/2` | 0.430729 | **ARMOR UPGRADES** |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/8/Text/1` | 0.428432 | **UNICLAMP** **UPGRADE 1** |

### Query 41
- Text: Summarize **TECH**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/47']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/1/Text/23', 'PZO22001 Starfinder Player Core 268-281::/page/1/Text/38', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/47']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/47', 'PZO22001 Starfinder Player Core 268-281::/page/0/SectionHeader/45', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/48']
- Expanded expected found: `True`
- Expanded expected rank: `3`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/0/SectionHeader/45` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/0/Text/48` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/23` | 0.917628 | **TECH** |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/38` | 0.917628 | **TECH** |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/47` | 0.917628 | **TECH** |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/65` | 0.875628 | **TECH** |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/53` | 0.875628 | **TECH** |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/52` | 0.875628 | **TECH** |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/6` | 0.875628 | **TECH** |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/61` | 0.875628 | **TECH** |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/35` | 0.875628 | **TECH** |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/6/Text/50` | 0.875628 | **TECH** |

### Query 42
- Text: Summarize **Usage** installed in armor; **Bulk **L
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/48']
- Expected found: `True`
- Expected rank: `14`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/1/Text/55', 'PZO22001 Starfinder Player Core 268-281::/page/1/Text/45', 'PZO22001 Starfinder Player Core 268-281::/page/1/Text/30']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/48', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/47', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/49']
- Expanded expected found: `True`
- Expanded expected rank: `14`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/0/Text/47` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/0/Text/49` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/55` | 1.025812 | **Usage** installed in armor; **Bulk **L |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/45` | 1.025812 | **Usage** installed in armor; **Bulk **L |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/30` | 1.025812 | **Usage** installed in armor; **Bulk **L |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/1/SectionHeader/40` | 0.983812 | **Usage** installed in armor; **Bulk **L |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/25` | 0.983812 | **Usage** installed in armor; **Bulk **L |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/53` | 0.983812 | **Usage** installed in armor; **Bulk **L |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/21` | 0.983812 | **Usage** installed in armor; **Bulk **L |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/27` | 0.983812 | **Usage** installed in armor; **Bulk **L |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/7` | 0.983812 | **Usage** installed in armor; **Bulk **L |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/43` | 0.983812 | **Usage** installed in armor; **Bulk **L |

### Query 43
- Text: Summarize This armor upgrade regulates heat, protecting you from extreme  temperatures. You're protected from mild cold and mild heat.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/49']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/49', 'PZO22001 Starfinder Player Core 268-281::/page/1/Text/2', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/19']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/49', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/50', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/48']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/0/Text/50` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/0/Text/48` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/49` | 1.040446 | This armor upgrade regulates heat, protecting you from extreme  temperatures. You're protected from mild cold and mild heat. |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/2` | 0.719432 | You're protected from incredible cold and incredible heat. |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/19` | 0.716591 | This upgrade protects the user against the effects of space as  well as thick and thin atmospheres. This armor loses the exposed  trait for as long as the upgrade is installed. |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/52` | 0.656112 | You're protected from severe cold and severe heat. |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/53` | 0.641353 | **Type **advanced; **Level **10; **Price **21,300 credits You're protected from extreme cold and extreme heat. |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/46` | 0.639232 | This armor is specially treated with insulation to protect against  a specific type of damage. You gain resistance 5 to acid, cold,  electricity, or fire. The crafter chooses the damage type when  cre |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/24` | 0.631438 | This armor upgrade supplements your armor's environmental  protections and filters out common contaminants, including  protection from most toxic atmospheres (*GM Core* 97). |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/3/Text/11` | 0.573371 | **Armor ** **Upgrades** |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/11/Text/50` | 0.573371 | **Armor ** **Upgrades** |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/7/Text/39` | 0.573371 | **Armor ** **Upgrades** |

### Query 44
- Text: Summarize **Type **commercial; **Level **1; **Price **120 credits
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/50']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/50', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/39', 'PZO22001 Starfinder Player Core 268-281::/page/6/Text/53']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/50', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/49', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/51']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/0/Text/49` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/0/Text/51` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/50` | 1.035900 | **Type **commercial; **Level **1; **Price **120 credits |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/39` | 0.956932 | **Type **commercial; **Level **1; **Price **130 credits |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/6/Text/53` | 0.938364 | **Type **commercial; **Level **1; **Price **150 credits |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/13/Text/28` | 0.880044 | **Type **commercial; **Level **0; **Price **110 credits |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/25` | 0.874166 | **Type **commercial; **Level **1; **Price **5 credits |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/4/Text/22` | 0.865936 | **Type **commercial; **Level **12; **Price **20,000 credits |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/5/Text/2` | 0.847339 | **Type **commercial; **Level **0; **Price **2 credits |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/5/Text/58` | 0.842022 | **Type **commercial; **Level **11; **Price **14,000 credits |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/30` | 0.831128 | **Type **commercial; **Level **5; **Price **1,600 credits |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/5/Text/20` | 0.831128 | **Type **commercial; **Level **5; **Price **1,600 credits |

### Query 45
- Text: What is the rule about **Type **tactical; **Level **6; **Price **1,800 credits?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/51']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/51', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/40', 'PZO22001 Starfinder Player Core 268-281::/page/6/Text/46']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/51', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/52', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/50']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/0/Text/52` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/0/Text/50` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/51` | 0.903533 | **Type **tactical; **Level **6; **Price **1,800 credits |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/40` | 0.843150 | **Type **tactical; **Level **6; **Price **2,150 credits |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/6/Text/46` | 0.841440 | **Type **tactical; **Level **6; **Price **2,600 credits |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/10` | 0.790756 | **Type **tactical; **Level **9; **Price **6,500 credits |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/8/Text/47` | 0.789733 | **Type **tactical; **Level **9; **Price **6,600 credits |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/6/Text/38` | 0.754832 | **Type **tactical; **Level **9; **Price **7,500 credits |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/48` | 0.754483 | **Type **tactical; **Level **12; **Price **16,200 credits |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/5/Text/59` | 0.754085 | **Type **tactical; **Level **16; **Price **80,000 credits |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/4/Text/23` | 0.738051 | **Type **tactical; **Level **16; **Price **80,950 credits |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/57` | 0.731616 | **Type **tactical; **Level **7; **Price **3,200 credits |

### Query 46
- Text: Summarize You're protected from severe cold and severe heat.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/52']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/52', 'PZO22001 Starfinder Player Core 268-281::/page/1/Text/2', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/53']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/52', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/53', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/51']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/0/Text/53` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/0/Text/51` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/52` | 1.025164 | You're protected from severe cold and severe heat. |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/2` | 0.906265 | You're protected from incredible cold and incredible heat. |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/53` | 0.686267 | **Type **advanced; **Level **10; **Price **21,300 credits You're protected from extreme cold and extreme heat. |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/49` | 0.641442 | This armor upgrade regulates heat, protecting you from extreme  temperatures. You're protected from mild cold and mild heat. |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/64` | 0.452863 | If your force field is tactical or better, it also protects you  from deadly blows. Each time you're critically hit while your |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/5/Text/43` | 0.426511 | This module siphons the heat from the weapon's striking edge  and ammunition, powering itself with the excess energy as it  chills the air around it. It deals an additional 1d6 cold damage.  On a crit |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/46` | 0.410169 | This armor is specially treated with insulation to protect against  a specific type of damage. You gain resistance 5 to acid, cold,  electricity, or fire. The crafter chooses the damage type when  cre |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/13` | 0.403688 | Environmental protections are crucial tools for explorers and  combatants alike, allowing any species to operate in hostile  conditions ill-suited for its survival. These items function as long  as th |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/13/Text/6` | 0.375587 | These grenades use an ignited chemical to explode in a  blast of intense heat and deal fire damage with a basic  Reflex save. If you have access to the critical specialization  effect of grenades, cre |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/5/Text/46` | 0.371800 | The save DC is 34. Cold damage dealt by this weapon ignores  the target's cold resistance. |

### Query 47
- Text: Summarize **Type **advanced; **Level **10; **Price **21,300 credits You're protected from extreme cold and extreme heat.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/53']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/53', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/42', 'PZO22001 Starfinder Player Core 268-281::/page/7/Text/23']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/0/Text/53', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/52', 'PZO22001 Starfinder Player Core 268-281::/page/1/SectionHeader/0']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/0/Text/52` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/1/SectionHeader/0` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/53` | 1.044248 | **Type **advanced; **Level **10; **Price **21,300 credits You're protected from extreme cold and extreme heat. |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/42` | 0.744995 | **Type **advanced; **Level **10; **Price **22,100 credits |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/7/Text/23` | 0.724619 | **Type **advanced; **Level **10; **Price **8,200 credits |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/2` | 0.678169 | You're protected from incredible cold and incredible heat. |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/52` | 0.662426 | You're protected from severe cold and severe heat. |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/4/Text/25` | 0.644282 | **Type **advanced; **Level **20; **Price **700,000 credits |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/49` | 0.641548 | This armor upgrade regulates heat, protecting you from extreme  temperatures. You're protected from mild cold and mild heat. |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/13/Text/31` | 0.637778 | **Type **superior; **Level **10; **Price **10,110 credits |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/30` | 0.630573 | **Type **superior; **Level **10; **Price **24,100 credits |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/59` | 0.621345 | **Type **advanced; **Level **11; **Price **13,400 credits |

### Query 48
- Text: Summarize 6 PLAYER CORE
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/1/SectionHeader/0']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/1/SectionHeader/0', 'PZO22001 Starfinder Player Core 268-281::/page/9/SectionHeader/0', 'PZO22001 Starfinder Player Core 268-281::/page/3/SectionHeader/0']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/1/SectionHeader/0', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/53', 'PZO22001 Starfinder Player Core 268-281::/page/1/Text/1']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/0/Text/53` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/1/Text/1` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/1/SectionHeader/0` | 0.992274 | 6 PLAYER CORE |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/9/SectionHeader/0` | 0.992274 | 6 PLAYER CORE |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/3/SectionHeader/0` | 0.992274 | 6 PLAYER CORE |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/9/TableCell/1037` | 0.480201 | 6 |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/9/TableCell/900` | 0.480201 | 6 |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/9/TableCell/1034` | 0.480201 | 6 |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/3/TableCell/785` | 0.480201 | 6 |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/3/TableCell/777` | 0.480201 | 6 |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/3/TableCell/781` | 0.480201 | 6 |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/3/TableCell/672` | 0.480201 | 6 |

### Query 49
- Text: Summarize **Type **superior; **Level **14; **Price **37,800 credits
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/1/Text/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/1/Text/1', 'PZO22001 Starfinder Player Core 268-281::/page/2/Text/61', 'PZO22001 Starfinder Player Core 268-281::/page/8/Text/51']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/1/Text/1', 'PZO22001 Starfinder Player Core 268-281::/page/1/SectionHeader/0', 'PZO22001 Starfinder Player Core 268-281::/page/1/Text/2']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/1/SectionHeader/0` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/1/Text/2` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/1` | 1.037195 | **Type **superior; **Level **14; **Price **37,800 credits |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/61` | 0.906399 | **Type **superior; **Level **15; **Price **64,400 credits |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/8/Text/51` | 0.897022 | **Type **superior; **Level **15; **Price **61,400 credits |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/7/Text/25` | 0.845865 | **Type **superior; **Level **16; **Price **79,000 credits |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/7/Text/2` | 0.813777 | **Type **superior; **Level **17; **Price **160,000 credits |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/32` | 0.790414 | **Type **elite; **Level **14; **Price **40,000 credits |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/12` | 0.768542 | **Type **advanced; **Level **17; **Price **140,000 credits |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/30` | 0.753152 | **Type **superior; **Level **10; **Price **24,100 credits |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/59` | 0.745927 | **Type **advanced; **Level **11; **Price **13,400 credits |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/8/Text/49` | 0.739456 | **Type **advanced; **Level **12; **Price **18,900 credits |

### Query 50
- Text: Summarize You're protected from incredible cold and incredible heat.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/1/Text/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/1/Text/2', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/52', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/53']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/1/Text/2', 'PZO22001 Starfinder Player Core 268-281::/page/1/SectionHeader/3', 'PZO22001 Starfinder Player Core 268-281::/page/1/Text/1']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/1/SectionHeader/3` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/1/Text/1` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/2` | 1.026383 | You're protected from incredible cold and incredible heat. |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/52` | 0.916121 | You're protected from severe cold and severe heat. |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/53` | 0.718822 | **Type **advanced; **Level **10; **Price **21,300 credits You're protected from extreme cold and extreme heat. |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/49` | 0.662017 | This armor upgrade regulates heat, protecting you from extreme  temperatures. You're protected from mild cold and mild heat. |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/5/Text/43` | 0.427692 | This module siphons the heat from the weapon's striking edge  and ammunition, powering itself with the excess energy as it  chills the air around it. It deals an additional 1d6 cold damage.  On a crit |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/64` | 0.420307 | If your force field is tactical or better, it also protects you  from deadly blows. Each time you're critically hit while your |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/46` | 0.419538 | This armor is specially treated with insulation to protect against  a specific type of damage. You gain resistance 5 to acid, cold,  electricity, or fire. The crafter chooses the damage type when  cre |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/13` | 0.405311 | Environmental protections are crucial tools for explorers and  combatants alike, allowing any species to operate in hostile  conditions ill-suited for its survival. These items function as long  as th |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/19` | 0.400999 | This upgrade protects the user against the effects of space as  well as thick and thin atmospheres. This armor loses the exposed  trait for as long as the upgrade is installed. |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/3/TableCell/743` | 0.371952 | Energy shielding, advanced |

### Query 51
- Text: Summarize ARMOR UPGRADES
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/1/SectionHeader/3']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/1/SectionHeader/3', 'PZO22001 Starfinder Player Core 268-281::/page/0/SectionHeader/1', 'PZO22001 Starfinder Player Core 268-281::/page/3/SectionHeader/2']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/1/SectionHeader/3', 'PZO22001 Starfinder Player Core 268-281::/page/1/SectionHeader/4', 'PZO22001 Starfinder Player Core 268-281::/page/1/Text/2']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/1/SectionHeader/4` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/1/Text/2` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/1/SectionHeader/3` | 0.984246 | ARMOR UPGRADES |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/0/SectionHeader/1` | 0.984246 | ARMOR UPGRADES |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/3/SectionHeader/2` | 0.949297 | **ARMOR UPGRADES** |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/0/SectionHeader/8` | 0.875564 | ACTIVATING ARMOR UPGRADES |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/0/SectionHeader/10` | 0.868654 | LIMITED ARMOR UPGRADES |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/5/Text/78` | 0.852911 | **Armor ** **Upgrades** |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/77` | 0.852910 | **Armor ** **Upgrades** |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/7/Text/39` | 0.852910 | **Armor ** **Upgrades** |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/3/Text/11` | 0.852910 | **Armor ** **Upgrades** |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/11/Text/50` | 0.852910 | **Armor ** **Upgrades** |

### Query 52
- Text: What is the rule about **ACTIVE CAMOUFLAGE** **UPGRADE 5+**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/1/SectionHeader/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/1/SectionHeader/4', 'PZO22001 Starfinder Player Core 268-281::/page/3/TableCell/739', 'PZO22001 Starfinder Player Core 268-281::/page/2/Text/25']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/1/SectionHeader/4', 'PZO22001 Starfinder Player Core 268-281::/page/1/SectionHeader/3', 'PZO22001 Starfinder Player Core 268-281::/page/1/Text/6']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/1/SectionHeader/3` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/1/Text/6` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/1/SectionHeader/4` | 0.917875 | **ACTIVE CAMOUFLAGE** **UPGRADE 5+** |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/3/TableCell/739` | 0.586012 | Active camouflage, advanced |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/25` | 0.552291 | **JETPACK** **UPGRADE 5+** |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/5/SectionHeader/15` | 0.476854 | **FEAR PROJECTOR** **UPGRADE 5+** |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/3/TableCell/663` | 0.470898 | Active camouflage, commercial |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/3/TableCell/695` | 0.470231 | Active camouflage, tactical |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/4/SectionHeader/12` | 0.459464 | **ANIMATED INTELLIGENCE** **UPGRADE 12+** |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/2/SectionHeader/63` | 0.446171 | **MOBILITY ENHANCER** **UPGRADE 3+** |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/5/SectionHeader/31` | 0.443521 | **FLAMING MODULE** **UPGRADE 8+** |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/9` | 0.440728 | Most upgrades grant their benefits continually so long as  you're properly wearing the armor they're installed in. Others  produce their effects only when used properly in the moment  by spending acti |

### Query 53
- Text: Summarize **TECH**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/1/Text/6']
- Expected found: `True`
- Expected rank: `7`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/1/Text/23', 'PZO22001 Starfinder Player Core 268-281::/page/1/Text/38', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/47']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/1/Text/6', 'PZO22001 Starfinder Player Core 268-281::/page/1/SectionHeader/4', 'PZO22001 Starfinder Player Core 268-281::/page/1/Text/7']
- Expanded expected found: `True`
- Expanded expected rank: `7`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/1/SectionHeader/4` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/1/Text/7` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/23` | 0.917628 | **TECH** |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/38` | 0.917628 | **TECH** |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/47` | 0.917628 | **TECH** |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/65` | 0.875628 | **TECH** |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/53` | 0.875628 | **TECH** |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/52` | 0.875628 | **TECH** |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/6` | 0.875628 | **TECH** |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/61` | 0.875628 | **TECH** |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/35` | 0.875628 | **TECH** |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/6/Text/50` | 0.875628 | **TECH** |

### Query 54
- Text: Summarize **Usage** installed in armor; **Bulk **L
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/1/Text/7']
- Expected found: `True`
- Expected rank: `9`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/1/Text/55', 'PZO22001 Starfinder Player Core 268-281::/page/1/Text/45', 'PZO22001 Starfinder Player Core 268-281::/page/1/Text/30']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/1/Text/7', 'PZO22001 Starfinder Player Core 268-281::/page/1/Text/8', 'PZO22001 Starfinder Player Core 268-281::/page/1/Text/6']
- Expanded expected found: `True`
- Expanded expected rank: `9`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/1/Text/8` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/1/Text/6` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/55` | 1.025812 | **Usage** installed in armor; **Bulk **L |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/45` | 1.025812 | **Usage** installed in armor; **Bulk **L |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/30` | 1.025812 | **Usage** installed in armor; **Bulk **L |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/1/SectionHeader/40` | 0.983812 | **Usage** installed in armor; **Bulk **L |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/25` | 0.983812 | **Usage** installed in armor; **Bulk **L |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/53` | 0.983812 | **Usage** installed in armor; **Bulk **L |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/21` | 0.983812 | **Usage** installed in armor; **Bulk **L |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/27` | 0.983812 | **Usage** installed in armor; **Bulk **L |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/7` | 0.983812 | **Usage** installed in armor; **Bulk **L |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/43` | 0.983812 | **Usage** installed in armor; **Bulk **L |

### Query 55
- Text: What is the rule about Hardlight projectors shift the appearance of your armor  using shifting colors and patterns that respond to your  environment. You gain a +1 item bonus to Stealth checks  while wearing the armor.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/1/Text/8']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/1/Text/8', 'PZO22001 Starfinder Player Core 268-281::/page/2/Text/23', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/19']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/1/Text/8', 'PZO22001 Starfinder Player Core 268-281::/page/1/Text/7', 'PZO22001 Starfinder Player Core 268-281::/page/1/Text/9']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/1/Text/7` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/1/Text/9` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/8` | 0.974938 | Hardlight projectors shift the appearance of your armor  using shifting colors and patterns that respond to your  environment. You gain a +1 item bonus to Stealth checks  while wearing the armor. |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/23` | 0.598857 | **Activate—Glamerize!** [one-action] (manipulate) **Effect** You instantly  change the appearance of your armor to any set of normal  clothes or any other type of light or heavy armor. This  upgrade i |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/19` | 0.542319 | This upgrade protects the user against the effects of space as  well as thick and thin atmospheres. This armor loses the exposed  trait for as long as the upgrade is installed. |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/22` | 0.511329 | Adjustable rings project magical holograms onto your armor,  changing its appearance to match your personal style and  suit any occasion. *Glamer projectors* come programmed with  preset options, incl |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/3` | 0.488212 | You can personalize armor by purchasing and installing armor  upgrades. Armor upgrades are installed into the upgrade slots  of armor; one armor upgrade occupies one armor upgrade slot.  The number of |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/19` | 0.478999 | This device changes the chemical composition of the insulation  installed on your armor, reacting to different types of energy. |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/9` | 0.472074 | Most upgrades grant their benefits continually so long as  you're properly wearing the armor they're installed in. Others  produce their effects only when used properly in the moment  by spending acti |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/6/Text/55` | 0.468144 | The scope grants you a +1 item bonus to visual Perception  checks to Seek creatures through the scope. |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/7/Text/12` | 0.456871 | The item bonus is +2. When you activate See the Truth,  you see the truth of the world. The GM rolls a secret  counteract check with a +20 counteract modifier and  a counteract rank of 7 against any i |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/49` | 0.452691 | This armor upgrade regulates heat, protecting you from extreme  temperatures. You're protected from mild cold and mild heat. |

### Query 56
- Text: Summarize **Type **commercial; **Level **5; **Price **500 credits
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/1/Text/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/1/Text/9', 'PZO22001 Starfinder Player Core 268-281::/page/1/Text/33', 'PZO22001 Starfinder Player Core 268-281::/page/5/Text/44']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/1/Text/9', 'PZO22001 Starfinder Player Core 268-281::/page/1/Text/8', 'PZO22001 Starfinder Player Core 268-281::/page/1/Text/10']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/1/Text/8` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/1/Text/10` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/9` | 1.038287 | **Type **commercial; **Level **5; **Price **500 credits |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/33` | 0.962687 | **Type **commercial; **Level **8; **Price **5,000 credits |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/5/Text/44` | 0.962687 | **Type **commercial; **Level **8; **Price **5,000 credits |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/6/Text/29` | 0.920687 | **Type **commercial; **Level **8; **Price **5,000 credits |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/5/Text/36` | 0.920687 | **Type **commercial; **Level **8; **Price **5,000 credits |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/6/Text/2` | 0.920687 | **Type **commercial; **Level **8; **Price **5,000 credits |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/5/Text/12` | 0.920687 | **Type **commercial; **Level **8; **Price **5,000 credits |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/25` | 0.901838 | **Type **commercial; **Level **1; **Price **5 credits |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/5/Text/20` | 0.878578 | **Type **commercial; **Level **5; **Price **1,600 credits |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/30` | 0.878578 | **Type **commercial; **Level **5; **Price **1,600 credits |

### Query 57
- Text: What is the rule about **Type **tactical; **Level **9; **Price **6,500 credits?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/1/Text/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/1/Text/10', 'PZO22001 Starfinder Player Core 268-281::/page/8/Text/47', 'PZO22001 Starfinder Player Core 268-281::/page/6/Text/38']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/1/Text/10', 'PZO22001 Starfinder Player Core 268-281::/page/1/Text/11', 'PZO22001 Starfinder Player Core 268-281::/page/1/Text/9']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/1/Text/11` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/1/Text/9` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/10` | 0.903623 | **Type **tactical; **Level **9; **Price **6,500 credits |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/8/Text/47` | 0.875151 | **Type **tactical; **Level **9; **Price **6,600 credits |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/6/Text/38` | 0.862393 | **Type **tactical; **Level **9; **Price **7,500 credits |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/51` | 0.780654 | **Type **tactical; **Level **6; **Price **1,800 credits |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/40` | 0.755931 | **Type **tactical; **Level **6; **Price **2,150 credits |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/6/Text/46` | 0.745899 | **Type **tactical; **Level **6; **Price **2,600 credits |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/48` | 0.739263 | **Type **tactical; **Level **12; **Price **16,200 credits |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/5/Text/59` | 0.722050 | **Type **tactical; **Level **16; **Price **80,000 credits |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/6/Text/3` | 0.721356 | **Type **tactical; **Level **15; **Price **65,000 credits |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/5/Text/37` | 0.721356 | **Type **tactical; **Level **15; **Price **65,000 credits |

### Query 58
- Text: Summarize The item bonus is +2.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/1/Text/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/1/Text/11', 'PZO22001 Starfinder Player Core 268-281::/page/1/Text/13', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/29']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/1/Text/11', 'PZO22001 Starfinder Player Core 268-281::/page/1/Text/10', 'PZO22001 Starfinder Player Core 268-281::/page/1/Text/12']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/1/Text/10` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/1/Text/12` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/11` | 1.011007 | The item bonus is +2. |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/13` | 0.963888 | The item bonus is +3. |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/29` | 0.834715 | The status bonus is +2. |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/31` | 0.772140 | The status bonus is +3. |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/33` | 0.769724 | The status bonus is +4. |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/41` | 0.575632 | The resistance is 4, and the status bonus is +2. |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/43` | 0.574785 | The resistance is 8, and the status bonus is +3. |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/8/Text/31` | 0.550276 | **Type ***+3 weapon potency*; **Level **16; **Price **89,350 credits The item bonus to attack rolls is +3, and the weapon or flare  can benefit from three orbital crystals. |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/8/Text/30` | 0.526623 | The item bonus to attack rolls is +2, and the weapon or flare  can benefit from two orbital crystals. |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/6/Text/55` | 0.504708 | The scope grants you a +1 item bonus to visual Perception  checks to Seek creatures through the scope. |

### Query 59
- Text: Summarize **Type **advanced; **Level **17; **Price **140,000 credits
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/1/Text/12']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/1/Text/12', 'PZO22001 Starfinder Player Core 268-281::/page/7/Text/2', 'PZO22001 Starfinder Player Core 268-281::/page/7/Text/25']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/1/Text/12', 'PZO22001 Starfinder Player Core 268-281::/page/1/Text/13', 'PZO22001 Starfinder Player Core 268-281::/page/1/Text/11']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/1/Text/13` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/1/Text/11` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/12` | 1.039668 | **Type **advanced; **Level **17; **Price **140,000 credits |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/7/Text/2` | 0.922086 | **Type **superior; **Level **17; **Price **160,000 credits |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/7/Text/25` | 0.875791 | **Type **superior; **Level **16; **Price **79,000 credits |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/4/Text/25` | 0.804282 | **Type **advanced; **Level **20; **Price **700,000 credits |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/8/Text/49` | 0.801132 | **Type **advanced; **Level **12; **Price **18,900 credits |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/59` | 0.798573 | **Type **advanced; **Level **11; **Price **13,400 credits |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/6/Text/56` | 0.775742 | **Type **advanced; **Level **9; **Price **8,000 credits |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/1` | 0.768001 | **Type **superior; **Level **14; **Price **37,800 credits |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/8/Text/21` | 0.758267 | **Type **advanced; **Level **19; **Price **310,650 credits |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/42` | 0.754601 | **Type **advanced; **Level **10; **Price **22,100 credits |

### Query 60
- Text: Summarize The item bonus is +3.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/1/Text/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/1/Text/13', 'PZO22001 Starfinder Player Core 268-281::/page/1/Text/11', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/31']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/1/Text/13', 'PZO22001 Starfinder Player Core 268-281::/page/1/Text/12', 'PZO22001 Starfinder Player Core 268-281::/page/1/SectionHeader/14']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/1/Text/12` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/1/SectionHeader/14` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/13` | 1.013999 | The item bonus is +3. |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/11` | 0.966477 | The item bonus is +2. |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/31` | 0.848916 | The status bonus is +3. |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/33` | 0.772217 | The status bonus is +4. |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/29` | 0.746543 | The status bonus is +2. |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/8/Text/31` | 0.589907 | **Type ***+3 weapon potency*; **Level **16; **Price **89,350 credits The item bonus to attack rolls is +3, and the weapon or flare  can benefit from three orbital crystals. |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/43` | 0.569137 | The resistance is 8, and the status bonus is +3. |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/41` | 0.558088 | The resistance is 4, and the status bonus is +2. |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/8/Text/30` | 0.524488 | The item bonus to attack rolls is +2, and the weapon or flare  can benefit from two orbital crystals. |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/9/TableCell/1021` | 0.524444 | +3 weapon potency |

### Query 61
- Text: Summarize **ADAPTIVE ENERGY SHIELDING** **UPGRADE 13**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/1/SectionHeader/14']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/1/SectionHeader/14', 'PZO22001 Starfinder Player Core 268-281::/page/1/SectionHeader/42', 'PZO22001 Starfinder Player Core 268-281::/page/3/TableCell/723']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/1/SectionHeader/14', 'PZO22001 Starfinder Player Core 268-281::/page/1/Text/13', 'PZO22001 Starfinder Player Core 268-281::/page/1/Text/16']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/1/Text/13` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/1/Text/16` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/1/SectionHeader/14` | 1.031598 | **ADAPTIVE ENERGY SHIELDING** **UPGRADE 13** |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/1/SectionHeader/42` | 0.735425 | **ENERGY SHIELDING** **UPGRADE 8+** |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/3/TableCell/723` | 0.722378 | Adaptive energy shielding |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/3/TableCell/743` | 0.644888 | Energy shielding, advanced |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/20` | 0.616228 | **Activate—Adapt** [reaction] **Frequency** once per 10 minutes; **Trigger** You  take acid, cold, electricity, or fire damage; **Effect** Your *energy * *shielding* upgrade changes to the triggering |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/4/SectionHeader/12` | 0.523154 | **ANIMATED INTELLIGENCE** **UPGRADE 12+** |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/0/SectionHeader/12` | 0.522736 | ENVIRONMENTAL  PROTECTION UPGRADES |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/46` | 0.508380 | This armor is specially treated with insulation to protect against  a specific type of damage. You gain resistance 5 to acid, cold,  electricity, or fire. The crafter chooses the damage type when  cre |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/18` | 0.505512 | **Usage** installed in armor with the energy shielding upgrade;  **Bulk **L |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/9/SectionHeader/17` | 0.497955 | **WEAPON UPGRADES** |

### Query 62
- Text: Summarize **MAGICAL** **TECH**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/1/Text/16']
- Expected found: `True`
- Expected rank: `7`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/1/Text/44', 'PZO22001 Starfinder Player Core 268-281::/page/2/Text/19', 'PZO22001 Starfinder Player Core 268-281::/page/7/Text/6']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/1/Text/16', 'PZO22001 Starfinder Player Core 268-281::/page/1/Text/17', 'PZO22001 Starfinder Player Core 268-281::/page/1/SectionHeader/14']
- Expanded expected found: `True`
- Expanded expected rank: `7`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/1/Text/17` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/1/SectionHeader/14` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/44` | 0.985621 | **MAGICAL** **TECH** |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/19` | 0.985621 | **MAGICAL** **TECH** |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/7/Text/6` | 0.985621 | **MAGICAL** **TECH** |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/5/Text/49` | 0.943621 | **MAGICAL** **TECH** |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/29` | 0.943621 | **MAGICAL** **TECH** |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/6/Text/7` | 0.943621 | **MAGICAL** **TECH** |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/16` | 0.943621 | **MAGICAL** **TECH** |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/6/Text/26` | 0.840401 | **ELECTRICITY** **MAGICAL** **TECH** |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/4/Text/14` | 0.820084 | **UNCOMMON** **MAGICAL** **TECH** |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/6/Text/14` | 0.820084 | **UNCOMMON** **MAGICAL** **TECH** |

### Query 63
- Text: Summarize **Price **22,500 credits
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/1/Text/17']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/1/Text/17', 'PZO22001 Starfinder Player Core 268-281::/page/1/Text/54', 'PZO22001 Starfinder Player Core 268-281::/page/8/Text/37']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/1/Text/17', 'PZO22001 Starfinder Player Core 268-281::/page/1/Text/18', 'PZO22001 Starfinder Player Core 268-281::/page/1/Text/16']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/1/Text/18` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/1/Text/16` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/17` | 1.017205 | **Price **22,500 credits |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/54` | 0.732395 | **Price **4,200 credits |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/8/Text/37` | 0.731698 | **Price **2,000 credits |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/24` | 0.688230 | **Price **200 credits |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/42` | 0.671991 | **Type **advanced; **Level **10; **Price **22,100 credits |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/61` | 0.630342 | **Type **superior; **Level **15; **Price **64,400 credits |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/1` | 0.629639 | **Type **superior; **Level **14; **Price **37,800 credits |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/6/Text/21` | 0.629175 | **Price **550 credits |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/36` | 0.629175 | **Price **550 credits |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/8/Text/51` | 0.623085 | **Type **superior; **Level **15; **Price **61,400 credits |

### Query 64
- Text: Summarize **Usage** installed in armor with the energy shielding upgrade;  **Bulk **L
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/1/Text/18']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/1/Text/18', 'PZO22001 Starfinder Player Core 268-281::/page/1/SectionHeader/40', 'PZO22001 Starfinder Player Core 268-281::/page/1/Text/45']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/1/Text/18', 'PZO22001 Starfinder Player Core 268-281::/page/1/Text/17', 'PZO22001 Starfinder Player Core 268-281::/page/1/Text/19']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/1/Text/17` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/1/Text/19` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/18` | 1.036197 | **Usage** installed in armor with the energy shielding upgrade;  **Bulk **L |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/1/SectionHeader/40` | 0.882121 | **Usage** installed in armor; **Bulk **L |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/45` | 0.882121 | **Usage** installed in armor; **Bulk **L |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/25` | 0.840121 | **Usage** installed in armor; **Bulk **L |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/30` | 0.840121 | **Usage** installed in armor; **Bulk **L |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/53` | 0.840121 | **Usage** installed in armor; **Bulk **L |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/66` | 0.840121 | **Usage** installed in armor; **Bulk **L |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/27` | 0.840121 | **Usage** installed in armor; **Bulk **L |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/21` | 0.840121 | **Usage** installed in armor; **Bulk **L |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/55` | 0.840121 | **Usage** installed in armor; **Bulk **L |

### Query 65
- Text: What is the rule about This device changes the chemical composition of the insulation  installed on your armor, reacting to different types of energy.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/1/Text/19']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/1/Text/19', 'PZO22001 Starfinder Player Core 268-281::/page/1/Text/46', 'PZO22001 Starfinder Player Core 268-281::/page/1/Text/20']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/1/Text/19', 'PZO22001 Starfinder Player Core 268-281::/page/1/Text/18', 'PZO22001 Starfinder Player Core 268-281::/page/1/Text/20']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/1/Text/18` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/1/Text/20` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/19` | 0.950918 | This device changes the chemical composition of the insulation  installed on your armor, reacting to different types of energy. |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/46` | 0.691107 | This armor is specially treated with insulation to protect against  a specific type of damage. You gain resistance 5 to acid, cold,  electricity, or fire. The crafter chooses the damage type when  cre |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/20` | 0.621828 | **Activate—Adapt** [reaction] **Frequency** once per 10 minutes; **Trigger** You  take acid, cold, electricity, or fire damage; **Effect** Your *energy * *shielding* upgrade changes to the triggering |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/19` | 0.537114 | This upgrade protects the user against the effects of space as  well as thick and thin atmospheres. This armor loses the exposed  trait for as long as the upgrade is installed. |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/3` | 0.529515 | You can personalize armor by purchasing and installing armor  upgrades. Armor upgrades are installed into the upgrade slots  of armor; one armor upgrade occupies one armor upgrade slot.  The number of |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/38` | 0.514646 | A layer of treated lead lines your armor with integrated radiation  sensors networked into your comm unit. While you're wearing  armor with this upgrade, you gain resistance 2 to poison damage  from r |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/18` | 0.503739 | **Usage** installed in armor with the energy shielding upgrade;  **Bulk **L |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/49` | 0.498683 | This armor upgrade regulates heat, protecting you from extreme  temperatures. You're protected from mild cold and mild heat. |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/23` | 0.486501 | **Activate—Glamerize!** [one-action] (manipulate) **Effect** You instantly  change the appearance of your armor to any set of normal  clothes or any other type of light or heavy armor. This  upgrade i |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/3/Text/9` | 0.484776 | **Tech Gear** **Armor** |

### Query 66
- Text: What is the rule about **Activate—Adapt** [reaction] **Frequency** once per 10 minutes; **Trigger** You  take acid, cold, electricity, or fire damage; **Effect** Your *energy * *shielding* upgrade changes to the triggering damage type.  This lasts until you Adapt again or uninstall any *adaptive * *energy shielding *or *energy shielding* upgrade from the same  armor. If you have multiple *energy shielding* upgrades on this  armor, choose one to change when you Adapt.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/1/Text/20']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/1/Text/20', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/9', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/11']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/1/Text/20', 'PZO22001 Starfinder Player Core 268-281::/page/1/Text/19', 'PZO22001 Starfinder Player Core 268-281::/page/1/SectionHeader/21']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/1/Text/19` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/1/SectionHeader/21` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/20` | 0.968699 | **Activate—Adapt** [reaction] **Frequency** once per 10 minutes; **Trigger** You  take acid, cold, electricity, or fire damage; **Effect** Your *energy * *shielding* upgrade changes to the triggering |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/9` | 0.659436 | Most upgrades grant their benefits continually so long as  you're properly wearing the armor they're installed in. Others  produce their effects only when used properly in the moment  by spending acti |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/11` | 0.656701 | Some armor upgrades that have special activations and benefits  can be activated only a limited number of times per day, as  described in the armor upgrade. This limit is independent of any  costs for |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/46` | 0.600933 | This armor is specially treated with insulation to protect against  a specific type of damage. You gain resistance 5 to acid, cold,  electricity, or fire. The crafter chooses the damage type when  cre |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/4/Text/5` | 0.593921 | Most upgrades grant their benefits continually so long as  you're wielding the weapon they're installed in. Others  produce their effects only when used properly in the moment  by spending actions. An |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/4/Text/7` | 0.579597 | Some weapon upgrades that have special activations and  abilities can be activated only a limited number of times  per day, as described in the weapon upgrade. This limit is  independent of any costs |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/8/Text/40` | 0.577944 | **Activate—Halt Cycle **[free-action] (concentrate) **Frequency** once per 10  minutes; **Trigger** You critically hit with your solar weapon  or solar flare as part of an action with the cycle trait; |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/57` | 0.561905 | **Activate—Store Grenade** [two-actions] (manipulate) **Effect** You place a  grenade inside a reinforced compartment in the explosive  defense unit. You can Interact to retrieve the grenade  normally |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/19` | 0.555655 | This device changes the chemical composition of the insulation  installed on your armor, reacting to different types of energy. |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/63` | 0.553425 | Force fields absorb damage. A force field's Hit Points are based  on its version. While your force field is active, any physical or  energy damage you would take is applied to the force field's Hit  P |

### Query 67
- Text: Summarize **AUTO-CPR UNIT** **UPGRADE 2**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/1/SectionHeader/21']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/1/SectionHeader/21', 'PZO22001 Starfinder Player Core 268-281::/page/3/TableCell/635', 'PZO22001 Starfinder Player Core 268-281::/page/2/SectionHeader/50']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/1/SectionHeader/21', 'PZO22001 Starfinder Player Core 268-281::/page/1/Text/20', 'PZO22001 Starfinder Player Core 268-281::/page/1/Text/23']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/1/Text/20` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/1/Text/23` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/1/SectionHeader/21` | 1.024648 | **AUTO-CPR UNIT** **UPGRADE 2** |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/3/TableCell/635` | 0.726146 | Auto-CPR unit |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/2/SectionHeader/50` | 0.548950 | **MANEUVERING UNIT** **UPGRADE 4+** |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/13/Text/50` | 0.501441 | **Upgrades** |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/9/Text/34` | 0.501441 | **Upgrades** |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/9/SectionHeader/17` | 0.477386 | **WEAPON UPGRADES** |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/13/Text/51` | 0.476955 | **Weapon ** **Upgrades** |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/9/Text/35` | 0.476955 | **Weapon ** **Upgrades** |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/3/Text/12` | 0.476955 | **Weapon ** **Upgrades** |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/5/Text/79` | 0.476955 | **Weapon ** **Upgrades** |

### Query 68
- Text: Summarize **TECH**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/1/Text/23']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/1/Text/23', 'PZO22001 Starfinder Player Core 268-281::/page/1/Text/38', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/47']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/1/Text/23', 'PZO22001 Starfinder Player Core 268-281::/page/1/Text/24', 'PZO22001 Starfinder Player Core 268-281::/page/1/SectionHeader/21']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/1/Text/24` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/1/SectionHeader/21` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/23` | 0.917628 | **TECH** |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/38` | 0.917628 | **TECH** |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/47` | 0.917628 | **TECH** |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/65` | 0.875628 | **TECH** |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/53` | 0.875628 | **TECH** |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/52` | 0.875628 | **TECH** |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/6` | 0.875628 | **TECH** |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/61` | 0.875628 | **TECH** |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/35` | 0.875628 | **TECH** |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/6/Text/50` | 0.875628 | **TECH** |

### Query 69
- Text: What is the rule about This device monitors your vital signs and automatically  administers aid. When you have the dying condition while  wearing this armor, the DC of your recovery checks is equal to 8  + your dying value (instead of 10 + your dying value).?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/1/Text/26']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/1/Text/26', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/9', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/11']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/1/Text/26', 'PZO22001 Starfinder Player Core 268-281::/page/1/Text/25', 'PZO22001 Starfinder Player Core 268-281::/page/1/SectionHeader/27']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/1/Text/25` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/1/SectionHeader/27` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/26` | 0.970465 | This device monitors your vital signs and automatically  administers aid. When you have the dying condition while  wearing this armor, the DC of your recovery checks is equal to 8  + your dying value |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/9` | 0.513677 | Most upgrades grant their benefits continually so long as  you're properly wearing the armor they're installed in. Others  produce their effects only when used properly in the moment  by spending acti |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/11` | 0.505204 | Some armor upgrades that have special activations and benefits  can be activated only a limited number of times per day, as  described in the armor upgrade. This limit is independent of any  costs for |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/38` | 0.436789 | A layer of treated lead lines your armor with integrated radiation  sensors networked into your comm unit. While you're wearing  armor with this upgrade, you gain resistance 2 to poison damage  from r |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/8` | 0.430097 | The force field has 20 Hit Points and replenishes 4 Hit Points  on your turn, and the flat check DC is 19. |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/6` | 0.428144 | The force field has 14 Hit Points and replenishes 3 Hit Points on  your turn, and the flat check DC is 20. |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/10` | 0.427840 | The force field has 26 Hit Points and replenishes 5 Hit Points  on your turn, and the flat check DC is 18. |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/4/Text/21` | 0.426775 | Each round, when the weapon finishes using its actions,  attempt a DC 6 flat check. On a failure, the activation ends.  The weapon falls to the ground and can't Autoattack again  for 10 minutes. |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/16` | 0.424424 | The force field has 42 Hit Points and replenishes 8 Hit Points  on your turn, and the flat check DC is 15. |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/12` | 0.424028 | The force field has 32 Hit Points and replenishes 6 Hit Points  on your turn, and the flat check DC is 17. |

### Query 70
- Text: What is the rule about **Activate—Bend Light **[one-action] (manipulate) **Frequency** once per day;  **Effect** You become invisible for 1 minute, gaining the effects  of a 2nd-rank *invisibility* spell.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/1/Text/32']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/1/Text/32', 'PZO22001 Starfinder Player Core 268-281::/page/7/Text/9', 'PZO22001 Starfinder Player Core 268-281::/page/2/Text/2']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/1/Text/32', 'PZO22001 Starfinder Player Core 268-281::/page/1/Text/31', 'PZO22001 Starfinder Player Core 268-281::/page/1/Text/33']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/1/Text/31` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/1/Text/33` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/32` | 0.986094 | **Activate—Bend Light **[one-action] (manipulate) **Frequency** once per day;  **Effect** You become invisible for 1 minute, gaining the effects  of a 2nd-rank *invisibility* spell. |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/7/Text/9` | 0.698072 | **Activate—See the Truth**[two-actions] (manipulate) **Frequency** once per  day; **Effect** For the next 10 minutes, while looking through  the scope, you can see invisible creatures as though they |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/2` | 0.644022 | **Activate—Raise Force Field** [one-action] (manipulate) **Frequency** three  times per day; **Effect** Your force field becomes active. It  remains active for 1 minute or until it's reduced to 0 Hit |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/29` | 0.538160 | **Activate—Fly** [one-action] (manipulate) **Effect** You activate a jetpack to  gain a fly Speed of 20 feet. This effect lasts for 1 minute or  until you Dismiss it. You can use an action to Fly 0 fe |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/39` | 0.519575 | **Activate—Jump** [one-action] (manipulate) **Frequency** once per round;  **Effect** You activate the jump jets to get a quick boost. You  Fly up to 20 feet with a maximum height of 10 feet, or  you |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/20` | 0.502859 | **Activate—Adapt** [reaction] **Frequency** once per 10 minutes; **Trigger** You  take acid, cold, electricity, or fire damage; **Effect** Your *energy * *shielding* upgrade changes to the triggering |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/55` | 0.496342 | **Activate—Thrust** [one-action] (move) **Requirements** You're in a zero-g  environment; **Effect** You move 5 feet in any direction you  choose. You begin to float in that direction. |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/8/Text/40` | 0.489642 | **Activate—Halt Cycle **[free-action] (concentrate) **Frequency** once per 10  minutes; **Trigger** You critically hit with your solar weapon  or solar flare as part of an action with the cycle trait; |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/23` | 0.487968 | **Activate—Glamerize!** [one-action] (manipulate) **Effect** You instantly  change the appearance of your armor to any set of normal  clothes or any other type of light or heavy armor. This  upgrade i |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/57` | 0.473832 | **Activate—Store Grenade** [two-actions] (manipulate) **Effect** You place a  grenade inside a reinforced compartment in the explosive  defense unit. You can Interact to retrieve the grenade  normally |

### Query 71
- Text: What is the rule about **Type **tactical; **Level **10; **Price **10,000 credits?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/1/Text/34']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/1/Text/34', 'PZO22001 Starfinder Player Core 268-281::/page/8/Text/19', 'PZO22001 Starfinder Player Core 268-281::/page/5/Text/3']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/1/Text/34', 'PZO22001 Starfinder Player Core 268-281::/page/1/Text/35', 'PZO22001 Starfinder Player Core 268-281::/page/1/Text/33']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/1/Text/35` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/1/Text/33` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/34` | 0.906694 | **Type **tactical; **Level **10; **Price **10,000 credits |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/8/Text/19` | 0.761075 | **Type **tactical; **Level **12; **Price **10,650 credits |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/5/Text/3` | 0.740633 | **Type **tactical; **Level **1; **Price **100 credits |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/10` | 0.691362 | **Type **tactical; **Level **9; **Price **6,500 credits |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/8/Text/47` | 0.684753 | **Type **tactical; **Level **9; **Price **6,600 credits |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/6/Text/38` | 0.680988 | **Type **tactical; **Level **9; **Price **7,500 credits |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/13/Text/29` | 0.675924 | **Type **tactical; **Level **2; **Price **410 credits |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/3/Text/1` | 0.675592 | **Type **tactical; **Level **10; **Price **11,000 credits The reduction to your armor's penalty to Speeds is 10 feet. |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/48` | 0.674483 | **Type **tactical; **Level **12; **Price **16,200 credits |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/13/Text/31` | 0.674351 | **Type **superior; **Level **10; **Price **10,110 credits |

### Query 72
- Text: What is the rule about This armor is specially treated with insulation to protect against  a specific type of damage. You gain resistance 5 to acid, cold,  electricity, or fire. The crafter chooses the damage type when  creating the upgrade. Multiple *energy shielding* upgrades can be  placed into a suit of armor, but each must provide resistance to  a different damage type.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/1/Text/46']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/1/Text/46', 'PZO22001 Starfinder Player Core 268-281::/page/1/Text/19', 'PZO22001 Starfinder Player Core 268-281::/page/1/Text/20']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/1/Text/46', 'PZO22001 Starfinder Player Core 268-281::/page/1/Text/45', 'PZO22001 Starfinder Player Core 268-281::/page/1/Text/47']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/1/Text/45` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/1/Text/47` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/46` | 0.966064 | This armor is specially treated with insulation to protect against  a specific type of damage. You gain resistance 5 to acid, cold,  electricity, or fire. The crafter chooses the damage type when  cre |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/19` | 0.681280 | This device changes the chemical composition of the insulation  installed on your armor, reacting to different types of energy. |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/20` | 0.680244 | **Activate—Adapt** [reaction] **Frequency** once per 10 minutes; **Trigger** You  take acid, cold, electricity, or fire damage; **Effect** Your *energy * *shielding* upgrade changes to the triggering |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/19` | 0.595144 | This upgrade protects the user against the effects of space as  well as thick and thin atmospheres. This armor loses the exposed  trait for as long as the upgrade is installed. |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/49` | 0.586509 | This armor upgrade regulates heat, protecting you from extreme  temperatures. You're protected from mild cold and mild heat. |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/18` | 0.570071 | **Usage** installed in armor with the energy shielding upgrade;  **Bulk **L |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/3` | 0.562330 | You can personalize armor by purchasing and installing armor  upgrades. Armor upgrades are installed into the upgrade slots  of armor; one armor upgrade occupies one armor upgrade slot.  The number of |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/49` | 0.552437 | You gain resistance 10 to the specified damage type. |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/38` | 0.535574 | A layer of treated lead lines your armor with integrated radiation  sensors networked into your comm unit. While you're wearing  armor with this upgrade, you gain resistance 2 to poison damage  from r |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/13` | 0.530542 | Environmental protections are crucial tools for explorers and  combatants alike, allowing any species to operate in hostile  conditions ill-suited for its survival. These items function as long  as th |

### Query 73
- Text: What is the rule about **Type **tactical; **Level **12; **Price **16,200 credits?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/1/Text/48']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/1/Text/48', 'PZO22001 Starfinder Player Core 268-281::/page/5/Text/21', 'PZO22001 Starfinder Player Core 268-281::/page/8/Text/19']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/1/Text/48', 'PZO22001 Starfinder Player Core 268-281::/page/1/Text/49', 'PZO22001 Starfinder Player Core 268-281::/page/1/Text/47']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/1/Text/49` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/1/Text/47` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/48` | 0.898354 | **Type **tactical; **Level **12; **Price **16,200 credits |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/5/Text/21` | 0.837830 | **Type **tactical; **Level **12; **Price **20,000 credits |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/8/Text/19` | 0.817632 | **Type **tactical; **Level **12; **Price **10,650 credits |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/5/Text/59` | 0.771591 | **Type **tactical; **Level **16; **Price **80,000 credits |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/4/Text/23` | 0.747061 | **Type **tactical; **Level **16; **Price **80,950 credits |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/5/Text/45` | 0.739364 | **Type **tactical; **Level **15; **Price **65,000 credits |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/5/Text/13` | 0.739364 | **Type **tactical; **Level **15; **Price **65,000 credits |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/6/Text/3` | 0.739364 | **Type **tactical; **Level **15; **Price **65,000 credits |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/6/Text/30` | 0.739364 | **Type **tactical; **Level **15; **Price **65,000 credits |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/5/Text/37` | 0.739364 | **Type **tactical; **Level **15; **Price **65,000 credits |

### Query 74
- Text: What is the rule about You gain resistance 10 to the specified damage type.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/1/Text/49']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/1/Text/49', 'PZO22001 Starfinder Player Core 268-281::/page/1/Text/50', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/43']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/1/Text/49', 'PZO22001 Starfinder Player Core 268-281::/page/1/Text/48', 'PZO22001 Starfinder Player Core 268-281::/page/1/Text/50']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/1/Text/48` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/1/Text/50` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/49` | 0.908328 | You gain resistance 10 to the specified damage type. |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/50` | 0.667563 | **Type **advanced; **Level **18; **Price **202,200 credits You gain resistance 15 to the specified damage type. |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/43` | 0.559187 | The resistance is 8, and the status bonus is +3. |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/5/Text/38` | 0.508443 | Increase the persistent damage on a critical hit to 2d10. Fire  damage dealt by this weapon (including the persistent fire  damage) ignores the target's fire resistance. |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/41` | 0.497424 | The resistance is 4, and the status bonus is +2. |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/46` | 0.491449 | This armor is specially treated with insulation to protect against  a specific type of damage. You gain resistance 5 to acid, cold,  electricity, or fire. The crafter chooses the damage type when  cre |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/3/Text/1` | 0.489692 | **Type **tactical; **Level **10; **Price **11,000 credits The reduction to your armor's penalty to Speeds is 10 feet. |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/34` | 0.483527 | **Type **tactical; **Level **10; **Price **10,000 credits |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/44` | 0.474282 | **Type **superior; **Level **14; **Price **35,000 credits The resistance is 12, and the status bonus is +4. |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/6/Text/32` | 0.457045 | 2d10 (including the damage dealt to two other creatures).  Electricity damage dealt by this weapon ignores the  target's electricity resistance (and the other creatures' on  a critical hit). |

### Query 75
- Text: What is the rule about **Type **advanced; **Level **18; **Price **202,200 credits You gain resistance 15 to the specified damage type.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/1/Text/50']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/1/Text/50', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/44', 'PZO22001 Starfinder Player Core 268-281::/page/1/Text/12']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/1/Text/50', 'PZO22001 Starfinder Player Core 268-281::/page/1/Text/49', 'PZO22001 Starfinder Player Core 268-281::/page/1/SectionHeader/51']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/1/Text/49` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/1/SectionHeader/51` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/50` | 0.940803 | **Type **advanced; **Level **18; **Price **202,200 credits You gain resistance 15 to the specified damage type. |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/44` | 0.709034 | **Type **superior; **Level **14; **Price **35,000 credits The resistance is 12, and the status bonus is +4. |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/12` | 0.688986 | **Type **advanced; **Level **17; **Price **140,000 credits |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/49` | 0.645889 | You gain resistance 10 to the specified damage type. |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/8/Text/49` | 0.635513 | **Type **advanced; **Level **12; **Price **18,900 credits |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/8/Text/21` | 0.617686 | **Type **advanced; **Level **19; **Price **310,650 credits |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/4/Text/25` | 0.616257 | **Type **advanced; **Level **20; **Price **700,000 credits |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/7/Text/23` | 0.616093 | **Type **advanced; **Level **10; **Price **8,200 credits |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/42` | 0.615734 | **Type **advanced; **Level **10; **Price **22,100 credits |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/6/Text/56` | 0.606236 | **Type **advanced; **Level **9; **Price **8,000 credits |

### Query 76
- Text: What is the rule about Reinforced custom armor plates automatically generate a  containment field to protect you from nearby explosions,  granting you resistance 2 to area damage (acid, cold,  electricity, and fire damage only). You can also store a  grenade in the explosive defense unit and detonate it without  harming yourself.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/1/Text/56']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/1/Text/56', 'PZO22001 Starfinder Player Core 268-281::/page/1/Text/58', 'PZO22001 Starfinder Player Core 268-281::/page/1/Text/57']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/1/Text/56', 'PZO22001 Starfinder Player Core 268-281::/page/1/Text/55', 'PZO22001 Starfinder Player Core 268-281::/page/1/Text/57']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/1/Text/55` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/1/Text/57` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/56` | 0.948164 | Reinforced custom armor plates automatically generate a  containment field to protect you from nearby explosions,  granting you resistance 2 to area damage (acid, cold,  electricity, and fire damage o |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/58` | 0.664306 | **Activate—Defensive Detonation **[one-action] (manipulate) **Requirements** You have a stored grenade; **Effect** You detonate the grenade  stored in the explosive defense unit. The explosion is cent |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/57` | 0.633270 | **Activate—Store Grenade** [two-actions] (manipulate) **Effect** You place a  grenade inside a reinforced compartment in the explosive  defense unit. You can Interact to retrieve the grenade  normally |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/46` | 0.510690 | This armor is specially treated with insulation to protect against  a specific type of damage. You gain resistance 5 to acid, cold,  electricity, or fire. The crafter chooses the damage type when  cre |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/12/Text/3` | 0.503295 | An item with the grenade trait can be thrown with a range of 70  feet using the Area Fire action (page 410) as though it had the  area (burst) trait at the listed radius using a single action instead |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/13/Text/6` | 0.501474 | These grenades use an ignited chemical to explode in a  blast of intense heat and deal fire damage with a basic  Reflex save. If you have access to the critical specialization  effect of grenades, cre |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/12/Text/11` | 0.483304 | These grenades discharge a shocking field that deals electricity  damage with a basic Reflex save. If you have access to the  critical specialization effect of grenades, tech creatures and  unattended |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/5/Text/29` | 0.469796 | **Activate—Fireburst Mode** [one-action] (manipulate) **Effect** The grenade  launcher or the undermounted grenade launcher gains  the area (cone) trait with a range of 15 feet and uses the |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/13/TableCell/875` | 0.461216 | Incendiary grenade, tactical |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/12/Text/42` | 0.453567 | These fragmentary grenades explode in a cloud of shrapnel  and deal piercing damage in a burst with a basic Reflex  save. |

### Query 77
- Text: What is the rule about **Activate—Store Grenade** [two-actions] (manipulate) **Effect** You place a  grenade inside a reinforced compartment in the explosive  defense unit. You can Interact to retrieve the grenade  normally. You can store only one grenade in the armor  upgrade at a time.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/1/Text/57']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/1/Text/57', 'PZO22001 Starfinder Player Core 268-281::/page/1/Text/58', 'PZO22001 Starfinder Player Core 268-281::/page/7/Text/18']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/1/Text/57', 'PZO22001 Starfinder Player Core 268-281::/page/1/Text/56', 'PZO22001 Starfinder Player Core 268-281::/page/1/Text/58']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/1/Text/56` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/1/Text/58` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/57` | 0.978893 | **Activate—Store Grenade** [two-actions] (manipulate) **Effect** You place a  grenade inside a reinforced compartment in the explosive  defense unit. You can Interact to retrieve the grenade  normally |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/58` | 0.820404 | **Activate—Defensive Detonation **[one-action] (manipulate) **Requirements** You have a stored grenade; **Effect** You detonate the grenade  stored in the explosive defense unit. The explosion is cent |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/7/Text/18` | 0.695468 | **Activate—Launch** [one-action] (attack) **Effect** You launch the loaded  grenade. |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/9` | 0.610967 | Most upgrades grant their benefits continually so long as  you're properly wearing the armor they're installed in. Others  produce their effects only when used properly in the moment  by spending acti |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/4/Text/5` | 0.600270 | Most upgrades grant their benefits continually so long as  you're wielding the weapon they're installed in. Others  produce their effects only when used properly in the moment  by spending actions. An |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/5/Text/29` | 0.597059 | **Activate—Fireburst Mode** [one-action] (manipulate) **Effect** The grenade  launcher or the undermounted grenade launcher gains  the area (cone) trait with a range of 15 feet and uses the |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/12/Text/3` | 0.564017 | An item with the grenade trait can be thrown with a range of 70  feet using the Area Fire action (page 410) as though it had the  area (burst) trait at the listed radius using a single action instead |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/2` | 0.545861 | **Activate—Raise Force Field** [one-action] (manipulate) **Frequency** three  times per day; **Effect** Your force field becomes active. It  remains active for 1 minute or until it's reduced to 0 Hit |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/4/Text/9` | 0.542518 | Some upgrades attach to or upgrade a specific part of a  weapon. A weapon can only have one such upgrade at a time.  These will always be designated in the upgrade's usage entry,  such as "installed i |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/11` | 0.537947 | Some armor upgrades that have special activations and benefits  can be activated only a limited number of times per day, as  described in the armor upgrade. This limit is independent of any  costs for |

### Query 78
- Text: What is the rule about **Activate—Defensive Detonation **[one-action] (manipulate) **Requirements** You have a stored grenade; **Effect** You detonate the grenade  stored in the explosive defense unit. The explosion is centered  on your space, but the upgrade generates a containment  field to protect you from its effects. The grenade otherwise  functions as if you'd activated it normally.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/1/Text/58']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/1/Text/58', 'PZO22001 Starfinder Player Core 268-281::/page/1/Text/57', 'PZO22001 Starfinder Player Core 268-281::/page/7/Text/18']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/1/Text/58', 'PZO22001 Starfinder Player Core 268-281::/page/1/Text/60', 'PZO22001 Starfinder Player Core 268-281::/page/1/Text/57']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/1/Text/60` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/1/Text/57` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/58` | 0.975745 | **Activate—Defensive Detonation **[one-action] (manipulate) **Requirements** You have a stored grenade; **Effect** You detonate the grenade  stored in the explosive defense unit. The explosion is cent |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/57` | 0.834591 | **Activate—Store Grenade** [two-actions] (manipulate) **Effect** You place a  grenade inside a reinforced compartment in the explosive  defense unit. You can Interact to retrieve the grenade  normally |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/7/Text/18` | 0.696655 | **Activate—Launch** [one-action] (attack) **Effect** You launch the loaded  grenade. |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/5/Text/29` | 0.606482 | **Activate—Fireburst Mode** [one-action] (manipulate) **Effect** The grenade  launcher or the undermounted grenade launcher gains  the area (cone) trait with a range of 15 feet and uses the |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/2` | 0.564305 | **Activate—Raise Force Field** [one-action] (manipulate) **Frequency** three  times per day; **Effect** Your force field becomes active. It  remains active for 1 minute or until it's reduced to 0 Hit |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/56` | 0.558699 | Reinforced custom armor plates automatically generate a  containment field to protect you from nearby explosions,  granting you resistance 2 to area damage (acid, cold,  electricity, and fire damage o |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/4/Text/5` | 0.555264 | Most upgrades grant their benefits continually so long as  you're wielding the weapon they're installed in. Others  produce their effects only when used properly in the moment  by spending actions. An |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/9` | 0.542624 | Most upgrades grant their benefits continually so long as  you're properly wearing the armor they're installed in. Others  produce their effects only when used properly in the moment  by spending acti |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/12/Text/3` | 0.539725 | An item with the grenade trait can be thrown with a range of 70  feet using the Area Fire action (page 410) as though it had the  area (burst) trait at the listed radius using a single action instead |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/29` | 0.534361 | **Activate—Fly** [one-action] (manipulate) **Effect** You activate a jetpack to  gain a fly Speed of 20 feet. This effect lasts for 1 minute or  until you Dismiss it. You can use an action to Fly 0 fe |

### Query 79
- Text: What is the rule about Force fields absorb damage. A force field's Hit Points are based  on its version. While your force field is active, any physical or  energy damage you would take is applied to the force field's Hit  Points first before being applied to your Hit Points (including  temporary Hit Points). If you have a shield raised, your force  field and shield both take damage. If damage from an attack or  effect reduces the force field to 0 Hit Points, you take any excess  damage, the force field deactivates, and it can't be activated  again for 10 minutes. Force fields replenish the indicated number  of Hit Points each round at the beginning of your turn while  they're active.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/1/Text/63']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/1/Text/63', 'PZO22001 Starfinder Player Core 268-281::/page/2/Text/4', 'PZO22001 Starfinder Player Core 268-281::/page/2/Text/2']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/1/Text/63', 'PZO22001 Starfinder Player Core 268-281::/page/1/Text/62', 'PZO22001 Starfinder Player Core 268-281::/page/1/Text/64']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/1/Text/62` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/1/Text/64` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/63` | 0.993051 | Force fields absorb damage. A force field's Hit Points are based  on its version. While your force field is active, any physical or  energy damage you would take is applied to the force field's Hit  P |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/4` | 0.689485 | The force field has 6 Hit Points and replenishes 2 Hit Points  on your turn. |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/2` | 0.680423 | **Activate—Raise Force Field** [one-action] (manipulate) **Frequency** three  times per day; **Effect** Your force field becomes active. It  remains active for 1 minute or until it's reduced to 0 Hit |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/64` | 0.569072 | If your force field is tactical or better, it also protects you  from deadly blows. Each time you're critically hit while your |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/6` | 0.540797 | The force field has 14 Hit Points and replenishes 3 Hit Points on  your turn, and the flat check DC is 20. |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/10` | 0.540431 | The force field has 26 Hit Points and replenishes 5 Hit Points  on your turn, and the flat check DC is 18. |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/8` | 0.539943 | The force field has 20 Hit Points and replenishes 4 Hit Points  on your turn, and the flat check DC is 19. |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/16` | 0.537235 | The force field has 42 Hit Points and replenishes 8 Hit Points  on your turn, and the flat check DC is 15. |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/14` | 0.535718 | The force field has 37 Hit Points and replenishes 7 Hit Points on  your turn, and the flat check DC is 16. |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/12` | 0.534318 | The force field has 32 Hit Points and replenishes 6 Hit Points  on your turn, and the flat check DC is 17. |

### Query 80
- Text: What is the rule about If your force field is tactical or better, it also protects you  from deadly blows. Each time you're critically hit while your?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/1/Text/64']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/1/Text/64', 'PZO22001 Starfinder Player Core 268-281::/page/1/Text/63', 'PZO22001 Starfinder Player Core 268-281::/page/3/TableCell/651']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/1/Text/64', 'PZO22001 Starfinder Player Core 268-281::/page/1/Text/66', 'PZO22001 Starfinder Player Core 268-281::/page/1/Text/63']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/1/Text/66` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/1/Text/63` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/64` | 0.962652 | If your force field is tactical or better, it also protects you  from deadly blows. Each time you're critically hit while your |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/63` | 0.614759 | Force fields absorb damage. A force field's Hit Points are based  on its version. While your force field is active, any physical or  energy damage you would take is applied to the force field's Hit  P |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/3/TableCell/651` | 0.596960 | Force field, tactical |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/4` | 0.476631 | The force field has 6 Hit Points and replenishes 2 Hit Points  on your turn. |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/5/Text/22` | 0.448331 | When you critically hit with this weapon, the target becomes  frightened 2. |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/3/TableCell/719` | 0.440222 | Energy shielding, tactical |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/9/TableCell/1018` | 0.431716 | Striking, tactical |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/6/Text/11` | 0.431239 | On a critical hit, a *merciful* weapon causes the target to  become fascinated with the weapon's wielder for 1 minute, as  the target is bombarded with feelings of guilt and remorse.  This is a mental |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/2` | 0.424327 | **Activate—Raise Force Field** [one-action] (manipulate) **Frequency** three  times per day; **Effect** Your force field becomes active. It  remains active for 1 minute or until it's reduced to 0 Hit |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/8/Text/57` | 0.423155 | A *graviton* *crystal* increases the forces of gravity around your  solar manifestations, accelerating its impact and possibly  trapping foes within its gravity field. While graviton attuned,  your so |

### Query 81
- Text: What is the rule about **ANCESTRIES & ** **BACKGROUNDS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/1/Text/67']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/1/Text/67', 'PZO22001 Starfinder Player Core 268-281::/page/7/Text/29', 'PZO22001 Starfinder Player Core 268-281::/page/5/Text/68']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/1/Text/67', 'PZO22001 Starfinder Player Core 268-281::/page/1/Text/68', 'PZO22001 Starfinder Player Core 268-281::/page/11/Text/40', 'PZO22001 Starfinder Player Core 268-281::/page/5/Text/68', 'PZO22001 Starfinder Player Core 268-281::/page/13/Text/39', 'PZO22001 Starfinder Player Core 268-281::/page/1/Text/66', 'PZO22001 Starfinder Player Core 268-281::/page/9/Text/25', 'PZO22001 Starfinder Player Core 268-281::/page/7/Text/29']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/1/Text/68` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/11/Text/40` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/5/Text/68` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/13/Text/39` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/1/Text/66` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/9/Text/25` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/7/Text/29` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/67` | 0.920820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/7/Text/29` | 0.920820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/5/Text/68` | 0.920820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/9/Text/25` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/11/Text/40` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/13/Text/39` | 0.672250 | **ANCESTRIES & ** |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/13/Text/40` | 0.527382 | **BACKGROUNDS** **CLASSES** |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/11/Text/58` | 0.343180 | **CONDITIONS ** **APPENDIX** |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/5/Text/86` | 0.343180 | **CONDITIONS ** **APPENDIX** |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/13/Text/58` | 0.343180 | **CONDITIONS ** **APPENDIX** |

### Query 82
- Text: What is the rule about **SKILLS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/1/Text/69']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/13/Text/41', 'PZO22001 Starfinder Player Core 268-281::/page/7/Text/31', 'PZO22001 Starfinder Player Core 268-281::/page/1/Text/69']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/1/Text/69', 'PZO22001 Starfinder Player Core 268-281::/page/1/Text/70', 'PZO22001 Starfinder Player Core 268-281::/page/1/Text/68']
- Expanded expected found: `True`
- Expanded expected rank: `3`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/1/Text/70` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/1/Text/68` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/13/Text/41` | 0.864442 | **SKILLS** |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/7/Text/31` | 0.864442 | **SKILLS** |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/69` | 0.864442 | **SKILLS** |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/5/Text/70` | 0.651094 | **SKILLS** **FEATS** |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/9/Text/27` | 0.651094 | **SKILLS** **FEATS** |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/11/Text/42` | 0.651094 | **SKILLS** **FEATS** |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/13/Text/40` | 0.420617 | **BACKGROUNDS** **CLASSES** |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/68` | 0.383018 | **CLASSES** |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/7/Text/30` | 0.383018 | **CLASSES** |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/6/Text/26` | 0.379883 | **ELECTRICITY** **MAGICAL** **TECH** |

### Query 83
- Text: What is the rule about **FEATS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/1/Text/70']
- Expected found: `True`
- Expected rank: `4`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/7/Text/32', 'PZO22001 Starfinder Player Core 268-281::/page/3/Text/22', 'PZO22001 Starfinder Player Core 268-281::/page/13/Text/42']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/1/Text/70', 'PZO22001 Starfinder Player Core 268-281::/page/1/Text/71', 'PZO22001 Starfinder Player Core 268-281::/page/1/Text/69']
- Expanded expected found: `True`
- Expanded expected rank: `4`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/1/Text/71` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/1/Text/69` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/7/Text/32` | 0.871817 | **FEATS** |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/13/Text/42` | 0.871817 | **FEATS** |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/3/Text/22` | 0.871817 | **FEATS** |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/70` | 0.829817 | **FEATS** |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/5/Text/70` | 0.653037 | **SKILLS** **FEATS** |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/9/Text/27` | 0.653037 | **SKILLS** **FEATS** |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/11/Text/42` | 0.653037 | **SKILLS** **FEATS** |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/9/Text/45` | 0.344938 | **SHEET** |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/63` | 0.313658 | Force fields absorb damage. A force field's Hit Points are based  on its version. While your force field is active, any physical or  energy damage you would take is applied to the force field's Hit  P |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/3/Text/1` | 0.309453 | **Type **tactical; **Level **10; **Price **11,000 credits The reduction to your armor's penalty to Speeds is 10 feet. |

### Query 84
- Text: What is the rule about **SPELLS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/1/Text/83']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/9/Text/39', 'PZO22001 Starfinder Player Core 268-281::/page/1/Text/83', 'PZO22001 Starfinder Player Core 268-281::/page/7/Text/45']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/1/Text/83', 'PZO22001 Starfinder Player Core 268-281::/page/1/Text/82', 'PZO22001 Starfinder Player Core 268-281::/page/1/Text/84']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/1/Text/82` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/1/Text/84` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/9/Text/39` | 0.889304 | **SPELLS** |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/83` | 0.889304 | **SPELLS** |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/7/Text/45` | 0.889304 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/5/Text/84` | 0.847304 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/3/Text/16` | 0.847303 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/13/Text/56` | 0.847303 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/11/Text/56` | 0.847303 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/69` | 0.388254 | **SKILLS** |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/7/Text/31` | 0.388254 | **SKILLS** |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/13/Text/41` | 0.388254 | **SKILLS** |

### Query 85
- Text: What is the rule about force field is active, attempt a flat check against the listed DC.  On a success, it becomes a normal hit.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/2/Text/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/2/Text/1', 'PZO22001 Starfinder Player Core 268-281::/page/2/Text/6', 'PZO22001 Starfinder Player Core 268-281::/page/2/Text/10']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/2/Text/1', 'PZO22001 Starfinder Player Core 268-281::/page/1/Text/86', 'PZO22001 Starfinder Player Core 268-281::/page/2/Text/2']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/1/Text/86` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/2/Text/2` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/1` | 0.964730 | force field is active, attempt a flat check against the listed DC.  On a success, it becomes a normal hit. |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/6` | 0.690559 | The force field has 14 Hit Points and replenishes 3 Hit Points on  your turn, and the flat check DC is 20. |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/10` | 0.685051 | The force field has 26 Hit Points and replenishes 5 Hit Points  on your turn, and the flat check DC is 18. |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/8` | 0.640211 | The force field has 20 Hit Points and replenishes 4 Hit Points  on your turn, and the flat check DC is 19. |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/12` | 0.639969 | The force field has 32 Hit Points and replenishes 6 Hit Points  on your turn, and the flat check DC is 17. |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/16` | 0.637836 | The force field has 42 Hit Points and replenishes 8 Hit Points  on your turn, and the flat check DC is 15. |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/14` | 0.636097 | The force field has 37 Hit Points and replenishes 7 Hit Points on  your turn, and the flat check DC is 16. |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/4/Text/21` | 0.555371 | Each round, when the weapon finishes using its actions,  attempt a DC 6 flat check. On a failure, the activation ends.  The weapon falls to the ground and can't Autoattack again  for 10 minutes. |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/63` | 0.524811 | Force fields absorb damage. A force field's Hit Points are based  on its version. While your force field is active, any physical or  energy damage you would take is applied to the force field's Hit  P |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/2` | 0.501215 | **Activate—Raise Force Field** [one-action] (manipulate) **Frequency** three  times per day; **Effect** Your force field becomes active. It  remains active for 1 minute or until it's reduced to 0 Hit |

### Query 86
- Text: What is the rule about **Activate—Raise Force Field** [one-action] (manipulate) **Frequency** three  times per day; **Effect** Your force field becomes active. It  remains active for 1 minute or until it's reduced to 0 Hit Points.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/2/Text/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/2/Text/2', 'PZO22001 Starfinder Player Core 268-281::/page/1/Text/63', 'PZO22001 Starfinder Player Core 268-281::/page/2/Text/29']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/2/Text/2', 'PZO22001 Starfinder Player Core 268-281::/page/2/Text/3', 'PZO22001 Starfinder Player Core 268-281::/page/2/Text/1']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/2/Text/3` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/2/Text/1` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/2` | 0.970171 | **Activate—Raise Force Field** [one-action] (manipulate) **Frequency** three  times per day; **Effect** Your force field becomes active. It  remains active for 1 minute or until it's reduced to 0 Hit |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/63` | 0.722220 | Force fields absorb damage. A force field's Hit Points are based  on its version. While your force field is active, any physical or  energy damage you would take is applied to the force field's Hit  P |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/29` | 0.653337 | **Activate—Fly** [one-action] (manipulate) **Effect** You activate a jetpack to  gain a fly Speed of 20 feet. This effect lasts for 1 minute or  until you Dismiss it. You can use an action to Fly 0 fe |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/55` | 0.584092 | **Activate—Thrust** [one-action] (move) **Requirements** You're in a zero-g  environment; **Effect** You move 5 feet in any direction you  choose. You begin to float in that direction. |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/39` | 0.574370 | **Activate—Jump** [one-action] (manipulate) **Frequency** once per round;  **Effect** You activate the jump jets to get a quick boost. You  Fly up to 20 feet with a maximum height of 10 feet, or  you |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/32` | 0.570576 | **Activate—Bend Light **[one-action] (manipulate) **Frequency** once per day;  **Effect** You become invisible for 1 minute, gaining the effects  of a 2nd-rank *invisibility* spell. |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/4/Text/5` | 0.545948 | Most upgrades grant their benefits continually so long as  you're wielding the weapon they're installed in. Others  produce their effects only when used properly in the moment  by spending actions. An |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/57` | 0.542002 | **Activate—Store Grenade** [two-actions] (manipulate) **Effect** You place a  grenade inside a reinforced compartment in the explosive  defense unit. You can Interact to retrieve the grenade  normally |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/8/Text/40` | 0.536169 | **Activate—Halt Cycle **[free-action] (concentrate) **Frequency** once per 10  minutes; **Trigger** You critically hit with your solar weapon  or solar flare as part of an action with the cycle trait; |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/58` | 0.535074 | **Activate—Defensive Detonation **[one-action] (manipulate) **Requirements** You have a stored grenade; **Effect** You detonate the grenade  stored in the explosive defense unit. The explosion is cent |

### Query 87
- Text: What is the rule about The force field has 6 Hit Points and replenishes 2 Hit Points  on your turn.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/2/Text/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/2/Text/4', 'PZO22001 Starfinder Player Core 268-281::/page/2/Text/12', 'PZO22001 Starfinder Player Core 268-281::/page/2/Text/10']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/2/Text/4', 'PZO22001 Starfinder Player Core 268-281::/page/2/Text/5', 'PZO22001 Starfinder Player Core 268-281::/page/2/Text/3']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/2/Text/5` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/2/Text/3` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/4` | 0.926937 | The force field has 6 Hit Points and replenishes 2 Hit Points  on your turn. |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/12` | 0.733149 | The force field has 32 Hit Points and replenishes 6 Hit Points  on your turn, and the flat check DC is 17. |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/10` | 0.731031 | The force field has 26 Hit Points and replenishes 5 Hit Points  on your turn, and the flat check DC is 18. |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/14` | 0.677599 | The force field has 37 Hit Points and replenishes 7 Hit Points on  your turn, and the flat check DC is 16. |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/8` | 0.675702 | The force field has 20 Hit Points and replenishes 4 Hit Points  on your turn, and the flat check DC is 19. |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/6` | 0.675348 | The force field has 14 Hit Points and replenishes 3 Hit Points on  your turn, and the flat check DC is 20. |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/16` | 0.675201 | The force field has 42 Hit Points and replenishes 8 Hit Points  on your turn, and the flat check DC is 15. |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/63` | 0.670587 | Force fields absorb damage. A force field's Hit Points are based  on its version. While your force field is active, any physical or  energy damage you would take is applied to the force field's Hit  P |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/2` | 0.505261 | **Activate—Raise Force Field** [one-action] (manipulate) **Frequency** three  times per day; **Effect** Your force field becomes active. It  remains active for 1 minute or until it's reduced to 0 Hit |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/1` | 0.460208 | force field is active, attempt a flat check against the listed DC.  On a success, it becomes a normal hit. |

### Query 88
- Text: What is the rule about **Type **tactical; **Level **4; **Price **1,000 credits; **Bulk **L?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/2/Text/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/2/Text/5', 'PZO22001 Starfinder Player Core 268-281::/page/2/Text/46', 'PZO22001 Starfinder Player Core 268-281::/page/13/Text/29']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/2/Text/5', 'PZO22001 Starfinder Player Core 268-281::/page/2/Text/4', 'PZO22001 Starfinder Player Core 268-281::/page/2/Text/6']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/2/Text/4` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/2/Text/6` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/5` | 0.894343 | **Type **tactical; **Level **4; **Price **1,000 credits; **Bulk **L |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/46` | 0.730713 | **Type **tactical; **Level **4; **Price **750 credits |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/13/Text/29` | 0.706250 | **Type **tactical; **Level **2; **Price **410 credits |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/5/Text/3` | 0.657537 | **Type **tactical; **Level **1; **Price **100 credits |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/48` | 0.649853 | **Type **tactical; **Level **12; **Price **16,200 credits |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/6/Text/38` | 0.647332 | **Type **tactical; **Level **9; **Price **7,500 credits |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/10` | 0.646818 | **Type **tactical; **Level **9; **Price **6,500 credits |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/9/Text/2` | 0.645991 | **Type **tactical; **Level **14; **Price **45,000 credits |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/9/Text/9` | 0.645991 | **Type **tactical; **Level **14; **Price **45,000 credits |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/26` | 0.645821 | **Type **tactical; **Level **1; **Price **150 credits |

### Query 89
- Text: What is the rule about The force field has 14 Hit Points and replenishes 3 Hit Points on  your turn, and the flat check DC is 20.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/2/Text/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/2/Text/6', 'PZO22001 Starfinder Player Core 268-281::/page/2/Text/8', 'PZO22001 Starfinder Player Core 268-281::/page/2/Text/10']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/2/Text/6', 'PZO22001 Starfinder Player Core 268-281::/page/2/Text/5', 'PZO22001 Starfinder Player Core 268-281::/page/2/Text/7']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/2/Text/5` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/2/Text/7` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/6` | 0.941091 | The force field has 14 Hit Points and replenishes 3 Hit Points on  your turn, and the flat check DC is 20. |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/8` | 0.930708 | The force field has 20 Hit Points and replenishes 4 Hit Points  on your turn, and the flat check DC is 19. |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/10` | 0.919638 | The force field has 26 Hit Points and replenishes 5 Hit Points  on your turn, and the flat check DC is 18. |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/16` | 0.877016 | The force field has 42 Hit Points and replenishes 8 Hit Points  on your turn, and the flat check DC is 15. |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/12` | 0.872516 | The force field has 32 Hit Points and replenishes 6 Hit Points  on your turn, and the flat check DC is 17. |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/14` | 0.869767 | The force field has 37 Hit Points and replenishes 7 Hit Points on  your turn, and the flat check DC is 16. |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/4` | 0.725800 | The force field has 6 Hit Points and replenishes 2 Hit Points  on your turn. |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/1` | 0.671241 | force field is active, attempt a flat check against the listed DC.  On a success, it becomes a normal hit. |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/63` | 0.621053 | Force fields absorb damage. A force field's Hit Points are based  on its version. While your force field is active, any physical or  energy damage you would take is applied to the force field's Hit  P |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/4/Text/24` | 0.483527 | This weapon has a fly Speed of 50 feet. The weapon makes  Strikes with an attack modifier of +27 plus its item bonus to  attack rolls. The flat check to determine if the activation ends  is DC 5 inste |

### Query 90
- Text: What is the rule about The force field has 20 Hit Points and replenishes 4 Hit Points  on your turn, and the flat check DC is 19.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/2/Text/8']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/2/Text/8', 'PZO22001 Starfinder Player Core 268-281::/page/2/Text/6', 'PZO22001 Starfinder Player Core 268-281::/page/2/Text/10']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/2/Text/8', 'PZO22001 Starfinder Player Core 268-281::/page/2/Text/7', 'PZO22001 Starfinder Player Core 268-281::/page/2/Text/9']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/2/Text/7` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/2/Text/9` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/8` | 0.940485 | The force field has 20 Hit Points and replenishes 4 Hit Points  on your turn, and the flat check DC is 19. |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/6` | 0.924248 | The force field has 14 Hit Points and replenishes 3 Hit Points on  your turn, and the flat check DC is 20. |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/10` | 0.914419 | The force field has 26 Hit Points and replenishes 5 Hit Points  on your turn, and the flat check DC is 18. |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/12` | 0.863133 | The force field has 32 Hit Points and replenishes 6 Hit Points  on your turn, and the flat check DC is 17. |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/16` | 0.859201 | The force field has 42 Hit Points and replenishes 8 Hit Points  on your turn, and the flat check DC is 15. |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/14` | 0.855760 | The force field has 37 Hit Points and replenishes 7 Hit Points on  your turn, and the flat check DC is 16. |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/4` | 0.711578 | The force field has 6 Hit Points and replenishes 2 Hit Points  on your turn. |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/1` | 0.654292 | force field is active, attempt a flat check against the listed DC.  On a success, it becomes a normal hit. |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/63` | 0.610719 | Force fields absorb damage. A force field's Hit Points are based  on its version. While your force field is active, any physical or  energy damage you would take is applied to the force field's Hit  P |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/4/Text/24` | 0.485207 | This weapon has a fly Speed of 50 feet. The weapon makes  Strikes with an attack modifier of +27 plus its item bonus to  attack rolls. The flat check to determine if the activation ends  is DC 5 inste |

### Query 91
- Text: What is the rule about The force field has 26 Hit Points and replenishes 5 Hit Points  on your turn, and the flat check DC is 18.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/2/Text/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/2/Text/10', 'PZO22001 Starfinder Player Core 268-281::/page/2/Text/12', 'PZO22001 Starfinder Player Core 268-281::/page/2/Text/8']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/2/Text/10', 'PZO22001 Starfinder Player Core 268-281::/page/2/Text/11', 'PZO22001 Starfinder Player Core 268-281::/page/2/Text/9']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/2/Text/11` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/2/Text/9` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/10` | 0.943709 | The force field has 26 Hit Points and replenishes 5 Hit Points  on your turn, and the flat check DC is 18. |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/12` | 0.926253 | The force field has 32 Hit Points and replenishes 6 Hit Points  on your turn, and the flat check DC is 17. |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/8` | 0.923831 | The force field has 20 Hit Points and replenishes 4 Hit Points  on your turn, and the flat check DC is 19. |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/6` | 0.878349 | The force field has 14 Hit Points and replenishes 3 Hit Points on  your turn, and the flat check DC is 20. |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/16` | 0.873434 | The force field has 42 Hit Points and replenishes 8 Hit Points  on your turn, and the flat check DC is 15. |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/14` | 0.872656 | The force field has 37 Hit Points and replenishes 7 Hit Points on  your turn, and the flat check DC is 16. |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/4` | 0.741652 | The force field has 6 Hit Points and replenishes 2 Hit Points  on your turn. |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/1` | 0.665409 | force field is active, attempt a flat check against the listed DC.  On a success, it becomes a normal hit. |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/63` | 0.620470 | Force fields absorb damage. A force field's Hit Points are based  on its version. While your force field is active, any physical or  energy damage you would take is applied to the force field's Hit  P |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/4/Text/24` | 0.515891 | This weapon has a fly Speed of 50 feet. The weapon makes  Strikes with an attack modifier of +27 plus its item bonus to  attack rolls. The flat check to determine if the activation ends  is DC 5 inste |

### Query 92
- Text: What is the rule about The force field has 32 Hit Points and replenishes 6 Hit Points  on your turn, and the flat check DC is 17.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/2/Text/12']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/2/Text/12', 'PZO22001 Starfinder Player Core 268-281::/page/2/Text/10', 'PZO22001 Starfinder Player Core 268-281::/page/2/Text/14']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/2/Text/12', 'PZO22001 Starfinder Player Core 268-281::/page/2/Text/11', 'PZO22001 Starfinder Player Core 268-281::/page/2/Text/13']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/2/Text/11` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/2/Text/13` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/12` | 0.946408 | The force field has 32 Hit Points and replenishes 6 Hit Points  on your turn, and the flat check DC is 17. |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/10` | 0.936566 | The force field has 26 Hit Points and replenishes 5 Hit Points  on your turn, and the flat check DC is 18. |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/14` | 0.928676 | The force field has 37 Hit Points and replenishes 7 Hit Points on  your turn, and the flat check DC is 16. |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/6` | 0.885132 | The force field has 14 Hit Points and replenishes 3 Hit Points on  your turn, and the flat check DC is 20. |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/8` | 0.884610 | The force field has 20 Hit Points and replenishes 4 Hit Points  on your turn, and the flat check DC is 19. |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/16` | 0.883263 | The force field has 42 Hit Points and replenishes 8 Hit Points  on your turn, and the flat check DC is 15. |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/4` | 0.742783 | The force field has 6 Hit Points and replenishes 2 Hit Points  on your turn. |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/1` | 0.672759 | force field is active, attempt a flat check against the listed DC.  On a success, it becomes a normal hit. |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/63` | 0.616294 | Force fields absorb damage. A force field's Hit Points are based  on its version. While your force field is active, any physical or  energy damage you would take is applied to the force field's Hit  P |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/4/Text/24` | 0.499891 | This weapon has a fly Speed of 50 feet. The weapon makes  Strikes with an attack modifier of +27 plus its item bonus to  attack rolls. The flat check to determine if the activation ends  is DC 5 inste |

### Query 93
- Text: What is the rule about The force field has 37 Hit Points and replenishes 7 Hit Points on  your turn, and the flat check DC is 16.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/2/Text/14']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/2/Text/14', 'PZO22001 Starfinder Player Core 268-281::/page/2/Text/12', 'PZO22001 Starfinder Player Core 268-281::/page/2/Text/10']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/2/Text/14', 'PZO22001 Starfinder Player Core 268-281::/page/2/Text/15', 'PZO22001 Starfinder Player Core 268-281::/page/2/Text/13']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/2/Text/15` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/2/Text/13` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/14` | 0.946662 | The force field has 37 Hit Points and replenishes 7 Hit Points on  your turn, and the flat check DC is 16. |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/12` | 0.943792 | The force field has 32 Hit Points and replenishes 6 Hit Points  on your turn, and the flat check DC is 17. |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/10` | 0.940745 | The force field has 26 Hit Points and replenishes 5 Hit Points  on your turn, and the flat check DC is 18. |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/16` | 0.897135 | The force field has 42 Hit Points and replenishes 8 Hit Points  on your turn, and the flat check DC is 15. |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/6` | 0.895425 | The force field has 14 Hit Points and replenishes 3 Hit Points on  your turn, and the flat check DC is 20. |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/8` | 0.891310 | The force field has 20 Hit Points and replenishes 4 Hit Points  on your turn, and the flat check DC is 19. |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/4` | 0.745295 | The force field has 6 Hit Points and replenishes 2 Hit Points  on your turn. |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/1` | 0.679686 | force field is active, attempt a flat check against the listed DC.  On a success, it becomes a normal hit. |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/63` | 0.626690 | Force fields absorb damage. A force field's Hit Points are based  on its version. While your force field is active, any physical or  energy damage you would take is applied to the force field's Hit  P |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/4/Text/24` | 0.501155 | This weapon has a fly Speed of 50 feet. The weapon makes  Strikes with an attack modifier of +27 plus its item bonus to  attack rolls. The flat check to determine if the activation ends  is DC 5 inste |

### Query 94
- Text: What is the rule about The force field has 42 Hit Points and replenishes 8 Hit Points  on your turn, and the flat check DC is 15.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/2/Text/16']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/2/Text/16', 'PZO22001 Starfinder Player Core 268-281::/page/2/Text/6', 'PZO22001 Starfinder Player Core 268-281::/page/2/Text/10']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/2/Text/16', 'PZO22001 Starfinder Player Core 268-281::/page/2/SectionHeader/17', 'PZO22001 Starfinder Player Core 268-281::/page/2/Text/15']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/2/SectionHeader/17` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/2/Text/15` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/16` | 0.945555 | The force field has 42 Hit Points and replenishes 8 Hit Points  on your turn, and the flat check DC is 15. |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/6` | 0.933209 | The force field has 14 Hit Points and replenishes 3 Hit Points on  your turn, and the flat check DC is 20. |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/10` | 0.930310 | The force field has 26 Hit Points and replenishes 5 Hit Points  on your turn, and the flat check DC is 18. |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/14` | 0.885901 | The force field has 37 Hit Points and replenishes 7 Hit Points on  your turn, and the flat check DC is 16. |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/12` | 0.885869 | The force field has 32 Hit Points and replenishes 6 Hit Points  on your turn, and the flat check DC is 17. |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/8` | 0.883588 | The force field has 20 Hit Points and replenishes 4 Hit Points  on your turn, and the flat check DC is 19. |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/4` | 0.734527 | The force field has 6 Hit Points and replenishes 2 Hit Points  on your turn. |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/1` | 0.668160 | force field is active, attempt a flat check against the listed DC.  On a success, it becomes a normal hit. |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/63` | 0.623650 | Force fields absorb damage. A force field's Hit Points are based  on its version. While your force field is active, any physical or  energy damage you would take is applied to the force field's Hit  P |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/4/Text/24` | 0.490983 | This weapon has a fly Speed of 50 feet. The weapon makes  Strikes with an attack modifier of +27 plus its item bonus to  attack rolls. The flat check to determine if the activation ends  is DC 5 inste |

### Query 95
- Text: What is the rule about **Activate—Glamerize!** [one-action] (manipulate) **Effect** You instantly  change the appearance of your armor to any set of normal  clothes or any other type of light or heavy armor. This  upgrade is capable of changing only the appearance of your  armor, not yourself or the rest of your equipment. You can  copy the look of any type of clothing, but you don't gain any  item bonuses provided by special types of clothing, such as  luxury fashion attire. Only a creature that's benefiting from  *truesight* or a similar effect can attempt to disbelieve this  illusion, opposed by your class DC.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/2/Text/23']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/2/Text/23', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/9', 'PZO22001 Starfinder Player Core 268-281::/page/0/Text/3']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/2/Text/23', 'PZO22001 Starfinder Player Core 268-281::/page/2/Text/25', 'PZO22001 Starfinder Player Core 268-281::/page/2/Text/22']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/2/Text/25` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/2/Text/22` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/23` | 0.998611 | **Activate—Glamerize!** [one-action] (manipulate) **Effect** You instantly  change the appearance of your armor to any set of normal  clothes or any other type of light or heavy armor. This  upgrade i |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/9` | 0.649266 | Most upgrades grant their benefits continually so long as  you're properly wearing the armor they're installed in. Others  produce their effects only when used properly in the moment  by spending acti |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/3` | 0.585731 | You can personalize armor by purchasing and installing armor  upgrades. Armor upgrades are installed into the upgrade slots  of armor; one armor upgrade occupies one armor upgrade slot.  The number of |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/57` | 0.534975 | **Activate—Store Grenade** [two-actions] (manipulate) **Effect** You place a  grenade inside a reinforced compartment in the explosive  defense unit. You can Interact to retrieve the grenade  normally |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/20` | 0.531425 | **Activate—Adapt** [reaction] **Frequency** once per 10 minutes; **Trigger** You  take acid, cold, electricity, or fire damage; **Effect** Your *energy * *shielding* upgrade changes to the triggering |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/4/Text/5` | 0.530352 | Most upgrades grant their benefits continually so long as  you're wielding the weapon they're installed in. Others  produce their effects only when used properly in the moment  by spending actions. An |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/11` | 0.524977 | Some armor upgrades that have special activations and benefits  can be activated only a limited number of times per day, as  described in the armor upgrade. This limit is independent of any  costs for |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/32` | 0.512713 | **Activate—Bend Light **[one-action] (manipulate) **Frequency** once per day;  **Effect** You become invisible for 1 minute, gaining the effects  of a 2nd-rank *invisibility* spell. |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/7/Text/9` | 0.511435 | **Activate—See the Truth**[two-actions] (manipulate) **Frequency** once per  day; **Effect** For the next 10 minutes, while looking through  the scope, you can see invisible creatures as though they |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/8` | 0.500914 | Hardlight projectors shift the appearance of your armor  using shifting colors and patterns that respond to your  environment. You gain a +1 item bonus to Stealth checks  while wearing the armor. |

### Query 96
- Text: What is the rule about **JETPACK** **UPGRADE 5+**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/2/Text/25']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/2/Text/25', 'PZO22001 Starfinder Player Core 268-281::/page/1/SectionHeader/4', 'PZO22001 Starfinder Player Core 268-281::/page/2/Text/34']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/2/Text/25', 'PZO22001 Starfinder Player Core 268-281::/page/2/Text/26', 'PZO22001 Starfinder Player Core 268-281::/page/2/Text/23']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/2/Text/26` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/2/Text/23` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/25` | 0.924067 | **JETPACK** **UPGRADE 5+** |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/1/SectionHeader/4` | 0.567310 | **ACTIVE CAMOUFLAGE** **UPGRADE 5+** |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/34` | 0.563648 | **JUMP JETS** **UPGRADE 3** |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/5/SectionHeader/15` | 0.478552 | **FEAR PROJECTOR** **UPGRADE 5+** |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/2/SectionHeader/63` | 0.462546 | **MOBILITY ENHANCER** **UPGRADE 3+** |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/6/SectionHeader/24` | 0.460284 | **SHOCK MODULE** **UPGRADE 8+** |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/2/SectionHeader/50` | 0.457923 | **MANEUVERING UNIT** **UPGRADE 4+** |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/1/SectionHeader/27` | 0.454427 | **CLOAKING DEVICE** **UPGRADE 8+** |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/9/Text/34` | 0.454043 | **Upgrades** |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/13/Text/50` | 0.454043 | **Upgrades** |

### Query 97
- Text: What is the rule about Boosters attached to your armor allow you to fly.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/2/Text/28']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/2/Text/28', 'PZO22001 Starfinder Player Core 268-281::/page/2/Text/38', 'PZO22001 Starfinder Player Core 268-281::/page/6/Text/23']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/2/Text/28', 'PZO22001 Starfinder Player Core 268-281::/page/2/Text/29', 'PZO22001 Starfinder Player Core 268-281::/page/2/Text/27']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/2/Text/29` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/2/Text/27` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/28` | 0.914596 | Boosters attached to your armor allow you to fly. |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/38` | 0.646672 | Boosters attached to your armor supercharge your leap. |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/6/Text/23` | 0.483248 | When you make a thrown Strike with this weapon, a complex  combination of stabilizers and boosters propels it back  into your free hand (or other appendage) after the Strike is  complete. If your hand |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/29` | 0.440977 | **Activate—Fly** [one-action] (manipulate) **Effect** You activate a jetpack to  gain a fly Speed of 20 feet. This effect lasts for 1 minute or  until you Dismiss it. You can use an action to Fly 0 fe |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/32` | 0.425034 | Increase the fly Speed of your jetpack to 40 feet. You aren't  off-guard while hovering in place. |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/11` | 0.418814 | Some armor upgrades that have special activations and benefits  can be activated only a limited number of times per day, as  described in the armor upgrade. This limit is independent of any  costs for |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/39` | 0.416679 | **Activate—Jump** [one-action] (manipulate) **Frequency** once per round;  **Effect** You activate the jump jets to get a quick boost. You  Fly up to 20 feet with a maximum height of 10 feet, or  you |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/3` | 0.412178 | You can personalize armor by purchasing and installing armor  upgrades. Armor upgrades are installed into the upgrade slots  of armor; one armor upgrade occupies one armor upgrade slot.  The number of |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/4/Text/31` | 0.394449 | A bipod can be attached to powerful weapons—those with  the kickback trait—to allow wielders with lower Strength to  use them at the cost of mobility. You can set up the bipod  with a single Interact |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/19` | 0.391699 | This upgrade protects the user against the effects of space as  well as thick and thin atmospheres. This armor loses the exposed  trait for as long as the upgrade is installed. |

### Query 98
- Text: What is the rule about **Activate—Fly** [one-action] (manipulate) **Effect** You activate a jetpack to  gain a fly Speed of 20 feet. This effect lasts for 1 minute or  until you Dismiss it. You can use an action to Fly 0 feet to  hover in place, but you're off-guard while doing so. A jetpack  can't lift you if you're encumbered.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/2/Text/29']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/2/Text/29', 'PZO22001 Starfinder Player Core 268-281::/page/2/Text/39', 'PZO22001 Starfinder Player Core 268-281::/page/2/Text/55']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/2/Text/29', 'PZO22001 Starfinder Player Core 268-281::/page/2/Text/30', 'PZO22001 Starfinder Player Core 268-281::/page/2/Text/28']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/2/Text/30` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/2/Text/28` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/29` | 0.980197 | **Activate—Fly** [one-action] (manipulate) **Effect** You activate a jetpack to  gain a fly Speed of 20 feet. This effect lasts for 1 minute or  until you Dismiss it. You can use an action to Fly 0 fe |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/39` | 0.827948 | **Activate—Jump** [one-action] (manipulate) **Frequency** once per round;  **Effect** You activate the jump jets to get a quick boost. You  Fly up to 20 feet with a maximum height of 10 feet, or  you |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/55` | 0.676359 | **Activate—Thrust** [one-action] (move) **Requirements** You're in a zero-g  environment; **Effect** You move 5 feet in any direction you  choose. You begin to float in that direction. |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/2` | 0.633158 | **Activate—Raise Force Field** [one-action] (manipulate) **Frequency** three  times per day; **Effect** Your force field becomes active. It  remains active for 1 minute or until it's reduced to 0 Hit |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/4/Text/18` | 0.619975 | **Activate—Autoattack** [two-actions] (concentrate, manipulate) **Effect** You Release the weapon and it glides through the air,  fighting on its own against the last enemy you attacked, or  the neare |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/32` | 0.602851 | Increase the fly Speed of your jetpack to 40 feet. You aren't  off-guard while hovering in place. |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/4/Text/5` | 0.548718 | Most upgrades grant their benefits continually so long as  you're wielding the weapon they're installed in. Others  produce their effects only when used properly in the moment  by spending actions. An |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/58` | 0.544273 | **Activate—Defensive Detonation **[one-action] (manipulate) **Requirements** You have a stored grenade; **Effect** You detonate the grenade  stored in the explosive defense unit. The explosion is cent |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/9` | 0.540426 | Most upgrades grant their benefits continually so long as  you're properly wearing the armor they're installed in. Others  produce their effects only when used properly in the moment  by spending acti |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/7/Text/18` | 0.536535 | **Activate—Launch** [one-action] (attack) **Effect** You launch the loaded  grenade. |

### Query 99
- Text: What is the rule about **Type **tactical; **Level **19; **Price **350,000 credits?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/2/Text/31']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/2/Text/31', 'PZO22001 Starfinder Player Core 268-281::/page/7/Text/11', 'PZO22001 Starfinder Player Core 268-281::/page/7/Text/21']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/2/Text/31', 'PZO22001 Starfinder Player Core 268-281::/page/2/Text/30', 'PZO22001 Starfinder Player Core 268-281::/page/2/Text/32']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/2/Text/30` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/2/Text/32` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/31` | 0.905424 | **Type **tactical; **Level **19; **Price **350,000 credits |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/7/Text/11` | 0.751215 | **Type **tactical; **Level **13; **Price **30,000 credits |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/7/Text/21` | 0.747837 | **Type **tactical; **Level **2; **Price **250 credits |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/9/Text/2` | 0.703133 | **Type **tactical; **Level **14; **Price **45,000 credits |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/9/Text/9` | 0.703133 | **Type **tactical; **Level **14; **Price **45,000 credits |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/13/Text/29` | 0.698993 | **Type **tactical; **Level **2; **Price **410 credits |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/0/Text/26` | 0.698747 | **Type **tactical; **Level **1; **Price **150 credits |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/10` | 0.697989 | **Type **tactical; **Level **9; **Price **6,500 credits |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/5/Text/3` | 0.696898 | **Type **tactical; **Level **1; **Price **100 credits |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/5/Text/21` | 0.692943 | **Type **tactical; **Level **12; **Price **20,000 credits |

### Query 100
- Text: Lookup values for ItemLevelPriceBulkDarkvision visor1150LForce field, commercial1200LGlamer projector1100LAuto-CPR unit2200LLoad lifter, commercial2550LJump jets3550LMobility enhancer,
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/3/Table/3']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/3/Table/3', 'PZO22001 Starfinder Player Core 268-281::/page/9/Table/19', 'PZO22001 Starfinder Player Core 268-281::/page/9/Table/18']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/3/Table/3', 'PZO22001 Starfinder Player Core 268-281::/page/3/SectionHeader/2', 'PZO22001 Starfinder Player Core 268-281::/page/3/TableCell/619']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/3/SectionHeader/2` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/3/TableCell/619` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/3/Table/3` | 0.962307 | ItemLevelPriceBulkDarkvision visor1150LForce field, commercial1200LGlamer projector1100LAuto-CPR unit2200LLoad lifter, commercial2550LJump jets3550LMobility enhancer, commercial31,000LForce field, tac |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/9/Table/19` | 0.729688 | ItemLevelPriceBulkFlaming module, commercial85,000—Frost module, commercial85,000—Loudener, commercial85,000LShock module, commercial85,000—Truesight sight, commercial88,000—Silencer, tactical97,500LS |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/9/Table/18` | 0.729333 | ItemLevelPriceBulkBipod, commercial021Silencer, commercial010LUndermounted grenade launcher, commercial0501Bipod, tactical11001Sniper's scope, commercial1150LUniclamp1100LBipod, advanced24501Smuggler' |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/3/Table/4` | 0.653511 | ItemLevelPriceBulkManeuvering unit, advanced1113,400LEnergy shielding, tactical1216,200LAdaptive energy shielding1322,500LForce field, elite1330,0001Maneuvering unit, superior1564,400LForce field, ult |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/3/Table/6` | 0.569367 | ItemLevelPriceBulkBasic environmental protection010LFiltered rebreather, commercial05LRadiation buffer, commercial11301Thermal capacitor, commercial1120LFiltered rebreather,advanced62,550LRadiation bu |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/3` | 0.532220 | **Type **commercial; **Level **1; **Price **200 credits; **Bulk **L |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/13/Table/36` | 0.528440 | GrenadeItem LevelPriceDamageElectromag grenade, commercial0101d8 EFrag grenade, commercial0101d8 PIncendiary grenade, commercial0101d8 FFlash grenade, commercial010–Smoke grenade, commercial010–Electr |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/3/TableCell/639` | 0.523977 | Load lifter, commercial |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/3/TableCell/623` | 0.479507 | Darkvision visor |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/5` | 0.478344 | **Type **tactical; **Level **4; **Price **1,000 credits; **Bulk **L |

### Query 101
- Text: Lookup values for ItemLevelPriceBulkManeuvering unit, advanced1113,400LEnergy shielding, tactical1216,200LAdaptive energy shielding1322,500LForce field, elite1330,0001Maneuvering unit, superior1564,400LForce field, ultimate16100,0001Active camouflage, advanced17140,000LEnergy shielding, advanced18202,200LForce field, paragon19400,0001Jetpack, tactical19350,000L
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/3/Table/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/3/Table/4', 'PZO22001 Starfinder Player Core 268-281::/page/3/Table/3', 'PZO22001 Starfinder Player Core 268-281::/page/9/Table/19']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/3/Table/4', 'PZO22001 Starfinder Player Core 268-281::/page/3/TableCell/710', 'PZO22001 Starfinder Player Core 268-281::/page/3/TableCell/711']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/3/TableCell/710` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/3/TableCell/711` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/3/Table/4` | 1.028515 | ItemLevelPriceBulkManeuvering unit, advanced1113,400LEnergy shielding, tactical1216,200LAdaptive energy shielding1322,500LForce field, elite1330,0001Maneuvering unit, superior1564,400LForce field, ult |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/3/Table/3` | 0.827204 | ItemLevelPriceBulkDarkvision visor1150LForce field, commercial1200LGlamer projector1100LAuto-CPR unit2200LLoad lifter, commercial2550LJump jets3550LMobility enhancer, commercial31,000LForce field, tac |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/9/Table/19` | 0.744005 | ItemLevelPriceBulkFlaming module, commercial85,000—Frost module, commercial85,000—Loudener, commercial85,000LShock module, commercial85,000—Truesight sight, commercial88,000—Silencer, tactical97,500LS |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/9/Table/18` | 0.643314 | ItemLevelPriceBulkBipod, commercial021Silencer, commercial010LUndermounted grenade launcher, commercial0501Bipod, tactical11001Sniper's scope, commercial1150LUniclamp1100LBipod, advanced24501Smuggler' |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/13/Table/36` | 0.625363 | GrenadeItem LevelPriceDamageElectromag grenade, commercial0101d8 EFrag grenade, commercial0101d8 PIncendiary grenade, commercial0101d8 FFlash grenade, commercial010–Smoke grenade, commercial010–Electr |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/3/Table/6` | 0.619373 | ItemLevelPriceBulkBasic environmental protection010LFiltered rebreather, commercial05LRadiation buffer, commercial11301Thermal capacitor, commercial1120LFiltered rebreather,advanced62,550LRadiation bu |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/15` | 0.570448 | **Type **paragon; **Level **19; **Price **400,000 credits; **Bulk **1 |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/5` | 0.561417 | **Type **tactical; **Level **4; **Price **1,000 credits; **Bulk **L |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/9/Table/21` | 0.558802 | Core CrystalsItemLevelPrice+1 weapon potency2350Striking, commercial4650+2 weapon potency109,350Striking, tactical1210,650+3 weapon potency1689,350Striking, advanced19310,650 |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/13` | 0.536919 | **Type **ultimate; **Level **16; **Price **100,000 credits; **Bulk **1 |

### Query 102
- Text: Lookup values for ItemLevelPriceBulkBasic environmental
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/3/Table/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/3/Table/6', 'PZO22001 Starfinder Player Core 268-281::/page/2/Text/3', 'PZO22001 Starfinder Player Core 268-281::/page/2/Text/9']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/3/Table/6', 'PZO22001 Starfinder Player Core 268-281::/page/3/TableCell/756', 'PZO22001 Starfinder Player Core 268-281::/page/3/SectionHeader/5']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/3/TableCell/756` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/3/SectionHeader/5` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/3/Table/6` | 0.583116 | ItemLevelPriceBulkBasic environmental protection010LFiltered rebreather, commercial05LRadiation buffer, commercial11301Thermal capacitor, commercial1120LFiltered rebreather,advanced62,550LRadiation bu |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/3` | 0.573252 | **Type **commercial; **Level **1; **Price **200 credits; **Bulk **L |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/9` | 0.525966 | **Type **superior; **Level **10; **Price **10,000 credits; **Bulk **L |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/7` | 0.474797 | **Type **advanced; **Level **7; **Price **3,600 credits; **Bulk **L |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/11` | 0.470801 | **Type **elite; **Level **13; **Price **30,000 credits; **Bulk **1 |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/3/Table/4` | 0.466286 | ItemLevelPriceBulkManeuvering unit, advanced1113,400LEnergy shielding, tactical1216,200LAdaptive energy shielding1322,500LForce field, elite1330,0001Maneuvering unit, superior1564,400LForce field, ult |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/13` | 0.457862 | **Type **ultimate; **Level **16; **Price **100,000 credits; **Bulk **1 |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/5` | 0.435101 | **Type **tactical; **Level **4; **Price **1,000 credits; **Bulk **L |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/3/Table/3` | 0.427392 | ItemLevelPriceBulkDarkvision visor1150LForce field, commercial1200LGlamer projector1100LAuto-CPR unit2200LLoad lifter, commercial2550LJump jets3550LMobility enhancer, commercial31,000LForce field, tac |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/0/SectionHeader/14` | 0.414280 | **BASIC ENVIRONMENTAL PROTECTION** **UPGRADE 0** |

### Query 103
- Text: Lookup values for ItemLevelPriceBulkBipod, commercial021Silencer, commercial010LUndermounted grenade
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/9/Table/18']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/9/Table/18', 'PZO22001 Starfinder Player Core 268-281::/page/9/Table/19', 'PZO22001 Starfinder Player Core 268-281::/page/3/Table/3']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/9/Table/18', 'PZO22001 Starfinder Player Core 268-281::/page/9/TableCell/835', 'PZO22001 Starfinder Player Core 268-281::/page/9/SectionHeader/17']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/9/TableCell/835` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/9/SectionHeader/17` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/9/Table/18` | 0.842768 | ItemLevelPriceBulkBipod, commercial021Silencer, commercial010LUndermounted grenade launcher, commercial0501Bipod, tactical11001Sniper's scope, commercial1150LUniclamp1100LBipod, advanced24501Smuggler' |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/9/Table/19` | 0.729676 | ItemLevelPriceBulkFlaming module, commercial85,000—Frost module, commercial85,000—Loudener, commercial85,000LShock module, commercial85,000—Truesight sight, commercial88,000—Silencer, tactical97,500LS |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/3/Table/3` | 0.661913 | ItemLevelPriceBulkDarkvision visor1150LForce field, commercial1200LGlamer projector1100LAuto-CPR unit2200LLoad lifter, commercial2550LJump jets3550LMobility enhancer, commercial31,000LForce field, tac |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/13/Table/36` | 0.605116 | GrenadeItem LevelPriceDamageElectromag grenade, commercial0101d8 EFrag grenade, commercial0101d8 PIncendiary grenade, commercial0101d8 FFlash grenade, commercial010–Smoke grenade, commercial010–Electr |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/9/TableCell/847` | 0.570437 | Undermounted grenade launcher, commercial |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/3` | 0.552395 | **Type **commercial; **Level **1; **Price **200 credits; **Bulk **L |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/5/Text/27` | 0.545862 | **Usage** installed in a grenade launcher or two-handed weapon  with an undermounted grenade launcher; **Bulk **L |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/9/TableCell/839` | 0.541768 | Bipod, commercial |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/3/Table/4` | 0.539513 | ItemLevelPriceBulkManeuvering unit, advanced1113,400LEnergy shielding, tactical1216,200LAdaptive energy shielding1322,500LForce field, elite1330,0001Maneuvering unit, superior1564,400LForce field, ult |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/13/TableCell/859` | 0.524403 | Flash grenade, commercial |

### Query 104
- Text: Lookup values for ItemLevelPriceBulkFlaming module, commercial85,000—Frost module, commercial85,000—Loudener, commercial85,000LShock module, commercial85,000—Truesight sight, commercial88,000—Silencer, tactical97,500LSniper's scope, advanced98,000LUndermounted grenade
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/9/Table/19']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/9/Table/19', 'PZO22001 Starfinder Player Core 268-281::/page/9/Table/18', 'PZO22001 Starfinder Player Core 268-281::/page/3/Table/3']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/9/Table/19', 'PZO22001 Starfinder Player Core 268-281::/page/9/TableCell/906', 'PZO22001 Starfinder Player Core 268-281::/page/9/TableCell/907']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/9/TableCell/906` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/9/TableCell/907` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/9/Table/19` | 0.978081 | ItemLevelPriceBulkFlaming module, commercial85,000—Frost module, commercial85,000—Loudener, commercial85,000LShock module, commercial85,000—Truesight sight, commercial88,000—Silencer, tactical97,500LS |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/9/Table/18` | 0.834617 | ItemLevelPriceBulkBipod, commercial021Silencer, commercial010LUndermounted grenade launcher, commercial0501Bipod, tactical11001Sniper's scope, commercial1150LUniclamp1100LBipod, advanced24501Smuggler' |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/3/Table/3` | 0.752677 | ItemLevelPriceBulkDarkvision visor1150LForce field, commercial1200LGlamer projector1100LAuto-CPR unit2200LLoad lifter, commercial2550LJump jets3550LMobility enhancer, commercial31,000LForce field, tac |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/3/Table/4` | 0.659181 | ItemLevelPriceBulkManeuvering unit, advanced1113,400LEnergy shielding, tactical1216,200LAdaptive energy shielding1322,500LForce field, elite1330,0001Maneuvering unit, superior1564,400LForce field, ult |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/13/Table/36` | 0.634841 | GrenadeItem LevelPriceDamageElectromag grenade, commercial0101d8 EFrag grenade, commercial0101d8 PIncendiary grenade, commercial0101d8 FFlash grenade, commercial010–Smoke grenade, commercial010–Electr |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/3/Table/6` | 0.568476 | ItemLevelPriceBulkBasic environmental protection010LFiltered rebreather, commercial05LRadiation buffer, commercial11301Thermal capacitor, commercial1120LFiltered rebreather,advanced62,550LRadiation bu |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/3` | 0.557179 | **Type **commercial; **Level **1; **Price **200 credits; **Bulk **L |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/9/Table/21` | 0.545748 | Core CrystalsItemLevelPrice+1 weapon potency2350Striking, commercial4650+2 weapon potency109,350Striking, tactical1210,650+3 weapon potency1689,350Striking, advanced19310,650 |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/9/TableCell/911` | 0.542750 | Flaming module, commercial |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/2/Text/5` | 0.535331 | **Type **tactical; **Level **4; **Price **1,000 credits; **Bulk **L |

### Query 105
- Text: Lookup values for Core CrystalsItemLevelPrice+1 weapon potency2350Striking, commercial4650+2 weapon potency109,350Striking, tactical1210,650+3 weapon potency1689,350Striking, advanced19310,650
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/9/Table/21']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/9/Table/21', 'PZO22001 Starfinder Player Core 268-281::/page/9/Table/22', 'PZO22001 Starfinder Player Core 268-281::/page/9/TableCell/1003']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/9/Table/21', 'PZO22001 Starfinder Player Core 268-281::/page/9/SectionHeader/20', 'PZO22001 Starfinder Player Core 268-281::/page/9/TableCell/1003']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/9/SectionHeader/20` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/9/TableCell/1003` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/9/Table/21` | 1.011165 | Core CrystalsItemLevelPrice+1 weapon potency2350Striking, commercial4650+2 weapon potency109,350Striking, tactical1210,650+3 weapon potency1689,350Striking, advanced19310,650 |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/9/Table/22` | 0.694353 | Orbital CrystalsItemLevelPriceCycling62,000Gluon, commercial62,360Graviton, commercial73,600Photon, commercial73,600Gluon, tactical96,600Gluon, advanced1218,900QuasarU1330,000Graviton, tactical1445,00 |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/9/TableCell/1003` | 0.643430 | Core Crystals |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/8/Text/29` | 0.568185 | **Type ***+2 weapon potency*; **Level **10; **Price **9,350 credits |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/8/Text/28` | 0.565310 | **Type ***+1 weapon potency*; **Level **2; **Price **350 credits |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/8/Text/23` | 0.557757 | **WEAPON POTENCY** **CRYSTAL 2+** |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/8/Text/31` | 0.543035 | **Type ***+3 weapon potency*; **Level **16; **Price **89,350 credits The item bonus to attack rolls is +3, and the weapon or flare  can benefit from three orbital crystals. |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/8/SectionHeader/11` | 0.531962 | Core Solarian Crystals |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/9/Table/19` | 0.526735 | ItemLevelPriceBulkFlaming module, commercial85,000—Frost module, commercial85,000—Loudener, commercial85,000LShock module, commercial85,000—Truesight sight, commercial88,000—Silencer, tactical97,500LS |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/9/TableCell/1009` | 0.524874 | +1 weapon potency |

### Query 106
- Text: Lookup values for Orbital CrystalsItemLevelPriceCycling62,000Gluon, commercial62,360Graviton, commercial73,600Photon, commercial73,600Gluon, tactical96,600Gluon, advanced1218,900QuasarU1330,000Graviton, tactical1445,000Photon, tactical1445,000Gluon, superior1561,400
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/9/Table/22']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/9/Table/22', 'PZO22001 Starfinder Player Core 268-281::/page/9/Table/21', 'PZO22001 Starfinder Player Core 268-281::/page/9/TableCell/1027']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/9/Table/22', 'PZO22001 Starfinder Player Core 268-281::/page/9/TableCell/1026', 'PZO22001 Starfinder Player Core 268-281::/page/9/TableCell/1027']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/9/TableCell/1026` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/9/TableCell/1027` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/9/Table/22` | 1.024057 | Orbital CrystalsItemLevelPriceCycling62,000Gluon, commercial62,360Graviton, commercial73,600Photon, commercial73,600Gluon, tactical96,600Gluon, advanced1218,900QuasarU1330,000Graviton, tactical1445,00 |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/9/Table/21` | 0.714592 | Core CrystalsItemLevelPrice+1 weapon potency2350Striking, commercial4650+2 weapon potency109,350Striking, tactical1210,650+3 weapon potency1689,350Striking, advanced19310,650 |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/9/TableCell/1027` | 0.694805 | Orbital Crystals |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/8/SectionHeader/32` | 0.613450 | Orbital Solarian Crystals |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/9/Table/19` | 0.534578 | ItemLevelPriceBulkFlaming module, commercial85,000—Frost module, commercial85,000—Loudener, commercial85,000LShock module, commercial85,000—Truesight sight, commercial88,000—Silencer, tactical97,500LS |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/9/Table/18` | 0.518115 | ItemLevelPriceBulkBipod, commercial021Silencer, commercial010LUndermounted grenade launcher, commercial0501Bipod, tactical11001Sniper's scope, commercial1150LUniclamp1100LBipod, advanced24501Smuggler' |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/9/SectionHeader/20` | 0.492473 | **SOLARIAN WEAPON CRYSTALS** |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/13/Text/20` | 0.482770 | **Type **commercial; **Level **0; **Price **10 credits; **Radius** 5 feet **Type **tactical; **Level **2; **Price **80 credits; **Radius** 10 feet **Type **advanced; **Level **4; **Price **120 credits |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/8/SectionHeader/11` | 0.480955 | Core Solarian Crystals |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/3/Table/3` | 0.467176 | ItemLevelPriceBulkDarkvision visor1150LForce field, commercial1200LGlamer projector1100LAuto-CPR unit2200LLoad lifter, commercial2550LJump jets3550LMobility enhancer, commercial31,000LForce field, tac |

### Query 107
- Text: Lookup values for GrenadeItem
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/13/Table/36']
- Expected found: `True`
- Expected rank: `6`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 268-281::/page/13/TableCell/843', 'PZO22001 Starfinder Player Core 268-281::/page/3/Text/14', 'PZO22001 Starfinder Player Core 268-281::/page/7/Text/42']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 268-281::/page/13/Table/36', 'PZO22001 Starfinder Player Core 268-281::/page/13/SectionHeader/35', 'PZO22001 Starfinder Player Core 268-281::/page/13/TableCell/843']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 268-281::/page/13/SectionHeader/35` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 268-281::/page/13/TableCell/843` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 268-281::/page/13/TableCell/843` | 0.644623 | Grenade |
| 2 | `PZO22001 Starfinder Player Core 268-281::/page/3/Text/14` | 0.619307 | **Grenades** **Magic Items** |
| 3 | `PZO22001 Starfinder Player Core 268-281::/page/7/Text/42` | 0.606447 | **Weapons** **Grenades** |
| 4 | `PZO22001 Starfinder Player Core 268-281::/page/1/Text/80` | 0.564447 | **Weapons** **Grenades** |
| 5 | `PZO22001 Starfinder Player Core 268-281::/page/5/Text/81` | 0.564447 | **Weapons** **Grenades** |
| 6 | `PZO22001 Starfinder Player Core 268-281::/page/13/Table/36` | 0.541333 | GrenadeItem LevelPriceDamageElectromag grenade, commercial0101d8 EFrag grenade, commercial0101d8 PIncendiary grenade, commercial0101d8 FFlash grenade, commercial010–Smoke grenade, commercial010–Electr |
| 7 | `PZO22001 Starfinder Player Core 268-281::/page/9/Text/37` | 0.506889 | **Grenades** |
| 8 | `PZO22001 Starfinder Player Core 268-281::/page/11/Text/53` | 0.506889 | **Grenades** |
| 9 | `PZO22001 Starfinder Player Core 268-281::/page/13/Text/53` | 0.506889 | **Grenades** |
| 10 | `PZO22001 Starfinder Player Core 268-281::/page/12/SectionHeader/37` | 0.506685 | **FRAG GRENADE** **ITEM 0+** |
