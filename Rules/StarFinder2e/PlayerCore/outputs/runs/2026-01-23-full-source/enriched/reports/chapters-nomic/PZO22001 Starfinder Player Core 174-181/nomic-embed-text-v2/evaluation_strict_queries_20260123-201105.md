# RulesLawyer Evaluation Report: nomic-embed-text-v2

## Summary
- Run ID: `None`
- Ruleset ID: `None`
- Document ID: `None`
- Chunk source: `enriched`
- Chunk count: `367`
- Query count: `150`
- Evaluated queries: `150`
- Coverage: `1.0000`
- MRR: `0.8134`
- hit@1: `0.7467`
- hit@3: `0.8667`
- hit@5: `0.9000`
- hit@10: `0.9200`
- Embeddings reused: `False`
- Graph boost: `0.05` (depth=2, top_k=50, source=top, seed_top_n=3, same_kind_only=False, decay=0.4)

## Timings (ms)
- Embedding (chunks): `5558`
- Embedding (queries): `3317`
- Evaluation (strict): `22`
- Evaluation (expanded): `0`
- Total: `13350`

### Timing Estimates (ms)
- Evaluation (strict): `15`
- Evaluation (expanded): `None`
- Total: `8890`

## Query Details
### Query 0
- Text: Summarize ARCHETYPES
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/0/SectionHeader/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/0/SectionHeader/1', 'PZO22001 Starfinder Player Core 174-181::/page/0/SectionHeader/20', 'PZO22001 Starfinder Player Core 174-181::/page/6/SectionHeader/43']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/0/SectionHeader/1` | 0.981117 | ARCHETYPES |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/0/SectionHeader/20` | 0.885125 | SPECIAL ARCHETYPES |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/6/SectionHeader/43` | 0.805388 | **ARCHETYPE** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/6/SectionHeader/48` | 0.763388 | **ARCHETYPE** |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/18` | 0.763388 | **ARCHETYPE** |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/33` | 0.763388 | **ARCHETYPE** |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/27` | 0.763388 | **ARCHETYPE** |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/21` | 0.763388 | **ARCHETYPE** |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/12` | 0.763388 | **ARCHETYPE** |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/16` | 0.763388 | **ARCHETYPE** |

### Query 1
- Text: What is the rule about Archetypes allow you to further customize your character concepts by taking more than one class.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/0/Text/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/0/Text/2', 'PZO22001 Starfinder Player Core 174-181::/page/0/Text/21', 'PZO22001 Starfinder Player Core 174-181::/page/0/Text/9']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/2` | 0.924873 | Archetypes allow you to further customize your character concepts by taking more than one class. |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/21` | 0.727470 | Some archetype feats in other books have the skill trait,  allowing you to take them in place of a skill feat rather than  a class feat. A skill feat still counts to satisfy the requirement  of the de |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/9` | 0.681262 | Most archetypes in this book have the multiclass trait.  These allow you to diversify your training into another  class's specialties. You can't select a multiclass archetype's  dedication feat if you |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/5` | 0.615068 | An archetype feat is subject to any restrictions on the class  feat it replaces. For example, if you had an ability at 6th level  that granted you a bonus class feat, but that class feat had to  be 4t |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/4` | 0.581549 | You gain an archetype by selecting archetype feats instead  of your normal feats. First, find the archetype that best  fits your character concept. Then select that archetype's  dedication feat, using |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/13` | 0.575468 | Sometimes an archetype feat lets you select another feat,  such as a class feat of a lower level. You must always meet  any prerequisites of the feat you gain in this way. These  always count as only |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/16` | 0.554365 | class feat you have. As you continue selecting operative  archetype class feats, you continue to gain additional Hit Points  in this way. |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/38` | 0.553728 | **Archetypes** |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/52` | 0.553728 | **Archetypes** |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/56` | 0.553728 | **Archetypes** |

### Query 2
- Text: What is the rule about You gain an archetype by selecting archetype feats instead  of your normal feats. First, find the archetype that best  fits your character concept. Then select that archetype's  dedication feat, using one of your class feat choices. Once  you've taken the dedication feat, you can select any feat from  that archetype, as long as you meet its prerequisites. Most  archetype feats are taken in place of class feats, and so these  are called archetype class feats.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/0/Text/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/0/Text/4', 'PZO22001 Starfinder Player Core 174-181::/page/0/Text/21', 'PZO22001 Starfinder Player Core 174-181::/page/0/Text/11']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/4` | 0.966026 | You gain an archetype by selecting archetype feats instead  of your normal feats. First, find the archetype that best  fits your character concept. Then select that archetype's  dedication feat, using |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/21` | 0.839730 | Some archetype feats in other books have the skill trait,  allowing you to take them in place of a skill feat rather than  a class feat. A skill feat still counts to satisfy the requirement  of the de |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/11` | 0.829674 | Some archetypes include a list of "Additional Feats" that  appear in other sources. The list includes each feat's level,  which might be different than normal when gained from the  archetype. You can |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/7` | 0.778084 | Each archetype's dedication feat represents your character's  dedicated effort learning a new set of abilities, making it  impossible to split your focus and pursue another archetype  at the same time |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/13` | 0.768975 | Sometimes an archetype feat lets you select another feat,  such as a class feat of a lower level. You must always meet  any prerequisites of the feat you gain in this way. These  always count as only |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/9` | 0.763131 | Most archetypes in this book have the multiclass trait.  These allow you to diversify your training into another  class's specialties. You can't select a multiclass archetype's  dedication feat if you |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/5` | 0.716784 | An archetype feat is subject to any restrictions on the class  feat it replaces. For example, if you had an ability at 6th level  that granted you a bonus class feat, but that class feat had to  be 4t |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/16` | 0.678803 | class feat you have. As you continue selecting operative  archetype class feats, you continue to gain additional Hit Points  in this way. |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/16` | 0.629963 | Spellcasting archetypes always grant the ability to cast  cantrips in their dedication, and then they have a basic  spellcasting feat, an expert spellcasting feat, and a master  spellcasting feat. The |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/2` | 0.624107 | Archetypes allow you to further customize your character concepts by taking more than one class. |

### Query 3
- Text: What is the rule about An archetype feat is subject to any restrictions on the class  feat it replaces. For example, if you had an ability at 6th level  that granted you a bonus class feat, but that class feat had to  be 4th level or lower and have the vesk trait, you could use  that class feat to take an archetype class feat, but only one of  4th level or lower with the vesk trait.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/0/Text/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/0/Text/5', 'PZO22001 Starfinder Player Core 174-181::/page/0/Text/21', 'PZO22001 Starfinder Player Core 174-181::/page/0/Text/13']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/5` | 1.014146 | An archetype feat is subject to any restrictions on the class  feat it replaces. For example, if you had an ability at 6th level  that granted you a bonus class feat, but that class feat had to  be 4t |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/21` | 0.768684 | Some archetype feats in other books have the skill trait,  allowing you to take them in place of a skill feat rather than  a class feat. A skill feat still counts to satisfy the requirement  of the de |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/13` | 0.729983 | Sometimes an archetype feat lets you select another feat,  such as a class feat of a lower level. You must always meet  any prerequisites of the feat you gain in this way. These  always count as only |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/11` | 0.687498 | Some archetypes include a list of "Additional Feats" that  appear in other sources. The list includes each feat's level,  which might be different than normal when gained from the  archetype. You can |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/9` | 0.620860 | Most archetypes in this book have the multiclass trait.  These allow you to diversify your training into another  class's specialties. You can't select a multiclass archetype's  dedication feat if you |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/4` | 0.616858 | You gain an archetype by selecting archetype feats instead  of your normal feats. First, find the archetype that best  fits your character concept. Then select that archetype's  dedication feat, using |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/7` | 0.610910 | Each archetype's dedication feat represents your character's  dedicated effort learning a new set of abilities, making it  impossible to split your focus and pursue another archetype  at the same time |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/40` | 0.545542 | You gain the adaptive talent class feature, but you do not  gain additional skill feats at higher levels. |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/16` | 0.536117 | class feat you have. As you continue selecting operative  archetype class feats, you continue to gain additional Hit Points  in this way. |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/14` | 0.533099 | You become trained in light armor and medium armor. If  you already were trained in light armor and medium armor,  you gain training in heavy armor as well. Whenever you gain  a class feature that gra |

### Query 4
- Text: Summarize DEDICATION DETAILS
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/0/SectionHeader/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/0/SectionHeader/6', 'PZO22001 Starfinder Player Core 174-181::/page/0/SectionHeader/8', 'PZO22001 Starfinder Player Core 174-181::/page/3/Text/10']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/0/SectionHeader/6` | 0.971304 | DEDICATION DETAILS |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/0/SectionHeader/8` | 0.668441 | Multiclass Dedications |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/10` | 0.597485 | **OPERATIVE DEDICATION** **FEAT 2** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/60` | 0.553964 | **Prerequisites** Operative Dedication |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/55` | 0.553964 | **Prerequisites** Operative Dedication |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/50` | 0.553964 | **Prerequisites** Operative Dedication |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/27` | 0.520652 | **ENVOY DEDICATION** **FEAT 2** |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/5/SectionHeader/10` | 0.515752 | **SOLDIER DEDICATION** **FEAT 2** |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/5` | 0.512037 | **MYSTIC DEDICATION** **FEAT 2** |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/12` | 0.509892 | **ARCHETYPE** **DEDICATION** **MULTICLASS** |

### Query 5
- Text: What is the rule about Each archetype's dedication feat represents your character's  dedicated effort learning a new set of abilities, making it  impossible to split your focus and pursue another archetype  at the same time. Once you take a dedication feat, you can't  select a different dedication feat until you complete your  dedication by taking two other feats from your current  archetype. You can't retrain a dedication feat as long as you  have any other feats from that archetype.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/0/Text/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/0/Text/7', 'PZO22001 Starfinder Player Core 174-181::/page/0/Text/9', 'PZO22001 Starfinder Player Core 174-181::/page/0/Text/21']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/7` | 1.008807 | Each archetype's dedication feat represents your character's  dedicated effort learning a new set of abilities, making it  impossible to split your focus and pursue another archetype  at the same time |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/9` | 0.786764 | Most archetypes in this book have the multiclass trait.  These allow you to diversify your training into another  class's specialties. You can't select a multiclass archetype's  dedication feat if you |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/21` | 0.784326 | Some archetype feats in other books have the skill trait,  allowing you to take them in place of a skill feat rather than  a class feat. A skill feat still counts to satisfy the requirement  of the de |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/11` | 0.738299 | Some archetypes include a list of "Additional Feats" that  appear in other sources. The list includes each feat's level,  which might be different than normal when gained from the  archetype. You can |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/4` | 0.728632 | You gain an archetype by selecting archetype feats instead  of your normal feats. First, find the archetype that best  fits your character concept. Then select that archetype's  dedication feat, using |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/13` | 0.706324 | Sometimes an archetype feat lets you select another feat,  such as a class feat of a lower level. You must always meet  any prerequisites of the feat you gain in this way. These  always count as only |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/5` | 0.645005 | An archetype feat is subject to any restrictions on the class  feat it replaces. For example, if you had an ability at 6th level  that granted you a bonus class feat, but that class feat had to  be 4t |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/61` | 0.594212 | Choose a specialization. You become trained in one skill  determined by your specialization; if you were already trained  in that skill, you instead become trained in another skill of your  choice. Yo |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/16` | 0.587083 | Spellcasting archetypes always grant the ability to cast  cantrips in their dedication, and then they have a basic  spellcasting feat, an expert spellcasting feat, and a master  spellcasting feat. The |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/7/Text/8` | 0.570298 | **Special** You can take this feat if you have the xenoarchaeologist  archetype dedication feat (*Starfinder* *Galaxy Guide*) even if  you haven't taken two additional xenoarchaeologist feats.  Xenoar |

### Query 6
- Text: Summarize Multiclass Dedications
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/0/SectionHeader/8']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/0/SectionHeader/8', 'PZO22001 Starfinder Player Core 174-181::/page/7/Text/5', 'PZO22001 Starfinder Player Core 174-181::/page/6/SectionHeader/7']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/0/SectionHeader/8` | 0.970375 | Multiclass Dedications |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/7/Text/5` | 0.665470 | **ARCHETYPE** **DEDICATION** **MULTICLASS** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/6/SectionHeader/7` | 0.665470 | **ARCHETYPE** **DEDICATION** **MULTICLASS** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/7` | 0.623470 | **ARCHETYPE** **DEDICATION** **MULTICLASS** |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/28` | 0.623470 | **ARCHETYPE** **DEDICATION** **MULTICLASS** |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/5/SectionHeader/11` | 0.623470 | **ARCHETYPE** **DEDICATION** **MULTICLASS** |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/12` | 0.623470 | **ARCHETYPE** **DEDICATION** **MULTICLASS** |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/12` | 0.623470 | **ARCHETYPE** **DEDICATION** **MULTICLASS** |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/0/SectionHeader/6` | 0.605688 | DEDICATION DETAILS |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/9` | 0.595931 | Most archetypes in this book have the multiclass trait.  These allow you to diversify your training into another  class's specialties. You can't select a multiclass archetype's  dedication feat if you |

### Query 7
- Text: What is the rule about Most archetypes in this book have the multiclass trait.  These allow you to diversify your training into another  class's specialties. You can't select a multiclass archetype's  dedication feat if you are already a member of that class.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/0/Text/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/0/Text/9', 'PZO22001 Starfinder Player Core 174-181::/page/0/Text/21', 'PZO22001 Starfinder Player Core 174-181::/page/0/Text/7']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/9` | 1.005930 | Most archetypes in this book have the multiclass trait.  These allow you to diversify your training into another  class's specialties. You can't select a multiclass archetype's  dedication feat if you |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/21` | 0.831857 | Some archetype feats in other books have the skill trait,  allowing you to take them in place of a skill feat rather than  a class feat. A skill feat still counts to satisfy the requirement  of the de |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/7` | 0.794706 | Each archetype's dedication feat represents your character's  dedicated effort learning a new set of abilities, making it  impossible to split your focus and pursue another archetype  at the same time |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/11` | 0.716660 | Some archetypes include a list of "Additional Feats" that  appear in other sources. The list includes each feat's level,  which might be different than normal when gained from the  archetype. You can |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/4` | 0.702082 | You gain an archetype by selecting archetype feats instead  of your normal feats. First, find the archetype that best  fits your character concept. Then select that archetype's  dedication feat, using |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/13` | 0.687789 | Sometimes an archetype feat lets you select another feat,  such as a class feat of a lower level. You must always meet  any prerequisites of the feat you gain in this way. These  always count as only |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/5` | 0.650581 | An archetype feat is subject to any restrictions on the class  feat it replaces. For example, if you had an ability at 6th level  that granted you a bonus class feat, but that class feat had to  be 4t |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/61` | 0.606743 | Choose a specialization. You become trained in one skill  determined by your specialization; if you were already trained  in that skill, you instead become trained in another skill of your  choice. Yo |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/2` | 0.579313 | Archetypes allow you to further customize your character concepts by taking more than one class. |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/16` | 0.573061 | Spellcasting archetypes always grant the ability to cast  cantrips in their dedication, and then they have a basic  spellcasting feat, an expert spellcasting feat, and a master  spellcasting feat. The |

### Query 8
- Text: What is the rule about ADDITIONAL FEATS?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/0/SectionHeader/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/0/SectionHeader/10', 'PZO22001 Starfinder Player Core 174-181::/page/0/Text/11', 'PZO22001 Starfinder Player Core 174-181::/page/0/SectionHeader/12']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/0/SectionHeader/10` | 0.893052 | ADDITIONAL FEATS |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/11` | 0.618316 | Some archetypes include a list of "Additional Feats" that  appear in other sources. The list includes each feat's level,  which might be different than normal when gained from the  archetype. You can |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/0/SectionHeader/12` | 0.574829 | FEATS THAT GRANT FEATS |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/13` | 0.515672 | Sometimes an archetype feat lets you select another feat,  such as a class feat of a lower level. You must always meet  any prerequisites of the feat you gain in this way. These  always count as only |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/23` | 0.474194 | **Special** You can select this feat more than once. Each time you  do, you gain another operative feat. |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/54` | 0.469319 | **FEATS** |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/40` | 0.469319 | **FEATS** |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/59` | 0.469319 | **FEATS** |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/7/Text/48` | 0.469319 | **FEATS** |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/41` | 0.462240 | **Special** You can select this feat a second time as a 10th level  feat and a 16th level feat, increasing the number of skill  feats you gain using adaptive talent by 1. |

### Query 9
- Text: What is the rule about Some archetypes include a list of "Additional Feats" that  appear in other sources. The list includes each feat's level,  which might be different than normal when gained from the  archetype. You can take the feat as an archetype feat of that  level, meaning it counts toward the number of feats required  by the archetype's dedication feat. When selected this way, a  feat that normally has a class's trait (such as the soldier trait)  doesn't have that class trait.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/0/Text/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/0/Text/11', 'PZO22001 Starfinder Player Core 174-181::/page/0/Text/21', 'PZO22001 Starfinder Player Core 174-181::/page/0/Text/13']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/11` | 1.005521 | Some archetypes include a list of "Additional Feats" that  appear in other sources. The list includes each feat's level,  which might be different than normal when gained from the  archetype. You can |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/21` | 0.833748 | Some archetype feats in other books have the skill trait,  allowing you to take them in place of a skill feat rather than  a class feat. A skill feat still counts to satisfy the requirement  of the de |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/13` | 0.805501 | Sometimes an archetype feat lets you select another feat,  such as a class feat of a lower level. You must always meet  any prerequisites of the feat you gain in this way. These  always count as only |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/5` | 0.729539 | An archetype feat is subject to any restrictions on the class  feat it replaces. For example, if you had an ability at 6th level  that granted you a bonus class feat, but that class feat had to  be 4t |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/4` | 0.716321 | You gain an archetype by selecting archetype feats instead  of your normal feats. First, find the archetype that best  fits your character concept. Then select that archetype's  dedication feat, using |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/7` | 0.714857 | Each archetype's dedication feat represents your character's  dedicated effort learning a new set of abilities, making it  impossible to split your focus and pursue another archetype  at the same time |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/9` | 0.714077 | Most archetypes in this book have the multiclass trait.  These allow you to diversify your training into another  class's specialties. You can't select a multiclass archetype's  dedication feat if you |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/16` | 0.617122 | class feat you have. As you continue selecting operative  archetype class feats, you continue to gain additional Hit Points  in this way. |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/24` | 0.615283 | You gain 3 additional Hit Points for each soldier archetype  class feat you have. As you continue selecting soldier  archetype class feats, you continue to gain additional Hit  Points in this way. |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/29` | 0.582521 | You gain one soldier feat. For the purpose of meeting its  prerequisites, your soldier level is half your character level. |

### Query 10
- Text: What is the rule about FEATS THAT GRANT FEATS?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/0/SectionHeader/12']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/0/SectionHeader/12', 'PZO22001 Starfinder Player Core 174-181::/page/0/SectionHeader/10', 'PZO22001 Starfinder Player Core 174-181::/page/7/Text/48']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/0/SectionHeader/12` | 0.883291 | FEATS THAT GRANT FEATS |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/0/SectionHeader/10` | 0.576942 | ADDITIONAL FEATS |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/7/Text/48` | 0.570233 | **FEATS** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/54` | 0.528233 | **FEATS** |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/59` | 0.528233 | **FEATS** |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/40` | 0.528233 | **FEATS** |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/13` | 0.467490 | Sometimes an archetype feat lets you select another feat,  such as a class feat of a lower level. You must always meet  any prerequisites of the feat you gain in this way. These  always count as only |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/11` | 0.452155 | Some archetypes include a list of "Additional Feats" that  appear in other sources. The list includes each feat's level,  which might be different than normal when gained from the  archetype. You can |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/23` | 0.417174 | **Special** You can select this feat more than once. Each time you  do, you gain another operative feat. |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/15` | 0.408811 | **Special** You can select this feat more than once. Each time  you select it, you gain another envoy feat. |

### Query 11
- Text: What is the rule about Sometimes an archetype feat lets you select another feat,  such as a class feat of a lower level. You must always meet  any prerequisites of the feat you gain in this way. These  always count as only one feat for the purposes of your  dedication; for example, taking the envoy archetype's Basic  Leadership feat to gain the Don't You Die On Me! class feat  counts as only one feat, not two.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/0/Text/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/0/Text/13', 'PZO22001 Starfinder Player Core 174-181::/page/0/Text/11', 'PZO22001 Starfinder Player Core 174-181::/page/0/Text/21']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/13` | 1.015922 | Sometimes an archetype feat lets you select another feat,  such as a class feat of a lower level. You must always meet  any prerequisites of the feat you gain in this way. These  always count as only |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/11` | 0.791331 | Some archetypes include a list of "Additional Feats" that  appear in other sources. The list includes each feat's level,  which might be different than normal when gained from the  archetype. You can |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/21` | 0.775874 | Some archetype feats in other books have the skill trait,  allowing you to take them in place of a skill feat rather than  a class feat. A skill feat still counts to satisfy the requirement  of the de |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/5` | 0.704991 | An archetype feat is subject to any restrictions on the class  feat it replaces. For example, if you had an ability at 6th level  that granted you a bonus class feat, but that class feat had to  be 4t |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/7` | 0.688198 | Each archetype's dedication feat represents your character's  dedicated effort learning a new set of abilities, making it  impossible to split your focus and pursue another archetype  at the same time |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/4` | 0.681647 | You gain an archetype by selecting archetype feats instead  of your normal feats. First, find the archetype that best  fits your character concept. Then select that archetype's  dedication feat, using |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/9` | 0.660416 | Most archetypes in this book have the multiclass trait.  These allow you to diversify your training into another  class's specialties. You can't select a multiclass archetype's  dedication feat if you |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/15` | 0.599978 | **Special** You can select this feat more than once. Each time  you select it, you gain another envoy feat. |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/14` | 0.590710 | You gain one envoy feat. For the purpose of meeting its  prerequisites, your envoy level is equal to half your character  level. |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/16` | 0.588397 | class feat you have. As you continue selecting operative  archetype class feats, you continue to gain additional Hit Points  in this way. |

### Query 12
- Text: What is the rule about SPELLCASTING ARCHETYPES?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/0/SectionHeader/14']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/0/SectionHeader/14', 'PZO22001 Starfinder Player Core 174-181::/page/0/SectionHeader/1', 'PZO22001 Starfinder Player Core 174-181::/page/0/SectionHeader/20']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/0/SectionHeader/14` | 0.903040 | SPELLCASTING ARCHETYPES |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/0/SectionHeader/1` | 0.575172 | ARCHETYPES |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/0/SectionHeader/20` | 0.558283 | SPECIAL ARCHETYPES |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/17` | 0.494179 | **BASIC MYSTIC SPELLCASTING** **FEAT 4** |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/43` | 0.490951 | **EXPERT MYSTIC SPELLCASTING** **FEAT 12** |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/15` | 0.472939 | Some archetypes grant you a substantial degree of  spellcasting, albeit delayed compared to a character from a  spellcasting class. The spellcasting ability from a spellcasting  archetype also allows |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/6/SectionHeader/41` | 0.443933 | **EXPERT WITCHWARPER SPELLCASTING** **FEAT 12** |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/16` | 0.443452 | Spellcasting archetypes always grant the ability to cast  cantrips in their dedication, and then they have a basic  spellcasting feat, an expert spellcasting feat, and a master  spellcasting feat. The |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/21` | 0.442093 | **ARCHETYPE** |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/27` | 0.442093 | **ARCHETYPE** |

