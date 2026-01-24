# RulesLawyer Evaluation Report: nomic-embed-text-v2

## Summary
- Run ID: `2026-01-23-full-source`
- Ruleset ID: `None`
- Document ID: `None`
- Chunk source: `enriched`
- Chunk count: `23248`
- Query count: `200`
- Evaluated queries: `141`
- Coverage: `0.7050`
- MRR: `0.8380`
- hit@1: `0.7943`
- hit@3: `0.8582`
- hit@5: `0.8723`
- hit@10: `0.9078`
- Embeddings reused: `True`
- Graph boost: `0.05` (depth=2, top_k=50, source=top, seed_top_n=3, same_kind_only=False, decay=0.4)
- Chapter routing: `top_n=12` (source=summary, chapters=29, avg_allowed_chunks=9921.83, expected_recall=0.705)

### Expanded Gold Metrics
- Coverage: `0.7050`
- MRR: `0.8482`
- hit@1: `0.8085`
- hit@3: `0.8652`
- hit@5: `0.8794`
- hit@10: `0.9149`

### Expanded Gold Expansion Stats
- Queries with additions: `200`
- Avg added per query: `2.25`
- Max added: `11`
- Addition reasons:
  - graph_depth_1: `449`

### Expanded Gold Delta (Expanded - Strict)
- Coverage Δ: `0.0000`
- MRR Δ: `0.0102`
- hit@1 Δ: `0.0142`
- hit@3 Δ: `0.0071`
- hit@5 Δ: `0.0071`
- hit@10 Δ: `0.0071`

## Timings (ms)
- Embedding (chunks): `0`
- Embedding (queries): `4281`
- Evaluation (strict): `2057`
- Evaluation (expanded): `2591`
- Total: `15858`

### Timing Estimates (ms)
- Evaluation (strict): `2060`
- Evaluation (expanded): `2140`
- Total: `8481`

## Query Details
### Query 0
- Text: What is the rule about Boosters attached to your armor allow you to fly.?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 268-281::/page/2/Text/28']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 268-281::/page/2/Text/28', 'merged::PZO22001 Starfinder Player Core 268-281::/page/2/Text/29', 'merged::PZO22001 Starfinder Player Core 268-281::/page/2/Text/27']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 268-281::/page/2/Text/29` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 268-281::/page/2/Text/27` (reasons: ['graph_depth_1'])

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
| 9 | `merged::PZO22001 Starfinder Player Core 150-161::/page/8/Text/16` | 0.423357 | **Requirements** You have a force field upgrade in your armor or  are holding a tech shield. |
| 10 | `merged::PZO22001 Starfinder Player Core 150-161::/page/3/Text/17` | 0.422102 | Your endurance training empowers you to carry a load of heavy  equipment. When determining your Strength for using armor,  you can instead choose to use your Constitution modifier. If  you already mee |

### Query 1
- Text: Summarize **Languages** **CLASSES**
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 040-057::/page/1/Text/52']
- Expected found: `True`
- Expected rank: `1`
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
| 2 | `merged::PZO22001 Starfinder Player Core 058-073::/page/3/Text/78` | 0.903496 | **Languages** **CLASSES** |
| 3 | `merged::PZO22001 Starfinder Player Core 058-073::/page/9/Text/44` | 0.903496 | **Languages** **CLASSES** |
| 4 | `merged::PZO22001 Starfinder Player Core 364-387::/page/13/Text/71` | 0.718334 | **CLASSES** |
| 5 | `merged::PZO22001 Starfinder Player Core 210-231::/page/7/Text/63` | 0.718334 | **CLASSES** |
| 6 | `merged::PZO22001 Starfinder Player Core 364-387::/page/11/Text/56` | 0.718334 | **CLASSES** |
| 7 | `merged::PZO22001 Starfinder Player Core 364-387::/page/5/Text/68` | 0.718334 | **CLASSES** |
| 8 | `merged::PZO22001 Starfinder Player Core 364-387::/page/3/Text/56` | 0.718334 | **CLASSES** |
| 9 | `merged::PZO22001 Starfinder Player Core 210-231::/page/5/Text/27` | 0.718334 | **CLASSES** |
| 10 | `merged::PZO22001 Starfinder Player Core 364-387::/page/1/Text/75` | 0.718334 | **CLASSES** |

### Query 2
- Text: Summarize ADDITIONAL DEVELOPMENT
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 001-013::/page/1/SectionHeader/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 001-013::/page/1/SectionHeader/2', 'merged::PZO22001 Starfinder Player Core 001-013::/page/1/Text/3', 'merged::PZO22001 Starfinder Player Core 001-013::/page/1/Text/1']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 001-013::/page/1/Text/3` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 001-013::/page/1/Text/1` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 001-013::/page/1/SectionHeader/2` | 0.933596 | ADDITIONAL DEVELOPMENT |
| 2 | `merged::PZO22001 Starfinder Player Core 174-181::/page/0/SectionHeader/10` | 0.460328 | ADDITIONAL FEATS |
| 3 | `merged::PZO22001 Starfinder Player Core 250-267::/page/15/Text/22` | 0.427694 | Augmentations |
| 4 | `merged::PZO22001 Starfinder Player Core 250-267::/page/17/Text/21` | 0.427694 | Augmentations |
| 5 | `merged::PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/6` | 0.419512 | **ADAPTED AUGMENTATIONS** **FEAT 1** |
| 6 | `merged::PZO22001 Starfinder Player Core 268-281::/page/1/SectionHeader/14` | 0.415361 | **ADAPTIVE ENERGY SHIELDING** **UPGRADE 13** |
| 7 | `merged::PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/714` | 0.413015 | Advanced |
| 8 | `merged::PZO22001 Starfinder Player Core 232-249::/page/16/TableCell/362` | 0.413015 | Advanced |
| 9 | `merged::PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/257` | 0.413015 | Advanced |
| 10 | `merged::PZO22001 Starfinder Player Core 040-057::/page/13/SectionHeader/4` | 0.411646 | **ADAPTIVE ADEPT** **FEAT 5** |

### Query 3
- Text: What is the rule about The illusion can cause damage by making the target believe  the illusion's attacks are real, but it cannot otherwise directly  affect the physical world. If the illusory creature hits with a  Strike, the target takes 3d4 mental damage. The illusion's  Strikes are nonlethal. If the damage doesn't correspond to  the image of the monster—for example, if an illusory Large  dragon deals only 5 damage—the GM might allow the target  to attempt an immediate Perception check to disbelieve the  spell. Any relevant resistances and weaknesses apply if the  target thinks they do, as judged by the GM. For example, if  the illusion wields a doshko and attacks a creature resistant to  piercing damage, the creature would take less mental damage.  However, illusory damage does not deactivate regeneration or  trigger other effects that require a certain damage type. The  GM should track illusory damage dealt by the illusion.?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 330-363::/page/9/Text/4']
- Expected found: `False`
- Expected rank: `None`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 330-363::/page/9/Text/4', 'merged::PZO22001 Starfinder Player Core 330-363::/page/9/Text/3', 'merged::PZO22001 Starfinder Player Core 330-363::/page/9/Text/5']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 330-363::/page/9/Text/3` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 330-363::/page/9/Text/5` (reasons: ['graph_depth_1'])

### Query 4
- Text: Summarize DURING SOCIAL ENCOUNTERS...
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/12']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/12', 'merged::PZO22001 Starfinder Player Core 114-125::/page/1/Text/11', 'merged::PZO22001 Starfinder Player Core 114-125::/page/1/Text/13']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 114-125::/page/1/Text/11` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 114-125::/page/1/Text/13` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/12` | 0.927694 | DURING SOCIAL ENCOUNTERS... |
| 2 | `merged::PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/12` | 0.927694 | DURING SOCIAL ENCOUNTERS... |
| 3 | `merged::PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/14` | 0.927694 | DURING SOCIAL ENCOUNTERS... |
| 4 | `merged::PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/14` | 0.927694 | DURING SOCIAL ENCOUNTERS... |
| 5 | `merged::PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/12` | 0.927694 | DURING SOCIAL ENCOUNTERS... |
| 6 | `merged::PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/14` | 0.927694 | DURING SOCIAL ENCOUNTERS... |
| 7 | `merged::PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/12` | 0.678104 | DURING COMBAT ENCOUNTERS... |
| 8 | `merged::PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/10` | 0.678104 | DURING COMBAT ENCOUNTERS... |
| 9 | `merged::PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/12` | 0.678104 | DURING COMBAT ENCOUNTERS... |
| 10 | `merged::PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/12` | 0.678104 | DURING COMBAT ENCOUNTERS... |

### Query 5
- Text: What is the rule about If something isn't listed in your character's class entry,  their proficiency rank in that statistic is untrained unless  they gain training from another source. If your character  is untrained in something, you add a proficiency bonus of  +0 when attempting a check or calculating a DC related to  that statistic.?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 098-113::/page/2/Text/8']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 098-113::/page/2/Text/8', 'merged::PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/9', 'merged::PZO22001 Starfinder Player Core 098-113::/page/2/Text/7']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/9` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 098-113::/page/2/Text/7` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 098-113::/page/2/Text/8` | 0.952201 | If something isn't listed in your character's class entry,  their proficiency rank in that statistic is untrained unless  they gain training from another source. If your character  is untrained in som |
| 2 | `merged::PZO22001 Starfinder Player Core 098-113::/page/5/Text/50` | 0.719787 | At 1st level, you gain the listed  proficiency ranks in the following  statistics. You are untrained in anything  not listed unless you gain a better  proficiency rank in some other way. |
| 3 | `merged::PZO22001 Starfinder Player Core 126-137::/page/1/Text/49` | 0.719787 | At 1st level, you gain the listed  proficiency ranks in the following  statistics. You are untrained in anything  not listed unless you gain a better  proficiency rank in some other way. |
| 4 | `merged::PZO22001 Starfinder Player Core 098-113::/page/2/Text/6` | 0.692504 | A proficiency rank can unlock various feats and class  features, and it also helps determine the modifier for any  check you roll or DC you calculate related to that statistic.  If your character is t |
| 5 | `merged::PZO22001 Starfinder Player Core 014-029::/page/10/Text/5` | 0.684729 | With most of the big decisions for your character made,  it's time to calculate the modifiers for each of the following  statistics. If your proficiency rank for a statistic is trained,  expert, maste |
| 6 | `merged::PZO22001 Starfinder Player Core 182-209::/page/1/Text/13` | 0.648424 | Anyone can use a skill's untrained actions, but you can  use trained actions only if you have a proficiency rank of  trained or better in that skill. A circumstance, condition, or  effect might bar yo |
| 7 | `merged::PZO22001 Starfinder Player Core 014-029::/page/10/Text/14` | 0.645315 | In the second box to the right of each skill on your character  sheet, there's an abbreviation to remind you of the attribute  modifier for that skill. For each skill in which your character is  train |
| 8 | `merged::PZO22001 Starfinder Player Core 098-113::/page/2/Text/5` | 0.636935 | Each class entry specifies your character's initial  proficiency rank in Perception, saving throws, attacks,  defenses, and class DC. You gain the trained proficiency  rank in several skills. The exac |
| 9 | `merged::PZO22001 Starfinder Player Core 424-441::/page/7/Text/5` | 0.634924 | Thanks to your ally's assistance, you can add your level  as a proficiency bonus to the associated skill check, even if  you're untrained. Additionally, you gain a circumstance bonus  to your skill ch |
| 10 | `merged::PZO22001 Starfinder Player Core 442-464::/page/10/Text/8` | 0.633276 | **proficiency** A measure of a character's aptitude at a specific  task or quality, with five ranks: untrained, trained, expert,  master, and legendary. Proficiency gives a proficiency  bonus. Being u |

### Query 6
- Text: Summarize **Barathu** **Human**
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 092-097::/page/1/Text/48']
- Expected found: `True`
- Expected rank: `6`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 092-097::/page/1/Text/48', 'merged::PZO22001 Starfinder Player Core 092-097::/page/1/Text/49', 'merged::PZO22001 Starfinder Player Core 092-097::/page/1/Text/47']
- Expanded expected found: `True`
- Expanded expected rank: `6`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 092-097::/page/1/Text/49` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 092-097::/page/1/Text/47` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 058-073::/page/9/Text/33` | 0.961021 | **Barathu** **Human** |
| 2 | `merged::PZO22001 Starfinder Player Core 092-097::/page/3/Text/35` | 0.961021 | **Barathu** **Human** |
| 3 | `merged::PZO22001 Starfinder Player Core 058-073::/page/1/Text/32` | 0.961021 | **Barathu** **Human** |
| 4 | `merged::PZO22001 Starfinder Player Core 040-057::/page/11/Text/33` | 0.961021 | **Barathu** **Human** |
| 5 | `merged::PZO22001 Starfinder Player Core 074-091::/page/5/Text/37` | 0.961021 | **Barathu** **Human** |
| 6 | `merged::PZO22001 Starfinder Player Core 092-097::/page/1/Text/48` | 0.961021 | **Barathu** **Human** |
| 7 | `merged::PZO22001 Starfinder Player Core 074-091::/page/7/Text/62` | 0.961021 | **Barathu** **Human** |
| 8 | `merged::PZO22001 Starfinder Player Core 040-057::/page/13/Text/64` | 0.961021 | **Barathu** **Human** |
| 9 | `merged::PZO22001 Starfinder Player Core 058-073::/page/13/Text/33` | 0.961021 | **Barathu** **Human** |
| 10 | `merged::PZO22001 Starfinder Player Core 040-057::/page/3/Text/33` | 0.815271 | **Barathu** |

### Query 7
- Text: What is the rule about Prioritize learning and diplomacy if you're a damaya, or  physique and tactical prowess if you're a korasha—or if  you're an unbound lashunta, you have different priorities.?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 058-073::/page/1/ListItem/3']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 058-073::/page/1/ListItem/3', 'merged::PZO22001 Starfinder Player Core 058-073::/page/1/ListItem/4', 'merged::PZO22001 Starfinder Player Core 058-073::/page/1/ListItem/2']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 058-073::/page/1/ListItem/4` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 058-073::/page/1/ListItem/2` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 058-073::/page/1/ListItem/3` | 0.935610 | Prioritize learning and diplomacy if you're a damaya, or  physique and tactical prowess if you're a korasha—or if  you're an unbound lashunta, you have different priorities. |
| 2 | `merged::PZO22001 Starfinder Player Core 058-073::/page/1/Text/25` | 0.590009 | You've chosen the adaptive genetics to become a damaya. You  might have a leaner, lither body type than other lashuntas and  are likely encouraged to pursue work as a scholar or politician.  In additi |
| 3 | `merged::PZO22001 Starfinder Player Core 058-073::/page/2/Text/31` | 0.519001 | You've studied the lives and achievements of other  lashuntas who have improved both their psychic powers  and their communities. You gain the trained proficiency  rank in Occultism and Society. If yo |
| 4 | `merged::PZO22001 Starfinder Player Core 058-073::/page/1/Text/13` | 0.513964 | Around puberty, lashuntas traditionally choose whether  to express damaya or korasha genetics—a decision that  determines their physical development and influences their  potential societal roles. Las |
| 5 | `merged::PZO22001 Starfinder Player Core 058-073::/page/1/Text/27` | 0.502198 | You've chosen the adaptive genetics to become a korasha. You  might be stockier and more muscular than other lashuntas. |
| 6 | `merged::PZO22001 Starfinder Player Core 058-073::/page/1/Text/12` | 0.500387 | Damayas tend to be tall and graceful with delicate features and  are traditionally pushed toward artistic or intellectual pursuits  and political occupations. Korashas are shorter, more muscular,  and |
| 7 | `merged::PZO22001 Starfinder Player Core 058-073::/page/2/Text/3` | 0.498280 | You decided against activating your ancestry's adaptive  genetics. You might show a combination of damaya and  korasha traits; you might be tall and muscular or short and  lithe, or perhaps you have u |
| 8 | `merged::PZO22001 Starfinder Player Core 058-073::/page/11/Text/4` | 0.493477 | Your ability to adapt to various beliefs instills you with  knowledge of many cultures. You gain the trained proficiency  rank in Diplomacy and Society. If you would automatically  become trained in o |
| 9 | `merged::PZO22001 Starfinder Player Core 058-073::/page/3/Text/8` | 0.492525 | **Prerequisites** korasha lashunta or unbound lashunta heritage You can leverage your telepathic abilities to influence the  minds of others, imparting orders or inflaming fears. You can  cast *comman |
| 10 | `merged::PZO22001 Starfinder Player Core 058-073::/page/14/Text/32` | 0.491286 | You're gregarious and friendly but also passionately  interested in the history of your people, going out of  your way to learn traditional stories and unearth  lost secrets. You gain the trained prof |

### Query 8
- Text: What does **HOWL **[two-actions] **SPELL 7** do?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 330-363::/page/7/Text/32']
- Expected found: `False`
- Expected rank: `None`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 330-363::/page/7/Text/32', 'merged::PZO22001 Starfinder Player Core 330-363::/page/7/Text/21', 'merged::PZO22001 Starfinder Player Core 330-363::/page/7/Text/74']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 330-363::/page/7/Text/21` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 330-363::/page/7/Text/74` (reasons: ['graph_depth_1'])

### Query 9
- Text: What is the rule about HIT POINTS?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 040-057::/page/1/SectionHeader/14']
- Expected found: `False`
- Expected rank: `None`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 040-057::/page/1/SectionHeader/14', 'merged::PZO22001 Starfinder Player Core 040-057::/page/1/Text/13', 'merged::PZO22001 Starfinder Player Core 040-057::/page/1/Text/15']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 040-057::/page/1/Text/13` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 040-057::/page/1/Text/15` (reasons: ['graph_depth_1'])

### Query 10
- Text: What is the rule about Other heightened entries give a number after a plus sign,  indicating that heightening grants extra advantages over  multiple ranks. The listed effect applies for every increment  of ranks by which the spell is heightened above its lowest  spell rank, and the benefit is cumulative. For example, *slice * *reality* says "**Heightened (+1)** The damage increases by 1d8."  Because *slice reality* deals 7d8 void damage at 6th rank, a  7th-rank *slice reality* would deal 8d8 void damage, an 8thrank spell would deal 9d8 void damage, and so on.?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 294-329::/page/2/Text/3']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 294-329::/page/2/Text/3', 'merged::PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/4', 'merged::PZO22001 Starfinder Player Core 294-329::/page/2/Text/2']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/4` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 294-329::/page/2/Text/2` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 294-329::/page/2/Text/3` | 0.959775 | Other heightened entries give a number after a plus sign,  indicating that heightening grants extra advantages over  multiple ranks. The listed effect applies for every increment  of ranks by which th |
| 2 | `merged::PZO22001 Starfinder Player Core 294-329::/page/2/Text/2` | 0.747572 | In addition, many spells have additional specific benefits  when they are heightened, such as increased damage. These  extra benefits are described at the end of the spell's stat  block. Some heighten |
| 3 | `merged::PZO22001 Starfinder Player Core 294-329::/page/7/Text/26` | 0.730649 | **Heightened** (rank) If the spell has special effects when  heightened (page 295), those effects appear at the end  of the stat block. |
| 4 | `merged::PZO22001 Starfinder Player Core 294-329::/page/2/Text/1` | 0.684672 | so long as they know the spell at that rank (see Heightened  Spontaneous Spells below). When you heighten your spell,  the spell's rank increases to match the higher rank of the  spell slot you've pre |
| 5 | `merged::PZO22001 Starfinder Player Core 114-125::/page/3/Text/8` | 0.640869 | When you get spell slots of 2nd rank and higher, you can fill those  slots with stronger versions of lower-rank spells. This increases  the spell's rank to match the spell slot. You must have a spell |
| 6 | `merged::PZO22001 Starfinder Player Core 294-329::/page/1/Text/16` | 0.635081 | Both prepared and spontaneous spellcasters can cast a spell  at a higher spell rank than that listed for the spell. This is  called heightening the spell. A prepared spellcaster can  heighten a spell |
| 7 | `merged::PZO22001 Starfinder Player Core 294-329::/page/29/Text/34` | 0.618107 | **Heightened (+1)** The damage increases by 2d6 (or by 2d8 if  the target is a divine spellcaster). |
| 8 | `merged::PZO22001 Starfinder Player Core 364-387::/page/12/Text/10` | 0.591223 | **Heightened (+1)** The amount of healing increases by 1d6,  and the extra healing for the 2-action version increases  by 6. |
| 9 | `merged::PZO22001 Starfinder Player Core 294-329::/page/32/Text/17` | 0.585027 | **Heightened (+1)** The damage increases by 1d6 and persistent  damage increases by 1d6. |
| 10 | `merged::PZO22001 Starfinder Player Core 114-125::/page/3/Text/14` | 0.577257 | When you gain access to a new rank of spells, your first new  spell is always the spell granted by your chosen connection,  but you can choose the other spells. At 2nd level, you select  another 1st-r |

### Query 11
- Text: What is the rule about actions, you can't use any special abilities, reactions, or free  actions that trigger when you Recall Knowledge.?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 330-363::/page/8/Text/26']
- Expected found: `False`
- Expected rank: `None`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 330-363::/page/8/Text/26', 'merged::PZO22001 Starfinder Player Core 330-363::/page/8/Text/25', 'merged::PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/27']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 330-363::/page/8/Text/25` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/27` (reasons: ['graph_depth_1'])

### Query 12
- Text: Lookup values for Stealth Skill FeatsLevelPrerequisitesBenefitsExperienced Smuggler1Trained in StealthConceal items from observers more effectivelyTerrain Stalker1Trained in StealthSneak in certain terrain without attempting a checkQuiet Allies2Expert in StealthRoll a single Stealth check when sneaking with alliesFoil Senses7Master in StealthTake precautions against special sensesSwift Sneak7Master in StealthMove your full Speed while you SneakLegendary Sneak15Legendary in Stealth, Swift
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 210-231::/page/5/Table/2']
- Expected found: `True`
- Expected rank: `1`
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
| 6 | `merged::PZO22001 Starfinder Player Core 210-231::/page/5/TableCell/544` | 0.646724 | Stealth Skill Feats |
| 7 | `merged::PZO22001 Starfinder Player Core 210-231::/page/5/TableCell/536` | 0.646724 | Stealth Skill Feats |
| 8 | `merged::PZO22001 Starfinder Player Core 210-231::/page/5/Table/4` | 0.644543 | Thievery Skill FeatsLevelPrerequisitesBenefitsPickpocket1Trained in ThieverySteal or Palm an Object more effectivelySubtle Theft1Trained in ThieveryYour thefts are harder to noticeWary Disarmament2Exp |
| 9 | `merged::PZO22001 Starfinder Player Core 092-097::/page/3/Text/17` | 0.629618 | You're trained in the Stealth skill and the Underworld Lore  skill. You gain the Experienced Smuggler skill feat. |
| 10 | `merged::PZO22001 Starfinder Player Core 210-231::/page/5/TableCell/570` | 0.625331 | Legendary in Stealth, Swift Sneak |

### Query 13
- Text: Summarize **CLASSES**
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 030-039::/page/1/Text/34']
- Expected found: `False`
- Expected rank: `None`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 030-039::/page/1/Text/34', 'merged::PZO22001 Starfinder Player Core 030-039::/page/1/Text/35', 'merged::PZO22001 Starfinder Player Core 030-039::/page/9/Text/47', 'merged::PZO22001 Starfinder Player Core 030-039::/page/1/Text/33', 'merged::PZO22001 Starfinder Player Core 030-039::/page/3/Text/37', 'merged::PZO22001 Starfinder Player Core 030-039::/page/7/Text/86', 'merged::PZO22001 Starfinder Player Core 030-039::/page/5/Text/58']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 030-039::/page/1/Text/35` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 030-039::/page/9/Text/47` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 030-039::/page/1/Text/33` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 030-039::/page/3/Text/37` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 030-039::/page/7/Text/86` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 030-039::/page/5/Text/58` (reasons: ['graph_depth_1'])

### Query 14
- Text: Summarize HARDNESS
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 250-267::/page/0/SectionHeader/11']
- Expected found: `True`
- Expected rank: `1`
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
| 4 | `merged::PZO22001 Starfinder Player Core 442-464::/page/6/Text/10` | 0.603868 | **Hardness** A statistic representing an object's durability. 236 **haunt** (trait) A hazard with this trait is a spiritual echo, often  of someone with a tragic death. |
| 5 | `merged::PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/454` | 0.525431 | Toughness |
| 6 | `merged::PZO22001 Starfinder Player Core 250-267::/page/0/Text/12` | 0.508008 | Whenever a shield takes damage, the amount of damage it  takes is reduced by this amount. This number is particularly  relevant for shields because of the Shield Block feat (page  228). The rules for |
| 7 | `merged::PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/13` | 0.481498 | DARKNESS |
| 8 | `merged::PZO22001 Starfinder Player Core 364-387::/page/11/Text/45` | 0.451465 | **Heightened (6th)** The barrier has Hardness 8 and 52 HP. **Heightened (7th)** The barrier has Hardness 8 and 60 HP. **Heightened (8th)** The barrier has Hardness 10 and 68 HP. |
| 9 | `merged::PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/7` | 0.451437 | **Strength** |
| 10 | `merged::PZO22001 Starfinder Player Core 364-387::/page/11/Text/70` | 0.443945 | **Heightened (9th)** The barrier has Hardness 10 and 80 HP. |

### Query 15
- Text: Summarize DURING COMBAT ENCOUNTERS...
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/12']
- Expected found: `True`
- Expected rank: `6`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/12', 'merged::PZO22001 Starfinder Player Core 162-173::/page/1/Text/13', 'merged::PZO22001 Starfinder Player Core 162-173::/page/1/Text/11']
- Expanded expected found: `True`
- Expanded expected rank: `6`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 162-173::/page/1/Text/13` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 162-173::/page/1/Text/11` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/10` | 0.933035 | DURING COMBAT ENCOUNTERS... |
| 2 | `merged::PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/12` | 0.933035 | DURING COMBAT ENCOUNTERS... |
| 3 | `merged::PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/12` | 0.933035 | DURING COMBAT ENCOUNTERS... |
| 4 | `merged::PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/10` | 0.933035 | DURING COMBAT ENCOUNTERS... |
| 5 | `merged::PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/10` | 0.933035 | DURING COMBAT ENCOUNTERS... |
| 6 | `merged::PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/12` | 0.933035 | DURING COMBAT ENCOUNTERS... |
| 7 | `merged::PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/12` | 0.695777 | DURING SOCIAL ENCOUNTERS... |
| 8 | `merged::PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/14` | 0.695777 | DURING SOCIAL ENCOUNTERS... |
| 9 | `merged::PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/14` | 0.695777 | DURING SOCIAL ENCOUNTERS... |
| 10 | `merged::PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/12` | 0.695777 | DURING SOCIAL ENCOUNTERS... |

### Query 16
- Text: What is the rule about CHARACTER CREATION17?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/132']
- Expected found: `False`
- Expected rank: `None`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/132', 'merged::PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/130', 'merged::PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/134']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/130` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/134` (reasons: ['graph_depth_1'])

### Query 17
- Text: Summarize **BASED ON THE DESIGN WORK OF **
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 001-013::/page/1/SectionHeader/22']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 001-013::/page/1/SectionHeader/22', 'merged::PZO22001 Starfinder Player Core 001-013::/page/1/Text/21', 'merged::PZO22001 Starfinder Player Core 001-013::/page/1/Text/23']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 001-013::/page/1/Text/21` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 001-013::/page/1/Text/23` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 001-013::/page/1/SectionHeader/22` | 0.921454 | **BASED ON THE DESIGN WORK OF ** |
| 2 | `merged::PZO22001 Starfinder Player Core 001-013::/page/1/SectionHeader/14` | 0.540955 | **GRAPHIC DESIGN ** |
| 3 | `merged::PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/40` | 0.414352 | **ARCHETYPE** |
| 4 | `merged::PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/12` | 0.414352 | **ARCHETYPE** |
| 5 | `merged::PZO22001 Starfinder Player Core 174-181::/page/6/SectionHeader/23` | 0.414352 | **ARCHETYPE** |
| 6 | `merged::PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/11` | 0.414352 | **ARCHETYPE** |
| 7 | `merged::PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/16` | 0.414352 | **ARCHETYPE** |
| 8 | `merged::PZO22001 Starfinder Player Core 174-181::/page/3/Text/49` | 0.414352 | **ARCHETYPE** |
| 9 | `merged::PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/27` | 0.414352 | **ARCHETYPE** |
| 10 | `merged::PZO22001 Starfinder Player Core 174-181::/page/3/Text/54` | 0.414352 | **ARCHETYPE** |

### Query 18
- Text: What is the rule about An android bounty hunter, pursuing dangerous criminals  and rogue virtual intelligences across the planet.?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/20']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/20', 'merged::PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/19', 'merged::PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/21']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/19` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/21` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/20` | 0.899164 | An android bounty hunter, pursuing dangerous criminals  and rogue virtual intelligences across the planet. |
| 2 | `merged::PZO22001 Starfinder Player Core 442-464::/page/0/Text/40` | 0.461687 | **android** (trait) A creature with this trait is a member of the  android ancestry. Androids are synthetic constructed  beings. An ability with this trait can be used or selected  only by androids. 4 |
| 3 | `merged::PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/3` | 0.454998 | A ghost courier, exploring the Ghost Levels on a hunt  for valuable relics, surviving dangerous anomalies and  fighting dimensionally displaced monsters. |
| 4 | `merged::PZO22001 Starfinder Player Core 092-097::/page/3/Text/11` | 0.433467 | You're a career criminal with a nasty reputation. Perhaps  unfair circumstances forced you into a life of crime, or maybe  you enjoy the thrill you get from pulling off a heist or living  through a sh |
| 5 | `merged::PZO22001 Starfinder Player Core 126-137::/page/8/Text/7` | 0.430450 | Acrobatics, Computers, Stealth, Thievery |
| 6 | `merged::PZO22001 Starfinder Player Core 014-029::/page/13/Text/17` | 0.421317 | Androids are synthetic  constructed beings with varied  shapes and origins. Page 42. |
| 7 | `merged::PZO22001 Starfinder Player Core 364-387::/page/19/Text/17` | 0.418585 | You grant intelligence to the target, transforming it into a  creature with the tech trait with free will. If it was previously  a minion, it can no longer serve as one. The creature is freed  from al |
| 8 | `merged::PZO22001 Starfinder Player Core 092-097::/page/5/Text/22` | 0.418395 | **Android** |
| 9 | `merged::PZO22001 Starfinder Player Core 074-091::/page/15/Text/35` | 0.418394 | **Android** |
| 10 | `merged::PZO22001 Starfinder Player Core 074-091::/page/13/Text/55` | 0.418394 | **Android** |

### Query 19
- Text: What is the rule about You're one among many professionals working in the  corporate world, but you're not just any suit. You're a  negotiator, dealmaker, or perhaps even a spy working to  advance a particular corporation's agenda. You might be a cog  in a corporation's massive machine or a shill for an up-andcoming entrepreneur no one has heard of... yet.?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 092-097::/page/1/Text/28']
- Expected found: `True`
- Expected rank: `1`
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
| 4 | `merged::PZO22001 Starfinder Player Core 126-137::/page/1/Text/13` | 0.550445 | You might fall back on your training, speaking up to give strategic advice to your  allies while remaining alert for strangers' hidden agendas or take the lead about a  subject you know. |
| 5 | `merged::PZO22001 Starfinder Player Core 092-097::/page/1/Text/4` | 0.546687 | You hunt people down for credits. You might work with a  corporation, military, or some other organization. |
| 6 | `merged::PZO22001 Starfinder Player Core 092-097::/page/3/Text/28` | 0.545836 | You work in a lab and conduct research about a scientific  topic. Perhaps you're a biotechnician, chemist, computer  programmer, theoretical physicist, or accomplished  researcher in some other field. |
| 7 | `merged::PZO22001 Starfinder Player Core 092-097::/page/2/Text/30` | 0.535084 | You're a con artist and trickster who swindles unsuspecting  dupes and blackmails rubes, but it's nothing personal you're just in it for the credits. You might run an operation  on the side, or you mi |
| 8 | `merged::PZO22001 Starfinder Player Core 092-097::/page/2/Text/6` | 0.533113 | You're an accomplished healer expertly using the latest tech  and pharmaceuticals to treat your patients. You might work  at a clinic, supervise a starship's medbay, serve as a military  medic, or ply |
| 9 | `merged::PZO22001 Starfinder Player Core 098-113::/page/5/Text/13` | 0.531613 | You're often the face for your team, whether you use diplomacy, lies, threats, or  whatever words it takes to get your way. |
| 10 | `merged::PZO22001 Starfinder Player Core 126-137::/page/2/Text/18` | 0.517391 | You specialize in slipping into a location, completing an  objective, and extricating yourself without being discovered.  You might use stealth tactics, cover identities, disguises, or  spy tech. Whet |

### Query 20
- Text: Summarize **CONDITIONS ** **APPENDIX**
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 092-097::/page/3/Text/47']
- Expected found: `False`
- Expected rank: `None`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 092-097::/page/3/Text/47', 'merged::PZO22001 Starfinder Player Core 092-097::/page/3/Text/53', 'merged::PZO22001 Starfinder Player Core 092-097::/page/5/Text/41', 'merged::PZO22001 Starfinder Player Core 092-097::/page/3/Text/46', 'merged::PZO22001 Starfinder Player Core 092-097::/page/1/Text/64']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 092-097::/page/3/Text/53` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 092-097::/page/5/Text/41` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 092-097::/page/3/Text/46` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 092-097::/page/1/Text/64` (reasons: ['graph_depth_1'])

### Query 21
- Text: What is the rule about Some skill activities have the exploration or downtime trait.  Exploration activities usually take a minute or more, while  downtime activities may take a day or more. They usually  can't be used during an encounter, though the GM might  bend this restriction. If you're not sure whether you have the  time to use one of these activities, ask your GM.?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 182-209::/page/2/Text/12']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 182-209::/page/2/Text/12', 'merged::PZO22001 Starfinder Player Core 182-209::/page/2/SectionHeader/13', 'merged::PZO22001 Starfinder Player Core 182-209::/page/2/SectionHeader/11']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 182-209::/page/2/SectionHeader/13` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 182-209::/page/2/SectionHeader/11` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 182-209::/page/2/Text/12` | 0.968181 | Some skill activities have the exploration or downtime trait.  Exploration activities usually take a minute or more, while  downtime activities may take a day or more. They usually  can't be used duri |
| 2 | `merged::PZO22001 Starfinder Player Core 406-423::/page/0/Text/24` | 0.761334 | Outside of encounters, activities can take minutes, hours, or  even days. These activities usually have the exploration or  downtime trait to indicate they're meant to be used during  these modes of p |
| 3 | `merged::PZO22001 Starfinder Player Core 424-441::/page/9/Text/3` | 0.644289 | Downtime gives you time to rest fully, engage in crafting  or a professional endeavor, learn new spells, retrain feats,  or just have fun. You can sell items acquired during your  adventures, buy new |
| 4 | `merged::PZO22001 Starfinder Player Core 442-464::/page/5/Text/1` | 0.642743 | **exploration** (trait) Activities with this trait take more  than a turn to use and can usually be used only during  exploration mode. |
| 5 | `merged::PZO22001 Starfinder Player Core 388-405::/page/1/Text/5` | 0.639455 | In **exploration mode**, time is more flexible and the play  more free-form. Minutes, hours, or even days in the game  world pass quickly in the real world, as the characters travel  between star syst |
| 6 | `merged::PZO22001 Starfinder Player Core 424-441::/page/4/Text/24` | 0.629949 | Activities that take longer than a turn can't normally be  performed during an encounter. Spells with a casting time of  1 minute or more are a common example, as are several skill  actions. When you |
| 7 | `merged::PZO22001 Starfinder Player Core 182-209::/page/26/Text/38` | 0.628883 | In some cases, you might Track in an encounter. In this  case, Track is a single action and doesn't have the exploration  trait, but you might need to roll more often because you're  in a tense situat |
| 8 | `merged::PZO22001 Starfinder Player Core 182-209::/page/4/Text/24` | 0.623377 | You can use a skill to earn money during downtime. You must be  trained in the skill to do so. This takes time to set up, and your  income depends on your proficiency rank and how lucrative a  task yo |
| 9 | `merged::PZO22001 Starfinder Player Core 442-464::/page/0/Text/20` | 0.622186 | **activity** A category of action that typically takes more than  a single action. Activities on your turn take 2 actions ([two-actions])  or 3 actions ([three-actions]). Exploration and downtime acti |
| 10 | `merged::PZO22001 Starfinder Player Core 182-209::/page/3/Footnote/3` | 0.611041 | D This skill action is used during downtime. |

### Query 22
- Text: Summarize —
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/653']
- Expected found: `False`
- Expected rank: `None`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/653', 'merged::PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/652', 'merged::PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/654']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/652` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/654` (reasons: ['graph_depth_1'])

### Query 23
- Text: Summarize **COVER ARTIST **
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 001-013::/page/1/SectionHeader/8']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 001-013::/page/1/SectionHeader/8', 'merged::PZO22001 Starfinder Player Core 001-013::/page/1/Text/9', 'merged::PZO22001 Starfinder Player Core 001-013::/page/1/Text/7']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 001-013::/page/1/Text/9` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 001-013::/page/1/Text/7` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 001-013::/page/1/SectionHeader/8` | 0.946466 | **COVER ARTIST ** |
| 2 | `merged::PZO22001 Starfinder Player Core 182-209::/page/26/SectionHeader/31` | 0.561121 | **COVER TRACKS** |
| 3 | `merged::PZO22001 Starfinder Player Core 092-097::/page/0/SectionHeader/6` | 0.544501 | **ARTIST** **BACKGROUND** |
| 4 | `merged::PZO22001 Starfinder Player Core 001-013::/page/1/SectionHeader/10` | 0.520684 | **INTERIOR ARTISTS ** |
| 5 | `merged::PZO22001 Starfinder Player Core 442-464::/page/13/Text/21` | 0.480595 | **Take Cover **[one-action] (basic action) Gain cover, or improve cover to  greater cover. 410 |
| 6 | `merged::PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/575` | 0.464273 | Covering Fire |
| 7 | `merged::PZO22001 Starfinder Player Core 001-013::/page/12/TableCell/466` | 0.459536 | For my third action, I Take Cover behind a |
| 8 | `merged::PZO22001 Starfinder Player Core 442-464::/page/3/Text/9` | 0.451230 | **Cover Tracks** (skill action) Conceal your trail during  exploration. (Survival, trained) 208 |
| 9 | `merged::PZO22001 Starfinder Player Core 150-161::/page/7/SectionHeader/5` | 0.450864 | **COVERING FIRE **[one-action]** OR **[two-actions] **FEAT 6** |
| 10 | `merged::PZO22001 Starfinder Player Core 442-464::/page/3/Text/8` | 0.444159 | Take Cover [one-action] (basic action) 410 |

