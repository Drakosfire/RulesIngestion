# RulesLawyer Evaluation Report: nomic-embed-text-v2

## Summary
- Run ID: `None`
- Ruleset ID: `None`
- Document ID: `None`
- Chunk source: `enriched`
- Chunk count: `655`
- Query count: `150`
- Evaluated queries: `150`
- Coverage: `1.0000`
- MRR: `0.8596`
- hit@1: `0.7800`
- hit@3: `0.9200`
- hit@5: `0.9667`
- hit@10: `1.0000`
- Embeddings reused: `False`
- Graph boost: `0.05` (depth=2, top_k=50, source=top, seed_top_n=3, same_kind_only=False, decay=0.4)

## Timings (ms)
- Embedding (chunks): `10796`
- Embedding (queries): `3683`
- Evaluation (strict): `73`
- Evaluation (expanded): `0`
- Total: `18903`

### Timing Estimates (ms)
- Evaluation (strict): `390`
- Evaluation (expanded): `None`
- Total: `14869`

## Query Details
### Query 0
- Text: Summarize LASHUNTA
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/0/SectionHeader/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/0/SectionHeader/1', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/2', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/15']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/0/SectionHeader/1` | 0.971144 | LASHUNTA |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/15` | 0.901013 | **LASHUNTA** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/2` | 0.901013 | **LASHUNTA** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/20` | 0.859013 | **LASHUNTA** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/20` | 0.859013 | **LASHUNTA** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/11` | 0.859013 | **LASHUNTA** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/11` | 0.859013 | **LASHUNTA** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/30` | 0.859013 | **LASHUNTA** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/30` | 0.859013 | **LASHUNTA** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/26` | 0.859013 | **LASHUNTA** |

### Query 1
- Text: What is the rule about Long ago, lashuntas evolved psychic abilities and a unique dimorphism that helped them survive on their home world of Castrovel. In modern times, lashuntas manipulate their own genetics at puberty, allowing each individual to develop into an enhanced scholar or warrior, though not every lashunta commits to these traditional choices.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/0/Text/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/0/Text/2', 'PZO22001 Starfinder Player Core 058-073::/page/1/Text/13', 'PZO22001 Starfinder Player Core 058-073::/page/1/Text/9']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/0/Text/2` | 0.991765 | Long ago, lashuntas evolved psychic abilities and a unique dimorphism that helped them survive on their home world of Castrovel. In modern times, lashuntas manipulate their own genetics at puberty, al |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/13` | 0.779356 | Around puberty, lashuntas traditionally choose whether  to express damaya or korasha genetics—a decision that  determines their physical development and influences their  potential societal roles. Las |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/9` | 0.769734 | Lashuntas are natural psychics with adaptive genetics who  traditionally develop into one of two heritages at puberty:  damayas or korashas. They have a well-earned reputation for  being charismatic, |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/23` | 0.679962 | Around puberty, many lashuntas choose to embrace a genetic  path that determines their physiology and role in society.  Choose one of the following lashunta heritages at 1st level. |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/10` | 0.651146 | If you want to play a character who strives for selfimprovement and has innate psychic abilities, you should play  a lashunta. |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/27` | 0.613516 | You've chosen the adaptive genetics to become a korasha. You  might be stockier and more muscular than other lashuntas. |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/31` | 0.602943 | You've studied the lives and achievements of other  lashuntas who have improved both their psychic powers  and their communities. You gain the trained proficiency  rank in Occultism and Society. If yo |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/25` | 0.599443 | You've chosen the adaptive genetics to become a damaya. You  might have a leaner, lither body type than other lashuntas and  are likely encouraged to pursue work as a scholar or politician.  In additi |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/12` | 0.587658 | Damayas tend to be tall and graceful with delicate features and  are traditionally pushed toward artistic or intellectual pursuits  and political occupations. Korashas are shorter, more muscular,  and |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/7` | 0.580079 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As a lashunta, you choose from among  the following |

### Query 2
- Text: Summarize SIZE: MEDIUM SPEED: 25 FEET
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/0/Text/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/0/Text/5', 'PZO22001 Starfinder Player Core 058-073::/page/4/Text/7', 'PZO22001 Starfinder Player Core 058-073::/page/8/Text/7']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/0/Text/5` | 1.022251 | SIZE: MEDIUM SPEED: 25 FEET |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/4/Text/7` | 1.022251 | SIZE: MEDIUM SPEED: 25 FEET |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/8/Text/7` | 1.022251 | SIZE: MEDIUM SPEED: 25 FEET |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/12/Text/5` | 0.854833 | SIZE: SMALL SPEED: 25 FEET |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/15/SectionHeader/48` | 0.455170 | **SUPERSONIC SPEED** **FEAT 13** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/14/Text/28` | 0.382132 | You're full of energy, and you often bound into action faster  than your friends can keep up. Your Speed increases by 5  feet. |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/31` | 0.355428 | **Special** If you're a winged shirren, you either grow a second set  of wings or your existing wings morph into a stronger set of  wings, increasing your fly Speed to 25 feet. |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/85` | 0.335293 | **FEATS** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/75` | 0.335293 | **FEATS** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/46` | 0.335293 | **FEATS** |

### Query 3
- Text: Summarize ATTRIBUTE BOOSTS
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/0/SectionHeader/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/0/SectionHeader/6', 'PZO22001 Starfinder Player Core 058-073::/page/4/Text/8', 'PZO22001 Starfinder Player Core 058-073::/page/12/Text/6']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/0/SectionHeader/6` | 0.975006 | ATTRIBUTE BOOSTS |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/4/Text/8` | 0.595194 | ATTRIBUTE BOOSTS Charisma Dexterity Free |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/12/Text/6` | 0.595194 | ATTRIBUTE BOOSTS Charisma Dexterity Free |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/8/Text/8` | 0.550900 | **ATTRIBUTE **BOOSTS Constitution Wisdom Free |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/12/Text/7` | 0.400910 | ATTRIBUTE FLAW Wisdom |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/4/Text/9` | 0.391562 | ATTRIBUTE FLAW Constitution |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/1` | 0.368476 | In addition to what you gain from your ancestry, you gain an  attribute boost to Strength and an attribute flaw to Wisdom,  but the free ancestry boost can't also be Strength. You gain 8  Hit Points f |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/8/Text/9` | 0.354682 | ATTRIBUTE FLAW Charisma |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/71` | 0.299181 | **Backgrounds** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/77` | 0.299181 | **Backgrounds** |

### Query 4
- Text: Summarize Charisma Free
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/0/Text/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/0/Text/7', 'PZO22001 Starfinder Player Core 058-073::/page/12/Text/6', 'PZO22001 Starfinder Player Core 058-073::/page/4/Text/8']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/0/Text/7` | 0.967404 | Charisma Free |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/12/Text/6` | 0.695866 | ATTRIBUTE BOOSTS Charisma Dexterity Free |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/4/Text/8` | 0.695866 | ATTRIBUTE BOOSTS Charisma Dexterity Free |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/8/Text/9` | 0.560536 | ATTRIBUTE FLAW Charisma |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/8/Text/8` | 0.379386 | **ATTRIBUTE **BOOSTS Constitution Wisdom Free |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/10` | 0.343502 | If you want to play a character who fights for freedom with  grace and style, you should play a pahtra. |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/41` | 0.336493 | **Prerequisites** Communalism |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/25` | 0.329286 | You've chosen the adaptive genetics to become a damaya. You  might have a leaner, lither body type than other lashuntas and  are likely encouraged to pursue work as a scholar or politician.  In additi |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/13` | 0.319747 | **CENTER THOUGHTS **[free-action] **FEAT 1** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/13/Text/33` | 0.315067 | **Barathu** **Human** |

### Query 5
- Text: Summarize LANGUAGES Castrovelian, Common
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/0/SectionHeader/8']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/0/SectionHeader/8', 'PZO22001 Starfinder Player Core 058-073::/page/8/SectionHeader/10', 'PZO22001 Starfinder Player Core 058-073::/page/4/SectionHeader/10']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/0/SectionHeader/8` | 1.025354 | LANGUAGES Castrovelian, Common |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/8/SectionHeader/10` | 0.538136 | LANGUAGES Common, Shirren |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/4/SectionHeader/10` | 0.449272 | LANGUAGES Common, Pahtra, Vesk |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/8/Text/11` | 0.367954 | One regional language of your choice Additional languages equal to your Intelligence modifier (if it's positive). Choose from the list of common languages and any other languages to which you have acc |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/16` | 0.357527 | picturesque cities along the shores and wildlands of Castrovel,  a lush jungle world teeming with dangerous predators and  extreme weather. These independent settlements are protected  by a mighty mil |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/4/Text/11` | 0.353885 | Additional languages equal to your Intelligence modifier (if it's positive). Choose from the list of common languages and any other languages to which you have access (such as the languages prevalent |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/0/Text/9` | 0.353885 | Additional languages equal to your Intelligence modifier (if it's positive). Choose from the list of common languages and any other languages to which you have access (such as the languages prevalent |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/12/Text/9` | 0.341885 | Additional languages equal to your Intelligence modifier (if it's positive). Choose from the list of common languages and any other languages to which you have access (such as the languages prevalent |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/43` | 0.337121 | **Backgrounds** **Languages** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/13/Text/44` | 0.337121 | **Backgrounds** **Languages** |

### Query 6
- Text: What is the rule about Additional languages equal to your Intelligence modifier (if it's positive). Choose from the list of common languages and any other languages to which you have access (such as the languages prevalent on your home world).?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/0/Text/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/0/Text/9', 'PZO22001 Starfinder Player Core 058-073::/page/4/Text/11', 'PZO22001 Starfinder Player Core 058-073::/page/12/Text/9']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/0/Text/9` | 0.982267 | Additional languages equal to your Intelligence modifier (if it's positive). Choose from the list of common languages and any other languages to which you have access (such as the languages prevalent |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/4/Text/11` | 0.982267 | Additional languages equal to your Intelligence modifier (if it's positive). Choose from the list of common languages and any other languages to which you have access (such as the languages prevalent |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/12/Text/9` | 0.982267 | Additional languages equal to your Intelligence modifier (if it's positive). Choose from the list of common languages and any other languages to which you have access (such as the languages prevalent |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/8/Text/11` | 0.905517 | One regional language of your choice Additional languages equal to your Intelligence modifier (if it's positive). Choose from the list of common languages and any other languages to which you have acc |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/10/Text/28` | 0.584960 | Learning new languages comes naturally to you. You gain two  additional languages of your choice, chosen from among the  common and uncommon languages available to you. Every time  you take the Multil |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/25` | 0.486165 | You've chosen the adaptive genetics to become a damaya. You  might have a leaner, lither body type than other lashuntas and  are likely encouraged to pursue work as a scholar or politician.  In additi |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/4` | 0.477043 | Your ability to adapt to various beliefs instills you with  knowledge of many cultures. You gain the trained proficiency  rank in Diplomacy and Society. If you would automatically  become trained in o |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/12/Text/8` | 0.455123 | One regional language of your choice |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/13/Text/44` | 0.450809 | **Backgrounds** **Languages** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/43` | 0.450809 | **Backgrounds** **Languages** |

### Query 7
- Text: What is the rule about **TRAITS **?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/0/SectionHeader/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/0/SectionHeader/10', 'PZO22001 Starfinder Player Core 058-073::/page/4/SectionHeader/12', 'PZO22001 Starfinder Player Core 058-073::/page/12/SectionHeader/10']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/0/SectionHeader/10` | 0.867974 | **TRAITS ** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/4/SectionHeader/12` | 0.867974 | **TRAITS ** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/12/SectionHeader/10` | 0.769948 | TRAITS |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/8/SectionHeader/12` | 0.739948 | TRAITS |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/74` | 0.464114 | **SKILLS** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/13/Text/46` | 0.464114 | **SKILLS** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/45` | 0.464114 | **SKILLS** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/84` | 0.464114 | **SKILLS** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/80` | 0.464114 | **SKILLS** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/45` | 0.464114 | **SKILLS** |

### Query 8
- Text: Summarize HUMANOID LASHUNTA
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/0/Text/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/0/Text/11', 'PZO22001 Starfinder Player Core 058-073::/page/0/SectionHeader/1', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/47']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/0/Text/11` | 1.002259 | HUMANOID LASHUNTA |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/0/SectionHeader/1` | 0.732315 | LASHUNTA |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/47` | 0.684557 | **LASHUNTA** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/59` | 0.642557 | **LASHUNTA** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/26` | 0.642557 | **LASHUNTA** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/20` | 0.642557 | **LASHUNTA** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/15` | 0.642557 | **LASHUNTA** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/30` | 0.642557 | **LASHUNTA** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/11` | 0.642557 | **LASHUNTA** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/2` | 0.642557 | **LASHUNTA** |

### Query 9
- Text: Summarize LIMITED TELEPATHY
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/0/SectionHeader/12']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/8/SectionHeader/14', 'PZO22001 Starfinder Player Core 058-073::/page/0/SectionHeader/12', 'PZO22001 Starfinder Player Core 058-073::/page/2/Text/25']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/8/SectionHeader/14` | 0.973045 | LIMITED TELEPATHY |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/0/SectionHeader/12` | 0.973045 | LIMITED TELEPATHY |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/25` | 0.709022 | **Prerequisites** limited telepathy |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/22` | 0.667022 | **Prerequisites** limited telepathy |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/21` | 0.667022 | **Prerequisites** limited telepathy |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/23` | 0.667022 | **Prerequisites** limited telepathy |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/22` | 0.554581 | **DISTANT TELEPATH** **FEAT 1** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/19` | 0.554581 | **DISTANT TELEPATH** **FEAT 1** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/26` | 0.538674 | Whether through training or innate talent, you've expanded  the range at which you can telepathically communicate.  Increase the range of your limited telepathy by 15 feet. |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/10/Text/23` | 0.526674 | Whether through training or innate talent,  you've expanded the range at which you can  telepathically communicate. Increase the range of  your limited telepathy by 15 feet. |

### Query 10
- Text: What is the rule about You can communicate mentally with creatures within 30 feet. You can communicate only with creatures that share a language with you. This doesn't give you any access to their thoughts and communicates no more information than normal speech would.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/0/Text/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/0/Text/13', 'PZO22001 Starfinder Player Core 058-073::/page/8/Text/15', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/16']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/0/Text/13` | 0.991225 | You can communicate mentally with creatures within 30 feet. You can communicate only with creatures that share a language with you. This doesn't give you any access to their thoughts and communicates |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/8/Text/15` | 0.991225 | You can communicate mentally with creatures within 30 feet. You can communicate only with creatures that share a language with you. This doesn't give you any access to their thoughts and communicates |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/16` | 0.632789 | Your antennae are covered in fine hairs that make them  more sensitive to psychic vibrations than most. You gain  thoughtsense as a vague sense with a range of 30 feet. This  means you can use your an |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/22` | 0.584190 | When you use limited telepathy to communicate with another  creature, you act as a conduit for their thoughts, allowing them  to respond to you for a few scant moments—if they wish. The  creature can |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/25` | 0.555713 | Your telepathy is stronger than most shirrens', allowing you to  combine physical, verbal, and telepathic communication. You  can transmit emotions alongside your messages whenever  you use limited te |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/26` | 0.549598 | Whether through training or innate talent, you've expanded  the range at which you can telepathically communicate.  Increase the range of your limited telepathy by 15 feet. |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/10/Text/23` | 0.549598 | Whether through training or innate talent,  you've expanded the range at which you can  telepathically communicate. Increase the range of  your limited telepathy by 15 feet. |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/41` | 0.524417 | You never let the inability to communicate stop you from  chatting with nufriends! You gain *speak with animals* as  a 2nd-rank primal innate spell, and *speak with plants* and  *translate* as 3rd-ran |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/24` | 0.523325 | When you use limited telepathy to communicate with another  creature, the creature can give you a brief response as a reaction,  or as a free action at the beginning of their next turn. |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/46` | 0.474885 | Your mastery of language reaches supernatural levels. You can  cast *truespeech* as a 5th-rank occult innate spell once per day on  yourself only. You gain a +1 status bonus to Diplomacy checks  for t |

### Query 11
- Text: What is the rule about Constantly strive to improve yourself through practicing  skills and honing your powers.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/1/ListItem/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/1/ListItem/2', 'PZO22001 Starfinder Player Core 058-073::/page/6/Text/14', 'PZO22001 Starfinder Player Core 058-073::/page/2/Text/31']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/1/ListItem/2` | 0.873505 | Constantly strive to improve yourself through practicing  skills and honing your powers. |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/6/Text/14` | 0.520990 | You push yourself to be the best by competing with the  triggering ally. Until the end of your next turn, you can attempt  the same skill check to perform the same action or activity  that the trigger |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/31` | 0.505056 | You've studied the lives and achievements of other  lashuntas who have improved both their psychic powers  and their communities. You gain the trained proficiency  rank in Occultism and Society. If yo |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/4` | 0.456240 | Your ability to adapt to various beliefs instills you with  knowledge of many cultures. You gain the trained proficiency  rank in Diplomacy and Society. If you would automatically  become trained in o |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/1/ListItem/6` | 0.449140 | Think you're a perfectionist and find your pursuit of  self-improvement tiresome. |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/20` | 0.447044 | **Popular Edicts** become the best version of yourself, never stop  learning, train your mind or body daily |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/1` | 0.420518 | performing arts. You gain the trained proficiency rank in  Acrobatics and Performance. If you would automatically become  trained in one of those skills (from your background or class, for  example), |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/51` | 0.418270 | You've continued to advance your powers using your  unconventional weapon. Whenever you gain a class feature  that grants you expert or greater proficiency in certain  weapons, you also gain that prof |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/59` | 0.404767 | You put forth your best effort and focus everything you've  got on the task at hand, putting allsix of your hands (three  of your sets of arms) into it! The next time you roll an attack  roll or skill |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/1/ListItem/4` | 0.403930 | Hold yourself to a much higher standard than you  apply to others. |

### Query 12
- Text: What is the rule about Prioritize learning and diplomacy if you're a damaya, or  physique and tactical prowess if you're a korasha—or if  you're an unbound lashunta, you have different priorities.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/1/ListItem/3']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/1/ListItem/3', 'PZO22001 Starfinder Player Core 058-073::/page/1/Text/25', 'PZO22001 Starfinder Player Core 058-073::/page/2/Text/31']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/1/ListItem/3` | 0.985610 | Prioritize learning and diplomacy if you're a damaya, or  physique and tactical prowess if you're a korasha—or if  you're an unbound lashunta, you have different priorities. |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/25` | 0.640009 | You've chosen the adaptive genetics to become a damaya. You  might have a leaner, lither body type than other lashuntas and  are likely encouraged to pursue work as a scholar or politician.  In additi |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/31` | 0.569001 | You've studied the lives and achievements of other  lashuntas who have improved both their psychic powers  and their communities. You gain the trained proficiency  rank in Occultism and Society. If yo |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/13` | 0.521964 | Around puberty, lashuntas traditionally choose whether  to express damaya or korasha genetics—a decision that  determines their physical development and influences their  potential societal roles. Las |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/27` | 0.510198 | You've chosen the adaptive genetics to become a korasha. You  might be stockier and more muscular than other lashuntas. |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/12` | 0.508387 | Damayas tend to be tall and graceful with delicate features and  are traditionally pushed toward artistic or intellectual pursuits  and political occupations. Korashas are shorter, more muscular,  and |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/3` | 0.506280 | You decided against activating your ancestry's adaptive  genetics. You might show a combination of damaya and  korasha traits; you might be tall and muscular or short and  lithe, or perhaps you have u |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/4` | 0.501477 | Your ability to adapt to various beliefs instills you with  knowledge of many cultures. You gain the trained proficiency  rank in Diplomacy and Society. If you would automatically  become trained in o |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/8` | 0.500525 | **Prerequisites** korasha lashunta or unbound lashunta heritage You can leverage your telepathic abilities to influence the  minds of others, imparting orders or inflaming fears. You can  cast *comman |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/14/Text/32` | 0.499286 | You're gregarious and friendly but also passionately  interested in the history of your people, going out of  your way to learn traditional stories and unearth  lost secrets. You gain the trained prof |

### Query 13
- Text: Summarize Hold yourself to a much higher standard than you  apply to others.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/1/ListItem/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/1/ListItem/4', 'PZO22001 Starfinder Player Core 058-073::/page/1/ListItem/2', 'PZO22001 Starfinder Player Core 058-073::/page/13/ListItem/8']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/1/ListItem/4` | 1.012450 | Hold yourself to a much higher standard than you  apply to others. |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/1/ListItem/2` | 0.540570 | Constantly strive to improve yourself through practicing  skills and honing your powers. |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/13/ListItem/8` | 0.478899 | Assume you're flighty or unreliable and that you don't  take yourself seriously. |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/14/Text/28` | 0.423166 | You're full of energy, and you often bound into action faster  than your friends can keep up. Your Speed increases by 5  feet. |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/4` | 0.423106 | Your ability to adapt to various beliefs instills you with  knowledge of many cultures. You gain the trained proficiency  rank in Diplomacy and Society. If you would automatically  become trained in o |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/5/ListItem/4` | 0.419102 | Hold true to your ancestral traditions and refuse to  kneel to cruel despots. |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/20` | 0.418058 | **Popular Edicts** become the best version of yourself, never stop  learning, train your mind or body daily |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/59` | 0.409141 | You put forth your best effort and focus everything you've  got on the task at hand, putting allsix of your hands (three  of your sets of arms) into it! The next time you roll an attack  roll or skill |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/1/ListItem/8` | 0.406660 | Idealize or label you based on your genetic expression. |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/25` | 0.398662 | You've learned to compensate for your hypersensitivity to  sound. You gain sonic resistance equal to half your level. If you  roll a success on a saving throw against a sonic effect, you get  a critic |

### Query 14
- Text: Summarize OTHERS PROBABLY...
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/1/SectionHeader/5']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/9/SectionHeader/5', 'PZO22001 Starfinder Player Core 058-073::/page/1/SectionHeader/5', 'PZO22001 Starfinder Player Core 058-073::/page/13/SectionHeader/5']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/9/SectionHeader/5` | 0.892334 | OTHERS PROBABLY... |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/1/SectionHeader/5` | 0.892334 | OTHERS PROBABLY... |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/13/SectionHeader/5` | 0.892334 | OTHERS PROBABLY... |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/5/SectionHeader/5` | 0.850334 | OTHERS PROBABLY... |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/67` | 0.304825 | **ANCESTRIES & ** **BACKGROUNDS** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/64` | 0.304825 | **ANCESTRIES & ** **BACKGROUNDS** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/30` | 0.304825 | **ANCESTRIES & ** **BACKGROUNDS** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/30` | 0.304825 | **ANCESTRIES & ** **BACKGROUNDS** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/31` | 0.304825 | **ANCESTRIES & ** **BACKGROUNDS** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/58` | 0.304825 | **ANCESTRIES & ** **BACKGROUNDS** |

### Query 15
- Text: Summarize Think you're a perfectionist and find your pursuit of  self-improvement tiresome.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/1/ListItem/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/1/ListItem/6', 'PZO22001 Starfinder Player Core 058-073::/page/1/ListItem/2', 'PZO22001 Starfinder Player Core 058-073::/page/13/ListItem/8']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/1/ListItem/6` | 1.031767 | Think you're a perfectionist and find your pursuit of  self-improvement tiresome. |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/1/ListItem/2` | 0.545033 | Constantly strive to improve yourself through practicing  skills and honing your powers. |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/13/ListItem/8` | 0.482967 | Assume you're flighty or unreliable and that you don't  take yourself seriously. |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/10` | 0.373573 | You're a master improviser with a bit of talent at everything even if you have no idea what you're doing. You gain the  Untrained Improvisation general feat. In addition, you gain  the Beginner's Luck |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/13/ListItem/2` | 0.373270 | Love to help others, perhaps even prioritizing their  needs over your own or feeling anxiety when you  can't offer assistance. |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/21` | 0.371633 | **Popular Anathema** neglect your goals, wallow in failure |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/5/ListItem/8` | 0.368830 | Assume you're looking for an excuse to prove yourself  in a fight. |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/14/Text/32` | 0.364771 | You're gregarious and friendly but also passionately  interested in the history of your people, going out of  your way to learn traditional stories and unearth  lost secrets. You gain the trained prof |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/13/ListItem/7` | 0.362078 | Expect you to want to help them and act surprised if  you don't. |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/1/ListItem/4` | 0.358971 | Hold yourself to a much higher standard than you  apply to others. |

