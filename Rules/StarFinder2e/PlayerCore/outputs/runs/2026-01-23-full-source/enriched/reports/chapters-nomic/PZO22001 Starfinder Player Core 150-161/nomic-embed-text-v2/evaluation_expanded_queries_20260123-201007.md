# RulesLawyer Evaluation Report: nomic-embed-text-v2

## Summary
- Run ID: `None`
- Ruleset ID: `None`
- Document ID: `None`
- Chunk source: `enriched`
- Chunk count: `583`
- Query count: `153`
- Evaluated queries: `153`
- Coverage: `1.0000`
- MRR: `0.8975`
- hit@1: `0.8497`
- hit@3: `0.9216`
- hit@5: `0.9673`
- hit@10: `1.0000`
- Embeddings reused: `False`
- Graph boost: `0.05` (depth=2, top_k=50, source=top, seed_top_n=3, same_kind_only=False, decay=0.4)

### Expanded Gold Metrics
- Coverage: `1.0000`
- MRR: `0.9019`
- hit@1: `0.8562`
- hit@3: `0.9216`
- hit@5: `0.9673`
- hit@10: `1.0000`

### Expanded Gold Expansion Stats
- Queries with additions: `153`
- Avg added per query: `2.06`
- Max added: `7`
- Addition reasons:
  - graph_depth_1: `315`

### Expanded Gold Delta (Expanded - Strict)
- Coverage Δ: `0.0000`
- MRR Δ: `0.0044`
- hit@1 Δ: `0.0065`
- hit@3 Δ: `0.0000`
- hit@5 Δ: `0.0000`
- hit@10 Δ: `0.0000`

## Timings (ms)
- Embedding (chunks): `8621`
- Embedding (queries): `2695`
- Evaluation (strict): `30`
- Evaluation (expanded): `38`
- Total: `15651`

### Timing Estimates (ms)
- Evaluation (strict): `30`
- Evaluation (expanded): `30`
- Total: `11376`

## Query Details
### Query 0
- Text: Summarize SOLDIER
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/1', 'PZO22001 Starfinder Player Core 150-161::/page/10/Text/40', 'PZO22001 Starfinder Player Core 150-161::/page/10/Text/53']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/1', 'PZO22001 Starfinder Player Core 150-161::/page/1/Text/2']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/1/Text/2` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/1` | 0.929622 | SOLDIER |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/10/Text/40` | 0.835976 | **SOLDIER** |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/10/Text/53` | 0.835976 | **SOLDIER** |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/10/Text/36` | 0.793976 | **SOLDIER** |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/11/Text/19` | 0.793976 | **SOLDIER** |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/11/Text/14` | 0.793976 | **SOLDIER** |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/11/Text/10` | 0.793976 | **SOLDIER** |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/10/Text/20` | 0.793976 | **SOLDIER** |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/10/Text/26` | 0.793976 | **SOLDIER** |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/7/SectionHeader/17` | 0.793976 | **SOLDIER** |

### Query 1
- Text: What is the rule about You're a master of area weapons, heavy armor, and soaking damage. You fight in the thick of the  battle and unleash devastating salvos against your foes as you take withering fire in return. By laying  down a barrage of suppressing fire with powerful weapons, you set your allies up to fulfill their  respective roles while encouraging enemies to focus on you.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/Text/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/1/Text/2', 'PZO22001 Starfinder Player Core 150-161::/page/1/Text/13', 'PZO22001 Starfinder Player Core 150-161::/page/2/Text/9']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/Text/2', 'PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/1', 'PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/6']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/1` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/6` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/2` | 0.916755 | You're a master of area weapons, heavy armor, and soaking damage. You fight in the thick of the  battle and unleash devastating salvos against your foes as you take withering fire in return. By laying |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/13` | 0.759570 | You set yourself up on the battlefield to rain down fire with heavy weapons. You  defy damage and keep your comrades safe from foes as they target you. |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/2/Text/9` | 0.716594 | You have a knack for using powerful weapons to harry your  foes and hinder their movement, preventing them from  operating at their peak. If you make an attack with a weapon  that has the area trait ( |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/2/Text/19` | 0.650981 | Your armor feels like a part of you and stands up to heavy fire  in the thick of battle. Your armor absorbs greater damage from  attacks made by enemies you've suppressed. In a fight, you  likely body |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/1/ListItem/21` | 0.632608 | Use your heavy weapons to demand enemy attention in combat, enjoying the  challenge of battle while soaking attacks for your allies. |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/3` | 0.631956 | There's nothing like a big gun (or maybe several) to get you  through tough times. You've come to terms with the fact that  a stray bullet from one of your barrages might sometimes hit  an ally, but y |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/2/Text/16` | 0.619422 | You believe that anything can be solved by shooting your way  out. Somehow, your bravado and over-the-top actions have  a way of working out for you, despite logic often suggesting  otherwise. To you, |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/8/Text/3` | 0.606734 | You lay down heavy fire with big guns while body  blocking for your allies. |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/5/Text/27` | 0.602296 | You focus your weapons fire on a resilient target in order  to suppress them with the sheer ferocity of your assault.  The required target must succeed at a Will save against  your class DC or become |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/32` | 0.597988 | You compel enemies to avoid your attacks by aiming at their  legs, wings, or other forms of movement to make them easier  to outmaneuver. When you suppress a target with one of your  attacks, it also |

### Query 2
- Text: Summarize **KEY ATTRIBUTE**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/6', 'PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/1', 'PZO22001 Starfinder Player Core 150-161::/page/8/SectionHeader/4']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/6', 'PZO22001 Starfinder Player Core 150-161::/page/1/Text/2', 'PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/7']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/1/Text/2` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/7` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/6` | 0.948607 | **KEY ATTRIBUTE** |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/1` | 0.665018 | **KEY TERMS** |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/8/SectionHeader/4` | 0.599101 | **Attributes** |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/8/SectionHeader/10` | 0.471900 | **Feats** |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/69` | 0.437617 | **BACKGROUNDS** |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/5/Text/66` | 0.437617 | **BACKGROUNDS** |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/58` | 0.437617 | **BACKGROUNDS** |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/7/Text/46` | 0.437617 | **BACKGROUNDS** |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/55` | 0.407698 | **INDEX** |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/8/SectionHeader/6` | 0.398872 | **Skills** |

### Query 3
- Text: Summarize **Constitution**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/7', 'PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/10', 'PZO22001 Starfinder Player Core 150-161::/page/1/Text/8']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/7', 'PZO22001 Starfinder Player Core 150-161::/page/1/Text/8', 'PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/6']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/1/Text/8` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/6` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/7` | 0.919836 | **Constitution** |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/10` | 0.636500 | **10 + Constitution modifier** |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/8` | 0.501186 | At 1st level, your class gives you  an attribute boost to Constitution. |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/8/Text/5` | 0.407505 | Prioritize Constitution, followed by Dexterity for  wielding your zero cannon and Wisdom for your  Perception and Will saves. |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/32` | 0.404615 | **INTRODUCTION** |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/11/Text/26` | 0.404615 | **INTRODUCTION** |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/60` | 0.393607 | **DEFENSES** |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/5/Text/66` | 0.391077 | **BACKGROUNDS** |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/58` | 0.391077 | **BACKGROUNDS** |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/69` | 0.391077 | **BACKGROUNDS** |

### Query 4
- Text: Summarize At 1st level, your class gives you  an attribute boost to Constitution.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/Text/8']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/1/Text/8', 'PZO22001 Starfinder Player Core 150-161::/page/2/Text/4', 'PZO22001 Starfinder Player Core 150-161::/page/1/Text/30']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/Text/8', 'PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/7', 'PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/9']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/7` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/9` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/8` | 1.033243 | At 1st level, your class gives you  an attribute boost to Constitution. |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/2/Text/4` | 0.721790 | In addition to what you get from your class at 1st level, you  have four free boosts to different attribute modifiers. |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/30` | 0.662691 | In addition to what you get from your class at 1st level, you have the benefits of  your selected ancestry and background, as described in Chapter 2. |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/2/Text/7` | 0.586845 | At 1st level, you gain a number of proficiencies that represent  your basic training. These proficiencies are noted at the start  of this class. |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/2/Text/5` | 0.561105 | At 5th level and every 5 levels thereafter, you get four free  boosts to different attribute modifiers. If an attribute modifier  is already +4 or higher, it takes two boosts to increase it; you  get |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/28` | 0.553531 | You gain these abilities as a soldier. Abilities gained at higher levels list the level at  which you gain them next to the features' names. |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/20` | 0.547082 | At 1st level and every even-numbered level, you gain a soldier  class feat. These begin on page 155. |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/11` | 0.522737 | You increase your maximum number  of HP by this number at 1st level and  every level thereafter. |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/2/Table/2` | 0.511076 | Your LevelClass Features1Ancestry and background, attribute boosts, initial proficiencies, suppressing fire, primary target, soldier fighting style, walking armory, soldier feat2Skill feat, soldier fe |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/18` | 0.488672 | In addition, increase the amount of Bulk you can carry  before becoming encumbered by half your Constitution  modifier rounded up. Increase your maximum carried Bulk by  your Constitution modifier. |

### Query 5
- Text: What is the rule about **HIT POINTS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/9', 'PZO22001 Starfinder Player Core 150-161::/page/9/Text/26', 'PZO22001 Starfinder Player Core 150-161::/page/6/Text/24']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/9', 'PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/10', 'PZO22001 Starfinder Player Core 150-161::/page/1/Text/8']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/10` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/1/Text/8` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/9` | 0.884304 | **HIT POINTS** |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/26` | 0.541036 | **Trigger** You are reduced to 0 Hit Points and would fall  unconscious. |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/6/Text/24` | 0.508229 | **Trigger** You reduce your primary target to 0 Hit Points using  Auto-Fire. |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/6/Text/11` | 0.412590 | You bounce back stronger after a hit, ready to continue the  fight. You gain 1d8+4 temporary Hit Points that last for 1  minute. Increase this amount by 1d8+4 at 6th level and  every 4 levels thereaft |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/7/Text/26` | 0.403655 | **Critical Success** Your taunts sting hard. Until the start of  your next turn, any hostile actions that the creature  takes must include you as a target or include you in the  area; otherwise, the c |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/7/Text/27` | 0.363838 | **Success** As critical success, but only the first hostile action  that the creature takes is affected. |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/6/Text/39` | 0.360464 | **Failure** The target is pushed back 10 feet. If using an area  (burst) weapon, the target is pushed away from the  burst's center point. |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/5/Text/66` | 0.354981 | **BACKGROUNDS** |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/58` | 0.354981 | **BACKGROUNDS** |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/7/Text/46` | 0.354981 | **BACKGROUNDS** |

### Query 6
- Text: What is the rule about **10 + Constitution modifier**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/10', 'PZO22001 Starfinder Player Core 150-161::/page/3/Text/18', 'PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/7']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/10', 'PZO22001 Starfinder Player Core 150-161::/page/1/Text/11', 'PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/9']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/1/Text/11` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/9` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/10` | 0.865167 | **10 + Constitution modifier** |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/18` | 0.571821 | In addition, increase the amount of Bulk you can carry  before becoming encumbered by half your Constitution  modifier rounded up. Increase your maximum carried Bulk by  your Constitution modifier. |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/7` | 0.505751 | **Constitution** |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/4` | 0.460295 | When you attack with an area weapon, you can select a  number of allies within the area equal to half your Constitution  modifier. The selected allies are unaffected by the attack. In  addition, enemi |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/26` | 0.459873 | Your sheer bulk terrifies foes, clearing a path for you on the  battlefield. You can use your Constitution modifier instead of  your Charisma modifier on Intimidation checks to Coerce or  Demoralize a |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/17` | 0.458028 | Your endurance training empowers you to carry a load of heavy  equipment. When determining your Strength for using armor,  you can instead choose to use your Constitution modifier. If  you already mee |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/407` | 0.448999 | 10 |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/632` | 0.448999 | 10 |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/560` | 0.448999 | 10 |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/556` | 0.448999 | 10 |

### Query 7
- Text: Summarize You increase your maximum number  of HP by this number at 1st level and  every level thereafter.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/Text/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/1/Text/11', 'PZO22001 Starfinder Player Core 150-161::/page/3/Text/35', 'PZO22001 Starfinder Player Core 150-161::/page/2/Text/5']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/Text/11', 'PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/12', 'PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/10']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/12` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/10` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/11` | 1.031874 | You increase your maximum number  of HP by this number at 1st level and  every level thereafter. |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/35` | 0.637439 | At 3rd level and every 2 levels thereafter, you gain a skill  increase. You can use this increase either to increase your  proficiency rank to trained in one skill you're untrained in, or  to increase |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/2/Text/5` | 0.604495 | At 5th level and every 5 levels thereafter, you get four free  boosts to different attribute modifiers. If an attribute modifier  is already +4 or higher, it takes two boosts to increase it; you  get |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/36` | 0.543409 | At 7th level, you can use skill increases to increase your  proficiency rank to master in a skill in which you're already  an expert, and at 15th level, you can use them to increase your  proficiency |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/6/Text/11` | 0.536162 | You bounce back stronger after a hit, ready to continue the  fight. You gain 1d8+4 temporary Hit Points that last for 1  minute. Increase this amount by 1d8+4 at 6th level and  every 4 levels thereaft |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/28` | 0.535553 | You gain these abilities as a soldier. Abilities gained at higher levels list the level at  which you gain them next to the features' names. |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/29` | 0.526529 | At 3rd level and every 4 levels thereafter, you gain a general  feat. General feats are listed in Chapter 5. |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/2/Text/4` | 0.520901 | In addition to what you get from your class at 1st level, you  have four free boosts to different attribute modifiers. |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/51` | 0.514252 | At 1st level, you gain the listed  proficiency ranks in the following  statistics. You are untrained in anything  not listed unless you gain a better  proficiency rank in some other way. |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/20` | 0.514193 | At 1st level and every even-numbered level, you gain a soldier  class feat. These begin on page 155. |

### Query 8
- Text: Summarize DURING COMBAT ENCOUNTERS...
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/12']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/12', 'PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/14', 'PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/16']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/12', 'PZO22001 Starfinder Player Core 150-161::/page/1/Text/13', 'PZO22001 Starfinder Player Core 150-161::/page/1/Text/11']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/1/Text/13` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/1/Text/11` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/12` | 0.983036 | DURING COMBAT ENCOUNTERS... |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/14` | 0.745777 | DURING SOCIAL ENCOUNTERS... |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/16` | 0.434305 | WHILE EXPLORING... |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/8/SectionHeader/8` | 0.357989 | **Fighting Style** |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/13` | 0.357182 | You set yourself up on the battlefield to rain down fire with heavy weapons. You  defy damage and keep your comrades safe from foes as they target you. |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/18` | 0.337787 | IN DOWNTIME... |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/39` | 0.333292 | **Soldier** |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/58` | 0.333292 | **Soldier** |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/11/Text/32` | 0.333292 | **Soldier** |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/2/SectionHeader/13` | 0.328708 | SOLDIER FIGHTING STYLE |

### Query 9
- Text: What is the rule about You set yourself up on the battlefield to rain down fire with heavy weapons. You  defy damage and keep your comrades safe from foes as they target you.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/Text/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/1/Text/13', 'PZO22001 Starfinder Player Core 150-161::/page/1/Text/2', 'PZO22001 Starfinder Player Core 150-161::/page/8/Text/3']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/Text/13', 'PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/14', 'PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/12']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/14` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/12` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/13` | 0.916638 | You set yourself up on the battlefield to rain down fire with heavy weapons. You  defy damage and keep your comrades safe from foes as they target you. |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/2` | 0.673591 | You're a master of area weapons, heavy armor, and soaking damage. You fight in the thick of the  battle and unleash devastating salvos against your foes as you take withering fire in return. By laying |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/8/Text/3` | 0.645345 | You lay down heavy fire with big guns while body  blocking for your allies. |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/3` | 0.571125 | There's nothing like a big gun (or maybe several) to get you  through tough times. You've come to terms with the fact that  a stray bullet from one of your barrages might sometimes hit  an ally, but y |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/2/Text/19` | 0.562976 | Your armor feels like a part of you and stands up to heavy fire  in the thick of battle. Your armor absorbs greater damage from  attacks made by enemies you've suppressed. In a fight, you  likely body |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/2/Text/9` | 0.550673 | You have a knack for using powerful weapons to harry your  foes and hinder their movement, preventing them from  operating at their peak. If you make an attack with a weapon  that has the area trait ( |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/1/ListItem/21` | 0.543131 | Use your heavy weapons to demand enemy attention in combat, enjoying the  challenge of battle while soaking attacks for your allies. |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/2/Text/16` | 0.524771 | You believe that anything can be solved by shooting your way  out. Somehow, your bravado and over-the-top actions have  a way of working out for you, despite logic often suggesting  otherwise. To you, |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/6` | 0.522919 | While you have the necessary training to employ heavy  weapons, you believe it's important to keep a backup for when  foes get too close. You might be a veteran Veskarium trooper  who knows their way |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/17` | 0.511863 | You're at the front of the group. You position yourself so you can unload a magazine  into any ambush that might pop up while body blocking for your allies. |

### Query 10
- Text: Summarize DURING SOCIAL ENCOUNTERS...
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/14']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/14', 'PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/12', 'PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/16']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/14', 'PZO22001 Starfinder Player Core 150-161::/page/1/Text/13', 'PZO22001 Starfinder Player Core 150-161::/page/1/Text/15']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/1/Text/13` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/1/Text/15` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/14` | 0.977694 | DURING SOCIAL ENCOUNTERS... |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/12` | 0.728104 | DURING COMBAT ENCOUNTERS... |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/16` | 0.408727 | WHILE EXPLORING... |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/18` | 0.315217 | IN DOWNTIME... |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/23` | 0.286287 | OTHERS PROBABLY... |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/20` | 0.285896 | YOU MIGHT... |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/7/Text/32` | 0.282589 | **Envoy** |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/43` | 0.282589 | **Envoy** |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/5/Text/51` | 0.282589 | **Envoy** |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/54` | 0.282589 | **Envoy** |

### Query 11
- Text: What is the rule about You might stand back and let others do the talking, using your menacing presence  to remind others not to mess with your allies. Sometimes you might surprise others  with an insightful take.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/Text/15']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/1/Text/15', 'PZO22001 Starfinder Player Core 150-161::/page/1/ListItem/26', 'PZO22001 Starfinder Player Core 150-161::/page/3/Text/14']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/Text/15', 'PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/14', 'PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/16']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/14` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/16` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/15` | 0.956158 | You might stand back and let others do the talking, using your menacing presence  to remind others not to mess with your allies. Sometimes you might surprise others  with an insightful take. |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/1/ListItem/26` | 0.564681 | Appreciate your menacing presence at the negotiating table. |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/14` | 0.551731 | You unnerve foes with a look, or similarly unsettle them with  subtle mannerisms or veiled threats. One enemy creature of  your choice within 60 feet becomes suppressed until the start  of your next t |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/3` | 0.499378 | There's nothing like a big gun (or maybe several) to get you  through tough times. You've come to terms with the fact that  a stray bullet from one of your barrages might sometimes hit  an ally, but y |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/17` | 0.485961 | You're at the front of the group. You position yourself so you can unload a magazine  into any ambush that might pop up while body blocking for your allies. |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/7/Text/25` | 0.481447 | You taunt your enemy mercilessly, forcing them to  acknowledge you as an immediate threat. Attempt an  Intimidation check and compare it to the Will DC of  one enemy creature within 60 feet. This acti |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/10/Text/10` | 0.480304 | Whether holding up a crumbling ceiling or jumping into  a fireball, you interpose yourself between your ally and  incoming danger. The result of your save becomes one  degree worse, but the result of |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/2/Text/19` | 0.472763 | Your armor feels like a part of you and stands up to heavy fire  in the thick of battle. Your armor absorbs greater damage from  attacks made by enemies you've suppressed. In a fight, you  likely body |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/32` | 0.464523 | You compel enemies to avoid your attacks by aiming at their  legs, wings, or other forms of movement to make them easier  to outmaneuver. When you suppress a target with one of your  attacks, it also |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/6/Text/18` | 0.462883 | You brace yourself as you prepare to defend your allies  behind you. You Area Fire or Auto-Fire. Until the start of  your next turn or until you use a move action, whichever  happens first, you gain t |

### Query 12
- Text: Summarize WHILE EXPLORING...
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/16']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/16', 'PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/14', 'PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/12']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/16', 'PZO22001 Starfinder Player Core 150-161::/page/1/Text/17', 'PZO22001 Starfinder Player Core 150-161::/page/1/Text/15']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/1/Text/17` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/1/Text/15` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/16` | 0.945993 | WHILE EXPLORING... |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/14` | 0.439598 | DURING SOCIAL ENCOUNTERS... |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/12` | 0.437469 | DURING COMBAT ENCOUNTERS... |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/18` | 0.348777 | IN DOWNTIME... |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/52` | 0.333417 | **PLAYING THE ** |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/46` | 0.330508 | **PLAYING THE ** **GAME** |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/64` | 0.330508 | **PLAYING THE ** **GAME** |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/5/Text/61` | 0.330508 | **PLAYING THE ** **GAME** |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/7/Text/41` | 0.330508 | **PLAYING THE ** **GAME** |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/11/Text/37` | 0.330507 | **PLAYING THE ** **GAME** |

### Query 13
- Text: Summarize You're at the front of the group. You position yourself so you can unload a magazine  into any ambush that might pop up while body blocking for your allies.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/Text/17']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/1/Text/17', 'PZO22001 Starfinder Player Core 150-161::/page/8/Text/3', 'PZO22001 Starfinder Player Core 150-161::/page/1/Text/13']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/Text/17', 'PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/18', 'PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/16']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/18` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/16` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/17` | 1.038153 | You're at the front of the group. You position yourself so you can unload a magazine  into any ambush that might pop up while body blocking for your allies. |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/8/Text/3` | 0.675822 | You lay down heavy fire with big guns while body  blocking for your allies. |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/13` | 0.616569 | You set yourself up on the battlefield to rain down fire with heavy weapons. You  defy damage and keep your comrades safe from foes as they target you. |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/32` | 0.573306 | You compel enemies to avoid your attacks by aiming at their  legs, wings, or other forms of movement to make them easier  to outmaneuver. When you suppress a target with one of your  attacks, it also |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/6/Text/18` | 0.569577 | You brace yourself as you prepare to defend your allies  behind you. You Area Fire or Auto-Fire. Until the start of  your next turn or until you use a move action, whichever  happens first, you gain t |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/2/Text/19` | 0.563190 | Your armor feels like a part of you and stands up to heavy fire  in the thick of battle. Your armor absorbs greater damage from  attacks made by enemies you've suppressed. In a fight, you  likely body |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/11/Text/7` | 0.561726 | **Requirements** You're wielding an area or automatic weapon. With a mighty bellow, you unload your weapon to give  your allies the cover they need to rally. You Area Fire  or Auto-Fire without select |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/2` | 0.552217 | You're a master of area weapons, heavy armor, and soaking damage. You fight in the thick of the  battle and unleash devastating salvos against your foes as you take withering fire in return. By laying |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/49` | 0.536676 | **Requirements** You're wielding an area or automatic weapon  with a full magazine. |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/3` | 0.531550 | There's nothing like a big gun (or maybe several) to get you  through tough times. You've come to terms with the fact that  a stray bullet from one of your barrages might sometimes hit  an ally, but y |

### Query 14
- Text: Summarize IN DOWNTIME...
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/18']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/18', 'PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/20', 'PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/14']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/18', 'PZO22001 Starfinder Player Core 150-161::/page/1/Text/19', 'PZO22001 Starfinder Player Core 150-161::/page/1/Text/17']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/1/Text/19` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/1/Text/17` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/18` | 0.786911 | IN DOWNTIME... |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/20` | 0.405939 | YOU MIGHT... |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/14` | 0.367088 | DURING SOCIAL ENCOUNTERS... |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/16` | 0.322232 | WHILE EXPLORING... |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/12` | 0.314851 | DURING COMBAT ENCOUNTERS... |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/23` | 0.302606 | OTHERS PROBABLY... |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/1` | 0.287179 | **KEY TERMS** |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/8/SectionHeader/10` | 0.282115 | **Feats** |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/9/SectionHeader/22` | 0.277477 | **COME GET SOME! **[reaction] **FEAT 10** |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/11/Text/26` | 0.271423 | **INTRODUCTION** |

### Query 15
- Text: Summarize You might join a military, perform physical labor, or take mercenary jobs when  you need credits. You likely spend time training at a gym or tinkering with your  weapons and shopping for new ammunition and upgrades.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/Text/19']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/1/Text/19', 'PZO22001 Starfinder Player Core 150-161::/page/3/Text/9', 'PZO22001 Starfinder Player Core 150-161::/page/4/Text/9']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/Text/19', 'PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/18', 'PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/20']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/18` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/20` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/19` | 1.040482 | You might join a military, perform physical labor, or take mercenary jobs when  you need credits. You likely spend time training at a gym or tinkering with your  weapons and shopping for new ammunitio |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/9` | 0.592710 | You realize that not every situation should be solved with  a gun. You're an intellectual as well as a warrior, solving  problems logically and learning about the galaxy. You keep  your mind sharp wit |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/4/Text/9` | 0.592666 | Your ability to unleash area attacks and utilize your  equipment improves. Your proficiency rank for your soldier |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/4/Text/4` | 0.503690 | Through practical experience, you've learned how to use  your weapons in a way that both pulverizes your foes  and best takes advantage of your area attacks. Your  proficiency ranks for simple weapons |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/28` | 0.502149 | You gain these abilities as a soldier. Abilities gained at higher levels list the level at  which you gain them next to the features' names. |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/2/Text/19` | 0.496215 | Your armor feels like a part of you and stands up to heavy fire  in the thick of battle. Your armor absorbs greater damage from  attacks made by enemies you've suppressed. In a fight, you  likely body |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/2/Text/14` | 0.490746 | As a soldier, you train using a specific style of fighting. Your  style determines how you approach combat and often changes  how you take advantage of your ability to suppress targets.  Choose a sold |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/5/Text/8` | 0.480955 | Through skill and dedication, you've mastered devastating  weapons. Your proficiency rank for your soldier class DC  increases to master. Your proficiency ranks for unarmed  attacks, simple weapons, a |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/4/Text/7` | 0.480204 | You have grown accustomed to wearing armor and  can make the most of its protection. Your proficiency  ranks for light armor, medium armor, heavy armor, and  unarmored defense increase to expert. You |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/5/Text/16` | 0.476220 | At every level that you gain a soldier feat, you can  select one of the following feats. You must satisfy any  prerequisites before selecting the feat. |

