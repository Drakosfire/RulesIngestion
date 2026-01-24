# RulesLawyer Evaluation Report: nomic-embed-text-v2

## Summary
- Run ID: `None`
- Ruleset ID: `None`
- Document ID: `None`
- Chunk source: `enriched`
- Chunk count: `791`
- Query count: `103`
- Evaluated queries: `103`
- Coverage: `1.0000`
- MRR: `0.8321`
- hit@1: `0.7282`
- hit@3: `0.9320`
- hit@5: `0.9806`
- hit@10: `1.0000`
- Embeddings reused: `False`
- Graph boost: `0.05` (depth=2, top_k=50, source=top, seed_top_n=3, same_kind_only=False, decay=0.4)

### Expanded Gold Metrics
- Coverage: `1.0000`
- MRR: `0.8545`
- hit@1: `0.7573`
- hit@3: `0.9515`
- hit@5: `0.9903`
- hit@10: `1.0000`

### Expanded Gold Expansion Stats
- Queries with additions: `103`
- Avg added per query: `2.23`
- Max added: `9`
- Addition reasons:
  - graph_depth_1: `230`

### Expanded Gold Delta (Expanded - Strict)
- Coverage Δ: `0.0000`
- MRR Δ: `0.0223`
- hit@1 Δ: `0.0291`
- hit@3 Δ: `0.0194`
- hit@5 Δ: `0.0097`
- hit@10 Δ: `0.0000`

## Timings (ms)
- Embedding (chunks): `11882`
- Embedding (queries): `2156`
- Evaluation (strict): `47`
- Evaluation (expanded): `39`
- Total: `18665`

### Timing Estimates (ms)
- Evaluation (strict): `82`
- Evaluation (expanded): `30`
- Total: `14150`

## Query Details
### Query 0
- Text: What is the rule about ACTIONS?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/0/SectionHeader/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 406-423::/page/0/SectionHeader/1', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/11', 'PZO22001 Starfinder Player Core 406-423::/page/3/Text/48']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/0/SectionHeader/1', 'PZO22001 Starfinder Player Core 406-423::/page/0/Text/2']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 406-423::/page/0/Text/2` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/0/SectionHeader/1` | 0.772859 | ACTIONS |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/11` | 0.766222 | These rules clarify some of the specifics of using actions. |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/48` | 0.719885 | **Actions** |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/15/Text/27` | 0.677885 | **Actions** |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/44` | 0.677885 | **Actions** |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/61` | 0.677885 | **Actions** |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/36` | 0.677885 | **Actions** |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/9/Text/37` | 0.677885 | **Actions** |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/11/Text/34` | 0.677885 | **Actions** |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/7/Text/42` | 0.677885 | **Actions** |

### Query 1
- Text: What is the rule about You affect the world around you primarily by using actions, which produce effects. Actions are most  closely measured and restricted during the encounter mode of play, but even when it isn't important for  you to keep strict track of actions, they remain the way in which you interact with the game world.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/0/Text/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 406-423::/page/0/Text/2', 'PZO22001 Starfinder Player Core 406-423::/page/0/Text/6', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/11']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/0/Text/2', 'PZO22001 Starfinder Player Core 406-423::/page/0/Text/6', 'PZO22001 Starfinder Player Core 406-423::/page/0/SectionHeader/1']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 406-423::/page/0/Text/6` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/0/SectionHeader/1` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/2` | 0.990104 | You affect the world around you primarily by using actions, which produce effects. Actions are most  closely measured and restricted during the encounter mode of play, but even when it isn't important |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/6` | 0.688132 | You'll need to track your actions carefully in an encounter. At  the start of each turn you take in an encounter, you regain 3  actions and 1 reaction to spend that round. (Regaining your  actions is |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/11` | 0.671452 | These rules clarify some of the specifics of using actions. |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/6/Text/2` | 0.629046 | Your movement and position determine how you interact with the world. Moving in exploration and  downtime modes is relatively fluid. Movement in encounter mode follows additional rules explained in  T |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/10` | 0.612247 | **Reactions** have triggers, which must be met for you to use  the reaction. You can use a reaction anytime its trigger is met,  whether it's your turn or not. Outside of encounters, your use  of reac |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/22` | 0.610853 | You have to spend all the actions of an activity at once  to gain its effects. In an encounter, this means you must  complete it during your turn. If an activity gets interrupted or  disrupted in an e |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/2/Text/2` | 0.598505 | Basic actions represent common tasks like moving around,  attacking, and helping others. As such, every creature can  use basic actions except in some extreme circumstances,  and many of those actions |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/7` | 0.592645 | Some effects are even more restrictive. Certain abilities,  instead of or in addition to changing the number of actions  you can use, say specifically that you can't use reactions.  The most restricti |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/21` | 0.591502 | An activity might cause you to use specific actions within  it. You don't have to spend additional actions to perform  them—they're already factored into the activity's required  actions. (See Subordi |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/12/Text/7` | 0.583553 | Most effects are discrete, creating an instantaneous effect  when you let the GM know what actions you're going to use.  Firing a gun, moving to a new space, or taking something  out of your pack all |

### Query 2
- Text: What is the rule about You'll need to track your actions carefully in an encounter. At  the start of each turn you take in an encounter, you regain 3  actions and 1 reaction to spend that round. (Regaining your  actions is described in detail on page 428.) You can spend  your actions in many different ways.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/0/Text/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 406-423::/page/0/Text/6', 'PZO22001 Starfinder Player Core 406-423::/page/0/Text/22', 'PZO22001 Starfinder Player Core 406-423::/page/0/Text/2']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/0/Text/6', 'PZO22001 Starfinder Player Core 406-423::/page/0/Text/7', 'PZO22001 Starfinder Player Core 406-423::/page/0/Text/2']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 406-423::/page/0/Text/7` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/0/Text/2` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/6` | 0.981722 | You'll need to track your actions carefully in an encounter. At  the start of each turn you take in an encounter, you regain 3  actions and 1 reaction to spend that round. (Regaining your  actions is |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/22` | 0.762276 | You have to spend all the actions of an activity at once  to gain its effects. In an encounter, this means you must  complete it during your turn. If an activity gets interrupted or  disrupted in an e |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/2` | 0.722257 | You affect the world around you primarily by using actions, which produce effects. Actions are most  closely measured and restricted during the encounter mode of play, but even when it isn't important |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/4` | 0.658169 | Sometimes you need to attempt something not already  covered by defined actions in the game. When this happens,  the rules tell you how many actions you need to spend as  well as any traits your actio |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/1` | 0.650294 | free actions limit when you can use those actions. You can use  only one action in response to a given trigger. For example, if  you had a reaction and a free action that both had a trigger  of "your |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/18` | 0.639493 | case of an activity, you usually lose all actions spent for the  activity up through the end of that turn. For instance, if you  began to Cast a Spell requiring 3 actions and the first action  was dis |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/10` | 0.627711 | **Reactions** have triggers, which must be met for you to use  the reaction. You can use a reaction anytime its trigger is met,  whether it's your turn or not. Outside of encounters, your use  of reac |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/11` | 0.617578 | These rules clarify some of the specifics of using actions. |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/11` | 0.616427 | **Free actions** don't cost you any of your actions per turn,  nor do they cost your reaction. A free action with no trigger  follows the same rules as a single action (except the action  cost). It mu |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/8` | 0.609272 | You prepare to use an action that will occur outside your  turn. Choose a single action or free action you can use, and  designate a trigger. Your turn then ends. If the trigger you  designated occurs |

### Query 3
- Text: What is the rule about There are four types of actions: single actions, activities,  reactions, and free actions.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/0/Text/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 406-423::/page/0/Text/7', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/11', 'PZO22001 Starfinder Player Core 406-423::/page/0/Text/20']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/0/Text/7', 'PZO22001 Starfinder Player Core 406-423::/page/0/Text/6', 'PZO22001 Starfinder Player Core 406-423::/page/0/Text/8']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 406-423::/page/0/Text/6` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/0/Text/8` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/7` | 0.942980 | There are four types of actions: single actions, activities,  reactions, and free actions. |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/11` | 0.675964 | These rules clarify some of the specifics of using actions. |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/20` | 0.664541 | An activity typically involves using multiple actions to create  an effect greater than you can produce with a single action,  or combining multiple single actions to produce an effect  that's differe |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/27` | 0.587227 | You can use free actions that have triggers and reactions only  in response to certain events. Each such reaction and free  action lists the trigger that must happen for you to perform it.  When its t |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/11` | 0.586163 | **Free actions** don't cost you any of your actions per turn,  nor do they cost your reaction. A free action with no trigger  follows the same rules as a single action (except the action  cost). It mu |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/1` | 0.565673 | free actions limit when you can use those actions. You can use  only one action in response to a given trigger. For example, if  you had a reaction and a free action that both had a trigger  of "your |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/13` | 0.560577 | You can use only one single action, activity, or free action  that doesn't have a trigger at a time. You must complete  one before beginning another. For example, the Double  Tap activity states you m |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/8/Text/3` | 0.560171 | Some actions, such as Step, specifically state  they don't trigger reactions or free actions based on  movement. |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/2` | 0.548125 | This limitation of one action per trigger is per creature;  more than one creature can use a reaction or free action  in response to a given trigger. If multiple actions would be  occurring at the sam |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/0/ListItem/16` | 0.544869 | [three-actions] Three-Action Activity |

### Query 4
- Text: What is the rule about **Single actions **can be completed in a very short time.  They're self-contained, and their effects are generated within  the span of that single action.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/0/Text/8']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 406-423::/page/0/Text/8', 'PZO22001 Starfinder Player Core 406-423::/page/0/Text/20', 'PZO22001 Starfinder Player Core 406-423::/page/1/SectionHeader/12']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/0/Text/8', 'PZO22001 Starfinder Player Core 406-423::/page/0/Text/9', 'PZO22001 Starfinder Player Core 406-423::/page/0/Text/7']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 406-423::/page/0/Text/9` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/0/Text/7` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/8` | 0.986468 | **Single actions **can be completed in a very short time.  They're self-contained, and their effects are generated within  the span of that single action. |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/20` | 0.596282 | An activity typically involves using multiple actions to create  an effect greater than you can produce with a single action,  or combining multiple single actions to produce an effect  that's differe |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/1/SectionHeader/12` | 0.596103 | **Simultaneous Actions** |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/21` | 0.542168 | An activity might cause you to use specific actions within  it. You don't have to spend additional actions to perform  them—they're already factored into the activity's required  actions. (See Subordi |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/0/ListItem/14` | 0.540134 | [one-action] Single Action |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/22` | 0.529664 | You have to spend all the actions of an activity at once  to gain its effects. In an encounter, this means you must  complete it during your turn. If an activity gets interrupted or  disrupted in an e |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/11` | 0.529215 | These rules clarify some of the specifics of using actions. |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/13` | 0.527913 | You can use only one single action, activity, or free action  that doesn't have a trigger at a time. You must complete  one before beginning another. For example, the Double  Tap activity states you m |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/12/Text/7` | 0.522676 | Most effects are discrete, creating an instantaneous effect  when you let the GM know what actions you're going to use.  Firing a gun, moving to a new space, or taking something  out of your pack all |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/9` | 0.519898 | **Activities** usually take longer and require using multiple  actions, which must be spent in succession. Strike is a single  action, but Double Tap is an activity in which you use both  the Aim and |

### Query 5
- Text: What is the rule about **Activities** usually take longer and require using multiple  actions, which must be spent in succession. Strike is a single  action, but Double Tap is an activity in which you use both  the Aim and Strike actions to generate its effect.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/0/Text/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 406-423::/page/0/Text/9', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/13', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/17']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/0/Text/9', 'PZO22001 Starfinder Player Core 406-423::/page/0/Text/10', 'PZO22001 Starfinder Player Core 406-423::/page/0/Text/8']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 406-423::/page/0/Text/10` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/0/Text/8` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/9` | 1.000910 | **Activities** usually take longer and require using multiple  actions, which must be spent in succession. Strike is a single  action, but Double Tap is an activity in which you use both  the Aim and |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/13` | 0.803885 | You can use only one single action, activity, or free action  that doesn't have a trigger at a time. You must complete  one before beginning another. For example, the Double  Tap activity states you m |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/17` | 0.657064 | Using an activity isn't the same as using any of  its subordinate actions. For example, the quickened  condition you get from the *haste* spell lets you spend  an extra action each turn to Stride or S |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/20` | 0.596910 | An activity typically involves using multiple actions to create  an effect greater than you can produce with a single action,  or combining multiple single actions to produce an effect  that's differe |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/21` | 0.584155 | An activity might cause you to use specific actions within  it. You don't have to spend additional actions to perform  them—they're already factored into the activity's required  actions. (See Subordi |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/0/ListItem/15` | 0.577007 | [two-actions] Two-Action Activity |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/2/Text/2` | 0.569890 | Basic actions represent common tasks like moving around,  attacking, and helping others. As such, every creature can  use basic actions except in some extreme circumstances,  and many of those actions |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/8` | 0.569867 | **Single actions **can be completed in a very short time.  They're self-contained, and their effects are generated within  the span of that single action. |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/20` | 0.558078 | **Long Tasks:** For a task that takes longer than a  round, you often need to spend more than one action  preparing to help, as determined by the GM. |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/22` | 0.556468 | You have to spend all the actions of an activity at once  to gain its effects. In an encounter, this means you must  complete it during your turn. If an activity gets interrupted or  disrupted in an e |

### Query 6
- Text: What is the rule about **Reactions** have triggers, which must be met for you to use  the reaction. You can use a reaction anytime its trigger is met,  whether it's your turn or not. Outside of encounters, your use  of reactions is more flexible and up to the GM. Reactions are  usually triggered by other creatures or by events outside  your control.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/0/Text/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 406-423::/page/0/Text/10', 'PZO22001 Starfinder Player Core 406-423::/page/0/Text/27', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/14']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/0/Text/10', 'PZO22001 Starfinder Player Core 406-423::/page/0/Text/9', 'PZO22001 Starfinder Player Core 406-423::/page/0/Text/11']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 406-423::/page/0/Text/9` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/0/Text/11` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/10` | 0.997356 | **Reactions** have triggers, which must be met for you to use  the reaction. You can use a reaction anytime its trigger is met,  whether it's your turn or not. Outside of encounters, your use  of reac |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/27` | 0.759593 | You can use free actions that have triggers and reactions only  in response to certain events. Each such reaction and free  action lists the trigger that must happen for you to perform it.  When its t |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/14` | 0.749478 | Free actions with triggers and reactions work  differently. You can use these whenever the trigger  occurs, even if the trigger occurs in the middle of  another action. |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/11` | 0.703735 | **Free actions** don't cost you any of your actions per turn,  nor do they cost your reaction. A free action with no trigger  follows the same rules as a single action (except the action  cost). It mu |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/8` | 0.701408 | You prepare to use an action that will occur outside your  turn. Choose a single action or free action you can use, and  designate a trigger. Your turn then ends. If the trigger you  designated occurs |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/1` | 0.693533 | free actions limit when you can use those actions. You can use  only one action in response to a given trigger. For example, if  you had a reaction and a free action that both had a trigger  of "your |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/2` | 0.657332 | This limitation of one action per trigger is per creature;  more than one creature can use a reaction or free action  in response to a given trigger. If multiple actions would be  occurring at the sam |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/8/Text/2` | 0.650537 | Some reactions and free actions are triggered by a  creature using an action with the move trait. The most  notable example is Reactive Strike (reproduced below).  Actions with the move trait can trig |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/28` | 0.649328 | There are only a few basic reactions and free actions that  all characters can use. You're more likely to gain actions with  triggers from your class, feats, and magic items. |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/2` | 0.600318 | You affect the world around you primarily by using actions, which produce effects. Actions are most  closely measured and restricted during the encounter mode of play, but even when it isn't important |

### Query 7
- Text: What is the rule about **Free actions** don't cost you any of your actions per turn,  nor do they cost your reaction. A free action with no trigger  follows the same rules as a single action (except the action  cost). It must be used on your turn and can't be used during  another action. A free action with a trigger follows the same  rules as a reaction (except the reaction cost). It can be used  any time its trigger is met.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/0/Text/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 406-423::/page/0/Text/11', 'PZO22001 Starfinder Player Core 406-423::/page/0/Text/27', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/14']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/0/Text/11', 'PZO22001 Starfinder Player Core 406-423::/page/0/Text/10', 'PZO22001 Starfinder Player Core 406-423::/page/0/SectionHeader/12']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 406-423::/page/0/Text/10` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/0/SectionHeader/12` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/11` | 1.005829 | **Free actions** don't cost you any of your actions per turn,  nor do they cost your reaction. A free action with no trigger  follows the same rules as a single action (except the action  cost). It mu |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/27` | 0.806219 | You can use free actions that have triggers and reactions only  in response to certain events. Each such reaction and free  action lists the trigger that must happen for you to perform it.  When its t |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/14` | 0.787186 | Free actions with triggers and reactions work  differently. You can use these whenever the trigger  occurs, even if the trigger occurs in the middle of  another action. |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/1` | 0.734823 | free actions limit when you can use those actions. You can use  only one action in response to a given trigger. For example, if  you had a reaction and a free action that both had a trigger  of "your |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/8` | 0.704192 | You prepare to use an action that will occur outside your  turn. Choose a single action or free action you can use, and  designate a trigger. Your turn then ends. If the trigger you  designated occurs |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/13` | 0.673662 | You can use only one single action, activity, or free action  that doesn't have a trigger at a time. You must complete  one before beginning another. For example, the Double  Tap activity states you m |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/10` | 0.650601 | **Reactions** have triggers, which must be met for you to use  the reaction. You can use a reaction anytime its trigger is met,  whether it's your turn or not. Outside of encounters, your use  of reac |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/28` | 0.650517 | There are only a few basic reactions and free actions that  all characters can use. You're more likely to gain actions with  triggers from your class, feats, and magic items. |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/8/Text/3` | 0.634715 | Some actions, such as Step, specifically state  they don't trigger reactions or free actions based on  movement. |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/2` | 0.628175 | This limitation of one action per trigger is per creature;  more than one creature can use a reaction or free action  in response to a given trigger. If multiple actions would be  occurring at the sam |

### Query 8
- Text: What is the rule about **ACTION ICON KEY**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/0/SectionHeader/12']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 406-423::/page/0/SectionHeader/12', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/11', 'PZO22001 Starfinder Player Core 406-423::/page/0/Text/13']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/0/SectionHeader/12', 'PZO22001 Starfinder Player Core 406-423::/page/0/Text/11', 'PZO22001 Starfinder Player Core 406-423::/page/0/Text/13']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 406-423::/page/0/Text/11` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/0/Text/13` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/0/SectionHeader/12` | 0.936468 | **ACTION ICON KEY** |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/11` | 0.570574 | These rules clarify some of the specifics of using actions. |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/13` | 0.557958 | These icons appear in stat blocks as shorthand for each  type of action. As a player, you'll usually see the icon in  an action's header (such as in a basic action, skill action,  feat, or spell). In |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/7/Text/42` | 0.513693 | **Actions** |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/11/Text/34` | 0.513693 | **Actions** |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/9/Text/37` | 0.513693 | **Actions** |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/48` | 0.513692 | **Actions** |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/61` | 0.513692 | **Actions** |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/15/Text/27` | 0.513692 | **Actions** |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/44` | 0.513692 | **Actions** |

### Query 9
- Text: What is the rule about These icons appear in stat blocks as shorthand for each  type of action. As a player, you'll usually see the icon in  an action's header (such as in a basic action, skill action,  feat, or spell). In a creature stat block, or a feat that  gives you a new action in addition to other benefits, the  icon will appear in the running text. For examples, see  the formatting of rules on page 15.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/0/Text/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 406-423::/page/0/Text/13', 'PZO22001 Starfinder Player Core 406-423::/page/16/Text/5', 'PZO22001 Starfinder Player Core 406-423::/page/2/Text/2']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/0/Text/13', 'PZO22001 Starfinder Player Core 406-423::/page/0/SectionHeader/12', 'PZO22001 Starfinder Player Core 406-423::/page/0/ListItem/14']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 406-423::/page/0/SectionHeader/12` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/0/ListItem/14` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/13` | 1.019799 | These icons appear in stat blocks as shorthand for each  type of action. As a player, you'll usually see the icon in  an action's header (such as in a basic action, skill action,  feat, or spell). In |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/16/Text/5` | 0.593549 | Whether appearing in a spell, as an item, or within a creature's  stat block, afflictions appear in the following format. |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/2/Text/2` | 0.550873 | Basic actions represent common tasks like moving around,  attacking, and helping others. As such, every creature can  use basic actions except in some extreme circumstances,  and many of those actions |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/2/Text/3` | 0.513802 | Actions that are used less frequently but are still available  to most creatures are presented in Specialty Basic Actions  starting on page 410. These typically have requirements that  not all charact |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/17` | 0.501290 | Using an activity isn't the same as using any of  its subordinate actions. For example, the quickened  condition you get from the *haste* spell lets you spend  an extra action each turn to Stride or S |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/2/Text/4` | 0.499243 | In addition to the actions in these two sections, the actions  for spellcasting can be found on page 298, and the actions for  using magic items appear on page 282. |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/11` | 0.493386 | These rules clarify some of the specifics of using actions. |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/6` | 0.478991 | Effects can change the number of actions you can use on  your turn, or whether you can use actions at all. The slowed  condition, for example, causes you to lose actions, while the  quickened conditio |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/12/Text/7` | 0.475562 | Most effects are discrete, creating an instantaneous effect  when you let the GM know what actions you're going to use.  Firing a gun, moving to a new space, or taking something  out of your pack all |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/4` | 0.475284 | Sometimes you need to attempt something not already  covered by defined actions in the game. When this happens,  the rules tell you how many actions you need to spend as  well as any traits your actio |

### Query 10
- Text: What is the rule about [one-action] Single Action?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/0/ListItem/14']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 406-423::/page/0/ListItem/14', 'PZO22001 Starfinder Player Core 406-423::/page/0/ListItem/15', 'PZO22001 Starfinder Player Core 406-423::/page/0/Text/20']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/0/ListItem/14', 'PZO22001 Starfinder Player Core 406-423::/page/0/ListItem/15', 'PZO22001 Starfinder Player Core 406-423::/page/0/Text/13']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 406-423::/page/0/ListItem/15` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/0/Text/13` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/0/ListItem/14` | 0.873478 | [one-action] Single Action |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/0/ListItem/15` | 0.669645 | [two-actions] Two-Action Activity |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/20` | 0.652810 | An activity typically involves using multiple actions to create  an effect greater than you can produce with a single action,  or combining multiple single actions to produce an effect  that's differe |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/8` | 0.609372 | **Single actions **can be completed in a very short time.  They're self-contained, and their effects are generated within  the span of that single action. |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/0/ListItem/16` | 0.603023 | [three-actions] Three-Action Activity |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/11` | 0.599226 | These rules clarify some of the specifics of using actions. |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/1/SectionHeader/12` | 0.583622 | **Simultaneous Actions** |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/13` | 0.565624 | You can use only one single action, activity, or free action  that doesn't have a trigger at a time. You must complete  one before beginning another. For example, the Double  Tap activity states you m |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/2` | 0.556481 | This limitation of one action per trigger is per creature;  more than one creature can use a reaction or free action  in response to a given trigger. If multiple actions would be  occurring at the sam |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/21` | 0.553062 | An activity might cause you to use specific actions within  it. You don't have to spend additional actions to perform  them—they're already factored into the activity's required  actions. (See Subordi |

### Query 11
- Text: What is the rule about [two-actions] Two-Action Activity?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/0/ListItem/15']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 406-423::/page/0/ListItem/15', 'PZO22001 Starfinder Player Core 406-423::/page/0/ListItem/16', 'PZO22001 Starfinder Player Core 406-423::/page/3/SectionHeader/6']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/0/ListItem/15', 'PZO22001 Starfinder Player Core 406-423::/page/0/ListItem/16', 'PZO22001 Starfinder Player Core 406-423::/page/0/ListItem/14']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 406-423::/page/0/ListItem/16` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/0/ListItem/14` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/0/ListItem/15` | 0.916413 | [two-actions] Two-Action Activity |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/0/ListItem/16` | 0.766592 | [three-actions] Three-Action Activity |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/3/SectionHeader/6` | 0.655956 | **READY **[two-actions] |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/11` | 0.609733 | These rules clarify some of the specifics of using actions. |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/9` | 0.587021 | **Activities** usually take longer and require using multiple  actions, which must be spent in succession. Strike is a single  action, but Double Tap is an activity in which you use both  the Aim and |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/13` | 0.586212 | You can use only one single action, activity, or free action  that doesn't have a trigger at a time. You must complete  one before beginning another. For example, the Double  Tap activity states you m |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/20` | 0.584286 | An activity typically involves using multiple actions to create  an effect greater than you can produce with a single action,  or combining multiple single actions to produce an effect  that's differe |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/21` | 0.564125 | An activity might cause you to use specific actions within  it. You don't have to spend additional actions to perform  them—they're already factored into the activity's required  actions. (See Subordi |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/1` | 0.546632 | free actions limit when you can use those actions. You can use  only one action in response to a given trigger. For example, if  you had a reaction and a free action that both had a trigger  of "your |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/1/SectionHeader/12` | 0.546300 | **Simultaneous Actions** |