### Query 16
- Text: Summarize Distrust your psychic abilities, fearing you'll read their  minds.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/1/ListItem/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/1/ListItem/7', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/27', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/16']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/1/ListItem/7` | 1.023839 | Distrust your psychic abilities, fearing you'll read their  minds. |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/27` | 0.569317 | Your psychic training allows you to block attempts to read  your thoughts. Any effect that specifically attempts to read  your mind to glean information must succeed at a counteract  check against the |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/16` | 0.519997 | Your antennae are covered in fine hairs that make them  more sensitive to psychic vibrations than most. You gain  thoughtsense as a vague sense with a range of 30 feet. This  means you can use your an |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/58` | 0.475635 | You can shield your mind by using similar techniques that  your ancestors once mastered to escape the Swarm. You block  the intruding effect by scattering your thoughts, making you  immune to the trig |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/43` | 0.467671 | You can use your telepathic abilities to quickly assess your  circumstances or subtly glean information from the minds of  others. You can cast *hypercognition* and *mind reading* as 3rdrank occult in |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/56` | 0.466446 | When a foe Casts a Spell that has the mental trait and you can  see or otherwise detect its manifestations, you use your psychic  powers to disrupt it. You expend 1 Focus Point to counter the  trigger |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/57` | 0.446648 | **Trigger** You're targeted by a mental effect. |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/9/ListItem/8` | 0.440125 | Are disconcerted by your insectile physiology and  telepathy. |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/8/Text/15` | 0.438625 | You can communicate mentally with creatures within 30 feet. You can communicate only with creatures that share a language with you. This doesn't give you any access to their thoughts and communicates |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/0/Text/13` | 0.438625 | You can communicate mentally with creatures within 30 feet. You can communicate only with creatures that share a language with you. This doesn't give you any access to their thoughts and communicates |

### Query 17
- Text: Summarize Idealize or label you based on your genetic expression.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/1/ListItem/8']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/1/ListItem/8', 'PZO22001 Starfinder Player Core 058-073::/page/2/Text/3', 'PZO22001 Starfinder Player Core 058-073::/page/12/Text/9']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/1/ListItem/8` | 1.014155 | Idealize or label you based on your genetic expression. |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/3` | 0.475082 | You decided against activating your ancestry's adaptive  genetics. You might show a combination of damaya and  korasha traits; you might be tall and muscular or short and  lithe, or perhaps you have u |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/12/Text/9` | 0.455301 | Additional languages equal to your Intelligence modifier (if it's positive). Choose from the list of common languages and any other languages to which you have access (such as the languages prevalent |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/4/Text/11` | 0.413301 | Additional languages equal to your Intelligence modifier (if it's positive). Choose from the list of common languages and any other languages to which you have access (such as the languages prevalent |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/0/Text/9` | 0.413301 | Additional languages equal to your Intelligence modifier (if it's positive). Choose from the list of common languages and any other languages to which you have access (such as the languages prevalent |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/8/Text/11` | 0.409761 | One regional language of your choice Additional languages equal to your Intelligence modifier (if it's positive). Choose from the list of common languages and any other languages to which you have acc |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/27` | 0.401120 | You've chosen the adaptive genetics to become a korasha. You  might be stockier and more muscular than other lashuntas. |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/13/ListItem/6` | 0.390440 | Are in awe of your boundless energy, enthusiasm, and  positivity (or another emotion you express most often). |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/1/ListItem/4` | 0.389661 | Hold yourself to a much higher standard than you  apply to others. |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/25` | 0.381101 | You've chosen the adaptive genetics to become a damaya. You  might have a leaner, lither body type than other lashuntas and  are likely encouraged to pursue work as a scholar or politician.  In additi |

### Query 18
- Text: What is the rule about Lashuntas are natural psychics with adaptive genetics who  traditionally develop into one of two heritages at puberty:  damayas or korashas. They have a well-earned reputation for  being charismatic, driven, and self-reflective, with a perpetual  desire for growth—both in terms of personal advancement and  self-improvement. This cultural push to know oneself, embrace  one's strengths, surpass one's past successes, and strive for evergreater goals drives lashuntas to value education, focus, and  training as well as to explore new discoveries, technologies, and  modes of thought. While many lashuntas today still fulfill the  traditional role of the enlightened warrior or the consummate  scholar, time and shifting social norms have gifted lashuntas  the freedom to branch out in countless ways, developing their  own interests, hobbies, and genetic expressions, with no regard  to their heritage or societal standing.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/9', 'PZO22001 Starfinder Player Core 058-073::/page/1/Text/13', 'PZO22001 Starfinder Player Core 058-073::/page/0/Text/2']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/9` | 1.013160 | Lashuntas are natural psychics with adaptive genetics who  traditionally develop into one of two heritages at puberty:  damayas or korashas. They have a well-earned reputation for  being charismatic, |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/13` | 0.846425 | Around puberty, lashuntas traditionally choose whether  to express damaya or korasha genetics—a decision that  determines their physical development and influences their  potential societal roles. Las |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/0/Text/2` | 0.821921 | Long ago, lashuntas evolved psychic abilities and a unique dimorphism that helped them survive on their home world of Castrovel. In modern times, lashuntas manipulate their own genetics at puberty, al |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/12` | 0.737943 | Damayas tend to be tall and graceful with delicate features and  are traditionally pushed toward artistic or intellectual pursuits  and political occupations. Korashas are shorter, more muscular,  and |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/19` | 0.645934 | Lashunta cultures value education, self-improvement, and  community defense. Religious lashuntas tend to identify with  faiths that encourage balance, knowledge, meditative practice,  and seeking enli |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/23` | 0.641085 | Around puberty, many lashuntas choose to embrace a genetic  path that determines their physiology and role in society.  Choose one of the following lashunta heritages at 1st level. |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/27` | 0.638947 | You've chosen the adaptive genetics to become a korasha. You  might be stockier and more muscular than other lashuntas. |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/25` | 0.622189 | You've chosen the adaptive genetics to become a damaya. You  might have a leaner, lither body type than other lashuntas and  are likely encouraged to pursue work as a scholar or politician.  In additi |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/31` | 0.602176 | You've studied the lives and achievements of other  lashuntas who have improved both their psychic powers  and their communities. You gain the trained proficiency  rank in Occultism and Society. If yo |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/10` | 0.598829 | If you want to play a character who strives for selfimprovement and has innate psychic abilities, you should play  a lashunta. |

### Query 19
- Text: What is the rule about If you want to play a character who strives for selfimprovement and has innate psychic abilities, you should play  a lashunta.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/10', 'PZO22001 Starfinder Player Core 058-073::/page/2/Text/7', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/8']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/10` | 0.952650 | If you want to play a character who strives for selfimprovement and has innate psychic abilities, you should play  a lashunta. |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/7` | 0.651278 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As a lashunta, you choose from among  the following |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/8` | 0.646887 | **Prerequisites** korasha lashunta or unbound lashunta heritage You can leverage your telepathic abilities to influence the  minds of others, imparting orders or inflaming fears. You can  cast *comman |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/0/Text/2` | 0.576554 | Long ago, lashuntas evolved psychic abilities and a unique dimorphism that helped them survive on their home world of Castrovel. In modern times, lashuntas manipulate their own genetics at puberty, al |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/31` | 0.574458 | You've studied the lives and achievements of other  lashuntas who have improved both their psychic powers  and their communities. You gain the trained proficiency  rank in Occultism and Society. If yo |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/12` | 0.555068 | **Prerequisites** damaya lashunta or unbound lashunta heritage You can transfer vast amounts of information to the minds of  others in mere moments. You can cast *mindlink* as a 1st-rank  occult innat |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/52` | 0.531903 | **LASHUNTA** **MENTAL** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/9` | 0.531761 | Lashuntas are natural psychics with adaptive genetics who  traditionally develop into one of two heritages at puberty:  damayas or korashas. They have a well-earned reputation for  being charismatic, |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/25` | 0.527838 | You've chosen the adaptive genetics to become a damaya. You  might have a leaner, lither body type than other lashuntas and  are likely encouraged to pursue work as a scholar or politician.  In additi |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/0/SectionHeader/1` | 0.513351 | LASHUNTA |

### Query 20
- Text: Summarize PHYSICAL DESCRIPTION
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/1/SectionHeader/11']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/5/SectionHeader/11', 'PZO22001 Starfinder Player Core 058-073::/page/1/SectionHeader/11', 'PZO22001 Starfinder Player Core 058-073::/page/9/SectionHeader/11']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/5/SectionHeader/11` | 0.971851 | PHYSICAL DESCRIPTION |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/1/SectionHeader/11` | 0.971851 | PHYSICAL DESCRIPTION |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/9/SectionHeader/11` | 0.971851 | PHYSICAL DESCRIPTION |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/13/SectionHeader/12` | 0.929851 | PHYSICAL DESCRIPTION |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/63` | 0.335394 | **INTRODUCTION** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/65` | 0.335394 | **INTRODUCTION** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/13/Text/30` | 0.335394 | **INTRODUCTION** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/29` | 0.335394 | **INTRODUCTION** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/30` | 0.335394 | **INTRODUCTION** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/66` | 0.335394 | **INTRODUCTION** |

### Query 21
- Text: What is the rule about Damayas tend to be tall and graceful with delicate features and  are traditionally pushed toward artistic or intellectual pursuits  and political occupations. Korashas are shorter, more muscular,  and gravitate toward military service, manual labor, and wartime  leadership. Regardless of heritage, all lashuntas have short  forehead antennae that focus their telepathy, with colorful  bumps and facial markings unique to each individual. Lashuntas  produce pheromones that subtly broadcast their moods in ways  that other ancestries might find alluring or unnerving.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/12']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/12', 'PZO22001 Starfinder Player Core 058-073::/page/1/Text/9', 'PZO22001 Starfinder Player Core 058-073::/page/1/Text/13']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/12` | 1.014594 | Damayas tend to be tall and graceful with delicate features and  are traditionally pushed toward artistic or intellectual pursuits  and political occupations. Korashas are shorter, more muscular,  and |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/9` | 0.787603 | Lashuntas are natural psychics with adaptive genetics who  traditionally develop into one of two heritages at puberty:  damayas or korashas. They have a well-earned reputation for  being charismatic, |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/13` | 0.716604 | Around puberty, lashuntas traditionally choose whether  to express damaya or korasha genetics—a decision that  determines their physical development and influences their  potential societal roles. Las |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/27` | 0.646534 | You've chosen the adaptive genetics to become a korasha. You  might be stockier and more muscular than other lashuntas. |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/1/ListItem/3` | 0.627269 | Prioritize learning and diplomacy if you're a damaya, or  physique and tactical prowess if you're a korasha—or if  you're an unbound lashunta, you have different priorities. |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/0/Text/2` | 0.611627 | Long ago, lashuntas evolved psychic abilities and a unique dimorphism that helped them survive on their home world of Castrovel. In modern times, lashuntas manipulate their own genetics at puberty, al |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/3` | 0.611451 | You decided against activating your ancestry's adaptive  genetics. You might show a combination of damaya and  korasha traits; you might be tall and muscular or short and  lithe, or perhaps you have u |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/25` | 0.609973 | You've chosen the adaptive genetics to become a damaya. You  might have a leaner, lither body type than other lashuntas and  are likely encouraged to pursue work as a scholar or politician.  In additi |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/23` | 0.563621 | Around puberty, many lashuntas choose to embrace a genetic  path that determines their physiology and role in society.  Choose one of the following lashunta heritages at 1st level. |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/17` | 0.491321 | **Sample Names:** Lashunta naming conventions often use  tonal elements. Some sample lashunta names are Domash,  Hesori, Imaaz, Kima, Kopalo, Maenala, Nomae, Oraeus, Raia,  Shess, Soryn, Stretto, Taeo |

### Query 22
- Text: What is the rule about Around puberty, lashuntas traditionally choose whether  to express damaya or korasha genetics—a decision that  determines their physical development and influences their  potential societal roles. Lashuntas achieve their choice through  a combination of psychic rituals and gene therapy. Today,  many young lashuntas have chosen to tread their own path  and abstain from this choice, instead becoming "unbound."  Unbound lashuntas defy traditional roles and labels, and they  might express traits and innate proclivities common to both  of or neither of these groups. A growing minority of lashuntas  instead pushes for further genetic diversification and aims to  express unique or long-buried genetic permutations, pioneering  entirely new chosen heritages. Whether such experimentation  will prove fruitful remains to be seen.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/13', 'PZO22001 Starfinder Player Core 058-073::/page/1/Text/9', 'PZO22001 Starfinder Player Core 058-073::/page/0/Text/2']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/13` | 1.028709 | Around puberty, lashuntas traditionally choose whether  to express damaya or korasha genetics—a decision that  determines their physical development and influences their  potential societal roles. Las |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/9` | 0.812245 | Lashuntas are natural psychics with adaptive genetics who  traditionally develop into one of two heritages at puberty:  damayas or korashas. They have a well-earned reputation for  being charismatic, |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/0/Text/2` | 0.776097 | Long ago, lashuntas evolved psychic abilities and a unique dimorphism that helped them survive on their home world of Castrovel. In modern times, lashuntas manipulate their own genetics at puberty, al |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/23` | 0.681329 | Around puberty, many lashuntas choose to embrace a genetic  path that determines their physiology and role in society.  Choose one of the following lashunta heritages at 1st level. |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/12` | 0.664264 | Damayas tend to be tall and graceful with delicate features and  are traditionally pushed toward artistic or intellectual pursuits  and political occupations. Korashas are shorter, more muscular,  and |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/3` | 0.642413 | You decided against activating your ancestry's adaptive  genetics. You might show a combination of damaya and  korasha traits; you might be tall and muscular or short and  lithe, or perhaps you have u |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/27` | 0.630788 | You've chosen the adaptive genetics to become a korasha. You  might be stockier and more muscular than other lashuntas. |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/1/ListItem/3` | 0.594043 | Prioritize learning and diplomacy if you're a damaya, or  physique and tactical prowess if you're a korasha—or if  you're an unbound lashunta, you have different priorities. |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/25` | 0.589198 | You've chosen the adaptive genetics to become a damaya. You  might have a leaner, lither body type than other lashuntas and  are likely encouraged to pursue work as a scholar or politician.  In additi |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/19` | 0.530115 | Lashunta cultures value education, self-improvement, and  community defense. Religious lashuntas tend to identify with  faiths that encourage balance, knowledge, meditative practice,  and seeking enli |

### Query 23
- Text: Summarize SOCIETY
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/1/SectionHeader/14']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/9/SectionHeader/14', 'PZO22001 Starfinder Player Core 058-073::/page/13/SectionHeader/14', 'PZO22001 Starfinder Player Core 058-073::/page/1/SectionHeader/14']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/9/SectionHeader/14` | 0.897896 | SOCIETY |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/13/SectionHeader/14` | 0.897896 | SOCIETY |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/1/SectionHeader/14` | 0.897896 | SOCIETY |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/5/SectionHeader/14` | 0.855896 | SOCIETY |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/13/Text/15` | 0.378435 | Skittermander societies don't create governments, laws, or  rules, yet residents naturally help each other, forming freeform independent communities or joining neighboring societies.  Communities are |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/13` | 0.331672 | **COMMUNALISM **[reaction] **FEAT 1** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/78` | 0.314547 | **Languages** **CLASSES** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/44` | 0.314547 | **Languages** **CLASSES** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/15` | 0.314239 | Shirrens value individual choice and rights, having escaped  from the Swarm thanks to an adaptation to their physiology  that causes pleasure when they make choices for themselves.  Shirren culture is |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/41` | 0.308308 | **Prerequisites** Communalism |

### Query 24
- Text: Summarize Since time immemorial, lashuntas have dwelled in sprawling,
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/15']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/15', 'PZO22001 Starfinder Player Core 058-073::/page/0/Text/2', 'PZO22001 Starfinder Player Core 058-073::/page/1/Text/9']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/15` | 1.029482 | Since time immemorial, lashuntas have dwelled in sprawling, |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/0/Text/2` | 0.645873 | Long ago, lashuntas evolved psychic abilities and a unique dimorphism that helped them survive on their home world of Castrovel. In modern times, lashuntas manipulate their own genetics at puberty, al |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/9` | 0.583962 | Lashuntas are natural psychics with adaptive genetics who  traditionally develop into one of two heritages at puberty:  damayas or korashas. They have a well-earned reputation for  being charismatic, |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/1/SectionHeader/22` | 0.516470 | LASHUNTA HERITAGES |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/13` | 0.509863 | Around puberty, lashuntas traditionally choose whether  to express damaya or korasha genetics—a decision that  determines their physical development and influences their  potential societal roles. Las |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/23` | 0.501389 | Around puberty, many lashuntas choose to embrace a genetic  path that determines their physiology and role in society.  Choose one of the following lashunta heritages at 1st level. |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/13/Text/35` | 0.492655 | **Lashunta** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/34` | 0.492654 | **Lashunta** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/62` | 0.492654 | **Lashunta** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/72` | 0.492654 | **Lashunta** |

### Query 25
- Text: Summarize picturesque cities along the shores and wildlands of Castrovel,  a lush jungle world teeming with dangerous predators and  extreme weather. These independent settlements are protected  by a mighty military caste of psychic warriors, technological  defenses, and magical countermeasures. The most iconic of  these soldiers are the shotalashu cavalry, lightly armored riders  who form telepathic bonds with (and take their name from)  their saurian mounts.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/16']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/16', 'PZO22001 Starfinder Player Core 058-073::/page/5/Text/9', 'PZO22001 Starfinder Player Core 058-073::/page/0/Text/2']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/16` | 1.045067 | picturesque cities along the shores and wildlands of Castrovel,  a lush jungle world teeming with dangerous predators and  extreme weather. These independent settlements are protected  by a mighty mil |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/9` | 0.536912 | Pahtras evolved on a low-gravity jungle world called Pulonis,  where they fought a long war for independence from their  Veskarium conquerors. Recently, pahtra freedom fighters  defeated the last Vesk |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/0/Text/2` | 0.531616 | Long ago, lashuntas evolved psychic abilities and a unique dimorphism that helped them survive on their home world of Castrovel. In modern times, lashuntas manipulate their own genetics at puberty, al |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/20` | 0.424979 | Many pahtras cling fiercely to their ancestral Pulonian  traditions in an effort to keep their cultures alive after  enduring generations of oppression by the Veskarium.  Pulonian culture values perso |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/8/Text/2` | 0.423968 | The insectile shirrens split from the destructive Swarm, forsaking the ruthless hive mind to pursue personal freedom and end the cycle of interstellar violence. Shirrens are a species of telepaths dev |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/9` | 0.422618 | Shirrens were originally members of the Swarm, a collection  of colonies controlled by a hive mind that devoured entire  planets. In time, shirrens gained a sense of individual self  and rejected the |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/15` | 0.405000 | Since time immemorial, lashuntas have dwelled in sprawling, |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/12` | 0.402620 | Damayas tend to be tall and graceful with delicate features and  are traditionally pushed toward artistic or intellectual pursuits  and political occupations. Korashas are shorter, more muscular,  and |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/4/Text/2` | 0.402456 | Pahtras are a humanoid feline species from a nearby star system. They're highly competitive and known for their achievements in magic, music, and war. Their home world was recently freed from the Vesk |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/15` | 0.399474 | Pahtra cultures are steeped in tradition and highly competitive,  with individuals vying for recognition and resources in a  struggle that mimics the harsh natural order of their planet.  Before the V |

### Query 26
- Text: Summarize **Sample Names:** Lashunta naming conventions often use  tonal elements. Some sample lashunta names are Domash,  Hesori, Imaaz, Kima, Kopalo, Maenala, Nomae, Oraeus, Raia,  Shess, Soryn, Stretto, Taeon, and Varikuara.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/17']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/17', 'PZO22001 Starfinder Player Core 058-073::/page/5/Text/18', 'PZO22001 Starfinder Player Core 058-073::/page/13/Text/18']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/17` | 1.045305 | **Sample Names:** Lashunta naming conventions often use  tonal elements. Some sample lashunta names are Domash,  Hesori, Imaaz, Kima, Kopalo, Maenala, Nomae, Oraeus, Raia,  Shess, Soryn, Stretto, Taeo |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/18` | 0.688808 | **Sample Names:** Traditional pahtra names contain  auspicious elements determined by a mystic. Pahtra names  include Cahnex, Dae, Fetenekku, Hafoumei, Ifset, Ihrasara,  Jeviish, Khieper, Lealorn, Mah |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/13/Text/18` | 0.658926 | **Sample Names:** Ayoka, Baazo, Bixby, Dakoyo, Fipzul, Gazigaz,  Jomp, Kayoko, Kimikim, Mimzy, Nako, Prismacora, Quonx,  Rudfuz, Sprax, Timinim, Tipps, Tonkona, Viverivim |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/16` | 0.552803 | **Sample Names:** Shirrens rely primarily on telepathy for  communication and have a secret "soul-name" that's purely  thought-based. Shirrens readily accept nicknames bestowed  by their companions. S |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/68` | 0.517186 | **Kasatha** **Lashunta** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/34` | 0.517186 | **Kasatha** **Lashunta** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/7` | 0.506506 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As a lashunta, you choose from among  the following |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/13/Text/17` | 0.491395 | A skittermander adds to their name as they age and pass  certain milestones. A name begins very short, usually no more  than one syllable. New syllables are added with the passing of  time or whenever |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/12` | 0.484512 | Damayas tend to be tall and graceful with delicate features and  are traditionally pushed toward artistic or intellectual pursuits  and political occupations. Korashas are shorter, more muscular,  and |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/17` | 0.479664 | Cesca, Chk Chk, Halicon, Izenzi, Jchk, J'scib, Keskodai, Kinnik,  Korskal, Philt, Schect, Thast, T'sen, Xylit, Zenka, and Zigvigix. |

### Query 27
- Text: Summarize BELIEFS
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/1/SectionHeader/18']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/1/SectionHeader/18', 'PZO22001 Starfinder Player Core 058-073::/page/9/SectionHeader/18', 'PZO22001 Starfinder Player Core 058-073::/page/13/SectionHeader/19']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/1/SectionHeader/18` | 0.920612 | BELIEFS |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/9/SectionHeader/18` | 0.920612 | BELIEFS |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/13/SectionHeader/19` | 0.920612 | BELIEFS |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/5/SectionHeader/19` | 0.878612 | BELIEFS |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/28` | 0.282773 | **Rebellious** **Defiance** [one-action] (mental) **Frequency** once per day;  **Effect** You decry one foe within 100 feet that you can see as  a tyrant or villain and prepare yourself to defy them, |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/1/ListItem/8` | 0.279710 | Idealize or label you based on your genetic expression. |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/4` | 0.268113 | Your ability to adapt to various beliefs instills you with  knowledge of many cultures. You gain the trained proficiency  rank in Diplomacy and Society. If you would automatically  become trained in o |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/13/Text/21` | 0.266904 | **Popular Edicts** be kind, help others, respect and nurture living  beings |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/13/ListItem/6` | 0.265193 | Are in awe of your boundless energy, enthusiasm, and  positivity (or another emotion you express most often). |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/83` | 0.264875 | **SKILLS** **FEATS** |

### Query 28
- Text: What is the rule about Lashunta cultures value education, self-improvement, and  community defense. Religious lashuntas tend to identify with  faiths that encourage balance, knowledge, meditative practice,  and seeking enlightenment, such as Eloritu, Ibra, or Yaraesa.  Other lashuntas shun religion entirely in favor of adopting a  philosophy like the Cycle or the Green Faith, honoring a state  leader, or following historic community traditions.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/19']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/19', 'PZO22001 Starfinder Player Core 058-073::/page/1/Text/9', 'PZO22001 Starfinder Player Core 058-073::/page/2/Text/31']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/19` | 1.008849 | Lashunta cultures value education, self-improvement, and  community defense. Religious lashuntas tend to identify with  faiths that encourage balance, knowledge, meditative practice,  and seeking enli |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/9` | 0.649712 | Lashuntas are natural psychics with adaptive genetics who  traditionally develop into one of two heritages at puberty:  damayas or korashas. They have a well-earned reputation for  being charismatic, |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/31` | 0.586441 | You've studied the lives and achievements of other  lashuntas who have improved both their psychic powers  and their communities. You gain the trained proficiency  rank in Occultism and Society. If yo |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/0/Text/2` | 0.536475 | Long ago, lashuntas evolved psychic abilities and a unique dimorphism that helped them survive on their home world of Castrovel. In modern times, lashuntas manipulate their own genetics at puberty, al |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/13` | 0.532750 | Around puberty, lashuntas traditionally choose whether  to express damaya or korasha genetics—a decision that  determines their physical development and influences their  potential societal roles. Las |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/10` | 0.525657 | If you want to play a character who strives for selfimprovement and has innate psychic abilities, you should play  a lashunta. |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/19` | 0.512618 | Shirrens define themselves by their choices and bristle against  all forms of oppression. They enjoy cultural exchange, and  while most eagerly adopt the deities and practices of other  communities, o |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/1/ListItem/3` | 0.512285 | Prioritize learning and diplomacy if you're a damaya, or  physique and tactical prowess if you're a korasha—or if  you're an unbound lashunta, you have different priorities. |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/23` | 0.500073 | Around puberty, many lashuntas choose to embrace a genetic  path that determines their physiology and role in society.  Choose one of the following lashunta heritages at 1st level. |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/20` | 0.476628 | Many pahtras cling fiercely to their ancestral Pulonian  traditions in an effort to keep their cultures alive after  enduring generations of oppression by the Veskarium.  Pulonian culture values perso |

