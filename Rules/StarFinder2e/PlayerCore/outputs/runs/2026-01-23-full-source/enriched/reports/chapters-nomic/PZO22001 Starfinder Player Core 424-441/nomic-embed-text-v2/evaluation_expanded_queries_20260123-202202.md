# RulesLawyer Evaluation Report: nomic-embed-text-v2

## Summary
- Run ID: `None`
- Ruleset ID: `None`
- Document ID: `None`
- Chunk source: `enriched`
- Chunk count: `649`
- Query count: `102`
- Evaluated queries: `102`
- Coverage: `1.0000`
- MRR: `0.9176`
- hit@1: `0.8627`
- hit@3: `0.9706`
- hit@5: `0.9902`
- hit@10: `1.0000`
- Embeddings reused: `False`
- Graph boost: `0.05` (depth=2, top_k=50, source=top, seed_top_n=3, same_kind_only=False, decay=0.4)

### Expanded Gold Metrics
- Coverage: `1.0000`
- MRR: `0.9298`
- hit@1: `0.8824`
- hit@3: `0.9804`
- hit@5: `0.9902`
- hit@10: `1.0000`

### Expanded Gold Expansion Stats
- Queries with additions: `102`
- Avg added per query: `2.29`
- Max added: `10`
- Addition reasons:
  - graph_depth_1: `234`

### Expanded Gold Delta (Expanded - Strict)
- Coverage Δ: `0.0000`
- MRR Δ: `0.0123`
- hit@1 Δ: `0.0196`
- hit@3 Δ: `0.0098`
- hit@5 Δ: `0.0000`
- hit@10 Δ: `0.0000`

## Timings (ms)
- Embedding (chunks): `13155`
- Embedding (queries): `3483`
- Evaluation (strict): `680`
- Evaluation (expanded): `457`
- Total: `22320`

### Timing Estimates (ms)
- Evaluation (strict): `785`
- Evaluation (expanded): `683`
- Total: `18106`

## Query Details
### Query 0
- Text: Summarize PERCEPTION AND  DETECTION
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/1', 'PZO22001 Starfinder Player Core 424-441::/page/7/Text/65', 'PZO22001 Starfinder Player Core 424-441::/page/3/Text/44']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/1', 'PZO22001 Starfinder Player Core 424-441::/page/0/Text/2']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 424-441::/page/0/Text/2` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/1` | 0.986931 | PERCEPTION AND  DETECTION |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/7/Text/65` | 0.849667 | **Perception and ** **Detection** |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/44` | 0.849667 | **Perception and ** **Detection** |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/9/Text/48` | 0.807667 | **Perception and ** **Detection** |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/46` | 0.807667 | **Perception and ** **Detection** |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/15` | 0.628526 | **DETECTING WITH OTHER SENSES** |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/2` | 0.613919 | Your Perception measures your ability to notice things, search for what's hidden, and tell whether  something about a situation is suspicious. |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/5/Text/53` | 0.606703 | **Counteracting** **Perception and ** |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/16` | 0.510379 | The ways a creature can use Perception depend on what  senses it has. The primary concepts you need to know for  understanding senses are precise senses, imprecise senses,  and the three states of det |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/5/Text/54` | 0.503228 | **Detection** **Encounter ** |

### Query 1
- Text: Summarize Your Perception measures your ability to notice things, search for what's hidden, and tell whether  something about a situation is suspicious.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/0/Text/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 424-441::/page/0/Text/2', 'PZO22001 Starfinder Player Core 424-441::/page/0/Text/16', 'PZO22001 Starfinder Player Core 424-441::/page/9/Text/48']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/0/Text/2', 'PZO22001 Starfinder Player Core 424-441::/page/0/Text/6', 'PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/1']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 424-441::/page/0/Text/6` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/1` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/2` | 1.030318 | Your Perception measures your ability to notice things, search for what's hidden, and tell whether  something about a situation is suspicious. |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/16` | 0.705069 | The ways a creature can use Perception depend on what  senses it has. The primary concepts you need to know for  understanding senses are precise senses, imprecise senses,  and the three states of det |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/9/Text/48` | 0.675453 | **Perception and ** **Detection** |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/44` | 0.633453 | **Perception and ** **Detection** |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/46` | 0.633453 | **Perception and ** **Detection** |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/7/Text/65` | 0.633453 | **Perception and ** **Detection** |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/6` | 0.616384 | Perception is frequently used for rolling initiative in an  encounter, and for the Seek action. See page 396 for the  procedure for rolling a Perception check. |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/1` | 0.615337 | PERCEPTION AND  DETECTION |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/7` | 0.608834 | Typically, you'll roll a Perception check to determine your  initiative—the more aware you are of your surroundings,  the more quickly you can respond. Sometimes, though, the  GM might call on you to |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/14/Text/20` | 0.554152 | Anything in plain view is observed by you. If a creature takes  measures to avoid detection, such as by using Stealth to Hide,  it can become hidden or undetected instead of observed. If you |

### Query 2
- Text: What is the rule about Perception is frequently used for rolling initiative in an  encounter, and for the Seek action. See page 396 for the  procedure for rolling a Perception check.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/0/Text/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 424-441::/page/0/Text/6', 'PZO22001 Starfinder Player Core 424-441::/page/3/Text/7', 'PZO22001 Starfinder Player Core 424-441::/page/6/Text/21']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/0/Text/6', 'PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/7', 'PZO22001 Starfinder Player Core 424-441::/page/0/Text/2']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/7` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/0/Text/2` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/6` | 0.986720 | Perception is frequently used for rolling initiative in an  encounter, and for the Seek action. See page 396 for the  procedure for rolling a Perception check. |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/7` | 0.809233 | Typically, you'll roll a Perception check to determine your  initiative—the more aware you are of your surroundings,  the more quickly you can respond. Sometimes, though, the  GM might call on you to |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/6/Text/21` | 0.734452 | You attempt a Stealth check to avoid notice while traveling  at half speed. If you're Avoiding Notice at the start of an  encounter, you usually roll a Stealth check instead of a  Perception check bot |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/6` | 0.654829 | When the GM calls for it, you'll roll initiative to determine  your place in the initiative order, which is the sequence in  which the encounter's participants will take their turns.  Rolling initiati |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/9` | 0.600869 | Unlike a check, where the result is compared to a DC, the  results of initiative rolls are ranked. This ranking sets the  order in which the encounter's participants act—the initiative  order. The cha |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/12/Text/16` | 0.577651 | You can't hear. You automatically critically fail Perception  checks that require you to be able to hear. You take a –2 status  penalty to Perception checks for initiative and checks that  involve sou |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/14/ListItem/7` | 0.575084 | The action to help might require a skill check or  another roll to determine its effectiveness. |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/15` | 0.565151 | Once everyone in the encounter has taken a turn, the round  is over and the next one begins. Don't roll initiative again; the  new round proceeds in the same order as the previous one,  repeating the |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/4` | 0.561398 | An encounter is played out in a series of rounds, during which  the player characters, adversaries, and other participants in the  encounter act in sequence. You roll initiative to determine this  ord |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/2` | 0.558284 | Your Perception measures your ability to notice things, search for what's hidden, and tell whether  something about a situation is suspicious. |

### Query 3
- Text: Summarize LIGHT
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/7', 'PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/9', 'PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/11']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/7', 'PZO22001 Starfinder Player Core 424-441::/page/0/Text/8', 'PZO22001 Starfinder Player Core 424-441::/page/0/Text/6']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 424-441::/page/0/Text/8` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/0/Text/6` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/7` | 0.877153 | LIGHT |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/9` | 0.643898 | BRIGHT LIGHT |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/11` | 0.625443 | DIM LIGHT |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/8` | 0.484495 | There are three levels of light: bright light, dim light, and  darkness. The rules in this book assume that all creatures are  in bright light unless otherwise noted. A source of light lists  the radi |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/2` | 0.475924 | LOW-LIGHT VISION |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/12` | 0.435400 | Areas in shadow or lit by weak light sources are in dim  light. Creatures and objects in dim light have the concealed  condition, unless the seeker has darkvision or low-light vision  (page 425), or a |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/3` | 0.358831 | A creature with low-light vision can see in dim light as though  it were bright light, so it ignores the concealed condition due  to dim light. |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/10` | 0.343959 | In bright light, such as sunlight, creatures and objects can  be observed clearly by anyone with average vision or better. |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/13` | 0.306315 | DARKNESS |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/5/Text/41` | 0.279698 | **Rules Overview** |

### Query 4
- Text: Summarize There are three levels of light: bright light, dim light, and  darkness. The rules in this book assume that all creatures are  in bright light unless otherwise noted. A source of light lists  the radius in which it sheds bright light, and it sheds dim light  to double that radius.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/0/Text/8']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 424-441::/page/0/Text/8', 'PZO22001 Starfinder Player Core 424-441::/page/0/Text/12', 'PZO22001 Starfinder Player Core 424-441::/page/0/Text/14']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/0/Text/8', 'PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/7', 'PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/9']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/7` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/9` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/8` | 1.044731 | There are three levels of light: bright light, dim light, and  darkness. The rules in this book assume that all creatures are  in bright light unless otherwise noted. A source of light lists  the radi |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/12` | 0.666213 | Areas in shadow or lit by weak light sources are in dim  light. Creatures and objects in dim light have the concealed  condition, unless the seeker has darkvision or low-light vision  (page 425), or a |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/14` | 0.592605 | A creature or object within darkness is hidden or undetected  unless the seeker has darkvision or a precise sense other  than vision. A creature without darkvision or another means  of perceiving in d |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/1` | 0.537332 | such vision is in black and white only. Some forms of magical  darkness, such as a 4th-rank *darkness* spell, block normal  darkvision. A creature with greater darkvision, however, can  see through ev |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/3` | 0.520218 | A creature with low-light vision can see in dim light as though  it were bright light, so it ignores the concealed condition due  to dim light. |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/10` | 0.508061 | In bright light, such as sunlight, creatures and objects can  be observed clearly by anyone with average vision or better. |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/28` | 0.506495 | A creature with darkvision or greater darkvision can see  perfectly well in areas of darkness and dim light, though |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/9` | 0.489481 | Three conditions measure the degree to which you can sense  a creature: observed, hidden, and undetected. However, the  concealed and invisible conditions can partially mask a  creature, and the unnot |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/9` | 0.463027 | BRIGHT LIGHT |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/10` | 0.453065 | With the exception of invisible, these conditions are  relative to the viewer—it's possible for a creature to be  observed to you but hidden from your ally. Most of these  rules apply to objects as we |

### Query 5
- Text: Summarize BRIGHT LIGHT
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/9', 'PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/7', 'PZO22001 Starfinder Player Core 424-441::/page/0/Text/8']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/9', 'PZO22001 Starfinder Player Core 424-441::/page/0/Text/10', 'PZO22001 Starfinder Player Core 424-441::/page/0/Text/8']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 424-441::/page/0/Text/10` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/0/Text/8` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/9` | 0.951558 | BRIGHT LIGHT |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/7` | 0.673381 | LIGHT |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/8` | 0.539394 | There are three levels of light: bright light, dim light, and  darkness. The rules in this book assume that all creatures are  in bright light unless otherwise noted. A source of light lists  the radi |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/11` | 0.488750 | DIM LIGHT |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/10` | 0.430087 | In bright light, such as sunlight, creatures and objects can  be observed clearly by anyone with average vision or better. |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/11/SectionHeader/9` | 0.380325 | BLINDED |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/12` | 0.367729 | Areas in shadow or lit by weak light sources are in dim  light. Creatures and objects in dim light have the concealed  condition, unless the seeker has darkvision or low-light vision  (page 425), or a |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/2` | 0.359849 | LOW-LIGHT VISION |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/13` | 0.337309 | DARKNESS |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/14` | 0.334527 | A creature or object within darkness is hidden or undetected  unless the seeker has darkvision or a precise sense other  than vision. A creature without darkvision or another means  of perceiving in d |

### Query 6
- Text: Summarize In bright light, such as sunlight, creatures and objects can  be observed clearly by anyone with average vision or better.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/0/Text/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 424-441::/page/0/Text/10', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/3', 'PZO22001 Starfinder Player Core 424-441::/page/0/Text/28']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/0/Text/10', 'PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/9', 'PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/11']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/9` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/11` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/10` | 1.037662 | In bright light, such as sunlight, creatures and objects can  be observed clearly by anyone with average vision or better. |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/3` | 0.641821 | A creature with low-light vision can see in dim light as though  it were bright light, so it ignores the concealed condition due  to dim light. |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/28` | 0.640388 | A creature with darkvision or greater darkvision can see  perfectly well in areas of darkness and dim light, though |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/14` | 0.596329 | In most circumstances, you can sense creatures without  difficulty and target them normally. Creatures in this state  are observed. Observing requires a precise sense, which for  most creatures means |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/14` | 0.590379 | A creature or object within darkness is hidden or undetected  unless the seeker has darkvision or a precise sense other  than vision. A creature without darkvision or another means  of perceiving in d |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/26` | 0.589989 | While a human might have a difficult time making creatures  out in dim light, an android can see those creatures just fine.  And though androids have no problem seeing on a dimly  lit street, their vi |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/14/Text/21` | 0.586718 | have another precise sense besides sight, you might be able  to observe a creature or object using that sense instead. You  can observe a creature with only your precise senses. When  Seeking a creatu |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/12` | 0.582321 | Areas in shadow or lit by weak light sources are in dim  light. Creatures and objects in dim light have the concealed  condition, unless the seeker has darkvision or low-light vision  (page 425), or a |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/12/Text/14` | 0.558313 | Your eyes are overstimulated or your vision is swimming. If  vision is your only precise sense, all creatures and objects are  concealed from you. |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/10` | 0.557756 | With the exception of invisible, these conditions are  relative to the viewer—it's possible for a creature to be  observed to you but hidden from your ally. Most of these  rules apply to objects as we |

### Query 7
- Text: Summarize DIM LIGHT
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/11', 'PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/7', 'PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/9']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/11', 'PZO22001 Starfinder Player Core 424-441::/page/0/Text/10', 'PZO22001 Starfinder Player Core 424-441::/page/0/Text/12']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 424-441::/page/0/Text/10` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/0/Text/12` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/11` | 0.971706 | DIM LIGHT |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/7` | 0.592001 | LIGHT |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/9` | 0.484297 | BRIGHT LIGHT |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/12` | 0.451693 | Areas in shadow or lit by weak light sources are in dim  light. Creatures and objects in dim light have the concealed  condition, unless the seeker has darkvision or low-light vision  (page 425), or a |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/8` | 0.414156 | There are three levels of light: bright light, dim light, and  darkness. The rules in this book assume that all creatures are  in bright light unless otherwise noted. A source of light lists  the radi |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/3` | 0.406461 | A creature with low-light vision can see in dim light as though  it were bright light, so it ignores the concealed condition due  to dim light. |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/2` | 0.406159 | LOW-LIGHT VISION |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/28` | 0.340722 | A creature with darkvision or greater darkvision can see  perfectly well in areas of darkness and dim light, though |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/26` | 0.259863 | While a human might have a difficult time making creatures  out in dim light, an android can see those creatures just fine.  And though androids have no problem seeing on a dimly  lit street, their vi |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/27` | 0.252054 | DARKVISION AND GREATER  DARKVISION |

### Query 8
- Text: Summarize Areas in shadow or lit by weak light sources are in dim  light. Creatures and objects in dim light have the concealed  condition, unless the seeker has darkvision or low-light vision  (page 425), or a precise sense other than vision.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/0/Text/12']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 424-441::/page/0/Text/12', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/3', 'PZO22001 Starfinder Player Core 424-441::/page/0/Text/14']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/0/Text/12', 'PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/13', 'PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/11']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/13` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/11` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/12` | 1.044312 | Areas in shadow or lit by weak light sources are in dim  light. Creatures and objects in dim light have the concealed  condition, unless the seeker has darkvision or low-light vision  (page 425), or a |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/3` | 0.820581 | A creature with low-light vision can see in dim light as though  it were bright light, so it ignores the concealed condition due  to dim light. |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/14` | 0.740504 | A creature or object within darkness is hidden or undetected  unless the seeker has darkvision or a precise sense other  than vision. A creature without darkvision or another means  of perceiving in d |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/28` | 0.688946 | A creature with darkvision or greater darkvision can see  perfectly well in areas of darkness and dim light, though |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/2/Text/6` | 0.636859 | A concealed creature is in mist, within dim light, or amid  something else that obscures sight but isn't a physical  barrier. When you target a creature that's concealed  from you, you must attempt a |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/8` | 0.620683 | There are three levels of light: bright light, dim light, and  darkness. The rules in this book assume that all creatures are  in bright light unless otherwise noted. A source of light lists  the radi |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/12/Text/14` | 0.589955 | Your eyes are overstimulated or your vision is swimming. If  vision is your only precise sense, all creatures and objects are  concealed from you. |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/26` | 0.584455 | While a human might have a difficult time making creatures  out in dim light, an android can see those creatures just fine.  And though androids have no problem seeing on a dimly  lit street, their vi |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/9` | 0.577527 | Three conditions measure the degree to which you can sense  a creature: observed, hidden, and undetected. However, the  concealed and invisible conditions can partially mask a  creature, and the unnot |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/10` | 0.570169 | In bright light, such as sunlight, creatures and objects can  be observed clearly by anyone with average vision or better. |

### Query 9
- Text: Summarize DARKNESS
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/13', 'PZO22001 Starfinder Player Core 424-441::/page/0/Text/14', 'PZO22001 Starfinder Player Core 424-441::/page/0/Text/12']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/13', 'PZO22001 Starfinder Player Core 424-441::/page/0/Text/14', 'PZO22001 Starfinder Player Core 424-441::/page/0/Text/12']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 424-441::/page/0/Text/14` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/0/Text/12` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/13` | 0.927762 | DARKNESS |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/14` | 0.508664 | A creature or object within darkness is hidden or undetected  unless the seeker has darkvision or a precise sense other  than vision. A creature without darkvision or another means  of perceiving in d |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/12` | 0.497403 | Areas in shadow or lit by weak light sources are in dim  light. Creatures and objects in dim light have the concealed  condition, unless the seeker has darkvision or low-light vision  (page 425), or a |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/27` | 0.421296 | DARKVISION AND GREATER  DARKVISION |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/8` | 0.420045 | There are three levels of light: bright light, dim light, and  darkness. The rules in this book assume that all creatures are  in bright light unless otherwise noted. A source of light lists  the radi |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/1` | 0.404754 | such vision is in black and white only. Some forms of magical  darkness, such as a 4th-rank *darkness* spell, block normal  darkvision. A creature with greater darkvision, however, can  see through ev |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/28` | 0.396864 | A creature with darkvision or greater darkvision can see  perfectly well in areas of darkness and dim light, though |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/12/Text/3` | 0.384223 | **Detection**: Observed, hidden, undetected, unnoticed **Senses**: Blinded, concealed, dazzled, deafened,  invisible |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/16/Text/15` | 0.357345 | noise), waking up if you succeed. If  creatures are attempting to stay quiet  around you, this Perception check uses  their Stealth DCs. Some effects make you sleep  so deeply that they don't allow yo |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/26` | 0.354680 | While a human might have a difficult time making creatures  out in dim light, an android can see those creatures just fine.  And though androids have no problem seeing on a dimly  lit street, their vi |