### Query 12
- Text: What is the rule about [three-actions] Three-Action Activity?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/0/ListItem/16']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 406-423::/page/0/ListItem/16', 'PZO22001 Starfinder Player Core 406-423::/page/0/ListItem/15', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/11']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/0/ListItem/16', 'PZO22001 Starfinder Player Core 406-423::/page/0/ListItem/15', 'PZO22001 Starfinder Player Core 406-423::/page/0/ListItem/17']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 406-423::/page/0/ListItem/15` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/0/ListItem/17` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/0/ListItem/16` | 0.920399 | [three-actions] Three-Action Activity |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/0/ListItem/15` | 0.764205 | [two-actions] Two-Action Activity |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/11` | 0.635708 | These rules clarify some of the specifics of using actions. |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/20` | 0.572295 | An activity typically involves using multiple actions to create  an effect greater than you can produce with a single action,  or combining multiple single actions to produce an effect  that's differe |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/21` | 0.549954 | An activity might cause you to use specific actions within  it. You don't have to spend additional actions to perform  them—they're already factored into the activity's required  actions. (See Subordi |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/18` | 0.548241 | case of an activity, you usually lose all actions spent for the  activity up through the end of that turn. For instance, if you  began to Cast a Spell requiring 3 actions and the first action  was dis |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/13` | 0.540932 | You can use only one single action, activity, or free action  that doesn't have a trigger at a time. You must complete  one before beginning another. For example, the Double  Tap activity states you m |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/7` | 0.532940 | There are four types of actions: single actions, activities,  reactions, and free actions. |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/17` | 0.519328 | Using an activity isn't the same as using any of  its subordinate actions. For example, the quickened  condition you get from the *haste* spell lets you spend  an extra action each turn to Stride or S |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/9` | 0.515081 | **Activities** usually take longer and require using multiple  actions, which must be spent in succession. Strike is a single  action, but Double Tap is an activity in which you use both  the Aim and |

### Query 13
- Text: What is the rule about [reaction] Reaction?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/0/ListItem/17']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 406-423::/page/0/ListItem/17', 'PZO22001 Starfinder Player Core 406-423::/page/0/Text/10', 'PZO22001 Starfinder Player Core 406-423::/page/0/Text/27']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/0/ListItem/17', 'PZO22001 Starfinder Player Core 406-423::/page/0/ListItem/16', 'PZO22001 Starfinder Player Core 406-423::/page/0/ListItem/18']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 406-423::/page/0/ListItem/16` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/0/ListItem/18` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/0/ListItem/17` | 0.802417 | [reaction] Reaction |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/10` | 0.630836 | **Reactions** have triggers, which must be met for you to use  the reaction. You can use a reaction anytime its trigger is met,  whether it's your turn or not. Outside of encounters, your use  of reac |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/27` | 0.563341 | You can use free actions that have triggers and reactions only  in response to certain events. Each such reaction and free  action lists the trigger that must happen for you to perform it.  When its t |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/11` | 0.506183 | These rules clarify some of the specifics of using actions. |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/8/SectionHeader/4` | 0.501957 | **REACTIVE STRIKE **[reaction] |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/8/SectionHeader/1` | 0.481181 | **REACTIONS TO MOVEMENT** |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/1` | 0.480174 | free actions limit when you can use those actions. You can use  only one action in response to a given trigger. For example, if  you had a reaction and a free action that both had a trigger  of "your |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/2/Text/10` | 0.474562 | You try to help your ally with a task. To use this reaction, you  must first prepare to help, usually by using an action during  your turn. You must explain to the GM exactly how you're trying  to hel |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/11` | 0.472669 | **Free actions** don't cost you any of your actions per turn,  nor do they cost your reaction. A free action with no trigger  follows the same rules as a single action (except the action  cost). It mu |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/8` | 0.471344 | You prepare to use an action that will occur outside your  turn. Choose a single action or free action you can use, and  designate a trigger. Your turn then ends. If the trigger you  designated occurs |

### Query 14
- Text: What is the rule about [free-action] Free Action?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/0/ListItem/18']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 406-423::/page/0/ListItem/18', 'PZO22001 Starfinder Player Core 406-423::/page/0/Text/11', 'PZO22001 Starfinder Player Core 406-423::/page/0/Text/27']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/0/ListItem/18', 'PZO22001 Starfinder Player Core 406-423::/page/0/ListItem/17', 'PZO22001 Starfinder Player Core 406-423::/page/0/SectionHeader/19']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 406-423::/page/0/ListItem/17` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/0/SectionHeader/19` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/0/ListItem/18` | 0.873410 | [free-action] Free Action |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/11` | 0.724931 | **Free actions** don't cost you any of your actions per turn,  nor do they cost your reaction. A free action with no trigger  follows the same rules as a single action (except the action  cost). It mu |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/27` | 0.674726 | You can use free actions that have triggers and reactions only  in response to certain events. Each such reaction and free  action lists the trigger that must happen for you to perform it.  When its t |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/3/SectionHeader/10` | 0.625199 | **RELEASE **[free-action] |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/11` | 0.593112 | These rules clarify some of the specifics of using actions. |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/1` | 0.580714 | free actions limit when you can use those actions. You can use  only one action in response to a given trigger. For example, if  you had a reaction and a free action that both had a trigger  of "your |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/2/SectionHeader/18` | 0.580143 | **DELAY **[free-action] |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/14` | 0.563739 | Free actions with triggers and reactions work  differently. You can use these whenever the trigger  occurs, even if the trigger occurs in the middle of  another action. |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/7` | 0.549680 | There are four types of actions: single actions, activities,  reactions, and free actions. |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/0/ListItem/16` | 0.549306 | [three-actions] Three-Action Activity |

### Query 15
- Text: What is the rule about ACTIVITIES?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/0/SectionHeader/19']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 406-423::/page/0/SectionHeader/19', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/11', 'PZO22001 Starfinder Player Core 406-423::/page/0/ListItem/15']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/0/SectionHeader/19', 'PZO22001 Starfinder Player Core 406-423::/page/0/ListItem/18', 'PZO22001 Starfinder Player Core 406-423::/page/0/Text/20']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 406-423::/page/0/ListItem/18` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/0/Text/20` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/0/SectionHeader/19` | 0.695690 | ACTIVITIES |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/11` | 0.648156 | These rules clarify some of the specifics of using actions. |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/0/ListItem/15` | 0.584715 | [two-actions] Two-Action Activity |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/0/ListItem/16` | 0.537196 | [three-actions] Three-Action Activity |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/17/Text/32` | 0.533175 | Rules Overview |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/21` | 0.512212 | An activity might cause you to use specific actions within  it. You don't have to spend additional actions to perform  them—they're already factored into the activity's required  actions. (See Subordi |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/1/SectionHeader/10` | 0.508585 | **IN-DEPTH ACTION RULES** |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/2/SectionHeader/6` | 0.492652 | BASIC ACTIONS |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/2/SectionHeader/1` | 0.492652 | BASIC ACTIONS |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/17` | 0.490423 | Using an activity isn't the same as using any of  its subordinate actions. For example, the quickened  condition you get from the *haste* spell lets you spend  an extra action each turn to Stride or S |

### Query 16
- Text: What is the rule about An activity typically involves using multiple actions to create  an effect greater than you can produce with a single action,  or combining multiple single actions to produce an effect  that's different from merely the sum of those actions. In some  cases, usually when spellcasting, an activity can consist of  only 1 action, 1 reaction, or even 1 free action.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/0/Text/20']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 406-423::/page/0/Text/20', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/18', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/17']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/0/Text/20', 'PZO22001 Starfinder Player Core 406-423::/page/0/Text/21', 'PZO22001 Starfinder Player Core 406-423::/page/0/SectionHeader/19']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 406-423::/page/0/Text/21` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/0/SectionHeader/19` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/20` | 0.999683 | An activity typically involves using multiple actions to create  an effect greater than you can produce with a single action,  or combining multiple single actions to produce an effect  that's differe |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/18` | 0.677314 | case of an activity, you usually lose all actions spent for the  activity up through the end of that turn. For instance, if you  began to Cast a Spell requiring 3 actions and the first action  was dis |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/17` | 0.673187 | Using an activity isn't the same as using any of  its subordinate actions. For example, the quickened  condition you get from the *haste* spell lets you spend  an extra action each turn to Stride or S |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/7` | 0.618334 | There are four types of actions: single actions, activities,  reactions, and free actions. |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/21` | 0.616276 | An activity might cause you to use specific actions within  it. You don't have to spend additional actions to perform  them—they're already factored into the activity's required  actions. (See Subordi |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/2` | 0.614376 | This limitation of one action per trigger is per creature;  more than one creature can use a reaction or free action  in response to a given trigger. If multiple actions would be  occurring at the sam |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/4` | 0.609412 | Sometimes you need to attempt something not already  covered by defined actions in the game. When this happens,  the rules tell you how many actions you need to spend as  well as any traits your actio |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/11` | 0.607741 | These rules clarify some of the specifics of using actions. |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/1` | 0.604884 | free actions limit when you can use those actions. You can use  only one action in response to a given trigger. For example, if  you had a reaction and a free action that both had a trigger  of "your |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/2/Text/4` | 0.593296 | In addition to the actions in these two sections, the actions  for spellcasting can be found on page 298, and the actions for  using magic items appear on page 282. |

### Query 17
- Text: What is the rule about An activity might cause you to use specific actions within  it. You don't have to spend additional actions to perform  them—they're already factored into the activity's required  actions. (See Subordinate Actions on page 407.)?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/0/Text/21']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 406-423::/page/0/Text/21', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/11', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/17']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/0/Text/21', 'PZO22001 Starfinder Player Core 406-423::/page/0/Text/22', 'PZO22001 Starfinder Player Core 406-423::/page/0/Text/20']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 406-423::/page/0/Text/22` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/0/Text/20` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/21` | 1.005789 | An activity might cause you to use specific actions within  it. You don't have to spend additional actions to perform  them—they're already factored into the activity's required  actions. (See Subordi |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/11` | 0.735325 | These rules clarify some of the specifics of using actions. |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/17` | 0.715835 | Using an activity isn't the same as using any of  its subordinate actions. For example, the quickened  condition you get from the *haste* spell lets you spend  an extra action each turn to Stride or S |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/16` | 0.681475 | An action might allow you to use a simpler action usually one of the Basic Actions on page 408—in a  different circumstance or with different effects. This  subordinate action still has its normal tra |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/4` | 0.653072 | Sometimes you need to attempt something not already  covered by defined actions in the game. When this happens,  the rules tell you how many actions you need to spend as  well as any traits your actio |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/20` | 0.608619 | An activity typically involves using multiple actions to create  an effect greater than you can produce with a single action,  or combining multiple single actions to produce an effect  that's differe |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/2/Text/2` | 0.596777 | Basic actions represent common tasks like moving around,  attacking, and helping others. As such, every creature can  use basic actions except in some extreme circumstances,  and many of those actions |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/27` | 0.592330 | You can use free actions that have triggers and reactions only  in response to certain events. Each such reaction and free  action lists the trigger that must happen for you to perform it.  When its t |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/22` | 0.588817 | You have to spend all the actions of an activity at once  to gain its effects. In an encounter, this means you must  complete it during your turn. If an activity gets interrupted or  disrupted in an e |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/6` | 0.572988 | Effects can change the number of actions you can use on  your turn, or whether you can use actions at all. The slowed  condition, for example, causes you to lose actions, while the  quickened conditio |

### Query 18
- Text: What is the rule about You have to spend all the actions of an activity at once  to gain its effects. In an encounter, this means you must  complete it during your turn. If an activity gets interrupted or  disrupted in an encounter (page 407), you lose all the actions  you committed to it.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/0/Text/22']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 406-423::/page/0/Text/22', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/18', 'PZO22001 Starfinder Player Core 406-423::/page/0/Text/25']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/0/Text/22', 'PZO22001 Starfinder Player Core 406-423::/page/0/Text/21', 'PZO22001 Starfinder Player Core 406-423::/page/0/SectionHeader/23']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 406-423::/page/0/Text/21` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/0/SectionHeader/23` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/22` | 0.999043 | You have to spend all the actions of an activity at once  to gain its effects. In an encounter, this means you must  complete it during your turn. If an activity gets interrupted or  disrupted in an e |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/18` | 0.806478 | case of an activity, you usually lose all actions spent for the  activity up through the end of that turn. For instance, if you  began to Cast a Spell requiring 3 actions and the first action  was dis |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/25` | 0.724626 | If an activity outside of an encounter is interrupted or  disrupted, as described in Disrupting Actions on page 407,  you usually lose the time you put in, but no additional time. |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/6` | 0.682193 | You'll need to track your actions carefully in an encounter. At  the start of each turn you take in an encounter, you regain 3  actions and 1 reaction to spend that round. (Regaining your  actions is |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/6` | 0.632961 | Effects can change the number of actions you can use on  your turn, or whether you can use actions at all. The slowed  condition, for example, causes you to lose actions, while the  quickened conditio |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/4` | 0.622274 | Sometimes you need to attempt something not already  covered by defined actions in the game. When this happens,  the rules tell you how many actions you need to spend as  well as any traits your actio |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/9` | 0.613053 | Various abilities and conditions, such as a Reactive Strike,  can disrupt an action. When an action is disrupted, you still  use the actions or reactions you committed, and you still  expend any costs |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/17` | 0.589463 | Using an activity isn't the same as using any of  its subordinate actions. For example, the quickened  condition you get from the *haste* spell lets you spend  an extra action each turn to Stride or S |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/21` | 0.585246 | An activity might cause you to use specific actions within  it. You don't have to spend additional actions to perform  them—they're already factored into the activity's required  actions. (See Subordi |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/2` | 0.582849 | You affect the world around you primarily by using actions, which produce effects. Actions are most  closely measured and restricted during the encounter mode of play, but even when it isn't important |

### Query 19
- Text: What is the rule about EXPLORATION AND DOWNTIME  ACTIVITIES?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/0/SectionHeader/23']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 406-423::/page/0/SectionHeader/23', 'PZO22001 Starfinder Player Core 406-423::/page/0/Text/24', 'PZO22001 Starfinder Player Core 406-423::/page/11/Text/41']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/0/SectionHeader/23', 'PZO22001 Starfinder Player Core 406-423::/page/0/Text/24', 'PZO22001 Starfinder Player Core 406-423::/page/0/Text/22']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 406-423::/page/0/Text/24` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/0/Text/22` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/0/SectionHeader/23` | 0.888749 | EXPLORATION AND DOWNTIME  ACTIVITIES |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/24` | 0.588137 | Outside of encounters, activities can take minutes, hours, or  even days. These activities usually have the exploration or  downtime trait to indicate they're meant to be used during  these modes of p |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/11/Text/41` | 0.548064 | **Exploration ** |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/25` | 0.506064 | **Exploration ** |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/6/Text/2` | 0.492598 | Your movement and position determine how you interact with the world. Moving in exploration and  downtime modes is relatively fluid. Movement in encounter mode follows additional rules explained in  T |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/17/Text/47` | 0.483379 | Exploration Mode |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/1/SectionHeader/10` | 0.469139 | **IN-DEPTH ACTION RULES** |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/22` | 0.449314 | You have to spend all the actions of an activity at once  to gain its effects. In an encounter, this means you must  complete it during your turn. If an activity gets interrupted or  disrupted in an e |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/17/Text/32` | 0.423948 | Rules Overview |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/13` | 0.419442 | You can use only one single action, activity, or free action  that doesn't have a trigger at a time. You must complete  one before beginning another. For example, the Double  Tap activity states you m |

### Query 20
- Text: What is the rule about Outside of encounters, activities can take minutes, hours, or  even days. These activities usually have the exploration or  downtime trait to indicate they're meant to be used during  these modes of play. You can often do other things off and on as  you carry out these activities, provided they aren't significant  activities of their own. For instance, if you're Repairing an  item, you might stretch your legs or have a brief discussion,  but you couldn't Decipher Writing at the same time.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/0/Text/24']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 406-423::/page/0/Text/24', 'PZO22001 Starfinder Player Core 406-423::/page/0/Text/25', 'PZO22001 Starfinder Player Core 406-423::/page/6/Text/2']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/0/Text/24', 'PZO22001 Starfinder Player Core 406-423::/page/0/Text/25', 'PZO22001 Starfinder Player Core 406-423::/page/0/SectionHeader/23']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 406-423::/page/0/Text/25` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/0/SectionHeader/23` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/24` | 1.000842 | Outside of encounters, activities can take minutes, hours, or  even days. These activities usually have the exploration or  downtime trait to indicate they're meant to be used during  these modes of p |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/25` | 0.695017 | If an activity outside of an encounter is interrupted or  disrupted, as described in Disrupting Actions on page 407,  you usually lose the time you put in, but no additional time. |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/6/Text/2` | 0.650735 | Your movement and position determine how you interact with the world. Moving in exploration and  downtime modes is relatively fluid. Movement in encounter mode follows additional rules explained in  T |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/22` | 0.607328 | You have to spend all the actions of an activity at once  to gain its effects. In an encounter, this means you must  complete it during your turn. If an activity gets interrupted or  disrupted in an e |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/4` | 0.565486 | Sometimes you need to attempt something not already  covered by defined actions in the game. When this happens,  the rules tell you how many actions you need to spend as  well as any traits your actio |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/12/Text/7` | 0.562364 | Most effects are discrete, creating an instantaneous effect  when you let the GM know what actions you're going to use.  Firing a gun, moving to a new space, or taking something  out of your pack all |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/17` | 0.558980 | Using an activity isn't the same as using any of  its subordinate actions. For example, the quickened  condition you get from the *haste* spell lets you spend  an extra action each turn to Stride or S |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/2` | 0.553805 | You affect the world around you primarily by using actions, which produce effects. Actions are most  closely measured and restricted during the encounter mode of play, but even when it isn't important |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/13` | 0.541927 | You can use only one single action, activity, or free action  that doesn't have a trigger at a time. You must complete  one before beginning another. For example, the Double  Tap activity states you m |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/6` | 0.537390 | You'll need to track your actions carefully in an encounter. At  the start of each turn you take in an encounter, you regain 3  actions and 1 reaction to spend that round. (Regaining your  actions is |