### Query 29
- Text: Summarize **Popular Edicts** become the best version of yourself, never stop  learning, train your mind or body daily
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/20']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/20', 'PZO22001 Starfinder Player Core 058-073::/page/9/Text/20', 'PZO22001 Starfinder Player Core 058-073::/page/5/Text/21']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/20` | 1.037736 | **Popular Edicts** become the best version of yourself, never stop  learning, train your mind or body daily |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/20` | 0.782080 | **Popular Edicts** make your own choices, try to solve problems  peacefully, work for the greater good of the group |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/21` | 0.756307 | **Popular Edicts** challenge yourself and your allies, perform  music and dance daily, take pride in your accomplishments **Popular Anathema** abandon your ancestral traditions, bow to  tyrants, give |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/13/Text/21` | 0.665436 | **Popular Edicts** be kind, help others, respect and nurture living  beings |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/1/ListItem/2` | 0.523753 | Constantly strive to improve yourself through practicing  skills and honing your powers. |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/21` | 0.449499 | **Popular Anathema** neglect your goals, wallow in failure |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/13/ListItem/6` | 0.418988 | Are in awe of your boundless energy, enthusiasm, and  positivity (or another emotion you express most often). |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/11` | 0.417766 | **Beginner's** **Luck** [free-action] (fortune) **Frequency** once per day;  **Trigger** You fail a skill check using a skill that you're  untrained in; **Effect** Reroll the triggering check and use |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/4` | 0.407374 | Your ability to adapt to various beliefs instills you with  knowledge of many cultures. You gain the trained proficiency  rank in Diplomacy and Society. If you would automatically  become trained in o |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/1/ListItem/4` | 0.399618 | Hold yourself to a much higher standard than you  apply to others. |

### Query 30
- Text: Summarize **Popular Anathema** neglect your goals, wallow in failure
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/21']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/21', 'PZO22001 Starfinder Player Core 058-073::/page/9/Text/21', 'PZO22001 Starfinder Player Core 058-073::/page/13/Text/22']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/21` | 1.030536 | **Popular Anathema** neglect your goals, wallow in failure |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/21` | 0.702738 | **Popular Anathema** inflict thoughtless destruction, take away  another's right to make choices |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/13/Text/22` | 0.688208 | **Popular Anathema** cause intentional harm without reason,  pollute the environment, refuse to help someone in dire need |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/21` | 0.633582 | **Popular Edicts** challenge yourself and your allies, perform  music and dance daily, take pride in your accomplishments **Popular Anathema** abandon your ancestral traditions, bow to  tyrants, give |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/20` | 0.503460 | **Popular Edicts** make your own choices, try to solve problems  peacefully, work for the greater good of the group |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/20` | 0.450594 | **Popular Edicts** become the best version of yourself, never stop  learning, train your mind or body daily |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/13/Text/21` | 0.430285 | **Popular Edicts** be kind, help others, respect and nurture living  beings |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/22` | 0.414654 | You fall utterly silent and focus strenuously on a problem  at hand. You attempt to Recall Knowledge with a +2  circumstance bonus to the skill check. If you would get a  critical failure, you get a f |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/1/ListItem/3` | 0.377093 | Prioritize learning and diplomacy if you're a damaya, or  physique and tactical prowess if you're a korasha—or if  you're an unbound lashunta, you have different priorities. |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/17` | 0.371798 | **Trigger** You fail a Will saving throw against a mental effect. You center your thoughts and focus your mind, shaking off  emotional turmoil and harmful mental intrusions. Reroll the  triggering sav |

### Query 31
- Text: Summarize LASHUNTA HERITAGES
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/1/SectionHeader/22']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/1/SectionHeader/22', 'PZO22001 Starfinder Player Core 058-073::/page/0/SectionHeader/1', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/20']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/1/SectionHeader/22` | 1.006130 | LASHUNTA HERITAGES |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/0/SectionHeader/1` | 0.836635 | LASHUNTA |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/20` | 0.757254 | **LASHUNTA** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/47` | 0.715254 | **LASHUNTA** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/15` | 0.715254 | **LASHUNTA** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/20` | 0.715254 | **LASHUNTA** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/2` | 0.715254 | **LASHUNTA** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/11` | 0.715254 | **LASHUNTA** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/7` | 0.715254 | **LASHUNTA** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/30` | 0.715254 | **LASHUNTA** |

### Query 32
- Text: What is the rule about Around puberty, many lashuntas choose to embrace a genetic  path that determines their physiology and role in society.  Choose one of the following lashunta heritages at 1st level.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/23']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/23', 'PZO22001 Starfinder Player Core 058-073::/page/1/Text/13', 'PZO22001 Starfinder Player Core 058-073::/page/0/Text/2']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/23` | 0.978198 | Around puberty, many lashuntas choose to embrace a genetic  path that determines their physiology and role in society.  Choose one of the following lashunta heritages at 1st level. |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/13` | 0.759561 | Around puberty, lashuntas traditionally choose whether  to express damaya or korasha genetics—a decision that  determines their physical development and influences their  potential societal roles. Las |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/0/Text/2` | 0.755956 | Long ago, lashuntas evolved psychic abilities and a unique dimorphism that helped them survive on their home world of Castrovel. In modern times, lashuntas manipulate their own genetics at puberty, al |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/7` | 0.646706 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As a lashunta, you choose from among  the following |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/9` | 0.636802 | Lashuntas are natural psychics with adaptive genetics who  traditionally develop into one of two heritages at puberty:  damayas or korashas. They have a well-earned reputation for  being charismatic, |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/25` | 0.585699 | You've chosen the adaptive genetics to become a damaya. You  might have a leaner, lither body type than other lashuntas and  are likely encouraged to pursue work as a scholar or politician.  In additi |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/12` | 0.582328 | Damayas tend to be tall and graceful with delicate features and  are traditionally pushed toward artistic or intellectual pursuits  and political occupations. Korashas are shorter, more muscular,  and |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/27` | 0.581434 | You've chosen the adaptive genetics to become a korasha. You  might be stockier and more muscular than other lashuntas. |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/10` | 0.571190 | If you want to play a character who strives for selfimprovement and has innate psychic abilities, you should play  a lashunta. |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/23` | 0.548317 | Pahtras have a variety of heritages throughout their species.  Choose one of the following pahtra heritages at 1st level. |

### Query 33
- Text: Summarize DAMAYA LASHUNTA
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/1/SectionHeader/24']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/1/SectionHeader/24', 'PZO22001 Starfinder Player Core 058-073::/page/0/SectionHeader/1', 'PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/11']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/1/SectionHeader/24` | 0.982943 | DAMAYA LASHUNTA |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/0/SectionHeader/1` | 0.730309 | LASHUNTA |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/11` | 0.672501 | **LASHUNTA** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/26` | 0.630501 | **LASHUNTA** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/30` | 0.630501 | **LASHUNTA** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/59` | 0.630501 | **LASHUNTA** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/11` | 0.630501 | **LASHUNTA** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/30` | 0.630501 | **LASHUNTA** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/20` | 0.630501 | **LASHUNTA** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/15` | 0.630501 | **LASHUNTA** |

### Query 34
- Text: What is the rule about You've chosen the adaptive genetics to become a damaya. You  might have a leaner, lither body type than other lashuntas and  are likely encouraged to pursue work as a scholar or politician.  In addition to what you gain from your ancestry, you gain  an attribute boost to Intelligence and an attribute flaw to  Constitution, but the free ancestry boost can't also be Intelligence.  You become trained in Diplomacy. If you would automatically  become trained in Diplomacy (from your background or class,  for example), you become trained in another skill of your choice.  You gain the Additional Lore general feat.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/25']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/25', 'PZO22001 Starfinder Player Core 058-073::/page/11/Text/4', 'PZO22001 Starfinder Player Core 058-073::/page/2/Text/3']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/25` | 1.008342 | You've chosen the adaptive genetics to become a damaya. You  might have a leaner, lither body type than other lashuntas and  are likely encouraged to pursue work as a scholar or politician.  In additi |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/4` | 0.686158 | Your ability to adapt to various beliefs instills you with  knowledge of many cultures. You gain the trained proficiency  rank in Diplomacy and Society. If you would automatically  become trained in o |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/3` | 0.685023 | You decided against activating your ancestry's adaptive  genetics. You might show a combination of damaya and  korasha traits; you might be tall and muscular or short and  lithe, or perhaps you have u |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/31` | 0.636483 | You've studied the lives and achievements of other  lashuntas who have improved both their psychic powers  and their communities. You gain the trained proficiency  rank in Occultism and Society. If yo |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/7` | 0.621840 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As a lashunta, you choose from among  the following |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/14/Text/32` | 0.620026 | You're gregarious and friendly but also passionately  interested in the history of your people, going out of  your way to learn traditional stories and unearth  lost secrets. You gain the trained prof |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/1/ListItem/3` | 0.619186 | Prioritize learning and diplomacy if you're a damaya, or  physique and tactical prowess if you're a korasha—or if  you're an unbound lashunta, you have different priorities. |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/32` | 0.600071 | You also gain the Additional Lore general feat for  Lashunta Lore. |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/27` | 0.589239 | You've chosen the adaptive genetics to become a korasha. You  might be stockier and more muscular than other lashuntas. |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/6/Text/7` | 0.584745 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As a pahtra, you choose from among the  following an |

### Query 35
- Text: Summarize KORASHA LASHUNTA
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/1/SectionHeader/26']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/1/SectionHeader/26', 'PZO22001 Starfinder Player Core 058-073::/page/0/SectionHeader/1', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/2']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/1/SectionHeader/26` | 1.001083 | KORASHA LASHUNTA |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/0/SectionHeader/1` | 0.755956 | LASHUNTA |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/2` | 0.722276 | **LASHUNTA** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/59` | 0.680276 | **LASHUNTA** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/20` | 0.680276 | **LASHUNTA** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/11` | 0.680276 | **LASHUNTA** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/20` | 0.680276 | **LASHUNTA** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/30` | 0.680276 | **LASHUNTA** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/11` | 0.680276 | **LASHUNTA** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/26` | 0.680276 | **LASHUNTA** |

### Query 36
- Text: Summarize You've chosen the adaptive genetics to become a korasha. You  might be stockier and more muscular than other lashuntas.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/27']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/27', 'PZO22001 Starfinder Player Core 058-073::/page/2/Text/3', 'PZO22001 Starfinder Player Core 058-073::/page/1/Text/12']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/27` | 1.038980 | You've chosen the adaptive genetics to become a korasha. You  might be stockier and more muscular than other lashuntas. |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/3` | 0.721797 | You decided against activating your ancestry's adaptive  genetics. You might show a combination of damaya and  korasha traits; you might be tall and muscular or short and  lithe, or perhaps you have u |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/12` | 0.676163 | Damayas tend to be tall and graceful with delicate features and  are traditionally pushed toward artistic or intellectual pursuits  and political occupations. Korashas are shorter, more muscular,  and |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/13` | 0.639616 | Around puberty, lashuntas traditionally choose whether  to express damaya or korasha genetics—a decision that  determines their physical development and influences their  potential societal roles. Las |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/9` | 0.632839 | Lashuntas are natural psychics with adaptive genetics who  traditionally develop into one of two heritages at puberty:  damayas or korashas. They have a well-earned reputation for  being charismatic, |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/25` | 0.631708 | You've chosen the adaptive genetics to become a damaya. You  might have a leaner, lither body type than other lashuntas and  are likely encouraged to pursue work as a scholar or politician.  In additi |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/0/Text/2` | 0.621125 | Long ago, lashuntas evolved psychic abilities and a unique dimorphism that helped them survive on their home world of Castrovel. In modern times, lashuntas manipulate their own genetics at puberty, al |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/1/ListItem/3` | 0.583927 | Prioritize learning and diplomacy if you're a damaya, or  physique and tactical prowess if you're a korasha—or if  you're an unbound lashunta, you have different priorities. |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/23` | 0.561496 | Around puberty, many lashuntas choose to embrace a genetic  path that determines their physiology and role in society.  Choose one of the following lashunta heritages at 1st level. |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/31` | 0.505287 | You've studied the lives and achievements of other  lashuntas who have improved both their psychic powers  and their communities. You gain the trained proficiency  rank in Occultism and Society. If yo |

### Query 37
- Text: Summarize **INTRODUCTION**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/29']
- Expected found: `True`
- Expected rank: `5`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/5/Text/29', 'PZO22001 Starfinder Player Core 058-073::/page/7/Text/57', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/63']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/29` | 0.880541 | **INTRODUCTION** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/57` | 0.880541 | **INTRODUCTION** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/63` | 0.880541 | **INTRODUCTION** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/30` | 0.838541 | **INTRODUCTION** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/29` | 0.838541 | **INTRODUCTION** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/66` | 0.838541 | **INTRODUCTION** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/65` | 0.838541 | **INTRODUCTION** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/13/Text/30` | 0.838541 | **INTRODUCTION** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/72` | 0.460996 | **Languages** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/81` | 0.460996 | **Languages** |

### Query 38
- Text: What is the rule about **ANCESTRIES & ** **BACKGROUNDS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/30']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/30', 'PZO22001 Starfinder Player Core 058-073::/page/5/Text/30', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/64']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/30` | 0.920820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/30` | 0.920820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/64` | 0.920820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/13/Text/31` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/31` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/67` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/66` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/58` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/43` | 0.526957 | **Backgrounds** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/43` | 0.526957 | **Backgrounds** |

### Query 39
- Text: Summarize **Android**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/31']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/9/Text/32', 'PZO22001 Starfinder Player Core 058-073::/page/1/Text/31', 'PZO22001 Starfinder Player Core 058-073::/page/5/Text/31']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/32` | 0.780962 | **Android** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/31` | 0.780962 | **Android** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/31` | 0.780962 | **Android** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/65` | 0.738962 | **Android** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/67` | 0.738962 | **Android** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/59` | 0.738962 | **Android** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/68` | 0.738962 | **Android** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/13/Text/32` | 0.738962 | **Android** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/91` | 0.380135 | **GAME** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/92` | 0.380135 | **GAME** |

### Query 40
- Text: Summarize **Barathu** **Human**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/32']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/32', 'PZO22001 Starfinder Player Core 058-073::/page/9/Text/33', 'PZO22001 Starfinder Player Core 058-073::/page/13/Text/33']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/32` | 1.011021 | **Barathu** **Human** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/33` | 1.011021 | **Barathu** **Human** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/13/Text/33` | 1.011021 | **Barathu** **Human** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/32` | 0.823271 | **Barathu** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/60` | 0.823271 | **Barathu** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/69` | 0.823271 | **Barathu** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/66` | 0.823271 | **Barathu** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/68` | 0.823271 | **Barathu** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/33` | 0.582673 | **Human** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/67` | 0.582673 | **Human** |

### Query 41
- Text: Summarize **Kasatha**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/33']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/9/Text/34', 'PZO22001 Starfinder Player Core 058-073::/page/11/Text/70', 'PZO22001 Starfinder Player Core 058-073::/page/1/Text/33']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/34` | 0.982519 | **Kasatha** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/70` | 0.982519 | **Kasatha** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/33` | 0.982519 | **Kasatha** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/71` | 0.940519 | **Kasatha** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/13/Text/34` | 0.940519 | **Kasatha** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/61` | 0.865414 | **Human** **Kasatha** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/68` | 0.741779 | **Kasatha** **Lashunta** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/34` | 0.741779 | **Kasatha** **Lashunta** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/69` | 0.396219 | **Barathu** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/66` | 0.396219 | **Barathu** |

### Query 42
- Text: Summarize **Lashunta**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/34']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/34', 'PZO22001 Starfinder Player Core 058-073::/page/7/Text/62', 'PZO22001 Starfinder Player Core 058-073::/page/15/Text/72']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/34` | 0.972315 | **Lashunta** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/62` | 0.972315 | **Lashunta** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/72` | 0.972315 | **Lashunta** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/71` | 0.930315 | **Lashunta** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/13/Text/35` | 0.930315 | **Lashunta** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/20` | 0.798647 | **LASHUNTA** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/11` | 0.798647 | **LASHUNTA** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/30` | 0.798647 | **LASHUNTA** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/26` | 0.798647 | **LASHUNTA** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/15` | 0.798647 | **LASHUNTA** |

### Query 43
- Text: Summarize **Pahtra**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/35']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/5/Text/35', 'PZO22001 Starfinder Player Core 058-073::/page/1/Text/35', 'PZO22001 Starfinder Player Core 058-073::/page/11/Text/72']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/35` | 0.983397 | **Pahtra** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/35` | 0.983397 | **Pahtra** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/72` | 0.983397 | **Pahtra** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/13/Text/36` | 0.941397 | **Pahtra** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/63` | 0.941397 | **Pahtra** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/73` | 0.941397 | **Pahtra** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/18` | 0.893842 | **PAHTRA** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/15` | 0.893842 | **PAHTRA** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/28` | 0.893842 | **PAHTRA** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/6/Text/16` | 0.893842 | **PAHTRA** |

### Query 44
- Text: Summarize **Shirren**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/36']
- Expected found: `True`
- Expected rank: `6`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/15/Text/74', 'PZO22001 Starfinder Player Core 058-073::/page/7/Text/64', 'PZO22001 Starfinder Player Core 058-073::/page/5/Text/36']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/74` | 0.983425 | **Shirren** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/64` | 0.983425 | **Shirren** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/36` | 0.983425 | **Shirren** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/13/Text/37` | 0.941425 | **Shirren** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/36` | 0.941425 | **Shirren** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/36` | 0.941424 | **Shirren** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/73` | 0.941424 | **Shirren** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/27` | 0.837306 | **SHIRREN** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/22` | 0.837306 | **SHIRREN** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/14` | 0.837306 | **SHIRREN** |

### Query 45
- Text: Summarize **Skittermander**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/37']
- Expected found: `True`
- Expected rank: `6`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/9/Text/37', 'PZO22001 Starfinder Player Core 058-073::/page/7/Text/65', 'PZO22001 Starfinder Player Core 058-073::/page/5/Text/37']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/37` | 0.984124 | **Skittermander** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/65` | 0.984124 | **Skittermander** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/37` | 0.984124 | **Skittermander** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/75` | 0.942124 | **Skittermander** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/71` | 0.942124 | **Skittermander** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/37` | 0.942124 | **Skittermander** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/13/Text/38` | 0.942124 | **Skittermander** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/74` | 0.942124 | **Skittermander** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/15/SectionHeader/44` | 0.755685 | **SKITTERMANDER** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/15/SectionHeader/4` | 0.755685 | **SKITTERMANDER** |

### Query 46
- Text: Summarize **Vesk**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/38']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/38', 'PZO22001 Starfinder Player Core 058-073::/page/13/Text/39', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/72']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/38` | 0.943397 | **Vesk** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/13/Text/39` | 0.943397 | **Vesk** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/72` | 0.943397 | **Vesk** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/66` | 0.901397 | **Vesk** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/38` | 0.901397 | **Vesk** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/38` | 0.901397 | **Vesk** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/75` | 0.901397 | **Vesk** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/76` | 0.901397 | **Vesk** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/4/SectionHeader/10` | 0.513981 | LANGUAGES Common, Pahtra, Vesk |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/9` | 0.413685 | You've familiarized yourself with a weapon from another  ancestry or culture. Choose an uncommon simple or martial  weapon with a trait corresponding to an ancestry (such as  vesk or ysoki) or that's |

### Query 47
- Text: Summarize **Ysoki**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/39']
- Expected found: `True`
- Expected rank: `6`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/5/Text/39', 'PZO22001 Starfinder Player Core 058-073::/page/11/Text/76', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/73']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/39` | 0.934336 | **Ysoki** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/76` | 0.934336 | **Ysoki** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/73` | 0.934336 | **Ysoki** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/77` | 0.892336 | **Ysoki** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/39` | 0.892336 | **Ysoki** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/39` | 0.892336 | **Ysoki** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/67` | 0.892336 | **Ysoki** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/13/Text/40` | 0.892336 | **Ysoki** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/13/Text/18` | 0.393143 | **Sample Names:** Ayoka, Baazo, Bixby, Dakoyo, Fipzul, Gazigaz,  Jomp, Kayoko, Kimikim, Mimzy, Nako, Prismacora, Quonx,  Rudfuz, Sprax, Timinim, Tipps, Tonkona, Viverivim |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/81` | 0.383117 | **Languages** |

### Query 48
- Text: Summarize **Versatile ** **Heritages**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/40']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/40', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/74', 'PZO22001 Starfinder Player Core 058-073::/page/9/Text/40']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/40` | 0.959353 | **Versatile ** **Heritages** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/74` | 0.959353 | **Versatile ** **Heritages** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/40` | 0.959353 | **Versatile ** **Heritages** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/13/Text/41` | 0.917353 | **Versatile ** **Heritages** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/40` | 0.917353 | **Versatile ** **Heritages** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/78` | 0.917353 | **Versatile ** **Heritages** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/77` | 0.628755 | **Versatile ** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/68` | 0.628755 | **Versatile ** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/69` | 0.498696 | **Heritages** **Borai** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/78` | 0.498696 | **Heritages** **Borai** |

### Query 49
- Text: Summarize **Borai**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/41']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/15/Text/79', 'PZO22001 Starfinder Player Core 058-073::/page/5/Text/41', 'PZO22001 Starfinder Player Core 058-073::/page/1/Text/41']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/79` | 0.983112 | **Borai** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/41` | 0.983112 | **Borai** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/41` | 0.983112 | **Borai** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/41` | 0.941112 | **Borai** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/13/Text/42` | 0.941112 | **Borai** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/75` | 0.941112 | **Borai** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/69` | 0.857213 | **Heritages** **Borai** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/78` | 0.857213 | **Heritages** **Borai** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/60` | 0.447974 | **Barathu** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/68` | 0.447974 | **Barathu** |

### Query 50
- Text: Summarize **Prismeni**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/42']
- Expected found: `True`
- Expected rank: `4`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/7/Text/70', 'PZO22001 Starfinder Player Core 058-073::/page/13/Text/43', 'PZO22001 Starfinder Player Core 058-073::/page/5/Text/42']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/70` | 0.966478 | **Prismeni** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/13/Text/43` | 0.966478 | **Prismeni** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/42` | 0.966478 | **Prismeni** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/42` | 0.924478 | **Prismeni** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/79` | 0.924478 | **Prismeni** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/76` | 0.924478 | **Prismeni** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/42` | 0.924477 | **Prismeni** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/80` | 0.924477 | **Prismeni** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/18` | 0.451471 | **COMMANDING PHEROMONES** **FEAT 1** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/9` | 0.426406 | **ALLURING PHEROMONES** **FEAT 1** |

### Query 51
- Text: What is the rule about **Backgrounds** **Languages**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/43']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/43', 'PZO22001 Starfinder Player Core 058-073::/page/13/Text/44', 'PZO22001 Starfinder Player Core 058-073::/page/5/Text/43']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/43` | 0.858103 | **Backgrounds** **Languages** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/13/Text/44` | 0.858103 | **Backgrounds** **Languages** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/43` | 0.672728 | **Backgrounds** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/77` | 0.630728 | **Backgrounds** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/81` | 0.630728 | **Backgrounds** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/80` | 0.630728 | **Backgrounds** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/71` | 0.630728 | **Backgrounds** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/43` | 0.630728 | **Backgrounds** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/44` | 0.558729 | **Languages** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/82` | 0.546730 | **Languages** |

### Query 52
- Text: Summarize **CLASSES**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/44']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/44', 'PZO22001 Starfinder Player Core 058-073::/page/5/Text/45', 'PZO22001 Starfinder Player Core 058-073::/page/7/Text/73']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/44` | 0.940061 | **CLASSES** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/45` | 0.940061 | **CLASSES** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/73` | 0.940061 | **CLASSES** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/13/Text/45` | 0.910061 | **CLASSES** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/82` | 0.910061 | **CLASSES** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/83` | 0.910061 | **CLASSES** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/78` | 0.814555 | **Languages** **CLASSES** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/44` | 0.814555 | **Languages** **CLASSES** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/44` | 0.481450 | **Languages** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/72` | 0.481450 | **Languages** |

