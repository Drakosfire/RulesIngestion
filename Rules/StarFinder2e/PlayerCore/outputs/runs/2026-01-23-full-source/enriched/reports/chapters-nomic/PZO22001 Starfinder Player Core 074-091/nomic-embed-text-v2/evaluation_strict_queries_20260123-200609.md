# RulesLawyer Evaluation Report: nomic-embed-text-v2

## Summary
- Run ID: `None`
- Ruleset ID: `None`
- Document ID: `None`
- Chunk source: `enriched`
- Chunk count: `699`
- Query count: `150`
- Evaluated queries: `150`
- Coverage: `1.0000`
- MRR: `0.8786`
- hit@1: `0.8067`
- hit@3: `0.9467`
- hit@5: `0.9800`
- hit@10: `1.0000`
- Embeddings reused: `False`
- Graph boost: `0.05` (depth=2, top_k=50, source=top, seed_top_n=3, same_kind_only=False, decay=0.4)

## Timings (ms)
- Embedding (chunks): `11048`
- Embedding (queries): `3299`
- Evaluation (strict): `79`
- Evaluation (expanded): `0`
- Total: `18882`

### Timing Estimates (ms)
- Evaluation (strict): `105`
- Evaluation (expanded): `None`
- Total: `14452`

## Query Details
### Query 0
- Text: Summarize -STARFINDER
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/0/Text/0']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/4/SectionHeader/0', 'PZO22001 Starfinder Player Core 074-091::/page/0/Text/0', 'PZO22001 Starfinder Player Core 074-091::/page/8/Text/6']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/4/SectionHeader/0` | 0.949063 | -STARFINDER |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/0/Text/0` | 0.949063 | -STARFINDER |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/8/Text/6` | 0.432972 | Two notable heritages in the Starfinder setting are prismeni,  born from the subtle influences of the hyperspace dimension  of the Drift or otherwise influenced by it, and borai, individuals  who surv |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/14/ListItem/7` | 0.360981 | Have an instinctive understanding of technology,  especially starships. |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/6/Text/2` | 0.338613 | Ysoki are sometimes referred to as ratfolk by other  ancestries and use the ratfolk trait. This was especially  true in the distant past. In Starfinder, individuals of  this ancestry are more commonly |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/15/Text/41` | 0.324833 | **Shirren** **Skittermander** |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/14/ListItem/12` | 0.320368 | Count on you to pilot the party's starship, navigate, or  maybe even act as the living Drift engine. |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/17/Text/60` | 0.304017 | **Skittermander** |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/38` | 0.304017 | **Skittermander** |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/9/Text/27` | 0.304017 | **Skittermander** |

### Query 1
- Text: Summarize VESK
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/0/SectionHeader/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/0/SectionHeader/1', 'PZO22001 Starfinder Player Core 074-091::/page/2/Text/15', 'PZO22001 Starfinder Player Core 074-091::/page/3/Text/43']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/0/SectionHeader/1` | 0.903355 | VESK |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/2/Text/15` | 0.833880 | **VESK** |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/43` | 0.833880 | **VESK** |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/3/SectionHeader/26` | 0.791880 | **VESK** |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/61` | 0.791880 | **VESK** |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/39` | 0.791880 | **VESK** |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/57` | 0.791880 | **VESK** |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/2/Text/23` | 0.791880 | **VESK** |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/3/SectionHeader/15` | 0.791880 | **VESK** |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/2/Text/11` | 0.791880 | **VESK** |

### Query 2
- Text: What is the rule about Vesk are a warmongering, reptilian people who conquered the eight worlds in their solar system shortly after they developed spaceflight, forming the Veskarium empire. Vesk tend to embrace conflict and respect strength and military might.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/0/Text/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/0/Text/2', 'PZO22001 Starfinder Player Core 074-091::/page/1/Text/15', 'PZO22001 Starfinder Player Core 074-091::/page/1/Text/9']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/0/Text/2` | 0.981797 | Vesk are a warmongering, reptilian people who conquered the eight worlds in their solar system shortly after they developed spaceflight, forming the Veskarium empire. Vesk tend to embrace conflict and |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/15` | 0.827094 | Vesk society is highly organized and militaristic. Vesk first  dwelled on a single planet but quickly spread to other worlds  in their system. Today, the name for these conquered worlds  is the Veskar |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/9` | 0.796330 | Vesk have a long history of conflict, first as conquerors within  their own star system and later clashing with neighboring  stellar powers such as the Pact Worlds and the Swarm.  Currently, the Veska |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/1/SectionHeader/18` | 0.676327 | Most vesk in the Veskarium venerate Damoritosh the  Conqueror, god of duty and war, and his army of battle  saints. In life, the saints were mortal paragons who embodied  vesk cultural values and atta |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/56` | 0.652949 | and conflicts within the Veskarium tend to be as disciplined  as they are violent, stretching to accommodate opposing  sides following the prescribed order of war. A typical vesk  always respects thei |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/22` | 0.612588 | Vesk lineages were shaped by the worlds they inhabited and  battled over. Choose one of the following vesk heritages at  1st level. |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/10` | 0.592419 | If you want a character who's duty bound, brave, and stoic,  you should play a vesk. |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/16` | 0.576403 | Vesk names typically combine elements of their parents'  names as well as those of other prominent ancestors.  Companions often shorten these names for casual use, but  doing so without permission is |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/13` | 0.554259 | Vesk adopted tech weapons early in their history but retain  the brutal claws and teeth of natural predators. They take  great care in grooming and painting their scales and claws to  showcase their p |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/2/Text/7` | 0.527065 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As a vesk, you choose from among the  following ance |

### Query 3
- Text: Summarize SIZE: MEDIUM SPEED: 20 FEET
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/0/Text/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/0/Text/5', 'PZO22001 Starfinder Player Core 074-091::/page/4/Text/5', 'PZO22001 Starfinder Player Core 074-091::/page/17/Text/69']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/0/Text/5` | 1.022145 | SIZE: MEDIUM SPEED: 20 FEET |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/4/Text/5` | 0.750433 | SIZE: SMALL SPEED: 25 FEET |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/17/Text/69` | 0.453436 | **FEATS** **EQUIPMENT** |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/17/SectionHeader/25` | 0.352319 | **FREQUENT DRIFTER** **FEAT 13** |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/76` | 0.348729 | **FEATS** |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/5/Text/52` | 0.348729 | **FEATS** |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/72` | 0.348729 | **FEATS** |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/47` | 0.348729 | **FEATS** |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/84` | 0.348729 | **FEATS** |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/15/Text/50` | 0.340731 | **SKILLS** **FEATS** |

### Query 4
- Text: Summarize ATTRIBUTE BOOSTS Constitution Strength Free
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/0/Text/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/0/Text/6', 'PZO22001 Starfinder Player Core 074-091::/page/4/Text/6', 'PZO22001 Starfinder Player Core 074-091::/page/4/Text/7']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/0/Text/6` | 1.010270 | ATTRIBUTE BOOSTS Constitution Strength Free |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/4/Text/6` | 0.628429 | ATTRIBUTE BOOSTS Dexterity Intelligence Free |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/4/Text/7` | 0.567113 | ATTRIBUTE FLAW Strength |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/12/Text/39` | 0.369798 | Your soul is radiant and can sustain your living body  indefinitely, without the need for outside nourishment. You  don't need to eat or drink, and you count your Constitution |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/3/SectionHeader/59` | 0.353064 | **BOLSTERED BY BATTLE **[free-action] **FEAT 17** |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/0/Text/7` | 0.345605 | ATTRIBUTE FLAW Wisdom |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/12/SectionHeader/32` | 0.333266 | **DEATHLY CONSTITUTION** **FEAT 5** |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/12/Text/35` | 0.324795 | Thanks to your life-altering brush with death, your living  body is better protected against the weaknesses of the  flesh. You gain a +1 circumstance bonus to Fortitude  saves against disease and pois |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/17/Text/11` | 0.309894 | The Drift revitalizes your spirit and restores your vitality,  physically healing your wounds. If you rest for 10 minutes  while within the Drift, you gain Hit Points equal to your  Constitution modif |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/72` | 0.298578 | **Backgrounds** |

### Query 5
- Text: Summarize ATTRIBUTE FLAW Wisdom
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/0/Text/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/0/Text/7', 'PZO22001 Starfinder Player Core 074-091::/page/4/Text/7', 'PZO22001 Starfinder Player Core 074-091::/page/13/Text/38']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/0/Text/7` | 1.001491 | ATTRIBUTE FLAW Wisdom |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/4/Text/7` | 0.734297 | ATTRIBUTE FLAW Strength |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/38` | 0.401468 | You're willful and stubborn, and you refuse to accept your  own failure—traits that have served you well in life and after  death. When you critically fail a saving throw against a  mental effect, you |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/4/Text/6` | 0.339140 | ATTRIBUTE BOOSTS Dexterity Intelligence Free |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/0/Text/6` | 0.323971 | ATTRIBUTE BOOSTS Constitution Strength Free |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/39` | 0.304047 | **Deny Failure** [reaction] (fortune) **Frequency** once per day; **Trigger** You fail or critically fail a saving throw; **Effect** You refuse  to accept your failure! Reroll the triggering saving th |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/53` | 0.297342 | You clear your mind of distractions and focus on your foe,  determined to overcome the shame of your failure lest it  forever blemish your reputation. The next time before the end  of your turn that y |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/2/Text/17` | 0.296565 | A claw unarmed attack deals 1d6 slashing damage and has  the agile, finesse, unarmed, and vesk traits. |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/4/SectionHeader/10` | 0.293634 | **TRAITS ** |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/17/Text/43` | 0.286056 | **Failure** You teleport the creature up to the noted distance. **Critical Failure** As failure, but the distance you can teleport  the creature is doubled. |

### Query 6
- Text: Summarize LANGUAGES Common, Vesk
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/0/SectionHeader/8']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/0/SectionHeader/8', 'PZO22001 Starfinder Player Core 074-091::/page/0/SectionHeader/1', 'PZO22001 Starfinder Player Core 074-091::/page/3/Text/43']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/0/SectionHeader/8` | 0.993413 | LANGUAGES Common, Vesk |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/0/SectionHeader/1` | 0.663683 | VESK |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/43` | 0.642909 | **VESK** |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/39` | 0.600909 | **VESK** |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/2/Text/11` | 0.600909 | **VESK** |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/2/Text/31` | 0.600909 | **VESK** |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/2/Text/23` | 0.600909 | **VESK** |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/2/Text/15` | 0.600909 | **VESK** |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/3/SectionHeader/5` | 0.600909 | **VESK** |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/3/SectionHeader/15` | 0.600909 | **VESK** |

### Query 7
- Text: What is the rule about One regional language of your choice?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/0/Text/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/0/Text/9', 'PZO22001 Starfinder Player Core 074-091::/page/4/Text/9', 'PZO22001 Starfinder Player Core 074-091::/page/9/Text/2']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/0/Text/9` | 0.661015 | One regional language of your choice Additional languages equal to your Intelligence modifier (if it's positive). Choose from the list of common languages and any other languages to which you have acc |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/4/Text/9` | 0.541620 | Additional languages equal to your Intelligence modifier (if it's positive). Choose from the list of common languages and any other languages to which you have access (such as the languages prevalent |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/9/Text/2` | 0.429775 | Sometimes a versatile heritage might give you an ability that  conflicts with an ability from your ancestry. In these cases, you  choose which of the conflicting abilities your character has. |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/9/Text/1` | 0.387544 | Since a versatile heritage is a heritage, you can have only  one, and you can't have any other heritage in addition to your  versatile heritage. |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/17/Text/66` | 0.381536 | **Languages** |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/15/Text/48` | 0.381536 | **Languages** |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/82` | 0.381536 | **Languages** |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/44` | 0.381536 | **Languages** |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/73` | 0.381536 | **Languages** |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/9/Text/34` | 0.381536 | **Languages** |

### Query 8
- Text: What is the rule about TRAITS?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/0/SectionHeader/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/0/SectionHeader/10', 'PZO22001 Starfinder Player Core 074-091::/page/4/SectionHeader/10', 'PZO22001 Starfinder Player Core 074-091::/page/9/Text/5']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/0/SectionHeader/10` | 0.800446 | TRAITS |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/4/SectionHeader/10` | 0.776531 | **TRAITS ** |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/9/Text/5` | 0.530349 | Some ancestry feats within a versatile heritage have the  lineage trait. These feats specify a physiological lineage your  character has—such as if a prismeni was born in the Drift or  chosen by Triun |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/9/Text/7` | 0.434023 | This book includes the rules for two kinds of versatile  heritages and rules for other mixed ancestral heritages. |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/9/Text/2` | 0.413951 | Sometimes a versatile heritage might give you an ability that  conflicts with an ability from your ancestry. In these cases, you  choose which of the conflicting abilities your character has. |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/9/Text/3` | 0.389763 | When selecting ancestry feats, you can choose from those  available to your ancestry as well as those specific to your  versatile heritage. |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/9/Text/36` | 0.385458 | **SKILLS** **FEATS** |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/15/Text/50` | 0.385458 | **SKILLS** **FEATS** |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/8/Text/11` | 0.385236 | To play a character with a versatile heritage, first select your  ancestry, just like you would for any character. You gain  Hit Points, size, Speed, attribute boosts and attribute flaws,  languages, |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/9/Text/17` | 0.371475 | **Custom Mixed Heritage:** You can work with your GM to  create a mixed heritage for any ancestry. A custom mixedancestry heritage is an uncommon heritage. Choose an  ancestry to tie to the heritage. |

### Query 9
- Text: Summarize HUMANOID VESK
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/0/Text/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/0/Text/11', 'PZO22001 Starfinder Player Core 074-091::/page/0/SectionHeader/1', 'PZO22001 Starfinder Player Core 074-091::/page/2/SectionHeader/1']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/0/Text/11` | 0.972648 | HUMANOID VESK |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/0/SectionHeader/1` | 0.670654 | VESK |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/2/SectionHeader/1` | 0.650465 | VENOMTHOUGHT VESK |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/1/SectionHeader/27` | 0.593869 | PLATED VESK |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/63` | 0.576838 | **Vesk** |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/68` | 0.576838 | **Vesk** |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/76` | 0.576838 | **Vesk** |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/9/Text/28` | 0.576838 | **Vesk** |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/5/Text/44` | 0.576838 | **Vesk** |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/39` | 0.576838 | **Vesk** |

### Query 10
- Text: Summarize LOW-LIGHT VISION
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/0/SectionHeader/12']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/0/SectionHeader/12', 'PZO22001 Starfinder Player Core 074-091::/page/4/SectionHeader/12', 'PZO22001 Starfinder Player Core 074-091::/page/15/Text/12']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/0/SectionHeader/12` | 0.973635 | LOW-LIGHT VISION |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/4/SectionHeader/12` | 0.929136 | **LOW-LIGHT VISION ** |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/15/Text/12` | 0.492239 | travels via conventional thrusters, as normal. When you  get a critical failure on a Piloting check to Navigate or Plot  Course through the Drift, you get a failure instead. You gain  low-light vision |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/26` | 0.377166 | You've adapted to live in darkness, perhaps due to living  underground, in dim starship corridors, under smokeshrouded skies, or on a planet far from its sun. You gain  darkvision. |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/5/Text/29` | 0.361092 | You're accustomed to living in dark places, such as  maintenance shafts, asteroids, and on distant moons and  planetoids far from the sun. You gain darkvision. |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/44` | 0.354008 | **Prerequisites** Baleful Gaze |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/0/Text/13` | 0.351854 | You can see in dim light as though it were bright light, and you ignore the concealed condition due to dim light. |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/4/Text/13` | 0.351854 | You can see in dim light as though it were bright light, and you ignore the concealed condition due to dim light. |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/17/Text/21` | 0.343353 | **PRISMENI** **VISUAL** |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/15/Text/19` | 0.320503 | **CONCENTRATE** **LIGHT** **LINEAGE** **PRISMENI** |

### Query 11
- Text: Summarize You can see in dim light as though it were bright light, and you ignore the concealed condition due to dim light.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/0/Text/13']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/4/Text/13', 'PZO22001 Starfinder Player Core 074-091::/page/0/Text/13', 'PZO22001 Starfinder Player Core 074-091::/page/15/Text/22']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/4/Text/13` | 1.038897 | You can see in dim light as though it were bright light, and you ignore the concealed condition due to dim light. |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/0/Text/13` | 1.038897 | You can see in dim light as though it were bright light, and you ignore the concealed condition due to dim light. |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/15/Text/22` | 0.587024 | for 10 feet on each side and dim light for the  next 10 feet. You can ignore any concealment  granted by the barrier. The barrier lasts for |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/26` | 0.516683 | You've adapted to live in darkness, perhaps due to living  underground, in dim starship corridors, under smokeshrouded skies, or on a planet far from its sun. You gain  darkvision. |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/17/Text/23` | 0.498371 | You instinctively encode your presence, obscuring your  identity and scrambling your visual appearance to  technological visual sensors. You become concealed to all |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/17/Text/24` | 0.443106 | technological visual sensors, such as security cameras,  ocular cybernetic augmentations, and the visual processors  of technological constructs, for 1 minute. As the nature of this  effect still leav |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/5/Text/29` | 0.435481 | You're accustomed to living in dark places, such as  maintenance shafts, asteroids, and on distant moons and  planetoids far from the sun. You gain darkvision. |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/20` | 0.423820 | Your mere presence attracts restless spirits, haunted objects,  spiritually active substances, and fragmented souls, like a  magnet attracts metal. You manifest these spirit shards in a  chaotic whirl |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/57` | 0.419229 | Using clever technology, magical talent, a divine blessing,  or uncanny luck, you slip from sight completely, becoming  invisible for 1 minute, or until you take a hostile action,  whichever comes fir |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/17/Text/18` | 0.393730 | You momentarily slip into the Drift, becoming concealed  against the triggering Strike. If the flat check for concealment  fails, the Strike misses you. After resolving the triggering  Strike, you ree |

### Query 12
- Text: Summarize YOU MIGHT...
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/1/SectionHeader/1']
- Expected found: `True`
- Expected rank: `4`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/10/SectionHeader/4', 'PZO22001 Starfinder Player Core 074-091::/page/5/SectionHeader/1', 'PZO22001 Starfinder Player Core 074-091::/page/14/SectionHeader/4']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/10/SectionHeader/4` | 0.903204 | YOU MIGHT... |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/5/SectionHeader/1` | 0.903204 | YOU MIGHT... |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/14/SectionHeader/4` | 0.903204 | YOU MIGHT... |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/1/SectionHeader/1` | 0.861204 | YOU MIGHT... |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/5/SectionHeader/5` | 0.480471 | OTHERS PROBABLY... |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/10/SectionHeader/8` | 0.480471 | OTHERS PROBABLY... |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/14/SectionHeader/8` | 0.480471 | OTHERS PROBABLY... |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/1/SectionHeader/5` | 0.480471 | OTHERS PROBABLY... |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/8/SectionHeader/8` | 0.355134 | UNLIMITED POSSIBILITIES! |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/46` | 0.296898 | **Requirements** You're engaged in combat. |

### Query 13
- Text: Summarize Relish the chance to prove yourself in combat against  worthy opponents.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/1/ListItem/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/1/ListItem/2', 'PZO22001 Starfinder Player Core 074-091::/page/3/Text/46', 'PZO22001 Starfinder Player Core 074-091::/page/1/Text/19']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/1/ListItem/2` | 1.011908 | Relish the chance to prove yourself in combat against  worthy opponents. |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/46` | 0.568012 | **Requirements** You're engaged in combat. |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/19` | 0.541247 | **Popular Edicts** battle honorably, keep private emotions in  check, never show weakness to enemies |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/53` | 0.488404 | You clear your mind of distractions and focus on your foe,  determined to overcome the shame of your failure lest it  forever blemish your reputation. The next time before the end  of your turn that y |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/1/ListItem/8` | 0.485421 | Fear facing you in battle. |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/10/ListItem/5` | 0.470513 | Be determined to succeed and refuse to accept your  own failure or defeat at any cost. |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/2/Text/28` | 0.465921 | Whether it comes from a sense of duty or a desire to  succeed, you rarely flinch when confronted by fearsome  foes. If you roll a success on a saving throw against a fear  effect, you get a critical s |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/28` | 0.461245 | At the start of a combat encounter, if you are aware of your  foes and aren't attempting to Sneak or Hide, you can roll an  Intimidation check for your initiative and can use the result  to Demoralize |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/64` | 0.461041 | You don't just fight because you have to; the threat of battle  and the thrill of victory invigorate you. You gain a number of  temporary Hit Points equal to your level. These temporary  Hit Points la |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/17` | 0.457492 | You laugh at your enemy's failed attempts to bully you,  turning the tables on your foe with a display of terrifying  bravado. You attempt an Intimidation check to Demoralize  the triggering creature. |

### Query 14
- Text: Summarize Have a strong sense of duty and honor.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/1/ListItem/3']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/1/ListItem/3', 'PZO22001 Starfinder Player Core 074-091::/page/1/Text/10', 'PZO22001 Starfinder Player Core 074-091::/page/1/ListItem/6']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/1/ListItem/3` | 1.019187 | Have a strong sense of duty and honor. |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/10` | 0.558930 | If you want a character who's duty bound, brave, and stoic,  you should play a vesk. |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/1/ListItem/6` | 0.538316 | Respect and fear your brutal reputation but appreciate  your strength as an ally. |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/19` | 0.486309 | **Popular Edicts** battle honorably, keep private emotions in  check, never show weakness to enemies |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/1/SectionHeader/18` | 0.442021 | Most vesk in the Veskarium venerate Damoritosh the  Conqueror, god of duty and war, and his army of battle  saints. In life, the saints were mortal paragons who embodied  vesk cultural values and atta |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/5/Text/22` | 0.426627 | **Popular Edicts** maintain good personal hygiene, put your  community's needs above your own, stay in touch with  friends, take care of your family |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/1/ListItem/2` | 0.426587 | Relish the chance to prove yourself in combat against  worthy opponents. |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/5/ListItem/8` | 0.424612 | Depend on you to stick up for others and always get  the job done. |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/10/ListItem/5` | 0.419252 | Be determined to succeed and refuse to accept your  own failure or defeat at any cost. |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/46` | 0.415765 | **Requirements** You're engaged in combat. |

### Query 15
- Text: Summarize Surprise your companions with tenderness and  emotional outbursts in private.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/1/ListItem/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/1/ListItem/4', 'PZO22001 Starfinder Player Core 074-091::/page/10/ListItem/10', 'PZO22001 Starfinder Player Core 074-091::/page/1/Text/19']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/1/ListItem/4` | 1.030985 | Surprise your companions with tenderness and  emotional outbursts in private. |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/10/ListItem/10` | 0.477512 | Find your presence unnerving, even if they can't  pinpoint why. |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/19` | 0.431917 | **Popular Edicts** battle honorably, keep private emotions in  check, never show weakness to enemies |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/17` | 0.376691 | You laugh at your enemy's failed attempts to bully you,  turning the tables on your foe with a display of terrifying  bravado. You attempt an Intimidation check to Demoralize  the triggering creature. |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/20` | 0.372591 | Your mere presence attracts restless spirits, haunted objects,  spiritually active substances, and fragmented souls, like a  magnet attracts metal. You manifest these spirit shards in a  chaotic whirl |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/12` | 0.366501 | You snarl, hiss, shout, or otherwise verbally menace the  triggering creature as you frighten them. Increase the value  of the frightened condition by 1. |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/10/ListItem/6` | 0.363588 | Seek life-affirming experiences and relationships,  perhaps even recklessly or to your own detriment. |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/14/ListItem/10` | 0.363287 | Expect you to worship Triune or be close friends with  a spectra. |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/14/Text/16` | 0.356167 | control and understand technology or speak wirelessly  with technological creatures. Some can create and harness  electricity. To many prismenis, entering the Drift feels  like coming home, and most d |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/5/Text/14` | 0.352242 | Ysoki instinctually maintain cleanliness through personal  grooming and reinforce these habits throughout their strong  social structures. Many ysoki use cosmetics to spice up their  looks and favor c |

### Query 16
- Text: Summarize OTHERS PROBABLY...
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/1/SectionHeader/5']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/5/SectionHeader/5', 'PZO22001 Starfinder Player Core 074-091::/page/1/SectionHeader/5', 'PZO22001 Starfinder Player Core 074-091::/page/14/SectionHeader/8']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/5/SectionHeader/5` | 0.892334 | OTHERS PROBABLY... |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/14/SectionHeader/8` | 0.892334 | OTHERS PROBABLY... |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/1/SectionHeader/5` | 0.892334 | OTHERS PROBABLY... |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/10/SectionHeader/8` | 0.850334 | OTHERS PROBABLY... |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/14/SectionHeader/4` | 0.494970 | YOU MIGHT... |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/1/SectionHeader/1` | 0.494970 | YOU MIGHT... |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/10/SectionHeader/4` | 0.494970 | YOU MIGHT... |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/5/SectionHeader/1` | 0.494970 | YOU MIGHT... |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/8/SectionHeader/8` | 0.339724 | UNLIMITED POSSIBILITIES! |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/5/Text/23` | 0.311884 | **Popular Anathema** throw away something that might be  useful later |

### Query 17
- Text: Summarize Respect and fear your brutal reputation but appreciate  your strength as an ally.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/1/ListItem/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/1/ListItem/6', 'PZO22001 Starfinder Player Core 074-091::/page/1/ListItem/3', 'PZO22001 Starfinder Player Core 074-091::/page/1/Text/20']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/1/ListItem/6` | 1.028748 | Respect and fear your brutal reputation but appreciate  your strength as an ally. |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/1/ListItem/3` | 0.561686 | Have a strong sense of duty and honor. |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/20` | 0.557445 | **Popular Anathema** betray an ally, give up the fight |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/19` | 0.505807 | **Popular Edicts** battle honorably, keep private emotions in  check, never show weakness to enemies |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/1/ListItem/8` | 0.465931 | Fear facing you in battle. |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/2/Text/28` | 0.462396 | Whether it comes from a sense of duty or a desire to  succeed, you rarely flinch when confronted by fearsome  foes. If you roll a success on a saving throw against a fear  effect, you get a critical s |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/23` | 0.459392 | You eagerly stride into battle, giving no thought to the  consequences. You Stride in a straight line directly toward an  enemy. |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/10/ListItem/5` | 0.448644 | Be determined to succeed and refuse to accept your  own failure or defeat at any cost. |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/1/ListItem/2` | 0.445620 | Relish the chance to prove yourself in combat against  worthy opponents. |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/15/Text/4` | 0.439769 | recovered from a significant failure, or  achieved something great. They collect  nicknames and appellations, accepting  those given to them by friends and  chosen for themselves. |

