# RulesLawyer Evaluation Report: nomic-embed-text-v2

## Summary
- Run ID: `None`
- Ruleset ID: `None`
- Document ID: `None`
- Chunk source: `enriched`
- Chunk count: `506`
- Query count: `100`
- Evaluated queries: `100`
- Coverage: `1.0000`
- MRR: `0.9171`
- hit@1: `0.8800`
- hit@3: `0.9400`
- hit@5: `0.9600`
- hit@10: `0.9800`
- Embeddings reused: `False`
- Graph boost: `0.05` (depth=2, top_k=50, source=top, seed_top_n=3, same_kind_only=False, decay=0.4)

## Timings (ms)
- Embedding (chunks): `8366`
- Embedding (queries): `3043`
- Evaluation (strict): `19`
- Evaluation (expanded): `0`
- Total: `15825`

### Timing Estimates (ms)
- Evaluation (strict): `20`
- Evaluation (expanded): `None`
- Total: `11429`

## Query Details
### Query 0
- Text: Summarize EXPLORING THE  GALAXY
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 030-039::/page/0/SectionHeader/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 030-039::/page/0/SectionHeader/1', 'PZO22001 Starfinder Player Core 030-039::/page/5/Text/55', 'PZO22001 Starfinder Player Core 030-039::/page/3/Text/34']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 030-039::/page/0/SectionHeader/1` | 0.954115 | EXPLORING THE  GALAXY |
| 2 | `PZO22001 Starfinder Player Core 030-039::/page/5/Text/55` | 0.737074 | **Exploring the ** **Galaxy** |
| 3 | `PZO22001 Starfinder Player Core 030-039::/page/3/Text/34` | 0.737074 | **Exploring the ** **Galaxy** |
| 4 | `PZO22001 Starfinder Player Core 030-039::/page/9/Text/44` | 0.695074 | **Exploring the ** **Galaxy** |
| 5 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/31` | 0.695074 | **Exploring the ** **Galaxy** |
| 6 | `PZO22001 Starfinder Player Core 030-039::/page/7/Text/83` | 0.695074 | **Exploring the ** **Galaxy** |
| 7 | `PZO22001 Starfinder Player Core 030-039::/page/0/ListItem/13` | 0.471417 | **The galaxy is diverse.** Countless worlds and cultures  flourish all over the galaxy (and beyond). Travelers  from Near Space often visit the Pact Worlds (and vice  versa). Visitors from the Vast ar |
| 8 | `PZO22001 Starfinder Player Core 030-039::/page/8/Text/46` | 0.459375 | Weydan enjoys discovery and exploration with  a purpose. He believes everyone deserves the equal right  to pursue such experiences and walks the galaxy in diverse  avatars to commune with his follower |
| 9 | `PZO22001 Starfinder Player Core 030-039::/page/0/ListItem/9` | 0.455300 | **The galaxy** **is magical.** Proof of people who magically  change reality and channel the primeval forces of the  universe is everywhere, and people know that it's  real. Magic and technology often |
| 10 | `PZO22001 Starfinder Player Core 030-039::/page/0/ListItem/14` | 0.453828 | **The galaxy is dangerous.** Among the planets occupied by  the allied Pact Worlds to Near Space and the remote Vast,  there's usually something causing trouble somewhere.  Adventurers are always seek |

### Query 1
- Text: What is the rule about While some players prefer to create a character and define them solely through roleplay, other players  might wish to tie their character into the world through backstory and motives. Knowing the setting  of the world you intend to play in can help flesh out your character, or even give rise to new ideas for  a character that you hadn't considered.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 030-039::/page/0/Text/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 030-039::/page/0/Text/2', 'PZO22001 Starfinder Player Core 030-039::/page/1/Text/17', 'PZO22001 Starfinder Player Core 030-039::/page/0/Text/8']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 030-039::/page/0/Text/2` | 0.978757 | While some players prefer to create a character and define them solely through roleplay, other players  might wish to tie their character into the world through backstory and motives. Knowing the sett |
| 2 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/17` | 0.658134 | In fact, you don't have to use this setting! While  the Starfinder RPG rules do make some assumptions  about the world, many of these assumptions are  common within the science fantasy genre. Elements |
| 3 | `PZO22001 Starfinder Player Core 030-039::/page/0/Text/8` | 0.647274 | As someone who lives in a science fantasy universe, your  character has a different set of assumptions than someone  from modern Earth. The following are some of these setting  assumptions to keep in |
| 4 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/16` | 0.565829 | Feel free to make the galaxy your own! If something  we write in our books gets in the way of a concept you  want to play, ask your group and your GM if you can  change it. What's important isn't that |
| 5 | `PZO22001 Starfinder Player Core 030-039::/page/0/Text/4` | 0.547517 | The Starfinder Roleplaying Game rules come with their own  default setting: the galaxy known as Desna's Path. The galaxy  is full of wonder and peril, advanced technology, magic,  meddling deities, an |
| 6 | `PZO22001 Starfinder Player Core 030-039::/page/0/SectionHeader/7` | 0.465606 | WHAT DOES MY CHARACTER  KNOW? |
| 7 | `PZO22001 Starfinder Player Core 030-039::/page/6/Text/2` | 0.420516 | The cleric spells listed for each deity are intended  to work with the cleric class found in the Pathfinder  Roleplaying Game. Similarly, clerics and some other  devotees can gain domain spells from t |
| 8 | `PZO22001 Starfinder Player Core 030-039::/page/9/Text/42` | 0.414997 | **Character ** **Creation** |
| 9 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/29` | 0.414997 | **Character ** **Creation** |
| 10 | `PZO22001 Starfinder Player Core 030-039::/page/5/Text/53` | 0.414997 | **Character ** **Creation** |

### Query 2
- Text: What is the rule about The Starfinder Roleplaying Game rules come with their own  default setting: the galaxy known as Desna's Path. The galaxy  is full of wonder and peril, advanced technology, magic,  meddling deities, and countless new worlds to explore.  Starfinder's setting combines elements of science fiction with  classic fantasy elements while taking inspiration from the  modern world. All kinds of characters can find a place in the  galaxy, and there are many galactic events, people, and plot  hooks that a player can base a character around.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 030-039::/page/0/Text/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 030-039::/page/0/Text/4', 'PZO22001 Starfinder Player Core 030-039::/page/1/Text/17', 'PZO22001 Starfinder Player Core 030-039::/page/0/Text/8']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 030-039::/page/0/Text/4` | 1.014087 | The Starfinder Roleplaying Game rules come with their own  default setting: the galaxy known as Desna's Path. The galaxy  is full of wonder and peril, advanced technology, magic,  meddling deities, an |
| 2 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/17` | 0.823221 | In fact, you don't have to use this setting! While  the Starfinder RPG rules do make some assumptions  about the world, many of these assumptions are  common within the science fantasy genre. Elements |
| 3 | `PZO22001 Starfinder Player Core 030-039::/page/0/Text/8` | 0.692426 | As someone who lives in a science fantasy universe, your  character has a different set of assumptions than someone  from modern Earth. The following are some of these setting  assumptions to keep in |
| 4 | `PZO22001 Starfinder Player Core 030-039::/page/6/Text/2` | 0.612814 | The cleric spells listed for each deity are intended  to work with the cleric class found in the Pathfinder  Roleplaying Game. Similarly, clerics and some other  devotees can gain domain spells from t |
| 5 | `PZO22001 Starfinder Player Core 030-039::/page/4/Text/2` | 0.573817 | A prominent group of adventurers, explorers, and  record-keepers, the Starfinder Society is well known  across the galaxy. This name is shared with Paizo's  official organized play campaign played aro |
| 6 | `PZO22001 Starfinder Player Core 030-039::/page/0/Text/6` | 0.556056 | Starfinder occurs in the far future after the Age of Lost Omens,  but there's a Gap in the galaxy's history. About 300 years  ago, something erased an entire era from memory. Records  for this forgott |
| 7 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/16` | 0.545702 | Feel free to make the galaxy your own! If something  we write in our books gets in the way of a concept you  want to play, ask your group and your GM if you can  change it. What's important isn't that |
| 8 | `PZO22001 Starfinder Player Core 030-039::/page/1/ListItem/8` | 0.543057 | A Starfinder exploring magitech ruins left by the  First Ones, risking encounters with deadly traps and  terrifying sentries. |
| 9 | `PZO22001 Starfinder Player Core 030-039::/page/0/Text/2` | 0.538428 | While some players prefer to create a character and define them solely through roleplay, other players  might wish to tie their character into the world through backstory and motives. Knowing the sett |
| 10 | `PZO22001 Starfinder Player Core 030-039::/page/0/ListItem/14` | 0.499998 | **The galaxy is dangerous.** Among the planets occupied by  the allied Pact Worlds to Near Space and the remote Vast,  there's usually something causing trouble somewhere.  Adventurers are always seek |

### Query 3
- Text: Summarize THE GAP
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 030-039::/page/0/SectionHeader/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 030-039::/page/0/SectionHeader/5', 'PZO22001 Starfinder Player Core 030-039::/page/0/Text/6', 'PZO22001 Starfinder Player Core 030-039::/page/0/SectionHeader/1']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 030-039::/page/0/SectionHeader/5` | 0.961821 | THE GAP |
| 2 | `PZO22001 Starfinder Player Core 030-039::/page/0/Text/6` | 0.374728 | Starfinder occurs in the far future after the Age of Lost Omens,  but there's a Gap in the galaxy's history. About 300 years  ago, something erased an entire era from memory. Records  for this forgott |
| 3 | `PZO22001 Starfinder Player Core 030-039::/page/0/SectionHeader/1` | 0.352455 | EXPLORING THE  GALAXY |
| 4 | `PZO22001 Starfinder Player Core 030-039::/page/2/Text/30` | 0.306881 | The Diaspora is an asteroid belt formed long before the  Gap, when a terrible cataclysm destroyed the twin planets  Damiar and Iovo. The remains of the two destroyed worlds  float among millions of ch |
| 5 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/5` | 0.301844 | Aballon is a rocky, cratered world of superheated metallic  deserts and deep ice wells. Thousands of years before the  Gap, a mysterious civilization called the First Ones utilized  Aballon's abundant |
| 6 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/25` | 0.290467 | Floating in lost Golarion's empty orbit, this bustling space  station is the center of interstellar trade and governance  in the Pact Worlds. Nobody knows who built Absalom  Station because it appeare |
| 7 | `PZO22001 Starfinder Player Core 030-039::/page/9/Text/56` | 0.290163 | **GAME** |
| 8 | `PZO22001 Starfinder Player Core 030-039::/page/1/SectionHeader/24` | 0.270217 | **Galactic Trade Nexus** |
| 9 | `PZO22001 Starfinder Player Core 030-039::/page/4/SectionHeader/27` | 0.268614 | THE VAST |
| 10 | `PZO22001 Starfinder Player Core 030-039::/page/0/ListItem/14` | 0.267222 | **The galaxy is dangerous.** Among the planets occupied by  the allied Pact Worlds to Near Space and the remote Vast,  there's usually something causing trouble somewhere.  Adventurers are always seek |

### Query 4
- Text: Summarize Starfinder occurs in the far future after the Age of Lost Omens,  but there's a Gap in the galaxy's history. About 300 years  ago, something erased an entire era from memory. Records  for this forgotten era simply don't exist. People who lived  through the Gap experienced a collective amnesia about its  events. Magic can't bridge the broken timeline, and even the  gods won't reveal what occurred. During this nebulous time  that might have spanned a few years or several centuries,  societies changed, the planet Golarion disappeared, and  Absalom Station was built with the *Starstone* at its core. A  few years later, Drift travel came to the galaxy, and a new age  of interstellar adventure began.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 030-039::/page/0/Text/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 030-039::/page/0/Text/6', 'PZO22001 Starfinder Player Core 030-039::/page/1/Text/25', 'PZO22001 Starfinder Player Core 030-039::/page/0/ListItem/12']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 030-039::/page/0/Text/6` | 1.042003 | Starfinder occurs in the far future after the Age of Lost Omens,  but there's a Gap in the galaxy's history. About 300 years  ago, something erased an entire era from memory. Records  for this forgott |
| 2 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/25` | 0.681012 | Floating in lost Golarion's empty orbit, this bustling space  station is the center of interstellar trade and governance  in the Pact Worlds. Nobody knows who built Absalom  Station because it appeare |
| 3 | `PZO22001 Starfinder Player Core 030-039::/page/0/ListItem/12` | 0.659313 | **The galaxy is connected.** Adventurers have used magical  engines and powerful spells to explore the galaxy  since ancient times, but such travel was rare until the  god Triune introduced hyperspace |
| 4 | `PZO22001 Starfinder Player Core 030-039::/page/0/Text/4` | 0.569390 | The Starfinder Roleplaying Game rules come with their own  default setting: the galaxy known as Desna's Path. The galaxy  is full of wonder and peril, advanced technology, magic,  meddling deities, an |
| 5 | `PZO22001 Starfinder Player Core 030-039::/page/0/Text/16` | 0.564570 | The Pact Worlds form the core of the Starfinder setting.  "The Pact Worlds" is the formal name for the united planets  orbiting lost Golarion's sun and their more distant allied  worlds, including Pul |
| 6 | `PZO22001 Starfinder Player Core 030-039::/page/1/ListItem/8` | 0.561946 | A Starfinder exploring magitech ruins left by the  First Ones, risking encounters with deadly traps and  terrifying sentries. |
| 7 | `PZO22001 Starfinder Player Core 030-039::/page/4/Text/2` | 0.533303 | A prominent group of adventurers, explorers, and  record-keepers, the Starfinder Society is well known  across the galaxy. This name is shared with Paizo's  official organized play campaign played aro |
| 8 | `PZO22001 Starfinder Player Core 030-039::/page/4/SectionHeader/1` | 0.507005 | **STARFINDER SOCIETY** |
| 9 | `PZO22001 Starfinder Player Core 030-039::/page/3/Text/10` | 0.496616 | Once, Triaxus's wandering orbit created an intense seasonal  cycle of steamy, fertile summers and brutal winters that  lasted hundreds of years. The planet's ecologies, landscape,  and inhabitants cha |
| 10 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/17` | 0.496559 | In fact, you don't have to use this setting! While  the Starfinder RPG rules do make some assumptions  about the world, many of these assumptions are  common within the science fantasy genre. Elements |

### Query 5
- Text: What is the rule about WHAT DOES MY CHARACTER  KNOW??
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 030-039::/page/0/SectionHeader/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 030-039::/page/0/SectionHeader/7', 'PZO22001 Starfinder Player Core 030-039::/page/1/Text/29', 'PZO22001 Starfinder Player Core 030-039::/page/3/Text/32']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 030-039::/page/0/SectionHeader/7` | 0.865911 | WHAT DOES MY CHARACTER  KNOW? |
| 2 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/29` | 0.454440 | **Character ** **Creation** |
| 3 | `PZO22001 Starfinder Player Core 030-039::/page/3/Text/32` | 0.454440 | **Character ** **Creation** |
| 4 | `PZO22001 Starfinder Player Core 030-039::/page/5/Text/53` | 0.412439 | **Character ** **Creation** |
| 5 | `PZO22001 Starfinder Player Core 030-039::/page/7/Text/81` | 0.412439 | **Character ** **Creation** |
| 6 | `PZO22001 Starfinder Player Core 030-039::/page/9/Text/42` | 0.412439 | **Character ** **Creation** |
| 7 | `PZO22001 Starfinder Player Core 030-039::/page/0/Text/8` | 0.374843 | As someone who lives in a science fantasy universe, your  character has a different set of assumptions than someone  from modern Earth. The following are some of these setting  assumptions to keep in |
| 8 | `PZO22001 Starfinder Player Core 030-039::/page/6/Text/53` | 0.365914 | **Domains** knowledge, star (*Divine* *Mysteries*), sun, void (*Divine* *Mysteries*) |
| 9 | `PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/1` | 0.361218 | Example Characters |
| 10 | `PZO22001 Starfinder Player Core 030-039::/page/3/SectionHeader/22` | 0.361218 | Example Characters |

### Query 6
- Text: What is the rule about As someone who lives in a science fantasy universe, your  character has a different set of assumptions than someone  from modern Earth. The following are some of these setting  assumptions to keep in mind as you create your character.  For more information on the galaxy and its cultures, see  *Starfinder Galaxy Guide*.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 030-039::/page/0/Text/8']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 030-039::/page/0/Text/8', 'PZO22001 Starfinder Player Core 030-039::/page/1/Text/17', 'PZO22001 Starfinder Player Core 030-039::/page/0/Text/4']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 030-039::/page/0/Text/8` | 1.002887 | As someone who lives in a science fantasy universe, your  character has a different set of assumptions than someone  from modern Earth. The following are some of these setting  assumptions to keep in |
| 2 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/17` | 0.809042 | In fact, you don't have to use this setting! While  the Starfinder RPG rules do make some assumptions  about the world, many of these assumptions are  common within the science fantasy genre. Elements |
| 3 | `PZO22001 Starfinder Player Core 030-039::/page/0/Text/4` | 0.658300 | The Starfinder Roleplaying Game rules come with their own  default setting: the galaxy known as Desna's Path. The galaxy  is full of wonder and peril, advanced technology, magic,  meddling deities, an |
| 4 | `PZO22001 Starfinder Player Core 030-039::/page/0/Text/2` | 0.597634 | While some players prefer to create a character and define them solely through roleplay, other players  might wish to tie their character into the world through backstory and motives. Knowing the sett |
| 5 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/16` | 0.589945 | Feel free to make the galaxy your own! If something  we write in our books gets in the way of a concept you  want to play, ask your group and your GM if you can  change it. What's important isn't that |
| 6 | `PZO22001 Starfinder Player Core 030-039::/page/0/ListItem/9` | 0.510213 | **The galaxy** **is magical.** Proof of people who magically  change reality and channel the primeval forces of the  universe is everywhere, and people know that it's  real. Magic and technology often |
| 7 | `PZO22001 Starfinder Player Core 030-039::/page/6/Text/2` | 0.473998 | The cleric spells listed for each deity are intended  to work with the cleric class found in the Pathfinder  Roleplaying Game. Similarly, clerics and some other  devotees can gain domain spells from t |
| 8 | `PZO22001 Starfinder Player Core 030-039::/page/0/ListItem/10` | 0.457099 | **The galaxy has technology.** Tech from computers  to starship systems are part of everyday life. |
| 9 | `PZO22001 Starfinder Player Core 030-039::/page/0/ListItem/14` | 0.457072 | **The galaxy is dangerous.** Among the planets occupied by  the allied Pact Worlds to Near Space and the remote Vast,  there's usually something causing trouble somewhere.  Adventurers are always seek |
| 10 | `PZO22001 Starfinder Player Core 030-039::/page/0/ListItem/13` | 0.456790 | **The galaxy is diverse.** Countless worlds and cultures  flourish all over the galaxy (and beyond). Travelers  from Near Space often visit the Pact Worlds (and vice  versa). Visitors from the Vast ar |

### Query 7
- Text: Summarize **The galaxy** **is magical.** Proof of people who magically  change reality and channel the primeval forces of the  universe is everywhere, and people know that it's  real. Magic and technology often blend into powerful  equipment known as magitech, and the presence of  gods and fiends manifests in undeniable ways.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 030-039::/page/0/ListItem/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 030-039::/page/0/ListItem/9', 'PZO22001 Starfinder Player Core 030-039::/page/0/ListItem/10', 'PZO22001 Starfinder Player Core 030-039::/page/0/ListItem/13']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 030-039::/page/0/ListItem/9` | 1.044734 | **The galaxy** **is magical.** Proof of people who magically  change reality and channel the primeval forces of the  universe is everywhere, and people know that it's  real. Magic and technology often |
| 2 | `PZO22001 Starfinder Player Core 030-039::/page/0/ListItem/10` | 0.700690 | **The galaxy has technology.** Tech from computers  to starship systems are part of everyday life. |
| 3 | `PZO22001 Starfinder Player Core 030-039::/page/0/ListItem/13` | 0.636738 | **The galaxy is diverse.** Countless worlds and cultures  flourish all over the galaxy (and beyond). Travelers  from Near Space often visit the Pact Worlds (and vice  versa). Visitors from the Vast ar |
| 4 | `PZO22001 Starfinder Player Core 030-039::/page/0/ListItem/14` | 0.590306 | **The galaxy is dangerous.** Among the planets occupied by  the allied Pact Worlds to Near Space and the remote Vast,  there's usually something causing trouble somewhere.  Adventurers are always seek |
| 5 | `PZO22001 Starfinder Player Core 030-039::/page/0/ListItem/12` | 0.561350 | **The galaxy is connected.** Adventurers have used magical  engines and powerful spells to explore the galaxy  since ancient times, but such travel was rare until the  god Triune introduced hyperspace |
| 6 | `PZO22001 Starfinder Player Core 030-039::/page/5/Text/1` | 0.550050 | Technology and scientific knowledge flourish across the galaxy, but these advancements can't  solve every problem or answer all existential questions. Many turn to religion to understand their  place |
| 7 | `PZO22001 Starfinder Player Core 030-039::/page/5/Text/55` | 0.535946 | **Exploring the ** **Galaxy** |
| 8 | `PZO22001 Starfinder Player Core 030-039::/page/7/Text/83` | 0.535946 | **Exploring the ** **Galaxy** |
| 9 | `PZO22001 Starfinder Player Core 030-039::/page/3/Text/34` | 0.535946 | **Exploring the ** **Galaxy** |
| 10 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/31` | 0.535946 | **Exploring the ** **Galaxy** |

### Query 8
- Text: Summarize **The galaxy has technology.** Tech from computers  to starship systems are part of everyday life.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 030-039::/page/0/ListItem/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 030-039::/page/0/ListItem/10', 'PZO22001 Starfinder Player Core 030-039::/page/0/ListItem/9', 'PZO22001 Starfinder Player Core 030-039::/page/0/ListItem/13']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 030-039::/page/0/ListItem/10` | 1.037273 | **The galaxy has technology.** Tech from computers  to starship systems are part of everyday life. |
| 2 | `PZO22001 Starfinder Player Core 030-039::/page/0/ListItem/9` | 0.711694 | **The galaxy** **is magical.** Proof of people who magically  change reality and channel the primeval forces of the  universe is everywhere, and people know that it's  real. Magic and technology often |
| 3 | `PZO22001 Starfinder Player Core 030-039::/page/0/ListItem/13` | 0.614821 | **The galaxy is diverse.** Countless worlds and cultures  flourish all over the galaxy (and beyond). Travelers  from Near Space often visit the Pact Worlds (and vice  versa). Visitors from the Vast ar |
| 4 | `PZO22001 Starfinder Player Core 030-039::/page/0/Text/11` | 0.573524 | Most people learn the basics of how to use tech in  school or on the job. People communicate with each  other instantaneously using comm units and the  infosphere, a virtual network connecting a world |
| 5 | `PZO22001 Starfinder Player Core 030-039::/page/0/ListItem/12` | 0.563738 | **The galaxy is connected.** Adventurers have used magical  engines and powerful spells to explore the galaxy  since ancient times, but such travel was rare until the  god Triune introduced hyperspace |
| 6 | `PZO22001 Starfinder Player Core 030-039::/page/9/Text/44` | 0.555905 | **Exploring the ** **Galaxy** |
| 7 | `PZO22001 Starfinder Player Core 030-039::/page/5/Text/55` | 0.555905 | **Exploring the ** **Galaxy** |
| 8 | `PZO22001 Starfinder Player Core 030-039::/page/3/Text/34` | 0.555905 | **Exploring the ** **Galaxy** |
| 9 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/31` | 0.555905 | **Exploring the ** **Galaxy** |
| 10 | `PZO22001 Starfinder Player Core 030-039::/page/7/Text/83` | 0.555905 | **Exploring the ** **Galaxy** |

### Query 9
- Text: What is the rule about Most people learn the basics of how to use tech in  school or on the job. People communicate with each  other instantaneously using comm units and the  infosphere, a virtual network connecting a world or  settlement. Inventions like laser guns, cybernetic  body augmentations, and medical serums have been  commonplace for hundreds of years.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 030-039::/page/0/Text/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 030-039::/page/0/Text/11', 'PZO22001 Starfinder Player Core 030-039::/page/0/ListItem/10', 'PZO22001 Starfinder Player Core 030-039::/page/6/Text/59']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 030-039::/page/0/Text/11` | 0.976618 | Most people learn the basics of how to use tech in  school or on the job. People communicate with each  other instantaneously using comm units and the  infosphere, a virtual network connecting a world |
| 2 | `PZO22001 Starfinder Player Core 030-039::/page/0/ListItem/10` | 0.589248 | **The galaxy has technology.** Tech from computers  to starship systems are part of everyday life. |
| 3 | `PZO22001 Starfinder Player Core 030-039::/page/6/Text/59` | 0.469382 | **Areas of Concern **infospheres, memes, pop culture |
| 4 | `PZO22001 Starfinder Player Core 030-039::/page/0/ListItem/9` | 0.433865 | **The galaxy** **is magical.** Proof of people who magically  change reality and channel the primeval forces of the  universe is everywhere, and people know that it's  real. Magic and technology often |
| 5 | `PZO22001 Starfinder Player Core 030-039::/page/0/ListItem/12` | 0.425554 | **The galaxy is connected.** Adventurers have used magical  engines and powerful spells to explore the galaxy  since ancient times, but such travel was rare until the  god Triune introduced hyperspace |
| 6 | `PZO22001 Starfinder Player Core 030-039::/page/4/Text/25` | 0.424213 | Near Space is a term used by people in the galaxy for all  worlds whose nearness to Drift beacons make travel swift  and relatively safe. Communication, trade, and travel between  Near Space planets i |
| 7 | `PZO22001 Starfinder Player Core 030-039::/page/5/Text/1` | 0.419719 | Technology and scientific knowledge flourish across the galaxy, but these advancements can't  solve every problem or answer all existential questions. Many turn to religion to understand their  place |
| 8 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/5` | 0.414087 | Aballon is a rocky, cratered world of superheated metallic  deserts and deep ice wells. Thousands of years before the  Gap, a mysterious civilization called the First Ones utilized  Aballon's abundant |
| 9 | `PZO22001 Starfinder Player Core 030-039::/page/6/Text/60` | 0.411845 | **Edicts** explore infospheres, try new things, share opinions |
| 10 | `PZO22001 Starfinder Player Core 030-039::/page/8/Text/25` | 0.409600 | **Divine Skill** Computers |

### Query 10
- Text: What is the rule about **The galaxy is connected.** Adventurers have used magical  engines and powerful spells to explore the galaxy  since ancient times, but such travel was rare until the  god Triune introduced hyperspace travel through the  mysterious plane of existence known as the Drift.  Triune's devoted followers build magical buoys called  Drift beacons that allow ships to navigate hyperspace  travel and transmit long distance messages. It takes  only days or weeks to travel vast interstellar distances  for a ship with a Drift engine. Drift lanes connect major  ports, making trips even faster, and journeys to Absalom  Station are always swift because of the *Starstone*.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 030-039::/page/0/ListItem/12']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 030-039::/page/0/ListItem/12', 'PZO22001 Starfinder Player Core 030-039::/page/4/Text/25', 'PZO22001 Starfinder Player Core 030-039::/page/1/ListItem/10']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 030-039::/page/0/ListItem/12` | 0.994005 | **The galaxy is connected.** Adventurers have used magical  engines and powerful spells to explore the galaxy  since ancient times, but such travel was rare until the  god Triune introduced hyperspace |
| 2 | `PZO22001 Starfinder Player Core 030-039::/page/4/Text/25` | 0.669334 | Near Space is a term used by people in the galaxy for all  worlds whose nearness to Drift beacons make travel swift  and relatively safe. Communication, trade, and travel between  Near Space planets i |
| 3 | `PZO22001 Starfinder Player Core 030-039::/page/1/ListItem/10` | 0.655953 | A priest of Triune who travels across the galaxy  installing and repairing Drift beacons, receiving sacred  downloads from Striving's sacred neural network. |
| 4 | `PZO22001 Starfinder Player Core 030-039::/page/0/ListItem/9` | 0.579207 | **The galaxy** **is magical.** Proof of people who magically  change reality and channel the primeval forces of the  universe is everywhere, and people know that it's  real. Magic and technology often |
| 5 | `PZO22001 Starfinder Player Core 030-039::/page/0/Text/6` | 0.578462 | Starfinder occurs in the far future after the Age of Lost Omens,  but there's a Gap in the galaxy's history. About 300 years  ago, something erased an entire era from memory. Records  for this forgott |
| 6 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/25` | 0.577280 | Floating in lost Golarion's empty orbit, this bustling space  station is the center of interstellar trade and governance  in the Pact Worlds. Nobody knows who built Absalom  Station because it appeare |
| 7 | `PZO22001 Starfinder Player Core 030-039::/page/8/Text/17` | 0.575727 | Triune is a fusion of the three technological  deities Epoch, Brigh, and Casandalee. Triune's Signal made  Drift travel possible. |
| 8 | `PZO22001 Starfinder Player Core 030-039::/page/0/ListItem/10` | 0.557152 | **The galaxy has technology.** Tech from computers  to starship systems are part of everyday life. |
| 9 | `PZO22001 Starfinder Player Core 030-039::/page/4/Text/28` | 0.554727 | The dangerous, infrequently traveled outskirts of the galaxy  and the endless sprawl of uncharted space beyond are called  the Vast. Only a handful of scattered Drift beacons exist to  guide ships thr |
| 10 | `PZO22001 Starfinder Player Core 030-039::/page/0/ListItem/13` | 0.530278 | **The galaxy is diverse.** Countless worlds and cultures  flourish all over the galaxy (and beyond). Travelers  from Near Space often visit the Pact Worlds (and vice  versa). Visitors from the Vast ar |

### Query 11
- Text: What is the rule about **The galaxy is diverse.** Countless worlds and cultures  flourish all over the galaxy (and beyond). Travelers  from Near Space often visit the Pact Worlds (and vice  versa). Visitors from the Vast are rarer, but such travel  is possible.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 030-039::/page/0/ListItem/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 030-039::/page/0/ListItem/13', 'PZO22001 Starfinder Player Core 030-039::/page/0/ListItem/14', 'PZO22001 Starfinder Player Core 030-039::/page/4/Text/28']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 030-039::/page/0/ListItem/13` | 0.966652 | **The galaxy is diverse.** Countless worlds and cultures  flourish all over the galaxy (and beyond). Travelers  from Near Space often visit the Pact Worlds (and vice  versa). Visitors from the Vast ar |
| 2 | `PZO22001 Starfinder Player Core 030-039::/page/0/ListItem/14` | 0.698206 | **The galaxy is dangerous.** Among the planets occupied by  the allied Pact Worlds to Near Space and the remote Vast,  there's usually something causing trouble somewhere.  Adventurers are always seek |
| 3 | `PZO22001 Starfinder Player Core 030-039::/page/4/Text/28` | 0.616779 | The dangerous, infrequently traveled outskirts of the galaxy  and the endless sprawl of uncharted space beyond are called  the Vast. Only a handful of scattered Drift beacons exist to  guide ships thr |
| 4 | `PZO22001 Starfinder Player Core 030-039::/page/0/ListItem/9` | 0.556464 | **The galaxy** **is magical.** Proof of people who magically  change reality and channel the primeval forces of the  universe is everywhere, and people know that it's  real. Magic and technology often |
| 5 | `PZO22001 Starfinder Player Core 030-039::/page/4/Text/25` | 0.536685 | Near Space is a term used by people in the galaxy for all  worlds whose nearness to Drift beacons make travel swift  and relatively safe. Communication, trade, and travel between  Near Space planets i |
| 6 | `PZO22001 Starfinder Player Core 030-039::/page/4/Text/29` | 0.506690 | Regions of the Vast include the Azlanti Star Empire, a vast  territory of unknown size controlled by a colonizing regime  ruled by the descendants of a human nation from lost Golarion;  Kazmurg's Absu |
| 7 | `PZO22001 Starfinder Player Core 030-039::/page/0/ListItem/10` | 0.505970 | **The galaxy has technology.** Tech from computers  to starship systems are part of everyday life. |
| 8 | `PZO22001 Starfinder Player Core 030-039::/page/0/ListItem/12` | 0.505651 | **The galaxy is connected.** Adventurers have used magical  engines and powerful spells to explore the galaxy  since ancient times, but such travel was rare until the  god Triune introduced hyperspace |
| 9 | `PZO22001 Starfinder Player Core 030-039::/page/3/Text/34` | 0.492517 | **Exploring the ** **Galaxy** |
| 10 | `PZO22001 Starfinder Player Core 030-039::/page/5/Text/55` | 0.492517 | **Exploring the ** **Galaxy** |

