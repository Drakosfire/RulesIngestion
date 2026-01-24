# RulesLawyer Evaluation Report: nomic-embed-text-v2

## Summary
- Run ID: `None`
- Ruleset ID: `None`
- Document ID: `None`
- Chunk source: `enriched`
- Chunk count: `601`
- Query count: `102`
- Evaluated queries: `102`
- Coverage: `1.0000`
- MRR: `0.8501`
- hit@1: `0.7745`
- hit@3: `0.9118`
- hit@5: `0.9412`
- hit@10: `1.0000`
- Embeddings reused: `False`
- Graph boost: `0.05` (depth=2, top_k=50, source=top, seed_top_n=3, same_kind_only=False, decay=0.4)

### Expanded Gold Metrics
- Coverage: `1.0000`
- MRR: `0.8814`
- hit@1: `0.8137`
- hit@3: `0.9412`
- hit@5: `0.9706`
- hit@10: `1.0000`

### Expanded Gold Expansion Stats
- Queries with additions: `102`
- Avg added per query: `2.27`
- Max added: `10`
- Addition reasons:
  - graph_depth_1: `232`

### Expanded Gold Delta (Expanded - Strict)
- Coverage Δ: `0.0000`
- MRR Δ: `0.0313`
- hit@1 Δ: `0.0392`
- hit@3 Δ: `0.0294`
- hit@5 Δ: `0.0294`
- hit@10 Δ: `0.0000`

## Timings (ms)
- Embedding (chunks): `10951`
- Embedding (queries): `2885`
- Evaluation (strict): `50`
- Evaluation (expanded): `32`
- Total: `18508`

### Timing Estimates (ms)
- Evaluation (strict): `71`
- Evaluation (expanded): `20`
- Total: `13927`

## Query Details
### Query 0
- Text: Summarize CHAPTER 8: PLAYING THE GAME
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/1/SectionHeader/0']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 388-405::/page/1/SectionHeader/0', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/28', 'PZO22001 Starfinder Player Core 388-405::/page/7/Text/20']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/1/SectionHeader/0', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/1']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 388-405::/page/1/Text/1` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 388-405::/page/1/SectionHeader/0` | 1.014311 | CHAPTER 8: PLAYING THE GAME |
| 2 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/28` | 0.719505 | **PLAYING THE ** **GAME** |
| 3 | `PZO22001 Starfinder Player Core 388-405::/page/7/Text/20` | 0.719505 | **PLAYING THE ** **GAME** |
| 4 | `PZO22001 Starfinder Player Core 388-405::/page/5/Text/23` | 0.677505 | **PLAYING THE ** **GAME** |
| 5 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/39` | 0.677505 | **PLAYING THE ** **GAME** |
| 6 | `PZO22001 Starfinder Player Core 388-405::/page/9/Text/26` | 0.677505 | **PLAYING THE ** **GAME** |
| 7 | `PZO22001 Starfinder Player Core 388-405::/page/13/Text/32` | 0.677505 | **PLAYING THE ** **GAME** |
| 8 | `PZO22001 Starfinder Player Core 388-405::/page/17/Text/17` | 0.538575 | **PLAYING THE ** |
| 9 | `PZO22001 Starfinder Player Core 388-405::/page/11/Text/21` | 0.538575 | **PLAYING THE ** |
| 10 | `PZO22001 Starfinder Player Core 388-405::/page/15/Text/25` | 0.538575 | **PLAYING THE ** |

### Query 1
- Text: What is the rule about At this point, you have a character and are ready to play Starfinder! Or maybe you're the GM and you're  getting ready to run your first adventure. Either way, this chapter provides the full details for the rules  outlined in Chapter 1. This chapter begins by describing the general rules and conventions of how the  game is played and then presents more in-depth explanations of the rules for each mode of play.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/1/Text/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 388-405::/page/1/Text/1', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/3', 'PZO22001 Starfinder Player Core 388-405::/page/3/Text/2']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/1/Text/1', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/3', 'PZO22001 Starfinder Player Core 388-405::/page/1/SectionHeader/0']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 388-405::/page/1/Text/3` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/1/SectionHeader/0` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/1` | 1.024797 | At this point, you have a character and are ready to play Starfinder! Or maybe you're the GM and you're  getting ready to run your first adventure. Either way, this chapter provides the full details f |
| 2 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/3` | 0.816020 | Before diving into how to play Starfinder, it's important to  understand the game's three modes of play, which determine  the pace of your adventure and the specific rules you'll use  at a given time. |
| 3 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/2` | 0.808292 | Starfinder has many specific rules, but you'll also want to keep these general guidelines in mind when playing. |
| 4 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/4` | 0.703314 | If you're ever uncertain how to apply a rule, the GM decides.  Of course, Starfinder is a game, so when adjudicating the  rules, the GM is encouraged to listen to everyone's point of  view and make a |
| 5 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/6` | 0.642987 | A core principle of Starfinder is that specific rules override  general ones. If two rules conflict, the more specific  one takes precedence. If there's still ambiguity, the GM  determines which rule |
| 6 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/5` | 0.615985 | In **exploration mode**, time is more flexible and the play  more free-form. Minutes, hours, or even days in the game  world pass quickly in the real world, as the characters travel  between star syst |
| 7 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/4` | 0.583064 | The most intricate of the modes is **encounter mode**. This  is where most of the intense action takes place, and it's  most often used for combat or other high-stakes situations.  The GM typically sw |
| 8 | `PZO22001 Starfinder Player Core 388-405::/page/11/Text/22` | 0.564192 | **GAME** **Rules Overview** |
| 9 | `PZO22001 Starfinder Player Core 388-405::/page/9/Text/7` | 0.534518 | Starfinder has a variety of skills for many different situations,  from Athletics to Computers to Piloting. Each grants you a  set of related actions that rely on you rolling a skill check.  Each skil |
| 10 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/12` | 0.528437 | Your group will likely talk about what types of content you  want in your game before your campaign begins. The following  is a set of basic assumptions that works for many groups. The  GM can find mo |

### Query 2
- Text: What is the rule about Before diving into how to play Starfinder, it's important to  understand the game's three modes of play, which determine  the pace of your adventure and the specific rules you'll use  at a given time. Each mode provides a different pace and  presents a different level of risk to your characters. The Game  Master (GM) determines which mode works best for the story  and controls the transition between them. You'll likely talk  about the modes less formally during your play session,  simply transitioning between exploration and encounters  during the adventure, before heading to a settlement to  achieve something during downtime.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/1/Text/3']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 388-405::/page/1/Text/3', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/1', 'PZO22001 Starfinder Player Core 388-405::/page/3/Text/4']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/1/Text/3', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/1', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/4']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 388-405::/page/1/Text/1` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/1/Text/4` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/3` | 1.024733 | Before diving into how to play Starfinder, it's important to  understand the game's three modes of play, which determine  the pace of your adventure and the specific rules you'll use  at a given time. |
| 2 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/1` | 0.860053 | At this point, you have a character and are ready to play Starfinder! Or maybe you're the GM and you're  getting ready to run your first adventure. Either way, this chapter provides the full details f |
| 3 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/4` | 0.765472 | If you're ever uncertain how to apply a rule, the GM decides.  Of course, Starfinder is a game, so when adjudicating the  rules, the GM is encouraged to listen to everyone's point of  view and make a |
| 4 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/2` | 0.704304 | Starfinder has many specific rules, but you'll also want to keep these general guidelines in mind when playing. |
| 5 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/5` | 0.688470 | In **exploration mode**, time is more flexible and the play  more free-form. Minutes, hours, or even days in the game  world pass quickly in the real world, as the characters travel  between star syst |
| 6 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/4` | 0.631981 | The most intricate of the modes is **encounter mode**. This  is where most of the intense action takes place, and it's  most often used for combat or other high-stakes situations.  The GM typically sw |
| 7 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/6` | 0.630566 | A core principle of Starfinder is that specific rules override  general ones. If two rules conflict, the more specific  one takes precedence. If there's still ambiguity, the GM  determines which rule |
| 8 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/9` | 0.604318 | Often, your choices have no immediate risk or consequences.  If you're exploring a starship and come across an intersection,  the GM asks, "Which way do you go?" You might choose to  take the corridor |
| 9 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/8` | 0.600298 | Throughout the game, the GM describes what's happening in  the world and then asks the players, "So what do you do?"  Exactly what you choose to do, and how the GM responds to  those choices, builds a |
| 10 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/6` | 0.599789 | The third mode is **downtime**. During downtime, the  characters are at little risk, and the passage of time is  measured in days or longer. This is when you might repair  or craft new equipment, rese |

### Query 3
- Text: What is the rule about The most intricate of the modes is **encounter mode**. This  is where most of the intense action takes place, and it's  most often used for combat or other high-stakes situations.  The GM typically switches to encounter mode by calling on  the players to "roll for initiative" to determine the order in  which all the actors take their turns during the encounter.  Time is then divided into a series of rounds, each lasting  roughly 6 seconds in the game world. Each round, player  characters, other creatures, and sometimes even hazards or  events take their turn in initiative order. At the start of a  participant's turn, they gain the use of a number of actions  (typically 3 in the case of PCs and other creatures) as well  as a special action called a reaction. These actions, and what  you do with them, are how you affect the world within an  encounter. The full rules for playing in encounter mode start  on page 427.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/1/Text/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 388-405::/page/1/Text/4', 'PZO22001 Starfinder Player Core 388-405::/page/2/Text/4', 'PZO22001 Starfinder Player Core 388-405::/page/9/Text/5']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/1/Text/4', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/5', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/3']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 388-405::/page/1/Text/5` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/1/Text/3` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/4` | 1.010259 | The most intricate of the modes is **encounter mode**. This  is where most of the intense action takes place, and it's  most often used for combat or other high-stakes situations.  The GM typically sw |
| 2 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/4` | 0.799659 | This game presents three main methods of structuring play.  **Encounter mode** (page 427) is highly structured and is most  often used for combat or stressful situations. Everyone in an  encounter rol |
| 3 | `PZO22001 Starfinder Player Core 388-405::/page/9/Text/5` | 0.726562 | Often, you'll roll a Perception check to determine your order  in initiative. When you do this, instead of comparing the  result against a DC, the GM will put the results for everyone  in the encounte |
| 4 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/5` | 0.683214 | In **exploration mode**, time is more flexible and the play  more free-form. Minutes, hours, or even days in the game  world pass quickly in the real world, as the characters travel  between star syst |
| 5 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/1` | 0.589921 | At this point, you have a character and are ready to play Starfinder! Or maybe you're the GM and you're  getting ready to run your first adventure. Either way, this chapter provides the full details f |
| 6 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/3` | 0.589416 | Before diving into how to play Starfinder, it's important to  understand the game's three modes of play, which determine  the pace of your adventure and the specific rules you'll use  at a given time. |
| 7 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/8` | 0.557211 | During an encounter, you get 3 actions and 1 reaction per turn  (page 427). Icons indicate whether your abilities take a single  action [one-action], 2 actions [two-actions], 3 actions [three-actions] |
| 8 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/8` | 0.544835 | Throughout the game, the GM describes what's happening in  the world and then asks the players, "So what do you do?"  Exactly what you choose to do, and how the GM responds to  those choices, builds a |
| 9 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/5` | 0.543262 | **Exploration** **mode** (page 430) takes place over minutes or  hours. You use your travel Speed if you're moving, and you  engage in **exploration** **activities** like Avoiding Notice, Detecting  M |
| 10 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/6` | 0.533522 | The third mode is **downtime**. During downtime, the  characters are at little risk, and the passage of time is  measured in days or longer. This is when you might repair  or craft new equipment, rese |

### Query 4
- Text: What is the rule about In **exploration mode**, time is more flexible and the play  more free-form. Minutes, hours, or even days in the game  world pass quickly in the real world, as the characters travel  between star systems, explore uninhabited wilderness on  a planet, recover from a battle, or roleplay during a social  gathering. Often, developments during exploration lead to  encounters, and the GM will switch to that mode of play until  the encounter ends, before returning to exploration mode.  The rules for exploration start on page 430.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/1/Text/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 388-405::/page/1/Text/5', 'PZO22001 Starfinder Player Core 388-405::/page/2/Text/5', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/4']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/1/Text/5', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/6', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/4']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 388-405::/page/1/Text/6` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/1/Text/4` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/5` | 1.009146 | In **exploration mode**, time is more flexible and the play  more free-form. Minutes, hours, or even days in the game  world pass quickly in the real world, as the characters travel  between star syst |
| 2 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/5` | 0.762255 | **Exploration** **mode** (page 430) takes place over minutes or  hours. You use your travel Speed if you're moving, and you  engage in **exploration** **activities** like Avoiding Notice, Detecting  M |
| 3 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/4` | 0.694002 | The most intricate of the modes is **encounter mode**. This  is where most of the intense action takes place, and it's  most often used for combat or other high-stakes situations.  The GM typically sw |
| 4 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/3` | 0.635021 | Before diving into how to play Starfinder, it's important to  understand the game's three modes of play, which determine  the pace of your adventure and the specific rules you'll use  at a given time. |
| 5 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/6` | 0.620156 | The third mode is **downtime**. During downtime, the  characters are at little risk, and the passage of time is  measured in days or longer. This is when you might repair  or craft new equipment, rese |
| 6 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/1` | 0.600527 | At this point, you have a character and are ready to play Starfinder! Or maybe you're the GM and you're  getting ready to run your first adventure. Either way, this chapter provides the full details f |
| 7 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/4` | 0.570981 | This game presents three main methods of structuring play.  **Encounter mode** (page 427) is highly structured and is most  often used for combat or stressful situations. Everyone in an  encounter rol |
| 8 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/8` | 0.550559 | Throughout the game, the GM describes what's happening in  the world and then asks the players, "So what do you do?"  Exactly what you choose to do, and how the GM responds to  those choices, builds a |
| 9 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/9` | 0.542238 | Often, your choices have no immediate risk or consequences.  If you're exploring a starship and come across an intersection,  the GM asks, "Which way do you go?" You might choose to  take the corridor |
| 10 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/26` | 0.517162 | Skill checks are required for all sorts of other tasks related  to adventuring and life in general. Most of their rules are  in Chapter 4 (page 183). You'll find the rules for **calculating ** **skill |

### Query 5
- Text: What is the rule about The third mode is **downtime**. During downtime, the  characters are at little risk, and the passage of time is  measured in days or longer. This is when you might repair  or craft new equipment, research a new spell, or prepare for  your next adventure. The rules for downtime are on page 433.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/1/Text/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 388-405::/page/1/Text/6', 'PZO22001 Starfinder Player Core 388-405::/page/2/Text/6', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/5']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/1/Text/6', 'PZO22001 Starfinder Player Core 388-405::/page/1/SectionHeader/7', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/5']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 388-405::/page/1/SectionHeader/7` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/1/Text/5` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/6` | 0.996234 | The third mode is **downtime**. During downtime, the  characters are at little risk, and the passage of time is  measured in days or longer. This is when you might repair  or craft new equipment, rese |
| 2 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/6` | 0.665680 | **Downtime mode** (page 433) takes place over days. You  might make money, train, or recover, among other things. |
| 3 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/5` | 0.638441 | In **exploration mode**, time is more flexible and the play  more free-form. Minutes, hours, or even days in the game  world pass quickly in the real world, as the characters travel  between star syst |
| 4 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/5` | 0.567712 | **Exploration** **mode** (page 430) takes place over minutes or  hours. You use your travel Speed if you're moving, and you  engage in **exploration** **activities** like Avoiding Notice, Detecting  M |
| 5 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/3` | 0.530729 | Before diving into how to play Starfinder, it's important to  understand the game's three modes of play, which determine  the pace of your adventure and the specific rules you'll use  at a given time. |
| 6 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/4` | 0.514269 | The most intricate of the modes is **encounter mode**. This  is where most of the intense action takes place, and it's  most often used for combat or other high-stakes situations.  The GM typically sw |
| 7 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/1` | 0.503048 | At this point, you have a character and are ready to play Starfinder! Or maybe you're the GM and you're  getting ready to run your first adventure. Either way, this chapter provides the full details f |
| 8 | `PZO22001 Starfinder Player Core 388-405::/page/7/Text/37` | 0.499104 | **Downtime ** **Mode** |
| 9 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/44` | 0.499104 | **Downtime ** **Mode** |
| 10 | `PZO22001 Starfinder Player Core 388-405::/page/5/Text/39` | 0.499104 | **Downtime ** **Mode** |

### Query 6
- Text: Summarize MAKING CHOICES
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/1/SectionHeader/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 388-405::/page/1/SectionHeader/7', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/10', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/9']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/1/SectionHeader/7', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/6', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/8']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 388-405::/page/1/Text/6` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/1/Text/8` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 388-405::/page/1/SectionHeader/7` | 0.931503 | MAKING CHOICES |
| 2 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/10` | 0.487963 | But sometimes what happens as a result of your choices  is less than certain. In those cases, you'll attempt a check, as  described starting on page 392. |
| 3 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/9` | 0.431587 | Often, your choices have no immediate risk or consequences.  If you're exploring a starship and come across an intersection,  the GM asks, "Which way do you go?" You might choose to  take the corridor |
| 4 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/8` | 0.382078 | Throughout the game, the GM describes what's happening in  the world and then asks the players, "So what do you do?"  Exactly what you choose to do, and how the GM responds to  those choices, builds a |
| 5 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/4` | 0.318308 | This game presents three main methods of structuring play.  **Encounter mode** (page 427) is highly structured and is most  often used for combat or stressful situations. Everyone in an  encounter rol |
| 6 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/4` | 0.315115 | If you're ever uncertain how to apply a rule, the GM decides.  Of course, Starfinder is a game, so when adjudicating the  rules, the GM is encouraged to listen to everyone's point of  view and make a |
| 7 | `PZO22001 Starfinder Player Core 388-405::/page/5/Text/2` | 0.307423 | Once you've identified all your various modifiers, bonuses,  and penalties, you move on to the next step. |
| 8 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/8` | 0.304826 | During an encounter, you get 3 actions and 1 reaction per turn  (page 427). Icons indicate whether your abilities take a single  action [one-action], 2 actions [two-actions], 3 actions [three-actions] |
| 9 | `PZO22001 Starfinder Player Core 388-405::/page/5/Text/31` | 0.301475 | **Actions** |
| 10 | `PZO22001 Starfinder Player Core 388-405::/page/15/Text/33` | 0.301475 | **Actions** |

### Query 7
- Text: What is the rule about Throughout the game, the GM describes what's happening in  the world and then asks the players, "So what do you do?"  Exactly what you choose to do, and how the GM responds to  those choices, builds a unique story experience. Every game  is different, because you'll rarely, if ever, make the same  decisions as another group of players. This is true for the GM  as well—two GMs running the exact same adventure will put  different emphasis and flourishes on the content.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/1/Text/8']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 388-405::/page/1/Text/8', 'PZO22001 Starfinder Player Core 388-405::/page/3/Text/4', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/12']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/1/Text/8', 'PZO22001 Starfinder Player Core 388-405::/page/1/SectionHeader/7', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/9']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 388-405::/page/1/SectionHeader/7` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/1/Text/9` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/8` | 1.011616 | Throughout the game, the GM describes what's happening in  the world and then asks the players, "So what do you do?"  Exactly what you choose to do, and how the GM responds to  those choices, builds a |
| 2 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/4` | 0.669848 | If you're ever uncertain how to apply a rule, the GM decides.  Of course, Starfinder is a game, so when adjudicating the  rules, the GM is encouraged to listen to everyone's point of  view and make a |
| 3 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/12` | 0.652780 | Your group will likely talk about what types of content you  want in your game before your campaign begins. The following  is a set of basic assumptions that works for many groups. The  GM can find mo |
| 4 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/9` | 0.609484 | Often, your choices have no immediate risk or consequences.  If you're exploring a starship and come across an intersection,  the GM asks, "Which way do you go?" You might choose to  take the corridor |
| 5 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/5` | 0.581520 | In **exploration mode**, time is more flexible and the play  more free-form. Minutes, hours, or even days in the game  world pass quickly in the real world, as the characters travel  between star syst |
| 6 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/3` | 0.577547 | Before diving into how to play Starfinder, it's important to  understand the game's three modes of play, which determine  the pace of your adventure and the specific rules you'll use  at a given time. |
| 7 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/4` | 0.551250 | The most intricate of the modes is **encounter mode**. This  is where most of the intense action takes place, and it's  most often used for combat or other high-stakes situations.  The GM typically sw |
| 8 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/1` | 0.545541 | At this point, you have a character and are ready to play Starfinder! Or maybe you're the GM and you're  getting ready to run your first adventure. Either way, this chapter provides the full details f |
| 9 | `PZO22001 Starfinder Player Core 388-405::/page/17/Text/9` | 0.541047 | Your character's deed might invoke a lesson learned  in a past adventure, could be spurred by a determination  to save someone else, or might depend on an item that  ended up on their person due to a |
| 10 | `PZO22001 Starfinder Player Core 388-405::/page/9/Text/15` | 0.535546 | The GM can choose to make any check secret, even  if it's not usually rolled secretly. Conversely, the GM  can let you roll any check yourself, even if that check  would usually be secret. Some groups |

### Query 8
- Text: What is the rule about Often, your choices have no immediate risk or consequences.  If you're exploring a starship and come across an intersection,  the GM asks, "Which way do you go?" You might choose to  take the corridor to the right or left, or climb through the  maintenance shaft overhead. Once your choice is made, the  GM tells you what happens next. Down the line, that choice  may impact what you encounter later in the game, but in many  cases nothing dangerous happens immediately.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/1/Text/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 388-405::/page/1/Text/9', 'PZO22001 Starfinder Player Core 388-405::/page/3/Text/4', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/8']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/1/Text/9', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/8', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/10']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 388-405::/page/1/Text/8` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/1/Text/10` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/9` | 1.015433 | Often, your choices have no immediate risk or consequences.  If you're exploring a starship and come across an intersection,  the GM asks, "Which way do you go?" You might choose to  take the corridor |
| 2 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/4` | 0.662612 | If you're ever uncertain how to apply a rule, the GM decides.  Of course, Starfinder is a game, so when adjudicating the  rules, the GM is encouraged to listen to everyone's point of  view and make a |
| 3 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/8` | 0.631972 | Throughout the game, the GM describes what's happening in  the world and then asks the players, "So what do you do?"  Exactly what you choose to do, and how the GM responds to  those choices, builds a |
| 4 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/3` | 0.560380 | Before diving into how to play Starfinder, it's important to  understand the game's three modes of play, which determine  the pace of your adventure and the specific rules you'll use  at a given time. |
| 5 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/5` | 0.548524 | In **exploration mode**, time is more flexible and the play  more free-form. Minutes, hours, or even days in the game  world pass quickly in the real world, as the characters travel  between star syst |
| 6 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/1` | 0.534626 | At this point, you have a character and are ready to play Starfinder! Or maybe you're the GM and you're  getting ready to run your first adventure. Either way, this chapter provides the full details f |
| 7 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/6` | 0.520302 | A core principle of Starfinder is that specific rules override  general ones. If two rules conflict, the more specific  one takes precedence. If there's still ambiguity, the GM  determines which rule |
| 8 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/10` | 0.503864 | But sometimes what happens as a result of your choices  is less than certain. In those cases, you'll attempt a check, as  described starting on page 392. |
| 9 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/2` | 0.501851 | Starfinder has many specific rules, but you'll also want to keep these general guidelines in mind when playing. |
| 10 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/4` | 0.498032 | The most intricate of the modes is **encounter mode**. This  is where most of the intense action takes place, and it's  most often used for combat or other high-stakes situations.  The GM typically sw |

### Query 9
- Text: What is the rule about But sometimes what happens as a result of your choices  is less than certain. In those cases, you'll attempt a check, as  described starting on page 392.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/1/Text/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 388-405::/page/1/Text/10', 'PZO22001 Starfinder Player Core 388-405::/page/5/Text/6', 'PZO22001 Starfinder Player Core 388-405::/page/5/Text/11']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/1/Text/10', 'PZO22001 Starfinder Player Core 388-405::/page/1/SectionHeader/11', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/9']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 388-405::/page/1/SectionHeader/11` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/1/Text/9` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/10` | 0.959640 | But sometimes what happens as a result of your choices  is less than certain. In those cases, you'll attempt a check, as  described starting on page 392. |
| 2 | `PZO22001 Starfinder Player Core 388-405::/page/5/Text/6` | 0.618655 | Whenever you attempt a check, you compare your result  against the **Difficulty Class (DC)** of the check. Your check  succeeds if it's equal to or greater than the DC. If you roll  anything less than |
| 3 | `PZO22001 Starfinder Player Core 388-405::/page/5/Text/11` | 0.614418 | Many times, it's important to determine not only if you |
| 4 | `PZO22001 Starfinder Player Core 388-405::/page/9/Text/11` | 0.561048 | When the likelihood something will happen or fail to  happen is based purely on chance, you'll attempt a flat  check. A flat check never includes any modifiers, bonuses,  or penalties—you just roll a |
| 5 | `PZO22001 Starfinder Player Core 388-405::/page/5/Text/7` | 0.557648 | Sometimes you'll know the DC and make the comparison  yourself. Other times, you might not know the DC right away.  Unlocking a looted comm unit would require a Computers check,  but it doesn't have a |
| 6 | `PZO22001 Starfinder Player Core 388-405::/page/4/Text/2` | 0.557060 | When success isn't certain—whether you're firing a laser pistol at a sentry robot, attempting to balance  on a moving conveyor belt, or straining to remember the name of the ambassador's pet squox at |
| 7 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/14` | 0.550163 | Sometimes a rule could be interpreted multiple ways. If one  version is too good to be true, it probably is. If a rule seems  to have wording with problematic repercussions or doesn't  work as intende |
| 8 | `PZO22001 Starfinder Player Core 388-405::/page/5/Text/16` | 0.545064 | succeed or fail, but also how spectacularly you succeed or  fail. Exceptional results—either good or bad—can cause you to  critically succeed or critically fail at a check. |
| 9 | `PZO22001 Starfinder Player Core 388-405::/page/9/Text/14` | 0.523735 | Sometimes you as the player shouldn't know the exact  result and effect of a check. In these situations, the rules  (or the GM) will call for a secret check. The secret trait  appears on anything that |
| 10 | `PZO22001 Starfinder Player Core 388-405::/page/5/Text/17` | 0.521725 | You **critically succeed** when the check's result meets or  exceeds the DC by 10 or more. If the check is an attack roll, this  is also known as a critical hit. You can also **critically fail** a che |

### Query 10
- Text: Summarize THE STARFINDER  BASELINE
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/1/SectionHeader/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 388-405::/page/1/SectionHeader/11', 'PZO22001 Starfinder Player Core 388-405::/page/3/Text/2', 'PZO22001 Starfinder Player Core 388-405::/page/9/Text/7']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/1/SectionHeader/11', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/12', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/10']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 388-405::/page/1/Text/12` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/1/Text/10` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 388-405::/page/1/SectionHeader/11` | 1.015149 | THE STARFINDER  BASELINE |
| 2 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/2` | 0.558466 | Starfinder has many specific rules, but you'll also want to keep these general guidelines in mind when playing. |
| 3 | `PZO22001 Starfinder Player Core 388-405::/page/9/Text/7` | 0.540177 | Starfinder has a variety of skills for many different situations,  from Athletics to Computers to Piloting. Each grants you a  set of related actions that rely on you rolling a skill check.  Each skil |
| 4 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/1` | 0.472734 | At this point, you have a character and are ready to play Starfinder! Or maybe you're the GM and you're  getting ready to run your first adventure. Either way, this chapter provides the full details f |
| 5 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/3` | 0.450433 | Before diving into how to play Starfinder, it's important to  understand the game's three modes of play, which determine  the pace of your adventure and the specific rules you'll use  at a given time. |
| 6 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/6` | 0.443479 | A core principle of Starfinder is that specific rules override  general ones. If two rules conflict, the more specific  one takes precedence. If there's still ambiguity, the GM  determines which rule |
| 7 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/4` | 0.426544 | If you're ever uncertain how to apply a rule, the GM decides.  Of course, Starfinder is a game, so when adjudicating the  rules, the GM is encouraged to listen to everyone's point of  view and make a |
| 8 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/28` | 0.281439 | Your **Perception **modifier (page 396) indicates how good you  are at noticing things around you. You typically use the **Seek** basic action (page 409) to find physical things or the **Sense ** **Mo |
| 9 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/26` | 0.269948 | Skill checks are required for all sorts of other tasks related  to adventuring and life in general. Most of their rules are  in Chapter 4 (page 183). You'll find the rules for **calculating ** **skill |
| 10 | `PZO22001 Starfinder Player Core 388-405::/page/2/SectionHeader/1` | 0.264185 | RULES OVERVIEW |

### Query 11
- Text: Summarize Your group will likely talk about what types of content you  want in your game before your campaign begins. The following  is a set of basic assumptions that works for many groups. The  GM can find more guidance in *GM Core*.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/1/Text/12']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 388-405::/page/1/Text/12', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/8', 'PZO22001 Starfinder Player Core 388-405::/page/3/Text/4']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/1/Text/12', 'PZO22001 Starfinder Player Core 388-405::/page/1/ListItem/13', 'PZO22001 Starfinder Player Core 388-405::/page/1/SectionHeader/11']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 388-405::/page/1/ListItem/13` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/1/SectionHeader/11` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/12` | 1.043567 | Your group will likely talk about what types of content you  want in your game before your campaign begins. The following  is a set of basic assumptions that works for many groups. The  GM can find mo |
| 2 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/8` | 0.642008 | Throughout the game, the GM describes what's happening in  the world and then asks the players, "So what do you do?"  Exactly what you choose to do, and how the GM responds to  those choices, builds a |
| 3 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/4` | 0.567285 | If you're ever uncertain how to apply a rule, the GM decides.  Of course, Starfinder is a game, so when adjudicating the  rules, the GM is encouraged to listen to everyone's point of  view and make a |
| 4 | `PZO22001 Starfinder Player Core 388-405::/page/17/Text/9` | 0.521413 | Your character's deed might invoke a lesson learned  in a past adventure, could be spurred by a determination  to save someone else, or might depend on an item that  ended up on their person due to a |
| 5 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/1` | 0.515935 | At this point, you have a character and are ready to play Starfinder! Or maybe you're the GM and you're  getting ready to run your first adventure. Either way, this chapter provides the full details f |
| 6 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/3` | 0.509366 | Before diving into how to play Starfinder, it's important to  understand the game's three modes of play, which determine  the pace of your adventure and the specific rules you'll use  at a given time. |
| 7 | `PZO22001 Starfinder Player Core 388-405::/page/1/ListItem/14` | 0.480824 | Romantic and sexual relationships can happen in the  game, but players should avoid being overly suggestive.  Sex happens "off-screen." Players should consent before  roleplaying a relationship and ha |
| 8 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/5` | 0.473838 | In **exploration mode**, time is more flexible and the play  more free-form. Minutes, hours, or even days in the game  world pass quickly in the real world, as the characters travel  between star syst |
| 9 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/9` | 0.465981 | Often, your choices have no immediate risk or consequences.  If you're exploring a starship and come across an intersection,  the GM asks, "Which way do you go?" You might choose to  take the corridor |
| 10 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/4` | 0.454581 | This game presents three main methods of structuring play.  **Encounter mode** (page 427) is highly structured and is most  often used for combat or stressful situations. Everyone in an  encounter rol |

### Query 12
- Text: Summarize Avoid excessive descriptions of gore and cruelty.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/1/ListItem/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 388-405::/page/1/ListItem/13', 'PZO22001 Starfinder Player Core 388-405::/page/1/ListItem/16', 'PZO22001 Starfinder Player Core 388-405::/page/1/ListItem/14']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/1/ListItem/13', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/12', 'PZO22001 Starfinder Player Core 388-405::/page/1/ListItem/14']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 388-405::/page/1/Text/12` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/1/ListItem/14` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 388-405::/page/1/ListItem/13` | 1.019678 | Avoid excessive descriptions of gore and cruelty. |
| 2 | `PZO22001 Starfinder Player Core 388-405::/page/1/ListItem/16` | 0.492094 | Torture, rape, nonconsensual sexual contact or threats |
| 3 | `PZO22001 Starfinder Player Core 388-405::/page/1/ListItem/14` | 0.474210 | Romantic and sexual relationships can happen in the  game, but players should avoid being overly suggestive.  Sex happens "off-screen." Players should consent before  roleplaying a relationship and ha |
| 4 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/15` | 0.386147 | Player characters shouldn't perform the following acts: |
| 5 | `PZO22001 Starfinder Player Core 388-405::/page/17/Text/8` | 0.357583 | Because spending Hero Points reflects heroic deeds or  tasks that surpass normal expectations, if you spend a  Hero Point, you should describe the deed or task your  character accomplishes with it to |
| 6 | `PZO22001 Starfinder Player Core 388-405::/page/14/Text/2` | 0.356638 | For adventurers, injury and death lurk around every corner. |
| 7 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/14` | 0.354205 | Sometimes a rule could be interpreted multiple ways. If one  version is too good to be true, it probably is. If a rule seems  to have wording with problematic repercussions or doesn't  work as intende |
| 8 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/12` | 0.352036 | Your group will likely talk about what types of content you  want in your game before your campaign begins. The following  is a set of basic assumptions that works for many groups. The  GM can find mo |
| 9 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/20` | 0.346518 | Villains might engage in such acts "off-screen," but many  groups choose to not have villains engage in these activities. |
| 10 | `PZO22001 Starfinder Player Core 388-405::/page/16/Text/16` | 0.343997 | Your life is ebbing away, bringing you ever closer to  death. Some powerful spells and evil creatures can  inflict the doomed condition on you. Doomed always  includes a value. The maximum dying value |