### Query 21
- Text: What is the rule about If an activity outside of an encounter is interrupted or  disrupted, as described in Disrupting Actions on page 407,  you usually lose the time you put in, but no additional time.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/0/Text/25']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 406-423::/page/0/Text/25', 'PZO22001 Starfinder Player Core 406-423::/page/0/Text/22', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/18']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/0/Text/25', 'PZO22001 Starfinder Player Core 406-423::/page/0/Text/24', 'PZO22001 Starfinder Player Core 406-423::/page/0/SectionHeader/26']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 406-423::/page/0/Text/24` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/0/SectionHeader/26` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/25` | 0.992927 | If an activity outside of an encounter is interrupted or  disrupted, as described in Disrupting Actions on page 407,  you usually lose the time you put in, but no additional time. |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/22` | 0.756980 | You have to spend all the actions of an activity at once  to gain its effects. In an encounter, this means you must  complete it during your turn. If an activity gets interrupted or  disrupted in an e |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/18` | 0.685735 | case of an activity, you usually lose all actions spent for the  activity up through the end of that turn. For instance, if you  began to Cast a Spell requiring 3 actions and the first action  was dis |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/24` | 0.620931 | Outside of encounters, activities can take minutes, hours, or  even days. These activities usually have the exploration or  downtime trait to indicate they're meant to be used during  these modes of p |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/9` | 0.614270 | Various abilities and conditions, such as a Reactive Strike,  can disrupt an action. When an action is disrupted, you still  use the actions or reactions you committed, and you still  expend any costs |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/19` | 0.581932 | The GM decides what effects a disruption causes beyond  simply negating the effects that would've occurred from  the disrupted action. For instance, a Leap disrupted midway  wouldn't transport you bac |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/6` | 0.554078 | Effects can change the number of actions you can use on  your turn, or whether you can use actions at all. The slowed  condition, for example, causes you to lose actions, while the  quickened conditio |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/17` | 0.553398 | Using an activity isn't the same as using any of  its subordinate actions. For example, the quickened  condition you get from the *haste* spell lets you spend  an extra action each turn to Stride or S |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/2/Text/20` | 0.536482 | You wait for the right moment to act. The rest of your  turn doesn't happen yet. Instead, you're removed from the  initiative order. You can return to the initiative order as a free  action triggered |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/21` | 0.529348 | An activity might cause you to use specific actions within  it. You don't have to spend additional actions to perform  them—they're already factored into the activity's required  actions. (See Subordi |

### Query 22
- Text: What is the rule about ACTIONS WITH TRIGGERS?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/0/SectionHeader/26']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 406-423::/page/0/SectionHeader/26', 'PZO22001 Starfinder Player Core 406-423::/page/0/SectionHeader/29', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/14']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/0/SectionHeader/26', 'PZO22001 Starfinder Player Core 406-423::/page/0/Text/25', 'PZO22001 Starfinder Player Core 406-423::/page/0/Text/27']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 406-423::/page/0/Text/25` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/0/Text/27` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/0/SectionHeader/26` | 0.883719 | ACTIONS WITH TRIGGERS |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/0/SectionHeader/29` | 0.687297 | LIMITATIONS ON TRIGGERS |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/14` | 0.653691 | Free actions with triggers and reactions work  differently. You can use these whenever the trigger  occurs, even if the trigger occurs in the middle of  another action. |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/11` | 0.572737 | **Free actions** don't cost you any of your actions per turn,  nor do they cost your reaction. A free action with no trigger  follows the same rules as a single action (except the action  cost). It mu |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/27` | 0.571489 | You can use free actions that have triggers and reactions only  in response to certain events. Each such reaction and free  action lists the trigger that must happen for you to perform it.  When its t |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/11` | 0.568453 | These rules clarify some of the specifics of using actions. |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/2` | 0.539845 | This limitation of one action per trigger is per creature;  more than one creature can use a reaction or free action  in response to a given trigger. If multiple actions would be  occurring at the sam |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/1` | 0.534138 | free actions limit when you can use those actions. You can use  only one action in response to a given trigger. For example, if  you had a reaction and a free action that both had a trigger  of "your |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/8` | 0.518496 | You prepare to use an action that will occur outside your  turn. Choose a single action or free action you can use, and  designate a trigger. Your turn then ends. If the trigger you  designated occurs |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/13` | 0.517799 | You can use only one single action, activity, or free action  that doesn't have a trigger at a time. You must complete  one before beginning another. For example, the Double  Tap activity states you m |

### Query 23
- Text: What is the rule about You can use free actions that have triggers and reactions only  in response to certain events. Each such reaction and free  action lists the trigger that must happen for you to perform it.  When its trigger is satisfied—and *only* when it's satisfied—you  can use the reaction or free action, though you don't have to  use the action if you don't want to.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/0/Text/27']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 406-423::/page/0/Text/27', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/14', 'PZO22001 Starfinder Player Core 406-423::/page/0/Text/11']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/0/Text/27', 'PZO22001 Starfinder Player Core 406-423::/page/0/SectionHeader/26', 'PZO22001 Starfinder Player Core 406-423::/page/0/Text/28']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 406-423::/page/0/SectionHeader/26` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/0/Text/28` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/27` | 0.999999 | You can use free actions that have triggers and reactions only  in response to certain events. Each such reaction and free  action lists the trigger that must happen for you to perform it.  When its t |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/14` | 0.829535 | Free actions with triggers and reactions work  differently. You can use these whenever the trigger  occurs, even if the trigger occurs in the middle of  another action. |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/11` | 0.816550 | **Free actions** don't cost you any of your actions per turn,  nor do they cost your reaction. A free action with no trigger  follows the same rules as a single action (except the action  cost). It mu |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/1` | 0.766973 | free actions limit when you can use those actions. You can use  only one action in response to a given trigger. For example, if  you had a reaction and a free action that both had a trigger  of "your |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/8` | 0.750721 | You prepare to use an action that will occur outside your  turn. Choose a single action or free action you can use, and  designate a trigger. Your turn then ends. If the trigger you  designated occurs |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/13` | 0.695868 | You can use only one single action, activity, or free action  that doesn't have a trigger at a time. You must complete  one before beginning another. For example, the Double  Tap activity states you m |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/10` | 0.692169 | **Reactions** have triggers, which must be met for you to use  the reaction. You can use a reaction anytime its trigger is met,  whether it's your turn or not. Outside of encounters, your use  of reac |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/2` | 0.652796 | This limitation of one action per trigger is per creature;  more than one creature can use a reaction or free action  in response to a given trigger. If multiple actions would be  occurring at the sam |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/28` | 0.627132 | There are only a few basic reactions and free actions that  all characters can use. You're more likely to gain actions with  triggers from your class, feats, and magic items. |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/11` | 0.617639 | These rules clarify some of the specifics of using actions. |

### Query 24
- Text: What is the rule about There are only a few basic reactions and free actions that  all characters can use. You're more likely to gain actions with  triggers from your class, feats, and magic items.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/0/Text/28']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 406-423::/page/0/Text/28', 'PZO22001 Starfinder Player Core 406-423::/page/0/Text/11', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/1']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/0/Text/28', 'PZO22001 Starfinder Player Core 406-423::/page/0/SectionHeader/29', 'PZO22001 Starfinder Player Core 406-423::/page/0/Text/27']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 406-423::/page/0/SectionHeader/29` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/0/Text/27` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/28` | 0.966227 | There are only a few basic reactions and free actions that  all characters can use. You're more likely to gain actions with  triggers from your class, feats, and magic items. |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/11` | 0.772860 | **Free actions** don't cost you any of your actions per turn,  nor do they cost your reaction. A free action with no trigger  follows the same rules as a single action (except the action  cost). It mu |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/1` | 0.726968 | free actions limit when you can use those actions. You can use  only one action in response to a given trigger. For example, if  you had a reaction and a free action that both had a trigger  of "your |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/27` | 0.686043 | You can use free actions that have triggers and reactions only  in response to certain events. Each such reaction and free  action lists the trigger that must happen for you to perform it.  When its t |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/10` | 0.671457 | **Reactions** have triggers, which must be met for you to use  the reaction. You can use a reaction anytime its trigger is met,  whether it's your turn or not. Outside of encounters, your use  of reac |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/14` | 0.655644 | Free actions with triggers and reactions work  differently. You can use these whenever the trigger  occurs, even if the trigger occurs in the middle of  another action. |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/2` | 0.641288 | This limitation of one action per trigger is per creature;  more than one creature can use a reaction or free action  in response to a given trigger. If multiple actions would be  occurring at the sam |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/2/Text/2` | 0.601131 | Basic actions represent common tasks like moving around,  attacking, and helping others. As such, every creature can  use basic actions except in some extreme circumstances,  and many of those actions |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/8` | 0.595646 | You prepare to use an action that will occur outside your  turn. Choose a single action or free action you can use, and  designate a trigger. Your turn then ends. If the trigger you  designated occurs |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/13` | 0.590589 | You can use only one single action, activity, or free action  that doesn't have a trigger at a time. You must complete  one before beginning another. For example, the Double  Tap activity states you m |

### Query 25
- Text: Summarize LIMITATIONS ON TRIGGERS
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/0/SectionHeader/29']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 406-423::/page/0/SectionHeader/29', 'PZO22001 Starfinder Player Core 406-423::/page/0/SectionHeader/26', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/2']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/0/SectionHeader/29', 'PZO22001 Starfinder Player Core 406-423::/page/0/Text/30', 'PZO22001 Starfinder Player Core 406-423::/page/0/Text/28']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 406-423::/page/0/Text/30` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/0/Text/28` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/0/SectionHeader/29` | 1.007112 | LIMITATIONS ON TRIGGERS |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/0/SectionHeader/26` | 0.726075 | ACTIONS WITH TRIGGERS |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/2` | 0.532013 | This limitation of one action per trigger is per creature;  more than one creature can use a reaction or free action  in response to a given trigger. If multiple actions would be  occurring at the sam |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/1` | 0.411509 | free actions limit when you can use those actions. You can use  only one action in response to a given trigger. For example, if  you had a reaction and a free action that both had a trigger  of "your |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/30` | 0.411339 | The triggers listed in the stat blocks of reactions and some |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/8/Text/5` | 0.404263 | **Trigger** A creature within your reach uses a manipulate  action or a move action, makes a ranged attack, or  leaves a square during a move action it's using. |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/4/Text/31` | 0.391534 | **Trigger** You fall. |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/2/SectionHeader/19` | 0.380302 | **Trigger** Your turn begins. |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/16` | 0.380231 | **Trigger** You fall from or past an edge or handhold. |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/14` | 0.376498 | Free actions with triggers and reactions work  differently. You can use these whenever the trigger  occurs, even if the trigger occurs in the middle of  another action. |

### Query 26
- Text: What is the rule about The triggers listed in the stat blocks of reactions and some?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/0/Text/30']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 406-423::/page/0/Text/30', 'PZO22001 Starfinder Player Core 406-423::/page/0/Text/10', 'PZO22001 Starfinder Player Core 406-423::/page/0/Text/27']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/0/Text/30', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/1', 'PZO22001 Starfinder Player Core 406-423::/page/0/SectionHeader/29']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 406-423::/page/1/Text/1` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/0/SectionHeader/29` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/30` | 0.927415 | The triggers listed in the stat blocks of reactions and some |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/10` | 0.642157 | **Reactions** have triggers, which must be met for you to use  the reaction. You can use a reaction anytime its trigger is met,  whether it's your turn or not. Outside of encounters, your use  of reac |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/27` | 0.605956 | You can use free actions that have triggers and reactions only  in response to certain events. Each such reaction and free  action lists the trigger that must happen for you to perform it.  When its t |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/14` | 0.562266 | Free actions with triggers and reactions work  differently. You can use these whenever the trigger  occurs, even if the trigger occurs in the middle of  another action. |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/2` | 0.545801 | This limitation of one action per trigger is per creature;  more than one creature can use a reaction or free action  in response to a given trigger. If multiple actions would be  occurring at the sam |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/1` | 0.539607 | free actions limit when you can use those actions. You can use  only one action in response to a given trigger. For example, if  you had a reaction and a free action that both had a trigger  of "your |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/11` | 0.539519 | **Free actions** don't cost you any of your actions per turn,  nor do they cost your reaction. A free action with no trigger  follows the same rules as a single action (except the action  cost). It mu |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/8` | 0.515858 | You prepare to use an action that will occur outside your  turn. Choose a single action or free action you can use, and  designate a trigger. Your turn then ends. If the trigger you  designated occurs |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/28` | 0.515798 | There are only a few basic reactions and free actions that  all characters can use. You're more likely to gain actions with  triggers from your class, feats, and magic items. |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/8/Text/2` | 0.507167 | Some reactions and free actions are triggered by a  creature using an action with the move trait. The most  notable example is Reactive Strike (reproduced below).  Actions with the move trait can trig |

### Query 27
- Text: What is the rule about free actions limit when you can use those actions. You can use  only one action in response to a given trigger. For example, if  you had a reaction and a free action that both had a trigger  of "your turn begins," you could use either of them at the  start of your turn—but not both. If two triggers are similar,  but not identical, the GM determines whether you can use  one action in response to each or whether they're effectively  the same thing. Usually, this decision will be based on what's  happening in the narrative.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/1', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/2', 'PZO22001 Starfinder Player Core 406-423::/page/0/Text/27']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/1', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/2', 'PZO22001 Starfinder Player Core 406-423::/page/0/Text/30']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 406-423::/page/1/Text/2` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/0/Text/30` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/1` | 1.010487 | free actions limit when you can use those actions. You can use  only one action in response to a given trigger. For example, if  you had a reaction and a free action that both had a trigger  of "your |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/2` | 0.821796 | This limitation of one action per trigger is per creature;  more than one creature can use a reaction or free action  in response to a given trigger. If multiple actions would be  occurring at the sam |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/27` | 0.802187 | You can use free actions that have triggers and reactions only  in response to certain events. Each such reaction and free  action lists the trigger that must happen for you to perform it.  When its t |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/11` | 0.743777 | **Free actions** don't cost you any of your actions per turn,  nor do they cost your reaction. A free action with no trigger  follows the same rules as a single action (except the action  cost). It mu |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/14` | 0.741671 | Free actions with triggers and reactions work  differently. You can use these whenever the trigger  occurs, even if the trigger occurs in the middle of  another action. |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/8` | 0.722668 | You prepare to use an action that will occur outside your  turn. Choose a single action or free action you can use, and  designate a trigger. Your turn then ends. If the trigger you  designated occurs |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/13` | 0.660427 | You can use only one single action, activity, or free action  that doesn't have a trigger at a time. You must complete  one before beginning another. For example, the Double  Tap activity states you m |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/10` | 0.655234 | **Reactions** have triggers, which must be met for you to use  the reaction. You can use a reaction anytime its trigger is met,  whether it's your turn or not. Outside of encounters, your use  of reac |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/28` | 0.623095 | There are only a few basic reactions and free actions that  all characters can use. You're more likely to gain actions with  triggers from your class, feats, and magic items. |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/7` | 0.611808 | Some effects are even more restrictive. Certain abilities,  instead of or in addition to changing the number of actions  you can use, say specifically that you can't use reactions.  The most restricti |

### Query 28
- Text: What is the rule about This limitation of one action per trigger is per creature;  more than one creature can use a reaction or free action  in response to a given trigger. If multiple actions would be  occurring at the same time, and it's unclear in what order  they happen, the GM determines the order based on the  narrative.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/2', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/1', 'PZO22001 Starfinder Player Core 406-423::/page/0/Text/27']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/2', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/1', 'PZO22001 Starfinder Player Core 406-423::/page/1/SectionHeader/3']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 406-423::/page/1/Text/1` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/1/SectionHeader/3` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/2` | 1.000636 | This limitation of one action per trigger is per creature;  more than one creature can use a reaction or free action  in response to a given trigger. If multiple actions would be  occurring at the sam |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/1` | 0.816148 | free actions limit when you can use those actions. You can use  only one action in response to a given trigger. For example, if  you had a reaction and a free action that both had a trigger  of "your |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/27` | 0.689083 | You can use free actions that have triggers and reactions only  in response to certain events. Each such reaction and free  action lists the trigger that must happen for you to perform it.  When its t |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/8` | 0.631581 | You prepare to use an action that will occur outside your  turn. Choose a single action or free action you can use, and  designate a trigger. Your turn then ends. If the trigger you  designated occurs |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/10` | 0.627569 | **Reactions** have triggers, which must be met for you to use  the reaction. You can use a reaction anytime its trigger is met,  whether it's your turn or not. Outside of encounters, your use  of reac |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/11` | 0.623429 | **Free actions** don't cost you any of your actions per turn,  nor do they cost your reaction. A free action with no trigger  follows the same rules as a single action (except the action  cost). It mu |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/14` | 0.622033 | Free actions with triggers and reactions work  differently. You can use these whenever the trigger  occurs, even if the trigger occurs in the middle of  another action. |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/13` | 0.596207 | You can use only one single action, activity, or free action  that doesn't have a trigger at a time. You must complete  one before beginning another. For example, the Double  Tap activity states you m |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/8/Text/2` | 0.588888 | Some reactions and free actions are triggered by a  creature using an action with the move trait. The most  notable example is Reactive Strike (reproduced below).  Actions with the move trait can trig |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/20` | 0.584472 | An activity typically involves using multiple actions to create  an effect greater than you can produce with a single action,  or combining multiple single actions to produce an effect  that's differe |

### Query 29
- Text: What is the rule about OTHER ACTIONS?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/SectionHeader/3']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 406-423::/page/1/SectionHeader/3', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/11', 'PZO22001 Starfinder Player Core 406-423::/page/0/SectionHeader/1']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/SectionHeader/3', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/4', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/2']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 406-423::/page/1/Text/4` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/1/Text/2` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/1/SectionHeader/3` | 0.841369 | OTHER ACTIONS |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/11` | 0.693013 | These rules clarify some of the specifics of using actions. |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/0/SectionHeader/1` | 0.621595 | ACTIONS |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/17/Text/39` | 0.558510 | Actions |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/61` | 0.553549 | **Actions** |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/15/Text/27` | 0.553549 | **Actions** |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/44` | 0.553549 | **Actions** |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/36` | 0.553549 | **Actions** |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/48` | 0.553549 | **Actions** |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/9/Text/37` | 0.553549 | **Actions** |

### Query 30
- Text: What is the rule about Sometimes you need to attempt something not already  covered by defined actions in the game. When this happens,  the rules tell you how many actions you need to spend as  well as any traits your action might have. For example, a  spell that lets you switch targets might say you can do so  "by spending a single action, which has the concentrate trait."  Game Masters can also use this approach when a character  tries to do something that isn't covered in the rules.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/4', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/17', 'PZO22001 Starfinder Player Core 406-423::/page/0/Text/21']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/4', 'PZO22001 Starfinder Player Core 406-423::/page/1/SectionHeader/3', 'PZO22001 Starfinder Player Core 406-423::/page/1/SectionHeader/5']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 406-423::/page/1/SectionHeader/3` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/1/SectionHeader/5` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/4` | 1.023133 | Sometimes you need to attempt something not already  covered by defined actions in the game. When this happens,  the rules tell you how many actions you need to spend as  well as any traits your actio |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/17` | 0.675492 | Using an activity isn't the same as using any of  its subordinate actions. For example, the quickened  condition you get from the *haste* spell lets you spend  an extra action each turn to Stride or S |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/21` | 0.669012 | An activity might cause you to use specific actions within  it. You don't have to spend additional actions to perform  them—they're already factored into the activity's required  actions. (See Subordi |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/22` | 0.609106 | You have to spend all the actions of an activity at once  to gain its effects. In an encounter, this means you must  complete it during your turn. If an activity gets interrupted or  disrupted in an e |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/1` | 0.601858 | free actions limit when you can use those actions. You can use  only one action in response to a given trigger. For example, if  you had a reaction and a free action that both had a trigger  of "your |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/20` | 0.584064 | An activity typically involves using multiple actions to create  an effect greater than you can produce with a single action,  or combining multiple single actions to produce an effect  that's differe |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/16` | 0.582508 | An action might allow you to use a simpler action usually one of the Basic Actions on page 408—in a  different circumstance or with different effects. This  subordinate action still has its normal tra |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/18` | 0.578140 | case of an activity, you usually lose all actions spent for the  activity up through the end of that turn. For instance, if you  began to Cast a Spell requiring 3 actions and the first action  was dis |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/6` | 0.568812 | You'll need to track your actions carefully in an encounter. At  the start of each turn you take in an encounter, you regain 3  actions and 1 reaction to spend that round. (Regaining your  actions is |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/13` | 0.562241 | You can use only one single action, activity, or free action  that doesn't have a trigger at a time. You must complete  one before beginning another. For example, the Double  Tap activity states you m |

### Query 31
- Text: What is the rule about GAINING AND LOSING  ACTIONS?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/SectionHeader/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 406-423::/page/1/SectionHeader/5', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/18', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/11']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/SectionHeader/5', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/4', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/6']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 406-423::/page/1/Text/4` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/1/Text/6` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/1/SectionHeader/5` | 0.913451 | GAINING AND LOSING  ACTIONS |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/18` | 0.569630 | case of an activity, you usually lose all actions spent for the  activity up through the end of that turn. For instance, if you  began to Cast a Spell requiring 3 actions and the first action  was dis |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/11` | 0.563813 | These rules clarify some of the specifics of using actions. |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/6` | 0.523997 | Effects can change the number of actions you can use on  your turn, or whether you can use actions at all. The slowed  condition, for example, causes you to lose actions, while the  quickened conditio |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/22` | 0.519278 | You have to spend all the actions of an activity at once  to gain its effects. In an encounter, this means you must  complete it during your turn. If an activity gets interrupted or  disrupted in an e |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/6` | 0.517032 | You'll need to track your actions carefully in an encounter. At  the start of each turn you take in an encounter, you regain 3  actions and 1 reaction to spend that round. (Regaining your  actions is |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/4` | 0.471956 | Sometimes you need to attempt something not already  covered by defined actions in the game. When this happens,  the rules tell you how many actions you need to spend as  well as any traits your actio |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/1` | 0.456816 | free actions limit when you can use those actions. You can use  only one action in response to a given trigger. For example, if  you had a reaction and a free action that both had a trigger  of "your |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/2/Text/20` | 0.447662 | You wait for the right moment to act. The rest of your  turn doesn't happen yet. Instead, you're removed from the  initiative order. You can return to the initiative order as a free  action triggered |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/0/ListItem/15` | 0.440333 | [two-actions] Two-Action Activity |

