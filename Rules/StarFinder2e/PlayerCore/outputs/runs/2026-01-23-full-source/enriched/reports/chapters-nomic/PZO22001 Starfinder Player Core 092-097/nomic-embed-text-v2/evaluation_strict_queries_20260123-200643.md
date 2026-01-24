# RulesLawyer Evaluation Report: nomic-embed-text-v2

## Summary
- Run ID: `None`
- Ruleset ID: `None`
- Document ID: `None`
- Chunk source: `enriched`
- Chunk count: `305`
- Query count: `103`
- Evaluated queries: `103`
- Coverage: `1.0000`
- MRR: `0.8600`
- hit@1: `0.7573`
- hit@3: `0.9806`
- hit@5: `0.9903`
- hit@10: `1.0000`
- Embeddings reused: `False`
- Graph boost: `0.05` (depth=2, top_k=50, source=top, seed_top_n=3, same_kind_only=False, decay=0.4)

## Timings (ms)
- Embedding (chunks): `4417`
- Embedding (queries): `2042`
- Evaluation (strict): `12`
- Evaluation (expanded): `0`
- Total: `10803`

### Timing Estimates (ms)
- Evaluation (strict): `10`
- Evaluation (expanded): `None`
- Total: `6469`

## Query Details
### Query 0
- Text: What is the rule about Your character's abilities don't spring into existence the moment they take up the adventuring life. Their background—the role they had before they became an adventurer—also provides a number of  abilities. Most backgrounds are common and can be selected by any character, but some adventurers  come from more distinctive roots and might have uncommon or rare backgrounds. The particular  histories behind these rare backgrounds provide specialized benefits.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 092-097::/page/0/Text/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 092-097::/page/0/Text/1', 'PZO22001 Starfinder Player Core 092-097::/page/5/Text/5', 'PZO22001 Starfinder Player Core 092-097::/page/3/Text/2']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 092-097::/page/0/Text/1` | 1.014610 | Your character's abilities don't spring into existence the moment they take up the adventuring life. Their background—the role they had before they became an adventurer—also provides a number of  abil |
| 2 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/5` | 0.647351 | It's possible for your character to learn languages laterin their  adventuring career. Selecting the Multilingual feat, for example,  grants a character two new languages chosen from those listed  bel |
| 3 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/2` | 0.629666 | You've spent years performing  arduous physical labor. It  was a difficult life, but you  survived. You may have  embraced adventuring  as an easier method to  make your way in the  world, or you migh |
| 4 | `PZO22001 Starfinder Player Core 092-097::/page/0/Text/3` | 0.575647 | At 1st level, when you create your character, you gain a  background of your choice. This decision is permanent;  you can't change it at later levels. Each background listed  here grants two boosts, u |
| 5 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/37` | 0.542227 | You solved crimes as a police inspector or took clandestine  jobs for various clients as a private investigator. You might  have become an adventurer as part of your next big mystery,  but it's equall |
| 6 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/22` | 0.538698 | The thrill of the win drew you into games of chance.  This might have been a lucrative pastime that paled in  comparison to the real risks of adventuring, or you might  have fallen on hard times due t |
| 7 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/7` | 0.530505 | You earned a living wrenching precious minerals from the  lightless depths. Adventuring might have seemed lucrative or  glamorous compared to this backbreaking labor—and if you  have to head back unde |
| 8 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/21` | 0.519486 | You are incredibly knowledgeable, skilled, and perhaps even  trained to teach children and adults about the world and  its wonders. From books to classes, you're committed to  imparting knowledge to a |
| 9 | `PZO22001 Starfinder Player Core 092-097::/page/0/Text/7` | 0.512501 | Your art is your greatest passion, whatever form it takes.  Adventuring might help you find inspiration for your  creations, or simply be a way to survive until you become a  world-famous artist. |
| 10 | `PZO22001 Starfinder Player Core 092-097::/page/0/Text/4` | 0.492702 | Lore skills represent deep knowledge of a specific subject  and are described on page 200. If a Lore skill involves a choice  (for instance, a choice of metaphysical topics), explain your  preference |

### Query 1
- Text: What is the rule about At 1st level, when you create your character, you gain a  background of your choice. This decision is permanent;  you can't change it at later levels. Each background listed  here grants two boosts, usually a skill feat, and the trained  proficiency rank in two skills, one of which is a Lore skill.  If you gain the trained proficiency rank in a skill from your  background and would then gain the trained proficiency  rank in the same skill from your class at 1st level, you instead  become trained in another skill of your choice.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 092-097::/page/0/Text/3']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 092-097::/page/0/Text/3', 'PZO22001 Starfinder Player Core 092-097::/page/0/Text/9', 'PZO22001 Starfinder Player Core 092-097::/page/3/Text/22']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 092-097::/page/0/Text/3` | 0.992802 | At 1st level, when you create your character, you gain a  background of your choice. This decision is permanent;  you can't change it at later levels. Each background listed  here grants two boosts, u |
| 2 | `PZO22001 Starfinder Player Core 092-097::/page/0/Text/9` | 0.643424 | You're trained in the Crafting skill and the Art Lore skill.  You gain the Specialty Crafting skill feat. |
| 3 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/22` | 0.619376 | You're trained in the deity's listed divine skill and gain the  Assurance feat with that skill. You are also trained in a Lore  skill related to your deity (Abadar Lore, for example). |
| 4 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/30` | 0.573814 | You're trained in the Crafting skill and a Lore skill related  to your field of research. You gain the Assurance skill feat  with that Lore skill. |
| 5 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/23` | 0.571895 | You're trained in your choice of either the Performance or  Society skill, as well as the Academia Lore skill. You gain the  Experienced Professional skill feat. |
| 6 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/26` | 0.556617 | You're trained in the Survival skill and a Lore skill related to  your former life. You gain the Dubious Knowledge skill feat. |
| 7 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/12` | 0.554213 | You're trained in the Occultism skill and a Lore skill  related to your choice of metaphysical topics. You gain the  Schooled in Secrets skill feat. |
| 8 | `PZO22001 Starfinder Player Core 092-097::/page/0/Text/4` | 0.546341 | Lore skills represent deep knowledge of a specific subject  and are described on page 200. If a Lore skill involves a choice  (for instance, a choice of metaphysical topics), explain your  preference |
| 9 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/9` | 0.541736 | You're trained in the Survival skill and the Mining  Lore skill. You gain the Terrain Expertise skill feat with  underground terrain. |
| 10 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/28` | 0.538528 | You're trained in the Crafting skill and the Augmentation or  Life Science Lore skill. You gain the Serum Crafting skill feat. |

### Query 2
- Text: What is the rule about Lore skills represent deep knowledge of a specific subject  and are described on page 200. If a Lore skill involves a choice  (for instance, a choice of metaphysical topics), explain your  preference to the GM, who has the final say on whether it's  acceptable or not. If you'd like some suggestions, the Common  Lore Subcategories sidebar on page 201 lists a number of Lore  skills that are suitable for most campaigns. Skill feats expand  the functions of your skills and appear in Chapter 5.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 092-097::/page/0/Text/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 092-097::/page/0/Text/4', 'PZO22001 Starfinder Player Core 092-097::/page/2/Text/12', 'PZO22001 Starfinder Player Core 092-097::/page/0/Text/3']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 092-097::/page/0/Text/4` | 1.004146 | Lore skills represent deep knowledge of a specific subject  and are described on page 200. If a Lore skill involves a choice  (for instance, a choice of metaphysical topics), explain your  preference |
| 2 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/12` | 0.636762 | You're trained in the Occultism skill and a Lore skill  related to your choice of metaphysical topics. You gain the  Schooled in Secrets skill feat. |
| 3 | `PZO22001 Starfinder Player Core 092-097::/page/0/Text/3` | 0.628881 | At 1st level, when you create your character, you gain a  background of your choice. This decision is permanent;  you can't change it at later levels. Each background listed  here grants two boosts, u |
| 4 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/22` | 0.545559 | You're trained in the deity's listed divine skill and gain the  Assurance feat with that skill. You are also trained in a Lore  skill related to your deity (Abadar Lore, for example). |
| 5 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/30` | 0.542261 | You're trained in the Crafting skill and a Lore skill related  to your field of research. You gain the Assurance skill feat  with that Lore skill. |
| 6 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/20` | 0.537957 | You're trained in the Society skill and a Lore skill related  to one city or region you've visited often. You gain the  Multilingual skill feat. |
| 7 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/23` | 0.534714 | You're trained in your choice of either the Performance or  Society skill, as well as the Academia Lore skill. You gain the  Experienced Professional skill feat. |
| 8 | `PZO22001 Starfinder Player Core 092-097::/page/0/Text/9` | 0.528443 | You're trained in the Crafting skill and the Art Lore skill.  You gain the Specialty Crafting skill feat. |
| 9 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/5` | 0.527135 | It's possible for your character to learn languages laterin their  adventuring career. Selecting the Multilingual feat, for example,  grants a character two new languages chosen from those listed  bel |
| 10 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/26` | 0.524528 | You're trained in the Survival skill and a Lore skill related to  your former life. You gain the Dubious Knowledge skill feat. |

### Query 3
- Text: What is the rule about **ARTIST** **BACKGROUND**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 092-097::/page/0/SectionHeader/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 092-097::/page/0/SectionHeader/6', 'PZO22001 Starfinder Player Core 092-097::/page/2/Text/1', 'PZO22001 Starfinder Player Core 092-097::/page/3/Text/27']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 092-097::/page/0/SectionHeader/6` | 0.841248 | **ARTIST** **BACKGROUND** |
| 2 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/1` | 0.641349 | **DISCIPLE** **BACKGROUND** |
| 3 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/27` | 0.609673 | **SCIENTIST** **BACKGROUND** |
| 4 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/23` | 0.565163 | **RECLUSE** **BACKGROUND** |
| 5 | `PZO22001 Starfinder Player Core 092-097::/page/2/SectionHeader/37` | 0.564360 | **ICON** **BACKGROUND** |
| 6 | `PZO22001 Starfinder Player Core 092-097::/page/0/SectionHeader/11` | 0.555831 | **ATHLETE** **BACKGROUND** |
| 7 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/34` | 0.539856 | **Backgrounds** |
| 8 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/57` | 0.539856 | **Backgrounds** |
| 9 | `PZO22001 Starfinder Player Core 092-097::/page/2/SectionHeader/5` | 0.538922 | **DOCTOR** **BACKGROUND** |
| 10 | `PZO22001 Starfinder Player Core 092-097::/page/1/SectionHeader/23` | 0.520460 | **COOK** **BACKGROUND** |

### Query 4
- Text: Summarize Your art is your greatest passion, whatever form it takes.  Adventuring might help you find inspiration for your  creations, or simply be a way to survive until you become a  world-famous artist.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 092-097::/page/0/Text/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 092-097::/page/0/Text/7', 'PZO22001 Starfinder Player Core 092-097::/page/3/Text/2', 'PZO22001 Starfinder Player Core 092-097::/page/2/Text/22']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 092-097::/page/0/Text/7` | 1.039659 | Your art is your greatest passion, whatever form it takes.  Adventuring might help you find inspiration for your  creations, or simply be a way to survive until you become a  world-famous artist. |
| 2 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/2` | 0.650889 | You've spent years performing  arduous physical labor. It  was a difficult life, but you  survived. You may have  embraced adventuring  as an easier method to  make your way in the  world, or you migh |
| 3 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/22` | 0.580392 | The thrill of the win drew you into games of chance.  This might have been a lucrative pastime that paled in  comparison to the real risks of adventuring, or you might  have fallen on hard times due t |
| 4 | `PZO22001 Starfinder Player Core 092-097::/page/0/Text/1` | 0.522391 | Your character's abilities don't spring into existence the moment they take up the adventuring life. Their background—the role they had before they became an adventurer—also provides a number of  abil |
| 5 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/21` | 0.513766 | You are incredibly knowledgeable, skilled, and perhaps even  trained to teach children and adults about the world and  its wonders. From books to classes, you're committed to  imparting knowledge to a |
| 6 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/7` | 0.497840 | You earned a living wrenching precious minerals from the  lightless depths. Adventuring might have seemed lucrative or  glamorous compared to this backbreaking labor—and if you  have to head back unde |
| 7 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/38` | 0.494969 | Gaming is more than just a hobby for you: it's your way of  life. Whether you're a professional player, game designer,  hobbyist influencer, or just a gamer who has mastered  every vidgame you can ins |
| 8 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/24` | 0.479149 | You grew up in the kitchens of a tavern or other dining  establishment and excelled there, becoming an exceptional  chef. Baking, cooking, a little brewing on the side—you've  spent lots of time out o |
| 9 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/38` | 0.474682 | Everybody wants their 15 minutes of fame, but for you, it's  somehow become a lifestyle. Whether by luck or dedication,  you're a star performer, celebrity, or popular influencer. Your  face, voice, a |
| 10 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/37` | 0.450053 | You solved crimes as a police inspector or took clandestine  jobs for various clients as a private investigator. You might  have become an adventurer as part of your next big mystery,  but it's equall |

### Query 5
- Text: What is the rule about Choose two attribute boosts. One must be to Dexterity or  Charisma, and one is a free attribute boost.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 092-097::/page/0/Text/8']
- Expected found: `True`
- Expected rank: `4`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 092-097::/page/1/Text/13', 'PZO22001 Starfinder Player Core 092-097::/page/1/Text/17', 'PZO22001 Starfinder Player Core 092-097::/page/2/Text/23']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/13` | 0.945158 | Choose two attribute boosts. One must be to Dexterity or  Charisma, and one is a free attribute boost. |
| 2 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/17` | 0.945158 | Choose two attribute boosts. One must be to Dexterity or  Charisma, and one is a free attribute boost. |
| 3 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/23` | 0.945158 | Choose two attribute boosts. One must be to Dexterity or  Charisma, and one is a free attribute boost. |
| 4 | `PZO22001 Starfinder Player Core 092-097::/page/0/Text/8` | 0.903158 | Choose two attribute boosts. One must be to Dexterity or  Charisma, and one is a free attribute boost. |
| 5 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/19` | 0.843785 | Choose two attribute boosts. One must be to Dexterity or  Wisdom, and one is a free attribute boost. |
| 6 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/3` | 0.843785 | Choose two attribute boosts. One must be to Dexterity or  Wisdom, and one is a free attribute boost. |
| 7 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/35` | 0.839064 | Choose two attribute boosts. One must be to Dexterity or  Intelligence, and one is a free attribute boost. |
| 8 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/7` | 0.839064 | Choose two attribute boosts. One must be to Dexterity or  Intelligence, and one is a free attribute boost. |
| 9 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/39` | 0.839064 | Choose two attribute boosts. One must be to Dexterity  or Intelligence, and one is a free attribute boost. |
| 10 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/11` | 0.827127 | Choose two attribute boosts. One must be to Strength or  Dexterity, and one is a free attribute boost. |

### Query 6
- Text: What is the rule about You're trained in the Crafting skill and the Art Lore skill.  You gain the Specialty Crafting skill feat.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 092-097::/page/0/Text/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 092-097::/page/0/Text/9', 'PZO22001 Starfinder Player Core 092-097::/page/2/Text/28', 'PZO22001 Starfinder Player Core 092-097::/page/3/Text/30']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 092-097::/page/0/Text/9` | 0.972752 | You're trained in the Crafting skill and the Art Lore skill.  You gain the Specialty Crafting skill feat. |
| 2 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/28` | 0.775097 | You're trained in the Crafting skill and the Augmentation or  Life Science Lore skill. You gain the Serum Crafting skill feat. |
| 3 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/30` | 0.759128 | You're trained in the Crafting skill and a Lore skill related  to your field of research. You gain the Assurance skill feat  with that Lore skill. |
| 4 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/35` | 0.704973 | You're trained in the Crafting skill and the Augmentation  Lore skill. You gain the Augmented Body feat. |
| 5 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/16` | 0.703062 | You're trained in the Crafting skill and the Physical  Science Lore skill. You gain the Electrical Engineer skill feat. |
| 6 | `PZO22001 Starfinder Player Core 092-097::/page/0/Text/3` | 0.658090 | At 1st level, when you create your character, you gain a  background of your choice. This decision is permanent;  you can't change it at later levels. Each background listed  here grants two boosts, u |
| 7 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/20` | 0.624542 | You're trained in the Survival skill and a Lore skill about a  specific settlement. You gain the Urban Survivalist skill feat. |
| 8 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/22` | 0.621129 | You're trained in the deity's listed divine skill and gain the  Assurance feat with that skill. You are also trained in a Lore  skill related to your deity (Abadar Lore, for example). |
| 9 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/4` | 0.606062 | You're trained in the deity's listed divine skill and a Lore  skill related to your deity (Abadar Lore, for example). You  gain the Religious Talisman skill feat even if you do not meet  the feat's pr |
| 10 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/23` | 0.603209 | You're trained in your choice of either the Performance or  Society skill, as well as the Academia Lore skill. You gain the  Experienced Professional skill feat. |

### Query 7
- Text: What is the rule about **ATHLETE** **BACKGROUND**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 092-097::/page/0/SectionHeader/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 092-097::/page/0/SectionHeader/11', 'PZO22001 Starfinder Player Core 092-097::/page/2/Text/1', 'PZO22001 Starfinder Player Core 092-097::/page/3/Text/23']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 092-097::/page/0/SectionHeader/11` | 0.907374 | **ATHLETE** **BACKGROUND** |
| 2 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/1` | 0.675960 | **DISCIPLE** **BACKGROUND** |
| 3 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/23` | 0.617837 | **RECLUSE** **BACKGROUND** |
| 4 | `PZO22001 Starfinder Player Core 092-097::/page/0/SectionHeader/6` | 0.535609 | **ARTIST** **BACKGROUND** |
| 5 | `PZO22001 Starfinder Player Core 092-097::/page/2/SectionHeader/37` | 0.529588 | **ICON** **BACKGROUND** |
| 6 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/57` | 0.525933 | **Backgrounds** |
| 7 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/34` | 0.525933 | **Backgrounds** |
| 8 | `PZO22001 Starfinder Player Core 092-097::/page/1/SectionHeader/23` | 0.506109 | **COOK** **BACKGROUND** |
| 9 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/27` | 0.500344 | **SCIENTIST** **BACKGROUND** |
| 10 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/33` | 0.494719 | **ANCESTRIES & ** **BACKGROUNDS** |

### Query 8
- Text: What is the rule about You've strengthened your body through practice drills and  workouts, making sure not to waste a single drop of sweat  in your quest for gains. You might be a champion fighting  in arena matches, a hardcore gym rat, or a heavy hitter on a  competitive sports team—what matters to you is the rush you  get when you beat a personal record.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 092-097::/page/0/Text/12']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 092-097::/page/0/Text/12', 'PZO22001 Starfinder Player Core 092-097::/page/1/Text/8', 'PZO22001 Starfinder Player Core 092-097::/page/1/Text/2']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 092-097::/page/0/Text/12` | 0.988478 | You've strengthened your body through practice drills and  workouts, making sure not to waste a single drop of sweat  in your quest for gains. You might be a champion fighting  in arena matches, a har |
| 2 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/8` | 0.536670 | The sound of a roaring crowd still sends your heart pumping  as you recall your glory days as a brutaris player. Whether  you retired successfully or were taken out of commission at  the height of you |
| 3 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/2` | 0.528882 | You're trained in the Athletics skill and the Sports Lore  skill. You gain the Deadlift skill feat. |
| 4 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/2` | 0.463024 | You've spent years performing  arduous physical labor. It  was a difficult life, but you  survived. You may have  embraced adventuring  as an easier method to  make your way in the  world, or you migh |
| 5 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/10` | 0.452420 | You're trained in the Athletics skill and the Sports Lore  skill. You gain the Quick Jump or Titan Wrestler skill feat. |
| 6 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/33` | 0.441932 | Your body is a temple to change and technology. Since  a young age, you've been upgrading your anatomy with  augmentations, perhaps after a terrible accident, as part of  an experiment, or because you |
| 7 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/5` | 0.437545 | You're trained in the Athletics skill and the Labor Lore skill.  You gain the Hefty Hauler skill feat. |
| 8 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/11` | 0.430083 | You're a career criminal with a nasty reputation. Perhaps  unfair circumstances forced you into a life of crime, or maybe  you enjoy the thrill you get from pulling off a heist or living  through a sh |
| 9 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/22` | 0.426995 | The thrill of the win drew you into games of chance.  This might have been a lucrative pastime that paled in  comparison to the real risks of adventuring, or you might  have fallen on hard times due t |
| 10 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/38` | 0.420056 | Everybody wants their 15 minutes of fame, but for you, it's  somehow become a lifestyle. Whether by luck or dedication,  you're a star performer, celebrity, or popular influencer. Your  face, voice, a |

### Query 9
- Text: What is the rule about Choose two attribute boosts. One must be to Strength or  Dexterity, and one is a free attribute boost.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 092-097::/page/1/Text/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 092-097::/page/1/Text/1', 'PZO22001 Starfinder Player Core 092-097::/page/4/Text/11', 'PZO22001 Starfinder Player Core 092-097::/page/4/Text/19']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/1` | 0.936861 | Choose two attribute boosts. One must be to Strength or  Dexterity, and one is a free attribute boost. |
| 2 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/11` | 0.936861 | Choose two attribute boosts. One must be to Strength or  Dexterity, and one is a free attribute boost. |
| 3 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/19` | 0.873036 | Choose two attribute boosts. One must be to Dexterity or  Wisdom, and one is a free attribute boost. |
| 4 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/3` | 0.831036 | Choose two attribute boosts. One must be to Dexterity or  Wisdom, and one is a free attribute boost. |
| 5 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/7` | 0.830803 | Choose two attribute boosts. One must be to Dexterity or  Intelligence, and one is a free attribute boost. |
| 6 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/35` | 0.830803 | Choose two attribute boosts. One must be to Dexterity or  Intelligence, and one is a free attribute boost. |
| 7 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/39` | 0.830803 | Choose two attribute boosts. One must be to Dexterity  or Intelligence, and one is a free attribute boost. |
| 8 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/27` | 0.818463 | Choose two attribute boosts. One must be to Strength or  Intelligence, and one is a free attribute boost. |
| 9 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/8` | 0.811641 | Choose two attribute boosts. One must be to Strength or  Wisdom, and one is a free attribute boost. |
| 10 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/15` | 0.808742 | Choose two attribute boosts. One must be to Dexterity or  Constitution, and one is a free attribute boost. |

### Query 10
- Text: What is the rule about You're trained in the Athletics skill and the Sports Lore  skill. You gain the Deadlift skill feat.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 092-097::/page/1/Text/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 092-097::/page/1/Text/2', 'PZO22001 Starfinder Player Core 092-097::/page/1/Text/10', 'PZO22001 Starfinder Player Core 092-097::/page/3/Text/5']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/2` | 0.972810 | You're trained in the Athletics skill and the Sports Lore  skill. You gain the Deadlift skill feat. |
| 2 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/10` | 0.761616 | You're trained in the Athletics skill and the Sports Lore  skill. You gain the Quick Jump or Titan Wrestler skill feat. |
| 3 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/5` | 0.706650 | You're trained in the Athletics skill and the Labor Lore skill.  You gain the Hefty Hauler skill feat. |
| 4 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/36` | 0.638102 | You're trained in the Athletics skill and the Warfare Lore  skill. You gain the Barricade feat. |
| 5 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/23` | 0.610814 | You're trained in your choice of either the Performance or  Society skill, as well as the Academia Lore skill. You gain the  Experienced Professional skill feat. |
| 6 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/40` | 0.602039 | You're trained in the Performance skill and the Media Lore  skill. You gain the Impressive Performance skill feat. |
| 7 | `PZO22001 Starfinder Player Core 092-097::/page/0/Text/9` | 0.600635 | You're trained in the Crafting skill and the Art Lore skill.  You gain the Specialty Crafting skill feat. |
| 8 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/31` | 0.599268 | You're trained in the Society skill and the History Lore  skill. You gain the Dubious Knowledge skill feat. |
| 9 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/22` | 0.596430 | You're trained in the deity's listed divine skill and gain the  Assurance feat with that skill. You are also trained in a Lore  skill related to your deity (Abadar Lore, for example). |
| 10 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/35` | 0.593108 | You're trained in the Crafting skill and the Augmentation  Lore skill. You gain the Augmented Body feat. |