### Query 18
- Text: Summarize Mistake your stoicism for heartlessness.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/1/ListItem/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/1/ListItem/7', 'PZO22001 Starfinder Player Core 074-091::/page/14/ListItem/11', 'PZO22001 Starfinder Player Core 074-091::/page/13/Text/38']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/1/ListItem/7` | 1.024233 | Mistake your stoicism for heartlessness. |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/14/ListItem/11` | 0.451995 | Consider you restless, flighty, or irresponsible. |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/38` | 0.448583 | You're willful and stubborn, and you refuse to accept your  own failure—traits that have served you well in life and after  death. When you critically fail a saving throw against a  mental effect, you |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/20` | 0.361497 | Your mere presence attracts restless spirits, haunted objects,  spiritually active substances, and fragmented souls, like a  magnet attracts metal. You manifest these spirit shards in a  chaotic whirl |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/11/Text/15` | 0.357954 | You became a borai through a botched resurrection  attempt—perhaps a magic spell was disrupted, a religious  rite went awry, or faulty technology went haywire, resulting  in your condition. Your soul |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/12/Text/4` | 0.353523 | You became a borai through your own stubborn willfulness.  When you died, you refused to accept your death and clung  to your corpse, forcing your soul back into your body and  regaining life along wi |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/51` | 0.351404 | You have died once before and have no intention of dying  ever again; your soul stubbornly resuscitates your body  when you would otherwise perish. You are restored to 1  Hit Point, lose the dying and |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/53` | 0.350471 | You clear your mind of distractions and focus on your foe,  determined to overcome the shame of your failure lest it  forever blemish your reputation. The next time before the end  of your turn that y |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/12/Text/14` | 0.346514 | You have an ominous presence that unnerves the living.  You have learned to harness this sinister aura to your  own advantage and can scare your foes with a focused  glance. Focus your ill intent at o |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/10/ListItem/11` | 0.343889 | Seek your advice about grief, loss, death, and the  afterlife. |

### Query 19
- Text: What is the rule about Fear facing you in battle.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/1/ListItem/8']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/1/ListItem/8', 'PZO22001 Starfinder Player Core 074-091::/page/3/Text/23', 'PZO22001 Starfinder Player Core 074-091::/page/2/Text/28']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/1/ListItem/8` | 0.871869 | Fear facing you in battle. |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/23` | 0.542079 | You eagerly stride into battle, giving no thought to the  consequences. You Stride in a straight line directly toward an  enemy. |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/2/Text/28` | 0.532237 | Whether it comes from a sense of duty or a desire to  succeed, you rarely flinch when confronted by fearsome  foes. If you roll a success on a saving throw against a fear  effect, you get a critical s |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/12/Text/14` | 0.472437 | You have an ominous presence that unnerves the living.  You have learned to harness this sinister aura to your  own advantage and can scare your foes with a focused  glance. Focus your ill intent at o |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/10/ListItem/7` | 0.456570 | Fear what killed you or avoid the place you died, or  feel mysteriously drawn back to it. |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/15` | 0.455192 | When you're physically outmatched, you fight with  unexpected ferocity. If a foe of a larger size than you  critically hits and damages you, that foe is off-guard to you  for 1 round. |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/19` | 0.448527 | **Popular Edicts** battle honorably, keep private emotions in  check, never show weakness to enemies |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/17` | 0.448352 | You laugh at your enemy's failed attempts to bully you,  turning the tables on your foe with a display of terrifying  bravado. You attempt an Intimidation check to Demoralize  the triggering creature. |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/11` | 0.447193 | **Trigger** You frighten a creature. |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/12/Text/16` | 0.427311 | higher of your class DC or spell DC, or become frightened  1 (frightened 2 on a critical failure) and stupefied 1 as long  as it's frightened. Once you've used Baleful Gaze against a  creature, it's t |

### Query 20
- Text: Summarize BELIEFS
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/1/Text/55']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/5/SectionHeader/20', 'PZO22001 Starfinder Player Core 074-091::/page/1/Text/55', 'PZO22001 Starfinder Player Core 074-091::/page/11/SectionHeader/3']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/5/SectionHeader/20` | 0.920612 | BELIEFS |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/55` | 0.920612 | BELIEFS |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/11/SectionHeader/3` | 0.920612 | BELIEFS |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/15/SectionHeader/6` | 0.878612 | BELIEFS |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/44` | 0.306059 | **Prerequisites** Baleful Gaze |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/20` | 0.289373 | **Popular Anathema** betray an ally, give up the fight |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/11/Text/5` | 0.288111 | **Popular Edicts** embrace being alive, learn from your past,  refuse to accept death as the end |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/15/Text/8` | 0.273342 | **Popular Edicts** break with tradition, trust  your feelings, visit new places |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/15/Text/50` | 0.264874 | **SKILLS** **FEATS** |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/9/Text/36` | 0.264874 | **SKILLS** **FEATS** |

### Query 21
- Text: What is the rule about Vesk have a long history of conflict, first as conquerors within  their own star system and later clashing with neighboring  stellar powers such as the Pact Worlds and the Swarm.  Currently, the Veskarium is at war with the Azlanti Star  Empire. Conflict permeates most aspects of vesk cultures,  creating powerful militaristic empires devoted to the bloody  worship of their warrior god Damoritosh. Their brutal history  and militaristic values shape vesk, who often embrace conflict  and value strength, duty, and a personal code of honor.  Individual vesk are just as likely to apply these cultural values  to other aspects of life besides battle, notably in business and  sport, and some vesk might abandon or oppose the ruthless  values enforced by the rulers of their home worlds entirely.  It's up to each vesk to claim their role as a conqueror or a  collaborator—or something else entirely.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/1/Text/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/1/Text/9', 'PZO22001 Starfinder Player Core 074-091::/page/1/SectionHeader/18', 'PZO22001 Starfinder Player Core 074-091::/page/1/Text/15']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/9` | 1.009153 | Vesk have a long history of conflict, first as conquerors within  their own star system and later clashing with neighboring  stellar powers such as the Pact Worlds and the Swarm.  Currently, the Veska |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/1/SectionHeader/18` | 0.814138 | Most vesk in the Veskarium venerate Damoritosh the  Conqueror, god of duty and war, and his army of battle  saints. In life, the saints were mortal paragons who embodied  vesk cultural values and atta |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/15` | 0.763638 | Vesk society is highly organized and militaristic. Vesk first  dwelled on a single planet but quickly spread to other worlds  in their system. Today, the name for these conquered worlds  is the Veskar |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/0/Text/2` | 0.701468 | Vesk are a warmongering, reptilian people who conquered the eight worlds in their solar system shortly after they developed spaceflight, forming the Veskarium empire. Vesk tend to embrace conflict and |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/56` | 0.652828 | and conflicts within the Veskarium tend to be as disciplined  as they are violent, stretching to accommodate opposing  sides following the prescribed order of war. A typical vesk  always respects thei |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/16` | 0.587244 | Vesk names typically combine elements of their parents'  names as well as those of other prominent ancestors.  Companions often shorten these names for casual use, but  doing so without permission is |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/10` | 0.582494 | If you want a character who's duty bound, brave, and stoic,  you should play a vesk. |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/22` | 0.580093 | Vesk lineages were shaped by the worlds they inhabited and  battled over. Choose one of the following vesk heritages at  1st level. |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/13` | 0.503930 | Vesk adopted tech weapons early in their history but retain  the brutal claws and teeth of natural predators. They take  great care in grooming and painting their scales and claws to  showcase their p |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/5/Text/9` | 0.487392 | Ysoki populations thrived on Akiton, lost Golarion, and several  other worlds for millennia before spaceflight accelerated  cultural exchange in the Pact System. The question of  whether these ethnici |

### Query 22
- Text: What is the rule about If you want a character who's duty bound, brave, and stoic,  you should play a vesk.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/1/Text/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/1/Text/10', 'PZO22001 Starfinder Player Core 074-091::/page/1/SectionHeader/18', 'PZO22001 Starfinder Player Core 074-091::/page/1/Text/56']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/10` | 0.956825 | If you want a character who's duty bound, brave, and stoic,  you should play a vesk. |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/1/SectionHeader/18` | 0.643755 | Most vesk in the Veskarium venerate Damoritosh the  Conqueror, god of duty and war, and his army of battle  saints. In life, the saints were mortal paragons who embodied  vesk cultural values and atta |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/56` | 0.615618 | and conflicts within the Veskarium tend to be as disciplined  as they are violent, stretching to accommodate opposing  sides following the prescribed order of war. A typical vesk  always respects thei |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/9` | 0.542967 | Vesk have a long history of conflict, first as conquerors within  their own star system and later clashing with neighboring  stellar powers such as the Pact Worlds and the Swarm.  Currently, the Veska |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/2/Text/7` | 0.516664 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As a vesk, you choose from among the  following ance |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/2/Text/32` | 0.512374 | You're trained with all doshkos. In addition, you gain access to  all uncommon weapons with the vesk trait. For the purposes  of proficiency, you treat any of these that are martial weapons |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/16` | 0.494232 | Vesk names typically combine elements of their parents'  names as well as those of other prominent ancestors.  Companions often shorten these names for casual use, but  doing so without permission is |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/0/SectionHeader/1` | 0.489564 | VESK |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/0/Text/2` | 0.484083 | Vesk are a warmongering, reptilian people who conquered the eight worlds in their solar system shortly after they developed spaceflight, forming the Veskarium empire. Vesk tend to embrace conflict and |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/2/Text/2` | 0.480581 | You're one of the notable vesk born with psychic talents.  According to folklore, your lineage originated with an  ancient cave-dwelling society on Vesk Prime who modified  themselves with occult ritu |

### Query 23
- Text: Summarize PHYSICAL DESCRIPTION
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/1/SectionHeader/11']
- Expected found: `True`
- Expected rank: `4`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/5/SectionHeader/12', 'PZO22001 Starfinder Player Core 074-091::/page/10/SectionHeader/15', 'PZO22001 Starfinder Player Core 074-091::/page/14/SectionHeader/18']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/5/SectionHeader/12` | 0.971851 | PHYSICAL DESCRIPTION |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/10/SectionHeader/15` | 0.971851 | PHYSICAL DESCRIPTION |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/14/SectionHeader/18` | 0.971851 | PHYSICAL DESCRIPTION |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/1/SectionHeader/11` | 0.929851 | PHYSICAL DESCRIPTION |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/5/Text/34` | 0.335394 | **INTRODUCTION** |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/17/Text/51` | 0.335394 | **INTRODUCTION** |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/9/Text/19` | 0.335394 | **INTRODUCTION** |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/15/Text/33` | 0.335394 | **INTRODUCTION** |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/59` | 0.335394 | **INTRODUCTION** |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/66` | 0.335394 | **INTRODUCTION** |

### Query 24
- Text: What is the rule about Vesk stand up to 7 feet tall, are generally muscular, and  are covered in tough, scaly skin. Spiky horns grow from  their skulls and form bony "beards" along their jaws that  sometimes extend down their spines to their powerful tails.  Vesk scales are generally shades of green but can also display  vibrant, mottled coloration that's sometimes considered an  indicator of health and attractiveness.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/1/Text/12']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/1/Text/12', 'PZO22001 Starfinder Player Core 074-091::/page/1/Text/13', 'PZO22001 Starfinder Player Core 074-091::/page/1/Text/56']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/12` | 0.985093 | Vesk stand up to 7 feet tall, are generally muscular, and  are covered in tough, scaly skin. Spiky horns grow from  their skulls and form bony "beards" along their jaws that  sometimes extend down the |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/13` | 0.641434 | Vesk adopted tech weapons early in their history but retain  the brutal claws and teeth of natural predators. They take  great care in grooming and painting their scales and claws to  showcase their p |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/56` | 0.604825 | and conflicts within the Veskarium tend to be as disciplined  as they are violent, stretching to accommodate opposing  sides following the prescribed order of war. A typical vesk  always respects thei |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/0/Text/2` | 0.539380 | Vesk are a warmongering, reptilian people who conquered the eight worlds in their solar system shortly after they developed spaceflight, forming the Veskarium empire. Vesk tend to embrace conflict and |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/15` | 0.537493 | Vesk society is highly organized and militaristic. Vesk first  dwelled on a single planet but quickly spread to other worlds  in their system. Today, the name for these conquered worlds  is the Veskar |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/1/SectionHeader/18` | 0.532936 | Most vesk in the Veskarium venerate Damoritosh the  Conqueror, god of duty and war, and his army of battle  saints. In life, the saints were mortal paragons who embodied  vesk cultural values and atta |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/9` | 0.521982 | Vesk have a long history of conflict, first as conquerors within  their own star system and later clashing with neighboring  stellar powers such as the Pact Worlds and the Swarm.  Currently, the Veska |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/28` | 0.503424 | Your ancestors were the hardiest specimens of vesk, having  traveled far and wide while enduring hostile environments.  Your scales count as medium armor in the plate armor group.  They grant a +3 ite |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/10` | 0.490799 | If you want a character who's duty bound, brave, and stoic,  you should play a vesk. |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/22` | 0.483035 | Vesk lineages were shaped by the worlds they inhabited and  battled over. Choose one of the following vesk heritages at  1st level. |

### Query 25
- Text: Summarize Vesk adopted tech weapons early in their history but retain  the brutal claws and teeth of natural predators. They take  great care in grooming and painting their scales and claws to  showcase their personal style and intimidate others.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/1/Text/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/1/Text/13', 'PZO22001 Starfinder Player Core 074-091::/page/1/Text/12', 'PZO22001 Starfinder Player Core 074-091::/page/0/Text/2']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/13` | 1.042732 | Vesk adopted tech weapons early in their history but retain  the brutal claws and teeth of natural predators. They take  great care in grooming and painting their scales and claws to  showcase their p |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/12` | 0.657848 | Vesk stand up to 7 feet tall, are generally muscular, and  are covered in tough, scaly skin. Spiky horns grow from  their skulls and form bony "beards" along their jaws that  sometimes extend down the |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/0/Text/2` | 0.611388 | Vesk are a warmongering, reptilian people who conquered the eight worlds in their solar system shortly after they developed spaceflight, forming the Veskarium empire. Vesk tend to embrace conflict and |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/56` | 0.566850 | and conflicts within the Veskarium tend to be as disciplined  as they are violent, stretching to accommodate opposing  sides following the prescribed order of war. A typical vesk  always respects thei |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/1/SectionHeader/18` | 0.552315 | Most vesk in the Veskarium venerate Damoritosh the  Conqueror, god of duty and war, and his army of battle  saints. In life, the saints were mortal paragons who embodied  vesk cultural values and atta |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/9` | 0.540212 | Vesk have a long history of conflict, first as conquerors within  their own star system and later clashing with neighboring  stellar powers such as the Pact Worlds and the Swarm.  Currently, the Veska |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/16` | 0.520766 | Vesk names typically combine elements of their parents'  names as well as those of other prominent ancestors.  Companions often shorten these names for casual use, but  doing so without permission is |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/15` | 0.520556 | Vesk society is highly organized and militaristic. Vesk first  dwelled on a single planet but quickly spread to other worlds  in their system. Today, the name for these conquered worlds  is the Veskar |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/22` | 0.520309 | Vesk lineages were shaped by the worlds they inhabited and  battled over. Choose one of the following vesk heritages at  1st level. |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/10` | 0.508438 | If you want a character who's duty bound, brave, and stoic,  you should play a vesk. |

### Query 26
- Text: Summarize SOCIETY
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/1/SectionHeader/14']
- Expected found: `True`
- Expected rank: `4`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/5/SectionHeader/15', 'PZO22001 Starfinder Player Core 074-091::/page/14/SectionHeader/20', 'PZO22001 Starfinder Player Core 074-091::/page/10/SectionHeader/18']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/5/SectionHeader/15` | 0.897896 | SOCIETY |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/14/SectionHeader/20` | 0.897896 | SOCIETY |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/10/SectionHeader/18` | 0.897896 | SOCIETY |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/1/SectionHeader/14` | 0.855896 | SOCIETY |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/16/SectionHeader/2` | 0.367040 | **TECH FAMILIARITY** **FEAT 1** |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/5/Text/22` | 0.341615 | **Popular Edicts** maintain good personal hygiene, put your  community's needs above your own, stay in touch with  friends, take care of your family |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/5/Text/21` | 0.336378 | Ysoki care more about their family than abstract moral  concepts, and most ysoki follow their community's strict  social codes even if they break civil laws. Community is  important to all ysoki, and |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/15` | 0.330132 | Vesk society is highly organized and militaristic. Vesk first  dwelled on a single planet but quickly spread to other worlds  in their system. Today, the name for these conquered worlds  is the Veskar |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/10/Text/20` | 0.323303 | Borais who have lived over a decade as undead tend to  consider family a matter of friendship, loyalty, and love  rather than that of genetics or lineage. Adopted families  and sprawling friendship gr |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/14/ListItem/6` | 0.316734 | Love to travel and experience new cultures and  societies. |

### Query 27
- Text: What is the rule about Vesk society is highly organized and militaristic. Vesk first  dwelled on a single planet but quickly spread to other worlds  in their system. Today, the name for these conquered worlds  is the Veskarium, with each given a number to mark their  distance from the sun and order of conquest (such as Vesk-3  or Vesk-8). Vesk Prime, the vesk ancestral home, is the seat of  Veskarium government and the heart of their culture.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/1/Text/15']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/1/Text/15', 'PZO22001 Starfinder Player Core 074-091::/page/0/Text/2', 'PZO22001 Starfinder Player Core 074-091::/page/1/Text/9']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/15` | 1.012321 | Vesk society is highly organized and militaristic. Vesk first  dwelled on a single planet but quickly spread to other worlds  in their system. Today, the name for these conquered worlds  is the Veskar |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/0/Text/2` | 0.786163 | Vesk are a warmongering, reptilian people who conquered the eight worlds in their solar system shortly after they developed spaceflight, forming the Veskarium empire. Vesk tend to embrace conflict and |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/9` | 0.759304 | Vesk have a long history of conflict, first as conquerors within  their own star system and later clashing with neighboring  stellar powers such as the Pact Worlds and the Swarm.  Currently, the Veska |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/1/SectionHeader/18` | 0.634338 | Most vesk in the Veskarium venerate Damoritosh the  Conqueror, god of duty and war, and his army of battle  saints. In life, the saints were mortal paragons who embodied  vesk cultural values and atta |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/22` | 0.632136 | Vesk lineages were shaped by the worlds they inhabited and  battled over. Choose one of the following vesk heritages at  1st level. |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/56` | 0.600274 | and conflicts within the Veskarium tend to be as disciplined  as they are violent, stretching to accommodate opposing  sides following the prescribed order of war. A typical vesk  always respects thei |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/16` | 0.554208 | Vesk names typically combine elements of their parents'  names as well as those of other prominent ancestors.  Companions often shorten these names for casual use, but  doing so without permission is |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/2/Text/7` | 0.528840 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As a vesk, you choose from among the  following ance |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/10` | 0.502905 | If you want a character who's duty bound, brave, and stoic,  you should play a vesk. |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/2/Text/2` | 0.486094 | You're one of the notable vesk born with psychic talents.  According to folklore, your lineage originated with an  ancient cave-dwelling society on Vesk Prime who modified  themselves with occult ritu |

### Query 28
- Text: Summarize Vesk names typically combine elements of their parents'  names as well as those of other prominent ancestors.  Companions often shorten these names for casual use, but  doing so without permission is a grave insult. Some vesk take  on epithets that signify their victories in combat, such as  "Three Guns," "Voidwalker," or "Squadeater."
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/1/Text/16']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/1/Text/16', 'PZO22001 Starfinder Player Core 074-091::/page/2/Text/7', 'PZO22001 Starfinder Player Core 074-091::/page/1/Text/22']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/16` | 1.045312 | Vesk names typically combine elements of their parents'  names as well as those of other prominent ancestors.  Companions often shorten these names for casual use, but  doing so without permission is |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/2/Text/7` | 0.598127 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As a vesk, you choose from among the  following ance |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/22` | 0.595720 | Vesk lineages were shaped by the worlds they inhabited and  battled over. Choose one of the following vesk heritages at  1st level. |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/56` | 0.549281 | and conflicts within the Veskarium tend to be as disciplined  as they are violent, stretching to accommodate opposing  sides following the prescribed order of war. A typical vesk  always respects thei |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/1/SectionHeader/18` | 0.548165 | Most vesk in the Veskarium venerate Damoritosh the  Conqueror, god of duty and war, and his army of battle  saints. In life, the saints were mortal paragons who embodied  vesk cultural values and atta |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/15` | 0.547835 | Vesk society is highly organized and militaristic. Vesk first  dwelled on a single planet but quickly spread to other worlds  in their system. Today, the name for these conquered worlds  is the Veskar |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/9` | 0.547346 | Vesk have a long history of conflict, first as conquerors within  their own star system and later clashing with neighboring  stellar powers such as the Pact Worlds and the Swarm.  Currently, the Veska |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/0/Text/2` | 0.529389 | Vesk are a warmongering, reptilian people who conquered the eight worlds in their solar system shortly after they developed spaceflight, forming the Veskarium empire. Vesk tend to embrace conflict and |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/5/Text/18` | 0.503846 | "Snack," "Dot," "Sparks," or "Boom-Boom." Many ysoki family  names incorporate their ships or home settlements. |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/13` | 0.496798 | Vesk adopted tech weapons early in their history but retain  the brutal claws and teeth of natural predators. They take  great care in grooming and painting their scales and claws to  showcase their p |

### Query 29
- Text: Summarize **Sample Names:** Abazobari, Ahadigar, Asthonad, Dotralan,  Evdokayo, Julukesh, Katara, Obozaya, Oromeras, Radokama,  Sarangari, Sobok, Terikoraz, Vindasorn, Yuluzak
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/1/Text/17']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/1/Text/17', 'PZO22001 Starfinder Player Core 074-091::/page/11/Text/2', 'PZO22001 Starfinder Player Core 074-091::/page/15/Text/5']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/17` | 1.040436 | **Sample Names:** Abazobari, Ahadigar, Asthonad, Dotralan,  Evdokayo, Julukesh, Katara, Obozaya, Oromeras, Radokama,  Sarangari, Sobok, Terikoraz, Vindasorn, Yuluzak |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/11/Text/2` | 0.782826 | **Sample Names:** Agavana, Ajanu, Cailis, Enduri, Jiann,  Kilarra, Orthei, Ruven, Taylehm, Thel-Sevai, Tis, Yevtori |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/15/Text/5` | 0.724342 | **Sample Names:** Anon, Coda, Bellasoar,  Ector, Freedom's Wing, Ilioch, Jalavel,  Ozarin, Red, Sipri, Szazah, Tizera, Una |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/5/Text/19` | 0.587695 | **Sample Names:** Bena, Coponisa, Cors, Datch, Fitch, Goba,  Kib, Lolo, Niknak, Quig, Resk, Sim, Twik |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/22` | 0.417300 | Vesk lineages were shaped by the worlds they inhabited and  battled over. Choose one of the following vesk heritages at  1st level. |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/5/Text/18` | 0.394463 | "Snack," "Dot," "Sparks," or "Boom-Boom." Many ysoki family  names incorporate their ships or home settlements. |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/16` | 0.371478 | Vesk names typically combine elements of their parents'  names as well as those of other prominent ancestors.  Companions often shorten these names for casual use, but  doing so without permission is |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/5/Text/9` | 0.364694 | Ysoki populations thrived on Akiton, lost Golarion, and several  other worlds for millennia before spaceflight accelerated  cultural exchange in the Pact System. The question of  whether these ethnici |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/15/Text/3` | 0.364193 | Prismenis don't follow naming conventions, selecting  names that speak to them on a personal level. Most change  their name at least twice in their life, once to shed the  name given to them by others |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/11/Text/1` | 0.362990 | No widespread naming conventions exist for borais, and  many prefer the name that they used in life. Some borais who  leave behind their old lives adopt new names of their own  creation that they feel |

### Query 30
- Text: What is the rule about Most vesk in the Veskarium venerate Damoritosh the  Conqueror, god of duty and war, and his army of battle  saints. In life, the saints were mortal paragons who embodied  vesk cultural values and attained divinity after earning  Damoritosh's blessing; now they're worshipped alongside  their deity. A typical vesk faces all of life's struggles armed  with ideals of personal honor and strength, recognizing  that not all conflicts occur on the battlefield. Many vesk  find comfort in rigid systems of law, while others hold their  personal sense of morality above all else—in either case, most  vesk don't hesitate to fight for what they believe is right.  Even while fighting, most vesk apply a code to their actions,?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/1/SectionHeader/18']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/1/SectionHeader/18', 'PZO22001 Starfinder Player Core 074-091::/page/1/Text/9', 'PZO22001 Starfinder Player Core 074-091::/page/1/Text/56']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/1/SectionHeader/18` | 1.014606 | Most vesk in the Veskarium venerate Damoritosh the  Conqueror, god of duty and war, and his army of battle  saints. In life, the saints were mortal paragons who embodied  vesk cultural values and atta |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/9` | 0.794429 | Vesk have a long history of conflict, first as conquerors within  their own star system and later clashing with neighboring  stellar powers such as the Pact Worlds and the Swarm.  Currently, the Veska |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/56` | 0.735440 | and conflicts within the Veskarium tend to be as disciplined  as they are violent, stretching to accommodate opposing  sides following the prescribed order of war. A typical vesk  always respects thei |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/10` | 0.618215 | If you want a character who's duty bound, brave, and stoic,  you should play a vesk. |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/15` | 0.604924 | Vesk society is highly organized and militaristic. Vesk first  dwelled on a single planet but quickly spread to other worlds  in their system. Today, the name for these conquered worlds  is the Veskar |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/0/Text/2` | 0.581152 | Vesk are a warmongering, reptilian people who conquered the eight worlds in their solar system shortly after they developed spaceflight, forming the Veskarium empire. Vesk tend to embrace conflict and |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/16` | 0.546499 | Vesk names typically combine elements of their parents'  names as well as those of other prominent ancestors.  Companions often shorten these names for casual use, but  doing so without permission is |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/47` | 0.538261 | You pray to Damoritosh (or a battle saint) for a blessing in the  heat of battle—and he answers. You regain 1 Focus Point, up  to your usual maximum. |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/19` | 0.519996 | **Popular Edicts** battle honorably, keep private emotions in  check, never show weakness to enemies |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/2/Text/32` | 0.515194 | You're trained with all doshkos. In addition, you gain access to  all uncommon weapons with the vesk trait. For the purposes  of proficiency, you treat any of these that are martial weapons |

### Query 31
- Text: What is the rule about **Popular Edicts** battle honorably, keep private emotions in  check, never show weakness to enemies?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/1/Text/19']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/1/Text/19', 'PZO22001 Starfinder Player Core 074-091::/page/5/Text/22', 'PZO22001 Starfinder Player Core 074-091::/page/15/Text/8']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/19` | 0.956361 | **Popular Edicts** battle honorably, keep private emotions in  check, never show weakness to enemies |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/5/Text/22` | 0.622012 | **Popular Edicts** maintain good personal hygiene, put your  community's needs above your own, stay in touch with  friends, take care of your family |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/15/Text/8` | 0.602241 | **Popular Edicts** break with tradition, trust  your feelings, visit new places |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/11/Text/5` | 0.525101 | **Popular Edicts** embrace being alive, learn from your past,  refuse to accept death as the end |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/15/Text/9` | 0.483449 | **Popular Anathema** allow others to dictate  your decisions or impede your freedom |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/20` | 0.450460 | **Popular Anathema** betray an ally, give up the fight |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/1/SectionHeader/18` | 0.448150 | Most vesk in the Veskarium venerate Damoritosh the  Conqueror, god of duty and war, and his army of battle  saints. In life, the saints were mortal paragons who embodied  vesk cultural values and atta |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/5/Text/23` | 0.425177 | **Popular Anathema** throw away something that might be  useful later |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/56` | 0.415997 | and conflicts within the Veskarium tend to be as disciplined  as they are violent, stretching to accommodate opposing  sides following the prescribed order of war. A typical vesk  always respects thei |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/1/ListItem/2` | 0.415417 | Relish the chance to prove yourself in combat against  worthy opponents. |

### Query 32
- Text: What is the rule about and conflicts within the Veskarium tend to be as disciplined  as they are violent, stretching to accommodate opposing  sides following the prescribed order of war. A typical vesk  always respects their opponent and shuns cowardly tactics,?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/1/Text/56']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/1/Text/56', 'PZO22001 Starfinder Player Core 074-091::/page/1/SectionHeader/18', 'PZO22001 Starfinder Player Core 074-091::/page/1/Text/9']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/56` | 1.005119 | and conflicts within the Veskarium tend to be as disciplined  as they are violent, stretching to accommodate opposing  sides following the prescribed order of war. A typical vesk  always respects thei |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/1/SectionHeader/18` | 0.739968 | Most vesk in the Veskarium venerate Damoritosh the  Conqueror, god of duty and war, and his army of battle  saints. In life, the saints were mortal paragons who embodied  vesk cultural values and atta |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/9` | 0.694585 | Vesk have a long history of conflict, first as conquerors within  their own star system and later clashing with neighboring  stellar powers such as the Pact Worlds and the Swarm.  Currently, the Veska |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/10` | 0.597994 | If you want a character who's duty bound, brave, and stoic,  you should play a vesk. |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/15` | 0.571975 | Vesk society is highly organized and militaristic. Vesk first  dwelled on a single planet but quickly spread to other worlds  in their system. Today, the name for these conquered worlds  is the Veskar |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/0/Text/2` | 0.559939 | Vesk are a warmongering, reptilian people who conquered the eight worlds in their solar system shortly after they developed spaceflight, forming the Veskarium empire. Vesk tend to embrace conflict and |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/16` | 0.552819 | Vesk names typically combine elements of their parents'  names as well as those of other prominent ancestors.  Companions often shorten these names for casual use, but  doing so without permission is |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/13` | 0.503547 | Vesk adopted tech weapons early in their history but retain  the brutal claws and teeth of natural predators. They take  great care in grooming and painting their scales and claws to  showcase their p |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/2/Text/32` | 0.488595 | You're trained with all doshkos. In addition, you gain access to  all uncommon weapons with the vesk trait. For the purposes  of proficiency, you treat any of these that are martial weapons |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/12` | 0.487549 | Vesk stand up to 7 feet tall, are generally muscular, and  are covered in tough, scaly skin. Spiky horns grow from  their skulls and form bony "beards" along their jaws that  sometimes extend down the |

### Query 33
- Text: Summarize **Popular Anathema** betray an ally, give up the fight
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/1/Text/20']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/1/Text/20', 'PZO22001 Starfinder Player Core 074-091::/page/5/Text/23', 'PZO22001 Starfinder Player Core 074-091::/page/11/Text/6']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/20` | 1.031568 | **Popular Anathema** betray an ally, give up the fight |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/5/Text/23` | 0.634270 | **Popular Anathema** throw away something that might be  useful later |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/11/Text/6` | 0.579456 | **Popular Anathema** abandon those who accept you as you  are, abstain from life's pleasures |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/15/Text/9` | 0.535643 | **Popular Anathema** allow others to dictate  your decisions or impede your freedom |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/19` | 0.505977 | **Popular Edicts** battle honorably, keep private emotions in  check, never show weakness to enemies |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/1/ListItem/6` | 0.479819 | Respect and fear your brutal reputation but appreciate  your strength as an ally. |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/52` | 0.414027 | **Trigger** You critically fail a Strike against an enemy. |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/17` | 0.409371 | You laugh at your enemy's failed attempts to bully you,  turning the tables on your foe with a display of terrifying  bravado. You attempt an Intimidation check to Demoralize  the triggering creature. |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/39` | 0.402628 | **Deny Failure** [reaction] (fortune) **Frequency** once per day; **Trigger** You fail or critically fail a saving throw; **Effect** You refuse  to accept your failure! Reroll the triggering saving th |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/11/Text/5` | 0.389518 | **Popular Edicts** embrace being alive, learn from your past,  refuse to accept death as the end |

