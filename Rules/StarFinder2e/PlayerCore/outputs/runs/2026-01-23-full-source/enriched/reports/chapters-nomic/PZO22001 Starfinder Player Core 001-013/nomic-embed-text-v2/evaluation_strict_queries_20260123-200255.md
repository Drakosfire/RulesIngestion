# RulesLawyer Evaluation Report: nomic-embed-text-v2

## Summary
- Run ID: `None`
- Ruleset ID: `None`
- Document ID: `None`
- Chunk source: `enriched`
- Chunk count: `454`
- Query count: `108`
- Evaluated queries: `108`
- Coverage: `1.0000`
- MRR: `0.9648`
- hit@1: `0.9444`
- hit@3: `0.9815`
- hit@5: `0.9907`
- hit@10: `1.0000`
- Embeddings reused: `False`
- Graph boost: `0.05` (depth=2, top_k=50, source=top, seed_top_n=3, same_kind_only=False, decay=0.4)

## Timings (ms)
- Embedding (chunks): `10492`
- Embedding (queries): `5256`
- Evaluation (strict): `17`
- Evaluation (expanded): `0`
- Total: `20165`

### Timing Estimates (ms)
- Evaluation (strict): `21`
- Evaluation (expanded): `None`
- Total: `15769`

## Query Details
### Query 0
- Text: Summarize **AUTHORS **
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/1/SectionHeader/0']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/1/SectionHeader/0', 'PZO22001 Starfinder Player Core 001-013::/page/1/SectionHeader/20', 'PZO22001 Starfinder Player Core 001-013::/page/1/SectionHeader/6']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/1/SectionHeader/0` | 0.831161 | **AUTHORS ** |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/1/SectionHeader/20` | 0.596378 | **PUBLISHER ** |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/1/SectionHeader/6` | 0.584510 | **EDITORS ** |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/21` | 0.526386 | **INTRODUCTION** |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/12/Text/29` | 0.526386 | **INTRODUCTION** |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/10/Text/33` | 0.526386 | **INTRODUCTION** |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/8/Text/14` | 0.526386 | **INTRODUCTION** |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/13` | 0.526386 | **INTRODUCTION** |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/9/SectionHeader/1` | 0.515702 | **KEY TERMS** |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/9/SectionHeader/13` | 0.501235 | **Background** |

### Query 1
- Text: Summarize Jessica Catalan, Thurston Hillman, Jenny Jarzabski, Mike Kimmel, and Dustin Knight
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/1/Text/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/1/Text/1', 'PZO22001 Starfinder Player Core 001-013::/page/1/Text/19', 'PZO22001 Starfinder Player Core 001-013::/page/1/Text/11']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/1/Text/1` | 1.030560 | Jessica Catalan, Thurston Hillman, Jenny Jarzabski, Mike Kimmel, and Dustin Knight |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/1/Text/19` | 0.578997 | Thurston Hillman |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/1/Text/11` | 0.479317 | Zach Causey, Franklin Chan, Nicholas DeLuca, Çağdaş Demiralp, Emanuele Desiati, Gunship Revolution (Arvin Albo, Rafael Cal-Ortiz, Jenno Diaz, Mico Dimagiba, Stefany Madduma, Luisa Odulio, Hinchel Or, |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/11/Text/10` | 0.420004 | Everyone rolls Perception for their initiative. Mike gets a total of  20. Jessica rolls 12, Dustin rolls 16, and Jenny rolls 10. Thurston  rolls for the driftdead, getting a 19 and 14. He secretly rol |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/12/TableCell/473` | 0.402859 | Thurston: |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/12/TableCell/463` | 0.402859 | Thurston: |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/12/TableCell/449` | 0.402859 | Thurston: |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/11/TableCell/424` | 0.402859 | Thurston: |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/11/TableCell/418` | 0.402859 | Thurston: |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/12/TableCell/469` | 0.402859 | Thurston: |

### Query 2
- Text: Summarize ADDITIONAL DEVELOPMENT
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/1/SectionHeader/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/1/SectionHeader/2', 'PZO22001 Starfinder Player Core 001-013::/page/9/SectionHeader/11', 'PZO22001 Starfinder Player Core 001-013::/page/6/Text/2']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/1/SectionHeader/2` | 0.983596 | ADDITIONAL DEVELOPMENT |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/9/SectionHeader/11` | 0.349707 | **Attribute Modifier** |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/2` | 0.322611 | In addition to level, characters are defined by **attributes**,  which measure raw potential and are used to calculate  most of their other statistics. There are six attributes in the  game. **Strengt |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/2/TableCell/15` | 0.271950 | INTRODUCTION TECH GEAR ARMOR SHIELDS WEAPONS ARMOR UPGRADES WEAPON UPGRADES PRECIOUS AMMUNITION & WEAPONS GRENADES MAGIC ITEMS AUGMENTATIONS |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/11/TableCell/423` | 0.267793 | 12. "I'm gonna need more coffee for this." |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/9/Text/12` | 0.259762 | Each creature has six attribute modifiers: Strength,  Dexterity, Constitution, Intelligence, Wisdom, and  Charisma. Each of these numbers represents a creature's  raw potential and general training. A |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/12/Text/3` | 0.254366 | Mike rolls a 12 and adds +8, due to Zemir's training with simple  weapons, for a total of 20. Thurston consults his notes to  confirm the driftdead has an AC of 16. |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/1` | 0.244316 | the character's adventuring career, to 20th, the very height  of power. As the characters overcome challenges, defeat  foes, and complete adventures, they accumulate **Experience ** **Points (XP)**. E |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/2/TableOfContents/2` | 0.239903 | 6EQUIPMENT232INTRODUCTION TECH GEAR ARMOR SHIELDS WEAPONS ARMOR UPGRADES WEAPON UPGRADES PRECIOUS AMMUNITION & WEAPONS GRENADES MAGIC ITEMS AUGMENTATIONS293 298 244 250 253 268 272 278 2807SPELLS294SP |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/7/Text/7` | 0.238311 | Checks like this are the heart of the game and are rolled all  the time, in every mode of play, to determine the outcome of  tasks. While the roll of the die is essential, the statistic you  add to th |

### Query 3
- Text: Summarize Logan Bonner, Jason Bulmahn, James Case, and Michael Sayre
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/1/Text/3']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/1/Text/3', 'PZO22001 Starfinder Player Core 001-013::/page/1/Text/23', 'PZO22001 Starfinder Player Core 001-013::/page/1/Text/11']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/1/Text/3` | 1.027581 | Logan Bonner, Jason Bulmahn, James Case, and Michael Sayre |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/1/Text/23` | 0.775955 | Logan Bonner, Jason Bulmahn, Lyz Liddell, Stephen Radney-MacFarland, and Mark Seifter |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/1/Text/11` | 0.413468 | Zach Causey, Franklin Chan, Nicholas DeLuca, Çağdaş Demiralp, Emanuele Desiati, Gunship Revolution (Arvin Albo, Rafael Cal-Ortiz, Jenno Diaz, Mico Dimagiba, Stefany Madduma, Luisa Odulio, Hinchel Or, |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/1/Text/7` | 0.293647 | \label{eq:Felix Dritz} \textit{Felix Dritz}, \textit{Patrick Hurley}, \textit{Avi Kool}, \textit{Priscilla N}. Lagares, Lynne M. Meyer, Zac Moran, Ianara Natividad, Solomon St. John, and Simone D. Sal |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/12/TableCell/465` | 0.252192 | Zemir (Mike): |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/11/TableCell/412` | 0.252192 | Zemir (Mike): |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/12/TableCell/445` | 0.252192 | Zemir (Mike): |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/11/TableCell/442` | 0.252192 | Zemir (Mike): |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/11/TableCell/462` | 0.252192 | Zemir (Mike): |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/12/TableCell/451` | 0.252192 | Zemir (Mike): |

### Query 4
- Text: Summarize **EDITING LEAD **
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/1/SectionHeader/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/1/SectionHeader/4', 'PZO22001 Starfinder Player Core 001-013::/page/1/SectionHeader/6', 'PZO22001 Starfinder Player Core 001-013::/page/9/SectionHeader/13']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/1/SectionHeader/4` | 0.978910 | **EDITING LEAD ** |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/1/SectionHeader/6` | 0.512608 | **EDITORS ** |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/9/SectionHeader/13` | 0.377186 | **Background** |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/1/SectionHeader/0` | 0.323826 | **AUTHORS ** |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/1/SectionHeader/20` | 0.322182 | **PUBLISHER ** |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/21` | 0.312327 | **INTRODUCTION** |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/13` | 0.312327 | **INTRODUCTION** |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/8/Text/14` | 0.312327 | **INTRODUCTION** |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/10/Text/33` | 0.312327 | **INTRODUCTION** |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/12/Text/29` | 0.312327 | **INTRODUCTION** |

### Query 5
- Text: Summarize Avi Kool
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/1/Text/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/1/Text/5', 'PZO22001 Starfinder Player Core 001-013::/page/12/Table/6', 'PZO22001 Starfinder Player Core 001-013::/page/2/SectionHeader/0']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/1/Text/5` | 0.931177 | Avi Kool |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/12/Table/6` | 0.282651 | Zemir (Mike):For my third action, I Take Cover behind arock in my quantum field.Thurston:The rotting vesk recoils as laser fire hits it,then it shoots a bolt of void energy at you. |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/2/SectionHeader/0` | 0.276059 | PLAYER CORE |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/1/Text/7` | 0.229597 | \label{eq:Felix Dritz} \textit{Felix Dritz}, \textit{Patrick Hurley}, \textit{Avi Kool}, \textit{Priscilla N}. Lagares, Lynne M. Meyer, Zac Moran, Ianara Natividad, Solomon St. John, and Simone D. Sal |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/12/Text/3` | 0.222018 | Mike rolls a 12 and adds +8, due to Zemir's training with simple  weapons, for a total of 20. Thurston consults his notes to  confirm the driftdead has an AC of 16. |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableOfContents/31` | 0.221721 | 1INTRODUCTION 4CHARACTER CREATION17LEVELING UP29EXPLORING THE GALAXY\ **2**ANCESTRIES & BACKGROUNDS 40ANDROID42BARATHU46 HUMAN50KASATHA54LASHUNTA58PAHTRA62SHIRREN66SKITTERMANDER70VESKVERSATILE HERITAG |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/9/SectionHeader/7` | 0.219262 | **Armor Class (AC)** |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/170` | 0.219196 | ENVOY102 |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/12/SectionHeader/0` | 0.215707 | 1 PLAYER CORE |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/11/TableCell/569` | 0.214855 | The autodoor stutters open. A vesk and a |

### Query 6
- Text: Summarize **EDITORS **
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/1/SectionHeader/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/1/SectionHeader/6', 'PZO22001 Starfinder Player Core 001-013::/page/1/SectionHeader/20', 'PZO22001 Starfinder Player Core 001-013::/page/1/SectionHeader/0']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/1/SectionHeader/6` | 0.922362 | **EDITORS ** |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/1/SectionHeader/20` | 0.582232 | **PUBLISHER ** |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/1/SectionHeader/0` | 0.544519 | **AUTHORS ** |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/1/SectionHeader/4` | 0.459110 | **EDITING LEAD ** |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/1/SectionHeader/18` | 0.393628 | **ASSOCIATE PUBLISHER ** |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/9/SectionHeader/1` | 0.381110 | **KEY TERMS** |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/9/SectionHeader/13` | 0.375020 | **Background** |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/21` | 0.365711 | **INTRODUCTION** |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/8/Text/14` | 0.365711 | **INTRODUCTION** |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/13` | 0.365711 | **INTRODUCTION** |

### Query 7
- Text: What is the rule about \label{eq:Felix Dritz} \textit{Felix Dritz}, \textit{Patrick Hurley}, \textit{Avi Kool}, \textit{Priscilla N}. Lagares, Lynne M. Meyer, Zac Moran, Ianara Natividad, Solomon St. John, and Simone D. Sallé?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/1/Text/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/1/Text/7', 'PZO22001 Starfinder Player Core 001-013::/page/1/Text/11', 'PZO22001 Starfinder Player Core 001-013::/page/12/SectionHeader/8']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/1/Text/7` | 0.917914 | \label{eq:Felix Dritz} \textit{Felix Dritz}, \textit{Patrick Hurley}, \textit{Avi Kool}, \textit{Priscilla N}. Lagares, Lynne M. Meyer, Zac Moran, Ianara Natividad, Solomon St. John, and Simone D. Sal |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/1/Text/11` | 0.432854 | Zach Causey, Franklin Chan, Nicholas DeLuca, Çağdaş Demiralp, Emanuele Desiati, Gunship Revolution (Arvin Albo, Rafael Cal-Ortiz, Jenno Diaz, Mico Dimagiba, Stefany Madduma, Luisa Odulio, Hinchel Or, |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/12/SectionHeader/8` | 0.408511 | **Chk Chk (Dustin):** I cast *vibe check*. I'm broadcasting an  angry poem about my childhood into the  human's mind: "Despite all my bile, I am  still just a bug in a vial!" That's two actions.  Then |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/11/Table/3` | 0.350044 | Thurston:Your ship speeds through the swirlingcolors and half-formed shapes of the Drift.You're getting close to the coordinates, butchunks of rock, ice, and metal scrap floatahead of you, blocking yo |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/11/Text/10` | 0.346123 | Everyone rolls Perception for their initiative. Mike gets a total of  20. Jessica rolls 12, Dustin rolls 16, and Jenny rolls 10. Thurston  rolls for the driftdead, getting a 19 and 14. He secretly rol |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/2/TableCell/27` | 0.340249 | RULES OVERVIEW |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/10/Text/29` | 0.337989 | All the traits used in this book appear in the Glossary  and Index beginning on page 442. |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/12/Text/23` | 0.336610 | **Obozaya (Jenny):** "Hahahahaha!" That's Menacing Laughter  for my third action. Oh, and don't forget,  the enemy is suppressed. |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/3` | 0.336445 | Your player character is also defined by some key choices  you make. The first choice is a PC's **ancestry**, representing the  character's parents and heritage, such as barathu, human, or  vesk. Next |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/11/Table/5` | 0.336228 | Zemir (Mike):"Thanks, Chk Chk." I chug some coffee andtry again. 13! I've got a +7 to Piloting sothat's a 20!Thurston:The ship zooms safely through thedebris until the beacon you were sent toinvestiga |

### Query 8
- Text: Summarize **COVER ARTIST **
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/1/SectionHeader/8']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/1/SectionHeader/8', 'PZO22001 Starfinder Player Core 001-013::/page/1/SectionHeader/10', 'PZO22001 Starfinder Player Core 001-013::/page/12/TableCell/466']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/1/SectionHeader/8` | 0.996466 | **COVER ARTIST ** |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/1/SectionHeader/10` | 0.570684 | **INTERIOR ARTISTS ** |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/12/TableCell/466` | 0.509536 | For my third action, I Take Cover behind a |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/8/Text/15` | 0.394364 | **Character ** **Creation** |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/14` | 0.394364 | **Character ** **Creation** |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/22` | 0.394364 | **Character ** **Creation** |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/12/Text/30` | 0.394364 | **Character ** **Creation** |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/10/Text/34` | 0.394364 | **Character ** **Creation** |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/1/SectionHeader/16` | 0.358062 | **CREATIVE MANAGER ** |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/12/Table/6` | 0.321955 | Zemir (Mike):For my third action, I Take Cover behind arock in my quantum field.Thurston:The rotting vesk recoils as laser fire hits it,then it shoots a bolt of void energy at you. |

### Query 9
- Text: Summarize Kent Hamilton
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/1/Text/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/1/Text/9', 'PZO22001 Starfinder Player Core 001-013::/page/1/Text/19', 'PZO22001 Starfinder Player Core 001-013::/page/1/Text/1']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/1/Text/9` | 0.923772 | Kent Hamilton |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/1/Text/19` | 0.333403 | Thurston Hillman |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/1/Text/1` | 0.318166 | Jessica Catalan, Thurston Hillman, Jenny Jarzabski, Mike Kimmel, and Dustin Knight |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/1/Text/11` | 0.270319 | Zach Causey, Franklin Chan, Nicholas DeLuca, Çağdaş Demiralp, Emanuele Desiati, Gunship Revolution (Arvin Albo, Rafael Cal-Ortiz, Jenno Diaz, Mico Dimagiba, Stefany Madduma, Luisa Odulio, Hinchel Or, |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/11/TableCell/412` | 0.247850 | Zemir (Mike): |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/11/TableCell/442` | 0.247850 | Zemir (Mike): |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/12/TableCell/465` | 0.247850 | Zemir (Mike): |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/12/TableCell/445` | 0.247850 | Zemir (Mike): |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/12/TableCell/451` | 0.247850 | Zemir (Mike): |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/11/TableCell/526` | 0.247850 | Zemir (Mike): |

### Query 10
- Text: Summarize **INTERIOR ARTISTS **
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/1/SectionHeader/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/1/SectionHeader/10', 'PZO22001 Starfinder Player Core 001-013::/page/1/SectionHeader/8', 'PZO22001 Starfinder Player Core 001-013::/page/4/Text/22']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/1/SectionHeader/10` | 1.007862 | **INTERIOR ARTISTS ** |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/1/SectionHeader/8` | 0.561591 | **COVER ARTIST ** |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/22` | 0.403744 | **Character ** **Creation** |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/14` | 0.361744 | **Character ** **Creation** |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/8/Text/15` | 0.361744 | **Character ** **Creation** |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/10/Text/34` | 0.361744 | **Character ** **Creation** |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/12/Text/30` | 0.361744 | **Character ** **Creation** |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/1/Text/11` | 0.324318 | Zach Causey, Franklin Chan, Nicholas DeLuca, Çağdaş Demiralp, Emanuele Desiati, Gunship Revolution (Arvin Albo, Rafael Cal-Ortiz, Jenno Diaz, Mico Dimagiba, Stefany Madduma, Luisa Odulio, Hinchel Or, |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/1/SectionHeader/0` | 0.321721 | **AUTHORS ** |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/10/SectionHeader/20` | 0.311296 | **Skill** |