### Query 24
- Text: What is the rule about Your character starts with 150 credits.?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 232-249::/page/1/Text/14']
- Expected found: `True`
- Expected rank: `1`
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
| 3 | `merged::PZO22001 Starfinder Player Core 182-209::/page/5/TableCell/668` | 0.626215 | 150 credits |
| 4 | `merged::PZO22001 Starfinder Player Core 182-209::/page/5/TableCell/672` | 0.626215 | 150 credits |
| 5 | `merged::PZO22001 Starfinder Player Core 182-209::/page/5/TableCell/689` | 0.626215 | 150 credits |
| 6 | `merged::PZO22001 Starfinder Player Core 182-209::/page/5/TableCell/667` | 0.626215 | 150 credits |
| 7 | `merged::PZO22001 Starfinder Player Core 232-249::/page/1/Text/6` | 0.553037 | Your character starts out with 150 credits to spend on any  common items from this chapter. Credits are a galactic  currency used to barter and trade for goods in the Starfinder  setting. Items with a |
| 8 | `merged::PZO22001 Starfinder Player Core 182-209::/page/5/TableCell/623` | 0.489673 | 15 credits |
| 9 | `merged::PZO22001 Starfinder Player Core 182-209::/page/5/TableCell/670` | 0.489673 | 15 credits |
| 10 | `merged::PZO22001 Starfinder Player Core 182-209::/page/5/TableCell/661` | 0.486684 | 100 credits |

### Query 25
- Text: What are the requirements for **OVERCOME SHAME **[free-action] **FEAT 13**?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 074-091::/page/3/SectionHeader/48']
- Expected found: `False`
- Expected rank: `None`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 074-091::/page/3/SectionHeader/48', 'merged::PZO22001 Starfinder Player Core 074-091::/page/3/Text/47', 'merged::PZO22001 Starfinder Player Core 074-091::/page/3/Text/50']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 074-091::/page/3/Text/47` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 074-091::/page/3/Text/50` (reasons: ['graph_depth_1'])

### Query 26
- Text: What is the rule about **SKILLS**?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 330-363::/page/1/Text/64']
- Expected found: `False`
- Expected rank: `None`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 330-363::/page/1/Text/64', 'merged::PZO22001 Starfinder Player Core 330-363::/page/1/Text/63', 'merged::PZO22001 Starfinder Player Core 330-363::/page/1/Text/65']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 330-363::/page/1/Text/63` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 330-363::/page/1/Text/65` (reasons: ['graph_depth_1'])

### Query 27
- Text: What is the rule about This nacreous, tapered cylinder provides a breath of air  when you need it most. You can hold your breath for twice  as long, and you gain a +1 item bonus to saves against  inhaled poisons.?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 282-293::/page/1/Text/8']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 282-293::/page/1/Text/8', 'merged::PZO22001 Starfinder Player Core 282-293::/page/1/Text/9', 'merged::PZO22001 Starfinder Player Core 282-293::/page/1/SectionHeader/7']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 282-293::/page/1/Text/9` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 282-293::/page/1/SectionHeader/7` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 282-293::/page/1/Text/8` | 0.927823 | This nacreous, tapered cylinder provides a breath of air  when you need it most. You can hold your breath for twice  as long, and you gain a +1 item bonus to saves against  inhaled poisons. |
| 2 | `merged::PZO22001 Starfinder Player Core 424-441::/page/5/Text/31` | 0.561974 | You can hold your breath for a number of rounds equal to 5  + your Constitution modifier. Reduce your remaining air by 1  round at the end of each of your turns, or by 2 if you attacked  or cast any s |
| 3 | `merged::PZO22001 Starfinder Player Core 442-464::/page/6/Text/52` | 0.471869 | **inhaled** (trait) A poison with this trait is delivered when  breathed in. |
| 4 | `merged::PZO22001 Starfinder Player Core 364-387::/page/4/SectionHeader/15` | 0.465416 | **TOXIC CLOUD **[three-actions] **SPELL 5**  **CONCENTRATE** **DEATH** **MANIPULATE** **POISON**  **Traditions** arcane, primal  **Range **120 feet;** Area** 20-foot burst  **Defense** basic Fortitude |
| 5 | `merged::PZO22001 Starfinder Player Core 268-281::/page/13/Text/19` | 0.459556 | This grenade unleashes a cloud of concealing smoke in  the radius. Creatures within the area have the concealed  condition, and all other creatures are concealed to them.  The smoke lasts for 1 minute |
| 6 | `merged::PZO22001 Starfinder Player Core 268-281::/page/0/Text/27` | 0.455223 | You gain a +1 status bonus to Fortitude saves against  inhaled effects. |
| 7 | `merged::PZO22001 Starfinder Player Core 424-441::/page/5/Text/32` | 0.441389 | When you run out of air, you fall unconscious and start  suffocating. You can't recover from being unconscious and  must attempt a DC 20 Fortitude save at the end of each of  your turns. On a failure, |
| 8 | `merged::PZO22001 Starfinder Player Core 282-293::/page/10/Text/36` | 0.428958 | This extra organ assimilates with and enhances your circulatory  and immune systems. When you succeed at a Fortitude save  against an ongoing disease or poison, you recover completely,  regardless of |
| 9 | `merged::PZO22001 Starfinder Player Core 364-387::/page/5/SectionHeader/37` | 0.420617 | **VAPOR FORM **[two-actions] **SPELL 4**  **AIR** **CONCENTRATE** **MANIPULATE** **POLYMORPH**  **Traditions** arcane, occult, primal  **Range **touch;** Targets** 1 willing creature  **Duration** 5 m |
| 10 | `merged::PZO22001 Starfinder Player Core 150-161::/page/9/Text/10` | 0.420009 | You hold down the trigger and push your weapons to their  absolute limits with a ceaseless barrage of firepower. Area Fire  twice with the required weapon, ignoring the unwieldy trait  of your weapon. |

### Query 28
- Text: What does **CHARM **[two-actions] **SPELL 1** do?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/52']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/52', 'merged::PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/44', 'merged::PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/6']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/44` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/6` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/52` | 0.601221 | **CHARM **[two-actions] **SPELL 1**  **CONCENTRATE** **EMOTION** **INCAPACITATION** **MANIPULATE** **MENTAL** **SUBTLE**  **Traditions** arcane, occult, primal **Range **30 feet;** Targets** 1 creatur |
| 2 | `merged::PZO22001 Starfinder Player Core 294-329::/page/7/Text/19` | 0.596610 | **SPELL NAME **[one-action] **SPELL (RANK)** |
| 3 | `merged::PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/15` | 0.559701 | **REACH SPELL **[one-action] **FEAT 1** |
| 4 | `merged::PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/34` | 0.542399 | **CONCEAL SPELL **[one-action] **FEAT 2** |
| 5 | `merged::PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/25` | 0.518547 | **WIDEN SPELL **[one-action] **FEAT 1** |
| 6 | `merged::PZO22001 Starfinder Player Core 162-173::/page/9/Text/2` | 0.517310 | **NONLETHAL SPELL **[one-action] **FEAT 2** |
| 7 | `merged::PZO22001 Starfinder Player Core 162-173::/page/7/SectionHeader/27` | 0.515232 | **OTHERWORLDLY SPELL **[one-action] **FEAT 1** |
| 8 | `merged::PZO22001 Starfinder Player Core 330-363::/page/7/Text/32` | 0.502645 | **HOWL **[two-actions] **SPELL 7**  **AUDITORY** **CONCENTRATE** **MANIPULATE** **MENTAL** **SONIC** |
| 9 | `merged::PZO22001 Starfinder Player Core 182-209::/page/7/SectionHeader/5` | 0.500381 | **LEARN A SPELL** |
| 10 | `merged::PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/25` | 0.494487 | **STELLAR RUSH **[two-actions] **FEAT 1** |

### Query 29
- Text: Lookup values for Society Skill FeatsLevelPrerequisitesBenefitsMultilingual1Trained in SocietyLearn two new languagesPlant Rumor1Trained in SocietyArgue by damaging reputationRead Lips1Trained in SocietyRead the lips of people you can seeSign Language1Trained in SocietyLearn sign languagesStreetwise1Trained in SocietyUse Society to Gather Information and Recall KnowledgeLegendary Codebreaker15Legendary in SocietyQuickly Decipher Writing using SocietyLegendary Linguist15Legendary in Society,
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 210-231::/page/5/Table/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 210-231::/page/5/Table/1', 'merged::PZO22001 Starfinder Player Core 210-231::/page/5/TableCell/504', 'merged::PZO22001 Starfinder Player Core 210-231::/page/5/SectionHeader/0']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 210-231::/page/5/TableCell/504` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 210-231::/page/5/SectionHeader/0` (reasons: ['graph_depth_1'])

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
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/51', 'merged::PZO22001 Starfinder Player Core 150-161::/page/10/Text/53', 'merged::PZO22001 Starfinder Player Core 150-161::/page/10/Text/50']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 150-161::/page/10/Text/53` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 150-161::/page/10/Text/50` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/51` | 0.854073 | **SOLDIER'S TRAINING** **FEAT 16** |
| 2 | `merged::PZO22001 Starfinder Player Core 174-181::/page/5/SectionHeader/25` | 0.687318 | **ADVANCED SOLDIER TRAINING** **FEAT 6** |
| 3 | `merged::PZO22001 Starfinder Player Core 174-181::/page/5/SectionHeader/15` | 0.657032 | **BASIC SOLDIER TRAINING** **FEAT 4** |
| 4 | `merged::PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/637` | 0.625061 | Soldier's Training |
| 5 | `merged::PZO22001 Starfinder Player Core 174-181::/page/5/Text/28` | 0.614301 | **Prerequisites** Basic Soldier Training |
| 6 | `merged::PZO22001 Starfinder Player Core 150-161::/page/7/SectionHeader/1` | 0.540927 | **SOLDIER FEATS BY NAME** |
| 7 | `merged::PZO22001 Starfinder Player Core 210-231::/page/18/Text/11` | 0.538490 | **SKILL TRAINING** **FEAT 1** |
| 8 | `merged::PZO22001 Starfinder Player Core 174-181::/page/5/SectionHeader/41` | 0.530962 | **SOLDIER'S TOUGHNESS** **FEAT 12** |
| 9 | `merged::PZO22001 Starfinder Player Core 150-161::/page/8/Text/32` | 0.529962 | **SOLDIER** |
| 10 | `merged::PZO22001 Starfinder Player Core 150-161::/page/11/Text/19` | 0.529962 | **SOLDIER** |

### Query 31
- Text: What is the rule about You're trained in the Crafting skill and the Augmentation  Lore skill. You gain the Augmented Body feat.?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 092-097::/page/1/Text/35']
- Expected found: `True`
- Expected rank: `1`
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
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 162-173::/page/9/SectionHeader/19', 'merged::PZO22001 Starfinder Player Core 162-173::/page/9/Text/21', 'merged::PZO22001 Starfinder Player Core 162-173::/page/9/Text/18']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 162-173::/page/9/Text/21` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 162-173::/page/9/Text/18` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 162-173::/page/9/SectionHeader/19` | 0.827632 | **WARP WOUNDS **[reaction] **FEAT 2** |
| 2 | `merged::PZO22001 Starfinder Player Core 364-387::/page/15/SectionHeader/2` | 0.550094 | **WARP PRESENCE **[reaction] **FOCUS 1** |
| 3 | `merged::PZO22001 Starfinder Player Core 174-181::/page/6/SectionHeader/5` | 0.533596 | **WITCHWARPER DEDICATION** **FEAT 2** |
| 4 | `merged::PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/600` | 0.529417 | Warp Wounds |
| 5 | `merged::PZO22001 Starfinder Player Core 364-387::/page/13/SectionHeader/58` | 0.522643 | **WARP PROBABILITY **[reaction] **FOCUS 1** |
| 6 | `merged::PZO22001 Starfinder Player Core 442-464::/page/13/Text/45` | 0.500909 | **Treat Wounds** (skill action) Restore Hit Points to a creature.  (Medicine, trained) 202 |
| 7 | `merged::PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/38` | 0.500520 | **FUNDAMENTAL UNDERSTANDING **[reaction] **FEAT 2** |
| 8 | `merged::PZO22001 Starfinder Player Core 098-113::/page/10/Text/41` | 0.491019 | **WATCH OUT **[reaction] **FEAT 1** |
| 9 | `merged::PZO22001 Starfinder Player Core 126-137::/page/6/SectionHeader/42` | 0.484193 | **BLOODY WOUNDS** **FEAT 4** |
| 10 | `merged::PZO22001 Starfinder Player Core 364-387::/page/14/SectionHeader/17` | 0.480553 | **WARP WORLD **[two-actions] **FOCUS 4** |

### Query 33
- Text: What is the rule about If you have access to the Shield Block reaction (from your  class or from a feat), you can use it while Raising your Shield  to reduce the damage you take by an amount equal to the  shield's Hardness. Both you and the shield then take any  remaining damage.?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 250-267::/page/0/Text/6']
- Expected found: `True`
- Expected rank: `1`
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
| 4 | `merged::PZO22001 Starfinder Player Core 138-149::/page/5/Text/19` | 0.681725 | While the shield is raised, you can use the Shield Block  reaction (page 228) with your shield. The shield has Hit Points  equal to 5 plus twice your level and Hardness equal to half  your level, roun |
| 5 | `merged::PZO22001 Starfinder Player Core 250-267::/page/0/Text/2` | 0.669696 | A shield can increase your character's defense beyond the protection their armor provides. Your  character must be wielding a shield in one hand to make use of it, and it grants its bonus to AC only |
| 6 | `merged::PZO22001 Starfinder Player Core 406-423::/page/5/Text/38` | 0.630447 | You position your shield to protect yourself. When you've  Raised a Shield, you gain its listed circumstance bonus to AC.  Your shield remains raised until the start of your next turn. |
| 7 | `merged::PZO22001 Starfinder Player Core 250-267::/page/1/Text/8` | 0.627323 | bonus to your AC, the shield upgrade emits an inertial  dampening barrier, and you automatically Raise a Shield.  You can't Raise a Shield installed as a weapon upgrade any  other way. If you use the |
| 8 | `merged::PZO22001 Starfinder Player Core 250-267::/page/0/Text/4` | 0.616303 | Raise a Shield is the action most commonly used with shields.  Most shields must be held in one hand, so you can't hold  anything with that hand and Raise a Shield, and you lose its  benefits if that |
| 9 | `merged::PZO22001 Starfinder Player Core 250-267::/page/0/Text/10` | 0.611484 | A shield grants a circumstance bonus to AC, but only when  the shield is raised. This requires using the Raise a Shield  action, found on page 411. |
| 10 | `merged::PZO22001 Starfinder Player Core 138-149::/page/9/Text/16` | 0.598874 | Your solar shield acts as an anchor for your mind as much as  your body. When your Raise your solar Shield, you gain the  shield's circumstance bonus to Will saves. In addition, while  you have your s |

### Query 34
- Text: Summarize Assume you view the universe through the lens of your connection.
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 114-125::/page/1/ListItem/25']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 114-125::/page/1/ListItem/25', 'merged::PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/26', 'merged::PZO22001 Starfinder Player Core 114-125::/page/1/ListItem/24']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/26` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 114-125::/page/1/ListItem/24` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 114-125::/page/1/ListItem/25` | 0.974264 | Assume you view the universe through the lens of your connection. |
| 2 | `merged::PZO22001 Starfinder Player Core 114-125::/page/10/Text/8` | 0.632058 | You see into the truth of the cosmos through your connection. You gain the greater epiphany spell for your chosen connection. |
| 3 | `merged::PZO22001 Starfinder Player Core 114-125::/page/5/Text/7` | 0.594081 | You discover the ultimate truth of your connection and its  role as a foundation of the cosmos. You learn your chosen  connection's perfect harmony. |
| 4 | `merged::PZO22001 Starfinder Player Core 114-125::/page/1/ListItem/20` | 0.591157 | Have insights into the nature of your connection that others find unorthodox. |
| 5 | `merged::PZO22001 Starfinder Player Core 114-125::/page/9/Text/35` | 0.548875 | Through dedication or serendipity, you've branched out to  explore other connections to the fundamental building blocks of  the cosmos. You learn the initial epiphany spell of a connection  that grant |
| 6 | `merged::PZO22001 Starfinder Player Core 114-125::/page/9/Text/44` | 0.546371 | You gain a deeper understanding of your connection. You gain  the advanced epiphany spell for your chosen connection. |
| 7 | `merged::PZO22001 Starfinder Player Core 114-125::/page/11/Text/7` | 0.545393 | Plumbing the depths of your own connection, you  understand how your piece of reality interconnects  with another. You learn the advanced epiphany spell of  the connection that grants training in the |
| 8 | `merged::PZO22001 Starfinder Player Core 114-125::/page/1/Text/2` | 0.544398 | You're a conduit, channeling the fundamental forces that connect and bind everything in the cosmos.  You can draw upon this supernatural wellspring to form deep spiritual bonds with your allies,  empo |
| 9 | `merged::PZO22001 Starfinder Player Core 114-125::/page/1/Text/13` | 0.518335 | Your connection shapes your perspective on the world and the way you approach  problems. When a disagreement erupts between bonded members, you're often the  one to help them talk through their proble |
| 10 | `merged::PZO22001 Starfinder Player Core 114-125::/page/5/Text/11` | 0.514653 | Your connection is a mystical force that grants you magic. It  could come from a divine patron, manifestation of a primeval  cosmic force, or some other mystery. Your connection  determines your spell |

### Query 35
- Text: What is the rule about You have to spend all the actions of an activity at once  to gain its effects. In an encounter, this means you must  complete it during your turn. If an activity gets interrupted or  disrupted in an encounter (page 407), you lose all the actions  you committed to it.?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 406-423::/page/0/Text/22']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 406-423::/page/0/Text/22', 'merged::PZO22001 Starfinder Player Core 406-423::/page/0/SectionHeader/23', 'merged::PZO22001 Starfinder Player Core 406-423::/page/0/Text/21']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 406-423::/page/0/SectionHeader/23` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 406-423::/page/0/Text/21` (reasons: ['graph_depth_1'])

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
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 442-464::/page/1/Text/15', 'merged::PZO22001 Starfinder Player Core 442-464::/page/1/Text/17', 'merged::PZO22001 Starfinder Player Core 442-464::/page/1/Text/14']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 442-464::/page/1/Text/17` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 442-464::/page/1/Text/14` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 442-464::/page/1/Text/15` | 0.891258 | multiple attack penalty (–5 on your second attack, –10 on  further attacks) 394 |
| 2 | `merged::PZO22001 Starfinder Player Core 442-464::/page/9/Text/18` | 0.818736 | multiple attack penalty (–5 on your second attack, –10 on  further attacks) 253, **394** |
| 3 | `merged::PZO22001 Starfinder Player Core 442-464::/page/8/Text/32` | 0.760087 | **multiple attack penalty** You take this penalty on all attacks  after the first on your turn. This is a –5 penalty on your  second attack and –10 on all subsequent attacks (or –4 and  –8 if your wea |
| 4 | `merged::PZO22001 Starfinder Player Core 250-267::/page/3/Text/9` | 0.723749 | If you use an action with the attack trait more than once  on the same turn, your attacks after the first take a penalty  called a multiple attack penalty. Your second attack  takes a –5 penalty, and |
| 5 | `merged::PZO22001 Starfinder Player Core 126-137::/page/5/Text/21` | 0.656267 | You unleash a devastating barrage of attacks upon your  mark. Your multiple attack penalty for attacks against your  mark is –3 (–2 with an agile weapon) on your second attack  of the turn instead of |
| 6 | `merged::PZO22001 Starfinder Player Core 250-267::/page/5/Text/13` | 0.635693 | **Agile:** The multiple attack penalty you take with this weapon  on the second attack on your turn is –4 instead of –5, and –8  instead of –10 on the third and subsequent attacks in the turn. |
| 7 | `merged::PZO22001 Starfinder Player Core 150-161::/page/6/Text/29` | 0.603933 | You overwhelm the defenses of suppressed foes. Your  multiple attack penalty for attacks against suppressed  targets is –4 (–3 with an agile weapon) on your second  attack of the turn instead of –5, a |
| 8 | `merged::PZO22001 Starfinder Player Core 250-267::/page/3/Text/10` | 0.600055 | The multiple attack penalty doesn't apply to attacks you  make when it isn't your turn (such as attacks made as part of  a reaction). You can use a weapon with the agile trait (page  255) to reduce yo |
| 9 | `merged::PZO22001 Starfinder Player Core 442-464::/page/1/Text/18` | 0.587316 | spell attack 394–395 |
| 10 | `merged::PZO22001 Starfinder Player Core 442-464::/page/12/Text/56` | 0.581050 | attack rolls 394–395 |

### Query 37
- Text: What is the rule about Armor Class Shiel?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Character Sheet::/page/0/TableCell/53']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Character Sheet::/page/0/TableCell/53', 'merged::PZO22001 Starfinder Character Sheet::/page/0/TableCell/54', 'merged::PZO22001 Starfinder Character Sheet::/page/0/TableCell/52']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Character Sheet::/page/0/TableCell/54` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Character Sheet::/page/0/TableCell/52` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Character Sheet::/page/0/TableCell/53` | 0.840954 | Armor Class Shiel |
| 2 | `merged::PZO22001 Starfinder Player Core 014-029::/page/9/Text/19` | 0.456400 | weapons, and other basic equipment. Your character's class  lists the types of weapons and armor with which they are  trained (or better!). Their weapons determine how much  damage they deal in combat |
| 3 | `merged::PZO22001 Starfinder Player Core 174-181::/page/5/Text/14` | 0.436280 | You become trained in light armor and medium armor. If  you already were trained in light armor and medium armor,  you gain training in heavy armor as well. Whenever you gain  a class feature that gra |
| 4 | `merged::PZO22001 Starfinder Player Core 014-029::/page/11/Text/23` | 0.430739 | Your character's Armor Class represents how difficult they  are to hit in combat. To calculate your AC, add 10 plus your  character's Dexterity modifier (up to their armor's Dexterity  modifier cap; p |
| 5 | `merged::PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/409` | 0.426557 | Become trained in a type of armor |
| 6 | `merged::PZO22001 Starfinder Player Core 210-231::/page/6/Text/24` | 0.421777 | You become trained in light armor. If you already were trained  in light armor, you gain training in medium armor. If you were  trained in both, you become trained in heavy armor. If you are  at least |
| 7 | `merged::PZO22001 Starfinder Player Core 014-029::/page/0/Text/8` | 0.418981 | This chapter contains the rules for 8 classes. Each class  entry includes guidelines on playing the class, rules for  building and advancing a character of that class, sample  builds, and all of the c |
| 8 | `merged::PZO22001 Starfinder Player Core 268-281::/page/9/Text/33` | 0.410882 | **Weapons** **Armor ** |
| 9 | `merged::PZO22001 Starfinder Player Core 268-281::/page/13/Text/49` | 0.410882 | **Weapons** **Armor ** |
| 10 | `merged::PZO22001 Starfinder Player Core 250-267::/page/0/Text/8` | 0.410774 | Shields have statistics that follow the same rules as armor:  Price, Speed Penalty, and Bulk. See page 245 for the rules  for those statistics. Their other statistics are described here. |

### Query 38
- Text: Summarize **PLAYING THE ** **GAME**
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 364-387::/page/3/Text/64']
- Expected found: `True`
- Expected rank: `53`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 364-387::/page/3/Text/64', 'merged::PZO22001 Starfinder Player Core 364-387::/page/3/Text/65', 'merged::PZO22001 Starfinder Player Core 364-387::/page/3/Text/63']
- Expanded expected found: `True`
- Expanded expected rank: `53`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 364-387::/page/3/Text/65` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 364-387::/page/3/Text/63` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 388-405::/page/5/Text/23` | 0.915000 | **PLAYING THE ** **GAME** |
| 2 | `merged::PZO22001 Starfinder Player Core 442-464::/page/7/Text/66` | 0.915000 | **PLAYING THE ** **GAME** |
| 3 | `merged::PZO22001 Starfinder Player Core 406-423::/page/5/Text/53` | 0.915000 | **PLAYING THE ** **GAME** |
| 4 | `merged::PZO22001 Starfinder Player Core 406-423::/page/1/Text/28` | 0.915000 | **PLAYING THE ** **GAME** |
| 5 | `merged::PZO22001 Starfinder Player Core 030-039::/page/7/Text/91` | 0.915000 | **PLAYING THE ** **GAME** |
| 6 | `merged::PZO22001 Starfinder Player Core 268-281::/page/13/Text/57` | 0.915000 | **PLAYING THE ** **GAME** |
| 7 | `merged::PZO22001 Starfinder Player Core 268-281::/page/7/Text/46` | 0.915000 | **PLAYING THE ** **GAME** |
| 8 | `merged::PZO22001 Starfinder Player Core 098-113::/page/9/Text/51` | 0.915000 | **PLAYING THE ** **GAME** |
| 9 | `merged::PZO22001 Starfinder Player Core 442-464::/page/13/Text/60` | 0.915000 | **PLAYING THE ** **GAME** |
| 10 | `merged::PZO22001 Starfinder Player Core 098-113::/page/11/Text/39` | 0.915000 | **PLAYING THE ** **GAME** |

### Query 39
- Text: What is the rule about There are four types of actions: single actions, activities,  reactions, and free actions.?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 406-423::/page/0/Text/7']
- Expected found: `True`
- Expected rank: `1`
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
| 2 | `merged::PZO22001 Starfinder Player Core 014-029::/page/2/Text/3` | 0.644609 | Activities that use two actions use this symbol: [two-actions].  Meanwhile, activities that use three actions use this  symbol: [three-actions]. There are also special activities, such as  spells you |
| 3 | `merged::PZO22001 Starfinder Player Core 424-441::/page/3/Text/19` | 0.640853 | When it's your turn to act, you can use single actions ([one-action]),  short activities ([two-actions] and [three-actions]), reactions ([reaction]), and free actions  ([free-action]). When you're fin |
| 4 | `merged::PZO22001 Starfinder Player Core 406-423::/page/1/Text/11` | 0.625964 | These rules clarify some of the specifics of using actions. |
| 5 | `merged::PZO22001 Starfinder Player Core 406-423::/page/0/Text/20` | 0.614541 | An activity typically involves using multiple actions to create  an effect greater than you can produce with a single action,  or combining multiple single actions to produce an effect  that's differe |
| 6 | `merged::PZO22001 Starfinder Player Core 424-441::/page/4/Text/14` | 0.606931 | you from acting. If you can't act, you can't use any actions,  including reactions and free actions. |
| 7 | `merged::PZO22001 Starfinder Player Core 014-029::/page/1/Text/16` | 0.604542 | Activities are special tasks that you complete by spending  one or more of your actions together. Usually, an activity  uses two or more actions and lets you do more than a |
| 8 | `merged::PZO22001 Starfinder Player Core 014-029::/page/1/Text/14` | 0.597745 | Free actions use this symbol: [free-action]. Free actions don't require  you to spend any of your three single actions or your reaction.  A free action might have a trigger like a reaction does. If so |
| 9 | `merged::PZO22001 Starfinder Player Core 442-464::/page/15/TableCell/234` | 0.588722 | ◆➤➤ Three-Action Activity ◆ Free Action |
| 10 | `merged::PZO22001 Starfinder Player Core 442-464::/page/17/TableCell/309` | 0.582239 | Free Actions and Reactions |

### Query 40
- Text: What are the requirements for **Prerequisites** limited telepathy?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 058-073::/page/3/Text/21']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 058-073::/page/3/Text/21', 'merged::PZO22001 Starfinder Player Core 058-073::/page/3/Text/22', 'merged::PZO22001 Starfinder Player Core 058-073::/page/3/Text/20']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 058-073::/page/3/Text/22` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 058-073::/page/3/Text/20` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 058-073::/page/3/Text/21` | 0.895401 | **Prerequisites** limited telepathy |
| 2 | `merged::PZO22001 Starfinder Player Core 058-073::/page/2/Text/25` | 0.895401 | **Prerequisites** limited telepathy |
| 3 | `merged::PZO22001 Starfinder Player Core 058-073::/page/11/Text/23` | 0.895401 | **Prerequisites** limited telepathy |
| 4 | `merged::PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/22` | 0.895401 | **Prerequisites** limited telepathy |
| 5 | `merged::PZO22001 Starfinder Player Core 058-073::/page/0/SectionHeader/12` | 0.610754 | LIMITED TELEPATHY |
| 6 | `merged::PZO22001 Starfinder Player Core 058-073::/page/8/SectionHeader/14` | 0.610754 | LIMITED TELEPATHY |
| 7 | `merged::PZO22001 Starfinder Player Core 058-073::/page/2/Text/26` | 0.549906 | Whether through training or innate talent, you've expanded  the range at which you can telepathically communicate.  Increase the range of your limited telepathy by 15 feet. |
| 8 | `merged::PZO22001 Starfinder Player Core 058-073::/page/10/Text/23` | 0.549906 | Whether through training or innate talent,  you've expanded the range at which you can  telepathically communicate. Increase the range of  your limited telepathy by 15 feet. |
| 9 | `merged::PZO22001 Starfinder Player Core 058-073::/page/9/Text/25` | 0.544556 | Your telepathy is stronger than most shirrens', allowing you to  combine physical, verbal, and telepathic communication. You  can transmit emotions alongside your messages whenever  you use limited te |
| 10 | `merged::PZO22001 Starfinder Player Core 250-267::/page/8/Text/9` | 0.526646 | **Thought:** Weapons with this trait are bioengineered with  neuroreceptors allowing them to be controlled with telepathy.  When you wield this weapon and have limited telepathy or  telepathy, you can |

### Query 41
- Text: What does **BLINDNESS **[two-actions] **SPELL 3** do?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/36']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/36', 'merged::PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/47', 'merged::PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/29']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/47` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/29` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 294-329::/page/7/Text/19` | 0.615801 | **SPELL NAME **[one-action] **SPELL (RANK)** |
| 2 | `merged::PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/36` | 0.607003 | **BLINDNESS **[two-actions] **SPELL 3**  **CONCENTRATE** **INCAPACITATION** **MANIPULATE**  **Traditions** arcane, divine, occult, primal  **Range **30 feet;** Targets** 1 creature  **Defense** Fortit |
| 3 | `merged::PZO22001 Starfinder Player Core 126-137::/page/5/Text/68` | 0.570847 | **SPELLS** |
| 4 | `merged::PZO22001 Starfinder Player Core 250-267::/page/13/Text/19` | 0.570847 | **SPELLS** |
| 5 | `merged::PZO22001 Starfinder Player Core 364-387::/page/13/Text/75` | 0.570847 | **SPELLS** |
| 6 | `merged::PZO22001 Starfinder Player Core 294-329::/page/11/Text/83` | 0.570847 | **SPELLS** |
| 7 | `merged::PZO22001 Starfinder Player Core 294-329::/page/9/Text/86` | 0.570847 | **SPELLS** |
| 8 | `merged::PZO22001 Starfinder Player Core 182-209::/page/17/Text/49` | 0.570847 | **SPELLS** |
| 9 | `merged::PZO22001 Starfinder Player Core 294-329::/page/17/Text/86` | 0.570847 | **SPELLS** |
| 10 | `merged::PZO22001 Starfinder Player Core 250-267::/page/1/Text/36` | 0.570847 | **SPELLS** |

### Query 42
- Text: Summarize You might solve problems with deductive reasoning or by determining mathematic  probabilities, drawing on your deep knowledge of the multiverse.
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 162-173::/page/1/Text/15']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 162-173::/page/1/Text/15', 'merged::PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/16', 'merged::PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/14']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/16` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/14` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 162-173::/page/1/Text/15` | 0.987244 | You might solve problems with deductive reasoning or by determining mathematic  probabilities, drawing on your deep knowledge of the multiverse. |
| 2 | `merged::PZO22001 Starfinder Player Core 162-173::/page/11/Text/17` | 0.564644 | The multiverse is a complex game—you use alternate realities to |
| 3 | `merged::PZO22001 Starfinder Player Core 162-173::/page/9/Text/53` | 0.558321 | You spend 10 minutes opening yourself to the mysteries of the  multiverse by peering across different timelines or analyzing  probability simulations. You gain the effects of *augury*, except  you lea |
| 4 | `merged::PZO22001 Starfinder Player Core 162-173::/page/1/Text/2` | 0.544701 | A strange paradoxical event forever altered your existence, and now you can manipulate reality. You  explore the infinite possibilities of the multiverse, possibly visualizing variant timelines or par |
| 5 | `merged::PZO22001 Starfinder Player Core 030-039::/page/5/Text/1` | 0.520180 | Technology and scientific knowledge flourish across the galaxy, but these advancements can't  solve every problem or answer all existential questions. Many turn to religion to understand their  place |
| 6 | `merged::PZO22001 Starfinder Player Core 162-173::/page/2/Text/10` | 0.474758 | from an alternate reality or a different timeline, or perhaps  you experienced an unnatural phenomenon that altered your  path, discovered a time-glitching alien device, or wrote a  treatise on quantu |
| 7 | `merged::PZO22001 Starfinder Player Core 162-173::/page/11/Text/6` | 0.471096 | Your paradoxical nature has become multifaceted. During daily  preparations, you can replace one of your paradox spells with a  spell of another paradox that grants training in the prerequisite  parad |
| 8 | `merged::PZO22001 Starfinder Player Core 182-209::/page/16/Text/6` | 0.466919 | You can trick and mislead others using disguises, lies, and  other forms of subterfuge. Deception often has a drawback  if you get found out, and it's often best to catch a shuttle  offworld by the ti |
| 9 | `merged::PZO22001 Starfinder Player Core 162-173::/page/2/Text/11` | 0.461516 | At 1st level, choose your paradox. Your chosen paradox  determines the tradition of your spells, additional trained  skills, additional spells you learn, and the effects of your  quantum field. You al |
| 10 | `merged::PZO22001 Starfinder Player Core 162-173::/page/4/Text/15` | 0.459216 | Your awareness of possible dangers, through incredible  analysis or an understanding of the wider multiverse,  increases your reflexes. Your proficiency rank for Reflex  saves increases to expert. |

### Query 43
- Text: What are the requirements for **PARKOUR **[one-action] **FEAT 8**?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 126-137::/page/9/Text/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 126-137::/page/9/Text/2', 'merged::PZO22001 Starfinder Player Core 126-137::/page/9/Text/1', 'merged::PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/4']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 126-137::/page/9/Text/1` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/4` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 126-137::/page/9/Text/2` | 0.853014 | **PARKOUR **[one-action] **FEAT 8** |
| 2 | `merged::PZO22001 Starfinder Player Core 126-137::/page/10/Text/10` | 0.587766 | **Prerequisites** Parkour |
| 3 | `merged::PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/18` | 0.583270 | **CHEER UP **[one-action] **FEAT 8** |
| 4 | `merged::PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/17` | 0.557376 | **MOMENTUM **[one-action] **FEAT 8** |
| 5 | `merged::PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/24` | 0.510277 | **PROPULSIVE SHIELD** **FEAT 8** |
| 6 | `merged::PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/43` | 0.504722 | **OPENING VOLLEY **[one-action] **FEAT 8** |
| 7 | `merged::PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/14` | 0.498869 | **HURRY **[one-action] **FEAT 6** |
| 8 | `merged::PZO22001 Starfinder Player Core 126-137::/page/9/Text/6` | 0.495186 | **TOPPLING SHOT **[two-actions] **FEAT 8** |
| 9 | `merged::PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/625` | 0.489645 | Parkour |
| 10 | `merged::PZO22001 Starfinder Player Core 210-231::/page/6/SectionHeader/49` | 0.480278 | **BARRICADE **[one-action] **FEAT 1** |

### Query 44
- Text: Summarize View your bond as a closed clique or think you're trying to recruit them.
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 114-125::/page/1/ListItem/24']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 114-125::/page/1/ListItem/24', 'merged::PZO22001 Starfinder Player Core 114-125::/page/1/ListItem/23', 'merged::PZO22001 Starfinder Player Core 114-125::/page/1/ListItem/25']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 114-125::/page/1/ListItem/23` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 114-125::/page/1/ListItem/25` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 114-125::/page/1/ListItem/24` | 0.982697 | View your bond as a closed clique or think you're trying to recruit them. |
| 2 | `merged::PZO22001 Starfinder Player Core 114-125::/page/1/Text/13` | 0.490524 | Your connection shapes your perspective on the world and the way you approach  problems. When a disagreement erupts between bonded members, you're often the  one to help them talk through their proble |
| 3 | `merged::PZO22001 Starfinder Player Core 114-125::/page/1/Text/17` | 0.473947 | You reflect on your connection to deepen your understanding. You spend time  with your bonded allies, perhaps working on the same side hustle, going on a hike  together, or forming a guild in your fav |
| 4 | `merged::PZO22001 Starfinder Player Core 092-097::/page/1/Text/4` | 0.457187 | You hunt people down for credits. You might work with a  corporation, military, or some other organization. |
| 5 | `merged::PZO22001 Starfinder Player Core 114-125::/page/2/Text/15` | 0.447292 | You form a bond between yourself and others, most typically  your closest companions. Forming bonds is different for every  mystic but always involves using a 10-minute activity related  to the mystic |
| 6 | `merged::PZO22001 Starfinder Player Core 114-125::/page/10/Text/44` | 0.445957 | You pulse energy through your bond as your ally casts a spell, empowering their spell in one of the following ways. |
| 7 | `merged::PZO22001 Starfinder Player Core 424-441::/page/15/Text/11` | 0.439451 | You are tied up and can barely move, or a creature has you  pinned. You have the off-guard and immobilized conditions,  and you can't use any attack or manipulate actions except  to attempt to Escape |
| 8 | `merged::PZO22001 Starfinder Player Core 114-125::/page/11/Text/16` | 0.431431 | **Target** any number of your bonded allies within 120 feet |
| 9 | `merged::PZO22001 Starfinder Player Core 114-125::/page/9/Text/17` | 0.421732 | You force link the target's mind to your bond and share a  confusing glimpse of your connection. Attempt a skill check  with your connection skill against the Will DC of a foe you  can see within 30 f |
| 10 | `merged::PZO22001 Starfinder Player Core 092-097::/page/2/Text/30` | 0.416562 | You're a con artist and trickster who swindles unsuspecting  dupes and blackmails rubes, but it's nothing personal you're just in it for the credits. You might run an operation  on the side, or you mi |

### Query 45
- Text: Summarize **LASHUNTA**
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/20']
- Expected found: `True`
- Expected rank: `12`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/20', 'merged::PZO22001 Starfinder Player Core 058-073::/page/2/Text/21', 'merged::PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/18']
- Expanded expected found: `True`
- Expanded expected rank: `12`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 058-073::/page/2/Text/21` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/18` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 058-073::/page/3/Text/11` | 0.922025 | **LASHUNTA** |
| 2 | `merged::PZO22001 Starfinder Player Core 058-073::/page/3/Text/20` | 0.922025 | **LASHUNTA** |
| 3 | `merged::PZO22001 Starfinder Player Core 058-073::/page/3/Text/26` | 0.922025 | **LASHUNTA** |
| 4 | `merged::PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/24` | 0.922025 | **LASHUNTA** |
| 5 | `merged::PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/11` | 0.922025 | **LASHUNTA** |
| 6 | `merged::PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/30` | 0.922025 | **LASHUNTA** |
| 7 | `merged::PZO22001 Starfinder Player Core 058-073::/page/3/Text/15` | 0.922025 | **LASHUNTA** |
| 8 | `merged::PZO22001 Starfinder Player Core 058-073::/page/3/Text/7` | 0.922025 | **LASHUNTA** |
| 9 | `merged::PZO22001 Starfinder Player Core 058-073::/page/3/Text/2` | 0.922025 | **LASHUNTA** |
| 10 | `merged::PZO22001 Starfinder Player Core 058-073::/page/3/Text/30` | 0.922025 | **LASHUNTA** |