### Query 34
- Text: Summarize such as executing prisoners or harming civilians.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/1/Text/57']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/1/Text/57', 'PZO22001 Starfinder Player Core 074-091::/page/3/Text/63', 'PZO22001 Starfinder Player Core 074-091::/page/7/Text/45']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/57` | 0.955667 | such as executing prisoners or harming civilians. |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/63` | 0.515342 | **Trigger** You deal the killing blow to an enemy. |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/45` | 0.480415 | **Trigger** An enemy occupying the same space as you uses a  manipulate action or a move action, makes a ranged attack,  or leaves a square during a move action it's using. |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/17` | 0.425489 | You laugh at your enemy's failed attempts to bully you,  turning the tables on your foe with a display of terrifying  bravado. You attempt an Intimidation check to Demoralize  the triggering creature. |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/19` | 0.402536 | **Trigger** An enemy's Strike or targeted effect would hit you,  and you weren't already concealed, hidden, or undetected  to that enemy. |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/52` | 0.401355 | **Trigger** You critically fail a Strike against an enemy. |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/17/Text/17` | 0.399456 | **Trigger** An enemy's Strike would hit you, and you weren't  already concealed, hidden, or undetected to that enemy. |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/23` | 0.398625 | You eagerly stride into battle, giving no thought to the  consequences. You Stride in a straight line directly toward an  enemy. |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/1` | 0.396203 | as simple weapons and any that are advanced weapons as  martial weapons. |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/12` | 0.392465 | You snarl, hiss, shout, or otherwise verbally menace the  triggering creature as you frighten them. Increase the value  of the frightened condition by 1. |

### Query 35
- Text: Summarize VESK HERITAGES
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/1/SectionHeader/21']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/1/SectionHeader/21', 'PZO22001 Starfinder Player Core 074-091::/page/0/SectionHeader/1', 'PZO22001 Starfinder Player Core 074-091::/page/2/Text/15']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/1/SectionHeader/21` | 0.984792 | VESK HERITAGES |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/0/SectionHeader/1` | 0.755333 | VESK |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/2/Text/15` | 0.689755 | **VESK** |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/43` | 0.647755 | **VESK** |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/3/SectionHeader/26` | 0.647755 | **VESK** |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/3/SectionHeader/31` | 0.647755 | **VESK** |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/57` | 0.647755 | **VESK** |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/2/Text/31` | 0.647755 | **VESK** |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/3/SectionHeader/5` | 0.647755 | **VESK** |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/3/SectionHeader/15` | 0.647755 | **VESK** |

### Query 36
- Text: Summarize Vesk lineages were shaped by the worlds they inhabited and  battled over. Choose one of the following vesk heritages at  1st level.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/1/Text/22']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/1/Text/22', 'PZO22001 Starfinder Player Core 074-091::/page/1/Text/15', 'PZO22001 Starfinder Player Core 074-091::/page/2/Text/7']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/22` | 1.039190 | Vesk lineages were shaped by the worlds they inhabited and  battled over. Choose one of the following vesk heritages at  1st level. |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/15` | 0.719450 | Vesk society is highly organized and militaristic. Vesk first  dwelled on a single planet but quickly spread to other worlds  in their system. Today, the name for these conquered worlds  is the Veskar |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/2/Text/7` | 0.688599 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As a vesk, you choose from among the  following ance |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/0/Text/2` | 0.639062 | Vesk are a warmongering, reptilian people who conquered the eight worlds in their solar system shortly after they developed spaceflight, forming the Veskarium empire. Vesk tend to embrace conflict and |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/9` | 0.605383 | Vesk have a long history of conflict, first as conquerors within  their own star system and later clashing with neighboring  stellar powers such as the Pact Worlds and the Swarm.  Currently, the Veska |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/5/Text/25` | 0.599405 | Ysoki adapt to almost any environment throughout the  galaxy. Some ysoki put down roots on different worlds or live  entirely on board generation ships that sail the stars. Choose  one of the followin |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/1/SectionHeader/21` | 0.591520 | VESK HERITAGES |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/16` | 0.572960 | Vesk names typically combine elements of their parents'  names as well as those of other prominent ancestors.  Companions often shorten these names for casual use, but  doing so without permission is |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/1/SectionHeader/18` | 0.535646 | Most vesk in the Veskarium venerate Damoritosh the  Conqueror, god of duty and war, and his army of battle  saints. In life, the saints were mortal paragons who embodied  vesk cultural values and atta |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/56` | 0.533453 | and conflicts within the Veskarium tend to be as disciplined  as they are violent, stretching to accommodate opposing  sides following the prescribed order of war. A typical vesk  always respects thei |

### Query 37
- Text: Summarize BRISKWANDER VESK
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/1/SectionHeader/23']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/1/SectionHeader/23', 'PZO22001 Starfinder Player Core 074-091::/page/1/SectionHeader/25', 'PZO22001 Starfinder Player Core 074-091::/page/0/SectionHeader/1']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/1/SectionHeader/23` | 0.981002 | BRISKWANDER VESK |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/1/SectionHeader/25` | 0.559819 | NIGHTSTALKER VESK |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/0/SectionHeader/1` | 0.554478 | VESK |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/2/SectionHeader/3` | 0.509688 | WARBLOOD VESK |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/5/Text/44` | 0.496029 | **Vesk** |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/63` | 0.496029 | **Vesk** |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/68` | 0.496029 | **Vesk** |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/9/Text/28` | 0.496029 | **Vesk** |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/15/Text/42` | 0.496029 | **Vesk** |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/76` | 0.496029 | **Vesk** |

### Query 38
- Text: Summarize You come from a line of vesk who were constantly on the  move. Your Speed increases by 5 feet.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/1/Text/24']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/1/Text/24', 'PZO22001 Starfinder Player Core 074-091::/page/2/Text/7', 'PZO22001 Starfinder Player Core 074-091::/page/16/Text/11']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/24` | 1.039950 | You come from a line of vesk who were constantly on the  move. Your Speed increases by 5 feet. |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/2/Text/7` | 0.539886 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As a vesk, you choose from among the  following ance |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/16/Text/11` | 0.532328 | You travel across the battlefield via the Drift. You  teleport up to a distance equal to your Speed within  your line of sight. If you're in the Drift, the distance you can  teleport is doubled. |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/17/Text/48` | 0.483043 | Whether through a quirk of your bloodline, the interference  of powerful spectra, or Triune's blessing, your body has been  flooded by the essence of the Drift, transforming you into  a spectra. You c |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/17/Text/29` | 0.463298 | Your connection to the Drift grows even stronger, allowing  you to travel through it more often. The frequency of Drift  Hop changes to once per hour. |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/17/Text/5` | 0.457457 | The Drift is your true home, and you can survive within it  indefinitely. While you're in the Drift, you gain the cosmic  trait, and you don't need to eat or drink. While you're in the  Drift or a vac |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/16/Text/15` | 0.456138 | Your body is insulated from electrical attacks.  You gain electricity resistance equal to half  your level. Additionally, you gain the Redirect |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/12` | 0.452775 | Vesk stand up to 7 feet tall, are generally muscular, and  are covered in tough, scaly skin. Spiky horns grow from  their skulls and form bony "beards" along their jaws that  sometimes extend down the |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/23` | 0.447374 | You eagerly stride into battle, giving no thought to the  consequences. You Stride in a straight line directly toward an  enemy. |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/0/Text/2` | 0.444406 | Vesk are a warmongering, reptilian people who conquered the eight worlds in their solar system shortly after they developed spaceflight, forming the Veskarium empire. Vesk tend to embrace conflict and |

### Query 39
- Text: Summarize NIGHTSTALKER VESK
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/1/SectionHeader/25']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/1/SectionHeader/25', 'PZO22001 Starfinder Player Core 074-091::/page/0/SectionHeader/1', 'PZO22001 Starfinder Player Core 074-091::/page/1/SectionHeader/23']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/1/SectionHeader/25` | 0.978448 | NIGHTSTALKER VESK |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/0/SectionHeader/1` | 0.604832 | VESK |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/1/SectionHeader/23` | 0.592135 | BRISKWANDER VESK |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/76` | 0.546812 | **Vesk** |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/63` | 0.546812 | **Vesk** |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/15/Text/42` | 0.546812 | **Vesk** |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/68` | 0.546812 | **Vesk** |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/39` | 0.546812 | **Vesk** |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/9/Text/28` | 0.546812 | **Vesk** |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/5/Text/44` | 0.546812 | **Vesk** |

### Query 40
- Text: Summarize You've adapted to live in darkness, perhaps due to living  underground, in dim starship corridors, under smokeshrouded skies, or on a planet far from its sun. You gain  darkvision.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/1/Text/26']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/1/Text/26', 'PZO22001 Starfinder Player Core 074-091::/page/5/Text/29', 'PZO22001 Starfinder Player Core 074-091::/page/4/Text/13']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/26` | 1.041760 | You've adapted to live in darkness, perhaps due to living  underground, in dim starship corridors, under smokeshrouded skies, or on a planet far from its sun. You gain  darkvision. |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/5/Text/29` | 0.864195 | You're accustomed to living in dark places, such as  maintenance shafts, asteroids, and on distant moons and  planetoids far from the sun. You gain darkvision. |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/4/Text/13` | 0.548655 | You can see in dim light as though it were bright light, and you ignore the concealed condition due to dim light. |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/0/Text/13` | 0.506655 | You can see in dim light as though it were bright light, and you ignore the concealed condition due to dim light. |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/15/Text/12` | 0.481655 | travels via conventional thrusters, as normal. When you  get a critical failure on a Piloting check to Navigate or Plot  Course through the Drift, you get a failure instead. You gain  low-light vision |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/17/Text/5` | 0.480431 | The Drift is your true home, and you can survive within it  indefinitely. While you're in the Drift, you gain the cosmic  trait, and you don't need to eat or drink. While you're in the  Drift or a vac |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/17/Text/48` | 0.471403 | Whether through a quirk of your bloodline, the interference  of powerful spectra, or Triune's blessing, your body has been  flooded by the essence of the Drift, transforming you into  a spectra. You c |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/17/Text/23` | 0.470245 | You instinctively encode your presence, obscuring your  identity and scrambling your visual appearance to  technological visual sensors. You become concealed to all |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/5` | 0.453694 | Some element of your borai nature gives you flashes from  the beyond: visions from the afterlife you were intended for  or might still one day obtain. You gain the trained proficiency  rank in Religio |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/10/Text/19` | 0.449239 | Borais are reanimated all throughout the galaxy, from the  Pact Worlds to the Vast, making them a diverse people with  a scattered population. Most borais are "born" on Eox or on  other planets where |

### Query 41
- Text: Summarize PLATED VESK
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/1/SectionHeader/27']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/1/SectionHeader/27', 'PZO22001 Starfinder Player Core 074-091::/page/0/SectionHeader/1', 'PZO22001 Starfinder Player Core 074-091::/page/3/Text/32']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/1/SectionHeader/27` | 0.990297 | PLATED VESK |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/0/SectionHeader/1` | 0.685286 | VESK |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/32` | 0.649660 | **Prerequisites** plated vesk heritage or Armor Ace |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/0/Text/11` | 0.606566 | HUMANOID VESK |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/2/SectionHeader/1` | 0.595251 | VENOMTHOUGHT VESK |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/5/Text/44` | 0.590005 | **Vesk** |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/63` | 0.590005 | **Vesk** |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/68` | 0.590005 | **Vesk** |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/76` | 0.590005 | **Vesk** |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/39` | 0.590005 | **Vesk** |

### Query 42
- Text: What is the rule about Your ancestors were the hardiest specimens of vesk, having  traveled far and wide while enduring hostile environments.  Your scales count as medium armor in the plate armor group.  They grant a +3 item bonus to AC, have a Dex cap of +1, a check  penalty of –2, and a Strength threshold of +3, and have the  comfort and exposed traits. This item bonus increases to +4 at  5th level. You can wear a flight suit, but you can't wear other  armor. You can etch armor runes (see page 226 of *Pathfinder* *GM* *Core*) onto your scales, but you can't install armor upgrades.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/1/Text/28']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/1/Text/28', 'PZO22001 Starfinder Player Core 074-091::/page/3/Text/33', 'PZO22001 Starfinder Player Core 074-091::/page/2/Text/7']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/28` | 0.993591 | Your ancestors were the hardiest specimens of vesk, having  traveled far and wide while enduring hostile environments.  Your scales count as medium armor in the plate armor group.  They grant a +3 ite |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/33` | 0.598547 | You've mastered using your own plate scales or worn armor  to absorb devastating strikes. You gain the Plate Deflection |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/2/Text/7` | 0.584688 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As a vesk, you choose from among the  following ance |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/32` | 0.524895 | **Prerequisites** plated vesk heritage or Armor Ace |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/6/Text/11` | 0.458568 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th,  9th, 13th, and 17th levels). As a ysoki, you select from  among the following an |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/15/Text/12` | 0.458233 | travels via conventional thrusters, as normal. When you  get a critical failure on a Piloting check to Navigate or Plot  Course through the Drift, you get a failure instead. You gain  low-light vision |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/2/Text/12` | 0.455678 | You've learned through trial and painful error how to make the  most out of your armor, deflecting damage from explosions  and similar effects. When donning armor, you can grant it the  bulwark trait |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/13` | 0.450056 | Vesk adopted tech weapons early in their history but retain  the brutal claws and teeth of natural predators. They take  great care in grooming and painting their scales and claws to  showcase their p |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/15/Text/31` | 0.444239 | Triune chose you specifically to become a  prismeni. You hold the All-Code close in your  heart and cherish the data it's imparted upon  you. You become trained in Religion and Triune  Lore. You have |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/8/Text/11` | 0.442070 | To play a character with a versatile heritage, first select your  ancestry, just like you would for any character. You gain  Hit Points, size, Speed, attribute boosts and attribute flaws,  languages, |

### Query 43
- Text: Summarize **INTRODUCTION**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/1/Text/30']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/17/Text/51', 'PZO22001 Starfinder Player Core 074-091::/page/1/Text/30', 'PZO22001 Starfinder Player Core 074-091::/page/5/Text/34']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/17/Text/51` | 0.880541 | **INTRODUCTION** |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/30` | 0.880541 | **INTRODUCTION** |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/5/Text/34` | 0.880541 | **INTRODUCTION** |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/66` | 0.838541 | **INTRODUCTION** |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/53` | 0.838541 | **INTRODUCTION** |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/9/Text/19` | 0.838541 | **INTRODUCTION** |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/59` | 0.838541 | **INTRODUCTION** |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/15/Text/33` | 0.838541 | **INTRODUCTION** |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/17/Text/66` | 0.460997 | **Languages** |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/69` | 0.460996 | **Languages** |

### Query 44
- Text: What is the rule about **ANCESTRIES & ** **BACKGROUNDS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/1/Text/31']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/17/Text/52', 'PZO22001 Starfinder Player Core 074-091::/page/1/Text/31', 'PZO22001 Starfinder Player Core 074-091::/page/3/Text/67']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/17/Text/52` | 0.920820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/31` | 0.920820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/67` | 0.920820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/60` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/5/Text/35` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/15/Text/34` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/54` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/11/Text/21` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/9/Text/20` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/9/Text/33` | 0.526957 | **Backgrounds** |

### Query 45
- Text: Summarize **Android**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/1/Text/32']
- Expected found: `True`
- Expected rank: `6`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/9/Text/21', 'PZO22001 Starfinder Player Core 074-091::/page/3/Text/68', 'PZO22001 Starfinder Player Core 074-091::/page/13/Text/55']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/9/Text/21` | 0.780962 | **Android** |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/68` | 0.780962 | **Android** |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/55` | 0.780962 | **Android** |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/15/Text/35` | 0.738962 | **Android** |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/17/Text/53` | 0.738962 | **Android** |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/32` | 0.738962 | **Android** |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/11/Text/22` | 0.738962 | **Android** |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/61` | 0.738962 | **Android** |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/5/Text/36` | 0.738962 | **Android** |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/80` | 0.380135 | **GAME** |

### Query 46
- Text: Summarize **Barathu**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/1/Text/33']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/9/Text/22', 'PZO22001 Starfinder Player Core 074-091::/page/1/Text/33', 'PZO22001 Starfinder Player Core 074-091::/page/3/Text/69']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/9/Text/22` | 0.983851 | **Barathu** |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/33` | 0.983851 | **Barathu** |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/69` | 0.983851 | **Barathu** |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/15/Text/36` | 0.941851 | **Barathu** |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/56` | 0.941851 | **Barathu** |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/17/Text/54` | 0.941851 | **Barathu** |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/62` | 0.842102 | **Barathu** **Human** |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/5/Text/37` | 0.842102 | **Barathu** **Human** |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/5/Text/47` | 0.445374 | **Borai** |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/9/Text/31` | 0.445374 | **Borai** |

### Query 47
- Text: Summarize **Human**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/1/Text/34']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/9/Text/23', 'PZO22001 Starfinder Player Core 074-091::/page/3/Text/70', 'PZO22001 Starfinder Player Core 074-091::/page/1/Text/34']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/9/Text/23` | 0.918191 | **Human** |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/70` | 0.918191 | **Human** |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/34` | 0.918191 | **Human** |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/57` | 0.876191 | **Human** |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/15/Text/37` | 0.876191 | **Human** |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/17/Text/55` | 0.876191 | **Human** |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/5/Text/37` | 0.565299 | **Barathu** **Human** |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/62` | 0.565299 | **Barathu** **Human** |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/17/Text/66` | 0.429117 | **Languages** |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/15/Text/48` | 0.429117 | **Languages** |

### Query 48
- Text: Summarize **Kasatha**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/1/Text/35']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/9/Text/24', 'PZO22001 Starfinder Player Core 074-091::/page/1/Text/35', 'PZO22001 Starfinder Player Core 074-091::/page/7/Text/63']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/9/Text/24` | 0.982519 | **Kasatha** |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/35` | 0.982519 | **Kasatha** |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/63` | 0.982519 | **Kasatha** |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/17/Text/56` | 0.940519 | **Kasatha** |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/71` | 0.940519 | **Kasatha** |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/58` | 0.940519 | **Kasatha** |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/15/Text/38` | 0.940519 | **Kasatha** |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/5/Text/39` | 0.940519 | **Kasatha** |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/9/Text/22` | 0.396219 | **Barathu** |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/15/Text/36` | 0.396219 | **Barathu** |

### Query 49
- Text: Summarize **Lashunta**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/1/Text/36']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/13/Text/59', 'PZO22001 Starfinder Player Core 074-091::/page/1/Text/36', 'PZO22001 Starfinder Player Core 074-091::/page/17/Text/57']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/59` | 0.972315 | **Lashunta** |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/36` | 0.972315 | **Lashunta** |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/17/Text/57` | 0.972315 | **Lashunta** |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/5/Text/40` | 0.930315 | **Lashunta** |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/64` | 0.930315 | **Lashunta** |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/15/Text/39` | 0.930315 | **Lashunta** |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/72` | 0.930315 | **Lashunta** |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/9/Text/25` | 0.696641 | **Lashunta** **Pahtra** |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/37` | 0.368718 | **Pahtra** **Shirren** |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/5/Text/42` | 0.343168 | **Shirren** |

### Query 50
- Text: Summarize **Pahtra** **Shirren**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/1/Text/37']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/1/Text/37', 'PZO22001 Starfinder Player Core 074-091::/page/7/Text/65', 'PZO22001 Starfinder Player Core 074-091::/page/3/Text/73']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/37` | 1.005619 | **Pahtra** **Shirren** |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/65` | 0.782910 | **Pahtra** |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/73` | 0.782910 | **Pahtra** |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/15/Text/40` | 0.740910 | **Pahtra** |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/5/Text/41` | 0.740910 | **Pahtra** |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/60` | 0.740910 | **Pahtra** |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/17/Text/58` | 0.740910 | **Pahtra** |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/9/Text/25` | 0.702280 | **Lashunta** **Pahtra** |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/74` | 0.702211 | **Shirren** |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/66` | 0.702211 | **Shirren** |

### Query 51
- Text: Summarize **Skittermander**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/1/Text/38']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/9/Text/27', 'PZO22001 Starfinder Player Core 074-091::/page/7/Text/67', 'PZO22001 Starfinder Player Core 074-091::/page/1/Text/38']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/9/Text/27` | 0.984124 | **Skittermander** |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/67` | 0.984124 | **Skittermander** |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/38` | 0.984124 | **Skittermander** |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/5/Text/43` | 0.942124 | **Skittermander** |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/17/Text/60` | 0.942124 | **Skittermander** |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/62` | 0.942124 | **Skittermander** |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/75` | 0.942124 | **Skittermander** |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/15/Text/41` | 0.746063 | **Shirren** **Skittermander** |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/9/Text/26` | 0.343107 | **Shirren** |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/66` | 0.343107 | **Shirren** |

### Query 52
- Text: Summarize **Vesk**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/1/Text/39']
- Expected found: `True`
- Expected rank: `7`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/5/Text/44', 'PZO22001 Starfinder Player Core 074-091::/page/13/Text/63', 'PZO22001 Starfinder Player Core 074-091::/page/9/Text/28']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/5/Text/44` | 0.943397 | **Vesk** |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/63` | 0.943397 | **Vesk** |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/9/Text/28` | 0.943397 | **Vesk** |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/68` | 0.901397 | **Vesk** |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/15/Text/42` | 0.901397 | **Vesk** |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/76` | 0.901397 | **Vesk** |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/39` | 0.901397 | **Vesk** |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/61` | 0.838285 | **VESK** |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/3/SectionHeader/26` | 0.838285 | **VESK** |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/43` | 0.838285 | **VESK** |

### Query 53
- Text: Summarize **Ysoki**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/1/Text/40']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/1/Text/40', 'PZO22001 Starfinder Player Core 074-091::/page/5/Text/45', 'PZO22001 Starfinder Player Core 074-091::/page/3/Text/77']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/40` | 0.934336 | **Ysoki** |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/5/Text/45` | 0.934336 | **Ysoki** |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/77` | 0.934336 | **Ysoki** |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/64` | 0.892336 | **Ysoki** |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/69` | 0.892336 | **Ysoki** |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/15/Text/43` | 0.892336 | **Ysoki** |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/9/Text/29` | 0.892336 | **Ysoki** |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/4/SectionHeader/1` | 0.743579 | **YSOKI ** |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/34` | 0.726747 | **YSOKI** |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/6/Text/19` | 0.726747 | **YSOKI** |

### Query 54
- Text: Summarize **Versatile ** **Heritages**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/1/Text/41']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/1/Text/41', 'PZO22001 Starfinder Player Core 074-091::/page/5/Text/46', 'PZO22001 Starfinder Player Core 074-091::/page/15/Text/44']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/41` | 0.959353 | **Versatile ** **Heritages** |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/15/Text/44` | 0.959353 | **Versatile ** **Heritages** |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/5/Text/46` | 0.959353 | **Versatile ** **Heritages** |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/78` | 0.917353 | **Versatile ** **Heritages** |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/70` | 0.917353 | **Versatile ** **Heritages** |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/9/Text/30` | 0.917353 | **Versatile ** **Heritages** |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/17/Text/62` | 0.917353 | **Versatile ** **Heritages** |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/65` | 0.917353 | **Versatile ** **Heritages** |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/11/SectionHeader/17` | 0.700905 | **VERSATILE HERITAGES** |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/8/SectionHeader/1` | 0.665310 | VERSATILE HERITAGES |