### Query 13
- Text: What is the rule about Some archetypes grant you a substantial degree of  spellcasting, albeit delayed compared to a character from a  spellcasting class. The spellcasting ability from a spellcasting  archetype also allows you to use Cast a Spell activations of  items (such as spell chips and spell gems).?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/0/Text/15']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/0/Text/15', 'PZO22001 Starfinder Player Core 174-181::/page/0/Text/16', 'PZO22001 Starfinder Player Core 174-181::/page/0/Text/19']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/15` | 1.000169 | Some archetypes grant you a substantial degree of  spellcasting, albeit delayed compared to a character from a  spellcasting class. The spellcasting ability from a spellcasting  archetype also allows |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/16` | 0.726072 | Spellcasting archetypes always grant the ability to cast  cantrips in their dedication, and then they have a basic  spellcasting feat, an expert spellcasting feat, and a master  spellcasting feat. The |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/19` | 0.677970 | **Master Spellcasting Feat:** Usually found at 18th level, these  feats make you a master in spell attack modifiers and spell  DCs and grant you a 7th-rank spell slot. If you have a spell  repertoire, |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/18` | 0.639205 | **Expert Spellcasting Feat:** Typically taken at 12th level,  these feats make you an expert in spell attack modifiers  and spell DCs and grant you a 4th-rank spell slot. If you  have a spell repertoi |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/17` | 0.625939 | **Basic Spellcasting Feat:** Usually available at 4th level,  these feats grant a 1st-rank spell slot. At 6th level, they  grant you a 2nd-rank spell slot, and if you have a spell  repertoire, you can |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/21` | 0.609693 | Some archetype feats in other books have the skill trait,  allowing you to take them in place of a skill feat rather than  a class feat. A skill feat still counts to satisfy the requirement  of the de |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/10` | 0.607093 | You cast spells like a mystic and gain the Cast a Spell  activity. You gain a spell repertoire with two common cantrips  from the spell list granted by your connection, from the spells  granted by you |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/21` | 0.591458 | You gain the basic spellcasting benefits (page 174). Each time  you gain a spell slot of a new rank from the mystic archetype,  add a spell of the appropriate spell rank to your repertoire: a  common |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/10` | 0.591170 | You cast spells like a witchwarper. You gain access to the Cast  a Spell activity. You gain a spell repertoire with two common  cantrips from the spell list associated with your paradox, from  the spe |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/29` | 0.575739 | You gain the basic spellcasting benefits (page 174). Each time  you gain a spell slot of a new rank from the witchwarper  archetype, add a spell of the appropriate spell rank to your  repertoire: a co |

### Query 14
- Text: What is the rule about Spellcasting archetypes always grant the ability to cast  cantrips in their dedication, and then they have a basic  spellcasting feat, an expert spellcasting feat, and a master  spellcasting feat. These feats share their name with the  archetype; for instance, the witchwarper's master spellcasting  feat is called Master Witchwarper Spellcasting. All spell slots  you gain from spellcasting archetypes are subject to the  restrictions within the archetype. For instance, the mystic  archetype allows you to pick a connection when you take  its dedication feat. If you pick a connection granting divine  spells, the archetype then grants you spell slots you can use  only to cast divine spells you prepare as a mystic, even if you  are a witchwarper with occult spells in your repertoire.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/0/Text/16']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/0/Text/16', 'PZO22001 Starfinder Player Core 174-181::/page/2/Text/10', 'PZO22001 Starfinder Player Core 174-181::/page/0/Text/19']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/16` | 1.003827 | Spellcasting archetypes always grant the ability to cast  cantrips in their dedication, and then they have a basic  spellcasting feat, an expert spellcasting feat, and a master  spellcasting feat. The |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/10` | 0.742852 | You cast spells like a mystic and gain the Cast a Spell  activity. You gain a spell repertoire with two common cantrips  from the spell list granted by your connection, from the spells  granted by you |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/19` | 0.711305 | **Master Spellcasting Feat:** Usually found at 18th level, these  feats make you a master in spell attack modifiers and spell  DCs and grant you a 7th-rank spell slot. If you have a spell  repertoire, |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/18` | 0.677830 | **Expert Spellcasting Feat:** Typically taken at 12th level,  these feats make you an expert in spell attack modifiers  and spell DCs and grant you a 4th-rank spell slot. If you  have a spell repertoi |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/15` | 0.676972 | Some archetypes grant you a substantial degree of  spellcasting, albeit delayed compared to a character from a  spellcasting class. The spellcasting ability from a spellcasting  archetype also allows |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/10` | 0.669220 | You cast spells like a witchwarper. You gain access to the Cast  a Spell activity. You gain a spell repertoire with two common  cantrips from the spell list associated with your paradox, from  the spe |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/21` | 0.661833 | You gain the basic spellcasting benefits (page 174). Each time  you gain a spell slot of a new rank from the mystic archetype,  add a spell of the appropriate spell rank to your repertoire: a  common |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/29` | 0.658966 | You gain the basic spellcasting benefits (page 174). Each time  you gain a spell slot of a new rank from the witchwarper  archetype, add a spell of the appropriate spell rank to your  repertoire: a co |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/21` | 0.641371 | Some archetype feats in other books have the skill trait,  allowing you to take them in place of a skill feat rather than  a class feat. A skill feat still counts to satisfy the requirement  of the de |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/17` | 0.640071 | **Basic Spellcasting Feat:** Usually available at 4th level,  these feats grant a 1st-rank spell slot. At 6th level, they  grant you a 2nd-rank spell slot, and if you have a spell  repertoire, you can |

### Query 15
- Text: What is the rule about **Basic Spellcasting Feat:** Usually available at 4th level,  these feats grant a 1st-rank spell slot. At 6th level, they  grant you a 2nd-rank spell slot, and if you have a spell  repertoire, you can select one spell from your repertoire as  a signature spell. At 8th level, they grant you a 3rd-rank  spell slot. Archetypes refer to these benefits as the "basic  spellcasting benefits."?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/0/Text/17']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/0/Text/17', 'PZO22001 Starfinder Player Core 174-181::/page/0/Text/19', 'PZO22001 Starfinder Player Core 174-181::/page/0/Text/18']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/17` | 0.994652 | **Basic Spellcasting Feat:** Usually available at 4th level,  these feats grant a 1st-rank spell slot. At 6th level, they  grant you a 2nd-rank spell slot, and if you have a spell  repertoire, you can |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/19` | 0.794252 | **Master Spellcasting Feat:** Usually found at 18th level, these  feats make you a master in spell attack modifiers and spell  DCs and grant you a 7th-rank spell slot. If you have a spell  repertoire, |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/18` | 0.774161 | **Expert Spellcasting Feat:** Typically taken at 12th level,  these feats make you an expert in spell attack modifiers  and spell DCs and grant you a 4th-rank spell slot. If you  have a spell repertoi |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/21` | 0.698139 | You gain the basic spellcasting benefits (page 174). Each time  you gain a spell slot of a new rank from the mystic archetype,  add a spell of the appropriate spell rank to your repertoire: a  common |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/29` | 0.653225 | You gain the basic spellcasting benefits (page 174). Each time  you gain a spell slot of a new rank from the witchwarper  archetype, add a spell of the appropriate spell rank to your  repertoire: a co |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/16` | 0.646787 | Spellcasting archetypes always grant the ability to cast  cantrips in their dedication, and then they have a basic  spellcasting feat, an expert spellcasting feat, and a master  spellcasting feat. The |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/15` | 0.603424 | Some archetypes grant you a substantial degree of  spellcasting, albeit delayed compared to a character from a  spellcasting class. The spellcasting ability from a spellcasting  archetype also allows |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/42` | 0.575345 | Increase the number of spells in your repertoire and number  of spell slots you gain from mystic archetype feats by 1 for  each spell rank other than your two highest mystic spell slots. |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/21` | 0.559105 | Some archetype feats in other books have the skill trait,  allowing you to take them in place of a skill feat rather than  a class feat. A skill feat still counts to satisfy the requirement  of the de |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/13` | 0.558696 | Sometimes an archetype feat lets you select another feat,  such as a class feat of a lower level. You must always meet  any prerequisites of the feat you gain in this way. These  always count as only |

### Query 16
- Text: What is the rule about **Expert Spellcasting Feat:** Typically taken at 12th level,  these feats make you an expert in spell attack modifiers  and spell DCs and grant you a 4th-rank spell slot. If you  have a spell repertoire, you can select a second spell from  your repertoire as a signature spell. At 14th level, they grant  you a 5th-rank spell slot, and at 16th level, they grant you a  6th-rank spell slot. Archetypes refer to these benefits as the  "expert spellcasting benefits."?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/0/Text/18']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/0/Text/18', 'PZO22001 Starfinder Player Core 174-181::/page/0/Text/19', 'PZO22001 Starfinder Player Core 174-181::/page/0/Text/17']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/18` | 1.000753 | **Expert Spellcasting Feat:** Typically taken at 12th level,  these feats make you an expert in spell attack modifiers  and spell DCs and grant you a 4th-rank spell slot. If you  have a spell repertoi |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/19` | 0.876511 | **Master Spellcasting Feat:** Usually found at 18th level, these  feats make you a master in spell attack modifiers and spell  DCs and grant you a 7th-rank spell slot. If you have a spell  repertoire, |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/17` | 0.806060 | **Basic Spellcasting Feat:** Usually available at 4th level,  these feats grant a 1st-rank spell slot. At 6th level, they  grant you a 2nd-rank spell slot, and if you have a spell  repertoire, you can |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/16` | 0.712925 | Spellcasting archetypes always grant the ability to cast  cantrips in their dedication, and then they have a basic  spellcasting feat, an expert spellcasting feat, and a master  spellcasting feat. The |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/47` | 0.630421 | You gain the expert spellcasting benefits (page 174). |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/45` | 0.630421 | You gain the expert spellcasting benefits (page 174). |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/15` | 0.629210 | Some archetypes grant you a substantial degree of  spellcasting, albeit delayed compared to a character from a  spellcasting class. The spellcasting ability from a spellcasting  archetype also allows |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/21` | 0.614781 | You gain the basic spellcasting benefits (page 174). Each time  you gain a spell slot of a new rank from the mystic archetype,  add a spell of the appropriate spell rank to your repertoire: a  common |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/21` | 0.587267 | Some archetype feats in other books have the skill trait,  allowing you to take them in place of a skill feat rather than  a class feat. A skill feat still counts to satisfy the requirement  of the de |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/29` | 0.580978 | You gain the basic spellcasting benefits (page 174). Each time  you gain a spell slot of a new rank from the witchwarper  archetype, add a spell of the appropriate spell rank to your  repertoire: a co |

### Query 17
- Text: What is the rule about **Master Spellcasting Feat:** Usually found at 18th level, these  feats make you a master in spell attack modifiers and spell  DCs and grant you a 7th-rank spell slot. If you have a spell  repertoire, you can select a third spell from your repertoire as  a signature spell. At 20th level, they grant you an 8th-rank  spell slot. Archetypes refer to these benefits as the "master  spellcasting benefits."?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/0/Text/19']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/0/Text/19', 'PZO22001 Starfinder Player Core 174-181::/page/0/Text/18', 'PZO22001 Starfinder Player Core 174-181::/page/0/Text/17']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/19` | 0.994563 | **Master Spellcasting Feat:** Usually found at 18th level, these  feats make you a master in spell attack modifiers and spell  DCs and grant you a 7th-rank spell slot. If you have a spell  repertoire, |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/18` | 0.877805 | **Expert Spellcasting Feat:** Typically taken at 12th level,  these feats make you an expert in spell attack modifiers  and spell DCs and grant you a 4th-rank spell slot. If you  have a spell repertoi |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/17` | 0.829893 | **Basic Spellcasting Feat:** Usually available at 4th level,  these feats grant a 1st-rank spell slot. At 6th level, they  grant you a 2nd-rank spell slot, and if you have a spell  repertoire, you can |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/16` | 0.725416 | Spellcasting archetypes always grant the ability to cast  cantrips in their dedication, and then they have a basic  spellcasting feat, an expert spellcasting feat, and a master  spellcasting feat. The |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/15` | 0.632834 | Some archetypes grant you a substantial degree of  spellcasting, albeit delayed compared to a character from a  spellcasting class. The spellcasting ability from a spellcasting  archetype also allows |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/21` | 0.626959 | You gain the basic spellcasting benefits (page 174). Each time  you gain a spell slot of a new rank from the mystic archetype,  add a spell of the appropriate spell rank to your repertoire: a  common |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/50` | 0.620442 | You gain the master spellcasting benefits (page 174). |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/52` | 0.620442 | You gain the master spellcasting benefits (page 174). |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/29` | 0.594230 | You gain the basic spellcasting benefits (page 174). Each time  you gain a spell slot of a new rank from the witchwarper  archetype, add a spell of the appropriate spell rank to your  repertoire: a co |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/42` | 0.588546 | Increase the number of spells in your repertoire and number  of spell slots you gain from mystic archetype feats by 1 for  each spell rank other than your two highest mystic spell slots. |

### Query 18
- Text: Summarize SPECIAL ARCHETYPES
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/0/SectionHeader/20']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/0/SectionHeader/20', 'PZO22001 Starfinder Player Core 174-181::/page/0/SectionHeader/1', 'PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/11']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/0/SectionHeader/20` | 0.998367 | SPECIAL ARCHETYPES |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/0/SectionHeader/1` | 0.841832 | ARCHETYPES |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/11` | 0.708172 | **ARCHETYPE** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/18` | 0.666172 | **ARCHETYPE** |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/12` | 0.666172 | **ARCHETYPE** |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/23` | 0.666172 | **ARCHETYPE** |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/27` | 0.666172 | **ARCHETYPE** |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/14` | 0.666172 | **ARCHETYPE** |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/33` | 0.666172 | **ARCHETYPE** |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/6/SectionHeader/43` | 0.666172 | **ARCHETYPE** |

### Query 19
- Text: What is the rule about Some archetype feats in other books have the skill trait,  allowing you to take them in place of a skill feat rather than  a class feat. A skill feat still counts to satisfy the requirement  of the dedication. There are also class archetypes that can  modify your class's abilities as soon as 1st level. You can  never have more than one class archetype.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/0/Text/21']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/0/Text/21', 'PZO22001 Starfinder Player Core 174-181::/page/0/Text/9', 'PZO22001 Starfinder Player Core 174-181::/page/0/Text/11']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/21` | 1.009969 | Some archetype feats in other books have the skill trait,  allowing you to take them in place of a skill feat rather than  a class feat. A skill feat still counts to satisfy the requirement  of the de |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/9` | 0.824602 | Most archetypes in this book have the multiclass trait.  These allow you to diversify your training into another  class's specialties. You can't select a multiclass archetype's  dedication feat if you |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/11` | 0.805090 | Some archetypes include a list of "Additional Feats" that  appear in other sources. The list includes each feat's level,  which might be different than normal when gained from the  archetype. You can |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/5` | 0.743882 | An archetype feat is subject to any restrictions on the class  feat it replaces. For example, if you had an ability at 6th level  that granted you a bonus class feat, but that class feat had to  be 4t |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/13` | 0.740068 | Sometimes an archetype feat lets you select another feat,  such as a class feat of a lower level. You must always meet  any prerequisites of the feat you gain in this way. These  always count as only |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/7` | 0.713958 | Each archetype's dedication feat represents your character's  dedicated effort learning a new set of abilities, making it  impossible to split your focus and pursue another archetype  at the same time |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/4` | 0.702097 | You gain an archetype by selecting archetype feats instead  of your normal feats. First, find the archetype that best  fits your character concept. Then select that archetype's  dedication feat, using |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/2` | 0.624146 | Archetypes allow you to further customize your character concepts by taking more than one class. |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/40` | 0.606308 | You gain the adaptive talent class feature, but you do not  gain additional skill feats at higher levels. |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/16` | 0.602164 | Spellcasting archetypes always grant the ability to cast  cantrips in their dedication, and then they have a basic  spellcasting feat, an expert spellcasting feat, and a master  spellcasting feat. The |

### Query 20
- Text: Summarize ENVOY
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/1', 'PZO22001 Starfinder Player Core 174-181::/page/1/Text/46', 'PZO22001 Starfinder Player Core 174-181::/page/5/Text/50']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/1` | 0.877104 | ENVOY |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/46` | 0.684437 | **Envoy** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/50` | 0.684437 | **Envoy** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/7/Text/40` | 0.642437 | **Envoy** |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/3` | 0.555571 | MULTICLASS ENVOY  CHARACTERS |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/27` | 0.496414 | **ENVOY DEDICATION** **FEAT 2** |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/24` | 0.469447 | **Prerequisites** Envoy Dedication |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/39` | 0.469447 | **Prerequisites** Envoy Dedication |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/34` | 0.469447 | **Prerequisites** Envoy Dedication |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/19` | 0.469447 | **Prerequisites** Envoy Dedication |

### Query 21
- Text: Summarize You step up and lead others to victory while manipulating  those who stand in your way.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/1/Text/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/1/Text/2', 'PZO22001 Starfinder Player Core 174-181::/page/1/Text/4', 'PZO22001 Starfinder Player Core 174-181::/page/2/Text/4']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/2` | 1.022761 | You step up and lead others to victory while manipulating  those who stand in your way. |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/4` | 0.540587 | The envoy archetype allows you to take on a leadership role  by giving out directives that can support allies or hinder  enemies. |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/4` | 0.477463 | Mystics support allies and themselves with powerful magic. |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/1/ListItem/5` | 0.422471 | Mystic envoys can choose between using their magic  or directives to empower their allies, widening the  breadth of options available to them. |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/15` | 0.421440 | Your disruptive powers grow. You gain a 1st- or 2nd-level  witchwarper feat. |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/5/ListItem/9` | 0.398797 | Witchwarper soldiers want to further  hamper their enemy's movements and  are excellent at using grenades. |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/5/ListItem/5` | 0.391148 | Envoy soldiers are natural tacticians who use directives to  position enemies and allies to optimize their area attacks. |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/4/ListItem/6` | 0.381274 | Mystic solarians can augment themselves with  powerful spells and heal themselves while confronting  power enemies on the frontline. |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/3/ListItem/9` | 0.377414 | Witchwarper operatives combine operative mobility  feats with their quantum field to shake up enemy. |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/1/ListItem/9` | 0.374651 | Witchwarper envoys make powerful battlefield  controllers that help maximize a partys mobility while  inhibiting their foe's movement capabilities with area  spells and quantum field. |

### Query 22
- Text: What is the rule about MULTICLASS ENVOY  CHARACTERS?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/3']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/3', 'PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/3', 'PZO22001 Starfinder Player Core 174-181::/page/5/SectionHeader/3']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/3` | 0.888333 | MULTICLASS ENVOY  CHARACTERS |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/3` | 0.664415 | MULTICLASS OPERATIVE  CHARACTERS |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/5/SectionHeader/3` | 0.634800 | MULTICLASS SOLDIER  CHARACTERS |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/3` | 0.585205 | MULTICLASS MYSTIC  CHARACTERS |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/6/SectionHeader/3` | 0.530526 | MULTICLASS WITCHWARPER  CHARACTERS |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/4/SectionHeader/3` | 0.518851 | MULTICLASS SOLARIAN  CHARACTERS |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/14` | 0.446304 | You gain one envoy feat. For the purpose of meeting its  prerequisites, your envoy level is equal to half your character  level. |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/68` | 0.418539 | **INTRODUCTION** **ANCESTRIES & ** **BACKGROUNDS** **CLASSES** **Envoy** **Mystic** **Operative ** **Solarian** **Soldier** **Witchwarper** |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/9` | 0.415995 | Most archetypes in this book have the multiclass trait.  These allow you to diversify your training into another  class's specialties. You can't select a multiclass archetype's  dedication feat if you |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/1` | 0.408300 | ENVOY |

### Query 23
- Text: Summarize The envoy archetype allows you to take on a leadership role  by giving out directives that can support allies or hinder  enemies.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/1/Text/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/1/Text/4', 'PZO22001 Starfinder Player Core 174-181::/page/5/ListItem/5', 'PZO22001 Starfinder Player Core 174-181::/page/1/ListItem/5']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/4` | 1.032418 | The envoy archetype allows you to take on a leadership role  by giving out directives that can support allies or hinder  enemies. |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/5/ListItem/5` | 0.714680 | Envoy soldiers are natural tacticians who use directives to  position enemies and allies to optimize their area attacks. |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/1/ListItem/5` | 0.690770 | Mystic envoys can choose between using their magic  or directives to empower their allies, widening the  breadth of options available to them. |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/4/ListItem/5` | 0.620771 | Envoy solarians can rush into close quarters to  properly assess an enemy's abilities and positioning  when determining what directives to use. |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/1/ListItem/8` | 0.597649 | Soldier envoys make natural commanders who can  use their defensive capabilities to keep the bonuses  of their directive's active against powerful enemies  while clearing out weaker foes with area fir |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/14` | 0.585445 | You gain one envoy feat. For the purpose of meeting its  prerequisites, your envoy level is equal to half your character  level. |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/30` | 0.566280 | You gain the envoy directives class feature (see page  104), but do not gain the Lead by Example benefits  of the Get 'Em! envoy directive. You become trained in  Deception, Diplomacy, or Intimidation |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/35` | 0.560574 | You gain a 1st- or 2nd-level envoy feat of your choice. |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/4` | 0.509466 | The soldier archetype is ideal for characters who want to  specialize in area attacks. |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/1/ListItem/7` | 0.505202 | Solarian envoys are beacons of hope amid a chaotic  battlefield leading the charge with feats like Pardon  Me and Get in There! A solarian envoy can use Adaptive  Talent to choose different Athletics |

### Query 24
- Text: Summarize Mystic envoys can choose between using their magic  or directives to empower their allies, widening the  breadth of options available to them.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/1/ListItem/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/1/ListItem/5', 'PZO22001 Starfinder Player Core 174-181::/page/2/Text/4', 'PZO22001 Starfinder Player Core 174-181::/page/1/Text/4']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/1/ListItem/5` | 1.032779 | Mystic envoys can choose between using their magic  or directives to empower their allies, widening the  breadth of options available to them. |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/4` | 0.716936 | Mystics support allies and themselves with powerful magic. |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/4` | 0.672970 | The envoy archetype allows you to take on a leadership role  by giving out directives that can support allies or hinder  enemies. |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/4/ListItem/5` | 0.604244 | Envoy solarians can rush into close quarters to  properly assess an enemy's abilities and positioning  when determining what directives to use. |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/5/ListItem/5` | 0.561532 | Envoy soldiers are natural tacticians who use directives to  position enemies and allies to optimize their area attacks. |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/4/ListItem/6` | 0.541275 | Mystic solarians can augment themselves with  powerful spells and heal themselves while confronting  power enemies on the frontline. |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/1/ListItem/8` | 0.534758 | Soldier envoys make natural commanders who can  use their defensive capabilities to keep the bonuses  of their directive's active against powerful enemies  while clearing out weaker foes with area fir |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/1/ListItem/9` | 0.532319 | Witchwarper envoys make powerful battlefield  controllers that help maximize a partys mobility while  inhibiting their foe's movement capabilities with area  spells and quantum field. |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/35` | 0.515388 | You gain a 1st- or 2nd-level envoy feat of your choice. |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/1/ListItem/7` | 0.508440 | Solarian envoys are beacons of hope amid a chaotic  battlefield leading the charge with feats like Pardon  Me and Get in There! A solarian envoy can use Adaptive  Talent to choose different Athletics |

### Query 25
- Text: What is the rule about Operative envoys become incredibly precise killing  machines that can combine Aim with abilities like Get  'em! and Distant Feint. Ghost operatives also appreciate  extra feats that use Deception.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/1/ListItem/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/1/ListItem/6', 'PZO22001 Starfinder Player Core 174-181::/page/1/Text/30', 'PZO22001 Starfinder Player Core 174-181::/page/3/ListItem/5']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/1/ListItem/6` | 0.988607 | Operative envoys become incredibly precise killing  machines that can combine Aim with abilities like Get  'em! and Distant Feint. Ghost operatives also appreciate  extra feats that use Deception. |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/30` | 0.576632 | You gain the envoy directives class feature (see page  104), but do not gain the Lead by Example benefits  of the Get 'Em! envoy directive. You become trained in  Deception, Diplomacy, or Intimidation |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/3/ListItem/5` | 0.552139 | Envoy operatives direct allies while lining up perfect shots. |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/1/ListItem/8` | 0.502478 | Soldier envoys make natural commanders who can  use their defensive capabilities to keep the bonuses  of their directive's active against powerful enemies  while clearing out weaker foes with area fir |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/4` | 0.480029 | The operative archetype allows you to deal high damage to  a single target and select class feats and exploits that add to  your offensive options in combat. |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/3/ListItem/9` | 0.479886 | Witchwarper operatives combine operative mobility  feats with their quantum field to shake up enemy. |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/5/ListItem/7` | 0.478275 | Operative soldiers become versatile damage dealers  that can use their area weapons in situations where Aim  isn't as useful. |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/27` | 0.478151 | **Prerequisites** Operative Dedication, Specialized Operative You gain the exploit of your chosen specialization. |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/4/ListItem/5` | 0.477764 | Envoy solarians can rush into close quarters to  properly assess an enemy's abilities and positioning  when determining what directives to use. |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/23` | 0.471586 | **Special** You can select this feat more than once. Each time you  do, you gain another operative feat. |