### Query 11
- Text: What is the rule about **BOUNTY HUNTER** **BACKGROUND**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 092-097::/page/1/SectionHeader/3']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 092-097::/page/1/SectionHeader/3', 'PZO22001 Starfinder Player Core 092-097::/page/1/SectionHeader/7', 'PZO22001 Starfinder Player Core 092-097::/page/2/Text/1']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 092-097::/page/1/SectionHeader/3` | 0.924695 | **BOUNTY HUNTER** **BACKGROUND** |
| 2 | `PZO22001 Starfinder Player Core 092-097::/page/1/SectionHeader/7` | 0.506964 | **BRUTARIS PLAYER** **BACKGROUND** |
| 3 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/1` | 0.504455 | **DISCIPLE** **BACKGROUND** |
| 4 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/23` | 0.434410 | **RECLUSE** **BACKGROUND** |
| 5 | `PZO22001 Starfinder Player Core 092-097::/page/1/SectionHeader/23` | 0.417090 | **COOK** **BACKGROUND** |
| 6 | `PZO22001 Starfinder Player Core 092-097::/page/2/SectionHeader/37` | 0.411161 | **ICON** **BACKGROUND** |
| 7 | `PZO22001 Starfinder Player Core 092-097::/page/0/SectionHeader/6` | 0.410469 | **ARTIST** **BACKGROUND** |
| 8 | `PZO22001 Starfinder Player Core 092-097::/page/0/SectionHeader/11` | 0.401564 | **ATHLETE** **BACKGROUND** |
| 9 | `PZO22001 Starfinder Player Core 092-097::/page/2/SectionHeader/33` | 0.400027 | **HACKER** **BACKGROUND** |
| 10 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/27` | 0.395521 | **SCIENTIST** **BACKGROUND** |

### Query 12
- Text: Summarize You hunt people down for credits. You might work with a  corporation, military, or some other organization.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 092-097::/page/1/Text/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 092-097::/page/1/Text/4', 'PZO22001 Starfinder Player Core 092-097::/page/2/Text/30', 'PZO22001 Starfinder Player Core 092-097::/page/1/Text/28']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/4` | 1.035762 | You hunt people down for credits. You might work with a  corporation, military, or some other organization. |
| 2 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/30` | 0.610425 | You're a con artist and trickster who swindles unsuspecting  dupes and blackmails rubes, but it's nothing personal you're just in it for the credits. You might run an operation  on the side, or you mi |
| 3 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/28` | 0.599971 | You're one among many professionals working in the  corporate world, but you're not just any suit. You're a  negotiator, dealmaker, or perhaps even a spy working to  advance a particular corporation's |
| 4 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/34` | 0.510079 | You enlisted in a military or were recruited by a paramilitary  group as a career trooper. As long as you've got enough  guns and the right squad to back you up, you can handle  just about anything. |
| 5 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/11` | 0.500045 | You're a career criminal with a nasty reputation. Perhaps  unfair circumstances forced you into a life of crime, or maybe  you enjoy the thrill you get from pulling off a heist or living  through a sh |
| 6 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/28` | 0.493878 | You work in a lab and conduct research about a scientific  topic. Perhaps you're a biotechnician, chemist, computer  programmer, theoretical physicist, or accomplished  researcher in some other field. |
| 7 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/2` | 0.479907 | You make your living smuggling cargo, whether on a planet or  in the depths of space. You don't ask your clients too many  questions, and the cargo could be anything—counterfeit  products, illegal goo |
| 8 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/14` | 0.463230 | Some people might say you've been out in the Drift too long,  but the truth is, you don't feel at home away from your post  on a starship deck. You might crew a long-haul freighter,  military gunship, |
| 9 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/41` | 0.461312 | You've dedicated your career to facilitating peaceful  alliances between different factions and peoples. You might  work at an intergalactic embassy or travel aboard a starship  on a mission to remote |
| 10 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/6` | 0.455841 | You're an accomplished healer expertly using the latest tech  and pharmaceuticals to treat your patients. You might work  at a clinic, supervise a starship's medbay, serve as a military  medic, or ply |

### Query 13
- Text: What is the rule about Choose two attribute boosts. One must be to Strength or  Constitution, and one is a free attribute boost.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 092-097::/page/1/Text/5']
- Expected found: `True`
- Expected rank: `6`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 092-097::/page/1/Text/9', 'PZO22001 Starfinder Player Core 092-097::/page/1/Text/34', 'PZO22001 Starfinder Player Core 092-097::/page/3/Text/4']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/9` | 0.946647 | Choose two attribute boosts. One must be to Strength or  Constitution, and one is a free attribute boost. |
| 2 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/34` | 0.946647 | Choose two attribute boosts. One must be to Strength or  Constitution, and one is a free attribute boost. |
| 3 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/4` | 0.946647 | Choose two attribute boosts. One must be to  Strength or Constitution, and one is a free attribute boost. |
| 4 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/35` | 0.904647 | Choose two attribute boosts. One must be to Strength or  Constitution, and one is a free attribute boost. |
| 5 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/16` | 0.904647 | Choose two attribute boosts. One must be to Strength or  Constitution, and one is a free attribute boost. |
| 6 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/5` | 0.904647 | Choose two attribute boosts. One must be to Strength or  Constitution, and one is a free attribute boost. |
| 7 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/27` | 0.831322 | Choose two attribute boosts. One must be to Strength or  Intelligence, and one is a free attribute boost. |
| 8 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/8` | 0.824293 | Choose two attribute boosts. One must be to Strength or  Wisdom, and one is a free attribute boost. |
| 9 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/25` | 0.805547 | Choose two attribute boosts. One must be to Constitution  or Wisdom, and one is a free attribute boost. |
| 10 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/11` | 0.805371 | Choose two attribute boosts. One must be to Strength or  Dexterity, and one is a free attribute boost. |

### Query 14
- Text: What is the rule about You're trained in the Survival skill and the Underworld Lore  skill. You gain the Experienced Tracker skill feat.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 092-097::/page/1/Text/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 092-097::/page/1/Text/6', 'PZO22001 Starfinder Player Core 092-097::/page/3/Text/9', 'PZO22001 Starfinder Player Core 092-097::/page/4/Text/20']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/6` | 0.972405 | You're trained in the Survival skill and the Underworld Lore  skill. You gain the Experienced Tracker skill feat. |
| 2 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/9` | 0.757617 | You're trained in the Survival skill and the Mining  Lore skill. You gain the Terrain Expertise skill feat with  underground terrain. |
| 3 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/20` | 0.747672 | You're trained in the Survival skill and a Lore skill about a  specific settlement. You gain the Urban Survivalist skill feat. |
| 4 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/18` | 0.697743 | You're trained in the Deception skill and Underworld Lore  skill. You gain the Without a Trace skill feat. |
| 5 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/26` | 0.688952 | You're trained in the Survival skill and a Lore skill related to  your former life. You gain the Dubious Knowledge skill feat. |
| 6 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/17` | 0.680792 | You're trained in the Stealth skill and the Underworld Lore  skill. You gain the Experienced Smuggler skill feat. |
| 7 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/26` | 0.665056 | You're trained in the Survival skill and the Cooking Lore  skill. You gain the Seasoned skill feat. |
| 8 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/39` | 0.646125 | You're trained in the Society skill and the Underworld  Lore skill. You gain the Streetwise skill feat. |
| 9 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/13` | 0.628922 | You're trained in the Intimidation skill and the Underworld  Lore skill. You gain the Intimidating Shot skill feat. |
| 10 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/22` | 0.628879 | You're trained in the deity's listed divine skill and gain the  Assurance feat with that skill. You are also trained in a Lore  skill related to your deity (Abadar Lore, for example). |

### Query 15
- Text: What is the rule about **BRUTARIS PLAYER** **BACKGROUND**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 092-097::/page/1/SectionHeader/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 092-097::/page/1/SectionHeader/7', 'PZO22001 Starfinder Player Core 092-097::/page/1/Text/8', 'PZO22001 Starfinder Player Core 092-097::/page/1/SectionHeader/3']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 092-097::/page/1/SectionHeader/7` | 0.949065 | **BRUTARIS PLAYER** **BACKGROUND** |
| 2 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/8` | 0.508353 | The sound of a roaring crowd still sends your heart pumping  as you recall your glory days as a brutaris player. Whether  you retired successfully or were taken out of commission at  the height of you |
| 3 | `PZO22001 Starfinder Player Core 092-097::/page/1/SectionHeader/3` | 0.487201 | **BOUNTY HUNTER** **BACKGROUND** |
| 4 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/23` | 0.425143 | **RECLUSE** **BACKGROUND** |
| 5 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/1` | 0.420423 | **DISCIPLE** **BACKGROUND** |
| 6 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/63` | 0.412811 | **PLAYING THE ** **GAME** |
| 7 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/40` | 0.412811 | **PLAYING THE ** **GAME** |
| 8 | `PZO22001 Starfinder Player Core 092-097::/page/2/SectionHeader/37` | 0.407904 | **ICON** **BACKGROUND** |
| 9 | `PZO22001 Starfinder Player Core 092-097::/page/0/SectionHeader/6` | 0.399499 | **ARTIST** **BACKGROUND** |
| 10 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/14` | 0.382613 | **PRISONER** **BACKGROUND** |

### Query 16
- Text: Summarize The sound of a roaring crowd still sends your heart pumping  as you recall your glory days as a brutaris player. Whether  you retired successfully or were taken out of commission at  the height of your career, you maintained your conditioning  and are always ready for your next big game.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 092-097::/page/1/Text/8']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 092-097::/page/1/Text/8', 'PZO22001 Starfinder Player Core 092-097::/page/0/Text/12', 'PZO22001 Starfinder Player Core 092-097::/page/1/SectionHeader/7']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/8` | 1.043130 | The sound of a roaring crowd still sends your heart pumping  as you recall your glory days as a brutaris player. Whether  you retired successfully or were taken out of commission at  the height of you |
| 2 | `PZO22001 Starfinder Player Core 092-097::/page/0/Text/12` | 0.588813 | You've strengthened your body through practice drills and  workouts, making sure not to waste a single drop of sweat  in your quest for gains. You might be a champion fighting  in arena matches, a har |
| 3 | `PZO22001 Starfinder Player Core 092-097::/page/1/SectionHeader/7` | 0.527080 | **BRUTARIS PLAYER** **BACKGROUND** |
| 4 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/11` | 0.484845 | You're a career criminal with a nasty reputation. Perhaps  unfair circumstances forced you into a life of crime, or maybe  you enjoy the thrill you get from pulling off a heist or living  through a sh |
| 5 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/34` | 0.470536 | You enlisted in a military or were recruited by a paramilitary  group as a career trooper. As long as you've got enough  guns and the right squad to back you up, you can handle  just about anything. |
| 6 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/22` | 0.465004 | The thrill of the win drew you into games of chance.  This might have been a lucrative pastime that paled in  comparison to the real risks of adventuring, or you might  have fallen on hard times due t |
| 7 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/2` | 0.456581 | You've spent years performing  arduous physical labor. It  was a difficult life, but you  survived. You may have  embraced adventuring  as an easier method to  make your way in the  world, or you migh |
| 8 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/12` | 0.448600 | You've lived long enough in a major settlement to know  how to keep your head down, avoid direct eye contact,  and otherwise move about your day without drawing any  attention to yourself. Whether you |
| 9 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/25` | 0.444485 | Whether working in a military outpost, a deep space  exploration vessel, or a local office, you have experience  supporting your comrades by assisting with their tech.  While you've undoubtedly surviv |
| 10 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/14` | 0.439163 | Some people might say you've been out in the Drift too long,  but the truth is, you don't feel at home away from your post  on a starship deck. You might crew a long-haul freighter,  military gunship, |

### Query 17
- Text: What is the rule about Choose two attribute boosts. One must be to Strength or  Constitution, and one is a free attribute boost.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 092-097::/page/1/Text/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 092-097::/page/1/Text/9', 'PZO22001 Starfinder Player Core 092-097::/page/1/Text/34', 'PZO22001 Starfinder Player Core 092-097::/page/3/Text/4']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/9` | 0.946647 | Choose two attribute boosts. One must be to Strength or  Constitution, and one is a free attribute boost. |
| 2 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/34` | 0.946647 | Choose two attribute boosts. One must be to Strength or  Constitution, and one is a free attribute boost. |
| 3 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/4` | 0.946647 | Choose two attribute boosts. One must be to  Strength or Constitution, and one is a free attribute boost. |
| 4 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/35` | 0.904647 | Choose two attribute boosts. One must be to Strength or  Constitution, and one is a free attribute boost. |
| 5 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/16` | 0.904647 | Choose two attribute boosts. One must be to Strength or  Constitution, and one is a free attribute boost. |
| 6 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/5` | 0.904647 | Choose two attribute boosts. One must be to Strength or  Constitution, and one is a free attribute boost. |
| 7 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/27` | 0.831322 | Choose two attribute boosts. One must be to Strength or  Intelligence, and one is a free attribute boost. |
| 8 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/8` | 0.824293 | Choose two attribute boosts. One must be to Strength or  Wisdom, and one is a free attribute boost. |
| 9 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/25` | 0.805547 | Choose two attribute boosts. One must be to Constitution  or Wisdom, and one is a free attribute boost. |
| 10 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/11` | 0.805371 | Choose two attribute boosts. One must be to Strength or  Dexterity, and one is a free attribute boost. |

### Query 18
- Text: What is the rule about You're trained in the Athletics skill and the Sports Lore  skill. You gain the Quick Jump or Titan Wrestler skill feat.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 092-097::/page/1/Text/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 092-097::/page/1/Text/10', 'PZO22001 Starfinder Player Core 092-097::/page/1/Text/2', 'PZO22001 Starfinder Player Core 092-097::/page/3/Text/5']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/10` | 0.980102 | You're trained in the Athletics skill and the Sports Lore  skill. You gain the Quick Jump or Titan Wrestler skill feat. |
| 2 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/2` | 0.754634 | You're trained in the Athletics skill and the Sports Lore  skill. You gain the Deadlift skill feat. |
| 3 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/5` | 0.672473 | You're trained in the Athletics skill and the Labor Lore skill.  You gain the Hefty Hauler skill feat. |
| 4 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/36` | 0.610231 | You're trained in the Athletics skill and the Warfare Lore  skill. You gain the Barricade feat. |
| 5 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/27` | 0.595625 | You're trained in the Computers skill and the Business  Lore skill. You gain the Quick Install skill feat. |
| 6 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/40` | 0.582284 | You're trained in the Performance skill and the Media Lore  skill. You gain the Impressive Performance skill feat. |
| 7 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/23` | 0.577154 | You're trained in your choice of either the Performance or  Society skill, as well as the Academia Lore skill. You gain the  Experienced Professional skill feat. |
| 8 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/20` | 0.571547 | You're trained in the Survival skill and a Lore skill about a  specific settlement. You gain the Urban Survivalist skill feat. |
| 9 | `PZO22001 Starfinder Player Core 092-097::/page/0/Text/9` | 0.570774 | You're trained in the Crafting skill and the Art Lore skill.  You gain the Specialty Crafting skill feat. |
| 10 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/22` | 0.569698 | You're trained in the deity's listed divine skill and gain the  Assurance feat with that skill. You are also trained in a Lore  skill related to your deity (Abadar Lore, for example). |

### Query 19
- Text: What is the rule about **CITY SLICKER** **BACKGROUND**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 092-097::/page/1/SectionHeader/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 092-097::/page/1/SectionHeader/11', 'PZO22001 Starfinder Player Core 092-097::/page/2/Text/1', 'PZO22001 Starfinder Player Core 092-097::/page/2/SectionHeader/25']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 092-097::/page/1/SectionHeader/11` | 0.926295 | **CITY SLICKER** **BACKGROUND** |
| 2 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/1` | 0.516773 | **DISCIPLE** **BACKGROUND** |
| 3 | `PZO22001 Starfinder Player Core 092-097::/page/2/SectionHeader/25` | 0.503314 | **GENE SPLICER** **BACKGROUND** |
| 4 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/23` | 0.448436 | **RECLUSE** **BACKGROUND** |
| 5 | `PZO22001 Starfinder Player Core 092-097::/page/2/SectionHeader/21` | 0.432248 | **GAMBLER** **BACKGROUND** |
| 6 | `PZO22001 Starfinder Player Core 092-097::/page/2/SectionHeader/33` | 0.429592 | **HACKER** **BACKGROUND** |
| 7 | `PZO22001 Starfinder Player Core 092-097::/page/1/SectionHeader/15` | 0.418922 | **CLEANER** **BACKGROUND** |
| 8 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/27` | 0.418439 | **SCIENTIST** **BACKGROUND** |
| 9 | `PZO22001 Starfinder Player Core 092-097::/page/2/SectionHeader/37` | 0.401930 | **ICON** **BACKGROUND** |
| 10 | `PZO22001 Starfinder Player Core 092-097::/page/4/SectionHeader/5` | 0.385120 | **SOCIALITE** **BACKGROUND** |

### Query 20
- Text: What is the rule about You've lived long enough in a major settlement to know  how to keep your head down, avoid direct eye contact,  and otherwise move about your day without drawing any  attention to yourself. Whether you were a detective tailing  a suspect or just lived in a crime-ridden neighborhood,  you've always been able to slip into a crowd to avoid  causing trouble.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 092-097::/page/1/Text/12']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 092-097::/page/1/Text/12', 'PZO22001 Starfinder Player Core 092-097::/page/4/Text/18', 'PZO22001 Starfinder Player Core 092-097::/page/2/Text/30']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/12` | 0.985975 | You've lived long enough in a major settlement to know  how to keep your head down, avoid direct eye contact,  and otherwise move about your day without drawing any  attention to yourself. Whether you |
| 2 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/18` | 0.598934 | You know the streets because they raised you. You grew  up scraping by in a massive cityscape like those on Verces  or Castrovel, or on a crowded space station like Absalom  Station. You might have ev |
| 3 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/30` | 0.549148 | You're a con artist and trickster who swindles unsuspecting  dupes and blackmails rubes, but it's nothing personal you're just in it for the credits. You might run an operation  on the side, or you mi |
| 4 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/11` | 0.480505 | You're a career criminal with a nasty reputation. Perhaps  unfair circumstances forced you into a life of crime, or maybe  you enjoy the thrill you get from pulling off a heist or living  through a sh |
| 5 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/24` | 0.465268 | You used to be someone, but that was in another life. You keep  to yourself these days, eking out an existence as a hermit in  the wilderness or a loner in a rundown neighborhood. You  thought you put |
| 6 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/14` | 0.455333 | You're trained in the Deception skill and a Lore skill about a  specific settlement. You gain the Face in the Crowd skill feat. |
| 7 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/24` | 0.442323 | You grew up in the kitchens of a tavern or other dining  establishment and excelled there, becoming an exceptional  chef. Baking, cooking, a little brewing on the side—you've  spent lots of time out o |
| 8 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/19` | 0.438710 | Whether in a monastery, a religious household, or just as part  of your everyday life, your upbringing was steeped in the  traditions of a particular deity (page 35). You might remain  committed, or y |
| 9 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/34` | 0.438588 | You enlisted in a military or were recruited by a paramilitary  group as a career trooper. As long as you've got enough  guns and the right squad to back you up, you can handle  just about anything. |
| 10 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/15` | 0.432973 | You've been imprisoned or punished for a crime, whether  you were guilty or not. Now that your sentence has ended  or you've escaped, you take full advantage of the newfound  freedom of your adventuri |

### Query 21
- Text: What is the rule about Choose two attribute boosts. One must be to Dexterity or  Charisma, and one is a free attribute boost.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 092-097::/page/1/Text/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 092-097::/page/1/Text/13', 'PZO22001 Starfinder Player Core 092-097::/page/1/Text/17', 'PZO22001 Starfinder Player Core 092-097::/page/2/Text/23']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/13` | 0.945158 | Choose two attribute boosts. One must be to Dexterity or  Charisma, and one is a free attribute boost. |
| 2 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/17` | 0.945158 | Choose two attribute boosts. One must be to Dexterity or  Charisma, and one is a free attribute boost. |
| 3 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/23` | 0.945158 | Choose two attribute boosts. One must be to Dexterity or  Charisma, and one is a free attribute boost. |
| 4 | `PZO22001 Starfinder Player Core 092-097::/page/0/Text/8` | 0.903158 | Choose two attribute boosts. One must be to Dexterity or  Charisma, and one is a free attribute boost. |
| 5 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/19` | 0.843785 | Choose two attribute boosts. One must be to Dexterity or  Wisdom, and one is a free attribute boost. |
| 6 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/3` | 0.843785 | Choose two attribute boosts. One must be to Dexterity or  Wisdom, and one is a free attribute boost. |
| 7 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/35` | 0.839064 | Choose two attribute boosts. One must be to Dexterity or  Intelligence, and one is a free attribute boost. |
| 8 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/7` | 0.839064 | Choose two attribute boosts. One must be to Dexterity or  Intelligence, and one is a free attribute boost. |
| 9 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/39` | 0.839064 | Choose two attribute boosts. One must be to Dexterity  or Intelligence, and one is a free attribute boost. |
| 10 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/11` | 0.827127 | Choose two attribute boosts. One must be to Strength or  Dexterity, and one is a free attribute boost. |