### Query 13
- Text: Summarize Romantic and sexual relationships can happen in the  game, but players should avoid being overly suggestive.  Sex happens "off-screen." Players should consent before  roleplaying a relationship and have a comfortable out.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/1/ListItem/14']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 388-405::/page/1/ListItem/14', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/15', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/20']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/1/ListItem/14', 'PZO22001 Starfinder Player Core 388-405::/page/1/ListItem/13', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/15']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 388-405::/page/1/ListItem/13` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/1/Text/15` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 388-405::/page/1/ListItem/14` | 1.043905 | Romantic and sexual relationships can happen in the  game, but players should avoid being overly suggestive.  Sex happens "off-screen." Players should consent before  roleplaying a relationship and ha |
| 2 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/15` | 0.547237 | Player characters shouldn't perform the following acts: |
| 3 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/20` | 0.542560 | Villains might engage in such acts "off-screen," but many  groups choose to not have villains engage in these activities. |
| 4 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/12` | 0.492657 | Your group will likely talk about what types of content you  want in your game before your campaign begins. The following  is a set of basic assumptions that works for many groups. The  GM can find mo |
| 5 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/5` | 0.490305 | In **exploration mode**, time is more flexible and the play  more free-form. Minutes, hours, or even days in the game  world pass quickly in the real world, as the characters travel  between star syst |
| 6 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/2` | 0.472664 | Starfinder has many specific rules, but you'll also want to keep these general guidelines in mind when playing. |
| 7 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/4` | 0.456285 | If you're ever uncertain how to apply a rule, the GM decides.  Of course, Starfinder is a game, so when adjudicating the  rules, the GM is encouraged to listen to everyone's point of  view and make a |
| 8 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/4` | 0.456282 | The most intricate of the modes is **encounter mode**. This  is where most of the intense action takes place, and it's  most often used for combat or other high-stakes situations.  The GM typically sw |
| 9 | `PZO22001 Starfinder Player Core 388-405::/page/11/Text/22` | 0.447802 | **GAME** **Rules Overview** |
| 10 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/9` | 0.445691 | Often, your choices have no immediate risk or consequences.  If you're exploring a starship and come across an intersection,  the GM asks, "Which way do you go?" You might choose to  take the corridor |

### Query 14
- Text: What is the rule about Player characters shouldn't perform the following acts:?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/1/Text/15']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 388-405::/page/1/Text/15', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/20', 'PZO22001 Starfinder Player Core 388-405::/page/1/ListItem/14']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/1/Text/15', 'PZO22001 Starfinder Player Core 388-405::/page/1/ListItem/16', 'PZO22001 Starfinder Player Core 388-405::/page/1/ListItem/14']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 388-405::/page/1/ListItem/16` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/1/ListItem/14` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/15` | 0.958093 | Player characters shouldn't perform the following acts: |
| 2 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/20` | 0.574032 | Villains might engage in such acts "off-screen," but many  groups choose to not have villains engage in these activities. |
| 3 | `PZO22001 Starfinder Player Core 388-405::/page/1/ListItem/14` | 0.571144 | Romantic and sexual relationships can happen in the  game, but players should avoid being overly suggestive.  Sex happens "off-screen." Players should consent before  roleplaying a relationship and ha |
| 4 | `PZO22001 Starfinder Player Core 388-405::/page/14/Text/19` | 0.524421 | 0 Hit Points. Instead, they are knocked out and are at risk  of death. The GM might determine that villains, powerful  monsters, special NPCs, and enemies with special abilities  that are likely to br |
| 5 | `PZO22001 Starfinder Player Core 388-405::/page/9/Text/16` | 0.471989 | unfavorable situations might give you a circumstance penalty  to your skill check, while harmful spells, magic, or conditions  might also impose a status penalty. Using shoddy or makeshift  tools migh |
| 6 | `PZO22001 Starfinder Player Core 388-405::/page/17/Text/8` | 0.471777 | Because spending Hero Points reflects heroic deeds or  tasks that surpass normal expectations, if you spend a  Hero Point, you should describe the deed or task your  character accomplishes with it to |
| 7 | `PZO22001 Starfinder Player Core 388-405::/page/14/Text/20` | 0.466114 | As a player character, when you're reduced to 0 Hit Points,  you're knocked out with the following effects: |
| 8 | `PZO22001 Starfinder Player Core 388-405::/page/14/Text/18` | 0.462557 | Player characters, their companions,  and other significant characters and  creatures don't automatically die when they reach |
| 9 | `PZO22001 Starfinder Player Core 388-405::/page/9/Text/15` | 0.459696 | The GM can choose to make any check secret, even  if it's not usually rolled secretly. Conversely, the GM  can let you roll any check yourself, even if that check  would usually be secret. Some groups |
| 10 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/6` | 0.459117 | A core principle of Starfinder is that specific rules override  general ones. If two rules conflict, the more specific  one takes precedence. If there's still ambiguity, the GM  determines which rule |

### Query 15
- Text: What is the rule about Torture, rape, nonconsensual sexual contact or threats?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/1/ListItem/16']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 388-405::/page/1/ListItem/16', 'PZO22001 Starfinder Player Core 388-405::/page/1/ListItem/17', 'PZO22001 Starfinder Player Core 388-405::/page/2/SectionHeader/1']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/1/ListItem/16', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/15', 'PZO22001 Starfinder Player Core 388-405::/page/1/ListItem/17']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 388-405::/page/1/Text/15` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/1/ListItem/17` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 388-405::/page/1/ListItem/16` | 0.904434 | Torture, rape, nonconsensual sexual contact or threats |
| 2 | `PZO22001 Starfinder Player Core 388-405::/page/1/ListItem/17` | 0.496373 | Harm to children, including sexual abuse |
| 3 | `PZO22001 Starfinder Player Core 388-405::/page/2/SectionHeader/1` | 0.471026 | RULES OVERVIEW |
| 4 | `PZO22001 Starfinder Player Core 388-405::/page/1/ListItem/14` | 0.426712 | Romantic and sexual relationships can happen in the  game, but players should avoid being overly suggestive.  Sex happens "off-screen." Players should consent before  roleplaying a relationship and ha |
| 5 | `PZO22001 Starfinder Player Core 388-405::/page/1/ListItem/13` | 0.423047 | Avoid excessive descriptions of gore and cruelty. |
| 6 | `PZO22001 Starfinder Player Core 388-405::/page/15/Text/26` | 0.399090 | **Rules Overview** |
| 7 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/40` | 0.399090 | **Rules Overview** |
| 8 | `PZO22001 Starfinder Player Core 388-405::/page/7/Text/21` | 0.399090 | **Rules Overview** |
| 9 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/29` | 0.399090 | **Rules Overview** |
| 10 | `PZO22001 Starfinder Player Core 388-405::/page/13/Text/33` | 0.399090 | **Rules Overview** |

### Query 16
- Text: Summarize Harm to children, including sexual abuse
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/1/ListItem/17']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 388-405::/page/1/ListItem/17', 'PZO22001 Starfinder Player Core 388-405::/page/1/ListItem/16', 'PZO22001 Starfinder Player Core 388-405::/page/10/Text/2']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/1/ListItem/17', 'PZO22001 Starfinder Player Core 388-405::/page/1/ListItem/16', 'PZO22001 Starfinder Player Core 388-405::/page/1/ListItem/18']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 388-405::/page/1/ListItem/16` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/1/ListItem/18` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 388-405::/page/1/ListItem/17` | 0.987789 | Harm to children, including sexual abuse |
| 2 | `PZO22001 Starfinder Player Core 388-405::/page/1/ListItem/16` | 0.573342 | Torture, rape, nonconsensual sexual contact or threats |
| 3 | `PZO22001 Starfinder Player Core 388-405::/page/10/Text/2` | 0.477509 | Strikes, spells, hazards, and all number of other dangers can deal damage, which can kill creatures and  destroy objects. |
| 4 | `PZO22001 Starfinder Player Core 388-405::/page/13/SectionHeader/13` | 0.409100 | **Mental Damage** |
| 5 | `PZO22001 Starfinder Player Core 388-405::/page/11/Text/7` | 0.388871 | or when the target is somehow vulnerable. The damage types  are described on page 401. |
| 6 | `PZO22001 Starfinder Player Core 388-405::/page/13/SectionHeader/3` | 0.369132 | **Physical Damage** |
| 7 | `PZO22001 Starfinder Player Core 388-405::/page/10/ListItem/7` | 0.360409 | 2. Determine the **damage type**. |
| 8 | `PZO22001 Starfinder Player Core 388-405::/page/13/Text/16` | 0.356872 | Venoms, toxins, radiation, and the like can deal **poison** damage, which affects creatures by way of contact,  ingestion, inhalation, or injury. In addition to coming from  monster attacks, items, an |
| 9 | `PZO22001 Starfinder Player Core 388-405::/page/1/ListItem/13` | 0.354753 | Avoid excessive descriptions of gore and cruelty. |
| 10 | `PZO22001 Starfinder Player Core 388-405::/page/10/ListItem/8` | 0.353049 | 3. Apply **immunities**, **weaknesses**, and **resistances **the  subject has to the damage. |

### Query 17
- Text: Summarize Enslaving people or profiting from slavery
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/1/ListItem/18']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 388-405::/page/1/ListItem/18', 'PZO22001 Starfinder Player Core 388-405::/page/1/ListItem/13', 'PZO22001 Starfinder Player Core 388-405::/page/17/Text/9']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/1/ListItem/18', 'PZO22001 Starfinder Player Core 388-405::/page/1/ListItem/19', 'PZO22001 Starfinder Player Core 388-405::/page/1/ListItem/17']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 388-405::/page/1/ListItem/19` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/1/ListItem/17` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 388-405::/page/1/ListItem/18` | 1.014936 | Enslaving people or profiting from slavery |
| 2 | `PZO22001 Starfinder Player Core 388-405::/page/1/ListItem/13` | 0.334534 | Avoid excessive descriptions of gore and cruelty. |
| 3 | `PZO22001 Starfinder Player Core 388-405::/page/17/Text/9` | 0.332363 | Your character's deed might invoke a lesson learned  in a past adventure, could be spurred by a determination  to save someone else, or might depend on an item that  ended up on their person due to a |
| 4 | `PZO22001 Starfinder Player Core 388-405::/page/17/Text/8` | 0.294126 | Because spending Hero Points reflects heroic deeds or  tasks that surpass normal expectations, if you spend a  Hero Point, you should describe the deed or task your  character accomplishes with it to |
| 5 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/15` | 0.286575 | **Related:** Flat checks and secret checks (sidebar on page  397), fortune and misfortune (sidebar on page 393) |
| 6 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/20` | 0.276081 | Villains might engage in such acts "off-screen," but many  groups choose to not have villains engage in these activities. |
| 7 | `PZO22001 Starfinder Player Core 388-405::/page/14/ListItem/22` | 0.275209 | **Gain the dying 1 condition. **If the effect that knocked you  out was a critical success from the attacker or the result  of your critical failure, you gain the dying 2 condition  instead. If you ha |
| 8 | `PZO22001 Starfinder Player Core 388-405::/page/1/ListItem/16` | 0.274376 | Torture, rape, nonconsensual sexual contact or threats |
| 9 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/6` | 0.271097 | **Downtime mode** (page 433) takes place over days. You  might make money, train, or recover, among other things. |
| 10 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/23` | 0.269235 | (page 394). For one that causes its subject to attempt a  saving throw, you'll need your **spell DC** (page 395). |

### Query 18
- Text: Summarize Reprehensible uses of mind-control magic
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/1/ListItem/19']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 388-405::/page/1/ListItem/19', 'PZO22001 Starfinder Player Core 388-405::/page/13/Text/14', 'PZO22001 Starfinder Player Core 388-405::/page/4/Text/24']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/1/ListItem/19', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/20', 'PZO22001 Starfinder Player Core 388-405::/page/1/ListItem/18']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 388-405::/page/1/Text/20` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/1/ListItem/18` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 388-405::/page/1/ListItem/19` | 1.007842 | Reprehensible uses of mind-control magic |
| 2 | `PZO22001 Starfinder Player Core 388-405::/page/13/Text/14` | 0.466593 | Sometimes an effect can target the mind with enough  psychic force to actually deal damage to the creature. When  it does, it deals **mental** damage. Mindless creatures and  those with only programme |
| 3 | `PZO22001 Starfinder Player Core 388-405::/page/4/Text/24` | 0.453094 | **Status bonuses** typically come from spells, other magical  effects, or something applying a helpful, often temporary,  condition to you. For instance, the *akashic download* spell  grants a +1 stat |
| 4 | `PZO22001 Starfinder Player Core 388-405::/page/5/Text/22` | 0.409598 | Fortune and misfortune effects can alter how you roll  your dice. These abilities might allow you to reroll a  failed roll, force you to reroll a successful roll, allow  you to roll twice and use the |
| 5 | `PZO22001 Starfinder Player Core 388-405::/page/13/Text/9` | 0.398180 | Powerful and pure magical energy can manifest itself  as **force** damage. Few things can resist this type of  damage—not even incorporeal creatures such as ghosts. |
| 6 | `PZO22001 Starfinder Player Core 388-405::/page/16/ListItem/11` | 0.394831 | Loud noise is being made around you—though this isn't  automatic. At the start of your turn, you automatically  attempt a Perception check against the noise's DC (or  the lowest DC if there's more tha |
| 7 | `PZO22001 Starfinder Player Core 388-405::/page/15/Text/13` | 0.390238 | After you die, you can't act or regain actions, can't be affected  by spells that target creatures (unless they specifically target  dead creatures), and for all other purposes, you're an object.  Whe |
| 8 | `PZO22001 Starfinder Player Core 388-405::/page/4/Text/2` | 0.374462 | When success isn't certain—whether you're firing a laser pistol at a sentry robot, attempting to balance  on a moving conveyor belt, or straining to remember the name of the ambassador's pet squox at |
| 9 | `PZO22001 Starfinder Player Core 388-405::/page/9/Text/14` | 0.368352 | Sometimes you as the player shouldn't know the exact  result and effect of a check. In these situations, the rules  (or the GM) will call for a secret check. The secret trait  appears on anything that |
| 10 | `PZO22001 Starfinder Player Core 388-405::/page/8/Text/14` | 0.368325 | **Will **saving throws measure how well you can resist  attacks to your mind and spirit. They use your Wisdom  modifier and are calculated as shown in the formula below. |

### Query 19
- Text: What is the rule about Villains might engage in such acts "off-screen," but many  groups choose to not have villains engage in these activities.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/1/Text/20']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 388-405::/page/1/Text/20', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/15', 'PZO22001 Starfinder Player Core 388-405::/page/14/Text/19']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/1/Text/20', 'PZO22001 Starfinder Player Core 388-405::/page/1/ListItem/19', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/22']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 388-405::/page/1/ListItem/19` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/1/Text/22` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/20` | 0.984897 | Villains might engage in such acts "off-screen," but many  groups choose to not have villains engage in these activities. |
| 2 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/15` | 0.576205 | Player characters shouldn't perform the following acts: |
| 3 | `PZO22001 Starfinder Player Core 388-405::/page/14/Text/19` | 0.544081 | 0 Hit Points. Instead, they are knocked out and are at risk  of death. The GM might determine that villains, powerful  monsters, special NPCs, and enemies with special abilities  that are likely to br |
| 4 | `PZO22001 Starfinder Player Core 388-405::/page/1/ListItem/14` | 0.495840 | Romantic and sexual relationships can happen in the  game, but players should avoid being overly suggestive.  Sex happens "off-screen." Players should consent before  roleplaying a relationship and ha |
| 5 | `PZO22001 Starfinder Player Core 388-405::/page/9/Text/15` | 0.437091 | The GM can choose to make any check secret, even  if it's not usually rolled secretly. Conversely, the GM  can let you roll any check yourself, even if that check  would usually be secret. Some groups |
| 6 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/6` | 0.414709 | A core principle of Starfinder is that specific rules override  general ones. If two rules conflict, the more specific  one takes precedence. If there's still ambiguity, the GM  determines which rule |
| 7 | `PZO22001 Starfinder Player Core 388-405::/page/11/Text/13` | 0.406389 | You can make a nonlethal attack to knock someone out  instead of killing them (see Knocked Out and Dying on pages  402–403). Weapons with the nonlethal trait (including fists) do  this automatically. |
| 8 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/4` | 0.405252 | The most intricate of the modes is **encounter mode**. This  is where most of the intense action takes place, and it's  most often used for combat or other high-stakes situations.  The GM typically sw |
| 9 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/12` | 0.401543 | Your group will likely talk about what types of content you  want in your game before your campaign begins. The following  is a set of basic assumptions that works for many groups. The  GM can find mo |
| 10 | `PZO22001 Starfinder Player Core 388-405::/page/17/Text/4` | 0.393996 | You can spend your Hero Points in one of two ways.  Neither of these is an action, and you can spend Hero Points  even if you aren't able to act. You can spend a Hero Point on  behalf of your familiar |

### Query 20
- Text: Summarize **INTRODUCTION**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/1/Text/22']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 388-405::/page/1/Text/22', 'PZO22001 Starfinder Player Core 388-405::/page/15/Text/19', 'PZO22001 Starfinder Player Core 388-405::/page/3/Text/32']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/1/Text/22', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/23', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/20']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 388-405::/page/1/Text/23` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/1/Text/20` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/22` | 0.880541 | **INTRODUCTION** |
| 2 | `PZO22001 Starfinder Player Core 388-405::/page/15/Text/19` | 0.880541 | **INTRODUCTION** |
| 3 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/32` | 0.880541 | **INTRODUCTION** |
| 4 | `PZO22001 Starfinder Player Core 388-405::/page/7/Text/14` | 0.838541 | **INTRODUCTION** |
| 5 | `PZO22001 Starfinder Player Core 388-405::/page/13/Text/25` | 0.838541 | **INTRODUCTION** |
| 6 | `PZO22001 Starfinder Player Core 388-405::/page/9/Text/19` | 0.838541 | **INTRODUCTION** |
| 7 | `PZO22001 Starfinder Player Core 388-405::/page/11/Text/15` | 0.838541 | **INTRODUCTION** |
| 8 | `PZO22001 Starfinder Player Core 388-405::/page/17/Text/11` | 0.838541 | **INTRODUCTION** |
| 9 | `PZO22001 Starfinder Player Core 388-405::/page/9/Text/27` | 0.457803 | **Rules Overview** |
| 10 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/40` | 0.457803 | **Rules Overview** |

### Query 21
- Text: What is the rule about **ANCESTRIES & ** **BACKGROUNDS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/1/Text/23']
- Expected found: `True`
- Expected rank: `6`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 388-405::/page/17/Text/12', 'PZO22001 Starfinder Player Core 388-405::/page/3/Text/33', 'PZO22001 Starfinder Player Core 388-405::/page/15/Text/20']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/1/Text/23', 'PZO22001 Starfinder Player Core 388-405::/page/15/Text/20', 'PZO22001 Starfinder Player Core 388-405::/page/9/Text/20', 'PZO22001 Starfinder Player Core 388-405::/page/7/Text/15', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/24', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/22', 'PZO22001 Starfinder Player Core 388-405::/page/13/Text/26', 'PZO22001 Starfinder Player Core 388-405::/page/11/Text/16', 'PZO22001 Starfinder Player Core 388-405::/page/3/Text/33', 'PZO22001 Starfinder Player Core 388-405::/page/17/Text/12']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 388-405::/page/15/Text/20` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/9/Text/20` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/7/Text/15` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/1/Text/24` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/1/Text/22` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/13/Text/26` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/11/Text/16` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/3/Text/33` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/17/Text/12` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 388-405::/page/17/Text/12` | 0.920820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 2 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/33` | 0.920820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 3 | `PZO22001 Starfinder Player Core 388-405::/page/15/Text/20` | 0.920820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 4 | `PZO22001 Starfinder Player Core 388-405::/page/7/Text/15` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 5 | `PZO22001 Starfinder Player Core 388-405::/page/9/Text/20` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 6 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/23` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 7 | `PZO22001 Starfinder Player Core 388-405::/page/13/Text/26` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 8 | `PZO22001 Starfinder Player Core 388-405::/page/11/Text/16` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 9 | `PZO22001 Starfinder Player Core 388-405::/page/5/Text/53` | 0.560657 | **INTRODUCTION** **ANCESTRIES & ** **BACKGROUNDS** **CLASSES** **SKILLS** **FEATS** **EQUIPMENT** **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 388-405::/page/15/Text/26` | 0.476883 | **Rules Overview** |

### Query 22
- Text: Summarize **CLASSES**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/1/Text/24']
- Expected found: `True`
- Expected rank: `6`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 388-405::/page/17/Text/13', 'PZO22001 Starfinder Player Core 388-405::/page/15/Text/21', 'PZO22001 Starfinder Player Core 388-405::/page/3/Text/34']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/1/Text/24', 'PZO22001 Starfinder Player Core 388-405::/page/11/Text/17', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/25', 'PZO22001 Starfinder Player Core 388-405::/page/17/Text/13', 'PZO22001 Starfinder Player Core 388-405::/page/15/Text/21', 'PZO22001 Starfinder Player Core 388-405::/page/9/Text/21', 'PZO22001 Starfinder Player Core 388-405::/page/13/Text/27', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/23', 'PZO22001 Starfinder Player Core 388-405::/page/7/Text/16', 'PZO22001 Starfinder Player Core 388-405::/page/3/Text/34']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 388-405::/page/11/Text/17` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/1/Text/25` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/17/Text/13` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/15/Text/21` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/9/Text/21` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/13/Text/27` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/1/Text/23` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/7/Text/16` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/3/Text/34` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 388-405::/page/17/Text/13` | 0.940061 | **CLASSES** |
| 2 | `PZO22001 Starfinder Player Core 388-405::/page/15/Text/21` | 0.940061 | **CLASSES** |
| 3 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/34` | 0.940061 | **CLASSES** |
| 4 | `PZO22001 Starfinder Player Core 388-405::/page/11/Text/17` | 0.910061 | **CLASSES** |
| 5 | `PZO22001 Starfinder Player Core 388-405::/page/7/Text/16` | 0.910061 | **CLASSES** |
| 6 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/24` | 0.910061 | **CLASSES** |
| 7 | `PZO22001 Starfinder Player Core 388-405::/page/9/Text/21` | 0.910061 | **CLASSES** |
| 8 | `PZO22001 Starfinder Player Core 388-405::/page/13/Text/27` | 0.910061 | **CLASSES** |
| 9 | `PZO22001 Starfinder Player Core 388-405::/page/5/Text/53` | 0.521344 | **INTRODUCTION** **ANCESTRIES & ** **BACKGROUNDS** **CLASSES** **SKILLS** **FEATS** **EQUIPMENT** **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 388-405::/page/7/SectionHeader/10` | 0.467480 | ARMOR CLASS |