### Query 26
- Text: What is the rule about Solarian envoys are beacons of hope amid a chaotic  battlefield leading the charge with feats like Pardon  Me and Get in There! A solarian envoy can use Adaptive  Talent to choose different Athletics feats based on the  terrain they expect to encounter.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/1/ListItem/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/1/ListItem/7', 'PZO22001 Starfinder Player Core 174-181::/page/4/ListItem/5', 'PZO22001 Starfinder Player Core 174-181::/page/4/Text/4']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/1/ListItem/7` | 0.987518 | Solarian envoys are beacons of hope amid a chaotic  battlefield leading the charge with feats like Pardon  Me and Get in There! A solarian envoy can use Adaptive  Talent to choose different Athletics |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/4/ListItem/5` | 0.654869 | Envoy solarians can rush into close quarters to  properly assess an enemy's abilities and positioning  when determining what directives to use. |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/4` | 0.592829 | The solarian archetype allows characters to wield powerful  solar weapons and engage in melee combat. |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/36` | 0.537095 | **Special** You can select this feat more than once. Each  time you do, you gain another solarian feat. |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/1/ListItem/8` | 0.530837 | Soldier envoys make natural commanders who can  use their defensive capabilities to keep the bonuses  of their directive's active against powerful enemies  while clearing out weaker foes with area fir |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/35` | 0.517905 | You gain a 1st- or 2nd-level envoy feat of your choice. |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/1/ListItem/5` | 0.516757 | Mystic envoys can choose between using their magic  or directives to empower their allies, widening the  breadth of options available to them. |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/35` | 0.516113 | You gain one solarian feat. For the purpose of meeting its  prerequisites, your solarian level is half your character level. |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/50` | 0.513883 | **Prerequisites** Solarian Dedication, expert in any kind of  weapon or unarmed attack |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/4` | 0.512894 | The envoy archetype allows you to take on a leadership role  by giving out directives that can support allies or hinder  enemies. |

### Query 27
- Text: What is the rule about Soldier envoys make natural commanders who can  use their defensive capabilities to keep the bonuses  of their directive's active against powerful enemies  while clearing out weaker foes with area fire. Erudite  warriors can take full advantage of Intimidation feats  like Quip and Cut 'em Deep.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/1/ListItem/8']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/1/ListItem/8', 'PZO22001 Starfinder Player Core 174-181::/page/5/ListItem/5', 'PZO22001 Starfinder Player Core 174-181::/page/4/ListItem/5']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/1/ListItem/8` | 0.981280 | Soldier envoys make natural commanders who can  use their defensive capabilities to keep the bonuses  of their directive's active against powerful enemies  while clearing out weaker foes with area fir |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/5/ListItem/5` | 0.672362 | Envoy soldiers are natural tacticians who use directives to  position enemies and allies to optimize their area attacks. |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/4/ListItem/5` | 0.637016 | Envoy solarians can rush into close quarters to  properly assess an enemy's abilities and positioning  when determining what directives to use. |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/30` | 0.581615 | You gain the envoy directives class feature (see page  104), but do not gain the Lead by Example benefits  of the Get 'Em! envoy directive. You become trained in  Deception, Diplomacy, or Intimidation |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/4` | 0.564878 | The envoy archetype allows you to take on a leadership role  by giving out directives that can support allies or hinder  enemies. |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/1/ListItem/9` | 0.522003 | Witchwarper envoys make powerful battlefield  controllers that help maximize a partys mobility while  inhibiting their foe's movement capabilities with area  spells and quantum field. |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/13` | 0.517855 | You become trained in Intimidation. If you  were already trained in Intimidation, you  instead become trained in a skill of your choice.  Increase your maximum and encumbered Bulk limits  by 2. You be |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/1/ListItem/5` | 0.513140 | Mystic envoys can choose between using their magic  or directives to empower their allies, widening the  breadth of options available to them. |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/1/ListItem/7` | 0.502638 | Solarian envoys are beacons of hope amid a chaotic  battlefield leading the charge with feats like Pardon  Me and Get in There! A solarian envoy can use Adaptive  Talent to choose different Athletics |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/1/ListItem/6` | 0.499441 | Operative envoys become incredibly precise killing  machines that can combine Aim with abilities like Get  'em! and Distant Feint. Ghost operatives also appreciate  extra feats that use Deception. |

### Query 28
- Text: What is the rule about Witchwarper envoys make powerful battlefield  controllers that help maximize a partys mobility while  inhibiting their foe's movement capabilities with area  spells and quantum field.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/1/ListItem/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/1/ListItem/9', 'PZO22001 Starfinder Player Core 174-181::/page/3/ListItem/9', 'PZO22001 Starfinder Player Core 174-181::/page/6/Text/4']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/1/ListItem/9` | 0.970290 | Witchwarper envoys make powerful battlefield  controllers that help maximize a partys mobility while  inhibiting their foe's movement capabilities with area  spells and quantum field. |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/3/ListItem/9` | 0.735783 | Witchwarper operatives combine operative mobility  feats with their quantum field to shake up enemy. |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/4` | 0.644450 | The witchwarper archetype allows you to cast reality warping  spells and manifest a quantum field. |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/4/ListItem/9` | 0.593019 | Witchwarper solarians can use gravity abilities to push  and pull enemies into their quantum auras. |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/5/ListItem/9` | 0.583740 | Witchwarper soldiers want to further  hamper their enemy's movements and  are excellent at using grenades. |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/15` | 0.538890 | Your disruptive powers grow. You gain a 1st- or 2nd-level  witchwarper feat. |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/4/ListItem/5` | 0.538553 | Envoy solarians can rush into close quarters to  properly assess an enemy's abilities and positioning  when determining what directives to use. |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/1/ListItem/5` | 0.537172 | Mystic envoys can choose between using their magic  or directives to empower their allies, widening the  breadth of options available to them. |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/1/ListItem/8` | 0.527016 | Soldier envoys make natural commanders who can  use their defensive capabilities to keep the bonuses  of their directive's active against powerful enemies  while clearing out weaker foes with area fir |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/5/ListItem/5` | 0.516759 | Envoy soldiers are natural tacticians who use directives to  position enemies and allies to optimize their area attacks. |

### Query 29
- Text: What are the requirements for **ADVANCED LEADERSHIP** **FEAT 6**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/10', 'PZO22001 Starfinder Player Core 174-181::/page/5/SectionHeader/25', 'PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/17']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/10` | 0.919789 | **ADVANCED LEADERSHIP** **FEAT 6** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/5/SectionHeader/25` | 0.712367 | **ADVANCED SOLDIER TRAINING** **FEAT 6** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/17` | 0.676219 | **ADVANCED GUNNER** **FEAT 6** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/6/SectionHeader/30` | 0.597849 | **ADVANCED DISTORTION** **FEAT 6** |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/36` | 0.581730 | **ADAPTIVE TALENT** **FEAT 6** |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/4/SectionHeader/31` | 0.560975 | **ADVANCED STELLAR ATTUNEMENT** **FEAT 6** |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/31` | 0.553388 | **BASIC LEADERSHIP** **FEAT 4** |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/27` | 0.552509 | **ADVANCED MYSTICISM** **FEAT 6** |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/13` | 0.497795 | **Prerequisites** Basic Leadership |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/21` | 0.470819 | **LEADER'S CONFIDENCE** **FEAT 12** |

### Query 30
- Text: Summarize **ARCHETYPE**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/12']
- Expected found: `True`
- Expected rank: `4`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/27', 'PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/21', 'PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/16']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/21` | 0.970267 | **ARCHETYPE** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/16` | 0.970267 | **ARCHETYPE** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/27` | 0.970267 | **ARCHETYPE** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/12` | 0.928267 | **ARCHETYPE** |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/18` | 0.928267 | **ARCHETYPE** |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/23` | 0.928267 | **ARCHETYPE** |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/32` | 0.928267 | **ARCHETYPE** |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/19` | 0.928267 | **ARCHETYPE** |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/14` | 0.928267 | **ARCHETYPE** |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/11` | 0.928267 | **ARCHETYPE** |

### Query 31
- Text: What are the requirements for **Prerequisites** Basic Leadership?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/1/Text/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/1/Text/13', 'PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/31', 'PZO22001 Starfinder Player Core 174-181::/page/5/Text/28']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/13` | 0.940411 | **Prerequisites** Basic Leadership |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/31` | 0.654650 | **BASIC LEADERSHIP** **FEAT 4** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/28` | 0.642748 | **Prerequisites** Basic Soldier Training |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/21` | 0.547700 | **Prerequisites** Basic Gunner |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/30` | 0.541123 | **Prerequisites** Basic Mysticism |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/33` | 0.495082 | **Prerequisites** Basic Distortion |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/12` | 0.448255 | **Prerequisites** Constitution +2 |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/8` | 0.431917 | **Prerequisites** Intelligence +2 |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/34` | 0.423852 | **Prerequisites** Basic Stellar Attunement |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/29` | 0.422168 | **Prerequisites** Charisma +2 |

### Query 32
- Text: What is the rule about You gain one envoy feat. For the purpose of meeting its  prerequisites, your envoy level is equal to half your character  level.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/1/Text/14']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/1/Text/14', 'PZO22001 Starfinder Player Core 174-181::/page/1/Text/35', 'PZO22001 Starfinder Player Core 174-181::/page/5/Text/29']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/14` | 0.977179 | You gain one envoy feat. For the purpose of meeting its  prerequisites, your envoy level is equal to half your character  level. |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/35` | 0.777565 | You gain a 1st- or 2nd-level envoy feat of your choice. |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/29` | 0.765914 | You gain one soldier feat. For the purpose of meeting its  prerequisites, your soldier level is half your character level. |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/22` | 0.680974 | You gain one operative feat. For the purpose of meeting its  prerequisites, your operative level is half your character level. |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/35` | 0.663972 | You gain one solarian feat. For the purpose of meeting its  prerequisites, your solarian level is half your character level. |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/31` | 0.661218 | You gain one mystic feat. For the purpose of meeting its  prerequisites, your mystic level is half your character level. |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/34` | 0.650527 | You gain one witchwarper feat. For the purpose of  meeting its prerequisites, your witchwarper level is half  your character level. |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/13` | 0.640965 | Sometimes an archetype feat lets you select another feat,  such as a class feat of a lower level. You must always meet  any prerequisites of the feat you gain in this way. These  always count as only |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/15` | 0.639493 | **Special** You can select this feat more than once. Each time  you select it, you gain another envoy feat. |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/4` | 0.531671 | The envoy archetype allows you to take on a leadership role  by giving out directives that can support allies or hinder  enemies. |

### Query 33
- Text: What is the rule about **Special** You can select this feat more than once. Each time  you select it, you gain another envoy feat.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/1/Text/15']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/1/Text/15', 'PZO22001 Starfinder Player Core 174-181::/page/3/Text/23', 'PZO22001 Starfinder Player Core 174-181::/page/5/Text/30']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/15` | 0.917262 | **Special** You can select this feat more than once. Each time  you select it, you gain another envoy feat. |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/23` | 0.773147 | **Special** You can select this feat more than once. Each time you  do, you gain another operative feat. |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/30` | 0.763890 | **Special** You can select this feat more than once. Each time  you do, you gain another soldier feat. |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/32` | 0.700117 | **Special** You can select this feat more than once. Each time  you do, you gain another mystic feat. |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/36` | 0.688773 | **Special** You can select this feat more than once. Each  time you do, you gain another solarian feat. |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/35` | 0.656291 | **Special** You can select this feat more than once. Each time  you do, you gain another witchwarper feat. |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/13` | 0.651309 | Sometimes an archetype feat lets you select another feat,  such as a class feat of a lower level. You must always meet  any prerequisites of the feat you gain in this way. These  always count as only |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/35` | 0.640420 | You gain a 1st- or 2nd-level envoy feat of your choice. |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/14` | 0.636919 | You gain one envoy feat. For the purpose of meeting its  prerequisites, your envoy level is equal to half your character  level. |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/41` | 0.567891 | **Special** You can select this feat a second time as a 10th level  feat and a 16th level feat, increasing the number of skill  feats you gain using adaptive talent by 1. |

### Query 34
- Text: What are the requirements for **REALLY GET EM!** **FEAT 8**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/16']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/16', 'PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/19', 'PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/24']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/16` | 0.843647 | **REALLY GET EM!** **FEAT 8** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/19` | 0.504987 | **STARFINDER PROVISIONS** **FEAT 8** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/24` | 0.501007 | **OPERATIVE EXPLOIT** **FEAT 8** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/38` | 0.451292 | **EXPANDED CONNECTION** **FEAT 8** |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/6/SectionHeader/36` | 0.444863 | **QUANTUM BREADTH** **FEAT 8** |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/25` | 0.437380 | **VETERAN TRAP FINDER** **FEAT 8** |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/54` | 0.388978 | **FEATS** |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/7/Text/48` | 0.388978 | **FEATS** |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/59` | 0.388978 | **FEATS** |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/40` | 0.388978 | **FEATS** |

### Query 35
- Text: Summarize **ARCHETYPE**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/18']
- Expected found: `True`
- Expected rank: `5`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/27', 'PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/21', 'PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/16']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/21` | 0.970267 | **ARCHETYPE** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/16` | 0.970267 | **ARCHETYPE** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/27` | 0.970267 | **ARCHETYPE** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/12` | 0.928267 | **ARCHETYPE** |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/18` | 0.928267 | **ARCHETYPE** |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/23` | 0.928267 | **ARCHETYPE** |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/32` | 0.928267 | **ARCHETYPE** |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/19` | 0.928267 | **ARCHETYPE** |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/14` | 0.928267 | **ARCHETYPE** |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/11` | 0.928267 | **ARCHETYPE** |

### Query 36
- Text: What are the requirements for **Prerequisites** Envoy Dedication?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/1/Text/19']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/1/Text/19', 'PZO22001 Starfinder Player Core 174-181::/page/1/Text/24', 'PZO22001 Starfinder Player Core 174-181::/page/1/Text/39']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/19` | 0.951082 | **Prerequisites** Envoy Dedication |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/39` | 0.951082 | **Prerequisites** Envoy Dedication |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/24` | 0.951082 | **Prerequisites** Envoy Dedication |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/34` | 0.909082 | **Prerequisites** Envoy Dedication |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/39` | 0.609078 | **Prerequisites** Soldier Dedication |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/18` | 0.609078 | **Prerequisites** Soldier Dedication |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/34` | 0.609078 | **Prerequisites** Soldier Dedication |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/60` | 0.586570 | **Prerequisites** Operative Dedication |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/55` | 0.586570 | **Prerequisites** Operative Dedication |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/50` | 0.586570 | **Prerequisites** Operative Dedication |

### Query 37
- Text: What is the rule about You gain the Lead by Example benefit for your Get 'Em!  directive, except you and your allies get a +2 status bonus  to damage on both the initial and subsequent Strikes.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/1/Text/20']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/1/Text/20', 'PZO22001 Starfinder Player Core 174-181::/page/1/Text/30', 'PZO22001 Starfinder Player Core 174-181::/page/3/Text/15']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/20` | 1.005338 | You gain the Lead by Example benefit for your Get 'Em!  directive, except you and your allies get a +2 status bonus  to damage on both the initial and subsequent Strikes. |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/30` | 0.669464 | You gain the envoy directives class feature (see page  104), but do not gain the Lead by Example benefits  of the Get 'Em! envoy directive. You become trained in  Deception, Diplomacy, or Intimidation |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/15` | 0.533558 | You gain the Aim action (page 128), it doesn't deal additional  damage, but still reduces the bonus to AC your mark gains  from cover (which does not increase as you gain levels). |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/19` | 0.457521 | You gain a 1st- or 2nd-level soldier feat. |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/13` | 0.446144 | Sometimes an archetype feat lets you select another feat,  such as a class feat of a lower level. You must always meet  any prerequisites of the feat you gain in this way. These  always count as only |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/30` | 0.434499 | **Special** You can select this feat more than once. Each time  you do, you gain another soldier feat. |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/56` | 0.421400 | Your ranged Strikes against the target of your Aim using the  required ranged weapon deal an additional 1d4 precision  damage until the end of your turn. This damage increases to  2d4 at 6th level. |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/24` | 0.416070 | You gain 3 additional Hit Points for each soldier archetype  class feat you have. As you continue selecting soldier  archetype class feats, you continue to gain additional Hit  Points in this way. |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/51` | 0.412711 | You gain a 1st- or 2nd-level operative feat. |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/16` | 0.407653 | class feat you have. As you continue selecting operative  archetype class feats, you continue to gain additional Hit Points  in this way. |

### Query 38
- Text: What are the requirements for **LEADER'S CONFIDENCE** **FEAT 12**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/21']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/21', 'PZO22001 Starfinder Player Core 174-181::/page/1/Text/25', 'PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/31']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/21` | 0.890760 | **LEADER'S CONFIDENCE** **FEAT 12** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/25` | 0.643419 | You gain the leader's confidence class feature (see page  107). |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/31` | 0.584533 | **BASIC LEADERSHIP** **FEAT 4** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/10` | 0.512087 | **ADVANCED LEADERSHIP** **FEAT 6** |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/5/SectionHeader/41` | 0.511312 | **SOLDIER'S TOUGHNESS** **FEAT 12** |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/13` | 0.509439 | **Prerequisites** Basic Leadership |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/28` | 0.492548 | **GUN EXPERT** **FEAT 12** |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/4/SectionHeader/47` | 0.472175 | **SOLAR MANIFESTATION EXPERT** **FEAT 12** |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/33` | 0.456530 | **MASTER SPY** **FEAT 12** |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/44` | 0.414588 | **Prerequisites** Soldier Dedication, expert in Fortitude saves. |

### Query 39
- Text: Summarize **ARCHETYPE**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/23']
- Expected found: `True`
- Expected rank: `6`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/27', 'PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/21', 'PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/16']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/21` | 0.970267 | **ARCHETYPE** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/16` | 0.970267 | **ARCHETYPE** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/27` | 0.970267 | **ARCHETYPE** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/12` | 0.928267 | **ARCHETYPE** |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/18` | 0.928267 | **ARCHETYPE** |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/23` | 0.928267 | **ARCHETYPE** |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/32` | 0.928267 | **ARCHETYPE** |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/19` | 0.928267 | **ARCHETYPE** |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/14` | 0.928267 | **ARCHETYPE** |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/11` | 0.928267 | **ARCHETYPE** |

### Query 40
- Text: What are the requirements for **Prerequisites** Envoy Dedication?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/1/Text/24']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/1/Text/19', 'PZO22001 Starfinder Player Core 174-181::/page/1/Text/24', 'PZO22001 Starfinder Player Core 174-181::/page/1/Text/39']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/19` | 0.951082 | **Prerequisites** Envoy Dedication |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/39` | 0.951082 | **Prerequisites** Envoy Dedication |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/24` | 0.951082 | **Prerequisites** Envoy Dedication |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/34` | 0.909082 | **Prerequisites** Envoy Dedication |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/39` | 0.609078 | **Prerequisites** Soldier Dedication |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/18` | 0.609078 | **Prerequisites** Soldier Dedication |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/34` | 0.609078 | **Prerequisites** Soldier Dedication |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/60` | 0.586570 | **Prerequisites** Operative Dedication |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/55` | 0.586570 | **Prerequisites** Operative Dedication |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/50` | 0.586570 | **Prerequisites** Operative Dedication |

### Query 41
- Text: What is the rule about You gain the leader's confidence class feature (see page  107).?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/1/Text/25']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/1/Text/25', 'PZO22001 Starfinder Player Core 174-181::/page/1/Text/30', 'PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/21']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/25` | 0.954314 | You gain the leader's confidence class feature (see page  107). |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/30` | 0.578723 | You gain the envoy directives class feature (see page  104), but do not gain the Lead by Example benefits  of the Get 'Em! envoy directive. You become trained in  Deception, Diplomacy, or Intimidation |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/21` | 0.576815 | **LEADER'S CONFIDENCE** **FEAT 12** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/13` | 0.514792 | **Prerequisites** Strength +2 You gain the stellar attunement class feature (page 140), but |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/40` | 0.493988 | You gain the primary target class feature (page 152). |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/35` | 0.493398 | You gain the suppressing fire class feature (page 152). |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/13` | 0.491401 | Sometimes an archetype feat lets you select another feat,  such as a class feat of a lower level. You must always meet  any prerequisites of the feat you gain in this way. These  always count as only |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/14` | 0.484867 | You become trained in light armor and medium armor. If  you already were trained in light armor and medium armor,  you gain training in heavy armor as well. Whenever you gain  a class feature that gra |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/40` | 0.466135 | You gain the adaptive talent class feature, but you do not  gain additional skill feats at higher levels. |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/20` | 0.460116 | You gain the Lead by Example benefit for your Get 'Em!  directive, except you and your allies get a +2 status bonus  to damage on both the initial and subsequent Strikes. |

### Query 42
- Text: What are the requirements for **ENVOY DEDICATION** **FEAT 2**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/27']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/27', 'PZO22001 Starfinder Player Core 174-181::/page/1/Text/34', 'PZO22001 Starfinder Player Core 174-181::/page/1/Text/19']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/27` | 0.904767 | **ENVOY DEDICATION** **FEAT 2** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/19` | 0.664474 | **Prerequisites** Envoy Dedication |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/34` | 0.664474 | **Prerequisites** Envoy Dedication |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/24` | 0.622474 | **Prerequisites** Envoy Dedication |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/39` | 0.622474 | **Prerequisites** Envoy Dedication |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/5/SectionHeader/10` | 0.602745 | **SOLDIER DEDICATION** **FEAT 2** |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/5` | 0.589489 | **MYSTIC DEDICATION** **FEAT 2** |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/10` | 0.587872 | **OPERATIVE DEDICATION** **FEAT 2** |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/4/SectionHeader/10` | 0.556735 | **SOLARIAN DEDICATION** **FEAT 2** |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/4` | 0.531926 | **STARFINDER FIELD AGENT DEDICATION** **FEAT 2** |

### Query 43
- Text: Summarize **ARCHETYPE** **DEDICATION** **MULTICLASS**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/1/Text/28']
- Expected found: `True`
- Expected rank: `4`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/3/Text/12', 'PZO22001 Starfinder Player Core 174-181::/page/6/SectionHeader/7', 'PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/7']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/7` | 1.016945 | **ARCHETYPE** **DEDICATION** **MULTICLASS** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/6/SectionHeader/7` | 1.016945 | **ARCHETYPE** **DEDICATION** **MULTICLASS** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/12` | 1.016945 | **ARCHETYPE** **DEDICATION** **MULTICLASS** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/28` | 0.974945 | **ARCHETYPE** **DEDICATION** **MULTICLASS** |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/7/Text/5` | 0.974945 | **ARCHETYPE** **DEDICATION** **MULTICLASS** |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/5/SectionHeader/11` | 0.974945 | **ARCHETYPE** **DEDICATION** **MULTICLASS** |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/12` | 0.974945 | **ARCHETYPE** **DEDICATION** **MULTICLASS** |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/0/SectionHeader/8` | 0.592590 | Multiclass Dedications |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/30` | 0.584352 | **ARCHETYPE** |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/5/SectionHeader/27` | 0.584352 | **ARCHETYPE** |

### Query 44
- Text: What are the requirements for **Prerequisites** Charisma +2?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/1/Text/29']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/1/Text/29', 'PZO22001 Starfinder Player Core 174-181::/page/6/Text/8', 'PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/8']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/29` | 0.930959 | **Prerequisites** Charisma +2 |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/8` | 0.632749 | **Prerequisites** Intelligence +2 |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/8` | 0.621242 | **Prerequisites** Wisdom +2 |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/12` | 0.556781 | **Prerequisites** Constitution +2 |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/30` | 0.520104 | **Prerequisites** Basic Mysticism |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/13` | 0.507021 | **Prerequisites** Dexterity +2 |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/13` | 0.438358 | **Prerequisites** Basic Leadership |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/13` | 0.423970 | **Prerequisites** Strength +2 You gain the stellar attunement class feature (page 140), but |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/36` | 0.416324 | **Prerequisites** Mystic Dedication |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/25` | 0.416324 | **Prerequisites** Mystic Dedication |