### Query 12
- Text: What is the rule about **The galaxy is dangerous.** Among the planets occupied by  the allied Pact Worlds to Near Space and the remote Vast,  there's usually something causing trouble somewhere.  Adventurers are always seeking knowledge, riches, and  new homes in this limitless and perilous galaxy!?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 030-039::/page/0/ListItem/14']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 030-039::/page/0/ListItem/14', 'PZO22001 Starfinder Player Core 030-039::/page/0/ListItem/13', 'PZO22001 Starfinder Player Core 030-039::/page/4/Text/28']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 030-039::/page/0/ListItem/14` | 0.970970 | **The galaxy is dangerous.** Among the planets occupied by  the allied Pact Worlds to Near Space and the remote Vast,  there's usually something causing trouble somewhere.  Adventurers are always seek |
| 2 | `PZO22001 Starfinder Player Core 030-039::/page/0/ListItem/13` | 0.709028 | **The galaxy is diverse.** Countless worlds and cultures  flourish all over the galaxy (and beyond). Travelers  from Near Space often visit the Pact Worlds (and vice  versa). Visitors from the Vast ar |
| 3 | `PZO22001 Starfinder Player Core 030-039::/page/4/Text/28` | 0.649667 | The dangerous, infrequently traveled outskirts of the galaxy  and the endless sprawl of uncharted space beyond are called  the Vast. Only a handful of scattered Drift beacons exist to  guide ships thr |
| 4 | `PZO22001 Starfinder Player Core 030-039::/page/0/ListItem/9` | 0.586533 | **The galaxy** **is magical.** Proof of people who magically  change reality and channel the primeval forces of the  universe is everywhere, and people know that it's  real. Magic and technology often |
| 5 | `PZO22001 Starfinder Player Core 030-039::/page/4/Text/25` | 0.577047 | Near Space is a term used by people in the galaxy for all  worlds whose nearness to Drift beacons make travel swift  and relatively safe. Communication, trade, and travel between  Near Space planets i |
| 6 | `PZO22001 Starfinder Player Core 030-039::/page/4/Text/29` | 0.516762 | Regions of the Vast include the Azlanti Star Empire, a vast  territory of unknown size controlled by a colonizing regime  ruled by the descendants of a human nation from lost Golarion;  Kazmurg's Absu |
| 7 | `PZO22001 Starfinder Player Core 030-039::/page/0/ListItem/10` | 0.516119 | **The galaxy has technology.** Tech from computers  to starship systems are part of everyday life. |
| 8 | `PZO22001 Starfinder Player Core 030-039::/page/0/ListItem/12` | 0.512120 | **The galaxy is connected.** Adventurers have used magical  engines and powerful spells to explore the galaxy  since ancient times, but such travel was rare until the  god Triune introduced hyperspace |
| 9 | `PZO22001 Starfinder Player Core 030-039::/page/9/Text/44` | 0.494166 | **Exploring the ** **Galaxy** |
| 10 | `PZO22001 Starfinder Player Core 030-039::/page/7/Text/83` | 0.494166 | **Exploring the ** **Galaxy** |

### Query 13
- Text: What is the rule about THE PACT WORLDS?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 030-039::/page/0/SectionHeader/15']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 030-039::/page/0/SectionHeader/15', 'PZO22001 Starfinder Player Core 030-039::/page/0/Text/16', 'PZO22001 Starfinder Player Core 030-039::/page/4/Text/18']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 030-039::/page/0/SectionHeader/15` | 0.886002 | THE PACT WORLDS |
| 2 | `PZO22001 Starfinder Player Core 030-039::/page/0/Text/16` | 0.501369 | The Pact Worlds form the core of the Starfinder setting.  "The Pact Worlds" is the formal name for the united planets  orbiting lost Golarion's sun and their more distant allied  worlds, including Pul |
| 3 | `PZO22001 Starfinder Player Core 030-039::/page/4/Text/18` | 0.457604 | for freedom, the pahtra rebels of Pulonis eventually drove  out the last Veskarium occupiers, declared independence,  and joined the Pact Worlds interstellar alliance. Pulonis is the  first world outs |
| 4 | `PZO22001 Starfinder Player Core 030-039::/page/0/ListItem/13` | 0.410834 | **The galaxy is diverse.** Countless worlds and cultures  flourish all over the galaxy (and beyond). Travelers  from Near Space often visit the Pact Worlds (and vice  versa). Visitors from the Vast ar |
| 5 | `PZO22001 Starfinder Player Core 030-039::/page/0/ListItem/14` | 0.403038 | **The galaxy is dangerous.** Among the planets occupied by  the allied Pact Worlds to Near Space and the remote Vast,  there's usually something causing trouble somewhere.  Adventurers are always seek |
| 6 | `PZO22001 Starfinder Player Core 030-039::/page/4/Text/9` | 0.372829 | Apostae is a hollow planetoid with no atmosphere and few  resources. Mysterious gateways on the planet's rocky surface  access a network of tunnels, magitech chambers, and caverns  inside its core. Th |
| 7 | `PZO22001 Starfinder Player Core 030-039::/page/2/Text/23` | 0.371533 | The *Idari* is a world ship built long ago on the world of Kasath  to transport its population away from the dying planet,  toward a desert world kasatha mystics believed was their  promised land: Aki |
| 8 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/17` | 0.363605 | In fact, you don't have to use this setting! While  the Starfinder RPG rules do make some assumptions  about the world, many of these assumptions are  common within the science fantasy genre. Elements |
| 9 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/1` | 0.362415 | The united worlds are Absalom Station, Aballon, Castrovel,  Akiton, Verces, the Diaspora, Eox, Triaxus, Dykon, Kalo-Mahoi,  Marata, Liavara, and Bretheda. The *Idari*—a starship—is counted  among thei |
| 10 | `PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/29` | 0.346039 | **Belt of Broken Worlds** |

### Query 14
- Text: What is the rule about The Pact Worlds form the core of the Starfinder setting.  "The Pact Worlds" is the formal name for the united planets  orbiting lost Golarion's sun and their more distant allied  worlds, including Pulonis in Near Space. After a short-lived  interplanetary war with the Veskarium threatened their home  system, the Pact Worlds united by signing the Absalom Pact  and creating the Stewards, a mutual defense force dedicated  to defending the system from outside threats and enforcing  their treaty.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 030-039::/page/0/Text/16']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 030-039::/page/0/Text/16', 'PZO22001 Starfinder Player Core 030-039::/page/4/Text/18', 'PZO22001 Starfinder Player Core 030-039::/page/4/Text/26']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 030-039::/page/0/Text/16` | 1.013525 | The Pact Worlds form the core of the Starfinder setting.  "The Pact Worlds" is the formal name for the united planets  orbiting lost Golarion's sun and their more distant allied  worlds, including Pul |
| 2 | `PZO22001 Starfinder Player Core 030-039::/page/4/Text/18` | 0.654326 | for freedom, the pahtra rebels of Pulonis eventually drove  out the last Veskarium occupiers, declared independence,  and joined the Pact Worlds interstellar alliance. Pulonis is the  first world outs |
| 3 | `PZO22001 Starfinder Player Core 030-039::/page/4/Text/26` | 0.610572 | Near Space regions include the Veskarium, an empire of  seven conquered planets and a few dozen colonies ruled  by vesk military leaders; the Marixah Republic, a group of  allied planets emerging onto |
| 4 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/1` | 0.579659 | The united worlds are Absalom Station, Aballon, Castrovel,  Akiton, Verces, the Diaspora, Eox, Triaxus, Dykon, Kalo-Mahoi,  Marata, Liavara, and Bretheda. The *Idari*—a starship—is counted  among thei |
| 5 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/25` | 0.547796 | Floating in lost Golarion's empty orbit, this bustling space  station is the center of interstellar trade and governance  in the Pact Worlds. Nobody knows who built Absalom  Station because it appeare |
| 6 | `PZO22001 Starfinder Player Core 030-039::/page/0/ListItem/14` | 0.547420 | **The galaxy is dangerous.** Among the planets occupied by  the allied Pact Worlds to Near Space and the remote Vast,  there's usually something causing trouble somewhere.  Adventurers are always seek |
| 7 | `PZO22001 Starfinder Player Core 030-039::/page/0/Text/6` | 0.532518 | Starfinder occurs in the far future after the Age of Lost Omens,  but there's a Gap in the galaxy's history. About 300 years  ago, something erased an entire era from memory. Records  for this forgott |
| 8 | `PZO22001 Starfinder Player Core 030-039::/page/4/Text/9` | 0.514588 | Apostae is a hollow planetoid with no atmosphere and few  resources. Mysterious gateways on the planet's rocky surface  access a network of tunnels, magitech chambers, and caverns  inside its core. Th |
| 9 | `PZO22001 Starfinder Player Core 030-039::/page/0/Text/4` | 0.513432 | The Starfinder Roleplaying Game rules come with their own  default setting: the galaxy known as Desna's Path. The galaxy  is full of wonder and peril, advanced technology, magic,  meddling deities, an |
| 10 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/17` | 0.510874 | In fact, you don't have to use this setting! While  the Starfinder RPG rules do make some assumptions  about the world, many of these assumptions are  common within the science fantasy genre. Elements |

### Query 15
- Text: Summarize The united worlds are Absalom Station, Aballon, Castrovel,  Akiton, Verces, the Diaspora, Eox, Triaxus, Dykon, Kalo-Mahoi,  Marata, Liavara, and Bretheda. The *Idari*—a starship—is counted  among their number, as is Pulonis, a planet in the Ghavaniska  system that was formerly occupied by the Veskarium.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 030-039::/page/1/Text/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 030-039::/page/1/Text/1', 'PZO22001 Starfinder Player Core 030-039::/page/0/Text/16', 'PZO22001 Starfinder Player Core 030-039::/page/1/Text/25']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/1` | 1.044705 | The united worlds are Absalom Station, Aballon, Castrovel,  Akiton, Verces, the Diaspora, Eox, Triaxus, Dykon, Kalo-Mahoi,  Marata, Liavara, and Bretheda. The *Idari*—a starship—is counted  among thei |
| 2 | `PZO22001 Starfinder Player Core 030-039::/page/0/Text/16` | 0.617806 | The Pact Worlds form the core of the Starfinder setting.  "The Pact Worlds" is the formal name for the united planets  orbiting lost Golarion's sun and their more distant allied  worlds, including Pul |
| 3 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/25` | 0.607965 | Floating in lost Golarion's empty orbit, this bustling space  station is the center of interstellar trade and governance  in the Pact Worlds. Nobody knows who built Absalom  Station because it appeare |
| 4 | `PZO22001 Starfinder Player Core 030-039::/page/3/Text/29` | 0.528588 | Bretheda's violent storms make most of its gaseous layers  unlivable. The planet's largest city is Trillidiem, a domed,  industrial arcology governed by Confluence, a union of many  merged barathus. B |
| 5 | `PZO22001 Starfinder Player Core 030-039::/page/4/Text/26` | 0.513344 | Near Space regions include the Veskarium, an empire of  seven conquered planets and a few dozen colonies ruled  by vesk military leaders; the Marixah Republic, a group of  allied planets emerging onto |
| 6 | `PZO22001 Starfinder Player Core 030-039::/page/2/Text/30` | 0.509752 | The Diaspora is an asteroid belt formed long before the  Gap, when a terrible cataclysm destroyed the twin planets  Damiar and Iovo. The remains of the two destroyed worlds  float among millions of ch |
| 7 | `PZO22001 Starfinder Player Core 030-039::/page/4/Text/29` | 0.503938 | Regions of the Vast include the Azlanti Star Empire, a vast  territory of unknown size controlled by a colonizing regime  ruled by the descendants of a human nation from lost Golarion;  Kazmurg's Absu |
| 8 | `PZO22001 Starfinder Player Core 030-039::/page/4/Text/18` | 0.498820 | for freedom, the pahtra rebels of Pulonis eventually drove  out the last Veskarium occupiers, declared independence,  and joined the Pact Worlds interstellar alliance. Pulonis is the  first world outs |
| 9 | `PZO22001 Starfinder Player Core 030-039::/page/2/Text/23` | 0.497206 | The *Idari* is a world ship built long ago on the world of Kasath  to transport its population away from the dying planet,  toward a desert world kasatha mystics believed was their  promised land: Aki |
| 10 | `PZO22001 Starfinder Player Core 030-039::/page/2/Text/16` | 0.494998 | Major locations on Verces include the Ring of Nations,  a band of sprawling megacities inhabited by augmented  verthani, androids, and many others; Skydock, modern  shipyards built atop an ancient spa |

### Query 16
- Text: What is the rule about What's left of Aucturn, a planet destroyed by the birth of  a god, floats among the field of ice and haunted space junk  ringing the system's outskirts, called the Gelid Edge.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 030-039::/page/1/Text/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 030-039::/page/1/Text/2', 'PZO22001 Starfinder Player Core 030-039::/page/7/Text/39', 'PZO22001 Starfinder Player Core 030-039::/page/4/Text/29']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/2` | 0.962134 | What's left of Aucturn, a planet destroyed by the birth of  a god, floats among the field of ice and haunted space junk  ringing the system's outskirts, called the Gelid Edge. |
| 2 | `PZO22001 Starfinder Player Core 030-039::/page/7/Text/39` | 0.645327 | Aucturn, destroying the planet in the process. |
| 3 | `PZO22001 Starfinder Player Core 030-039::/page/4/Text/29` | 0.539210 | Regions of the Vast include the Azlanti Star Empire, a vast  territory of unknown size controlled by a colonizing regime  ruled by the descendants of a human nation from lost Golarion;  Kazmurg's Absu |
| 4 | `PZO22001 Starfinder Player Core 030-039::/page/4/Text/10` | 0.477563 | Regions include Nightarch, a pressurized megacity where  opulent spires tower over air-choked slums, named for the  massive gate leading inside the planet at the center of the  settlement; the Silted |
| 5 | `PZO22001 Starfinder Player Core 030-039::/page/3/Text/2` | 0.474271 | In the modern era, bone sages rule scattered fiefdoms  on Eox's irradiated surface, and hordes of mindless undead  wander the wastes outside magical bunkers and walled  necropolises. Many are tragic b |
| 6 | `PZO22001 Starfinder Player Core 030-039::/page/4/Text/28` | 0.470806 | The dangerous, infrequently traveled outskirts of the galaxy  and the endless sprawl of uncharted space beyond are called  the Vast. Only a handful of scattered Drift beacons exist to  guide ships thr |
| 7 | `PZO22001 Starfinder Player Core 030-039::/page/0/ListItem/14` | 0.461198 | **The galaxy is dangerous.** Among the planets occupied by  the allied Pact Worlds to Near Space and the remote Vast,  there's usually something causing trouble somewhere.  Adventurers are always seek |
| 8 | `PZO22001 Starfinder Player Core 030-039::/page/4/Text/9` | 0.458124 | Apostae is a hollow planetoid with no atmosphere and few  resources. Mysterious gateways on the planet's rocky surface  access a network of tunnels, magitech chambers, and caverns  inside its core. Th |
| 9 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/5` | 0.446605 | Aballon is a rocky, cratered world of superheated metallic  deserts and deep ice wells. Thousands of years before the  Gap, a mysterious civilization called the First Ones utilized  Aballon's abundant |
| 10 | `PZO22001 Starfinder Player Core 030-039::/page/1/ListItem/8` | 0.443121 | A Starfinder exploring magitech ruins left by the  First Ones, risking encounters with deadly traps and  terrifying sentries. |

### Query 17
- Text: Summarize ABALLON
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 030-039::/page/1/SectionHeader/3']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 030-039::/page/1/SectionHeader/3', 'PZO22001 Starfinder Player Core 030-039::/page/1/SectionHeader/23', 'PZO22001 Starfinder Player Core 030-039::/page/1/Text/5']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 030-039::/page/1/SectionHeader/3` | 0.915713 | ABALLON |
| 2 | `PZO22001 Starfinder Player Core 030-039::/page/1/SectionHeader/23` | 0.391955 | ABSALOM STATION |
| 3 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/5` | 0.377108 | Aballon is a rocky, cratered world of superheated metallic  deserts and deep ice wells. Thousands of years before the  Gap, a mysterious civilization called the First Ones utilized  Aballon's abundant |
| 4 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/6` | 0.339279 | The largest community on Aballon is Striving, an  industrious megacity containing a citywide neural network  sacred to Triune. Other regions include the industrial forgecity Automatrix; the immense, f |
| 5 | `PZO22001 Starfinder Player Core 030-039::/page/5/SectionHeader/5` | 0.333804 | ABADAR |
| 6 | `PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/5` | 0.313165 | AKITON |
| 7 | `PZO22001 Starfinder Player Core 030-039::/page/4/SectionHeader/7` | 0.288301 | APOSTAE |
| 8 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/26` | 0.285786 | At the center of Absalom Station is the Eye, a shielded  sector famous for lush Jatembe Park, glittering corporate  towers and luxurious neighborhoods, and a sprawling  academic sector that houses a s |
| 9 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/1` | 0.275687 | The united worlds are Absalom Station, Aballon, Castrovel,  Akiton, Verces, the Diaspora, Eox, Triaxus, Dykon, Kalo-Mahoi,  Marata, Liavara, and Bretheda. The *Idari*—a starship—is counted  among thei |
| 10 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/25` | 0.260323 | Floating in lost Golarion's empty orbit, this bustling space  station is the center of interstellar trade and governance  in the Pact Worlds. Nobody knows who built Absalom  Station because it appeare |

### Query 18
- Text: What is the rule about **Industrial World of Intelligent Machines**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 030-039::/page/1/SectionHeader/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 030-039::/page/1/SectionHeader/4', 'PZO22001 Starfinder Player Core 030-039::/page/8/Text/18', 'PZO22001 Starfinder Player Core 030-039::/page/0/Text/11']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 030-039::/page/1/SectionHeader/4` | 0.837555 | **Industrial World of Intelligent Machines** |
| 2 | `PZO22001 Starfinder Player Core 030-039::/page/8/Text/18` | 0.471348 | **Areas of Concern **artificial intelligence, computers, the Drift **Edicts** advance the development of artificial life and  artificial intelligence, innovate new technology, promote  Drift travel |
| 3 | `PZO22001 Starfinder Player Core 030-039::/page/0/Text/11` | 0.408259 | Most people learn the basics of how to use tech in  school or on the job. People communicate with each  other instantaneously using comm units and the  infosphere, a virtual network connecting a world |
| 4 | `PZO22001 Starfinder Player Core 030-039::/page/0/ListItem/10` | 0.345928 | **The galaxy has technology.** Tech from computers  to starship systems are part of everyday life. |
| 5 | `PZO22001 Starfinder Player Core 030-039::/page/5/Text/63` | 0.345759 | **GAME** **CONDITIONS ** |
| 6 | `PZO22001 Starfinder Player Core 030-039::/page/8/Text/19` | 0.344716 | **Anathema** treat artificial life as inferior to organic life,  subjugate artificial life-forms, destroy a Drift beacon |
| 7 | `PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/27` | 0.335891 | A restless engineer who's bored with the *Idari*'s  predictable orbit and ancient schematics. |
| 8 | `PZO22001 Starfinder Player Core 030-039::/page/7/Text/14` | 0.333914 | **Divine Attribute** Intelligence or Wisdom |
| 9 | `PZO22001 Starfinder Player Core 030-039::/page/6/Text/20` | 0.333914 | **Divine Attribute** Intelligence or Wisdom |
| 10 | `PZO22001 Starfinder Player Core 030-039::/page/6/Text/47` | 0.333914 | **Divine Attribute** Intelligence or Wisdom |

### Query 19
- Text: What is the rule about Aballon is a rocky, cratered world of superheated metallic  deserts and deep ice wells. Thousands of years before the  Gap, a mysterious civilization called the First Ones utilized  Aballon's abundant metals and solar energy to build a host  of servitor machines. The First Ones tasked their machine  progeny with harvesting the planet's resources—and then  they left. Abandoned by their creators, the machines  upgraded themselves and formed their own societies. The  machines, now called anacites, have evolved into many forms  and functions and established a society where androids and  other synthetic beings are welcomed as siblings.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 030-039::/page/1/Text/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 030-039::/page/1/Text/5', 'PZO22001 Starfinder Player Core 030-039::/page/1/Text/6', 'PZO22001 Starfinder Player Core 030-039::/page/4/Text/9']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/5` | 1.022365 | Aballon is a rocky, cratered world of superheated metallic  deserts and deep ice wells. Thousands of years before the  Gap, a mysterious civilization called the First Ones utilized  Aballon's abundant |
| 2 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/6` | 0.614519 | The largest community on Aballon is Striving, an  industrious megacity containing a citywide neural network  sacred to Triune. Other regions include the industrial forgecity Automatrix; the immense, f |
| 3 | `PZO22001 Starfinder Player Core 030-039::/page/4/Text/9` | 0.590105 | Apostae is a hollow planetoid with no atmosphere and few  resources. Mysterious gateways on the planet's rocky surface  access a network of tunnels, magitech chambers, and caverns  inside its core. Th |
| 4 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/25` | 0.530677 | Floating in lost Golarion's empty orbit, this bustling space  station is the center of interstellar trade and governance  in the Pact Worlds. Nobody knows who built Absalom  Station because it appeare |
| 5 | `PZO22001 Starfinder Player Core 030-039::/page/2/Text/30` | 0.517586 | The Diaspora is an asteroid belt formed long before the  Gap, when a terrible cataclysm destroyed the twin planets  Damiar and Iovo. The remains of the two destroyed worlds  float among millions of ch |
| 6 | `PZO22001 Starfinder Player Core 030-039::/page/2/Text/7` | 0.508205 | Akiton is a dusty red world of sunbaked deserts, rundown  cities, and rusting scrapyards. It was once a booming industrial  paradise overflowing with wealth earned from mining thasteron,  a starship f |
| 7 | `PZO22001 Starfinder Player Core 030-039::/page/4/Text/10` | 0.508174 | Regions include Nightarch, a pressurized megacity where  opulent spires tower over air-choked slums, named for the  massive gate leading inside the planet at the center of the  settlement; the Silted |
| 8 | `PZO22001 Starfinder Player Core 030-039::/page/2/Text/16` | 0.505699 | Major locations on Verces include the Ring of Nations,  a band of sprawling megacities inhabited by augmented  verthani, androids, and many others; Skydock, modern  shipyards built atop an ancient spa |
| 9 | `PZO22001 Starfinder Player Core 030-039::/page/1/ListItem/8` | 0.496825 | A Starfinder exploring magitech ruins left by the  First Ones, risking encounters with deadly traps and  terrifying sentries. |
| 10 | `PZO22001 Starfinder Player Core 030-039::/page/0/Text/6` | 0.496260 | Starfinder occurs in the far future after the Age of Lost Omens,  but there's a Gap in the galaxy's history. About 300 years  ago, something erased an entire era from memory. Records  for this forgott |

### Query 20
- Text: What is the rule about The largest community on Aballon is Striving, an  industrious megacity containing a citywide neural network  sacred to Triune. Other regions include the industrial forgecity Automatrix; the immense, floating Horse Eye Orbital  Plate factory; the sprawling technological ruin of Eternity  and other meticulously preserved First Ones cities; the gemencrusted Sea of Glass; and the ore-laden Midnight Trenches.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 030-039::/page/1/Text/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 030-039::/page/1/Text/6', 'PZO22001 Starfinder Player Core 030-039::/page/1/Text/5', 'PZO22001 Starfinder Player Core 030-039::/page/4/Text/10']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/6` | 1.006199 | The largest community on Aballon is Striving, an  industrious megacity containing a citywide neural network  sacred to Triune. Other regions include the industrial forgecity Automatrix; the immense, f |
| 2 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/5` | 0.627847 | Aballon is a rocky, cratered world of superheated metallic  deserts and deep ice wells. Thousands of years before the  Gap, a mysterious civilization called the First Ones utilized  Aballon's abundant |
| 3 | `PZO22001 Starfinder Player Core 030-039::/page/4/Text/10` | 0.613138 | Regions include Nightarch, a pressurized megacity where  opulent spires tower over air-choked slums, named for the  massive gate leading inside the planet at the center of the  settlement; the Silted |
| 4 | `PZO22001 Starfinder Player Core 030-039::/page/2/Text/16` | 0.550031 | Major locations on Verces include the Ring of Nations,  a band of sprawling megacities inhabited by augmented  verthani, androids, and many others; Skydock, modern  shipyards built atop an ancient spa |
| 5 | `PZO22001 Starfinder Player Core 030-039::/page/1/ListItem/10` | 0.542996 | A priest of Triune who travels across the galaxy  installing and repairing Drift beacons, receiving sacred  downloads from Striving's sacred neural network. |
| 6 | `PZO22001 Starfinder Player Core 030-039::/page/3/Text/29` | 0.522461 | Bretheda's violent storms make most of its gaseous layers  unlivable. The planet's largest city is Trillidiem, a domed,  industrial arcology governed by Confluence, a union of many  merged barathus. B |
| 7 | `PZO22001 Starfinder Player Core 030-039::/page/4/Text/19` | 0.515303 | Regions include Voyedris, a treacherous wilderness  ravaged by rapid industrialization; Hafrerren, a rebel nationstate known for biotech research; Rafemii, a hub for magical  and spiritual development |
| 8 | `PZO22001 Starfinder Player Core 030-039::/page/3/Text/28` | 0.503387 | Bretheda is a massive, stormy gas giant orbited by moons  where diverse peoples have built thriving, cosmopolitan  societies. Bretheda and its moons are home to cuttingedge biotech foundries, living c |
| 9 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/18` | 0.502869 | spires of Sovyrian, a nation of surrealist cities sculpted  by elven magic. Castrovel's wilds are virtually unspoiled  because the planet's industry occurs on the super-polluted  moon Elindrae. |
| 10 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/25` | 0.502387 | Floating in lost Golarion's empty orbit, this bustling space  station is the center of interstellar trade and governance  in the Pact Worlds. Nobody knows who built Absalom  Station because it appeare |

### Query 21
- Text: What is the rule about Example Characters?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 030-039::/page/1/SectionHeader/7']
- Expected found: `True`
- Expected rank: `13`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 030-039::/page/1/SectionHeader/19', 'PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/17', 'PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/9']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 030-039::/page/1/SectionHeader/19` | 0.837066 | Example Characters |
| 2 | `PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/9` | 0.837066 | Example Characters |
| 3 | `PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/17` | 0.837066 | Example Characters |
| 4 | `PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/1` | 0.807066 | Example Characters |
| 5 | `PZO22001 Starfinder Player Core 030-039::/page/4/SectionHeader/11` | 0.807066 | Example Characters |
| 6 | `PZO22001 Starfinder Player Core 030-039::/page/4/SectionHeader/3` | 0.807066 | Example Characters |
| 7 | `PZO22001 Starfinder Player Core 030-039::/page/3/SectionHeader/22` | 0.807066 | Example Characters |
| 8 | `PZO22001 Starfinder Player Core 030-039::/page/3/SectionHeader/13` | 0.807066 | Example Characters |
| 9 | `PZO22001 Starfinder Player Core 030-039::/page/3/SectionHeader/4` | 0.807066 | Example Characters |
| 10 | `PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/31` | 0.807066 | Example Characters |