### Query 32
- Text: What is the rule about Effects can change the number of actions you can use on  your turn, or whether you can use actions at all. The slowed  condition, for example, causes you to lose actions, while the  quickened condition causes you to gain them. Conditions are  detailed in the appendix on pages 435–441. Whenever you  lose a number of actions—whether from these conditions or  in any other way—you choose which to lose if there's any  difference between them. For instance, the *haste* spell makes  you quickened, but it limits what you can use your extra  action to do. If you lost an action while *haste* was active, you  might want to lose the action from *haste* first since it's more  limited than your normal actions.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/6', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/17', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/18']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/6', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/7', 'PZO22001 Starfinder Player Core 406-423::/page/1/SectionHeader/5']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 406-423::/page/1/Text/7` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/1/SectionHeader/5` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/6` | 1.010901 | Effects can change the number of actions you can use on  your turn, or whether you can use actions at all. The slowed  condition, for example, causes you to lose actions, while the  quickened conditio |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/17` | 0.764376 | Using an activity isn't the same as using any of  its subordinate actions. For example, the quickened  condition you get from the *haste* spell lets you spend  an extra action each turn to Stride or S |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/18` | 0.723862 | case of an activity, you usually lose all actions spent for the  activity up through the end of that turn. For instance, if you  began to Cast a Spell requiring 3 actions and the first action  was dis |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/7` | 0.688288 | Some effects are even more restrictive. Certain abilities,  instead of or in addition to changing the number of actions  you can use, say specifically that you can't use reactions.  The most restricti |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/22` | 0.638802 | You have to spend all the actions of an activity at once  to gain its effects. In an encounter, this means you must  complete it during your turn. If an activity gets interrupted or  disrupted in an e |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/1` | 0.625162 | free actions limit when you can use those actions. You can use  only one action in response to a given trigger. For example, if  you had a reaction and a free action that both had a trigger  of "your |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/16` | 0.622525 | An action might allow you to use a simpler action usually one of the Basic Actions on page 408—in a  different circumstance or with different effects. This  subordinate action still has its normal tra |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/4` | 0.594893 | Sometimes you need to attempt something not already  covered by defined actions in the game. When this happens,  the rules tell you how many actions you need to spend as  well as any traits your actio |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/58` | 0.592819 | Some effects apply conditions to a creature or item. These change your state of being in some way. Conditions are  persistent, lasting until the stated duration ends, the condition is removed, or term |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/9` | 0.591526 | Various abilities and conditions, such as a Reactive Strike,  can disrupt an action. When an action is disrupted, you still  use the actions or reactions you committed, and you still  expend any costs |

### Query 33
- Text: What is the rule about Some effects are even more restrictive. Certain abilities,  instead of or in addition to changing the number of actions  you can use, say specifically that you can't use reactions.  The most restrictive form of reducing actions is when an  effect states that you can't act: this means you can't use  any actions, or even speak. When you can't act, you still  regain your actions unless another effect (like the stunned  condition) prevents it.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/7', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/6', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/9']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/7', 'PZO22001 Starfinder Player Core 406-423::/page/1/SectionHeader/8', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/6']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 406-423::/page/1/SectionHeader/8` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/1/Text/6` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/7` | 1.015329 | Some effects are even more restrictive. Certain abilities,  instead of or in addition to changing the number of actions  you can use, say specifically that you can't use reactions.  The most restricti |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/6` | 0.708052 | Effects can change the number of actions you can use on  your turn, or whether you can use actions at all. The slowed  condition, for example, causes you to lose actions, while the  quickened conditio |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/9` | 0.705968 | Various abilities and conditions, such as a Reactive Strike,  can disrupt an action. When an action is disrupted, you still  use the actions or reactions you committed, and you still  expend any costs |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/1` | 0.623159 | free actions limit when you can use those actions. You can use  only one action in response to a given trigger. For example, if  you had a reaction and a free action that both had a trigger  of "your |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/27` | 0.612588 | You can use free actions that have triggers and reactions only  in response to certain events. Each such reaction and free  action lists the trigger that must happen for you to perform it.  When its t |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/2` | 0.598255 | You affect the world around you primarily by using actions, which produce effects. Actions are most  closely measured and restricted during the encounter mode of play, but even when it isn't important |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/11` | 0.587557 | These rules clarify some of the specifics of using actions. |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/17` | 0.586957 | Using an activity isn't the same as using any of  its subordinate actions. For example, the quickened  condition you get from the *haste* spell lets you spend  an extra action each turn to Stride or S |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/16` | 0.581664 | An action might allow you to use a simpler action usually one of the Basic Actions on page 408—in a  different circumstance or with different effects. This  subordinate action still has its normal tra |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/2` | 0.580147 | This limitation of one action per trigger is per creature;  more than one creature can use a reaction or free action  in response to a given trigger. If multiple actions would be  occurring at the sam |

### Query 34
- Text: What is the rule about DISRUPTING ACTIONS?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/SectionHeader/8']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 406-423::/page/1/SectionHeader/8', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/9', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/11']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/SectionHeader/8', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/9', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/7']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 406-423::/page/1/Text/9` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/1/Text/7` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/1/SectionHeader/8` | 0.880369 | DISRUPTING ACTIONS |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/9` | 0.644083 | Various abilities and conditions, such as a Reactive Strike,  can disrupt an action. When an action is disrupted, you still  use the actions or reactions you committed, and you still  expend any costs |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/11` | 0.583962 | These rules clarify some of the specifics of using actions. |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/25` | 0.533724 | If an activity outside of an encounter is interrupted or  disrupted, as described in Disrupting Actions on page 407,  you usually lose the time you put in, but no additional time. |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/43` | 0.524840 | If your Sustain action is disrupted, the ability ends. |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/19` | 0.524762 | The GM decides what effects a disruption causes beyond  simply negating the effects that would've occurred from  the disrupted action. For instance, a Leap disrupted midway  wouldn't transport you bac |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/22` | 0.520495 | You have to spend all the actions of an activity at once  to gain its effects. In an encounter, this means you must  complete it during your turn. If an activity gets interrupted or  disrupted in an e |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/18` | 0.511176 | case of an activity, you usually lose all actions spent for the  activity up through the end of that turn. For instance, if you  began to Cast a Spell requiring 3 actions and the first action  was dis |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/7` | 0.497249 | Some effects are even more restrictive. Certain abilities,  instead of or in addition to changing the number of actions  you can use, say specifically that you can't use reactions.  The most restricti |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/1/SectionHeader/10` | 0.488559 | **IN-DEPTH ACTION RULES** |

### Query 35
- Text: What is the rule about Various abilities and conditions, such as a Reactive Strike,  can disrupt an action. When an action is disrupted, you still  use the actions or reactions you committed, and you still  expend any costs, but the action's effects don't occur. In the?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/9', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/7', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/19']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/9', 'PZO22001 Starfinder Player Core 406-423::/page/1/SectionHeader/10', 'PZO22001 Starfinder Player Core 406-423::/page/1/SectionHeader/8']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 406-423::/page/1/SectionHeader/10` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/1/SectionHeader/8` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/9` | 1.004769 | Various abilities and conditions, such as a Reactive Strike,  can disrupt an action. When an action is disrupted, you still  use the actions or reactions you committed, and you still  expend any costs |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/7` | 0.690454 | Some effects are even more restrictive. Certain abilities,  instead of or in addition to changing the number of actions  you can use, say specifically that you can't use reactions.  The most restricti |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/19` | 0.657181 | The GM decides what effects a disruption causes beyond  simply negating the effects that would've occurred from  the disrupted action. For instance, a Leap disrupted midway  wouldn't transport you bac |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/22` | 0.611205 | You have to spend all the actions of an activity at once  to gain its effects. In an encounter, this means you must  complete it during your turn. If an activity gets interrupted or  disrupted in an e |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/18` | 0.604260 | case of an activity, you usually lose all actions spent for the  activity up through the end of that turn. For instance, if you  began to Cast a Spell requiring 3 actions and the first action  was dis |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/43` | 0.603041 | If your Sustain action is disrupted, the ability ends. |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/6` | 0.592102 | Effects can change the number of actions you can use on  your turn, or whether you can use actions at all. The slowed  condition, for example, causes you to lose actions, while the  quickened conditio |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/25` | 0.588405 | If an activity outside of an encounter is interrupted or  disrupted, as described in Disrupting Actions on page 407,  you usually lose the time you put in, but no additional time. |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/8/Text/6` | 0.576588 | You lash out at a foe that leaves an opening. Make a  melee Strike against the triggering creature. If your  attack is a critical hit and the trigger was a manipulate  action, you disrupt that action. |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/1` | 0.566545 | free actions limit when you can use those actions. You can use  only one action in response to a given trigger. For example, if  you had a reaction and a free action that both had a trigger  of "your |

### Query 36
- Text: What is the rule about **IN-DEPTH ACTION RULES**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/SectionHeader/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 406-423::/page/1/SectionHeader/10', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/11', 'PZO22001 Starfinder Player Core 406-423::/page/11/Text/27']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/SectionHeader/10', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/9', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/11']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 406-423::/page/1/Text/9` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/1/Text/11` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/1/SectionHeader/10` | 0.975812 | **IN-DEPTH ACTION RULES** |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/11` | 0.626404 | These rules clarify some of the specifics of using actions. |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/11/Text/27` | 0.568615 | **Rules Overview** |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/29` | 0.526615 | **Rules Overview** |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/7/Text/35` | 0.526615 | **Rules Overview** |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/37` | 0.526615 | **Rules Overview** |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/54` | 0.526615 | **Rules Overview** |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/41` | 0.526615 | **Rules Overview** |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/15/Text/20` | 0.526615 | **Rules Overview** |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/9/Text/30` | 0.526615 | **Rules Overview** |

### Query 37
- Text: What is the rule about These rules clarify some of the specifics of using actions.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/11', 'PZO22001 Starfinder Player Core 406-423::/page/0/Text/21', 'PZO22001 Starfinder Player Core 406-423::/page/2/Text/2']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/11', 'PZO22001 Starfinder Player Core 406-423::/page/1/SectionHeader/10', 'PZO22001 Starfinder Player Core 406-423::/page/1/SectionHeader/12']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 406-423::/page/1/SectionHeader/10` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/1/SectionHeader/12` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/11` | 0.957903 | These rules clarify some of the specifics of using actions. |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/21` | 0.668990 | An activity might cause you to use specific actions within  it. You don't have to spend additional actions to perform  them—they're already factored into the activity's required  actions. (See Subordi |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/2/Text/2` | 0.613398 | Basic actions represent common tasks like moving around,  attacking, and helping others. As such, every creature can  use basic actions except in some extreme circumstances,  and many of those actions |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/16` | 0.556976 | An action might allow you to use a simpler action usually one of the Basic Actions on page 408—in a  different circumstance or with different effects. This  subordinate action still has its normal tra |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/2` | 0.554687 | You affect the world around you primarily by using actions, which produce effects. Actions are most  closely measured and restricted during the encounter mode of play, but even when it isn't important |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/4/Text/25` | 0.551853 | These actions are useful under specific circumstances. The  Arrest a Fall, Burrow, and Fly actions require you to have a  special movement type (page 412). Area Fire and Auto-Fire  require you to use |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/7` | 0.530694 | There are four types of actions: single actions, activities,  reactions, and free actions. |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/4` | 0.529148 | Sometimes you need to attempt something not already  covered by defined actions in the game. When this happens,  the rules tell you how many actions you need to spend as  well as any traits your actio |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/17/Text/39` | 0.528931 | Actions |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/1/SectionHeader/10` | 0.527023 | **IN-DEPTH ACTION RULES** |

### Query 38
- Text: What is the rule about **Simultaneous Actions**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/SectionHeader/12']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 406-423::/page/1/SectionHeader/12', 'PZO22001 Starfinder Player Core 406-423::/page/0/ListItem/15', 'PZO22001 Starfinder Player Core 406-423::/page/0/Text/8']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/SectionHeader/12', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/11', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/13']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 406-423::/page/1/Text/11` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/1/Text/13` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/1/SectionHeader/12` | 0.915581 | **Simultaneous Actions** |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/0/ListItem/15` | 0.623416 | [two-actions] Two-Action Activity |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/8` | 0.612658 | **Single actions **can be completed in a very short time.  They're self-contained, and their effects are generated within  the span of that single action. |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/11` | 0.575533 | These rules clarify some of the specifics of using actions. |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/20` | 0.562404 | An activity typically involves using multiple actions to create  an effect greater than you can produce with a single action,  or combining multiple single actions to produce an effect  that's differe |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/13` | 0.548581 | You can use only one single action, activity, or free action  that doesn't have a trigger at a time. You must complete  one before beginning another. For example, the Double  Tap activity states you m |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/0/ListItem/14` | 0.544703 | [one-action] Single Action |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/9` | 0.540378 | **Activities** usually take longer and require using multiple  actions, which must be spent in succession. Strike is a single  action, but Double Tap is an activity in which you use both  the Aim and |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/22` | 0.539720 | You have to spend all the actions of an activity at once  to gain its effects. In an encounter, this means you must  complete it during your turn. If an activity gets interrupted or  disrupted in an e |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/0/ListItem/16` | 0.539257 | [three-actions] Three-Action Activity |

### Query 39
- Text: What is the rule about You can use only one single action, activity, or free action  that doesn't have a trigger at a time. You must complete  one before beginning another. For example, the Double  Tap activity states you must Aim and then make two  ranged Strikes, so you couldn't use an Interact action to  open a door in the middle of the Strikes.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/13', 'PZO22001 Starfinder Player Core 406-423::/page/0/Text/9', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/1']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/13', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/14', 'PZO22001 Starfinder Player Core 406-423::/page/1/SectionHeader/12']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 406-423::/page/1/Text/14` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/1/SectionHeader/12` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/13` | 1.000866 | You can use only one single action, activity, or free action  that doesn't have a trigger at a time. You must complete  one before beginning another. For example, the Double  Tap activity states you m |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/9` | 0.784199 | **Activities** usually take longer and require using multiple  actions, which must be spent in succession. Strike is a single  action, but Double Tap is an activity in which you use both  the Aim and |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/1` | 0.729566 | free actions limit when you can use those actions. You can use  only one action in response to a given trigger. For example, if  you had a reaction and a free action that both had a trigger  of "your |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/11` | 0.683385 | **Free actions** don't cost you any of your actions per turn,  nor do they cost your reaction. A free action with no trigger  follows the same rules as a single action (except the action  cost). It mu |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/27` | 0.682800 | You can use free actions that have triggers and reactions only  in response to certain events. Each such reaction and free  action lists the trigger that must happen for you to perform it.  When its t |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/8` | 0.658976 | You prepare to use an action that will occur outside your  turn. Choose a single action or free action you can use, and  designate a trigger. Your turn then ends. If the trigger you  designated occurs |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/2` | 0.652550 | This limitation of one action per trigger is per creature;  more than one creature can use a reaction or free action  in response to a given trigger. If multiple actions would be  occurring at the sam |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/14` | 0.649639 | Free actions with triggers and reactions work  differently. You can use these whenever the trigger  occurs, even if the trigger occurs in the middle of  another action. |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/17` | 0.625284 | Using an activity isn't the same as using any of  its subordinate actions. For example, the quickened  condition you get from the *haste* spell lets you spend  an extra action each turn to Stride or S |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/4` | 0.603148 | Sometimes you need to attempt something not already  covered by defined actions in the game. When this happens,  the rules tell you how many actions you need to spend as  well as any traits your actio |

### Query 40
- Text: What is the rule about Free actions with triggers and reactions work  differently. You can use these whenever the trigger  occurs, even if the trigger occurs in the middle of  another action.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/14']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/14', 'PZO22001 Starfinder Player Core 406-423::/page/0/Text/27', 'PZO22001 Starfinder Player Core 406-423::/page/0/Text/11']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/14', 'PZO22001 Starfinder Player Core 406-423::/page/1/SectionHeader/15', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/13']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 406-423::/page/1/SectionHeader/15` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/1/Text/13` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/14` | 0.989591 | Free actions with triggers and reactions work  differently. You can use these whenever the trigger  occurs, even if the trigger occurs in the middle of  another action. |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/27` | 0.845270 | You can use free actions that have triggers and reactions only  in response to certain events. Each such reaction and free  action lists the trigger that must happen for you to perform it.  When its t |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/11` | 0.819010 | **Free actions** don't cost you any of your actions per turn,  nor do they cost your reaction. A free action with no trigger  follows the same rules as a single action (except the action  cost). It mu |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/1` | 0.753944 | free actions limit when you can use those actions. You can use  only one action in response to a given trigger. For example, if  you had a reaction and a free action that both had a trigger  of "your |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/8` | 0.744181 | You prepare to use an action that will occur outside your  turn. Choose a single action or free action you can use, and  designate a trigger. Your turn then ends. If the trigger you  designated occurs |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/10` | 0.694129 | **Reactions** have triggers, which must be met for you to use  the reaction. You can use a reaction anytime its trigger is met,  whether it's your turn or not. Outside of encounters, your use  of reac |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/13` | 0.665073 | You can use only one single action, activity, or free action  that doesn't have a trigger at a time. You must complete  one before beginning another. For example, the Double  Tap activity states you m |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/8/Text/2` | 0.664597 | Some reactions and free actions are triggered by a  creature using an action with the move trait. The most  notable example is Reactive Strike (reproduced below).  Actions with the move trait can trig |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/2` | 0.660170 | This limitation of one action per trigger is per creature;  more than one creature can use a reaction or free action  in response to a given trigger. If multiple actions would be  occurring at the sam |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/28` | 0.634454 | There are only a few basic reactions and free actions that  all characters can use. You're more likely to gain actions with  triggers from your class, feats, and magic items. |

### Query 41
- Text: What is the rule about **Subordinate Actions**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/SectionHeader/15']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 406-423::/page/1/SectionHeader/15', 'PZO22001 Starfinder Player Core 406-423::/page/0/Text/21', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/16']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/SectionHeader/15', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/16', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/14']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 406-423::/page/1/Text/16` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/1/Text/14` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/1/SectionHeader/15` | 0.885827 | **Subordinate Actions** |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/21` | 0.659079 | An activity might cause you to use specific actions within  it. You don't have to spend additional actions to perform  them—they're already factored into the activity's required  actions. (See Subordi |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/16` | 0.628418 | An action might allow you to use a simpler action usually one of the Basic Actions on page 408—in a  different circumstance or with different effects. This  subordinate action still has its normal tra |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/1/SectionHeader/12` | 0.565052 | **Simultaneous Actions** |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/11` | 0.543166 | These rules clarify some of the specifics of using actions. |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/17` | 0.515759 | Using an activity isn't the same as using any of  its subordinate actions. For example, the quickened  condition you get from the *haste* spell lets you spend  an extra action each turn to Stride or S |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/11/Text/34` | 0.497669 | **Actions** |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/7/Text/42` | 0.497669 | **Actions** |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/36` | 0.497669 | **Actions** |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/9/Text/37` | 0.497669 | **Actions** |