### Query 11
- Text: What is the rule about Zach Causey, Franklin Chan, Nicholas DeLuca, Çağdaş Demiralp, Emanuele Desiati, Gunship Revolution (Arvin Albo, Rafael Cal-Ortiz, Jenno Diaz, Mico Dimagiba, Stefany Madduma, Luisa Odulio, Hinchel Or, Marcus Reyno, Jen Santos, Timothy Terrenal, and Brian Valeza), Kent Hamilton, Rowan Holloway, Kyle Hunter, Bastien Jez, Sammy Khalid, Roman Kierszenbaum, Emanuel Pantaleon, Pixoloid Studios (Mark Molnar, David Metzger, Gaspar Gombos, Zsolt "Mike" Szabados, Janos Gardos, Laszlo Hackl, Orsolya Villanyi), Ainur Salimova, Daniele Sorrentino, and Jessé Suursoo?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/1/Text/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/1/Text/11', 'PZO22001 Starfinder Player Core 001-013::/page/1/Text/7', 'PZO22001 Starfinder Player Core 001-013::/page/1/Text/1']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/1/Text/11` | 0.876488 | Zach Causey, Franklin Chan, Nicholas DeLuca, Çağdaş Demiralp, Emanuele Desiati, Gunship Revolution (Arvin Albo, Rafael Cal-Ortiz, Jenno Diaz, Mico Dimagiba, Stefany Madduma, Luisa Odulio, Hinchel Or, |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/1/Text/7` | 0.524974 | \label{eq:Felix Dritz} \textit{Felix Dritz}, \textit{Patrick Hurley}, \textit{Avi Kool}, \textit{Priscilla N}. Lagares, Lynne M. Meyer, Zac Moran, Ianara Natividad, Solomon St. John, and Simone D. Sal |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/1/Text/1` | 0.472302 | Jessica Catalan, Thurston Hillman, Jenny Jarzabski, Mike Kimmel, and Dustin Knight |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/11/Text/10` | 0.397746 | Everyone rolls Perception for their initiative. Mike gets a total of  20. Jessica rolls 12, Dustin rolls 16, and Jenny rolls 10. Thurston  rolls for the driftdead, getting a 19 and 14. He secretly rol |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/1/Text/23` | 0.391886 | Logan Bonner, Jason Bulmahn, Lyz Liddell, Stephen Radney-MacFarland, and Mark Seifter |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/1/Text/3` | 0.375371 | Logan Bonner, Jason Bulmahn, James Case, and Michael Sayre |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/12/SectionHeader/8` | 0.371237 | **Chk Chk (Dustin):** I cast *vibe check*. I'm broadcasting an  angry poem about my childhood into the  human's mind: "Despite all my bile, I am  still just a bug in a vial!" That's two actions.  Then |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/10` | 0.362413 | take turns describing what their characters attempt to  do, while the GM determines the outcome, with everyone  working together to create the story. The GM also describes  the environment, other char |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/2/TableCell/27` | 0.361723 | RULES OVERVIEW |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/6` | 0.359221 | Characters and their choices create the story of Starfinder,  but how they interact with each other and the galaxy around  them is governed by rules. So, while you might decide that  your character st |

### Query 12
- Text: Summarize ART DIRECTION
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/1/SectionHeader/12']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/1/SectionHeader/12', 'PZO22001 Starfinder Player Core 001-013::/page/11/TableCell/405', 'PZO22001 Starfinder Player Core 001-013::/page/11/TableCell/429']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/1/SectionHeader/12` | 0.960291 | ART DIRECTION |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/11/TableCell/405` | 0.334461 | colors and half-formed shapes of the Drift. |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/11/TableCell/429` | 0.326201 | path he was following. |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/1/SectionHeader/10` | 0.281890 | **INTERIOR ARTISTS ** |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/11/Table/3` | 0.270923 | Thurston:Your ship speeds through the swirlingcolors and half-formed shapes of the Drift.You're getting close to the coordinates, butchunks of rock, ice, and metal scrap floatahead of you, blocking yo |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/11/TableCell/559` | 0.245296 | draw my laser pistol. |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/12/Table/2` | 0.239428 | Thurston:Zemir, you're up first.Zemir (Mike):Excellent. For my first action, I spend 1Focus Point to cast warp terrain.Thurston:Which effect do you choose?Zemir (Mike):I choose difficult terrain. My q |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/8/Text/5` | 0.239354 | While exploration is handled in a free-form manner,  encounters are more structured. The players and GM  roll **initiative** to determine who acts in what order. The  encounter occurs over a number of |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/1/Text/7` | 0.239218 | \label{eq:Felix Dritz} \textit{Felix Dritz}, \textit{Patrick Hurley}, \textit{Avi Kool}, \textit{Priscilla N}. Lagares, Lynne M. Meyer, Zac Moran, Ianara Natividad, Solomon St. John, and Simone D. Sal |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/180` | 0.239081 | ARCHETYPES174 |

### Query 13
- Text: Summarize Sonja Morris
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/1/Text/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/1/Text/13', 'PZO22001 Starfinder Player Core 001-013::/page/1/Text/15', 'PZO22001 Starfinder Player Core 001-013::/page/1/Text/21']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/1/Text/13` | 0.933725 | Sonja Morris |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/1/Text/15` | 0.933725 | Sonja Morris |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/1/Text/21` | 0.326752 | Erik Mona |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/12/Text/23` | 0.242241 | **Obozaya (Jenny):** "Hahahahaha!" That's Menacing Laughter  for my third action. Oh, and don't forget,  the enemy is suppressed. |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/11/TableCell/485` | 0.241377 | Obozaya (Jenny): "Only if you don't break it." |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/12/Text/41` | 0.232719 | **GLOSSARY & ** **INDEX** |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/10/Text/46` | 0.232719 | **GLOSSARY & ** **INDEX** |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/8/Text/27` | 0.232719 | **GLOSSARY & ** **INDEX** |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/27` | 0.232719 | **GLOSSARY & ** **INDEX** |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/34` | 0.232719 | **GLOSSARY & ** **INDEX** |

### Query 14
- Text: Summarize **GRAPHIC DESIGN **
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/1/SectionHeader/14']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/1/SectionHeader/14', 'PZO22001 Starfinder Player Core 001-013::/page/1/SectionHeader/22', 'PZO22001 Starfinder Player Core 001-013::/page/8/Text/15']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/1/SectionHeader/14` | 0.970018 | **GRAPHIC DESIGN ** |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/1/SectionHeader/22` | 0.599954 | **BASED ON THE DESIGN WORK OF ** |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/8/Text/15` | 0.455407 | **Character ** **Creation** |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/10/Text/34` | 0.413407 | **Character ** **Creation** |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/12/Text/30` | 0.413407 | **Character ** **Creation** |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/22` | 0.413407 | **Character ** **Creation** |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/14` | 0.413407 | **Character ** **Creation** |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/9/SectionHeader/13` | 0.407190 | **Background** |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/8/Text/14` | 0.368767 | **INTRODUCTION** |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/10/Text/33` | 0.356767 | **INTRODUCTION** |

### Query 15
- Text: Summarize Sonja Morris
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/1/Text/15']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/1/Text/13', 'PZO22001 Starfinder Player Core 001-013::/page/1/Text/15', 'PZO22001 Starfinder Player Core 001-013::/page/1/Text/21']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/1/Text/13` | 0.933725 | Sonja Morris |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/1/Text/15` | 0.933725 | Sonja Morris |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/1/Text/21` | 0.326752 | Erik Mona |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/12/Text/23` | 0.242241 | **Obozaya (Jenny):** "Hahahahaha!" That's Menacing Laughter  for my third action. Oh, and don't forget,  the enemy is suppressed. |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/11/TableCell/485` | 0.241377 | Obozaya (Jenny): "Only if you don't break it." |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/12/Text/41` | 0.232719 | **GLOSSARY & ** **INDEX** |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/10/Text/46` | 0.232719 | **GLOSSARY & ** **INDEX** |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/8/Text/27` | 0.232719 | **GLOSSARY & ** **INDEX** |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/27` | 0.232719 | **GLOSSARY & ** **INDEX** |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/34` | 0.232719 | **GLOSSARY & ** **INDEX** |

### Query 16
- Text: Summarize **CREATIVE MANAGER **
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/1/SectionHeader/16']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/1/SectionHeader/16', 'PZO22001 Starfinder Player Core 001-013::/page/6/Text/14', 'PZO22001 Starfinder Player Core 001-013::/page/8/Text/15']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/1/SectionHeader/16` | 1.005222 | **CREATIVE MANAGER ** |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/14` | 0.464071 | **Character ** **Creation** |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/8/Text/15` | 0.464071 | **Character ** **Creation** |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/22` | 0.422071 | **Character ** **Creation** |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/12/Text/30` | 0.422071 | **Character ** **Creation** |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/10/Text/34` | 0.422071 | **Character ** **Creation** |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/1/SectionHeader/8` | 0.370923 | **COVER ARTIST ** |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/9/SectionHeader/27` | 0.369352 | **Game Master (GM)** |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/10/SectionHeader/20` | 0.353964 | **Skill** |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/9/SectionHeader/1` | 0.346704 | **KEY TERMS** |

### Query 17
- Text: Summarize Jenny Jarzabski
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/1/Text/17']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/1/Text/17', 'PZO22001 Starfinder Player Core 001-013::/page/1/Text/1', 'PZO22001 Starfinder Player Core 001-013::/page/11/TableCell/553']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/1/Text/17` | 0.957106 | Jenny Jarzabski |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/1/Text/1` | 0.466366 | Jessica Catalan, Thurston Hillman, Jenny Jarzabski, Mike Kimmel, and Dustin Knight |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/11/TableCell/553` | 0.406476 | Obozaya (Jenny): I pull out my machine gun and move in |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/11/TableCell/505` | 0.345010 | Obozaya (Jenny): "Careful, Dae. I don't want to have to clean |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/12/Text/23` | 0.342702 | **Obozaya (Jenny):** "Hahahahaha!" That's Menacing Laughter  for my third action. Oh, and don't forget,  the enemy is suppressed. |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/11/TableCell/485` | 0.339842 | Obozaya (Jenny): "Only if you don't break it." |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/12/Text/21` | 0.322111 | **Obozaya (Jenny):** "Thanks for the setup, Dae!" I Auto-Fire at  both enemies. The human is closest to me,  so she's my primary target. |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/11/Text/12` | 0.269427 | **Thurston:** Dae, are you installing Obozaya's jetpack  into your armor? **Obozaya (Jenny):** Paws off! I'll do it with Quick Install. |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/1/Text/13` | 0.245972 | Sonja Morris |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/1/Text/15` | 0.245972 | Sonja Morris |

### Query 18
- Text: Summarize **ASSOCIATE PUBLISHER **
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/1/SectionHeader/18']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/1/SectionHeader/18', 'PZO22001 Starfinder Player Core 001-013::/page/1/SectionHeader/20', 'PZO22001 Starfinder Player Core 001-013::/page/1/SectionHeader/6']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/1/SectionHeader/18` | 1.005391 | **ASSOCIATE PUBLISHER ** |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/1/SectionHeader/20` | 0.724276 | **PUBLISHER ** |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/1/SectionHeader/6` | 0.426391 | **EDITORS ** |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/1/SectionHeader/0` | 0.351968 | **AUTHORS ** |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/8/Text/19` | 0.296879 | **ANCESTRIES & ** **BACKGROUNDS** |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/26` | 0.296879 | **ANCESTRIES & ** **BACKGROUNDS** |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/10/Text/38` | 0.296879 | **ANCESTRIES & ** **BACKGROUNDS** |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/12/Text/33` | 0.296879 | **ANCESTRIES & ** **BACKGROUNDS** |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/18` | 0.296879 | **ANCESTRIES & ** **BACKGROUNDS** |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/9/SectionHeader/5` | 0.293152 | **Ancestry** |

### Query 19
- Text: Summarize Thurston Hillman
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/1/Text/19']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/1/Text/19', 'PZO22001 Starfinder Player Core 001-013::/page/11/TableCell/464', 'PZO22001 Starfinder Player Core 001-013::/page/11/TableCell/402']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/1/Text/19` | 0.989291 | Thurston Hillman |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/11/TableCell/464` | 0.690332 | Thurston: |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/11/TableCell/402` | 0.690332 | Thurston: |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/11/TableCell/418` | 0.648332 | Thurston: |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/11/TableCell/448` | 0.648332 | Thurston: |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/12/TableCell/469` | 0.648332 | Thurston: |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/12/TableCell/449` | 0.648332 | Thurston: |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/11/TableCell/532` | 0.648332 | Thurston: |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/12/TableCell/443` | 0.648332 | Thurston: |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/12/TableCell/463` | 0.648332 | Thurston: |

### Query 20
- Text: Summarize **PUBLISHER **
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/1/SectionHeader/20']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/1/SectionHeader/20', 'PZO22001 Starfinder Player Core 001-013::/page/1/SectionHeader/18', 'PZO22001 Starfinder Player Core 001-013::/page/1/SectionHeader/6']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/1/SectionHeader/20` | 0.920774 | **PUBLISHER ** |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/1/SectionHeader/18` | 0.805592 | **ASSOCIATE PUBLISHER ** |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/1/SectionHeader/6` | 0.555607 | **EDITORS ** |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/1/SectionHeader/0` | 0.480063 | **AUTHORS ** |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/8/Text/14` | 0.381806 | **INTRODUCTION** |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/10/Text/33` | 0.381806 | **INTRODUCTION** |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/13` | 0.381806 | **INTRODUCTION** |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/12/Text/29` | 0.381806 | **INTRODUCTION** |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/21` | 0.381806 | **INTRODUCTION** |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/9/SectionHeader/13` | 0.377213 | **Background** |

### Query 21
- Text: Summarize Erik Mona
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/1/Text/21']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/1/Text/21', 'PZO22001 Starfinder Player Core 001-013::/page/1/Text/13', 'PZO22001 Starfinder Player Core 001-013::/page/1/Text/15']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/1/Text/21` | 0.944922 | Erik Mona |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/1/Text/13` | 0.331915 | Sonja Morris |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/1/Text/15` | 0.331915 | Sonja Morris |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/1/Text/7` | 0.243511 | \label{eq:Felix Dritz} \textit{Felix Dritz}, \textit{Patrick Hurley}, \textit{Avi Kool}, \textit{Priscilla N}. Lagares, Lynne M. Meyer, Zac Moran, Ianara Natividad, Solomon St. John, and Simone D. Sal |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/160` | 0.223986 | BORAI 84 |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/12/Table/6` | 0.215814 | Zemir (Mike):For my third action, I Take Cover behind arock in my quantum field.Thurston:The rotting vesk recoils as laser fire hits it,then it shoots a bolt of void energy at you. |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/1/SectionHeader/6` | 0.209746 | **EDITORS ** |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/1/SectionHeader/20` | 0.204683 | **PUBLISHER ** |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/11/Table/7` | 0.203380 | Dae (Jessica):I head for the airlock, then strike a pose asI step into space. "Hey Chk Chk, make sureyou're recording this!"Thurston:Now you're untethered. Are you freefloating?Dae (Jessica):Nope! I a |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/11/Table/5` | 0.197965 | Zemir (Mike):"Thanks, Chk Chk." I chug some coffee andtry again. 13! I've got a +7 to Piloting sothat's a 20!Thurston:The ship zooms safely through thedebris until the beacon you were sent toinvestiga |

### Query 22
- Text: Summarize **BASED ON THE DESIGN WORK OF **
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/1/SectionHeader/22']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/1/SectionHeader/22', 'PZO22001 Starfinder Player Core 001-013::/page/1/SectionHeader/14', 'PZO22001 Starfinder Player Core 001-013::/page/6/Text/14']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/1/SectionHeader/22` | 0.971454 | **BASED ON THE DESIGN WORK OF ** |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/1/SectionHeader/14` | 0.590955 | **GRAPHIC DESIGN ** |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/14` | 0.457464 | **Character ** **Creation** |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/8/Text/15` | 0.415464 | **Character ** **Creation** |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/22` | 0.415464 | **Character ** **Creation** |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/10/Text/34` | 0.415464 | **Character ** **Creation** |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/12/Text/30` | 0.415464 | **Character ** **Creation** |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/9/SectionHeader/13` | 0.370763 | **Background** |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/1/SectionHeader/0` | 0.357240 | **AUTHORS ** |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/13` | 0.356897 | **INTRODUCTION** |

### Query 23
- Text: What is the rule about Logan Bonner, Jason Bulmahn, Lyz Liddell, Stephen Radney-MacFarland, and Mark Seifter?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/1/Text/23']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/1/Text/23', 'PZO22001 Starfinder Player Core 001-013::/page/1/Text/3', 'PZO22001 Starfinder Player Core 001-013::/page/1/Text/7']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/1/Text/23` | 0.935321 | Logan Bonner, Jason Bulmahn, Lyz Liddell, Stephen Radney-MacFarland, and Mark Seifter |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/1/Text/3` | 0.700340 | Logan Bonner, Jason Bulmahn, James Case, and Michael Sayre |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/1/Text/7` | 0.415035 | \label{eq:Felix Dritz} \textit{Felix Dritz}, \textit{Patrick Hurley}, \textit{Avi Kool}, \textit{Priscilla N}. Lagares, Lynne M. Meyer, Zac Moran, Ianara Natividad, Solomon St. John, and Simone D. Sal |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/1/Text/11` | 0.370320 | Zach Causey, Franklin Chan, Nicholas DeLuca, Çağdaş Demiralp, Emanuele Desiati, Gunship Revolution (Arvin Albo, Rafael Cal-Ortiz, Jenno Diaz, Mico Dimagiba, Stefany Madduma, Luisa Odulio, Hinchel Or, |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/2/TableCell/27` | 0.273888 | RULES OVERVIEW |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/1/Text/1` | 0.270733 | Jessica Catalan, Thurston Hillman, Jenny Jarzabski, Mike Kimmel, and Dustin Knight |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/6` | 0.269670 | Characters and their choices create the story of Starfinder,  but how they interact with each other and the galaxy around  them is governed by rules. So, while you might decide that  your character st |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/11/Text/10` | 0.268723 | Everyone rolls Perception for their initiative. Mike gets a total of  20. Jessica rolls 12, Dustin rolls 16, and Jenny rolls 10. Thurston  rolls for the driftdead, getting a 19 and 14. He secretly rol |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/17` | 0.267362 | Everyone involved in a Starfinder game is a player, including  the Game Master, but for the sake of simplicity, "player"  usually refers to participants other than the GM. Before  the game begins, pla |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/12/TableCell/445` | 0.257879 | Zemir (Mike): |

### Query 24
- Text: Summarize **SPECIAL THANKS **
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/1/SectionHeader/24']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/1/SectionHeader/24', 'PZO22001 Starfinder Player Core 001-013::/page/9/SectionHeader/1', 'PZO22001 Starfinder Player Core 001-013::/page/9/SectionHeader/13']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/1/SectionHeader/24` | 0.914056 | **SPECIAL THANKS ** |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/9/SectionHeader/1` | 0.424607 | **KEY TERMS** |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/9/SectionHeader/13` | 0.405930 | **Background** |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/9/SectionHeader/17` | 0.360480 | **Check** |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/9/SectionHeader/15` | 0.354567 | **Bonuses and Penalties** |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/9/SectionHeader/25` | 0.347023 | **Feat** |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/11/TableCell/443` | 0.343052 | "Thanks, Chk Chk." I chug some coffee and |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/8/Text/22` | 0.340433 | **FEATS** |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/10/Text/41` | 0.340433 | **FEATS** |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/29` | 0.340433 | **FEATS** |

### Query 25
- Text: Summarize To everyone who participated in the Starfinder open playtest
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/1/Text/25']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/1/Text/25', 'PZO22001 Starfinder Player Core 001-013::/page/5/Text/9', 'PZO22001 Starfinder Player Core 001-013::/page/4/Text/2']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/1/Text/25` | 1.024703 | To everyone who participated in the Starfinder open playtest |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/5/Text/9` | 0.656931 | Starfinder is a game for everyone, regardless of their age,  gender, race or ethnicity, religion, sexual orientation, or any |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/2` | 0.616464 | Starfinder is a science fantasy tabletop roleplaying game (RPG) where you and a group of friends  gather to play out a story of daring adventurers exploring a galaxy filled with impossible magic,  ama |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/14` | 0.556969 | The first rule of Starfinder is that this game is *yours*. Use  it to tell the stories you want to tell, be the character  you want to be, and share exciting adventures with  friends. If any other rul |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/11/Text/2` | 0.551553 | The following example is presented to give you a better idea of  how Starfinder is played. In this adventure, Thurston is the GM.  Jenny is playing Obozaya, an aggressive vesk soldier; Jessica is  pla |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/6` | 0.547729 | Characters and their choices create the story of Starfinder,  but how they interact with each other and the galaxy around  them is governed by rules. So, while you might decide that  your character st |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/5/Text/12` | 0.532630 | In addition to this book, there are a few things you will need  to play Starfinder. These supplies can be found at your local  hobby shop or online at **paizo.com**. |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/11` | 0.530645 | Starfinder is played in sessions during which players gather in  person or online for a few hours to play the game. A complete  story can be as short as a single session, often referred to as  a "one- |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/17` | 0.516242 | Everyone involved in a Starfinder game is a player, including  the Game Master, but for the sake of simplicity, "player"  usually refers to participants other than the GM. Before  the game begins, pla |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/7/Text/2` | 0.512248 | In a Starfinder game, three modes of play determine the  pacing of each scene in the story. Most of your character's  time is spent in **exploration**, uncovering mysteries, solving  problems, and int |

### Query 26
- Text: Summarize 15902 Woodinville-Redmond Rd NE, Unit B Woodinville, WA 98072-4572
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/1/Text/28']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/1/Text/28', 'PZO22001 Starfinder Player Core 001-013::/page/2/TableCell/23', 'PZO22001 Starfinder Player Core 001-013::/page/2/TableCell/28']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/1/Text/28` | 1.026219 | 15902 Woodinville-Redmond Rd NE, Unit B Woodinville, WA 98072-4572 |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/2/TableCell/23` | 0.252465 | в |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/2/TableCell/28` | 0.228001 | 992 998 400 401 405 405 406 416 418 420 421 421 421 421 421 |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/2/TableCell/31` | 0.180458 | 435 442 457 |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/2/TableCell/19` | 0.175813 | 294 |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/2/TableCell/27` | 0.170783 | RULES OVERVIEW |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/8/SectionHeader/11` | 0.166497 | DOWNTIME |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/11/Table/9` | 0.166197 | Thurston:The autodoor stutters open. A vesk and ahuman wearing tattered spacesuits loomin the doorway. Milky eyes bulge out oftheir rotting faces. Roll for initiative! |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/9/SectionHeader/19` | 0.165014 | **Class** |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/11/TableCell/535` | 0.164784 | you notice blood smears on the floor that |

### Query 27
- Text: What is the rule about 1INTRODUCTION 4CHARACTER CREATION17LEVELING UP29EXPLORING THE GALAXY\ **2**ANCESTRIES & BACKGROUNDS 40ANDROID42BARATHU46?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/1/TableOfContents/31']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/1/TableOfContents/31', 'PZO22001 Starfinder Player Core 001-013::/page/5/Text/19', 'PZO22001 Starfinder Player Core 001-013::/page/6/Text/6']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableOfContents/31` | 0.768079 | 1INTRODUCTION 4CHARACTER CREATION17LEVELING UP29EXPLORING THE GALAXY\ **2**ANCESTRIES & BACKGROUNDS 40ANDROID42BARATHU46 HUMAN50KASATHA54LASHUNTA58PAHTRA62SHIRREN66SKITTERMANDER70VESKVERSATILE HERITAG |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/5/Text/19` | 0.578927 | Before creating your first character or adventure, you should  understand a number of basic concepts used in the game.  New concepts are presented in bold to make them easy to  find, but this chapter |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/6` | 0.555799 | Characters and their choices create the story of Starfinder,  but how they interact with each other and the galaxy around  them is governed by rules. So, while you might decide that  your character st |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/4` | 0.501026 | In addition to these key choices, PCs also have a number of  **feats**—individual abilities selected during character creation  and as the character increases in level. Every feat has a type  to denot |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/2/TableCell/27` | 0.495835 | RULES OVERVIEW |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/2/TableOfContents/2` | 0.487296 | 6EQUIPMENT232INTRODUCTION TECH GEAR ARMOR SHIELDS WEAPONS ARMOR UPGRADES WEAPON UPGRADES PRECIOUS AMMUNITION & WEAPONS GRENADES MAGIC ITEMS AUGMENTATIONS293 298 244 250 253 268 272 278 2807SPELLS294SP |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/14` | 0.485917 | The first rule of Starfinder is that this game is *yours*. Use  it to tell the stories you want to tell, be the character  you want to be, and share exciting adventures with  friends. If any other rul |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/19` | 0.485199 | If this is your first experience with a roleplaying game,  it's recommended that you take on the role of a player to  familiarize yourself with the rules and the galaxy. |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/8/Text/5` | 0.475220 | While exploration is handled in a free-form manner,  encounters are more structured. The players and GM  roll **initiative** to determine who acts in what order. The  encounter occurs over a number of |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/17` | 0.464996 | Everyone involved in a Starfinder game is a player, including  the Game Master, but for the sake of simplicity, "player"  usually refers to participants other than the GM. Before  the game begins, pla |

### Query 28
- Text: Summarize 1
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/129']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/129', 'PZO22001 Starfinder Player Core 001-013::/page/4/SectionHeader/1', 'PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/139']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/129` | 0.669108 | 1 |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/4/SectionHeader/1` | 0.449979 | CHAPTER 1: INTRODUCTION |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/139` | 0.449924 | \ **2** |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/2/TableCell/11` | 0.374893 | 6 |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/130` | 0.357231 | INTRODUCTION 4 |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/189` | 0.338191 | 5 |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/2/TableCell/17` | 0.335708 | 7 |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/11/Table/7` | 0.327861 | Dae (Jessica):I head for the airlock, then strike a pose asI step into space. "Hey Chk Chk, make sureyou're recording this!"Thurston:Now you're untethered. Are you freefloating?Dae (Jessica):Nope! I a |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableOfContents/31` | 0.325277 | 1INTRODUCTION 4CHARACTER CREATION17LEVELING UP29EXPLORING THE GALAXY\ **2**ANCESTRIES & BACKGROUNDS 40ANDROID42BARATHU46 HUMAN50KASATHA54LASHUNTA58PAHTRA62SHIRREN66SKITTERMANDER70VESKVERSATILE HERITAG |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/2/TableCell/23` | 0.323557 | в |

### Query 29
- Text: Summarize INTRODUCTION 4
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/130']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/130', 'PZO22001 Starfinder Player Core 001-013::/page/4/SectionHeader/1', 'PZO22001 Starfinder Player Core 001-013::/page/4/Text/21']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/130` | 0.927422 | INTRODUCTION 4 |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/4/SectionHeader/1` | 0.586969 | CHAPTER 1: INTRODUCTION |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/21` | 0.494951 | **INTRODUCTION** |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/13` | 0.452951 | **INTRODUCTION** |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/8/Text/14` | 0.452951 | **INTRODUCTION** |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/10/Text/33` | 0.452951 | **INTRODUCTION** |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/12/Text/29` | 0.452951 | **INTRODUCTION** |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableOfContents/31` | 0.358380 | 1INTRODUCTION 4CHARACTER CREATION17LEVELING UP29EXPLORING THE GALAXY\ **2**ANCESTRIES & BACKGROUNDS 40ANDROID42BARATHU46 HUMAN50KASATHA54LASHUNTA58PAHTRA62SHIRREN66SKITTERMANDER70VESKVERSATILE HERITAG |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/140` | 0.353196 | ANCESTRIES & BACKGROUNDS 40 |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/2/TableCell/11` | 0.341344 | 6 |