### Query 46
- Text: What is the rule about You're trained in the Deception skill and a Lore skill about a  specific settlement. You gain the Face in the Crowd skill feat.?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 092-097::/page/1/Text/14']
- Expected found: `True`
- Expected rank: `1`
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
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 364-387::/page/5/Text/1', 'merged::PZO22001 Starfinder Player Core 364-387::/page/5/SectionHeader/0', 'merged::PZO22001 Starfinder Player Core 364-387::/page/5/Text/2']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 364-387::/page/5/SectionHeader/0` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 364-387::/page/5/Text/2` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 364-387::/page/5/Text/1` | 0.911017 | can't use reactions. It also can't use move actions except to  dance, using the Stride action to move up to half its Speed. **Critical Success** The target is unaffected. |
| 2 | `merged::PZO22001 Starfinder Player Core 406-423::/page/1/Text/16` | 0.623571 | An action might allow you to use a simpler action usually one of the Basic Actions on page 408—in a  different circumstance or with different effects. This  subordinate action still has its normal tra |
| 3 | `merged::PZO22001 Starfinder Player Core 406-423::/page/2/Text/2` | 0.597638 | Basic actions represent common tasks like moving around,  attacking, and helping others. As such, every creature can  use basic actions except in some extreme circumstances,  and many of those actions |
| 4 | `merged::PZO22001 Starfinder Player Core 406-423::/page/1/Text/7` | 0.591370 | Some effects are even more restrictive. Certain abilities,  instead of or in addition to changing the number of actions  you can use, say specifically that you can't use reactions.  The most restricti |
| 5 | `merged::PZO22001 Starfinder Player Core 126-137::/page/6/Text/7` | 0.573327 | You dodge, roll, and weave out of danger, leaving no openings  for attack as you move across the battlefield. Stride up to  your Speed. This movement doesn't trigger reactions. |
| 6 | `merged::PZO22001 Starfinder Player Core 406-423::/page/0/Text/27` | 0.572198 | You can use free actions that have triggers and reactions only  in response to certain events. Each such reaction and free  action lists the trigger that must happen for you to perform it.  When its t |
| 7 | `merged::PZO22001 Starfinder Player Core 210-231::/page/16/Text/30` | 0.572177 | You can use High Jump and Long Jump as a single action  instead of 2 actions. If you do, you don't perform the initial  Stride (nor do you fail if you don't Stride 10 feet). |
| 8 | `merged::PZO22001 Starfinder Player Core 406-423::/page/1/Text/9` | 0.571528 | Various abilities and conditions, such as a Reactive Strike,  can disrupt an action. When an action is disrupted, you still  use the actions or reactions you committed, and you still  expend any costs |
| 9 | `merged::PZO22001 Starfinder Player Core 406-423::/page/0/Text/10` | 0.571158 | **Reactions** have triggers, which must be met for you to use  the reaction. You can use a reaction anytime its trigger is met,  whether it's your turn or not. Outside of encounters, your use  of reac |
| 10 | `merged::PZO22001 Starfinder Player Core 406-423::/page/6/Text/12` | 0.567404 | When you use the Stride action, you move a number of  feet equal to your Speed. Whenever a rule mentions your  Speed without specifying a type, it's referring to your  land Speed. |

### Query 48
- Text: What are the requirements for **Prerequisites** trained in Intimidation?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 126-137::/page/6/Text/58']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 126-137::/page/6/Text/58', 'merged::PZO22001 Starfinder Player Core 126-137::/page/7/SectionHeader/1', 'merged::PZO22001 Starfinder Player Core 126-137::/page/6/SectionHeader/57']
- Expanded expected found: `True`
- Expanded expected rank: `3`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 126-137::/page/7/SectionHeader/1` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 126-137::/page/6/SectionHeader/57` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 210-231::/page/12/Text/39` | 0.919563 | **Prerequisites** trained in Intimidation |
| 2 | `merged::PZO22001 Starfinder Player Core 210-231::/page/11/Text/27` | 0.919563 | **Prerequisites** trained in Intimidation |
| 3 | `merged::PZO22001 Starfinder Player Core 126-137::/page/6/Text/58` | 0.919563 | **Prerequisites** trained in Intimidation |
| 4 | `merged::PZO22001 Starfinder Player Core 210-231::/page/16/Text/10` | 0.919563 | **Prerequisites** trained in Intimidation |
| 5 | `merged::PZO22001 Starfinder Player Core 210-231::/page/12/Text/28` | 0.919563 | **Prerequisites** trained in Intimidation |
| 6 | `merged::PZO22001 Starfinder Player Core 150-161::/page/7/SectionHeader/24` | 0.919563 | **Prerequisites** trained in Intimidation |
| 7 | `merged::PZO22001 Starfinder Player Core 210-231::/page/13/Text/4` | 0.830359 | **Prerequisites** expert in Intimidation |
| 8 | `merged::PZO22001 Starfinder Player Core 210-231::/page/19/Text/48` | 0.808302 | **Prerequisites** master in Intimidation |
| 9 | `merged::PZO22001 Starfinder Player Core 210-231::/page/6/Text/56` | 0.808302 | **Prerequisites** master in Intimidation |
| 10 | `merged::PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/663` | 0.781026 | Trained in Intimidation |

### Query 49
- Text: What is the rule about Each entry includes details about the ancestry and presents  the rules elements described below.?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 040-057::/page/1/Text/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 040-057::/page/1/Text/13', 'merged::PZO22001 Starfinder Player Core 040-057::/page/1/SectionHeader/12', 'merged::PZO22001 Starfinder Player Core 040-057::/page/1/SectionHeader/14']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 040-057::/page/1/SectionHeader/12` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 040-057::/page/1/SectionHeader/14` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 040-057::/page/1/Text/13` | 0.871381 | Each entry includes details about the ancestry and presents  the rules elements described below. |
| 2 | `merged::PZO22001 Starfinder Player Core 040-057::/page/1/Text/29` | 0.623663 | Any other entries in the sidebar represent abilities, senses,  and other qualities all members of the ancestry manifest.  These are omitted for ancestries with no special rules. |
| 3 | `merged::PZO22001 Starfinder Player Core 014-029::/page/2/Text/7` | 0.618696 | Regardless of the game mechanic they convey, rules  elements are always presented in the form of a stat block,  a summary of the rules necessary to bring the monster,  character, item, or other rules |
| 4 | `merged::PZO22001 Starfinder Player Core 442-464::/page/0/Text/38` | 0.601462 | **ancestry** A broad family of people that a creature belongs to.  Each player character chooses an ancestry as the first step of  character creation. 10, 19, 27, **41–91** mixed ancestry 83 |
| 5 | `merged::PZO22001 Starfinder Player Core 014-029::/page/9/Text/3` | 0.585235 | **Ancestry:** Each ancestry provides attribute boosts, and sometimes an attribute flaw. If you're taking any voluntary  flaws, apply them in this step (see the sidebar on page 25). |
| 6 | `merged::PZO22001 Starfinder Player Core 014-029::/page/0/Text/6` | 0.580176 | The rules for ancestries and heritages representing the  Pact Worlds are in this chapter, including their ancestry  feat options. Backgrounds are at the end of this chapter,  along with a section abou |
| 7 | `merged::PZO22001 Starfinder Player Core 040-057::/page/1/Text/21` | 0.556631 | When creating a character of this ancestry, you apply attribute |
| 8 | `merged::PZO22001 Starfinder Player Core 098-113::/page/2/Text/26` | 0.554490 | This section serves as a reminder of the ancestry feats your  character gains at 5th, 9th, 13th, and 17th levels. Ancestry  feats are detailed in each ancestry entry in Chapter 2, which  begins on pag |
| 9 | `merged::PZO22001 Starfinder Player Core 040-057::/page/1/ListItem/8` | 0.553538 | **Ancestries** express the lineage your character hails from.  Within ancestries are heritages—subgroups that have  unique characteristics. An ancestry provides attribute  boosts (and perhaps attribut |
| 10 | `merged::PZO22001 Starfinder Player Core 040-057::/page/12/Text/4` | 0.544549 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As a human, you choose from among the  following anc |

### Query 50
- Text: What is the rule about Major locations on Verces include the Ring of Nations,  a band of sprawling megacities inhabited by augmented  verthani, androids, and many others; Skydock, modern  shipyards built atop an ancient space platform; Fullbright, a  burning desert of corporate solar farms and fringe Outlaw  Kingdoms; and Darkside, a frozen landscape of ice mines and  howling tundra stalked by terrible beasts.?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 030-039::/page/2/Text/16']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 030-039::/page/2/Text/16', 'merged::PZO22001 Starfinder Player Core 030-039::/page/2/Text/15', 'merged::PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/17']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 030-039::/page/2/Text/15` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/17` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 030-039::/page/2/Text/16` | 0.909462 | Major locations on Verces include the Ring of Nations,  a band of sprawling megacities inhabited by augmented  verthani, androids, and many others; Skydock, modern  shipyards built atop an ancient spa |
| 2 | `merged::PZO22001 Starfinder Player Core 030-039::/page/2/Text/15` | 0.700183 | Verces is a tidally locked world with a sun-scoured light side,  a frozen dark side, and a belt of opulent cybercities linked by  high-speed bullet trains called the Ring of Nations. The Ring  of Nati |
| 3 | `merged::PZO22001 Starfinder Player Core 442-464::/page/14/Text/22` | 0.541346 | **Verces** A tidally locked planet which is half frozen and half desert,  with a world-spanning Ring of Nations between the two. 32 |
| 4 | `merged::PZO22001 Starfinder Player Core 030-039::/page/4/Text/10` | 0.537026 | Regions include Nightarch, a pressurized megacity where  opulent spires tower over air-choked slums, named for the  massive gate leading inside the planet at the center of the  settlement; the Silted |
| 5 | `merged::PZO22001 Starfinder Player Core 030-039::/page/3/Text/12` | 0.523142 | Regions on Triaxus include the Drakelands, a continental  wilderness preserve tended by dragons; the Skyfire Mandate,  an isthmus guarded by the oldest aeries of the Skyfire Legion;  the Allied Territ |
| 6 | `merged::PZO22001 Starfinder Player Core 030-039::/page/4/Text/19` | 0.520122 | Regions include Voyedris, a treacherous wilderness  ravaged by rapid industrialization; Hafrerren, a rebel nationstate known for biotech research; Rafemii, a hub for magical  and spiritual development |
| 7 | `merged::PZO22001 Starfinder Player Core 030-039::/page/4/Text/29` | 0.517775 | Regions of the Vast include the Azlanti Star Empire, a vast  territory of unknown size controlled by a colonizing regime  ruled by the descendants of a human nation from lost Golarion;  Kazmurg's Absu |
| 8 | `merged::PZO22001 Starfinder Player Core 030-039::/page/1/Text/6` | 0.512933 | The largest community on Aballon is Striving, an  industrious megacity containing a citywide neural network  sacred to Triune. Other regions include the industrial forgecity Automatrix; the immense, f |
| 9 | `merged::PZO22001 Starfinder Player Core 040-057::/page/11/Text/28` | 0.486996 | You have grown up in a big city and are accustomed to the  press and pull of the largest crowds, the electric buzz and  tangle of streets, or the dense nature of vertical living on a  station or megap |
| 10 | `merged::PZO22001 Starfinder Player Core 030-039::/page/4/Text/26` | 0.486962 | Near Space regions include the Veskarium, an empire of  seven conquered planets and a few dozen colonies ruled  by vesk military leaders; the Marixah Republic, a group of  allied planets emerging onto |

### Query 51
- Text: What are the requirements for **SINGULARITY **[three-actions] **FEAT 14**?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 138-149::/page/10/SectionHeader/29']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 138-149::/page/10/SectionHeader/29', 'merged::PZO22001 Starfinder Player Core 138-149::/page/10/Text/28', 'merged::PZO22001 Starfinder Player Core 138-149::/page/10/Text/31']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 138-149::/page/10/Text/28` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 138-149::/page/10/Text/31` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 138-149::/page/10/SectionHeader/29` | 0.893014 | **SINGULARITY **[three-actions] **FEAT 14** |
| 2 | `merged::PZO22001 Starfinder Player Core 126-137::/page/10/SectionHeader/23` | 0.581458 | **CLUSTERED SHOTS **[two-actions] **FEAT 14** |
| 3 | `merged::PZO22001 Starfinder Player Core 138-149::/page/10/SectionHeader/19` | 0.568060 | **BIG BANG **[three-actions] **FEAT 14** |
| 4 | `merged::PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/28` | 0.566688 | **SCATTERING FIRE **[two-actions] **FEAT 14** |
| 5 | `merged::PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/49` | 0.558073 | **YOU CAN DO IT **[one-action] **FEAT 14** |
| 6 | `merged::PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/34` | 0.557617 | **TERROR-FORMING **[two-actions] **FEAT 14** |
| 7 | `merged::PZO22001 Starfinder Player Core 442-464::/page/11/Text/30` | 0.536715 | **single action **([one-action]) An action that takes one of your three  actions on your turn. 15, **406** |
| 8 | `merged::PZO22001 Starfinder Player Core 126-137::/page/10/SectionHeader/28` | 0.529350 | **FISH IN A BARREL **[two-actions] **FEAT 14** |
| 9 | `merged::PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/44` | 0.526643 | **READY TO ROLL **[free-action] **FEAT 14** |
| 10 | `merged::PZO22001 Starfinder Player Core 210-231::/page/13/SectionHeader/21` | 0.522931 | **LEGENDARY NEGOTIATION **[three-actions] **FEAT 15** |

### Query 52
- Text: Summarize A sarcesian witchwarper from a reality where the water  in the River Between never dried up.
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/33']
- Expected found: `True`
- Expected rank: `1`
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
| 3 | `merged::PZO22001 Starfinder Player Core 098-113::/page/3/Text/41` | 0.477777 | A witchwarper alters reality by drawing on the  infinite possibilities of other universes and timelines.  Every witchwarper is influenced by an event, and they  can harness paradoxical powers to creat |
| 4 | `merged::PZO22001 Starfinder Player Core 098-113::/page/3/Text/44` | 0.474730 | **Zemir** the human witchwarper jumps between  realities and timelines, trusting his uncanny  luck and years of experience to keep him  anchored while searching for the loved ones he  lost years ago t |
| 5 | `merged::PZO22001 Starfinder Player Core 294-329::/page/3/Text/19` | 0.474266 | are determined by their connection, and a witchwarper's are  determined by their paradox. |
| 6 | `merged::PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/1` | 0.468019 | **Sample Witchwarper** |
| 7 | `merged::PZO22001 Starfinder Player Core 030-039::/page/4/ListItem/23` | 0.450249 | A mystic wandering the wastes ravaged by the Shriek,  seeking natural ways to heal your war-torn ancestral lands. |
| 8 | `merged::PZO22001 Starfinder Player Core 098-113::/page/13/Text/64` | 0.432472 | **Witchwarper** |
| 9 | `merged::PZO22001 Starfinder Player Core 162-173::/page/9/Text/76` | 0.432472 | **Witchwarper** |
| 10 | `merged::PZO22001 Starfinder Player Core 114-125::/page/5/Text/28` | 0.432472 | **Witchwarper** |

### Query 53
- Text: What is the rule about Trained in solarian class DC?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 138-149::/page/1/Text/62']
- Expected found: `True`
- Expected rank: `1`
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
| 4 | `merged::PZO22001 Starfinder Player Core 126-137::/page/1/Text/61` | 0.612261 | Trained in operative class DC |
| 5 | `merged::PZO22001 Starfinder Player Core 098-113::/page/5/Text/64` | 0.582520 | Trained in envoy class DC |
| 6 | `merged::PZO22001 Starfinder Player Core 138-149::/page/4/Text/9` | 0.580162 | Your ability to manipulate stellar forces has improved. Your  proficiency rank for your solarian class DC increases to expert. |
| 7 | `merged::PZO22001 Starfinder Player Core 014-029::/page/12/Text/15` | 0.558336 | Turning to skills, Jessica marks Athletics as trained  because all solarians are trained in Athletics. She then gets  to choose four more skills (if her character had a higher  Intelligence, she would |
| 8 | `merged::PZO22001 Starfinder Player Core 442-464::/page/15/TableCell/220` | 0.535547 | Class DC |
| 9 | `merged::PZO22001 Starfinder Player Core 014-029::/page/11/SectionHeader/14` | 0.534821 | CLASS DC |
| 10 | `merged::PZO22001 Starfinder Player Core 138-149::/page/3/Text/40` | 0.528006 | At 1st level and every even-numbered level, you gain a  solarian class feat. These begin on page 143. |

### Query 54
- Text: Summarize **Exploration ** **Mode**
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 424-441::/page/1/Text/48']
- Expected found: `True`
- Expected rank: `16`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 424-441::/page/1/Text/48', 'merged::PZO22001 Starfinder Player Core 424-441::/page/1/Text/47', 'merged::PZO22001 Starfinder Player Core 424-441::/page/1/Text/49']
- Expanded expected found: `True`
- Expanded expected rank: `16`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 424-441::/page/1/Text/47` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 424-441::/page/1/Text/49` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 424-441::/page/3/Text/46` | 0.933318 | **Exploration ** **Mode** |
| 2 | `merged::PZO22001 Starfinder Player Core 424-441::/page/5/Text/55` | 0.933318 | **Exploration ** **Mode** |
| 3 | `merged::PZO22001 Starfinder Player Core 424-441::/page/7/Text/67` | 0.933318 | **Exploration ** **Mode** |
| 4 | `merged::PZO22001 Starfinder Player Core 424-441::/page/9/Text/50` | 0.933318 | **Exploration ** **Mode** |
| 5 | `merged::PZO22001 Starfinder Player Core 388-405::/page/5/Text/38` | 0.933318 | **Exploration ** **Mode** |
| 6 | `merged::PZO22001 Starfinder Player Core 388-405::/page/3/Text/54` | 0.933318 | **Exploration ** **Mode** |
| 7 | `merged::PZO22001 Starfinder Player Core 406-423::/page/15/Text/35` | 0.933318 | **Exploration ** **Mode** |
| 8 | `merged::PZO22001 Starfinder Player Core 406-423::/page/9/Text/44` | 0.933318 | **Exploration ** **Mode** |
| 9 | `merged::PZO22001 Starfinder Player Core 388-405::/page/11/Text/37` | 0.933318 | **Exploration ** **Mode** |
| 10 | `merged::PZO22001 Starfinder Player Core 388-405::/page/9/Text/41` | 0.933318 | **Exploration ** **Mode** |

### Query 55
- Text: What are the requirements for **Prerequisites** Parkour?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 126-137::/page/10/Text/10']
- Expected found: `False`
- Expected rank: `None`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 126-137::/page/10/Text/10', 'merged::PZO22001 Starfinder Player Core 126-137::/page/10/Text/9', 'merged::PZO22001 Starfinder Player Core 126-137::/page/10/Text/11']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 126-137::/page/10/Text/9` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 126-137::/page/10/Text/11` (reasons: ['graph_depth_1'])

### Query 56
- Text: Summarize +1
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/660']
- Expected found: `False`
- Expected rank: `None`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/660', 'merged::PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/661', 'merged::PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/659']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/661` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/659` (reasons: ['graph_depth_1'])

### Query 57
- Text: What are the requirements for **Prerequisites** trained in Deception?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 098-113::/page/12/Text/22']
- Expected found: `True`
- Expected rank: `6`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 098-113::/page/12/Text/22', 'merged::PZO22001 Starfinder Player Core 098-113::/page/12/Text/21', 'merged::PZO22001 Starfinder Player Core 098-113::/page/12/Text/23']
- Expanded expected found: `True`
- Expanded expected rank: `6`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 098-113::/page/12/Text/21` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 098-113::/page/12/Text/23` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 210-231::/page/7/Text/34` | 0.889915 | **Prerequisites** trained in Deception |
| 2 | `merged::PZO22001 Starfinder Player Core 210-231::/page/10/Text/42` | 0.889915 | **Prerequisites** trained in Deception |
| 3 | `merged::PZO22001 Starfinder Player Core 098-113::/page/10/Text/23` | 0.889915 | **Prerequisites** trained in Deception |
| 4 | `merged::PZO22001 Starfinder Player Core 210-231::/page/10/Text/25` | 0.889915 | **Prerequisites** trained in Deception |
| 5 | `merged::PZO22001 Starfinder Player Core 210-231::/page/14/Text/10` | 0.889915 | **Prerequisites** trained in Deception |
| 6 | `merged::PZO22001 Starfinder Player Core 098-113::/page/12/Text/22` | 0.889915 | **Prerequisites** trained in Deception |
| 7 | `merged::PZO22001 Starfinder Player Core 210-231::/page/14/Text/5` | 0.889915 | **Prerequisites** trained in Deception |
| 8 | `merged::PZO22001 Starfinder Player Core 210-231::/page/8/Text/6` | 0.806080 | **Prerequisites** expert in Deception |
| 9 | `merged::PZO22001 Starfinder Player Core 210-231::/page/10/Text/52` | 0.806080 | **Prerequisites** expert in Deception |
| 10 | `merged::PZO22001 Starfinder Player Core 210-231::/page/16/Text/15` | 0.806080 | **Prerequisites** expert in Deception |

### Query 58
- Text: What is the rule about **ACTION ICON KEY**?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 406-423::/page/0/SectionHeader/12']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 406-423::/page/0/SectionHeader/12', 'merged::PZO22001 Starfinder Player Core 406-423::/page/0/Text/11', 'merged::PZO22001 Starfinder Player Core 406-423::/page/0/Text/13']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 406-423::/page/0/Text/11` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 406-423::/page/0/Text/13` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 406-423::/page/0/SectionHeader/12` | 0.886468 | **ACTION ICON KEY** |
| 2 | `merged::PZO22001 Starfinder Player Core 442-464::/page/15/TableCell/222` | 0.621044 | Action Icons |
| 3 | `merged::PZO22001 Starfinder Character Sheet::/page/0/TableCell/201` | 0.601814 | Action Icons  ❖ Single Action  ❖ Two-Action Activity |
| 4 | `merged::PZO22001 Starfinder Player Core 014-029::/page/1/Text/8` | 0.524193 | Throughout this book, you will see special icons to  denote actions. |
| 5 | `merged::PZO22001 Starfinder Player Core 406-423::/page/1/Text/11` | 0.520574 | These rules clarify some of the specifics of using actions. |
| 6 | `merged::PZO22001 Starfinder Player Core 182-209::/page/27/Text/41` | 0.520518 | **General Skill ** **Actions** |
| 7 | `merged::PZO22001 Starfinder Player Core 182-209::/page/25/Text/31` | 0.520518 | **General Skill ** **Actions** |
| 8 | `merged::PZO22001 Starfinder Player Core 182-209::/page/9/Text/40` | 0.520518 | **General Skill ** **Actions** |
| 9 | `merged::PZO22001 Starfinder Player Core 182-209::/page/1/Text/24` | 0.520518 | **General Skill ** **Actions** |
| 10 | `merged::PZO22001 Starfinder Player Core 182-209::/page/11/Text/39` | 0.520518 | **General Skill ** **Actions** |

### Query 59
- Text: What is the rule about **ANCESTRIES & ** **BACKGROUNDS**?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 001-013::/page/4/Text/26']
- Expected found: `False`
- Expected rank: `None`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 001-013::/page/4/Text/26', 'merged::PZO22001 Starfinder Player Core 001-013::/page/6/Text/18', 'merged::PZO22001 Starfinder Player Core 001-013::/page/10/Text/38', 'merged::PZO22001 Starfinder Player Core 001-013::/page/8/Text/19', 'merged::PZO22001 Starfinder Player Core 001-013::/page/4/Text/27', 'merged::PZO22001 Starfinder Player Core 001-013::/page/12/Text/33', 'merged::PZO22001 Starfinder Player Core 001-013::/page/4/Text/25']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 001-013::/page/6/Text/18` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 001-013::/page/10/Text/38` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 001-013::/page/8/Text/19` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 001-013::/page/4/Text/27` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 001-013::/page/12/Text/33` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 001-013::/page/4/Text/25` (reasons: ['graph_depth_1'])

### Query 60
- Text: What does **GHOSTLY CARRIER **[two-actions] **SPELL 2** do?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 330-363::/page/4/SectionHeader/17']
- Expected found: `False`
- Expected rank: `None`
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
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 174-181::/page/0/SectionHeader/14', 'merged::PZO22001 Starfinder Player Core 174-181::/page/0/Text/13', 'merged::PZO22001 Starfinder Player Core 174-181::/page/0/Text/15']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 174-181::/page/0/Text/13` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 174-181::/page/0/Text/15` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 174-181::/page/0/SectionHeader/14` | 0.853040 | SPELLCASTING ARCHETYPES |
| 2 | `merged::PZO22001 Starfinder Player Core 232-249::/page/11/SectionHeader/37` | 0.658823 | SPELLCASTING |
| 3 | `merged::PZO22001 Starfinder Player Core 014-029::/page/11/SectionHeader/18` | 0.631034 | **SPELLS AND SPELLCASTING** |
| 4 | `merged::PZO22001 Starfinder Player Core 232-249::/page/11/SectionHeader/39` | 0.573786 | **SPELLCASTING SERVICES** |
| 5 | `merged::PZO22001 Starfinder Player Core 174-181::/page/0/SectionHeader/1` | 0.525172 | ARCHETYPES |
| 6 | `merged::PZO22001 Starfinder Player Core 174-181::/page/0/SectionHeader/20` | 0.508283 | SPECIAL ARCHETYPES |
| 7 | `merged::PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/11` | 0.491979 | **SPELLCASTING IN STARFINDER** |
| 8 | `merged::PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/17` | 0.486179 | **BASIC MYSTIC SPELLCASTING** **FEAT 4** |
| 9 | `merged::PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/43` | 0.482951 | **EXPERT MYSTIC SPELLCASTING** **FEAT 12** |
| 10 | `merged::PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0` | 0.455668 | CHAPTER 7: SPELLS |

### Query 62
- Text: What is the rule about Gain a 1st-level ancestry feat?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/465']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/465', 'merged::PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/464', 'merged::PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/466']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/464` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/466` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/465` | 0.870093 | Gain a 1st-level ancestry feat |
| 2 | `merged::PZO22001 Starfinder Player Core 040-057::/page/12/Text/4` | 0.783056 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As a human, you choose from among the  following anc |
| 3 | `merged::PZO22001 Starfinder Player Core 098-113::/page/8/Text/14` | 0.721273 | In addition to the initial ancestry feat you started with, you  gain an ancestry feat at 5th level and every 4 levels thereafter. |
| 4 | `merged::PZO22001 Starfinder Player Core 126-137::/page/4/Text/21` | 0.721273 | In addition to the initial ancestry feat you started with, you  gain an ancestry feat at 5th level and every 4 levels thereafter. |
| 5 | `merged::PZO22001 Starfinder Player Core 040-057::/page/4/Text/5` | 0.701677 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As an android, you choose from among  the following |
| 6 | `merged::PZO22001 Starfinder Player Core 040-057::/page/1/Text/33` | 0.695332 | This section presents ancestry feats, which allow you to  customize your character. You gain your first ancestry feat  at 1st level, and you gain another at 5th level, 9th level, 13th  level, and 17th |
| 7 | `merged::PZO22001 Starfinder Player Core 058-073::/page/6/Text/7` | 0.695208 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As a pahtra, you choose from among the  following an |
| 8 | `merged::PZO22001 Starfinder Player Core 058-073::/page/10/Text/11` | 0.694104 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As a shirren, you choose from among the  following a |
| 9 | `merged::PZO22001 Starfinder Player Core 040-057::/page/8/Text/4` | 0.692293 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th,  9th, 13th, and 17th level). As a barathu, you choose from  among the following a |
| 10 | `merged::PZO22001 Starfinder Player Core 040-057::/page/16/Text/7` | 0.688358 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As a kasatha, you choose from among  the following a |

### Query 63
- Text: What are the requirements for **INTERNAL COMPARTMENT** **FEAT 1**?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 040-057::/page/4/SectionHeader/17']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 040-057::/page/4/SectionHeader/17', 'merged::PZO22001 Starfinder Player Core 040-057::/page/4/Text/16', 'merged::PZO22001 Starfinder Player Core 040-057::/page/4/Text/19']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 040-057::/page/4/Text/16` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 040-057::/page/4/Text/19` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 040-057::/page/4/SectionHeader/17` | 0.814023 | **INTERNAL COMPARTMENT** **FEAT 1** |
| 2 | `merged::PZO22001 Starfinder Player Core 040-057::/page/9/SectionHeader/30` | 0.461687 | **INTERNAL CHEMISTRY** **FEAT 13** |
| 3 | `merged::PZO22001 Starfinder Player Core 040-057::/page/5/SectionHeader/16` | 0.448879 | **INTERNAL RESPIRATOR** **FEAT 9** |
| 4 | `merged::PZO22001 Starfinder Player Core 040-057::/page/12/SectionHeader/22` | 0.424204 | **GENERAL TRAINING** **FEAT 1** |
| 5 | `merged::PZO22001 Starfinder Player Core 210-231::/page/18/Text/11` | 0.421373 | **SKILL TRAINING** **FEAT 1** |
| 6 | `merged::PZO22001 Starfinder Player Core 330-363::/page/25/Text/59` | 0.417391 | **FEATS** **EQUIPMENT** |
| 7 | `merged::PZO22001 Starfinder Player Core 232-249::/page/9/Text/21` | 0.417391 | **FEATS** **EQUIPMENT** |
| 8 | `merged::PZO22001 Starfinder Player Core 330-363::/page/27/Text/61` | 0.417391 | **FEATS** **EQUIPMENT** |
| 9 | `merged::PZO22001 Starfinder Player Core 210-231::/page/12/SectionHeader/16` | 0.414544 | **IMPRESSIVE PERFORMANCE** **FEAT 1** |
| 10 | `merged::PZO22001 Starfinder Player Core 210-231::/page/16/Text/21` | 0.413606 | **QUICK INSTALL** **FEAT 1** |

### Query 64
- Text: What are the requirements for **TWIN GUARD **[reaction] **FEAT 10**?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/51']
- Expected found: `False`
- Expected rank: `None`
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
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 030-039::/page/0/SectionHeader/15', 'merged::PZO22001 Starfinder Player Core 030-039::/page/0/Text/16', 'merged::PZO22001 Starfinder Player Core 030-039::/page/0/ListItem/14']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 030-039::/page/0/Text/16` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 030-039::/page/0/ListItem/14` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 030-039::/page/0/SectionHeader/15` | 0.836002 | THE PACT WORLDS |
| 2 | `merged::PZO22001 Starfinder Player Core 442-464::/page/9/Text/10` | 0.596749 | **Pact Worlds** The governing body of planets that make up the  core of the primary Starfinder setting. 30–34 |
| 3 | `merged::PZO22001 Starfinder Player Core 092-097::/page/5/TableCell/491` | 0.580314 | Humans, most citizens of the Pact Worlds |
| 4 | `merged::PZO22001 Starfinder Player Core 014-029::/page/0/Text/6` | 0.540005 | The rules for ancestries and heritages representing the  Pact Worlds are in this chapter, including their ancestry  feat options. Backgrounds are at the end of this chapter,  along with a section abou |
| 5 | `merged::PZO22001 Starfinder Player Core 232-249::/page/1/Text/9` | 0.485436 | The basic currency of the Pact Worlds (and Starfinder overall)  is the credit. Interplanetary business is conducted through  the trade of credits standardized by the strenuous banking  regulations of |
| 6 | `merged::PZO22001 Starfinder Player Core 030-039::/page/0/Text/16` | 0.451369 | The Pact Worlds form the core of the Starfinder setting.  "The Pact Worlds" is the formal name for the united planets  orbiting lost Golarion's sun and their more distant allied  worlds, including Pul |
| 7 | `merged::PZO22001 Starfinder Player Core 092-097::/page/5/Table/7` | 0.439815 | LanguageSpeakersCommonHumans, most citizens of the Pact WorldsKasathaKasathas, inhabitants of Kasath or the IdariPahtraPahtras |
| 8 | `merged::PZO22001 Starfinder Player Core 092-097::/page/5/Text/14` | 0.433334 | Most characters also learn the Common language. This  is the most widely used language in the galaxy and is the  dominant language of the Pact Worlds. In many systems,  even if Common is not the offic |
| 9 | `merged::PZO22001 Starfinder Player Core 232-249::/page/1/Text/10` | 0.427171 | Pact credits themselves are a combination of both digital  and physical currency assets. One person might contain all  their credits on a digital datacrypt that's safeguarded by the  most rigorous of |
| 10 | `merged::PZO22001 Starfinder Player Core 092-097::/page/5/Text/4` | 0.426893 | The languages presented here are grouped according to their use in the Pact Worlds. Languages that are uncommon  are most frequently spoken by their native speakers, but  they are also spoken by certa |

### Query 66
- Text: What are the requirements for **BREATH CONTROL** **FEAT 1**?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 210-231::/page/7/Text/17']
- Expected found: `True`
- Expected rank: `1`
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
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/405', 'merged::PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/406', 'merged::PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/404']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/406` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/404` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/405` | 0.850498 | 5th-rank spells, ancestry feat, resilient soul, skill increase |
| 2 | `merged::PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/421` | 0.658874 | 9th-rank spells, ancestry feat, skill increase |
| 3 | `merged::PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/397` | 0.628403 | 3rd-rank spells, ancestry feat, attribute boosts, fortitude expertise, skill increase |
| 4 | `merged::PZO22001 Starfinder Player Core 040-057::/page/12/Text/4` | 0.603836 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As a human, you choose from among the  following anc |
| 5 | `merged::PZO22001 Starfinder Player Core 114-125::/page/4/Text/13` | 0.590824 | In addition to the initial ancestry feat you started with,  you gain an ancestry feat at 5th level and every 4 levels  thereafter. The list of ancestry feats available to you can be  found in your anc |
| 6 | `merged::PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/413` | 0.586420 | 7th-rank spells, ancestry feat, armor expertise, skill increase, weapon specialization |
| 7 | `merged::PZO22001 Starfinder Player Core 098-113::/page/8/Text/14` | 0.580460 | In addition to the initial ancestry feat you started with, you  gain an ancestry feat at 5th level and every 4 levels thereafter. |
| 8 | `merged::PZO22001 Starfinder Player Core 040-057::/page/8/Text/4` | 0.557064 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th,  9th, 13th, and 17th level). As a barathu, you choose from  among the following a |
| 9 | `merged::PZO22001 Starfinder Player Core 040-057::/page/16/Text/7` | 0.553984 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As a kasatha, you choose from among  the following a |
| 10 | `merged::PZO22001 Starfinder Player Core 040-057::/page/4/Text/5` | 0.546653 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As an android, you choose from among  the following |

### Query 68
- Text: Lookup values for SizeSpaceReach (Tall)Reach (Long)TinyLess than 5
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 406-423::/page/7/Table/25']
- Expected found: `False`
- Expected rank: `None`
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
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 268-281::/page/1/SectionHeader/4', 'merged::PZO22001 Starfinder Player Core 268-281::/page/1/SectionHeader/3', 'merged::PZO22001 Starfinder Player Core 268-281::/page/1/Text/6']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 268-281::/page/1/SectionHeader/3` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 268-281::/page/1/Text/6` (reasons: ['graph_depth_1'])

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
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 442-464::/page/0/Text/29', 'merged::PZO22001 Starfinder Player Core 442-464::/page/0/Text/28', 'merged::PZO22001 Starfinder Player Core 442-464::/page/0/Text/30']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 442-464::/page/0/Text/28` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 442-464::/page/0/Text/30` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 442-464::/page/0/Text/29` | 0.880172 | **agile** (weapon trait) 255 |
| 2 | `merged::PZO22001 Starfinder Player Core 442-464::/page/1/Text/37` | 0.719173 | **automatic** (weapon trait) 255 |
| 3 | `merged::PZO22001 Starfinder Player Core 442-464::/page/3/Text/16` | 0.657998 | **critical** (weapon trait) 256 |
| 4 | `merged::PZO22001 Starfinder Player Core 442-464::/page/10/Text/7` | 0.656425 | **professional** (weapon trait) 256 |
| 5 | `merged::PZO22001 Starfinder Player Core 442-464::/page/13/Text/31` | 0.643055 | **thought** (weapon trait) 258 |
| 6 | `merged::PZO22001 Starfinder Player Core 442-464::/page/9/Text/42` | 0.637008 | **powered** (weapon trait) 256 |
| 7 | `merged::PZO22001 Starfinder Player Core 442-464::/page/13/Text/39` | 0.636856 | weapon traits 255–258 |
| 8 | `merged::PZO22001 Starfinder Player Core 442-464::/page/14/Text/38` | 0.636856 | weapon traits 255–258 |
| 9 | `merged::PZO22001 Starfinder Player Core 442-464::/page/2/Text/4` | 0.633844 | **breakdown** (weapon trait) 255 |
| 10 | `merged::PZO22001 Starfinder Player Core 442-464::/page/1/Text/2` | 0.632970 | **arc** (weapon trait) 255 |