### Query 22
- Text: What is the rule about You're trained in the Deception skill and a Lore skill about a  specific settlement. You gain the Face in the Crowd skill feat.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 092-097::/page/1/Text/14']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 092-097::/page/1/Text/14', 'PZO22001 Starfinder Player Core 092-097::/page/2/Text/24', 'PZO22001 Starfinder Player Core 092-097::/page/1/Text/18']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/14` | 0.982930 | You're trained in the Deception skill and a Lore skill about a  specific settlement. You gain the Face in the Crowd skill feat. |
| 2 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/24` | 0.743186 | You're trained in the Deception skill and the Games Lore  skill. You gain the Lie to Me skill feat. |
| 3 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/18` | 0.710383 | You're trained in the Deception skill and Underworld Lore  skill. You gain the Without a Trace skill feat. |
| 4 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/32` | 0.648918 | You're trained in the Deception skill and a Lore skill related  to a profession or subject you fake expertise in. You gain the  Charming Liar skill feat. |
| 5 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/20` | 0.640936 | You're trained in the Survival skill and a Lore skill about a  specific settlement. You gain the Urban Survivalist skill feat. |
| 6 | `PZO22001 Starfinder Player Core 092-097::/page/0/Text/9` | 0.624353 | You're trained in the Crafting skill and the Art Lore skill.  You gain the Specialty Crafting skill feat. |
| 7 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/20` | 0.611570 | You're trained in the Society skill and a Lore skill related  to one city or region you've visited often. You gain the  Multilingual skill feat. |
| 8 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/31` | 0.611451 | You're trained in the Society skill and the History Lore  skill. You gain the Dubious Knowledge skill feat. |
| 9 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/30` | 0.595111 | You're trained in the Crafting skill and a Lore skill related  to your field of research. You gain the Assurance skill feat  with that Lore skill. |
| 10 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/26` | 0.592861 | You're trained in the Survival skill and a Lore skill related to  your former life. You gain the Dubious Knowledge skill feat. |

### Query 23
- Text: What is the rule about **CLEANER** **BACKGROUND**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 092-097::/page/1/SectionHeader/15']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 092-097::/page/1/SectionHeader/15', 'PZO22001 Starfinder Player Core 092-097::/page/2/Text/1', 'PZO22001 Starfinder Player Core 092-097::/page/3/Text/23']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 092-097::/page/1/SectionHeader/15` | 0.913486 | **CLEANER** **BACKGROUND** |
| 2 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/1` | 0.592531 | **DISCIPLE** **BACKGROUND** |
| 3 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/23` | 0.575163 | **RECLUSE** **BACKGROUND** |
| 4 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/27` | 0.500904 | **SCIENTIST** **BACKGROUND** |
| 5 | `PZO22001 Starfinder Player Core 092-097::/page/2/SectionHeader/37` | 0.484709 | **ICON** **BACKGROUND** |
| 6 | `PZO22001 Starfinder Player Core 092-097::/page/2/SectionHeader/33` | 0.482676 | **HACKER** **BACKGROUND** |
| 7 | `PZO22001 Starfinder Player Core 092-097::/page/0/SectionHeader/6` | 0.477164 | **ARTIST** **BACKGROUND** |
| 8 | `PZO22001 Starfinder Player Core 092-097::/page/1/SectionHeader/23` | 0.472042 | **COOK** **BACKGROUND** |
| 9 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/6` | 0.462297 | **MINER** **BACKGROUND** |
| 10 | `PZO22001 Starfinder Player Core 092-097::/page/2/SectionHeader/5` | 0.450946 | **DOCTOR** **BACKGROUND** |

### Query 24
- Text: What is the rule about You know how to remove all traces of a crime. Whether you  worked under the table for legitimate clients like AbadarCorp  or learned your trade working for shady organizations and  crime bosses, you know how to leave a crime scene as good  as new.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 092-097::/page/1/Text/16']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 092-097::/page/1/Text/16', 'PZO22001 Starfinder Player Core 092-097::/page/2/Text/30', 'PZO22001 Starfinder Player Core 092-097::/page/1/Text/37']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/16` | 0.989160 | You know how to remove all traces of a crime. Whether you  worked under the table for legitimate clients like AbadarCorp  or learned your trade working for shady organizations and  crime bosses, you k |
| 2 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/30` | 0.560851 | You're a con artist and trickster who swindles unsuspecting  dupes and blackmails rubes, but it's nothing personal you're just in it for the credits. You might run an operation  on the side, or you mi |
| 3 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/37` | 0.549504 | You solved crimes as a police inspector or took clandestine  jobs for various clients as a private investigator. You might  have become an adventurer as part of your next big mystery,  but it's equall |
| 4 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/11` | 0.497424 | You're a career criminal with a nasty reputation. Perhaps  unfair circumstances forced you into a life of crime, or maybe  you enjoy the thrill you get from pulling off a heist or living  through a sh |
| 5 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/24` | 0.435764 | You grew up in the kitchens of a tavern or other dining  establishment and excelled there, becoming an exceptional  chef. Baking, cooking, a little brewing on the side—you've  spent lots of time out o |
| 6 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/15` | 0.433763 | You've been imprisoned or punished for a crime, whether  you were guilty or not. Now that your sentence has ended  or you've escaped, you take full advantage of the newfound  freedom of your adventuri |
| 7 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/28` | 0.431933 | You're one among many professionals working in the  corporate world, but you're not just any suit. You're a  negotiator, dealmaker, or perhaps even a spy working to  advance a particular corporation's |
| 8 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/18` | 0.430108 | You know the streets because they raised you. You grew  up scraping by in a massive cityscape like those on Verces  or Castrovel, or on a crowded space station like Absalom  Station. You might have ev |
| 9 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/2` | 0.429142 | You make your living smuggling cargo, whether on a planet or  in the depths of space. You don't ask your clients too many  questions, and the cargo could be anything—counterfeit  products, illegal goo |
| 10 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/18` | 0.420521 | You're trained in the Deception skill and Underworld Lore  skill. You gain the Without a Trace skill feat. |

### Query 25
- Text: What is the rule about Choose two attribute boosts. One must be to Dexterity or  Charisma, and one is a free attribute boost.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 092-097::/page/1/Text/17']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 092-097::/page/1/Text/13', 'PZO22001 Starfinder Player Core 092-097::/page/1/Text/17', 'PZO22001 Starfinder Player Core 092-097::/page/2/Text/23']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/13` | 0.945158 | Choose two attribute boosts. One must be to Dexterity or  Charisma, and one is a free attribute boost. |
| 2 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/17` | 0.945158 | Choose two attribute boosts. One must be to Dexterity or  Charisma, and one is a free attribute boost. |
| 3 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/23` | 0.945158 | Choose two attribute boosts. One must be to Dexterity or  Charisma, and one is a free attribute boost. |
| 4 | `PZO22001 Starfinder Player Core 092-097::/page/0/Text/8` | 0.903158 | Choose two attribute boosts. One must be to Dexterity or  Charisma, and one is a free attribute boost. |
| 5 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/19` | 0.843785 | Choose two attribute boosts. One must be to Dexterity or  Wisdom, and one is a free attribute boost. |
| 6 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/3` | 0.843785 | Choose two attribute boosts. One must be to Dexterity or  Wisdom, and one is a free attribute boost. |
| 7 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/35` | 0.839064 | Choose two attribute boosts. One must be to Dexterity or  Intelligence, and one is a free attribute boost. |
| 8 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/7` | 0.839064 | Choose two attribute boosts. One must be to Dexterity or  Intelligence, and one is a free attribute boost. |
| 9 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/39` | 0.839064 | Choose two attribute boosts. One must be to Dexterity  or Intelligence, and one is a free attribute boost. |
| 10 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/11` | 0.827127 | Choose two attribute boosts. One must be to Strength or  Dexterity, and one is a free attribute boost. |

### Query 26
- Text: What is the rule about You're trained in the Deception skill and Underworld Lore  skill. You gain the Without a Trace skill feat.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 092-097::/page/1/Text/18']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 092-097::/page/1/Text/18', 'PZO22001 Starfinder Player Core 092-097::/page/1/Text/6', 'PZO22001 Starfinder Player Core 092-097::/page/2/Text/24']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/18` | 0.977011 | You're trained in the Deception skill and Underworld Lore  skill. You gain the Without a Trace skill feat. |
| 2 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/6` | 0.730960 | You're trained in the Survival skill and the Underworld Lore  skill. You gain the Experienced Tracker skill feat. |
| 3 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/24` | 0.729324 | You're trained in the Deception skill and the Games Lore  skill. You gain the Lie to Me skill feat. |
| 4 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/14` | 0.679446 | You're trained in the Deception skill and a Lore skill about a  specific settlement. You gain the Face in the Crowd skill feat. |
| 5 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/17` | 0.640589 | You're trained in the Stealth skill and the Underworld Lore  skill. You gain the Experienced Smuggler skill feat. |
| 6 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/39` | 0.639319 | You're trained in the Society skill and the Underworld  Lore skill. You gain the Streetwise skill feat. |
| 7 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/13` | 0.637501 | You're trained in the Intimidation skill and the Underworld  Lore skill. You gain the Intimidating Shot skill feat. |
| 8 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/32` | 0.626405 | You're trained in the Deception skill and a Lore skill related  to a profession or subject you fake expertise in. You gain the  Charming Liar skill feat. |
| 9 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/12` | 0.608353 | You're trained in the Occultism skill and a Lore skill  related to your choice of metaphysical topics. You gain the  Schooled in Secrets skill feat. |
| 10 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/22` | 0.608175 | You're trained in the deity's listed divine skill and gain the  Assurance feat with that skill. You are also trained in a Lore  skill related to your deity (Abadar Lore, for example). |

### Query 27
- Text: What is the rule about **COMEDIAN** **BACKGROUND**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 092-097::/page/1/SectionHeader/19']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 092-097::/page/1/SectionHeader/19', 'PZO22001 Starfinder Player Core 092-097::/page/1/SectionHeader/23', 'PZO22001 Starfinder Player Core 092-097::/page/2/Text/1']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 092-097::/page/1/SectionHeader/19` | 0.903518 | **COMEDIAN** **BACKGROUND** |
| 2 | `PZO22001 Starfinder Player Core 092-097::/page/1/SectionHeader/23` | 0.581449 | **COOK** **BACKGROUND** |
| 3 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/1` | 0.574297 | **DISCIPLE** **BACKGROUND** |
| 4 | `PZO22001 Starfinder Player Core 092-097::/page/0/SectionHeader/6` | 0.490479 | **ARTIST** **BACKGROUND** |
| 5 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/34` | 0.482120 | **Backgrounds** |
| 6 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/57` | 0.482120 | **Backgrounds** |
| 7 | `PZO22001 Starfinder Player Core 092-097::/page/2/SectionHeader/37` | 0.481769 | **ICON** **BACKGROUND** |
| 8 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/23` | 0.476833 | **RECLUSE** **BACKGROUND** |
| 9 | `PZO22001 Starfinder Player Core 092-097::/page/2/SectionHeader/5` | 0.474572 | **DOCTOR** **BACKGROUND** |
| 10 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/27` | 0.458661 | **SCIENTIST** **BACKGROUND** |

### Query 28
- Text: Summarize Whether you're the office joker, a professional comedian, or  just a troll on the infosphere, you're always prepared with a  well-timed joke, even if it occasionally gets you in hot water  when you cross the line.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 092-097::/page/1/Text/20']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 092-097::/page/1/Text/20', 'PZO22001 Starfinder Player Core 092-097::/page/1/Text/28', 'PZO22001 Starfinder Player Core 092-097::/page/2/Text/38']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/20` | 1.039308 | Whether you're the office joker, a professional comedian, or  just a troll on the infosphere, you're always prepared with a  well-timed joke, even if it occasionally gets you in hot water  when you cr |
| 2 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/28` | 0.553399 | You're one among many professionals working in the  corporate world, but you're not just any suit. You're a  negotiator, dealmaker, or perhaps even a spy working to  advance a particular corporation's |
| 3 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/38` | 0.515825 | Everybody wants their 15 minutes of fame, but for you, it's  somehow become a lifestyle. Whether by luck or dedication,  you're a star performer, celebrity, or popular influencer. Your  face, voice, a |
| 4 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/34` | 0.449102 | You've always had a knack for computers and virtual spaces  and pride yourself on your ability to learn technical secrets.  The open networks known as infospheres are your home  and the place you can |
| 5 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/12` | 0.446739 | You've lived long enough in a major settlement to know  how to keep your head down, avoid direct eye contact,  and otherwise move about your day without drawing any  attention to yourself. Whether you |
| 6 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/6` | 0.435578 | Thanks to generational wealth or lucky circumstance, you  live a charmed life flitting between galas dressed in the  latest designer fashion. You memorialize every glittering  moment on social media, |
| 7 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/24` | 0.411589 | You grew up in the kitchens of a tavern or other dining  establishment and excelled there, becoming an exceptional  chef. Baking, cooking, a little brewing on the side—you've  spent lots of time out o |
| 8 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/30` | 0.408096 | You're a con artist and trickster who swindles unsuspecting  dupes and blackmails rubes, but it's nothing personal you're just in it for the credits. You might run an operation  on the side, or you mi |
| 9 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/25` | 0.400225 | Whether working in a military outpost, a deep space  exploration vessel, or a local office, you have experience  supporting your comrades by assisting with their tech.  While you've undoubtedly surviv |
| 10 | `PZO22001 Starfinder Player Core 092-097::/page/0/Text/12` | 0.397887 | You've strengthened your body through practice drills and  workouts, making sure not to waste a single drop of sweat  in your quest for gains. You might be a champion fighting  in arena matches, a har |

### Query 29
- Text: What is the rule about Choose two attribute boosts. One must be to Wisdom or  Charisma, and one is a free attribute boost.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 092-097::/page/1/Text/21']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 092-097::/page/1/Text/21', 'PZO22001 Starfinder Player Core 092-097::/page/2/Text/11', 'PZO22001 Starfinder Player Core 092-097::/page/2/Text/31']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/21` | 0.951308 | Choose two attribute boosts. One must be to Wisdom or  Charisma, and one is a free attribute boost. |
| 2 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/11` | 0.951308 | Choose two attribute boosts. One must be to Wisdom or  Charisma, and one is a free attribute boost. |
| 3 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/31` | 0.877275 | Choose two attribute boosts. One must be to Intelligence  or Charisma, and one is a free attribute boost. |
| 4 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/42` | 0.835275 | Choose two attribute boosts. One must be to Intelligence  or Charisma, and one is a free attribute boost. |
| 5 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/29` | 0.835275 | Choose two attribute boosts. One must be to Intelligence  or Charisma, and one is a free attribute boost. |
| 6 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/7` | 0.835275 | Choose two attribute boosts. One must be to Intelligence  or Charisma, and one is a free attribute boost. |
| 7 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/19` | 0.835275 | Choose two attribute boosts. One must be to Intelligence  or Charisma, and one is a free attribute boost. |
| 8 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/8` | 0.830592 | Choose two attribute boosts. One must be to Strength or  Wisdom, and one is a free attribute boost. |
| 9 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/29` | 0.827810 | Choose two attribute boosts. One must be to Intelligence  or Wisdom, and one is a free attribute boost. |
| 10 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/38` | 0.827810 | Choose two attribute boosts. One must be to Intelligence  or Wisdom, and one is a free attribute boost. |