### Query 30
- Text: What is the rule about CHARACTER CREATION17?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/132']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/132', 'PZO22001 Starfinder Player Core 001-013::/page/4/Text/22', 'PZO22001 Starfinder Player Core 001-013::/page/12/Text/30']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/132` | 0.866330 | CHARACTER CREATION17 |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/22` | 0.583669 | **Character ** **Creation** |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/12/Text/30` | 0.583669 | **Character ** **Creation** |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/14` | 0.541669 | **Character ** **Creation** |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/8/Text/15` | 0.541669 | **Character ** **Creation** |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/10/Text/34` | 0.541669 | **Character ** **Creation** |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/17` | 0.441338 | Everyone involved in a Starfinder game is a player, including  the Game Master, but for the sake of simplicity, "player"  usually refers to participants other than the GM. Before  the game begins, pla |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/10/Text/8` | 0.418506 | This is a character created and controlled by a player. |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/2` | 0.395063 | In addition to level, characters are defined by **attributes**,  which measure raw potential and are used to calculate  most of their other statistics. There are six attributes in the  game. **Strengt |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/7/Text/6` | 0.388030 | For example, while aboard a starship traveling to a faraway  world, your character might find a faster route through an  uncharted asteroid field. You decide to go for it, but the GM  declares this a |

### Query 31
- Text: Summarize LEVELING UP29
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/134']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/134', 'PZO22001 Starfinder Player Core 001-013::/page/8/Text/16', 'PZO22001 Starfinder Player Core 001-013::/page/10/Text/35']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/134` | 0.973601 | LEVELING UP29 |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/8/Text/16` | 0.772425 | **Leveling Up** |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/10/Text/35` | 0.772425 | **Leveling Up** |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/15` | 0.730425 | **Leveling Up** |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/23` | 0.730425 | **Leveling Up** |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/12/Text/31` | 0.605782 | **Leveling Up** **Exploring the ** |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableOfContents/31` | 0.298690 | 1INTRODUCTION 4CHARACTER CREATION17LEVELING UP29EXPLORING THE GALAXY\ **2**ANCESTRIES & BACKGROUNDS 40ANDROID42BARATHU46 HUMAN50KASATHA54LASHUNTA58PAHTRA62SHIRREN66SKITTERMANDER70VESKVERSATILE HERITAG |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/2/TableCell/19` | 0.293422 | 294 |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/148` | 0.285046 | LASHUNTA58 |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/2/TableCell/16` | 0.272110 | 293 298 244 250 253 268 272 278 280 |

### Query 32
- Text: Summarize EXPLORING THE GALAXY
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/136']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/136', 'PZO22001 Starfinder Player Core 001-013::/page/4/Text/24', 'PZO22001 Starfinder Player Core 001-013::/page/8/Text/17']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/136` | 0.954115 | EXPLORING THE GALAXY |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/24` | 0.737074 | **Exploring the ** **Galaxy** |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/8/Text/17` | 0.737074 | **Exploring the ** **Galaxy** |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/16` | 0.695074 | **Exploring the ** **Galaxy** |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/10/Text/36` | 0.695074 | **Exploring the ** **Galaxy** |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/6/SectionHeader/8` | 0.621738 | **THE GALAXY AS A PARTICIPANT** |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/9/SectionHeader/29` | 0.543518 | **The Galaxy** |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/7/SectionHeader/10` | 0.540505 | EXPLORATION |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableOfContents/31` | 0.502653 | 1INTRODUCTION 4CHARACTER CREATION17LEVELING UP29EXPLORING THE GALAXY\ **2**ANCESTRIES & BACKGROUNDS 40ANDROID42BARATHU46 HUMAN50KASATHA54LASHUNTA58PAHTRA62SHIRREN66SKITTERMANDER70VESKVERSATILE HERITAG |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/12/Text/31` | 0.483400 | **Leveling Up** **Exploring the ** |

### Query 33
- Text: Summarize \ **2**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/139']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/139', 'PZO22001 Starfinder Player Core 001-013::/page/4/Text/21', 'PZO22001 Starfinder Player Core 001-013::/page/6/Text/13']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/139` | 0.887233 | \ **2** |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/21` | 0.509089 | **INTRODUCTION** |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/13` | 0.509089 | **INTRODUCTION** |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/8/Text/14` | 0.467089 | **INTRODUCTION** |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/12/Text/29` | 0.467089 | **INTRODUCTION** |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/10/Text/33` | 0.467089 | **INTRODUCTION** |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/1/SectionHeader/0` | 0.463703 | **AUTHORS ** |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/9/SectionHeader/13` | 0.447019 | **Background** |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/129` | 0.422918 | 1 |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/9/SectionHeader/17` | 0.421615 | **Check** |

### Query 34
- Text: What is the rule about ANCESTRIES & BACKGROUNDS 40?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/140']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/140', 'PZO22001 Starfinder Player Core 001-013::/page/4/Text/26', 'PZO22001 Starfinder Player Core 001-013::/page/10/Text/38']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/140` | 0.913636 | ANCESTRIES & BACKGROUNDS 40 |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/26` | 0.729294 | **ANCESTRIES & ** **BACKGROUNDS** |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/10/Text/38` | 0.729294 | **ANCESTRIES & ** **BACKGROUNDS** |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/18` | 0.699294 | **ANCESTRIES & ** **BACKGROUNDS** |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/12/Text/33` | 0.699294 | **ANCESTRIES & ** **BACKGROUNDS** |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/8/Text/19` | 0.699294 | **ANCESTRIES & ** **BACKGROUNDS** |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/2/TableCell/27` | 0.417974 | RULES OVERVIEW |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/9/Text/6` | 0.415204 | An ancestry is the broad family of people that a character  belongs to. Ancestry determines a character's starting Hit  Points, languages, senses, and Speed, and it grants access  to ancestry feats. A |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/164` | 0.361850 | BACKGROUNDS92 |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableOfContents/31` | 0.356387 | 1INTRODUCTION 4CHARACTER CREATION17LEVELING UP29EXPLORING THE GALAXY\ **2**ANCESTRIES & BACKGROUNDS 40ANDROID42BARATHU46 HUMAN50KASATHA54LASHUNTA58PAHTRA62SHIRREN66SKITTERMANDER70VESKVERSATILE HERITAG |

### Query 35
- Text: Summarize ANDROID42
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/142']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/142', 'PZO22001 Starfinder Player Core 001-013::/page/1/TableOfContents/31', 'PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/170']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/142` | 0.927884 | ANDROID42 |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableOfContents/31` | 0.422131 | 1INTRODUCTION 4CHARACTER CREATION17LEVELING UP29EXPLORING THE GALAXY\ **2**ANCESTRIES & BACKGROUNDS 40ANDROID42BARATHU46 HUMAN50KASATHA54LASHUNTA58PAHTRA62SHIRREN66SKITTERMANDER70VESKVERSATILE HERITAG |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/170` | 0.380467 | ENVOY102 |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/2/TableCell/31` | 0.314899 | 435 442 457 |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/164` | 0.305220 | BACKGROUNDS92 |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/140` | 0.290794 | ANCESTRIES & BACKGROUNDS 40 |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/2/TableOfContents/2` | 0.280670 | 6EQUIPMENT232INTRODUCTION TECH GEAR ARMOR SHIELDS WEAPONS ARMOR UPGRADES WEAPON UPGRADES PRECIOUS AMMUNITION & WEAPONS GRENADES MAGIC ITEMS AUGMENTATIONS293 298 244 250 253 268 272 278 2807SPELLS294SP |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/146` | 0.278596 | KASATHA54 |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/150` | 0.275515 | PAHTRA62 |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/182` | 0.262179 | SKILLS 182 |

### Query 36
- Text: Summarize BARATHU46
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/144']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/144', 'PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/146', 'PZO22001 Starfinder Player Core 001-013::/page/2/TableCell/11']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/144` | 0.740479 | BARATHU46 HUMAN50 |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/146` | 0.404236 | KASATHA54 |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/2/TableCell/11` | 0.377861 | 6 |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableOfContents/31` | 0.326972 | 1INTRODUCTION 4CHARACTER CREATION17LEVELING UP29EXPLORING THE GALAXY\ **2**ANCESTRIES & BACKGROUNDS 40ANDROID42BARATHU46 HUMAN50KASATHA54LASHUNTA58PAHTRA62SHIRREN66SKITTERMANDER70VESKVERSATILE HERITAG |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/148` | 0.321389 | LASHUNTA58 |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/2/TableCell/13` | 0.320554 | 232 |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/150` | 0.298673 | PAHTRA62 |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/160` | 0.298184 | BORAI 84 |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/2/TableCell/25` | 0.297937 | 388 |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/140` | 0.289667 | ANCESTRIES & BACKGROUNDS 40 |

### Query 37
- Text: Summarize KASATHA54
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/146']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/146', 'PZO22001 Starfinder Player Core 001-013::/page/1/TableOfContents/31', 'PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/144']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/146` | 0.955850 | KASATHA54 |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableOfContents/31` | 0.408594 | 1INTRODUCTION 4CHARACTER CREATION17LEVELING UP29EXPLORING THE GALAXY\ **2**ANCESTRIES & BACKGROUNDS 40ANDROID42BARATHU46 HUMAN50KASATHA54LASHUNTA58PAHTRA62SHIRREN66SKITTERMANDER70VESKVERSATILE HERITAG |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/144` | 0.392119 | BARATHU46 HUMAN50 |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/172` | 0.339141 | MYSTIC114 |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/148` | 0.323233 | LASHUNTA58 |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/130` | 0.313132 | INTRODUCTION 4 |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/150` | 0.301832 | PAHTRA62 |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/140` | 0.301404 | ANCESTRIES & BACKGROUNDS 40 |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/160` | 0.278964 | BORAI 84 |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/189` | 0.276007 | 5 |

### Query 38
- Text: Summarize LASHUNTA58
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/148']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/148', 'PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/146', 'PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/162']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/148` | 0.981129 | LASHUNTA58 |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/146` | 0.368021 | KASATHA54 |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/162` | 0.342785 | PRISMENI88 |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/144` | 0.293418 | BARATHU46 HUMAN50 |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/134` | 0.279302 | LEVELING UP29 |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableOfContents/31` | 0.273382 | 1INTRODUCTION 4CHARACTER CREATION17LEVELING UP29EXPLORING THE GALAXY\ **2**ANCESTRIES & BACKGROUNDS 40ANDROID42BARATHU46 HUMAN50KASATHA54LASHUNTA58PAHTRA62SHIRREN66SKITTERMANDER70VESKVERSATILE HERITAG |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/150` | 0.272368 | PAHTRA62 |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/2/TableCell/13` | 0.271873 | 232 |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/12/Text/41` | 0.263666 | **GLOSSARY & ** **INDEX** |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/8/Text/27` | 0.263666 | **GLOSSARY & ** **INDEX** |

### Query 39
- Text: Summarize PAHTRA62
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/150']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/150', 'PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/152', 'PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/188']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/150` | 0.973039 | PAHTRA62 |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/152` | 0.370049 | SHIRREN66 |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/188` | 0.350199 | SKILLS 192 |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/164` | 0.301922 | BACKGROUNDS92 |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/146` | 0.291322 | KASATHA54 |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/10/Text/29` | 0.290139 | All the traits used in this book appear in the Glossary  and Index beginning on page 442. |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/158` | 0.278950 | VERSATILE HERITAGES 82 |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/148` | 0.272224 | LASHUNTA58 |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/170` | 0.267359 | ENVOY102 |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/142` | 0.264972 | ANDROID42 |

### Query 40
- Text: Summarize SHIRREN66
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/152']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/152', 'PZO22001 Starfinder Player Core 001-013::/page/2/TableCell/11', 'PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/150']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/152` | 0.959671 | SHIRREN66 |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/2/TableCell/11` | 0.389892 | 6 |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/150` | 0.362225 | PAHTRA62 |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableOfContents/31` | 0.308753 | 1INTRODUCTION 4CHARACTER CREATION17LEVELING UP29EXPLORING THE GALAXY\ **2**ANCESTRIES & BACKGROUNDS 40ANDROID42BARATHU46 HUMAN50KASATHA54LASHUNTA58PAHTRA62SHIRREN66SKITTERMANDER70VESKVERSATILE HERITAG |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/2/TableOfContents/2` | 0.301651 | 6EQUIPMENT232INTRODUCTION TECH GEAR ARMOR SHIELDS WEAPONS ARMOR UPGRADES WEAPON UPGRADES PRECIOUS AMMUNITION & WEAPONS GRENADES MAGIC ITEMS AUGMENTATIONS293 298 244 250 253 268 272 278 2807SPELLS294SP |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/154` | 0.294893 | SKITTERMANDER70 |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/12/SectionHeader/19` | 0.273503 | **Thurston:** The creature snarls as the ribbon of starlight  lashes across its torso, singeing its ruined |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/162` | 0.271347 | PRISMENI88 |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/11/Text/2` | 0.255119 | The following example is presented to give you a better idea of  how Starfinder is played. In this adventure, Thurston is the GM.  Jenny is playing Obozaya, an aggressive vesk soldier; Jessica is  pla |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/12/Text/17` | 0.253318 | **Dae (Jessica):** My black battle ribbon bursts into solar  flame. I pirouette and attack the vesk,  making sure the camera drone can see all  my moves. I rolled a 26. |

### Query 41
- Text: Summarize SKITTERMANDER70
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/154']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/154', 'PZO22001 Starfinder Player Core 001-013::/page/1/TableOfContents/31', 'PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/152']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/154` | 0.976616 | SKITTERMANDER70 |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableOfContents/31` | 0.387890 | 1INTRODUCTION 4CHARACTER CREATION17LEVELING UP29EXPLORING THE GALAXY\ **2**ANCESTRIES & BACKGROUNDS 40ANDROID42BARATHU46 HUMAN50KASATHA54LASHUNTA58PAHTRA62SHIRREN66SKITTERMANDER70VESKVERSATILE HERITAG |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/152` | 0.341781 | SHIRREN66 |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/144` | 0.280717 | BARATHU46 HUMAN50 |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/132` | 0.277387 | CHARACTER CREATION17 |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/2/TableCell/17` | 0.274735 | 7 |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/2/TableOfContents/2` | 0.267572 | 6EQUIPMENT232INTRODUCTION TECH GEAR ARMOR SHIELDS WEAPONS ARMOR UPGRADES WEAPON UPGRADES PRECIOUS AMMUNITION & WEAPONS GRENADES MAGIC ITEMS AUGMENTATIONS293 298 244 250 253 268 272 278 2807SPELLS294SP |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/166` | 0.247990 | LANGUAGES97 |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/11/Table/3` | 0.245694 | Thurston:Your ship speeds through the swirlingcolors and half-formed shapes of the Drift.You're getting close to the coordinates, butchunks of rock, ice, and metal scrap floatahead of you, blocking yo |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/11/Table/7` | 0.243460 | Dae (Jessica):I head for the airlock, then strike a pose asI step into space. "Hey Chk Chk, make sureyou're recording this!"Thurston:Now you're untethered. Are you freefloating?Dae (Jessica):Nope! I a |

### Query 42
- Text: Summarize VESK
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/156']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/156', 'PZO22001 Starfinder Player Core 001-013::/page/12/TableCell/460', 'PZO22001 Starfinder Player Core 001-013::/page/12/TableCell/470']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/156` | 0.903355 | VESK |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/12/TableCell/460` | 0.472273 | shoot the vesk with my new laser pistol! |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/12/TableCell/470` | 0.430116 | The rotting vesk recoils as laser fire hits it, |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/11/TableCell/569` | 0.381756 | The autodoor stutters open. A vesk and a |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/12/Table/6` | 0.320934 | Zemir (Mike):For my third action, I Take Cover behind arock in my quantum field.Thurston:The rotting vesk recoils as laser fire hits it,then it shoots a bolt of void energy at you. |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/12/Text/17` | 0.320090 | **Dae (Jessica):** My black battle ribbon bursts into solar  flame. I pirouette and attack the vesk,  making sure the camera drone can see all  my moves. I rolled a 26. |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/11/TableCell/480` | 0.277582 | Dae (Jessica): |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/11/TableCell/514` | 0.277582 | Dae (Jessica): |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/11/TableCell/500` | 0.277582 | Dae (Jessica): |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/11/TableCell/490` | 0.277582 | Dae (Jessica): |

### Query 43
- Text: Summarize VERSATILE HERITAGES 82
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/158']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/158', 'PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/180', 'PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/182']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/158` | 0.992499 | VERSATILE HERITAGES 82 |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/180` | 0.407710 | ARCHETYPES174 |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/182` | 0.374764 | SKILLS 182 |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/160` | 0.336518 | BORAI 84 |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableOfContents/31` | 0.328001 | 1INTRODUCTION 4CHARACTER CREATION17LEVELING UP29EXPLORING THE GALAXY\ **2**ANCESTRIES & BACKGROUNDS 40ANDROID42BARATHU46 HUMAN50KASATHA54LASHUNTA58PAHTRA62SHIRREN66SKITTERMANDER70VESKVERSATILE HERITAG |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/2/TableCell/13` | 0.298866 | 232 |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/10/Text/29` | 0.288663 | All the traits used in this book appear in the Glossary  and Index beginning on page 442. |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/164` | 0.282544 | BACKGROUNDS92 |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/140` | 0.270887 | ANCESTRIES & BACKGROUNDS 40 |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/162` | 0.267221 | PRISMENI88 |

### Query 44
- Text: Summarize BORAI 84
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/160']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/160', 'PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/158', 'PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/162']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/160` | 0.973024 | BORAI 84 |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/158` | 0.382551 | VERSATILE HERITAGES 82 |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/162` | 0.333629 | PRISMENI88 |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/146` | 0.265482 | KASATHA54 |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableOfContents/31` | 0.262565 | 1INTRODUCTION 4CHARACTER CREATION17LEVELING UP29EXPLORING THE GALAXY\ **2**ANCESTRIES & BACKGROUNDS 40ANDROID42BARATHU46 HUMAN50KASATHA54LASHUNTA58PAHTRA62SHIRREN66SKITTERMANDER70VESKVERSATILE HERITAG |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/150` | 0.262236 | PAHTRA62 |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/172` | 0.256383 | MYSTIC114 |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/140` | 0.245964 | ANCESTRIES & BACKGROUNDS 40 |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/164` | 0.243304 | BACKGROUNDS92 |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/130` | 0.239914 | INTRODUCTION 4 |

### Query 45
- Text: Summarize PRISMENI88
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/162']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/162', 'PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/148', 'PZO22001 Starfinder Player Core 001-013::/page/2/TableCell/25']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/162` | 0.944962 | PRISMENI88 |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/148` | 0.360727 | LASHUNTA58 |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/2/TableCell/25` | 0.348358 | 388 |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/160` | 0.307104 | BORAI 84 |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/152` | 0.295406 | SHIRREN66 |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/158` | 0.282004 | VERSATILE HERITAGES 82 |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/2/TableCell/13` | 0.276762 | 232 |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/12/Text/41` | 0.263630 | **GLOSSARY & ** **INDEX** |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/8/Text/27` | 0.263630 | **GLOSSARY & ** **INDEX** |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/34` | 0.263630 | **GLOSSARY & ** **INDEX** |

### Query 46
- Text: What is the rule about BACKGROUNDS92?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/164']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/164', 'PZO22001 Starfinder Player Core 001-013::/page/12/Text/33', 'PZO22001 Starfinder Player Core 001-013::/page/8/Text/19']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/164` | 0.852713 | BACKGROUNDS92 |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/12/Text/33` | 0.492712 | **ANCESTRIES & ** **BACKGROUNDS** |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/8/Text/19` | 0.492712 | **ANCESTRIES & ** **BACKGROUNDS** |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/26` | 0.462712 | **ANCESTRIES & ** **BACKGROUNDS** |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/18` | 0.462712 | **ANCESTRIES & ** **BACKGROUNDS** |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/10/Text/38` | 0.462712 | **ANCESTRIES & ** **BACKGROUNDS** |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/140` | 0.423350 | ANCESTRIES & BACKGROUNDS 40 |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/9/SectionHeader/13` | 0.408206 | **Background** |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/2/TableCell/27` | 0.397261 | RULES OVERVIEW |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/9/Text/14` | 0.361979 | A background represents what a character experienced  before they became an adventurer. Each background  grants a feat and training in one or more skills. You can  read more about backgrounds in Chapt |

### Query 47
- Text: Summarize LANGUAGES97
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/166']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/166', 'PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/168', 'PZO22001 Starfinder Player Core 001-013::/page/1/TableOfContents/31']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/166` | 0.946943 | LANGUAGES97 |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/168` | 0.452126 | CLASSES 98 |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableOfContents/31` | 0.398843 | 1INTRODUCTION 4CHARACTER CREATION17LEVELING UP29EXPLORING THE GALAXY\ **2**ANCESTRIES & BACKGROUNDS 40ANDROID42BARATHU46 HUMAN50KASATHA54LASHUNTA58PAHTRA62SHIRREN66SKITTERMANDER70VESKVERSATILE HERITAG |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/164` | 0.368637 | BACKGROUNDS92 |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/180` | 0.337283 | ARCHETYPES174 |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/132` | 0.331874 | CHARACTER CREATION17 |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/2/TableOfContents/2` | 0.324420 | 6EQUIPMENT232INTRODUCTION TECH GEAR ARMOR SHIELDS WEAPONS ARMOR UPGRADES WEAPON UPGRADES PRECIOUS AMMUNITION & WEAPONS GRENADES MAGIC ITEMS AUGMENTATIONS293 298 244 250 253 268 272 278 2807SPELLS294SP |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/188` | 0.315346 | SKILLS 192 |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/2/TableCell/17` | 0.305610 | 7 |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/154` | 0.276068 | SKITTERMANDER70 |

### Query 48
- Text: Summarize (∃)
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/167']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/167', 'PZO22001 Starfinder Player Core 001-013::/page/1/TableOfContents/31', 'PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/139']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/167` | 0.773422 | (∃) |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableOfContents/31` | 0.369704 | 1INTRODUCTION 4CHARACTER CREATION17LEVELING UP29EXPLORING THE GALAXY\ **2**ANCESTRIES & BACKGROUNDS 40ANDROID42BARATHU46 HUMAN50KASATHA54LASHUNTA58PAHTRA62SHIRREN66SKITTERMANDER70VESKVERSATILE HERITAG |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/139` | 0.364908 | \ **2** |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/11/SectionHeader/1` | 0.296947 | EXAMPLE OF PLAY |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/21` | 0.291131 | **INTRODUCTION** |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/12/Text/29` | 0.291131 | **INTRODUCTION** |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/10/Text/33` | 0.291131 | **INTRODUCTION** |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/8/Text/14` | 0.291131 | **INTRODUCTION** |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/13` | 0.291131 | **INTRODUCTION** |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/11` | 0.289030 | A single narrative—including the setup, plot, and  conclusion—is called an **adventure**. A series of adventures  creates an even larger narrative called a **campaign**. An  adventure might take sever |