### Query 22
- Text: Summarize A Starfinder exploring magitech ruins left by the  First Ones, risking encounters with deadly traps and  terrifying sentries.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 030-039::/page/1/ListItem/8']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 030-039::/page/1/ListItem/8', 'PZO22001 Starfinder Player Core 030-039::/page/0/Text/4', 'PZO22001 Starfinder Player Core 030-039::/page/0/Text/6']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 030-039::/page/1/ListItem/8` | 1.031240 | A Starfinder exploring magitech ruins left by the  First Ones, risking encounters with deadly traps and  terrifying sentries. |
| 2 | `PZO22001 Starfinder Player Core 030-039::/page/0/Text/4` | 0.609142 | The Starfinder Roleplaying Game rules come with their own  default setting: the galaxy known as Desna's Path. The galaxy  is full of wonder and peril, advanced technology, magic,  meddling deities, an |
| 3 | `PZO22001 Starfinder Player Core 030-039::/page/0/Text/6` | 0.603565 | Starfinder occurs in the far future after the Age of Lost Omens,  but there's a Gap in the galaxy's history. About 300 years  ago, something erased an entire era from memory. Records  for this forgott |
| 4 | `PZO22001 Starfinder Player Core 030-039::/page/4/ListItem/13` | 0.535588 | A xenoarchaeologist exploring the planet's hollow interior  and cataloging the strange ruins and dangerous creatures  that lurk within. |
| 5 | `PZO22001 Starfinder Player Core 030-039::/page/3/Text/2` | 0.509758 | In the modern era, bone sages rule scattered fiefdoms  on Eox's irradiated surface, and hordes of mindless undead  wander the wastes outside magical bunkers and walled  necropolises. Many are tragic b |
| 6 | `PZO22001 Starfinder Player Core 030-039::/page/4/Text/10` | 0.508371 | Regions include Nightarch, a pressurized megacity where  opulent spires tower over air-choked slums, named for the  massive gate leading inside the planet at the center of the  settlement; the Silted |
| 7 | `PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/3` | 0.507554 | A ghost courier, exploring the Ghost Levels on a hunt  for valuable relics, surviving dangerous anomalies and  fighting dimensionally displaced monsters. |
| 8 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/5` | 0.502013 | Aballon is a rocky, cratered world of superheated metallic  deserts and deep ice wells. Thousands of years before the  Gap, a mysterious civilization called the First Ones utilized  Aballon's abundant |
| 9 | `PZO22001 Starfinder Player Core 030-039::/page/0/Text/16` | 0.500702 | The Pact Worlds form the core of the Starfinder setting.  "The Pact Worlds" is the formal name for the united planets  orbiting lost Golarion's sun and their more distant allied  worlds, including Pul |
| 10 | `PZO22001 Starfinder Player Core 030-039::/page/3/ListItem/7` | 0.498235 | A xenoarchaeologist studying the ruins beneath  Murthal, dodging ancient traps and uncovering relics  deep within its forgotten tombs. |

### Query 23
- Text: Summarize A Xenowarden nurturing bizarre flora and fauna  deep inside secluded Ice Wells and undermining local  industry.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 030-039::/page/1/ListItem/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 030-039::/page/1/ListItem/9', 'PZO22001 Starfinder Player Core 030-039::/page/4/ListItem/13', 'PZO22001 Starfinder Player Core 030-039::/page/3/ListItem/7']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 030-039::/page/1/ListItem/9` | 1.036301 | A Xenowarden nurturing bizarre flora and fauna  deep inside secluded Ice Wells and undermining local  industry. |
| 2 | `PZO22001 Starfinder Player Core 030-039::/page/4/ListItem/13` | 0.581656 | A xenoarchaeologist exploring the planet's hollow interior  and cataloging the strange ruins and dangerous creatures  that lurk within. |
| 3 | `PZO22001 Starfinder Player Core 030-039::/page/3/ListItem/7` | 0.500505 | A xenoarchaeologist studying the ruins beneath  Murthal, dodging ancient traps and uncovering relics  deep within its forgotten tombs. |
| 4 | `PZO22001 Starfinder Player Core 030-039::/page/9/Text/33` | 0.448064 | Many Xenowardens practice a modern version of  the old Green Faith. They view nature as sacred |
| 5 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/18` | 0.428965 | spires of Sovyrian, a nation of surrealist cities sculpted  by elven magic. Castrovel's wilds are virtually unspoiled  because the planet's industry occurs on the super-polluted  moon Elindrae. |
| 6 | `PZO22001 Starfinder Player Core 030-039::/page/3/Text/21` | 0.424194 | Regions include Roselight, a cloud of floating domes built  by barathu architects, and Deep Station, a research outpost  submerged in Liavara's alien seas. Liavara has many moons:  Hallas, a warded pr |
| 7 | `PZO22001 Starfinder Player Core 030-039::/page/4/Text/19` | 0.422150 | Regions include Voyedris, a treacherous wilderness  ravaged by rapid industrialization; Hafrerren, a rebel nationstate known for biotech research; Rafemii, a hub for magical  and spiritual development |
| 8 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/5` | 0.420936 | Aballon is a rocky, cratered world of superheated metallic  deserts and deep ice wells. Thousands of years before the  Gap, a mysterious civilization called the First Ones utilized  Aballon's abundant |
| 9 | `PZO22001 Starfinder Player Core 030-039::/page/4/Text/10` | 0.409798 | Regions include Nightarch, a pressurized megacity where  opulent spires tower over air-choked slums, named for the  massive gate leading inside the planet at the center of the  settlement; the Silted |
| 10 | `PZO22001 Starfinder Player Core 030-039::/page/2/Text/16` | 0.409257 | Major locations on Verces include the Ring of Nations,  a band of sprawling megacities inhabited by augmented  verthani, androids, and many others; Skydock, modern  shipyards built atop an ancient spa |

### Query 24
- Text: What is the rule about A priest of Triune who travels across the galaxy  installing and repairing Drift beacons, receiving sacred  downloads from Striving's sacred neural network.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 030-039::/page/1/ListItem/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 030-039::/page/1/ListItem/10', 'PZO22001 Starfinder Player Core 030-039::/page/0/ListItem/12', 'PZO22001 Starfinder Player Core 030-039::/page/8/Text/17']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 030-039::/page/1/ListItem/10` | 0.954814 | A priest of Triune who travels across the galaxy  installing and repairing Drift beacons, receiving sacred  downloads from Striving's sacred neural network. |
| 2 | `PZO22001 Starfinder Player Core 030-039::/page/0/ListItem/12` | 0.655590 | **The galaxy is connected.** Adventurers have used magical  engines and powerful spells to explore the galaxy  since ancient times, but such travel was rare until the  god Triune introduced hyperspace |
| 3 | `PZO22001 Starfinder Player Core 030-039::/page/8/Text/17` | 0.598294 | Triune is a fusion of the three technological  deities Epoch, Brigh, and Casandalee. Triune's Signal made  Drift travel possible. |
| 4 | `PZO22001 Starfinder Player Core 030-039::/page/4/Text/25` | 0.476181 | Near Space is a term used by people in the galaxy for all  worlds whose nearness to Drift beacons make travel swift  and relatively safe. Communication, trade, and travel between  Near Space planets i |
| 5 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/6` | 0.473227 | The largest community on Aballon is Striving, an  industrious megacity containing a citywide neural network  sacred to Triune. Other regions include the industrial forgecity Automatrix; the immense, f |
| 6 | `PZO22001 Starfinder Player Core 030-039::/page/8/Text/18` | 0.421709 | **Areas of Concern **artificial intelligence, computers, the Drift **Edicts** advance the development of artificial life and  artificial intelligence, innovate new technology, promote  Drift travel |
| 7 | `PZO22001 Starfinder Player Core 030-039::/page/0/Text/6` | 0.404020 | Starfinder occurs in the far future after the Age of Lost Omens,  but there's a Gap in the galaxy's history. About 300 years  ago, something erased an entire era from memory. Records  for this forgott |
| 8 | `PZO22001 Starfinder Player Core 030-039::/page/0/ListItem/9` | 0.403928 | **The galaxy** **is magical.** Proof of people who magically  change reality and channel the primeval forces of the  universe is everywhere, and people know that it's  real. Magic and technology often |
| 9 | `PZO22001 Starfinder Player Core 030-039::/page/5/Text/4` | 0.403664 | Anyone can worship a deity, but those who do so devoutly  should take care to pursue the faith's edicts (behaviors  the faith encourages) and avoid its anathemas (actions  considered blasphemous). Eac |
| 10 | `PZO22001 Starfinder Player Core 030-039::/page/3/ListItem/24` | 0.402892 | A shirren devotee of Hylax, leaving Nchak on a sacred  mission. |

### Query 25
- Text: Summarize CASTROVEL
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 030-039::/page/1/SectionHeader/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 030-039::/page/1/SectionHeader/11', 'PZO22001 Starfinder Player Core 030-039::/page/1/Text/14', 'PZO22001 Starfinder Player Core 030-039::/page/1/Text/13']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 030-039::/page/1/SectionHeader/11` | 0.951780 | CASTROVEL |
| 2 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/14` | 0.521768 | Castrovel's regions include Asana and its major spaceport  Qabarat, a beautiful living monument of ancient walls of  crushed shells cradling a modern metropolis; the towering  hive-city of Queensrock |
| 3 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/13` | 0.480447 | Castrovel is a pristine jungle planet where thriving  metropolises coexist in harmony with nature. Magical  gateways called *aiudara* connect Castrovel's cities, which  are governed by a planetary fed |
| 4 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/18` | 0.408262 | spires of Sovyrian, a nation of surrealist cities sculpted  by elven magic. Castrovel's wilds are virtually unspoiled  because the planet's industry occurs on the super-polluted  moon Elindrae. |
| 5 | `PZO22001 Starfinder Player Core 030-039::/page/4/SectionHeader/27` | 0.301785 | THE VAST |
| 6 | `PZO22001 Starfinder Player Core 030-039::/page/4/Text/29` | 0.252255 | Regions of the Vast include the Azlanti Star Empire, a vast  territory of unknown size controlled by a colonizing regime  ruled by the descendants of a human nation from lost Golarion;  Kazmurg's Absu |
| 7 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/6` | 0.235322 | The largest community on Aballon is Striving, an  industrious megacity containing a citywide neural network  sacred to Triune. Other regions include the industrial forgecity Automatrix; the immense, f |
| 8 | `PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/22` | 0.234428 | **Kasatha World Ship** |
| 9 | `PZO22001 Starfinder Player Core 030-039::/page/4/SectionHeader/7` | 0.233782 | APOSTAE |
| 10 | `PZO22001 Starfinder Player Core 030-039::/page/8/SectionHeader/2` | 0.232009 | TALAVET |

### Query 26
- Text: Summarize **Psychic Federation of Three Powers**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 030-039::/page/1/SectionHeader/12']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 030-039::/page/1/SectionHeader/12', 'PZO22001 Starfinder Player Core 030-039::/page/5/Text/16', 'PZO22001 Starfinder Player Core 030-039::/page/8/Text/13']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 030-039::/page/1/SectionHeader/12` | 1.017604 | **Psychic Federation of Three Powers** |
| 2 | `PZO22001 Starfinder Player Core 030-039::/page/5/Text/16` | 0.385723 | **Divine Skill** Society |
| 3 | `PZO22001 Starfinder Player Core 030-039::/page/8/Text/13` | 0.385723 | **Divine Skill** Society |
| 4 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/13` | 0.346008 | Castrovel is a pristine jungle planet where thriving  metropolises coexist in harmony with nature. Magical  gateways called *aiudara* connect Castrovel's cities, which  are governed by a planetary fed |
| 5 | `PZO22001 Starfinder Player Core 030-039::/page/8/Text/17` | 0.334017 | Triune is a fusion of the three technological  deities Epoch, Brigh, and Casandalee. Triune's Signal made  Drift travel possible. |
| 6 | `PZO22001 Starfinder Player Core 030-039::/page/8/Text/66` | 0.331381 | **Cleric Spells** 1st: *akashic* *download*, 3rd *hypercognition*, 5th:  *dreaming potential* |
| 7 | `PZO22001 Starfinder Player Core 030-039::/page/4/Text/26` | 0.319452 | Near Space regions include the Veskarium, an empire of  seven conquered planets and a few dozen colonies ruled  by vesk military leaders; the Marixah Republic, a group of  allied planets emerging onto |
| 8 | `PZO22001 Starfinder Player Core 030-039::/page/6/Text/26` | 0.315188 | **Domains** knowledge, magic, secrecy, truth |
| 9 | `PZO22001 Starfinder Player Core 030-039::/page/7/Text/42` | 0.313770 | **Anathema** deny occult beliefs, shut out the cosmic other,  interfere with the birth of new ideas or entities |
| 10 | `PZO22001 Starfinder Player Core 030-039::/page/7/Text/45` | 0.311853 | **Cleric Spells** 1st: *shifting surge*, 7th: *warp mind,* 9th: *telekinetic * *tantrum* |

### Query 27
- Text: Summarize Castrovel is a pristine jungle planet where thriving  metropolises coexist in harmony with nature. Magical  gateways called *aiudara* connect Castrovel's cities, which  are governed by a planetary federation of elven councils,  formian queens, and lashunta magnates. Castrovel's unique  infosphere is a web of psychically linked minds; those  without psychic senses connect by bonding with tiny psychic  creatures called shefis.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 030-039::/page/1/Text/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 030-039::/page/1/Text/13', 'PZO22001 Starfinder Player Core 030-039::/page/1/Text/14', 'PZO22001 Starfinder Player Core 030-039::/page/1/Text/18']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/13` | 1.044504 | Castrovel is a pristine jungle planet where thriving  metropolises coexist in harmony with nature. Magical  gateways called *aiudara* connect Castrovel's cities, which  are governed by a planetary fed |
| 2 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/14` | 0.705132 | Castrovel's regions include Asana and its major spaceport  Qabarat, a beautiful living monument of ancient walls of  crushed shells cradling a modern metropolis; the towering  hive-city of Queensrock |
| 3 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/18` | 0.661482 | spires of Sovyrian, a nation of surrealist cities sculpted  by elven magic. Castrovel's wilds are virtually unspoiled  because the planet's industry occurs on the super-polluted  moon Elindrae. |
| 4 | `PZO22001 Starfinder Player Core 030-039::/page/3/Text/21` | 0.547141 | Regions include Roselight, a cloud of floating domes built  by barathu architects, and Deep Station, a research outpost  submerged in Liavara's alien seas. Liavara has many moons:  Hallas, a warded pr |
| 5 | `PZO22001 Starfinder Player Core 030-039::/page/4/Text/29` | 0.510641 | Regions of the Vast include the Azlanti Star Empire, a vast  territory of unknown size controlled by a colonizing regime  ruled by the descendants of a human nation from lost Golarion;  Kazmurg's Absu |
| 6 | `PZO22001 Starfinder Player Core 030-039::/page/3/Text/19` | 0.507439 | Liavara is a peach-colored gas giant encircled by dust  rings and many shepherd moons. In Liavara's upper  atmosphere, elegant arcologies float through swirling  skies; deeper down, piscine titans swi |
| 7 | `PZO22001 Starfinder Player Core 030-039::/page/4/Text/9` | 0.504824 | Apostae is a hollow planetoid with no atmosphere and few  resources. Mysterious gateways on the planet's rocky surface  access a network of tunnels, magitech chambers, and caverns  inside its core. Th |
| 8 | `PZO22001 Starfinder Player Core 030-039::/page/4/Text/10` | 0.499525 | Regions include Nightarch, a pressurized megacity where  opulent spires tower over air-choked slums, named for the  massive gate leading inside the planet at the center of the  settlement; the Silted |
| 9 | `PZO22001 Starfinder Player Core 030-039::/page/3/Text/28` | 0.481430 | Bretheda is a massive, stormy gas giant orbited by moons  where diverse peoples have built thriving, cosmopolitan  societies. Bretheda and its moons are home to cuttingedge biotech foundries, living c |
| 10 | `PZO22001 Starfinder Player Core 030-039::/page/3/Text/29` | 0.478600 | Bretheda's violent storms make most of its gaseous layers  unlivable. The planet's largest city is Trillidiem, a domed,  industrial arcology governed by Confluence, a union of many  merged barathus. B |

### Query 28
- Text: What is the rule about Castrovel's regions include Asana and its major spaceport  Qabarat, a beautiful living monument of ancient walls of  crushed shells cradling a modern metropolis; the towering  hive-city of Queensrock and other formian colonies; the  primeval jungles of Ukulam, protected by communities  of plantlike khizars and their Xenowarden allies; and the?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 030-039::/page/1/Text/14']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 030-039::/page/1/Text/14', 'PZO22001 Starfinder Player Core 030-039::/page/1/Text/13', 'PZO22001 Starfinder Player Core 030-039::/page/1/Text/18']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/14` | 0.997651 | Castrovel's regions include Asana and its major spaceport  Qabarat, a beautiful living monument of ancient walls of  crushed shells cradling a modern metropolis; the towering  hive-city of Queensrock |
| 2 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/13` | 0.671698 | Castrovel is a pristine jungle planet where thriving  metropolises coexist in harmony with nature. Magical  gateways called *aiudara* connect Castrovel's cities, which  are governed by a planetary fed |
| 3 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/18` | 0.601710 | spires of Sovyrian, a nation of surrealist cities sculpted  by elven magic. Castrovel's wilds are virtually unspoiled  because the planet's industry occurs on the super-polluted  moon Elindrae. |
| 4 | `PZO22001 Starfinder Player Core 030-039::/page/4/Text/29` | 0.547761 | Regions of the Vast include the Azlanti Star Empire, a vast  territory of unknown size controlled by a colonizing regime  ruled by the descendants of a human nation from lost Golarion;  Kazmurg's Absu |
| 5 | `PZO22001 Starfinder Player Core 030-039::/page/3/Text/21` | 0.539645 | Regions include Roselight, a cloud of floating domes built  by barathu architects, and Deep Station, a research outpost  submerged in Liavara's alien seas. Liavara has many moons:  Hallas, a warded pr |
| 6 | `PZO22001 Starfinder Player Core 030-039::/page/2/Text/8` | 0.512490 | Akiton's regions include Arl, an ancient city infamous for  historical blood sports that still draw crowds; the trench city  Maro with its Thousand Lights; Ka, a mountain peak sacred  to some shobhad |
| 7 | `PZO22001 Starfinder Player Core 030-039::/page/4/Text/19` | 0.506077 | Regions include Voyedris, a treacherous wilderness  ravaged by rapid industrialization; Hafrerren, a rebel nationstate known for biotech research; Rafemii, a hub for magical  and spiritual development |
| 8 | `PZO22001 Starfinder Player Core 030-039::/page/3/Text/12` | 0.484493 | Regions on Triaxus include the Drakelands, a continental  wilderness preserve tended by dragons; the Skyfire Mandate,  an isthmus guarded by the oldest aeries of the Skyfire Legion;  the Allied Territ |
| 9 | `PZO22001 Starfinder Player Core 030-039::/page/4/Text/10` | 0.477462 | Regions include Nightarch, a pressurized megacity where  opulent spires tower over air-choked slums, named for the  massive gate leading inside the planet at the center of the  settlement; the Silted |
| 10 | `PZO22001 Starfinder Player Core 030-039::/page/3/Text/29` | 0.460667 | Bretheda's violent storms make most of its gaseous layers  unlivable. The planet's largest city is Trillidiem, a domed,  industrial arcology governed by Confluence, a union of many  merged barathus. B |

### Query 29
- Text: Summarize **ADJUSTING THE SETTING**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 030-039::/page/1/SectionHeader/15']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 030-039::/page/1/SectionHeader/15', 'PZO22001 Starfinder Player Core 030-039::/page/1/Text/28', 'PZO22001 Starfinder Player Core 030-039::/page/9/Text/41']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 030-039::/page/1/SectionHeader/15` | 0.973743 | **ADJUSTING THE SETTING** |
| 2 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/28` | 0.440109 | **INTRODUCTION** |
| 3 | `PZO22001 Starfinder Player Core 030-039::/page/9/Text/41` | 0.440109 | **INTRODUCTION** |
| 4 | `PZO22001 Starfinder Player Core 030-039::/page/3/Text/31` | 0.398109 | **INTRODUCTION** |
| 5 | `PZO22001 Starfinder Player Core 030-039::/page/7/Text/80` | 0.398109 | **INTRODUCTION** |
| 6 | `PZO22001 Starfinder Player Core 030-039::/page/5/Text/52` | 0.398109 | **INTRODUCTION** |
| 7 | `PZO22001 Starfinder Player Core 030-039::/page/7/Text/89` | 0.350333 | **EQUIPMENT** |
| 8 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/37` | 0.350333 | **EQUIPMENT** |
| 9 | `PZO22001 Starfinder Player Core 030-039::/page/9/Text/50` | 0.350333 | **EQUIPMENT** |
| 10 | `PZO22001 Starfinder Player Core 030-039::/page/5/Text/61` | 0.350333 | **EQUIPMENT** |

### Query 30
- Text: What is the rule about Feel free to make the galaxy your own! If something  we write in our books gets in the way of a concept you  want to play, ask your group and your GM if you can  change it. What's important isn't that you agree with  the "official" material that we publish, but that the  people you play with facilitate communal storytelling.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 030-039::/page/1/Text/16']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 030-039::/page/1/Text/16', 'PZO22001 Starfinder Player Core 030-039::/page/1/Text/17', 'PZO22001 Starfinder Player Core 030-039::/page/0/Text/8']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/16` | 0.966521 | Feel free to make the galaxy your own! If something  we write in our books gets in the way of a concept you  want to play, ask your group and your GM if you can  change it. What's important isn't that |
| 2 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/17` | 0.622516 | In fact, you don't have to use this setting! While  the Starfinder RPG rules do make some assumptions  about the world, many of these assumptions are  common within the science fantasy genre. Elements |
| 3 | `PZO22001 Starfinder Player Core 030-039::/page/0/Text/8` | 0.550671 | As someone who lives in a science fantasy universe, your  character has a different set of assumptions than someone  from modern Earth. The following are some of these setting  assumptions to keep in |
| 4 | `PZO22001 Starfinder Player Core 030-039::/page/0/Text/2` | 0.458203 | While some players prefer to create a character and define them solely through roleplay, other players  might wish to tie their character into the world through backstory and motives. Knowing the sett |
| 5 | `PZO22001 Starfinder Player Core 030-039::/page/0/Text/4` | 0.439499 | The Starfinder Roleplaying Game rules come with their own  default setting: the galaxy known as Desna's Path. The galaxy  is full of wonder and peril, advanced technology, magic,  meddling deities, an |
| 6 | `PZO22001 Starfinder Player Core 030-039::/page/0/ListItem/9` | 0.438009 | **The galaxy** **is magical.** Proof of people who magically  change reality and channel the primeval forces of the  universe is everywhere, and people know that it's  real. Magic and technology often |
| 7 | `PZO22001 Starfinder Player Core 030-039::/page/0/ListItem/14` | 0.411052 | **The galaxy is dangerous.** Among the planets occupied by  the allied Pact Worlds to Near Space and the remote Vast,  there's usually something causing trouble somewhere.  Adventurers are always seek |
| 8 | `PZO22001 Starfinder Player Core 030-039::/page/4/Text/2` | 0.391921 | A prominent group of adventurers, explorers, and  record-keepers, the Starfinder Society is well known  across the galaxy. This name is shared with Paizo's  official organized play campaign played aro |
| 9 | `PZO22001 Starfinder Player Core 030-039::/page/6/Text/2` | 0.377087 | The cleric spells listed for each deity are intended  to work with the cleric class found in the Pathfinder  Roleplaying Game. Similarly, clerics and some other  devotees can gain domain spells from t |
| 10 | `PZO22001 Starfinder Player Core 030-039::/page/8/Text/5` | 0.376511 | **Areas of Concern **community, storytelling, and tradition |

### Query 31
- Text: What is the rule about In fact, you don't have to use this setting! While  the Starfinder RPG rules do make some assumptions  about the world, many of these assumptions are  common within the science fantasy genre. Elements  that are more specific to our galaxy are often confined  to certain feats and archetypes, which you can change  and remove as you see fit. You can easily use the rules  of Starfinder to run a different setting, or a world of  your own creation.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 030-039::/page/1/Text/17']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 030-039::/page/1/Text/17', 'PZO22001 Starfinder Player Core 030-039::/page/0/Text/8', 'PZO22001 Starfinder Player Core 030-039::/page/0/Text/4']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/17` | 1.023941 | In fact, you don't have to use this setting! While  the Starfinder RPG rules do make some assumptions  about the world, many of these assumptions are  common within the science fantasy genre. Elements |
| 2 | `PZO22001 Starfinder Player Core 030-039::/page/0/Text/8` | 0.779990 | As someone who lives in a science fantasy universe, your  character has a different set of assumptions than someone  from modern Earth. The following are some of these setting  assumptions to keep in |
| 3 | `PZO22001 Starfinder Player Core 030-039::/page/0/Text/4` | 0.756098 | The Starfinder Roleplaying Game rules come with their own  default setting: the galaxy known as Desna's Path. The galaxy  is full of wonder and peril, advanced technology, magic,  meddling deities, an |
| 4 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/16` | 0.624948 | Feel free to make the galaxy your own! If something  we write in our books gets in the way of a concept you  want to play, ask your group and your GM if you can  change it. What's important isn't that |
| 5 | `PZO22001 Starfinder Player Core 030-039::/page/0/Text/2` | 0.573282 | While some players prefer to create a character and define them solely through roleplay, other players  might wish to tie their character into the world through backstory and motives. Knowing the sett |
| 6 | `PZO22001 Starfinder Player Core 030-039::/page/6/Text/2` | 0.565597 | The cleric spells listed for each deity are intended  to work with the cleric class found in the Pathfinder  Roleplaying Game. Similarly, clerics and some other  devotees can gain domain spells from t |
| 7 | `PZO22001 Starfinder Player Core 030-039::/page/4/Text/2` | 0.489137 | A prominent group of adventurers, explorers, and  record-keepers, the Starfinder Society is well known  across the galaxy. This name is shared with Paizo's  official organized play campaign played aro |
| 8 | `PZO22001 Starfinder Player Core 030-039::/page/0/ListItem/9` | 0.475800 | **The galaxy** **is magical.** Proof of people who magically  change reality and channel the primeval forces of the  universe is everywhere, and people know that it's  real. Magic and technology often |
| 9 | `PZO22001 Starfinder Player Core 030-039::/page/0/Text/6` | 0.456393 | Starfinder occurs in the far future after the Age of Lost Omens,  but there's a Gap in the galaxy's history. About 300 years  ago, something erased an entire era from memory. Records  for this forgott |
| 10 | `PZO22001 Starfinder Player Core 030-039::/page/0/Text/16` | 0.454312 | The Pact Worlds form the core of the Starfinder setting.  "The Pact Worlds" is the formal name for the united planets  orbiting lost Golarion's sun and their more distant allied  worlds, including Pul |

### Query 32
- Text: Summarize spires of Sovyrian, a nation of surrealist cities sculpted  by elven magic. Castrovel's wilds are virtually unspoiled  because the planet's industry occurs on the super-polluted  moon Elindrae.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 030-039::/page/1/Text/18']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 030-039::/page/1/Text/18', 'PZO22001 Starfinder Player Core 030-039::/page/1/Text/13', 'PZO22001 Starfinder Player Core 030-039::/page/4/Text/10']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/18` | 1.035951 | spires of Sovyrian, a nation of surrealist cities sculpted  by elven magic. Castrovel's wilds are virtually unspoiled  because the planet's industry occurs on the super-polluted  moon Elindrae. |
| 2 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/13` | 0.638469 | Castrovel is a pristine jungle planet where thriving  metropolises coexist in harmony with nature. Magical  gateways called *aiudara* connect Castrovel's cities, which  are governed by a planetary fed |
| 3 | `PZO22001 Starfinder Player Core 030-039::/page/4/Text/10` | 0.605036 | Regions include Nightarch, a pressurized megacity where  opulent spires tower over air-choked slums, named for the  massive gate leading inside the planet at the center of the  settlement; the Silted |
| 4 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/14` | 0.569737 | Castrovel's regions include Asana and its major spaceport  Qabarat, a beautiful living monument of ancient walls of  crushed shells cradling a modern metropolis; the towering  hive-city of Queensrock |
| 5 | `PZO22001 Starfinder Player Core 030-039::/page/4/Text/19` | 0.532265 | Regions include Voyedris, a treacherous wilderness  ravaged by rapid industrialization; Hafrerren, a rebel nationstate known for biotech research; Rafemii, a hub for magical  and spiritual development |
| 6 | `PZO22001 Starfinder Player Core 030-039::/page/4/Text/9` | 0.525264 | Apostae is a hollow planetoid with no atmosphere and few  resources. Mysterious gateways on the planet's rocky surface  access a network of tunnels, magitech chambers, and caverns  inside its core. Th |
| 7 | `PZO22001 Starfinder Player Core 030-039::/page/3/Text/21` | 0.514623 | Regions include Roselight, a cloud of floating domes built  by barathu architects, and Deep Station, a research outpost  submerged in Liavara's alien seas. Liavara has many moons:  Hallas, a warded pr |
| 8 | `PZO22001 Starfinder Player Core 030-039::/page/4/Text/29` | 0.513382 | Regions of the Vast include the Azlanti Star Empire, a vast  territory of unknown size controlled by a colonizing regime  ruled by the descendants of a human nation from lost Golarion;  Kazmurg's Absu |
| 9 | `PZO22001 Starfinder Player Core 030-039::/page/2/Text/16` | 0.500783 | Major locations on Verces include the Ring of Nations,  a band of sprawling megacities inhabited by augmented  verthani, androids, and many others; Skydock, modern  shipyards built atop an ancient spa |
| 10 | `PZO22001 Starfinder Player Core 030-039::/page/3/Text/29` | 0.498013 | Bretheda's violent storms make most of its gaseous layers  unlivable. The planet's largest city is Trillidiem, a domed,  industrial arcology governed by Confluence, a union of many  merged barathus. B |