### Query 30
- Text: What is the rule about You're trained in the Performance skill and the Media Lore  skill. You gain the Just Kidding skill feat.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 092-097::/page/1/Text/22']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 092-097::/page/1/Text/22', 'PZO22001 Starfinder Player Core 092-097::/page/2/Text/40', 'PZO22001 Starfinder Player Core 092-097::/page/4/Text/23']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/22` | 0.977553 | You're trained in the Performance skill and the Media Lore  skill. You gain the Just Kidding skill feat. |
| 2 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/40` | 0.800212 | You're trained in the Performance skill and the Media Lore  skill. You gain the Impressive Performance skill feat. |
| 3 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/23` | 0.687533 | You're trained in your choice of either the Performance or  Society skill, as well as the Academia Lore skill. You gain the  Experienced Professional skill feat. |
| 4 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/31` | 0.626334 | You're trained in the Society skill and the History Lore  skill. You gain the Dubious Knowledge skill feat. |
| 5 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/24` | 0.602848 | You're trained in the Deception skill and the Games Lore  skill. You gain the Lie to Me skill feat. |
| 6 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/26` | 0.591123 | You're trained in the Survival skill and a Lore skill related to  your former life. You gain the Dubious Knowledge skill feat. |
| 7 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/10` | 0.579035 | You're trained in the Athletics skill and the Sports Lore  skill. You gain the Quick Jump or Titan Wrestler skill feat. |
| 8 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/18` | 0.578304 | You're trained in the Deception skill and Underworld Lore  skill. You gain the Without a Trace skill feat. |
| 9 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/14` | 0.574973 | You're trained in the Deception skill and a Lore skill about a  specific settlement. You gain the Face in the Crowd skill feat. |
| 10 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/8` | 0.573121 | You're trained in the Society skill and a Lore skill related  to your home planet. You gain the Plant Rumor skill feat. |

### Query 31
- Text: What is the rule about **COOK** **BACKGROUND**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 092-097::/page/1/SectionHeader/23']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 092-097::/page/1/SectionHeader/23', 'PZO22001 Starfinder Player Core 092-097::/page/2/Text/1', 'PZO22001 Starfinder Player Core 092-097::/page/3/Text/23']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 092-097::/page/1/SectionHeader/23` | 0.881703 | **COOK** **BACKGROUND** |
| 2 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/1` | 0.654999 | **DISCIPLE** **BACKGROUND** |
| 3 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/23` | 0.597625 | **RECLUSE** **BACKGROUND** |
| 4 | `PZO22001 Starfinder Player Core 092-097::/page/2/SectionHeader/37` | 0.548865 | **ICON** **BACKGROUND** |
| 5 | `PZO22001 Starfinder Player Core 092-097::/page/1/SectionHeader/19` | 0.542687 | **COMEDIAN** **BACKGROUND** |
| 6 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/34` | 0.510723 | **Backgrounds** |
| 7 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/57` | 0.510723 | **Backgrounds** |
| 8 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/21` | 0.491001 | **ANCESTRIES & ** **BACKGROUNDS** |
| 9 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/33` | 0.491001 | **ANCESTRIES & ** **BACKGROUNDS** |
| 10 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/46` | 0.491001 | **ANCESTRIES & ** **BACKGROUNDS** |

### Query 32
- Text: Summarize You grew up in the kitchens of a tavern or other dining  establishment and excelled there, becoming an exceptional  chef. Baking, cooking, a little brewing on the side—you've  spent lots of time out of sight. It's about time you went out  into the world to catch some sights for yourself.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 092-097::/page/1/Text/24']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 092-097::/page/1/Text/24', 'PZO22001 Starfinder Player Core 092-097::/page/4/Text/14', 'PZO22001 Starfinder Player Core 092-097::/page/4/Text/21']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/24` | 1.043035 | You grew up in the kitchens of a tavern or other dining  establishment and excelled there, becoming an exceptional  chef. Baking, cooking, a little brewing on the side—you've  spent lots of time out o |
| 2 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/14` | 0.577613 | Some people might say you've been out in the Drift too long,  but the truth is, you don't feel at home away from your post  on a starship deck. You might crew a long-haul freighter,  military gunship, |
| 3 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/21` | 0.574444 | You are incredibly knowledgeable, skilled, and perhaps even  trained to teach children and adults about the world and  its wonders. From books to classes, you're committed to  imparting knowledge to a |
| 4 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/24` | 0.518037 | You used to be someone, but that was in another life. You keep  to yourself these days, eking out an existence as a hermit in  the wilderness or a loner in a rundown neighborhood. You  thought you put |
| 5 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/19` | 0.512501 | Whether in a monastery, a religious household, or just as part  of your everyday life, your upbringing was steeped in the  traditions of a particular deity (page 35). You might remain  committed, or y |
| 6 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/2` | 0.509747 | You've spent years performing  arduous physical labor. It  was a difficult life, but you  survived. You may have  embraced adventuring  as an easier method to  make your way in the  world, or you migh |
| 7 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/37` | 0.494343 | You solved crimes as a police inspector or took clandestine  jobs for various clients as a private investigator. You might  have become an adventurer as part of your next big mystery,  but it's equall |
| 8 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/22` | 0.493478 | The thrill of the win drew you into games of chance.  This might have been a lucrative pastime that paled in  comparison to the real risks of adventuring, or you might  have fallen on hard times due t |
| 9 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/11` | 0.489505 | You're a career criminal with a nasty reputation. Perhaps  unfair circumstances forced you into a life of crime, or maybe  you enjoy the thrill you get from pulling off a heist or living  through a sh |
| 10 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/38` | 0.489192 | Everybody wants their 15 minutes of fame, but for you, it's  somehow become a lifestyle. Whether by luck or dedication,  you're a star performer, celebrity, or popular influencer. Your  face, voice, a |

### Query 33
- Text: What is the rule about Choose two attribute boosts. One must be to Constitution  or Intelligence, and one is a free attribute boost.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 092-097::/page/1/Text/25']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 092-097::/page/1/Text/25', 'PZO22001 Starfinder Player Core 092-097::/page/4/Text/26', 'PZO22001 Starfinder Player Core 092-097::/page/2/Text/15']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/25` | 0.954303 | Choose two attribute boosts. One must be to Constitution  or Intelligence, and one is a free attribute boost. |
| 2 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/26` | 0.954303 | Choose two attribute boosts. One must be to Constitution  or Intelligence, and one is a free attribute boost. |
| 3 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/15` | 0.954303 | Choose two attribute boosts. One must be to Constitution  or Intelligence, and one is a free attribute boost. |
| 4 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/25` | 0.851807 | Choose two attribute boosts. One must be to Constitution  or Wisdom, and one is a free attribute boost. |
| 5 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/38` | 0.830713 | Choose two attribute boosts. One must be to Intelligence  or Wisdom, and one is a free attribute boost. |
| 6 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/22` | 0.830713 | Choose two attribute boosts. One must be to Intelligence  or Wisdom, and one is a free attribute boost. |
| 7 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/29` | 0.830713 | Choose two attribute boosts. One must be to Intelligence  or Wisdom, and one is a free attribute boost. |
| 8 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/4` | 0.824036 | Choose two attribute boosts. One must be to  Strength or Constitution, and one is a free attribute boost. |
| 9 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/35` | 0.824036 | Choose two attribute boosts. One must be to Strength or  Constitution, and one is a free attribute boost. |
| 10 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/16` | 0.824036 | Choose two attribute boosts. One must be to Strength or  Constitution, and one is a free attribute boost. |

### Query 34
- Text: What is the rule about You're trained in the Survival skill and the Cooking Lore  skill. You gain the Seasoned skill feat.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 092-097::/page/1/Text/26']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 092-097::/page/1/Text/26', 'PZO22001 Starfinder Player Core 092-097::/page/4/Text/20', 'PZO22001 Starfinder Player Core 092-097::/page/3/Text/26']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/26` | 0.966757 | You're trained in the Survival skill and the Cooking Lore  skill. You gain the Seasoned skill feat. |
| 2 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/20` | 0.752908 | You're trained in the Survival skill and a Lore skill about a  specific settlement. You gain the Urban Survivalist skill feat. |
| 3 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/26` | 0.736603 | You're trained in the Survival skill and a Lore skill related to  your former life. You gain the Dubious Knowledge skill feat. |
| 4 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/6` | 0.663293 | You're trained in the Survival skill and the Underworld Lore  skill. You gain the Experienced Tracker skill feat. |
| 5 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/9` | 0.653957 | You're trained in the Survival skill and the Mining  Lore skill. You gain the Terrain Expertise skill feat with  underground terrain. |
| 6 | `PZO22001 Starfinder Player Core 092-097::/page/0/Text/9` | 0.634746 | You're trained in the Crafting skill and the Art Lore skill.  You gain the Specialty Crafting skill feat. |
| 7 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/30` | 0.632869 | You're trained in the Crafting skill and a Lore skill related  to your field of research. You gain the Assurance skill feat  with that Lore skill. |
| 8 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/28` | 0.628017 | You're trained in the Crafting skill and the Augmentation or  Life Science Lore skill. You gain the Serum Crafting skill feat. |
| 9 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/31` | 0.616140 | You're trained in the Society skill and the History Lore  skill. You gain the Dubious Knowledge skill feat. |
| 10 | `PZO22001 Starfinder Player Core 092-097::/page/0/Text/3` | 0.611580 | At 1st level, when you create your character, you gain a  background of your choice. This decision is permanent;  you can't change it at later levels. Each background listed  here grants two boosts, u |

### Query 35
- Text: What is the rule about **CORPORATE AGENT** **BACKGROUND**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 092-097::/page/1/SectionHeader/27']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 092-097::/page/1/SectionHeader/27', 'PZO22001 Starfinder Player Core 092-097::/page/2/Text/1', 'PZO22001 Starfinder Player Core 092-097::/page/4/SectionHeader/5']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 092-097::/page/1/SectionHeader/27` | 0.909361 | **CORPORATE AGENT** **BACKGROUND** |
| 2 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/1` | 0.582241 | **DISCIPLE** **BACKGROUND** |
| 3 | `PZO22001 Starfinder Player Core 092-097::/page/4/SectionHeader/5` | 0.556256 | **SOCIALITE** **BACKGROUND** |
| 4 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/23` | 0.502788 | **RECLUSE** **BACKGROUND** |
| 5 | `PZO22001 Starfinder Player Core 092-097::/page/2/SectionHeader/37` | 0.496070 | **ICON** **BACKGROUND** |
| 6 | `PZO22001 Starfinder Player Core 092-097::/page/1/SectionHeader/19` | 0.492527 | **COMEDIAN** **BACKGROUND** |
| 7 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/27` | 0.478516 | **SCIENTIST** **BACKGROUND** |
| 8 | `PZO22001 Starfinder Player Core 092-097::/page/2/SectionHeader/5` | 0.469648 | **DOCTOR** **BACKGROUND** |
| 9 | `PZO22001 Starfinder Player Core 092-097::/page/0/SectionHeader/6` | 0.466183 | **ARTIST** **BACKGROUND** |
| 10 | `PZO22001 Starfinder Player Core 092-097::/page/1/SectionHeader/23` | 0.463392 | **COOK** **BACKGROUND** |

### Query 36
- Text: What is the rule about You're one among many professionals working in the  corporate world, but you're not just any suit. You're a  negotiator, dealmaker, or perhaps even a spy working to  advance a particular corporation's agenda. You might be a cog  in a corporation's massive machine or a shill for an up-andcoming entrepreneur no one has heard of... yet.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 092-097::/page/1/Text/28']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 092-097::/page/1/Text/28', 'PZO22001 Starfinder Player Core 092-097::/page/1/Text/4', 'PZO22001 Starfinder Player Core 092-097::/page/3/Text/28']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/28` | 0.988393 | You're one among many professionals working in the  corporate world, but you're not just any suit. You're a  negotiator, dealmaker, or perhaps even a spy working to  advance a particular corporation's |
| 2 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/4` | 0.596687 | You hunt people down for credits. You might work with a  corporation, military, or some other organization. |
| 3 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/28` | 0.595836 | You work in a lab and conduct research about a scientific  topic. Perhaps you're a biotechnician, chemist, computer  programmer, theoretical physicist, or accomplished  researcher in some other field. |
| 4 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/30` | 0.543084 | You're a con artist and trickster who swindles unsuspecting  dupes and blackmails rubes, but it's nothing personal you're just in it for the credits. You might run an operation  on the side, or you mi |
| 5 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/6` | 0.541113 | You're an accomplished healer expertly using the latest tech  and pharmaceuticals to treat your patients. You might work  at a clinic, supervise a starship's medbay, serve as a military  medic, or ply |
| 6 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/34` | 0.522822 | You've always had a knack for computers and virtual spaces  and pride yourself on your ability to learn technical secrets.  The open networks known as infospheres are your home  and the place you can |
| 7 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/10` | 0.521708 | You're a crewmate on a pirate vessel with ambitions of  pillaging interstellar shipping lanes or taking over a chunk  of a notable planetary body. Perhaps you grew up on such  a ship, were taken priso |
| 8 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/41` | 0.517706 | You've dedicated your career to facilitating peaceful  alliances between different factions and peoples. You might  work at an intergalactic embassy or travel aboard a starship  on a mission to remote |
| 9 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/21` | 0.514902 | You are incredibly knowledgeable, skilled, and perhaps even  trained to teach children and adults about the world and  its wonders. From books to classes, you're committed to  imparting knowledge to a |
| 10 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/18` | 0.508175 | As a diplomat or messenger, you traveled extensively,  communicating with new people and brokering alliances  wherever you went. |

### Query 37
- Text: What is the rule about Choose two attribute boosts. One must be to Intelligence  or Charisma, and one is a free attribute boost.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 092-097::/page/1/Text/29']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 092-097::/page/1/Text/42', 'PZO22001 Starfinder Player Core 092-097::/page/1/Text/29', 'PZO22001 Starfinder Player Core 092-097::/page/4/Text/7']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/42` | 0.947131 | Choose two attribute boosts. One must be to Intelligence  or Charisma, and one is a free attribute boost. |
| 2 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/29` | 0.947131 | Choose two attribute boosts. One must be to Intelligence  or Charisma, and one is a free attribute boost. |
| 3 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/7` | 0.947131 | Choose two attribute boosts. One must be to Intelligence  or Charisma, and one is a free attribute boost. |
| 4 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/19` | 0.905131 | Choose two attribute boosts. One must be to Intelligence  or Charisma, and one is a free attribute boost. |
| 5 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/31` | 0.905131 | Choose two attribute boosts. One must be to Intelligence  or Charisma, and one is a free attribute boost. |
| 6 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/22` | 0.843184 | Choose two attribute boosts. One must be to Intelligence  or Wisdom, and one is a free attribute boost. |
| 7 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/38` | 0.843184 | Choose two attribute boosts. One must be to Intelligence  or Wisdom, and one is a free attribute boost. |
| 8 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/29` | 0.843184 | Choose two attribute boosts. One must be to Intelligence  or Wisdom, and one is a free attribute boost. |
| 9 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/21` | 0.841134 | Choose two attribute boosts. One must be to Wisdom or  Charisma, and one is a free attribute boost. |
| 10 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/11` | 0.841134 | Choose two attribute boosts. One must be to Wisdom or  Charisma, and one is a free attribute boost. |

### Query 38
- Text: What is the rule about You're trained in the Society skill and the Corporate Lore  skill. You gain the Management Material skill feat.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 092-097::/page/1/Text/30']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 092-097::/page/1/Text/30', 'PZO22001 Starfinder Player Core 092-097::/page/4/Text/31', 'PZO22001 Starfinder Player Core 092-097::/page/4/Text/23']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/30` | 0.976197 | You're trained in the Society skill and the Corporate Lore  skill. You gain the Management Material skill feat. |
| 2 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/31` | 0.736007 | You're trained in the Society skill and the History Lore  skill. You gain the Dubious Knowledge skill feat. |
| 3 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/23` | 0.725364 | You're trained in your choice of either the Performance or  Society skill, as well as the Academia Lore skill. You gain the  Experienced Professional skill feat. |
| 4 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/39` | 0.672802 | You're trained in the Society skill and the Underworld  Lore skill. You gain the Streetwise skill feat. |
| 5 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/20` | 0.663804 | You're trained in the Society skill and a Lore skill related  to one city or region you've visited often. You gain the  Multilingual skill feat. |
| 6 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/8` | 0.649294 | You're trained in the Society skill and a Lore skill related  to your home planet. You gain the Plant Rumor skill feat. |
| 7 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/27` | 0.621578 | You're trained in the Computers skill and the Business  Lore skill. You gain the Quick Install skill feat. |
| 8 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/30` | 0.605685 | You're trained in the Crafting skill and a Lore skill related  to your field of research. You gain the Assurance skill feat  with that Lore skill. |
| 9 | `PZO22001 Starfinder Player Core 092-097::/page/0/Text/9` | 0.598016 | You're trained in the Crafting skill and the Art Lore skill.  You gain the Specialty Crafting skill feat. |
| 10 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/16` | 0.590006 | You're trained in the Crafting skill and the Physical  Science Lore skill. You gain the Electrical Engineer skill feat. |

### Query 39
- Text: What is the rule about **CYBERBORN** **BACKGROUND**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 092-097::/page/1/SectionHeader/31']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 092-097::/page/1/SectionHeader/31', 'PZO22001 Starfinder Player Core 092-097::/page/2/Text/1', 'PZO22001 Starfinder Player Core 092-097::/page/4/SectionHeader/24']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 092-097::/page/1/SectionHeader/31` | 0.921656 | **CYBERBORN** **BACKGROUND** |
| 2 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/1` | 0.511128 | **DISCIPLE** **BACKGROUND** |
| 3 | `PZO22001 Starfinder Player Core 092-097::/page/4/SectionHeader/24` | 0.474780 | **TECH SUPPORT** **BACKGROUND** |
| 4 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/57` | 0.428273 | **Backgrounds** |
| 5 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/34` | 0.428273 | **Backgrounds** |
| 6 | `PZO22001 Starfinder Player Core 092-097::/page/2/SectionHeader/37` | 0.422200 | **ICON** **BACKGROUND** |
| 7 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/33` | 0.422014 | **ANCESTRIES & ** **BACKGROUNDS** |
| 8 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/21` | 0.422014 | **ANCESTRIES & ** **BACKGROUNDS** |
| 9 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/46` | 0.422014 | **ANCESTRIES & ** **BACKGROUNDS** |
| 10 | `PZO22001 Starfinder Player Core 092-097::/page/2/SectionHeader/33` | 0.420461 | **HACKER** **BACKGROUND** |

### Query 40
- Text: Summarize **UNCOMMON**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 092-097::/page/1/SectionHeader/32']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 092-097::/page/1/SectionHeader/32', 'PZO22001 Starfinder Player Core 092-097::/page/4/SectionHeader/33', 'PZO22001 Starfinder Player Core 092-097::/page/5/TableCell/490']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 092-097::/page/1/SectionHeader/32` | 0.956210 | **UNCOMMON** |
| 2 | `PZO22001 Starfinder Player Core 092-097::/page/4/SectionHeader/33` | 0.956210 | **UNCOMMON** |
| 3 | `PZO22001 Starfinder Player Core 092-097::/page/5/TableCell/490` | 0.519874 | Common |
| 4 | `PZO22001 Starfinder Player Core 092-097::/page/5/SectionHeader/10` | 0.475600 | **UNCOMMON EXTRAPLANAR LANGUAGES** |
| 5 | `PZO22001 Starfinder Player Core 092-097::/page/5/SectionHeader/8` | 0.401969 | **COMMON REGIONAL LANGUAGES** |
| 6 | `PZO22001 Starfinder Player Core 092-097::/page/5/SectionHeader/6` | 0.401444 | **COMMON ANCESTRY LANGUAGES** |
| 7 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/20` | 0.373995 | **INTRODUCTION** |
| 8 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/45` | 0.373995 | **INTRODUCTION** |
| 9 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/32` | 0.373995 | **INTRODUCTION** |
| 10 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/24` | 0.371621 | **Human** |

### Query 41
- Text: What is the rule about Your body is a temple to change and technology. Since  a young age, you've been upgrading your anatomy with  augmentations, perhaps after a terrible accident, as part of  an experiment, or because you desire to transform your body  into something more.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 092-097::/page/1/Text/33']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 092-097::/page/1/Text/33', 'PZO22001 Starfinder Player Core 092-097::/page/2/Text/26', 'PZO22001 Starfinder Player Core 092-097::/page/2/Text/6']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/33` | 0.987663 | Your body is a temple to change and technology. Since  a young age, you've been upgrading your anatomy with  augmentations, perhaps after a terrible accident, as part of  an experiment, or because you |
| 2 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/26` | 0.541555 | You're an expert on biotech and genetics and frequently  experiment on your own body. You might have worked with  patients who needed gene therapy, conducted research in  laboratories looking for the |
| 3 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/6` | 0.523549 | You're an accomplished healer expertly using the latest tech  and pharmaceuticals to treat your patients. You might work  at a clinic, supervise a starship's medbay, serve as a military  medic, or ply |
| 4 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/2` | 0.474131 | You've spent years performing  arduous physical labor. It  was a difficult life, but you  survived. You may have  embraced adventuring  as an easier method to  make your way in the  world, or you migh |
| 5 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/35` | 0.469132 | You're trained in the Crafting skill and the Augmentation  Lore skill. You gain the Augmented Body feat. |
| 6 | `PZO22001 Starfinder Player Core 092-097::/page/0/Text/12` | 0.452269 | You've strengthened your body through practice drills and  workouts, making sure not to waste a single drop of sweat  in your quest for gains. You might be a champion fighting  in arena matches, a har |
| 7 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/21` | 0.416699 | You are incredibly knowledgeable, skilled, and perhaps even  trained to teach children and adults about the world and  its wonders. From books to classes, you're committed to  imparting knowledge to a |
| 8 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/28` | 0.407012 | You work in a lab and conduct research about a scientific  topic. Perhaps you're a biotechnician, chemist, computer  programmer, theoretical physicist, or accomplished  researcher in some other field. |
| 9 | `PZO22001 Starfinder Player Core 092-097::/page/0/Text/7` | 0.399063 | Your art is your greatest passion, whatever form it takes.  Adventuring might help you find inspiration for your  creations, or simply be a way to survive until you become a  world-famous artist. |
| 10 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/28` | 0.389690 | You're trained in the Crafting skill and the Augmentation or  Life Science Lore skill. You gain the Serum Crafting skill feat. |

### Query 42
- Text: What is the rule about Choose two attribute boosts. One must be to Strength or  Constitution, and one is a free attribute boost.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 092-097::/page/1/Text/34']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 092-097::/page/1/Text/9', 'PZO22001 Starfinder Player Core 092-097::/page/1/Text/34', 'PZO22001 Starfinder Player Core 092-097::/page/3/Text/4']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/9` | 0.946647 | Choose two attribute boosts. One must be to Strength or  Constitution, and one is a free attribute boost. |
| 2 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/34` | 0.946647 | Choose two attribute boosts. One must be to Strength or  Constitution, and one is a free attribute boost. |
| 3 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/4` | 0.946647 | Choose two attribute boosts. One must be to  Strength or Constitution, and one is a free attribute boost. |
| 4 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/35` | 0.904647 | Choose two attribute boosts. One must be to Strength or  Constitution, and one is a free attribute boost. |
| 5 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/16` | 0.904647 | Choose two attribute boosts. One must be to Strength or  Constitution, and one is a free attribute boost. |
| 6 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/5` | 0.904647 | Choose two attribute boosts. One must be to Strength or  Constitution, and one is a free attribute boost. |
| 7 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/27` | 0.831322 | Choose two attribute boosts. One must be to Strength or  Intelligence, and one is a free attribute boost. |
| 8 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/8` | 0.824293 | Choose two attribute boosts. One must be to Strength or  Wisdom, and one is a free attribute boost. |
| 9 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/25` | 0.805547 | Choose two attribute boosts. One must be to Constitution  or Wisdom, and one is a free attribute boost. |
| 10 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/11` | 0.805371 | Choose two attribute boosts. One must be to Strength or  Dexterity, and one is a free attribute boost. |

### Query 43
- Text: What is the rule about You're trained in the Crafting skill and the Augmentation  Lore skill. You gain the Augmented Body feat.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 092-097::/page/1/Text/35']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 092-097::/page/1/Text/35', 'PZO22001 Starfinder Player Core 092-097::/page/2/Text/28', 'PZO22001 Starfinder Player Core 092-097::/page/0/Text/9']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/35` | 0.968069 | You're trained in the Crafting skill and the Augmentation  Lore skill. You gain the Augmented Body feat. |
| 2 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/28` | 0.818635 | You're trained in the Crafting skill and the Augmentation or  Life Science Lore skill. You gain the Serum Crafting skill feat. |
| 3 | `PZO22001 Starfinder Player Core 092-097::/page/0/Text/9` | 0.758469 | You're trained in the Crafting skill and the Art Lore skill.  You gain the Specialty Crafting skill feat. |
| 4 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/30` | 0.674445 | You're trained in the Crafting skill and a Lore skill related  to your field of research. You gain the Assurance skill feat  with that Lore skill. |
| 5 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/16` | 0.672042 | You're trained in the Crafting skill and the Physical  Science Lore skill. You gain the Electrical Engineer skill feat. |
| 6 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/22` | 0.631170 | You're trained in the deity's listed divine skill and gain the  Assurance feat with that skill. You are also trained in a Lore  skill related to your deity (Abadar Lore, for example). |
| 7 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/8` | 0.613267 | You're trained in the Medicine skill and the Life Science  Lore skill. You gain the Battle Medicine skill feat. |
| 8 | `PZO22001 Starfinder Player Core 092-097::/page/0/Text/3` | 0.589932 | At 1st level, when you create your character, you gain a  background of your choice. This decision is permanent;  you can't change it at later levels. Each background listed  here grants two boosts, u |
| 9 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/13` | 0.586013 | You're trained in the Intimidation skill and the Underworld  Lore skill. You gain the Intimidating Shot skill feat. |
| 10 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/2` | 0.573698 | You're trained in the Athletics skill and the Sports Lore  skill. You gain the Deadlift skill feat. |

### Query 44
- Text: What is the rule about **DETECTIVE** **BACKGROUND**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 092-097::/page/1/SectionHeader/36']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 092-097::/page/1/SectionHeader/36', 'PZO22001 Starfinder Player Core 092-097::/page/2/Text/1', 'PZO22001 Starfinder Player Core 092-097::/page/3/Text/23']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 092-097::/page/1/SectionHeader/36` | 0.891366 | **DETECTIVE** **BACKGROUND** |
| 2 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/1` | 0.683269 | **DISCIPLE** **BACKGROUND** |
| 3 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/23` | 0.598669 | **RECLUSE** **BACKGROUND** |
| 4 | `PZO22001 Starfinder Player Core 092-097::/page/1/SectionHeader/23` | 0.509795 | **COOK** **BACKGROUND** |
| 5 | `PZO22001 Starfinder Player Core 092-097::/page/2/SectionHeader/37` | 0.508634 | **ICON** **BACKGROUND** |
| 6 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/57` | 0.506156 | **Backgrounds** |
| 7 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/34` | 0.506156 | **Backgrounds** |
| 8 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/27` | 0.500237 | **SCIENTIST** **BACKGROUND** |
| 9 | `PZO22001 Starfinder Player Core 092-097::/page/2/SectionHeader/5` | 0.495566 | **DOCTOR** **BACKGROUND** |
| 10 | `PZO22001 Starfinder Player Core 092-097::/page/0/SectionHeader/11` | 0.484815 | **ATHLETE** **BACKGROUND** |

### Query 45
- Text: Summarize You solved crimes as a police inspector or took clandestine  jobs for various clients as a private investigator. You might  have become an adventurer as part of your next big mystery,  but it's equally likely it was due to the consequences or  aftermath of a prior case.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 092-097::/page/1/Text/37']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 092-097::/page/1/Text/37', 'PZO22001 Starfinder Player Core 092-097::/page/2/Text/22', 'PZO22001 Starfinder Player Core 092-097::/page/3/Text/11']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/37` | 1.042783 | You solved crimes as a police inspector or took clandestine  jobs for various clients as a private investigator. You might  have become an adventurer as part of your next big mystery,  but it's equall |
| 2 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/22` | 0.608504 | The thrill of the win drew you into games of chance.  This might have been a lucrative pastime that paled in  comparison to the real risks of adventuring, or you might  have fallen on hard times due t |
| 3 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/11` | 0.595375 | You're a career criminal with a nasty reputation. Perhaps  unfair circumstances forced you into a life of crime, or maybe  you enjoy the thrill you get from pulling off a heist or living  through a sh |
| 4 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/2` | 0.550446 | You've spent years performing  arduous physical labor. It  was a difficult life, but you  survived. You may have  embraced adventuring  as an easier method to  make your way in the  world, or you migh |
| 5 | `PZO22001 Starfinder Player Core 092-097::/page/0/Text/1` | 0.543359 | Your character's abilities don't spring into existence the moment they take up the adventuring life. Their background—the role they had before they became an adventurer—also provides a number of  abil |
| 6 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/30` | 0.525618 | You're a con artist and trickster who swindles unsuspecting  dupes and blackmails rubes, but it's nothing personal you're just in it for the credits. You might run an operation  on the side, or you mi |
| 7 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/16` | 0.519236 | You know how to remove all traces of a crime. Whether you  worked under the table for legitimate clients like AbadarCorp  or learned your trade working for shady organizations and  crime bosses, you k |
| 8 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/15` | 0.509346 | You've been imprisoned or punished for a crime, whether  you were guilty or not. Now that your sentence has ended  or you've escaped, you take full advantage of the newfound  freedom of your adventuri |
| 9 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/24` | 0.503408 | You used to be someone, but that was in another life. You keep  to yourself these days, eking out an existence as a hermit in  the wilderness or a loner in a rundown neighborhood. You  thought you put |
| 10 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/21` | 0.503127 | You are incredibly knowledgeable, skilled, and perhaps even  trained to teach children and adults about the world and  its wonders. From books to classes, you're committed to  imparting knowledge to a |