### Query 42
- Text: What is the rule about An action might allow you to use a simpler action usually one of the Basic Actions on page 408—in a  different circumstance or with different effects. This  subordinate action still has its normal traits and effects,  but it's modified in any ways listed in the larger action.  For example, an activity that tells you to Stride up to  half your Speed alters the normal distance you can  move in a Stride. The Stride would still have the move  trait, would still trigger reactions that occur based on  movement, and so on. The subordinate action doesn't  gain any of the traits of the larger action unless specified.  The action that allows you to use a subordinate action  doesn't require you to spend more actions or reactions  to do so; that cost is already factored in.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/16']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/16', 'PZO22001 Starfinder Player Core 406-423::/page/0/Text/21', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/17']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/16', 'PZO22001 Starfinder Player Core 406-423::/page/1/SectionHeader/15', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/17']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 406-423::/page/1/SectionHeader/15` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/1/Text/17` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/16` | 1.010854 | An action might allow you to use a simpler action usually one of the Basic Actions on page 408—in a  different circumstance or with different effects. This  subordinate action still has its normal tra |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/21` | 0.723638 | An activity might cause you to use specific actions within  it. You don't have to spend additional actions to perform  them—they're already factored into the activity's required  actions. (See Subordi |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/17` | 0.723418 | Using an activity isn't the same as using any of  its subordinate actions. For example, the quickened  condition you get from the *haste* spell lets you spend  an extra action each turn to Stride or S |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/2/Text/2` | 0.680180 | Basic actions represent common tasks like moving around,  attacking, and helping others. As such, every creature can  use basic actions except in some extreme circumstances,  and many of those actions |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/11` | 0.619333 | These rules clarify some of the specifics of using actions. |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/6/Text/9` | 0.612595 | Switching from one movement type to another requires  ending your action that has the first movement type and  using a new action that has the second movement type. For  instance, if you Climbed 10 fe |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/4` | 0.606498 | Sometimes you need to attempt something not already  covered by defined actions in the game. When this happens,  the rules tell you how many actions you need to spend as  well as any traits your actio |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/1` | 0.599754 | free actions limit when you can use those actions. You can use  only one action in response to a given trigger. For example, if  you had a reaction and a free action that both had a trigger  of "your |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/27` | 0.589060 | You can use free actions that have triggers and reactions only  in response to certain events. Each such reaction and free  action lists the trigger that must happen for you to perform it.  When its t |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/6` | 0.588730 | Effects can change the number of actions you can use on  your turn, or whether you can use actions at all. The slowed  condition, for example, causes you to lose actions, while the  quickened conditio |

### Query 43
- Text: What is the rule about Using an activity isn't the same as using any of  its subordinate actions. For example, the quickened  condition you get from the *haste* spell lets you spend  an extra action each turn to Stride or Strike, but you  couldn't use the extra action for an activity that  includes a Stride or Strike. As another example, if you  used an action that specified, "If the next action you use  is a Strike," an activity that includes a Strike wouldn't  count because the next thing you're doing is starting an  activity, not using the Strike basic action.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/17']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/17', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/6', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/16']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/17', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/18', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/16']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 406-423::/page/1/Text/18` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/1/Text/16` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/17` | 1.018460 | Using an activity isn't the same as using any of  its subordinate actions. For example, the quickened  condition you get from the *haste* spell lets you spend  an extra action each turn to Stride or S |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/6` | 0.728034 | Effects can change the number of actions you can use on  your turn, or whether you can use actions at all. The slowed  condition, for example, causes you to lose actions, while the  quickened conditio |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/16` | 0.716536 | An action might allow you to use a simpler action usually one of the Basic Actions on page 408—in a  different circumstance or with different effects. This  subordinate action still has its normal tra |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/21` | 0.652036 | An activity might cause you to use specific actions within  it. You don't have to spend additional actions to perform  them—they're already factored into the activity's required  actions. (See Subordi |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/4` | 0.622828 | Sometimes you need to attempt something not already  covered by defined actions in the game. When this happens,  the rules tell you how many actions you need to spend as  well as any traits your actio |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/20` | 0.605723 | An activity typically involves using multiple actions to create  an effect greater than you can produce with a single action,  or combining multiple single actions to produce an effect  that's differe |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/2/Text/2` | 0.604591 | Basic actions represent common tasks like moving around,  attacking, and helping others. As such, every creature can  use basic actions except in some extreme circumstances,  and many of those actions |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/18` | 0.603581 | case of an activity, you usually lose all actions spent for the  activity up through the end of that turn. For instance, if you  began to Cast a Spell requiring 3 actions and the first action  was dis |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/1` | 0.594448 | free actions limit when you can use those actions. You can use  only one action in response to a given trigger. For example, if  you had a reaction and a free action that both had a trigger  of "your |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/13` | 0.586484 | You can use only one single action, activity, or free action  that doesn't have a trigger at a time. You must complete  one before beginning another. For example, the Double  Tap activity states you m |

### Query 44
- Text: What is the rule about case of an activity, you usually lose all actions spent for the  activity up through the end of that turn. For instance, if you  began to Cast a Spell requiring 3 actions and the first action  was disrupted, you lose all 3 actions that you committed to  that activity.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/18']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/18', 'PZO22001 Starfinder Player Core 406-423::/page/0/Text/22', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/6']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/18', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/17', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/19']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 406-423::/page/1/Text/17` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/1/Text/19` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/18` | 0.999776 | case of an activity, you usually lose all actions spent for the  activity up through the end of that turn. For instance, if you  began to Cast a Spell requiring 3 actions and the first action  was dis |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/22` | 0.778477 | You have to spend all the actions of an activity at once  to gain its effects. In an encounter, this means you must  complete it during your turn. If an activity gets interrupted or  disrupted in an e |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/6` | 0.679903 | Effects can change the number of actions you can use on  your turn, or whether you can use actions at all. The slowed  condition, for example, causes you to lose actions, while the  quickened conditio |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/17` | 0.606250 | Using an activity isn't the same as using any of  its subordinate actions. For example, the quickened  condition you get from the *haste* spell lets you spend  an extra action each turn to Stride or S |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/20` | 0.593787 | An activity typically involves using multiple actions to create  an effect greater than you can produce with a single action,  or combining multiple single actions to produce an effect  that's differe |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/25` | 0.590929 | If an activity outside of an encounter is interrupted or  disrupted, as described in Disrupting Actions on page 407,  you usually lose the time you put in, but no additional time. |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/6` | 0.579956 | You'll need to track your actions carefully in an encounter. At  the start of each turn you take in an encounter, you regain 3  actions and 1 reaction to spend that round. (Regaining your  actions is |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/9` | 0.573403 | Various abilities and conditions, such as a Reactive Strike,  can disrupt an action. When an action is disrupted, you still  use the actions or reactions you committed, and you still  expend any costs |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/43` | 0.558554 | If your Sustain action is disrupted, the ability ends. |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/4` | 0.558524 | Sometimes you need to attempt something not already  covered by defined actions in the game. When this happens,  the rules tell you how many actions you need to spend as  well as any traits your actio |

### Query 45
- Text: What is the rule about The GM decides what effects a disruption causes beyond  simply negating the effects that would've occurred from  the disrupted action. For instance, a Leap disrupted midway  wouldn't transport you back to the start of your jump, and a  disrupted item hand off might cause the item to fall to the  ground instead of staying in the hand of the creature who  was trying to give it away.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/19']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/19', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/9', 'PZO22001 Starfinder Player Core 406-423::/page/0/Text/25']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/19', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/18', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/21']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 406-423::/page/1/Text/18` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/1/Text/21` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/19` | 1.007282 | The GM decides what effects a disruption causes beyond  simply negating the effects that would've occurred from  the disrupted action. For instance, a Leap disrupted midway  wouldn't transport you bac |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/9` | 0.692201 | Various abilities and conditions, such as a Reactive Strike,  can disrupt an action. When an action is disrupted, you still  use the actions or reactions you committed, and you still  expend any costs |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/25` | 0.627600 | If an activity outside of an encounter is interrupted or  disrupted, as described in Disrupting Actions on page 407,  you usually lose the time you put in, but no additional time. |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/18` | 0.565830 | case of an activity, you usually lose all actions spent for the  activity up through the end of that turn. For instance, if you  began to Cast a Spell requiring 3 actions and the first action  was dis |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/22` | 0.554881 | You have to spend all the actions of an activity at once  to gain its effects. In an encounter, this means you must  complete it during your turn. If an activity gets interrupted or  disrupted in an e |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/2/Text/21` | 0.548645 | When you Delay, any persistent damage or other  negative effects that normally occur at the start or end of  your turn occur immediately when you use the Delay action.  Any beneficial effects that wou |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/8/Text/22` | 0.537810 | Usually the creature or effect forcing the movement  chooses the path the victim takes. If you're pushed or  pulled, you can usually be moved through hazardous  terrain, pushed out of an airlock, or t |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/7/Text/11` | 0.537725 | A dropped object takes damage just like a falling creature. If  the object lands on a creature, that creature can attempt a  Reflex save using the same rules as for a creature falling on a  creature. |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/8/Text/20` | 0.521003 | When an effect forces you to move, or if you start falling,  the distance you move is defined by the effect that moved  you, not by your Speed. Forced movement doesn't trigger  reactions that are trig |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/6` | 0.513839 | Effects can change the number of actions you can use on  your turn, or whether you can use actions at all. The slowed  condition, for example, causes you to lose actions, while the  quickened conditio |

### Query 46
- Text: Summarize **INTRODUCTION**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/21']
- Expected found: `True`
- Expected rank: `4`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 406-423::/page/11/Text/20', 'PZO22001 Starfinder Player Core 406-423::/page/13/Text/30', 'PZO22001 Starfinder Player Core 406-423::/page/5/Text/47']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/21', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/22', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/19']
- Expanded expected found: `True`
- Expanded expected rank: `4`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 406-423::/page/1/Text/22` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/1/Text/19` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/11/Text/20` | 0.880541 | **INTRODUCTION** |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/30` | 0.880541 | **INTRODUCTION** |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/47` | 0.880541 | **INTRODUCTION** |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/21` | 0.838541 | **INTRODUCTION** |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/34` | 0.838541 | **INTRODUCTION** |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/9/Text/23` | 0.838541 | **INTRODUCTION** |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/7/Text/27` | 0.838541 | **INTRODUCTION** |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/17/Text/24` | 0.672734 | INTRODUCTION |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/31` | 0.581679 | **BACKGROUNDS** |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/55` | 0.524467 | **INDEX** |

### Query 47
- Text: What is the rule about **ANCESTRIES & ** **BACKGROUNDS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/22']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/22', 'PZO22001 Starfinder Player Core 406-423::/page/3/Text/35', 'PZO22001 Starfinder Player Core 406-423::/page/9/Text/24']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/22', 'PZO22001 Starfinder Player Core 406-423::/page/3/Text/35', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/23', 'PZO22001 Starfinder Player Core 406-423::/page/5/Text/48', 'PZO22001 Starfinder Player Core 406-423::/page/9/Text/24', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/21', 'PZO22001 Starfinder Player Core 406-423::/page/13/Text/3', 'PZO22001 Starfinder Player Core 406-423::/page/7/Text/28', 'PZO22001 Starfinder Player Core 406-423::/page/11/Text/21']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 406-423::/page/3/Text/35` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/1/Text/23` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/5/Text/48` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/9/Text/24` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/1/Text/21` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/13/Text/3` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/7/Text/28` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/11/Text/21` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/22` | 0.920820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/35` | 0.920820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/9/Text/24` | 0.920820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/48` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/7/Text/28` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/11/Text/21` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/17/Text/25` | 0.822421 | ANCESTRIES & BACKGROUNDS |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/3` | 0.672250 | **ANCESTRIES & ** |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/31` | 0.594354 | **BACKGROUNDS** |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/7/Text/35` | 0.476883 | **Rules Overview** |

### Query 48
- Text: Summarize **CLASSES**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/23']
- Expected found: `True`
- Expected rank: `5`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 406-423::/page/11/Text/22', 'PZO22001 Starfinder Player Core 406-423::/page/9/Text/25', 'PZO22001 Starfinder Player Core 406-423::/page/3/Text/36']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/23', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/22', 'PZO22001 Starfinder Player Core 406-423::/page/13/Text/4', 'PZO22001 Starfinder Player Core 406-423::/page/11/Text/22', 'PZO22001 Starfinder Player Core 406-423::/page/5/Text/49', 'PZO22001 Starfinder Player Core 406-423::/page/9/Text/25', 'PZO22001 Starfinder Player Core 406-423::/page/7/Text/29', 'PZO22001 Starfinder Player Core 406-423::/page/3/Text/36', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/24']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 406-423::/page/1/Text/22` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/13/Text/4` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/11/Text/22` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/5/Text/49` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/9/Text/25` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/7/Text/29` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/3/Text/36` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/1/Text/24` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/11/Text/22` | 0.940061 | **CLASSES** |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/9/Text/25` | 0.940061 | **CLASSES** |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/36` | 0.940061 | **CLASSES** |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/49` | 0.910061 | **CLASSES** |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/23` | 0.910061 | **CLASSES** |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/7/Text/29` | 0.910061 | **CLASSES** |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/4` | 0.910061 | **CLASSES** |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/17/Text/26` | 0.763092 | CLASSES |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/55` | 0.463681 | **INDEX** |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/9/Text/26` | 0.437714 | **SKILLS** |

### Query 49
- Text: What is the rule about **SKILLS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/24']
- Expected found: `True`
- Expected rank: `5`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 406-423::/page/7/Text/30', 'PZO22001 Starfinder Player Core 406-423::/page/9/Text/26', 'PZO22001 Starfinder Player Core 406-423::/page/11/Text/23']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/24', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/23', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/25']
- Expanded expected found: `True`
- Expanded expected rank: `5`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 406-423::/page/1/Text/23` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/1/Text/25` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/7/Text/30` | 0.864442 | **SKILLS** |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/9/Text/26` | 0.864442 | **SKILLS** |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/11/Text/23` | 0.864442 | **SKILLS** |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/5` | 0.822442 | **SKILLS** |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/24` | 0.822442 | **SKILLS** |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/15/Text/16` | 0.822442 | **SKILLS** |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/50` | 0.822442 | **SKILLS** |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/37` | 0.822442 | **SKILLS** |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/17/Text/27` | 0.712079 | SKILLS |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/37` | 0.509909 | **Rules Overview** |

### Query 50
- Text: What is the rule about **FEATS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/25']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 406-423::/page/5/Text/51', 'PZO22001 Starfinder Player Core 406-423::/page/3/Text/38', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/25']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/25', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/26', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/24']
- Expanded expected found: `True`
- Expanded expected rank: `3`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 406-423::/page/1/Text/26` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/1/Text/24` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/51` | 0.871817 | **FEATS** |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/38` | 0.871817 | **FEATS** |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/25` | 0.871817 | **FEATS** |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/7/Text/31` | 0.829817 | **FEATS** |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/11/Text/24` | 0.829817 | **FEATS** |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/9/Text/27` | 0.829817 | **FEATS** |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/6` | 0.829817 | **FEATS** |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/15/Text/17` | 0.829817 | **FEATS** |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/17/Text/28` | 0.651337 | FEATS |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/11/Text/27` | 0.389330 | **Rules Overview** |

### Query 51
- Text: Summarize **EQUIPMENT**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/26']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/26', 'PZO22001 Starfinder Player Core 406-423::/page/7/Text/32', 'PZO22001 Starfinder Player Core 406-423::/page/13/Text/7']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/26', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/25', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/27']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 406-423::/page/1/Text/25` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/1/Text/27` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/26` | 0.944726 | **EQUIPMENT** |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/7/Text/32` | 0.944726 | **EQUIPMENT** |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/7` | 0.944726 | **EQUIPMENT** |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/17/Text/29` | 0.902387 | **EQUIPMENT ** |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/15/Text/18` | 0.578761 | **EQUIPMENT** **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/9/Text/28` | 0.578761 | **EQUIPMENT** **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/39` | 0.578761 | **EQUIPMENT** **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/11/Text/25` | 0.578761 | **EQUIPMENT** **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/52` | 0.578761 | **EQUIPMENT** **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/55` | 0.421643 | **INDEX** |

### Query 52
- Text: What is the rule about **SPELLS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/27']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 406-423::/page/7/Text/33', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/27', 'PZO22001 Starfinder Player Core 406-423::/page/13/Text/35']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/27', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/28', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/26']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 406-423::/page/1/Text/28` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/1/Text/26` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/7/Text/33` | 0.889304 | **SPELLS** |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/27` | 0.889304 | **SPELLS** |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/35` | 0.889304 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/17/Text/30` | 0.776591 | SPELLS |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/11/Text/25` | 0.759411 | **EQUIPMENT** **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/39` | 0.759411 | **EQUIPMENT** **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/15/Text/18` | 0.759411 | **EQUIPMENT** **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/9/Text/28` | 0.759411 | **EQUIPMENT** **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/52` | 0.759411 | **EQUIPMENT** **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/7/Text/35` | 0.414331 | **Rules Overview** |

### Query 53
- Text: Summarize **PLAYING THE ** **GAME**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/28']
- Expected found: `True`
- Expected rank: `4`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 406-423::/page/7/Text/34', 'PZO22001 Starfinder Player Core 406-423::/page/5/Text/53', 'PZO22001 Starfinder Player Core 406-423::/page/3/Text/40']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/28', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/29', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/27']
- Expanded expected found: `True`
- Expanded expected rank: `4`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 406-423::/page/1/Text/29` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/1/Text/27` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/53` | 0.965000 | **PLAYING THE ** **GAME** |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/7/Text/34` | 0.965000 | **PLAYING THE ** **GAME** |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/40` | 0.965000 | **PLAYING THE ** **GAME** |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/28` | 0.923000 | **PLAYING THE ** **GAME** |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/36` | 0.923000 | **PLAYING THE ** **GAME** |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/11/Text/26` | 0.923000 | **PLAYING THE ** **GAME** |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/9/Text/29` | 0.923000 | **PLAYING THE ** **GAME** |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/15/Text/19` | 0.811006 | **PLAYING THE ** |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/17/Text/31` | 0.749688 | PLAYING THE GAME |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/15/Text/41` | 0.663024 | **GAME** |

### Query 54
- Text: Summarize **Rules Overview**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/29']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/29', 'PZO22001 Starfinder Player Core 406-423::/page/3/Text/41', 'PZO22001 Starfinder Player Core 406-423::/page/9/Text/30']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/29', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/28', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/30']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 406-423::/page/1/Text/28` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/1/Text/30` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/29` | 0.894112 | **Rules Overview** |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/41` | 0.894112 | **Rules Overview** |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/9/Text/30` | 0.894112 | **Rules Overview** |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/7/Text/35` | 0.852112 | **Rules Overview** |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/54` | 0.852112 | **Rules Overview** |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/15/Text/20` | 0.852112 | **Rules Overview** |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/11/Text/27` | 0.852112 | **Rules Overview** |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/37` | 0.852112 | **Rules Overview** |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/17/Text/32` | 0.779340 | Rules Overview |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/1/SectionHeader/10` | 0.493204 | **IN-DEPTH ACTION RULES** |

### Query 55
- Text: What is the rule about **Checks**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/30']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 406-423::/page/9/Text/31', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/30', 'PZO22001 Starfinder Player Core 406-423::/page/7/Text/36']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/30', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/31', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/29']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 406-423::/page/1/Text/31` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/1/Text/29` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/9/Text/31` | 0.767288 | **Checks** |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/30` | 0.767288 | **Checks** |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/7/Text/36` | 0.767288 | **Checks** |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/11/Text/28` | 0.725288 | **Checks** |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/38` | 0.725288 | **Checks** |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/55` | 0.725288 | **Checks** |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/15/Text/21` | 0.725288 | **Checks** |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/42` | 0.725288 | **Checks** |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/17/Text/33` | 0.703313 | Checks |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/12/Text/5` | 0.478691 | Effects sometimes require checks, but not always. Casting  a *fly* spell on yourself creates an effect that allows you to  soar through the air, but casting the spell doesn't require a  check. Convers |

### Query 56
- Text: Summarize **Immunity, ** **Weakness, & ** **Resistance**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/32']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 406-423::/page/3/Text/44', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/32', 'PZO22001 Starfinder Player Core 406-423::/page/7/Text/38']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/32', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/33', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/31']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 406-423::/page/1/Text/33` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/1/Text/31` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/44` | 1.020504 | **Immunity, ** **Weakness, & ** **Resistance** |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/32` | 1.020504 | **Immunity, ** **Weakness, & ** **Resistance** |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/7/Text/38` | 1.020504 | **Immunity, ** **Weakness, & ** **Resistance** |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/57` | 0.978504 | **Immunity, ** **Weakness, & ** **Resistance** |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/11/Text/30` | 0.978504 | **Immunity, ** **Weakness, & ** **Resistance** |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/9/Text/33` | 0.978504 | **Immunity, ** **Weakness, & ** **Resistance** |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/15/Text/23` | 0.978504 | **Immunity, ** **Weakness, & ** **Resistance** |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/17/Text/35` | 0.918890 | Immunity, Weakness, & Resistance |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/13` | 0.881551 | **Immunity, ** **Weakness, & ** |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/40` | 0.637808 | **Resistance** |

### Query 57
- Text: Summarize **Hero Points**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/35']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 406-423::/page/3/Text/47', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/35', 'PZO22001 Starfinder Player Core 406-423::/page/5/Text/60']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/35', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/36', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/34']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 406-423::/page/1/Text/36` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/1/Text/34` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/47` | 0.970595 | **Hero Points** |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/35` | 0.970595 | **Hero Points** |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/60` | 0.970595 | **Hero Points** |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/9/Text/36` | 0.928595 | **Hero Points** |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/7/Text/41` | 0.928595 | **Hero Points** |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/15/Text/26` | 0.928595 | **Hero Points** |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/16` | 0.928595 | **Hero Points** |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/11/Text/33` | 0.928595 | **Hero Points** |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/17/Text/38` | 0.806477 | Hero Points |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/15` | 0.506598 | **Hit Points, ** **Healing, and ** |

### Query 58
- Text: Summarize **Movement**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/37']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 406-423::/page/3/Text/49', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/37', 'PZO22001 Starfinder Player Core 406-423::/page/9/Text/38']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/37', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/36', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/38']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 406-423::/page/1/Text/36` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/1/Text/38` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/49` | 0.929132 | **Movement** |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/37` | 0.929132 | **Movement** |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/9/Text/38` | 0.929132 | **Movement** |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/7/Text/43` | 0.887132 | **Movement** |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/62` | 0.887132 | **Movement** |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/15/Text/28` | 0.887132 | **Movement** |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/11/Text/35` | 0.887132 | **Movement** |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/45` | 0.887132 | **Movement** |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/8/SectionHeader/1` | 0.620839 | **REACTIONS TO MOVEMENT** |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/6/SectionHeader/1` | 0.614658 | MOVEMENT |

### Query 59
- Text: Summarize **Effects** **Area**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/38']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/38', 'PZO22001 Starfinder Player Core 406-423::/page/3/Text/50', 'PZO22001 Starfinder Player Core 406-423::/page/17/Text/41']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/38', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/37', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/39']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 406-423::/page/1/Text/37` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/1/Text/39` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/38` | 0.987469 | **Effects** **Area** |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/50` | 0.987469 | **Effects** **Area** |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/17/Text/41` | 0.814158 | Effects Area |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/7/Text/44` | 0.746103 | **Effects** |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/63` | 0.746103 | **Effects** |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/9/Text/39` | 0.746103 | **Effects** |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/11/Text/36` | 0.746103 | **Effects** |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/15/Text/29` | 0.746103 | **Effects** |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/18` | 0.746103 | **Effects** |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/12/SectionHeader/1` | 0.684706 | EFFECTS |