### Query 49
- Text: Summarize CLASSES 98
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/168']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/168', 'PZO22001 Starfinder Player Core 001-013::/page/10/Text/39', 'PZO22001 Starfinder Player Core 001-013::/page/8/Text/20']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/168` | 0.961064 | CLASSES 98 |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/10/Text/39` | 0.614221 | **CLASSES** |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/8/Text/20` | 0.614221 | **CLASSES** |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/19` | 0.584221 | **CLASSES** |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/27` | 0.584221 | **CLASSES** |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/12/Text/34` | 0.584221 | **CLASSES** |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/166` | 0.443157 | LANGUAGES97 |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/9/SectionHeader/19` | 0.441872 | **Class** |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/188` | 0.421218 | SKILLS 192 |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/182` | 0.389634 | SKILLS 182 |

### Query 50
- Text: Summarize ENVOY102
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/170']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/170', 'PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/164', 'PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/142']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/170` | 0.955025 | ENVOY102 |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/164` | 0.396779 | BACKGROUNDS92 |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/142` | 0.382314 | ANDROID42 |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/8/SectionHeader/3` | 0.307752 | ENCOUNTERS |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableOfContents/31` | 0.300148 | 1INTRODUCTION 4CHARACTER CREATION17LEVELING UP29EXPLORING THE GALAXY\ **2**ANCESTRIES & BACKGROUNDS 40ANDROID42BARATHU46 HUMAN50KASATHA54LASHUNTA58PAHTRA62SHIRREN66SKITTERMANDER70VESKVERSATILE HERITAG |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/188` | 0.299409 | SKILLS 192 |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/182` | 0.297597 | SKILLS 182 |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/150` | 0.277166 | PAHTRA62 |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/2/TableOfContents/2` | 0.268692 | 6EQUIPMENT232INTRODUCTION TECH GEAR ARMOR SHIELDS WEAPONS ARMOR UPGRADES WEAPON UPGRADES PRECIOUS AMMUNITION & WEAPONS GRENADES MAGIC ITEMS AUGMENTATIONS293 298 244 250 253 268 272 278 2807SPELLS294SP |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/140` | 0.257929 | ANCESTRIES & BACKGROUNDS 40 |

### Query 51
- Text: Summarize MYSTIC114
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/172']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/172', 'PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/146', 'PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/180']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/172` | 0.951944 | MYSTIC114 |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/146` | 0.357735 | KASATHA54 |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/180` | 0.325614 | ARCHETYPES174 |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableOfContents/31` | 0.251358 | 1INTRODUCTION 4CHARACTER CREATION17LEVELING UP29EXPLORING THE GALAXY\ **2**ANCESTRIES & BACKGROUNDS 40ANDROID42BARATHU46 HUMAN50KASATHA54LASHUNTA58PAHTRA62SHIRREN66SKITTERMANDER70VESKVERSATILE HERITAG |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/160` | 0.251300 | BORAI 84 |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/5/Text/16` | 0.230571 | *Starfinder Alien Core:* From the vanguard components  of the Swarm to immensely powerful starmetal dragons,  monsters are a common threat that the PCs might face, and  each type has its own statistic |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/182` | 0.225375 | SKILLS 182 |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/2/TableOfContents/2` | 0.225104 | 6EQUIPMENT232INTRODUCTION TECH GEAR ARMOR SHIELDS WEAPONS ARMOR UPGRADES WEAPON UPGRADES PRECIOUS AMMUNITION & WEAPONS GRENADES MAGIC ITEMS AUGMENTATIONS293 298 244 250 253 268 272 278 2807SPELLS294SP |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/130` | 0.223444 | INTRODUCTION 4 |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/8/Text/7` | 0.217240 | Attacking another creature is one of the most common  actions in combat and is done by using the **Strike** action.  This requires an attack roll—a kind of check made against  the **Armor** **Class (A |

### Query 52
- Text: Summarize OPERATIVE
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/174']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/174', 'PZO22001 Starfinder Player Core 001-013::/page/9/SectionHeader/3', 'PZO22001 Starfinder Player Core 001-013::/page/8/Text/5']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/174` | 0.899805 | OPERATIVE |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/9/SectionHeader/3` | 0.371410 | **Action** |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/8/Text/5` | 0.347191 | While exploration is handled in a free-form manner,  encounters are more structured. The players and GM  roll **initiative** to determine who acts in what order. The  encounter occurs over a number of |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/9/SectionHeader/33` | 0.304768 | **Initiative** |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/11/SectionHeader/1` | 0.286164 | EXAMPLE OF PLAY |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableOfContents/31` | 0.285138 | 1INTRODUCTION 4CHARACTER CREATION17LEVELING UP29EXPLORING THE GALAXY\ **2**ANCESTRIES & BACKGROUNDS 40ANDROID42BARATHU46 HUMAN50KASATHA54LASHUNTA58PAHTRA62SHIRREN66SKITTERMANDER70VESKVERSATILE HERITAG |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/7/Text/4` | 0.281246 | Once a check is rolled, the GM compares the result to a  target number called the **difficulty** **class (DC) **to determine  the outcome. If the result of the check is equal to or greater  than the D |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/5/SectionHeader/18` | 0.270859 | BASICS OF PLAY |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/9/SectionHeader/1` | 0.269302 | **KEY TERMS** |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/9/Text/4` | 0.264062 | During encounters, each creature gets three actions during  their turn. These actions are spent to attack, interact with  objects, move, and use special abilities. Actions available to  all characters |

### Query 53
- Text: Summarize SOLARIAN
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/176']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/176', 'PZO22001 Starfinder Player Core 001-013::/page/8/Text/27', 'PZO22001 Starfinder Player Core 001-013::/page/6/Text/27']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/176` | 0.954773 | SOLARIAN |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/27` | 0.330348 | **GLOSSARY & ** **INDEX** |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/8/Text/27` | 0.330348 | **GLOSSARY & ** **INDEX** |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/34` | 0.288348 | **GLOSSARY & ** **INDEX** |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/10/Text/46` | 0.288348 | **GLOSSARY & ** **INDEX** |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/12/Text/41` | 0.288348 | **GLOSSARY & ** **INDEX** |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/12/Text/1` | 0.284617 | his quantum field, an area of warped reality he controls. He  chooses to center it between the enemy and himself. Solarians  can Attune as a free action when they roll initiative, so Dae  chooses to b |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableOfContents/31` | 0.281350 | 1INTRODUCTION 4CHARACTER CREATION17LEVELING UP29EXPLORING THE GALAXY\ **2**ANCESTRIES & BACKGROUNDS 40ANDROID42BARATHU46 HUMAN50KASATHA54LASHUNTA58PAHTRA62SHIRREN66SKITTERMANDER70VESKVERSATILE HERITAG |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/9/Text/30` | 0.238507 | Starfinder is set in the Pact Worlds, a system of allied  planets that was once home to the lost world Golarion,  though many adventures explore the wider galaxy.  More information about the galaxy ca |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/12/Text/15` | 0.230835 | Stellar Rush is a solarian feat that lets Dae Stride twice with  a +10 circumstance bonus to their movement speed. When  Dae finishes both Strides, enemies within 15 feet attempt a  Fortitude save to |

### Query 54
- Text: Summarize WITCHWARPER
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/178']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/178', 'PZO22001 Starfinder Player Core 001-013::/page/12/TableCell/448', 'PZO22001 Starfinder Player Core 001-013::/page/12/Table/2']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/178` | 0.962389 | WITCHWARPER |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/12/TableCell/448` | 0.383965 | Focus Point to cast warp terrain. |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/12/Table/2` | 0.351472 | Thurston:Zemir, you're up first.Zemir (Mike):Excellent. For my first action, I spend 1Focus Point to cast warp terrain.Thurston:Which effect do you choose?Zemir (Mike):I choose difficult terrain. My q |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/2/TableOfContents/2` | 0.291536 | 6EQUIPMENT232INTRODUCTION TECH GEAR ARMOR SHIELDS WEAPONS ARMOR UPGRADES WEAPON UPGRADES PRECIOUS AMMUNITION & WEAPONS GRENADES MAGIC ITEMS AUGMENTATIONS293 298 244 250 253 268 272 278 2807SPELLS294SP |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableOfContents/31` | 0.285945 | 1INTRODUCTION 4CHARACTER CREATION17LEVELING UP29EXPLORING THE GALAXY\ **2**ANCESTRIES & BACKGROUNDS 40ANDROID42BARATHU46 HUMAN50KASATHA54LASHUNTA58PAHTRA62SHIRREN66SKITTERMANDER70VESKVERSATILE HERITAG |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/156` | 0.284462 | VESK |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/3` | 0.278294 | Your player character is also defined by some key choices  you make. The first choice is a PC's **ancestry**, representing the  character's parents and heritage, such as barathu, human, or  vesk. Next |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/2/TableCell/15` | 0.276776 | INTRODUCTION TECH GEAR ARMOR SHIELDS WEAPONS ARMOR UPGRADES WEAPON UPGRADES PRECIOUS AMMUNITION & WEAPONS GRENADES MAGIC ITEMS AUGMENTATIONS |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/11/Table/7` | 0.276162 | Dae (Jessica):I head for the airlock, then strike a pose asI step into space. "Hey Chk Chk, make sureyou're recording this!"Thurston:Now you're untethered. Are you freefloating?Dae (Jessica):Nope! I a |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/11/Table/5` | 0.259408 | Zemir (Mike):"Thanks, Chk Chk." I chug some coffee andtry again. 13! I've got a +7 to Piloting sothat's a 20!Thurston:The ship zooms safely through thedebris until the beacon you were sent toinvestiga |

### Query 55
- Text: Summarize ARCHETYPES174
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/180']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/180', 'PZO22001 Starfinder Player Core 001-013::/page/1/TableOfContents/31', 'PZO22001 Starfinder Player Core 001-013::/page/2/TableCell/13']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/180` | 0.987618 | ARCHETYPES174 |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableOfContents/31` | 0.418844 | 1INTRODUCTION 4CHARACTER CREATION17LEVELING UP29EXPLORING THE GALAXY\ **2**ANCESTRIES & BACKGROUNDS 40ANDROID42BARATHU46 HUMAN50KASATHA54LASHUNTA58PAHTRA62SHIRREN66SKITTERMANDER70VESKVERSATILE HERITAG |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/2/TableCell/13` | 0.415767 | 232 |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/158` | 0.366800 | VERSATILE HERITAGES 82 |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/132` | 0.355507 | CHARACTER CREATION17 |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/2/TableOfContents/2` | 0.330361 | 6EQUIPMENT232INTRODUCTION TECH GEAR ARMOR SHIELDS WEAPONS ARMOR UPGRADES WEAPON UPGRADES PRECIOUS AMMUNITION & WEAPONS GRENADES MAGIC ITEMS AUGMENTATIONS293 298 244 250 253 268 272 278 2807SPELLS294SP |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/140` | 0.321908 | ANCESTRIES & BACKGROUNDS 40 |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/188` | 0.307449 | SKILLS 192 |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/166` | 0.299079 | LANGUAGES97 |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/182` | 0.297710 | SKILLS 182 |

### Query 56
- Text: What is the rule about SKILLS 182?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/182']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/182', 'PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/188', 'PZO22001 Starfinder Player Core 001-013::/page/4/Text/28']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/182` | 0.877572 | SKILLS 182 |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/188` | 0.629623 | SKILLS 192 |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/28` | 0.484687 | **SKILLS** |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/10/Text/40` | 0.442687 | **SKILLS** |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/12/Text/35` | 0.442687 | **SKILLS** |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/8/Text/21` | 0.442687 | **SKILLS** |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/20` | 0.442687 | **SKILLS** |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/184` | 0.405026 | SKILLS TABLE |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/186` | 0.393742 | GENERAL SKILL ACTIONS |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/10/Text/21` | 0.391086 | A skill represents a creature's ability to perform certain  tasks that require instruction or practice. All characters are  trained in certain skills due to their background and class.  Skills are ful |

### Query 57
- Text: What is the rule about SKILLS TABLE?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/184']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/184', 'PZO22001 Starfinder Player Core 001-013::/page/4/Text/28', 'PZO22001 Starfinder Player Core 001-013::/page/8/Text/21']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/184` | 0.881120 | SKILLS TABLE |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/28` | 0.540360 | **SKILLS** |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/8/Text/21` | 0.540360 | **SKILLS** |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/20` | 0.498360 | **SKILLS** |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/12/Text/35` | 0.498360 | **SKILLS** |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/10/Text/40` | 0.498360 | **SKILLS** |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/10/Text/21` | 0.452694 | A skill represents a creature's ability to perform certain  tasks that require instruction or practice. All characters are  trained in certain skills due to their background and class.  Skills are ful |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/186` | 0.421424 | GENERAL SKILL ACTIONS |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/10/SectionHeader/20` | 0.409929 | **Skill** |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableOfContents/31` | 0.403303 | 1INTRODUCTION 4CHARACTER CREATION17LEVELING UP29EXPLORING THE GALAXY\ **2**ANCESTRIES & BACKGROUNDS 40ANDROID42BARATHU46 HUMAN50KASATHA54LASHUNTA58PAHTRA62SHIRREN66SKITTERMANDER70VESKVERSATILE HERITAG |

### Query 58
- Text: What is the rule about GENERAL SKILL ACTIONS?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/186']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/186', 'PZO22001 Starfinder Player Core 001-013::/page/8/Text/5', 'PZO22001 Starfinder Player Core 001-013::/page/4/Text/28']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/186` | 0.893908 | GENERAL SKILL ACTIONS |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/8/Text/5` | 0.500552 | While exploration is handled in a free-form manner,  encounters are more structured. The players and GM  roll **initiative** to determine who acts in what order. The  encounter occurs over a number of |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/28` | 0.470043 | **SKILLS** |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/10/Text/40` | 0.428043 | **SKILLS** |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/8/Text/21` | 0.428043 | **SKILLS** |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/20` | 0.428043 | **SKILLS** |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/12/Text/35` | 0.428043 | **SKILLS** |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/10/Text/21` | 0.426994 | A skill represents a creature's ability to perform certain  tasks that require instruction or practice. All characters are  trained in certain skills due to their background and class.  Skills are ful |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/184` | 0.421269 | SKILLS TABLE |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/8/Text/6` | 0.405066 | **Free actions**, such as dropping an object, don't count  toward the three actions you can take on your turn. Finally,  each character can use up to one **reaction** during a round.  This special typ |

### Query 59
- Text: What is the rule about SKILLS 192?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/188']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/188', 'PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/182', 'PZO22001 Starfinder Player Core 001-013::/page/10/Text/40']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/188` | 0.869960 | SKILLS 192 |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/182` | 0.653690 | SKILLS 182 |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/10/Text/40` | 0.485660 | **SKILLS** |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/28` | 0.443660 | **SKILLS** |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/20` | 0.443660 | **SKILLS** |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/12/Text/35` | 0.443660 | **SKILLS** |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/8/Text/21` | 0.443660 | **SKILLS** |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/184` | 0.424642 | SKILLS TABLE |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/10/Text/21` | 0.416567 | A skill represents a creature's ability to perform certain  tasks that require instruction or practice. All characters are  trained in certain skills due to their background and class.  Skills are ful |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/186` | 0.384315 | GENERAL SKILL ACTIONS |

### Query 60
- Text: Summarize 5
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/189']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/189', 'PZO22001 Starfinder Player Core 001-013::/page/2/TableCell/11', 'PZO22001 Starfinder Player Core 001-013::/page/2/TableCell/17']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/189` | 0.772788 | 5 |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/2/TableCell/11` | 0.509672 | 6 |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/2/TableCell/17` | 0.454834 | 7 |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/130` | 0.399767 | INTRODUCTION 4 |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/11/TableCell/421` | 0.360649 | I rolled a 5, so with my +7 modifier I got a |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/129` | 0.347386 | 1 |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/11/Table/7` | 0.293153 | Dae (Jessica):I head for the airlock, then strike a pose asI step into space. "Hey Chk Chk, make sureyou're recording this!"Thurston:Now you're untethered. Are you freefloating?Dae (Jessica):Nope! I a |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableOfContents/31` | 0.286619 | 1INTRODUCTION 4CHARACTER CREATION17LEVELING UP29EXPLORING THE GALAXY\ **2**ANCESTRIES & BACKGROUNDS 40ANDROID42BARATHU46 HUMAN50KASATHA54LASHUNTA58PAHTRA62SHIRREN66SKITTERMANDER70VESKVERSATILE HERITAG |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/2/TableCell/23` | 0.277703 | в |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/2/TableOfContents/2` | 0.277475 | 6EQUIPMENT232INTRODUCTION TECH GEAR ARMOR SHIELDS WEAPONS ARMOR UPGRADES WEAPON UPGRADES PRECIOUS AMMUNITION & WEAPONS GRENADES MAGIC ITEMS AUGMENTATIONS293 298 244 250 253 268 272 278 2807SPELLS294SP |

### Query 61
- Text: What is the rule about FEATS 210?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/190']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/190', 'PZO22001 Starfinder Player Core 001-013::/page/8/Text/22', 'PZO22001 Starfinder Player Core 001-013::/page/10/Text/41']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/190` | 0.869310 | FEATS 210 |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/8/Text/22` | 0.579554 | **FEATS** |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/10/Text/41` | 0.579554 | **FEATS** |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/29` | 0.537554 | **FEATS** |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/21` | 0.537554 | **FEATS** |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/12/Text/36` | 0.537554 | **FEATS** |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/192` | 0.460384 | FEATS TABLE211 |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/9/SectionHeader/25` | 0.420930 | **Feat** |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/9/Text/26` | 0.409592 | A feat is an ability you can select for your character due  to their ancestry, background, class, general training, or  skill training. Some feats grant the ability to use special  actions, while othe |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/2/TableCell/27` | 0.362430 | RULES OVERVIEW |

### Query 62
- Text: What is the rule about FEATS TABLE211?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/192']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/192', 'PZO22001 Starfinder Player Core 001-013::/page/8/Text/22', 'PZO22001 Starfinder Player Core 001-013::/page/4/Text/29']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/192` | 0.897460 | FEATS TABLE211 |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/8/Text/22` | 0.580548 | **FEATS** |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/29` | 0.580548 | **FEATS** |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/10/Text/41` | 0.538548 | **FEATS** |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/12/Text/36` | 0.538548 | **FEATS** |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/21` | 0.538548 | **FEATS** |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/190` | 0.536727 | FEATS 210 |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/9/SectionHeader/25` | 0.452792 | **Feat** |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/9/Text/26` | 0.416091 | A feat is an ability you can select for your character due  to their ancestry, background, class, general training, or  skill training. Some feats grant the ability to use special  actions, while othe |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/184` | 0.403355 | SKILLS TABLE |

### Query 63
- Text: What is the rule about 6EQUIPMENT232INTRODUCTION?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/2/TableOfContents/2']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/2/TableCell/12', 'PZO22001 Starfinder Player Core 001-013::/page/2/TableOfContents/2', 'PZO22001 Starfinder Player Core 001-013::/page/8/Text/23']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/2/TableCell/12` | 0.466349 | EQUIPMENT |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/2/TableOfContents/2` | 0.464397 | 6EQUIPMENT232INTRODUCTION TECH GEAR ARMOR SHIELDS WEAPONS ARMOR UPGRADES WEAPON UPGRADES PRECIOUS AMMUNITION & WEAPONS GRENADES MAGIC ITEMS AUGMENTATIONS293 298 244 250 253 268 272 278 2807SPELLS294SP |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/8/Text/23` | 0.453288 | **EQUIPMENT** |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/2/TableCell/11` | 0.419349 | 6 |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/30` | 0.411288 | **EQUIPMENT** |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/10/Text/42` | 0.411288 | **EQUIPMENT** |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/22` | 0.411288 | **EQUIPMENT** |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/12/Text/37` | 0.411288 | **EQUIPMENT** |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/2/TableCell/13` | 0.408133 | 232 |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/130` | 0.357641 | INTRODUCTION 4 |

### Query 64
- Text: What is the rule about SPELLS?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/2/TableCell/18']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/2/TableCell/18', 'PZO22001 Starfinder Player Core 001-013::/page/4/Text/31', 'PZO22001 Starfinder Player Core 001-013::/page/10/Text/43']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/2/TableCell/18` | 0.844517 | SPELLS |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/31` | 0.796446 | **SPELLS** |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/10/Text/43` | 0.796446 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/23` | 0.754446 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/8/Text/24` | 0.754446 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/12/Text/38` | 0.754446 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/2/TableCell/21` | 0.609111 | SPELL LISTSSPELLSFOCUS SPELLSRITUALS |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/10/SectionHeader/24` | 0.548505 | **Spell** |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/2/TableCell/27` | 0.397642 | RULES OVERVIEW |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/10/Text/25` | 0.389859 | Spells are magical effects created by performing mystical  incantations and gestures. Casting a spell is an activity  that usually uses two actions. Each spell specifies what it  targets, the actions |

### Query 65
- Text: What is the rule about SPELL LISTSSPELLSFOCUS SPELLSRITUALS?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/2/TableCell/21']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/2/TableCell/21', 'PZO22001 Starfinder Player Core 001-013::/page/4/Text/31', 'PZO22001 Starfinder Player Core 001-013::/page/6/Text/23']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/2/TableCell/21` | 0.904384 | SPELL LISTSSPELLSFOCUS SPELLSRITUALS |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/31` | 0.607080 | **SPELLS** |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/23` | 0.607080 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/8/Text/24` | 0.565080 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/10/Text/43` | 0.565080 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/12/Text/38` | 0.565080 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/2/TableCell/18` | 0.558341 | SPELLS |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/2/TableCell/27` | 0.441190 | RULES OVERVIEW |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/10/SectionHeader/24` | 0.429112 | **Spell** |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/2/TableOfContents/2` | 0.401912 | 6EQUIPMENT232INTRODUCTION TECH GEAR ARMOR SHIELDS WEAPONS ARMOR UPGRADES WEAPON UPGRADES PRECIOUS AMMUNITION & WEAPONS GRENADES MAGIC ITEMS AUGMENTATIONS293 298 244 250 253 268 272 278 2807SPELLS294SP |

### Query 66
- Text: What is the rule about CONDITIONS APPENDIX?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/2/TableCell/30']
- Expected found: `True`
- Expected rank: `6`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/4/Text/33', 'PZO22001 Starfinder Player Core 001-013::/page/10/Text/45', 'PZO22001 Starfinder Player Core 001-013::/page/12/Text/40']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/33` | 0.800997 | **CONDITIONS ** **APPENDIX** |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/10/Text/45` | 0.800997 | **CONDITIONS ** **APPENDIX** |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/12/Text/40` | 0.800997 | **CONDITIONS ** **APPENDIX** |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/8/Text/26` | 0.770997 | **CONDITIONS ** **APPENDIX** |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/26` | 0.580376 | **APPENDIX** |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/2/TableCell/30` | 0.566482 | CONDITIONS APPENDIX GLOSSARY & INDEX CHARACTER SHEET |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/9/Text/22` | 0.528324 | An ongoing effect that changes how a character can act,  or that alters some of their statistics, is called a condition.  The rules for the basic conditions used in the game can be  found in the Condi |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/25` | 0.482651 | **CONDITIONS ** |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/2/TableCell/27` | 0.440261 | RULES OVERVIEW |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/9/SectionHeader/21` | 0.426950 | **Condition** |