### Query 46
- Text: What is the rule about Choose two attribute boosts. One must be to Intelligence  or Wisdom, and one is a free attribute boost.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 092-097::/page/1/Text/38']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 092-097::/page/3/Text/29', 'PZO22001 Starfinder Player Core 092-097::/page/4/Text/22', 'PZO22001 Starfinder Player Core 092-097::/page/1/Text/38']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/29` | 0.949960 | Choose two attribute boosts. One must be to Intelligence  or Wisdom, and one is a free attribute boost. |
| 2 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/22` | 0.949960 | Choose two attribute boosts. One must be to Intelligence  or Wisdom, and one is a free attribute boost. |
| 3 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/38` | 0.949960 | Choose two attribute boosts. One must be to Intelligence  or Wisdom, and one is a free attribute boost. |
| 4 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/27` | 0.841468 | Choose two attribute boosts. One must be to Strength or  Intelligence, and one is a free attribute boost. |
| 5 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/8` | 0.835328 | Choose two attribute boosts. One must be to Strength or  Wisdom, and one is a free attribute boost. |
| 6 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/7` | 0.823527 | Choose two attribute boosts. One must be to Intelligence  or Charisma, and one is a free attribute boost. |
| 7 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/31` | 0.823527 | Choose two attribute boosts. One must be to Intelligence  or Charisma, and one is a free attribute boost. |
| 8 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/42` | 0.823527 | Choose two attribute boosts. One must be to Intelligence  or Charisma, and one is a free attribute boost. |
| 9 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/29` | 0.823527 | Choose two attribute boosts. One must be to Intelligence  or Charisma, and one is a free attribute boost. |
| 10 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/19` | 0.823527 | Choose two attribute boosts. One must be to Intelligence  or Charisma, and one is a free attribute boost. |

### Query 47
- Text: What is the rule about You're trained in the Society skill and the Underworld  Lore skill. You gain the Streetwise skill feat.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 092-097::/page/1/Text/39']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 092-097::/page/1/Text/39', 'PZO22001 Starfinder Player Core 092-097::/page/4/Text/31', 'PZO22001 Starfinder Player Core 092-097::/page/2/Text/20']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/39` | 0.973917 | You're trained in the Society skill and the Underworld  Lore skill. You gain the Streetwise skill feat. |
| 2 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/31` | 0.735530 | You're trained in the Society skill and the History Lore  skill. You gain the Dubious Knowledge skill feat. |
| 3 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/20` | 0.733666 | You're trained in the Society skill and a Lore skill related  to one city or region you've visited often. You gain the  Multilingual skill feat. |
| 4 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/30` | 0.676551 | You're trained in the Society skill and the Corporate Lore  skill. You gain the Management Material skill feat. |
| 5 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/23` | 0.666847 | You're trained in your choice of either the Performance or  Society skill, as well as the Academia Lore skill. You gain the  Experienced Professional skill feat. |
| 6 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/20` | 0.658203 | You're trained in the Survival skill and a Lore skill about a  specific settlement. You gain the Urban Survivalist skill feat. |
| 7 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/8` | 0.644676 | You're trained in the Society skill and a Lore skill related  to your home planet. You gain the Plant Rumor skill feat. |
| 8 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/18` | 0.640033 | You're trained in the Deception skill and Underworld Lore  skill. You gain the Without a Trace skill feat. |
| 9 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/6` | 0.637013 | You're trained in the Survival skill and the Underworld Lore  skill. You gain the Experienced Tracker skill feat. |
| 10 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/12` | 0.625628 | You're trained in the Occultism skill and a Lore skill  related to your choice of metaphysical topics. You gain the  Schooled in Secrets skill feat. |

### Query 48
- Text: What is the rule about **DIPLOMAT** **BACKGROUND**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 092-097::/page/1/SectionHeader/40']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 092-097::/page/1/SectionHeader/40', 'PZO22001 Starfinder Player Core 092-097::/page/2/Text/1', 'PZO22001 Starfinder Player Core 092-097::/page/3/Text/23']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 092-097::/page/1/SectionHeader/40` | 0.913049 | **DIPLOMAT** **BACKGROUND** |
| 2 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/1` | 0.658738 | **DISCIPLE** **BACKGROUND** |
| 3 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/23` | 0.547521 | **RECLUSE** **BACKGROUND** |
| 4 | `PZO22001 Starfinder Player Core 092-097::/page/2/SectionHeader/5` | 0.499480 | **DOCTOR** **BACKGROUND** |
| 5 | `PZO22001 Starfinder Player Core 092-097::/page/1/SectionHeader/36` | 0.485322 | **DETECTIVE** **BACKGROUND** |
| 6 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/57` | 0.470571 | **Backgrounds** |
| 7 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/34` | 0.470571 | **Backgrounds** |
| 8 | `PZO22001 Starfinder Player Core 092-097::/page/0/SectionHeader/11` | 0.467953 | **ATHLETE** **BACKGROUND** |
| 9 | `PZO22001 Starfinder Player Core 092-097::/page/2/SectionHeader/37` | 0.464717 | **ICON** **BACKGROUND** |
| 10 | `PZO22001 Starfinder Player Core 092-097::/page/1/SectionHeader/19` | 0.458181 | **COMEDIAN** **BACKGROUND** |

### Query 49
- Text: What is the rule about You've dedicated your career to facilitating peaceful  alliances between different factions and peoples. You might  work at an intergalactic embassy or travel aboard a starship  on a mission to remote space. First contact situations are  your specialty.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 092-097::/page/1/Text/41']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 092-097::/page/1/Text/41', 'PZO22001 Starfinder Player Core 092-097::/page/2/Text/18', 'PZO22001 Starfinder Player Core 092-097::/page/4/Text/10']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/41` | 0.964571 | You've dedicated your career to facilitating peaceful  alliances between different factions and peoples. You might  work at an intergalactic embassy or travel aboard a starship  on a mission to remote |
| 2 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/18` | 0.663073 | As a diplomat or messenger, you traveled extensively,  communicating with new people and brokering alliances  wherever you went. |
| 3 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/10` | 0.616112 | You're a crewmate on a pirate vessel with ambitions of  pillaging interstellar shipping lanes or taking over a chunk  of a notable planetary body. Perhaps you grew up on such  a ship, were taken priso |
| 4 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/28` | 0.554870 | You work in a lab and conduct research about a scientific  topic. Perhaps you're a biotechnician, chemist, computer  programmer, theoretical physicist, or accomplished  researcher in some other field. |
| 5 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/14` | 0.541808 | Some people might say you've been out in the Drift too long,  but the truth is, you don't feel at home away from your post  on a starship deck. You might crew a long-haul freighter,  military gunship, |
| 6 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/6` | 0.532200 | You're an accomplished healer expertly using the latest tech  and pharmaceuticals to treat your patients. You might work  at a clinic, supervise a starship's medbay, serve as a military  medic, or ply |
| 7 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/2` | 0.519644 | You've spent years performing  arduous physical labor. It  was a difficult life, but you  survived. You may have  embraced adventuring  as an easier method to  make your way in the  world, or you migh |
| 8 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/28` | 0.507507 | You're one among many professionals working in the  corporate world, but you're not just any suit. You're a  negotiator, dealmaker, or perhaps even a spy working to  advance a particular corporation's |
| 9 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/2` | 0.493000 | You're a loyal disciple of a particular deity. You might have  been raised in a religious culture or perhaps felt a kindred  calling toward a god later in life, but you've honed your skills  and devot |
| 10 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/34` | 0.491729 | You've always had a knack for computers and virtual spaces  and pride yourself on your ability to learn technical secrets.  The open networks known as infospheres are your home  and the place you can |

### Query 50
- Text: What is the rule about Choose two attribute boosts. One must be to Intelligence  or Charisma, and one is a free attribute boost.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 092-097::/page/1/Text/42']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 092-097::/page/1/Text/42', 'PZO22001 Starfinder Player Core 092-097::/page/1/Text/29', 'PZO22001 Starfinder Player Core 092-097::/page/4/Text/7']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/42` | 0.947131 | Choose two attribute boosts. One must be to Intelligence  or Charisma, and one is a free attribute boost. |
| 2 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/29` | 0.947131 | Choose two attribute boosts. One must be to Intelligence  or Charisma, and one is a free attribute boost. |
| 3 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/7` | 0.947131 | Choose two attribute boosts. One must be to Intelligence  or Charisma, and one is a free attribute boost. |
| 4 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/19` | 0.905131 | Choose two attribute boosts. One must be to Intelligence  or Charisma, and one is a free attribute boost. |
| 5 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/31` | 0.905131 | Choose two attribute boosts. One must be to Intelligence  or Charisma, and one is a free attribute boost. |
| 6 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/22` | 0.843184 | Choose two attribute boosts. One must be to Intelligence  or Wisdom, and one is a free attribute boost. |
| 7 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/38` | 0.843184 | Choose two attribute boosts. One must be to Intelligence  or Wisdom, and one is a free attribute boost. |
| 8 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/29` | 0.843184 | Choose two attribute boosts. One must be to Intelligence  or Wisdom, and one is a free attribute boost. |
| 9 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/21` | 0.841134 | Choose two attribute boosts. One must be to Wisdom or  Charisma, and one is a free attribute boost. |
| 10 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/11` | 0.841134 | Choose two attribute boosts. One must be to Wisdom or  Charisma, and one is a free attribute boost. |

### Query 51
- Text: What is the rule about You're trained in the Diplomacy skill and one Lore skill for  a planet of your choosing. You gain the Group Impression  skill feat.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 092-097::/page/1/Text/43']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 092-097::/page/1/Text/43', 'PZO22001 Starfinder Player Core 092-097::/page/4/Text/12', 'PZO22001 Starfinder Player Core 092-097::/page/4/Text/8']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/43` | 0.974973 | You're trained in the Diplomacy skill and one Lore skill for  a planet of your choosing. You gain the Group Impression  skill feat. |
| 2 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/12` | 0.694461 | You're trained in the Intimidation skill and the Piracy Lore  skill. You gain the Group Coercion skill feat. |
| 3 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/8` | 0.683990 | You're trained in the Society skill and a Lore skill related  to your home planet. You gain the Plant Rumor skill feat. |
| 4 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/20` | 0.619268 | You're trained in the Society skill and a Lore skill related  to one city or region you've visited often. You gain the  Multilingual skill feat. |
| 5 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/40` | 0.614000 | You're trained in the Performance skill and the Media Lore  skill. You gain the Impressive Performance skill feat. |
| 6 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/13` | 0.607634 | You're trained in the Intimidation skill and the Underworld  Lore skill. You gain the Intimidating Shot skill feat. |
| 7 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/14` | 0.603752 | You're trained in the Deception skill and a Lore skill about a  specific settlement. You gain the Face in the Crowd skill feat. |
| 8 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/23` | 0.600493 | You're trained in your choice of either the Performance or  Society skill, as well as the Academia Lore skill. You gain the  Experienced Professional skill feat. |
| 9 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/31` | 0.598281 | You're trained in the Society skill and the History Lore  skill. You gain the Dubious Knowledge skill feat. |
| 10 | `PZO22001 Starfinder Player Core 092-097::/page/0/Text/3` | 0.590472 | At 1st level, when you create your character, you gain a  background of your choice. This decision is permanent;  you can't change it at later levels. Each background listed  here grants two boosts, u |

### Query 52
- Text: Summarize **INTRODUCTION**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 092-097::/page/1/Text/45']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 092-097::/page/5/Text/20', 'PZO22001 Starfinder Player Core 092-097::/page/1/Text/45', 'PZO22001 Starfinder Player Core 092-097::/page/3/Text/32']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/20` | 0.880541 | **INTRODUCTION** |
| 2 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/45` | 0.880541 | **INTRODUCTION** |
| 3 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/32` | 0.880541 | **INTRODUCTION** |
| 4 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/1` | 0.582365 | **DISCIPLE** **BACKGROUND** |
| 5 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/54` | 0.524467 | **INDEX** |
| 6 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/58` | 0.460996 | **Languages** |
| 7 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/35` | 0.460996 | **Languages** |
| 8 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/42` | 0.460996 | **Languages** |
| 9 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/23` | 0.456302 | **RECLUSE** **BACKGROUND** |
| 10 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/53` | 0.452320 | **GAME** |

### Query 53
- Text: What is the rule about **ANCESTRIES & ** **BACKGROUNDS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 092-097::/page/1/Text/46']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 092-097::/page/5/Text/21', 'PZO22001 Starfinder Player Core 092-097::/page/1/Text/46', 'PZO22001 Starfinder Player Core 092-097::/page/3/Text/33']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/21` | 0.920820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 2 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/46` | 0.920820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 3 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/33` | 0.920820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 4 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/1` | 0.576082 | **DISCIPLE** **BACKGROUND** |
| 5 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/57` | 0.526957 | **Backgrounds** |
| 6 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/34` | 0.526957 | **Backgrounds** |
| 7 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/23` | 0.526510 | **RECLUSE** **BACKGROUND** |
| 8 | `PZO22001 Starfinder Player Core 092-097::/page/1/SectionHeader/23` | 0.490241 | **COOK** **BACKGROUND** |
| 9 | `PZO22001 Starfinder Player Core 092-097::/page/5/SectionHeader/6` | 0.484311 | **COMMON ANCESTRY LANGUAGES** |
| 10 | `PZO22001 Starfinder Player Core 092-097::/page/0/SectionHeader/6` | 0.483042 | **ARTIST** **BACKGROUND** |

### Query 54
- Text: Summarize **Android**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 092-097::/page/1/Text/47']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 092-097::/page/5/Text/22', 'PZO22001 Starfinder Player Core 092-097::/page/1/Text/47', 'PZO22001 Starfinder Player Core 092-097::/page/3/Text/34']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/22` | 0.780963 | **Android** |
| 2 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/47` | 0.780963 | **Android** |
| 3 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/34` | 0.780963 | **Android** |
| 4 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/53` | 0.380135 | **GAME** |
| 5 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/58` | 0.366971 | **Languages** |
| 6 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/35` | 0.366971 | **Languages** |
| 7 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/42` | 0.366971 | **Languages** |
| 8 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/20` | 0.356045 | **INTRODUCTION** |
| 9 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/45` | 0.356045 | **INTRODUCTION** |
| 10 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/32` | 0.356045 | **INTRODUCTION** |

### Query 55
- Text: Summarize **Barathu** **Human**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 092-097::/page/1/Text/48']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 092-097::/page/1/Text/48', 'PZO22001 Starfinder Player Core 092-097::/page/3/Text/35', 'PZO22001 Starfinder Player Core 092-097::/page/5/Text/23']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/48` | 1.011021 | **Barathu** **Human** |
| 2 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/35` | 1.011021 | **Barathu** **Human** |
| 3 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/23` | 0.865271 | **Barathu** |
| 4 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/24` | 0.594673 | **Human** |
| 5 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/32` | 0.420703 | **Heritages** **Borai** |
| 6 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/52` | 0.400708 | **Borai** |
| 7 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/49` | 0.398036 | **Kasatha** |
| 8 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/36` | 0.398036 | **Kasatha** |
| 9 | `PZO22001 Starfinder Player Core 092-097::/page/5/Table/9` | 0.388974 | LanguageSpeakersAkitonianAkiton (shobhads, ysoki)BrethedanBretheda, Liavara, and their moons (barathus, kalos, maraquoi)CastrovelianCastrovel (lashuntas and formians)DiasporanDiaspora (sarcesians)Drac |
| 10 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/25` | 0.386036 | **Kasatha** |

### Query 56
- Text: Summarize **Kasatha**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 092-097::/page/1/Text/49']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 092-097::/page/1/Text/49', 'PZO22001 Starfinder Player Core 092-097::/page/5/Text/25', 'PZO22001 Starfinder Player Core 092-097::/page/3/Text/36']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/49` | 0.982519 | **Kasatha** |
| 2 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/25` | 0.982519 | **Kasatha** |
| 3 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/36` | 0.982519 | **Kasatha** |
| 4 | `PZO22001 Starfinder Player Core 092-097::/page/5/TableCell/492` | 0.863855 | Kasatha |
| 5 | `PZO22001 Starfinder Player Core 092-097::/page/5/TableCell/493` | 0.619101 | Kasathas, inhabitants of Kasath or the Idari |
| 6 | `PZO22001 Starfinder Player Core 092-097::/page/5/Table/7` | 0.492914 | LanguageSpeakersCommonHumans, most citizens of the Pact WorldsKasathaKasathas, inhabitants of Kasath or the IdariPahtraPahtras |
| 7 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/23` | 0.396219 | **Barathu** |
| 8 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/48` | 0.395725 | **Barathu** **Human** |
| 9 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/35` | 0.395725 | **Barathu** **Human** |
| 10 | `PZO22001 Starfinder Player Core 092-097::/page/5/Table/9` | 0.372748 | LanguageSpeakersAkitonianAkiton (shobhads, ysoki)BrethedanBretheda, Liavara, and their moons (barathus, kalos, maraquoi)CastrovelianCastrovel (lashuntas and formians)DiasporanDiaspora (sarcesians)Drac |

### Query 57
- Text: Summarize **Lashunta**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 092-097::/page/1/Text/50']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 092-097::/page/1/Text/50', 'PZO22001 Starfinder Player Core 092-097::/page/5/Text/26', 'PZO22001 Starfinder Player Core 092-097::/page/3/Text/37']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/50` | 0.972315 | **Lashunta** |
| 2 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/26` | 0.972315 | **Lashunta** |
| 3 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/37` | 0.738641 | **Lashunta** **Pahtra** |
| 4 | `PZO22001 Starfinder Player Core 092-097::/page/5/TableCell/503` | 0.489374 | Castrovel (lashuntas and formians) |
| 5 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/51` | 0.368718 | **Pahtra** **Shirren** |
| 6 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/27` | 0.368718 | **Pahtra** **Shirren** |
| 7 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/48` | 0.368112 | **GLOSSARY & ** |
| 8 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/51` | 0.355168 | **Shirren** |
| 9 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/65` | 0.331878 | **GLOSSARY & ** **INDEX** |
| 10 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/42` | 0.331878 | **GLOSSARY & ** **INDEX** |

### Query 58
- Text: Summarize **Pahtra** **Shirren**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 092-097::/page/1/Text/51']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 092-097::/page/5/Text/27', 'PZO22001 Starfinder Player Core 092-097::/page/1/Text/51', 'PZO22001 Starfinder Player Core 092-097::/page/3/Text/37']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/27` | 1.005619 | **Pahtra** **Shirren** |
| 2 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/51` | 1.005619 | **Pahtra** **Shirren** |
| 3 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/37` | 0.744280 | **Lashunta** **Pahtra** |
| 4 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/51` | 0.702211 | **Shirren** |
| 5 | `PZO22001 Starfinder Player Core 092-097::/page/5/TableCell/494` | 0.645161 | Pahtra |
| 6 | `PZO22001 Starfinder Player Core 092-097::/page/5/TableCell/495` | 0.643100 | Pahtras |
| 7 | `PZO22001 Starfinder Player Core 092-097::/page/5/Table/7` | 0.438689 | LanguageSpeakersCommonHumans, most citizens of the Pact WorldsKasathaKasathas, inhabitants of Kasath or the IdariPahtraPahtras |
| 8 | `PZO22001 Starfinder Player Core 092-097::/page/5/Table/9` | 0.393570 | LanguageSpeakersAkitonianAkiton (shobhads, ysoki)BrethedanBretheda, Liavara, and their moons (barathus, kalos, maraquoi)CastrovelianCastrovel (lashuntas and formians)DiasporanDiaspora (sarcesians)Drac |
| 9 | `PZO22001 Starfinder Player Core 092-097::/page/5/TableCell/515` | 0.365138 | Pulonis, the Veskarium (pahtras, vesk) |
| 10 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/36` | 0.353474 | **Kasatha** |

### Query 59
- Text: Summarize **Skittermander**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 092-097::/page/1/Text/52']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 092-097::/page/1/Text/52', 'PZO22001 Starfinder Player Core 092-097::/page/5/Text/28', 'PZO22001 Starfinder Player Core 092-097::/page/5/Text/43']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/52` | 0.984124 | **Skittermander** |
| 2 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/28` | 0.984124 | **Skittermander** |
| 3 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/43` | 0.374756 | **CHARACTER ** **SHEET** |
| 4 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/66` | 0.332756 | **CHARACTER ** **SHEET** |
| 5 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/49` | 0.332756 | **CHARACTER ** **SHEET** |
| 6 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/51` | 0.331107 | **Shirren** |
| 7 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/33` | 0.328981 | **Prismeni** |
| 8 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/56` | 0.314073 | **Borai** **Prismeni** |
| 9 | `PZO22001 Starfinder Player Core 092-097::/page/5/TableCell/500` | 0.304495 | Brethedan |
| 10 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/51` | 0.303718 | **Pahtra** **Shirren** |

### Query 60
- Text: Summarize **Vesk**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 092-097::/page/1/Text/53']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 092-097::/page/1/Text/53', 'PZO22001 Starfinder Player Core 092-097::/page/3/Text/38', 'PZO22001 Starfinder Player Core 092-097::/page/5/Text/29']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/53` | 0.943397 | **Vesk** |
| 2 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/38` | 0.943397 | **Vesk** |
| 3 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/29` | 0.943397 | **Vesk** |
| 4 | `PZO22001 Starfinder Player Core 092-097::/page/5/TableCell/514` | 0.807644 | Vesk |
| 5 | `PZO22001 Starfinder Player Core 092-097::/page/5/TableCell/515` | 0.552234 | Pulonis, the Veskarium (pahtras, vesk) |
| 6 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/36` | 0.367531 | **Kasatha** |
| 7 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/49` | 0.367531 | **Kasatha** |
| 8 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/25` | 0.367531 | **Kasatha** |
| 9 | `PZO22001 Starfinder Player Core 092-097::/page/5/Table/9` | 0.346223 | LanguageSpeakersAkitonianAkiton (shobhads, ysoki)BrethedanBretheda, Liavara, and their moons (barathus, kalos, maraquoi)CastrovelianCastrovel (lashuntas and formians)DiasporanDiaspora (sarcesians)Drac |
| 10 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/54` | 0.339943 | **INDEX** |