### Query 33
- Text: What is the rule about Example Characters?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 030-039::/page/1/SectionHeader/19']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 030-039::/page/1/SectionHeader/19', 'PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/17', 'PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/9']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 030-039::/page/1/SectionHeader/19` | 0.837066 | Example Characters |
| 2 | `PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/9` | 0.837066 | Example Characters |
| 3 | `PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/17` | 0.837066 | Example Characters |
| 4 | `PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/1` | 0.807066 | Example Characters |
| 5 | `PZO22001 Starfinder Player Core 030-039::/page/4/SectionHeader/11` | 0.807066 | Example Characters |
| 6 | `PZO22001 Starfinder Player Core 030-039::/page/4/SectionHeader/3` | 0.807066 | Example Characters |
| 7 | `PZO22001 Starfinder Player Core 030-039::/page/3/SectionHeader/22` | 0.807066 | Example Characters |
| 8 | `PZO22001 Starfinder Player Core 030-039::/page/3/SectionHeader/13` | 0.807066 | Example Characters |
| 9 | `PZO22001 Starfinder Player Core 030-039::/page/3/SectionHeader/4` | 0.807066 | Example Characters |
| 10 | `PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/31` | 0.807066 | Example Characters |

### Query 34
- Text: What is the rule about A lashunta soldier patrolling the jungle accompanied by  a shotalashu hatchling that has imprinted on you.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 030-039::/page/1/ListItem/20']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 030-039::/page/1/ListItem/20', 'PZO22001 Starfinder Player Core 030-039::/page/4/ListItem/12', 'PZO22001 Starfinder Player Core 030-039::/page/8/Text/60']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 030-039::/page/1/ListItem/20` | 0.938008 | A lashunta soldier patrolling the jungle accompanied by  a shotalashu hatchling that has imprinted on you. |
| 2 | `PZO22001 Starfinder Player Core 030-039::/page/4/ListItem/12` | 0.405350 | A corporate assassin hired to guard the scion of a  powerful azrinaran dynasty—when you're not spying on  her rivals or sniping your enemies. |
| 3 | `PZO22001 Starfinder Player Core 030-039::/page/8/Text/60` | 0.403551 | Yaraesa was a lashunta who attained divinity  through enlightenment, guiding others to follow her path. |
| 4 | `PZO22001 Starfinder Player Core 030-039::/page/3/ListItem/16` | 0.333348 | A battleflower, a painted ritual warrior who treats  fighting as an art form. |
| 5 | `PZO22001 Starfinder Player Core 030-039::/page/1/ListItem/22` | 0.321353 | A brave formian hive guard battling the twisted husks  that have emerged from underground to attack your  community. |
| 6 | `PZO22001 Starfinder Player Core 030-039::/page/3/Text/12` | 0.318831 | Regions on Triaxus include the Drakelands, a continental  wilderness preserve tended by dragons; the Skyfire Mandate,  an isthmus guarded by the oldest aeries of the Skyfire Legion;  the Allied Territ |
| 7 | `PZO22001 Starfinder Player Core 030-039::/page/4/Text/29` | 0.311660 | Regions of the Vast include the Azlanti Star Empire, a vast  territory of unknown size controlled by a colonizing regime  ruled by the descendants of a human nation from lost Golarion;  Kazmurg's Absu |
| 8 | `PZO22001 Starfinder Player Core 030-039::/page/3/Text/14` | 0.309823 | • A dragonkin member of the Skyfire Legion, exploring  the galaxy with your bonded partner. |
| 9 | `PZO22001 Starfinder Player Core 030-039::/page/4/ListItem/21` | 0.305678 | A freedom fighter sworn to defend your world's  reclaimed independence at any cost. |
| 10 | `PZO22001 Starfinder Player Core 030-039::/page/1/ListItem/21` | 0.304594 | A young elf ambassador experiencing life outside their  walled ancestral city for the first time. |

### Query 35
- Text: Summarize A young elf ambassador experiencing life outside their  walled ancestral city for the first time.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 030-039::/page/1/ListItem/21']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 030-039::/page/1/ListItem/21', 'PZO22001 Starfinder Player Core 030-039::/page/4/ListItem/23', 'PZO22001 Starfinder Player Core 030-039::/page/8/Text/46']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 030-039::/page/1/ListItem/21` | 1.029332 | A young elf ambassador experiencing life outside their  walled ancestral city for the first time. |
| 2 | `PZO22001 Starfinder Player Core 030-039::/page/4/ListItem/23` | 0.455748 | A mystic wandering the wastes ravaged by the Shriek,  seeking natural ways to heal your war-torn ancestral lands. |
| 3 | `PZO22001 Starfinder Player Core 030-039::/page/8/Text/46` | 0.439364 | Weydan enjoys discovery and exploration with  a purpose. He believes everyone deserves the equal right  to pursue such experiences and walks the galaxy in diverse  avatars to commune with his follower |
| 4 | `PZO22001 Starfinder Player Core 030-039::/page/2/Text/30` | 0.396231 | The Diaspora is an asteroid belt formed long before the  Gap, when a terrible cataclysm destroyed the twin planets  Damiar and Iovo. The remains of the two destroyed worlds  float among millions of ch |
| 5 | `PZO22001 Starfinder Player Core 030-039::/page/2/Text/37` | 0.394742 | Once a green world ruled by living elebrians, Eox is now a  deadly wasteland inhabited by undead. Hubristic elebrian |
| 6 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/18` | 0.391770 | spires of Sovyrian, a nation of surrealist cities sculpted  by elven magic. Castrovel's wilds are virtually unspoiled  because the planet's industry occurs on the super-polluted  moon Elindrae. |
| 7 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/13` | 0.391731 | Castrovel is a pristine jungle planet where thriving  metropolises coexist in harmony with nature. Magical  gateways called *aiudara* connect Castrovel's cities, which  are governed by a planetary fed |
| 8 | `PZO22001 Starfinder Player Core 030-039::/page/1/ListItem/9` | 0.390752 | A Xenowarden nurturing bizarre flora and fauna  deep inside secluded Ice Wells and undermining local  industry. |
| 9 | `PZO22001 Starfinder Player Core 030-039::/page/1/ListItem/8` | 0.383126 | A Starfinder exploring magitech ruins left by the  First Ones, risking encounters with deadly traps and  terrifying sentries. |
| 10 | `PZO22001 Starfinder Player Core 030-039::/page/4/Text/17` | 0.374393 | Pulonis is a low-gravity jungle world wracked by severe  magnetic storms and scarred by war. After years of fighting |

### Query 36
- Text: What is the rule about A brave formian hive guard battling the twisted husks  that have emerged from underground to attack your  community.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 030-039::/page/1/ListItem/22']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 030-039::/page/1/ListItem/22', 'PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/11', 'PZO22001 Starfinder Player Core 030-039::/page/1/ListItem/20']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 030-039::/page/1/ListItem/22` | 0.923660 | A brave formian hive guard battling the twisted husks  that have emerged from underground to attack your  community. |
| 2 | `PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/11` | 0.419831 | A reckless gladiator, battling ferocious beasts and  cunning opponents for glory and riches in the dusty  arenas of Arl. |
| 3 | `PZO22001 Starfinder Player Core 030-039::/page/1/ListItem/20` | 0.414741 | A lashunta soldier patrolling the jungle accompanied by  a shotalashu hatchling that has imprinted on you. |
| 4 | `PZO22001 Starfinder Player Core 030-039::/page/3/Text/2` | 0.349730 | In the modern era, bone sages rule scattered fiefdoms  on Eox's irradiated surface, and hordes of mindless undead  wander the wastes outside magical bunkers and walled  necropolises. Many are tragic b |
| 5 | `PZO22001 Starfinder Player Core 030-039::/page/4/ListItem/23` | 0.348108 | A mystic wandering the wastes ravaged by the Shriek,  seeking natural ways to heal your war-torn ancestral lands. |
| 6 | `PZO22001 Starfinder Player Core 030-039::/page/2/Text/37` | 0.344610 | Once a green world ruled by living elebrians, Eox is now a  deadly wasteland inhabited by undead. Hubristic elebrian |
| 7 | `PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/3` | 0.343737 | A ghost courier, exploring the Ghost Levels on a hunt  for valuable relics, surviving dangerous anomalies and  fighting dimensionally displaced monsters. |
| 8 | `PZO22001 Starfinder Player Core 030-039::/page/6/Text/31` | 0.341301 | Hylax was once a mortal shirren hive queen who  ascended to divinity. |
| 9 | `PZO22001 Starfinder Player Core 030-039::/page/4/ListItem/12` | 0.337779 | A corporate assassin hired to guard the scion of a  powerful azrinaran dynasty—when you're not spying on  her rivals or sniping your enemies. |
| 10 | `PZO22001 Starfinder Player Core 030-039::/page/5/Text/36` | 0.335055 | **Edicts** crush your enemies, seek victory, fight worthy foes |

### Query 37
- Text: Summarize ABSALOM STATION
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 030-039::/page/1/SectionHeader/23']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 030-039::/page/1/SectionHeader/23', 'PZO22001 Starfinder Player Core 030-039::/page/1/Text/25', 'PZO22001 Starfinder Player Core 030-039::/page/1/Text/26']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 030-039::/page/1/SectionHeader/23` | 0.986652 | ABSALOM STATION |
| 2 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/25` | 0.600047 | Floating in lost Golarion's empty orbit, this bustling space  station is the center of interstellar trade and governance  in the Pact Worlds. Nobody knows who built Absalom  Station because it appeare |
| 3 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/26` | 0.585015 | At the center of Absalom Station is the Eye, a shielded  sector famous for lush Jatembe Park, glittering corporate  towers and luxurious neighborhoods, and a sprawling  academic sector that houses a s |
| 4 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/1` | 0.386541 | The united worlds are Absalom Station, Aballon, Castrovel,  Akiton, Verces, the Diaspora, Eox, Triaxus, Dykon, Kalo-Mahoi,  Marata, Liavara, and Bretheda. The *Idari*—a starship—is counted  among thei |
| 5 | `PZO22001 Starfinder Player Core 030-039::/page/1/SectionHeader/3` | 0.376063 | ABALLON |
| 6 | `PZO22001 Starfinder Player Core 030-039::/page/0/Text/6` | 0.340832 | Starfinder occurs in the far future after the Age of Lost Omens,  but there's a Gap in the galaxy's history. About 300 years  ago, something erased an entire era from memory. Records  for this forgott |
| 7 | `PZO22001 Starfinder Player Core 030-039::/page/4/SectionHeader/7` | 0.328613 | APOSTAE |
| 8 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/5` | 0.318614 | Aballon is a rocky, cratered world of superheated metallic  deserts and deep ice wells. Thousands of years before the  Gap, a mysterious civilization called the First Ones utilized  Aballon's abundant |
| 9 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/6` | 0.313843 | The largest community on Aballon is Striving, an  industrious megacity containing a citywide neural network  sacred to Triune. Other regions include the industrial forgecity Automatrix; the immense, f |
| 10 | `PZO22001 Starfinder Player Core 030-039::/page/0/ListItem/12` | 0.311225 | **The galaxy is connected.** Adventurers have used magical  engines and powerful spells to explore the galaxy  since ancient times, but such travel was rare until the  god Triune introduced hyperspace |

### Query 38
- Text: What is the rule about **Galactic Trade Nexus**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 030-039::/page/1/SectionHeader/24']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 030-039::/page/1/SectionHeader/24', 'PZO22001 Starfinder Player Core 030-039::/page/1/Text/31', 'PZO22001 Starfinder Player Core 030-039::/page/3/Text/34']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 030-039::/page/1/SectionHeader/24` | 0.889907 | **Galactic Trade Nexus** |
| 2 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/31` | 0.428263 | **Exploring the ** **Galaxy** |
| 3 | `PZO22001 Starfinder Player Core 030-039::/page/3/Text/34` | 0.428263 | **Exploring the ** **Galaxy** |
| 4 | `PZO22001 Starfinder Player Core 030-039::/page/7/Text/83` | 0.386263 | **Exploring the ** **Galaxy** |
| 5 | `PZO22001 Starfinder Player Core 030-039::/page/9/Text/44` | 0.386263 | **Exploring the ** **Galaxy** |
| 6 | `PZO22001 Starfinder Player Core 030-039::/page/5/Text/55` | 0.386263 | **Exploring the ** **Galaxy** |
| 7 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/16` | 0.385381 | Feel free to make the galaxy your own! If something  we write in our books gets in the way of a concept you  want to play, ask your group and your GM if you can  change it. What's important isn't that |
| 8 | `PZO22001 Starfinder Player Core 030-039::/page/0/ListItem/14` | 0.379067 | **The galaxy is dangerous.** Among the planets occupied by  the allied Pact Worlds to Near Space and the remote Vast,  there's usually something causing trouble somewhere.  Adventurers are always seek |
| 9 | `PZO22001 Starfinder Player Core 030-039::/page/4/Text/25` | 0.374003 | Near Space is a term used by people in the galaxy for all  worlds whose nearness to Drift beacons make travel swift  and relatively safe. Communication, trade, and travel between  Near Space planets i |
| 10 | `PZO22001 Starfinder Player Core 030-039::/page/5/Text/63` | 0.372259 | **GAME** **CONDITIONS ** |

### Query 39
- Text: What is the rule about Floating in lost Golarion's empty orbit, this bustling space  station is the center of interstellar trade and governance  in the Pact Worlds. Nobody knows who built Absalom  Station because it appeared sometime during the Gap. The  station's ancient magitech reactors are powered by the  legendary *Starstone*, which also acts as the most powerful  Drift beacon, inviting tourists and immigrants from  faraway worlds. Hundreds of corporations and embassies  have built headquarters here and a diverse population  calls it home.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 030-039::/page/1/Text/25']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 030-039::/page/1/Text/25', 'PZO22001 Starfinder Player Core 030-039::/page/0/Text/6', 'PZO22001 Starfinder Player Core 030-039::/page/0/ListItem/12']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/25` | 0.977328 | Floating in lost Golarion's empty orbit, this bustling space  station is the center of interstellar trade and governance  in the Pact Worlds. Nobody knows who built Absalom  Station because it appeare |
| 2 | `PZO22001 Starfinder Player Core 030-039::/page/0/Text/6` | 0.685301 | Starfinder occurs in the far future after the Age of Lost Omens,  but there's a Gap in the galaxy's history. About 300 years  ago, something erased an entire era from memory. Records  for this forgott |
| 3 | `PZO22001 Starfinder Player Core 030-039::/page/0/ListItem/12` | 0.668130 | **The galaxy is connected.** Adventurers have used magical  engines and powerful spells to explore the galaxy  since ancient times, but such travel was rare until the  god Triune introduced hyperspace |
| 4 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/26` | 0.617228 | At the center of Absalom Station is the Eye, a shielded  sector famous for lush Jatembe Park, glittering corporate  towers and luxurious neighborhoods, and a sprawling  academic sector that houses a s |
| 5 | `PZO22001 Starfinder Player Core 030-039::/page/4/Text/9` | 0.594793 | Apostae is a hollow planetoid with no atmosphere and few  resources. Mysterious gateways on the planet's rocky surface  access a network of tunnels, magitech chambers, and caverns  inside its core. Th |
| 6 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/1` | 0.562838 | The united worlds are Absalom Station, Aballon, Castrovel,  Akiton, Verces, the Diaspora, Eox, Triaxus, Dykon, Kalo-Mahoi,  Marata, Liavara, and Bretheda. The *Idari*—a starship—is counted  among thei |
| 7 | `PZO22001 Starfinder Player Core 030-039::/page/0/Text/16` | 0.554026 | The Pact Worlds form the core of the Starfinder setting.  "The Pact Worlds" is the formal name for the united planets  orbiting lost Golarion's sun and their more distant allied  worlds, including Pul |
| 8 | `PZO22001 Starfinder Player Core 030-039::/page/3/Text/21` | 0.536407 | Regions include Roselight, a cloud of floating domes built  by barathu architects, and Deep Station, a research outpost  submerged in Liavara's alien seas. Liavara has many moons:  Hallas, a warded pr |
| 9 | `PZO22001 Starfinder Player Core 030-039::/page/4/Text/28` | 0.528185 | The dangerous, infrequently traveled outskirts of the galaxy  and the endless sprawl of uncharted space beyond are called  the Vast. Only a handful of scattered Drift beacons exist to  guide ships thr |
| 10 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/5` | 0.520130 | Aballon is a rocky, cratered world of superheated metallic  deserts and deep ice wells. Thousands of years before the  Gap, a mysterious civilization called the First Ones utilized  Aballon's abundant |

### Query 40
- Text: What is the rule about At the center of Absalom Station is the Eye, a shielded  sector famous for lush Jatembe Park, glittering corporate  towers and luxurious neighborhoods, and a sprawling  academic sector that houses a solarian cosmonastery and  university. The Ring is a cluster of eclectic neighborhoods and  industrial districts encircling the Eye; the Arms are a series  of hangars and docks protruding from the Ring; the Spike  is a warren of dilapidated industrial tunnels that intersect  with the dangerous Ghost Levels; and the Armada is a ragtag  swarm of ships docked in orbit.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 030-039::/page/1/Text/26']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 030-039::/page/1/Text/26', 'PZO22001 Starfinder Player Core 030-039::/page/1/Text/25', 'PZO22001 Starfinder Player Core 030-039::/page/3/Text/21']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/26` | 0.982968 | At the center of Absalom Station is the Eye, a shielded  sector famous for lush Jatembe Park, glittering corporate  towers and luxurious neighborhoods, and a sprawling  academic sector that houses a s |
| 2 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/25` | 0.684088 | Floating in lost Golarion's empty orbit, this bustling space  station is the center of interstellar trade and governance  in the Pact Worlds. Nobody knows who built Absalom  Station because it appeare |
| 3 | `PZO22001 Starfinder Player Core 030-039::/page/3/Text/21` | 0.564092 | Regions include Roselight, a cloud of floating domes built  by barathu architects, and Deep Station, a research outpost  submerged in Liavara's alien seas. Liavara has many moons:  Hallas, a warded pr |
| 4 | `PZO22001 Starfinder Player Core 030-039::/page/1/SectionHeader/23` | 0.513489 | ABSALOM STATION |
| 5 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/6` | 0.506866 | The largest community on Aballon is Striving, an  industrious megacity containing a citywide neural network  sacred to Triune. Other regions include the industrial forgecity Automatrix; the immense, f |
| 6 | `PZO22001 Starfinder Player Core 030-039::/page/4/Text/10` | 0.491318 | Regions include Nightarch, a pressurized megacity where  opulent spires tower over air-choked slums, named for the  massive gate leading inside the planet at the center of the  settlement; the Silted |
| 7 | `PZO22001 Starfinder Player Core 030-039::/page/2/Text/15` | 0.486786 | Verces is a tidally locked world with a sun-scoured light side,  a frozen dark side, and a belt of opulent cybercities linked by  high-speed bullet trains called the Ring of Nations. The Ring  of Nati |
| 8 | `PZO22001 Starfinder Player Core 030-039::/page/4/Text/29` | 0.486661 | Regions of the Vast include the Azlanti Star Empire, a vast  territory of unknown size controlled by a colonizing regime  ruled by the descendants of a human nation from lost Golarion;  Kazmurg's Absu |
| 9 | `PZO22001 Starfinder Player Core 030-039::/page/2/Text/16` | 0.477683 | Major locations on Verces include the Ring of Nations,  a band of sprawling megacities inhabited by augmented  verthani, androids, and many others; Skydock, modern  shipyards built atop an ancient spa |
| 10 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/1` | 0.476602 | The united worlds are Absalom Station, Aballon, Castrovel,  Akiton, Verces, the Diaspora, Eox, Triaxus, Dykon, Kalo-Mahoi,  Marata, Liavara, and Bretheda. The *Idari*—a starship—is counted  among thei |

### Query 41
- Text: Summarize **INTRODUCTION**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 030-039::/page/1/Text/28']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 030-039::/page/1/Text/28', 'PZO22001 Starfinder Player Core 030-039::/page/3/Text/31', 'PZO22001 Starfinder Player Core 030-039::/page/5/Text/52']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/28` | 0.880541 | **INTRODUCTION** |
| 2 | `PZO22001 Starfinder Player Core 030-039::/page/3/Text/31` | 0.880541 | **INTRODUCTION** |
| 3 | `PZO22001 Starfinder Player Core 030-039::/page/5/Text/52` | 0.880541 | **INTRODUCTION** |
| 4 | `PZO22001 Starfinder Player Core 030-039::/page/9/Text/41` | 0.838541 | **INTRODUCTION** |
| 5 | `PZO22001 Starfinder Player Core 030-039::/page/7/Text/80` | 0.838541 | **INTRODUCTION** |
| 6 | `PZO22001 Starfinder Player Core 030-039::/page/9/Text/56` | 0.452320 | **GAME** |
| 7 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/33` | 0.404404 | **ANCESTRIES & ** **BACKGROUNDS** |
| 8 | `PZO22001 Starfinder Player Core 030-039::/page/5/Text/57` | 0.404404 | **ANCESTRIES & ** **BACKGROUNDS** |
| 9 | `PZO22001 Starfinder Player Core 030-039::/page/3/Text/36` | 0.404404 | **ANCESTRIES & ** **BACKGROUNDS** |
| 10 | `PZO22001 Starfinder Player Core 030-039::/page/7/Text/85` | 0.404404 | **ANCESTRIES & ** **BACKGROUNDS** |

### Query 42
- Text: What is the rule about **Character ** **Creation**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 030-039::/page/1/Text/29']
- Expected found: `True`
- Expected rank: `4`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 030-039::/page/5/Text/53', 'PZO22001 Starfinder Player Core 030-039::/page/3/Text/32', 'PZO22001 Starfinder Player Core 030-039::/page/9/Text/42']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 030-039::/page/9/Text/42` | 0.851651 | **Character ** **Creation** |
| 2 | `PZO22001 Starfinder Player Core 030-039::/page/5/Text/53` | 0.851651 | **Character ** **Creation** |
| 3 | `PZO22001 Starfinder Player Core 030-039::/page/3/Text/32` | 0.851651 | **Character ** **Creation** |
| 4 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/29` | 0.809651 | **Character ** **Creation** |
| 5 | `PZO22001 Starfinder Player Core 030-039::/page/7/Text/81` | 0.809651 | **Character ** **Creation** |
| 6 | `PZO22001 Starfinder Player Core 030-039::/page/0/SectionHeader/7` | 0.483031 | WHAT DOES MY CHARACTER  KNOW? |
| 7 | `PZO22001 Starfinder Player Core 030-039::/page/0/Text/8` | 0.477770 | As someone who lives in a science fantasy universe, your  character has a different set of assumptions than someone  from modern Earth. The following are some of these setting  assumptions to keep in |
| 8 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/16` | 0.434266 | Feel free to make the galaxy your own! If something  we write in our books gets in the way of a concept you  want to play, ask your group and your GM if you can  change it. What's important isn't that |
| 9 | `PZO22001 Starfinder Player Core 030-039::/page/1/SectionHeader/7` | 0.432619 | Example Characters |
| 10 | `PZO22001 Starfinder Player Core 030-039::/page/4/SectionHeader/11` | 0.432619 | Example Characters |

### Query 43
- Text: Summarize **Leveling Up**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 030-039::/page/1/Text/30']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 030-039::/page/3/Text/33', 'PZO22001 Starfinder Player Core 030-039::/page/1/Text/30', 'PZO22001 Starfinder Player Core 030-039::/page/9/Text/43']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 030-039::/page/3/Text/33` | 0.970922 | **Leveling Up** |
| 2 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/30` | 0.970922 | **Leveling Up** |
| 3 | `PZO22001 Starfinder Player Core 030-039::/page/9/Text/43` | 0.970922 | **Leveling Up** |
| 4 | `PZO22001 Starfinder Player Core 030-039::/page/5/Text/54` | 0.928922 | **Leveling Up** |
| 5 | `PZO22001 Starfinder Player Core 030-039::/page/7/Text/82` | 0.928922 | **Leveling Up** |
| 6 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/28` | 0.308527 | **INTRODUCTION** |
| 7 | `PZO22001 Starfinder Player Core 030-039::/page/7/Text/80` | 0.308527 | **INTRODUCTION** |
| 8 | `PZO22001 Starfinder Player Core 030-039::/page/9/Text/41` | 0.308527 | **INTRODUCTION** |
| 9 | `PZO22001 Starfinder Player Core 030-039::/page/5/Text/52` | 0.308527 | **INTRODUCTION** |
| 10 | `PZO22001 Starfinder Player Core 030-039::/page/3/Text/31` | 0.308527 | **INTRODUCTION** |

### Query 44
- Text: Summarize **Exploring the ** **Galaxy**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 030-039::/page/1/Text/31']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 030-039::/page/3/Text/34', 'PZO22001 Starfinder Player Core 030-039::/page/1/Text/31', 'PZO22001 Starfinder Player Core 030-039::/page/9/Text/44']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 030-039::/page/3/Text/34` | 0.993218 | **Exploring the ** **Galaxy** |
| 2 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/31` | 0.993218 | **Exploring the ** **Galaxy** |
| 3 | `PZO22001 Starfinder Player Core 030-039::/page/9/Text/44` | 0.993218 | **Exploring the ** **Galaxy** |
| 4 | `PZO22001 Starfinder Player Core 030-039::/page/5/Text/55` | 0.951218 | **Exploring the ** **Galaxy** |
| 5 | `PZO22001 Starfinder Player Core 030-039::/page/7/Text/83` | 0.951218 | **Exploring the ** **Galaxy** |
| 6 | `PZO22001 Starfinder Player Core 030-039::/page/0/SectionHeader/1` | 0.701401 | EXPLORING THE  GALAXY |
| 7 | `PZO22001 Starfinder Player Core 030-039::/page/0/ListItem/10` | 0.565864 | **The galaxy has technology.** Tech from computers  to starship systems are part of everyday life. |
| 8 | `PZO22001 Starfinder Player Core 030-039::/page/0/ListItem/13` | 0.561332 | **The galaxy is diverse.** Countless worlds and cultures  flourish all over the galaxy (and beyond). Travelers  from Near Space often visit the Pact Worlds (and vice  versa). Visitors from the Vast ar |
| 9 | `PZO22001 Starfinder Player Core 030-039::/page/0/ListItem/9` | 0.523404 | **The galaxy** **is magical.** Proof of people who magically  change reality and channel the primeval forces of the  universe is everywhere, and people know that it's  real. Magic and technology often |
| 10 | `PZO22001 Starfinder Player Core 030-039::/page/0/ListItem/14` | 0.516939 | **The galaxy is dangerous.** Among the planets occupied by  the allied Pact Worlds to Near Space and the remote Vast,  there's usually something causing trouble somewhere.  Adventurers are always seek |

### Query 45
- Text: Summarize **Religion**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 030-039::/page/1/Text/32']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 030-039::/page/1/Text/32', 'PZO22001 Starfinder Player Core 030-039::/page/3/Text/35', 'PZO22001 Starfinder Player Core 030-039::/page/5/Text/56']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/32` | 0.921440 | **Religion** |
| 2 | `PZO22001 Starfinder Player Core 030-039::/page/3/Text/35` | 0.921440 | **Religion** |
| 3 | `PZO22001 Starfinder Player Core 030-039::/page/5/Text/56` | 0.921440 | **Religion** |
| 4 | `PZO22001 Starfinder Player Core 030-039::/page/9/Text/45` | 0.879440 | **Religion** |
| 5 | `PZO22001 Starfinder Player Core 030-039::/page/7/Text/84` | 0.879440 | **Religion** |
| 6 | `PZO22001 Starfinder Player Core 030-039::/page/5/SectionHeader/0` | 0.750142 | RELIGION |
| 7 | `PZO22001 Starfinder Player Core 030-039::/page/5/Text/1` | 0.462147 | Technology and scientific knowledge flourish across the galaxy, but these advancements can't  solve every problem or answer all existential questions. Many turn to religion to understand their  place |
| 8 | `PZO22001 Starfinder Player Core 030-039::/page/6/Text/36` | 0.437766 | **Cleric Spells** 1st: *ant haul*, 3rd: *insect form*, 5th: *subjective* *reality* |
| 9 | `PZO22001 Starfinder Player Core 030-039::/page/9/Text/9` | 0.424455 | Faith can express itself in more ways than venerating a single  deity—or any deity at all. A few examples of popular nondeific religions and philosophies are presented below. These  faiths and philoso |
| 10 | `PZO22001 Starfinder Player Core 030-039::/page/9/Text/14` | 0.423743 | excel **Anathema** offer prayers to a deity |