### Query 10
- Text: Summarize A creature or object within darkness is hidden or undetected  unless the seeker has darkvision or a precise sense other  than vision. A creature without darkvision or another means  of perceiving in darkness has the blinded condition while in  darkness, though it might be able to see illuminated areas beyond  the darkness. If a creature can see into an illuminated area, it can  observe creatures within that illuminated area normally. After  being in darkness, sudden exposure to bright light might make  you dazzled for a short time, as determined by the GM.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/0/Text/14']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 424-441::/page/0/Text/14', 'PZO22001 Starfinder Player Core 424-441::/page/14/Text/18', 'PZO22001 Starfinder Player Core 424-441::/page/0/Text/12']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/0/Text/14', 'PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/13', 'PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/15']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/13` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/15` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/14` | 1.044542 | A creature or object within darkness is hidden or undetected  unless the seeker has darkvision or a precise sense other  than vision. A creature without darkvision or another means  of perceiving in d |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/14/Text/18` | 0.758914 | You can't be seen. You're undetected to everyone. Creatures  can Seek to detect you; if a creature succeeds at its Perception  check against your Stealth DC, you become hidden to that  creature until |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/12` | 0.758307 | Areas in shadow or lit by weak light sources are in dim  light. Creatures and objects in dim light have the concealed  condition, unless the seeker has darkvision or low-light vision  (page 425), or a |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/2/Text/8` | 0.702461 | A creature with the invisible condition (by way of an  *invisibility* spell, for example) is automatically undetected  to any creatures relying on sight as their only precise  sense. Precise senses ot |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/14` | 0.699280 | In most circumstances, you can sense creatures without  difficulty and target them normally. Creatures in this state  are observed. Observing requires a precise sense, which for  most creatures means |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/28` | 0.698110 | A creature with darkvision or greater darkvision can see  perfectly well in areas of darkness and dim light, though |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/3` | 0.680942 | A creature with low-light vision can see in dim light as though  it were bright light, so it ignores the concealed condition due  to dim light. |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/14/Text/20` | 0.679616 | Anything in plain view is observed by you. If a creature takes  measures to avoid detection, such as by using Stealth to Hide,  it can become hidden or undetected instead of observed. If you |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/10` | 0.669115 | With the exception of invisible, these conditions are  relative to the viewer—it's possible for a creature to be  observed to you but hidden from your ally. Most of these  rules apply to objects as we |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/17/Text/2` | 0.666519 | When you're undetected by a creature, that creature can't  see you at all, has no idea what space you occupy, and can't  target you, though you still can be affected by abilities that  target an area. |

### Query 11
- Text: Summarize SENSES
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/15']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/15', 'PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/17', 'PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/20']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/15', 'PZO22001 Starfinder Player Core 424-441::/page/0/Text/16', 'PZO22001 Starfinder Player Core 424-441::/page/0/Text/14']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 424-441::/page/0/Text/16` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/0/Text/14` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/15` | 0.874703 | SENSES |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/17` | 0.790547 | PRECISE SENSES |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/20` | 0.755847 | IMPRECISE SENSES |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/25` | 0.646524 | SPECIAL SENSES |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/22` | 0.590549 | VAGUE SENSES |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/16` | 0.517708 | The ways a creature can use Perception depend on what  senses it has. The primary concepts you need to know for  understanding senses are precise senses, imprecise senses,  and the three states of det |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/15` | 0.483522 | **DETECTING WITH OTHER SENSES** |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/12/Text/3` | 0.447922 | **Detection**: Observed, hidden, undetected, unnoticed **Senses**: Blinded, concealed, dazzled, deafened,  invisible |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/17` | 0.424807 | **Using Stealth with Other Senses** |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/19` | 0.395740 | a creature without having drawbacks is to use a precise  sense. You can usually detect a creature automatically with  a precise sense unless that creature is hiding or obscured by  the environment, in |

### Query 12
- Text: What is the rule about The ways a creature can use Perception depend on what  senses it has. The primary concepts you need to know for  understanding senses are precise senses, imprecise senses,  and the three states of detection a target can be in: observed,  hidden, or undetected. Vision, hearing, and scent are three  prominent senses, but each has a different degree of acuity.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/0/Text/16']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 424-441::/page/0/Text/16', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/14', 'PZO22001 Starfinder Player Core 424-441::/page/14/Text/21']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/0/Text/16', 'PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/17', 'PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/15']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/17` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/15` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/16` | 1.012799 | The ways a creature can use Perception depend on what  senses it has. The primary concepts you need to know for  understanding senses are precise senses, imprecise senses,  and the three states of det |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/14` | 0.764223 | In most circumstances, you can sense creatures without  difficulty and target them normally. Creatures in this state  are observed. Observing requires a precise sense, which for  most creatures means |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/14/Text/21` | 0.746243 | have another precise sense besides sight, you might be able  to observe a creature or object using that sense instead. You  can observe a creature with only your precise senses. When  Seeking a creatu |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/21` | 0.678290 | Average hearing is an imprecise sense—it can't detect the  full range of detail that a precise sense can. You can usually  sense a creature automatically with an imprecise sense, but  it has the hidde |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/16` | 0.662950 | Most abilities that designate "a creature you can see"  or the like function just as well if the user can precisely  sense the subject with a different sense. If a monster  uses a sense other than vis |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/9` | 0.646653 | Three conditions measure the degree to which you can sense  a creature: observed, hidden, and undetected. However, the  concealed and invisible conditions can partially mask a  creature, and the unnot |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/19` | 0.636764 | a creature without having drawbacks is to use a precise  sense. You can usually detect a creature automatically with  a precise sense unless that creature is hiding or obscured by  the environment, in |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/2` | 0.616128 | Your Perception measures your ability to notice things, search for what's hidden, and tell whether  something about a situation is suspicious. |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/12/Text/14` | 0.606074 | Your eyes are overstimulated or your vision is swimming. If  vision is your only precise sense, all creatures and objects are  concealed from you. |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/12/Text/3` | 0.603873 | **Detection**: Observed, hidden, undetected, unnoticed **Senses**: Blinded, concealed, dazzled, deafened,  invisible |

### Query 13
- Text: Summarize PRECISE SENSES
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/17']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/17', 'PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/15', 'PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/20']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/17', 'PZO22001 Starfinder Player Core 424-441::/page/0/Text/16', 'PZO22001 Starfinder Player Core 424-441::/page/0/Text/18']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 424-441::/page/0/Text/16` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/0/Text/18` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/17` | 0.935808 | PRECISE SENSES |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/15` | 0.686687 | SENSES |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/20` | 0.679311 | IMPRECISE SENSES |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/25` | 0.608245 | SPECIAL SENSES |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/16` | 0.525321 | The ways a creature can use Perception depend on what  senses it has. The primary concepts you need to know for  understanding senses are precise senses, imprecise senses,  and the three states of det |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/19` | 0.500790 | a creature without having drawbacks is to use a precise  sense. You can usually detect a creature automatically with  a precise sense unless that creature is hiding or obscured by  the environment, in |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/18` | 0.485035 | Average vision is a precise sense—a sense that can be used to  perceive the world in nuanced detail. The only way to target |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/22` | 0.483503 | VAGUE SENSES |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/15` | 0.458437 | **DETECTING WITH OTHER SENSES** |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/14/Text/21` | 0.456750 | have another precise sense besides sight, you might be able  to observe a creature or object using that sense instead. You  can observe a creature with only your precise senses. When  Seeking a creatu |

### Query 14
- Text: Summarize Average vision is a precise sense—a sense that can be used to  perceive the world in nuanced detail. The only way to target
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/0/Text/18']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 424-441::/page/0/Text/18', 'PZO22001 Starfinder Player Core 424-441::/page/0/Text/21', 'PZO22001 Starfinder Player Core 424-441::/page/0/Text/16']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/0/Text/18', 'PZO22001 Starfinder Player Core 424-441::/page/0/Text/19', 'PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/17']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 424-441::/page/0/Text/19` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/17` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/18` | 1.036042 | Average vision is a precise sense—a sense that can be used to  perceive the world in nuanced detail. The only way to target |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/21` | 0.617772 | Average hearing is an imprecise sense—it can't detect the  full range of detail that a precise sense can. You can usually  sense a creature automatically with an imprecise sense, but  it has the hidde |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/16` | 0.612427 | The ways a creature can use Perception depend on what  senses it has. The primary concepts you need to know for  understanding senses are precise senses, imprecise senses,  and the three states of det |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/12/Text/14` | 0.562416 | Your eyes are overstimulated or your vision is swimming. If  vision is your only precise sense, all creatures and objects are  concealed from you. |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/10` | 0.530507 | In bright light, such as sunlight, creatures and objects can  be observed clearly by anyone with average vision or better. |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/14` | 0.523838 | In most circumstances, you can sense creatures without  difficulty and target them normally. Creatures in this state  are observed. Observing requires a precise sense, which for  most creatures means |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/14/Text/21` | 0.522362 | have another precise sense besides sight, you might be able  to observe a creature or object using that sense instead. You  can observe a creature with only your precise senses. When  Seeking a creatu |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/19` | 0.502243 | a creature without having drawbacks is to use a precise  sense. You can usually detect a creature automatically with  a precise sense unless that creature is hiding or obscured by  the environment, in |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/23` | 0.478226 | A character also has many vague senses—ones that can alert  you that something is there but aren't useful for zeroing in on  it to determine exactly what it is. The most useful of these  for a typical |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/11/Text/10` | 0.476843 | You can't see. All normal terrain is difficult terrain to you.  You can't detect anything using vision. You automatically  critically fail Perception checks that require you to be able  to see, and if |

### Query 15
- Text: What is the rule about a creature without having drawbacks is to use a precise  sense. You can usually detect a creature automatically with  a precise sense unless that creature is hiding or obscured by  the environment, in which case you can use the Seek basic  action to better detect the creature.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/0/Text/19']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 424-441::/page/0/Text/19', 'PZO22001 Starfinder Player Core 424-441::/page/14/Text/21', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/14']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/0/Text/19', 'PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/20', 'PZO22001 Starfinder Player Core 424-441::/page/0/Text/18']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/20` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/0/Text/18` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/19` | 1.004725 | a creature without having drawbacks is to use a precise  sense. You can usually detect a creature automatically with  a precise sense unless that creature is hiding or obscured by  the environment, in |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/14/Text/21` | 0.822290 | have another precise sense besides sight, you might be able  to observe a creature or object using that sense instead. You  can observe a creature with only your precise senses. When  Seeking a creatu |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/14` | 0.781272 | In most circumstances, you can sense creatures without  difficulty and target them normally. Creatures in this state  are observed. Observing requires a precise sense, which for  most creatures means |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/21` | 0.738876 | Average hearing is an imprecise sense—it can't detect the  full range of detail that a precise sense can. You can usually  sense a creature automatically with an imprecise sense, but  it has the hidde |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/24` | 0.731740 | If a creature is undetected, you don't know what space it  occupies and you're off-guard to it. The Seek basic action can  help you find an undetected creature, usually making it hidden  from you inst |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/2/Text/8` | 0.718470 | A creature with the invisible condition (by way of an  *invisibility* spell, for example) is automatically undetected  to any creatures relying on sight as their only precise  sense. Precise senses ot |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/16` | 0.695203 | Most abilities that designate "a creature you can see"  or the like function just as well if the user can precisely  sense the subject with a different sense. If a monster  uses a sense other than vis |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/21` | 0.681556 | A creature that's hidden is only barely perceptible. You only  know what space it occupies. Perhaps the creature just used  the Hide action. Your target might be behind some obstruction,  where you ca |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/13/Text/23` | 0.660796 | While you're hidden from a creature, that creature knows  the space you're in but can't tell precisely where you are.  You typically become hidden by using Stealth to Hide. When  Seeking a creature us |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/24` | 0.660696 | When one creature might detect another, the GM almost  always uses the most precise sense available. |

### Query 16
- Text: Summarize IMPRECISE SENSES
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/20']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/20', 'PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/15', 'PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/17']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/20', 'PZO22001 Starfinder Player Core 424-441::/page/0/Text/19', 'PZO22001 Starfinder Player Core 424-441::/page/0/Text/21']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 424-441::/page/0/Text/19` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/0/Text/21` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/20` | 0.922865 | IMPRECISE SENSES |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/15` | 0.656626 | SENSES |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/17` | 0.655142 | PRECISE SENSES |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/25` | 0.531668 | SPECIAL SENSES |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/21` | 0.507243 | Average hearing is an imprecise sense—it can't detect the  full range of detail that a precise sense can. You can usually  sense a creature automatically with an imprecise sense, but  it has the hidde |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/16` | 0.500563 | The ways a creature can use Perception depend on what  senses it has. The primary concepts you need to know for  understanding senses are precise senses, imprecise senses,  and the three states of det |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/22` | 0.458819 | VAGUE SENSES |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/14/Text/21` | 0.443901 | have another precise sense besides sight, you might be able  to observe a creature or object using that sense instead. You  can observe a creature with only your precise senses. When  Seeking a creatu |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/15` | 0.437806 | **DETECTING WITH OTHER SENSES** |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/7` | 0.435192 | Tremorsense allows a creature to feel the vibrations through  a solid surface caused by movement. It's usually an imprecise  sense with a limited range (listed in the ability). Tremorsense  functions |

### Query 17
- Text: What is the rule about Average hearing is an imprecise sense—it can't detect the  full range of detail that a precise sense can. You can usually  sense a creature automatically with an imprecise sense, but  it has the hidden condition instead of the observed condition.  It might be undetected by you if it's using Stealth or in an  environment that distorts the sense, such as a noisy room  in the case of hearing. In those cases, you have to use the  Seek basic action to detect the creature. At best, an imprecise  sense can be used to make an undetected creature (or one  you didn't even know was there) merely hidden—it can't make  the creature observed.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/0/Text/21']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 424-441::/page/0/Text/21', 'PZO22001 Starfinder Player Core 424-441::/page/14/Text/21', 'PZO22001 Starfinder Player Core 424-441::/page/0/Text/19']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/0/Text/21', 'PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/20', 'PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/22']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/20` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/22` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/21` | 1.020895 | Average hearing is an imprecise sense—it can't detect the  full range of detail that a precise sense can. You can usually  sense a creature automatically with an imprecise sense, but  it has the hidde |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/14/Text/21` | 0.793124 | have another precise sense besides sight, you might be able  to observe a creature or object using that sense instead. You  can observe a creature with only your precise senses. When  Seeking a creatu |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/19` | 0.781523 | a creature without having drawbacks is to use a precise  sense. You can usually detect a creature automatically with  a precise sense unless that creature is hiding or obscured by  the environment, in |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/21` | 0.713816 | A creature that's hidden is only barely perceptible. You only  know what space it occupies. Perhaps the creature just used  the Hide action. Your target might be behind some obstruction,  where you ca |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/2/Text/8` | 0.705500 | A creature with the invisible condition (by way of an  *invisibility* spell, for example) is automatically undetected  to any creatures relying on sight as their only precise  sense. Precise senses ot |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/14` | 0.701249 | In most circumstances, you can sense creatures without  difficulty and target them normally. Creatures in this state  are observed. Observing requires a precise sense, which for  most creatures means |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/13/Text/23` | 0.693521 | While you're hidden from a creature, that creature knows  the space you're in but can't tell precisely where you are.  You typically become hidden by using Stealth to Hide. When  Seeking a creature us |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/16` | 0.693512 | Most abilities that designate "a creature you can see"  or the like function just as well if the user can precisely  sense the subject with a different sense. If a monster  uses a sense other than vis |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/24` | 0.667264 | If a creature is undetected, you don't know what space it  occupies and you're off-guard to it. The Seek basic action can  help you find an undetected creature, usually making it hidden  from you inst |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/14/Text/20` | 0.666832 | Anything in plain view is observed by you. If a creature takes  measures to avoid detection, such as by using Stealth to Hide,  it can become hidden or undetected instead of observed. If you |

### Query 18
- Text: Summarize VAGUE SENSES
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/22']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/22', 'PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/15', 'PZO22001 Starfinder Player Core 424-441::/page/0/Text/23']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/22', 'PZO22001 Starfinder Player Core 424-441::/page/0/Text/23', 'PZO22001 Starfinder Player Core 424-441::/page/0/Text/21']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 424-441::/page/0/Text/23` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/0/Text/21` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/22` | 0.961085 | VAGUE SENSES |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/15` | 0.626854 | SENSES |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/23` | 0.589352 | A character also has many vague senses—ones that can alert  you that something is there but aren't useful for zeroing in on  it to determine exactly what it is. The most useful of these  for a typical |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/17` | 0.525589 | PRECISE SENSES |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/25` | 0.502592 | SPECIAL SENSES |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/20` | 0.498155 | IMPRECISE SENSES |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/16` | 0.372359 | The ways a creature can use Perception depend on what  senses it has. The primary concepts you need to know for  understanding senses are precise senses, imprecise senses,  and the three states of det |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/18` | 0.352314 | Average vision is a precise sense—a sense that can be used to  perceive the world in nuanced detail. The only way to target |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/5` | 0.340550 | Scent involves sensing creatures or objects by smell, and is  usually a vague sense. The range is listed in the ability, and it  functions only if the creature or object being detected emits  an aroma |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/15` | 0.333189 | **DETECTING WITH OTHER SENSES** |

### Query 19
- Text: What is the rule about A character also has many vague senses—ones that can alert  you that something is there but aren't useful for zeroing in on  it to determine exactly what it is. The most useful of these  for a typical character is the sense of smell. At best, a vague  sense can be used to detect the presence of an unnoticed  creature, making it undetected. Even then, the vague sense  isn't sufficient to make the creature hidden or observed.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/0/Text/23']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 424-441::/page/0/Text/23', 'PZO22001 Starfinder Player Core 424-441::/page/0/Text/21', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/16']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/0/Text/23', 'PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/22', 'PZO22001 Starfinder Player Core 424-441::/page/0/Text/24']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/22` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/0/Text/24` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/23` | 1.004018 | A character also has many vague senses—ones that can alert  you that something is there but aren't useful for zeroing in on  it to determine exactly what it is. The most useful of these  for a typical |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/21` | 0.699991 | Average hearing is an imprecise sense—it can't detect the  full range of detail that a precise sense can. You can usually  sense a creature automatically with an imprecise sense, but  it has the hidde |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/16` | 0.692641 | Most abilities that designate "a creature you can see"  or the like function just as well if the user can precisely  sense the subject with a different sense. If a monster  uses a sense other than vis |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/19` | 0.646082 | a creature without having drawbacks is to use a precise  sense. You can usually detect a creature automatically with  a precise sense unless that creature is hiding or obscured by  the environment, in |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/14` | 0.630955 | In most circumstances, you can sense creatures without  difficulty and target them normally. Creatures in this state  are observed. Observing requires a precise sense, which for  most creatures means |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/5` | 0.630760 | Scent involves sensing creatures or objects by smell, and is  usually a vague sense. The range is listed in the ability, and it  functions only if the creature or object being detected emits  an aroma |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/2/Text/4` | 0.620476 | If you have no idea a creature is even present, that creature  is unnoticed by you. A creature that's undetected might also  be unnoticed. This condition usually matters for abilities  that can be use |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/24` | 0.611986 | When one creature might detect another, the GM almost  always uses the most precise sense available. |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/2/Text/8` | 0.605425 | A creature with the invisible condition (by way of an  *invisibility* spell, for example) is automatically undetected  to any creatures relying on sight as their only precise  sense. Precise senses ot |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/14/Text/21` | 0.602940 | have another precise sense besides sight, you might be able  to observe a creature or object using that sense instead. You  can observe a creature with only your precise senses. When  Seeking a creatu |

### Query 20
- Text: Summarize When one creature might detect another, the GM almost  always uses the most precise sense available.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/0/Text/24']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 424-441::/page/0/Text/24', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/11', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/16']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/0/Text/24', 'PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/25', 'PZO22001 Starfinder Player Core 424-441::/page/0/Text/23']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/25` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/0/Text/23` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/24` | 1.034278 | When one creature might detect another, the GM almost  always uses the most precise sense available. |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/11` | 0.769581 | Typically, the GM tracks how well creatures detect each  other since neither party has perfect information. For  example, you might think a creature is in the last place  you sensed it, but it was abl |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/16` | 0.716390 | Most abilities that designate "a creature you can see"  or the like function just as well if the user can precisely  sense the subject with a different sense. If a monster  uses a sense other than vis |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/19` | 0.673680 | a creature without having drawbacks is to use a precise  sense. You can usually detect a creature automatically with  a precise sense unless that creature is hiding or obscured by  the environment, in |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/14/Text/21` | 0.622145 | have another precise sense besides sight, you might be able  to observe a creature or object using that sense instead. You  can observe a creature with only your precise senses. When  Seeking a creatu |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/14` | 0.600514 | In most circumstances, you can sense creatures without  difficulty and target them normally. Creatures in this state  are observed. Observing requires a precise sense, which for  most creatures means |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/23` | 0.592886 | A character also has many vague senses—ones that can alert  you that something is there but aren't useful for zeroing in on  it to determine exactly what it is. The most useful of these  for a typical |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/21` | 0.587510 | Average hearing is an imprecise sense—it can't detect the  full range of detail that a precise sense can. You can usually  sense a creature automatically with an imprecise sense, but  it has the hidde |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/7` | 0.555374 | Typically, you'll roll a Perception check to determine your  initiative—the more aware you are of your surroundings,  the more quickly you can respond. Sometimes, though, the  GM might call on you to |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/2/Text/8` | 0.551935 | A creature with the invisible condition (by way of an  *invisibility* spell, for example) is automatically undetected  to any creatures relying on sight as their only precise  sense. Precise senses ot |

### Query 21
- Text: Summarize SPECIAL SENSES
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/25']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/25', 'PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/15', 'PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/17']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/25', 'PZO22001 Starfinder Player Core 424-441::/page/0/Text/24', 'PZO22001 Starfinder Player Core 424-441::/page/0/Text/26']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 424-441::/page/0/Text/24` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/0/Text/26` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/25` | 0.959602 | SPECIAL SENSES |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/15` | 0.720542 | SENSES |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/17` | 0.674398 | PRECISE SENSES |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/20` | 0.564854 | IMPRECISE SENSES |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/15` | 0.531227 | **DETECTING WITH OTHER SENSES** |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/22` | 0.488994 | VAGUE SENSES |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/17` | 0.475710 | **Using Stealth with Other Senses** |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/16` | 0.473089 | The ways a creature can use Perception depend on what  senses it has. The primary concepts you need to know for  understanding senses are precise senses, imprecise senses,  and the three states of det |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/26` | 0.464020 | While a human might have a difficult time making creatures  out in dim light, an android can see those creatures just fine.  And though androids have no problem seeing on a dimly  lit street, their vi |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/5/SectionHeader/2` | 0.410584 | SPECIAL BATTLES |

### Query 22
- Text: Summarize While a human might have a difficult time making creatures  out in dim light, an android can see those creatures just fine.  And though androids have no problem seeing on a dimly  lit street, their vision can't penetrate complete darkness,  whereas a pahtra's can. Special senses allow a creature to  ignore or reduce the effects of the undetected, hidden, or  concealed conditions (described on pages 425–426) when it  comes to situations that foil average vision.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/0/Text/26']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 424-441::/page/0/Text/26', 'PZO22001 Starfinder Player Core 424-441::/page/0/Text/28', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/3']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/0/Text/26', 'PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/25', 'PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/27']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/25` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/27` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/26` | 1.046605 | While a human might have a difficult time making creatures  out in dim light, an android can see those creatures just fine.  And though androids have no problem seeing on a dimly  lit street, their vi |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/28` | 0.698792 | A creature with darkvision or greater darkvision can see  perfectly well in areas of darkness and dim light, though |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/3` | 0.674869 | A creature with low-light vision can see in dim light as though  it were bright light, so it ignores the concealed condition due  to dim light. |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/14` | 0.630604 | In most circumstances, you can sense creatures without  difficulty and target them normally. Creatures in this state  are observed. Observing requires a precise sense, which for  most creatures means |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/14` | 0.625398 | A creature or object within darkness is hidden or undetected  unless the seeker has darkvision or a precise sense other  than vision. A creature without darkvision or another means  of perceiving in d |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/12` | 0.604664 | Areas in shadow or lit by weak light sources are in dim  light. Creatures and objects in dim light have the concealed  condition, unless the seeker has darkvision or low-light vision  (page 425), or a |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/16` | 0.602571 | Most abilities that designate "a creature you can see"  or the like function just as well if the user can precisely  sense the subject with a different sense. If a monster  uses a sense other than vis |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/10` | 0.592821 | In bright light, such as sunlight, creatures and objects can  be observed clearly by anyone with average vision or better. |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/14/Text/21` | 0.589332 | have another precise sense besides sight, you might be able  to observe a creature or object using that sense instead. You  can observe a creature with only your precise senses. When  Seeking a creatu |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/1` | 0.586039 | such vision is in black and white only. Some forms of magical  darkness, such as a 4th-rank *darkness* spell, block normal  darkvision. A creature with greater darkvision, however, can  see through ev |

### Query 23
- Text: Summarize DARKVISION AND GREATER  DARKVISION
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/27']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/27', 'PZO22001 Starfinder Player Core 424-441::/page/0/Text/28', 'PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/2']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/27', 'PZO22001 Starfinder Player Core 424-441::/page/0/Text/28', 'PZO22001 Starfinder Player Core 424-441::/page/0/Text/26']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 424-441::/page/0/Text/28` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/0/Text/26` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/27` | 1.006085 | DARKVISION AND GREATER  DARKVISION |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/28` | 0.606863 | A creature with darkvision or greater darkvision can see  perfectly well in areas of darkness and dim light, though |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/2` | 0.497892 | LOW-LIGHT VISION |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/1` | 0.455832 | such vision is in black and white only. Some forms of magical  darkness, such as a 4th-rank *darkness* spell, block normal  darkvision. A creature with greater darkvision, however, can  see through ev |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/12` | 0.451635 | Areas in shadow or lit by weak light sources are in dim  light. Creatures and objects in dim light have the concealed  condition, unless the seeker has darkvision or low-light vision  (page 425), or a |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/14` | 0.421831 | A creature or object within darkness is hidden or undetected  unless the seeker has darkvision or a precise sense other  than vision. A creature without darkvision or another means  of perceiving in d |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/13` | 0.401663 | DARKNESS |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/26` | 0.372790 | While a human might have a difficult time making creatures  out in dim light, an android can see those creatures just fine.  And though androids have no problem seeing on a dimly  lit street, their vi |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/11` | 0.369273 | Typically, the GM tracks how well creatures detect each  other since neither party has perfect information. For  example, you might think a creature is in the last place  you sensed it, but it was abl |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/3` | 0.364837 | A creature with low-light vision can see in dim light as though  it were bright light, so it ignores the concealed condition due  to dim light. |

