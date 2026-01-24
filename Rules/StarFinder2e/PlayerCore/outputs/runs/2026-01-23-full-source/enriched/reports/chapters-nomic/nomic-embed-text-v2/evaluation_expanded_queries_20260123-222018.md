# RulesLawyer Evaluation Report: nomic-embed-text-v2

## Summary
- Run ID: `2026-01-23-full-source`
- Ruleset ID: `None`
- Document ID: `None`
- Chunk source: `enriched`
- Chunk count: `23248`
- Query count: `200`
- Evaluated queries: `77`
- Coverage: `0.3850`
- MRR: `0.8849`
- hit@1: `0.8312`
- hit@3: `0.9221`
- hit@5: `0.9351`
- hit@10: `0.9610`
- Embeddings reused: `True`
- Graph boost: `0.05` (depth=2, top_k=50, source=top, seed_top_n=3, same_kind_only=False, decay=0.4)
- Chapter routing: `top_n=3` (source=summary, chapters=29, avg_allowed_chunks=2736.09, expected_recall=0.385)

### Expanded Gold Metrics
- Coverage: `0.3850`
- MRR: `0.8849`
- hit@1: `0.8312`
- hit@3: `0.9221`
- hit@5: `0.9351`
- hit@10: `0.9610`

### Expanded Gold Expansion Stats
- Queries with additions: `200`
- Avg added per query: `2.25`
- Max added: `11`
- Addition reasons:
  - graph_depth_1: `449`

### Expanded Gold Delta (Expanded - Strict)
- Coverage Δ: `0.0000`
- MRR Δ: `0.0000`
- hit@1 Δ: `0.0000`
- hit@3 Δ: `0.0000`
- hit@5 Δ: `0.0000`
- hit@10 Δ: `0.0000`

### Expanded Gold Note
- Expanded gold metrics match strict metrics (no change).

## Timings (ms)
- Embedding (chunks): `0`
- Embedding (queries): `3944`
- Evaluation (strict): `1099`
- Evaluation (expanded): `1076`
- Total: `12797`

### Timing Estimates (ms)
- Evaluation (strict): `919`
- Evaluation (expanded): `960`
- Total: `5823`

## Query Details
### Query 0
- Text: What is the rule about Boosters attached to your armor allow you to fly.?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 268-281::/page/2/Text/28']
- Expected found: `True`
- Expected rank: `1`
- Routed chapters:
  - PZO22001 Starfinder Player Core 268-281: `0.3929`
  - PZO22001 Starfinder Player Core 232-249: `0.3493`
  - PZO22001 Starfinder Player Core 250-267: `0.3101`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 268-281::/page/2/Text/28', 'merged::PZO22001 Starfinder Player Core 268-281::/page/2/Text/27', 'merged::PZO22001 Starfinder Player Core 268-281::/page/2/Text/29']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 268-281::/page/2/Text/27` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 268-281::/page/2/Text/29` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 268-281::/page/2/Text/28` | 0.864596 | Boosters attached to your armor allow you to fly. |
| 2 | `merged::PZO22001 Starfinder Player Core 268-281::/page/2/Text/38` | 0.596672 | Boosters attached to your armor supercharge your leap. |
| 3 | `merged::PZO22001 Starfinder Player Core 232-249::/page/16/TableCell/209` | 0.440801 | Freebooter Armor |
| 4 | `merged::PZO22001 Starfinder Player Core 232-249::/page/12/Text/2` | 0.437326 | Armor increases your character's defenses, but some medium or heavy armor can hamper movement.  If you want to increase your character's defense beyond the protection their armor provides, they  can u |
| 5 | `merged::PZO22001 Starfinder Player Core 268-281::/page/6/Text/23` | 0.433248 | When you make a thrown Strike with this weapon, a complex  combination of stabilizers and boosters propels it back  into your free hand (or other appendage) after the Strike is  complete. If your hand |
| 6 | `merged::PZO22001 Starfinder Player Core 232-249::/page/13/Text/28` | 0.431136 | **Flexible:** The armor is flexible enough that it doesn't  hinder most actions. You don't apply its check penalty to  Acrobatics or Athletics checks. |
| 7 | `merged::PZO22001 Starfinder Player Core 232-249::/page/14/Text/23` | 0.426084 | **Freebooter** **Armor:** Freebooter armor is named for the  pirates and outlaws who often wear these outfits. Freebooter  armor typically consists of a breastplate worn under a  jacket or flight suit |
| 8 | `merged::PZO22001 Starfinder Player Core 232-249::/page/13/Text/8` | 0.423692 | This number is the maximum amount of your Dexterity  modifier that can apply to your AC while you are wearing  a given suit of armor. For example, if you have a Dexterity  modifier of +4 and you are w |
| 9 | `merged::PZO22001 Starfinder Player Core 268-281::/page/2/Text/29` | 0.420977 | **Activate—Fly** [one-action] (manipulate) **Effect** You activate a jetpack to  gain a fly Speed of 20 feet. This effect lasts for 1 minute or  until you Dismiss it. You can use an action to Fly 0 fe |
| 10 | `merged::PZO22001 Starfinder Player Core 268-281::/page/2/Text/32` | 0.417034 | Increase the fly Speed of your jetpack to 40 feet. You aren't  off-guard while hovering in place. |

### Query 1
- Text: Summarize **Languages** **CLASSES**
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 040-057::/page/1/Text/52']
- Expected found: `True`
- Expected rank: `1`
- Routed chapters:
  - PZO22001 Starfinder Player Core 040-057: `0.3832`
  - PZO22001 Starfinder Player Core 092-097: `0.3656`
  - PZO22001 Starfinder Player Core 014-029: `0.3457`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 040-057::/page/1/Text/52', 'merged::PZO22001 Starfinder Player Core 040-057::/page/1/Text/51', 'merged::PZO22001 Starfinder Player Core 040-057::/page/1/Text/53']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 040-057::/page/1/Text/51` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 040-057::/page/1/Text/53` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 040-057::/page/1/Text/52` | 0.903496 | **Languages** **CLASSES** |
| 2 | `merged::PZO22001 Starfinder Player Core 040-057::/page/11/Text/45` | 0.718334 | **CLASSES** |
| 3 | `merged::PZO22001 Starfinder Player Core 040-057::/page/13/Text/77` | 0.718334 | **CLASSES** |
| 4 | `merged::PZO22001 Starfinder Player Core 014-029::/page/11/Text/33` | 0.718334 | **CLASSES** |
| 5 | `merged::PZO22001 Starfinder Player Core 014-029::/page/13/Text/8` | 0.718334 | **CLASSES** |
| 6 | `merged::PZO22001 Starfinder Player Core 014-029::/page/9/Text/30` | 0.718334 | **CLASSES** |
| 7 | `merged::PZO22001 Starfinder Player Core 040-057::/page/15/Text/48` | 0.718334 | **CLASSES** |
| 8 | `merged::PZO22001 Starfinder Player Core 040-057::/page/9/Text/67` | 0.718334 | **CLASSES** |
| 9 | `merged::PZO22001 Starfinder Player Core 040-057::/page/17/Text/72` | 0.718334 | **CLASSES** |
| 10 | `merged::PZO22001 Starfinder Player Core 092-097::/page/5/Text/36` | 0.718334 | **CLASSES** |

### Query 2
- Text: Summarize ADDITIONAL DEVELOPMENT
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 001-013::/page/1/SectionHeader/2']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 268-281: `0.3251`
  - PZO22001 Starfinder Player Core 282-293: `0.3043`
  - PZO22001 Starfinder Player Core 014-029: `0.2857`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 001-013::/page/1/SectionHeader/2', 'merged::PZO22001 Starfinder Player Core 001-013::/page/1/Text/1', 'merged::PZO22001 Starfinder Player Core 001-013::/page/1/Text/3']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 001-013::/page/1/Text/1` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 001-013::/page/1/Text/3` (reasons: ['graph_depth_1'])

### Query 3
- Text: What is the rule about The illusion can cause damage by making the target believe  the illusion's attacks are real, but it cannot otherwise directly  affect the physical world. If the illusory creature hits with a  Strike, the target takes 3d4 mental damage. The illusion's  Strikes are nonlethal. If the damage doesn't correspond to  the image of the monster—for example, if an illusory Large  dragon deals only 5 damage—the GM might allow the target  to attempt an immediate Perception check to disbelieve the  spell. Any relevant resistances and weaknesses apply if the  target thinks they do, as judged by the GM. For example, if  the illusion wields a doshko and attacks a creature resistant to  piercing damage, the creature would take less mental damage.  However, illusory damage does not deactivate regeneration or  trigger other effects that require a certain damage type. The  GM should track illusory damage dealt by the illusion.?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 330-363::/page/9/Text/4']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 182-209: `0.4523`
  - PZO22001 Starfinder Player Core 424-441: `0.4345`
  - PZO22001 Starfinder Player Core 388-405: `0.4118`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 330-363::/page/9/Text/4', 'merged::PZO22001 Starfinder Player Core 330-363::/page/9/Text/5', 'merged::PZO22001 Starfinder Player Core 330-363::/page/9/Text/3']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 330-363::/page/9/Text/5` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 330-363::/page/9/Text/3` (reasons: ['graph_depth_1'])

### Query 4
- Text: Summarize DURING SOCIAL ENCOUNTERS...
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/12']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 424-441: `0.2570`
  - PZO22001 Starfinder Player Core 098-113: `0.2388`
  - PZO22001 Starfinder Player Core 001-013: `0.2179`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/12', 'merged::PZO22001 Starfinder Player Core 114-125::/page/1/Text/11', 'merged::PZO22001 Starfinder Player Core 114-125::/page/1/Text/13']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 114-125::/page/1/Text/11` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 114-125::/page/1/Text/13` (reasons: ['graph_depth_1'])

### Query 5
- Text: What is the rule about If something isn't listed in your character's class entry,  their proficiency rank in that statistic is untrained unless  they gain training from another source. If your character  is untrained in something, you add a proficiency bonus of  +0 when attempting a check or calculating a DC related to  that statistic.?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 098-113::/page/2/Text/8']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 182-209: `0.5240`
  - PZO22001 Starfinder Player Core 210-231: `0.4664`
  - PZO22001 Starfinder Player Core 092-097: `0.4400`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 098-113::/page/2/Text/8', 'merged::PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/9', 'merged::PZO22001 Starfinder Player Core 098-113::/page/2/Text/7']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/9` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 098-113::/page/2/Text/7` (reasons: ['graph_depth_1'])

### Query 6
- Text: Summarize **Barathu** **Human**
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 092-097::/page/1/Text/48']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 058-073: `0.3539`
  - PZO22001 Starfinder Player Core 040-057: `0.3475`
  - PZO22001 Starfinder Player Core 074-091: `0.3042`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 092-097::/page/1/Text/48', 'merged::PZO22001 Starfinder Player Core 092-097::/page/1/Text/47', 'merged::PZO22001 Starfinder Player Core 092-097::/page/1/Text/49']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 092-097::/page/1/Text/47` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 092-097::/page/1/Text/49` (reasons: ['graph_depth_1'])

### Query 7
- Text: What is the rule about Prioritize learning and diplomacy if you're a damaya, or  physique and tactical prowess if you're a korasha—or if  you're an unbound lashunta, you have different priorities.?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 058-073::/page/1/ListItem/3']
- Expected found: `True`
- Expected rank: `1`
- Routed chapters:
  - PZO22001 Starfinder Player Core 058-073: `0.4559`
  - PZO22001 Starfinder Player Core 210-231: `0.3895`
  - PZO22001 Starfinder Player Core 040-057: `0.3615`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 058-073::/page/1/ListItem/3', 'merged::PZO22001 Starfinder Player Core 058-073::/page/1/ListItem/2', 'merged::PZO22001 Starfinder Player Core 058-073::/page/1/ListItem/4']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 058-073::/page/1/ListItem/2` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 058-073::/page/1/ListItem/4` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 058-073::/page/1/ListItem/3` | 0.935610 | Prioritize learning and diplomacy if you're a damaya, or  physique and tactical prowess if you're a korasha—or if  you're an unbound lashunta, you have different priorities. |
| 2 | `merged::PZO22001 Starfinder Player Core 040-057::/page/16/Text/21` | 0.598314 | You've studied the kasathan traditions of balance  and harmony. You gain the trained proficiency  rank in Diplomacy and Society. If you would  automatically become trained in one of those skills  (fro |
| 3 | `merged::PZO22001 Starfinder Player Core 058-073::/page/1/Text/25` | 0.590009 | You've chosen the adaptive genetics to become a damaya. You  might have a leaner, lither body type than other lashuntas and  are likely encouraged to pursue work as a scholar or politician.  In additi |
| 4 | `merged::PZO22001 Starfinder Player Core 058-073::/page/2/Text/31` | 0.519001 | You've studied the lives and achievements of other  lashuntas who have improved both their psychic powers  and their communities. You gain the trained proficiency  rank in Occultism and Society. If yo |
| 5 | `merged::PZO22001 Starfinder Player Core 058-073::/page/1/Text/13` | 0.513964 | Around puberty, lashuntas traditionally choose whether  to express damaya or korasha genetics—a decision that  determines their physical development and influences their  potential societal roles. Las |
| 6 | `merged::PZO22001 Starfinder Player Core 058-073::/page/1/Text/27` | 0.502198 | You've chosen the adaptive genetics to become a korasha. You  might be stockier and more muscular than other lashuntas. |
| 7 | `merged::PZO22001 Starfinder Player Core 058-073::/page/1/Text/12` | 0.500387 | Damayas tend to be tall and graceful with delicate features and  are traditionally pushed toward artistic or intellectual pursuits  and political occupations. Korashas are shorter, more muscular,  and |
| 8 | `merged::PZO22001 Starfinder Player Core 058-073::/page/2/Text/3` | 0.498280 | You decided against activating your ancestry's adaptive  genetics. You might show a combination of damaya and  korasha traits; you might be tall and muscular or short and  lithe, or perhaps you have u |
| 9 | `merged::PZO22001 Starfinder Player Core 058-073::/page/11/Text/4` | 0.493477 | Your ability to adapt to various beliefs instills you with  knowledge of many cultures. You gain the trained proficiency  rank in Diplomacy and Society. If you would automatically  become trained in o |
| 10 | `merged::PZO22001 Starfinder Player Core 058-073::/page/3/Text/8` | 0.492525 | **Prerequisites** korasha lashunta or unbound lashunta heritage You can leverage your telepathic abilities to influence the  minds of others, imparting orders or inflaming fears. You can  cast *comman |

### Query 8
- Text: What does **HOWL **[two-actions] **SPELL 7** do?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 330-363::/page/7/Text/32']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 406-423: `0.3343`
  - PZO22001 Starfinder Player Core 182-209: `0.3035`
  - PZO22001 Starfinder Player Core 388-405: `0.2901`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 330-363::/page/7/Text/32', 'merged::PZO22001 Starfinder Player Core 330-363::/page/7/Text/74', 'merged::PZO22001 Starfinder Player Core 330-363::/page/7/Text/21']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 330-363::/page/7/Text/74` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 330-363::/page/7/Text/21` (reasons: ['graph_depth_1'])

### Query 9
- Text: What is the rule about HIT POINTS?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 040-057::/page/1/SectionHeader/14']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 388-405: `0.2991`
  - PZO22001 Starfinder Player Core 250-267: `0.2751`
  - PZO22001 Starfinder Player Core 406-423: `0.2369`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 040-057::/page/1/SectionHeader/14', 'merged::PZO22001 Starfinder Player Core 040-057::/page/1/Text/15', 'merged::PZO22001 Starfinder Player Core 040-057::/page/1/Text/13']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 040-057::/page/1/Text/15` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 040-057::/page/1/Text/13` (reasons: ['graph_depth_1'])

### Query 10
- Text: What is the rule about Other heightened entries give a number after a plus sign,  indicating that heightening grants extra advantages over  multiple ranks. The listed effect applies for every increment  of ranks by which the spell is heightened above its lowest  spell rank, and the benefit is cumulative. For example, *slice * *reality* says "**Heightened (+1)** The damage increases by 1d8."  Because *slice reality* deals 7d8 void damage at 6th rank, a  7th-rank *slice reality* would deal 8d8 void damage, an 8thrank spell would deal 9d8 void damage, and so on.?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 294-329::/page/2/Text/3']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 364-387: `0.4554`
  - PZO22001 Starfinder Player Core 182-209: `0.4460`
  - PZO22001 Starfinder Player Core 282-293: `0.4399`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 294-329::/page/2/Text/3', 'merged::PZO22001 Starfinder Player Core 294-329::/page/2/Text/2', 'merged::PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/4']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 294-329::/page/2/Text/2` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/4` (reasons: ['graph_depth_1'])

### Query 11
- Text: What is the rule about actions, you can't use any special abilities, reactions, or free  actions that trigger when you Recall Knowledge.?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 330-363::/page/8/Text/26']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 406-423: `0.4854`
  - PZO22001 Starfinder Player Core 182-209: `0.4145`
  - PZO22001 Starfinder Player Core 210-231: `0.4121`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 330-363::/page/8/Text/26', 'merged::PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/27', 'merged::PZO22001 Starfinder Player Core 330-363::/page/8/Text/25']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/27` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 330-363::/page/8/Text/25` (reasons: ['graph_depth_1'])

### Query 12
- Text: Lookup values for Stealth Skill FeatsLevelPrerequisitesBenefitsExperienced Smuggler1Trained in StealthConceal items from observers more effectivelyTerrain Stalker1Trained in StealthSneak in certain terrain without attempting a checkQuiet Allies2Expert in StealthRoll a single Stealth check when sneaking with alliesFoil Senses7Master in StealthTake precautions against special sensesSwift Sneak7Master in StealthMove your full Speed while you SneakLegendary Sneak15Legendary in Stealth, Swift
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 210-231::/page/5/Table/2']
- Expected found: `True`
- Expected rank: `1`
- Routed chapters:
  - PZO22001 Starfinder Player Core 210-231: `0.5464`
  - PZO22001 Starfinder Player Core 424-441: `0.5081`
  - PZO22001 Starfinder Player Core 182-209: `0.4878`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 210-231::/page/5/Table/2', 'merged::PZO22001 Starfinder Player Core 210-231::/page/5/TableCell/543', 'merged::PZO22001 Starfinder Player Core 210-231::/page/5/TableCell/544']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 210-231::/page/5/TableCell/543` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 210-231::/page/5/TableCell/544` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 210-231::/page/5/Table/2` | 0.945059 | Stealth Skill FeatsLevelPrerequisitesBenefitsExperienced Smuggler1Trained in StealthConceal items from observers more effectivelyTerrain Stalker1Trained in StealthSneak in certain terrain without atte |
| 2 | `merged::PZO22001 Starfinder Player Core 210-231::/page/5/Table/1` | 0.663616 | Society Skill FeatsLevelPrerequisitesBenefitsMultilingual1Trained in SocietyLearn two new languagesPlant Rumor1Trained in SocietyArgue by damaging reputationRead Lips1Trained in SocietyRead the lips o |
| 3 | `merged::PZO22001 Starfinder Player Core 210-231::/page/13/Text/41` | 0.661360 | **Prerequisites** legendary in Stealth, Swift Sneak |
| 4 | `merged::PZO22001 Starfinder Player Core 210-231::/page/5/Table/3` | 0.657331 | Survival Skill FeatsLevelPrerequisitesBenefitsExperienced Tracker1Trained in SurvivalTrack at your full Speed at a –5 penaltySurvey Wildlife1Trained in SurvivalIdentify nearby creatures through signs |
| 5 | `merged::PZO22001 Starfinder Player Core 424-441::/page/1/Text/18` | 0.655166 | The Stealth skill is designed to use Hide for avoiding  visual detection and Avoid Notice and Sneak to avoid  being both seen and heard. For many special senses,  a player can describe how they're avo |
| 6 | `merged::PZO22001 Starfinder Player Core 210-231::/page/5/TableCell/536` | 0.646724 | Stealth Skill Feats |
| 7 | `merged::PZO22001 Starfinder Player Core 210-231::/page/5/TableCell/544` | 0.646724 | Stealth Skill Feats |
| 8 | `merged::PZO22001 Starfinder Player Core 210-231::/page/5/Table/4` | 0.644543 | Thievery Skill FeatsLevelPrerequisitesBenefitsPickpocket1Trained in ThieverySteal or Palm an Object more effectivelySubtle Theft1Trained in ThieveryYour thefts are harder to noticeWary Disarmament2Exp |
| 9 | `merged::PZO22001 Starfinder Player Core 210-231::/page/5/TableCell/570` | 0.625331 | Legendary in Stealth, Swift Sneak |
| 10 | `merged::PZO22001 Starfinder Player Core 210-231::/page/2/Table/1` | 0.622912 | Varying Skill FeatsLevelPrerequisitesBenefitsRecognize Spell1Trained in Arcana, Nature, Occultism, or ReligionIdentify a spell as a reaction as it's being castSeasoned1Trained in Alcohol Lore, Cooking |

### Query 13
- Text: Summarize **CLASSES**
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 030-039::/page/1/Text/34']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 098-113: `0.3661`
  - PZO22001 Starfinder Player Core 182-209: `0.3335`
  - PZO22001 Starfinder Player Core 014-029: `0.3334`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 030-039::/page/1/Text/34', 'merged::PZO22001 Starfinder Player Core 030-039::/page/7/Text/86', 'merged::PZO22001 Starfinder Player Core 030-039::/page/5/Text/58', 'merged::PZO22001 Starfinder Player Core 030-039::/page/1/Text/33', 'merged::PZO22001 Starfinder Player Core 030-039::/page/1/Text/35', 'merged::PZO22001 Starfinder Player Core 030-039::/page/3/Text/37', 'merged::PZO22001 Starfinder Player Core 030-039::/page/9/Text/47']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 030-039::/page/7/Text/86` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 030-039::/page/5/Text/58` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 030-039::/page/1/Text/33` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 030-039::/page/1/Text/35` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 030-039::/page/3/Text/37` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 030-039::/page/9/Text/47` (reasons: ['graph_depth_1'])

### Query 14
- Text: Summarize HARDNESS
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 250-267::/page/0/SectionHeader/11']
- Expected found: `True`
- Expected rank: `1`
- Routed chapters:
  - PZO22001 Starfinder Player Core 250-267: `0.3548`
  - PZO22001 Starfinder Player Core 388-405: `0.2948`
  - PZO22001 Starfinder Player Core 424-441: `0.2921`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 250-267::/page/0/SectionHeader/11', 'merged::PZO22001 Starfinder Player Core 250-267::/page/0/Text/12', 'merged::PZO22001 Starfinder Player Core 250-267::/page/0/Text/10']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 250-267::/page/0/Text/12` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 250-267::/page/0/Text/10` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 250-267::/page/0/SectionHeader/11` | 0.898501 | HARDNESS |
| 2 | `merged::PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/627` | 0.738844 | Hardness |
| 3 | `merged::PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/697` | 0.738844 | Hardness |
| 4 | `merged::PZO22001 Starfinder Player Core 250-267::/page/0/Text/12` | 0.508008 | Whenever a shield takes damage, the amount of damage it  takes is reduced by this amount. This number is particularly  relevant for shields because of the Shield Block feat (page  228). The rules for |
| 5 | `merged::PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/13` | 0.481498 | DARKNESS |
| 6 | `merged::PZO22001 Starfinder Player Core 388-405::/page/12/SectionHeader/15` | 0.463557 | WEAKNESS |
| 7 | `merged::PZO22001 Starfinder Player Core 388-405::/page/12/SectionHeader/1` | 0.402042 | IMMUNITY, WEAKNESS,  AND RESISTANCE |
| 8 | `merged::PZO22001 Starfinder Player Core 388-405::/page/10/ListItem/8` | 0.386060 | 3. Apply **immunities**, **weaknesses**, and **resistances **the  subject has to the damage. |
| 9 | `merged::PZO22001 Starfinder Player Core 250-267::/page/0/Text/22` | 0.379632 | **Hefty:** This shield is so heavy that raising it takes more  effort. Raising a Shield with the hefty trait is a 2-action  activity unless your Strength modifier equals or exceeds  the number with th |
| 10 | `merged::PZO22001 Starfinder Player Core 388-405::/page/14/Text/15` | 0.363346 | Items have Hit Points like creatures, but the rules for  damaging them are different, as explained on page 236. An  item has a Hardness statistic that reduces damage the item  takes by that amount. Th |

### Query 15
- Text: Summarize DURING COMBAT ENCOUNTERS...
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/12']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 424-441: `0.3437`
  - PZO22001 Starfinder Player Core 150-161: `0.2947`
  - PZO22001 Starfinder Player Core 098-113: `0.2817`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/12', 'merged::PZO22001 Starfinder Player Core 162-173::/page/1/Text/11', 'merged::PZO22001 Starfinder Player Core 162-173::/page/1/Text/13']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 162-173::/page/1/Text/11` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 162-173::/page/1/Text/13` (reasons: ['graph_depth_1'])

### Query 16
- Text: What is the rule about CHARACTER CREATION17?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/132']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 014-029: `0.4367`
  - PZO22001 Starfinder Player Core 442-464: `0.4115`
  - PZO22001 Starfinder Character Sheet: `0.3936`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/132', 'merged::PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/134', 'merged::PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/130']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/134` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/130` (reasons: ['graph_depth_1'])

### Query 17
- Text: Summarize **BASED ON THE DESIGN WORK OF **
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 001-013::/page/1/SectionHeader/22']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 388-405: `0.2810`
  - PZO22001 Starfinder Player Core 040-057: `0.2342`
  - PZO22001 Starfinder Player Core 182-209: `0.2316`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 001-013::/page/1/SectionHeader/22', 'merged::PZO22001 Starfinder Player Core 001-013::/page/1/Text/21', 'merged::PZO22001 Starfinder Player Core 001-013::/page/1/Text/23']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 001-013::/page/1/Text/21` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 001-013::/page/1/Text/23` (reasons: ['graph_depth_1'])

### Query 18
- Text: What is the rule about An android bounty hunter, pursuing dangerous criminals  and rogue virtual intelligences across the planet.?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/20']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 001-013: `0.4022`
  - PZO22001 Starfinder Player Core 388-405: `0.3914`
  - PZO22001 Starfinder Player Core 294-329: `0.3639`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/20', 'merged::PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/21', 'merged::PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/19']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/21` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/19` (reasons: ['graph_depth_1'])

### Query 19
- Text: What is the rule about You're one among many professionals working in the  corporate world, but you're not just any suit. You're a  negotiator, dealmaker, or perhaps even a spy working to  advance a particular corporation's agenda. You might be a cog  in a corporation's massive machine or a shill for an up-andcoming entrepreneur no one has heard of... yet.?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 092-097::/page/1/Text/28']
- Expected found: `True`
- Expected rank: `1`
- Routed chapters:
  - PZO22001 Starfinder Player Core 092-097: `0.3854`
  - PZO22001 Starfinder Player Core 098-113: `0.3738`
  - PZO22001 Starfinder Player Core 182-209: `0.3583`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 092-097::/page/1/Text/28', 'merged::PZO22001 Starfinder Player Core 092-097::/page/1/Text/29', 'merged::PZO22001 Starfinder Player Core 092-097::/page/1/SectionHeader/27']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 092-097::/page/1/Text/29` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 092-097::/page/1/SectionHeader/27` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 092-097::/page/1/Text/28` | 0.938393 | You're one among many professionals working in the  corporate world, but you're not just any suit. You're a  negotiator, dealmaker, or perhaps even a spy working to  advance a particular corporation's |
| 2 | `merged::PZO22001 Starfinder Player Core 098-113::/page/5/Text/2` | 0.599543 | You're a master influencer. You make your way in the universe with a charming smile, quick wit, and keen  sense of self-preservation. You're a leader who motivates your teammates, pushes them past the |
| 3 | `merged::PZO22001 Starfinder Player Core 098-113::/page/5/Text/17` | 0.590647 | You look for new opportunities to make a name for yourself, work your way up  through the ranks of an organization, or establish an enterprise of your own. |
| 4 | `merged::PZO22001 Starfinder Player Core 092-097::/page/1/Text/4` | 0.546687 | You hunt people down for credits. You might work with a  corporation, military, or some other organization. |
| 5 | `merged::PZO22001 Starfinder Player Core 092-097::/page/3/Text/28` | 0.545836 | You work in a lab and conduct research about a scientific  topic. Perhaps you're a biotechnician, chemist, computer  programmer, theoretical physicist, or accomplished  researcher in some other field. |
| 6 | `merged::PZO22001 Starfinder Player Core 092-097::/page/2/Text/30` | 0.535084 | You're a con artist and trickster who swindles unsuspecting  dupes and blackmails rubes, but it's nothing personal you're just in it for the credits. You might run an operation  on the side, or you mi |
| 7 | `merged::PZO22001 Starfinder Player Core 092-097::/page/2/Text/6` | 0.533113 | You're an accomplished healer expertly using the latest tech  and pharmaceuticals to treat your patients. You might work  at a clinic, supervise a starship's medbay, serve as a military  medic, or ply |
| 8 | `merged::PZO22001 Starfinder Player Core 098-113::/page/5/Text/13` | 0.531613 | You're often the face for your team, whether you use diplomacy, lies, threats, or  whatever words it takes to get your way. |
| 9 | `merged::PZO22001 Starfinder Player Core 092-097::/page/2/Text/34` | 0.514822 | You've always had a knack for computers and virtual spaces  and pride yourself on your ability to learn technical secrets.  The open networks known as infospheres are your home  and the place you can |
| 10 | `merged::PZO22001 Starfinder Player Core 092-097::/page/4/Text/10` | 0.513707 | You're a crewmate on a pirate vessel with ambitions of  pillaging interstellar shipping lanes or taking over a chunk  of a notable planetary body. Perhaps you grew up on such  a ship, were taken priso |

### Query 20
- Text: Summarize **CONDITIONS ** **APPENDIX**
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 092-097::/page/3/Text/47']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 424-441: `0.3294`
  - PZO22001 Starfinder Player Core 014-029: `0.3252`
  - PZO22001 Starfinder Player Core 250-267: `0.3094`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 092-097::/page/3/Text/47', 'merged::PZO22001 Starfinder Player Core 092-097::/page/1/Text/64', 'merged::PZO22001 Starfinder Player Core 092-097::/page/5/Text/41', 'merged::PZO22001 Starfinder Player Core 092-097::/page/3/Text/46', 'merged::PZO22001 Starfinder Player Core 092-097::/page/3/Text/53']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 092-097::/page/1/Text/64` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 092-097::/page/5/Text/41` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 092-097::/page/3/Text/46` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 092-097::/page/3/Text/53` (reasons: ['graph_depth_1'])

### Query 21
- Text: What is the rule about Some skill activities have the exploration or downtime trait.  Exploration activities usually take a minute or more, while  downtime activities may take a day or more. They usually  can't be used during an encounter, though the GM might  bend this restriction. If you're not sure whether you have the  time to use one of these activities, ask your GM.?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 182-209::/page/2/Text/12']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 388-405: `0.5111`
  - PZO22001 Starfinder Player Core 424-441: `0.4778`
  - PZO22001 Starfinder Player Core 406-423: `0.4647`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 182-209::/page/2/Text/12', 'merged::PZO22001 Starfinder Player Core 182-209::/page/2/SectionHeader/13', 'merged::PZO22001 Starfinder Player Core 182-209::/page/2/SectionHeader/11']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 182-209::/page/2/SectionHeader/13` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 182-209::/page/2/SectionHeader/11` (reasons: ['graph_depth_1'])

### Query 22
- Text: Summarize —
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/653']
- Expected found: `True`
- Expected rank: `2`
- Routed chapters:
  - PZO22001 Starfinder Player Core 014-029: `0.3008`
  - PZO22001 Starfinder Player Core 250-267: `0.3003`
  - PZO22001 Starfinder Player Core 150-161: `0.2668`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/653', 'merged::PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/652', 'merged::PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/654']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/652` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/654` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/703` | 0.522766 | — |
| 2 | `merged::PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/653` | 0.522766 | — |
| 3 | `merged::PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/652` | 0.522766 | — |
| 4 | `merged::PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/704` | 0.522766 | — |
| 5 | `merged::PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/680` | 0.522766 | — |
| 6 | `merged::PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/705` | 0.522766 | — |
| 7 | `merged::PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/679` | 0.522766 | — |
| 8 | `merged::PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/643` | 0.522766 | — |
| 9 | `merged::PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/661` | 0.522766 | — |
| 10 | `merged::PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/702` | 0.522766 | — |

### Query 23
- Text: Summarize **COVER ARTIST **
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 001-013::/page/1/SectionHeader/8']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 092-097: `0.2637`
  - PZO22001 Starfinder Player Core 182-209: `0.2550`
  - PZO22001 Starfinder Player Core 424-441: `0.2403`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 001-013::/page/1/SectionHeader/8', 'merged::PZO22001 Starfinder Player Core 001-013::/page/1/Text/7', 'merged::PZO22001 Starfinder Player Core 001-013::/page/1/Text/9']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 001-013::/page/1/Text/7` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 001-013::/page/1/Text/9` (reasons: ['graph_depth_1'])

### Query 24
- Text: What is the rule about Your character starts with 150 credits.?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 232-249::/page/1/Text/14']
- Expected found: `True`
- Expected rank: `1`
- Routed chapters:
  - PZO22001 Starfinder Player Core 014-029: `0.4391`
  - PZO22001 Starfinder Character Sheet: `0.4005`
  - PZO22001 Starfinder Player Core 232-249: `0.3894`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 232-249::/page/1/Text/14', 'merged::PZO22001 Starfinder Player Core 232-249::/page/1/Text/15', 'merged::PZO22001 Starfinder Player Core 232-249::/page/1/SectionHeader/13']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 232-249::/page/1/Text/15` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 232-249::/page/1/SectionHeader/13` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 232-249::/page/1/Text/14` | 0.867330 | Your character starts with 150 credits. |
| 2 | `merged::PZO22001 Starfinder Player Core 014-029::/page/9/Text/18` | 0.661405 | At 1st level, your character has 150 credits to spend on armor, |
| 3 | `merged::PZO22001 Starfinder Player Core 232-249::/page/1/Text/6` | 0.553037 | Your character starts out with 150 credits to spend on any  common items from this chapter. Credits are a galactic  currency used to barter and trade for goods in the Starfinder  setting. Items with a |
| 4 | `merged::PZO22001 Starfinder Player Core 014-029::/page/9/Text/22` | 0.471659 | Once you've spent your character's starting wealth,  calculate any remaining credits they might still have  and write those amounts in the Inventory section on  the second page. Record your character' |
| 5 | `merged::PZO22001 Starfinder Player Core 232-249::/page/5/TableCell/537` | 0.466433 | 50 credits |
| 6 | `merged::PZO22001 Starfinder Player Core 232-249::/page/5/TableCell/549` | 0.456465 | 180 credits |
| 7 | `merged::PZO22001 Starfinder Player Core 232-249::/page/11/TableCell/885` | 0.456465 | 180 credits |
| 8 | `merged::PZO22001 Starfinder Player Core 232-249::/page/10/Text/7` | 0.454740 | **Type **elite; **Level **15; **Price **13,000 credits |
| 9 | `merged::PZO22001 Starfinder Player Core 232-249::/page/10/Text/49` | 0.450988 | **Price **100 credits |
| 10 | `merged::PZO22001 Starfinder Player Core 232-249::/page/16/TableCell/372` | 0.446922 | 14,000 credits |