### Query 53
- Text: What is the rule about **SKILLS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/45']
- Expected found: `True`
- Expected rank: `5`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/9/Text/45', 'PZO22001 Starfinder Player Core 058-073::/page/7/Text/74', 'PZO22001 Starfinder Player Core 058-073::/page/13/Text/46']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/45` | 0.864442 | **SKILLS** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/74` | 0.864442 | **SKILLS** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/13/Text/46` | 0.864442 | **SKILLS** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/80` | 0.822442 | **SKILLS** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/45` | 0.822442 | **SKILLS** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/84` | 0.822442 | **SKILLS** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/83` | 0.651094 | **SKILLS** **FEATS** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/46` | 0.651094 | **SKILLS** **FEATS** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/22` | 0.490741 | You fall utterly silent and focus strenuously on a problem  at hand. You attempt to Recall Knowledge with a +2  circumstance bonus to the skill check. If you would get a  critical failure, you get a f |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/4` | 0.437417 | Your ability to adapt to various beliefs instills you with  knowledge of many cultures. You gain the trained proficiency  rank in Diplomacy and Society. If you would automatically  become trained in o |

### Query 54
- Text: What is the rule about **FEATS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/46']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/46', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/81', 'PZO22001 Starfinder Player Core 058-073::/page/13/Text/47']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/46` | 0.871817 | **FEATS** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/81` | 0.871817 | **FEATS** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/13/Text/47` | 0.871817 | **FEATS** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/75` | 0.829817 | **FEATS** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/46` | 0.829817 | **FEATS** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/85` | 0.829817 | **FEATS** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/83` | 0.653037 | **SKILLS** **FEATS** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/46` | 0.653037 | **SKILLS** **FEATS** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/3` | 0.442859 | **PREDATORY** **FEAT 1** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/14/SectionHeader/26` | 0.435722 | **HYPER** **FEAT 1** |

### Query 55
- Text: Summarize **EQUIPMENT**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/47']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/15/Text/86', 'PZO22001 Starfinder Player Core 058-073::/page/1/Text/47', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/82']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/86` | 0.944726 | **EQUIPMENT** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/47` | 0.944726 | **EQUIPMENT** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/82` | 0.944726 | **EQUIPMENT** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/76` | 0.902726 | **EQUIPMENT** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/13/Text/48` | 0.902726 | **EQUIPMENT** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/84` | 0.902726 | **EQUIPMENT** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/47` | 0.902726 | **EQUIPMENT** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/47` | 0.902726 | **EQUIPMENT** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/66` | 0.385549 | **INTRODUCTION** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/63` | 0.385549 | **INTRODUCTION** |

### Query 56
- Text: What is the rule about **SPELLS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/48']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/9/Text/48', 'PZO22001 Starfinder Player Core 058-073::/page/1/Text/48', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/83']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/48` | 0.889304 | **SPELLS** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/48` | 0.889304 | **SPELLS** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/83` | 0.889304 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/77` | 0.847304 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/48` | 0.847304 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/85` | 0.847304 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/13/Text/49` | 0.847304 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/87` | 0.740792 | **SPELLS** **PLAYING THE ** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/74` | 0.388254 | **SKILLS** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/13/Text/46` | 0.388254 | **SKILLS** |

### Query 57
- Text: Summarize **PLAYING THE ** **GAME**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/49']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/49', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/84', 'PZO22001 Starfinder Player Core 058-073::/page/7/Text/78']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/49` | 0.965000 | **PLAYING THE ** **GAME** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/78` | 0.965000 | **PLAYING THE ** **GAME** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/84` | 0.965000 | **PLAYING THE ** **GAME** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/13/Text/50` | 0.923000 | **PLAYING THE ** **GAME** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/49` | 0.923000 | **PLAYING THE ** **GAME** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/49` | 0.923000 | **PLAYING THE ** **GAME** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/86` | 0.811006 | **PLAYING THE ** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/91` | 0.663024 | **GAME** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/92` | 0.663024 | **GAME** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/87` | 0.576670 | **SPELLS** **PLAYING THE ** |

### Query 58
- Text: Summarize **CONDITIONS ** **APPENDIX**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/50']
- Expected found: `True`
- Expected rank: `4`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/13/Text/51', 'PZO22001 Starfinder Player Core 058-073::/page/9/Text/50', 'PZO22001 Starfinder Player Core 058-073::/page/11/Text/87']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/50` | 0.983499 | **CONDITIONS ** **APPENDIX** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/87` | 0.983499 | **CONDITIONS ** **APPENDIX** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/13/Text/51` | 0.983499 | **CONDITIONS ** **APPENDIX** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/50` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/79` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/85` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/50` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/88` | 0.645203 | **CONDITIONS ** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/89` | 0.576258 | **APPENDIX** **GLOSSARY & ** **INDEX** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/58` | 0.416141 | **ANCESTRIES & ** **BACKGROUNDS** |

### Query 59
- Text: Summarize **GLOSSARY & ** **INDEX**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/51']
- Expected found: `True`
- Expected rank: `7`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/9/Text/51', 'PZO22001 Starfinder Player Core 058-073::/page/7/Text/80', 'PZO22001 Starfinder Player Core 058-073::/page/11/Text/88']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/51` | 0.993465 | **GLOSSARY & ** **INDEX** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/80` | 0.993465 | **GLOSSARY & ** **INDEX** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/88` | 0.993465 | **GLOSSARY & ** **INDEX** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/51` | 0.951465 | **GLOSSARY & ** **INDEX** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/13/Text/52` | 0.951465 | **GLOSSARY & ** **INDEX** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/86` | 0.951465 | **GLOSSARY & ** **INDEX** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/51` | 0.951465 | **GLOSSARY & ** **INDEX** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/89` | 0.856301 | **APPENDIX** **GLOSSARY & ** **INDEX** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/78` | 0.398029 | **Languages** **CLASSES** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/44` | 0.398029 | **Languages** **CLASSES** |

### Query 60
- Text: What is the rule about **CHARACTER ** **SHEET**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/52']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/52', 'PZO22001 Starfinder Player Core 058-073::/page/11/Text/91', 'PZO22001 Starfinder Player Core 058-073::/page/15/Text/92']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/52` | 0.859300 | **CHARACTER ** **SHEET** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/91` | 0.422766 | **GAME** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/92` | 0.422766 | **GAME** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/88` | 0.390942 | **CONDITIONS ** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/69` | 0.360758 | **Human** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/70` | 0.360758 | **Human** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/33` | 0.360758 | **Human** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/67` | 0.360758 | **Human** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/46` | 0.357339 | **SKILLS** **FEATS** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/83` | 0.357339 | **SKILLS** **FEATS** |

### Query 61
- Text: Summarize 59
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/53']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/53', 'PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/21', 'PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/25']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/53` | 0.782249 | 59 |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/21` | 0.293267 | 9TH LEVEL |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/25` | 0.293267 | 9TH LEVEL |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/23` | 0.251267 | 9TH LEVEL |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/15/SectionHeader/12` | 0.251267 | 9TH LEVEL |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/17` | 0.249709 | Cesca, Chk Chk, Halicon, Izenzi, Jchk, J'scib, Keskodai, Kinnik,  Korskal, Philt, Schect, Thast, T'sen, Xylit, Zenka, and Zigvigix. |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/17` | 0.244716 | At 9th level, this becomes an imprecise sense. |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/28` | 0.227703 | **PSYCHIC MASTERY** **FEAT 9** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/32` | 0.227178 | **PSYCHIC MASTER** **FEAT 9** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/13/Text/18` | 0.226880 | **Sample Names:** Ayoka, Baazo, Bixby, Dakoyo, Fipzul, Gazigaz,  Jomp, Kayoko, Kimikim, Mimzy, Nako, Prismacora, Quonx,  Rudfuz, Sprax, Timinim, Tipps, Tonkona, Viverivim |

### Query 62
- Text: What is the rule about In addition to what you gain from your ancestry, you gain an  attribute boost to Strength and an attribute flaw to Wisdom,  but the free ancestry boost can't also be Strength. You gain 8  Hit Points from your ancestry instead of 6, and you gain a +1  circumstance bonus to Athletics checks to Shove or Trip.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/2/Text/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/2/Text/1', 'PZO22001 Starfinder Player Core 058-073::/page/6/Text/7', 'PZO22001 Starfinder Player Core 058-073::/page/1/Text/25']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/1` | 0.993442 | In addition to what you gain from your ancestry, you gain an  attribute boost to Strength and an attribute flaw to Wisdom,  but the free ancestry boost can't also be Strength. You gain 8  Hit Points f |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/6/Text/7` | 0.581878 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As a pahtra, you choose from among the  following an |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/25` | 0.563111 | You've chosen the adaptive genetics to become a damaya. You  might have a leaner, lither body type than other lashuntas and  are likely encouraged to pursue work as a scholar or politician.  In additi |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/7` | 0.518102 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As a lashunta, you choose from among  the following |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/14/Text/7` | 0.516963 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As a skittermander, you choose from  among the follo |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/10/Text/11` | 0.497725 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As a shirren, you choose from among the  following a |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/6/Text/14` | 0.485224 | You push yourself to be the best by competing with the  triggering ally. Until the end of your next turn, you can attempt  the same skill check to perform the same action or activity  that the trigger |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/14/Text/25` | 0.472073 | A good, solid hug makes everything better, and you're  bringing hugs to the battlefield. You gain the Titan Wrestler  skill feat. Additionally, you gain a +1 circumstance bonus to  Athletics checks to |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/25` | 0.459732 | You descend from a long line of hunters, and your fur is  especially well suited to blending into multiple environments.  As long as you're in a natural and undeveloped environment,  you gain a +2 cir |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/10` | 0.442913 | If you're trained in all martial weapons, you can instead  choose an uncommon advanced weapon that has an ancestry's  trait or is common in another culture. You gain access to that  weapon and have fa |

### Query 63
- Text: Summarize UNBOUND LASHUNTA
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/2', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/41', 'PZO22001 Starfinder Player Core 058-073::/page/0/SectionHeader/1']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/2` | 0.993687 | UNBOUND LASHUNTA |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/41` | 0.761476 | **UNCOMMON** **LASHUNTA** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/0/SectionHeader/1` | 0.745970 | LASHUNTA |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/2` | 0.661293 | **LASHUNTA** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/11` | 0.661293 | **LASHUNTA** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/30` | 0.661293 | **LASHUNTA** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/26` | 0.661293 | **LASHUNTA** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/20` | 0.661293 | **LASHUNTA** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/20` | 0.661293 | **LASHUNTA** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/59` | 0.661293 | **LASHUNTA** |

### Query 64
- Text: What is the rule about You decided against activating your ancestry's adaptive  genetics. You might show a combination of damaya and  korasha traits; you might be tall and muscular or short and  lithe, or perhaps you have unusual features, such as bumps  and swirls covering your body or long, fuzzy antennae. You  gain the Unbound Mind reaction.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/2/Text/3']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/2/Text/3', 'PZO22001 Starfinder Player Core 058-073::/page/1/Text/27', 'PZO22001 Starfinder Player Core 058-073::/page/1/Text/25']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/3` | 0.998173 | You decided against activating your ancestry's adaptive  genetics. You might show a combination of damaya and  korasha traits; you might be tall and muscular or short and  lithe, or perhaps you have u |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/27` | 0.690453 | You've chosen the adaptive genetics to become a korasha. You  might be stockier and more muscular than other lashuntas. |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/25` | 0.690450 | You've chosen the adaptive genetics to become a damaya. You  might have a leaner, lither body type than other lashuntas and  are likely encouraged to pursue work as a scholar or politician.  In additi |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/13` | 0.620622 | Around puberty, lashuntas traditionally choose whether  to express damaya or korasha genetics—a decision that  determines their physical development and influences their  potential societal roles. Las |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/1/ListItem/3` | 0.549706 | Prioritize learning and diplomacy if you're a damaya, or  physique and tactical prowess if you're a korasha—or if  you're an unbound lashunta, you have different priorities. |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/12` | 0.546719 | Damayas tend to be tall and graceful with delicate features and  are traditionally pushed toward artistic or intellectual pursuits  and political occupations. Korashas are shorter, more muscular,  and |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/4` | 0.530750 | **Unbound Mind **[reaction] **Trigger** You attempt a saving throw against  a mental effect, but you haven't rolled yet; **Effect** You refuse  to conform to the will of others, shaking off their atte |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/9` | 0.526634 | Lashuntas are natural psychics with adaptive genetics who  traditionally develop into one of two heritages at puberty:  damayas or korashas. They have a well-earned reputation for  being charismatic, |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/1` | 0.493471 | In addition to what you gain from your ancestry, you gain an  attribute boost to Strength and an attribute flaw to Wisdom,  but the free ancestry boost can't also be Strength. You gain 8  Hit Points f |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/58` | 0.488593 | You can shield your mind by using similar techniques that  your ancestors once mastered to escape the Swarm. You block  the intruding effect by scattering your thoughts, making you  immune to the trig |

### Query 65
- Text: What is the rule about **Unbound Mind **[reaction] **Trigger** You attempt a saving throw against  a mental effect, but you haven't rolled yet; **Effect** You refuse  to conform to the will of others, shaking off their attempts  to control you with sheer determination. You gain a +1  circumstance bonus to the triggering saving throw and other  saves against mental effects until the start of your next turn.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/2/Text/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/2/Text/4', 'PZO22001 Starfinder Player Core 058-073::/page/2/Text/17', 'PZO22001 Starfinder Player Core 058-073::/page/11/Text/57']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/4` | 0.965472 | **Unbound Mind **[reaction] **Trigger** You attempt a saving throw against  a mental effect, but you haven't rolled yet; **Effect** You refuse  to conform to the will of others, shaking off their atte |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/17` | 0.717885 | **Trigger** You fail a Will saving throw against a mental effect. You center your thoughts and focus your mind, shaking off  emotional turmoil and harmful mental intrusions. Reroll the  triggering sav |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/57` | 0.638249 | **Trigger** You're targeted by a mental effect. |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/6/Text/14` | 0.556153 | You push yourself to be the best by competing with the  triggering ally. Until the end of your next turn, you can attempt  the same skill check to perform the same action or activity  that the trigger |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/54` | 0.546774 | **Trigger** A creature Casts a Spell with the mental trait. |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/14/Text/18` | 0.532377 | You're rarely discouraged or afraid. You gain a +1 circumstance  bonus to saves against fear and to your Will DC against  attempts to Demoralize you. If you get a success on a save  against a fear eff |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/56` | 0.525412 | When a foe Casts a Spell that has the mental trait and you can  see or otherwise detect its manifestations, you use your psychic  powers to disrupt it. You expend 1 Focus Point to counter the  trigger |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/3` | 0.524518 | You decided against activating your ancestry's adaptive  genetics. You might show a combination of damaya and  korasha traits; you might be tall and muscular or short and  lithe, or perhaps you have u |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/27` | 0.517788 | Despite the passage of time, you remain resolute in your  defiance of the Swarm and all forms of mental control. If you  roll a success on a Will saving throw against an effect that  was created by a |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/45` | 0.507814 | **Trigger** A creature critically fails a melee Strike against you. **Requirements** The triggering creature is within your reach,  you have at least one free active hand, and your target is  no more |

### Query 66
- Text: What is the rule about LASHUNTA ANCESTRY  FEATS?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/6', 'PZO22001 Starfinder Player Core 058-073::/page/2/Text/7', 'PZO22001 Starfinder Player Core 058-073::/page/0/SectionHeader/1']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/6` | 0.923960 | LASHUNTA ANCESTRY  FEATS |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/7` | 0.672100 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As a lashunta, you choose from among  the following |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/0/SectionHeader/1` | 0.645782 | LASHUNTA |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/6/SectionHeader/6` | 0.584838 | PAHTRA ANCESTRY  FEATS |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/10` | 0.583223 | SHIRREN ANCESTRY  FEATS |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/1/SectionHeader/22` | 0.573871 | LASHUNTA HERITAGES |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/14/SectionHeader/6` | 0.557362 | SKITTERMANDER  ANCESTRY FEATS |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/2` | 0.538733 | **LASHUNTA** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/11` | 0.538733 | **LASHUNTA** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/15` | 0.538733 | **LASHUNTA** |

### Query 67
- Text: What is the rule about At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As a lashunta, you choose from among  the following ancestry feats.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/2/Text/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/2/Text/7', 'PZO22001 Starfinder Player Core 058-073::/page/6/Text/7', 'PZO22001 Starfinder Player Core 058-073::/page/10/Text/11']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/7` | 0.974696 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As a lashunta, you choose from among  the following |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/6/Text/7` | 0.810816 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As a pahtra, you choose from among the  following an |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/10/Text/11` | 0.797847 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As a shirren, you choose from among the  following a |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/14/Text/7` | 0.727925 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As a skittermander, you choose from  among the follo |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/25` | 0.608928 | You've chosen the adaptive genetics to become a damaya. You  might have a leaner, lither body type than other lashuntas and  are likely encouraged to pursue work as a scholar or politician.  In additi |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/32` | 0.600487 | You also gain the Additional Lore general feat for  Lashunta Lore. |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/23` | 0.587376 | Around puberty, many lashuntas choose to embrace a genetic  path that determines their physiology and role in society.  Choose one of the following lashunta heritages at 1st level. |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/10/Text/28` | 0.532504 | Learning new languages comes naturally to you. You gain two  additional languages of your choice, chosen from among the  common and uncommon languages available to you. Every time  you take the Multil |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/1` | 0.524712 | In addition to what you gain from your ancestry, you gain an  attribute boost to Strength and an attribute flaw to Wisdom,  but the free ancestry boost can't also be Strength. You gain 8  Hit Points f |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/10` | 0.524674 | If you want to play a character who strives for selfimprovement and has innate psychic abilities, you should play  a lashunta. |

### Query 68
- Text: Summarize 1ST LEVEL
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/8']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/12', 'PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/8', 'PZO22001 Starfinder Player Core 058-073::/page/14/SectionHeader/8']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/12` | 0.938612 | 1ST LEVEL |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/8` | 0.938612 | 1ST LEVEL |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/14/SectionHeader/8` | 0.938612 | 1ST LEVEL |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/6/SectionHeader/8` | 0.896612 | 1ST LEVEL |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/10` | 0.552315 | 5TH LEVEL |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/14/SectionHeader/34` | 0.552314 | 5TH LEVEL |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/11` | 0.552314 | 5TH LEVEL |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/4` | 0.552314 | 5TH LEVEL |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/15/SectionHeader/12` | 0.535171 | 9TH LEVEL |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/23` | 0.535171 | 9TH LEVEL |

### Query 69
- Text: What are the requirements for **ALLURING PHEROMONES** **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/9', 'PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/18', 'PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/34']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/9` | 0.907708 | **ALLURING PHEROMONES** **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/18` | 0.717647 | **COMMANDING PHEROMONES** **FEAT 1** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/34` | 0.596057 | **FOCUS PHEROMONES **[one-action] **FEAT 13** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/6/SectionHeader/15` | 0.473761 | **HARMONIC SENSITIVITY** **FEAT 1** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/3` | 0.410470 | **PREDATORY** **FEAT 1** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/22` | 0.410149 | **HARMONIC SHIELDING** **FEAT 9** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/14/SectionHeader/26` | 0.390961 | **HYPER** **FEAT 1** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/24` | 0.384940 | **Prerequisites** Harmonic Sensitivity |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/25` | 0.371304 | **LINGUISTIC PRODIGY** **FEAT 1** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/38` | 0.360192 | You can purposefully deploy your pheromones to manipulate  the reactions of those around you. If your next action is to  attempt a Deception check to Create a Diversion, a Diplomacy  check to Request, |

### Query 70
- Text: Summarize **LASHUNTA**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/11']
- Expected found: `True`
- Expected rank: `4`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/24', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/7', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/2']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/24` | 0.972025 | **LASHUNTA** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/7` | 0.972025 | **LASHUNTA** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/2` | 0.972025 | **LASHUNTA** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/11` | 0.930025 | **LASHUNTA** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/30` | 0.930025 | **LASHUNTA** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/11` | 0.930025 | **LASHUNTA** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/20` | 0.930025 | **LASHUNTA** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/59` | 0.930025 | **LASHUNTA** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/26` | 0.930025 | **LASHUNTA** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/30` | 0.930025 | **LASHUNTA** |

### Query 71
- Text: What is the rule about You influence others with pheromones, even when you lack  other means of communication. You can use Diplomacy  to Make an Impression on creatures with whom you don't  share a language and to make simple Requests of them. This  could include getting directions or getting the target to pick a  specific individual out from a crowd. When you do, Make an  Impression and Request lose the linguistic trait and gain the  olfactory trait.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/2/Text/12']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/2/Text/12', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/38', 'PZO22001 Starfinder Player Core 058-073::/page/2/Text/21']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/12` | 1.007747 | You influence others with pheromones, even when you lack  other means of communication. You can use Diplomacy  to Make an Impression on creatures with whom you don't  share a language and to make simp |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/38` | 0.689300 | You can purposefully deploy your pheromones to manipulate  the reactions of those around you. If your next action is to  attempt a Deception check to Create a Diversion, a Diplomacy  check to Request, |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/21` | 0.611494 | You can leverage your alluring pheromones to soothe ill will  and take the edge off your threats, turning your attempts  at coercion into acts of leadership. When you Coerce a  creature, if your targe |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/22` | 0.509974 | When you use limited telepathy to communicate with another  creature, you act as a conduit for their thoughts, allowing them  to respond to you for a few scant moments—if they wish. The  creature can |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/24` | 0.504892 | When you use limited telepathy to communicate with another  creature, the creature can give you a brief response as a reaction,  or as a free action at the beginning of their next turn. |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/25` | 0.482690 | Your telepathy is stronger than most shirrens', allowing you to  combine physical, verbal, and telepathic communication. You  can transmit emotions alongside your messages whenever  you use limited te |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/0/Text/13` | 0.478084 | You can communicate mentally with creatures within 30 feet. You can communicate only with creatures that share a language with you. This doesn't give you any access to their thoughts and communicates |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/8/Text/15` | 0.478084 | You can communicate mentally with creatures within 30 feet. You can communicate only with creatures that share a language with you. This doesn't give you any access to their thoughts and communicates |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/4` | 0.473191 | Your ability to adapt to various beliefs instills you with  knowledge of many cultures. You gain the trained proficiency  rank in Diplomacy and Society. If you would automatically  become trained in o |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/14/Text/32` | 0.468613 | You're gregarious and friendly but also passionately  interested in the history of your people, going out of  your way to learn traditional stories and unearth  lost secrets. You gain the trained prof |

### Query 72
- Text: What are the requirements for **CENTER THOUGHTS **[free-action] **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/13', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/48', 'PZO22001 Starfinder Player Core 058-073::/page/15/SectionHeader/2']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/13` | 0.884423 | **CENTER THOUGHTS **[free-action] **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/48` | 0.685497 | **Prerequisites** Center Thoughts |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/15/SectionHeader/2` | 0.528023 | **HELPING HAND **[free-action] **FEAT 5** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/24` | 0.470209 | **GUARDED THOUGHTS** **FEAT 9** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/55` | 0.439673 | **Requirements** You have at least 1 Focus Point. |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/15/SectionHeader/13` | 0.434118 | **ALL HANDS ON DECK **[free-action] **FEAT 9** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/49` | 0.421216 | You know your own mind and instinctively resist attempts to  unbalance your thoughts or control your emotions. You can  use Center Thoughts once per hour, rather than once per day. |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/45` | 0.419497 | **CENTERED MIND** **FEAT 17** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/14/SectionHeader/35` | 0.417071 | **DOUBLE DRAW **[one-action] **FEAT 5** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/42` | 0.413019 | **SCRUPULOUS STALKER **[free-action] **FEAT 13** |

### Query 73
- Text: Summarize **CONCENTRATE** **FORTUNE** **LASHUNTA** **MENTAL**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/15']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/15', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/36', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/52']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/15` | 1.003164 | **CONCENTRATE** **FORTUNE** **LASHUNTA** **MENTAL** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/36` | 0.740219 | **FORTUNE** **LASHUNTA** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/52` | 0.737014 | **LASHUNTA** **MENTAL** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/15` | 0.632320 | **CONCENTRATE** **FORTUNE** **SHIRREN** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/2` | 0.545490 | **LASHUNTA** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/7` | 0.545490 | **LASHUNTA** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/24` | 0.545490 | **LASHUNTA** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/11` | 0.545489 | **LASHUNTA** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/30` | 0.545489 | **LASHUNTA** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/20` | 0.545489 | **LASHUNTA** |

### Query 74
- Text: Summarize **Frequency** once per day
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/2/Text/16']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/15/Text/57', 'PZO22001 Starfinder Player Core 058-073::/page/15/Text/21', 'PZO22001 Starfinder Player Core 058-073::/page/2/Text/16']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/57` | 0.988598 | **Frequency** once per day |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/16` | 0.988598 | **Frequency** once per day |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/21` | 0.988598 | **Frequency** once per day |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/15/SectionHeader/35` | 0.946598 | **Frequency** once per day |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/10/Text/16` | 0.946598 | **Frequency** once per day |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/56` | 0.946598 | **Frequency** once per day |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/27` | 0.791401 | **Frequency** once per hour |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/37` | 0.791401 | **Frequency** once per hour |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/6/Text/12` | 0.791401 | **Frequency** once per hour |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/5` | 0.759243 | **Frequency** once every 10 minutes |

### Query 75
- Text: What is the rule about **Trigger** You fail a Will saving throw against a mental effect. You center your thoughts and focus your mind, shaking off  emotional turmoil and harmful mental intrusions. Reroll the  triggering saving throw and use the better result.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/2/Text/17']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/2/Text/17', 'PZO22001 Starfinder Player Core 058-073::/page/2/Text/4', 'PZO22001 Starfinder Player Core 058-073::/page/11/Text/57']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/17` | 0.964444 | **Trigger** You fail a Will saving throw against a mental effect. You center your thoughts and focus your mind, shaking off  emotional turmoil and harmful mental intrusions. Reroll the  triggering sav |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/4` | 0.734245 | **Unbound Mind **[reaction] **Trigger** You attempt a saving throw against  a mental effect, but you haven't rolled yet; **Effect** You refuse  to conform to the will of others, shaking off their atte |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/57` | 0.723696 | **Trigger** You're targeted by a mental effect. |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/54` | 0.620658 | **Trigger** A creature Casts a Spell with the mental trait. |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/6/Text/14` | 0.582789 | You push yourself to be the best by competing with the  triggering ally. Until the end of your next turn, you can attempt  the same skill check to perform the same action or activity  that the trigger |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/10/Text/18` | 0.568845 | You broadcast helpful encouragement or pertinent information  to your ally's mind. Your ally rerolls the triggering skill check and  takes the better result. |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/45` | 0.562649 | **Trigger** A creature critically fails a melee Strike against you. **Requirements** The triggering creature is within your reach,  you have at least one free active hand, and your target is  no more |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/6/Text/13` | 0.538818 | **Trigger** An ally attempts a skill check with a skill that you have  trained or better proficiency rank in. |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/56` | 0.534880 | When a foe Casts a Spell that has the mental trait and you can  see or otherwise detect its manifestations, you use your psychic  powers to disrupt it. You expend 1 Focus Point to counter the  trigger |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/14/Text/18` | 0.529793 | You're rarely discouraged or afraid. You gain a +1 circumstance  bonus to saves against fear and to your Will DC against  attempts to Demoralize you. If you get a success on a save  against a fear eff |