### Query 16
- Text: Summarize YOU MIGHT...
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/20']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/20', 'PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/23', 'PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/18']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/20', 'PZO22001 Starfinder Player Core 150-161::/page/1/Text/19', 'PZO22001 Starfinder Player Core 150-161::/page/1/ListItem/21']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/1/Text/19` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/1/ListItem/21` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/20` | 0.903204 | YOU MIGHT... |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/23` | 0.522471 | OTHERS PROBABLY... |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/18` | 0.362798 | IN DOWNTIME... |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/16` | 0.315404 | WHILE EXPLORING... |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/12` | 0.303473 | DURING COMBAT ENCOUNTERS... |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/15` | 0.300271 | You might stand back and let others do the talking, using your menacing presence  to remind others not to mess with your allies. Sometimes you might surprise others  with an insightful take. |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/10` | 0.287086 | **10 + Constitution modifier** |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/16` | 0.286931 | **YOU'LL HAVE TO GO THROUGH ME! **[two-actions] **FEAT 2** |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/6/Text/10` | 0.284588 | **Trigger** You take damage. |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/1` | 0.278501 | **KEY TERMS** |

### Query 17
- Text: What is the rule about Use your heavy weapons to demand enemy attention in combat, enjoying the  challenge of battle while soaking attacks for your allies.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/ListItem/21']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/1/ListItem/21', 'PZO22001 Starfinder Player Core 150-161::/page/1/Text/13', 'PZO22001 Starfinder Player Core 150-161::/page/1/Text/2']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/ListItem/21', 'PZO22001 Starfinder Player Core 150-161::/page/1/ListItem/22', 'PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/20']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/1/ListItem/22` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/20` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/1/ListItem/21` | 0.914335 | Use your heavy weapons to demand enemy attention in combat, enjoying the  challenge of battle while soaking attacks for your allies. |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/13` | 0.618947 | You set yourself up on the battlefield to rain down fire with heavy weapons. You  defy damage and keep your comrades safe from foes as they target you. |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/2` | 0.604017 | You're a master of area weapons, heavy armor, and soaking damage. You fight in the thick of the  battle and unleash devastating salvos against your foes as you take withering fire in return. By laying |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/8/Text/3` | 0.518012 | You lay down heavy fire with big guns while body  blocking for your allies. |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/6` | 0.515328 | While you have the necessary training to employ heavy  weapons, you believe it's important to keep a backup for when  foes get too close. You might be a veteran Veskarium trooper  who knows their way |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/3` | 0.509825 | There's nothing like a big gun (or maybe several) to get you  through tough times. You've come to terms with the fact that  a stray bullet from one of your barrages might sometimes hit  an ally, but y |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/2/Text/9` | 0.499723 | You have a knack for using powerful weapons to harry your  foes and hinder their movement, preventing them from  operating at their peak. If you make an attack with a weapon  that has the area trait ( |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/15` | 0.486567 | You might stand back and let others do the talking, using your menacing presence  to remind others not to mess with your allies. Sometimes you might surprise others  with an insightful take. |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/2/Text/19` | 0.478709 | Your armor feels like a part of you and stands up to heavy fire  in the thick of battle. Your armor absorbs greater damage from  attacks made by enemies you've suppressed. In a fight, you  likely body |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/4/Text/4` | 0.470278 | Through practical experience, you've learned how to use  your weapons in a way that both pulverizes your foes  and best takes advantage of your area attacks. Your  proficiency ranks for simple weapons |

### Query 18
- Text: Summarize Rush forward, knowing that your bulk and endurance will see you through.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/ListItem/22']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/1/ListItem/22', 'PZO22001 Starfinder Player Core 150-161::/page/3/Text/17', 'PZO22001 Starfinder Player Core 150-161::/page/3/Text/26']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/ListItem/22', 'PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/23', 'PZO22001 Starfinder Player Core 150-161::/page/1/ListItem/21']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/23` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/1/ListItem/21` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/1/ListItem/22` | 1.021421 | Rush forward, knowing that your bulk and endurance will see you through. |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/17` | 0.467127 | Your endurance training empowers you to carry a load of heavy  equipment. When determining your Strength for using armor,  you can instead choose to use your Constitution modifier. If  you already mee |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/26` | 0.465912 | Your sheer bulk terrifies foes, clearing a path for you on the  battlefield. You can use your Constitution modifier instead of  your Charisma modifier on Intimidation checks to Coerce or  Demoralize a |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/18` | 0.401967 | In addition, increase the amount of Bulk you can carry  before becoming encumbered by half your Constitution  modifier rounded up. Increase your maximum carried Bulk by  your Constitution modifier. |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/2/Text/16` | 0.387538 | You believe that anything can be solved by shooting your way  out. Somehow, your bravado and over-the-top actions have  a way of working out for you, despite logic often suggesting  otherwise. To you, |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/2/Text/19` | 0.386010 | Your armor feels like a part of you and stands up to heavy fire  in the thick of battle. Your armor absorbs greater damage from  attacks made by enemies you've suppressed. In a fight, you  likely body |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/5/Text/22` | 0.379370 | You draw on your inner reserves and rally yourself to try  again. Reroll the triggering check, but you must use the  new result, even if it's worse. |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/17` | 0.368313 | You're at the front of the group. You position yourself so you can unload a magazine  into any ambush that might pop up while body blocking for your allies. |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/649` | 0.357969 | You'll Have To Go Through Me! |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/15` | 0.356036 | You might stand back and let others do the talking, using your menacing presence  to remind others not to mess with your allies. Sometimes you might surprise others  with an insightful take. |

### Query 19
- Text: Summarize OTHERS PROBABLY...
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/23']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/23', 'PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/20', 'PZO22001 Starfinder Player Core 150-161::/page/1/Text/15']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/23', 'PZO22001 Starfinder Player Core 150-161::/page/1/ListItem/22', 'PZO22001 Starfinder Player Core 150-161::/page/1/ListItem/24']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/1/ListItem/22` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/1/ListItem/24` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/23` | 0.892334 | OTHERS PROBABLY... |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/20` | 0.536970 | YOU MIGHT... |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/15` | 0.360494 | You might stand back and let others do the talking, using your menacing presence  to remind others not to mess with your allies. Sometimes you might surprise others  with an insightful take. |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/16` | 0.318763 | WHILE EXPLORING... |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/33` | 0.304825 | **ANCESTRIES & ** **BACKGROUNDS** |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/14` | 0.292939 | DURING SOCIAL ENCOUNTERS... |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/12` | 0.274839 | DURING COMBAT ENCOUNTERS... |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/52` | 0.260114 | **INTRODUCTION** **ANCESTRIES & ** |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/41` | 0.260114 | **INTRODUCTION** **ANCESTRIES & ** |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/5/Text/49` | 0.260114 | **INTRODUCTION** **ANCESTRIES & ** |

### Query 20
- Text: Summarize Rely on you to lead the charge and take incoming fire.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/ListItem/24']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/1/ListItem/24', 'PZO22001 Starfinder Player Core 150-161::/page/1/Text/2', 'PZO22001 Starfinder Player Core 150-161::/page/1/Text/13']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/ListItem/24', 'PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/23', 'PZO22001 Starfinder Player Core 150-161::/page/1/ListItem/25']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/23` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/1/ListItem/25` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/1/ListItem/24` | 1.014483 | Rely on you to lead the charge and take incoming fire. |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/2` | 0.554430 | You're a master of area weapons, heavy armor, and soaking damage. You fight in the thick of the  battle and unleash devastating salvos against your foes as you take withering fire in return. By laying |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/13` | 0.552370 | You set yourself up on the battlefield to rain down fire with heavy weapons. You  defy damage and keep your comrades safe from foes as they target you. |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/7/Text/13` | 0.509497 | **Requirements** You're wielding an area or automatic weapon. The flash and smoke from your frenzied gunfire conceals  you from any enemies who might be left standing in the  aftermath. You Area Fire |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/11/Text/7` | 0.502836 | **Requirements** You're wielding an area or automatic weapon. With a mighty bellow, you unload your weapon to give  your allies the cover they need to rally. You Area Fire  or Auto-Fire without select |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/10/Text/22` | 0.471901 | **Requirements** Your last action this turn was an Area Fire  or Auto-Fire. |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/575` | 0.459005 | Covering Fire |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/2/Text/19` | 0.455321 | Your armor feels like a part of you and stands up to heavy fire  in the thick of battle. Your armor absorbs greater damage from  attacks made by enemies you've suppressed. In a fight, you  likely body |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/7/SectionHeader/5` | 0.444951 | **COVERING FIRE **[one-action]** OR **[two-actions] **FEAT 6** |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/6/Text/33` | 0.444866 | **Requirements** Your last action this turn was an Area Fire  attack. |

### Query 21
- Text: Summarize Assume there's not much of a personality or intellect under all that armor.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/ListItem/25']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/1/ListItem/25', 'PZO22001 Starfinder Player Core 150-161::/page/4/Text/7', 'PZO22001 Starfinder Player Core 150-161::/page/3/Text/9']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/ListItem/25', 'PZO22001 Starfinder Player Core 150-161::/page/1/ListItem/24', 'PZO22001 Starfinder Player Core 150-161::/page/1/ListItem/26']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/1/ListItem/24` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/1/ListItem/26` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/1/ListItem/25` | 1.018641 | Assume there's not much of a personality or intellect under all that armor. |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/4/Text/7` | 0.597204 | You have grown accustomed to wearing armor and  can make the most of its protection. Your proficiency  ranks for light armor, medium armor, heavy armor, and  unarmored defense increase to expert. You |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/9` | 0.565480 | You realize that not every situation should be solved with  a gun. You're an intellectual as well as a warrior, solving  problems logically and learning about the galaxy. You keep  your mind sharp wit |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/2/Text/19` | 0.501362 | Your armor feels like a part of you and stands up to heavy fire  in the thick of battle. Your armor absorbs greater damage from  attacks made by enemies you've suppressed. In a fight, you  likely body |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/5/Text/6` | 0.500973 | Your skill with armor further improves. Your proficiency  ranks for light armor, medium armor, heavy armor, and  unarmored defense increase to master. |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/5/Text/12` | 0.500397 | Your skill with armor is unparalleled. Your proficiency  ranks for light armor, medium armor, heavy armor, and  unarmored defense increase to legendary. |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/10` | 0.494878 | Choose either Diplomacy or Society. You become trained in  the chosen skill and one Lore skill of your choice. When you  gain armor expertise, you gain expert proficiency in Diplomacy  or Society (whi |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/61` | 0.465638 | Trained in all armor Trained in unarmored defense |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/402` | 0.448353 | Armor expertise, general feat, skill increase, soldier expertise, tough as nails, weapon specialization |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/17` | 0.437874 | Your endurance training empowers you to carry a load of heavy  equipment. When determining your Strength for using armor,  you can instead choose to use your Constitution modifier. If  you already mee |

### Query 22
- Text: What is the rule about Appreciate your menacing presence at the negotiating table.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/ListItem/26']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/1/ListItem/26', 'PZO22001 Starfinder Player Core 150-161::/page/1/Text/15', 'PZO22001 Starfinder Player Core 150-161::/page/7/Text/26']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/ListItem/26', 'PZO22001 Starfinder Player Core 150-161::/page/1/ListItem/25', 'PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/27']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/1/ListItem/25` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/27` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/1/ListItem/26` | 0.905254 | Appreciate your menacing presence at the negotiating table. |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/15` | 0.563246 | You might stand back and let others do the talking, using your menacing presence  to remind others not to mess with your allies. Sometimes you might surprise others  with an insightful take. |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/7/Text/26` | 0.468678 | **Critical Success** Your taunts sting hard. Until the start of  your next turn, any hostile actions that the creature  takes must include you as a target or include you in the  area; otherwise, the c |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/7/Text/25` | 0.418636 | You taunt your enemy mercilessly, forcing them to  acknowledge you as an immediate threat. Attempt an  Intimidation check and compare it to the Will DC of  one enemy creature within 60 feet. This acti |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/14` | 0.387582 | You unnerve foes with a look, or similarly unsettle them with  subtle mannerisms or veiled threats. One enemy creature of  your choice within 60 feet becomes suppressed until the start  of your next t |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/6/Text/18` | 0.356794 | You brace yourself as you prepare to defend your allies  behind you. You Area Fire or Auto-Fire. Until the start of  your next turn or until you use a move action, whichever  happens first, you gain t |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/4/Text/2` | 0.347767 | You remain alert to threats around you. Your proficiency  rank for Perception increases to expert. |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/2/Text/9` | 0.333323 | You have a knack for using powerful weapons to harry your  foes and hinder their movement, preventing them from  operating at their peak. If you make an attack with a weapon  that has the area trait ( |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/599` | 0.328009 | Menacing Laughter |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/4` | 0.323923 | When you attack with an area weapon, you can select a  number of allies within the area equal to half your Constitution  modifier. The selected allies are unaffected by the attack. In  addition, enemi |

### Query 23
- Text: What is the rule about CLASS FEATURES?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/27']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/27', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/388', 'PZO22001 Starfinder Player Core 150-161::/page/9/Text/53']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/27', 'PZO22001 Starfinder Player Core 150-161::/page/1/Text/28', 'PZO22001 Starfinder Player Core 150-161::/page/1/ListItem/26']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/1/Text/28` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/1/ListItem/26` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/27` | 0.841653 | CLASS FEATURES |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/388` | 0.758361 | Class Features |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/53` | 0.537843 | **CLASSES** |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/7/Text/31` | 0.507843 | **CLASSES** |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/11/Text/27` | 0.507843 | **CLASSES** |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/5/Text/50` | 0.507843 | **CLASSES** |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/34` | 0.507843 | **CLASSES** |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/42` | 0.507843 | **CLASSES** |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/6/Text/2` | 0.486862 | You'll see the following key terms in many soldier  class features. |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/8/SectionHeader/4` | 0.440561 | **Attributes** |

### Query 24
- Text: What is the rule about You gain these abilities as a soldier. Abilities gained at higher levels list the level at  which you gain them next to the features' names.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/Text/28']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/1/Text/28', 'PZO22001 Starfinder Player Core 150-161::/page/3/Text/23', 'PZO22001 Starfinder Player Core 150-161::/page/3/Text/20']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/Text/28', 'PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/29', 'PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/27']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/29` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/27` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/28` | 0.974110 | You gain these abilities as a soldier. Abilities gained at higher levels list the level at  which you gain them next to the features' names. |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/23` | 0.658640 | At 2nd level and every 2 levels thereafter, you gain a skill feat.  Skill feats can be found in Chapter 5 and have the skill trait.  You must be trained or better in the corresponding skill to  select |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/20` | 0.645356 | At 1st level and every even-numbered level, you gain a soldier  class feat. These begin on page 155. |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/2/Table/2` | 0.599107 | Your LevelClass Features1Ancestry and background, attribute boosts, initial proficiencies, suppressing fire, primary target, soldier fighting style, walking armory, soldier feat2Skill feat, soldier fe |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/29` | 0.598796 | At 3rd level and every 4 levels thereafter, you gain a general  feat. General feats are listed in Chapter 5. |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/6/Text/2` | 0.594623 | You'll see the following key terms in many soldier  class features. |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/5/Text/16` | 0.585616 | At every level that you gain a soldier feat, you can  select one of the following feats. You must satisfy any  prerequisites before selecting the feat. |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/4/Text/9` | 0.575718 | Your ability to unleash area attacks and utilize your  equipment improves. Your proficiency rank for your soldier |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/428` | 0.570850 | Attribute boosts, skill feat, soldier feat |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/408` | 0.570850 | Attribute boosts, skill feat, soldier feat |

### Query 25
- Text: What is the rule about ANCESTRY AND BACKGROUND?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/29']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/29', 'PZO22001 Starfinder Player Core 150-161::/page/1/Text/33', 'PZO22001 Starfinder Player Core 150-161::/page/7/Text/30']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/29', 'PZO22001 Starfinder Player Core 150-161::/page/1/Text/28', 'PZO22001 Starfinder Player Core 150-161::/page/1/Text/30']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/1/Text/28` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/1/Text/30` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/29` | 0.928306 | ANCESTRY AND BACKGROUND |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/33` | 0.739658 | **ANCESTRIES & ** **BACKGROUNDS** |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/7/Text/30` | 0.534053 | **INTRODUCTION** **ANCESTRIES & ** |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/5/Text/49` | 0.504053 | **INTRODUCTION** **ANCESTRIES & ** |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/52` | 0.504053 | **INTRODUCTION** **ANCESTRIES & ** |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/41` | 0.504053 | **INTRODUCTION** **ANCESTRIES & ** |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/7/Text/46` | 0.461777 | **BACKGROUNDS** |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/58` | 0.449777 | **BACKGROUNDS** |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/5/Text/66` | 0.449777 | **BACKGROUNDS** |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/69` | 0.449777 | **BACKGROUNDS** |

### Query 26
- Text: What is the rule about In addition to what you get from your class at 1st level, you have the benefits of  your selected ancestry and background, as described in Chapter 2.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/Text/30']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/1/Text/30', 'PZO22001 Starfinder Player Core 150-161::/page/3/Text/39', 'PZO22001 Starfinder Player Core 150-161::/page/1/Text/8']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/Text/30', 'PZO22001 Starfinder Player Core 150-161::/page/1/Text/32', 'PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/29']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/1/Text/32` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/29` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/30` | 0.963223 | In addition to what you get from your class at 1st level, you have the benefits of  your selected ancestry and background, as described in Chapter 2. |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/39` | 0.653098 | In addition to the initial ancestry feat you started with, you  gain an ancestry feat at 5th level and every 4 levels thereafter.  The list of ancestry feats available to you can be found in your  anc |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/8` | 0.622147 | At 1st level, your class gives you  an attribute boost to Constitution. |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/2/Text/7` | 0.556690 | At 1st level, you gain a number of proficiencies that represent  your basic training. These proficiencies are noted at the start  of this class. |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/2/Text/4` | 0.530786 | In addition to what you get from your class at 1st level, you  have four free boosts to different attribute modifiers. |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/51` | 0.494730 | At 1st level, you gain the listed  proficiency ranks in the following  statistics. You are untrained in anything  not listed unless you gain a better  proficiency rank in some other way. |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/28` | 0.480367 | You gain these abilities as a soldier. Abilities gained at higher levels list the level at  which you gain them next to the features' names. |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/23` | 0.476847 | At 2nd level and every 2 levels thereafter, you gain a skill feat.  Skill feats can be found in Chapter 5 and have the skill trait.  You must be trained or better in the corresponding skill to  select |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/406` | 0.460796 | Ancestry feat, skill increase |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/390` | 0.459641 | Ancestry and background, attribute boosts, initial proficiencies, suppressing fire, primary target, soldier fighting style, walking armory, soldier feat |

### Query 27
- Text: Summarize **INTRODUCTION**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/Text/32']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/1/Text/32', 'PZO22001 Starfinder Player Core 150-161::/page/11/Text/26', 'PZO22001 Starfinder Player Core 150-161::/page/3/Text/58']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/Text/32', 'PZO22001 Starfinder Player Core 150-161::/page/1/Text/30', 'PZO22001 Starfinder Player Core 150-161::/page/1/Text/33']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/1/Text/30` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/1/Text/33` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/32` | 0.880541 | **INTRODUCTION** |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/11/Text/26` | 0.880541 | **INTRODUCTION** |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/58` | 0.611679 | **BACKGROUNDS** |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/5/Text/66` | 0.569679 | **BACKGROUNDS** |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/7/Text/46` | 0.569679 | **BACKGROUNDS** |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/69` | 0.569679 | **BACKGROUNDS** |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/55` | 0.524467 | **INDEX** |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/41` | 0.507539 | **INTRODUCTION** **ANCESTRIES & ** |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/7/Text/30` | 0.495539 | **INTRODUCTION** **ANCESTRIES & ** |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/5/Text/49` | 0.495539 | **INTRODUCTION** **ANCESTRIES & ** |

### Query 28
- Text: What is the rule about **ANCESTRIES & ** **BACKGROUNDS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/Text/33']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/1/Text/33', 'PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/29', 'PZO22001 Starfinder Player Core 150-161::/page/9/Text/52']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/Text/33', 'PZO22001 Starfinder Player Core 150-161::/page/1/Text/32', 'PZO22001 Starfinder Player Core 150-161::/page/1/Text/34']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/1/Text/32` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/1/Text/34` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/33` | 0.920820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/29` | 0.768682 | ANCESTRY AND BACKGROUND |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/52` | 0.714101 | **INTRODUCTION** **ANCESTRIES & ** |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/5/Text/49` | 0.684101 | **INTRODUCTION** **ANCESTRIES & ** |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/41` | 0.684101 | **INTRODUCTION** **ANCESTRIES & ** |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/7/Text/30` | 0.684101 | **INTRODUCTION** **ANCESTRIES & ** |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/69` | 0.606354 | **BACKGROUNDS** |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/58` | 0.594354 | **BACKGROUNDS** |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/7/Text/46` | 0.594354 | **BACKGROUNDS** |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/5/Text/66` | 0.594354 | **BACKGROUNDS** |

### Query 29
- Text: Summarize **CLASSES**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/Text/34']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/1/Text/34', 'PZO22001 Starfinder Player Core 150-161::/page/5/Text/50', 'PZO22001 Starfinder Player Core 150-161::/page/3/Text/42']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/Text/34', 'PZO22001 Starfinder Player Core 150-161::/page/9/Text/53', 'PZO22001 Starfinder Player Core 150-161::/page/11/Text/27', 'PZO22001 Starfinder Player Core 150-161::/page/7/Text/31', 'PZO22001 Starfinder Player Core 150-161::/page/5/Text/50', 'PZO22001 Starfinder Player Core 150-161::/page/3/Text/42', 'PZO22001 Starfinder Player Core 150-161::/page/1/Text/35', 'PZO22001 Starfinder Player Core 150-161::/page/1/Text/33']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/9/Text/53` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/11/Text/27` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/7/Text/31` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/5/Text/50` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/3/Text/42` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/1/Text/35` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/1/Text/33` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/34` | 0.940061 | **CLASSES** |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/5/Text/50` | 0.940061 | **CLASSES** |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/42` | 0.940061 | **CLASSES** |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/7/Text/31` | 0.910061 | **CLASSES** |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/11/Text/27` | 0.910061 | **CLASSES** |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/53` | 0.910061 | **CLASSES** |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/27` | 0.573477 | CLASS FEATURES |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/62` | 0.515930 | **CLASS DC** |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/388` | 0.498036 | Class Features |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/8/SectionHeader/6` | 0.476046 | **Skills** |

### Query 30
- Text: Summarize **Envoy**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/Text/35']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/7/Text/32', 'PZO22001 Starfinder Player Core 150-161::/page/1/Text/35', 'PZO22001 Starfinder Player Core 150-161::/page/3/Text/43']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/Text/35', 'PZO22001 Starfinder Player Core 150-161::/page/1/Text/36', 'PZO22001 Starfinder Player Core 150-161::/page/1/Text/34']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/1/Text/36` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/1/Text/34` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/7/Text/32` | 0.951326 | **Envoy** |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/35` | 0.951326 | **Envoy** |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/43` | 0.951326 | **Envoy** |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/54` | 0.909326 | **Envoy** |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/5/Text/51` | 0.909326 | **Envoy** |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/11/Text/28` | 0.909326 | **Envoy** |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/55` | 0.382028 | **INDEX** |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/39` | 0.364330 | **Soldier** |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/11/Text/32` | 0.364330 | **Soldier** |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/58` | 0.364330 | **Soldier** |

### Query 31
- Text: Summarize **Mystic**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/Text/36']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/11/Text/29', 'PZO22001 Starfinder Player Core 150-161::/page/1/Text/36', 'PZO22001 Starfinder Player Core 150-161::/page/9/Text/55']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/Text/36', 'PZO22001 Starfinder Player Core 150-161::/page/1/Text/37', 'PZO22001 Starfinder Player Core 150-161::/page/1/Text/35']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/1/Text/37` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/1/Text/35` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/11/Text/29` | 0.959379 | **Mystic** |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/36` | 0.959378 | **Mystic** |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/55` | 0.959378 | **Mystic** |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/7/Text/33` | 0.917378 | **Mystic** |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/5/Text/52` | 0.917378 | **Mystic** |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/44` | 0.917378 | **Mystic** |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/1` | 0.339324 | **KEY TERMS** |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/8/SectionHeader/10` | 0.326924 | **Feats** |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/55` | 0.321087 | **INDEX** |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/37` | 0.319269 | **Operative ** |

### Query 32
- Text: Summarize **Operative **
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/Text/37']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/1/Text/37', 'PZO22001 Starfinder Player Core 150-161::/page/11/Text/30', 'PZO22001 Starfinder Player Core 150-161::/page/5/Text/53']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/Text/37', 'PZO22001 Starfinder Player Core 150-161::/page/1/Text/36', 'PZO22001 Starfinder Player Core 150-161::/page/1/Text/38']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/1/Text/36` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/1/Text/38` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/37` | 0.958402 | **Operative ** |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/5/Text/53` | 0.958402 | **Operative ** |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/11/Text/30` | 0.958402 | **Operative ** |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/7/Text/34` | 0.916402 | **Operative ** |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/45` | 0.916402 | **Operative ** |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/56` | 0.916402 | **Operative ** |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/3/SectionHeader/11` | 0.466965 | **OPPRESSIVE PRESENCE **[one-action] |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/8/SectionHeader/13` | 0.413555 | **OFFENSIVE DEFENSE **[two-actions] **FEAT 6** |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/1` | 0.361666 | **KEY TERMS** |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/58` | 0.345470 | **Soldier** |

### Query 33
- Text: Summarize **Solarian**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/Text/38']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/1/Text/38', 'PZO22001 Starfinder Player Core 150-161::/page/11/Text/31', 'PZO22001 Starfinder Player Core 150-161::/page/9/Text/57']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/Text/38', 'PZO22001 Starfinder Player Core 150-161::/page/1/Text/37', 'PZO22001 Starfinder Player Core 150-161::/page/1/Text/39']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/1/Text/37` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/1/Text/39` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/38` | 0.974700 | **Solarian** |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/11/Text/31` | 0.974700 | **Solarian** |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/57` | 0.974700 | **Solarian** |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/46` | 0.787602 | **Solarian** **Soldier** |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/5/Text/54` | 0.787602 | **Solarian** **Soldier** |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/7/Text/35` | 0.787602 | **Solarian** **Soldier** |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/58` | 0.471086 | **Soldier** |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/11/Text/32` | 0.471086 | **Soldier** |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/39` | 0.471086 | **Soldier** |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/10/Text/36` | 0.444504 | **SOLDIER** |