### Query 24
- Text: Summarize A creature with darkvision or greater darkvision can see  perfectly well in areas of darkness and dim light, though
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/0/Text/28']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 424-441::/page/0/Text/28', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/1', 'PZO22001 Starfinder Player Core 424-441::/page/0/Text/12']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/0/Text/28', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/1', 'PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/27']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 424-441::/page/1/Text/1` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/27` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/28` | 1.037890 | A creature with darkvision or greater darkvision can see  perfectly well in areas of darkness and dim light, though |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/1` | 0.779910 | such vision is in black and white only. Some forms of magical  darkness, such as a 4th-rank *darkness* spell, block normal  darkvision. A creature with greater darkvision, however, can  see through ev |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/12` | 0.751730 | Areas in shadow or lit by weak light sources are in dim  light. Creatures and objects in dim light have the concealed  condition, unless the seeker has darkvision or low-light vision  (page 425), or a |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/14` | 0.699606 | A creature or object within darkness is hidden or undetected  unless the seeker has darkvision or a precise sense other  than vision. A creature without darkvision or another means  of perceiving in d |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/3` | 0.690033 | A creature with low-light vision can see in dim light as though  it were bright light, so it ignores the concealed condition due  to dim light. |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/26` | 0.657621 | While a human might have a difficult time making creatures  out in dim light, an android can see those creatures just fine.  And though androids have no problem seeing on a dimly  lit street, their vi |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/10` | 0.616317 | In bright light, such as sunlight, creatures and objects can  be observed clearly by anyone with average vision or better. |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/11` | 0.572492 | Typically, the GM tracks how well creatures detect each  other since neither party has perfect information. For  example, you might think a creature is in the last place  you sensed it, but it was abl |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/16` | 0.553664 | Most abilities that designate "a creature you can see"  or the like function just as well if the user can precisely  sense the subject with a different sense. If a monster  uses a sense other than vis |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/27` | 0.535224 | DARKVISION AND GREATER  DARKVISION |

### Query 25
- Text: What is the rule about such vision is in black and white only. Some forms of magical  darkness, such as a 4th-rank *darkness* spell, block normal  darkvision. A creature with greater darkvision, however, can  see through even these forms of magical darkness.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/1', 'PZO22001 Starfinder Player Core 424-441::/page/0/Text/28', 'PZO22001 Starfinder Player Core 424-441::/page/0/Text/14']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/1', 'PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/2', 'PZO22001 Starfinder Player Core 424-441::/page/0/Text/28']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/2` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/0/Text/28` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/1` | 1.008477 | such vision is in black and white only. Some forms of magical  darkness, such as a 4th-rank *darkness* spell, block normal  darkvision. A creature with greater darkvision, however, can  see through ev |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/28` | 0.757593 | A creature with darkvision or greater darkvision can see  perfectly well in areas of darkness and dim light, though |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/14` | 0.683352 | A creature or object within darkness is hidden or undetected  unless the seeker has darkvision or a precise sense other  than vision. A creature without darkvision or another means  of perceiving in d |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/12` | 0.573682 | Areas in shadow or lit by weak light sources are in dim  light. Creatures and objects in dim light have the concealed  condition, unless the seeker has darkvision or low-light vision  (page 425), or a |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/26` | 0.560135 | While a human might have a difficult time making creatures  out in dim light, an android can see those creatures just fine.  And though androids have no problem seeing on a dimly  lit street, their vi |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/3` | 0.560030 | A creature with low-light vision can see in dim light as though  it were bright light, so it ignores the concealed condition due  to dim light. |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/8` | 0.547730 | There are three levels of light: bright light, dim light, and  darkness. The rules in this book assume that all creatures are  in bright light unless otherwise noted. A source of light lists  the radi |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/16` | 0.528553 | Most abilities that designate "a creature you can see"  or the like function just as well if the user can precisely  sense the subject with a different sense. If a monster  uses a sense other than vis |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/10` | 0.525914 | With the exception of invisible, these conditions are  relative to the viewer—it's possible for a creature to be  observed to you but hidden from your ally. Most of these  rules apply to objects as we |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/11/Text/10` | 0.508718 | You can't see. All normal terrain is difficult terrain to you.  You can't detect anything using vision. You automatically  critically fail Perception checks that require you to be able  to see, and if |

### Query 26
- Text: Summarize LOW-LIGHT VISION
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/2', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/3', 'PZO22001 Starfinder Player Core 424-441::/page/0/Text/12']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/2', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/3', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/1']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 424-441::/page/1/Text/3` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/1/Text/1` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/2` | 0.973635 | LOW-LIGHT VISION |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/3` | 0.608362 | A creature with low-light vision can see in dim light as though  it were bright light, so it ignores the concealed condition due  to dim light. |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/12` | 0.557322 | Areas in shadow or lit by weak light sources are in dim  light. Creatures and objects in dim light have the concealed  condition, unless the seeker has darkvision or low-light vision  (page 425), or a |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/7` | 0.454544 | LIGHT |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/28` | 0.429423 | A creature with darkvision or greater darkvision can see  perfectly well in areas of darkness and dim light, though |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/11` | 0.427961 | DIM LIGHT |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/27` | 0.414796 | DARKVISION AND GREATER  DARKVISION |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/10` | 0.409389 | In bright light, such as sunlight, creatures and objects can  be observed clearly by anyone with average vision or better. |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/18` | 0.404524 | Average vision is a precise sense—a sense that can be used to  perceive the world in nuanced detail. The only way to target |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/1` | 0.386001 | such vision is in black and white only. Some forms of magical  darkness, such as a 4th-rank *darkness* spell, block normal  darkvision. A creature with greater darkvision, however, can  see through ev |

### Query 27
- Text: Summarize A creature with low-light vision can see in dim light as though  it were bright light, so it ignores the concealed condition due  to dim light.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/3']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/3', 'PZO22001 Starfinder Player Core 424-441::/page/0/Text/12', 'PZO22001 Starfinder Player Core 424-441::/page/0/Text/14']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/3', 'PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/2', 'PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/4']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/2` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/4` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/3` | 1.037377 | A creature with low-light vision can see in dim light as though  it were bright light, so it ignores the concealed condition due  to dim light. |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/12` | 0.843685 | Areas in shadow or lit by weak light sources are in dim  light. Creatures and objects in dim light have the concealed  condition, unless the seeker has darkvision or low-light vision  (page 425), or a |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/14` | 0.728913 | A creature or object within darkness is hidden or undetected  unless the seeker has darkvision or a precise sense other  than vision. A creature without darkvision or another means  of perceiving in d |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/28` | 0.677523 | A creature with darkvision or greater darkvision can see  perfectly well in areas of darkness and dim light, though |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/2/Text/6` | 0.646700 | A concealed creature is in mist, within dim light, or amid  something else that obscures sight but isn't a physical  barrier. When you target a creature that's concealed  from you, you must attempt a |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/26` | 0.628017 | While a human might have a difficult time making creatures  out in dim light, an android can see those creatures just fine.  And though androids have no problem seeing on a dimly  lit street, their vi |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/14` | 0.609882 | In most circumstances, you can sense creatures without  difficulty and target them normally. Creatures in this state  are observed. Observing requires a precise sense, which for  most creatures means |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/10` | 0.604488 | In bright light, such as sunlight, creatures and objects can  be observed clearly by anyone with average vision or better. |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/1` | 0.582491 | such vision is in black and white only. Some forms of magical  darkness, such as a 4th-rank *darkness* spell, block normal  darkvision. A creature with greater darkvision, however, can  see through ev |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/14/Text/20` | 0.580076 | Anything in plain view is observed by you. If a creature takes  measures to avoid detection, such as by using Stealth to Hide,  it can become hidden or undetected instead of observed. If you |

### Query 28
- Text: Summarize SCENT
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/4', 'PZO22001 Starfinder Player Core 424-441::/page/15/SectionHeader/12', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/5']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/4', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/3', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/5']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 424-441::/page/1/Text/3` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/1/Text/5` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/4` | 0.892466 | SCENT |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/15/SectionHeader/12` | 0.425770 | SICKENED |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/5` | 0.420740 | Scent involves sensing creatures or objects by smell, and is  usually a vague sense. The range is listed in the ability, and it  functions only if the creature or object being detected emits  an aroma |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/15/SectionHeader/21` | 0.340177 | STUNNED |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/6/SectionHeader/16` | 0.289989 | **CONCENTRATE** **EXPLORATION** |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/8/SectionHeader/15` | 0.289989 | **CONCENTRATE** **EXPLORATION** |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/8/SectionHeader/12` | 0.289989 | **CONCENTRATE** **EXPLORATION** |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/7/SectionHeader/18` | 0.289989 | **CONCENTRATE** **EXPLORATION** |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/7/SectionHeader/42` | 0.289989 | **CONCENTRATE** **EXPLORATION** |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/8/SectionHeader/9` | 0.289989 | **CONCENTRATE** **EXPLORATION** |

### Query 29
- Text: What is the rule about Scent involves sensing creatures or objects by smell, and is  usually a vague sense. The range is listed in the ability, and it  functions only if the creature or object being detected emits  an aroma. If a creature emits a heavy aroma or is upwind, the  GM can double or even triple the range of scent abilities used  to detect that creature, and the GM can reduce the range if a  creature is downwind.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/5', 'PZO22001 Starfinder Player Core 424-441::/page/0/Text/23', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/16']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/5', 'PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/4', 'PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/6']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/4` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/6` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/5` | 0.983995 | Scent involves sensing creatures or objects by smell, and is  usually a vague sense. The range is listed in the ability, and it  functions only if the creature or object being detected emits  an aroma |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/23` | 0.628910 | A character also has many vague senses—ones that can alert  you that something is there but aren't useful for zeroing in on  it to determine exactly what it is. The most useful of these  for a typical |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/16` | 0.603731 | Most abilities that designate "a creature you can see"  or the like function just as well if the user can precisely  sense the subject with a different sense. If a monster  uses a sense other than vis |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/11` | 0.533648 | Typically, the GM tracks how well creatures detect each  other since neither party has perfect information. For  example, you might think a creature is in the last place  you sensed it, but it was abl |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/16` | 0.528909 | The ways a creature can use Perception depend on what  senses it has. The primary concepts you need to know for  understanding senses are precise senses, imprecise senses,  and the three states of det |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/24` | 0.520015 | When one creature might detect another, the GM almost  always uses the most precise sense available. |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/13/Text/2` | 0.499812 | You're compelled to focus your attention on something,  distracting you from whatever else is going on around you. You  take a –2 status penalty to Perception and skill checks, and you  can't use conc |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/19` | 0.499024 | a creature without having drawbacks is to use a precise  sense. You can usually detect a creature automatically with  a precise sense unless that creature is hiding or obscured by  the environment, in |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/21` | 0.484328 | Average hearing is an imprecise sense—it can't detect the  full range of detail that a precise sense can. You can usually  sense a creature automatically with an imprecise sense, but  it has the hidde |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/14` | 0.481725 | In most circumstances, you can sense creatures without  difficulty and target them normally. Creatures in this state  are observed. Observing requires a precise sense, which for  most creatures means |

### Query 30
- Text: Summarize TREMORSENSE
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/6', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/7', 'PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/20']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/6', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/7', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/5']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 424-441::/page/1/Text/7` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/1/Text/5` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/6` | 0.951654 | TREMORSENSE |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/7` | 0.639063 | Tremorsense allows a creature to feel the vibrations through  a solid surface caused by movement. It's usually an imprecise  sense with a limited range (listed in the ability). Tremorsense  functions |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/20` | 0.363243 | IMPRECISE SENSES |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/15` | 0.308777 | SENSES |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/18` | 0.275418 | The Stealth skill is designed to use Hide for avoiding  visual detection and Avoid Notice and Sneak to avoid  being both seen and heard. For many special senses,  a player can describe how they're avo |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/11/SectionHeader/14` | 0.270099 | CLUMSY |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/25` | 0.264503 | SPECIAL SENSES |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/17` | 0.263176 | PRECISE SENSES |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/15/Text/22` | 0.253317 | You've become senseless. You can't act. Stunned usually  includes a value, which indicates how many total actions you  lose, possibly over multiple turns, from being stunned. Each  time you regain act |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/8/Text/16` | 0.250550 | You Sustain one effect with a sustained duration while  moving at half speed. Most such effects can be sustained for  10 minutes, though some specify they can be sustained for a  different duration. S |

### Query 31
- Text: What is the rule about Tremorsense allows a creature to feel the vibrations through  a solid surface caused by movement. It's usually an imprecise  sense with a limited range (listed in the ability). Tremorsense  functions only if the detecting creature is on the same surface  as the subject, and only if the subject is moving along (or  burrowing through) the surface.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/7', 'PZO22001 Starfinder Player Core 424-441::/page/0/Text/19', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/16']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/7', 'PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/6', 'PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/8']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/6` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/8` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/7` | 0.991109 | Tremorsense allows a creature to feel the vibrations through  a solid surface caused by movement. It's usually an imprecise  sense with a limited range (listed in the ability). Tremorsense  functions |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/19` | 0.602172 | a creature without having drawbacks is to use a precise  sense. You can usually detect a creature automatically with  a precise sense unless that creature is hiding or obscured by  the environment, in |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/16` | 0.601921 | Most abilities that designate "a creature you can see"  or the like function just as well if the user can precisely  sense the subject with a different sense. If a monster  uses a sense other than vis |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/14/Text/21` | 0.554635 | have another precise sense besides sight, you might be able  to observe a creature or object using that sense instead. You  can observe a creature with only your precise senses. When  Seeking a creatu |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/21` | 0.540738 | Average hearing is an imprecise sense—it can't detect the  full range of detail that a precise sense can. You can usually  sense a creature automatically with an imprecise sense, but  it has the hidde |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/21` | 0.518127 | A creature that's hidden is only barely perceptible. You only  know what space it occupies. Perhaps the creature just used  the Hide action. Your target might be behind some obstruction,  where you ca |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/14` | 0.513410 | In most circumstances, you can sense creatures without  difficulty and target them normally. Creatures in this state  are observed. Observing requires a precise sense, which for  most creatures means |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/2/Text/8` | 0.498777 | A creature with the invisible condition (by way of an  *invisibility* spell, for example) is automatically undetected  to any creatures relying on sight as their only precise  sense. Precise senses ot |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/16` | 0.497275 | The ways a creature can use Perception depend on what  senses it has. The primary concepts you need to know for  understanding senses are precise senses, imprecise senses,  and the three states of det |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/17/Text/2` | 0.490826 | When you're undetected by a creature, that creature can't  see you at all, has no idea what space you occupy, and can't  target you, though you still can be affected by abilities that  target an area. |

### Query 32
- Text: Summarize DETECTING CREATURES
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/8']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/8', 'PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/1', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/46']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/8', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/7', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/9']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 424-441::/page/1/Text/7` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/1/Text/9` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/8` | 0.983144 | DETECTING CREATURES |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/1` | 0.574411 | PERCEPTION AND  DETECTION |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/46` | 0.535108 | **Perception and ** **Detection** |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/44` | 0.493108 | **Perception and ** **Detection** |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/7/Text/65` | 0.493108 | **Perception and ** **Detection** |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/9/Text/48` | 0.493108 | **Perception and ** **Detection** |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/5/Text/54` | 0.484078 | **Detection** **Encounter ** |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/15` | 0.480523 | **DETECTING WITH OTHER SENSES** |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/11` | 0.477733 | Typically, the GM tracks how well creatures detect each  other since neither party has perfect information. For  example, you might think a creature is in the last place  you sensed it, but it was abl |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/19` | 0.459702 | a creature without having drawbacks is to use a precise  sense. You can usually detect a creature automatically with  a precise sense unless that creature is hiding or obscured by  the environment, in |

### Query 33
- Text: Summarize Three conditions measure the degree to which you can sense  a creature: observed, hidden, and undetected. However, the  concealed and invisible conditions can partially mask a  creature, and the unnoticed condition indicates you have no  idea a creature is around. You can find these conditions in  the Conditions Appendix on pages 435–441.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/9', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/14', 'PZO22001 Starfinder Player Core 424-441::/page/2/Text/8']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/9', 'PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/8', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/10']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/8` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/1/Text/10` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/9` | 1.044777 | Three conditions measure the degree to which you can sense  a creature: observed, hidden, and undetected. However, the  concealed and invisible conditions can partially mask a  creature, and the unnot |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/14` | 0.776079 | In most circumstances, you can sense creatures without  difficulty and target them normally. Creatures in this state  are observed. Observing requires a precise sense, which for  most creatures means |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/2/Text/8` | 0.766773 | A creature with the invisible condition (by way of an  *invisibility* spell, for example) is automatically undetected  to any creatures relying on sight as their only precise  sense. Precise senses ot |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/10` | 0.719743 | With the exception of invisible, these conditions are  relative to the viewer—it's possible for a creature to be  observed to you but hidden from your ally. Most of these  rules apply to objects as we |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/2/Text/4` | 0.717824 | If you have no idea a creature is even present, that creature  is unnoticed by you. A creature that's undetected might also  be unnoticed. This condition usually matters for abilities  that can be use |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/17/Text/7` | 0.687094 | If you're unnoticed by a creature, that creature has no  idea you're present. When you're unnoticed, you're also  undetected. This matters for abilities that can be used only  against targets totally |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/14/Text/18` | 0.675467 | You can't be seen. You're undetected to everyone. Creatures  can Seek to detect you; if a creature succeeds at its Perception  check against your Stealth DC, you become hidden to that  creature until |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/24` | 0.664827 | If a creature is undetected, you don't know what space it  occupies and you're off-guard to it. The Seek basic action can  help you find an undetected creature, usually making it hidden  from you inst |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/17/Text/2` | 0.662660 | When you're undetected by a creature, that creature can't  see you at all, has no idea what space you occupy, and can't  target you, though you still can be affected by abilities that  target an area. |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/14` | 0.655955 | A creature or object within darkness is hidden or undetected  unless the seeker has darkvision or a precise sense other  than vision. A creature without darkvision or another means  of perceiving in d |

### Query 34
- Text: Summarize With the exception of invisible, these conditions are  relative to the viewer—it's possible for a creature to be  observed to you but hidden from your ally. Most of these  rules apply to objects as well as creatures.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/10', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/14', 'PZO22001 Starfinder Player Core 424-441::/page/14/Text/20']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/10', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/11', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/9']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 424-441::/page/1/Text/11` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/1/Text/9` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/10` | 1.041571 | With the exception of invisible, these conditions are  relative to the viewer—it's possible for a creature to be  observed to you but hidden from your ally. Most of these  rules apply to objects as we |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/14` | 0.779788 | In most circumstances, you can sense creatures without  difficulty and target them normally. Creatures in this state  are observed. Observing requires a precise sense, which for  most creatures means |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/14/Text/20` | 0.773308 | Anything in plain view is observed by you. If a creature takes  measures to avoid detection, such as by using Stealth to Hide,  it can become hidden or undetected instead of observed. If you |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/9` | 0.713532 | Three conditions measure the degree to which you can sense  a creature: observed, hidden, and undetected. However, the  concealed and invisible conditions can partially mask a  creature, and the unnot |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/14/Text/18` | 0.710236 | You can't be seen. You're undetected to everyone. Creatures  can Seek to detect you; if a creature succeeds at its Perception  check against your Stealth DC, you become hidden to that  creature until |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/2/Text/8` | 0.701855 | A creature with the invisible condition (by way of an  *invisibility* spell, for example) is automatically undetected  to any creatures relying on sight as their only precise  sense. Precise senses ot |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/2/Text/4` | 0.695423 | If you have no idea a creature is even present, that creature  is unnoticed by you. A creature that's undetected might also  be unnoticed. This condition usually matters for abilities  that can be use |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/2/Text/9` | 0.689778 | Other effects might partially foil invisibility. For instance,  if you were tracking an invisible creature's footprints through  the snow, the footprints would make it hidden. Throwing a  net over an |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/17/Text/2` | 0.667331 | When you're undetected by a creature, that creature can't  see you at all, has no idea what space you occupy, and can't  target you, though you still can be affected by abilities that  target an area. |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/17/Text/7` | 0.664715 | If you're unnoticed by a creature, that creature has no  idea you're present. When you're unnoticed, you're also  undetected. This matters for abilities that can be used only  against targets totally |

### Query 35
- Text: What is the rule about Typically, the GM tracks how well creatures detect each  other since neither party has perfect information. For  example, you might think a creature is in the last place  you sensed it, but it was able to Sneak away. Or you  might think a creature can't see you in the dark, but it has  darkvision.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/11', 'PZO22001 Starfinder Player Core 424-441::/page/0/Text/24', 'PZO22001 Starfinder Player Core 424-441::/page/2/Text/8']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/11', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/12', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/10']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 424-441::/page/1/Text/12` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/1/Text/10` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/11` | 1.000222 | Typically, the GM tracks how well creatures detect each  other since neither party has perfect information. For  example, you might think a creature is in the last place  you sensed it, but it was abl |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/24` | 0.726062 | When one creature might detect another, the GM almost  always uses the most precise sense available. |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/2/Text/8` | 0.695173 | A creature with the invisible condition (by way of an  *invisibility* spell, for example) is automatically undetected  to any creatures relying on sight as their only precise  sense. Precise senses ot |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/14/Text/18` | 0.651111 | You can't be seen. You're undetected to everyone. Creatures  can Seek to detect you; if a creature succeeds at its Perception  check against your Stealth DC, you become hidden to that  creature until |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/10` | 0.648862 | With the exception of invisible, these conditions are  relative to the viewer—it's possible for a creature to be  observed to you but hidden from your ally. Most of these  rules apply to objects as we |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/14` | 0.641347 | In most circumstances, you can sense creatures without  difficulty and target them normally. Creatures in this state  are observed. Observing requires a precise sense, which for  most creatures means |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/17/Text/2` | 0.638726 | When you're undetected by a creature, that creature can't  see you at all, has no idea what space you occupy, and can't  target you, though you still can be affected by abilities that  target an area. |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/4/Text/2` | 0.636263 | The GM keeps track of the initiative order for an  encounter. It's usually okay for the players to know  this order since they'll see who goes when and be  aware of one another's results. However, the |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/13/Text/23` | 0.624735 | While you're hidden from a creature, that creature knows  the space you're in but can't tell precisely where you are.  You typically become hidden by using Stealth to Hide. When  Seeking a creature us |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/19` | 0.624458 | In some cases, rolling a Dexterity-based Stealth  skill check to Sneak doesn't make the most sense.  For example, a PC trying to avoid being detected by  a creature that senses heartbeats might medita |

### Query 36
- Text: What is the rule about You can attempt to avoid detection by using the Stealth  skill (page 207) to Avoid Notice, Hide, or Sneak, or by using  Deception to Create a Diversion (page 198).?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/12']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/12', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/18', 'PZO22001 Starfinder Player Core 424-441::/page/6/Text/21']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/12', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/11', 'PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/13']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 424-441::/page/1/Text/11` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/13` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/12` | 0.972879 | You can attempt to avoid detection by using the Stealth  skill (page 207) to Avoid Notice, Hide, or Sneak, or by using  Deception to Create a Diversion (page 198). |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/18` | 0.777527 | The Stealth skill is designed to use Hide for avoiding  visual detection and Avoid Notice and Sneak to avoid  being both seen and heard. For many special senses,  a player can describe how they're avo |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/6/Text/21` | 0.709133 | You attempt a Stealth check to avoid notice while traveling  at half speed. If you're Avoiding Notice at the start of an  encounter, you usually roll a Stealth check instead of a  Perception check bot |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/14/Text/20` | 0.641796 | Anything in plain view is observed by you. If a creature takes  measures to avoid detection, such as by using Stealth to Hide,  it can become hidden or undetected instead of observed. If you |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/19` | 0.620092 | In some cases, rolling a Dexterity-based Stealth  skill check to Sneak doesn't make the most sense.  For example, a PC trying to avoid being detected by  a creature that senses heartbeats might medita |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/14/Text/18` | 0.613379 | You can't be seen. You're undetected to everyone. Creatures  can Seek to detect you; if a creature succeeds at its Perception  check against your Stealth DC, you become hidden to that  creature until |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/7` | 0.606679 | Typically, you'll roll a Perception check to determine your  initiative—the more aware you are of your surroundings,  the more quickly you can respond. Sometimes, though, the  GM might call on you to |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/13/Text/23` | 0.583135 | While you're hidden from a creature, that creature knows  the space you're in but can't tell precisely where you are.  You typically become hidden by using Stealth to Hide. When  Seeking a creature us |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/2/Text/8` | 0.573085 | A creature with the invisible condition (by way of an  *invisibility* spell, for example) is automatically undetected  to any creatures relying on sight as their only precise  sense. Precise senses ot |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/16/Text/15` | 0.537873 | noise), waking up if you succeed. If  creatures are attempting to stay quiet  around you, this Perception check uses  their Stealth DCs. Some effects make you sleep  so deeply that they don't allow yo |