### Query 25
- Text: What are the requirements for **OVERCOME SHAME **[free-action] **FEAT 13**?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 074-091::/page/3/SectionHeader/48']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 424-441: `0.3720`
  - PZO22001 Starfinder Player Core 210-231: `0.3594`
  - PZO22001 Starfinder Player Core 014-029: `0.3572`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 074-091::/page/3/SectionHeader/48', 'merged::PZO22001 Starfinder Player Core 074-091::/page/3/Text/50', 'merged::PZO22001 Starfinder Player Core 074-091::/page/3/Text/47']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 074-091::/page/3/Text/50` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 074-091::/page/3/Text/47` (reasons: ['graph_depth_1'])

### Query 26
- Text: What is the rule about **SKILLS**?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 330-363::/page/1/Text/64']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 182-209: `0.5422`
  - PZO22001 Starfinder Player Core 210-231: `0.4266`
  - PZO22001 Starfinder Player Core 442-464: `0.3689`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 330-363::/page/1/Text/64', 'merged::PZO22001 Starfinder Player Core 330-363::/page/1/Text/65', 'merged::PZO22001 Starfinder Player Core 330-363::/page/1/Text/63']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 330-363::/page/1/Text/65` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 330-363::/page/1/Text/63` (reasons: ['graph_depth_1'])

### Query 27
- Text: What is the rule about This nacreous, tapered cylinder provides a breath of air  when you need it most. You can hold your breath for twice  as long, and you gain a +1 item bonus to saves against  inhaled poisons.?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 282-293::/page/1/Text/8']
- Expected found: `True`
- Expected rank: `1`
- Routed chapters:
  - PZO22001 Starfinder Player Core 232-249: `0.2889`
  - PZO22001 Starfinder Player Core 406-423: `0.2878`
  - PZO22001 Starfinder Player Core 282-293: `0.2820`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 282-293::/page/1/Text/8', 'merged::PZO22001 Starfinder Player Core 282-293::/page/1/SectionHeader/7', 'merged::PZO22001 Starfinder Player Core 282-293::/page/1/Text/9']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 282-293::/page/1/SectionHeader/7` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 282-293::/page/1/Text/9` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 282-293::/page/1/Text/8` | 0.927823 | This nacreous, tapered cylinder provides a breath of air  when you need it most. You can hold your breath for twice  as long, and you gain a +1 item bonus to saves against  inhaled poisons. |
| 2 | `merged::PZO22001 Starfinder Player Core 232-249::/page/10/Text/17` | 0.470580 | This tiny cylinder contains specialized nanites. Different  types have different effects. |
| 3 | `merged::PZO22001 Starfinder Player Core 282-293::/page/10/Text/36` | 0.428958 | This extra organ assimilates with and enhances your circulatory  and immune systems. When you succeed at a Fortitude save  against an ongoing disease or poison, you recover completely,  regardless of |
| 4 | `merged::PZO22001 Starfinder Player Core 282-293::/page/2/Text/39` | 0.419715 | You can Interact with the *null* *space* *chamber* to stow  items in it or remove them. The *null* *space* *chamber* can be  opened and closed only from the outside. When a *null* *space* *chamber* is |
| 5 | `merged::PZO22001 Starfinder Player Core 282-293::/page/7/Text/15` | 0.419226 | Your skin is biologically engineered to protect your entire  body, including your brain, from harmful effects. You gain a  +1 item bonus to saving throws. |
| 6 | `merged::PZO22001 Starfinder Player Core 282-293::/page/6/Text/31` | 0.407383 | Oxygen-filtering nodules line the outside of your lungs. If you  breathe in water, the gill sheath filters the oxygen into your  lungs. This allows you to breathe underwater or in the air.  You exhale |
| 7 | `merged::PZO22001 Starfinder Player Core 406-423::/page/5/Text/2` | 0.406913 | You avert your gaze from danger. You gain a +2 circumstance  bonus to saves against visual abilities that require you to look at  a creature or object, such as the radiant gaze of a solar nymph.  Your |
| 8 | `merged::PZO22001 Starfinder Player Core 282-293::/page/6/Text/18` | 0.405549 | With cutting edge surgery, you're implanted with an  magical gland modified to function for a creature of your  ancestry at the back of your throat. Choose your breath  weapon's damage type when the o |
| 9 | `merged::PZO22001 Starfinder Player Core 232-249::/page/13/Text/31` | 0.403928 | **Resilient:** This armor has been developed with several  integrated recalibration and defensive systems. While  wearing this armor, you gain an item bonus to saving  throws equal to the listed value |
| 10 | `merged::PZO22001 Starfinder Player Core 232-249::/page/11/Text/2` | 0.402375 | This tangy crimson elixir grants you 1d10+5 temporary Hit  Points, as well as a +5-foot item bonus to any Speed you have  for 1 minute. When you drink this serum, your veins protrude,  and your eyes t |

### Query 28
- Text: What does **CHARM **[two-actions] **SPELL 1** do?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/52']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 406-423: `0.3531`
  - PZO22001 Starfinder Player Core 442-464: `0.3066`
  - PZO22001 Starfinder Player Core 182-209: `0.2995`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/52', 'merged::PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/44', 'merged::PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/6']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/44` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/6` (reasons: ['graph_depth_1'])

### Query 29
- Text: Lookup values for Society Skill FeatsLevelPrerequisitesBenefitsMultilingual1Trained in SocietyLearn two new languagesPlant Rumor1Trained in SocietyArgue by damaging reputationRead Lips1Trained in SocietyRead the lips of people you can seeSign Language1Trained in SocietyLearn sign languagesStreetwise1Trained in SocietyUse Society to Gather Information and Recall KnowledgeLegendary Codebreaker15Legendary in SocietyQuickly Decipher Writing using SocietyLegendary Linguist15Legendary in Society,
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 210-231::/page/5/Table/1']
- Expected found: `True`
- Expected rank: `1`
- Routed chapters:
  - PZO22001 Starfinder Player Core 182-209: `0.4914`
  - PZO22001 Starfinder Player Core 092-097: `0.4858`
  - PZO22001 Starfinder Player Core 210-231: `0.4791`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 210-231::/page/5/Table/1', 'merged::PZO22001 Starfinder Player Core 210-231::/page/5/SectionHeader/0', 'merged::PZO22001 Starfinder Player Core 210-231::/page/5/TableCell/504']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 210-231::/page/5/SectionHeader/0` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 210-231::/page/5/TableCell/504` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 210-231::/page/5/Table/1` | 0.919277 | Society Skill FeatsLevelPrerequisitesBenefitsMultilingual1Trained in SocietyLearn two new languagesPlant Rumor1Trained in SocietyArgue by damaging reputationRead Lips1Trained in SocietyRead the lips o |
| 2 | `merged::PZO22001 Starfinder Player Core 210-231::/page/5/TableCell/531` | 0.643952 | Quickly Decipher Writing using Society |
| 3 | `merged::PZO22001 Starfinder Player Core 182-209::/page/24/Text/22` | 0.632734 | You must be trained in Society to use it to Decipher  Writing. |
| 4 | `merged::PZO22001 Starfinder Player Core 210-231::/page/13/Text/10` | 0.617899 | Your skill with languages and codes is so great you can  decipher information with little more than a quick read  through a text. You can Decipher Writing using Society while  reading at normal speed. |
| 5 | `merged::PZO22001 Starfinder Player Core 210-231::/page/13/Text/14` | 0.602924 | **Prerequisites** legendary in Society, Multilingual |
| 6 | `merged::PZO22001 Starfinder Player Core 210-231::/page/4/Table/1` | 0.590992 | Lore Skill FeatsLevelPrerequisitesBenefitsLegendary Professional15Legendary in LoreGain renown for your LoreMedicine Skill FeatsLevelPrerequisitesBenefitsBattle Medicine1Trained in MedicineHeal yourse |
| 7 | `merged::PZO22001 Starfinder Player Core 210-231::/page/3/Table/1` | 0.589544 | Crafting Skill FeatsLevelPrerequisitesBenefitsQuick Install1Trained in CraftingInstall upgrades quicklyQuick Repair1Trained in CraftingRepair items quicklySerum Crafting1Trained in CraftingCraft serum |
| 8 | `merged::PZO22001 Starfinder Player Core 210-231::/page/5/TableCell/534` | 0.585726 | Legendary in Society, Multilingual |
| 9 | `merged::PZO22001 Starfinder Player Core 092-097::/page/2/Text/20` | 0.582961 | You're trained in the Society skill and a Lore skill related  to one city or region you've visited often. You gain the  Multilingual skill feat. |
| 10 | `merged::PZO22001 Starfinder Player Core 182-209::/page/24/Text/18` | 0.579569 | You understand the people and systems that make organized  society run, and you know the historical events that make  societies what they are today. Further, you can use that  knowledge to navigate th |

### Query 30
- Text: What are the requirements for **SOLDIER'S TRAINING** **FEAT 16**?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/51']
- Expected found: `True`
- Expected rank: `1`
- Routed chapters:
  - PZO22001 Starfinder Player Core 150-161: `0.4928`
  - PZO22001 Starfinder Player Core 210-231: `0.4002`
  - PZO22001 Starfinder Player Core 098-113: `0.3624`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/51', 'merged::PZO22001 Starfinder Player Core 150-161::/page/10/Text/50', 'merged::PZO22001 Starfinder Player Core 150-161::/page/10/Text/53']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 150-161::/page/10/Text/50` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 150-161::/page/10/Text/53` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/51` | 0.854073 | **SOLDIER'S TRAINING** **FEAT 16** |
| 2 | `merged::PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/637` | 0.625061 | Soldier's Training |
| 3 | `merged::PZO22001 Starfinder Player Core 150-161::/page/7/SectionHeader/1` | 0.540927 | **SOLDIER FEATS BY NAME** |
| 4 | `merged::PZO22001 Starfinder Player Core 210-231::/page/18/Text/11` | 0.538490 | **SKILL TRAINING** **FEAT 1** |
| 5 | `merged::PZO22001 Starfinder Player Core 150-161::/page/6/Text/23` | 0.529962 | **SOLDIER** |
| 6 | `merged::PZO22001 Starfinder Player Core 150-161::/page/6/Text/28` | 0.529962 | **SOLDIER** |
| 7 | `merged::PZO22001 Starfinder Player Core 150-161::/page/6/Text/32` | 0.529962 | **SOLDIER** |
| 8 | `merged::PZO22001 Starfinder Player Core 150-161::/page/6/Text/37` | 0.529962 | **SOLDIER** |
| 9 | `merged::PZO22001 Starfinder Player Core 150-161::/page/10/Text/40` | 0.529962 | **SOLDIER** |
| 10 | `merged::PZO22001 Starfinder Player Core 150-161::/page/7/SectionHeader/7` | 0.529962 | **SOLDIER** |

### Query 31
- Text: What is the rule about You're trained in the Crafting skill and the Augmentation  Lore skill. You gain the Augmented Body feat.?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 092-097::/page/1/Text/35']
- Expected found: `True`
- Expected rank: `1`
- Routed chapters:
  - PZO22001 Starfinder Player Core 210-231: `0.5348`
  - PZO22001 Starfinder Player Core 182-209: `0.4959`
  - PZO22001 Starfinder Player Core 092-097: `0.4831`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 092-097::/page/1/Text/35', 'merged::PZO22001 Starfinder Player Core 092-097::/page/1/Text/34', 'merged::PZO22001 Starfinder Player Core 092-097::/page/1/SectionHeader/36']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 092-097::/page/1/Text/34` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 092-097::/page/1/SectionHeader/36` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 092-097::/page/1/Text/35` | 0.918069 | You're trained in the Crafting skill and the Augmentation  Lore skill. You gain the Augmented Body feat. |
| 2 | `merged::PZO22001 Starfinder Player Core 092-097::/page/2/Text/28` | 0.768635 | You're trained in the Crafting skill and the Augmentation or  Life Science Lore skill. You gain the Serum Crafting skill feat. |
| 3 | `merged::PZO22001 Starfinder Player Core 092-097::/page/0/Text/9` | 0.708469 | You're trained in the Crafting skill and the Art Lore skill.  You gain the Specialty Crafting skill feat. |
| 4 | `merged::PZO22001 Starfinder Player Core 092-097::/page/3/Text/30` | 0.666445 | You're trained in the Crafting skill and a Lore skill related  to your field of research. You gain the Assurance skill feat  with that Lore skill. |
| 5 | `merged::PZO22001 Starfinder Player Core 092-097::/page/2/Text/16` | 0.664042 | You're trained in the Crafting skill and the Physical  Science Lore skill. You gain the Electrical Engineer skill feat. |
| 6 | `merged::PZO22001 Starfinder Player Core 092-097::/page/3/Text/22` | 0.623170 | You're trained in the deity's listed divine skill and gain the  Assurance feat with that skill. You are also trained in a Lore  skill related to your deity (Abadar Lore, for example). |
| 7 | `merged::PZO22001 Starfinder Player Core 092-097::/page/2/Text/8` | 0.605267 | You're trained in the Medicine skill and the Life Science  Lore skill. You gain the Battle Medicine skill feat. |
| 8 | `merged::PZO22001 Starfinder Player Core 182-209::/page/1/Text/7` | 0.595552 | A character gains training in certain skills at 1st level:  typically two from their background, a small number of  predetermined skills from their class, and several skills of  your choice granted by |
| 9 | `merged::PZO22001 Starfinder Player Core 092-097::/page/0/Text/3` | 0.581932 | At 1st level, when you create your character, you gain a  background of your choice. This decision is permanent;  you can't change it at later levels. Each background listed  here grants two boosts, u |
| 10 | `merged::PZO22001 Starfinder Player Core 092-097::/page/3/Text/13` | 0.578013 | You're trained in the Intimidation skill and the Underworld  Lore skill. You gain the Intimidating Shot skill feat. |

### Query 32
- Text: What are the requirements for **WARP WOUNDS **[reaction] **FEAT 2**?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 162-173::/page/9/SectionHeader/19']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 210-231: `0.3151`
  - PZO22001 Starfinder Player Core 250-267: `0.3125`
  - PZO22001 Starfinder Player Core 014-029: `0.3071`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 162-173::/page/9/SectionHeader/19', 'merged::PZO22001 Starfinder Player Core 162-173::/page/9/Text/18', 'merged::PZO22001 Starfinder Player Core 162-173::/page/9/Text/21']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 162-173::/page/9/Text/18` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 162-173::/page/9/Text/21` (reasons: ['graph_depth_1'])

### Query 33
- Text: What is the rule about If you have access to the Shield Block reaction (from your  class or from a feat), you can use it while Raising your Shield  to reduce the damage you take by an amount equal to the  shield's Hardness. Both you and the shield then take any  remaining damage.?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 250-267::/page/0/Text/6']
- Expected found: `True`
- Expected rank: `1`
- Routed chapters:
  - PZO22001 Starfinder Player Core 250-267: `0.5376`
  - PZO22001 Starfinder Player Core 406-423: `0.4098`
  - PZO22001 Starfinder Player Core 210-231: `0.3880`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 250-267::/page/0/Text/6', 'merged::PZO22001 Starfinder Player Core 250-267::/page/0/Text/5', 'merged::PZO22001 Starfinder Player Core 250-267::/page/0/SectionHeader/7']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 250-267::/page/0/Text/5` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 250-267::/page/0/SectionHeader/7` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 250-267::/page/0/Text/6` | 0.940183 | If you have access to the Shield Block reaction (from your  class or from a feat), you can use it while Raising your Shield  to reduce the damage you take by an amount equal to the  shield's Hardness. |
| 2 | `merged::PZO22001 Starfinder Player Core 250-267::/page/0/Text/12` | 0.692019 | Whenever a shield takes damage, the amount of damage it  takes is reduced by this amount. This number is particularly  relevant for shields because of the Shield Block feat (page  228). The rules for |
| 3 | `merged::PZO22001 Starfinder Player Core 210-231::/page/18/Text/5` | 0.690248 | You snap your shield in place to ward off a blow. Your shield  prevents you from taking an amount of damage up to the  shield's Hardness. You and the shield each take any remaining  damage, possibly b |
| 4 | `merged::PZO22001 Starfinder Player Core 250-267::/page/0/Text/2` | 0.669696 | A shield can increase your character's defense beyond the protection their armor provides. Your  character must be wielding a shield in one hand to make use of it, and it grants its bonus to AC only |
| 5 | `merged::PZO22001 Starfinder Player Core 406-423::/page/5/Text/38` | 0.630447 | You position your shield to protect yourself. When you've  Raised a Shield, you gain its listed circumstance bonus to AC.  Your shield remains raised until the start of your next turn. |
| 6 | `merged::PZO22001 Starfinder Player Core 250-267::/page/1/Text/8` | 0.627323 | bonus to your AC, the shield upgrade emits an inertial  dampening barrier, and you automatically Raise a Shield.  You can't Raise a Shield installed as a weapon upgrade any  other way. If you use the |
| 7 | `merged::PZO22001 Starfinder Player Core 250-267::/page/0/Text/4` | 0.616303 | Raise a Shield is the action most commonly used with shields.  Most shields must be held in one hand, so you can't hold  anything with that hand and Raise a Shield, and you lose its  benefits if that |
| 8 | `merged::PZO22001 Starfinder Player Core 250-267::/page/0/Text/10` | 0.611484 | A shield grants a circumstance bonus to AC, but only when  the shield is raised. This requires using the Raise a Shield  action, found on page 411. |
| 9 | `merged::PZO22001 Starfinder Player Core 250-267::/page/0/Text/14` | 0.568584 | This column lists the shield's Hit Points (HP) and Broken  Threshold (BT). These measure how much damage the shield  can take before it's destroyed (its total HP) and how much it  can take before bein |
| 10 | `merged::PZO22001 Starfinder Player Core 210-231::/page/18/Text/4` | 0.564316 | **Trigger** While you have your shield raised, you would take  physical damage (bludgeoning, piercing, or slashing) from  an attack. |

### Query 34
- Text: Summarize Assume you view the universe through the lens of your connection.
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 114-125::/page/1/ListItem/25']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 030-039: `0.3446`
  - PZO22001 Starfinder Player Core 058-073: `0.3262`
  - PZO22001 Starfinder Player Core 294-329: `0.3158`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 114-125::/page/1/ListItem/25', 'merged::PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/26', 'merged::PZO22001 Starfinder Player Core 114-125::/page/1/ListItem/24']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/26` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 114-125::/page/1/ListItem/24` (reasons: ['graph_depth_1'])

### Query 35
- Text: What is the rule about You have to spend all the actions of an activity at once  to gain its effects. In an encounter, this means you must  complete it during your turn. If an activity gets interrupted or  disrupted in an encounter (page 407), you lose all the actions  you committed to it.?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 406-423::/page/0/Text/22']
- Expected found: `True`
- Expected rank: `1`
- Routed chapters:
  - PZO22001 Starfinder Player Core 406-423: `0.5537`
  - PZO22001 Starfinder Player Core 388-405: `0.4893`
  - PZO22001 Starfinder Player Core 424-441: `0.4605`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 406-423::/page/0/Text/22', 'merged::PZO22001 Starfinder Player Core 406-423::/page/0/Text/21', 'merged::PZO22001 Starfinder Player Core 406-423::/page/0/SectionHeader/23']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 406-423::/page/0/Text/21` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 406-423::/page/0/SectionHeader/23` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 406-423::/page/0/Text/22` | 0.949043 | You have to spend all the actions of an activity at once  to gain its effects. In an encounter, this means you must  complete it during your turn. If an activity gets interrupted or  disrupted in an e |