### Query 46
- Text: What is the rule about **ANCESTRIES & ** **BACKGROUNDS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 030-039::/page/1/Text/33']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 030-039::/page/1/Text/33', 'PZO22001 Starfinder Player Core 030-039::/page/7/Text/85', 'PZO22001 Starfinder Player Core 030-039::/page/9/Text/46']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/33` | 0.920820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 2 | `PZO22001 Starfinder Player Core 030-039::/page/7/Text/85` | 0.920820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 3 | `PZO22001 Starfinder Player Core 030-039::/page/9/Text/46` | 0.920820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 4 | `PZO22001 Starfinder Player Core 030-039::/page/5/Text/57` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 5 | `PZO22001 Starfinder Player Core 030-039::/page/3/Text/36` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 6 | `PZO22001 Starfinder Player Core 030-039::/page/5/Text/63` | 0.348173 | **GAME** **CONDITIONS ** |
| 7 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/40` | 0.343180 | **CONDITIONS ** **APPENDIX** |
| 8 | `PZO22001 Starfinder Player Core 030-039::/page/7/Text/92` | 0.343180 | **CONDITIONS ** **APPENDIX** |
| 9 | `PZO22001 Starfinder Player Core 030-039::/page/3/Text/43` | 0.343180 | **CONDITIONS ** **APPENDIX** |
| 10 | `PZO22001 Starfinder Player Core 030-039::/page/9/Text/52` | 0.343180 | **CONDITIONS ** **APPENDIX** |

### Query 47
- Text: Summarize **CLASSES**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 030-039::/page/1/Text/34']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 030-039::/page/1/Text/34', 'PZO22001 Starfinder Player Core 030-039::/page/3/Text/37', 'PZO22001 Starfinder Player Core 030-039::/page/5/Text/58']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/34` | 0.940061 | **CLASSES** |
| 2 | `PZO22001 Starfinder Player Core 030-039::/page/3/Text/37` | 0.940061 | **CLASSES** |
| 3 | `PZO22001 Starfinder Player Core 030-039::/page/5/Text/58` | 0.940061 | **CLASSES** |
| 4 | `PZO22001 Starfinder Player Core 030-039::/page/7/Text/86` | 0.910061 | **CLASSES** |
| 5 | `PZO22001 Starfinder Player Core 030-039::/page/9/Text/47` | 0.910061 | **CLASSES** |
| 6 | `PZO22001 Starfinder Player Core 030-039::/page/5/Text/59` | 0.437714 | **SKILLS** |
| 7 | `PZO22001 Starfinder Player Core 030-039::/page/3/Text/38` | 0.437714 | **SKILLS** |
| 8 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/35` | 0.437714 | **SKILLS** |
| 9 | `PZO22001 Starfinder Player Core 030-039::/page/5/Text/52` | 0.435377 | **INTRODUCTION** |
| 10 | `PZO22001 Starfinder Player Core 030-039::/page/3/Text/31` | 0.435377 | **INTRODUCTION** |

### Query 48
- Text: What is the rule about **SKILLS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 030-039::/page/1/Text/35']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 030-039::/page/5/Text/59', 'PZO22001 Starfinder Player Core 030-039::/page/1/Text/35', 'PZO22001 Starfinder Player Core 030-039::/page/9/Text/48']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 030-039::/page/5/Text/59` | 0.864442 | **SKILLS** |
| 2 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/35` | 0.864442 | **SKILLS** |
| 3 | `PZO22001 Starfinder Player Core 030-039::/page/9/Text/48` | 0.864442 | **SKILLS** |
| 4 | `PZO22001 Starfinder Player Core 030-039::/page/3/Text/38` | 0.822442 | **SKILLS** |
| 5 | `PZO22001 Starfinder Player Core 030-039::/page/7/Text/87` | 0.822442 | **SKILLS** |
| 6 | `PZO22001 Starfinder Player Core 030-039::/page/7/Text/34` | 0.506139 | **Divine Skill** Performance |
| 7 | `PZO22001 Starfinder Player Core 030-039::/page/6/Text/67` | 0.500362 | **Divine Skill** Computers |
| 8 | `PZO22001 Starfinder Player Core 030-039::/page/8/Text/25` | 0.500362 | **Divine Skill** Computers |
| 9 | `PZO22001 Starfinder Player Core 030-039::/page/7/Text/48` | 0.481800 | **Divine Skill** Occultism |
| 10 | `PZO22001 Starfinder Player Core 030-039::/page/6/Text/52` | 0.481800 | **Divine Skill** Occultism |

### Query 49
- Text: What is the rule about **FEATS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 030-039::/page/1/Text/36']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 030-039::/page/3/Text/39', 'PZO22001 Starfinder Player Core 030-039::/page/1/Text/36', 'PZO22001 Starfinder Player Core 030-039::/page/7/Text/88']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 030-039::/page/3/Text/39` | 0.871817 | **FEATS** |
| 2 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/36` | 0.871817 | **FEATS** |
| 3 | `PZO22001 Starfinder Player Core 030-039::/page/7/Text/88` | 0.871817 | **FEATS** |
| 4 | `PZO22001 Starfinder Player Core 030-039::/page/5/Text/60` | 0.829817 | **FEATS** |
| 5 | `PZO22001 Starfinder Player Core 030-039::/page/9/Text/49` | 0.829817 | **FEATS** |
| 6 | `PZO22001 Starfinder Player Core 030-039::/page/9/SectionHeader/32` | 0.369643 | GREEN FAITH |
| 7 | `PZO22001 Starfinder Player Core 030-039::/page/9/SectionHeader/8` | 0.345575 | FAITHS AND PHILOSOPHIES |
| 8 | `PZO22001 Starfinder Player Core 030-039::/page/7/Text/11` | 0.336911 | **Areas of Concern **duty, fate, obedience, reward of service |
| 9 | `PZO22001 Starfinder Player Core 030-039::/page/7/Text/68` | 0.308131 | **Areas of Concern **birth, death, fate, prophecy, time |
| 10 | `PZO22001 Starfinder Player Core 030-039::/page/7/Text/20` | 0.305138 | **Domains **fate, glyph (*Divine* *Mysteries*), magic, toil (*Pathfinder* *Rage* *of* *Elements*) |

### Query 50
- Text: Summarize **EQUIPMENT**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 030-039::/page/1/Text/37']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 030-039::/page/1/Text/37', 'PZO22001 Starfinder Player Core 030-039::/page/3/Text/40', 'PZO22001 Starfinder Player Core 030-039::/page/7/Text/89']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/37` | 0.944726 | **EQUIPMENT** |
| 2 | `PZO22001 Starfinder Player Core 030-039::/page/3/Text/40` | 0.944726 | **EQUIPMENT** |
| 3 | `PZO22001 Starfinder Player Core 030-039::/page/7/Text/89` | 0.944726 | **EQUIPMENT** |
| 4 | `PZO22001 Starfinder Player Core 030-039::/page/5/Text/61` | 0.902726 | **EQUIPMENT** |
| 5 | `PZO22001 Starfinder Player Core 030-039::/page/9/Text/50` | 0.902726 | **EQUIPMENT** |
| 6 | `PZO22001 Starfinder Player Core 030-039::/page/7/Text/80` | 0.385549 | **INTRODUCTION** |
| 7 | `PZO22001 Starfinder Player Core 030-039::/page/3/Text/31` | 0.385549 | **INTRODUCTION** |
| 8 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/28` | 0.385549 | **INTRODUCTION** |
| 9 | `PZO22001 Starfinder Player Core 030-039::/page/9/Text/41` | 0.385549 | **INTRODUCTION** |
| 10 | `PZO22001 Starfinder Player Core 030-039::/page/5/Text/52` | 0.385549 | **INTRODUCTION** |

### Query 51
- Text: What is the rule about **SPELLS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 030-039::/page/1/Text/38']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 030-039::/page/1/Text/38', 'PZO22001 Starfinder Player Core 030-039::/page/3/Text/41', 'PZO22001 Starfinder Player Core 030-039::/page/7/Text/90']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/38` | 0.889304 | **SPELLS** |
| 2 | `PZO22001 Starfinder Player Core 030-039::/page/3/Text/41` | 0.889304 | **SPELLS** |
| 3 | `PZO22001 Starfinder Player Core 030-039::/page/7/Text/90` | 0.889304 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 030-039::/page/5/Text/62` | 0.740792 | **SPELLS** **PLAYING THE ** |
| 5 | `PZO22001 Starfinder Player Core 030-039::/page/9/Text/51` | 0.740792 | **SPELLS** **PLAYING THE ** |
| 6 | `PZO22001 Starfinder Player Core 030-039::/page/5/Text/59` | 0.388254 | **SKILLS** |
| 7 | `PZO22001 Starfinder Player Core 030-039::/page/3/Text/38` | 0.388254 | **SKILLS** |
| 8 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/35` | 0.388254 | **SKILLS** |
| 9 | `PZO22001 Starfinder Player Core 030-039::/page/9/Text/48` | 0.388254 | **SKILLS** |
| 10 | `PZO22001 Starfinder Player Core 030-039::/page/7/Text/87` | 0.388254 | **SKILLS** |

### Query 52
- Text: Summarize **PLAYING THE ** **GAME**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 030-039::/page/1/Text/39']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 030-039::/page/1/Text/39', 'PZO22001 Starfinder Player Core 030-039::/page/3/Text/42', 'PZO22001 Starfinder Player Core 030-039::/page/7/Text/91']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/39` | 0.965000 | **PLAYING THE ** **GAME** |
| 2 | `PZO22001 Starfinder Player Core 030-039::/page/3/Text/42` | 0.965000 | **PLAYING THE ** **GAME** |
| 3 | `PZO22001 Starfinder Player Core 030-039::/page/7/Text/91` | 0.965000 | **PLAYING THE ** **GAME** |
| 4 | `PZO22001 Starfinder Player Core 030-039::/page/9/Text/56` | 0.663024 | **GAME** |
| 5 | `PZO22001 Starfinder Player Core 030-039::/page/5/Text/62` | 0.576671 | **SPELLS** **PLAYING THE ** |
| 6 | `PZO22001 Starfinder Player Core 030-039::/page/9/Text/51` | 0.576671 | **SPELLS** **PLAYING THE ** |
| 7 | `PZO22001 Starfinder Player Core 030-039::/page/5/Text/63` | 0.545563 | **GAME** **CONDITIONS ** |
| 8 | `PZO22001 Starfinder Player Core 030-039::/page/3/Text/31` | 0.418586 | **INTRODUCTION** |
| 9 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/28` | 0.418586 | **INTRODUCTION** |
| 10 | `PZO22001 Starfinder Player Core 030-039::/page/7/Text/80` | 0.418586 | **INTRODUCTION** |

### Query 53
- Text: Summarize **CONDITIONS ** **APPENDIX**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 030-039::/page/1/Text/40']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 030-039::/page/1/Text/40', 'PZO22001 Starfinder Player Core 030-039::/page/9/Text/52', 'PZO22001 Starfinder Player Core 030-039::/page/7/Text/92']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/40` | 0.983498 | **CONDITIONS ** **APPENDIX** |
| 2 | `PZO22001 Starfinder Player Core 030-039::/page/7/Text/92` | 0.983498 | **CONDITIONS ** **APPENDIX** |
| 3 | `PZO22001 Starfinder Player Core 030-039::/page/9/Text/52` | 0.983498 | **CONDITIONS ** **APPENDIX** |
| 4 | `PZO22001 Starfinder Player Core 030-039::/page/3/Text/43` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 5 | `PZO22001 Starfinder Player Core 030-039::/page/5/Text/64` | 0.769880 | **APPENDIX** |
| 6 | `PZO22001 Starfinder Player Core 030-039::/page/5/Text/63` | 0.535379 | **GAME** **CONDITIONS ** |
| 7 | `PZO22001 Starfinder Player Core 030-039::/page/3/Text/36` | 0.416141 | **ANCESTRIES & ** **BACKGROUNDS** |
| 8 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/33` | 0.416141 | **ANCESTRIES & ** **BACKGROUNDS** |
| 9 | `PZO22001 Starfinder Player Core 030-039::/page/9/Text/46` | 0.416141 | **ANCESTRIES & ** **BACKGROUNDS** |
| 10 | `PZO22001 Starfinder Player Core 030-039::/page/7/Text/85` | 0.416141 | **ANCESTRIES & ** **BACKGROUNDS** |

### Query 54
- Text: Summarize **GLOSSARY & ** **INDEX**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 030-039::/page/1/Text/41']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 030-039::/page/1/Text/41', 'PZO22001 Starfinder Player Core 030-039::/page/3/Text/44', 'PZO22001 Starfinder Player Core 030-039::/page/5/Text/65']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/41` | 0.993465 | **GLOSSARY & ** **INDEX** |
| 2 | `PZO22001 Starfinder Player Core 030-039::/page/3/Text/44` | 0.993465 | **GLOSSARY & ** **INDEX** |
| 3 | `PZO22001 Starfinder Player Core 030-039::/page/5/Text/65` | 0.993465 | **GLOSSARY & ** **INDEX** |
| 4 | `PZO22001 Starfinder Player Core 030-039::/page/7/Text/93` | 0.951465 | **GLOSSARY & ** **INDEX** |
| 5 | `PZO22001 Starfinder Player Core 030-039::/page/9/Text/53` | 0.951465 | **GLOSSARY & ** **INDEX** |
| 6 | `PZO22001 Starfinder Player Core 030-039::/page/3/Text/37` | 0.385404 | **CLASSES** |
| 7 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/34` | 0.385404 | **CLASSES** |
| 8 | `PZO22001 Starfinder Player Core 030-039::/page/9/Text/47` | 0.385404 | **CLASSES** |
| 9 | `PZO22001 Starfinder Player Core 030-039::/page/7/Text/86` | 0.385404 | **CLASSES** |
| 10 | `PZO22001 Starfinder Player Core 030-039::/page/5/Text/58` | 0.385404 | **CLASSES** |

### Query 55
- Text: What is the rule about Example Characters?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/1']
- Expected found: `True`
- Expected rank: `4`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 030-039::/page/1/SectionHeader/19', 'PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/17', 'PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/9']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 030-039::/page/1/SectionHeader/19` | 0.837066 | Example Characters |
| 2 | `PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/9` | 0.837066 | Example Characters |
| 3 | `PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/17` | 0.837066 | Example Characters |
| 4 | `PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/1` | 0.807066 | Example Characters |
| 5 | `PZO22001 Starfinder Player Core 030-039::/page/4/SectionHeader/11` | 0.807066 | Example Characters |
| 6 | `PZO22001 Starfinder Player Core 030-039::/page/4/SectionHeader/3` | 0.807066 | Example Characters |
| 7 | `PZO22001 Starfinder Player Core 030-039::/page/3/SectionHeader/22` | 0.807066 | Example Characters |
| 8 | `PZO22001 Starfinder Player Core 030-039::/page/3/SectionHeader/13` | 0.807066 | Example Characters |
| 9 | `PZO22001 Starfinder Player Core 030-039::/page/3/SectionHeader/4` | 0.807066 | Example Characters |
| 10 | `PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/31` | 0.807066 | Example Characters |

### Query 56
- Text: What is the rule about A corporate spy, tasked by a shady megacorp with  infiltrating the cutthroat boardrooms of Bluerise Tower.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/2', 'PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/34', 'PZO22001 Starfinder Player Core 030-039::/page/4/ListItem/12']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/2` | 0.967672 | A corporate spy, tasked by a shady megacorp with  infiltrating the cutthroat boardrooms of Bluerise Tower. |
| 2 | `PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/34` | 0.543920 | A mercenary hired to guard a secret corporate laboratory  who's having second thoughts about the contract. |
| 3 | `PZO22001 Starfinder Player Core 030-039::/page/4/ListItem/12` | 0.529720 | A corporate assassin hired to guard the scion of a  powerful azrinaran dynasty—when you're not spying on  her rivals or sniping your enemies. |
| 4 | `PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/19` | 0.466299 | A hacktivist who exposes corporate conspiracies,  operating out of a dingy cybercafe under a virtual identity. |
| 5 | `PZO22001 Starfinder Player Core 030-039::/page/4/Text/10` | 0.410340 | Regions include Nightarch, a pressurized megacity where  opulent spires tower over air-choked slums, named for the  massive gate leading inside the planet at the center of the  settlement; the Silted |
| 6 | `PZO22001 Starfinder Player Core 030-039::/page/3/ListItem/15` | 0.377184 | A daring ace pilot, flying for fame and fortune on the  payroll of a dragon-owned corporation. |
| 7 | `PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/3` | 0.375000 | A ghost courier, exploring the Ghost Levels on a hunt  for valuable relics, surviving dangerous anomalies and  fighting dimensionally displaced monsters. |
| 8 | `PZO22001 Starfinder Player Core 030-039::/page/4/ListItem/14` | 0.367561 | A plucky smuggler, working to save up enough creds to  pay off your debt to a ruthless azrinaran oligarch so you  can finally buy back your starship. |
| 9 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/25` | 0.364576 | Floating in lost Golarion's empty orbit, this bustling space  station is the center of interstellar trade and governance  in the Pact Worlds. Nobody knows who built Absalom  Station because it appeare |
| 10 | `PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/20` | 0.362273 | An android bounty hunter, pursuing dangerous criminals  and rogue virtual intelligences across the planet. |

### Query 57
- Text: What is the rule about A ghost courier, exploring the Ghost Levels on a hunt  for valuable relics, surviving dangerous anomalies and  fighting dimensionally displaced monsters.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/3']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/3', 'PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/20', 'PZO22001 Starfinder Player Core 030-039::/page/1/ListItem/8']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/3` | 0.923745 | A ghost courier, exploring the Ghost Levels on a hunt  for valuable relics, surviving dangerous anomalies and  fighting dimensionally displaced monsters. |
| 2 | `PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/20` | 0.491836 | An android bounty hunter, pursuing dangerous criminals  and rogue virtual intelligences across the planet. |
| 3 | `PZO22001 Starfinder Player Core 030-039::/page/1/ListItem/8` | 0.487085 | A Starfinder exploring magitech ruins left by the  First Ones, risking encounters with deadly traps and  terrifying sentries. |
| 4 | `PZO22001 Starfinder Player Core 030-039::/page/4/ListItem/13` | 0.437781 | A xenoarchaeologist exploring the planet's hollow interior  and cataloging the strange ruins and dangerous creatures  that lurk within. |
| 5 | `PZO22001 Starfinder Player Core 030-039::/page/7/Text/73` | 0.423759 | **Cleric Spells** 1st: *mindlink*, 3rd: *ghost killer weapon*, 6th:  *vision of death* |
| 6 | `PZO22001 Starfinder Player Core 030-039::/page/0/ListItem/14` | 0.423457 | **The galaxy is dangerous.** Among the planets occupied by  the allied Pact Worlds to Near Space and the remote Vast,  there's usually something causing trouble somewhere.  Adventurers are always seek |
| 7 | `PZO22001 Starfinder Player Core 030-039::/page/3/Text/2` | 0.421327 | In the modern era, bone sages rule scattered fiefdoms  on Eox's irradiated surface, and hordes of mindless undead  wander the wastes outside magical bunkers and walled  necropolises. Many are tragic b |
| 8 | `PZO22001 Starfinder Player Core 030-039::/page/4/ListItem/23` | 0.413508 | A mystic wandering the wastes ravaged by the Shriek,  seeking natural ways to heal your war-torn ancestral lands. |
| 9 | `PZO22001 Starfinder Player Core 030-039::/page/6/Text/36` | 0.410545 | **Cleric Spells** 1st: *ant haul*, 3rd: *insect form*, 5th: *subjective* *reality* |
| 10 | `PZO22001 Starfinder Player Core 030-039::/page/5/Text/23` | 0.409812 | **Anathema** betray shipmates, forsake piracy, settle on a planet **Divine Attribute** Dexterity or Constitution |

### Query 58
- Text: Summarize A solarian disciple, training at the Cosmonastery of the  Empty Orbit.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/4', 'PZO22001 Starfinder Player Core 030-039::/page/9/Text/24', 'PZO22001 Starfinder Player Core 030-039::/page/5/Text/1']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/4` | 1.034835 | A solarian disciple, training at the Cosmonastery of the  Empty Orbit. |
| 2 | `PZO22001 Starfinder Player Core 030-039::/page/9/Text/24` | 0.608502 | ignition and entropy. They believe that the universe was and  will be destroyed and remade by these cosmic forces, and  that this ever-changing duality connects everything in the  universe. Many solar |
| 3 | `PZO22001 Starfinder Player Core 030-039::/page/5/Text/1` | 0.498394 | Technology and scientific knowledge flourish across the galaxy, but these advancements can't  solve every problem or answer all existential questions. Many turn to religion to understand their  place |
| 4 | `PZO22001 Starfinder Player Core 030-039::/page/6/Text/44` | 0.446783 | Ibra is an outer god of cosmic enlightenment, an  inscrutable being seeking to understand the multiverse. |
| 5 | `PZO22001 Starfinder Player Core 030-039::/page/7/Text/54` | 0.434406 | Oras evolved from a single-celled organism  into a deity. It now teaches others to seek personal growth,  prioritize exploration, and unlock their true potential  through science. |
| 6 | `PZO22001 Starfinder Player Core 030-039::/page/9/Text/23` | 0.431166 | Disciples of the Cycle believe that all aspects  of existence follow the endless cosmic cycle of |
| 7 | `PZO22001 Starfinder Player Core 030-039::/page/1/ListItem/10` | 0.406749 | A priest of Triune who travels across the galaxy  installing and repairing Drift beacons, receiving sacred  downloads from Striving's sacred neural network. |
| 8 | `PZO22001 Starfinder Player Core 030-039::/page/2/Text/30` | 0.405896 | The Diaspora is an asteroid belt formed long before the  Gap, when a terrible cataclysm destroyed the twin planets  Damiar and Iovo. The remains of the two destroyed worlds  float among millions of ch |
| 9 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/25` | 0.402904 | Floating in lost Golarion's empty orbit, this bustling space  station is the center of interstellar trade and governance  in the Pact Worlds. Nobody knows who built Absalom  Station because it appeare |
| 10 | `PZO22001 Starfinder Player Core 030-039::/page/6/Text/16` | 0.399206 | Eloritu is a mysterious god who has revealed  secrets of magic and metaphysics to his disciples. |

### Query 59
- Text: Summarize AKITON
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/5', 'PZO22001 Starfinder Player Core 030-039::/page/2/Text/7', 'PZO22001 Starfinder Player Core 030-039::/page/2/Text/8']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/5` | 0.952682 | AKITON |
| 2 | `PZO22001 Starfinder Player Core 030-039::/page/2/Text/7` | 0.571144 | Akiton is a dusty red world of sunbaked deserts, rundown  cities, and rusting scrapyards. It was once a booming industrial  paradise overflowing with wealth earned from mining thasteron,  a starship f |
| 3 | `PZO22001 Starfinder Player Core 030-039::/page/2/Text/8` | 0.436860 | Akiton's regions include Arl, an ancient city infamous for  historical blood sports that still draw crowds; the trench city  Maro with its Thousand Lights; Ka, a mountain peak sacred  to some shobhad |
| 4 | `PZO22001 Starfinder Player Core 030-039::/page/2/Text/23` | 0.338936 | The *Idari* is a world ship built long ago on the world of Kasath  to transport its population away from the dying planet,  toward a desert world kasatha mystics believed was their  promised land: Aki |
| 5 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/5` | 0.312222 | Aballon is a rocky, cratered world of superheated metallic  deserts and deep ice wells. Thousands of years before the  Gap, a mysterious civilization called the First Ones utilized  Aballon's abundant |
| 6 | `PZO22001 Starfinder Player Core 030-039::/page/7/Text/39` | 0.304725 | Aucturn, destroying the planet in the process. |
| 7 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/1` | 0.279439 | The united worlds are Absalom Station, Aballon, Castrovel,  Akiton, Verces, the Diaspora, Eox, Triaxus, Dykon, Kalo-Mahoi,  Marata, Liavara, and Bretheda. The *Idari*—a starship—is counted  among thei |
| 8 | `PZO22001 Starfinder Player Core 030-039::/page/1/SectionHeader/3` | 0.260866 | ABALLON |
| 9 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/6` | 0.257565 | The largest community on Aballon is Striving, an  industrious megacity containing a citywide neural network  sacred to Triune. Other regions include the industrial forgecity Automatrix; the immense, f |
| 10 | `PZO22001 Starfinder Player Core 030-039::/page/8/Text/75` | 0.255868 | Zon-Shelyn is the divine reunion of Shelyn the  Eternal Rose and her estranged brother, the Midnight Lord  Zon-Kuthon. Together, the siblings represent the concepts of  overcoming suffering through ar |

### Query 60
- Text: Summarize **Lonely Red Desert World**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/6', 'PZO22001 Starfinder Player Core 030-039::/page/3/SectionHeader/9', 'PZO22001 Starfinder Player Core 030-039::/page/3/SectionHeader/18']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/6` | 0.996790 | **Lonely Red Desert World** |
| 2 | `PZO22001 Starfinder Player Core 030-039::/page/3/SectionHeader/9` | 0.474706 | **The Dragon Planet** |
| 3 | `PZO22001 Starfinder Player Core 030-039::/page/3/SectionHeader/18` | 0.471400 | **Many-Mooned World of Dreamers** |
| 4 | `PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/29` | 0.393228 | **Belt of Broken Worlds** |
| 5 | `PZO22001 Starfinder Player Core 030-039::/page/2/Text/15` | 0.390059 | Verces is a tidally locked world with a sun-scoured light side,  a frozen dark side, and a belt of opulent cybercities linked by  high-speed bullet trains called the Ring of Nations. The Ring  of Nati |
| 6 | `PZO22001 Starfinder Player Core 030-039::/page/4/SectionHeader/16` | 0.388164 | **Liberated Pahtra Home World** |
| 7 | `PZO22001 Starfinder Player Core 030-039::/page/4/SectionHeader/8` | 0.386248 | **Dungeon Planet** |
| 8 | `PZO22001 Starfinder Player Core 030-039::/page/2/Text/7` | 0.385235 | Akiton is a dusty red world of sunbaked deserts, rundown  cities, and rusting scrapyards. It was once a booming industrial  paradise overflowing with wealth earned from mining thasteron,  a starship f |
| 9 | `PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/36` | 0.384080 | **Planet of the Dead** |
| 10 | `PZO22001 Starfinder Player Core 030-039::/page/4/Text/19` | 0.371979 | Regions include Voyedris, a treacherous wilderness  ravaged by rapid industrialization; Hafrerren, a rebel nationstate known for biotech research; Rafemii, a hub for magical  and spiritual development |

### Query 61
- Text: What is the rule about Akiton is a dusty red world of sunbaked deserts, rundown  cities, and rusting scrapyards. It was once a booming industrial  paradise overflowing with wealth earned from mining thasteron,  a starship fuel that fell out of favor after the discovery of  hyperspace. Now, Akiton is a decadent battlefield where  corporate lynchpins and crime families fight to return to their  former glory days while everyday people struggle to get by.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 030-039::/page/2/Text/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 030-039::/page/2/Text/7', 'PZO22001 Starfinder Player Core 030-039::/page/2/Text/8', 'PZO22001 Starfinder Player Core 030-039::/page/2/Text/23']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 030-039::/page/2/Text/7` | 0.998759 | Akiton is a dusty red world of sunbaked deserts, rundown  cities, and rusting scrapyards. It was once a booming industrial  paradise overflowing with wealth earned from mining thasteron,  a starship f |
| 2 | `PZO22001 Starfinder Player Core 030-039::/page/2/Text/8` | 0.636991 | Akiton's regions include Arl, an ancient city infamous for  historical blood sports that still draw crowds; the trench city  Maro with its Thousand Lights; Ka, a mountain peak sacred  to some shobhad |
| 3 | `PZO22001 Starfinder Player Core 030-039::/page/2/Text/23` | 0.576557 | The *Idari* is a world ship built long ago on the world of Kasath  to transport its population away from the dying planet,  toward a desert world kasatha mystics believed was their  promised land: Aki |
| 4 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/5` | 0.526016 | Aballon is a rocky, cratered world of superheated metallic  deserts and deep ice wells. Thousands of years before the  Gap, a mysterious civilization called the First Ones utilized  Aballon's abundant |
| 5 | `PZO22001 Starfinder Player Core 030-039::/page/4/Text/10` | 0.511782 | Regions include Nightarch, a pressurized megacity where  opulent spires tower over air-choked slums, named for the  massive gate leading inside the planet at the center of the  settlement; the Silted |
| 6 | `PZO22001 Starfinder Player Core 030-039::/page/4/Text/19` | 0.502535 | Regions include Voyedris, a treacherous wilderness  ravaged by rapid industrialization; Hafrerren, a rebel nationstate known for biotech research; Rafemii, a hub for magical  and spiritual development |
| 7 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/25` | 0.502160 | Floating in lost Golarion's empty orbit, this bustling space  station is the center of interstellar trade and governance  in the Pact Worlds. Nobody knows who built Absalom  Station because it appeare |
| 8 | `PZO22001 Starfinder Player Core 030-039::/page/3/Text/29` | 0.494683 | Bretheda's violent storms make most of its gaseous layers  unlivable. The planet's largest city is Trillidiem, a domed,  industrial arcology governed by Confluence, a union of many  merged barathus. B |
| 9 | `PZO22001 Starfinder Player Core 030-039::/page/4/Text/9` | 0.489114 | Apostae is a hollow planetoid with no atmosphere and few  resources. Mysterious gateways on the planet's rocky surface  access a network of tunnels, magitech chambers, and caverns  inside its core. Th |
| 10 | `PZO22001 Starfinder Player Core 030-039::/page/2/Text/16` | 0.487185 | Major locations on Verces include the Ring of Nations,  a band of sprawling megacities inhabited by augmented  verthani, androids, and many others; Skydock, modern  shipyards built atop an ancient spa |