### Query 37
- Text: Summarize OBSERVED
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/13', 'PZO22001 Starfinder Player Core 424-441::/page/14/SectionHeader/19', 'PZO22001 Starfinder Player Core 424-441::/page/12/SectionHeader/27']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/13', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/14', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/12']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 424-441::/page/1/Text/14` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/1/Text/12` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/13` | 0.867597 | OBSERVED |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/14/SectionHeader/19` | 0.867597 | OBSERVED |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/12/SectionHeader/27` | 0.416570 | ENCUMBERED |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/7/SectionHeader/3` | 0.356767 | **AUDITORY** **CONCENTRATE** **EXPLORATION** **VISUAL** |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/14` | 0.350698 | In most circumstances, you can sense creatures without  difficulty and target them normally. Creatures in this state  are observed. Observing requires a precise sense, which for  most creatures means |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/16/SectionHeader/4` | 0.350098 | SUPPRESSED |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/17/SectionHeader/6` | 0.348451 | UNNOTICED |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/2/SectionHeader/3` | 0.348451 | UNNOTICED |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/6/SectionHeader/20` | 0.343628 | **EXPLORATION** |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/6/SectionHeader/23` | 0.343628 | **EXPLORATION** |

### Query 38
- Text: What is the rule about In most circumstances, you can sense creatures without  difficulty and target them normally. Creatures in this state  are observed. Observing requires a precise sense, which for  most creatures means sight. If you can't observe the creature,  it's either hidden, undetected, or unnoticed, and you'll need  to factor in the targeting restrictions. Even if a creature is  observed, it might still be concealed.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/14']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/14', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/10', 'PZO22001 Starfinder Player Core 424-441::/page/14/Text/21']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/14', 'PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/15', 'PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/13']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/15` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/13` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/14` | 1.001272 | In most circumstances, you can sense creatures without  difficulty and target them normally. Creatures in this state  are observed. Observing requires a precise sense, which for  most creatures means |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/10` | 0.800446 | With the exception of invisible, these conditions are  relative to the viewer—it's possible for a creature to be  observed to you but hidden from your ally. Most of these  rules apply to objects as we |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/14/Text/21` | 0.799448 | have another precise sense besides sight, you might be able  to observe a creature or object using that sense instead. You  can observe a creature with only your precise senses. When  Seeking a creatu |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/14/Text/20` | 0.734719 | Anything in plain view is observed by you. If a creature takes  measures to avoid detection, such as by using Stealth to Hide,  it can become hidden or undetected instead of observed. If you |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/9` | 0.730877 | Three conditions measure the degree to which you can sense  a creature: observed, hidden, and undetected. However, the  concealed and invisible conditions can partially mask a  creature, and the unnot |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/2/Text/8` | 0.729264 | A creature with the invisible condition (by way of an  *invisibility* spell, for example) is automatically undetected  to any creatures relying on sight as their only precise  sense. Precise senses ot |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/17/Text/2` | 0.716605 | When you're undetected by a creature, that creature can't  see you at all, has no idea what space you occupy, and can't  target you, though you still can be affected by abilities that  target an area. |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/2/Text/6` | 0.715471 | A concealed creature is in mist, within dim light, or amid  something else that obscures sight but isn't a physical  barrier. When you target a creature that's concealed  from you, you must attempt a |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/2/Text/4` | 0.699369 | If you have no idea a creature is even present, that creature  is unnoticed by you. A creature that's undetected might also  be unnoticed. This condition usually matters for abilities  that can be use |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/19` | 0.695062 | a creature without having drawbacks is to use a precise  sense. You can usually detect a creature automatically with  a precise sense unless that creature is hiding or obscured by  the environment, in |

### Query 39
- Text: Summarize **DETECTING WITH OTHER SENSES**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/15']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/15', 'PZO22001 Starfinder Player Core 424-441::/page/7/Text/65', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/46']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/15', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/14', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/16']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 424-441::/page/1/Text/14` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/1/Text/16` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/15` | 0.998725 | **DETECTING WITH OTHER SENSES** |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/7/Text/65` | 0.731736 | **Perception and ** **Detection** |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/46` | 0.731736 | **Perception and ** **Detection** |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/9/Text/48` | 0.689736 | **Perception and ** **Detection** |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/44` | 0.689736 | **Perception and ** **Detection** |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/1` | 0.650296 | PERCEPTION AND  DETECTION |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/17` | 0.593009 | **Using Stealth with Other Senses** |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/5/Text/54` | 0.533514 | **Detection** **Encounter ** |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/16` | 0.493638 | Most abilities that designate "a creature you can see"  or the like function just as well if the user can precisely  sense the subject with a different sense. If a monster  uses a sense other than vis |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/12/Text/3` | 0.491090 | **Detection**: Observed, hidden, undetected, unnoticed **Senses**: Blinded, concealed, dazzled, deafened,  invisible |

### Query 40
- Text: What is the rule about Most abilities that designate "a creature you can see"  or the like function just as well if the user can precisely  sense the subject with a different sense. If a monster  uses a sense other than vision, the GM can adapt ways  of avoiding detection that work with the monster's  senses. For example, a creature that has echolocation  might use hearing as a primary sense. This could mean  its quarry is concealed in a noisy chamber, hidden in  a great enough din, or invisible under a *silence* spell.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/16']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/16', 'PZO22001 Starfinder Player Core 424-441::/page/14/Text/21', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/14']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/16', 'PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/15', 'PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/17']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/15` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/17` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/16` | 1.006017 | Most abilities that designate "a creature you can see"  or the like function just as well if the user can precisely  sense the subject with a different sense. If a monster  uses a sense other than vis |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/14/Text/21` | 0.758427 | have another precise sense besides sight, you might be able  to observe a creature or object using that sense instead. You  can observe a creature with only your precise senses. When  Seeking a creatu |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/14` | 0.751052 | In most circumstances, you can sense creatures without  difficulty and target them normally. Creatures in this state  are observed. Observing requires a precise sense, which for  most creatures means |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/21` | 0.690337 | Average hearing is an imprecise sense—it can't detect the  full range of detail that a precise sense can. You can usually  sense a creature automatically with an imprecise sense, but  it has the hidde |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/10` | 0.686075 | With the exception of invisible, these conditions are  relative to the viewer—it's possible for a creature to be  observed to you but hidden from your ally. Most of these  rules apply to objects as we |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/2/Text/8` | 0.683570 | A creature with the invisible condition (by way of an  *invisibility* spell, for example) is automatically undetected  to any creatures relying on sight as their only precise  sense. Precise senses ot |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/19` | 0.677191 | a creature without having drawbacks is to use a precise  sense. You can usually detect a creature automatically with  a precise sense unless that creature is hiding or obscured by  the environment, in |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/21` | 0.654604 | A creature that's hidden is only barely perceptible. You only  know what space it occupies. Perhaps the creature just used  the Hide action. Your target might be behind some obstruction,  where you ca |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/24` | 0.650195 | When one creature might detect another, the GM almost  always uses the most precise sense available. |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/14/Text/18` | 0.645834 | You can't be seen. You're undetected to everyone. Creatures  can Seek to detect you; if a creature succeeds at its Perception  check against your Stealth DC, you become hidden to that  creature until |

### Query 41
- Text: Summarize **Using Stealth with Other Senses**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/17']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/17', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/18', 'PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/15']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/17', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/18', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/16']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 424-441::/page/1/Text/18` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/1/Text/16` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/17` | 1.009005 | **Using Stealth with Other Senses** |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/18` | 0.686305 | The Stealth skill is designed to use Hide for avoiding  visual detection and Avoid Notice and Sneak to avoid  being both seen and heard. For many special senses,  a player can describe how they're avo |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/15` | 0.637894 | **DETECTING WITH OTHER SENSES** |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/19` | 0.567638 | In some cases, rolling a Dexterity-based Stealth  skill check to Sneak doesn't make the most sense.  For example, a PC trying to avoid being detected by  a creature that senses heartbeats might medita |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/16` | 0.564855 | Most abilities that designate "a creature you can see"  or the like function just as well if the user can precisely  sense the subject with a different sense. If a monster  uses a sense other than vis |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/13/Text/23` | 0.564598 | While you're hidden from a creature, that creature knows  the space you're in but can't tell precisely where you are.  You typically become hidden by using Stealth to Hide. When  Seeking a creature us |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/12` | 0.553409 | You can attempt to avoid detection by using the Stealth  skill (page 207) to Avoid Notice, Hide, or Sneak, or by using  Deception to Create a Diversion (page 198). |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/14/Text/20` | 0.552634 | Anything in plain view is observed by you. If a creature takes  measures to avoid detection, such as by using Stealth to Hide,  it can become hidden or undetected instead of observed. If you |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/21` | 0.534797 | Average hearing is an imprecise sense—it can't detect the  full range of detail that a precise sense can. You can usually  sense a creature automatically with an imprecise sense, but  it has the hidde |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/14/Text/18` | 0.515888 | You can't be seen. You're undetected to everyone. Creatures  can Seek to detect you; if a creature succeeds at its Perception  check against your Stealth DC, you become hidden to that  creature until |

### Query 42
- Text: What is the rule about The Stealth skill is designed to use Hide for avoiding  visual detection and Avoid Notice and Sneak to avoid  being both seen and heard. For many special senses,  a player can describe how they're avoiding detection  by that special sense and use the most applicable  Stealth action. For instance, a creature stepping lightly  to avoid being detected via tremorsense would be using Sneak.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/18']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/18', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/12', 'PZO22001 Starfinder Player Core 424-441::/page/14/Text/20']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/18', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/19', 'PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/17']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 424-441::/page/1/Text/19` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/17` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/18` | 1.003042 | The Stealth skill is designed to use Hide for avoiding  visual detection and Avoid Notice and Sneak to avoid  being both seen and heard. For many special senses,  a player can describe how they're avo |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/12` | 0.804524 | You can attempt to avoid detection by using the Stealth  skill (page 207) to Avoid Notice, Hide, or Sneak, or by using  Deception to Create a Diversion (page 198). |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/14/Text/20` | 0.737398 | Anything in plain view is observed by you. If a creature takes  measures to avoid detection, such as by using Stealth to Hide,  it can become hidden or undetected instead of observed. If you |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/14/Text/18` | 0.690601 | You can't be seen. You're undetected to everyone. Creatures  can Seek to detect you; if a creature succeeds at its Perception  check against your Stealth DC, you become hidden to that  creature until |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/6/Text/21` | 0.685226 | You attempt a Stealth check to avoid notice while traveling  at half speed. If you're Avoiding Notice at the start of an  encounter, you usually roll a Stealth check instead of a  Perception check bot |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/19` | 0.680981 | In some cases, rolling a Dexterity-based Stealth  skill check to Sneak doesn't make the most sense.  For example, a PC trying to avoid being detected by  a creature that senses heartbeats might medita |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/2/Text/8` | 0.677088 | A creature with the invisible condition (by way of an  *invisibility* spell, for example) is automatically undetected  to any creatures relying on sight as their only precise  sense. Precise senses ot |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/13/Text/23` | 0.662880 | While you're hidden from a creature, that creature knows  the space you're in but can't tell precisely where you are.  You typically become hidden by using Stealth to Hide. When  Seeking a creature us |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/17` | 0.620416 | **Using Stealth with Other Senses** |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/16` | 0.605855 | Most abilities that designate "a creature you can see"  or the like function just as well if the user can precisely  sense the subject with a different sense. If a monster  uses a sense other than vis |

### Query 43
- Text: What is the rule about In some cases, rolling a Dexterity-based Stealth  skill check to Sneak doesn't make the most sense.  For example, a PC trying to avoid being detected by  a creature that senses heartbeats might meditate  to slow their heart rate, using Wisdom instead of  Dexterity for their Stealth check. When a creature  could detect you using multiple different senses, use  your lowest applicable attribute modifier.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/19']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/19', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/18', 'PZO22001 Starfinder Player Core 424-441::/page/6/Text/21']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/19', 'PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/20', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/18']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/20` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/1/Text/18` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/19` | 1.009414 | In some cases, rolling a Dexterity-based Stealth  skill check to Sneak doesn't make the most sense.  For example, a PC trying to avoid being detected by  a creature that senses heartbeats might medita |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/18` | 0.701098 | The Stealth skill is designed to use Hide for avoiding  visual detection and Avoid Notice and Sneak to avoid  being both seen and heard. For many special senses,  a player can describe how they're avo |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/6/Text/21` | 0.697649 | You attempt a Stealth check to avoid notice while traveling  at half speed. If you're Avoiding Notice at the start of an  encounter, you usually roll a Stealth check instead of a  Perception check bot |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/7` | 0.636670 | Typically, you'll roll a Perception check to determine your  initiative—the more aware you are of your surroundings,  the more quickly you can respond. Sometimes, though, the  GM might call on you to |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/11` | 0.614196 | Typically, the GM tracks how well creatures detect each  other since neither party has perfect information. For  example, you might think a creature is in the last place  you sensed it, but it was abl |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/13/Text/23` | 0.593283 | While you're hidden from a creature, that creature knows  the space you're in but can't tell precisely where you are.  You typically become hidden by using Stealth to Hide. When  Seeking a creature us |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/12` | 0.592624 | You can attempt to avoid detection by using the Stealth  skill (page 207) to Avoid Notice, Hide, or Sneak, or by using  Deception to Create a Diversion (page 198). |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/16/Text/15` | 0.587395 | noise), waking up if you succeed. If  creatures are attempting to stay quiet  around you, this Perception check uses  their Stealth DCs. Some effects make you sleep  so deeply that they don't allow yo |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/13/Text/2` | 0.584422 | You're compelled to focus your attention on something,  distracting you from whatever else is going on around you. You  take a –2 status penalty to Perception and skill checks, and you  can't use conc |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/14/Text/18` | 0.569992 | You can't be seen. You're undetected to everyone. Creatures  can Seek to detect you; if a creature succeeds at its Perception  check against your Stealth DC, you become hidden to that  creature until |

### Query 44
- Text: Summarize HIDDEN
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/20']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/20', 'PZO22001 Starfinder Player Core 424-441::/page/13/SectionHeader/22', 'PZO22001 Starfinder Player Core 424-441::/page/12/Text/3']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/20', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/21', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/19']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 424-441::/page/1/Text/21` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/1/Text/19` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/20` | 0.933981 | HIDDEN |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/13/SectionHeader/22` | 0.933981 | HIDDEN |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/12/Text/3` | 0.502108 | **Detection**: Observed, hidden, undetected, unnoticed **Senses**: Blinded, concealed, dazzled, deafened,  invisible |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/21` | 0.468872 | A creature that's hidden is only barely perceptible. You only  know what space it occupies. Perhaps the creature just used  the Hide action. Your target might be behind some obstruction,  where you ca |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/13/Text/23` | 0.466901 | While you're hidden from a creature, that creature knows  the space you're in but can't tell precisely where you are.  You typically become hidden by using Stealth to Hide. When  Seeking a creature us |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/14/Text/20` | 0.455165 | Anything in plain view is observed by you. If a creature takes  measures to avoid detection, such as by using Stealth to Hide,  it can become hidden or undetected instead of observed. If you |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/14/Text/18` | 0.438310 | You can't be seen. You're undetected to everyone. Creatures  can Seek to detect you; if a creature succeeds at its Perception  check against your Stealth DC, you become hidden to that  creature until |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/2/Text/8` | 0.415381 | A creature with the invisible condition (by way of an  *invisibility* spell, for example) is automatically undetected  to any creatures relying on sight as their only precise  sense. Precise senses ot |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/18` | 0.414160 | The Stealth skill is designed to use Hide for avoiding  visual detection and Avoid Notice and Sneak to avoid  being both seen and heard. For many special senses,  a player can describe how they're avo |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/12` | 0.398661 | You can attempt to avoid detection by using the Stealth  skill (page 207) to Avoid Notice, Hide, or Sneak, or by using  Deception to Create a Diversion (page 198). |

### Query 45
- Text: What is the rule about A creature that's hidden is only barely perceptible. You only  know what space it occupies. Perhaps the creature just used  the Hide action. Your target might be behind some obstruction,  where you can see some movement but can't determine an  exact location. Maybe you've been blinded or the creature is  invisible, but you used the Seek basic action to determine its  general location based on hearing alone. Regardless of the  specifics, you're off-guard to a hidden creature.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/21']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/21', 'PZO22001 Starfinder Player Core 424-441::/page/13/Text/23', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/24']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/21', 'PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/20', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/22']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/20` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/1/Text/22` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/21` | 0.999347 | A creature that's hidden is only barely perceptible. You only  know what space it occupies. Perhaps the creature just used  the Hide action. Your target might be behind some obstruction,  where you ca |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/13/Text/23` | 0.811689 | While you're hidden from a creature, that creature knows  the space you're in but can't tell precisely where you are.  You typically become hidden by using Stealth to Hide. When  Seeking a creature us |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/24` | 0.780661 | If a creature is undetected, you don't know what space it  occupies and you're off-guard to it. The Seek basic action can  help you find an undetected creature, usually making it hidden  from you inst |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/17/Text/2` | 0.728645 | When you're undetected by a creature, that creature can't  see you at all, has no idea what space you occupy, and can't  target you, though you still can be affected by abilities that  target an area. |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/2/Text/8` | 0.714882 | A creature with the invisible condition (by way of an  *invisibility* spell, for example) is automatically undetected  to any creatures relying on sight as their only precise  sense. Precise senses ot |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/10` | 0.701213 | With the exception of invisible, these conditions are  relative to the viewer—it's possible for a creature to be  observed to you but hidden from your ally. Most of these  rules apply to objects as we |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/21` | 0.694422 | Average hearing is an imprecise sense—it can't detect the  full range of detail that a precise sense can. You can usually  sense a creature automatically with an imprecise sense, but  it has the hidde |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/14` | 0.689679 | In most circumstances, you can sense creatures without  difficulty and target them normally. Creatures in this state  are observed. Observing requires a precise sense, which for  most creatures means |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/2/Text/4` | 0.670077 | If you have no idea a creature is even present, that creature  is unnoticed by you. A creature that's undetected might also  be unnoticed. This condition usually matters for abilities  that can be use |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/14/Text/18` | 0.667355 | You can't be seen. You're undetected to everyone. Creatures  can Seek to detect you; if a creature succeeds at its Perception  check against your Stealth DC, you become hidden to that  creature until |

### Query 46
- Text: What is the rule about When targeting a hidden creature, before you roll to  determine your effect, you must attempt a DC 11 flat check.  If you fail, you don't affect the creature, though the actions  you used are still expended—as well as any spell slots, costs,  and other resources. You remain off-guard to the creature,  whether you successfully target it or not.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/22']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/22', 'PZO22001 Starfinder Player Core 424-441::/page/17/Text/3', 'PZO22001 Starfinder Player Core 424-441::/page/13/Text/23']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/22', 'PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/23', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/21']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/23` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/1/Text/21` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/22` | 1.017046 | When targeting a hidden creature, before you roll to  determine your effect, you must attempt a DC 11 flat check.  If you fail, you don't affect the creature, though the actions  you used are still ex |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/17/Text/3` | 0.786567 | A creature you're undetected by can guess which square  you're in to try targeting you. It must pick a square and  attempt an attack. This works like targeting a hidden  creature (requiring a DC 11 fl |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/13/Text/23` | 0.780822 | While you're hidden from a creature, that creature knows  the space you're in but can't tell precisely where you are.  You typically become hidden by using Stealth to Hide. When  Seeking a creature us |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/2/Text/6` | 0.726570 | A concealed creature is in mist, within dim light, or amid  something else that obscures sight but isn't a physical  barrier. When you target a creature that's concealed  from you, you must attempt a |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/11/Text/17` | 0.720204 | You're difficult for one or more creatures to see due to thick  fog or some other obscuring feature. You can be concealed  to some creatures but not others. While concealed, you can  still be observed |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/2/Text/1` | 0.718780 | Targeting an undetected creature is difficult. If you suspect  there's a creature around, you can pick a square and attempt  an attack. This works like targeting a hidden creature, but the  flat check |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/13/Text/19` | 0.706698 | You're held in place by another creature, giving you the offguard and immobilized conditions. If you attempt a manipulate  action while grabbed, you must succeed at a DC 5 flat check or  it's lost; ro |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/11/Text/21` | 0.656505 | Each time you take damage from an attack or spell,  you can attempt a DC 11 flat check to recover from your  confusion and end the condition. |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/21` | 0.631719 | A creature that's hidden is only barely perceptible. You only  know what space it occupies. Perhaps the creature just used  the Hide action. Your target might be behind some obstruction,  where you ca |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/17/Text/2` | 0.614322 | When you're undetected by a creature, that creature can't  see you at all, has no idea what space you occupy, and can't  target you, though you still can be affected by abilities that  target an area. |

### Query 47
- Text: Summarize UNDETECTED
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/23']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 424-441::/page/17/SectionHeader/1', 'PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/23', 'PZO22001 Starfinder Player Core 424-441::/page/17/SectionHeader/8']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/23', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/24', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/22']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 424-441::/page/1/Text/24` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/1/Text/22` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/17/SectionHeader/1` | 0.972301 | UNDETECTED |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/23` | 0.972301 | UNDETECTED |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/17/SectionHeader/8` | 0.659103 | UNTETHERED |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/17/SectionHeader/6` | 0.504610 | UNNOTICED |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/2/SectionHeader/3` | 0.504610 | UNNOTICED |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/17/Text/12` | 0.402931 | **Requirements** You have at least one hand or leg (or suitable  appendage) free, and you're untethered. |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/24` | 0.386980 | If a creature is undetected, you don't know what space it  occupies and you're off-guard to it. The Seek basic action can  help you find an undetected creature, usually making it hidden  from you inst |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/2/Text/1` | 0.373702 | Targeting an undetected creature is difficult. If you suspect  there's a creature around, you can pick a square and attempt  an attack. This works like targeting a hidden creature, but the  flat check |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/15/SectionHeader/8` | 0.366775 | QUICKENED |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/12/SectionHeader/27` | 0.365259 | ENCUMBERED |