### Query 34
- Text: Summarize **Soldier**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/Text/39']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/1/Text/39', 'PZO22001 Starfinder Player Core 150-161::/page/9/Text/58', 'PZO22001 Starfinder Player Core 150-161::/page/11/Text/32']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/Text/39', 'PZO22001 Starfinder Player Core 150-161::/page/1/Text/38', 'PZO22001 Starfinder Player Core 150-161::/page/1/Text/40']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/1/Text/38` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/1/Text/40` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/39` | 0.953061 | **Soldier** |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/58` | 0.953061 | **Soldier** |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/11/Text/32` | 0.953061 | **Soldier** |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/10/Text/30` | 0.825859 | **SOLDIER** |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/10/Text/53` | 0.825859 | **SOLDIER** |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/10/Text/36` | 0.825859 | **SOLDIER** |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/10/Text/40` | 0.825859 | **SOLDIER** |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/11/Text/19` | 0.825859 | **SOLDIER** |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/10/Text/26` | 0.825859 | **SOLDIER** |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/10/Text/20` | 0.825859 | **SOLDIER** |

### Query 35
- Text: Summarize **Witchwarper**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/Text/40']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/1/Text/40', 'PZO22001 Starfinder Player Core 150-161::/page/5/Text/55', 'PZO22001 Starfinder Player Core 150-161::/page/9/Text/59']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/Text/40', 'PZO22001 Starfinder Player Core 150-161::/page/1/Text/41', 'PZO22001 Starfinder Player Core 150-161::/page/1/Text/39']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/1/Text/41` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/1/Text/39` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/40` | 0.988715 | **Witchwarper** |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/5/Text/55` | 0.988715 | **Witchwarper** |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/59` | 0.988715 | **Witchwarper** |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/47` | 0.946715 | **Witchwarper** |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/7/Text/36` | 0.946715 | **Witchwarper** |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/11/Text/33` | 0.808939 | **Witchwarper** **Archetypes** |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/38` | 0.352191 | **VECTOR REFLECTOR **[reaction] **FEAT 14** |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/8/SectionHeader/6` | 0.345863 | **Skills** |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/58` | 0.342425 | **Soldier** |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/39` | 0.342425 | **Soldier** |

### Query 36
- Text: Summarize **Archetypes**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/Text/41']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/1/Text/41', 'PZO22001 Starfinder Player Core 150-161::/page/3/Text/48', 'PZO22001 Starfinder Player Core 150-161::/page/5/Text/56']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/Text/41', 'PZO22001 Starfinder Player Core 150-161::/page/1/Text/42', 'PZO22001 Starfinder Player Core 150-161::/page/1/Text/40']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/1/Text/42` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/1/Text/40` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/41` | 0.973323 | **Archetypes** |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/48` | 0.973323 | **Archetypes** |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/5/Text/56` | 0.973323 | **Archetypes** |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/7/Text/37` | 0.931323 | **Archetypes** |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/60` | 0.748593 | **Archetypes** **SKILLS** |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/11/Text/33` | 0.668054 | **Witchwarper** **Archetypes** |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/8/SectionHeader/4` | 0.431887 | **Attributes** |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/55` | 0.382400 | **INDEX** |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/8/SectionHeader/6` | 0.378068 | **Skills** |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/33` | 0.376744 | **ANCESTRIES & ** **BACKGROUNDS** |

### Query 37
- Text: What is the rule about **SKILLS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/Text/42']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/56', 'PZO22001 Starfinder Player Core 150-161::/page/1/Text/42', 'PZO22001 Starfinder Player Core 150-161::/page/9/Text/60']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/Text/42', 'PZO22001 Starfinder Player Core 150-161::/page/1/Text/43', 'PZO22001 Starfinder Player Core 150-161::/page/1/Text/41']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/1/Text/43` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/1/Text/41` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/56` | 0.864442 | **SKILLS** |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/42` | 0.864442 | **SKILLS** |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/60` | 0.719288 | **Archetypes** **SKILLS** |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/7/Text/38` | 0.651094 | **SKILLS** **FEATS** |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/49` | 0.651094 | **SKILLS** **FEATS** |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/5/Text/57` | 0.651094 | **SKILLS** **FEATS** |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/8/SectionHeader/6` | 0.640740 | **Skills** |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/23` | 0.458870 | At 2nd level and every 2 levels thereafter, you gain a skill feat.  Skill feats can be found in Chapter 5 and have the skill trait.  You must be trained or better in the corresponding skill to  select |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/35` | 0.422118 | At 3rd level and every 2 levels thereafter, you gain a skill  increase. You can use this increase either to increase your  proficiency rank to trained in one skill you're untrained in, or  to increase |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/51` | 0.421224 | At 1st level, you gain the listed  proficiency ranks in the following  statistics. You are untrained in anything  not listed unless you gain a better  proficiency rank in some other way. |

### Query 38
- Text: What is the rule about **FEATS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/Text/43']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/9/Text/61', 'PZO22001 Starfinder Player Core 150-161::/page/11/Text/34', 'PZO22001 Starfinder Player Core 150-161::/page/1/Text/43']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/Text/43', 'PZO22001 Starfinder Player Core 150-161::/page/1/Text/42', 'PZO22001 Starfinder Player Core 150-161::/page/1/Text/44']
- Expanded expected found: `True`
- Expanded expected rank: `3`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/1/Text/42` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/1/Text/44` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/61` | 0.871817 | **FEATS** |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/11/Text/34` | 0.871817 | **FEATS** |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/43` | 0.871817 | **FEATS** |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/49` | 0.653037 | **SKILLS** **FEATS** |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/5/Text/57` | 0.653037 | **SKILLS** **FEATS** |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/7/Text/38` | 0.653037 | **SKILLS** **FEATS** |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/551` | 0.619086 | Feat |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/601` | 0.619086 | Feat |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/5/SectionHeader/15` | 0.531806 | SOLDIER FEATS |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/3/SectionHeader/19` | 0.531806 | SOLDIER FEATS |

### Query 39
- Text: Summarize **EQUIPMENT**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/Text/44']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/1/Text/44', 'PZO22001 Starfinder Player Core 150-161::/page/11/Text/35', 'PZO22001 Starfinder Player Core 150-161::/page/7/Text/39']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/Text/44', 'PZO22001 Starfinder Player Core 150-161::/page/1/Text/43', 'PZO22001 Starfinder Player Core 150-161::/page/1/Text/45']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/1/Text/43` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/1/Text/45` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/44` | 0.944726 | **EQUIPMENT** |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/11/Text/35` | 0.944726 | **EQUIPMENT** |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/7/Text/39` | 0.944726 | **EQUIPMENT** |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/5/Text/59` | 0.902726 | **EQUIPMENT** |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/62` | 0.902726 | **EQUIPMENT** |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/51` | 0.578761 | **EQUIPMENT** **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/55` | 0.421643 | **INDEX** |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/69` | 0.409329 | **BACKGROUNDS** |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/5/Text/66` | 0.409329 | **BACKGROUNDS** |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/7/Text/46` | 0.409329 | **BACKGROUNDS** |

### Query 40
- Text: What is the rule about **SPELLS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/Text/45']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/1/Text/45', 'PZO22001 Starfinder Player Core 150-161::/page/9/Text/63', 'PZO22001 Starfinder Player Core 150-161::/page/11/Text/36']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/Text/45', 'PZO22001 Starfinder Player Core 150-161::/page/1/Text/44', 'PZO22001 Starfinder Player Core 150-161::/page/1/Text/46']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/1/Text/44` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/1/Text/46` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/45` | 0.889304 | **SPELLS** |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/63` | 0.889304 | **SPELLS** |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/11/Text/36` | 0.889304 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/5/Text/60` | 0.847304 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/7/Text/40` | 0.847304 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/51` | 0.759411 | **EQUIPMENT** **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/56` | 0.388254 | **SKILLS** |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/42` | 0.388254 | **SKILLS** |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/50` | 0.335811 | Spinning in place, you fire indiscriminately to completely  clear out the room. You Area Fire (even if using an automatic  weapon), affecting each creature in an emanation around you  with a radius eq |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/49` | 0.332025 | **SKILLS** **FEATS** |

### Query 41
- Text: Summarize **PLAYING THE ** **GAME**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/Text/46']
- Expected found: `True`
- Expected rank: `5`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/11/Text/37', 'PZO22001 Starfinder Player Core 150-161::/page/5/Text/61', 'PZO22001 Starfinder Player Core 150-161::/page/7/Text/41']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/Text/46', 'PZO22001 Starfinder Player Core 150-161::/page/1/Text/45', 'PZO22001 Starfinder Player Core 150-161::/page/1/Text/47']
- Expanded expected found: `True`
- Expanded expected rank: `5`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/1/Text/45` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/1/Text/47` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/11/Text/37` | 0.965001 | **PLAYING THE ** **GAME** |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/5/Text/61` | 0.965000 | **PLAYING THE ** **GAME** |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/7/Text/41` | 0.965000 | **PLAYING THE ** **GAME** |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/64` | 0.923000 | **PLAYING THE ** **GAME** |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/46` | 0.923000 | **PLAYING THE ** **GAME** |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/52` | 0.811006 | **PLAYING THE ** |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/53` | 0.545563 | **GAME** **CONDITIONS ** |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/12` | 0.449573 | **SHOT ON THE RUN **[two-actions] **FEAT 2** |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/32` | 0.418586 | **INTRODUCTION** |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/11/Text/26` | 0.418586 | **INTRODUCTION** |

### Query 42
- Text: Summarize **CONDITIONS ** **APPENDIX**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/Text/47']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/9/Text/65', 'PZO22001 Starfinder Player Core 150-161::/page/5/Text/62', 'PZO22001 Starfinder Player Core 150-161::/page/1/Text/47']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/Text/47', 'PZO22001 Starfinder Player Core 150-161::/page/11/Text/38', 'PZO22001 Starfinder Player Core 150-161::/page/5/Text/62', 'PZO22001 Starfinder Player Core 150-161::/page/1/Text/46', 'PZO22001 Starfinder Player Core 150-161::/page/1/Text/48', 'PZO22001 Starfinder Player Core 150-161::/page/9/Text/65', 'PZO22001 Starfinder Player Core 150-161::/page/7/Text/42']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/11/Text/38` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/5/Text/62` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/1/Text/46` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/1/Text/48` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/9/Text/65` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/7/Text/42` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/65` | 0.983499 | **CONDITIONS ** **APPENDIX** |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/5/Text/62` | 0.983499 | **CONDITIONS ** **APPENDIX** |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/47` | 0.983499 | **CONDITIONS ** **APPENDIX** |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/7/Text/42` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/11/Text/38` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/54` | 0.573689 | **APPENDIX** **GLOSSARY & ** |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/53` | 0.535379 | **GAME** **CONDITIONS ** |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/8/SectionHeader/4` | 0.463693 | **Attributes** |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/1` | 0.439047 | **KEY TERMS** |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/55` | 0.423722 | **INDEX** |

### Query 43
- Text: Summarize **GLOSSARY & ** **INDEX**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/Text/48']
- Expected found: `True`
- Expected rank: `5`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/11/Text/39', 'PZO22001 Starfinder Player Core 150-161::/page/5/Text/63', 'PZO22001 Starfinder Player Core 150-161::/page/7/Text/43']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/Text/48', 'PZO22001 Starfinder Player Core 150-161::/page/1/Text/47', 'PZO22001 Starfinder Player Core 150-161::/page/1/Text/49']
- Expanded expected found: `True`
- Expanded expected rank: `5`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/1/Text/47` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/1/Text/49` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/11/Text/39` | 0.993465 | **GLOSSARY & ** **INDEX** |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/5/Text/63` | 0.993465 | **GLOSSARY & ** **INDEX** |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/7/Text/43` | 0.993465 | **GLOSSARY & ** **INDEX** |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/66` | 0.951465 | **GLOSSARY & ** **INDEX** |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/48` | 0.951465 | **GLOSSARY & ** **INDEX** |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/54` | 0.697531 | **APPENDIX** **GLOSSARY & ** |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/55` | 0.618357 | **INDEX** |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/42` | 0.385404 | **CLASSES** |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/11/Text/27` | 0.385404 | **CLASSES** |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/53` | 0.385404 | **CLASSES** |

### Query 44
- Text: What is the rule about **CHARACTER ** **SHEET**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/Text/49']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/1/Text/49', 'PZO22001 Starfinder Player Core 150-161::/page/3/Text/53', 'PZO22001 Starfinder Player Core 150-161::/page/9/Text/60']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/Text/49', 'PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/50', 'PZO22001 Starfinder Player Core 150-161::/page/1/Text/48']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/50` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/1/Text/48` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/49` | 0.859300 | **CHARACTER ** **SHEET** |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/53` | 0.456237 | **GAME** **CONDITIONS ** |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/60` | 0.448576 | **Archetypes** **SKILLS** |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/48` | 0.392353 | **Archetypes** |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/41` | 0.392353 | **Archetypes** |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/5/Text/56` | 0.392353 | **Archetypes** |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/7/Text/37` | 0.392353 | **Archetypes** |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/6` | 0.378450 | **RUN HOT **[three-actions] **FEAT 8** |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/8/SectionHeader/6` | 0.371280 | **Skills** |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/12` | 0.370023 | **SHOT ON THE RUN **[two-actions] **FEAT 2** |

### Query 45
- Text: Summarize **INITIAL PROFICIENCIES**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/50']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/50', 'PZO22001 Starfinder Player Core 150-161::/page/2/SectionHeader/6', 'PZO22001 Starfinder Player Core 150-161::/page/2/Text/7']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/50', 'PZO22001 Starfinder Player Core 150-161::/page/1/Text/49', 'PZO22001 Starfinder Player Core 150-161::/page/1/Text/51']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/1/Text/49` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/1/Text/51` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/50` | 1.001056 | **INITIAL PROFICIENCIES** |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/2/SectionHeader/6` | 0.851001 | INITIAL PROFICIENCIES |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/2/Text/7` | 0.516203 | At 1st level, you gain a number of proficiencies that represent  your basic training. These proficiencies are noted at the start  of this class. |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/32` | 0.400378 | **INTRODUCTION** |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/11/Text/26` | 0.400378 | **INTRODUCTION** |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/8/SectionHeader/6` | 0.396642 | **Skills** |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/51` | 0.376597 | At 1st level, you gain the listed  proficiency ranks in the following  statistics. You are untrained in anything  not listed unless you gain a better  proficiency rank in some other way. |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/7/SectionHeader/24` | 0.357424 | **Prerequisites** trained in Intimidation |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/58` | 0.353772 | **BACKGROUNDS** |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/5/Text/66` | 0.353772 | **BACKGROUNDS** |

### Query 46
- Text: What is the rule about At 1st level, you gain the listed  proficiency ranks in the following  statistics. You are untrained in anything  not listed unless you gain a better  proficiency rank in some other way.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/Text/51']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/1/Text/51', 'PZO22001 Starfinder Player Core 150-161::/page/3/Text/35', 'PZO22001 Starfinder Player Core 150-161::/page/2/Text/7']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/Text/51', 'PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/52', 'PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/50']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/52` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/50` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/51` | 0.992024 | At 1st level, you gain the listed  proficiency ranks in the following  statistics. You are untrained in anything  not listed unless you gain a better  proficiency rank in some other way. |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/35` | 0.743637 | At 3rd level and every 2 levels thereafter, you gain a skill  increase. You can use this increase either to increase your  proficiency rank to trained in one skill you're untrained in, or  to increase |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/2/Text/7` | 0.706615 | At 1st level, you gain a number of proficiencies that represent  your basic training. These proficiencies are noted at the start  of this class. |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/36` | 0.611362 | At 7th level, you can use skill increases to increase your  proficiency rank to master in a skill in which you're already  an expert, and at 15th level, you can use them to increase your  proficiency |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/5/Text/6` | 0.536878 | Your skill with armor further improves. Your proficiency  ranks for light armor, medium armor, heavy armor, and  unarmored defense increase to master. |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/23` | 0.528757 | At 2nd level and every 2 levels thereafter, you gain a skill feat.  Skill feats can be found in Chapter 5 and have the skill trait.  You must be trained or better in the corresponding skill to  select |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/4/Text/11` | 0.524727 | Your proficiency rank for Fortitude saves increases to  master. When you roll a success on a Fortitude save, you |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/4/Text/2` | 0.523184 | You remain alert to threats around you. Your proficiency  rank for Perception increases to expert. |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/4/Text/9` | 0.521528 | Your ability to unleash area attacks and utilize your  equipment improves. Your proficiency rank for your soldier |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/5/Text/8` | 0.520645 | Through skill and dedication, you've mastered devastating  weapons. Your proficiency rank for your soldier class DC  increases to master. Your proficiency ranks for unarmed  attacks, simple weapons, a |

### Query 47
- Text: Summarize **PERCEPTION**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/52']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/52', 'PZO22001 Starfinder Player Core 150-161::/page/1/Text/53', 'PZO22001 Starfinder Player Core 150-161::/page/4/SectionHeader/1']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/52', 'PZO22001 Starfinder Player Core 150-161::/page/1/Text/53', 'PZO22001 Starfinder Player Core 150-161::/page/1/Text/51']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/1/Text/53` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/1/Text/51` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/52` | 0.934058 | **PERCEPTION** |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/53` | 0.583165 | Trained in Perception |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/4/SectionHeader/1` | 0.523846 | PERCEPTION EXPERTISE 5TH |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/32` | 0.443002 | **INTRODUCTION** |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/11/Text/26` | 0.443002 | **INTRODUCTION** |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/5/Text/66` | 0.438809 | **BACKGROUNDS** |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/58` | 0.438809 | **BACKGROUNDS** |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/7/Text/46` | 0.438809 | **BACKGROUNDS** |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/69` | 0.438809 | **BACKGROUNDS** |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/4/Text/2` | 0.431666 | You remain alert to threats around you. Your proficiency  rank for Perception increases to expert. |

### Query 48
- Text: Summarize Trained in Perception
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/Text/53']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/1/Text/53', 'PZO22001 Starfinder Player Core 150-161::/page/4/Text/2', 'PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/637']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/Text/53', 'PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/52', 'PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/54']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/52` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/54` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/53` | 0.944339 | Trained in Perception |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/4/Text/2` | 0.582133 | You remain alert to threats around you. Your proficiency  rank for Perception increases to expert. |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/637` | 0.530916 | Soldier's Training |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/4/SectionHeader/1` | 0.494641 | PERCEPTION EXPERTISE 5TH |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/52` | 0.476849 | **PERCEPTION** |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/59` | 0.473909 | Trained in simple weapons Trained in martial weapons Trained in unarmed attacks |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/61` | 0.455212 | Trained in all armor Trained in unarmored defense |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/55` | 0.438266 | Expert in Fortitude Trained in Reflex Expert in Will |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/57` | 0.390323 | Trained in Intimidation Trained in a number of additional  skills equal to 3 plus your Intelligence  modifier |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/7/SectionHeader/24` | 0.385469 | **Prerequisites** trained in Intimidation |

### Query 49
- Text: What is the rule about **SAVING THROWS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/54']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/54', 'PZO22001 Starfinder Player Core 150-161::/page/5/Text/26', 'PZO22001 Starfinder Player Core 150-161::/page/10/Text/31']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/54', 'PZO22001 Starfinder Player Core 150-161::/page/1/Text/53', 'PZO22001 Starfinder Player Core 150-161::/page/1/Text/55']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/1/Text/53` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/1/Text/55` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/54` | 0.904955 | **SAVING THROWS** |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/5/Text/26` | 0.423276 | **Trigger** A creature you're observing succeeds at their  saving throw against your Area Fire or Auto-Fire attack. |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/10/Text/31` | 0.399184 | **Prerequisites** Shoving Shot |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/10/Text/4` | 0.357184 | **Prerequisites** Shoving Shot |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/2/Text/9` | 0.352072 | You have a knack for using powerful weapons to harry your  foes and hinder their movement, preventing them from  operating at their peak. If you make an attack with a weapon  that has the area trait ( |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/10/Text/33` | 0.337529 | in the wind. When you Shoving Shot, all creatures in the  area attempt the Fortitude save to avoid forced movement,  rather than just your primary target. |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/7/Text/26` | 0.321354 | **Critical Success** Your taunts sting hard. Until the start of  your next turn, any hostile actions that the creature  takes must include you as a target or include you in the  area; otherwise, the c |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/5/SectionHeader/28` | 0.305638 | **QUICK SWAP **[reaction] **FEAT 1** |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/6/Text/34` | 0.302380 | You know unleashing a barrage of gunfire can bring most  enemies low. You make a follow-up Strike against your  primary target using the same weapon. Ignore the unwieldy  trait on your weapon when usi |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/5/Text/42` | 0.300175 | You swipe your weapon in a wide swing to create a deadly  arc. Your weapon gains the area (burst 5 feet) and unwieldy  traits until the end of the turn. If your weapon has reach, the  burst radius bec |

### Query 50
- Text: Summarize Expert in Fortitude Trained in Reflex Expert in Will
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/Text/55']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/1/Text/55', 'PZO22001 Starfinder Player Core 150-161::/page/3/Text/32', 'PZO22001 Starfinder Player Core 150-161::/page/3/SectionHeader/30']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/Text/55', 'PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/56', 'PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/54']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/56` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/54` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/55` | 1.020666 | Expert in Fortitude Trained in Reflex Expert in Will |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/32` | 0.588885 | You've developed a knack for dodging danger. Your proficiency  rank for Reflex saves increases to expert. |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/3/SectionHeader/30` | 0.543247 | REFLEX EXPERTISE 3RD |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/10/Text/9` | 0.495398 | **Trigger** You and one adjacent ally attempt a Reflex or  Fortitude save against the same effect. |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/394` | 0.489766 | Fearsome bulwark, general feat, reflex expertise, skill increase |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/4/Text/11` | 0.468577 | Your proficiency rank for Fortitude saves increases to  master. When you roll a success on a Fortitude save, you |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/4/Text/2` | 0.467841 | You remain alert to threats around you. Your proficiency  rank for Perception increases to expert. |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/402` | 0.454714 | Armor expertise, general feat, skill increase, soldier expertise, tough as nails, weapon specialization |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/398` | 0.435202 | Ancestry feat, attribute boosts, perception expertise, skill increase, soldier weapon expert |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/4/Text/7` | 0.432309 | You have grown accustomed to wearing armor and  can make the most of its protection. Your proficiency  ranks for light armor, medium armor, heavy armor, and  unarmored defense increase to expert. You |

### Query 51
- Text: What is the rule about **SKILLS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/56']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/56', 'PZO22001 Starfinder Player Core 150-161::/page/1/Text/42', 'PZO22001 Starfinder Player Core 150-161::/page/9/Text/60']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/56', 'PZO22001 Starfinder Player Core 150-161::/page/8/SectionHeader/6', 'PZO22001 Starfinder Player Core 150-161::/page/1/Text/55', 'PZO22001 Starfinder Player Core 150-161::/page/1/Text/57']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/8/SectionHeader/6` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/1/Text/55` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/1/Text/57` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/56` | 0.864442 | **SKILLS** |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/42` | 0.864442 | **SKILLS** |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/60` | 0.719288 | **Archetypes** **SKILLS** |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/7/Text/38` | 0.651094 | **SKILLS** **FEATS** |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/49` | 0.651094 | **SKILLS** **FEATS** |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/5/Text/57` | 0.651094 | **SKILLS** **FEATS** |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/8/SectionHeader/6` | 0.640740 | **Skills** |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/23` | 0.458870 | At 2nd level and every 2 levels thereafter, you gain a skill feat.  Skill feats can be found in Chapter 5 and have the skill trait.  You must be trained or better in the corresponding skill to  select |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/35` | 0.422118 | At 3rd level and every 2 levels thereafter, you gain a skill  increase. You can use this increase either to increase your  proficiency rank to trained in one skill you're untrained in, or  to increase |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/51` | 0.421224 | At 1st level, you gain the listed  proficiency ranks in the following  statistics. You are untrained in anything  not listed unless you gain a better  proficiency rank in some other way. |

### Query 52
- Text: What is the rule about Trained in Intimidation Trained in a number of additional  skills equal to 3 plus your Intelligence  modifier?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/Text/57']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/1/Text/57', 'PZO22001 Starfinder Player Core 150-161::/page/7/SectionHeader/24', 'PZO22001 Starfinder Player Core 150-161::/page/3/Text/35']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/Text/57', 'PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/56', 'PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/58']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/56` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/58` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/57` | 0.954477 | Trained in Intimidation Trained in a number of additional  skills equal to 3 plus your Intelligence  modifier |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/7/SectionHeader/24` | 0.694765 | **Prerequisites** trained in Intimidation |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/35` | 0.568985 | At 3rd level and every 2 levels thereafter, you gain a skill  increase. You can use this increase either to increase your  proficiency rank to trained in one skill you're untrained in, or  to increase |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/7/Text/25` | 0.487285 | You taunt your enemy mercilessly, forcing them to  acknowledge you as an immediate threat. Attempt an  Intimidation check and compare it to the Will DC of  one enemy creature within 60 feet. This acti |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/5/Text/2` | 0.476217 | You inflict greater injuries with the weapons you know  best. You deal 2 additional damage with weapons and  unarmed attacks in which you're an expert. This damage  increases to 3 if you're a master, |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/26` | 0.469349 | Your sheer bulk terrifies foes, clearing a path for you on the  battlefield. You can use your Constitution modifier instead of  your Charisma modifier on Intimidation checks to Coerce or  Demoralize a |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/36` | 0.456561 | At 7th level, you can use skill increases to increase your  proficiency rank to master in a skill in which you're already  an expert, and at 15th level, you can use them to increase your  proficiency |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/23` | 0.452369 | At 2nd level and every 2 levels thereafter, you gain a skill feat.  Skill feats can be found in Chapter 5 and have the skill trait.  You must be trained or better in the corresponding skill to  select |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/10` | 0.447014 | Choose either Diplomacy or Society. You become trained in  the chosen skill and one Lore skill of your choice. When you  gain armor expertise, you gain expert proficiency in Diplomacy  or Society (whi |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/6/Text/29` | 0.439063 | You overwhelm the defenses of suppressed foes. Your  multiple attack penalty for attacks against suppressed  targets is –4 (–3 with an agile weapon) on your second  attack of the turn instead of –5, a |

### Query 53
- Text: What is the rule about **ATTACKS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/58']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/58', 'PZO22001 Starfinder Player Core 150-161::/page/7/Text/26', 'PZO22001 Starfinder Player Core 150-161::/page/9/Text/27']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/58', 'PZO22001 Starfinder Player Core 150-161::/page/1/Text/59', 'PZO22001 Starfinder Player Core 150-161::/page/1/Text/57']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/1/Text/59` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/1/Text/57` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/58` | 0.855189 | **ATTACKS** |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/7/Text/26` | 0.462434 | **Critical Success** Your taunts sting hard. Until the start of  your next turn, any hostile actions that the creature  takes must include you as a target or include you in the  area; otherwise, the c |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/27` | 0.462350 | You fight on to the absolute last, pushing yourself to make  one final attack at a foe. Make a Strike with a –2 circumstance  penalty, or make an Area Fire or Auto-Fire attack ignoring the |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/2/Text/12` | 0.405140 | You can focus fire on a single target when unleashing the  full devastation of your powerful area weaponry. Before you  make an area attack with a weapon (such as from the Area  Fire or Auto-Fire acti |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/7/Text/8` | 0.399723 | You make a well placed shot or unleash a hail of fire to cover  your allies. Make a ranged Strike against a target and select  one ally within range of the same attack. If your Strike hits  your targe |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/6/Text/10` | 0.384663 | **Trigger** You take damage. |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/11/Text/20` | 0.377385 | Your destructive power has become second nature as  enemies stand in awe of your overwhelming firepower. You  can use the Area Fire or Auto-Fire attacks as a single action.  However, you can never mak |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/8/Text/23` | 0.376873 | Your foe's momentary lapse in defense gives you an opening  Make a melee Strike against the triggering creature, ignoring  the unwieldy trait on any weapons you're wielding for this  Strike. This Stri |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/5` | 0.374538 | You concentrate fire on a specific target operating within  your weapon's threat range. Make a ranged Strike against the  triggering creature, ignoring the unwieldy trait of weapons you  wield for thi |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/6/Text/33` | 0.374248 | **Requirements** Your last action this turn was an Area Fire  attack. |

### Query 54
- Text: What is the rule about Trained in simple weapons Trained in martial weapons Trained in unarmed attacks?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/Text/59']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/1/Text/59', 'PZO22001 Starfinder Player Core 150-161::/page/1/Text/61', 'PZO22001 Starfinder Player Core 150-161::/page/4/Text/4']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/Text/59', 'PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/60', 'PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/58']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/60` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/58` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/59` | 0.918604 | Trained in simple weapons Trained in martial weapons Trained in unarmed attacks |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/61` | 0.660922 | Trained in all armor Trained in unarmored defense |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/4/Text/4` | 0.583667 | Through practical experience, you've learned how to use  your weapons in a way that both pulverizes your foes  and best takes advantage of your area attacks. Your  proficiency ranks for simple weapons |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/637` | 0.489224 | Soldier's Training |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/5/Text/8` | 0.470856 | Through skill and dedication, you've mastered devastating  weapons. Your proficiency rank for your soldier class DC  increases to master. Your proficiency ranks for unarmed  attacks, simple weapons, a |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/2/Text/20` | 0.461384 | You never count as being in the area of a ranged weapon  you've made an attack with. You gain resistance equal to half  your level (minimum 1) to all damage against attacks made by  suppressed targets |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/9` | 0.453634 | You realize that not every situation should be solved with  a gun. You're an intellectual as well as a warrior, solving  problems logically and learning about the galaxy. You keep  your mind sharp wit |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/5/Text/2` | 0.448659 | You inflict greater injuries with the weapons you know  best. You deal 2 additional damage with weapons and  unarmed attacks in which you're an expert. This damage  increases to 3 if you're a master, |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/6/Text/34` | 0.425645 | You know unleashing a barrage of gunfire can bring most  enemies low. You make a follow-up Strike against your  primary target using the same weapon. Ignore the unwieldy  trait on your weapon when usi |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/7` | 0.421003 | As long as you're wielding a two-handed melee weapon, you  meet the requirements for soldier feats that require an area  weapon. When you're using a soldier feat, any two-handed  melee weapon you're w |