### Query 23
- Text: What is the rule about **SKILLS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/1/Text/25']
- Expected found: `True`
- Expected rank: `5`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 388-405::/page/17/Text/14', 'PZO22001 Starfinder Player Core 388-405::/page/13/Text/28', 'PZO22001 Starfinder Player Core 388-405::/page/15/Text/22']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/1/Text/25', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/26', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/24']
- Expanded expected found: `True`
- Expanded expected rank: `5`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 388-405::/page/1/Text/26` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/1/Text/24` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 388-405::/page/17/Text/14` | 0.864442 | **SKILLS** |
| 2 | `PZO22001 Starfinder Player Core 388-405::/page/13/Text/28` | 0.864442 | **SKILLS** |
| 3 | `PZO22001 Starfinder Player Core 388-405::/page/15/Text/22` | 0.864442 | **SKILLS** |
| 4 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/35` | 0.822442 | **SKILLS** |
| 5 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/25` | 0.822442 | **SKILLS** |
| 6 | `PZO22001 Starfinder Player Core 388-405::/page/11/Text/18` | 0.822442 | **SKILLS** |
| 7 | `PZO22001 Starfinder Player Core 388-405::/page/9/Text/22` | 0.822442 | **SKILLS** |
| 8 | `PZO22001 Starfinder Player Core 388-405::/page/7/Text/17` | 0.822442 | **SKILLS** |
| 9 | `PZO22001 Starfinder Player Core 388-405::/page/3/SectionHeader/25` | 0.712079 | SKILLS |
| 10 | `PZO22001 Starfinder Player Core 388-405::/page/9/SectionHeader/6` | 0.572507 | SKILL CHECKS |

### Query 24
- Text: What is the rule about **FEATS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/1/Text/26']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 388-405::/page/3/Text/36', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/26', 'PZO22001 Starfinder Player Core 388-405::/page/7/Text/18']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/1/Text/26', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/25', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/27']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 388-405::/page/1/Text/25` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/1/Text/27` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/36` | 0.871817 | **FEATS** |
| 2 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/26` | 0.871817 | **FEATS** |
| 3 | `PZO22001 Starfinder Player Core 388-405::/page/7/Text/18` | 0.871817 | **FEATS** |
| 4 | `PZO22001 Starfinder Player Core 388-405::/page/15/Text/23` | 0.829817 | **FEATS** |
| 5 | `PZO22001 Starfinder Player Core 388-405::/page/17/Text/15` | 0.829817 | **FEATS** |
| 6 | `PZO22001 Starfinder Player Core 388-405::/page/11/Text/19` | 0.829817 | **FEATS** |
| 7 | `PZO22001 Starfinder Player Core 388-405::/page/9/Text/23` | 0.829817 | **FEATS** |
| 8 | `PZO22001 Starfinder Player Core 388-405::/page/13/Text/29` | 0.829817 | **FEATS** |
| 9 | `PZO22001 Starfinder Player Core 388-405::/page/5/Text/24` | 0.389330 | **Rules Overview** |
| 10 | `PZO22001 Starfinder Player Core 388-405::/page/7/Text/21` | 0.389330 | **Rules Overview** |

### Query 25
- Text: What is the rule about **EQUIPMENT** **SPELLS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/1/Text/27']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 388-405::/page/1/Text/27', 'PZO22001 Starfinder Player Core 388-405::/page/13/Text/31', 'PZO22001 Starfinder Player Core 388-405::/page/7/Text/19']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/1/Text/27', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/26', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/28']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 388-405::/page/1/Text/26` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/1/Text/28` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/27` | 0.887907 | **EQUIPMENT** **SPELLS** |
| 2 | `PZO22001 Starfinder Player Core 388-405::/page/13/Text/31` | 0.887907 | **EQUIPMENT** **SPELLS** |
| 3 | `PZO22001 Starfinder Player Core 388-405::/page/7/Text/19` | 0.887907 | **EQUIPMENT** **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 388-405::/page/9/Text/25` | 0.697854 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/38` | 0.697854 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 388-405::/page/3/SectionHeader/21` | 0.635701 | SPELLS |
| 7 | `PZO22001 Starfinder Player Core 388-405::/page/5/Text/53` | 0.552384 | **INTRODUCTION** **ANCESTRIES & ** **BACKGROUNDS** **CLASSES** **SKILLS** **FEATS** **EQUIPMENT** **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 388-405::/page/11/Text/20` | 0.542103 | **EQUIPMENT** |
| 9 | `PZO22001 Starfinder Player Core 388-405::/page/15/Text/24` | 0.542103 | **EQUIPMENT** |
| 10 | `PZO22001 Starfinder Player Core 388-405::/page/9/Text/24` | 0.542103 | **EQUIPMENT** |

### Query 26
- Text: Summarize **PLAYING THE ** **GAME**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/1/Text/28']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 388-405::/page/1/Text/28', 'PZO22001 Starfinder Player Core 388-405::/page/3/Text/39', 'PZO22001 Starfinder Player Core 388-405::/page/13/Text/32']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/1/Text/28', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/29', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/27']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 388-405::/page/1/Text/29` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/1/Text/27` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/28` | 0.965000 | **PLAYING THE ** **GAME** |
| 2 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/39` | 0.965000 | **PLAYING THE ** **GAME** |
| 3 | `PZO22001 Starfinder Player Core 388-405::/page/13/Text/32` | 0.965000 | **PLAYING THE ** **GAME** |
| 4 | `PZO22001 Starfinder Player Core 388-405::/page/5/Text/23` | 0.923000 | **PLAYING THE ** **GAME** |
| 5 | `PZO22001 Starfinder Player Core 388-405::/page/9/Text/26` | 0.923000 | **PLAYING THE ** **GAME** |
| 6 | `PZO22001 Starfinder Player Core 388-405::/page/7/Text/20` | 0.923000 | **PLAYING THE ** **GAME** |
| 7 | `PZO22001 Starfinder Player Core 388-405::/page/15/Text/25` | 0.811006 | **PLAYING THE ** |
| 8 | `PZO22001 Starfinder Player Core 388-405::/page/11/Text/21` | 0.811006 | **PLAYING THE ** |
| 9 | `PZO22001 Starfinder Player Core 388-405::/page/17/Text/17` | 0.811006 | **PLAYING THE ** |
| 10 | `PZO22001 Starfinder Player Core 388-405::/page/1/SectionHeader/0` | 0.724027 | CHAPTER 8: PLAYING THE GAME |

### Query 27
- Text: Summarize **Rules Overview**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/1/Text/29']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 388-405::/page/15/Text/26', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/29', 'PZO22001 Starfinder Player Core 388-405::/page/13/Text/33']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/1/Text/29', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/30', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/28']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 388-405::/page/1/Text/30` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/1/Text/28` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 388-405::/page/15/Text/26` | 0.894112 | **Rules Overview** |
| 2 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/29` | 0.894112 | **Rules Overview** |
| 3 | `PZO22001 Starfinder Player Core 388-405::/page/13/Text/33` | 0.894112 | **Rules Overview** |
| 4 | `PZO22001 Starfinder Player Core 388-405::/page/5/Text/24` | 0.852112 | **Rules Overview** |
| 5 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/40` | 0.852112 | **Rules Overview** |
| 6 | `PZO22001 Starfinder Player Core 388-405::/page/7/Text/21` | 0.852112 | **Rules Overview** |
| 7 | `PZO22001 Starfinder Player Core 388-405::/page/9/Text/27` | 0.852112 | **Rules Overview** |
| 8 | `PZO22001 Starfinder Player Core 388-405::/page/2/SectionHeader/1` | 0.784852 | RULES OVERVIEW |
| 9 | `PZO22001 Starfinder Player Core 388-405::/page/11/Text/22` | 0.734841 | **GAME** **Rules Overview** |
| 10 | `PZO22001 Starfinder Player Core 388-405::/page/3/SectionHeader/13` | 0.558800 | **Ambiguous Rules** |

### Query 28
- Text: What is the rule about **Checks**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/1/Text/30']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 388-405::/page/3/Text/41', 'PZO22001 Starfinder Player Core 388-405::/page/13/Text/34', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/30']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/1/Text/30', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/31', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/29']
- Expanded expected found: `True`
- Expanded expected rank: `3`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 388-405::/page/1/Text/31` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/1/Text/29` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/41` | 0.767288 | **Checks** |
| 2 | `PZO22001 Starfinder Player Core 388-405::/page/13/Text/34` | 0.767288 | **Checks** |
| 3 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/30` | 0.767288 | **Checks** |
| 4 | `PZO22001 Starfinder Player Core 388-405::/page/7/Text/22` | 0.725288 | **Checks** |
| 5 | `PZO22001 Starfinder Player Core 388-405::/page/11/Text/23` | 0.725288 | **Checks** |
| 6 | `PZO22001 Starfinder Player Core 388-405::/page/17/Text/19` | 0.725288 | **Checks** |
| 7 | `PZO22001 Starfinder Player Core 388-405::/page/15/Text/27` | 0.725288 | **Checks** |
| 8 | `PZO22001 Starfinder Player Core 388-405::/page/5/Text/25` | 0.725288 | **Checks** |
| 9 | `PZO22001 Starfinder Player Core 388-405::/page/9/Text/28` | 0.725288 | **Checks** |
| 10 | `PZO22001 Starfinder Player Core 388-405::/page/4/SectionHeader/1` | 0.578686 | CHECKS |

### Query 29
- Text: What is the rule about **Damage Rolls**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/1/Text/31']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 388-405::/page/7/Text/23', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/31', 'PZO22001 Starfinder Player Core 388-405::/page/5/Text/26']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/1/Text/31', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/32', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/30']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 388-405::/page/1/Text/32` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/1/Text/30` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 388-405::/page/7/Text/23` | 0.900985 | **Damage Rolls** |
| 2 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/31` | 0.900985 | **Damage Rolls** |
| 3 | `PZO22001 Starfinder Player Core 388-405::/page/5/Text/26` | 0.900985 | **Damage Rolls** |
| 4 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/42` | 0.858985 | **Damage Rolls** |
| 5 | `PZO22001 Starfinder Player Core 388-405::/page/9/Text/29` | 0.858985 | **Damage Rolls** |
| 6 | `PZO22001 Starfinder Player Core 388-405::/page/15/Text/28` | 0.858985 | **Damage Rolls** |
| 7 | `PZO22001 Starfinder Player Core 388-405::/page/11/Text/24` | 0.858985 | **Damage Rolls** |
| 8 | `PZO22001 Starfinder Player Core 388-405::/page/13/Text/35` | 0.858985 | **Damage Rolls** |
| 9 | `PZO22001 Starfinder Player Core 388-405::/page/17/Text/20` | 0.858985 | **Damage Rolls** |
| 10 | `PZO22001 Starfinder Player Core 388-405::/page/10/SectionHeader/1` | 0.747132 | DAMAGE ROLLS |

### Query 30
- Text: Summarize **Immunity, ** **Weakness, & ** **Resistance**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/1/Text/32']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 388-405::/page/1/Text/32', 'PZO22001 Starfinder Player Core 388-405::/page/15/Text/29', 'PZO22001 Starfinder Player Core 388-405::/page/3/Text/43']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/1/Text/32', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/31', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/33']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 388-405::/page/1/Text/31` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/1/Text/33` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/32` | 1.020504 | **Immunity, ** **Weakness, & ** **Resistance** |
| 2 | `PZO22001 Starfinder Player Core 388-405::/page/15/Text/29` | 1.020504 | **Immunity, ** **Weakness, & ** **Resistance** |
| 3 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/43` | 1.020504 | **Immunity, ** **Weakness, & ** **Resistance** |
| 4 | `PZO22001 Starfinder Player Core 388-405::/page/13/Text/36` | 0.978504 | **Immunity, ** **Weakness, & ** **Resistance** |
| 5 | `PZO22001 Starfinder Player Core 388-405::/page/17/Text/21` | 0.978504 | **Immunity, ** **Weakness, & ** **Resistance** |
| 6 | `PZO22001 Starfinder Player Core 388-405::/page/9/Text/30` | 0.978504 | **Immunity, ** **Weakness, & ** **Resistance** |
| 7 | `PZO22001 Starfinder Player Core 388-405::/page/11/Text/25` | 0.978504 | **Immunity, ** **Weakness, & ** **Resistance** |
| 8 | `PZO22001 Starfinder Player Core 388-405::/page/5/Text/27` | 0.978504 | **Immunity, ** **Weakness, & ** **Resistance** |
| 9 | `PZO22001 Starfinder Player Core 388-405::/page/7/Text/24` | 0.978504 | **Immunity, ** **Weakness, & ** **Resistance** |
| 10 | `PZO22001 Starfinder Player Core 388-405::/page/12/SectionHeader/1` | 0.913276 | IMMUNITY, WEAKNESS,  AND RESISTANCE |

### Query 31
- Text: What is the rule about **Damage Types**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/1/Text/33']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 388-405::/page/1/Text/33', 'PZO22001 Starfinder Player Core 388-405::/page/5/Text/28', 'PZO22001 Starfinder Player Core 388-405::/page/3/Text/44']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/1/Text/33', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/32', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/34']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 388-405::/page/1/Text/32` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/1/Text/34` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/33` | 0.891010 | **Damage Types** |
| 2 | `PZO22001 Starfinder Player Core 388-405::/page/5/Text/28` | 0.891010 | **Damage Types** |
| 3 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/44` | 0.891010 | **Damage Types** |
| 4 | `PZO22001 Starfinder Player Core 388-405::/page/7/Text/25` | 0.849010 | **Damage Types** |
| 5 | `PZO22001 Starfinder Player Core 388-405::/page/9/Text/31` | 0.849010 | **Damage Types** |
| 6 | `PZO22001 Starfinder Player Core 388-405::/page/15/Text/30` | 0.849010 | **Damage Types** |
| 7 | `PZO22001 Starfinder Player Core 388-405::/page/11/Text/26` | 0.849010 | **Damage Types** |
| 8 | `PZO22001 Starfinder Player Core 388-405::/page/13/Text/37` | 0.849010 | **Damage Types** |
| 9 | `PZO22001 Starfinder Player Core 388-405::/page/17/Text/22` | 0.849010 | **Damage Types** |
| 10 | `PZO22001 Starfinder Player Core 388-405::/page/13/SectionHeader/1` | 0.779677 | **DAMAGE TYPES** |

### Query 32
- Text: What is the rule about **Hit Points, ** **Healing, and ** **Dying**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/1/Text/34']
- Expected found: `True`
- Expected rank: `5`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 388-405::/page/3/Text/45', 'PZO22001 Starfinder Player Core 388-405::/page/5/Text/29', 'PZO22001 Starfinder Player Core 388-405::/page/9/Text/32']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/1/Text/34', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/35', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/33']
- Expanded expected found: `True`
- Expanded expected rank: `5`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 388-405::/page/1/Text/35` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/1/Text/33` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/45` | 0.937527 | **Hit Points, ** **Healing, and ** **Dying** |
| 2 | `PZO22001 Starfinder Player Core 388-405::/page/5/Text/29` | 0.937527 | **Hit Points, ** **Healing, and ** **Dying** |
| 3 | `PZO22001 Starfinder Player Core 388-405::/page/9/Text/32` | 0.937527 | **Hit Points, ** **Healing, and ** **Dying** |
| 4 | `PZO22001 Starfinder Player Core 388-405::/page/15/Text/31` | 0.895527 | **Hit Points, ** **Healing, and ** **Dying** |
| 5 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/34` | 0.895527 | **Hit Points, ** **Healing, and ** **Dying** |
| 6 | `PZO22001 Starfinder Player Core 388-405::/page/11/Text/27` | 0.895527 | **Hit Points, ** **Healing, and ** **Dying** |
| 7 | `PZO22001 Starfinder Player Core 388-405::/page/7/Text/26` | 0.895527 | **Hit Points, ** **Healing, and ** **Dying** |
| 8 | `PZO22001 Starfinder Player Core 388-405::/page/13/Text/38` | 0.895527 | **Hit Points, ** **Healing, and ** **Dying** |
| 9 | `PZO22001 Starfinder Player Core 388-405::/page/17/Text/23` | 0.895527 | **Hit Points, ** **Healing, and ** **Dying** |
| 10 | `PZO22001 Starfinder Player Core 388-405::/page/14/SectionHeader/1` | 0.690335 | HIT POINTS, HEALING,  AND DYING |

### Query 33
- Text: Summarize **Hero Points**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/1/Text/35']
- Expected found: `True`
- Expected rank: `8`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 388-405::/page/17/Text/24', 'PZO22001 Starfinder Player Core 388-405::/page/9/Text/33', 'PZO22001 Starfinder Player Core 388-405::/page/15/Text/32']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/1/Text/35', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/34', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/36']
- Expanded expected found: `True`
- Expanded expected rank: `8`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 388-405::/page/1/Text/34` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/1/Text/36` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 388-405::/page/17/Text/24` | 0.970595 | **Hero Points** |
| 2 | `PZO22001 Starfinder Player Core 388-405::/page/9/Text/33` | 0.970595 | **Hero Points** |
| 3 | `PZO22001 Starfinder Player Core 388-405::/page/15/Text/32` | 0.970595 | **Hero Points** |
| 4 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/46` | 0.928595 | **Hero Points** |
| 5 | `PZO22001 Starfinder Player Core 388-405::/page/13/Text/39` | 0.928595 | **Hero Points** |
| 6 | `PZO22001 Starfinder Player Core 388-405::/page/11/Text/28` | 0.928595 | **Hero Points** |
| 7 | `PZO22001 Starfinder Player Core 388-405::/page/7/Text/27` | 0.928595 | **Hero Points** |
| 8 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/35` | 0.928595 | **Hero Points** |
| 9 | `PZO22001 Starfinder Player Core 388-405::/page/5/Text/30` | 0.928595 | **Hero Points** |
| 10 | `PZO22001 Starfinder Player Core 388-405::/page/17/Text/3` | 0.627416 | The GM is in charge of awarding Hero Points. Usually, each  character gets 1 Hero Point at the start of a session and  can gain more later by performing heroic deeds—something  selfless, daring, or be |

### Query 34
- Text: What is the rule about **Actions**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/1/Text/36']
- Expected found: `True`
- Expected rank: `8`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 388-405::/page/15/Text/33', 'PZO22001 Starfinder Player Core 388-405::/page/7/Text/28', 'PZO22001 Starfinder Player Core 388-405::/page/5/Text/31']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/1/Text/36', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/37', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/35']
- Expanded expected found: `True`
- Expanded expected rank: `8`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 388-405::/page/1/Text/37` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/1/Text/35` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 388-405::/page/15/Text/33` | 0.831891 | **Actions** |
| 2 | `PZO22001 Starfinder Player Core 388-405::/page/7/Text/28` | 0.831891 | **Actions** |
| 3 | `PZO22001 Starfinder Player Core 388-405::/page/5/Text/31` | 0.831891 | **Actions** |
| 4 | `PZO22001 Starfinder Player Core 388-405::/page/9/Text/34` | 0.789891 | **Actions** |
| 5 | `PZO22001 Starfinder Player Core 388-405::/page/13/Text/40` | 0.789891 | **Actions** |
| 6 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/47` | 0.789891 | **Actions** |
| 7 | `PZO22001 Starfinder Player Core 388-405::/page/17/Text/25` | 0.789891 | **Actions** |
| 8 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/36` | 0.789891 | **Actions** |
| 9 | `PZO22001 Starfinder Player Core 388-405::/page/11/Text/29` | 0.789891 | **Actions** |
| 10 | `PZO22001 Starfinder Player Core 388-405::/page/2/SectionHeader/7` | 0.679878 | ACTIONS |

### Query 35
- Text: Summarize **Movement**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/1/Text/37']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 388-405::/page/17/Text/26', 'PZO22001 Starfinder Player Core 388-405::/page/9/Text/35', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/37']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/1/Text/37', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/38', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/36']
- Expanded expected found: `True`
- Expanded expected rank: `3`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 388-405::/page/1/Text/38` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/1/Text/36` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 388-405::/page/17/Text/26` | 0.929132 | **Movement** |
| 2 | `PZO22001 Starfinder Player Core 388-405::/page/9/Text/35` | 0.929132 | **Movement** |
| 3 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/37` | 0.929132 | **Movement** |
| 4 | `PZO22001 Starfinder Player Core 388-405::/page/7/Text/29` | 0.887132 | **Movement** |
| 5 | `PZO22001 Starfinder Player Core 388-405::/page/5/Text/32` | 0.887132 | **Movement** |
| 6 | `PZO22001 Starfinder Player Core 388-405::/page/15/Text/34` | 0.887132 | **Movement** |
| 7 | `PZO22001 Starfinder Player Core 388-405::/page/11/Text/30` | 0.887132 | **Movement** |
| 8 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/48` | 0.887132 | **Movement** |
| 9 | `PZO22001 Starfinder Player Core 388-405::/page/13/Text/41` | 0.887132 | **Movement** |
| 10 | `PZO22001 Starfinder Player Core 388-405::/page/2/SectionHeader/19` | 0.614658 | MOVEMENT |

### Query 36
- Text: Summarize **Effects** **Area**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/1/Text/38']
- Expected found: `True`
- Expected rank: `4`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 388-405::/page/9/Text/36', 'PZO22001 Starfinder Player Core 388-405::/page/17/Text/27', 'PZO22001 Starfinder Player Core 388-405::/page/13/Text/42']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/1/Text/38', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/39', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/37']
- Expanded expected found: `True`
- Expanded expected rank: `4`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 388-405::/page/1/Text/39` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/1/Text/37` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 388-405::/page/9/Text/36` | 0.987469 | **Effects** **Area** |
| 2 | `PZO22001 Starfinder Player Core 388-405::/page/17/Text/27` | 0.987469 | **Effects** **Area** |
| 3 | `PZO22001 Starfinder Player Core 388-405::/page/13/Text/42` | 0.987469 | **Effects** **Area** |
| 4 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/38` | 0.945469 | **Effects** **Area** |
| 5 | `PZO22001 Starfinder Player Core 388-405::/page/11/Text/31` | 0.746103 | **Effects** |
| 6 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/49` | 0.746103 | **Effects** |
| 7 | `PZO22001 Starfinder Player Core 388-405::/page/5/Text/33` | 0.746103 | **Effects** |
| 8 | `PZO22001 Starfinder Player Core 388-405::/page/7/Text/30` | 0.746103 | **Effects** |
| 9 | `PZO22001 Starfinder Player Core 388-405::/page/15/Text/35` | 0.746103 | **Effects** |
| 10 | `PZO22001 Starfinder Player Core 388-405::/page/2/SectionHeader/16` | 0.684706 | EFFECTS |

### Query 37
- Text: Summarize **Afflictions**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/1/Text/39']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 388-405::/page/1/Text/39', 'PZO22001 Starfinder Player Core 388-405::/page/15/Text/37', 'PZO22001 Starfinder Player Core 388-405::/page/17/Text/28']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/1/Text/39', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/38', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/40']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 388-405::/page/1/Text/38` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/1/Text/40` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/39` | 0.968408 | **Afflictions** |
| 2 | `PZO22001 Starfinder Player Core 388-405::/page/15/Text/37` | 0.968407 | **Afflictions** |
| 3 | `PZO22001 Starfinder Player Core 388-405::/page/17/Text/28` | 0.968407 | **Afflictions** |
| 4 | `PZO22001 Starfinder Player Core 388-405::/page/7/Text/32` | 0.926407 | **Afflictions** |
| 5 | `PZO22001 Starfinder Player Core 388-405::/page/13/Text/43` | 0.926407 | **Afflictions** |
| 6 | `PZO22001 Starfinder Player Core 388-405::/page/9/Text/37` | 0.926407 | **Afflictions** |
| 7 | `PZO22001 Starfinder Player Core 388-405::/page/11/Text/33` | 0.926407 | **Afflictions** |
| 8 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/50` | 0.844597 | **Area** **Afflictions** |
| 9 | `PZO22001 Starfinder Player Core 388-405::/page/5/Text/34` | 0.844597 | **Area** **Afflictions** |
| 10 | `PZO22001 Starfinder Player Core 388-405::/page/10/ListItem/8` | 0.509217 | 3. Apply **immunities**, **weaknesses**, and **resistances **the  subject has to the damage. |

### Query 38
- Text: What is the rule about **Counteracting**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/1/Text/40']
- Expected found: `True`
- Expected rank: `6`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 388-405::/page/5/Text/35', 'PZO22001 Starfinder Player Core 388-405::/page/15/Text/38', 'PZO22001 Starfinder Player Core 388-405::/page/7/Text/33']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/1/Text/40', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/41', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/39']
- Expanded expected found: `True`
- Expanded expected rank: `6`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 388-405::/page/1/Text/41` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/1/Text/39` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 388-405::/page/5/Text/35` | 0.882936 | **Counteracting** |
| 2 | `PZO22001 Starfinder Player Core 388-405::/page/15/Text/38` | 0.882936 | **Counteracting** |
| 3 | `PZO22001 Starfinder Player Core 388-405::/page/7/Text/33` | 0.882936 | **Counteracting** |
| 4 | `PZO22001 Starfinder Player Core 388-405::/page/11/Text/34` | 0.840936 | **Counteracting** |
| 5 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/51` | 0.840936 | **Counteracting** |
| 6 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/40` | 0.840936 | **Counteracting** |
| 7 | `PZO22001 Starfinder Player Core 388-405::/page/9/Text/38` | 0.840936 | **Counteracting** |
| 8 | `PZO22001 Starfinder Player Core 388-405::/page/13/Text/44` | 0.840936 | **Counteracting** |
| 9 | `PZO22001 Starfinder Player Core 388-405::/page/17/Text/29` | 0.840936 | **Counteracting** |
| 10 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/6` | 0.410356 | A core principle of Starfinder is that specific rules override  general ones. If two rules conflict, the more specific  one takes precedence. If there's still ambiguity, the GM  determines which rule |

### Query 39
- Text: Summarize **Perception and ** **Detection**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/1/Text/41']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 388-405::/page/9/Text/39', 'PZO22001 Starfinder Player Core 388-405::/page/3/Text/52', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/41']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/1/Text/41', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/42', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/40']
- Expanded expected found: `True`
- Expanded expected rank: `3`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 388-405::/page/1/Text/42` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/1/Text/40` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 388-405::/page/9/Text/39` | 0.992556 | **Perception and ** **Detection** |
| 2 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/52` | 0.992556 | **Perception and ** **Detection** |
| 3 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/41` | 0.992556 | **Perception and ** **Detection** |
| 4 | `PZO22001 Starfinder Player Core 388-405::/page/5/Text/36` | 0.950556 | **Perception and ** **Detection** |
| 5 | `PZO22001 Starfinder Player Core 388-405::/page/7/Text/34` | 0.950556 | **Perception and ** **Detection** |
| 6 | `PZO22001 Starfinder Player Core 388-405::/page/17/Text/30` | 0.950556 | **Perception and ** **Detection** |
| 7 | `PZO22001 Starfinder Player Core 388-405::/page/11/Text/35` | 0.950556 | **Perception and ** **Detection** |
| 8 | `PZO22001 Starfinder Player Core 388-405::/page/13/Text/45` | 0.950556 | **Perception and ** **Detection** |
| 9 | `PZO22001 Starfinder Player Core 388-405::/page/15/Text/39` | 0.950556 | **Perception and ** **Detection** |
| 10 | `PZO22001 Starfinder Player Core 388-405::/page/3/SectionHeader/27` | 0.828482 | PERCEPTION AND DETECTION |

### Query 40
- Text: Summarize **Encounter ** **Mode**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/1/Text/42']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 388-405::/page/17/Text/31', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/42', 'PZO22001 Starfinder Player Core 388-405::/page/15/Text/40']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/1/Text/42', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/41', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/43']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 388-405::/page/1/Text/41` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/1/Text/43` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 388-405::/page/17/Text/31` | 0.996085 | **Encounter ** **Mode** |
| 2 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/42` | 0.996085 | **Encounter ** **Mode** |
| 3 | `PZO22001 Starfinder Player Core 388-405::/page/15/Text/40` | 0.996085 | **Encounter ** **Mode** |
| 4 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/53` | 0.954085 | **Encounter ** **Mode** |
| 5 | `PZO22001 Starfinder Player Core 388-405::/page/13/Text/46` | 0.954085 | **Encounter ** **Mode** |
| 6 | `PZO22001 Starfinder Player Core 388-405::/page/5/Text/37` | 0.954085 | **Encounter ** **Mode** |
| 7 | `PZO22001 Starfinder Player Core 388-405::/page/9/Text/40` | 0.954085 | **Encounter ** **Mode** |
| 8 | `PZO22001 Starfinder Player Core 388-405::/page/7/Text/35` | 0.954085 | **Encounter ** **Mode** |
| 9 | `PZO22001 Starfinder Player Core 388-405::/page/11/Text/36` | 0.954085 | **Encounter ** **Mode** |
| 10 | `PZO22001 Starfinder Player Core 388-405::/page/15/Text/41` | 0.650901 | **Exploration ** **Mode** |

### Query 41
- Text: Summarize **Exploration ** **Mode**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/1/Text/43']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 388-405::/page/15/Text/41', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/43', 'PZO22001 Starfinder Player Core 388-405::/page/17/Text/32']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/1/Text/43', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/42', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/44']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 388-405::/page/1/Text/42` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/1/Text/44` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 388-405::/page/15/Text/41` | 0.983318 | **Exploration ** **Mode** |
| 2 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/43` | 0.983318 | **Exploration ** **Mode** |
| 3 | `PZO22001 Starfinder Player Core 388-405::/page/17/Text/32` | 0.983318 | **Exploration ** **Mode** |
| 4 | `PZO22001 Starfinder Player Core 388-405::/page/7/Text/36` | 0.941318 | **Exploration ** **Mode** |
| 5 | `PZO22001 Starfinder Player Core 388-405::/page/13/Text/47` | 0.941318 | **Exploration ** **Mode** |
| 6 | `PZO22001 Starfinder Player Core 388-405::/page/11/Text/37` | 0.941318 | **Exploration ** **Mode** |
| 7 | `PZO22001 Starfinder Player Core 388-405::/page/9/Text/41` | 0.941318 | **Exploration ** **Mode** |
| 8 | `PZO22001 Starfinder Player Core 388-405::/page/5/Text/38` | 0.941318 | **Exploration ** **Mode** |
| 9 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/54` | 0.941318 | **Exploration ** **Mode** |
| 10 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/5` | 0.613909 | **Exploration** **mode** (page 430) takes place over minutes or  hours. You use your travel Speed if you're moving, and you  engage in **exploration** **activities** like Avoiding Notice, Detecting  M |

### Query 42
- Text: Summarize **Downtime ** **Mode**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/1/Text/44']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 388-405::/page/17/Text/33', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/44', 'PZO22001 Starfinder Player Core 388-405::/page/3/Text/55']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/1/Text/44', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/45', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/43']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 388-405::/page/1/Text/45` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/1/Text/43` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 388-405::/page/17/Text/33` | 0.972659 | **Downtime ** **Mode** |
| 2 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/44` | 0.972659 | **Downtime ** **Mode** |
| 3 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/55` | 0.972659 | **Downtime ** **Mode** |
| 4 | `PZO22001 Starfinder Player Core 388-405::/page/15/Text/42` | 0.930659 | **Downtime ** **Mode** |
| 5 | `PZO22001 Starfinder Player Core 388-405::/page/13/Text/48` | 0.930659 | **Downtime ** **Mode** |
| 6 | `PZO22001 Starfinder Player Core 388-405::/page/9/Text/42` | 0.930659 | **Downtime ** **Mode** |
| 7 | `PZO22001 Starfinder Player Core 388-405::/page/7/Text/37` | 0.930659 | **Downtime ** **Mode** |
| 8 | `PZO22001 Starfinder Player Core 388-405::/page/5/Text/39` | 0.930659 | **Downtime ** **Mode** |
| 9 | `PZO22001 Starfinder Player Core 388-405::/page/11/Text/38` | 0.930659 | **Downtime ** **Mode** |
| 10 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/6` | 0.654072 | **Downtime mode** (page 433) takes place over days. You  might make money, train, or recover, among other things. |

### Query 43
- Text: Summarize **CONDITIONS ** **APPENDIX**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/1/Text/45']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 388-405::/page/17/Text/34', 'PZO22001 Starfinder Player Core 388-405::/page/15/Text/43', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/45']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/1/Text/45', 'PZO22001 Starfinder Player Core 388-405::/page/3/Text/56', 'PZO22001 Starfinder Player Core 388-405::/page/7/Text/38', 'PZO22001 Starfinder Player Core 388-405::/page/17/Text/34', 'PZO22001 Starfinder Player Core 388-405::/page/9/Text/43', 'PZO22001 Starfinder Player Core 388-405::/page/5/Text/40', 'PZO22001 Starfinder Player Core 388-405::/page/11/Text/39', 'PZO22001 Starfinder Player Core 388-405::/page/15/Text/43', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/44', 'PZO22001 Starfinder Player Core 388-405::/page/13/Text/49', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/46']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 388-405::/page/3/Text/56` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/7/Text/38` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/17/Text/34` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/9/Text/43` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/5/Text/40` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/11/Text/39` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/15/Text/43` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/1/Text/44` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/13/Text/49` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/1/Text/46` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 388-405::/page/17/Text/34` | 0.983499 | **CONDITIONS ** **APPENDIX** |
| 2 | `PZO22001 Starfinder Player Core 388-405::/page/15/Text/43` | 0.983498 | **CONDITIONS ** **APPENDIX** |
| 3 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/45` | 0.983498 | **CONDITIONS ** **APPENDIX** |
| 4 | `PZO22001 Starfinder Player Core 388-405::/page/7/Text/38` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 5 | `PZO22001 Starfinder Player Core 388-405::/page/5/Text/40` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 6 | `PZO22001 Starfinder Player Core 388-405::/page/13/Text/49` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 7 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/56` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 8 | `PZO22001 Starfinder Player Core 388-405::/page/9/Text/43` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 9 | `PZO22001 Starfinder Player Core 388-405::/page/11/Text/39` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 10 | `PZO22001 Starfinder Player Core 388-405::/page/5/Text/24` | 0.446150 | **Rules Overview** |