### Query 67
- Text: What is the rule about Starfinder is a science fantasy tabletop roleplaying game (RPG) where you and a group of friends  gather to play out a story of daring adventurers exploring a galaxy filled with impossible magic,  amazing technology, and fantastical alien cultures. More importantly, Starfinder is a game where your  character's choices determine how the story unfolds.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/4/Text/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/4/Text/2', 'PZO22001 Starfinder Player Core 001-013::/page/4/Text/14', 'PZO22001 Starfinder Player Core 001-013::/page/6/Text/6']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/2` | 0.976973 | Starfinder is a science fantasy tabletop roleplaying game (RPG) where you and a group of friends  gather to play out a story of daring adventurers exploring a galaxy filled with impossible magic,  ama |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/14` | 0.826564 | The first rule of Starfinder is that this game is *yours*. Use  it to tell the stories you want to tell, be the character  you want to be, and share exciting adventures with  friends. If any other rul |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/6` | 0.822793 | Characters and their choices create the story of Starfinder,  but how they interact with each other and the galaxy around  them is governed by rules. So, while you might decide that  your character st |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/8` | 0.751688 | A roleplaying game is an interactive story where one  player, the Game Master (GM), sets the scene and presents  challenges, while other players take the roles of player  characters (PCs) and attempt |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/5/Text/9` | 0.715384 | Starfinder is a game for everyone, regardless of their age,  gender, race or ethnicity, religion, sexual orientation, or any |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/11` | 0.713042 | Starfinder is played in sessions during which players gather in  person or online for a few hours to play the game. A complete  story can be as short as a single session, often referred to as  a "one- |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/17` | 0.706671 | Everyone involved in a Starfinder game is a player, including  the Game Master, but for the sake of simplicity, "player"  usually refers to participants other than the GM. Before  the game begins, pla |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/7/Text/2` | 0.701085 | In a Starfinder game, three modes of play determine the  pacing of each scene in the story. Most of your character's  time is spent in **exploration**, uncovering mysteries, solving  problems, and int |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/6` | 0.694220 | Starfinder takes place following the Gap, an era of collective  memory loss. Explore a galaxy full of magic and mystery,  from the vibrant worlds and bustling satellites of the Pact  Worlds to cosmic |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/11/Text/2` | 0.659564 | The following example is presented to give you a better idea of  how Starfinder is played. In this adventure, Thurston is the GM.  Jenny is playing Obozaya, an aggressive vesk soldier; Jessica is  pla |

### Query 68
- Text: What is the rule about Starfinder takes place following the Gap, an era of collective  memory loss. Explore a galaxy full of magic and mystery,  from the vibrant worlds and bustling satellites of the Pact  Worlds to cosmic wonders and warring civilizations in Near  Space or the distant regions of the perilous Vast. A Starfinder  character's adventures might take them to sleepless  megacities full of technological marvels, rugged alien planets  prowled by dangerous monsters, or magical installations  orbiting distant stars. Worlds of endless possibility await!?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/4/Text/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/4/Text/6', 'PZO22001 Starfinder Player Core 001-013::/page/4/Text/2', 'PZO22001 Starfinder Player Core 001-013::/page/9/Text/30']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/6` | 1.016826 | Starfinder takes place following the Gap, an era of collective  memory loss. Explore a galaxy full of magic and mystery,  from the vibrant worlds and bustling satellites of the Pact  Worlds to cosmic |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/2` | 0.779827 | Starfinder is a science fantasy tabletop roleplaying game (RPG) where you and a group of friends  gather to play out a story of daring adventurers exploring a galaxy filled with impossible magic,  ama |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/9/Text/30` | 0.744256 | Starfinder is set in the Pact Worlds, a system of allied  planets that was once home to the lost world Golarion,  though many adventures explore the wider galaxy.  More information about the galaxy ca |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/6` | 0.701965 | Characters and their choices create the story of Starfinder,  but how they interact with each other and the galaxy around  them is governed by rules. So, while you might decide that  your character st |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/7/Text/2` | 0.679291 | In a Starfinder game, three modes of play determine the  pacing of each scene in the story. Most of your character's  time is spent in **exploration**, uncovering mysteries, solving  problems, and int |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/14` | 0.625504 | The first rule of Starfinder is that this game is *yours*. Use  it to tell the stories you want to tell, be the character  you want to be, and share exciting adventures with  friends. If any other rul |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/5/Text/9` | 0.620855 | Starfinder is a game for everyone, regardless of their age,  gender, race or ethnicity, religion, sexual orientation, or any |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/11` | 0.609511 | Starfinder is played in sessions during which players gather in  person or online for a few hours to play the game. A complete  story can be as short as a single session, often referred to as  a "one- |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/9` | 0.608956 | Aside from characters and monsters, the galaxy of  Starfinder itself can be a force at the table and in the  narrative. While the presence of the larger setting  can sometimes be an obvious hazard, su |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/8` | 0.601698 | A roleplaying game is an interactive story where one  player, the Game Master (GM), sets the scene and presents  challenges, while other players take the roles of player  characters (PCs) and attempt |

### Query 69
- Text: What is the rule about A roleplaying game is an interactive story where one  player, the Game Master (GM), sets the scene and presents  challenges, while other players take the roles of player  characters (PCs) and attempt to overcome those challenges.  Danger comes in the form of monsters, hostile tech, and alien  environments, but Starfinder conflicts also involve political  schemes, puzzles, interpersonal drama, and more.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/4/Text/8']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/4/Text/8', 'PZO22001 Starfinder Player Core 001-013::/page/4/Text/17', 'PZO22001 Starfinder Player Core 001-013::/page/5/Text/4']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/8` | 0.986774 | A roleplaying game is an interactive story where one  player, the Game Master (GM), sets the scene and presents  challenges, while other players take the roles of player  characters (PCs) and attempt |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/17` | 0.791037 | Everyone involved in a Starfinder game is a player, including  the Game Master, but for the sake of simplicity, "player"  usually refers to participants other than the GM. Before  the game begins, pla |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/5/Text/4` | 0.785439 | While the other players create and control their characters,  the Game Master (or GM) is in charge of the story and setting.  The GM describes all the situations the player characters  experience in a |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/2` | 0.723401 | Starfinder is a science fantasy tabletop roleplaying game (RPG) where you and a group of friends  gather to play out a story of daring adventurers exploring a galaxy filled with impossible magic,  ama |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/5/Text/21` | 0.721932 | In Starfinder, the players take on the role of **player characters ** **(PCs)**, while the Game Master portrays **nonplayer characters ** **(NPCs)** and **monsters**. While PCs and NPCs are both impor |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/9/Text/28` | 0.720582 | The Game Master is the player who adjudicates the rules  and narrates the various elements of the Starfinder story  and world that the other players explore. The GM uses the  rules found in *Starfinde |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/14` | 0.690707 | The first rule of Starfinder is that this game is *yours*. Use  it to tell the stories you want to tell, be the character  you want to be, and share exciting adventures with  friends. If any other rul |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/6` | 0.688043 | Characters and their choices create the story of Starfinder,  but how they interact with each other and the galaxy around  them is governed by rules. So, while you might decide that  your character st |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/11` | 0.674563 | Starfinder is played in sessions during which players gather in  person or online for a few hours to play the game. A complete  story can be as short as a single session, often referred to as  a "one- |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/7/Text/2` | 0.661571 | In a Starfinder game, three modes of play determine the  pacing of each scene in the story. Most of your character's  time is spent in **exploration**, uncovering mysteries, solving  problems, and int |

### Query 70
- Text: What is the rule about The game is typically played in a group of four to seven  players, with one of those players serving as the group's GM.  The GM prepares, presents, and presides over the game's  setting and story, posing challenges and playing adversaries,  allies, and bystanders alike. As each scene flows, every player  contributes to the story, responding to situations according  to the personality and abilities of their character. Combined  with preassigned statistics, dice rolls add an element of  chance to the game and determine whether characters  succeed or fail at actions.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/4/Text/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/4/Text/9', 'PZO22001 Starfinder Player Core 001-013::/page/4/Text/18', 'PZO22001 Starfinder Player Core 001-013::/page/6/Text/7']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/9` | 1.004965 | The game is typically played in a group of four to seven  players, with one of those players serving as the group's GM.  The GM prepares, presents, and presides over the game's  setting and story, pos |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/18` | 0.756041 | During the game, players describe the actions their  characters take and roll dice, using their characters' abilities.  The GM resolves the outcome of these actions. Some players  enjoy acting out (or |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/7` | 0.748786 | The GM determines the premise  and background of most adventures,  although character histories and  personalities should also play a part.  Once a game session begins, the players |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/8/Text/5` | 0.670040 | While exploration is handled in a free-form manner,  encounters are more structured. The players and GM  roll **initiative** to determine who acts in what order. The  encounter occurs over a number of |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/10` | 0.666887 | take turns describing what their characters attempt to  do, while the GM determines the outcome, with everyone  working together to create the story. The GM also describes  the environment, other char |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/5/Text/4` | 0.650589 | While the other players create and control their characters,  the Game Master (or GM) is in charge of the story and setting.  The GM describes all the situations the player characters  experience in a |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/8` | 0.646188 | A roleplaying game is an interactive story where one  player, the Game Master (GM), sets the scene and presents  challenges, while other players take the roles of player  characters (PCs) and attempt |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/17` | 0.643933 | Everyone involved in a Starfinder game is a player, including  the Game Master, but for the sake of simplicity, "player"  usually refers to participants other than the GM. Before  the game begins, pla |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/7/Text/7` | 0.634530 | Checks like this are the heart of the game and are rolled all  the time, in every mode of play, to determine the outcome of  tasks. While the roll of the die is essential, the statistic you  add to th |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/5/Text/5` | 0.623161 | The GM can create a new adventure—crafting a narrative,  selecting monsters, and assigning rewards on their own or they can instead rely on a published adventure, using  it as a basis for the session |

### Query 71
- Text: What is the rule about A session can be mostly action, featuring battles with  ferocious monsters, hacking computer terminals and magitech  traps, and the completion of heroic missions. Alternatively,?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/4/Text/12']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/4/Text/12', 'PZO22001 Starfinder Player Core 001-013::/page/8/Text/5', 'PZO22001 Starfinder Player Core 001-013::/page/6/Text/7']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/12` | 0.961544 | A session can be mostly action, featuring battles with  ferocious monsters, hacking computer terminals and magitech  traps, and the completion of heroic missions. Alternatively, |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/8/Text/5` | 0.660778 | While exploration is handled in a free-form manner,  encounters are more structured. The players and GM  roll **initiative** to determine who acts in what order. The  encounter occurs over a number of |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/7` | 0.592733 | The GM determines the premise  and background of most adventures,  although character histories and  personalities should also play a part.  Once a game session begins, the players |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/15` | 0.550542 | it could include unionizing miners on an asteroid teeming  with megafauna, infiltrating a galactic empire's military, or  bargaining with enigmatic spectras for a starship's speedy  passage through th |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/5/Text/5` | 0.543732 | The GM can create a new adventure—crafting a narrative,  selecting monsters, and assigning rewards on their own or they can instead rely on a published adventure, using  it as a basis for the session |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/8/Text/4` | 0.527288 | During your adventures, there will be times when a simple  skill check is not enough to resolve a challenge—when  vicious monsters or ruthless enemies attack your character  and the only choice is to |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/7/Text/11` | 0.526906 | Most of the time, your character will  explore an environment, interact with  other characters, travel from place  to place, and overcome challenges.  This is called exploration. Gameplay  is relative |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/11` | 0.507729 | Starfinder is played in sessions during which players gather in  person or online for a few hours to play the game. A complete  story can be as short as a single session, often referred to as  a "one- |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/8` | 0.503830 | A roleplaying game is an interactive story where one  player, the Game Master (GM), sets the scene and presents  challenges, while other players take the roles of player  characters (PCs) and attempt |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/19` | 0.500564 | If this is your first experience with a roleplaying game,  it's recommended that you take on the role of a player to  familiarize yourself with the rules and the galaxy. |

### Query 72
- Text: What is the rule about The first rule of Starfinder is that this game is *yours*. Use  it to tell the stories you want to tell, be the character  you want to be, and share exciting adventures with  friends. If any other rule gets in the way of your fun,  you can alter or ignore it to fit your story as long as  your group agrees. The true goal of Starfinder is for  everyone to enjoy themselves.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/4/Text/14']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/4/Text/14', 'PZO22001 Starfinder Player Core 001-013::/page/6/Text/6', 'PZO22001 Starfinder Player Core 001-013::/page/4/Text/17']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/14` | 1.025683 | The first rule of Starfinder is that this game is *yours*. Use  it to tell the stories you want to tell, be the character  you want to be, and share exciting adventures with  friends. If any other rul |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/6` | 0.775637 | Characters and their choices create the story of Starfinder,  but how they interact with each other and the galaxy around  them is governed by rules. So, while you might decide that  your character st |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/17` | 0.747860 | Everyone involved in a Starfinder game is a player, including  the Game Master, but for the sake of simplicity, "player"  usually refers to participants other than the GM. Before  the game begins, pla |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/2` | 0.680844 | Starfinder is a science fantasy tabletop roleplaying game (RPG) where you and a group of friends  gather to play out a story of daring adventurers exploring a galaxy filled with impossible magic,  ama |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/5/Text/9` | 0.678988 | Starfinder is a game for everyone, regardless of their age,  gender, race or ethnicity, religion, sexual orientation, or any |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/11` | 0.644123 | Starfinder is played in sessions during which players gather in  person or online for a few hours to play the game. A complete  story can be as short as a single session, often referred to as  a "one- |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/7/Text/2` | 0.627349 | In a Starfinder game, three modes of play determine the  pacing of each scene in the story. Most of your character's  time is spent in **exploration**, uncovering mysteries, solving  problems, and int |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/8` | 0.616818 | A roleplaying game is an interactive story where one  player, the Game Master (GM), sets the scene and presents  challenges, while other players take the roles of player  characters (PCs) and attempt |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/5/Text/4` | 0.616451 | While the other players create and control their characters,  the Game Master (or GM) is in charge of the story and setting.  The GM describes all the situations the player characters  experience in a |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/9/Text/28` | 0.614703 | The Game Master is the player who adjudicates the rules  and narrates the various elements of the Starfinder story  and world that the other players explore. The GM uses the  rules found in *Starfinde |

### Query 73
- Text: What is the rule about it could include unionizing miners on an asteroid teeming  with megafauna, infiltrating a galactic empire's military, or  bargaining with enigmatic spectras for a starship's speedy  passage through the Drift. Ultimately, it's up to you and your  group to determine what kind of game you're playing, from  exploration of uncharted space to an intergalactic political  drama, or anything in between.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/4/Text/15']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/4/Text/15', 'PZO22001 Starfinder Player Core 001-013::/page/6/Text/6', 'PZO22001 Starfinder Player Core 001-013::/page/7/Text/2']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/15` | 0.994285 | it could include unionizing miners on an asteroid teeming  with megafauna, infiltrating a galactic empire's military, or  bargaining with enigmatic spectras for a starship's speedy  passage through th |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/6` | 0.655698 | Characters and their choices create the story of Starfinder,  but how they interact with each other and the galaxy around  them is governed by rules. So, while you might decide that  your character st |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/7/Text/2` | 0.642349 | In a Starfinder game, three modes of play determine the  pacing of each scene in the story. Most of your character's  time is spent in **exploration**, uncovering mysteries, solving  problems, and int |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/8/Text/5` | 0.581078 | While exploration is handled in a free-form manner,  encounters are more structured. The players and GM  roll **initiative** to determine who acts in what order. The  encounter occurs over a number of |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/11/Text/2` | 0.575260 | The following example is presented to give you a better idea of  how Starfinder is played. In this adventure, Thurston is the GM.  Jenny is playing Obozaya, an aggressive vesk soldier; Jessica is  pla |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/19` | 0.575090 | If this is your first experience with a roleplaying game,  it's recommended that you take on the role of a player to  familiarize yourself with the rules and the galaxy. |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/14` | 0.565805 | The first rule of Starfinder is that this game is *yours*. Use  it to tell the stories you want to tell, be the character  you want to be, and share exciting adventures with  friends. If any other rul |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/7/Text/11` | 0.563708 | Most of the time, your character will  explore an environment, interact with  other characters, travel from place  to place, and overcome challenges.  This is called exploration. Gameplay  is relative |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/2` | 0.558377 | Starfinder is a science fantasy tabletop roleplaying game (RPG) where you and a group of friends  gather to play out a story of daring adventurers exploring a galaxy filled with impossible magic,  ama |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/8` | 0.546104 | A roleplaying game is an interactive story where one  player, the Game Master (GM), sets the scene and presents  challenges, while other players take the roles of player  characters (PCs) and attempt |

### Query 74
- Text: What is the rule about Everyone involved in a Starfinder game is a player, including  the Game Master, but for the sake of simplicity, "player"  usually refers to participants other than the GM. Before  the game begins, players invent a history and personality  for their characters, using the rules to determine their  characters' statistics, abilities, strengths, and weaknesses.  The GM might limit the options available to the players during  character creation, but these restrictions should be discussed  ahead of time so everyone can create interesting heroes. In  general, the only limits to character concepts are the players'  imaginations and the GM's guidelines.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/4/Text/17']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/4/Text/17', 'PZO22001 Starfinder Player Core 001-013::/page/5/Text/4', 'PZO22001 Starfinder Player Core 001-013::/page/9/Text/28']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/17` | 1.017463 | Everyone involved in a Starfinder game is a player, including  the Game Master, but for the sake of simplicity, "player"  usually refers to participants other than the GM. Before  the game begins, pla |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/5/Text/4` | 0.803549 | While the other players create and control their characters,  the Game Master (or GM) is in charge of the story and setting.  The GM describes all the situations the player characters  experience in a |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/9/Text/28` | 0.764494 | The Game Master is the player who adjudicates the rules  and narrates the various elements of the Starfinder story  and world that the other players explore. The GM uses the  rules found in *Starfinde |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/5/Text/21` | 0.697831 | In Starfinder, the players take on the role of **player characters ** **(PCs)**, while the Game Master portrays **nonplayer characters ** **(NPCs)** and **monsters**. While PCs and NPCs are both impor |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/14` | 0.696757 | The first rule of Starfinder is that this game is *yours*. Use  it to tell the stories you want to tell, be the character  you want to be, and share exciting adventures with  friends. If any other rul |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/8` | 0.696373 | A roleplaying game is an interactive story where one  player, the Game Master (GM), sets the scene and presents  challenges, while other players take the roles of player  characters (PCs) and attempt |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/6` | 0.693371 | Characters and their choices create the story of Starfinder,  but how they interact with each other and the galaxy around  them is governed by rules. So, while you might decide that  your character st |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/11` | 0.641649 | Starfinder is played in sessions during which players gather in  person or online for a few hours to play the game. A complete  story can be as short as a single session, often referred to as  a "one- |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/7` | 0.631663 | The GM determines the premise  and background of most adventures,  although character histories and  personalities should also play a part.  Once a game session begins, the players |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/2` | 0.606166 | Starfinder is a science fantasy tabletop roleplaying game (RPG) where you and a group of friends  gather to play out a story of daring adventurers exploring a galaxy filled with impossible magic,  ama |

### Query 75
- Text: What is the rule about During the game, players describe the actions their  characters take and roll dice, using their characters' abilities.  The GM resolves the outcome of these actions. Some players  enjoy acting out (or roleplaying) what they do as if they  were their characters, while others describe their characters'  actions as if they were telling a story. Do whatever feels best!?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/4/Text/18']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/4/Text/18', 'PZO22001 Starfinder Player Core 001-013::/page/10/Text/14', 'PZO22001 Starfinder Player Core 001-013::/page/4/Text/9']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/18` | 0.987820 | During the game, players describe the actions their  characters take and roll dice, using their characters' abilities.  The GM resolves the outcome of these actions. Some players  enjoy acting out (or |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/10/Text/14` | 0.748030 | Describing a character's actions, often while acting from the  perspective of the character, is called roleplaying. When a  player speaks or describes action from the perspective of a  character, they |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/9` | 0.703497 | The game is typically played in a group of four to seven  players, with one of those players serving as the group's GM.  The GM prepares, presents, and presides over the game's  setting and story, pos |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/8/Text/5` | 0.624384 | While exploration is handled in a free-form manner,  encounters are more structured. The players and GM  roll **initiative** to determine who acts in what order. The  encounter occurs over a number of |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/5/Text/4` | 0.601820 | While the other players create and control their characters,  the Game Master (or GM) is in charge of the story and setting.  The GM describes all the situations the player characters  experience in a |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/8/Text/2` | 0.599488 | Throughout this mode of play, the GM asks the players  what their characters are doing as they explore. This is  important in case a conflict arises. If combat breaks out, the  tasks the PCs undertook |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/7` | 0.594673 | The GM determines the premise  and background of most adventures,  although character histories and  personalities should also play a part.  Once a game session begins, the players |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/10` | 0.594022 | take turns describing what their characters attempt to  do, while the GM determines the outcome, with everyone  working together to create the story. The GM also describes  the environment, other char |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/17` | 0.587294 | Everyone involved in a Starfinder game is a player, including  the Game Master, but for the sake of simplicity, "player"  usually refers to participants other than the GM. Before  the game begins, pla |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/3` | 0.579072 | Your player character is also defined by some key choices  you make. The first choice is a PC's **ancestry**, representing the  character's parents and heritage, such as barathu, human, or  vesk. Next |

### Query 76
- Text: What is the rule about **Character ** **Creation**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/4/Text/22']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/4/Text/22', 'PZO22001 Starfinder Player Core 001-013::/page/6/Text/14', 'PZO22001 Starfinder Player Core 001-013::/page/12/Text/30']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/22` | 0.851651 | **Character ** **Creation** |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/14` | 0.851651 | **Character ** **Creation** |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/12/Text/30` | 0.851651 | **Character ** **Creation** |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/10/Text/34` | 0.809651 | **Character ** **Creation** |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/8/Text/15` | 0.809651 | **Character ** **Creation** |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/10/Text/8` | 0.556785 | This is a character created and controlled by a player. |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/17` | 0.515524 | Everyone involved in a Starfinder game is a player, including  the Game Master, but for the sake of simplicity, "player"  usually refers to participants other than the GM. Before  the game begins, pla |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/9/Text/2` | 0.508207 | There are a number of important terms that you'll need to know as you create your first character or adventure. Some of  the most important terms mentioned on previous pages are also included here for |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/4` | 0.506902 | In addition to these key choices, PCs also have a number of  **feats**—individual abilities selected during character creation  and as the character increases in level. Every feat has a type  to denot |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/132` | 0.506528 | CHARACTER CREATION17 |