### Query 55
- Text: Summarize **DEFENSES**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/60']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/60', 'PZO22001 Starfinder Player Core 150-161::/page/8/SectionHeader/13', 'PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/603']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/60', 'PZO22001 Starfinder Player Core 150-161::/page/1/Text/61', 'PZO22001 Starfinder Player Core 150-161::/page/1/Text/59']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/1/Text/61` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/1/Text/59` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/60` | 0.959826 | **DEFENSES** |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/8/SectionHeader/13` | 0.654852 | **OFFENSIVE DEFENSE **[two-actions] **FEAT 6** |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/603` | 0.597520 | Offensive Defense |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/8/SectionHeader/10` | 0.444403 | **Feats** |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/61` | 0.435042 | Trained in all armor Trained in unarmored defense |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/32` | 0.411981 | **INTRODUCTION** |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/11/Text/26` | 0.411981 | **INTRODUCTION** |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/8/SectionHeader/6` | 0.406384 | **Skills** |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/51` | 0.402846 | **SOLDIER'S TRAINING** **FEAT 16** |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/6/Text/10` | 0.400443 | **Trigger** You take damage. |

### Query 56
- Text: Summarize Trained in all armor Trained in unarmored defense
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/Text/61']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/1/Text/61', 'PZO22001 Starfinder Player Core 150-161::/page/1/Text/59', 'PZO22001 Starfinder Player Core 150-161::/page/4/Text/7']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/Text/61', 'PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/60', 'PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/62']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/60` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/62` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/61` | 1.021715 | Trained in all armor Trained in unarmored defense |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/59` | 0.774445 | Trained in simple weapons Trained in martial weapons Trained in unarmed attacks |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/4/Text/7` | 0.624185 | You have grown accustomed to wearing armor and  can make the most of its protection. Your proficiency  ranks for light armor, medium armor, heavy armor, and  unarmored defense increase to expert. You |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/5/Text/12` | 0.563837 | Your skill with armor is unparalleled. Your proficiency  ranks for light armor, medium armor, heavy armor, and  unarmored defense increase to legendary. |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/5/Text/6` | 0.556711 | Your skill with armor further improves. Your proficiency  ranks for light armor, medium armor, heavy armor, and  unarmored defense increase to master. |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/637` | 0.530792 | Soldier's Training |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/10` | 0.477495 | Choose either Diplomacy or Society. You become trained in  the chosen skill and one Lore skill of your choice. When you  gain armor expertise, you gain expert proficiency in Diplomacy  or Society (whi |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/1/ListItem/25` | 0.475549 | Assume there's not much of a personality or intellect under all that armor. |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/63` | 0.471051 | Trained in soldier class DC |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/2/Text/19` | 0.452536 | Your armor feels like a part of you and stands up to heavy fire  in the thick of battle. Your armor absorbs greater damage from  attacks made by enemies you've suppressed. In a fight, you  likely body |

### Query 57
- Text: What is the rule about **CLASS DC**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/62']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/62', 'PZO22001 Starfinder Player Core 150-161::/page/3/Text/42', 'PZO22001 Starfinder Player Core 150-161::/page/1/Text/34']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/62', 'PZO22001 Starfinder Player Core 150-161::/page/1/Text/61', 'PZO22001 Starfinder Player Core 150-161::/page/1/Text/63']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/1/Text/61` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/1/Text/63` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/62` | 0.881905 | **CLASS DC** |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/42` | 0.521525 | **CLASSES** |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/34` | 0.521525 | **CLASSES** |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/7/Text/31` | 0.491525 | **CLASSES** |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/5/Text/50` | 0.491525 | **CLASSES** |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/11/Text/27` | 0.491525 | **CLASSES** |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/53` | 0.491525 | **CLASSES** |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/63` | 0.434829 | Trained in soldier class DC |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/6/Text/38` | 0.396539 | **Requirements** You're wielding an area or automatic weapon. You use the blast of your weapon to push back your  adversaries. You Area Fire or Auto-Fire. Your primary target  must attempt a Fortitude |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/27` | 0.381301 | CLASS FEATURES |

### Query 58
- Text: What is the rule about Trained in soldier class DC?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/Text/63']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/1/Text/63', 'PZO22001 Starfinder Player Core 150-161::/page/5/Text/8', 'PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/637']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/1/Text/63', 'PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/62', 'PZO22001 Starfinder Player Core 150-161::/page/2/SectionHeader/1']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/62` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/2/SectionHeader/1` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/63` | 0.877518 | Trained in soldier class DC |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/5/Text/8` | 0.580563 | Through skill and dedication, you've mastered devastating  weapons. Your proficiency rank for your soldier class DC  increases to master. Your proficiency ranks for unarmed  attacks, simple weapons, a |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/637` | 0.575815 | Soldier's Training |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/6/Text/2` | 0.494349 | You'll see the following key terms in many soldier  class features. |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/20` | 0.478778 | At 1st level and every even-numbered level, you gain a soldier  class feat. These begin on page 155. |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/5/Text/14` | 0.471630 | You're a legendary hero (or outlaw) of the galaxy renowned  for the rain of destruction you unleash on a battlefield.  Your proficiency rank for your soldier class DC increases  to legendary. |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/61` | 0.463741 | Trained in all armor Trained in unarmored defense |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/59` | 0.457102 | Trained in simple weapons Trained in martial weapons Trained in unarmed attacks |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/62` | 0.450242 | **CLASS DC** |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/11/Text/1` | 0.415771 | soldier class feat you have that grants a reaction. At the  start of your turn, you gain an additional reaction that you  can only use for the selected class feat or an action granted  by the selected |

### Query 59
- Text: Summarize **SOLDIER ADVANCEMENT**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/2/SectionHeader/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/2/SectionHeader/1', 'PZO22001 Starfinder Player Core 150-161::/page/10/Text/40', 'PZO22001 Starfinder Player Core 150-161::/page/10/Text/36']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/2/SectionHeader/1', 'PZO22001 Starfinder Player Core 150-161::/page/1/Text/63', 'PZO22001 Starfinder Player Core 150-161::/page/2/Table/2']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/1/Text/63` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/2/Table/2` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/2/SectionHeader/1` | 1.003835 | **SOLDIER ADVANCEMENT** |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/10/Text/40` | 0.709928 | **SOLDIER** |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/10/Text/36` | 0.709928 | **SOLDIER** |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/11/Text/10` | 0.667928 | **SOLDIER** |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/11/Text/14` | 0.667928 | **SOLDIER** |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/10/Text/8` | 0.667928 | **SOLDIER** |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/10/Text/3` | 0.667928 | **SOLDIER** |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/47` | 0.667928 | **SOLDIER** |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/10/Text/26` | 0.667928 | **SOLDIER** |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/10/Text/13` | 0.667928 | **SOLDIER** |

### Query 60
- Text: Lookup values for Your LevelClass Features1Ancestry and background, attribute boosts,
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/2/Table/2']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/1/Text/30', 'PZO22001 Starfinder Player Core 150-161::/page/2/Table/2', 'PZO22001 Starfinder Player Core 150-161::/page/2/Text/4']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/2/Table/2', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/387', 'PZO22001 Starfinder Player Core 150-161::/page/2/SectionHeader/1']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/387` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/2/SectionHeader/1` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/30` | 0.671822 | In addition to what you get from your class at 1st level, you have the benefits of  your selected ancestry and background, as described in Chapter 2. |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/2/Table/2` | 0.668310 | Your LevelClass Features1Ancestry and background, attribute boosts, initial proficiencies, suppressing fire, primary target, soldier fighting style, walking armory, soldier feat2Skill feat, soldier fe |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/2/Text/4` | 0.624096 | In addition to what you get from your class at 1st level, you  have four free boosts to different attribute modifiers. |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/8` | 0.573626 | At 1st level, your class gives you  an attribute boost to Constitution. |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/2/Text/5` | 0.545659 | At 5th level and every 5 levels thereafter, you get four free  boosts to different attribute modifiers. If an attribute modifier  is already +4 or higher, it takes two boosts to increase it; you  get |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/388` | 0.528105 | Class Features |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/28` | 0.519199 | You gain these abilities as a soldier. Abilities gained at higher levels list the level at  which you gain them next to the features' names. |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/390` | 0.514322 | Ancestry and background, attribute boosts, initial proficiencies, suppressing fire, primary target, soldier fighting style, walking armory, soldier feat |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/39` | 0.511768 | In addition to the initial ancestry feat you started with, you  gain an ancestry feat at 5th level and every 4 levels thereafter.  The list of ancestry feats available to you can be found in your  anc |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/398` | 0.498135 | Ancestry feat, attribute boosts, perception expertise, skill increase, soldier weapon expert |

### Query 61
- Text: Summarize Your Level
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/387']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/387', 'PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/552', 'PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/602']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/387', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/388', 'PZO22001 Starfinder Player Core 150-161::/page/2/Table/2']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/388` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/2/Table/2` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/387` | 0.853813 | Your Level |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/552` | 0.729099 | Level |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/602` | 0.729099 | Level |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/5/SectionHeader/43` | 0.549996 | 2ND LEVEL |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/20` | 0.534036 | 4TH LEVEL |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/11/SectionHeader/3` | 0.523376 | 18TH LEVEL |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/8/SectionHeader/24` | 0.514596 | 8TH LEVEL |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/17` | 0.513306 | 14TH LEVEL |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/42` | 0.501266 | 16TH LEVEL |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/11/SectionHeader/16` | 0.497936 | 20TH LEVEL |

### Query 62
- Text: What is the rule about Class Features?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/388']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/388', 'PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/27', 'PZO22001 Starfinder Player Core 150-161::/page/6/Text/2']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/388', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/387', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/389']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/387` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/389` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/388` | 0.835742 | Class Features |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/27` | 0.700239 | CLASS FEATURES |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/6/Text/2` | 0.556007 | You'll see the following key terms in many soldier  class features. |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/2/Table/2` | 0.424223 | Your LevelClass Features1Ancestry and background, attribute boosts, initial proficiencies, suppressing fire, primary target, soldier fighting style, walking armory, soldier feat2Skill feat, soldier fe |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/28` | 0.423954 | You gain these abilities as a soldier. Abilities gained at higher levels list the level at  which you gain them next to the features' names. |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/8` | 0.417454 | At 1st level, your class gives you  an attribute boost to Constitution. |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/8/SectionHeader/4` | 0.414280 | **Attributes** |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/42` | 0.407880 | **CLASSES** |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/11/Text/27` | 0.407880 | **CLASSES** |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/5/Text/50` | 0.407880 | **CLASSES** |

### Query 63
- Text: Summarize 1
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/389']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/389', 'PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/646', 'PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/612']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/389', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/388', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/390']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/388` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/390` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/389` | 0.669108 | 1 |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/612` | 0.669108 | 1 |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/646` | 0.669108 | 1 |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/566` | 0.627108 | 1 |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/620` | 0.627108 | 1 |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/618` | 0.627108 | 1 |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/622` | 0.513765 | 2 |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/391` | 0.513765 | 2 |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/650` | 0.513765 | 2 |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/600` | 0.513765 | 2 |

### Query 64
- Text: What is the rule about Ancestry and background, attribute boosts,?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/390']
- Expected found: `True`
- Expected rank: `4`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/406', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/398', 'PZO22001 Starfinder Player Core 150-161::/page/1/Text/30']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/390', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/391', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/389']
- Expanded expected found: `True`
- Expanded expected rank: `4`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/391` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/389` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/406` | 0.604113 | Ancestry feat, skill increase |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/398` | 0.598302 | Ancestry feat, attribute boosts, perception expertise, skill increase, soldier weapon expert |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/30` | 0.581688 | In addition to what you get from your class at 1st level, you have the benefits of  your selected ancestry and background, as described in Chapter 2. |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/390` | 0.533174 | Ancestry and background, attribute boosts, initial proficiencies, suppressing fire, primary target, soldier fighting style, walking armory, soldier feat |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/2/Text/5` | 0.509477 | At 5th level and every 5 levels thereafter, you get four free  boosts to different attribute modifiers. If an attribute modifier  is already +4 or higher, it takes two boosts to increase it; you  get |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/29` | 0.506753 | ANCESTRY AND BACKGROUND |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/39` | 0.497227 | In addition to the initial ancestry feat you started with, you  gain an ancestry feat at 5th level and every 4 levels thereafter.  The list of ancestry feats available to you can be found in your  anc |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/33` | 0.496934 | **ANCESTRIES & ** **BACKGROUNDS** |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/422` | 0.486650 | Ancestry feat, legendary armor, skill increase |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/414` | 0.485461 | Ancestry feat, armor mastery, skill increase |

### Query 65
- Text: Summarize 2
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/391']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/391', 'PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/600', 'PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/650']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/391', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/390', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/392']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/390` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/392` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/391` | 0.689465 | 2 |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/600` | 0.689465 | 2 |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/650` | 0.689465 | 2 |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/622` | 0.647465 | 2 |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/634` | 0.647465 | 2 |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/389` | 0.459336 | 1 |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/620` | 0.459336 | 1 |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/618` | 0.459336 | 1 |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/566` | 0.459336 | 1 |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/646` | 0.459336 | 1 |

### Query 66
- Text: What is the rule about Skill feat, soldier feat?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/392']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/400', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/392', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/396']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/392', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/391', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/393']
- Expanded expected found: `True`
- Expanded expected rank: `3`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/391` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/393` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/396` | 0.925386 | Skill feat, soldier feat |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/400` | 0.925386 | Skill feat, soldier feat |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/392` | 0.925386 | Skill feat, soldier feat |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/404` | 0.883386 | Skill feat, soldier feat |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/412` | 0.883386 | Skill feat, soldier feat |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/416` | 0.883386 | Skill feat, soldier feat |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/420` | 0.883386 | Skill feat, soldier feat |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/424` | 0.883386 | Skill feat, soldier feat |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/408` | 0.757525 | Attribute boosts, skill feat, soldier feat |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/428` | 0.757525 | Attribute boosts, skill feat, soldier feat |

### Query 67
- Text: Summarize 3
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/393']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/393', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/391', 'PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/650']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/393', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/394', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/392']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/394` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/392` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/393` | 0.731895 | 3 |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/391` | 0.558533 | 2 |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/650` | 0.558533 | 2 |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/622` | 0.516533 | 2 |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/634` | 0.516533 | 2 |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/600` | 0.516533 | 2 |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/3/SectionHeader/27` | 0.487018 | GENERAL FEATS 3RD |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/389` | 0.435144 | 1 |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/620` | 0.435144 | 1 |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/646` | 0.435144 | 1 |

### Query 68
- Text: What is the rule about Fearsome bulwark, general feat, reflex?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/394']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/394', 'PZO22001 Starfinder Player Core 150-161::/page/3/SectionHeader/24', 'PZO22001 Starfinder Player Core 150-161::/page/3/Text/29']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/394', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/395', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/393']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/395` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/393` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/394` | 0.844901 | Fearsome bulwark, general feat, reflex expertise, skill increase |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/3/SectionHeader/24` | 0.548522 | FEARSOME BULWARK 3RD |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/29` | 0.471750 | At 3rd level and every 4 levels thereafter, you gain a general  feat. General feats are listed in Chapter 5. |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/32` | 0.392178 | You've developed a knack for dodging danger. Your proficiency  rank for Reflex saves increases to expert. |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/10/Text/9` | 0.386776 | **Trigger** You and one adjacent ally attempt a Reflex or  Fortitude save against the same effect. |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/11/Text/2` | 0.384588 | You can change the reaction selected for this feat when  you make your daily preparations as long as the new feat  meets the requirements. |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/55` | 0.378986 | Expert in Fortitude Trained in Reflex Expert in Will |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/14` | 0.373103 | You unnerve foes with a look, or similarly unsettle them with  subtle mannerisms or veiled threats. One enemy creature of  your choice within 60 feet becomes suppressed until the start  of your next t |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/426` | 0.371925 | General feat, legendary soldier, skill increase |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/5/Text/16` | 0.370901 | At every level that you gain a soldier feat, you can  select one of the following feats. You must satisfy any  prerequisites before selecting the feat. |

### Query 69
- Text: Summarize 4
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/395']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/395', 'PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/610', 'PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/636']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/395', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/396', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/394']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/396` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/394` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/395` | 0.774878 | 4 |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/610` | 0.774878 | 4 |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/636` | 0.774878 | 4 |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/568` | 0.732878 | 4 |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/648` | 0.732878 | 4 |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/614` | 0.732878 | 4 |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/20` | 0.487593 | 4TH LEVEL |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/393` | 0.459139 | 3 |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/634` | 0.438507 | 2 |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/650` | 0.438507 | 2 |

### Query 70
- Text: What is the rule about Skill feat, soldier feat?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/396']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/400', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/392', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/396']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/396', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/395', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/397']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/395` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/397` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/396` | 0.925386 | Skill feat, soldier feat |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/400` | 0.925386 | Skill feat, soldier feat |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/392` | 0.925386 | Skill feat, soldier feat |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/404` | 0.883386 | Skill feat, soldier feat |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/412` | 0.883386 | Skill feat, soldier feat |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/416` | 0.883386 | Skill feat, soldier feat |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/420` | 0.883386 | Skill feat, soldier feat |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/424` | 0.883386 | Skill feat, soldier feat |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/408` | 0.757525 | Attribute boosts, skill feat, soldier feat |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/428` | 0.757525 | Attribute boosts, skill feat, soldier feat |

### Query 71
- Text: Summarize 5
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/397']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/397', 'PZO22001 Starfinder Player Core 150-161::/page/3/SectionHeader/37', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/399']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/397', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/398', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/396']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/398` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/396` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/397` | 0.772788 | 5 |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/3/SectionHeader/37` | 0.521739 | ANCESTRY FEATS 5TH |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/399` | 0.509672 | 6 |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/594` | 0.467672 | 6 |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/576` | 0.467672 | 6 |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/586` | 0.467672 | 6 |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/592` | 0.467672 | 6 |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/616` | 0.467672 | 6 |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/604` | 0.467672 | 6 |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/610` | 0.446968 | 4 |

### Query 72
- Text: What is the rule about Ancestry feat, attribute boosts, perception?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/398']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/398', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/406', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/414']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/398', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/397', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/399']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/397` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/399` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/398` | 0.766406 | Ancestry feat, attribute boosts, perception expertise, skill increase, soldier weapon expert |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/406` | 0.743969 | Ancestry feat, skill increase |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/414` | 0.654288 | Ancestry feat, armor mastery, skill increase |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/422` | 0.605579 | Ancestry feat, legendary armor, skill increase |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/39` | 0.600080 | In addition to the initial ancestry feat you started with, you  gain an ancestry feat at 5th level and every 4 levels thereafter.  The list of ancestry feats available to you can be found in your  anc |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/428` | 0.597138 | Attribute boosts, skill feat, soldier feat |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/408` | 0.597138 | Attribute boosts, skill feat, soldier feat |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/390` | 0.543155 | Ancestry and background, attribute boosts, initial proficiencies, suppressing fire, primary target, soldier fighting style, walking armory, soldier feat |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/2/Table/2` | 0.458764 | Your LevelClass Features1Ancestry and background, attribute boosts, initial proficiencies, suppressing fire, primary target, soldier fighting style, walking armory, soldier feat2Skill feat, soldier fe |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/2/Text/5` | 0.458697 | At 5th level and every 5 levels thereafter, you get four free  boosts to different attribute modifiers. If an attribute modifier  is already +4 or higher, it takes two boosts to increase it; you  get |

### Query 73
- Text: Summarize 6
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/399']
- Expected found: `True`
- Expected rank: `5`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/576', 'PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/586', 'PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/592']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/399', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/398', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/400']
- Expanded expected found: `True`
- Expanded expected rank: `5`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/398` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/400` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/576` | 0.783525 | 6 |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/586` | 0.783525 | 6 |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/592` | 0.783525 | 6 |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/616` | 0.741525 | 6 |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/399` | 0.741525 | 6 |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/604` | 0.741525 | 6 |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/594` | 0.741525 | 6 |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/7/SectionHeader/4` | 0.508078 | 6TH LEVEL |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/401` | 0.496931 | 7 |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/606` | 0.468373 | 16 |

### Query 74
- Text: What is the rule about Skill feat, soldier feat?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/400']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/400', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/392', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/396']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/400', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/401', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/399']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/401` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/399` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/396` | 0.925386 | Skill feat, soldier feat |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/400` | 0.925386 | Skill feat, soldier feat |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/392` | 0.925386 | Skill feat, soldier feat |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/404` | 0.883386 | Skill feat, soldier feat |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/412` | 0.883386 | Skill feat, soldier feat |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/416` | 0.883386 | Skill feat, soldier feat |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/420` | 0.883386 | Skill feat, soldier feat |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/424` | 0.883386 | Skill feat, soldier feat |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/408` | 0.757525 | Attribute boosts, skill feat, soldier feat |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/428` | 0.757525 | Attribute boosts, skill feat, soldier feat |

### Query 75
- Text: Summarize 7
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/401']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/401', 'PZO22001 Starfinder Player Core 150-161::/page/5/SectionHeader/1', 'PZO22001 Starfinder Player Core 150-161::/page/4/SectionHeader/6']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/401', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/402', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/400']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/402` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/400` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/401` | 0.766039 | 7 |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/5/SectionHeader/1` | 0.585452 | WEAPON SPECIALIZATION 7TH |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/4/SectionHeader/6` | 0.576430 | ARMOR EXPERTISE 7TH |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/4/SectionHeader/8` | 0.526417 | SOLDIER EXPERTISE 7TH |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/399` | 0.473241 | 6 |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/604` | 0.473241 | 6 |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/592` | 0.473241 | 6 |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/576` | 0.473241 | 6 |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/594` | 0.473241 | 6 |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/586` | 0.473241 | 6 |

### Query 76
- Text: What is the rule about Armor expertise, general feat, skill increase,?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/402']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/402', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/414', 'PZO22001 Starfinder Player Core 150-161::/page/4/Text/7']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/402', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/403', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/401']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/403` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/401` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/402` | 0.787588 | Armor expertise, general feat, skill increase, soldier expertise, tough as nails, weapon specialization |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/414` | 0.700860 | Ancestry feat, armor mastery, skill increase |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/4/Text/7` | 0.683583 | You have grown accustomed to wearing armor and  can make the most of its protection. Your proficiency  ranks for light armor, medium armor, heavy armor, and  unarmored defense increase to expert. You |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/422` | 0.621024 | Ancestry feat, legendary armor, skill increase |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/5/Text/6` | 0.617059 | Your skill with armor further improves. Your proficiency  ranks for light armor, medium armor, heavy armor, and  unarmored defense increase to master. |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/5/Text/12` | 0.606093 | Your skill with armor is unparalleled. Your proficiency  ranks for light armor, medium armor, heavy armor, and  unarmored defense increase to legendary. |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/410` | 0.597812 | General feat, skill increase, soldier's resolution |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/426` | 0.595083 | General feat, legendary soldier, skill increase |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/10` | 0.586757 | Choose either Diplomacy or Society. You become trained in  the chosen skill and one Lore skill of your choice. When you  gain armor expertise, you gain expert proficiency in Diplomacy  or Society (whi |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/398` | 0.582760 | Ancestry feat, attribute boosts, perception expertise, skill increase, soldier weapon expert |

### Query 77
- Text: Summarize 8
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/403']
- Expected found: `True`
- Expected rank: `6`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/558', 'PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/626', 'PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/608']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/403', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/404', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/402']
- Expanded expected found: `True`
- Expanded expected rank: `6`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/404` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/402` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/608` | 0.787704 | 8 |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/558` | 0.787704 | 8 |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/626` | 0.787704 | 8 |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/554` | 0.745704 | 8 |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/572` | 0.745704 | 8 |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/403` | 0.745704 | 8 |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/8/SectionHeader/24` | 0.546940 | 8TH LEVEL |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/401` | 0.471909 | 7 |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/405` | 0.452855 | 9 |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/576` | 0.445146 | 6 |