### Query 48
- Text: What is the rule about If a creature is undetected, you don't know what space it  occupies and you're off-guard to it. The Seek basic action can  help you find an undetected creature, usually making it hidden  from you instead of undetected. If a creature is undetected,  that doesn't mean you're unaware of its presence—you might  suspect an undetected creature is nearby. The unnoticed  condition covers creatures you're unaware of.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/24']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/24', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/21', 'PZO22001 Starfinder Player Core 424-441::/page/2/Text/8']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/24', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/26', 'PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/23']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 424-441::/page/1/Text/26` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/23` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/24` | 1.012012 | If a creature is undetected, you don't know what space it  occupies and you're off-guard to it. The Seek basic action can  help you find an undetected creature, usually making it hidden  from you inst |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/21` | 0.825603 | A creature that's hidden is only barely perceptible. You only  know what space it occupies. Perhaps the creature just used  the Hide action. Your target might be behind some obstruction,  where you ca |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/2/Text/8` | 0.815548 | A creature with the invisible condition (by way of an  *invisibility* spell, for example) is automatically undetected  to any creatures relying on sight as their only precise  sense. Precise senses ot |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/2/Text/4` | 0.772850 | If you have no idea a creature is even present, that creature  is unnoticed by you. A creature that's undetected might also  be unnoticed. This condition usually matters for abilities  that can be use |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/17/Text/7` | 0.748369 | If you're unnoticed by a creature, that creature has no  idea you're present. When you're unnoticed, you're also  undetected. This matters for abilities that can be used only  against targets totally |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/19` | 0.740735 | a creature without having drawbacks is to use a precise  sense. You can usually detect a creature automatically with  a precise sense unless that creature is hiding or obscured by  the environment, in |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/17/Text/2` | 0.732988 | When you're undetected by a creature, that creature can't  see you at all, has no idea what space you occupy, and can't  target you, though you still can be affected by abilities that  target an area. |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/13/Text/23` | 0.703099 | While you're hidden from a creature, that creature knows  the space you're in but can't tell precisely where you are.  You typically become hidden by using Stealth to Hide. When  Seeking a creature us |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/2/Text/1` | 0.693386 | Targeting an undetected creature is difficult. If you suspect  there's a creature around, you can pick a square and attempt  an attack. This works like targeting a hidden creature, but the  flat check |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/14` | 0.686671 | In most circumstances, you can sense creatures without  difficulty and target them normally. Creatures in this state  are observed. Observing requires a precise sense, which for  most creatures means |

### Query 49
- Text: Summarize **INTRODUCTION**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/26']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/26', 'PZO22001 Starfinder Player Core 424-441::/page/3/Text/24', 'PZO22001 Starfinder Player Core 424-441::/page/17/Text/26']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/26', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/24', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/27']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 424-441::/page/1/Text/24` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/1/Text/27` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/26` | 0.880541 | **INTRODUCTION** |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/24` | 0.880541 | **INTRODUCTION** |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/17/Text/26` | 0.880541 | **INTRODUCTION** |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/11/Text/23` | 0.838541 | **INTRODUCTION** |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/5/Text/34` | 0.838541 | **INTRODUCTION** |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/7/Text/45` | 0.838541 | **INTRODUCTION** |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/15/Text/24` | 0.838541 | **INTRODUCTION** |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/9/Text/28` | 0.838541 | **INTRODUCTION** |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/13/Text/30` | 0.838541 | **INTRODUCTION** |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/5/Text/41` | 0.457802 | **Rules Overview** |

### Query 50
- Text: What is the rule about **ANCESTRIES & ** **BACKGROUNDS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/27']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/27', 'PZO22001 Starfinder Player Core 424-441::/page/15/Text/25', 'PZO22001 Starfinder Player Core 424-441::/page/13/Text/31']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/27', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/28', 'PZO22001 Starfinder Player Core 424-441::/page/7/Text/46', 'PZO22001 Starfinder Player Core 424-441::/page/5/Text/35', 'PZO22001 Starfinder Player Core 424-441::/page/17/Text/27', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/26', 'PZO22001 Starfinder Player Core 424-441::/page/11/Text/24', 'PZO22001 Starfinder Player Core 424-441::/page/13/Text/31', 'PZO22001 Starfinder Player Core 424-441::/page/15/Text/25', 'PZO22001 Starfinder Player Core 424-441::/page/3/Text/25', 'PZO22001 Starfinder Player Core 424-441::/page/9/Text/29']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 424-441::/page/1/Text/28` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/7/Text/46` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/5/Text/35` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/17/Text/27` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/1/Text/26` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/11/Text/24` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/13/Text/31` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/15/Text/25` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/3/Text/25` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/9/Text/29` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/27` | 0.920820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/15/Text/25` | 0.920820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/13/Text/31` | 0.920820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/25` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/11/Text/24` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/9/Text/29` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/7/Text/46` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/17/Text/27` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/5/Text/35` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/34` | 0.476883 | **Rules Overview** |

### Query 51
- Text: Summarize **CLASSES**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/28']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/28', 'PZO22001 Starfinder Player Core 424-441::/page/15/Text/26', 'PZO22001 Starfinder Player Core 424-441::/page/3/Text/26']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/28', 'PZO22001 Starfinder Player Core 424-441::/page/11/Text/25', 'PZO22001 Starfinder Player Core 424-441::/page/7/Text/47', 'PZO22001 Starfinder Player Core 424-441::/page/9/Text/30', 'PZO22001 Starfinder Player Core 424-441::/page/3/Text/26', 'PZO22001 Starfinder Player Core 424-441::/page/5/Text/36', 'PZO22001 Starfinder Player Core 424-441::/page/17/Text/28', 'PZO22001 Starfinder Player Core 424-441::/page/13/Text/32', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/27', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/29', 'PZO22001 Starfinder Player Core 424-441::/page/15/Text/26']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 424-441::/page/11/Text/25` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/7/Text/47` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/9/Text/30` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/3/Text/26` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/5/Text/36` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/17/Text/28` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/13/Text/32` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/1/Text/27` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/1/Text/29` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/15/Text/26` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/28` | 0.940061 | **CLASSES** |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/15/Text/26` | 0.940061 | **CLASSES** |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/26` | 0.940061 | **CLASSES** |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/5/Text/36` | 0.910061 | **CLASSES** |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/9/Text/30` | 0.910061 | **CLASSES** |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/7/Text/47` | 0.910061 | **CLASSES** |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/13/Text/32` | 0.910061 | **CLASSES** |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/11/Text/25` | 0.910061 | **CLASSES** |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/17/Text/28` | 0.910061 | **CLASSES** |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/10/SectionHeader/3` | 0.573477 | CLASS FEATURES |

### Query 52
- Text: What is the rule about **SKILLS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/29']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 424-441::/page/17/Text/29', 'PZO22001 Starfinder Player Core 424-441::/page/9/Text/31', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/29']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/29', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/28', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/30']
- Expanded expected found: `True`
- Expanded expected rank: `3`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 424-441::/page/1/Text/28` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/1/Text/30` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/17/Text/29` | 0.864442 | **SKILLS** |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/9/Text/31` | 0.864442 | **SKILLS** |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/29` | 0.864442 | **SKILLS** |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/15/Text/27` | 0.822442 | **SKILLS** |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/7/Text/48` | 0.822442 | **SKILLS** |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/5/Text/37` | 0.822442 | **SKILLS** |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/27` | 0.822442 | **SKILLS** |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/11/Text/26` | 0.822442 | **SKILLS** |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/13/Text/33` | 0.822442 | **SKILLS** |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/9/SectionHeader/25` | 0.712079 | SKILLS |

### Query 53
- Text: What is the rule about **FEATS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/30']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/30', 'PZO22001 Starfinder Player Core 424-441::/page/3/Text/28', 'PZO22001 Starfinder Player Core 424-441::/page/11/Text/27']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/30', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/29', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/31']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 424-441::/page/1/Text/29` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/1/Text/31` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/30` | 0.871817 | **FEATS** |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/28` | 0.871817 | **FEATS** |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/11/Text/27` | 0.871817 | **FEATS** |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/5/Text/38` | 0.829817 | **FEATS** |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/9/Text/32` | 0.829817 | **FEATS** |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/13/Text/34` | 0.829817 | **FEATS** |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/15/Text/28` | 0.829817 | **FEATS** |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/17/Text/30` | 0.829817 | **FEATS** |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/7/Text/49` | 0.829817 | **FEATS** |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/9/SectionHeader/23` | 0.651337 | FEATS |

### Query 54
- Text: Summarize **EQUIPMENT**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/31']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/31', 'PZO22001 Starfinder Player Core 424-441::/page/15/Text/29', 'PZO22001 Starfinder Player Core 424-441::/page/3/Text/29']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/31', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/32', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/30']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 424-441::/page/1/Text/32` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/1/Text/30` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/31` | 0.944726 | **EQUIPMENT** |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/15/Text/29` | 0.944726 | **EQUIPMENT** |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/29` | 0.944726 | **EQUIPMENT** |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/7/Text/50` | 0.902726 | **EQUIPMENT** |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/13/Text/35` | 0.902726 | **EQUIPMENT** |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/9/Text/33` | 0.902726 | **EQUIPMENT** |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/11/Text/28` | 0.902726 | **EQUIPMENT** |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/17/Text/31` | 0.902726 | **EQUIPMENT** |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/5/Text/39` | 0.578761 | **EQUIPMENT** **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/6/SectionHeader/15` | 0.423297 | **ANALYZE ENVIRONMENT ** |

### Query 55
- Text: What is the rule about **SPELLS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/32']
- Expected found: `True`
- Expected rank: `5`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 424-441::/page/13/Text/36', 'PZO22001 Starfinder Player Core 424-441::/page/3/Text/30', 'PZO22001 Starfinder Player Core 424-441::/page/9/Text/34']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/32', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/33', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/31']
- Expanded expected found: `True`
- Expanded expected rank: `5`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 424-441::/page/1/Text/33` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/1/Text/31` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/9/Text/34` | 0.889304 | **SPELLS** |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/30` | 0.889304 | **SPELLS** |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/13/Text/36` | 0.889304 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/7/Text/51` | 0.847304 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/32` | 0.847304 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/11/Text/29` | 0.847304 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/5/Text/39` | 0.759411 | **EQUIPMENT** **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/17/Text/32` | 0.740792 | **SPELLS** **PLAYING THE ** |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/15/Text/30` | 0.740792 | **SPELLS** **PLAYING THE ** |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/8/SectionHeader/5` | 0.716581 | **REPEAT A SPELL** |

### Query 56
- Text: Summarize **PLAYING THE ** **GAME**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/33']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/33', 'PZO22001 Starfinder Player Core 424-441::/page/9/Text/35', 'PZO22001 Starfinder Player Core 424-441::/page/13/Text/37']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/33', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/32', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/34']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 424-441::/page/1/Text/32` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/1/Text/34` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/33` | 0.965000 | **PLAYING THE ** **GAME** |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/13/Text/37` | 0.965000 | **PLAYING THE ** **GAME** |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/9/Text/35` | 0.965000 | **PLAYING THE ** **GAME** |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/7/Text/52` | 0.923000 | **PLAYING THE ** **GAME** |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/5/Text/40` | 0.923000 | **PLAYING THE ** **GAME** |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/11/Text/30` | 0.923000 | **PLAYING THE ** **GAME** |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/31` | 0.811006 | **PLAYING THE ** |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/52` | 0.663024 | **GAME** |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/15/Text/34` | 0.663024 | **GAME** |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/15/Text/30` | 0.576671 | **SPELLS** **PLAYING THE ** |

### Query 57
- Text: Summarize **Rules Overview**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/34']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/34', 'PZO22001 Starfinder Player Core 424-441::/page/3/Text/32', 'PZO22001 Starfinder Player Core 424-441::/page/7/Text/53']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/34', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/33', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/35']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 424-441::/page/1/Text/33` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/1/Text/35` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/34` | 0.894112 | **Rules Overview** |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/32` | 0.894112 | **Rules Overview** |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/7/Text/53` | 0.894112 | **Rules Overview** |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/5/Text/41` | 0.852112 | **Rules Overview** |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/9/Text/36` | 0.852112 | **Rules Overview** |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/12/SectionHeader/7` | 0.565362 | **DEATH AND DYING RULES** |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/14/SectionHeader/1` | 0.449031 | **PERSISTENT DAMAGE RULES** |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/13/Text/30` | 0.426714 | **INTRODUCTION** |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/15/Text/24` | 0.426714 | **INTRODUCTION** |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/7/Text/45` | 0.426714 | **INTRODUCTION** |

### Query 58
- Text: What is the rule about **Checks**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/35']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 424-441::/page/5/Text/42', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/35', 'PZO22001 Starfinder Player Core 424-441::/page/3/Text/33']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/35', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/36', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/34']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 424-441::/page/1/Text/36` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/1/Text/34` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/5/Text/42` | 0.767288 | **Checks** |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/35` | 0.767288 | **Checks** |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/33` | 0.767288 | **Checks** |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/7/Text/54` | 0.725288 | **Checks** |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/9/Text/37` | 0.725288 | **Checks** |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/34` | 0.476682 | **Rules Overview** |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/32` | 0.476682 | **Rules Overview** |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/5/Text/41` | 0.476682 | **Rules Overview** |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/7` | 0.475886 | Typically, you'll roll a Perception check to determine your  initiative—the more aware you are of your surroundings,  the more quickly you can respond. Sometimes, though, the  GM might call on you to |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/9/Text/36` | 0.464682 | **Rules Overview** |

### Query 59
- Text: What is the rule about **Damage Rolls**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/36']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/36', 'PZO22001 Starfinder Player Core 424-441::/page/3/Text/34', 'PZO22001 Starfinder Player Core 424-441::/page/5/Text/43']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/36', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/37', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/35']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 424-441::/page/1/Text/37` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/1/Text/35` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/36` | 0.900985 | **Damage Rolls** |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/34` | 0.900985 | **Damage Rolls** |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/5/Text/43` | 0.900985 | **Damage Rolls** |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/9/Text/38` | 0.858985 | **Damage Rolls** |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/7/Text/55` | 0.858985 | **Damage Rolls** |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/14/SectionHeader/1` | 0.595027 | **PERSISTENT DAMAGE RULES** |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/12/SectionHeader/7` | 0.491271 | **DEATH AND DYING RULES** |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/38` | 0.490898 | **Damage Types** |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/5/Text/45` | 0.490898 | **Damage Types** |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/7/Text/57` | 0.490898 | **Damage Types** |

### Query 60
- Text: Summarize **Immunity, ** **Weakness, & ** **Resistance**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/37']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/37', 'PZO22001 Starfinder Player Core 424-441::/page/3/Text/35', 'PZO22001 Starfinder Player Core 424-441::/page/5/Text/44']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/37', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/38', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/36']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 424-441::/page/1/Text/38` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/1/Text/36` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/37` | 1.020504 | **Immunity, ** **Weakness, & ** **Resistance** |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/35` | 1.020504 | **Immunity, ** **Weakness, & ** **Resistance** |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/5/Text/44` | 1.020504 | **Immunity, ** **Weakness, & ** **Resistance** |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/7/Text/56` | 0.978504 | **Immunity, ** **Weakness, & ** **Resistance** |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/9/Text/39` | 0.978504 | **Immunity, ** **Weakness, & ** **Resistance** |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/14/SectionHeader/11` | 0.865802 | **Immunities, Resistances, and Weaknesses** |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/14/Text/12` | 0.469750 | Immunities, resistances, and weaknesses all apply to  persistent damage. If an effect deals initial damage  in addition to persistent damage, apply immunities,  resistances, and weaknesses separately |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/11/Text/19` | 0.398086 | You don't have your wits about you, and you attack wildly.  You're off-guard, you don't treat anyone as your ally (though  they might still treat you as theirs), and you can't Delay,  Ready, or use re |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/13/Text/28` | 0.372236 | You're incapable of movement. You can't use any actions that  have the move trait. If you're immobilized by something holding  you in place and an external force would move you out of your  space, the |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/11/Text/1` | 0.370824 | While adventuring, characters (and sometimes their belongings) are affected by abilities and  effects that apply conditions. For example, a spell or magic item might turn you invisible or cause  you t |

### Query 61
- Text: What is the rule about **Damage Types**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/38']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 424-441::/page/7/Text/57', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/38', 'PZO22001 Starfinder Player Core 424-441::/page/5/Text/45']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/38', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/37', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/39']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 424-441::/page/1/Text/37` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/1/Text/39` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/7/Text/57` | 0.891010 | **Damage Types** |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/38` | 0.891010 | **Damage Types** |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/5/Text/45` | 0.891010 | **Damage Types** |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/36` | 0.849010 | **Damage Types** |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/9/Text/40` | 0.849010 | **Damage Types** |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/14/SectionHeader/1` | 0.607319 | **PERSISTENT DAMAGE RULES** |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/7/Text/55` | 0.508386 | **Damage Rolls** |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/34` | 0.508386 | **Damage Rolls** |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/9/Text/38` | 0.508386 | **Damage Rolls** |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/36` | 0.508386 | **Damage Rolls** |

### Query 62
- Text: What is the rule about **Hit Points, ** **Healing, and ** **Dying**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/39']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 424-441::/page/3/Text/37', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/39', 'PZO22001 Starfinder Player Core 424-441::/page/7/Text/58']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/39', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/38', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/40']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 424-441::/page/1/Text/38` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/1/Text/40` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/37` | 0.937527 | **Hit Points, ** **Healing, and ** **Dying** |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/39` | 0.937527 | **Hit Points, ** **Healing, and ** **Dying** |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/7/Text/58` | 0.937527 | **Hit Points, ** **Healing, and ** **Dying** |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/5/Text/46` | 0.895527 | **Hit Points, ** **Healing, and ** **Dying** |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/9/Text/41` | 0.895527 | **Hit Points, ** **Healing, and ** **Dying** |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/4/ListItem/9` | 0.561779 | Do anything else that's specified to happen at the start of  your turn, such as regaining Hit Points from fast healing  or regeneration. |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/12/Text/8` | 0.496542 | The doomed, dying, unconscious, and wounded  conditions all relate to the process of coming closer to  death. The full rules are on pages 402–403. The most  significant information not contained in th |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/16/ListItem/11` | 0.492662 | You take damage, though  if the damage reduces you  to 0 Hit Points, you remain  unconscious and gain the dying  condition as normal.  You receive healing, other  than the natural healing you  get fro |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/12/SectionHeader/7` | 0.491511 | **DEATH AND DYING RULES** |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/17/Text/24` | 0.469328 | The wounded condition ends if someone successfully  restores Hit Points to you using Treat Wounds, or if you  are restored to full Hit Points by any means and rest for 10  minutes. |

### Query 63
- Text: Summarize **Hero Points**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/40']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/40', 'PZO22001 Starfinder Player Core 424-441::/page/3/Text/38', 'PZO22001 Starfinder Player Core 424-441::/page/5/Text/47']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/40', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/41', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/39']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 424-441::/page/1/Text/41` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/1/Text/39` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/40` | 0.970595 | **Hero Points** |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/38` | 0.970595 | **Hero Points** |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/5/Text/47` | 0.970595 | **Hero Points** |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/7/Text/59` | 0.928595 | **Hero Points** |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/9/Text/42` | 0.928595 | **Hero Points** |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/39` | 0.469850 | **Hit Points, ** **Healing, and ** **Dying** |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/37` | 0.469850 | **Hit Points, ** **Healing, and ** **Dying** |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/5/Text/46` | 0.469850 | **Hit Points, ** **Healing, and ** **Dying** |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/9/Text/41` | 0.457850 | **Hit Points, ** **Healing, and ** **Dying** |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/7/Text/58` | 0.457850 | **Hit Points, ** **Healing, and ** **Dying** |

### Query 64
- Text: What is the rule about **Actions**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/41']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 424-441::/page/5/Text/48', 'PZO22001 Starfinder Player Core 424-441::/page/7/Text/60', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/41']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/41', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/42', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/40']
- Expanded expected found: `True`
- Expanded expected rank: `3`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 424-441::/page/1/Text/42` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/1/Text/40` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/5/Text/48` | 0.831891 | **Actions** |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/7/Text/60` | 0.831891 | **Actions** |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/41` | 0.831891 | **Actions** |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/39` | 0.789891 | **Actions** |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/9/Text/43` | 0.789891 | **Actions** |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/19` | 0.605118 | When it's your turn to act, you can use single actions ([one-action]),  short activities ([two-actions] and [three-actions]), reactions ([reaction]), and free actions  ([free-action]). When you're fin |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/4/Text/14` | 0.595896 | you from acting. If you can't act, you can't use any actions,  including reactions and free actions. |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/4/Text/13` | 0.570049 | You can use actions in any order you wish during your  turn, but you have to complete one action or activity before  beginning another; for example, you can't use a single action in  the middle of per |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/15/Text/16` | 0.533916 | Some conditions prevent you from taking a certain  subset of actions, typically reactions. Other conditions  simply say you can't act. When you can't act, you're  unable to take any actions at all. Un |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/15/SectionHeader/14` | 0.518532 | **GAINING AND LOSING ACTIONS** |

### Query 65
- Text: Summarize **Movement**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/42']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/42', 'PZO22001 Starfinder Player Core 424-441::/page/3/Text/40', 'PZO22001 Starfinder Player Core 424-441::/page/5/Text/49']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/42', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/43', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/41']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 424-441::/page/1/Text/43` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/1/Text/41` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/42` | 0.929132 | **Movement** |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/40` | 0.929132 | **Movement** |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/5/Text/49` | 0.929132 | **Movement** |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/7/Text/61` | 0.887132 | **Movement** |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/9/Text/44` | 0.887132 | **Movement** |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/17/SectionHeader/11` | 0.557307 | **MOVE** |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/7/SectionHeader/7` | 0.542652 | **EXPLORATION** **MOVE** |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/6/Text/12` | 0.441938 | than make steady progress toward your goal, you move at  the full travel speeds given in the table. |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/39` | 0.410771 | **Actions** |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/5/Text/48` | 0.410771 | **Actions** |

### Query 66
- Text: Summarize **Effects**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/43']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/43', 'PZO22001 Starfinder Player Core 424-441::/page/7/Text/62', 'PZO22001 Starfinder Player Core 424-441::/page/5/Text/50']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/43', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/42', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/44']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 424-441::/page/1/Text/42` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/1/Text/44` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/43` | 0.937642 | **Effects** |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/5/Text/50` | 0.937642 | **Effects** |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/7/Text/62` | 0.937642 | **Effects** |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/41` | 0.895642 | **Effects** |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/9/Text/45` | 0.742540 | **Effects** **Area** |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/8/SectionHeader/14` | 0.653759 | **SUSTAIN AN EFFECT** |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/9/Text/46` | 0.437616 | **Afflictions** |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/5/Text/52` | 0.437616 | **Afflictions** |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/9/Text/43` | 0.431589 | **Actions** |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/7/Text/60` | 0.431589 | **Actions** |

### Query 67
- Text: Summarize **Area** **Afflictions**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/44']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/44', 'PZO22001 Starfinder Player Core 424-441::/page/3/Text/42', 'PZO22001 Starfinder Player Core 424-441::/page/7/Text/63']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/44', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/45', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/43']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 424-441::/page/1/Text/45` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/1/Text/43` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/44` | 0.972537 | **Area** **Afflictions** |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/42` | 0.972537 | **Area** **Afflictions** |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/7/Text/63` | 0.972537 | **Area** **Afflictions** |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/9/Text/46` | 0.788756 | **Afflictions** |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/5/Text/52` | 0.788756 | **Afflictions** |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/9/Text/45` | 0.584278 | **Effects** **Area** |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/5/Text/51` | 0.557848 | **Area** |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/5/Text/45` | 0.419813 | **Damage Types** |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/36` | 0.419813 | **Damage Types** |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/38` | 0.419813 | **Damage Types** |