| 2 | `merged::PZO22001 Starfinder Player Core 406-423::/page/1/Text/18` | 0.756478 | case of an activity, you usually lose all actions spent for the  activity up through the end of that turn. For instance, if you  began to Cast a Spell requiring 3 actions and the first action  was dis |
| 3 | `merged::PZO22001 Starfinder Player Core 424-441::/page/4/Text/24` | 0.722352 | Activities that take longer than a turn can't normally be  performed during an encounter. Spells with a casting time of  1 minute or more are a common example, as are several skill  actions. When you |
| 4 | `merged::PZO22001 Starfinder Player Core 406-423::/page/0/Text/25` | 0.674626 | If an activity outside of an encounter is interrupted or  disrupted, as described in Disrupting Actions on page 407,  you usually lose the time you put in, but no additional time. |
| 5 | `merged::PZO22001 Starfinder Player Core 406-423::/page/0/Text/6` | 0.674193 | You'll need to track your actions carefully in an encounter. At  the start of each turn you take in an encounter, you regain 3  actions and 1 reaction to spend that round. (Regaining your  actions is |
| 6 | `merged::PZO22001 Starfinder Player Core 424-441::/page/15/Text/15` | 0.634222 | Quickened, slowed, and stunned are the primary  ways you can gain or lose actions on a turn. The rules  for how this works appear on page 407. In brief, these  conditions alter how many actions you re |
| 7 | `merged::PZO22001 Starfinder Player Core 406-423::/page/1/Text/6` | 0.624961 | Effects can change the number of actions you can use on  your turn, or whether you can use actions at all. The slowed  condition, for example, causes you to lose actions, while the  quickened conditio |
| 8 | `merged::PZO22001 Starfinder Player Core 406-423::/page/1/Text/4` | 0.614274 | Sometimes you need to attempt something not already  covered by defined actions in the game. When this happens,  the rules tell you how many actions you need to spend as  well as any traits your actio |
| 9 | `merged::PZO22001 Starfinder Player Core 424-441::/page/4/Text/16` | 0.612761 | Once you've spent all three of your actions, your turn ends  (as described in Step 3) and the next creature's turn begins. You  can choose to end your turn early, losing all remaining actions  (but no |
| 10 | `merged::PZO22001 Starfinder Player Core 406-423::/page/1/Text/9` | 0.605053 | Various abilities and conditions, such as a Reactive Strike,  can disrupt an action. When an action is disrupted, you still  use the actions or reactions you committed, and you still  expend any costs |

### Query 36
- Text: What is the rule about multiple attack penalty (–5 on your second attack, –10 on  further attacks) 394?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 442-464::/page/1/Text/15']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 250-267: `0.3920`
  - PZO22001 Starfinder Player Core 388-405: `0.3777`
  - PZO22001 Starfinder Player Core 406-423: `0.3543`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 442-464::/page/1/Text/15', 'merged::PZO22001 Starfinder Player Core 442-464::/page/1/Text/14', 'merged::PZO22001 Starfinder Player Core 442-464::/page/1/Text/17']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 442-464::/page/1/Text/14` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 442-464::/page/1/Text/17` (reasons: ['graph_depth_1'])

### Query 37
- Text: What is the rule about Armor Class Shiel?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Character Sheet::/page/0/TableCell/53']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 098-113: `0.3563`
  - PZO22001 Starfinder Player Core 250-267: `0.3448`
  - PZO22001 Starfinder Player Core 150-161: `0.3433`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Character Sheet::/page/0/TableCell/53', 'merged::PZO22001 Starfinder Character Sheet::/page/0/TableCell/54', 'merged::PZO22001 Starfinder Character Sheet::/page/0/TableCell/52']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Character Sheet::/page/0/TableCell/54` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Character Sheet::/page/0/TableCell/52` (reasons: ['graph_depth_1'])

### Query 38
- Text: Summarize **PLAYING THE ** **GAME**
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 364-387::/page/3/Text/64']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 388-405: `0.4598`
  - PZO22001 Starfinder Player Core 406-423: `0.4326`
  - PZO22001 Starfinder Player Core 001-013: `0.4018`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 364-387::/page/3/Text/64', 'merged::PZO22001 Starfinder Player Core 364-387::/page/3/Text/65', 'merged::PZO22001 Starfinder Player Core 364-387::/page/3/Text/63']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 364-387::/page/3/Text/65` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 364-387::/page/3/Text/63` (reasons: ['graph_depth_1'])

### Query 39
- Text: What is the rule about There are four types of actions: single actions, activities,  reactions, and free actions.?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 406-423::/page/0/Text/7']
- Expected found: `True`
- Expected rank: `1`
- Routed chapters:
  - PZO22001 Starfinder Player Core 406-423: `0.5452`
  - PZO22001 Starfinder Player Core 388-405: `0.4220`
  - PZO22001 Starfinder Player Core 442-464: `0.3936`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 406-423::/page/0/Text/7', 'merged::PZO22001 Starfinder Player Core 406-423::/page/0/Text/8', 'merged::PZO22001 Starfinder Player Core 406-423::/page/0/Text/6']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 406-423::/page/0/Text/8` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 406-423::/page/0/Text/6` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 406-423::/page/0/Text/7` | 0.892980 | There are four types of actions: single actions, activities,  reactions, and free actions. |
| 2 | `merged::PZO22001 Starfinder Player Core 406-423::/page/1/Text/11` | 0.625964 | These rules clarify some of the specifics of using actions. |
| 3 | `merged::PZO22001 Starfinder Player Core 406-423::/page/0/Text/20` | 0.614541 | An activity typically involves using multiple actions to create  an effect greater than you can produce with a single action,  or combining multiple single actions to produce an effect  that's differe |
| 4 | `merged::PZO22001 Starfinder Player Core 442-464::/page/15/TableCell/234` | 0.588722 | ◆➤➤ Three-Action Activity ◆ Free Action |
| 5 | `merged::PZO22001 Starfinder Player Core 442-464::/page/17/TableCell/309` | 0.582239 | Free Actions and Reactions |
| 6 | `merged::PZO22001 Starfinder Player Core 388-405::/page/2/Text/8` | 0.579309 | During an encounter, you get 3 actions and 1 reaction per turn  (page 427). Icons indicate whether your abilities take a single  action [one-action], 2 actions [two-actions], 3 actions [three-actions] |
| 7 | `merged::PZO22001 Starfinder Player Core 406-423::/page/0/Text/27` | 0.579227 | You can use free actions that have triggers and reactions only  in response to certain events. Each such reaction and free  action lists the trigger that must happen for you to perform it.  When its t |
| 8 | `merged::PZO22001 Starfinder Player Core 406-423::/page/0/Text/11` | 0.578163 | **Free actions** don't cost you any of your actions per turn,  nor do they cost your reaction. A free action with no trigger  follows the same rules as a single action (except the action  cost). It mu |
| 9 | `merged::PZO22001 Starfinder Player Core 442-464::/page/0/Text/20` | 0.574144 | **activity** A category of action that typically takes more than  a single action. Activities on your turn take 2 actions ([two-actions])  or 3 actions ([three-actions]). Exploration and downtime acti |
| 10 | `merged::PZO22001 Starfinder Player Core 442-464::/page/11/Text/30` | 0.560068 | **single action **([one-action]) An action that takes one of your three  actions on your turn. 15, **406** |

### Query 40
- Text: What are the requirements for **Prerequisites** limited telepathy?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 058-073::/page/3/Text/21']
- Expected found: `True`
- Expected rank: `2`
- Routed chapters:
  - PZO22001 Starfinder Player Core 058-073: `0.2964`
  - PZO22001 Starfinder Player Core 138-149: `0.2760`
  - PZO22001 Starfinder Player Core 364-387: `0.2711`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 058-073::/page/3/Text/21', 'merged::PZO22001 Starfinder Player Core 058-073::/page/3/Text/22', 'merged::PZO22001 Starfinder Player Core 058-073::/page/3/Text/20']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 058-073::/page/3/Text/22` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 058-073::/page/3/Text/20` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/22` | 0.895401 | **Prerequisites** limited telepathy |
| 2 | `merged::PZO22001 Starfinder Player Core 058-073::/page/3/Text/21` | 0.895401 | **Prerequisites** limited telepathy |
| 3 | `merged::PZO22001 Starfinder Player Core 058-073::/page/2/Text/25` | 0.895401 | **Prerequisites** limited telepathy |
| 4 | `merged::PZO22001 Starfinder Player Core 058-073::/page/11/Text/23` | 0.895401 | **Prerequisites** limited telepathy |
| 5 | `merged::PZO22001 Starfinder Player Core 058-073::/page/8/SectionHeader/14` | 0.610754 | LIMITED TELEPATHY |
| 6 | `merged::PZO22001 Starfinder Player Core 058-073::/page/0/SectionHeader/12` | 0.610754 | LIMITED TELEPATHY |
| 7 | `merged::PZO22001 Starfinder Player Core 058-073::/page/10/Text/23` | 0.549906 | Whether through training or innate talent,  you've expanded the range at which you can  telepathically communicate. Increase the range of  your limited telepathy by 15 feet. |
| 8 | `merged::PZO22001 Starfinder Player Core 058-073::/page/2/Text/26` | 0.549906 | Whether through training or innate talent, you've expanded  the range at which you can telepathically communicate.  Increase the range of your limited telepathy by 15 feet. |
| 9 | `merged::PZO22001 Starfinder Player Core 058-073::/page/9/Text/25` | 0.544556 | Your telepathy is stronger than most shirrens', allowing you to  combine physical, verbal, and telepathic communication. You  can transmit emotions alongside your messages whenever  you use limited te |
| 10 | `merged::PZO22001 Starfinder Player Core 058-073::/page/3/Text/22` | 0.519129 | When you use limited telepathy to communicate with another  creature, you act as a conduit for their thoughts, allowing them  to respond to you for a few scant moments—if they wish. The  creature can |

### Query 41
- Text: What does **BLINDNESS **[two-actions] **SPELL 3** do?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/36']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 406-423: `0.3915`
  - PZO22001 Starfinder Player Core 424-441: `0.3367`
  - PZO22001 Starfinder Player Core 182-209: `0.3366`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/36', 'merged::PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/29', 'merged::PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/47']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/29` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/47` (reasons: ['graph_depth_1'])

### Query 42
- Text: Summarize You might solve problems with deductive reasoning or by determining mathematic  probabilities, drawing on your deep knowledge of the multiverse.
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 162-173::/page/1/Text/15']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 182-209: `0.3890`
  - PZO22001 Starfinder Player Core 092-097: `0.3625`
  - PZO22001 Starfinder Player Core 388-405: `0.3526`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 162-173::/page/1/Text/15', 'merged::PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/14', 'merged::PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/16']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/14` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/16` (reasons: ['graph_depth_1'])

### Query 43
- Text: What are the requirements for **PARKOUR **[one-action] **FEAT 8**?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 126-137::/page/9/Text/2']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 406-423: `0.3327`
  - PZO22001 Starfinder Player Core 014-029: `0.3211`
  - PZO22001 Starfinder Player Core 442-464: `0.3118`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 126-137::/page/9/Text/2', 'merged::PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/4', 'merged::PZO22001 Starfinder Player Core 126-137::/page/9/Text/1']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/4` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 126-137::/page/9/Text/1` (reasons: ['graph_depth_1'])

### Query 44
- Text: Summarize View your bond as a closed clique or think you're trying to recruit them.
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 114-125::/page/1/ListItem/24']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 424-441: `0.2669`
  - PZO22001 Starfinder Player Core 182-209: `0.2304`
  - PZO22001 Starfinder Player Core 388-405: `0.2177`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 114-125::/page/1/ListItem/24', 'merged::PZO22001 Starfinder Player Core 114-125::/page/1/ListItem/25', 'merged::PZO22001 Starfinder Player Core 114-125::/page/1/ListItem/23']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 114-125::/page/1/ListItem/25` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 114-125::/page/1/ListItem/23` (reasons: ['graph_depth_1'])

### Query 45
- Text: Summarize **LASHUNTA**
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/20']
- Expected found: `True`
- Expected rank: `13`
- Routed chapters:
  - PZO22001 Starfinder Player Core 058-073: `0.3917`
  - PZO22001 Starfinder Player Core 030-039: `0.2299`
  - PZO22001 Starfinder Player Core 250-267: `0.2140`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/20', 'merged::PZO22001 Starfinder Player Core 058-073::/page/2/Text/21', 'merged::PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/18']
- Expanded expected found: `True`
- Expanded expected rank: `13`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 058-073::/page/2/Text/21` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/18` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 058-073::/page/3/Text/7` | 0.922025 | **LASHUNTA** |
| 2 | `merged::PZO22001 Starfinder Player Core 058-073::/page/3/Text/47` | 0.922025 | **LASHUNTA** |
| 3 | `merged::PZO22001 Starfinder Player Core 058-073::/page/3/Text/15` | 0.922025 | **LASHUNTA** |
| 4 | `merged::PZO22001 Starfinder Player Core 058-073::/page/3/Text/2` | 0.922025 | **LASHUNTA** |
| 5 | `merged::PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/30` | 0.922025 | **LASHUNTA** |
| 6 | `merged::PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/24` | 0.922025 | **LASHUNTA** |
| 7 | `merged::PZO22001 Starfinder Player Core 058-073::/page/3/Text/20` | 0.922025 | **LASHUNTA** |
| 8 | `merged::PZO22001 Starfinder Player Core 058-073::/page/3/Text/11` | 0.922025 | **LASHUNTA** |
| 9 | `merged::PZO22001 Starfinder Player Core 058-073::/page/3/Text/30` | 0.922025 | **LASHUNTA** |
| 10 | `merged::PZO22001 Starfinder Player Core 058-073::/page/3/Text/26` | 0.922025 | **LASHUNTA** |

### Query 46
- Text: What is the rule about You're trained in the Deception skill and a Lore skill about a  specific settlement. You gain the Face in the Crowd skill feat.?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 092-097::/page/1/Text/14']
- Expected found: `True`
- Expected rank: `1`
- Routed chapters:
  - PZO22001 Starfinder Player Core 210-231: `0.5377`
  - PZO22001 Starfinder Player Core 092-097: `0.5098`
  - PZO22001 Starfinder Player Core 182-209: `0.5014`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 092-097::/page/1/Text/14', 'merged::PZO22001 Starfinder Player Core 092-097::/page/1/Text/13', 'merged::PZO22001 Starfinder Player Core 092-097::/page/1/SectionHeader/15']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 092-097::/page/1/Text/13` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 092-097::/page/1/SectionHeader/15` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 092-097::/page/1/Text/14` | 0.932930 | You're trained in the Deception skill and a Lore skill about a  specific settlement. You gain the Face in the Crowd skill feat. |
| 2 | `merged::PZO22001 Starfinder Player Core 092-097::/page/2/Text/24` | 0.693186 | You're trained in the Deception skill and the Games Lore  skill. You gain the Lie to Me skill feat. |
| 3 | `merged::PZO22001 Starfinder Player Core 092-097::/page/1/Text/18` | 0.660383 | You're trained in the Deception skill and Underworld Lore  skill. You gain the Without a Trace skill feat. |
| 4 | `merged::PZO22001 Starfinder Player Core 092-097::/page/2/Text/32` | 0.640918 | You're trained in the Deception skill and a Lore skill related  to a profession or subject you fake expertise in. You gain the  Charming Liar skill feat. |
| 5 | `merged::PZO22001 Starfinder Player Core 092-097::/page/4/Text/20` | 0.632936 | You're trained in the Survival skill and a Lore skill about a  specific settlement. You gain the Urban Survivalist skill feat. |
| 6 | `merged::PZO22001 Starfinder Player Core 092-097::/page/0/Text/9` | 0.616353 | You're trained in the Crafting skill and the Art Lore skill.  You gain the Specialty Crafting skill feat. |
| 7 | `merged::PZO22001 Starfinder Player Core 092-097::/page/2/Text/20` | 0.603570 | You're trained in the Society skill and a Lore skill related  to one city or region you've visited often. You gain the  Multilingual skill feat. |
| 8 | `merged::PZO22001 Starfinder Player Core 092-097::/page/4/Text/31` | 0.603451 | You're trained in the Society skill and the History Lore  skill. You gain the Dubious Knowledge skill feat. |
| 9 | `merged::PZO22001 Starfinder Player Core 092-097::/page/3/Text/30` | 0.587111 | You're trained in the Crafting skill and a Lore skill related  to your field of research. You gain the Assurance skill feat  with that Lore skill. |
| 10 | `merged::PZO22001 Starfinder Player Core 092-097::/page/3/Text/26` | 0.584861 | You're trained in the Survival skill and a Lore skill related to  your former life. You gain the Dubious Knowledge skill feat. |

### Query 47
- Text: What is the rule about can't use reactions. It also can't use move actions except to  dance, using the Stride action to move up to half its Speed. **Critical Success** The target is unaffected.?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 364-387::/page/5/Text/1']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 406-423: `0.5369`
  - PZO22001 Starfinder Player Core 388-405: `0.4257`
  - PZO22001 Starfinder Player Core 250-267: `0.4005`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 364-387::/page/5/Text/1', 'merged::PZO22001 Starfinder Player Core 364-387::/page/5/Text/2', 'merged::PZO22001 Starfinder Player Core 364-387::/page/5/SectionHeader/0']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 364-387::/page/5/Text/2` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 364-387::/page/5/SectionHeader/0` (reasons: ['graph_depth_1'])

### Query 48
- Text: What are the requirements for **Prerequisites** trained in Intimidation?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 126-137::/page/6/Text/58']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 210-231: `0.3192`
  - PZO22001 Starfinder Player Core 092-097: `0.2993`
  - PZO22001 Starfinder Player Core 182-209: `0.2855`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 126-137::/page/6/Text/58', 'merged::PZO22001 Starfinder Player Core 126-137::/page/6/SectionHeader/57', 'merged::PZO22001 Starfinder Player Core 126-137::/page/7/SectionHeader/1']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 126-137::/page/6/SectionHeader/57` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 126-137::/page/7/SectionHeader/1` (reasons: ['graph_depth_1'])

### Query 49
- Text: What is the rule about Each entry includes details about the ancestry and presents  the rules elements described below.?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 040-057::/page/1/Text/13']
- Expected found: `True`
- Expected rank: `1`
- Routed chapters:
  - PZO22001 Starfinder Player Core 040-057: `0.4791`
  - PZO22001 Starfinder Player Core 014-029: `0.4517`
  - PZO22001 Starfinder Player Core 442-464: `0.3962`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 040-057::/page/1/Text/13', 'merged::PZO22001 Starfinder Player Core 040-057::/page/1/SectionHeader/14', 'merged::PZO22001 Starfinder Player Core 040-057::/page/1/SectionHeader/12']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 040-057::/page/1/SectionHeader/14` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 040-057::/page/1/SectionHeader/12` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 040-057::/page/1/Text/13` | 0.871381 | Each entry includes details about the ancestry and presents  the rules elements described below. |
| 2 | `merged::PZO22001 Starfinder Player Core 040-057::/page/1/Text/29` | 0.623663 | Any other entries in the sidebar represent abilities, senses,  and other qualities all members of the ancestry manifest.  These are omitted for ancestries with no special rules. |
| 3 | `merged::PZO22001 Starfinder Player Core 014-029::/page/2/Text/7` | 0.618696 | Regardless of the game mechanic they convey, rules  elements are always presented in the form of a stat block,  a summary of the rules necessary to bring the monster,  character, item, or other rules |
| 4 | `merged::PZO22001 Starfinder Player Core 442-464::/page/0/Text/38` | 0.601462 | **ancestry** A broad family of people that a creature belongs to.  Each player character chooses an ancestry as the first step of  character creation. 10, 19, 27, **41–91** mixed ancestry 83 |
| 5 | `merged::PZO22001 Starfinder Player Core 014-029::/page/9/Text/3` | 0.585235 | **Ancestry:** Each ancestry provides attribute boosts, and sometimes an attribute flaw. If you're taking any voluntary  flaws, apply them in this step (see the sidebar on page 25). |
| 6 | `merged::PZO22001 Starfinder Player Core 014-029::/page/0/Text/6` | 0.580176 | The rules for ancestries and heritages representing the  Pact Worlds are in this chapter, including their ancestry  feat options. Backgrounds are at the end of this chapter,  along with a section abou |
| 7 | `merged::PZO22001 Starfinder Player Core 040-057::/page/1/Text/21` | 0.556631 | When creating a character of this ancestry, you apply attribute |
| 8 | `merged::PZO22001 Starfinder Player Core 040-057::/page/1/ListItem/8` | 0.553538 | **Ancestries** express the lineage your character hails from.  Within ancestries are heritages—subgroups that have  unique characteristics. An ancestry provides attribute  boosts (and perhaps attribut |
| 9 | `merged::PZO22001 Starfinder Player Core 040-057::/page/12/Text/4` | 0.544549 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As a human, you choose from among the  following anc |
| 10 | `merged::PZO22001 Starfinder Player Core 442-464::/page/15/TableCell/32` | 0.541068 | Ancestry ——— |

### Query 50
- Text: What is the rule about Major locations on Verces include the Ring of Nations,  a band of sprawling megacities inhabited by augmented  verthani, androids, and many others; Skydock, modern  shipyards built atop an ancient space platform; Fullbright, a  burning desert of corporate solar farms and fringe Outlaw  Kingdoms; and Darkside, a frozen landscape of ice mines and  howling tundra stalked by terrible beasts.?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 030-039::/page/2/Text/16']
- Expected found: `True`
- Expected rank: `1`
- Routed chapters:
  - PZO22001 Starfinder Player Core 030-039: `0.5114`
  - PZO22001 Starfinder Player Core 074-091: `0.4438`
  - PZO22001 Starfinder Player Core 294-329: `0.4118`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 030-039::/page/2/Text/16', 'merged::PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/17', 'merged::PZO22001 Starfinder Player Core 030-039::/page/2/Text/15']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/17` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 030-039::/page/2/Text/15` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 030-039::/page/2/Text/16` | 0.909462 | Major locations on Verces include the Ring of Nations,  a band of sprawling megacities inhabited by augmented  verthani, androids, and many others; Skydock, modern  shipyards built atop an ancient spa |
| 2 | `merged::PZO22001 Starfinder Player Core 030-039::/page/2/Text/15` | 0.700183 | Verces is a tidally locked world with a sun-scoured light side,  a frozen dark side, and a belt of opulent cybercities linked by  high-speed bullet trains called the Ring of Nations. The Ring  of Nati |
| 3 | `merged::PZO22001 Starfinder Player Core 030-039::/page/4/Text/10` | 0.537026 | Regions include Nightarch, a pressurized megacity where  opulent spires tower over air-choked slums, named for the  massive gate leading inside the planet at the center of the  settlement; the Silted |
| 4 | `merged::PZO22001 Starfinder Player Core 030-039::/page/3/Text/12` | 0.523142 | Regions on Triaxus include the Drakelands, a continental  wilderness preserve tended by dragons; the Skyfire Mandate,  an isthmus guarded by the oldest aeries of the Skyfire Legion;  the Allied Territ |
| 5 | `merged::PZO22001 Starfinder Player Core 030-039::/page/4/Text/19` | 0.520122 | Regions include Voyedris, a treacherous wilderness  ravaged by rapid industrialization; Hafrerren, a rebel nationstate known for biotech research; Rafemii, a hub for magical  and spiritual development |
| 6 | `merged::PZO22001 Starfinder Player Core 030-039::/page/4/Text/29` | 0.517775 | Regions of the Vast include the Azlanti Star Empire, a vast  territory of unknown size controlled by a colonizing regime  ruled by the descendants of a human nation from lost Golarion;  Kazmurg's Absu |
| 7 | `merged::PZO22001 Starfinder Player Core 030-039::/page/1/Text/6` | 0.512933 | The largest community on Aballon is Striving, an  industrious megacity containing a citywide neural network  sacred to Triune. Other regions include the industrial forgecity Automatrix; the immense, f |
| 8 | `merged::PZO22001 Starfinder Player Core 030-039::/page/4/Text/26` | 0.486962 | Near Space regions include the Veskarium, an empire of  seven conquered planets and a few dozen colonies ruled  by vesk military leaders; the Marixah Republic, a group of  allied planets emerging onto |
| 9 | `merged::PZO22001 Starfinder Player Core 074-091::/page/1/Text/15` | 0.484889 | Vesk society is highly organized and militaristic. Vesk first  dwelled on a single planet but quickly spread to other worlds  in their system. Today, the name for these conquered worlds  is the Veskar |
| 10 | `merged::PZO22001 Starfinder Player Core 030-039::/page/3/Text/21` | 0.481003 | Regions include Roselight, a cloud of floating domes built  by barathu architects, and Deep Station, a research outpost  submerged in Liavara's alien seas. Liavara has many moons:  Hallas, a warded pr |

### Query 51
- Text: What are the requirements for **SINGULARITY **[three-actions] **FEAT 14**?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 138-149::/page/10/SectionHeader/29']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 210-231: `0.3713`
  - PZO22001 Starfinder Player Core 406-423: `0.3695`
  - PZO22001 Starfinder Player Core 014-029: `0.3267`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 138-149::/page/10/SectionHeader/29', 'merged::PZO22001 Starfinder Player Core 138-149::/page/10/Text/31', 'merged::PZO22001 Starfinder Player Core 138-149::/page/10/Text/28']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 138-149::/page/10/Text/31` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 138-149::/page/10/Text/28` (reasons: ['graph_depth_1'])

### Query 52
- Text: Summarize A sarcesian witchwarper from a reality where the water  in the River Between never dried up.
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/33']
- Expected found: `True`
- Expected rank: `1`
- Routed chapters:
  - PZO22001 Starfinder Player Core 162-173: `0.4106`
  - PZO22001 Starfinder Player Core 030-039: `0.3689`
  - PZO22001 Starfinder Player Core 074-091: `0.3046`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/33', 'merged::PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/32', 'merged::PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/34']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/32` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/34` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/33` | 0.985210 | A sarcesian witchwarper from a reality where the water  in the River Between never dried up. |
| 2 | `merged::PZO22001 Starfinder Player Core 030-039::/page/2/Text/30` | 0.493201 | The Diaspora is an asteroid belt formed long before the  Gap, when a terrible cataclysm destroyed the twin planets  Damiar and Iovo. The remains of the two destroyed worlds  float among millions of ch |
| 3 | `merged::PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/1` | 0.468019 | **Sample Witchwarper** |
| 4 | `merged::PZO22001 Starfinder Player Core 030-039::/page/4/ListItem/23` | 0.450249 | A mystic wandering the wastes ravaged by the Shriek,  seeking natural ways to heal your war-torn ancestral lands. |
| 5 | `merged::PZO22001 Starfinder Player Core 162-173::/page/5/Text/29` | 0.432472 | **Witchwarper** |
| 6 | `merged::PZO22001 Starfinder Player Core 162-173::/page/7/Text/38` | 0.432472 | **Witchwarper** |
| 7 | `merged::PZO22001 Starfinder Player Core 162-173::/page/11/Text/39` | 0.432472 | **Witchwarper** |
| 8 | `merged::PZO22001 Starfinder Player Core 162-173::/page/1/Text/41` | 0.432472 | **Witchwarper** |
| 9 | `merged::PZO22001 Starfinder Player Core 162-173::/page/3/Text/40` | 0.432472 | **Witchwarper** |
| 10 | `merged::PZO22001 Starfinder Player Core 162-173::/page/9/Text/76` | 0.432472 | **Witchwarper** |

### Query 53
- Text: What is the rule about Trained in solarian class DC?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 138-149::/page/1/Text/62']
- Expected found: `True`
- Expected rank: `1`
- Routed chapters:
  - PZO22001 Starfinder Player Core 138-149: `0.4684`
  - PZO22001 Starfinder Player Core 182-209: `0.3868`
  - PZO22001 Starfinder Player Core 150-161: `0.3534`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 138-149::/page/1/Text/62', 'merged::PZO22001 Starfinder Player Core 138-149::/page/2/SectionHeader/1', 'merged::PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/61']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 138-149::/page/2/SectionHeader/1` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/61` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 138-149::/page/1/Text/62` | 0.855344 | Trained in solarian class DC |
| 2 | `merged::PZO22001 Starfinder Player Core 150-161::/page/1/Text/63` | 0.634924 | Trained in soldier class DC |
| 3 | `merged::PZO22001 Starfinder Player Core 138-149::/page/4/Text/24` | 0.623637 | Your ability to manipulate stellar forces is unparalleled.  Your proficiency rank for your solarian class DC increases  to master. |
| 4 | `merged::PZO22001 Starfinder Player Core 138-149::/page/4/Text/9` | 0.580162 | Your ability to manipulate stellar forces has improved. Your  proficiency rank for your solarian class DC increases to expert. |
| 5 | `merged::PZO22001 Starfinder Player Core 138-149::/page/3/Text/40` | 0.528006 | At 1st level and every even-numbered level, you gain a  solarian class feat. These begin on page 143. |
| 6 | `merged::PZO22001 Starfinder Player Core 138-149::/page/6/Text/2` | 0.500471 | You'll see the following key traits in many solarian  class features. |
| 7 | `merged::PZO22001 Starfinder Player Core 182-209::/page/1/Text/7` | 0.492632 | A character gains training in certain skills at 1st level:  typically two from their background, a small number of  predetermined skills from their class, and several skills of  your choice granted by |
| 8 | `merged::PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/413` | 0.471806 | Skill feat, solarian feat |
| 9 | `merged::PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/405` | 0.471806 | Skill feat, solarian feat |
| 10 | `merged::PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/421` | 0.471806 | Skill feat, solarian feat |

### Query 54
- Text: Summarize **Exploration ** **Mode**
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 424-441::/page/1/Text/48']
- Expected found: `True`
- Expected rank: `14`
- Routed chapters:
  - PZO22001 Starfinder Player Core 388-405: `0.4057`
  - PZO22001 Starfinder Player Core 424-441: `0.3970`
  - PZO22001 Starfinder Player Core 232-249: `0.3674`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 424-441::/page/1/Text/48', 'merged::PZO22001 Starfinder Player Core 424-441::/page/1/Text/49', 'merged::PZO22001 Starfinder Player Core 424-441::/page/1/Text/47']
- Expanded expected found: `True`
- Expanded expected rank: `14`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 424-441::/page/1/Text/49` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 424-441::/page/1/Text/47` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 388-405::/page/15/Text/41` | 0.933318 | **Exploration ** **Mode** |
| 2 | `merged::PZO22001 Starfinder Player Core 424-441::/page/3/Text/46` | 0.933318 | **Exploration ** **Mode** |
| 3 | `merged::PZO22001 Starfinder Player Core 388-405::/page/7/Text/36` | 0.933318 | **Exploration ** **Mode** |
| 4 | `merged::PZO22001 Starfinder Player Core 388-405::/page/3/Text/54` | 0.933318 | **Exploration ** **Mode** |
| 5 | `merged::PZO22001 Starfinder Player Core 388-405::/page/17/Text/32` | 0.933318 | **Exploration ** **Mode** |
| 6 | `merged::PZO22001 Starfinder Player Core 424-441::/page/7/Text/67` | 0.933318 | **Exploration ** **Mode** |
| 7 | `merged::PZO22001 Starfinder Player Core 388-405::/page/5/Text/38` | 0.933318 | **Exploration ** **Mode** |
| 8 | `merged::PZO22001 Starfinder Player Core 388-405::/page/9/Text/41` | 0.933318 | **Exploration ** **Mode** |
| 9 | `merged::PZO22001 Starfinder Player Core 388-405::/page/1/Text/43` | 0.933318 | **Exploration ** **Mode** |
| 10 | `merged::PZO22001 Starfinder Player Core 424-441::/page/9/Text/50` | 0.933318 | **Exploration ** **Mode** |

### Query 55
- Text: What are the requirements for **Prerequisites** Parkour?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 126-137::/page/10/Text/10']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 092-097: `0.2517`
  - PZO22001 Starfinder Player Core 442-464: `0.2376`
  - PZO22001 Starfinder Player Core 014-029: `0.2347`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 126-137::/page/10/Text/10', 'merged::PZO22001 Starfinder Player Core 126-137::/page/10/Text/9', 'merged::PZO22001 Starfinder Player Core 126-137::/page/10/Text/11']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 126-137::/page/10/Text/9` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 126-137::/page/10/Text/11` (reasons: ['graph_depth_1'])

### Query 56
- Text: Summarize +1
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/660']
- Expected found: `True`
- Expected rank: `2`
- Routed chapters:
  - PZO22001 Starfinder Player Core 014-029: `0.2877`
  - PZO22001 Starfinder Player Core 282-293: `0.2367`
  - PZO22001 Starfinder Player Core 250-267: `0.2353`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/660', 'merged::PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/661', 'merged::PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/659']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/661` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/659` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/642` | 0.714275 | +1 |
| 2 | `merged::PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/660` | 0.714275 | +1 |
| 3 | `merged::PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/261` | 0.714275 | +1 |
| 4 | `merged::PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/268` | 0.714275 | +1 |
| 5 | `merged::PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/651` | 0.714275 | +1 |
| 6 | `merged::PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/289` | 0.641232 | +3 |
| 7 | `merged::PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/725` | 0.641232 | +3 |
| 8 | `merged::PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/711` | 0.641232 | +3 |
| 9 | `merged::PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/718` | 0.641232 | +3 |
| 10 | `merged::PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/732` | 0.626751 | +5 |

### Query 57
- Text: What are the requirements for **Prerequisites** trained in Deception?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 098-113::/page/12/Text/22']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 182-209: `0.3766`
  - PZO22001 Starfinder Player Core 092-097: `0.3369`
  - PZO22001 Starfinder Player Core 210-231: `0.3337`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 098-113::/page/12/Text/22', 'merged::PZO22001 Starfinder Player Core 098-113::/page/12/Text/23', 'merged::PZO22001 Starfinder Player Core 098-113::/page/12/Text/21']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 098-113::/page/12/Text/23` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 098-113::/page/12/Text/21` (reasons: ['graph_depth_1'])

### Query 58
- Text: What is the rule about **ACTION ICON KEY**?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 406-423::/page/0/SectionHeader/12']
- Expected found: `True`
- Expected rank: `1`
- Routed chapters:
  - PZO22001 Starfinder Player Core 406-423: `0.3877`
  - PZO22001 Starfinder Player Core 014-029: `0.3676`
  - PZO22001 Starfinder Player Core 442-464: `0.3663`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 406-423::/page/0/SectionHeader/12', 'merged::PZO22001 Starfinder Player Core 406-423::/page/0/Text/13', 'merged::PZO22001 Starfinder Player Core 406-423::/page/0/Text/11']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 406-423::/page/0/Text/13` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 406-423::/page/0/Text/11` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 406-423::/page/0/SectionHeader/12` | 0.886468 | **ACTION ICON KEY** |
| 2 | `merged::PZO22001 Starfinder Player Core 442-464::/page/15/TableCell/222` | 0.621044 | Action Icons |
| 3 | `merged::PZO22001 Starfinder Player Core 014-029::/page/1/Text/8` | 0.524193 | Throughout this book, you will see special icons to  denote actions. |
| 4 | `merged::PZO22001 Starfinder Player Core 406-423::/page/1/Text/11` | 0.520574 | These rules clarify some of the specifics of using actions. |
| 5 | `merged::PZO22001 Starfinder Player Core 406-423::/page/0/Text/13` | 0.507958 | These icons appear in stat blocks as shorthand for each  type of action. As a player, you'll usually see the icon in  an action's header (such as in a basic action, skill action,  feat, or spell). In |
| 6 | `merged::PZO22001 Starfinder Player Core 406-423::/page/3/Text/48` | 0.505693 | **Actions** |
| 7 | `merged::PZO22001 Starfinder Player Core 406-423::/page/7/Text/42` | 0.505693 | **Actions** |
| 8 | `merged::PZO22001 Starfinder Player Core 406-423::/page/15/Text/27` | 0.505693 | **Actions** |
| 9 | `merged::PZO22001 Starfinder Player Core 406-423::/page/11/Text/34` | 0.505693 | **Actions** |
| 10 | `merged::PZO22001 Starfinder Player Core 406-423::/page/13/Text/44` | 0.505692 | **Actions** |

### Query 59
- Text: What is the rule about **ANCESTRIES & ** **BACKGROUNDS**?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 001-013::/page/4/Text/26']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 040-057: `0.4405`
  - PZO22001 Starfinder Player Core 092-097: `0.3655`
  - PZO22001 Starfinder Player Core 014-029: `0.3538`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 001-013::/page/4/Text/26', 'merged::PZO22001 Starfinder Player Core 001-013::/page/6/Text/18', 'merged::PZO22001 Starfinder Player Core 001-013::/page/12/Text/33', 'merged::PZO22001 Starfinder Player Core 001-013::/page/4/Text/27', 'merged::PZO22001 Starfinder Player Core 001-013::/page/10/Text/38', 'merged::PZO22001 Starfinder Player Core 001-013::/page/4/Text/25', 'merged::PZO22001 Starfinder Player Core 001-013::/page/8/Text/19']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 001-013::/page/6/Text/18` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 001-013::/page/12/Text/33` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 001-013::/page/4/Text/27` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 001-013::/page/10/Text/38` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 001-013::/page/4/Text/25` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 001-013::/page/8/Text/19` (reasons: ['graph_depth_1'])

### Query 60
- Text: What does **GHOSTLY CARRIER **[two-actions] **SPELL 2** do?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 330-363::/page/4/SectionHeader/17']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 406-423: `0.3771`
  - PZO22001 Starfinder Player Core 162-173: `0.3408`
  - PZO22001 Starfinder Player Core 294-329: `0.3278`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 330-363::/page/4/SectionHeader/17', 'merged::PZO22001 Starfinder Player Core 330-363::/page/4/SectionHeader/23', 'merged::PZO22001 Starfinder Player Core 330-363::/page/4/SectionHeader/10']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 330-363::/page/4/SectionHeader/23` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 330-363::/page/4/SectionHeader/10` (reasons: ['graph_depth_1'])

### Query 61
- Text: What is the rule about SPELLCASTING ARCHETYPES?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 174-181::/page/0/SectionHeader/14']
- Expected found: `True`
- Expected rank: `1`
- Routed chapters:
  - PZO22001 Starfinder Player Core 442-464: `0.3672`
  - PZO22001 Starfinder Player Core 174-181: `0.3647`
  - PZO22001 Starfinder Player Core 294-329: `0.3151`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 174-181::/page/0/SectionHeader/14', 'merged::PZO22001 Starfinder Player Core 174-181::/page/0/Text/15', 'merged::PZO22001 Starfinder Player Core 174-181::/page/0/Text/13']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 174-181::/page/0/Text/15` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 174-181::/page/0/Text/13` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 174-181::/page/0/SectionHeader/14` | 0.853040 | SPELLCASTING ARCHETYPES |
| 2 | `merged::PZO22001 Starfinder Player Core 174-181::/page/0/SectionHeader/1` | 0.525172 | ARCHETYPES |
| 3 | `merged::PZO22001 Starfinder Player Core 174-181::/page/0/SectionHeader/20` | 0.508283 | SPECIAL ARCHETYPES |
| 4 | `merged::PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/11` | 0.491979 | **SPELLCASTING IN STARFINDER** |
| 5 | `merged::PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/17` | 0.486179 | **BASIC MYSTIC SPELLCASTING** **FEAT 4** |
| 6 | `merged::PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/43` | 0.482951 | **EXPERT MYSTIC SPELLCASTING** **FEAT 12** |
| 7 | `merged::PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0` | 0.455668 | CHAPTER 7: SPELLS |
| 8 | `merged::PZO22001 Starfinder Player Core 174-181::/page/0/Text/15` | 0.452939 | Some archetypes grant you a substantial degree of  spellcasting, albeit delayed compared to a character from a  spellcasting class. The spellcasting ability from a spellcasting  archetype also allows |
| 9 | `merged::PZO22001 Starfinder Player Core 294-329::/page/7/SectionHeader/3` | 0.451165 | IDENTIFYING SPELLS |
| 10 | `merged::PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/2` | 0.446302 | CASTING SPELLS |

### Query 62
- Text: What is the rule about Gain a 1st-level ancestry feat?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/465']
- Expected found: `True`
- Expected rank: `1`
- Routed chapters:
  - PZO22001 Starfinder Player Core 210-231: `0.5229`
  - PZO22001 Starfinder Player Core 040-057: `0.4597`
  - PZO22001 Starfinder Player Core 014-029: `0.4383`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/465', 'merged::PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/466', 'merged::PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/464']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/466` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/464` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/465` | 0.870093 | Gain a 1st-level ancestry feat |
| 2 | `merged::PZO22001 Starfinder Player Core 040-057::/page/12/Text/4` | 0.783056 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As a human, you choose from among the  following anc |
| 3 | `merged::PZO22001 Starfinder Player Core 040-057::/page/4/Text/5` | 0.701677 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As an android, you choose from among  the following |
| 4 | `merged::PZO22001 Starfinder Player Core 040-057::/page/1/Text/33` | 0.695332 | This section presents ancestry feats, which allow you to  customize your character. You gain your first ancestry feat  at 1st level, and you gain another at 5th level, 9th level, 13th  level, and 17th |
| 5 | `merged::PZO22001 Starfinder Player Core 040-057::/page/8/Text/4` | 0.692293 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th,  9th, 13th, and 17th level). As a barathu, you choose from  among the following a |
| 6 | `merged::PZO22001 Starfinder Player Core 040-057::/page/16/Text/7` | 0.688358 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As a kasatha, you choose from among  the following a |
| 7 | `merged::PZO22001 Starfinder Player Core 040-057::/page/1/Text/34` | 0.660760 | As a starting character, you can choose from only 1stlevel ancestry feats, but later choices can be made from any  feat of your level or lower. These feats also sometimes list  prerequisites, which ar |
| 8 | `merged::PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/405` | 0.657229 | Gain access to ancestry feats from another ancestry |
| 9 | `merged::PZO22001 Starfinder Player Core 210-231::/page/6/Text/14` | 0.641032 | Whether through instinct, study, or magic, you feel a deeper  connection to your ancestry. You gain a 1st-level ancestry feat. |
| 10 | `merged::PZO22001 Starfinder Player Core 014-029::/page/5/ListItem/24` | 0.614036 | Choose an ancestry feat, representing an ability your  hero learned at an early age. |

### Query 63
- Text: What are the requirements for **INTERNAL COMPARTMENT** **FEAT 1**?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 040-057::/page/4/SectionHeader/17']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 210-231: `0.2457`
  - PZO22001 Starfinder Player Core 268-281: `0.2360`
  - PZO22001 Starfinder Player Core 014-029: `0.2288`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 040-057::/page/4/SectionHeader/17', 'merged::PZO22001 Starfinder Player Core 040-057::/page/4/Text/16', 'merged::PZO22001 Starfinder Player Core 040-057::/page/4/Text/19']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 040-057::/page/4/Text/16` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 040-057::/page/4/Text/19` (reasons: ['graph_depth_1'])

### Query 64
- Text: What are the requirements for **TWIN GUARD **[reaction] **FEAT 10**?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/51']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 014-029: `0.3358`
  - PZO22001 Starfinder Player Core 406-423: `0.3245`
  - PZO22001 Starfinder Player Core 210-231: `0.3222`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/51', 'merged::PZO22001 Starfinder Player Core 138-149::/page/9/Text/50', 'merged::PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/53']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 138-149::/page/9/Text/50` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/53` (reasons: ['graph_depth_1'])

### Query 65
- Text: What is the rule about THE PACT WORLDS?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 030-039::/page/0/SectionHeader/15']
- Expected found: `True`
- Expected rank: `1`
- Routed chapters:
  - PZO22001 Starfinder Player Core 030-039: `0.3785`
  - PZO22001 Starfinder Player Core 074-091: `0.3628`
  - PZO22001 Starfinder Player Core 092-097: `0.3056`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 030-039::/page/0/SectionHeader/15', 'merged::PZO22001 Starfinder Player Core 030-039::/page/0/ListItem/14', 'merged::PZO22001 Starfinder Player Core 030-039::/page/0/Text/16']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 030-039::/page/0/ListItem/14` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 030-039::/page/0/Text/16` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 030-039::/page/0/SectionHeader/15` | 0.836002 | THE PACT WORLDS |
| 2 | `merged::PZO22001 Starfinder Player Core 092-097::/page/5/TableCell/491` | 0.580314 | Humans, most citizens of the Pact Worlds |
| 3 | `merged::PZO22001 Starfinder Player Core 074-091::/page/8/Text/2` | 0.472810 | The peoples of the Pact Worlds (and other worlds in the galaxy) are many, and they have a long  history of intermingling or dabbling with forces capable of altering the very fabric of a mortal  body o |
| 4 | `merged::PZO22001 Starfinder Player Core 030-039::/page/0/Text/16` | 0.451369 | The Pact Worlds form the core of the Starfinder setting.  "The Pact Worlds" is the formal name for the united planets  orbiting lost Golarion's sun and their more distant allied  worlds, including Pul |
| 5 | `merged::PZO22001 Starfinder Player Core 092-097::/page/5/Table/7` | 0.439815 | LanguageSpeakersCommonHumans, most citizens of the Pact WorldsKasathaKasathas, inhabitants of Kasath or the IdariPahtraPahtras |
| 6 | `merged::PZO22001 Starfinder Player Core 092-097::/page/5/Text/14` | 0.433334 | Most characters also learn the Common language. This  is the most widely used language in the galaxy and is the  dominant language of the Pact Worlds. In many systems,  even if Common is not the offic |
| 7 | `merged::PZO22001 Starfinder Player Core 074-091::/page/8/Text/7` | 0.432838 | The Pact Worlds is home to a variety of versatile heritages.  Some are born to unusual creatures or arise through specific  mundane or supernatural circumstances. Because the  circumstances that give |
| 8 | `merged::PZO22001 Starfinder Player Core 092-097::/page/5/Text/4` | 0.426893 | The languages presented here are grouped according to their use in the Pact Worlds. Languages that are uncommon  are most frequently spoken by their native speakers, but  they are also spoken by certa |
| 9 | `merged::PZO22001 Starfinder Player Core 030-039::/page/4/Text/18` | 0.407604 | for freedom, the pahtra rebels of Pulonis eventually drove  out the last Veskarium occupiers, declared independence,  and joined the Pact Worlds interstellar alliance. Pulonis is the  first world outs |
| 10 | `merged::PZO22001 Starfinder Player Core 030-039::/page/0/ListItem/13` | 0.402834 | **The galaxy is diverse.** Countless worlds and cultures  flourish all over the galaxy (and beyond). Travelers  from Near Space often visit the Pact Worlds (and vice  versa). Visitors from the Vast ar |

### Query 66
- Text: What are the requirements for **BREATH CONTROL** **FEAT 1**?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 210-231::/page/7/Text/17']
- Expected found: `True`
- Expected rank: `1`
- Routed chapters:
  - PZO22001 Starfinder Player Core 210-231: `0.3314`
  - PZO22001 Starfinder Player Core 014-029: `0.2903`
  - PZO22001 Starfinder Player Core 150-161: `0.2677`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 210-231::/page/7/Text/17', 'merged::PZO22001 Starfinder Player Core 210-231::/page/7/Text/16', 'merged::PZO22001 Starfinder Player Core 210-231::/page/7/Text/19']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 210-231::/page/7/Text/16` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 210-231::/page/7/Text/19` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 210-231::/page/7/Text/17` | 0.849824 | **BREATH CONTROL** **FEAT 1** |
| 2 | `merged::PZO22001 Starfinder Player Core 210-231::/page/8/Text/17` | 0.549379 | **CROWD CONTROL** **FEAT 2** |
| 3 | `merged::PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/418` | 0.502722 | Breath Control |
| 4 | `merged::PZO22001 Starfinder Player Core 210-231::/page/18/Text/11` | 0.501098 | **SKILL TRAINING** **FEAT 1** |
| 5 | `merged::PZO22001 Starfinder Player Core 210-231::/page/17/Text/14` | 0.478955 | **RIDE** **FEAT 1** |
| 6 | `merged::PZO22001 Starfinder Player Core 210-231::/page/14/SectionHeader/17` | 0.470713 | **MANAGEMENT MATERIAL** **FEAT 1** |
| 7 | `merged::PZO22001 Starfinder Player Core 210-231::/page/11/Text/3` | 0.470420 | **FLEET** **FEAT 1** |
| 8 | `merged::PZO22001 Starfinder Player Core 210-231::/page/7/Text/7` | 0.458196 | **BLEND IN** **FEAT 1** |
| 9 | `merged::PZO22001 Starfinder Player Core 210-231::/page/7/Text/12` | 0.453416 | **BREAK CURSE** **FEAT 7** |
| 10 | `merged::PZO22001 Starfinder Player Core 210-231::/page/18/Text/26` | 0.453010 | **STEADY BALANCE** **FEAT 1** |

### Query 67
- Text: What is the rule about 5th-rank spells, ancestry feat, resilient soul,?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/405']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 210-231: `0.4807`
  - PZO22001 Starfinder Player Core 040-057: `0.4625`
  - PZO22001 Starfinder Character Sheet: `0.4441`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/405', 'merged::PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/404', 'merged::PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/406']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/404` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/406` (reasons: ['graph_depth_1'])

### Query 68
- Text: Lookup values for SizeSpaceReach (Tall)Reach (Long)TinyLess than 5
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 406-423::/page/7/Table/25']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 250-267: `0.2870`
  - PZO22001 Starfinder Player Core 424-441: `0.2598`
  - PZO22001 Starfinder Player Core 268-281: `0.2530`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 406-423::/page/7/Table/25', 'merged::PZO22001 Starfinder Player Core 406-423::/page/7/TableCell/544', 'merged::PZO22001 Starfinder Player Core 406-423::/page/7/SectionHeader/24']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 406-423::/page/7/TableCell/544` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 406-423::/page/7/SectionHeader/24` (reasons: ['graph_depth_1'])

### Query 69
- Text: What is the rule about **ACTIVE CAMOUFLAGE** **UPGRADE 5+**?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 268-281::/page/1/SectionHeader/4']
- Expected found: `True`
- Expected rank: `1`
- Routed chapters:
  - PZO22001 Starfinder Player Core 268-281: `0.3573`
  - PZO22001 Starfinder Player Core 014-029: `0.3376`
  - PZO22001 Starfinder Player Core 232-249: `0.3256`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 268-281::/page/1/SectionHeader/4', 'merged::PZO22001 Starfinder Player Core 268-281::/page/1/Text/6', 'merged::PZO22001 Starfinder Player Core 268-281::/page/1/SectionHeader/3']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 268-281::/page/1/Text/6` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 268-281::/page/1/SectionHeader/3` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 268-281::/page/1/SectionHeader/4` | 0.867875 | **ACTIVE CAMOUFLAGE** **UPGRADE 5+** |
| 2 | `merged::PZO22001 Starfinder Player Core 268-281::/page/3/TableCell/739` | 0.536012 | Active camouflage, advanced |
| 3 | `merged::PZO22001 Starfinder Player Core 268-281::/page/2/Text/25` | 0.502291 | **JETPACK** **UPGRADE 5+** |
| 4 | `merged::PZO22001 Starfinder Player Core 268-281::/page/5/SectionHeader/15` | 0.468854 | **FEAR PROJECTOR** **UPGRADE 5+** |
| 5 | `merged::PZO22001 Starfinder Player Core 268-281::/page/3/TableCell/663` | 0.462898 | Active camouflage, commercial |
| 6 | `merged::PZO22001 Starfinder Player Core 268-281::/page/3/TableCell/695` | 0.462231 | Active camouflage, tactical |
| 7 | `merged::PZO22001 Starfinder Player Core 268-281::/page/4/SectionHeader/12` | 0.451464 | **ANIMATED INTELLIGENCE** **UPGRADE 12+** |
| 8 | `merged::PZO22001 Starfinder Player Core 268-281::/page/2/SectionHeader/63` | 0.438171 | **MOBILITY ENHANCER** **UPGRADE 3+** |
| 9 | `merged::PZO22001 Starfinder Player Core 268-281::/page/5/SectionHeader/31` | 0.435521 | **FLAMING MODULE** **UPGRADE 8+** |
| 10 | `merged::PZO22001 Starfinder Player Core 268-281::/page/0/Text/9` | 0.432728 | Most upgrades grant their benefits continually so long as  you're properly wearing the armor they're installed in. Others  produce their effects only when used properly in the moment  by spending acti |

### Query 70
- Text: What is the rule about Environmental protections are crucial tools for explorers and  combatants alike, allowing any species to operate in hostile  conditions ill-suited for its survival. These items function as long  as the armor's environmental protections (page 244) are active  and can quickly recharge while a character is resting as other  functions in an armor enter sleep mode.?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 268-281::/page/0/Text/13']
- Expected found: `True`
- Expected rank: `1`
- Routed chapters:
  - PZO22001 Starfinder Player Core 232-249: `0.4950`
  - PZO22001 Starfinder Player Core 424-441: `0.4785`
  - PZO22001 Starfinder Player Core 268-281: `0.4726`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 268-281::/page/0/Text/13', 'merged::PZO22001 Starfinder Player Core 268-281::/page/0/SectionHeader/12', 'merged::PZO22001 Starfinder Player Core 268-281::/page/0/SectionHeader/14']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 268-281::/page/0/SectionHeader/12` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 268-281::/page/0/SectionHeader/14` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 268-281::/page/0/Text/13` | 0.955686 | Environmental protections are crucial tools for explorers and  combatants alike, allowing any species to operate in hostile  conditions ill-suited for its survival. These items function as long  as th |