### Query 45
- Text: What is the rule about You gain the envoy directives class feature (see page  104), but do not gain the Lead by Example benefits  of the Get 'Em! envoy directive. You become trained in  Deception, Diplomacy, or Intimidation plus another skill of your  choice. If you were already trained in Deception, Diplomacy,  and Intimidation, you instead become trained in an additional  skill of your choice. You also become trained in envoy class DC.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/1/Text/30']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/1/Text/30', 'PZO22001 Starfinder Player Core 174-181::/page/1/Text/20', 'PZO22001 Starfinder Player Core 174-181::/page/5/Text/13']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/30` | 1.021078 | You gain the envoy directives class feature (see page  104), but do not gain the Lead by Example benefits  of the Get 'Em! envoy directive. You become trained in  Deception, Diplomacy, or Intimidation |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/20` | 0.694057 | You gain the Lead by Example benefit for your Get 'Em!  directive, except you and your allies get a +2 status bonus  to damage on both the initial and subsequent Strikes. |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/13` | 0.635884 | You become trained in Intimidation. If you  were already trained in Intimidation, you  instead become trained in a skill of your choice.  Increase your maximum and encumbered Bulk limits  by 2. You be |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/35` | 0.548178 | You gain a 1st- or 2nd-level envoy feat of your choice. |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/14` | 0.537546 | You become trained in light armor and medium armor. If  you already were trained in light armor and medium armor,  you gain training in heavy armor as well. Whenever you gain  a class feature that gra |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/1/ListItem/8` | 0.530407 | Soldier envoys make natural commanders who can  use their defensive capabilities to keep the bonuses  of their directive's active against powerful enemies  while clearing out weaker foes with area fir |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/4` | 0.527098 | The envoy archetype allows you to take on a leadership role  by giving out directives that can support allies or hinder  enemies. |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/14` | 0.526945 | You gain one envoy feat. For the purpose of meeting its  prerequisites, your envoy level is equal to half your character  level. |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/13` | 0.521599 | Sometimes an archetype feat lets you select another feat,  such as a class feat of a lower level. You must always meet  any prerequisites of the feat you gain in this way. These  always count as only |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/25` | 0.518361 | You gain the leader's confidence class feature (see page  107). |

### Query 46
- Text: What are the requirements for **BASIC LEADERSHIP** **FEAT 4**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/31']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/31', 'PZO22001 Starfinder Player Core 174-181::/page/1/Text/13', 'PZO22001 Starfinder Player Core 174-181::/page/5/SectionHeader/15']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/31` | 0.911767 | **BASIC LEADERSHIP** **FEAT 4** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/13` | 0.753075 | **Prerequisites** Basic Leadership |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/5/SectionHeader/15` | 0.673160 | **BASIC SOLDIER TRAINING** **FEAT 4** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/48` | 0.594860 | **BASIC GUNNER** **FEAT 4** |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/6/SectionHeader/11` | 0.568937 | **BASIC DISTORTION** **FEAT 4** |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/6/SectionHeader/16` | 0.558782 | **BASIC QUANTUM FIELD** **FEAT 4** |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/22` | 0.531887 | **BASIC MYSTICISM** **FEAT 4** |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/10` | 0.530039 | **ADVANCED LEADERSHIP** **FEAT 6** |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/4/SectionHeader/16` | 0.523284 | **BASIC STELLAR ATTUNEMENT** **FEAT 4** |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/6/SectionHeader/21` | 0.493049 | **BASIC WARP SPELL** **FEAT 4** |

### Query 47
- Text: Summarize **ARCHETYPE**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/33']
- Expected found: `True`
- Expected rank: `12`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/27', 'PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/21', 'PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/16']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/21` | 0.970267 | **ARCHETYPE** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/16` | 0.970267 | **ARCHETYPE** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/27` | 0.970267 | **ARCHETYPE** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/12` | 0.928267 | **ARCHETYPE** |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/18` | 0.928267 | **ARCHETYPE** |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/23` | 0.928267 | **ARCHETYPE** |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/32` | 0.928267 | **ARCHETYPE** |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/19` | 0.928267 | **ARCHETYPE** |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/14` | 0.928267 | **ARCHETYPE** |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/11` | 0.928267 | **ARCHETYPE** |

### Query 48
- Text: What are the requirements for **Prerequisites** Envoy Dedication?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/1/Text/34']
- Expected found: `True`
- Expected rank: `4`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/1/Text/19', 'PZO22001 Starfinder Player Core 174-181::/page/1/Text/24', 'PZO22001 Starfinder Player Core 174-181::/page/1/Text/39']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/19` | 0.951082 | **Prerequisites** Envoy Dedication |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/39` | 0.951082 | **Prerequisites** Envoy Dedication |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/24` | 0.951082 | **Prerequisites** Envoy Dedication |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/34` | 0.909082 | **Prerequisites** Envoy Dedication |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/39` | 0.609078 | **Prerequisites** Soldier Dedication |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/18` | 0.609078 | **Prerequisites** Soldier Dedication |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/34` | 0.609078 | **Prerequisites** Soldier Dedication |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/60` | 0.586570 | **Prerequisites** Operative Dedication |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/55` | 0.586570 | **Prerequisites** Operative Dedication |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/50` | 0.586570 | **Prerequisites** Operative Dedication |

### Query 49
- Text: What is the rule about You gain a 1st- or 2nd-level envoy feat of your choice.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/1/Text/35']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/1/Text/35', 'PZO22001 Starfinder Player Core 174-181::/page/1/Text/14', 'PZO22001 Starfinder Player Core 174-181::/page/1/Text/15']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/35` | 0.948736 | You gain a 1st- or 2nd-level envoy feat of your choice. |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/14` | 0.817219 | You gain one envoy feat. For the purpose of meeting its  prerequisites, your envoy level is equal to half your character  level. |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/15` | 0.738822 | **Special** You can select this feat more than once. Each time  you select it, you gain another envoy feat. |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/19` | 0.684020 | You gain a 1st- or 2nd-level soldier feat. |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/51` | 0.658142 | You gain a 1st- or 2nd-level operative feat. |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/20` | 0.632182 | You gain a 1st- or 2nd-level solarian feat. |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/13` | 0.628630 | Sometimes an archetype feat lets you select another feat,  such as a class feat of a lower level. You must always meet  any prerequisites of the feat you gain in this way. These  always count as only |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/26` | 0.614437 | You gain a 1st- or 2nd-level mystic feat. |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/30` | 0.579770 | You gain the envoy directives class feature (see page  104), but do not gain the Lead by Example benefits  of the Get 'Em! envoy directive. You become trained in  Deception, Diplomacy, or Intimidation |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/29` | 0.554148 | You gain one soldier feat. For the purpose of meeting its  prerequisites, your soldier level is half your character level. |

### Query 50
- Text: What are the requirements for **ADAPTIVE TALENT** **FEAT 6**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/36']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/36', 'PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/10', 'PZO22001 Starfinder Player Core 174-181::/page/5/SectionHeader/25']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/36` | 0.928092 | **ADAPTIVE TALENT** **FEAT 6** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/10` | 0.618561 | **ADVANCED LEADERSHIP** **FEAT 6** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/5/SectionHeader/25` | 0.593877 | **ADVANCED SOLDIER TRAINING** **FEAT 6** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/17` | 0.529437 | **ADVANCED GUNNER** **FEAT 6** |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/41` | 0.522647 | **Special** You can select this feat a second time as a 10th level  feat and a 16th level feat, increasing the number of skill  feats you gain using adaptive talent by 1. |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/4/SectionHeader/31` | 0.511895 | **ADVANCED STELLAR ATTUNEMENT** **FEAT 6** |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/6/SectionHeader/30` | 0.501377 | **ADVANCED DISTORTION** **FEAT 6** |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/40` | 0.500772 | You gain the adaptive talent class feature, but you do not  gain additional skill feats at higher levels. |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/5/SectionHeader/31` | 0.462126 | **SUPPRESSING FIRE** **FEAT 6** |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/27` | 0.448946 | **ADVANCED MYSTICISM** **FEAT 6** |

### Query 51
- Text: Summarize **ARCHETYPE**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/38']
- Expected found: `True`
- Expected rank: `13`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/27', 'PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/21', 'PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/16']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/21` | 0.970267 | **ARCHETYPE** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/16` | 0.970267 | **ARCHETYPE** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/27` | 0.970267 | **ARCHETYPE** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/12` | 0.928267 | **ARCHETYPE** |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/18` | 0.928267 | **ARCHETYPE** |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/23` | 0.928267 | **ARCHETYPE** |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/32` | 0.928267 | **ARCHETYPE** |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/19` | 0.928267 | **ARCHETYPE** |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/14` | 0.928267 | **ARCHETYPE** |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/11` | 0.928267 | **ARCHETYPE** |

### Query 52
- Text: What are the requirements for **Prerequisites** Envoy Dedication?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/1/Text/39']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/1/Text/19', 'PZO22001 Starfinder Player Core 174-181::/page/1/Text/24', 'PZO22001 Starfinder Player Core 174-181::/page/1/Text/39']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/19` | 0.951082 | **Prerequisites** Envoy Dedication |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/39` | 0.951082 | **Prerequisites** Envoy Dedication |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/24` | 0.951082 | **Prerequisites** Envoy Dedication |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/34` | 0.909082 | **Prerequisites** Envoy Dedication |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/39` | 0.609078 | **Prerequisites** Soldier Dedication |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/18` | 0.609078 | **Prerequisites** Soldier Dedication |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/34` | 0.609078 | **Prerequisites** Soldier Dedication |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/60` | 0.586570 | **Prerequisites** Operative Dedication |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/55` | 0.586570 | **Prerequisites** Operative Dedication |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/50` | 0.586570 | **Prerequisites** Operative Dedication |

### Query 53
- Text: What is the rule about You gain the adaptive talent class feature, but you do not  gain additional skill feats at higher levels.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/1/Text/40']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/1/Text/40', 'PZO22001 Starfinder Player Core 174-181::/page/1/Text/41', 'PZO22001 Starfinder Player Core 174-181::/page/0/Text/21']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/40` | 0.977442 | You gain the adaptive talent class feature, but you do not  gain additional skill feats at higher levels. |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/41` | 0.722599 | **Special** You can select this feat a second time as a 10th level  feat and a 16th level feat, increasing the number of skill  feats you gain using adaptive talent by 1. |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/21` | 0.681521 | Some archetype feats in other books have the skill trait,  allowing you to take them in place of a skill feat rather than  a class feat. A skill feat still counts to satisfy the requirement  of the de |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/5` | 0.577452 | An archetype feat is subject to any restrictions on the class  feat it replaces. For example, if you had an ability at 6th level  that granted you a bonus class feat, but that class feat had to  be 4t |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/11` | 0.576280 | Some archetypes include a list of "Additional Feats" that  appear in other sources. The list includes each feat's level,  which might be different than normal when gained from the  archetype. You can |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/14` | 0.553383 | You become trained in light armor and medium armor. If  you already were trained in light armor and medium armor,  you gain training in heavy armor as well. Whenever you gain  a class feature that gra |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/61` | 0.547362 | Choose a specialization. You become trained in one skill  determined by your specialization; if you were already trained  in that skill, you instead become trained in another skill of your  choice. Yo |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/13` | 0.538650 | Sometimes an archetype feat lets you select another feat,  such as a class feat of a lower level. You must always meet  any prerequisites of the feat you gain in this way. These  always count as only |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/9` | 0.531021 | Most archetypes in this book have the multiclass trait.  These allow you to diversify your training into another  class's specialties. You can't select a multiclass archetype's  dedication feat if you |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/16` | 0.521258 | class feat you have. As you continue selecting operative  archetype class feats, you continue to gain additional Hit Points  in this way. |

### Query 54
- Text: What is the rule about **Special** You can select this feat a second time as a 10th level  feat and a 16th level feat, increasing the number of skill  feats you gain using adaptive talent by 1.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/1/Text/41']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/1/Text/41', 'PZO22001 Starfinder Player Core 174-181::/page/3/Text/23', 'PZO22001 Starfinder Player Core 174-181::/page/1/Text/40']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/41` | 0.912258 | **Special** You can select this feat a second time as a 10th level  feat and a 16th level feat, increasing the number of skill  feats you gain using adaptive talent by 1. |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/23` | 0.707495 | **Special** You can select this feat more than once. Each time you  do, you gain another operative feat. |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/40` | 0.700905 | You gain the adaptive talent class feature, but you do not  gain additional skill feats at higher levels. |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/30` | 0.629466 | **Special** You can select this feat more than once. Each time  you do, you gain another soldier feat. |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/11` | 0.629083 | Some archetypes include a list of "Additional Feats" that  appear in other sources. The list includes each feat's level,  which might be different than normal when gained from the  archetype. You can |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/32` | 0.619888 | **Special** You can select this feat more than once. Each time  you do, you gain another mystic feat. |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/13` | 0.606333 | Sometimes an archetype feat lets you select another feat,  such as a class feat of a lower level. You must always meet  any prerequisites of the feat you gain in this way. These  always count as only |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/36` | 0.604678 | **Special** You can select this feat more than once. Each  time you do, you gain another solarian feat. |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/15` | 0.602067 | **Special** You can select this feat more than once. Each time  you select it, you gain another envoy feat. |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/21` | 0.597849 | Some archetype feats in other books have the skill trait,  allowing you to take them in place of a skill feat rather than  a class feat. A skill feat still counts to satisfy the requirement  of the de |

### Query 55
- Text: Summarize **INTRODUCTION**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/1/Text/43']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/1/Text/43', 'PZO22001 Starfinder Player Core 174-181::/page/5/Text/47', 'PZO22001 Starfinder Player Core 174-181::/page/7/Text/58']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/43` | 0.880541 | **INTRODUCTION** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/47` | 0.880541 | **INTRODUCTION** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/7/Text/58` | 0.611679 | **BACKGROUNDS** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/46` | 0.524467 | **INDEX** |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/7/Text/54` | 0.524467 | **INDEX** |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/7/Text/38` | 0.507539 | **INTRODUCTION** **ANCESTRIES & ** |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/66` | 0.452841 | **CHARACTER ** |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/44` | 0.416404 | **ANCESTRIES & ** **BACKGROUNDS** |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/48` | 0.416404 | **ANCESTRIES & ** **BACKGROUNDS** |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/7/Text/39` | 0.396768 | **CLASSES** |

### Query 56
- Text: What is the rule about **ANCESTRIES & ** **BACKGROUNDS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/1/Text/44']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/1/Text/44', 'PZO22001 Starfinder Player Core 174-181::/page/5/Text/48', 'PZO22001 Starfinder Player Core 174-181::/page/7/Text/38']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/44` | 0.920820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/48` | 0.920820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/7/Text/38` | 0.714101 | **INTRODUCTION** **ANCESTRIES & ** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/7/Text/58` | 0.606354 | **BACKGROUNDS** |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/68` | 0.438226 | **INTRODUCTION** **ANCESTRIES & ** **BACKGROUNDS** **CLASSES** **Envoy** **Mystic** **Operative ** **Solarian** **Soldier** **Witchwarper** |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/63` | 0.390721 | **CONDITIONS ** |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/33` | 0.357428 | **Prerequisites** Basic Distortion |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/7/Text/52` | 0.343180 | **CONDITIONS ** **APPENDIX** |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/44` | 0.343180 | **CONDITIONS ** **APPENDIX** |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/58` | 0.343180 | **CONDITIONS ** **APPENDIX** |

### Query 57
- Text: Summarize **CLASSES**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/1/Text/45']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/7/Text/39', 'PZO22001 Starfinder Player Core 174-181::/page/1/Text/45', 'PZO22001 Starfinder Player Core 174-181::/page/5/Text/49']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/7/Text/39` | 0.940061 | **CLASSES** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/45` | 0.940061 | **CLASSES** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/49` | 0.940061 | **CLASSES** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/68` | 0.500282 | **INTRODUCTION** **ANCESTRIES & ** **BACKGROUNDS** **CLASSES** **Envoy** **Mystic** **Operative ** **Solarian** **Soldier** **Witchwarper** |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/28` | 0.478760 | **ARCHETYPE** **DEDICATION** **MULTICLASS** |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/7/Text/5` | 0.478760 | **ARCHETYPE** **DEDICATION** **MULTICLASS** |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/5/SectionHeader/11` | 0.478760 | **ARCHETYPE** **DEDICATION** **MULTICLASS** |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/6/SectionHeader/7` | 0.478760 | **ARCHETYPE** **DEDICATION** **MULTICLASS** |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/12` | 0.478760 | **ARCHETYPE** **DEDICATION** **MULTICLASS** |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/7` | 0.478760 | **ARCHETYPE** **DEDICATION** **MULTICLASS** |

### Query 58
- Text: Summarize **Envoy**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/1/Text/46']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/1/Text/46', 'PZO22001 Starfinder Player Core 174-181::/page/5/Text/50', 'PZO22001 Starfinder Player Core 174-181::/page/7/Text/40']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/46` | 0.951326 | **Envoy** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/50` | 0.951326 | **Envoy** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/7/Text/40` | 0.951326 | **Envoy** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/24` | 0.645158 | **Prerequisites** Envoy Dedication |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/39` | 0.645158 | **Prerequisites** Envoy Dedication |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/34` | 0.645158 | **Prerequisites** Envoy Dedication |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/19` | 0.645158 | **Prerequisites** Envoy Dedication |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/1` | 0.566878 | ENVOY |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/35` | 0.523930 | You gain a 1st- or 2nd-level envoy feat of your choice. |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/3` | 0.520358 | MULTICLASS ENVOY  CHARACTERS |

### Query 59
- Text: Summarize **Mystic**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/1/Text/47']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/1/Text/47', 'PZO22001 Starfinder Player Core 174-181::/page/5/Text/51', 'PZO22001 Starfinder Player Core 174-181::/page/7/Text/41']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/47` | 0.959378 | **Mystic** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/51` | 0.959378 | **Mystic** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/7/Text/41` | 0.959378 | **Mystic** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/1` | 0.692252 | MYSTIC |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/15` | 0.675078 | **Prerequisites** Mystic Dedication |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/25` | 0.675078 | **Prerequisites** Mystic Dedication |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/20` | 0.675078 | **Prerequisites** Mystic Dedication |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/36` | 0.675078 | **Prerequisites** Mystic Dedication |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/30` | 0.664234 | **Prerequisites** Basic Mysticism |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/41` | 0.614018 | **Prerequisites** Basic Mystic Spellcasting |

### Query 60
- Text: Summarize **Operative **
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/1/Text/48']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/1/Text/48', 'PZO22001 Starfinder Player Core 174-181::/page/5/Text/52', 'PZO22001 Starfinder Player Core 174-181::/page/7/Text/42']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/48` | 0.958402 | **Operative ** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/52` | 0.958402 | **Operative ** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/7/Text/42` | 0.958402 | **Operative ** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/1` | 0.788647 | OPERATIVE |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/57` | 0.575799 | **SPECIALIZED OPERATIVE** **FEAT 4** |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/27` | 0.560053 | **Prerequisites** Operative Dedication, Specialized Operative You gain the exploit of your chosen specialization. |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/55` | 0.528468 | **Prerequisites** Operative Dedication |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/50` | 0.528468 | **Prerequisites** Operative Dedication |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/60` | 0.528468 | **Prerequisites** Operative Dedication |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/24` | 0.512281 | **OPERATIVE EXPLOIT** **FEAT 8** |

### Query 61
- Text: Summarize **Solarian**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/1/Text/49']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/1/Text/49', 'PZO22001 Starfinder Player Core 174-181::/page/7/Text/43', 'PZO22001 Starfinder Player Core 174-181::/page/5/Text/53']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/49` | 0.974700 | **Solarian** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/7/Text/43` | 0.974700 | **Solarian** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/53` | 0.974700 | **Solarian** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/4/SectionHeader/1` | 0.741070 | SOLARIAN |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/4/SectionHeader/10` | 0.649763 | **SOLARIAN DEDICATION** **FEAT 2** |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/4/SectionHeader/26` | 0.644115 | **SOLARIAN'S RESILIENCY** **FEAT 4** |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/45` | 0.612102 | **Prerequisites** Solarian Dedication |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/19` | 0.612102 | **Prerequisites** Solarian Dedication |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/24` | 0.612102 | **Prerequisites** Solarian Dedication |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/40` | 0.612102 | **Prerequisites** Solarian Dedication |

### Query 62
- Text: Summarize **Soldier**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/1/Text/50']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/1/Text/50', 'PZO22001 Starfinder Player Core 174-181::/page/7/Text/44', 'PZO22001 Starfinder Player Core 174-181::/page/5/Text/54']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/50` | 0.953061 | **Soldier** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/7/Text/44` | 0.953061 | **Soldier** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/54` | 0.953061 | **Soldier** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/5/SectionHeader/1` | 0.738275 | SOLDIER |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/39` | 0.636392 | **Prerequisites** Soldier Dedication |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/18` | 0.636392 | **Prerequisites** Soldier Dedication |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/34` | 0.636392 | **Prerequisites** Soldier Dedication |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/5/SectionHeader/10` | 0.633678 | **SOLDIER DEDICATION** **FEAT 2** |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/5/SectionHeader/3` | 0.576498 | MULTICLASS SOLDIER  CHARACTERS |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/5/SectionHeader/15` | 0.570636 | **BASIC SOLDIER TRAINING** **FEAT 4** |

### Query 63
- Text: Summarize **Witchwarper**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/1/Text/51']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/1/Text/51', 'PZO22001 Starfinder Player Core 174-181::/page/5/Text/55', 'PZO22001 Starfinder Player Core 174-181::/page/7/Text/45']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/51` | 0.988715 | **Witchwarper** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/55` | 0.988715 | **Witchwarper** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/7/Text/45` | 0.988715 | **Witchwarper** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/6/SectionHeader/1` | 0.809792 | WITCHWARPER |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/14` | 0.694514 | **Prerequisites** Witchwarper Dedication |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/19` | 0.694514 | **Prerequisites** Witchwarper Dedication |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/28` | 0.694514 | **Prerequisites** Witchwarper Dedication |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/24` | 0.694514 | **Prerequisites** Witchwarper Dedication |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/6/SectionHeader/5` | 0.682587 | **WITCHWARPER DEDICATION** **FEAT 2** |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/6/SectionHeader/3` | 0.665772 | MULTICLASS WITCHWARPER  CHARACTERS |

### Query 64
- Text: Summarize **Archetypes**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/1/Text/52']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/5/Text/56', 'PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/38', 'PZO22001 Starfinder Player Core 174-181::/page/1/Text/52']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/56` | 0.973323 | **Archetypes** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/38` | 0.973323 | **Archetypes** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/52` | 0.973323 | **Archetypes** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/7/Text/46` | 0.931323 | **Archetypes** |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/23` | 0.799429 | **ARCHETYPE** |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/21` | 0.799429 | **ARCHETYPE** |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/33` | 0.799429 | **ARCHETYPE** |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/40` | 0.799429 | **ARCHETYPE** |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/16` | 0.799429 | **ARCHETYPE** |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/50` | 0.799429 | **ARCHETYPE** |

### Query 65
- Text: What is the rule about **SKILLS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/1/Text/53']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/5/Text/57', 'PZO22001 Starfinder Player Core 174-181::/page/1/Text/53', 'PZO22001 Starfinder Player Core 174-181::/page/7/Text/47']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/57` | 0.864442 | **SKILLS** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/53` | 0.864442 | **SKILLS** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/7/Text/47` | 0.864442 | **SKILLS** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/39` | 0.822442 | **SKILLS** |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/21` | 0.462746 | Some archetype feats in other books have the skill trait,  allowing you to take them in place of a skill feat rather than  a class feat. A skill feat still counts to satisfy the requirement  of the de |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/61` | 0.432162 | Choose a specialization. You become trained in one skill  determined by your specialization; if you were already trained  in that skill, you instead become trained in another skill of your  choice. Yo |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/63` | 0.402477 | **CONDITIONS ** |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/7/Text/13` | 0.394510 | Coming prepared to mission briefings gives you extra time  to ask questions and research a topic relevant to your next  adventure. You are trained in Mission Lore, a special Lore skill  that can be us |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/40` | 0.393575 | You gain the adaptive talent class feature, but you do not  gain additional skill feats at higher levels. |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/9` | 0.384399 | Choose a connection (see page 119). You become trained in  the connection's skill or, if you were already trained, you  become trained in a skill of your choice. You don't gain any  other abilities fr |

### Query 66
- Text: What is the rule about **FEATS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/1/Text/54']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/3/Text/40', 'PZO22001 Starfinder Player Core 174-181::/page/5/Text/59', 'PZO22001 Starfinder Player Core 174-181::/page/1/Text/54']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/40` | 0.871817 | **FEATS** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/59` | 0.871817 | **FEATS** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/54` | 0.871817 | **FEATS** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/7/Text/48` | 0.829817 | **FEATS** |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/0/SectionHeader/10` | 0.520847 | ADDITIONAL FEATS |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/0/SectionHeader/12` | 0.512517 | FEATS THAT GRANT FEATS |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/13` | 0.450660 | Sometimes an archetype feat lets you select another feat,  such as a class feat of a lower level. You must always meet  any prerequisites of the feat you gain in this way. These  always count as only |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/16` | 0.436090 | **REALLY GET EM!** **FEAT 8** |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/11` | 0.425022 | Some archetypes include a list of "Additional Feats" that  appear in other sources. The list includes each feat's level,  which might be different than normal when gained from the  archetype. You can |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/23` | 0.398911 | **Special** You can select this feat more than once. Each time you  do, you gain another operative feat. |