### Query 44
- Text: Summarize **GLOSSARY & ** **INDEX**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/1/Text/46']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 388-405::/page/15/Text/44', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/46', 'PZO22001 Starfinder Player Core 388-405::/page/13/Text/50']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/1/Text/46', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/45', 'PZO22001 Starfinder Player Core 388-405::/page/2/SectionHeader/1']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 388-405::/page/1/Text/45` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/2/SectionHeader/1` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 388-405::/page/15/Text/44` | 0.993465 | **GLOSSARY & ** **INDEX** |
| 2 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/46` | 0.993465 | **GLOSSARY & ** **INDEX** |
| 3 | `PZO22001 Starfinder Player Core 388-405::/page/13/Text/50` | 0.993465 | **GLOSSARY & ** **INDEX** |
| 4 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/57` | 0.951465 | **GLOSSARY & ** **INDEX** |
| 5 | `PZO22001 Starfinder Player Core 388-405::/page/7/Text/39` | 0.951465 | **GLOSSARY & ** **INDEX** |
| 6 | `PZO22001 Starfinder Player Core 388-405::/page/11/Text/40` | 0.951465 | **GLOSSARY & ** **INDEX** |
| 7 | `PZO22001 Starfinder Player Core 388-405::/page/9/Text/44` | 0.951465 | **GLOSSARY & ** **INDEX** |
| 8 | `PZO22001 Starfinder Player Core 388-405::/page/17/Text/35` | 0.951465 | **GLOSSARY & ** **INDEX** |
| 9 | `PZO22001 Starfinder Player Core 388-405::/page/5/Text/41` | 0.951465 | **GLOSSARY & ** **INDEX** |
| 10 | `PZO22001 Starfinder Player Core 388-405::/page/15/Text/21` | 0.385404 | **CLASSES** |

### Query 45
- Text: Summarize RULES OVERVIEW
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/2/SectionHeader/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 388-405::/page/2/SectionHeader/1', 'PZO22001 Starfinder Player Core 388-405::/page/3/Text/40', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/29']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/2/SectionHeader/1', 'PZO22001 Starfinder Player Core 388-405::/page/2/SectionHeader/3', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/46']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 388-405::/page/2/SectionHeader/3` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/1/Text/46` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 388-405::/page/2/SectionHeader/1` | 0.855516 | RULES OVERVIEW |
| 2 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/40` | 0.770001 | **Rules Overview** |
| 3 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/29` | 0.770001 | **Rules Overview** |
| 4 | `PZO22001 Starfinder Player Core 388-405::/page/15/Text/26` | 0.728001 | **Rules Overview** |
| 5 | `PZO22001 Starfinder Player Core 388-405::/page/7/Text/21` | 0.728001 | **Rules Overview** |
| 6 | `PZO22001 Starfinder Player Core 388-405::/page/13/Text/33` | 0.728001 | **Rules Overview** |
| 7 | `PZO22001 Starfinder Player Core 388-405::/page/5/Text/24` | 0.728001 | **Rules Overview** |
| 8 | `PZO22001 Starfinder Player Core 388-405::/page/9/Text/27` | 0.728001 | **Rules Overview** |
| 9 | `PZO22001 Starfinder Player Core 388-405::/page/11/Text/22` | 0.641795 | **GAME** **Rules Overview** |
| 10 | `PZO22001 Starfinder Player Core 388-405::/page/3/SectionHeader/13` | 0.507618 | **Ambiguous Rules** |

### Query 46
- Text: Summarize MODES OF PLAY
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/2/SectionHeader/3']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 388-405::/page/2/SectionHeader/3', 'PZO22001 Starfinder Player Core 388-405::/page/2/Text/4', 'PZO22001 Starfinder Player Core 388-405::/page/1/SectionHeader/0']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/2/SectionHeader/3', 'PZO22001 Starfinder Player Core 388-405::/page/2/SectionHeader/1', 'PZO22001 Starfinder Player Core 388-405::/page/2/Text/4']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 388-405::/page/2/SectionHeader/1` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/2/Text/4` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 388-405::/page/2/SectionHeader/3` | 0.948382 | MODES OF PLAY |
| 2 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/4` | 0.576609 | This game presents three main methods of structuring play.  **Encounter mode** (page 427) is highly structured and is most  often used for combat or stressful situations. Everyone in an  encounter rol |
| 3 | `PZO22001 Starfinder Player Core 388-405::/page/1/SectionHeader/0` | 0.546091 | CHAPTER 8: PLAYING THE GAME |
| 4 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/3` | 0.488318 | Before diving into how to play Starfinder, it's important to  understand the game's three modes of play, which determine  the pace of your adventure and the specific rules you'll use  at a given time. |
| 5 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/4` | 0.478848 | The most intricate of the modes is **encounter mode**. This  is where most of the intense action takes place, and it's  most often used for combat or other high-stakes situations.  The GM typically sw |
| 6 | `PZO22001 Starfinder Player Core 388-405::/page/9/Text/26` | 0.470924 | **PLAYING THE ** **GAME** |
| 7 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/28` | 0.470924 | **PLAYING THE ** **GAME** |
| 8 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/39` | 0.470924 | **PLAYING THE ** **GAME** |
| 9 | `PZO22001 Starfinder Player Core 388-405::/page/7/Text/20` | 0.470924 | **PLAYING THE ** **GAME** |
| 10 | `PZO22001 Starfinder Player Core 388-405::/page/13/Text/32` | 0.470924 | **PLAYING THE ** **GAME** |

### Query 47
- Text: What is the rule about This game presents three main methods of structuring play.  **Encounter mode** (page 427) is highly structured and is most  often used for combat or stressful situations. Everyone in an  encounter rolls **initiative** (page 427) to determine the order  they act, with highest results going first. A participant takes  their **turn** when their initiative comes up (page 427). You can  **Delay** to change when you take your turn (page 408).?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/2/Text/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 388-405::/page/2/Text/4', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/4', 'PZO22001 Starfinder Player Core 388-405::/page/9/Text/5']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/2/Text/4', 'PZO22001 Starfinder Player Core 388-405::/page/2/SectionHeader/3', 'PZO22001 Starfinder Player Core 388-405::/page/2/Text/5']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 388-405::/page/2/SectionHeader/3` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/2/Text/5` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/4` | 1.006151 | This game presents three main methods of structuring play.  **Encounter mode** (page 427) is highly structured and is most  often used for combat or stressful situations. Everyone in an  encounter rol |
| 2 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/4` | 0.829177 | The most intricate of the modes is **encounter mode**. This  is where most of the intense action takes place, and it's  most often used for combat or other high-stakes situations.  The GM typically sw |
| 3 | `PZO22001 Starfinder Player Core 388-405::/page/9/Text/5` | 0.718608 | Often, you'll roll a Perception check to determine your order  in initiative. When you do this, instead of comparing the  result against a DC, the GM will put the results for everyone  in the encounte |
| 4 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/5` | 0.608324 | In **exploration mode**, time is more flexible and the play  more free-form. Minutes, hours, or even days in the game  world pass quickly in the real world, as the characters travel  between star syst |
| 5 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/8` | 0.597733 | During an encounter, you get 3 actions and 1 reaction per turn  (page 427). Icons indicate whether your abilities take a single  action [one-action], 2 actions [two-actions], 3 actions [three-actions] |
| 6 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/5` | 0.574922 | **Exploration** **mode** (page 430) takes place over minutes or  hours. You use your travel Speed if you're moving, and you  engage in **exploration** **activities** like Avoiding Notice, Detecting  M |
| 7 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/25` | 0.555512 | **Strike** (page 410) actions have the attack trait and allow you  to attack with a weapon you're wielding or an unarmed attack  (such as a tail). If you're using a melee weapon or unarmed  attack, yo |
| 8 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/3` | 0.551645 | Before diving into how to play Starfinder, it's important to  understand the game's three modes of play, which determine  the pace of your adventure and the specific rules you'll use  at a given time. |
| 9 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/1` | 0.543665 | At this point, you have a character and are ready to play Starfinder! Or maybe you're the GM and you're  getting ready to run your first adventure. Either way, this chapter provides the full details f |
| 10 | `PZO22001 Starfinder Player Core 388-405::/page/11/Text/22` | 0.537192 | **GAME** **Rules Overview** |

### Query 48
- Text: What is the rule about **Exploration** **mode** (page 430) takes place over minutes or  hours. You use your travel Speed if you're moving, and you  engage in **exploration** **activities** like Avoiding Notice, Detecting  Magic, Scouting, or Searching. You can **rest** while exploring to  recover HP and abilities, and make **daily preparations** at the  start of each day (page 432).?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/2/Text/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 388-405::/page/2/Text/5', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/5', 'PZO22001 Starfinder Player Core 388-405::/page/3/Text/26']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/2/Text/5', 'PZO22001 Starfinder Player Core 388-405::/page/2/Text/4', 'PZO22001 Starfinder Player Core 388-405::/page/2/Text/6']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 388-405::/page/2/Text/4` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/2/Text/6` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/5` | 0.982916 | **Exploration** **mode** (page 430) takes place over minutes or  hours. You use your travel Speed if you're moving, and you  engage in **exploration** **activities** like Avoiding Notice, Detecting  M |
| 2 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/5` | 0.786474 | In **exploration mode**, time is more flexible and the play  more free-form. Minutes, hours, or even days in the game  world pass quickly in the real world, as the characters travel  between star syst |
| 3 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/26` | 0.651209 | Skill checks are required for all sorts of other tasks related  to adventuring and life in general. Most of their rules are  in Chapter 4 (page 183). You'll find the rules for **calculating ** **skill |
| 4 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/6` | 0.597106 | The third mode is **downtime**. During downtime, the  characters are at little risk, and the passage of time is  measured in days or longer. This is when you might repair  or craft new equipment, rese |
| 5 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/6` | 0.596313 | **Downtime mode** (page 433) takes place over days. You  might make money, train, or recover, among other things. |
| 6 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/23` | 0.583494 | **Related:** Escape a grab or restraint (page 408), falling (page  413), forced movement (page 414), moving through creatures  (page 414), special movement modes (burrow, climb, fly, and  swim; page 4 |
| 7 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/28` | 0.571262 | Your **Perception **modifier (page 396) indicates how good you  are at noticing things around you. You typically use the **Seek** basic action (page 409) to find physical things or the **Sense ** **Mo |
| 8 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/4` | 0.551433 | This game presents three main methods of structuring play.  **Encounter mode** (page 427) is highly structured and is most  often used for combat or stressful situations. Everyone in an  encounter rol |
| 9 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/4` | 0.537525 | The most intricate of the modes is **encounter mode**. This  is where most of the intense action takes place, and it's  most often used for combat or other high-stakes situations.  The GM typically sw |
| 10 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/20` | 0.527319 | Your **Speed **(page 412) governs how far you can move. **Stride** (page 410) is an action that has the move trait and allows you to  move a number of feet up to your Speed. You may need to Stride  mu |

### Query 49
- Text: What is the rule about **Downtime mode** (page 433) takes place over days. You  might make money, train, or recover, among other things.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/2/Text/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 388-405::/page/2/Text/6', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/6', 'PZO22001 Starfinder Player Core 388-405::/page/2/Text/5']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/2/Text/6', 'PZO22001 Starfinder Player Core 388-405::/page/2/SectionHeader/7', 'PZO22001 Starfinder Player Core 388-405::/page/2/Text/5']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 388-405::/page/2/SectionHeader/7` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/2/Text/5` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/6` | 0.977390 | **Downtime mode** (page 433) takes place over days. You  might make money, train, or recover, among other things. |
| 2 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/6` | 0.720662 | The third mode is **downtime**. During downtime, the  characters are at little risk, and the passage of time is  measured in days or longer. This is when you might repair  or craft new equipment, rese |
| 3 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/5` | 0.635882 | **Exploration** **mode** (page 430) takes place over minutes or  hours. You use your travel Speed if you're moving, and you  engage in **exploration** **activities** like Avoiding Notice, Detecting  M |
| 4 | `PZO22001 Starfinder Player Core 388-405::/page/5/Text/39` | 0.586471 | **Downtime ** **Mode** |
| 5 | `PZO22001 Starfinder Player Core 388-405::/page/9/Text/42` | 0.586471 | **Downtime ** **Mode** |
| 6 | `PZO22001 Starfinder Player Core 388-405::/page/7/Text/37` | 0.586471 | **Downtime ** **Mode** |
| 7 | `PZO22001 Starfinder Player Core 388-405::/page/11/Text/38` | 0.586471 | **Downtime ** **Mode** |
| 8 | `PZO22001 Starfinder Player Core 388-405::/page/15/Text/42` | 0.586471 | **Downtime ** **Mode** |
| 9 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/55` | 0.586471 | **Downtime ** **Mode** |
| 10 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/44` | 0.586471 | **Downtime ** **Mode** |

### Query 50
- Text: What is the rule about ACTIONS?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/2/SectionHeader/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 388-405::/page/2/SectionHeader/7', 'PZO22001 Starfinder Player Core 388-405::/page/15/Text/33', 'PZO22001 Starfinder Player Core 388-405::/page/7/Text/28']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/2/SectionHeader/7', 'PZO22001 Starfinder Player Core 388-405::/page/2/Text/6', 'PZO22001 Starfinder Player Core 388-405::/page/2/Text/8']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 388-405::/page/2/Text/6` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/2/Text/8` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 388-405::/page/2/SectionHeader/7` | 0.772859 | ACTIONS |
| 2 | `PZO22001 Starfinder Player Core 388-405::/page/15/Text/33` | 0.719885 | **Actions** |
| 3 | `PZO22001 Starfinder Player Core 388-405::/page/7/Text/28` | 0.719885 | **Actions** |
| 4 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/36` | 0.677885 | **Actions** |
| 5 | `PZO22001 Starfinder Player Core 388-405::/page/9/Text/34` | 0.677885 | **Actions** |
| 6 | `PZO22001 Starfinder Player Core 388-405::/page/17/Text/25` | 0.677885 | **Actions** |
| 7 | `PZO22001 Starfinder Player Core 388-405::/page/5/Text/31` | 0.677885 | **Actions** |
| 8 | `PZO22001 Starfinder Player Core 388-405::/page/13/Text/40` | 0.677885 | **Actions** |
| 9 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/47` | 0.677885 | **Actions** |
| 10 | `PZO22001 Starfinder Player Core 388-405::/page/11/Text/29` | 0.677885 | **Actions** |

### Query 51
- Text: What is the rule about During an encounter, you get 3 actions and 1 reaction per turn  (page 427). Icons indicate whether your abilities take a single  action [one-action], 2 actions [two-actions], 3 actions [three-actions], a reaction [reaction], or a  free action [free-action]. **Reactions** have **Triggers** (page 406), allowing  you to take them whenever they come up. The **Ready** basic  action (page 409) lets you prepare to use a single action as a  reaction. Free actions can have triggers like reactions; a free  action with no trigger can be used like a single action, but don't  cost any of your actions for the turn.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/2/Text/8']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 388-405::/page/2/Text/8', 'PZO22001 Starfinder Player Core 388-405::/page/2/Text/25', 'PZO22001 Starfinder Player Core 388-405::/page/2/Text/20']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/2/Text/8', 'PZO22001 Starfinder Player Core 388-405::/page/2/Text/9', 'PZO22001 Starfinder Player Core 388-405::/page/2/SectionHeader/7']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 388-405::/page/2/Text/9` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/2/SectionHeader/7` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/8` | 0.984581 | During an encounter, you get 3 actions and 1 reaction per turn  (page 427). Icons indicate whether your abilities take a single  action [one-action], 2 actions [two-actions], 3 actions [three-actions] |
| 2 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/25` | 0.650979 | **Strike** (page 410) actions have the attack trait and allow you  to attack with a weapon you're wielding or an unarmed attack  (such as a tail). If you're using a melee weapon or unarmed  attack, yo |
| 3 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/20` | 0.650849 | Your **Speed **(page 412) governs how far you can move. **Stride** (page 410) is an action that has the move trait and allows you to  move a number of feet up to your Speed. You may need to Stride  mu |
| 4 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/4` | 0.586250 | This game presents three main methods of structuring play.  **Encounter mode** (page 427) is highly structured and is most  often used for combat or stressful situations. Everyone in an  encounter rol |
| 5 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/9` | 0.569881 | The most important actions to learn are the **basic actions** (page 408). Specialty basic actions come up less frequently,  and you typically won't look them up until you need them.  **Speaking** (pag |
| 6 | `PZO22001 Starfinder Player Core 388-405::/page/6/Text/16` | 0.568329 | The multiple attack penalty applies only during your turn,  so you don't have to keep track of it if you can perform a  Reactive Strike or a similar reaction that lets you make a  Strike on someone el |
| 7 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/4` | 0.565610 | The most intricate of the modes is **encounter mode**. This  is where most of the intense action takes place, and it's  most often used for combat or other high-stakes situations.  The GM typically sw |
| 8 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/17` | 0.527496 | An effect is the rules term for anything that occurs in the game  world. Effects (page 418) might have limited **Range**, and you  may need to designate **Targets** or create **Areas** for your effect |
| 9 | `PZO22001 Starfinder Player Core 388-405::/page/9/Text/5` | 0.525176 | Often, you'll roll a Perception check to determine your order  in initiative. When you do this, instead of comparing the  result against a DC, the GM will put the results for everyone  in the encounte |
| 10 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/23` | 0.524786 | **Related:** Escape a grab or restraint (page 408), falling (page  413), forced movement (page 414), moving through creatures  (page 414), special movement modes (burrow, climb, fly, and  swim; page 4 |

### Query 52
- Text: What is the rule about The most important actions to learn are the **basic actions** (page 408). Specialty basic actions come up less frequently,  and you typically won't look them up until you need them.  **Speaking** (page 410) normally doesn't take an action.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/2/Text/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 388-405::/page/2/Text/9', 'PZO22001 Starfinder Player Core 388-405::/page/2/Text/8', 'PZO22001 Starfinder Player Core 388-405::/page/2/Text/10']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/2/Text/9', 'PZO22001 Starfinder Player Core 388-405::/page/2/Text/10', 'PZO22001 Starfinder Player Core 388-405::/page/2/Text/8']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 388-405::/page/2/Text/10` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/2/Text/8` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/9` | 1.002856 | The most important actions to learn are the **basic actions** (page 408). Specialty basic actions come up less frequently,  and you typically won't look them up until you need them.  **Speaking** (pag |
| 2 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/8` | 0.611509 | During an encounter, you get 3 actions and 1 reaction per turn  (page 427). Icons indicate whether your abilities take a single  action [one-action], 2 actions [two-actions], 3 actions [three-actions] |
| 3 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/10` | 0.570044 | **Related:** Activities (page 406), disrupting actions (page 407) |
| 4 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/28` | 0.520933 | Your **Perception **modifier (page 396) indicates how good you  are at noticing things around you. You typically use the **Seek** basic action (page 409) to find physical things or the **Sense ** **Mo |
| 5 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/20` | 0.512057 | Your **Speed **(page 412) governs how far you can move. **Stride** (page 410) is an action that has the move trait and allows you to  move a number of feet up to your Speed. You may need to Stride  mu |
| 6 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/26` | 0.498378 | Skill checks are required for all sorts of other tasks related  to adventuring and life in general. Most of their rules are  in Chapter 4 (page 183). You'll find the rules for **calculating ** **skill |
| 7 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/25` | 0.494671 | **Strike** (page 410) actions have the attack trait and allow you  to attack with a weapon you're wielding or an unarmed attack  (such as a tail). If you're using a melee weapon or unarmed  attack, yo |
| 8 | `PZO22001 Starfinder Player Core 388-405::/page/8/Text/19` | 0.492114 | Sometimes you will be called on to attempt a basic saving  throw (or "basic save"). This type of saving throw works  just like any other saving throw—the "basic" part refers to  the effects. For a bas |
| 9 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/23` | 0.490074 | **Related:** Escape a grab or restraint (page 408), falling (page  413), forced movement (page 414), moving through creatures  (page 414), special movement modes (burrow, climb, fly, and  swim; page 4 |
| 10 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/14` | 0.459785 | Sometimes a rule could be interpreted multiple ways. If one  version is too good to be true, it probably is. If a rule seems  to have wording with problematic repercussions or doesn't  work as intende |

### Query 53
- Text: What is the rule about **Related:** Activities (page 406), disrupting actions (page 407)?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/2/Text/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 388-405::/page/2/Text/10', 'PZO22001 Starfinder Player Core 388-405::/page/2/Text/23', 'PZO22001 Starfinder Player Core 388-405::/page/3/Text/24']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/2/Text/10', 'PZO22001 Starfinder Player Core 388-405::/page/2/Text/9', 'PZO22001 Starfinder Player Core 388-405::/page/2/SectionHeader/11']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 388-405::/page/2/Text/9` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/2/SectionHeader/11` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/10` | 0.936928 | **Related:** Activities (page 406), disrupting actions (page 407) |
| 2 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/23` | 0.595736 | **Related:** Escape a grab or restraint (page 408), falling (page  413), forced movement (page 414), moving through creatures  (page 414), special movement modes (burrow, climb, fly, and  swim; page 4 |
| 3 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/24` | 0.579859 | **Related: **Dismiss and Sustain basic actions (page 411) |
| 4 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/9` | 0.545840 | The most important actions to learn are the **basic actions** (page 408). Specialty basic actions come up less frequently,  and you typically won't look them up until you need them.  **Speaking** (pag |
| 5 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/26` | 0.514590 | **Related:** Area Fire (page 410), cover (page 416), flanking  enemies (page 417), spell attacks (page 394), targeting  creatures (page 418) |
| 6 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/8` | 0.485923 | During an encounter, you get 3 actions and 1 reaction per turn  (page 427). Icons indicate whether your abilities take a single  action [one-action], 2 actions [two-actions], 3 actions [three-actions] |
| 7 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/20` | 0.483790 | Your **Speed **(page 412) governs how far you can move. **Stride** (page 410) is an action that has the move trait and allows you to  move a number of feet up to your Speed. You may need to Stride  mu |
| 8 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/4` | 0.480789 | This game presents three main methods of structuring play.  **Encounter mode** (page 427) is highly structured and is most  often used for combat or stressful situations. Everyone in an  encounter rol |
| 9 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/28` | 0.478637 | Your **Perception **modifier (page 396) indicates how good you  are at noticing things around you. You typically use the **Seek** basic action (page 409) to find physical things or the **Sense ** **Mo |
| 10 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/23` | 0.464858 | (page 394). For one that causes its subject to attempt a  saving throw, you'll need your **spell DC** (page 395). |

### Query 54
- Text: What is the rule about ROLLING CHECKS?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/2/SectionHeader/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 388-405::/page/2/SectionHeader/11', 'PZO22001 Starfinder Player Core 388-405::/page/4/SectionHeader/1', 'PZO22001 Starfinder Player Core 388-405::/page/4/Text/6']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/2/SectionHeader/11', 'PZO22001 Starfinder Player Core 388-405::/page/2/Text/12', 'PZO22001 Starfinder Player Core 388-405::/page/2/Text/10']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 388-405::/page/2/Text/12` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/2/Text/10` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 388-405::/page/2/SectionHeader/11` | 0.904464 | ROLLING CHECKS |
| 2 | `PZO22001 Starfinder Player Core 388-405::/page/4/SectionHeader/1` | 0.608694 | CHECKS |
| 3 | `PZO22001 Starfinder Player Core 388-405::/page/4/Text/6` | 0.546948 | All types of checks, from skill checks to attack rolls to saving  throws, follow these basic steps. |
| 4 | `PZO22001 Starfinder Player Core 388-405::/page/9/Text/15` | 0.497157 | The GM can choose to make any check secret, even  if it's not usually rolled secretly. Conversely, the GM  can let you roll any check yourself, even if that check  would usually be secret. Some groups |
| 5 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/12` | 0.484197 | An action that can potentially fail requires rolling a **check** (page 392). Roll a d20 (20-sided die) and identify the modifiers,  bonuses, and penalties that apply. Then, calculate the result,  comp |
| 6 | `PZO22001 Starfinder Player Core 388-405::/page/4/Text/12` | 0.482978 | No matter the details, for any check you must roll the d20  and achieve a result equal to or greater than the DC to succeed.  Each of these steps is explained below. |
| 7 | `PZO22001 Starfinder Player Core 388-405::/page/5/Text/6` | 0.471900 | Whenever you attempt a check, you compare your result  against the **Difficulty Class (DC)** of the check. Your check  succeeds if it's equal to or greater than the DC. If you roll  anything less than |
| 8 | `PZO22001 Starfinder Player Core 388-405::/page/9/Text/12` | 0.462710 | If more than one flat check would ever cause or  prevent the same thing, just roll once and use the  highest DC. In the rare circumstance that a flat check  has a DC of 1 or lower, skip rolling; you a |
| 9 | `PZO22001 Starfinder Player Core 388-405::/page/9/Text/5` | 0.452641 | Often, you'll roll a Perception check to determine your order  in initiative. When you do this, instead of comparing the  result against a DC, the GM will put the results for everyone  in the encounte |
| 10 | `PZO22001 Starfinder Player Core 388-405::/page/10/SectionHeader/10` | 0.445061 | STEP 1: ROLL DAMAGE DICE |