### Query 55
- Text: Summarize **Borai** **Prismeni**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/1/Text/42']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/1/Text/42', 'PZO22001 Starfinder Player Core 074-091::/page/7/Text/71', 'PZO22001 Starfinder Player Core 074-091::/page/15/Text/45']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/42` | 1.000180 | **Borai** **Prismeni** |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/71` | 1.000180 | **Borai** **Prismeni** |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/15/Text/45` | 0.802444 | **Borai** |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/5/Text/47` | 0.760444 | **Borai** |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/66` | 0.760444 | **Borai** |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/17/Text/63` | 0.760444 | **Borai** |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/9/Text/31` | 0.760444 | **Borai** |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/79` | 0.760444 | **Borai** |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/12/SectionHeader/19` | 0.710029 | **BORAI** |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/12/SectionHeader/29` | 0.710029 | **BORAI** |

### Query 56
- Text: What is the rule about **Backgrounds**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/1/Text/43']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/1/Text/43', 'PZO22001 Starfinder Player Core 074-091::/page/3/Text/81', 'PZO22001 Starfinder Player Core 074-091::/page/15/Text/47']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/43` | 0.796516 | **Backgrounds** |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/81` | 0.796516 | **Backgrounds** |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/15/Text/47` | 0.796516 | **Backgrounds** |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/9/Text/33` | 0.754516 | **Backgrounds** |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/17/Text/65` | 0.754516 | **Backgrounds** |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/72` | 0.754516 | **Backgrounds** |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/68` | 0.754516 | **Backgrounds** |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/5/Text/49` | 0.661389 | **Backgrounds** **Languages** |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/15/Text/34` | 0.510451 | **ANCESTRIES & ** **BACKGROUNDS** |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/9/Text/20` | 0.510451 | **ANCESTRIES & ** **BACKGROUNDS** |

### Query 57
- Text: Summarize **Languages**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/1/Text/44']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/17/Text/66', 'PZO22001 Starfinder Player Core 074-091::/page/1/Text/44', 'PZO22001 Starfinder Player Core 074-091::/page/7/Text/73']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/17/Text/66` | 0.876250 | **Languages** |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/44` | 0.876250 | **Languages** |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/73` | 0.876250 | **Languages** |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/9/Text/34` | 0.834250 | **Languages** |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/82` | 0.834250 | **Languages** |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/15/Text/48` | 0.834250 | **Languages** |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/69` | 0.834250 | **Languages** |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/5/Text/49` | 0.701824 | **Backgrounds** **Languages** |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/4/Text/9` | 0.488715 | Additional languages equal to your Intelligence modifier (if it's positive). Choose from the list of common languages and any other languages to which you have access (such as the languages prevalent |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/0/Text/9` | 0.484389 | One regional language of your choice Additional languages equal to your Intelligence modifier (if it's positive). Choose from the list of common languages and any other languages to which you have acc |

### Query 58
- Text: Summarize **CLASSES**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/1/Text/45']
- Expected found: `True`
- Expected rank: `5`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/15/Text/49', 'PZO22001 Starfinder Player Core 074-091::/page/7/Text/74', 'PZO22001 Starfinder Player Core 074-091::/page/9/Text/35']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/15/Text/49` | 0.940061 | **CLASSES** |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/74` | 0.940061 | **CLASSES** |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/9/Text/35` | 0.940061 | **CLASSES** |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/5/Text/50` | 0.910061 | **CLASSES** |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/45` | 0.910061 | **CLASSES** |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/70` | 0.910061 | **CLASSES** |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/17/Text/67` | 0.910061 | **CLASSES** |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/83` | 0.719499 | **CLASSES** **SKILLS** |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/15/Text/48` | 0.481450 | **Languages** |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/9/Text/34` | 0.481450 | **Languages** |

### Query 59
- Text: What is the rule about **SKILLS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/1/Text/46']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/7/Text/75', 'PZO22001 Starfinder Player Core 074-091::/page/17/Text/68', 'PZO22001 Starfinder Player Core 074-091::/page/1/Text/46']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/75` | 0.864442 | **SKILLS** |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/17/Text/68` | 0.864442 | **SKILLS** |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/46` | 0.864442 | **SKILLS** |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/71` | 0.822442 | **SKILLS** |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/5/Text/51` | 0.822442 | **SKILLS** |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/83` | 0.738936 | **CLASSES** **SKILLS** |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/9/Text/36` | 0.651094 | **SKILLS** **FEATS** |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/15/Text/50` | 0.651094 | **SKILLS** **FEATS** |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/16/Text/5` | 0.448779 | You have an intuitive understanding of  computers, machines, and other technological  devices. You become trained in Computers and  Crafting. If you would automatically become trained  in one of those |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/4/SectionHeader/10` | 0.429807 | **TRAITS ** |

### Query 60
- Text: What is the rule about **FEATS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/1/Text/47']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/3/Text/84', 'PZO22001 Starfinder Player Core 074-091::/page/7/Text/76', 'PZO22001 Starfinder Player Core 074-091::/page/1/Text/47']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/84` | 0.871817 | **FEATS** |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/47` | 0.871817 | **FEATS** |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/76` | 0.871817 | **FEATS** |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/5/Text/52` | 0.829817 | **FEATS** |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/72` | 0.829817 | **FEATS** |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/17/Text/69` | 0.702296 | **FEATS** **EQUIPMENT** |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/9/Text/36` | 0.653037 | **SKILLS** **FEATS** |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/15/Text/50` | 0.653037 | **SKILLS** **FEATS** |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/9/SectionHeader/4` | 0.460192 | LINEAGE FEATS |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/7/SectionHeader/36` | 0.439162 | **UNDERFOOT** **FEAT 9** |

### Query 61
- Text: Summarize **EQUIPMENT**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/1/Text/48']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/1/Text/48', 'PZO22001 Starfinder Player Core 074-091::/page/9/Text/37', 'PZO22001 Starfinder Player Core 074-091::/page/15/Text/51']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/48` | 0.944726 | **EQUIPMENT** |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/9/Text/37` | 0.944726 | **EQUIPMENT** |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/15/Text/51` | 0.944726 | **EQUIPMENT** |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/85` | 0.902726 | **EQUIPMENT** |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/5/Text/53` | 0.902726 | **EQUIPMENT** |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/77` | 0.902726 | **EQUIPMENT** |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/73` | 0.902726 | **EQUIPMENT** |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/17/Text/69` | 0.627947 | **FEATS** **EQUIPMENT** |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/66` | 0.385549 | **INTRODUCTION** |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/59` | 0.385549 | **INTRODUCTION** |

### Query 62
- Text: What is the rule about **SPELLS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/1/Text/49']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/9/Text/38', 'PZO22001 Starfinder Player Core 074-091::/page/15/Text/52', 'PZO22001 Starfinder Player Core 074-091::/page/1/Text/49']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/9/Text/38` | 0.889304 | **SPELLS** |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/15/Text/52` | 0.889304 | **SPELLS** |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/49` | 0.889304 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/74` | 0.847304 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/86` | 0.847304 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/79` | 0.847304 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/17/Text/70` | 0.847304 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/5/Text/54` | 0.847304 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/75` | 0.388254 | **SKILLS** |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/46` | 0.388254 | **SKILLS** |

### Query 63
- Text: Summarize **PLAYING THE ** **GAME**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/1/Text/50']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/17/Text/71', 'PZO22001 Starfinder Player Core 074-091::/page/1/Text/50', 'PZO22001 Starfinder Player Core 074-091::/page/15/Text/53']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/17/Text/71` | 0.965000 | **PLAYING THE ** **GAME** |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/50` | 0.965000 | **PLAYING THE ** **GAME** |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/15/Text/53` | 0.965000 | **PLAYING THE ** **GAME** |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/5/Text/55` | 0.923000 | **PLAYING THE ** **GAME** |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/87` | 0.923000 | **PLAYING THE ** **GAME** |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/80` | 0.923000 | **PLAYING THE ** **GAME** |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/9/Text/39` | 0.923000 | **PLAYING THE ** **GAME** |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/75` | 0.811006 | **PLAYING THE ** |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/80` | 0.663024 | **GAME** |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/17/Text/51` | 0.418586 | **INTRODUCTION** |

### Query 64
- Text: Summarize **CONDITIONS ** **APPENDIX**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/1/Text/51']
- Expected found: `True`
- Expected rank: `6`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/9/Text/40', 'PZO22001 Starfinder Player Core 074-091::/page/15/Text/54', 'PZO22001 Starfinder Player Core 074-091::/page/7/Text/81']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/9/Text/40` | 0.983499 | **CONDITIONS ** **APPENDIX** |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/15/Text/54` | 0.983499 | **CONDITIONS ** **APPENDIX** |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/81` | 0.983499 | **CONDITIONS ** **APPENDIX** |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/88` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/5/Text/56` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/51` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/17/Text/72` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/76` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/17/Text/52` | 0.416141 | **ANCESTRIES & ** **BACKGROUNDS** |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/60` | 0.416141 | **ANCESTRIES & ** **BACKGROUNDS** |

### Query 65
- Text: Summarize **GLOSSARY & ** **INDEX**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/1/Text/52']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/9/Text/41', 'PZO22001 Starfinder Player Core 074-091::/page/7/Text/82', 'PZO22001 Starfinder Player Core 074-091::/page/1/Text/52']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/9/Text/41` | 0.993465 | **GLOSSARY & ** **INDEX** |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/82` | 0.993465 | **GLOSSARY & ** **INDEX** |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/52` | 0.993465 | **GLOSSARY & ** **INDEX** |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/15/Text/55` | 0.951465 | **GLOSSARY & ** **INDEX** |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/89` | 0.951465 | **GLOSSARY & ** **INDEX** |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/77` | 0.951465 | **GLOSSARY & ** **INDEX** |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/17/Text/73` | 0.951465 | **GLOSSARY & ** **INDEX** |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/5/Text/57` | 0.951465 | **GLOSSARY & ** **INDEX** |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/45` | 0.385404 | **CLASSES** |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/9/Text/35` | 0.385404 | **CLASSES** |

### Query 66
- Text: Summarize VENOMTHOUGHT VESK
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/2/SectionHeader/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/2/SectionHeader/1', 'PZO22001 Starfinder Player Core 074-091::/page/0/SectionHeader/1', 'PZO22001 Starfinder Player Core 074-091::/page/0/Text/11']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/2/SectionHeader/1` | 0.992822 | VENOMTHOUGHT VESK |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/0/SectionHeader/1` | 0.690655 | VESK |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/0/Text/11` | 0.659699 | HUMANOID VESK |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/63` | 0.586853 | **Vesk** |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/5/Text/44` | 0.586853 | **Vesk** |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/9/Text/28` | 0.586853 | **Vesk** |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/76` | 0.586853 | **Vesk** |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/39` | 0.586853 | **Vesk** |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/15/Text/42` | 0.586853 | **Vesk** |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/68` | 0.586853 | **Vesk** |

### Query 67
- Text: What is the rule about You're one of the notable vesk born with psychic talents.  According to folklore, your lineage originated with an  ancient cave-dwelling society on Vesk Prime who modified  themselves with occult rituals, which granted them  "venomous thoughts" that could manifest in any future  progeny. You can cast *daze* as an occult innate cantrip at  will. A cantrip is heightened to a spell rank equal to half  your level rounded up. You gain a +1 circumstance bonus  to Occultism checks to Recall Knowledge about psychic  traditions and philosophies.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/2/Text/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/2/Text/2', 'PZO22001 Starfinder Player Core 074-091::/page/2/Text/7', 'PZO22001 Starfinder Player Core 074-091::/page/12/Text/25']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/2/Text/2` | 1.004292 | You're one of the notable vesk born with psychic talents.  According to folklore, your lineage originated with an  ancient cave-dwelling society on Vesk Prime who modified  themselves with occult ritu |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/2/Text/7` | 0.583981 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As a vesk, you choose from among the  following ance |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/12/Text/25` | 0.578768 | You exist on the boundaries between life and death, and  you can channel your own imbalanced spiritual essence into  magical spells. Choose one of the following cantrips: *vitality* *lash* or *void* * |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/16/Text/39` | 0.535879 | You can easily send data to technological devices like a  spectra. You can cast the *implant data* cantrip as a divine  innate spell at will. A cantrip is heightened to a spell rank |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/16/Text/20` | 0.530614 | Your body produces an overabundance of electrical energy,  which you can emit as a blast of lightning or use to power  technological devices. You can cast the *electric arc* cantrip as  a divine innat |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/2/Text/32` | 0.518307 | You're trained with all doshkos. In addition, you gain access to  all uncommon weapons with the vesk trait. For the purposes  of proficiency, you treat any of these that are martial weapons |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/12/Text/20` | 0.497043 | Since your resurrection, you've learned a lot about yourself,  your place in the cycle of souls, and other undead. You gain  the trained proficiency rank in Intimidation and Religion.  If you would au |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/5` | 0.486899 | Some element of your borai nature gives you flashes from  the beyond: visions from the afterlife you were intended for  or might still one day obtain. You gain the trained proficiency  rank in Religio |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/9` | 0.485395 | Vesk have a long history of conflict, first as conquerors within  their own star system and later clashing with neighboring  stellar powers such as the Pact Worlds and the Swarm.  Currently, the Veska |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/15` | 0.481122 | Vesk society is highly organized and militaristic. Vesk first  dwelled on a single planet but quickly spread to other worlds  in their system. Today, the name for these conquered worlds  is the Veskar |

### Query 68
- Text: What is the rule about You come from a bloodline of renowned and honored  warriors who have honed their bodies over centuries to  become lethal weapons. You gain the Brutal Anatomy  ancestry feat twice.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/2/Text/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/2/Text/4', 'PZO22001 Starfinder Player Core 074-091::/page/2/Text/7', 'PZO22001 Starfinder Player Core 074-091::/page/11/Text/8']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/2/Text/4` | 0.976182 | You come from a bloodline of renowned and honored  warriors who have honed their bodies over centuries to  become lethal weapons. You gain the Brutal Anatomy  ancestry feat twice. |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/2/Text/7` | 0.552857 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As a vesk, you choose from among the  following ance |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/11/Text/8` | 0.545587 | You've returned from the brink of death as a borai at once both living and undead. You gain the borai  and undead trait, in addition to the traits from  your ancestry. Unlike other undead, you don't |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/9/Text/16` | 0.486768 | You can choose a mixed ancestry to represent having two  ancestral lines for your character. This doesn't preclude  having more than two ancestries in your genealogy, but  you'll need to work with you |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/4/Text/15` | 0.484964 | Your prominent incisors offer an alternative to the fists other humanoids bring to a fight. You have a jaws unarmed attack that deals 1d4 piercing damage, is in the brawling group, and has the agile a |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/9/Text/5` | 0.476934 | Some ancestry feats within a versatile heritage have the  lineage trait. These feats specify a physiological lineage your  character has—such as if a prismeni was born in the Drift or  chosen by Triun |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/6/Text/11` | 0.461739 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th,  9th, 13th, and 17th levels). As a ysoki, you select from  among the following an |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/2/Text/16` | 0.461670 | You're a natural predator trained to use part of your body  as a weapon. When you select this feat, you gain one of the  following unarmed attacks of your choice: claw, jaws, or tail.  Each of these a |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/9/Text/2` | 0.445206 | Sometimes a versatile heritage might give you an ability that  conflicts with an ability from your ancestry. In these cases, you  choose which of the conflicting abilities your character has. |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/16` | 0.443856 | Vesk names typically combine elements of their parents'  names as well as those of other prominent ancestors.  Companions often shorten these names for casual use, but  doing so without permission is |

### Query 69
- Text: What is the rule about VESK ANCESTRY FEATS?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/2/SectionHeader/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/2/SectionHeader/6', 'PZO22001 Starfinder Player Core 074-091::/page/6/SectionHeader/10', 'PZO22001 Starfinder Player Core 074-091::/page/2/Text/7']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/2/SectionHeader/6` | 0.911111 | VESK ANCESTRY FEATS |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/6/SectionHeader/10` | 0.662184 | YSOKI ANCESTRY FEATS |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/2/Text/7` | 0.646128 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As a vesk, you choose from among the  following ance |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/15/SectionHeader/13` | 0.594001 | PRISMENI ANCESTRY  FEATS |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/11/SectionHeader/9` | 0.574351 | BORAI ANCESTRY FEATS |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/0/SectionHeader/1` | 0.522307 | VESK |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/1/SectionHeader/21` | 0.490476 | VESK HERITAGES |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/2/SectionHeader/29` | 0.476385 | **VESK WEAPON FAMILIARITY** **FEAT 1** |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/1/SectionHeader/25` | 0.474631 | NIGHTSTALKER VESK |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/61` | 0.470792 | **VESK** |

### Query 70
- Text: What is the rule about At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As a vesk, you choose from among the  following ancestry feats.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/2/Text/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/2/Text/7', 'PZO22001 Starfinder Player Core 074-091::/page/6/Text/11', 'PZO22001 Starfinder Player Core 074-091::/page/9/Text/5']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/2/Text/7` | 0.974977 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As a vesk, you choose from among the  following ance |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/6/Text/11` | 0.829770 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th,  9th, 13th, and 17th levels). As a ysoki, you select from  among the following an |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/9/Text/5` | 0.653145 | Some ancestry feats within a versatile heritage have the  lineage trait. These feats specify a physiological lineage your  character has—such as if a prismeni was born in the Drift or  chosen by Triun |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/9/Text/3` | 0.608571 | When selecting ancestry feats, you can choose from those  available to your ancestry as well as those specific to your  versatile heritage. |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/22` | 0.596749 | Vesk lineages were shaped by the worlds they inhabited and  battled over. Choose one of the following vesk heritages at  1st level. |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/9/Text/16` | 0.557349 | You can choose a mixed ancestry to represent having two  ancestral lines for your character. This doesn't preclude  having more than two ancestries in your genealogy, but  you'll need to work with you |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/16` | 0.522355 | Vesk names typically combine elements of their parents'  names as well as those of other prominent ancestors.  Companions often shorten these names for casual use, but  doing so without permission is |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/28` | 0.511017 | Your ancestors were the hardiest specimens of vesk, having  traveled far and wide while enduring hostile environments.  Your scales count as medium armor in the plate armor group.  They grant a +3 ite |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/8/Text/11` | 0.509464 | To play a character with a versatile heritage, first select your  ancestry, just like you would for any character. You gain  Hit Points, size, Speed, attribute boosts and attribute flaws,  languages, |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/9/Text/2` | 0.499920 | Sometimes a versatile heritage might give you an ability that  conflicts with an ability from your ancestry. In these cases, you  choose which of the conflicting abilities your character has. |

### Query 71
- Text: What are the requirements for **ARMOR ACE** **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/2/SectionHeader/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/2/SectionHeader/9', 'PZO22001 Starfinder Player Core 074-091::/page/3/Text/32', 'PZO22001 Starfinder Player Core 074-091::/page/17/Text/69']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/2/SectionHeader/9` | 0.882793 | **ARMOR ACE** **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/32` | 0.583890 | **Prerequisites** plated vesk heritage or Armor Ace |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/17/Text/69` | 0.497926 | **FEATS** **EQUIPMENT** |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/12/SectionHeader/1` | 0.455802 | **HEADSTRONG** **FEAT 1** |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/11/Text/13` | 0.408577 | **ETHERIC** **FEAT 1** |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/15/Text/50` | 0.398979 | **SKILLS** **FEATS** |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/9/Text/36` | 0.398979 | **SKILLS** **FEATS** |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/11` | 0.398297 | **RESONANT WEAPON **[one-action] **FEAT 9** |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/84` | 0.394440 | **FEATS** |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/5/Text/52` | 0.394440 | **FEATS** |

### Query 72
- Text: What is the rule about You've learned through trial and painful error how to make the  most out of your armor, deflecting damage from explosions  and similar effects. When donning armor, you can grant it the  bulwark trait until you remove it. When you're wearing armor  that already has the bulwark trait, increase the modifier to  Reflex saves to avoid damaging effects granted by that armor  to +4, rather than +3.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/2/Text/12']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/2/Text/12', 'PZO22001 Starfinder Player Core 074-091::/page/13/Text/25', 'PZO22001 Starfinder Player Core 074-091::/page/3/Text/33']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/2/Text/12` | 0.994401 | You've learned through trial and painful error how to make the  most out of your armor, deflecting damage from explosions  and similar effects. When donning armor, you can grant it the  bulwark trait |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/25` | 0.547545 | You unleash a portion of your spiritual essence—either the  vitality of your living body or the void of your undead soul in a violent burst around you. You deal 5d6 damage of your  selected type (see |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/33` | 0.530326 | You've mastered using your own plate scales or worn armor  to absorb devastating strikes. You gain the Plate Deflection |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/16/Text/17` | 0.479805 | **Redirect Current** [reaction] (electricity) **Frequency** once per hour;  **Trigger** You take electricity damage, and your electricity  resistance doesn't reduce this damage to 0; **Effect** After |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/28` | 0.479237 | Your ancestors were the hardiest specimens of vesk, having  traveled far and wide while enduring hostile environments.  Your scales count as medium armor in the plate armor group.  They grant a +3 ite |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/40` | 0.468200 | When your foe is weak, you press on. When you successfully  Strike a creature that has the frightened or persistent  bleed condition with a melee or ranged weapon, you gain a  circumstance bonus to th |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/1` | 0.459040 | modifier as one higher while determining how much you  heal from resting. |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/6/Text/29` | 0.450534 | You grew up learning to tinker with devices, repair  objects, and take things apart. You're trained in Crafting. If  you're trained in Crafting from another source (from your  background or class, for |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/35` | 0.444116 | **Plate** **Deflection** [reaction] **Frequency** once per day; **Trigger** You're  struck by a critical hit; **Effect** You deflect the attack to a  heavily armored part of your body. You don't take |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/53` | 0.437040 | You clear your mind of distractions and focus on your foe,  determined to overcome the shame of your failure lest it  forever blemish your reputation. The next time before the end  of your turn that y |

### Query 73
- Text: What are the requirements for **BRUTAL ANATOMY** **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/2/SectionHeader/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/2/SectionHeader/13', 'PZO22001 Starfinder Player Core 074-091::/page/7/Text/44', 'PZO22001 Starfinder Player Core 074-091::/page/12/SectionHeader/1']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/2/SectionHeader/13` | 0.882517 | **BRUTAL ANATOMY** **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/44` | 0.438533 | **Prerequisites** Underfoot |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/12/SectionHeader/1` | 0.434452 | **HEADSTRONG** **FEAT 1** |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/9/Text/36` | 0.373536 | **SKILLS** **FEATS** |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/15/Text/50` | 0.373536 | **SKILLS** **FEATS** |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/17/Text/69` | 0.362003 | **FEATS** **EQUIPMENT** |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/2/SectionHeader/9` | 0.361953 | **ARMOR ACE** **FEAT 1** |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/84` | 0.356907 | **FEATS** |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/76` | 0.356907 | **FEATS** |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/5/Text/52` | 0.356907 | **FEATS** |

### Query 74
- Text: What is the rule about You're a natural predator trained to use part of your body  as a weapon. When you select this feat, you gain one of the  following unarmed attacks of your choice: claw, jaws, or tail.  Each of these attacks is in the brawling weapon group.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/2/Text/16']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/2/Text/16', 'PZO22001 Starfinder Player Core 074-091::/page/4/Text/15', 'PZO22001 Starfinder Player Core 074-091::/page/2/Text/17']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/2/Text/16` | 0.987968 | You're a natural predator trained to use part of your body  as a weapon. When you select this feat, you gain one of the  following unarmed attacks of your choice: claw, jaws, or tail.  Each of these a |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/4/Text/15` | 0.657852 | Your prominent incisors offer an alternative to the fists other humanoids bring to a fight. You have a jaws unarmed attack that deals 1d4 piercing damage, is in the brawling group, and has the agile a |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/2/Text/17` | 0.618989 | A claw unarmed attack deals 1d6 slashing damage and has  the agile, finesse, unarmed, and vesk traits. |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/2/Text/18` | 0.524427 | A jaws unarmed attack deals 1d6 piercing damage and has  the grapple, unarmed, and vesk traits. |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/2/Text/19` | 0.505910 | A tail unarmed attack deals 1d6 bludgeoning damage and  has the sweep, trip, unarmed, and vesk traits. |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/19` | 0.481744 | Your tail functions like an extra limb. You can hold one extra  hand's worth of equipment with your tail, and you can use  your tail to perform Interact actions. You tail is considered  one pair of ha |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/4` | 0.462842 | Years of experience living among ysoki communities have  trained your nimble steps and sneaky moves. You gain the  trained proficiency rank in Acrobatics and Stealth. If you  would automatically becom |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/2/Text/32` | 0.462277 | You're trained with all doshkos. In addition, you gain access to  all uncommon weapons with the vesk trait. For the purposes  of proficiency, you treat any of these that are martial weapons |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/2/Text/4` | 0.461720 | You come from a bloodline of renowned and honored  warriors who have honed their bodies over centuries to  become lethal weapons. You gain the Brutal Anatomy  ancestry feat twice. |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/2/Text/7` | 0.459754 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As a vesk, you choose from among the  following ance |

### Query 75
- Text: What is the rule about A claw unarmed attack deals 1d6 slashing damage and has  the agile, finesse, unarmed, and vesk traits.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/2/Text/17']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/2/Text/17', 'PZO22001 Starfinder Player Core 074-091::/page/2/Text/19', 'PZO22001 Starfinder Player Core 074-091::/page/2/Text/18']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/2/Text/17` | 0.961032 | A claw unarmed attack deals 1d6 slashing damage and has  the agile, finesse, unarmed, and vesk traits. |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/2/Text/19` | 0.710228 | A tail unarmed attack deals 1d6 bludgeoning damage and  has the sweep, trip, unarmed, and vesk traits. |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/2/Text/18` | 0.656352 | A jaws unarmed attack deals 1d6 piercing damage and has  the grapple, unarmed, and vesk traits. |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/2/Text/16` | 0.582006 | You're a natural predator trained to use part of your body  as a weapon. When you select this feat, you gain one of the  following unarmed attacks of your choice: claw, jaws, or tail.  Each of these a |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/4/Text/15` | 0.527945 | Your prominent incisors offer an alternative to the fists other humanoids bring to a fight. You have a jaws unarmed attack that deals 1d4 piercing damage, is in the brawling group, and has the agile a |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/10` | 0.440151 | If you want a character who's duty bound, brave, and stoic,  you should play a vesk. |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/2/Text/32` | 0.439653 | You're trained with all doshkos. In addition, you gain access to  all uncommon weapons with the vesk trait. For the purposes  of proficiency, you treat any of these that are martial weapons |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/13` | 0.429979 | Vesk adopted tech weapons early in their history but retain  the brutal claws and teeth of natural predators. They take  great care in grooming and painting their scales and claws to  showcase their p |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/28` | 0.399484 | Your ancestors were the hardiest specimens of vesk, having  traveled far and wide while enduring hostile environments.  Your scales count as medium armor in the plate armor group.  They grant a +3 ite |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/40` | 0.398381 | When your foe is weak, you press on. When you successfully  Strike a creature that has the frightened or persistent  bleed condition with a melee or ranged weapon, you gain a  circumstance bonus to th |