### Query 67
- Text: Summarize **EQUIPMENT**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/1/Text/55']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/1/Text/55', 'PZO22001 Starfinder Player Core 174-181::/page/3/Text/41', 'PZO22001 Starfinder Player Core 174-181::/page/7/Text/49']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/55` | 0.944726 | **EQUIPMENT** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/41` | 0.944726 | **EQUIPMENT** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/7/Text/49` | 0.944726 | **EQUIPMENT** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/60` | 0.902726 | **EQUIPMENT** |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/11` | 0.429872 | **ARCHETYPE** |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/16` | 0.429872 | **ARCHETYPE** |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/38` | 0.429872 | **ARCHETYPE** |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/21` | 0.429872 | **ARCHETYPE** |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/33` | 0.429872 | **ARCHETYPE** |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/18` | 0.429872 | **ARCHETYPE** |

### Query 68
- Text: What is the rule about **SPELLS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/1/Text/56']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/5/Text/61', 'PZO22001 Starfinder Player Core 174-181::/page/1/Text/56', 'PZO22001 Starfinder Player Core 174-181::/page/3/Text/42']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/61` | 0.889304 | **SPELLS** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/56` | 0.889304 | **SPELLS** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/42` | 0.889304 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/7/Text/50` | 0.847304 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/6/SectionHeader/21` | 0.458093 | **BASIC WARP SPELL** **FEAT 4** |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/17` | 0.412247 | **BASIC MYSTIC SPELLCASTING** **FEAT 4** |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/43` | 0.393878 | **EXPERT MYSTIC SPELLCASTING** **FEAT 12** |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/39` | 0.388254 | **SKILLS** |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/57` | 0.388254 | **SKILLS** |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/53` | 0.388254 | **SKILLS** |

### Query 69
- Text: Summarize **PLAYING THE ** **GAME**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/1/Text/57']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/1/Text/57', 'PZO22001 Starfinder Player Core 174-181::/page/3/Text/43', 'PZO22001 Starfinder Player Core 174-181::/page/5/Text/62']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/57` | 0.965000 | **PLAYING THE ** **GAME** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/43` | 0.965000 | **PLAYING THE ** **GAME** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/62` | 0.965000 | **PLAYING THE ** **GAME** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/7/Text/51` | 0.923000 | **PLAYING THE ** **GAME** |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/47` | 0.418586 | **INTRODUCTION** |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/43` | 0.418586 | **INTRODUCTION** |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/66` | 0.388648 | **CHARACTER ** |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/60` | 0.356979 | **CHARACTER ** **SHEET** |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/47` | 0.356979 | **CHARACTER ** **SHEET** |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/7/Text/55` | 0.356979 | **CHARACTER ** **SHEET** |

### Query 70
- Text: Summarize **CONDITIONS ** **APPENDIX**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/1/Text/58']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/1/Text/58', 'PZO22001 Starfinder Player Core 174-181::/page/3/Text/44', 'PZO22001 Starfinder Player Core 174-181::/page/7/Text/52']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/58` | 0.983498 | **CONDITIONS ** **APPENDIX** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/44` | 0.983498 | **CONDITIONS ** **APPENDIX** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/7/Text/52` | 0.983498 | **CONDITIONS ** **APPENDIX** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/64` | 0.769880 | **APPENDIX** |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/63` | 0.645203 | **CONDITIONS ** |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/7/Text/54` | 0.423722 | **INDEX** |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/46` | 0.423722 | **INDEX** |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/48` | 0.416141 | **ANCESTRIES & ** **BACKGROUNDS** |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/44` | 0.416141 | **ANCESTRIES & ** **BACKGROUNDS** |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/7/Text/58` | 0.414903 | **BACKGROUNDS** |

### Query 71
- Text: Summarize **GLOSSARY & ** **INDEX**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/1/Text/59']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/1/Text/59', 'PZO22001 Starfinder Player Core 174-181::/page/5/Text/65', 'PZO22001 Starfinder Player Core 174-181::/page/3/Text/45']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/59` | 0.993465 | **GLOSSARY & ** **INDEX** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/65` | 0.993465 | **GLOSSARY & ** **INDEX** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/45` | 0.846819 | **GLOSSARY & ** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/7/Text/53` | 0.804819 | **GLOSSARY & ** |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/46` | 0.630357 | **INDEX** |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/7/Text/54` | 0.618357 | **INDEX** |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/7/Text/39` | 0.385404 | **CLASSES** |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/49` | 0.385404 | **CLASSES** |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/45` | 0.385404 | **CLASSES** |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/7/Text/38` | 0.372943 | **INTRODUCTION** **ANCESTRIES & ** |

### Query 72
- Text: What is the rule about **CHARACTER ** **SHEET**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/1/Text/60']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/7/Text/55', 'PZO22001 Starfinder Player Core 174-181::/page/1/Text/60', 'PZO22001 Starfinder Player Core 174-181::/page/3/Text/47']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/7/Text/55` | 0.859300 | **CHARACTER ** **SHEET** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/60` | 0.859300 | **CHARACTER ** **SHEET** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/47` | 0.859300 | **CHARACTER ** **SHEET** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/66` | 0.590820 | **CHARACTER ** |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/56` | 0.392353 | **Archetypes** |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/38` | 0.392353 | **Archetypes** |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/52` | 0.392353 | **Archetypes** |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/7/Text/46` | 0.392353 | **Archetypes** |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/63` | 0.378942 | **CONDITIONS ** |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/21` | 0.378239 | Some archetype feats in other books have the skill trait,  allowing you to take them in place of a skill feat rather than  a class feat. A skill feat still counts to satisfy the requirement  of the de |

### Query 73
- Text: Summarize MYSTIC
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/1', 'PZO22001 Starfinder Player Core 174-181::/page/1/Text/47', 'PZO22001 Starfinder Player Core 174-181::/page/5/Text/51']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/1` | 0.947410 | MYSTIC |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/47` | 0.738015 | **Mystic** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/51` | 0.738015 | **Mystic** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/7/Text/41` | 0.696015 | **Mystic** |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/3` | 0.602199 | MULTICLASS MYSTIC  CHARACTERS |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/15` | 0.533113 | **Prerequisites** Mystic Dedication |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/20` | 0.533113 | **Prerequisites** Mystic Dedication |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/36` | 0.533113 | **Prerequisites** Mystic Dedication |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/25` | 0.533113 | **Prerequisites** Mystic Dedication |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/5` | 0.519792 | **MYSTIC DEDICATION** **FEAT 2** |

### Query 74
- Text: Summarize You channel a fundamental force of the universe.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/2/Text/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/2/Text/2', 'PZO22001 Starfinder Player Core 174-181::/page/4/Text/2', 'PZO22001 Starfinder Player Core 174-181::/page/6/Text/2']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/2` | 1.021431 | You channel a fundamental force of the universe. |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/2` | 0.588214 | You are a solar knight attuned to the powerful forces  of gravity and light, manifesting the cosmic cycle into  armaments made of stellar energy. |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/2` | 0.489904 | You can draw on the infinite possibilities of other universes and  timelines to warp reality with powerful magic. |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/20` | 0.415303 | Your quantum field gains the effect of your chosen paradox. |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/4/ListItem/9` | 0.398263 | Witchwarper solarians can use gravity abilities to push  and pull enemies into their quantum auras. |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/9` | 0.389775 | Choose a paradox (page 167). You become trained in the paradox's  skill or, if you were already trained, you become trained in a skill  of your choice. You gain the Warp Reality action (page 164), but |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/7/Text/2` | 0.385159 | You are a trained agent of the Starfinder Society, a group  of adventures, scholars, and xenoarchaeologists seeking  knowledge, treasure, and secrets across the galaxy. |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/4` | 0.373376 | The witchwarper archetype allows you to cast reality warping  spells and manifest a quantum field. |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/35` | 0.367864 | You gain one solarian feat. For the purpose of meeting its  prerequisites, your solarian level is half your character level. |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/15` | 0.364502 | Your disruptive powers grow. You gain a 1st- or 2nd-level  witchwarper feat. |

### Query 75
- Text: What is the rule about MULTICLASS MYSTIC  CHARACTERS?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/3']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/3', 'PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/3', 'PZO22001 Starfinder Player Core 174-181::/page/5/SectionHeader/3']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/3` | 0.890922 | MULTICLASS MYSTIC  CHARACTERS |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/3` | 0.702458 | MULTICLASS OPERATIVE  CHARACTERS |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/5/SectionHeader/3` | 0.652933 | MULTICLASS SOLDIER  CHARACTERS |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/3` | 0.580353 | MULTICLASS ENVOY  CHARACTERS |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/6/SectionHeader/3` | 0.575223 | MULTICLASS WITCHWARPER  CHARACTERS |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/4/SectionHeader/3` | 0.569711 | MULTICLASS SOLARIAN  CHARACTERS |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/9` | 0.469406 | Most archetypes in this book have the multiclass trait.  These allow you to diversify your training into another  class's specialties. You can't select a multiclass archetype's  dedication feat if you |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/1` | 0.460930 | MYSTIC |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/12` | 0.419405 | **ARCHETYPE** **DEDICATION** **MULTICLASS** |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/12` | 0.419405 | **ARCHETYPE** **DEDICATION** **MULTICLASS** |

### Query 76
- Text: Summarize Mystics support allies and themselves with powerful magic.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/2/Text/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/2/Text/4', 'PZO22001 Starfinder Player Core 174-181::/page/1/ListItem/5', 'PZO22001 Starfinder Player Core 174-181::/page/4/ListItem/6']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/4` | 1.024853 | Mystics support allies and themselves with powerful magic. |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/1/ListItem/5` | 0.723928 | Mystic envoys can choose between using their magic  or directives to empower their allies, widening the  breadth of options available to them. |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/4/ListItem/6` | 0.701281 | Mystic solarians can augment themselves with  powerful spells and heal themselves while confronting  power enemies on the frontline. |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/51` | 0.554645 | **Mystic** |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/47` | 0.554645 | **Mystic** |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/7/Text/41` | 0.554645 | **Mystic** |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/31` | 0.516878 | You gain one mystic feat. For the purpose of meeting its  prerequisites, your mystic level is half your character level. |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/26` | 0.496309 | You gain a 1st- or 2nd-level mystic feat. |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/5/ListItem/6` | 0.476017 | Mystic soldiers with the elemental connection can make  different area weapons on the fly that deal different  types of damage. |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/25` | 0.474459 | **Prerequisites** Mystic Dedication |

### Query 77
- Text: What are the requirements for **MYSTIC DEDICATION** **FEAT 2**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/5', 'PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/15', 'PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/36']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/5` | 0.901130 | **MYSTIC DEDICATION** **FEAT 2** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/15` | 0.699172 | **Prerequisites** Mystic Dedication |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/36` | 0.699172 | **Prerequisites** Mystic Dedication |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/20` | 0.657172 | **Prerequisites** Mystic Dedication |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/25` | 0.657172 | **Prerequisites** Mystic Dedication |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/27` | 0.627907 | **ENVOY DEDICATION** **FEAT 2** |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/10` | 0.617685 | **OPERATIVE DEDICATION** **FEAT 2** |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/4/SectionHeader/10` | 0.591066 | **SOLARIAN DEDICATION** **FEAT 2** |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/5/SectionHeader/10` | 0.581890 | **SOLDIER DEDICATION** **FEAT 2** |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/55` | 0.532959 | **Prerequisites** Operative Dedication |

### Query 78
- Text: Summarize **ARCHETYPE** **DEDICATION** **MULTICLASS**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/3/Text/12', 'PZO22001 Starfinder Player Core 174-181::/page/6/SectionHeader/7', 'PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/7']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/7` | 1.016945 | **ARCHETYPE** **DEDICATION** **MULTICLASS** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/6/SectionHeader/7` | 1.016945 | **ARCHETYPE** **DEDICATION** **MULTICLASS** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/12` | 1.016945 | **ARCHETYPE** **DEDICATION** **MULTICLASS** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/28` | 0.974945 | **ARCHETYPE** **DEDICATION** **MULTICLASS** |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/7/Text/5` | 0.974945 | **ARCHETYPE** **DEDICATION** **MULTICLASS** |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/5/SectionHeader/11` | 0.974945 | **ARCHETYPE** **DEDICATION** **MULTICLASS** |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/12` | 0.974945 | **ARCHETYPE** **DEDICATION** **MULTICLASS** |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/0/SectionHeader/8` | 0.592590 | Multiclass Dedications |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/30` | 0.584352 | **ARCHETYPE** |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/5/SectionHeader/27` | 0.584352 | **ARCHETYPE** |

### Query 79
- Text: What are the requirements for **Prerequisites** Wisdom +2?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/8']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/8', 'PZO22001 Starfinder Player Core 174-181::/page/6/Text/8', 'PZO22001 Starfinder Player Core 174-181::/page/1/Text/29']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/8` | 0.910895 | **Prerequisites** Wisdom +2 |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/8` | 0.771462 | **Prerequisites** Intelligence +2 |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/29` | 0.652199 | **Prerequisites** Charisma +2 |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/12` | 0.608834 | **Prerequisites** Constitution +2 |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/13` | 0.560012 | **Prerequisites** Dexterity +2 |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/30` | 0.499921 | **Prerequisites** Basic Mysticism |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/13` | 0.446681 | **Prerequisites** Basic Leadership |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/28` | 0.419762 | **Prerequisites** Witchwarper Dedication |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/14` | 0.419762 | **Prerequisites** Witchwarper Dedication |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/19` | 0.419762 | **Prerequisites** Witchwarper Dedication |

### Query 80
- Text: What is the rule about Choose a connection (see page 119). You become trained in  the connection's skill or, if you were already trained, you  become trained in a skill of your choice. You don't gain any  other abilities from your choice of connection. You gain the  mystic bond class feature (see page 116).?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/2/Text/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/2/Text/9', 'PZO22001 Starfinder Player Core 174-181::/page/3/Text/61', 'PZO22001 Starfinder Player Core 174-181::/page/2/Text/21']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/9` | 0.996261 | Choose a connection (see page 119). You become trained in  the connection's skill or, if you were already trained, you  become trained in a skill of your choice. You don't gain any  other abilities fr |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/61` | 0.681440 | Choose a specialization. You become trained in one skill  determined by your specialization; if you were already trained  in that skill, you instead become trained in another skill of your  choice. Yo |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/21` | 0.623928 | You gain the basic spellcasting benefits (page 174). Each time  you gain a spell slot of a new rank from the mystic archetype,  add a spell of the appropriate spell rank to your repertoire: a  common |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/10` | 0.568824 | You cast spells like a mystic and gain the Cast a Spell  activity. You gain a spell repertoire with two common cantrips  from the spell list granted by your connection, from the spells  granted by you |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/9` | 0.526587 | Choose a paradox (page 167). You become trained in the paradox's  skill or, if you were already trained, you become trained in a skill  of your choice. You gain the Warp Reality action (page 164), but |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/46` | 0.522356 | **Prerequisites** Basic Mystic Spellcasting; master in  connection skill |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/21` | 0.516745 | Some archetype feats in other books have the skill trait,  allowing you to take them in place of a skill feat rather than  a class feat. A skill feat still counts to satisfy the requirement  of the de |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/32` | 0.509560 | **Special** You can select this feat more than once. Each time  you do, you gain another mystic feat. |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/9` | 0.509078 | Most archetypes in this book have the multiclass trait.  These allow you to diversify your training into another  class's specialties. You can't select a multiclass archetype's  dedication feat if you |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/37` | 0.502218 | You gain your connection's initial epiphany spell. If  you don't already have one, you also gain a focus  pool of 1 Focus Point, which you can Refocus by  reflecting on your connection. |

### Query 81
- Text: What is the rule about You cast spells like a mystic and gain the Cast a Spell  activity. You gain a spell repertoire with two common cantrips  from the spell list granted by your connection, from the spells  granted by your connection, or any other cantrips of that  tradition you learn or discover. You're trained in the spell  attack modifier and spell DC statistics. Your key spellcasting  attribute for mystic archetype spells is Wisdom, and they are  mystic spells of your connection's tradition.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/2/Text/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/2/Text/10', 'PZO22001 Starfinder Player Core 174-181::/page/2/Text/21', 'PZO22001 Starfinder Player Core 174-181::/page/6/Text/10']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/10` | 0.987701 | You cast spells like a mystic and gain the Cast a Spell  activity. You gain a spell repertoire with two common cantrips  from the spell list granted by your connection, from the spells  granted by you |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/21` | 0.780147 | You gain the basic spellcasting benefits (page 174). Each time  you gain a spell slot of a new rank from the mystic archetype,  add a spell of the appropriate spell rank to your repertoire: a  common |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/10` | 0.772277 | You cast spells like a witchwarper. You gain access to the Cast  a Spell activity. You gain a spell repertoire with two common  cantrips from the spell list associated with your paradox, from  the spe |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/16` | 0.710396 | Spellcasting archetypes always grant the ability to cast  cantrips in their dedication, and then they have a basic  spellcasting feat, an expert spellcasting feat, and a master  spellcasting feat. The |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/29` | 0.637239 | You gain the basic spellcasting benefits (page 174). Each time  you gain a spell slot of a new rank from the witchwarper  archetype, add a spell of the appropriate spell rank to your  repertoire: a co |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/9` | 0.632062 | Choose a connection (see page 119). You become trained in  the connection's skill or, if you were already trained, you  become trained in a skill of your choice. You don't gain any  other abilities fr |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/42` | 0.626362 | Increase the number of spells in your repertoire and number  of spell slots you gain from mystic archetype feats by 1 for  each spell rank other than your two highest mystic spell slots. |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/15` | 0.612836 | Some archetypes grant you a substantial degree of  spellcasting, albeit delayed compared to a character from a  spellcasting class. The spellcasting ability from a spellcasting  archetype also allows |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/40` | 0.593186 | Your repertoire expands, and you can cast more spells of your  paradox's tradition each day. Increase the number of spells  in your repertoire and number of spell slots you gain from  witchwarper arch |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/46` | 0.582354 | **Prerequisites** Basic Mystic Spellcasting; master in  connection skill |

### Query 82
- Text: What are the requirements for **VITALITY NETWORK** **FEAT 4**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/12']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/12', 'PZO22001 Starfinder Player Core 174-181::/page/2/Text/16', 'PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/31']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/12` | 0.910006 | **VITALITY NETWORK** **FEAT 4** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/16` | 0.497801 | You gain a vitality network with 10 Hit Points and can  use Transfer Vitality to transfer up to 10 HP. Increase the  maximum capacity of your vitality network by 10 at 10th,  15th, and 20th-level. Inc |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/31` | 0.489713 | **BASIC LEADERSHIP** **FEAT 4** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/62` | 0.436639 | **OPERATIVE RESILIENCY** **FEAT 4** |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/52` | 0.425908 | **SHARPSHOOTER** **FEAT 4** |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/57` | 0.414536 | **SPECIALIZED OPERATIVE** **FEAT 4** |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/4/SectionHeader/26` | 0.406962 | **SOLARIAN'S RESILIENCY** **FEAT 4** |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/5/SectionHeader/20` | 0.401939 | **SOLDIER'S RESILIENCY** **FEAT 4** |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/9` | 0.400169 | **MISSION BRIEFING** **FEAT 4** |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/4/SectionHeader/21` | 0.380252 | **SOLAR WEAPON CUSTOMIZATION** **FEAT 4** |

### Query 83
- Text: Summarize **ARCHETYPE**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/14']
- Expected found: `True`
- Expected rank: `9`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/27', 'PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/21', 'PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/16']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/21` | 0.970267 | **ARCHETYPE** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/16` | 0.970267 | **ARCHETYPE** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/27` | 0.970267 | **ARCHETYPE** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/12` | 0.928267 | **ARCHETYPE** |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/18` | 0.928267 | **ARCHETYPE** |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/23` | 0.928267 | **ARCHETYPE** |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/32` | 0.928267 | **ARCHETYPE** |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/19` | 0.928267 | **ARCHETYPE** |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/14` | 0.928267 | **ARCHETYPE** |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/11` | 0.928267 | **ARCHETYPE** |

### Query 84
- Text: What are the requirements for **Prerequisites** Mystic Dedication?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/15']
- Expected found: `True`
- Expected rank: `4`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/20', 'PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/25', 'PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/36']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/20` | 0.961052 | **Prerequisites** Mystic Dedication |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/25` | 0.961052 | **Prerequisites** Mystic Dedication |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/36` | 0.961052 | **Prerequisites** Mystic Dedication |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/15` | 0.919052 | **Prerequisites** Mystic Dedication |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/30` | 0.738153 | **Prerequisites** Basic Mysticism |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/41` | 0.614823 | **Prerequisites** Basic Mystic Spellcasting |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/19` | 0.612598 | **Prerequisites** Solarian Dedication |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/45` | 0.612598 | **Prerequisites** Solarian Dedication |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/24` | 0.612598 | **Prerequisites** Solarian Dedication |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/40` | 0.612598 | **Prerequisites** Solarian Dedication |

### Query 85
- Text: What is the rule about You gain a vitality network with 10 Hit Points and can  use Transfer Vitality to transfer up to 10 HP. Increase the  maximum capacity of your vitality network by 10 at 10th,  15th, and 20th-level. Increase the amount you can transfer  by 5 at 5th, 10th, 15th, and 20th-level.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/2/Text/16']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/2/Text/16', 'PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/12', 'PZO22001 Starfinder Player Core 174-181::/page/1/Text/41']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/16` | 0.973766 | You gain a vitality network with 10 Hit Points and can  use Transfer Vitality to transfer up to 10 HP. Increase the  maximum capacity of your vitality network by 10 at 10th,  15th, and 20th-level. Inc |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/12` | 0.497100 | **VITALITY NETWORK** **FEAT 4** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/41` | 0.494646 | **Special** You can select this feat a second time as a 10th level  feat and a 16th level feat, increasing the number of skill  feats you gain using adaptive talent by 1. |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/16` | 0.450896 | class feat you have. As you continue selecting operative  archetype class feats, you continue to gain additional Hit Points  in this way. |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/66` | 0.446721 | You gain 3 additional Hit Points for each operative archetype |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/30` | 0.437637 | You gain 3 additional Hit Points for each solarian archetype  class feat you have. As you continue selecting solarian  archetype class feats, you continue to gain additional Hit  Points in this way. |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/37` | 0.431095 | You gain your connection's initial epiphany spell. If  you don't already have one, you also gain a focus  pool of 1 Focus Point, which you can Refocus by  reflecting on your connection. |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/24` | 0.420677 | You gain 3 additional Hit Points for each soldier archetype  class feat you have. As you continue selecting soldier  archetype class feats, you continue to gain additional Hit  Points in this way. |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/42` | 0.420256 | Increase the number of spells in your repertoire and number  of spell slots you gain from mystic archetype feats by 1 for  each spell rank other than your two highest mystic spell slots. |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/40` | 0.414218 | Your repertoire expands, and you can cast more spells of your  paradox's tradition each day. Increase the number of spells  in your repertoire and number of spell slots you gain from  witchwarper arch |

### Query 86
- Text: What are the requirements for **BASIC MYSTIC SPELLCASTING** **FEAT 4**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/17']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/17', 'PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/43', 'PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/48']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/17` | 0.915593 | **BASIC MYSTIC SPELLCASTING** **FEAT 4** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/43` | 0.749274 | **EXPERT MYSTIC SPELLCASTING** **FEAT 12** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/48` | 0.722734 | **MASTER MYSTIC SPELLCASTING** **FEAT 18** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/6/SectionHeader/26` | 0.645958 | **BASIC WITCHWARPER SPELLCASTING** **FEAT 4** |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/41` | 0.582178 | **Prerequisites** Basic Mystic Spellcasting |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/6/SectionHeader/21` | 0.550124 | **BASIC WARP SPELL** **FEAT 4** |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/22` | 0.548110 | **BASIC MYSTICISM** **FEAT 4** |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/6/SectionHeader/11` | 0.512700 | **BASIC DISTORTION** **FEAT 4** |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/46` | 0.506366 | **Prerequisites** Basic Mystic Spellcasting; master in  connection skill |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/4/SectionHeader/16` | 0.503887 | **BASIC STELLAR ATTUNEMENT** **FEAT 4** |