### Query 77
- Text: What is the rule about **ANCESTRIES & ** **BACKGROUNDS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/4/Text/26']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/4/Text/26', 'PZO22001 Starfinder Player Core 001-013::/page/12/Text/33', 'PZO22001 Starfinder Player Core 001-013::/page/10/Text/38']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/26` | 0.920820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/12/Text/33` | 0.920820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/10/Text/38` | 0.920820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/8/Text/19` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/18` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/140` | 0.695806 | ANCESTRIES & BACKGROUNDS 40 |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/9/SectionHeader/13` | 0.474264 | **Background** |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/9/Text/6` | 0.471205 | An ancestry is the broad family of people that a character  belongs to. Ancestry determines a character's starting Hit  Points, languages, senses, and Speed, and it grants access  to ancestry feats. A |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/2/TableCell/27` | 0.455103 | RULES OVERVIEW |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/164` | 0.432404 | BACKGROUNDS92 |

### Query 78
- Text: What is the rule about **SKILLS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/4/Text/28']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/8/Text/21', 'PZO22001 Starfinder Player Core 001-013::/page/6/Text/20', 'PZO22001 Starfinder Player Core 001-013::/page/4/Text/28']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/8/Text/21` | 0.864442 | **SKILLS** |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/20` | 0.864442 | **SKILLS** |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/28` | 0.864442 | **SKILLS** |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/12/Text/35` | 0.822442 | **SKILLS** |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/10/Text/40` | 0.822442 | **SKILLS** |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/10/SectionHeader/20` | 0.650605 | **Skill** |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/10/Text/21` | 0.579699 | A skill represents a creature's ability to perform certain  tasks that require instruction or practice. All characters are  trained in certain skills due to their background and class.  Skills are ful |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/184` | 0.527317 | SKILLS TABLE |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/188` | 0.479252 | SKILLS 192 |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/2/TableCell/27` | 0.466402 | RULES OVERVIEW |

### Query 79
- Text: What is the rule about **FEATS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/4/Text/29']
- Expected found: `True`
- Expected rank: `5`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/8/Text/22', 'PZO22001 Starfinder Player Core 001-013::/page/12/Text/36', 'PZO22001 Starfinder Player Core 001-013::/page/10/Text/41']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/8/Text/22` | 0.871817 | **FEATS** |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/12/Text/36` | 0.871817 | **FEATS** |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/10/Text/41` | 0.871817 | **FEATS** |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/21` | 0.829817 | **FEATS** |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/29` | 0.829817 | **FEATS** |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/9/SectionHeader/25` | 0.587965 | **Feat** |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/190` | 0.532763 | FEATS 210 |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/9/Text/26` | 0.519225 | A feat is an ability you can select for your character due  to their ancestry, background, class, general training, or  skill training. Some feats grant the ability to use special  actions, while othe |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/1/TableCell/192` | 0.424040 | FEATS TABLE211 |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/4` | 0.383687 | In addition to these key choices, PCs also have a number of  **feats**—individual abilities selected during character creation  and as the character increases in level. Every feat has a type  to denot |

### Query 80
- Text: What is the rule about **SPELLS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/4/Text/31']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/4/Text/31', 'PZO22001 Starfinder Player Core 001-013::/page/12/Text/38', 'PZO22001 Starfinder Player Core 001-013::/page/10/Text/43']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/31` | 0.889304 | **SPELLS** |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/12/Text/38` | 0.889304 | **SPELLS** |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/10/Text/43` | 0.889304 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/8/Text/24` | 0.847304 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/23` | 0.847304 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/2/TableCell/18` | 0.776591 | SPELLS |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/2/TableCell/21` | 0.614070 | SPELL LISTSSPELLSFOCUS SPELLSRITUALS |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/10/SectionHeader/24` | 0.606471 | **Spell** |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/2/TableCell/27` | 0.399582 | RULES OVERVIEW |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/10/Text/25` | 0.395790 | Spells are magical effects created by performing mystical  incantations and gestures. Casting a spell is an activity  that usually uses two actions. Each spell specifies what it  targets, the actions |

### Query 81
- Text: What is the rule about Starfinder requires a set of polyhedral dice. Each die  has a different number of sides—four, six, eight, or  more. When these dice are mentioned in the text,  they're indicated by a "d" followed by the number of  sides on the die. Starfinder uses 4-sided dice (or d4),  6-sided dice (d6), 8-sided dice (d8), 10-sided dice  (d10), 12-sided dice (d12), and 20-sided dice (d20). If  you need to roll multiple dice, a number before the "d"  tells you how many. For example, "4d6" means you  should roll four dice, all 6-sided. If a rule asks for d%,  you generate a number from 1 to 100 by rolling two  10-sided dice, treating one as the tens place and the  other as the ones place.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/5/Text/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/5/Text/2', 'PZO22001 Starfinder Player Core 001-013::/page/5/Text/14', 'PZO22001 Starfinder Player Core 001-013::/page/6/Text/6']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/5/Text/2` | 1.000798 | Starfinder requires a set of polyhedral dice. Each die  has a different number of sides—four, six, eight, or  more. When these dice are mentioned in the text,  they're indicated by a "d" followed by t |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/5/Text/14` | 0.705357 | **Dice:** The players and GM need at least one set of  polyhedral dice, although most participants bring their own.  Six-sided dice are quite common, but all the dice in the set  can be found at hobby |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/6` | 0.603596 | Characters and their choices create the story of Starfinder,  but how they interact with each other and the galaxy around  them is governed by rules. So, while you might decide that  your character st |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/14` | 0.486121 | The first rule of Starfinder is that this game is *yours*. Use  it to tell the stories you want to tell, be the character  you want to be, and share exciting adventures with  friends. If any other rul |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/11/Text/2` | 0.483478 | The following example is presented to give you a better idea of  how Starfinder is played. In this adventure, Thurston is the GM.  Jenny is playing Obozaya, an aggressive vesk soldier; Jessica is  pla |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/7/Text/2` | 0.483347 | In a Starfinder game, three modes of play determine the  pacing of each scene in the story. Most of your character's  time is spent in **exploration**, uncovering mysteries, solving  problems, and int |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/7/Text/7` | 0.477117 | Checks like this are the heart of the game and are rolled all  the time, in every mode of play, to determine the outcome of  tasks. While the roll of the die is essential, the statistic you  add to th |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/7/Text/3` | 0.474217 | During the game, your character will face situations where  the outcome is uncertain. A character might need to navigate  while inside the Drift, survive in an alien desert, or sneak past  a corporate |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/7/Text/6` | 0.469618 | For example, while aboard a starship traveling to a faraway  world, your character might find a faster route through an  uncharted asteroid field. You decide to go for it, but the GM  declares this a |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/2` | 0.469037 | Starfinder is a science fantasy tabletop roleplaying game (RPG) where you and a group of friends  gather to play out a story of daring adventurers exploring a galaxy filled with impossible magic,  ama |

### Query 82
- Text: What is the rule about While the other players create and control their characters,  the Game Master (or GM) is in charge of the story and setting.  The GM describes all the situations the player characters  experience in an adventure, considers how the actions of  player characters affect the story, and interprets the rules  along the way. The Game Master uses the rules and advice  found in *Starfinder GM Core*.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/5/Text/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/5/Text/4', 'PZO22001 Starfinder Player Core 001-013::/page/9/Text/28', 'PZO22001 Starfinder Player Core 001-013::/page/4/Text/17']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/5/Text/4` | 1.003068 | While the other players create and control their characters,  the Game Master (or GM) is in charge of the story and setting.  The GM describes all the situations the player characters  experience in a |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/9/Text/28` | 0.935700 | The Game Master is the player who adjudicates the rules  and narrates the various elements of the Starfinder story  and world that the other players explore. The GM uses the  rules found in *Starfinde |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/17` | 0.839712 | Everyone involved in a Starfinder game is a player, including  the Game Master, but for the sake of simplicity, "player"  usually refers to participants other than the GM. Before  the game begins, pla |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/8` | 0.736812 | A roleplaying game is an interactive story where one  player, the Game Master (GM), sets the scene and presents  challenges, while other players take the roles of player  characters (PCs) and attempt |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/7` | 0.708235 | The GM determines the premise  and background of most adventures,  although character histories and  personalities should also play a part.  Once a game session begins, the players |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/5/Text/21` | 0.701424 | In Starfinder, the players take on the role of **player characters ** **(PCs)**, while the Game Master portrays **nonplayer characters ** **(NPCs)** and **monsters**. While PCs and NPCs are both impor |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/14` | 0.665755 | The first rule of Starfinder is that this game is *yours*. Use  it to tell the stories you want to tell, be the character  you want to be, and share exciting adventures with  friends. If any other rul |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/6` | 0.659322 | Characters and their choices create the story of Starfinder,  but how they interact with each other and the galaxy around  them is governed by rules. So, while you might decide that  your character st |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/9` | 0.654021 | The game is typically played in a group of four to seven  players, with one of those players serving as the group's GM.  The GM prepares, presents, and presides over the game's  setting and story, pos |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/5/Text/5` | 0.653155 | The GM can create a new adventure—crafting a narrative,  selecting monsters, and assigning rewards on their own or they can instead rely on a published adventure, using  it as a basis for the session |

### Query 83
- Text: What is the rule about The GM can create a new adventure—crafting a narrative,  selecting monsters, and assigning rewards on their own or they can instead rely on a published adventure, using  it as a basis for the session and modifying it as needed to  accommodate their individual players and the group's style  of play. Some GMs run games that combine original and  published content, mixing both together to form a new story.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/5/Text/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/5/Text/5', 'PZO22001 Starfinder Player Core 001-013::/page/6/Text/7', 'PZO22001 Starfinder Player Core 001-013::/page/5/Text/4']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/5/Text/5` | 0.987002 | The GM can create a new adventure—crafting a narrative,  selecting monsters, and assigning rewards on their own or they can instead rely on a published adventure, using  it as a basis for the session |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/7` | 0.729803 | The GM determines the premise  and background of most adventures,  although character histories and  personalities should also play a part.  Once a game session begins, the players |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/5/Text/4` | 0.659402 | While the other players create and control their characters,  the Game Master (or GM) is in charge of the story and setting.  The GM describes all the situations the player characters  experience in a |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/10` | 0.600586 | take turns describing what their characters attempt to  do, while the GM determines the outcome, with everyone  working together to create the story. The GM also describes  the environment, other char |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/11` | 0.600229 | A single narrative—including the setup, plot, and  conclusion—is called an **adventure**. A series of adventures  creates an even larger narrative called a **campaign**. An  adventure might take sever |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/5/Text/6` | 0.582907 | Being the GM is a challenge, requiring you to adjudicate  the rules, narrate the story, and juggle other responsibilities.  But it can also be very rewarding and worth all the work  required to run a |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/9` | 0.577738 | The game is typically played in a group of four to seven  players, with one of those players serving as the group's GM.  The GM prepares, presents, and presides over the game's  setting and story, pos |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/5/Text/15` | 0.571088 | **Adventure:** Every group needs an adventure to play,  whether it's designed by the GM or found in a published  resource. You can find a variety of exciting adventures and  even entire Adventure Path |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/18` | 0.566391 | During the game, players describe the actions their  characters take and roll dice, using their characters' abilities.  The GM resolves the outcome of these actions. Some players  enjoy acting out (or |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/7/Text/11` | 0.562559 | Most of the time, your character will  explore an environment, interact with  other characters, travel from place  to place, and overcome challenges.  This is called exploration. Gameplay  is relative |

### Query 84
- Text: What is the rule about Being the GM is a challenge, requiring you to adjudicate  the rules, narrate the story, and juggle other responsibilities.  But it can also be very rewarding and worth all the work  required to run a good game. If it's your first time running  a game, remember that the only thing that matters is that  everyone, including you, has a fun time. Everything else will  come naturally with practice and patience.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/5/Text/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/5/Text/6', 'PZO22001 Starfinder Player Core 001-013::/page/5/Text/10', 'PZO22001 Starfinder Player Core 001-013::/page/5/Text/8']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/5/Text/6` | 0.995239 | Being the GM is a challenge, requiring you to adjudicate  the rules, narrate the story, and juggle other responsibilities.  But it can also be very rewarding and worth all the work  required to run a |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/5/Text/10` | 0.765091 | other identities and life experiences. It's the responsibility of  all of the players, not just the GM, to make sure the game is  fun and welcoming for everyone. |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/5/Text/8` | 0.680792 | Whether you're the GM or a player, participating in a tabletop  roleplaying game includes a social contract: everyone's  gathered together to have fun. For many, roleplaying is a  way to escape the tr |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/19` | 0.633020 | If this is your first experience with a roleplaying game,  it's recommended that you take on the role of a player to  familiarize yourself with the rules and the galaxy. |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/7` | 0.615388 | The GM determines the premise  and background of most adventures,  although character histories and  personalities should also play a part.  Once a game session begins, the players |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/9` | 0.609370 | The game is typically played in a group of four to seven  players, with one of those players serving as the group's GM.  The GM prepares, presents, and presides over the game's  setting and story, pos |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/5/Text/19` | 0.606482 | Before creating your first character or adventure, you should  understand a number of basic concepts used in the game.  New concepts are presented in bold to make them easy to  find, but this chapter |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/5/Text/5` | 0.600449 | The GM can create a new adventure—crafting a narrative,  selecting monsters, and assigning rewards on their own or they can instead rely on a published adventure, using  it as a basis for the session |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/5/Text/4` | 0.583375 | While the other players create and control their characters,  the Game Master (or GM) is in charge of the story and setting.  The GM describes all the situations the player characters  experience in a |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/14` | 0.573933 | The first rule of Starfinder is that this game is *yours*. Use  it to tell the stories you want to tell, be the character  you want to be, and share exciting adventures with  friends. If any other rul |

### Query 85
- Text: What is the rule about Whether you're the GM or a player, participating in a tabletop  roleplaying game includes a social contract: everyone's  gathered together to have fun. For many, roleplaying is a  way to escape the troubles of everyday life. Be mindful of  everyone at the table and what they want out of the game;  when a group gathers for the first time, they should talk  about what they hope to experience at the table, as well as  any topics they'd like to avoid. Everyone should understand  that elements might come up that make some players feel  uncomfortable or even unwelcome, and everyone should  agree to respect those boundaries during play. That way,  everyone can enjoy the game together.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/5/Text/8']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/5/Text/8', 'PZO22001 Starfinder Player Core 001-013::/page/5/Text/10', 'PZO22001 Starfinder Player Core 001-013::/page/4/Text/19']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/5/Text/8` | 1.014950 | Whether you're the GM or a player, participating in a tabletop  roleplaying game includes a social contract: everyone's  gathered together to have fun. For many, roleplaying is a  way to escape the tr |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/5/Text/10` | 0.721171 | other identities and life experiences. It's the responsibility of  all of the players, not just the GM, to make sure the game is  fun and welcoming for everyone. |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/19` | 0.699675 | If this is your first experience with a roleplaying game,  it's recommended that you take on the role of a player to  familiarize yourself with the rules and the galaxy. |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/5/Text/6` | 0.642697 | Being the GM is a challenge, requiring you to adjudicate  the rules, narrate the story, and juggle other responsibilities.  But it can also be very rewarding and worth all the work  required to run a |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/14` | 0.592037 | The first rule of Starfinder is that this game is *yours*. Use  it to tell the stories you want to tell, be the character  you want to be, and share exciting adventures with  friends. If any other rul |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/8/Text/5` | 0.579839 | While exploration is handled in a free-form manner,  encounters are more structured. The players and GM  roll **initiative** to determine who acts in what order. The  encounter occurs over a number of |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/9` | 0.577511 | The game is typically played in a group of four to seven  players, with one of those players serving as the group's GM.  The GM prepares, presents, and presides over the game's  setting and story, pos |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/18` | 0.575071 | During the game, players describe the actions their  characters take and roll dice, using their characters' abilities.  The GM resolves the outcome of these actions. Some players  enjoy acting out (or |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/8` | 0.574010 | A roleplaying game is an interactive story where one  player, the Game Master (GM), sets the scene and presents  challenges, while other players take the roles of player  characters (PCs) and attempt |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/5/Text/19` | 0.572725 | Before creating your first character or adventure, you should  understand a number of basic concepts used in the game.  New concepts are presented in bold to make them easy to  find, but this chapter |

### Query 86
- Text: What is the rule about Starfinder is a game for everyone, regardless of their age,  gender, race or ethnicity, religion, sexual orientation, or any?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/5/Text/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/5/Text/9', 'PZO22001 Starfinder Player Core 001-013::/page/4/Text/14', 'PZO22001 Starfinder Player Core 001-013::/page/4/Text/17']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/5/Text/9` | 0.939754 | Starfinder is a game for everyone, regardless of their age,  gender, race or ethnicity, religion, sexual orientation, or any |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/14` | 0.783584 | The first rule of Starfinder is that this game is *yours*. Use  it to tell the stories you want to tell, be the character  you want to be, and share exciting adventures with  friends. If any other rul |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/17` | 0.717245 | Everyone involved in a Starfinder game is a player, including  the Game Master, but for the sake of simplicity, "player"  usually refers to participants other than the GM. Before  the game begins, pla |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/2` | 0.635501 | Starfinder is a science fantasy tabletop roleplaying game (RPG) where you and a group of friends  gather to play out a story of daring adventurers exploring a galaxy filled with impossible magic,  ama |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/6` | 0.626345 | Characters and their choices create the story of Starfinder,  but how they interact with each other and the galaxy around  them is governed by rules. So, while you might decide that  your character st |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/11` | 0.582663 | Starfinder is played in sessions during which players gather in  person or online for a few hours to play the game. A complete  story can be as short as a single session, often referred to as  a "one- |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/1/Text/25` | 0.571067 | To everyone who participated in the Starfinder open playtest |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/8` | 0.566426 | A roleplaying game is an interactive story where one  player, the Game Master (GM), sets the scene and presents  challenges, while other players take the roles of player  characters (PCs) and attempt |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/5/Text/10` | 0.565420 | other identities and life experiences. It's the responsibility of  all of the players, not just the GM, to make sure the game is  fun and welcoming for everyone. |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/7/Text/2` | 0.554528 | In a Starfinder game, three modes of play determine the  pacing of each scene in the story. Most of your character's  time is spent in **exploration**, uncovering mysteries, solving  problems, and int |

### Query 87
- Text: What is the rule about **Character Sheet:** Each player needs a character sheet to  create their character and to record what happens to them  during play. You can find a character sheet in the back of this  book and online as a free PDF.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/5/Text/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/5/Text/13', 'PZO22001 Starfinder Player Core 001-013::/page/5/Text/19', 'PZO22001 Starfinder Player Core 001-013::/page/9/Text/2']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/5/Text/13` | 0.969031 | **Character Sheet:** Each player needs a character sheet to  create their character and to record what happens to them  during play. You can find a character sheet in the back of this  book and online |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/5/Text/19` | 0.616216 | Before creating your first character or adventure, you should  understand a number of basic concepts used in the game.  New concepts are presented in bold to make them easy to  find, but this chapter |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/9/Text/2` | 0.592102 | There are a number of important terms that you'll need to know as you create your first character or adventure. Some of  the most important terms mentioned on previous pages are also included here for |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/9/Text/22` | 0.538083 | An ongoing effect that changes how a character can act,  or that alters some of their statistics, is called a condition.  The rules for the basic conditions used in the game can be  found in the Condi |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/5/Text/14` | 0.523968 | **Dice:** The players and GM need at least one set of  polyhedral dice, although most participants bring their own.  Six-sided dice are quite common, but all the dice in the set  can be found at hobby |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/4` | 0.523514 | In addition to these key choices, PCs also have a number of  **feats**—individual abilities selected during character creation  and as the character increases in level. Every feat has a type  to denot |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/17` | 0.520460 | Everyone involved in a Starfinder game is a player, including  the Game Master, but for the sake of simplicity, "player"  usually refers to participants other than the GM. Before  the game begins, pla |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/3` | 0.511225 | Your player character is also defined by some key choices  you make. The first choice is a PC's **ancestry**, representing the  character's parents and heritage, such as barathu, human, or  vesk. Next |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/10/Text/21` | 0.506847 | A skill represents a creature's ability to perform certain  tasks that require instruction or practice. All characters are  trained in certain skills due to their background and class.  Skills are ful |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/18` | 0.504840 | During the game, players describe the actions their  characters take and roll dice, using their characters' abilities.  The GM resolves the outcome of these actions. Some players  enjoy acting out (or |

### Query 88
- Text: What is the rule about *Starfinder Alien Core:* From the vanguard components  of the Swarm to immensely powerful starmetal dragons,  monsters are a common threat that the PCs might face, and  each type has its own statistics and abilities. These can be  found in *Starfinder Alien Core*, an invaluable book for GMs.  Monster statistics can also be found online for free at **paizo.** **com/prd**.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/5/Text/16']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/5/Text/16', 'PZO22001 Starfinder Player Core 001-013::/page/6/Text/9', 'PZO22001 Starfinder Player Core 001-013::/page/5/Text/21']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/5/Text/16` | 0.990228 | *Starfinder Alien Core:* From the vanguard components  of the Swarm to immensely powerful starmetal dragons,  monsters are a common threat that the PCs might face, and  each type has its own statistic |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/9` | 0.688705 | Aside from characters and monsters, the galaxy of  Starfinder itself can be a force at the table and in the  narrative. While the presence of the larger setting  can sometimes be an obvious hazard, su |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/5/Text/21` | 0.658291 | In Starfinder, the players take on the role of **player characters ** **(PCs)**, while the Game Master portrays **nonplayer characters ** **(NPCs)** and **monsters**. While PCs and NPCs are both impor |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/17` | 0.571323 | Everyone involved in a Starfinder game is a player, including  the Game Master, but for the sake of simplicity, "player"  usually refers to participants other than the GM. Before  the game begins, pla |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/6` | 0.560043 | Characters and their choices create the story of Starfinder,  but how they interact with each other and the galaxy around  them is governed by rules. So, while you might decide that  your character st |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/8` | 0.557952 | A roleplaying game is an interactive story where one  player, the Game Master (GM), sets the scene and presents  challenges, while other players take the roles of player  characters (PCs) and attempt |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/5/Text/12` | 0.541828 | In addition to this book, there are a few things you will need  to play Starfinder. These supplies can be found at your local  hobby shop or online at **paizo.com**. |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/14` | 0.533949 | The first rule of Starfinder is that this game is *yours*. Use  it to tell the stories you want to tell, be the character  you want to be, and share exciting adventures with  friends. If any other rul |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/2` | 0.530224 | Starfinder is a science fantasy tabletop roleplaying game (RPG) where you and a group of friends  gather to play out a story of daring adventurers exploring a galaxy filled with impossible magic,  ama |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/4` | 0.525816 | In addition to these key choices, PCs also have a number of  **feats**—individual abilities selected during character creation  and as the character increases in level. Every feat has a type  to denot |

### Query 89
- Text: What is the rule about **Maps and Miniatures:** The chaos of combat can be difficult  to imagine, so many groups use maps to represent the  battlefield. These maps are marked with a 1-inch grid, and  each square usually represents 5 feet in the game. Miniatures  and illustrated tokens called pawns are used to represent the  characters and the adversaries they face.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/5/Text/17']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/5/Text/17', 'PZO22001 Starfinder Player Core 001-013::/page/5/Text/19', 'PZO22001 Starfinder Player Core 001-013::/page/5/Text/14']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/5/Text/17` | 0.959344 | **Maps and Miniatures:** The chaos of combat can be difficult  to imagine, so many groups use maps to represent the  battlefield. These maps are marked with a 1-inch grid, and  each square usually rep |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/5/Text/19` | 0.526049 | Before creating your first character or adventure, you should  understand a number of basic concepts used in the game.  New concepts are presented in bold to make them easy to  find, but this chapter |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/5/Text/14` | 0.505062 | **Dice:** The players and GM need at least one set of  polyhedral dice, although most participants bring their own.  Six-sided dice are quite common, but all the dice in the set  can be found at hobby |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/8/Text/5` | 0.443021 | While exploration is handled in a free-form manner,  encounters are more structured. The players and GM  roll **initiative** to determine who acts in what order. The  encounter occurs over a number of |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/9` | 0.437632 | Aside from characters and monsters, the galaxy of  Starfinder itself can be a force at the table and in the  narrative. While the presence of the larger setting  can sometimes be an obvious hazard, su |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/10/Text/2` | 0.435541 | A level is a number that measures something's overall  power. Player characters have a level, ranging from 1st  to 20th, representing their level of experience. Monsters,  NPCs, hazards, diseases, and |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/2` | 0.433072 | In addition to level, characters are defined by **attributes**,  which measure raw potential and are used to calculate  most of their other statistics. There are six attributes in the  game. **Strengt |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/3` | 0.432949 | Your player character is also defined by some key choices  you make. The first choice is a PC's **ancestry**, representing the  character's parents and heritage, such as barathu, human, or  vesk. Next |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/5/Text/21` | 0.430079 | In Starfinder, the players take on the role of **player characters ** **(PCs)**, while the Game Master portrays **nonplayer characters ** **(NPCs)** and **monsters**. While PCs and NPCs are both impor |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/5/Text/15` | 0.426191 | **Adventure:** Every group needs an adventure to play,  whether it's designed by the GM or found in a published  resource. You can find a variety of exciting adventures and  even entire Adventure Path |

### Query 90
- Text: What is the rule about Before creating your first character or adventure, you should  understand a number of basic concepts used in the game.  New concepts are presented in bold to make them easy to  find, but this chapter is only an introduction to the basics of  play. The complete game rules are defined in later chapters,  and the Glossary and Index in the back of this book will help  you find the specific rules you need.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/5/Text/19']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/5/Text/19', 'PZO22001 Starfinder Player Core 001-013::/page/9/Text/2', 'PZO22001 Starfinder Player Core 001-013::/page/8/Text/5']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/5/Text/19` | 1.001466 | Before creating your first character or adventure, you should  understand a number of basic concepts used in the game.  New concepts are presented in bold to make them easy to  find, but this chapter |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/9/Text/2` | 0.772225 | There are a number of important terms that you'll need to know as you create your first character or adventure. Some of  the most important terms mentioned on previous pages are also included here for |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/8/Text/5` | 0.677446 | While exploration is handled in a free-form manner,  encounters are more structured. The players and GM  roll **initiative** to determine who acts in what order. The  encounter occurs over a number of |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/19` | 0.628965 | If this is your first experience with a roleplaying game,  it's recommended that you take on the role of a player to  familiarize yourself with the rules and the galaxy. |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/9/Text/14` | 0.621176 | A background represents what a character experienced  before they became an adventurer. Each background  grants a feat and training in one or more skills. You can  read more about backgrounds in Chapt |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/7` | 0.607558 | The GM determines the premise  and background of most adventures,  although character histories and  personalities should also play a part.  Once a game session begins, the players |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/9/Text/22` | 0.603834 | An ongoing effect that changes how a character can act,  or that alters some of their statistics, is called a condition.  The rules for the basic conditions used in the game can be  found in the Condi |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/7/Text/11` | 0.592796 | Most of the time, your character will  explore an environment, interact with  other characters, travel from place  to place, and overcome challenges.  This is called exploration. Gameplay  is relative |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/9/Text/20` | 0.591347 | A class represents the adventuring profession chosen by  a character. A character's class determines most of their  proficiencies, grants the character Hit Points each time  they gain a new level, and |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/5/Text/6` | 0.586806 | Being the GM is a challenge, requiring you to adjudicate  the rules, narrate the story, and juggle other responsibilities.  But it can also be very rewarding and worth all the work  required to run a |

### Query 91
- Text: What is the rule about DEFINING CHARACTERS?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/5/SectionHeader/20']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/5/SectionHeader/20', 'PZO22001 Starfinder Player Core 001-013::/page/4/Text/17', 'PZO22001 Starfinder Player Core 001-013::/page/6/Text/2']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/5/SectionHeader/20` | 0.874461 | DEFINING CHARACTERS |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/17` | 0.516423 | Everyone involved in a Starfinder game is a player, including  the Game Master, but for the sake of simplicity, "player"  usually refers to participants other than the GM. Before  the game begins, pla |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/2` | 0.496314 | In addition to level, characters are defined by **attributes**,  which measure raw potential and are used to calculate  most of their other statistics. There are six attributes in the  game. **Strengt |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/3` | 0.461844 | Your player character is also defined by some key choices  you make. The first choice is a PC's **ancestry**, representing the  character's parents and heritage, such as barathu, human, or  vesk. Next |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/5/Text/21` | 0.457242 | In Starfinder, the players take on the role of **player characters ** **(PCs)**, while the Game Master portrays **nonplayer characters ** **(NPCs)** and **monsters**. While PCs and NPCs are both impor |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/6` | 0.407540 | Characters and their choices create the story of Starfinder,  but how they interact with each other and the galaxy around  them is governed by rules. So, while you might decide that  your character st |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/10/SectionHeader/7` | 0.400713 | **Player Character (PC)** |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/9/Text/12` | 0.394225 | Each creature has six attribute modifiers: Strength,  Dexterity, Constitution, Intelligence, Wisdom, and  Charisma. Each of these numbers represents a creature's  raw potential and general training. A |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/7/Text/7` | 0.393548 | Checks like this are the heart of the game and are rolled all  the time, in every mode of play, to determine the outcome of  tasks. While the roll of the die is essential, the statistic you  add to th |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/4` | 0.389215 | In addition to these key choices, PCs also have a number of  **feats**—individual abilities selected during character creation  and as the character increases in level. Every feat has a type  to denot |

### Query 92
- Text: What is the rule about In Starfinder, the players take on the role of **player characters ** **(PCs)**, while the Game Master portrays **nonplayer characters ** **(NPCs)** and **monsters**. While PCs and NPCs are both important  to the story, they serve very different purposes in the game.  PCs are the protagonists—the narrative is about them—while  NPCs are allies, contacts, adversaries, and villains. That said,  PCs, NPCs, and monsters share several characteristics.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/5/Text/21']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/5/Text/21', 'PZO22001 Starfinder Player Core 001-013::/page/4/Text/17', 'PZO22001 Starfinder Player Core 001-013::/page/4/Text/8']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/5/Text/21` | 1.021805 | In Starfinder, the players take on the role of **player characters ** **(PCs)**, while the Game Master portrays **nonplayer characters ** **(NPCs)** and **monsters**. While PCs and NPCs are both impor |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/17` | 0.755925 | Everyone involved in a Starfinder game is a player, including  the Game Master, but for the sake of simplicity, "player"  usually refers to participants other than the GM. Before  the game begins, pla |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/8` | 0.726776 | A roleplaying game is an interactive story where one  player, the Game Master (GM), sets the scene and presents  challenges, while other players take the roles of player  characters (PCs) and attempt |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/5/Text/4` | 0.679810 | While the other players create and control their characters,  the Game Master (or GM) is in charge of the story and setting.  The GM describes all the situations the player characters  experience in a |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/9/Text/28` | 0.658966 | The Game Master is the player who adjudicates the rules  and narrates the various elements of the Starfinder story  and world that the other players explore. The GM uses the  rules found in *Starfinde |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/10/SectionHeader/3` | 0.625853 | **Nonplayer Character (NPC)** |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/3` | 0.608054 | Your player character is also defined by some key choices  you make. The first choice is a PC's **ancestry**, representing the  character's parents and heritage, such as barathu, human, or  vesk. Next |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/9` | 0.603920 | Aside from characters and monsters, the galaxy of  Starfinder itself can be a force at the table and in the  narrative. While the presence of the larger setting  can sometimes be an obvious hazard, su |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/6` | 0.602920 | Characters and their choices create the story of Starfinder,  but how they interact with each other and the galaxy around  them is governed by rules. So, while you might decide that  your character st |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/14` | 0.587117 | The first rule of Starfinder is that this game is *yours*. Use  it to tell the stories you want to tell, be the character  you want to be, and share exciting adventures with  friends. If any other rul |