### Query 76
- Text: What is the rule about A jaws unarmed attack deals 1d6 piercing damage and has  the grapple, unarmed, and vesk traits.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/2/Text/18']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/2/Text/18', 'PZO22001 Starfinder Player Core 074-091::/page/2/Text/19', 'PZO22001 Starfinder Player Core 074-091::/page/4/Text/15']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/2/Text/18` | 0.952021 | A jaws unarmed attack deals 1d6 piercing damage and has  the grapple, unarmed, and vesk traits. |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/2/Text/19` | 0.682424 | A tail unarmed attack deals 1d6 bludgeoning damage and  has the sweep, trip, unarmed, and vesk traits. |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/4/Text/15` | 0.680065 | Your prominent incisors offer an alternative to the fists other humanoids bring to a fight. You have a jaws unarmed attack that deals 1d4 piercing damage, is in the brawling group, and has the agile a |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/2/Text/17` | 0.620955 | A claw unarmed attack deals 1d6 slashing damage and has  the agile, finesse, unarmed, and vesk traits. |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/2/Text/16` | 0.508587 | You're a natural predator trained to use part of your body  as a weapon. When you select this feat, you gain one of the  following unarmed attacks of your choice: claw, jaws, or tail.  Each of these a |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/2/Text/32` | 0.420222 | You're trained with all doshkos. In addition, you gain access to  all uncommon weapons with the vesk trait. For the purposes  of proficiency, you treat any of these that are martial weapons |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/40` | 0.404804 | When your foe is weak, you press on. When you successfully  Strike a creature that has the frightened or persistent  bleed condition with a melee or ranged weapon, you gain a  circumstance bonus to th |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/15` | 0.402115 | When you're physically outmatched, you fight with  unexpected ferocity. If a foe of a larger size than you  critically hits and damages you, that foe is off-guard to you  for 1 round. |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/19` | 0.374225 | **Trigger** An enemy's Strike or targeted effect would hit you,  and you weren't already concealed, hidden, or undetected  to that enemy. |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/46` | 0.373816 | You launch a surprise attack from below. Make a melee  Strike against the triggering creature. If your attack is a  critical hit and the trigger was a manipulate action, you  disrupt that action. This |

### Query 77
- Text: What is the rule about A tail unarmed attack deals 1d6 bludgeoning damage and  has the sweep, trip, unarmed, and vesk traits.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/2/Text/19']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/2/Text/19', 'PZO22001 Starfinder Player Core 074-091::/page/2/Text/17', 'PZO22001 Starfinder Player Core 074-091::/page/2/Text/18']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/2/Text/19` | 0.963724 | A tail unarmed attack deals 1d6 bludgeoning damage and  has the sweep, trip, unarmed, and vesk traits. |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/2/Text/17` | 0.696301 | A claw unarmed attack deals 1d6 slashing damage and has  the agile, finesse, unarmed, and vesk traits. |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/2/Text/18` | 0.671218 | A jaws unarmed attack deals 1d6 piercing damage and has  the grapple, unarmed, and vesk traits. |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/2/Text/16` | 0.496839 | You're a natural predator trained to use part of your body  as a weapon. When you select this feat, you gain one of the  following unarmed attacks of your choice: claw, jaws, or tail.  Each of these a |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/2/Text/32` | 0.444364 | You're trained with all doshkos. In addition, you gain access to  all uncommon weapons with the vesk trait. For the purposes  of proficiency, you treat any of these that are martial weapons |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/4/Text/15` | 0.437601 | Your prominent incisors offer an alternative to the fists other humanoids bring to a fight. You have a jaws unarmed attack that deals 1d4 piercing damage, is in the brawling group, and has the agile a |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/2/Text/7` | 0.412268 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As a vesk, you choose from among the  following ance |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/25` | 0.409035 | You unleash a portion of your spiritual essence—either the  vitality of your living body or the void of your undead soul in a violent burst around you. You deal 5d6 damage of your  selected type (see |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/40` | 0.403729 | When your foe is weak, you press on. When you successfully  Strike a creature that has the frightened or persistent  bleed condition with a melee or ranged weapon, you gain a  circumstance bonus to th |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/19` | 0.387831 | Your tail functions like an extra limb. You can hold one extra  hand's worth of equipment with your tail, and you can use  your tail to perform Interact actions. You tail is considered  one pair of ha |

### Query 78
- Text: What is the rule about At 5th level, whenever you get a critical hit with one  of these attacks, you get its critical specialization effect. **Special** You can take this feat three times. Each time you  do, select a different attack from the options listed above.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/2/Text/20']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/2/Text/20', 'PZO22001 Starfinder Player Core 074-091::/page/3/Text/2', 'PZO22001 Starfinder Player Core 074-091::/page/7/Text/46']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/2/Text/20` | 0.982920 | At 5th level, whenever you get a critical hit with one  of these attacks, you get its critical specialization effect. **Special** You can take this feat three times. Each time you  do, select a differ |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/2` | 0.844491 | At 5th level, whenever you get a critical hit with one of  these weapons, you get its critical specialization effect. |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/46` | 0.587580 | You launch a surprise attack from below. Make a melee  Strike against the triggering creature. If your attack is a  critical hit and the trigger was a manipulate action, you  disrupt that action. This |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/12/Text/26` | 0.533576 | **Special** You can select this feat twice. Each time, you must  select a different cantrip. |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/2/Text/24` | 0.515513 | You're a skilled leader. Whenever an ally selects you as the  target of their attempts to Follow the Expert, you increase  the circumstance bonus they receive to their skill check  by an additional +1 |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/35` | 0.501088 | **Plate** **Deflection** [reaction] **Frequency** once per day; **Trigger** You're  struck by a critical hit; **Effect** You deflect the attack to a  heavily armored part of your body. You don't take |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/40` | 0.472904 | When your foe is weak, you press on. When you successfully  Strike a creature that has the frightened or persistent  bleed condition with a melee or ranged weapon, you gain a  circumstance bonus to th |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/64` | 0.461639 | You don't just fight because you have to; the threat of battle  and the thrill of victory invigorate you. You gain a number of  temporary Hit Points equal to your level. These temporary  Hit Points la |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/2/Text/7` | 0.460565 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As a vesk, you choose from among the  following ance |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/6/Text/11` | 0.459504 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th,  9th, 13th, and 17th levels). As a ysoki, you select from  among the following an |

### Query 79
- Text: What are the requirements for **COMMAND TACTICS** **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/2/SectionHeader/21']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/2/SectionHeader/21', 'PZO22001 Starfinder Player Core 074-091::/page/15/SectionHeader/17', 'PZO22001 Starfinder Player Core 074-091::/page/9/Text/36']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/2/SectionHeader/21` | 0.895941 | **COMMAND TACTICS** **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/15/SectionHeader/17` | 0.501566 | **DRIFT-TOUCHED **[one-action] **FEAT 1** |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/9/Text/36` | 0.482615 | **SKILLS** **FEATS** |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/15/Text/50` | 0.440615 | **SKILLS** **FEATS** |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/12/SectionHeader/1` | 0.420846 | **HEADSTRONG** **FEAT 1** |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/2/SectionHeader/9` | 0.412849 | **ARMOR ACE** **FEAT 1** |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/11/Text/13` | 0.409953 | **ETHERIC** **FEAT 1** |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/17/Text/69` | 0.390167 | **FEATS** **EQUIPMENT** |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/16/SectionHeader/2` | 0.377532 | **TECH FAMILIARITY** **FEAT 1** |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/84` | 0.375053 | **FEATS** |

### Query 80
- Text: What is the rule about You're a skilled leader. Whenever an ally selects you as the  target of their attempts to Follow the Expert, you increase  the circumstance bonus they receive to their skill check  by an additional +1, or an additional +2 if you have master  proficiency or higher (for a total of +3 for expert, +5 for  master, and +6 for legendary).?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/2/Text/24']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/2/Text/24', 'PZO22001 Starfinder Player Core 074-091::/page/3/Text/40', 'PZO22001 Starfinder Player Core 074-091::/page/2/Text/20']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/2/Text/24` | 0.993087 | You're a skilled leader. Whenever an ally selects you as the  target of their attempts to Follow the Expert, you increase  the circumstance bonus they receive to their skill check  by an additional +1 |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/40` | 0.530910 | When your foe is weak, you press on. When you successfully  Strike a creature that has the frightened or persistent  bleed condition with a melee or ranged weapon, you gain a  circumstance bonus to th |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/2/Text/20` | 0.514160 | At 5th level, whenever you get a critical hit with one  of these attacks, you get its critical specialization effect. **Special** You can take this feat three times. Each time you  do, select a differ |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/16/Text/25` | 0.459666 | You've learned to leverage your intrinsic link to the Drift,  making you an excellent pilot. You gain the trained proficiency  rank in Piloting and Stealth. If you would automatically  become trained |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/6/Text/29` | 0.454464 | You grew up learning to tinker with devices, repair  objects, and take things apart. You're trained in Crafting. If  you're trained in Crafting from another source (from your  background or class, for |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/6/Text/20` | 0.444828 | You follow Lao Shu Po's teachings and aren't afraid to lie,  cheat, or steal to get what you desire. Thanks to your extra  devotion, you gain the trained proficiency rank in Deception  and Thievery. I |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/12/Text/20` | 0.441781 | Since your resurrection, you've learned a lot about yourself,  your place in the cycle of souls, and other undead. You gain  the trained proficiency rank in Intimidation and Religion.  If you would au |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/2` | 0.439406 | At 5th level, whenever you get a critical hit with one of  these weapons, you get its critical specialization effect. |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/5/Text/32` | 0.437221 | In addition, you gain a +2 circumstance bonus to  Perception checks to Seek a creature or object within the  range of your scent. |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/6/Text/4` | 0.432734 | You were born aboard a starship, inside a space station's  access corridors, or another similar environment. You  gain the trained proficiency rank in Piloting. If you would  automatically become trai |

### Query 81
- Text: What are the requirements for **FEARLESS** **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/2/SectionHeader/25']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/2/SectionHeader/25', 'PZO22001 Starfinder Player Core 074-091::/page/12/SectionHeader/1', 'PZO22001 Starfinder Player Core 074-091::/page/15/Text/50']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/2/SectionHeader/25` | 0.845989 | **FEARLESS** **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/12/SectionHeader/1` | 0.490078 | **HEADSTRONG** **FEAT 1** |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/15/Text/50` | 0.483970 | **SKILLS** **FEATS** |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/9/Text/36` | 0.441970 | **SKILLS** **FEATS** |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/72` | 0.432091 | **FEATS** |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/76` | 0.432091 | **FEATS** |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/47` | 0.432091 | **FEATS** |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/5/Text/52` | 0.432091 | **FEATS** |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/84` | 0.432091 | **FEATS** |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/15/SectionHeader/24` | 0.426104 | **SPECTRASOUL** **FEAT 1** |

### Query 82
- Text: What is the rule about Whether it comes from a sense of duty or a desire to  succeed, you rarely flinch when confronted by fearsome  foes. If you roll a success on a saving throw against a fear  effect, you get a critical success instead.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/2/Text/28']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/2/Text/28', 'PZO22001 Starfinder Player Core 074-091::/page/13/Text/38', 'PZO22001 Starfinder Player Core 074-091::/page/3/Text/53']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/2/Text/28` | 0.963631 | Whether it comes from a sense of duty or a desire to  succeed, you rarely flinch when confronted by fearsome  foes. If you roll a success on a saving throw against a fear  effect, you get a critical s |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/38` | 0.679326 | You're willful and stubborn, and you refuse to accept your  own failure—traits that have served you well in life and after  death. When you critically fail a saving throw against a  mental effect, you |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/53` | 0.622711 | You clear your mind of distractions and focus on your foe,  determined to overcome the shame of your failure lest it  forever blemish your reputation. The next time before the end  of your turn that y |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/39` | 0.574899 | **Deny Failure** [reaction] (fortune) **Frequency** once per day; **Trigger** You fail or critically fail a saving throw; **Effect** You refuse  to accept your failure! Reroll the triggering saving th |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/16` | 0.531281 | **Trigger** You critically succeed on a save against a fear effect  whose source was a creature, or a creature fails or critically  fails an Intimidation check to Demoralize you. |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/52` | 0.512396 | **Trigger** You critically fail a Strike against an enemy. |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/17` | 0.501073 | You laugh at your enemy's failed attempts to bully you,  turning the tables on your foe with a display of terrifying  bravado. You attempt an Intimidation check to Demoralize  the triggering creature. |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/15` | 0.499437 | When you're physically outmatched, you fight with  unexpected ferocity. If a foe of a larger size than you  critically hits and damages you, that foe is off-guard to you  for 1 round. |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/12/Text/14` | 0.486518 | You have an ominous presence that unnerves the living.  You have learned to harness this sinister aura to your  own advantage and can scare your foes with a focused  glance. Focus your ill intent at o |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/1/ListItem/8` | 0.482389 | Fear facing you in battle. |

### Query 83
- Text: What are the requirements for **VESK WEAPON FAMILIARITY** **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/2/SectionHeader/29']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/2/SectionHeader/29', 'PZO22001 Starfinder Player Core 074-091::/page/2/Text/7', 'PZO22001 Starfinder Player Core 074-091::/page/16/SectionHeader/2']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/2/SectionHeader/29` | 0.923246 | **VESK WEAPON FAMILIARITY** **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/2/Text/7` | 0.597815 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As a vesk, you choose from among the  following ance |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/16/SectionHeader/2` | 0.596831 | **TECH FAMILIARITY** **FEAT 1** |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/2/Text/31` | 0.558371 | **VESK** |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/32` | 0.549464 | **Prerequisites** plated vesk heritage or Armor Ace |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/2/Text/15` | 0.546371 | **VESK** |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/2/Text/11` | 0.546371 | **VESK** |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/61` | 0.546371 | **VESK** |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/2/Text/27` | 0.546371 | **VESK** |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/57` | 0.546371 | **VESK** |

### Query 84
- Text: What is the rule about You're trained with all doshkos. In addition, you gain access to  all uncommon weapons with the vesk trait. For the purposes  of proficiency, you treat any of these that are martial weapons?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/2/Text/32']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/2/Text/32', 'PZO22001 Starfinder Player Core 074-091::/page/2/Text/7', 'PZO22001 Starfinder Player Core 074-091::/page/3/Text/1']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/2/Text/32` | 0.986767 | You're trained with all doshkos. In addition, you gain access to  all uncommon weapons with the vesk trait. For the purposes  of proficiency, you treat any of these that are martial weapons |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/2/Text/7` | 0.573778 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As a vesk, you choose from among the  following ance |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/1` | 0.573534 | as simple weapons and any that are advanced weapons as  martial weapons. |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/1/SectionHeader/18` | 0.519272 | Most vesk in the Veskarium venerate Damoritosh the  Conqueror, god of duty and war, and his army of battle  saints. In life, the saints were mortal paragons who embodied  vesk cultural values and atta |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/4` | 0.517039 | Years of experience living among ysoki communities have  trained your nimble steps and sneaky moves. You gain the  trained proficiency rank in Acrobatics and Stealth. If you  would automatically becom |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/56` | 0.504830 | and conflicts within the Veskarium tend to be as disciplined  as they are violent, stretching to accommodate opposing  sides following the prescribed order of war. A typical vesk  always respects thei |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/2/Text/2` | 0.497235 | You're one of the notable vesk born with psychic talents.  According to folklore, your lineage originated with an  ancient cave-dwelling society on Vesk Prime who modified  themselves with occult ritu |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/10` | 0.492488 | If you want a character who's duty bound, brave, and stoic,  you should play a vesk. |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/15/Text/31` | 0.486692 | Triune chose you specifically to become a  prismeni. You hold the All-Code close in your  heart and cherish the data it's imparted upon  you. You become trained in Religion and Triune  Lore. You have |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/16` | 0.469287 | Vesk names typically combine elements of their parents'  names as well as those of other prominent ancestors.  Companions often shorten these names for casual use, but  doing so without permission is |

### Query 85
- Text: What are the requirements for **BLOOD SENSE** **FEAT 5**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/3/SectionHeader/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/3/SectionHeader/4', 'PZO22001 Starfinder Player Core 074-091::/page/12/SectionHeader/36', 'PZO22001 Starfinder Player Core 074-091::/page/13/Text/6']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/3/SectionHeader/4` | 0.880632 | **BLOOD SENSE** **FEAT 5** |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/12/SectionHeader/36` | 0.622921 | **SOUL SUSTENANCE** **FEAT 5** |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/6` | 0.608508 | **VOID BLOOD** **FEAT 5** |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/16` | 0.494741 | **PREHENSILE TAIL** **FEAT 5** |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/16/SectionHeader/12` | 0.485819 | **ELECTRICAL SHIELDING** **FEAT 5** |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/2` | 0.466568 | **UNLIVING MEMORIES** **FEAT 5** |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/16/SectionHeader/26` | 0.465676 | **SPECTRA TRANSMISSION **[one-action] **FEAT 5** |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/16/SectionHeader/7` | 0.443888 | **DRIFT HOP **[one-action] **FEAT 5** |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/6` | 0.443241 | You have a keen sense of smell and are capable of detecting  bloody wounds at a distance. You gain blood sense as an  imprecise sense with a range of 30 feet. This means you can  use your sense of sme |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/12/SectionHeader/32` | 0.438288 | **DEATHLY CONSTITUTION** **FEAT 5** |

### Query 86
- Text: What is the rule about You have a keen sense of smell and are capable of detecting  bloody wounds at a distance. You gain blood sense as an  imprecise sense with a range of 30 feet. This means you can  use your sense of smell to determine the exact location of a  living creature who isn't at its full Hit Points. Creatures that  don't have blood, such as oozes and most constructs, can't be  detected with your blood sense.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/3/Text/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/3/Text/6', 'PZO22001 Starfinder Player Core 074-091::/page/5/Text/32', 'PZO22001 Starfinder Player Core 074-091::/page/5/Text/31']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/6` | 0.999313 | You have a keen sense of smell and are capable of detecting  bloody wounds at a distance. You gain blood sense as an  imprecise sense with a range of 30 feet. This means you can  use your sense of sme |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/5/Text/32` | 0.623450 | In addition, you gain a +2 circumstance bonus to  Perception checks to Seek a creature or object within the  range of your scent. |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/5/Text/31` | 0.617242 | The long snouts that run in your family give you a keener  sense of smell than most ysoki. You gain imprecise scent with  a range of 30 feet. This means you can use your sense of  smell to determine a |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/12/Text/14` | 0.497200 | You have an ominous presence that unnerves the living.  You have learned to harness this sinister aura to your  own advantage and can scare your foes with a focused  glance. Focus your ill intent at o |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/15/Text/27` | 0.481646 | You became a prismeni after a close  encounter with one or more spectra.  You can communicate mentally with  spectra and with intelligent constructs  with the tech trait within 30 feet. You don't  nee |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/12/Text/30` | 0.464400 | Your living body is flush with vitality, which easily hides  your ichor-filled veins from sight. You don't have to attempt  Deception checks against a creature's Perception DC to  successfully Imperso |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/20` | 0.434439 | Your mere presence attracts restless spirits, haunted objects,  spiritually active substances, and fragmented souls, like a  magnet attracts metal. You manifest these spirit shards in a  chaotic whirl |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/40` | 0.428541 | When your foe is weak, you press on. When you successfully  Strike a creature that has the frightened or persistent  bleed condition with a melee or ranged weapon, you gain a  circumstance bonus to th |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/51` | 0.416313 | You have died once before and have no intention of dying  ever again; your soul stubbornly resuscitates your body  when you would otherwise perish. You are restored to 1  Hit Point, lose the dying and |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/10/ListItem/9` | 0.411251 | Confuse you with another type of undead and are  surprised when you breathe, eat, or sleep. |

### Query 87
- Text: What are the requirements for **MENACING SNARL **[free-action] **FEAT 5**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/3/SectionHeader/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/3/SectionHeader/7', 'PZO22001 Starfinder Player Core 074-091::/page/7/Text/20', 'PZO22001 Starfinder Player Core 074-091::/page/16/SectionHeader/7']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/3/SectionHeader/7` | 0.914853 | **MENACING SNARL **[free-action] **FEAT 5** |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/20` | 0.542780 | **QUICK STOW **[free-action] **FEAT 5** |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/16/SectionHeader/7` | 0.515176 | **DRIFT HOP **[one-action] **FEAT 5** |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/16` | 0.469628 | **PREHENSILE TAIL** **FEAT 5** |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/16/SectionHeader/12` | 0.458858 | **ELECTRICAL SHIELDING** **FEAT 5** |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/3/SectionHeader/19` | 0.453034 | **EAGER COMBATANT **[free-action] **FEAT 9** |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/16/SectionHeader/26` | 0.440681 | **SPECTRA TRANSMISSION **[one-action] **FEAT 5** |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/3/SectionHeader/41` | 0.433006 | **DAMORITOSH'S CLAW **[one-action] **FEAT 5** |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/12/SectionHeader/32` | 0.428539 | **DEATHLY CONSTITUTION** **FEAT 5** |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/13/SectionHeader/30` | 0.423234 | **INTUITIVE TALENT **[free-action] **FEAT 13** |

### Query 88
- Text: What is the rule about You snarl, hiss, shout, or otherwise verbally menace the  triggering creature as you frighten them. Increase the value  of the frightened condition by 1.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/3/Text/12']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/3/Text/12', 'PZO22001 Starfinder Player Core 074-091::/page/3/Text/11', 'PZO22001 Starfinder Player Core 074-091::/page/3/Text/17']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/12` | 0.987293 | You snarl, hiss, shout, or otherwise verbally menace the  triggering creature as you frighten them. Increase the value  of the frightened condition by 1. |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/11` | 0.696539 | **Trigger** You frighten a creature. |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/17` | 0.617092 | You laugh at your enemy's failed attempts to bully you,  turning the tables on your foe with a display of terrifying  bravado. You attempt an Intimidation check to Demoralize  the triggering creature. |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/16` | 0.569506 | **Trigger** You critically succeed on a save against a fear effect  whose source was a creature, or a creature fails or critically  fails an Intimidation check to Demoralize you. |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/12/Text/14` | 0.540326 | You have an ominous presence that unnerves the living.  You have learned to harness this sinister aura to your  own advantage and can scare your foes with a focused  glance. Focus your ill intent at o |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/12/Text/16` | 0.496626 | higher of your class DC or spell DC, or become frightened  1 (frightened 2 on a critical failure) and stupefied 1 as long  as it's frightened. Once you've used Baleful Gaze against a  creature, it's t |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/63` | 0.474175 | **Trigger** You deal the killing blow to an enemy. |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/45` | 0.473538 | **Trigger** An enemy occupying the same space as you uses a  manipulate action or a move action, makes a ranged attack,  or leaves a square during a move action it's using. |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/40` | 0.458255 | When your foe is weak, you press on. When you successfully  Strike a creature that has the frightened or persistent  bleed condition with a melee or ranged weapon, you gain a  circumstance bonus to th |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/20` | 0.456553 | Your mere presence attracts restless spirits, haunted objects,  spiritually active substances, and fragmented souls, like a  magnet attracts metal. You manifest these spirit shards in a  chaotic whirl |

### Query 89
- Text: What are the requirements for **TERRIFYING BRAVADO **[reaction] **FEAT 5**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/3/SectionHeader/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/3/SectionHeader/13', 'PZO22001 Starfinder Player Core 074-091::/page/16/SectionHeader/12', 'PZO22001 Starfinder Player Core 074-091::/page/7/Text/16']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/3/SectionHeader/13` | 0.902686 | **TERRIFYING BRAVADO **[reaction] **FEAT 5** |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/16/SectionHeader/12` | 0.487447 | **ELECTRICAL SHIELDING** **FEAT 5** |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/16` | 0.481620 | **PREHENSILE TAIL** **FEAT 5** |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/17` | 0.417208 | You laugh at your enemy's failed attempts to bully you,  turning the tables on your foe with a display of terrifying  bravado. You attempt an Intimidation check to Demoralize  the triggering creature. |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/16/SectionHeader/7` | 0.414799 | **DRIFT HOP **[one-action] **FEAT 5** |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/12/SectionHeader/32` | 0.410551 | **DEATHLY CONSTITUTION** **FEAT 5** |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/16/SectionHeader/26` | 0.407648 | **SPECTRA TRANSMISSION **[one-action] **FEAT 5** |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/6` | 0.407121 | **VOID BLOOD** **FEAT 5** |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/27` | 0.401426 | **Prerequisites** expert in Intimidation |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/12` | 0.398224 | You snarl, hiss, shout, or otherwise verbally menace the  triggering creature as you frighten them. Increase the value  of the frightened condition by 1. |

### Query 90
- Text: What is the rule about **Trigger** You critically succeed on a save against a fear effect  whose source was a creature, or a creature fails or critically  fails an Intimidation check to Demoralize you.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/3/Text/16']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/3/Text/16', 'PZO22001 Starfinder Player Core 074-091::/page/3/Text/52', 'PZO22001 Starfinder Player Core 074-091::/page/3/Text/17']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/16` | 0.953161 | **Trigger** You critically succeed on a save against a fear effect  whose source was a creature, or a creature fails or critically  fails an Intimidation check to Demoralize you. |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/52` | 0.708865 | **Trigger** You critically fail a Strike against an enemy. |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/17` | 0.707459 | You laugh at your enemy's failed attempts to bully you,  turning the tables on your foe with a display of terrifying  bravado. You attempt an Intimidation check to Demoralize  the triggering creature. |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/11` | 0.659127 | **Trigger** You frighten a creature. |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/19` | 0.570610 | **Trigger** An enemy's Strike or targeted effect would hit you,  and you weren't already concealed, hidden, or undetected  to that enemy. |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/46` | 0.570445 | You launch a surprise attack from below. Make a melee  Strike against the triggering creature. If your attack is a  critical hit and the trigger was a manipulate action, you  disrupt that action. This |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/63` | 0.561392 | **Trigger** You deal the killing blow to an enemy. |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/28` | 0.558835 | At the start of a combat encounter, if you are aware of your  foes and aren't attempting to Sneak or Hide, you can roll an  Intimidation check for your initiative and can use the result  to Demoralize |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/53` | 0.552676 | You clear your mind of distractions and focus on your foe,  determined to overcome the shame of your failure lest it  forever blemish your reputation. The next time before the end  of your turn that y |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/17/Text/17` | 0.551116 | **Trigger** An enemy's Strike would hit you, and you weren't  already concealed, hidden, or undetected to that enemy. |