### Query 62
- Text: What is the rule about Akiton's regions include Arl, an ancient city infamous for  historical blood sports that still draw crowds; the trench city  Maro with its Thousand Lights; Ka, a mountain peak sacred  to some shobhad communities that cradles the bustling  Hivemarket at its base; Khefak Depot, a junker town and  tourist hotspot; the rocky Sloughscar Hills, crash site of the  Wreck of the Returned; and the icy polar Winterlands. A few  contemplative communes thrive underground, remaining  aloof from current events while closely monitoring Akiton's  geological, meteorological, and political conditions.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 030-039::/page/2/Text/8']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 030-039::/page/2/Text/8', 'PZO22001 Starfinder Player Core 030-039::/page/2/Text/7', 'PZO22001 Starfinder Player Core 030-039::/page/1/Text/14']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 030-039::/page/2/Text/8` | 1.003958 | Akiton's regions include Arl, an ancient city infamous for  historical blood sports that still draw crowds; the trench city  Maro with its Thousand Lights; Ka, a mountain peak sacred  to some shobhad |
| 2 | `PZO22001 Starfinder Player Core 030-039::/page/2/Text/7` | 0.650495 | Akiton is a dusty red world of sunbaked deserts, rundown  cities, and rusting scrapyards. It was once a booming industrial  paradise overflowing with wealth earned from mining thasteron,  a starship f |
| 3 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/14` | 0.597329 | Castrovel's regions include Asana and its major spaceport  Qabarat, a beautiful living monument of ancient walls of  crushed shells cradling a modern metropolis; the towering  hive-city of Queensrock |
| 4 | `PZO22001 Starfinder Player Core 030-039::/page/4/Text/19` | 0.517622 | Regions include Voyedris, a treacherous wilderness  ravaged by rapid industrialization; Hafrerren, a rebel nationstate known for biotech research; Rafemii, a hub for magical  and spiritual development |
| 5 | `PZO22001 Starfinder Player Core 030-039::/page/3/Text/29` | 0.501559 | Bretheda's violent storms make most of its gaseous layers  unlivable. The planet's largest city is Trillidiem, a domed,  industrial arcology governed by Confluence, a union of many  merged barathus. B |
| 6 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/6` | 0.494335 | The largest community on Aballon is Striving, an  industrious megacity containing a citywide neural network  sacred to Triune. Other regions include the industrial forgecity Automatrix; the immense, f |
| 7 | `PZO22001 Starfinder Player Core 030-039::/page/4/Text/29` | 0.489487 | Regions of the Vast include the Azlanti Star Empire, a vast  territory of unknown size controlled by a colonizing regime  ruled by the descendants of a human nation from lost Golarion;  Kazmurg's Absu |
| 8 | `PZO22001 Starfinder Player Core 030-039::/page/3/Text/21` | 0.484133 | Regions include Roselight, a cloud of floating domes built  by barathu architects, and Deep Station, a research outpost  submerged in Liavara's alien seas. Liavara has many moons:  Hallas, a warded pr |
| 9 | `PZO22001 Starfinder Player Core 030-039::/page/4/Text/10` | 0.473688 | Regions include Nightarch, a pressurized megacity where  opulent spires tower over air-choked slums, named for the  massive gate leading inside the planet at the center of the  settlement; the Silted |
| 10 | `PZO22001 Starfinder Player Core 030-039::/page/2/Text/16` | 0.464351 | Major locations on Verces include the Ring of Nations,  a band of sprawling megacities inhabited by augmented  verthani, androids, and many others; Skydock, modern  shipyards built atop an ancient spa |

### Query 63
- Text: What is the rule about Example Characters?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/9']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 030-039::/page/1/SectionHeader/19', 'PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/17', 'PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/9']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 030-039::/page/1/SectionHeader/19` | 0.837066 | Example Characters |
| 2 | `PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/9` | 0.837066 | Example Characters |
| 3 | `PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/17` | 0.837066 | Example Characters |
| 4 | `PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/1` | 0.807066 | Example Characters |
| 5 | `PZO22001 Starfinder Player Core 030-039::/page/4/SectionHeader/11` | 0.807066 | Example Characters |
| 6 | `PZO22001 Starfinder Player Core 030-039::/page/4/SectionHeader/3` | 0.807066 | Example Characters |
| 7 | `PZO22001 Starfinder Player Core 030-039::/page/3/SectionHeader/22` | 0.807066 | Example Characters |
| 8 | `PZO22001 Starfinder Player Core 030-039::/page/3/SectionHeader/13` | 0.807066 | Example Characters |
| 9 | `PZO22001 Starfinder Player Core 030-039::/page/3/SectionHeader/4` | 0.807066 | Example Characters |
| 10 | `PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/31` | 0.807066 | Example Characters |

### Query 64
- Text: Summarize An eccentric junker, salvaging treasures from the  scrapheaps of Khefak Depot and looking for a way out.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/10', 'PZO22001 Starfinder Player Core 030-039::/page/4/ListItem/23', 'PZO22001 Starfinder Player Core 030-039::/page/4/ListItem/14']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/10` | 1.033954 | An eccentric junker, salvaging treasures from the  scrapheaps of Khefak Depot and looking for a way out. |
| 2 | `PZO22001 Starfinder Player Core 030-039::/page/4/ListItem/23` | 0.573548 | A mystic wandering the wastes ravaged by the Shriek,  seeking natural ways to heal your war-torn ancestral lands. |
| 3 | `PZO22001 Starfinder Player Core 030-039::/page/4/ListItem/14` | 0.539812 | A plucky smuggler, working to save up enough creds to  pay off your debt to a ruthless azrinaran oligarch so you  can finally buy back your starship. |
| 4 | `PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/3` | 0.461956 | A ghost courier, exploring the Ghost Levels on a hunt  for valuable relics, surviving dangerous anomalies and  fighting dimensionally displaced monsters. |
| 5 | `PZO22001 Starfinder Player Core 030-039::/page/2/Text/8` | 0.458255 | Akiton's regions include Arl, an ancient city infamous for  historical blood sports that still draw crowds; the trench city  Maro with its Thousand Lights; Ka, a mountain peak sacred  to some shobhad |
| 6 | `PZO22001 Starfinder Player Core 030-039::/page/3/ListItem/24` | 0.455572 | A shirren devotee of Hylax, leaving Nchak on a sacred  mission. |
| 7 | `PZO22001 Starfinder Player Core 030-039::/page/4/ListItem/13` | 0.427796 | A xenoarchaeologist exploring the planet's hollow interior  and cataloging the strange ruins and dangerous creatures  that lurk within. |
| 8 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/2` | 0.423268 | What's left of Aucturn, a planet destroyed by the birth of  a god, floats among the field of ice and haunted space junk  ringing the system's outskirts, called the Gelid Edge. |
| 9 | `PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/11` | 0.417454 | A reckless gladiator, battling ferocious beasts and  cunning opponents for glory and riches in the dusty  arenas of Arl. |
| 10 | `PZO22001 Starfinder Player Core 030-039::/page/3/ListItem/7` | 0.414204 | A xenoarchaeologist studying the ruins beneath  Murthal, dodging ancient traps and uncovering relics  deep within its forgotten tombs. |

### Query 65
- Text: Summarize A reckless gladiator, battling ferocious beasts and  cunning opponents for glory and riches in the dusty  arenas of Arl.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/11', 'PZO22001 Starfinder Player Core 030-039::/page/3/ListItem/16', 'PZO22001 Starfinder Player Core 030-039::/page/1/ListItem/22']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/11` | 1.033736 | A reckless gladiator, battling ferocious beasts and  cunning opponents for glory and riches in the dusty  arenas of Arl. |
| 2 | `PZO22001 Starfinder Player Core 030-039::/page/3/ListItem/16` | 0.494329 | A battleflower, a painted ritual warrior who treats  fighting as an art form. |
| 3 | `PZO22001 Starfinder Player Core 030-039::/page/1/ListItem/22` | 0.474279 | A brave formian hive guard battling the twisted husks  that have emerged from underground to attack your  community. |
| 4 | `PZO22001 Starfinder Player Core 030-039::/page/9/Text/19` | 0.426329 | Different battle saints represent every struggle, from  treating chronic illness to moving up the corporate ladder.  Some aren't vesk, like Apna the brave skittermander, whose  legendary helpfulness m |
| 5 | `PZO22001 Starfinder Player Core 030-039::/page/2/Text/8` | 0.424688 | Akiton's regions include Arl, an ancient city infamous for  historical blood sports that still draw crowds; the trench city  Maro with its Thousand Lights; Ka, a mountain peak sacred  to some shobhad |
| 6 | `PZO22001 Starfinder Player Core 030-039::/page/4/ListItem/12` | 0.424409 | A corporate assassin hired to guard the scion of a  powerful azrinaran dynasty—when you're not spying on  her rivals or sniping your enemies. |
| 7 | `PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/3` | 0.412908 | A ghost courier, exploring the Ghost Levels on a hunt  for valuable relics, surviving dangerous anomalies and  fighting dimensionally displaced monsters. |
| 8 | `PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/10` | 0.410084 | An eccentric junker, salvaging treasures from the  scrapheaps of Khefak Depot and looking for a way out. |
| 9 | `PZO22001 Starfinder Player Core 030-039::/page/4/Text/29` | 0.394322 | Regions of the Vast include the Azlanti Star Empire, a vast  territory of unknown size controlled by a colonizing regime  ruled by the descendants of a human nation from lost Golarion;  Kazmurg's Absu |
| 10 | `PZO22001 Starfinder Player Core 030-039::/page/3/ListItem/15` | 0.388152 | A daring ace pilot, flying for fame and fortune on the  payroll of a dragon-owned corporation. |

### Query 66
- Text: Summarize A curious contemplative, recording every detail  observed while exploring the Wreck of the Returned.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/12']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/12', 'PZO22001 Starfinder Player Core 030-039::/page/3/ListItem/7', 'PZO22001 Starfinder Player Core 030-039::/page/4/ListItem/13']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/12` | 1.027305 | A curious contemplative, recording every detail  observed while exploring the Wreck of the Returned. |
| 2 | `PZO22001 Starfinder Player Core 030-039::/page/3/ListItem/7` | 0.476482 | A xenoarchaeologist studying the ruins beneath  Murthal, dodging ancient traps and uncovering relics  deep within its forgotten tombs. |
| 3 | `PZO22001 Starfinder Player Core 030-039::/page/4/ListItem/13` | 0.456904 | A xenoarchaeologist exploring the planet's hollow interior  and cataloging the strange ruins and dangerous creatures  that lurk within. |
| 4 | `PZO22001 Starfinder Player Core 030-039::/page/4/ListItem/23` | 0.412318 | A mystic wandering the wastes ravaged by the Shriek,  seeking natural ways to heal your war-torn ancestral lands. |
| 5 | `PZO22001 Starfinder Player Core 030-039::/page/1/ListItem/10` | 0.407922 | A priest of Triune who travels across the galaxy  installing and repairing Drift beacons, receiving sacred  downloads from Striving's sacred neural network. |
| 6 | `PZO22001 Starfinder Player Core 030-039::/page/3/ListItem/24` | 0.400163 | A shirren devotee of Hylax, leaving Nchak on a sacred  mission. |
| 7 | `PZO22001 Starfinder Player Core 030-039::/page/3/ListItem/23` | 0.396133 | A dream prophet, investigating the cause of the  dreamers' troubling behavior. |
| 8 | `PZO22001 Starfinder Player Core 030-039::/page/8/Text/46` | 0.393345 | Weydan enjoys discovery and exploration with  a purpose. He believes everyone deserves the equal right  to pursue such experiences and walks the galaxy in diverse  avatars to commune with his follower |
| 9 | `PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/3` | 0.381949 | A ghost courier, exploring the Ghost Levels on a hunt  for valuable relics, surviving dangerous anomalies and  fighting dimensionally displaced monsters. |
| 10 | `PZO22001 Starfinder Player Core 030-039::/page/3/Text/2` | 0.373296 | In the modern era, bone sages rule scattered fiefdoms  on Eox's irradiated surface, and hordes of mindless undead  wander the wastes outside magical bunkers and walled  necropolises. Many are tragic b |

### Query 67
- Text: Summarize VERCES
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/13', 'PZO22001 Starfinder Player Core 030-039::/page/2/Text/16', 'PZO22001 Starfinder Player Core 030-039::/page/2/Text/15']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/13` | 0.860253 | VERCES |
| 2 | `PZO22001 Starfinder Player Core 030-039::/page/2/Text/16` | 0.504465 | Major locations on Verces include the Ring of Nations,  a band of sprawling megacities inhabited by augmented  verthani, androids, and many others; Skydock, modern  shipyards built atop an ancient spa |
| 3 | `PZO22001 Starfinder Player Core 030-039::/page/2/Text/15` | 0.478117 | Verces is a tidally locked world with a sun-scoured light side,  a frozen dark side, and a belt of opulent cybercities linked by  high-speed bullet trains called the Ring of Nations. The Ring  of Nati |
| 4 | `PZO22001 Starfinder Player Core 030-039::/page/4/SectionHeader/27` | 0.311236 | THE VAST |
| 5 | `PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/17` | 0.293117 | Example Characters |
| 6 | `PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/1` | 0.281117 | Example Characters |
| 7 | `PZO22001 Starfinder Player Core 030-039::/page/1/SectionHeader/7` | 0.281117 | Example Characters |
| 8 | `PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/9` | 0.281117 | Example Characters |
| 9 | `PZO22001 Starfinder Player Core 030-039::/page/1/SectionHeader/19` | 0.281117 | Example Characters |
| 10 | `PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/24` | 0.281117 | Example Characters |

### Query 68
- Text: Summarize **Expanse of Twilight Cybercities**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/14']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/14', 'PZO22001 Starfinder Player Core 030-039::/page/2/Text/16', 'PZO22001 Starfinder Player Core 030-039::/page/2/Text/15']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/14` | 1.012271 | **Expanse of Twilight Cybercities** |
| 2 | `PZO22001 Starfinder Player Core 030-039::/page/2/Text/16` | 0.478442 | Major locations on Verces include the Ring of Nations,  a band of sprawling megacities inhabited by augmented  verthani, androids, and many others; Skydock, modern  shipyards built atop an ancient spa |
| 3 | `PZO22001 Starfinder Player Core 030-039::/page/2/Text/15` | 0.433989 | Verces is a tidally locked world with a sun-scoured light side,  a frozen dark side, and a belt of opulent cybercities linked by  high-speed bullet trains called the Ring of Nations. The Ring  of Nati |
| 4 | `PZO22001 Starfinder Player Core 030-039::/page/5/Text/8` | 0.387925 | **Areas of Concern **cities, law, corporations, wealth |
| 5 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/6` | 0.381693 | The largest community on Aballon is Striving, an  industrious megacity containing a citywide neural network  sacred to Triune. Other regions include the industrial forgecity Automatrix; the immense, f |
| 6 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/18` | 0.370351 | spires of Sovyrian, a nation of surrealist cities sculpted  by elven magic. Castrovel's wilds are virtually unspoiled  because the planet's industry occurs on the super-polluted  moon Elindrae. |
| 7 | `PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/19` | 0.369328 | A hacktivist who exposes corporate conspiracies,  operating out of a dingy cybercafe under a virtual identity. |
| 8 | `PZO22001 Starfinder Player Core 030-039::/page/5/Text/21` | 0.363853 | **Areas of Concern **piracy, space monsters, strife |
| 9 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/13` | 0.362760 | Castrovel is a pristine jungle planet where thriving  metropolises coexist in harmony with nature. Magical  gateways called *aiudara* connect Castrovel's cities, which  are governed by a planetary fed |
| 10 | `PZO22001 Starfinder Player Core 030-039::/page/1/ListItem/21` | 0.359692 | A young elf ambassador experiencing life outside their  walled ancestral city for the first time. |

### Query 69
- Text: Summarize Verces is a tidally locked world with a sun-scoured light side,  a frozen dark side, and a belt of opulent cybercities linked by  high-speed bullet trains called the Ring of Nations. The Ring  of Nations is governed by a representative Grand Assembly,  while frontier outposts and bandit camps struggle to survive  outside its borders.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 030-039::/page/2/Text/15']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 030-039::/page/2/Text/15', 'PZO22001 Starfinder Player Core 030-039::/page/2/Text/16', 'PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/13']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 030-039::/page/2/Text/15` | 1.038845 | Verces is a tidally locked world with a sun-scoured light side,  a frozen dark side, and a belt of opulent cybercities linked by  high-speed bullet trains called the Ring of Nations. The Ring  of Nati |
| 2 | `PZO22001 Starfinder Player Core 030-039::/page/2/Text/16` | 0.835141 | Major locations on Verces include the Ring of Nations,  a band of sprawling megacities inhabited by augmented  verthani, androids, and many others; Skydock, modern  shipyards built atop an ancient spa |
| 3 | `PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/13` | 0.554615 | VERCES |
| 4 | `PZO22001 Starfinder Player Core 030-039::/page/4/Text/10` | 0.498885 | Regions include Nightarch, a pressurized megacity where  opulent spires tower over air-choked slums, named for the  massive gate leading inside the planet at the center of the  settlement; the Silted |
| 5 | `PZO22001 Starfinder Player Core 030-039::/page/4/Text/19` | 0.498335 | Regions include Voyedris, a treacherous wilderness  ravaged by rapid industrialization; Hafrerren, a rebel nationstate known for biotech research; Rafemii, a hub for magical  and spiritual development |
| 6 | `PZO22001 Starfinder Player Core 030-039::/page/4/Text/29` | 0.493347 | Regions of the Vast include the Azlanti Star Empire, a vast  territory of unknown size controlled by a colonizing regime  ruled by the descendants of a human nation from lost Golarion;  Kazmurg's Absu |
| 7 | `PZO22001 Starfinder Player Core 030-039::/page/4/Text/28` | 0.493307 | The dangerous, infrequently traveled outskirts of the galaxy  and the endless sprawl of uncharted space beyond are called  the Vast. Only a handful of scattered Drift beacons exist to  guide ships thr |
| 8 | `PZO22001 Starfinder Player Core 030-039::/page/2/Text/30` | 0.480506 | The Diaspora is an asteroid belt formed long before the  Gap, when a terrible cataclysm destroyed the twin planets  Damiar and Iovo. The remains of the two destroyed worlds  float among millions of ch |
| 9 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/5` | 0.476600 | Aballon is a rocky, cratered world of superheated metallic  deserts and deep ice wells. Thousands of years before the  Gap, a mysterious civilization called the First Ones utilized  Aballon's abundant |
| 10 | `PZO22001 Starfinder Player Core 030-039::/page/3/Text/12` | 0.471153 | Regions on Triaxus include the Drakelands, a continental  wilderness preserve tended by dragons; the Skyfire Mandate,  an isthmus guarded by the oldest aeries of the Skyfire Legion;  the Allied Territ |

### Query 70
- Text: What is the rule about Major locations on Verces include the Ring of Nations,  a band of sprawling megacities inhabited by augmented  verthani, androids, and many others; Skydock, modern  shipyards built atop an ancient space platform; Fullbright, a  burning desert of corporate solar farms and fringe Outlaw  Kingdoms; and Darkside, a frozen landscape of ice mines and  howling tundra stalked by terrible beasts.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 030-039::/page/2/Text/16']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 030-039::/page/2/Text/16', 'PZO22001 Starfinder Player Core 030-039::/page/2/Text/15', 'PZO22001 Starfinder Player Core 030-039::/page/4/Text/10']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 030-039::/page/2/Text/16` | 0.959462 | Major locations on Verces include the Ring of Nations,  a band of sprawling megacities inhabited by augmented  verthani, androids, and many others; Skydock, modern  shipyards built atop an ancient spa |
| 2 | `PZO22001 Starfinder Player Core 030-039::/page/2/Text/15` | 0.750183 | Verces is a tidally locked world with a sun-scoured light side,  a frozen dark side, and a belt of opulent cybercities linked by  high-speed bullet trains called the Ring of Nations. The Ring  of Nati |
| 3 | `PZO22001 Starfinder Player Core 030-039::/page/4/Text/10` | 0.587026 | Regions include Nightarch, a pressurized megacity where  opulent spires tower over air-choked slums, named for the  massive gate leading inside the planet at the center of the  settlement; the Silted |
| 4 | `PZO22001 Starfinder Player Core 030-039::/page/3/Text/12` | 0.531142 | Regions on Triaxus include the Drakelands, a continental  wilderness preserve tended by dragons; the Skyfire Mandate,  an isthmus guarded by the oldest aeries of the Skyfire Legion;  the Allied Territ |
| 5 | `PZO22001 Starfinder Player Core 030-039::/page/4/Text/19` | 0.528122 | Regions include Voyedris, a treacherous wilderness  ravaged by rapid industrialization; Hafrerren, a rebel nationstate known for biotech research; Rafemii, a hub for magical  and spiritual development |
| 6 | `PZO22001 Starfinder Player Core 030-039::/page/4/Text/29` | 0.525775 | Regions of the Vast include the Azlanti Star Empire, a vast  territory of unknown size controlled by a colonizing regime  ruled by the descendants of a human nation from lost Golarion;  Kazmurg's Absu |
| 7 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/6` | 0.520933 | The largest community on Aballon is Striving, an  industrious megacity containing a citywide neural network  sacred to Triune. Other regions include the industrial forgecity Automatrix; the immense, f |
| 8 | `PZO22001 Starfinder Player Core 030-039::/page/4/Text/26` | 0.494962 | Near Space regions include the Veskarium, an empire of  seven conquered planets and a few dozen colonies ruled  by vesk military leaders; the Marixah Republic, a group of  allied planets emerging onto |
| 9 | `PZO22001 Starfinder Player Core 030-039::/page/3/Text/21` | 0.489003 | Regions include Roselight, a cloud of floating domes built  by barathu architects, and Deep Station, a research outpost  submerged in Liavara's alien seas. Liavara has many moons:  Hallas, a warded pr |
| 10 | `PZO22001 Starfinder Player Core 030-039::/page/4/Text/28` | 0.476301 | The dangerous, infrequently traveled outskirts of the galaxy  and the endless sprawl of uncharted space beyond are called  the Vast. Only a handful of scattered Drift beacons exist to  guide ships thr |

### Query 71
- Text: What is the rule about Example Characters?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/17']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 030-039::/page/1/SectionHeader/19', 'PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/17', 'PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/9']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 030-039::/page/1/SectionHeader/19` | 0.837066 | Example Characters |
| 2 | `PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/9` | 0.837066 | Example Characters |
| 3 | `PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/17` | 0.837066 | Example Characters |
| 4 | `PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/1` | 0.807066 | Example Characters |
| 5 | `PZO22001 Starfinder Player Core 030-039::/page/4/SectionHeader/11` | 0.807066 | Example Characters |
| 6 | `PZO22001 Starfinder Player Core 030-039::/page/4/SectionHeader/3` | 0.807066 | Example Characters |
| 7 | `PZO22001 Starfinder Player Core 030-039::/page/3/SectionHeader/22` | 0.807066 | Example Characters |
| 8 | `PZO22001 Starfinder Player Core 030-039::/page/3/SectionHeader/13` | 0.807066 | Example Characters |
| 9 | `PZO22001 Starfinder Player Core 030-039::/page/3/SectionHeader/4` | 0.807066 | Example Characters |
| 10 | `PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/31` | 0.807066 | Example Characters |

### Query 72
- Text: Summarize • An augmented entertainer, transforming yourself into  living art.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 030-039::/page/2/Text/18']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 030-039::/page/2/Text/18', 'PZO22001 Starfinder Player Core 030-039::/page/4/ListItem/4', 'PZO22001 Starfinder Player Core 030-039::/page/3/ListItem/6']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 030-039::/page/2/Text/18` | 1.022537 | • An augmented entertainer, transforming yourself into  living art. |
| 2 | `PZO22001 Starfinder Player Core 030-039::/page/4/ListItem/4` | 0.490908 | A barathu scientist, pushing nature's boundaries by  transforming your own body into a marvel of biotech. |
| 3 | `PZO22001 Starfinder Player Core 030-039::/page/3/ListItem/6` | 0.459513 | A living necromancer, building up political clout and  magical power with the goal of becoming a bone sage. |
| 4 | `PZO22001 Starfinder Player Core 030-039::/page/3/ListItem/5` | 0.386792 | A reality show survivor who escaped the Halls of the  Living but is still bound by a predatory media contract. |
| 5 | `PZO22001 Starfinder Player Core 030-039::/page/8/Text/77` | 0.386400 | **Edicts** channel your pain into art, seek beauty in all places,  express yourself creatively according to your own aesthetics |
| 6 | `PZO22001 Starfinder Player Core 030-039::/page/8/Text/78` | 0.382660 | **Anathema** suffer in silence, destroy or copy another's creative  works, conform to society's beauty standards |
| 7 | `PZO22001 Starfinder Player Core 030-039::/page/4/ListItem/22` | 0.375707 | A famous pop star navigating the glitzy social scene in  Starlance—the high life isn't always as plush as it looks! |
| 8 | `PZO22001 Starfinder Player Core 030-039::/page/8/Text/19` | 0.373521 | **Anathema** treat artificial life as inferior to organic life,  subjugate artificial life-forms, destroy a Drift beacon |
| 9 | `PZO22001 Starfinder Player Core 030-039::/page/7/Text/26` | 0.371985 | She empowers her followers to fight oppression, create art,  and live free. |
| 10 | `PZO22001 Starfinder Player Core 030-039::/page/4/ListItem/5` | 0.369436 | A kalo fashionista, traveling the galaxy and discovering  alien trends to inspire your personal style. |