### Query 72
- Text: Summarize 4
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/396']
- Expected found: `False`
- Expected rank: `None`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/396', 'merged::PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/395', 'merged::PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/397']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/395` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/397` (reasons: ['graph_depth_1'])

### Query 73
- Text: Summarize Huge
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/244']
- Expected found: `False`
- Expected rank: `None`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/244', 'merged::PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/245', 'merged::PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/243']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/245` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 232-249::/page/3/TableCell/243` (reasons: ['graph_depth_1'])

### Query 74
- Text: What is the rule about At 5th level, whenever you get a critical hit with one  of these attacks, you get its critical specialization effect. **Special** You can take this feat three times. Each time you  do, select a different attack from the options listed above.?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 074-091::/page/2/Text/20']
- Expected found: `False`
- Expected rank: `None`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 074-091::/page/2/Text/20', 'merged::PZO22001 Starfinder Player Core 074-091::/page/2/SectionHeader/21', 'merged::PZO22001 Starfinder Player Core 074-091::/page/2/Text/19']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 074-091::/page/2/SectionHeader/21` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 074-091::/page/2/Text/19` (reasons: ['graph_depth_1'])

### Query 75
- Text: What does **COZY CRASHPAD** **SPELL 3** do?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/47']
- Expected found: `True`
- Expected rank: `18`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/47', 'merged::PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/39', 'merged::PZO22001 Starfinder Player Core 294-329::/page/29/Text/2']
- Expanded expected found: `True`
- Expanded expected rank: `18`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/39` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 294-329::/page/29/Text/2` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 406-423::/page/3/Text/39` | 0.535735 | **EQUIPMENT** **SPELLS** |
| 2 | `merged::PZO22001 Starfinder Player Core 442-464::/page/19/Text/83` | 0.535735 | **EQUIPMENT** **SPELLS** |
| 3 | `merged::PZO22001 Starfinder Player Core 406-423::/page/5/Text/52` | 0.535735 | **EQUIPMENT** **SPELLS** |
| 4 | `merged::PZO22001 Starfinder Player Core 406-423::/page/15/Text/18` | 0.535735 | **EQUIPMENT** **SPELLS** |
| 5 | `merged::PZO22001 Starfinder Player Core 442-464::/page/1/Text/58` | 0.535735 | **EQUIPMENT** **SPELLS** |
| 6 | `merged::PZO22001 Starfinder Player Core 364-387::/page/9/Text/57` | 0.535735 | **EQUIPMENT** **SPELLS** |
| 7 | `merged::PZO22001 Starfinder Player Core 364-387::/page/21/Text/54` | 0.535735 | **EQUIPMENT** **SPELLS** |
| 8 | `merged::PZO22001 Starfinder Player Core 294-329::/page/7/Text/33` | 0.535735 | **EQUIPMENT** **SPELLS** |
| 9 | `merged::PZO22001 Starfinder Player Core 406-423::/page/11/Text/25` | 0.535735 | **EQUIPMENT** **SPELLS** |
| 10 | `merged::PZO22001 Starfinder Player Core 150-161::/page/3/Text/51` | 0.535735 | **EQUIPMENT** **SPELLS** |

### Query 76
- Text: Summarize **Constitution**
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 014-029::/page/5/SectionHeader/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 014-029::/page/5/SectionHeader/9', 'merged::PZO22001 Starfinder Player Core 014-029::/page/5/Text/10', 'merged::PZO22001 Starfinder Player Core 014-029::/page/5/Text/8']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 014-029::/page/5/Text/10` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 014-029::/page/5/Text/8` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 014-029::/page/5/SectionHeader/9` | 0.869836 | **Constitution** |
| 2 | `merged::PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/7` | 0.869836 | **Constitution** |
| 3 | `merged::PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/10` | 0.586500 | **10 + Constitution modifier** |
| 4 | `merged::PZO22001 Starfinder Player Core 138-149::/page/1/Text/10` | 0.586500 | **10 + Constitution modifier** |
| 5 | `merged::PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/10` | 0.577806 | **8 + Constitution modifier** |
| 6 | `merged::PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/8` | 0.577806 | **8 + Constitution modifier** |
| 7 | `merged::PZO22001 Starfinder Player Core 150-161::/page/1/Text/8` | 0.451186 | At 1st level, your class gives you  an attribute boost to Constitution. |
| 8 | `merged::PZO22001 Starfinder Player Core 014-029::/page/5/Text/10` | 0.432471 | Constitution measures your character's health and stamina,  and is important for all characters, especially those who  fight in close range. Your Constitution modifier is added to  your Hit Points and |
| 9 | `merged::PZO22001 Starfinder Player Core 014-029::/page/5/Text/32` | 0.432347 | **Religion** |
| 10 | `merged::PZO22001 Starfinder Player Core 014-029::/page/11/Text/31` | 0.432347 | **Religion** |

### Query 77
- Text: What is the rule about **Character Sheet:** Each player needs a character sheet to  create their character and to record what happens to them  during play. You can find a character sheet in the back of this  book and online as a free PDF.?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 001-013::/page/5/Text/13']
- Expected found: `False`
- Expected rank: `None`
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
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 282-293::/page/1/Text/60', 'merged::PZO22001 Starfinder Player Core 282-293::/page/1/Text/61', 'merged::PZO22001 Starfinder Player Core 282-293::/page/1/Text/59']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 282-293::/page/1/Text/61` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 282-293::/page/1/Text/59` (reasons: ['graph_depth_1'])

### Query 79
- Text: Summarize You know better than most the power of electricity,  having survived several close calls yourself, and you know  firsthand how shocking it can be when something goes  wrong. Whether you learned by installing power stations or  repairing broken circuits, you're familiar with the positives  and negatives of electricity.
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 092-097::/page/2/Text/14']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 092-097::/page/2/Text/14', 'merged::PZO22001 Starfinder Player Core 092-097::/page/2/Text/15', 'merged::PZO22001 Starfinder Player Core 092-097::/page/2/SectionHeader/13']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 092-097::/page/2/Text/15` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 092-097::/page/2/SectionHeader/13` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 092-097::/page/2/Text/14` | 0.988598 | You know better than most the power of electricity,  having survived several close calls yourself, and you know  firsthand how shocking it can be when something goes  wrong. Whether you learned by ins |
| 2 | `merged::PZO22001 Starfinder Player Core 442-464::/page/4/Text/41` | 0.513351 | **electricity** (trait) Effects with this trait deal electricity  damage. A creature with this trait has a connection to  magical electricity. |
| 3 | `merged::PZO22001 Starfinder Player Core 210-231::/page/9/Text/21` | 0.480922 | You can fuel battery-powered devices by drawing electricity  from different sources. Doing so takes 1 minute of work and  an adjacent source of power appropriate to the device. If the  source of power |
| 4 | `merged::PZO22001 Starfinder Player Core 098-113::/page/10/Text/8` | 0.465986 | Your savvy and skill are unparalleled. No matter the situation,  you quickly course correct to set the tone you need to succeed.  You gain the following action. |
| 5 | `merged::PZO22001 Starfinder Player Core 182-209::/page/6/Text/26` | 0.461018 | **Success** For an item or location, you get a sense of what it  does and learn any means of activating it. For an ongoing  effect (such as a spell with a duration), you learn the  effect's name and w |
| 6 | `merged::PZO22001 Starfinder Player Core 182-209::/page/14/Text/10` | 0.459165 | **Success** You manage to operate the device in the necessary  manner, including getting basic functionality. You gain  general information from the program. |
| 7 | `merged::PZO22001 Starfinder Player Core 182-209::/page/6/Text/25` | 0.449455 | **Critical Success** You learn all the attributes of the magic,  including its name (for an effect), what it does, any means of  activating it (for an item or location), and whether it's cursed. |
| 8 | `merged::PZO22001 Starfinder Player Core 182-209::/page/24/Text/18` | 0.445234 | You understand the people and systems that make organized  society run, and you know the historical events that make  societies what they are today. Further, you can use that  knowledge to navigate th |
| 9 | `merged::PZO22001 Starfinder Player Core 092-097::/page/4/Text/21` | 0.443007 | You are incredibly knowledgeable, skilled, and perhaps even  trained to teach children and adults about the world and  its wonders. From books to classes, you're committed to  imparting knowledge to a |
| 10 | `merged::PZO22001 Starfinder Player Core 114-125::/page/6/Text/14` | 0.440567 | You're connected to the fount of vitality and void energy that  flows through all living things on every planet. You weave these  energies into spells that heal your allies and harm your enemies. |

### Query 80
- Text: Summarize 2
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/493']
- Expected found: `True`
- Expected rank: `29`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/493', 'merged::PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/492', 'merged::PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/494']
- Expanded expected found: `True`
- Expanded expected rank: `29`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/492` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/494` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/670` | 0.639465 | 2 |
| 2 | `merged::PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/638` | 0.639465 | 2 |
| 3 | `merged::PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/634` | 0.639465 | 2 |
| 4 | `merged::PZO22001 Starfinder Player Core 210-231::/page/5/TableCell/617` | 0.639465 | 2 |
| 5 | `merged::PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/479` | 0.639465 | 2 |
| 6 | `merged::PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/477` | 0.639465 | 2 |
| 7 | `merged::PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/411` | 0.639465 | 2 |
| 8 | `merged::PZO22001 Starfinder Player Core 424-441::/page/6/TableCell/362` | 0.639465 | 2 |
| 9 | `merged::PZO22001 Starfinder Character Sheet::/page/1/TableCell/298` | 0.639465 | 2 |
| 10 | `merged::PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/474` | 0.639465 | 2 |

### Query 81
- Text: Summarize 2
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/390']
- Expected found: `False`
- Expected rank: `None`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/390', 'merged::PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/391', 'merged::PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/389']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/391` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/389` (reasons: ['graph_depth_1'])

### Query 82
- Text: Summarize ABALLON
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 030-039::/page/1/SectionHeader/3']
- Expected found: `False`
- Expected rank: `None`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 030-039::/page/1/SectionHeader/3', 'merged::PZO22001 Starfinder Player Core 030-039::/page/1/Text/2', 'merged::PZO22001 Starfinder Player Core 030-039::/page/1/SectionHeader/4']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 030-039::/page/1/Text/2` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 030-039::/page/1/SectionHeader/4` (reasons: ['graph_depth_1'])

### Query 83
- Text: What is the rule about **Aballon** A rocky, sun-blasted planet of industry which is home to  intelligent machines created by the enigmatic First Ones. 31?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 442-464::/page/0/Text/3']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 442-464::/page/0/Text/3', 'merged::PZO22001 Starfinder Player Core 442-464::/page/0/Text/4', 'merged::PZO22001 Starfinder Player Core 442-464::/page/0/SectionHeader/1']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 442-464::/page/0/Text/4` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 442-464::/page/0/SectionHeader/1` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 442-464::/page/0/Text/3` | 0.907373 | **Aballon** A rocky, sun-blasted planet of industry which is home to  intelligent machines created by the enigmatic First Ones. 31 |
| 2 | `merged::PZO22001 Starfinder Player Core 030-039::/page/1/Text/5` | 0.619340 | Aballon is a rocky, cratered world of superheated metallic  deserts and deep ice wells. Thousands of years before the  Gap, a mysterious civilization called the First Ones utilized  Aballon's abundant |
| 3 | `merged::PZO22001 Starfinder Player Core 030-039::/page/1/SectionHeader/3` | 0.535993 | ABALLON |
| 4 | `merged::PZO22001 Starfinder Player Core 092-097::/page/5/TableCell/511` | 0.513481 | Aballon (anacites, androids) |
| 5 | `merged::PZO22001 Starfinder Player Core 030-039::/page/1/Text/6` | 0.511273 | The largest community on Aballon is Striving, an  industrious megacity containing a citywide neural network  sacred to Triune. Other regions include the industrial forgecity Automatrix; the immense, f |
| 6 | `merged::PZO22001 Starfinder Player Core 442-464::/page/0/Text/6` | 0.505471 | **Absalom Station** A space station which serves as a major hub  of trade and culture in the Pact Worlds. 31 |
| 7 | `merged::PZO22001 Starfinder Player Core 030-039::/page/1/Text/25` | 0.485913 | Floating in lost Golarion's empty orbit, this bustling space  station is the center of interstellar trade and governance  in the Pact Worlds. Nobody knows who built Absalom  Station because it appeare |
| 8 | `merged::PZO22001 Starfinder Player Core 442-464::/page/0/Text/30` | 0.457386 | **Akiton** A red desert planet often defined by its economic  decline due to changes in starship technology. 32 |
| 9 | `merged::PZO22001 Starfinder Player Core 092-097::/page/4/Text/18` | 0.455858 | You know the streets because they raised you. You grew  up scraping by in a massive cityscape like those on Verces  or Castrovel, or on a crowded space station like Absalom  Station. You might have ev |
| 10 | `merged::PZO22001 Starfinder Player Core 030-039::/page/1/Text/1` | 0.445061 | The united worlds are Absalom Station, Aballon, Castrovel,  Akiton, Verces, the Diaspora, Eox, Triaxus, Dykon, Kalo-Mahoi,  Marata, Liavara, and Bretheda. The *Idari*—a starship—is counted  among thei |

### Query 84
- Text: Summarize **GAME**
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 092-097::/page/3/Text/53']
- Expected found: `False`
- Expected rank: `None`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 092-097::/page/3/Text/53', 'merged::PZO22001 Starfinder Player Core 092-097::/page/3/Text/47', 'merged::PZO22001 Starfinder Player Core 092-097::/page/3/Text/48']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 092-097::/page/3/Text/47` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 092-097::/page/3/Text/48` (reasons: ['graph_depth_1'])

### Query 85
- Text: What is the rule about arcane spell list 302–305?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 442-464::/page/1/Text/4']
- Expected found: `True`
- Expected rank: `1`
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
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 040-057::/page/1/ListItem/8', 'merged::PZO22001 Starfinder Player Core 040-057::/page/1/Text/37', 'merged::PZO22001 Starfinder Player Core 040-057::/page/1/Text/7', 'merged::PZO22001 Starfinder Player Core 040-057::/page/11/Text/31', 'merged::PZO22001 Starfinder Player Core 040-057::/page/3/Text/31', 'merged::PZO22001 Starfinder Player Core 040-057::/page/9/Text/51', 'merged::PZO22001 Starfinder Player Core 040-057::/page/1/ListItem/9', 'merged::PZO22001 Starfinder Player Core 040-057::/page/17/Text/56', 'merged::PZO22001 Starfinder Player Core 040-057::/page/5/Text/66', 'merged::PZO22001 Starfinder Player Core 040-057::/page/13/Text/62', 'merged::PZO22001 Starfinder Player Core 040-057::/page/15/Text/32', 'merged::PZO22001 Starfinder Player Core 040-057::/page/7/Text/31']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 040-057::/page/1/Text/37` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 040-057::/page/1/Text/7` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 040-057::/page/11/Text/31` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 040-057::/page/3/Text/31` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 040-057::/page/9/Text/51` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 040-057::/page/1/ListItem/9` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 040-057::/page/17/Text/56` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 040-057::/page/5/Text/66` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 040-057::/page/13/Text/62` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 040-057::/page/15/Text/32` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 040-057::/page/7/Text/31` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 040-057::/page/1/ListItem/8` | 0.949964 | **Ancestries** express the lineage your character hails from.  Within ancestries are heritages—subgroups that have  unique characteristics. An ancestry provides attribute  boosts (and perhaps attribut |
| 2 | `merged::PZO22001 Starfinder Player Core 014-029::/page/9/Text/3` | 0.709607 | **Ancestry:** Each ancestry provides attribute boosts, and sometimes an attribute flaw. If you're taking any voluntary  flaws, apply them in this step (see the sidebar on page 25). |
| 3 | `merged::PZO22001 Starfinder Player Core 442-464::/page/0/Text/38` | 0.686280 | **ancestry** A broad family of people that a creature belongs to.  Each player character chooses an ancestry as the first step of  character creation. 10, 19, 27, **41–91** mixed ancestry 83 |
| 4 | `merged::PZO22001 Starfinder Player Core 014-029::/page/5/Text/19` | 0.672065 | Select an ancestry for your character. The ancestry  summaries on page 27 provide an overview of Starfinder's  core ancestry options, and each is fully detailed in Chapter  2. Ancestry determines your |
| 5 | `merged::PZO22001 Starfinder Player Core 014-029::/page/10/Text/2` | 0.667918 | The attribute boosts and flaws listed in each ancestry  represent general trends or help guide players to  create the kinds of characters from that ancestry most  likely to pursue the life of an adven |
| 6 | `merged::PZO22001 Starfinder Player Core 040-057::/page/1/Text/23` | 0.649851 | **Alternate** **Ancestry** **Boosts:** Because of the wide variety of  people within any ancestry, you can *always* choose to take two  free boosts to represent your character, even if the ancestry  n |
| 7 | `merged::PZO22001 Starfinder Player Core 014-029::/page/4/Text/2` | 0.648186 | On pages 27–28, you'll see a visual representation  of ancestries and classes that provides at-a-glance  information for players looking to make the most of  their starting attribute modifiers. In the |
| 8 | `merged::PZO22001 Starfinder Player Core 040-057::/page/1/Text/21` | 0.647241 | When creating a character of this ancestry, you apply attribute |
| 9 | `merged::PZO22001 Starfinder Player Core 014-029::/page/0/Text/6` | 0.646280 | The rules for ancestries and heritages representing the  Pact Worlds are in this chapter, including their ancestry  feat options. Backgrounds are at the end of this chapter,  along with a section abou |
| 10 | `merged::PZO22001 Starfinder Player Core 040-057::/page/1/Text/29` | 0.644141 | Any other entries in the sidebar represent abilities, senses,  and other qualities all members of the ancestry manifest.  These are omitted for ancestries with no special rules. |

### Query 87
- Text: What are the requirements for **SENSE ABNORMALITIES** **FEAT 12**?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/39']
- Expected found: `False`
- Expected rank: `None`
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
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 268-281::/page/1/Text/67', 'merged::PZO22001 Starfinder Player Core 268-281::/page/1/Text/68', 'merged::PZO22001 Starfinder Player Core 268-281::/page/5/Text/68', 'merged::PZO22001 Starfinder Player Core 268-281::/page/9/Text/25', 'merged::PZO22001 Starfinder Player Core 268-281::/page/11/Text/40', 'merged::PZO22001 Starfinder Player Core 268-281::/page/7/Text/29', 'merged::PZO22001 Starfinder Player Core 268-281::/page/13/Text/39', 'merged::PZO22001 Starfinder Player Core 268-281::/page/1/Text/66']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 268-281::/page/1/Text/68` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 268-281::/page/5/Text/68` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 268-281::/page/9/Text/25` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 268-281::/page/11/Text/40` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 268-281::/page/7/Text/29` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 268-281::/page/13/Text/39` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 268-281::/page/1/Text/66` (reasons: ['graph_depth_1'])

### Query 89
- Text: Summarize IMPRECISE SENSES
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/20']
- Expected found: `True`
- Expected rank: `1`
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
| 4 | `merged::PZO22001 Starfinder Player Core 442-464::/page/6/Text/48` | 0.590450 | **imprecise sense** A sense that can make creatures hidden, but  not observed, such as human hearing. 424 |
| 5 | `merged::PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/25` | 0.523668 | SPECIAL SENSES |
| 6 | `merged::PZO22001 Starfinder Player Core 406-423::/page/3/Text/23` | 0.504023 | if you're using an imprecise sense or if an effect (such as  *invisibility*) prevents the subject from being observed. |
| 7 | `merged::PZO22001 Starfinder Player Core 424-441::/page/0/Text/21` | 0.487243 | Average hearing is an imprecise sense—it can't detect the  full range of detail that a precise sense can. You can usually  sense a creature automatically with an imprecise sense, but  it has the hidde |
| 8 | `merged::PZO22001 Starfinder Player Core 098-113::/page/9/SectionHeader/34` | 0.483176 | INCREDIBLE SENSES 17TH |
| 9 | `merged::PZO22001 Starfinder Player Core 424-441::/page/0/Text/16` | 0.480563 | The ways a creature can use Perception depend on what  senses it has. The primary concepts you need to know for  understanding senses are precise senses, imprecise senses,  and the three states of det |
| 10 | `merged::PZO22001 Starfinder Player Core 442-464::/page/15/TableCell/107` | 0.453978 | Senses and No |

### Query 90
- Text: What is the rule about Attribute boosts, skill feat, solarian feat?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/409']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/409', 'merged::PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/410', 'merged::PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/408']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/410` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/408` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/429` | 0.862263 | Attribute boosts, skill feat, solarian feat |
| 2 | `merged::PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/409` | 0.862263 | Attribute boosts, skill feat, solarian feat |
| 3 | `merged::PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/421` | 0.700242 | Skill feat, solarian feat |
| 4 | `merged::PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/401` | 0.700242 | Skill feat, solarian feat |
| 5 | `merged::PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/405` | 0.700242 | Skill feat, solarian feat |
| 6 | `merged::PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/425` | 0.700242 | Skill feat, solarian feat |
| 7 | `merged::PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/417` | 0.700242 | Skill feat, solarian feat |
| 8 | `merged::PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/393` | 0.700242 | Skill feat, solarian feat |
| 9 | `merged::PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/397` | 0.700242 | Skill feat, solarian feat |
| 10 | `merged::PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/413` | 0.700242 | Skill feat, solarian feat |

### Query 91
- Text: What are the requirements for **Prerequisites** Center Thoughts?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 058-073::/page/3/Text/48']
- Expected found: `False`
- Expected rank: `None`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 058-073::/page/3/Text/48', 'merged::PZO22001 Starfinder Player Core 058-073::/page/3/Text/47', 'merged::PZO22001 Starfinder Player Core 058-073::/page/3/Text/49']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 058-073::/page/3/Text/47` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 058-073::/page/3/Text/49` (reasons: ['graph_depth_1'])

### Query 92
- Text: What are the requirements for **HAMPERING FLARE **[one-action] **FEAT 1**?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/8']
- Expected found: `False`
- Expected rank: `None`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/8', 'merged::PZO22001 Starfinder Player Core 138-149::/page/5/Text/7', 'merged::PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/10']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 138-149::/page/5/Text/7` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/10` (reasons: ['graph_depth_1'])

### Query 93
- Text: Summarize **GLOSSARY & ** **INDEX**
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 138-149::/page/1/Text/47']
- Expected found: `True`
- Expected rank: `45`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 138-149::/page/1/Text/47', 'merged::PZO22001 Starfinder Player Core 138-149::/page/1/Text/48', 'merged::PZO22001 Starfinder Player Core 138-149::/page/1/Text/46']
- Expanded expected found: `True`
- Expanded expected rank: `45`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 138-149::/page/1/Text/48` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 138-149::/page/1/Text/46` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 040-057::/page/15/Text/54` | 0.943465 | **GLOSSARY & ** **INDEX** |
| 2 | `merged::PZO22001 Starfinder Player Core 040-057::/page/13/Text/83` | 0.943465 | **GLOSSARY & ** **INDEX** |
| 3 | `merged::PZO22001 Starfinder Player Core 364-387::/page/23/Text/48` | 0.943465 | **GLOSSARY & ** **INDEX** |
| 4 | `merged::PZO22001 Starfinder Player Core 442-464::/page/9/Text/54` | 0.943465 | **GLOSSARY & ** **INDEX** |
| 5 | `merged::PZO22001 Starfinder Player Core 162-173::/page/11/Text/46` | 0.943465 | **GLOSSARY & ** **INDEX** |
| 6 | `merged::PZO22001 Starfinder Player Core 364-387::/page/17/Text/34` | 0.943465 | **GLOSSARY & ** **INDEX** |
| 7 | `merged::PZO22001 Starfinder Player Core 040-057::/page/9/Text/73` | 0.943465 | **GLOSSARY & ** **INDEX** |
| 8 | `merged::PZO22001 Starfinder Player Core 424-441::/page/5/Text/58` | 0.943465 | **GLOSSARY & ** **INDEX** |
| 9 | `merged::PZO22001 Starfinder Player Core 424-441::/page/1/Text/51` | 0.943465 | **GLOSSARY & ** **INDEX** |
| 10 | `merged::PZO22001 Starfinder Player Core 424-441::/page/3/Text/49` | 0.943465 | **GLOSSARY & ** **INDEX** |

### Query 94
- Text: What are the requirements for **VOID BLOOD** **FEAT 5**?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 074-091::/page/13/Text/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 074-091::/page/13/Text/6', 'merged::PZO22001 Starfinder Player Core 074-091::/page/13/Text/8', 'merged::PZO22001 Starfinder Player Core 074-091::/page/13/Text/5']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 074-091::/page/13/Text/8` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 074-091::/page/13/Text/5` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 074-091::/page/13/Text/6` | 0.834308 | **VOID BLOOD** **FEAT 5** |
| 2 | `merged::PZO22001 Starfinder Player Core 074-091::/page/3/SectionHeader/4` | 0.570660 | **BLOOD SENSE** **FEAT 5** |
| 3 | `merged::PZO22001 Starfinder Player Core 074-091::/page/12/SectionHeader/36` | 0.463826 | **SOUL SUSTENANCE** **FEAT 5** |
| 4 | `merged::PZO22001 Starfinder Player Core 074-091::/page/16/SectionHeader/7` | 0.454194 | **DRIFT HOP **[one-action] **FEAT 5** |
| 5 | `merged::PZO22001 Starfinder Player Core 114-125::/page/8/SectionHeader/41` | 0.450087 | **WILD BOND** **FEAT 2** |
| 6 | `merged::PZO22001 Starfinder Player Core 126-137::/page/6/SectionHeader/42` | 0.444989 | **BLOODY WOUNDS** **FEAT 4** |
| 7 | `merged::PZO22001 Starfinder Player Core 074-091::/page/16/SectionHeader/12` | 0.444459 | **ELECTRICAL SHIELDING** **FEAT 5** |
| 8 | `merged::PZO22001 Starfinder Player Core 074-091::/page/12/SectionHeader/1` | 0.443802 | **HEADSTRONG** **FEAT 1** |
| 9 | `merged::PZO22001 Starfinder Player Core 074-091::/page/7/Text/16` | 0.434078 | **PREHENSILE TAIL** **FEAT 5** |
| 10 | `merged::PZO22001 Starfinder Player Core 074-091::/page/12/SectionHeader/32` | 0.430709 | **DEATHLY CONSTITUTION** **FEAT 5** |