### Query 60
- Text: Summarize **Afflictions**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/39']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 406-423::/page/3/Text/51', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/39', 'PZO22001 Starfinder Player Core 406-423::/page/13/Text/48']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/39', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/40', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/38']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 406-423::/page/1/Text/40` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/1/Text/38` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/51` | 0.968407 | **Afflictions** |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/39` | 0.968407 | **Afflictions** |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/48` | 0.968407 | **Afflictions** |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/15/Text/31` | 0.926407 | **Afflictions** |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/11/Text/37` | 0.844597 | **Area** **Afflictions** |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/64` | 0.844597 | **Area** **Afflictions** |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/7/Text/46` | 0.743603 | **Afflictions** **Counteracting** |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/9/Text/41` | 0.743603 | **Afflictions** **Counteracting** |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/16/Text/5` | 0.585084 | Whether appearing in a spell, as an item, or within a creature's  stat block, afflictions appear in the following format. |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/16/Text/2` | 0.497975 | Diseases and poisons are types of afflictions, as are curses and radiation. An affliction can infect a  creature for a long time, progressing through different and often increasingly debilitating stag |

### Query 61
- Text: Summarize **Perception and ** **Detection**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/41']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 406-423::/page/5/Text/66', 'PZO22001 Starfinder Player Core 406-423::/page/3/Text/53', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/41']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/41', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/40', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/42']
- Expanded expected found: `True`
- Expanded expected rank: `3`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 406-423::/page/1/Text/40` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/1/Text/42` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/66` | 0.992556 | **Perception and ** **Detection** |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/53` | 0.992556 | **Perception and ** **Detection** |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/41` | 0.992556 | **Perception and ** **Detection** |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/15/Text/33` | 0.950556 | **Perception and ** **Detection** |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/9/Text/42` | 0.818773 | **Perception and ** |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/7/Text/47` | 0.818773 | **Perception and ** |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/50` | 0.818773 | **Perception and ** |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/11/Text/39` | 0.818773 | **Perception and ** |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/23` | 0.733480 | **Detection** |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/17/Text/44` | 0.720729 | Perception and |

### Query 62
- Text: Summarize **Encounter ** **Mode**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/42']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/42', 'PZO22001 Starfinder Player Core 406-423::/page/3/Text/54', 'PZO22001 Starfinder Player Core 406-423::/page/5/Text/67']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/42', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/43', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/41']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 406-423::/page/1/Text/43` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/1/Text/41` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/42` | 0.996085 | **Encounter ** **Mode** |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/54` | 0.996085 | **Encounter ** **Mode** |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/67` | 0.996085 | **Encounter ** **Mode** |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/15/Text/34` | 0.954085 | **Encounter ** **Mode** |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/7/Text/48` | 0.877882 | **Detection** **Encounter ** **Mode** |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/9/Text/43` | 0.877882 | **Detection** **Encounter ** **Mode** |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/24` | 0.792479 | **Encounter ** |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/11/Text/40` | 0.732350 | **Detection** **Encounter ** |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/68` | 0.650901 | **Exploration ** **Mode** |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/43` | 0.650901 | **Exploration ** **Mode** |

### Query 63
- Text: Summarize **Exploration ** **Mode**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/43']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/43', 'PZO22001 Starfinder Player Core 406-423::/page/3/Text/55', 'PZO22001 Starfinder Player Core 406-423::/page/5/Text/68']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/43', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/44', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/42']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 406-423::/page/1/Text/44` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/1/Text/42` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/43` | 0.983318 | **Exploration ** **Mode** |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/55` | 0.983318 | **Exploration ** **Mode** |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/68` | 0.983318 | **Exploration ** **Mode** |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/15/Text/35` | 0.941318 | **Exploration ** **Mode** |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/7/Text/49` | 0.941318 | **Exploration ** **Mode** |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/9/Text/44` | 0.941318 | **Exploration ** **Mode** |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/11/Text/41` | 0.753024 | **Exploration ** |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/25` | 0.753024 | **Exploration ** |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/17/Text/47` | 0.691057 | Exploration Mode |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/52` | 0.624681 | **Mode** |

### Query 64
- Text: Summarize **Downtime ** **Mode**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/44']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/44', 'PZO22001 Starfinder Player Core 406-423::/page/3/Text/56', 'PZO22001 Starfinder Player Core 406-423::/page/5/Text/69']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/44', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/45', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/43']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 406-423::/page/1/Text/45` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/1/Text/43` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/44` | 0.972659 | **Downtime ** **Mode** |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/56` | 0.972659 | **Downtime ** **Mode** |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/69` | 0.972659 | **Downtime ** **Mode** |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/9/Text/45` | 0.930659 | **Downtime ** **Mode** |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/7/Text/50` | 0.930659 | **Downtime ** **Mode** |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/15/Text/36` | 0.930659 | **Downtime ** **Mode** |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/11/Text/42` | 0.929443 | **Mode** **Downtime ** |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/26` | 0.793123 | **Downtime ** |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/17/Text/48` | 0.669744 | Downtime Mode |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/53` | 0.567110 | **Mode** |

### Query 65
- Text: Summarize **CONDITIONS ** **APPENDIX**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/45']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/45', 'PZO22001 Starfinder Player Core 406-423::/page/5/Text/70', 'PZO22001 Starfinder Player Core 406-423::/page/3/Text/57']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/45', 'PZO22001 Starfinder Player Core 406-423::/page/13/SectionHeader/57', 'PZO22001 Starfinder Player Core 406-423::/page/13/Text/27', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/46', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/44', 'PZO22001 Starfinder Player Core 406-423::/page/7/Text/51', 'PZO22001 Starfinder Player Core 406-423::/page/5/Text/70', 'PZO22001 Starfinder Player Core 406-423::/page/9/Text/46', 'PZO22001 Starfinder Player Core 406-423::/page/3/Text/57', 'PZO22001 Starfinder Player Core 406-423::/page/15/Text/37']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 406-423::/page/13/SectionHeader/57` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/13/Text/27` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/1/Text/46` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/1/Text/44` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/7/Text/51` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/5/Text/70` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/9/Text/46` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/3/Text/57` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/15/Text/37` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/45` | 0.983499 | **CONDITIONS ** **APPENDIX** |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/70` | 0.983499 | **CONDITIONS ** **APPENDIX** |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/57` | 0.983499 | **CONDITIONS ** **APPENDIX** |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/9/Text/46` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/7/Text/51` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/15/Text/37` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/17/Text/49` | 0.837763 | CONDITIONS APPENDIX |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/54` | 0.769880 | **APPENDIX** |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/11/Text/44` | 0.769880 | **APPENDIX** |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/27` | 0.645203 | **CONDITIONS ** |

### Query 66
- Text: Summarize **GLOSSARY & ** **INDEX**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/46']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 406-423::/page/7/Text/52', 'PZO22001 Starfinder Player Core 406-423::/page/15/Text/38', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/46']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/46', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/45', 'PZO22001 Starfinder Player Core 406-423::/page/2/SectionHeader/1']
- Expanded expected found: `True`
- Expanded expected rank: `3`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 406-423::/page/1/Text/45` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/2/SectionHeader/1` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/7/Text/52` | 0.993465 | **GLOSSARY & ** **INDEX** |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/15/Text/38` | 0.993465 | **GLOSSARY & ** **INDEX** |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/46` | 0.993465 | **GLOSSARY & ** **INDEX** |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/71` | 0.951465 | **GLOSSARY & ** **INDEX** |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/9/Text/47` | 0.951465 | **GLOSSARY & ** **INDEX** |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/58` | 0.951465 | **GLOSSARY & ** **INDEX** |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/11/Text/45` | 0.951465 | **GLOSSARY & ** **INDEX** |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/17/Text/50` | 0.825490 | GLOSSARY & INDEX |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/28` | 0.804819 | **GLOSSARY & ** |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/55` | 0.618357 | **INDEX** |

### Query 67
- Text: Summarize **MOVE**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/2/SectionHeader/16']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 406-423::/page/4/Text/12', 'PZO22001 Starfinder Player Core 406-423::/page/2/Text/23', 'PZO22001 Starfinder Player Core 406-423::/page/2/SectionHeader/16']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/2/SectionHeader/16', 'PZO22001 Starfinder Player Core 406-423::/page/2/SectionHeader/15', 'PZO22001 Starfinder Player Core 406-423::/page/2/Text/17']
- Expanded expected found: `True`
- Expanded expected rank: `3`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 406-423::/page/2/SectionHeader/15` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/2/Text/17` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/4/Text/12` | 0.926118 | **MOVE** |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/2/Text/23` | 0.926118 | **MOVE** |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/2/SectionHeader/16` | 0.926118 | **MOVE** |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/3/SectionHeader/2` | 0.884118 | **MOVE** |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/4/Text/4` | 0.884118 | **MOVE** |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/4/Text/7` | 0.884118 | **MOVE** |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/5/SectionHeader/4` | 0.884118 | **MOVE** |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/5/SectionHeader/11` | 0.884118 | **MOVE** |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/5/SectionHeader/23` | 0.884118 | **MOVE** |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/5/SectionHeader/32` | 0.884118 | **MOVE** |

### Query 68
- Text: Summarize **Requirements** You're prone, and your Speed is at least 10 feet. You move 5 feet by crawling and continue to stay prone.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/2/Text/17']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 406-423::/page/2/Text/17', 'PZO22001 Starfinder Player Core 406-423::/page/4/Text/8', 'PZO22001 Starfinder Player Core 406-423::/page/8/Text/13']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/2/Text/17', 'PZO22001 Starfinder Player Core 406-423::/page/2/SectionHeader/16', 'PZO22001 Starfinder Player Core 406-423::/page/2/SectionHeader/18']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 406-423::/page/2/SectionHeader/16` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/2/SectionHeader/18` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/2/Text/17` | 1.041839 | **Requirements** You're prone, and your Speed is at least 10 feet. You move 5 feet by crawling and continue to stay prone. |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/4/Text/8` | 0.744188 | **Requirements** Your Speed is at least 10 feet. |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/8/Text/13` | 0.624188 | size or smaller. The GM might allow you to climb atop the  corpse or unconscious body of a larger creature in some  situations. A prone creature can't stand up while someone  else occupies its space, |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/13` | 0.576301 | You move through the air up to your fly Speed. Moving upward  (straight up or diagonally) uses the rules for moving through  difficult terrain. You can move straight down 10 feet for every  5 feet of |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/6/Text/8` | 0.568213 | There are other ways to move, such as through the air  or underground. Each of these special movement types has  its own Speed value. Many creatures have these Speeds  naturally, such as a barathu hav |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/12` | 0.564497 | **Requirements** You have a fly Speed. |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/4/Text/32` | 0.564497 | **Requirements** You have a fly Speed. |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/3/ListItem/4` | 0.554784 | **Horizontal Jump **up to 10 feet horizontally if your  Speed is at least 15 feet, or up to 15 feet horizontally  if your Speed is at least 30 feet. You land in the space  where your Leap ends (meanin |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/6/Text/25` | 0.552161 | With a swim Speed, you can propel yourself through liquids  with little impediment. Instead of attempting Athletics  checks to Swim, you automatically succeed and move up to  your swim Speed instead o |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/6/Text/17` | 0.550695 | A climb Speed allows you to move up or down inclines  and vertical surfaces. Most creatures need to succeed at  Athletics checks to Climb, but if you have a climb Speed,  you automatically succeed and |

### Query 69
- Text: Summarize **Trigger** Your turn begins.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/2/SectionHeader/19']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 406-423::/page/2/SectionHeader/19', 'PZO22001 Starfinder Player Core 406-423::/page/4/Text/31', 'PZO22001 Starfinder Player Core 406-423::/page/5/Text/16']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/2/SectionHeader/19', 'PZO22001 Starfinder Player Core 406-423::/page/2/Text/20', 'PZO22001 Starfinder Player Core 406-423::/page/2/SectionHeader/18']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 406-423::/page/2/Text/20` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/2/SectionHeader/18` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/2/SectionHeader/19` | 1.010188 | **Trigger** Your turn begins. |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/4/Text/31` | 0.754709 | **Trigger** You fall. |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/16` | 0.685049 | **Trigger** You fall from or past an edge or handhold. |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/2/Text/8` | 0.604976 | **Trigger** An ally is about to use an action that requires a skill  check or attack roll. |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/8/Text/5` | 0.604434 | **Trigger** A creature within your reach uses a manipulate  action or a move action, makes a ranged attack, or  leaves a square during a move action it's using. |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/8` | 0.564464 | You prepare to use an action that will occur outside your  turn. Choose a single action or free action you can use, and  designate a trigger. Your turn then ends. If the trigger you  designated occurs |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/0/SectionHeader/26` | 0.543529 | ACTIONS WITH TRIGGERS |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/1` | 0.530611 | free actions limit when you can use those actions. You can use  only one action in response to a given trigger. For example, if  you had a reaction and a free action that both had a trigger  of "your |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/10` | 0.502047 | **Reactions** have triggers, which must be met for you to use  the reaction. You can use a reaction anytime its trigger is met,  whether it's your turn or not. Outside of encounters, your use  of reac |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/14` | 0.501172 | Free actions with triggers and reactions work  differently. You can use these whenever the trigger  occurs, even if the trigger occurs in the middle of  another action. |

### Query 70
- Text: Summarize **MOVE**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/2/Text/23']
- Expected found: `True`
- Expected rank: `9`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 406-423::/page/4/Text/12', 'PZO22001 Starfinder Player Core 406-423::/page/2/SectionHeader/16', 'PZO22001 Starfinder Player Core 406-423::/page/4/Text/4']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/2/Text/23', 'PZO22001 Starfinder Player Core 406-423::/page/2/Text/24', 'PZO22001 Starfinder Player Core 406-423::/page/2/SectionHeader/22']
- Expanded expected found: `True`
- Expanded expected rank: `9`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 406-423::/page/2/Text/24` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/2/SectionHeader/22` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/4/Text/12` | 0.926118 | **MOVE** |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/2/SectionHeader/16` | 0.926118 | **MOVE** |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/4/Text/4` | 0.926118 | **MOVE** |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/4/Text/7` | 0.884118 | **MOVE** |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/5/SectionHeader/4` | 0.884118 | **MOVE** |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/5/SectionHeader/11` | 0.884118 | **MOVE** |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/5/SectionHeader/32` | 0.884118 | **MOVE** |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/5/SectionHeader/23` | 0.884118 | **MOVE** |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/2/Text/23` | 0.884118 | **MOVE** |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/3/SectionHeader/2` | 0.884118 | **MOVE** |

### Query 71
- Text: Summarize You fall prone.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/2/Text/24']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 406-423::/page/2/Text/24', 'PZO22001 Starfinder Player Core 406-423::/page/4/Text/5', 'PZO22001 Starfinder Player Core 406-423::/page/13/Text/96']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/2/Text/24', 'PZO22001 Starfinder Player Core 406-423::/page/2/SectionHeader/25', 'PZO22001 Starfinder Player Core 406-423::/page/2/Text/23']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 406-423::/page/2/SectionHeader/25` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/2/Text/23` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/2/Text/24` | 0.992561 | You fall prone. |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/4/Text/5` | 0.777679 | You stand up from being prone. |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/96` | 0.664518 | **Prone:** You're lying on the ground and easier to attack. |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/4/Text/31` | 0.582486 | **Trigger** You fall. |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/2/Text/17` | 0.521469 | **Requirements** You're prone, and your Speed is at least 10 feet. You move 5 feet by crawling and continue to stay prone. |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/7/Text/2` | 0.511167 | If you fall more than 5 feet, when you land you take  bludgeoning damage equal to half the distance you fell. Treat  falls longer than 1,500 feet as though they were 1,500 feet  (750 damage). If you t |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/16` | 0.499999 | **Trigger** You fall from or past an edge or handhold. |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/8/Text/13` | 0.470672 | size or smaller. The GM might allow you to climb atop the  corpse or unconscious body of a larger creature in some  situations. A prone creature can't stand up while someone  else occupies its space, |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/4/Text/22` | 0.464925 | **Requirements** You are benefiting from cover, are near a  feature that allows you to take cover, or are prone. |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/8/Text/12` | 0.459998 | You can share a space with a prone creature if that  creature is willing, unconscious, or dead and if it's your |

### Query 72
- Text: Summarize **Critical Success** You get free and remove the grabbed,  immobilized, and restrained conditions imposed by your  chosen target. You can then Stride up to 5 feet.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/2/Text/28']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 406-423::/page/2/Text/28', 'PZO22001 Starfinder Player Core 406-423::/page/2/Text/29', 'PZO22001 Starfinder Player Core 406-423::/page/5/Text/19']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/2/Text/28', 'PZO22001 Starfinder Player Core 406-423::/page/2/Text/27', 'PZO22001 Starfinder Player Core 406-423::/page/2/Text/29']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 406-423::/page/2/Text/27` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/2/Text/29` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/2/Text/28` | 1.044354 | **Critical Success** You get free and remove the grabbed,  immobilized, and restrained conditions imposed by your  chosen target. You can then Stride up to 5 feet. |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/2/Text/29` | 0.813674 | **Success** You get free and remove the grabbed, immobilized,  and restrained conditions imposed by your chosen  target. |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/19` | 0.640392 | **Critical Success** You grab the edge or handhold, whether or  not you have a hand free, typically by using a suitable held  item to catch yourself (catching a doshko on a ledge, for  example). You s |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/7/Text/13` | 0.580161 | Your movement during encounter mode—and at other times  where precise movement matters—depends on the actions  and other abilities you use. Whether you Stride, Step, Swim,  or Climb, the maximum dista |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/20` | 0.567212 | **Success** If you have at least one hand free, you grab the edge  or handhold, stopping your fall. You still take damage from  the distance fallen so far, but you treat the fall as though  it were 20 |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/6/Text/12` | 0.544000 | When you use the Stride action, you move a number of  feet equal to your Speed. Whenever a rule mentions your  Speed without specifying a type, it's referring to your  land Speed. |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/2/Text/27` | 0.536635 | You attempt to escape from being grabbed, immobilized, or  restrained. Choose one creature, object, spell effect, hazard,  or other impediment imposing any of those conditions on  you. Attempt a check |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/9/Text/2` | 0.534176 | Iseph decides to Stride. They have a  Speed of 25 feet. Iseph moves straight  south, spending 10 feet of their Speed,  then diagonally, spending another 5 feet.  Iseph's next diagonal move, because it |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/6/Text/9` | 0.532501 | Switching from one movement type to another requires  ending your action that has the first movement type and  using a new action that has the second movement type. For  instance, if you Climbed 10 fe |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/2/Text/17` | 0.524743 | **Requirements** You're prone, and your Speed is at least 10 feet. You move 5 feet by crawling and continue to stay prone. |

### Query 73
- Text: Summarize **Success** You get free and remove the grabbed, immobilized,  and restrained conditions imposed by your chosen  target.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/2/Text/29']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 406-423::/page/2/Text/29', 'PZO22001 Starfinder Player Core 406-423::/page/2/Text/28', 'PZO22001 Starfinder Player Core 406-423::/page/2/Text/27']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/2/Text/29', 'PZO22001 Starfinder Player Core 406-423::/page/2/Text/30', 'PZO22001 Starfinder Player Core 406-423::/page/2/Text/28']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 406-423::/page/2/Text/30` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/2/Text/28` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/2/Text/29` | 1.030825 | **Success** You get free and remove the grabbed, immobilized,  and restrained conditions imposed by your chosen  target. |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/2/Text/28` | 0.810813 | **Critical Success** You get free and remove the grabbed,  immobilized, and restrained conditions imposed by your  chosen target. You can then Stride up to 5 feet. |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/2/Text/27` | 0.596019 | You attempt to escape from being grabbed, immobilized, or  restrained. Choose one creature, object, spell effect, hazard,  or other impediment imposing any of those conditions on  you. Attempt a check |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/27` | 0.544486 | You can use free actions that have triggers and reactions only  in response to certain events. Each such reaction and free  action lists the trigger that must happen for you to perform it.  When its t |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/98` | 0.538243 | **Restrained:** You're tied up and can't move, or a grappling |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/14` | 0.538192 | Free actions with triggers and reactions work  differently. You can use these whenever the trigger  occurs, even if the trigger occurs in the middle of  another action. |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/19` | 0.528581 | **Critical Success** You grab the edge or handhold, whether or  not you have a hand free, typically by using a suitable held  item to catch yourself (catching a doshko on a ledge, for  example). You s |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/8` | 0.528360 | You prepare to use an action that will occur outside your  turn. Choose a single action or free action you can use, and  designate a trigger. Your turn then ends. If the trigger you  designated occurs |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/11` | 0.525178 | **Free actions** don't cost you any of your actions per turn,  nor do they cost your reaction. A free action with no trigger  follows the same rules as a single action (except the action  cost). It mu |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/20` | 0.522213 | **Success** If you have at least one hand free, you grab the edge  or handhold, stopping your fall. You still take damage from  the distance fallen so far, but you treat the fall as though  it were 20 |

### Query 74
- Text: Summarize **Critical Failure** You don't get free, and you can't attempt to  Escape again until your next turn.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/2/Text/30']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 406-423::/page/2/Text/30', 'PZO22001 Starfinder Player Core 406-423::/page/3/Text/32', 'PZO22001 Starfinder Player Core 406-423::/page/7/Text/9']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/2/Text/30', 'PZO22001 Starfinder Player Core 406-423::/page/2/SectionHeader/31', 'PZO22001 Starfinder Player Core 406-423::/page/2/Text/29']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 406-423::/page/2/SectionHeader/31` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/2/Text/29` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/2/Text/30` | 1.035791 | **Critical Failure** You don't get free, and you can't attempt to  Escape again until your next turn. |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/32` | 0.673364 | **Critical Failure** You get a false sense of the creature's  intentions. |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/7/Text/9` | 0.594020 | **Critical Failure** The creature takes the same amount of  bludgeoning damage you took from the fall. |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/17/Text/19` | 0.540875 | Critical Failure You fail to counteract the target. |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/24` | 0.539283 | **Critical Success** Any undetected or hidden creature you  critically succeeded against becomes observed by you.  You learn the location of objects in the area you critically  succeeded against. |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/16/Text/11` | 0.531611 | If you fail the initial saving throw, you advance to stage 1 of  the affliction and are subjected to the listed effect. On a critical  failure, after its onset period (if applicable), you advance to |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/31` | 0.529980 | **Failure** You detect what a deceptive creature wants you to  believe. If they're not being deceptive, you believe they're  behaving normally. |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/21` | 0.526660 | **Critical Failure** You continue to fall, and if you've fallen 20 feet  or more before you use this reaction, you take 10 bludgeoning  damage from the impact for every 20 feet fallen. |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/22` | 0.507910 | You have to spend all the actions of an activity at once  to gain its effects. In an encounter, this means you must  complete it during your turn. If an activity gets interrupted or  disrupted in an e |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/29` | 0.503574 | **Critical Success** You determine the creature's true intentions  and get a solid idea of any mental magic affecting it. |

### Query 75
- Text: Summarize **MANIPULATE**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/2/SectionHeader/32']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 406-423::/page/3/SectionHeader/11', 'PZO22001 Starfinder Player Core 406-423::/page/2/SectionHeader/32', 'PZO22001 Starfinder Player Core 406-423::/page/5/SectionHeader/15']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/2/SectionHeader/32', 'PZO22001 Starfinder Player Core 406-423::/page/2/Text/33', 'PZO22001 Starfinder Player Core 406-423::/page/2/SectionHeader/31']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 406-423::/page/2/Text/33` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/2/SectionHeader/31` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/3/SectionHeader/11` | 0.964151 | **MANIPULATE** |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/2/SectionHeader/32` | 0.964151 | **MANIPULATE** |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/5/SectionHeader/15` | 0.964151 | **MANIPULATE** |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/5/SectionHeader/28` | 0.639815 | **AUDITORY** **MANIPULATE** **VISUAL** |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/87` | 0.444731 | **Immobilized:** You can't move. |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/2/Text/29` | 0.435819 | **Success** You get free and remove the grabbed, immobilized,  and restrained conditions imposed by your chosen  target. |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/5/SectionHeader/40` | 0.424160 | **CONCENTRATE** |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/5/SectionHeader/8` | 0.424160 | **CONCENTRATE** |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/3/SectionHeader/7` | 0.424160 | **CONCENTRATE** |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/45` | 0.415645 | **Movement** |