### Query 55
- Text: What is the rule about An action that can potentially fail requires rolling a **check** (page 392). Roll a d20 (20-sided die) and identify the modifiers,  bonuses, and penalties that apply. Then, calculate the result,  compare it to the DC (your target number), and determine the  degree of success and the effect.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/2/Text/12']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 388-405::/page/2/Text/12', 'PZO22001 Starfinder Player Core 388-405::/page/4/Text/12', 'PZO22001 Starfinder Player Core 388-405::/page/4/ListItem/7']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/2/Text/12', 'PZO22001 Starfinder Player Core 388-405::/page/2/Text/13', 'PZO22001 Starfinder Player Core 388-405::/page/2/SectionHeader/11']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 388-405::/page/2/Text/13` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/2/SectionHeader/11` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/12` | 1.000791 | An action that can potentially fail requires rolling a **check** (page 392). Roll a d20 (20-sided die) and identify the modifiers,  bonuses, and penalties that apply. Then, calculate the result,  comp |
| 2 | `PZO22001 Starfinder Player Core 388-405::/page/4/Text/12` | 0.797025 | No matter the details, for any check you must roll the d20  and achieve a result equal to or greater than the DC to succeed.  Each of these steps is explained below. |
| 3 | `PZO22001 Starfinder Player Core 388-405::/page/4/ListItem/7` | 0.758258 | 1. **Roll a d20** and identify the modifiers, bonuses, and  penalties that apply. |
| 4 | `PZO22001 Starfinder Player Core 388-405::/page/5/Text/20` | 0.694477 | If you rolled a 20 on the die (a "natural 20"), your result is one  degree of success better than it would be by numbers alone.  If you roll a 1 on the d20 (a "natural 1"), your result is one  degree |
| 5 | `PZO22001 Starfinder Player Core 388-405::/page/9/Text/11` | 0.675437 | When the likelihood something will happen or fail to  happen is based purely on chance, you'll attempt a flat  check. A flat check never includes any modifiers, bonuses,  or penalties—you just roll a |
| 6 | `PZO22001 Starfinder Player Core 388-405::/page/5/Text/4` | 0.669935 | This step is simple. Add up all the various modifiers, bonuses,  and penalties you identified in Step 1—this is your total  modifier. Next add that to the number that came up on your  d20 roll. This t |
| 7 | `PZO22001 Starfinder Player Core 388-405::/page/5/Text/6` | 0.667885 | Whenever you attempt a check, you compare your result  against the **Difficulty Class (DC)** of the check. Your check  succeeds if it's equal to or greater than the DC. If you roll  anything less than |
| 8 | `PZO22001 Starfinder Player Core 388-405::/page/4/Text/14` | 0.659937 | Start by rolling your d20. You'll then identify all the relevant  modifiers, bonuses, and penalties that apply. A **modifier** can  be either positive or negative, but a **bonus** is always positive, |
| 9 | `PZO22001 Starfinder Player Core 388-405::/page/9/Text/12` | 0.643493 | If more than one flat check would ever cause or  prevent the same thing, just roll once and use the  highest DC. In the rare circumstance that a flat check  has a DC of 1 or lower, skip rolling; you a |
| 10 | `PZO22001 Starfinder Player Core 388-405::/page/5/Text/17` | 0.629279 | You **critically succeed** when the check's result meets or  exceeds the DC by 10 or more. If the check is an attack roll, this  is also known as a critical hit. You can also **critically fail** a che |

### Query 56
- Text: What is the rule about Most checks are modified by your **attribute modifier** (Strength, Dexterity, Constitution, Intelligence, Wisdom, or  Charisma) and your **proficiency modifier** (untrained, trained,  expert, master, or legendary) for the statistic. You might get a  **circumstance**, **status**, or **item** **bonus** or **penalty** as well.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/2/Text/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 388-405::/page/2/Text/13', 'PZO22001 Starfinder Player Core 388-405::/page/4/Text/18', 'PZO22001 Starfinder Player Core 388-405::/page/9/Text/9']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/2/Text/13', 'PZO22001 Starfinder Player Core 388-405::/page/2/Text/12', 'PZO22001 Starfinder Player Core 388-405::/page/2/Text/14']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 388-405::/page/2/Text/12` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/2/Text/14` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/13` | 0.998577 | Most checks are modified by your **attribute modifier** (Strength, Dexterity, Constitution, Intelligence, Wisdom, or  Charisma) and your **proficiency modifier** (untrained, trained,  expert, master, |
| 2 | `PZO22001 Starfinder Player Core 388-405::/page/4/Text/18` | 0.761335 | When attempting a check that involves something you have  some training in, you also add your **proficiency bonus**. This bonus  depends on your proficiency rank: untrained, trained, expert, |
| 3 | `PZO22001 Starfinder Player Core 388-405::/page/9/Text/9` | 0.700617 | You're unlikely to be trained in every skill. As normal,  when using a skill in which you're untrained, your proficiency  bonus is +0; otherwise, it equals your level plus 2 for trained,  or higher on |
| 4 | `PZO22001 Starfinder Player Core 388-405::/page/10/Text/18` | 0.656793 | As with checks, you might add circumstance, status, or item  bonuses to your damage rolls, but if you have multiple bonuses  of the same type, you add only the highest bonus of that type.  Again like |
| 5 | `PZO22001 Starfinder Player Core 388-405::/page/9/Text/16` | 0.647562 | unfavorable situations might give you a circumstance penalty  to your skill check, while harmful spells, magic, or conditions  might also impose a status penalty. Using shoddy or makeshift  tools migh |
| 6 | `PZO22001 Starfinder Player Core 388-405::/page/4/Text/16` | 0.636744 | Nearly all checks allow you to add an **attribute** **modifier** to  the roll. Attribute modifiers represent your raw capability and  are described on page 19. Exactly which attribute modifier  you us |
| 7 | `PZO22001 Starfinder Player Core 388-405::/page/9/Text/8` | 0.636339 | **Skill check result = d20 roll + the skill's key attribute ** **modifier + proficiency bonus + other bonuses + penalties** |
| 8 | `PZO22001 Starfinder Player Core 388-405::/page/8/Text/2` | 0.635741 | When creating your character and adventuring you'll  record the total modifier for various important checks  on your character sheet. Since many bonuses and  penalties are due to the immediate circums |
| 9 | `PZO22001 Starfinder Player Core 388-405::/page/4/Text/19` | 0.625131 | master, or legendary. If you're untrained, your bonus is +0—you  must rely on raw talent and any situational bonuses. Otherwise,  the bonus equals your character's level plus a certain amount  dependi |
| 10 | `PZO22001 Starfinder Player Core 388-405::/page/8/Text/3` | 0.621003 | For example, the number you write down for  your **attack modifier** with your doshko would likely  be your Strength modifier + your proficiency bonus  with martial weapons. Your **spell attack modifi |

### Query 57
- Text: What is the rule about The **degrees of success** (page 393) are critical success,  success, failure, and critical failure. You get a success if you  meet or exceed the DC, or a critical success if you exceed the  DC by 10 or more. If your result is lower than the DC, you get a  failure, or a critical failure if you failed by 10 or more.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/2/Text/14']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 388-405::/page/2/Text/14', 'PZO22001 Starfinder Player Core 388-405::/page/5/Text/17', 'PZO22001 Starfinder Player Core 388-405::/page/15/Text/5']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/2/Text/14', 'PZO22001 Starfinder Player Core 388-405::/page/2/Text/15', 'PZO22001 Starfinder Player Core 388-405::/page/2/Text/13']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 388-405::/page/2/Text/15` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/2/Text/13` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/14` | 0.992424 | The **degrees of success** (page 393) are critical success,  success, failure, and critical failure. You get a success if you  meet or exceed the DC, or a critical success if you exceed the  DC by 10 |
| 2 | `PZO22001 Starfinder Player Core 388-405::/page/5/Text/17` | 0.757794 | You **critically succeed** when the check's result meets or  exceeds the DC by 10 or more. If the check is an attack roll, this  is also known as a critical hit. You can also **critically fail** a che |
| 3 | `PZO22001 Starfinder Player Core 388-405::/page/15/Text/5` | 0.687517 | **Critical Success** Your dying value is reduced by 2. **Success** Your dying value is reduced by 1. **Failure** Your dying value increases by 1. **Critical Failure** Your dying value increases by 2. |
| 4 | `PZO22001 Starfinder Player Core 388-405::/page/5/Text/18` | 0.641200 | Some actions and abilities have stronger effects on a critical  success or failure. For example, a Strike deals double damage  on a critical hit. If an effect doesn't list a critical success effect, |
| 5 | `PZO22001 Starfinder Player Core 388-405::/page/5/Text/6` | 0.640935 | Whenever you attempt a check, you compare your result  against the **Difficulty Class (DC)** of the check. Your check  succeeds if it's equal to or greater than the DC. If you roll  anything less than |
| 6 | `PZO22001 Starfinder Player Core 388-405::/page/5/Text/20` | 0.628744 | If you rolled a 20 on the die (a "natural 20"), your result is one  degree of success better than it would be by numbers alone.  If you roll a 1 on the d20 (a "natural 1"), your result is one  degree |
| 7 | `PZO22001 Starfinder Player Core 388-405::/page/5/Text/16` | 0.626440 | succeed or fail, but also how spectacularly you succeed or  fail. Exceptional results—either good or bad—can cause you to  critically succeed or critically fail at a check. |
| 8 | `PZO22001 Starfinder Player Core 388-405::/page/4/ListItem/10` | 0.621300 | 4. Determine the **degree of success** and the effect. |
| 9 | `PZO22001 Starfinder Player Core 388-405::/page/8/Text/20` | 0.620682 | **Critical Success** You take no damage from the effect. **Success** You take half the listed damage from the effect. **Failure** You take the full damage listed from the effect. **Critical Failure** |
| 10 | `PZO22001 Starfinder Player Core 388-405::/page/5/SectionHeader/10` | 0.580911 | STEP 4: DEGREES OF  SUCCESS |

### Query 58
- Text: What is the rule about **Related:** Flat checks and secret checks (sidebar on page  397), fortune and misfortune (sidebar on page 393)?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/2/Text/15']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 388-405::/page/2/Text/15', 'PZO22001 Starfinder Player Core 388-405::/page/9/Text/14', 'PZO22001 Starfinder Player Core 388-405::/page/9/Text/11']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/2/Text/15', 'PZO22001 Starfinder Player Core 388-405::/page/2/SectionHeader/16', 'PZO22001 Starfinder Player Core 388-405::/page/2/Text/14']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 388-405::/page/2/SectionHeader/16` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/2/Text/14` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/15` | 0.926360 | **Related:** Flat checks and secret checks (sidebar on page  397), fortune and misfortune (sidebar on page 393) |
| 2 | `PZO22001 Starfinder Player Core 388-405::/page/9/Text/14` | 0.592030 | Sometimes you as the player shouldn't know the exact  result and effect of a check. In these situations, the rules  (or the GM) will call for a secret check. The secret trait  appears on anything that |
| 3 | `PZO22001 Starfinder Player Core 388-405::/page/9/Text/11` | 0.568501 | When the likelihood something will happen or fail to  happen is based purely on chance, you'll attempt a flat  check. A flat check never includes any modifiers, bonuses,  or penalties—you just roll a |
| 4 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/6` | 0.519012 | A core principle of Starfinder is that specific rules override  general ones. If two rules conflict, the more specific  one takes precedence. If there's still ambiguity, the GM  determines which rule |
| 5 | `PZO22001 Starfinder Player Core 388-405::/page/5/Text/14` | 0.516967 | You can never have more than one fortune effect  or misfortune effect come into play on a single roll.  For instance, if an effect lets you roll twice and use  the higher roll, you can't then use Meye |
| 6 | `PZO22001 Starfinder Player Core 388-405::/page/5/Text/15` | 0.508717 | If both a fortune effect and a misfortune effect  would apply to the same roll, the two cancel each  other out, and you roll normally. |
| 7 | `PZO22001 Starfinder Player Core 388-405::/page/13/Text/12` | 0.502260 | of which are described in the sidebar on page 39, and on  pages 448 and 456. |
| 8 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/26` | 0.490301 | Skill checks are required for all sorts of other tasks related  to adventuring and life in general. Most of their rules are  in Chapter 4 (page 183). You'll find the rules for **calculating ** **skill |
| 9 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/26` | 0.486576 | **Related:** Area Fire (page 410), cover (page 416), flanking  enemies (page 417), spell attacks (page 394), targeting  creatures (page 418) |
| 10 | `PZO22001 Starfinder Player Core 388-405::/page/4/Text/18` | 0.480543 | When attempting a check that involves something you have  some training in, you also add your **proficiency bonus**. This bonus  depends on your proficiency rank: untrained, trained, expert, |

### Query 59
- Text: Summarize EFFECTS
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/2/SectionHeader/16']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 388-405::/page/2/SectionHeader/16', 'PZO22001 Starfinder Player Core 388-405::/page/11/Text/31', 'PZO22001 Starfinder Player Core 388-405::/page/15/Text/35']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/2/SectionHeader/16', 'PZO22001 Starfinder Player Core 388-405::/page/2/Text/15', 'PZO22001 Starfinder Player Core 388-405::/page/2/Text/17']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 388-405::/page/2/Text/15` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/2/Text/17` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 388-405::/page/2/SectionHeader/16` | 0.932141 | EFFECTS |
| 2 | `PZO22001 Starfinder Player Core 388-405::/page/11/Text/31` | 0.830668 | **Effects** |
| 3 | `PZO22001 Starfinder Player Core 388-405::/page/15/Text/35` | 0.830668 | **Effects** |
| 4 | `PZO22001 Starfinder Player Core 388-405::/page/7/Text/30` | 0.788668 | **Effects** |
| 5 | `PZO22001 Starfinder Player Core 388-405::/page/5/Text/33` | 0.788668 | **Effects** |
| 6 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/49` | 0.788668 | **Effects** |
| 7 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/38` | 0.666458 | **Effects** **Area** |
| 8 | `PZO22001 Starfinder Player Core 388-405::/page/13/Text/42` | 0.666458 | **Effects** **Area** |
| 9 | `PZO22001 Starfinder Player Core 388-405::/page/17/Text/27` | 0.666458 | **Effects** **Area** |
| 10 | `PZO22001 Starfinder Player Core 388-405::/page/9/Text/36` | 0.666458 | **Effects** **Area** |

### Query 60
- Text: Summarize An effect is the rules term for anything that occurs in the game  world. Effects (page 418) might have limited **Range**, and you  may need to designate **Targets** or create **Areas** for your effects.  Areas include bursts from a single point, cones blasting out  from you, emanations surrounding you or another creature, or  straight lines.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/2/Text/17']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 388-405::/page/2/Text/17', 'PZO22001 Starfinder Player Core 388-405::/page/17/Text/27', 'PZO22001 Starfinder Player Core 388-405::/page/13/Text/42']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/2/Text/17', 'PZO22001 Starfinder Player Core 388-405::/page/2/SectionHeader/16', 'PZO22001 Starfinder Player Core 388-405::/page/2/Text/18']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 388-405::/page/2/SectionHeader/16` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/2/Text/18` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/17` | 1.045768 | An effect is the rules term for anything that occurs in the game  world. Effects (page 418) might have limited **Range**, and you  may need to designate **Targets** or create **Areas** for your effect |
| 2 | `PZO22001 Starfinder Player Core 388-405::/page/17/Text/27` | 0.672080 | **Effects** **Area** |
| 3 | `PZO22001 Starfinder Player Core 388-405::/page/13/Text/42` | 0.672080 | **Effects** **Area** |
| 4 | `PZO22001 Starfinder Player Core 388-405::/page/9/Text/36` | 0.630080 | **Effects** **Area** |
| 5 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/38` | 0.630080 | **Effects** **Area** |
| 6 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/18` | 0.621415 | Effects that last for a period of time list a **Duration** (page  418). These can last a set increment of time, or can end if  certain requirements are met. Many effects apply **conditions** (page 419 |
| 7 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/26` | 0.539322 | **Related:** Area Fire (page 410), cover (page 416), flanking  enemies (page 417), spell attacks (page 394), targeting  creatures (page 418) |
| 8 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/8` | 0.533290 | During an encounter, you get 3 actions and 1 reaction per turn  (page 427). Icons indicate whether your abilities take a single  action [one-action], 2 actions [two-actions], 3 actions [three-actions] |
| 9 | `PZO22001 Starfinder Player Core 388-405::/page/10/ListItem/6` | 0.519148 | 1. **Roll damage dice** indicated by the weapon, unarmed attack,  or spell, and apply the modifiers, bonuses, and penalties  that apply to the result of the roll. |
| 10 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/25` | 0.517476 | **Strike** (page 410) actions have the attack trait and allow you  to attack with a weapon you're wielding or an unarmed attack  (such as a tail). If you're using a melee weapon or unarmed  attack, yo |

### Query 61
- Text: Summarize Effects that last for a period of time list a **Duration** (page  418). These can last a set increment of time, or can end if  certain requirements are met. Many effects apply **conditions** (page 419), which measure advantages or impediments like  being blinded, frightened, or invisible.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/2/Text/18']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 388-405::/page/2/Text/18', 'PZO22001 Starfinder Player Core 388-405::/page/2/Text/17', 'PZO22001 Starfinder Player Core 388-405::/page/12/Text/12']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/2/Text/18', 'PZO22001 Starfinder Player Core 388-405::/page/2/SectionHeader/19', 'PZO22001 Starfinder Player Core 388-405::/page/2/Text/17']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 388-405::/page/2/SectionHeader/19` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/2/Text/17` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/18` | 1.037668 | Effects that last for a period of time list a **Duration** (page  418). These can last a set increment of time, or can end if  certain requirements are met. Many effects apply **conditions** (page 419 |
| 2 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/17` | 0.647720 | An effect is the rules term for anything that occurs in the game  world. Effects (page 418) might have limited **Range**, and you  may need to designate **Targets** or create **Areas** for your effect |
| 3 | `PZO22001 Starfinder Player Core 388-405::/page/12/Text/12` | 0.624060 | Some effects grant you immunity to the same effect for a set  amount of time. If an effect grants you temporary immunity,  repeated applications of that effect don't affect you for as  long as the tem |
| 4 | `PZO22001 Starfinder Player Core 388-405::/page/11/Text/31` | 0.510692 | **Effects** |
| 5 | `PZO22001 Starfinder Player Core 388-405::/page/15/Text/35` | 0.510692 | **Effects** |
| 6 | `PZO22001 Starfinder Player Core 388-405::/page/7/Text/30` | 0.510692 | **Effects** |
| 7 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/49` | 0.510692 | **Effects** |
| 8 | `PZO22001 Starfinder Player Core 388-405::/page/5/Text/33` | 0.510692 | **Effects** |
| 9 | `PZO22001 Starfinder Player Core 388-405::/page/16/Text/2` | 0.503000 | The effects of the dying condition are described under the Dying header on page 403, but you might also need to  reference the unconscious, wounded, and doomed conditions. |
| 10 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/19` | 0.495687 | Damage reduces the **Hit Points (HP)** (page 402) that  measure a creature's overall health or an object's durability.  A creature might have **immunity** to damage or effects of  certain kinds, a **r |

### Query 62
- Text: Summarize MOVEMENT
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/2/SectionHeader/19']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 388-405::/page/2/SectionHeader/19', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/37', 'PZO22001 Starfinder Player Core 388-405::/page/15/Text/34']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/2/SectionHeader/19', 'PZO22001 Starfinder Player Core 388-405::/page/2/Text/18', 'PZO22001 Starfinder Player Core 388-405::/page/2/Text/20']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 388-405::/page/2/Text/18` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/2/Text/20` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 388-405::/page/2/SectionHeader/19` | 0.889500 | MOVEMENT |
| 2 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/37` | 0.727272 | **Movement** |
| 3 | `PZO22001 Starfinder Player Core 388-405::/page/15/Text/34` | 0.727272 | **Movement** |
| 4 | `PZO22001 Starfinder Player Core 388-405::/page/11/Text/30` | 0.685272 | **Movement** |
| 5 | `PZO22001 Starfinder Player Core 388-405::/page/5/Text/32` | 0.685272 | **Movement** |
| 6 | `PZO22001 Starfinder Player Core 388-405::/page/13/Text/41` | 0.685272 | **Movement** |
| 7 | `PZO22001 Starfinder Player Core 388-405::/page/7/Text/29` | 0.685272 | **Movement** |
| 8 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/48` | 0.685272 | **Movement** |
| 9 | `PZO22001 Starfinder Player Core 388-405::/page/17/Text/26` | 0.685272 | **Movement** |
| 10 | `PZO22001 Starfinder Player Core 388-405::/page/9/Text/35` | 0.685272 | **Movement** |

### Query 63
- Text: What is the rule about Your **Speed **(page 412) governs how far you can move. **Stride** (page 410) is an action that has the move trait and allows you to  move a number of feet up to your Speed. You may need to Stride  multiple times in a turn! Move actions can often trigger reactions  or free actions. However, unlike other actions, a move action can  **Trigger** reactions not only when you first use the action, but also  for every 5 feet you move during that action (page 414). The **Step** action (page 410) lets you move without triggering reactions,  but only 5 feet. Other basic actions with the move trait include  **Crawl**, **Drop Prone**, and **Stand** (pages 408–410).?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/2/Text/20']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 388-405::/page/2/Text/20', 'PZO22001 Starfinder Player Core 388-405::/page/2/Text/25', 'PZO22001 Starfinder Player Core 388-405::/page/2/Text/8']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/2/Text/20', 'PZO22001 Starfinder Player Core 388-405::/page/2/Text/21', 'PZO22001 Starfinder Player Core 388-405::/page/2/SectionHeader/19']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 388-405::/page/2/Text/21` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/2/SectionHeader/19` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/20` | 1.027670 | Your **Speed **(page 412) governs how far you can move. **Stride** (page 410) is an action that has the move trait and allows you to  move a number of feet up to your Speed. You may need to Stride  mu |
| 2 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/25` | 0.672084 | **Strike** (page 410) actions have the attack trait and allow you  to attack with a weapon you're wielding or an unarmed attack  (such as a tail). If you're using a melee weapon or unarmed  attack, yo |
| 3 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/8` | 0.671891 | During an encounter, you get 3 actions and 1 reaction per turn  (page 427). Icons indicate whether your abilities take a single  action [one-action], 2 actions [two-actions], 3 actions [three-actions] |
| 4 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/23` | 0.622924 | **Related:** Escape a grab or restraint (page 408), falling (page  413), forced movement (page 414), moving through creatures  (page 414), special movement modes (burrow, climb, fly, and  swim; page 4 |
| 5 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/21` | 0.619592 | This game measures **movement** on a grid (page 413). **Difficult ** **terrain** and other types of terrain (page 415) may impede your  movement, while elevation is relevant to flying creatures. |
| 6 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/5` | 0.564206 | **Exploration** **mode** (page 430) takes place over minutes or  hours. You use your travel Speed if you're moving, and you  engage in **exploration** **activities** like Avoiding Notice, Detecting  M |
| 7 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/9` | 0.522225 | The most important actions to learn are the **basic actions** (page 408). Specialty basic actions come up less frequently,  and you typically won't look them up until you need them.  **Speaking** (pag |
| 8 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/28` | 0.505472 | Your **Perception **modifier (page 396) indicates how good you  are at noticing things around you. You typically use the **Seek** basic action (page 409) to find physical things or the **Sense ** **Mo |
| 9 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/4` | 0.505007 | This game presents three main methods of structuring play.  **Encounter mode** (page 427) is highly structured and is most  often used for combat or stressful situations. Everyone in an  encounter rol |
| 10 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/17` | 0.494877 | An effect is the rules term for anything that occurs in the game  world. Effects (page 418) might have limited **Range**, and you  may need to designate **Targets** or create **Areas** for your effect |

### Query 64
- Text: Summarize This game measures **movement** on a grid (page 413). **Difficult ** **terrain** and other types of terrain (page 415) may impede your  movement, while elevation is relevant to flying creatures.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/2/Text/21']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 388-405::/page/2/Text/21', 'PZO22001 Starfinder Player Core 388-405::/page/2/Text/23', 'PZO22001 Starfinder Player Core 388-405::/page/2/Text/20']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/2/Text/21', 'PZO22001 Starfinder Player Core 388-405::/page/2/Text/20', 'PZO22001 Starfinder Player Core 388-405::/page/2/Text/22']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 388-405::/page/2/Text/20` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/2/Text/22` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/21` | 1.044927 | This game measures **movement** on a grid (page 413). **Difficult ** **terrain** and other types of terrain (page 415) may impede your  movement, while elevation is relevant to flying creatures. |
| 2 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/23` | 0.684763 | **Related:** Escape a grab or restraint (page 408), falling (page  413), forced movement (page 414), moving through creatures  (page 414), special movement modes (burrow, climb, fly, and  swim; page 4 |
| 3 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/20` | 0.650149 | Your **Speed **(page 412) governs how far you can move. **Stride** (page 410) is an action that has the move trait and allows you to  move a number of feet up to your Speed. You may need to Stride  mu |
| 4 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/22` | 0.512142 | Creatures can get tactical advantages by careful positioning.  The most common are using **cover** from terrain and other  creatures to increase your AC (page 416), and **flanking** (page  417), which |
| 5 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/5` | 0.510909 | **Exploration** **mode** (page 430) takes place over minutes or  hours. You use your travel Speed if you're moving, and you  engage in **exploration** **activities** like Avoiding Notice, Detecting  M |
| 6 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/17` | 0.496300 | An effect is the rules term for anything that occurs in the game  world. Effects (page 418) might have limited **Range**, and you  may need to designate **Targets** or create **Areas** for your effect |
| 7 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/26` | 0.491529 | **Related:** Area Fire (page 410), cover (page 416), flanking  enemies (page 417), spell attacks (page 394), targeting  creatures (page 418) |
| 8 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/29` | 0.479480 | Four main conditions indicate how well you can pinpoint  and target a creature: **observed**, **hidden**, **undetected**, and  **unnoticed** (page 425). A creature with the **concealed** or  **invisib |
| 9 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/4` | 0.475426 | This game presents three main methods of structuring play.  **Encounter mode** (page 427) is highly structured and is most  often used for combat or stressful situations. Everyone in an  encounter rol |
| 10 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/19` | 0.471780 | Damage reduces the **Hit Points (HP)** (page 402) that  measure a creature's overall health or an object's durability.  A creature might have **immunity** to damage or effects of  certain kinds, a **r |

### Query 65
- Text: What is the rule about Creatures can get tactical advantages by careful positioning.  The most common are using **cover** from terrain and other  creatures to increase your AC (page 416), and **flanking** (page  417), which requires you and an ally to be on the opposite sides  of an enemy to reduce the enemy's AC.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/2/Text/22']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 388-405::/page/2/Text/22', 'PZO22001 Starfinder Player Core 388-405::/page/2/Text/26', 'PZO22001 Starfinder Player Core 388-405::/page/3/Text/6']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/2/Text/22', 'PZO22001 Starfinder Player Core 388-405::/page/2/Text/21', 'PZO22001 Starfinder Player Core 388-405::/page/2/Text/23']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 388-405::/page/2/Text/21` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/2/Text/23` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/22` | 1.007335 | Creatures can get tactical advantages by careful positioning.  The most common are using **cover** from terrain and other  creatures to increase your AC (page 416), and **flanking** (page  417), which |
| 2 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/26` | 0.611939 | **Related:** Area Fire (page 410), cover (page 416), flanking  enemies (page 417), spell attacks (page 394), targeting  creatures (page 418) |
| 3 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/6` | 0.576663 | A core principle of Starfinder is that specific rules override  general ones. If two rules conflict, the more specific  one takes precedence. If there's still ambiguity, the GM  determines which rule |
| 4 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/25` | 0.544798 | **Strike** (page 410) actions have the attack trait and allow you  to attack with a weapon you're wielding or an unarmed attack  (such as a tail). If you're using a melee weapon or unarmed  attack, yo |
| 5 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/29` | 0.513961 | Four main conditions indicate how well you can pinpoint  and target a creature: **observed**, **hidden**, **undetected**, and  **unnoticed** (page 425). A creature with the **concealed** or  **invisib |
| 6 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/16` | 0.504826 | Your **Armor Class** **(AC) **(page 395) is the main DC used for  attacks against you. You might also roll a type of check called  a **Saving Throw** (page 396), also called a **save**, against spells |
| 7 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/21` | 0.500153 | This game measures **movement** on a grid (page 413). **Difficult ** **terrain** and other types of terrain (page 415) may impede your  movement, while elevation is relevant to flying creatures. |
| 8 | `PZO22001 Starfinder Player Core 388-405::/page/4/Text/22` | 0.497888 | **Circumstance bonuses** involve the situation you find yourself  in when attempting a check. For instance, using Raise a Shield  with a compact shield grants you a +1 circumstance bonus to AC.  Being |
| 9 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/23` | 0.494625 | **Related:** Escape a grab or restraint (page 408), falling (page  413), forced movement (page 414), moving through creatures  (page 414), special movement modes (burrow, climb, fly, and  swim; page 4 |
| 10 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/22` | 0.493998 | Most of the rules for casting spells are in Chapter 7 (pages  294–301). For a spell that requires an attack roll against  the target's AC, you'll calculate your **spell attack modifier** |

### Query 66
- Text: Summarize **Related:** Escape a grab or restraint (page 408), falling (page  413), forced movement (page 414), moving through creatures  (page 414), special movement modes (burrow, climb, fly, and  swim; page 412), travel speed outside of encounters (page 430),  untethered (page 441)
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/2/Text/23']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 388-405::/page/2/Text/23', 'PZO22001 Starfinder Player Core 388-405::/page/2/Text/21', 'PZO22001 Starfinder Player Core 388-405::/page/2/Text/20']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/2/Text/23', 'PZO22001 Starfinder Player Core 388-405::/page/2/Text/22', 'PZO22001 Starfinder Player Core 388-405::/page/2/SectionHeader/24']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 388-405::/page/2/Text/22` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/2/SectionHeader/24` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/23` | 1.043944 | **Related:** Escape a grab or restraint (page 408), falling (page  413), forced movement (page 414), moving through creatures  (page 414), special movement modes (burrow, climb, fly, and  swim; page 4 |
| 2 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/21` | 0.687168 | This game measures **movement** on a grid (page 413). **Difficult ** **terrain** and other types of terrain (page 415) may impede your  movement, while elevation is relevant to flying creatures. |
| 3 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/20` | 0.674780 | Your **Speed **(page 412) governs how far you can move. **Stride** (page 410) is an action that has the move trait and allows you to  move a number of feet up to your Speed. You may need to Stride  mu |
| 4 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/5` | 0.631780 | **Exploration** **mode** (page 430) takes place over minutes or  hours. You use your travel Speed if you're moving, and you  engage in **exploration** **activities** like Avoiding Notice, Detecting  M |
| 5 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/26` | 0.601108 | **Related:** Area Fire (page 410), cover (page 416), flanking  enemies (page 417), spell attacks (page 394), targeting  creatures (page 418) |
| 6 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/10` | 0.589636 | **Related:** Activities (page 406), disrupting actions (page 407) |
| 7 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/8` | 0.564375 | During an encounter, you get 3 actions and 1 reaction per turn  (page 427). Icons indicate whether your abilities take a single  action [one-action], 2 actions [two-actions], 3 actions [three-actions] |
| 8 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/29` | 0.547308 | Four main conditions indicate how well you can pinpoint  and target a creature: **observed**, **hidden**, **undetected**, and  **unnoticed** (page 425). A creature with the **concealed** or  **invisib |
| 9 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/4` | 0.535950 | This game presents three main methods of structuring play.  **Encounter mode** (page 427) is highly structured and is most  often used for combat or stressful situations. Everyone in an  encounter rol |
| 10 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/28` | 0.533306 | Your **Perception **modifier (page 396) indicates how good you  are at noticing things around you. You typically use the **Seek** basic action (page 409) to find physical things or the **Sense ** **Mo |

### Query 67
- Text: What is the rule about ATTACKING?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/2/SectionHeader/24']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 388-405::/page/2/SectionHeader/24', 'PZO22001 Starfinder Player Core 388-405::/page/6/TableCell/354', 'PZO22001 Starfinder Player Core 388-405::/page/11/SectionHeader/12']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/2/SectionHeader/24', 'PZO22001 Starfinder Player Core 388-405::/page/2/Text/23', 'PZO22001 Starfinder Player Core 388-405::/page/2/Text/25']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 388-405::/page/2/Text/23` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/2/Text/25` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 388-405::/page/2/SectionHeader/24` | 0.800297 | ATTACKING |
| 2 | `PZO22001 Starfinder Player Core 388-405::/page/6/TableCell/354` | 0.572967 | Attack |
| 3 | `PZO22001 Starfinder Player Core 388-405::/page/11/SectionHeader/12` | 0.560932 | NONLETHAL ATTACKS |
| 4 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/25` | 0.512308 | **Strike** (page 410) actions have the attack trait and allow you  to attack with a weapon you're wielding or an unarmed attack  (such as a tail). If you're using a melee weapon or unarmed  attack, yo |
| 5 | `PZO22001 Starfinder Player Core 388-405::/page/6/SectionHeader/2` | 0.471235 | ATTACK ROLLS |
| 6 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/22` | 0.447675 | Most of the rules for casting spells are in Chapter 7 (pages  294–301). For a spell that requires an attack roll against  the target's AC, you'll calculate your **spell attack modifier** |
| 7 | `PZO22001 Starfinder Player Core 388-405::/page/2/SectionHeader/1` | 0.441259 | RULES OVERVIEW |
| 8 | `PZO22001 Starfinder Player Core 388-405::/page/6/Text/10` | 0.441069 | Penalties to attack rolls come from situations and effects  as well. Circumstance penalties come from risky tactics or  detrimental circumstances, status penalties come from spells  and magic working |
| 9 | `PZO22001 Starfinder Player Core 388-405::/page/6/TableCell/355` | 0.440581 | Multiple Attack Penalty |
| 10 | `PZO22001 Starfinder Player Core 388-405::/page/6/Text/16` | 0.437961 | The multiple attack penalty applies only during your turn,  so you don't have to keep track of it if you can perform a  Reactive Strike or a similar reaction that lets you make a  Strike on someone el |