### Query 91
- Text: What is the rule about You laugh at your enemy's failed attempts to bully you,  turning the tables on your foe with a display of terrifying  bravado. You attempt an Intimidation check to Demoralize  the triggering creature.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/3/Text/17']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/3/Text/17', 'PZO22001 Starfinder Player Core 074-091::/page/3/Text/28', 'PZO22001 Starfinder Player Core 074-091::/page/3/Text/16']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/17` | 0.961922 | You laugh at your enemy's failed attempts to bully you,  turning the tables on your foe with a display of terrifying  bravado. You attempt an Intimidation check to Demoralize  the triggering creature. |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/28` | 0.699184 | At the start of a combat encounter, if you are aware of your  foes and aren't attempting to Sneak or Hide, you can roll an  Intimidation check for your initiative and can use the result  to Demoralize |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/16` | 0.698920 | **Trigger** You critically succeed on a save against a fear effect  whose source was a creature, or a creature fails or critically  fails an Intimidation check to Demoralize you. |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/53` | 0.539187 | You clear your mind of distractions and focus on your foe,  determined to overcome the shame of your failure lest it  forever blemish your reputation. The next time before the end  of your turn that y |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/63` | 0.532630 | **Trigger** You deal the killing blow to an enemy. |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/12` | 0.526593 | You snarl, hiss, shout, or otherwise verbally menace the  triggering creature as you frighten them. Increase the value  of the frightened condition by 1. |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/52` | 0.516840 | **Trigger** You critically fail a Strike against an enemy. |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/12/Text/16` | 0.505169 | higher of your class DC or spell DC, or become frightened  1 (frightened 2 on a critical failure) and stupefied 1 as long  as it's frightened. Once you've used Baleful Gaze against a  creature, it's t |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/2/Text/28` | 0.499070 | Whether it comes from a sense of duty or a desire to  succeed, you rarely flinch when confronted by fearsome  foes. If you roll a success on a saving throw against a fear  effect, you get a critical s |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/22` | 0.497057 | **Trigger** You roll Athletics or Intimidation for initiative. |

### Query 92
- Text: What are the requirements for **EAGER COMBATANT **[free-action] **FEAT 9**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/3/SectionHeader/19']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/3/SectionHeader/19', 'PZO22001 Starfinder Player Core 074-091::/page/13/Text/11', 'PZO22001 Starfinder Player Core 074-091::/page/3/Text/46']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/3/SectionHeader/19` | 0.896750 | **EAGER COMBATANT **[free-action] **FEAT 9** |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/11` | 0.580640 | **RESONANT WEAPON **[one-action] **FEAT 9** |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/46` | 0.560274 | **Requirements** You're engaged in combat. |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/7/SectionHeader/36` | 0.447361 | **UNDERFOOT** **FEAT 9** |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/32` | 0.445132 | **OVERCROWD** **FEAT 9** |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/3/SectionHeader/48` | 0.441017 | **OVERCOME SHAME **[free-action] **FEAT 13** |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/3/SectionHeader/59` | 0.435490 | **BOLSTERED BY BATTLE **[free-action] **FEAT 17** |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/17/Text/6` | 0.430567 | **REMOTE ACCESS** **FEAT 9** |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/17/Text/3` | 0.430299 | **COSMIC TRAVELER** **FEAT 9** |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/13/SectionHeader/30` | 0.426918 | **INTUITIVE TALENT **[free-action] **FEAT 13** |

### Query 93
- Text: What is the rule about **Trigger** You roll Athletics or Intimidation for initiative.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/3/Text/22']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/3/Text/22', 'PZO22001 Starfinder Player Core 074-091::/page/7/Text/45', 'PZO22001 Starfinder Player Core 074-091::/page/3/Text/16']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/22` | 0.968005 | **Trigger** You roll Athletics or Intimidation for initiative. |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/45` | 0.576362 | **Trigger** An enemy occupying the same space as you uses a  manipulate action or a move action, makes a ranged attack,  or leaves a square during a move action it's using. |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/16` | 0.571977 | **Trigger** You critically succeed on a save against a fear effect  whose source was a creature, or a creature fails or critically  fails an Intimidation check to Demoralize you. |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/63` | 0.529418 | **Trigger** You deal the killing blow to an enemy. |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/17` | 0.514791 | You laugh at your enemy's failed attempts to bully you,  turning the tables on your foe with a display of terrifying  bravado. You attempt an Intimidation check to Demoralize  the triggering creature. |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/52` | 0.499933 | **Trigger** You critically fail a Strike against an enemy. |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/27` | 0.497028 | **Prerequisites** expert in Intimidation |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/28` | 0.490408 | At the start of a combat encounter, if you are aware of your  foes and aren't attempting to Sneak or Hide, you can roll an  Intimidation check for your initiative and can use the result  to Demoralize |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/11` | 0.488161 | **Trigger** You frighten a creature. |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/19` | 0.474844 | **Trigger** An enemy's Strike or targeted effect would hit you,  and you weren't already concealed, hidden, or undetected  to that enemy. |

### Query 94
- Text: What are the requirements for **OPENING ROAR** **FEAT 9**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/3/SectionHeader/24']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/3/SectionHeader/24', 'PZO22001 Starfinder Player Core 074-091::/page/17/Text/6', 'PZO22001 Starfinder Player Core 074-091::/page/7/SectionHeader/36']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/3/SectionHeader/24` | 0.907894 | **OPENING ROAR** **FEAT 9** |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/17/Text/6` | 0.579444 | **REMOTE ACCESS** **FEAT 9** |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/7/SectionHeader/36` | 0.567432 | **UNDERFOOT** **FEAT 9** |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/32` | 0.482450 | **OVERCROWD** **FEAT 9** |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/27` | 0.481377 | **BIG MOUTH** **FEAT 9** |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/11` | 0.465110 | **RESONANT WEAPON **[one-action] **FEAT 9** |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/3/SectionHeader/29` | 0.453107 | **PLATED DEFLECTION** **FEAT 9** |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/17/Text/3` | 0.441666 | **COSMIC TRAVELER** **FEAT 9** |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/17/Text/9` | 0.422357 | **REVITALIZED BY THE DRIFT** **FEAT 9** |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/13/SectionHeader/15` | 0.422157 | **SHROUD OF SHATTERED SPIRITS **[reaction] **FEAT 9** |

### Query 95
- Text: What are the requirements for **Prerequisites** expert in Intimidation?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/3/Text/27']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/3/Text/27', 'PZO22001 Starfinder Player Core 074-091::/page/3/Text/17', 'PZO22001 Starfinder Player Core 074-091::/page/3/Text/28']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/27` | 0.976481 | **Prerequisites** expert in Intimidation |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/17` | 0.516791 | You laugh at your enemy's failed attempts to bully you,  turning the tables on your foe with a display of terrifying  bravado. You attempt an Intimidation check to Demoralize  the triggering creature. |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/28` | 0.514369 | At the start of a combat encounter, if you are aware of your  foes and aren't attempting to Sneak or Hide, you can roll an  Intimidation check for your initiative and can use the result  to Demoralize |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/22` | 0.439095 | **Trigger** You roll Athletics or Intimidation for initiative. |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/12/Text/20` | 0.437559 | Since your resurrection, you've learned a lot about yourself,  your place in the cycle of souls, and other undead. You gain  the trained proficiency rank in Intimidation and Religion.  If you would au |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/16` | 0.434214 | **Trigger** You critically succeed on a save against a fear effect  whose source was a creature, or a creature fails or critically  fails an Intimidation check to Demoralize you. |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/44` | 0.390364 | **Prerequisites** Baleful Gaze |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/46` | 0.384141 | **Requirements** You're engaged in combat. |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/2/Text/24` | 0.377584 | You're a skilled leader. Whenever an ally selects you as the  target of their attempts to Follow the Expert, you increase  the circumstance bonus they receive to their skill check  by an additional +1 |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/12` | 0.356347 | You snarl, hiss, shout, or otherwise verbally menace the  triggering creature as you frighten them. Increase the value  of the frightened condition by 1. |

### Query 96
- Text: What is the rule about At the start of a combat encounter, if you are aware of your  foes and aren't attempting to Sneak or Hide, you can roll an  Intimidation check for your initiative and can use the result  to Demoralize one observed foe.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/3/Text/28']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/3/Text/28', 'PZO22001 Starfinder Player Core 074-091::/page/3/Text/17', 'PZO22001 Starfinder Player Core 074-091::/page/3/Text/16']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/28` | 1.000395 | At the start of a combat encounter, if you are aware of your  foes and aren't attempting to Sneak or Hide, you can roll an  Intimidation check for your initiative and can use the result  to Demoralize |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/17` | 0.696965 | You laugh at your enemy's failed attempts to bully you,  turning the tables on your foe with a display of terrifying  bravado. You attempt an Intimidation check to Demoralize  the triggering creature. |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/16` | 0.602908 | **Trigger** You critically succeed on a save against a fear effect  whose source was a creature, or a creature fails or critically  fails an Intimidation check to Demoralize you. |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/56` | 0.545535 | **Trigger** You successfully use Stealth to Hide and become  hidden from all your current foes, or use Stealth to Sneak  and become undetected to all your current foes. |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/12/Text/30` | 0.513805 | Your living body is flush with vitality, which easily hides  your ichor-filled veins from sight. You don't have to attempt  Deception checks against a creature's Perception DC to  successfully Imperso |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/27` | 0.502776 | **Prerequisites** expert in Intimidation |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/53` | 0.501637 | You clear your mind of distractions and focus on your foe,  determined to overcome the shame of your failure lest it  forever blemish your reputation. The next time before the end  of your turn that y |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/17/Text/17` | 0.500333 | **Trigger** An enemy's Strike would hit you, and you weren't  already concealed, hidden, or undetected to that enemy. |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/22` | 0.494818 | **Trigger** You roll Athletics or Intimidation for initiative. |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/19` | 0.494192 | **Trigger** An enemy's Strike or targeted effect would hit you,  and you weren't already concealed, hidden, or undetected  to that enemy. |

### Query 97
- Text: What are the requirements for **PLATED DEFLECTION** **FEAT 9**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/3/SectionHeader/29']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/3/SectionHeader/29', 'PZO22001 Starfinder Player Core 074-091::/page/7/SectionHeader/36', 'PZO22001 Starfinder Player Core 074-091::/page/7/Text/27']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/3/SectionHeader/29` | 0.913492 | **PLATED DEFLECTION** **FEAT 9** |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/7/SectionHeader/36` | 0.546396 | **UNDERFOOT** **FEAT 9** |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/27` | 0.525425 | **BIG MOUTH** **FEAT 9** |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/32` | 0.482296 | **OVERCROWD** **FEAT 9** |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/17/Text/6` | 0.472622 | **REMOTE ACCESS** **FEAT 9** |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/3/SectionHeader/24` | 0.468246 | **OPENING ROAR** **FEAT 9** |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/17/Text/9` | 0.438358 | **REVITALIZED BY THE DRIFT** **FEAT 9** |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/17/Text/3` | 0.437054 | **COSMIC TRAVELER** **FEAT 9** |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/13/SectionHeader/15` | 0.432068 | **SHROUD OF SHATTERED SPIRITS **[reaction] **FEAT 9** |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/33` | 0.417312 | You've mastered using your own plate scales or worn armor  to absorb devastating strikes. You gain the Plate Deflection |

### Query 98
- Text: What are the requirements for **Prerequisites** plated vesk heritage or Armor Ace?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/3/Text/32']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/3/Text/32', 'PZO22001 Starfinder Player Core 074-091::/page/1/SectionHeader/27', 'PZO22001 Starfinder Player Core 074-091::/page/1/Text/28']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/32` | 0.960817 | **Prerequisites** plated vesk heritage or Armor Ace |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/1/SectionHeader/27` | 0.596298 | PLATED VESK |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/28` | 0.588179 | Your ancestors were the hardiest specimens of vesk, having  traveled far and wide while enduring hostile environments.  Your scales count as medium armor in the plate armor group.  They grant a +3 ite |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/1/SectionHeader/21` | 0.517298 | VESK HERITAGES |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/2/Text/7` | 0.480243 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As a vesk, you choose from among the  following ance |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/22` | 0.464060 | Vesk lineages were shaped by the worlds they inhabited and  battled over. Choose one of the following vesk heritages at  1st level. |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/3/SectionHeader/31` | 0.463400 | **VESK** |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/10` | 0.458522 | If you want a character who's duty bound, brave, and stoic,  you should play a vesk. |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/2/SectionHeader/29` | 0.457727 | **VESK WEAPON FAMILIARITY** **FEAT 1** |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/61` | 0.451400 | **VESK** |

### Query 99
- Text: What is the rule about reaction.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/3/Text/34']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/3/Text/34', 'PZO22001 Starfinder Player Core 074-091::/page/16/Text/16', 'PZO22001 Starfinder Player Core 074-091::/page/7/Text/46']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/34` | 0.771952 | reaction. |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/16/Text/16` | 0.661693 | Current reaction. |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/46` | 0.386147 | You launch a surprise attack from below. Make a melee  Strike against the triggering creature. If your attack is a  critical hit and the trigger was a manipulate action, you  disrupt that action. This |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/63` | 0.333346 | **Trigger** You deal the killing blow to an enemy. |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/35` | 0.329240 | **Plate** **Deflection** [reaction] **Frequency** once per day; **Trigger** You're  struck by a critical hit; **Effect** You deflect the attack to a  heavily armored part of your body. You don't take |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/23` | 0.320679 | You eagerly stride into battle, giving no thought to the  consequences. You Stride in a straight line directly toward an  enemy. |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/41` | 0.319620 | **SKULKING STRIKE **[reaction] **FEAT 13** |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/51` | 0.316895 | You have died once before and have no intention of dying  ever again; your soul stubbornly resuscitates your body  when you would otherwise perish. You are restored to 1  Hit Point, lose the dying and |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/16/Text/17` | 0.316476 | **Redirect Current** [reaction] (electricity) **Frequency** once per hour;  **Trigger** You take electricity damage, and your electricity  resistance doesn't reduce this damage to 0; **Effect** After |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/13/SectionHeader/46` | 0.313455 | **UNDYING **[reaction] **FEAT 17** |

### Query 100
- Text: What is the rule about **Plate** **Deflection** [reaction] **Frequency** once per day; **Trigger** You're  struck by a critical hit; **Effect** You deflect the attack to a  heavily armored part of your body. You don't take double  damage from the critical hit but still take other effects.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/3/Text/35']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/3/Text/35', 'PZO22001 Starfinder Player Core 074-091::/page/3/Text/33', 'PZO22001 Starfinder Player Core 074-091::/page/7/Text/46']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/35` | 0.924246 | **Plate** **Deflection** [reaction] **Frequency** once per day; **Trigger** You're  struck by a critical hit; **Effect** You deflect the attack to a  heavily armored part of your body. You don't take |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/33` | 0.653238 | You've mastered using your own plate scales or worn armor  to absorb devastating strikes. You gain the Plate Deflection |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/46` | 0.599462 | You launch a surprise attack from below. Make a melee  Strike against the triggering creature. If your attack is a  critical hit and the trigger was a manipulate action, you  disrupt that action. This |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/16/Text/17` | 0.541019 | **Redirect Current** [reaction] (electricity) **Frequency** once per hour;  **Trigger** You take electricity damage, and your electricity  resistance doesn't reduce this damage to 0; **Effect** After |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/19` | 0.522193 | **Trigger** An enemy's Strike or targeted effect would hit you,  and you weren't already concealed, hidden, or undetected  to that enemy. |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/11/Text/16` | 0.521641 | **Soul Shield** [reaction] (void) **Frequency** once per day; **Trigger** You  would take void damage; **Effect** You push your soul out  of your body and use it as a shield to protect your living |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/45` | 0.517407 | **Trigger** An enemy occupying the same space as you uses a  manipulate action or a move action, makes a ranged attack,  or leaves a square during a move action it's using. |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/17/Text/17` | 0.501691 | **Trigger** An enemy's Strike would hit you, and you weren't  already concealed, hidden, or undetected to that enemy. |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/17/Text/49` | 0.500154 | **Cosmic Blast** [two-actions] (concentrate, fire, light, manipulate)  **Frequency** once per day; **Effect** You fire a powerful laser blast  in a 120-foot line, dealing 7d12 fire damage (basic Refle |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/2/Text/20` | 0.484016 | At 5th level, whenever you get a critical hit with one  of these attacks, you get its critical specialization effect. **Special** You can take this feat three times. Each time you  do, select a differ |

### Query 101
- Text: What are the requirements for **ADVANTAGEOUS ASSAULT** **FEAT 13**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/3/SectionHeader/37']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/3/SectionHeader/37', 'PZO22001 Starfinder Player Core 074-091::/page/17/SectionHeader/25', 'PZO22001 Starfinder Player Core 074-091::/page/13/SectionHeader/30']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/3/SectionHeader/37` | 0.907208 | **ADVANTAGEOUS ASSAULT** **FEAT 13** |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/17/SectionHeader/25` | 0.542797 | **FREQUENT DRIFTER** **FEAT 13** |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/13/SectionHeader/30` | 0.539154 | **INTUITIVE TALENT **[free-action] **FEAT 13** |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/7` | 0.473002 | **EXPLOSIVE SURPRISE** **FEAT 13** |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/3/SectionHeader/48` | 0.441191 | **OVERCOME SHAME **[free-action] **FEAT 13** |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/17/SectionHeader/30` | 0.440507 | **SCRAMBLE TECH** **FEAT 13** |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/17/Text/19` | 0.433125 | **ENCODE PRESENCE **[two-actions] **FEAT 13** |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/17/Text/14` | 0.422159 | **DRIFT BLINK **[reaction] **FEAT 13** |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/41` | 0.411068 | **SKULKING STRIKE **[reaction] **FEAT 13** |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/46` | 0.409616 | **Requirements** You're engaged in combat. |

### Query 102
- Text: What is the rule about When your foe is weak, you press on. When you successfully  Strike a creature that has the frightened or persistent  bleed condition with a melee or ranged weapon, you gain a  circumstance bonus to the damage roll equal to the number  of weapon damage dice of the weapon used for the Strike.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/3/Text/40']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/3/Text/40', 'PZO22001 Starfinder Player Core 074-091::/page/7/Text/46', 'PZO22001 Starfinder Player Core 074-091::/page/3/Text/53']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/40` | 0.983724 | When your foe is weak, you press on. When you successfully  Strike a creature that has the frightened or persistent  bleed condition with a melee or ranged weapon, you gain a  circumstance bonus to th |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/46` | 0.621719 | You launch a surprise attack from below. Make a melee  Strike against the triggering creature. If your attack is a  critical hit and the trigger was a manipulate action, you  disrupt that action. This |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/53` | 0.547410 | You clear your mind of distractions and focus on your foe,  determined to overcome the shame of your failure lest it  forever blemish your reputation. The next time before the end  of your turn that y |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/2/Text/24` | 0.500845 | You're a skilled leader. Whenever an ally selects you as the  target of their attempts to Follow the Expert, you increase  the circumstance bonus they receive to their skill check  by an additional +1 |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/17/Text/39` | 0.489374 | **Requirements** Your last action was a melee Strike that  critically hit a creature. |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/5/Text/32` | 0.486315 | In addition, you gain a +2 circumstance bonus to  Perception checks to Seek a creature or object within the  range of your scent. |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/52` | 0.476883 | **Trigger** You critically fail a Strike against an enemy. |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/28` | 0.459750 | At the start of a combat encounter, if you are aware of your  foes and aren't attempting to Sneak or Hide, you can roll an  Intimidation check for your initiative and can use the result  to Demoralize |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/2` | 0.456400 | At 5th level, whenever you get a critical hit with one of  these weapons, you get its critical specialization effect. |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/64` | 0.451787 | You don't just fight because you have to; the threat of battle  and the thrill of victory invigorate you. You gain a number of  temporary Hit Points equal to your level. These temporary  Hit Points la |

### Query 103
- Text: What are the requirements for **DAMORITOSH'S CLAW **[one-action] **FEAT 5**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/3/SectionHeader/41']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/3/SectionHeader/41', 'PZO22001 Starfinder Player Core 074-091::/page/16/SectionHeader/7', 'PZO22001 Starfinder Player Core 074-091::/page/16/SectionHeader/26']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/3/SectionHeader/41` | 0.893455 | **DAMORITOSH'S CLAW **[one-action] **FEAT 5** |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/16/SectionHeader/7` | 0.575971 | **DRIFT HOP **[one-action] **FEAT 5** |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/16/SectionHeader/26` | 0.512721 | **SPECTRA TRANSMISSION **[one-action] **FEAT 5** |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/20` | 0.453146 | **QUICK STOW **[free-action] **FEAT 5** |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/16` | 0.450406 | **PREHENSILE TAIL** **FEAT 5** |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/3/SectionHeader/7` | 0.442097 | **MENACING SNARL **[free-action] **FEAT 5** |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/15/SectionHeader/17` | 0.424802 | **DRIFT-TOUCHED **[one-action] **FEAT 1** |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/3/SectionHeader/4` | 0.423221 | **BLOOD SENSE** **FEAT 5** |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/2/Text/16` | 0.420229 | You're a natural predator trained to use part of your body  as a weapon. When you select this feat, you gain one of the  following unarmed attacks of your choice: claw, jaws, or tail.  Each of these a |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/11` | 0.418918 | **RESONANT WEAPON **[one-action] **FEAT 9** |

### Query 104
- Text: What are the requirements for **Prerequisites** focus pool?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/3/Text/44']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/3/Text/44', 'PZO22001 Starfinder Player Core 074-091::/page/7/Text/44', 'PZO22001 Starfinder Player Core 074-091::/page/17/Text/28']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/44` | 0.944885 | **Prerequisites** focus pool |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/44` | 0.443553 | **Prerequisites** Underfoot |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/17/Text/28` | 0.433716 | **Prerequisites** Drift Hop |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/44` | 0.372377 | **Prerequisites** Baleful Gaze |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/17/Text/47` | 0.361881 | **Prerequisites** Cosmic Traveler |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/27` | 0.350063 | **Prerequisites** expert in Intimidation |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/10` | 0.343773 | **Prerequisites** Cheek Pouches |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/23` | 0.343773 | **Prerequisites** Cheek Pouches |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/30` | 0.343773 | **Prerequisites** Cheek Pouches |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/46` | 0.338150 | **Requirements** You're engaged in combat. |

### Query 105
- Text: What are the requirements for **OVERCOME SHAME **[free-action] **FEAT 13**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/3/SectionHeader/48']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/3/SectionHeader/48', 'PZO22001 Starfinder Player Core 074-091::/page/13/SectionHeader/30', 'PZO22001 Starfinder Player Core 074-091::/page/17/SectionHeader/30']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/3/SectionHeader/48` | 0.911339 | **OVERCOME SHAME **[free-action] **FEAT 13** |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/13/SectionHeader/30` | 0.592107 | **INTUITIVE TALENT **[free-action] **FEAT 13** |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/17/SectionHeader/30` | 0.521732 | **SCRAMBLE TECH** **FEAT 13** |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/17/Text/19` | 0.476419 | **ENCODE PRESENCE **[two-actions] **FEAT 13** |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/3/SectionHeader/19` | 0.455708 | **EAGER COMBATANT **[free-action] **FEAT 9** |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/7` | 0.435149 | **EXPLOSIVE SURPRISE** **FEAT 13** |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/3/SectionHeader/37` | 0.431111 | **ADVANTAGEOUS ASSAULT** **FEAT 13** |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/7/SectionHeader/52` | 0.419199 | **SLIP FROM SIGHT **[free-action] **FEAT 17** |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/3/SectionHeader/59` | 0.416189 | **BOLSTERED BY BATTLE **[free-action] **FEAT 17** |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/17/SectionHeader/25` | 0.412871 | **FREQUENT DRIFTER** **FEAT 13** |

### Query 106
- Text: What is the rule about You clear your mind of distractions and focus on your foe,  determined to overcome the shame of your failure lest it  forever blemish your reputation. The next time before the end  of your turn that you attempt a Strike with the same weapon  and target as the triggering attack, you roll the attack roll  twice and use the higher result. If the attack misses, you're  overwhelmed with shame, becoming off-guard until the end  of your next turn.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/3/Text/53']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/3/Text/53', 'PZO22001 Starfinder Player Core 074-091::/page/3/Text/52', 'PZO22001 Starfinder Player Core 074-091::/page/17/Text/18']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/53` | 0.992691 | You clear your mind of distractions and focus on your foe,  determined to overcome the shame of your failure lest it  forever blemish your reputation. The next time before the end  of your turn that y |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/52` | 0.642716 | **Trigger** You critically fail a Strike against an enemy. |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/17/Text/18` | 0.604770 | You momentarily slip into the Drift, becoming concealed  against the triggering Strike. If the flat check for concealment  fails, the Strike misses you. After resolving the triggering  Strike, you ree |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/2/Text/28` | 0.555498 | Whether it comes from a sense of duty or a desire to  succeed, you rarely flinch when confronted by fearsome  foes. If you roll a success on a saving throw against a fear  effect, you get a critical s |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/20` | 0.537574 | Your mere presence attracts restless spirits, haunted objects,  spiritually active substances, and fragmented souls, like a  magnet attracts metal. You manifest these spirit shards in a  chaotic whirl |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/46` | 0.534537 | You launch a surprise attack from below. Make a melee  Strike against the triggering creature. If your attack is a  critical hit and the trigger was a manipulate action, you  disrupt that action. This |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/17` | 0.529969 | You laugh at your enemy's failed attempts to bully you,  turning the tables on your foe with a display of terrifying  bravado. You attempt an Intimidation check to Demoralize  the triggering creature. |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/17/Text/17` | 0.527934 | **Trigger** An enemy's Strike would hit you, and you weren't  already concealed, hidden, or undetected to that enemy. |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/15` | 0.524040 | When you're physically outmatched, you fight with  unexpected ferocity. If a foe of a larger size than you  critically hits and damages you, that foe is off-guard to you  for 1 round. |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/38` | 0.523909 | You're willful and stubborn, and you refuse to accept your  own failure—traits that have served you well in life and after  death. When you critically fail a saving throw against a  mental effect, you |

### Query 107
- Text: What are the requirements for **BATTLE SAINT** **FEAT 17**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/3/SectionHeader/55']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/3/SectionHeader/55', 'PZO22001 Starfinder Player Core 074-091::/page/3/SectionHeader/59', 'PZO22001 Starfinder Player Core 074-091::/page/13/SectionHeader/41']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/3/SectionHeader/55` | 0.899087 | **BATTLE SAINT** **FEAT 17** |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/3/SectionHeader/59` | 0.601959 | **BOLSTERED BY BATTLE **[free-action] **FEAT 17** |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/13/SectionHeader/41` | 0.573617 | **BALEFUL PRESENCE** **FEAT 17** |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/13/SectionHeader/46` | 0.480610 | **UNDYING **[reaction] **FEAT 17** |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/17/SectionHeader/44` | 0.470469 | **SPECTRA ASCENDANT** **FEAT 17** |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/17/SectionHeader/35` | 0.441002 | **DRIFT STRIKE **[one-action] **FEAT 17** |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/3/SectionHeader/54` | 0.437593 | 17TH LEVEL |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/13/SectionHeader/40` | 0.437593 | 17TH LEVEL |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/7/SectionHeader/52` | 0.437026 | **SLIP FROM SIGHT **[free-action] **FEAT 17** |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/7/SectionHeader/47` | 0.425593 | 17TH LEVEL |