### Query 76
- Text: Summarize **MOVE**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/3/SectionHeader/2']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 406-423::/page/4/Text/12', 'PZO22001 Starfinder Player Core 406-423::/page/3/SectionHeader/2', 'PZO22001 Starfinder Player Core 406-423::/page/2/SectionHeader/16']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/3/SectionHeader/2', 'PZO22001 Starfinder Player Core 406-423::/page/2/Text/33', 'PZO22001 Starfinder Player Core 406-423::/page/3/Text/3']
- Expanded expected found: `True`
- Expanded expected rank: `3`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 406-423::/page/2/Text/33` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/3/Text/3` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/2/SectionHeader/16` | 0.926118 | **MOVE** |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/4/Text/12` | 0.926118 | **MOVE** |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/3/SectionHeader/2` | 0.926118 | **MOVE** |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/2/Text/23` | 0.884118 | **MOVE** |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/5/SectionHeader/32` | 0.884118 | **MOVE** |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/5/SectionHeader/11` | 0.884118 | **MOVE** |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/5/SectionHeader/4` | 0.884118 | **MOVE** |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/5/SectionHeader/23` | 0.884118 | **MOVE** |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/4/Text/4` | 0.884118 | **MOVE** |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/4/Text/7` | 0.884118 | **MOVE** |

### Query 77
- Text: Summarize **CONCENTRATE**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/3/SectionHeader/7']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 406-423::/page/5/SectionHeader/8', 'PZO22001 Starfinder Player Core 406-423::/page/3/SectionHeader/7', 'PZO22001 Starfinder Player Core 406-423::/page/5/SectionHeader/40']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/3/SectionHeader/7', 'PZO22001 Starfinder Player Core 406-423::/page/3/SectionHeader/6', 'PZO22001 Starfinder Player Core 406-423::/page/3/Text/8']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 406-423::/page/3/SectionHeader/6` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/3/Text/8` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/5/SectionHeader/8` | 0.979465 | **CONCENTRATE** |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/3/SectionHeader/7` | 0.979465 | **CONCENTRATE** |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/5/SectionHeader/40` | 0.979465 | **CONCENTRATE** |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/3/SectionHeader/27` | 0.775500 | **CONCENTRATE** **SECRET** |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/3/SectionHeader/15` | 0.775500 | **CONCENTRATE** **SECRET** |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/72` | 0.428903 | **Fascinated:** You're compelled to focus your attention on  something. |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/5/SectionHeader/22` | 0.422183 | **MOUNT **[one-action] |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/52` | 0.420562 | **Counteracting** |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/11/Text/38` | 0.420562 | **Counteracting** |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/40` | 0.420562 | **Counteracting** |

### Query 78
- Text: Summarize **MANIPULATE**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/3/SectionHeader/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 406-423::/page/3/SectionHeader/11', 'PZO22001 Starfinder Player Core 406-423::/page/2/SectionHeader/32', 'PZO22001 Starfinder Player Core 406-423::/page/5/SectionHeader/15']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/3/SectionHeader/11', 'PZO22001 Starfinder Player Core 406-423::/page/3/SectionHeader/10', 'PZO22001 Starfinder Player Core 406-423::/page/3/Text/12']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 406-423::/page/3/SectionHeader/10` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/3/Text/12` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/3/SectionHeader/11` | 0.964151 | **MANIPULATE** |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/2/SectionHeader/32` | 0.964151 | **MANIPULATE** |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/5/SectionHeader/15` | 0.964151 | **MANIPULATE** |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/5/SectionHeader/28` | 0.639815 | **AUDITORY** **MANIPULATE** **VISUAL** |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/87` | 0.444731 | **Immobilized:** You can't move. |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/2/Text/29` | 0.435819 | **Success** You get free and remove the grabbed, immobilized,  and restrained conditions imposed by your chosen  target. |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/5/SectionHeader/40` | 0.424160 | **CONCENTRATE** |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/5/SectionHeader/8` | 0.424160 | **CONCENTRATE** |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/3/SectionHeader/7` | 0.424160 | **CONCENTRATE** |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/45` | 0.415645 | **Movement** |

### Query 79
- Text: Summarize **CONCENTRATE** **SECRET**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/3/SectionHeader/15']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 406-423::/page/3/SectionHeader/15', 'PZO22001 Starfinder Player Core 406-423::/page/3/SectionHeader/27', 'PZO22001 Starfinder Player Core 406-423::/page/3/SectionHeader/7']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/3/SectionHeader/15', 'PZO22001 Starfinder Player Core 406-423::/page/3/Text/16', 'PZO22001 Starfinder Player Core 406-423::/page/3/SectionHeader/14']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 406-423::/page/3/Text/16` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/3/SectionHeader/14` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/3/SectionHeader/15` | 0.994343 | **CONCENTRATE** **SECRET** |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/3/SectionHeader/27` | 0.994343 | **CONCENTRATE** **SECRET** |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/3/SectionHeader/7` | 0.841199 | **CONCENTRATE** |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/5/SectionHeader/40` | 0.799199 | **CONCENTRATE** |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/5/SectionHeader/8` | 0.799199 | **CONCENTRATE** |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/5/SectionHeader/22` | 0.407037 | **MOUNT **[one-action] |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/1/SectionHeader/15` | 0.406908 | **Subordinate Actions** |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/40` | 0.390841 | **Counteracting** |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/15/Text/32` | 0.390841 | **Counteracting** |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/49` | 0.390841 | **Counteracting** |

### Query 80
- Text: Summarize **AID DETAILS**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/3/SectionHeader/18']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 406-423::/page/3/SectionHeader/18', 'PZO22001 Starfinder Player Core 406-423::/page/2/SectionHeader/7', 'PZO22001 Starfinder Player Core 406-423::/page/2/Text/9']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/3/SectionHeader/18', 'PZO22001 Starfinder Player Core 406-423::/page/3/Text/19', 'PZO22001 Starfinder Player Core 406-423::/page/3/Text/17']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 406-423::/page/3/Text/19` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/3/Text/17` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/3/SectionHeader/18` | 0.917339 | **AID DETAILS** |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/2/SectionHeader/7` | 0.632031 | **AID **[reaction] |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/2/Text/9` | 0.540654 | **Requirements** The ally is willing to accept your aid, and you've  prepared to help (see below). |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/31` | 0.470751 | **BACKGROUNDS** |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/19` | 0.461958 | The following clarifications might be relevant when  Aiding an ally. |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/55` | 0.459564 | **INDEX** |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/2/Text/11` | 0.451494 | When you use your Aid reaction, attempt a skill check or  attack roll of a type decided by the GM. The typical DC is 15,  but the GM might adjust this DC for particularly hard or easy  tasks. The GM c |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/30` | 0.430307 | **INTRODUCTION** |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/21` | 0.430307 | **INTRODUCTION** |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/47` | 0.430307 | **INTRODUCTION** |

### Query 81
- Text: Summarize The following clarifications might be relevant when  Aiding an ally.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/3/Text/19']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 406-423::/page/3/Text/19', 'PZO22001 Starfinder Player Core 406-423::/page/2/Text/9', 'PZO22001 Starfinder Player Core 406-423::/page/3/Text/21']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/3/Text/19', 'PZO22001 Starfinder Player Core 406-423::/page/3/SectionHeader/18', 'PZO22001 Starfinder Player Core 406-423::/page/3/Text/20']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 406-423::/page/3/SectionHeader/18` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/3/Text/20` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/19` | 1.022060 | The following clarifications might be relevant when  Aiding an ally. |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/2/Text/9` | 0.736520 | **Requirements** The ally is willing to accept your aid, and you've  prepared to help (see below). |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/21` | 0.698568 | **Proximity:** You don't necessarily need to be next to  your ally to aid, though you must be in a reasonable  location to help them both when you set up and when  you take the reaction. |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/2/Text/10` | 0.643791 | You try to help your ally with a task. To use this reaction, you  must first prepare to help, usually by using an action during  your turn. You must explain to the GM exactly how you're trying  to hel |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/12/Text/19` | 0.577171 | Some effects target or require an ally, or otherwise refer  to an ally. This must be someone on your side, often another  PC, but it might be a bystander you're trying to protect. You  don't count as |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/2/Text/8` | 0.503917 | **Trigger** An ally is about to use an action that requires a skill  check or attack roll. |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/22` | 0.485366 | **Repetition:** Aiding the same creature multiple times  can have diminishing returns. In particular, if you  try to repeatedly Aid attacks or skill checks against  a creature, the GM will usually inc |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/30` | 0.481551 | You indicate a creature that you can see to one or more allies,  gesturing in a direction and describing the distance verbally.  That creature is hidden to your allies, rather than undetected  (page 4 |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/2/Text/13` | 0.478057 | **Success** You grant your ally a +1 circumstance bonus to the  triggering check. |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/2/Text/11` | 0.465124 | When you use your Aid reaction, attempt a skill check or  attack roll of a type decided by the GM. The typical DC is 15,  but the GM might adjust this DC for particularly hard or easy  tasks. The GM c |

### Query 82
- Text: Summarize if you're using an imprecise sense or if an effect (such as  *invisibility*) prevents the subject from being observed.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/3/Text/23']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 406-423::/page/3/Text/23', 'PZO22001 Starfinder Player Core 406-423::/page/13/Text/89', 'PZO22001 Starfinder Player Core 406-423::/page/3/Text/30']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/3/Text/23', 'PZO22001 Starfinder Player Core 406-423::/page/3/Text/24', 'PZO22001 Starfinder Player Core 406-423::/page/3/Text/22']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 406-423::/page/3/Text/24` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/3/Text/22` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/23` | 1.005954 | if you're using an imprecise sense or if an effect (such as  *invisibility*) prevents the subject from being observed. |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/89` | 0.677106 | strong opinion about you. **Invisible:** Creatures can't see you. **Observed:** You're in plain view. |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/30` | 0.550896 | **Success** You can tell whether the creature is behaving  normally, but you don't know its exact intentions or what  magic might be affecting it. |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/31` | 0.503313 | **Failure** You detect what a deceptive creature wants you to  believe. If they're not being deceptive, you believe they're  behaving normally. |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/84` | 0.501448 | Some effects require you to have line of sight to your target.  As long as you can precisely sense the area (as described  in Perception on page 424) and it isn't blocked by a solid  barrier (as descr |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/30` | 0.498521 | You indicate a creature that you can see to one or more allies,  gesturing in a direction and describing the distance verbally.  That creature is hidden to your allies, rather than undetected  (page 4 |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/24` | 0.495078 | **Critical Success** Any undetected or hidden creature you  critically succeeded against becomes observed by you.  You learn the location of objects in the area you critically  succeeded against. |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/62` | 0.491290 | **Concealed:** Fog or similar obscuration makes you difficult  to see and target. |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/59` | 0.490883 | **Blinded:** You're unable to see. |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/41` | 0.487571 | **Perception and ** **Detection** |

### Query 83
- Text: Summarize **Critical Success** Any undetected or hidden creature you  critically succeeded against becomes observed by you.  You learn the location of objects in the area you critically  succeeded against.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/3/Text/24']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 406-423::/page/3/Text/24', 'PZO22001 Starfinder Player Core 406-423::/page/3/Text/25', 'PZO22001 Starfinder Player Core 406-423::/page/3/Text/29']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/3/Text/24', 'PZO22001 Starfinder Player Core 406-423::/page/3/Text/23', 'PZO22001 Starfinder Player Core 406-423::/page/3/Text/25']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 406-423::/page/3/Text/23` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/3/Text/25` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/24` | 1.039850 | **Critical Success** Any undetected or hidden creature you  critically succeeded against becomes observed by you.  You learn the location of objects in the area you critically  succeeded against. |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/25` | 0.856108 | **Success** Any undetected creature you succeeded against  becomes hidden from you instead of undetected, and  any hidden creature you succeeded against becomes  observed by you. You learn the locatio |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/29` | 0.768677 | **Critical Success** You determine the creature's true intentions  and get a solid idea of any mental magic affecting it. |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/32` | 0.631950 | **Critical Failure** You get a false sense of the creature's  intentions. |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/30` | 0.587494 | You indicate a creature that you can see to one or more allies,  gesturing in a direction and describing the distance verbally.  That creature is hidden to your allies, rather than undetected  (page 4 |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/17` | 0.585723 | The GM attempts a single secret Perception check for  you and compares the result to the Stealth DCs of any  undetected or hidden creatures in the area, or the DC to  detect each object in the area (a |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/30` | 0.583068 | **Success** You can tell whether the creature is behaving  normally, but you don't know its exact intentions or what  magic might be affecting it. |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/17/TableCell/310` | 0.582984 | Critical Success |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/89` | 0.579694 | strong opinion about you. **Invisible:** Creatures can't see you. **Observed:** You're in plain view. |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/31` | 0.570371 | **Failure** You detect what a deceptive creature wants you to  believe. If they're not being deceptive, you believe they're  behaving normally. |

### Query 84
- Text: Summarize **Success** Any undetected creature you succeeded against  becomes hidden from you instead of undetected, and  any hidden creature you succeeded against becomes  observed by you. You learn the location of any object or  get a clue to its whereabouts, as determined by the GM.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/3/Text/25']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 406-423::/page/3/Text/25', 'PZO22001 Starfinder Player Core 406-423::/page/3/Text/24', 'PZO22001 Starfinder Player Core 406-423::/page/3/Text/17']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/3/Text/25', 'PZO22001 Starfinder Player Core 406-423::/page/3/Text/24', 'PZO22001 Starfinder Player Core 406-423::/page/3/SectionHeader/26']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 406-423::/page/3/Text/24` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/3/SectionHeader/26` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/25` | 1.043460 | **Success** Any undetected creature you succeeded against  becomes hidden from you instead of undetected, and  any hidden creature you succeeded against becomes  observed by you. You learn the locatio |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/24` | 0.880856 | **Critical Success** Any undetected or hidden creature you  critically succeeded against becomes observed by you.  You learn the location of objects in the area you critically  succeeded against. |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/17` | 0.760622 | The GM attempts a single secret Perception check for  you and compares the result to the Stealth DCs of any  undetected or hidden creatures in the area, or the DC to  detect each object in the area (a |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/29` | 0.644728 | **Requirements** A creature is undetected by one or more of  your allies but isn't undetected by you. |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/30` | 0.638117 | You indicate a creature that you can see to one or more allies,  gesturing in a direction and describing the distance verbally.  That creature is hidden to your allies, rather than undetected  (page 4 |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/79` | 0.612970 | **Hidden:** A creature you're hidden from knows your location  but can't see you. |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/106` | 0.607837 | **Undetected:** A creature you're undetected by doesn't |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/30` | 0.604947 | **Success** You can tell whether the creature is behaving  normally, but you don't know its exact intentions or what  magic might be affecting it. |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/29` | 0.595932 | **Critical Success** You determine the creature's true intentions  and get a solid idea of any mental magic affecting it. |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/31` | 0.546797 | **Failure** You detect what a deceptive creature wants you to  believe. If they're not being deceptive, you believe they're  behaving normally. |

### Query 85
- Text: Summarize **CONCENTRATE** **SECRET**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/3/SectionHeader/27']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 406-423::/page/3/SectionHeader/15', 'PZO22001 Starfinder Player Core 406-423::/page/3/SectionHeader/27', 'PZO22001 Starfinder Player Core 406-423::/page/3/SectionHeader/7']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/3/SectionHeader/27', 'PZO22001 Starfinder Player Core 406-423::/page/3/SectionHeader/26', 'PZO22001 Starfinder Player Core 406-423::/page/3/Text/28']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 406-423::/page/3/SectionHeader/26` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/3/Text/28` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/3/SectionHeader/15` | 0.994343 | **CONCENTRATE** **SECRET** |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/3/SectionHeader/27` | 0.994343 | **CONCENTRATE** **SECRET** |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/3/SectionHeader/7` | 0.841199 | **CONCENTRATE** |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/5/SectionHeader/40` | 0.799199 | **CONCENTRATE** |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/5/SectionHeader/8` | 0.799199 | **CONCENTRATE** |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/5/SectionHeader/22` | 0.407037 | **MOUNT **[one-action] |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/1/SectionHeader/15` | 0.406908 | **Subordinate Actions** |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/40` | 0.390841 | **Counteracting** |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/15/Text/32` | 0.390841 | **Counteracting** |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/49` | 0.390841 | **Counteracting** |

### Query 86
- Text: Summarize **Critical Success** You determine the creature's true intentions  and get a solid idea of any mental magic affecting it.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/3/Text/29']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 406-423::/page/3/Text/29', 'PZO22001 Starfinder Player Core 406-423::/page/3/Text/24', 'PZO22001 Starfinder Player Core 406-423::/page/3/Text/32']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/3/Text/29', 'PZO22001 Starfinder Player Core 406-423::/page/3/Text/30', 'PZO22001 Starfinder Player Core 406-423::/page/3/Text/28']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 406-423::/page/3/Text/30` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/3/Text/28` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/29` | 1.032217 | **Critical Success** You determine the creature's true intentions  and get a solid idea of any mental magic affecting it. |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/24` | 0.796800 | **Critical Success** Any undetected or hidden creature you  critically succeeded against becomes observed by you.  You learn the location of objects in the area you critically  succeeded against. |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/32` | 0.782294 | **Critical Failure** You get a false sense of the creature's  intentions. |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/30` | 0.721061 | **Success** You can tell whether the creature is behaving  normally, but you don't know its exact intentions or what  magic might be affecting it. |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/31` | 0.599272 | **Failure** You detect what a deceptive creature wants you to  believe. If they're not being deceptive, you believe they're  behaving normally. |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/25` | 0.590296 | **Success** Any undetected creature you succeeded against  becomes hidden from you instead of undetected, and  any hidden creature you succeeded against becomes  observed by you. You learn the locatio |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/7/Text/6` | 0.585331 | **Critical Success** The creature takes no damage. |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/2/Text/12` | 0.558735 | **Critical Success** You grant your ally a +2 circumstance bonus  to the triggering check. If you're a master with the check  you attempted, the bonus is +3, and if you're legendary,  it's +4. |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/28` | 0.556568 | You try to tell whether a creature's behavior is abnormal.  Choose one creature and assess it for odd body language,  signs of nervousness, and other indicators that it might be  trying to deceive som |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/17/TableCell/310` | 0.545773 | Critical Success |

### Query 87
- Text: Summarize **Failure** You detect what a deceptive creature wants you to  believe. If they're not being deceptive, you believe they're  behaving normally.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/3/Text/31']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 406-423::/page/3/Text/31', 'PZO22001 Starfinder Player Core 406-423::/page/3/Text/32', 'PZO22001 Starfinder Player Core 406-423::/page/3/Text/30']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/3/Text/31', 'PZO22001 Starfinder Player Core 406-423::/page/3/Text/30', 'PZO22001 Starfinder Player Core 406-423::/page/3/Text/32']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 406-423::/page/3/Text/30` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/3/Text/32` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/31` | 1.039601 | **Failure** You detect what a deceptive creature wants you to  believe. If they're not being deceptive, you believe they're  behaving normally. |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/32` | 0.758616 | **Critical Failure** You get a false sense of the creature's  intentions. |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/30` | 0.645219 | **Success** You can tell whether the creature is behaving  normally, but you don't know its exact intentions or what  magic might be affecting it. |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/29` | 0.570064 | **Critical Success** You determine the creature's true intentions  and get a solid idea of any mental magic affecting it. |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/7/Text/8` | 0.561462 | **Failure** The creature takes bludgeoning damage equal to half  the falling damage you took. |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/24` | 0.547171 | **Critical Success** Any undetected or hidden creature you  critically succeeded against becomes observed by you.  You learn the location of objects in the area you critically  succeeded against. |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/17/TableCell/309` | 0.519794 | Failure |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/28` | 0.514038 | You try to tell whether a creature's behavior is abnormal.  Choose one creature and assess it for odd body language,  signs of nervousness, and other indicators that it might be  trying to deceive som |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/2/Text/30` | 0.513844 | **Critical Failure** You don't get free, and you can't attempt to  Escape again until your next turn. |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/7/Text/9` | 0.512327 | **Critical Failure** The creature takes the same amount of  bludgeoning damage you took from the fall. |