### Query 68
- Text: What is the rule about **Strike** (page 410) actions have the attack trait and allow you  to attack with a weapon you're wielding or an unarmed attack  (such as a tail). If you're using a melee weapon or unarmed  attack, your target must be within your **reach** (page 413); if  you're attacking with a ranged weapon, your target must  be within your **Range **(page 418). Ranged weapons get less  effective as you exceed their **range increments**. Striking  multiple times in a turn has diminishing returns. A **multiple ** **attack penalty** (page 394) applies to each attack after the first.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/2/Text/25']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 388-405::/page/2/Text/25', 'PZO22001 Starfinder Player Core 388-405::/page/6/Text/18', 'PZO22001 Starfinder Player Core 388-405::/page/6/Text/15']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/2/Text/25', 'PZO22001 Starfinder Player Core 388-405::/page/2/Text/26', 'PZO22001 Starfinder Player Core 388-405::/page/2/SectionHeader/24']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 388-405::/page/2/Text/26` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/2/SectionHeader/24` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/25` | 1.003836 | **Strike** (page 410) actions have the attack trait and allow you  to attack with a weapon you're wielding or an unarmed attack  (such as a tail). If you're using a melee weapon or unarmed  attack, yo |
| 2 | `PZO22001 Starfinder Player Core 388-405::/page/6/Text/18` | 0.729258 | Ranged and thrown weapons each have a listed **Range ** increment, and attacks with them grow less accurate against  targets farther away (range and range increments are  covered in depth on page 254) |
| 3 | `PZO22001 Starfinder Player Core 388-405::/page/6/Text/15` | 0.717604 | Always calculate your multiple attack penalty based on  the weapon you're using on that attack, not ones you used  on previous attacks. For example, let's say you're wielding a  plasma sword in one ha |
| 4 | `PZO22001 Starfinder Player Core 388-405::/page/6/Text/16` | 0.682074 | The multiple attack penalty applies only during your turn,  so you don't have to keep track of it if you can perform a  Reactive Strike or a similar reaction that lets you make a  Strike on someone el |
| 5 | `PZO22001 Starfinder Player Core 388-405::/page/6/Text/12` | 0.659230 | The more attacks you make beyond your first in a single turn, the  less accurate you become, represented by the **multiple attack ** **penalty**. The second time you use an attack action during your |
| 6 | `PZO22001 Starfinder Player Core 388-405::/page/6/Text/10` | 0.647702 | Penalties to attack rolls come from situations and effects  as well. Circumstance penalties come from risky tactics or  detrimental circumstances, status penalties come from spells  and magic working |
| 7 | `PZO22001 Starfinder Player Core 388-405::/page/5/Text/1` | 0.575549 | Unlike bonuses, penalties can also be **untyped**, in which case  they won't be classified as "circumstance," "item," or "status."  Unlike other penalties, you always add all your untyped penalties  t |
| 8 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/20` | 0.571051 | Your **Speed **(page 412) governs how far you can move. **Stride** (page 410) is an action that has the move trait and allows you to  move a number of feet up to your Speed. You may need to Stride  mu |
| 9 | `PZO22001 Starfinder Player Core 388-405::/page/6/Text/3` | 0.570021 | When you use a Strike action or make a spell attack, you  attempt a check called an attack roll. Attack rolls take a  variety of forms and are often highly variable based on the  weapon you are using |
| 10 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/8` | 0.555532 | During an encounter, you get 3 actions and 1 reaction per turn  (page 427). Icons indicate whether your abilities take a single  action [one-action], 2 actions [two-actions], 3 actions [three-actions] |

### Query 69
- Text: What is the rule about **Related:** Area Fire (page 410), cover (page 416), flanking  enemies (page 417), spell attacks (page 394), targeting  creatures (page 418)?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/2/Text/26']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 388-405::/page/2/Text/26', 'PZO22001 Starfinder Player Core 388-405::/page/2/Text/25', 'PZO22001 Starfinder Player Core 388-405::/page/2/Text/22']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/2/Text/26', 'PZO22001 Starfinder Player Core 388-405::/page/3/SectionHeader/1', 'PZO22001 Starfinder Player Core 388-405::/page/2/Text/25']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 388-405::/page/3/SectionHeader/1` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/2/Text/25` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/26` | 0.895723 | **Related:** Area Fire (page 410), cover (page 416), flanking  enemies (page 417), spell attacks (page 394), targeting  creatures (page 418) |
| 2 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/25` | 0.636335 | **Strike** (page 410) actions have the attack trait and allow you  to attack with a weapon you're wielding or an unarmed attack  (such as a tail). If you're using a melee weapon or unarmed  attack, yo |
| 3 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/22` | 0.612779 | Creatures can get tactical advantages by careful positioning.  The most common are using **cover** from terrain and other  creatures to increase your AC (page 416), and **flanking** (page  417), which |
| 4 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/17` | 0.565258 | An effect is the rules term for anything that occurs in the game  world. Effects (page 418) might have limited **Range**, and you  may need to designate **Targets** or create **Areas** for your effect |
| 5 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/23` | 0.548062 | **Related:** Escape a grab or restraint (page 408), falling (page  413), forced movement (page 414), moving through creatures  (page 414), special movement modes (burrow, climb, fly, and  swim; page 4 |
| 6 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/22` | 0.545198 | Most of the rules for casting spells are in Chapter 7 (pages  294–301). For a spell that requires an attack roll against  the target's AC, you'll calculate your **spell attack modifier** |
| 7 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/18` | 0.530707 | Attacks, spells, and other dangers **deal damage** (page 398).  The amount is typically determined by a **Damage **roll (page  398), which can use a variety of sizes and numbers of dice. |
| 8 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/6` | 0.524663 | A core principle of Starfinder is that specific rules override  general ones. If two rules conflict, the more specific  one takes precedence. If there's still ambiguity, the GM  determines which rule |
| 9 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/29` | 0.512912 | Four main conditions indicate how well you can pinpoint  and target a creature: **observed**, **hidden**, **undetected**, and  **unnoticed** (page 425). A creature with the **concealed** or  **invisib |
| 10 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/26` | 0.509586 | Skill checks are required for all sorts of other tasks related  to adventuring and life in general. Most of their rules are  in Chapter 4 (page 183). You'll find the rules for **calculating ** **skill |

### Query 70
- Text: Summarize **GAME CONVENTIONS**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/3/SectionHeader/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 388-405::/page/3/SectionHeader/1', 'PZO22001 Starfinder Player Core 388-405::/page/11/Text/22', 'PZO22001 Starfinder Player Core 388-405::/page/7/Text/20']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/3/SectionHeader/1', 'PZO22001 Starfinder Player Core 388-405::/page/2/Text/26', 'PZO22001 Starfinder Player Core 388-405::/page/3/Text/2']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 388-405::/page/2/Text/26` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/3/Text/2` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 388-405::/page/3/SectionHeader/1` | 0.989445 | **GAME CONVENTIONS** |
| 2 | `PZO22001 Starfinder Player Core 388-405::/page/11/Text/22` | 0.543109 | **GAME** **Rules Overview** |
| 3 | `PZO22001 Starfinder Player Core 388-405::/page/7/Text/20` | 0.462505 | **PLAYING THE ** **GAME** |
| 4 | `PZO22001 Starfinder Player Core 388-405::/page/9/Text/26` | 0.420505 | **PLAYING THE ** **GAME** |
| 5 | `PZO22001 Starfinder Player Core 388-405::/page/5/Text/23` | 0.420505 | **PLAYING THE ** **GAME** |
| 6 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/28` | 0.420505 | **PLAYING THE ** **GAME** |
| 7 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/39` | 0.420505 | **PLAYING THE ** **GAME** |
| 8 | `PZO22001 Starfinder Player Core 388-405::/page/13/Text/32` | 0.420505 | **PLAYING THE ** **GAME** |
| 9 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/4` | 0.416490 | This game presents three main methods of structuring play.  **Encounter mode** (page 427) is highly structured and is most  often used for combat or stressful situations. Everyone in an  encounter rol |
| 10 | `PZO22001 Starfinder Player Core 388-405::/page/7/Text/21` | 0.411810 | **Rules Overview** |

### Query 71
- Text: Summarize Starfinder has many specific rules, but you'll also want to keep these general guidelines in mind when playing.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/3/Text/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 388-405::/page/3/Text/2', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/1', 'PZO22001 Starfinder Player Core 388-405::/page/3/Text/4']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/3/Text/2', 'PZO22001 Starfinder Player Core 388-405::/page/3/SectionHeader/1', 'PZO22001 Starfinder Player Core 388-405::/page/3/SectionHeader/3']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 388-405::/page/3/SectionHeader/1` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/3/SectionHeader/3` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/2` | 1.034885 | Starfinder has many specific rules, but you'll also want to keep these general guidelines in mind when playing. |
| 2 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/1` | 0.809824 | At this point, you have a character and are ready to play Starfinder! Or maybe you're the GM and you're  getting ready to run your first adventure. Either way, this chapter provides the full details f |
| 3 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/4` | 0.757718 | If you're ever uncertain how to apply a rule, the GM decides.  Of course, Starfinder is a game, so when adjudicating the  rules, the GM is encouraged to listen to everyone's point of  view and make a |
| 4 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/6` | 0.707949 | A core principle of Starfinder is that specific rules override  general ones. If two rules conflict, the more specific  one takes precedence. If there's still ambiguity, the GM  determines which rule |
| 5 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/3` | 0.687597 | Before diving into how to play Starfinder, it's important to  understand the game's three modes of play, which determine  the pace of your adventure and the specific rules you'll use  at a given time. |
| 6 | `PZO22001 Starfinder Player Core 388-405::/page/9/Text/7` | 0.572894 | Starfinder has a variety of skills for many different situations,  from Athletics to Computers to Piloting. Each grants you a  set of related actions that rely on you rolling a skill check.  Each skil |
| 7 | `PZO22001 Starfinder Player Core 388-405::/page/1/SectionHeader/11` | 0.514719 | THE STARFINDER  BASELINE |
| 8 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/5` | 0.492612 | In **exploration mode**, time is more flexible and the play  more free-form. Minutes, hours, or even days in the game  world pass quickly in the real world, as the characters travel  between star syst |
| 9 | `PZO22001 Starfinder Player Core 388-405::/page/11/Text/22` | 0.478110 | **GAME** **Rules Overview** |
| 10 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/9` | 0.470533 | Often, your choices have no immediate risk or consequences.  If you're exploring a starship and come across an intersection,  the GM asks, "Which way do you go?" You might choose to  take the corridor |

### Query 72
- Text: Summarize **The GM Has the Final Say**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/3/SectionHeader/3']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 388-405::/page/3/SectionHeader/3', 'PZO22001 Starfinder Player Core 388-405::/page/3/Text/4', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/8']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/3/SectionHeader/3', 'PZO22001 Starfinder Player Core 388-405::/page/3/Text/4', 'PZO22001 Starfinder Player Core 388-405::/page/3/Text/2']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 388-405::/page/3/Text/4` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/3/Text/2` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 388-405::/page/3/SectionHeader/3` | 1.003391 | **The GM Has the Final Say** |
| 2 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/4` | 0.495006 | If you're ever uncertain how to apply a rule, the GM decides.  Of course, Starfinder is a game, so when adjudicating the  rules, the GM is encouraged to listen to everyone's point of  view and make a |
| 3 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/8` | 0.469254 | Throughout the game, the GM describes what's happening in  the world and then asks the players, "So what do you do?"  Exactly what you choose to do, and how the GM responds to  those choices, builds a |
| 4 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/12` | 0.364316 | Your group will likely talk about what types of content you  want in your game before your campaign begins. The following  is a set of basic assumptions that works for many groups. The  GM can find mo |
| 5 | `PZO22001 Starfinder Player Core 388-405::/page/5/Text/23` | 0.361375 | **PLAYING THE ** **GAME** |
| 6 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/39` | 0.361375 | **PLAYING THE ** **GAME** |
| 7 | `PZO22001 Starfinder Player Core 388-405::/page/7/Text/20` | 0.361375 | **PLAYING THE ** **GAME** |
| 8 | `PZO22001 Starfinder Player Core 388-405::/page/13/Text/32` | 0.361375 | **PLAYING THE ** **GAME** |
| 9 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/28` | 0.361375 | **PLAYING THE ** **GAME** |
| 10 | `PZO22001 Starfinder Player Core 388-405::/page/9/Text/26` | 0.361375 | **PLAYING THE ** **GAME** |

### Query 73
- Text: Summarize If you're ever uncertain how to apply a rule, the GM decides.  Of course, Starfinder is a game, so when adjudicating the  rules, the GM is encouraged to listen to everyone's point of  view and make a decision that is both fair and fun.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/3/Text/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 388-405::/page/3/Text/4', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/3', 'PZO22001 Starfinder Player Core 388-405::/page/3/Text/2']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/3/Text/4', 'PZO22001 Starfinder Player Core 388-405::/page/3/SectionHeader/3', 'PZO22001 Starfinder Player Core 388-405::/page/3/SectionHeader/5']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 388-405::/page/3/SectionHeader/3` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/3/SectionHeader/5` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/4` | 1.045124 | If you're ever uncertain how to apply a rule, the GM decides.  Of course, Starfinder is a game, so when adjudicating the  rules, the GM is encouraged to listen to everyone's point of  view and make a |
| 2 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/3` | 0.730318 | Before diving into how to play Starfinder, it's important to  understand the game's three modes of play, which determine  the pace of your adventure and the specific rules you'll use  at a given time. |
| 3 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/2` | 0.729861 | Starfinder has many specific rules, but you'll also want to keep these general guidelines in mind when playing. |
| 4 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/1` | 0.692582 | At this point, you have a character and are ready to play Starfinder! Or maybe you're the GM and you're  getting ready to run your first adventure. Either way, this chapter provides the full details f |
| 5 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/6` | 0.638799 | A core principle of Starfinder is that specific rules override  general ones. If two rules conflict, the more specific  one takes precedence. If there's still ambiguity, the GM  determines which rule |
| 6 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/8` | 0.608913 | Throughout the game, the GM describes what's happening in  the world and then asks the players, "So what do you do?"  Exactly what you choose to do, and how the GM responds to  those choices, builds a |
| 7 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/9` | 0.607838 | Often, your choices have no immediate risk or consequences.  If you're exploring a starship and come across an intersection,  the GM asks, "Which way do you go?" You might choose to  take the corridor |
| 8 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/12` | 0.535098 | Your group will likely talk about what types of content you  want in your game before your campaign begins. The following  is a set of basic assumptions that works for many groups. The  GM can find mo |
| 9 | `PZO22001 Starfinder Player Core 388-405::/page/9/Text/15` | 0.515131 | The GM can choose to make any check secret, even  if it's not usually rolled secretly. Conversely, the GM  can let you roll any check yourself, even if that check  would usually be secret. Some groups |
| 10 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/14` | 0.511346 | Sometimes a rule could be interpreted multiple ways. If one  version is too good to be true, it probably is. If a rule seems  to have wording with problematic repercussions or doesn't  work as intende |

### Query 74
- Text: Summarize **Specific Overrides General**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/3/SectionHeader/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 388-405::/page/3/SectionHeader/5', 'PZO22001 Starfinder Player Core 388-405::/page/15/Text/26', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/29']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/3/SectionHeader/5', 'PZO22001 Starfinder Player Core 388-405::/page/3/Text/6', 'PZO22001 Starfinder Player Core 388-405::/page/3/Text/4']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 388-405::/page/3/Text/6` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/3/Text/4` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 388-405::/page/3/SectionHeader/5` | 0.967627 | **Specific Overrides General** |
| 2 | `PZO22001 Starfinder Player Core 388-405::/page/15/Text/26` | 0.455547 | **Rules Overview** |
| 3 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/29` | 0.455547 | **Rules Overview** |
| 4 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/40` | 0.413547 | **Rules Overview** |
| 5 | `PZO22001 Starfinder Player Core 388-405::/page/13/Text/33` | 0.413547 | **Rules Overview** |
| 6 | `PZO22001 Starfinder Player Core 388-405::/page/7/Text/21` | 0.413547 | **Rules Overview** |
| 7 | `PZO22001 Starfinder Player Core 388-405::/page/5/Text/24` | 0.413547 | **Rules Overview** |
| 8 | `PZO22001 Starfinder Player Core 388-405::/page/9/Text/27` | 0.413547 | **Rules Overview** |
| 9 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/6` | 0.397350 | A core principle of Starfinder is that specific rules override  general ones. If two rules conflict, the more specific  one takes precedence. If there's still ambiguity, the GM  determines which rule |
| 10 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/23` | 0.382956 | **Related:** Escape a grab or restraint (page 408), falling (page  413), forced movement (page 414), moving through creatures  (page 414), special movement modes (burrow, climb, fly, and  swim; page 4 |

### Query 75
- Text: What is the rule about A core principle of Starfinder is that specific rules override  general ones. If two rules conflict, the more specific  one takes precedence. If there's still ambiguity, the GM  determines which rule to use. For example, the rules state  that when attacking a concealed creature, you must attempt  a DC 5 flat check to determine if you hit. Flat checks don't  benefit from modifiers, bonuses, or penalties, but an ability  that's specifically designed to overcome concealment  might override and alter this. While some special rules  may also state the normal rules to provide context, you  should always default to the general rules presented in this  chapter, even if effects don't specifically say to.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/3/Text/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 388-405::/page/3/Text/6', 'PZO22001 Starfinder Player Core 388-405::/page/3/Text/2', 'PZO22001 Starfinder Player Core 388-405::/page/3/Text/4']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/3/Text/6', 'PZO22001 Starfinder Player Core 388-405::/page/3/SectionHeader/5', 'PZO22001 Starfinder Player Core 388-405::/page/3/SectionHeader/7']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 388-405::/page/3/SectionHeader/5` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/3/SectionHeader/7` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/6` | 1.022080 | A core principle of Starfinder is that specific rules override  general ones. If two rules conflict, the more specific  one takes precedence. If there's still ambiguity, the GM  determines which rule |
| 2 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/2` | 0.733522 | Starfinder has many specific rules, but you'll also want to keep these general guidelines in mind when playing. |
| 3 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/4` | 0.693495 | If you're ever uncertain how to apply a rule, the GM decides.  Of course, Starfinder is a game, so when adjudicating the  rules, the GM is encouraged to listen to everyone's point of  view and make a |
| 4 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/1` | 0.629492 | At this point, you have a character and are ready to play Starfinder! Or maybe you're the GM and you're  getting ready to run your first adventure. Either way, this chapter provides the full details f |
| 5 | `PZO22001 Starfinder Player Core 388-405::/page/9/Text/11` | 0.603223 | When the likelihood something will happen or fail to  happen is based purely on chance, you'll attempt a flat  check. A flat check never includes any modifiers, bonuses,  or penalties—you just roll a |
| 6 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/3` | 0.559387 | Before diving into how to play Starfinder, it's important to  understand the game's three modes of play, which determine  the pace of your adventure and the specific rules you'll use  at a given time. |
| 7 | `PZO22001 Starfinder Player Core 388-405::/page/9/Text/5` | 0.556864 | Often, you'll roll a Perception check to determine your order  in initiative. When you do this, instead of comparing the  result against a DC, the GM will put the results for everyone  in the encounte |
| 8 | `PZO22001 Starfinder Player Core 388-405::/page/9/Text/7` | 0.552437 | Starfinder has a variety of skills for many different situations,  from Athletics to Computers to Piloting. Each grants you a  set of related actions that rely on you rolling a skill check.  Each skil |
| 9 | `PZO22001 Starfinder Player Core 388-405::/page/9/Text/14` | 0.548128 | Sometimes you as the player shouldn't know the exact  result and effect of a check. In these situations, the rules  (or the GM) will call for a secret check. The secret trait  appears on anything that |
| 10 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/26` | 0.543718 | Skill checks are required for all sorts of other tasks related  to adventuring and life in general. Most of their rules are  in Chapter 4 (page 183). You'll find the rules for **calculating ** **skill |

### Query 76
- Text: Summarize **Rounding**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/3/SectionHeader/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 388-405::/page/3/SectionHeader/7', 'PZO22001 Starfinder Player Core 388-405::/page/17/Text/26', 'PZO22001 Starfinder Player Core 388-405::/page/15/Text/34']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/3/SectionHeader/7', 'PZO22001 Starfinder Player Core 388-405::/page/3/Text/6', 'PZO22001 Starfinder Player Core 388-405::/page/3/Text/8']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 388-405::/page/3/Text/6` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/3/Text/8` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 388-405::/page/3/SectionHeader/7` | 0.955060 | **Rounding** |
| 2 | `PZO22001 Starfinder Player Core 388-405::/page/17/Text/26` | 0.470685 | **Movement** |
| 3 | `PZO22001 Starfinder Player Core 388-405::/page/15/Text/34` | 0.470685 | **Movement** |
| 4 | `PZO22001 Starfinder Player Core 388-405::/page/7/Text/29` | 0.428685 | **Movement** |
| 5 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/37` | 0.428685 | **Movement** |
| 6 | `PZO22001 Starfinder Player Core 388-405::/page/5/Text/32` | 0.428685 | **Movement** |
| 7 | `PZO22001 Starfinder Player Core 388-405::/page/9/Text/35` | 0.428685 | **Movement** |
| 8 | `PZO22001 Starfinder Player Core 388-405::/page/13/Text/41` | 0.428685 | **Movement** |
| 9 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/48` | 0.428685 | **Movement** |
| 10 | `PZO22001 Starfinder Player Core 388-405::/page/11/Text/30` | 0.428685 | **Movement** |

### Query 77
- Text: What is the rule about You may need to calculate a fraction of a value, like halving  damage. Always round down unless otherwise specified.  For example, if a spell deals 7 damage and a creature takes  half damage from it, that creature takes 3 damage.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/3/Text/8']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 388-405::/page/3/Text/8', 'PZO22001 Starfinder Player Core 388-405::/page/11/Text/3', 'PZO22001 Starfinder Player Core 388-405::/page/10/Text/5']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/3/Text/8', 'PZO22001 Starfinder Player Core 388-405::/page/3/SectionHeader/9', 'PZO22001 Starfinder Player Core 388-405::/page/3/SectionHeader/7']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 388-405::/page/3/SectionHeader/9` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/3/SectionHeader/7` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/8` | 1.002334 | You may need to calculate a fraction of a value, like halving  damage. Always round down unless otherwise specified.  For example, if a spell deals 7 damage and a creature takes  half damage from it, |
| 2 | `PZO22001 Starfinder Player Core 388-405::/page/11/Text/3` | 0.736004 | Sometimes you'll need to halve or double an amount of  damage, such as when the outcome of your Strike is a critical  hit or when you succeed at a basic Reflex save against a spell.  When this happens |
| 3 | `PZO22001 Starfinder Player Core 388-405::/page/10/Text/5` | 0.590898 | Damage is sometimes given as a fixed amount, but more often  than not you'll make a **damage roll** to determine how much  damage you deal. A damage roll typically uses a number and  type of dice dete |
| 4 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/18` | 0.543731 | Attacks, spells, and other dangers **deal damage** (page 398).  The amount is typically determined by a **Damage **roll (page  398), which can use a variety of sizes and numbers of dice. |
| 5 | `PZO22001 Starfinder Player Core 388-405::/page/10/Text/19` | 0.540979 | If the combined penalties on an attack would reduce the  damage to 0 or below, you still deal 1 damage. Sometimes there  are other considerations, as described below. |
| 6 | `PZO22001 Starfinder Player Core 388-405::/page/7/Text/6` | 0.530465 | Many times, instead of requiring you to make a spell attack roll,  the spells you cast require those within the area or targeted  by the spell to attempt a saving throw against your **spell DC** to de |
| 7 | `PZO22001 Starfinder Player Core 388-405::/page/11/Text/6` | 0.529800 | Once you've calculated how much damage you deal, you'll  need to determine the damage type. The blast of a laser rifle  deals fire damage. The sting of an *entropy strike* spell deals  void damage. So |
| 8 | `PZO22001 Starfinder Player Core 388-405::/page/10/Text/11` | 0.526869 | Your weapon, unarmed attack, spell, or even a magic item  determines what size and number of dice you roll for damage.  For instance, if you're using a normal doshko, you'll roll 1d12.  If you're cast |
| 9 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/22` | 0.524036 | Most of the rules for casting spells are in Chapter 7 (pages  294–301). For a spell that requires an attack roll against  the target's AC, you'll calculate your **spell attack modifier** |
| 10 | `PZO22001 Starfinder Player Core 388-405::/page/12/Text/16` | 0.520364 | If you have a weakness to a certain type of damage or  damage from a certain source, that type of damage is extra  effective against you. Whenever you would take that type of  damage, increase the dam |