### Query 87
- Text: Summarize **ARCHETYPE**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/19']
- Expected found: `True`
- Expected rank: `8`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/27', 'PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/21', 'PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/16']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/21` | 0.970267 | **ARCHETYPE** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/16` | 0.970267 | **ARCHETYPE** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/27` | 0.970267 | **ARCHETYPE** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/12` | 0.928267 | **ARCHETYPE** |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/18` | 0.928267 | **ARCHETYPE** |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/23` | 0.928267 | **ARCHETYPE** |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/32` | 0.928267 | **ARCHETYPE** |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/19` | 0.928267 | **ARCHETYPE** |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/14` | 0.928267 | **ARCHETYPE** |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/11` | 0.928267 | **ARCHETYPE** |

### Query 88
- Text: What are the requirements for **Prerequisites** Mystic Dedication?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/20']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/20', 'PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/25', 'PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/36']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/20` | 0.961052 | **Prerequisites** Mystic Dedication |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/25` | 0.961052 | **Prerequisites** Mystic Dedication |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/36` | 0.961052 | **Prerequisites** Mystic Dedication |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/15` | 0.919052 | **Prerequisites** Mystic Dedication |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/30` | 0.738153 | **Prerequisites** Basic Mysticism |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/41` | 0.614823 | **Prerequisites** Basic Mystic Spellcasting |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/19` | 0.612598 | **Prerequisites** Solarian Dedication |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/45` | 0.612598 | **Prerequisites** Solarian Dedication |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/24` | 0.612598 | **Prerequisites** Solarian Dedication |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/40` | 0.612598 | **Prerequisites** Solarian Dedication |

### Query 89
- Text: What is the rule about You gain the basic spellcasting benefits (page 174). Each time  you gain a spell slot of a new rank from the mystic archetype,  add a spell of the appropriate spell rank to your repertoire: a  common spell of your connection's tradition, or one of your  connection's granted spells.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/2/Text/21']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/2/Text/21', 'PZO22001 Starfinder Player Core 174-181::/page/6/Text/29', 'PZO22001 Starfinder Player Core 174-181::/page/2/Text/10']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/21` | 0.971189 | You gain the basic spellcasting benefits (page 174). Each time  you gain a spell slot of a new rank from the mystic archetype,  add a spell of the appropriate spell rank to your repertoire: a  common |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/29` | 0.832605 | You gain the basic spellcasting benefits (page 174). Each time  you gain a spell slot of a new rank from the witchwarper  archetype, add a spell of the appropriate spell rank to your  repertoire: a co |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/10` | 0.719871 | You cast spells like a mystic and gain the Cast a Spell  activity. You gain a spell repertoire with two common cantrips  from the spell list granted by your connection, from the spells  granted by you |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/42` | 0.676859 | Increase the number of spells in your repertoire and number  of spell slots you gain from mystic archetype feats by 1 for  each spell rank other than your two highest mystic spell slots. |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/17` | 0.671417 | **Basic Spellcasting Feat:** Usually available at 4th level,  these feats grant a 1st-rank spell slot. At 6th level, they  grant you a 2nd-rank spell slot, and if you have a spell  repertoire, you can |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/9` | 0.632197 | Choose a connection (see page 119). You become trained in  the connection's skill or, if you were already trained, you  become trained in a skill of your choice. You don't gain any  other abilities fr |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/16` | 0.631054 | Spellcasting archetypes always grant the ability to cast  cantrips in their dedication, and then they have a basic  spellcasting feat, an expert spellcasting feat, and a master  spellcasting feat. The |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/52` | 0.598626 | You gain the master spellcasting benefits (page 174). |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/50` | 0.598626 | You gain the master spellcasting benefits (page 174). |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/40` | 0.593600 | Your repertoire expands, and you can cast more spells of your  paradox's tradition each day. Increase the number of spells  in your repertoire and number of spell slots you gain from  witchwarper arch |

### Query 90
- Text: What are the requirements for **BASIC MYSTICISM** **FEAT 4**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/22']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/22', 'PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/30', 'PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/41']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/22` | 0.876370 | **BASIC MYSTICISM** **FEAT 4** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/30` | 0.770393 | **Prerequisites** Basic Mysticism |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/41` | 0.653578 | **Prerequisites** Basic Mystic Spellcasting |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/31` | 0.578105 | **BASIC LEADERSHIP** **FEAT 4** |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/27` | 0.568931 | **ADVANCED MYSTICISM** **FEAT 6** |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/6/SectionHeader/16` | 0.563580 | **BASIC QUANTUM FIELD** **FEAT 4** |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/6/SectionHeader/11` | 0.552287 | **BASIC DISTORTION** **FEAT 4** |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/17` | 0.545020 | **BASIC MYSTIC SPELLCASTING** **FEAT 4** |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/20` | 0.540443 | **Prerequisites** Mystic Dedication |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/15` | 0.540443 | **Prerequisites** Mystic Dedication |

### Query 91
- Text: Summarize **ARCHETYPE**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/24']
- Expected found: `True`
- Expected rank: `30`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/27', 'PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/21', 'PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/16']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/21` | 0.970267 | **ARCHETYPE** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/16` | 0.970267 | **ARCHETYPE** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/27` | 0.970267 | **ARCHETYPE** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/12` | 0.928267 | **ARCHETYPE** |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/18` | 0.928267 | **ARCHETYPE** |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/23` | 0.928267 | **ARCHETYPE** |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/32` | 0.928267 | **ARCHETYPE** |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/19` | 0.928267 | **ARCHETYPE** |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/14` | 0.928267 | **ARCHETYPE** |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/11` | 0.928267 | **ARCHETYPE** |

### Query 92
- Text: What are the requirements for **Prerequisites** Mystic Dedication?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/25']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/20', 'PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/25', 'PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/36']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/20` | 0.961052 | **Prerequisites** Mystic Dedication |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/25` | 0.961052 | **Prerequisites** Mystic Dedication |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/36` | 0.961052 | **Prerequisites** Mystic Dedication |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/15` | 0.919052 | **Prerequisites** Mystic Dedication |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/30` | 0.738153 | **Prerequisites** Basic Mysticism |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/41` | 0.614823 | **Prerequisites** Basic Mystic Spellcasting |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/19` | 0.612598 | **Prerequisites** Solarian Dedication |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/45` | 0.612598 | **Prerequisites** Solarian Dedication |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/24` | 0.612598 | **Prerequisites** Solarian Dedication |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/40` | 0.612598 | **Prerequisites** Solarian Dedication |

### Query 93
- Text: What is the rule about You gain a 1st- or 2nd-level mystic feat.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/2/Text/26']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/2/Text/26', 'PZO22001 Starfinder Player Core 174-181::/page/2/Text/31', 'PZO22001 Starfinder Player Core 174-181::/page/3/Text/51']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/26` | 0.946130 | You gain a 1st- or 2nd-level mystic feat. |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/31` | 0.766906 | You gain one mystic feat. For the purpose of meeting its  prerequisites, your mystic level is half your character level. |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/51` | 0.721345 | You gain a 1st- or 2nd-level operative feat. |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/32` | 0.680579 | **Special** You can select this feat more than once. Each time  you do, you gain another mystic feat. |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/20` | 0.670947 | You gain a 1st- or 2nd-level solarian feat. |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/19` | 0.650183 | You gain a 1st- or 2nd-level soldier feat. |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/35` | 0.609738 | You gain a 1st- or 2nd-level envoy feat of your choice. |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/42` | 0.587955 | Increase the number of spells in your repertoire and number  of spell slots you gain from mystic archetype feats by 1 for  each spell rank other than your two highest mystic spell slots. |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/15` | 0.570212 | Your disruptive powers grow. You gain a 1st- or 2nd-level  witchwarper feat. |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/21` | 0.550594 | You gain the basic spellcasting benefits (page 174). Each time  you gain a spell slot of a new rank from the mystic archetype,  add a spell of the appropriate spell rank to your repertoire: a  common |

### Query 94
- Text: What are the requirements for **ADVANCED MYSTICISM** **FEAT 6**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/27']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/27', 'PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/30', 'PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/10']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/27` | 0.894896 | **ADVANCED MYSTICISM** **FEAT 6** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/30` | 0.673978 | **Prerequisites** Basic Mysticism |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/10` | 0.634210 | **ADVANCED LEADERSHIP** **FEAT 6** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/22` | 0.588035 | **BASIC MYSTICISM** **FEAT 4** |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/6/SectionHeader/30` | 0.564281 | **ADVANCED DISTORTION** **FEAT 6** |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/41` | 0.556595 | **Prerequisites** Basic Mystic Spellcasting |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/4/SectionHeader/31` | 0.556321 | **ADVANCED STELLAR ATTUNEMENT** **FEAT 6** |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/20` | 0.555231 | **Prerequisites** Mystic Dedication |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/15` | 0.555231 | **Prerequisites** Mystic Dedication |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/25` | 0.555231 | **Prerequisites** Mystic Dedication |

### Query 95
- Text: Summarize **ARCHETYPE**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/29']
- Expected found: `True`
- Expected rank: `29`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/27', 'PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/21', 'PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/16']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/21` | 0.970267 | **ARCHETYPE** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/16` | 0.970267 | **ARCHETYPE** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/27` | 0.970267 | **ARCHETYPE** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/12` | 0.928267 | **ARCHETYPE** |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/18` | 0.928267 | **ARCHETYPE** |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/23` | 0.928267 | **ARCHETYPE** |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/32` | 0.928267 | **ARCHETYPE** |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/19` | 0.928267 | **ARCHETYPE** |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/14` | 0.928267 | **ARCHETYPE** |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/11` | 0.928267 | **ARCHETYPE** |

### Query 96
- Text: What are the requirements for **Prerequisites** Basic Mysticism?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/30']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/30', 'PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/15', 'PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/20']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/30` | 0.965472 | **Prerequisites** Basic Mysticism |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/15` | 0.728195 | **Prerequisites** Mystic Dedication |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/20` | 0.728195 | **Prerequisites** Mystic Dedication |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/25` | 0.686195 | **Prerequisites** Mystic Dedication |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/36` | 0.686195 | **Prerequisites** Mystic Dedication |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/41` | 0.677983 | **Prerequisites** Basic Mystic Spellcasting |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/46` | 0.586651 | **Prerequisites** Basic Mystic Spellcasting; master in  connection skill |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/22` | 0.560480 | **BASIC MYSTICISM** **FEAT 4** |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/13` | 0.543221 | **Prerequisites** Basic Leadership |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/51` | 0.510089 | **Prerequisites** Expert Mystic Spellcasting; legendary in  connection skill |

### Query 97
- Text: What is the rule about You gain one mystic feat. For the purpose of meeting its  prerequisites, your mystic level is half your character level.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/2/Text/31']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/2/Text/31', 'PZO22001 Starfinder Player Core 174-181::/page/6/Text/34', 'PZO22001 Starfinder Player Core 174-181::/page/2/Text/26']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/31` | 0.974343 | You gain one mystic feat. For the purpose of meeting its  prerequisites, your mystic level is half your character level. |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/34` | 0.754879 | You gain one witchwarper feat. For the purpose of  meeting its prerequisites, your witchwarper level is half  your character level. |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/26` | 0.750850 | You gain a 1st- or 2nd-level mystic feat. |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/22` | 0.707319 | You gain one operative feat. For the purpose of meeting its  prerequisites, your operative level is half your character level. |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/35` | 0.687953 | You gain one solarian feat. For the purpose of meeting its  prerequisites, your solarian level is half your character level. |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/29` | 0.685041 | You gain one soldier feat. For the purpose of meeting its  prerequisites, your soldier level is half your character level. |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/14` | 0.672024 | You gain one envoy feat. For the purpose of meeting its  prerequisites, your envoy level is equal to half your character  level. |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/32` | 0.626987 | **Special** You can select this feat more than once. Each time  you do, you gain another mystic feat. |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/42` | 0.569559 | Increase the number of spells in your repertoire and number  of spell slots you gain from mystic archetype feats by 1 for  each spell rank other than your two highest mystic spell slots. |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/13` | 0.559282 | Sometimes an archetype feat lets you select another feat,  such as a class feat of a lower level. You must always meet  any prerequisites of the feat you gain in this way. These  always count as only |

### Query 98
- Text: What is the rule about **Special** You can select this feat more than once. Each time  you do, you gain another mystic feat.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/2/Text/32']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/2/Text/32', 'PZO22001 Starfinder Player Core 174-181::/page/3/Text/23', 'PZO22001 Starfinder Player Core 174-181::/page/4/Text/36']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/32` | 0.908154 | **Special** You can select this feat more than once. Each time  you do, you gain another mystic feat. |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/23` | 0.782405 | **Special** You can select this feat more than once. Each time you  do, you gain another operative feat. |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/36` | 0.751449 | **Special** You can select this feat more than once. Each  time you do, you gain another solarian feat. |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/15` | 0.703566 | **Special** You can select this feat more than once. Each time  you select it, you gain another envoy feat. |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/35` | 0.697313 | **Special** You can select this feat more than once. Each time  you do, you gain another witchwarper feat. |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/30` | 0.686746 | **Special** You can select this feat more than once. Each time  you do, you gain another soldier feat. |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/26` | 0.624601 | You gain a 1st- or 2nd-level mystic feat. |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/31` | 0.602335 | You gain one mystic feat. For the purpose of meeting its  prerequisites, your mystic level is half your character level. |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/13` | 0.589371 | Sometimes an archetype feat lets you select another feat,  such as a class feat of a lower level. You must always meet  any prerequisites of the feat you gain in this way. These  always count as only |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/41` | 0.587756 | **Special** You can select this feat a second time as a 10th level  feat and a 16th level feat, increasing the number of skill  feats you gain using adaptive talent by 1. |

### Query 99
- Text: What are the requirements for **BASIC EPIPHANY** **FEAT 6**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/33']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/33', 'PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/31', 'PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/36']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/33` | 0.907763 | **BASIC EPIPHANY** **FEAT 6** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/31` | 0.504254 | **BASIC LEADERSHIP** **FEAT 4** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/36` | 0.486556 | **ADAPTIVE TALENT** **FEAT 6** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/5/SectionHeader/31` | 0.444008 | **SUPPRESSING FIRE** **FEAT 6** |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/5/SectionHeader/25` | 0.437853 | **ADVANCED SOLDIER TRAINING** **FEAT 6** |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/48` | 0.436634 | **BASIC GUNNER** **FEAT 4** |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/5/SectionHeader/15` | 0.433769 | **BASIC SOLDIER TRAINING** **FEAT 4** |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/17` | 0.428020 | **ADVANCED GUNNER** **FEAT 6** |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/6/SectionHeader/11` | 0.424303 | **BASIC DISTORTION** **FEAT 4** |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/21` | 0.422720 | **Prerequisites** Basic Gunner |

### Query 100
- Text: Summarize **ARCHETYPE**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/35']
- Expected found: `True`
- Expected rank: `28`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/27', 'PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/21', 'PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/16']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/21` | 0.970267 | **ARCHETYPE** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/16` | 0.970267 | **ARCHETYPE** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/27` | 0.970267 | **ARCHETYPE** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/12` | 0.928267 | **ARCHETYPE** |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/18` | 0.928267 | **ARCHETYPE** |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/23` | 0.928267 | **ARCHETYPE** |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/32` | 0.928267 | **ARCHETYPE** |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/19` | 0.928267 | **ARCHETYPE** |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/14` | 0.928267 | **ARCHETYPE** |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/11` | 0.928267 | **ARCHETYPE** |

### Query 101
- Text: What are the requirements for **Prerequisites** Mystic Dedication?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/36']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/20', 'PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/25', 'PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/36']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/20` | 0.961052 | **Prerequisites** Mystic Dedication |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/25` | 0.961052 | **Prerequisites** Mystic Dedication |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/36` | 0.961052 | **Prerequisites** Mystic Dedication |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/15` | 0.919052 | **Prerequisites** Mystic Dedication |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/30` | 0.738153 | **Prerequisites** Basic Mysticism |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/41` | 0.614823 | **Prerequisites** Basic Mystic Spellcasting |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/19` | 0.612598 | **Prerequisites** Solarian Dedication |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/45` | 0.612598 | **Prerequisites** Solarian Dedication |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/24` | 0.612598 | **Prerequisites** Solarian Dedication |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/40` | 0.612598 | **Prerequisites** Solarian Dedication |

### Query 102
- Text: What is the rule about You gain your connection's initial epiphany spell. If  you don't already have one, you also gain a focus  pool of 1 Focus Point, which you can Refocus by  reflecting on your connection.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/2/Text/37']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/2/Text/37', 'PZO22001 Starfinder Player Core 174-181::/page/6/Text/25', 'PZO22001 Starfinder Player Core 174-181::/page/2/Text/9']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/37` | 0.988198 | You gain your connection's initial epiphany spell. If  you don't already have one, you also gain a focus  pool of 1 Focus Point, which you can Refocus by  reflecting on your connection. |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/25` | 0.685846 | You gain your paradox's initial warp spell. If you don't already  have one, you also gain a focus pool of 1 Focus Point, which you  can Refocus by contemplating infinite worlds. (For more on warp  spe |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/9` | 0.607687 | Choose a connection (see page 119). You become trained in  the connection's skill or, if you were already trained, you  become trained in a skill of your choice. You don't gain any  other abilities fr |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/21` | 0.518378 | You gain the basic spellcasting benefits (page 174). Each time  you gain a spell slot of a new rank from the mystic archetype,  add a spell of the appropriate spell rank to your repertoire: a  common |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/10` | 0.466518 | You cast spells like a mystic and gain the Cast a Spell  activity. You gain a spell repertoire with two common cantrips  from the spell list granted by your connection, from the spells  granted by you |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/7` | 0.463240 | Each archetype's dedication feat represents your character's  dedicated effort learning a new set of abilities, making it  impossible to split your focus and pursue another archetype  at the same time |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/29` | 0.457116 | You gain the basic spellcasting benefits (page 174). Each time  you gain a spell slot of a new rank from the witchwarper  archetype, add a spell of the appropriate spell rank to your  repertoire: a co |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/42` | 0.448283 | Increase the number of spells in your repertoire and number  of spell slots you gain from mystic archetype feats by 1 for  each spell rank other than your two highest mystic spell slots. |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/13` | 0.445507 | Sometimes an archetype feat lets you select another feat,  such as a class feat of a lower level. You must always meet  any prerequisites of the feat you gain in this way. These  always count as only |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/46` | 0.440699 | **Prerequisites** Basic Mystic Spellcasting; master in  connection skill |

### Query 103
- Text: What are the requirements for **EXPANDED CONNECTION** **FEAT 8**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/38']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/38', 'PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/16', 'PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/24']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/38` | 0.921111 | **EXPANDED CONNECTION** **FEAT 8** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/16` | 0.532821 | **REALLY GET EM!** **FEAT 8** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/24` | 0.517509 | **OPERATIVE EXPLOIT** **FEAT 8** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/19` | 0.447814 | **STARFINDER PROVISIONS** **FEAT 8** |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/37` | 0.429909 | You gain your connection's initial epiphany spell. If  you don't already have one, you also gain a focus  pool of 1 Focus Point, which you can Refocus by  reflecting on your connection. |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/46` | 0.429183 | **Prerequisites** Basic Mystic Spellcasting; master in  connection skill |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/6/SectionHeader/36` | 0.417415 | **QUANTUM BREADTH** **FEAT 8** |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/25` | 0.389793 | **VETERAN TRAP FINDER** **FEAT 8** |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/10` | 0.376672 | **ADVANCED LEADERSHIP** **FEAT 6** |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/51` | 0.376637 | **Prerequisites** Expert Mystic Spellcasting; legendary in  connection skill |

### Query 104
- Text: Summarize **ARCHETYPE**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/40']
- Expected found: `True`
- Expected rank: `27`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/27', 'PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/21', 'PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/16']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/21` | 0.970267 | **ARCHETYPE** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/16` | 0.970267 | **ARCHETYPE** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/27` | 0.970267 | **ARCHETYPE** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/12` | 0.928267 | **ARCHETYPE** |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/18` | 0.928267 | **ARCHETYPE** |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/23` | 0.928267 | **ARCHETYPE** |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/32` | 0.928267 | **ARCHETYPE** |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/19` | 0.928267 | **ARCHETYPE** |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/14` | 0.928267 | **ARCHETYPE** |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/11` | 0.928267 | **ARCHETYPE** |

### Query 105
- Text: What are the requirements for **Prerequisites** Basic Mystic Spellcasting?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/41']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/41', 'PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/30', 'PZO22001 Starfinder Player Core 174-181::/page/2/Text/46']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/41` | 0.963218 | **Prerequisites** Basic Mystic Spellcasting |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/30` | 0.808876 | **Prerequisites** Basic Mysticism |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/46` | 0.802752 | **Prerequisites** Basic Mystic Spellcasting; master in  connection skill |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/51` | 0.708986 | **Prerequisites** Expert Mystic Spellcasting; legendary in  connection skill |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/39` | 0.681987 | **Prerequisites** Basic Witchwarper Spellcasting |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/36` | 0.639657 | **Prerequisites** Mystic Dedication |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/20` | 0.639657 | **Prerequisites** Mystic Dedication |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/15` | 0.639657 | **Prerequisites** Mystic Dedication |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/25` | 0.639657 | **Prerequisites** Mystic Dedication |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/21` | 0.578356 | You gain the basic spellcasting benefits (page 174). Each time  you gain a spell slot of a new rank from the mystic archetype,  add a spell of the appropriate spell rank to your repertoire: a  common |

### Query 106
- Text: What is the rule about Increase the number of spells in your repertoire and number  of spell slots you gain from mystic archetype feats by 1 for  each spell rank other than your two highest mystic spell slots.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/2/Text/42']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/2/Text/42', 'PZO22001 Starfinder Player Core 174-181::/page/6/Text/40', 'PZO22001 Starfinder Player Core 174-181::/page/2/Text/21']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/42` | 0.937716 | Increase the number of spells in your repertoire and number  of spell slots you gain from mystic archetype feats by 1 for  each spell rank other than your two highest mystic spell slots. |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/40` | 0.752701 | Your repertoire expands, and you can cast more spells of your  paradox's tradition each day. Increase the number of spells  in your repertoire and number of spell slots you gain from  witchwarper arch |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/21` | 0.721959 | You gain the basic spellcasting benefits (page 174). Each time  you gain a spell slot of a new rank from the mystic archetype,  add a spell of the appropriate spell rank to your repertoire: a  common |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/29` | 0.588845 | You gain the basic spellcasting benefits (page 174). Each time  you gain a spell slot of a new rank from the witchwarper  archetype, add a spell of the appropriate spell rank to your  repertoire: a co |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/16` | 0.576246 | Spellcasting archetypes always grant the ability to cast  cantrips in their dedication, and then they have a basic  spellcasting feat, an expert spellcasting feat, and a master  spellcasting feat. The |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/10` | 0.569429 | You cast spells like a mystic and gain the Cast a Spell  activity. You gain a spell repertoire with two common cantrips  from the spell list granted by your connection, from the spells  granted by you |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/26` | 0.564169 | You gain a 1st- or 2nd-level mystic feat. |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/31` | 0.561519 | You gain one mystic feat. For the purpose of meeting its  prerequisites, your mystic level is half your character level. |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/32` | 0.558165 | **Special** You can select this feat more than once. Each time  you do, you gain another mystic feat. |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/17` | 0.555771 | **Basic Spellcasting Feat:** Usually available at 4th level,  these feats grant a 1st-rank spell slot. At 6th level, they  grant you a 2nd-rank spell slot, and if you have a spell  repertoire, you can |

### Query 107
- Text: What are the requirements for **EXPERT MYSTIC SPELLCASTING** **FEAT 12**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/43']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/43', 'PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/17', 'PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/48']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/43` | 0.922505 | **EXPERT MYSTIC SPELLCASTING** **FEAT 12** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/17` | 0.761190 | **BASIC MYSTIC SPELLCASTING** **FEAT 4** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/48` | 0.749174 | **MASTER MYSTIC SPELLCASTING** **FEAT 18** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/6/SectionHeader/41` | 0.664093 | **EXPERT WITCHWARPER SPELLCASTING** **FEAT 12** |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/41` | 0.560635 | **Prerequisites** Basic Mystic Spellcasting |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/51` | 0.533925 | **Prerequisites** Expert Mystic Spellcasting; legendary in  connection skill |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/6/SectionHeader/46` | 0.513848 | **MASTER WITCHWARPER SPELLCASTING** **FEAT 18** |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/28` | 0.506196 | **GUN EXPERT** **FEAT 12** |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/46` | 0.501922 | **Prerequisites** Basic Mystic Spellcasting; master in  connection skill |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/6/SectionHeader/26` | 0.492204 | **BASIC WITCHWARPER SPELLCASTING** **FEAT 4** |