### Query 73
- Text: What is the rule about A hacktivist who exposes corporate conspiracies,  operating out of a dingy cybercafe under a virtual identity.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/19']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/19', 'PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/2', 'PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/20']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/19` | 0.934105 | A hacktivist who exposes corporate conspiracies,  operating out of a dingy cybercafe under a virtual identity. |
| 2 | `PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/2` | 0.485662 | A corporate spy, tasked by a shady megacorp with  infiltrating the cutthroat boardrooms of Bluerise Tower. |
| 3 | `PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/20` | 0.461847 | An android bounty hunter, pursuing dangerous criminals  and rogue virtual intelligences across the planet. |
| 4 | `PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/34` | 0.392651 | A mercenary hired to guard a secret corporate laboratory  who's having second thoughts about the contract. |
| 5 | `PZO22001 Starfinder Player Core 030-039::/page/4/ListItem/12` | 0.391963 | A corporate assassin hired to guard the scion of a  powerful azrinaran dynasty—when you're not spying on  her rivals or sniping your enemies. |
| 6 | `PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/14` | 0.377076 | **Expanse of Twilight Cybercities** |
| 7 | `PZO22001 Starfinder Player Core 030-039::/page/5/Text/23` | 0.364003 | **Anathema** betray shipmates, forsake piracy, settle on a planet **Divine Attribute** Dexterity or Constitution |
| 8 | `PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/3` | 0.363975 | A ghost courier, exploring the Ghost Levels on a hunt  for valuable relics, surviving dangerous anomalies and  fighting dimensionally displaced monsters. |
| 9 | `PZO22001 Starfinder Player Core 030-039::/page/5/Text/10` | 0.351413 | **Anathema** engage in banditry or piracy, steal, undermine a  law-abiding court |
| 10 | `PZO22001 Starfinder Player Core 030-039::/page/0/Text/11` | 0.346091 | Most people learn the basics of how to use tech in  school or on the job. People communicate with each  other instantaneously using comm units and the  infosphere, a virtual network connecting a world |

### Query 74
- Text: What is the rule about An android bounty hunter, pursuing dangerous criminals  and rogue virtual intelligences across the planet.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/20']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/20', 'PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/3', 'PZO22001 Starfinder Player Core 030-039::/page/0/ListItem/14']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/20` | 0.949164 | An android bounty hunter, pursuing dangerous criminals  and rogue virtual intelligences across the planet. |
| 2 | `PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/3` | 0.504998 | A ghost courier, exploring the Ghost Levels on a hunt  for valuable relics, surviving dangerous anomalies and  fighting dimensionally displaced monsters. |
| 3 | `PZO22001 Starfinder Player Core 030-039::/page/0/ListItem/14` | 0.466123 | **The galaxy is dangerous.** Among the planets occupied by  the allied Pact Worlds to Near Space and the remote Vast,  there's usually something causing trouble somewhere.  Adventurers are always seek |
| 4 | `PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/19` | 0.422591 | A hacktivist who exposes corporate conspiracies,  operating out of a dingy cybercafe under a virtual identity. |
| 5 | `PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/27` | 0.405631 | A restless engineer who's bored with the *Idari*'s  predictable orbit and ancient schematics. |
| 6 | `PZO22001 Starfinder Player Core 030-039::/page/0/Text/4` | 0.394376 | The Starfinder Roleplaying Game rules come with their own  default setting: the galaxy known as Desna's Path. The galaxy  is full of wonder and peril, advanced technology, magic,  meddling deities, an |
| 7 | `PZO22001 Starfinder Player Core 030-039::/page/4/ListItem/13` | 0.393433 | A xenoarchaeologist exploring the planet's hollow interior  and cataloging the strange ruins and dangerous creatures  that lurk within. |
| 8 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/5` | 0.390763 | Aballon is a rocky, cratered world of superheated metallic  deserts and deep ice wells. Thousands of years before the  Gap, a mysterious civilization called the First Ones utilized  Aballon's abundant |
| 9 | `PZO22001 Starfinder Player Core 030-039::/page/1/ListItem/8` | 0.389378 | A Starfinder exploring magitech ruins left by the  First Ones, risking encounters with deadly traps and  terrifying sentries. |
| 10 | `PZO22001 Starfinder Player Core 030-039::/page/5/Text/23` | 0.388580 | **Anathema** betray shipmates, forsake piracy, settle on a planet **Divine Attribute** Dexterity or Constitution |

### Query 75
- Text: Summarize THE IDARI
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/21']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/21', 'PZO22001 Starfinder Player Core 030-039::/page/2/Text/23', 'PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/27']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/21` | 0.968380 | THE IDARI |
| 2 | `PZO22001 Starfinder Player Core 030-039::/page/2/Text/23` | 0.602377 | The *Idari* is a world ship built long ago on the world of Kasath  to transport its population away from the dying planet,  toward a desert world kasatha mystics believed was their  promised land: Aki |
| 3 | `PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/27` | 0.574169 | A restless engineer who's bored with the *Idari*'s  predictable orbit and ancient schematics. |
| 4 | `PZO22001 Starfinder Player Core 030-039::/page/5/SectionHeader/5` | 0.371645 | ABADAR |
| 5 | `PZO22001 Starfinder Player Core 030-039::/page/6/Text/44` | 0.363441 | Ibra is an outer god of cosmic enlightenment, an  inscrutable being seeking to understand the multiverse. |
| 6 | `PZO22001 Starfinder Player Core 030-039::/page/6/SectionHeader/42` | 0.349585 | IBRA |
| 7 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/1` | 0.349147 | The united worlds are Absalom Station, Aballon, Castrovel,  Akiton, Verces, the Diaspora, Eox, Triaxus, Dykon, Kalo-Mahoi,  Marata, Liavara, and Bretheda. The *Idari*—a starship—is counted  among thei |
| 8 | `PZO22001 Starfinder Player Core 030-039::/page/5/Text/7` | 0.327464 | Abadar brings civilization to uninhabited worlds,  promotes law, and encourages commerce and trade between  cultures. |
| 9 | `PZO22001 Starfinder Player Core 030-039::/page/2/Text/30` | 0.326471 | The Diaspora is an asteroid belt formed long before the  Gap, when a terrible cataclysm destroyed the twin planets  Damiar and Iovo. The remains of the two destroyed worlds  float among millions of ch |
| 10 | `PZO22001 Starfinder Player Core 030-039::/page/3/Text/19` | 0.321063 | Liavara is a peach-colored gas giant encircled by dust  rings and many shepherd moons. In Liavara's upper  atmosphere, elegant arcologies float through swirling  skies; deeper down, piscine titans swi |

### Query 76
- Text: Summarize **Kasatha World Ship**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/22']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/22', 'PZO22001 Starfinder Player Core 030-039::/page/2/Text/23', 'PZO22001 Starfinder Player Core 030-039::/page/5/Text/20']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/22` | 1.013173 | **Kasatha World Ship** |
| 2 | `PZO22001 Starfinder Player Core 030-039::/page/2/Text/23` | 0.575236 | The *Idari* is a world ship built long ago on the world of Kasath  to transport its population away from the dying planet,  toward a desert world kasatha mystics believed was their  promised land: Aki |
| 3 | `PZO22001 Starfinder Player Core 030-039::/page/5/Text/20` | 0.481293 | Besmara is worshipped by pirate crews in  shipping lanes across the galaxy. |
| 4 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/1` | 0.415991 | The united worlds are Absalom Station, Aballon, Castrovel,  Akiton, Verces, the Diaspora, Eox, Triaxus, Dykon, Kalo-Mahoi,  Marata, Liavara, and Bretheda. The *Idari*—a starship—is counted  among thei |
| 5 | `PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/26` | 0.412048 | A young kasatha who's decided not to return from your  Tempering, joining a touring Driftwave band instead. |
| 6 | `PZO22001 Starfinder Player Core 030-039::/page/4/Text/9` | 0.393288 | Apostae is a hollow planetoid with no atmosphere and few  resources. Mysterious gateways on the planet's rocky surface  access a network of tunnels, magitech chambers, and caverns  inside its core. Th |
| 7 | `PZO22001 Starfinder Player Core 030-039::/page/5/Text/23` | 0.391797 | **Anathema** betray shipmates, forsake piracy, settle on a planet **Divine Attribute** Dexterity or Constitution |
| 8 | `PZO22001 Starfinder Player Core 030-039::/page/0/ListItem/14` | 0.391227 | **The galaxy is dangerous.** Among the planets occupied by  the allied Pact Worlds to Near Space and the remote Vast,  there's usually something causing trouble somewhere.  Adventurers are always seek |
| 9 | `PZO22001 Starfinder Player Core 030-039::/page/8/Text/4` | 0.377454 | Talavet is a kasathan deity of tradition, communal  memories, and living stories. |
| 10 | `PZO22001 Starfinder Player Core 030-039::/page/0/ListItem/13` | 0.375425 | **The galaxy is diverse.** Countless worlds and cultures  flourish all over the galaxy (and beyond). Travelers  from Near Space often visit the Pact Worlds (and vice  versa). Visitors from the Vast ar |

### Query 77
- Text: What is the rule about The *Idari* is a world ship built long ago on the world of Kasath  to transport its population away from the dying planet,  toward a desert world kasatha mystics believed was their  promised land: Akiton. The *Idari* traveled slowly at a fraction  of light speed, so by the time the ship arrived, Akiton had  already boomed and declined, but a massive population still  lived there. Unwilling to invade an occupied world, the *Idari*'s  ancestral ruling Doyenate decided to remain in the system  for a time and prepare for another journey. The *Idari *has full  Pact World status, meaning residents are free to move to  other worlds in the system, and immigrants are welcomed in  turn. The *Idari* has its own manufacturing Crucibles, farms,  water reservoirs, and natural preserves teeming with animals  and plants cultivated from the ancient kasatha home world.  A popular political movement gaining traction among the  Doyenate advocates for the *Idari* to leave the system.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 030-039::/page/2/Text/23']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 030-039::/page/2/Text/23', 'PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/27', 'PZO22001 Starfinder Player Core 030-039::/page/0/ListItem/14']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 030-039::/page/2/Text/23` | 0.990814 | The *Idari* is a world ship built long ago on the world of Kasath  to transport its population away from the dying planet,  toward a desert world kasatha mystics believed was their  promised land: Aki |
| 2 | `PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/27` | 0.571492 | A restless engineer who's bored with the *Idari*'s  predictable orbit and ancient schematics. |
| 3 | `PZO22001 Starfinder Player Core 030-039::/page/0/ListItem/14` | 0.556431 | **The galaxy is dangerous.** Among the planets occupied by  the allied Pact Worlds to Near Space and the remote Vast,  there's usually something causing trouble somewhere.  Adventurers are always seek |
| 4 | `PZO22001 Starfinder Player Core 030-039::/page/4/Text/9` | 0.494253 | Apostae is a hollow planetoid with no atmosphere and few  resources. Mysterious gateways on the planet's rocky surface  access a network of tunnels, magitech chambers, and caverns  inside its core. Th |
| 5 | `PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/22` | 0.491035 | **Kasatha World Ship** |
| 6 | `PZO22001 Starfinder Player Core 030-039::/page/0/ListItem/13` | 0.489859 | **The galaxy is diverse.** Countless worlds and cultures  flourish all over the galaxy (and beyond). Travelers  from Near Space often visit the Pact Worlds (and vice  versa). Visitors from the Vast ar |
| 7 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/1` | 0.484821 | The united worlds are Absalom Station, Aballon, Castrovel,  Akiton, Verces, the Diaspora, Eox, Triaxus, Dykon, Kalo-Mahoi,  Marata, Liavara, and Bretheda. The *Idari*—a starship—is counted  among thei |
| 8 | `PZO22001 Starfinder Player Core 030-039::/page/2/Text/7` | 0.477204 | Akiton is a dusty red world of sunbaked deserts, rundown  cities, and rusting scrapyards. It was once a booming industrial  paradise overflowing with wealth earned from mining thasteron,  a starship f |
| 9 | `PZO22001 Starfinder Player Core 030-039::/page/5/Text/7` | 0.471391 | Abadar brings civilization to uninhabited worlds,  promotes law, and encourages commerce and trade between  cultures. |
| 10 | `PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/21` | 0.471386 | THE IDARI |

### Query 78
- Text: What is the rule about Example Characters?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/24']
- Expected found: `True`
- Expected rank: `11`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 030-039::/page/1/SectionHeader/19', 'PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/17', 'PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/9']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 030-039::/page/1/SectionHeader/19` | 0.837066 | Example Characters |
| 2 | `PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/9` | 0.837066 | Example Characters |
| 3 | `PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/17` | 0.837066 | Example Characters |
| 4 | `PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/1` | 0.807066 | Example Characters |
| 5 | `PZO22001 Starfinder Player Core 030-039::/page/4/SectionHeader/11` | 0.807066 | Example Characters |
| 6 | `PZO22001 Starfinder Player Core 030-039::/page/4/SectionHeader/3` | 0.807066 | Example Characters |
| 7 | `PZO22001 Starfinder Player Core 030-039::/page/3/SectionHeader/22` | 0.807066 | Example Characters |
| 8 | `PZO22001 Starfinder Player Core 030-039::/page/3/SectionHeader/13` | 0.807066 | Example Characters |
| 9 | `PZO22001 Starfinder Player Core 030-039::/page/3/SectionHeader/4` | 0.807066 | Example Characters |
| 10 | `PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/31` | 0.807066 | Example Characters |

### Query 79
- Text: Summarize A priest of Talavet (goddess of community, storytelling,  and tradition), who was chosen by the Doyenate to  carry on your ancestral traditions.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/25']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/25', 'PZO22001 Starfinder Player Core 030-039::/page/8/Text/4', 'PZO22001 Starfinder Player Core 030-039::/page/8/Text/60']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/25` | 1.034626 | A priest of Talavet (goddess of community, storytelling,  and tradition), who was chosen by the Doyenate to  carry on your ancestral traditions. |
| 2 | `PZO22001 Starfinder Player Core 030-039::/page/8/Text/4` | 0.715737 | Talavet is a kasathan deity of tradition, communal  memories, and living stories. |
| 3 | `PZO22001 Starfinder Player Core 030-039::/page/8/Text/60` | 0.489186 | Yaraesa was a lashunta who attained divinity  through enlightenment, guiding others to follow her path. |
| 4 | `PZO22001 Starfinder Player Core 030-039::/page/9/Text/18` | 0.442299 | figures from mythology or history who were chosen by  Damoritosh to join his army when they died. Each saint is  known for their heroic deeds in life. In the afterlife, they  gained unique powers with |
| 5 | `PZO22001 Starfinder Player Core 030-039::/page/8/Text/5` | 0.406612 | **Areas of Concern **community, storytelling, and tradition |
| 6 | `PZO22001 Starfinder Player Core 030-039::/page/6/Text/73` | 0.402775 | Legends say that Lao Shu Po was once a simple rat  who gnawed on the corpse of a dead god and became divine.  She's considered an ancestral deity by many ysoki. |
| 7 | `PZO22001 Starfinder Player Core 030-039::/page/7/Text/67` | 0.378449 | Ancient and powerful beyond even most other  gods, Pharasma judges the souls of all who perish from  her throne in the Boneyard. Through these judgments, she  ensures that the natural cycle of birth a |
| 8 | `PZO22001 Starfinder Player Core 030-039::/page/6/Text/16` | 0.377030 | Eloritu is a mysterious god who has revealed  secrets of magic and metaphysics to his disciples. |
| 9 | `PZO22001 Starfinder Player Core 030-039::/page/2/Text/23` | 0.376142 | The *Idari* is a world ship built long ago on the world of Kasath  to transport its population away from the dying planet,  toward a desert world kasatha mystics believed was their  promised land: Aki |
| 10 | `PZO22001 Starfinder Player Core 030-039::/page/5/Text/4` | 0.375569 | Anyone can worship a deity, but those who do so devoutly  should take care to pursue the faith's edicts (behaviors  the faith encourages) and avoid its anathemas (actions  considered blasphemous). Eac |

### Query 80
- Text: Summarize A young kasatha who's decided not to return from your  Tempering, joining a touring Driftwave band instead.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/26']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/26', 'PZO22001 Starfinder Player Core 030-039::/page/8/Text/17', 'PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/22']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/26` | 1.039845 | A young kasatha who's decided not to return from your  Tempering, joining a touring Driftwave band instead. |
| 2 | `PZO22001 Starfinder Player Core 030-039::/page/8/Text/17` | 0.451983 | Triune is a fusion of the three technological  deities Epoch, Brigh, and Casandalee. Triune's Signal made  Drift travel possible. |
| 3 | `PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/22` | 0.445236 | **Kasatha World Ship** |
| 4 | `PZO22001 Starfinder Player Core 030-039::/page/1/ListItem/10` | 0.375042 | A priest of Triune who travels across the galaxy  installing and repairing Drift beacons, receiving sacred  downloads from Striving's sacred neural network. |
| 5 | `PZO22001 Starfinder Player Core 030-039::/page/3/Text/19` | 0.373970 | Liavara is a peach-colored gas giant encircled by dust  rings and many shepherd moons. In Liavara's upper  atmosphere, elegant arcologies float through swirling  skies; deeper down, piscine titans swi |
| 6 | `PZO22001 Starfinder Player Core 030-039::/page/8/Text/4` | 0.371826 | Talavet is a kasathan deity of tradition, communal  memories, and living stories. |
| 7 | `PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/4` | 0.363207 | A solarian disciple, training at the Cosmonastery of the  Empty Orbit. |
| 8 | `PZO22001 Starfinder Player Core 030-039::/page/2/Text/23` | 0.356555 | The *Idari* is a world ship built long ago on the world of Kasath  to transport its population away from the dying planet,  toward a desert world kasatha mystics believed was their  promised land: Aki |
| 9 | `PZO22001 Starfinder Player Core 030-039::/page/0/ListItem/12` | 0.343884 | **The galaxy is connected.** Adventurers have used magical  engines and powerful spells to explore the galaxy  since ancient times, but such travel was rare until the  god Triune introduced hyperspace |
| 10 | `PZO22001 Starfinder Player Core 030-039::/page/1/ListItem/20` | 0.330998 | A lashunta soldier patrolling the jungle accompanied by  a shotalashu hatchling that has imprinted on you. |

### Query 81
- Text: Summarize A restless engineer who's bored with the *Idari*'s  predictable orbit and ancient schematics.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/27']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/27', 'PZO22001 Starfinder Player Core 030-039::/page/2/Text/23', 'PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/21']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/27` | 1.032775 | A restless engineer who's bored with the *Idari*'s  predictable orbit and ancient schematics. |
| 2 | `PZO22001 Starfinder Player Core 030-039::/page/2/Text/23` | 0.581734 | The *Idari* is a world ship built long ago on the world of Kasath  to transport its population away from the dying planet,  toward a desert world kasatha mystics believed was their  promised land: Aki |
| 3 | `PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/21` | 0.517254 | THE IDARI |
| 4 | `PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/20` | 0.451438 | An android bounty hunter, pursuing dangerous criminals  and rogue virtual intelligences across the planet. |
| 5 | `PZO22001 Starfinder Player Core 030-039::/page/6/Text/44` | 0.444744 | Ibra is an outer god of cosmic enlightenment, an  inscrutable being seeking to understand the multiverse. |
| 6 | `PZO22001 Starfinder Player Core 030-039::/page/1/ListItem/10` | 0.437780 | A priest of Triune who travels across the galaxy  installing and repairing Drift beacons, receiving sacred  downloads from Striving's sacred neural network. |
| 7 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/1` | 0.428367 | The united worlds are Absalom Station, Aballon, Castrovel,  Akiton, Verces, the Diaspora, Eox, Triaxus, Dykon, Kalo-Mahoi,  Marata, Liavara, and Bretheda. The *Idari*—a starship—is counted  among thei |
| 8 | `PZO22001 Starfinder Player Core 030-039::/page/4/ListItem/13` | 0.428176 | A xenoarchaeologist exploring the planet's hollow interior  and cataloging the strange ruins and dangerous creatures  that lurk within. |
| 9 | `PZO22001 Starfinder Player Core 030-039::/page/4/ListItem/14` | 0.411356 | A plucky smuggler, working to save up enough creds to  pay off your debt to a ruthless azrinaran oligarch so you  can finally buy back your starship. |
| 10 | `PZO22001 Starfinder Player Core 030-039::/page/8/Text/46` | 0.408415 | Weydan enjoys discovery and exploration with  a purpose. He believes everyone deserves the equal right  to pursue such experiences and walks the galaxy in diverse  avatars to commune with his follower |

### Query 82
- Text: Summarize THE DIASPORA
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/28']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/28', 'PZO22001 Starfinder Player Core 030-039::/page/2/Text/30', 'PZO22001 Starfinder Player Core 030-039::/page/6/Text/39']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/28` | 0.961822 | THE DIASPORA |
| 2 | `PZO22001 Starfinder Player Core 030-039::/page/2/Text/30` | 0.510638 | The Diaspora is an asteroid belt formed long before the  Gap, when a terrible cataclysm destroyed the twin planets  Damiar and Iovo. The remains of the two destroyed worlds  float among millions of ch |
| 3 | `PZO22001 Starfinder Player Core 030-039::/page/6/Text/39` | 0.379745 | **Divine Skill** Diplomacy |
| 4 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/1` | 0.331469 | The united worlds are Absalom Station, Aballon, Castrovel,  Akiton, Verces, the Diaspora, Eox, Triaxus, Dykon, Kalo-Mahoi,  Marata, Liavara, and Bretheda. The *Idari*—a starship—is counted  among thei |
| 5 | `PZO22001 Starfinder Player Core 030-039::/page/5/SectionHeader/47` | 0.330996 | THE DEVOURER |
| 6 | `PZO22001 Starfinder Player Core 030-039::/page/3/SectionHeader/9` | 0.319479 | **The Dragon Planet** |
| 7 | `PZO22001 Starfinder Player Core 030-039::/page/4/SectionHeader/7` | 0.303995 | APOSTAE |
| 8 | `PZO22001 Starfinder Player Core 030-039::/page/5/Text/23` | 0.301829 | **Anathema** betray shipmates, forsake piracy, settle on a planet **Divine Attribute** Dexterity or Constitution |
| 9 | `PZO22001 Starfinder Player Core 030-039::/page/9/SectionHeader/8` | 0.298686 | FAITHS AND PHILOSOPHIES |
| 10 | `PZO22001 Starfinder Player Core 030-039::/page/7/Text/13` | 0.298399 | **Anathema** disobey a superior, shirk your duties, settle for  easy rewards |

### Query 83
- Text: Summarize **Belt of Broken Worlds**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/29']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/29', 'PZO22001 Starfinder Player Core 030-039::/page/2/Text/15', 'PZO22001 Starfinder Player Core 030-039::/page/3/SectionHeader/18']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/29` | 0.990665 | **Belt of Broken Worlds** |
| 2 | `PZO22001 Starfinder Player Core 030-039::/page/2/Text/15` | 0.521214 | Verces is a tidally locked world with a sun-scoured light side,  a frozen dark side, and a belt of opulent cybercities linked by  high-speed bullet trains called the Ring of Nations. The Ring  of Nati |
| 3 | `PZO22001 Starfinder Player Core 030-039::/page/3/SectionHeader/18` | 0.461869 | **Many-Mooned World of Dreamers** |
| 4 | `PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/36` | 0.409355 | **Planet of the Dead** |
| 5 | `PZO22001 Starfinder Player Core 030-039::/page/2/Text/16` | 0.400779 | Major locations on Verces include the Ring of Nations,  a band of sprawling megacities inhabited by augmented  verthani, androids, and many others; Skydock, modern  shipyards built atop an ancient spa |
| 6 | `PZO22001 Starfinder Player Core 030-039::/page/3/Text/28` | 0.391767 | Bretheda is a massive, stormy gas giant orbited by moons  where diverse peoples have built thriving, cosmopolitan  societies. Bretheda and its moons are home to cuttingedge biotech foundries, living c |
| 7 | `PZO22001 Starfinder Player Core 030-039::/page/2/Text/30` | 0.389558 | The Diaspora is an asteroid belt formed long before the  Gap, when a terrible cataclysm destroyed the twin planets  Damiar and Iovo. The remains of the two destroyed worlds  float among millions of ch |
| 8 | `PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/6` | 0.385308 | **Lonely Red Desert World** |
| 9 | `PZO22001 Starfinder Player Core 030-039::/page/0/SectionHeader/15` | 0.381077 | THE PACT WORLDS |
| 10 | `PZO22001 Starfinder Player Core 030-039::/page/4/Text/29` | 0.378014 | Regions of the Vast include the Azlanti Star Empire, a vast  territory of unknown size controlled by a colonizing regime  ruled by the descendants of a human nation from lost Golarion;  Kazmurg's Absu |

### Query 84
- Text: What is the rule about The Diaspora is an asteroid belt formed long before the  Gap, when a terrible cataclysm destroyed the twin planets  Damiar and Iovo. The remains of the two destroyed worlds  float among millions of chunks of rock and ice. Smugglers and  pirates hide out in the debris, and native sarcesians glide on  shimmering wings between their terraformed crèche worlds.  The River Between flows through it, a current of radiant solar  energy that serves as both a space highway and spiritual hub  for many sarcesians.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 030-039::/page/2/Text/30']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 030-039::/page/2/Text/30', 'PZO22001 Starfinder Player Core 030-039::/page/1/Text/5', 'PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/33']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 030-039::/page/2/Text/30` | 1.009081 | The Diaspora is an asteroid belt formed long before the  Gap, when a terrible cataclysm destroyed the twin planets  Damiar and Iovo. The remains of the two destroyed worlds  float among millions of ch |
| 2 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/5` | 0.580211 | Aballon is a rocky, cratered world of superheated metallic  deserts and deep ice wells. Thousands of years before the  Gap, a mysterious civilization called the First Ones utilized  Aballon's abundant |
| 3 | `PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/33` | 0.563561 | A sarcesian witchwarper from a reality where the water  in the River Between never dried up. |
| 4 | `PZO22001 Starfinder Player Core 030-039::/page/4/Text/10` | 0.521099 | Regions include Nightarch, a pressurized megacity where  opulent spires tower over air-choked slums, named for the  massive gate leading inside the planet at the center of the  settlement; the Silted |
| 5 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/1` | 0.521053 | The united worlds are Absalom Station, Aballon, Castrovel,  Akiton, Verces, the Diaspora, Eox, Triaxus, Dykon, Kalo-Mahoi,  Marata, Liavara, and Bretheda. The *Idari*—a starship—is counted  among thei |
| 6 | `PZO22001 Starfinder Player Core 030-039::/page/3/Text/19` | 0.517329 | Liavara is a peach-colored gas giant encircled by dust  rings and many shepherd moons. In Liavara's upper  atmosphere, elegant arcologies float through swirling  skies; deeper down, piscine titans swi |
| 7 | `PZO22001 Starfinder Player Core 030-039::/page/3/Text/28` | 0.516261 | Bretheda is a massive, stormy gas giant orbited by moons  where diverse peoples have built thriving, cosmopolitan  societies. Bretheda and its moons are home to cuttingedge biotech foundries, living c |
| 8 | `PZO22001 Starfinder Player Core 030-039::/page/2/Text/15` | 0.512501 | Verces is a tidally locked world with a sun-scoured light side,  a frozen dark side, and a belt of opulent cybercities linked by  high-speed bullet trains called the Ring of Nations. The Ring  of Nati |
| 9 | `PZO22001 Starfinder Player Core 030-039::/page/2/Text/23` | 0.512098 | The *Idari* is a world ship built long ago on the world of Kasath  to transport its population away from the dying planet,  toward a desert world kasatha mystics believed was their  promised land: Aki |
| 10 | `PZO22001 Starfinder Player Core 030-039::/page/2/Text/16` | 0.508583 | Major locations on Verces include the Ring of Nations,  a band of sprawling megacities inhabited by augmented  verthani, androids, and many others; Skydock, modern  shipyards built atop an ancient spa |

### Query 85
- Text: What is the rule about Example Characters?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/31']
- Expected found: `True`
- Expected rank: `10`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 030-039::/page/1/SectionHeader/19', 'PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/17', 'PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/9']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 030-039::/page/1/SectionHeader/19` | 0.837066 | Example Characters |
| 2 | `PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/9` | 0.837066 | Example Characters |
| 3 | `PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/17` | 0.837066 | Example Characters |
| 4 | `PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/1` | 0.807066 | Example Characters |
| 5 | `PZO22001 Starfinder Player Core 030-039::/page/4/SectionHeader/11` | 0.807066 | Example Characters |
| 6 | `PZO22001 Starfinder Player Core 030-039::/page/4/SectionHeader/3` | 0.807066 | Example Characters |
| 7 | `PZO22001 Starfinder Player Core 030-039::/page/3/SectionHeader/22` | 0.807066 | Example Characters |
| 8 | `PZO22001 Starfinder Player Core 030-039::/page/3/SectionHeader/13` | 0.807066 | Example Characters |
| 9 | `PZO22001 Starfinder Player Core 030-039::/page/3/SectionHeader/4` | 0.807066 | Example Characters |
| 10 | `PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/31` | 0.807066 | Example Characters |

### Query 86
- Text: Summarize A pirate loyal to the Free Captains who always donates  some of their loot to those in need.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/32']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/32', 'PZO22001 Starfinder Player Core 030-039::/page/5/Text/20', 'PZO22001 Starfinder Player Core 030-039::/page/4/ListItem/14']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/32` | 1.022847 | A pirate loyal to the Free Captains who always donates  some of their loot to those in need. |
| 2 | `PZO22001 Starfinder Player Core 030-039::/page/5/Text/20` | 0.535816 | Besmara is worshipped by pirate crews in  shipping lanes across the galaxy. |
| 3 | `PZO22001 Starfinder Player Core 030-039::/page/4/ListItem/14` | 0.488504 | A plucky smuggler, working to save up enough creds to  pay off your debt to a ruthless azrinaran oligarch so you  can finally buy back your starship. |
| 4 | `PZO22001 Starfinder Player Core 030-039::/page/4/ListItem/21` | 0.432823 | A freedom fighter sworn to defend your world's  reclaimed independence at any cost. |
| 5 | `PZO22001 Starfinder Player Core 030-039::/page/5/Text/22` | 0.428038 | **Edicts** traverse the stars, stay loyal to a worthy captain and  crew, take what you want |
| 6 | `PZO22001 Starfinder Player Core 030-039::/page/5/Text/23` | 0.402632 | **Anathema** betray shipmates, forsake piracy, settle on a planet **Divine Attribute** Dexterity or Constitution |
| 7 | `PZO22001 Starfinder Player Core 030-039::/page/9/Text/18` | 0.375794 | figures from mythology or history who were chosen by  Damoritosh to join his army when they died. Each saint is  known for their heroic deeds in life. In the afterlife, they  gained unique powers with |
| 8 | `PZO22001 Starfinder Player Core 030-039::/page/9/Text/39` | 0.373069 | **Anathema** give charity to others; offer money to those who  don't deserve wealth; overindulge in physical pleasures,  food, or drink; spend money frivolously |
| 9 | `PZO22001 Starfinder Player Core 030-039::/page/7/Text/26` | 0.369644 | She empowers her followers to fight oppression, create art,  and live free. |
| 10 | `PZO22001 Starfinder Player Core 030-039::/page/7/Text/10` | 0.366324 | Empire. She rewards followers who survive her brutal demands. |

### Query 87
- Text: Summarize A sarcesian witchwarper from a reality where the water  in the River Between never dried up.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/33']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/33', 'PZO22001 Starfinder Player Core 030-039::/page/2/Text/30', 'PZO22001 Starfinder Player Core 030-039::/page/4/ListItem/23']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/33` | 1.035210 | A sarcesian witchwarper from a reality where the water  in the River Between never dried up. |
| 2 | `PZO22001 Starfinder Player Core 030-039::/page/2/Text/30` | 0.543201 | The Diaspora is an asteroid belt formed long before the  Gap, when a terrible cataclysm destroyed the twin planets  Damiar and Iovo. The remains of the two destroyed worlds  float among millions of ch |
| 3 | `PZO22001 Starfinder Player Core 030-039::/page/4/ListItem/23` | 0.500249 | A mystic wandering the wastes ravaged by the Shriek,  seeking natural ways to heal your war-torn ancestral lands. |
| 4 | `PZO22001 Starfinder Player Core 030-039::/page/3/ListItem/6` | 0.403359 | A living necromancer, building up political clout and  magical power with the goal of becoming a bone sage. |
| 5 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/18` | 0.400592 | spires of Sovyrian, a nation of surrealist cities sculpted  by elven magic. Castrovel's wilds are virtually unspoiled  because the planet's industry occurs on the super-polluted  moon Elindrae. |
| 6 | `PZO22001 Starfinder Player Core 030-039::/page/7/Text/67` | 0.398619 | Ancient and powerful beyond even most other  gods, Pharasma judges the souls of all who perish from  her throne in the Boneyard. Through these judgments, she  ensures that the natural cycle of birth a |
| 7 | `PZO22001 Starfinder Player Core 030-039::/page/4/Text/29` | 0.390297 | Regions of the Vast include the Azlanti Star Empire, a vast  territory of unknown size controlled by a colonizing regime  ruled by the descendants of a human nation from lost Golarion;  Kazmurg's Absu |
| 8 | `PZO22001 Starfinder Player Core 030-039::/page/9/Text/19` | 0.389642 | Different battle saints represent every struggle, from  treating chronic illness to moving up the corporate ladder.  Some aren't vesk, like Apna the brave skittermander, whose  legendary helpfulness m |
| 9 | `PZO22001 Starfinder Player Core 030-039::/page/3/ListItem/24` | 0.388752 | A shirren devotee of Hylax, leaving Nchak on a sacred  mission. |
| 10 | `PZO22001 Starfinder Player Core 030-039::/page/4/Text/9` | 0.384955 | Apostae is a hollow planetoid with no atmosphere and few  resources. Mysterious gateways on the planet's rocky surface  access a network of tunnels, magitech chambers, and caverns  inside its core. Th |

### Query 88
- Text: What is the rule about A mercenary hired to guard a secret corporate laboratory  who's having second thoughts about the contract.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/34']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/34', 'PZO22001 Starfinder Player Core 030-039::/page/4/ListItem/12', 'PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/2']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/34` | 0.945228 | A mercenary hired to guard a secret corporate laboratory  who's having second thoughts about the contract. |
| 2 | `PZO22001 Starfinder Player Core 030-039::/page/4/ListItem/12` | 0.513243 | A corporate assassin hired to guard the scion of a  powerful azrinaran dynasty—when you're not spying on  her rivals or sniping your enemies. |
| 3 | `PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/2` | 0.473609 | A corporate spy, tasked by a shady megacorp with  infiltrating the cutthroat boardrooms of Bluerise Tower. |
| 4 | `PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/19` | 0.374349 | A hacktivist who exposes corporate conspiracies,  operating out of a dingy cybercafe under a virtual identity. |
| 5 | `PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/3` | 0.344032 | A ghost courier, exploring the Ghost Levels on a hunt  for valuable relics, surviving dangerous anomalies and  fighting dimensionally displaced monsters. |
| 6 | `PZO22001 Starfinder Player Core 030-039::/page/6/Text/76` | 0.341649 | **Anathema** work honestly for something you could steal  instead, risk too much for someone else, harm a rat |
| 7 | `PZO22001 Starfinder Player Core 030-039::/page/5/Text/23` | 0.339262 | **Anathema** betray shipmates, forsake piracy, settle on a planet **Divine Attribute** Dexterity or Constitution |
| 8 | `PZO22001 Starfinder Player Core 030-039::/page/5/Text/8` | 0.328710 | **Areas of Concern **cities, law, corporations, wealth |
| 9 | `PZO22001 Starfinder Player Core 030-039::/page/3/ListItem/15` | 0.326194 | A daring ace pilot, flying for fame and fortune on the  payroll of a dragon-owned corporation. |
| 10 | `PZO22001 Starfinder Player Core 030-039::/page/6/Text/74` | 0.321233 | **Areas of Concern **assassins, rats, spies, thieves |