| 2 | `merged::PZO22001 Starfinder Player Core 232-249::/page/12/Text/14` | 0.686394 | A suit of armor's environmental protections last for a  number of days equal to its item level. Activating or  deactivating these environmental protections takes a single  Interact action if you're we |
| 3 | `merged::PZO22001 Starfinder Player Core 232-249::/page/12/Text/11` | 0.681476 | Armor environmental protections work only while within  a thick or thin atmosphere, a vacuum, or non-hazardous liquid.  In all other environments, armor is designed to cycle down,  refill its air supp |
| 4 | `merged::PZO22001 Starfinder Player Core 232-249::/page/12/Text/12` | 0.668877 | **Armor** **Protections:** All armors, except those with the  exposed trait, allow you to breathe and survive in a thick or  thin atmosphere, a vacuum, or in non-hazardous underwater  environments. Th |
| 5 | `merged::PZO22001 Starfinder Player Core 232-249::/page/12/Text/2` | 0.667691 | Armor increases your character's defenses, but some medium or heavy armor can hamper movement.  If you want to increase your character's defense beyond the protection their armor provides, they  can u |
| 6 | `merged::PZO22001 Starfinder Player Core 232-249::/page/12/Text/10` | 0.630268 | The galaxy is a vast and wondrous place, with countless dangers  and worlds within it, but space is inhospitable and incredibly  deadly. Every type of modern armor has built-in environmental  protecti |
| 7 | `merged::PZO22001 Starfinder Player Core 232-249::/page/12/Text/15` | 0.619361 | The duration of armor's environmental protections is  utilized in 1-day increments. Recharging this duration  requires access to a functioning starship or an environment  recharging station (publicly |
| 8 | `merged::PZO22001 Starfinder Player Core 424-441::/page/6/Text/17` | 0.584046 | **Requirements** You have environmental protection on your  armor or a field scientist's kit. |
| 9 | `merged::PZO22001 Starfinder Player Core 424-441::/page/6/Text/18` | 0.567618 | You analyze your environment to determine whether it's safe  by checking the gauges and sensors on your armor or a field  scientist's kit you're holding. You move at half your travel speed  or slower. |
| 10 | `merged::PZO22001 Starfinder Player Core 268-281::/page/3/SectionHeader/5` | 0.546073 | **ENVIRONMENTAL PROTECTIONS** |

### Query 71
- Text: What is the rule about **agile** (weapon trait) 255?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 442-464::/page/0/Text/29']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 250-267: `0.4312`
  - PZO22001 Starfinder Player Core 388-405: `0.3916`
  - PZO22001 Starfinder Player Core 098-113: `0.3696`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 442-464::/page/0/Text/29', 'merged::PZO22001 Starfinder Player Core 442-464::/page/0/Text/30', 'merged::PZO22001 Starfinder Player Core 442-464::/page/0/Text/28']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 442-464::/page/0/Text/30` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 442-464::/page/0/Text/28` (reasons: ['graph_depth_1'])

### Query 72
- Text: Summarize 4
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/396']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 014-029: `0.2321`
  - PZO22001 Starfinder Player Core 282-293: `0.2317`
  - PZO22001 Starfinder Player Core 250-267: `0.2308`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/396', 'merged::PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/397', 'merged::PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/395']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/397` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/395` (reasons: ['graph_depth_1'])

### Query 73
- Text: Summarize Huge
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/244']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 364-387: `0.2823`
  - PZO22001 Starfinder Player Core 150-161: `0.2558`
  - PZO22001 Starfinder Player Core 282-293: `0.2487`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/244', 'merged::PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/243', 'merged::PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/245']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/243` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/245` (reasons: ['graph_depth_1'])

### Query 74
- Text: What is the rule about At 5th level, whenever you get a critical hit with one  of these attacks, you get its critical specialization effect. **Special** You can take this feat three times. Each time you  do, select a different attack from the options listed above.?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 074-091::/page/2/Text/20']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 210-231: `0.5254`
  - PZO22001 Starfinder Player Core 406-423: `0.4602`
  - PZO22001 Starfinder Player Core 250-267: `0.4223`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 074-091::/page/2/Text/20', 'merged::PZO22001 Starfinder Player Core 074-091::/page/2/Text/19', 'merged::PZO22001 Starfinder Player Core 074-091::/page/2/SectionHeader/21']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 074-091::/page/2/Text/19` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 074-091::/page/2/SectionHeader/21` (reasons: ['graph_depth_1'])

### Query 75
- Text: What does **COZY CRASHPAD** **SPELL 3** do?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/47']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 162-173: `0.2803`
  - PZO22001 Starfinder Player Core 330-363: `0.2728`
  - PZO22001 Starfinder Player Core 406-423: `0.2595`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/47', 'merged::PZO22001 Starfinder Player Core 294-329::/page/29/Text/2', 'merged::PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/39']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 294-329::/page/29/Text/2` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/39` (reasons: ['graph_depth_1'])

### Query 76
- Text: Summarize **Constitution**
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 014-029::/page/5/SectionHeader/9']
- Expected found: `True`
- Expected rank: `2`
- Routed chapters:
  - PZO22001 Starfinder Player Core 150-161: `0.3027`
  - PZO22001 Starfinder Player Core 388-405: `0.2912`
  - PZO22001 Starfinder Player Core 014-029: `0.2859`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 014-029::/page/5/SectionHeader/9', 'merged::PZO22001 Starfinder Player Core 014-029::/page/5/Text/10', 'merged::PZO22001 Starfinder Player Core 014-029::/page/5/Text/8']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 014-029::/page/5/Text/10` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 014-029::/page/5/Text/8` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/7` | 0.869836 | **Constitution** |
| 2 | `merged::PZO22001 Starfinder Player Core 014-029::/page/5/SectionHeader/9` | 0.869836 | **Constitution** |
| 3 | `merged::PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/10` | 0.586500 | **10 + Constitution modifier** |
| 4 | `merged::PZO22001 Starfinder Player Core 150-161::/page/1/Text/8` | 0.451186 | At 1st level, your class gives you  an attribute boost to Constitution. |
| 5 | `merged::PZO22001 Starfinder Player Core 014-029::/page/5/Text/10` | 0.432471 | Constitution measures your character's health and stamina,  and is important for all characters, especially those who  fight in close range. Your Constitution modifier is added to  your Hit Points and |
| 6 | `merged::PZO22001 Starfinder Player Core 014-029::/page/1/Text/22` | 0.432347 | **Religion** |
| 7 | `merged::PZO22001 Starfinder Player Core 014-029::/page/15/Text/27` | 0.432347 | **Religion** |
| 8 | `merged::PZO22001 Starfinder Player Core 014-029::/page/13/Text/6` | 0.432347 | **Religion** |
| 9 | `merged::PZO22001 Starfinder Player Core 014-029::/page/11/Text/31` | 0.432347 | **Religion** |
| 10 | `merged::PZO22001 Starfinder Player Core 014-029::/page/9/Text/28` | 0.432347 | **Religion** |

### Query 77
- Text: What is the rule about **Character Sheet:** Each player needs a character sheet to  create their character and to record what happens to them  during play. You can find a character sheet in the back of this  book and online as a free PDF.?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 001-013::/page/5/Text/13']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Character Sheet: `0.5737`
  - PZO22001 Starfinder Player Core 014-029: `0.5530`
  - PZO22001 Starfinder Player Core 442-464: `0.5088`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 001-013::/page/5/Text/13', 'merged::PZO22001 Starfinder Player Core 001-013::/page/5/Text/12', 'merged::PZO22001 Starfinder Player Core 001-013::/page/5/Text/14']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 001-013::/page/5/Text/12` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 001-013::/page/5/Text/14` (reasons: ['graph_depth_1'])

### Query 78
- Text: Summarize **Grenades**
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 282-293::/page/1/Text/60']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 150-161: `0.2322`
  - PZO22001 Starfinder Player Core 268-281: `0.2202`
  - PZO22001 Starfinder Player Core 330-363: `0.2133`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 282-293::/page/1/Text/60', 'merged::PZO22001 Starfinder Player Core 282-293::/page/1/Text/59', 'merged::PZO22001 Starfinder Player Core 282-293::/page/1/Text/61']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 282-293::/page/1/Text/59` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 282-293::/page/1/Text/61` (reasons: ['graph_depth_1'])

### Query 79
- Text: Summarize You know better than most the power of electricity,  having survived several close calls yourself, and you know  firsthand how shocking it can be when something goes  wrong. Whether you learned by installing power stations or  repairing broken circuits, you're familiar with the positives  and negatives of electricity.
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 092-097::/page/2/Text/14']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 182-209: `0.3568`
  - PZO22001 Starfinder Player Core 364-387: `0.3516`
  - PZO22001 Starfinder Player Core 424-441: `0.3445`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 092-097::/page/2/Text/14', 'merged::PZO22001 Starfinder Player Core 092-097::/page/2/Text/15', 'merged::PZO22001 Starfinder Player Core 092-097::/page/2/SectionHeader/13']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 092-097::/page/2/Text/15` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 092-097::/page/2/SectionHeader/13` (reasons: ['graph_depth_1'])

### Query 80
- Text: Summarize 2
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/493']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 014-029: `0.2645`
  - PZO22001 Starfinder Player Core 250-267: `0.2502`
  - PZO22001-HC Player Core 000: `0.2431`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/493', 'merged::PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/494', 'merged::PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/492']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/494` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/492` (reasons: ['graph_depth_1'])

### Query 81
- Text: Summarize 2
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/390']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 014-029: `0.2645`
  - PZO22001 Starfinder Player Core 250-267: `0.2502`
  - PZO22001-HC Player Core 000: `0.2431`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/390', 'merged::PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/389', 'merged::PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/391']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/389` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/391` (reasons: ['graph_depth_1'])

### Query 82
- Text: Summarize ABALLON
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 030-039::/page/1/SectionHeader/3']
- Expected found: `True`
- Expected rank: `1`
- Routed chapters:
  - PZO22001 Starfinder Player Core 030-039: `0.2510`
  - PZO22001 Starfinder Player Core 250-267: `0.2290`
  - PZO22001 Starfinder Player Core 014-029: `0.2119`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 030-039::/page/1/SectionHeader/3', 'merged::PZO22001 Starfinder Player Core 030-039::/page/1/SectionHeader/4', 'merged::PZO22001 Starfinder Player Core 030-039::/page/1/Text/2']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 030-039::/page/1/SectionHeader/4` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 030-039::/page/1/Text/2` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 030-039::/page/1/SectionHeader/3` | 0.865713 | ABALLON |
| 2 | `merged::PZO22001 Starfinder Player Core 250-267::/page/16/TableCell/10` | 0.359221 | eapon |
| 3 | `merged::PZO22001 Starfinder Player Core 030-039::/page/1/SectionHeader/23` | 0.341955 | ABSALOM STATION |
| 4 | `merged::PZO22001 Starfinder Player Core 250-267::/page/15/TableCell/200` | 0.336562 | Analog |
| 5 | `merged::PZO22001 Starfinder Player Core 250-267::/page/15/TableCell/252` | 0.336562 | Analog |
| 6 | `merged::PZO22001 Starfinder Player Core 250-267::/page/15/TableCell/343` | 0.336562 | Analog |
| 7 | `merged::PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/692` | 0.336562 | Analog |
| 8 | `merged::PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/638` | 0.336562 | Analog |
| 9 | `merged::PZO22001 Starfinder Player Core 030-039::/page/1/Text/5` | 0.327108 | Aballon is a rocky, cratered world of superheated metallic  deserts and deep ice wells. Thousands of years before the  Gap, a mysterious civilization called the First Ones utilized  Aballon's abundant |
| 10 | `merged::PZO22001 Starfinder Player Core 030-039::/page/5/SectionHeader/5` | 0.325804 | ABADAR |

### Query 83
- Text: What is the rule about **Aballon** A rocky, sun-blasted planet of industry which is home to  intelligent machines created by the enigmatic First Ones. 31?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 442-464::/page/0/Text/3']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 030-039: `0.4699`
  - PZO22001 Starfinder Player Core 001-013: `0.3999`
  - PZO22001 Starfinder Player Core 330-363: `0.3784`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 442-464::/page/0/Text/3', 'merged::PZO22001 Starfinder Player Core 442-464::/page/0/Text/4', 'merged::PZO22001 Starfinder Player Core 442-464::/page/0/SectionHeader/1']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 442-464::/page/0/Text/4` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 442-464::/page/0/SectionHeader/1` (reasons: ['graph_depth_1'])

### Query 84
- Text: Summarize **GAME**
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 092-097::/page/3/Text/53']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 388-405: `0.4680`
  - PZO22001 Starfinder Player Core 001-013: `0.4300`
  - PZO22001 Starfinder Player Core 406-423: `0.4216`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 092-097::/page/3/Text/53', 'merged::PZO22001 Starfinder Player Core 092-097::/page/3/Text/48', 'merged::PZO22001 Starfinder Player Core 092-097::/page/3/Text/47']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 092-097::/page/3/Text/48` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 092-097::/page/3/Text/47` (reasons: ['graph_depth_1'])

### Query 85
- Text: What is the rule about arcane spell list 302–305?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 442-464::/page/1/Text/4']
- Expected found: `True`
- Expected rank: `1`
- Routed chapters:
  - PZO22001 Starfinder Player Core 294-329: `0.4071`
  - PZO22001 Starfinder Player Core 442-464: `0.3905`
  - PZO22001 Starfinder Player Core 330-363: `0.3866`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 442-464::/page/1/Text/4', 'merged::PZO22001 Starfinder Player Core 442-464::/page/1/Text/3', 'merged::PZO22001 Starfinder Player Core 442-464::/page/1/Text/5']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 442-464::/page/1/Text/3` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 442-464::/page/1/Text/5` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 442-464::/page/1/Text/4` | 0.876454 | arcane spell list 302–305 |
| 2 | `merged::PZO22001 Starfinder Player Core 442-464::/page/14/Text/45` | 0.747256 | spell lists 302–305,307–310 |
| 3 | `merged::PZO22001 Starfinder Player Core 442-464::/page/12/Text/22` | 0.686889 | spell lists 302–312 |
| 4 | `merged::PZO22001 Starfinder Player Core 442-464::/page/8/Text/37` | 0.685825 | spell lists 305–312 |
| 5 | `merged::PZO22001 Starfinder Player Core 442-464::/page/13/Text/23` | 0.579189 | spell targets 298, 300 |
| 6 | `merged::PZO22001 Starfinder Player Core 442-464::/page/12/Text/6` | 0.561190 | casting spells 298 |
| 7 | `merged::PZO22001 Starfinder Player Core 442-464::/page/12/Text/28` | 0.559774 | traditions (arcane, divine, occult, and primal) 297 |
| 8 | `merged::PZO22001 Starfinder Player Core 442-464::/page/7/Text/43` | 0.557861 | spell rank (spells have a rank instead of a level, ranging  from 1–10) 295–296 |
| 9 | `merged::PZO22001 Starfinder Player Core 442-464::/page/12/Text/10` | 0.549869 | focus spells (epiphany and warp spells) 296–297, 375– 380 |
| 10 | `merged::PZO22001 Starfinder Player Core 442-464::/page/12/Text/4` | 0.542693 | attacking with a spell 300, **394–395** |

### Query 86
- Text: What is the rule about **Ancestries** express the lineage your character hails from.  Within ancestries are heritages—subgroups that have  unique characteristics. An ancestry provides attribute  boosts (and perhaps attribute flaws), Hit Points, ancestry  feats, and sometimes additional abilities.?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 040-057::/page/1/ListItem/8']
- Expected found: `True`
- Expected rank: `1`
- Routed chapters:
  - PZO22001 Starfinder Player Core 040-057: `0.7200`
  - PZO22001 Starfinder Player Core 014-029: `0.5577`
  - PZO22001 Starfinder Player Core 092-097: `0.5197`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 040-057::/page/1/ListItem/8', 'merged::PZO22001 Starfinder Player Core 040-057::/page/11/Text/31', 'merged::PZO22001 Starfinder Player Core 040-057::/page/15/Text/32', 'merged::PZO22001 Starfinder Player Core 040-057::/page/7/Text/31', 'merged::PZO22001 Starfinder Player Core 040-057::/page/3/Text/31', 'merged::PZO22001 Starfinder Player Core 040-057::/page/9/Text/51', 'merged::PZO22001 Starfinder Player Core 040-057::/page/1/ListItem/9', 'merged::PZO22001 Starfinder Player Core 040-057::/page/5/Text/66', 'merged::PZO22001 Starfinder Player Core 040-057::/page/1/Text/37', 'merged::PZO22001 Starfinder Player Core 040-057::/page/17/Text/56', 'merged::PZO22001 Starfinder Player Core 040-057::/page/13/Text/62', 'merged::PZO22001 Starfinder Player Core 040-057::/page/1/Text/7']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 040-057::/page/11/Text/31` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 040-057::/page/15/Text/32` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 040-057::/page/7/Text/31` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 040-057::/page/3/Text/31` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 040-057::/page/9/Text/51` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 040-057::/page/1/ListItem/9` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 040-057::/page/5/Text/66` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 040-057::/page/1/Text/37` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 040-057::/page/17/Text/56` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 040-057::/page/13/Text/62` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 040-057::/page/1/Text/7` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 040-057::/page/1/ListItem/8` | 0.949964 | **Ancestries** express the lineage your character hails from.  Within ancestries are heritages—subgroups that have  unique characteristics. An ancestry provides attribute  boosts (and perhaps attribut |
| 2 | `merged::PZO22001 Starfinder Player Core 014-029::/page/9/Text/3` | 0.709607 | **Ancestry:** Each ancestry provides attribute boosts, and sometimes an attribute flaw. If you're taking any voluntary  flaws, apply them in this step (see the sidebar on page 25). |
| 3 | `merged::PZO22001 Starfinder Player Core 014-029::/page/5/Text/19` | 0.672065 | Select an ancestry for your character. The ancestry  summaries on page 27 provide an overview of Starfinder's  core ancestry options, and each is fully detailed in Chapter  2. Ancestry determines your |
| 4 | `merged::PZO22001 Starfinder Player Core 014-029::/page/10/Text/2` | 0.667918 | The attribute boosts and flaws listed in each ancestry  represent general trends or help guide players to  create the kinds of characters from that ancestry most  likely to pursue the life of an adven |
| 5 | `merged::PZO22001 Starfinder Player Core 040-057::/page/1/Text/23` | 0.649851 | **Alternate** **Ancestry** **Boosts:** Because of the wide variety of  people within any ancestry, you can *always* choose to take two  free boosts to represent your character, even if the ancestry  n |
| 6 | `merged::PZO22001 Starfinder Player Core 014-029::/page/4/Text/2` | 0.648186 | On pages 27–28, you'll see a visual representation  of ancestries and classes that provides at-a-glance  information for players looking to make the most of  their starting attribute modifiers. In the |
| 7 | `merged::PZO22001 Starfinder Player Core 040-057::/page/1/Text/21` | 0.647241 | When creating a character of this ancestry, you apply attribute |
| 8 | `merged::PZO22001 Starfinder Player Core 014-029::/page/0/Text/6` | 0.646280 | The rules for ancestries and heritages representing the  Pact Worlds are in this chapter, including their ancestry  feat options. Backgrounds are at the end of this chapter,  along with a section abou |
| 9 | `merged::PZO22001 Starfinder Player Core 040-057::/page/1/Text/29` | 0.644141 | Any other entries in the sidebar represent abilities, senses,  and other qualities all members of the ancestry manifest.  These are omitted for ancestries with no special rules. |
| 10 | `merged::PZO22001 Starfinder Player Core 040-057::/page/1/Text/31` | 0.638279 | You select a heritage at 1st level to reflect abilities common  among those of your ancestry in the environment where  you were born or grew up. You have only one heritage and  can't change it later. |

### Query 87
- Text: What are the requirements for **SENSE ABNORMALITIES** **FEAT 12**?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/39']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 210-231: `0.3324`
  - PZO22001 Starfinder Player Core 424-441: `0.3188`
  - PZO22001 Starfinder Player Core 182-209: `0.2390`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/39', 'merged::PZO22001 Starfinder Player Core 162-173::/page/10/Text/41', 'merged::PZO22001 Starfinder Player Core 162-173::/page/10/Text/38']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 162-173::/page/10/Text/41` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 162-173::/page/10/Text/38` (reasons: ['graph_depth_1'])

### Query 88
- Text: What is the rule about **ANCESTRIES & ** **BACKGROUNDS**?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 268-281::/page/1/Text/67']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 040-057: `0.4405`
  - PZO22001 Starfinder Player Core 092-097: `0.3655`
  - PZO22001 Starfinder Player Core 014-029: `0.3538`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 268-281::/page/1/Text/67', 'merged::PZO22001 Starfinder Player Core 268-281::/page/13/Text/39', 'merged::PZO22001 Starfinder Player Core 268-281::/page/7/Text/29', 'merged::PZO22001 Starfinder Player Core 268-281::/page/9/Text/25', 'merged::PZO22001 Starfinder Player Core 268-281::/page/1/Text/68', 'merged::PZO22001 Starfinder Player Core 268-281::/page/5/Text/68', 'merged::PZO22001 Starfinder Player Core 268-281::/page/11/Text/40', 'merged::PZO22001 Starfinder Player Core 268-281::/page/1/Text/66']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 268-281::/page/13/Text/39` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 268-281::/page/7/Text/29` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 268-281::/page/9/Text/25` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 268-281::/page/1/Text/68` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 268-281::/page/5/Text/68` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 268-281::/page/11/Text/40` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 268-281::/page/1/Text/66` (reasons: ['graph_depth_1'])

### Query 89
- Text: Summarize IMPRECISE SENSES
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/20']
- Expected found: `True`
- Expected rank: `1`
- Routed chapters:
  - PZO22001 Starfinder Player Core 424-441: `0.2977`
  - PZO22001 Starfinder Player Core 182-209: `0.1850`
  - PZO22001 Starfinder Player Core 126-137: `0.1842`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/20', 'merged::PZO22001 Starfinder Player Core 424-441::/page/0/Text/19', 'merged::PZO22001 Starfinder Player Core 424-441::/page/0/Text/21']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 424-441::/page/0/Text/19` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 424-441::/page/0/Text/21` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/20` | 0.872865 | IMPRECISE SENSES |
| 2 | `merged::PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/15` | 0.606626 | SENSES |
| 3 | `merged::PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/17` | 0.605142 | PRECISE SENSES |
| 4 | `merged::PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/25` | 0.523668 | SPECIAL SENSES |
| 5 | `merged::PZO22001 Starfinder Player Core 424-441::/page/0/Text/21` | 0.487243 | Average hearing is an imprecise sense—it can't detect the  full range of detail that a precise sense can. You can usually  sense a creature automatically with an imprecise sense, but  it has the hidde |
| 6 | `merged::PZO22001 Starfinder Player Core 424-441::/page/0/Text/16` | 0.480563 | The ways a creature can use Perception depend on what  senses it has. The primary concepts you need to know for  understanding senses are precise senses, imprecise senses,  and the three states of det |
| 7 | `merged::PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/24` | 0.468260 | INCREDIBLE SENSES 19TH |
| 8 | `merged::PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/22` | 0.450819 | VAGUE SENSES |
| 9 | `merged::PZO22001 Starfinder Player Core 424-441::/page/14/Text/21` | 0.435901 | have another precise sense besides sight, you might be able  to observe a creature or object using that sense instead. You  can observe a creature with only your precise senses. When  Seeking a creatu |
| 10 | `merged::PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/15` | 0.429806 | **DETECTING WITH OTHER SENSES** |

### Query 90
- Text: What is the rule about Attribute boosts, skill feat, solarian feat?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/409']
- Expected found: `True`
- Expected rank: `1`
- Routed chapters:
  - PZO22001 Starfinder Player Core 210-231: `0.5320`
  - PZO22001 Starfinder Player Core 138-149: `0.5072`
  - PZO22001 Starfinder Player Core 174-181: `0.4852`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/409', 'merged::PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/410', 'merged::PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/408']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/410` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/408` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/409` | 0.862263 | Attribute boosts, skill feat, solarian feat |
| 2 | `merged::PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/429` | 0.862263 | Attribute boosts, skill feat, solarian feat |
| 3 | `merged::PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/417` | 0.700242 | Skill feat, solarian feat |
| 4 | `merged::PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/413` | 0.700242 | Skill feat, solarian feat |
| 5 | `merged::PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/421` | 0.700242 | Skill feat, solarian feat |
| 6 | `merged::PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/393` | 0.700242 | Skill feat, solarian feat |
| 7 | `merged::PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/425` | 0.700242 | Skill feat, solarian feat |
| 8 | `merged::PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/397` | 0.700242 | Skill feat, solarian feat |
| 9 | `merged::PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/401` | 0.700242 | Skill feat, solarian feat |
| 10 | `merged::PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/405` | 0.700242 | Skill feat, solarian feat |

### Query 91
- Text: What are the requirements for **Prerequisites** Center Thoughts?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 058-073::/page/3/Text/48']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 014-029: `0.2081`
  - PZO22001 Starfinder Player Core 092-097: `0.2063`
  - PZO22001 Starfinder Player Core 182-209: `0.2056`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 058-073::/page/3/Text/48', 'merged::PZO22001 Starfinder Player Core 058-073::/page/3/Text/49', 'merged::PZO22001 Starfinder Player Core 058-073::/page/3/Text/47']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 058-073::/page/3/Text/49` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 058-073::/page/3/Text/47` (reasons: ['graph_depth_1'])

### Query 92
- Text: What are the requirements for **HAMPERING FLARE **[one-action] **FEAT 1**?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/8']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 406-423: `0.3731`
  - PZO22001 Starfinder Player Core 442-464: `0.3229`
  - PZO22001 Starfinder Player Core 014-029: `0.3145`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/8', 'merged::PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/10', 'merged::PZO22001 Starfinder Player Core 138-149::/page/5/Text/7']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/10` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 138-149::/page/5/Text/7` (reasons: ['graph_depth_1'])

### Query 93
- Text: Summarize **GLOSSARY & ** **INDEX**
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 138-149::/page/1/Text/47']
- Expected found: `True`
- Expected rank: `8`
- Routed chapters:
  - PZO22001 Starfinder Player Core 250-267: `0.3114`
  - PZO22001 Starfinder Player Core 138-149: `0.2811`
  - PZO22001 Starfinder Player Core 182-209: `0.2809`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 138-149::/page/1/Text/47', 'merged::PZO22001 Starfinder Player Core 138-149::/page/1/Text/48', 'merged::PZO22001 Starfinder Player Core 138-149::/page/1/Text/46']
- Expanded expected found: `True`
- Expanded expected rank: `8`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 138-149::/page/1/Text/48` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 138-149::/page/1/Text/46` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 250-267::/page/3/Text/45` | 0.943465 | **GLOSSARY & ** **INDEX** |
| 2 | `merged::PZO22001 Starfinder Player Core 182-209::/page/25/Text/37` | 0.943465 | **GLOSSARY & ** **INDEX** |
| 3 | `merged::PZO22001 Starfinder Player Core 138-149::/page/5/Text/59` | 0.943465 | **GLOSSARY & ** **INDEX** |
| 4 | `merged::PZO22001 Starfinder Player Core 138-149::/page/11/Text/46` | 0.943465 | **GLOSSARY & ** **INDEX** |
| 5 | `merged::PZO22001 Starfinder Player Core 138-149::/page/7/Text/47` | 0.943465 | **GLOSSARY & ** **INDEX** |
| 6 | `merged::PZO22001 Starfinder Player Core 182-209::/page/5/Text/32` | 0.943465 | **GLOSSARY & ** **INDEX** |
| 7 | `merged::PZO22001 Starfinder Player Core 250-267::/page/7/Text/21` | 0.943465 | **GLOSSARY & ** **INDEX** |
| 8 | `merged::PZO22001 Starfinder Player Core 138-149::/page/1/Text/47` | 0.943465 | **GLOSSARY & ** **INDEX** |
| 9 | `merged::PZO22001 Starfinder Player Core 250-267::/page/1/Text/39` | 0.943465 | **GLOSSARY & ** **INDEX** |
| 10 | `merged::PZO22001 Starfinder Player Core 250-267::/page/5/Text/45` | 0.943465 | **GLOSSARY & ** **INDEX** |

### Query 94
- Text: What are the requirements for **VOID BLOOD** **FEAT 5**?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 074-091::/page/13/Text/6']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 210-231: `0.2674`
  - PZO22001 Starfinder Player Core 150-161: `0.2538`
  - PZO22001 Starfinder Player Core 098-113: `0.2514`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 074-091::/page/13/Text/6', 'merged::PZO22001 Starfinder Player Core 074-091::/page/13/Text/8', 'merged::PZO22001 Starfinder Player Core 074-091::/page/13/Text/5']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 074-091::/page/13/Text/8` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 074-091::/page/13/Text/5` (reasons: ['graph_depth_1'])

### Query 95
- Text: What is the rule about If you're a prepared spellcaster—such as a technomancer  (see *Starfinder Tech Core*)—you must spend time each day  preparing spells for that day. At the start of your daily  preparations, you select a number of spells of different  spell ranks, determined by your character level and class.  Your spells remain prepared until you cast them or until you  prepare spells again.?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 294-329::/page/1/Text/8']
- Expected found: `True`
- Expected rank: `1`
- Routed chapters:
  - PZO22001 Starfinder Player Core 294-329: `0.5299`
  - PZO22001 Starfinder Player Core 442-464: `0.4830`
  - PZO22001 Starfinder Character Sheet: `0.4763`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 294-329::/page/1/Text/8', 'merged::PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/7', 'merged::PZO22001 Starfinder Player Core 294-329::/page/1/Text/9']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/7` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 294-329::/page/1/Text/9` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 294-329::/page/1/Text/8` | 0.934632 | If you're a prepared spellcaster—such as a technomancer  (see *Starfinder Tech Core*)—you must spend time each day  preparing spells for that day. At the start of your daily  preparations, you select |