### Query 76
- Text: What are the requirements for **COMMANDING PHEROMONES** **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/18']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/18', 'PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/9', 'PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/34']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/18` | 0.899792 | **COMMANDING PHEROMONES** **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/9` | 0.716381 | **ALLURING PHEROMONES** **FEAT 1** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/34` | 0.604257 | **FOCUS PHEROMONES **[one-action] **FEAT 13** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/6/SectionHeader/15` | 0.464588 | **HARMONIC SENSITIVITY** **FEAT 1** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/3` | 0.412374 | **PREDATORY** **FEAT 1** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/38` | 0.411297 | You can purposefully deploy your pheromones to manipulate  the reactions of those around you. If your next action is to  attempt a Deception check to Create a Diversion, a Diplomacy  check to Request, |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/22` | 0.400992 | **HARMONIC SHIELDING** **FEAT 9** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/12` | 0.395643 | You influence others with pheromones, even when you lack  other means of communication. You can use Diplomacy  to Make an Impression on creatures with whom you don't  share a language and to make simp |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/21` | 0.389802 | You can leverage your alluring pheromones to soothe ill will  and take the edge off your threats, turning your attempts  at coercion into acts of leadership. When you Coerce a  creature, if your targe |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/24` | 0.380976 | **Prerequisites** Harmonic Sensitivity |

### Query 77
- Text: Summarize **LASHUNTA**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/20']
- Expected found: `True`
- Expected rank: `7`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/24', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/7', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/2']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/24` | 0.972025 | **LASHUNTA** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/7` | 0.972025 | **LASHUNTA** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/2` | 0.972025 | **LASHUNTA** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/11` | 0.930025 | **LASHUNTA** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/30` | 0.930025 | **LASHUNTA** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/11` | 0.930025 | **LASHUNTA** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/20` | 0.930025 | **LASHUNTA** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/59` | 0.930025 | **LASHUNTA** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/26` | 0.930025 | **LASHUNTA** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/30` | 0.930025 | **LASHUNTA** |

### Query 78
- Text: What is the rule about You can leverage your alluring pheromones to soothe ill will  and take the edge off your threats, turning your attempts  at coercion into acts of leadership. When you Coerce a  creature, if your target would become unfriendly (and they  aren't already unfriendly or hostile), they become indifferent  instead.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/2/Text/21']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/2/Text/21', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/38', 'PZO22001 Starfinder Player Core 058-073::/page/2/Text/12']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/21` | 0.985545 | You can leverage your alluring pheromones to soothe ill will  and take the edge off your threats, turning your attempts  at coercion into acts of leadership. When you Coerce a  creature, if your targe |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/38` | 0.646481 | You can purposefully deploy your pheromones to manipulate  the reactions of those around you. If your next action is to  attempt a Deception check to Create a Diversion, a Diplomacy  check to Request, |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/12` | 0.614950 | You influence others with pheromones, even when you lack  other means of communication. You can use Diplomacy  to Make an Impression on creatures with whom you don't  share a language and to make simp |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/27` | 0.520812 | Despite the passage of time, you remain resolute in your  defiance of the Swarm and all forms of mental control. If you  roll a success on a Will saving throw against an effect that  was created by a |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/22` | 0.512955 | When you use limited telepathy to communicate with another  creature, you act as a conduit for their thoughts, allowing them  to respond to you for a few scant moments—if they wish. The  creature can |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/15` | 0.490548 | You love helping your friends and allies achieve their goals. At  the start of your turn, you gain one additional reaction, which  you can use only to Aid. |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/24` | 0.482830 | When you use limited telepathy to communicate with another  creature, the creature can give you a brief response as a reaction,  or as a free action at the beginning of their next turn. |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/14/Text/18` | 0.459647 | You're rarely discouraged or afraid. You gain a +1 circumstance  bonus to saves against fear and to your Will DC against  attempts to Demoralize you. If you get a success on a save  against a fear eff |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/63` | 0.452242 | Whether gradual or in an instant burst of glorious evolution,  you've metamorphosed into a powerful Swarm-like creature.  You gain a +2 status bonus to saves against fear, and you gain  acid resistanc |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/25` | 0.441176 | Your telepathy is stronger than most shirrens', allowing you to  combine physical, verbal, and telepathic communication. You  can transmit emotions alongside your messages whenever  you use limited te |

### Query 79
- Text: What are the requirements for **DISTANT TELEPATH** **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/22']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/22', 'PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/19', 'PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/22']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/22` | 0.870231 | **DISTANT TELEPATH** **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/19` | 0.870231 | **DISTANT TELEPATH** **FEAT 1** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/22` | 0.655712 | **Prerequisites** limited telepathy |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/23` | 0.613712 | **Prerequisites** limited telepathy |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/21` | 0.613712 | **Prerequisites** limited telepathy |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/25` | 0.613712 | **Prerequisites** limited telepathy |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/8/SectionHeader/14` | 0.582904 | LIMITED TELEPATHY |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/0/SectionHeader/12` | 0.582904 | LIMITED TELEPATHY |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/18` | 0.545931 | **TELEPATHIC CONDUIT** **FEAT 5** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/20` | 0.545931 | **TELEPATHIC CONDUIT** **FEAT 5** |

### Query 80
- Text: Summarize **LASHUNTA**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/24']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/24', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/7', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/2']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/24` | 0.972025 | **LASHUNTA** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/7` | 0.972025 | **LASHUNTA** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/2` | 0.972025 | **LASHUNTA** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/11` | 0.930025 | **LASHUNTA** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/30` | 0.930025 | **LASHUNTA** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/11` | 0.930025 | **LASHUNTA** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/20` | 0.930025 | **LASHUNTA** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/59` | 0.930025 | **LASHUNTA** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/26` | 0.930025 | **LASHUNTA** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/30` | 0.930025 | **LASHUNTA** |

### Query 81
- Text: What are the requirements for **Prerequisites** limited telepathy?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/2/Text/25']
- Expected found: `True`
- Expected rank: `4`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/3/Text/21', 'PZO22001 Starfinder Player Core 058-073::/page/11/Text/23', 'PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/22']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/21` | 0.945401 | **Prerequisites** limited telepathy |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/23` | 0.945401 | **Prerequisites** limited telepathy |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/22` | 0.945401 | **Prerequisites** limited telepathy |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/25` | 0.903401 | **Prerequisites** limited telepathy |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/0/SectionHeader/12` | 0.618754 | LIMITED TELEPATHY |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/8/SectionHeader/14` | 0.618754 | LIMITED TELEPATHY |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/10/Text/23` | 0.569906 | Whether through training or innate talent,  you've expanded the range at which you can  telepathically communicate. Increase the range of  your limited telepathy by 15 feet. |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/26` | 0.557906 | Whether through training or innate talent, you've expanded  the range at which you can telepathically communicate.  Increase the range of your limited telepathy by 15 feet. |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/25` | 0.552556 | Your telepathy is stronger than most shirrens', allowing you to  combine physical, verbal, and telepathic communication. You  can transmit emotions alongside your messages whenever  you use limited te |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/22` | 0.539129 | When you use limited telepathy to communicate with another  creature, you act as a conduit for their thoughts, allowing them  to respond to you for a few scant moments—if they wish. The  creature can |

### Query 82
- Text: What is the rule about **Special** You can select this feat more than once.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/2/Text/27']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/2/Text/27', 'PZO22001 Starfinder Player Core 058-073::/page/10/Text/24', 'PZO22001 Starfinder Player Core 058-073::/page/7/Text/9']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/27` | 0.900242 | **Special** You can select this feat more than once. |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/10/Text/24` | 0.900242 | **Special** You can select this feat more than once. |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/9` | 0.726220 | **Special** You can take this feat a second time. If you do, select  the other attack from the options above. |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/10/Text/28` | 0.479801 | Learning new languages comes naturally to you. You gain two  additional languages of your choice, chosen from among the  common and uncommon languages available to you. Every time  you take the Multil |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/10/Text/11` | 0.436007 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As a shirren, you choose from among the  following a |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/5` | 0.434148 | You also gain the Additional Lore general feat for Shirren Lore. |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/14/Text/21` | 0.432272 | You're fascinated with a particular topic, such as the  religion of a small sect of worshippers, the process of  spaghettification, or the songs sung by asterays. You gain  the Additional Lore feat an |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/14/Text/7` | 0.429097 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As a skittermander, you choose from  among the follo |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/32` | 0.425952 | You also gain the Additional Lore general feat for  Lashunta Lore. |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/51` | 0.418941 | You've continued to advance your powers using your  unconventional weapon. Whenever you gain a class feature  that grants you expert or greater proficiency in certain  weapons, you also gain that prof |

### Query 83
- Text: What are the requirements for **LASHUNTA LORE** **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/28']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/28', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/47', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/20']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/28` | 0.887091 | **LASHUNTA LORE** **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/20` | 0.633492 | **LASHUNTA** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/47` | 0.633492 | **LASHUNTA** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/30` | 0.603492 | **LASHUNTA** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/20` | 0.591492 | **LASHUNTA** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/11` | 0.591492 | **LASHUNTA** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/7` | 0.591492 | **LASHUNTA** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/24` | 0.591492 | **LASHUNTA** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/30` | 0.591492 | **LASHUNTA** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/15` | 0.591492 | **LASHUNTA** |

### Query 84
- Text: What is the rule about You've studied the lives and achievements of other  lashuntas who have improved both their psychic powers  and their communities. You gain the trained proficiency  rank in Occultism and Society. If you would automatically  become trained in one of those skills (from your background  or class, for example), you instead become trained in a skill  of your choice.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/2/Text/31']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/2/Text/31', 'PZO22001 Starfinder Player Core 058-073::/page/11/Text/4', 'PZO22001 Starfinder Player Core 058-073::/page/14/Text/32']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/31` | 1.004655 | You've studied the lives and achievements of other  lashuntas who have improved both their psychic powers  and their communities. You gain the trained proficiency  rank in Occultism and Society. If yo |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/4` | 0.772093 | Your ability to adapt to various beliefs instills you with  knowledge of many cultures. You gain the trained proficiency  rank in Diplomacy and Society. If you would automatically  become trained in o |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/14/Text/32` | 0.761839 | You're gregarious and friendly but also passionately  interested in the history of your people, going out of  your way to learn traditional stories and unearth  lost secrets. You gain the trained prof |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/1` | 0.678201 | performing arts. You gain the trained proficiency rank in  Acrobatics and Performance. If you would automatically become  trained in one of those skills (from your background or class, for  example), |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/25` | 0.610712 | You've chosen the adaptive genetics to become a damaya. You  might have a leaner, lither body type than other lashuntas and  are likely encouraged to pursue work as a scholar or politician.  In additi |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/51` | 0.562670 | You've continued to advance your powers using your  unconventional weapon. Whenever you gain a class feature  that grants you expert or greater proficiency in certain  weapons, you also gain that prof |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/10` | 0.536770 | If you're trained in all martial weapons, you can instead  choose an uncommon advanced weapon that has an ancestry's  trait or is common in another culture. You gain access to that  weapon and have fa |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/1/ListItem/3` | 0.512936 | Prioritize learning and diplomacy if you're a damaya, or  physique and tactical prowess if you're a korasha—or if  you're an unbound lashunta, you have different priorities. |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/32` | 0.503362 | Your psychic abilities have grown stronger, allowing you to  tap into entirely new dimensions of psychic power. Choose  one common 2nd-rank spell from the occult spell list. You can  cast that spell a |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/6/Text/14` | 0.500664 | You push yourself to be the best by competing with the  triggering ally. Until the end of your next turn, you can attempt  the same skill check to perform the same action or activity  that the trigger |

### Query 85
- Text: What is the rule about You also gain the Additional Lore general feat for  Lashunta Lore.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/2/Text/32']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/2/Text/32', 'PZO22001 Starfinder Player Core 058-073::/page/11/Text/5', 'PZO22001 Starfinder Player Core 058-073::/page/7/Text/2']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/32` | 0.951461 | You also gain the Additional Lore general feat for  Lashunta Lore. |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/5` | 0.769094 | You also gain the Additional Lore general feat for Shirren Lore. |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/2` | 0.768708 | You also gain the Additional Lore general feat for Pahtra Lore. |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/7` | 0.662484 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As a lashunta, you choose from among  the following |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/25` | 0.625798 | You've chosen the adaptive genetics to become a damaya. You  might have a leaner, lither body type than other lashuntas and  are likely encouraged to pursue work as a scholar or politician.  In additi |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/14/Text/21` | 0.585729 | You're fascinated with a particular topic, such as the  religion of a small sect of worshippers, the process of  spaghettification, or the songs sung by asterays. You gain  the Additional Lore feat an |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/14/Text/33` | 0.529027 | You also gain the Additional Lore general feat for  Skittermander Lore, and you learn Morandomandranan,  the original skittermander language that has long been  suppressed by the Veskarium. |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/10/Text/11` | 0.519628 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As a shirren, you choose from among the  following a |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/6/Text/7` | 0.514872 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As a pahtra, you choose from among the  following an |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/28` | 0.502719 | **LASHUNTA LORE** **FEAT 1** |

### Query 86
- Text: What are the requirements for **PSYCHIC TALENT** **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/3/Text/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/3/Text/1', 'PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/29', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/31']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/1` | 0.904026 | **PSYCHIC TALENT** **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/29` | 0.904026 | **PSYCHIC TALENT** **FEAT 1** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/31` | 0.788789 | **Prerequisites** Psychic Talent |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/35` | 0.746789 | **Prerequisites** Psychic Talent |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/42` | 0.587925 | **Prerequisites** Psychic Bully, Psychic Scholar, or Psychic Talent |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/60` | 0.577438 | **Prerequisites** Psychic Mastery |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/28` | 0.564227 | **PSYCHIC MASTERY** **FEAT 9** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/32` | 0.560909 | **PSYCHIC MASTER** **FEAT 9** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/9` | 0.521626 | **PSYCHIC SCHOLAR** **FEAT 5** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/46` | 0.509243 | **SKILLS** **FEATS** |

### Query 87
- Text: What is the rule about Your psychic abilities have developed beyond simple  communication. Choose one cantrip from the occult spell list. You  can cast this cantrip as an occult innate spell at will. A cantrip is  heightened to a spell rank equal to half your level rounded up.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/3/Text/3']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/10/Text/32', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/3', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/32']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/10/Text/32` | 0.979722 | Your psychic abilities have developed beyond simple  communication. Choose one cantrip from the occult spell list. You  can cast this cantrip as an occult innate spell at will. A cantrip is  heightene |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/3` | 0.979722 | Your psychic abilities have developed beyond simple  communication. Choose one cantrip from the occult spell list. You  can cast this cantrip as an occult innate spell at will. A cantrip is  heightene |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/32` | 0.772238 | Your psychic abilities have grown stronger, allowing you to  tap into entirely new dimensions of psychic power. Choose  one common 2nd-rank spell from the occult spell list. You can  cast that spell a |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/36` | 0.719171 | Your psychic abilities have grown stronger. Choose one  common 2nd-rank spell from the occult spell list. You can cast  that spell as an occult innate spell once per day. |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/61` | 0.704834 | Your psychic abilities have grown stronger. Choose one  common 6th-rank spell from the occult spell list. You can cast  that spell as an occult innate spell once per day. |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/43` | 0.638925 | You can use your telepathic abilities to quickly assess your  circumstances or subtly glean information from the minds of  others. You can cast *hypercognition* and *mind reading* as 3rdrank occult in |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/46` | 0.595938 | Your mastery of language reaches supernatural levels. You can  cast *truespeech* as a 5th-rank occult innate spell once per day on  yourself only. You gain a +1 status bonus to Diplomacy checks  for t |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/8` | 0.588181 | **Prerequisites** korasha lashunta or unbound lashunta heritage You can leverage your telepathic abilities to influence the  minds of others, imparting orders or inflaming fears. You can  cast *comman |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/31` | 0.568265 | You've studied the lives and achievements of other  lashuntas who have improved both their psychic powers  and their communities. You gain the trained proficiency  rank in Occultism and Society. If yo |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/12` | 0.559032 | **Prerequisites** damaya lashunta or unbound lashunta heritage You can transfer vast amounts of information to the minds of  others in mere moments. You can cast *mindlink* as a 1st-rank  occult innat |

### Query 88
- Text: What are the requirements for **PSYCHIC BULLY** **FEAT 5**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/3/Text/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/3/Text/5', 'PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/9', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/42']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/5` | 0.881741 | **PSYCHIC BULLY** **FEAT 5** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/9` | 0.682963 | **PSYCHIC SCHOLAR** **FEAT 5** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/42` | 0.667205 | **Prerequisites** Psychic Bully, Psychic Scholar, or Psychic Talent |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/31` | 0.568013 | **Prerequisites** Psychic Talent |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/35` | 0.568013 | **Prerequisites** Psychic Talent |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/29` | 0.541884 | **PSYCHIC TALENT** **FEAT 1** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/1` | 0.541884 | **PSYCHIC TALENT** **FEAT 1** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/60` | 0.532199 | **Prerequisites** Psychic Mastery |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/28` | 0.509019 | **PSYCHIC MASTERY** **FEAT 9** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/32` | 0.499205 | **PSYCHIC MASTER** **FEAT 9** |

### Query 89
- Text: What are the requirements for **Prerequisites** korasha lashunta or unbound lashunta heritage You can leverage your telepathic abilities to influence the  minds of others, imparting orders or inflaming fears. You can  cast *command* and *fear* as 1st-rank occult innate spells. You  can cast each of these occult innate spells once per day.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/3/Text/8']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/3/Text/8', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/12', 'PZO22001 Starfinder Player Core 058-073::/page/1/Text/10']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/8` | 0.978840 | **Prerequisites** korasha lashunta or unbound lashunta heritage You can leverage your telepathic abilities to influence the  minds of others, imparting orders or inflaming fears. You can  cast *comman |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/12` | 0.766286 | **Prerequisites** damaya lashunta or unbound lashunta heritage You can transfer vast amounts of information to the minds of  others in mere moments. You can cast *mindlink* as a 1st-rank  occult innat |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/10` | 0.664130 | If you want to play a character who strives for selfimprovement and has innate psychic abilities, you should play  a lashunta. |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/43` | 0.595948 | You can use your telepathic abilities to quickly assess your  circumstances or subtly glean information from the minds of  others. You can cast *hypercognition* and *mind reading* as 3rdrank occult in |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/7` | 0.573912 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As a lashunta, you choose from among  the following |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/1/ListItem/3` | 0.565696 | Prioritize learning and diplomacy if you're a damaya, or  physique and tactical prowess if you're a korasha—or if  you're an unbound lashunta, you have different priorities. |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/32` | 0.555713 | Your psychic abilities have grown stronger, allowing you to  tap into entirely new dimensions of psychic power. Choose  one common 2nd-rank spell from the occult spell list. You can  cast that spell a |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/36` | 0.539974 | Your psychic abilities have grown stronger. Choose one  common 2nd-rank spell from the occult spell list. You can cast  that spell as an occult innate spell once per day. |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/13` | 0.528425 | Around puberty, lashuntas traditionally choose whether  to express damaya or korasha genetics—a decision that  determines their physical development and influences their  potential societal roles. Las |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/9` | 0.527904 | Lashuntas are natural psychics with adaptive genetics who  traditionally develop into one of two heritages at puberty:  damayas or korashas. They have a well-earned reputation for  being charismatic, |

### Query 90
- Text: What are the requirements for **PSYCHIC SCHOLAR** **FEAT 5**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/9', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/5', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/42']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/9` | 0.880793 | **PSYCHIC SCHOLAR** **FEAT 5** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/5` | 0.650753 | **PSYCHIC BULLY** **FEAT 5** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/42` | 0.614838 | **Prerequisites** Psychic Bully, Psychic Scholar, or Psychic Talent |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/31` | 0.570933 | **Prerequisites** Psychic Talent |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/35` | 0.570933 | **Prerequisites** Psychic Talent |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/29` | 0.545190 | **PSYCHIC TALENT** **FEAT 1** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/1` | 0.545190 | **PSYCHIC TALENT** **FEAT 1** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/60` | 0.538863 | **Prerequisites** Psychic Mastery |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/16` | 0.535647 | **LEARNING EXPERIENCE** **FEAT 5** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/32` | 0.528392 | **PSYCHIC MASTER** **FEAT 9** |

### Query 91
- Text: What are the requirements for **Prerequisites** damaya lashunta or unbound lashunta heritage You can transfer vast amounts of information to the minds of  others in mere moments. You can cast *mindlink* as a 1st-rank  occult innate spell twice per day.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/3/Text/12']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/3/Text/12', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/8', 'PZO22001 Starfinder Player Core 058-073::/page/1/Text/10']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/12` | 0.965430 | **Prerequisites** damaya lashunta or unbound lashunta heritage You can transfer vast amounts of information to the minds of  others in mere moments. You can cast *mindlink* as a 1st-rank  occult innat |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/8` | 0.744131 | **Prerequisites** korasha lashunta or unbound lashunta heritage You can leverage your telepathic abilities to influence the  minds of others, imparting orders or inflaming fears. You can  cast *comman |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/10` | 0.624475 | If you want to play a character who strives for selfimprovement and has innate psychic abilities, you should play  a lashunta. |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/1/ListItem/3` | 0.562740 | Prioritize learning and diplomacy if you're a damaya, or  physique and tactical prowess if you're a korasha—or if  you're an unbound lashunta, you have different priorities. |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/7` | 0.556035 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As a lashunta, you choose from among  the following |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/25` | 0.553441 | You've chosen the adaptive genetics to become a damaya. You  might have a leaner, lither body type than other lashuntas and  are likely encouraged to pursue work as a scholar or politician.  In additi |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/13` | 0.537720 | Around puberty, lashuntas traditionally choose whether  to express damaya or korasha genetics—a decision that  determines their physical development and influences their  potential societal roles. Las |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/31` | 0.525130 | You've studied the lives and achievements of other  lashuntas who have improved both their psychic powers  and their communities. You gain the trained proficiency  rank in Occultism and Society. If yo |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/43` | 0.523643 | You can use your telepathic abilities to quickly assess your  circumstances or subtly glean information from the minds of  others. You can cast *hypercognition* and *mind reading* as 3rdrank occult in |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/9` | 0.520157 | Lashuntas are natural psychics with adaptive genetics who  traditionally develop into one of two heritages at puberty:  damayas or korashas. They have a well-earned reputation for  being charismatic, |