### Query 61
- Text: Summarize **Ysoki**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 092-097::/page/1/Text/54']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 092-097::/page/5/Text/30', 'PZO22001 Starfinder Player Core 092-097::/page/3/Text/39', 'PZO22001 Starfinder Player Core 092-097::/page/1/Text/54']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/30` | 0.934336 | **Ysoki** |
| 2 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/39` | 0.934336 | **Ysoki** |
| 3 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/54` | 0.934336 | **Ysoki** |
| 4 | `PZO22001 Starfinder Player Core 092-097::/page/5/TableCell/499` | 0.515883 | Akiton (shobhads, ysoki) |
| 5 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/42` | 0.383117 | **Languages** |
| 6 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/58` | 0.383117 | **Languages** |
| 7 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/35` | 0.383117 | **Languages** |
| 8 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/54` | 0.366194 | **INDEX** |
| 9 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/20` | 0.364466 | **INTRODUCTION** |
| 10 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/45` | 0.364466 | **INTRODUCTION** |

### Query 62
- Text: Summarize **Versatile ** **Heritages**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 092-097::/page/1/Text/55']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 092-097::/page/1/Text/55', 'PZO22001 Starfinder Player Core 092-097::/page/3/Text/40', 'PZO22001 Starfinder Player Core 092-097::/page/5/Text/31']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/55` | 0.959353 | **Versatile ** **Heritages** |
| 2 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/40` | 0.959353 | **Versatile ** **Heritages** |
| 3 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/31` | 0.670755 | **Versatile ** |
| 4 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/32` | 0.510696 | **Heritages** **Borai** |
| 5 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/34` | 0.419632 | **Backgrounds** |
| 6 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/57` | 0.419632 | **Backgrounds** |
| 7 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/1` | 0.398140 | **DISCIPLE** **BACKGROUND** |
| 8 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/46` | 0.397026 | **ANCESTRIES & ** **BACKGROUNDS** |
| 9 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/21` | 0.397026 | **ANCESTRIES & ** **BACKGROUNDS** |
| 10 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/33` | 0.397026 | **ANCESTRIES & ** **BACKGROUNDS** |

### Query 63
- Text: Summarize **Borai** **Prismeni**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 092-097::/page/1/Text/56']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 092-097::/page/1/Text/56', 'PZO22001 Starfinder Player Core 092-097::/page/3/Text/52', 'PZO22001 Starfinder Player Core 092-097::/page/5/Text/32']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/56` | 1.000180 | **Borai** **Prismeni** |
| 2 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/52` | 0.802444 | **Borai** |
| 3 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/32` | 0.758148 | **Heritages** **Borai** |
| 4 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/33` | 0.671637 | **Prismeni** |
| 5 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/41` | 0.639687 | **Prismeni** **Backgrounds** |
| 6 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/48` | 0.386347 | **Barathu** **Human** |
| 7 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/35` | 0.386347 | **Barathu** **Human** |
| 8 | `PZO22001 Starfinder Player Core 092-097::/page/5/Table/9` | 0.376025 | LanguageSpeakersAkitonianAkiton (shobhads, ysoki)BrethedanBretheda, Liavara, and their moons (barathus, kalos, maraquoi)CastrovelianCastrovel (lashuntas and formians)DiasporanDiaspora (sarcesians)Drac |
| 9 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/23` | 0.373902 | **Barathu** |
| 10 | `PZO22001 Starfinder Player Core 092-097::/page/5/TableCell/513` | 0.318741 | Verces (verthani) |

### Query 64
- Text: What is the rule about **Backgrounds**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 092-097::/page/1/Text/57']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 092-097::/page/1/Text/57', 'PZO22001 Starfinder Player Core 092-097::/page/5/Text/34', 'PZO22001 Starfinder Player Core 092-097::/page/2/Text/1']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/57` | 0.796516 | **Backgrounds** |
| 2 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/34` | 0.796516 | **Backgrounds** |
| 3 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/1` | 0.615403 | **DISCIPLE** **BACKGROUND** |
| 4 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/41` | 0.566542 | **Prismeni** **Backgrounds** |
| 5 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/23` | 0.536638 | **RECLUSE** **BACKGROUND** |
| 6 | `PZO22001 Starfinder Player Core 092-097::/page/2/SectionHeader/37` | 0.531519 | **ICON** **BACKGROUND** |
| 7 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/46` | 0.510451 | **ANCESTRIES & ** **BACKGROUNDS** |
| 8 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/33` | 0.510451 | **ANCESTRIES & ** **BACKGROUNDS** |
| 9 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/21` | 0.510451 | **ANCESTRIES & ** **BACKGROUNDS** |
| 10 | `PZO22001 Starfinder Player Core 092-097::/page/0/SectionHeader/6` | 0.504301 | **ARTIST** **BACKGROUND** |

### Query 65
- Text: Summarize **Languages**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 092-097::/page/1/Text/58']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 092-097::/page/5/Text/35', 'PZO22001 Starfinder Player Core 092-097::/page/1/Text/58', 'PZO22001 Starfinder Player Core 092-097::/page/3/Text/42']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/35` | 0.876251 | **Languages** |
| 2 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/58` | 0.876251 | **Languages** |
| 3 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/42` | 0.876251 | **Languages** |
| 4 | `PZO22001 Starfinder Player Core 092-097::/page/5/SectionHeader/0` | 0.622405 | LANGUAGES |
| 5 | `PZO22001 Starfinder Player Core 092-097::/page/5/TableCell/516` | 0.562137 | Language |
| 6 | `PZO22001 Starfinder Player Core 092-097::/page/5/TableCell/496` | 0.562137 | Language |
| 7 | `PZO22001 Starfinder Player Core 092-097::/page/5/TableCell/488` | 0.562137 | Language |
| 8 | `PZO22001 Starfinder Player Core 092-097::/page/5/SectionHeader/8` | 0.542038 | **COMMON REGIONAL LANGUAGES** |
| 9 | `PZO22001 Starfinder Player Core 092-097::/page/5/SectionHeader/12` | 0.506057 | REGIONAL LANGUAGES |
| 10 | `PZO22001 Starfinder Player Core 092-097::/page/5/SectionHeader/6` | 0.452126 | **COMMON ANCESTRY LANGUAGES** |

### Query 66
- Text: Summarize **CLASSES**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 092-097::/page/1/Text/59']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 092-097::/page/1/Text/59', 'PZO22001 Starfinder Player Core 092-097::/page/5/Text/36', 'PZO22001 Starfinder Player Core 092-097::/page/3/Text/43']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/59` | 0.940061 | **CLASSES** |
| 2 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/36` | 0.940061 | **CLASSES** |
| 3 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/43` | 0.749499 | **CLASSES** **SKILLS** |
| 4 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/42` | 0.481450 | **Languages** |
| 5 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/58` | 0.481450 | **Languages** |
| 6 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/35` | 0.481450 | **Languages** |
| 7 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/54` | 0.463681 | **INDEX** |
| 8 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/32` | 0.435377 | **INTRODUCTION** |
| 9 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/20` | 0.435377 | **INTRODUCTION** |
| 10 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/45` | 0.435377 | **INTRODUCTION** |

### Query 67
- Text: What is the rule about **SKILLS** **FEATS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 092-097::/page/1/Text/60']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 092-097::/page/1/Text/60', 'PZO22001 Starfinder Player Core 092-097::/page/5/Text/37', 'PZO22001 Starfinder Player Core 092-097::/page/3/Text/43']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/60` | 0.909736 | **SKILLS** **FEATS** |
| 2 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/37` | 0.909736 | **SKILLS** **FEATS** |
| 3 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/43` | 0.658394 | **CLASSES** **SKILLS** |
| 4 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/44` | 0.625813 | **FEATS** |
| 5 | `PZO22001 Starfinder Player Core 092-097::/page/0/Text/4` | 0.411947 | Lore skills represent deep knowledge of a specific subject  and are described on page 200. If a Lore skill involves a choice  (for instance, a choice of metaphysical topics), explain your  preference |
| 6 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/4` | 0.410572 | You're trained in the deity's listed divine skill and a Lore  skill related to your deity (Abadar Lore, for example). You  gain the Religious Talisman skill feat even if you do not meet  the feat's pr |
| 7 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/22` | 0.399506 | You're trained in the deity's listed divine skill and gain the  Assurance feat with that skill. You are also trained in a Lore  skill related to your deity (Abadar Lore, for example). |
| 8 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/12` | 0.399003 | You're trained in the Occultism skill and a Lore skill  related to your choice of metaphysical topics. You gain the  Schooled in Secrets skill feat. |
| 9 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/16` | 0.384929 | You might know the signed languages associated with the  languages you know, or how to read lips. You can learn  these by taking the Sign Language or Read Lips skill feats,  or both. If you are creati |
| 10 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/26` | 0.378975 | You're trained in the Survival skill and the Cooking Lore  skill. You gain the Seasoned skill feat. |

### Query 68
- Text: Summarize **EQUIPMENT**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 092-097::/page/1/Text/61']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 092-097::/page/5/Text/38', 'PZO22001 Starfinder Player Core 092-097::/page/3/Text/45', 'PZO22001 Starfinder Player Core 092-097::/page/1/Text/61']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/38` | 0.944726 | **EQUIPMENT** |
| 2 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/45` | 0.944726 | **EQUIPMENT** |
| 3 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/61` | 0.944726 | **EQUIPMENT** |
| 4 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/54` | 0.421643 | **INDEX** |
| 5 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/1` | 0.412371 | **DISCIPLE** **BACKGROUND** |
| 6 | `PZO22001 Starfinder Player Core 092-097::/page/4/SectionHeader/24` | 0.407946 | **TECH SUPPORT** **BACKGROUND** |
| 7 | `PZO22001 Starfinder Player Core 092-097::/page/0/SectionHeader/11` | 0.407588 | **ATHLETE** **BACKGROUND** |
| 8 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/45` | 0.385549 | **INTRODUCTION** |
| 9 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/20` | 0.385549 | **INTRODUCTION** |
| 10 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/32` | 0.385549 | **INTRODUCTION** |

### Query 69
- Text: What is the rule about **SPELLS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 092-097::/page/1/Text/62']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 092-097::/page/1/Text/62', 'PZO22001 Starfinder Player Core 092-097::/page/5/Text/39', 'PZO22001 Starfinder Player Core 092-097::/page/3/Text/46']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/62` | 0.889304 | **SPELLS** |
| 2 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/39` | 0.889303 | **SPELLS** |
| 3 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/46` | 0.782791 | **SPELLS** **PLAYING THE ** |
| 4 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/43` | 0.376551 | **CLASSES** **SKILLS** |
| 5 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/37` | 0.332025 | **SKILLS** **FEATS** |
| 6 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/60` | 0.332025 | **SKILLS** **FEATS** |
| 7 | `PZO22001 Starfinder Player Core 092-097::/page/2/SectionHeader/25` | 0.302508 | **GENE SPLICER** **BACKGROUND** |
| 8 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/1` | 0.280933 | **DISCIPLE** **BACKGROUND** |
| 9 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/63` | 0.277596 | **PLAYING THE ** **GAME** |
| 10 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/40` | 0.277596 | **PLAYING THE ** **GAME** |

### Query 70
- Text: Summarize **PLAYING THE ** **GAME**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 092-097::/page/1/Text/63']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 092-097::/page/5/Text/40', 'PZO22001 Starfinder Player Core 092-097::/page/1/Text/63', 'PZO22001 Starfinder Player Core 092-097::/page/3/Text/53']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/40` | 0.965000 | **PLAYING THE ** **GAME** |
| 2 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/63` | 0.965000 | **PLAYING THE ** **GAME** |
| 3 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/53` | 0.705024 | **GAME** |
| 4 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/46` | 0.576670 | **SPELLS** **PLAYING THE ** |
| 5 | `PZO22001 Starfinder Player Core 092-097::/page/1/SectionHeader/7` | 0.466675 | **BRUTARIS PLAYER** **BACKGROUND** |
| 6 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/20` | 0.418586 | **INTRODUCTION** |
| 7 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/45` | 0.418586 | **INTRODUCTION** |
| 8 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/32` | 0.418586 | **INTRODUCTION** |
| 9 | `PZO22001 Starfinder Player Core 092-097::/page/2/SectionHeader/21` | 0.416541 | **GAMBLER** **BACKGROUND** |
| 10 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/38` | 0.397359 | Gaming is more than just a hobby for you: it's your way of  life. Whether you're a professional player, game designer,  hobbyist influencer, or just a gamer who has mastered  every vidgame you can ins |

### Query 71
- Text: Summarize **CONDITIONS ** **APPENDIX**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 092-097::/page/1/Text/64']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 092-097::/page/3/Text/47', 'PZO22001 Starfinder Player Core 092-097::/page/1/Text/64', 'PZO22001 Starfinder Player Core 092-097::/page/5/Text/41']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/47` | 0.983499 | **CONDITIONS ** **APPENDIX** |
| 2 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/64` | 0.983499 | **CONDITIONS ** **APPENDIX** |
| 3 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/41` | 0.983499 | **CONDITIONS ** **APPENDIX** |
| 4 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/54` | 0.423722 | **INDEX** |
| 5 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/33` | 0.416141 | **ANCESTRIES & ** **BACKGROUNDS** |
| 6 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/21` | 0.416141 | **ANCESTRIES & ** **BACKGROUNDS** |
| 7 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/46` | 0.416141 | **ANCESTRIES & ** **BACKGROUNDS** |
| 8 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/1` | 0.393926 | **DISCIPLE** **BACKGROUND** |
| 9 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/23` | 0.373981 | **RECLUSE** **BACKGROUND** |
| 10 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/61` | 0.372115 | **EQUIPMENT** |

### Query 72
- Text: Summarize **GLOSSARY & ** **INDEX**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 092-097::/page/1/Text/65']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 092-097::/page/1/Text/65', 'PZO22001 Starfinder Player Core 092-097::/page/5/Text/42', 'PZO22001 Starfinder Player Core 092-097::/page/3/Text/48']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/65` | 0.993465 | **GLOSSARY & ** **INDEX** |
| 2 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/42` | 0.993465 | **GLOSSARY & ** **INDEX** |
| 3 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/48` | 0.846819 | **GLOSSARY & ** |
| 4 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/54` | 0.618357 | **INDEX** |
| 5 | `PZO22001 Starfinder Player Core 092-097::/page/2/SectionHeader/37` | 0.396646 | **ICON** **BACKGROUND** |
| 6 | `PZO22001 Starfinder Player Core 092-097::/page/2/SectionHeader/17` | 0.396429 | **EMISSARY** **BACKGROUND** |
| 7 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/59` | 0.385404 | **CLASSES** |
| 8 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/36` | 0.385404 | **CLASSES** |
| 9 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/58` | 0.373037 | **Languages** |
| 10 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/35` | 0.373037 | **Languages** |

### Query 73
- Text: What is the rule about **CHARACTER ** **SHEET**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 092-097::/page/1/Text/66']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 092-097::/page/3/Text/49', 'PZO22001 Starfinder Player Core 092-097::/page/5/Text/43', 'PZO22001 Starfinder Player Core 092-097::/page/1/Text/66']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/49` | 0.859300 | **CHARACTER ** **SHEET** |
| 2 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/43` | 0.859300 | **CHARACTER ** **SHEET** |
| 3 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/66` | 0.859300 | **CHARACTER ** **SHEET** |
| 4 | `PZO22001 Starfinder Player Core 092-097::/page/2/SectionHeader/33` | 0.381647 | **HACKER** **BACKGROUND** |
| 5 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/53` | 0.380766 | **GAME** |
| 6 | `PZO22001 Starfinder Player Core 092-097::/page/0/SectionHeader/6` | 0.363016 | **ARTIST** **BACKGROUND** |
| 7 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/24` | 0.360758 | **Human** |
| 8 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/43` | 0.359306 | **CLASSES** **SKILLS** |
| 9 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/37` | 0.357339 | **SKILLS** **FEATS** |
| 10 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/60` | 0.357339 | **SKILLS** **FEATS** |

### Query 74
- Text: Summarize You know better than most the power of electricity,  having survived several close calls yourself, and you know  firsthand how shocking it can be when something goes  wrong. Whether you learned by installing power stations or  repairing broken circuits, you're familiar with the positives  and negatives of electricity.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 092-097::/page/2/Text/14']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 092-097::/page/2/Text/14', 'PZO22001 Starfinder Player Core 092-097::/page/4/Text/21', 'PZO22001 Starfinder Player Core 092-097::/page/2/Text/34']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/14` | 1.038598 | You know better than most the power of electricity,  having survived several close calls yourself, and you know  firsthand how shocking it can be when something goes  wrong. Whether you learned by ins |
| 2 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/21` | 0.493007 | You are incredibly knowledgeable, skilled, and perhaps even  trained to teach children and adults about the world and  its wonders. From books to classes, you're committed to  imparting knowledge to a |
| 3 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/34` | 0.472407 | You've always had a knack for computers and virtual spaces  and pride yourself on your ability to learn technical secrets.  The open networks known as infospheres are your home  and the place you can |
| 4 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/25` | 0.426069 | Whether working in a military outpost, a deep space  exploration vessel, or a local office, you have experience  supporting your comrades by assisting with their tech.  While you've undoubtedly surviv |
| 5 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/16` | 0.415157 | You're trained in the Crafting skill and the Physical  Science Lore skill. You gain the Electrical Engineer skill feat. |
| 6 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/2` | 0.404389 | You've spent years performing  arduous physical labor. It  was a difficult life, but you  survived. You may have  embraced adventuring  as an easier method to  make your way in the  world, or you migh |
| 7 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/6` | 0.404055 | You're an accomplished healer expertly using the latest tech  and pharmaceuticals to treat your patients. You might work  at a clinic, supervise a starship's medbay, serve as a military  medic, or ply |
| 8 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/11` | 0.399439 | You're a career criminal with a nasty reputation. Perhaps  unfair circumstances forced you into a life of crime, or maybe  you enjoy the thrill you get from pulling off a heist or living  through a sh |
| 9 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/28` | 0.395819 | You work in a lab and conduct research about a scientific  topic. Perhaps you're a biotechnician, chemist, computer  programmer, theoretical physicist, or accomplished  researcher in some other field. |
| 10 | `PZO22001 Starfinder Player Core 092-097::/page/2/SectionHeader/13` | 0.391371 | **ELECTRICIAN** **BACKGROUND** |

### Query 75
- Text: Summarize As a diplomat or messenger, you traveled extensively,  communicating with new people and brokering alliances  wherever you went.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 092-097::/page/2/Text/18']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 092-097::/page/2/Text/18', 'PZO22001 Starfinder Player Core 092-097::/page/1/Text/41', 'PZO22001 Starfinder Player Core 092-097::/page/1/Text/28']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/18` | 1.031283 | As a diplomat or messenger, you traveled extensively,  communicating with new people and brokering alliances  wherever you went. |
| 2 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/41` | 0.668007 | You've dedicated your career to facilitating peaceful  alliances between different factions and peoples. You might  work at an intergalactic embassy or travel aboard a starship  on a mission to remote |
| 3 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/28` | 0.554594 | You're one among many professionals working in the  corporate world, but you're not just any suit. You're a  negotiator, dealmaker, or perhaps even a spy working to  advance a particular corporation's |
| 4 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/14` | 0.499646 | Some people might say you've been out in the Drift too long,  but the truth is, you don't feel at home away from your post  on a starship deck. You might crew a long-haul freighter,  military gunship, |
| 5 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/10` | 0.491622 | You're a crewmate on a pirate vessel with ambitions of  pillaging interstellar shipping lanes or taking over a chunk  of a notable planetary body. Perhaps you grew up on such  a ship, were taken priso |
| 6 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/2` | 0.474160 | You've spent years performing  arduous physical labor. It  was a difficult life, but you  survived. You may have  embraced adventuring  as an easier method to  make your way in the  world, or you migh |
| 7 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/6` | 0.462744 | You're an accomplished healer expertly using the latest tech  and pharmaceuticals to treat your patients. You might work  at a clinic, supervise a starship's medbay, serve as a military  medic, or ply |
| 8 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/21` | 0.450441 | You are incredibly knowledgeable, skilled, and perhaps even  trained to teach children and adults about the world and  its wonders. From books to classes, you're committed to  imparting knowledge to a |
| 9 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/2` | 0.447906 | You're a loyal disciple of a particular deity. You might have  been raised in a religious culture or perhaps felt a kindred  calling toward a god later in life, but you've honed your skills  and devot |
| 10 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/24` | 0.444881 | You used to be someone, but that was in another life. You keep  to yourself these days, eking out an existence as a hermit in  the wilderness or a loner in a rundown neighborhood. You  thought you put |