### Query 78
- Text: What is the rule about Skill feat, soldier feat?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/404']
- Expected found: `True`
- Expected rank: `4`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/400', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/392', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/396']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/404', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/403', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/405']
- Expanded expected found: `True`
- Expanded expected rank: `4`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/403` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/405` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/396` | 0.925386 | Skill feat, soldier feat |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/400` | 0.925386 | Skill feat, soldier feat |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/392` | 0.925386 | Skill feat, soldier feat |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/404` | 0.883386 | Skill feat, soldier feat |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/412` | 0.883386 | Skill feat, soldier feat |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/416` | 0.883386 | Skill feat, soldier feat |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/420` | 0.883386 | Skill feat, soldier feat |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/424` | 0.883386 | Skill feat, soldier feat |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/408` | 0.757525 | Attribute boosts, skill feat, soldier feat |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/428` | 0.757525 | Attribute boosts, skill feat, soldier feat |

### Query 79
- Text: Summarize 9
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/405']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/405', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/403', 'PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/554']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/405', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/404', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/406']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/404` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/406` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/405` | 0.770045 | 9 |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/403` | 0.497491 | 8 |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/554` | 0.497491 | 8 |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/572` | 0.455491 | 8 |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/626` | 0.455491 | 8 |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/558` | 0.455491 | 8 |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/608` | 0.455491 | 8 |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/407` | 0.446800 | 10 |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/580` | 0.446800 | 10 |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/560` | 0.446800 | 10 |

### Query 80
- Text: What is the rule about Ancestry feat, skill increase?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/406']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/406', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/414', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/422']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/406', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/405', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/407']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/405` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/407` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/406` | 0.926911 | Ancestry feat, skill increase |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/414` | 0.804013 | Ancestry feat, armor mastery, skill increase |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/422` | 0.780501 | Ancestry feat, legendary armor, skill increase |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/398` | 0.689372 | Ancestry feat, attribute boosts, perception expertise, skill increase, soldier weapon expert |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/39` | 0.686284 | In addition to the initial ancestry feat you started with, you  gain an ancestry feat at 5th level and every 4 levels thereafter.  The list of ancestry feats available to you can be found in your  anc |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/408` | 0.564273 | Attribute boosts, skill feat, soldier feat |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/428` | 0.564273 | Attribute boosts, skill feat, soldier feat |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/426` | 0.559201 | General feat, legendary soldier, skill increase |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/410` | 0.555028 | General feat, skill increase, soldier's resolution |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/23` | 0.541636 | At 2nd level and every 2 levels thereafter, you gain a skill feat.  Skill feats can be found in Chapter 5 and have the skill trait.  You must be trained or better in the corresponding skill to  select |

### Query 81
- Text: Summarize 10
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/407']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/407', 'PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/632', 'PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/556']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/407', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/406', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/408']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/406` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/408` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/407` | 0.782219 | 10 |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/556` | 0.782219 | 10 |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/632` | 0.782219 | 10 |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/580` | 0.740219 | 10 |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/560` | 0.740219 | 10 |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/570` | 0.740219 | 10 |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/9/SectionHeader/12` | 0.501945 | 10TH LEVEL |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/29` | 0.500459 | **DANCE!** **FEAT 10** |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/409` | 0.492929 | 11 |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/9/SectionHeader/22` | 0.462148 | **COME GET SOME! **[reaction] **FEAT 10** |

### Query 82
- Text: What is the rule about Attribute boosts, skill feat, soldier feat?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/408']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/428', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/408', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/404']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/408', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/409', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/407']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/409` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/407` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/428` | 0.903542 | Attribute boosts, skill feat, soldier feat |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/408` | 0.903542 | Attribute boosts, skill feat, soldier feat |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/404` | 0.740241 | Skill feat, soldier feat |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/392` | 0.698241 | Skill feat, soldier feat |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/424` | 0.698241 | Skill feat, soldier feat |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/400` | 0.698241 | Skill feat, soldier feat |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/396` | 0.698241 | Skill feat, soldier feat |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/416` | 0.698241 | Skill feat, soldier feat |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/412` | 0.698241 | Skill feat, soldier feat |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/420` | 0.698241 | Skill feat, soldier feat |

### Query 83
- Text: Summarize 11
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/409']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/409', 'PZO22001 Starfinder Player Core 150-161::/page/5/SectionHeader/3', 'PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/582']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/409', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/410', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/408']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/410` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/408` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/409` | 0.764621 | 11 |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/5/SectionHeader/3` | 0.588010 | SOLDIER'S RESOLUTION 11TH |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/582` | 0.535902 | 12 |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/411` | 0.493902 | 12 |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/598` | 0.493902 | 12 |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/588` | 0.493902 | 12 |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/562` | 0.493902 | 12 |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/624` | 0.493902 | 12 |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/407` | 0.479429 | 10 |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/556` | 0.479429 | 10 |

### Query 84
- Text: What is the rule about General feat, skill increase, soldier's resolution?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/410']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/410', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/426', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/416']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/410', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/409', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/411']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/409` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/411` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/410` | 0.928383 | General feat, skill increase, soldier's resolution |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/426` | 0.753276 | General feat, legendary soldier, skill increase |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/416` | 0.685917 | Skill feat, soldier feat |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/400` | 0.643917 | Skill feat, soldier feat |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/392` | 0.643917 | Skill feat, soldier feat |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/412` | 0.643917 | Skill feat, soldier feat |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/404` | 0.643917 | Skill feat, soldier feat |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/420` | 0.643917 | Skill feat, soldier feat |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/424` | 0.643917 | Skill feat, soldier feat |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/396` | 0.643917 | Skill feat, soldier feat |

### Query 85
- Text: Summarize 12
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/411']
- Expected found: `True`
- Expected rank: `4`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/582', 'PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/588', 'PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/598']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/411', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/412', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/410']
- Expanded expected found: `True`
- Expanded expected rank: `4`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/412` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/410` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/598` | 0.783359 | 12 |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/582` | 0.783359 | 12 |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/588` | 0.783359 | 12 |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/411` | 0.741359 | 12 |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/562` | 0.741359 | 12 |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/624` | 0.741359 | 12 |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/413` | 0.524768 | 13 |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/9/SectionHeader/39` | 0.516176 | 12TH LEVEL |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/409` | 0.515039 | 11 |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/1` | 0.440593 | **HAMMER THE NAIL** **FEAT 12** |

### Query 86
- Text: What is the rule about Skill feat, soldier feat?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/412']
- Expected found: `True`
- Expected rank: `5`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/400', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/392', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/396']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/412', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/411', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/413']
- Expanded expected found: `True`
- Expanded expected rank: `5`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/411` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/413` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/396` | 0.925386 | Skill feat, soldier feat |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/400` | 0.925386 | Skill feat, soldier feat |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/392` | 0.925386 | Skill feat, soldier feat |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/404` | 0.883386 | Skill feat, soldier feat |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/412` | 0.883386 | Skill feat, soldier feat |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/416` | 0.883386 | Skill feat, soldier feat |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/420` | 0.883386 | Skill feat, soldier feat |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/424` | 0.883386 | Skill feat, soldier feat |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/408` | 0.757525 | Attribute boosts, skill feat, soldier feat |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/428` | 0.757525 | Attribute boosts, skill feat, soldier feat |

### Query 87
- Text: Summarize 13
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/413']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/413', 'PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/598', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/411']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/413', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/412', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/414']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/412` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/414` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/413` | 0.781589 | 13 |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/598` | 0.578297 | 12 |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/411` | 0.578297 | 12 |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/588` | 0.536297 | 12 |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/562` | 0.536297 | 12 |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/624` | 0.536297 | 12 |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/582` | 0.536297 | 12 |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/415` | 0.531543 | 14 |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/644` | 0.531543 | 14 |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/642` | 0.531543 | 14 |

### Query 88
- Text: What is the rule about Ancestry feat, armor mastery, skill increase?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/414']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/414', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/422', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/406']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/414', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/415', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/413']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/415` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/413` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/414` | 0.913796 | Ancestry feat, armor mastery, skill increase |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/422` | 0.816364 | Ancestry feat, legendary armor, skill increase |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/406` | 0.801918 | Ancestry feat, skill increase |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/398` | 0.648008 | Ancestry feat, attribute boosts, perception expertise, skill increase, soldier weapon expert |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/39` | 0.619071 | In addition to the initial ancestry feat you started with, you  gain an ancestry feat at 5th level and every 4 levels thereafter.  The list of ancestry feats available to you can be found in your  anc |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/390` | 0.575529 | Ancestry and background, attribute boosts, initial proficiencies, suppressing fire, primary target, soldier fighting style, walking armory, soldier feat |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/402` | 0.567042 | Armor expertise, general feat, skill increase, soldier expertise, tough as nails, weapon specialization |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/408` | 0.542309 | Attribute boosts, skill feat, soldier feat |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/428` | 0.542309 | Attribute boosts, skill feat, soldier feat |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/2/Table/2` | 0.539223 | Your LevelClass Features1Ancestry and background, attribute boosts, initial proficiencies, suppressing fire, primary target, soldier fighting style, walking armory, soldier feat2Skill feat, soldier fe |

### Query 89
- Text: What is the rule about Skill feat, soldier feat?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/416']
- Expected found: `True`
- Expected rank: `6`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/400', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/392', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/396']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/416', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/415', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/417']
- Expanded expected found: `True`
- Expanded expected rank: `6`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/415` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/417` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/396` | 0.925386 | Skill feat, soldier feat |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/400` | 0.925386 | Skill feat, soldier feat |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/392` | 0.925386 | Skill feat, soldier feat |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/404` | 0.883386 | Skill feat, soldier feat |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/412` | 0.883386 | Skill feat, soldier feat |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/416` | 0.883386 | Skill feat, soldier feat |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/420` | 0.883386 | Skill feat, soldier feat |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/424` | 0.883386 | Skill feat, soldier feat |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/408` | 0.757525 | Attribute boosts, skill feat, soldier feat |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/428` | 0.757525 | Attribute boosts, skill feat, soldier feat |

### Query 90
- Text: What is the rule about Attribute boosts, general feat, skill increase,?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/418']
- Expected found: `True`
- Expected rank: `6`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/408', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/428', 'PZO22001 Starfinder Player Core 150-161::/page/2/Text/5']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/418', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/417', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/419']
- Expanded expected found: `True`
- Expanded expected rank: `6`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/417` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/419` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/408` | 0.745931 | Attribute boosts, skill feat, soldier feat |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/428` | 0.745931 | Attribute boosts, skill feat, soldier feat |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/2/Text/5` | 0.636240 | At 5th level and every 5 levels thereafter, you get four free  boosts to different attribute modifiers. If an attribute modifier  is already +4 or higher, it takes two boosts to increase it; you  get |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/398` | 0.587909 | Ancestry feat, attribute boosts, perception expertise, skill increase, soldier weapon expert |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/29` | 0.579655 | At 3rd level and every 4 levels thereafter, you gain a general  feat. General feats are listed in Chapter 5. |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/418` | 0.578383 | Attribute boosts, general feat, skill increase, soldier weapon mastery, unshakable juggernaut |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/406` | 0.577338 | Ancestry feat, skill increase |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/426` | 0.567455 | General feat, legendary soldier, skill increase |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/410` | 0.561386 | General feat, skill increase, soldier's resolution |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/23` | 0.559100 | At 2nd level and every 2 levels thereafter, you gain a skill feat.  Skill feats can be found in Chapter 5 and have the skill trait.  You must be trained or better in the corresponding skill to  select |

### Query 91
- Text: What is the rule about Skill feat, soldier feat?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/420']
- Expected found: `True`
- Expected rank: `7`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/400', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/392', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/396']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/420', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/419', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/421']
- Expanded expected found: `True`
- Expanded expected rank: `7`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/419` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/421` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/396` | 0.925386 | Skill feat, soldier feat |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/400` | 0.925386 | Skill feat, soldier feat |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/392` | 0.925386 | Skill feat, soldier feat |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/404` | 0.883386 | Skill feat, soldier feat |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/412` | 0.883386 | Skill feat, soldier feat |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/416` | 0.883386 | Skill feat, soldier feat |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/420` | 0.883386 | Skill feat, soldier feat |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/424` | 0.883386 | Skill feat, soldier feat |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/408` | 0.757525 | Attribute boosts, skill feat, soldier feat |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/428` | 0.757525 | Attribute boosts, skill feat, soldier feat |

### Query 92
- Text: What is the rule about Ancestry feat, legendary armor, skill increase?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/422']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/422', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/414', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/406']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/422', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/423', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/421']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/423` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/421` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/422` | 0.900220 | Ancestry feat, legendary armor, skill increase |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/414` | 0.836435 | Ancestry feat, armor mastery, skill increase |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/406` | 0.795297 | Ancestry feat, skill increase |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/398` | 0.648488 | Ancestry feat, attribute boosts, perception expertise, skill increase, soldier weapon expert |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/426` | 0.630059 | General feat, legendary soldier, skill increase |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/39` | 0.607341 | In addition to the initial ancestry feat you started with, you  gain an ancestry feat at 5th level and every 4 levels thereafter.  The list of ancestry feats available to you can be found in your  anc |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/390` | 0.572806 | Ancestry and background, attribute boosts, initial proficiencies, suppressing fire, primary target, soldier fighting style, walking armory, soldier feat |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/402` | 0.556657 | Armor expertise, general feat, skill increase, soldier expertise, tough as nails, weapon specialization |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/5/Text/12` | 0.552840 | Your skill with armor is unparalleled. Your proficiency  ranks for light armor, medium armor, heavy armor, and  unarmored defense increase to legendary. |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/428` | 0.549344 | Attribute boosts, skill feat, soldier feat |

### Query 93
- Text: What is the rule about Skill feat, soldier feat?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/424']
- Expected found: `True`
- Expected rank: `8`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/400', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/392', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/396']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/424', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/425', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/423']
- Expanded expected found: `True`
- Expanded expected rank: `8`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/425` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/423` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/396` | 0.925386 | Skill feat, soldier feat |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/400` | 0.925386 | Skill feat, soldier feat |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/392` | 0.925386 | Skill feat, soldier feat |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/404` | 0.883386 | Skill feat, soldier feat |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/412` | 0.883386 | Skill feat, soldier feat |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/416` | 0.883386 | Skill feat, soldier feat |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/420` | 0.883386 | Skill feat, soldier feat |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/424` | 0.883386 | Skill feat, soldier feat |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/408` | 0.757525 | Attribute boosts, skill feat, soldier feat |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/428` | 0.757525 | Attribute boosts, skill feat, soldier feat |

### Query 94
- Text: What is the rule about General feat, legendary soldier, skill increase?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/426']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/426', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/410', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/408']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/426', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/425', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/427']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/425` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/427` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/426` | 0.894378 | General feat, legendary soldier, skill increase |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/410` | 0.780613 | General feat, skill increase, soldier's resolution |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/408` | 0.717377 | Attribute boosts, skill feat, soldier feat |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/428` | 0.675377 | Attribute boosts, skill feat, soldier feat |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/400` | 0.670844 | Skill feat, soldier feat |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/396` | 0.670844 | Skill feat, soldier feat |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/392` | 0.670844 | Skill feat, soldier feat |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/404` | 0.670844 | Skill feat, soldier feat |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/412` | 0.670844 | Skill feat, soldier feat |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/416` | 0.670844 | Skill feat, soldier feat |

### Query 95
- Text: What is the rule about Attribute boosts, skill feat, soldier feat?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/428']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/428', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/408', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/404']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/428', 'PZO22001 Starfinder Player Core 150-161::/page/2/SectionHeader/3', 'PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/427']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/2/SectionHeader/3` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/427` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/428` | 0.903542 | Attribute boosts, skill feat, soldier feat |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/408` | 0.903542 | Attribute boosts, skill feat, soldier feat |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/404` | 0.740241 | Skill feat, soldier feat |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/392` | 0.698241 | Skill feat, soldier feat |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/424` | 0.698241 | Skill feat, soldier feat |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/400` | 0.698241 | Skill feat, soldier feat |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/396` | 0.698241 | Skill feat, soldier feat |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/416` | 0.698241 | Skill feat, soldier feat |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/412` | 0.698241 | Skill feat, soldier feat |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/420` | 0.698241 | Skill feat, soldier feat |

### Query 96
- Text: What is the rule about In addition to what you get from your class at 1st level, you  have four free boosts to different attribute modifiers.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/2/Text/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/2/Text/4', 'PZO22001 Starfinder Player Core 150-161::/page/2/Text/5', 'PZO22001 Starfinder Player Core 150-161::/page/1/Text/8']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/2/Text/4', 'PZO22001 Starfinder Player Core 150-161::/page/2/SectionHeader/3', 'PZO22001 Starfinder Player Core 150-161::/page/2/Text/5']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/2/SectionHeader/3` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/2/Text/5` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/2/Text/4` | 0.943824 | In addition to what you get from your class at 1st level, you  have four free boosts to different attribute modifiers. |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/2/Text/5` | 0.843002 | At 5th level and every 5 levels thereafter, you get four free  boosts to different attribute modifiers. If an attribute modifier  is already +4 or higher, it takes two boosts to increase it; you  get |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/8` | 0.664077 | At 1st level, your class gives you  an attribute boost to Constitution. |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/28` | 0.537800 | You gain these abilities as a soldier. Abilities gained at higher levels list the level at  which you gain them next to the features' names. |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/30` | 0.530456 | In addition to what you get from your class at 1st level, you have the benefits of  your selected ancestry and background, as described in Chapter 2. |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/11` | 0.505161 | You increase your maximum number  of HP by this number at 1st level and  every level thereafter. |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/408` | 0.492840 | Attribute boosts, skill feat, soldier feat |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/428` | 0.492840 | Attribute boosts, skill feat, soldier feat |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/29` | 0.469559 | At 3rd level and every 4 levels thereafter, you gain a general  feat. General feats are listed in Chapter 5. |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/2/Text/7` | 0.468865 | At 1st level, you gain a number of proficiencies that represent  your basic training. These proficiencies are noted at the start  of this class. |

### Query 97
- Text: What is the rule about At 5th level and every 5 levels thereafter, you get four free  boosts to different attribute modifiers. If an attribute modifier  is already +4 or higher, it takes two boosts to increase it; you  get a partial boost and must boost that attribute again at a  later level to increase it by 1.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/2/Text/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/2/Text/5', 'PZO22001 Starfinder Player Core 150-161::/page/2/Text/4', 'PZO22001 Starfinder Player Core 150-161::/page/1/Text/11']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/2/Text/5', 'PZO22001 Starfinder Player Core 150-161::/page/2/SectionHeader/6', 'PZO22001 Starfinder Player Core 150-161::/page/2/Text/4']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/2/SectionHeader/6` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/2/Text/4` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/2/Text/5` | 0.966227 | At 5th level and every 5 levels thereafter, you get four free  boosts to different attribute modifiers. If an attribute modifier  is already +4 or higher, it takes two boosts to increase it; you  get |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/2/Text/4` | 0.768876 | In addition to what you get from your class at 1st level, you  have four free boosts to different attribute modifiers. |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/11` | 0.601486 | You increase your maximum number  of HP by this number at 1st level and  every level thereafter. |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/35` | 0.540230 | At 3rd level and every 2 levels thereafter, you gain a skill  increase. You can use this increase either to increase your  proficiency rank to trained in one skill you're untrained in, or  to increase |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/36` | 0.514247 | At 7th level, you can use skill increases to increase your  proficiency rank to master in a skill in which you're already  an expert, and at 15th level, you can use them to increase your  proficiency |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/39` | 0.508997 | In addition to the initial ancestry feat you started with, you  gain an ancestry feat at 5th level and every 4 levels thereafter.  The list of ancestry feats available to you can be found in your  anc |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/28` | 0.506714 | You gain these abilities as a soldier. Abilities gained at higher levels list the level at  which you gain them next to the features' names. |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/1` | 0.505033 | circumstance bonus to damage. This bonus increases to +6 at  11th level and +8 at 15th level. |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/29` | 0.502212 | At 3rd level and every 4 levels thereafter, you gain a general  feat. General feats are listed in Chapter 5. |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/8` | 0.494473 | At 1st level, your class gives you  an attribute boost to Constitution. |

### Query 98
- Text: What is the rule about You have a knack for using powerful weapons to harry your  foes and hinder their movement, preventing them from  operating at their peak. If you make an attack with a weapon  that has the area trait (such as from the Area Fire or Auto-Fire  actions), you use it in a manner that suppresses your targets.  Enemies in the affected area who fail their save against your  attack become suppressed (page 440) until the start of your?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/2/Text/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/2/Text/9', 'PZO22001 Starfinder Player Core 150-161::/page/10/Text/23', 'PZO22001 Starfinder Player Core 150-161::/page/3/Text/4']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/2/Text/9', 'PZO22001 Starfinder Player Core 150-161::/page/2/Text/10', 'PZO22001 Starfinder Player Core 150-161::/page/2/SectionHeader/8']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/2/Text/10` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/2/SectionHeader/8` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/2/Text/9` | 0.997051 | You have a knack for using powerful weapons to harry your  foes and hinder their movement, preventing them from  operating at their peak. If you make an attack with a weapon  that has the area trait ( |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/10/Text/23` | 0.739098 | You hold down the trigger and continue blasting. You Area  Fire or Auto-Fire, ignoring your weapon's unwieldy trait.  You don't designate a primary target with this attack,  and creatures you damage w |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/4` | 0.729245 | When you attack with an area weapon, you can select a  number of allies within the area equal to half your Constitution  modifier. The selected allies are unaffected by the attack. In  addition, enemi |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/44` | 0.664544 | You fire your weapon in sustained bursts to unleash a consistent  deluge of firepower that tears apart the terrain to become  treacherous. Make an Area Fire or Auto-Fire attack with your  weapon. Unti |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/10/Text/27` | 0.644072 | You use your weapon to help corral panicked enemies. An  enemy who critically fails a save against your Area Fire or  Auto-Fire is fleeing for 1 round. |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/6/Text/5` | 0.626366 | **Suppressed:** Suppressed is a condition often  applied by the soldier when using area and automatic  weapons against targets. Creatures a soldier  suppresses might receive additional conditions and |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/32` | 0.617951 | You compel enemies to avoid your attacks by aiming at their  legs, wings, or other forms of movement to make them easier  to outmaneuver. When you suppress a target with one of your  attacks, it also |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/6/Text/3` | 0.614057 | **Area Fire:** This is a special action usually made with  weapons that have the area trait. This type of action  is used to launch weapons that affect a wide area,  such as a burst, cone, or line. Se |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/2/Text/12` | 0.614046 | You can focus fire on a single target when unleashing the  full devastation of your powerful area weaponry. Before you  make an area attack with a weapon (such as from the Area  Fire or Auto-Fire acti |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/10/Text/37` | 0.605786 | **Requirements** You're wielding an area or automatic weapon. Your weapon blasts apart the battlefield and leaves it  a ruinous waste. You Area Fire or Auto-Fire. You don't  designate a primary target |

### Query 99
- Text: What is the rule about next turn. A suppressed target takes a –1 circumstance penalty  on attack rolls and takes a –10-foot status penalty to its Speeds.  Some soldier abilities and class feats interact further with the  suppressed condition.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/2/Text/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/2/Text/10', 'PZO22001 Starfinder Player Core 150-161::/page/9/Text/16', 'PZO22001 Starfinder Player Core 150-161::/page/6/Text/5']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/2/Text/10', 'PZO22001 Starfinder Player Core 150-161::/page/2/Text/9', 'PZO22001 Starfinder Player Core 150-161::/page/2/SectionHeader/11']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/2/Text/9` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/2/SectionHeader/11` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/2/Text/10` | 0.984502 | next turn. A suppressed target takes a –1 circumstance penalty  on attack rolls and takes a –10-foot status penalty to its Speeds.  Some soldier abilities and class feats interact further with the  su |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/16` | 0.756320 | Your suppressing attacks pin foes in place, preventing  them from moving at more than a crawling pace. When you  suppress a target with one of your attacks, increase the  speed penalty to a –20-foot s |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/6/Text/5` | 0.696790 | **Suppressed:** Suppressed is a condition often  applied by the soldier when using area and automatic  weapons against targets. Creatures a soldier  suppresses might receive additional conditions and |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/6/Text/29` | 0.645292 | You overwhelm the defenses of suppressed foes. Your  multiple attack penalty for attacks against suppressed  targets is –4 (–3 with an agile weapon) on your second  attack of the turn instead of –5, a |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/15` | 0.578117 | other offensive action, it loses the suppressed condition from  this effect. |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/14` | 0.572059 | You unnerve foes with a look, or similarly unsettle them with  subtle mannerisms or veiled threats. One enemy creature of  your choice within 60 feet becomes suppressed until the start  of your next t |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/2/Text/9` | 0.547106 | You have a knack for using powerful weapons to harry your  foes and hinder their movement, preventing them from  operating at their peak. If you make an attack with a weapon  that has the area trait ( |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/11/Text/1` | 0.540666 | soldier class feat you have that grants a reaction. At the  start of your turn, you gain an additional reaction that you  can only use for the selected class feat or an action granted  by the selected |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/7/Text/8` | 0.527562 | You make a well placed shot or unleash a hail of fire to cover  your allies. Make a ranged Strike against a target and select  one ally within range of the same attack. If your Strike hits  your targe |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/1` | 0.524366 | When you successfully Disarm, Grapple, Reposition, Shove, or  Trip a creature, it becomes suppressed until the start of your  next turn. |