### Query 95
- Text: What is the rule about If you're a prepared spellcaster—such as a technomancer  (see *Starfinder Tech Core*)—you must spend time each day  preparing spells for that day. At the start of your daily  preparations, you select a number of spells of different  spell ranks, determined by your character level and class.  Your spells remain prepared until you cast them or until you  prepare spells again.?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 294-329::/page/1/Text/8']
- Expected found: `True`
- Expected rank: `1`
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
| 6 | `merged::PZO22001 Starfinder Player Core 294-329::/page/6/Text/16` | 0.613399 | If a spell's duration says it lasts until your next daily  preparations, on the next day you can refrain from preparing  a new spell in that spell's slot. (If you are a spontaneous caster,  you can in |
| 7 | `merged::PZO22001 Starfinder Player Core 040-057::/page/9/Text/23` | 0.608685 | Your songs become more complex and tinged with greater  magic. Each day during your daily preparations, you can  choose one common 2nd-rank spell from the occult spell list.  You can cast this spell a |
| 8 | `merged::PZO22001 Starfinder Player Core 182-209::/page/8/Text/24` | 0.588181 | If you have a spell repertoire, such as the mystic or  witchwarper do, a spell you learn isn't automatically added  since you can only know a limited number of spells. Instead,  you can select it when |
| 9 | `merged::PZO22001 Starfinder Player Core 294-329::/page/7/Text/4` | 0.566996 | Sometimes you need to identify a spell, especially if its  effects aren't obvious right away. If you notice a spell  being cast, and you have that spell in your repertoire  or prepared it that day (ev |
| 10 | `merged::PZO22001 Starfinder Player Core 014-029::/page/0/Text/16` | 0.566335 | This chapter starts with rules for casting spells,  determining their effects, and negating foes' spells  (called counteracting). After that, the spell lists for  each spellcasting tradition are inclu |

### Query 96
- Text: What are the requirements for **CONFOUNDING DISQUISITION **[two-actions] **FEAT 8**?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/22']
- Expected found: `False`
- Expected rank: `None`
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
| 4 | `merged::PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/25` | 0.511379 | **STELLAR RUSH **[two-actions] **FEAT 1** |
| 5 | `merged::PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/34` | 0.488161 | **CONCEAL SPELL **[one-action] **FEAT 2** |
| 6 | `merged::PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/15` | 0.481660 | **REACH SPELL **[one-action] **FEAT 1** |
| 7 | `merged::PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/68` | 0.478011 | **SYNAPTIC PULSE **[two-actions] **SPELL 5**  **CONCENTRATE** **INCAPACITATION** **MANIPULATE** **MENTAL**  **Traditions** occult **Area** 30-foot emanation **Defense** Will; **Duration** 1 round |
| 8 | `merged::PZO22001 Starfinder Player Core 210-231::/page/17/SectionHeader/1` | 0.464473 | **RECOGNIZE SPELL **[reaction] **FEAT 1** |
| 9 | `merged::PZO22001 Starfinder Player Core 138-149::/page/8/SectionHeader/5` | 0.462038 | **CORONA **[two-actions] **FEAT 6** |
| 10 | `merged::PZO22001 Starfinder Player Core 162-173::/page/7/SectionHeader/27` | 0.457324 | **OTHERWORLDLY SPELL **[one-action] **FEAT 1** |

### Query 98
- Text: What is the rule about beyond the Universe. Mystics connected with the cosmic  forces of healing and shadows are divine spellcasters.?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 294-329::/page/3/Text/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 294-329::/page/3/Text/11', 'merged::PZO22001 Starfinder Player Core 294-329::/page/3/Text/10', 'merged::PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/13']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 294-329::/page/3/Text/10` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/13` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 294-329::/page/3/Text/11` | 0.927953 | beyond the Universe. Mystics connected with the cosmic  forces of healing and shadows are divine spellcasters. |
| 2 | `merged::PZO22001 Starfinder Player Core 114-125::/page/2/Text/9` | 0.653563 | All mystics have a supernatural connection with a cosmic force  that grants magical powers. The exact nature of your connection  can vary widely—you might worship a god or pantheon, embody  a metaphys |
| 3 | `merged::PZO22001 Starfinder Player Core 098-113::/page/3/Text/24` | 0.641832 | The mystic is a spellcaster with a connection  to a divine, occult, or primal aspect of the universe. A  mystic casts powerful spells, learning new epiphanies  based on their chosen connection, and he |
| 4 | `merged::PZO22001 Starfinder Player Core 294-329::/page/1/Text/3` | 0.606783 | Even with the widespread presence of technology,  spellcasters can be found in every corner of the galaxy.  Some spellcasters draw magic from other realities, some  from their mystical connections to |
| 5 | `merged::PZO22001 Starfinder Player Core 114-125::/page/3/Text/3` | 0.593502 | You are a spellcaster and can cast spells using the Cast a Spell  activity (see Casting Spells on page 298). As a mystic, when  you cast spells, you might intone a prayer or hum a song  inspired by yo |
| 6 | `merged::PZO22001 Starfinder Player Core 294-329::/page/3/Text/15` | 0.588439 | systematic way. Witchwarpers touched by the Gap or  alternate timelines, as well as mystics who are psychically  linked to the Akashic Record, are occult spellcasters. |
| 7 | `merged::PZO22001 Starfinder Player Core 294-329::/page/3/Text/18` | 0.566392 | An instinctual connection to and faith in the  world, the cycle of day and night, the turning  of the seasons, and the natural selection of predator and  prey drive the primal tradition. Mystics conne |
| 8 | `merged::PZO22001 Starfinder Player Core 030-039::/page/5/Text/4` | 0.529415 | Anyone can worship a deity, but those who do so devoutly  should take care to pursue the faith's edicts (behaviors  the faith encourages) and avoid its anathemas (actions  considered blasphemous). Eac |
| 9 | `merged::PZO22001 Starfinder Player Core 030-039::/page/5/Text/1` | 0.524122 | Technology and scientific knowledge flourish across the galaxy, but these advancements can't  solve every problem or answer all existential questions. Many turn to religion to understand their  place |
| 10 | `merged::PZO22001 Starfinder Player Core 030-039::/page/0/ListItem/9` | 0.522290 | **The galaxy** **is magical.** Proof of people who magically  change reality and channel the primeval forces of the  universe is everywhere, and people know that it's  real. Magic and technology often |

### Query 99
- Text: Summarize these stones are purportedly all fragments of crystal tools  used by otherworldly entities to build the Universe in  ancient times.
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 282-293::/page/1/Text/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 282-293::/page/1/Text/1', 'merged::PZO22001 Starfinder Player Core 282-293::/page/1/Text/2', 'merged::PZO22001 Starfinder Player Core 282-293::/page/0/Text/26']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 282-293::/page/1/Text/2` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 282-293::/page/0/Text/26` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 282-293::/page/1/Text/1` | 0.985694 | these stones are purportedly all fragments of crystal tools  used by otherworldly entities to build the Universe in  ancient times. |
| 2 | `merged::PZO22001 Starfinder Player Core 282-293::/page/1/Text/3` | 0.527434 | There are various types of *aeon stones*, each with a  different appearance and magical effect. Each *aeon stone* also  gains a resonant power when slotted into specific items, such  as weapons with t |
| 3 | `merged::PZO22001 Starfinder Player Core 330-363::/page/32/SectionHeader/32` | 0.478911 | **SPEAK WITH STONES **[two-actions] **SPELL 5**  **CONCENTRATE** **EARTH** **MANIPULATE**  **Traditions** divine, occult, primal  **Duration** 1 hour  You can ask questions of and receive answers from |
| 4 | `merged::PZO22001 Starfinder Player Core 294-329::/page/18/Text/17` | 0.464989 | **Speak with Stones**H Communicate with natural and worked  stone. |
| 5 | `merged::PZO22001 Starfinder Player Core 294-329::/page/15/Text/52` | 0.464989 | **Speak with Stones**H Communicate with natural and worked  stone. |
| 6 | `merged::PZO22001 Starfinder Player Core 294-329::/page/12/Text/61` | 0.464989 | **Speak with Stones**H Communicate with natural and worked  stone. |
| 7 | `merged::PZO22001 Starfinder Player Core 294-329::/page/18/Text/2` | 0.460604 | **Shape Stone** Reshape a cube of stone. |
| 8 | `merged::PZO22001 Starfinder Player Core 294-329::/page/10/Text/7` | 0.460604 | **Shape Stone** Reshape a cube of stone. |
| 9 | `merged::PZO22001 Starfinder Player Core 294-329::/page/10/Text/33` | 0.459346 | **Wall of Stone**H Shape a wall of stone. |
| 10 | `merged::PZO22001 Starfinder Player Core 294-329::/page/18/Text/22` | 0.459346 | **Wall of Stone**H Shape a wall of stone. |

### Query 100
- Text: Summarize **Leveling Up**
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 014-029::/page/5/Text/30']
- Expected found: `False`
- Expected rank: `None`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 014-029::/page/5/Text/30', 'merged::PZO22001 Starfinder Player Core 014-029::/page/5/Text/31', 'merged::PZO22001 Starfinder Player Core 014-029::/page/5/Text/29']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 014-029::/page/5/Text/31` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 014-029::/page/5/Text/29` (reasons: ['graph_depth_1'])

### Query 101
- Text: What is the rule about **SKILLS** **FEATS**?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 250-267::/page/1/Text/23']
- Expected found: `True`
- Expected rank: `10`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 250-267::/page/1/Text/23', 'merged::PZO22001 Starfinder Player Core 250-267::/page/1/Text/24', 'merged::PZO22001 Starfinder Player Core 250-267::/page/1/Text/22']
- Expanded expected found: `True`
- Expanded expected rank: `10`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 250-267::/page/1/Text/24` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 250-267::/page/1/Text/22` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 250-267::/page/7/Text/5` | 0.859736 | **SKILLS** **FEATS** |
| 2 | `merged::PZO22001 Starfinder Player Core 098-113::/page/5/Text/42` | 0.859736 | **SKILLS** **FEATS** |
| 3 | `merged::PZO22001 Starfinder Player Core 250-267::/page/5/Text/29` | 0.859736 | **SKILLS** **FEATS** |
| 4 | `merged::PZO22001 Starfinder Player Core 098-113::/page/3/Text/15` | 0.859736 | **SKILLS** **FEATS** |
| 5 | `merged::PZO22001 Starfinder Player Core 098-113::/page/9/Text/48` | 0.859736 | **SKILLS** **FEATS** |
| 6 | `merged::PZO22001 Starfinder Player Core 098-113::/page/7/Text/58` | 0.859736 | **SKILLS** **FEATS** |
| 7 | `merged::PZO22001 Starfinder Player Core 092-097::/page/1/Text/60` | 0.859736 | **SKILLS** **FEATS** |
| 8 | `merged::PZO22001 Starfinder Player Core 098-113::/page/13/Text/66` | 0.859736 | **SKILLS** **FEATS** |
| 9 | `merged::PZO22001 Starfinder Player Core 098-113::/page/1/Text/31` | 0.859736 | **SKILLS** **FEATS** |
| 10 | `merged::PZO22001 Starfinder Player Core 250-267::/page/1/Text/23` | 0.859736 | **SKILLS** **FEATS** |

### Query 102
- Text: What is the rule about **Activate—Defensive Detonation **[one-action] (manipulate) **Requirements** You have a stored grenade; **Effect** You detonate the grenade  stored in the explosive defense unit. The explosion is centered  on your space, but the upgrade generates a containment  field to protect you from its effects. The grenade otherwise  functions as if you'd activated it normally.?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 268-281::/page/1/Text/58']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 268-281::/page/1/Text/58', 'merged::PZO22001 Starfinder Player Core 268-281::/page/1/Text/57', 'merged::PZO22001 Starfinder Player Core 268-281::/page/1/Text/60']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 268-281::/page/1/Text/57` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 268-281::/page/1/Text/60` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 268-281::/page/1/Text/58` | 0.925745 | **Activate—Defensive Detonation **[one-action] (manipulate) **Requirements** You have a stored grenade; **Effect** You detonate the grenade  stored in the explosive defense unit. The explosion is cent |
| 2 | `merged::PZO22001 Starfinder Player Core 268-281::/page/1/Text/57` | 0.784591 | **Activate—Store Grenade** [two-actions] (manipulate) **Effect** You place a  grenade inside a reinforced compartment in the explosive  defense unit. You can Interact to retrieve the grenade  normally |
| 3 | `merged::PZO22001 Starfinder Player Core 268-281::/page/7/Text/18` | 0.646655 | **Activate—Launch** [one-action] (attack) **Effect** You launch the loaded  grenade. |
| 4 | `merged::PZO22001 Starfinder Player Core 268-281::/page/5/Text/29` | 0.598482 | **Activate—Fireburst Mode** [one-action] (manipulate) **Effect** The grenade  launcher or the undermounted grenade launcher gains  the area (cone) trait with a range of 15 feet and uses the |
| 5 | `merged::PZO22001 Starfinder Player Core 126-137::/page/10/Text/54` | 0.592727 | You attempt to detonate the grenade with a well-timed shot  from your gun. Expend an amount of ammunition from your  gun equal to its usage, as if you'd fired the gun. You gain a +4  circumstance bonu |
| 6 | `merged::PZO22001 Starfinder Player Core 268-281::/page/2/Text/2` | 0.556305 | **Activate—Raise Force Field** [one-action] (manipulate) **Frequency** three  times per day; **Effect** Your force field becomes active. It  remains active for 1 minute or until it's reduced to 0 Hit |
| 7 | `merged::PZO22001 Starfinder Player Core 268-281::/page/4/Text/5` | 0.547264 | Most upgrades grant their benefits continually so long as  you're wielding the weapon they're installed in. Others  produce their effects only when used properly in the moment  by spending actions. An |
| 8 | `merged::PZO22001 Starfinder Player Core 268-281::/page/1/Text/56` | 0.538699 | Reinforced custom armor plates automatically generate a  containment field to protect you from nearby explosions,  granting you resistance 2 to area damage (acid, cold,  electricity, and fire damage o |
| 9 | `merged::PZO22001 Starfinder Player Core 268-281::/page/0/Text/9` | 0.534624 | Most upgrades grant their benefits continually so long as  you're properly wearing the armor they're installed in. Others  produce their effects only when used properly in the moment  by spending acti |
| 10 | `merged::PZO22001 Starfinder Player Core 268-281::/page/12/Text/3` | 0.531725 | An item with the grenade trait can be thrown with a range of 70  feet using the Area Fire action (page 410) as though it had the  area (burst) trait at the listed radius using a single action instead |

### Query 103
- Text: What are the requirements for **REMIX WORLD'S RHYTHM** **FEAT 13**?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/37']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/37', 'merged::PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/36', 'merged::PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/39']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/36` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/39` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/37` | 0.841289 | **REMIX WORLD'S RHYTHM** **FEAT 13** |
| 2 | `merged::PZO22001 Starfinder Player Core 074-091::/page/17/SectionHeader/25` | 0.486164 | **FREQUENT DRIFTER** **FEAT 13** |
| 3 | `merged::PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/43` | 0.478744 | **LINGUISTIC MASTER** **FEAT 13** |
| 4 | `merged::PZO22001 Starfinder Player Core 074-091::/page/17/SectionHeader/30` | 0.473384 | **SCRAMBLE TECH** **FEAT 13** |
| 5 | `merged::PZO22001 Starfinder Player Core 058-073::/page/15/SectionHeader/48` | 0.468925 | **SUPERSONIC SPEED** **FEAT 13** |
| 6 | `merged::PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/34` | 0.468701 | **FOCUS PHEROMONES **[one-action] **FEAT 13** |
| 7 | `merged::PZO22001 Starfinder Player Core 058-073::/page/15/SectionHeader/38` | 0.447656 | **CHATTERMANDER** **FEAT 13** |
| 8 | `merged::PZO22001 Starfinder Player Core 074-091::/page/17/Text/14` | 0.440837 | **DRIFT BLINK **[reaction] **FEAT 13** |
| 9 | `merged::PZO22001 Starfinder Player Core 074-091::/page/3/SectionHeader/48` | 0.436797 | **OVERCOME SHAME **[free-action] **FEAT 13** |
| 10 | `merged::PZO22001 Starfinder Player Core 074-091::/page/13/SectionHeader/30` | 0.430876 | **INTUITIVE TALENT **[free-action] **FEAT 13** |

### Query 104
- Text: Summarize Shield Block
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/450']
- Expected found: `False`
- Expected rank: `None`
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
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 330-363::/page/4/SectionHeader/2', 'merged::PZO22001 Starfinder Player Core 330-363::/page/4/Text/1', 'merged::PZO22001 Starfinder Player Core 330-363::/page/4/SectionHeader/10']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 330-363::/page/4/Text/1` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 330-363::/page/4/SectionHeader/10` (reasons: ['graph_depth_1'])

### Query 106
- Text: What is the rule about Spellcasting classes grant a proficiency rank for spell  attacks and DCs, which are further detailed in each class's  entry. These classes rarely use their class DC.?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 098-113::/page/2/Text/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 098-113::/page/2/Text/7', 'merged::PZO22001 Starfinder Player Core 098-113::/page/2/Text/8', 'merged::PZO22001 Starfinder Player Core 098-113::/page/2/Text/6']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 098-113::/page/2/Text/8` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 098-113::/page/2/Text/6` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 098-113::/page/2/Text/7` | 0.938933 | Spellcasting classes grant a proficiency rank for spell  attacks and DCs, which are further detailed in each class's  entry. These classes rarely use their class DC. |
| 2 | `merged::PZO22001 Starfinder Player Core 098-113::/page/2/Text/6` | 0.643566 | A proficiency rank can unlock various feats and class  features, and it also helps determine the modifier for any  check you roll or DC you calculate related to that statistic.  If your character is t |
| 3 | `merged::PZO22001 Starfinder Player Core 098-113::/page/2/Text/5` | 0.639863 | Each class entry specifies your character's initial  proficiency rank in Perception, saving throws, attacks,  defenses, and class DC. You gain the trained proficiency  rank in several skills. The exac |
| 4 | `merged::PZO22001 Starfinder Player Core 174-181::/page/0/Text/18` | 0.637886 | **Expert Spellcasting Feat:** Typically taken at 12th level,  these feats make you an expert in spell attack modifiers  and spell DCs and grant you a 4th-rank spell slot. If you  have a spell repertoi |
| 5 | `merged::PZO22001 Starfinder Player Core 098-113::/page/1/Text/15` | 0.633872 | For instance, this is the attribute modifier you'll use to  determine the Difficulty Class (DC) associated with your  character's class features and feats. This is called your  class DC. If your chara |
| 6 | `merged::PZO22001 Starfinder Player Core 174-181::/page/0/Text/19` | 0.631424 | **Master Spellcasting Feat:** Usually found at 18th level, these  feats make you a master in spell attack modifiers and spell  DCs and grant you a 7th-rank spell slot. If you have a spell  repertoire, |
| 7 | `merged::PZO22001 Starfinder Player Core 294-329::/page/3/Text/21` | 0.626835 | If you get focus spells from a class or other source that  doesn't grant spellcasting ability, the ability that gives you  focus spells also provides your proficiency for your spell  attack modifier a |
| 8 | `merged::PZO22001 Starfinder Player Core 014-029::/page/11/Text/15` | 0.620528 | A class DC sets the difficulty for certain abilities granted  by your character's class. This DC equals 10 plus their  proficiency bonus for their class DC (+3 for most 1st-level  characters) plus the |
| 9 | `merged::PZO22001 Starfinder Player Core 098-113::/page/2/Text/8` | 0.617980 | If something isn't listed in your character's class entry,  their proficiency rank in that statistic is untrained unless  they gain training from another source. If your character  is untrained in som |
| 10 | `merged::PZO22001 Starfinder Player Core 442-464::/page/12/Text/31` | 0.609286 | **spell DC** Your spell DC measures how hard it is to resist your  spells with saving throws or to counteract them. Spell DC  = 10 + spellcasting attribute modifier + proficiency bonus +  other bonuse |

### Query 107
- Text: What is the rule about **Trigger** A creature Casts a Spell with the mental trait.?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 058-073::/page/3/Text/54']
- Expected found: `False`
- Expected rank: `None`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 058-073::/page/3/Text/54', 'merged::PZO22001 Starfinder Player Core 058-073::/page/3/Text/53', 'merged::PZO22001 Starfinder Player Core 058-073::/page/3/Text/55']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 058-073::/page/3/Text/53` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 058-073::/page/3/Text/55` (reasons: ['graph_depth_1'])

### Query 108
- Text: Summarize Mystic envoys can choose between using their magic  or directives to empower their allies, widening the  breadth of options available to them.
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 174-181::/page/1/ListItem/5']
- Expected found: `False`
- Expected rank: `None`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 174-181::/page/1/ListItem/5', 'merged::PZO22001 Starfinder Player Core 174-181::/page/1/ListItem/6', 'merged::PZO22001 Starfinder Player Core 174-181::/page/1/Text/4']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 174-181::/page/1/ListItem/6` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 174-181::/page/1/Text/4` (reasons: ['graph_depth_1'])

### Query 109
- Text: What are the requirements for **WORMHOLE **[two-actions] **FEAT 12**?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 138-149::/page/10/SectionHeader/11']
- Expected found: `False`
- Expected rank: `None`
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
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/19', 'merged::PZO22001 Starfinder Player Core 098-113::/page/14/Text/21', 'merged::PZO22001 Starfinder Player Core 098-113::/page/14/Text/18']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 098-113::/page/14/Text/21` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 098-113::/page/14/Text/18` (reasons: ['graph_depth_1'])

### Query 111
- Text: What is the rule about **Type **tactical; **Level **19; **Price **350,000 credits?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 268-281::/page/2/Text/31']
- Expected found: `False`
- Expected rank: `None`
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
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/16', 'merged::PZO22001 Starfinder Player Core 294-329::/page/4/Text/17', 'merged::PZO22001 Starfinder Player Core 294-329::/page/4/Text/15']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 294-329::/page/4/Text/17` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 294-329::/page/4/Text/15` (reasons: ['graph_depth_1'])

### Query 113
- Text: What are the requirements for **CROWD CONTROL** **FEAT 2**?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 210-231::/page/8/Text/17']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 210-231::/page/8/Text/17', 'merged::PZO22001 Starfinder Player Core 210-231::/page/8/Text/19', 'merged::PZO22001 Starfinder Player Core 210-231::/page/8/Text/16']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 210-231::/page/8/Text/19` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 210-231::/page/8/Text/16` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 210-231::/page/8/Text/17` | 0.869761 | **CROWD CONTROL** **FEAT 2** |
| 2 | `merged::PZO22001 Starfinder Player Core 210-231::/page/8/Text/26` | 0.584927 | **CROWD SURFING** **FEAT 1** |
| 3 | `merged::PZO22001 Starfinder Player Core 210-231::/page/10/SectionHeader/22` | 0.547566 | **FACE IN THE CROWD** **FEAT 1** |
| 4 | `merged::PZO22001 Starfinder Player Core 210-231::/page/7/Text/17` | 0.535054 | **BREATH CONTROL** **FEAT 1** |
| 5 | `merged::PZO22001 Starfinder Player Core 210-231::/page/14/SectionHeader/34` | 0.533952 | **NIMBLE CRAWL** **FEAT 2** |
| 6 | `merged::PZO22001 Starfinder Player Core 210-231::/page/19/SectionHeader/26` | 0.487995 | **TECH CRAFTING** **FEAT 2** |
| 7 | `merged::PZO22001 Starfinder Player Core 210-231::/page/12/SectionHeader/41` | 0.473361 | **INVENTOR** **FEAT 2** |
| 8 | `merged::PZO22001 Starfinder Player Core 330-363::/page/25/Text/59` | 0.440394 | **FEATS** **EQUIPMENT** |
| 9 | `merged::PZO22001 Starfinder Player Core 232-249::/page/9/Text/21` | 0.440394 | **FEATS** **EQUIPMENT** |
| 10 | `merged::PZO22001 Starfinder Player Core 330-363::/page/27/Text/61` | 0.440394 | **FEATS** **EQUIPMENT** |

### Query 114
- Text: Summarize **UNCOMMON**
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 092-097::/page/1/SectionHeader/32']
- Expected found: `False`
- Expected rank: `None`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 092-097::/page/1/SectionHeader/32', 'merged::PZO22001 Starfinder Player Core 092-097::/page/1/Text/33', 'merged::PZO22001 Starfinder Player Core 092-097::/page/1/SectionHeader/31']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 092-097::/page/1/Text/33` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 092-097::/page/1/SectionHeader/31` (reasons: ['graph_depth_1'])

### Query 115
- Text: What is the rule about An instinctual connection to and faith in the  world, the cycle of day and night, the turning  of the seasons, and the natural selection of predator and  prey drive the primal tradition. Mystics connected to  the primordial elements and underlying rhythms of the  cosmos are primal spellcasters.?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 294-329::/page/3/Text/18']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 294-329::/page/3/Text/18', 'merged::PZO22001 Starfinder Player Core 294-329::/page/3/Text/19', 'merged::PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/17']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 294-329::/page/3/Text/19` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/17` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 294-329::/page/3/Text/18` | 0.953244 | An instinctual connection to and faith in the  world, the cycle of day and night, the turning  of the seasons, and the natural selection of predator and  prey drive the primal tradition. Mystics conne |
| 2 | `merged::PZO22001 Starfinder Player Core 114-125::/page/6/Text/7` | 0.620077 | **Tradition** primal; **Connection Skill** Nature |
| 3 | `merged::PZO22001 Starfinder Player Core 114-125::/page/2/Text/9` | 0.610927 | All mystics have a supernatural connection with a cosmic force  that grants magical powers. The exact nature of your connection  can vary widely—you might worship a god or pantheon, embody  a metaphys |
| 4 | `merged::PZO22001 Starfinder Player Core 114-125::/page/10/Text/4` | 0.587762 | **Prerequisites** connection with primal spellcasting |
| 5 | `merged::PZO22001 Starfinder Player Core 114-125::/page/7/Text/29` | 0.587762 | **Prerequisites** connection with primal spellcasting |
| 6 | `merged::PZO22001 Starfinder Player Core 114-125::/page/8/Text/44` | 0.587762 | **Prerequisites** connection with primal spellcasting |
| 7 | `merged::PZO22001 Starfinder Player Core 442-464::/page/7/Text/59` | 0.584614 | **magical tradition** Arcane, divine, occult, and primal are the  traditions of magic. 297 |
| 8 | `merged::PZO22001 Starfinder Player Core 294-329::/page/3/Text/11` | 0.564251 | beyond the Universe. Mystics connected with the cosmic  forces of healing and shadows are divine spellcasters. |
| 9 | `merged::PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/389` | 0.552652 | Ancestry and background, attribute boosts, initial proficiencies, connection, initial epiphany, mystic bond, vitality network, mystic spellcasting, spell repertoire |
| 10 | `merged::PZO22001 Starfinder Player Core 294-329::/page/3/Text/3` | 0.552282 | Your class determines which tradition of magic your spells use. In some cases, such as when a mystic gains spells from  their connection or when a witchwarper learns spells from their paradox, you mig |

### Query 116
- Text: Summarize 4
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/394']
- Expected found: `False`
- Expected rank: `None`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/394', 'merged::PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/395', 'merged::PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/393']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/395` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/393` (reasons: ['graph_depth_1'])

### Query 117
- Text: What is the rule about **SKILLS**?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 424-441::/page/1/Text/29']
- Expected found: `True`
- Expected rank: `29`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 424-441::/page/1/Text/29', 'merged::PZO22001 Starfinder Player Core 424-441::/page/1/Text/28', 'merged::PZO22001 Starfinder Player Core 424-441::/page/1/Text/30']
- Expanded expected found: `True`
- Expanded expected rank: `29`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 424-441::/page/1/Text/28` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 424-441::/page/1/Text/30` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 210-231::/page/3/Text/6` | 0.814442 | **SKILLS** |
| 2 | `merged::PZO22001 Starfinder Player Core 406-423::/page/9/Text/26` | 0.814442 | **SKILLS** |
| 3 | `merged::PZO22001 Starfinder Player Core 442-464::/page/13/Text/56` | 0.814442 | **SKILLS** |
| 4 | `merged::PZO22001 Starfinder Player Core 424-441::/page/17/Text/29` | 0.814442 | **SKILLS** |
| 5 | `merged::PZO22001 Starfinder Player Core 442-464::/page/9/Text/48` | 0.814442 | **SKILLS** |
| 6 | `merged::PZO22001 Starfinder Player Core 182-209::/page/27/Text/39` | 0.814442 | **SKILLS** |
| 7 | `merged::PZO22001 Starfinder Player Core 406-423::/page/7/Text/30` | 0.814442 | **SKILLS** |
| 8 | `merged::PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/56` | 0.814442 | **SKILLS** |
| 9 | `merged::PZO22001 Starfinder Player Core 424-441::/page/7/Text/48` | 0.814442 | **SKILLS** |
| 10 | `merged::PZO22001 Starfinder Player Core 182-209::/page/5/Text/23` | 0.814442 | **SKILLS** |

### Query 118
- Text: What is the rule about **Spell Lists**?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 364-387::/page/5/Text/73']
- Expected found: `True`
- Expected rank: `20`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 364-387::/page/5/Text/73', 'merged::PZO22001 Starfinder Player Core 364-387::/page/5/Text/72', 'merged::PZO22001 Starfinder Player Core 364-387::/page/5/Text/74']
- Expanded expected found: `True`
- Expanded expected rank: `20`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 364-387::/page/5/Text/72` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 364-387::/page/5/Text/74` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 364-387::/page/9/Text/58` | 0.840837 | **Spell Lists** |
| 2 | `merged::PZO22001 Starfinder Player Core 294-329::/page/5/Text/27` | 0.840837 | **Spell Lists** |
| 3 | `merged::PZO22001 Starfinder Player Core 294-329::/page/1/Text/25` | 0.840837 | **Spell Lists** |
| 4 | `merged::PZO22001 Starfinder Player Core 294-329::/page/7/Text/34` | 0.840837 | **Spell Lists** |
| 5 | `merged::PZO22001 Starfinder Player Core 294-329::/page/13/Text/75` | 0.840837 | **Spell Lists** |
| 6 | `merged::PZO22001 Starfinder Player Core 294-329::/page/11/Text/84` | 0.840837 | **Spell Lists** |
| 7 | `merged::PZO22001 Starfinder Player Core 294-329::/page/3/Text/37` | 0.840837 | **Spell Lists** |
| 8 | `merged::PZO22001 Starfinder Player Core 294-329::/page/15/Text/81` | 0.840837 | **Spell Lists** |
| 9 | `merged::PZO22001 Starfinder Player Core 364-387::/page/21/Text/55` | 0.840837 | **Spell Lists** |
| 10 | `merged::PZO22001 Starfinder Player Core 364-387::/page/23/Text/42` | 0.840837 | **Spell Lists** |

### Query 119
- Text: Summarize 13
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/505']
- Expected found: `True`
- Expected rank: `4`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/505', 'merged::PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/506', 'merged::PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/504']
- Expanded expected found: `True`
- Expanded expected rank: `4`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/506` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/504` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 232-249::/page/11/TableCell/823` | 0.731589 | 13 |
| 2 | `merged::PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/414` | 0.731589 | 13 |
| 3 | `merged::PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/512` | 0.731589 | 13 |
| 4 | `merged::PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/505` | 0.731589 | 13 |
| 5 | `merged::PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/433` | 0.731589 | 13 |
| 6 | `merged::PZO22001 Starfinder Character Sheet::/page/1/TableCell/353` | 0.731589 | 13 |
| 7 | `merged::PZO22001 Starfinder Player Core 232-249::/page/5/TableCell/530` | 0.731589 | 13 |
| 8 | `merged::PZO22001 Starfinder Player Core 442-464::/page/16/TableCell/353` | 0.731589 | 13 |
| 9 | `merged::PZO22001 Starfinder Player Core 406-423::/page/17/TableCell/355` | 0.561605 | 13 (25 to 26) |
| 10 | `merged::PZO22001 Starfinder Player Core 040-057::/page/17/SectionHeader/35` | 0.549217 | **DISCIPLE OF THE CYCLE** **FEAT 13** |

### Query 120
- Text: What is the rule about Throughout this rulebook, you will see formatting  standards that might look a bit unusual at first. These  standards are in place to make the rules elements in this  book easier to recognize.?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 014-029::/page/1/Text/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 014-029::/page/1/Text/2', 'merged::PZO22001 Starfinder Player Core 014-029::/page/1/Text/3', 'merged::PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/1']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 014-029::/page/1/Text/3` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/1` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 014-029::/page/1/Text/2` | 0.923918 | Throughout this rulebook, you will see formatting  standards that might look a bit unusual at first. These  standards are in place to make the rules elements in this  book easier to recognize. |
| 2 | `merged::PZO22001 Starfinder Player Core 014-029::/page/2/Text/17` | 0.609087 | **Special** Any special qualities of the rule are explained in  this section. Usually this section appears in feats you  can select more than once, explaining what happens  when you do. |
| 3 | `merged::PZO22001 Starfinder Player Core 014-029::/page/2/Text/7` | 0.601874 | Regardless of the game mechanic they convey, rules  elements are always presented in the form of a stat block,  a summary of the rules necessary to bring the monster,  character, item, or other rules |
| 4 | `merged::PZO22001 Starfinder Player Core 014-029::/page/0/Text/2` | 0.589417 | While this chapter is here to teach you the basics of  Starfinder, the rest of this rulebook serves as a reference  manual during play, and it is organized to make finding  the rule you need as easy a |
| 5 | `merged::PZO22001 Starfinder Player Core 014-029::/page/0/Text/20` | 0.553269 | The back of this book has an  appendix with the rules for all of  the conditions that you will find  in the game. This section also  includes a blank character sheet,  and an index with a comprehensiv |
| 6 | `merged::PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/1` | 0.550390 | FORMAT OF RULES |
| 7 | `merged::PZO22001 Starfinder Player Core 406-423::/page/17/Text/32` | 0.534013 | Rules Overview |
| 8 | `merged::PZO22001 Starfinder Player Core 388-405::/page/2/SectionHeader/1` | 0.530408 | RULES OVERVIEW |
| 9 | `merged::PZO22001 Starfinder Player Core 388-405::/page/3/Text/14` | 0.520223 | Sometimes a rule could be interpreted multiple ways. If one  version is too good to be true, it probably is. If a rule seems  to have wording with problematic repercussions or doesn't  work as intende |
| 10 | `merged::PZO22001 Starfinder Player Core 014-029::/page/2/Text/6` | 0.519426 | This book contains many rules elements that give characters  new and interesting ways to respond to situations in the  game. All characters can use the basic actions found in  Chapter 8, but an indivi |

### Query 121
- Text: Summarize You're a career criminal with a nasty reputation. Perhaps  unfair circumstances forced you into a life of crime, or maybe  you enjoy the thrill you get from pulling off a heist or living  through a shoot-out. Either way, this life is the only one you  know, and thanks to the bounty on your head, you're in it  until the casket drops or you make enough creds to buy a  new one.
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 092-097::/page/3/Text/11']
- Expected found: `True`
- Expected rank: `1`
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
| 7 | `merged::PZO22001 Starfinder Player Core 126-137::/page/2/Text/18` | 0.535106 | You specialize in slipping into a location, completing an  objective, and extricating yourself without being discovered.  You might use stealth tactics, cover identities, disguises, or  spy tech. Whet |
| 8 | `merged::PZO22001 Starfinder Player Core 126-137::/page/1/Text/2` | 0.530399 | You're a focused, quick-witted professional who thrives in high-stakes combat. Your deadly aim and  tactical training give you an edge over the competition—for you, even the most powerful enemy is jus |
| 9 | `merged::PZO22001 Starfinder Player Core 150-161::/page/1/Text/19` | 0.525456 | You might join a military, perform physical labor, or take mercenary jobs when  you need credits. You likely spend time training at a gym or tinkering with your  weapons and shopping for new ammunitio |
| 10 | `merged::PZO22001 Starfinder Player Core 092-097::/page/4/Text/10` | 0.524204 | You're a crewmate on a pirate vessel with ambitions of  pillaging interstellar shipping lanes or taking over a chunk  of a notable planetary body. Perhaps you grew up on such  a ship, were taken priso |

### Query 122
- Text: Summarize **Trigger** Your turn begins.
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 406-423::/page/2/SectionHeader/19']
- Expected found: `True`
- Expected rank: `1`
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
| 2 | `merged::PZO22001 Starfinder Player Core 126-137::/page/8/Text/24` | 0.960189 | **Trigger** Your turn begins. |
| 3 | `merged::PZO22001 Starfinder Player Core 098-113::/page/15/Text/5` | 0.750661 | **Trigger** Your turn begins, and you issued a 2-action directive  on your last turn. |
| 4 | `merged::PZO22001 Starfinder Player Core 210-231::/page/11/SectionHeader/1` | 0.714144 | **Trigger** You take damage. |
| 5 | `merged::PZO22001 Starfinder Player Core 150-161::/page/6/Text/10` | 0.714144 | **Trigger** You take damage. |
| 6 | `merged::PZO22001 Starfinder Player Core 406-423::/page/4/Text/31` | 0.704709 | **Trigger** You fall. |
| 7 | `merged::PZO22001 Starfinder Player Core 424-441::/page/4/ListItem/7` | 0.697262 | You can use 1 free action or reaction with a trigger of  "Your turn begins" or something similar. |
| 8 | `merged::PZO22001 Starfinder Player Core 098-113::/page/14/Text/37` | 0.677214 | **Trigger** The final action on your turn is a 1-action directive. |
| 9 | `merged::PZO22001 Starfinder Player Core 098-113::/page/14/Text/47` | 0.666589 | **Trigger** You roll initiative. |
| 10 | `merged::PZO22001 Starfinder Player Core 126-137::/page/9/Text/35` | 0.666352 | **Trigger** A creature grabs, immobilizes, or restrains you. |

### Query 123
- Text: Summarize LEVELING UP29
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/134']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/134', 'merged::PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/136', 'merged::PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/132']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/136` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/132` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/134` | 0.923601 | LEVELING UP29 |
| 2 | `merged::PZO22001 Starfinder Player Core 014-029::/page/15/SectionHeader/0` | 0.774938 | LEVELING UP |
| 3 | `merged::PZO22001 Starfinder Player Core 014-029::/page/5/Text/30` | 0.722425 | **Leveling Up** |
| 4 | `merged::PZO22001 Starfinder Player Core 014-029::/page/13/Text/4` | 0.722425 | **Leveling Up** |
| 5 | `merged::PZO22001 Starfinder Player Core 014-029::/page/9/Text/26` | 0.722425 | **Leveling Up** |
| 6 | `merged::PZO22001 Starfinder Player Core 014-029::/page/15/Text/25` | 0.722425 | **Leveling Up** |
| 7 | `merged::PZO22001 Starfinder Player Core 014-029::/page/11/Text/29` | 0.722425 | **Leveling Up** |
| 8 | `merged::PZO22001 Starfinder Player Core 001-013::/page/6/Text/15` | 0.722425 | **Leveling Up** |
| 9 | `merged::PZO22001 Starfinder Player Core 001-013::/page/10/Text/35` | 0.722425 | **Leveling Up** |
| 10 | `merged::PZO22001 Starfinder Player Core 001-013::/page/4/Text/23` | 0.722425 | **Leveling Up** |

### Query 124
- Text: What is the rule about ACTIONS?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 406-423::/page/0/SectionHeader/1']
- Expected found: `True`
- Expected rank: `1`
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
| 4 | `merged::PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/6` | 0.699753 | UNDERSTANDING ACTIONS |
| 5 | `merged::PZO22001 Starfinder Player Core 424-441::/page/7/Text/60` | 0.669885 | **Actions** |
| 6 | `merged::PZO22001 Starfinder Player Core 424-441::/page/9/Text/43` | 0.669885 | **Actions** |
| 7 | `merged::PZO22001 Starfinder Player Core 406-423::/page/1/Text/36` | 0.669885 | **Actions** |
| 8 | `merged::PZO22001 Starfinder Player Core 388-405::/page/13/Text/40` | 0.669885 | **Actions** |
| 9 | `merged::PZO22001 Starfinder Player Core 388-405::/page/7/Text/28` | 0.669885 | **Actions** |
| 10 | `merged::PZO22001 Starfinder Player Core 388-405::/page/5/Text/31` | 0.669885 | **Actions** |

### Query 125
- Text: Summarize **Solarian**
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 126-137::/page/1/Text/35']
- Expected found: `False`
- Expected rank: `None`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 126-137::/page/1/Text/35', 'merged::PZO22001 Starfinder Player Core 126-137::/page/1/Text/36', 'merged::PZO22001 Starfinder Player Core 126-137::/page/1/Text/34']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 126-137::/page/1/Text/36` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 126-137::/page/1/Text/34` (reasons: ['graph_depth_1'])

### Query 126
- Text: What is the rule about Armor expertise, general feat, skill increase,?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/402']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/402', 'merged::PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/401', 'merged::PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/403']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/401` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/403` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/402` | 0.737588 | Armor expertise, general feat, skill increase, soldier expertise, tough as nails, weapon specialization |
| 2 | `merged::PZO22001 Starfinder Player Core 174-181::/page/5/Text/14` | 0.654663 | You become trained in light armor and medium armor. If  you already were trained in light armor and medium armor,  you gain training in heavy armor as well. Whenever you gain  a class feature that gra |
| 3 | `merged::PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/422` | 0.652816 | Fortitude expertise, general feat, leader's confidence, skill increase, weapon specialization |
| 4 | `merged::PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/414` | 0.650860 | Ancestry feat, armor mastery, skill increase |
| 5 | `merged::PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/434` | 0.645382 | Ancestry feat, light armor expertise, skill increase, tactician, weapon mastery |
| 6 | `merged::PZO22001 Starfinder Player Core 150-161::/page/4/Text/7` | 0.633583 | You have grown accustomed to wearing armor and  can make the most of its protection. Your proficiency  ranks for light armor, medium armor, heavy armor, and  unarmored defense increase to expert. You |
| 7 | `merged::PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/422` | 0.613024 | Ancestry feat, legendary armor, skill increase |
| 8 | `merged::PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/446` | 0.612582 | General feat, light armor mastery, silver tongue, skill increase |
| 9 | `merged::PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/440` | 0.609915 | Envoy feat, skill feat, skill increase |
| 10 | `merged::PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/424` | 0.609915 | Envoy feat, skill feat, skill increase |

### Query 127
- Text: What are the requirements for **Prerequisites** Watch Out?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/34']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/34', 'merged::PZO22001 Starfinder Player Core 098-113::/page/13/Text/35', 'merged::PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/33']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 098-113::/page/13/Text/35` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/33` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/34` | 0.879420 | **Prerequisites** Watch Out |
| 2 | `merged::PZO22001 Starfinder Player Core 098-113::/page/14/Text/26` | 0.879420 | **Prerequisites** Watch Out |
| 3 | `merged::PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/499` | 0.605694 | Prerequisites |
| 4 | `merged::PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/547` | 0.605694 | Prerequisites |
| 5 | `merged::PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/511` | 0.605694 | Prerequisites |
| 6 | `merged::PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/575` | 0.605694 | Prerequisites |
| 7 | `merged::PZO22001 Starfinder Player Core 210-231::/page/4/TableCell/452` | 0.605694 | Prerequisites |
| 8 | `merged::PZO22001 Starfinder Player Core 210-231::/page/4/TableCell/476` | 0.605694 | Prerequisites |
| 9 | `merged::PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/483` | 0.605694 | Prerequisites |
| 10 | `merged::PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/451` | 0.605694 | Prerequisites |

### Query 128
- Text: What is the rule about This section describes the effects or benefits of a rules  element. If the rule is an action, it explains what the effect  is or what you must roll. If it's a feat that modifies an  existing action or grants a constant effect, the benefit is  explained here.?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 014-029::/page/2/Text/16']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 014-029::/page/2/Text/16', 'merged::PZO22001 Starfinder Player Core 014-029::/page/2/Text/17', 'merged::PZO22001 Starfinder Player Core 014-029::/page/2/Text/15']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 014-029::/page/2/Text/17` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 014-029::/page/2/Text/15` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 014-029::/page/2/Text/16` | 0.953488 | This section describes the effects or benefits of a rules  element. If the rule is an action, it explains what the effect  is or what you must roll. If it's a feat that modifies an  existing action or |
| 2 | `merged::PZO22001 Starfinder Player Core 014-029::/page/2/Text/17` | 0.715987 | **Special** Any special qualities of the rule are explained in  this section. Usually this section appears in feats you  can select more than once, explaining what happens  when you do. |
| 3 | `merged::PZO22001 Starfinder Player Core 442-464::/page/4/Text/39` | 0.651739 | **effect** An effect is the result of an ability, though an ability's  exact effect is sometimes contingent on the result of a  check or other roll. 418–419 |
| 4 | `merged::PZO22001 Starfinder Player Core 388-405::/page/2/Text/17` | 0.625421 | An effect is the rules term for anything that occurs in the game  world. Effects (page 418) might have limited **Range**, and you  may need to designate **Targets** or create **Areas** for your effect |
| 5 | `merged::PZO22001 Starfinder Player Core 182-209::/page/6/Text/26` | 0.616468 | **Success** For an item or location, you get a sense of what it  does and learn any means of activating it. For an ongoing  effect (such as a spell with a duration), you learn the  effect's name and w |
| 6 | `merged::PZO22001 Starfinder Player Core 442-464::/page/0/Text/5` | 0.592305 | **ability** A general term referring to rules that provide an  exception to the basic rules. An ability could come from a  number of sources, so "an ability that gives you a bonus to  damage rolls" co |
| 7 | `merged::PZO22001 Starfinder Player Core 442-464::/page/5/Text/13` | 0.592245 | **feat** An ability you gain or select for your character due to  their ancestry, background, class, general training, or skill  training. Some feats grant special actions. 10, 16 |
| 8 | `merged::PZO22001 Starfinder Player Core 406-423::/page/13/Text/58` | 0.582481 | Some effects apply conditions to a creature or item. These change your state of being in some way. Conditions are  persistent, lasting until the stated duration ends, the condition is removed, or term |
| 9 | `merged::PZO22001 Starfinder Player Core 442-464::/page/5/Text/42` | 0.580947 | **fortune** (trait) A fortune effect beneficially alters how you roll  your dice. You can never have more than one fortune effect  alter a single roll. If multiple fortune effects would apply,  you ha |
| 10 | `merged::PZO22001 Starfinder Player Core 014-029::/page/2/Text/19` | 0.578986 | **Name** [one-action] (traits) **Frequency** how often it can be used;  **Trigger** when a reaction or free action can be  used; **Requirements** some actions require specific  circumstances, listed h |

### Query 129
- Text: What is the rule about Choose two attribute boosts. One must be to Dexterity or  Charisma, and one is a free attribute boost.?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 092-097::/page/0/Text/8']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 092-097::/page/0/Text/8', 'merged::PZO22001 Starfinder Player Core 092-097::/page/0/Text/9', 'merged::PZO22001 Starfinder Player Core 092-097::/page/0/Text/7']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 092-097::/page/0/Text/9` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 092-097::/page/0/Text/7` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 092-097::/page/1/Text/13` | 0.895158 | Choose two attribute boosts. One must be to Dexterity or  Charisma, and one is a free attribute boost. |
| 2 | `merged::PZO22001 Starfinder Player Core 092-097::/page/0/Text/8` | 0.895158 | Choose two attribute boosts. One must be to Dexterity or  Charisma, and one is a free attribute boost. |
| 3 | `merged::PZO22001 Starfinder Player Core 092-097::/page/2/Text/23` | 0.895158 | Choose two attribute boosts. One must be to Dexterity or  Charisma, and one is a free attribute boost. |
| 4 | `merged::PZO22001 Starfinder Player Core 092-097::/page/1/Text/17` | 0.895158 | Choose two attribute boosts. One must be to Dexterity or  Charisma, and one is a free attribute boost. |
| 5 | `merged::PZO22001 Starfinder Player Core 092-097::/page/4/Text/19` | 0.835786 | Choose two attribute boosts. One must be to Dexterity or  Wisdom, and one is a free attribute boost. |
| 6 | `merged::PZO22001 Starfinder Player Core 092-097::/page/4/Text/3` | 0.835786 | Choose two attribute boosts. One must be to Dexterity or  Wisdom, and one is a free attribute boost. |
| 7 | `merged::PZO22001 Starfinder Player Core 092-097::/page/2/Text/7` | 0.831064 | Choose two attribute boosts. One must be to Dexterity or  Intelligence, and one is a free attribute boost. |
| 8 | `merged::PZO22001 Starfinder Player Core 092-097::/page/2/Text/35` | 0.831064 | Choose two attribute boosts. One must be to Dexterity or  Intelligence, and one is a free attribute boost. |
| 9 | `merged::PZO22001 Starfinder Player Core 092-097::/page/4/Text/39` | 0.831064 | Choose two attribute boosts. One must be to Dexterity  or Intelligence, and one is a free attribute boost. |
| 10 | `merged::PZO22001 Starfinder Player Core 092-097::/page/1/Text/1` | 0.819127 | Choose two attribute boosts. One must be to Strength or  Dexterity, and one is a free attribute boost. |

### Query 130
- Text: What is the rule about **SPELLS**?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 232-249::/page/1/Text/42']
- Expected found: `False`
- Expected rank: `None`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 232-249::/page/1/Text/42', 'merged::PZO22001 Starfinder Player Core 232-249::/page/1/Text/43', 'merged::PZO22001 Starfinder Player Core 232-249::/page/1/Text/41']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 232-249::/page/1/Text/43` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 232-249::/page/1/Text/41` (reasons: ['graph_depth_1'])

### Query 131
- Text: Summarize **concealed** (condition) Low visibility makes you difficult to  target. 426, **435**
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 442-464::/page/2/Text/44']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 442-464::/page/2/Text/44', 'merged::PZO22001 Starfinder Player Core 442-464::/page/2/Text/45', 'merged::PZO22001 Starfinder Player Core 442-464::/page/2/Text/43']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 442-464::/page/2/Text/45` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 442-464::/page/2/Text/43` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 442-464::/page/2/Text/44` | 0.980283 | **concealed** (condition) Low visibility makes you difficult to  target. 426, **435** |
| 2 | `merged::PZO22001 Starfinder Player Core 406-423::/page/13/Text/62` | 0.681145 | **Concealed:** Fog or similar obscuration makes you difficult  to see and target. |
| 3 | `merged::PZO22001 Starfinder Player Core 442-464::/page/1/Text/49` | 0.630791 | **blinded** (condition) You're unable to see. 435 |
| 4 | `merged::PZO22001 Starfinder Player Core 442-464::/page/3/Text/36` | 0.591532 | **darkvision** (sense) See in black and white in darkness 424 **dazzled** (condition) Everything is concealed to you. 436 **DC (Difficulty Class)** *See also* Difficulty Class. 393 |
| 5 | `merged::PZO22001 Starfinder Player Core 424-441::/page/11/Text/17` | 0.588480 | You're difficult for one or more creatures to see due to thick  fog or some other obscuring feature. You can be concealed  to some creatures but not others. While concealed, you can  still be observed |
| 6 | `merged::PZO22001 Starfinder Player Core 442-464::/page/8/Text/47` | 0.584723 | **observed** (condition) You're in clear view. 424, **438** |
| 7 | `merged::PZO22001 Starfinder Player Core 442-464::/page/6/Text/24` | 0.571112 | **hidden** (condition) A creature knows your location but can't  see you. 425, **437** |
| 8 | `merged::PZO22001 Starfinder Player Core 442-464::/page/7/Text/6` | 0.569919 | **Investigate** (exploration activity) Study your surroundings. 431 **invisible** (condition) Creatures can't see you. 426, **438** |
| 9 | `merged::PZO22001 Starfinder Player Core 442-464::/page/2/Text/49` | 0.558815 | **confused** (condition) You attack indiscriminately. 435 |
| 10 | `merged::PZO22001 Starfinder Player Core 442-464::/page/5/Text/11` | 0.551397 | **fatigued** (condition) Your defenses are lower, and you can't  use exploration activities while traveling. 437 |