### Query 93
- Text: What is the rule about the character's adventuring career, to 20th, the very height  of power. As the characters overcome challenges, defeat  foes, and complete adventures, they accumulate **Experience ** **Points (XP)**. Every time a character amasses 1,000 XP, they  go up a level, gaining new abilities so they can take on even  greater challenges. A 1st-level PC might face off against a  rampant assembly ooze or a hardlight scamp, but at 20th  level, that same character might be able to decimate an army  with a supermassive black hole or trade blows with a god.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/6/Text/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/6/Text/1', 'PZO22001 Starfinder Player Core 001-013::/page/5/Text/22', 'PZO22001 Starfinder Player Core 001-013::/page/10/Text/2']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/1` | 0.983304 | the character's adventuring career, to 20th, the very height  of power. As the characters overcome challenges, defeat  foes, and complete adventures, they accumulate **Experience ** **Points (XP)**. E |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/5/Text/22` | 0.636802 | **Level **is one of the most important statistics of the game,  as it conveys the approximate power and capabilities of every  individual creature. PCs range in level from 1st, at the start of |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/10/Text/2` | 0.626707 | A level is a number that measures something's overall  power. Player characters have a level, ranging from 1st  to 20th, representing their level of experience. Monsters,  NPCs, hazards, diseases, and |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/7/Text/6` | 0.580315 | For example, while aboard a starship traveling to a faraway  world, your character might find a faster route through an  uncharted asteroid field. You decide to go for it, but the GM  declares this a |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/2` | 0.579600 | In addition to level, characters are defined by **attributes**,  which measure raw potential and are used to calculate  most of their other statistics. There are six attributes in the  game. **Strengt |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/9/Text/20` | 0.566293 | A class represents the adventuring profession chosen by  a character. A character's class determines most of their  proficiencies, grants the character Hit Points each time  they gain a new level, and |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/4` | 0.562616 | In addition to these key choices, PCs also have a number of  **feats**—individual abilities selected during character creation  and as the character increases in level. Every feat has a type  to denot |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/7/Text/9` | 0.551581 | expert, master, and legendary, your  bonus equals your character's level  plus another number based on the  rank (2, 4, 6, and 8, respectively).  Proficiency ranks are part of almost  every statistic |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/3` | 0.544477 | Your player character is also defined by some key choices  you make. The first choice is a PC's **ancestry**, representing the  character's parents and heritage, such as barathu, human, or  vesk. Next |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/7/Text/11` | 0.529919 | Most of the time, your character will  explore an environment, interact with  other characters, travel from place  to place, and overcome challenges.  This is called exploration. Gameplay  is relative |

### Query 94
- Text: What is the rule about In addition to level, characters are defined by **attributes**,  which measure raw potential and are used to calculate  most of their other statistics. There are six attributes in the  game. **Strength** represents a character's physical might,  while **Dexterity** represents agility and their ability to avoid  danger. **Constitution** indicates a character's overall health  and well-being. **Intelligence** represents raw knowledge and  problem-solving ability, while **Wisdom** measures a character's  insight and their ability to evaluate a situation. Finally,  **Charisma** indicates charm, persuasiveness, and force of  personality. Attribute modifiers for ordinary creatures range  from as low as –5 to as high as +5, with +0 representing average  human capabilities. High-level characters can have attribute  modifiers that range much higher than +5. An attribute  modifier above the average increases your chance of success  at related tasks, while those below the average decrease  your chance.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/6/Text/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/6/Text/2', 'PZO22001 Starfinder Player Core 001-013::/page/9/Text/12', 'PZO22001 Starfinder Player Core 001-013::/page/7/Text/7']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/2` | 0.999143 | In addition to level, characters are defined by **attributes**,  which measure raw potential and are used to calculate  most of their other statistics. There are six attributes in the  game. **Strengt |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/9/Text/12` | 0.803557 | Each creature has six attribute modifiers: Strength,  Dexterity, Constitution, Intelligence, Wisdom, and  Charisma. Each of these numbers represents a creature's  raw potential and general training. A |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/7/Text/7` | 0.737223 | Checks like this are the heart of the game and are rolled all  the time, in every mode of play, to determine the outcome of  tasks. While the roll of the die is essential, the statistic you  add to th |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/7/Text/8` | 0.700433 | **Proficiency** is a simple way of assessing your character's  general level of training and aptitude for a given task. It's  broken into five different ranks: **untrained**, **trained**, **expert**, |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/10/Text/2` | 0.682032 | A level is a number that measures something's overall  power. Player characters have a level, ranging from 1st  to 20th, representing their level of experience. Monsters,  NPCs, hazards, diseases, and |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/4` | 0.666443 | In addition to these key choices, PCs also have a number of  **feats**—individual abilities selected during character creation  and as the character increases in level. Every feat has a type  to denot |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/5/Text/22` | 0.656491 | **Level **is one of the most important statistics of the game,  as it conveys the approximate power and capabilities of every  individual creature. PCs range in level from 1st, at the start of |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/7/Text/9` | 0.645611 | expert, master, and legendary, your  bonus equals your character's level  plus another number based on the  rank (2, 4, 6, and 8, respectively).  Proficiency ranks are part of almost  every statistic |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/10/Text/10` | 0.638980 | Proficiency is a system that measures a character's aptitude  at a specific task or quality, and it has five ranks: untrained,  trained, expert, master, and legendary. Proficiency gives  you a bonus t |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/3` | 0.633566 | Your player character is also defined by some key choices  you make. The first choice is a PC's **ancestry**, representing the  character's parents and heritage, such as barathu, human, or  vesk. Next |

### Query 95
- Text: What is the rule about Your player character is also defined by some key choices  you make. The first choice is a PC's **ancestry**, representing the  character's parents and heritage, such as barathu, human, or  vesk. Next up is the PC's **background**, which describes their  upbringing, from sly smuggler to famous icon. Finally, and  most importantly, a PC's **class** defines the majority of their  aptitudes and abilities, like a soldier's training to put down  heavy fire or a witchwarper's knack for altering reality.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/6/Text/3']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/6/Text/3', 'PZO22001 Starfinder Player Core 001-013::/page/6/Text/4', 'PZO22001 Starfinder Player Core 001-013::/page/9/Text/6']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/3` | 1.010735 | Your player character is also defined by some key choices  you make. The first choice is a PC's **ancestry**, representing the  character's parents and heritage, such as barathu, human, or  vesk. Next |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/4` | 0.757163 | In addition to these key choices, PCs also have a number of  **feats**—individual abilities selected during character creation  and as the character increases in level. Every feat has a type  to denot |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/9/Text/6` | 0.672489 | An ancestry is the broad family of people that a character  belongs to. Ancestry determines a character's starting Hit  Points, languages, senses, and Speed, and it grants access  to ancestry feats. A |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/2` | 0.638978 | In addition to level, characters are defined by **attributes**,  which measure raw potential and are used to calculate  most of their other statistics. There are six attributes in the  game. **Strengt |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/9/Text/20` | 0.614065 | A class represents the adventuring profession chosen by  a character. A character's class determines most of their  proficiencies, grants the character Hit Points each time  they gain a new level, and |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/9/Text/14` | 0.606271 | A background represents what a character experienced  before they became an adventurer. Each background  grants a feat and training in one or more skills. You can  read more about backgrounds in Chapt |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/5/Text/21` | 0.599666 | In Starfinder, the players take on the role of **player characters ** **(PCs)**, while the Game Master portrays **nonplayer characters ** **(NPCs)** and **monsters**. While PCs and NPCs are both impor |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/18` | 0.573185 | During the game, players describe the actions their  characters take and roll dice, using their characters' abilities.  The GM resolves the outcome of these actions. Some players  enjoy acting out (or |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/5/Text/19` | 0.570427 | Before creating your first character or adventure, you should  understand a number of basic concepts used in the game.  New concepts are presented in bold to make them easy to  find, but this chapter |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/7/Text/7` | 0.566745 | Checks like this are the heart of the game and are rolled all  the time, in every mode of play, to determine the outcome of  tasks. While the roll of the die is essential, the statistic you  add to th |

### Query 96
- Text: What is the rule about In addition to these key choices, PCs also have a number of  **feats**—individual abilities selected during character creation  and as the character increases in level. Every feat has a type  to denote where its explanation can be found (for example,  android feats can be found in the android ancestry) and its  theme (mystic feats, for example, grant abilities that deal  with spells). Finally, characters have **skills **that measure their  ability to treat wounds, use computers, pilot vehicles, and  perform other common tasks.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/6/Text/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/6/Text/4', 'PZO22001 Starfinder Player Core 001-013::/page/6/Text/3', 'PZO22001 Starfinder Player Core 001-013::/page/9/Text/26']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/4` | 1.011616 | In addition to these key choices, PCs also have a number of  **feats**—individual abilities selected during character creation  and as the character increases in level. Every feat has a type  to denot |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/3` | 0.726994 | Your player character is also defined by some key choices  you make. The first choice is a PC's **ancestry**, representing the  character's parents and heritage, such as barathu, human, or  vesk. Next |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/9/Text/26` | 0.715475 | A feat is an ability you can select for your character due  to their ancestry, background, class, general training, or  skill training. Some feats grant the ability to use special  actions, while othe |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/2` | 0.651358 | In addition to level, characters are defined by **attributes**,  which measure raw potential and are used to calculate  most of their other statistics. There are six attributes in the  game. **Strengt |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/7/Text/7` | 0.610940 | Checks like this are the heart of the game and are rolled all  the time, in every mode of play, to determine the outcome of  tasks. While the roll of the die is essential, the statistic you  add to th |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/10/Text/21` | 0.600692 | A skill represents a creature's ability to perform certain  tasks that require instruction or practice. All characters are  trained in certain skills due to their background and class.  Skills are ful |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/9/Text/20` | 0.594717 | A class represents the adventuring profession chosen by  a character. A character's class determines most of their  proficiencies, grants the character Hit Points each time  they gain a new level, and |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/5/Text/22` | 0.582880 | **Level **is one of the most important statistics of the game,  as it conveys the approximate power and capabilities of every  individual creature. PCs range in level from 1st, at the start of |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/1` | 0.574648 | the character's adventuring career, to 20th, the very height  of power. As the characters overcome challenges, defeat  foes, and complete adventures, they accumulate **Experience ** **Points (XP)**. E |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/9/Text/14` | 0.558882 | A background represents what a character experienced  before they became an adventurer. Each background  grants a feat and training in one or more skills. You can  read more about backgrounds in Chapt |

### Query 97
- Text: What is the rule about Characters and their choices create the story of Starfinder,  but how they interact with each other and the galaxy around  them is governed by rules. So, while you might decide that  your character steals a starship and takes off on a perilous  interstellar journey, your character's chance of success is  determined by their abilities, the choices you make,  and the roll of the dice.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/6/Text/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/6/Text/6', 'PZO22001 Starfinder Player Core 001-013::/page/4/Text/14', 'PZO22001 Starfinder Player Core 001-013::/page/4/Text/17']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/6` | 1.004237 | Characters and their choices create the story of Starfinder,  but how they interact with each other and the galaxy around  them is governed by rules. So, while you might decide that  your character st |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/14` | 0.769612 | The first rule of Starfinder is that this game is *yours*. Use  it to tell the stories you want to tell, be the character  you want to be, and share exciting adventures with  friends. If any other rul |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/17` | 0.732749 | Everyone involved in a Starfinder game is a player, including  the Game Master, but for the sake of simplicity, "player"  usually refers to participants other than the GM. Before  the game begins, pla |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/11/Text/2` | 0.660793 | The following example is presented to give you a better idea of  how Starfinder is played. In this adventure, Thurston is the GM.  Jenny is playing Obozaya, an aggressive vesk soldier; Jessica is  pla |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/2` | 0.657186 | Starfinder is a science fantasy tabletop roleplaying game (RPG) where you and a group of friends  gather to play out a story of daring adventurers exploring a galaxy filled with impossible magic,  ama |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/7/Text/2` | 0.651461 | In a Starfinder game, three modes of play determine the  pacing of each scene in the story. Most of your character's  time is spent in **exploration**, uncovering mysteries, solving  problems, and int |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/5/Text/4` | 0.628280 | While the other players create and control their characters,  the Game Master (or GM) is in charge of the story and setting.  The GM describes all the situations the player characters  experience in a |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/9` | 0.609406 | Aside from characters and monsters, the galaxy of  Starfinder itself can be a force at the table and in the  narrative. While the presence of the larger setting  can sometimes be an obvious hazard, su |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/8` | 0.605921 | A roleplaying game is an interactive story where one  player, the Game Master (GM), sets the scene and presents  challenges, while other players take the roles of player  characters (PCs) and attempt |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/5/Text/21` | 0.585466 | In Starfinder, the players take on the role of **player characters ** **(PCs)**, while the Game Master portrays **nonplayer characters ** **(NPCs)** and **monsters**. While PCs and NPCs are both impor |