### Query 76
- Text: Summarize The thrill of the win drew you into games of chance.  This might have been a lucrative pastime that paled in  comparison to the real risks of adventuring, or you might  have fallen on hard times due to your gambling and pursued  adventuring as a way out of a spiral.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 092-097::/page/2/Text/22']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 092-097::/page/2/Text/22', 'PZO22001 Starfinder Player Core 092-097::/page/3/Text/2', 'PZO22001 Starfinder Player Core 092-097::/page/3/Text/7']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/22` | 1.042229 | The thrill of the win drew you into games of chance.  This might have been a lucrative pastime that paled in  comparison to the real risks of adventuring, or you might  have fallen on hard times due t |
| 2 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/2` | 0.665189 | You've spent years performing  arduous physical labor. It  was a difficult life, but you  survived. You may have  embraced adventuring  as an easier method to  make your way in the  world, or you migh |
| 3 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/7` | 0.620544 | You earned a living wrenching precious minerals from the  lightless depths. Adventuring might have seemed lucrative or  glamorous compared to this backbreaking labor—and if you  have to head back unde |
| 4 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/37` | 0.570565 | You solved crimes as a police inspector or took clandestine  jobs for various clients as a private investigator. You might  have become an adventurer as part of your next big mystery,  but it's equall |
| 5 | `PZO22001 Starfinder Player Core 092-097::/page/0/Text/7` | 0.538410 | Your art is your greatest passion, whatever form it takes.  Adventuring might help you find inspiration for your  creations, or simply be a way to survive until you become a  world-famous artist. |
| 6 | `PZO22001 Starfinder Player Core 092-097::/page/0/Text/1` | 0.528728 | Your character's abilities don't spring into existence the moment they take up the adventuring life. Their background—the role they had before they became an adventurer—also provides a number of  abil |
| 7 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/24` | 0.523689 | You used to be someone, but that was in another life. You keep  to yourself these days, eking out an existence as a hermit in  the wilderness or a loner in a rundown neighborhood. You  thought you put |
| 8 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/11` | 0.496899 | You're a career criminal with a nasty reputation. Perhaps  unfair circumstances forced you into a life of crime, or maybe  you enjoy the thrill you get from pulling off a heist or living  through a sh |
| 9 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/15` | 0.493672 | You've been imprisoned or punished for a crime, whether  you were guilty or not. Now that your sentence has ended  or you've escaped, you take full advantage of the newfound  freedom of your adventuri |
| 10 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/24` | 0.490790 | You grew up in the kitchens of a tavern or other dining  establishment and excelled there, becoming an exceptional  chef. Baking, cooking, a little brewing on the side—you've  spent lots of time out o |

### Query 77
- Text: Summarize You're an expert on biotech and genetics and frequently  experiment on your own body. You might have worked with  patients who needed gene therapy, conducted research in  laboratories looking for the next breakthrough in biotech, or  even concocted serums for your own personal use.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 092-097::/page/2/Text/26']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 092-097::/page/2/Text/26', 'PZO22001 Starfinder Player Core 092-097::/page/3/Text/28', 'PZO22001 Starfinder Player Core 092-097::/page/2/Text/6']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/26` | 1.032296 | You're an expert on biotech and genetics and frequently  experiment on your own body. You might have worked with  patients who needed gene therapy, conducted research in  laboratories looking for the |
| 2 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/28` | 0.693144 | You work in a lab and conduct research about a scientific  topic. Perhaps you're a biotechnician, chemist, computer  programmer, theoretical physicist, or accomplished  researcher in some other field. |
| 3 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/6` | 0.602045 | You're an accomplished healer expertly using the latest tech  and pharmaceuticals to treat your patients. You might work  at a clinic, supervise a starship's medbay, serve as a military  medic, or ply |
| 4 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/33` | 0.528256 | Your body is a temple to change and technology. Since  a young age, you've been upgrading your anatomy with  augmentations, perhaps after a terrible accident, as part of  an experiment, or because you |
| 5 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/28` | 0.476862 | You're one among many professionals working in the  corporate world, but you're not just any suit. You're a  negotiator, dealmaker, or perhaps even a spy working to  advance a particular corporation's |
| 6 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/34` | 0.442931 | You've always had a knack for computers and virtual spaces  and pride yourself on your ability to learn technical secrets.  The open networks known as infospheres are your home  and the place you can |
| 7 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/41` | 0.441133 | You've dedicated your career to facilitating peaceful  alliances between different factions and peoples. You might  work at an intergalactic embassy or travel aboard a starship  on a mission to remote |
| 8 | `PZO22001 Starfinder Player Core 092-097::/page/0/Text/12` | 0.436979 | You've strengthened your body through practice drills and  workouts, making sure not to waste a single drop of sweat  in your quest for gains. You might be a champion fighting  in arena matches, a har |
| 9 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/21` | 0.430879 | You are incredibly knowledgeable, skilled, and perhaps even  trained to teach children and adults about the world and  its wonders. From books to classes, you're committed to  imparting knowledge to a |
| 10 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/10` | 0.425822 | You're a crewmate on a pirate vessel with ambitions of  pillaging interstellar shipping lanes or taking over a chunk  of a notable planetary body. Perhaps you grew up on such  a ship, were taken priso |

### Query 78
- Text: Summarize else's command.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 092-097::/page/3/Text/55']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 092-097::/page/3/Text/55', 'PZO22001 Starfinder Player Core 092-097::/page/4/Text/25', 'PZO22001 Starfinder Player Core 092-097::/page/5/Text/5']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/55` | 0.865876 | else's command. |
| 2 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/25` | 0.353074 | Whether working in a military outpost, a deep space  exploration vessel, or a local office, you have experience  supporting your comrades by assisting with their tech.  While you've undoubtedly surviv |
| 3 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/5` | 0.340841 | It's possible for your character to learn languages laterin their  adventuring career. Selecting the Multilingual feat, for example,  grants a character two new languages chosen from those listed  bel |
| 4 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/26` | 0.289635 | Choose two attribute boosts. One must be to Constitution  or Intelligence, and one is a free attribute boost. |
| 5 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/39` | 0.287098 | Choose two attribute boosts. One must be to Constitution  or Charisma, and one is a free attribute boost. |
| 6 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/15` | 0.286357 | Choose two attribute boosts. One must be to Dexterity or  Constitution, and one is a free attribute boost. |
| 7 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/25` | 0.282533 | Choose two attribute boosts. One must be to Constitution  or Wisdom, and one is a free attribute boost. |
| 8 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/15` | 0.277635 | Choose two attribute boosts. One must be to Constitution  or Intelligence, and one is a free attribute boost. |
| 9 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/25` | 0.277635 | Choose two attribute boosts. One must be to Constitution  or Intelligence, and one is a free attribute boost. |
| 10 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/4` | 0.272746 | Choose two attribute boosts. One must be to  Strength or Constitution, and one is a free attribute boost. |

### Query 79
- Text: Summarize You're a career criminal with a nasty reputation. Perhaps  unfair circumstances forced you into a life of crime, or maybe  you enjoy the thrill you get from pulling off a heist or living  through a shoot-out. Either way, this life is the only one you  know, and thanks to the bounty on your head, you're in it  until the casket drops or you make enough creds to buy a  new one.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 092-097::/page/3/Text/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 092-097::/page/3/Text/11', 'PZO22001 Starfinder Player Core 092-097::/page/2/Text/30', 'PZO22001 Starfinder Player Core 092-097::/page/4/Text/34']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/11` | 1.035734 | You're a career criminal with a nasty reputation. Perhaps  unfair circumstances forced you into a life of crime, or maybe  you enjoy the thrill you get from pulling off a heist or living  through a sh |
| 2 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/30` | 0.657229 | You're a con artist and trickster who swindles unsuspecting  dupes and blackmails rubes, but it's nothing personal you're just in it for the credits. You might run an operation  on the side, or you mi |
| 3 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/34` | 0.607747 | You enlisted in a military or were recruited by a paramilitary  group as a career trooper. As long as you've got enough  guns and the right squad to back you up, you can handle  just about anything. |
| 4 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/37` | 0.564317 | You solved crimes as a police inspector or took clandestine  jobs for various clients as a private investigator. You might  have become an adventurer as part of your next big mystery,  but it's equall |
| 5 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/24` | 0.557313 | You used to be someone, but that was in another life. You keep  to yourself these days, eking out an existence as a hermit in  the wilderness or a loner in a rundown neighborhood. You  thought you put |
| 6 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/15` | 0.544089 | You've been imprisoned or punished for a crime, whether  you were guilty or not. Now that your sentence has ended  or you've escaped, you take full advantage of the newfound  freedom of your adventuri |
| 7 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/10` | 0.532204 | You're a crewmate on a pirate vessel with ambitions of  pillaging interstellar shipping lanes or taking over a chunk  of a notable planetary body. Perhaps you grew up on such  a ship, were taken priso |
| 8 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/16` | 0.524542 | You know how to remove all traces of a crime. Whether you  worked under the table for legitimate clients like AbadarCorp  or learned your trade working for shady organizations and  crime bosses, you k |
| 9 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/38` | 0.518804 | Everybody wants their 15 minutes of fame, but for you, it's  somehow become a lifestyle. Whether by luck or dedication,  you're a star performer, celebrity, or popular influencer. Your  face, voice, a |
| 10 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/12` | 0.512842 | You've lived long enough in a major settlement to know  how to keep your head down, avoid direct eye contact,  and otherwise move about your day without drawing any  attention to yourself. Whether you |

### Query 80
- Text: Summarize You've been imprisoned or punished for a crime, whether  you were guilty or not. Now that your sentence has ended  or you've escaped, you take full advantage of the newfound  freedom of your adventuring life.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 092-097::/page/3/Text/15']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 092-097::/page/3/Text/15', 'PZO22001 Starfinder Player Core 092-097::/page/3/Text/2', 'PZO22001 Starfinder Player Core 092-097::/page/3/Text/11']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/15` | 1.038978 | You've been imprisoned or punished for a crime, whether  you were guilty or not. Now that your sentence has ended  or you've escaped, you take full advantage of the newfound  freedom of your adventuri |
| 2 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/2` | 0.599942 | You've spent years performing  arduous physical labor. It  was a difficult life, but you  survived. You may have  embraced adventuring  as an easier method to  make your way in the  world, or you migh |
| 3 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/11` | 0.583335 | You're a career criminal with a nasty reputation. Perhaps  unfair circumstances forced you into a life of crime, or maybe  you enjoy the thrill you get from pulling off a heist or living  through a sh |
| 4 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/24` | 0.520252 | You used to be someone, but that was in another life. You keep  to yourself these days, eking out an existence as a hermit in  the wilderness or a loner in a rundown neighborhood. You  thought you put |
| 5 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/37` | 0.514180 | You solved crimes as a police inspector or took clandestine  jobs for various clients as a private investigator. You might  have become an adventurer as part of your next big mystery,  but it's equall |
| 6 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/22` | 0.504924 | The thrill of the win drew you into games of chance.  This might have been a lucrative pastime that paled in  comparison to the real risks of adventuring, or you might  have fallen on hard times due t |
| 7 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/16` | 0.453025 | You know how to remove all traces of a crime. Whether you  worked under the table for legitimate clients like AbadarCorp  or learned your trade working for shady organizations and  crime bosses, you k |
| 8 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/24` | 0.443304 | You grew up in the kitchens of a tavern or other dining  establishment and excelled there, becoming an exceptional  chef. Baking, cooking, a little brewing on the side—you've  spent lots of time out o |
| 9 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/12` | 0.441111 | You've lived long enough in a major settlement to know  how to keep your head down, avoid direct eye contact,  and otherwise move about your day without drawing any  attention to yourself. Whether you |
| 10 | `PZO22001 Starfinder Player Core 092-097::/page/0/Text/7` | 0.434426 | Your art is your greatest passion, whatever form it takes.  Adventuring might help you find inspiration for your  creations, or simply be a way to survive until you become a  world-famous artist. |

### Query 81
- Text: Summarize **INTRODUCTION**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 092-097::/page/3/Text/32']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 092-097::/page/5/Text/20', 'PZO22001 Starfinder Player Core 092-097::/page/1/Text/45', 'PZO22001 Starfinder Player Core 092-097::/page/3/Text/32']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/20` | 0.880541 | **INTRODUCTION** |
| 2 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/45` | 0.880541 | **INTRODUCTION** |
| 3 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/32` | 0.880541 | **INTRODUCTION** |
| 4 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/1` | 0.582365 | **DISCIPLE** **BACKGROUND** |
| 5 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/54` | 0.524467 | **INDEX** |
| 6 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/58` | 0.460996 | **Languages** |
| 7 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/35` | 0.460996 | **Languages** |
| 8 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/42` | 0.460996 | **Languages** |
| 9 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/23` | 0.456302 | **RECLUSE** **BACKGROUND** |
| 10 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/53` | 0.452320 | **GAME** |

### Query 82
- Text: Summarize **Android**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 092-097::/page/3/Text/34']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 092-097::/page/5/Text/22', 'PZO22001 Starfinder Player Core 092-097::/page/1/Text/47', 'PZO22001 Starfinder Player Core 092-097::/page/3/Text/34']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/22` | 0.780963 | **Android** |
| 2 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/47` | 0.780963 | **Android** |
| 3 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/34` | 0.780963 | **Android** |
| 4 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/53` | 0.380135 | **GAME** |
| 5 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/58` | 0.366971 | **Languages** |
| 6 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/35` | 0.366971 | **Languages** |
| 7 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/42` | 0.366971 | **Languages** |
| 8 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/20` | 0.356045 | **INTRODUCTION** |
| 9 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/45` | 0.356045 | **INTRODUCTION** |
| 10 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/32` | 0.356045 | **INTRODUCTION** |

### Query 83
- Text: Summarize **Barathu** **Human**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 092-097::/page/3/Text/35']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 092-097::/page/1/Text/48', 'PZO22001 Starfinder Player Core 092-097::/page/3/Text/35', 'PZO22001 Starfinder Player Core 092-097::/page/5/Text/23']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/48` | 1.011021 | **Barathu** **Human** |
| 2 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/35` | 1.011021 | **Barathu** **Human** |
| 3 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/23` | 0.865271 | **Barathu** |
| 4 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/24` | 0.594673 | **Human** |
| 5 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/32` | 0.420703 | **Heritages** **Borai** |
| 6 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/52` | 0.400708 | **Borai** |
| 7 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/49` | 0.398036 | **Kasatha** |
| 8 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/36` | 0.398036 | **Kasatha** |
| 9 | `PZO22001 Starfinder Player Core 092-097::/page/5/Table/9` | 0.388974 | LanguageSpeakersAkitonianAkiton (shobhads, ysoki)BrethedanBretheda, Liavara, and their moons (barathus, kalos, maraquoi)CastrovelianCastrovel (lashuntas and formians)DiasporanDiaspora (sarcesians)Drac |
| 10 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/25` | 0.386036 | **Kasatha** |

### Query 84
- Text: Summarize **Kasatha**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 092-097::/page/3/Text/36']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 092-097::/page/1/Text/49', 'PZO22001 Starfinder Player Core 092-097::/page/5/Text/25', 'PZO22001 Starfinder Player Core 092-097::/page/3/Text/36']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/49` | 0.982519 | **Kasatha** |
| 2 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/25` | 0.982519 | **Kasatha** |
| 3 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/36` | 0.982519 | **Kasatha** |
| 4 | `PZO22001 Starfinder Player Core 092-097::/page/5/TableCell/492` | 0.863855 | Kasatha |
| 5 | `PZO22001 Starfinder Player Core 092-097::/page/5/TableCell/493` | 0.619101 | Kasathas, inhabitants of Kasath or the Idari |
| 6 | `PZO22001 Starfinder Player Core 092-097::/page/5/Table/7` | 0.492914 | LanguageSpeakersCommonHumans, most citizens of the Pact WorldsKasathaKasathas, inhabitants of Kasath or the IdariPahtraPahtras |
| 7 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/23` | 0.396219 | **Barathu** |
| 8 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/48` | 0.395725 | **Barathu** **Human** |
| 9 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/35` | 0.395725 | **Barathu** **Human** |
| 10 | `PZO22001 Starfinder Player Core 092-097::/page/5/Table/9` | 0.372748 | LanguageSpeakersAkitonianAkiton (shobhads, ysoki)BrethedanBretheda, Liavara, and their moons (barathus, kalos, maraquoi)CastrovelianCastrovel (lashuntas and formians)DiasporanDiaspora (sarcesians)Drac |

### Query 85
- Text: Summarize **Lashunta** **Pahtra**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 092-097::/page/3/Text/37']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 092-097::/page/3/Text/37', 'PZO22001 Starfinder Player Core 092-097::/page/1/Text/50', 'PZO22001 Starfinder Player Core 092-097::/page/5/Text/26']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/37` | 0.997371 | **Lashunta** **Pahtra** |
| 2 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/50` | 0.794342 | **Lashunta** |
| 3 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/26` | 0.794342 | **Lashunta** |
| 4 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/51` | 0.697032 | **Pahtra** **Shirren** |
| 5 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/27` | 0.697032 | **Pahtra** **Shirren** |
| 6 | `PZO22001 Starfinder Player Core 092-097::/page/5/TableCell/494` | 0.646817 | Pahtra |
| 7 | `PZO22001 Starfinder Player Core 092-097::/page/5/TableCell/495` | 0.628531 | Pahtras |
| 8 | `PZO22001 Starfinder Player Core 092-097::/page/5/TableCell/503` | 0.427295 | Castrovel (lashuntas and formians) |
| 9 | `PZO22001 Starfinder Player Core 092-097::/page/5/Table/7` | 0.413600 | LanguageSpeakersCommonHumans, most citizens of the Pact WorldsKasathaKasathas, inhabitants of Kasath or the IdariPahtraPahtras |
| 10 | `PZO22001 Starfinder Player Core 092-097::/page/5/Table/9` | 0.386800 | LanguageSpeakersAkitonianAkiton (shobhads, ysoki)BrethedanBretheda, Liavara, and their moons (barathus, kalos, maraquoi)CastrovelianCastrovel (lashuntas and formians)DiasporanDiaspora (sarcesians)Drac |

### Query 86
- Text: Summarize **Shirren**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 092-097::/page/3/Text/51']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 092-097::/page/3/Text/51', 'PZO22001 Starfinder Player Core 092-097::/page/5/Text/27', 'PZO22001 Starfinder Player Core 092-097::/page/1/Text/51']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/51` | 0.983425 | **Shirren** |
| 2 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/27` | 0.773976 | **Pahtra** **Shirren** |
| 3 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/51` | 0.773976 | **Pahtra** **Shirren** |
| 4 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/50` | 0.320426 | **Lashunta** |
| 5 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/26` | 0.320426 | **Lashunta** |
| 6 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/28` | 0.312421 | **Skittermander** |
| 7 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/52` | 0.312421 | **Skittermander** |
| 8 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/20` | 0.310952 | **INTRODUCTION** |
| 9 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/32` | 0.310952 | **INTRODUCTION** |
| 10 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/45` | 0.310952 | **INTRODUCTION** |

### Query 87
- Text: Summarize **Vesk**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 092-097::/page/3/Text/38']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 092-097::/page/1/Text/53', 'PZO22001 Starfinder Player Core 092-097::/page/3/Text/38', 'PZO22001 Starfinder Player Core 092-097::/page/5/Text/29']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/53` | 0.943397 | **Vesk** |
| 2 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/38` | 0.943397 | **Vesk** |
| 3 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/29` | 0.943397 | **Vesk** |
| 4 | `PZO22001 Starfinder Player Core 092-097::/page/5/TableCell/514` | 0.807644 | Vesk |
| 5 | `PZO22001 Starfinder Player Core 092-097::/page/5/TableCell/515` | 0.552234 | Pulonis, the Veskarium (pahtras, vesk) |
| 6 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/36` | 0.367531 | **Kasatha** |
| 7 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/49` | 0.367531 | **Kasatha** |
| 8 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/25` | 0.367531 | **Kasatha** |
| 9 | `PZO22001 Starfinder Player Core 092-097::/page/5/Table/9` | 0.346223 | LanguageSpeakersAkitonianAkiton (shobhads, ysoki)BrethedanBretheda, Liavara, and their moons (barathus, kalos, maraquoi)CastrovelianCastrovel (lashuntas and formians)DiasporanDiaspora (sarcesians)Drac |
| 10 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/54` | 0.339943 | **INDEX** |

### Query 88
- Text: Summarize **Ysoki**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 092-097::/page/3/Text/39']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 092-097::/page/5/Text/30', 'PZO22001 Starfinder Player Core 092-097::/page/3/Text/39', 'PZO22001 Starfinder Player Core 092-097::/page/1/Text/54']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/30` | 0.934336 | **Ysoki** |
| 2 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/39` | 0.934336 | **Ysoki** |
| 3 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/54` | 0.934336 | **Ysoki** |
| 4 | `PZO22001 Starfinder Player Core 092-097::/page/5/TableCell/499` | 0.515883 | Akiton (shobhads, ysoki) |
| 5 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/42` | 0.383117 | **Languages** |
| 6 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/58` | 0.383117 | **Languages** |
| 7 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/35` | 0.383117 | **Languages** |
| 8 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/54` | 0.366194 | **INDEX** |
| 9 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/20` | 0.364466 | **INTRODUCTION** |
| 10 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/45` | 0.364466 | **INTRODUCTION** |

### Query 89
- Text: Summarize **Versatile ** **Heritages**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 092-097::/page/3/Text/40']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 092-097::/page/1/Text/55', 'PZO22001 Starfinder Player Core 092-097::/page/3/Text/40', 'PZO22001 Starfinder Player Core 092-097::/page/5/Text/31']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/55` | 0.959353 | **Versatile ** **Heritages** |
| 2 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/40` | 0.959353 | **Versatile ** **Heritages** |
| 3 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/31` | 0.670755 | **Versatile ** |
| 4 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/32` | 0.510696 | **Heritages** **Borai** |
| 5 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/34` | 0.419632 | **Backgrounds** |
| 6 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/57` | 0.419632 | **Backgrounds** |
| 7 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/1` | 0.398140 | **DISCIPLE** **BACKGROUND** |
| 8 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/46` | 0.397026 | **ANCESTRIES & ** **BACKGROUNDS** |
| 9 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/21` | 0.397026 | **ANCESTRIES & ** **BACKGROUNDS** |
| 10 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/33` | 0.397026 | **ANCESTRIES & ** **BACKGROUNDS** |