| 2 | `merged::PZO22001 Starfinder Player Core 294-329::/page/1/Text/9` | 0.682903 | Each prepared spell is expended after a single casting,  so if you want to cast a particular spell more than once in  a day, you need to prepare that spell multiple times. The  exception to this rule |
| 3 | `merged::PZO22001 Starfinder Player Core 294-329::/page/1/Text/10` | 0.668825 | You might gain an ability that allows you to swap  prepared spells or perform other aspects of preparing spells  at different times throughout the day, but only your daily  preparation counts for the |
| 4 | `merged::PZO22001 Starfinder Player Core 294-329::/page/1/Text/6` | 0.647712 | Characters of spellcasting classes can cast a number of spells  each day; the spells you can cast in a day are referred to as  spell slots. At 1st level, a character has only a small number  of 1st-ra |
| 5 | `merged::PZO22001 Starfinder Player Core 294-329::/page/1/Text/14` | 0.626996 | If you're a spontaneous spellcaster—such as a mystic—you  choose which spell from your spell repertoire that you're  using a spell slot for at the moment you decide to cast it. This  provides you with |
| 6 | `merged::PZO22001 Starfinder Player Core 442-464::/page/14/Text/17` | 0.622964 | **until the next time you make your daily preparations** A spell  with this duration lasts until you next prepare, and you can  extend it by leaving its spell slot open. 300 |
| 7 | `merged::PZO22001 Starfinder Player Core 294-329::/page/6/Text/16` | 0.613399 | If a spell's duration says it lasts until your next daily  preparations, on the next day you can refrain from preparing  a new spell in that spell's slot. (If you are a spontaneous caster,  you can in |
| 8 | `merged::PZO22001 Starfinder Player Core 294-329::/page/7/Text/4` | 0.566996 | Sometimes you need to identify a spell, especially if its  effects aren't obvious right away. If you notice a spell  being cast, and you have that spell in your repertoire  or prepared it that day (ev |
| 9 | `merged::PZO22001 Starfinder Player Core 442-464::/page/3/Text/24` | 0.562550 | **daily preparations** During your morning preparations, you  ready your gear, prepare spells, and otherwise get ready  for your adventuring day. 432 |
| 10 | `merged::PZO22001 Starfinder Player Core 294-329::/page/2/Text/5` | 0.561602 | If you're a spontaneous spellcaster, you must know a spell at  the specific rank that you want to cast it in order to heighten  it. You can add a spell to your spell repertoire at more than  a single |

### Query 96
- Text: What are the requirements for **CONFOUNDING DISQUISITION **[two-actions] **FEAT 8**?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/22']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 406-423: `0.3791`
  - PZO22001 Starfinder Player Core 424-441: `0.3289`
  - PZO22001 Starfinder Player Core 388-405: `0.3286`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/22', 'merged::PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/24', 'merged::PZO22001 Starfinder Player Core 098-113::/page/13/Text/21']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/24` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 098-113::/page/13/Text/21` (reasons: ['graph_depth_1'])

### Query 97
- Text: What does **CHRONO PUSH **[two-actions] **SPELL 5** do?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/17']
- Expected found: `True`
- Expected rank: `1`
- Routed chapters:
  - PZO22001 Starfinder Player Core 406-423: `0.3437`
  - PZO22001 Starfinder Player Core 294-329: `0.3071`
  - PZO22001 Starfinder Player Core 388-405: `0.2982`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/17', 'merged::PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/24', 'merged::PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/6']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/24` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/6` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/17` | 0.678147 | **CHRONO PUSH **[two-actions] **SPELL 5**  **ATTACK** **CONCENTRATE** **FORCE** **MANIPULATE**  **Traditions** occult  **Range **500 feet;** Targets** 1 creature **Defense** AC and basic Reflex  You p |
| 2 | `merged::PZO22001 Starfinder Player Core 294-329::/page/15/Text/42` | 0.582036 | **Chrono** **Push ** H Push a target away and damage creatures  nearby. |
| 3 | `merged::PZO22001 Starfinder Player Core 294-329::/page/7/Text/19` | 0.533065 | **SPELL NAME **[one-action] **SPELL (RANK)** |
| 4 | `merged::PZO22001 Starfinder Player Core 294-329::/page/19/Text/59` | 0.455753 | **SPELLS** |
| 5 | `merged::PZO22001 Starfinder Player Core 294-329::/page/3/Text/36` | 0.455753 | **SPELLS** |
| 6 | `merged::PZO22001 Starfinder Player Core 294-329::/page/15/Text/80` | 0.455753 | **SPELLS** |
| 7 | `merged::PZO22001 Starfinder Player Core 406-423::/page/13/Text/35` | 0.455753 | **SPELLS** |
| 8 | `merged::PZO22001 Starfinder Player Core 294-329::/page/29/Text/65` | 0.455753 | **SPELLS** |
| 9 | `merged::PZO22001 Starfinder Player Core 294-329::/page/27/Text/68` | 0.455753 | **SPELLS** |
| 10 | `merged::PZO22001 Starfinder Player Core 294-329::/page/35/Text/68` | 0.455753 | **SPELLS** |

### Query 98
- Text: What is the rule about beyond the Universe. Mystics connected with the cosmic  forces of healing and shadows are divine spellcasters.?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 294-329::/page/3/Text/11']
- Expected found: `True`
- Expected rank: `1`
- Routed chapters:
  - PZO22001 Starfinder Player Core 114-125: `0.5723`
  - PZO22001 Starfinder Player Core 294-329: `0.5000`
  - PZO22001 Starfinder Player Core 330-363: `0.4266`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 294-329::/page/3/Text/11', 'merged::PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/13', 'merged::PZO22001 Starfinder Player Core 294-329::/page/3/Text/10']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/13` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 294-329::/page/3/Text/10` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 294-329::/page/3/Text/11` | 0.927953 | beyond the Universe. Mystics connected with the cosmic  forces of healing and shadows are divine spellcasters. |
| 2 | `merged::PZO22001 Starfinder Player Core 114-125::/page/2/Text/9` | 0.653563 | All mystics have a supernatural connection with a cosmic force  that grants magical powers. The exact nature of your connection  can vary widely—you might worship a god or pantheon, embody  a metaphys |
| 3 | `merged::PZO22001 Starfinder Player Core 294-329::/page/1/Text/3` | 0.606783 | Even with the widespread presence of technology,  spellcasters can be found in every corner of the galaxy.  Some spellcasters draw magic from other realities, some  from their mystical connections to |
| 4 | `merged::PZO22001 Starfinder Player Core 114-125::/page/3/Text/3` | 0.593502 | You are a spellcaster and can cast spells using the Cast a Spell  activity (see Casting Spells on page 298). As a mystic, when  you cast spells, you might intone a prayer or hum a song  inspired by yo |
| 5 | `merged::PZO22001 Starfinder Player Core 294-329::/page/3/Text/15` | 0.588439 | systematic way. Witchwarpers touched by the Gap or  alternate timelines, as well as mystics who are psychically  linked to the Akashic Record, are occult spellcasters. |
| 6 | `merged::PZO22001 Starfinder Player Core 294-329::/page/3/Text/18` | 0.566392 | An instinctual connection to and faith in the  world, the cycle of day and night, the turning  of the seasons, and the natural selection of predator and  prey drive the primal tradition. Mystics conne |
| 7 | `merged::PZO22001 Starfinder Player Core 114-125::/page/7/Text/14` | 0.518819 | **Prerequisites** connection with divine spellcasting, you  worship a deity |
| 8 | `merged::PZO22001 Starfinder Player Core 294-329::/page/1/Text/4` | 0.516984 | With special gestures and utterances, a spellcaster can  call forth mystic energies, warp the mind, protect themself  against danger, or even create something from nothing.  Each class has its own met |
| 9 | `merged::PZO22001 Starfinder Player Core 114-125::/page/1/Text/2` | 0.505313 | You're a conduit, channeling the fundamental forces that connect and bind everything in the cosmos.  You can draw upon this supernatural wellspring to form deep spiritual bonds with your allies,  empo |
| 10 | `merged::PZO22001 Starfinder Player Core 294-329::/page/1/Text/12` | 0.500607 | After Triune's Signal connected cultures across the  Universe, the peoples of the galaxy have learned more  than ever before about the Universe's composition  thanks to science and technology. As tech |

### Query 99
- Text: Summarize these stones are purportedly all fragments of crystal tools  used by otherworldly entities to build the Universe in  ancient times.
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 282-293::/page/1/Text/1']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 294-329: `0.3657`
  - PZO22001 Starfinder Player Core 030-039: `0.3606`
  - PZO22001 Starfinder Player Core 330-363: `0.3473`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 282-293::/page/1/Text/1', 'merged::PZO22001 Starfinder Player Core 282-293::/page/1/Text/2', 'merged::PZO22001 Starfinder Player Core 282-293::/page/0/Text/26']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 282-293::/page/1/Text/2` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 282-293::/page/0/Text/26` (reasons: ['graph_depth_1'])

### Query 100
- Text: Summarize **Leveling Up**
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 014-029::/page/5/Text/30']
- Expected found: `True`
- Expected rank: `2`
- Routed chapters:
  - PZO22001 Starfinder Player Core 098-113: `0.2932`
  - PZO22001 Starfinder Player Core 014-029: `0.2375`
  - PZO22001 Starfinder Player Core 040-057: `0.2318`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 014-029::/page/5/Text/30', 'merged::PZO22001 Starfinder Player Core 014-029::/page/5/Text/29', 'merged::PZO22001 Starfinder Player Core 014-029::/page/5/Text/31']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 014-029::/page/5/Text/29` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 014-029::/page/5/Text/31` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 014-029::/page/13/Text/4` | 0.920922 | **Leveling Up** |
| 2 | `merged::PZO22001 Starfinder Player Core 014-029::/page/5/Text/30` | 0.920922 | **Leveling Up** |
| 3 | `merged::PZO22001 Starfinder Player Core 014-029::/page/11/Text/29` | 0.920922 | **Leveling Up** |
| 4 | `merged::PZO22001 Starfinder Player Core 014-029::/page/1/Text/20` | 0.920922 | **Leveling Up** |
| 5 | `merged::PZO22001 Starfinder Player Core 014-029::/page/9/Text/26` | 0.920922 | **Leveling Up** |
| 6 | `merged::PZO22001 Starfinder Player Core 014-029::/page/15/Text/25` | 0.920922 | **Leveling Up** |
| 7 | `merged::PZO22001 Starfinder Player Core 014-029::/page/15/SectionHeader/0` | 0.799826 | LEVELING UP |
| 8 | `merged::PZO22001 Starfinder Player Core 014-029::/page/15/SectionHeader/11` | 0.653624 | **LEVELING-UP CHECKLIST** |
| 9 | `merged::PZO22001 Starfinder Player Core 014-029::/page/7/Text/18` | 0.602760 | Leveling Up |
| 10 | `merged::PZO22001 Starfinder Player Core 098-113::/page/1/ListItem/6` | 0.598633 | **Leveling Up **on page 29 tells you how to make your  character stronger when you get enough Experience  Points to reach a new level. |

### Query 101
- Text: What is the rule about **SKILLS** **FEATS**?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 250-267::/page/1/Text/23']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 210-231: `0.5697`
  - PZO22001 Starfinder Player Core 182-209: `0.4789`
  - PZO22001 Starfinder Player Core 014-029: `0.3554`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 250-267::/page/1/Text/23', 'merged::PZO22001 Starfinder Player Core 250-267::/page/1/Text/24', 'merged::PZO22001 Starfinder Player Core 250-267::/page/1/Text/22']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 250-267::/page/1/Text/24` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 250-267::/page/1/Text/22` (reasons: ['graph_depth_1'])

### Query 102
- Text: What is the rule about **Activate—Defensive Detonation **[one-action] (manipulate) **Requirements** You have a stored grenade; **Effect** You detonate the grenade  stored in the explosive defense unit. The explosion is centered  on your space, but the upgrade generates a containment  field to protect you from its effects. The grenade otherwise  functions as if you'd activated it normally.?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 268-281::/page/1/Text/58']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 406-423: `0.4741`
  - PZO22001 Starfinder Player Core 424-441: `0.4031`
  - PZO22001 Starfinder Player Core 388-405: `0.4028`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 268-281::/page/1/Text/58', 'merged::PZO22001 Starfinder Player Core 268-281::/page/1/Text/60', 'merged::PZO22001 Starfinder Player Core 268-281::/page/1/Text/57']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 268-281::/page/1/Text/60` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 268-281::/page/1/Text/57` (reasons: ['graph_depth_1'])

### Query 103
- Text: What are the requirements for **REMIX WORLD'S RHYTHM** **FEAT 13**?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/37']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 014-029: `0.2941`
  - PZO22001 Starfinder Player Core 210-231: `0.2879`
  - PZO22001 Starfinder Player Core 442-464: `0.2661`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/37', 'merged::PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/36', 'merged::PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/39']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/36` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/39` (reasons: ['graph_depth_1'])

### Query 104
- Text: Summarize Shield Block
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/450']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 250-267: `0.4770`
  - PZO22001 Starfinder Player Core 014-029: `0.2678`
  - PZO22001 Starfinder Player Core 150-161: `0.2609`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/450', 'merged::PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/449', 'merged::PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/451']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/449` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/451` (reasons: ['graph_depth_1'])

### Query 105
- Text: What does **GENETIC REGENERATION **[two-actions] **SPELL 4** do?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 330-363::/page/4/SectionHeader/2']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 406-423: `0.3619`
  - PZO22001 Starfinder Player Core 282-293: `0.3279`
  - PZO22001 Starfinder Player Core 210-231: `0.3196`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 330-363::/page/4/SectionHeader/2', 'merged::PZO22001 Starfinder Player Core 330-363::/page/4/Text/1', 'merged::PZO22001 Starfinder Player Core 330-363::/page/4/SectionHeader/10']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 330-363::/page/4/Text/1` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 330-363::/page/4/SectionHeader/10` (reasons: ['graph_depth_1'])

### Query 106
- Text: What is the rule about Spellcasting classes grant a proficiency rank for spell  attacks and DCs, which are further detailed in each class's  entry. These classes rarely use their class DC.?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 098-113::/page/2/Text/7']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 182-209: `0.5458`
  - PZO22001 Starfinder Player Core 442-464: `0.5060`
  - PZO22001 Starfinder Player Core 210-231: `0.4830`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 098-113::/page/2/Text/7', 'merged::PZO22001 Starfinder Player Core 098-113::/page/2/Text/8', 'merged::PZO22001 Starfinder Player Core 098-113::/page/2/Text/6']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 098-113::/page/2/Text/8` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 098-113::/page/2/Text/6` (reasons: ['graph_depth_1'])

### Query 107
- Text: What is the rule about **Trigger** A creature Casts a Spell with the mental trait.?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 058-073::/page/3/Text/54']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 294-329: `0.4599`
  - PZO22001 Starfinder Player Core 442-464: `0.4540`
  - PZO22001 Starfinder Player Core 182-209: `0.4278`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 058-073::/page/3/Text/54', 'merged::PZO22001 Starfinder Player Core 058-073::/page/3/Text/55', 'merged::PZO22001 Starfinder Player Core 058-073::/page/3/Text/53']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 058-073::/page/3/Text/55` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 058-073::/page/3/Text/53` (reasons: ['graph_depth_1'])

### Query 108
- Text: Summarize Mystic envoys can choose between using their magic  or directives to empower their allies, widening the  breadth of options available to them.
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 174-181::/page/1/ListItem/5']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 114-125: `0.5228`
  - PZO22001 Starfinder Player Core 098-113: `0.5177`
  - PZO22001 Starfinder Player Core 364-387: `0.4987`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 174-181::/page/1/ListItem/5', 'merged::PZO22001 Starfinder Player Core 174-181::/page/1/Text/4', 'merged::PZO22001 Starfinder Player Core 174-181::/page/1/ListItem/6']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 174-181::/page/1/Text/4` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 174-181::/page/1/ListItem/6` (reasons: ['graph_depth_1'])

### Query 109
- Text: What are the requirements for **WORMHOLE **[two-actions] **FEAT 12**?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 138-149::/page/10/SectionHeader/11']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 182-209: `0.3313`
  - PZO22001 Starfinder Player Core 406-423: `0.3270`
  - PZO22001 Starfinder Player Core 388-405: `0.3252`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 138-149::/page/10/SectionHeader/11', 'merged::PZO22001 Starfinder Player Core 138-149::/page/10/Text/13', 'merged::PZO22001 Starfinder Player Core 138-149::/page/10/Text/10']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 138-149::/page/10/Text/13` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 138-149::/page/10/Text/10` (reasons: ['graph_depth_1'])

### Query 110
- Text: What are the requirements for **SITUATIONAL AWARENESS **[two-actions] **FEAT 12**?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/19']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 424-441: `0.3871`
  - PZO22001 Starfinder Player Core 406-423: `0.3315`
  - PZO22001 Starfinder Player Core 210-231: `0.3255`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/19', 'merged::PZO22001 Starfinder Player Core 098-113::/page/14/Text/18', 'merged::PZO22001 Starfinder Player Core 098-113::/page/14/Text/21']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 098-113::/page/14/Text/18` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 098-113::/page/14/Text/21` (reasons: ['graph_depth_1'])

### Query 111
- Text: What is the rule about **Type **tactical; **Level **19; **Price **350,000 credits?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 268-281::/page/2/Text/31']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 232-249: `0.4289`
  - PZO22001 Starfinder Player Core 388-405: `0.4123`
  - PZO22001 Starfinder Player Core 014-029: `0.4078`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 268-281::/page/2/Text/31', 'merged::PZO22001 Starfinder Player Core 268-281::/page/2/Text/30', 'merged::PZO22001 Starfinder Player Core 268-281::/page/2/Text/32']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 268-281::/page/2/Text/30` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 268-281::/page/2/Text/32` (reasons: ['graph_depth_1'])

### Query 112
- Text: Summarize TOUCH RANGE
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/16']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 250-267: `0.3239`
  - PZO22001 Starfinder Player Core 406-423: `0.2951`
  - PZO22001 Starfinder Player Core 388-405: `0.2609`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/16', 'merged::PZO22001 Starfinder Player Core 294-329::/page/4/Text/15', 'merged::PZO22001 Starfinder Player Core 294-329::/page/4/Text/17']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 294-329::/page/4/Text/15` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 294-329::/page/4/Text/17` (reasons: ['graph_depth_1'])

### Query 113
- Text: What are the requirements for **CROWD CONTROL** **FEAT 2**?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 210-231::/page/8/Text/17']
- Expected found: `True`
- Expected rank: `1`
- Routed chapters:
  - PZO22001 Starfinder Player Core 210-231: `0.3300`
  - PZO22001 Starfinder Player Core 150-161: `0.2665`
  - PZO22001 Starfinder Player Core 406-423: `0.2553`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 210-231::/page/8/Text/17', 'merged::PZO22001 Starfinder Player Core 210-231::/page/8/Text/16', 'merged::PZO22001 Starfinder Player Core 210-231::/page/8/Text/19']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 210-231::/page/8/Text/16` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 210-231::/page/8/Text/19` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 210-231::/page/8/Text/17` | 0.869761 | **CROWD CONTROL** **FEAT 2** |
| 2 | `merged::PZO22001 Starfinder Player Core 210-231::/page/8/Text/26` | 0.584927 | **CROWD SURFING** **FEAT 1** |
| 3 | `merged::PZO22001 Starfinder Player Core 210-231::/page/10/SectionHeader/22` | 0.547566 | **FACE IN THE CROWD** **FEAT 1** |
| 4 | `merged::PZO22001 Starfinder Player Core 210-231::/page/7/Text/17` | 0.535054 | **BREATH CONTROL** **FEAT 1** |
| 5 | `merged::PZO22001 Starfinder Player Core 210-231::/page/14/SectionHeader/34` | 0.533952 | **NIMBLE CRAWL** **FEAT 2** |
| 6 | `merged::PZO22001 Starfinder Player Core 210-231::/page/19/SectionHeader/26` | 0.487995 | **TECH CRAFTING** **FEAT 2** |
| 7 | `merged::PZO22001 Starfinder Player Core 210-231::/page/12/SectionHeader/41` | 0.473361 | **INVENTOR** **FEAT 2** |
| 8 | `merged::PZO22001 Starfinder Player Core 210-231::/page/6/SectionHeader/38` | 0.435813 | **AUTOMATIC KNOWLEDGE** **FEAT 2** |
| 9 | `merged::PZO22001 Starfinder Player Core 150-161::/page/3/SectionHeader/21` | 0.419793 | SKILL FEATS 2ND |
| 10 | `merged::PZO22001 Starfinder Player Core 210-231::/page/8/Text/4` | 0.416933 | **CONFABULATOR** **FEAT 2** |

### Query 114
- Text: Summarize **UNCOMMON**
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 092-097::/page/1/SectionHeader/32']
- Expected found: `True`
- Expected rank: `2`
- Routed chapters:
  - PZO22001 Starfinder Player Core 092-097: `0.2578`
  - PZO22001 Starfinder Player Core 330-363: `0.2471`
  - PZO22001 Starfinder Player Core 282-293: `0.2445`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 092-097::/page/1/SectionHeader/32', 'merged::PZO22001 Starfinder Player Core 092-097::/page/1/SectionHeader/31', 'merged::PZO22001 Starfinder Player Core 092-097::/page/1/Text/33']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 092-097::/page/1/SectionHeader/31` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 092-097::/page/1/Text/33` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 092-097::/page/4/SectionHeader/33` | 0.906210 | **UNCOMMON** |
| 2 | `merged::PZO22001 Starfinder Player Core 092-097::/page/1/SectionHeader/32` | 0.906210 | **UNCOMMON** |
| 3 | `merged::PZO22001 Starfinder Player Core 282-293::/page/0/Text/24` | 0.581839 | **UNCOMMON** **INVESTED** **MAGICAL** |
| 4 | `merged::PZO22001 Starfinder Player Core 092-097::/page/5/TableCell/490` | 0.469874 | Common |
| 5 | `merged::PZO22001 Starfinder Player Core 092-097::/page/5/SectionHeader/10` | 0.467600 | **UNCOMMON EXTRAPLANAR LANGUAGES** |
| 6 | `merged::PZO22001 Starfinder Player Core 092-097::/page/5/SectionHeader/8` | 0.393969 | **COMMON REGIONAL LANGUAGES** |
| 7 | `merged::PZO22001 Starfinder Player Core 092-097::/page/5/SectionHeader/6` | 0.393444 | **COMMON ANCESTRY LANGUAGES** |
| 8 | `merged::PZO22001 Starfinder Player Core 282-293::/page/3/Text/38` | 0.383097 | **Introduction** |
| 9 | `merged::PZO22001 Starfinder Player Core 282-293::/page/9/Text/42` | 0.383097 | **Introduction** |
| 10 | `merged::PZO22001 Starfinder Player Core 282-293::/page/7/Text/66` | 0.383097 | **Introduction** |

### Query 115
- Text: What is the rule about An instinctual connection to and faith in the  world, the cycle of day and night, the turning  of the seasons, and the natural selection of predator and  prey drive the primal tradition. Mystics connected to  the primordial elements and underlying rhythms of the  cosmos are primal spellcasters.?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 294-329::/page/3/Text/18']
- Expected found: `True`
- Expected rank: `1`
- Routed chapters:
  - PZO22001 Starfinder Player Core 294-329: `0.5139`
  - PZO22001 Starfinder Player Core 114-125: `0.4848`
  - PZO22001 Starfinder Player Core 330-363: `0.4300`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 294-329::/page/3/Text/18', 'merged::PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/17', 'merged::PZO22001 Starfinder Player Core 294-329::/page/3/Text/19']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/17` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 294-329::/page/3/Text/19` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 294-329::/page/3/Text/18` | 0.953244 | An instinctual connection to and faith in the  world, the cycle of day and night, the turning  of the seasons, and the natural selection of predator and  prey drive the primal tradition. Mystics conne |
| 2 | `merged::PZO22001 Starfinder Player Core 114-125::/page/6/Text/7` | 0.620077 | **Tradition** primal; **Connection Skill** Nature |
| 3 | `merged::PZO22001 Starfinder Player Core 114-125::/page/2/Text/9` | 0.610927 | All mystics have a supernatural connection with a cosmic force  that grants magical powers. The exact nature of your connection  can vary widely—you might worship a god or pantheon, embody  a metaphys |
| 4 | `merged::PZO22001 Starfinder Player Core 114-125::/page/8/Text/44` | 0.587762 | **Prerequisites** connection with primal spellcasting |
| 5 | `merged::PZO22001 Starfinder Player Core 114-125::/page/7/Text/29` | 0.587762 | **Prerequisites** connection with primal spellcasting |
| 6 | `merged::PZO22001 Starfinder Player Core 114-125::/page/10/Text/4` | 0.587762 | **Prerequisites** connection with primal spellcasting |
| 7 | `merged::PZO22001 Starfinder Player Core 330-363::/page/12/Text/45` | 0.580678 | **Traditions** divine, primal |
| 8 | `merged::PZO22001 Starfinder Player Core 330-363::/page/7/Text/34` | 0.573012 | **Traditions** divine, occult, primal |
| 9 | `merged::PZO22001 Starfinder Player Core 294-329::/page/3/Text/11` | 0.564251 | beyond the Universe. Mystics connected with the cosmic  forces of healing and shadows are divine spellcasters. |
| 10 | `merged::PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/389` | 0.552652 | Ancestry and background, attribute boosts, initial proficiencies, connection, initial epiphany, mystic bond, vitality network, mystic spellcasting, spell repertoire |

### Query 116
- Text: Summarize 4
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/394']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 014-029: `0.2321`
  - PZO22001 Starfinder Player Core 282-293: `0.2317`
  - PZO22001 Starfinder Player Core 250-267: `0.2308`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/394', 'merged::PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/395', 'merged::PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/393']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/395` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/393` (reasons: ['graph_depth_1'])

### Query 117
- Text: What is the rule about **SKILLS**?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 424-441::/page/1/Text/29']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 182-209: `0.5422`
  - PZO22001 Starfinder Player Core 210-231: `0.4266`
  - PZO22001 Starfinder Player Core 442-464: `0.3689`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 424-441::/page/1/Text/29', 'merged::PZO22001 Starfinder Player Core 424-441::/page/1/Text/28', 'merged::PZO22001 Starfinder Player Core 424-441::/page/1/Text/30']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 424-441::/page/1/Text/28` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 424-441::/page/1/Text/30` (reasons: ['graph_depth_1'])

### Query 118
- Text: What is the rule about **Spell Lists**?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 364-387::/page/5/Text/73']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 294-329: `0.3662`
  - PZO22001 Starfinder Character Sheet: `0.3534`
  - PZO22001 Starfinder Player Core 442-464: `0.3474`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 364-387::/page/5/Text/73', 'merged::PZO22001 Starfinder Player Core 364-387::/page/5/Text/74', 'merged::PZO22001 Starfinder Player Core 364-387::/page/5/Text/72']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 364-387::/page/5/Text/74` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 364-387::/page/5/Text/72` (reasons: ['graph_depth_1'])

### Query 119
- Text: Summarize 13
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/505']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 250-267: `0.2419`
  - PZO22001 Starfinder Player Core 014-029: `0.2306`
  - PZO22001 Starfinder Player Core 040-057: `0.2303`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/505', 'merged::PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/506', 'merged::PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/504']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/506` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/504` (reasons: ['graph_depth_1'])

### Query 120
- Text: What is the rule about Throughout this rulebook, you will see formatting  standards that might look a bit unusual at first. These  standards are in place to make the rules elements in this  book easier to recognize.?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 014-029::/page/1/Text/2']
- Expected found: `True`
- Expected rank: `1`
- Routed chapters:
  - PZO22001 Starfinder Player Core 014-029: `0.4498`
  - PZO22001 Starfinder Player Core 424-441: `0.4161`
  - PZO22001 Starfinder Player Core 388-405: `0.4156`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 014-029::/page/1/Text/2', 'merged::PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/1', 'merged::PZO22001 Starfinder Player Core 014-029::/page/1/Text/3']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/1` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 014-029::/page/1/Text/3` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 014-029::/page/1/Text/2` | 0.923918 | Throughout this rulebook, you will see formatting  standards that might look a bit unusual at first. These  standards are in place to make the rules elements in this  book easier to recognize. |
| 2 | `merged::PZO22001 Starfinder Player Core 014-029::/page/2/Text/17` | 0.609087 | **Special** Any special qualities of the rule are explained in  this section. Usually this section appears in feats you  can select more than once, explaining what happens  when you do. |
| 3 | `merged::PZO22001 Starfinder Player Core 014-029::/page/2/Text/7` | 0.601874 | Regardless of the game mechanic they convey, rules  elements are always presented in the form of a stat block,  a summary of the rules necessary to bring the monster,  character, item, or other rules |
| 4 | `merged::PZO22001 Starfinder Player Core 014-029::/page/0/Text/2` | 0.589417 | While this chapter is here to teach you the basics of  Starfinder, the rest of this rulebook serves as a reference  manual during play, and it is organized to make finding  the rule you need as easy a |
| 5 | `merged::PZO22001 Starfinder Player Core 014-029::/page/0/Text/20` | 0.553269 | The back of this book has an  appendix with the rules for all of  the conditions that you will find  in the game. This section also  includes a blank character sheet,  and an index with a comprehensiv |
| 6 | `merged::PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/1` | 0.550390 | FORMAT OF RULES |
| 7 | `merged::PZO22001 Starfinder Player Core 388-405::/page/2/SectionHeader/1` | 0.530408 | RULES OVERVIEW |
| 8 | `merged::PZO22001 Starfinder Player Core 388-405::/page/3/Text/14` | 0.520223 | Sometimes a rule could be interpreted multiple ways. If one  version is too good to be true, it probably is. If a rule seems  to have wording with problematic repercussions or doesn't  work as intende |
| 9 | `merged::PZO22001 Starfinder Player Core 014-029::/page/2/Text/6` | 0.519426 | This book contains many rules elements that give characters  new and interesting ways to respond to situations in the  game. All characters can use the basic actions found in  Chapter 8, but an indivi |
| 10 | `merged::PZO22001 Starfinder Player Core 014-029::/page/2/Text/16` | 0.514135 | This section describes the effects or benefits of a rules  element. If the rule is an action, it explains what the effect  is or what you must roll. If it's a feat that modifies an  existing action or |

### Query 121
- Text: Summarize You're a career criminal with a nasty reputation. Perhaps  unfair circumstances forced you into a life of crime, or maybe  you enjoy the thrill you get from pulling off a heist or living  through a shoot-out. Either way, this life is the only one you  know, and thanks to the bounty on your head, you're in it  until the casket drops or you make enough creds to buy a  new one.
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 092-097::/page/3/Text/11']
- Expected found: `True`
- Expected rank: `1`
- Routed chapters:
  - PZO22001 Starfinder Player Core 092-097: `0.3976`
  - PZO22001 Starfinder Player Core 210-231: `0.3637`
  - PZO22001 Starfinder Player Core 424-441: `0.3615`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 092-097::/page/3/Text/11', 'merged::PZO22001 Starfinder Player Core 092-097::/page/3/Text/10', 'merged::PZO22001 Starfinder Player Core 092-097::/page/3/Text/12']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 092-097::/page/3/Text/10` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 092-097::/page/3/Text/12` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 092-097::/page/3/Text/11` | 0.985734 | You're a career criminal with a nasty reputation. Perhaps  unfair circumstances forced you into a life of crime, or maybe  you enjoy the thrill you get from pulling off a heist or living  through a sh |
| 2 | `merged::PZO22001 Starfinder Player Core 092-097::/page/2/Text/30` | 0.607229 | You're a con artist and trickster who swindles unsuspecting  dupes and blackmails rubes, but it's nothing personal you're just in it for the credits. You might run an operation  on the side, or you mi |
| 3 | `merged::PZO22001 Starfinder Player Core 092-097::/page/4/Text/34` | 0.557747 | You enlisted in a military or were recruited by a paramilitary  group as a career trooper. As long as you've got enough  guns and the right squad to back you up, you can handle  just about anything. |
| 4 | `merged::PZO22001 Starfinder Player Core 092-097::/page/1/Text/37` | 0.556317 | You solved crimes as a police inspector or took clandestine  jobs for various clients as a private investigator. You might  have become an adventurer as part of your next big mystery,  but it's equall |
| 5 | `merged::PZO22001 Starfinder Player Core 092-097::/page/3/Text/24` | 0.549313 | You used to be someone, but that was in another life. You keep  to yourself these days, eking out an existence as a hermit in  the wilderness or a loner in a rundown neighborhood. You  thought you put |
| 6 | `merged::PZO22001 Starfinder Player Core 092-097::/page/3/Text/15` | 0.536089 | You've been imprisoned or punished for a crime, whether  you were guilty or not. Now that your sentence has ended  or you've escaped, you take full advantage of the newfound  freedom of your adventuri |
| 7 | `merged::PZO22001 Starfinder Player Core 092-097::/page/4/Text/10` | 0.524204 | You're a crewmate on a pirate vessel with ambitions of  pillaging interstellar shipping lanes or taking over a chunk  of a notable planetary body. Perhaps you grew up on such  a ship, were taken priso |
| 8 | `merged::PZO22001 Starfinder Player Core 092-097::/page/1/Text/16` | 0.516542 | You know how to remove all traces of a crime. Whether you  worked under the table for legitimate clients like AbadarCorp  or learned your trade working for shady organizations and  crime bosses, you k |
| 9 | `merged::PZO22001 Starfinder Player Core 092-097::/page/2/Text/38` | 0.510804 | Everybody wants their 15 minutes of fame, but for you, it's  somehow become a lifestyle. Whether by luck or dedication,  you're a star performer, celebrity, or popular influencer. Your  face, voice, a |
| 10 | `merged::PZO22001 Starfinder Player Core 092-097::/page/1/Text/12` | 0.504842 | You've lived long enough in a major settlement to know  how to keep your head down, avoid direct eye contact,  and otherwise move about your day without drawing any  attention to yourself. Whether you |

### Query 122
- Text: Summarize **Trigger** Your turn begins.
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 406-423::/page/2/SectionHeader/19']
- Expected found: `True`
- Expected rank: `1`
- Routed chapters:
  - PZO22001 Starfinder Player Core 406-423: `0.3813`
  - PZO22001 Starfinder Player Core 424-441: `0.3739`
  - PZO22001 Starfinder Player Core 388-405: `0.3498`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 406-423::/page/2/SectionHeader/19', 'merged::PZO22001 Starfinder Player Core 406-423::/page/2/SectionHeader/18', 'merged::PZO22001 Starfinder Player Core 406-423::/page/2/Text/20']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 406-423::/page/2/SectionHeader/18` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 406-423::/page/2/Text/20` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 406-423::/page/2/SectionHeader/19` | 0.960189 | **Trigger** Your turn begins. |
| 2 | `merged::PZO22001 Starfinder Player Core 406-423::/page/4/Text/31` | 0.704709 | **Trigger** You fall. |
| 3 | `merged::PZO22001 Starfinder Player Core 424-441::/page/4/ListItem/7` | 0.697262 | You can use 1 free action or reaction with a trigger of  "Your turn begins" or something similar. |
| 4 | `merged::PZO22001 Starfinder Player Core 406-423::/page/5/Text/16` | 0.635049 | **Trigger** You fall from or past an edge or handhold. |
| 5 | `merged::PZO22001 Starfinder Player Core 424-441::/page/4/ListItem/21` | 0.610902 | You can use 1 free action or reaction with a trigger of  "Your turn ends" or something similar. |
| 6 | `merged::PZO22001 Starfinder Player Core 406-423::/page/2/Text/8` | 0.596976 | **Trigger** An ally is about to use an action that requires a skill  check or attack roll. |
| 7 | `merged::PZO22001 Starfinder Player Core 406-423::/page/8/Text/5` | 0.596434 | **Trigger** A creature within your reach uses a manipulate  action or a move action, makes a ranged attack, or  leaves a square during a move action it's using. |
| 8 | `merged::PZO22001 Starfinder Player Core 424-441::/page/3/SectionHeader/20` | 0.587008 | STEP 1: START YOUR TURN |
| 9 | `merged::PZO22001 Starfinder Player Core 406-423::/page/3/Text/8` | 0.556464 | You prepare to use an action that will occur outside your  turn. Choose a single action or free action you can use, and  designate a trigger. Your turn then ends. If the trigger you  designated occurs |
| 10 | `merged::PZO22001 Starfinder Player Core 424-441::/page/4/Text/10` | 0.547350 | The last step of starting your turn is always the same. |

### Query 123
- Text: Summarize LEVELING UP29
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/134']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 098-113: `0.2515`
  - PZO22001 Starfinder Player Core 424-441: `0.2146`
  - PZO22001 Starfinder Player Core 040-057: `0.2028`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/134', 'merged::PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/136', 'merged::PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/132']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/136` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/132` (reasons: ['graph_depth_1'])

### Query 124
- Text: What is the rule about ACTIONS?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 406-423::/page/0/SectionHeader/1']
- Expected found: `True`
- Expected rank: `1`
- Routed chapters:
  - PZO22001 Starfinder Player Core 406-423: `0.5312`
  - PZO22001 Starfinder Player Core 424-441: `0.3746`
  - PZO22001 Starfinder Player Core 388-405: `0.3709`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 406-423::/page/0/SectionHeader/1', 'merged::PZO22001 Starfinder Player Core 406-423::/page/0/Text/2']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 406-423::/page/0/Text/2` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 406-423::/page/0/SectionHeader/1` | 0.722859 | ACTIONS |
| 2 | `merged::PZO22001 Starfinder Player Core 388-405::/page/2/SectionHeader/7` | 0.722859 | ACTIONS |
| 3 | `merged::PZO22001 Starfinder Player Core 406-423::/page/1/Text/11` | 0.716222 | These rules clarify some of the specifics of using actions. |
| 4 | `merged::PZO22001 Starfinder Player Core 406-423::/page/3/Text/48` | 0.669885 | **Actions** |
| 5 | `merged::PZO22001 Starfinder Player Core 406-423::/page/5/Text/61` | 0.669885 | **Actions** |
| 6 | `merged::PZO22001 Starfinder Player Core 406-423::/page/1/Text/36` | 0.669885 | **Actions** |
| 7 | `merged::PZO22001 Starfinder Player Core 388-405::/page/1/Text/36` | 0.669885 | **Actions** |
| 8 | `merged::PZO22001 Starfinder Player Core 424-441::/page/9/Text/43` | 0.669885 | **Actions** |
| 9 | `merged::PZO22001 Starfinder Player Core 424-441::/page/7/Text/60` | 0.669885 | **Actions** |
| 10 | `merged::PZO22001 Starfinder Player Core 388-405::/page/13/Text/40` | 0.669885 | **Actions** |

### Query 125
- Text: Summarize **Solarian**
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 126-137::/page/1/Text/35']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 138-149: `0.5425`
  - PZO22001 Starfinder Player Core 030-039: `0.2832`
  - PZO22001 Starfinder Player Core 150-161: `0.2812`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 126-137::/page/1/Text/35', 'merged::PZO22001 Starfinder Player Core 126-137::/page/1/Text/36', 'merged::PZO22001 Starfinder Player Core 126-137::/page/1/Text/34']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 126-137::/page/1/Text/36` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 126-137::/page/1/Text/34` (reasons: ['graph_depth_1'])