### Query 100
- Text: What is the rule about You can focus fire on a single target when unleashing the  full devastation of your powerful area weaponry. Before you  make an area attack with a weapon (such as from the Area  Fire or Auto-Fire actions), you can make a ranged Strike as a  free action with the same weapon against a single creature  in the area, who's selected as your primary target. If your  attack is a burst, you must select the creature closest to the  center of the attack. If your attack is a cone or line, you must  select the creature closest to you. If two or more creatures are  equidistant, you can choose which one is your primary target.  On a hit, if your primary target rolls a success against your  Area Fire or Auto-Fire action, they get a failure instead. This  Strike doesn't count toward your multiple attack penalty.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/2/Text/12']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/2/Text/12', 'PZO22001 Starfinder Player Core 150-161::/page/2/Text/17', 'PZO22001 Starfinder Player Core 150-161::/page/7/Text/8']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/2/Text/12', 'PZO22001 Starfinder Player Core 150-161::/page/2/SectionHeader/13', 'PZO22001 Starfinder Player Core 150-161::/page/2/SectionHeader/11']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/2/SectionHeader/13` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/2/SectionHeader/11` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/2/Text/12` | 0.994731 | You can focus fire on a single target when unleashing the  full devastation of your powerful area weaponry. Before you  make an area attack with a weapon (such as from the Area  Fire or Auto-Fire acti |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/2/Text/17` | 0.774477 | When you successfully make a ranged Strike with an  automatic weapon, you suppress the target until the start of  your next turn. In addition, when you Auto-Fire, the size of  the cone is equal to the |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/7/Text/8` | 0.766492 | You make a well placed shot or unleash a hail of fire to cover  your allies. Make a ranged Strike against a target and select  one ally within range of the same attack. If your Strike hits  your targe |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/5` | 0.713188 | You concentrate fire on a specific target operating within  your weapon's threat range. Make a ranged Strike against the  triggering creature, ignoring the unwieldy trait of weapons you  wield for thi |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/6/Text/34` | 0.710983 | You know unleashing a barrage of gunfire can bring most  enemies low. You make a follow-up Strike against your  primary target using the same weapon. Ignore the unwieldy  trait on your weapon when usi |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/5/Text/42` | 0.698660 | You swipe your weapon in a wide swing to create a deadly  arc. Your weapon gains the area (burst 5 feet) and unwieldy  traits until the end of the turn. If your weapon has reach, the  burst radius bec |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/27` | 0.688800 | You fight on to the absolute last, pushing yourself to make  one final attack at a foe. Make a Strike with a –2 circumstance  penalty, or make an Area Fire or Auto-Fire attack ignoring the |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/10/Text/23` | 0.676337 | You hold down the trigger and continue blasting. You Area  Fire or Auto-Fire, ignoring your weapon's unwieldy trait.  You don't designate a primary target with this attack,  and creatures you damage w |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/11/Text/20` | 0.668109 | Your destructive power has become second nature as  enemies stand in awe of your overwhelming firepower. You  can use the Area Fire or Auto-Fire attacks as a single action.  However, you can never mak |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/8/Text/17` | 0.657579 | You overcharge a shield to create a concussive blast that  repulses nearby foes. You Area Fire using your force field or  shield, dealing 2d10 bludgeoning damage in a 5-foot radius  burst centered on |

### Query 101
- Text: What are the requirements for **BURST OF STRENGTH **[reaction] **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/5/SectionHeader/18']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/5/SectionHeader/18', 'PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/565', 'PZO22001 Starfinder Player Core 150-161::/page/9/SectionHeader/17']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/5/SectionHeader/18', 'PZO22001 Starfinder Player Core 150-161::/page/5/Text/19', 'PZO22001 Starfinder Player Core 150-161::/page/5/SectionHeader/17']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/5/Text/19` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/5/SectionHeader/17` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/5/SectionHeader/18` | 0.888184 | **BURST OF STRENGTH **[reaction] **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/565` | 0.656880 | Burst of Strength |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/9/SectionHeader/17` | 0.511587 | **BRUTAL BARRAGE **[one-action] **FEAT 10** |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/10/Text/14` | 0.461094 | **Requirements** You're wielding an area (burst) weapon. |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/8/SectionHeader/19` | 0.460023 | **PUNITIVE STRIKE **[reaction] **FEAT 6** |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/5/Text/57` | 0.425361 | **SKILLS** **FEATS** |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/7/Text/38` | 0.425361 | **SKILLS** **FEATS** |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/49` | 0.425361 | **SKILLS** **FEATS** |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/5/SectionHeader/23` | 0.423751 | **PIN DOWN **[reaction] **FEAT 1** |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/9/SectionHeader/22` | 0.416964 | **COME GET SOME! **[reaction] **FEAT 10** |

### Query 102
- Text: What are the requirements for **PIN DOWN **[reaction] **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/5/SectionHeader/23']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/5/SectionHeader/23', 'PZO22001 Starfinder Player Core 150-161::/page/8/Text/11', 'PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/12']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/5/SectionHeader/23', 'PZO22001 Starfinder Player Core 150-161::/page/5/Text/22', 'PZO22001 Starfinder Player Core 150-161::/page/5/Text/25']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/5/Text/22` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/5/Text/25` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/5/SectionHeader/23` | 0.859480 | **PIN DOWN **[reaction] **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/8/Text/11` | 0.524498 | Pin Down (1st), Shot on the Run (2nd), Covering Fire  (6th), Terror-Forming (14th) |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/12` | 0.523975 | **SHOT ON THE RUN **[two-actions] **FEAT 2** |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/611` | 0.467076 | Pin Down |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/8/SectionHeader/30` | 0.459397 | **BRING IT ON! **[one-action] **FEAT 8** |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/9/SectionHeader/22` | 0.451168 | **COME GET SOME! **[reaction] **FEAT 10** |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/5/SectionHeader/33` | 0.450752 | **READY RELOAD **[one-action] **FEAT 1** |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/5/SectionHeader/28` | 0.439556 | **QUICK SWAP **[reaction] **FEAT 1** |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/2` | 0.438024 | **OVERWATCH **[reaction] **FEAT 8** |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/6` | 0.430924 | **RUN HOT **[three-actions] **FEAT 8** |

### Query 103
- Text: What are the requirements for **QUICK SWAP **[reaction] **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/5/SectionHeader/28']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/5/SectionHeader/28', 'PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/617', 'PZO22001 Starfinder Player Core 150-161::/page/10/Text/31']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/5/SectionHeader/28', 'PZO22001 Starfinder Player Core 150-161::/page/5/Text/30', 'PZO22001 Starfinder Player Core 150-161::/page/5/Text/27']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/5/Text/30` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/5/Text/27` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/5/SectionHeader/28` | 0.889842 | **QUICK SWAP **[reaction] **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/617` | 0.623426 | Quick Swap |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/10/Text/31` | 0.544360 | **Prerequisites** Shoving Shot |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/10/Text/4` | 0.502360 | **Prerequisites** Shoving Shot |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/35` | 0.472689 | **SHOVING SHOT **[two-actions] **FEAT 4** |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/11/Text/2` | 0.454266 | You can change the reaction selected for this feat when  you make your daily preparations as long as the new feat  meets the requirements. |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/5/SectionHeader/23` | 0.446543 | **PIN DOWN **[reaction] **FEAT 1** |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/5/SectionHeader/38` | 0.434740 | **WHIRLING SWIPE **[two-actions] **FEAT 1** |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/5/SectionHeader/18` | 0.417241 | **BURST OF STRENGTH **[reaction] **FEAT 1** |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/5/SectionHeader/33` | 0.415693 | **READY RELOAD **[one-action] **FEAT 1** |

### Query 104
- Text: What are the requirements for **READY RELOAD **[one-action] **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/5/SectionHeader/33']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/5/SectionHeader/33', 'PZO22001 Starfinder Player Core 150-161::/page/8/SectionHeader/30', 'PZO22001 Starfinder Player Core 150-161::/page/7/SectionHeader/5']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/5/SectionHeader/33', 'PZO22001 Starfinder Player Core 150-161::/page/5/Text/35', 'PZO22001 Starfinder Player Core 150-161::/page/5/Text/32']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/5/Text/35` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/5/Text/32` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/5/SectionHeader/33` | 0.897079 | **READY RELOAD **[one-action] **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/8/SectionHeader/30` | 0.551672 | **BRING IT ON! **[one-action] **FEAT 8** |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/7/SectionHeader/5` | 0.513335 | **COVERING FIRE **[one-action]** OR **[two-actions] **FEAT 6** |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/41` | 0.439682 | **WIDEN AREA **[one-action] **FEAT 4** |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/11/Text/7` | 0.422961 | **Requirements** You're wielding an area or automatic weapon. With a mighty bellow, you unload your weapon to give  your allies the cover they need to rally. You Area Fire  or Auto-Fire without select |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/5/SectionHeader/44` | 0.422495 | **MENACING LAUGHTER **[one-action] **FEAT 2** |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/619` | 0.403825 | Ready Reload |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/30` | 0.400757 | **PUNISHING SALVO **[one-action] **FEAT 4** |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/6` | 0.399891 | **RUN HOT **[three-actions] **FEAT 8** |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/6` | 0.399479 | **RELENTLESS ENDURANCE **[reaction] **FEAT 2** |

### Query 105
- Text: What are the requirements for **WHIRLING SWIPE **[two-actions] **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/5/SectionHeader/38']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/5/SectionHeader/38', 'PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/645', 'PZO22001 Starfinder Player Core 150-161::/page/3/Text/7']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/5/SectionHeader/38', 'PZO22001 Starfinder Player Core 150-161::/page/5/Text/37', 'PZO22001 Starfinder Player Core 150-161::/page/5/Text/40']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/5/Text/37` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/5/Text/40` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/5/SectionHeader/38` | 0.928105 | **WHIRLING SWIPE **[two-actions] **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/645` | 0.664050 | Whirling Swipe |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/7` | 0.560230 | As long as you're wielding a two-handed melee weapon, you  meet the requirements for soldier feats that require an area  weapon. When you're using a soldier feat, any two-handed  melee weapon you're w |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/11/SectionHeader/21` | 0.495325 | **HYBRID TECHNIQUE **[two-actions] **FEAT 20** |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/16` | 0.494709 | **YOU'LL HAVE TO GO THROUGH ME! **[two-actions] **FEAT 2** |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/35` | 0.486190 | **SHOVING SHOT **[two-actions] **FEAT 4** |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/7/SectionHeader/5` | 0.475905 | **COVERING FIRE **[one-action]** OR **[two-actions] **FEAT 6** |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/6/Text/44` | 0.459534 | **Requirements** You're wielding an area or automatic weapon. You set up your area weapon to affect more targets. If the  next action you use is to Area Fire or Auto-Fire in a burst,  cone, or line, o |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/12` | 0.454079 | **SHOT ON THE RUN **[two-actions] **FEAT 2** |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/5/Text/41` | 0.446737 | **Requirements** You're wielding a two-handed melee  weapon. |

### Query 106
- Text: What are the requirements for **MENACING LAUGHTER **[one-action] **FEAT 2**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/5/SectionHeader/44']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/5/SectionHeader/44', 'PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/16', 'PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/599']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/5/SectionHeader/44', 'PZO22001 Starfinder Player Core 150-161::/page/5/Text/46', 'PZO22001 Starfinder Player Core 150-161::/page/5/SectionHeader/43']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/5/Text/46` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/5/SectionHeader/43` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/5/SectionHeader/44` | 0.881520 | **MENACING LAUGHTER **[one-action] **FEAT 2** |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/16` | 0.539366 | **YOU'LL HAVE TO GO THROUGH ME! **[two-actions] **FEAT 2** |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/599` | 0.535366 | Menacing Laughter |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/7/SectionHeader/5` | 0.462547 | **COVERING FIRE **[one-action]** OR **[two-actions] **FEAT 6** |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/7/SectionHeader/21` | 0.459819 | **INTIMIDATING TAUNT **[one-action] **FEAT 6** |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/8/SectionHeader/30` | 0.453383 | **BRING IT ON! **[one-action] **FEAT 8** |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/5/SectionHeader/33` | 0.440709 | **READY RELOAD **[one-action] **FEAT 1** |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/34` | 0.439781 | **TERROR-FORMING **[two-actions] **FEAT 14** |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/11` | 0.430261 | **ROCKET JUMP **[two-actions] **FEAT 12** |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/12` | 0.427683 | **SHOT ON THE RUN **[two-actions] **FEAT 2** |

### Query 107
- Text: What are the requirements for **RELENTLESS ENDURANCE **[reaction] **FEAT 2**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/6', 'PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/621', 'PZO22001 Starfinder Player Core 150-161::/page/9/Text/48']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/6', 'PZO22001 Starfinder Player Core 150-161::/page/6/Text/5', 'PZO22001 Starfinder Player Core 150-161::/page/6/Text/8']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/6/Text/5` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/6/Text/8` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/6` | 0.880977 | **RELENTLESS ENDURANCE **[reaction] **FEAT 2** |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/621` | 0.593149 | Relentless Endurance |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/48` | 0.490731 | **Prerequisites** Run Hot |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/12` | 0.439945 | **SHOT ON THE RUN **[two-actions] **FEAT 2** |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/49` | 0.433005 | **SKILLS** **FEATS** |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/7/Text/38` | 0.433005 | **SKILLS** **FEATS** |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/5/Text/57` | 0.433005 | **SKILLS** **FEATS** |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/5/SectionHeader/33` | 0.428453 | **READY RELOAD **[one-action] **FEAT 1** |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/5/SectionHeader/23` | 0.409537 | **PIN DOWN **[reaction] **FEAT 1** |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/8/Text/16` | 0.407916 | **Requirements** You have a force field upgrade in your armor or  are holding a tech shield. |

### Query 108
- Text: What are the requirements for **SHOT ON THE RUN **[two-actions] **FEAT 2**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/12']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/12', 'PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/35', 'PZO22001 Starfinder Player Core 150-161::/page/9/Text/6']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/12', 'PZO22001 Starfinder Player Core 150-161::/page/6/Text/11', 'PZO22001 Starfinder Player Core 150-161::/page/6/Text/14']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/6/Text/11` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/6/Text/14` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/12` | 0.913308 | **SHOT ON THE RUN **[two-actions] **FEAT 2** |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/35` | 0.659793 | **SHOVING SHOT **[two-actions] **FEAT 4** |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/6` | 0.635469 | **RUN HOT **[three-actions] **FEAT 8** |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/633` | 0.569992 | Shot on the Run |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/16` | 0.567386 | **YOU'LL HAVE TO GO THROUGH ME! **[two-actions] **FEAT 2** |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/10/Text/31` | 0.551994 | **Prerequisites** Shoving Shot |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/10/Text/4` | 0.551994 | **Prerequisites** Shoving Shot |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/8/SectionHeader/35` | 0.541863 | **CONCENTRATED SHOT **[two-actions] **FEAT 8** |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/48` | 0.530927 | **Prerequisites** Run Hot |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/28` | 0.504931 | **SCATTERING FIRE **[two-actions] **FEAT 14** |

### Query 109
- Text: What are the requirements for **YOU'LL HAVE TO GO THROUGH ME! **[two-actions] **FEAT 2**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/16']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/16', 'PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/649', 'PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/12']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/16', 'PZO22001 Starfinder Player Core 150-161::/page/6/Text/15', 'PZO22001 Starfinder Player Core 150-161::/page/6/Text/17']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/6/Text/15` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/6/Text/17` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/16` | 0.929228 | **YOU'LL HAVE TO GO THROUGH ME! **[two-actions] **FEAT 2** |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/649` | 0.643356 | You'll Have To Go Through Me! |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/12` | 0.553328 | **SHOT ON THE RUN **[two-actions] **FEAT 2** |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/7/SectionHeader/5` | 0.466373 | **COVERING FIRE **[one-action]** OR **[two-actions] **FEAT 6** |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/35` | 0.459567 | **SHOVING SHOT **[two-actions] **FEAT 4** |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/11/SectionHeader/21` | 0.458130 | **HYBRID TECHNIQUE **[two-actions] **FEAT 20** |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/11` | 0.455875 | **ROCKET JUMP **[two-actions] **FEAT 12** |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/7/SectionHeader/15` | 0.454571 | **I'LL BE BACK **[free-action] **FEAT 6** |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/5/Text/41` | 0.450394 | **Requirements** You're wielding a two-handed melee  weapon. |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/8/Text/33` | 0.449194 | **Requirements** You're wielding a two-handed  weapon. |

### Query 110
- Text: What are the requirements for **COLLATERAL WITNESS **[reaction] **FEAT 4**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/21']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/21', 'PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/38', 'PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/35']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/21', 'PZO22001 Starfinder Player Core 150-161::/page/6/Text/23', 'PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/20']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/6/Text/23` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/20` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/21` | 0.915314 | **COLLATERAL WITNESS **[reaction] **FEAT 4** |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/38` | 0.449506 | **VECTOR REFLECTOR **[reaction] **FEAT 14** |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/35` | 0.443222 | **SHOVING SHOT **[two-actions] **FEAT 4** |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/6` | 0.394033 | **RELENTLESS ENDURANCE **[reaction] **FEAT 2** |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/5/Text/57` | 0.392916 | **SKILLS** **FEATS** |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/7/Text/38` | 0.392916 | **SKILLS** **FEATS** |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/49` | 0.392916 | **SKILLS** **FEATS** |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/567` | 0.391902 | Collateral Witness |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/41` | 0.389766 | **WIDEN AREA **[one-action] **FEAT 4** |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/26` | 0.384968 | **OVERWHELMING ASSAULT** **FEAT 4** |

### Query 111
- Text: What are the requirements for **OVERWHELMING ASSAULT** **FEAT 4**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/26']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/26', 'PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/609', 'PZO22001 Starfinder Player Core 150-161::/page/9/Text/2']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/26', 'PZO22001 Starfinder Player Core 150-161::/page/6/Text/28', 'PZO22001 Starfinder Player Core 150-161::/page/6/Text/25']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/6/Text/28` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/6/Text/25` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/26` | 0.870005 | **OVERWHELMING ASSAULT** **FEAT 4** |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/609` | 0.571260 | Overwhelming Assault |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/2` | 0.530911 | **OVERWATCH **[reaction] **FEAT 8** |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/47` | 0.472466 | **OVERKILL** **FEAT 16** |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/35` | 0.471092 | **SHOVING SHOT **[two-actions] **FEAT 4** |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/7/Table/14` | 0.442058 | FeatLevelOffensive Defense6Overkill16Overwatch8Overwhelming Assault4Pin Down1Punishing Salvo4Punitive Strike6Quick Swap1Ready Reload1Relentless Endurance2Rocket Jump12Run Hot8Run, Cowards!14Scattering |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/30` | 0.422614 | **PUNISHING SALVO **[one-action] **FEAT 4** |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/41` | 0.416301 | **WIDEN AREA **[one-action] **FEAT 4** |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/49` | 0.392605 | **SKILLS** **FEATS** |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/5/Text/57` | 0.392605 | **SKILLS** **FEATS** |

### Query 112
- Text: What are the requirements for **PUNISHING SALVO **[one-action] **FEAT 4**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/30']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/30', 'PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/613', 'PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/35']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/30', 'PZO22001 Starfinder Player Core 150-161::/page/6/Text/32', 'PZO22001 Starfinder Player Core 150-161::/page/6/Text/29']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/6/Text/32` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/6/Text/29` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/30` | 0.904282 | **PUNISHING SALVO **[one-action] **FEAT 4** |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/613` | 0.612576 | Punishing Salvo |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/35` | 0.566937 | **SHOVING SHOT **[two-actions] **FEAT 4** |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/41` | 0.469104 | **WIDEN AREA **[one-action] **FEAT 4** |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/7/SectionHeader/5` | 0.438680 | **COVERING FIRE **[one-action]** OR **[two-actions] **FEAT 6** |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/7/Table/14` | 0.433688 | FeatLevelOffensive Defense6Overkill16Overwatch8Overwhelming Assault4Pin Down1Punishing Salvo4Punitive Strike6Quick Swap1Ready Reload1Relentless Endurance2Rocket Jump12Run Hot8Run, Cowards!14Scattering |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/5/SectionHeader/44` | 0.431471 | **MENACING LAUGHTER **[one-action] **FEAT 2** |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/8/SectionHeader/30` | 0.430267 | **BRING IT ON! **[one-action] **FEAT 8** |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/7/SectionHeader/21` | 0.421893 | **INTIMIDATING TAUNT **[one-action] **FEAT 6** |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/26` | 0.418623 | **OVERWHELMING ASSAULT** **FEAT 4** |

### Query 113
- Text: What are the requirements for **SHOVING SHOT **[two-actions] **FEAT 4**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/35']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/35', 'PZO22001 Starfinder Player Core 150-161::/page/10/Text/4', 'PZO22001 Starfinder Player Core 150-161::/page/10/Text/31']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/35', 'PZO22001 Starfinder Player Core 150-161::/page/6/Text/34', 'PZO22001 Starfinder Player Core 150-161::/page/6/Text/37']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/6/Text/34` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/6/Text/37` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/35` | 0.890403 | **SHOVING SHOT **[two-actions] **FEAT 4** |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/10/Text/4` | 0.706098 | **Prerequisites** Shoving Shot |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/10/Text/31` | 0.706098 | **Prerequisites** Shoving Shot |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/12` | 0.605667 | **SHOT ON THE RUN **[two-actions] **FEAT 2** |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/635` | 0.536413 | Shoving Shot |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/16` | 0.519331 | **YOU'LL HAVE TO GO THROUGH ME! **[two-actions] **FEAT 2** |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/8/SectionHeader/35` | 0.518103 | **CONCENTRATED SHOT **[two-actions] **FEAT 8** |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/30` | 0.504755 | **PUNISHING SALVO **[one-action] **FEAT 4** |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/6` | 0.490481 | **RUN HOT **[three-actions] **FEAT 8** |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/7/SectionHeader/5` | 0.479450 | **COVERING FIRE **[one-action]** OR **[two-actions] **FEAT 6** |

### Query 114
- Text: What are the requirements for **WIDEN AREA **[one-action] **FEAT 4**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/41']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/41', 'PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/35', 'PZO22001 Starfinder Player Core 150-161::/page/8/SectionHeader/30']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/41', 'PZO22001 Starfinder Player Core 150-161::/page/6/Text/40', 'PZO22001 Starfinder Player Core 150-161::/page/6/Text/43']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/6/Text/40` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/6/Text/43` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/41` | 0.899822 | **WIDEN AREA **[one-action] **FEAT 4** |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/35` | 0.535061 | **SHOVING SHOT **[two-actions] **FEAT 4** |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/8/SectionHeader/30` | 0.530476 | **BRING IT ON! **[one-action] **FEAT 8** |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/9` | 0.482127 | **Requirements** You're wielding an area weapon. |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/30` | 0.482086 | **PUNISHING SALVO **[one-action] **FEAT 4** |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/7/SectionHeader/5` | 0.480971 | **COVERING FIRE **[one-action]** OR **[two-actions] **FEAT 6** |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/5/SectionHeader/33` | 0.478417 | **READY RELOAD **[one-action] **FEAT 1** |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/20` | 0.456867 | **Requirements** You're wielding an area or automatic weapon. |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/11/Text/24` | 0.455869 | **Requirements** You're wielding an area or automatic weapon. You can combine methods into a deadly new hybrid  technique. Choose two soldier feats that take 2 actions to  use, require you to wield an |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/6/Text/33` | 0.453825 | **Requirements** Your last action this turn was an Area Fire  attack. |

### Query 115
- Text: Lookup values for FeatLevelAmmo Hoarder8Anchoring Impacts10Bring It On!8Brutal Barrage10Bullet Hell12Bullet Typhoon20Burst of Strength1Collateral Witness4Come Get Some!10Concentrated Shot8Coordinated Fire18Covering Fire6Damoritosh's Grip18Dance!10Death Blossom12Fan the Hammer14Fog of War6Hammer the Nail12Hybrid Technique20I'll Be Back6Intimidating Taunt6Light 'Em Up16Load-Bearing Hero12Menacing Laughter2
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/7/Table/3']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/7/Table/3', 'PZO22001 Starfinder Player Core 150-161::/page/7/Table/14', 'PZO22001 Starfinder Player Core 150-161::/page/2/Table/2']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/7/Table/3', 'PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/551', 'PZO22001 Starfinder Player Core 150-161::/page/7/Text/2']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/551` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/7/Text/2` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/7/Table/3` | 0.995649 | FeatLevelAmmo Hoarder8Anchoring Impacts10Bring It On!8Brutal Barrage10Bullet Hell12Bullet Typhoon20Burst of Strength1Collateral Witness4Come Get Some!10Concentrated Shot8Coordinated Fire18Covering Fir |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/7/Table/14` | 0.711351 | FeatLevelOffensive Defense6Overkill16Overwatch8Overwhelming Assault4Pin Down1Punishing Salvo4Punitive Strike6Quick Swap1Ready Reload1Relentless Endurance2Rocket Jump12Run Hot8Run, Cowards!14Scattering |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/2/Table/2` | 0.629963 | Your LevelClass Features1Ancestry and background, attribute boosts, initial proficiencies, suppressing fire, primary target, soldier fighting style, walking armory, soldier feat2Skill feat, soldier fe |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/7/Text/2` | 0.523831 | Use this table to look up soldier feats by name. |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/8/SectionHeader/25` | 0.509528 | **AMMO HOARDER** **FEAT 8** |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/29` | 0.478352 | At 3rd level and every 4 levels thereafter, you gain a general  feat. General feats are listed in Chapter 5. |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/10/Text/41` | 0.459786 | **Trigger** A suppressed creature damages you with a Strike. Your armor absorbs some of the kinetic energy of your  opponent's attack. You gain resistance equal to half your  level against the trigger |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/28` | 0.443231 | You gain these abilities as a soldier. Abilities gained at higher levels list the level at  which you gain them next to the features' names. |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/23` | 0.438774 | At 2nd level and every 2 levels thereafter, you gain a skill feat.  Skill feats can be found in Chapter 5 and have the skill trait.  You must be trained or better in the corresponding skill to  select |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/10/Text/5` | 0.438429 | You adjust the angle of your barrage to maximize the  ammunition's impact on creatures' bodies. Increase the  distance creatures are pushed by your Shoving Shot to 5  feet on a success, 10 feet on a f |

### Query 116
- Text: What are the requirements for **COVERING FIRE **[one-action]** OR **[two-actions] **FEAT 6**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/7/SectionHeader/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/7/SectionHeader/5', 'PZO22001 Starfinder Player Core 150-161::/page/7/SectionHeader/10', 'PZO22001 Starfinder Player Core 150-161::/page/8/SectionHeader/13']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/7/SectionHeader/5', 'PZO22001 Starfinder Player Core 150-161::/page/7/SectionHeader/7', 'PZO22001 Starfinder Player Core 150-161::/page/7/SectionHeader/4']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/7/SectionHeader/7` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/7/SectionHeader/4` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/7/SectionHeader/5` | 0.958324 | **COVERING FIRE **[one-action]** OR **[two-actions] **FEAT 6** |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/7/SectionHeader/10` | 0.651930 | **FOG OF WAR **[two-actions] **FEAT 6** |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/8/SectionHeader/13` | 0.640481 | **OFFENSIVE DEFENSE **[two-actions] **FEAT 6** |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/7/Text/9` | 0.604326 | You can use Covering Fire as a 2-action activity to Area  Fire or Auto-Fire instead of making a ranged Strike, affecting  targets that fail their save. |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/11/SectionHeader/4` | 0.569507 | **COORDINATED FIRE **[three-actions] **FEAT 18** |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/28` | 0.556696 | **SCATTERING FIRE **[two-actions] **FEAT 14** |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/575` | 0.552405 | Covering Fire |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/15` | 0.545085 | **Prerequisites** suppressing fire |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/31` | 0.545085 | **Prerequisites** suppressing fire |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/11/Text/7` | 0.509179 | **Requirements** You're wielding an area or automatic weapon. With a mighty bellow, you unload your weapon to give  your allies the cover they need to rally. You Area Fire  or Auto-Fire without select |