### Query 78
- Text: Summarize **Multiplying**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/3/SectionHeader/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 388-405::/page/3/SectionHeader/9', 'PZO22001 Starfinder Player Core 388-405::/page/3/Text/10', 'PZO22001 Starfinder Player Core 388-405::/page/3/SectionHeader/11']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/3/SectionHeader/9', 'PZO22001 Starfinder Player Core 388-405::/page/3/Text/10', 'PZO22001 Starfinder Player Core 388-405::/page/3/Text/8']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 388-405::/page/3/Text/10` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/3/Text/8` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 388-405::/page/3/SectionHeader/9` | 0.983179 | **Multiplying** |
| 2 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/10` | 0.566859 | When more than one effect would multiply the same  number, don't multiply more than once. Instead, combine  all the multipliers into a single multiplier, with each  multiple after the first adding 1 l |
| 3 | `PZO22001 Starfinder Player Core 388-405::/page/3/SectionHeader/11` | 0.443974 | **Duplicate Effects** |
| 4 | `PZO22001 Starfinder Player Core 388-405::/page/6/Text/12` | 0.374755 | The more attacks you make beyond your first in a single turn, the  less accurate you become, represented by the **multiple attack ** **penalty**. The second time you use an attack action during your |
| 5 | `PZO22001 Starfinder Player Core 388-405::/page/6/TableCell/355` | 0.329880 | Multiple Attack Penalty |
| 6 | `PZO22001 Starfinder Player Core 388-405::/page/4/ListItem/8` | 0.326988 | 2. **Calculate the result.** |
| 7 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/40` | 0.324492 | **Counteracting** |
| 8 | `PZO22001 Starfinder Player Core 388-405::/page/15/Text/38` | 0.324492 | **Counteracting** |
| 9 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/51` | 0.324492 | **Counteracting** |
| 10 | `PZO22001 Starfinder Player Core 388-405::/page/11/Text/34` | 0.324492 | **Counteracting** |

### Query 79
- Text: What is the rule about When more than one effect would multiply the same  number, don't multiply more than once. Instead, combine  all the multipliers into a single multiplier, with each  multiple after the first adding 1 less than its value. For  instance, if one ability doubled the duration of one of your  spells and another one doubled the duration of the same  spell, you would triple the duration, not quadruple it.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/3/Text/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 388-405::/page/3/Text/10', 'PZO22001 Starfinder Player Core 388-405::/page/3/Text/12', 'PZO22001 Starfinder Player Core 388-405::/page/11/Text/4']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/3/Text/10', 'PZO22001 Starfinder Player Core 388-405::/page/3/SectionHeader/11', 'PZO22001 Starfinder Player Core 388-405::/page/3/SectionHeader/9']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 388-405::/page/3/SectionHeader/11` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/3/SectionHeader/9` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/10` | 0.999884 | When more than one effect would multiply the same  number, don't multiply more than once. Instead, combine  all the multipliers into a single multiplier, with each  multiple after the first adding 1 l |
| 2 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/12` | 0.682240 | When you're affected by the same thing multiple times, only  one instance applies, using the higher level or rank of the  effects, or the newer effect if the two are equal. For example,  if you were u |
| 3 | `PZO22001 Starfinder Player Core 388-405::/page/11/Text/4` | 0.628772 | When doubling, the GM might allow you to roll the dice  twice and double the modifiers, bonuses, and penalties instead  of doubling the entire result, but this usually works best for  single-target at |
| 4 | `PZO22001 Starfinder Player Core 388-405::/page/5/Text/14` | 0.554290 | You can never have more than one fortune effect  or misfortune effect come into play on a single roll.  For instance, if an effect lets you roll twice and use  the higher roll, you can't then use Meye |
| 5 | `PZO22001 Starfinder Player Core 388-405::/page/11/Text/3` | 0.541399 | Sometimes you'll need to halve or double an amount of  damage, such as when the outcome of your Strike is a critical  hit or when you succeed at a basic Reflex save against a spell.  When this happens |
| 6 | `PZO22001 Starfinder Player Core 388-405::/page/6/Text/12` | 0.531015 | The more attacks you make beyond your first in a single turn, the  less accurate you become, represented by the **multiple attack ** **penalty**. The second time you use an attack action during your |
| 7 | `PZO22001 Starfinder Player Core 388-405::/page/4/Text/21` | 0.521498 | There are three other types of bonus that frequently appear:  circumstance bonuses, item bonuses, and status bonuses. If  you have different types of bonuses that would apply to the  same roll, you'll |
| 8 | `PZO22001 Starfinder Player Core 388-405::/page/3/SectionHeader/9` | 0.515712 | **Multiplying** |
| 9 | `PZO22001 Starfinder Player Core 388-405::/page/6/Text/15` | 0.503520 | Always calculate your multiple attack penalty based on  the weapon you're using on that attack, not ones you used  on previous attacks. For example, let's say you're wielding a  plasma sword in one ha |
| 10 | `PZO22001 Starfinder Player Core 388-405::/page/4/Text/26` | 0.496019 | Penalties work very much like bonuses. You can have  **circumstance penalties**, **status penalties**, and sometimes even  **item penalties**. Like bonuses of the same type, you take only  the worst a |

### Query 80
- Text: Summarize **Duplicate Effects**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/3/SectionHeader/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 388-405::/page/3/SectionHeader/11', 'PZO22001 Starfinder Player Core 388-405::/page/11/Text/31', 'PZO22001 Starfinder Player Core 388-405::/page/7/Text/30']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/3/SectionHeader/11', 'PZO22001 Starfinder Player Core 388-405::/page/3/Text/10', 'PZO22001 Starfinder Player Core 388-405::/page/3/Text/12']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 388-405::/page/3/Text/10` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/3/Text/12` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 388-405::/page/3/SectionHeader/11` | 0.979483 | **Duplicate Effects** |
| 2 | `PZO22001 Starfinder Player Core 388-405::/page/11/Text/31` | 0.665959 | **Effects** |
| 3 | `PZO22001 Starfinder Player Core 388-405::/page/7/Text/30` | 0.665959 | **Effects** |
| 4 | `PZO22001 Starfinder Player Core 388-405::/page/5/Text/33` | 0.623959 | **Effects** |
| 5 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/49` | 0.623959 | **Effects** |
| 6 | `PZO22001 Starfinder Player Core 388-405::/page/15/Text/35` | 0.623959 | **Effects** |
| 7 | `PZO22001 Starfinder Player Core 388-405::/page/2/SectionHeader/16` | 0.562616 | EFFECTS |
| 8 | `PZO22001 Starfinder Player Core 388-405::/page/17/Text/27` | 0.530820 | **Effects** **Area** |
| 9 | `PZO22001 Starfinder Player Core 388-405::/page/9/Text/36` | 0.530820 | **Effects** **Area** |
| 10 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/38` | 0.530820 | **Effects** **Area** |

### Query 81
- Text: What is the rule about When you're affected by the same thing multiple times, only  one instance applies, using the higher level or rank of the  effects, or the newer effect if the two are equal. For example,  if you were using *cellular stimulant* and then cast it again,  you'd still benefit from only one casting of that spell. Casting  a spell again on the same target might get you a better  duration or effect if it were cast at a higher rank the second  time, but otherwise doing so gives you no advantage.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/3/Text/12']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 388-405::/page/3/Text/12', 'PZO22001 Starfinder Player Core 388-405::/page/5/Text/14', 'PZO22001 Starfinder Player Core 388-405::/page/3/Text/10']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/3/Text/12', 'PZO22001 Starfinder Player Core 388-405::/page/3/SectionHeader/11', 'PZO22001 Starfinder Player Core 388-405::/page/3/SectionHeader/13']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 388-405::/page/3/SectionHeader/11` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/3/SectionHeader/13` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/12` | 1.006848 | When you're affected by the same thing multiple times, only  one instance applies, using the higher level or rank of the  effects, or the newer effect if the two are equal. For example,  if you were u |
| 2 | `PZO22001 Starfinder Player Core 388-405::/page/5/Text/14` | 0.683023 | You can never have more than one fortune effect  or misfortune effect come into play on a single roll.  For instance, if an effect lets you roll twice and use  the higher roll, you can't then use Meye |
| 3 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/10` | 0.642118 | When more than one effect would multiply the same  number, don't multiply more than once. Instead, combine  all the multipliers into a single multiplier, with each  multiple after the first adding 1 l |
| 4 | `PZO22001 Starfinder Player Core 388-405::/page/12/Text/12` | 0.594952 | Some effects grant you immunity to the same effect for a set  amount of time. If an effect grants you temporary immunity,  repeated applications of that effect don't affect you for as  long as the tem |
| 5 | `PZO22001 Starfinder Player Core 388-405::/page/4/Text/26` | 0.579896 | Penalties work very much like bonuses. You can have  **circumstance penalties**, **status penalties**, and sometimes even  **item penalties**. Like bonuses of the same type, you take only  the worst a |
| 6 | `PZO22001 Starfinder Player Core 388-405::/page/4/Text/21` | 0.558518 | There are three other types of bonus that frequently appear:  circumstance bonuses, item bonuses, and status bonuses. If  you have different types of bonuses that would apply to the  same roll, you'll |
| 7 | `PZO22001 Starfinder Player Core 388-405::/page/11/Text/4` | 0.554457 | When doubling, the GM might allow you to roll the dice  twice and double the modifiers, bonuses, and penalties instead  of doubling the entire result, but this usually works best for  single-target at |
| 8 | `PZO22001 Starfinder Player Core 388-405::/page/5/Text/15` | 0.535457 | If both a fortune effect and a misfortune effect  would apply to the same roll, the two cancel each  other out, and you roll normally. |
| 9 | `PZO22001 Starfinder Player Core 388-405::/page/10/Text/18` | 0.525595 | As with checks, you might add circumstance, status, or item  bonuses to your damage rolls, but if you have multiple bonuses  of the same type, you add only the highest bonus of that type.  Again like |
| 10 | `PZO22001 Starfinder Player Core 388-405::/page/6/Text/16` | 0.518414 | The multiple attack penalty applies only during your turn,  so you don't have to keep track of it if you can perform a  Reactive Strike or a similar reaction that lets you make a  Strike on someone el |

### Query 82
- Text: Summarize **Ambiguous Rules**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/3/SectionHeader/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 388-405::/page/3/SectionHeader/13', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/29', 'PZO22001 Starfinder Player Core 388-405::/page/15/Text/26']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/3/SectionHeader/13', 'PZO22001 Starfinder Player Core 388-405::/page/3/Text/14', 'PZO22001 Starfinder Player Core 388-405::/page/3/Text/12']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 388-405::/page/3/Text/14` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/3/Text/12` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 388-405::/page/3/SectionHeader/13` | 0.973676 | **Ambiguous Rules** |
| 2 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/29` | 0.657184 | **Rules Overview** |
| 3 | `PZO22001 Starfinder Player Core 388-405::/page/15/Text/26` | 0.657184 | **Rules Overview** |
| 4 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/40` | 0.615184 | **Rules Overview** |
| 5 | `PZO22001 Starfinder Player Core 388-405::/page/9/Text/27` | 0.615184 | **Rules Overview** |
| 6 | `PZO22001 Starfinder Player Core 388-405::/page/7/Text/21` | 0.615184 | **Rules Overview** |
| 7 | `PZO22001 Starfinder Player Core 388-405::/page/13/Text/33` | 0.615184 | **Rules Overview** |
| 8 | `PZO22001 Starfinder Player Core 388-405::/page/5/Text/24` | 0.615184 | **Rules Overview** |
| 9 | `PZO22001 Starfinder Player Core 388-405::/page/2/SectionHeader/1` | 0.576024 | RULES OVERVIEW |
| 10 | `PZO22001 Starfinder Player Core 388-405::/page/11/Text/22` | 0.541444 | **GAME** **Rules Overview** |

### Query 83
- Text: Summarize Sometimes a rule could be interpreted multiple ways. If one  version is too good to be true, it probably is. If a rule seems  to have wording with problematic repercussions or doesn't  work as intended, work with your group to find a good  solution, rather than just playing with the rule as printed.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/3/Text/14']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 388-405::/page/3/Text/14', 'PZO22001 Starfinder Player Core 388-405::/page/3/Text/6', 'PZO22001 Starfinder Player Core 388-405::/page/3/Text/4']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/3/Text/14', 'PZO22001 Starfinder Player Core 388-405::/page/3/SectionHeader/15', 'PZO22001 Starfinder Player Core 388-405::/page/3/SectionHeader/13']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 388-405::/page/3/SectionHeader/15` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/3/SectionHeader/13` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/14` | 1.040150 | Sometimes a rule could be interpreted multiple ways. If one  version is too good to be true, it probably is. If a rule seems  to have wording with problematic repercussions or doesn't  work as intende |
| 2 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/6` | 0.558655 | A core principle of Starfinder is that specific rules override  general ones. If two rules conflict, the more specific  one takes precedence. If there's still ambiguity, the GM  determines which rule |
| 3 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/4` | 0.552711 | If you're ever uncertain how to apply a rule, the GM decides.  Of course, Starfinder is a game, so when adjudicating the  rules, the GM is encouraged to listen to everyone's point of  view and make a |
| 4 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/10` | 0.505176 | But sometimes what happens as a result of your choices  is less than certain. In those cases, you'll attempt a check, as  described starting on page 392. |
| 5 | `PZO22001 Starfinder Player Core 388-405::/page/5/Text/14` | 0.488735 | You can never have more than one fortune effect  or misfortune effect come into play on a single roll.  For instance, if an effect lets you roll twice and use  the higher roll, you can't then use Meye |
| 6 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/12` | 0.487471 | An action that can potentially fail requires rolling a **check** (page 392). Roll a d20 (20-sided die) and identify the modifiers,  bonuses, and penalties that apply. Then, calculate the result,  comp |
| 7 | `PZO22001 Starfinder Player Core 388-405::/page/9/Text/5` | 0.487388 | Often, you'll roll a Perception check to determine your order  in initiative. When you do this, instead of comparing the  result against a DC, the GM will put the results for everyone  in the encounte |
| 8 | `PZO22001 Starfinder Player Core 388-405::/page/4/Text/26` | 0.482818 | Penalties work very much like bonuses. You can have  **circumstance penalties**, **status penalties**, and sometimes even  **item penalties**. Like bonuses of the same type, you take only  the worst a |
| 9 | `PZO22001 Starfinder Player Core 388-405::/page/9/Text/16` | 0.473842 | unfavorable situations might give you a circumstance penalty  to your skill check, while harmful spells, magic, or conditions  might also impose a status penalty. Using shoddy or makeshift  tools migh |
| 10 | `PZO22001 Starfinder Player Core 388-405::/page/5/Text/17` | 0.468304 | You **critically succeed** when the check's result meets or  exceeds the DC by 10 or more. If the check is an attack roll, this  is also known as a critical hit. You can also **critically fail** a che |

### Query 84
- Text: Summarize DEFENSES
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/3/SectionHeader/15']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 388-405::/page/7/SectionHeader/8', 'PZO22001 Starfinder Player Core 388-405::/page/3/SectionHeader/15', 'PZO22001 Starfinder Player Core 388-405::/page/11/Text/9']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/3/SectionHeader/15', 'PZO22001 Starfinder Player Core 388-405::/page/3/Text/16', 'PZO22001 Starfinder Player Core 388-405::/page/3/Text/14']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 388-405::/page/3/Text/16` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/3/Text/14` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 388-405::/page/7/SectionHeader/8` | 0.953789 | DEFENSES |
| 2 | `PZO22001 Starfinder Player Core 388-405::/page/3/SectionHeader/15` | 0.953789 | DEFENSES |
| 3 | `PZO22001 Starfinder Player Core 388-405::/page/11/Text/9` | 0.490290 | Defenses against certain types of damage or effects are called  immunities or resistances, while vulnerabilities are called  weaknesses. Apply immunities first, then weaknesses, and  resistances third |
| 4 | `PZO22001 Starfinder Player Core 388-405::/page/7/Text/9` | 0.434423 | Multiple statistics help you defend against attacks, spells,  hazards, and other dangers of adventuring: Armor Class and  three saving throws. |
| 5 | `PZO22001 Starfinder Player Core 388-405::/page/10/ListItem/8` | 0.401063 | 3. Apply **immunities**, **weaknesses**, and **resistances **the  subject has to the damage. |
| 6 | `PZO22001 Starfinder Player Core 388-405::/page/10/SectionHeader/22` | 0.395687 | COUNTING DAMAGE DICE |
| 7 | `PZO22001 Starfinder Player Core 388-405::/page/3/SectionHeader/17` | 0.383061 | DAMAGE |
| 8 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/16` | 0.382293 | Your **Armor Class** **(AC) **(page 395) is the main DC used for  attacks against you. You might also roll a type of check called  a **Saving Throw** (page 396), also called a **save**, against spells |
| 9 | `PZO22001 Starfinder Player Core 388-405::/page/10/SectionHeader/20` | 0.380410 | ADDING DAMAGE DICE |
| 10 | `PZO22001 Starfinder Player Core 388-405::/page/13/SectionHeader/1` | 0.378878 | **DAMAGE TYPES** |

### Query 85
- Text: What is the rule about Your **Armor Class** **(AC) **(page 395) is the main DC used for  attacks against you. You might also roll a type of check called  a **Saving Throw** (page 396), also called a **save**, against spells,  afflictions, and a wide variety of other effects. There are three  kinds of saving throw: **Fortitude**, **Reflex**, and **Will**.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/3/Text/16']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 388-405::/page/3/Text/16', 'PZO22001 Starfinder Player Core 388-405::/page/8/Text/9', 'PZO22001 Starfinder Player Core 388-405::/page/6/Text/21']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/3/Text/16', 'PZO22001 Starfinder Player Core 388-405::/page/3/SectionHeader/15', 'PZO22001 Starfinder Player Core 388-405::/page/3/SectionHeader/17']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 388-405::/page/3/SectionHeader/15` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/3/SectionHeader/17` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/16` | 1.022380 | Your **Armor Class** **(AC) **(page 395) is the main DC used for  attacks against you. You might also roll a type of check called  a **Saving Throw** (page 396), also called a **save**, against spells |
| 2 | `PZO22001 Starfinder Player Core 388-405::/page/8/Text/9` | 0.748959 | There are three types of saving throws: Fortitude saves, Reflex  saves, and Will saves. These are frequently called "saves" it's the same thing. Saving throws measure your ability to  shrug off harmfu |
| 3 | `PZO22001 Starfinder Player Core 388-405::/page/6/Text/21` | 0.747474 | You compare your attack roll to Armor Class (AC), a special  type of DC. Learn how to calculate it on page 25. |
| 4 | `PZO22001 Starfinder Player Core 388-405::/page/7/Text/11` | 0.678118 | Attack rolls are compared to a special DC called **Armor Class ** **(AC)**, which measures how hard it is for your foes to hit you  with Strikes, spell attack rolls, and other attacks. Just like for |
| 5 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/23` | 0.676575 | (page 394). For one that causes its subject to attempt a  saving throw, you'll need your **spell DC** (page 395). |
| 6 | `PZO22001 Starfinder Player Core 388-405::/page/7/Text/6` | 0.662486 | Many times, instead of requiring you to make a spell attack roll,  the spells you cast require those within the area or targeted  by the spell to attempt a saving throw against your **spell DC** to de |
| 7 | `PZO22001 Starfinder Player Core 388-405::/page/8/Text/16` | 0.648799 | Sometimes you'll need to know your DC for a given saving  throw (such as a Grapple attempt requiring a roll against your  Fortitude DC). Like any other DC derived from a modifier,  the DC for a saving |
| 8 | `PZO22001 Starfinder Player Core 388-405::/page/8/Text/10` | 0.637752 | **Fortitude** saving throws allow you to reduce the effects of  abilities and afflictions that can debilitate the body. They use  your Constitution modifier and are calculated as shown in the  formula |
| 9 | `PZO22001 Starfinder Player Core 388-405::/page/8/Text/19` | 0.614292 | Sometimes you will be called on to attempt a basic saving  throw (or "basic save"). This type of saving throw works  just like any other saving throw—the "basic" part refers to  the effects. For a bas |
| 10 | `PZO22001 Starfinder Player Core 388-405::/page/8/Text/12` | 0.606117 | **Reflex** saving throws measure how well you can respond  quickly to a situation and how gracefully you can avoid  effects that have been thrown at you. They use your Dexterity  modifier and are calc |

### Query 86
- Text: What is the rule about DAMAGE?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/3/SectionHeader/17']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 388-405::/page/3/SectionHeader/17', 'PZO22001 Starfinder Player Core 388-405::/page/15/SectionHeader/6', 'PZO22001 Starfinder Player Core 388-405::/page/13/SectionHeader/1']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/3/SectionHeader/17', 'PZO22001 Starfinder Player Core 388-405::/page/3/Text/18', 'PZO22001 Starfinder Player Core 388-405::/page/3/Text/16']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 388-405::/page/3/Text/18` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/3/Text/16` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 388-405::/page/3/SectionHeader/17` | 0.789147 | DAMAGE |
| 2 | `PZO22001 Starfinder Player Core 388-405::/page/15/SectionHeader/6` | 0.733216 | TAKING DAMAGE |
| 3 | `PZO22001 Starfinder Player Core 388-405::/page/13/SectionHeader/1` | 0.642985 | **DAMAGE TYPES** |
| 4 | `PZO22001 Starfinder Player Core 388-405::/page/10/ListItem/7` | 0.597699 | 2. Determine the **damage type**. |
| 5 | `PZO22001 Starfinder Player Core 388-405::/page/11/SectionHeader/5` | 0.589020 | STEP 2: DAMAGE TYPE |
| 6 | `PZO22001 Starfinder Player Core 388-405::/page/10/SectionHeader/22` | 0.580995 | COUNTING DAMAGE DICE |
| 7 | `PZO22001 Starfinder Player Core 388-405::/page/10/SectionHeader/20` | 0.576747 | ADDING DAMAGE DICE |
| 8 | `PZO22001 Starfinder Player Core 388-405::/page/10/SectionHeader/27` | 0.563680 | PERSISTENT DAMAGE |
| 9 | `PZO22001 Starfinder Player Core 388-405::/page/13/SectionHeader/3` | 0.558184 | **Physical Damage** |
| 10 | `PZO22001 Starfinder Player Core 388-405::/page/10/SectionHeader/10` | 0.550065 | STEP 1: ROLL DAMAGE DICE |

### Query 87
- Text: What is the rule about Attacks, spells, and other dangers **deal damage** (page 398).  The amount is typically determined by a **Damage **roll (page  398), which can use a variety of sizes and numbers of dice.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/3/Text/18']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 388-405::/page/3/Text/18', 'PZO22001 Starfinder Player Core 388-405::/page/10/Text/5', 'PZO22001 Starfinder Player Core 388-405::/page/10/ListItem/6']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/3/Text/18', 'PZO22001 Starfinder Player Core 388-405::/page/3/Text/19', 'PZO22001 Starfinder Player Core 388-405::/page/3/SectionHeader/17']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 388-405::/page/3/Text/19` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/3/SectionHeader/17` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/18` | 0.979585 | Attacks, spells, and other dangers **deal damage** (page 398).  The amount is typically determined by a **Damage **roll (page  398), which can use a variety of sizes and numbers of dice. |
| 2 | `PZO22001 Starfinder Player Core 388-405::/page/10/Text/5` | 0.697206 | Damage is sometimes given as a fixed amount, but more often  than not you'll make a **damage roll** to determine how much  damage you deal. A damage roll typically uses a number and  type of dice dete |
| 3 | `PZO22001 Starfinder Player Core 388-405::/page/10/ListItem/6` | 0.692241 | 1. **Roll damage dice** indicated by the weapon, unarmed attack,  or spell, and apply the modifiers, bonuses, and penalties  that apply to the result of the roll. |
| 4 | `PZO22001 Starfinder Player Core 388-405::/page/10/Text/11` | 0.647784 | Your weapon, unarmed attack, spell, or even a magic item  determines what size and number of dice you roll for damage.  For instance, if you're using a normal doshko, you'll roll 1d12.  If you're cast |
| 5 | `PZO22001 Starfinder Player Core 388-405::/page/10/Text/21` | 0.617830 | Each weapon lists the damage die used for its damage roll.  A standard weapon deals one die of damage, but upgrading  to a tactical or better version of the weapon increases the  number of dice rolled |
| 6 | `PZO22001 Starfinder Player Core 388-405::/page/10/Text/2` | 0.591005 | Strikes, spells, hazards, and all number of other dangers can deal damage, which can kill creatures and  destroy objects. |
| 7 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/19` | 0.576348 | Damage reduces the **Hit Points (HP)** (page 402) that  measure a creature's overall health or an object's durability.  A creature might have **immunity** to damage or effects of  certain kinds, a **r |
| 8 | `PZO22001 Starfinder Player Core 388-405::/page/6/Text/10` | 0.572884 | Penalties to attack rolls come from situations and effects  as well. Circumstance penalties come from risky tactics or  detrimental circumstances, status penalties come from spells  and magic working |
| 9 | `PZO22001 Starfinder Player Core 388-405::/page/10/Text/16` | 0.565181 | For damage rolls with **spells**, **grenades**, and similar items, you  don't add an attribute modifier unless otherwise noted. |
| 10 | `PZO22001 Starfinder Player Core 388-405::/page/10/Text/23` | 0.555919 | Effects based on a weapon's number of damage dice include  only the weapon's damage die plus any extra dice from the  weapon's type (tactical, advanced, superior, elite, ultimate, and  paragon). They |

### Query 88
- Text: What is the rule about Damage reduces the **Hit Points (HP)** (page 402) that  measure a creature's overall health or an object's durability.  A creature might have **immunity** to damage or effects of  certain kinds, a **resistance** that reduces the damage it takes,  or a **weakness** that increases damage it takes (page 400).  These are typically keyed to **Damage **types (page 401) such  as slashing damage or fire damage.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/3/Text/19']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 388-405::/page/3/Text/19', 'PZO22001 Starfinder Player Core 388-405::/page/10/Text/4', 'PZO22001 Starfinder Player Core 388-405::/page/14/Text/15']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/3/Text/19', 'PZO22001 Starfinder Player Core 388-405::/page/3/Text/18', 'PZO22001 Starfinder Player Core 388-405::/page/3/Text/20']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 388-405::/page/3/Text/18` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/3/Text/20` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/19` | 1.009111 | Damage reduces the **Hit Points (HP)** (page 402) that  measure a creature's overall health or an object's durability.  A creature might have **immunity** to damage or effects of  certain kinds, a **r |
| 2 | `PZO22001 Starfinder Player Core 388-405::/page/10/Text/4` | 0.772375 | Damage decreases a creature's Hit Points (HP) on a 1-to-1 basis  (so a creature that takes 6 damage loses 6 Hit Points). The full  rules for losing HP can be found in the Hit Points, Healing, and  Dyi |
| 3 | `PZO22001 Starfinder Player Core 388-405::/page/14/Text/15` | 0.725675 | Items have Hit Points like creatures, but the rules for  damaging them are different, as explained on page 236. An  item has a Hardness statistic that reduces damage the item  takes by that amount. Th |
| 4 | `PZO22001 Starfinder Player Core 388-405::/page/14/Text/7` | 0.666862 | All creatures and objects have **Hit Points (HP)**. Your maximum  Hit Point value represents your health, wherewithal, and  heroic drive when you're in good health and rested. Your  maximum Hit Points |
| 5 | `PZO22001 Starfinder Player Core 388-405::/page/11/Text/11` | 0.638411 | Any remaining damage reduces the target's Hit Points on a  1-to-1 basis. More information can be found in the Hit Points,  Healing, and Dying sections on pages 402–403. |
| 6 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/18` | 0.606149 | Attacks, spells, and other dangers **deal damage** (page 398).  The amount is typically determined by a **Damage **roll (page  398), which can use a variety of sizes and numbers of dice. |
| 7 | `PZO22001 Starfinder Player Core 388-405::/page/10/ListItem/8` | 0.605597 | 3. Apply **immunities**, **weaknesses**, and **resistances **the  subject has to the damage. |
| 8 | `PZO22001 Starfinder Player Core 388-405::/page/14/Text/12` | 0.595820 | A creature with fast healing or  regeneration regains the listed  amount of Hit Points each round  at the beginning of its turn. A  creature with regeneration  has additional benefits. Its  dying cond |
| 9 | `PZO22001 Starfinder Player Core 388-405::/page/11/Text/9` | 0.588356 | Defenses against certain types of damage or effects are called  immunities or resistances, while vulnerabilities are called  weaknesses. Apply immunities first, then weaknesses, and  resistances third |
| 10 | `PZO22001 Starfinder Player Core 388-405::/page/12/Text/3` | 0.588297 | Damage and effects can be negated, deal less damage, or  deal more damage due to the recipient's immunity, weakness,  or resistance. |

### Query 89
- Text: What is the rule about **Related:** Persistent damage condition (page 438)?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/3/Text/20']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 388-405::/page/3/Text/20', 'PZO22001 Starfinder Player Core 388-405::/page/11/Text/1', 'PZO22001 Starfinder Player Core 388-405::/page/2/Text/10']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/3/Text/20', 'PZO22001 Starfinder Player Core 388-405::/page/3/SectionHeader/21', 'PZO22001 Starfinder Player Core 388-405::/page/3/Text/19']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 388-405::/page/3/SectionHeader/21` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/3/Text/19` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/20` | 0.913375 | **Related:** Persistent damage condition (page 438) |
| 2 | `PZO22001 Starfinder Player Core 388-405::/page/11/Text/1` | 0.731892 | you recover from the persistent damage. See the sidebar on  page 438 in the Conditions Appendix for the complete rules  regarding the persistent damage condition. |
| 3 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/10` | 0.571416 | **Related:** Activities (page 406), disrupting actions (page 407) |
| 4 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/18` | 0.501332 | Attacks, spells, and other dangers **deal damage** (page 398).  The amount is typically determined by a **Damage **roll (page  398), which can use a variety of sizes and numbers of dice. |
| 5 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/19` | 0.499594 | Damage reduces the **Hit Points (HP)** (page 402) that  measure a creature's overall health or an object's durability.  A creature might have **immunity** to damage or effects of  certain kinds, a **r |
| 6 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/26` | 0.488537 | **Related:** Area Fire (page 410), cover (page 416), flanking  enemies (page 417), spell attacks (page 394), targeting  creatures (page 418) |
| 7 | `PZO22001 Starfinder Player Core 388-405::/page/10/Text/28` | 0.487726 | Persistent damage is a condition that causes damage to  recur beyond the original effect. Like normal damage, it can  be doubled or halved based on the results of an attack roll  or saving throw. Unli |
| 8 | `PZO22001 Starfinder Player Core 388-405::/page/10/SectionHeader/27` | 0.477451 | PERSISTENT DAMAGE |
| 9 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/23` | 0.475049 | **Related:** Escape a grab or restraint (page 408), falling (page  413), forced movement (page 414), moving through creatures  (page 414), special movement modes (burrow, climb, fly, and  swim; page 4 |
| 10 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/30` | 0.463710 | **Related:** Light (page 424), special senses (page 424) |