### Query 90
- Text: Summarize **Borai**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 092-097::/page/3/Text/52']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 092-097::/page/3/Text/52', 'PZO22001 Starfinder Player Core 092-097::/page/5/Text/32', 'PZO22001 Starfinder Player Core 092-097::/page/1/Text/56']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/52` | 0.983112 | **Borai** |
| 2 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/32` | 0.899213 | **Heritages** **Borai** |
| 3 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/56` | 0.770343 | **Borai** **Prismeni** |
| 4 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/23` | 0.447974 | **Barathu** |
| 5 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/35` | 0.411932 | **Barathu** **Human** |
| 6 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/48` | 0.411932 | **Barathu** **Human** |
| 7 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/54` | 0.348229 | **Ysoki** |
| 8 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/39` | 0.348229 | **Ysoki** |
| 9 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/30` | 0.348229 | **Ysoki** |
| 10 | `PZO22001 Starfinder Player Core 092-097::/page/1/SectionHeader/31` | 0.330918 | **CYBERBORN** **BACKGROUND** |

### Query 91
- Text: Summarize **Languages**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 092-097::/page/3/Text/42']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 092-097::/page/5/Text/35', 'PZO22001 Starfinder Player Core 092-097::/page/1/Text/58', 'PZO22001 Starfinder Player Core 092-097::/page/3/Text/42']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/35` | 0.876251 | **Languages** |
| 2 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/58` | 0.876251 | **Languages** |
| 3 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/42` | 0.876251 | **Languages** |
| 4 | `PZO22001 Starfinder Player Core 092-097::/page/5/SectionHeader/0` | 0.622405 | LANGUAGES |
| 5 | `PZO22001 Starfinder Player Core 092-097::/page/5/TableCell/516` | 0.562137 | Language |
| 6 | `PZO22001 Starfinder Player Core 092-097::/page/5/TableCell/496` | 0.562137 | Language |
| 7 | `PZO22001 Starfinder Player Core 092-097::/page/5/TableCell/488` | 0.562137 | Language |
| 8 | `PZO22001 Starfinder Player Core 092-097::/page/5/SectionHeader/8` | 0.542038 | **COMMON REGIONAL LANGUAGES** |
| 9 | `PZO22001 Starfinder Player Core 092-097::/page/5/SectionHeader/12` | 0.506057 | REGIONAL LANGUAGES |
| 10 | `PZO22001 Starfinder Player Core 092-097::/page/5/SectionHeader/6` | 0.452126 | **COMMON ANCESTRY LANGUAGES** |

### Query 92
- Text: Summarize **EQUIPMENT**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 092-097::/page/3/Text/45']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 092-097::/page/5/Text/38', 'PZO22001 Starfinder Player Core 092-097::/page/3/Text/45', 'PZO22001 Starfinder Player Core 092-097::/page/1/Text/61']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/38` | 0.944726 | **EQUIPMENT** |
| 2 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/45` | 0.944726 | **EQUIPMENT** |
| 3 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/61` | 0.944726 | **EQUIPMENT** |
| 4 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/54` | 0.421643 | **INDEX** |
| 5 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/1` | 0.412371 | **DISCIPLE** **BACKGROUND** |
| 6 | `PZO22001 Starfinder Player Core 092-097::/page/4/SectionHeader/24` | 0.407946 | **TECH SUPPORT** **BACKGROUND** |
| 7 | `PZO22001 Starfinder Player Core 092-097::/page/0/SectionHeader/11` | 0.407588 | **ATHLETE** **BACKGROUND** |
| 8 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/45` | 0.385549 | **INTRODUCTION** |
| 9 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/20` | 0.385549 | **INTRODUCTION** |
| 10 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/32` | 0.385549 | **INTRODUCTION** |

### Query 93
- Text: Summarize **CONDITIONS ** **APPENDIX**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 092-097::/page/3/Text/47']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 092-097::/page/3/Text/47', 'PZO22001 Starfinder Player Core 092-097::/page/1/Text/64', 'PZO22001 Starfinder Player Core 092-097::/page/5/Text/41']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/47` | 0.983499 | **CONDITIONS ** **APPENDIX** |
| 2 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/64` | 0.983499 | **CONDITIONS ** **APPENDIX** |
| 3 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/41` | 0.983499 | **CONDITIONS ** **APPENDIX** |
| 4 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/54` | 0.423722 | **INDEX** |
| 5 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/33` | 0.416141 | **ANCESTRIES & ** **BACKGROUNDS** |
| 6 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/21` | 0.416141 | **ANCESTRIES & ** **BACKGROUNDS** |
| 7 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/46` | 0.416141 | **ANCESTRIES & ** **BACKGROUNDS** |
| 8 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/1` | 0.393926 | **DISCIPLE** **BACKGROUND** |
| 9 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/23` | 0.373981 | **RECLUSE** **BACKGROUND** |
| 10 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/61` | 0.372115 | **EQUIPMENT** |

### Query 94
- Text: Summarize **GAME**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 092-097::/page/3/Text/53']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 092-097::/page/3/Text/53', 'PZO22001 Starfinder Player Core 092-097::/page/5/Text/40', 'PZO22001 Starfinder Player Core 092-097::/page/1/Text/63']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/53` | 0.878539 | **GAME** |
| 2 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/40` | 0.728831 | **PLAYING THE ** **GAME** |
| 3 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/63` | 0.728831 | **PLAYING THE ** **GAME** |
| 4 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/45` | 0.507571 | **INTRODUCTION** |
| 5 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/32` | 0.507571 | **INTRODUCTION** |
| 6 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/20` | 0.507571 | **INTRODUCTION** |
| 7 | `PZO22001 Starfinder Player Core 092-097::/page/2/SectionHeader/21` | 0.483683 | **GAMBLER** **BACKGROUND** |
| 8 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/22` | 0.480262 | **Android** |
| 9 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/47` | 0.480262 | **Android** |
| 10 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/34` | 0.480262 | **Android** |

### Query 95
- Text: Summarize **GLOSSARY & **
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 092-097::/page/3/Text/48']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 092-097::/page/3/Text/48', 'PZO22001 Starfinder Player Core 092-097::/page/1/Text/65', 'PZO22001 Starfinder Player Core 092-097::/page/5/Text/42']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/48` | 0.986628 | **GLOSSARY & ** |
| 2 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/65` | 0.872894 | **GLOSSARY & ** **INDEX** |
| 3 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/42` | 0.872894 | **GLOSSARY & ** **INDEX** |
| 4 | `PZO22001 Starfinder Player Core 092-097::/page/2/SectionHeader/17` | 0.395256 | **EMISSARY** **BACKGROUND** |
| 5 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/42` | 0.382212 | **Languages** |
| 6 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/35` | 0.382212 | **Languages** |
| 7 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/58` | 0.382212 | **Languages** |
| 8 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/59` | 0.373615 | **CLASSES** |
| 9 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/36` | 0.373615 | **CLASSES** |
| 10 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/26` | 0.366462 | **Lashunta** |

### Query 96
- Text: Summarize **INDEX**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 092-097::/page/3/Text/54']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 092-097::/page/3/Text/54', 'PZO22001 Starfinder Player Core 092-097::/page/1/Text/65', 'PZO22001 Starfinder Player Core 092-097::/page/5/Text/42']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/54` | 0.897726 | **INDEX** |
| 2 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/65` | 0.648125 | **GLOSSARY & ** **INDEX** |
| 3 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/42` | 0.648125 | **GLOSSARY & ** **INDEX** |
| 4 | `PZO22001 Starfinder Player Core 092-097::/page/2/SectionHeader/37` | 0.501926 | **ICON** **BACKGROUND** |
| 5 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/1` | 0.450014 | **DISCIPLE** **BACKGROUND** |
| 6 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/32` | 0.449260 | **INTRODUCTION** |
| 7 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/20` | 0.449260 | **INTRODUCTION** |
| 8 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/45` | 0.449260 | **INTRODUCTION** |
| 9 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/57` | 0.406334 | **Backgrounds** |
| 10 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/34` | 0.406334 | **Backgrounds** |

### Query 97
- Text: Summarize Thanks to generational wealth or lucky circumstance, you  live a charmed life flitting between galas dressed in the  latest designer fashion. You memorialize every glittering  moment on social media, and if nobody pays attention,  that's just because they're jealous.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 092-097::/page/4/Text/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 092-097::/page/4/Text/6', 'PZO22001 Starfinder Player Core 092-097::/page/2/Text/38', 'PZO22001 Starfinder Player Core 092-097::/page/3/Text/11']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/6` | 1.040763 | Thanks to generational wealth or lucky circumstance, you  live a charmed life flitting between galas dressed in the  latest designer fashion. You memorialize every glittering  moment on social media, |
| 2 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/38` | 0.639453 | Everybody wants their 15 minutes of fame, but for you, it's  somehow become a lifestyle. Whether by luck or dedication,  you're a star performer, celebrity, or popular influencer. Your  face, voice, a |
| 3 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/11` | 0.517644 | You're a career criminal with a nasty reputation. Perhaps  unfair circumstances forced you into a life of crime, or maybe  you enjoy the thrill you get from pulling off a heist or living  through a sh |
| 4 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/12` | 0.461290 | You've lived long enough in a major settlement to know  how to keep your head down, avoid direct eye contact,  and otherwise move about your day without drawing any  attention to yourself. Whether you |
| 5 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/30` | 0.438918 | You're a con artist and trickster who swindles unsuspecting  dupes and blackmails rubes, but it's nothing personal you're just in it for the credits. You might run an operation  on the side, or you mi |
| 6 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/24` | 0.438567 | You grew up in the kitchens of a tavern or other dining  establishment and excelled there, becoming an exceptional  chef. Baking, cooking, a little brewing on the side—you've  spent lots of time out o |
| 7 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/20` | 0.436361 | Whether you're the office joker, a professional comedian, or  just a troll on the infosphere, you're always prepared with a  well-timed joke, even if it occasionally gets you in hot water  when you cr |
| 8 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/24` | 0.435969 | You used to be someone, but that was in another life. You keep  to yourself these days, eking out an existence as a hermit in  the wilderness or a loner in a rundown neighborhood. You  thought you put |
| 9 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/18` | 0.434724 | You know the streets because they raised you. You grew  up scraping by in a massive cityscape like those on Verces  or Castrovel, or on a crowded space station like Absalom  Station. You might have ev |
| 10 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/22` | 0.420851 | The thrill of the win drew you into games of chance.  This might have been a lucrative pastime that paled in  comparison to the real risks of adventuring, or you might  have fallen on hard times due t |

### Query 98
- Text: Summarize You're a crewmate on a pirate vessel with ambitions of  pillaging interstellar shipping lanes or taking over a chunk  of a notable planetary body. Perhaps you grew up on such  a ship, were taken prisoner by the crew at a young age and  adapted to their lifestyle, or commandeered a vessel from a  pirate captain.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 092-097::/page/4/Text/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 092-097::/page/4/Text/10', 'PZO22001 Starfinder Player Core 092-097::/page/4/Text/14', 'PZO22001 Starfinder Player Core 092-097::/page/1/Text/41']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/10` | 1.034544 | You're a crewmate on a pirate vessel with ambitions of  pillaging interstellar shipping lanes or taking over a chunk  of a notable planetary body. Perhaps you grew up on such  a ship, were taken priso |
| 2 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/14` | 0.656692 | Some people might say you've been out in the Drift too long,  but the truth is, you don't feel at home away from your post  on a starship deck. You might crew a long-haul freighter,  military gunship, |
| 3 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/41` | 0.628066 | You've dedicated your career to facilitating peaceful  alliances between different factions and peoples. You might  work at an intergalactic embassy or travel aboard a starship  on a mission to remote |
| 4 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/2` | 0.536499 | You make your living smuggling cargo, whether on a planet or  in the depths of space. You don't ask your clients too many  questions, and the cargo could be anything—counterfeit  products, illegal goo |
| 5 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/24` | 0.530645 | You used to be someone, but that was in another life. You keep  to yourself these days, eking out an existence as a hermit in  the wilderness or a loner in a rundown neighborhood. You  thought you put |
| 6 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/2` | 0.527080 | You've spent years performing  arduous physical labor. It  was a difficult life, but you  survived. You may have  embraced adventuring  as an easier method to  make your way in the  world, or you migh |
| 7 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/30` | 0.525616 | You're a con artist and trickster who swindles unsuspecting  dupes and blackmails rubes, but it's nothing personal you're just in it for the credits. You might run an operation  on the side, or you mi |
| 8 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/11` | 0.523303 | You're a career criminal with a nasty reputation. Perhaps  unfair circumstances forced you into a life of crime, or maybe  you enjoy the thrill you get from pulling off a heist or living  through a sh |
| 9 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/28` | 0.518697 | You're one among many professionals working in the  corporate world, but you're not just any suit. You're a  negotiator, dealmaker, or perhaps even a spy working to  advance a particular corporation's |
| 10 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/2` | 0.516727 | You're a loyal disciple of a particular deity. You might have  been raised in a religious culture or perhaps felt a kindred  calling toward a god later in life, but you've honed your skills  and devot |

### Query 99
- Text: Summarize Some people might say you've been out in the Drift too long,  but the truth is, you don't feel at home away from your post  on a starship deck. You might crew a long-haul freighter,  military gunship, or tourist shuttle. Truth is, you'd probably  sign up for any job that took you off-world.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 092-097::/page/4/Text/14']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 092-097::/page/4/Text/14', 'PZO22001 Starfinder Player Core 092-097::/page/4/Text/10', 'PZO22001 Starfinder Player Core 092-097::/page/1/Text/41']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/14` | 1.045676 | Some people might say you've been out in the Drift too long,  but the truth is, you don't feel at home away from your post  on a starship deck. You might crew a long-haul freighter,  military gunship, |
| 2 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/10` | 0.667712 | You're a crewmate on a pirate vessel with ambitions of  pillaging interstellar shipping lanes or taking over a chunk  of a notable planetary body. Perhaps you grew up on such  a ship, were taken priso |
| 3 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/41` | 0.617403 | You've dedicated your career to facilitating peaceful  alliances between different factions and peoples. You might  work at an intergalactic embassy or travel aboard a starship  on a mission to remote |
| 4 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/24` | 0.539985 | You grew up in the kitchens of a tavern or other dining  establishment and excelled there, becoming an exceptional  chef. Baking, cooking, a little brewing on the side—you've  spent lots of time out o |
| 5 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/2` | 0.536971 | You make your living smuggling cargo, whether on a planet or  in the depths of space. You don't ask your clients too many  questions, and the cargo could be anything—counterfeit  products, illegal goo |
| 6 | `PZO22001 Starfinder Player Core 092-097::/page/2/Text/18` | 0.525059 | As a diplomat or messenger, you traveled extensively,  communicating with new people and brokering alliances  wherever you went. |
| 7 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/2` | 0.518101 | You've spent years performing  arduous physical labor. It  was a difficult life, but you  survived. You may have  embraced adventuring  as an easier method to  make your way in the  world, or you migh |
| 8 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/24` | 0.505700 | You used to be someone, but that was in another life. You keep  to yourself these days, eking out an existence as a hermit in  the wilderness or a loner in a rundown neighborhood. You  thought you put |
| 9 | `PZO22001 Starfinder Player Core 092-097::/page/3/Text/7` | 0.499012 | You earned a living wrenching precious minerals from the  lightless depths. Adventuring might have seemed lucrative or  glamorous compared to this backbreaking labor—and if you  have to head back unde |
| 10 | `PZO22001 Starfinder Player Core 092-097::/page/4/Text/34` | 0.493595 | You enlisted in a military or were recruited by a paramilitary  group as a career trooper. As long as you've got enough  guns and the right squad to back you up, you can handle  just about anything. |

### Query 100
- Text: Lookup values for LanguageSpeakersCommonHumans, most citizens of the Pact WorldsKasathaKasathas, inhabitants of Kasath or the IdariPahtraPahtras
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 092-097::/page/5/Table/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 092-097::/page/5/Table/7', 'PZO22001 Starfinder Player Core 092-097::/page/5/TableCell/491', 'PZO22001 Starfinder Player Core 092-097::/page/5/TableCell/493']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 092-097::/page/5/Table/7` | 1.018790 | LanguageSpeakersCommonHumans, most citizens of the Pact WorldsKasathaKasathas, inhabitants of Kasath or the IdariPahtraPahtras |
| 2 | `PZO22001 Starfinder Player Core 092-097::/page/5/TableCell/491` | 0.748060 | Humans, most citizens of the Pact Worlds |
| 3 | `PZO22001 Starfinder Player Core 092-097::/page/5/TableCell/493` | 0.741437 | Kasathas, inhabitants of Kasath or the Idari |
| 4 | `PZO22001 Starfinder Player Core 092-097::/page/5/Table/9` | 0.612566 | LanguageSpeakersAkitonianAkiton (shobhads, ysoki)BrethedanBretheda, Liavara, and their moons (barathus, kalos, maraquoi)CastrovelianCastrovel (lashuntas and formians)DiasporanDiaspora (sarcesians)Drac |
| 5 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/4` | 0.609628 | The languages presented here are grouped according to their use in the Pact Worlds. Languages that are uncommon  are most frequently spoken by their native speakers, but  they are also spoken by certa |
| 6 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/14` | 0.554093 | Most characters also learn the Common language. This  is the most widely used language in the galaxy and is the  dominant language of the Pact Worlds. In many systems,  even if Common is not the offic |
| 7 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/2` | 0.473912 | The galaxy is filled with countless species and even more  languages, many of which have hundreds of dialects and  regional variations. Most characters in Starfinder can get by  with Common (also know |
| 8 | `PZO22001 Starfinder Player Core 092-097::/page/5/TableCell/492` | 0.461960 | Kasatha |
| 9 | `PZO22001 Starfinder Player Core 092-097::/page/1/Text/49` | 0.451077 | **Kasatha** |
| 10 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/25` | 0.451077 | **Kasatha** |

### Query 101
- Text: Lookup values for LanguageSpeakersAkitonianAkiton (shobhads, ysoki)BrethedanBretheda, Liavara, and their moons
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 092-097::/page/5/Table/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 092-097::/page/5/Table/9', 'PZO22001 Starfinder Player Core 092-097::/page/5/TableCell/499', 'PZO22001 Starfinder Player Core 092-097::/page/5/TableCell/501']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 092-097::/page/5/Table/9` | 0.833749 | LanguageSpeakersAkitonianAkiton (shobhads, ysoki)BrethedanBretheda, Liavara, and their moons (barathus, kalos, maraquoi)CastrovelianCastrovel (lashuntas and formians)DiasporanDiaspora (sarcesians)Drac |
| 2 | `PZO22001 Starfinder Player Core 092-097::/page/5/TableCell/499` | 0.661464 | Akiton (shobhads, ysoki) |
| 3 | `PZO22001 Starfinder Player Core 092-097::/page/5/TableCell/501` | 0.660774 | Bretheda, Liavara, and their moons (barathus, kalos, maraquoi) |
| 4 | `PZO22001 Starfinder Player Core 092-097::/page/5/Table/11` | 0.559462 | LanguageSpeakersAkloEvil fey, otherworldly monstersChthonianDemonsDiabolicDevilsEmpyreanAngelsMuanWood elemental creaturesNecrilUndeadOrcishOrcs, dromaarsPetranEarth elemental creaturesPyricFire eleme |
| 5 | `PZO22001 Starfinder Player Core 092-097::/page/5/Table/7` | 0.492610 | LanguageSpeakersCommonHumans, most citizens of the Pact WorldsKasathaKasathas, inhabitants of Kasath or the IdariPahtraPahtras |
| 6 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/13` | 0.471862 | Regional languages vary based on planet. The tables above  list the regional languages of the Starfinder setting and  where they're spoken. These languages are uncommon. A  character hailing from one |
| 7 | `PZO22001 Starfinder Player Core 092-097::/page/5/TableCell/500` | 0.421945 | Brethedan |
| 8 | `PZO22001 Starfinder Player Core 092-097::/page/5/Text/4` | 0.419666 | The languages presented here are grouped according to their use in the Pact Worlds. Languages that are uncommon  are most frequently spoken by their native speakers, but  they are also spoken by certa |
| 9 | `PZO22001 Starfinder Player Core 092-097::/page/5/TableCell/498` | 0.412423 | Akitonian |
| 10 | `PZO22001 Starfinder Player Core 092-097::/page/5/TableCell/493` | 0.406646 | Kasathas, inhabitants of Kasath or the Idari |

### Query 102
- Text: Lookup values for LanguageSpeakersAkloEvil fey, otherworldly monstersChthonianDemonsDiabolicDevilsEmpyreanAngelsMuanWood elemental creaturesNecrilUndeadOrcishOrcs, dromaarsPetranEarth elemental creaturesPyricFire elemental creaturesShadowtongueNetherworld creaturesSussuranAir elemental creatures, flying creaturesTalicanMetal elemental creaturesThalassicAquatic creatures, water elemental
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 092-097::/page/5/Table/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 092-097::/page/5/Table/11', 'PZO22001 Starfinder Player Core 092-097::/page/5/Table/9', 'PZO22001 Starfinder Player Core 092-097::/page/5/TableCell/543']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 092-097::/page/5/Table/11` | 1.010356 | LanguageSpeakersAkloEvil fey, otherworldly monstersChthonianDemonsDiabolicDevilsEmpyreanAngelsMuanWood elemental creaturesNecrilUndeadOrcishOrcs, dromaarsPetranEarth elemental creaturesPyricFire eleme |
| 2 | `PZO22001 Starfinder Player Core 092-097::/page/5/Table/9` | 0.771874 | LanguageSpeakersAkitonianAkiton (shobhads, ysoki)BrethedanBretheda, Liavara, and their moons (barathus, kalos, maraquoi)CastrovelianCastrovel (lashuntas and formians)DiasporanDiaspora (sarcesians)Drac |
| 3 | `PZO22001 Starfinder Player Core 092-097::/page/5/TableCell/543` | 0.659872 | Aquatic creatures, water elemental creatures |
| 4 | `PZO22001 Starfinder Player Core 092-097::/page/5/TableCell/533` | 0.590069 | Earth elemental creatures |
| 5 | `PZO22001 Starfinder Player Core 092-097::/page/5/TableCell/535` | 0.584126 | Fire elemental creatures |
| 6 | `PZO22001 Starfinder Player Core 092-097::/page/5/TableCell/539` | 0.568761 | Air elemental creatures, flying creatures |
| 7 | `PZO22001 Starfinder Player Core 092-097::/page/5/TableCell/537` | 0.564833 | Netherworld creatures |
| 8 | `PZO22001 Starfinder Player Core 092-097::/page/5/TableCell/541` | 0.556791 | Metal elemental creatures |
| 9 | `PZO22001 Starfinder Player Core 092-097::/page/5/TableCell/527` | 0.552007 | Wood elemental creatures |
| 10 | `PZO22001 Starfinder Player Core 092-097::/page/5/TableCell/519` | 0.508446 | Evil fey, otherworldly monsters |