### Query 68
- Text: What is the rule about **Counteracting**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/45']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/45', 'PZO22001 Starfinder Player Core 424-441::/page/7/Text/64', 'PZO22001 Starfinder Player Core 424-441::/page/9/Text/47']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/45', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/46', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/44']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 424-441::/page/1/Text/46` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/1/Text/44` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/45` | 0.882936 | **Counteracting** |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/7/Text/64` | 0.882936 | **Counteracting** |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/9/Text/47` | 0.882936 | **Counteracting** |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/43` | 0.840936 | **Counteracting** |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/5/Text/53` | 0.701247 | **Counteracting** **Perception and ** |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/4/Text/14` | 0.427497 | you from acting. If you can't act, you can't use any actions,  including reactions and free actions. |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/12/Text/12` | 0.415357 | You've been commanded or magically dominated, or you  otherwise had your will subverted. The controller dictates  how you act and can make you use any of your actions,  including attacks, reactions, o |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/19` | 0.406783 | When it's your turn to act, you can use single actions ([one-action]),  short activities ([two-actions] and [three-actions]), reactions ([reaction]), and free actions  ([free-action]). When you're fin |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/32` | 0.402597 | **Rules Overview** |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/7/Text/53` | 0.402597 | **Rules Overview** |

### Query 69
- Text: Summarize **Perception and ** **Detection**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/46']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 424-441::/page/7/Text/65', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/46', 'PZO22001 Starfinder Player Core 424-441::/page/3/Text/44']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/46', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/45', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/47']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 424-441::/page/1/Text/45` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/1/Text/47` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/7/Text/65` | 0.992556 | **Perception and ** **Detection** |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/46` | 0.992556 | **Perception and ** **Detection** |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/44` | 0.992556 | **Perception and ** **Detection** |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/9/Text/48` | 0.950556 | **Perception and ** **Detection** |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/1` | 0.828482 | PERCEPTION AND  DETECTION |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/5/Text/53` | 0.726991 | **Counteracting** **Perception and ** |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/15` | 0.671811 | **DETECTING WITH OTHER SENSES** |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/2` | 0.637212 | Your Perception measures your ability to notice things, search for what's hidden, and tell whether  something about a situation is suspicious. |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/5/Text/54` | 0.614319 | **Detection** **Encounter ** |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/16` | 0.589446 | The ways a creature can use Perception depend on what  senses it has. The primary concepts you need to know for  understanding senses are precise senses, imprecise senses,  and the three states of det |

### Query 70
- Text: Summarize **Encounter ** **Mode**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/47']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/47', 'PZO22001 Starfinder Player Core 424-441::/page/3/Text/45', 'PZO22001 Starfinder Player Core 424-441::/page/7/Text/66']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/47', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/46', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/48']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 424-441::/page/1/Text/46` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/1/Text/48` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/47` | 0.996085 | **Encounter ** **Mode** |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/45` | 0.996085 | **Encounter ** **Mode** |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/7/Text/66` | 0.996085 | **Encounter ** **Mode** |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/9/Text/49` | 0.954085 | **Encounter ** **Mode** |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/5/Text/54` | 0.732350 | **Detection** **Encounter ** |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/46` | 0.650901 | **Exploration ** **Mode** |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/48` | 0.650901 | **Exploration ** **Mode** |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/7/Text/67` | 0.650901 | **Exploration ** **Mode** |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/9/Text/50` | 0.638901 | **Exploration ** **Mode** |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/5/Text/55` | 0.638901 | **Exploration ** **Mode** |

### Query 71
- Text: Summarize **Exploration ** **Mode**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/48']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/48', 'PZO22001 Starfinder Player Core 424-441::/page/3/Text/46', 'PZO22001 Starfinder Player Core 424-441::/page/5/Text/55']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/48', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/49', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/47']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 424-441::/page/1/Text/49` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/1/Text/47` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/48` | 0.983318 | **Exploration ** **Mode** |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/46` | 0.983318 | **Exploration ** **Mode** |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/5/Text/55` | 0.983318 | **Exploration ** **Mode** |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/9/Text/50` | 0.941318 | **Exploration ** **Mode** |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/7/Text/67` | 0.941318 | **Exploration ** **Mode** |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/6/SectionHeader/1` | 0.733077 | EXPLORATION MODE |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/6/SectionHeader/20` | 0.669003 | **EXPLORATION** |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/6/SectionHeader/23` | 0.669003 | **EXPLORATION** |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/5/Text/61` | 0.636681 | **Mode** |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/7/SectionHeader/7` | 0.617745 | **EXPLORATION** **MOVE** |

### Query 72
- Text: Summarize **Downtime ** **Mode**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/49']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 424-441::/page/9/Text/51', 'PZO22001 Starfinder Player Core 424-441::/page/7/Text/68', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/49']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/49', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/48', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/50']
- Expanded expected found: `True`
- Expanded expected rank: `3`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 424-441::/page/1/Text/48` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/1/Text/50` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/9/Text/51` | 0.972659 | **Downtime ** **Mode** |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/7/Text/68` | 0.972659 | **Downtime ** **Mode** |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/49` | 0.972659 | **Downtime ** **Mode** |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/47` | 0.930659 | **Downtime ** **Mode** |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/5/Text/56` | 0.930659 | **Downtime ** **Mode** |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/9/SectionHeader/0` | 0.615229 | DOWNTIME MODE |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/5/Text/61` | 0.567110 | **Mode** |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/9/Text/1` | 0.543402 | Downtime mode is played day-by-day rather than minute-by-minute or scene-by-scene. Usually,  this mode of play occurs when you're in the safety of a settlement, maybe recovering from your  adventures |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/48` | 0.530051 | **Exploration ** **Mode** |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/7/Text/67` | 0.530051 | **Exploration ** **Mode** |

### Query 73
- Text: Summarize **CONDITIONS ** **APPENDIX**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/50']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 424-441::/page/15/Text/31', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/50', 'PZO22001 Starfinder Player Core 424-441::/page/3/Text/48']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/50', 'PZO22001 Starfinder Player Core 424-441::/page/13/Text/38', 'PZO22001 Starfinder Player Core 424-441::/page/11/Text/31', 'PZO22001 Starfinder Player Core 424-441::/page/5/Text/57', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/49', 'PZO22001 Starfinder Player Core 424-441::/page/15/Text/31', 'PZO22001 Starfinder Player Core 424-441::/page/9/Text/52', 'PZO22001 Starfinder Player Core 424-441::/page/3/Text/48', 'PZO22001 Starfinder Player Core 424-441::/page/7/Text/69', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/51']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 424-441::/page/13/Text/38` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/11/Text/31` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/5/Text/57` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/1/Text/49` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/15/Text/31` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/9/Text/52` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/3/Text/48` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/7/Text/69` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/1/Text/51` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/15/Text/31` | 0.983499 | **CONDITIONS ** **APPENDIX** |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/50` | 0.983499 | **CONDITIONS ** **APPENDIX** |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/48` | 0.983499 | **CONDITIONS ** **APPENDIX** |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/13/Text/38` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/5/Text/57` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/9/Text/52` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/7/Text/69` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/11/Text/31` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/11/SectionHeader/0` | 0.837763 | CONDITIONS APPENDIX |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/17/Text/34` | 0.573689 | **APPENDIX** **GLOSSARY & ** |

### Query 74
- Text: Summarize **GLOSSARY & ** **INDEX**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/51']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/51', 'PZO22001 Starfinder Player Core 424-441::/page/13/Text/39', 'PZO22001 Starfinder Player Core 424-441::/page/3/Text/49']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/51', 'PZO22001 Starfinder Player Core 424-441::/page/2/Text/1', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/50']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 424-441::/page/2/Text/1` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/1/Text/50` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/51` | 0.993465 | **GLOSSARY & ** **INDEX** |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/13/Text/39` | 0.993465 | **GLOSSARY & ** **INDEX** |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/49` | 0.993465 | **GLOSSARY & ** **INDEX** |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/5/Text/58` | 0.951465 | **GLOSSARY & ** **INDEX** |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/7/Text/70` | 0.951465 | **GLOSSARY & ** **INDEX** |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/9/Text/53` | 0.951465 | **GLOSSARY & ** **INDEX** |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/11/Text/32` | 0.832530 | **GLOSSARY & ** **INDEX** **CHARACTER ** |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/15/Text/32` | 0.832530 | **GLOSSARY & ** **INDEX** **CHARACTER ** |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/17/Text/34` | 0.697531 | **APPENDIX** **GLOSSARY & ** |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/17/Text/35` | 0.434384 | **INDEX** **CHARACTER ** **SHEET** |

### Query 75
- Text: What is the rule about Targeting an undetected creature is difficult. If you suspect  there's a creature around, you can pick a square and attempt  an attack. This works like targeting a hidden creature, but the  flat check and attack roll are both rolled in secret by the GM.  The GM won't tell you why you missed—whether it was due  to failing the flat check, rolling an insufficient attack roll, or  choosing the wrong square. The GM might allow you to try  targeting an undetected creature with some spells or other  abilities in a similar fashion. Undetected creatures are subject  to area effects normally.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/2/Text/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 424-441::/page/2/Text/1', 'PZO22001 Starfinder Player Core 424-441::/page/17/Text/3', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/22']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/2/Text/1', 'PZO22001 Starfinder Player Core 424-441::/page/2/Text/2', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/51']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 424-441::/page/2/Text/2` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/1/Text/51` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/2/Text/1` | 1.019324 | Targeting an undetected creature is difficult. If you suspect  there's a creature around, you can pick a square and attempt  an attack. This works like targeting a hidden creature, but the  flat check |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/17/Text/3` | 0.901146 | A creature you're undetected by can guess which square  you're in to try targeting you. It must pick a square and  attempt an attack. This works like targeting a hidden  creature (requiring a DC 11 fl |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/22` | 0.763445 | When targeting a hidden creature, before you roll to  determine your effect, you must attempt a DC 11 flat check.  If you fail, you don't affect the creature, though the actions  you used are still ex |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/17/Text/2` | 0.671634 | When you're undetected by a creature, that creature can't  see you at all, has no idea what space you occupy, and can't  target you, though you still can be affected by abilities that  target an area. |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/24` | 0.669172 | If a creature is undetected, you don't know what space it  occupies and you're off-guard to it. The Seek basic action can  help you find an undetected creature, usually making it hidden  from you inst |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/11/Text/17` | 0.657534 | You're difficult for one or more creatures to see due to thick  fog or some other obscuring feature. You can be concealed  to some creatures but not others. While concealed, you can  still be observed |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/13/Text/23` | 0.654174 | While you're hidden from a creature, that creature knows  the space you're in but can't tell precisely where you are.  You typically become hidden by using Stealth to Hide. When  Seeking a creature us |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/2/Text/4` | 0.650379 | If you have no idea a creature is even present, that creature  is unnoticed by you. A creature that's undetected might also  be unnoticed. This condition usually matters for abilities  that can be use |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/2/Text/2` | 0.642210 | For instance, suppose an enemy witchwarper cast  *invisibility* and then Sneaked away. You suspect that with  the witchwarper's Speed of 25 feet, they probably moved 15  feet toward an open door. You |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/17/Text/7` | 0.638676 | If you're unnoticed by a creature, that creature has no  idea you're present. When you're unnoticed, you're also  undetected. This matters for abilities that can be used only  against targets totally |

### Query 76
- Text: What is the rule about For instance, suppose an enemy witchwarper cast  *invisibility* and then Sneaked away. You suspect that with  the witchwarper's Speed of 25 feet, they probably moved 15  feet toward an open door. You move up and attack a space 15  feet from where the witchwarper started and directly on the  path to the door. The GM secretly rolls an attack roll and flat  check, but they know that you weren't quite correct—your foe  was actually in the adjacent space! The GM tells you that you  missed, so you decide to make your next attack on the adjacent  space, just in case. This time, it's the right space, and the GM's  secret attack roll and flat check both succeed, so you hit!?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/2/Text/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 424-441::/page/2/Text/2', 'PZO22001 Starfinder Player Core 424-441::/page/17/Text/3', 'PZO22001 Starfinder Player Core 424-441::/page/2/Text/1']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/2/Text/2', 'PZO22001 Starfinder Player Core 424-441::/page/2/SectionHeader/3', 'PZO22001 Starfinder Player Core 424-441::/page/2/Text/1']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 424-441::/page/2/SectionHeader/3` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/2/Text/1` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/2/Text/2` | 0.996893 | For instance, suppose an enemy witchwarper cast  *invisibility* and then Sneaked away. You suspect that with  the witchwarper's Speed of 25 feet, they probably moved 15  feet toward an open door. You |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/17/Text/3` | 0.668479 | A creature you're undetected by can guess which square  you're in to try targeting you. It must pick a square and  attempt an attack. This works like targeting a hidden  creature (requiring a DC 11 fl |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/2/Text/1` | 0.651835 | Targeting an undetected creature is difficult. If you suspect  there's a creature around, you can pick a square and attempt  an attack. This works like targeting a hidden creature, but the  flat check |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/13/Text/23` | 0.606200 | While you're hidden from a creature, that creature knows  the space you're in but can't tell precisely where you are.  You typically become hidden by using Stealth to Hide. When  Seeking a creature us |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/22` | 0.579002 | When targeting a hidden creature, before you roll to  determine your effect, you must attempt a DC 11 flat check.  If you fail, you don't affect the creature, though the actions  you used are still ex |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/2/Text/8` | 0.571807 | A creature with the invisible condition (by way of an  *invisibility* spell, for example) is automatically undetected  to any creatures relying on sight as their only precise  sense. Precise senses ot |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/11` | 0.561731 | Typically, the GM tracks how well creatures detect each  other since neither party has perfect information. For  example, you might think a creature is in the last place  you sensed it, but it was abl |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/6/Text/21` | 0.555560 | You attempt a Stealth check to avoid notice while traveling  at half speed. If you're Avoiding Notice at the start of an  encounter, you usually roll a Stealth check instead of a  Perception check bot |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/10` | 0.553018 | With the exception of invisible, these conditions are  relative to the viewer—it's possible for a creature to be  observed to you but hidden from your ally. Most of these  rules apply to objects as we |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/21` | 0.552533 | A creature that's hidden is only barely perceptible. You only  know what space it occupies. Perhaps the creature just used  the Hide action. Your target might be behind some obstruction,  where you ca |

### Query 77
- Text: Summarize UNNOTICED
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/2/SectionHeader/3']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 424-441::/page/17/SectionHeader/6', 'PZO22001 Starfinder Player Core 424-441::/page/2/SectionHeader/3', 'PZO22001 Starfinder Player Core 424-441::/page/17/Text/7']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/2/SectionHeader/3', 'PZO22001 Starfinder Player Core 424-441::/page/2/Text/2', 'PZO22001 Starfinder Player Core 424-441::/page/2/Text/4']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 424-441::/page/2/Text/2` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/2/Text/4` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/17/SectionHeader/6` | 0.914859 | UNNOTICED |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/2/SectionHeader/3` | 0.914859 | UNNOTICED |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/17/Text/7` | 0.525055 | If you're unnoticed by a creature, that creature has no  idea you're present. When you're unnoticed, you're also  undetected. This matters for abilities that can be used only  against targets totally |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/2/Text/4` | 0.485560 | If you have no idea a creature is even present, that creature  is unnoticed by you. A creature that's undetected might also  be unnoticed. This condition usually matters for abilities  that can be use |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/17/SectionHeader/1` | 0.466589 | UNDETECTED |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/23` | 0.466589 | UNDETECTED |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/20` | 0.434838 | HIDDEN |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/13/SectionHeader/22` | 0.434838 | HIDDEN |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/17/SectionHeader/8` | 0.432668 | UNTETHERED |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/24` | 0.428629 | If a creature is undetected, you don't know what space it  occupies and you're off-guard to it. The Seek basic action can  help you find an undetected creature, usually making it hidden  from you inst |

### Query 78
- Text: Summarize If you have no idea a creature is even present, that creature  is unnoticed by you. A creature that's undetected might also  be unnoticed. This condition usually matters for abilities  that can be used only against targets totally unaware of  your presence.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/2/Text/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 424-441::/page/2/Text/4', 'PZO22001 Starfinder Player Core 424-441::/page/17/Text/7', 'PZO22001 Starfinder Player Core 424-441::/page/17/Text/2']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/2/Text/4', 'PZO22001 Starfinder Player Core 424-441::/page/2/SectionHeader/3', 'PZO22001 Starfinder Player Core 424-441::/page/2/SectionHeader/5']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 424-441::/page/2/SectionHeader/3` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/2/SectionHeader/5` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/2/Text/4` | 1.044172 | If you have no idea a creature is even present, that creature  is unnoticed by you. A creature that's undetected might also  be unnoticed. This condition usually matters for abilities  that can be use |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/17/Text/7` | 1.006943 | If you're unnoticed by a creature, that creature has no  idea you're present. When you're unnoticed, you're also  undetected. This matters for abilities that can be used only  against targets totally |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/17/Text/2` | 0.852189 | When you're undetected by a creature, that creature can't  see you at all, has no idea what space you occupy, and can't  target you, though you still can be affected by abilities that  target an area. |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/24` | 0.767895 | If a creature is undetected, you don't know what space it  occupies and you're off-guard to it. The Seek basic action can  help you find an undetected creature, usually making it hidden  from you inst |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/2/Text/8` | 0.732979 | A creature with the invisible condition (by way of an  *invisibility* spell, for example) is automatically undetected  to any creatures relying on sight as their only precise  sense. Precise senses ot |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/9` | 0.714738 | Three conditions measure the degree to which you can sense  a creature: observed, hidden, and undetected. However, the  concealed and invisible conditions can partially mask a  creature, and the unnot |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/14` | 0.713669 | In most circumstances, you can sense creatures without  difficulty and target them normally. Creatures in this state  are observed. Observing requires a precise sense, which for  most creatures means |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/14/Text/18` | 0.708248 | You can't be seen. You're undetected to everyone. Creatures  can Seek to detect you; if a creature succeeds at its Perception  check against your Stealth DC, you become hidden to that  creature until |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/10` | 0.694638 | With the exception of invisible, these conditions are  relative to the viewer—it's possible for a creature to be  observed to you but hidden from your ally. Most of these  rules apply to objects as we |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/14/Text/20` | 0.673309 | Anything in plain view is observed by you. If a creature takes  measures to avoid detection, such as by using Stealth to Hide,  it can become hidden or undetected instead of observed. If you |

### Query 79
- Text: What is the rule about A concealed creature is in mist, within dim light, or amid  something else that obscures sight but isn't a physical  barrier. When you target a creature that's concealed  from you, you must attempt a DC 5 flat check before  you roll to determine your effect. If you fail, you don't  affect the target. The concealed condition doesn't change  which of the main categories of detection apply. A  creature in a light fog bank is still observed even though  it's concealed.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/2/Text/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 424-441::/page/2/Text/6', 'PZO22001 Starfinder Player Core 424-441::/page/11/Text/17', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/22']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/2/Text/6', 'PZO22001 Starfinder Player Core 424-441::/page/2/SectionHeader/7', 'PZO22001 Starfinder Player Core 424-441::/page/2/SectionHeader/5']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 424-441::/page/2/SectionHeader/7` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/2/SectionHeader/5` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/2/Text/6` | 1.010722 | A concealed creature is in mist, within dim light, or amid  something else that obscures sight but isn't a physical  barrier. When you target a creature that's concealed  from you, you must attempt a |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/11/Text/17` | 0.860513 | You're difficult for one or more creatures to see due to thick  fog or some other obscuring feature. You can be concealed  to some creatures but not others. While concealed, you can  still be observed |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/22` | 0.731987 | When targeting a hidden creature, before you roll to  determine your effect, you must attempt a DC 11 flat check.  If you fail, you don't affect the creature, though the actions  you used are still ex |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/14` | 0.685486 | In most circumstances, you can sense creatures without  difficulty and target them normally. Creatures in this state  are observed. Observing requires a precise sense, which for  most creatures means |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/13/Text/23` | 0.654342 | While you're hidden from a creature, that creature knows  the space you're in but can't tell precisely where you are.  You typically become hidden by using Stealth to Hide. When  Seeking a creature us |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/12` | 0.651344 | Areas in shadow or lit by weak light sources are in dim  light. Creatures and objects in dim light have the concealed  condition, unless the seeker has darkvision or low-light vision  (page 425), or a |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/14` | 0.647677 | A creature or object within darkness is hidden or undetected  unless the seeker has darkvision or a precise sense other  than vision. A creature without darkvision or another means  of perceiving in d |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/10` | 0.634827 | With the exception of invisible, these conditions are  relative to the viewer—it's possible for a creature to be  observed to you but hidden from your ally. Most of these  rules apply to objects as we |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/3` | 0.632978 | A creature with low-light vision can see in dim light as though  it were bright light, so it ignores the concealed condition due  to dim light. |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/14/Text/18` | 0.629346 | You can't be seen. You're undetected to everyone. Creatures  can Seek to detect you; if a creature succeeds at its Perception  check against your Stealth DC, you become hidden to that  creature until |

### Query 80
- Text: What is the rule about A creature with the invisible condition (by way of an  *invisibility* spell, for example) is automatically undetected  to any creatures relying on sight as their only precise  sense. Precise senses other than sight ignore the invisible  condition. You can Seek (page 409) to attempt to figure out  an invisible creature's location, making it only hidden from  you. This lasts until the invisible creature successfully  uses Sneak to become undetected again. If you're already  observing a creature when it becomes invisible, it starts  out hidden since you know where it was, though it can  then Sneak to become undetected.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/2/Text/8']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 424-441::/page/2/Text/8', 'PZO22001 Starfinder Player Core 424-441::/page/14/Text/18', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/24']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/2/Text/8', 'PZO22001 Starfinder Player Core 424-441::/page/2/SectionHeader/7', 'PZO22001 Starfinder Player Core 424-441::/page/2/Text/9']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 424-441::/page/2/SectionHeader/7` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/2/Text/9` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/2/Text/8` | 1.007620 | A creature with the invisible condition (by way of an  *invisibility* spell, for example) is automatically undetected  to any creatures relying on sight as their only precise  sense. Precise senses ot |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/14/Text/18` | 0.847031 | You can't be seen. You're undetected to everyone. Creatures  can Seek to detect you; if a creature succeeds at its Perception  check against your Stealth DC, you become hidden to that  creature until |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/24` | 0.775375 | If a creature is undetected, you don't know what space it  occupies and you're off-guard to it. The Seek basic action can  help you find an undetected creature, usually making it hidden  from you inst |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/14` | 0.731452 | In most circumstances, you can sense creatures without  difficulty and target them normally. Creatures in this state  are observed. Observing requires a precise sense, which for  most creatures means |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/2/Text/4` | 0.726448 | If you have no idea a creature is even present, that creature  is unnoticed by you. A creature that's undetected might also  be unnoticed. This condition usually matters for abilities  that can be use |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/10` | 0.722281 | With the exception of invisible, these conditions are  relative to the viewer—it's possible for a creature to be  observed to you but hidden from your ally. Most of these  rules apply to objects as we |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/17/Text/7` | 0.720729 | If you're unnoticed by a creature, that creature has no  idea you're present. When you're unnoticed, you're also  undetected. This matters for abilities that can be used only  against targets totally |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/14/Text/20` | 0.719553 | Anything in plain view is observed by you. If a creature takes  measures to avoid detection, such as by using Stealth to Hide,  it can become hidden or undetected instead of observed. If you |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/13/Text/23` | 0.713976 | While you're hidden from a creature, that creature knows  the space you're in but can't tell precisely where you are.  You typically become hidden by using Stealth to Hide. When  Seeking a creature us |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/14/Text/21` | 0.711839 | have another precise sense besides sight, you might be able  to observe a creature or object using that sense instead. You  can observe a creature with only your precise senses. When  Seeking a creatu |