### Query 126
- Text: What is the rule about Armor expertise, general feat, skill increase,?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/402']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 210-231: `0.5832`
  - PZO22001 Starfinder Player Core 182-209: `0.5409`
  - PZO22001 Starfinder Player Core 098-113: `0.4752`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/402', 'merged::PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/401', 'merged::PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/403']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/401` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/403` (reasons: ['graph_depth_1'])

### Query 127
- Text: What are the requirements for **Prerequisites** Watch Out?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/34']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 424-441: `0.2401`
  - PZO22001 Starfinder Player Core 092-097: `0.2109`
  - PZO22001 Starfinder Player Core 250-267: `0.2087`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/34', 'merged::PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/33', 'merged::PZO22001 Starfinder Player Core 098-113::/page/13/Text/35']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/33` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 098-113::/page/13/Text/35` (reasons: ['graph_depth_1'])

### Query 128
- Text: What is the rule about This section describes the effects or benefits of a rules  element. If the rule is an action, it explains what the effect  is or what you must roll. If it's a feat that modifies an  existing action or grants a constant effect, the benefit is  explained here.?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 014-029::/page/2/Text/16']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 406-423: `0.5569`
  - PZO22001 Starfinder Player Core 388-405: `0.5093`
  - PZO22001 Starfinder Player Core 210-231: `0.5061`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 014-029::/page/2/Text/16', 'merged::PZO22001 Starfinder Player Core 014-029::/page/2/Text/15', 'merged::PZO22001 Starfinder Player Core 014-029::/page/2/Text/17']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 014-029::/page/2/Text/15` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 014-029::/page/2/Text/17` (reasons: ['graph_depth_1'])

### Query 129
- Text: What is the rule about Choose two attribute boosts. One must be to Dexterity or  Charisma, and one is a free attribute boost.?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 092-097::/page/0/Text/8']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 014-029: `0.4858`
  - PZO22001 Starfinder Player Core 182-209: `0.4220`
  - PZO22001 Starfinder Player Core 174-181: `0.4013`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 092-097::/page/0/Text/8', 'merged::PZO22001 Starfinder Player Core 092-097::/page/0/Text/7', 'merged::PZO22001 Starfinder Player Core 092-097::/page/0/Text/9']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 092-097::/page/0/Text/7` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 092-097::/page/0/Text/9` (reasons: ['graph_depth_1'])

### Query 130
- Text: What is the rule about **SPELLS**?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 232-249::/page/1/Text/42']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 250-267: `0.2635`
  - PZO22001 Starfinder Player Core 330-363: `0.2590`
  - PZO22001 Starfinder Player Core 294-329: `0.2516`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 232-249::/page/1/Text/42', 'merged::PZO22001 Starfinder Player Core 232-249::/page/1/Text/43', 'merged::PZO22001 Starfinder Player Core 232-249::/page/1/Text/41']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 232-249::/page/1/Text/43` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 232-249::/page/1/Text/41` (reasons: ['graph_depth_1'])

### Query 131
- Text: Summarize **concealed** (condition) Low visibility makes you difficult to  target. 426, **435**
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 442-464::/page/2/Text/44']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 424-441: `0.5000`
  - PZO22001 Starfinder Player Core 250-267: `0.3479`
  - PZO22001 Starfinder Player Core 182-209: `0.3150`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 442-464::/page/2/Text/44', 'merged::PZO22001 Starfinder Player Core 442-464::/page/2/Text/45', 'merged::PZO22001 Starfinder Player Core 442-464::/page/2/Text/43']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 442-464::/page/2/Text/45` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 442-464::/page/2/Text/43` (reasons: ['graph_depth_1'])

### Query 132
- Text: Summarize **PLAYING THE ** **GAME**
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 330-363::/page/1/Text/72']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 388-405: `0.4598`
  - PZO22001 Starfinder Player Core 406-423: `0.4326`
  - PZO22001 Starfinder Player Core 001-013: `0.4018`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 330-363::/page/1/Text/72', 'merged::PZO22001 Starfinder Player Core 330-363::/page/1/Text/73', 'merged::PZO22001 Starfinder Player Core 330-363::/page/1/Text/71']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 330-363::/page/1/Text/73` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 330-363::/page/1/Text/71` (reasons: ['graph_depth_1'])

### Query 133
- Text: Summarize **CLASSES**
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 126-137::/page/1/Text/31']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 098-113: `0.3661`
  - PZO22001 Starfinder Player Core 182-209: `0.3335`
  - PZO22001 Starfinder Player Core 014-029: `0.3334`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 126-137::/page/1/Text/31', 'merged::PZO22001 Starfinder Player Core 126-137::/page/1/Text/32', 'merged::PZO22001 Starfinder Player Core 126-137::/page/3/Text/34', 'merged::PZO22001 Starfinder Player Core 126-137::/page/9/Text/63', 'merged::PZO22001 Starfinder Player Core 126-137::/page/7/Text/30', 'merged::PZO22001 Starfinder Player Core 126-137::/page/11/Text/30', 'merged::PZO22001 Starfinder Player Core 126-137::/page/5/Text/59', 'merged::PZO22001 Starfinder Player Core 126-137::/page/1/Text/30']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 126-137::/page/1/Text/32` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 126-137::/page/3/Text/34` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 126-137::/page/9/Text/63` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 126-137::/page/7/Text/30` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 126-137::/page/11/Text/30` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 126-137::/page/5/Text/59` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 126-137::/page/1/Text/30` (reasons: ['graph_depth_1'])

### Query 134
- Text: What is the rule about **BOUNTY HUNTER** **BACKGROUND**?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 092-097::/page/1/SectionHeader/3']
- Expected found: `True`
- Expected rank: `1`
- Routed chapters:
  - PZO22001 Starfinder Player Core 388-405: `0.3561`
  - PZO22001 Starfinder Player Core 092-097: `0.3450`
  - PZO22001 Starfinder Player Core 014-029: `0.3230`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 092-097::/page/1/SectionHeader/3', 'merged::PZO22001 Starfinder Player Core 092-097::/page/1/Text/4', 'merged::PZO22001 Starfinder Player Core 092-097::/page/1/Text/2']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 092-097::/page/1/Text/4` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 092-097::/page/1/Text/2` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 092-097::/page/1/SectionHeader/3` | 0.874695 | **BOUNTY HUNTER** **BACKGROUND** |
| 2 | `merged::PZO22001 Starfinder Player Core 092-097::/page/1/SectionHeader/7` | 0.456964 | **BRUTARIS PLAYER** **BACKGROUND** |
| 3 | `merged::PZO22001 Starfinder Player Core 092-097::/page/2/Text/1` | 0.454455 | **DISCIPLE** **BACKGROUND** |
| 4 | `merged::PZO22001 Starfinder Player Core 092-097::/page/3/Text/23` | 0.426410 | **RECLUSE** **BACKGROUND** |
| 5 | `merged::PZO22001 Starfinder Player Core 388-405::/page/11/Text/22` | 0.419357 | **GAME** **Rules Overview** |
| 6 | `merged::PZO22001 Starfinder Player Core 388-405::/page/15/Text/26` | 0.418461 | **Rules Overview** |
| 7 | `merged::PZO22001 Starfinder Player Core 388-405::/page/13/Text/33` | 0.418461 | **Rules Overview** |
| 8 | `merged::PZO22001 Starfinder Player Core 388-405::/page/9/Text/27` | 0.418461 | **Rules Overview** |
| 9 | `merged::PZO22001 Starfinder Player Core 388-405::/page/1/Text/29` | 0.418461 | **Rules Overview** |
| 10 | `merged::PZO22001 Starfinder Player Core 388-405::/page/3/Text/40` | 0.418461 | **Rules Overview** |

### Query 135
- Text: What is the rule about This convoluted web of synthweave straps is worn as a  fashion statement in some subcultures but has a useful  application in extreme environments. You gain a +1 item  bonus to Acrobatics checks, and you aren't off-guard or  clumsy while untethered in zero-g.?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 282-293::/page/1/Text/33']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 232-249: `0.4753`
  - PZO22001 Starfinder Player Core 182-209: `0.4208`
  - PZO22001 Starfinder Player Core 268-281: `0.4135`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 282-293::/page/1/Text/33', 'merged::PZO22001 Starfinder Player Core 282-293::/page/1/Text/32', 'merged::PZO22001 Starfinder Player Core 282-293::/page/1/Text/34']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 282-293::/page/1/Text/32` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 282-293::/page/1/Text/34` (reasons: ['graph_depth_1'])

### Query 136
- Text: Summarize **CONDITIONS ** **APPENDIX**
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 182-209::/page/1/Text/30']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 424-441: `0.3294`
  - PZO22001 Starfinder Player Core 014-029: `0.3252`
  - PZO22001 Starfinder Player Core 250-267: `0.3094`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 182-209::/page/1/Text/30', 'merged::PZO22001 Starfinder Player Core 182-209::/page/15/Text/36', 'merged::PZO22001 Starfinder Player Core 182-209::/page/19/Text/70', 'merged::PZO22001 Starfinder Player Core 182-209::/page/25/Text/36', 'merged::PZO22001 Starfinder Player Core 182-209::/page/13/Text/52', 'merged::PZO22001 Starfinder Player Core 182-209::/page/17/Text/51', 'merged::PZO22001 Starfinder Player Core 182-209::/page/9/Text/46', 'merged::PZO22001 Starfinder Player Core 182-209::/page/27/Text/46', 'merged::PZO22001 Starfinder Player Core 182-209::/page/5/Text/31', 'merged::PZO22001 Starfinder Player Core 182-209::/page/1/Text/29', 'merged::PZO22001 Starfinder Player Core 182-209::/page/7/Text/38', 'merged::PZO22001 Starfinder Player Core 182-209::/page/1/Text/31']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 182-209::/page/15/Text/36` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 182-209::/page/19/Text/70` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 182-209::/page/25/Text/36` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 182-209::/page/13/Text/52` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 182-209::/page/17/Text/51` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 182-209::/page/9/Text/46` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 182-209::/page/27/Text/46` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 182-209::/page/5/Text/31` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 182-209::/page/1/Text/29` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 182-209::/page/7/Text/38` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 182-209::/page/1/Text/31` (reasons: ['graph_depth_1'])

### Query 137
- Text: What is the rule about **ATTACKS**?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/58']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 406-423: `0.3644`
  - PZO22001 Starfinder Player Core 250-267: `0.3581`
  - PZO22001 Starfinder Player Core 388-405: `0.3436`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/58', 'merged::PZO22001 Starfinder Player Core 150-161::/page/1/Text/57', 'merged::PZO22001 Starfinder Player Core 150-161::/page/1/Text/59']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 150-161::/page/1/Text/57` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 150-161::/page/1/Text/59` (reasons: ['graph_depth_1'])

### Query 138
- Text: What is the rule about The tables on pages 286–287 list level, price, Bulk,  and hands entries for a wide variety of magic and hybrid  items. Each item has its own rules for how it functions:  some require bespoke activations, while others function  automatically, such as by granting constant item bonuses  or other benefits when worn or held.?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 282-293::/page/0/Text/5']
- Expected found: `True`
- Expected rank: `1`
- Routed chapters:
  - PZO22001 Starfinder Player Core 282-293: `0.5202`
  - PZO22001 Starfinder Player Core 232-249: `0.5097`
  - PZO22001 Starfinder Character Sheet: `0.4930`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 282-293::/page/0/Text/5', 'merged::PZO22001 Starfinder Player Core 282-293::/page/0/Text/4', 'merged::PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/6']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 282-293::/page/0/Text/4` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/6` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 282-293::/page/0/Text/5` | 0.939073 | The tables on pages 286–287 list level, price, Bulk,  and hands entries for a wide variety of magic and hybrid  items. Each item has its own rules for how it functions:  some require bespoke activatio |
| 2 | `merged::PZO22001 Starfinder Player Core 232-249::/page/6/Text/5` | 0.645793 | The tables starting on page 240 list the Price and Bulk entries  for a wide variety of gear you can use to kit out your character.  Any item with a number after it in parentheses indicates that  the i |
| 3 | `merged::PZO22001 Starfinder Player Core 282-293::/page/0/Text/12` | 0.581588 | While some items function automatically and grant constant  benefits, others produce effects only when properly used. An  activation lists the number of actions it takes and any traits  of the activat |
| 4 | `merged::PZO22001 Starfinder Player Core 232-249::/page/2/Text/7` | 0.579101 | Each item has an item level, which represents the item's  complexity and any magic or technology used in its  construction. Simpler items with a lower level are easier to  construct, and you can't Cra |
| 5 | `merged::PZO22001 Starfinder Player Core 232-249::/page/3/Text/19` | 0.548619 | Higher-level magic and tech items that cost significantly more than 8 times the cost of a mundane item use their listed Price regardless of size. Precious materials, however, have a Price based on the |
| 6 | `merged::PZO22001 Starfinder Player Core 282-293::/page/0/Text/7` | 0.530881 | Certain magic and hybrid items convey their benefits only  when worn and invested using the Invest an Item activity,  connecting them to a specific PC. A PC can benefit from  no more than 10 invested |
| 7 | `merged::PZO22001 Starfinder Player Core 282-293::/page/2/Text/6` | 0.521421 | **Tech:** Items with the tech trait can be crafted by  anyone, but if they're level 1 or higher, they require  the Tech Crafting feat (page 229) to craft. If a tech  item also has the magical trait, t |
| 8 | `merged::PZO22001 Starfinder Player Core 282-293::/page/0/Text/4` | 0.501466 | Technology and magic are everywhere in the galaxy.  While some magic equipment have gone unchanged for  thousands of years, the integration of technology to  improve the functionality or cost of many |
| 9 | `merged::PZO22001 Starfinder Player Core 232-249::/page/1/Text/21` | 0.498809 | Most items in the following tables have a Price, which is the  amount of currency it typically takes to purchase that item. |
| 10 | `merged::PZO22001 Starfinder Player Core 232-249::/page/2/Text/11` | 0.490521 | Equipment on page 235 lists some ways that you might  change the items you're holding or carrying, and the number  of hands you need to do so. |

### Query 139
- Text: What is the rule about FEATS THAT GRANT FEATS?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 174-181::/page/0/SectionHeader/12']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 210-231: `0.4303`
  - PZO22001 Starfinder Player Core 406-423: `0.2676`
  - PZO22001 Starfinder Player Core 232-249: `0.2658`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 174-181::/page/0/SectionHeader/12', 'merged::PZO22001 Starfinder Player Core 174-181::/page/0/Text/13', 'merged::PZO22001 Starfinder Player Core 174-181::/page/0/Text/11']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 174-181::/page/0/Text/13` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 174-181::/page/0/Text/11` (reasons: ['graph_depth_1'])

### Query 140
- Text: Summarize **Sample Names:** Lashunta naming conventions often use  tonal elements. Some sample lashunta names are Domash,  Hesori, Imaaz, Kima, Kopalo, Maenala, Nomae, Oraeus, Raia,  Shess, Soryn, Stretto, Taeon, and Varikuara.
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 058-073::/page/1/Text/17']
- Expected found: `True`
- Expected rank: `1`
- Routed chapters:
  - PZO22001 Starfinder Player Core 058-073: `0.5036`
  - PZO22001 Starfinder Player Core 330-363: `0.3766`
  - PZO22001 Starfinder Player Core 040-057: `0.3705`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 058-073::/page/1/Text/17', 'merged::PZO22001 Starfinder Player Core 058-073::/page/1/SectionHeader/18', 'merged::PZO22001 Starfinder Player Core 058-073::/page/1/Text/16']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 058-073::/page/1/SectionHeader/18` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 058-073::/page/1/Text/16` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 058-073::/page/1/Text/17` | 0.995305 | **Sample Names:** Lashunta naming conventions often use  tonal elements. Some sample lashunta names are Domash,  Hesori, Imaaz, Kima, Kopalo, Maenala, Nomae, Oraeus, Raia,  Shess, Soryn, Stretto, Taeo |
| 2 | `merged::PZO22001 Starfinder Player Core 040-057::/page/11/Text/16` | 0.675780 | **Sample Names:** Akif, Alezandaru, Amare, Baolo, Belor,  Darilian, Hadzi, Hai Minh, Hiriko, Iolana, Jokug, Korva, Morvius,  Navasi, Pao, Pasara, Raziya, Revhi, Sahba, Seoni, Sephia, Signe,  Valeros, |
| 3 | `merged::PZO22001 Starfinder Player Core 058-073::/page/5/Text/18` | 0.638808 | **Sample Names:** Traditional pahtra names contain  auspicious elements determined by a mystic. Pahtra names  include Cahnex, Dae, Fetenekku, Hafoumei, Ifset, Ihrasara,  Jeviish, Khieper, Lealorn, Mah |
| 4 | `merged::PZO22001 Starfinder Player Core 040-057::/page/15/Text/17` | 0.627682 | **Sample Names:** Altronus, Barasul, Ehu, Esar, Gorsen, Hadif,  Jahir, Kala, Khsutil, Maeda, Metweska, Ninura, Remu, Senesel,  Tolar, Umana, Voloteo, Zye |
| 5 | `merged::PZO22001 Starfinder Player Core 040-057::/page/7/Text/15` | 0.611159 | **Sample Names:** Barathu names change when they merge  and split back into their component parts. Many early stage  barathus choose their own names, selecting words for concepts  that resonate with t |
| 6 | `merged::PZO22001 Starfinder Player Core 058-073::/page/13/Text/18` | 0.608926 | **Sample Names:** Ayoka, Baazo, Bixby, Dakoyo, Fipzul, Gazigaz,  Jomp, Kayoko, Kimikim, Mimzy, Nako, Prismacora, Quonx,  Rudfuz, Sprax, Timinim, Tipps, Tonkona, Viverivim |
| 7 | `merged::PZO22001 Starfinder Player Core 040-057::/page/3/Text/15` | 0.596044 | **Sample Names:** Asha, Blue-17, Celita, Daniv, Emene-3, Era-4, Flick, Garro, Historia-6, Hope-1, Iseph, Melody, Naga, Olas,  Omen, Prime, Ruby-17, Stringer, Twenty Six, Urdun, Verity-3,  Yose |
| 8 | `merged::PZO22001 Starfinder Player Core 040-057::/page/15/Text/16` | 0.549469 | While most kasathas go by their first name, many have a  full name consisting of up to half a dozen elements referring  to one's ancestors, clan, and connection to the Great Families  of Kasath. For e |
| 9 | `merged::PZO22001 Starfinder Player Core 058-073::/page/9/Text/16` | 0.544803 | **Sample Names:** Shirrens rely primarily on telepathy for  communication and have a secret "soul-name" that's purely  thought-based. Shirrens readily accept nicknames bestowed  by their companions. S |
| 10 | `merged::PZO22001 Starfinder Player Core 058-073::/page/5/Text/34` | 0.509186 | **Kasatha** **Lashunta** |

### Query 141
- Text: What are the requirements for **INFLUENCE **[reaction] **FEAT 4**?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/29']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 210-231: `0.3550`
  - PZO22001 Starfinder Player Core 406-423: `0.3454`
  - PZO22001 Starfinder Player Core 014-029: `0.3201`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/29', 'merged::PZO22001 Starfinder Player Core 098-113::/page/12/Text/28', 'merged::PZO22001 Starfinder Player Core 098-113::/page/12/Text/31']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 098-113::/page/12/Text/28` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 098-113::/page/12/Text/31` (reasons: ['graph_depth_1'])

### Query 142
- Text: What is the rule about This section specifies the levels at which your character  gains class feats—special feats that only members of that  class can access. Class feats are granted beginning at 1st or  2nd level, depending on the class. Specific class feats are  detailed at the end of each class entry.?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 098-113::/page/2/Text/15']
- Expected found: `True`
- Expected rank: `1`
- Routed chapters:
  - PZO22001 Starfinder Player Core 210-231: `0.6516`
  - PZO22001 Starfinder Player Core 098-113: `0.5402`
  - PZO22001 Starfinder Player Core 182-209: `0.4983`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 098-113::/page/2/Text/15', 'merged::PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/16', 'merged::PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/14']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/16` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/14` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 098-113::/page/2/Text/15` | 0.911669 | This section specifies the levels at which your character  gains class feats—special feats that only members of that  class can access. Class feats are granted beginning at 1st or  2nd level, dependin |
| 2 | `merged::PZO22001 Starfinder Player Core 098-113::/page/2/Text/19` | 0.767545 | This section specifies the levels at which your character  gains general feats. Most classes grant a general feat at 3rd  level and every 4 levels thereafter. At each of these levels,  you can select |
| 3 | `merged::PZO22001 Starfinder Player Core 098-113::/page/2/Text/17` | 0.714367 | This section specifies the levels at which your character gains  feats with the skill trait, called skill feats. Skill feats can be  found in Chapter 5, beginning on page 210. At 2nd level and  every |
| 4 | `merged::PZO22001 Starfinder Player Core 210-231::/page/1/Text/5` | 0.703077 | General feats also include a subcategory of skill feats,  which expand on what you can accomplish via skills.  These feats also have the skill trait. Most characters gain  skill feats at 2nd level and |
| 5 | `merged::PZO22001 Starfinder Player Core 182-209::/page/2/Text/14` | 0.669971 | As your character advances in level, there are two  main ways their skills improve: skill increases and skill  feats. Your class lists the levels at which you gain each  of these improvements. |
| 6 | `merged::PZO22001 Starfinder Player Core 098-113::/page/2/Text/10` | 0.656635 | This table summarizes the feats, skill increases, attribute  boosts, and other benefits your character gains as they  advance in level. The first column of the class table  indicates a level, and the |
| 7 | `merged::PZO22001 Starfinder Player Core 098-113::/page/2/Text/26` | 0.651420 | This section serves as a reminder of the ancestry feats your  character gains at 5th, 9th, 13th, and 17th levels. Ancestry  feats are detailed in each ancestry entry in Chapter 2, which  begins on pag |
| 8 | `merged::PZO22001 Starfinder Player Core 098-113::/page/8/Text/10` | 0.641676 | At 3rd level and every 4 levels thereafter, you gain a general  feat. General feats are listed in Chapter 5. |
| 9 | `merged::PZO22001 Starfinder Player Core 098-113::/page/2/Text/12` | 0.635714 | This section presents all the abilities the class grants  your character. An ability gained at a higher level lists the |
| 10 | `merged::PZO22001 Starfinder Player Core 210-231::/page/1/Text/6` | 0.631262 | you gain a skill feat, you must select a general feat with  the skill trait; you can't select a general feat that lacks the  skill trait. The level of a skill feat is typically the minimum  level at w |

### Query 143
- Text: What does **SUMMON PLANT OR FUNGUS **[three-actions] **SPELL 1** do?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/11']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 406-423: `0.3740`
  - PZO22001 Starfinder Player Core 294-329: `0.3406`
  - PZO22001 Starfinder Player Core 330-363: `0.3349`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/11', 'merged::PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/4', 'merged::PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/18']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/4` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/18` (reasons: ['graph_depth_1'])

### Query 144
- Text: What is the rule about is necessary, they can require audio or biometric imprints  in order to activate. Some advanced credsticks even have a  magical component that might require a mental password or  the recitation of a specific spell to access stored funds.?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 232-249::/page/1/Text/15']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 182-209: `0.4026`
  - PZO22001 Starfinder Player Core 364-387: `0.3981`
  - PZO22001 Starfinder Player Core 282-293: `0.3966`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 232-249::/page/1/Text/15', 'merged::PZO22001 Starfinder Player Core 232-249::/page/1/Text/16', 'merged::PZO22001 Starfinder Player Core 232-249::/page/1/Text/14']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 232-249::/page/1/Text/16` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 232-249::/page/1/Text/14` (reasons: ['graph_depth_1'])

### Query 145
- Text: What is the rule about **SKILLS**?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 210-231::/page/1/Text/16']
- Expected found: `True`
- Expected rank: `19`
- Routed chapters:
  - PZO22001 Starfinder Player Core 182-209: `0.5422`
  - PZO22001 Starfinder Player Core 210-231: `0.4266`
  - PZO22001 Starfinder Player Core 442-464: `0.3689`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 210-231::/page/1/Text/16', 'merged::PZO22001 Starfinder Player Core 210-231::/page/1/Text/17', 'merged::PZO22001 Starfinder Player Core 210-231::/page/1/Text/15']
- Expanded expected found: `True`
- Expanded expected rank: `19`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 210-231::/page/1/Text/17` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 210-231::/page/1/Text/15` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 442-464::/page/9/Text/48` | 0.814442 | **SKILLS** |
| 2 | `merged::PZO22001 Starfinder Player Core 442-464::/page/13/Text/56` | 0.814442 | **SKILLS** |
| 3 | `merged::PZO22001 Starfinder Player Core 182-209::/page/27/Text/39` | 0.814442 | **SKILLS** |
| 4 | `merged::PZO22001 Starfinder Player Core 210-231::/page/3/Text/6` | 0.814442 | **SKILLS** |
| 5 | `merged::PZO22001 Starfinder Player Core 210-231::/page/19/Text/70` | 0.814442 | **SKILLS** |
| 6 | `merged::PZO22001 Starfinder Player Core 182-209::/page/5/Text/23` | 0.814442 | **SKILLS** |
| 7 | `merged::PZO22001 Starfinder Player Core 182-209::/page/25/Text/29` | 0.814442 | **SKILLS** |
| 8 | `merged::PZO22001 Starfinder Player Core 210-231::/page/13/Text/62` | 0.814442 | **SKILLS** |
| 9 | `merged::PZO22001 Starfinder Player Core 182-209::/page/11/SectionHeader/37` | 0.814442 | **SKILLS** |
| 10 | `merged::PZO22001 Starfinder Player Core 182-209::/page/1/Text/22` | 0.814442 | **SKILLS** |

### Query 146
- Text: What are the requirements for **DON'T YOU DIE ON ME **[one-action] **FEAT 2**?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/13']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 406-423: `0.3148`
  - PZO22001 Starfinder Player Core 014-029: `0.3068`
  - PZO22001 Starfinder Player Core 210-231: `0.2974`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/13', 'merged::PZO22001 Starfinder Player Core 098-113::/page/11/Text/14', 'merged::PZO22001 Starfinder Player Core 098-113::/page/11/Text/12']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 098-113::/page/11/Text/14` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 098-113::/page/11/Text/12` (reasons: ['graph_depth_1'])

### Query 147
- Text: What is the rule about If the globe overlaps with an area of magical darkness,  *sunburst* attempts to counteract the darkness effect.?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 364-387::/page/1/Text/44']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 294-329: `0.3633`
  - PZO22001 Starfinder Player Core 138-149: `0.3621`
  - PZO22001 Starfinder Player Core 030-039: `0.3331`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 364-387::/page/1/Text/44', 'merged::PZO22001 Starfinder Player Core 364-387::/page/1/Text/43', 'merged::PZO22001 Starfinder Player Core 364-387::/page/1/Text/45']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 364-387::/page/1/Text/43` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 364-387::/page/1/Text/45` (reasons: ['graph_depth_1'])

### Query 148
- Text: What is the rule about Armor, shields and weapons gain more upgrade slots as they improve. Higher grades of armor add more AC and gains the resilient trait, improving the saving throws of their wielder by the listed value. Higher grades of weapons have improved damage dice and gain the tracking trait, improving their attack rolls by the listed value. Higher grades of shields have increased Hardness, Hit Points, and BT.?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 232-249::/page/4/Text/10']
- Expected found: `True`
- Expected rank: `1`
- Routed chapters:
  - PZO22001 Starfinder Player Core 250-267: `0.6487`
  - PZO22001 Starfinder Player Core 268-281: `0.6101`
  - PZO22001 Starfinder Player Core 232-249: `0.5554`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 232-249::/page/4/Text/10', 'merged::PZO22001 Starfinder Player Core 232-249::/page/4/Text/9', 'merged::PZO22001 Starfinder Player Core 232-249::/page/4/SectionHeader/11']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 232-249::/page/4/Text/9` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 232-249::/page/4/SectionHeader/11` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 232-249::/page/4/Text/10` | 0.916961 | Armor, shields and weapons gain more upgrade slots as they improve. Higher grades of armor add more AC and gains the resilient trait, improving the saving throws of their wielder by the listed value. |
| 2 | `merged::PZO22001 Starfinder Player Core 250-267::/page/0/Text/2` | 0.605896 | A shield can increase your character's defense beyond the protection their armor provides. Your  character must be wielding a shield in one hand to make use of it, and it grants its bonus to AC only |
| 3 | `merged::PZO22001 Starfinder Player Core 232-249::/page/4/Text/6` | 0.591856 | Most types of armor, shields, and weapons in Starfinder come in a variety of grades. Each grade represents an improved version of that piece of equipment and should be sought after once your character |
| 4 | `merged::PZO22001 Starfinder Player Core 250-267::/page/0/Text/23` | 0.586013 | **Installed:** Some shields aren't held but are installed  as armor or weapon upgrades. You can Raise a Shield  installed as an armor upgrade as normal. Shields can be  installed only into weapons wit |
| 5 | `merged::PZO22001 Starfinder Player Core 232-249::/page/4/Text/9` | 0.573180 | Armor, shields, and weapons (pages 244, 250, and 253 respectively) are typically listed using their lowest available grade, usually commercial. Each grade beyond the first provides the equipment with |
| 6 | `merged::PZO22001 Starfinder Player Core 268-281::/page/0/Text/9` | 0.570898 | Most upgrades grant their benefits continually so long as  you're properly wearing the armor they're installed in. Others  produce their effects only when used properly in the moment  by spending acti |
| 7 | `merged::PZO22001 Starfinder Player Core 250-267::/page/0/Text/8` | 0.566300 | Shields have statistics that follow the same rules as armor:  Price, Speed Penalty, and Bulk. See page 245 for the rules  for those statistics. Their other statistics are described here. |
| 8 | `merged::PZO22001 Starfinder Player Core 232-249::/page/4/Text/8` | 0.564998 | Equipment typically comes in seven grades: commercial, tactical, advanced, superior, elite, ultimate, and paragon. While most armor, shields, and weapons can exist in any grade from commercial to para |
| 9 | `merged::PZO22001 Starfinder Player Core 250-267::/page/1/Text/8` | 0.557287 | bonus to your AC, the shield upgrade emits an inertial  dampening barrier, and you automatically Raise a Shield.  You can't Raise a Shield installed as a weapon upgrade any  other way. If you use the |
| 10 | `merged::PZO22001 Starfinder Player Core 250-267::/page/3/Text/15` | 0.555281 | Ranged weapons don't normally add an attribute modifier  to the damage roll, though thrown weapons add your full  Strength modifier. At higher levels, most characters also gain  extra damage from weap |

### Query 149
- Text: Summarize **Solarian**
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 162-173::/page/1/Text/39']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 138-149: `0.5425`
  - PZO22001 Starfinder Player Core 030-039: `0.2832`
  - PZO22001 Starfinder Player Core 150-161: `0.2812`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 162-173::/page/1/Text/39', 'merged::PZO22001 Starfinder Player Core 162-173::/page/1/Text/38', 'merged::PZO22001 Starfinder Player Core 162-173::/page/1/Text/40']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 162-173::/page/1/Text/38` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 162-173::/page/1/Text/40` (reasons: ['graph_depth_1'])

### Query 150
- Text: What is the rule about 3 Retrieving an item stowed in your own backpack requires first taking off the backpack with a separate Interact action.?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 232-249::/page/4/ListItem/4']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 406-423: `0.3964`
  - PZO22001 Starfinder Player Core 424-441: `0.3537`
  - PZO22001 Starfinder Player Core 388-405: `0.3471`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 232-249::/page/4/ListItem/4', 'merged::PZO22001 Starfinder Player Core 232-249::/page/4/ListItem/3', 'merged::PZO22001 Starfinder Player Core 232-249::/page/4/SectionHeader/5']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 232-249::/page/4/ListItem/3` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 232-249::/page/4/SectionHeader/5` (reasons: ['graph_depth_1'])

### Query 151
- Text: What is the rule about Fearsome bulwark, general feat, reflex?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/394']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 210-231: `0.3583`
  - PZO22001 Starfinder Player Core 364-387: `0.3389`
  - PZO22001 Starfinder Player Core 250-267: `0.3296`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/394', 'merged::PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/395', 'merged::PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/393']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/395` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/393` (reasons: ['graph_depth_1'])

### Query 152
- Text: What is the rule about Skill feat, solarian feat?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/397']
- Expected found: `True`
- Expected rank: `5`
- Routed chapters:
  - PZO22001 Starfinder Player Core 138-149: `0.5553`
  - PZO22001 Starfinder Player Core 210-231: `0.5412`
  - PZO22001 Starfinder Player Core 182-209: `0.4474`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/397', 'merged::PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/396', 'merged::PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/398']
- Expanded expected found: `True`
- Expanded expected rank: `5`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/396` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/398` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/425` | 0.881260 | Skill feat, solarian feat |
| 2 | `merged::PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/413` | 0.881260 | Skill feat, solarian feat |
| 3 | `merged::PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/421` | 0.881260 | Skill feat, solarian feat |
| 4 | `merged::PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/401` | 0.881260 | Skill feat, solarian feat |
| 5 | `merged::PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/397` | 0.881260 | Skill feat, solarian feat |
| 6 | `merged::PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/417` | 0.881260 | Skill feat, solarian feat |
| 7 | `merged::PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/405` | 0.881260 | Skill feat, solarian feat |
| 8 | `merged::PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/393` | 0.881260 | Skill feat, solarian feat |
| 9 | `merged::PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/429` | 0.767088 | Attribute boosts, skill feat, solarian feat |
| 10 | `merged::PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/409` | 0.767088 | Attribute boosts, skill feat, solarian feat |

### Query 153
- Text: What is the rule about **CYBERBORN** **BACKGROUND**?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 092-097::/page/1/SectionHeader/31']
- Expected found: `True`
- Expected rank: `1`
- Routed chapters:
  - PZO22001 Starfinder Player Core 092-097: `0.3805`
  - PZO22001 Starfinder Player Core 040-057: `0.3029`
  - PZO22001 Starfinder Player Core 388-405: `0.3026`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 092-097::/page/1/SectionHeader/31', 'merged::PZO22001 Starfinder Player Core 092-097::/page/1/Text/30', 'merged::PZO22001 Starfinder Player Core 092-097::/page/1/SectionHeader/32']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 092-097::/page/1/Text/30` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 092-097::/page/1/SectionHeader/32` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 092-097::/page/1/SectionHeader/31` | 0.871656 | **CYBERBORN** **BACKGROUND** |
| 2 | `merged::PZO22001 Starfinder Player Core 092-097::/page/2/Text/1` | 0.461128 | **DISCIPLE** **BACKGROUND** |
| 3 | `merged::PZO22001 Starfinder Player Core 388-405::/page/13/Text/33` | 0.455622 | **Rules Overview** |
| 4 | `merged::PZO22001 Starfinder Player Core 388-405::/page/3/Text/40` | 0.455622 | **Rules Overview** |
| 5 | `merged::PZO22001 Starfinder Player Core 388-405::/page/7/Text/21` | 0.455622 | **Rules Overview** |
| 6 | `merged::PZO22001 Starfinder Player Core 388-405::/page/5/Text/24` | 0.455622 | **Rules Overview** |
| 7 | `merged::PZO22001 Starfinder Player Core 388-405::/page/15/Text/26` | 0.455622 | **Rules Overview** |
| 8 | `merged::PZO22001 Starfinder Player Core 388-405::/page/1/Text/29` | 0.455622 | **Rules Overview** |
| 9 | `merged::PZO22001 Starfinder Player Core 388-405::/page/9/Text/27` | 0.455622 | **Rules Overview** |
| 10 | `merged::PZO22001 Starfinder Player Core 092-097::/page/4/SectionHeader/24` | 0.424780 | **TECH SUPPORT** **BACKGROUND** |