### Query 92
- Text: What are the requirements for **SENSITIVE ANTENNAE** **FEAT 5**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/13', 'PZO22001 Starfinder Player Core 058-073::/page/6/SectionHeader/15', 'PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/24']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/13` | 0.921172 | **SENSITIVE ANTENNAE** **FEAT 5** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/6/SectionHeader/15` | 0.539735 | **HARMONIC SENSITIVITY** **FEAT 1** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/24` | 0.531781 | **Prerequisites** Harmonic Sensitivity |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/18` | 0.471059 | **TELEPATHIC CONDUIT** **FEAT 5** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/20` | 0.471059 | **TELEPATHIC CONDUIT** **FEAT 5** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/16` | 0.467257 | **LEARNING EXPERIENCE** **FEAT 5** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/12` | 0.430667 | **EAGER ASSISTANT** **FEAT 5** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/16` | 0.417758 | Your antennae are covered in fine hairs that make them  more sensitive to psychic vibrations than most. You gain  thoughtsense as a vague sense with a range of 30 feet. This  means you can use your an |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/26` | 0.390253 | **MELODIC ADAPTATION** **FEAT 9** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/9` | 0.389912 | **PSYCHIC SCHOLAR** **FEAT 5** |

### Query 93
- Text: What are the requirements for **TELEPATHIC CONDUIT** **FEAT 5**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/18']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/18', 'PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/20', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/21']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/18` | 0.914094 | **TELEPATHIC CONDUIT** **FEAT 5** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/20` | 0.914094 | **TELEPATHIC CONDUIT** **FEAT 5** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/21` | 0.591851 | **Prerequisites** limited telepathy |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/22` | 0.549851 | **Prerequisites** limited telepathy |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/25` | 0.549851 | **Prerequisites** limited telepathy |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/23` | 0.549851 | **Prerequisites** limited telepathy |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/19` | 0.466195 | **DISTANT TELEPATH** **FEAT 1** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/22` | 0.466195 | **DISTANT TELEPATH** **FEAT 1** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/16` | 0.461815 | **LEARNING EXPERIENCE** **FEAT 5** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/0/SectionHeader/12` | 0.439801 | LIMITED TELEPATHY |

### Query 94
- Text: What are the requirements for **Prerequisites** limited telepathy?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/3/Text/21']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/3/Text/21', 'PZO22001 Starfinder Player Core 058-073::/page/11/Text/23', 'PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/22']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/21` | 0.945401 | **Prerequisites** limited telepathy |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/23` | 0.945401 | **Prerequisites** limited telepathy |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/22` | 0.945401 | **Prerequisites** limited telepathy |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/25` | 0.903401 | **Prerequisites** limited telepathy |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/0/SectionHeader/12` | 0.618754 | LIMITED TELEPATHY |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/8/SectionHeader/14` | 0.618754 | LIMITED TELEPATHY |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/10/Text/23` | 0.569906 | Whether through training or innate talent,  you've expanded the range at which you can  telepathically communicate. Increase the range of  your limited telepathy by 15 feet. |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/26` | 0.557906 | Whether through training or innate talent, you've expanded  the range at which you can telepathically communicate.  Increase the range of your limited telepathy by 15 feet. |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/25` | 0.552556 | Your telepathy is stronger than most shirrens', allowing you to  combine physical, verbal, and telepathic communication. You  can transmit emotions alongside your messages whenever  you use limited te |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/22` | 0.539129 | When you use limited telepathy to communicate with another  creature, you act as a conduit for their thoughts, allowing them  to respond to you for a few scant moments—if they wish. The  creature can |

### Query 95
- Text: What is the rule about When you use limited telepathy to communicate with another  creature, you act as a conduit for their thoughts, allowing them  to respond to you for a few scant moments—if they wish. The  creature can give you a brief response as a reaction, or as a  free action at the beginning of their next turn as long as they  remain within range of your telepathy.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/3/Text/22']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/3/Text/22', 'PZO22001 Starfinder Player Core 058-073::/page/11/Text/24', 'PZO22001 Starfinder Player Core 058-073::/page/9/Text/25']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/22` | 1.001744 | When you use limited telepathy to communicate with another  creature, you act as a conduit for their thoughts, allowing them  to respond to you for a few scant moments—if they wish. The  creature can |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/24` | 0.907924 | When you use limited telepathy to communicate with another  creature, the creature can give you a brief response as a reaction,  or as a free action at the beginning of their next turn. |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/25` | 0.714711 | Your telepathy is stronger than most shirrens', allowing you to  combine physical, verbal, and telepathic communication. You  can transmit emotions alongside your messages whenever  you use limited te |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/0/Text/13` | 0.591816 | You can communicate mentally with creatures within 30 feet. You can communicate only with creatures that share a language with you. This doesn't give you any access to their thoughts and communicates |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/8/Text/15` | 0.591816 | You can communicate mentally with creatures within 30 feet. You can communicate only with creatures that share a language with you. This doesn't give you any access to their thoughts and communicates |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/23` | 0.547116 | **Prerequisites** limited telepathy |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/21` | 0.547116 | **Prerequisites** limited telepathy |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/26` | 0.544637 | Whether through training or innate talent, you've expanded  the range at which you can telepathically communicate.  Increase the range of your limited telepathy by 15 feet. |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/10/Text/23` | 0.544637 | Whether through training or innate talent,  you've expanded the range at which you can  telepathically communicate. Increase the range of  your limited telepathy by 15 feet. |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/22` | 0.535116 | **Prerequisites** limited telepathy |

### Query 96
- Text: What are the requirements for **GUARDED THOUGHTS** **FEAT 9**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/24']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/24', 'PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/32', 'PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/22']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/24` | 0.876835 | **GUARDED THOUGHTS** **FEAT 9** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/32` | 0.562869 | **PSYCHIC MASTER** **FEAT 9** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/22` | 0.561712 | **HARMONIC SHIELDING** **FEAT 9** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/28` | 0.516375 | **PSYCHIC MASTERY** **FEAT 9** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/26` | 0.461252 | **BASIC INSECTILE FLIGHT** **FEAT 9** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/26` | 0.459035 | **MELODIC ADAPTATION** **FEAT 9** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/13` | 0.450618 | **CENTER THOUGHTS **[free-action] **FEAT 1** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/15/SectionHeader/13` | 0.446122 | **ALL HANDS ON DECK **[free-action] **FEAT 9** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/15/SectionHeader/18` | 0.443091 | **HUSH **[one-action] **FEAT 9** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/48` | 0.439163 | **Prerequisites** Center Thoughts |

### Query 97
- Text: What is the rule about Your psychic training allows you to block attempts to read  your thoughts. Any effect that specifically attempts to read  your mind to glean information must succeed at a counteract  check against the higher of your class DC or your spell DC  to do so successfully; otherwise, it gains no information. The  counteract rank is equal to half your level rounded up.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/3/Text/27']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/3/Text/27', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/56', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/16']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/27` | 1.011751 | Your psychic training allows you to block attempts to read  your thoughts. Any effect that specifically attempts to read  your mind to glean information must succeed at a counteract  check against the |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/56` | 0.655286 | When a foe Casts a Spell that has the mental trait and you can  see or otherwise detect its manifestations, you use your psychic  powers to disrupt it. You expend 1 Focus Point to counter the  trigger |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/16` | 0.574853 | Your antennae are covered in fine hairs that make them  more sensitive to psychic vibrations than most. You gain  thoughtsense as a vague sense with a range of 30 feet. This  means you can use your an |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/43` | 0.516236 | You can use your telepathic abilities to quickly assess your  circumstances or subtly glean information from the minds of  others. You can cast *hypercognition* and *mind reading* as 3rdrank occult in |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/1/ListItem/7` | 0.515659 | Distrust your psychic abilities, fearing you'll read their  minds. |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/6/Text/14` | 0.508174 | You push yourself to be the best by competing with the  triggering ally. Until the end of your next turn, you can attempt  the same skill check to perform the same action or activity  that the trigger |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/58` | 0.494217 | You can shield your mind by using similar techniques that  your ancestors once mastered to escape the Swarm. You block  the intruding effect by scattering your thoughts, making you  immune to the trig |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/19` | 0.492762 | Your body can partially absorb persistent damage to learn  from it. Before you roll damage from a persistent effect, you  can choose to take half damage from the effect. When you do,  you automaticall |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/30` | 0.488082 | At 13th level, the rank of *detect magic* increases to 3rd. At  17th level, the rank of *detect magic* increases to 4th. |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/31` | 0.483299 | You've studied the lives and achievements of other  lashuntas who have improved both their psychic powers  and their communities. You gain the trained proficiency  rank in Occultism and Society. If yo |

### Query 98
- Text: What are the requirements for **PSYCHIC MASTERY** **FEAT 9**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/28']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/28', 'PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/32', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/60']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/28` | 0.883461 | **PSYCHIC MASTERY** **FEAT 9** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/32` | 0.859767 | **PSYCHIC MASTER** **FEAT 9** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/60` | 0.695716 | **Prerequisites** Psychic Mastery |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/1` | 0.569343 | **PSYCHIC TALENT** **FEAT 1** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/29` | 0.569343 | **PSYCHIC TALENT** **FEAT 1** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/31` | 0.560857 | **Prerequisites** Psychic Talent |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/35` | 0.560857 | **Prerequisites** Psychic Talent |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/26` | 0.526913 | **MELODIC ADAPTATION** **FEAT 9** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/9` | 0.514394 | **PSYCHIC SCHOLAR** **FEAT 5** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/24` | 0.506042 | **GUARDED THOUGHTS** **FEAT 9** |

### Query 99
- Text: What are the requirements for **Prerequisites** Psychic Talent?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/3/Text/31']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/11/Text/35', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/31', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/60']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/35` | 0.961200 | **Prerequisites** Psychic Talent |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/31` | 0.961200 | **Prerequisites** Psychic Talent |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/60` | 0.784352 | **Prerequisites** Psychic Mastery |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/42` | 0.723813 | **Prerequisites** Psychic Bully, Psychic Scholar, or Psychic Talent |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/1` | 0.635000 | **PSYCHIC TALENT** **FEAT 1** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/29` | 0.635000 | **PSYCHIC TALENT** **FEAT 1** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/25` | 0.484275 | **Prerequisites** limited telepathy |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/21` | 0.484275 | **Prerequisites** limited telepathy |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/23` | 0.484275 | **Prerequisites** limited telepathy |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/22` | 0.484275 | **Prerequisites** limited telepathy |

### Query 100
- Text: What is the rule about Your psychic abilities have grown stronger, allowing you to  tap into entirely new dimensions of psychic power. Choose  one common 2nd-rank spell from the occult spell list. You can  cast that spell as an occult innate spell once per day.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/3/Text/32']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/3/Text/32', 'PZO22001 Starfinder Player Core 058-073::/page/11/Text/36', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/61']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/32` | 0.990186 | Your psychic abilities have grown stronger, allowing you to  tap into entirely new dimensions of psychic power. Choose  one common 2nd-rank spell from the occult spell list. You can  cast that spell a |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/36` | 0.971458 | Your psychic abilities have grown stronger. Choose one  common 2nd-rank spell from the occult spell list. You can cast  that spell as an occult innate spell once per day. |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/61` | 0.909913 | Your psychic abilities have grown stronger. Choose one  common 6th-rank spell from the occult spell list. You can cast  that spell as an occult innate spell once per day. |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/10/Text/32` | 0.730255 | Your psychic abilities have developed beyond simple  communication. Choose one cantrip from the occult spell list. You  can cast this cantrip as an occult innate spell at will. A cantrip is  heightene |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/3` | 0.730255 | Your psychic abilities have developed beyond simple  communication. Choose one cantrip from the occult spell list. You  can cast this cantrip as an occult innate spell at will. A cantrip is  heightene |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/43` | 0.671524 | You can use your telepathic abilities to quickly assess your  circumstances or subtly glean information from the minds of  others. You can cast *hypercognition* and *mind reading* as 3rdrank occult in |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/8` | 0.625506 | **Prerequisites** korasha lashunta or unbound lashunta heritage You can leverage your telepathic abilities to influence the  minds of others, imparting orders or inflaming fears. You can  cast *comman |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/46` | 0.615629 | Your mastery of language reaches supernatural levels. You can  cast *truespeech* as a 5th-rank occult innate spell once per day on  yourself only. You gain a +1 status bonus to Diplomacy checks  for t |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/12` | 0.598890 | **Prerequisites** damaya lashunta or unbound lashunta heritage You can transfer vast amounts of information to the minds of  others in mere moments. You can cast *mindlink* as a 1st-rank  occult innat |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/41` | 0.579897 | You never let the inability to communicate stop you from  chatting with nufriends! You gain *speak with animals* as  a 2nd-rank primal innate spell, and *speak with plants* and  *translate* as 3rd-ran |

### Query 101
- Text: What are the requirements for **FOCUS PHEROMONES **[one-action] **FEAT 13**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/34']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/34', 'PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/18', 'PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/9']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/34` | 0.919391 | **FOCUS PHEROMONES **[one-action] **FEAT 13** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/18` | 0.613666 | **COMMANDING PHEROMONES** **FEAT 1** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/9` | 0.606192 | **ALLURING PHEROMONES** **FEAT 1** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/15/SectionHeader/48` | 0.521050 | **SUPERSONIC SPEED** **FEAT 13** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/15/SectionHeader/38` | 0.511587 | **CHATTERMANDER** **FEAT 13** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/43` | 0.494867 | **LINGUISTIC MASTER** **FEAT 13** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/37` | 0.488075 | **REMIX WORLD'S RHYTHM** **FEAT 13** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/42` | 0.487170 | **SCRUPULOUS STALKER **[free-action] **FEAT 13** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/39` | 0.485001 | **PSYCHIC INVESTIGATOR** **FEAT 13** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/15/SectionHeader/31` | 0.468983 | **ZOOMIES **[one-action] **FEAT 9** |

### Query 102
- Text: What is the rule about You can purposefully deploy your pheromones to manipulate  the reactions of those around you. If your next action is to  attempt a Deception check to Create a Diversion, a Diplomacy  check to Request, or an Intimidation check to Demoralize, roll  that skill check twice and use the better result.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/3/Text/38']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/3/Text/38', 'PZO22001 Starfinder Player Core 058-073::/page/2/Text/12', 'PZO22001 Starfinder Player Core 058-073::/page/2/Text/21']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/38` | 0.995659 | You can purposefully deploy your pheromones to manipulate  the reactions of those around you. If your next action is to  attempt a Deception check to Create a Diversion, a Diplomacy  check to Request, |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/12` | 0.670330 | You influence others with pheromones, even when you lack  other means of communication. You can use Diplomacy  to Make an Impression on creatures with whom you don't  share a language and to make simp |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/21` | 0.628080 | You can leverage your alluring pheromones to soothe ill will  and take the edge off your threats, turning your attempts  at coercion into acts of leadership. When you Coerce a  creature, if your targe |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/6/Text/14` | 0.532754 | You push yourself to be the best by competing with the  triggering ally. Until the end of your next turn, you can attempt  the same skill check to perform the same action or activity  that the trigger |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/10/Text/18` | 0.491258 | You broadcast helpful encouragement or pertinent information  to your ally's mind. Your ally rerolls the triggering skill check and  takes the better result. |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/27` | 0.481405 | Despite the passage of time, you remain resolute in your  defiance of the Swarm and all forms of mental control. If you  roll a success on a Will saving throw against an effect that  was created by a |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/27` | 0.466605 | Your psychic training allows you to block attempts to read  your thoughts. Any effect that specifically attempts to read  your mind to glean information must succeed at a counteract  check against the |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/59` | 0.457358 | You put forth your best effort and focus everything you've  got on the task at hand, putting allsix of your hands (three  of your sets of arms) into it! The next time you roll an attack  roll or skill |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/15` | 0.456742 | You love helping your friends and allies achieve their goals. At  the start of your turn, you gain one additional reaction, which  you can use only to Aid. |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/4` | 0.451485 | Your ability to adapt to various beliefs instills you with  knowledge of many cultures. You gain the trained proficiency  rank in Diplomacy and Society. If you would automatically  become trained in o |

### Query 103
- Text: What are the requirements for **PSYCHIC INVESTIGATOR** **FEAT 13**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/39']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/39', 'PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/43', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/31']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/39` | 0.846966 | **PSYCHIC INVESTIGATOR** **FEAT 13** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/43` | 0.604594 | **LINGUISTIC MASTER** **FEAT 13** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/31` | 0.581615 | **Prerequisites** Psychic Talent |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/35` | 0.539615 | **Prerequisites** Psychic Talent |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/60` | 0.520002 | **Prerequisites** Psychic Mastery |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/29` | 0.518667 | **PSYCHIC TALENT** **FEAT 1** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/1` | 0.518667 | **PSYCHIC TALENT** **FEAT 1** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/42` | 0.514416 | **Prerequisites** Psychic Bully, Psychic Scholar, or Psychic Talent |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/32` | 0.512736 | **PSYCHIC MASTER** **FEAT 9** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/28` | 0.507883 | **PSYCHIC MASTERY** **FEAT 9** |

### Query 104
- Text: What are the requirements for **Prerequisites** Psychic Bully, Psychic Scholar, or Psychic Talent?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/3/Text/42']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/3/Text/42', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/31', 'PZO22001 Starfinder Player Core 058-073::/page/11/Text/35']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/42` | 0.986978 | **Prerequisites** Psychic Bully, Psychic Scholar, or Psychic Talent |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/31` | 0.802950 | **Prerequisites** Psychic Talent |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/35` | 0.802950 | **Prerequisites** Psychic Talent |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/60` | 0.667436 | **Prerequisites** Psychic Mastery |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/1` | 0.516002 | **PSYCHIC TALENT** **FEAT 1** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/29` | 0.516002 | **PSYCHIC TALENT** **FEAT 1** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/5` | 0.494256 | **PSYCHIC BULLY** **FEAT 5** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/31` | 0.456647 | You've studied the lives and achievements of other  lashuntas who have improved both their psychic powers  and their communities. You gain the trained proficiency  rank in Occultism and Society. If yo |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/9` | 0.444139 | **PSYCHIC SCHOLAR** **FEAT 5** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/40` | 0.404483 | **Prerequisites** expert in Performance |

### Query 105
- Text: What is the rule about You can use your telepathic abilities to quickly assess your  circumstances or subtly glean information from the minds of  others. You can cast *hypercognition* and *mind reading* as 3rdrank occult innate spells. You can cast each of these occult  innate spells once per day.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/3/Text/43']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/3/Text/43', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/8', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/32']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/43` | 0.992515 | You can use your telepathic abilities to quickly assess your  circumstances or subtly glean information from the minds of  others. You can cast *hypercognition* and *mind reading* as 3rdrank occult in |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/8` | 0.714337 | **Prerequisites** korasha lashunta or unbound lashunta heritage You can leverage your telepathic abilities to influence the  minds of others, imparting orders or inflaming fears. You can  cast *comman |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/32` | 0.702910 | Your psychic abilities have grown stronger, allowing you to  tap into entirely new dimensions of psychic power. Choose  one common 2nd-rank spell from the occult spell list. You can  cast that spell a |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/36` | 0.660572 | Your psychic abilities have grown stronger. Choose one  common 2nd-rank spell from the occult spell list. You can cast  that spell as an occult innate spell once per day. |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/61` | 0.631353 | Your psychic abilities have grown stronger. Choose one  common 6th-rank spell from the occult spell list. You can cast  that spell as an occult innate spell once per day. |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/3` | 0.619407 | Your psychic abilities have developed beyond simple  communication. Choose one cantrip from the occult spell list. You  can cast this cantrip as an occult innate spell at will. A cantrip is  heightene |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/10/Text/32` | 0.619407 | Your psychic abilities have developed beyond simple  communication. Choose one cantrip from the occult spell list. You  can cast this cantrip as an occult innate spell at will. A cantrip is  heightene |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/46` | 0.608996 | Your mastery of language reaches supernatural levels. You can  cast *truespeech* as a 5th-rank occult innate spell once per day on  yourself only. You gain a +1 status bonus to Diplomacy checks  for t |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/12` | 0.595152 | **Prerequisites** damaya lashunta or unbound lashunta heritage You can transfer vast amounts of information to the minds of  others in mere moments. You can cast *mindlink* as a 1st-rank  occult innat |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/41` | 0.591257 | You never let the inability to communicate stop you from  chatting with nufriends! You gain *speak with animals* as  a 2nd-rank primal innate spell, and *speak with plants* and  *translate* as 3rd-ran |

### Query 106
- Text: What are the requirements for **CENTERED MIND** **FEAT 17**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/45']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/45', 'PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/50', 'PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/57']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/45` | 0.882893 | **CENTERED MIND** **FEAT 17** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/50` | 0.565949 | **MENTAL DEFLECTION **[reaction] **FEAT 17** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/57` | 0.526751 | **PSYCHIC PARAGON** **FEAT 17** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/53` | 0.481934 | **SCATTER THOUGHTS **[reaction] **FEAT 17** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/15/SectionHeader/60` | 0.478339 | **BOUNDLESS ENERGY** **FEAT 17** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/15/SectionHeader/54` | 0.456352 | **ALLSIX **[one-action] **FEAT 17** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/48` | 0.453782 | **Prerequisites** Center Thoughts |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/44` | 0.451695 | 17TH LEVEL |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/52` | 0.443062 | **SONG OF MY PEOPLE** **FEAT 17** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/47` | 0.439695 | 17TH LEVEL |

### Query 107
- Text: What are the requirements for **Prerequisites** Center Thoughts?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/3/Text/48']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/3/Text/48', 'PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/13', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/49']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/48` | 0.954368 | **Prerequisites** Center Thoughts |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/13` | 0.527309 | **CENTER THOUGHTS **[free-action] **FEAT 1** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/49` | 0.515455 | You know your own mind and instinctively resist attempts to  unbalance your thoughts or control your emotions. You can  use Center Thoughts once per hour, rather than once per day. |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/55` | 0.406566 | **Requirements** You have at least 1 Focus Point. |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/41` | 0.403055 | **Prerequisites** Communalism |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/31` | 0.396993 | **Prerequisites** Psychic Talent |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/35` | 0.396993 | **Prerequisites** Psychic Talent |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/53` | 0.392020 | **Prerequisites** expert in Occultism, focus pool |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/34` | 0.389071 | **Prerequisites** Hyper |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/23` | 0.372172 | **Prerequisites** limited telepathy |

### Query 108
- Text: What are the requirements for **MENTAL DEFLECTION **[reaction] **FEAT 17**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/50']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/50', 'PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/53', 'PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/57']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/50` | 0.906770 | **MENTAL DEFLECTION **[reaction] **FEAT 17** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/53` | 0.607612 | **SCATTER THOUGHTS **[reaction] **FEAT 17** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/57` | 0.578723 | **PSYCHIC PARAGON** **FEAT 17** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/45` | 0.522217 | **CENTERED MIND** **FEAT 17** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/15/SectionHeader/54` | 0.476560 | **ALLSIX **[one-action] **FEAT 17** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/15/SectionHeader/60` | 0.467580 | **BOUNDLESS ENERGY** **FEAT 17** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/29` | 0.449264 | **PSYCHIC TALENT** **FEAT 1** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/1` | 0.449264 | **PSYCHIC TALENT** **FEAT 1** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/52` | 0.447051 | **SONG OF MY PEOPLE** **FEAT 17** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/52` | 0.431450 | 17TH LEVEL |

### Query 109
- Text: What are the requirements for **Prerequisites** expert in Occultism, focus pool?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/3/Text/53']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/3/Text/53', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/55', 'PZO22001 Starfinder Player Core 058-073::/page/2/Text/31']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/53` | 0.966177 | **Prerequisites** expert in Occultism, focus pool |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/55` | 0.576394 | **Requirements** You have at least 1 Focus Point. |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/31` | 0.545842 | You've studied the lives and achievements of other  lashuntas who have improved both their psychic powers  and their communities. You gain the trained proficiency  rank in Occultism and Society. If yo |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/31` | 0.472718 | **Prerequisites** Psychic Talent |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/35` | 0.472718 | **Prerequisites** Psychic Talent |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/40` | 0.460058 | **Prerequisites** expert in Performance |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/48` | 0.446154 | **Prerequisites** Center Thoughts |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/60` | 0.443304 | **Prerequisites** Psychic Mastery |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/42` | 0.440781 | **Prerequisites** Psychic Bully, Psychic Scholar, or Psychic Talent |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/22` | 0.426182 | **Prerequisites** limited telepathy |