### Query 81
- Text: What is the rule about Other effects might partially foil invisibility. For instance,  if you were tracking an invisible creature's footprints through  the snow, the footprints would make it hidden. Throwing a  net over an invisible creature would make it observed but  concealed for as long as the net is on it.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/2/Text/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 424-441::/page/2/Text/9', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/10', 'PZO22001 Starfinder Player Core 424-441::/page/2/Text/6']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/2/Text/9', 'PZO22001 Starfinder Player Core 424-441::/page/2/Text/8', 'PZO22001 Starfinder Player Core 424-441::/page/3/SectionHeader/0']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 424-441::/page/2/Text/8` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/3/SectionHeader/0` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/2/Text/9` | 0.989960 | Other effects might partially foil invisibility. For instance,  if you were tracking an invisible creature's footprints through  the snow, the footprints would make it hidden. Throwing a  net over an |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/10` | 0.728700 | With the exception of invisible, these conditions are  relative to the viewer—it's possible for a creature to be  observed to you but hidden from your ally. Most of these  rules apply to objects as we |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/2/Text/6` | 0.652636 | A concealed creature is in mist, within dim light, or amid  something else that obscures sight but isn't a physical  barrier. When you target a creature that's concealed  from you, you must attempt a |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/2/Text/8` | 0.611966 | A creature with the invisible condition (by way of an  *invisibility* spell, for example) is automatically undetected  to any creatures relying on sight as their only precise  sense. Precise senses ot |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/14/Text/20` | 0.608103 | Anything in plain view is observed by you. If a creature takes  measures to avoid detection, such as by using Stealth to Hide,  it can become hidden or undetected instead of observed. If you |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/14` | 0.594993 | In most circumstances, you can sense creatures without  difficulty and target them normally. Creatures in this state  are observed. Observing requires a precise sense, which for  most creatures means |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/11/Text/17` | 0.591979 | You're difficult for one or more creatures to see due to thick  fog or some other obscuring feature. You can be concealed  to some creatures but not others. While concealed, you can  still be observed |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/9` | 0.580974 | Three conditions measure the degree to which you can sense  a creature: observed, hidden, and undetected. However, the  concealed and invisible conditions can partially mask a  creature, and the unnot |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/2/Text/4` | 0.571881 | If you have no idea a creature is even present, that creature  is unnoticed by you. A creature that's undetected might also  be unnoticed. This condition usually matters for abilities  that can be use |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/14/Text/18` | 0.563724 | You can't be seen. You're undetected to everyone. Creatures  can Seek to detect you; if a creature succeeds at its Perception  check against your Stealth DC, you become hidden to that  creature until |

### Query 82
- Text: What is the rule about When every individual action counts, you enter the encounter mode of play. In this mode, time  is divided into rounds, each of which is 6 seconds of time in the game world. Every round, each  participant takes a turn in an established order. During your turn, you can use actions, and depending  on the details of the encounter, you might have the opportunity to use reactions and free actions on  your own turn and on others' turns.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/3/Text/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 424-441::/page/3/Text/1', 'PZO22001 Starfinder Player Core 424-441::/page/3/Text/4', 'PZO22001 Starfinder Player Core 424-441::/page/3/Text/19']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/3/Text/1', 'PZO22001 Starfinder Player Core 424-441::/page/3/SectionHeader/3', 'PZO22001 Starfinder Player Core 424-441::/page/3/SectionHeader/0']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 424-441::/page/3/SectionHeader/3` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/3/SectionHeader/0` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/1` | 0.970651 | When every individual action counts, you enter the encounter mode of play. In this mode, time  is divided into rounds, each of which is 6 seconds of time in the game world. Every round, each  particip |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/4` | 0.774940 | An encounter is played out in a series of rounds, during which  the player characters, adversaries, and other participants in the  encounter act in sequence. You roll initiative to determine this  ord |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/19` | 0.719220 | When it's your turn to act, you can use single actions ([one-action]),  short activities ([two-actions] and [three-actions]), reactions ([reaction]), and free actions  ([free-action]). When you're fin |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/4/Text/26` | 0.657870 | Your reactions let you respond immediately to what's  happening around you. The GM determines whether you can  use reactions before your first turn begins, depending on the  situation in which the enc |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/13` | 0.624935 | A round begins when the participant with the highest  initiative roll result starts their turn, and it ends when the  one with the lowest initiative ends their turn. The process  of taking a turn is d |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/15` | 0.618875 | Once everyone in the encounter has taken a turn, the round  is over and the next one begins. Don't roll initiative again; the  new round proceeds in the same order as the previous one,  repeating the |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/4/Text/24` | 0.616175 | Activities that take longer than a turn can't normally be  performed during an encounter. Spells with a casting time of  1 minute or more are a common example, as are several skill  actions. When you |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/21` | 0.610388 | Many things happen automatically at the start of your turn it's a common point for tracking the passage of time for  effects that last multiple rounds. At the start of each of your  turns, take these |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/17` | 0.592691 | When your foes are defeated, some sort of truce is reached,  or some other event or circumstance ends the combat, the  encounter is over. You and the other participants no longer  follow the initiativ |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/4/Text/16` | 0.586986 | Once you've spent all three of your actions, your turn ends  (as described in Step 3) and the next creature's turn begins. You  can choose to end your turn early, losing all remaining actions  (but no |

### Query 83
- Text: What is the rule about An encounter is played out in a series of rounds, during which  the player characters, adversaries, and other participants in the  encounter act in sequence. You roll initiative to determine this  order at the start of the encounter and then play through rounds  until a conclusion is reached and the encounter ends. The rules  in this section assume a combat encounter—a battle—but the  general structure can apply to any kind of encounter. Other  types of encounters, like social encounters, might use longer  rounds or have other modifications to the basic structure.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/3/Text/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 424-441::/page/3/Text/4', 'PZO22001 Starfinder Player Core 424-441::/page/3/Text/1', 'PZO22001 Starfinder Player Core 424-441::/page/3/Text/15']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/3/Text/4', 'PZO22001 Starfinder Player Core 424-441::/page/3/SectionHeader/5', 'PZO22001 Starfinder Player Core 424-441::/page/3/SectionHeader/3']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 424-441::/page/3/SectionHeader/5` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/3/SectionHeader/3` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/4` | 1.002205 | An encounter is played out in a series of rounds, during which  the player characters, adversaries, and other participants in the  encounter act in sequence. You roll initiative to determine this  ord |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/1` | 0.764467 | When every individual action counts, you enter the encounter mode of play. In this mode, time  is divided into rounds, each of which is 6 seconds of time in the game world. Every round, each  particip |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/15` | 0.744205 | Once everyone in the encounter has taken a turn, the round  is over and the next one begins. Don't roll initiative again; the  new round proceeds in the same order as the previous one,  repeating the |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/6` | 0.687644 | When the GM calls for it, you'll roll initiative to determine  your place in the initiative order, which is the sequence in  which the encounter's participants will take their turns.  Rolling initiati |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/9` | 0.651386 | Unlike a check, where the result is compared to a DC, the  results of initiative rolls are ranked. This ranking sets the  order in which the encounter's participants act—the initiative  order. The cha |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/17` | 0.637952 | When your foes are defeated, some sort of truce is reached,  or some other event or circumstance ends the combat, the  encounter is over. You and the other participants no longer  follow the initiativ |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/4/Text/24` | 0.632787 | Activities that take longer than a turn can't normally be  performed during an encounter. Spells with a casting time of  1 minute or more are a common example, as are several skill  actions. When you |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/13` | 0.631646 | A round begins when the participant with the highest  initiative roll result starts their turn, and it ends when the  one with the lowest initiative ends their turn. The process  of taking a turn is d |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/19` | 0.628329 | When it's your turn to act, you can use single actions ([one-action]),  short activities ([two-actions] and [three-actions]), reactions ([reaction]), and free actions  ([free-action]). When you're fin |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/8` | 0.622799 | The GM rolls initiative for anyone other than the player  characters in the encounter. If these include a number of  identical creatures, the GM could roll once for the group as a  whole and have them |

### Query 84
- Text: What is the rule about STEP 1: ROLL INITIATIVE?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/3/SectionHeader/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 424-441::/page/3/SectionHeader/5', 'PZO22001 Starfinder Player Core 424-441::/page/3/Text/6', 'PZO22001 Starfinder Player Core 424-441::/page/3/Text/15']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/3/SectionHeader/5', 'PZO22001 Starfinder Player Core 424-441::/page/3/Text/4', 'PZO22001 Starfinder Player Core 424-441::/page/3/Text/6']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 424-441::/page/3/Text/4` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/3/Text/6` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/3/SectionHeader/5` | 0.920074 | STEP 1: ROLL INITIATIVE |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/6` | 0.640585 | When the GM calls for it, you'll roll initiative to determine  your place in the initiative order, which is the sequence in  which the encounter's participants will take their turns.  Rolling initiati |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/15` | 0.581697 | Once everyone in the encounter has taken a turn, the round  is over and the next one begins. Don't roll initiative again; the  new round proceeds in the same order as the previous one,  repeating the |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/3/SectionHeader/12` | 0.519730 | STEP 2: PLAY A ROUND |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/9` | 0.511891 | Unlike a check, where the result is compared to a DC, the  results of initiative rolls are ranked. This ranking sets the  order in which the encounter's participants act—the initiative  order. The cha |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/8` | 0.488494 | The GM rolls initiative for anyone other than the player  characters in the encounter. If these include a number of  identical creatures, the GM could roll once for the group as a  whole and have them |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/13` | 0.481216 | A round begins when the participant with the highest  initiative roll result starts their turn, and it ends when the  one with the lowest initiative ends their turn. The process  of taking a turn is d |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/3/SectionHeader/14` | 0.478224 | STEP 3: BEGIN THE NEXT ROUND |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/6` | 0.457077 | Perception is frequently used for rolling initiative in an  encounter, and for the Seek action. See page 396 for the  procedure for rolling a Perception check. |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/4` | 0.447504 | An encounter is played out in a series of rounds, during which  the player characters, adversaries, and other participants in the  encounter act in sequence. You roll initiative to determine this  ord |

### Query 85
- Text: What is the rule about When the GM calls for it, you'll roll initiative to determine  your place in the initiative order, which is the sequence in  which the encounter's participants will take their turns.  Rolling initiative marks the start of an encounter. More often  than not, you'll roll initiative when you enter a battle.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/3/Text/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 424-441::/page/3/Text/6', 'PZO22001 Starfinder Player Core 424-441::/page/3/Text/9', 'PZO22001 Starfinder Player Core 424-441::/page/3/Text/15']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/3/Text/6', 'PZO22001 Starfinder Player Core 424-441::/page/3/SectionHeader/5', 'PZO22001 Starfinder Player Core 424-441::/page/3/Text/7']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 424-441::/page/3/SectionHeader/5` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/3/Text/7` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/6` | 1.005580 | When the GM calls for it, you'll roll initiative to determine  your place in the initiative order, which is the sequence in  which the encounter's participants will take their turns.  Rolling initiati |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/9` | 0.768565 | Unlike a check, where the result is compared to a DC, the  results of initiative rolls are ranked. This ranking sets the  order in which the encounter's participants act—the initiative  order. The cha |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/15` | 0.763562 | Once everyone in the encounter has taken a turn, the round  is over and the next one begins. Don't roll initiative again; the  new round proceeds in the same order as the previous one,  repeating the |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/8` | 0.724100 | The GM rolls initiative for anyone other than the player  characters in the encounter. If these include a number of  identical creatures, the GM could roll once for the group as a  whole and have them |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/4` | 0.692566 | An encounter is played out in a series of rounds, during which  the player characters, adversaries, and other participants in the  encounter act in sequence. You roll initiative to determine this  ord |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/10` | 0.648365 | If your result is tied with an enemy's result, the enemy  goes first. If your result is tied with another PC's, you can  decide between yourselves who goes first when you reach  that place in the init |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/4/Text/2` | 0.638860 | The GM keeps track of the initiative order for an  encounter. It's usually okay for the players to know  this order since they'll see who goes when and be  aware of one another's results. However, the |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/13` | 0.636983 | A round begins when the participant with the highest  initiative roll result starts their turn, and it ends when the  one with the lowest initiative ends their turn. The process  of taking a turn is d |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/6` | 0.611954 | Perception is frequently used for rolling initiative in an  encounter, and for the Seek action. See page 396 for the  procedure for rolling a Perception check. |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/11` | 0.611813 | initiative order usually don't change during the encounter.  (But see the Delay basic action on page 408.) |

### Query 86
- Text: What is the rule about Typically, you'll roll a Perception check to determine your  initiative—the more aware you are of your surroundings,  the more quickly you can respond. Sometimes, though, the  GM might call on you to roll some other type of check. For  instance, if you were Avoiding Notice during exploration  (page 430), you'd roll a Stealth check. A social encounter  could call for a Deception or Diplomacy check. In most cases,  you can still use Perception if you prefer.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/3/Text/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 424-441::/page/3/Text/7', 'PZO22001 Starfinder Player Core 424-441::/page/6/Text/21', 'PZO22001 Starfinder Player Core 424-441::/page/0/Text/6']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/3/Text/7', 'PZO22001 Starfinder Player Core 424-441::/page/3/Text/8', 'PZO22001 Starfinder Player Core 424-441::/page/3/Text/6']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 424-441::/page/3/Text/8` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/3/Text/6` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/7` | 1.021033 | Typically, you'll roll a Perception check to determine your  initiative—the more aware you are of your surroundings,  the more quickly you can respond. Sometimes, though, the  GM might call on you to |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/6/Text/21` | 0.825996 | You attempt a Stealth check to avoid notice while traveling  at half speed. If you're Avoiding Notice at the start of an  encounter, you usually roll a Stealth check instead of a  Perception check bot |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/6` | 0.812378 | Perception is frequently used for rolling initiative in an  encounter, and for the Seek action. See page 396 for the  procedure for rolling a Perception check. |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/19` | 0.642831 | In some cases, rolling a Dexterity-based Stealth  skill check to Sneak doesn't make the most sense.  For example, a PC trying to avoid being detected by  a creature that senses heartbeats might medita |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/2` | 0.609637 | Your Perception measures your ability to notice things, search for what's hidden, and tell whether  something about a situation is suspicious. |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/11` | 0.600418 | Typically, the GM tracks how well creatures detect each  other since neither party has perfect information. For  example, you might think a creature is in the last place  you sensed it, but it was abl |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/12` | 0.592845 | You can attempt to avoid detection by using the Stealth  skill (page 207) to Avoid Notice, Hide, or Sneak, or by using  Deception to Create a Diversion (page 198). |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/6` | 0.591975 | When the GM calls for it, you'll roll initiative to determine  your place in the initiative order, which is the sequence in  which the encounter's participants will take their turns.  Rolling initiati |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/13/Text/2` | 0.589934 | You're compelled to focus your attention on something,  distracting you from whatever else is going on around you. You  take a –2 status penalty to Perception and skill checks, and you  can't use conc |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/12/Text/16` | 0.587995 | You can't hear. You automatically critically fail Perception  checks that require you to be able to hear. You take a –2 status  penalty to Perception checks for initiative and checks that  involve sou |

### Query 87
- Text: What is the rule about The GM rolls initiative for anyone other than the player  characters in the encounter. If these include a number of  identical creatures, the GM could roll once for the group as a  whole and have them take their turns within the group in any  order. However, this can make battles less predictable and more  dangerous, so the GM might want to roll initiative for some or  all creatures individually unless it's too much of a burden.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/3/Text/8']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 424-441::/page/3/Text/8', 'PZO22001 Starfinder Player Core 424-441::/page/3/Text/6', 'PZO22001 Starfinder Player Core 424-441::/page/3/Text/15']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/3/Text/8', 'PZO22001 Starfinder Player Core 424-441::/page/3/Text/9', 'PZO22001 Starfinder Player Core 424-441::/page/3/Text/7']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 424-441::/page/3/Text/9` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/3/Text/7` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/8` | 1.002188 | The GM rolls initiative for anyone other than the player  characters in the encounter. If these include a number of  identical creatures, the GM could roll once for the group as a  whole and have them |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/6` | 0.723081 | When the GM calls for it, you'll roll initiative to determine  your place in the initiative order, which is the sequence in  which the encounter's participants will take their turns.  Rolling initiati |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/15` | 0.695365 | Once everyone in the encounter has taken a turn, the round  is over and the next one begins. Don't roll initiative again; the  new round proceeds in the same order as the previous one,  repeating the |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/4/Text/2` | 0.623031 | The GM keeps track of the initiative order for an  encounter. It's usually okay for the players to know  this order since they'll see who goes when and be  aware of one another's results. However, the |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/9` | 0.616960 | Unlike a check, where the result is compared to a DC, the  results of initiative rolls are ranked. This ranking sets the  order in which the encounter's participants act—the initiative  order. The cha |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/4` | 0.605774 | An encounter is played out in a series of rounds, during which  the player characters, adversaries, and other participants in the  encounter act in sequence. You roll initiative to determine this  ord |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/13` | 0.567816 | A round begins when the participant with the highest  initiative roll result starts their turn, and it ends when the  one with the lowest initiative ends their turn. The process  of taking a turn is d |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/8/Text/10` | 0.543419 | You scout ahead and behind the group to watch danger,  moving at half speed. At the start of the next encounter,  every creature in your party gains a +1 circumstance bonus  to their initiative rolls. |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/11` | 0.512478 | initiative order usually don't change during the encounter.  (But see the Delay basic action on page 408.) |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/10` | 0.508876 | If your result is tied with an enemy's result, the enemy  goes first. If your result is tied with another PC's, you can  decide between yourselves who goes first when you reach  that place in the init |

### Query 88
- Text: What is the rule about Unlike a check, where the result is compared to a DC, the  results of initiative rolls are ranked. This ranking sets the  order in which the encounter's participants act—the initiative  order. The character with the highest result goes first. The  second highest follows, and so on until whoever had the  lowest result takes their turn last.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/3/Text/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 424-441::/page/3/Text/9', 'PZO22001 Starfinder Player Core 424-441::/page/3/Text/6', 'PZO22001 Starfinder Player Core 424-441::/page/3/Text/10']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/3/Text/9', 'PZO22001 Starfinder Player Core 424-441::/page/3/Text/8', 'PZO22001 Starfinder Player Core 424-441::/page/3/Text/10']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 424-441::/page/3/Text/8` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/3/Text/10` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/9` | 0.952317 | Unlike a check, where the result is compared to a DC, the  results of initiative rolls are ranked. This ranking sets the  order in which the encounter's participants act—the initiative  order. The cha |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/6` | 0.697014 | When the GM calls for it, you'll roll initiative to determine  your place in the initiative order, which is the sequence in  which the encounter's participants will take their turns.  Rolling initiati |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/10` | 0.688087 | If your result is tied with an enemy's result, the enemy  goes first. If your result is tied with another PC's, you can  decide between yourselves who goes first when you reach  that place in the init |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/4` | 0.627500 | An encounter is played out in a series of rounds, during which  the player characters, adversaries, and other participants in the  encounter act in sequence. You roll initiative to determine this  ord |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/15` | 0.626834 | Once everyone in the encounter has taken a turn, the round  is over and the next one begins. Don't roll initiative again; the  new round proceeds in the same order as the previous one,  repeating the |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/13` | 0.625984 | A round begins when the participant with the highest  initiative roll result starts their turn, and it ends when the  one with the lowest initiative ends their turn. The process  of taking a turn is d |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/11` | 0.592618 | initiative order usually don't change during the encounter.  (But see the Delay basic action on page 408.) |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/8` | 0.590773 | The GM rolls initiative for anyone other than the player  characters in the encounter. If these include a number of  identical creatures, the GM could roll once for the group as a  whole and have them |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/19` | 0.577424 | When it's your turn to act, you can use single actions ([one-action]),  short activities ([two-actions] and [three-actions]), reactions ([reaction]), and free actions  ([free-action]). When you're fin |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/4/Text/2` | 0.565139 | The GM keeps track of the initiative order for an  encounter. It's usually okay for the players to know  this order since they'll see who goes when and be  aware of one another's results. However, the |

### Query 89
- Text: What is the rule about If your result is tied with an enemy's result, the enemy  goes first. If your result is tied with another PC's, you can  decide between yourselves who goes first when you reach  that place in the initiative order. After that, your places in the?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/3/Text/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 424-441::/page/3/Text/10', 'PZO22001 Starfinder Player Core 424-441::/page/3/Text/9', 'PZO22001 Starfinder Player Core 424-441::/page/3/Text/6']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/3/Text/10', 'PZO22001 Starfinder Player Core 424-441::/page/3/Text/11', 'PZO22001 Starfinder Player Core 424-441::/page/3/Text/9']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 424-441::/page/3/Text/11` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/3/Text/9` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/10` | 0.993445 | If your result is tied with an enemy's result, the enemy  goes first. If your result is tied with another PC's, you can  decide between yourselves who goes first when you reach  that place in the init |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/9` | 0.668781 | Unlike a check, where the result is compared to a DC, the  results of initiative rolls are ranked. This ranking sets the  order in which the encounter's participants act—the initiative  order. The cha |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/6` | 0.648044 | When the GM calls for it, you'll roll initiative to determine  your place in the initiative order, which is the sequence in  which the encounter's participants will take their turns.  Rolling initiati |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/4/Text/2` | 0.598451 | The GM keeps track of the initiative order for an  encounter. It's usually okay for the players to know  this order since they'll see who goes when and be  aware of one another's results. However, the |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/4` | 0.559126 | An encounter is played out in a series of rounds, during which  the player characters, adversaries, and other participants in the  encounter act in sequence. You roll initiative to determine this  ord |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/4/Text/18` | 0.558585 | Once you've done all the things you want to do with the actions  you have available, you reach the end of your turn. Take the  following steps in any order you choose. Play then proceeds to  the next |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/15` | 0.548342 | Once everyone in the encounter has taken a turn, the round  is over and the next one begins. Don't roll initiative again; the  new round proceeds in the same order as the previous one,  repeating the |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/19` | 0.546497 | When it's your turn to act, you can use single actions ([one-action]),  short activities ([two-actions] and [three-actions]), reactions ([reaction]), and free actions  ([free-action]). When you're fin |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/13` | 0.543617 | A round begins when the participant with the highest  initiative roll result starts their turn, and it ends when the  one with the lowest initiative ends their turn. The process  of taking a turn is d |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/4/Text/5` | 0.538216 | Any method used to track the initiative order needs to  be flexible because the order can change. A creature can  use the Delay basic action to change its place in the order,  in which case you can er |