### Query 132
- Text: Summarize **PLAYING THE ** **GAME**
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 330-363::/page/1/Text/72']
- Expected found: `False`
- Expected rank: `None`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 330-363::/page/1/Text/72', 'merged::PZO22001 Starfinder Player Core 330-363::/page/1/Text/71', 'merged::PZO22001 Starfinder Player Core 330-363::/page/1/Text/73']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 330-363::/page/1/Text/71` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 330-363::/page/1/Text/73` (reasons: ['graph_depth_1'])

### Query 133
- Text: Summarize **CLASSES**
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 126-137::/page/1/Text/31']
- Expected found: `True`
- Expected rank: `68`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 126-137::/page/1/Text/31', 'merged::PZO22001 Starfinder Player Core 126-137::/page/5/Text/59', 'merged::PZO22001 Starfinder Player Core 126-137::/page/11/Text/30', 'merged::PZO22001 Starfinder Player Core 126-137::/page/1/Text/30', 'merged::PZO22001 Starfinder Player Core 126-137::/page/3/Text/34', 'merged::PZO22001 Starfinder Player Core 126-137::/page/9/Text/63', 'merged::PZO22001 Starfinder Player Core 126-137::/page/1/Text/32', 'merged::PZO22001 Starfinder Player Core 126-137::/page/7/Text/30']
- Expanded expected found: `True`
- Expanded expected rank: `24`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 126-137::/page/5/Text/59` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 126-137::/page/11/Text/30` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 126-137::/page/1/Text/30` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 126-137::/page/3/Text/34` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 126-137::/page/9/Text/63` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 126-137::/page/1/Text/32` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 126-137::/page/7/Text/30` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 174-181::/page/5/Text/49` | 0.890061 | **CLASSES** |
| 2 | `merged::PZO22001 Starfinder Player Core 210-231::/page/7/Text/63` | 0.890061 | **CLASSES** |
| 3 | `merged::PZO22001 Starfinder Player Core 442-464::/page/19/Text/79` | 0.890061 | **CLASSES** |
| 4 | `merged::PZO22001 Starfinder Player Core 442-464::/page/11/Text/56` | 0.890061 | **CLASSES** |
| 5 | `merged::PZO22001 Starfinder Player Core 182-209::/page/25/Text/28` | 0.890061 | **CLASSES** |
| 6 | `merged::PZO22001 Starfinder Player Core 364-387::/page/23/Text/37` | 0.890061 | **CLASSES** |
| 7 | `merged::PZO22001 Starfinder Player Core 182-209::/page/27/Text/38` | 0.890061 | **CLASSES** |
| 8 | `merged::PZO22001 Starfinder Player Core 150-161::/page/3/Text/42` | 0.890061 | **CLASSES** |
| 9 | `merged::PZO22001 Starfinder Player Core 150-161::/page/5/Text/50` | 0.890061 | **CLASSES** |
| 10 | `merged::PZO22001 Starfinder Player Core 210-231::/page/19/Text/69` | 0.890061 | **CLASSES** |

### Query 134
- Text: What is the rule about **BOUNTY HUNTER** **BACKGROUND**?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 092-097::/page/1/SectionHeader/3']
- Expected found: `True`
- Expected rank: `1`
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
| 2 | `merged::PZO22001 Starfinder Player Core 210-231::/page/6/SectionHeader/44` | 0.518158 | **BARGAIN HUNTER** **FEAT 1** |
| 3 | `merged::PZO22001 Starfinder Player Core 092-097::/page/1/SectionHeader/7` | 0.456964 | **BRUTARIS PLAYER** **BACKGROUND** |
| 4 | `merged::PZO22001 Starfinder Player Core 092-097::/page/2/Text/1` | 0.454455 | **DISCIPLE** **BACKGROUND** |
| 5 | `merged::PZO22001 Starfinder Player Core 098-113::/page/7/Text/67` | 0.434950 | **BACKGROUNDS** |
| 6 | `merged::PZO22001 Starfinder Player Core 406-423::/page/13/Text/31` | 0.434950 | **BACKGROUNDS** |
| 7 | `merged::PZO22001 Starfinder Player Core 126-137::/page/9/Text/80` | 0.434950 | **BACKGROUNDS** |
| 8 | `merged::PZO22001 Starfinder Player Core 126-137::/page/3/Text/50` | 0.434950 | **BACKGROUNDS** |
| 9 | `merged::PZO22001 Starfinder Player Core 098-113::/page/9/Text/56` | 0.434950 | **BACKGROUNDS** |
| 10 | `merged::PZO22001 Starfinder Player Core 150-161::/page/7/Text/46` | 0.434950 | **BACKGROUNDS** |

### Query 135
- Text: What is the rule about This convoluted web of synthweave straps is worn as a  fashion statement in some subcultures but has a useful  application in extreme environments. You gain a +1 item  bonus to Acrobatics checks, and you aren't off-guard or  clumsy while untethered in zero-g.?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 282-293::/page/1/Text/33']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 282-293::/page/1/Text/33', 'merged::PZO22001 Starfinder Player Core 282-293::/page/1/Text/32', 'merged::PZO22001 Starfinder Player Core 282-293::/page/1/Text/34']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 282-293::/page/1/Text/32` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 282-293::/page/1/Text/34` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 282-293::/page/1/Text/33` | 0.939037 | This convoluted web of synthweave straps is worn as a  fashion statement in some subcultures but has a useful  application in extreme environments. You gain a +1 item  bonus to Acrobatics checks, and |
| 2 | `merged::PZO22001 Starfinder Player Core 250-267::/page/6/Text/14` | 0.489285 | **Grapple:** You can use this weapon to Grapple with the  Athletics skill even if you don't have a free hand. This uses  the weapon's reach (if different from your own) and adds the  weapon's item bon |
| 3 | `merged::PZO22001 Starfinder Player Core 250-267::/page/8/Text/12` | 0.481461 | **Trip:** You can use this weapon to Trip with the Athletics  skill even if you don't have a free hand. This uses the  weapon's reach (if different from your own) and adds the  weapon's item bonus to |
| 4 | `merged::PZO22001 Starfinder Player Core 282-293::/page/2/Text/19` | 0.479120 | This magitech interface is a sophisticated pair of linked  bracers, wristbands, gloves, or other garments suitable to  the part of a creature's anatomy it uses to wield weapons.  One of the paired enh |
| 5 | `merged::PZO22001 Starfinder Player Core 406-423::/page/9/Text/17` | 0.472189 | A narrow surface is so precariously thin that you need to  Balance (see Acrobatics on page 192) or risk falling. Even  on a success, you're off-guard on a narrow surface. Each  time you are hit by an |
| 6 | `merged::PZO22001 Starfinder Player Core 424-441::/page/11/Text/15` | 0.463951 | Your movements become clumsy and inexact. Clumsy  always includes a value. You take a status penalty equal  to the condition value to Dexterity-based rolls and DCs,  including AC, Reflex saves, ranged |
| 7 | `merged::PZO22001 Starfinder Player Core 282-293::/page/2/Text/4` | 0.462419 | **Invested:** A PC can wear only 10 magical items that  have the invested trait. A character can still gain any  normal benefit from using a physical item without  investing it, such as using a *progr |
| 8 | `merged::PZO22001 Starfinder Player Core 442-464::/page/3/Text/7` | 0.459108 | **cover** When you're behind a physical obstacle, you get a +2  circumstance bonus to AC, Reflex saves vs. area effects,  and Stealth checks. This increases to +4 for greater cover.  Creatures can pro |
| 9 | `merged::PZO22001 Starfinder Player Core 250-267::/page/8/Text/6` | 0.457952 | **Shove:** You can use this weapon to Shove with the  Athletics skill even if you don't have a free hand. This uses  the weapon's reach (if different from your own) and adds the  weapon's item bonus t |
| 10 | `merged::PZO22001 Starfinder Player Core 282-293::/page/1/Text/17` | 0.454264 | This deep-blue prism with cloudy inclusions is light as a  feather. Its resonant power gives you a +1 item bonus to  Acrobatics checks. |

### Query 136
- Text: Summarize **CONDITIONS ** **APPENDIX**
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 182-209::/page/1/Text/30']
- Expected found: `False`
- Expected rank: `None`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 182-209::/page/1/Text/30', 'merged::PZO22001 Starfinder Player Core 182-209::/page/9/Text/46', 'merged::PZO22001 Starfinder Player Core 182-209::/page/1/Text/31', 'merged::PZO22001 Starfinder Player Core 182-209::/page/27/Text/46', 'merged::PZO22001 Starfinder Player Core 182-209::/page/19/Text/70', 'merged::PZO22001 Starfinder Player Core 182-209::/page/13/Text/52', 'merged::PZO22001 Starfinder Player Core 182-209::/page/17/Text/51', 'merged::PZO22001 Starfinder Player Core 182-209::/page/5/Text/31', 'merged::PZO22001 Starfinder Player Core 182-209::/page/11/Text/44', 'merged::PZO22001 Starfinder Player Core 182-209::/page/7/Text/38', 'merged::PZO22001 Starfinder Player Core 182-209::/page/25/Text/36', 'merged::PZO22001 Starfinder Player Core 182-209::/page/1/Text/29']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 182-209::/page/9/Text/46` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 182-209::/page/1/Text/31` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 182-209::/page/27/Text/46` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 182-209::/page/19/Text/70` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 182-209::/page/13/Text/52` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 182-209::/page/17/Text/51` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 182-209::/page/5/Text/31` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 182-209::/page/11/Text/44` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 182-209::/page/7/Text/38` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 182-209::/page/25/Text/36` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 182-209::/page/1/Text/29` (reasons: ['graph_depth_1'])

### Query 137
- Text: What is the rule about **ATTACKS**?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/58']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/58', 'merged::PZO22001 Starfinder Player Core 150-161::/page/1/Text/57', 'merged::PZO22001 Starfinder Player Core 150-161::/page/1/Text/59']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 150-161::/page/1/Text/57` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 150-161::/page/1/Text/59` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/58` | 0.805189 | **ATTACKS** |
| 2 | `merged::PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/59` | 0.805189 | **ATTACKS** |
| 3 | `merged::PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/57` | 0.805189 | **ATTACKS** |
| 4 | `merged::PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/56` | 0.805189 | **ATTACKS** |
| 5 | `merged::PZO22001 Starfinder Player Core 406-423::/page/2/SectionHeader/26` | 0.714130 | **ATTACK** |
| 6 | `merged::PZO22001 Starfinder Player Core 406-423::/page/4/Text/15` | 0.714130 | **ATTACK** |
| 7 | `merged::PZO22001 Starfinder Player Core 406-423::/page/4/Text/36` | 0.628757 | **AREA** **ATTACK** |
| 8 | `merged::PZO22001 Starfinder Player Core 406-423::/page/4/Text/27` | 0.628757 | **AREA** **ATTACK** |
| 9 | `merged::PZO22001 Starfinder Player Core 250-267::/page/3/SectionHeader/19` | 0.543231 | UNARMED ATTACKS |
| 10 | `merged::PZO22001 Starfinder Player Core 250-267::/page/3/SectionHeader/3` | 0.509180 | ATTACK ROLLS |

### Query 138
- Text: What is the rule about The tables on pages 286–287 list level, price, Bulk,  and hands entries for a wide variety of magic and hybrid  items. Each item has its own rules for how it functions:  some require bespoke activations, while others function  automatically, such as by granting constant item bonuses  or other benefits when worn or held.?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 282-293::/page/0/Text/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 282-293::/page/0/Text/5', 'merged::PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/6', 'merged::PZO22001 Starfinder Player Core 282-293::/page/0/Text/4']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 282-293::/page/0/SectionHeader/6` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 282-293::/page/0/Text/4` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 282-293::/page/0/Text/5` | 0.939073 | The tables on pages 286–287 list level, price, Bulk,  and hands entries for a wide variety of magic and hybrid  items. Each item has its own rules for how it functions:  some require bespoke activatio |
| 2 | `merged::PZO22001 Starfinder Player Core 232-249::/page/6/Text/5` | 0.645793 | The tables starting on page 240 list the Price and Bulk entries  for a wide variety of gear you can use to kit out your character.  Any item with a number after it in parentheses indicates that  the i |
| 3 | `merged::PZO22001 Starfinder Player Core 282-293::/page/0/Text/12` | 0.581588 | While some items function automatically and grant constant  benefits, others produce effects only when properly used. An  activation lists the number of actions it takes and any traits  of the activat |
| 4 | `merged::PZO22001 Starfinder Player Core 232-249::/page/2/Text/7` | 0.579101 | Each item has an item level, which represents the item's  complexity and any magic or technology used in its  construction. Simpler items with a lower level are easier to  construct, and you can't Cra |
| 5 | `merged::PZO22001 Starfinder Player Core 232-249::/page/3/Text/19` | 0.548619 | Higher-level magic and tech items that cost significantly more than 8 times the cost of a mundane item use their listed Price regardless of size. Precious materials, however, have a Price based on the |
| 6 | `merged::PZO22001 Starfinder Player Core 406-423::/page/2/Text/4` | 0.544940 | In addition to the actions in these two sections, the actions  for spellcasting can be found on page 298, and the actions for  using magic items appear on page 282. |
| 7 | `merged::PZO22001 Starfinder Player Core 014-029::/page/2/Text/17` | 0.537294 | **Special** Any special qualities of the rule are explained in  this section. Usually this section appears in feats you  can select more than once, explaining what happens  when you do. |
| 8 | `merged::PZO22001 Starfinder Player Core 282-293::/page/0/Text/7` | 0.530881 | Certain magic and hybrid items convey their benefits only  when worn and invested using the Invest an Item activity,  connecting them to a specific PC. A PC can benefit from  no more than 10 invested |
| 9 | `merged::PZO22001 Starfinder Player Core 014-029::/page/2/Text/9` | 0.523583 | Spells, tech items, and magic items use a similar format,  but their stat blocks contain a number of unique elements,  such as the possible magical traditions for a spell (see  Chapter 7 for more on r |
| 10 | `merged::PZO22001 Starfinder Player Core 014-029::/page/2/Text/8` | 0.523304 | The general format for stat blocks is shown below.  Entries are omitted from a stat block when they don't  apply, so not all rule elements will have ever each of the  entries given below. Actions, rea |

### Query 139
- Text: What is the rule about FEATS THAT GRANT FEATS?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 174-181::/page/0/SectionHeader/12']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 174-181::/page/0/SectionHeader/12', 'merged::PZO22001 Starfinder Player Core 174-181::/page/0/Text/13', 'merged::PZO22001 Starfinder Player Core 174-181::/page/0/Text/11']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 174-181::/page/0/Text/13` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 174-181::/page/0/Text/11` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 174-181::/page/0/SectionHeader/12` | 0.833291 | FEATS THAT GRANT FEATS |
| 2 | `merged::PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/11` | 0.637003 | CHAPTER 5: FEATS |
| 3 | `merged::PZO22001 Starfinder Player Core 210-231::/page/1/SectionHeader/1` | 0.637003 | CHAPTER 5: FEATS |
| 4 | `merged::PZO22001 Starfinder Player Core 250-267::/page/17/Text/10` | 0.585706 | FEATS |
| 5 | `merged::PZO22001 Starfinder Player Core 406-423::/page/17/Text/28` | 0.585705 | FEATS |
| 6 | `merged::PZO22001 Starfinder Player Core 014-029::/page/7/Text/24` | 0.585705 | FEATS |
| 7 | `merged::PZO22001 Starfinder Player Core 250-267::/page/15/Text/10` | 0.585705 | FEATS |
| 8 | `merged::PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/540` | 0.536309 | Feat |
| 9 | `merged::PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/590` | 0.536309 | Feat |
| 10 | `merged::PZO22001 Starfinder Player Core 174-181::/page/0/SectionHeader/10` | 0.526942 | ADDITIONAL FEATS |

### Query 140
- Text: Summarize **Sample Names:** Lashunta naming conventions often use  tonal elements. Some sample lashunta names are Domash,  Hesori, Imaaz, Kima, Kopalo, Maenala, Nomae, Oraeus, Raia,  Shess, Soryn, Stretto, Taeon, and Varikuara.
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 058-073::/page/1/Text/17']
- Expected found: `True`
- Expected rank: `1`
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
| 4 | `merged::PZO22001 Starfinder Player Core 074-091::/page/1/Text/17` | 0.634878 | **Sample Names:** Abazobari, Ahadigar, Asthonad, Dotralan,  Evdokayo, Julukesh, Katara, Obozaya, Oromeras, Radokama,  Sarangari, Sobok, Terikoraz, Vindasorn, Yuluzak |
| 5 | `merged::PZO22001 Starfinder Player Core 040-057::/page/15/Text/17` | 0.627682 | **Sample Names:** Altronus, Barasul, Ehu, Esar, Gorsen, Hadif,  Jahir, Kala, Khsutil, Maeda, Metweska, Ninura, Remu, Senesel,  Tolar, Umana, Voloteo, Zye |
| 6 | `merged::PZO22001 Starfinder Player Core 040-057::/page/7/Text/15` | 0.611159 | **Sample Names:** Barathu names change when they merge  and split back into their component parts. Many early stage  barathus choose their own names, selecting words for concepts  that resonate with t |
| 7 | `merged::PZO22001 Starfinder Player Core 058-073::/page/13/Text/18` | 0.608926 | **Sample Names:** Ayoka, Baazo, Bixby, Dakoyo, Fipzul, Gazigaz,  Jomp, Kayoko, Kimikim, Mimzy, Nako, Prismacora, Quonx,  Rudfuz, Sprax, Timinim, Tipps, Tonkona, Viverivim |
| 8 | `merged::PZO22001 Starfinder Player Core 040-057::/page/3/Text/15` | 0.596044 | **Sample Names:** Asha, Blue-17, Celita, Daniv, Emene-3, Era-4, Flick, Garro, Historia-6, Hope-1, Iseph, Melody, Naga, Olas,  Omen, Prime, Ruby-17, Stringer, Twenty Six, Urdun, Verity-3,  Yose |
| 9 | `merged::PZO22001 Starfinder Player Core 074-091::/page/11/Text/2` | 0.576051 | **Sample Names:** Agavana, Ajanu, Cailis, Enduri, Jiann,  Kilarra, Orthei, Ruven, Taylehm, Thel-Sevai, Tis, Yevtori |
| 10 | `merged::PZO22001 Starfinder Player Core 442-464::/page/7/Text/34` | 0.574939 | **lashunta** (trait) A creature with this trait is a member of the  lashunta ancestry. Lashunta are charming telepaths known  for their unique dimorphism. An ability with this trait can  be used or se |

### Query 141
- Text: What are the requirements for **INFLUENCE **[reaction] **FEAT 4**?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/29']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/29', 'merged::PZO22001 Starfinder Player Core 098-113::/page/12/Text/31', 'merged::PZO22001 Starfinder Player Core 098-113::/page/12/Text/28']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 098-113::/page/12/Text/31` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 098-113::/page/12/Text/28` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/29` | 0.862397 | **INFLUENCE **[reaction] **FEAT 4** |
| 2 | `merged::PZO22001 Starfinder Player Core 098-113::/page/14/Text/58` | 0.661999 | **Prerequisites** Influence |
| 3 | `merged::PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/19` | 0.572960 | **NOT IN THE FACE **[reaction] **FEAT 4** |
| 4 | `merged::PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/2` | 0.535046 | **INFLUENCER** |
| 5 | `merged::PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/592` | 0.529341 | Influence |
| 6 | `merged::PZO22001 Starfinder Player Core 174-181::/page/5/SectionHeader/20` | 0.489869 | **SOLDIER'S RESILIENCY** **FEAT 4** |
| 7 | `merged::PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/9` | 0.486373 | **MISSION BRIEFING** **FEAT 4** |
| 8 | `merged::PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/55` | 0.485386 | **EFFORTLESS INFLUENCER** **FEAT 16** |
| 9 | `merged::PZO22001 Starfinder Player Core 364-387::/page/13/SectionHeader/63` | 0.485356 | **ALTERNATE OUTCOME **[reaction] **FOCUS 4** |
| 10 | `merged::PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/62` | 0.475420 | **OPERATIVE RESILIENCY** **FEAT 4** |

### Query 142
- Text: What is the rule about This section specifies the levels at which your character  gains class feats—special feats that only members of that  class can access. Class feats are granted beginning at 1st or  2nd level, depending on the class. Specific class feats are  detailed at the end of each class entry.?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 098-113::/page/2/Text/15']
- Expected found: `True`
- Expected rank: `1`
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
| 5 | `merged::PZO22001 Starfinder Player Core 014-029::/page/15/ListItem/16` | 0.677392 | Select feats as indicated on your class advancement  table. For ancestry feats, see Chapter 2. For class  feats, see your class entry in Chapter 3. For general  feats and skill feats, see Chapter 5. |
| 6 | `merged::PZO22001 Starfinder Player Core 014-029::/page/0/Text/12` | 0.676406 | As a character advances in level, they gain additional feats  to represent their growing abilities. General feats and skill  feats (which are a subset of general feats) are presented  in this chapter. |
| 7 | `merged::PZO22001 Starfinder Player Core 182-209::/page/2/Text/14` | 0.669971 | As your character advances in level, there are two  main ways their skills improve: skill increases and skill  feats. Your class lists the levels at which you gain each  of these improvements. |
| 8 | `merged::PZO22001 Starfinder Player Core 014-029::/page/2/Text/17` | 0.663851 | **Special** Any special qualities of the rule are explained in  this section. Usually this section appears in feats you  can select more than once, explaining what happens  when you do. |
| 9 | `merged::PZO22001 Starfinder Player Core 098-113::/page/2/Text/10` | 0.656635 | This table summarizes the feats, skill increases, attribute  boosts, and other benefits your character gains as they  advance in level. The first column of the class table  indicates a level, and the |
| 10 | `merged::PZO22001 Starfinder Player Core 174-181::/page/0/Text/11` | 0.654812 | Some archetypes include a list of "Additional Feats" that  appear in other sources. The list includes each feat's level,  which might be different than normal when gained from the  archetype. You can |

### Query 143
- Text: What does **SUMMON PLANT OR FUNGUS **[three-actions] **SPELL 1** do?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/11', 'merged::PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/18', 'merged::PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/4']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/18` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/4` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/11` | 0.706162 | **SUMMON PLANT OR FUNGUS **[three-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** primal **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creature |
| 2 | `merged::PZO22001 Starfinder Player Core 294-329::/page/17/Text/13` | 0.592144 | **Summon Plant or Fungus**H Conjure a plant or fungus to fight  on your behalf. |
| 3 | `merged::PZO22001 Starfinder Player Core 114-125::/page/8/Text/15` | 0.578250 | **Order **Plant; **Skill** Plant Lore; **Spells** 1st: *summon* *plant* *or* *fungus*; 2nd: *verdant* *code*; 5th: *plant form* |
| 4 | `merged::PZO22001 Starfinder Player Core 294-329::/page/7/Text/19` | 0.552024 | **SPELL NAME **[one-action] **SPELL (RANK)** |
| 5 | `merged::PZO22001 Starfinder Player Core 114-125::/page/7/SectionHeader/18` | 0.539708 | **REACH SPELL **[one-action] **FEAT 1** |
| 6 | `merged::PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/15` | 0.539708 | **REACH SPELL **[one-action] **FEAT 1** |
| 7 | `merged::PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/25` | 0.532115 | **WIDEN SPELL **[one-action] **FEAT 1** |
| 8 | `merged::PZO22001 Starfinder Player Core 114-125::/page/7/SectionHeader/22` | 0.532115 | **WIDEN SPELL **[one-action] **FEAT 1** |
| 9 | `merged::PZO22001 Starfinder Player Core 162-173::/page/7/SectionHeader/27` | 0.528838 | **OTHERWORLDLY SPELL **[one-action] **FEAT 1** |
| 10 | `merged::PZO22001 Starfinder Player Core 114-125::/page/3/SectionHeader/29` | 0.521035 | **NETWORK SPELL **[one-action] |

### Query 144
- Text: What is the rule about is necessary, they can require audio or biometric imprints  in order to activate. Some advanced credsticks even have a  magical component that might require a mental password or  the recitation of a specific spell to access stored funds.?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 232-249::/page/1/Text/15']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 232-249::/page/1/Text/15', 'merged::PZO22001 Starfinder Player Core 232-249::/page/1/Text/14', 'merged::PZO22001 Starfinder Player Core 232-249::/page/1/Text/16']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 232-249::/page/1/Text/14` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 232-249::/page/1/Text/16` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 232-249::/page/1/Text/15` | 0.939248 | is necessary, they can require audio or biometric imprints  in order to activate. Some advanced credsticks even have a  magical component that might require a mental password or  the recitation of a s |
| 2 | `merged::PZO22001 Starfinder Player Core 232-249::/page/1/Text/12` | 0.586952 | Most people in Starfinder keep their wealth on a protected  item known as a credstick. These devices are often flat and  roughly the size of a human finger. They range in dimensions  and quality, but |
| 3 | `merged::PZO22001 Starfinder Player Core 232-249::/page/1/Text/16` | 0.581412 | Credsticks aren't gateways to the entirety of one's wealth,  and larger stores of credits are often kept secured in banks,  personal vaults, or secure databases. Instead, a credstick  is a safe and an |
| 4 | `merged::PZO22001 Starfinder Player Core 232-249::/page/1/Text/17` | 0.534580 | Individuals in the Pact Worlds often carry credsticks,  and other civilizations that interact with the Pact often turn  local funds into credits and thus carry them to spend their  converted currency. |
| 5 | `merged::PZO22001 Starfinder Player Core 232-249::/page/1/Text/10` | 0.491208 | Pact credits themselves are a combination of both digital  and physical currency assets. One person might contain all  their credits on a digital datacrypt that's safeguarded by the  most rigorous of |
| 6 | `merged::PZO22001 Starfinder Player Core 232-249::/page/2/Text/4` | 0.474139 | UPBs are so common that they're used as currency in  many major settlements and trade hubs. While credsticks are  a more convenient and secure way to carry value, UPBs have  the advantage of direct ut |
| 7 | `merged::PZO22001 Starfinder Player Core 210-231::/page/8/Text/16` | 0.465999 | You can find ways to craft just about anything, despite  restrictions. As long as you have the appropriate Crafting  skill feat (such as Magical Crafting for magic items) and meet  the item's level an |
| 8 | `merged::PZO22001 Starfinder Player Core 294-329::/page/4/Text/7` | 0.465575 | Some spells require you to pay a cost or provide a locus. If the  spell lists a **cost**, you must have the listed money, valuable  materials, or other resources to cast the spell (such as gems or  ma |
| 9 | `merged::PZO22001 Starfinder Player Core 282-293::/page/3/Text/18` | 0.460972 | **Activate—Secret Password** [two-actions] (auditory) **Effect** You  whisper a secret passcode known only to yourself  and your *programmer's* *plushie*, securing a computer,  container, door, or loc |
| 10 | `merged::PZO22001 Starfinder Player Core 210-231::/page/20/Text/4` | 0.454602 | **Prerequisites** trained in Arcana, Nature, Occultism, or Religion You examine a magic item you normally couldn't use in an  effort to fool it and activate it temporarily. For example,  this might al |

### Query 145
- Text: What is the rule about **SKILLS**?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 210-231::/page/1/Text/16']
- Expected found: `True`
- Expected rank: `61`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 210-231::/page/1/Text/16', 'merged::PZO22001 Starfinder Player Core 210-231::/page/1/Text/15', 'merged::PZO22001 Starfinder Player Core 210-231::/page/1/Text/17']
- Expanded expected found: `True`
- Expanded expected rank: `61`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 210-231::/page/1/Text/15` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 210-231::/page/1/Text/17` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 210-231::/page/3/Text/6` | 0.814442 | **SKILLS** |
| 2 | `merged::PZO22001 Starfinder Player Core 406-423::/page/9/Text/26` | 0.814442 | **SKILLS** |
| 3 | `merged::PZO22001 Starfinder Player Core 442-464::/page/13/Text/56` | 0.814442 | **SKILLS** |
| 4 | `merged::PZO22001 Starfinder Player Core 424-441::/page/17/Text/29` | 0.814442 | **SKILLS** |
| 5 | `merged::PZO22001 Starfinder Player Core 442-464::/page/9/Text/48` | 0.814442 | **SKILLS** |
| 6 | `merged::PZO22001 Starfinder Player Core 182-209::/page/27/Text/39` | 0.814442 | **SKILLS** |
| 7 | `merged::PZO22001 Starfinder Player Core 406-423::/page/7/Text/30` | 0.814442 | **SKILLS** |
| 8 | `merged::PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/56` | 0.814442 | **SKILLS** |
| 9 | `merged::PZO22001 Starfinder Player Core 424-441::/page/7/Text/48` | 0.814442 | **SKILLS** |
| 10 | `merged::PZO22001 Starfinder Player Core 182-209::/page/5/Text/23` | 0.814442 | **SKILLS** |

### Query 146
- Text: What are the requirements for **DON'T YOU DIE ON ME **[one-action] **FEAT 2**?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/13']
- Expected found: `False`
- Expected rank: `None`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/13', 'merged::PZO22001 Starfinder Player Core 098-113::/page/11/Text/12', 'merged::PZO22001 Starfinder Player Core 098-113::/page/11/Text/14']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 098-113::/page/11/Text/12` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 098-113::/page/11/Text/14` (reasons: ['graph_depth_1'])