### Query 108
- Text: Summarize **ARCHETYPE**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/45']
- Expected found: `True`
- Expected rank: `26`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/27', 'PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/21', 'PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/16']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/21` | 0.970267 | **ARCHETYPE** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/16` | 0.970267 | **ARCHETYPE** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/27` | 0.970267 | **ARCHETYPE** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/12` | 0.928267 | **ARCHETYPE** |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/18` | 0.928267 | **ARCHETYPE** |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/23` | 0.928267 | **ARCHETYPE** |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/32` | 0.928267 | **ARCHETYPE** |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/19` | 0.928267 | **ARCHETYPE** |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/14` | 0.928267 | **ARCHETYPE** |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/11` | 0.928267 | **ARCHETYPE** |

### Query 109
- Text: What are the requirements for **Prerequisites** Basic Mystic Spellcasting; master in  connection skill?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/2/Text/46']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/2/Text/46', 'PZO22001 Starfinder Player Core 174-181::/page/2/Text/51', 'PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/41']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/46` | 0.970999 | **Prerequisites** Basic Mystic Spellcasting; master in  connection skill |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/51` | 0.867632 | **Prerequisites** Expert Mystic Spellcasting; legendary in  connection skill |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/41` | 0.830698 | **Prerequisites** Basic Mystic Spellcasting |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/30` | 0.673100 | **Prerequisites** Basic Mysticism |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/21` | 0.598016 | You gain the basic spellcasting benefits (page 174). Each time  you gain a spell slot of a new rank from the mystic archetype,  add a spell of the appropriate spell rank to your repertoire: a  common |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/39` | 0.591677 | **Prerequisites** Basic Witchwarper Spellcasting |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/10` | 0.587288 | You cast spells like a mystic and gain the Cast a Spell  activity. You gain a spell repertoire with two common cantrips  from the spell list granted by your connection, from the spells  granted by you |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/9` | 0.583474 | Choose a connection (see page 119). You become trained in  the connection's skill or, if you were already trained, you  become trained in a skill of your choice. You don't gain any  other abilities fr |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/44` | 0.581508 | **Prerequisites** Basic Witchwarper Spellcasting; master in Arcana  or Occultism, depending on paradox |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/20` | 0.577392 | **Prerequisites** Mystic Dedication |

### Query 110
- Text: What is the rule about You gain the expert spellcasting benefits (page 174).?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/2/Text/47']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/6/Text/45', 'PZO22001 Starfinder Player Core 174-181::/page/2/Text/47', 'PZO22001 Starfinder Player Core 174-181::/page/6/Text/50']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/45` | 0.940728 | You gain the expert spellcasting benefits (page 174). |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/47` | 0.940728 | You gain the expert spellcasting benefits (page 174). |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/50` | 0.891640 | You gain the master spellcasting benefits (page 174). |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/52` | 0.849640 | You gain the master spellcasting benefits (page 174). |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/21` | 0.648321 | You gain the basic spellcasting benefits (page 174). Each time  you gain a spell slot of a new rank from the mystic archetype,  add a spell of the appropriate spell rank to your repertoire: a  common |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/18` | 0.620033 | **Expert Spellcasting Feat:** Typically taken at 12th level,  these feats make you an expert in spell attack modifiers  and spell DCs and grant you a 4th-rank spell slot. If you  have a spell repertoi |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/29` | 0.609967 | You gain the basic spellcasting benefits (page 174). Each time  you gain a spell slot of a new rank from the witchwarper  archetype, add a spell of the appropriate spell rank to your  repertoire: a co |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/19` | 0.557844 | **Master Spellcasting Feat:** Usually found at 18th level, these  feats make you a master in spell attack modifiers and spell  DCs and grant you a 7th-rank spell slot. If you have a spell  repertoire, |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/16` | 0.522740 | Spellcasting archetypes always grant the ability to cast  cantrips in their dedication, and then they have a basic  spellcasting feat, an expert spellcasting feat, and a master  spellcasting feat. The |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/15` | 0.518515 | Some archetypes grant you a substantial degree of  spellcasting, albeit delayed compared to a character from a  spellcasting class. The spellcasting ability from a spellcasting  archetype also allows |

### Query 111
- Text: What are the requirements for **MASTER MYSTIC SPELLCASTING** **FEAT 18**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/48']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/48', 'PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/43', 'PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/17']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/48` | 0.924264 | **MASTER MYSTIC SPELLCASTING** **FEAT 18** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/43` | 0.771632 | **EXPERT MYSTIC SPELLCASTING** **FEAT 12** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/17` | 0.749615 | **BASIC MYSTIC SPELLCASTING** **FEAT 4** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/6/SectionHeader/46` | 0.690778 | **MASTER WITCHWARPER SPELLCASTING** **FEAT 18** |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/41` | 0.556493 | **Prerequisites** Basic Mystic Spellcasting |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/46` | 0.532870 | **Prerequisites** Basic Mystic Spellcasting; master in  connection skill |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/6/SectionHeader/41` | 0.503731 | **EXPERT WITCHWARPER SPELLCASTING** **FEAT 12** |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/51` | 0.500664 | **Prerequisites** Expert Mystic Spellcasting; legendary in  connection skill |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/6/SectionHeader/26` | 0.478725 | **BASIC WITCHWARPER SPELLCASTING** **FEAT 4** |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/19` | 0.464185 | **Master Spellcasting Feat:** Usually found at 18th level, these  feats make you a master in spell attack modifiers and spell  DCs and grant you a 7th-rank spell slot. If you have a spell  repertoire, |

### Query 112
- Text: Summarize **ARCHETYPE**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/50']
- Expected found: `True`
- Expected rank: `25`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/27', 'PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/21', 'PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/16']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/21` | 0.970267 | **ARCHETYPE** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/16` | 0.970267 | **ARCHETYPE** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/27` | 0.970267 | **ARCHETYPE** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/12` | 0.928267 | **ARCHETYPE** |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/18` | 0.928267 | **ARCHETYPE** |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/23` | 0.928267 | **ARCHETYPE** |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/32` | 0.928267 | **ARCHETYPE** |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/19` | 0.928267 | **ARCHETYPE** |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/14` | 0.928267 | **ARCHETYPE** |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/11` | 0.928267 | **ARCHETYPE** |

### Query 113
- Text: What are the requirements for **Prerequisites** Expert Mystic Spellcasting; legendary in  connection skill?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/2/Text/51']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/2/Text/51', 'PZO22001 Starfinder Player Core 174-181::/page/2/Text/46', 'PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/41']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/51` | 0.975060 | **Prerequisites** Expert Mystic Spellcasting; legendary in  connection skill |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/46` | 0.877963 | **Prerequisites** Basic Mystic Spellcasting; master in  connection skill |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/41` | 0.786903 | **Prerequisites** Basic Mystic Spellcasting |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/49` | 0.650880 | **Prerequisites** Expert Witchwarper Spellcasting; legendary in  Arcana or Occultism, depending on paradox |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/30` | 0.595812 | **Prerequisites** Basic Mysticism |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/10` | 0.581429 | You cast spells like a mystic and gain the Cast a Spell  activity. You gain a spell repertoire with two common cantrips  from the spell list granted by your connection, from the spells  granted by you |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/15` | 0.570439 | **Prerequisites** Mystic Dedication |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/25` | 0.570439 | **Prerequisites** Mystic Dedication |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/20` | 0.570439 | **Prerequisites** Mystic Dedication |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/36` | 0.570439 | **Prerequisites** Mystic Dedication |

### Query 114
- Text: What is the rule about You gain the master spellcasting benefits (page 174).?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/2/Text/52']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/6/Text/50', 'PZO22001 Starfinder Player Core 174-181::/page/2/Text/52', 'PZO22001 Starfinder Player Core 174-181::/page/2/Text/47']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/50` | 0.944775 | You gain the master spellcasting benefits (page 174). |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/52` | 0.944775 | You gain the master spellcasting benefits (page 174). |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/47` | 0.888435 | You gain the expert spellcasting benefits (page 174). |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/45` | 0.846435 | You gain the expert spellcasting benefits (page 174). |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/21` | 0.648616 | You gain the basic spellcasting benefits (page 174). Each time  you gain a spell slot of a new rank from the mystic archetype,  add a spell of the appropriate spell rank to your repertoire: a  common |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/29` | 0.617469 | You gain the basic spellcasting benefits (page 174). Each time  you gain a spell slot of a new rank from the witchwarper  archetype, add a spell of the appropriate spell rank to your  repertoire: a co |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/19` | 0.607969 | **Master Spellcasting Feat:** Usually found at 18th level, these  feats make you a master in spell attack modifiers and spell  DCs and grant you a 7th-rank spell slot. If you have a spell  repertoire, |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/18` | 0.543832 | **Expert Spellcasting Feat:** Typically taken at 12th level,  these feats make you an expert in spell attack modifiers  and spell DCs and grant you a 4th-rank spell slot. If you  have a spell repertoi |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/16` | 0.541771 | Spellcasting archetypes always grant the ability to cast  cantrips in their dedication, and then they have a basic  spellcasting feat, an expert spellcasting feat, and a master  spellcasting feat. The |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/15` | 0.514727 | Some archetypes grant you a substantial degree of  spellcasting, albeit delayed compared to a character from a  spellcasting class. The spellcasting ability from a spellcasting  archetype also allows |

### Query 115
- Text: Summarize OPERATIVE
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/1', 'PZO22001 Starfinder Player Core 174-181::/page/1/Text/48', 'PZO22001 Starfinder Player Core 174-181::/page/5/Text/52']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/1` | 0.899805 | OPERATIVE |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/48` | 0.829902 | **Operative ** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/52` | 0.829902 | **Operative ** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/7/Text/42` | 0.787902 | **Operative ** |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/57` | 0.564933 | **SPECIALIZED OPERATIVE** **FEAT 4** |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/27` | 0.537895 | **Prerequisites** Operative Dedication, Specialized Operative You gain the exploit of your chosen specialization. |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/3` | 0.485976 | MULTICLASS OPERATIVE  CHARACTERS |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/55` | 0.481247 | **Prerequisites** Operative Dedication |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/60` | 0.481247 | **Prerequisites** Operative Dedication |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/50` | 0.481247 | **Prerequisites** Operative Dedication |

### Query 116
- Text: What is the rule about You're a professional with crack aim and lethal instincts.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/3/Text/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/3/Text/2', 'PZO22001 Starfinder Player Core 174-181::/page/3/Text/32', 'PZO22001 Starfinder Player Core 174-181::/page/3/Text/31']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/2` | 0.947308 | You're a professional with crack aim and lethal instincts. |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/32` | 0.427953 | Your proficiency ranks for simple and martial guns increase to  expert. |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/31` | 0.426640 | **Prerequisites** Operative Dedication, expert in any kind of  weapon or unarmed attack |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/14` | 0.368389 | You become trained in light armor and medium armor. If  you already were trained in light armor and medium armor,  you gain training in heavy armor as well. Whenever you gain  a class feature that gra |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/13` | 0.366995 | You become trained in Intimidation. If you  were already trained in Intimidation, you  instead become trained in a skill of your choice.  Increase your maximum and encumbered Bulk limits  by 2. You be |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/22` | 0.357618 | You gain one operative feat. For the purpose of meeting its  prerequisites, your operative level is half your character level. |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/2` | 0.356964 | You're a stalwart shield who never stops blasting while  protecting your allies from danger, including from your own  terrifying destruction. |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/51` | 0.354841 | Your proficiency ranks for solar flare and solar weapon  increase to expert. |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/21` | 0.349899 | Some archetype feats in other books have the skill trait,  allowing you to take them in place of a skill feat rather than  a class feat. A skill feat still counts to satisfy the requirement  of the de |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/30` | 0.348094 | You gain the envoy directives class feature (see page  104), but do not gain the Lead by Example benefits  of the Get 'Em! envoy directive. You become trained in  Deception, Diplomacy, or Intimidation |

### Query 117
- Text: What is the rule about MULTICLASS OPERATIVE  CHARACTERS?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/3']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/3', 'PZO22001 Starfinder Player Core 174-181::/page/5/SectionHeader/3', 'PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/3']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/3` | 0.892630 | MULTICLASS OPERATIVE  CHARACTERS |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/5/SectionHeader/3` | 0.673473 | MULTICLASS SOLDIER  CHARACTERS |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/3` | 0.668137 | MULTICLASS MYSTIC  CHARACTERS |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/3` | 0.589828 | MULTICLASS ENVOY  CHARACTERS |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/6/SectionHeader/3` | 0.561059 | MULTICLASS WITCHWARPER  CHARACTERS |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/4/SectionHeader/3` | 0.548047 | MULTICLASS SOLARIAN  CHARACTERS |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/9` | 0.469685 | Most archetypes in this book have the multiclass trait.  These allow you to diversify your training into another  class's specialties. You can't select a multiclass archetype's  dedication feat if you |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/22` | 0.397232 | You gain one operative feat. For the purpose of meeting its  prerequisites, your operative level is half your character level. |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/68` | 0.396460 | **INTRODUCTION** **ANCESTRIES & ** **BACKGROUNDS** **CLASSES** **Envoy** **Mystic** **Operative ** **Solarian** **Soldier** **Witchwarper** |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/1` | 0.388864 | OPERATIVE |

### Query 118
- Text: What is the rule about The operative archetype allows you to deal high damage to  a single target and select class feats and exploits that add to  your offensive options in combat.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/3/Text/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/3/Text/4', 'PZO22001 Starfinder Player Core 174-181::/page/3/Text/16', 'PZO22001 Starfinder Player Core 174-181::/page/0/Text/21']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/4` | 0.946665 | The operative archetype allows you to deal high damage to  a single target and select class feats and exploits that add to  your offensive options in combat. |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/16` | 0.701435 | class feat you have. As you continue selecting operative  archetype class feats, you continue to gain additional Hit Points  in this way. |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/21` | 0.648737 | Some archetype feats in other books have the skill trait,  allowing you to take them in place of a skill feat rather than  a class feat. A skill feat still counts to satisfy the requirement  of the de |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/66` | 0.576738 | You gain 3 additional Hit Points for each operative archetype |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/9` | 0.574367 | Most archetypes in this book have the multiclass trait.  These allow you to diversify your training into another  class's specialties. You can't select a multiclass archetype's  dedication feat if you |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/13` | 0.568944 | Sometimes an archetype feat lets you select another feat,  such as a class feat of a lower level. You must always meet  any prerequisites of the feat you gain in this way. These  always count as only |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/22` | 0.568685 | You gain one operative feat. For the purpose of meeting its  prerequisites, your operative level is half your character level. |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/23` | 0.562566 | **Special** You can select this feat more than once. Each time you  do, you gain another operative feat. |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/5` | 0.550725 | An archetype feat is subject to any restrictions on the class  feat it replaces. For example, if you had an ability at 6th level  that granted you a bonus class feat, but that class feat had to  be 4t |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/11` | 0.539102 | Some archetypes include a list of "Additional Feats" that  appear in other sources. The list includes each feat's level,  which might be different than normal when gained from the  archetype. You can |

### Query 119
- Text: Summarize Envoy operatives direct allies while lining up perfect shots.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/3/ListItem/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/3/ListItem/5', 'PZO22001 Starfinder Player Core 174-181::/page/5/ListItem/5', 'PZO22001 Starfinder Player Core 174-181::/page/1/ListItem/6']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/3/ListItem/5` | 1.034753 | Envoy operatives direct allies while lining up perfect shots. |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/5/ListItem/5` | 0.676266 | Envoy soldiers are natural tacticians who use directives to  position enemies and allies to optimize their area attacks. |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/1/ListItem/6` | 0.617588 | Operative envoys become incredibly precise killing  machines that can combine Aim with abilities like Get  'em! and Distant Feint. Ghost operatives also appreciate  extra feats that use Deception. |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/4/ListItem/5` | 0.574358 | Envoy solarians can rush into close quarters to  properly assess an enemy's abilities and positioning  when determining what directives to use. |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/4` | 0.549006 | The envoy archetype allows you to take on a leadership role  by giving out directives that can support allies or hinder  enemies. |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/1/ListItem/8` | 0.541331 | Soldier envoys make natural commanders who can  use their defensive capabilities to keep the bonuses  of their directive's active against powerful enemies  while clearing out weaker foes with area fir |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/1/ListItem/5` | 0.540225 | Mystic envoys can choose between using their magic  or directives to empower their allies, widening the  breadth of options available to them. |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/35` | 0.505439 | You gain a 1st- or 2nd-level envoy feat of your choice. |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/14` | 0.462017 | You gain one envoy feat. For the purpose of meeting its  prerequisites, your envoy level is equal to half your character  level. |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/34` | 0.453208 | **Prerequisites** Envoy Dedication |

### Query 120
- Text: What is the rule about Mystic operatives might run out of spells, but they won't  run out of shells.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/3/ListItem/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/3/ListItem/6', 'PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/41', 'PZO22001 Starfinder Player Core 174-181::/page/2/Text/42']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/3/ListItem/6` | 0.952599 | Mystic operatives might run out of spells, but they won't  run out of shells. |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/41` | 0.521712 | **Prerequisites** Basic Mystic Spellcasting |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/42` | 0.511353 | Increase the number of spells in your repertoire and number  of spell slots you gain from mystic archetype feats by 1 for  each spell rank other than your two highest mystic spell slots. |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/31` | 0.467739 | You gain one mystic feat. For the purpose of meeting its  prerequisites, your mystic level is half your character level. |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/30` | 0.442155 | **Prerequisites** Basic Mysticism |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/26` | 0.434407 | You gain a 1st- or 2nd-level mystic feat. |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/32` | 0.427884 | **Special** You can select this feat more than once. Each time  you do, you gain another mystic feat. |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/20` | 0.413358 | **Prerequisites** Mystic Dedication |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/25` | 0.413358 | **Prerequisites** Mystic Dedication |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/36` | 0.413358 | **Prerequisites** Mystic Dedication |

### Query 121
- Text: Summarize Solarian operatives can Aim their solar flare and enhance  their cycle combos with operative exploits.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/3/ListItem/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/3/ListItem/7', 'PZO22001 Starfinder Player Core 174-181::/page/4/ListItem/7', 'PZO22001 Starfinder Player Core 174-181::/page/4/ListItem/8']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/3/ListItem/7` | 1.040021 | Solarian operatives can Aim their solar flare and enhance  their cycle combos with operative exploits. |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/4/ListItem/7` | 0.697240 | Operative solarians might not be able to use their  manifestations with most of their class features, but  close quarters operatives can take advantage of the  solarian's high mobility and gravity def |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/4/ListItem/8` | 0.656532 | Soldier solarians with the close quarters fighting style  can use their solar weapon to dispatch multiple foes at  once, while using solar flare as a potent ranged option. |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/4` | 0.564517 | The solarian archetype allows characters to wield powerful  solar weapons and engage in melee combat. |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/51` | 0.561173 | Your proficiency ranks for solar flare and solar weapon  increase to expert. |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/5/ListItem/8` | 0.560388 | Solarian soldiers can make use of Whirling Swipe to  damage multiple enemies at once with their solar  weapon. |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/4/ListItem/6` | 0.542657 | Mystic solarians can augment themselves with  powerful spells and heal themselves while confronting  power enemies on the frontline. |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/41` | 0.517149 | You can create and maintain a solar flare (page 140), but  do not add your Strength modifier to damage rolls with  your solar flare or any additional benefits based on your  attunement. |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/36` | 0.513878 | **Special** You can select this feat more than once. Each  time you do, you gain another solarian feat. |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/50` | 0.507911 | **Prerequisites** Solarian Dedication, expert in any kind of  weapon or unarmed attack |

### Query 122
- Text: What are the requirements for **OPERATIVE DEDICATION** **FEAT 2**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/3/Text/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/3/Text/10', 'PZO22001 Starfinder Player Core 174-181::/page/3/Text/60', 'PZO22001 Starfinder Player Core 174-181::/page/3/Text/50']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/10` | 0.905456 | **OPERATIVE DEDICATION** **FEAT 2** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/50` | 0.768099 | **Prerequisites** Operative Dedication |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/60` | 0.768099 | **Prerequisites** Operative Dedication |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/55` | 0.726099 | **Prerequisites** Operative Dedication |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/27` | 0.612639 | **ENVOY DEDICATION** **FEAT 2** |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/5` | 0.605353 | **MYSTIC DEDICATION** **FEAT 2** |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/5/SectionHeader/10` | 0.603995 | **SOLDIER DEDICATION** **FEAT 2** |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/36` | 0.592196 | **Prerequisites** Operative Dedication, expert in Perception |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/27` | 0.575264 | **Prerequisites** Operative Dedication, Specialized Operative You gain the exploit of your chosen specialization. |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/4/SectionHeader/10` | 0.559442 | **SOLARIAN DEDICATION** **FEAT 2** |

### Query 123
- Text: Summarize **ARCHETYPE** **DEDICATION** **MULTICLASS**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/3/Text/12']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/3/Text/12', 'PZO22001 Starfinder Player Core 174-181::/page/6/SectionHeader/7', 'PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/7']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/7` | 1.016945 | **ARCHETYPE** **DEDICATION** **MULTICLASS** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/6/SectionHeader/7` | 1.016945 | **ARCHETYPE** **DEDICATION** **MULTICLASS** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/12` | 1.016945 | **ARCHETYPE** **DEDICATION** **MULTICLASS** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/28` | 0.974945 | **ARCHETYPE** **DEDICATION** **MULTICLASS** |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/7/Text/5` | 0.974945 | **ARCHETYPE** **DEDICATION** **MULTICLASS** |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/5/SectionHeader/11` | 0.974945 | **ARCHETYPE** **DEDICATION** **MULTICLASS** |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/12` | 0.974945 | **ARCHETYPE** **DEDICATION** **MULTICLASS** |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/0/SectionHeader/8` | 0.592590 | Multiclass Dedications |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/30` | 0.584352 | **ARCHETYPE** |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/5/SectionHeader/27` | 0.584352 | **ARCHETYPE** |

### Query 124
- Text: What are the requirements for **Prerequisites** Dexterity +2?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/3/Text/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/3/Text/13', 'PZO22001 Starfinder Player Core 174-181::/page/6/Text/8', 'PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/8']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/13` | 0.932751 | **Prerequisites** Dexterity +2 |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/8` | 0.675416 | **Prerequisites** Intelligence +2 |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/8` | 0.599395 | **Prerequisites** Wisdom +2 |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/12` | 0.556345 | **Prerequisites** Constitution +2 |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/29` | 0.531633 | **Prerequisites** Charisma +2 |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/31` | 0.475658 | **Prerequisites** Operative Dedication, expert in any kind of  weapon or unarmed attack |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/60` | 0.474168 | **Prerequisites** Operative Dedication |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/55` | 0.474168 | **Prerequisites** Operative Dedication |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/50` | 0.474168 | **Prerequisites** Operative Dedication |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/33` | 0.468209 | **Prerequisites** Basic Distortion |

### Query 125
- Text: What are the requirements for **ADVANCED GUNNER** **FEAT 6**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/17']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/17', 'PZO22001 Starfinder Player Core 174-181::/page/5/SectionHeader/25', 'PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/10']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/17` | 0.899696 | **ADVANCED GUNNER** **FEAT 6** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/5/SectionHeader/25` | 0.731119 | **ADVANCED SOLDIER TRAINING** **FEAT 6** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/10` | 0.676818 | **ADVANCED LEADERSHIP** **FEAT 6** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/6/SectionHeader/30` | 0.559403 | **ADVANCED DISTORTION** **FEAT 6** |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/48` | 0.553316 | **BASIC GUNNER** **FEAT 4** |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/36` | 0.530540 | **ADAPTIVE TALENT** **FEAT 6** |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/21` | 0.527131 | **Prerequisites** Basic Gunner |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/4/SectionHeader/31` | 0.512393 | **ADVANCED STELLAR ATTUNEMENT** **FEAT 6** |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/27` | 0.497653 | **ADVANCED MYSTICISM** **FEAT 6** |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/28` | 0.491461 | **GUN EXPERT** **FEAT 12** |

### Query 126
- Text: Summarize **ARCHETYPE**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/3/Text/20']
- Expected found: `True`
- Expected rank: `23`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/27', 'PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/21', 'PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/16']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/21` | 0.970267 | **ARCHETYPE** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/16` | 0.970267 | **ARCHETYPE** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/27` | 0.970267 | **ARCHETYPE** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/12` | 0.928267 | **ARCHETYPE** |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/18` | 0.928267 | **ARCHETYPE** |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/23` | 0.928267 | **ARCHETYPE** |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/32` | 0.928267 | **ARCHETYPE** |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/19` | 0.928267 | **ARCHETYPE** |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/14` | 0.928267 | **ARCHETYPE** |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/11` | 0.928267 | **ARCHETYPE** |