### Query 108
- Text: What is the rule about You have ascended to the rank of living battle saint and are  on a path to become a true divine servant of Damoritosh  when you meet him in the afterlife. You can cast *bless*ed  *boundary* and *divine decree* as 7th-rank divine innate spells  once per day each.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/3/Text/58']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/3/Text/58', 'PZO22001 Starfinder Player Core 074-091::/page/7/Text/51', 'PZO22001 Starfinder Player Core 074-091::/page/17/Text/1']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/58` | 0.999355 | You have ascended to the rank of living battle saint and are  on a path to become a true divine servant of Damoritosh  when you meet him in the afterlife. You can cast *bless*ed  *boundary* and *divin |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/51` | 0.643721 | Your steadfast faith in Grandmother Rat yields more  rewards. You gain *divine decree* as a 7th-rank divine innate  spell once per day. Additionally, once per month, whenever  you would die, your body |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/17/Text/1` | 0.636513 | has improved. You gain *delete* and *supercharge weapon* as 1st-rank divine innate spells. You can cast each of these  divine innate spells once per day. |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/47` | 0.543565 | You pray to Damoritosh (or a battle saint) for a blessing in the  heat of battle—and he answers. You regain 1 Focus Point, up  to your usual maximum. |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/12/Text/25` | 0.517502 | You exist on the boundaries between life and death, and  you can channel your own imbalanced spiritual essence into  magical spells. Choose one of the following cantrips: *vitality* *lash* or *void* * |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/17/Text/33` | 0.487435 | With a thought, you can infect a technological creature or  device with a short-lived virus, causing the object to glitch  and malfunction. You can cast *discharge* as a 3rd-rank divine  innate spell |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/12/Text/20` | 0.470005 | Since your resurrection, you've learned a lot about yourself,  your place in the cycle of souls, and other undead. You gain  the trained proficiency rank in Intimidation and Religion.  If you would au |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/16/Text/20` | 0.467866 | Your body produces an overabundance of electrical energy,  which you can emit as a blast of lightning or use to power  technological devices. You can cast the *electric arc* cantrip as  a divine innat |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/1/SectionHeader/18` | 0.467523 | Most vesk in the Veskarium venerate Damoritosh the  Conqueror, god of duty and war, and his army of battle  saints. In life, the saints were mortal paragons who embodied  vesk cultural values and atta |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/5` | 0.458708 | Some element of your borai nature gives you flashes from  the beyond: visions from the afterlife you were intended for  or might still one day obtain. You gain the trained proficiency  rank in Religio |

### Query 109
- Text: What are the requirements for **BOLSTERED BY BATTLE **[free-action] **FEAT 17**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/3/SectionHeader/59']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/3/SectionHeader/59', 'PZO22001 Starfinder Player Core 074-091::/page/3/SectionHeader/55', 'PZO22001 Starfinder Player Core 074-091::/page/7/SectionHeader/52']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/3/SectionHeader/59` | 0.907682 | **BOLSTERED BY BATTLE **[free-action] **FEAT 17** |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/3/SectionHeader/55` | 0.614632 | **BATTLE SAINT** **FEAT 17** |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/7/SectionHeader/52` | 0.588466 | **SLIP FROM SIGHT **[free-action] **FEAT 17** |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/13/SectionHeader/41` | 0.487484 | **BALEFUL PRESENCE** **FEAT 17** |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/46` | 0.480564 | **Requirements** You're engaged in combat. |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/17/SectionHeader/35` | 0.469128 | **DRIFT STRIKE **[one-action] **FEAT 17** |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/3/SectionHeader/19` | 0.462503 | **EAGER COMBATANT **[free-action] **FEAT 9** |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/13/SectionHeader/46` | 0.462181 | **UNDYING **[reaction] **FEAT 17** |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/13/SectionHeader/30` | 0.453181 | **INTUITIVE TALENT **[free-action] **FEAT 13** |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/3/SectionHeader/48` | 0.432967 | **OVERCOME SHAME **[free-action] **FEAT 13** |

### Query 110
- Text: What is the rule about You don't just fight because you have to; the threat of battle  and the thrill of victory invigorate you. You gain a number of  temporary Hit Points equal to your level. These temporary  Hit Points last for 1 minute or until the encounter ends,  whichever comes first.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/3/Text/64']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/3/Text/64', 'PZO22001 Starfinder Player Core 074-091::/page/3/Text/53', 'PZO22001 Starfinder Player Core 074-091::/page/17/Text/12']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/64` | 0.983871 | You don't just fight because you have to; the threat of battle  and the thrill of victory invigorate you. You gain a number of  temporary Hit Points equal to your level. These temporary  Hit Points la |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/53` | 0.556260 | You clear your mind of distractions and focus on your foe,  determined to overcome the shame of your failure lest it  forever blemish your reputation. The next time before the end  of your turn that y |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/17/Text/12` | 0.541793 | Once per hour, you can focus or meditate on your inherent  connection to the Drift. This is a 10-minute activity that has  the concentrate and exploration traits. When you do, you're  treated as if yo |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/17/Text/11` | 0.499113 | The Drift revitalizes your spirit and restores your vitality,  physically healing your wounds. If you rest for 10 minutes  while within the Drift, you gain Hit Points equal to your  Constitution modif |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/52` | 0.483595 | **Trigger** You critically fail a Strike against an enemy. |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/23` | 0.479092 | You eagerly stride into battle, giving no thought to the  consequences. You Stride in a straight line directly toward an  enemy. |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/40` | 0.478593 | When your foe is weak, you press on. When you successfully  Strike a creature that has the frightened or persistent  bleed condition with a melee or ranged weapon, you gain a  circumstance bonus to th |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/19` | 0.478406 | **Trigger** An enemy's Strike or targeted effect would hit you,  and you weren't already concealed, hidden, or undetected  to that enemy. |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/17/Text/17` | 0.470889 | **Trigger** An enemy's Strike would hit you, and you weren't  already concealed, hidden, or undetected to that enemy. |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/51` | 0.464903 | You have died once before and have no intention of dying  ever again; your soul stubbornly resuscitates your body  when you would otherwise perish. You are restored to 1  Hit Point, lose the dying and |

### Query 111
- Text: What is the rule about **ANCESTRIES & ** **BACKGROUNDS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/3/Text/67']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/17/Text/52', 'PZO22001 Starfinder Player Core 074-091::/page/1/Text/31', 'PZO22001 Starfinder Player Core 074-091::/page/3/Text/67']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/17/Text/52` | 0.920820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/31` | 0.920820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/67` | 0.920820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/60` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/5/Text/35` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/15/Text/34` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/54` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/11/Text/21` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/9/Text/20` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/9/Text/33` | 0.526957 | **Backgrounds** |

### Query 112
- Text: What is the rule about **Backgrounds**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/3/Text/81']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/1/Text/43', 'PZO22001 Starfinder Player Core 074-091::/page/3/Text/81', 'PZO22001 Starfinder Player Core 074-091::/page/15/Text/47']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/43` | 0.796516 | **Backgrounds** |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/81` | 0.796516 | **Backgrounds** |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/15/Text/47` | 0.796516 | **Backgrounds** |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/9/Text/33` | 0.754516 | **Backgrounds** |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/17/Text/65` | 0.754516 | **Backgrounds** |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/72` | 0.754516 | **Backgrounds** |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/68` | 0.754516 | **Backgrounds** |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/5/Text/49` | 0.661389 | **Backgrounds** **Languages** |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/15/Text/34` | 0.510451 | **ANCESTRIES & ** **BACKGROUNDS** |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/9/Text/20` | 0.510451 | **ANCESTRIES & ** **BACKGROUNDS** |

### Query 113
- Text: What is the rule about **CLASSES** **SKILLS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/3/Text/83']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/3/Text/83', 'PZO22001 Starfinder Player Core 074-091::/page/7/Text/75', 'PZO22001 Starfinder Player Core 074-091::/page/13/Text/71']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/83` | 0.874079 | **CLASSES** **SKILLS** |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/75` | 0.730507 | **SKILLS** |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/71` | 0.730507 | **SKILLS** |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/5/Text/51` | 0.688507 | **SKILLS** |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/46` | 0.688507 | **SKILLS** |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/17/Text/68` | 0.688506 | **SKILLS** |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/5/Text/50` | 0.656063 | **CLASSES** |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/74` | 0.656063 | **CLASSES** |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/70` | 0.656063 | **CLASSES** |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/45` | 0.656063 | **CLASSES** |

### Query 114
- Text: What is the rule about **FEATS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/3/Text/84']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/3/Text/84', 'PZO22001 Starfinder Player Core 074-091::/page/7/Text/76', 'PZO22001 Starfinder Player Core 074-091::/page/1/Text/47']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/84` | 0.871817 | **FEATS** |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/47` | 0.871817 | **FEATS** |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/76` | 0.871817 | **FEATS** |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/5/Text/52` | 0.829817 | **FEATS** |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/72` | 0.829817 | **FEATS** |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/17/Text/69` | 0.702296 | **FEATS** **EQUIPMENT** |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/9/Text/36` | 0.653037 | **SKILLS** **FEATS** |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/15/Text/50` | 0.653037 | **SKILLS** **FEATS** |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/9/SectionHeader/4` | 0.460192 | LINEAGE FEATS |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/7/SectionHeader/36` | 0.439162 | **UNDERFOOT** **FEAT 9** |

### Query 115
- Text: What is the rule about **SPELLS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/3/Text/86']
- Expected found: `True`
- Expected rank: `5`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/9/Text/38', 'PZO22001 Starfinder Player Core 074-091::/page/15/Text/52', 'PZO22001 Starfinder Player Core 074-091::/page/1/Text/49']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/9/Text/38` | 0.889304 | **SPELLS** |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/15/Text/52` | 0.889304 | **SPELLS** |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/49` | 0.889304 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/74` | 0.847304 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/86` | 0.847304 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/79` | 0.847304 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/17/Text/70` | 0.847304 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/5/Text/54` | 0.847304 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/75` | 0.388254 | **SKILLS** |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/46` | 0.388254 | **SKILLS** |

### Query 116
- Text: What is the rule about Once known as ratfolk, ysoki are clever and flexible. With roots on countless worlds, ysoki work alongside larger species, helping to establish communities and accomplish tough tasks. From the largest of crowds to the tightest of tunnels, a ysoki always knows how to find their way.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/4/Text/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/4/Text/2', 'PZO22001 Starfinder Player Core 074-091::/page/6/Text/2', 'PZO22001 Starfinder Player Core 074-091::/page/5/Text/16']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/4/Text/2` | 0.994147 | Once known as ratfolk, ysoki are clever and flexible. With roots on countless worlds, ysoki work alongside larger species, helping to establish communities and accomplish tough tasks. From the largest |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/6/Text/2` | 0.721009 | Ysoki are sometimes referred to as ratfolk by other  ancestries and use the ratfolk trait. This was especially  true in the distant past. In Starfinder, individuals of  this ancestry are more commonly |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/5/Text/16` | 0.703683 | Ysoki culture values life over credits, framing work as another  communal activity to enjoy. Ysoki communities are tight-knit  and welcoming, always eager to share a meal or swap spare  parts with str |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/5/Text/11` | 0.659063 | If you want a character who's adventurous, confident, and  curious, you should play a ysoki. |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/5/Text/10` | 0.647066 | Most ysoki love technology and travel, even gravitating  toward professions that others find unpleasant. Ysoki often  work as junkers, long-haul starship crew members, or  mechanics squeezing through |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/5/Text/21` | 0.619590 | Ysoki care more about their family than abstract moral  concepts, and most ysoki follow their community's strict  social codes even if they break civil laws. Community is  important to all ysoki, and |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/5/Text/13` | 0.605777 | Ysoki have whiskered snouts, large ears, and hairless tails, with  red or black eyes and fur colors typically in shades of black,  brown, gray, and white. Ysoki appearances vary considerably,  even wi |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/5/Text/17` | 0.602305 | Nicknames are often as important to ysoki as their given  names, and they enjoy giving their friends and family  monikers based on their appearance or personality, such as |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/5/Text/9` | 0.591506 | Ysoki populations thrived on Akiton, lost Golarion, and several  other worlds for millennia before spaceflight accelerated  cultural exchange in the Pact System. The question of  whether these ethnici |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/5/Text/14` | 0.577994 | Ysoki instinctually maintain cleanliness through personal  grooming and reinforce these habits throughout their strong  social structures. Many ysoki use cosmetics to spice up their  looks and favor c |

### Query 117
- Text: What is the rule about Additional languages equal to your Intelligence modifier (if it's positive). Choose from the list of common languages and any other languages to which you have access (such as the languages prevalent on your home world).?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/4/Text/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/4/Text/9', 'PZO22001 Starfinder Player Core 074-091::/page/0/Text/9', 'PZO22001 Starfinder Player Core 074-091::/page/9/Text/7']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/4/Text/9` | 0.982267 | Additional languages equal to your Intelligence modifier (if it's positive). Choose from the list of common languages and any other languages to which you have access (such as the languages prevalent |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/0/Text/9` | 0.947517 | One regional language of your choice Additional languages equal to your Intelligence modifier (if it's positive). Choose from the list of common languages and any other languages to which you have acc |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/9/Text/7` | 0.521321 | This book includes the rules for two kinds of versatile  heritages and rules for other mixed ancestral heritages. |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/15/Text/27` | 0.465298 | You became a prismeni after a close  encounter with one or more spectra.  You can communicate mentally with  spectra and with intelligent constructs  with the tech trait within 30 feet. You don't  nee |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/9/Text/2` | 0.452697 | Sometimes a versatile heritage might give you an ability that  conflicts with an ability from your ancestry. In these cases, you  choose which of the conflicting abilities your character has. |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/5/Text/49` | 0.450808 | **Backgrounds** **Languages** |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/16/Text/5` | 0.438072 | You have an intuitive understanding of  computers, machines, and other technological  devices. You become trained in Computers and  Crafting. If you would automatically become trained  in one of those |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/9/Text/16` | 0.437530 | You can choose a mixed ancestry to represent having two  ancestral lines for your character. This doesn't preclude  having more than two ancestries in your genealogy, but  you'll need to work with you |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/8/Text/11` | 0.437273 | To play a character with a versatile heritage, first select your  ancestry, just like you would for any character. You gain  Hit Points, size, Speed, attribute boosts and attribute flaws,  languages, |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/8/Text/7` | 0.431365 | The Pact Worlds is home to a variety of versatile heritages.  Some are born to unusual creatures or arise through specific  mundane or supernatural circumstances. Because the  circumstances that give |

### Query 118
- Text: What is the rule about **TRAITS **?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/4/SectionHeader/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/4/SectionHeader/10', 'PZO22001 Starfinder Player Core 074-091::/page/0/SectionHeader/10', 'PZO22001 Starfinder Player Core 074-091::/page/7/Text/75']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/4/SectionHeader/10` | 0.867974 | **TRAITS ** |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/0/SectionHeader/10` | 0.769948 | TRAITS |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/75` | 0.506114 | **SKILLS** |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/46` | 0.464114 | **SKILLS** |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/5/Text/51` | 0.464114 | **SKILLS** |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/71` | 0.464114 | **SKILLS** |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/17/Text/68` | 0.464114 | **SKILLS** |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/83` | 0.453915 | **CLASSES** **SKILLS** |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/9/Text/5` | 0.452490 | Some ancestry feats within a versatile heritage have the  lineage trait. These feats specify a physiological lineage your  character has—such as if a prismeni was born in the Drift or  chosen by Triun |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/15/Text/50` | 0.452322 | **SKILLS** **FEATS** |

### Query 119
- Text: What are the requirements for **CHEEK POUCHES** **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/6/SectionHeader/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/6/SectionHeader/13', 'PZO22001 Starfinder Player Core 074-091::/page/7/Text/30', 'PZO22001 Starfinder Player Core 074-091::/page/7/Text/10']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/6/SectionHeader/13` | 0.884804 | **CHEEK POUCHES** **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/10` | 0.741424 | **Prerequisites** Cheek Pouches |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/30` | 0.741424 | **Prerequisites** Cheek Pouches |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/23` | 0.699424 | **Prerequisites** Cheek Pouches |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/6/Text/16` | 0.455219 | Your cheeks are stretchy, and you can store up to four items  of light Bulk or less in these cheek pouches. None of these  items can have a dimension longer than 1 foot. As long as  you have at least |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/25` | 0.451147 | You're trained in the trick of quickly moving items into your  cheek pouches. You Interact to store one held item in your  cheek pouches (provided it fits). |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/31` | 0.418990 | Your cheek pouches are especially large and stretchy. Instead  of storing up to four items of light Bulk in your cheek pouches,  you can store up to 1 Bulk worth of items. The maximum size  of a given |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/16/Text/37` | 0.408401 | **DATA JOCKEY** **FEAT 1** |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/17/Text/69` | 0.404624 | **FEATS** **EQUIPMENT** |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/2/SectionHeader/9` | 0.399726 | **ARMOR ACE** **FEAT 1** |

### Query 120
- Text: What are the requirements for **GRANDMOTHER'S LORE** **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/6/SectionHeader/17']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/6/SectionHeader/17', 'PZO22001 Starfinder Player Core 074-091::/page/7/SectionHeader/48', 'PZO22001 Starfinder Player Core 074-091::/page/16/SectionHeader/22']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/6/SectionHeader/17` | 0.875222 | **GRANDMOTHER'S LORE** **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/7/SectionHeader/48` | 0.612745 | **GRANDMOTHER'S FAVORITE** **FEAT 17** |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/16/SectionHeader/22` | 0.580562 | **PRISMENI LORE** **FEAT 1** |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/1` | 0.524723 | **YSOKI LORE** **FEAT 1** |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/12/SectionHeader/17` | 0.477499 | **BORAI LORE** **FEAT 1** |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/2/SectionHeader/9` | 0.441214 | **ARMOR ACE** **FEAT 1** |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/12/SectionHeader/1` | 0.404294 | **HEADSTRONG** **FEAT 1** |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/3/SectionHeader/24` | 0.385124 | **OPENING ROAR** **FEAT 9** |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/16/Text/1` | 0.383732 | You also gain the Additional Lore general feat for  Prismeni Lore. |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/15/SectionHeader/24` | 0.371141 | **SPECTRASOUL** **FEAT 1** |

### Query 121
- Text: What are the requirements for **NIMBLE TAIL** **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/6/SectionHeader/22']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/6/SectionHeader/22', 'PZO22001 Starfinder Player Core 074-091::/page/7/Text/16', 'PZO22001 Starfinder Player Core 074-091::/page/12/SectionHeader/1']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/6/SectionHeader/22` | 0.884999 | **NIMBLE TAIL** **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/16` | 0.589541 | **PREHENSILE TAIL** **FEAT 5** |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/12/SectionHeader/1` | 0.470472 | **HEADSTRONG** **FEAT 1** |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/9/Text/36` | 0.424834 | **SKILLS** **FEATS** |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/15/Text/50` | 0.424834 | **SKILLS** **FEATS** |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/13/SectionHeader/30` | 0.411453 | **INTUITIVE TALENT **[free-action] **FEAT 13** |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/17/Text/69` | 0.403403 | **FEATS** **EQUIPMENT** |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/12/SectionHeader/5` | 0.399026 | **NECROTIZED** **FEAT 1** |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/2/SectionHeader/9` | 0.394054 | **ARMOR ACE** **FEAT 1** |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/16/SectionHeader/18` | 0.391468 | **LIVING BATTERY** **FEAT 1** |

### Query 122
- Text: What are the requirements for **TINKERING FINGERS** **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/6/SectionHeader/26']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/6/SectionHeader/26', 'PZO22001 Starfinder Player Core 074-091::/page/12/SectionHeader/1', 'PZO22001 Starfinder Player Core 074-091::/page/15/SectionHeader/17']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/6/SectionHeader/26` | 0.868132 | **TINKERING FINGERS** **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/12/SectionHeader/1` | 0.474136 | **HEADSTRONG** **FEAT 1** |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/15/SectionHeader/17` | 0.470179 | **DRIFT-TOUCHED **[one-action] **FEAT 1** |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/11/Text/13` | 0.403196 | **ETHERIC** **FEAT 1** |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/15/Text/50` | 0.403054 | **SKILLS** **FEATS** |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/9/Text/36` | 0.403054 | **SKILLS** **FEATS** |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/6/SectionHeader/22` | 0.392476 | **NIMBLE TAIL** **FEAT 1** |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/15/SectionHeader/28` | 0.384832 | **TRIUNE'S CHOSEN** **FEAT 1** |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/2/SectionHeader/21` | 0.383500 | **COMMAND TACTICS** **FEAT 1** |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/44` | 0.378534 | **Prerequisites** Underfoot |

### Query 123
- Text: What are the requirements for **YSOKI LORE** **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/7/Text/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/7/Text/1', 'PZO22001 Starfinder Player Core 074-091::/page/12/SectionHeader/17', 'PZO22001 Starfinder Player Core 074-091::/page/16/SectionHeader/22']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/1` | 0.883440 | **YSOKI LORE** **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/12/SectionHeader/17` | 0.657612 | **BORAI LORE** **FEAT 1** |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/16/SectionHeader/22` | 0.607219 | **PRISMENI LORE** **FEAT 1** |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/5` | 0.551374 | You also gain the Additional Lore general feat for Ysoki  Lore. |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/6/Text/11` | 0.526367 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th,  9th, 13th, and 17th levels). As a ysoki, you select from  among the following an |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/6/SectionHeader/10` | 0.502094 | YSOKI ANCESTRY FEATS |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/6/SectionHeader/17` | 0.500576 | **GRANDMOTHER'S LORE** **FEAT 1** |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/3` | 0.499742 | **YSOKI** |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/4/SectionHeader/1` | 0.491613 | **YSOKI ** |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/43` | 0.487742 | **YSOKI** |

### Query 124
- Text: What are the requirements for **EXPLOSIVE SURPRISE** **FEAT 13**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/7/Text/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/7/Text/7', 'PZO22001 Starfinder Player Core 074-091::/page/3/SectionHeader/37', 'PZO22001 Starfinder Player Core 074-091::/page/13/SectionHeader/30']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/7` | 0.876507 | **EXPLOSIVE SURPRISE** **FEAT 13** |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/3/SectionHeader/37` | 0.533716 | **ADVANTAGEOUS ASSAULT** **FEAT 13** |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/13/SectionHeader/30` | 0.529567 | **INTUITIVE TALENT **[free-action] **FEAT 13** |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/17/Text/19` | 0.481351 | **ENCODE PRESENCE **[two-actions] **FEAT 13** |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/17/SectionHeader/25` | 0.470641 | **FREQUENT DRIFTER** **FEAT 13** |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/3/SectionHeader/48` | 0.463431 | **OVERCOME SHAME **[free-action] **FEAT 13** |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/17/SectionHeader/30` | 0.453065 | **SCRAMBLE TECH** **FEAT 13** |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/41` | 0.442578 | **SKULKING STRIKE **[reaction] **FEAT 13** |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/13/SectionHeader/35` | 0.432167 | **STUBBORN CORPSE** **FEAT 13** |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/87` | 0.414916 | 13TH LEVEL |

### Query 125
- Text: What are the requirements for **Prerequisites** Cheek Pouches?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/7/Text/10']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/7/Text/23', 'PZO22001 Starfinder Player Core 074-091::/page/7/Text/10', 'PZO22001 Starfinder Player Core 074-091::/page/7/Text/30']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/23` | 0.964389 | **Prerequisites** Cheek Pouches |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/10` | 0.964389 | **Prerequisites** Cheek Pouches |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/30` | 0.964389 | **Prerequisites** Cheek Pouches |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/6/SectionHeader/13` | 0.587102 | **CHEEK POUCHES** **FEAT 1** |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/6/Text/16` | 0.563447 | Your cheeks are stretchy, and you can store up to four items  of light Bulk or less in these cheek pouches. None of these  items can have a dimension longer than 1 foot. As long as  you have at least |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/31` | 0.541867 | Your cheek pouches are especially large and stretchy. Instead  of storing up to four items of light Bulk in your cheek pouches,  you can store up to 1 Bulk worth of items. The maximum size  of a given |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/25` | 0.519691 | You're trained in the trick of quickly moving items into your  cheek pouches. You Interact to store one held item in your  cheek pouches (provided it fits). |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/44` | 0.368266 | **Prerequisites** Underfoot |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/44` | 0.355959 | **Prerequisites** focus pool |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/44` | 0.341552 | **Prerequisites** Baleful Gaze |

### Query 126
- Text: What are the requirements for **CORNERED FURY** **FEAT 5**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/7/Text/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/7/Text/13', 'PZO22001 Starfinder Player Core 074-091::/page/16/SectionHeader/12', 'PZO22001 Starfinder Player Core 074-091::/page/7/Text/16']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/13` | 0.889829 | **CORNERED FURY** **FEAT 5** |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/16/SectionHeader/12` | 0.527732 | **ELECTRICAL SHIELDING** **FEAT 5** |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/16` | 0.496245 | **PREHENSILE TAIL** **FEAT 5** |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/6` | 0.422115 | **VOID BLOOD** **FEAT 5** |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/16/SectionHeader/7` | 0.418861 | **DRIFT HOP **[one-action] **FEAT 5** |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/12/SectionHeader/32` | 0.414583 | **DEATHLY CONSTITUTION** **FEAT 5** |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/16/SectionHeader/31` | 0.406035 | **TECH CASTER** **FEAT 5** |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/3/SectionHeader/4` | 0.401355 | **BLOOD SENSE** **FEAT 5** |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/12/SectionHeader/36` | 0.398181 | **SOUL SUSTENANCE** **FEAT 5** |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/2` | 0.397346 | **UNLIVING MEMORIES** **FEAT 5** |

### Query 127
- Text: What are the requirements for **PREHENSILE TAIL** **FEAT 5**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/7/Text/16']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/7/Text/16', 'PZO22001 Starfinder Player Core 074-091::/page/6/SectionHeader/22', 'PZO22001 Starfinder Player Core 074-091::/page/16/SectionHeader/12']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/16` | 0.897193 | **PREHENSILE TAIL** **FEAT 5** |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/6/SectionHeader/22` | 0.564240 | **NIMBLE TAIL** **FEAT 1** |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/16/SectionHeader/12` | 0.535124 | **ELECTRICAL SHIELDING** **FEAT 5** |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/3/SectionHeader/4` | 0.465338 | **BLOOD SENSE** **FEAT 5** |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/16/SectionHeader/31` | 0.444053 | **TECH CASTER** **FEAT 5** |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/16/SectionHeader/26` | 0.437303 | **SPECTRA TRANSMISSION **[one-action] **FEAT 5** |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/12/SectionHeader/32` | 0.436733 | **DEATHLY CONSTITUTION** **FEAT 5** |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/12/SectionHeader/36` | 0.434517 | **SOUL SUSTENANCE** **FEAT 5** |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/2` | 0.430039 | **UNLIVING MEMORIES** **FEAT 5** |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/16/SectionHeader/7` | 0.418974 | **DRIFT HOP **[one-action] **FEAT 5** |

### Query 128
- Text: What are the requirements for **QUICK STOW **[free-action] **FEAT 5**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/7/Text/20']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/7/Text/20', 'PZO22001 Starfinder Player Core 074-091::/page/16/SectionHeader/7', 'PZO22001 Starfinder Player Core 074-091::/page/3/SectionHeader/7']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/20` | 0.885637 | **QUICK STOW **[free-action] **FEAT 5** |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/16/SectionHeader/7` | 0.554197 | **DRIFT HOP **[one-action] **FEAT 5** |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/3/SectionHeader/7` | 0.528322 | **MENACING SNARL **[free-action] **FEAT 5** |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/13/SectionHeader/30` | 0.450131 | **INTUITIVE TALENT **[free-action] **FEAT 13** |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/9/Text/36` | 0.445655 | **SKILLS** **FEATS** |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/15/Text/50` | 0.445655 | **SKILLS** **FEATS** |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/16` | 0.443850 | **PREHENSILE TAIL** **FEAT 5** |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/16/SectionHeader/12` | 0.436868 | **ELECTRICAL SHIELDING** **FEAT 5** |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/6` | 0.432036 | **VOID BLOOD** **FEAT 5** |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/7/SectionHeader/52` | 0.431539 | **SLIP FROM SIGHT **[free-action] **FEAT 17** |