### Query 154
- Text: What is the rule about **TRAITS **?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 058-073::/page/0/SectionHeader/10']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 250-267: `0.3988`
  - PZO22001 Starfinder Player Core 040-057: `0.3942`
  - PZO22001 Starfinder Player Core 182-209: `0.3725`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 058-073::/page/0/SectionHeader/10', 'merged::PZO22001 Starfinder Player Core 058-073::/page/0/Text/11', 'merged::PZO22001 Starfinder Player Core 058-073::/page/12/SectionHeader/10', 'merged::PZO22001 Starfinder Player Core 058-073::/page/4/SectionHeader/12', 'merged::PZO22001 Starfinder Player Core 058-073::/page/0/Text/9', 'merged::PZO22001 Starfinder Player Core 058-073::/page/8/SectionHeader/12']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 058-073::/page/0/Text/11` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 058-073::/page/12/SectionHeader/10` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 058-073::/page/4/SectionHeader/12` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 058-073::/page/0/Text/9` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 058-073::/page/8/SectionHeader/12` (reasons: ['graph_depth_1'])

### Query 155
- Text: Summarize Maneuver in Flight ❖
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/98']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 388-405: `0.3365`
  - PZO22001 Starfinder Player Core 406-423: `0.3343`
  - PZO22001 Starfinder Player Core 424-441: `0.3060`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/98', 'merged::PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/97', 'merged::PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/99']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/97` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/99` (reasons: ['graph_depth_1'])

### Query 156
- Text: What is the rule about A character's acumen in skills can come from all sorts of  training, from piloting starships to researching a topic on  an infosphere to rehearsing a performing art. When you  create your character and as they advance in level, you  have flexibility as to which skills they become better at  and when. Some classes benefit more from improving  certain skills—such as the envoy's focus on their leadership  skill—but for most classes, you can choose whichever  skills make the most sense for your character's theme  and backstory at 1st level, then use their adventure and  downtime experiences to inform how their skills should  improve as your character levels up.?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 182-209::/page/1/Text/6']
- Expected found: `True`
- Expected rank: `1`
- Routed chapters:
  - PZO22001 Starfinder Player Core 092-097: `0.6403`
  - PZO22001 Starfinder Player Core 182-209: `0.6287`
  - PZO22001 Starfinder Player Core 098-113: `0.6250`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 182-209::/page/1/Text/6', 'merged::PZO22001 Starfinder Player Core 182-209::/page/1/Text/7', 'merged::PZO22001 Starfinder Player Core 182-209::/page/1/Text/2']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 182-209::/page/1/Text/7` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 182-209::/page/1/Text/2` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 182-209::/page/1/Text/6` | 0.959137 | A character's acumen in skills can come from all sorts of  training, from piloting starships to researching a topic on  an infosphere to rehearsing a performing art. When you  create your character an |
| 2 | `merged::PZO22001 Starfinder Player Core 098-113::/page/2/Text/21` | 0.700909 | This section specifies the levels at which your character  can increase their proficiency rank in a skill. At 3rd level  and every 2 levels thereafter, most classes grant a skill  increase, though env |
| 3 | `merged::PZO22001 Starfinder Player Core 182-209::/page/1/Text/7` | 0.696968 | A character gains training in certain skills at 1st level:  typically two from their background, a small number of  predetermined skills from their class, and several skills of  your choice granted by |
| 4 | `merged::PZO22001 Starfinder Player Core 182-209::/page/2/Text/14` | 0.675676 | As your character advances in level, there are two  main ways their skills improve: skill increases and skill  feats. Your class lists the levels at which you gain each  of these improvements. |
| 5 | `merged::PZO22001 Starfinder Player Core 182-209::/page/1/Text/2` | 0.665763 | While your character's attributes represent their raw talent and potential, skills represent their  training and experience at performing certain tasks. Each skill is keyed to one of your character's |
| 6 | `merged::PZO22001 Starfinder Player Core 098-113::/page/2/Text/4` | 0.646037 | When you choose your character's class, they gain a set of  initial proficiencies. Proficiencies measure your character's  ability to perform tasks, use abilities, and succeed at  checks. Proficiency |
| 7 | `merged::PZO22001 Starfinder Player Core 098-113::/page/1/Text/2` | 0.644667 | Just as your character's ancestry plays a key role in expressing their identity and worldview, their  class indicates the training they have and will improve upon as an adventurer. Choosing your  char |
| 8 | `merged::PZO22001 Starfinder Player Core 098-113::/page/2/Text/17` | 0.636433 | This section specifies the levels at which your character gains  feats with the skill trait, called skill feats. Skill feats can be  found in Chapter 5, beginning on page 210. At 2nd level and  every |
| 9 | `merged::PZO22001 Starfinder Player Core 098-113::/page/8/Text/3` | 0.631379 | You gain more skill increases than members of other classes.  At 2nd level and every level thereafter, you gain a skill  increase. You can use this increase to either become trained  in one skill you' |
| 10 | `merged::PZO22001 Starfinder Player Core 182-209::/page/2/Text/16` | 0.630425 | Skill increases improve your proficiency in skills of your  choice. You can use these increases to become trained  in new skills or increase your proficiency rank in skills  you're trained in (from tr |

### Query 157
- Text: What is the rule about Example Characters?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/9']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 442-464: `0.3689`
  - PZO22001 Starfinder Player Core 014-029: `0.3653`
  - PZO22001 Starfinder Character Sheet: `0.3589`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/9', 'merged::PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/10', 'merged::PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/31', 'merged::PZO22001 Starfinder Player Core 030-039::/page/4/SectionHeader/11', 'merged::PZO22001 Starfinder Player Core 030-039::/page/1/SectionHeader/7', 'merged::PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/24', 'merged::PZO22001 Starfinder Player Core 030-039::/page/3/SectionHeader/4', 'merged::PZO22001 Starfinder Player Core 030-039::/page/2/Text/8', 'merged::PZO22001 Starfinder Player Core 030-039::/page/3/SectionHeader/22', 'merged::PZO22001 Starfinder Player Core 030-039::/page/3/SectionHeader/13', 'merged::PZO22001 Starfinder Player Core 030-039::/page/4/SectionHeader/3', 'merged::PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/1']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/10` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/31` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 030-039::/page/4/SectionHeader/11` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 030-039::/page/1/SectionHeader/7` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/24` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 030-039::/page/3/SectionHeader/4` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 030-039::/page/2/Text/8` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 030-039::/page/3/SectionHeader/22` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 030-039::/page/3/SectionHeader/13` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 030-039::/page/4/SectionHeader/3` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/1` (reasons: ['graph_depth_1'])

### Query 158
- Text: What does **TELEPORT** **SPELL 6** do?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 364-387::/page/3/SectionHeader/30']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 268-281: `0.2592`
  - PZO22001 Starfinder Player Core 294-329: `0.2501`
  - PZO22001 Starfinder Player Core 162-173: `0.2439`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 364-387::/page/3/SectionHeader/30', 'merged::PZO22001 Starfinder Player Core 364-387::/page/3/Text/29', 'merged::PZO22001 Starfinder Player Core 364-387::/page/3/SectionHeader/41']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 364-387::/page/3/Text/29` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 364-387::/page/3/SectionHeader/41` (reasons: ['graph_depth_1'])

### Query 159
- Text: What is the rule about In Starfinder, the players take on the role of **player characters ** **(PCs)**, while the Game Master portrays **nonplayer characters ** **(NPCs)** and **monsters**. While PCs and NPCs are both important  to the story, they serve very different purposes in the game.  PCs are the protagonists—the narrative is about them—while  NPCs are allies, contacts, adversaries, and villains. That said,  PCs, NPCs, and monsters share several characteristics.?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 001-013::/page/5/Text/21']
- Expected found: `True`
- Expected rank: `1`
- Routed chapters:
  - PZO22001 Starfinder Player Core 001-013: `0.6246`
  - PZO22001 Starfinder Player Core 442-464: `0.5473`
  - PZO22001 Starfinder Player Core 294-329: `0.5078`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 001-013::/page/5/Text/21', 'merged::PZO22001 Starfinder Player Core 001-013::/page/5/Text/22', 'merged::PZO22001 Starfinder Player Core 001-013::/page/5/SectionHeader/20']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 001-013::/page/5/Text/22` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 001-013::/page/5/SectionHeader/20` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 001-013::/page/5/Text/21` | 0.971805 | In Starfinder, the players take on the role of **player characters ** **(PCs)**, while the Game Master portrays **nonplayer characters ** **(NPCs)** and **monsters**. While PCs and NPCs are both impor |
| 2 | `merged::PZO22001 Starfinder Player Core 001-013::/page/4/Text/17` | 0.705925 | Everyone involved in a Starfinder game is a player, including  the Game Master, but for the sake of simplicity, "player"  usually refers to participants other than the GM. Before  the game begins, pla |
| 3 | `merged::PZO22001 Starfinder Player Core 001-013::/page/4/Text/8` | 0.676776 | A roleplaying game is an interactive story where one  player, the Game Master (GM), sets the scene and presents  challenges, while other players take the roles of player  characters (PCs) and attempt |
| 4 | `merged::PZO22001 Starfinder Player Core 001-013::/page/5/Text/4` | 0.671810 | While the other players create and control their characters,  the Game Master (or GM) is in charge of the story and setting.  The GM describes all the situations the player characters  experience in a |
| 5 | `merged::PZO22001 Starfinder Player Core 442-464::/page/5/Text/52` | 0.654238 | **Game Master (GM)** The player who adjudicates the rules and  narrates the elements of the Starfinder story and world  that the other players explore. **5**, 10 |
| 6 | `merged::PZO22001 Starfinder Player Core 001-013::/page/9/Text/28` | 0.650966 | The Game Master is the player who adjudicates the rules  and narrates the various elements of the Starfinder story  and world that the other players explore. The GM uses the  rules found in *Starfinde |
| 7 | `merged::PZO22001 Starfinder Player Core 001-013::/page/10/SectionHeader/3` | 0.617853 | **Nonplayer Character (NPC)** |
| 8 | `merged::PZO22001 Starfinder Player Core 442-464::/page/8/Text/19` | 0.601432 | **monster** A monster is a creature that is typically inhuman and  serves to thwart the PCs in some way. Beneficial monsters  are exceptions in most games. The GM plays the role of any  monster the PC |
| 9 | `merged::PZO22001 Starfinder Player Core 001-013::/page/6/Text/3` | 0.600054 | Your player character is also defined by some key choices  you make. The first choice is a PC's **ancestry**, representing the  character's parents and heritage, such as barathu, human, or  vesk. Next |
| 10 | `merged::PZO22001 Starfinder Player Core 001-013::/page/6/Text/9` | 0.595920 | Aside from characters and monsters, the galaxy of  Starfinder itself can be a force at the table and in the  narrative. While the presence of the larger setting  can sometimes be an obvious hazard, su |

### Query 160
- Text: Summarize **affliction** An affliction can affect a creature for a long time,  over several different stages. The most common kinds are  curses, diseases, and poisons. 422–423
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 442-464::/page/0/Text/27']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 330-363: `0.3538`
  - PZO22001 Starfinder Player Core 406-423: `0.3340`
  - PZO22001 Starfinder Player Core 364-387: `0.3331`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 442-464::/page/0/Text/27', 'merged::PZO22001 Starfinder Player Core 442-464::/page/0/Text/28', 'merged::PZO22001 Starfinder Player Core 442-464::/page/0/Text/26']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 442-464::/page/0/Text/28` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 442-464::/page/0/Text/26` (reasons: ['graph_depth_1'])

### Query 161
- Text: Summarize **Skittermander**
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 040-057::/page/1/Text/45']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 058-073: `0.2429`
  - PZO22001 Starfinder Player Core 001-013: `0.2339`
  - PZO22001 Starfinder Player Core 424-441: `0.2181`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 040-057::/page/1/Text/45', 'merged::PZO22001 Starfinder Player Core 040-057::/page/1/Text/44', 'merged::PZO22001 Starfinder Player Core 040-057::/page/1/Text/46']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 040-057::/page/1/Text/44` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 040-057::/page/1/Text/46` (reasons: ['graph_depth_1'])

### Query 162
- Text: What is the rule about At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As a lashunta, you choose from among  the following ancestry feats.?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 058-073::/page/2/Text/7']
- Expected found: `True`
- Expected rank: `1`
- Routed chapters:
  - PZO22001 Starfinder Player Core 210-231: `0.5255`
  - PZO22001 Starfinder Player Core 040-057: `0.4883`
  - PZO22001 Starfinder Player Core 058-073: `0.4684`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 058-073::/page/2/Text/7', 'merged::PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/6', 'merged::PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/8']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/6` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/8` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 058-073::/page/2/Text/7` | 0.924696 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As a lashunta, you choose from among  the following |
| 2 | `merged::PZO22001 Starfinder Player Core 040-057::/page/12/Text/4` | 0.828839 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As a human, you choose from among the  following anc |
| 3 | `merged::PZO22001 Starfinder Player Core 040-057::/page/8/Text/4` | 0.787715 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th,  9th, 13th, and 17th level). As a barathu, you choose from  among the following a |
| 4 | `merged::PZO22001 Starfinder Player Core 040-057::/page/16/Text/7` | 0.779727 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As a kasatha, you choose from among  the following a |
| 5 | `merged::PZO22001 Starfinder Player Core 058-073::/page/6/Text/7` | 0.760816 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As a pahtra, you choose from among the  following an |
| 6 | `merged::PZO22001 Starfinder Player Core 040-057::/page/4/Text/5` | 0.752989 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As an android, you choose from among  the following |
| 7 | `merged::PZO22001 Starfinder Player Core 058-073::/page/10/Text/11` | 0.747847 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As a shirren, you choose from among the  following a |
| 8 | `merged::PZO22001 Starfinder Player Core 058-073::/page/14/Text/7` | 0.719925 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As a skittermander, you choose from  among the follo |
| 9 | `merged::PZO22001 Starfinder Player Core 040-057::/page/1/Text/33` | 0.715065 | This section presents ancestry feats, which allow you to  customize your character. You gain your first ancestry feat  at 1st level, and you gain another at 5th level, 9th level, 13th  level, and 17th |
| 10 | `merged::PZO22001 Starfinder Player Core 040-057::/page/1/Text/34` | 0.677742 | As a starting character, you can choose from only 1stlevel ancestry feats, but later choices can be made from any  feat of your level or lower. These feats also sometimes list  prerequisites, which ar |

### Query 163
- Text: Summarize 6 PLAYER CORE
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 268-281::/page/1/SectionHeader/0']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 388-405: `0.3827`
  - PZO22001 Starfinder Player Core 098-113: `0.3474`
  - PZO22001 Starfinder Player Core 442-464: `0.3424`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 268-281::/page/1/SectionHeader/0', 'merged::PZO22001 Starfinder Player Core 268-281::/page/0/Text/53', 'merged::PZO22001 Starfinder Player Core 268-281::/page/1/Text/1']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 268-281::/page/0/Text/53` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 268-281::/page/1/Text/1` (reasons: ['graph_depth_1'])

### Query 164
- Text: What are the requirements for **GUARDED THOUGHTS** **FEAT 9**?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/24']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 210-231: `0.3424`
  - PZO22001 Starfinder Player Core 150-161: `0.2960`
  - PZO22001 Starfinder Player Core 250-267: `0.2788`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/24', 'merged::PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/23', 'merged::PZO22001 Starfinder Player Core 058-073::/page/3/Text/26']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/23` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 058-073::/page/3/Text/26` (reasons: ['graph_depth_1'])

### Query 165
- Text: What is the rule about **Downtime mode** (page 433) takes place over days. You  might make money, train, or recover, among other things.?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 388-405::/page/2/Text/6']
- Expected found: `True`
- Expected rank: `1`
- Routed chapters:
  - PZO22001 Starfinder Player Core 388-405: `0.4791`
  - PZO22001 Starfinder Player Core 424-441: `0.4219`
  - PZO22001 Starfinder Player Core 406-423: `0.3594`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 388-405::/page/2/Text/6', 'merged::PZO22001 Starfinder Player Core 388-405::/page/2/Text/5', 'merged::PZO22001 Starfinder Player Core 388-405::/page/2/SectionHeader/7']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 388-405::/page/2/Text/5` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 388-405::/page/2/SectionHeader/7` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 388-405::/page/2/Text/6` | 0.927390 | **Downtime mode** (page 433) takes place over days. You  might make money, train, or recover, among other things. |
| 2 | `merged::PZO22001 Starfinder Player Core 388-405::/page/1/Text/6` | 0.670662 | The third mode is **downtime**. During downtime, the  characters are at little risk, and the passage of time is  measured in days or longer. This is when you might repair  or craft new equipment, rese |
| 3 | `merged::PZO22001 Starfinder Player Core 424-441::/page/9/Text/1` | 0.605663 | Downtime mode is played day-by-day rather than minute-by-minute or scene-by-scene. Usually,  this mode of play occurs when you're in the safety of a settlement, maybe recovering from your  adventures |
| 4 | `merged::PZO22001 Starfinder Player Core 406-423::/page/11/Text/42` | 0.590756 | **Mode** **Downtime ** |
| 5 | `merged::PZO22001 Starfinder Player Core 388-405::/page/2/Text/5` | 0.585882 | **Exploration** **mode** (page 430) takes place over minutes or  hours. You use your travel Speed if you're moving, and you  engage in **exploration** **activities** like Avoiding Notice, Detecting  M |
| 6 | `merged::PZO22001 Starfinder Player Core 406-423::/page/7/Text/50` | 0.578471 | **Downtime ** **Mode** |
| 7 | `merged::PZO22001 Starfinder Player Core 388-405::/page/7/Text/37` | 0.578471 | **Downtime ** **Mode** |
| 8 | `merged::PZO22001 Starfinder Player Core 424-441::/page/1/Text/49` | 0.578471 | **Downtime ** **Mode** |
| 9 | `merged::PZO22001 Starfinder Player Core 424-441::/page/7/Text/68` | 0.578471 | **Downtime ** **Mode** |
| 10 | `merged::PZO22001 Starfinder Player Core 388-405::/page/11/Text/38` | 0.578471 | **Downtime ** **Mode** |

### Query 166
- Text: Summarize **Requirements** You have a focus pool.
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 294-329::/page/2/Text/19']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Character Sheet: `0.3359`
  - PZO22001 Starfinder Player Core 126-137: `0.3042`
  - PZO22001 Starfinder Player Core 210-231: `0.3010`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 294-329::/page/2/Text/19', 'merged::PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/18', 'merged::PZO22001 Starfinder Player Core 294-329::/page/2/Text/20']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/18` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 294-329::/page/2/Text/20` (reasons: ['graph_depth_1'])

### Query 167
- Text: What is the rule about You reshape terrain and manipulate events to match other realities. You cast powerful  spells and recenter yourself through your anchor when pushed to your limits.?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 162-173::/page/1/Text/13']
- Expected found: `True`
- Expected rank: `1`
- Routed chapters:
  - PZO22001 Starfinder Player Core 162-173: `0.5207`
  - PZO22001 Starfinder Player Core 442-464: `0.4937`
  - PZO22001 Starfinder Player Core 364-387: `0.4905`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 162-173::/page/1/Text/13', 'merged::PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/14', 'merged::PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/12']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/14` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/12` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 162-173::/page/1/Text/13` | 0.867532 | You reshape terrain and manipulate events to match other realities. You cast powerful  spells and recenter yourself through your anchor when pushed to your limits. |
| 2 | `merged::PZO22001 Starfinder Player Core 162-173::/page/1/Text/2` | 0.563612 | A strange paradoxical event forever altered your existence, and now you can manipulate reality. You  explore the infinite possibilities of the multiverse, possibly visualizing variant timelines or par |
| 3 | `merged::PZO22001 Starfinder Player Core 162-173::/page/3/Text/3` | 0.552339 | Your paradox grants you magical power. You can cast spells  using the Cast a Spell activity. As a witchwarper, when you  cast spells, you might describe your revelations about other  realities aloud, |
| 4 | `merged::PZO22001 Starfinder Player Core 364-387::/page/14/ListItem/14` | 0.537254 | You suppress terrain in your field, turning any existing  difficult or greater difficult terrain in your quantum field  to normal terrain. This does not apply to effects that  cause a creature to coun |
| 5 | `merged::PZO22001 Starfinder Player Core 162-173::/page/10/Text/49` | 0.532352 | By reaching across both time and space, you can borrow the  use of a spell from a version of yourself inhabiting another  reality. During this turn, you can cast one spell without  spending a spell sl |
| 6 | `merged::PZO22001 Starfinder Player Core 162-173::/page/1/Text/19` | 0.530282 | You craft magic items for your party. You might travel to other dimensions or distant  star systems as part of your training or embark on such journeys by accident. |
| 7 | `merged::PZO22001 Starfinder Player Core 162-173::/page/6/Text/26` | 0.529886 | Your anchor keeps you centered, reminding you what's  real, and helps counter the disorienting effects one might  experience by causing paradoxes. You select your anchor at 1st  level. Your anchor gra |
| 8 | `merged::PZO22001 Starfinder Player Core 364-387::/page/14/Text/12` | 0.519322 | You materialize terrain features from another reality within  your quantum field. Choose one of the following effects, which  lasts as long as your quantum field remains active, until you  cast *warp* |
| 9 | `merged::PZO22001 Starfinder Player Core 364-387::/page/14/ListItem/13` | 0.515798 | You cause the area of your quantum field to become  difficult terrain. You determine the appearance of the  warped terrain. You and your allies can move through  the warped terrain normally and can Ta |
| 10 | `merged::PZO22001 Starfinder Player Core 162-173::/page/11/Text/32` | 0.514913 | You become a true embodiment of your paradox and surpass  what mortals can achieve in your reality. You gain an additional  10th-rank spell slot. |

### Query 168
- Text: Summarize Carbon shield, commercial
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/630']
- Expected found: `True`
- Expected rank: `1`
- Routed chapters:
  - PZO22001 Starfinder Player Core 250-267: `0.3517`
  - PZO22001 Starfinder Player Core 268-281: `0.2353`
  - PZO22001 Starfinder Player Core 232-249: `0.2068`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/630', 'merged::PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/629', 'merged::PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/631']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/629` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/631` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/630` | 0.951868 | Carbon shield, commercial |
| 2 | `merged::PZO22001 Starfinder Player Core 268-281::/page/3/TableCell/691` | 0.738530 | Energy shielding, commercial |
| 3 | `merged::PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/639` | 0.730089 | Compact shield, commercial |
| 4 | `merged::PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/675` | 0.685759 | Phase shield, commercial |
| 5 | `merged::PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/657` | 0.660509 | Irising shield, commercial |
| 6 | `merged::PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/684` | 0.650180 | Riot shield, commercial |
| 7 | `merged::PZO22001 Starfinder Player Core 250-267::/page/1/Text/13` | 0.576039 | **Carbon** **Shield:** This durable yet lightweight defensive  plate comes in a variety of shapes and sizes, and it's often  customized with LED displays that broadcast personal  insignia or an organi |
| 8 | `merged::PZO22001 Starfinder Player Core 250-267::/page/1/Table/2` | 0.551039 | ShieldLevelPriceAC Bonus1Speed PenaltyBulkHardnessHP (BT)TraitsCarbon shield, commercial025+2—1520 (10)AnalogCompact shield, commercial015+1—L48 (4)Analog, compactDeflecting field, commercial010+1——24 |
| 9 | `merged::PZO22001 Starfinder Player Core 268-281::/page/3/TableCell/743` | 0.532080 | Energy shielding, advanced |
| 10 | `merged::PZO22001 Starfinder Player Core 250-267::/page/15/Text/15` | 0.521965 | Shields |

### Query 169
- Text: What is the rule about All tasks that take longer than a turn are activities. If an  activity is meant to be done during exploration, it has the  exploration trait. An activity that takes a day or more of  commitment and that can be done only during downtime  has the downtime trait.?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 014-029::/page/2/Text/4']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 388-405: `0.4641`
  - PZO22001 Starfinder Player Core 406-423: `0.4409`
  - PZO22001 Starfinder Player Core 424-441: `0.4329`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 014-029::/page/2/Text/4', 'merged::PZO22001 Starfinder Player Core 014-029::/page/2/SectionHeader/5', 'merged::PZO22001 Starfinder Player Core 014-029::/page/2/Text/3']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 014-029::/page/2/SectionHeader/5` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 014-029::/page/2/Text/3` (reasons: ['graph_depth_1'])

### Query 170
- Text: What is the rule about You set yourself up on the battlefield to rain down fire with heavy weapons. You  defy damage and keep your comrades safe from foes as they target you.?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 150-161::/page/1/Text/13']
- Expected found: `True`
- Expected rank: `1`
- Routed chapters:
  - PZO22001 Starfinder Player Core 150-161: `0.4744`
  - PZO22001 Starfinder Player Core 388-405: `0.4297`
  - PZO22001 Starfinder Player Core 406-423: `0.4127`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 150-161::/page/1/Text/13', 'merged::PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/14', 'merged::PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/12']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/14` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/12` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 150-161::/page/1/Text/13` | 0.866638 | You set yourself up on the battlefield to rain down fire with heavy weapons. You  defy damage and keep your comrades safe from foes as they target you. |