### Query 117
- Text: What are the requirements for **FOG OF WAR **[two-actions] **FEAT 6**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/7/SectionHeader/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/7/SectionHeader/10', 'PZO22001 Starfinder Player Core 150-161::/page/8/SectionHeader/13', 'PZO22001 Starfinder Player Core 150-161::/page/7/SectionHeader/5']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/7/SectionHeader/10', 'PZO22001 Starfinder Player Core 150-161::/page/7/Text/9', 'PZO22001 Starfinder Player Core 150-161::/page/7/SectionHeader/12']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/7/Text/9` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/7/SectionHeader/12` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/7/SectionHeader/10` | 0.894410 | **FOG OF WAR **[two-actions] **FEAT 6** |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/8/SectionHeader/13` | 0.656725 | **OFFENSIVE DEFENSE **[two-actions] **FEAT 6** |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/7/SectionHeader/5` | 0.636628 | **COVERING FIRE **[one-action]** OR **[two-actions] **FEAT 6** |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/585` | 0.535031 | Fog of War |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/16` | 0.498363 | **YOU'LL HAVE TO GO THROUGH ME! **[two-actions] **FEAT 2** |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/7/SectionHeader/15` | 0.471822 | **I'LL BE BACK **[free-action] **FEAT 6** |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/34` | 0.462745 | **TERROR-FORMING **[two-actions] **FEAT 14** |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/12` | 0.461912 | **SHOT ON THE RUN **[two-actions] **FEAT 2** |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/7/SectionHeader/21` | 0.454379 | **INTIMIDATING TAUNT **[one-action] **FEAT 6** |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/28` | 0.452995 | **SCATTERING FIRE **[two-actions] **FEAT 14** |

### Query 118
- Text: Lookup values for FeatLevelOffensive Defense6Overkill16Overwatch8Overwhelming Assault4Pin Down1Punishing Salvo4Punitive Strike6Quick Swap1Ready Reload1Relentless Endurance2Rocket Jump12Run Hot8Run, Cowards!14Scattering Fire14Shell Shower10Shot on the Run2Shoving Shot4Soldier's Training16Spread the Love18Terror-Forming14Vector Reflector14Whirling Swipe1Widen Area4You'll Have To Go Through Me!2
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/7/Table/14']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/7/Table/14', 'PZO22001 Starfinder Player Core 150-161::/page/7/Table/3', 'PZO22001 Starfinder Player Core 150-161::/page/2/Table/2']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/7/Table/14', 'PZO22001 Starfinder Player Core 150-161::/page/7/Text/13', 'PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/601']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/7/Text/13` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/601` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/7/Table/14` | 1.005180 | FeatLevelOffensive Defense6Overkill16Overwatch8Overwhelming Assault4Pin Down1Punishing Salvo4Punitive Strike6Quick Swap1Ready Reload1Relentless Endurance2Rocket Jump12Run Hot8Run, Cowards!14Scattering |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/7/Table/3` | 0.700445 | FeatLevelAmmo Hoarder8Anchoring Impacts10Bring It On!8Brutal Barrage10Bullet Hell12Bullet Typhoon20Burst of Strength1Collateral Witness4Come Get Some!10Concentrated Shot8Coordinated Fire18Covering Fir |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/2/Table/2` | 0.660987 | Your LevelClass Features1Ancestry and background, attribute boosts, initial proficiencies, suppressing fire, primary target, soldier fighting style, walking armory, soldier feat2Skill feat, soldier fe |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/7/Text/2` | 0.548836 | Use this table to look up soldier feats by name. |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/607` | 0.478991 | Overwatch |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/28` | 0.478690 | You gain these abilities as a soldier. Abilities gained at higher levels list the level at  which you gain them next to the features' names. |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/29` | 0.476515 | At 3rd level and every 4 levels thereafter, you gain a general  feat. General feats are listed in Chapter 5. |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/390` | 0.464689 | Ancestry and background, attribute boosts, initial proficiencies, suppressing fire, primary target, soldier fighting style, walking armory, soldier feat |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/5/Text/16` | 0.454366 | At every level that you gain a soldier feat, you can  select one of the following feats. You must satisfy any  prerequisites before selecting the feat. |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/23` | 0.442124 | At 2nd level and every 2 levels thereafter, you gain a skill feat.  Skill feats can be found in Chapter 5 and have the skill trait.  You must be trained or better in the corresponding skill to  select |

### Query 119
- Text: What are the requirements for **I'LL BE BACK **[free-action] **FEAT 6**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/7/SectionHeader/15']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/7/SectionHeader/15', 'PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/16', 'PZO22001 Starfinder Player Core 150-161::/page/7/SectionHeader/10']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/7/SectionHeader/15', 'PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/650', 'PZO22001 Starfinder Player Core 150-161::/page/7/SectionHeader/17']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/650` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/7/SectionHeader/17` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/7/SectionHeader/15` | 0.868117 | **I'LL BE BACK **[free-action] **FEAT 6** |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/16` | 0.576282 | **YOU'LL HAVE TO GO THROUGH ME! **[two-actions] **FEAT 2** |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/7/SectionHeader/10` | 0.545239 | **FOG OF WAR **[two-actions] **FEAT 6** |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/591` | 0.500131 | I'll Be Back |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/7/SectionHeader/5` | 0.492518 | **COVERING FIRE **[one-action]** OR **[two-actions] **FEAT 6** |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/8/SectionHeader/13` | 0.473043 | **OFFENSIVE DEFENSE **[two-actions] **FEAT 6** |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/8/SectionHeader/30` | 0.466235 | **BRING IT ON! **[one-action] **FEAT 8** |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/7/SectionHeader/21` | 0.458806 | **INTIMIDATING TAUNT **[one-action] **FEAT 6** |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/9/SectionHeader/34` | 0.431154 | **SHELL SHOWER **[free-action] **FEAT 10** |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/6` | 0.420594 | **RUN HOT **[three-actions] **FEAT 8** |

### Query 120
- Text: What are the requirements for **INTIMIDATING TAUNT **[one-action] **FEAT 6**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/7/SectionHeader/21']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/7/SectionHeader/21', 'PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/593', 'PZO22001 Starfinder Player Core 150-161::/page/7/SectionHeader/5']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/7/SectionHeader/21', 'PZO22001 Starfinder Player Core 150-161::/page/7/Text/20', 'PZO22001 Starfinder Player Core 150-161::/page/7/SectionHeader/23']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/7/Text/20` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/7/SectionHeader/23` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/7/SectionHeader/21` | 0.909341 | **INTIMIDATING TAUNT **[one-action] **FEAT 6** |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/593` | 0.599526 | Intimidating Taunt |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/7/SectionHeader/5` | 0.543226 | **COVERING FIRE **[one-action]** OR **[two-actions] **FEAT 6** |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/7/SectionHeader/24` | 0.500930 | **Prerequisites** trained in Intimidation |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/8/SectionHeader/30` | 0.487335 | **BRING IT ON! **[one-action] **FEAT 8** |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/7/SectionHeader/10` | 0.487119 | **FOG OF WAR **[two-actions] **FEAT 6** |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/7/Text/25` | 0.484099 | You taunt your enemy mercilessly, forcing them to  acknowledge you as an immediate threat. Attempt an  Intimidation check and compare it to the Will DC of  one enemy creature within 60 feet. This acti |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/8/SectionHeader/13` | 0.475289 | **OFFENSIVE DEFENSE **[two-actions] **FEAT 6** |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/7/Text/26` | 0.470497 | **Critical Success** Your taunts sting hard. Until the start of  your next turn, any hostile actions that the creature  takes must include you as a target or include you in the  area; otherwise, the c |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/5/SectionHeader/44` | 0.453230 | **MENACING LAUGHTER **[one-action] **FEAT 2** |

### Query 121
- Text: What are the requirements for **Prerequisites** trained in Intimidation?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/7/SectionHeader/24']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/7/SectionHeader/24', 'PZO22001 Starfinder Player Core 150-161::/page/1/Text/57', 'PZO22001 Starfinder Player Core 150-161::/page/7/Text/25']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/7/SectionHeader/24', 'PZO22001 Starfinder Player Core 150-161::/page/7/Text/25', 'PZO22001 Starfinder Player Core 150-161::/page/7/SectionHeader/23']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/7/Text/25` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/7/SectionHeader/23` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/7/SectionHeader/24` | 0.969563 | **Prerequisites** trained in Intimidation |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/1/Text/57` | 0.713139 | Trained in Intimidation Trained in a number of additional  skills equal to 3 plus your Intelligence  modifier |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/7/Text/25` | 0.513397 | You taunt your enemy mercilessly, forcing them to  acknowledge you as an immediate threat. Attempt an  Intimidation check and compare it to the Will DC of  one enemy creature within 60 feet. This acti |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/593` | 0.454901 | Intimidating Taunt |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/15` | 0.432957 | **Prerequisites** suppressing fire |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/31` | 0.432957 | **Prerequisites** suppressing fire |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/5/Text/47` | 0.399408 | Your laughter (or other vocalization) remains audible over  the din of your weapons fire. Attempt an Intimidation  check to Demoralize each creature within 30 feet who's  suppressed. |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/50` | 0.372592 | **INITIAL PROFICIENCIES** |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/7/Text/26` | 0.367549 | **Critical Success** Your taunts sting hard. Until the start of  your next turn, any hostile actions that the creature  takes must include you as a target or include you in the  area; otherwise, the c |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/637` | 0.365656 | Soldier's Training |

### Query 122
- Text: What are the requirements for **OFFENSIVE DEFENSE **[two-actions] **FEAT 6**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/8/SectionHeader/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/8/SectionHeader/13', 'PZO22001 Starfinder Player Core 150-161::/page/7/SectionHeader/10', 'PZO22001 Starfinder Player Core 150-161::/page/7/SectionHeader/5']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/8/SectionHeader/13', 'PZO22001 Starfinder Player Core 150-161::/page/8/Text/11', 'PZO22001 Starfinder Player Core 150-161::/page/8/Text/15']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/8/Text/11` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/8/Text/15` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/8/SectionHeader/13` | 0.919741 | **OFFENSIVE DEFENSE **[two-actions] **FEAT 6** |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/7/SectionHeader/10` | 0.685205 | **FOG OF WAR **[two-actions] **FEAT 6** |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/7/SectionHeader/5` | 0.636762 | **COVERING FIRE **[one-action]** OR **[two-actions] **FEAT 6** |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/603` | 0.521792 | Offensive Defense |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/1/SectionHeader/60` | 0.498315 | **DEFENSES** |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/16` | 0.473858 | **YOU'LL HAVE TO GO THROUGH ME! **[two-actions] **FEAT 2** |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/7/SectionHeader/15` | 0.464950 | **I'LL BE BACK **[free-action] **FEAT 6** |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/51` | 0.463786 | **SOLDIER'S TRAINING** **FEAT 16** |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/11/SectionHeader/21` | 0.457366 | **HYBRID TECHNIQUE **[two-actions] **FEAT 20** |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/34` | 0.451643 | **TERROR-FORMING **[two-actions] **FEAT 14** |

### Query 123
- Text: What are the requirements for **PUNITIVE STRIKE **[reaction] **FEAT 6**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/8/SectionHeader/19']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/8/SectionHeader/19', 'PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/615', 'PZO22001 Starfinder Player Core 150-161::/page/5/SectionHeader/18']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/8/SectionHeader/19', 'PZO22001 Starfinder Player Core 150-161::/page/8/Text/18', 'PZO22001 Starfinder Player Core 150-161::/page/8/Text/21']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/8/Text/18` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/8/Text/21` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/8/SectionHeader/19` | 0.914549 | **PUNITIVE STRIKE **[reaction] **FEAT 6** |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/615` | 0.578083 | Punitive Strike |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/5/SectionHeader/18` | 0.501894 | **BURST OF STRENGTH **[reaction] **FEAT 1** |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/9/SectionHeader/22` | 0.433181 | **COME GET SOME! **[reaction] **FEAT 10** |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/8/SectionHeader/13` | 0.428455 | **OFFENSIVE DEFENSE **[two-actions] **FEAT 6** |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/7/SectionHeader/10` | 0.426276 | **FOG OF WAR **[two-actions] **FEAT 6** |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/7/SectionHeader/21` | 0.419876 | **INTIMIDATING TAUNT **[one-action] **FEAT 6** |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/5` | 0.418690 | You concentrate fire on a specific target operating within  your weapon's threat range. Make a ranged Strike against the  triggering creature, ignoring the unwieldy trait of weapons you  wield for thi |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/27` | 0.416953 | You fight on to the absolute last, pushing yourself to make  one final attack at a foe. Make a Strike with a –2 circumstance  penalty, or make an Area Fire or Auto-Fire attack ignoring the |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/7/SectionHeader/5` | 0.416365 | **COVERING FIRE **[one-action]** OR **[two-actions] **FEAT 6** |

### Query 124
- Text: What are the requirements for **AMMO HOARDER** **FEAT 8**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/8/SectionHeader/25']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/8/SectionHeader/25', 'PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/553', 'PZO22001 Starfinder Player Core 150-161::/page/7/Table/3']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/8/SectionHeader/25', 'PZO22001 Starfinder Player Core 150-161::/page/8/SectionHeader/24', 'PZO22001 Starfinder Player Core 150-161::/page/8/Text/27']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/8/SectionHeader/24` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/8/Text/27` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/8/SectionHeader/25` | 0.887383 | **AMMO HOARDER** **FEAT 8** |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/553` | 0.553263 | Ammo Hoarder |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/7/Table/3` | 0.553070 | FeatLevelAmmo Hoarder8Anchoring Impacts10Bring It On!8Brutal Barrage10Bullet Hell12Bullet Typhoon20Burst of Strength1Collateral Witness4Come Get Some!10Concentrated Shot8Coordinated Fire18Covering Fir |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/2` | 0.429350 | **OVERWATCH **[reaction] **FEAT 8** |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/6` | 0.427929 | **RUN HOT **[three-actions] **FEAT 8** |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/8/SectionHeader/30` | 0.414274 | **BRING IT ON! **[one-action] **FEAT 8** |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/554` | 0.396398 | 8 |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/8/Text/16` | 0.386119 | **Requirements** You have a force field upgrade in your armor or  are holding a tech shield. |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/572` | 0.384398 | 8 |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/626` | 0.384398 | 8 |

### Query 125
- Text: What are the requirements for **BRING IT ON! **[one-action] **FEAT 8**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/8/SectionHeader/30']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/8/SectionHeader/30', 'PZO22001 Starfinder Player Core 150-161::/page/9/Text/6', 'PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/557']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/8/SectionHeader/30', 'PZO22001 Starfinder Player Core 150-161::/page/8/Text/32', 'PZO22001 Starfinder Player Core 150-161::/page/8/Text/29']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/8/Text/32` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/8/Text/29` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/8/SectionHeader/30` | 0.916345 | **BRING IT ON! **[one-action] **FEAT 8** |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/6` | 0.617704 | **RUN HOT **[three-actions] **FEAT 8** |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/557` | 0.587424 | Bring It On! |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/7/SectionHeader/5` | 0.517423 | **COVERING FIRE **[one-action]** OR **[two-actions] **FEAT 6** |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/8/SectionHeader/35` | 0.508067 | **CONCENTRATED SHOT **[two-actions] **FEAT 8** |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/12` | 0.507108 | **SHOT ON THE RUN **[two-actions] **FEAT 2** |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/5/SectionHeader/33` | 0.506092 | **READY RELOAD **[one-action] **FEAT 1** |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/2` | 0.483119 | **OVERWATCH **[reaction] **FEAT 8** |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/16` | 0.483009 | **YOU'LL HAVE TO GO THROUGH ME! **[two-actions] **FEAT 2** |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/7/SectionHeader/21` | 0.475226 | **INTIMIDATING TAUNT **[one-action] **FEAT 6** |

### Query 126
- Text: What are the requirements for **CONCENTRATED SHOT **[two-actions] **FEAT 8**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/8/SectionHeader/35']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/8/SectionHeader/35', 'PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/571', 'PZO22001 Starfinder Player Core 150-161::/page/9/Text/6']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/8/SectionHeader/35', 'PZO22001 Starfinder Player Core 150-161::/page/8/Text/34', 'PZO22001 Starfinder Player Core 150-161::/page/8/Text/37']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/8/Text/34` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/8/Text/37` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/8/SectionHeader/35` | 0.921955 | **CONCENTRATED SHOT **[two-actions] **FEAT 8** |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/571` | 0.633732 | Concentrated Shot |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/6` | 0.618637 | **RUN HOT **[three-actions] **FEAT 8** |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/12` | 0.547875 | **SHOT ON THE RUN **[two-actions] **FEAT 2** |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/8/SectionHeader/30` | 0.531094 | **BRING IT ON! **[one-action] **FEAT 8** |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/35` | 0.521141 | **SHOVING SHOT **[two-actions] **FEAT 4** |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/11/SectionHeader/4` | 0.510976 | **COORDINATED FIRE **[three-actions] **FEAT 18** |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/7/SectionHeader/5` | 0.474353 | **COVERING FIRE **[one-action]** OR **[two-actions] **FEAT 6** |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/11/SectionHeader/21` | 0.471010 | **HYBRID TECHNIQUE **[two-actions] **FEAT 20** |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/28` | 0.466052 | **SCATTERING FIRE **[two-actions] **FEAT 14** |

### Query 127
- Text: What are the requirements for **OVERWATCH **[reaction] **FEAT 8**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/9/Text/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/9/Text/2', 'PZO22001 Starfinder Player Core 150-161::/page/8/SectionHeader/30', 'PZO22001 Starfinder Player Core 150-161::/page/9/Text/6']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/9/Text/2', 'PZO22001 Starfinder Player Core 150-161::/page/9/Text/3', 'PZO22001 Starfinder Player Core 150-161::/page/9/Text/1']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/9/Text/3` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/9/Text/1` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/2` | 0.901699 | **OVERWATCH **[reaction] **FEAT 8** |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/8/SectionHeader/30` | 0.590937 | **BRING IT ON! **[one-action] **FEAT 8** |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/6` | 0.564681 | **RUN HOT **[three-actions] **FEAT 8** |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/47` | 0.521353 | **OVERKILL** **FEAT 16** |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/8/SectionHeader/35` | 0.481349 | **CONCENTRATED SHOT **[two-actions] **FEAT 8** |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/26` | 0.477108 | **OVERWHELMING ASSAULT** **FEAT 4** |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/7/Table/14` | 0.476205 | FeatLevelOffensive Defense6Overkill16Overwatch8Overwhelming Assault4Pin Down1Punishing Salvo4Punitive Strike6Quick Swap1Ready Reload1Relentless Endurance2Rocket Jump12Run Hot8Run, Cowards!14Scattering |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/5/SectionHeader/23` | 0.461963 | **PIN DOWN **[reaction] **FEAT 1** |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/607` | 0.456019 | Overwatch |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/9/SectionHeader/22` | 0.452660 | **COME GET SOME! **[reaction] **FEAT 10** |

### Query 128
- Text: What are the requirements for **RUN HOT **[three-actions] **FEAT 8**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/9/Text/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/9/Text/6', 'PZO22001 Starfinder Player Core 150-161::/page/9/Text/48', 'PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/12']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/9/Text/6', 'PZO22001 Starfinder Player Core 150-161::/page/9/Text/8', 'PZO22001 Starfinder Player Core 150-161::/page/9/Text/5']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/9/Text/8` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/9/Text/5` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/6` | 0.901438 | **RUN HOT **[three-actions] **FEAT 8** |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/48` | 0.735211 | **Prerequisites** Run Hot |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/12` | 0.631231 | **SHOT ON THE RUN **[two-actions] **FEAT 2** |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/625` | 0.553030 | Run Hot |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/8/SectionHeader/30` | 0.540485 | **BRING IT ON! **[one-action] **FEAT 8** |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/8/SectionHeader/35` | 0.512962 | **CONCENTRATED SHOT **[two-actions] **FEAT 8** |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/11/SectionHeader/4` | 0.502525 | **COORDINATED FIRE **[three-actions] **FEAT 18** |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/7/SectionHeader/5` | 0.476937 | **COVERING FIRE **[one-action]** OR **[two-actions] **FEAT 6** |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/35` | 0.469381 | **SHOVING SHOT **[two-actions] **FEAT 4** |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/16` | 0.464381 | **YOU'LL HAVE TO GO THROUGH ME! **[two-actions] **FEAT 2** |

### Query 129
- Text: What are the requirements for **ANCHORING IMPACTS** **FEAT 10**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/9/SectionHeader/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/9/SectionHeader/13', 'PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/555', 'PZO22001 Starfinder Player Core 150-161::/page/9/Text/29']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/9/SectionHeader/13', 'PZO22001 Starfinder Player Core 150-161::/page/9/Text/14', 'PZO22001 Starfinder Player Core 150-161::/page/9/SectionHeader/12']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/9/Text/14` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/9/SectionHeader/12` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/9/SectionHeader/13` | 0.921987 | **ANCHORING IMPACTS** **FEAT 10** |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/555` | 0.653696 | Anchoring Impacts |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/29` | 0.580174 | **DANCE!** **FEAT 10** |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/9/SectionHeader/22` | 0.484978 | **COME GET SOME! **[reaction] **FEAT 10** |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/556` | 0.436581 | 10 |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/632` | 0.424581 | 10 |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/570` | 0.424581 | 10 |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/560` | 0.424581 | 10 |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/580` | 0.424581 | 10 |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/407` | 0.424581 | 10 |

### Query 130
- Text: What are the requirements for **Prerequisites** suppressing fire?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/9/Text/15']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/9/Text/15', 'PZO22001 Starfinder Player Core 150-161::/page/9/Text/31', 'PZO22001 Starfinder Player Core 150-161::/page/2/SectionHeader/8']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/9/Text/15', 'PZO22001 Starfinder Player Core 150-161::/page/9/Text/16', 'PZO22001 Starfinder Player Core 150-161::/page/9/Text/14']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/9/Text/16` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/9/Text/14` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/15` | 0.965384 | **Prerequisites** suppressing fire |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/31` | 0.965384 | **Prerequisites** suppressing fire |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/2/SectionHeader/8` | 0.679538 | SUPPRESSING FIRE |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/575` | 0.524871 | Covering Fire |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/2/Text/9` | 0.471168 | You have a knack for using powerful weapons to harry your  foes and hinder their movement, preventing them from  operating at their peak. If you make an attack with a weapon  that has the area trait ( |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/5/Text/27` | 0.467274 | You focus your weapons fire on a resilient target in order  to suppress them with the sheer ferocity of your assault.  The required target must succeed at a Will save against  your class DC or become |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/7/Text/13` | 0.444611 | **Requirements** You're wielding an area or automatic weapon. The flash and smoke from your frenzied gunfire conceals  you from any enemies who might be left standing in the  aftermath. You Area Fire |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/48` | 0.438365 | **Prerequisites** Run Hot |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/6/Text/5` | 0.425146 | **Suppressed:** Suppressed is a condition often  applied by the soldier when using area and automatic  weapons against targets. Creatures a soldier  suppresses might receive additional conditions and |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/7/SectionHeader/5` | 0.422940 | **COVERING FIRE **[one-action]** OR **[two-actions] **FEAT 6** |

### Query 131
- Text: What are the requirements for **BRUTAL BARRAGE **[one-action] **FEAT 10**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/9/SectionHeader/17']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/9/SectionHeader/17', 'PZO22001 Starfinder Player Core 150-161::/page/9/Text/29', 'PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/559']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/9/SectionHeader/17', 'PZO22001 Starfinder Player Core 150-161::/page/9/Text/16', 'PZO22001 Starfinder Player Core 150-161::/page/9/Text/19']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/9/Text/16` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/9/Text/19` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/9/SectionHeader/17` | 0.921703 | **BRUTAL BARRAGE **[one-action] **FEAT 10** |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/29` | 0.517014 | **DANCE!** **FEAT 10** |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/559` | 0.512250 | Brutal Barrage |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/8/SectionHeader/30` | 0.434212 | **BRING IT ON! **[one-action] **FEAT 8** |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/9/SectionHeader/22` | 0.427686 | **COME GET SOME! **[reaction] **FEAT 10** |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/7/SectionHeader/5` | 0.424660 | **COVERING FIRE **[one-action]** OR **[two-actions] **FEAT 6** |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/9/SectionHeader/34` | 0.422488 | **SHELL SHOWER **[free-action] **FEAT 10** |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/9/SectionHeader/40` | 0.414330 | **BULLET HELL **[two-actions] **FEAT 12** |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/5/SectionHeader/18` | 0.413941 | **BURST OF STRENGTH **[reaction] **FEAT 1** |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/11/SectionHeader/21` | 0.413168 | **HYBRID TECHNIQUE **[two-actions] **FEAT 20** |