### Query 88
- Text: Summarize **Critical Failure** You get a false sense of the creature's  intentions.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/3/Text/32']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 406-423::/page/3/Text/32', 'PZO22001 Starfinder Player Core 406-423::/page/3/Text/29', 'PZO22001 Starfinder Player Core 406-423::/page/3/Text/31']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/3/Text/32', 'PZO22001 Starfinder Player Core 406-423::/page/3/Text/34', 'PZO22001 Starfinder Player Core 406-423::/page/3/Text/31']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 406-423::/page/3/Text/34` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/3/Text/31` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/32` | 1.034558 | **Critical Failure** You get a false sense of the creature's  intentions. |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/29` | 0.779613 | **Critical Success** You determine the creature's true intentions  and get a solid idea of any mental magic affecting it. |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/31` | 0.762681 | **Failure** You detect what a deceptive creature wants you to  believe. If they're not being deceptive, you believe they're  behaving normally. |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/2/Text/30` | 0.643947 | **Critical Failure** You don't get free, and you can't attempt to  Escape again until your next turn. |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/24` | 0.641321 | **Critical Success** Any undetected or hidden creature you  critically succeeded against becomes observed by you.  You learn the location of objects in the area you critically  succeeded against. |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/17/Text/19` | 0.636010 | Critical Failure You fail to counteract the target. |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/7/Text/9` | 0.631223 | **Critical Failure** The creature takes the same amount of  bludgeoning damage you took from the fall. |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/30` | 0.610109 | **Success** You can tell whether the creature is behaving  normally, but you don't know its exact intentions or what  magic might be affecting it. |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/7/Text/6` | 0.535765 | **Critical Success** The creature takes no damage. |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/7/Text/8` | 0.535605 | **Failure** The creature takes bludgeoning damage equal to half  the falling damage you took. |

### Query 89
- Text: Summarize **INTRODUCTION**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/3/Text/34']
- Expected found: `True`
- Expected rank: `5`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 406-423::/page/11/Text/20', 'PZO22001 Starfinder Player Core 406-423::/page/13/Text/30', 'PZO22001 Starfinder Player Core 406-423::/page/5/Text/47']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/3/Text/34', 'PZO22001 Starfinder Player Core 406-423::/page/3/Text/35', 'PZO22001 Starfinder Player Core 406-423::/page/3/Text/32']
- Expanded expected found: `True`
- Expanded expected rank: `5`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 406-423::/page/3/Text/35` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/3/Text/32` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/11/Text/20` | 0.880541 | **INTRODUCTION** |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/30` | 0.880541 | **INTRODUCTION** |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/47` | 0.880541 | **INTRODUCTION** |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/21` | 0.838541 | **INTRODUCTION** |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/34` | 0.838541 | **INTRODUCTION** |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/9/Text/23` | 0.838541 | **INTRODUCTION** |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/7/Text/27` | 0.838541 | **INTRODUCTION** |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/17/Text/24` | 0.672734 | INTRODUCTION |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/31` | 0.581679 | **BACKGROUNDS** |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/55` | 0.524467 | **INDEX** |

### Query 90
- Text: Summarize **CLASSES**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/3/Text/36']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 406-423::/page/11/Text/22', 'PZO22001 Starfinder Player Core 406-423::/page/9/Text/25', 'PZO22001 Starfinder Player Core 406-423::/page/3/Text/36']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/3/Text/36', 'PZO22001 Starfinder Player Core 406-423::/page/3/Text/35', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/23', 'PZO22001 Starfinder Player Core 406-423::/page/13/Text/4', 'PZO22001 Starfinder Player Core 406-423::/page/11/Text/22', 'PZO22001 Starfinder Player Core 406-423::/page/5/Text/49', 'PZO22001 Starfinder Player Core 406-423::/page/9/Text/25', 'PZO22001 Starfinder Player Core 406-423::/page/7/Text/29', 'PZO22001 Starfinder Player Core 406-423::/page/3/Text/37']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 406-423::/page/3/Text/35` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/1/Text/23` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/13/Text/4` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/11/Text/22` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/5/Text/49` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/9/Text/25` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/7/Text/29` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/3/Text/37` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/11/Text/22` | 0.940061 | **CLASSES** |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/9/Text/25` | 0.940061 | **CLASSES** |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/36` | 0.940061 | **CLASSES** |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/49` | 0.910061 | **CLASSES** |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/23` | 0.910061 | **CLASSES** |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/7/Text/29` | 0.910061 | **CLASSES** |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/4` | 0.910061 | **CLASSES** |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/17/Text/26` | 0.763092 | CLASSES |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/55` | 0.463681 | **INDEX** |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/9/Text/26` | 0.437714 | **SKILLS** |

### Query 91
- Text: Summarize **PLAYING THE ** **GAME**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/3/Text/40']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 406-423::/page/7/Text/34', 'PZO22001 Starfinder Player Core 406-423::/page/5/Text/53', 'PZO22001 Starfinder Player Core 406-423::/page/3/Text/40']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/3/Text/40', 'PZO22001 Starfinder Player Core 406-423::/page/3/Text/39', 'PZO22001 Starfinder Player Core 406-423::/page/3/Text/41']
- Expanded expected found: `True`
- Expanded expected rank: `3`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 406-423::/page/3/Text/39` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/3/Text/41` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/53` | 0.965000 | **PLAYING THE ** **GAME** |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/7/Text/34` | 0.965000 | **PLAYING THE ** **GAME** |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/40` | 0.965000 | **PLAYING THE ** **GAME** |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/28` | 0.923000 | **PLAYING THE ** **GAME** |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/36` | 0.923000 | **PLAYING THE ** **GAME** |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/11/Text/26` | 0.923000 | **PLAYING THE ** **GAME** |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/9/Text/29` | 0.923000 | **PLAYING THE ** **GAME** |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/15/Text/19` | 0.811006 | **PLAYING THE ** |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/17/Text/31` | 0.749688 | PLAYING THE GAME |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/15/Text/41` | 0.663024 | **GAME** |

### Query 92
- Text: Summarize **Rules Overview**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/3/Text/41']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/29', 'PZO22001 Starfinder Player Core 406-423::/page/3/Text/41', 'PZO22001 Starfinder Player Core 406-423::/page/9/Text/30']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/3/Text/41', 'PZO22001 Starfinder Player Core 406-423::/page/3/Text/40', 'PZO22001 Starfinder Player Core 406-423::/page/3/Text/42']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 406-423::/page/3/Text/40` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/3/Text/42` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/29` | 0.894112 | **Rules Overview** |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/41` | 0.894112 | **Rules Overview** |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/9/Text/30` | 0.894112 | **Rules Overview** |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/7/Text/35` | 0.852112 | **Rules Overview** |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/54` | 0.852112 | **Rules Overview** |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/15/Text/20` | 0.852112 | **Rules Overview** |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/11/Text/27` | 0.852112 | **Rules Overview** |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/37` | 0.852112 | **Rules Overview** |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/17/Text/32` | 0.779340 | Rules Overview |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/1/SectionHeader/10` | 0.493204 | **IN-DEPTH ACTION RULES** |

### Query 93
- Text: Summarize **Immunity, ** **Weakness, & ** **Resistance**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/3/Text/44']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 406-423::/page/3/Text/44', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/32', 'PZO22001 Starfinder Player Core 406-423::/page/7/Text/38']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/3/Text/44', 'PZO22001 Starfinder Player Core 406-423::/page/3/Text/43', 'PZO22001 Starfinder Player Core 406-423::/page/3/Text/45']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 406-423::/page/3/Text/43` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/3/Text/45` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/44` | 1.020504 | **Immunity, ** **Weakness, & ** **Resistance** |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/32` | 1.020504 | **Immunity, ** **Weakness, & ** **Resistance** |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/7/Text/38` | 1.020504 | **Immunity, ** **Weakness, & ** **Resistance** |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/57` | 0.978504 | **Immunity, ** **Weakness, & ** **Resistance** |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/11/Text/30` | 0.978504 | **Immunity, ** **Weakness, & ** **Resistance** |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/9/Text/33` | 0.978504 | **Immunity, ** **Weakness, & ** **Resistance** |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/15/Text/23` | 0.978504 | **Immunity, ** **Weakness, & ** **Resistance** |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/17/Text/35` | 0.918890 | Immunity, Weakness, & Resistance |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/13` | 0.881551 | **Immunity, ** **Weakness, & ** |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/40` | 0.637808 | **Resistance** |

### Query 94
- Text: Summarize **Hero Points**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/3/Text/47']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 406-423::/page/3/Text/47', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/35', 'PZO22001 Starfinder Player Core 406-423::/page/5/Text/60']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/3/Text/47', 'PZO22001 Starfinder Player Core 406-423::/page/3/Text/46', 'PZO22001 Starfinder Player Core 406-423::/page/3/Text/48']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 406-423::/page/3/Text/46` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/3/Text/48` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/47` | 0.970595 | **Hero Points** |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/35` | 0.970595 | **Hero Points** |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/60` | 0.970595 | **Hero Points** |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/9/Text/36` | 0.928595 | **Hero Points** |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/7/Text/41` | 0.928595 | **Hero Points** |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/15/Text/26` | 0.928595 | **Hero Points** |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/16` | 0.928595 | **Hero Points** |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/11/Text/33` | 0.928595 | **Hero Points** |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/17/Text/38` | 0.806477 | Hero Points |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/15` | 0.506598 | **Hit Points, ** **Healing, and ** |

### Query 95
- Text: Summarize **Movement**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/3/Text/49']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 406-423::/page/13/Text/45', 'PZO22001 Starfinder Player Core 406-423::/page/3/Text/49', 'PZO22001 Starfinder Player Core 406-423::/page/7/Text/43']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/3/Text/49', 'PZO22001 Starfinder Player Core 406-423::/page/3/Text/50', 'PZO22001 Starfinder Player Core 406-423::/page/3/Text/48']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 406-423::/page/3/Text/50` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/3/Text/48` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/45` | 0.929132 | **Movement** |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/49` | 0.929132 | **Movement** |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/7/Text/43` | 0.929132 | **Movement** |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/15/Text/28` | 0.887132 | **Movement** |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/62` | 0.887132 | **Movement** |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/9/Text/38` | 0.887132 | **Movement** |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/11/Text/35` | 0.887132 | **Movement** |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/37` | 0.887132 | **Movement** |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/8/SectionHeader/1` | 0.620839 | **REACTIONS TO MOVEMENT** |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/6/SectionHeader/1` | 0.614658 | MOVEMENT |

### Query 96
- Text: Summarize **Effects** **Area**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/3/Text/50']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/38', 'PZO22001 Starfinder Player Core 406-423::/page/3/Text/50', 'PZO22001 Starfinder Player Core 406-423::/page/17/Text/41']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/3/Text/50', 'PZO22001 Starfinder Player Core 406-423::/page/3/Text/49', 'PZO22001 Starfinder Player Core 406-423::/page/3/Text/51']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 406-423::/page/3/Text/49` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/3/Text/51` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/38` | 0.987469 | **Effects** **Area** |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/50` | 0.987469 | **Effects** **Area** |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/17/Text/41` | 0.814158 | Effects Area |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/7/Text/44` | 0.746103 | **Effects** |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/63` | 0.746103 | **Effects** |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/9/Text/39` | 0.746103 | **Effects** |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/11/Text/36` | 0.746103 | **Effects** |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/15/Text/29` | 0.746103 | **Effects** |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/18` | 0.746103 | **Effects** |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/12/SectionHeader/1` | 0.684706 | EFFECTS |

### Query 97
- Text: Summarize **Afflictions**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/3/Text/51']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 406-423::/page/3/Text/51', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/39', 'PZO22001 Starfinder Player Core 406-423::/page/13/Text/48']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/3/Text/51', 'PZO22001 Starfinder Player Core 406-423::/page/3/Text/50', 'PZO22001 Starfinder Player Core 406-423::/page/3/Text/52']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 406-423::/page/3/Text/50` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/3/Text/52` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/51` | 0.968407 | **Afflictions** |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/39` | 0.968407 | **Afflictions** |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/48` | 0.968407 | **Afflictions** |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/15/Text/31` | 0.926407 | **Afflictions** |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/11/Text/37` | 0.844597 | **Area** **Afflictions** |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/64` | 0.844597 | **Area** **Afflictions** |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/7/Text/46` | 0.743603 | **Afflictions** **Counteracting** |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/9/Text/41` | 0.743603 | **Afflictions** **Counteracting** |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/16/Text/5` | 0.585084 | Whether appearing in a spell, as an item, or within a creature's  stat block, afflictions appear in the following format. |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/16/Text/2` | 0.497975 | Diseases and poisons are types of afflictions, as are curses and radiation. An affliction can infect a  creature for a long time, progressing through different and often increasingly debilitating stag |

### Query 98
- Text: Summarize **Perception and ** **Detection**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/3/Text/53']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 406-423::/page/5/Text/66', 'PZO22001 Starfinder Player Core 406-423::/page/3/Text/53', 'PZO22001 Starfinder Player Core 406-423::/page/1/Text/41']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/3/Text/53', 'PZO22001 Starfinder Player Core 406-423::/page/3/Text/54', 'PZO22001 Starfinder Player Core 406-423::/page/3/Text/52']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 406-423::/page/3/Text/54` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/3/Text/52` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/66` | 0.992556 | **Perception and ** **Detection** |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/53` | 0.992556 | **Perception and ** **Detection** |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/41` | 0.992556 | **Perception and ** **Detection** |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/15/Text/33` | 0.950556 | **Perception and ** **Detection** |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/9/Text/42` | 0.818773 | **Perception and ** |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/7/Text/47` | 0.818773 | **Perception and ** |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/50` | 0.818773 | **Perception and ** |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/11/Text/39` | 0.818773 | **Perception and ** |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/23` | 0.733480 | **Detection** |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/17/Text/44` | 0.720729 | Perception and |

### Query 99
- Text: Summarize **Encounter ** **Mode**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/3/Text/54']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/42', 'PZO22001 Starfinder Player Core 406-423::/page/3/Text/54', 'PZO22001 Starfinder Player Core 406-423::/page/5/Text/67']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/3/Text/54', 'PZO22001 Starfinder Player Core 406-423::/page/3/Text/55', 'PZO22001 Starfinder Player Core 406-423::/page/3/Text/53']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 406-423::/page/3/Text/55` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/3/Text/53` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/42` | 0.996085 | **Encounter ** **Mode** |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/54` | 0.996085 | **Encounter ** **Mode** |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/67` | 0.996085 | **Encounter ** **Mode** |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/15/Text/34` | 0.954085 | **Encounter ** **Mode** |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/7/Text/48` | 0.877882 | **Detection** **Encounter ** **Mode** |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/9/Text/43` | 0.877882 | **Detection** **Encounter ** **Mode** |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/24` | 0.792479 | **Encounter ** |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/11/Text/40` | 0.732350 | **Detection** **Encounter ** |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/68` | 0.650901 | **Exploration ** **Mode** |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/43` | 0.650901 | **Exploration ** **Mode** |

### Query 100
- Text: Lookup values for SizeSpaceReach (Tall)Reach (Long)TinyLess than 5
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/7/Table/25']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 406-423::/page/7/Table/25', 'PZO22001 Starfinder Player Core 406-423::/page/7/SectionHeader/21', 'PZO22001 Starfinder Player Core 406-423::/page/7/SectionHeader/24']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/7/Table/25', 'PZO22001 Starfinder Player Core 406-423::/page/7/TableCell/544', 'PZO22001 Starfinder Player Core 406-423::/page/7/SectionHeader/24']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 406-423::/page/7/TableCell/544` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/7/SectionHeader/24` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/7/Table/25` | 0.844772 | SizeSpaceReach (Tall)Reach (Long)TinyLess than 5 feet0 feet0 feetSmall5 feet5 feet5 feetMedium5 feet5 feet5 feetLarge10 feet10 feet5 feetHuge15 feet15 feet10 feetGargantuan20 feet or more20 feet15 fee |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/7/SectionHeader/21` | 0.651444 | SIZE, SPACE, AND REACH |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/7/SectionHeader/24` | 0.596702 | **SIZE AND REACH** |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/7/Text/22` | 0.510647 | Creatures and objects of different sizes occupy different  amounts of space. The sizes and the spaces they each take  up on a grid are listed in the Size and Reach table (see below).  The table also l |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/15/SectionHeader/3` | 0.503122 | **5 feet** **M** **10 feet** **5 feet** **L** **10 feet** **M** **L** |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/7/TableCell/546` | 0.482297 | Reach (Tall) |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/7/TableCell/549` | 0.473668 | Less than 5 feet |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/12/Text/15` | 0.472793 | **Reach** is how far you can physically reach with your  body or a weapon. Melee Strikes rely on reach. Your reach is  typically 5 feet, but weapons with the reach trait can extend  this. Larger creat |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/7/TableCell/547` | 0.442709 | Reach (Long) |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/12/SectionHeader/11` | 0.418707 | RANGE AND REACH |

### Query 101
- Text: Lookup values for Type of CoverBonusCan HideLesser+1 to ACNoStandard+2 to AC, Reflex,
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/10/Table/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 406-423::/page/10/Table/10', 'PZO22001 Starfinder Player Core 406-423::/page/10/Text/9', 'PZO22001 Starfinder Player Core 406-423::/page/4/Text/23']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/10/Table/10', 'PZO22001 Starfinder Player Core 406-423::/page/10/Text/9', 'PZO22001 Starfinder Player Core 406-423::/page/10/TableCell/302']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 406-423::/page/10/Text/9` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/10/TableCell/302` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/10/Table/10` | 0.918113 | Type of CoverBonusCan HideLesser+1 to ACNoStandard+2 to AC, Reflex, StealthYesGreater+4 to AC, Reflex, StealthYes |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/10/Text/9` | 0.650012 | When you're behind an obstacle that could block weapons,  guard you against explosions, and make you harder to detect,  you're behind cover. Standard cover gives you a +2 circumstance  bonus to AC, to |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/4/Text/23` | 0.613551 | You press yourself against a wall or duck behind an obstacle  to take better advantage of cover (page 416). If you would  have standard cover, you instead gain greater cover, which  provides a +4 circ |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/4/Text/22` | 0.536838 | **Requirements** You are benefiting from cover, are near a  feature that allows you to take cover, or are prone. |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/10/TableCell/309` | 0.521610 | +2 to AC, Reflex, Stealth |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/10/TableCell/312` | 0.515832 | +4 to AC, Reflex, Stealth |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/10/TableCell/302` | 0.500203 | Type of Cover |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/10/Text/12` | 0.417705 | Usually, the GM can quickly decide whether your target  has cover. If you're uncertain or need to be more precise,  draw a line from the center of your space to the center of  the target's space. If t |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/10/TableCell/306` | 0.390734 | +1 to AC |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/10/Text/11` | 0.384016 | Cover is relative, so you might simultaneously have cover  against one creature and not another. Cover applies only if  your path to the target is partially blocked. If a creature is  entirely behind |

### Query 102
- Text: Lookup values for Counteract
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/17/Table/22']
- Expected found: `True`
- Expected rank: `6`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 406-423::/page/17/TableCell/308', 'PZO22001 Starfinder Player Core 406-423::/page/17/Text/43', 'PZO22001 Starfinder Player Core 406-423::/page/17/Text/18']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/17/Table/22', 'PZO22001 Starfinder Player Core 406-423::/page/17/TableCell/308', 'PZO22001 Starfinder Player Core 406-423::/page/17/Text/21']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 406-423::/page/17/TableCell/308` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 406-423::/page/17/Text/21` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/17/TableCell/308` | 0.754090 | Counteract Rank |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/17/Text/43` | 0.708786 | Counteracting |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/17/Text/18` | 0.625424 | Success Counteract the target if its counteract rank is no more than 1 higher than your effect's counteract rank.  Failure Counteract the target if its counteract rank is lower than your effect's coun |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/17/Text/21` | 0.562162 | This table provides a reference for what an effect can counteract based on its rank and the check result. The first number in each column is the counteract rank at which you can counteract an effect b |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/17/Text/17` | 0.556661 | **Critical Success** Counteract the target if its counteract rank is no more than 3 higher than your effect's counteract rank. |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/17/Table/22` | 0.551602 | Counteract RankFailureCritical SuccessSuccess0-1 (1 to 2)3 (5 to 6)10 (-1 to 0)2 (3 to 4)4 (7 to 8)21 (1 to 2)3 (5 to 6)5 (9 to 10)32 (3 to 4)4 (7 to 8)6 (11 to 12)43 (5 to 6)5 (9 to 10)7 (13 to 14)54 |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/17/SectionHeader/20` | 0.550101 | **Counteract Table ** |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/17/Text/16` | 0.519906 | What you can counteract depends on the check result and the target's counteract rank. If an effect is a spell, its rank is the counteract rank. Otherwise, halve its level and round up to determine its |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/17/Text/14` | 0.514259 | Some effects try to counteract spells, afflictions, conditions, or other effects. Counteract checks compare the power of two forces and determine which defeats the other. Successfully counteracting an |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/65` | 0.503924 | **Counteracting** |