| 2 | `merged::PZO22001 Starfinder Player Core 150-161::/page/1/Text/2` | 0.623591 | You're a master of area weapons, heavy armor, and soaking damage. You fight in the thick of the  battle and unleash devastating salvos against your foes as you take withering fire in return. By laying |
| 3 | `merged::PZO22001 Starfinder Player Core 150-161::/page/8/Text/3` | 0.595345 | You lay down heavy fire with big guns while body  blocking for your allies. |
| 4 | `merged::PZO22001 Starfinder Player Core 150-161::/page/3/Text/3` | 0.563125 | There's nothing like a big gun (or maybe several) to get you  through tough times. You've come to terms with the fact that  a stray bullet from one of your barrages might sometimes hit  an ally, but y |
| 5 | `merged::PZO22001 Starfinder Player Core 150-161::/page/2/Text/19` | 0.554976 | Your armor feels like a part of you and stands up to heavy fire  in the thick of battle. Your armor absorbs greater damage from  attacks made by enemies you've suppressed. In a fight, you  likely body |
| 6 | `merged::PZO22001 Starfinder Player Core 150-161::/page/2/Text/9` | 0.542673 | You have a knack for using powerful weapons to harry your  foes and hinder their movement, preventing them from  operating at their peak. If you make an attack with a weapon  that has the area trait ( |
| 7 | `merged::PZO22001 Starfinder Player Core 150-161::/page/1/ListItem/21` | 0.535131 | Use your heavy weapons to demand enemy attention in combat, enjoying the  challenge of battle while soaking attacks for your allies. |
| 8 | `merged::PZO22001 Starfinder Player Core 150-161::/page/2/Text/16` | 0.516771 | You believe that anything can be solved by shooting your way  out. Somehow, your bravado and over-the-top actions have  a way of working out for you, despite logic often suggesting  otherwise. To you, |
| 9 | `merged::PZO22001 Starfinder Player Core 150-161::/page/3/Text/6` | 0.514919 | While you have the necessary training to employ heavy  weapons, you believe it's important to keep a backup for when  foes get too close. You might be a veteran Veskarium trooper  who knows their way |
| 10 | `merged::PZO22001 Starfinder Player Core 150-161::/page/1/Text/17` | 0.503863 | You're at the front of the group. You position yourself so you can unload a magazine  into any ambush that might pop up while body blocking for your allies. |

### Query 171
- Text: What are the requirements for **ATTUNED WARDS** **FEAT 18**?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 138-149::/page/11/SectionHeader/11']
- Expected found: `True`
- Expected rank: `1`
- Routed chapters:
  - PZO22001 Starfinder Player Core 210-231: `0.2743`
  - PZO22001 Starfinder Player Core 150-161: `0.2681`
  - PZO22001 Starfinder Player Core 138-149: `0.2670`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 138-149::/page/11/SectionHeader/11', 'merged::PZO22001 Starfinder Player Core 138-149::/page/11/SectionHeader/10', 'merged::PZO22001 Starfinder Player Core 138-149::/page/11/SectionHeader/13']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 138-149::/page/11/SectionHeader/10` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 138-149::/page/11/SectionHeader/13` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 138-149::/page/11/SectionHeader/11` | 0.849378 | **ATTUNED WARDS** **FEAT 18** |
| 2 | `merged::PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/559` | 0.525432 | Attuned Wards |
| 3 | `merged::PZO22001 Starfinder Player Core 138-149::/page/11/SectionHeader/2` | 0.518203 | **ATTUNED BLOW** **FEAT 16** |
| 4 | `merged::PZO22001 Starfinder Player Core 138-149::/page/11/SectionHeader/26` | 0.466703 | **PERFECTLY-ATTUNED** **FEAT 20** |
| 5 | `merged::PZO22001 Starfinder Player Core 138-149::/page/11/SectionHeader/17` | 0.455177 | **HOMING MOTE** **FEAT 18** |
| 6 | `merged::PZO22001 Starfinder Player Core 138-149::/page/10/Text/23` | 0.447791 | **Requirements** You're photon-attuned. |
| 7 | `merged::PZO22001 Starfinder Player Core 138-149::/page/7/Text/18` | 0.447791 | **Requirements** You're photon-attuned. |
| 8 | `merged::PZO22001 Starfinder Player Core 150-161::/page/11/SectionHeader/4` | 0.424781 | **COORDINATED FIRE **[three-actions] **FEAT 18** |
| 9 | `merged::PZO22001 Starfinder Player Core 138-149::/page/6/Text/3` | 0.399138 | **Attuned:** You can't use abilities with the attuned  trait while you're unattuned. Many attuned abilities  require you to be specifically graviton-attuned or  photon-attuned, while others can grant |
| 10 | `merged::PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/51` | 0.393663 | **SOLDIER'S TRAINING** **FEAT 16** |

### Query 172
- Text: Summarize HP (BT)
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/628']
- Expected found: `True`
- Expected rank: `1`
- Routed chapters:
  - PZO22001 Starfinder Player Core 014-029: `0.3197`
  - PZO22001 Starfinder Player Core 250-267: `0.3040`
  - PZO22001 Starfinder Player Core 150-161: `0.2638`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/628', 'merged::PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/629', 'merged::PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/627']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/629` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/627` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/628` | 0.895073 | HP (BT) |
| 2 | `merged::PZO22001 Starfinder Player Core 250-267::/page/0/SectionHeader/13` | 0.895073 | HP (BT) |
| 3 | `merged::PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/698` | 0.633690 | HP |
| 4 | `merged::PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/699` | 0.551162 | BT |
| 5 | `merged::PZO22001 Starfinder Player Core 250-267::/page/0/Text/14` | 0.511955 | This column lists the shield's Hit Points (HP) and Broken  Threshold (BT). These measure how much damage the shield  can take before it's destroyed (its total HP) and how much it  can take before bein |
| 6 | `merged::PZO22001 Starfinder Player Core 250-267::/page/1/Table/2` | 0.433034 | ShieldLevelPriceAC Bonus1Speed PenaltyBulkHardnessHP (BT)TraitsCarbon shield, commercial025+2—1520 (10)AnalogCompact shield, commercial015+1—L48 (4)Analog, compactDeflecting field, commercial010+1——24 |
| 7 | `merged::PZO22001 Starfinder Player Core 250-267::/page/1/Table/6` | 0.432628 | GradeLevelUpgrade PriceTotal Value1HardnessHPBTCommercial0—————Tactical5+750 credits750 credits+3+46+23Advanced8+2,250 credits3,000 credits+3+56+28Superior11+6,000 credits9,000 credits+3+68+34Elite14+ |
| 8 | `merged::PZO22001 Starfinder Player Core 150-161::/page/1/Text/11` | 0.370903 | You increase your maximum number  of HP by this number at 1st level and  every level thereafter. |
| 9 | `merged::PZO22001 Starfinder Player Core 250-267::/page/14/TableCell/101` | 0.302336 | Agile, finesse, powered, tech, versatile P |
| 10 | `merged::PZO22001 Starfinder Player Core 250-267::/page/14/TableCell/110` | 0.302336 | Agile, finesse, powered, tech, versatile P |

### Query 173
- Text: What are the requirements for **Prerequisites** Envoy Dedication?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 174-181::/page/1/Text/34']
- Expected found: `True`
- Expected rank: `1`
- Routed chapters:
  - PZO22001 Starfinder Player Core 098-113: `0.3456`
  - PZO22001 Starfinder Player Core 174-181: `0.2562`
  - PZO22001 Starfinder Player Core 232-249: `0.2194`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 174-181::/page/1/Text/34', 'merged::PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/33', 'merged::PZO22001 Starfinder Player Core 174-181::/page/1/Text/35']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/33` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 174-181::/page/1/Text/35` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 174-181::/page/1/Text/34` | 0.901082 | **Prerequisites** Envoy Dedication |
| 2 | `merged::PZO22001 Starfinder Player Core 174-181::/page/1/Text/39` | 0.901082 | **Prerequisites** Envoy Dedication |
| 3 | `merged::PZO22001 Starfinder Player Core 174-181::/page/1/Text/24` | 0.901082 | **Prerequisites** Envoy Dedication |
| 4 | `merged::PZO22001 Starfinder Player Core 174-181::/page/1/Text/19` | 0.901082 | **Prerequisites** Envoy Dedication |
| 5 | `merged::PZO22001 Starfinder Player Core 174-181::/page/5/Text/39` | 0.601078 | **Prerequisites** Soldier Dedication |
| 6 | `merged::PZO22001 Starfinder Player Core 174-181::/page/5/Text/34` | 0.601078 | **Prerequisites** Soldier Dedication |
| 7 | `merged::PZO22001 Starfinder Player Core 174-181::/page/5/Text/18` | 0.601078 | **Prerequisites** Soldier Dedication |
| 8 | `merged::PZO22001 Starfinder Player Core 174-181::/page/3/Text/50` | 0.578570 | **Prerequisites** Operative Dedication |
| 9 | `merged::PZO22001 Starfinder Player Core 174-181::/page/3/Text/55` | 0.578570 | **Prerequisites** Operative Dedication |
| 10 | `merged::PZO22001 Starfinder Player Core 174-181::/page/3/Text/60` | 0.578570 | **Prerequisites** Operative Dedication |

### Query 174
- Text: Summarize Fast Recovery
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/430']
- Expected found: `True`
- Expected rank: `1`
- Routed chapters:
  - PZO22001 Starfinder Player Core 388-405: `0.2383`
  - PZO22001 Starfinder Player Core 364-387: `0.2353`
  - PZO22001 Starfinder Player Core 210-231: `0.2124`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/430', 'merged::PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/429', 'merged::PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/431']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/429` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/431` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/430` | 0.881665 | Fast Recovery |
| 2 | `merged::PZO22001 Starfinder Player Core 210-231::/page/10/SectionHeader/34` | 0.732739 | **FAST RECOVERY** **FEAT 1** |
| 3 | `merged::PZO22001 Starfinder Player Core 210-231::/page/4/TableCell/418` | 0.638074 | Robust Recovery |
| 4 | `merged::PZO22001 Starfinder Player Core 388-405::/page/14/SectionHeader/11` | 0.626462 | FAST HEALING AND  REGENERATION |
| 5 | `merged::PZO22001 Starfinder Player Core 210-231::/page/4/TableCell/414` | 0.591125 | Continual Recovery |
| 6 | `merged::PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/433` | 0.537124 | Regain more HP from rest, recover faster from disease |
| 7 | `merged::PZO22001 Starfinder Player Core 210-231::/page/16/SectionHeader/36` | 0.506617 | **QUICK REPAIR** **FEAT 1** |
| 8 | `merged::PZO22001 Starfinder Player Core 388-405::/page/16/SectionHeader/18` | 0.502626 | **HEROIC RECOVERY** |
| 9 | `merged::PZO22001 Starfinder Player Core 210-231::/page/17/SectionHeader/18` | 0.496581 | **ROBUST RECOVERY** **FEAT 2** |
| 10 | `merged::PZO22001 Starfinder Player Core 210-231::/page/8/SectionHeader/8` | 0.491982 | **CONTINUAL RECOVERY** **FEAT 2** |

### Query 175
- Text: Summarize The pahtra solarian **Dae** loves showing off  by combining their flashy dance moves with  solar flares or turning their battle ribbon into  a electrotether or a whip of solar fire.
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 098-113::/page/3/Text/14']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 138-149: `0.5218`
  - PZO22001 Starfinder Player Core 058-073: `0.4261`
  - PZO22001 Starfinder Player Core 174-181: `0.3915`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 098-113::/page/3/Text/14', 'merged::PZO22001 Starfinder Player Core 098-113::/page/3/Text/15', 'merged::PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/13']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 098-113::/page/3/Text/15` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/13` (reasons: ['graph_depth_1'])

### Query 176
- Text: What are the requirements for **Prerequisites** trained in Deception?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 210-231::/page/7/Text/34']
- Expected found: `True`
- Expected rank: `2`
- Routed chapters:
  - PZO22001 Starfinder Player Core 182-209: `0.3766`
  - PZO22001 Starfinder Player Core 092-097: `0.3369`
  - PZO22001 Starfinder Player Core 210-231: `0.3337`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 210-231::/page/7/Text/34', 'merged::PZO22001 Starfinder Player Core 210-231::/page/7/Text/35', 'merged::PZO22001 Starfinder Player Core 210-231::/page/7/Text/33']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 210-231::/page/7/Text/35` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 210-231::/page/7/Text/33` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 210-231::/page/10/Text/42` | 0.889915 | **Prerequisites** trained in Deception |
| 2 | `merged::PZO22001 Starfinder Player Core 210-231::/page/7/Text/34` | 0.889915 | **Prerequisites** trained in Deception |
| 3 | `merged::PZO22001 Starfinder Player Core 210-231::/page/10/Text/25` | 0.889915 | **Prerequisites** trained in Deception |
| 4 | `merged::PZO22001 Starfinder Player Core 210-231::/page/14/Text/5` | 0.889915 | **Prerequisites** trained in Deception |
| 5 | `merged::PZO22001 Starfinder Player Core 210-231::/page/14/Text/10` | 0.889915 | **Prerequisites** trained in Deception |
| 6 | `merged::PZO22001 Starfinder Player Core 210-231::/page/10/Text/52` | 0.806080 | **Prerequisites** expert in Deception |
| 7 | `merged::PZO22001 Starfinder Player Core 210-231::/page/16/Text/15` | 0.806080 | **Prerequisites** expert in Deception |
| 8 | `merged::PZO22001 Starfinder Player Core 210-231::/page/8/Text/6` | 0.806080 | **Prerequisites** expert in Deception |
| 9 | `merged::PZO22001 Starfinder Player Core 210-231::/page/18/Text/18` | 0.775207 | **Prerequisites** master in Deception |
| 10 | `merged::PZO22001 Starfinder Player Core 210-231::/page/12/Text/61` | 0.773271 | **Prerequisites **expert in Deception |

### Query 177
- Text: What is the rule about **aeon** (weapon trait) 255?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 442-464::/page/0/Text/25']
- Expected found: `True`
- Expected rank: `1`
- Routed chapters:
  - PZO22001 Starfinder Player Core 250-267: `0.4272`
  - PZO22001 Starfinder Player Core 442-464: `0.3610`
  - PZO22001 Starfinder Player Core 282-293: `0.3419`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 442-464::/page/0/Text/25', 'merged::PZO22001 Starfinder Player Core 442-464::/page/0/Text/24', 'merged::PZO22001 Starfinder Player Core 442-464::/page/0/Text/26']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 442-464::/page/0/Text/24` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 442-464::/page/0/Text/26` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 442-464::/page/0/Text/25` | 0.893315 | **aeon** (weapon trait) 255 |
| 2 | `merged::PZO22001 Starfinder Player Core 442-464::/page/1/Text/37` | 0.695292 | **automatic** (weapon trait) 255 |
| 3 | `merged::PZO22001 Starfinder Player Core 442-464::/page/0/Text/29` | 0.666345 | **agile** (weapon trait) 255 |
| 4 | `merged::PZO22001 Starfinder Player Core 442-464::/page/2/Text/4` | 0.651076 | **breakdown** (weapon trait) 255 |
| 5 | `merged::PZO22001 Starfinder Player Core 442-464::/page/2/Text/1` | 0.647274 | **boost** (weapon trait) 255 |
| 6 | `merged::PZO22001 Starfinder Player Core 442-464::/page/1/Text/42` | 0.644604 | **backswing** (weapon trait) 255 |
| 7 | `merged::PZO22001 Starfinder Player Core 442-464::/page/3/Text/16` | 0.644185 | **critical** (weapon trait) 256 |
| 8 | `merged::PZO22001 Starfinder Player Core 442-464::/page/1/Text/2` | 0.640475 | **arc** (weapon trait) 255 |
| 9 | `merged::PZO22001 Starfinder Player Core 442-464::/page/13/Text/31` | 0.638826 | **thought** (weapon trait) 258 |
| 10 | `merged::PZO22001 Starfinder Player Core 442-464::/page/10/Text/7` | 0.637665 | **professional** (weapon trait) 256 |

### Query 178
- Text: Summarize Languages —
- Expected chunk IDs: ['merged::PZO22001 Starfinder Character Sheet::/page/0/TableCell/79']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 040-057: `0.3678`
  - PZO22001 Starfinder Player Core 092-097: `0.3313`
  - PZO22001 Starfinder Player Core 014-029: `0.2946`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Character Sheet::/page/0/TableCell/79', 'merged::PZO22001 Starfinder Character Sheet::/page/0/TableCell/78', 'merged::PZO22001 Starfinder Character Sheet::/page/0/TableCell/80']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Character Sheet::/page/0/TableCell/78` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Character Sheet::/page/0/TableCell/80` (reasons: ['graph_depth_1'])

### Query 179
- Text: Summarize **CONCENTRATE** **EXPLORATION**
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/18']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 388-405: `0.3048`
  - PZO22001 Starfinder Player Core 424-441: `0.3023`
  - PZO22001 Starfinder Player Core 364-387: `0.2849`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/18', 'merged::PZO22001 Starfinder Player Core 294-329::/page/2/Text/19', 'merged::PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/17']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 294-329::/page/2/Text/19` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/17` (reasons: ['graph_depth_1'])

### Query 180
- Text: What does **FIREBALL **[two-actions] **SPELL 3** do?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 330-363::/page/2/Text/48']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 406-423: `0.4218`
  - PZO22001 Starfinder Player Core 388-405: `0.3397`
  - PZO22001 Starfinder Player Core 182-209: `0.3119`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 330-363::/page/2/Text/48', 'merged::PZO22001 Starfinder Player Core 330-363::/page/2/Text/41', 'merged::PZO22001 Starfinder Player Core 330-363::/page/2/Text/56']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 330-363::/page/2/Text/41` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 330-363::/page/2/Text/56` (reasons: ['graph_depth_1'])

### Query 181
- Text: Summarize ATTRIBUTE FLAW
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 040-057::/page/2/Text/7']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 182-209: `0.2396`
  - PZO22001 Starfinder Player Core 232-249: `0.2337`
  - PZO22001 Starfinder Player Core 250-267: `0.2178`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 040-057::/page/2/Text/7', 'merged::PZO22001 Starfinder Player Core 040-057::/page/2/Text/6', 'merged::PZO22001 Starfinder Player Core 040-057::/page/2/SectionHeader/8']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 040-057::/page/2/Text/6` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 040-057::/page/2/SectionHeader/8` (reasons: ['graph_depth_1'])

### Query 182
- Text: What is the rule about Spellcasters cast spells from one of four different spell lists, each representing a different magical tradition: arcane,  divine, occult, and primal.?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 294-329::/page/3/Text/2']
- Expected found: `True`
- Expected rank: `1`
- Routed chapters:
  - PZO22001 Starfinder Player Core 294-329: `0.5621`
  - PZO22001 Starfinder Player Core 330-363: `0.4823`
  - PZO22001 Starfinder Player Core 442-464: `0.4595`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 294-329::/page/3/Text/2', 'merged::PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/1', 'merged::PZO22001 Starfinder Player Core 294-329::/page/3/Text/3']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/1` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 294-329::/page/3/Text/3` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 294-329::/page/3/Text/2` | 0.908193 | Spellcasters cast spells from one of four different spell lists, each representing a different magical tradition: arcane,  divine, occult, and primal. |
| 2 | `merged::PZO22001 Starfinder Player Core 294-329::/page/3/Text/3` | 0.653649 | Your class determines which tradition of magic your spells use. In some cases, such as when a mystic gains spells from  their connection or when a witchwarper learns spells from their paradox, you mig |
| 3 | `merged::PZO22001 Starfinder Player Core 442-464::/page/7/Text/59` | 0.614230 | **magical tradition** Arcane, divine, occult, and primal are the  traditions of magic. 297 |
| 4 | `merged::PZO22001 Starfinder Player Core 294-329::/page/3/Text/7` | 0.603608 | Arcane spellcasters use logic and  rationality to categorize the magic inherent  in the world around them. Because of its far-reaching  approach, the arcane tradition has the broadest spell  list, tho |
| 5 | `merged::PZO22001 Starfinder Player Core 294-329::/page/1/Text/6` | 0.556239 | Characters of spellcasting classes can cast a number of spells  each day; the spells you can cast in a day are referred to as  spell slots. At 1st level, a character has only a small number  of 1st-ra |
| 6 | `merged::PZO22001 Starfinder Player Core 330-363::/page/3/Text/6` | 0.556175 | **Traditions** arcane, divine, occult, primal |
| 7 | `merged::PZO22001 Starfinder Player Core 294-329::/page/3/Text/15` | 0.555690 | systematic way. Witchwarpers touched by the Gap or  alternate timelines, as well as mystics who are psychically  linked to the Akashic Record, are occult spellcasters. |
| 8 | `merged::PZO22001 Starfinder Player Core 442-464::/page/13/Text/36` | 0.552143 | **tradition** A fundamental category of magic (arcane, divine,  occult, or primal). 297 |
| 9 | `merged::PZO22001 Starfinder Player Core 294-329::/page/4/Text/5` | 0.548011 | Spells can vary in how many actions they take, as shown in  the spell's stat block. You cast cantrips, spells from spell slots,  and focus spells using the same process, but must expend the  spell whe |
| 10 | `merged::PZO22001 Starfinder Player Core 442-464::/page/12/Text/28` | 0.539036 | traditions (arcane, divine, occult, and primal) 297 |

### Query 183
- Text: Lookup values for Varying Skill FeatsLevelPrerequisitesBenefitsAssurance1Trained in at least one skillReceive a fixed result on a skill checkDubious Knowledge1Trained in a skill with the
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 210-231::/page/1/Table/11']
- Expected found: `True`
- Expected rank: `1`
- Routed chapters:
  - PZO22001 Starfinder Player Core 182-209: `0.5771`
  - PZO22001 Starfinder Player Core 210-231: `0.5248`
  - PZO22001 Starfinder Player Core 092-097: `0.4201`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 210-231::/page/1/Table/11', 'merged::PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/482', 'merged::PZO22001 Starfinder Player Core 210-231::/page/1/SectionHeader/10']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/482` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 210-231::/page/1/SectionHeader/10` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 210-231::/page/1/Table/11` | 0.725766 | Varying Skill FeatsLevelPrerequisitesBenefitsAssurance1Trained in at least one skillReceive a fixed result on a skill checkDubious Knowledge1Trained in a skill with the Recall Knowledge actionLearn tr |
| 2 | `merged::PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/482` | 0.626365 | Varying Skill Feats |
| 3 | `merged::PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/413` | 0.626365 | Varying Skill Feats |
| 4 | `merged::PZO22001 Starfinder Player Core 210-231::/page/1/Text/7` | 0.587049 | In addition to the skill feats specifically associated with  each skill, there are some that can be taken with various  skills or even all skills, like Assurance. |
| 5 | `merged::PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/489` | 0.575024 | Receive a fixed result on a skill check |
| 6 | `merged::PZO22001 Starfinder Player Core 210-231::/page/6/Text/42` | 0.567269 | You know basic facts off the top of your head. Choose a skill  you're an expert in that has the Recall Knowledge action and  for which you have the Assurance feat. You can use the Recall  Knowledge ac |
| 7 | `merged::PZO22001 Starfinder Player Core 210-231::/page/2/Table/1` | 0.565880 | Varying Skill FeatsLevelPrerequisitesBenefitsRecognize Spell1Trained in Arcana, Nature, Occultism, or ReligionIdentify a spell as a reaction as it's being castSeasoned1Trained in Alcohol Lore, Cooking |
| 8 | `merged::PZO22001 Starfinder Player Core 210-231::/page/1/Text/6` | 0.563364 | you gain a skill feat, you must select a general feat with  the skill trait; you can't select a general feat that lacks the  skill trait. The level of a skill feat is typically the minimum  level at w |
| 9 | `merged::PZO22001 Starfinder Player Core 182-209::/page/4/Table/6` | 0.562692 | General Skill ActionProficiencyPageDecipher WritingTrained186Earn IncomeTrained186–188Identify MagicTrained188Learn a SpellTrained189–190Recall Knowledge [one-action]Untrained190–191SubsistUntrained19 |
| 10 | `merged::PZO22001 Starfinder Player Core 182-209::/page/10/Text/4` | 0.542773 | A brief description of the skill is followed by a list of actions  anyone can use, and then the actions you can perform only  if you are trained in that skill. Some actions list sample tasks  for each |

### Query 184
- Text: Summarize **Rituals**
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 364-387::/page/1/Text/83']
- Expected found: `True`
- Expected rank: `9`
- Routed chapters:
  - PZO22001 Starfinder Player Core 364-387: `0.4451`
  - PZO22001 Starfinder Character Sheet: `0.3276`
  - PZO22001 Starfinder Player Core 282-293: `0.2914`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 364-387::/page/1/Text/83', 'merged::PZO22001 Starfinder Player Core 364-387::/page/1/Text/82', 'merged::PZO22001 Starfinder Player Core 364-387::/page/1/Text/84']
- Expanded expected found: `True`
- Expanded expected rank: `9`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 364-387::/page/1/Text/82` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 364-387::/page/1/Text/84` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 364-387::/page/9/Text/61` | 0.921113 | **Rituals** |
| 2 | `merged::PZO22001 Starfinder Player Core 364-387::/page/3/Text/63` | 0.921113 | **Rituals** |
| 3 | `merged::PZO22001 Starfinder Player Core 364-387::/page/23/Text/45` | 0.921113 | **Rituals** |
| 4 | `merged::PZO22001 Starfinder Player Core 364-387::/page/5/Text/76` | 0.921113 | **Rituals** |
| 5 | `merged::PZO22001 Starfinder Player Core 364-387::/page/19/Text/57` | 0.921113 | **Rituals** |
| 6 | `merged::PZO22001 Starfinder Player Core 364-387::/page/11/Text/64` | 0.921113 | **Rituals** |
| 7 | `merged::PZO22001 Starfinder Player Core 364-387::/page/17/Text/31` | 0.921113 | **Rituals** |
| 8 | `merged::PZO22001 Starfinder Player Core 364-387::/page/13/Text/79` | 0.921113 | **Rituals** |
| 9 | `merged::PZO22001 Starfinder Player Core 364-387::/page/1/Text/83` | 0.921113 | **Rituals** |
| 10 | `merged::PZO22001 Starfinder Player Core 364-387::/page/21/Text/58` | 0.921113 | **Rituals** |

### Query 185
- Text: What are the requirements for **Prerequisites** trained in Medicine?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/20']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 092-097: `0.2807`
  - PZO22001 Starfinder Player Core 182-209: `0.2746`
  - PZO22001 Starfinder Player Core 210-231: `0.2425`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/20', 'merged::PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/19', 'merged::PZO22001 Starfinder Player Core 098-113::/page/13/Text/21']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/19` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 098-113::/page/13/Text/21` (reasons: ['graph_depth_1'])

### Query 186
- Text: What is the rule about **Spells**?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 364-387::/page/5/Text/74']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 182-209: `0.2968`
  - PZO22001 Starfinder Player Core 442-464: `0.2960`
  - PZO22001 Starfinder Player Core 330-363: `0.2912`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 364-387::/page/5/Text/74', 'merged::PZO22001 Starfinder Player Core 364-387::/page/5/Text/75', 'merged::PZO22001 Starfinder Player Core 364-387::/page/5/Text/73']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 364-387::/page/5/Text/75` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 364-387::/page/5/Text/73` (reasons: ['graph_depth_1'])

### Query 187
- Text: Lookup values for ItemLevelPriceBulkBipod, commercial021Silencer, commercial010LUndermounted grenade
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 268-281::/page/9/Table/18']
- Expected found: `True`
- Expected rank: `1`
- Routed chapters:
  - PZO22001 Starfinder Player Core 268-281: `0.3658`
  - PZO22001 Starfinder Player Core 250-267: `0.3368`
  - PZO22001 Starfinder Player Core 150-161: `0.3243`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 268-281::/page/9/Table/18', 'merged::PZO22001 Starfinder Player Core 268-281::/page/9/TableCell/835', 'merged::PZO22001 Starfinder Player Core 268-281::/page/9/SectionHeader/17']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 268-281::/page/9/TableCell/835` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 268-281::/page/9/SectionHeader/17` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 268-281::/page/9/Table/18` | 0.792768 | ItemLevelPriceBulkBipod, commercial021Silencer, commercial010LUndermounted grenade launcher, commercial0501Bipod, tactical11001Sniper's scope, commercial1150LUniclamp1100LBipod, advanced24501Smuggler' |
| 2 | `merged::PZO22001 Starfinder Player Core 268-281::/page/9/Table/19` | 0.679676 | ItemLevelPriceBulkFlaming module, commercial85,000—Frost module, commercial85,000—Loudener, commercial85,000LShock module, commercial85,000—Truesight sight, commercial88,000—Silencer, tactical97,500LS |
| 3 | `merged::PZO22001 Starfinder Player Core 268-281::/page/3/Table/3` | 0.611913 | ItemLevelPriceBulkDarkvision visor1150LForce field, commercial1200LGlamer projector1100LAuto-CPR unit2200LLoad lifter, commercial2550LJump jets3550LMobility enhancer, commercial31,000LForce field, tac |
| 4 | `merged::PZO22001 Starfinder Player Core 268-281::/page/13/Table/36` | 0.597116 | GrenadeItem LevelPriceDamageElectromag grenade, commercial0101d8 EFrag grenade, commercial0101d8 PIncendiary grenade, commercial0101d8 FFlash grenade, commercial010–Smoke grenade, commercial010–Electr |
| 5 | `merged::PZO22001 Starfinder Player Core 250-267::/page/17/Table/0` | 0.587423 | Advanced RangedWeaponsWeapon (Commercial)Item LevelPriceDamageRangeReloadBulkHandsMagazineExpendUpgradesGroupWeapon TraitsCard slinger0261d4 P30 ft.1L17 projectiles11DartAgile, concealable, deadly d8, |
| 6 | `merged::PZO22001 Starfinder Player Core 250-267::/page/16/Table/1` | 0.567484 | Martial Rangged WeaponsWeapon (Commercial)Item LevelPriceDamageRangeReloadBulkHandsMagazineExpendUpgradesGroupWeapon TraitsAssassin rifle01001d10 P120 ft.1121 projectile11SniperAnalog, backstabber, fa |
| 7 | `merged::PZO22001 Starfinder Player Core 268-281::/page/9/TableCell/847` | 0.562437 | Undermounted grenade launcher, commercial |
| 8 | `merged::PZO22001 Starfinder Player Core 250-267::/page/15/Table/3` | 0.549238 | Simple RangSimple Ranged WeaponsWeapon (Commercial)Item LevelPriceDamageRangeReloadBulkHandsMagazineExpendUpgradesGroupWeapon TraitsAcid dart rifle0401d8 A80 ft.1125 projectiles11CorrosiveAnalogArc pi |
| 9 | `merged::PZO22001 Starfinder Player Core 250-267::/page/17/Table/4` | 0.548861 | Projectile AmmoAmmunitionItem LevelPriceMagazineBulkProjectile ammo (10)01--BatteriesAmmunitionItemPriceMagazineBulkLevelMagazinioDuikBattery, commercialLevel 01010- JulikBattery, commercial Battery, |
| 10 | `merged::PZO22001 Starfinder Player Core 268-281::/page/2/Text/3` | 0.544395 | **Type **commercial; **Level **1; **Price **200 credits; **Bulk **L |

### Query 188
- Text: What is the rule about Attribute boosts, mystic feat, skill feat?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/407']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 210-231: `0.5337`
  - PZO22001 Starfinder Player Core 014-029: `0.4726`
  - PZO22001 Starfinder Player Core 182-209: `0.4723`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/407', 'merged::PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/406', 'merged::PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/408']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/406` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/408` (reasons: ['graph_depth_1'])

### Query 189
- Text: What is the rule about Trained in spell attack modifier Trained in spell DC?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 162-173::/page/1/Text/65']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 182-209: `0.4863`
  - PZO22001 Starfinder Player Core 442-464: `0.4218`
  - PZO22001 Starfinder Player Core 014-029: `0.4197`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 162-173::/page/1/Text/65', 'merged::PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/64', 'merged::PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/66']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/64` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/66` (reasons: ['graph_depth_1'])

### Query 190
- Text: What are the requirements for **PSYCHIC BULLY** **FEAT 5**?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 058-073::/page/3/Text/5']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 210-231: `0.3235`
  - PZO22001 Starfinder Player Core 014-029: `0.2871`
  - PZO22001 Starfinder Player Core 098-113: `0.2776`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 058-073::/page/3/Text/5', 'merged::PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/4', 'merged::PZO22001 Starfinder Player Core 058-073::/page/3/Text/7']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/4` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 058-073::/page/3/Text/7` (reasons: ['graph_depth_1'])

### Query 191
- Text: What are the requirements for **BORROW SPELL **[free-action] **FEAT 14**?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/44']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 014-029: `0.3233`
  - PZO22001 Starfinder Player Core 210-231: `0.3202`
  - PZO22001 Starfinder Player Core 250-267: `0.3035`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/44', 'merged::PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/43', 'merged::PZO22001 Starfinder Player Core 162-173::/page/10/Text/46']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/43` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 162-173::/page/10/Text/46` (reasons: ['graph_depth_1'])

### Query 192
- Text: What is the rule about Background ——?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Character Sheet::/page/0/TableCell/26']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 092-097: `0.4735`
  - PZO22001 Starfinder Player Core 040-057: `0.4032`
  - PZO22001 Starfinder Player Core 388-405: `0.3037`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Character Sheet::/page/0/TableCell/26', 'merged::PZO22001 Starfinder Character Sheet::/page/0/TableCell/28', 'merged::PZO22001 Starfinder Character Sheet::/page/0/TableCell/24']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Character Sheet::/page/0/TableCell/28` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Character Sheet::/page/0/TableCell/24` (reasons: ['graph_depth_1'])

### Query 193
- Text: What is the rule about When you Sustain this spell, you can levitate the flame up to  10 feet. It then deals damage to each creature whose space  it shared at any point during its flight. This uses the same  damage and save, and you roll the damage once each time  you Sustain. A given creature can take damage from *floating * *flame* only once per round.?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 330-363::/page/3/Text/1']
- Expected found: `True`
- Expected rank: `1`
- Routed chapters:
  - PZO22001 Starfinder Player Core 388-405: `0.4067`
  - PZO22001 Starfinder Player Core 406-423: `0.3875`
  - PZO22001 Starfinder Player Core 330-363: `0.3662`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 330-363::/page/3/Text/1', 'merged::PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/0', 'merged::PZO22001 Starfinder Player Core 330-363::/page/3/Text/2']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/0` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 330-363::/page/3/Text/2` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 330-363::/page/3/Text/1` | 0.947132 | When you Sustain this spell, you can levitate the flame up to  10 feet. It then deals damage to each creature whose space  it shared at any point during its flight. This uses the same  damage and save |
| 2 | `merged::PZO22001 Starfinder Player Core 330-363::/page/12/Text/36` | 0.605241 | **LEVITATE **[two-actions] **SPELL 3**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult  **Range **touch;** Targets** 1 unattended object or willing creature **Duration** 5 minutes  You |
| 3 | `merged::PZO22001 Starfinder Player Core 330-363::/page/2/Text/69` | 0.560335 | **FLOATING FLAME **[two-actions] **SPELL 2**  **CONCENTRATE** **FIRE** **MANIPULATE**  **Traditions** arcane, primal  **Range **30 feet; **Targets** one 5-foot square  **Defense** Reflex; **Duration** |
| 4 | `merged::PZO22001 Starfinder Player Core 406-423::/page/7/Text/11` | 0.559489 | A dropped object takes damage just like a falling creature. If  the object lands on a creature, that creature can attempt a  Reflex save using the same rules as for a creature falling on a  creature. |
| 5 | `merged::PZO22001 Starfinder Player Core 330-363::/page/9/Text/3` | 0.552193 | In combat, the illusion can use 2 actions per turn, which  it uses when you Sustain the spell. It uses your spell attack  modifier for attack rolls and your spell DC for its AC. Its  saving throw modi |
| 6 | `merged::PZO22001 Starfinder Player Core 406-423::/page/5/Text/41` | 0.526528 | Choose one of your effects that has a sustained duration or  lists a special benefit when you Sustain it. Most such effects  come from spells or magic item activations. If the effect has a  sustained |
| 7 | `merged::PZO22001 Starfinder Player Core 330-363::/page/1/SectionHeader/44` | 0.519881 | **FALLING STARS **[two-actions] **SPELL 9**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal  **Range **500 feet;** Area** four 40-foot bursts  **Defense** basic Reflex  You reach into t |
| 8 | `merged::PZO22001 Starfinder Player Core 330-363::/page/10/SectionHeader/25` | 0.518033 | **IMPLOSION **[two-actions] **SPELL 9**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal  **Range **30 feet;** Targets** 1 corporeal creature  **Defense** basic Fortitude; **Duration** s |
| 9 | `merged::PZO22001 Starfinder Player Core 388-405::/page/3/Text/8` | 0.514054 | You may need to calculate a fraction of a value, like halving  damage. Always round down unless otherwise specified.  For example, if a spell deals 7 damage and a creature takes  half damage from it, |
| 10 | `merged::PZO22001 Starfinder Player Core 330-363::/page/28/Text/16` | 0.510898 | **SHARE LIFE **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE**  **Traditions** divine  **Range **30 feet;** Targets** 1 creature  **Duration** 10 minutes  You forge a temporary link between |

### Query 194
- Text: Summarize **circumstance penalty** A penalty due to a situation. 392
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 442-464::/page/2/Text/30']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 424-441: `0.3337`
  - PZO22001 Starfinder Player Core 250-267: `0.3211`
  - PZO22001 Starfinder Player Core 388-405: `0.3129`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 442-464::/page/2/Text/30', 'merged::PZO22001 Starfinder Player Core 442-464::/page/2/Text/29', 'merged::PZO22001 Starfinder Player Core 442-464::/page/2/Text/31']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 442-464::/page/2/Text/29` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 442-464::/page/2/Text/31` (reasons: ['graph_depth_1'])

### Query 195
- Text: What is the rule about **Heightened (4th)** The spell's range is touch and it targets 1  willing creature.?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 330-363::/page/2/Text/24']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 364-387: `0.4439`
  - PZO22001 Starfinder Player Core 294-329: `0.3774`
  - PZO22001 Starfinder Player Core 250-267: `0.3665`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 330-363::/page/2/Text/24', 'merged::PZO22001 Starfinder Player Core 330-363::/page/2/Text/25', 'merged::PZO22001 Starfinder Player Core 330-363::/page/2/Text/23']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 330-363::/page/2/Text/25` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 330-363::/page/2/Text/23` (reasons: ['graph_depth_1'])

### Query 196
- Text: What are the requirements for **GET IN THERE! **[one-action]** TO **[two-actions] **FEAT 2**?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/18']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 406-423: `0.3991`
  - PZO22001 Starfinder Player Core 014-029: `0.3738`
  - PZO22001 Starfinder Player Core 210-231: `0.3662`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/18', 'merged::PZO22001 Starfinder Player Core 098-113::/page/11/Text/17', 'merged::PZO22001 Starfinder Player Core 098-113::/page/11/Text/19']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 098-113::/page/11/Text/17` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 098-113::/page/11/Text/19` (reasons: ['graph_depth_1'])

### Query 197
- Text: Summarize Task Difficulty
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/247']
- Expected found: `True`
- Expected rank: `1`
- Routed chapters:
  - PZO22001 Starfinder Player Core 388-405: `0.2869`
  - PZO22001 Starfinder Player Core 182-209: `0.2686`
  - PZO22001 Starfinder Player Core 014-029: `0.2642`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/247', 'merged::PZO22001 Starfinder Player Core 182-209::/page/2/Table/4', 'merged::PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/248']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 182-209::/page/2/Table/4` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/248` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/247` | 0.826163 | Task Difficulty |
| 2 | `merged::PZO22001 Starfinder Player Core 182-209::/page/2/Table/4` | 0.565712 | Task DifficultySimple DCUntrained10Trained15Expert20Master30Legendary40 |
| 3 | `merged::PZO22001 Starfinder Player Core 182-209::/page/22/SectionHeader/11` | 0.488102 | **SAMPLE PERFORM TASKS** |
| 4 | `merged::PZO22001 Starfinder Player Core 182-209::/page/11/SectionHeader/2` | 0.472967 | **SAMPLE SQUEEZE TASKS** |
| 5 | `merged::PZO22001 Starfinder Player Core 182-209::/page/9/SectionHeader/28` | 0.453439 | **SAMPLE SUBSIST TASKS** |
| 6 | `merged::PZO22001 Starfinder Player Core 182-209::/page/4/SectionHeader/20` | 0.428003 | **SAMPLE DECIPHER TASKS** |
| 7 | `merged::PZO22001 Starfinder Player Core 182-209::/page/10/SectionHeader/16` | 0.423230 | **SAMPLE BALANCE TASKS** |
| 8 | `merged::PZO22001 Starfinder Player Core 182-209::/page/5/TableCell/579` | 0.419281 | Task Level |
| 9 | `merged::PZO22001 Starfinder Player Core 182-209::/page/11/SectionHeader/28` | 0.415491 | **SAMPLE CLIMB TASKS** |
| 10 | `merged::PZO22001 Starfinder Player Core 182-209::/page/14/SectionHeader/13` | 0.413133 | **SAMPLE OPERATE DEVICE TASKS** |

### Query 198
- Text: What does **TRANSLATE **[two-actions] **SPELL 2** do?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 364-387::/page/4/SectionHeader/23']
- Expected found: `False`
- Expected rank: `None`
- Routed chapters:
  - PZO22001 Starfinder Player Core 406-423: `0.3727`
  - PZO22001 Starfinder Player Core 388-405: `0.2990`
  - PZO22001 Starfinder Player Core 182-209: `0.2803`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 364-387::/page/4/SectionHeader/23', 'merged::PZO22001 Starfinder Player Core 364-387::/page/4/SectionHeader/15', 'merged::PZO22001 Starfinder Player Core 364-387::/page/4/SectionHeader/30']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 364-387::/page/4/SectionHeader/15` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 364-387::/page/4/SectionHeader/30` (reasons: ['graph_depth_1'])

### Query 199
- Text: What is the rule about If you want a character who's duty bound, brave, and stoic,  you should play a vesk.?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 074-091::/page/1/Text/10']
- Expected found: `True`
- Expected rank: `1`
- Routed chapters:
  - PZO22001 Starfinder Player Core 074-091: `0.4456`
  - PZO22001 Starfinder Player Core 098-113: `0.3930`
  - PZO22001 Starfinder Character Sheet: `0.3886`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 074-091::/page/1/Text/10', 'merged::PZO22001 Starfinder Player Core 074-091::/page/1/Text/9', 'merged::PZO22001 Starfinder Player Core 074-091::/page/1/SectionHeader/11']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 074-091::/page/1/Text/9` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 074-091::/page/1/SectionHeader/11` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 074-091::/page/1/Text/10` | 0.906825 | If you want a character who's duty bound, brave, and stoic,  you should play a vesk. |
| 2 | `merged::PZO22001 Starfinder Player Core 074-091::/page/1/SectionHeader/18` | 0.593754 | Most vesk in the Veskarium venerate Damoritosh the  Conqueror, god of duty and war, and his army of battle  saints. In life, the saints were mortal paragons who embodied  vesk cultural values and atta |
| 3 | `merged::PZO22001 Starfinder Player Core 074-091::/page/1/Text/56` | 0.565618 | and conflicts within the Veskarium tend to be as disciplined  as they are violent, stretching to accommodate opposing  sides following the prescribed order of war. A typical vesk  always respects thei |
| 4 | `merged::PZO22001 Starfinder Player Core 074-091::/page/1/Text/9` | 0.522967 | Vesk have a long history of conflict, first as conquerors within  their own star system and later clashing with neighboring  stellar powers such as the Pact Worlds and the Swarm.  Currently, the Veska |
| 5 | `merged::PZO22001 Starfinder Player Core 074-091::/page/2/Text/7` | 0.508664 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As a vesk, you choose from among the  following ance |
| 6 | `merged::PZO22001 Starfinder Player Core 098-113::/page/1/Text/4` | 0.507903 | The rules within each class allow you to bring a wealth of  character concepts to life. Perhaps you want to create an  observant but impulsive mystic who can see the pain in  someone's eyes but can't |
| 7 | `merged::PZO22001 Starfinder Player Core 074-091::/page/2/Text/32` | 0.504374 | You're trained with all doshkos. In addition, you gain access to  all uncommon weapons with the vesk trait. For the purposes  of proficiency, you treat any of these that are martial weapons |
| 8 | `merged::PZO22001 Starfinder Player Core 074-091::/page/1/Text/16` | 0.486232 | Vesk names typically combine elements of their parents'  names as well as those of other prominent ancestors.  Companions often shorten these names for casual use, but  doing so without permission is |
| 9 | `merged::PZO22001 Starfinder Player Core 074-091::/page/0/SectionHeader/1` | 0.481564 | VESK |
| 10 | `merged::PZO22001 Starfinder Player Core 074-091::/page/0/Text/2` | 0.476083 | Vesk are a warmongering, reptilian people who conquered the eight worlds in their solar system shortly after they developed spaceflight, forming the Veskarium empire. Vesk tend to embrace conflict and |