### Query 98
- Text: What is the rule about The GM determines the premise  and background of most adventures,  although character histories and  personalities should also play a part.  Once a game session begins, the players?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/6/Text/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/6/Text/7', 'PZO22001 Starfinder Player Core 001-013::/page/5/Text/4', 'PZO22001 Starfinder Player Core 001-013::/page/5/Text/5']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/7` | 0.962447 | The GM determines the premise  and background of most adventures,  although character histories and  personalities should also play a part.  Once a game session begins, the players |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/5/Text/4` | 0.725514 | While the other players create and control their characters,  the Game Master (or GM) is in charge of the story and setting.  The GM describes all the situations the player characters  experience in a |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/5/Text/5` | 0.711295 | The GM can create a new adventure—crafting a narrative,  selecting monsters, and assigning rewards on their own or they can instead rely on a published adventure, using  it as a basis for the session |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/9` | 0.656429 | The game is typically played in a group of four to seven  players, with one of those players serving as the group's GM.  The GM prepares, presents, and presides over the game's  setting and story, pos |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/17` | 0.647878 | Everyone involved in a Starfinder game is a player, including  the Game Master, but for the sake of simplicity, "player"  usually refers to participants other than the GM. Before  the game begins, pla |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/10` | 0.640173 | take turns describing what their characters attempt to  do, while the GM determines the outcome, with everyone  working together to create the story. The GM also describes  the environment, other char |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/5/Text/10` | 0.632217 | other identities and life experiences. It's the responsibility of  all of the players, not just the GM, to make sure the game is  fun and welcoming for everyone. |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/5/Text/6` | 0.624765 | Being the GM is a challenge, requiring you to adjudicate  the rules, narrate the story, and juggle other responsibilities.  But it can also be very rewarding and worth all the work  required to run a |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/8/Text/2` | 0.607520 | Throughout this mode of play, the GM asks the players  what their characters are doing as they explore. This is  important in case a conflict arises. If combat breaks out, the  tasks the PCs undertook |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/5/Text/19` | 0.598888 | Before creating your first character or adventure, you should  understand a number of basic concepts used in the game.  New concepts are presented in bold to make them easy to  find, but this chapter |

### Query 99
- Text: What is the rule about Aside from characters and monsters, the galaxy of  Starfinder itself can be a force at the table and in the  narrative. While the presence of the larger setting  can sometimes be an obvious hazard, such as when a  firestorm rages through an alien jungle, the setting can  also act in subtler, smaller ways. Traps and treasures  are just as important in many tales as monstrous foes.  To help you understand these game elements, many of  them use the same characteristics as characters and  monsters. For example, most environmental hazards  have a level that indicates how dangerous they are,  and the level of a magic item gives you a sense of its  overall power and impact on a story.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/6/Text/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/6/Text/9', 'PZO22001 Starfinder Player Core 001-013::/page/6/Text/6', 'PZO22001 Starfinder Player Core 001-013::/page/7/Text/2']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/9` | 1.015352 | Aside from characters and monsters, the galaxy of  Starfinder itself can be a force at the table and in the  narrative. While the presence of the larger setting  can sometimes be an obvious hazard, su |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/6/Text/6` | 0.721880 | Characters and their choices create the story of Starfinder,  but how they interact with each other and the galaxy around  them is governed by rules. So, while you might decide that  your character st |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/7/Text/2` | 0.685325 | In a Starfinder game, three modes of play determine the  pacing of each scene in the story. Most of your character's  time is spent in **exploration**, uncovering mysteries, solving  problems, and int |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/5/Text/21` | 0.637785 | In Starfinder, the players take on the role of **player characters ** **(PCs)**, while the Game Master portrays **nonplayer characters ** **(NPCs)** and **monsters**. While PCs and NPCs are both impor |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/5/Text/16` | 0.620729 | *Starfinder Alien Core:* From the vanguard components  of the Swarm to immensely powerful starmetal dragons,  monsters are a common threat that the PCs might face, and  each type has its own statistic |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/14` | 0.615649 | The first rule of Starfinder is that this game is *yours*. Use  it to tell the stories you want to tell, be the character  you want to be, and share exciting adventures with  friends. If any other rul |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/8` | 0.607483 | A roleplaying game is an interactive story where one  player, the Game Master (GM), sets the scene and presents  challenges, while other players take the roles of player  characters (PCs) and attempt |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/2` | 0.602854 | Starfinder is a science fantasy tabletop roleplaying game (RPG) where you and a group of friends  gather to play out a story of daring adventurers exploring a galaxy filled with impossible magic,  ama |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/4/Text/17` | 0.598610 | Everyone involved in a Starfinder game is a player, including  the Game Master, but for the sake of simplicity, "player"  usually refers to participants other than the GM. Before  the game begins, pla |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/8/Text/4` | 0.575746 | During your adventures, there will be times when a simple  skill check is not enough to resolve a challenge—when  vicious monsters or ruthless enemies attack your character  and the only choice is to |

### Query 100
- Text: Lookup values for Thurston:Your ship speeds through the swirlingcolors and half-formed shapes of the Drift.You're getting close to the coordinates, butchunks of rock, ice, and metal scrap floatahead of you, blocking your path.Zemir (Mike):"Time to chart a course through this mess."I take a deep breath, grip the controls, andpilot the ship into the debris field.Thurston:Roll your Piloting check.Zemir (Mike):I rolled a 5, so with my +7 modifier I got a12. "I'm gonna need more coffee for this."Thurston:Zemir turns just in time to avoid crashinginto a massive asteroid, but he loses thepath he was following.Chk Chk (Dustin): I perform a dramatic reading of a poem Iwrote about finding inspiration in failurethrough our Group Chat.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/11/Table/3']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/11/Table/3', 'PZO22001 Starfinder Player Core 001-013::/page/11/Table/5', 'PZO22001 Starfinder Player Core 001-013::/page/12/Table/2']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/11/Table/3` | 1.006210 | Thurston:Your ship speeds through the swirlingcolors and half-formed shapes of the Drift.You're getting close to the coordinates, butchunks of rock, ice, and metal scrap floatahead of you, blocking yo |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/11/Table/5` | 0.804123 | Zemir (Mike):"Thanks, Chk Chk." I chug some coffee andtry again. 13! I've got a +7 to Piloting sothat's a 20!Thurston:The ship zooms safely through thedebris until the beacon you were sent toinvestiga |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/12/Table/2` | 0.759797 | Thurston:Zemir, you're up first.Zemir (Mike):Excellent. For my first action, I spend 1Focus Point to cast warp terrain.Thurston:Which effect do you choose?Zemir (Mike):I choose difficult terrain. My q |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/11/Table/7` | 0.688358 | Dae (Jessica):I head for the airlock, then strike a pose asI step into space. "Hey Chk Chk, make sureyou're recording this!"Thurston:Now you're untethered. Are you freefloating?Dae (Jessica):Nope! I a |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/12/Table/6` | 0.610700 | Zemir (Mike):For my third action, I Take Cover behind arock in my quantum field.Thurston:The rotting vesk recoils as laser fire hits it,then it shoots a bolt of void energy at you. |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/12/Text/7` | 0.602513 | Thurston rolls a 22. Zemir's AC is 21, but he gains a +2  circumstance bonus from standard cover. The attack misses.  The driftdead fires another bolt at him. Thurston rolls a 23,  which hits Zemir's |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/11/Text/2` | 0.592048 | The following example is presented to give you a better idea of  how Starfinder is played. In this adventure, Thurston is the GM.  Jenny is playing Obozaya, an aggressive vesk soldier; Jessica is  pla |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/11/Table/9` | 0.582536 | Thurston:The autodoor stutters open. A vesk and ahuman wearing tattered spacesuits loomin the doorway. Milky eyes bulge out oftheir rotting faces. Roll for initiative! |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/12/Text/3` | 0.567013 | Mike rolls a 12 and adds +8, due to Zemir's training with simple  weapons, for a total of 20. Thurston consults his notes to  confirm the driftdead has an AC of 16. |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/12/Table/10` | 0.563706 | Thurston:The walking corpse turns its anger on you,Chk Chk. It lurches toward you and lashesout with clawed hands. Does a 23 hit you? |

### Query 101
- Text: Lookup values for Zemir (Mike):"Thanks, Chk Chk." I chug some coffee andtry again. 13! I've got a +7 to Piloting sothat's a 20!Thurston:The
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/11/Table/5']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/11/Table/3', 'PZO22001 Starfinder Player Core 001-013::/page/11/Table/5', 'PZO22001 Starfinder Player Core 001-013::/page/12/Text/3']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/11/Table/3` | 0.727383 | Thurston:Your ship speeds through the swirlingcolors and half-formed shapes of the Drift.You're getting close to the coordinates, butchunks of rock, ice, and metal scrap floatahead of you, blocking yo |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/11/Table/5` | 0.712535 | Zemir (Mike):"Thanks, Chk Chk." I chug some coffee andtry again. 13! I've got a +7 to Piloting sothat's a 20!Thurston:The ship zooms safely through thedebris until the beacon you were sent toinvestiga |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/12/Text/3` | 0.642449 | Mike rolls a 12 and adds +8, due to Zemir's training with simple  weapons, for a total of 20. Thurston consults his notes to  confirm the driftdead has an AC of 16. |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/12/Table/2` | 0.598052 | Thurston:Zemir, you're up first.Zemir (Mike):Excellent. For my first action, I spend 1Focus Point to cast warp terrain.Thurston:Which effect do you choose?Zemir (Mike):I choose difficult terrain. My q |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/11/TableCell/469` | 0.585730 | Chk Chk (Dustin): "Zemir, can you get us closer?" I'm going to |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/12/SectionHeader/8` | 0.578281 | **Chk Chk (Dustin):** I cast *vibe check*. I'm broadcasting an  angry poem about my childhood into the  human's mind: "Despite all my bile, I am  still just a bug in a vial!" That's two actions.  Then |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/11/TableCell/445` | 0.541071 | try again. 13! I've got a +7 to Piloting so |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/11/TableCell/442` | 0.540893 | Zemir (Mike): |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/12/Table/6` | 0.539994 | Zemir (Mike):For my third action, I Take Cover behind arock in my quantum field.Thurston:The rotting vesk recoils as laser fire hits it,then it shoots a bolt of void energy at you. |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/12/TableCell/444` | 0.530553 | Zemir, you're up first. |

### Query 102
- Text: Lookup values for Dae (Jessica):I head for the airlock, then strike a pose asI step into space. "Hey Chk Chk, make sureyou're recording this!"Thurston:Now you're untethered. Are you freefloating?Dae (Jessica):Nope! I activate the jetpack and fly towardthe ysoki.Obozaya (Jenny): "Careful, Dae. I don't want to have to cleanyou off the side of that Drift beacon."Chk Chk (Dustin): "A splash of red would look great on thatsilver metal. But not if it's Dae's blood!Don't look at me like that, Zemir."Dae (Jessica):"No worries, bestie. After we rescue theysoki, we can give the beacon a glow up."Thurston:Dae, up close, you notice that the ysoki'sspacesuit is covered in blood, and thatthere's a crack in their helmet. Underneath,their face is frozen in a mask of terror.Zemir (Mike):"Dae, it's time to get back to the ship."Dae (Jessica):"You don't have tell me twice, Z!" I grab theysoki and drag them back to the ship.Thurston:Dae, when you get back to the airlock,you notice blood smears on the floor thatweren't there when you left.Dae (Jessica):"Heads up. I think something got onto theship." I leave the ysoki in the airlock andsprint toward the bridge.Thurston:Dae stops 60 feet down the hall fromthe bridge door. The rest of you heardull scraping outside. It sounds likesomething's shuffling toward you.Obozaya (Jenny): I pull out my machine gun and move infront of my allies, facing the door. Bring it.Zemir (Mike):I stand up from the pilot's console anddraw my laser pistol.Chk Chk (Dustin): I draw my painglaive and check my bondto make sure Dae's safe.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/11/Table/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/11/Table/7', 'PZO22001 Starfinder Player Core 001-013::/page/11/Table/5', 'PZO22001 Starfinder Player Core 001-013::/page/11/Table/3']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/11/Table/7` | 1.016324 | Dae (Jessica):I head for the airlock, then strike a pose asI step into space. "Hey Chk Chk, make sureyou're recording this!"Thurston:Now you're untethered. Are you freefloating?Dae (Jessica):Nope! I a |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/11/Table/5` | 0.836480 | Zemir (Mike):"Thanks, Chk Chk." I chug some coffee andtry again. 13! I've got a +7 to Piloting sothat's a 20!Thurston:The ship zooms safely through thedebris until the beacon you were sent toinvestiga |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/11/Table/3` | 0.765154 | Thurston:Your ship speeds through the swirlingcolors and half-formed shapes of the Drift.You're getting close to the coordinates, butchunks of rock, ice, and metal scrap floatahead of you, blocking yo |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/12/Text/17` | 0.615694 | **Dae (Jessica):** My black battle ribbon bursts into solar  flame. I pirouette and attack the vesk,  making sure the camera drone can see all  my moves. I rolled a 26. |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/12/Text/14` | 0.612703 | **Dae (Jessica):** My turn! I Stellar Rush down the hall and  into the bridge. Black lightning crackles  around me and drags both enemies toward  me when I dash past them. |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/11/Text/12` | 0.598612 | **Thurston:** Dae, are you installing Obozaya's jetpack  into your armor? **Obozaya (Jenny):** Paws off! I'll do it with Quick Install. |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/12/Text/26` | 0.592070 | **Thurston:** One foe falls to Obozaya's barrage. There's a  sudden lurch that feels like being pulled into  the Drift as the dead ysoki from the airlock  phases through the floor and lunges at Dae  c |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/12/Table/2` | 0.579162 | Thurston:Zemir, you're up first.Zemir (Mike):Excellent. For my first action, I spend 1Focus Point to cast warp terrain.Thurston:Which effect do you choose?Zemir (Mike):I choose difficult terrain. My q |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/11/TableCell/541` | 0.562971 | ship." I leave the ysoki in the airlock and |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/12/Text/21` | 0.546759 | **Obozaya (Jenny):** "Thanks for the setup, Dae!" I Auto-Fire at  both enemies. The human is closest to me,  so she's my primary target. |

### Query 103
- Text: Lookup values for Thurston:The autodoor stutters open. A vesk and ahuman wearing tattered spacesuits loomin the doorway. Milky eyes bulge out oftheir rotting faces. Roll for initiative!
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/11/Table/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/11/Table/9', 'PZO22001 Starfinder Player Core 001-013::/page/11/TableCell/569', 'PZO22001 Starfinder Player Core 001-013::/page/12/Table/10']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/11/Table/9` | 0.969267 | Thurston:The autodoor stutters open. A vesk and ahuman wearing tattered spacesuits loomin the doorway. Milky eyes bulge out oftheir rotting faces. Roll for initiative! |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/11/TableCell/569` | 0.660566 | The autodoor stutters open. A vesk and a |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/12/Table/10` | 0.631489 | Thurston:The walking corpse turns its anger on you,Chk Chk. It lurches toward you and lashesout with clawed hands. Does a 23 hit you? |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/12/SectionHeader/19` | 0.587601 | **Thurston:** The creature snarls as the ribbon of starlight  lashes across its torso, singeing its ruined |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/11/Table/3` | 0.585363 | Thurston:Your ship speeds through the swirlingcolors and half-formed shapes of the Drift.You're getting close to the coordinates, butchunks of rock, ice, and metal scrap floatahead of you, blocking yo |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/12/TableCell/473` | 0.578794 | Thurston: |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/11/TableCell/568` | 0.578794 | Thurston: |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/11/Table/5` | 0.576005 | Zemir (Mike):"Thanks, Chk Chk." I chug some coffee andtry again. 13! I've got a +7 to Piloting sothat's a 20!Thurston:The ship zooms safely through thedebris until the beacon you were sent toinvestiga |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/12/TableCell/449` | 0.566794 | Thurston: |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/11/TableCell/496` | 0.566794 | Thurston: |

### Query 104
- Text: Lookup values for Thurston:Zemir, you're up first.Zemir (Mike):Excellent. For my first action, I spend 1Focus Point to cast warp terrain.Thurston:Which effect do you choose?Zemir (Mike):I choose difficult terrain. My quantum fieldfills with twisted metal and chunks of rockfrom a reality where we didn't make it pastthat asteroid safely. For my next action, Ishoot the vesk with my new laser pistol!
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/12/Table/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/12/Table/2', 'PZO22001 Starfinder Player Core 001-013::/page/12/Table/6', 'PZO22001 Starfinder Player Core 001-013::/page/11/Table/3']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/12/Table/2` | 1.027962 | Thurston:Zemir, you're up first.Zemir (Mike):Excellent. For my first action, I spend 1Focus Point to cast warp terrain.Thurston:Which effect do you choose?Zemir (Mike):I choose difficult terrain. My q |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/12/Table/6` | 0.769697 | Zemir (Mike):For my third action, I Take Cover behind arock in my quantum field.Thurston:The rotting vesk recoils as laser fire hits it,then it shoots a bolt of void energy at you. |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/11/Table/3` | 0.754501 | Thurston:Your ship speeds through the swirlingcolors and half-formed shapes of the Drift.You're getting close to the coordinates, butchunks of rock, ice, and metal scrap floatahead of you, blocking yo |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/11/Table/5` | 0.655496 | Zemir (Mike):"Thanks, Chk Chk." I chug some coffee andtry again. 13! I've got a +7 to Piloting sothat's a 20!Thurston:The ship zooms safely through thedebris until the beacon you were sent toinvestiga |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/12/Text/7` | 0.561948 | Thurston rolls a 22. Zemir's AC is 21, but he gains a +2  circumstance bonus from standard cover. The attack misses.  The driftdead fires another bolt at him. Thurston rolls a 23,  which hits Zemir's |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/11/Table/7` | 0.557888 | Dae (Jessica):I head for the airlock, then strike a pose asI step into space. "Hey Chk Chk, make sureyou're recording this!"Thurston:Now you're untethered. Are you freefloating?Dae (Jessica):Nope! I a |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/12/TableCell/452` | 0.547604 | I choose difficult terrain. My quantum field |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/12/TableCell/448` | 0.547187 | Focus Point to cast warp terrain. |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/12/SectionHeader/8` | 0.528756 | **Chk Chk (Dustin):** I cast *vibe check*. I'm broadcasting an  angry poem about my childhood into the  human's mind: "Despite all my bile, I am  still just a bug in a vial!" That's two actions.  Then |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/12/Text/3` | 0.524376 | Mike rolls a 12 and adds +8, due to Zemir's training with simple  weapons, for a total of 20. Thurston consults his notes to  confirm the driftdead has an AC of 16. |

### Query 105
- Text: Lookup values for Thurston:You hit! Roll for damage.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/12/Table/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/12/Table/4', 'PZO22001 Starfinder Player Core 001-013::/page/12/TableCell/464', 'PZO22001 Starfinder Player Core 001-013::/page/12/Text/12']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/12/Table/4` | 0.922598 | Thurston:You hit! Roll for damage. |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/12/TableCell/464` | 0.711883 | You hit! Roll for damage. |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/12/Text/12` | 0.645799 | Thurston rolls for slashing damage from the driftdead's claws  and gets a total of 10. |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/12/TableCell/463` | 0.569397 | Thurston: |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/12/TableCell/469` | 0.557397 | Thurston: |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/12/TableCell/473` | 0.557397 | Thurston: |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/11/TableCell/448` | 0.557397 | Thurston: |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/11/TableCell/568` | 0.557397 | Thurston: |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/12/TableCell/443` | 0.557397 | Thurston: |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/12/TableCell/449` | 0.557397 | Thurston: |

### Query 106
- Text: Lookup values for Zemir (Mike):For my third action, I Take Cover behind arock in my quantum field.Thurston:The rotting vesk recoils as laser fire hits it,then it shoots a bolt of void energy at you.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/12/Table/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/12/Table/6', 'PZO22001 Starfinder Player Core 001-013::/page/12/Table/2', 'PZO22001 Starfinder Player Core 001-013::/page/11/Table/3']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/12/Table/6` | 0.986533 | Zemir (Mike):For my third action, I Take Cover behind arock in my quantum field.Thurston:The rotting vesk recoils as laser fire hits it,then it shoots a bolt of void energy at you. |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/12/Table/2` | 0.756200 | Thurston:Zemir, you're up first.Zemir (Mike):Excellent. For my first action, I spend 1Focus Point to cast warp terrain.Thurston:Which effect do you choose?Zemir (Mike):I choose difficult terrain. My q |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/11/Table/3` | 0.652740 | Thurston:Your ship speeds through the swirlingcolors and half-formed shapes of the Drift.You're getting close to the coordinates, butchunks of rock, ice, and metal scrap floatahead of you, blocking yo |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/11/Table/5` | 0.590919 | Zemir (Mike):"Thanks, Chk Chk." I chug some coffee andtry again. 13! I've got a +7 to Piloting sothat's a 20!Thurston:The ship zooms safely through thedebris until the beacon you were sent toinvestiga |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/12/TableCell/470` | 0.558244 | The rotting vesk recoils as laser fire hits it, |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/12/TableCell/465` | 0.548197 | Zemir (Mike): |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/11/TableCell/556` | 0.536197 | Zemir (Mike): |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/11/TableCell/526` | 0.536197 | Zemir (Mike): |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/11/TableCell/420` | 0.536197 | Zemir (Mike): |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/11/TableCell/462` | 0.536197 | Zemir (Mike): |

### Query 107
- Text: Lookup values for Thurston:The walking corpse turns its anger on you,Chk Chk. It lurches toward you and lashesout with clawed hands. Does a 23 hit you?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 001-013::/page/12/Table/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 001-013::/page/12/Table/10', 'PZO22001 Starfinder Player Core 001-013::/page/12/TableCell/474', 'PZO22001 Starfinder Player Core 001-013::/page/12/Table/4']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 001-013::/page/12/Table/10` | 0.958955 | Thurston:The walking corpse turns its anger on you,Chk Chk. It lurches toward you and lashesout with clawed hands. Does a 23 hit you? |
| 2 | `PZO22001 Starfinder Player Core 001-013::/page/12/TableCell/474` | 0.611340 | The walking corpse turns its anger on you, |
| 3 | `PZO22001 Starfinder Player Core 001-013::/page/12/Table/4` | 0.594323 | Thurston:You hit! Roll for damage. |
| 4 | `PZO22001 Starfinder Player Core 001-013::/page/11/Table/9` | 0.551923 | Thurston:The autodoor stutters open. A vesk and ahuman wearing tattered spacesuits loomin the doorway. Milky eyes bulge out oftheir rotting faces. Roll for initiative! |
| 5 | `PZO22001 Starfinder Player Core 001-013::/page/12/Text/9` | 0.537820 | Thurston rolls a 17 for the human driftdead's Will save against  Chk Chk's spell DC of 21. The driftdead fails and must use its  next action to attack the nearest creature. The angry driftdead  goes n |
| 6 | `PZO22001 Starfinder Player Core 001-013::/page/11/Table/3` | 0.529558 | Thurston:Your ship speeds through the swirlingcolors and half-formed shapes of the Drift.You're getting close to the coordinates, butchunks of rock, ice, and metal scrap floatahead of you, blocking yo |
| 7 | `PZO22001 Starfinder Player Core 001-013::/page/12/TableCell/478` | 0.518863 | out with clawed hands. Does a 23 hit you? |
| 8 | `PZO22001 Starfinder Player Core 001-013::/page/12/SectionHeader/19` | 0.518362 | **Thurston:** The creature snarls as the ribbon of starlight  lashes across its torso, singeing its ruined |
| 9 | `PZO22001 Starfinder Player Core 001-013::/page/12/Text/26` | 0.517853 | **Thurston:** One foe falls to Obozaya's barrage. There's a  sudden lurch that feels like being pulled into  the Drift as the dead ysoki from the airlock  phases through the floor and lunges at Dae  c |
| 10 | `PZO22001 Starfinder Player Core 001-013::/page/11/Table/5` | 0.512976 | Zemir (Mike):"Thanks, Chk Chk." I chug some coffee andtry again. 13! I've got a +7 to Piloting sothat's a 20!Thurston:The ship zooms safely through thedebris until the beacon you were sent toinvestiga |