### Query 89
- Text: Summarize EOX
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/35']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/35', 'PZO22001 Starfinder Player Core 030-039::/page/2/Text/37', 'PZO22001 Starfinder Player Core 030-039::/page/3/Text/3']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/35` | 0.903345 | EOX |
| 2 | `PZO22001 Starfinder Player Core 030-039::/page/2/Text/37` | 0.516845 | Once a green world ruled by living elebrians, Eox is now a  deadly wasteland inhabited by undead. Hubristic elebrian |
| 3 | `PZO22001 Starfinder Player Core 030-039::/page/3/Text/3` | 0.461068 | Notable locations on Eox include the undying capital of  Orphys, a grim metropolis of bone spires, blood aqueducts,  and funerary gardens; the Necroforges of the Lifeline,  a walled complex peddling i |
| 4 | `PZO22001 Starfinder Player Core 030-039::/page/3/Text/2` | 0.429438 | In the modern era, bone sages rule scattered fiefdoms  on Eox's irradiated surface, and hordes of mindless undead  wander the wastes outside magical bunkers and walled  necropolises. Many are tragic b |
| 5 | `PZO22001 Starfinder Player Core 030-039::/page/3/Text/1` | 0.409944 | leaders tried to conquer Damiar and Iovo, launching a terrible  attack against them. The assault shattered both targets  at the cost of burning their own world's atmosphere and  irradiating its surfac |
| 6 | `PZO22001 Starfinder Player Core 030-039::/page/3/SectionHeader/8` | 0.280929 | TRIAXUS |
| 7 | `PZO22001 Starfinder Player Core 030-039::/page/6/SectionHeader/29` | 0.264967 | HYLAX |
| 8 | `PZO22001 Starfinder Player Core 030-039::/page/7/SectionHeader/52` | 0.246617 | ORAS |
| 9 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/1` | 0.223040 | The united worlds are Absalom Station, Aballon, Castrovel,  Akiton, Verces, the Diaspora, Eox, Triaxus, Dykon, Kalo-Mahoi,  Marata, Liavara, and Bretheda. The *Idari*—a starship—is counted  among thei |
| 10 | `PZO22001 Starfinder Player Core 030-039::/page/5/Text/64` | 0.221251 | **APPENDIX** |

### Query 90
- Text: Summarize **Planet of the Dead**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/36']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/36', 'PZO22001 Starfinder Player Core 030-039::/page/3/SectionHeader/9', 'PZO22001 Starfinder Player Core 030-039::/page/4/SectionHeader/8']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/36` | 0.972647 | **Planet of the Dead** |
| 2 | `PZO22001 Starfinder Player Core 030-039::/page/3/SectionHeader/9` | 0.546669 | **The Dragon Planet** |
| 3 | `PZO22001 Starfinder Player Core 030-039::/page/4/SectionHeader/8` | 0.527797 | **Dungeon Planet** |
| 4 | `PZO22001 Starfinder Player Core 030-039::/page/7/Text/70` | 0.457117 | **Anathema** create undead, desecrate a corpse, take from the  dead in bad faith |
| 5 | `PZO22001 Starfinder Player Core 030-039::/page/2/Text/37` | 0.427120 | Once a green world ruled by living elebrians, Eox is now a  deadly wasteland inhabited by undead. Hubristic elebrian |
| 6 | `PZO22001 Starfinder Player Core 030-039::/page/8/Text/33` | 0.408023 | **Edicts** become undead upon death, create or protect the  undead, sate your appetites |
| 7 | `PZO22001 Starfinder Player Core 030-039::/page/7/Text/68` | 0.406812 | **Areas of Concern **birth, death, fate, prophecy, time |
| 8 | `PZO22001 Starfinder Player Core 030-039::/page/0/ListItem/14` | 0.402009 | **The galaxy is dangerous.** Among the planets occupied by  the allied Pact Worlds to Near Space and the remote Vast,  there's usually something causing trouble somewhere.  Adventurers are always seek |
| 9 | `PZO22001 Starfinder Player Core 030-039::/page/7/Text/77` | 0.392501 | **Domains** death, fate, healing, knowledge |
| 10 | `PZO22001 Starfinder Player Core 030-039::/page/9/Text/56` | 0.389857 | **GAME** |

### Query 91
- Text: Summarize Once a green world ruled by living elebrians, Eox is now a  deadly wasteland inhabited by undead. Hubristic elebrian
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 030-039::/page/2/Text/37']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 030-039::/page/2/Text/37', 'PZO22001 Starfinder Player Core 030-039::/page/3/Text/2', 'PZO22001 Starfinder Player Core 030-039::/page/3/Text/3']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 030-039::/page/2/Text/37` | 1.033194 | Once a green world ruled by living elebrians, Eox is now a  deadly wasteland inhabited by undead. Hubristic elebrian |
| 2 | `PZO22001 Starfinder Player Core 030-039::/page/3/Text/2` | 0.687929 | In the modern era, bone sages rule scattered fiefdoms  on Eox's irradiated surface, and hordes of mindless undead  wander the wastes outside magical bunkers and walled  necropolises. Many are tragic b |
| 3 | `PZO22001 Starfinder Player Core 030-039::/page/3/Text/3` | 0.638736 | Notable locations on Eox include the undying capital of  Orphys, a grim metropolis of bone spires, blood aqueducts,  and funerary gardens; the Necroforges of the Lifeline,  a walled complex peddling i |
| 4 | `PZO22001 Starfinder Player Core 030-039::/page/3/Text/1` | 0.584461 | leaders tried to conquer Damiar and Iovo, launching a terrible  attack against them. The assault shattered both targets  at the cost of burning their own world's atmosphere and  irradiating its surfac |
| 5 | `PZO22001 Starfinder Player Core 030-039::/page/4/Text/10` | 0.502338 | Regions include Nightarch, a pressurized megacity where  opulent spires tower over air-choked slums, named for the  massive gate leading inside the planet at the center of the  settlement; the Silted |
| 6 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/18` | 0.481984 | spires of Sovyrian, a nation of surrealist cities sculpted  by elven magic. Castrovel's wilds are virtually unspoiled  because the planet's industry occurs on the super-polluted  moon Elindrae. |
| 7 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/5` | 0.471183 | Aballon is a rocky, cratered world of superheated metallic  deserts and deep ice wells. Thousands of years before the  Gap, a mysterious civilization called the First Ones utilized  Aballon's abundant |
| 8 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/2` | 0.462222 | What's left of Aucturn, a planet destroyed by the birth of  a god, floats among the field of ice and haunted space junk  ringing the system's outskirts, called the Gelid Edge. |
| 9 | `PZO22001 Starfinder Player Core 030-039::/page/3/Text/21` | 0.459384 | Regions include Roselight, a cloud of floating domes built  by barathu architects, and Deep Station, a research outpost  submerged in Liavara's alien seas. Liavara has many moons:  Hallas, a warded pr |
| 10 | `PZO22001 Starfinder Player Core 030-039::/page/4/Text/19` | 0.454440 | Regions include Voyedris, a treacherous wilderness  ravaged by rapid industrialization; Hafrerren, a rebel nationstate known for biotech research; Rafemii, a hub for magical  and spiritual development |

### Query 92
- Text: What is the rule about leaders tried to conquer Damiar and Iovo, launching a terrible  attack against them. The assault shattered both targets  at the cost of burning their own world's atmosphere and  irradiating its surface. Countless people died screaming.  The traumatized survivors embraced necromancy to rebuild  Eox, becoming the first bone sages and reviving their fallen  families and friends into an eternity of undeath.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 030-039::/page/3/Text/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 030-039::/page/3/Text/1', 'PZO22001 Starfinder Player Core 030-039::/page/3/Text/2', 'PZO22001 Starfinder Player Core 030-039::/page/2/Text/37']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 030-039::/page/3/Text/1` | 0.961278 | leaders tried to conquer Damiar and Iovo, launching a terrible  attack against them. The assault shattered both targets  at the cost of burning their own world's atmosphere and  irradiating its surfac |
| 2 | `PZO22001 Starfinder Player Core 030-039::/page/3/Text/2` | 0.682720 | In the modern era, bone sages rule scattered fiefdoms  on Eox's irradiated surface, and hordes of mindless undead  wander the wastes outside magical bunkers and walled  necropolises. Many are tragic b |
| 3 | `PZO22001 Starfinder Player Core 030-039::/page/2/Text/37` | 0.583260 | Once a green world ruled by living elebrians, Eox is now a  deadly wasteland inhabited by undead. Hubristic elebrian |
| 4 | `PZO22001 Starfinder Player Core 030-039::/page/3/Text/3` | 0.501099 | Notable locations on Eox include the undying capital of  Orphys, a grim metropolis of bone spires, blood aqueducts,  and funerary gardens; the Necroforges of the Lifeline,  a walled complex peddling i |
| 5 | `PZO22001 Starfinder Player Core 030-039::/page/2/Text/30` | 0.427416 | The Diaspora is an asteroid belt formed long before the  Gap, when a terrible cataclysm destroyed the twin planets  Damiar and Iovo. The remains of the two destroyed worlds  float among millions of ch |
| 6 | `PZO22001 Starfinder Player Core 030-039::/page/3/ListItem/6` | 0.423191 | A living necromancer, building up political clout and  magical power with the goal of becoming a bone sage. |
| 7 | `PZO22001 Starfinder Player Core 030-039::/page/9/Text/18` | 0.415232 | figures from mythology or history who were chosen by  Damoritosh to join his army when they died. Each saint is  known for their heroic deeds in life. In the afterlife, they  gained unique powers with |
| 8 | `PZO22001 Starfinder Player Core 030-039::/page/3/Text/11` | 0.411434 | Triaxus is defended by the Skyfire Legion, an ancient  military order formed by dragonkin troopers and their  bonded humanoid partners, all supported by powerful  dragon allies. |
| 9 | `PZO22001 Starfinder Player Core 030-039::/page/8/Text/33` | 0.408753 | **Edicts** become undead upon death, create or protect the  undead, sate your appetites |
| 10 | `PZO22001 Starfinder Player Core 030-039::/page/3/Text/19` | 0.406714 | Liavara is a peach-colored gas giant encircled by dust  rings and many shepherd moons. In Liavara's upper  atmosphere, elegant arcologies float through swirling  skies; deeper down, piscine titans swi |

### Query 93
- Text: What is the rule about In the modern era, bone sages rule scattered fiefdoms  on Eox's irradiated surface, and hordes of mindless undead  wander the wastes outside magical bunkers and walled  necropolises. Many are tragic botched resurrections the  Eoxian ruling class can't bear to destroy, and all of them  are dangerous.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 030-039::/page/3/Text/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 030-039::/page/3/Text/2', 'PZO22001 Starfinder Player Core 030-039::/page/3/Text/1', 'PZO22001 Starfinder Player Core 030-039::/page/2/Text/37']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 030-039::/page/3/Text/2` | 0.988554 | In the modern era, bone sages rule scattered fiefdoms  on Eox's irradiated surface, and hordes of mindless undead  wander the wastes outside magical bunkers and walled  necropolises. Many are tragic b |
| 2 | `PZO22001 Starfinder Player Core 030-039::/page/3/Text/1` | 0.644934 | leaders tried to conquer Damiar and Iovo, launching a terrible  attack against them. The assault shattered both targets  at the cost of burning their own world's atmosphere and  irradiating its surfac |
| 3 | `PZO22001 Starfinder Player Core 030-039::/page/2/Text/37` | 0.626731 | Once a green world ruled by living elebrians, Eox is now a  deadly wasteland inhabited by undead. Hubristic elebrian |
| 4 | `PZO22001 Starfinder Player Core 030-039::/page/3/Text/3` | 0.593082 | Notable locations on Eox include the undying capital of  Orphys, a grim metropolis of bone spires, blood aqueducts,  and funerary gardens; the Necroforges of the Lifeline,  a walled complex peddling i |
| 5 | `PZO22001 Starfinder Player Core 030-039::/page/3/ListItem/6` | 0.499611 | A living necromancer, building up political clout and  magical power with the goal of becoming a bone sage. |
| 6 | `PZO22001 Starfinder Player Core 030-039::/page/9/Text/37` | 0.458205 | The mysterious Prophecies of Kalistrade date  back to older eras of lost Golarion, when the human known as  Kalistrade created a set of mystic teachings that drew upon  dreams he received. Modern mise |
| 7 | `PZO22001 Starfinder Player Core 030-039::/page/7/Text/69` | 0.453566 | **Edicts** strive to understand ancient prophecies, destroy  undead, lay bodies to rest |
| 8 | `PZO22001 Starfinder Player Core 030-039::/page/3/ListItem/7` | 0.445602 | A xenoarchaeologist studying the ruins beneath  Murthal, dodging ancient traps and uncovering relics  deep within its forgotten tombs. |
| 9 | `PZO22001 Starfinder Player Core 030-039::/page/4/ListItem/13` | 0.438722 | A xenoarchaeologist exploring the planet's hollow interior  and cataloging the strange ruins and dangerous creatures  that lurk within. |
| 10 | `PZO22001 Starfinder Player Core 030-039::/page/1/ListItem/8` | 0.438654 | A Starfinder exploring magitech ruins left by the  First Ones, risking encounters with deadly traps and  terrifying sentries. |

### Query 94
- Text: What is the rule about Notable locations on Eox include the undying capital of  Orphys, a grim metropolis of bone spires, blood aqueducts,  and funerary gardens; the Necroforges of the Lifeline,  a walled complex peddling immortality via gruesome  necrografts; Blackmoon, an ancient weapon crashed atop  the layered prehistoric necropolis Murthal; the Halls of the  Living, an underground bunker city designed as both a haven  for the living and a backdrop to bombastic reality shows; and  Lacustria Hollow, a dry seabed full of radioactive ruins and  wrecked magitech.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 030-039::/page/3/Text/3']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 030-039::/page/3/Text/3', 'PZO22001 Starfinder Player Core 030-039::/page/3/Text/2', 'PZO22001 Starfinder Player Core 030-039::/page/2/Text/37']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 030-039::/page/3/Text/3` | 0.965783 | Notable locations on Eox include the undying capital of  Orphys, a grim metropolis of bone spires, blood aqueducts,  and funerary gardens; the Necroforges of the Lifeline,  a walled complex peddling i |
| 2 | `PZO22001 Starfinder Player Core 030-039::/page/3/Text/2` | 0.676734 | In the modern era, bone sages rule scattered fiefdoms  on Eox's irradiated surface, and hordes of mindless undead  wander the wastes outside magical bunkers and walled  necropolises. Many are tragic b |
| 3 | `PZO22001 Starfinder Player Core 030-039::/page/2/Text/37` | 0.620455 | Once a green world ruled by living elebrians, Eox is now a  deadly wasteland inhabited by undead. Hubristic elebrian |
| 4 | `PZO22001 Starfinder Player Core 030-039::/page/4/Text/10` | 0.572232 | Regions include Nightarch, a pressurized megacity where  opulent spires tower over air-choked slums, named for the  massive gate leading inside the planet at the center of the  settlement; the Silted |
| 5 | `PZO22001 Starfinder Player Core 030-039::/page/3/Text/1` | 0.507065 | leaders tried to conquer Damiar and Iovo, launching a terrible  attack against them. The assault shattered both targets  at the cost of burning their own world's atmosphere and  irradiating its surfac |
| 6 | `PZO22001 Starfinder Player Core 030-039::/page/3/Text/21` | 0.494724 | Regions include Roselight, a cloud of floating domes built  by barathu architects, and Deep Station, a research outpost  submerged in Liavara's alien seas. Liavara has many moons:  Hallas, a warded pr |
| 7 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/6` | 0.491232 | The largest community on Aballon is Striving, an  industrious megacity containing a citywide neural network  sacred to Triune. Other regions include the industrial forgecity Automatrix; the immense, f |
| 8 | `PZO22001 Starfinder Player Core 030-039::/page/4/Text/19` | 0.490029 | Regions include Voyedris, a treacherous wilderness  ravaged by rapid industrialization; Hafrerren, a rebel nationstate known for biotech research; Rafemii, a hub for magical  and spiritual development |
| 9 | `PZO22001 Starfinder Player Core 030-039::/page/2/Text/16` | 0.485522 | Major locations on Verces include the Ring of Nations,  a band of sprawling megacities inhabited by augmented  verthani, androids, and many others; Skydock, modern  shipyards built atop an ancient spa |
| 10 | `PZO22001 Starfinder Player Core 030-039::/page/3/Text/29` | 0.461681 | Bretheda's violent storms make most of its gaseous layers  unlivable. The planet's largest city is Trillidiem, a domed,  industrial arcology governed by Confluence, a union of many  merged barathus. B |

### Query 95
- Text: What is the rule about Example Characters?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 030-039::/page/3/SectionHeader/4']
- Expected found: `True`
- Expected rank: `9`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 030-039::/page/1/SectionHeader/19', 'PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/17', 'PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/9']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 030-039::/page/1/SectionHeader/19` | 0.837066 | Example Characters |
| 2 | `PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/9` | 0.837066 | Example Characters |
| 3 | `PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/17` | 0.837066 | Example Characters |
| 4 | `PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/1` | 0.807066 | Example Characters |
| 5 | `PZO22001 Starfinder Player Core 030-039::/page/4/SectionHeader/11` | 0.807066 | Example Characters |
| 6 | `PZO22001 Starfinder Player Core 030-039::/page/4/SectionHeader/3` | 0.807066 | Example Characters |
| 7 | `PZO22001 Starfinder Player Core 030-039::/page/3/SectionHeader/22` | 0.807066 | Example Characters |
| 8 | `PZO22001 Starfinder Player Core 030-039::/page/3/SectionHeader/13` | 0.807066 | Example Characters |
| 9 | `PZO22001 Starfinder Player Core 030-039::/page/3/SectionHeader/4` | 0.807066 | Example Characters |
| 10 | `PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/31` | 0.807066 | Example Characters |

### Query 96
- Text: What is the rule about A reality show survivor who escaped the Halls of the  Living but is still bound by a predatory media contract.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 030-039::/page/3/ListItem/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 030-039::/page/3/ListItem/5', 'PZO22001 Starfinder Player Core 030-039::/page/7/Text/10', 'PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/34']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 030-039::/page/3/ListItem/5` | 0.949237 | A reality show survivor who escaped the Halls of the  Living but is still bound by a predatory media contract. |
| 2 | `PZO22001 Starfinder Player Core 030-039::/page/7/Text/10` | 0.420925 | Empire. She rewards followers who survive her brutal demands. |
| 3 | `PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/34` | 0.387529 | A mercenary hired to guard a secret corporate laboratory  who's having second thoughts about the contract. |
| 4 | `PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/33` | 0.341266 | A sarcesian witchwarper from a reality where the water  in the River Between never dried up. |
| 5 | `PZO22001 Starfinder Player Core 030-039::/page/3/Text/2` | 0.334972 | In the modern era, bone sages rule scattered fiefdoms  on Eox's irradiated surface, and hordes of mindless undead  wander the wastes outside magical bunkers and walled  necropolises. Many are tragic b |
| 6 | `PZO22001 Starfinder Player Core 030-039::/page/2/Text/18` | 0.321092 | • An augmented entertainer, transforming yourself into  living art. |
| 7 | `PZO22001 Starfinder Player Core 030-039::/page/7/Text/26` | 0.309695 | She empowers her followers to fight oppression, create art,  and live free. |
| 8 | `PZO22001 Starfinder Player Core 030-039::/page/6/Text/38` | 0.309186 | **Divine Sanctification** must choose holy |
| 9 | `PZO22001 Starfinder Player Core 030-039::/page/9/Text/27` | 0.305956 | Some deities sanctify their mystics and similarly  devoted followers. This gives the follower the holy  or unholy trait. The **holy** trait (page 448) indicates  a powerful devotion to altruism, helpi |
| 10 | `PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/19` | 0.305331 | A hacktivist who exposes corporate conspiracies,  operating out of a dingy cybercafe under a virtual identity. |

### Query 97
- Text: Summarize A living necromancer, building up political clout and  magical power with the goal of becoming a bone sage.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 030-039::/page/3/ListItem/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 030-039::/page/3/ListItem/6', 'PZO22001 Starfinder Player Core 030-039::/page/3/Text/2', 'PZO22001 Starfinder Player Core 030-039::/page/3/Text/1']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 030-039::/page/3/ListItem/6` | 1.032219 | A living necromancer, building up political clout and  magical power with the goal of becoming a bone sage. |
| 2 | `PZO22001 Starfinder Player Core 030-039::/page/3/Text/2` | 0.573666 | In the modern era, bone sages rule scattered fiefdoms  on Eox's irradiated surface, and hordes of mindless undead  wander the wastes outside magical bunkers and walled  necropolises. Many are tragic b |
| 3 | `PZO22001 Starfinder Player Core 030-039::/page/3/Text/1` | 0.486833 | leaders tried to conquer Damiar and Iovo, launching a terrible  attack against them. The assault shattered both targets  at the cost of burning their own world's atmosphere and  irradiating its surfac |
| 4 | `PZO22001 Starfinder Player Core 030-039::/page/3/Text/3` | 0.423249 | Notable locations on Eox include the undying capital of  Orphys, a grim metropolis of bone spires, blood aqueducts,  and funerary gardens; the Necroforges of the Lifeline,  a walled complex peddling i |
| 5 | `PZO22001 Starfinder Player Core 030-039::/page/8/Text/33` | 0.420793 | **Edicts** become undead upon death, create or protect the  undead, sate your appetites |
| 6 | `PZO22001 Starfinder Player Core 030-039::/page/2/Text/37` | 0.414727 | Once a green world ruled by living elebrians, Eox is now a  deadly wasteland inhabited by undead. Hubristic elebrian |
| 7 | `PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/20` | 0.407846 | An android bounty hunter, pursuing dangerous criminals  and rogue virtual intelligences across the planet. |
| 8 | `PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/33` | 0.403079 | A sarcesian witchwarper from a reality where the water  in the River Between never dried up. |
| 9 | `PZO22001 Starfinder Player Core 030-039::/page/2/Text/18` | 0.401554 | • An augmented entertainer, transforming yourself into  living art. |
| 10 | `PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/3` | 0.400070 | A ghost courier, exploring the Ghost Levels on a hunt  for valuable relics, surviving dangerous anomalies and  fighting dimensionally displaced monsters. |

### Query 98
- Text: Summarize A xenoarchaeologist studying the ruins beneath  Murthal, dodging ancient traps and uncovering relics  deep within its forgotten tombs.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 030-039::/page/3/ListItem/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 030-039::/page/3/ListItem/7', 'PZO22001 Starfinder Player Core 030-039::/page/4/ListItem/13', 'PZO22001 Starfinder Player Core 030-039::/page/3/Text/2']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 030-039::/page/3/ListItem/7` | 1.033976 | A xenoarchaeologist studying the ruins beneath  Murthal, dodging ancient traps and uncovering relics  deep within its forgotten tombs. |
| 2 | `PZO22001 Starfinder Player Core 030-039::/page/4/ListItem/13` | 0.712735 | A xenoarchaeologist exploring the planet's hollow interior  and cataloging the strange ruins and dangerous creatures  that lurk within. |
| 3 | `PZO22001 Starfinder Player Core 030-039::/page/3/Text/2` | 0.525676 | In the modern era, bone sages rule scattered fiefdoms  on Eox's irradiated surface, and hordes of mindless undead  wander the wastes outside magical bunkers and walled  necropolises. Many are tragic b |
| 4 | `PZO22001 Starfinder Player Core 030-039::/page/3/Text/3` | 0.481317 | Notable locations on Eox include the undying capital of  Orphys, a grim metropolis of bone spires, blood aqueducts,  and funerary gardens; the Necroforges of the Lifeline,  a walled complex peddling i |
| 5 | `PZO22001 Starfinder Player Core 030-039::/page/1/ListItem/8` | 0.469533 | A Starfinder exploring magitech ruins left by the  First Ones, risking encounters with deadly traps and  terrifying sentries. |
| 6 | `PZO22001 Starfinder Player Core 030-039::/page/1/ListItem/9` | 0.458567 | A Xenowarden nurturing bizarre flora and fauna  deep inside secluded Ice Wells and undermining local  industry. |
| 7 | `PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/12` | 0.444791 | A curious contemplative, recording every detail  observed while exploring the Wreck of the Returned. |
| 8 | `PZO22001 Starfinder Player Core 030-039::/page/2/ListItem/3` | 0.444017 | A ghost courier, exploring the Ghost Levels on a hunt  for valuable relics, surviving dangerous anomalies and  fighting dimensionally displaced monsters. |
| 9 | `PZO22001 Starfinder Player Core 030-039::/page/4/ListItem/23` | 0.424864 | A mystic wandering the wastes ravaged by the Shriek,  seeking natural ways to heal your war-torn ancestral lands. |
| 10 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/14` | 0.424238 | Castrovel's regions include Asana and its major spaceport  Qabarat, a beautiful living monument of ancient walls of  crushed shells cradling a modern metropolis; the towering  hive-city of Queensrock |

### Query 99
- Text: Summarize TRIAXUS
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 030-039::/page/3/SectionHeader/8']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 030-039::/page/3/SectionHeader/8', 'PZO22001 Starfinder Player Core 030-039::/page/3/Text/11', 'PZO22001 Starfinder Player Core 030-039::/page/3/Text/10']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 030-039::/page/3/SectionHeader/8` | 0.961972 | TRIAXUS |
| 2 | `PZO22001 Starfinder Player Core 030-039::/page/3/Text/11` | 0.543008 | Triaxus is defended by the Skyfire Legion, an ancient  military order formed by dragonkin troopers and their  bonded humanoid partners, all supported by powerful  dragon allies. |
| 3 | `PZO22001 Starfinder Player Core 030-039::/page/3/Text/10` | 0.512397 | Once, Triaxus's wandering orbit created an intense seasonal  cycle of steamy, fertile summers and brutal winters that  lasted hundreds of years. The planet's ecologies, landscape,  and inhabitants cha |
| 4 | `PZO22001 Starfinder Player Core 030-039::/page/3/Text/12` | 0.472842 | Regions on Triaxus include the Drakelands, a continental  wilderness preserve tended by dragons; the Skyfire Mandate,  an isthmus guarded by the oldest aeries of the Skyfire Legion;  the Allied Territ |
| 5 | `PZO22001 Starfinder Player Core 030-039::/page/6/SectionHeader/29` | 0.374220 | HYLAX |
| 6 | `PZO22001 Starfinder Player Core 030-039::/page/5/Text/64` | 0.320453 | **APPENDIX** |
| 7 | `PZO22001 Starfinder Player Core 030-039::/page/8/Text/17` | 0.297025 | Triune is a fusion of the three technological  deities Epoch, Brigh, and Casandalee. Triune's Signal made  Drift travel possible. |
| 8 | `PZO22001 Starfinder Player Core 030-039::/page/2/SectionHeader/35` | 0.294555 | EOX |
| 9 | `PZO22001 Starfinder Player Core 030-039::/page/0/SectionHeader/1` | 0.253764 | EXPLORING THE  GALAXY |
| 10 | `PZO22001 Starfinder Player Core 030-039::/page/1/Text/40` | 0.246996 | **CONDITIONS ** **APPENDIX** |