### Query 132
- Text: What are the requirements for **COME GET SOME! **[reaction] **FEAT 10**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/9/SectionHeader/22']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/9/SectionHeader/22', 'PZO22001 Starfinder Player Core 150-161::/page/9/Text/29', 'PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/569']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/9/SectionHeader/22', 'PZO22001 Starfinder Player Core 150-161::/page/9/Text/21', 'PZO22001 Starfinder Player Core 150-161::/page/9/Text/24']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/9/Text/21` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/9/Text/24` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/9/SectionHeader/22` | 0.907523 | **COME GET SOME! **[reaction] **FEAT 10** |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/29` | 0.610132 | **DANCE!** **FEAT 10** |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/569` | 0.488331 | Come Get Some! |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/9/SectionHeader/13` | 0.419182 | **ANCHORING IMPACTS** **FEAT 10** |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/16` | 0.418787 | **YOU'LL HAVE TO GO THROUGH ME! **[two-actions] **FEAT 2** |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/9/SectionHeader/34` | 0.416377 | **SHELL SHOWER **[free-action] **FEAT 10** |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/8/SectionHeader/30` | 0.406119 | **BRING IT ON! **[one-action] **FEAT 8** |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/5/SectionHeader/23` | 0.404817 | **PIN DOWN **[reaction] **FEAT 1** |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/9/SectionHeader/17` | 0.397721 | **BRUTAL BARRAGE **[one-action] **FEAT 10** |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/6` | 0.392185 | **LOAD-BEARING HERO **[reaction] **FEAT 12** |

### Query 133
- Text: What are the requirements for **DANCE!** **FEAT 10**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/9/Text/29']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/9/Text/29', 'PZO22001 Starfinder Player Core 150-161::/page/9/SectionHeader/22', 'PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/579']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/9/Text/29', 'PZO22001 Starfinder Player Core 150-161::/page/9/Text/28', 'PZO22001 Starfinder Player Core 150-161::/page/9/Text/30']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/9/Text/28` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/9/Text/30` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/29` | 0.885839 | **DANCE!** **FEAT 10** |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/9/SectionHeader/22` | 0.596821 | **COME GET SOME! **[reaction] **FEAT 10** |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/579` | 0.579802 | Dance! |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/580` | 0.450676 | 10 |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/9/SectionHeader/13` | 0.449583 | **ANCHORING IMPACTS** **FEAT 10** |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/632` | 0.438676 | 10 |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/556` | 0.438676 | 10 |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/560` | 0.438676 | 10 |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/570` | 0.438676 | 10 |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/407` | 0.438676 | 10 |

### Query 134
- Text: What are the requirements for **Prerequisites** suppressing fire?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/9/Text/31']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/9/Text/15', 'PZO22001 Starfinder Player Core 150-161::/page/9/Text/31', 'PZO22001 Starfinder Player Core 150-161::/page/2/SectionHeader/8']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/9/Text/31', 'PZO22001 Starfinder Player Core 150-161::/page/9/Text/32', 'PZO22001 Starfinder Player Core 150-161::/page/9/Text/30']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/9/Text/32` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/9/Text/30` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/15` | 0.965384 | **Prerequisites** suppressing fire |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/31` | 0.965384 | **Prerequisites** suppressing fire |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/2/SectionHeader/8` | 0.679538 | SUPPRESSING FIRE |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/575` | 0.524871 | Covering Fire |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/2/Text/9` | 0.471168 | You have a knack for using powerful weapons to harry your  foes and hinder their movement, preventing them from  operating at their peak. If you make an attack with a weapon  that has the area trait ( |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/5/Text/27` | 0.467274 | You focus your weapons fire on a resilient target in order  to suppress them with the sheer ferocity of your assault.  The required target must succeed at a Will save against  your class DC or become |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/7/Text/13` | 0.444611 | **Requirements** You're wielding an area or automatic weapon. The flash and smoke from your frenzied gunfire conceals  you from any enemies who might be left standing in the  aftermath. You Area Fire |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/48` | 0.438365 | **Prerequisites** Run Hot |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/6/Text/5` | 0.425146 | **Suppressed:** Suppressed is a condition often  applied by the soldier when using area and automatic  weapons against targets. Creatures a soldier  suppresses might receive additional conditions and |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/7/SectionHeader/5` | 0.422940 | **COVERING FIRE **[one-action]** OR **[two-actions] **FEAT 6** |

### Query 135
- Text: What are the requirements for **SHELL SHOWER **[free-action] **FEAT 10**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/9/SectionHeader/34']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/9/SectionHeader/34', 'PZO22001 Starfinder Player Core 150-161::/page/9/Text/29', 'PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/631']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/9/SectionHeader/34', 'PZO22001 Starfinder Player Core 150-161::/page/9/Text/36', 'PZO22001 Starfinder Player Core 150-161::/page/9/Text/33']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/9/Text/36` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/9/Text/33` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/9/SectionHeader/34` | 0.914437 | **SHELL SHOWER **[free-action] **FEAT 10** |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/29` | 0.515108 | **DANCE!** **FEAT 10** |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/631` | 0.512829 | Shell Shower |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/9/SectionHeader/22` | 0.440365 | **COME GET SOME! **[reaction] **FEAT 10** |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/9/SectionHeader/17` | 0.417423 | **BRUTAL BARRAGE **[one-action] **FEAT 10** |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/35` | 0.412305 | **SHOVING SHOT **[two-actions] **FEAT 4** |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/7/SectionHeader/15` | 0.406765 | **I'LL BE BACK **[free-action] **FEAT 6** |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/16` | 0.405317 | **YOU'LL HAVE TO GO THROUGH ME! **[two-actions] **FEAT 2** |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/49` | 0.401917 | **SKILLS** **FEATS** |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/5/Text/57` | 0.401917 | **SKILLS** **FEATS** |

### Query 136
- Text: What are the requirements for **BULLET HELL **[two-actions] **FEAT 12**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/9/SectionHeader/40']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/9/SectionHeader/40', 'PZO22001 Starfinder Player Core 150-161::/page/9/SectionHeader/45', 'PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/11']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/9/SectionHeader/40', 'PZO22001 Starfinder Player Core 150-161::/page/9/Text/42', 'PZO22001 Starfinder Player Core 150-161::/page/9/SectionHeader/39']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/9/Text/42` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/9/SectionHeader/39` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/9/SectionHeader/40` | 0.915213 | **BULLET HELL **[two-actions] **FEAT 12** |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/9/SectionHeader/45` | 0.584682 | **DEATH BLOSSOM **[three-actions] **FEAT 12** |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/11` | 0.582602 | **ROCKET JUMP **[two-actions] **FEAT 12** |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/561` | 0.491402 | Bullet Hell |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/6` | 0.483766 | **LOAD-BEARING HERO **[reaction] **FEAT 12** |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/16` | 0.472249 | **YOU'LL HAVE TO GO THROUGH ME! **[two-actions] **FEAT 2** |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/34` | 0.466966 | **TERROR-FORMING **[two-actions] **FEAT 14** |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/11/SectionHeader/17` | 0.460570 | **BULLET TYPHOON** **FEAT 20** |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/7/SectionHeader/5` | 0.456633 | **COVERING FIRE **[one-action]** OR **[two-actions] **FEAT 6** |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/9/SectionHeader/17` | 0.449679 | **BRUTAL BARRAGE **[one-action] **FEAT 10** |

### Query 137
- Text: What are the requirements for **DEATH BLOSSOM **[three-actions] **FEAT 12**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/9/SectionHeader/45']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/9/SectionHeader/45', 'PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/581', 'PZO22001 Starfinder Player Core 150-161::/page/9/SectionHeader/40']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/9/SectionHeader/45', 'PZO22001 Starfinder Player Core 150-161::/page/9/Text/47', 'PZO22001 Starfinder Player Core 150-161::/page/9/Text/44']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/9/Text/47` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/9/Text/44` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/9/SectionHeader/45` | 0.925578 | **DEATH BLOSSOM **[three-actions] **FEAT 12** |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/581` | 0.598947 | Death Blossom |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/9/SectionHeader/40` | 0.546345 | **BULLET HELL **[two-actions] **FEAT 12** |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/11` | 0.489002 | **ROCKET JUMP **[two-actions] **FEAT 12** |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/16` | 0.445997 | **YOU'LL HAVE TO GO THROUGH ME! **[two-actions] **FEAT 2** |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/6` | 0.444029 | **RUN HOT **[three-actions] **FEAT 8** |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/11/SectionHeader/4` | 0.441417 | **COORDINATED FIRE **[three-actions] **FEAT 18** |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/7/SectionHeader/5` | 0.431166 | **COVERING FIRE **[one-action]** OR **[two-actions] **FEAT 6** |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/35` | 0.414220 | **SHOVING SHOT **[two-actions] **FEAT 4** |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/6` | 0.413826 | **LOAD-BEARING HERO **[reaction] **FEAT 12** |

### Query 138
- Text: What are the requirements for **Prerequisites** Run Hot?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/9/Text/48']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/9/Text/48', 'PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/625', 'PZO22001 Starfinder Player Core 150-161::/page/9/Text/6']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/9/Text/48', 'PZO22001 Starfinder Player Core 150-161::/page/9/Text/47', 'PZO22001 Starfinder Player Core 150-161::/page/9/Text/49']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/9/Text/47` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/9/Text/49` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/48` | 0.948160 | **Prerequisites** Run Hot |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/625` | 0.726601 | Run Hot |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/6` | 0.532341 | **RUN HOT **[three-actions] **FEAT 8** |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/31` | 0.465513 | **Prerequisites** suppressing fire |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/15` | 0.465513 | **Prerequisites** suppressing fire |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/10/Text/31` | 0.440232 | **Prerequisites** Shoving Shot |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/10/Text/4` | 0.440232 | **Prerequisites** Shoving Shot |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/633` | 0.420460 | Shot on the Run |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/12` | 0.369231 | **SHOT ON THE RUN **[two-actions] **FEAT 2** |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/7/SectionHeader/24` | 0.366619 | **Prerequisites** trained in Intimidation |

### Query 139
- Text: What are the requirements for **HAMMER THE NAIL** **FEAT 12**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/1', 'PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/587', 'PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/18']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/1', 'PZO22001 Starfinder Player Core 150-161::/page/9/Text/66', 'PZO22001 Starfinder Player Core 150-161::/page/10/Text/3']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/9/Text/66` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/10/Text/3` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/1` | 0.882978 | **HAMMER THE NAIL** **FEAT 12** |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/587` | 0.659266 | Hammer the Nail |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/18` | 0.570043 | **FAN THE HAMMER **[one-action] **FEAT 14** |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/11` | 0.457946 | **ROCKET JUMP **[two-actions] **FEAT 12** |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/583` | 0.457114 | Fan the Hammer |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/588` | 0.422927 | 12 |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/7/Table/3` | 0.416062 | FeatLevelAmmo Hoarder8Anchoring Impacts10Bring It On!8Brutal Barrage10Bullet Hell12Bullet Typhoon20Burst of Strength1Collateral Witness4Come Get Some!10Concentrated Shot8Coordinated Fire18Covering Fir |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/6` | 0.412917 | **LOAD-BEARING HERO **[reaction] **FEAT 12** |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/2/TableCell/411` | 0.410927 | 12 |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/582` | 0.410927 | 12 |

### Query 140
- Text: What are the requirements for **Prerequisites** Shoving Shot?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/10/Text/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/10/Text/4', 'PZO22001 Starfinder Player Core 150-161::/page/10/Text/31', 'PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/635']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/10/Text/4', 'PZO22001 Starfinder Player Core 150-161::/page/10/Text/5', 'PZO22001 Starfinder Player Core 150-161::/page/10/Text/3']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/10/Text/5` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/10/Text/3` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/10/Text/4` | 0.955890 | **Prerequisites** Shoving Shot |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/10/Text/31` | 0.955890 | **Prerequisites** Shoving Shot |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/635` | 0.740684 | Shoving Shot |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/10/Text/5` | 0.495794 | You adjust the angle of your barrage to maximize the  ammunition's impact on creatures' bodies. Increase the  distance creatures are pushed by your Shoving Shot to 5  feet on a success, 10 feet on a f |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/10/Text/33` | 0.472390 | in the wind. When you Shoving Shot, all creatures in the  area attempt the Fortitude save to avoid forced movement,  rather than just your primary target. |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/35` | 0.470713 | **SHOVING SHOT **[two-actions] **FEAT 4** |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/48` | 0.447055 | **Prerequisites** Run Hot |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/31` | 0.429353 | **Prerequisites** suppressing fire |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/15` | 0.429353 | **Prerequisites** suppressing fire |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/8/Text/38` | 0.427166 | **Requirements** You're wielding an automatic weapon. |

### Query 141
- Text: What are the requirements for **LOAD-BEARING HERO **[reaction] **FEAT 12**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/6', 'PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/597', 'PZO22001 Starfinder Player Core 150-161::/page/9/SectionHeader/40']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/6', 'PZO22001 Starfinder Player Core 150-161::/page/10/Text/8', 'PZO22001 Starfinder Player Core 150-161::/page/10/Text/5']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/10/Text/8` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/10/Text/5` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/6` | 0.907407 | **LOAD-BEARING HERO **[reaction] **FEAT 12** |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/597` | 0.608477 | Load-Bearing Hero |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/9/SectionHeader/40` | 0.528761 | **BULLET HELL **[two-actions] **FEAT 12** |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/11` | 0.464771 | **ROCKET JUMP **[two-actions] **FEAT 12** |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/9/SectionHeader/45` | 0.459816 | **DEATH BLOSSOM **[three-actions] **FEAT 12** |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/9/SectionHeader/22` | 0.453433 | **COME GET SOME! **[reaction] **FEAT 10** |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/7/Table/3` | 0.433365 | FeatLevelAmmo Hoarder8Anchoring Impacts10Bring It On!8Brutal Barrage10Bullet Hell12Bullet Typhoon20Burst of Strength1Collateral Witness4Come Get Some!10Concentrated Shot8Coordinated Fire18Covering Fir |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/8/SectionHeader/30` | 0.431835 | **BRING IT ON! **[one-action] **FEAT 8** |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/16` | 0.422021 | **YOU'LL HAVE TO GO THROUGH ME! **[two-actions] **FEAT 2** |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/34` | 0.415019 | **TERROR-FORMING **[two-actions] **FEAT 14** |

### Query 142
- Text: What are the requirements for **ROCKET JUMP **[two-actions] **FEAT 12**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/11', 'PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/16', 'PZO22001 Starfinder Player Core 150-161::/page/9/SectionHeader/40']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/11', 'PZO22001 Starfinder Player Core 150-161::/page/10/Text/13', 'PZO22001 Starfinder Player Core 150-161::/page/10/Text/10']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/10/Text/13` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/10/Text/10` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/11` | 0.905962 | **ROCKET JUMP **[two-actions] **FEAT 12** |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/16` | 0.554437 | **YOU'LL HAVE TO GO THROUGH ME! **[two-actions] **FEAT 2** |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/9/SectionHeader/40` | 0.543222 | **BULLET HELL **[two-actions] **FEAT 12** |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/9/SectionHeader/45` | 0.499924 | **DEATH BLOSSOM **[three-actions] **FEAT 12** |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/12` | 0.471241 | **SHOT ON THE RUN **[two-actions] **FEAT 2** |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/7/SectionHeader/5` | 0.456386 | **COVERING FIRE **[one-action]** OR **[two-actions] **FEAT 6** |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/43` | 0.447242 | **LIGHT 'EM UP **[two-actions] **FEAT 16** |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/34` | 0.443018 | **TERROR-FORMING **[two-actions] **FEAT 14** |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/6` | 0.440745 | **RUN HOT **[three-actions] **FEAT 8** |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/623` | 0.439994 | Rocket Jump |

### Query 143
- Text: What are the requirements for **FAN THE HAMMER **[one-action] **FEAT 14**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/18']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/18', 'PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/583', 'PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/28']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/18', 'PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/17', 'PZO22001 Starfinder Player Core 150-161::/page/10/Text/20']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/17` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/10/Text/20` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/18` | 0.884027 | **FAN THE HAMMER **[one-action] **FEAT 14** |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/583` | 0.570513 | Fan the Hammer |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/28` | 0.548470 | **SCATTERING FIRE **[two-actions] **FEAT 14** |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/34` | 0.504740 | **TERROR-FORMING **[two-actions] **FEAT 14** |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/1` | 0.494151 | **HAMMER THE NAIL** **FEAT 12** |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/8/SectionHeader/30` | 0.448808 | **BRING IT ON! **[one-action] **FEAT 8** |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/11` | 0.441918 | **ROCKET JUMP **[two-actions] **FEAT 12** |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/38` | 0.438013 | **VECTOR REFLECTOR **[reaction] **FEAT 14** |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/7/SectionHeader/5` | 0.437335 | **COVERING FIRE **[one-action]** OR **[two-actions] **FEAT 6** |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/6` | 0.432321 | **RUN HOT **[three-actions] **FEAT 8** |

### Query 144
- Text: What are the requirements for **RUN, COWARDS!** **FEAT 14**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/24']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/24', 'PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/627', 'PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/18']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/24', 'PZO22001 Starfinder Player Core 150-161::/page/10/Text/23', 'PZO22001 Starfinder Player Core 150-161::/page/10/Text/26']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/10/Text/23` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/10/Text/26` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/24` | 0.899290 | **RUN, COWARDS!** **FEAT 14** |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/627` | 0.676521 | Run, Cowards! |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/18` | 0.467327 | **FAN THE HAMMER **[one-action] **FEAT 14** |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/29` | 0.421210 | **DANCE!** **FEAT 10** |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/628` | 0.417630 | 14 |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/28` | 0.415250 | **SCATTERING FIRE **[two-actions] **FEAT 14** |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/48` | 0.412817 | **Prerequisites** Run Hot |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/642` | 0.405630 | 14 |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/584` | 0.405630 | 14 |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/644` | 0.405630 | 14 |

### Query 145
- Text: What are the requirements for **SCATTERING FIRE **[two-actions] **FEAT 14**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/28']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/28', 'PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/34', 'PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/629']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/28', 'PZO22001 Starfinder Player Core 150-161::/page/10/Text/30', 'PZO22001 Starfinder Player Core 150-161::/page/10/Text/27']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/10/Text/30` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/10/Text/27` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/28` | 0.930001 | **SCATTERING FIRE **[two-actions] **FEAT 14** |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/34` | 0.649124 | **TERROR-FORMING **[two-actions] **FEAT 14** |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/629` | 0.647760 | Scattering Fire |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/7/SectionHeader/5` | 0.589726 | **COVERING FIRE **[one-action]** OR **[two-actions] **FEAT 6** |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/11/SectionHeader/4` | 0.576026 | **COORDINATED FIRE **[three-actions] **FEAT 18** |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/12` | 0.509502 | **SHOT ON THE RUN **[two-actions] **FEAT 2** |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/35` | 0.493057 | **SHOVING SHOT **[two-actions] **FEAT 4** |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/18` | 0.489972 | **FAN THE HAMMER **[one-action] **FEAT 14** |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/10/Text/22` | 0.476402 | **Requirements** Your last action this turn was an Area Fire  or Auto-Fire. |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/8/SectionHeader/35` | 0.476035 | **CONCENTRATED SHOT **[two-actions] **FEAT 8** |

### Query 146
- Text: What are the requirements for **Prerequisites** Shoving Shot?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/10/Text/31']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/10/Text/4', 'PZO22001 Starfinder Player Core 150-161::/page/10/Text/31', 'PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/635']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/10/Text/31', 'PZO22001 Starfinder Player Core 150-161::/page/10/Text/30', 'PZO22001 Starfinder Player Core 150-161::/page/10/Text/32']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/10/Text/30` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/10/Text/32` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/10/Text/4` | 0.955890 | **Prerequisites** Shoving Shot |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/10/Text/31` | 0.955890 | **Prerequisites** Shoving Shot |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/635` | 0.740684 | Shoving Shot |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/10/Text/5` | 0.495794 | You adjust the angle of your barrage to maximize the  ammunition's impact on creatures' bodies. Increase the  distance creatures are pushed by your Shoving Shot to 5  feet on a success, 10 feet on a f |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/10/Text/33` | 0.472390 | in the wind. When you Shoving Shot, all creatures in the  area attempt the Fortitude save to avoid forced movement,  rather than just your primary target. |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/35` | 0.470713 | **SHOVING SHOT **[two-actions] **FEAT 4** |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/48` | 0.447055 | **Prerequisites** Run Hot |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/31` | 0.429353 | **Prerequisites** suppressing fire |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/15` | 0.429353 | **Prerequisites** suppressing fire |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/8/Text/38` | 0.427166 | **Requirements** You're wielding an automatic weapon. |

### Query 147
- Text: What are the requirements for **TERROR-FORMING **[two-actions] **FEAT 14**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/34']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/34', 'PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/28', 'PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/641']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/34', 'PZO22001 Starfinder Player Core 150-161::/page/10/Text/33', 'PZO22001 Starfinder Player Core 150-161::/page/10/Text/36']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/10/Text/33` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/10/Text/36` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/34` | 0.933489 | **TERROR-FORMING **[two-actions] **FEAT 14** |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/28` | 0.663935 | **SCATTERING FIRE **[two-actions] **FEAT 14** |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/641` | 0.579710 | Terror-Forming |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/18` | 0.496735 | **FAN THE HAMMER **[one-action] **FEAT 14** |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/38` | 0.487838 | **VECTOR REFLECTOR **[reaction] **FEAT 14** |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/16` | 0.484435 | **YOU'LL HAVE TO GO THROUGH ME! **[two-actions] **FEAT 2** |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/7/SectionHeader/5` | 0.480203 | **COVERING FIRE **[one-action]** OR **[two-actions] **FEAT 6** |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/7/SectionHeader/10` | 0.477982 | **FOG OF WAR **[two-actions] **FEAT 6** |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/35` | 0.473293 | **SHOVING SHOT **[two-actions] **FEAT 4** |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/11` | 0.469608 | **ROCKET JUMP **[two-actions] **FEAT 12** |

### Query 148
- Text: What are the requirements for **VECTOR REFLECTOR **[reaction] **FEAT 14**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/38']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/38', 'PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/643', 'PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/34']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/38', 'PZO22001 Starfinder Player Core 150-161::/page/10/Text/40', 'PZO22001 Starfinder Player Core 150-161::/page/10/Text/37']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/10/Text/40` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/10/Text/37` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/38` | 0.902835 | **VECTOR REFLECTOR **[reaction] **FEAT 14** |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/643` | 0.578655 | Vector Reflector |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/34` | 0.541338 | **TERROR-FORMING **[two-actions] **FEAT 14** |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/28` | 0.494304 | **SCATTERING FIRE **[two-actions] **FEAT 14** |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/18` | 0.438575 | **FAN THE HAMMER **[one-action] **FEAT 14** |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/9/SectionHeader/22` | 0.430748 | **COME GET SOME! **[reaction] **FEAT 10** |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/21` | 0.421660 | **COLLATERAL WITNESS **[reaction] **FEAT 4** |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/642` | 0.403973 | 14 |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/644` | 0.403973 | 14 |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/6` | 0.399882 | **RELENTLESS ENDURANCE **[reaction] **FEAT 2** |

### Query 149
- Text: What are the requirements for **LIGHT 'EM UP **[two-actions] **FEAT 16**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/43']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/43', 'PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/595', 'PZO22001 Starfinder Player Core 150-161::/page/7/SectionHeader/5']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/43', 'PZO22001 Starfinder Player Core 150-161::/page/10/Text/45', 'PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/42']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/10/Text/45` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/42` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/43` | 0.903318 | **LIGHT 'EM UP **[two-actions] **FEAT 16** |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/595` | 0.618621 | Light 'Em Up |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/7/SectionHeader/5` | 0.542597 | **COVERING FIRE **[one-action]** OR **[two-actions] **FEAT 6** |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/51` | 0.485757 | **SOLDIER'S TRAINING** **FEAT 16** |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/6/SectionHeader/16` | 0.484940 | **YOU'LL HAVE TO GO THROUGH ME! **[two-actions] **FEAT 2** |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/28` | 0.480480 | **SCATTERING FIRE **[two-actions] **FEAT 14** |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/11` | 0.480186 | **ROCKET JUMP **[two-actions] **FEAT 12** |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/47` | 0.475430 | **OVERKILL** **FEAT 16** |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/11/SectionHeader/4` | 0.467832 | **COORDINATED FIRE **[three-actions] **FEAT 18** |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/7/SectionHeader/10` | 0.463050 | **FOG OF WAR **[two-actions] **FEAT 6** |

### Query 150
- Text: What are the requirements for **OVERKILL** **FEAT 16**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/47']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/47', 'PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/51', 'PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/605']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/47', 'PZO22001 Starfinder Player Core 150-161::/page/10/Text/49', 'PZO22001 Starfinder Player Core 150-161::/page/10/Text/46']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/10/Text/49` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/10/Text/46` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/47` | 0.901155 | **OVERKILL** **FEAT 16** |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/51` | 0.580524 | **SOLDIER'S TRAINING** **FEAT 16** |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/605` | 0.556033 | Overkill |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/2` | 0.485023 | **OVERWATCH **[reaction] **FEAT 8** |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/5/Text/57` | 0.464042 | **SKILLS** **FEATS** |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/3/Text/49` | 0.464042 | **SKILLS** **FEATS** |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/7/Text/38` | 0.464042 | **SKILLS** **FEATS** |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/7/Table/14` | 0.458080 | FeatLevelOffensive Defense6Overkill16Overwatch8Overwhelming Assault4Pin Down1Punishing Salvo4Punitive Strike6Quick Swap1Ready Reload1Relentless Endurance2Rocket Jump12Run Hot8Run, Cowards!14Scattering |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/42` | 0.433513 | 16TH LEVEL |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/606` | 0.421639 | 16 |

### Query 151
- Text: What are the requirements for **SOLDIER'S TRAINING** **FEAT 16**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/51']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/51', 'PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/637', 'PZO22001 Starfinder Player Core 150-161::/page/7/SectionHeader/1']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/51', 'PZO22001 Starfinder Player Core 150-161::/page/10/Text/53', 'PZO22001 Starfinder Player Core 150-161::/page/10/Text/50']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/10/Text/53` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/10/Text/50` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/51` | 0.904073 | **SOLDIER'S TRAINING** **FEAT 16** |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/637` | 0.675061 | Soldier's Training |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/7/SectionHeader/1` | 0.590927 | **SOLDIER FEATS BY NAME** |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/10/Text/53` | 0.549962 | **SOLDIER** |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/11/Text/19` | 0.537962 | **SOLDIER** |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/10/Text/36` | 0.537962 | **SOLDIER** |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/11/Text/14` | 0.537962 | **SOLDIER** |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/11/Text/10` | 0.537962 | **SOLDIER** |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/10/Text/20` | 0.537962 | **SOLDIER** |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/10/Text/26` | 0.537962 | **SOLDIER** |

### Query 152
- Text: What are the requirements for **COORDINATED FIRE **[three-actions] **FEAT 18**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/11/SectionHeader/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 150-161::/page/11/SectionHeader/4', 'PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/573', 'PZO22001 Starfinder Player Core 150-161::/page/7/SectionHeader/5']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 150-161::/page/11/SectionHeader/4', 'PZO22001 Starfinder Player Core 150-161::/page/11/Text/6', 'PZO22001 Starfinder Player Core 150-161::/page/11/SectionHeader/3']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 150-161::/page/11/Text/6` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 150-161::/page/11/SectionHeader/3` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 150-161::/page/11/SectionHeader/4` | 0.937380 | **COORDINATED FIRE **[three-actions] **FEAT 18** |
| 2 | `PZO22001 Starfinder Player Core 150-161::/page/7/TableCell/573` | 0.643359 | Coordinated Fire |
| 3 | `PZO22001 Starfinder Player Core 150-161::/page/7/SectionHeader/5` | 0.616968 | **COVERING FIRE **[one-action]** OR **[two-actions] **FEAT 6** |
| 4 | `PZO22001 Starfinder Player Core 150-161::/page/10/SectionHeader/28` | 0.540491 | **SCATTERING FIRE **[two-actions] **FEAT 14** |
| 5 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/6` | 0.515646 | **RUN HOT **[three-actions] **FEAT 8** |
| 6 | `PZO22001 Starfinder Player Core 150-161::/page/10/Text/22` | 0.500385 | **Requirements** Your last action this turn was an Area Fire  or Auto-Fire. |
| 7 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/15` | 0.493929 | **Prerequisites** suppressing fire |
| 8 | `PZO22001 Starfinder Player Core 150-161::/page/9/Text/31` | 0.493929 | **Prerequisites** suppressing fire |
| 9 | `PZO22001 Starfinder Player Core 150-161::/page/6/Text/33` | 0.485374 | **Requirements** Your last action this turn was an Area Fire  attack. |
| 10 | `PZO22001 Starfinder Player Core 150-161::/page/11/SectionHeader/12` | 0.467717 | **SPREAD THE LOVE **[two-actions] **FEAT 18** |