### Query 110
- Text: What is the rule about **Trigger** A creature Casts a Spell with the mental trait.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/3/Text/54']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/3/Text/54', 'PZO22001 Starfinder Player Core 058-073::/page/11/Text/57', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/56']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/54` | 0.946250 | **Trigger** A creature Casts a Spell with the mental trait. |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/57` | 0.713221 | **Trigger** You're targeted by a mental effect. |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/56` | 0.678622 | When a foe Casts a Spell that has the mental trait and you can  see or otherwise detect its manifestations, you use your psychic  powers to disrupt it. You expend 1 Focus Point to counter the  trigger |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/45` | 0.634097 | **Trigger** A creature critically fails a melee Strike against you. **Requirements** The triggering creature is within your reach,  you have at least one free active hand, and your target is  no more |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/17` | 0.601973 | **Trigger** You fail a Will saving throw against a mental effect. You center your thoughts and focus your mind, shaking off  emotional turmoil and harmful mental intrusions. Reroll the  triggering sav |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/4` | 0.567652 | **Unbound Mind **[reaction] **Trigger** You attempt a saving throw against  a mental effect, but you haven't rolled yet; **Effect** You refuse  to conform to the will of others, shaking off their atte |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/6/Text/13` | 0.547890 | **Trigger** An ally attempts a skill check with a skill that you have  trained or better proficiency rank in. |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/6/Text/14` | 0.520358 | You push yourself to be the best by competing with the  triggering ally. Until the end of your next turn, you can attempt  the same skill check to perform the same action or activity  that the trigger |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/11` | 0.480125 | **Beginner's** **Luck** [free-action] (fortune) **Frequency** once per day;  **Trigger** You fail a skill check using a skill that you're  untrained in; **Effect** Reroll the triggering check and use |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/10/Text/18` | 0.469191 | You broadcast helpful encouragement or pertinent information  to your ally's mind. Your ally rerolls the triggering skill check and  takes the better result. |

### Query 111
- Text: What is the rule about When a foe Casts a Spell that has the mental trait and you can  see or otherwise detect its manifestations, you use your psychic  powers to disrupt it. You expend 1 Focus Point to counter the  triggering creature's casting of the spell. You then attempt  to counteract the triggering spell using your spellcasting  attribute modifier plus your spellcasting proficiency bonus as  your counteract modifier and half your level, rounded up, as  your counteract rank.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/3/Text/56']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/3/Text/56', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/54', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/27']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/56` | 0.972820 | When a foe Casts a Spell that has the mental trait and you can  see or otherwise detect its manifestations, you use your psychic  powers to disrupt it. You expend 1 Focus Point to counter the  trigger |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/54` | 0.664117 | **Trigger** A creature Casts a Spell with the mental trait. |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/27` | 0.661081 | Your psychic training allows you to block attempts to read  your thoughts. Any effect that specifically attempts to read  your mind to glean information must succeed at a counteract  check against the |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/6/Text/14` | 0.581286 | You push yourself to be the best by competing with the  triggering ally. Until the end of your next turn, you can attempt  the same skill check to perform the same action or activity  that the trigger |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/4` | 0.514041 | **Unbound Mind **[reaction] **Trigger** You attempt a saving throw against  a mental effect, but you haven't rolled yet; **Effect** You refuse  to conform to the will of others, shaking off their atte |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/17` | 0.506210 | **Trigger** You fail a Will saving throw against a mental effect. You center your thoughts and focus your mind, shaking off  emotional turmoil and harmful mental intrusions. Reroll the  triggering sav |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/57` | 0.500345 | **Trigger** You're targeted by a mental effect. |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/27` | 0.499634 | Despite the passage of time, you remain resolute in your  defiance of the Swarm and all forms of mental control. If you  roll a success on a Will saving throw against an effect that  was created by a |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/3` | 0.499507 | Your psychic abilities have developed beyond simple  communication. Choose one cantrip from the occult spell list. You  can cast this cantrip as an occult innate spell at will. A cantrip is  heightene |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/10/Text/32` | 0.499507 | Your psychic abilities have developed beyond simple  communication. Choose one cantrip from the occult spell list. You  can cast this cantrip as an occult innate spell at will. A cantrip is  heightene |

### Query 112
- Text: What are the requirements for **PSYCHIC PARAGON** **FEAT 17**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/57']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/57', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/31', 'PZO22001 Starfinder Player Core 058-073::/page/11/Text/35']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/57` | 0.880271 | **PSYCHIC PARAGON** **FEAT 17** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/31` | 0.586799 | **Prerequisites** Psychic Talent |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/35` | 0.586799 | **Prerequisites** Psychic Talent |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/60` | 0.528916 | **Prerequisites** Psychic Mastery |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/50` | 0.515388 | **MENTAL DEFLECTION **[reaction] **FEAT 17** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/1` | 0.501337 | **PSYCHIC TALENT** **FEAT 1** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/29` | 0.501337 | **PSYCHIC TALENT** **FEAT 1** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/28` | 0.500761 | **PSYCHIC MASTERY** **FEAT 9** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/32` | 0.489539 | **PSYCHIC MASTER** **FEAT 9** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/9` | 0.472991 | **PSYCHIC SCHOLAR** **FEAT 5** |

### Query 113
- Text: What are the requirements for **Prerequisites** Psychic Mastery?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/3/Text/60']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/3/Text/60', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/31', 'PZO22001 Starfinder Player Core 058-073::/page/11/Text/35']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/60` | 0.952315 | **Prerequisites** Psychic Mastery |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/31` | 0.796330 | **Prerequisites** Psychic Talent |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/35` | 0.796330 | **Prerequisites** Psychic Talent |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/42` | 0.643076 | **Prerequisites** Psychic Bully, Psychic Scholar, or Psychic Talent |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/28` | 0.481885 | **PSYCHIC MASTERY** **FEAT 9** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/21` | 0.458149 | **Prerequisites** limited telepathy |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/22` | 0.458149 | **Prerequisites** limited telepathy |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/23` | 0.458149 | **Prerequisites** limited telepathy |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/25` | 0.458149 | **Prerequisites** limited telepathy |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/29` | 0.450052 | **PSYCHIC TALENT** **FEAT 1** |

### Query 114
- Text: What is the rule about Your psychic abilities have grown stronger. Choose one  common 6th-rank spell from the occult spell list. You can cast  that spell as an occult innate spell once per day.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/3/Text/61']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/3/Text/61', 'PZO22001 Starfinder Player Core 058-073::/page/11/Text/36', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/32']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/61` | 0.988035 | Your psychic abilities have grown stronger. Choose one  common 6th-rank spell from the occult spell list. You can cast  that spell as an occult innate spell once per day. |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/36` | 0.928895 | Your psychic abilities have grown stronger. Choose one  common 2nd-rank spell from the occult spell list. You can cast  that spell as an occult innate spell once per day. |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/32` | 0.908307 | Your psychic abilities have grown stronger, allowing you to  tap into entirely new dimensions of psychic power. Choose  one common 2nd-rank spell from the occult spell list. You can  cast that spell a |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/10/Text/32` | 0.699591 | Your psychic abilities have developed beyond simple  communication. Choose one cantrip from the occult spell list. You  can cast this cantrip as an occult innate spell at will. A cantrip is  heightene |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/3` | 0.699591 | Your psychic abilities have developed beyond simple  communication. Choose one cantrip from the occult spell list. You  can cast this cantrip as an occult innate spell at will. A cantrip is  heightene |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/43` | 0.637744 | You can use your telepathic abilities to quickly assess your  circumstances or subtly glean information from the minds of  others. You can cast *hypercognition* and *mind reading* as 3rdrank occult in |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/46` | 0.607432 | Your mastery of language reaches supernatural levels. You can  cast *truespeech* as a 5th-rank occult innate spell once per day on  yourself only. You gain a +1 status bonus to Diplomacy checks  for t |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/8` | 0.589559 | **Prerequisites** korasha lashunta or unbound lashunta heritage You can leverage your telepathic abilities to influence the  minds of others, imparting orders or inflaming fears. You can  cast *comman |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/12` | 0.570518 | **Prerequisites** damaya lashunta or unbound lashunta heritage You can transfer vast amounts of information to the minds of  others in mere moments. You can cast *mindlink* as a 1st-rank  occult innat |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/41` | 0.554743 | You never let the inability to communicate stop you from  chatting with nufriends! You gain *speak with animals* as  a 2nd-rank primal innate spell, and *speak with plants* and  *translate* as 3rd-ran |

### Query 115
- Text: What is the rule about **ANCESTRIES & ** **BACKGROUNDS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/3/Text/64']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/30', 'PZO22001 Starfinder Player Core 058-073::/page/5/Text/30', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/64']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/30` | 0.920820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/30` | 0.920820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/64` | 0.920820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/13/Text/31` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/31` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/67` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/66` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/58` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/43` | 0.526957 | **Backgrounds** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/43` | 0.526957 | **Backgrounds** |

### Query 116
- Text: What is the rule about **Backgrounds**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/3/Text/77']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/3/Text/77', 'PZO22001 Starfinder Player Core 058-073::/page/7/Text/71', 'PZO22001 Starfinder Player Core 058-073::/page/15/Text/81']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/77` | 0.796516 | **Backgrounds** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/81` | 0.796516 | **Backgrounds** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/71` | 0.796516 | **Backgrounds** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/43` | 0.754516 | **Backgrounds** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/43` | 0.754516 | **Backgrounds** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/80` | 0.754516 | **Backgrounds** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/43` | 0.661389 | **Backgrounds** **Languages** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/13/Text/44` | 0.661389 | **Backgrounds** **Languages** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/31` | 0.510451 | **ANCESTRIES & ** **BACKGROUNDS** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/58` | 0.510451 | **ANCESTRIES & ** **BACKGROUNDS** |

### Query 117
- Text: What is the rule about **SKILLS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/3/Text/80']
- Expected found: `True`
- Expected rank: `4`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/9/Text/45', 'PZO22001 Starfinder Player Core 058-073::/page/7/Text/74', 'PZO22001 Starfinder Player Core 058-073::/page/13/Text/46']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/45` | 0.864442 | **SKILLS** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/74` | 0.864442 | **SKILLS** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/13/Text/46` | 0.864442 | **SKILLS** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/80` | 0.822442 | **SKILLS** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/45` | 0.822442 | **SKILLS** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/84` | 0.822442 | **SKILLS** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/83` | 0.651094 | **SKILLS** **FEATS** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/46` | 0.651094 | **SKILLS** **FEATS** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/22` | 0.490741 | You fall utterly silent and focus strenuously on a problem  at hand. You attempt to Recall Knowledge with a +2  circumstance bonus to the skill check. If you would get a  critical failure, you get a f |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/4` | 0.437417 | Your ability to adapt to various beliefs instills you with  knowledge of many cultures. You gain the trained proficiency  rank in Diplomacy and Society. If you would automatically  become trained in o |

### Query 118
- Text: What is the rule about **FEATS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/3/Text/81']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/46', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/81', 'PZO22001 Starfinder Player Core 058-073::/page/13/Text/47']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/46` | 0.871817 | **FEATS** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/81` | 0.871817 | **FEATS** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/13/Text/47` | 0.871817 | **FEATS** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/75` | 0.829817 | **FEATS** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/46` | 0.829817 | **FEATS** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/85` | 0.829817 | **FEATS** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/83` | 0.653037 | **SKILLS** **FEATS** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/46` | 0.653037 | **SKILLS** **FEATS** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/3` | 0.442859 | **PREDATORY** **FEAT 1** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/14/SectionHeader/26` | 0.435722 | **HYPER** **FEAT 1** |

### Query 119
- Text: What is the rule about **SPELLS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/3/Text/83']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/9/Text/48', 'PZO22001 Starfinder Player Core 058-073::/page/1/Text/48', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/83']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/48` | 0.889304 | **SPELLS** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/48` | 0.889304 | **SPELLS** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/83` | 0.889304 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/77` | 0.847304 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/48` | 0.847304 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/85` | 0.847304 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/13/Text/49` | 0.847304 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/87` | 0.740792 | **SPELLS** **PLAYING THE ** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/74` | 0.388254 | **SKILLS** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/13/Text/46` | 0.388254 | **SKILLS** |

### Query 120
- Text: What is the rule about Pahtras are a humanoid feline species from a nearby star system. They're highly competitive and known for their achievements in magic, music, and war. Their home world was recently freed from the Veskarium's occupation, and they've joined the Pact Worlds.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/4/Text/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/4/Text/2', 'PZO22001 Starfinder Player Core 058-073::/page/5/Text/9', 'PZO22001 Starfinder Player Core 058-073::/page/5/Text/12']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/4/Text/2` | 0.984562 | Pahtras are a humanoid feline species from a nearby star system. They're highly competitive and known for their achievements in magic, music, and war. Their home world was recently freed from the Vesk |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/9` | 0.725527 | Pahtras evolved on a low-gravity jungle world called Pulonis,  where they fought a long war for independence from their  Veskarium conquerors. Recently, pahtra freedom fighters  defeated the last Vesk |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/12` | 0.703317 | Pahtras are feline humanoids covered in fur. Their coats vary  from black, white, blue, calico, bi-colored, and tabby, often  possessing unique patterns of irregular shapes that seers  traditionally u |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/15` | 0.603866 | Pahtra cultures are steeped in tradition and highly competitive,  with individuals vying for recognition and resources in a  struggle that mimics the harsh natural order of their planet.  Before the V |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/20` | 0.569727 | Many pahtras cling fiercely to their ancestral Pulonian  traditions in an effort to keep their cultures alive after  enduring generations of oppression by the Veskarium.  Pulonian culture values perso |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/10` | 0.565942 | If you want to play a character who fights for freedom with  grace and style, you should play a pahtra. |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/6/Text/5` | 0.559709 | Your ancestors roamed blasted terrain leached of vital nutrients  by the Veskarium. You're shorter and stockier than most  pahtras, with wide, tufted ears and fur-covered paw pads. Your  size is Small |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/13` | 0.517195 | Pahtras have sharp teeth and retractable claws on their  hands and feet. They have a unique set of sensory organs  across their muzzles, with functions varying from individual  to individual. The most |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/4/SectionHeader/1` | 0.511119 | **PAHTRA ** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/35` | 0.506031 | **Pahtra** |

### Query 121
- Text: What is the rule about Additional languages equal to your Intelligence modifier (if it's positive). Choose from the list of common languages and any other languages to which you have access (such as the languages prevalent on your home world).?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/4/Text/11']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/0/Text/9', 'PZO22001 Starfinder Player Core 058-073::/page/4/Text/11', 'PZO22001 Starfinder Player Core 058-073::/page/12/Text/9']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/0/Text/9` | 0.982267 | Additional languages equal to your Intelligence modifier (if it's positive). Choose from the list of common languages and any other languages to which you have access (such as the languages prevalent |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/4/Text/11` | 0.982267 | Additional languages equal to your Intelligence modifier (if it's positive). Choose from the list of common languages and any other languages to which you have access (such as the languages prevalent |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/12/Text/9` | 0.982267 | Additional languages equal to your Intelligence modifier (if it's positive). Choose from the list of common languages and any other languages to which you have access (such as the languages prevalent |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/8/Text/11` | 0.905517 | One regional language of your choice Additional languages equal to your Intelligence modifier (if it's positive). Choose from the list of common languages and any other languages to which you have acc |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/10/Text/28` | 0.584960 | Learning new languages comes naturally to you. You gain two  additional languages of your choice, chosen from among the  common and uncommon languages available to you. Every time  you take the Multil |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/25` | 0.486165 | You've chosen the adaptive genetics to become a damaya. You  might have a leaner, lither body type than other lashuntas and  are likely encouraged to pursue work as a scholar or politician.  In additi |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/4` | 0.477043 | Your ability to adapt to various beliefs instills you with  knowledge of many cultures. You gain the trained proficiency  rank in Diplomacy and Society. If you would automatically  become trained in o |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/12/Text/8` | 0.455123 | One regional language of your choice |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/13/Text/44` | 0.450809 | **Backgrounds** **Languages** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/43` | 0.450809 | **Backgrounds** **Languages** |

### Query 122
- Text: What is the rule about **TRAITS **?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/4/SectionHeader/12']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/0/SectionHeader/10', 'PZO22001 Starfinder Player Core 058-073::/page/4/SectionHeader/12', 'PZO22001 Starfinder Player Core 058-073::/page/12/SectionHeader/10']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/0/SectionHeader/10` | 0.867974 | **TRAITS ** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/4/SectionHeader/12` | 0.867974 | **TRAITS ** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/12/SectionHeader/10` | 0.769948 | TRAITS |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/8/SectionHeader/12` | 0.739948 | TRAITS |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/74` | 0.464114 | **SKILLS** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/13/Text/46` | 0.464114 | **SKILLS** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/45` | 0.464114 | **SKILLS** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/84` | 0.464114 | **SKILLS** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/80` | 0.464114 | **SKILLS** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/45` | 0.464114 | **SKILLS** |

### Query 123
- Text: What is the rule about You can see in darkness and dim light just as well as you can see in bright light, though your vision in darkness is in black and white.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/4/Text/15']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/4/Text/15', 'PZO22001 Starfinder Player Core 058-073::/page/12/Text/13', 'PZO22001 Starfinder Player Core 058-073::/page/14/Text/1']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/4/Text/15` | 0.960207 | You can see in darkness and dim light just as well as you can see in bright light, though your vision in darkness is in black and white. |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/12/Text/13` | 0.632435 | You can see in dim light as though it were bright light, and you ignore the concealed condition due to dim light. |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/14/Text/1` | 0.521613 | pale-colored fur, a slender build, and large, luminous eyes. You  gain darkvision. |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/12/SectionHeader/12` | 0.394267 | **LOW-LIGHT VISION ** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/4/SectionHeader/14` | 0.377690 | DARKVISION |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/16` | 0.361421 | Your antennae are covered in fine hairs that make them  more sensitive to psychic vibrations than most. You gain  thoughtsense as a vague sense with a range of 30 feet. This  means you can use your an |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/46` | 0.352645 | You quickly scan your surroundings for threats. You Seek. If  you use electromagnetic sense, you gain a +2 circumstance  bonus to this check. |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/20` | 0.351103 | You've honed your whiskers' sensitivity to the degree that you  can sense the movement of the weak electric fields emitted  by potential enemies. You gain electromagnetic sense as an  imprecise sense |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/4` | 0.349309 | Your ability to adapt to various beliefs instills you with  knowledge of many cultures. You gain the trained proficiency  rank in Diplomacy and Society. If you would automatically  become trained in o |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/25` | 0.343068 | Your telepathy is stronger than most shirrens', allowing you to  combine physical, verbal, and telepathic communication. You  can transmit emotions alongside your messages whenever  you use limited te |

### Query 124
- Text: What is the rule about Pahtras evolved on a low-gravity jungle world called Pulonis,  where they fought a long war for independence from their  Veskarium conquerors. Recently, pahtra freedom fighters  defeated the last Veskarium occupiers, then voted to join the  Pact Worlds as a sovereign planet. Today, Pulonis is a lush,  verdant world wracked by dangerous magnetic storms and  scarred by the Veskarium's brutal invasion. The struggles of  survival have influenced many pahtra traditions, leading to a  culture of competitive war games, time-honored mysticism,  and unorthodox technology. Music accompanies everything  in pahtra culture, from popular entertainment to traditional  battle tactics, with martial combat even categorized as a form  of battle dance.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/5/Text/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/5/Text/9', 'PZO22001 Starfinder Player Core 058-073::/page/5/Text/20', 'PZO22001 Starfinder Player Core 058-073::/page/5/Text/15']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/9` | 1.009894 | Pahtras evolved on a low-gravity jungle world called Pulonis,  where they fought a long war for independence from their  Veskarium conquerors. Recently, pahtra freedom fighters  defeated the last Vesk |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/20` | 0.809877 | Many pahtras cling fiercely to their ancestral Pulonian  traditions in an effort to keep their cultures alive after  enduring generations of oppression by the Veskarium.  Pulonian culture values perso |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/15` | 0.796805 | Pahtra cultures are steeped in tradition and highly competitive,  with individuals vying for recognition and resources in a  struggle that mimics the harsh natural order of their planet.  Before the V |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/4/Text/2` | 0.637154 | Pahtras are a humanoid feline species from a nearby star system. They're highly competitive and known for their achievements in magic, music, and war. Their home world was recently freed from the Vesk |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/10` | 0.587740 | If you want to play a character who fights for freedom with  grace and style, you should play a pahtra. |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/6/Text/5` | 0.564269 | Your ancestors roamed blasted terrain leached of vital nutrients  by the Veskarium. You're shorter and stockier than most  pahtras, with wide, tufted ears and fur-covered paw pads. Your  size is Small |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/12` | 0.503970 | Pahtras are feline humanoids covered in fur. Their coats vary  from black, white, blue, calico, bi-colored, and tabby, often  possessing unique patterns of irregular shapes that seers  traditionally u |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/16` | 0.489811 | picturesque cities along the shores and wildlands of Castrovel,  a lush jungle world teeming with dangerous predators and  extreme weather. These independent settlements are protected  by a mighty mil |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/6/Text/25` | 0.481980 | You're an expert in both the traditional and modern pahtra |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/6/Text/7` | 0.478637 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As a pahtra, you choose from among the  following an |

### Query 125
- Text: What is the rule about If you want to play a character who fights for freedom with  grace and style, you should play a pahtra.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/5/Text/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/5/Text/10', 'PZO22001 Starfinder Player Core 058-073::/page/6/Text/7', 'PZO22001 Starfinder Player Core 058-073::/page/6/Text/25']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/10` | 0.936330 | If you want to play a character who fights for freedom with  grace and style, you should play a pahtra. |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/6/Text/7` | 0.621463 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As a pahtra, you choose from among the  following an |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/6/Text/25` | 0.601094 | You're an expert in both the traditional and modern pahtra |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/20` | 0.526610 | Many pahtras cling fiercely to their ancestral Pulonian  traditions in an effort to keep their cultures alive after  enduring generations of oppression by the Veskarium.  Pulonian culture values perso |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/9` | 0.519803 | Pahtras evolved on a low-gravity jungle world called Pulonis,  where they fought a long war for independence from their  Veskarium conquerors. Recently, pahtra freedom fighters  defeated the last Vesk |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/6/Text/24` | 0.504514 | **PAHTRA** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/6/Text/5` | 0.498468 | Your ancestors roamed blasted terrain leached of vital nutrients  by the Veskarium. You're shorter and stockier than most  pahtras, with wide, tufted ears and fur-covered paw pads. Your  size is Small |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/10` | 0.494323 | If you want to play a character who strives for selfimprovement and has innate psychic abilities, you should play  a lashunta. |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/6/Text/16` | 0.492514 | **PAHTRA** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/54` | 0.492514 | **PAHTRA** |

### Query 126
- Text: What are the requirements for **COMPETITIVE SPIRIT **[reaction] **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/6/SectionHeader/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/6/SectionHeader/9', 'PZO22001 Starfinder Player Core 058-073::/page/6/Text/14', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/1']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/6/SectionHeader/9` | 0.884213 | **COMPETITIVE SPIRIT **[reaction] **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/6/Text/14` | 0.527279 | You push yourself to be the best by competing with the  triggering ally. Until the end of your next turn, you can attempt  the same skill check to perform the same action or activity  that the trigger |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/1` | 0.488330 | **PSYCHIC TALENT** **FEAT 1** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/29` | 0.458330 | **PSYCHIC TALENT** **FEAT 1** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/46` | 0.446100 | **SKILLS** **FEATS** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/83` | 0.446100 | **SKILLS** **FEATS** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/6/SectionHeader/15` | 0.437343 | **HARMONIC SENSITIVITY** **FEAT 1** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/13` | 0.423451 | **COMMUNALISM **[reaction] **FEAT 1** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/40` | 0.417375 | **Prerequisites** expert in Performance |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/25` | 0.414388 | **LINGUISTIC PRODIGY** **FEAT 1** |

### Query 127
- Text: What are the requirements for **HARMONIC SENSITIVITY** **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/6/SectionHeader/15']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/6/SectionHeader/15', 'PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/24', 'PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/22']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/6/SectionHeader/15` | 0.928362 | **HARMONIC SENSITIVITY** **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/24` | 0.801100 | **Prerequisites** Harmonic Sensitivity |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/22` | 0.582211 | **HARMONIC SHIELDING** **FEAT 9** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/13` | 0.476221 | **SENSITIVE ANTENNAE** **FEAT 5** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/9` | 0.450849 | **ALLURING PHEROMONES** **FEAT 1** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/18` | 0.438511 | **COMMANDING PHEROMONES** **FEAT 1** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/26` | 0.434573 | **MELODIC ADAPTATION** **FEAT 9** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/3` | 0.434355 | **PREDATORY** **FEAT 1** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/14/SectionHeader/26` | 0.432898 | **HYPER** **FEAT 1** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/6/Text/17` | 0.417943 | You've developed keen organs that have a sensitivity to sound and you know how to put them to use. You become trained in  Performance or gain the Assurance skill feat with Performance  if you're are a |