### Query 147
- Text: What is the rule about If the globe overlaps with an area of magical darkness,  *sunburst* attempts to counteract the darkness effect.?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 364-387::/page/1/Text/44']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 364-387::/page/1/Text/44', 'merged::PZO22001 Starfinder Player Core 364-387::/page/1/Text/43', 'merged::PZO22001 Starfinder Player Core 364-387::/page/1/Text/45']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 364-387::/page/1/Text/43` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 364-387::/page/1/Text/45` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 364-387::/page/1/Text/44` | 0.922228 | If the globe overlaps with an area of magical darkness,  *sunburst* attempts to counteract the darkness effect. |
| 2 | `merged::PZO22001 Starfinder Player Core 294-329::/page/18/Text/45` | 0.625056 | **Sunburst**H A globe of sunlight deals fire damage, hurts undead,  and overcomes darkness. |
| 3 | `merged::PZO22001 Starfinder Player Core 294-329::/page/13/Text/19` | 0.625056 | **Sunburst**H A globe of sunlight deals fire damage, hurts  undead, and overcomes darkness. |
| 4 | `merged::PZO22001 Starfinder Player Core 442-464::/page/7/Text/46` | 0.620854 | **light** (trait) Light effects overcome non-magical darkness  in the area, and can counteract magical darkness. You  must usually target darkness magic with your light magic  directly to counteract t |
| 5 | `merged::PZO22001 Starfinder Player Core 294-329::/page/5/Text/4` | 0.615370 | Non-magical light always shines in non-magical darkness  and always fails to shine in magical darkness. Magical light  always shines in non-magical darkness but shines in magical  darkness only if the |
| 6 | `merged::PZO22001 Starfinder Player Core 442-464::/page/3/Text/35` | 0.611821 | **darkness** (trait) Darkness effects extinguish non-magical light  in the area and can counteract less powerful magical light.  You must usually target light magic with your darkness  magic directly |
| 7 | `merged::PZO22001 Starfinder Player Core 294-329::/page/6/Text/11` | 0.577450 | Some spells have effects that remain even after the spell's  magic is gone. Any ongoing effect that isn't part of the spell's  duration entry isn't magical. For instance, a spell such as  *sunburst* t |
| 8 | `merged::PZO22001 Starfinder Player Core 294-329::/page/34/SectionHeader/6` | 0.559565 | **ECLIPSE BURST **[two-actions] **SPELL 7**  **COLD** **CONCENTRATE** **DARKNESS** **MANIPULATE** **VOID**  **Traditions** arcane, divine, primal **Range **500 feet;** Area** 60-foot burst  **Defense* |
| 9 | `merged::PZO22001 Starfinder Player Core 364-387::/page/12/ListItem/16` | 0.546826 | If you spend 20 or more Hit Points and the spell was  cast in an area of magical darkness, vitality nova  attempts to counteract the darkness effect. |
| 10 | `merged::PZO22001 Starfinder Player Core 162-173::/page/10/Text/25` | 0.544908 | You expose this reality to a realm of pure darkness filled with  gibbering voices and otherworldly entities. The area of your  quantum field functions as though it were an area of 2ndrank *darkness*. |

### Query 148
- Text: What is the rule about Armor, shields and weapons gain more upgrade slots as they improve. Higher grades of armor add more AC and gains the resilient trait, improving the saving throws of their wielder by the listed value. Higher grades of weapons have improved damage dice and gain the tracking trait, improving their attack rolls by the listed value. Higher grades of shields have increased Hardness, Hit Points, and BT.?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 232-249::/page/4/Text/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 232-249::/page/4/Text/10', 'merged::PZO22001 Starfinder Player Core 232-249::/page/4/SectionHeader/11', 'merged::PZO22001 Starfinder Player Core 232-249::/page/4/Text/9']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 232-249::/page/4/SectionHeader/11` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 232-249::/page/4/Text/9` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 232-249::/page/4/Text/10` | 0.916961 | Armor, shields and weapons gain more upgrade slots as they improve. Higher grades of armor add more AC and gains the resilient trait, improving the saving throws of their wielder by the listed value. |
| 2 | `merged::PZO22001 Starfinder Player Core 210-231::/page/18/TableCell/409` | 0.630364 | Armor, shields and upgrades |
| 3 | `merged::PZO22001 Starfinder Player Core 150-161::/page/5/Text/6` | 0.622945 | Your skill with armor further improves. Your proficiency  ranks for light armor, medium armor, heavy armor, and  unarmored defense increase to master. |
| 4 | `merged::PZO22001 Starfinder Player Core 250-267::/page/0/Text/2` | 0.605896 | A shield can increase your character's defense beyond the protection their armor provides. Your  character must be wielding a shield in one hand to make use of it, and it grants its bonus to AC only |
| 5 | `merged::PZO22001 Starfinder Player Core 150-161::/page/4/Text/7` | 0.597963 | You have grown accustomed to wearing armor and  can make the most of its protection. Your proficiency  ranks for light armor, medium armor, heavy armor, and  unarmored defense increase to expert. You |
| 6 | `merged::PZO22001 Starfinder Player Core 098-113::/page/2/Text/1` | 0.594075 | rush into battle with weapons raised gain a higher number  of Hit Points each level, while characters who cast spells or  engage in trickery gain fewer. |
| 7 | `merged::PZO22001 Starfinder Player Core 232-249::/page/4/Text/6` | 0.591856 | Most types of armor, shields, and weapons in Starfinder come in a variety of grades. Each grade represents an improved version of that piece of equipment and should be sought after once your character |
| 8 | `merged::PZO22001 Starfinder Player Core 250-267::/page/0/Text/23` | 0.586013 | **Installed:** Some shields aren't held but are installed  as armor or weapon upgrades. You can Raise a Shield  installed as an armor upgrade as normal. Shields can be  installed only into weapons wit |
| 9 | `merged::PZO22001 Starfinder Player Core 442-464::/page/1/Text/10` | 0.581616 | **Armor Class (AC)** This score represents how hard it is to hit  and damage a creature. It typically serves as the DC to hit a  creature with an attack. AC = 10 + Dex modifier (up to your  armor's De |
| 10 | `merged::PZO22001 Starfinder Player Core 232-249::/page/4/Text/9` | 0.573180 | Armor, shields, and weapons (pages 244, 250, and 253 respectively) are typically listed using their lowest available grade, usually commercial. Each grade beyond the first provides the equipment with |

### Query 149
- Text: Summarize **Solarian**
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 162-173::/page/1/Text/39']
- Expected found: `False`
- Expected rank: `None`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 162-173::/page/1/Text/39', 'merged::PZO22001 Starfinder Player Core 162-173::/page/1/Text/40', 'merged::PZO22001 Starfinder Player Core 162-173::/page/1/Text/38']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 162-173::/page/1/Text/40` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 162-173::/page/1/Text/38` (reasons: ['graph_depth_1'])

### Query 150
- Text: What is the rule about 3 Retrieving an item stowed in your own backpack requires first taking off the backpack with a separate Interact action.?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 232-249::/page/4/ListItem/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 232-249::/page/4/ListItem/4', 'merged::PZO22001 Starfinder Player Core 232-249::/page/4/SectionHeader/5', 'merged::PZO22001 Starfinder Player Core 232-249::/page/4/ListItem/3']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 232-249::/page/4/SectionHeader/5` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 232-249::/page/4/ListItem/3` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 232-249::/page/4/ListItem/4` | 0.907493 | 3 Retrieving an item stowed in your own backpack requires first taking off the backpack with a separate Interact action. |
| 2 | `merged::PZO22001 Starfinder Player Core 232-249::/page/4/TableCell/195` | 0.618302 | Retrieve an item from a backpack3, sack, or similar container |
| 3 | `merged::PZO22001 Starfinder Player Core 232-249::/page/4/Table/1` | 0.567046 | ChangeHandsActionChange your grip by removing a hand from an item2ReleaseChange your grip by adding a hand to an item2InteractRetrieve an item from a backpack3, sack, or similar container2Interact |
| 4 | `merged::PZO22001 Starfinder Player Core 268-281::/page/5/Text/1` | 0.558349 | However, you must spend a single Interact action to retrieve  the bipod before you can move the weapon to a different  position. Deploying or retrieving a bipod with an Interact  action doesn't automa |
| 5 | `merged::PZO22001 Starfinder Player Core 232-249::/page/2/Text/12` | 0.557807 | Many ways of using items require you to spend multiple  actions. For example, drinking a serum worn at your belt  requires using an Interact action to draw it and then using  a second action to drink |
| 6 | `merged::PZO22001 Starfinder Player Core 232-249::/page/2/Text/10` | 0.551811 | Drawing a worn item or changing how you're carrying an  item usually requires you to use an Interact action (though to  drop an item, you use the Release action instead). Changing |
| 7 | `merged::PZO22001 Starfinder Player Core 442-464::/page/7/Text/3` | 0.514537 | **Interact **[one-action] (basic action) Grab or manipulate an object. 408 drawing and stowing items 234 |
| 8 | `merged::PZO22001 Starfinder Player Core 406-423::/page/0/Text/6` | 0.511341 | You'll need to track your actions carefully in an encounter. At  the start of each turn you take in an encounter, you regain 3  actions and 1 reaction to spend that round. (Regaining your  actions is |
| 9 | `merged::PZO22001 Starfinder Player Core 232-249::/page/3/Table/23` | 0.510646 | ChangeHandsActionDraw or put away a worn item, swap one item for another, or pick up an item11 or 2InteractPass an item to or take an item from a willing creature21 or 2InteractDrop an item to the gro |
| 10 | `merged::PZO22001 Starfinder Player Core 250-267::/page/4/Text/18` | 0.489794 | An item with an entry of "—" must be drawn to be thrown,  which usually takes an Interact action just like drawing any  other weapon. Reloading a ranged weapon and drawing a  thrown weapon both requir |

### Query 151
- Text: What is the rule about Fearsome bulwark, general feat, reflex?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/394']
- Expected found: `False`
- Expected rank: `None`
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
- Expected rank: `7`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/397', 'merged::PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/398', 'merged::PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/396']
- Expanded expected found: `True`
- Expanded expected rank: `7`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/398` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/396` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/405` | 0.881260 | Skill feat, solarian feat |
| 2 | `merged::PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/425` | 0.881260 | Skill feat, solarian feat |
| 3 | `merged::PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/401` | 0.881260 | Skill feat, solarian feat |
| 4 | `merged::PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/421` | 0.881260 | Skill feat, solarian feat |
| 5 | `merged::PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/417` | 0.881260 | Skill feat, solarian feat |
| 6 | `merged::PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/413` | 0.881260 | Skill feat, solarian feat |
| 7 | `merged::PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/397` | 0.881260 | Skill feat, solarian feat |
| 8 | `merged::PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/393` | 0.881260 | Skill feat, solarian feat |
| 9 | `merged::PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/429` | 0.767088 | Attribute boosts, skill feat, solarian feat |
| 10 | `merged::PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/409` | 0.767088 | Attribute boosts, skill feat, solarian feat |

### Query 153
- Text: What is the rule about **CYBERBORN** **BACKGROUND**?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 092-097::/page/1/SectionHeader/31']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 092-097::/page/1/SectionHeader/31', 'merged::PZO22001 Starfinder Player Core 092-097::/page/1/SectionHeader/32', 'merged::PZO22001 Starfinder Player Core 092-097::/page/1/Text/30']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 092-097::/page/1/SectionHeader/32` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 092-097::/page/1/Text/30` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 092-097::/page/1/SectionHeader/31` | 0.871656 | **CYBERBORN** **BACKGROUND** |
| 2 | `merged::PZO22001 Starfinder Player Core 114-125::/page/3/Text/50` | 0.464637 | **BACKGROUNDS** |
| 3 | `merged::PZO22001 Starfinder Player Core 098-113::/page/9/Text/56` | 0.464637 | **BACKGROUNDS** |
| 4 | `merged::PZO22001 Starfinder Player Core 114-125::/page/5/Text/38` | 0.464637 | **BACKGROUNDS** |
| 5 | `merged::PZO22001 Starfinder Player Core 098-113::/page/7/Text/67` | 0.464637 | **BACKGROUNDS** |
| 6 | `merged::PZO22001 Starfinder Player Core 098-113::/page/11/Text/44` | 0.464637 | **BACKGROUNDS** |
| 7 | `merged::PZO22001 Starfinder Player Core 114-125::/page/9/Text/76` | 0.464637 | **BACKGROUNDS** |
| 8 | `merged::PZO22001 Starfinder Player Core 406-423::/page/13/Text/31` | 0.464637 | **BACKGROUNDS** |
| 9 | `merged::PZO22001 Starfinder Player Core 162-173::/page/7/Text/48` | 0.464637 | **BACKGROUNDS** |
| 10 | `merged::PZO22001 Starfinder Player Core 114-125::/page/7/Text/49` | 0.464637 | **BACKGROUNDS** |

### Query 154
- Text: What is the rule about **TRAITS **?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 058-073::/page/0/SectionHeader/10']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 058-073::/page/0/SectionHeader/10', 'merged::PZO22001 Starfinder Player Core 058-073::/page/4/SectionHeader/12', 'merged::PZO22001 Starfinder Player Core 058-073::/page/8/SectionHeader/12', 'merged::PZO22001 Starfinder Player Core 058-073::/page/12/SectionHeader/10', 'merged::PZO22001 Starfinder Player Core 058-073::/page/0/Text/9', 'merged::PZO22001 Starfinder Player Core 058-073::/page/0/Text/11']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 058-073::/page/4/SectionHeader/12` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 058-073::/page/8/SectionHeader/12` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 058-073::/page/12/SectionHeader/10` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 058-073::/page/0/Text/9` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 058-073::/page/0/Text/11` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 058-073::/page/4/SectionHeader/12` | 0.817974 | **TRAITS ** |
| 2 | `merged::PZO22001 Starfinder Player Core 058-073::/page/0/SectionHeader/10` | 0.817974 | **TRAITS ** |
| 3 | `merged::PZO22001 Starfinder Player Core 040-057::/page/10/SectionHeader/9` | 0.719948 | TRAITS |
| 4 | `merged::PZO22001 Starfinder Player Core 040-057::/page/6/SectionHeader/12` | 0.719948 | TRAITS |
| 5 | `merged::PZO22001 Starfinder Player Core 040-057::/page/2/SectionHeader/11` | 0.719948 | TRAITS |
| 6 | `merged::PZO22001 Starfinder Player Core 058-073::/page/12/SectionHeader/10` | 0.719948 | TRAITS |
| 7 | `merged::PZO22001 Starfinder Player Core 040-057::/page/14/SectionHeader/14` | 0.719948 | TRAITS |
| 8 | `merged::PZO22001 Starfinder Player Core 058-073::/page/8/SectionHeader/12` | 0.719948 | TRAITS |
| 9 | `merged::PZO22001 Starfinder Player Core 040-057::/page/1/SectionHeader/26` | 0.719948 | TRAITS |
| 10 | `merged::PZO22001 Starfinder Player Core 442-464::/page/17/TableCell/347` | 0.673883 | Traits |

### Query 155
- Text: Summarize Maneuver in Flight ❖
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/98']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/98', 'merged::PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/99', 'merged::PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/97']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/99` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/97` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/98` | 0.745881 | Maneuver in Flight ❖ SqueezeE |
| 2 | `merged::PZO22001 Starfinder Player Core 182-209::/page/10/SectionHeader/36` | 0.713333 | **SAMPLE MANEUVER IN FLIGHT TASKS** |
| 3 | `merged::PZO22001 Starfinder Player Core 182-209::/page/10/SectionHeader/29` | 0.684289 | **MANEUVER IN FLIGHT **[one-action] |
| 4 | `merged::PZO22001 Starfinder Player Core 442-464::/page/7/Text/61` | 0.681816 | **Maneuver in Flight **[one-action] (skill action) Execute a difficult  movement while flying. (Acrobatics, trained) 192 |
| 5 | `merged::PZO22001 Starfinder Player Core 210-231::/page/4/TableCell/506` | 0.565522 | Stunt Maneuver |
| 6 | `merged::PZO22001 Starfinder Player Core 182-209::/page/10/Text/33` | 0.563212 | **Success** You succeed at the maneuver. |
| 7 | `merged::PZO22001 Starfinder Player Core 182-209::/page/10/Text/32` | 0.549533 | You try a difficult maneuver while flying. Attempt an Acrobatics  check. The GM determines what maneuvers are possible, but  they rarely allow you to move farther than your fly Speed. |
| 8 | `merged::PZO22001 Starfinder Player Core 406-423::/page/6/Text/21` | 0.539002 | As long as you have a fly Speed, you can use the Fly (page  411) and Arrest a Fall actions (page 410). You can also attempt  to Maneuver in Flight if you're trained in the Acrobatics skill. |
| 9 | `merged::PZO22001 Starfinder Player Core 182-209::/page/10/Text/34` | 0.535628 | **Failure** Your maneuver fails. The GM chooses if you simply  can't move or if some other detrimental effect happens.  The outcome should be appropriate for the maneuver you  attempted (for instance, |
| 10 | `merged::PZO22001 Starfinder Player Core 210-231::/page/19/SectionHeader/1` | 0.488407 | **STUNT MANEUVER** **FEAT 2** |

### Query 156
- Text: What is the rule about A character's acumen in skills can come from all sorts of  training, from piloting starships to researching a topic on  an infosphere to rehearsing a performing art. When you  create your character and as they advance in level, you  have flexibility as to which skills they become better at  and when. Some classes benefit more from improving  certain skills—such as the envoy's focus on their leadership  skill—but for most classes, you can choose whichever  skills make the most sense for your character's theme  and backstory at 1st level, then use their adventure and  downtime experiences to inform how their skills should  improve as your character levels up.?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 182-209::/page/1/Text/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 182-209::/page/1/Text/6', 'merged::PZO22001 Starfinder Player Core 182-209::/page/1/Text/2', 'merged::PZO22001 Starfinder Player Core 182-209::/page/1/Text/7']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 182-209::/page/1/Text/2` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 182-209::/page/1/Text/7` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 182-209::/page/1/Text/6` | 0.959137 | A character's acumen in skills can come from all sorts of  training, from piloting starships to researching a topic on  an infosphere to rehearsing a performing art. When you  create your character an |
| 2 | `merged::PZO22001 Starfinder Player Core 098-113::/page/2/Text/21` | 0.700909 | This section specifies the levels at which your character  can increase their proficiency rank in a skill. At 3rd level  and every 2 levels thereafter, most classes grant a skill  increase, though env |
| 3 | `merged::PZO22001 Starfinder Player Core 182-209::/page/1/Text/7` | 0.696968 | A character gains training in certain skills at 1st level:  typically two from their background, a small number of  predetermined skills from their class, and several skills of  your choice granted by |
| 4 | `merged::PZO22001 Starfinder Player Core 014-029::/page/0/Text/10` | 0.688808 | The rules for using skills are presented in this chapter,  and they detail what a character can do with a given  skill, based on that character's proficiency rank. Ancestry,  background, and class can |
| 5 | `merged::PZO22001 Starfinder Player Core 182-209::/page/2/Text/14` | 0.675676 | As your character advances in level, there are two  main ways their skills improve: skill increases and skill  feats. Your class lists the levels at which you gain each  of these improvements. |
| 6 | `merged::PZO22001 Starfinder Player Core 182-209::/page/1/Text/2` | 0.665763 | While your character's attributes represent their raw talent and potential, skills represent their  training and experience at performing certain tasks. Each skill is keyed to one of your character's |
| 7 | `merged::PZO22001 Starfinder Player Core 098-113::/page/2/Text/4` | 0.646037 | When you choose your character's class, they gain a set of  initial proficiencies. Proficiencies measure your character's  ability to perform tasks, use abilities, and succeed at  checks. Proficiency |
| 8 | `merged::PZO22001 Starfinder Player Core 098-113::/page/1/Text/2` | 0.644667 | Just as your character's ancestry plays a key role in expressing their identity and worldview, their  class indicates the training they have and will improve upon as an adventurer. Choosing your  char |
| 9 | `merged::PZO22001 Starfinder Player Core 098-113::/page/2/Text/17` | 0.636433 | This section specifies the levels at which your character gains  feats with the skill trait, called skill feats. Skill feats can be  found in Chapter 5, beginning on page 210. At 2nd level and  every |
| 10 | `merged::PZO22001 Starfinder Player Core 098-113::/page/8/Text/3` | 0.631379 | You gain more skill increases than members of other classes.  At 2nd level and every level thereafter, you gain a skill  increase. You can use this increase to either become trained  in one skill you' |

### Query 157
- Text: What is the rule about Example Characters?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/9']
- Expected found: `True`
- Expected rank: `11`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/9', 'merged::PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/1', 'merged::PZO22001 Starfinder Player Core 030-039::/page/4/SectionHeader/20', 'merged::PZO22001 Starfinder Player Core 030-039::/page/2/Text/8', 'merged::PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/31', 'merged::PZO22001 Starfinder Player Core 030-039::/page/3/SectionHeader/22', 'merged::PZO22001 Starfinder Player Core 030-039::/page/1/SectionHeader/19', 'merged::PZO22001 Starfinder Player Core 030-039::/page/4/SectionHeader/11', 'merged::PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/17', 'merged::PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/24', 'merged::PZO22001 Starfinder Player Core 030-039::/page/4/SectionHeader/3', 'merged::PZO22001 Starfinder Player Core 030-039::/page/3/SectionHeader/13']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/1` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 030-039::/page/4/SectionHeader/20` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 030-039::/page/2/Text/8` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/31` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 030-039::/page/3/SectionHeader/22` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 030-039::/page/1/SectionHeader/19` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 030-039::/page/4/SectionHeader/11` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/17` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/24` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 030-039::/page/4/SectionHeader/3` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 030-039::/page/3/SectionHeader/13` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 030-039::/page/3/SectionHeader/13` | 0.787066 | Example Characters |
| 2 | `merged::PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/1` | 0.787066 | Example Characters |
| 3 | `merged::PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/24` | 0.787066 | Example Characters |
| 4 | `merged::PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/17` | 0.787066 | Example Characters |
| 5 | `merged::PZO22001 Starfinder Player Core 030-039::/page/3/SectionHeader/4` | 0.787066 | Example Characters |
| 6 | `merged::PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/31` | 0.787066 | Example Characters |
| 7 | `merged::PZO22001 Starfinder Player Core 030-039::/page/4/SectionHeader/20` | 0.787066 | Example Characters |
| 8 | `merged::PZO22001 Starfinder Player Core 030-039::/page/1/SectionHeader/7` | 0.787066 | Example Characters |
| 9 | `merged::PZO22001 Starfinder Player Core 030-039::/page/4/SectionHeader/3` | 0.787066 | Example Characters |
| 10 | `merged::PZO22001 Starfinder Player Core 030-039::/page/4/SectionHeader/11` | 0.787066 | Example Characters |

### Query 158
- Text: What does **TELEPORT** **SPELL 6** do?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 364-387::/page/3/SectionHeader/30']
- Expected found: `True`
- Expected rank: `18`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 364-387::/page/3/SectionHeader/30', 'merged::PZO22001 Starfinder Player Core 364-387::/page/3/SectionHeader/41', 'merged::PZO22001 Starfinder Player Core 364-387::/page/3/Text/29']
- Expanded expected found: `True`
- Expanded expected rank: `18`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 364-387::/page/3/SectionHeader/41` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 364-387::/page/3/Text/29` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 442-464::/page/19/Text/83` | 0.505013 | **EQUIPMENT** **SPELLS** |
| 2 | `merged::PZO22001 Starfinder Player Core 364-387::/page/21/Text/54` | 0.505013 | **EQUIPMENT** **SPELLS** |
| 3 | `merged::PZO22001 Starfinder Player Core 040-057::/page/17/Text/75` | 0.505013 | **EQUIPMENT** **SPELLS** |
| 4 | `merged::PZO22001 Starfinder Player Core 182-209::/page/13/Text/49` | 0.505013 | **EQUIPMENT** **SPELLS** |
| 5 | `merged::PZO22001 Starfinder Player Core 406-423::/page/11/Text/25` | 0.505013 | **EQUIPMENT** **SPELLS** |
| 6 | `merged::PZO22001 Starfinder Player Core 040-057::/page/5/Text/85` | 0.505013 | **EQUIPMENT** **SPELLS** |
| 7 | `merged::PZO22001 Starfinder Player Core 442-464::/page/1/Text/58` | 0.505013 | **EQUIPMENT** **SPELLS** |
| 8 | `merged::PZO22001 Starfinder Player Core 406-423::/page/5/Text/52` | 0.505013 | **EQUIPMENT** **SPELLS** |
| 9 | `merged::PZO22001 Starfinder Player Core 364-387::/page/9/Text/57` | 0.505013 | **EQUIPMENT** **SPELLS** |
| 10 | `merged::PZO22001 Starfinder Player Core 406-423::/page/3/Text/39` | 0.505013 | **EQUIPMENT** **SPELLS** |

### Query 159
- Text: What is the rule about In Starfinder, the players take on the role of **player characters ** **(PCs)**, while the Game Master portrays **nonplayer characters ** **(NPCs)** and **monsters**. While PCs and NPCs are both important  to the story, they serve very different purposes in the game.  PCs are the protagonists—the narrative is about them—while  NPCs are allies, contacts, adversaries, and villains. That said,  PCs, NPCs, and monsters share several characteristics.?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 001-013::/page/5/Text/21']
- Expected found: `False`
- Expected rank: `None`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 001-013::/page/5/Text/21', 'merged::PZO22001 Starfinder Player Core 001-013::/page/5/Text/22', 'merged::PZO22001 Starfinder Player Core 001-013::/page/5/SectionHeader/20']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 001-013::/page/5/Text/22` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 001-013::/page/5/SectionHeader/20` (reasons: ['graph_depth_1'])

### Query 160
- Text: Summarize **affliction** An affliction can affect a creature for a long time,  over several different stages. The most common kinds are  curses, diseases, and poisons. 422–423
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 442-464::/page/0/Text/27']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 442-464::/page/0/Text/27', 'merged::PZO22001 Starfinder Player Core 442-464::/page/0/Text/28', 'merged::PZO22001 Starfinder Player Core 442-464::/page/0/Text/26']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 442-464::/page/0/Text/28` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 442-464::/page/0/Text/26` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 442-464::/page/0/Text/27` | 0.988250 | **affliction** An affliction can affect a creature for a long time,  over several different stages. The most common kinds are  curses, diseases, and poisons. 422–423 |
| 2 | `merged::PZO22001 Starfinder Player Core 406-423::/page/16/Text/2` | 0.794585 | Diseases and poisons are types of afflictions, as are curses and radiation. An affliction can infect a  creature for a long time, progressing through different and often increasingly debilitating stag |
| 3 | `merged::PZO22001 Starfinder Player Core 406-423::/page/16/Text/7` | 0.679590 | The affliction's name is given first, followed by its traits in  parentheses—including the trait for the type of affliction  (curse, disease, poison, and so forth). If the affliction needs  to have a |
| 4 | `merged::PZO22001 Starfinder Player Core 406-423::/page/16/Text/17` | 0.633712 | An affliction typically has multiple stages, each of which lists |
| 5 | `merged::PZO22001 Starfinder Player Core 294-329::/page/14/Text/29` | 0.615014 | **Cleanse Affliction**H Treat a curse, disease, or poison. |
| 6 | `merged::PZO22001 Starfinder Player Core 294-329::/page/11/Text/73` | 0.615014 | **Cleanse Affliction**H Treat a curse, disease, or poison. |
| 7 | `merged::PZO22001 Starfinder Player Core 294-329::/page/17/Text/22` | 0.615014 | **Cleanse Affliction**H Treat a curse, disease, or poison. |
| 8 | `merged::PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/39` | 0.593782 | **CLEANSE AFFLICTION **[two-actions] **SPELL 2**  **CONCENTRATE** **HEALING** **MANIPULATE**  **Traditions** divine, occult, primal  **Range **touch; **Targets** 1 willing creature  Gentle restorative |
| 9 | `merged::PZO22001 Starfinder Player Core 406-423::/page/16/Text/5` | 0.588137 | Whether appearing in a spell, as an item, or within a creature's  stat block, afflictions appear in the following format. |
| 10 | `merged::PZO22001 Starfinder Player Core 406-423::/page/16/Text/18` | 0.584943 | an effect followed by an interval in parentheses. When you  reach a given stage of an affliction, you're subjected to the  effects listed for that stage. |

### Query 161
- Text: Summarize **Skittermander**
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 040-057::/page/1/Text/45']
- Expected found: `False`
- Expected rank: `None`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 040-057::/page/1/Text/45', 'merged::PZO22001 Starfinder Player Core 040-057::/page/1/Text/46', 'merged::PZO22001 Starfinder Player Core 040-057::/page/1/Text/44']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 040-057::/page/1/Text/46` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 040-057::/page/1/Text/44` (reasons: ['graph_depth_1'])

### Query 162
- Text: What is the rule about At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As a lashunta, you choose from among  the following ancestry feats.?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 058-073::/page/2/Text/7']
- Expected found: `True`
- Expected rank: `1`
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
| 8 | `merged::PZO22001 Starfinder Player Core 098-113::/page/8/Text/14` | 0.740603 | In addition to the initial ancestry feat you started with, you  gain an ancestry feat at 5th level and every 4 levels thereafter. |
| 9 | `merged::PZO22001 Starfinder Player Core 058-073::/page/14/Text/7` | 0.719925 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As a skittermander, you choose from  among the follo |
| 10 | `merged::PZO22001 Starfinder Player Core 040-057::/page/1/Text/33` | 0.715065 | This section presents ancestry feats, which allow you to  customize your character. You gain your first ancestry feat  at 1st level, and you gain another at 5th level, 9th level, 13th  level, and 17th |

### Query 163
- Text: Summarize 6 PLAYER CORE
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 268-281::/page/1/SectionHeader/0']
- Expected found: `False`
- Expected rank: `None`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 268-281::/page/1/SectionHeader/0', 'merged::PZO22001 Starfinder Player Core 268-281::/page/1/Text/1', 'merged::PZO22001 Starfinder Player Core 268-281::/page/0/Text/53']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 268-281::/page/1/Text/1` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 268-281::/page/0/Text/53` (reasons: ['graph_depth_1'])