### Query 127
- Text: What are the requirements for **Prerequisites** Basic Gunner?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/3/Text/21']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/3/Text/21', 'PZO22001 Starfinder Player Core 174-181::/page/5/Text/28', 'PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/48']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/21` | 0.952921 | **Prerequisites** Basic Gunner |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/28` | 0.740150 | **Prerequisites** Basic Soldier Training |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/48` | 0.626093 | **BASIC GUNNER** **FEAT 4** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/13` | 0.565269 | **Prerequisites** Basic Leadership |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/30` | 0.483837 | **Prerequisites** Basic Mysticism |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/33` | 0.483109 | **Prerequisites** Basic Distortion |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/31` | 0.483033 | **Prerequisites** Operative Dedication, expert in any kind of  weapon or unarmed attack |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/34` | 0.463193 | **Prerequisites** Basic Stellar Attunement |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/5/SectionHeader/15` | 0.463081 | **BASIC SOLDIER TRAINING** **FEAT 4** |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/18` | 0.457551 | **Prerequisites** Soldier Dedication |

### Query 128
- Text: What are the requirements for **OPERATIVE EXPLOIT** **FEAT 8**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/24']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/24', 'PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/16', 'PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/57']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/24` | 0.910502 | **OPERATIVE EXPLOIT** **FEAT 8** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/16` | 0.596978 | **REALLY GET EM!** **FEAT 8** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/57` | 0.564396 | **SPECIALIZED OPERATIVE** **FEAT 4** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/38` | 0.499656 | **EXPANDED CONNECTION** **FEAT 8** |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/62` | 0.494868 | **OPERATIVE RESILIENCY** **FEAT 4** |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/10` | 0.468437 | **OPERATIVE DEDICATION** **FEAT 2** |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/27` | 0.465667 | **Prerequisites** Operative Dedication, Specialized Operative You gain the exploit of your chosen specialization. |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/22` | 0.460547 | You gain one operative feat. For the purpose of meeting its  prerequisites, your operative level is half your character level. |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/51` | 0.448089 | You gain a 1st- or 2nd-level operative feat. |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/1` | 0.443910 | OPERATIVE |

### Query 129
- Text: Summarize **ARCHETYPE**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/3/Text/26']
- Expected found: `True`
- Expected rank: `24`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/27', 'PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/21', 'PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/16']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/21` | 0.970267 | **ARCHETYPE** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/16` | 0.970267 | **ARCHETYPE** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/27` | 0.970267 | **ARCHETYPE** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/12` | 0.928267 | **ARCHETYPE** |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/18` | 0.928267 | **ARCHETYPE** |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/23` | 0.928267 | **ARCHETYPE** |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/32` | 0.928267 | **ARCHETYPE** |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/19` | 0.928267 | **ARCHETYPE** |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/14` | 0.928267 | **ARCHETYPE** |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/11` | 0.928267 | **ARCHETYPE** |

### Query 130
- Text: What are the requirements for **Prerequisites** Operative Dedication, Specialized Operative You gain the exploit of your chosen specialization.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/3/Text/27']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/3/Text/27', 'PZO22001 Starfinder Player Core 174-181::/page/3/Text/55', 'PZO22001 Starfinder Player Core 174-181::/page/3/Text/50']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/27` | 0.959117 | **Prerequisites** Operative Dedication, Specialized Operative You gain the exploit of your chosen specialization. |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/55` | 0.795636 | **Prerequisites** Operative Dedication |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/50` | 0.795636 | **Prerequisites** Operative Dedication |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/60` | 0.753636 | **Prerequisites** Operative Dedication |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/31` | 0.685232 | **Prerequisites** Operative Dedication, expert in any kind of  weapon or unarmed attack |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/36` | 0.647750 | **Prerequisites** Operative Dedication, expert in Perception |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/65` | 0.590738 | **Prerequisites** Operative Dedication, class granting no more Hit  Points per level than 6 + your Constitution |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/18` | 0.536764 | **Prerequisites** Soldier Dedication |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/34` | 0.536764 | **Prerequisites** Soldier Dedication |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/39` | 0.536764 | **Prerequisites** Soldier Dedication |

### Query 131
- Text: What are the requirements for **GUN EXPERT** **FEAT 12**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/28']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/28', 'PZO22001 Starfinder Player Core 174-181::/page/4/SectionHeader/47', 'PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/33']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/28` | 0.874559 | **GUN EXPERT** **FEAT 12** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/4/SectionHeader/47` | 0.592312 | **SOLAR MANIFESTATION EXPERT** **FEAT 12** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/33` | 0.571241 | **MASTER SPY** **FEAT 12** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/31` | 0.513459 | **Prerequisites** Operative Dedication, expert in any kind of  weapon or unarmed attack |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/32` | 0.494508 | Your proficiency ranks for simple and martial guns increase to  expert. |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/17` | 0.481951 | **ADVANCED GUNNER** **FEAT 6** |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/21` | 0.478315 | **Prerequisites** Basic Gunner |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/6/SectionHeader/41` | 0.471754 | **EXPERT WITCHWARPER SPELLCASTING** **FEAT 12** |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/5/SectionHeader/41` | 0.465538 | **SOLDIER'S TOUGHNESS** **FEAT 12** |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/21` | 0.455968 | **LEADER'S CONFIDENCE** **FEAT 12** |

### Query 132
- Text: Summarize **ARCHETYPE**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/3/Text/30']
- Expected found: `True`
- Expected rank: `18`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/27', 'PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/21', 'PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/16']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/21` | 0.970267 | **ARCHETYPE** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/16` | 0.970267 | **ARCHETYPE** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/27` | 0.970267 | **ARCHETYPE** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/12` | 0.928267 | **ARCHETYPE** |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/18` | 0.928267 | **ARCHETYPE** |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/23` | 0.928267 | **ARCHETYPE** |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/32` | 0.928267 | **ARCHETYPE** |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/19` | 0.928267 | **ARCHETYPE** |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/14` | 0.928267 | **ARCHETYPE** |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/11` | 0.928267 | **ARCHETYPE** |

### Query 133
- Text: What are the requirements for **Prerequisites** Operative Dedication, expert in any kind of  weapon or unarmed attack?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/3/Text/31']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/3/Text/31', 'PZO22001 Starfinder Player Core 174-181::/page/3/Text/50', 'PZO22001 Starfinder Player Core 174-181::/page/3/Text/55']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/31` | 0.961452 | **Prerequisites** Operative Dedication, expert in any kind of  weapon or unarmed attack |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/50` | 0.764326 | **Prerequisites** Operative Dedication |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/55` | 0.764326 | **Prerequisites** Operative Dedication |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/60` | 0.722326 | **Prerequisites** Operative Dedication |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/50` | 0.721356 | **Prerequisites** Solarian Dedication, expert in any kind of  weapon or unarmed attack |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/27` | 0.687352 | **Prerequisites** Operative Dedication, Specialized Operative You gain the exploit of your chosen specialization. |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/36` | 0.635395 | **Prerequisites** Operative Dedication, expert in Perception |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/34` | 0.626496 | **Prerequisites** Soldier Dedication |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/39` | 0.626496 | **Prerequisites** Soldier Dedication |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/18` | 0.626496 | **Prerequisites** Soldier Dedication |

### Query 134
- Text: What are the requirements for **MASTER SPY** **FEAT 12**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/33']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/33', 'PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/28', 'PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/43']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/33` | 0.880161 | **MASTER SPY** **FEAT 12** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/28` | 0.606260 | **GUN EXPERT** **FEAT 12** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/43` | 0.529467 | **EXPERT MYSTIC SPELLCASTING** **FEAT 12** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/4/SectionHeader/47` | 0.469367 | **SOLAR MANIFESTATION EXPERT** **FEAT 12** |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/21` | 0.465281 | **LEADER'S CONFIDENCE** **FEAT 12** |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/6/SectionHeader/41` | 0.438318 | **EXPERT WITCHWARPER SPELLCASTING** **FEAT 12** |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/48` | 0.430664 | **MASTER MYSTIC SPELLCASTING** **FEAT 18** |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/8` | 0.413900 | **Prerequisites** Intelligence +2 |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/5/SectionHeader/41` | 0.412065 | **SOLDIER'S TOUGHNESS** **FEAT 12** |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/31` | 0.397922 | **Prerequisites** Operative Dedication, expert in any kind of  weapon or unarmed attack |

### Query 135
- Text: Summarize **ARCHETYPE**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/3/Text/35']
- Expected found: `True`
- Expected rank: `17`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/27', 'PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/21', 'PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/16']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/21` | 0.970267 | **ARCHETYPE** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/16` | 0.970267 | **ARCHETYPE** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/27` | 0.970267 | **ARCHETYPE** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/12` | 0.928267 | **ARCHETYPE** |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/18` | 0.928267 | **ARCHETYPE** |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/23` | 0.928267 | **ARCHETYPE** |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/32` | 0.928267 | **ARCHETYPE** |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/19` | 0.928267 | **ARCHETYPE** |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/14` | 0.928267 | **ARCHETYPE** |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/11` | 0.928267 | **ARCHETYPE** |

### Query 136
- Text: What are the requirements for **Prerequisites** Operative Dedication, expert in Perception?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/3/Text/36']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/3/Text/36', 'PZO22001 Starfinder Player Core 174-181::/page/3/Text/50', 'PZO22001 Starfinder Player Core 174-181::/page/3/Text/60']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/36` | 0.963749 | **Prerequisites** Operative Dedication, expert in Perception |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/60` | 0.769707 | **Prerequisites** Operative Dedication |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/50` | 0.769707 | **Prerequisites** Operative Dedication |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/55` | 0.727707 | **Prerequisites** Operative Dedication |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/27` | 0.642127 | **Prerequisites** Operative Dedication, Specialized Operative You gain the exploit of your chosen specialization. |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/31` | 0.637999 | **Prerequisites** Operative Dedication, expert in any kind of  weapon or unarmed attack |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/39` | 0.511517 | **Prerequisites** Soldier Dedication |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/34` | 0.511517 | **Prerequisites** Soldier Dedication |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/18` | 0.511517 | **Prerequisites** Soldier Dedication |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/10` | 0.504614 | **OPERATIVE DEDICATION** **FEAT 2** |

### Query 137
- Text: Summarize **Archetypes**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/38']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/5/Text/56', 'PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/38', 'PZO22001 Starfinder Player Core 174-181::/page/1/Text/52']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/56` | 0.973323 | **Archetypes** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/38` | 0.973323 | **Archetypes** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/52` | 0.973323 | **Archetypes** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/7/Text/46` | 0.931323 | **Archetypes** |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/23` | 0.799429 | **ARCHETYPE** |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/21` | 0.799429 | **ARCHETYPE** |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/33` | 0.799429 | **ARCHETYPE** |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/40` | 0.799429 | **ARCHETYPE** |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/16` | 0.799429 | **ARCHETYPE** |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/50` | 0.799429 | **ARCHETYPE** |

### Query 138
- Text: Summarize **EQUIPMENT**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/3/Text/41']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/1/Text/55', 'PZO22001 Starfinder Player Core 174-181::/page/5/Text/60', 'PZO22001 Starfinder Player Core 174-181::/page/3/Text/41']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/55` | 0.944726 | **EQUIPMENT** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/60` | 0.944726 | **EQUIPMENT** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/41` | 0.944726 | **EQUIPMENT** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/7/Text/49` | 0.902726 | **EQUIPMENT** |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/11` | 0.429872 | **ARCHETYPE** |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/16` | 0.429872 | **ARCHETYPE** |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/38` | 0.429872 | **ARCHETYPE** |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/21` | 0.429872 | **ARCHETYPE** |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/33` | 0.429872 | **ARCHETYPE** |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/18` | 0.429872 | **ARCHETYPE** |

### Query 139
- Text: Summarize **PLAYING THE ** **GAME**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/3/Text/43']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/1/Text/57', 'PZO22001 Starfinder Player Core 174-181::/page/3/Text/43', 'PZO22001 Starfinder Player Core 174-181::/page/5/Text/62']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/57` | 0.965000 | **PLAYING THE ** **GAME** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/43` | 0.965000 | **PLAYING THE ** **GAME** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/62` | 0.965000 | **PLAYING THE ** **GAME** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/7/Text/51` | 0.923000 | **PLAYING THE ** **GAME** |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/47` | 0.418586 | **INTRODUCTION** |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/43` | 0.418586 | **INTRODUCTION** |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/66` | 0.388648 | **CHARACTER ** |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/60` | 0.356979 | **CHARACTER ** **SHEET** |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/47` | 0.356979 | **CHARACTER ** **SHEET** |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/7/Text/55` | 0.356979 | **CHARACTER ** **SHEET** |

### Query 140
- Text: What are the requirements for **BASIC GUNNER** **FEAT 4**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/48']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/48', 'PZO22001 Starfinder Player Core 174-181::/page/3/Text/21', 'PZO22001 Starfinder Player Core 174-181::/page/5/SectionHeader/15']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/48` | 0.903971 | **BASIC GUNNER** **FEAT 4** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/21` | 0.745324 | **Prerequisites** Basic Gunner |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/5/SectionHeader/15` | 0.698760 | **BASIC SOLDIER TRAINING** **FEAT 4** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/31` | 0.614662 | **BASIC LEADERSHIP** **FEAT 4** |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/17` | 0.549158 | **ADVANCED GUNNER** **FEAT 6** |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/6/SectionHeader/11` | 0.543040 | **BASIC DISTORTION** **FEAT 4** |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/6/SectionHeader/16` | 0.535341 | **BASIC QUANTUM FIELD** **FEAT 4** |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/28` | 0.519072 | **Prerequisites** Basic Soldier Training |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/6/SectionHeader/21` | 0.508271 | **BASIC WARP SPELL** **FEAT 4** |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/57` | 0.497906 | **SPECIALIZED OPERATIVE** **FEAT 4** |

### Query 141
- Text: What are the requirements for **Prerequisites** Operative Dedication?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/3/Text/50']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/3/Text/55', 'PZO22001 Starfinder Player Core 174-181::/page/3/Text/50', 'PZO22001 Starfinder Player Core 174-181::/page/3/Text/60']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/55` | 0.954185 | **Prerequisites** Operative Dedication |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/50` | 0.954185 | **Prerequisites** Operative Dedication |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/60` | 0.954185 | **Prerequisites** Operative Dedication |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/27` | 0.726802 | **Prerequisites** Operative Dedication, Specialized Operative You gain the exploit of your chosen specialization. |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/36` | 0.701982 | **Prerequisites** Operative Dedication, expert in Perception |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/31` | 0.688052 | **Prerequisites** Operative Dedication, expert in any kind of  weapon or unarmed attack |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/18` | 0.651443 | **Prerequisites** Soldier Dedication |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/34` | 0.651443 | **Prerequisites** Soldier Dedication |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/39` | 0.651443 | **Prerequisites** Soldier Dedication |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/65` | 0.622450 | **Prerequisites** Operative Dedication, class granting no more Hit  Points per level than 6 + your Constitution |

### Query 142
- Text: What are the requirements for **SHARPSHOOTER** **FEAT 4**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/52']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/52', 'PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/9', 'PZO22001 Starfinder Player Core 174-181::/page/6/SectionHeader/21']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/52` | 0.907818 | **SHARPSHOOTER** **FEAT 4** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/9` | 0.524978 | **MISSION BRIEFING** **FEAT 4** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/6/SectionHeader/21` | 0.519335 | **BASIC WARP SPELL** **FEAT 4** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/57` | 0.473380 | **SPECIALIZED OPERATIVE** **FEAT 4** |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/6/SectionHeader/26` | 0.440903 | **BASIC WITCHWARPER SPELLCASTING** **FEAT 4** |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/12` | 0.436720 | **VITALITY NETWORK** **FEAT 4** |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/31` | 0.436162 | **BASIC LEADERSHIP** **FEAT 4** |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/4/SectionHeader/21` | 0.433851 | **SOLAR WEAPON CUSTOMIZATION** **FEAT 4** |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/48` | 0.433179 | **BASIC GUNNER** **FEAT 4** |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/5/SectionHeader/15` | 0.433013 | **BASIC SOLDIER TRAINING** **FEAT 4** |

### Query 143
- Text: What are the requirements for **Prerequisites** Operative Dedication?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/3/Text/55']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/3/Text/55', 'PZO22001 Starfinder Player Core 174-181::/page/3/Text/50', 'PZO22001 Starfinder Player Core 174-181::/page/3/Text/60']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/55` | 0.954185 | **Prerequisites** Operative Dedication |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/50` | 0.954185 | **Prerequisites** Operative Dedication |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/60` | 0.954185 | **Prerequisites** Operative Dedication |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/27` | 0.726802 | **Prerequisites** Operative Dedication, Specialized Operative You gain the exploit of your chosen specialization. |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/36` | 0.701982 | **Prerequisites** Operative Dedication, expert in Perception |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/31` | 0.688052 | **Prerequisites** Operative Dedication, expert in any kind of  weapon or unarmed attack |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/18` | 0.651443 | **Prerequisites** Soldier Dedication |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/34` | 0.651443 | **Prerequisites** Soldier Dedication |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/39` | 0.651443 | **Prerequisites** Soldier Dedication |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/65` | 0.622450 | **Prerequisites** Operative Dedication, class granting no more Hit  Points per level than 6 + your Constitution |

### Query 144
- Text: What are the requirements for **SPECIALIZED OPERATIVE** **FEAT 4**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/57']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/57', 'PZO22001 Starfinder Player Core 174-181::/page/3/Text/27', 'PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/9']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/57` | 0.908933 | **SPECIALIZED OPERATIVE** **FEAT 4** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/27` | 0.627475 | **Prerequisites** Operative Dedication, Specialized Operative You gain the exploit of your chosen specialization. |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/9` | 0.525324 | **MISSION BRIEFING** **FEAT 4** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/62` | 0.478178 | **OPERATIVE RESILIENCY** **FEAT 4** |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/31` | 0.477714 | **Prerequisites** Operative Dedication, expert in any kind of  weapon or unarmed attack |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/60` | 0.473897 | **Prerequisites** Operative Dedication |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/50` | 0.473897 | **Prerequisites** Operative Dedication |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/55` | 0.473897 | **Prerequisites** Operative Dedication |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/1` | 0.466446 | OPERATIVE |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/5/SectionHeader/15` | 0.466029 | **BASIC SOLDIER TRAINING** **FEAT 4** |

### Query 145
- Text: What are the requirements for **Prerequisites** Operative Dedication?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/3/Text/60']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/3/Text/55', 'PZO22001 Starfinder Player Core 174-181::/page/3/Text/50', 'PZO22001 Starfinder Player Core 174-181::/page/3/Text/60']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/55` | 0.954185 | **Prerequisites** Operative Dedication |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/50` | 0.954185 | **Prerequisites** Operative Dedication |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/60` | 0.954185 | **Prerequisites** Operative Dedication |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/27` | 0.726802 | **Prerequisites** Operative Dedication, Specialized Operative You gain the exploit of your chosen specialization. |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/36` | 0.701982 | **Prerequisites** Operative Dedication, expert in Perception |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/31` | 0.688052 | **Prerequisites** Operative Dedication, expert in any kind of  weapon or unarmed attack |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/18` | 0.651443 | **Prerequisites** Soldier Dedication |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/34` | 0.651443 | **Prerequisites** Soldier Dedication |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/39` | 0.651443 | **Prerequisites** Soldier Dedication |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/65` | 0.622450 | **Prerequisites** Operative Dedication, class granting no more Hit  Points per level than 6 + your Constitution |

### Query 146
- Text: What are the requirements for **OPERATIVE RESILIENCY** **FEAT 4**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/62']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/62', 'PZO22001 Starfinder Player Core 174-181::/page/5/SectionHeader/20', 'PZO22001 Starfinder Player Core 174-181::/page/4/SectionHeader/26']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/62` | 0.921512 | **OPERATIVE RESILIENCY** **FEAT 4** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/5/SectionHeader/20` | 0.706812 | **SOLDIER'S RESILIENCY** **FEAT 4** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/4/SectionHeader/26` | 0.629139 | **SOLARIAN'S RESILIENCY** **FEAT 4** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/57` | 0.550415 | **SPECIALIZED OPERATIVE** **FEAT 4** |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/24` | 0.492251 | **OPERATIVE EXPLOIT** **FEAT 8** |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/12` | 0.474661 | **VITALITY NETWORK** **FEAT 4** |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/10` | 0.474511 | **OPERATIVE DEDICATION** **FEAT 2** |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/31` | 0.462253 | **BASIC LEADERSHIP** **FEAT 4** |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/55` | 0.442249 | **Prerequisites** Operative Dedication |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/50` | 0.442249 | **Prerequisites** Operative Dedication |

### Query 147
- Text: What are the requirements for **Prerequisites** Operative Dedication, class granting no more Hit  Points per level than 6 + your Constitution?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/3/Text/65']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/3/Text/65', 'PZO22001 Starfinder Player Core 174-181::/page/5/Text/23', 'PZO22001 Starfinder Player Core 174-181::/page/4/Text/29']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/65` | 0.981754 | **Prerequisites** Operative Dedication, class granting no more Hit  Points per level than 6 + your Constitution |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/23` | 0.821466 | **Prerequisites** Soldier Dedication, class granting no more Hit  Points per level than 8 + your Constitution modifier |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/29` | 0.766696 | **Prerequisites** Solarian Dedication, class granting no more Hit  Points per level than 8 + your Constitution modifier |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/50` | 0.656139 | **Prerequisites** Operative Dedication |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/60` | 0.656139 | **Prerequisites** Operative Dedication |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/55` | 0.656139 | **Prerequisites** Operative Dedication |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/31` | 0.614694 | **Prerequisites** Operative Dedication, expert in any kind of  weapon or unarmed attack |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/27` | 0.603287 | **Prerequisites** Operative Dedication, Specialized Operative You gain the exploit of your chosen specialization. |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/66` | 0.548141 | You gain 3 additional Hit Points for each operative archetype |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/39` | 0.537061 | **Prerequisites** Soldier Dedication |

### Query 148
- Text: What are the requirements for **SOLARIAN DEDICATION** **FEAT 2**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/4/SectionHeader/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/4/SectionHeader/10', 'PZO22001 Starfinder Player Core 174-181::/page/4/Text/45', 'PZO22001 Starfinder Player Core 174-181::/page/4/Text/19']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/4/SectionHeader/10` | 0.911520 | **SOLARIAN DEDICATION** **FEAT 2** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/45` | 0.769157 | **Prerequisites** Solarian Dedication |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/19` | 0.769157 | **Prerequisites** Solarian Dedication |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/40` | 0.727157 | **Prerequisites** Solarian Dedication |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/24` | 0.727157 | **Prerequisites** Solarian Dedication |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/5/SectionHeader/10` | 0.638557 | **SOLDIER DEDICATION** **FEAT 2** |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/27` | 0.591618 | **ENVOY DEDICATION** **FEAT 2** |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/5` | 0.588923 | **MYSTIC DEDICATION** **FEAT 2** |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/50` | 0.588002 | **Prerequisites** Solarian Dedication, expert in any kind of  weapon or unarmed attack |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/4/SectionHeader/26` | 0.585137 | **SOLARIAN'S RESILIENCY** **FEAT 4** |

### Query 149
- Text: What are the requirements for **Prerequisites** Strength +2 You gain the stellar attunement class feature (page 140), but?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/4/Text/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 174-181::/page/4/Text/13', 'PZO22001 Starfinder Player Core 174-181::/page/4/Text/34', 'PZO22001 Starfinder Player Core 174-181::/page/4/Text/41']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/13` | 0.983181 | **Prerequisites** Strength +2 You gain the stellar attunement class feature (page 140), but |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/34` | 0.680573 | **Prerequisites** Basic Stellar Attunement |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/41` | 0.574120 | You can create and maintain a solar flare (page 140), but  do not add your Strength modifier to damage rolls with  your solar flare or any additional benefits based on your  attunement. |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/15` | 0.508955 | You can manifest a solar weapon (page 141). Your weapon has  the attuned and solarian traits, but you can't select additional  traits and it gains no benefits based on your attunement. You  gain the R |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/46` | 0.489576 | You gain the Nimbus Surge reaction (page 141), but do not  gain any additional benefits based on your attunement. |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/35` | 0.489179 | You gain the suppressing fire class feature (page 152). |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/12` | 0.482392 | **Prerequisites** Constitution +2 |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/8` | 0.478714 | **Prerequisites** Intelligence +2 |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/25` | 0.466625 | You gain the leader's confidence class feature (see page  107). |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/40` | 0.461007 | You gain the primary target class feature (page 152). |