### Query 128
- Text: What are the requirements for **LONG WHISKERED** **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/6/SectionHeader/19']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/6/SectionHeader/19', 'PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/19', 'PZO22001 Starfinder Player Core 058-073::/page/14/SectionHeader/26']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/6/SectionHeader/19` | 0.885818 | **LONG WHISKERED** **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/19` | 0.799642 | **Prerequisites** Long Whiskered |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/14/SectionHeader/26` | 0.485370 | **HYPER** **FEAT 1** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/25` | 0.435049 | **LINGUISTIC PRODIGY** **FEAT 1** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/17` | 0.420662 | **ELECTROMAGNETIC WHISKERS** **FEAT 5** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/3` | 0.420345 | **PREDATORY** **FEAT 1** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/43` | 0.401020 | **LINGUISTIC MASTER** **FEAT 13** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/14/SectionHeader/22` | 0.390119 | **HUG MASTER FEAT 1** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/6/SectionHeader/15` | 0.384427 | **HARMONIC SENSITIVITY** **FEAT 1** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/13/Text/47` | 0.378593 | **FEATS** |

### Query 129
- Text: What are the requirements for **PAHTRA LORE** **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/6/Text/23']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/6/Text/23', 'PZO22001 Starfinder Player Core 058-073::/page/7/Text/2', 'PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/50']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/6/Text/23` | 0.888528 | **PAHTRA LORE** **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/2` | 0.638017 | You also gain the Additional Lore general feat for Pahtra Lore. |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/50` | 0.624269 | **PAHTRA** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/6/Text/24` | 0.594269 | **PAHTRA** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/44` | 0.582269 | **PAHTRA** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/54` | 0.582269 | **PAHTRA** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/23` | 0.582269 | **PAHTRA** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/15` | 0.582269 | **PAHTRA** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/12` | 0.582269 | **PAHTRA** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/4` | 0.582269 | **PAHTRA** |

### Query 130
- Text: What are the requirements for **PREDATORY** **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/7/Text/3']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/7/Text/3', 'PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/25', 'PZO22001 Starfinder Player Core 058-073::/page/14/SectionHeader/26']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/3` | 0.813258 | **PREDATORY** **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/25` | 0.554240 | **LINGUISTIC PRODIGY** **FEAT 1** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/14/SectionHeader/26` | 0.513547 | **HYPER** **FEAT 1** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/46` | 0.430045 | **FEATS** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/13/Text/47` | 0.430045 | **FEATS** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/75` | 0.430045 | **FEATS** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/46` | 0.430045 | **FEATS** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/85` | 0.430045 | **FEATS** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/81` | 0.430045 | **FEATS** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/14/SectionHeader/22` | 0.424106 | **HUG MASTER FEAT 1** |

### Query 131
- Text: What are the requirements for **BATTLEBLESSED** **FEAT 5**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/11', 'PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/16', 'PZO22001 Starfinder Player Core 058-073::/page/14/SectionHeader/35']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/11` | 0.878348 | **BATTLEBLESSED** **FEAT 5** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/16` | 0.551941 | **LEARNING EXPERIENCE** **FEAT 5** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/14/SectionHeader/35` | 0.489004 | **DOUBLE DRAW **[one-action] **FEAT 5** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/12` | 0.446901 | **EAGER ASSISTANT** **FEAT 5** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/18` | 0.424157 | **TELEPATHIC CONDUIT** **FEAT 5** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/20` | 0.424157 | **TELEPATHIC CONDUIT** **FEAT 5** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/5` | 0.420457 | **PSYCHIC BULLY** **FEAT 5** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/14/SectionHeader/15` | 0.415751 | **DAUNTLESS** **FEAT 1** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/15/SectionHeader/7` | 0.411208 | **LUCKY IMPROVISER** **FEAT 5** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/14` | 0.411036 | **CLIMBING CLAWS** **FEAT 5** |

### Query 132
- Text: What are the requirements for **CLIMBING CLAWS** **FEAT 5**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/14']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/14', 'PZO22001 Starfinder Player Core 058-073::/page/7/Text/16', 'PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/16']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/14` | 0.899998 | **CLIMBING CLAWS** **FEAT 5** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/16` | 0.536719 | You can extend your claws to aid you in climbing. You gain a  climb Speed equal to your land Speed. |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/16` | 0.522089 | **LEARNING EXPERIENCE** **FEAT 5** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/9` | 0.441928 | **PSYCHIC SCHOLAR** **FEAT 5** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/15/SectionHeader/7` | 0.440241 | **LUCKY IMPROVISER** **FEAT 5** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/12` | 0.435159 | **EAGER ASSISTANT** **FEAT 5** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/20` | 0.414434 | **TELEPATHIC CONDUIT** **FEAT 5** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/18` | 0.414434 | **TELEPATHIC CONDUIT** **FEAT 5** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/14/Text/3` | 0.406335 | You never mastered coordinating all six of your arms for manual  manipulation, instead using the lowest two limbs for the extra  mobility, balance, and stabilization of a natural climber. You  have fo |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/5` | 0.400857 | **PSYCHIC BULLY** **FEAT 5** |

### Query 133
- Text: What are the requirements for **ELECTROMAGNETIC WHISKERS** **FEAT 5**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/17']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/17', 'PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/18', 'PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/20']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/17` | 0.908294 | **ELECTROMAGNETIC WHISKERS** **FEAT 5** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/18` | 0.502759 | **TELEPATHIC CONDUIT** **FEAT 5** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/20` | 0.502759 | **TELEPATHIC CONDUIT** **FEAT 5** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/12` | 0.457357 | **EAGER ASSISTANT** **FEAT 5** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/16` | 0.430784 | **LEARNING EXPERIENCE** **FEAT 5** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/15/SectionHeader/7` | 0.408658 | **LUCKY IMPROVISER** **FEAT 5** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/19` | 0.394464 | **Prerequisites** Long Whiskered |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/9` | 0.384758 | **PSYCHIC SCHOLAR** **FEAT 5** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/5` | 0.374630 | **PSYCHIC BULLY** **FEAT 5** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/20` | 0.372038 | You've honed your whiskers' sensitivity to the degree that you  can sense the movement of the weak electric fields emitted  by potential enemies. You gain electromagnetic sense as an  imprecise sense |

### Query 134
- Text: What are the requirements for **Prerequisites** Long Whiskered?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/19']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/19', 'PZO22001 Starfinder Player Core 058-073::/page/6/SectionHeader/19', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/60']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/19` | 0.955022 | **Prerequisites** Long Whiskered |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/6/SectionHeader/19` | 0.642470 | **LONG WHISKERED** **FEAT 1** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/60` | 0.422645 | **Prerequisites** Psychic Mastery |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/35` | 0.377965 | **Prerequisites** Psychic Talent |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/31` | 0.377965 | **Prerequisites** Psychic Talent |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/34` | 0.368558 | **Prerequisites** Hyper |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/26` | 0.356371 | **Prerequisites** everwhelp skittermander heritage |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/14/Text/12` | 0.356371 | **Prerequisites** everwhelp skittermander heritage |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/23` | 0.348646 | **Prerequisites** limited telepathy |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/22` | 0.348646 | **Prerequisites** limited telepathy |

### Query 135
- Text: What are the requirements for **HARMONIC SHIELDING** **FEAT 9**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/22']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/22', 'PZO22001 Starfinder Player Core 058-073::/page/6/SectionHeader/15', 'PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/24']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/22` | 0.936915 | **HARMONIC SHIELDING** **FEAT 9** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/6/SectionHeader/15` | 0.582424 | **HARMONIC SENSITIVITY** **FEAT 1** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/24` | 0.571422 | **GUARDED THOUGHTS** **FEAT 9** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/24` | 0.512157 | **Prerequisites** Harmonic Sensitivity |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/26` | 0.486156 | **BASIC INSECTILE FLIGHT** **FEAT 9** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/26` | 0.472732 | **MELODIC ADAPTATION** **FEAT 9** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/28` | 0.470872 | **PSYCHIC MASTERY** **FEAT 9** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/32` | 0.470214 | **PSYCHIC MASTER** **FEAT 9** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/31` | 0.427202 | **MEYEL'S MELODY** **FEAT 9** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/15/SectionHeader/18` | 0.398204 | **HUSH **[one-action] **FEAT 9** |

### Query 136
- Text: What are the requirements for **Prerequisites** Harmonic Sensitivity?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/24']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/24', 'PZO22001 Starfinder Player Core 058-073::/page/6/SectionHeader/15', 'PZO22001 Starfinder Player Core 058-073::/page/15/Text/34']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/24` | 0.966003 | **Prerequisites** Harmonic Sensitivity |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/6/SectionHeader/15` | 0.696630 | **HARMONIC SENSITIVITY** **FEAT 1** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/34` | 0.460656 | **Prerequisites** Hyper |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/25` | 0.409440 | You've learned to compensate for your hypersensitivity to  sound. You gain sonic resistance equal to half your level. If you  roll a success on a saving throw against a sonic effect, you get  a critic |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/41` | 0.408298 | **Prerequisites** Communalism |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/40` | 0.401123 | **Prerequisites** expert in Performance |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/21` | 0.398080 | **Prerequisites** limited telepathy |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/22` | 0.398080 | **Prerequisites** limited telepathy |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/23` | 0.398080 | **Prerequisites** limited telepathy |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/25` | 0.398080 | **Prerequisites** limited telepathy |

### Query 137
- Text: What are the requirements for **MELODIC ADAPTATION** **FEAT 9**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/26']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/26', 'PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/31', 'PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/32']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/26` | 0.939208 | **MELODIC ADAPTATION** **FEAT 9** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/31` | 0.632942 | **MEYEL'S MELODY** **FEAT 9** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/32` | 0.561181 | **PSYCHIC MASTER** **FEAT 9** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/28` | 0.516807 | **PSYCHIC MASTERY** **FEAT 9** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/22` | 0.474254 | **HARMONIC SHIELDING** **FEAT 9** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/24` | 0.469338 | **GUARDED THOUGHTS** **FEAT 9** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/26` | 0.437084 | **BASIC INSECTILE FLIGHT** **FEAT 9** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/6/SectionHeader/15` | 0.415667 | **HARMONIC SENSITIVITY** **FEAT 1** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/15/SectionHeader/18` | 0.411394 | **HUSH **[one-action] **FEAT 9** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/24` | 0.409188 | **Prerequisites** Harmonic Sensitivity |

### Query 138
- Text: What are the requirements for **Prerequisites** trained in Arcana, Nature, Occultism, or Religion You can hear the thrum of magic as if it were a swirling note, a  shifting melody, a harmonic chord, or a percussive beat, pulsing  in tune with your heart. You can detect the presence of magic  as though you were always using a 1st-rank *detect magic* spell.  This detects magic within a 30-foot emanation.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/7/Text/29']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/7/Text/29', 'PZO22001 Starfinder Player Core 058-073::/page/2/Text/31', 'PZO22001 Starfinder Player Core 058-073::/page/7/Text/41']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/29` | 0.960142 | **Prerequisites** trained in Arcana, Nature, Occultism, or Religion You can hear the thrum of magic as if it were a swirling note, a  shifting melody, a harmonic chord, or a percussive beat, pulsing |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/31` | 0.569245 | You've studied the lives and achievements of other  lashuntas who have improved both their psychic powers  and their communities. You gain the trained proficiency  rank in Occultism and Society. If yo |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/41` | 0.560697 | Whether through intense musical training, magical insight, or  Meyel's divine blessing, you can feel the rhythm of the world  around you and tug on time's chords to manipulate its melody  and flow. Yo |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/30` | 0.520847 | At 13th level, the rank of *detect magic* increases to 3rd. At  17th level, the rank of *detect magic* increases to 4th. |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/53` | 0.501941 | **Prerequisites** expert in Occultism, focus pool |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/16` | 0.497119 | Your antennae are covered in fine hairs that make them  more sensitive to psychic vibrations than most. You gain  thoughtsense as a vague sense with a range of 30 feet. This  means you can use your an |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/20` | 0.495085 | You've honed your whiskers' sensitivity to the degree that you  can sense the movement of the weak electric fields emitted  by potential enemies. You gain electromagnetic sense as an  imprecise sense |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/3` | 0.487968 | Your psychic abilities have developed beyond simple  communication. Choose one cantrip from the occult spell list. You  can cast this cantrip as an occult innate spell at will. A cantrip is  heightene |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/10/Text/32` | 0.487968 | Your psychic abilities have developed beyond simple  communication. Choose one cantrip from the occult spell list. You  can cast this cantrip as an occult innate spell at will. A cantrip is  heightene |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/46` | 0.487235 | Your mastery of language reaches supernatural levels. You can  cast *truespeech* as a 5th-rank occult innate spell once per day on  yourself only. You gain a +1 status bonus to Diplomacy checks  for t |

### Query 139
- Text: What are the requirements for **MEYEL'S MELODY** **FEAT 9**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/31']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/31', 'PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/26', 'PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/34']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/31` | 0.897563 | **MEYEL'S MELODY** **FEAT 9** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/26` | 0.633367 | **MELODIC ADAPTATION** **FEAT 9** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/34` | 0.548767 | **Prerequisites** Meyel's chosen pahtra heritage |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/24` | 0.479338 | **GUARDED THOUGHTS** **FEAT 9** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/22` | 0.477680 | **HARMONIC SHIELDING** **FEAT 9** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/32` | 0.464791 | **PSYCHIC MASTER** **FEAT 9** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/26` | 0.461498 | **BASIC INSECTILE FLIGHT** **FEAT 9** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/28` | 0.457182 | **PSYCHIC MASTERY** **FEAT 9** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/15/SectionHeader/18` | 0.422671 | **HUSH **[one-action] **FEAT 9** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/5/SectionHeader/26` | 0.394025 | MEYEL'S CHOSEN PAHTRA |

### Query 140
- Text: What are the requirements for **Prerequisites** Meyel's chosen pahtra heritage?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/34']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/34', 'PZO22001 Starfinder Player Core 058-073::/page/5/SectionHeader/26', 'PZO22001 Starfinder Player Core 058-073::/page/6/Text/7']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/34` | 0.956905 | **Prerequisites** Meyel's chosen pahtra heritage |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/5/SectionHeader/26` | 0.681929 | MEYEL'S CHOSEN PAHTRA |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/6/Text/7` | 0.576872 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As a pahtra, you choose from among the  following an |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/23` | 0.518849 | Pahtras have a variety of heritages throughout their species.  Choose one of the following pahtra heritages at 1st level. |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/5/SectionHeader/22` | 0.509151 | PAHTRA HERITAGES |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/20` | 0.499273 | Many pahtras cling fiercely to their ancestral Pulonian  traditions in an effort to keep their cultures alive after  enduring generations of oppression by the Veskarium.  Pulonian culture values perso |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/6/Text/25` | 0.492414 | You're an expert in both the traditional and modern pahtra |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/35` | 0.453082 | **Pahtra** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/13/Text/36` | 0.453082 | **Pahtra** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/63` | 0.453082 | **Pahtra** |

### Query 141
- Text: What are the requirements for **REMIX WORLD'S RHYTHM** **FEAT 13**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/37']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/37', 'PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/43', 'PZO22001 Starfinder Player Core 058-073::/page/15/SectionHeader/48']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/37` | 0.891289 | **REMIX WORLD'S RHYTHM** **FEAT 13** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/43` | 0.528744 | **LINGUISTIC MASTER** **FEAT 13** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/15/SectionHeader/48` | 0.518925 | **SUPERSONIC SPEED** **FEAT 13** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/34` | 0.476701 | **FOCUS PHEROMONES **[one-action] **FEAT 13** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/15/SectionHeader/38` | 0.455656 | **CHATTERMANDER** **FEAT 13** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/39` | 0.423602 | **PSYCHIC INVESTIGATOR** **FEAT 13** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/15/SectionHeader/42` | 0.422096 | **OPPORTUNISTIC HUG **[reaction] **FEAT 13** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/47` | 0.401675 | **UNCONVENTIONAL EXPERTISE** **FEAT 13** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/38` | 0.397261 | **CONSISTENT COMMUNALISM** **FEAT 13** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/36` | 0.396764 | 13TH LEVEL |

### Query 142
- Text: What are the requirements for **Prerequisites** expert in Performance?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/40']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/40', 'PZO22001 Starfinder Player Core 058-073::/page/7/Text/1', 'PZO22001 Starfinder Player Core 058-073::/page/11/Text/35']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/40` | 0.960304 | **Prerequisites** expert in Performance |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/1` | 0.511324 | performing arts. You gain the trained proficiency rank in  Acrobatics and Performance. If you would automatically become  trained in one of those skills (from your background or class, for  example), |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/35` | 0.510369 | **Prerequisites** Psychic Talent |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/31` | 0.468369 | **Prerequisites** Psychic Talent |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/6/Text/17` | 0.436186 | You've developed keen organs that have a sensitivity to sound and you know how to put them to use. You become trained in  Performance or gain the Assurance skill feat with Performance  if you're are a |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/34` | 0.421025 | **Prerequisites** Hyper |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/25` | 0.406761 | **Prerequisites** limited telepathy |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/23` | 0.406761 | **Prerequisites** limited telepathy |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/22` | 0.406761 | **Prerequisites** limited telepathy |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/21` | 0.406761 | **Prerequisites** limited telepathy |

### Query 143
- Text: What are the requirements for **SCRUPULOUS STALKER **[free-action] **FEAT 13**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/42']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/42', 'PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/43', 'PZO22001 Starfinder Player Core 058-073::/page/15/SectionHeader/38']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/42` | 0.917333 | **SCRUPULOUS STALKER **[free-action] **FEAT 13** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/43` | 0.553230 | **LINGUISTIC MASTER** **FEAT 13** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/15/SectionHeader/38` | 0.548986 | **CHATTERMANDER** **FEAT 13** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/15/SectionHeader/48` | 0.505575 | **SUPERSONIC SPEED** **FEAT 13** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/34` | 0.481484 | **FOCUS PHEROMONES **[one-action] **FEAT 13** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/39` | 0.468669 | **PSYCHIC INVESTIGATOR** **FEAT 13** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/15/SectionHeader/42` | 0.442641 | **OPPORTUNISTIC HUG **[reaction] **FEAT 13** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/38` | 0.441808 | **CONSISTENT COMMUNALISM** **FEAT 13** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/15/SectionHeader/2` | 0.426601 | **HELPING HAND **[free-action] **FEAT 5** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/28` | 0.426455 | **Requirements** Your last action was a successful Strike with  your stomach-mouth jaws unarmed attack. |

### Query 144
- Text: What are the requirements for **BOUNDLESS BRACHIATOR** **FEAT 17**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/48']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/48', 'PZO22001 Starfinder Player Core 058-073::/page/15/SectionHeader/60', 'PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/53']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/48` | 0.905452 | **BOUNDLESS BRACHIATOR** **FEAT 17** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/15/SectionHeader/60` | 0.672035 | **BOUNDLESS ENERGY** **FEAT 17** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/53` | 0.481306 | **SCATTER THOUGHTS **[reaction] **FEAT 17** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/59` | 0.408478 | **SWARM EVOLUTION** **FEAT 17** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/15/SectionHeader/54` | 0.400397 | **ALLSIX **[one-action] **FEAT 17** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/14/SectionHeader/15` | 0.390559 | **DAUNTLESS** **FEAT 1** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/47` | 0.372385 | 17TH LEVEL |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/52` | 0.372385 | 17TH LEVEL |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/57` | 0.370167 | **PSYCHIC PARAGON** **FEAT 17** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/45` | 0.367067 | **CENTERED MIND** **FEAT 17** |

### Query 145
- Text: What are the requirements for **SONG OF MY PEOPLE** **FEAT 17**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/52']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/52', 'PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/53', 'PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/57']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/52` | 0.897595 | **SONG OF MY PEOPLE** **FEAT 17** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/53` | 0.505768 | **SCATTER THOUGHTS **[reaction] **FEAT 17** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/57` | 0.495431 | **PSYCHIC PARAGON** **FEAT 17** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/15/SectionHeader/60` | 0.453144 | **BOUNDLESS ENERGY** **FEAT 17** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/59` | 0.453041 | **SWARM EVOLUTION** **FEAT 17** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/50` | 0.445198 | **MENTAL DEFLECTION **[reaction] **FEAT 17** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/45` | 0.434386 | **CENTERED MIND** **FEAT 17** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/15/SectionHeader/54` | 0.427070 | **ALLSIX **[one-action] **FEAT 17** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/48` | 0.409973 | **BOUNDLESS BRACHIATOR** **FEAT 17** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/52` | 0.407913 | 17TH LEVEL |

### Query 146
- Text: What are the requirements for **COMMUNALISM **[reaction] **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/13', 'PZO22001 Starfinder Player Core 058-073::/page/11/Text/41', 'PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/38']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/13` | 0.870747 | **COMMUNALISM **[reaction] **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/41` | 0.762265 | **Prerequisites** Communalism |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/38` | 0.643536 | **CONSISTENT COMMUNALISM** **FEAT 13** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/6/SectionHeader/9` | 0.471020 | **COMPETITIVE SPIRIT **[reaction] **FEAT 1** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/15/SectionHeader/42` | 0.439285 | **OPPORTUNISTIC HUG **[reaction] **FEAT 13** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/13` | 0.418865 | **CENTER THOUGHTS **[free-action] **FEAT 1** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/42` | 0.415338 | You're always ready to help your allies when they need you the  most. You can use Communalism once per hour, rather than  once per day. |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/25` | 0.413368 | **LINGUISTIC PRODIGY** **FEAT 1** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/53` | 0.400099 | **SCATTER THOUGHTS **[reaction] **FEAT 17** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/50` | 0.388146 | **MENTAL DEFLECTION **[reaction] **FEAT 17** |

### Query 147
- Text: What are the requirements for **DISTANT TELEPATH** **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/19']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/22', 'PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/19', 'PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/22']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/22` | 0.870231 | **DISTANT TELEPATH** **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/19` | 0.870231 | **DISTANT TELEPATH** **FEAT 1** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/22` | 0.655712 | **Prerequisites** limited telepathy |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/23` | 0.613712 | **Prerequisites** limited telepathy |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/21` | 0.613712 | **Prerequisites** limited telepathy |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/25` | 0.613712 | **Prerequisites** limited telepathy |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/8/SectionHeader/14` | 0.582904 | LIMITED TELEPATHY |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/0/SectionHeader/12` | 0.582904 | LIMITED TELEPATHY |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/18` | 0.545931 | **TELEPATHIC CONDUIT** **FEAT 5** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/20` | 0.545931 | **TELEPATHIC CONDUIT** **FEAT 5** |

### Query 148
- Text: What are the requirements for **Prerequisites** limited telepathy?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/22']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/3/Text/21', 'PZO22001 Starfinder Player Core 058-073::/page/11/Text/23', 'PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/22']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/21` | 0.945401 | **Prerequisites** limited telepathy |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/23` | 0.945401 | **Prerequisites** limited telepathy |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/22` | 0.945401 | **Prerequisites** limited telepathy |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/25` | 0.903401 | **Prerequisites** limited telepathy |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/0/SectionHeader/12` | 0.618754 | LIMITED TELEPATHY |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/8/SectionHeader/14` | 0.618754 | LIMITED TELEPATHY |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/10/Text/23` | 0.569906 | Whether through training or innate talent,  you've expanded the range at which you can  telepathically communicate. Increase the range of  your limited telepathy by 15 feet. |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/26` | 0.557906 | Whether through training or innate talent, you've expanded  the range at which you can telepathically communicate.  Increase the range of your limited telepathy by 15 feet. |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/25` | 0.552556 | Your telepathy is stronger than most shirrens', allowing you to  combine physical, verbal, and telepathic communication. You  can transmit emotions alongside your messages whenever  you use limited te |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/22` | 0.539129 | When you use limited telepathy to communicate with another  creature, you act as a conduit for their thoughts, allowing them  to respond to you for a few scant moments—if they wish. The  creature can |

### Query 149
- Text: What are the requirements for **LINGUISTIC PRODIGY** **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/25']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/25', 'PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/43', 'PZO22001 Starfinder Player Core 058-073::/page/7/Text/3']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/25` | 0.907704 | **LINGUISTIC PRODIGY** **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/43` | 0.623070 | **LINGUISTIC MASTER** **FEAT 13** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/3` | 0.531952 | **PREDATORY** **FEAT 1** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/16` | 0.415736 | **LEARNING EXPERIENCE** **FEAT 5** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/83` | 0.413934 | **SKILLS** **FEATS** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/46` | 0.413934 | **SKILLS** **FEATS** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/14/SectionHeader/26` | 0.408198 | **HYPER** **FEAT 1** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/6/SectionHeader/19` | 0.407084 | **LONG WHISKERED** **FEAT 1** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/78` | 0.397100 | **Languages** **CLASSES** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/44` | 0.397100 | **Languages** **CLASSES** |