### Query 90
- Text: What is the rule about initiative order usually don't change during the encounter.  (But see the Delay basic action on page 408.)?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/3/Text/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 424-441::/page/3/Text/11', 'PZO22001 Starfinder Player Core 424-441::/page/4/Text/5', 'PZO22001 Starfinder Player Core 424-441::/page/3/Text/6']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/3/Text/11', 'PZO22001 Starfinder Player Core 424-441::/page/3/SectionHeader/12', 'PZO22001 Starfinder Player Core 424-441::/page/3/Text/10']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 424-441::/page/3/SectionHeader/12` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/3/Text/10` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/11` | 0.996707 | initiative order usually don't change during the encounter.  (But see the Delay basic action on page 408.) |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/4/Text/5` | 0.776177 | Any method used to track the initiative order needs to  be flexible because the order can change. A creature can  use the Delay basic action to change its place in the order,  in which case you can er |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/6` | 0.681386 | When the GM calls for it, you'll roll initiative to determine  your place in the initiative order, which is the sequence in  which the encounter's participants will take their turns.  Rolling initiati |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/9` | 0.624168 | Unlike a check, where the result is compared to a DC, the  results of initiative rolls are ranked. This ranking sets the  order in which the encounter's participants act—the initiative  order. The cha |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/15` | 0.614077 | Once everyone in the encounter has taken a turn, the round  is over and the next one begins. Don't roll initiative again; the  new round proceeds in the same order as the previous one,  repeating the |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/4` | 0.599001 | An encounter is played out in a series of rounds, during which  the player characters, adversaries, and other participants in the  encounter act in sequence. You roll initiative to determine this  ord |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/4/Text/2` | 0.595836 | The GM keeps track of the initiative order for an  encounter. It's usually okay for the players to know  this order since they'll see who goes when and be  aware of one another's results. However, the |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/4/SectionHeader/4` | 0.581797 | **Changing the Initiative Order** |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/8` | 0.564444 | The GM rolls initiative for anyone other than the player  characters in the encounter. If these include a number of  identical creatures, the GM could roll once for the group as a  whole and have them |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/10` | 0.559164 | If your result is tied with an enemy's result, the enemy  goes first. If your result is tied with another PC's, you can  decide between yourselves who goes first when you reach  that place in the init |

### Query 91
- Text: What is the rule about A round begins when the participant with the highest  initiative roll result starts their turn, and it ends when the  one with the lowest initiative ends their turn. The process  of taking a turn is detailed below. Creatures might also act  outside their turns with reactions and free actions.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/3/Text/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 424-441::/page/3/Text/13', 'PZO22001 Starfinder Player Core 424-441::/page/3/Text/19', 'PZO22001 Starfinder Player Core 424-441::/page/4/Text/16']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/3/Text/13', 'PZO22001 Starfinder Player Core 424-441::/page/3/SectionHeader/12', 'PZO22001 Starfinder Player Core 424-441::/page/3/SectionHeader/14']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 424-441::/page/3/SectionHeader/12` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/3/SectionHeader/14` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/13` | 0.998134 | A round begins when the participant with the highest  initiative roll result starts their turn, and it ends when the  one with the lowest initiative ends their turn. The process  of taking a turn is d |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/19` | 0.736916 | When it's your turn to act, you can use single actions ([one-action]),  short activities ([two-actions] and [three-actions]), reactions ([reaction]), and free actions  ([free-action]). When you're fin |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/4/Text/16` | 0.717301 | Once you've spent all three of your actions, your turn ends  (as described in Step 3) and the next creature's turn begins. You  can choose to end your turn early, losing all remaining actions  (but no |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/15` | 0.666298 | Once everyone in the encounter has taken a turn, the round  is over and the next one begins. Don't roll initiative again; the  new round proceeds in the same order as the previous one,  repeating the |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/9` | 0.654753 | Unlike a check, where the result is compared to a DC, the  results of initiative rolls are ranked. This ranking sets the  order in which the encounter's participants act—the initiative  order. The cha |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/6` | 0.642912 | When the GM calls for it, you'll roll initiative to determine  your place in the initiative order, which is the sequence in  which the encounter's participants will take their turns.  Rolling initiati |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/4/Text/18` | 0.632065 | Once you've done all the things you want to do with the actions  you have available, you reach the end of your turn. Take the  following steps in any order you choose. Play then proceeds to  the next |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/4` | 0.621714 | An encounter is played out in a series of rounds, during which  the player characters, adversaries, and other participants in the  encounter act in sequence. You roll initiative to determine this  ord |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/4/Text/15` | 0.598032 | If you begin a 2-action or 3-action activity on your turn,  you must be able to complete it on your turn. You can't, for  example, begin to High Jump using your final action on one  turn and then comp |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/8` | 0.581799 | The GM rolls initiative for anyone other than the player  characters in the encounter. If these include a number of  identical creatures, the GM could roll once for the group as a  whole and have them |

### Query 92
- Text: What is the rule about Once everyone in the encounter has taken a turn, the round  is over and the next one begins. Don't roll initiative again; the  new round proceeds in the same order as the previous one,  repeating the cycle until the encounter ends.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/3/Text/15']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 424-441::/page/3/Text/15', 'PZO22001 Starfinder Player Core 424-441::/page/3/Text/6', 'PZO22001 Starfinder Player Core 424-441::/page/3/Text/4']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/3/Text/15', 'PZO22001 Starfinder Player Core 424-441::/page/3/SectionHeader/14', 'PZO22001 Starfinder Player Core 424-441::/page/3/SectionHeader/16']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 424-441::/page/3/SectionHeader/14` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/3/SectionHeader/16` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/15` | 0.956625 | Once everyone in the encounter has taken a turn, the round  is over and the next one begins. Don't roll initiative again; the  new round proceeds in the same order as the previous one,  repeating the |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/6` | 0.776413 | When the GM calls for it, you'll roll initiative to determine  your place in the initiative order, which is the sequence in  which the encounter's participants will take their turns.  Rolling initiati |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/4` | 0.764973 | An encounter is played out in a series of rounds, during which  the player characters, adversaries, and other participants in the  encounter act in sequence. You roll initiative to determine this  ord |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/9` | 0.687505 | Unlike a check, where the result is compared to a DC, the  results of initiative rolls are ranked. This ranking sets the  order in which the encounter's participants act—the initiative  order. The cha |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/13` | 0.681894 | A round begins when the participant with the highest  initiative roll result starts their turn, and it ends when the  one with the lowest initiative ends their turn. The process  of taking a turn is d |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/8` | 0.669641 | The GM rolls initiative for anyone other than the player  characters in the encounter. If these include a number of  identical creatures, the GM could roll once for the group as a  whole and have them |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/19` | 0.624730 | When it's your turn to act, you can use single actions ([one-action]),  short activities ([two-actions] and [three-actions]), reactions ([reaction]), and free actions  ([free-action]). When you're fin |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/4/Text/18` | 0.621629 | Once you've done all the things you want to do with the actions  you have available, you reach the end of your turn. Take the  following steps in any order you choose. Play then proceeds to  the next |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/1` | 0.612109 | When every individual action counts, you enter the encounter mode of play. In this mode, time  is divided into rounds, each of which is 6 seconds of time in the game world. Every round, each  particip |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/10` | 0.607636 | If your result is tied with an enemy's result, the enemy  goes first. If your result is tied with another PC's, you can  decide between yourselves who goes first when you reach  that place in the init |

### Query 93
- Text: What is the rule about When your foes are defeated, some sort of truce is reached,  or some other event or circumstance ends the combat, the  encounter is over. You and the other participants no longer  follow the initiative order, and a more free-form style of play  resumes, with the game typically moving into exploration mode.  Sometimes, at the end of an encounter, the GM will award  Experience Points to the party or you'll find treasure to divvy up.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/3/Text/17']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 424-441::/page/3/Text/17', 'PZO22001 Starfinder Player Core 424-441::/page/3/Text/4', 'PZO22001 Starfinder Player Core 424-441::/page/3/Text/1']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/3/Text/17', 'PZO22001 Starfinder Player Core 424-441::/page/3/SectionHeader/16', 'PZO22001 Starfinder Player Core 424-441::/page/3/SectionHeader/18']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 424-441::/page/3/SectionHeader/16` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/3/SectionHeader/18` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/17` | 0.986048 | When your foes are defeated, some sort of truce is reached,  or some other event or circumstance ends the combat, the  encounter is over. You and the other participants no longer  follow the initiativ |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/4` | 0.722274 | An encounter is played out in a series of rounds, during which  the player characters, adversaries, and other participants in the  encounter act in sequence. You roll initiative to determine this  ord |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/1` | 0.673387 | When every individual action counts, you enter the encounter mode of play. In this mode, time  is divided into rounds, each of which is 6 seconds of time in the game world. Every round, each  particip |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/6` | 0.608347 | When the GM calls for it, you'll roll initiative to determine  your place in the initiative order, which is the sequence in  which the encounter's participants will take their turns.  Rolling initiati |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/15` | 0.598955 | Once everyone in the encounter has taken a turn, the round  is over and the next one begins. Don't roll initiative again; the  new round proceeds in the same order as the previous one,  repeating the |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/6/Text/2` | 0.594817 | While encounters use rounds for combat, exploration is more free-form. The GM determines the  flow of time, as you could be traveling by enercycle through a machine megaplex, negotiating with  Free Ca |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/9` | 0.585666 | Unlike a check, where the result is compared to a DC, the  results of initiative rolls are ranked. This ranking sets the  order in which the encounter's participants act—the initiative  order. The cha |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/10` | 0.581156 | If your result is tied with an enemy's result, the enemy  goes first. If your result is tied with another PC's, you can  decide between yourselves who goes first when you reach  that place in the init |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/4/Text/2` | 0.562911 | The GM keeps track of the initiative order for an  encounter. It's usually okay for the players to know  this order since they'll see who goes when and be  aware of one another's results. However, the |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/4/Text/24` | 0.556311 | Activities that take longer than a turn can't normally be  performed during an encounter. Spells with a casting time of  1 minute or more are a common example, as are several skill  actions. When you |

### Query 94
- Text: What is the rule about When it's your turn to act, you can use single actions ([one-action]),  short activities ([two-actions] and [three-actions]), reactions ([reaction]), and free actions  ([free-action]). When you're finished, your turn ends and the character  next in the initiative order begins their turn. Sometimes it's  important to note when during your turn something happens,  so a turn is divided into three steps.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/3/Text/19']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 424-441::/page/3/Text/19', 'PZO22001 Starfinder Player Core 424-441::/page/4/Text/16', 'PZO22001 Starfinder Player Core 424-441::/page/4/Text/13']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/3/Text/19', 'PZO22001 Starfinder Player Core 424-441::/page/3/SectionHeader/20', 'PZO22001 Starfinder Player Core 424-441::/page/3/SectionHeader/18']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 424-441::/page/3/SectionHeader/20` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/3/SectionHeader/18` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/19` | 1.004664 | When it's your turn to act, you can use single actions ([one-action]),  short activities ([two-actions] and [three-actions]), reactions ([reaction]), and free actions  ([free-action]). When you're fin |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/4/Text/16` | 0.760417 | Once you've spent all three of your actions, your turn ends  (as described in Step 3) and the next creature's turn begins. You  can choose to end your turn early, losing all remaining actions  (but no |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/4/Text/13` | 0.748981 | You can use actions in any order you wish during your  turn, but you have to complete one action or activity before  beginning another; for example, you can't use a single action in  the middle of per |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/4/Text/15` | 0.718740 | If you begin a 2-action or 3-action activity on your turn,  you must be able to complete it on your turn. You can't, for  example, begin to High Jump using your final action on one  turn and then comp |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/13` | 0.692932 | A round begins when the participant with the highest  initiative roll result starts their turn, and it ends when the  one with the lowest initiative ends their turn. The process  of taking a turn is d |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/15/Text/15` | 0.657596 | Quickened, slowed, and stunned are the primary  ways you can gain or lose actions on a turn. The rules  for how this works appear on page 407. In brief, these  conditions alter how many actions you re |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/4/Text/18` | 0.650579 | Once you've done all the things you want to do with the actions  you have available, you reach the end of your turn. Take the  following steps in any order you choose. Play then proceeds to  the next |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/4/Text/11` | 0.645635 | • Regain your 3 actions and 1 reaction. If you haven't spent  your reaction from your last turn, you lose it—you can't  "save" actions or reactions from one turn to use during the  next turn. Some abi |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/4/ListItem/7` | 0.642663 | You can use 1 free action or reaction with a trigger of  "Your turn begins" or something similar. |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/21` | 0.637598 | Many things happen automatically at the start of your turn it's a common point for tracking the passage of time for  effects that last multiple rounds. At the start of each of your  turns, take these |

### Query 95
- Text: What is the rule about Many things happen automatically at the start of your turn it's a common point for tracking the passage of time for  effects that last multiple rounds. At the start of each of your  turns, take these steps in any order you choose.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/3/Text/21']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 424-441::/page/3/Text/21', 'PZO22001 Starfinder Player Core 424-441::/page/3/Text/19', 'PZO22001 Starfinder Player Core 424-441::/page/4/ListItem/9']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/3/Text/21', 'PZO22001 Starfinder Player Core 424-441::/page/3/Text/22', 'PZO22001 Starfinder Player Core 424-441::/page/3/SectionHeader/20']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 424-441::/page/3/Text/22` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/3/SectionHeader/20` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/21` | 0.968913 | Many things happen automatically at the start of your turn it's a common point for tracking the passage of time for  effects that last multiple rounds. At the start of each of your  turns, take these |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/19` | 0.692131 | When it's your turn to act, you can use single actions ([one-action]),  short activities ([two-actions] and [three-actions]), reactions ([reaction]), and free actions  ([free-action]). When you're fin |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/4/ListItem/9` | 0.660087 | Do anything else that's specified to happen at the start of  your turn, such as regaining Hit Points from fast healing  or regeneration. |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/4/Text/16` | 0.616905 | Once you've spent all three of your actions, your turn ends  (as described in Step 3) and the next creature's turn begins. You  can choose to end your turn early, losing all remaining actions  (but no |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/1` | 0.612455 | When every individual action counts, you enter the encounter mode of play. In this mode, time  is divided into rounds, each of which is 6 seconds of time in the game world. Every round, each  particip |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/4/Text/6` | 0.609727 | your first turn of a fight, it would affect you during that  turn, decrease to 2 rounds of duration at the start of your  second turn, decrease to 1 round of duration at the start of  your third turn, |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/4/ListItem/22` | 0.598052 | Resolve anything else specified to happen at the end of  your turn. |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/4/Text/10` | 0.595102 | The last step of starting your turn is always the same. |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/4/ListItem/19` | 0.593905 | End any effects that last until the end of your turn. For  example, spells with a sustained duration end at the end of  your turn unless you used the Sustain a Spell action during  your turn to extend |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/13` | 0.591756 | A round begins when the participant with the highest  initiative roll result starts their turn, and it ends when the  one with the lowest initiative ends their turn. The process  of taking a turn is d |

### Query 96
- Text: What is the rule about • If you created an effect lasting for a certain number of  rounds, reduce the number of rounds remaining by 1. The  effect ends if the duration is reduced to 0. For example,  if you cast a spell that lasts 3 rounds on yourself during?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/3/Text/22']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 424-441::/page/3/Text/22', 'PZO22001 Starfinder Player Core 424-441::/page/4/ListItem/19', 'PZO22001 Starfinder Player Core 424-441::/page/4/Text/6']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/3/Text/22', 'PZO22001 Starfinder Player Core 424-441::/page/3/Text/21', 'PZO22001 Starfinder Player Core 424-441::/page/3/Text/24']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 424-441::/page/3/Text/21` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/3/Text/24` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/22` | 0.973085 | • If you created an effect lasting for a certain number of  rounds, reduce the number of rounds remaining by 1. The  effect ends if the duration is reduced to 0. For example,  if you cast a spell that |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/4/ListItem/19` | 0.788195 | End any effects that last until the end of your turn. For  example, spells with a sustained duration end at the end of  your turn unless you used the Sustain a Spell action during  your turn to extend |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/4/Text/6` | 0.699291 | your first turn of a fight, it would affect you during that  turn, decrease to 2 rounds of duration at the start of your  second turn, decrease to 1 round of duration at the start of  your third turn, |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/17/Text/22` | 0.610271 | Conditions with different values are considered  different conditions. If you're affected by a condition  with a value multiple times, you apply only the  highest value, although you might have to tra |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/5/Text/31` | 0.603105 | You can hold your breath for a number of rounds equal to 5  + your Constitution modifier. Reduce your remaining air by 1  round at the end of each of your turns, or by 2 if you attacked  or cast any s |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/21` | 0.572459 | Many things happen automatically at the start of your turn it's a common point for tracking the passage of time for  effects that last multiple rounds. At the start of each of your  turns, take these |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/17/Text/18` | 0.570744 | You can have a given condition only once at a time. If  an effect would impose a condition you already have,  you now have that condition for the longer of the two  durations. The shorter-duration con |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/11/Text/5` | 0.561218 | Some conditions have a number after the condition, called a  condition value. This value conveys the severity of a condition,  and such conditions often give you a bonus or penalty equal  to their val |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/4/Text/16` | 0.545824 | Once you've spent all three of your actions, your turn ends  (as described in Step 3) and the next creature's turn begins. You  can choose to end your turn early, losing all remaining actions  (but no |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/4/Text/11` | 0.541399 | • Regain your 3 actions and 1 reaction. If you haven't spent  your reaction from your last turn, you lose it—you can't  "save" actions or reactions from one turn to use during the  next turn. Some abi |

### Query 97
- Text: What is the rule about **ANCESTRIES & ** **BACKGROUNDS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/3/Text/25']
- Expected found: `True`
- Expected rank: `4`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/27', 'PZO22001 Starfinder Player Core 424-441::/page/15/Text/25', 'PZO22001 Starfinder Player Core 424-441::/page/13/Text/31']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/3/Text/25', 'PZO22001 Starfinder Player Core 424-441::/page/3/Text/24', 'PZO22001 Starfinder Player Core 424-441::/page/7/Text/46', 'PZO22001 Starfinder Player Core 424-441::/page/3/Text/26', 'PZO22001 Starfinder Player Core 424-441::/page/5/Text/35', 'PZO22001 Starfinder Player Core 424-441::/page/17/Text/27', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/27', 'PZO22001 Starfinder Player Core 424-441::/page/11/Text/24', 'PZO22001 Starfinder Player Core 424-441::/page/13/Text/31', 'PZO22001 Starfinder Player Core 424-441::/page/15/Text/25', 'PZO22001 Starfinder Player Core 424-441::/page/9/Text/29']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 424-441::/page/3/Text/24` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/7/Text/46` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/3/Text/26` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/5/Text/35` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/17/Text/27` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/1/Text/27` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/11/Text/24` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/13/Text/31` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/15/Text/25` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/9/Text/29` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/27` | 0.920820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/15/Text/25` | 0.920820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/13/Text/31` | 0.920820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/25` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/11/Text/24` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/9/Text/29` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/7/Text/46` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/17/Text/27` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/5/Text/35` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/34` | 0.476883 | **Rules Overview** |

### Query 98
- Text: What is the rule about **SKILLS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/3/Text/27']
- Expected found: `True`
- Expected rank: `7`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 424-441::/page/17/Text/29', 'PZO22001 Starfinder Player Core 424-441::/page/9/Text/31', 'PZO22001 Starfinder Player Core 424-441::/page/1/Text/29']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/3/Text/27', 'PZO22001 Starfinder Player Core 424-441::/page/3/Text/28', 'PZO22001 Starfinder Player Core 424-441::/page/3/Text/26']
- Expanded expected found: `True`
- Expanded expected rank: `7`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 424-441::/page/3/Text/28` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/3/Text/26` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/17/Text/29` | 0.864442 | **SKILLS** |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/9/Text/31` | 0.864442 | **SKILLS** |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/29` | 0.864442 | **SKILLS** |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/15/Text/27` | 0.822442 | **SKILLS** |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/7/Text/48` | 0.822442 | **SKILLS** |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/5/Text/37` | 0.822442 | **SKILLS** |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/27` | 0.822442 | **SKILLS** |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/11/Text/26` | 0.822442 | **SKILLS** |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/13/Text/33` | 0.822442 | **SKILLS** |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/9/SectionHeader/25` | 0.712079 | SKILLS |

### Query 99
- Text: What is the rule about **FEATS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/3/Text/28']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/30', 'PZO22001 Starfinder Player Core 424-441::/page/3/Text/28', 'PZO22001 Starfinder Player Core 424-441::/page/11/Text/27']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/3/Text/28', 'PZO22001 Starfinder Player Core 424-441::/page/3/Text/29', 'PZO22001 Starfinder Player Core 424-441::/page/3/Text/27']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 424-441::/page/3/Text/29` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/3/Text/27` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/30` | 0.871817 | **FEATS** |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/28` | 0.871817 | **FEATS** |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/11/Text/27` | 0.871817 | **FEATS** |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/5/Text/38` | 0.829817 | **FEATS** |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/9/Text/32` | 0.829817 | **FEATS** |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/13/Text/34` | 0.829817 | **FEATS** |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/15/Text/28` | 0.829817 | **FEATS** |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/17/Text/30` | 0.829817 | **FEATS** |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/7/Text/49` | 0.829817 | **FEATS** |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/9/SectionHeader/23` | 0.651337 | FEATS |

### Query 100
- Text: Lookup values for SpeedFeet per
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/6/Table/8']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 424-441::/page/6/Table/8', 'PZO22001 Starfinder Player Core 424-441::/page/6/TableCell/349', 'PZO22001 Starfinder Player Core 424-441::/page/6/TableCell/348']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/6/Table/8', 'PZO22001 Starfinder Player Core 424-441::/page/6/SectionHeader/7', 'PZO22001 Starfinder Player Core 424-441::/page/6/TableCell/348']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 424-441::/page/6/SectionHeader/7` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/6/TableCell/348` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/6/Table/8` | 0.687667 | SpeedFeet per MinuteMiles per HourMiles per Day10 feet1001815 feet1501-1/21220 feet20021625 feet2502-1/22030 feet30032435 feet3503-1/22840 feet40043250 feet50054060 feet600648 |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/6/TableCell/349` | 0.545988 | Feet per Minute |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/6/TableCell/348` | 0.539603 | Speed |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/6/Text/6` | 0.454454 | Depending on how the GM tracks movement, you move  in feet or miles based on your character's Speed with the  relevant movement type. Typical rates are on the table below. |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/6/SectionHeader/5` | 0.438654 | TRAVEL SPEED |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/6/SectionHeader/7` | 0.408233 | **TRAVEL SPEED** |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/9/SectionHeader/23` | 0.406553 | FEATS |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/8/Text/13` | 0.399734 | You Seek meticulously for hidden doors, concealed hazards,  and so on. You can usually make an educated guess as to which  locations are best to check and move at half speed, but if you  want to be th |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/28` | 0.357850 | **FEATS** |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/5/Text/38` | 0.357850 | **FEATS** |

### Query 101
- Text: What are the requirements for **Prerequisites** master in Medicine or Augmentation Specialist **Requirements** You have a medkit.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/7/Text/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 424-441::/page/7/Text/11', 'PZO22001 Starfinder Player Core 424-441::/page/7/Text/12', 'PZO22001 Starfinder Player Core 424-441::/page/7/SectionHeader/9']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/7/Text/11', 'PZO22001 Starfinder Player Core 424-441::/page/7/Text/12', 'PZO22001 Starfinder Player Core 424-441::/page/7/SectionHeader/10']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 424-441::/page/7/Text/12` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 424-441::/page/7/SectionHeader/10` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/7/Text/11` | 0.981120 | **Prerequisites** master in Medicine or Augmentation Specialist **Requirements** You have a medkit. |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/7/Text/12` | 0.509873 | You safely implant or remove an augmentation on a willing  creature. This takes 1 hour per item level of the augmentation  if using a medkit or half the normal amount of time if you  have access to a |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/7/SectionHeader/9` | 0.484084 | **IMPLANT AUGMENTATION** |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/6/Text/17` | 0.360208 | **Requirements** You have environmental protection on your  armor or a field scientist's kit. |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/10/Text/1` | 0.347313 | losing its increase by one step and increase your proficiency  rank in another skill by one step. The new proficiency rank has  to be equal to or lower than the proficiency rank you traded  away. For |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/9/Text/22` | 0.321177 | For instance, you can't replace a skill feat you chose at 2nd  level for a 4th-level one, or for one that requires prerequisites  you didn't meet at the time you took the original feat. If you  don't |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/7/Text/15` | 0.319832 | **Requirements** You have a repair kit and one free hand. |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/7/SectionHeader/13` | 0.317581 | **INSTALL UPGRADE** |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/7/Text/16` | 0.296534 | You spend 10 minutes installing an upgrade into a suit of  armor or weapon, placing the upgrade into an empty upgrade  slot. You can also use this activity to uninstall an upgrade.  You can't install |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/7/SectionHeader/2` | 0.294181 | **FOLLOW THE EXPERT** |