### Query 129
- Text: What are the requirements for **Prerequisites** Cheek Pouches?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/7/Text/23']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/7/Text/23', 'PZO22001 Starfinder Player Core 074-091::/page/7/Text/10', 'PZO22001 Starfinder Player Core 074-091::/page/7/Text/30']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/23` | 0.964389 | **Prerequisites** Cheek Pouches |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/10` | 0.964389 | **Prerequisites** Cheek Pouches |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/30` | 0.964389 | **Prerequisites** Cheek Pouches |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/6/SectionHeader/13` | 0.587102 | **CHEEK POUCHES** **FEAT 1** |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/6/Text/16` | 0.563447 | Your cheeks are stretchy, and you can store up to four items  of light Bulk or less in these cheek pouches. None of these  items can have a dimension longer than 1 foot. As long as  you have at least |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/31` | 0.541867 | Your cheek pouches are especially large and stretchy. Instead  of storing up to four items of light Bulk in your cheek pouches,  you can store up to 1 Bulk worth of items. The maximum size  of a given |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/25` | 0.519691 | You're trained in the trick of quickly moving items into your  cheek pouches. You Interact to store one held item in your  cheek pouches (provided it fits). |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/44` | 0.368266 | **Prerequisites** Underfoot |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/44` | 0.355959 | **Prerequisites** focus pool |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/44` | 0.341552 | **Prerequisites** Baleful Gaze |

### Query 130
- Text: What are the requirements for **BIG MOUTH** **FEAT 9**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/7/Text/27']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/7/Text/27', 'PZO22001 Starfinder Player Core 074-091::/page/7/SectionHeader/36', 'PZO22001 Starfinder Player Core 074-091::/page/7/Text/32']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/27` | 0.894307 | **BIG MOUTH** **FEAT 9** |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/7/SectionHeader/36` | 0.563965 | **UNDERFOOT** **FEAT 9** |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/32` | 0.562448 | **OVERCROWD** **FEAT 9** |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/17/Text/6` | 0.511482 | **REMOTE ACCESS** **FEAT 9** |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/3/SectionHeader/24` | 0.496966 | **OPENING ROAR** **FEAT 9** |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/3/SectionHeader/29` | 0.492780 | **PLATED DEFLECTION** **FEAT 9** |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/17/Text/3` | 0.455509 | **COSMIC TRAVELER** **FEAT 9** |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/17/Text/9` | 0.428181 | **REVITALIZED BY THE DRIFT** **FEAT 9** |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/11` | 0.420008 | **RESONANT WEAPON **[one-action] **FEAT 9** |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/3/SectionHeader/19` | 0.402849 | **EAGER COMBATANT **[free-action] **FEAT 9** |

### Query 131
- Text: What are the requirements for **Prerequisites** Cheek Pouches?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/7/Text/30']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/7/Text/23', 'PZO22001 Starfinder Player Core 074-091::/page/7/Text/10', 'PZO22001 Starfinder Player Core 074-091::/page/7/Text/30']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/23` | 0.964389 | **Prerequisites** Cheek Pouches |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/10` | 0.964389 | **Prerequisites** Cheek Pouches |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/30` | 0.964389 | **Prerequisites** Cheek Pouches |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/6/SectionHeader/13` | 0.587102 | **CHEEK POUCHES** **FEAT 1** |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/6/Text/16` | 0.563447 | Your cheeks are stretchy, and you can store up to four items  of light Bulk or less in these cheek pouches. None of these  items can have a dimension longer than 1 foot. As long as  you have at least |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/31` | 0.541867 | Your cheek pouches are especially large and stretchy. Instead  of storing up to four items of light Bulk in your cheek pouches,  you can store up to 1 Bulk worth of items. The maximum size  of a given |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/25` | 0.519691 | You're trained in the trick of quickly moving items into your  cheek pouches. You Interact to store one held item in your  cheek pouches (provided it fits). |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/44` | 0.368266 | **Prerequisites** Underfoot |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/44` | 0.355959 | **Prerequisites** focus pool |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/44` | 0.341552 | **Prerequisites** Baleful Gaze |

### Query 132
- Text: What are the requirements for **OVERCROWD** **FEAT 9**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/7/Text/32']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/7/Text/32', 'PZO22001 Starfinder Player Core 074-091::/page/7/SectionHeader/36', 'PZO22001 Starfinder Player Core 074-091::/page/17/Text/6']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/32` | 0.893174 | **OVERCROWD** **FEAT 9** |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/7/SectionHeader/36` | 0.626498 | **UNDERFOOT** **FEAT 9** |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/17/Text/6` | 0.558345 | **REMOTE ACCESS** **FEAT 9** |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/27` | 0.506362 | **BIG MOUTH** **FEAT 9** |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/17/Text/9` | 0.488783 | **REVITALIZED BY THE DRIFT** **FEAT 9** |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/17/Text/3` | 0.486881 | **COSMIC TRAVELER** **FEAT 9** |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/3/SectionHeader/24` | 0.485577 | **OPENING ROAR** **FEAT 9** |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/3/SectionHeader/29` | 0.475942 | **PLATED DEFLECTION** **FEAT 9** |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/13/SectionHeader/15` | 0.474233 | **SHROUD OF SHATTERED SPIRITS **[reaction] **FEAT 9** |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/11` | 0.462355 | **RESONANT WEAPON **[one-action] **FEAT 9** |

### Query 133
- Text: What are the requirements for **UNDERFOOT** **FEAT 9**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/7/SectionHeader/36']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/7/SectionHeader/36', 'PZO22001 Starfinder Player Core 074-091::/page/7/Text/44', 'PZO22001 Starfinder Player Core 074-091::/page/17/Text/6']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/7/SectionHeader/36` | 0.906234 | **UNDERFOOT** **FEAT 9** |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/44` | 0.597241 | **Prerequisites** Underfoot |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/17/Text/6` | 0.573567 | **REMOTE ACCESS** **FEAT 9** |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/32` | 0.531451 | **OVERCROWD** **FEAT 9** |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/3/SectionHeader/24` | 0.482395 | **OPENING ROAR** **FEAT 9** |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/17/Text/69` | 0.475562 | **FEATS** **EQUIPMENT** |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/17/Text/3` | 0.463468 | **COSMIC TRAVELER** **FEAT 9** |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/3/SectionHeader/29` | 0.460861 | **PLATED DEFLECTION** **FEAT 9** |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/72` | 0.452856 | **FEATS** |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/5/Text/52` | 0.452856 | **FEATS** |

### Query 134
- Text: What are the requirements for **Prerequisites** shipborn ysoki or tunnel ysoki heritage?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/7/Text/39']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/7/Text/39', 'PZO22001 Starfinder Player Core 074-091::/page/6/SectionHeader/3', 'PZO22001 Starfinder Player Core 074-091::/page/5/SectionHeader/24']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/39` | 0.948304 | **Prerequisites** shipborn ysoki or tunnel ysoki heritage |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/6/SectionHeader/3` | 0.607638 | SHIPBORN YSOKI |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/5/SectionHeader/24` | 0.590981 | YSOKI HERITAGES |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/5/Text/25` | 0.555942 | Ysoki adapt to almost any environment throughout the  galaxy. Some ysoki put down roots on different worlds or live  entirely on board generation ships that sail the stars. Choose  one of the followin |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/6/Text/11` | 0.527325 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th,  9th, 13th, and 17th levels). As a ysoki, you select from  among the following an |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/6/Text/2` | 0.480665 | Ysoki are sometimes referred to as ratfolk by other  ancestries and use the ratfolk trait. This was especially  true in the distant past. In Starfinder, individuals of  this ancestry are more commonly |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/5/Text/18` | 0.480617 | "Snack," "Dot," "Sparks," or "Boom-Boom." Many ysoki family  names incorporate their ships or home settlements. |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/77` | 0.480288 | **Ysoki** |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/40` | 0.480288 | **Ysoki** |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/64` | 0.480288 | **Ysoki** |

### Query 135
- Text: What are the requirements for **SKULKING STRIKE **[reaction] **FEAT 13**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/7/Text/41']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/7/Text/41', 'PZO22001 Starfinder Player Core 074-091::/page/17/Text/14', 'PZO22001 Starfinder Player Core 074-091::/page/17/SectionHeader/35']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/41` | 0.915993 | **SKULKING STRIKE **[reaction] **FEAT 13** |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/17/Text/14` | 0.561020 | **DRIFT BLINK **[reaction] **FEAT 13** |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/17/SectionHeader/35` | 0.551328 | **DRIFT STRIKE **[one-action] **FEAT 17** |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/13/SectionHeader/30` | 0.449824 | **INTUITIVE TALENT **[free-action] **FEAT 13** |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/17/SectionHeader/30` | 0.440253 | **SCRAMBLE TECH** **FEAT 13** |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/17/SectionHeader/25` | 0.421099 | **FREQUENT DRIFTER** **FEAT 13** |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/3/SectionHeader/48` | 0.419408 | **OVERCOME SHAME **[free-action] **FEAT 13** |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/13/SectionHeader/35` | 0.417901 | **STUBBORN CORPSE** **FEAT 13** |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/7` | 0.415116 | **EXPLOSIVE SURPRISE** **FEAT 13** |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/17/Text/39` | 0.413627 | **Requirements** Your last action was a melee Strike that  critically hit a creature. |

### Query 136
- Text: What are the requirements for **Prerequisites** Underfoot?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/7/Text/44']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/7/Text/44', 'PZO22001 Starfinder Player Core 074-091::/page/3/Text/44', 'PZO22001 Starfinder Player Core 074-091::/page/7/SectionHeader/36']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/44` | 0.955083 | **Prerequisites** Underfoot |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/44` | 0.442176 | **Prerequisites** focus pool |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/7/SectionHeader/36` | 0.437401 | **UNDERFOOT** **FEAT 9** |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/46` | 0.383113 | **Requirements** You're engaged in combat. |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/27` | 0.346273 | **Prerequisites** expert in Intimidation |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/30` | 0.346243 | **Prerequisites** Cheek Pouches |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/10` | 0.346243 | **Prerequisites** Cheek Pouches |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/23` | 0.346243 | **Prerequisites** Cheek Pouches |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/44` | 0.345800 | **Prerequisites** Baleful Gaze |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/17/Text/28` | 0.340308 | **Prerequisites** Drift Hop |

### Query 137
- Text: What are the requirements for **GRANDMOTHER'S FAVORITE** **FEAT 17**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/7/SectionHeader/48']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/7/SectionHeader/48', 'PZO22001 Starfinder Player Core 074-091::/page/6/SectionHeader/17', 'PZO22001 Starfinder Player Core 074-091::/page/13/SectionHeader/46']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/7/SectionHeader/48` | 0.877251 | **GRANDMOTHER'S FAVORITE** **FEAT 17** |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/6/SectionHeader/17` | 0.607178 | **GRANDMOTHER'S LORE** **FEAT 1** |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/13/SectionHeader/46` | 0.504396 | **UNDYING **[reaction] **FEAT 17** |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/13/SectionHeader/41` | 0.446982 | **BALEFUL PRESENCE** **FEAT 17** |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/17/SectionHeader/44` | 0.446334 | **SPECTRA ASCENDANT** **FEAT 17** |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/7/SectionHeader/47` | 0.437209 | 17TH LEVEL |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/3/SectionHeader/55` | 0.431252 | **BATTLE SAINT** **FEAT 17** |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/3/SectionHeader/54` | 0.425209 | 17TH LEVEL |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/13/SectionHeader/40` | 0.425209 | 17TH LEVEL |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/17/Text/34` | 0.425209 | 17TH LEVEL |

### Query 138
- Text: What are the requirements for **SLIP FROM SIGHT **[free-action] **FEAT 17**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/7/SectionHeader/52']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/7/SectionHeader/52', 'PZO22001 Starfinder Player Core 074-091::/page/17/SectionHeader/35', 'PZO22001 Starfinder Player Core 074-091::/page/3/SectionHeader/59']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/7/SectionHeader/52` | 0.917572 | **SLIP FROM SIGHT **[free-action] **FEAT 17** |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/17/SectionHeader/35` | 0.609879 | **DRIFT STRIKE **[one-action] **FEAT 17** |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/3/SectionHeader/59` | 0.607794 | **BOLSTERED BY BATTLE **[free-action] **FEAT 17** |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/17/SectionHeader/44` | 0.496340 | **SPECTRA ASCENDANT** **FEAT 17** |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/13/SectionHeader/30` | 0.477836 | **INTUITIVE TALENT **[free-action] **FEAT 13** |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/20` | 0.475998 | **QUICK STOW **[free-action] **FEAT 5** |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/13/SectionHeader/46` | 0.472643 | **UNDYING **[reaction] **FEAT 17** |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/3/SectionHeader/55` | 0.472299 | **BATTLE SAINT** **FEAT 17** |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/13/SectionHeader/41` | 0.470462 | **BALEFUL PRESENCE** **FEAT 17** |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/3/SectionHeader/48` | 0.452059 | **OVERCOME SHAME **[free-action] **FEAT 13** |

### Query 139
- Text: What are the requirements for **ETHERIC** **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/11/Text/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/11/Text/13', 'PZO22001 Starfinder Player Core 074-091::/page/12/SectionHeader/1', 'PZO22001 Starfinder Player Core 074-091::/page/15/SectionHeader/24']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/11/Text/13` | 0.869301 | **ETHERIC** **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/12/SectionHeader/1` | 0.499956 | **HEADSTRONG** **FEAT 1** |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/15/SectionHeader/24` | 0.482964 | **SPECTRASOUL** **FEAT 1** |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/17/Text/69` | 0.438530 | **FEATS** **EQUIPMENT** |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/2/SectionHeader/9` | 0.435927 | **ARMOR ACE** **FEAT 1** |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/84` | 0.431654 | **FEATS** |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/76` | 0.431654 | **FEATS** |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/5/Text/52` | 0.431654 | **FEATS** |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/1/Text/47` | 0.431654 | **FEATS** |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/72` | 0.431654 | **FEATS** |

### Query 140
- Text: What are the requirements for **HEADSTRONG** **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/12/SectionHeader/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/12/SectionHeader/1', 'PZO22001 Starfinder Player Core 074-091::/page/15/SectionHeader/24', 'PZO22001 Starfinder Player Core 074-091::/page/9/Text/36']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/12/SectionHeader/1` | 0.892327 | **HEADSTRONG** **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/15/SectionHeader/24` | 0.530506 | **SPECTRASOUL** **FEAT 1** |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/9/Text/36` | 0.493410 | **SKILLS** **FEATS** |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/15/Text/50` | 0.451410 | **SKILLS** **FEATS** |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/2/SectionHeader/9` | 0.444950 | **ARMOR ACE** **FEAT 1** |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/16/SectionHeader/7` | 0.425379 | **DRIFT HOP **[one-action] **FEAT 5** |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/11/Text/13` | 0.425169 | **ETHERIC** **FEAT 1** |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/17/Text/69` | 0.423845 | **FEATS** **EQUIPMENT** |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/6` | 0.416336 | **VOID BLOOD** **FEAT 5** |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/15/SectionHeader/17` | 0.412031 | **DRIFT-TOUCHED **[one-action] **FEAT 1** |

### Query 141
- Text: What are the requirements for **NECROTIZED** **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/12/SectionHeader/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/12/SectionHeader/5', 'PZO22001 Starfinder Player Core 074-091::/page/6/SectionHeader/22', 'PZO22001 Starfinder Player Core 074-091::/page/11/Text/13']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/12/SectionHeader/5` | 0.860089 | **NECROTIZED** **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/6/SectionHeader/22` | 0.486991 | **NIMBLE TAIL** **FEAT 1** |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/11/Text/13` | 0.470760 | **ETHERIC** **FEAT 1** |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/12/SectionHeader/27` | 0.421875 | **ONLY SLIGHTLY DEAD** **FEAT 1** |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/12/SectionHeader/1` | 0.419792 | **HEADSTRONG** **FEAT 1** |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/15/SectionHeader/24` | 0.419187 | **SPECTRASOUL** **FEAT 1** |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/15/SectionHeader/17` | 0.411378 | **DRIFT-TOUCHED **[one-action] **FEAT 1** |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/32` | 0.395291 | **OVERCROWD** **FEAT 9** |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/2/SectionHeader/9` | 0.394571 | **ARMOR ACE** **FEAT 1** |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/17/Text/9` | 0.387159 | **REVITALIZED BY THE DRIFT** **FEAT 9** |

### Query 142
- Text: What are the requirements for **BALEFUL GAZE **[one-action] **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/12/SectionHeader/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/12/SectionHeader/10', 'PZO22001 Starfinder Player Core 074-091::/page/13/Text/44', 'PZO22001 Starfinder Player Core 074-091::/page/13/Text/45']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/12/SectionHeader/10` | 0.895416 | **BALEFUL GAZE **[one-action] **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/44` | 0.657618 | **Prerequisites** Baleful Gaze |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/45` | 0.528286 | You've learned to unleash the anger and malice you've built  up over the course of your life and restless undeath against  multiple foes at once, creating a potent effect around  yourself. You can cho |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/15/SectionHeader/17` | 0.474832 | **DRIFT-TOUCHED **[one-action] **FEAT 1** |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/13/SectionHeader/41` | 0.460812 | **BALEFUL PRESENCE** **FEAT 17** |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/16/SectionHeader/7` | 0.458130 | **DRIFT HOP **[one-action] **FEAT 5** |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/11` | 0.443043 | **RESONANT WEAPON **[one-action] **FEAT 9** |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/16/SectionHeader/26` | 0.432881 | **SPECTRA TRANSMISSION **[one-action] **FEAT 5** |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/12/Text/16` | 0.432652 | higher of your class DC or spell DC, or become frightened  1 (frightened 2 on a critical failure) and stupefied 1 as long  as it's frightened. Once you've used Baleful Gaze against a  creature, it's t |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/2/SectionHeader/9` | 0.425207 | **ARMOR ACE** **FEAT 1** |

### Query 143
- Text: What are the requirements for **BORAI LORE** **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/12/SectionHeader/17']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/12/SectionHeader/17', 'PZO22001 Starfinder Player Core 074-091::/page/7/Text/1', 'PZO22001 Starfinder Player Core 074-091::/page/9/Text/31']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/12/SectionHeader/17` | 0.891218 | **BORAI LORE** **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/1` | 0.656865 | **YSOKI LORE** **FEAT 1** |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/9/Text/31` | 0.650305 | **Borai** |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/12/SectionHeader/19` | 0.616875 | **BORAI** |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/5/Text/47` | 0.608305 | **Borai** |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/3/Text/79` | 0.608305 | **Borai** |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/15/Text/45` | 0.608305 | **Borai** |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/66` | 0.608305 | **Borai** |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/17/Text/63` | 0.608305 | **Borai** |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/23` | 0.604875 | **BORAI** |

### Query 144
- Text: What are the requirements for **DEATH-TOUCHED CASTER** **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/12/SectionHeader/22']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/12/SectionHeader/22', 'PZO22001 Starfinder Player Core 074-091::/page/15/SectionHeader/17', 'PZO22001 Starfinder Player Core 074-091::/page/16/SectionHeader/31']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/12/SectionHeader/22` | 0.884356 | **DEATH-TOUCHED CASTER** **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/15/SectionHeader/17` | 0.565399 | **DRIFT-TOUCHED **[one-action] **FEAT 1** |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/16/SectionHeader/31` | 0.564553 | **TECH CASTER** **FEAT 5** |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/12/SectionHeader/27` | 0.453508 | **ONLY SLIGHTLY DEAD** **FEAT 1** |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/12/SectionHeader/32` | 0.444429 | **DEATHLY CONSTITUTION** **FEAT 5** |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/2/SectionHeader/21` | 0.401435 | **COMMAND TACTICS** **FEAT 1** |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/12/SectionHeader/5` | 0.400530 | **NECROTIZED** **FEAT 1** |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/6/SectionHeader/22` | 0.389574 | **NIMBLE TAIL** **FEAT 1** |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/12/SectionHeader/1` | 0.386318 | **HEADSTRONG** **FEAT 1** |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/17/Text/39` | 0.372108 | **Requirements** Your last action was a melee Strike that  critically hit a creature. |

### Query 145
- Text: What are the requirements for **ONLY SLIGHTLY DEAD** **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/12/SectionHeader/27']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/12/SectionHeader/27', 'PZO22001 Starfinder Player Core 074-091::/page/12/SectionHeader/5', 'PZO22001 Starfinder Player Core 074-091::/page/16/SectionHeader/7']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/12/SectionHeader/27` | 0.855901 | **ONLY SLIGHTLY DEAD** **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/12/SectionHeader/5` | 0.480450 | **NECROTIZED** **FEAT 1** |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/16/SectionHeader/7` | 0.469794 | **DRIFT HOP **[one-action] **FEAT 5** |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/15/SectionHeader/17` | 0.423595 | **DRIFT-TOUCHED **[one-action] **FEAT 1** |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/12/SectionHeader/22` | 0.420690 | **DEATH-TOUCHED CASTER** **FEAT 1** |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/12/SectionHeader/32` | 0.413440 | **DEATHLY CONSTITUTION** **FEAT 5** |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/2/SectionHeader/25` | 0.409441 | **FEARLESS** **FEAT 1** |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/12/SectionHeader/1` | 0.406667 | **HEADSTRONG** **FEAT 1** |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/6/SectionHeader/22` | 0.405478 | **NIMBLE TAIL** **FEAT 1** |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/9/Text/36` | 0.397604 | **SKILLS** **FEATS** |

### Query 146
- Text: What are the requirements for **DEATHLY CONSTITUTION** **FEAT 5**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/12/SectionHeader/32']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/12/SectionHeader/32', 'PZO22001 Starfinder Player Core 074-091::/page/13/Text/2', 'PZO22001 Starfinder Player Core 074-091::/page/7/Text/16']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/12/SectionHeader/32` | 0.890508 | **DEATHLY CONSTITUTION** **FEAT 5** |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/2` | 0.518823 | **UNLIVING MEMORIES** **FEAT 5** |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/16` | 0.504319 | **PREHENSILE TAIL** **FEAT 5** |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/16/SectionHeader/12` | 0.456432 | **ELECTRICAL SHIELDING** **FEAT 5** |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/16/SectionHeader/7` | 0.455371 | **DRIFT HOP **[one-action] **FEAT 5** |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/6` | 0.447091 | **VOID BLOOD** **FEAT 5** |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/12/SectionHeader/36` | 0.444224 | **SOUL SUSTENANCE** **FEAT 5** |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/3/SectionHeader/4` | 0.444062 | **BLOOD SENSE** **FEAT 5** |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/16/SectionHeader/31` | 0.415237 | **TECH CASTER** **FEAT 5** |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/16/SectionHeader/26` | 0.409747 | **SPECTRA TRANSMISSION **[one-action] **FEAT 5** |

### Query 147
- Text: What are the requirements for **SOUL SUSTENANCE** **FEAT 5**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/12/SectionHeader/36']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/12/SectionHeader/36', 'PZO22001 Starfinder Player Core 074-091::/page/3/SectionHeader/4', 'PZO22001 Starfinder Player Core 074-091::/page/16/SectionHeader/12']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/12/SectionHeader/36` | 0.917872 | **SOUL SUSTENANCE** **FEAT 5** |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/3/SectionHeader/4` | 0.604806 | **BLOOD SENSE** **FEAT 5** |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/16/SectionHeader/12` | 0.503113 | **ELECTRICAL SHIELDING** **FEAT 5** |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/16` | 0.448674 | **PREHENSILE TAIL** **FEAT 5** |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/6` | 0.438372 | **VOID BLOOD** **FEAT 5** |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/2` | 0.435078 | **UNLIVING MEMORIES** **FEAT 5** |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/15/Text/50` | 0.430417 | **SKILLS** **FEATS** |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/9/Text/36` | 0.430417 | **SKILLS** **FEATS** |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/12/SectionHeader/32` | 0.415567 | **DEATHLY CONSTITUTION** **FEAT 5** |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/16/SectionHeader/26` | 0.409163 | **SPECTRA TRANSMISSION **[one-action] **FEAT 5** |

### Query 148
- Text: What are the requirements for **UNLIVING MEMORIES** **FEAT 5**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/13/Text/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/13/Text/2', 'PZO22001 Starfinder Player Core 074-091::/page/3/SectionHeader/4', 'PZO22001 Starfinder Player Core 074-091::/page/12/SectionHeader/32']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/2` | 0.866126 | **UNLIVING MEMORIES** **FEAT 5** |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/3/SectionHeader/4` | 0.528874 | **BLOOD SENSE** **FEAT 5** |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/12/SectionHeader/32` | 0.522760 | **DEATHLY CONSTITUTION** **FEAT 5** |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/12/SectionHeader/36` | 0.479073 | **SOUL SUSTENANCE** **FEAT 5** |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/16` | 0.474921 | **PREHENSILE TAIL** **FEAT 5** |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/6` | 0.449161 | **VOID BLOOD** **FEAT 5** |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/16/SectionHeader/12` | 0.447403 | **ELECTRICAL SHIELDING** **FEAT 5** |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/16/SectionHeader/7` | 0.423685 | **DRIFT HOP **[one-action] **FEAT 5** |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/7/SectionHeader/36` | 0.417848 | **UNDERFOOT** **FEAT 9** |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/44` | 0.414242 | **Prerequisites** Underfoot |

### Query 149
- Text: What are the requirements for **VOID BLOOD** **FEAT 5**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 074-091::/page/13/Text/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 074-091::/page/13/Text/6', 'PZO22001 Starfinder Player Core 074-091::/page/3/SectionHeader/4', 'PZO22001 Starfinder Player Core 074-091::/page/12/SectionHeader/36']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/6` | 0.884308 | **VOID BLOOD** **FEAT 5** |
| 2 | `PZO22001 Starfinder Player Core 074-091::/page/3/SectionHeader/4` | 0.620660 | **BLOOD SENSE** **FEAT 5** |
| 3 | `PZO22001 Starfinder Player Core 074-091::/page/12/SectionHeader/36` | 0.513826 | **SOUL SUSTENANCE** **FEAT 5** |
| 4 | `PZO22001 Starfinder Player Core 074-091::/page/16/SectionHeader/7` | 0.462194 | **DRIFT HOP **[one-action] **FEAT 5** |
| 5 | `PZO22001 Starfinder Player Core 074-091::/page/16/SectionHeader/12` | 0.452459 | **ELECTRICAL SHIELDING** **FEAT 5** |
| 6 | `PZO22001 Starfinder Player Core 074-091::/page/12/SectionHeader/1` | 0.451802 | **HEADSTRONG** **FEAT 1** |
| 7 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/16` | 0.442078 | **PREHENSILE TAIL** **FEAT 5** |
| 8 | `PZO22001 Starfinder Player Core 074-091::/page/12/SectionHeader/32` | 0.438709 | **DEATHLY CONSTITUTION** **FEAT 5** |
| 9 | `PZO22001 Starfinder Player Core 074-091::/page/13/Text/2` | 0.430215 | **UNLIVING MEMORIES** **FEAT 5** |
| 10 | `PZO22001 Starfinder Player Core 074-091::/page/7/Text/13` | 0.423973 | **CORNERED FURY** **FEAT 5** |