### Query 90
- Text: What is the rule about SPELLS?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/3/SectionHeader/21']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 388-405::/page/3/SectionHeader/21', 'PZO22001 Starfinder Player Core 388-405::/page/9/Text/25', 'PZO22001 Starfinder Player Core 388-405::/page/3/Text/38']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/3/SectionHeader/21', 'PZO22001 Starfinder Player Core 388-405::/page/3/Text/22', 'PZO22001 Starfinder Player Core 388-405::/page/3/Text/20']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 388-405::/page/3/Text/22` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/3/Text/20` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 388-405::/page/3/SectionHeader/21` | 0.844517 | SPELLS |
| 2 | `PZO22001 Starfinder Player Core 388-405::/page/9/Text/25` | 0.796446 | **SPELLS** |
| 3 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/38` | 0.796446 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 388-405::/page/13/Text/31` | 0.691237 | **EQUIPMENT** **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/27` | 0.691237 | **EQUIPMENT** **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 388-405::/page/7/Text/19` | 0.691237 | **EQUIPMENT** **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 388-405::/page/7/SectionHeader/5` | 0.527374 | SPELL DC |
| 8 | `PZO22001 Starfinder Player Core 388-405::/page/6/SectionHeader/22` | 0.495799 | SPELL ATTACK ROLLS |
| 9 | `PZO22001 Starfinder Player Core 388-405::/page/7/Text/3` | 0.478489 | Calculate a **spell attack roll** with the following formula. |
| 10 | `PZO22001 Starfinder Player Core 388-405::/page/10/SectionHeader/17` | 0.467280 | **Spell **(or similar effect)** damage roll = damage die of effect ** **+ bonuses + penalties** |

### Query 91
- Text: What is the rule about Most of the rules for casting spells are in Chapter 7 (pages  294–301). For a spell that requires an attack roll against  the target's AC, you'll calculate your **spell attack modifier**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/3/Text/22']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 388-405::/page/3/Text/22', 'PZO22001 Starfinder Player Core 388-405::/page/6/Text/23', 'PZO22001 Starfinder Player Core 388-405::/page/7/Text/6']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/3/Text/22', 'PZO22001 Starfinder Player Core 388-405::/page/3/Text/23', 'PZO22001 Starfinder Player Core 388-405::/page/3/SectionHeader/21']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 388-405::/page/3/Text/23` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/3/SectionHeader/21` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/22` | 1.006593 | Most of the rules for casting spells are in Chapter 7 (pages  294–301). For a spell that requires an attack roll against  the target's AC, you'll calculate your **spell attack modifier** |
| 2 | `PZO22001 Starfinder Player Core 388-405::/page/6/Text/23` | 0.784059 | If you cast spells, you might need to make a spell attack  roll. These rolls are usually made when you cast a spell that  targets a creature's AC. |
| 3 | `PZO22001 Starfinder Player Core 388-405::/page/7/Text/6` | 0.735645 | Many times, instead of requiring you to make a spell attack roll,  the spells you cast require those within the area or targeted  by the spell to attempt a saving throw against your **spell DC** to de |
| 4 | `PZO22001 Starfinder Player Core 388-405::/page/7/Text/2` | 0.690931 | If you have the ability to cast spells, you'll have a  proficiency rank for your spell attack modifier, so you'll  always add a proficiency bonus. Spell attack rolls can benefit  from circumstance bon |
| 5 | `PZO22001 Starfinder Player Core 388-405::/page/7/Text/11` | 0.662326 | Attack rolls are compared to a special DC called **Armor Class ** **(AC)**, which measures how hard it is for your foes to hit you  with Strikes, spell attack rolls, and other attacks. Just like for |
| 6 | `PZO22001 Starfinder Player Core 388-405::/page/7/Text/1` | 0.644680 | The attribute modifier for a spell attack roll depends  on how you gained the spell. If your class grants you  spellcasting, use your key attribute modifier (such as  Wisdom for a mystic). Innate spel |
| 7 | `PZO22001 Starfinder Player Core 388-405::/page/7/Text/4` | 0.633194 | **Spell attack roll result = d20 roll + spellcasting ** **attribute modifier + proficiency bonus + other ** **bonuses + penalties** |
| 8 | `PZO22001 Starfinder Player Core 388-405::/page/7/Text/3` | 0.629031 | Calculate a **spell attack roll** with the following formula. |
| 9 | `PZO22001 Starfinder Player Core 388-405::/page/8/Text/3` | 0.618639 | For example, the number you write down for  your **attack modifier** with your doshko would likely  be your Strength modifier + your proficiency bonus  with martial weapons. Your **spell attack modifi |
| 10 | `PZO22001 Starfinder Player Core 388-405::/page/6/Text/3` | 0.593040 | When you use a Strike action or make a spell attack, you  attempt a check called an attack roll. Attack rolls take a  variety of forms and are often highly variable based on the  weapon you are using |

### Query 92
- Text: What is the rule about (page 394). For one that causes its subject to attempt a  saving throw, you'll need your **spell DC** (page 395).?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/3/Text/23']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 388-405::/page/3/Text/23', 'PZO22001 Starfinder Player Core 388-405::/page/7/Text/6', 'PZO22001 Starfinder Player Core 388-405::/page/3/Text/16']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/3/Text/23', 'PZO22001 Starfinder Player Core 388-405::/page/3/Text/24', 'PZO22001 Starfinder Player Core 388-405::/page/3/Text/22']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 388-405::/page/3/Text/24` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/3/Text/22` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/23` | 0.965494 | (page 394). For one that causes its subject to attempt a  saving throw, you'll need your **spell DC** (page 395). |
| 2 | `PZO22001 Starfinder Player Core 388-405::/page/7/Text/6` | 0.690647 | Many times, instead of requiring you to make a spell attack roll,  the spells you cast require those within the area or targeted  by the spell to attempt a saving throw against your **spell DC** to de |
| 3 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/16` | 0.673023 | Your **Armor Class** **(AC) **(page 395) is the main DC used for  attacks against you. You might also roll a type of check called  a **Saving Throw** (page 396), also called a **save**, against spells |
| 4 | `PZO22001 Starfinder Player Core 388-405::/page/8/Text/16` | 0.610404 | Sometimes you'll need to know your DC for a given saving  throw (such as a Grapple attempt requiring a roll against your  Fortitude DC). Like any other DC derived from a modifier,  the DC for a saving |
| 5 | `PZO22001 Starfinder Player Core 388-405::/page/8/Text/17` | 0.536010 | Most of the time, when you attempt a saving throw,  you don't have to use your actions or your reaction. You  don't even need to be able to act to attempt saving throws.  However, in some special case |
| 6 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/22` | 0.525334 | Most of the rules for casting spells are in Chapter 7 (pages  294–301). For a spell that requires an attack roll against  the target's AC, you'll calculate your **spell attack modifier** |
| 7 | `PZO22001 Starfinder Player Core 388-405::/page/8/Text/19` | 0.522994 | Sometimes you will be called on to attempt a basic saving  throw (or "basic save"). This type of saving throw works  just like any other saving throw—the "basic" part refers to  the effects. For a bas |
| 8 | `PZO22001 Starfinder Player Core 388-405::/page/8/Text/3` | 0.499989 | For example, the number you write down for  your **attack modifier** with your doshko would likely  be your Strength modifier + your proficiency bonus  with martial weapons. Your **spell attack modifi |
| 9 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/12` | 0.481822 | An action that can potentially fail requires rolling a **check** (page 392). Roll a d20 (20-sided die) and identify the modifiers,  bonuses, and penalties that apply. Then, calculate the result,  comp |
| 10 | `PZO22001 Starfinder Player Core 388-405::/page/8/Text/12` | 0.474761 | **Reflex** saving throws measure how well you can respond  quickly to a situation and how gracefully you can avoid  effects that have been thrown at you. They use your Dexterity  modifier and are calc |

### Query 93
- Text: Summarize PERCEPTION AND DETECTION
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/3/SectionHeader/27']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 388-405::/page/3/SectionHeader/27', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/41', 'PZO22001 Starfinder Player Core 388-405::/page/7/Text/34']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/3/SectionHeader/27', 'PZO22001 Starfinder Player Core 388-405::/page/3/Text/26', 'PZO22001 Starfinder Player Core 388-405::/page/3/Text/28']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 388-405::/page/3/Text/26` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/3/Text/28` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 388-405::/page/3/SectionHeader/27` | 0.986931 | PERCEPTION AND DETECTION |
| 2 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/41` | 0.849667 | **Perception and ** **Detection** |
| 3 | `PZO22001 Starfinder Player Core 388-405::/page/7/Text/34` | 0.849667 | **Perception and ** **Detection** |
| 4 | `PZO22001 Starfinder Player Core 388-405::/page/13/Text/45` | 0.807667 | **Perception and ** **Detection** |
| 5 | `PZO22001 Starfinder Player Core 388-405::/page/5/Text/36` | 0.807667 | **Perception and ** **Detection** |
| 6 | `PZO22001 Starfinder Player Core 388-405::/page/17/Text/30` | 0.807667 | **Perception and ** **Detection** |
| 7 | `PZO22001 Starfinder Player Core 388-405::/page/15/Text/39` | 0.807667 | **Perception and ** **Detection** |
| 8 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/52` | 0.807667 | **Perception and ** **Detection** |
| 9 | `PZO22001 Starfinder Player Core 388-405::/page/11/Text/35` | 0.807667 | **Perception and ** **Detection** |
| 10 | `PZO22001 Starfinder Player Core 388-405::/page/9/Text/39` | 0.807667 | **Perception and ** **Detection** |

### Query 94
- Text: Summarize Four main conditions indicate how well you can pinpoint  and target a creature: **observed**, **hidden**, **undetected**, and  **unnoticed** (page 425). A creature with the **concealed** or  **invisible** condition is harder to find and target (page 426).
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/3/Text/29']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 388-405::/page/3/Text/29', 'PZO22001 Starfinder Player Core 388-405::/page/2/Text/23', 'PZO22001 Starfinder Player Core 388-405::/page/3/Text/28']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/3/Text/29', 'PZO22001 Starfinder Player Core 388-405::/page/3/Text/30', 'PZO22001 Starfinder Player Core 388-405::/page/3/Text/28']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 388-405::/page/3/Text/30` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/3/Text/28` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/29` | 1.045404 | Four main conditions indicate how well you can pinpoint  and target a creature: **observed**, **hidden**, **undetected**, and  **unnoticed** (page 425). A creature with the **concealed** or  **invisib |
| 2 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/23` | 0.586368 | **Related:** Escape a grab or restraint (page 408), falling (page  413), forced movement (page 414), moving through creatures  (page 414), special movement modes (burrow, climb, fly, and  swim; page 4 |
| 3 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/28` | 0.581573 | Your **Perception **modifier (page 396) indicates how good you  are at noticing things around you. You typically use the **Seek** basic action (page 409) to find physical things or the **Sense ** **Mo |
| 4 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/22` | 0.532326 | Creatures can get tactical advantages by careful positioning.  The most common are using **cover** from terrain and other  creatures to increase your AC (page 416), and **flanking** (page  417), which |
| 5 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/26` | 0.520627 | **Related:** Area Fire (page 410), cover (page 416), flanking  enemies (page 417), spell attacks (page 394), targeting  creatures (page 418) |
| 6 | `PZO22001 Starfinder Player Core 388-405::/page/8/Text/22` | 0.512171 | Perception measures your ability to be aware of your  environment. Every creature has Perception, which works  with and is limited by a creature's senses. (Details on senses  and detecting things begi |
| 7 | `PZO22001 Starfinder Player Core 388-405::/page/7/Text/34` | 0.505512 | **Perception and ** **Detection** |
| 8 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/41` | 0.505512 | **Perception and ** **Detection** |
| 9 | `PZO22001 Starfinder Player Core 388-405::/page/17/Text/30` | 0.505512 | **Perception and ** **Detection** |
| 10 | `PZO22001 Starfinder Player Core 388-405::/page/13/Text/45` | 0.505512 | **Perception and ** **Detection** |

### Query 95
- Text: Summarize **Related:** Light (page 424), special senses (page 424)
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/3/Text/30']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 388-405::/page/3/Text/30', 'PZO22001 Starfinder Player Core 388-405::/page/2/Text/23', 'PZO22001 Starfinder Player Core 388-405::/page/2/Text/26']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/3/Text/30', 'PZO22001 Starfinder Player Core 388-405::/page/3/Text/29', 'PZO22001 Starfinder Player Core 388-405::/page/3/Text/32']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 388-405::/page/3/Text/29` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/3/Text/32` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/30` | 1.031026 | **Related:** Light (page 424), special senses (page 424) |
| 2 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/23` | 0.577074 | **Related:** Escape a grab or restraint (page 408), falling (page  413), forced movement (page 414), moving through creatures  (page 414), special movement modes (burrow, climb, fly, and  swim; page 4 |
| 3 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/26` | 0.571518 | **Related:** Area Fire (page 410), cover (page 416), flanking  enemies (page 417), spell attacks (page 394), targeting  creatures (page 418) |
| 4 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/10` | 0.497136 | **Related:** Activities (page 406), disrupting actions (page 407) |
| 5 | `PZO22001 Starfinder Player Core 388-405::/page/13/Text/12` | 0.465671 | of which are described in the sidebar on page 39, and on  pages 448 and 456. |
| 6 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/15` | 0.459765 | **Related:** Flat checks and secret checks (sidebar on page  397), fortune and misfortune (sidebar on page 393) |
| 7 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/20` | 0.453227 | **Related:** Persistent damage condition (page 438) |
| 8 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/28` | 0.451468 | Your **Perception **modifier (page 396) indicates how good you  are at noticing things around you. You typically use the **Seek** basic action (page 409) to find physical things or the **Sense ** **Mo |
| 9 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/24` | 0.439357 | **Related: **Dismiss and Sustain basic actions (page 411) |
| 10 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/29` | 0.431423 | Four main conditions indicate how well you can pinpoint  and target a creature: **observed**, **hidden**, **undetected**, and  **unnoticed** (page 425). A creature with the **concealed** or  **invisib |

### Query 96
- Text: Summarize **INTRODUCTION**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/3/Text/32']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 388-405::/page/1/Text/22', 'PZO22001 Starfinder Player Core 388-405::/page/15/Text/19', 'PZO22001 Starfinder Player Core 388-405::/page/3/Text/32']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/3/Text/32', 'PZO22001 Starfinder Player Core 388-405::/page/3/Text/30', 'PZO22001 Starfinder Player Core 388-405::/page/3/Text/33']
- Expanded expected found: `True`
- Expanded expected rank: `3`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 388-405::/page/3/Text/30` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/3/Text/33` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/22` | 0.880541 | **INTRODUCTION** |
| 2 | `PZO22001 Starfinder Player Core 388-405::/page/15/Text/19` | 0.880541 | **INTRODUCTION** |
| 3 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/32` | 0.880541 | **INTRODUCTION** |
| 4 | `PZO22001 Starfinder Player Core 388-405::/page/7/Text/14` | 0.838541 | **INTRODUCTION** |
| 5 | `PZO22001 Starfinder Player Core 388-405::/page/13/Text/25` | 0.838541 | **INTRODUCTION** |
| 6 | `PZO22001 Starfinder Player Core 388-405::/page/9/Text/19` | 0.838541 | **INTRODUCTION** |
| 7 | `PZO22001 Starfinder Player Core 388-405::/page/11/Text/15` | 0.838541 | **INTRODUCTION** |
| 8 | `PZO22001 Starfinder Player Core 388-405::/page/17/Text/11` | 0.838541 | **INTRODUCTION** |
| 9 | `PZO22001 Starfinder Player Core 388-405::/page/9/Text/27` | 0.457803 | **Rules Overview** |
| 10 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/40` | 0.457803 | **Rules Overview** |

### Query 97
- Text: Summarize **CLASSES**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/3/Text/34']
- Expected found: `True`
- Expected rank: `7`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 388-405::/page/17/Text/13', 'PZO22001 Starfinder Player Core 388-405::/page/15/Text/21', 'PZO22001 Starfinder Player Core 388-405::/page/9/Text/21']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/3/Text/34', 'PZO22001 Starfinder Player Core 388-405::/page/11/Text/17', 'PZO22001 Starfinder Player Core 388-405::/page/17/Text/13', 'PZO22001 Starfinder Player Core 388-405::/page/15/Text/21', 'PZO22001 Starfinder Player Core 388-405::/page/1/Text/24', 'PZO22001 Starfinder Player Core 388-405::/page/9/Text/21', 'PZO22001 Starfinder Player Core 388-405::/page/13/Text/27', 'PZO22001 Starfinder Player Core 388-405::/page/3/Text/35', 'PZO22001 Starfinder Player Core 388-405::/page/3/Text/33', 'PZO22001 Starfinder Player Core 388-405::/page/7/Text/16']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 388-405::/page/11/Text/17` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/17/Text/13` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/15/Text/21` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/1/Text/24` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/9/Text/21` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/13/Text/27` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/3/Text/35` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/3/Text/33` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/7/Text/16` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 388-405::/page/17/Text/13` | 0.940061 | **CLASSES** |
| 2 | `PZO22001 Starfinder Player Core 388-405::/page/15/Text/21` | 0.940061 | **CLASSES** |
| 3 | `PZO22001 Starfinder Player Core 388-405::/page/9/Text/21` | 0.940061 | **CLASSES** |
| 4 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/24` | 0.910061 | **CLASSES** |
| 5 | `PZO22001 Starfinder Player Core 388-405::/page/13/Text/27` | 0.910061 | **CLASSES** |
| 6 | `PZO22001 Starfinder Player Core 388-405::/page/11/Text/17` | 0.910061 | **CLASSES** |
| 7 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/34` | 0.910061 | **CLASSES** |
| 8 | `PZO22001 Starfinder Player Core 388-405::/page/7/Text/16` | 0.910061 | **CLASSES** |
| 9 | `PZO22001 Starfinder Player Core 388-405::/page/5/Text/53` | 0.521344 | **INTRODUCTION** **ANCESTRIES & ** **BACKGROUNDS** **CLASSES** **SKILLS** **FEATS** **EQUIPMENT** **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 388-405::/page/7/SectionHeader/10` | 0.467480 | ARMOR CLASS |

### Query 98
- Text: Summarize **EQUIPMENT**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/3/Text/37']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 388-405::/page/17/Text/16', 'PZO22001 Starfinder Player Core 388-405::/page/11/Text/20', 'PZO22001 Starfinder Player Core 388-405::/page/3/Text/37']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/3/Text/37', 'PZO22001 Starfinder Player Core 388-405::/page/3/Text/38', 'PZO22001 Starfinder Player Core 388-405::/page/3/Text/36']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 388-405::/page/3/Text/38` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/3/Text/36` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/37` | 0.944726 | **EQUIPMENT** |
| 2 | `PZO22001 Starfinder Player Core 388-405::/page/11/Text/20` | 0.944726 | **EQUIPMENT** |
| 3 | `PZO22001 Starfinder Player Core 388-405::/page/17/Text/16` | 0.944726 | **EQUIPMENT** |
| 4 | `PZO22001 Starfinder Player Core 388-405::/page/15/Text/24` | 0.902726 | **EQUIPMENT** |
| 5 | `PZO22001 Starfinder Player Core 388-405::/page/9/Text/24` | 0.902726 | **EQUIPMENT** |
| 6 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/27` | 0.578761 | **EQUIPMENT** **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 388-405::/page/13/Text/31` | 0.578761 | **EQUIPMENT** **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 388-405::/page/7/Text/19` | 0.578761 | **EQUIPMENT** **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 388-405::/page/5/Text/53` | 0.490885 | **INTRODUCTION** **ANCESTRIES & ** **BACKGROUNDS** **CLASSES** **SKILLS** **FEATS** **EQUIPMENT** **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/37` | 0.393793 | **Movement** |

### Query 99
- Text: Summarize **PLAYING THE ** **GAME**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/3/Text/39']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 388-405::/page/1/Text/28', 'PZO22001 Starfinder Player Core 388-405::/page/3/Text/39', 'PZO22001 Starfinder Player Core 388-405::/page/13/Text/32']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/3/Text/39', 'PZO22001 Starfinder Player Core 388-405::/page/3/Text/38', 'PZO22001 Starfinder Player Core 388-405::/page/3/Text/40']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 388-405::/page/3/Text/38` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/3/Text/40` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 388-405::/page/1/Text/28` | 0.965000 | **PLAYING THE ** **GAME** |
| 2 | `PZO22001 Starfinder Player Core 388-405::/page/3/Text/39` | 0.965000 | **PLAYING THE ** **GAME** |
| 3 | `PZO22001 Starfinder Player Core 388-405::/page/13/Text/32` | 0.965000 | **PLAYING THE ** **GAME** |
| 4 | `PZO22001 Starfinder Player Core 388-405::/page/5/Text/23` | 0.923000 | **PLAYING THE ** **GAME** |
| 5 | `PZO22001 Starfinder Player Core 388-405::/page/9/Text/26` | 0.923000 | **PLAYING THE ** **GAME** |
| 6 | `PZO22001 Starfinder Player Core 388-405::/page/7/Text/20` | 0.923000 | **PLAYING THE ** **GAME** |
| 7 | `PZO22001 Starfinder Player Core 388-405::/page/15/Text/25` | 0.811006 | **PLAYING THE ** |
| 8 | `PZO22001 Starfinder Player Core 388-405::/page/11/Text/21` | 0.811006 | **PLAYING THE ** |
| 9 | `PZO22001 Starfinder Player Core 388-405::/page/17/Text/17` | 0.811006 | **PLAYING THE ** |
| 10 | `PZO22001 Starfinder Player Core 388-405::/page/1/SectionHeader/0` | 0.724027 | CHAPTER 8: PLAYING THE GAME |

### Query 100
- Text: Lookup values for Proficiency RankProficiency BonusUntrained0TrainedYour level + 2ExpertYour level + 4MasterYour level + 6LegendaryYour level + 8
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/4/Table/20']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 388-405::/page/4/Table/20', 'PZO22001 Starfinder Player Core 388-405::/page/4/Text/19', 'PZO22001 Starfinder Player Core 388-405::/page/9/Text/9']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/4/Table/20', 'PZO22001 Starfinder Player Core 388-405::/page/4/Text/19', 'PZO22001 Starfinder Player Core 388-405::/page/4/TableCell/343']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 388-405::/page/4/Text/19` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/4/TableCell/343` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 388-405::/page/4/Table/20` | 0.989019 | Proficiency RankProficiency BonusUntrained0TrainedYour level + 2ExpertYour level + 4MasterYour level + 6LegendaryYour level + 8 |
| 2 | `PZO22001 Starfinder Player Core 388-405::/page/4/Text/19` | 0.754099 | master, or legendary. If you're untrained, your bonus is +0—you  must rely on raw talent and any situational bonuses. Otherwise,  the bonus equals your character's level plus a certain amount  dependi |
| 3 | `PZO22001 Starfinder Player Core 388-405::/page/9/Text/9` | 0.729638 | You're unlikely to be trained in every skill. As normal,  when using a skill in which you're untrained, your proficiency  bonus is +0; otherwise, it equals your level plus 2 for trained,  or higher on |
| 4 | `PZO22001 Starfinder Player Core 388-405::/page/4/Text/18` | 0.678414 | When attempting a check that involves something you have  some training in, you also add your **proficiency bonus**. This bonus  depends on your proficiency rank: untrained, trained, expert, |
| 5 | `PZO22001 Starfinder Player Core 388-405::/page/6/Text/8` | 0.607973 | When attacking with a weapon, whether melee or ranged,  you add your proficiency bonus for the weapon you're using.  Your class determines your proficiency rank for various  weapons. Sometimes, you'll |
| 6 | `PZO22001 Starfinder Player Core 388-405::/page/4/TableCell/343` | 0.596204 | Proficiency Rank |
| 7 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/13` | 0.574520 | Most checks are modified by your **attribute modifier** (Strength, Dexterity, Constitution, Intelligence, Wisdom, or  Charisma) and your **proficiency modifier** (untrained, trained,  expert, master, |
| 8 | `PZO22001 Starfinder Player Core 388-405::/page/4/TableCell/344` | 0.571541 | Proficiency Bonus |
| 9 | `PZO22001 Starfinder Player Core 388-405::/page/5/Text/49` | 0.568639 | Proficiency bonus Circumstance bonus Status bonus Item bonus |
| 10 | `PZO22001 Starfinder Player Core 388-405::/page/9/Text/8` | 0.546419 | **Skill check result = d20 roll + the skill's key attribute ** **modifier + proficiency bonus + other bonuses + penalties** |

### Query 101
- Text: Lookup values for AttackMultiple Attack PenaltyAgileFirstNoneNoneSecond–5–4Third or subsequent–10–8
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/6/Table/14']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 388-405::/page/6/Table/14', 'PZO22001 Starfinder Player Core 388-405::/page/6/TableCell/355', 'PZO22001 Starfinder Player Core 388-405::/page/6/SectionHeader/11']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 388-405::/page/6/Table/14', 'PZO22001 Starfinder Player Core 388-405::/page/6/Text/13', 'PZO22001 Starfinder Player Core 388-405::/page/6/TableCell/354']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 388-405::/page/6/Text/13` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 388-405::/page/6/TableCell/354` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 388-405::/page/6/Table/14` | 0.971117 | AttackMultiple Attack PenaltyAgileFirstNoneNoneSecond–5–4Third or subsequent–10–8 |
| 2 | `PZO22001 Starfinder Player Core 388-405::/page/6/TableCell/355` | 0.759526 | Multiple Attack Penalty |
| 3 | `PZO22001 Starfinder Player Core 388-405::/page/6/SectionHeader/11` | 0.654761 | MULTIPLE ATTACK PENALTY |
| 4 | `PZO22001 Starfinder Player Core 388-405::/page/6/Text/13` | 0.607551 | Some weapons and abilities reduce multiple attack penalties,  such as agile weapons, which reduce these penalties to –4 on  the second attack or –8 on further attacks. |
| 5 | `PZO22001 Starfinder Player Core 388-405::/page/6/Text/12` | 0.606649 | The more attacks you make beyond your first in a single turn, the  less accurate you become, represented by the **multiple attack ** **penalty**. The second time you use an attack action during your |
| 6 | `PZO22001 Starfinder Player Core 388-405::/page/6/Text/15` | 0.585778 | Always calculate your multiple attack penalty based on  the weapon you're using on that attack, not ones you used  on previous attacks. For example, let's say you're wielding a  plasma sword in one ha |
| 7 | `PZO22001 Starfinder Player Core 388-405::/page/6/Text/16` | 0.555382 | The multiple attack penalty applies only during your turn,  so you don't have to keep track of it if you can perform a  Reactive Strike or a similar reaction that lets you make a  Strike on someone el |
| 8 | `PZO22001 Starfinder Player Core 388-405::/page/6/Text/10` | 0.523215 | Penalties to attack rolls come from situations and effects  as well. Circumstance penalties come from risky tactics or  detrimental circumstances, status penalties come from spells  and magic working |
| 9 | `PZO22001 Starfinder Player Core 388-405::/page/2/Text/25` | 0.495279 | **Strike** (page 410) actions have the attack trait and allow you  to attack with a weapon you're wielding or an unarmed attack  (such as a tail). If you're using a melee weapon or unarmed  attack, yo |
| 10 | `PZO22001 Starfinder Player Core 388-405::/page/5/Text/1` | 0.481122 | Unlike bonuses, penalties can also be **untyped**, in which case  they won't be classified as "circumstance," "item," or "status."  Unlike other penalties, you always add all your untyped penalties  t |