### Query 164
- Text: What are the requirements for **GUARDED THOUGHTS** **FEAT 9**?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/24']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/24', 'merged::PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/23', 'merged::PZO22001 Starfinder Player Core 058-073::/page/3/Text/26']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/23` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 058-073::/page/3/Text/26` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/24` | 0.826835 | **GUARDED THOUGHTS** **FEAT 9** |
| 2 | `merged::PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/32` | 0.512869 | **PSYCHIC MASTER** **FEAT 9** |
| 3 | `merged::PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/22` | 0.511712 | **HARMONIC SHIELDING** **FEAT 9** |
| 4 | `merged::PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/28` | 0.508375 | **PSYCHIC MASTERY** **FEAT 9** |
| 5 | `merged::PZO22001 Starfinder Player Core 174-181::/page/5/SectionHeader/36` | 0.465258 | **PRIMARY TARGET** **FEAT 10** |
| 6 | `merged::PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/26` | 0.453252 | **BASIC INSECTILE FLIGHT** **FEAT 9** |
| 7 | `merged::PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/26` | 0.451035 | **MELODIC ADAPTATION** **FEAT 9** |
| 8 | `merged::PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/16` | 0.444988 | **REALLY GET EM!** **FEAT 8** |
| 9 | `merged::PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/13` | 0.442618 | **CENTER THOUGHTS **[free-action] **FEAT 1** |
| 10 | `merged::PZO22001 Starfinder Player Core 058-073::/page/15/SectionHeader/13` | 0.438122 | **ALL HANDS ON DECK **[free-action] **FEAT 9** |

### Query 165
- Text: What is the rule about **Downtime mode** (page 433) takes place over days. You  might make money, train, or recover, among other things.?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 388-405::/page/2/Text/6']
- Expected found: `True`
- Expected rank: `1`
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
| 3 | `merged::PZO22001 Starfinder Player Core 442-464::/page/4/Text/23` | 0.607949 | **downtime** A mode of play in which characters are not  adventuring. Days pass quickly at the table, and characters  engage in long-term activities. 9, 390–391, **433–434** downtime activities 433–43 |
| 4 | `merged::PZO22001 Starfinder Player Core 424-441::/page/9/Text/1` | 0.605663 | Downtime mode is played day-by-day rather than minute-by-minute or scene-by-scene. Usually,  this mode of play occurs when you're in the safety of a settlement, maybe recovering from your  adventures |
| 5 | `merged::PZO22001 Starfinder Player Core 406-423::/page/11/Text/42` | 0.590756 | **Mode** **Downtime ** |
| 6 | `merged::PZO22001 Starfinder Player Core 388-405::/page/2/Text/5` | 0.585882 | **Exploration** **mode** (page 430) takes place over minutes or  hours. You use your travel Speed if you're moving, and you  engage in **exploration** **activities** like Avoiding Notice, Detecting  M |
| 7 | `merged::PZO22001 Starfinder Player Core 388-405::/page/15/Text/42` | 0.578471 | **Downtime ** **Mode** |
| 8 | `merged::PZO22001 Starfinder Player Core 406-423::/page/3/Text/56` | 0.578471 | **Downtime ** **Mode** |
| 9 | `merged::PZO22001 Starfinder Player Core 388-405::/page/9/Text/42` | 0.578471 | **Downtime ** **Mode** |
| 10 | `merged::PZO22001 Starfinder Player Core 388-405::/page/7/Text/37` | 0.578471 | **Downtime ** **Mode** |

### Query 166
- Text: Summarize **Requirements** You have a focus pool.
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 294-329::/page/2/Text/19']
- Expected found: `False`
- Expected rank: `None`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 294-329::/page/2/Text/19', 'merged::PZO22001 Starfinder Player Core 294-329::/page/2/Text/20', 'merged::PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/18']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 294-329::/page/2/Text/20` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/18` (reasons: ['graph_depth_1'])

### Query 167
- Text: What is the rule about You reshape terrain and manipulate events to match other realities. You cast powerful  spells and recenter yourself through your anchor when pushed to your limits.?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 162-173::/page/1/Text/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 162-173::/page/1/Text/13', 'merged::PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/12', 'merged::PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/14']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/12` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/14` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 162-173::/page/1/Text/13` | 0.867532 | You reshape terrain and manipulate events to match other realities. You cast powerful  spells and recenter yourself through your anchor when pushed to your limits. |
| 2 | `merged::PZO22001 Starfinder Player Core 098-113::/page/1/Text/4` | 0.591557 | The rules within each class allow you to bring a wealth of  character concepts to life. Perhaps you want to create an  observant but impulsive mystic who can see the pain in  someone's eyes but can't |
| 3 | `merged::PZO22001 Starfinder Player Core 162-173::/page/1/Text/2` | 0.563612 | A strange paradoxical event forever altered your existence, and now you can manipulate reality. You  explore the infinite possibilities of the multiverse, possibly visualizing variant timelines or par |
| 4 | `merged::PZO22001 Starfinder Player Core 162-173::/page/3/Text/3` | 0.552339 | Your paradox grants you magical power. You can cast spells  using the Cast a Spell activity. As a witchwarper, when you  cast spells, you might describe your revelations about other  realities aloud, |
| 5 | `merged::PZO22001 Starfinder Player Core 406-423::/page/2/Text/33` | 0.538460 | You use your hand or hands to manipulate an object or the  terrain. You can grab an unattended or stored object, draw  a weapon, swap a held item for another (see the Changing  Equipment table on page |
| 6 | `merged::PZO22001 Starfinder Player Core 364-387::/page/14/ListItem/14` | 0.537254 | You suppress terrain in your field, turning any existing  difficult or greater difficult terrain in your quantum field  to normal terrain. This does not apply to effects that  cause a creature to coun |
| 7 | `merged::PZO22001 Starfinder Player Core 162-173::/page/10/Text/49` | 0.532352 | By reaching across both time and space, you can borrow the  use of a spell from a version of yourself inhabiting another  reality. During this turn, you can cast one spell without  spending a spell sl |
| 8 | `merged::PZO22001 Starfinder Player Core 162-173::/page/1/Text/19` | 0.530282 | You craft magic items for your party. You might travel to other dimensions or distant  star systems as part of your training or embark on such journeys by accident. |
| 9 | `merged::PZO22001 Starfinder Player Core 162-173::/page/6/Text/26` | 0.529886 | Your anchor keeps you centered, reminding you what's  real, and helps counter the disorienting effects one might  experience by causing paradoxes. You select your anchor at 1st  level. Your anchor gra |
| 10 | `merged::PZO22001 Starfinder Player Core 406-423::/page/8/Text/22` | 0.529381 | Usually the creature or effect forcing the movement  chooses the path the victim takes. If you're pushed or  pulled, you can usually be moved through hazardous  terrain, pushed out of an airlock, or t |

### Query 168
- Text: Summarize Carbon shield, commercial
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/630']
- Expected found: `True`
- Expected rank: `1`
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
| 5 | `merged::PZO22001 Starfinder Player Core 282-293::/page/11/TableCell/764` | 0.665202 | Shielding skin, commercial |
| 6 | `merged::PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/657` | 0.660509 | Irising shield, commercial |
| 7 | `merged::PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/684` | 0.650180 | Riot shield, commercial |
| 8 | `merged::PZO22001 Starfinder Player Core 250-267::/page/1/Text/13` | 0.576039 | **Carbon** **Shield:** This durable yet lightweight defensive  plate comes in a variety of shapes and sizes, and it's often  customized with LED displays that broadcast personal  insignia or an organi |
| 9 | `merged::PZO22001 Starfinder Player Core 250-267::/page/1/Table/2` | 0.551039 | ShieldLevelPriceAC Bonus1Speed PenaltyBulkHardnessHP (BT)TraitsCarbon shield, commercial025+2—1520 (10)AnalogCompact shield, commercial015+1—L48 (4)Analog, compactDeflecting field, commercial010+1——24 |
| 10 | `merged::PZO22001 Starfinder Player Core 268-281::/page/3/TableCell/743` | 0.532080 | Energy shielding, advanced |

### Query 169
- Text: What is the rule about All tasks that take longer than a turn are activities. If an  activity is meant to be done during exploration, it has the  exploration trait. An activity that takes a day or more of  commitment and that can be done only during downtime  has the downtime trait.?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 014-029::/page/2/Text/4']
- Expected found: `False`
- Expected rank: `None`
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
| 6 | `merged::PZO22001 Starfinder Player Core 126-137::/page/7/Text/21` | 0.552739 | You dash across the battlefield, tearing up your surroundings  and toppling nearby objects as you go to make it harder  for your foes to maneuver or to give chase. Stride up to  your Speed. The square |
| 7 | `merged::PZO22001 Starfinder Player Core 098-113::/page/5/Text/11` | 0.551157 | You issue directives to your allies, granting benefits and letting you take the lead.  Your words and deeds bolster your allies or harry your foes, and your cunning can  get you and your team out of d |
| 8 | `merged::PZO22001 Starfinder Player Core 098-113::/page/6/Text/19` | 0.547784 | You're most comfortable leading your allies from the front lines  of battle while you fight alongside them. You might raise a  shield to help weather the storm of incoming gunfire or simply  lead with |
| 9 | `merged::PZO22001 Starfinder Player Core 150-161::/page/2/Text/9` | 0.542673 | You have a knack for using powerful weapons to harry your  foes and hinder their movement, preventing them from  operating at their peak. If you make an attack with a weapon  that has the area trait ( |
| 10 | `merged::PZO22001 Starfinder Player Core 138-149::/page/1/Text/17` | 0.539330 | You likely stick near the front of the group to quickly get into the fight. You use  your powers to overcome challenges, like moving debris or climbing strange terrain. |

### Query 171
- Text: What are the requirements for **ATTUNED WARDS** **FEAT 18**?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 138-149::/page/11/SectionHeader/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 138-149::/page/11/SectionHeader/11', 'merged::PZO22001 Starfinder Player Core 138-149::/page/11/SectionHeader/13', 'merged::PZO22001 Starfinder Player Core 138-149::/page/11/SectionHeader/10']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 138-149::/page/11/SectionHeader/13` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 138-149::/page/11/SectionHeader/10` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 138-149::/page/11/SectionHeader/11` | 0.849378 | **ATTUNED WARDS** **FEAT 18** |
| 2 | `merged::PZO22001 Starfinder Player Core 114-125::/page/11/SectionHeader/13` | 0.546986 | **NETWORK ATTUNEMENT **[one-action] **FEAT 18** |
| 3 | `merged::PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/559` | 0.525432 | Attuned Wards |
| 4 | `merged::PZO22001 Starfinder Player Core 162-173::/page/11/SectionHeader/14` | 0.521713 | **COMPLETE TRANSPOSITION** **FEAT 18** |
| 5 | `merged::PZO22001 Starfinder Player Core 138-149::/page/11/SectionHeader/2` | 0.518203 | **ATTUNED BLOW** **FEAT 16** |
| 6 | `merged::PZO22001 Starfinder Player Core 162-173::/page/11/SectionHeader/19` | 0.472004 | **INFINITE MAGIC** **FEAT 18** |
| 7 | `merged::PZO22001 Starfinder Player Core 138-149::/page/11/SectionHeader/26` | 0.466703 | **PERFECTLY-ATTUNED** **FEAT 20** |
| 8 | `merged::PZO22001 Starfinder Player Core 126-137::/page/11/SectionHeader/14` | 0.462388 | **RELENTLESS AIM** **FEAT 18** |
| 9 | `merged::PZO22001 Starfinder Player Core 138-149::/page/11/SectionHeader/17` | 0.455177 | **HOMING MOTE** **FEAT 18** |
| 10 | `merged::PZO22001 Starfinder Player Core 138-149::/page/7/Text/18` | 0.447791 | **Requirements** You're photon-attuned. |

### Query 172
- Text: Summarize HP (BT)
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/628']
- Expected found: `True`
- Expected rank: `1`
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
| 3 | `merged::PZO22001 Starfinder Player Core 442-464::/page/15/TableCell/69` | 0.711262 | Hardness Max HP BT HP |
| 4 | `merged::PZO22001 Starfinder Character Sheet::/page/0/TableCell/60` | 0.639573 | Hardness Max HP BT HP Armor Proficiencies |
| 5 | `merged::PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/698` | 0.633690 | HP |
| 6 | `merged::PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/699` | 0.551162 | BT |
| 7 | `merged::PZO22001 Starfinder Player Core 442-464::/page/2/Text/7` | 0.536996 | **Broken Threshold (BT)** When an object's HP reaches this  number, it becomes broken. 236 |
| 8 | `merged::PZO22001 Starfinder Player Core 442-464::/page/15/TableCell/67` | 0.532817 | HP Temporary HP |
| 9 | `merged::PZO22001 Starfinder Character Sheet::/page/0/TableCell/58` | 0.532817 | HP Temporary HP |
| 10 | `merged::PZO22001 Starfinder Player Core 250-267::/page/0/Text/14` | 0.511955 | This column lists the shield's Hit Points (HP) and Broken  Threshold (BT). These measure how much damage the shield  can take before it's destroyed (its total HP) and how much it  can take before bein |

### Query 173
- Text: What are the requirements for **Prerequisites** Envoy Dedication?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 174-181::/page/1/Text/34']
- Expected found: `True`
- Expected rank: `4`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 174-181::/page/1/Text/34', 'merged::PZO22001 Starfinder Player Core 174-181::/page/1/Text/35', 'merged::PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/33']
- Expanded expected found: `True`
- Expanded expected rank: `4`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 174-181::/page/1/Text/35` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/33` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 174-181::/page/1/Text/24` | 0.901082 | **Prerequisites** Envoy Dedication |
| 2 | `merged::PZO22001 Starfinder Player Core 174-181::/page/1/Text/19` | 0.901082 | **Prerequisites** Envoy Dedication |
| 3 | `merged::PZO22001 Starfinder Player Core 174-181::/page/1/Text/39` | 0.901082 | **Prerequisites** Envoy Dedication |
| 4 | `merged::PZO22001 Starfinder Player Core 174-181::/page/1/Text/34` | 0.901082 | **Prerequisites** Envoy Dedication |
| 5 | `merged::PZO22001 Starfinder Player Core 174-181::/page/5/Text/39` | 0.601078 | **Prerequisites** Soldier Dedication |
| 6 | `merged::PZO22001 Starfinder Player Core 174-181::/page/5/Text/18` | 0.601078 | **Prerequisites** Soldier Dedication |
| 7 | `merged::PZO22001 Starfinder Player Core 174-181::/page/5/Text/34` | 0.601078 | **Prerequisites** Soldier Dedication |
| 8 | `merged::PZO22001 Starfinder Player Core 174-181::/page/3/Text/60` | 0.578570 | **Prerequisites** Operative Dedication |
| 9 | `merged::PZO22001 Starfinder Player Core 174-181::/page/3/Text/50` | 0.578570 | **Prerequisites** Operative Dedication |
| 10 | `merged::PZO22001 Starfinder Player Core 174-181::/page/3/Text/55` | 0.578570 | **Prerequisites** Operative Dedication |

### Query 174
- Text: Summarize Fast Recovery
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/430']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/430', 'merged::PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/431', 'merged::PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/429']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/431` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/429` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/430` | 0.881665 | Fast Recovery |
| 2 | `merged::PZO22001 Starfinder Player Core 210-231::/page/10/SectionHeader/34` | 0.732739 | **FAST RECOVERY** **FEAT 1** |
| 3 | `merged::PZO22001 Starfinder Player Core 210-231::/page/4/TableCell/418` | 0.638074 | Robust Recovery |
| 4 | `merged::PZO22001 Starfinder Player Core 210-231::/page/4/TableCell/414` | 0.591125 | Continual Recovery |
| 5 | `merged::PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/433` | 0.537124 | Regain more HP from rest, recover faster from disease |
| 6 | `merged::PZO22001 Starfinder Player Core 210-231::/page/16/SectionHeader/36` | 0.506617 | **QUICK REPAIR** **FEAT 1** |
| 7 | `merged::PZO22001 Starfinder Player Core 210-231::/page/17/SectionHeader/18` | 0.496581 | **ROBUST RECOVERY** **FEAT 2** |
| 8 | `merged::PZO22001 Starfinder Player Core 210-231::/page/8/SectionHeader/8` | 0.491982 | **CONTINUAL RECOVERY** **FEAT 2** |
| 9 | `merged::PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/457` | 0.482783 | Increase your maximum HP and reduce the DCs of recovery checks |
| 10 | `merged::PZO22001 Starfinder Player Core 442-464::/page/6/Text/23` | 0.479650 | **heroic recovery** 404 |

### Query 175
- Text: Summarize The pahtra solarian **Dae** loves showing off  by combining their flashy dance moves with  solar flares or turning their battle ribbon into  a electrotether or a whip of solar fire.
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 098-113::/page/3/Text/14']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 098-113::/page/3/Text/14', 'merged::PZO22001 Starfinder Player Core 098-113::/page/3/Text/15', 'merged::PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/13']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 098-113::/page/3/Text/15` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/13` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 098-113::/page/3/Text/14` | 0.989924 | The pahtra solarian **Dae** loves showing off  by combining their flashy dance moves with  solar flares or turning their battle ribbon into  a electrotether or a whip of solar fire. |
| 2 | `merged::PZO22001 Starfinder Player Core 182-209::/page/6/Text/10` | 0.554048 | Dae is a 16th-level solarian and a legendary dancer.  With their Meyel's Melody ancestry feat they have  a +2 status bonus to Performance checks, for a total  Performance modifier of +30. |
| 3 | `merged::PZO22001 Starfinder Player Core 138-149::/page/2/Text/22` | 0.550789 | A small mote of solar power hovers nearby or appears embedded  on some part of your body, such as the palm of your hand or on  your face. This mote can unleash a directed blast of energy at  short ran |
| 4 | `merged::PZO22001 Starfinder Player Core 138-149::/page/6/Text/7` | 0.529140 | **Manifestation:** Feats with this trait enhance or  alter your solar manifestations (flare, nimbus, and  weapon) or allow you to create a new type of solar  manifestation. |
| 5 | `merged::PZO22001 Starfinder Player Core 138-149::/page/5/Text/43` | 0.525599 | Your attacks create a brilliant eclipse that veil you from  the enemy's view. Make a Strike with your solar weapon or  your solar flare. On a hit, you create an impressive display of  solar energy bet |
| 6 | `merged::PZO22001 Starfinder Player Core 182-209::/page/6/SectionHeader/9` | 0.520899 | **Dae Performs in a Dance Contest** |
| 7 | `merged::PZO22001 Starfinder Player Core 138-149::/page/9/Text/28` | 0.518158 | You fire blasts of solar energy through your raised shield,  harnessing its gravitational force to propel your attacks.  When you make a solar flare Strike while you have your solar |
| 8 | `merged::PZO22001 Starfinder Player Core 138-149::/page/4/Text/26` | 0.500608 | You're a paragon among solarians, capable of shaping stellar  forces into powerful weapons that bend to your will. Your  proficiency ranks for your solar flare and solar weapon  increase to legendary. |
| 9 | `merged::PZO22001 Starfinder Player Core 098-113::/page/3/Text/11` | 0.497232 | The solarian is a warrior who channels the  cosmic cycle. Every solarian creates weapons of pure  stellar energy that they can manifest at will. Cycling  between graviton and photon attunement, a sola |
| 10 | `merged::PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/13` | 0.489450 | **Dae** |

### Query 176
- Text: What are the requirements for **Prerequisites** trained in Deception?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 210-231::/page/7/Text/34']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 210-231::/page/7/Text/34', 'merged::PZO22001 Starfinder Player Core 210-231::/page/7/Text/33', 'merged::PZO22001 Starfinder Player Core 210-231::/page/7/Text/35']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 210-231::/page/7/Text/33` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 210-231::/page/7/Text/35` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 210-231::/page/7/Text/34` | 0.889915 | **Prerequisites** trained in Deception |
| 2 | `merged::PZO22001 Starfinder Player Core 210-231::/page/10/Text/42` | 0.889915 | **Prerequisites** trained in Deception |
| 3 | `merged::PZO22001 Starfinder Player Core 098-113::/page/10/Text/23` | 0.889915 | **Prerequisites** trained in Deception |
| 4 | `merged::PZO22001 Starfinder Player Core 210-231::/page/10/Text/25` | 0.889915 | **Prerequisites** trained in Deception |
| 5 | `merged::PZO22001 Starfinder Player Core 210-231::/page/14/Text/10` | 0.889915 | **Prerequisites** trained in Deception |
| 6 | `merged::PZO22001 Starfinder Player Core 098-113::/page/12/Text/22` | 0.889915 | **Prerequisites** trained in Deception |
| 7 | `merged::PZO22001 Starfinder Player Core 210-231::/page/14/Text/5` | 0.889915 | **Prerequisites** trained in Deception |
| 8 | `merged::PZO22001 Starfinder Player Core 210-231::/page/8/Text/6` | 0.806080 | **Prerequisites** expert in Deception |
| 9 | `merged::PZO22001 Starfinder Player Core 210-231::/page/10/Text/52` | 0.806080 | **Prerequisites** expert in Deception |
| 10 | `merged::PZO22001 Starfinder Player Core 210-231::/page/16/Text/15` | 0.806080 | **Prerequisites** expert in Deception |

### Query 177
- Text: What is the rule about **aeon** (weapon trait) 255?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 442-464::/page/0/Text/25']
- Expected found: `True`
- Expected rank: `1`
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
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Character Sheet::/page/0/TableCell/79', 'merged::PZO22001 Starfinder Character Sheet::/page/0/TableCell/80', 'merged::PZO22001 Starfinder Character Sheet::/page/0/TableCell/78']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Character Sheet::/page/0/TableCell/80` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Character Sheet::/page/0/TableCell/78` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Character Sheet::/page/0/TableCell/79` | 0.757535 | Languages — |
| 2 | `merged::PZO22001 Starfinder Player Core 074-091::/page/1/Text/44` | 0.561431 | **Languages** |
| 3 | `merged::PZO22001 Starfinder Player Core 058-073::/page/15/Text/82` | 0.561431 | **Languages** |
| 4 | `merged::PZO22001 Starfinder Player Core 040-057::/page/17/Text/71` | 0.561431 | **Languages** |
| 5 | `merged::PZO22001 Starfinder Player Core 040-057::/page/11/Text/44` | 0.561431 | **Languages** |
| 6 | `merged::PZO22001 Starfinder Player Core 040-057::/page/9/Text/66` | 0.561431 | **Languages** |
| 7 | `merged::PZO22001 Starfinder Player Core 040-057::/page/7/Text/45` | 0.561431 | **Languages** |
| 8 | `merged::PZO22001 Starfinder Player Core 074-091::/page/15/Text/48` | 0.561431 | **Languages** |
| 9 | `merged::PZO22001 Starfinder Player Core 058-073::/page/7/Text/72` | 0.561431 | **Languages** |
| 10 | `merged::PZO22001 Starfinder Player Core 040-057::/page/13/Text/76` | 0.561431 | **Languages** |

### Query 179
- Text: Summarize **CONCENTRATE** **EXPLORATION**
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/18']
- Expected found: `False`
- Expected rank: `None`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/18', 'merged::PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/17', 'merged::PZO22001 Starfinder Player Core 294-329::/page/2/Text/19']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/17` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 294-329::/page/2/Text/19` (reasons: ['graph_depth_1'])

### Query 180
- Text: What does **FIREBALL **[two-actions] **SPELL 3** do?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 330-363::/page/2/Text/48']
- Expected found: `False`
- Expected rank: `None`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 330-363::/page/2/Text/48', 'merged::PZO22001 Starfinder Player Core 330-363::/page/2/Text/56', 'merged::PZO22001 Starfinder Player Core 330-363::/page/2/Text/41']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 330-363::/page/2/Text/56` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 330-363::/page/2/Text/41` (reasons: ['graph_depth_1'])

### Query 181
- Text: Summarize ATTRIBUTE FLAW
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 040-057::/page/2/Text/7']
- Expected found: `False`
- Expected rank: `None`
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
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 294-329::/page/3/Text/2', 'merged::PZO22001 Starfinder Player Core 294-329::/page/3/Text/3', 'merged::PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/1']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 294-329::/page/3/Text/3` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/1` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 294-329::/page/3/Text/2` | 0.908193 | Spellcasters cast spells from one of four different spell lists, each representing a different magical tradition: arcane,  divine, occult, and primal. |
| 2 | `merged::PZO22001 Starfinder Player Core 294-329::/page/3/Text/3` | 0.653649 | Your class determines which tradition of magic your spells use. In some cases, such as when a mystic gains spells from  their connection or when a witchwarper learns spells from their paradox, you mig |
| 3 | `merged::PZO22001 Starfinder Player Core 442-464::/page/7/Text/59` | 0.614230 | **magical tradition** Arcane, divine, occult, and primal are the  traditions of magic. 297 |
| 4 | `merged::PZO22001 Starfinder Player Core 294-329::/page/3/Text/7` | 0.603608 | Arcane spellcasters use logic and  rationality to categorize the magic inherent  in the world around them. Because of its far-reaching  approach, the arcane tradition has the broadest spell  list, tho |
| 5 | `merged::PZO22001 Starfinder Player Core 114-125::/page/8/Text/34` | 0.603028 | **Prerequisites** connection with occult spellcasting |
| 6 | `merged::PZO22001 Starfinder Player Core 114-125::/page/9/Text/54` | 0.603028 | **Prerequisites** connection with occult spellcasting |
| 7 | `merged::PZO22001 Starfinder Player Core 174-181::/page/0/Text/16` | 0.584418 | Spellcasting archetypes always grant the ability to cast  cantrips in their dedication, and then they have a basic  spellcasting feat, an expert spellcasting feat, and a master  spellcasting feat. The |
| 8 | `merged::PZO22001 Starfinder Player Core 014-029::/page/0/Text/16` | 0.564861 | This chapter starts with rules for casting spells,  determining their effects, and negating foes' spells  (called counteracting). After that, the spell lists for  each spellcasting tradition are inclu |
| 9 | `merged::PZO22001 Starfinder Player Core 294-329::/page/1/Text/6` | 0.556239 | Characters of spellcasting classes can cast a number of spells  each day; the spells you can cast in a day are referred to as  spell slots. At 1st level, a character has only a small number  of 1st-ra |
| 10 | `merged::PZO22001 Starfinder Player Core 330-363::/page/3/Text/6` | 0.556175 | **Traditions** arcane, divine, occult, primal |

### Query 183
- Text: Lookup values for Varying Skill FeatsLevelPrerequisitesBenefitsAssurance1Trained in at least one skillReceive a fixed result on a skill checkDubious Knowledge1Trained in a skill with the
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 210-231::/page/1/Table/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 210-231::/page/1/Table/11', 'merged::PZO22001 Starfinder Player Core 210-231::/page/1/SectionHeader/10', 'merged::PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/482']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 210-231::/page/1/SectionHeader/10` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/482` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 210-231::/page/1/Table/11` | 0.725766 | Varying Skill FeatsLevelPrerequisitesBenefitsAssurance1Trained in at least one skillReceive a fixed result on a skill checkDubious Knowledge1Trained in a skill with the Recall Knowledge actionLearn tr |
| 2 | `merged::PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/482` | 0.626365 | Varying Skill Feats |
| 3 | `merged::PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/413` | 0.626365 | Varying Skill Feats |
| 4 | `merged::PZO22001 Starfinder Player Core 210-231::/page/1/Text/7` | 0.587049 | In addition to the skill feats specifically associated with  each skill, there are some that can be taken with various  skills or even all skills, like Assurance. |
| 5 | `merged::PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/489` | 0.575024 | Receive a fixed result on a skill check |
| 6 | `merged::PZO22001 Starfinder Player Core 210-231::/page/6/Text/42` | 0.567269 | You know basic facts off the top of your head. Choose a skill  you're an expert in that has the Recall Knowledge action and  for which you have the Assurance feat. You can use the Recall  Knowledge ac |
| 7 | `merged::PZO22001 Starfinder Player Core 210-231::/page/2/Table/1` | 0.565880 | Varying Skill FeatsLevelPrerequisitesBenefitsRecognize Spell1Trained in Arcana, Nature, Occultism, or ReligionIdentify a spell as a reaction as it's being castSeasoned1Trained in Alcohol Lore, Cooking |
| 8 | `merged::PZO22001 Starfinder Player Core 098-113::/page/2/Text/17` | 0.565326 | This section specifies the levels at which your character gains  feats with the skill trait, called skill feats. Skill feats can be  found in Chapter 5, beginning on page 210. At 2nd level and  every |
| 9 | `merged::PZO22001 Starfinder Player Core 210-231::/page/1/Text/6` | 0.563364 | you gain a skill feat, you must select a general feat with  the skill trait; you can't select a general feat that lacks the  skill trait. The level of a skill feat is typically the minimum  level at w |
| 10 | `merged::PZO22001 Starfinder Player Core 182-209::/page/4/Table/6` | 0.562692 | General Skill ActionProficiencyPageDecipher WritingTrained186Earn IncomeTrained186–188Identify MagicTrained188Learn a SpellTrained189–190Recall Knowledge [one-action]Untrained190–191SubsistUntrained19 |

### Query 184
- Text: Summarize **Rituals**
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 364-387::/page/1/Text/83']
- Expected found: `True`
- Expected rank: `21`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 364-387::/page/1/Text/83', 'merged::PZO22001 Starfinder Player Core 364-387::/page/1/Text/82', 'merged::PZO22001 Starfinder Player Core 364-387::/page/1/Text/84']
- Expanded expected found: `True`
- Expanded expected rank: `21`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 364-387::/page/1/Text/82` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 364-387::/page/1/Text/84` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 330-363::/page/27/Text/66` | 0.921113 | **Rituals** |
| 2 | `merged::PZO22001 Starfinder Player Core 364-387::/page/13/Text/79` | 0.921113 | **Rituals** |
| 3 | `merged::PZO22001 Starfinder Player Core 330-363::/page/19/Text/76` | 0.921113 | **Rituals** |
| 4 | `merged::PZO22001 Starfinder Player Core 364-387::/page/11/Text/64` | 0.921113 | **Rituals** |
| 5 | `merged::PZO22001 Starfinder Player Core 330-363::/page/15/Text/64` | 0.921113 | **Rituals** |
| 6 | `merged::PZO22001 Starfinder Player Core 330-363::/page/23/Text/73` | 0.921113 | **Rituals** |
| 7 | `merged::PZO22001 Starfinder Player Core 364-387::/page/17/Text/31` | 0.921113 | **Rituals** |
| 8 | `merged::PZO22001 Starfinder Player Core 364-387::/page/23/Text/45` | 0.921113 | **Rituals** |
| 9 | `merged::PZO22001 Starfinder Player Core 330-363::/page/9/Text/48` | 0.921113 | **Rituals** |
| 10 | `merged::PZO22001 Starfinder Player Core 364-387::/page/5/Text/76` | 0.921113 | **Rituals** |

### Query 185
- Text: What are the requirements for **Prerequisites** trained in Medicine?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/20']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/20', 'merged::PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/19', 'merged::PZO22001 Starfinder Player Core 098-113::/page/13/Text/21']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/19` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 098-113::/page/13/Text/21` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/20` | 0.875383 | **Prerequisites** trained in Medicine |
| 2 | `merged::PZO22001 Starfinder Player Core 210-231::/page/6/Text/61` | 0.875383 | **Prerequisites** trained in Medicine |
| 3 | `merged::PZO22001 Starfinder Player Core 210-231::/page/17/SectionHeader/21` | 0.717903 | **Prerequisites** expert in Medicine |
| 4 | `merged::PZO22001 Starfinder Player Core 210-231::/page/21/Text/9` | 0.717903 | **Prerequisites** expert in Medicine |
| 5 | `merged::PZO22001 Starfinder Player Core 210-231::/page/8/Text/11` | 0.717903 | **Prerequisites** expert in Medicine |
| 6 | `merged::PZO22001 Starfinder Player Core 210-231::/page/20/Text/28` | 0.717903 | **Prerequisites** expert in Medicine |
| 7 | `merged::PZO22001 Starfinder Player Core 210-231::/page/5/Text/18` | 0.701512 | **Prerequisites** master in Medicine |
| 8 | `merged::PZO22001 Starfinder Player Core 210-231::/page/4/TableCell/412` | 0.643139 | Trained in Medicine |
| 9 | `merged::PZO22001 Starfinder Player Core 210-231::/page/18/Text/38` | 0.632150 | **Prerequisites** trained in Religion |
| 10 | `merged::PZO22001 Starfinder Player Core 210-231::/page/13/Text/19` | 0.619084 | **Prerequisites** legendary in Medicine |

### Query 186
- Text: What is the rule about **Spells**?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 364-387::/page/5/Text/74']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 364-387::/page/5/Text/74', 'merged::PZO22001 Starfinder Player Core 364-387::/page/5/Text/75', 'merged::PZO22001 Starfinder Player Core 364-387::/page/5/Text/73']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 364-387::/page/5/Text/75` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 364-387::/page/5/Text/73` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 294-329::/page/33/Text/63` | 0.748799 | **Spells** |
| 2 | `merged::PZO22001 Starfinder Player Core 364-387::/page/5/Text/74` | 0.748799 | **Spells** |
| 3 | `merged::PZO22001 Starfinder Player Core 364-387::/page/13/Text/77` | 0.748799 | **Spells** |
| 4 | `merged::PZO22001 Starfinder Player Core 294-329::/page/29/Text/67` | 0.748799 | **Spells** |
| 5 | `merged::PZO22001 Starfinder Player Core 294-329::/page/9/Text/88` | 0.748799 | **Spells** |
| 6 | `merged::PZO22001 Starfinder Player Core 364-387::/page/11/Text/62` | 0.748799 | **Spells** |
| 7 | `merged::PZO22001 Starfinder Player Core 294-329::/page/1/Text/26` | 0.748799 | **Spells** |
| 8 | `merged::PZO22001 Starfinder Player Core 294-329::/page/35/Text/70` | 0.748799 | **Spells** |
| 9 | `merged::PZO22001 Starfinder Player Core 294-329::/page/27/Text/70` | 0.748799 | **Spells** |
| 10 | `merged::PZO22001 Starfinder Player Core 294-329::/page/31/Text/62` | 0.748799 | **Spells** |

### Query 187
- Text: Lookup values for ItemLevelPriceBulkBipod, commercial021Silencer, commercial010LUndermounted grenade
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 268-281::/page/9/Table/18']
- Expected found: `True`
- Expected rank: `1`
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
| 7 | `merged::PZO22001 Starfinder Player Core 282-293::/page/5/Table/1` | 0.566271 | ItemLevelPriceBulkHandsGlow up spell amp,commercial150L1Reusable grenade shell18011Hardlight handwraps, tactical2355——Jump spell amp260L11st-rank spell chip3600——2nd-rank spell gem3120——Akashic lens, |
| 8 | `merged::PZO22001 Starfinder Player Core 268-281::/page/9/TableCell/847` | 0.562437 | Undermounted grenade launcher, commercial |
| 9 | `merged::PZO22001 Starfinder Player Core 232-249::/page/9/Table/1` | 0.561306 | ItemLevelPriceBulkHandsCable line, tactical (50 Feet)2150L—Camping kit03022Chemalyzer1150L1Climbing kit, commercial0512Climbing kit, tactical34012Comm unitT17L1Container, ordinary01——Container, design |
| 10 | `merged::PZO22001 Starfinder Player Core 250-267::/page/15/Table/3` | 0.549238 | Simple RangSimple Ranged WeaponsWeapon (Commercial)Item LevelPriceDamageRangeReloadBulkHandsMagazineExpendUpgradesGroupWeapon TraitsAcid dart rifle0401d8 A80 ft.1125 projectiles11CorrosiveAnalogArc pi |

### Query 188
- Text: What is the rule about Attribute boosts, mystic feat, skill feat?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/407']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/407', 'merged::PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/406', 'merged::PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/408']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/406` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/408` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/427` | 0.852405 | Attribute boosts, mystic feat, skill feat |
| 2 | `merged::PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/407` | 0.852405 | Attribute boosts, mystic feat, skill feat |
| 3 | `merged::PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/429` | 0.694391 | Attribute boosts, skill feat, solarian feat |
| 4 | `merged::PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/409` | 0.694391 | Attribute boosts, skill feat, solarian feat |
| 5 | `merged::PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/391` | 0.692856 | Mystic feat, skill feat |
| 6 | `merged::PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/395` | 0.692856 | Mystic feat, skill feat |
| 7 | `merged::PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/399` | 0.692856 | Mystic feat, skill feat |
| 8 | `merged::PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/411` | 0.692856 | Mystic feat, skill feat |
| 9 | `merged::PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/415` | 0.692856 | Mystic feat, skill feat |
| 10 | `merged::PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/403` | 0.692856 | Mystic feat, skill feat |

### Query 189
- Text: What is the rule about Trained in spell attack modifier Trained in spell DC?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 162-173::/page/1/Text/65']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 162-173::/page/1/Text/65', 'merged::PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/64', 'merged::PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/66']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/64` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/66` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 162-173::/page/1/Text/65` | 0.879793 | Trained in spell attack modifier Trained in spell DC |
| 2 | `merged::PZO22001 Starfinder Player Core 114-125::/page/1/Text/64` | 0.879793 | Trained in spell attack modifier Trained in spell DC |
| 3 | `merged::PZO22001 Starfinder Player Core 162-173::/page/3/Text/6` | 0.638068 | Some of your spells require you to attempt a spell attack to  see how effective they are or have your enemies roll against  your spell DC (typically by attempting a saving throw). Your spell  attack m |
| 4 | `merged::PZO22001 Starfinder Player Core 114-125::/page/3/Text/6` | 0.635990 | Some of your spells require you to attempt a spell attack to  see how effective they are or have your enemies roll against  your spell DC (typically by attempting a saving throw). Since  your key attr |
| 5 | `merged::PZO22001 Starfinder Player Core 114-125::/page/4/Text/31` | 0.607392 | You channel magic through your connection.  Your proficiency ranks for spell attack  modifiers and spell DCs increase to master. |
| 6 | `merged::PZO22001 Starfinder Player Core 294-329::/page/3/Text/27` | 0.606706 | When you gain an innate spell, you become trained in  the spell attack modifier and spell DC statistics. At 12th  level, these proficiencies increase to expert. Unless noted  otherwise, Charisma is yo |
| 7 | `merged::PZO22001 Starfinder Player Core 162-173::/page/5/Text/9` | 0.584159 | You push way past the boundaries of magical theory to  embody the pinnacle of spellcasting. Your proficiency  ranks for spell attack modifier and spell DC increase to  legendary. |
| 8 | `merged::PZO22001 Starfinder Player Core 114-125::/page/4/Text/17` | 0.577577 | You've formed a more powerful bond with your connection.  Your proficiency ranks for spell attack modifiers and spell  DCs increase to expert. |
| 9 | `merged::PZO22001 Starfinder Player Core 162-173::/page/5/Text/5` | 0.566303 | Your spells are among the most potent across all possible  worlds. Your proficiency ranks for class DC, spell attack  modifier, and spell DC increase to master. |
| 10 | `merged::PZO22001 Starfinder Player Core 162-173::/page/4/Text/17` | 0.563636 | Extended practice of magic has improved your capabilities.  Your proficiency ranks for class DC, spell attack  modifier, and spell DC increase to expert. |

### Query 190
- Text: What are the requirements for **PSYCHIC BULLY** **FEAT 5**?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 058-073::/page/3/Text/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 058-073::/page/3/Text/5', 'merged::PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/4', 'merged::PZO22001 Starfinder Player Core 058-073::/page/3/Text/7']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/4` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 058-073::/page/3/Text/7` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 058-073::/page/3/Text/5` | 0.831741 | **PSYCHIC BULLY** **FEAT 5** |
| 2 | `merged::PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/9` | 0.632963 | **PSYCHIC SCHOLAR** **FEAT 5** |
| 3 | `merged::PZO22001 Starfinder Player Core 058-073::/page/3/Text/42` | 0.617205 | **Prerequisites** Psychic Bully, Psychic Scholar, or Psychic Talent |
| 4 | `merged::PZO22001 Starfinder Player Core 058-073::/page/3/Text/31` | 0.560013 | **Prerequisites** Psychic Talent |
| 5 | `merged::PZO22001 Starfinder Player Core 058-073::/page/11/Text/35` | 0.560013 | **Prerequisites** Psychic Talent |
| 6 | `merged::PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/29` | 0.533884 | **PSYCHIC TALENT** **FEAT 1** |
| 7 | `merged::PZO22001 Starfinder Player Core 058-073::/page/3/Text/1` | 0.533884 | **PSYCHIC TALENT** **FEAT 1** |
| 8 | `merged::PZO22001 Starfinder Player Core 058-073::/page/3/Text/60` | 0.524199 | **Prerequisites** Psychic Mastery |
| 9 | `merged::PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/28` | 0.501019 | **PSYCHIC MASTERY** **FEAT 9** |
| 10 | `merged::PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/32` | 0.491205 | **PSYCHIC MASTER** **FEAT 9** |

### Query 191
- Text: What are the requirements for **BORROW SPELL **[free-action] **FEAT 14**?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/44']
- Expected found: `False`
- Expected rank: `None`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/44', 'merged::PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/43', 'merged::PZO22001 Starfinder Player Core 162-173::/page/10/Text/46']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/43` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 162-173::/page/10/Text/46` (reasons: ['graph_depth_1'])

### Query 192
- Text: What is the rule about Background ——?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Character Sheet::/page/0/TableCell/26']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Character Sheet::/page/0/TableCell/26', 'merged::PZO22001 Starfinder Character Sheet::/page/0/TableCell/28', 'merged::PZO22001 Starfinder Character Sheet::/page/0/TableCell/24']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Character Sheet::/page/0/TableCell/28` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Character Sheet::/page/0/TableCell/24` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Character Sheet::/page/0/TableCell/26` | 0.684290 | Background —— |
| 2 | `merged::PZO22001 Starfinder Player Core 442-464::/page/15/TableCell/34` | 0.684290 | Background —— |
| 3 | `merged::PZO22001 Starfinder Player Core 040-057::/page/5/Text/80` | 0.616679 | **Backgrounds** |
| 4 | `merged::PZO22001 Starfinder Player Core 040-057::/page/9/Text/65` | 0.616679 | **Backgrounds** |
| 5 | `merged::PZO22001 Starfinder Player Core 040-057::/page/17/Text/70` | 0.616679 | **Backgrounds** |
| 6 | `merged::PZO22001 Starfinder Player Core 040-057::/page/7/Text/44` | 0.616679 | **Backgrounds** |
| 7 | `merged::PZO22001 Starfinder Player Core 092-097::/page/1/Text/57` | 0.616679 | **Backgrounds** |
| 8 | `merged::PZO22001 Starfinder Player Core 040-057::/page/3/Text/44` | 0.616679 | **Backgrounds** |
| 9 | `merged::PZO22001 Starfinder Player Core 040-057::/page/1/Text/51` | 0.616679 | **Backgrounds** |
| 10 | `merged::PZO22001 Starfinder Player Core 040-057::/page/11/Text/43` | 0.616679 | **Backgrounds** |

### Query 193
- Text: What is the rule about When you Sustain this spell, you can levitate the flame up to  10 feet. It then deals damage to each creature whose space  it shared at any point during its flight. This uses the same  damage and save, and you roll the damage once each time  you Sustain. A given creature can take damage from *floating * *flame* only once per round.?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 330-363::/page/3/Text/1']
- Expected found: `False`
- Expected rank: `None`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 330-363::/page/3/Text/1', 'merged::PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/0', 'merged::PZO22001 Starfinder Player Core 330-363::/page/3/Text/2']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/0` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 330-363::/page/3/Text/2` (reasons: ['graph_depth_1'])

### Query 194
- Text: Summarize **circumstance penalty** A penalty due to a situation. 392
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 442-464::/page/2/Text/30']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 442-464::/page/2/Text/30', 'merged::PZO22001 Starfinder Player Core 442-464::/page/2/Text/29', 'merged::PZO22001 Starfinder Player Core 442-464::/page/2/Text/31']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 442-464::/page/2/Text/29` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 442-464::/page/2/Text/31` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 442-464::/page/2/Text/30` | 0.979339 | **circumstance penalty** A penalty due to a situation. 392 |
| 2 | `merged::PZO22001 Starfinder Player Core 442-464::/page/2/Text/29` | 0.811640 | **circumstance bonus** A bonus due to a situation. 392 |
| 3 | `merged::PZO22001 Starfinder Player Core 442-464::/page/12/Text/46` | 0.677346 | **status penalty** A penalty that typically comes from a spell or  condition and represents a detrimental status. 392 |
| 4 | `merged::PZO22001 Starfinder Player Core 442-464::/page/9/Text/17` | 0.587291 | **penalty** A negative value added to a calculation. Add only  the worst penalty of a single type (circumstance, item,  status). 10, **392–393** |
| 5 | `merged::PZO22001 Starfinder Player Core 442-464::/page/9/Text/3` | 0.584068 | **off-guard** (condition) You take a –2 circumstance penalty to  AC. 438 |
| 6 | `merged::PZO22001 Starfinder Player Core 442-464::/page/14/Text/19` | 0.566006 | **untyped penalty** A penalty that doesn't list a type and is  cumulative with other untyped penalties. 392 |
| 7 | `merged::PZO22001 Starfinder Player Core 126-137::/page/10/ListItem/19` | 0.565573 | You take a –1 circumstance penalty to AC. |
| 8 | `merged::PZO22001 Starfinder Player Core 388-405::/page/8/Text/7` | 0.561998 | Penalties to AC come from situations and effects in much  the same way bonuses do. Circumstance penalties come from  unfavorable situations, and status penalties come from effects  that impede your ab |
| 9 | `merged::PZO22001 Starfinder Player Core 442-464::/page/7/Text/15` | 0.555301 | item bonus or penalty 392 |
| 10 | `merged::PZO22001 Starfinder Player Core 442-464::/page/2/Text/47` | 0.546982 | **condition** An ongoing effect that changes how a character  can act or alters some of their statistics. 10, 419, **435–441** redundant conditions 441 |

### Query 195
- Text: What is the rule about **Heightened (4th)** The spell's range is touch and it targets 1  willing creature.?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 330-363::/page/2/Text/24']
- Expected found: `False`
- Expected rank: `None`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 330-363::/page/2/Text/24', 'merged::PZO22001 Starfinder Player Core 330-363::/page/2/Text/23', 'merged::PZO22001 Starfinder Player Core 330-363::/page/2/Text/25']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 330-363::/page/2/Text/23` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 330-363::/page/2/Text/25` (reasons: ['graph_depth_1'])

### Query 196
- Text: What are the requirements for **GET IN THERE! **[one-action]** TO **[two-actions] **FEAT 2**?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/18']
- Expected found: `False`
- Expected rank: `None`
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/18', 'merged::PZO22001 Starfinder Player Core 098-113::/page/11/Text/19', 'merged::PZO22001 Starfinder Player Core 098-113::/page/11/Text/17']
- Expanded expected found: `False`
- Expanded expected rank: `None`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 098-113::/page/11/Text/19` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 098-113::/page/11/Text/17` (reasons: ['graph_depth_1'])

### Query 197
- Text: Summarize Task Difficulty
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/247']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/247', 'merged::PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/248', 'merged::PZO22001 Starfinder Player Core 182-209::/page/2/Table/4']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/248` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 182-209::/page/2/Table/4` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/247` | 0.826163 | Task Difficulty |
| 2 | `merged::PZO22001 Starfinder Player Core 182-209::/page/2/Table/4` | 0.565712 | Task DifficultySimple DCUntrained10Trained15Expert20Master30Legendary40 |
| 3 | `merged::PZO22001 Starfinder Player Core 182-209::/page/22/SectionHeader/11` | 0.488102 | **SAMPLE PERFORM TASKS** |
| 4 | `merged::PZO22001 Starfinder Player Core 182-209::/page/11/SectionHeader/2` | 0.472967 | **SAMPLE SQUEEZE TASKS** |
| 5 | `merged::PZO22001 Starfinder Player Core 182-209::/page/9/SectionHeader/28` | 0.453439 | **SAMPLE SUBSIST TASKS** |
| 6 | `merged::PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/437` | 0.445662 | Step into difficult terrain |
| 7 | `merged::PZO22001 Starfinder Player Core 182-209::/page/4/SectionHeader/20` | 0.428003 | **SAMPLE DECIPHER TASKS** |
| 8 | `merged::PZO22001 Starfinder Player Core 182-209::/page/10/SectionHeader/16` | 0.423230 | **SAMPLE BALANCE TASKS** |
| 9 | `merged::PZO22001 Starfinder Player Core 182-209::/page/5/TableCell/579` | 0.419281 | Task Level |
| 10 | `merged::PZO22001 Starfinder Player Core 406-423::/page/9/SectionHeader/11` | 0.418198 | Ignore Difficult Terrain |

### Query 198
- Text: What does **TRANSLATE **[two-actions] **SPELL 2** do?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 364-387::/page/4/SectionHeader/23']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `False`
- Graph boosted count: `0`
- Graph boost seed source: `top`
- Graph boost seed ids: []
- Expanded expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 364-387::/page/4/SectionHeader/23', 'merged::PZO22001 Starfinder Player Core 364-387::/page/4/SectionHeader/15', 'merged::PZO22001 Starfinder Player Core 364-387::/page/4/SectionHeader/30']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `merged::PZO22001 Starfinder Player Core 364-387::/page/4/SectionHeader/15` (reasons: ['graph_depth_1'])
  - `merged::PZO22001 Starfinder Player Core 364-387::/page/4/SectionHeader/30` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `merged::PZO22001 Starfinder Player Core 294-329::/page/7/Text/19` | 0.604220 | **SPELL NAME **[one-action] **SPELL (RANK)** |
| 2 | `merged::PZO22001 Starfinder Player Core 364-387::/page/4/SectionHeader/23` | 0.580204 | **TRANSLATE **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, occult **Range **30 feet;** Targets** 1 creature  **Duration** 1 hour  The target can understand |
| 3 | `merged::PZO22001 Starfinder Player Core 442-464::/page/13/Text/59` | 0.540846 | **SPELLS** |
| 4 | `merged::PZO22001 Starfinder Player Core 424-441::/page/13/Text/36` | 0.540846 | **SPELLS** |
| 5 | `merged::PZO22001 Starfinder Player Core 424-441::/page/9/Text/34` | 0.540846 | **SPELLS** |
| 6 | `merged::PZO22001 Starfinder Player Core 250-267::/page/3/Text/42` | 0.540846 | **SPELLS** |
| 7 | `merged::PZO22001 Starfinder Player Core 442-464::/page/3/Text/62` | 0.540846 | **SPELLS** |
| 8 | `merged::PZO22001 Starfinder Player Core 210-231::/page/5/Text/33` | 0.540846 | **SPELLS** |
| 9 | `merged::PZO22001 Starfinder Player Core 210-231::/page/7/Text/69` | 0.540846 | **SPELLS** |
| 10 | `merged::PZO22001 Starfinder Player Core 210-231::/page/13/Text/67` | 0.540846 | **SPELLS** |

### Query 199
- Text: What is the rule about If you want a character who's duty bound, brave, and stoic,  you should play a vesk.?
- Expected chunk IDs: ['merged::PZO22001 Starfinder Player Core 074-091::/page/1/Text/10']
- Expected found: `True`
- Expected rank: `1`
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
| 5 | `merged::PZO22001 Starfinder Player Core 014-029::/page/3/Text/8` | 0.522235 | What sort of character do you want to play? The answer  to this question might be as simple as "a starship pilot," or  as complicated as "a kasatha seer raised on a generation  ship far from their anc |
| 6 | `merged::PZO22001 Starfinder Player Core 014-029::/page/4/Text/11` | 0.510803 | Building a character around a specific ancestry,  background, or class can be a fun way to interact with the  galaxy's lore. For example, you could play a pacifist vesk who  prefers negotiation over c |
| 7 | `merged::PZO22001 Starfinder Player Core 074-091::/page/2/Text/7` | 0.508664 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As a vesk, you choose from among the  following ance |
| 8 | `merged::PZO22001 Starfinder Player Core 098-113::/page/1/Text/4` | 0.507903 | The rules within each class allow you to bring a wealth of  character concepts to life. Perhaps you want to create an  observant but impulsive mystic who can see the pain in  someone's eyes but can't |
| 9 | `merged::PZO22001 Starfinder Player Core 074-091::/page/2/Text/32` | 0.504374 | You're trained with all doshkos. In addition, you gain access to  all uncommon weapons with the vesk trait. For the purposes  of proficiency, you treat any of these that are martial weapons |
| 10 | `merged::PZO22001 Starfinder Player Core 014-029::/page/13/Text/45` | 0.502434 | Vesk are proud reptilian  conquerors with a strong  desire to prove their strength  honorably. Page 74. |
