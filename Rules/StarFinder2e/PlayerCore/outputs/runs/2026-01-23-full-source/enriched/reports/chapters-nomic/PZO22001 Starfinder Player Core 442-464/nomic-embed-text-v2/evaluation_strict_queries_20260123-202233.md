# RulesLawyer Evaluation Report: nomic-embed-text-v2

## Summary
- Run ID: `None`
- Ruleset ID: `None`
- Document ID: `None`
- Chunk source: `enriched`
- Chunk count: `1291`
- Query count: `102`
- Evaluated queries: `102`
- Coverage: `1.0000`
- MRR: `0.9577`
- hit@1: `0.9412`
- hit@3: `0.9608`
- hit@5: `0.9804`
- hit@10: `1.0000`
- Embeddings reused: `False`
- Graph boost: `0.05` (depth=2, top_k=50, source=top, seed_top_n=3, same_kind_only=False, decay=0.4)

## Timings (ms)
- Embedding (chunks): `20043`
- Embedding (queries): `1932`
- Evaluation (strict): `88`
- Evaluation (expanded): `0`
- Total: `26586`

### Timing Estimates (ms)
- Evaluation (strict): `122`
- Evaluation (expanded): `None`
- Total: `22097`

## Query Details
### Query 0
- Text: Summarize GLOSSARY & INDEX
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 442-464::/page/0/SectionHeader/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 442-464::/page/0/SectionHeader/1', 'PZO22001 Starfinder Player Core 442-464::/page/13/Text/62', 'PZO22001 Starfinder Player Core 442-464::/page/3/Text/65']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 442-464::/page/0/SectionHeader/1` | 0.975022 | GLOSSARY & INDEX |
| 2 | `PZO22001 Starfinder Player Core 442-464::/page/13/Text/62` | 0.889503 | **GLOSSARY & ** **INDEX** |
| 3 | `PZO22001 Starfinder Player Core 442-464::/page/3/Text/65` | 0.889503 | **GLOSSARY & ** **INDEX** |
| 4 | `PZO22001 Starfinder Player Core 442-464::/page/5/Text/69` | 0.847503 | **GLOSSARY & ** **INDEX** |
| 5 | `PZO22001 Starfinder Player Core 442-464::/page/7/Text/68` | 0.847503 | **GLOSSARY & ** **INDEX** |
| 6 | `PZO22001 Starfinder Player Core 442-464::/page/11/Text/63` | 0.847503 | **GLOSSARY & ** **INDEX** |
| 7 | `PZO22001 Starfinder Player Core 442-464::/page/9/Text/54` | 0.847503 | **GLOSSARY & ** **INDEX** |
| 8 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/61` | 0.847503 | **GLOSSARY & ** **INDEX** |
| 9 | `PZO22001 Starfinder Player Core 442-464::/page/19/Text/86` | 0.658206 | **APPENDIX** **GLOSSARY & ** |
| 10 | `PZO22001 Starfinder Player Core 442-464::/page/19/Text/87` | 0.345884 | **INDEX** **CHARACTER ** |

### Query 1
- Text: What is the rule about **Aballon** A rocky, sun-blasted planet of industry which is home to  intelligent machines created by the enigmatic First Ones. 31?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 442-464::/page/0/Text/3']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 442-464::/page/0/Text/3', 'PZO22001 Starfinder Player Core 442-464::/page/0/Text/6', 'PZO22001 Starfinder Player Core 442-464::/page/0/Text/30']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/3` | 0.957373 | **Aballon** A rocky, sun-blasted planet of industry which is home to  intelligent machines created by the enigmatic First Ones. 31 |
| 2 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/6` | 0.555471 | **Absalom Station** A space station which serves as a major hub  of trade and culture in the Pact Worlds. 31 |
| 3 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/30` | 0.507386 | **Akiton** A red desert planet often defined by its economic  decline due to changes in starship technology. 32 |
| 4 | `PZO22001 Starfinder Player Core 442-464::/page/4/Text/52` | 0.451242 | **Eox **A radioactive wasteland of a planet ruled by the undead who  destroyed their once lush home world in a terrible disaster. 32 |
| 5 | `PZO22001 Starfinder Player Core 442-464::/page/9/Text/10` | 0.422917 | **Pact Worlds** The governing body of planets that make up the  core of the primary Starfinder setting. 30–34 |
| 6 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/44` | 0.422822 | **Apostae** A hollow planetoid containing mysterious gateways to  tunnel networks and ancient mechanical complexes. 34 |
| 7 | `PZO22001 Starfinder Player Core 442-464::/page/2/Text/18` | 0.422058 | **Castrovel** A jungle planet teeming with psychic energy which  is home to elves, lashunta, and formians. 31 |
| 8 | `PZO22001 Starfinder Player Core 442-464::/page/13/Text/24` | 0.418636 | **tech** (trait) Equipment with the tech trait rely on electricity  and may gain the glitching condition. Some creatures  and hazards also have the tech trait, such as artificial  intelligence, robots |
| 9 | `PZO22001 Starfinder Player Core 442-464::/page/4/Text/1` | 0.413029 | **Diaspora** An asteroid belt formed when the twin planets  Damiar and Iovo were destroyed, home to smugglers,  pirates, and sarcesians. 32 |
| 10 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/32` | 0.412608 | **aucturnite** (material) A dull remnant of the planet Aucturn  that causes madness. 278 |

### Query 2
- Text: What is the rule about **aberration** (trait) Aberrations are creatures from beyond the  planes or corruptions of the natural order.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 442-464::/page/0/Text/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 442-464::/page/0/Text/4', 'PZO22001 Starfinder Player Core 442-464::/page/5/Text/21', 'PZO22001 Starfinder Player Core 442-464::/page/9/Text/30']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/4` | 0.975650 | **aberration** (trait) Aberrations are creatures from beyond the  planes or corruptions of the natural order. |
| 2 | `PZO22001 Starfinder Player Core 442-464::/page/5/Text/21` | 0.544740 | **fiend** (trait) Creatures that hail from or have a strong  connection to the unholy planes are called fiends. |
| 3 | `PZO22001 Starfinder Player Core 442-464::/page/9/Text/30` | 0.543272 | **plant** (trait) Vegetable creatures have the plant trait. They are  distinct from normal plants. Magical effects with this trait  manipulate or conjure plants or plant matter in some way.  Effects t |
| 4 | `PZO22001 Starfinder Player Core 442-464::/page/14/Text/26` | 0.500231 | **visual** (trait) A visual effect can affect only creatures that can  see it. This applies only to visible parts of the effect, as  determined by the GM. |
| 5 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/45` | 0.499159 | **aquatic** (trait) Aquatic creatures are at home underwater.  Their bludgeoning and slashing unarmed Strikes don't  take the usual –2 penalty for being underwater. Aquatic  creatures can breathe wate |
| 6 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/36` | 0.493928 | **aura** (trait) An aura is an emanation that continually ebbs out  from you, affecting creatures within a certain radius. Aura  can also refer to the magical signature of an item. |
| 7 | `PZO22001 Starfinder Player Core 442-464::/page/4/Text/55` | 0.483389 | **ethereal** (trait) Creatures with this trait are native to the Ethereal  plane. |
| 8 | `PZO22001 Starfinder Player Core 442-464::/page/3/Text/34` | 0.482563 | **darkness** Creatures and objects in darkness are hidden or  undetected, and creatures without darkvision have the  blinded condition in darkness. 424 |
| 9 | `PZO22001 Starfinder Player Core 442-464::/page/4/Text/37` | 0.481518 | **earth** (trait) Effects with the earth trait either manipulate or  conjure earth. Those that manipulate earth have no effect  in an area without earth. Creatures with this trait consist  primarily o |
| 10 | `PZO22001 Starfinder Player Core 442-464::/page/5/Text/20` | 0.471937 | **fey** (trait) Creatures of the First World are called the fey. |

### Query 3
- Text: What is the rule about **ability** A general term referring to rules that provide an  exception to the basic rules. An ability could come from a  number of sources, so "an ability that gives you a bonus to  damage rolls" could be a feat, a spell, and so on.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 442-464::/page/0/Text/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 442-464::/page/0/Text/5', 'PZO22001 Starfinder Player Core 442-464::/page/5/Text/13', 'PZO22001 Starfinder Player Core 442-464::/page/4/Text/39']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/5` | 1.011457 | **ability** A general term referring to rules that provide an  exception to the basic rules. An ability could come from a  number of sources, so "an ability that gives you a bonus to  damage rolls" co |
| 2 | `PZO22001 Starfinder Player Core 442-464::/page/5/Text/13` | 0.672762 | **feat** An ability you gain or select for your character due to  their ancestry, background, class, general training, or skill  training. Some feats grant special actions. 10, 16 |
| 3 | `PZO22001 Starfinder Player Core 442-464::/page/4/Text/39` | 0.661789 | **effect** An effect is the result of an ability, though an ability's  exact effect is sometimes contingent on the result of a  check or other roll. 418–419 |
| 4 | `PZO22001 Starfinder Player Core 442-464::/page/2/Text/33` | 0.589514 | **class feature** Any ability granted by a class is a class feature.  These mainly consist of class feats and other abilities  specific to the class. 100 |
| 5 | `PZO22001 Starfinder Player Core 442-464::/page/10/Text/18` | 0.583861 | **rare** (trait) This rarity indicates that a rules element is very  difficult to find in the game world. A rare feat, spell, item or  the like is available to players only if the GM decides to includ |
| 6 | `PZO22001 Starfinder Player Core 442-464::/page/6/Text/49` | 0.569206 | **incapacitation** (trait) An ability with this trait can take a  character completely out of the fight or even kill them, and  it's harder to use on a more powerful character. If a spell has  the inc |
| 7 | `PZO22001 Starfinder Player Core 442-464::/page/11/Text/35` | 0.554598 | **skill** (trait) A general feat with the skill trait improves your  skills and their actions or gives you new actions for a skill.  A feat with this trait can be selected when a class grants  a skill |
| 8 | `PZO22001 Starfinder Player Core 442-464::/page/11/Text/32` | 0.552435 | **skill** A statistic representing the ability to perform certain  tasks that require instruction or practice. Skill modifier  = modifier of the skill's key attribute score + proficiency  bonus + othe |
| 9 | `PZO22001 Starfinder Player Core 442-464::/page/5/Text/45` | 0.544088 | **frequency** An ability that can't be used at will might list a  frequency. 16 |
| 10 | `PZO22001 Starfinder Player Core 442-464::/page/5/Text/57` | 0.533650 | **general** (trait) A type of feat that any character can select,  regardless of ancestry and class, as long as they meet the  prerequisites. You can select a feat with this trait when  your class gra |

### Query 4
- Text: What is the rule about **Absalom Station** A space station which serves as a major hub  of trade and culture in the Pact Worlds. 31?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 442-464::/page/0/Text/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 442-464::/page/0/Text/6', 'PZO22001 Starfinder Player Core 442-464::/page/0/Text/3', 'PZO22001 Starfinder Player Core 442-464::/page/9/Text/10']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/6` | 0.945029 | **Absalom Station** A space station which serves as a major hub  of trade and culture in the Pact Worlds. 31 |
| 2 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/3` | 0.537207 | **Aballon** A rocky, sun-blasted planet of industry which is home to  intelligent machines created by the enigmatic First Ones. 31 |
| 3 | `PZO22001 Starfinder Player Core 442-464::/page/9/Text/10` | 0.482420 | **Pact Worlds** The governing body of planets that make up the  core of the primary Starfinder setting. 30–34 |
| 4 | `PZO22001 Starfinder Player Core 442-464::/page/6/Text/40` | 0.403114 | **Idari, the** A world ship which transported the kasatha from a  doomed planet to the Pact Worlds. 32 |
| 5 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/44` | 0.391742 | **Apostae** A hollow planetoid containing mysterious gateways to  tunnel networks and ancient mechanical complexes. 34 |
| 6 | `PZO22001 Starfinder Player Core 442-464::/page/10/Text/10` | 0.385704 | **Pulonis** A recently liberated, low-gravity jungle world in the  Veskarium which recently became a member of the Pact  Worlds. 34 |
| 7 | `PZO22001 Starfinder Player Core 442-464::/page/4/Text/52` | 0.369036 | **Eox **A radioactive wasteland of a planet ruled by the undead who  destroyed their once lush home world in a terrible disaster. 32 |
| 8 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/31` | 0.368772 | **Aucturn** A former Pact World planet that was destroyed  when the Newborn hatched from it. |
| 9 | `PZO22001 Starfinder Player Core 442-464::/page/4/Text/1` | 0.367925 | **Diaspora** An asteroid belt formed when the twin planets  Damiar and Iovo were destroyed, home to smugglers,  pirates, and sarcesians. 32 |
| 10 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/33` | 0.361828 | **ambiguous rules** 391 |

### Query 5
- Text: What is the rule about **abysium** (material) A glowing blue-green glowing metal that  damages creatures' immune system. 278?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 442-464::/page/0/Text/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 442-464::/page/0/Text/7', 'PZO22001 Starfinder Player Core 442-464::/page/11/Text/29', 'PZO22001 Starfinder Player Core 442-464::/page/1/Text/32']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/7` | 0.982547 | **abysium** (material) A glowing blue-green glowing metal that  damages creatures' immune system. 278 |
| 2 | `PZO22001 Starfinder Player Core 442-464::/page/11/Text/29` | 0.565956 | **sickened** (condition) You're sick to your stomach. 439 **silver** (material) A shiny metal that's dangerous to devils and  werecreatures. 279 |
| 3 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/32` | 0.535586 | **aucturnite** (material) A dull remnant of the planet Aucturn  that causes madness. 278 |
| 4 | `PZO22001 Starfinder Player Core 442-464::/page/8/Text/44` | 0.485530 | **nonplayer character (NPC)** A character controlled by the GM. 11 **noqual** (material) A light metal with anti-magic properties.  279 |
| 5 | `PZO22001 Starfinder Player Core 442-464::/page/2/Text/38` | 0.483943 | **cold iron** (material) Metal dangerous to devils and fey. 278–279 **comfort** (armor trait) 245 |
| 6 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/22` | 0.479149 | **adamantine** (material) One of the hardest known metals. 278 **Administer First Aid **[two-actions] (skill action) Stabilize a dying  creature or stanch bleeding. (Medicine) 201 |
| 7 | `PZO22001 Starfinder Player Core 442-464::/page/8/Text/9` | 0.474543 | **metal** (trait) Effects with the metal trait conjure or  manipulate metal. Those that manipulate metal have  no effect in an area without metal. Creatures with this  trait consist primarily of metal |
| 8 | `PZO22001 Starfinder Player Core 442-464::/page/6/Text/44` | 0.452910 | **immunity** An immunity causes a creature to ignore all  damage, effects, or conditions of a certain type. 400 object immunities 236 |
| 9 | `PZO22001 Starfinder Player Core 442-464::/page/9/Text/9` | 0.445141 | **operative** (trait) This indicates abilities from the operative class. **orichalcum** (material) A metal with strange temporal  properties. 279 |
| 10 | `PZO22001 Starfinder Player Core 442-464::/page/3/Text/34` | 0.429349 | **darkness** Creatures and objects in darkness are hidden or  undetected, and creatures without darkvision have the  blinded condition in darkness. 424 |

### Query 6
- Text: What is the rule about **AC (Armor Class)** *See also* Armor Class. 10, 268, 395–396?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 442-464::/page/0/Text/8']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 442-464::/page/0/Text/8', 'PZO22001 Starfinder Player Core 442-464::/page/1/Text/10', 'PZO22001 Starfinder Player Core 442-464::/page/1/Text/9']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/8` | 0.964641 | **AC (Armor Class)** *See also* Armor Class. 10, 268, 395–396 |
| 2 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/10` | 0.741522 | **Armor Class (AC)** This score represents how hard it is to hit  and damage a creature. It typically serves as the DC to hit a  creature with an attack. AC = 10 + Dex modifier (up to your  armor's De |
| 3 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/9` | 0.552260 | **armor** 244–249 |
| 4 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/2` | 0.501275 | **arc** (weapon trait) 255 |
| 5 | `PZO22001 Starfinder Player Core 442-464::/page/5/Text/4` | 0.487235 | **exposed** (armor trait) 245 |
| 6 | `PZO22001 Starfinder Player Core 442-464::/page/2/Text/31` | 0.475465 | **class** The adventuring profession chosen by a character. Each  player character picks a class during character creation.  10, 20, 28, **99–173** |
| 7 | `PZO22001 Starfinder Player Core 442-464::/page/10/Text/13` | 0.473418 | **Raise a Shield **[one-action] (specialty basic action) Gain your shield's  bonus to AC. 411 |
| 8 | `PZO22001 Starfinder Player Core 442-464::/page/2/Text/25` | 0.462286 | check penalty (penalty to skill checks imposed by armor) 245 degrees of success (critical success, success, failure,  critical failure) 393 |
| 9 | `PZO22001 Starfinder Player Core 442-464::/page/4/Text/5` | 0.460745 | **Difficulty Class (DC)** The number you need to succeed at a  check. To generate a DC from a modifier (like Perception  DC), add 10 to the modifier. 8, **393** |
| 10 | `PZO22001 Starfinder Player Core 442-464::/page/5/Text/28` | 0.460722 | **flexible** (armor trait) 245 |

### Query 7
- Text: What is the rule about **access** You can select an uncommon rules element if you  meet the criteria listed in its access entry. 11?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 442-464::/page/0/Text/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 442-464::/page/0/Text/9', 'PZO22001 Starfinder Player Core 442-464::/page/14/Text/7', 'PZO22001 Starfinder Player Core 442-464::/page/2/Text/40']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/9` | 0.949786 | **access** You can select an uncommon rules element if you  meet the criteria listed in its access entry. 11 |
| 2 | `PZO22001 Starfinder Player Core 442-464::/page/14/Text/7` | 0.624156 | **uncommon** (trait) Something of uncommon rarity requires  special training or comes from a particular culture or part of  the world. Some character choices give access to uncommon  options, and the |
| 3 | `PZO22001 Starfinder Player Core 442-464::/page/2/Text/40` | 0.563725 | **common** (trait) Anything that doesn't list another rarity trait  (uncommon, rare, or unique) automatically has the common  trait. This rarity indicates that an ability, item, or spell is  available |
| 4 | `PZO22001 Starfinder Player Core 442-464::/page/10/Text/18` | 0.517511 | **rare** (trait) This rarity indicates that a rules element is very  difficult to find in the game world. A rare feat, spell, item or  the like is available to players only if the GM decides to includ |
| 5 | `PZO22001 Starfinder Player Core 442-464::/page/10/Text/42` | 0.493031 | **requirements** Some abilities can be used only if you meet  their requirements. 16 |
| 6 | `PZO22001 Starfinder Player Core 442-464::/page/14/Text/14` | 0.472536 | **unique** (trait) A rules element with this trait is one-of-a-kind. 11 **unlimited** A spell with this duration lasts indefinitely. 300 |
| 7 | `PZO22001 Starfinder Player Core 442-464::/page/10/Text/19` | 0.461976 | **rarity** How often something is encountered in the game  world. The rarities are common, uncommon, rare, and  unique. Anything that doesn't list a rarity is common. 11 |
| 8 | `PZO22001 Starfinder Player Core 442-464::/page/5/Text/45` | 0.447341 | **frequency** An ability that can't be used at will might list a  frequency. 16 |
| 9 | `PZO22001 Starfinder Player Core 442-464::/page/5/Text/57` | 0.445747 | **general** (trait) A type of feat that any character can select,  regardless of ancestry and class, as long as they meet the  prerequisites. You can select a feat with this trait when  your class gra |
| 10 | `PZO22001 Starfinder Player Core 442-464::/page/10/Text/4` | 0.442014 | **prerequisites** Many feats and other abilities can be taken  only if you meet their prerequisites. Prerequisites are often  feats or proficiency ranks. 16 |

### Query 8
- Text: What is the rule about **Access Infosphere** (skill action) Search a network of  computers for information. (Computers) 195–196?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 442-464::/page/0/Text/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 442-464::/page/0/Text/10', 'PZO22001 Starfinder Player Core 442-464::/page/6/Text/9', 'PZO22001 Starfinder Player Core 442-464::/page/2/Text/42']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/10` | 0.961792 | **Access Infosphere** (skill action) Search a network of  computers for information. (Computers) 195–196 |
| 2 | `PZO22001 Starfinder Player Core 442-464::/page/6/Text/9` | 0.595093 | **Hack** (skill action) Attempt to access a secured computer.  (Computers) 196 |
| 3 | `PZO22001 Starfinder Player Core 442-464::/page/2/Text/42` | 0.591446 | **computers** (skill) Work with a computer system. (Int) 195–196 **Conceal an Object **[one-action] (skill action) Hide an object on your  person. (Stealth) 207 |
| 4 | `PZO22001 Starfinder Player Core 442-464::/page/9/Text/7` | 0.528699 | **Operate Device** (skill action) You perform a basic task with a  computer. (Computers) 196 |
| 5 | `PZO22001 Starfinder Player Core 442-464::/page/5/Text/54` | 0.517548 | **Gather Information** (skill action) Socialize to learn things.  (Diplomacy) 199 |
| 6 | `PZO22001 Starfinder Player Core 442-464::/page/10/Text/41` | 0.493019 | **Reposition **[one-action] (skill action) Move a creature within your reach 194 **Request **[one-action] (skill action) Get someone to help you. (Diplomacy)  199–200 |
| 7 | `PZO22001 Starfinder Player Core 442-464::/page/11/Text/12` | 0.492793 | **Search** (exploration activity) Look for hidden things. 432 **secret** (trait) The GM rolls the check for this ability in  secret. 397 |
| 8 | `PZO22001 Starfinder Player Core 442-464::/page/11/Text/13` | 0.465029 | **Seek **[one-action] (basic action) Scan an area for creatures or objects  using Perception. 409 |
| 9 | `PZO22001 Starfinder Player Core 442-464::/page/10/Text/28` | 0.462068 | **Recall Knowledge **[one-action] (skill action) 190–191 |
| 10 | `PZO22001 Starfinder Player Core 442-464::/page/3/Text/42` | 0.450394 | **Decipher Writing** (skill action) Understand obscure or coded  text. (Arcana, Occultism, Religion, Society; trained) 186 |

### Query 9
- Text: What is the rule about **acid** (damage type) 401?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 442-464::/page/0/Text/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 442-464::/page/0/Text/11', 'PZO22001 Starfinder Player Core 442-464::/page/14/Text/29', 'PZO22001 Starfinder Player Core 442-464::/page/9/Text/35']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/11` | 0.937399 | **acid** (damage type) 401 |
| 2 | `PZO22001 Starfinder Player Core 442-464::/page/14/Text/29` | 0.783338 | **void** (damage type) 401 |
| 3 | `PZO22001 Starfinder Player Core 442-464::/page/9/Text/35` | 0.771653 | **poison** (damage type) 401 |
| 4 | `PZO22001 Starfinder Player Core 442-464::/page/4/Text/40` | 0.701709 | **electricity** (damage type) 401 |
| 5 | `PZO22001 Starfinder Player Core 442-464::/page/5/Text/23` | 0.701574 | **fire** (damage type) 401 |
| 6 | `PZO22001 Starfinder Player Core 442-464::/page/14/Text/27` | 0.700155 | **vitality** (damage type) 401 |
| 7 | `PZO22001 Starfinder Player Core 442-464::/page/5/Text/35` | 0.692082 | **force** (damage type) 401 |
| 8 | `PZO22001 Starfinder Player Core 442-464::/page/8/Text/7` | 0.689130 | **mental** (damage type) 401 |
| 9 | `PZO22001 Starfinder Player Core 442-464::/page/3/Text/28` | 0.685223 | damage types 401 |
| 10 | `PZO22001 Starfinder Player Core 442-464::/page/12/Text/34` | 0.675557 | **spirit** (damage type) 401 |

### Query 10
- Text: What is the rule about **acid** (trait) Effects with this trait deal acid damage. Creatures  with this trait have a connection to magical acid.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 442-464::/page/0/Text/12']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 442-464::/page/0/Text/12', 'PZO22001 Starfinder Player Core 442-464::/page/2/Text/37', 'PZO22001 Starfinder Player Core 442-464::/page/4/Text/41']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/12` | 0.987899 | **acid** (trait) Effects with this trait deal acid damage. Creatures  with this trait have a connection to magical acid. |
| 2 | `PZO22001 Starfinder Player Core 442-464::/page/2/Text/37` | 0.736143 | **cold** (trait) Effects with this trait deal cold damage. Creatures  with this trait have a connection to magical cold. |
| 3 | `PZO22001 Starfinder Player Core 442-464::/page/4/Text/41` | 0.703125 | **electricity** (trait) Effects with this trait deal electricity  damage. A creature with this trait has a connection to  magical electricity. |
| 4 | `PZO22001 Starfinder Player Core 442-464::/page/14/Text/30` | 0.655342 | **void** (trait) Effects with this trait heal undead creatures  with void energy, deal void damage to living creatures, or  manipulate void energy. Creatures with this trait are natives  of the Void. |
| 5 | `PZO22001 Starfinder Player Core 442-464::/page/14/Text/34` | 0.653233 | **water** (trait) Effects with the water trait either manipulate  or conjure water. Those that manipulate water have  no effect in an area without water. Creatures with this  trait consist primarily o |
| 6 | `PZO22001 Starfinder Player Core 442-464::/page/14/Text/47` | 0.620107 | **wood** (trait) Effects with the wood trait conjure or manipulate  wood. Those that manipulate wood have no effect in an  area without wood. Creatures with this trait consist  primarily of wood or ha |
| 7 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/31` | 0.617097 | **Aid **[one-action[reaction][fre-actio (basic action) Improve an ally's skill check or attack. 408 **air** (trait) Effects with the air trait either manipulate or  conjure air. Those that manipulate |
| 8 | `PZO22001 Starfinder Player Core 442-464::/page/5/Text/24` | 0.600776 | **fire** (trait) Effects with the fire trait deal fire damage or either  conjure or manipulate fire. Those that manipulate fire have  no effect in an area without fire. Creatures with this trait  cons |
| 9 | `PZO22001 Starfinder Player Core 442-464::/page/9/Text/30` | 0.600710 | **plant** (trait) Vegetable creatures have the plant trait. They are  distinct from normal plants. Magical effects with this trait  manipulate or conjure plants or plant matter in some way.  Effects t |
| 10 | `PZO22001 Starfinder Player Core 442-464::/page/12/Text/35` | 0.598574 | **spirit** (trait) Effects with this trait can affect creatures  with spiritual essence and might deal spirit damage. A  creature with this trait is defined by its spiritual essence.  Spirit creatures |

### Query 11
- Text: What is the rule about **Acrobatics** (skill) Perform tasks requiring coordination and  grace. (Dex) 192–193?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 442-464::/page/0/Text/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 442-464::/page/0/Text/13', 'PZO22001 Starfinder Player Core 442-464::/page/15/TableCell/98', 'PZO22001 Starfinder Player Core 442-464::/page/1/Text/12']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/13` | 0.956876 | **Acrobatics** (skill) Perform tasks requiring coordination and  grace. (Dex) 192–193 |
| 2 | `PZO22001 Starfinder Player Core 442-464::/page/15/TableCell/98` | 0.654927 | Acrobatics ( |
| 3 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/12` | 0.635720 | **Athletics** (skill) Perform deeds of physical prowess. (Str) 193–195 **attack** (trait) An ability with this trait involves an attack. For  each attack you make beyond the first on your turn, you  t |
| 4 | `PZO22001 Starfinder Player Core 442-464::/page/12/Text/37` | 0.573457 | **squeeze** (skill action) Move through a gap while exploring.  (Acrobatics, trained) 192–193 |
| 5 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/43` | 0.541873 | **Balance **[one-action] (skill action) Move on a narrow or unstable  surface. (Acrobatics) 192 |
| 6 | `PZO22001 Starfinder Player Core 442-464::/page/10/Text/41` | 0.519981 | **Reposition **[one-action] (skill action) Move a creature within your reach 194 **Request **[one-action] (skill action) Get someone to help you. (Diplomacy)  199–200 |
| 7 | `PZO22001 Starfinder Player Core 442-464::/page/3/Text/10` | 0.515606 | **Craft** (skill action) Make an item. (Crafting, trained) **197–198**, 434 **Crafting** (skill) Create, understand, and repair items. (Int) 196–198 **Crawl **[one-action] (basic action) Move 5 feet w |
| 8 | `PZO22001 Starfinder Player Core 442-464::/page/10/Text/4` | 0.500348 | **prerequisites** Many feats and other abilities can be taken  only if you meet their prerequisites. Prerequisites are often  feats or proficiency ranks. 16 |
| 9 | `PZO22001 Starfinder Player Core 442-464::/page/6/Text/6` | 0.485711 | **Grapple **[one-action] (skill action) Grab or restrain a target. (Athletics) 194 **grenade** (weapon trait) 256 |
| 10 | `PZO22001 Starfinder Player Core 442-464::/page/7/Text/61` | 0.484489 | **Maneuver in Flight **[one-action] (skill action) Execute a difficult  movement while flying. (Acrobatics, trained) 192 |

### Query 12
- Text: What is the rule about **actions** Discrete tasks that generate a specific effect, possibly  requiring a check to determine the result. Actions can be  used to accomplish a variety of things, such as moving,  attacking, casting a spell, or interacting with an item or  object. Most creatures can use up to 3 actions during their  turn. 10, 15, **406–407**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 442-464::/page/0/Text/14']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 442-464::/page/0/Text/14', 'PZO22001 Starfinder Player Core 442-464::/page/14/Text/2', 'PZO22001 Starfinder Player Core 442-464::/page/0/Text/20']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/14` | 0.997420 | **actions** Discrete tasks that generate a specific effect, possibly  requiring a check to determine the result. Actions can be  used to accomplish a variety of things, such as moving,  attacking, cas |
| 2 | `PZO22001 Starfinder Player Core 442-464::/page/14/Text/2` | 0.743924 | **turn** During a round in an encounter, each creature takes a  single turn. A creature typically uses up to 3 actions during  its turn. 11, **427–428** |
| 3 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/20` | 0.704026 | **activity** A category of action that typically takes more than  a single action. Activities on your turn take 2 actions ([two-actions])  or 3 actions ([three-actions]). Exploration and downtime acti |
| 4 | `PZO22001 Starfinder Player Core 442-464::/page/11/Text/30` | 0.661576 | **single action **([one-action]) An action that takes one of your three  actions on your turn. 15, **406** |
| 5 | `PZO22001 Starfinder Player Core 442-464::/page/10/Text/25` | 0.644520 | **reaction** ([reaction]) An action you can use even if it's not your turn.  You can use 1 reaction per round. 15, **406** reactions in encounters 428–429 |
| 6 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/46` | 0.641328 | **basic action** An action all creatures can use. 408–410 |
| 7 | `PZO22001 Starfinder Player Core 442-464::/page/3/Text/10` | 0.616167 | **Craft** (skill action) Make an item. (Crafting, trained) **197–198**, 434 **Crafting** (skill) Create, understand, and repair items. (Int) 196–198 **Crawl **[one-action] (basic action) Move 5 feet w |
| 8 | `PZO22001 Starfinder Player Core 442-464::/page/4/Text/39` | 0.603210 | **effect** An effect is the result of an ability, though an ability's  exact effect is sometimes contingent on the result of a  check or other roll. 418–419 |
| 9 | `PZO22001 Starfinder Player Core 442-464::/page/10/Text/41` | 0.600375 | **Reposition **[one-action] (skill action) Move a creature within your reach 194 **Request **[one-action] (skill action) Get someone to help you. (Diplomacy)  199–200 |
| 10 | `PZO22001 Starfinder Player Core 442-464::/page/13/Text/35` | 0.600219 | **touch** A spell range requiring you to touch the target. 298 **Track** (skill action) Follow a creature's tracks. (Survival) 208–209 **tracking** (weapon trait) 258 |

### Query 13
- Text: What is the rule about activities 406?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 442-464::/page/0/Text/15']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 442-464::/page/0/Text/15', 'PZO22001 Starfinder Player Core 442-464::/page/0/Text/16', 'PZO22001 Starfinder Player Core 442-464::/page/0/Text/18']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/15` | 0.832911 | activities 406 |
| 2 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/16` | 0.601268 | basic actions 408–411 |
| 3 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/18` | 0.581896 | single action ([one-action]) *See also* single action. 406 |
| 4 | `PZO22001 Starfinder Player Core 442-464::/page/5/Text/3` | 0.523157 | exploration activities 430–432 |
| 5 | `PZO22001 Starfinder Player Core 442-464::/page/17/TableCell/305` | 0.511242 | Actions and Activities |
| 6 | `PZO22001 Starfinder Player Core 442-464::/page/4/Text/35` | 0.480020 | death and dying rules 402–404 |
| 7 | `PZO22001 Starfinder Player Core 442-464::/page/6/Text/54` | 0.474783 | delay (basic action) 408 |
| 8 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/20` | 0.468119 | **activity** A category of action that typically takes more than  a single action. Activities on your turn take 2 actions ([two-actions])  or 3 actions ([three-actions]). Exploration and downtime acti |
| 9 | `PZO22001 Starfinder Player Core 442-464::/page/11/Text/14` | 0.465106 | Search exploration activity 432 |
| 10 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/19` | 0.457297 | Strike (action) 410 |

### Query 14
- Text: What is the rule about basic actions 408–411?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 442-464::/page/0/Text/16']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 442-464::/page/0/Text/16', 'PZO22001 Starfinder Player Core 442-464::/page/1/Text/46', 'PZO22001 Starfinder Player Core 442-464::/page/6/Text/54']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/16` | 0.932388 | basic actions 408–411 |
| 2 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/46` | 0.720839 | **basic action** An action all creatures can use. 408–410 |
| 3 | `PZO22001 Starfinder Player Core 442-464::/page/6/Text/54` | 0.647471 | delay (basic action) 408 |
| 4 | `PZO22001 Starfinder Player Core 442-464::/page/4/Text/35` | 0.596925 | death and dying rules 402–404 |
| 5 | `PZO22001 Starfinder Player Core 442-464::/page/11/Text/48` | 0.570235 | **special battles** mounted, aerial, and aquatic combat 429 **specialty basic action** 410–411 |
| 6 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/19` | 0.542435 | Strike (action) 410 |
| 7 | `PZO22001 Starfinder Player Core 442-464::/page/8/Text/24` | 0.529349 | **movement** 412–414 |
| 8 | `PZO22001 Starfinder Player Core 442-464::/page/11/Text/23` | 0.518643 | Raise a Shield action 411 |
| 9 | `PZO22001 Starfinder Player Core 442-464::/page/11/Text/33` | 0.499831 | general skill actions 186–191 |
| 10 | `PZO22001 Starfinder Player Core 442-464::/page/5/Text/3` | 0.478079 | exploration activities 430–432 |

### Query 15
- Text: What is the rule about hostile actions 301?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 442-464::/page/0/Text/17']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 442-464::/page/0/Text/17', 'PZO22001 Starfinder Player Core 442-464::/page/6/Text/33', 'PZO22001 Starfinder Player Core 442-464::/page/13/Text/49']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/17` | 0.881203 | hostile actions 301 |
| 2 | `PZO22001 Starfinder Player Core 442-464::/page/6/Text/33` | 0.710802 | **hostile action** A hostile action is one that can harm or damage  another creature, whether directly or indirectly, but not  one that a creature is unaware could cause harm. 301 |
| 3 | `PZO22001 Starfinder Player Core 442-464::/page/13/Text/49` | 0.569817 | setting spell triggers 301 |
| 4 | `PZO22001 Starfinder Player Core 442-464::/page/6/Text/32` | 0.521420 | **hostile** (condition) A hostile NPC is likely to attack you. 437 |
| 5 | `PZO22001 Starfinder Player Core 442-464::/page/12/Text/17` | 0.515332 | setting triggers 301 |
| 6 | `PZO22001 Starfinder Player Core 442-464::/page/12/Text/7` | 0.506362 | counteracting 301, **423** |
| 7 | `PZO22001 Starfinder Player Core 442-464::/page/12/Text/29` | 0.459877 | walls 301 |
| 8 | `PZO22001 Starfinder Player Core 442-464::/page/14/Text/45` | 0.450978 | spell lists 302–305,307–310 |
| 9 | `PZO22001 Starfinder Player Core 442-464::/page/12/Text/25` | 0.447124 | spell stat block 301 |
| 10 | `PZO22001 Starfinder Player Core 442-464::/page/11/Text/23` | 0.427781 | Raise a Shield action 411 |

### Query 16
- Text: What is the rule about single action ([one-action]) *See also* single action. 406?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 442-464::/page/0/Text/18']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 442-464::/page/0/Text/18', 'PZO22001 Starfinder Player Core 442-464::/page/11/Text/30', 'PZO22001 Starfinder Player Core 442-464::/page/4/Text/27']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/18` | 0.952505 | single action ([one-action]) *See also* single action. 406 |
| 2 | `PZO22001 Starfinder Player Core 442-464::/page/11/Text/30` | 0.808408 | **single action **([one-action]) An action that takes one of your three  actions on your turn. 15, **406** |
| 3 | `PZO22001 Starfinder Player Core 442-464::/page/4/Text/27` | 0.626779 | **Drive** [one-action] to [three-actions] (skill action) Direct a vehicle to move.  (Piloting) 204 |
| 4 | `PZO22001 Starfinder Player Core 442-464::/page/10/Text/41` | 0.582697 | **Reposition **[one-action] (skill action) Move a creature within your reach 194 **Request **[one-action] (skill action) Get someone to help you. (Diplomacy)  199–200 |
| 5 | `PZO22001 Starfinder Player Core 442-464::/page/15/TableCell/228` | 0.578041 | Single Action Two-Action Activity |
| 6 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/46` | 0.577361 | **basic action** An action all creatures can use. 408–410 |
| 7 | `PZO22001 Starfinder Player Core 442-464::/page/12/Text/55` | 0.572402 | **Strike **[one-action] (basic action) Make an attack with a weapon or  unarmed attack. 410 |
| 8 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/20` | 0.565575 | **activity** A category of action that typically takes more than  a single action. Activities on your turn take 2 actions ([two-actions])  or 3 actions ([three-actions]). Exploration and downtime acti |
| 9 | `PZO22001 Starfinder Player Core 442-464::/page/5/Text/43` | 0.550048 | **free action** ([free-action]) An action you can use without spending one  of your actions. Free actions with triggers can be used at  any time, but they don't use up your 1 reaction per round.  15, |
| 10 | `PZO22001 Starfinder Player Core 442-464::/page/11/Text/16` | 0.549794 | **Sense Motive **[one-action] (basic action) Determine if a creature is  lying. 409 |

### Query 17
- Text: What is the rule about **active hands** Multi-armed characters can only designate one  pair of hands as your active hands. You can only wield  items in your active hands. *See *Switch Hands.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 442-464::/page/0/Text/19']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 442-464::/page/0/Text/19', 'PZO22001 Starfinder Player Core 442-464::/page/13/Text/19', 'PZO22001 Starfinder Player Core 442-464::/page/14/Text/40']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/19` | 0.978577 | **active hands** Multi-armed characters can only designate one  pair of hands as your active hands. You can only wield  items in your active hands. *See *Switch Hands. |
| 2 | `PZO22001 Starfinder Player Core 442-464::/page/13/Text/19` | 0.807392 | **Switch Hands** [one-action] (specialty basic action) You designate a pair  of limbs as your active hands. You can only have one pair  of hands designated as your active hands at a time. 254 |
| 3 | `PZO22001 Starfinder Player Core 442-464::/page/14/Text/40` | 0.606987 | **wield** You are wielding a weapon or shield whenever you are  holding it in the number of active hands needed to use it  effectively. 235 |
| 4 | `PZO22001 Starfinder Player Core 442-464::/page/8/Text/31` | 0.461966 | **multiclass** (trait) Archetypes with the multiclass trait  represent diversifying your training into another class's  specialties. You can't select a multiclass archetype's  dedication feat if you a |
| 5 | `PZO22001 Starfinder Player Core 442-464::/page/8/Text/32` | 0.461803 | **multiple attack penalty** You take this penalty on all attacks  after the first on your turn. This is a –5 penalty on your  second attack and –10 on all subsequent attacks (or –4 and  –8 if your wea |
| 6 | `PZO22001 Starfinder Player Core 442-464::/page/11/Text/30` | 0.460941 | **single action **([one-action]) An action that takes one of your three  actions on your turn. 15, **406** |
| 7 | `PZO22001 Starfinder Player Core 442-464::/page/14/Text/4` | 0.458954 | **two-hand** (weapon trait) 258 |
| 8 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/14` | 0.455310 | **actions** Discrete tasks that generate a specific effect, possibly  requiring a check to determine the result. Actions can be  used to accomplish a variety of things, such as moving,  attacking, cas |
| 9 | `PZO22001 Starfinder Player Core 442-464::/page/5/Text/43` | 0.455223 | **free action** ([free-action]) An action you can use without spending one  of your actions. Free actions with triggers can be used at  any time, but they don't use up your 1 reaction per round.  15, |
| 10 | `PZO22001 Starfinder Player Core 442-464::/page/4/Text/12` | 0.452690 | **Disable a Device **[two-actions] (skill action) Disable a trap or other  complex mechanism (Computers or Thievery, trained) 209 **disarm** (weapon trait) 256 |

### Query 18
- Text: What is the rule about **activity** A category of action that typically takes more than  a single action. Activities on your turn take 2 actions ([two-actions])  or 3 actions ([three-actions]). Exploration and downtime activities  can take minutes, hours, or days. 15–16, **406** exploration activities 430–432?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 442-464::/page/0/Text/20']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 442-464::/page/0/Text/20', 'PZO22001 Starfinder Player Core 442-464::/page/11/Text/30', 'PZO22001 Starfinder Player Core 442-464::/page/0/Text/14']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/20` | 0.998641 | **activity** A category of action that typically takes more than  a single action. Activities on your turn take 2 actions ([two-actions])  or 3 actions ([three-actions]). Exploration and downtime acti |
| 2 | `PZO22001 Starfinder Player Core 442-464::/page/11/Text/30` | 0.736500 | **single action **([one-action]) An action that takes one of your three  actions on your turn. 15, **406** |
| 3 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/14` | 0.720270 | **actions** Discrete tasks that generate a specific effect, possibly  requiring a check to determine the result. Actions can be  used to accomplish a variety of things, such as moving,  attacking, cas |
| 4 | `PZO22001 Starfinder Player Core 442-464::/page/4/Text/23` | 0.655981 | **downtime** A mode of play in which characters are not  adventuring. Days pass quickly at the table, and characters  engage in long-term activities. 9, 390–391, **433–434** downtime activities 433–43 |
| 5 | `PZO22001 Starfinder Player Core 442-464::/page/5/Text/2` | 0.646977 | **exploration** A mode of play used for traveling, investigating,  and otherwise exploring. The GM determines the flow of  time. 8–9, 390–391, **430–432** |
| 6 | `PZO22001 Starfinder Player Core 442-464::/page/5/Text/1` | 0.639918 | **exploration** (trait) Activities with this trait take more  than a turn to use and can usually be used only during  exploration mode. |
| 7 | `PZO22001 Starfinder Player Core 442-464::/page/8/Text/14` | 0.633953 | **mode of play** The three types of play in the game—encounters,  exploration, and downtime. Each has a different time scale  and degree of rules precision. 8–9, 390, **427–434** |
| 8 | `PZO22001 Starfinder Player Core 442-464::/page/14/Text/2` | 0.612317 | **turn** During a round in an encounter, each creature takes a  single turn. A creature typically uses up to 3 actions during  its turn. 11, **427–428** |
| 9 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/23` | 0.607183 | **adventure** A single narrative—including the setup, plot,  and conclusion. The player characters play through an  adventure over the course of one or more game sessions,  and the adventure might be |
| 10 | `PZO22001 Starfinder Player Core 442-464::/page/3/Text/10` | 0.599664 | **Craft** (skill action) Make an item. (Crafting, trained) **197–198**, 434 **Crafting** (skill) Create, understand, and repair items. (Int) 196–198 **Crawl **[one-action] (basic action) Move 5 feet w |

### Query 19
- Text: Summarize in encounters 428
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 442-464::/page/0/Text/21']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 442-464::/page/0/Text/21', 'PZO22001 Starfinder Player Core 442-464::/page/8/Text/27', 'PZO22001 Starfinder Player Core 442-464::/page/11/Text/14']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/21` | 0.902082 | in encounters 428 |
| 2 | `PZO22001 Starfinder Player Core 442-464::/page/8/Text/27` | 0.583480 | in encounters and on a grid 413 |
| 3 | `PZO22001 Starfinder Player Core 442-464::/page/11/Text/14` | 0.491000 | Search exploration activity 432 |
| 4 | `PZO22001 Starfinder Player Core 442-464::/page/6/Text/53` | 0.442788 | **initiative** At the start of an encounter, all participants  involved roll for initiative to determine the order in which  they act. 10, **427**, 428 |
| 5 | `PZO22001 Starfinder Player Core 442-464::/page/14/Text/10` | 0.437625 | **underwater combat** 429 |
| 6 | `PZO22001 Starfinder Player Core 442-464::/page/14/Text/2` | 0.426009 | **turn** During a round in an encounter, each creature takes a  single turn. A creature typically uses up to 3 actions during  its turn. 11, **427–428** |
| 7 | `PZO22001 Starfinder Player Core 442-464::/page/5/Text/3` | 0.424733 | exploration activities 430–432 |
| 8 | `PZO22001 Starfinder Player Core 442-464::/page/11/Text/10` | 0.414913 | **Scout** (exploration activity) Look ahead for danger. 432 |
| 9 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/1` | 0.414760 | **aquatic combat** 429 |
| 10 | `PZO22001 Starfinder Player Core 442-464::/page/12/Text/27` | 0.414180 | targets 298 |

### Query 20
- Text: What is the rule about **adamantine** (material) One of the hardest known metals. 278 **Administer First Aid **[two-actions] (skill action) Stabilize a dying  creature or stanch bleeding. (Medicine) 201?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 442-464::/page/0/Text/22']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 442-464::/page/0/Text/22', 'PZO22001 Starfinder Player Core 442-464::/page/11/Text/28', 'PZO22001 Starfinder Player Core 442-464::/page/11/Text/29']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/22` | 0.993749 | **adamantine** (material) One of the hardest known metals. 278 **Administer First Aid **[two-actions] (skill action) Stabilize a dying  creature or stanch bleeding. (Medicine) 201 |
| 2 | `PZO22001 Starfinder Player Core 442-464::/page/11/Text/28` | 0.621229 | **Shove **[one-action] (skill action) Push a creature. (Athletics) 194–195 **siccatite** (material) A metal that can be refined to hold heat or  cold especially well. 279 |
| 3 | `PZO22001 Starfinder Player Core 442-464::/page/11/Text/29` | 0.610123 | **sickened** (condition) You're sick to your stomach. 439 **silver** (material) A shiny metal that's dangerous to devils and  werecreatures. 279 |
| 4 | `PZO22001 Starfinder Player Core 442-464::/page/8/Text/5` | 0.557375 | **Medicine** (skill) Heal people and help them recover from  afflictions. (Wis) 201–202 |
| 5 | `PZO22001 Starfinder Player Core 442-464::/page/3/Text/48` | 0.545099 | **Demoralize **[one-action] (skill action) Frighten enemies. (Intimidation) 200 **Detect Magic** (exploration activity) Repeatedly *detect magic*.  430–431 |
| 6 | `PZO22001 Starfinder Player Core 442-464::/page/13/Text/13` | 0.531818 | **Survival** (skill) Travel and survive in the wild. (Wis) 208–209 **Sustain **[one-action] (specialty basic action) Extend the duration of an  effect that can be Sustained. 300, **411** |
| 7 | `PZO22001 Starfinder Player Core 442-464::/page/9/Text/9` | 0.529861 | **operative** (trait) This indicates abilities from the operative class. **orichalcum** (material) A metal with strange temporal  properties. 279 |
| 8 | `PZO22001 Starfinder Player Core 442-464::/page/10/Text/41` | 0.526004 | **Reposition **[one-action] (skill action) Move a creature within your reach 194 **Request **[one-action] (skill action) Get someone to help you. (Diplomacy)  199–200 |
| 9 | `PZO22001 Starfinder Player Core 442-464::/page/10/Text/39` | 0.524640 | **Repair** (skill action) Fix a broken or damaged item. (Crafting)  196 |
| 10 | `PZO22001 Starfinder Player Core 442-464::/page/3/Text/10` | 0.522006 | **Craft** (skill action) Make an item. (Crafting, trained) **197–198**, 434 **Crafting** (skill) Create, understand, and repair items. (Int) 196–198 **Crawl **[one-action] (basic action) Move 5 feet w |

### Query 21
- Text: What is the rule about **adventure** A single narrative—including the setup, plot,  and conclusion. The player characters play through an  adventure over the course of one or more game sessions,  and the adventure might be part of a larger campaign. 7?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 442-464::/page/0/Text/23']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 442-464::/page/0/Text/23', 'PZO22001 Starfinder Player Core 442-464::/page/2/Text/14', 'PZO22001 Starfinder Player Core 442-464::/page/1/Text/40']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/23` | 0.961385 | **adventure** A single narrative—including the setup, plot,  and conclusion. The player characters play through an  adventure over the course of one or more game sessions,  and the adventure might be |
| 2 | `PZO22001 Starfinder Player Core 442-464::/page/2/Text/14` | 0.729084 | **campaign** A serialized story focusing on a single party of  characters and taking place over multiple adventures. 7 |
| 3 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/40` | 0.635278 | **background** The experiences your character had before  becoming an adventurer. Each player character chooses a  background during character creation. 10, 20, **92–96** |
| 4 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/20` | 0.592264 | **activity** A category of action that typically takes more than  a single action. Activities on your turn take 2 actions ([two-actions])  or 3 actions ([three-actions]). Exploration and downtime acti |
| 5 | `PZO22001 Starfinder Player Core 442-464::/page/5/Text/2` | 0.586460 | **exploration** A mode of play used for traveling, investigating,  and otherwise exploring. The GM determines the flow of  time. 8–9, 390–391, **430–432** |
| 6 | `PZO22001 Starfinder Player Core 442-464::/page/4/Text/23` | 0.584280 | **downtime** A mode of play in which characters are not  adventuring. Days pass quickly at the table, and characters  engage in long-term activities. 9, 390–391, **433–434** downtime activities 433–43 |
| 7 | `PZO22001 Starfinder Player Core 442-464::/page/10/Text/52` | 0.581835 | **roleplaying game (RPG)** An interactive story where one player,  the Game Master (GM), sets the scene and presents challenges,  while other players take the roles of player characters (PCs)  and att |
| 8 | `PZO22001 Starfinder Player Core 442-464::/page/2/Text/31` | 0.568275 | **class** The adventuring profession chosen by a character. Each  player character picks a class during character creation.  10, 20, 28, **99–173** |
| 9 | `PZO22001 Starfinder Player Core 442-464::/page/8/Text/14` | 0.556849 | **mode of play** The three types of play in the game—encounters,  exploration, and downtime. Each has a different time scale  and degree of rules precision. 8–9, 390, **427–434** |
| 10 | `PZO22001 Starfinder Player Core 442-464::/page/9/Text/32` | 0.538472 | **player character (character or PC)** A character created and  controlled by a player other than the GM. 11 |

### Query 22
- Text: Summarize **adventuring gear** 238–243
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 442-464::/page/0/Text/24']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 442-464::/page/0/Text/24', 'PZO22001 Starfinder Player Core 442-464::/page/5/Text/55', 'PZO22001 Starfinder Player Core 442-464::/page/13/Text/25']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/24` | 1.018905 | **adventuring gear** 238–243 |
| 2 | `PZO22001 Starfinder Player Core 442-464::/page/5/Text/55` | 0.888795 | **gear** *See also* item. 23, **233–293** adventuring gear 238–243 |
| 3 | `PZO22001 Starfinder Player Core 442-464::/page/13/Text/25` | 0.823882 | **tech gear** 238–243 |
| 4 | `PZO22001 Starfinder Player Core 442-464::/page/4/Text/53` | 0.647895 | **equipment** *See also* items. 23, **233–293** |
| 5 | `PZO22001 Starfinder Player Core 442-464::/page/7/Text/11` | 0.607293 | carrying, wearing, and wielding 234–235 |
| 6 | `PZO22001 Starfinder Player Core 442-464::/page/8/Text/4` | 0.605826 | **medical items** 241–243 |
| 7 | `PZO22001 Starfinder Player Core 442-464::/page/13/Text/34` | 0.601311 | **toolkit** 238–240 |
| 8 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/9` | 0.597956 | **armor** 244–249 |
| 9 | `PZO22001 Starfinder Player Core 442-464::/page/7/Text/25` | 0.574470 | weapons 253–267 |
| 10 | `PZO22001 Starfinder Player Core 442-464::/page/7/Text/8` | 0.552207 | armor 244–249 |

### Query 23
- Text: What is the rule about **aeon** (weapon trait) 255?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 442-464::/page/0/Text/25']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 442-464::/page/0/Text/25', 'PZO22001 Starfinder Player Core 442-464::/page/1/Text/37', 'PZO22001 Starfinder Player Core 442-464::/page/0/Text/29']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/25` | 0.943316 | **aeon** (weapon trait) 255 |
| 2 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/37` | 0.745292 | **automatic** (weapon trait) 255 |
| 3 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/29` | 0.716345 | **agile** (weapon trait) 255 |
| 4 | `PZO22001 Starfinder Player Core 442-464::/page/2/Text/4` | 0.659076 | **breakdown** (weapon trait) 255 |
| 5 | `PZO22001 Starfinder Player Core 442-464::/page/2/Text/1` | 0.655274 | **boost** (weapon trait) 255 |
| 6 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/42` | 0.652604 | **backswing** (weapon trait) 255 |
| 7 | `PZO22001 Starfinder Player Core 442-464::/page/3/Text/16` | 0.652185 | **critical** (weapon trait) 256 |
| 8 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/2` | 0.648475 | **arc** (weapon trait) 255 |
| 9 | `PZO22001 Starfinder Player Core 442-464::/page/13/Text/31` | 0.646826 | **thought** (weapon trait) 258 |
| 10 | `PZO22001 Starfinder Player Core 442-464::/page/10/Text/7` | 0.645665 | **professional** (weapon trait) 256 |

### Query 24
- Text: Summarize **aerial combat** 429
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 442-464::/page/0/Text/26']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 442-464::/page/0/Text/26', 'PZO22001 Starfinder Player Core 442-464::/page/11/Text/48', 'PZO22001 Starfinder Player Core 442-464::/page/1/Text/1']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/26` | 1.005062 | **aerial combat** 429 |
| 2 | `PZO22001 Starfinder Player Core 442-464::/page/11/Text/48` | 0.735632 | **special battles** mounted, aerial, and aquatic combat 429 **specialty basic action** 410–411 |
| 3 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/1` | 0.730817 | **aquatic combat** 429 |
| 4 | `PZO22001 Starfinder Player Core 442-464::/page/5/Text/30` | 0.686580 | **fly **[one-action] (specialty basic action) Move up to your fly Speed. 411 aerial combat 429 |
| 5 | `PZO22001 Starfinder Player Core 442-464::/page/14/Text/10` | 0.668955 | **underwater combat** 429 |
| 6 | `PZO22001 Starfinder Player Core 442-464::/page/8/Text/22` | 0.558335 | **Mount **[one-action] (specialty basic action) Ride an allied creature. 411 **mounted combat** 429 |
| 7 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/25` | 0.514368 | **aeon** (weapon trait) 255 |
| 8 | `PZO22001 Starfinder Player Core 442-464::/page/13/Text/9` | 0.502105 | **suffocating** 429 |
| 9 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/8` | 0.501260 | **Area Fire **[two-actions] (specialty basic action) Hit each creature in a  designated area. 156, 255, **410** |
| 10 | `PZO22001 Starfinder Player Core 442-464::/page/6/SectionHeader/30` | 0.496299 | **holding your breath** 429 |

### Query 25
- Text: Summarize **affliction** An affliction can affect a creature for a long time,  over several different stages. The most common kinds are  curses, diseases, and poisons. 422–423
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 442-464::/page/0/Text/27']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 442-464::/page/0/Text/27', 'PZO22001 Starfinder Player Core 442-464::/page/12/Text/39', 'PZO22001 Starfinder Player Core 442-464::/page/11/Text/37']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/27` | 1.038250 | **affliction** An affliction can affect a creature for a long time,  over several different stages. The most common kinds are  curses, diseases, and poisons. 422–423 |
| 2 | `PZO22001 Starfinder Player Core 442-464::/page/12/Text/39` | 0.608380 | **stage** One of the steps of an affliction. 422 |
| 3 | `PZO22001 Starfinder Player Core 442-464::/page/11/Text/37` | 0.582720 | **slashing** (damage type) A type of physical damage. 401 **sleep** (trait) This effect causes a creature to sleep or get drowsy. **slowed** (condition) You lose actions each turn. 439 **Small** (size |
| 4 | `PZO22001 Starfinder Player Core 442-464::/page/9/Text/5` | 0.528643 | **onset** The delay before an affliction, elixir, or potion takes  effect. 422 |
| 5 | `PZO22001 Starfinder Player Core 442-464::/page/6/Text/44` | 0.506465 | **immunity** An immunity causes a creature to ignore all  damage, effects, or conditions of a certain type. 400 object immunities 236 |
| 6 | `PZO22001 Starfinder Player Core 442-464::/page/14/Text/13` | 0.505474 | **unfriendly** (condition) An unfriendly NPC doesn't like you. 441 **unholy** (trait) If a creature with weakness to unholy uses a  holy item or effect, it takes damage from its weakness. **39** |
| 7 | `PZO22001 Starfinder Player Core 442-464::/page/9/Text/4` | 0.496351 | **olfactory** (trait) An olfactory effect can affect only creatures  that can smell it. This applies only to olfactory parts of the  effect, as determined by the GM. |
| 8 | `PZO22001 Starfinder Player Core 442-464::/page/12/Text/35` | 0.495296 | **spirit** (trait) Effects with this trait can affect creatures  with spiritual essence and might deal spirit damage. A  creature with this trait is defined by its spiritual essence.  Spirit creatures |
| 9 | `PZO22001 Starfinder Player Core 442-464::/page/11/Text/29` | 0.493634 | **sickened** (condition) You're sick to your stomach. 439 **silver** (material) A shiny metal that's dangerous to devils and  werecreatures. 279 |
| 10 | `PZO22001 Starfinder Player Core 442-464::/page/6/Text/10` | 0.480206 | **Hardness** A statistic representing an object's durability. 236 **haunt** (trait) A hazard with this trait is a spiritual echo, often  of someone with a tragic death. |

### Query 26
- Text: Summarize **age** 25
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 442-464::/page/0/Text/28']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 442-464::/page/0/Text/28', 'PZO22001 Starfinder Player Core 442-464::/page/5/Text/56', 'PZO22001 Starfinder Player Core 442-464::/page/17/TableCell/202']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/28` | 0.926080 | **age** 25 |
| 2 | `PZO22001 Starfinder Player Core 442-464::/page/5/Text/56` | 0.587023 | **gender and pronouns** 25 |
| 3 | `PZO22001 Starfinder Player Core 442-464::/page/17/TableCell/202` | 0.505421 | Age |
| 4 | `PZO22001 Starfinder Player Core 442-464::/page/11/Text/21` | 0.462465 | **shields** 250–252 |
| 5 | `PZO22001 Starfinder Player Core 442-464::/page/14/Text/36` | 0.435989 | critical specialization 258–259 |
| 6 | `PZO22001 Starfinder Player Core 442-464::/page/14/Text/4` | 0.418487 | **two-hand** (weapon trait) 258 |
| 7 | `PZO22001 Starfinder Player Core 442-464::/page/13/Text/31` | 0.415254 | **thought** (weapon trait) 258 |
| 8 | `PZO22001 Starfinder Player Core 442-464::/page/7/Text/18` | 0.410079 | shields 250–252 |
| 9 | `PZO22001 Starfinder Player Core 442-464::/page/14/Text/32` | 0.408780 | **volley** (weapon trait) 258 |
| 10 | `PZO22001 Starfinder Player Core 442-464::/page/10/Text/21` | 0.407503 | **razing** (weapon trait) 258 |

### Query 27
- Text: What is the rule about **agile** (weapon trait) 255?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 442-464::/page/0/Text/29']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 442-464::/page/0/Text/29', 'PZO22001 Starfinder Player Core 442-464::/page/1/Text/37', 'PZO22001 Starfinder Player Core 442-464::/page/3/Text/16']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/29` | 0.930173 | **agile** (weapon trait) 255 |
| 2 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/37` | 0.769173 | **automatic** (weapon trait) 255 |
| 3 | `PZO22001 Starfinder Player Core 442-464::/page/3/Text/16` | 0.707998 | **critical** (weapon trait) 256 |
| 4 | `PZO22001 Starfinder Player Core 442-464::/page/10/Text/7` | 0.664425 | **professional** (weapon trait) 256 |
| 5 | `PZO22001 Starfinder Player Core 442-464::/page/13/Text/31` | 0.651055 | **thought** (weapon trait) 258 |
| 6 | `PZO22001 Starfinder Player Core 442-464::/page/9/Text/42` | 0.645008 | **powered** (weapon trait) 256 |
| 7 | `PZO22001 Starfinder Player Core 442-464::/page/14/Text/38` | 0.644856 | weapon traits 255–258 |
| 8 | `PZO22001 Starfinder Player Core 442-464::/page/13/Text/39` | 0.644856 | weapon traits 255–258 |
| 9 | `PZO22001 Starfinder Player Core 442-464::/page/2/Text/4` | 0.641844 | **breakdown** (weapon trait) 255 |
| 10 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/2` | 0.640970 | **arc** (weapon trait) 255 |

### Query 28
- Text: Summarize **Akiton** A red desert planet often defined by its economic  decline due to changes in starship technology. 32
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 442-464::/page/0/Text/30']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 442-464::/page/0/Text/30', 'PZO22001 Starfinder Player Core 442-464::/page/0/Text/3', 'PZO22001 Starfinder Player Core 442-464::/page/1/Text/31']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/30` | 1.042036 | **Akiton** A red desert planet often defined by its economic  decline due to changes in starship technology. 32 |
| 2 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/3` | 0.570576 | **Aballon** A rocky, sun-blasted planet of industry which is home to  intelligent machines created by the enigmatic First Ones. 31 |
| 3 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/31` | 0.570018 | **Aucturn** A former Pact World planet that was destroyed  when the Newborn hatched from it. |
| 4 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/32` | 0.504261 | **aucturnite** (material) A dull remnant of the planet Aucturn  that causes madness. 278 |
| 5 | `PZO22001 Starfinder Player Core 442-464::/page/4/Text/1` | 0.498733 | **Diaspora** An asteroid belt formed when the twin planets  Damiar and Iovo were destroyed, home to smugglers,  pirates, and sarcesians. 32 |
| 6 | `PZO22001 Starfinder Player Core 442-464::/page/4/Text/52` | 0.477403 | **Eox **A radioactive wasteland of a planet ruled by the undead who  destroyed their once lush home world in a terrible disaster. 32 |
| 7 | `PZO22001 Starfinder Player Core 442-464::/page/14/Text/22` | 0.476835 | **Verces** A tidally locked planet which is half frozen and half desert,  with a world-spanning Ring of Nations between the two. 32 |
| 8 | `PZO22001 Starfinder Player Core 442-464::/page/13/Text/47` | 0.475614 | **Triaxus** A planet defined by its long seasons and high  population of dragons. 33 |
| 9 | `PZO22001 Starfinder Player Core 442-464::/page/9/Text/10` | 0.460614 | **Pact Worlds** The governing body of planets that make up the  core of the primary Starfinder setting. 30–34 |
| 10 | `PZO22001 Starfinder Player Core 442-464::/page/2/Text/18` | 0.453082 | **Castrovel** A jungle planet teeming with psychic energy which  is home to elves, lashunta, and formians. 31 |

### Query 29
- Text: What is the rule about **Aid **[one-action[reaction][fre-actio (basic action) Improve an ally's skill check or attack. 408 **air** (trait) Effects with the air trait either manipulate or  conjure air. Those that manipulate air have no effect in a  vacuum or an area without air. Creatures with this trait  consist primarily of air or have a connection to magical air.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 442-464::/page/0/Text/31']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 442-464::/page/0/Text/31', 'PZO22001 Starfinder Player Core 442-464::/page/5/Text/24', 'PZO22001 Starfinder Player Core 442-464::/page/14/Text/47']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/31` | 0.983581 | **Aid **[one-action[reaction][fre-actio (basic action) Improve an ally's skill check or attack. 408 **air** (trait) Effects with the air trait either manipulate or  conjure air. Those that manipulate |
| 2 | `PZO22001 Starfinder Player Core 442-464::/page/5/Text/24` | 0.712632 | **fire** (trait) Effects with the fire trait deal fire damage or either  conjure or manipulate fire. Those that manipulate fire have  no effect in an area without fire. Creatures with this trait  cons |
| 3 | `PZO22001 Starfinder Player Core 442-464::/page/14/Text/47` | 0.703734 | **wood** (trait) Effects with the wood trait conjure or manipulate  wood. Those that manipulate wood have no effect in an  area without wood. Creatures with this trait consist  primarily of wood or ha |
| 4 | `PZO22001 Starfinder Player Core 442-464::/page/14/Text/34` | 0.647065 | **water** (trait) Effects with the water trait either manipulate  or conjure water. Those that manipulate water have  no effect in an area without water. Creatures with this  trait consist primarily o |
| 5 | `PZO22001 Starfinder Player Core 442-464::/page/4/Text/37` | 0.644374 | **earth** (trait) Effects with the earth trait either manipulate or  conjure earth. Those that manipulate earth have no effect  in an area without earth. Creatures with this trait consist  primarily o |
| 6 | `PZO22001 Starfinder Player Core 442-464::/page/8/Text/1` | 0.642055 | **manipulate** (trait) Actions with this trait require you to  physically manipulate an item or make gestures to use.  Creatures without a suitable appendage can't perform  actions with this trait. Ma |
| 7 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/12` | 0.636699 | **acid** (trait) Effects with this trait deal acid damage. Creatures  with this trait have a connection to magical acid. |
| 8 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/14` | 0.610048 | **actions** Discrete tasks that generate a specific effect, possibly  requiring a check to determine the result. Actions can be  used to accomplish a variety of things, such as moving,  attacking, cas |
| 9 | `PZO22001 Starfinder Player Core 442-464::/page/9/Text/30` | 0.608519 | **plant** (trait) Vegetable creatures have the plant trait. They are  distinct from normal plants. Magical effects with this trait  manipulate or conjure plants or plant matter in some way.  Effects t |
| 10 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/46` | 0.608515 | **basic action** An action all creatures can use. 408–410 |

### Query 30
- Text: Summarize **ally** An ally is someone on your side. You are not counted as  your own ally. 418
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 442-464::/page/0/Text/32']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 442-464::/page/0/Text/32', 'PZO22001 Starfinder Player Core 442-464::/page/5/Text/25', 'PZO22001 Starfinder Player Core 442-464::/page/6/Text/20']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/32` | 1.030995 | **ally** An ally is someone on your side. You are not counted as  your own ally. 418 |
| 2 | `PZO22001 Starfinder Player Core 442-464::/page/5/Text/25` | 0.574171 | **flanking** When two creatures are on opposite sides of an enemy,  the enemy becomes off-guard to those creatures. 417 |
| 3 | `PZO22001 Starfinder Player Core 442-464::/page/6/Text/20` | 0.565012 | **helpful** (condition) A helpful NPC is likely to assist you. 437 **heritage** A choice made to further define your ancestry. 41 |
| 4 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/31` | 0.497502 | **Aid **[one-action[reaction][fre-actio (basic action) Improve an ally's skill check or attack. 408 **air** (trait) Effects with the air trait either manipulate or  conjure air. Those that manipulate |
| 5 | `PZO22001 Starfinder Player Core 442-464::/page/14/Text/40` | 0.482038 | **wield** You are wielding a weapon or shield whenever you are  holding it in the number of active hands needed to use it  effectively. 235 |
| 6 | `PZO22001 Starfinder Player Core 442-464::/page/6/Text/32` | 0.468197 | **hostile** (condition) A hostile NPC is likely to attack you. 437 |
| 7 | `PZO22001 Starfinder Player Core 442-464::/page/8/Text/22` | 0.462001 | **Mount **[one-action] (specialty basic action) Ride an allied creature. 411 **mounted combat** 429 |
| 8 | `PZO22001 Starfinder Player Core 442-464::/page/17/TableCell/282` | 0.460503 | Allies |
| 9 | `PZO22001 Starfinder Player Core 442-464::/page/10/Text/9` | 0.458858 | **prone** (condition) You're lying on the ground. 439 |
| 10 | `PZO22001 Starfinder Player Core 442-464::/page/2/Text/49` | 0.455872 | **confused** (condition) You attack indiscriminately. 435 |

### Query 31
- Text: Summarize **ambiguous rules** 391
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 442-464::/page/0/Text/33']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 442-464::/page/0/Text/33', 'PZO22001 Starfinder Player Core 442-464::/page/11/Text/3', 'PZO22001 Starfinder Player Core 442-464::/page/8/Text/33']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/33` | 0.993589 | **ambiguous rules** 391 |
| 2 | `PZO22001 Starfinder Player Core 442-464::/page/11/Text/3` | 0.706672 | **rules overview** 390–391 |
| 3 | `PZO22001 Starfinder Player Core 442-464::/page/8/Text/33` | 0.627763 | **multiplying** 391 |
| 4 | `PZO22001 Starfinder Player Core 442-464::/page/3/Text/3` | 0.572115 | **conventions** 391 |
| 5 | `PZO22001 Starfinder Player Core 442-464::/page/5/Text/51` | 0.545494 | **game conventions** 391 |
| 6 | `PZO22001 Starfinder Player Core 442-464::/page/11/Text/1` | 0.528615 | **rounding** 391 |
| 7 | `PZO22001 Starfinder Player Core 442-464::/page/4/Text/31` | 0.507187 | **duplicate effects** 391 |
| 8 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/45` | 0.492902 | **baseline** 389 |
| 9 | `PZO22001 Starfinder Player Core 442-464::/page/12/Text/20` | 0.490380 | bonus + other bonuses + penalties) 395 |
| 10 | `PZO22001 Starfinder Player Core 442-464::/page/13/Text/10` | 0.455450 | **summon** (trait) 370 |

### Query 32
- Text: What is the rule about **ammunition** usually stored in magazine or battery, 254–255 **amphibious** (trait) An amphibious creature can breathe in water  and in air, even outside of its preferred environment, usually  indefinitely but at least for hours. These creatures often have  a swim Speed. Their bludgeoning and slashing unarmed  Strikes don't take the usual –2 penalty for being underwater.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 442-464::/page/0/Text/34']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 442-464::/page/0/Text/34', 'PZO22001 Starfinder Player Core 442-464::/page/0/Text/45', 'PZO22001 Starfinder Player Core 442-464::/page/3/Text/4']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/34` | 0.993705 | **ammunition** usually stored in magazine or battery, 254–255 **amphibious** (trait) An amphibious creature can breathe in water  and in air, even outside of its preferred environment, usually  indefi |
| 2 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/45` | 0.711335 | **aquatic** (trait) Aquatic creatures are at home underwater.  Their bludgeoning and slashing unarmed Strikes don't  take the usual –2 penalty for being underwater. Aquatic  creatures can breathe wate |
| 3 | `PZO22001 Starfinder Player Core 442-464::/page/3/Text/4` | 0.546067 | **cosmic **(trait) Creatures with this trait can survive in the  harsh vacuum of space and the vast distances between  planets and stars. They don't breathe while in space  or in a vacuum. Creatures w |
| 4 | `PZO22001 Starfinder Player Core 442-464::/page/14/Text/10` | 0.473670 | **underwater combat** 429 |
| 5 | `PZO22001 Starfinder Player Core 442-464::/page/13/Text/18` | 0.465293 | **Swim **[one-action] (skill action) Move through the water. (Athletics) 195 aquatic combat 429 swim Speed 412 |
| 6 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/1` | 0.452547 | **aquatic combat** 429 |
| 7 | `PZO22001 Starfinder Player Core 442-464::/page/13/Text/2` | 0.449021 | The structure doesn't harm creatures within the area when  it appears, and it can't be created within a crowd or in a densely  populated area. Any creature inadvertently caught inside the  structure w |
| 8 | `PZO22001 Starfinder Player Core 442-464::/page/13/Text/13` | 0.443548 | **Survival** (skill) Travel and survive in the wild. (Wis) 208–209 **Sustain **[one-action] (specialty basic action) Extend the duration of an  effect that can be Sustained. 300, **411** |
| 9 | `PZO22001 Starfinder Player Core 442-464::/page/6/Text/5` | 0.442899 | **grabbed** (condition) something holds you in place. 437 **grapple** (weapon trait) 256 |
| 10 | `PZO22001 Starfinder Player Core 442-464::/page/13/Text/31` | 0.440081 | **thought** (weapon trait) 258 |

### Query 33
- Text: What is the rule about **analog** (trait) 245, 250, 255?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 442-464::/page/0/Text/35']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 442-464::/page/0/Text/35', 'PZO22001 Starfinder Player Core 442-464::/page/1/Text/5', 'PZO22001 Starfinder Player Core 442-464::/page/1/Text/37']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/35` | 0.934206 | **analog** (trait) 245, 250, 255 |
| 2 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/5` | 0.703560 | **archaic** (item trait) 245, 250, 255 |
| 3 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/37` | 0.596349 | **automatic** (weapon trait) 255 |
| 4 | `PZO22001 Starfinder Player Core 442-464::/page/5/Text/28` | 0.540229 | **flexible** (armor trait) 245 |
| 5 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/29` | 0.539334 | **agile** (weapon trait) 255 |
| 6 | `PZO22001 Starfinder Player Core 442-464::/page/11/Text/18` | 0.538065 | **serum** (trait) 242–243 |
| 7 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/25` | 0.534700 | **aeon** (weapon trait) 255 |
| 8 | `PZO22001 Starfinder Player Core 442-464::/page/3/Text/16` | 0.517216 | **critical** (weapon trait) 256 |
| 9 | `PZO22001 Starfinder Player Core 442-464::/page/8/Text/42` | 0.516886 | **nonlethal** (trait) 256, **399** |
| 10 | `PZO22001 Starfinder Player Core 442-464::/page/10/Text/7` | 0.516108 | **professional** (weapon trait) 256 |

### Query 34
- Text: What is the rule about **Analyze Environment** (exploration activity) check if your  environment is safe. 430?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 442-464::/page/0/Text/36']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 442-464::/page/0/Text/36', 'PZO22001 Starfinder Player Core 442-464::/page/11/Text/10', 'PZO22001 Starfinder Player Core 442-464::/page/7/Text/6']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/36` | 0.946444 | **Analyze Environment** (exploration activity) check if your  environment is safe. 430 |
| 2 | `PZO22001 Starfinder Player Core 442-464::/page/11/Text/10` | 0.629379 | **Scout** (exploration activity) Look ahead for danger. 432 |
| 3 | `PZO22001 Starfinder Player Core 442-464::/page/7/Text/6` | 0.581879 | **Investigate** (exploration activity) Study your surroundings. 431 **invisible** (condition) Creatures can't see you. 426, **438** |
| 4 | `PZO22001 Starfinder Player Core 442-464::/page/13/Text/14` | 0.526066 | **Sustain an Effect** (exploration activity) Repeatedly Sustain an  effect as you move. 432 |
| 5 | `PZO22001 Starfinder Player Core 442-464::/page/3/Text/44` | 0.501033 | **Defend** (exploration activity) Travel with your shield raised. 430 **degrees of success** The four possible outcomes of a check:  critical success, success, failure, and critical failure. 393 |
| 6 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/39` | 0.498155 | **Avert Gaze **[one-action] (specialty basic action) Avoid visual abilities. 411 **Avoid Notice** (exploration activity) Travel stealthily. 430 |
| 7 | `PZO22001 Starfinder Player Core 442-464::/page/5/Text/3` | 0.497598 | exploration activities 430–432 |
| 8 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/20` | 0.494737 | **activity** A category of action that typically takes more than  a single action. Activities on your turn take 2 actions ([two-actions])  or 3 actions ([three-actions]). Exploration and downtime acti |
| 9 | `PZO22001 Starfinder Player Core 442-464::/page/5/Text/34` | 0.486041 | **Follow the Expert** (exploration activity) Benefit from another's  skill proficiency. 431 |
| 10 | `PZO22001 Starfinder Player Core 442-464::/page/3/Text/48` | 0.474509 | **Demoralize **[one-action] (skill action) Frighten enemies. (Intimidation) 200 **Detect Magic** (exploration activity) Repeatedly *detect magic*.  430–431 |

### Query 35
- Text: What is the rule about **anathema** Actions contrary to your point of view and violations  of your personal code are called anathema. If you gain  anathema from a source of power such as a deity, violating  the anathema can cause you to lose related abilities. 24 deity anathema 35–39?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 442-464::/page/0/Text/37']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 442-464::/page/0/Text/37', 'PZO22001 Starfinder Player Core 442-464::/page/4/Text/38', 'PZO22001 Starfinder Player Core 442-464::/page/3/Text/45']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/37` | 1.004126 | **anathema** Actions contrary to your point of view and violations  of your personal code are called anathema. If you gain  anathema from a source of power such as a deity, violating  the anathema can |
| 2 | `PZO22001 Starfinder Player Core 442-464::/page/4/Text/38` | 0.641996 | **edict** Behaviors encouraged by your personal philosophy or  code are edicts. You might also gain edicts from a source of  power such as a deity. 24 deity edicts 35–39 |
| 3 | `PZO22001 Starfinder Player Core 442-464::/page/3/Text/45` | 0.572872 | **deity** Deities are powerful entities. 25, **35–39** |
| 4 | `PZO22001 Starfinder Player Core 442-464::/page/14/Text/13` | 0.513243 | **unfriendly** (condition) An unfriendly NPC doesn't like you. 441 **unholy** (trait) If a creature with weakness to unholy uses a  holy item or effect, it takes damage from its weakness. **39** |
| 5 | `PZO22001 Starfinder Player Core 442-464::/page/17/TableCell/238` | 0.508961 | Anathema |
| 6 | `PZO22001 Starfinder Player Core 442-464::/page/6/Text/3` | 0.504560 | **gods** *See also* deity. 25, **35–39** |
| 7 | `PZO22001 Starfinder Player Core 442-464::/page/7/Text/58` | 0.496901 | **magical** (trait) Something with the magical trait is imbued  with magical energies not tied to a specific tradition  of magic. Some items or effects are closely tied to a  particular tradition of m |
| 8 | `PZO22001 Starfinder Player Core 442-464::/page/11/Text/5` | 0.495696 | **sanctified** (trait) When you use an ability with the sanctified  trait, you can choose to give it the holy trait if you have it  or the unholy trait if you have that. 39 |
| 9 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/3` | 0.493498 | **Arcana** (skill) Know arcane magic and creature facts. (Int) 193 **arcane** (trait) This magic comes from the arcane tradition,  which is built on logic and rationality. Anything with this  trait is |
| 10 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/12` | 0.490150 | **Athletics** (skill) Perform deeds of physical prowess. (Str) 193–195 **attack** (trait) An ability with this trait involves an attack. For  each attack you make beyond the first on your turn, you  t |

### Query 36
- Text: What is the rule about **ancestry** A broad family of people that a creature belongs to.  Each player character chooses an ancestry as the first step of  character creation. 10, 19, 27, **41–91** mixed ancestry 83?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 442-464::/page/0/Text/38']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 442-464::/page/0/Text/38', 'PZO22001 Starfinder Player Core 442-464::/page/6/Text/37', 'PZO22001 Starfinder Player Core 442-464::/page/6/Text/20']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/38` | 0.981931 | **ancestry** A broad family of people that a creature belongs to.  Each player character chooses an ancestry as the first step of  character creation. 10, 19, 27, **41–91** mixed ancestry 83 |
| 2 | `PZO22001 Starfinder Player Core 442-464::/page/6/Text/37` | 0.666915 | **human** (trait) A creature with this trait is a member of the  human ancestry. An ability with this trait can be used or  selected only by humans. 50–53 |
| 3 | `PZO22001 Starfinder Player Core 442-464::/page/6/Text/20` | 0.647443 | **helpful** (condition) A helpful NPC is likely to assist you. 437 **heritage** A choice made to further define your ancestry. 41 |
| 4 | `PZO22001 Starfinder Player Core 442-464::/page/15/TableCell/32` | 0.590160 | Ancestry ——— |
| 5 | `PZO22001 Starfinder Player Core 442-464::/page/6/Text/21` | 0.578726 | A custom heritage for characters with two ancestral lines. 83 versatile heritages (can be chosen for a character of any  ancestry) 82–91 |
| 6 | `PZO22001 Starfinder Player Core 442-464::/page/7/Text/51` | 0.567582 | **lineage** (trait) A feat with this trait indicates a character's  descendance from a particular type of creature. You can  have only one lineage feat. You can select a lineage feat  only at 1st leve |
| 7 | `PZO22001 Starfinder Player Core 442-464::/page/2/Text/31` | 0.546078 | **class** The adventuring profession chosen by a character. Each  player character picks a class during character creation.  10, 20, 28, **99–173** |
| 8 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/40` | 0.543510 | **android** (trait) A creature with this trait is a member of the  android ancestry. Androids are synthetic constructed  beings. An ability with this trait can be used or selected  only by androids. 4 |
| 9 | `PZO22001 Starfinder Player Core 442-464::/page/3/Text/13` | 0.542851 | **creature** An active participant in the story and world, whether  monster, nonplayer character, or player character. monster identification 190–191 |
| 10 | `PZO22001 Starfinder Player Core 442-464::/page/7/Text/27` | 0.542685 | **kasatha** (trait) A creature with this trait is a member of the  kasatha ancestry. Kasatha are four-armed migrants from  a dying world who value cosmic balance and tradition.  An ability with this t |

### Query 37
- Text: What is the rule about **anchoring** (trait) 168?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 442-464::/page/0/Text/39']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 442-464::/page/0/Text/39', 'PZO22001 Starfinder Player Core 442-464::/page/14/Text/54', 'PZO22001 Starfinder Player Core 442-464::/page/5/Text/29']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/39` | 0.925858 | **anchoring** (trait) 168 |
| 2 | `PZO22001 Starfinder Player Core 442-464::/page/14/Text/54` | 0.583678 | **zone** (trait) 168 |
| 3 | `PZO22001 Starfinder Player Core 442-464::/page/5/Text/29` | 0.560120 | **flourish** (trait) You can only use one action with the flourish  trait per round. 144 |
| 4 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/30` | 0.485064 | **attuned** (trait) 144 |
| 5 | `PZO22001 Starfinder Player Core 442-464::/page/4/Text/51` | 0.483055 | **envoy** (trait) This indicates abilities from the envoy class. |
| 6 | `PZO22001 Starfinder Player Core 442-464::/page/7/Text/72` | 0.478375 | **manifestation** (trait) 144 |
| 7 | `PZO22001 Starfinder Player Core 442-464::/page/4/Text/15` | 0.462782 | **disharmony** (trait) 144 |
| 8 | `PZO22001 Starfinder Player Core 442-464::/page/4/Text/10` | 0.445635 | **directive** (trait) 108 |
| 9 | `PZO22001 Starfinder Player Core 442-464::/page/3/Text/43` | 0.444609 | **dedication** (trait) You must select a feat with this trait to  apply an archetype to your character. Once you take a  dedication feat, you can't select a different dedication feat  until you comple |
| 10 | `PZO22001 Starfinder Player Core 442-464::/page/3/Text/21` | 0.440197 | **cycle** (trait) 144 |

### Query 38
- Text: What is the rule about **android** (trait) A creature with this trait is a member of the  android ancestry. Androids are synthetic constructed  beings. An ability with this trait can be used or selected  only by androids. 42–45?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 442-464::/page/0/Text/40']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 442-464::/page/0/Text/40', 'PZO22001 Starfinder Player Core 442-464::/page/6/Text/37', 'PZO22001 Starfinder Player Core 442-464::/page/2/Text/2']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/40` | 0.988612 | **android** (trait) A creature with this trait is a member of the  android ancestry. Androids are synthetic constructed  beings. An ability with this trait can be used or selected  only by androids. 4 |
| 2 | `PZO22001 Starfinder Player Core 442-464::/page/6/Text/37` | 0.755406 | **human** (trait) A creature with this trait is a member of the  human ancestry. An ability with this trait can be used or  selected only by humans. 50–53 |
| 3 | `PZO22001 Starfinder Player Core 442-464::/page/2/Text/2` | 0.640154 | **Borai** (trait) A creature with this trait has the borai versatile  heritage. An ability with this trait can be used or selected  only by borai. 84–87 |
| 4 | `PZO22001 Starfinder Player Core 442-464::/page/9/Text/11` | 0.596707 | **pahtra** (trait) A creature with this trait is a member of the  pahtra ancestry. Pahtra are cat-like people who value  competition, music, and freedom. An ability with this trait  can be used or sel |
| 5 | `PZO22001 Starfinder Player Core 442-464::/page/7/Text/27` | 0.589723 | **kasatha** (trait) A creature with this trait is a member of the  kasatha ancestry. Kasatha are four-armed migrants from  a dying world who value cosmic balance and tradition.  An ability with this t |
| 6 | `PZO22001 Starfinder Player Core 442-464::/page/11/Text/25` | 0.579033 | **shirren** (trait) A creature with this trait is a member of the  shirren ancestry. Shirren are telepathic insect-like people  searching for meaning after freeing themselves from the  Swarm hive mind |
| 7 | `PZO22001 Starfinder Player Core 442-464::/page/10/Text/6` | 0.577616 | **Prismeni** (trait) A creature with this trait has the prismeni  versatile heritage. An ability with this trait can be used or  selected only by prismeni. 88–91 |
| 8 | `PZO22001 Starfinder Player Core 442-464::/page/9/Text/30` | 0.571449 | **plant** (trait) Vegetable creatures have the plant trait. They are  distinct from normal plants. Magical effects with this trait  manipulate or conjure plants or plant matter in some way.  Effects t |
| 9 | `PZO22001 Starfinder Player Core 442-464::/page/7/Text/51` | 0.569458 | **lineage** (trait) A feat with this trait indicates a character's  descendance from a particular type of creature. You can  have only one lineage feat. You can select a lineage feat  only at 1st leve |
| 10 | `PZO22001 Starfinder Player Core 442-464::/page/13/Text/24` | 0.561408 | **tech** (trait) Equipment with the tech trait rely on electricity  and may gain the glitching condition. Some creatures  and hazards also have the tech trait, such as artificial  intelligence, robots |

### Query 39
- Text: What is the rule about **angel** (trait) This family of celestials is native to the plane of  Nirvana.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 442-464::/page/0/Text/41']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 442-464::/page/0/Text/41', 'PZO22001 Starfinder Player Core 442-464::/page/2/Text/19', 'PZO22001 Starfinder Player Core 442-464::/page/4/Text/42']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/41` | 0.962446 | **angel** (trait) This family of celestials is native to the plane of  Nirvana. |
| 2 | `PZO22001 Starfinder Player Core 442-464::/page/2/Text/19` | 0.653618 | **celestial** (trait) Creatures with this trait hail from or have a  strong connection to the holy planes. |
| 3 | `PZO22001 Starfinder Player Core 442-464::/page/4/Text/42` | 0.610834 | **elemental** (trait) Elementals are creatures directly tied to an  element and native to the elemental planes. |
| 4 | `PZO22001 Starfinder Player Core 442-464::/page/4/Text/55` | 0.567389 | **ethereal** (trait) Creatures with this trait are native to the Ethereal  plane. |
| 5 | `PZO22001 Starfinder Player Core 442-464::/page/3/Text/51` | 0.557832 | **devil** (trait) A family of fiends from Hell. |
| 6 | `PZO22001 Starfinder Player Core 442-464::/page/5/Text/21` | 0.518999 | **fiend** (trait) Creatures that hail from or have a strong  connection to the unholy planes are called fiends. |
| 7 | `PZO22001 Starfinder Player Core 442-464::/page/3/Text/47` | 0.518997 | **demon** (trait) A family of fiends, demons hail from or trace  their origins to the Outer Rifts. |
| 8 | `PZO22001 Starfinder Player Core 442-464::/page/7/Text/27` | 0.507677 | **kasatha** (trait) A creature with this trait is a member of the  kasatha ancestry. Kasatha are four-armed migrants from  a dying world who value cosmic balance and tradition.  An ability with this t |
| 9 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/40` | 0.506734 | **android** (trait) A creature with this trait is a member of the  android ancestry. Androids are synthetic constructed  beings. An ability with this trait can be used or selected  only by androids. 4 |
| 10 | `PZO22001 Starfinder Player Core 442-464::/page/3/Text/23` | 0.502873 | **daemon** (trait) A family of fiends from Abaddon. |

### Query 40
- Text: What is the rule about **animal** (trait) An animal is a creature with a relatively low  intelligence. It typically doesn't have an Intelligence  attribute modifier over –4, can't speak languages, and can't  be trained in Intelligence-based skills.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 442-464::/page/0/Text/42']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 442-464::/page/0/Text/42', 'PZO22001 Starfinder Player Core 442-464::/page/1/Text/47', 'PZO22001 Starfinder Player Core 442-464::/page/6/Text/37']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/42` | 0.960941 | **animal** (trait) An animal is a creature with a relatively low  intelligence. It typically doesn't have an Intelligence  attribute modifier over –4, can't speak languages, and can't  be trained in I |
| 2 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/47` | 0.737387 | **beast** (trait) A creature similar to an animal but with an  Intelligence modifier of –3 or higher is usually a beast.  Unlike an animal, a beast might be able to speak and reason. |
| 3 | `PZO22001 Starfinder Player Core 442-464::/page/6/Text/37` | 0.693966 | **human** (trait) A creature with this trait is a member of the  human ancestry. An ability with this trait can be used or  selected only by humans. 50–53 |
| 4 | `PZO22001 Starfinder Player Core 442-464::/page/8/Text/10` | 0.648690 | **mindless** (trait) A mindless creature has either programmed  or rudimentary mental attributes. Most, if not all, of their  mental attribute modifiers are –5. They are immune to all  mental effects. |
| 5 | `PZO22001 Starfinder Player Core 442-464::/page/7/Text/52` | 0.601552 | **linguistic** (trait) An effect with this trait depends on language  comprehension. A linguistic effect that targets a creature  works only if the target understands the language you are  using. |
| 6 | `PZO22001 Starfinder Player Core 442-464::/page/4/Text/44` | 0.594624 | **emotion** (trait) This effect alters a creature's emotions.  Effects with this trait always have the mental trait as well.  Creatures with special training or that have mechanical or  artificial int |
| 7 | `PZO22001 Starfinder Player Core 442-464::/page/13/Text/38` | 0.574575 | **trait** A keyword that conveys information about a rules  element. Often a trait indicates how other rules interact with  an ability, creature, item, or other rules element with that  trait. Individ |
| 8 | `PZO22001 Starfinder Player Core 442-464::/page/8/Text/1` | 0.569261 | **manipulate** (trait) Actions with this trait require you to  physically manipulate an item or make gestures to use.  Creatures without a suitable appendage can't perform  actions with this trait. Ma |
| 9 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/40` | 0.567744 | **android** (trait) A creature with this trait is a member of the  android ancestry. Androids are synthetic constructed  beings. An ability with this trait can be used or selected  only by androids. 4 |
| 10 | `PZO22001 Starfinder Player Core 442-464::/page/9/Text/30` | 0.552942 | **plant** (trait) Vegetable creatures have the plant trait. They are  distinct from normal plants. Magical effects with this trait  manipulate or conjure plants or plant matter in some way.  Effects t |

### Query 41
- Text: What is the rule about **apex** (trait) 292?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 442-464::/page/0/Text/43']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 442-464::/page/0/Text/43', 'PZO22001 Starfinder Player Core 442-464::/page/1/Text/35', 'PZO22001 Starfinder Player Core 442-464::/page/13/Text/11']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/43` | 0.919673 | **apex** (trait) 292 |
| 2 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/35` | 0.554110 | apex augmentations 292–293  biotech augmentations 288–289  cybernetic augmentations 289–291 magitech augmentations 291–292 |
| 3 | `PZO22001 Starfinder Player Core 442-464::/page/13/Text/11` | 0.547111 | **summoned** (trait) 299 |
| 4 | `PZO22001 Starfinder Player Core 442-464::/page/8/Text/20` | 0.499413 | **morph** (trait) 299 |
| 5 | `PZO22001 Starfinder Player Core 442-464::/page/9/Text/36` | 0.470704 | **polymorph** (trait) 299 |
| 6 | `PZO22001 Starfinder Player Core 442-464::/page/14/Text/25` | 0.464040 | **virulent** (trait) 422 |
| 7 | `PZO22001 Starfinder Player Core 442-464::/page/13/Text/38` | 0.450210 | **trait** A keyword that conveys information about a rules  element. Often a trait indicates how other rules interact with  an ability, creature, item, or other rules element with that  trait. Individ |
| 8 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/7` | 0.433601 | **archetype** (trait) This feat belongs to an archetype. 174 **area** A specified shape and size of an effect. 298, 300, **420** **area (burst, cone, line)** (weapon trait) 255 |
| 9 | `PZO22001 Starfinder Player Core 442-464::/page/4/Text/10` | 0.431023 | **directive** (trait) 108 |
| 10 | `PZO22001 Starfinder Player Core 442-464::/page/8/Text/42` | 0.425090 | **nonlethal** (trait) 256, **399** |

### Query 42
- Text: Summarize **Apostae** A hollow planetoid containing mysterious gateways to  tunnel networks and ancient mechanical complexes. 34
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 442-464::/page/0/Text/44']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 442-464::/page/0/Text/44', 'PZO22001 Starfinder Player Core 442-464::/page/4/Text/1', 'PZO22001 Starfinder Player Core 442-464::/page/2/Text/5']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/44` | 1.036951 | **Apostae** A hollow planetoid containing mysterious gateways to  tunnel networks and ancient mechanical complexes. 34 |
| 2 | `PZO22001 Starfinder Player Core 442-464::/page/4/Text/1` | 0.543865 | **Diaspora** An asteroid belt formed when the twin planets  Damiar and Iovo were destroyed, home to smugglers,  pirates, and sarcesians. 32 |
| 3 | `PZO22001 Starfinder Player Core 442-464::/page/2/Text/5` | 0.522990 | **Bretheda** A massive gas giant orbited by highly populated  moons, home to floating arcologies known for their biotech  science and artists. 33 |
| 4 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/3` | 0.479956 | **Aballon** A rocky, sun-blasted planet of industry which is home to  intelligent machines created by the enigmatic First Ones. 31 |
| 5 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/6` | 0.464810 | **Absalom Station** A space station which serves as a major hub  of trade and culture in the Pact Worlds. 31 |
| 6 | `PZO22001 Starfinder Player Core 442-464::/page/2/Text/18` | 0.458444 | **Castrovel** A jungle planet teeming with psychic energy which  is home to elves, lashunta, and formians. 31 |
| 7 | `PZO22001 Starfinder Player Core 442-464::/page/10/Text/10` | 0.455904 | **Pulonis** A recently liberated, low-gravity jungle world in the  Veskarium which recently became a member of the Pact  Worlds. 34 |
| 8 | `PZO22001 Starfinder Player Core 442-464::/page/14/Text/22` | 0.443960 | **Verces** A tidally locked planet which is half frozen and half desert,  with a world-spanning Ring of Nations between the two. 32 |
| 9 | `PZO22001 Starfinder Player Core 442-464::/page/9/Text/10` | 0.436297 | **Pact Worlds** The governing body of planets that make up the  core of the primary Starfinder setting. 30–34 |
| 10 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/30` | 0.422881 | **Akiton** A red desert planet often defined by its economic  decline due to changes in starship technology. 32 |

### Query 43
- Text: What is the rule about **aquatic** (trait) Aquatic creatures are at home underwater.  Their bludgeoning and slashing unarmed Strikes don't  take the usual –2 penalty for being underwater. Aquatic  creatures can breathe water but not air.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 442-464::/page/0/Text/45']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 442-464::/page/0/Text/45', 'PZO22001 Starfinder Player Core 442-464::/page/0/Text/34', 'PZO22001 Starfinder Player Core 442-464::/page/14/Text/34']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/45` | 0.986373 | **aquatic** (trait) Aquatic creatures are at home underwater.  Their bludgeoning and slashing unarmed Strikes don't  take the usual –2 penalty for being underwater. Aquatic  creatures can breathe wate |
| 2 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/34` | 0.700112 | **ammunition** usually stored in magazine or battery, 254–255 **amphibious** (trait) An amphibious creature can breathe in water  and in air, even outside of its preferred environment, usually  indefi |
| 3 | `PZO22001 Starfinder Player Core 442-464::/page/14/Text/34` | 0.591193 | **water** (trait) Effects with the water trait either manipulate  or conjure water. Those that manipulate water have  no effect in an area without water. Creatures with this  trait consist primarily o |
| 4 | `PZO22001 Starfinder Player Core 442-464::/page/3/Text/4` | 0.529764 | **cosmic **(trait) Creatures with this trait can survive in the  harsh vacuum of space and the vast distances between  planets and stars. They don't breathe while in space  or in a vacuum. Creatures w |
| 5 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/1` | 0.502112 | **aquatic combat** 429 |
| 6 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/42` | 0.477889 | **animal** (trait) An animal is a creature with a relatively low  intelligence. It typically doesn't have an Intelligence  attribute modifier over –4, can't speak languages, and can't  be trained in I |
| 7 | `PZO22001 Starfinder Player Core 442-464::/page/13/Text/18` | 0.466715 | **Swim **[one-action] (skill action) Move through the water. (Athletics) 195 aquatic combat 429 swim Speed 412 |
| 8 | `PZO22001 Starfinder Player Core 442-464::/page/14/Text/26` | 0.461171 | **visual** (trait) A visual effect can affect only creatures that can  see it. This applies only to visible parts of the effect, as  determined by the GM. |
| 9 | `PZO22001 Starfinder Player Core 442-464::/page/12/Text/57` | 0.452449 | **structure** (trait) An item with the structure trait creates a  magical building or other structure when activated. The  item must be activated on a plot of land free of other  structures. The struc |
| 10 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/31` | 0.448298 | **Aid **[one-action[reaction][fre-actio (basic action) Improve an ally's skill check or attack. 408 **air** (trait) Effects with the air trait either manipulate or  conjure air. Those that manipulate |

### Query 44
- Text: Summarize **aquatic combat** 429
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 442-464::/page/1/Text/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 442-464::/page/1/Text/1', 'PZO22001 Starfinder Player Core 442-464::/page/14/Text/10', 'PZO22001 Starfinder Player Core 442-464::/page/0/Text/26']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/1` | 1.006417 | **aquatic combat** 429 |
| 2 | `PZO22001 Starfinder Player Core 442-464::/page/14/Text/10` | 0.856909 | **underwater combat** 429 |
| 3 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/26` | 0.713727 | **aerial combat** 429 |
| 4 | `PZO22001 Starfinder Player Core 442-464::/page/11/Text/48` | 0.668736 | **special battles** mounted, aerial, and aquatic combat 429 **specialty basic action** 410–411 |
| 5 | `PZO22001 Starfinder Player Core 442-464::/page/13/Text/18` | 0.618060 | **Swim **[one-action] (skill action) Move through the water. (Athletics) 195 aquatic combat 429 swim Speed 412 |
| 6 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/45` | 0.541668 | **aquatic** (trait) Aquatic creatures are at home underwater.  Their bludgeoning and slashing unarmed Strikes don't  take the usual –2 penalty for being underwater. Aquatic  creatures can breathe wate |
| 7 | `PZO22001 Starfinder Player Core 442-464::/page/4/Text/30` | 0.517085 | **drowning and suffocating** 429 |
| 8 | `PZO22001 Starfinder Player Core 442-464::/page/8/Text/22` | 0.499378 | **Mount **[one-action] (specialty basic action) Ride an allied creature. 411 **mounted combat** 429 |
| 9 | `PZO22001 Starfinder Player Core 442-464::/page/5/Text/30` | 0.490134 | **fly **[one-action] (specialty basic action) Move up to your fly Speed. 411 aerial combat 429 |
| 10 | `PZO22001 Starfinder Player Core 442-464::/page/3/Text/49` | 0.484457 | **detecting creatures** 425 |

### Query 45
- Text: What is the rule about **arc** (weapon trait) 255?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 442-464::/page/1/Text/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 442-464::/page/1/Text/2', 'PZO22001 Starfinder Player Core 442-464::/page/1/Text/37', 'PZO22001 Starfinder Player Core 442-464::/page/0/Text/29']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/2` | 0.942708 | **arc** (weapon trait) 255 |
| 2 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/37` | 0.757547 | **automatic** (weapon trait) 255 |
| 3 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/29` | 0.714554 | **agile** (weapon trait) 255 |
| 4 | `PZO22001 Starfinder Player Core 442-464::/page/2/Text/4` | 0.659758 | **breakdown** (weapon trait) 255 |
| 5 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/25` | 0.656453 | **aeon** (weapon trait) 255 |
| 6 | `PZO22001 Starfinder Player Core 442-464::/page/13/Text/31` | 0.653711 | **thought** (weapon trait) 258 |
| 7 | `PZO22001 Starfinder Player Core 442-464::/page/3/Text/16` | 0.653260 | **critical** (weapon trait) 256 |
| 8 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/42` | 0.652044 | **backswing** (weapon trait) 255 |
| 9 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/41` | 0.647667 | **backstabber** (weapon trait) 255 |
| 10 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/5` | 0.647654 | **archaic** (item trait) 245, 250, 255 |

### Query 46
- Text: What is the rule about **Arcana** (skill) Know arcane magic and creature facts. (Int) 193 **arcane** (trait) This magic comes from the arcane tradition,  which is built on logic and rationality. Anything with this  trait is magical.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 442-464::/page/1/Text/3']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 442-464::/page/1/Text/3', 'PZO22001 Starfinder Player Core 442-464::/page/7/Text/58', 'PZO22001 Starfinder Player Core 442-464::/page/13/Text/36']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/3` | 0.964691 | **Arcana** (skill) Know arcane magic and creature facts. (Int) 193 **arcane** (trait) This magic comes from the arcane tradition,  which is built on logic and rationality. Anything with this  trait is |
| 2 | `PZO22001 Starfinder Player Core 442-464::/page/7/Text/58` | 0.726420 | **magical** (trait) Something with the magical trait is imbued  with magical energies not tied to a specific tradition  of magic. Some items or effects are closely tied to a  particular tradition of m |
| 3 | `PZO22001 Starfinder Player Core 442-464::/page/13/Text/36` | 0.680209 | **tradition** A fundamental category of magic (arcane, divine,  occult, or primal). 297 |
| 4 | `PZO22001 Starfinder Player Core 442-464::/page/7/Text/59` | 0.645726 | **magical tradition** Arcane, divine, occult, and primal are the  traditions of magic. 297 |
| 5 | `PZO22001 Starfinder Player Core 442-464::/page/2/Text/3` | 0.611299 | **Borrow an Arcane Spell** (skill action) Temporarily gain access  to an arcane spell. (Arcana, trained) 193 |
| 6 | `PZO22001 Starfinder Player Core 442-464::/page/11/Text/35` | 0.602628 | **skill** (trait) A general feat with the skill trait improves your  skills and their actions or gives you new actions for a skill.  A feat with this trait can be selected when a class grants  a skill |
| 7 | `PZO22001 Starfinder Player Core 442-464::/page/6/Text/41` | 0.598971 | **Identify Magic** (skill action) Determine specifics of magic.  (Arcana, Nature, Occultism, Religion; trained) 188–189 |
| 8 | `PZO22001 Starfinder Player Core 442-464::/page/9/Text/1` | 0.598387 | **occult** (trait) This magic comes from the occult tradition,  calling upon bizarre and ephemeral mysteries. Anything  with this trait is magical. 297 occult spell list 307–310 |
| 9 | `PZO22001 Starfinder Player Core 442-464::/page/7/Text/37` | 0.596814 | **Learn a Spell** (skill action) Learn a new spell. (Arcana, Nature,  Occultism, Religion; trained) 189–190 |
| 10 | `PZO22001 Starfinder Player Core 442-464::/page/9/Text/2` | 0.578522 | **Occultism** (skill) Know about philosophies, mysticism, and  occult magic. (Int) 203 |

### Query 47
- Text: What is the rule about arcane spell list 302–305?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 442-464::/page/1/Text/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 442-464::/page/1/Text/4', 'PZO22001 Starfinder Player Core 442-464::/page/14/Text/45', 'PZO22001 Starfinder Player Core 442-464::/page/12/Text/22']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/4` | 0.926454 | arcane spell list 302–305 |
| 2 | `PZO22001 Starfinder Player Core 442-464::/page/14/Text/45` | 0.797256 | spell lists 302–305,307–310 |
| 3 | `PZO22001 Starfinder Player Core 442-464::/page/12/Text/22` | 0.736889 | spell lists 302–312 |
| 4 | `PZO22001 Starfinder Player Core 442-464::/page/8/Text/37` | 0.693825 | spell lists 305–312 |
| 5 | `PZO22001 Starfinder Player Core 442-464::/page/13/Text/23` | 0.587189 | spell targets 298, 300 |
| 6 | `PZO22001 Starfinder Player Core 442-464::/page/12/Text/6` | 0.569190 | casting spells 298 |
| 7 | `PZO22001 Starfinder Player Core 442-464::/page/12/Text/28` | 0.567774 | traditions (arcane, divine, occult, and primal) 297 |
| 8 | `PZO22001 Starfinder Player Core 442-464::/page/7/Text/43` | 0.565861 | spell rank (spells have a rank instead of a level, ranging  from 1–10) 295–296 |
| 9 | `PZO22001 Starfinder Player Core 442-464::/page/12/Text/10` | 0.557870 | focus spells (epiphany and warp spells) 296–297, 375– 380 |
| 10 | `PZO22001 Starfinder Player Core 442-464::/page/12/Text/4` | 0.550693 | attacking with a spell 300, **394–395** |

### Query 48
- Text: What is the rule about **archaic** (item trait) 245, 250, 255?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 442-464::/page/1/Text/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 442-464::/page/1/Text/5', 'PZO22001 Starfinder Player Core 442-464::/page/0/Text/35', 'PZO22001 Starfinder Player Core 442-464::/page/1/Text/2']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/5` | 0.955562 | **archaic** (item trait) 245, 250, 255 |
| 2 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/35` | 0.686067 | **analog** (trait) 245, 250, 255 |
| 3 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/2` | 0.669408 | **arc** (weapon trait) 255 |
| 4 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/37` | 0.617463 | **automatic** (weapon trait) 255 |
| 5 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/29` | 0.590995 | **agile** (weapon trait) 255 |
| 6 | `PZO22001 Starfinder Player Core 442-464::/page/5/Text/28` | 0.574622 | **flexible** (armor trait) 245 |
| 7 | `PZO22001 Starfinder Player Core 442-464::/page/13/Text/39` | 0.561586 | weapon traits 255–258 |
| 8 | `PZO22001 Starfinder Player Core 442-464::/page/14/Text/38` | 0.561586 | weapon traits 255–258 |
| 9 | `PZO22001 Starfinder Player Core 442-464::/page/3/Text/16` | 0.555000 | **critical** (weapon trait) 256 |
| 10 | `PZO22001 Starfinder Player Core 442-464::/page/9/Text/37` | 0.551251 | **ponderous** (armor trait) 245 |

### Query 49
- Text: What is the rule about **archetype** A special additional theme for your character that  you can choose using your class feats. 174–181?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 442-464::/page/1/Text/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 442-464::/page/1/Text/6', 'PZO22001 Starfinder Player Core 442-464::/page/3/Text/43', 'PZO22001 Starfinder Player Core 442-464::/page/1/Text/7']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/6` | 0.952570 | **archetype** A special additional theme for your character that  you can choose using your class feats. 174–181 |
| 2 | `PZO22001 Starfinder Player Core 442-464::/page/3/Text/43` | 0.703881 | **dedication** (trait) You must select a feat with this trait to  apply an archetype to your character. Once you take a  dedication feat, you can't select a different dedication feat  until you comple |
| 3 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/7` | 0.699305 | **archetype** (trait) This feat belongs to an archetype. 174 **area** A specified shape and size of an effect. 298, 300, **420** **area (burst, cone, line)** (weapon trait) 255 |
| 4 | `PZO22001 Starfinder Player Core 442-464::/page/8/Text/31` | 0.644745 | **multiclass** (trait) Archetypes with the multiclass trait  represent diversifying your training into another class's  specialties. You can't select a multiclass archetype's  dedication feat if you a |
| 5 | `PZO22001 Starfinder Player Core 442-464::/page/11/Text/35` | 0.598104 | **skill** (trait) A general feat with the skill trait improves your  skills and their actions or gives you new actions for a skill.  A feat with this trait can be selected when a class grants  a skill |
| 6 | `PZO22001 Starfinder Player Core 442-464::/page/5/Text/15` | 0.581388 | archetype feat 174 |
| 7 | `PZO22001 Starfinder Player Core 442-464::/page/2/Text/33` | 0.554937 | **class feature** Any ability granted by a class is a class feature.  These mainly consist of class feats and other abilities  specific to the class. 100 |
| 8 | `PZO22001 Starfinder Player Core 442-464::/page/2/Text/31` | 0.542388 | **class** The adventuring profession chosen by a character. Each  player character picks a class during character creation.  10, 20, 28, **99–173** |
| 9 | `PZO22001 Starfinder Player Core 442-464::/page/5/Text/57` | 0.537305 | **general** (trait) A type of feat that any character can select,  regardless of ancestry and class, as long as they meet the  prerequisites. You can select a feat with this trait when  your class gra |
| 10 | `PZO22001 Starfinder Player Core 442-464::/page/5/Text/13` | 0.532732 | **feat** An ability you gain or select for your character due to  their ancestry, background, class, general training, or skill  training. Some feats grant special actions. 10, 16 |

### Query 50
- Text: What is the rule about **archetype** (trait) This feat belongs to an archetype. 174 **area** A specified shape and size of an effect. 298, 300, **420** **area (burst, cone, line)** (weapon trait) 255?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 442-464::/page/1/Text/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 442-464::/page/1/Text/7', 'PZO22001 Starfinder Player Core 442-464::/page/11/Text/35', 'PZO22001 Starfinder Player Core 442-464::/page/1/Text/2']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/7` | 0.992215 | **archetype** (trait) This feat belongs to an archetype. 174 **area** A specified shape and size of an effect. 298, 300, **420** **area (burst, cone, line)** (weapon trait) 255 |
| 2 | `PZO22001 Starfinder Player Core 442-464::/page/11/Text/35` | 0.720460 | **skill** (trait) A general feat with the skill trait improves your  skills and their actions or gives you new actions for a skill.  A feat with this trait can be selected when a class grants  a skill |
| 3 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/2` | 0.708995 | **arc** (weapon trait) 255 |
| 4 | `PZO22001 Starfinder Player Core 442-464::/page/3/Text/43` | 0.656438 | **dedication** (trait) You must select a feat with this trait to  apply an archetype to your character. Once you take a  dedication feat, you can't select a different dedication feat  until you comple |
| 5 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/6` | 0.653870 | **archetype** A special additional theme for your character that  you can choose using your class feats. 174–181 |
| 6 | `PZO22001 Starfinder Player Core 442-464::/page/8/Text/31` | 0.652261 | **multiclass** (trait) Archetypes with the multiclass trait  represent diversifying your training into another class's  specialties. You can't select a multiclass archetype's  dedication feat if you a |
| 7 | `PZO22001 Starfinder Player Core 442-464::/page/13/Text/38` | 0.631701 | **trait** A keyword that conveys information about a rules  element. Often a trait indicates how other rules interact with  an ability, creature, item, or other rules element with that  trait. Individ |
| 8 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/29` | 0.615015 | **agile** (weapon trait) 255 |
| 9 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/37` | 0.608678 | **automatic** (weapon trait) 255 |
| 10 | `PZO22001 Starfinder Player Core 442-464::/page/5/Text/57` | 0.603107 | **general** (trait) A type of feat that any character can select,  regardless of ancestry and class, as long as they meet the  prerequisites. You can select a feat with this trait when  your class gra |

### Query 51
- Text: What is the rule about **Area Fire **[two-actions] (specialty basic action) Hit each creature in a  designated area. 156, 255, **410**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 442-464::/page/1/Text/8']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 442-464::/page/1/Text/8', 'PZO22001 Starfinder Player Core 442-464::/page/1/Text/38', 'PZO22001 Starfinder Player Core 442-464::/page/1/Text/46']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/8` | 0.968356 | **Area Fire **[two-actions] (specialty basic action) Hit each creature in a  designated area. 156, 255, **410** |
| 2 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/38` | 0.798304 | **Auto-Fire**[two-actions] (specialty basic action) You hit each creature in  a cone. 156, 255, **410** |
| 3 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/46` | 0.659190 | **basic action** An action all creatures can use. 408–410 |
| 4 | `PZO22001 Starfinder Player Core 442-464::/page/9/Text/34` | 0.581752 | **Point Out **[one-action] (specialty basic action) Indicate an undetected  creature's location. 411 |
| 5 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/31` | 0.579638 | **Aid **[one-action[reaction][fre-actio (basic action) Improve an ally's skill check or attack. 408 **air** (trait) Effects with the air trait either manipulate or  conjure air. Those that manipulate |
| 6 | `PZO22001 Starfinder Player Core 442-464::/page/5/Text/30` | 0.579015 | **fly **[one-action] (specialty basic action) Move up to your fly Speed. 411 aerial combat 429 |
| 7 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/7` | 0.566942 | **archetype** (trait) This feat belongs to an archetype. 174 **area** A specified shape and size of an effect. 298, 300, **420** **area (burst, cone, line)** (weapon trait) 255 |
| 8 | `PZO22001 Starfinder Player Core 442-464::/page/10/Text/41` | 0.566672 | **Reposition **[one-action] (skill action) Move a creature within your reach 194 **Request **[one-action] (skill action) Get someone to help you. (Diplomacy)  199–200 |
| 9 | `PZO22001 Starfinder Player Core 442-464::/page/2/Text/39` | 0.549844 | **Command an Animal **[one-action] (skill action) Get an animal to obey  you. (Nature) 202 |
| 10 | `PZO22001 Starfinder Player Core 442-464::/page/14/Text/2` | 0.546974 | **turn** During a round in an encounter, each creature takes a  single turn. A creature typically uses up to 3 actions during  its turn. 11, **427–428** |

### Query 52
- Text: Summarize **armor** 244–249
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 442-464::/page/1/Text/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 442-464::/page/1/Text/9', 'PZO22001 Starfinder Player Core 442-464::/page/7/Text/8', 'PZO22001 Starfinder Player Core 442-464::/page/8/Text/4']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/9` | 1.012705 | **armor** 244–249 |
| 2 | `PZO22001 Starfinder Player Core 442-464::/page/7/Text/8` | 0.968049 | armor 244–249 |
| 3 | `PZO22001 Starfinder Player Core 442-464::/page/8/Text/4` | 0.697299 | **medical items** 241–243 |
| 4 | `PZO22001 Starfinder Player Core 442-464::/page/5/Text/28` | 0.630456 | **flexible** (armor trait) 245 |
| 5 | `PZO22001 Starfinder Player Core 442-464::/page/2/Text/10` | 0.626846 | creature Bulk 234–235 **bulwark** (armor trait) 245 |
| 6 | `PZO22001 Starfinder Player Core 442-464::/page/13/Text/25` | 0.623036 | **tech gear** 238–243 |
| 7 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/24` | 0.621521 | **adventuring gear** 238–243 |
| 8 | `PZO22001 Starfinder Player Core 442-464::/page/5/Text/4` | 0.611392 | **exposed** (armor trait) 245 |
| 9 | `PZO22001 Starfinder Player Core 442-464::/page/11/Text/18` | 0.596695 | **serum** (trait) 242–243 |
| 10 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/8` | 0.590351 | **AC (Armor Class)** *See also* Armor Class. 10, 268, 395–396 |

### Query 53
- Text: What is the rule about **Armor Class (AC)** This score represents how hard it is to hit  and damage a creature. It typically serves as the DC to hit a  creature with an attack. AC = 10 + Dex modifier (up to your  armor's Dex Cap) + proficiency bonus + armor's item bonus  to AC + other bonuses + penalties. 10, 25, 244, **395–396** armor (equipment) 244–249 shields (equipment) 250–252?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 442-464::/page/1/Text/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 442-464::/page/1/Text/10', 'PZO22001 Starfinder Player Core 442-464::/page/0/Text/8', 'PZO22001 Starfinder Player Core 442-464::/page/1/Text/13']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/10` | 1.003580 | **Armor Class (AC)** This score represents how hard it is to hit  and damage a creature. It typically serves as the DC to hit a  creature with an attack. AC = 10 + Dex modifier (up to your  armor's De |
| 2 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/8` | 0.778429 | **AC (Armor Class)** *See also* Armor Class. 10, 268, 395–396 |
| 3 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/13` | 0.663485 | **attack** When a creature tries to harm another creature, it  makes a Strike or uses another attack action. Most attacks  require an attack roll and target Armor Class. Melee attack  roll modifier = |
| 4 | `PZO22001 Starfinder Player Core 442-464::/page/2/Text/32` | 0.610014 | **class DC** A class DC sets the difficulty for some abilities  granted by your character's class. Class DC = 10 +  proficiency bonus + key attribute modifier. 25, 99 |
| 5 | `PZO22001 Starfinder Player Core 442-464::/page/12/Text/31` | 0.570457 | **spell DC** Your spell DC measures how hard it is to resist your  spells with saving throws or to counteract them. Spell DC  = 10 + spellcasting attribute modifier + proficiency bonus +  other bonuse |
| 6 | `PZO22001 Starfinder Player Core 442-464::/page/4/Text/5` | 0.563395 | **Difficulty Class (DC)** The number you need to succeed at a  check. To generate a DC from a modifier (like Perception  DC), add 10 to the modifier. 8, **393** |
| 7 | `PZO22001 Starfinder Player Core 442-464::/page/15/Form/0` | 0.556123 | Character Name -Level ———Hero Points —ANDERChorocier Nome∧ XP\bigcirc\bigcirc\bigcirc\bigcirc< >Gain 1 at the start of each sessionCharacter SheetPlayer Nameand when granted by the GM.  Spend 1 to rer |
| 8 | `PZO22001 Starfinder Player Core 442-464::/page/15/TableCell/86` | 0.546414 | Base Dex* Prof Item * Use armor's Dex cap if lower |
| 9 | `PZO22001 Starfinder Player Core 442-464::/page/2/Text/24` | 0.537865 | **check** When you roll a d20 and add modifiers, bonuses, and  penalties, then compare your result to a Difficulty Class,  you're attempting a check. 10, **392–394** |
| 10 | `PZO22001 Starfinder Player Core 442-464::/page/11/Text/32` | 0.532276 | **skill** A statistic representing the ability to perform certain  tasks that require instruction or practice. Skill modifier  = modifier of the skill's key attribute score + proficiency  bonus + othe |

### Query 54
- Text: What is the rule about **Arrest a Fall **[reaction] (specialty basic action) Slow your fall while  flying. 410?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 442-464::/page/1/Text/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 442-464::/page/1/Text/11', 'PZO22001 Starfinder Player Core 442-464::/page/6/Text/4', 'PZO22001 Starfinder Player Core 442-464::/page/5/Text/30']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/11` | 0.951150 | **Arrest a Fall **[reaction] (specialty basic action) Slow your fall while  flying. 410 |
| 2 | `PZO22001 Starfinder Player Core 442-464::/page/6/Text/4` | 0.680673 | **Grab an Edge **[reaction] (specialty basic action) Try to catch yourself  while falling. 411 |
| 3 | `PZO22001 Starfinder Player Core 442-464::/page/5/Text/30` | 0.660746 | **fly **[one-action] (specialty basic action) Move up to your fly Speed. 411 aerial combat 429 |
| 4 | `PZO22001 Starfinder Player Core 442-464::/page/5/Text/27` | 0.550191 | **fleeing** (condition) You must run away. 437 |
| 5 | `PZO22001 Starfinder Player Core 442-464::/page/5/Text/7` | 0.540087 | **falling** When you fall more than 5 feet, you take bludgeoning  damage equal to half the distance you fell and land prone. 413 |
| 6 | `PZO22001 Starfinder Player Core 442-464::/page/7/Text/61` | 0.533513 | **Maneuver in Flight **[one-action] (skill action) Execute a difficult  movement while flying. (Acrobatics, trained) 192 |
| 7 | `PZO22001 Starfinder Player Core 442-464::/page/4/Text/29` | 0.522727 | **Drop Prone **[one-action] (basic action) Fall flat. **408**, 439 |
| 8 | `PZO22001 Starfinder Player Core 442-464::/page/10/Text/27` | 0.515731 | **Ready **[two-actions] (basic action) Prepare an action to use when it's  not your turn. 409 |
| 9 | `PZO22001 Starfinder Player Core 442-464::/page/14/Text/12` | 0.510071 | **uneven ground** You must Balance or fall when crossing  uneven ground. 415 |
| 10 | `PZO22001 Starfinder Player Core 442-464::/page/7/Text/35` | 0.508539 | **Leap **[one-action] (basic action) Jump horizontally 10 feet (15 feet if  your Speed is 30 feet or more), or vertically 3 feet and  horizontally 5 feet. 409 |

### Query 55
- Text: What is the rule about **Athletics** (skill) Perform deeds of physical prowess. (Str) 193–195 **attack** (trait) An ability with this trait involves an attack. For  each attack you make beyond the first on your turn, you  take a multiple attack penalty. 10, **394–395**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 442-464::/page/1/Text/12']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 442-464::/page/1/Text/12', 'PZO22001 Starfinder Player Core 442-464::/page/8/Text/32', 'PZO22001 Starfinder Player Core 442-464::/page/0/Text/13']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/12` | 0.991956 | **Athletics** (skill) Perform deeds of physical prowess. (Str) 193–195 **attack** (trait) An ability with this trait involves an attack. For  each attack you make beyond the first on your turn, you  t |
| 2 | `PZO22001 Starfinder Player Core 442-464::/page/8/Text/32` | 0.651820 | **multiple attack penalty** You take this penalty on all attacks  after the first on your turn. This is a –5 penalty on your  second attack and –10 on all subsequent attacks (or –4 and  –8 if your wea |
| 3 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/13` | 0.638815 | **Acrobatics** (skill) Perform tasks requiring coordination and  grace. (Dex) 192–193 |
| 4 | `PZO22001 Starfinder Player Core 442-464::/page/11/Text/35` | 0.593652 | **skill** (trait) A general feat with the skill trait improves your  skills and their actions or gives you new actions for a skill.  A feat with this trait can be selected when a class grants  a skill |
| 5 | `PZO22001 Starfinder Player Core 442-464::/page/13/Text/51` | 0.592276 | **Trip **[one-action] (skill action) Knock a creature down. (Athletics) 195 |
| 6 | `PZO22001 Starfinder Player Core 442-464::/page/3/Text/10` | 0.583833 | **Craft** (skill action) Make an item. (Crafting, trained) **197–198**, 434 **Crafting** (skill) Create, understand, and repair items. (Int) 196–198 **Crawl **[one-action] (basic action) Move 5 feet w |
| 7 | `PZO22001 Starfinder Player Core 442-464::/page/11/Text/32` | 0.569930 | **skill** A statistic representing the ability to perform certain  tasks that require instruction or practice. Skill modifier  = modifier of the skill's key attribute score + proficiency  bonus + othe |
| 8 | `PZO22001 Starfinder Player Core 442-464::/page/6/Text/6` | 0.560347 | **Grapple **[one-action] (skill action) Grab or restrain a target. (Athletics) 194 **grenade** (weapon trait) 256 |
| 9 | `PZO22001 Starfinder Player Core 442-464::/page/6/Text/25` | 0.556959 | **Hide **[one-action] (skill action) Make yourself hidden. (Stealth) 207 **High Jump **[two-actions] (skill action) Jump vertically. (Athletics) 194 |
| 10 | `PZO22001 Starfinder Player Core 442-464::/page/10/Text/4` | 0.556451 | **prerequisites** Many feats and other abilities can be taken  only if you meet their prerequisites. Prerequisites are often  feats or proficiency ranks. 16 |

### Query 56
- Text: What is the rule about **attack** When a creature tries to harm another creature, it  makes a Strike or uses another attack action. Most attacks  require an attack roll and target Armor Class. Melee attack  roll modifier = Str modifier (or optionally Dex modifier for  a finesse weapon) + proficiency bonus + other bonuses  + penalties; Ranged attack roll modifier = Dex modifier +  proficiency bonus + other bonuses + penalties. 10, 24, 253,  **394–395**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 442-464::/page/1/Text/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 442-464::/page/1/Text/13', 'PZO22001 Starfinder Player Core 442-464::/page/12/Text/30', 'PZO22001 Starfinder Player Core 442-464::/page/3/Text/26']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/13` | 1.004245 | **attack** When a creature tries to harm another creature, it  makes a Strike or uses another attack action. Most attacks  require an attack roll and target Armor Class. Melee attack  roll modifier = |
| 2 | `PZO22001 Starfinder Player Core 442-464::/page/12/Text/30` | 0.789949 | **spell attack modifier** You attempt a spell attack roll when  targeting a creature with aimed magic. Your multiple  attack penalty applies. Spell attack modifier = spellcasting  attribute modifier + |
| 3 | `PZO22001 Starfinder Player Core 442-464::/page/3/Text/26` | 0.727485 | **damage** Damage dealt that reduces a creature's Hit Points on a  1-to-1 basis. Melee damage roll = damage die of the weapon  or unarmed attack + Str mod + bonuses + penalties; Ranged  damage roll = |
| 4 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/10` | 0.585934 | **Armor Class (AC)** This score represents how hard it is to hit  and damage a creature. It typically serves as the DC to hit a  creature with an attack. AC = 10 + Dex modifier (up to your  armor's De |
| 5 | `PZO22001 Starfinder Player Core 442-464::/page/12/Text/18` | 0.581789 | spell attack modifier (spellcasting attribute modifier +  proficiency bonus + other bonuses + penalties) 394–395 |
| 6 | `PZO22001 Starfinder Player Core 442-464::/page/13/Text/35` | 0.578391 | **touch** A spell range requiring you to touch the target. 298 **Track** (skill action) Follow a creature's tracks. (Survival) 208–209 **tracking** (weapon trait) 258 |
| 7 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/12` | 0.566000 | **Athletics** (skill) Perform deeds of physical prowess. (Str) 193–195 **attack** (trait) An ability with this trait involves an attack. For  each attack you make beyond the first on your turn, you  t |
| 8 | `PZO22001 Starfinder Player Core 442-464::/page/12/Text/36` | 0.562173 | **splash** (trait) Some weapons and effects have the splash trait.  When you use a weapon or effect with the splash trait,  you don't add your Strength modifier to the damage roll. A  splash weapon or |
| 9 | `PZO22001 Starfinder Player Core 442-464::/page/11/Text/32` | 0.555707 | **skill** A statistic representing the ability to perform certain  tasks that require instruction or practice. Skill modifier  = modifier of the skill's key attribute score + proficiency  bonus + othe |
| 10 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/26` | 0.537654 | **attribute modifier** Each creature has six attribute modifiers:  Strength, Dexterity, Constitution, Intelligence, Wisdom,  and Charisma. These numbers represent a creature's raw  potential and basic |

### Query 57
- Text: What is the rule about Aid (reaction used to grant a bonus to an ally's attack roll) 408 critical hits **393**, 399, 410?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 442-464::/page/1/Text/14']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 442-464::/page/1/Text/14', 'PZO22001 Starfinder Player Core 442-464::/page/0/Text/31', 'PZO22001 Starfinder Player Core 442-464::/page/12/Text/56']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/14` | 0.959479 | Aid (reaction used to grant a bonus to an ally's attack roll) 408 critical hits **393**, 399, 410 |
| 2 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/31` | 0.577654 | **Aid **[one-action[reaction][fre-actio (basic action) Improve an ally's skill check or attack. 408 **air** (trait) Effects with the air trait either manipulate or  conjure air. Those that manipulate |
| 3 | `PZO22001 Starfinder Player Core 442-464::/page/12/Text/56` | 0.574686 | attack rolls 394–395 |
| 4 | `PZO22001 Starfinder Player Core 442-464::/page/10/Text/25` | 0.527810 | **reaction** ([reaction]) An action you can use even if it's not your turn.  You can use 1 reaction per round. 15, **406** reactions in encounters 428–429 |
| 5 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/15` | 0.525468 | multiple attack penalty (–5 on your second attack, –10 on  further attacks) 394 |
| 6 | `PZO22001 Starfinder Player Core 442-464::/page/8/Text/32` | 0.520106 | **multiple attack penalty** You take this penalty on all attacks  after the first on your turn. This is a –5 penalty on your  second attack and –10 on all subsequent attacks (or –4 and  –8 if your wea |
| 7 | `PZO22001 Starfinder Player Core 442-464::/page/11/Text/32` | 0.519341 | **skill** A statistic representing the ability to perform certain  tasks that require instruction or practice. Skill modifier  = modifier of the skill's key attribute score + proficiency  bonus + othe |
| 8 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/13` | 0.501192 | **attack** When a creature tries to harm another creature, it  makes a Strike or uses another attack action. Most attacks  require an attack roll and target Armor Class. Melee attack  roll modifier = |
| 9 | `PZO22001 Starfinder Player Core 442-464::/page/12/Text/30` | 0.499747 | **spell attack modifier** You attempt a spell attack roll when  targeting a creature with aimed magic. Your multiple  attack penalty applies. Spell attack modifier = spellcasting  attribute modifier + |
| 10 | `PZO22001 Starfinder Player Core 442-464::/page/3/Text/18` | 0.499382 | critical hit (Strike) 410 |

### Query 58
- Text: What is the rule about multiple attack penalty (–5 on your second attack, –10 on  further attacks) 394?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 442-464::/page/1/Text/15']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 442-464::/page/1/Text/15', 'PZO22001 Starfinder Player Core 442-464::/page/9/Text/18', 'PZO22001 Starfinder Player Core 442-464::/page/8/Text/32']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/15` | 0.941258 | multiple attack penalty (–5 on your second attack, –10 on  further attacks) 394 |
| 2 | `PZO22001 Starfinder Player Core 442-464::/page/9/Text/18` | 0.868736 | multiple attack penalty (–5 on your second attack, –10 on  further attacks) 253, **394** |
| 3 | `PZO22001 Starfinder Player Core 442-464::/page/8/Text/32` | 0.810087 | **multiple attack penalty** You take this penalty on all attacks  after the first on your turn. This is a –5 penalty on your  second attack and –10 on all subsequent attacks (or –4 and  –8 if your wea |
| 4 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/18` | 0.595316 | spell attack 394–395 |
| 5 | `PZO22001 Starfinder Player Core 442-464::/page/12/Text/56` | 0.589050 | attack rolls 394–395 |
| 6 | `PZO22001 Starfinder Player Core 442-464::/page/10/Text/15` | 0.581039 | range increment 254, **394** range penalty 394 |
| 7 | `PZO22001 Starfinder Player Core 442-464::/page/12/Text/18` | 0.574942 | spell attack modifier (spellcasting attribute modifier +  proficiency bonus + other bonuses + penalties) 394–395 |
| 8 | `PZO22001 Starfinder Player Core 442-464::/page/7/Text/15` | 0.562642 | item bonus or penalty 392 |
| 9 | `PZO22001 Starfinder Player Core 442-464::/page/12/Text/20` | 0.555823 | bonus + other bonuses + penalties) 395 |
| 10 | `PZO22001 Starfinder Player Core 442-464::/page/9/Text/19` | 0.553639 | range penalty 254, **394** |

### Query 59
- Text: What is the rule about nonlethal attack 399?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 442-464::/page/1/Text/17']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 442-464::/page/1/Text/17', 'PZO22001 Starfinder Player Core 442-464::/page/3/Text/32', 'PZO22001 Starfinder Player Core 442-464::/page/8/Text/42']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/17` | 0.874331 | nonlethal attack 399 |
| 2 | `PZO22001 Starfinder Player Core 442-464::/page/3/Text/32` | 0.874331 | nonlethal attack 399 |
| 3 | `PZO22001 Starfinder Player Core 442-464::/page/8/Text/42` | 0.582443 | **nonlethal** (trait) 256, **399** |
| 4 | `PZO22001 Starfinder Player Core 442-464::/page/12/Text/4` | 0.489434 | attacking with a spell 300, **394–395** |
| 5 | `PZO22001 Starfinder Player Core 442-464::/page/3/Text/30` | 0.474645 | doubling and halving 399 |
| 6 | `PZO22001 Starfinder Player Core 442-464::/page/8/Text/43` | 0.459405 | immunity to nonlethal 400 |
| 7 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/18` | 0.443298 | spell attack 394–395 |
| 8 | `PZO22001 Starfinder Player Core 442-464::/page/12/Text/56` | 0.443263 | attack rolls 394–395 |
| 9 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/20` | 0.409795 | unarmed attack 253 |
| 10 | `PZO22001 Starfinder Player Core 442-464::/page/13/Text/23` | 0.406490 | spell targets 298, 300 |

### Query 60
- Text: What is the rule about spell attack 394–395?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 442-464::/page/1/Text/18']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 442-464::/page/1/Text/18', 'PZO22001 Starfinder Player Core 442-464::/page/12/Text/56', 'PZO22001 Starfinder Player Core 442-464::/page/12/Text/4']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/18` | 0.939102 | spell attack 394–395 |
| 2 | `PZO22001 Starfinder Player Core 442-464::/page/12/Text/56` | 0.816111 | attack rolls 394–395 |
| 3 | `PZO22001 Starfinder Player Core 442-464::/page/12/Text/4` | 0.807796 | attacking with a spell 300, **394–395** |
| 4 | `PZO22001 Starfinder Player Core 442-464::/page/12/Text/18` | 0.708130 | spell attack modifier (spellcasting attribute modifier +  proficiency bonus + other bonuses + penalties) 394–395 |
| 5 | `PZO22001 Starfinder Player Core 442-464::/page/12/Text/30` | 0.619283 | **spell attack modifier** You attempt a spell attack roll when  targeting a creature with aimed magic. Your multiple  attack penalty applies. Spell attack modifier = spellcasting  attribute modifier + |
| 6 | `PZO22001 Starfinder Player Core 442-464::/page/11/Text/3` | 0.561282 | **rules overview** 390–391 |
| 7 | `PZO22001 Starfinder Player Core 442-464::/page/18/TableCell/234` | 0.556970 | Spell Attack |
| 8 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/15` | 0.533310 | multiple attack penalty (–5 on your second attack, –10 on  further attacks) 394 |
| 9 | `PZO22001 Starfinder Player Core 442-464::/page/8/Text/35` | 0.523613 | epiphany spells 116, **375–377** |
| 10 | `PZO22001 Starfinder Player Core 442-464::/page/4/Text/8` | 0.506697 | spell DC (10 + spellcasting attribute modifier + proficiency  bonus + other bonuses + penalties) **395** |

### Query 61
- Text: What is the rule about Strike (action) 410?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 442-464::/page/1/Text/19']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 442-464::/page/1/Text/19', 'PZO22001 Starfinder Player Core 442-464::/page/3/Text/18', 'PZO22001 Starfinder Player Core 442-464::/page/12/Text/55']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/19` | 0.899924 | Strike (action) 410 |
| 2 | `PZO22001 Starfinder Player Core 442-464::/page/3/Text/18` | 0.741056 | critical hit (Strike) 410 |
| 3 | `PZO22001 Starfinder Player Core 442-464::/page/12/Text/55` | 0.667711 | **Strike **[one-action] (basic action) Make an attack with a weapon or  unarmed attack. 410 |
| 4 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/16` | 0.564920 | basic actions 408–411 |
| 5 | `PZO22001 Starfinder Player Core 442-464::/page/12/Text/1` | 0.529773 | Step and Stride actions 410 travel Speed 430 |
| 6 | `PZO22001 Starfinder Player Core 442-464::/page/10/Text/26` | 0.527217 | **Reactive Strike** [reaction] 414 |
| 7 | `PZO22001 Starfinder Player Core 442-464::/page/12/Text/54` | 0.517233 | **Stride **[one-action] (basic action) Move up to your Speed. 410 Speed 412 |
| 8 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/46` | 0.499833 | **basic action** An action all creatures can use. 408–410 |
| 9 | `PZO22001 Starfinder Player Core 442-464::/page/11/Text/47` | 0.495524 | **speaking** 410 |
| 10 | `PZO22001 Starfinder Player Core 442-464::/page/3/Text/8` | 0.493766 | Take Cover [one-action] (basic action) 410 |

### Query 62
- Text: Summarize **attitudes** 199
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 442-464::/page/1/Text/21']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 442-464::/page/1/Text/21', 'PZO22001 Starfinder Player Core 442-464::/page/7/Text/60', 'PZO22001 Starfinder Player Core 442-464::/page/17/TableCell/227']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/21` | 0.974651 | **attitudes** 199 |
| 2 | `PZO22001 Starfinder Player Core 442-464::/page/7/Text/60` | 0.608801 | **Make an Impression** (skill action) Change someone's attitude.  (Diplomacy) 199 |
| 3 | `PZO22001 Starfinder Player Core 442-464::/page/17/TableCell/227` | 0.586792 | Attitude |
| 4 | `PZO22001 Starfinder Player Core 442-464::/page/5/Text/54` | 0.488407 | **Gather Information** (skill action) Socialize to learn things.  (Diplomacy) 199 |
| 5 | `PZO22001 Starfinder Player Core 442-464::/page/10/Text/41` | 0.476442 | **Reposition **[one-action] (skill action) Move a creature within your reach 194 **Request **[one-action] (skill action) Get someone to help you. (Diplomacy)  199–200 |
| 6 | `PZO22001 Starfinder Player Core 442-464::/page/12/Text/27` | 0.465109 | targets 298 |
| 7 | `PZO22001 Starfinder Player Core 442-464::/page/7/Text/13` | 0.462370 | formulas 197, **237** |
| 8 | `PZO22001 Starfinder Player Core 442-464::/page/5/Text/17` | 0.458093 | general feat 100, **210** |
| 9 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/12` | 0.447995 | **Athletics** (skill) Perform deeds of physical prowess. (Str) 193–195 **attack** (trait) An ability with this trait involves an attack. For  each attack you make beyond the first on your turn, you  t |
| 10 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/29` | 0.442943 | **agile** (weapon trait) 255 |

### Query 63
- Text: Summarize alternate ancestry boosts 24
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 442-464::/page/1/Text/23']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 442-464::/page/1/Text/23', 'PZO22001 Starfinder Player Core 442-464::/page/1/Text/27', 'PZO22001 Starfinder Player Core 442-464::/page/16/TableCell/314']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/23` | 0.998579 | alternate ancestry boosts 24 |
| 2 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/27` | 0.998579 | alternate ancestry boosts 24 |
| 3 | `PZO22001 Starfinder Player Core 442-464::/page/16/TableCell/314` | 0.656415 | Ancestry Feat Boosts |
| 4 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/22` | 0.465992 | **attribute boost** An attribute boost allows you to increase one  of your attribute modifiers by 1. If the attribute modifier  is already +4 or higher, it takes two boosts to increase it;  you get a |
| 5 | `PZO22001 Starfinder Player Core 442-464::/page/15/TableCell/32` | 0.457666 | Ancestry ——— |
| 6 | `PZO22001 Starfinder Player Core 442-464::/page/6/Text/21` | 0.453716 | A custom heritage for characters with two ancestral lines. 83 versatile heritages (can be chosen for a character of any  ancestry) 82–91 |
| 7 | `PZO22001 Starfinder Player Core 442-464::/page/16/TableCell/284` | 0.433069 | Ancestry and Heritage Abilities |
| 8 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/38` | 0.428491 | **ancestry** A broad family of people that a creature belongs to.  Each player character chooses an ancestry as the first step of  character creation. 10, 19, 27, **41–91** mixed ancestry 83 |
| 9 | `PZO22001 Starfinder Player Core 442-464::/page/16/TableCell/364` | 0.424396 | General Feat Boosts |
| 10 | `PZO22001 Starfinder Player Core 442-464::/page/16/Form/0` | 0.417573 | Ancestry and General FeatsClass AbilitiesInventoryLevel 1Ancestry and Heritage AbilitiesClass Feats and FeaturesHeld ItemsBulkAncestry FeatBackground Skill Feat2Skill FeatClass Feat3General FeatClass |

### Query 64
- Text: Summarize voluntary flaws 25
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 442-464::/page/1/Text/25']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 442-464::/page/1/Text/25', 'PZO22001 Starfinder Player Core 442-464::/page/1/Text/24', 'PZO22001 Starfinder Player Core 442-464::/page/14/Text/23']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/25` | 0.993501 | voluntary flaws 25 |
| 2 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/24` | 0.469913 | **attribute flaw** An attribute flaw decreases one of your  attribute modifiers by 1. 23 |
| 3 | `PZO22001 Starfinder Player Core 442-464::/page/14/Text/23` | 0.467855 | **versatile** (weapon trait) 258 |
| 4 | `PZO22001 Starfinder Player Core 442-464::/page/14/Text/20` | 0.400468 | **unwieldy** (weapon trait) 258 |
| 5 | `PZO22001 Starfinder Player Core 442-464::/page/14/Text/32` | 0.383328 | **volley** (weapon trait) 258 |
| 6 | `PZO22001 Starfinder Player Core 442-464::/page/5/Text/56` | 0.371619 | **gender and pronouns** 25 |
| 7 | `PZO22001 Starfinder Player Core 442-464::/page/5/Text/29` | 0.355050 | **flourish** (trait) You can only use one action with the flourish  trait per round. 144 |
| 8 | `PZO22001 Starfinder Player Core 442-464::/page/3/Text/19` | 0.350682 | critical specialization effects (weapons) 258–259 |
| 9 | `PZO22001 Starfinder Player Core 442-464::/page/13/Text/31` | 0.350672 | **thought** (weapon trait) 258 |
| 10 | `PZO22001 Starfinder Player Core 442-464::/page/12/Text/26` | 0.350561 | spontaneous 295 |

### Query 65
- Text: Summarize alternate ancestry boosts 24
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 442-464::/page/1/Text/27']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 442-464::/page/1/Text/23', 'PZO22001 Starfinder Player Core 442-464::/page/1/Text/27', 'PZO22001 Starfinder Player Core 442-464::/page/16/TableCell/314']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/23` | 0.998579 | alternate ancestry boosts 24 |
| 2 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/27` | 0.998579 | alternate ancestry boosts 24 |
| 3 | `PZO22001 Starfinder Player Core 442-464::/page/16/TableCell/314` | 0.656415 | Ancestry Feat Boosts |
| 4 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/22` | 0.465992 | **attribute boost** An attribute boost allows you to increase one  of your attribute modifiers by 1. If the attribute modifier  is already +4 or higher, it takes two boosts to increase it;  you get a |
| 5 | `PZO22001 Starfinder Player Core 442-464::/page/15/TableCell/32` | 0.457666 | Ancestry ——— |
| 6 | `PZO22001 Starfinder Player Core 442-464::/page/6/Text/21` | 0.453716 | A custom heritage for characters with two ancestral lines. 83 versatile heritages (can be chosen for a character of any  ancestry) 82–91 |
| 7 | `PZO22001 Starfinder Player Core 442-464::/page/16/TableCell/284` | 0.433069 | Ancestry and Heritage Abilities |
| 8 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/38` | 0.428491 | **ancestry** A broad family of people that a creature belongs to.  Each player character chooses an ancestry as the first step of  character creation. 10, 19, 27, **41–91** mixed ancestry 83 |
| 9 | `PZO22001 Starfinder Player Core 442-464::/page/16/TableCell/364` | 0.424396 | General Feat Boosts |
| 10 | `PZO22001 Starfinder Player Core 442-464::/page/16/Form/0` | 0.417573 | Ancestry and General FeatsClass AbilitiesInventoryLevel 1Ancestry and Heritage AbilitiesClass Feats and FeaturesHeld ItemsBulkAncestry FeatBackground Skill Feat2Skill FeatClass Feat3General FeatClass |

### Query 66
- Text: Summarize divine attribute (deities) 35, *Pathfinder Player Core* 35 key attribute (class) 99
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 442-464::/page/1/Text/28']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 442-464::/page/1/Text/28', 'PZO22001 Starfinder Player Core 442-464::/page/7/Text/28', 'PZO22001 Starfinder Player Core 442-464::/page/19/Text/71']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/28` | 1.035688 | divine attribute (deities) 35, *Pathfinder Player Core* 35 key attribute (class) 99 |
| 2 | `PZO22001 Starfinder Player Core 442-464::/page/7/Text/28` | 0.647427 | **key attribute** Your key attribute is the attribute modifier  you use to determine your class DC, as well as your spell  attack modifier and spell DC if you're a spellcaster. A  key attribute for a |
| 3 | `PZO22001 Starfinder Player Core 442-464::/page/19/Text/71` | 0.605579 | *Starfinder Player Core *© 2025, Paizo Inc. Paizo, the Paizo  golem, Pathfinder, Starfinder, and other trademarks owned  by Paizo are property of Paizo Inc. All rights reserved. |
| 4 | `PZO22001 Starfinder Player Core 442-464::/page/3/Text/45` | 0.547028 | **deity** Deities are powerful entities. 25, **35–39** |
| 5 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/29` | 0.533245 | key attribute (skill) 183 |
| 6 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/26` | 0.511635 | **attribute modifier** Each creature has six attribute modifiers:  Strength, Dexterity, Constitution, Intelligence, Wisdom,  and Charisma. These numbers represent a creature's raw  potential and basic |
| 7 | `PZO22001 Starfinder Player Core 442-464::/page/2/Text/32` | 0.511152 | **class DC** A class DC sets the difficulty for some abilities  granted by your character's class. Class DC = 10 +  proficiency bonus + key attribute modifier. 25, 99 |
| 8 | `PZO22001 Starfinder Player Core 442-464::/page/11/Text/20` | 0.509983 | **session** A Pathfinder game session usually last a few hours. 5 **shadow** (trait) Magic with this trait involves shadows or the  energy of the Netherworld. |
| 9 | `PZO22001 Starfinder Player Core 442-464::/page/9/Text/16` | 0.505349 | **PC (player character)** *See also* player character. 11 character creation 17–26 |
| 10 | `PZO22001 Starfinder Player Core 442-464::/page/6/Text/3` | 0.497280 | **gods** *See also* deity. 25, **35–39** |

### Query 67
- Text: Summarize **aucturnite** (material) A dull remnant of the planet Aucturn  that causes madness. 278
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 442-464::/page/1/Text/32']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 442-464::/page/1/Text/32', 'PZO22001 Starfinder Player Core 442-464::/page/1/Text/31', 'PZO22001 Starfinder Player Core 442-464::/page/0/Text/22']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/32` | 1.033963 | **aucturnite** (material) A dull remnant of the planet Aucturn  that causes madness. 278 |
| 2 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/31` | 0.634203 | **Aucturn** A former Pact World planet that was destroyed  when the Newborn hatched from it. |
| 3 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/22` | 0.542337 | **adamantine** (material) One of the hardest known metals. 278 **Administer First Aid **[two-actions] (skill action) Stabilize a dying  creature or stanch bleeding. (Medicine) 201 |
| 4 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/30` | 0.497679 | **Akiton** A red desert planet often defined by its economic  decline due to changes in starship technology. 32 |
| 5 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/7` | 0.489420 | **abysium** (material) A glowing blue-green glowing metal that  damages creatures' immune system. 278 |
| 6 | `PZO22001 Starfinder Player Core 442-464::/page/11/Text/29` | 0.484251 | **sickened** (condition) You're sick to your stomach. 439 **silver** (material) A shiny metal that's dangerous to devils and  werecreatures. 279 |
| 7 | `PZO22001 Starfinder Player Core 442-464::/page/6/Text/10` | 0.467763 | **Hardness** A statistic representing an object's durability. 236 **haunt** (trait) A hazard with this trait is a spiritual echo, often  of someone with a tragic death. |
| 8 | `PZO22001 Starfinder Player Core 442-464::/page/8/Text/44` | 0.467097 | **nonplayer character (NPC)** A character controlled by the GM. 11 **noqual** (material) A light metal with anti-magic properties.  279 |
| 9 | `PZO22001 Starfinder Player Core 442-464::/page/3/Text/34` | 0.465837 | **darkness** Creatures and objects in darkness are hidden or  undetected, and creatures without darkvision have the  blinded condition in darkness. 424 |
| 10 | `PZO22001 Starfinder Player Core 442-464::/page/11/Text/24` | 0.457729 | **shimmerstone** (material) A psychically active crystalline ore  that radiates a calming aura. 279 |

### Query 68
- Text: Summarize **augmentations** 288-293
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 442-464::/page/1/Text/34']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 442-464::/page/1/Text/34', 'PZO22001 Starfinder Player Core 442-464::/page/7/Text/9', 'PZO22001 Starfinder Player Core 442-464::/page/1/Text/35']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/34` | 1.012247 | **augmentations** 288-293 |
| 2 | `PZO22001 Starfinder Player Core 442-464::/page/7/Text/9` | 0.951920 | augmentations 288–293 |
| 3 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/35` | 0.683772 | apex augmentations 292–293  biotech augmentations 288–289  cybernetic augmentations 289–291 magitech augmentations 291–292 |
| 4 | `PZO22001 Starfinder Player Core 442-464::/page/14/Text/37` | 0.542702 | weapon upgrades 272–277 |
| 5 | `PZO22001 Starfinder Player Core 442-464::/page/7/Text/1` | 0.485570 | **Install Upgrade** (action) 268 |
| 6 | `PZO22001 Starfinder Player Core 442-464::/page/12/Text/15` | 0.483323 | ranges 298–299 |
| 7 | `PZO22001 Starfinder Player Core 442-464::/page/13/Text/11` | 0.472012 | **summoned** (trait) 299 |
| 8 | `PZO22001 Starfinder Player Core 442-464::/page/7/Text/25` | 0.449401 | weapons 253–267 |
| 9 | `PZO22001 Starfinder Player Core 442-464::/page/7/Text/42` | 0.447535 | leveling up 29 |
| 10 | `PZO22001 Starfinder Player Core 442-464::/page/13/Text/23` | 0.445114 | spell targets 298, 300 |

### Query 69
- Text: Summarize apex augmentations 292–293  biotech augmentations 288–289  cybernetic augmentations 289–291 magitech augmentations 291–292
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 442-464::/page/1/Text/35']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 442-464::/page/1/Text/35', 'PZO22001 Starfinder Player Core 442-464::/page/7/Text/9', 'PZO22001 Starfinder Player Core 442-464::/page/1/Text/34']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/35` | 1.030954 | apex augmentations 292–293  biotech augmentations 288–289  cybernetic augmentations 289–291 magitech augmentations 291–292 |
| 2 | `PZO22001 Starfinder Player Core 442-464::/page/7/Text/9` | 0.652089 | augmentations 288–293 |
| 3 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/34` | 0.605556 | **augmentations** 288-293 |
| 4 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/43` | 0.556878 | **apex** (trait) 292 |
| 5 | `PZO22001 Starfinder Player Core 442-464::/page/14/Text/37` | 0.524768 | weapon upgrades 272–277 |
| 6 | `PZO22001 Starfinder Player Core 442-464::/page/6/Text/47` | 0.482026 | **Implant Augmentation** (exploration activity) implant or  remove an augmentation. 431 |
| 7 | `PZO22001 Starfinder Player Core 442-464::/page/3/Text/19` | 0.424888 | critical specialization effects (weapons) 258–259 |
| 8 | `PZO22001 Starfinder Player Core 442-464::/page/12/Text/10` | 0.416887 | focus spells (epiphany and warp spells) 296–297, 375– 380 |
| 9 | `PZO22001 Starfinder Player Core 442-464::/page/14/Text/50` | 0.414878 | **XP (Experience Points)** *See also* Experience Points 6–7, 29 |
| 10 | `PZO22001 Starfinder Player Core 442-464::/page/7/Text/1` | 0.412202 | **Install Upgrade** (action) 268 |

### Query 70
- Text: Summarize **baseline** 389
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 442-464::/page/1/Text/45']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 442-464::/page/1/Text/45', 'PZO22001 Starfinder Player Core 442-464::/page/9/Text/15', 'PZO22001 Starfinder Player Core 442-464::/page/8/Text/33']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/45` | 0.968738 | **baseline** 389 |
| 2 | `PZO22001 Starfinder Player Core 442-464::/page/9/Text/15` | 0.760943 | **Starfinder baseline** 389 |
| 3 | `PZO22001 Starfinder Player Core 442-464::/page/8/Text/33` | 0.659722 | **multiplying** 391 |
| 4 | `PZO22001 Starfinder Player Core 442-464::/page/11/Text/3` | 0.585015 | **rules overview** 390–391 |
| 5 | `PZO22001 Starfinder Player Core 442-464::/page/11/Text/1` | 0.560860 | **rounding** 391 |
| 6 | `PZO22001 Starfinder Player Core 442-464::/page/3/Text/3` | 0.520922 | **conventions** 391 |
| 7 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/33` | 0.517720 | **ambiguous rules** 391 |
| 8 | `PZO22001 Starfinder Player Core 442-464::/page/12/Text/20` | 0.499934 | bonus + other bonuses + penalties) 395 |
| 9 | `PZO22001 Starfinder Player Core 442-464::/page/5/Text/51` | 0.493915 | **game conventions** 391 |
| 10 | `PZO22001 Starfinder Player Core 442-464::/page/13/Text/10` | 0.489667 | **summon** (trait) 370 |

### Query 71
- Text: Summarize **blinded** (condition) You're unable to see. 435
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 442-464::/page/1/Text/49']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 442-464::/page/1/Text/49', 'PZO22001 Starfinder Player Core 442-464::/page/8/Text/47', 'PZO22001 Starfinder Player Core 442-464::/page/2/Text/44']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/49` | 1.020666 | **blinded** (condition) You're unable to see. 435 |
| 2 | `PZO22001 Starfinder Player Core 442-464::/page/8/Text/47` | 0.675444 | **observed** (condition) You're in clear view. 424, **438** |
| 3 | `PZO22001 Starfinder Player Core 442-464::/page/2/Text/44` | 0.671795 | **concealed** (condition) Low visibility makes you difficult to  target. 426, **435** |
| 4 | `PZO22001 Starfinder Player Core 442-464::/page/7/Text/6` | 0.625524 | **Investigate** (exploration activity) Study your surroundings. 431 **invisible** (condition) Creatures can't see you. 426, **438** |
| 5 | `PZO22001 Starfinder Player Core 442-464::/page/6/Text/24` | 0.613721 | **hidden** (condition) A creature knows your location but can't  see you. 425, **437** |
| 6 | `PZO22001 Starfinder Player Core 442-464::/page/2/Text/6` | 0.611084 | **bright light** Most creatures can see normally in bright light. 424 **broken** (condition) This item can't be used for its normal  function until repaired. 237, **435** |
| 7 | `PZO22001 Starfinder Player Core 442-464::/page/6/Text/43` | 0.602580 | **immobilized** (condition) You can't move. 437 |
| 8 | `PZO22001 Starfinder Player Core 442-464::/page/3/Text/36` | 0.576411 | **darkvision** (sense) See in black and white in darkness 424 **dazzled** (condition) Everything is concealed to you. 436 **DC (Difficulty Class)** *See also* Difficulty Class. 393 |
| 9 | `PZO22001 Starfinder Player Core 442-464::/page/2/Text/49` | 0.570286 | **confused** (condition) You attack indiscriminately. 435 |
| 10 | `PZO22001 Starfinder Player Core 442-464::/page/10/Text/9` | 0.562041 | **prone** (condition) You're lying on the ground. 439 |

### Query 72
- Text: Summarize **INTRODUCTION**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 442-464::/page/1/Text/52']
- Expected found: `True`
- Expected rank: `7`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 442-464::/page/11/Text/54', 'PZO22001 Starfinder Player Core 442-464::/page/5/Text/60', 'PZO22001 Starfinder Player Core 442-464::/page/9/Text/45']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 442-464::/page/11/Text/54` | 0.880541 | **INTRODUCTION** |
| 2 | `PZO22001 Starfinder Player Core 442-464::/page/5/Text/60` | 0.880541 | **INTRODUCTION** |
| 3 | `PZO22001 Starfinder Player Core 442-464::/page/9/Text/45` | 0.880541 | **INTRODUCTION** |
| 4 | `PZO22001 Starfinder Player Core 442-464::/page/3/Text/56` | 0.838541 | **INTRODUCTION** |
| 5 | `PZO22001 Starfinder Player Core 442-464::/page/13/Text/53` | 0.838541 | **INTRODUCTION** |
| 6 | `PZO22001 Starfinder Player Core 442-464::/page/19/Text/77` | 0.838541 | **INTRODUCTION** |
| 7 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/52` | 0.838541 | **INTRODUCTION** |
| 8 | `PZO22001 Starfinder Player Core 442-464::/page/7/Text/71` | 0.526179 | **INTRODUCTION** **ANCESTRIES & ** **BACKGROUNDS** |
| 9 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/64` | 0.452320 | **GAME** |
| 10 | `PZO22001 Starfinder Player Core 442-464::/page/19/Text/87` | 0.448913 | **INDEX** **CHARACTER ** |

### Query 73
- Text: Summarize **CLASSES**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 442-464::/page/1/Text/54']
- Expected found: `True`
- Expected rank: `5`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 442-464::/page/9/Text/47', 'PZO22001 Starfinder Player Core 442-464::/page/11/Text/56', 'PZO22001 Starfinder Player Core 442-464::/page/3/Text/58']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 442-464::/page/9/Text/47` | 0.940061 | **CLASSES** |
| 2 | `PZO22001 Starfinder Player Core 442-464::/page/11/Text/56` | 0.940061 | **CLASSES** |
| 3 | `PZO22001 Starfinder Player Core 442-464::/page/3/Text/58` | 0.940061 | **CLASSES** |
| 4 | `PZO22001 Starfinder Player Core 442-464::/page/19/Text/79` | 0.910061 | **CLASSES** |
| 5 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/54` | 0.910061 | **CLASSES** |
| 6 | `PZO22001 Starfinder Player Core 442-464::/page/13/Text/55` | 0.910061 | **CLASSES** |
| 7 | `PZO22001 Starfinder Player Core 442-464::/page/5/Text/62` | 0.910061 | **CLASSES** |
| 8 | `PZO22001 Starfinder Player Core 442-464::/page/7/Text/62` | 0.719498 | **CLASSES** **SKILLS** |
| 9 | `PZO22001 Starfinder Player Core 442-464::/page/15/TableCell/36` | 0.561502 | Class — |
| 10 | `PZO22001 Starfinder Player Core 442-464::/page/15/TableCell/48` | 0.522230 | Class Notes |

### Query 74
- Text: Summarize **PLAYING THE **
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 442-464::/page/1/Text/59']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 442-464::/page/19/Text/84', 'PZO22001 Starfinder Player Core 442-464::/page/1/Text/59', 'PZO22001 Starfinder Player Core 442-464::/page/11/Text/61']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 442-464::/page/19/Text/84` | 0.953666 | **PLAYING THE ** |
| 2 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/59` | 0.953666 | **PLAYING THE ** |
| 3 | `PZO22001 Starfinder Player Core 442-464::/page/11/Text/61` | 0.833654 | **PLAYING THE ** **GAME** |
| 4 | `PZO22001 Starfinder Player Core 442-464::/page/13/Text/60` | 0.791654 | **PLAYING THE ** **GAME** |
| 5 | `PZO22001 Starfinder Player Core 442-464::/page/3/Text/63` | 0.791654 | **PLAYING THE ** **GAME** |
| 6 | `PZO22001 Starfinder Player Core 442-464::/page/5/Text/67` | 0.791654 | **PLAYING THE ** **GAME** |
| 7 | `PZO22001 Starfinder Player Core 442-464::/page/9/Text/52` | 0.791654 | **PLAYING THE ** **GAME** |
| 8 | `PZO22001 Starfinder Player Core 442-464::/page/7/Text/66` | 0.791654 | **PLAYING THE ** **GAME** |
| 9 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/64` | 0.466206 | **GAME** |
| 10 | `PZO22001 Starfinder Player Core 442-464::/page/9/Text/31` | 0.421609 | **player** One of the real people playing the game. 5 |

### Query 75
- Text: Summarize **GAME**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 442-464::/page/1/Text/64']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 442-464::/page/1/Text/64', 'PZO22001 Starfinder Player Core 442-464::/page/13/Text/60', 'PZO22001 Starfinder Player Core 442-464::/page/9/Text/52']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/64` | 0.878539 | **GAME** |
| 2 | `PZO22001 Starfinder Player Core 442-464::/page/13/Text/60` | 0.728831 | **PLAYING THE ** **GAME** |
| 3 | `PZO22001 Starfinder Player Core 442-464::/page/9/Text/52` | 0.728831 | **PLAYING THE ** **GAME** |
| 4 | `PZO22001 Starfinder Player Core 442-464::/page/11/Text/61` | 0.686831 | **PLAYING THE ** **GAME** |
| 5 | `PZO22001 Starfinder Player Core 442-464::/page/5/Text/67` | 0.686831 | **PLAYING THE ** **GAME** |
| 6 | `PZO22001 Starfinder Player Core 442-464::/page/7/Text/66` | 0.686831 | **PLAYING THE ** **GAME** |
| 7 | `PZO22001 Starfinder Player Core 442-464::/page/3/Text/63` | 0.686831 | **PLAYING THE ** **GAME** |
| 8 | `PZO22001 Starfinder Player Core 442-464::/page/19/Text/85` | 0.621317 | **GAME** **CONDITIONS ** |
| 9 | `PZO22001 Starfinder Player Core 442-464::/page/11/Text/2` | 0.574716 | **RPG (roleplaying game)** 5–6 |
| 10 | `PZO22001 Starfinder Player Core 442-464::/page/10/Text/52` | 0.536194 | **roleplaying game (RPG)** An interactive story where one player,  the Game Master (GM), sets the scene and presents challenges,  while other players take the roles of player characters (PCs)  and att |

### Query 76
- Text: Summarize **CONDITIONS ** **APPENDIX**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 442-464::/page/1/Text/60']
- Expected found: `True`
- Expected rank: `7`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 442-464::/page/13/Text/61', 'PZO22001 Starfinder Player Core 442-464::/page/3/Text/64', 'PZO22001 Starfinder Player Core 442-464::/page/11/Text/62']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 442-464::/page/13/Text/61` | 0.983499 | **CONDITIONS ** **APPENDIX** |
| 2 | `PZO22001 Starfinder Player Core 442-464::/page/3/Text/64` | 0.983499 | **CONDITIONS ** **APPENDIX** |
| 3 | `PZO22001 Starfinder Player Core 442-464::/page/11/Text/62` | 0.983499 | **CONDITIONS ** **APPENDIX** |
| 4 | `PZO22001 Starfinder Player Core 442-464::/page/7/Text/67` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 5 | `PZO22001 Starfinder Player Core 442-464::/page/9/Text/53` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 6 | `PZO22001 Starfinder Player Core 442-464::/page/5/Text/68` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 7 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/60` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 8 | `PZO22001 Starfinder Player Core 442-464::/page/19/Text/86` | 0.573689 | **APPENDIX** **GLOSSARY & ** |
| 9 | `PZO22001 Starfinder Player Core 442-464::/page/19/Text/85` | 0.535379 | **GAME** **CONDITIONS ** |
| 10 | `PZO22001 Starfinder Player Core 442-464::/page/15/TableCell/90` | 0.487719 | Conditions |

### Query 77
- Text: Summarize **GLOSSARY & ** **INDEX**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 442-464::/page/1/Text/61']
- Expected found: `True`
- Expected rank: `5`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 442-464::/page/5/Text/69', 'PZO22001 Starfinder Player Core 442-464::/page/9/Text/54', 'PZO22001 Starfinder Player Core 442-464::/page/7/Text/68']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 442-464::/page/5/Text/69` | 0.993465 | **GLOSSARY & ** **INDEX** |
| 2 | `PZO22001 Starfinder Player Core 442-464::/page/9/Text/54` | 0.993465 | **GLOSSARY & ** **INDEX** |
| 3 | `PZO22001 Starfinder Player Core 442-464::/page/7/Text/68` | 0.993465 | **GLOSSARY & ** **INDEX** |
| 4 | `PZO22001 Starfinder Player Core 442-464::/page/13/Text/62` | 0.951465 | **GLOSSARY & ** **INDEX** |
| 5 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/61` | 0.951465 | **GLOSSARY & ** **INDEX** |
| 6 | `PZO22001 Starfinder Player Core 442-464::/page/11/Text/63` | 0.951465 | **GLOSSARY & ** **INDEX** |
| 7 | `PZO22001 Starfinder Player Core 442-464::/page/3/Text/65` | 0.951465 | **GLOSSARY & ** **INDEX** |
| 8 | `PZO22001 Starfinder Player Core 442-464::/page/0/SectionHeader/1` | 0.825490 | GLOSSARY & INDEX |
| 9 | `PZO22001 Starfinder Player Core 442-464::/page/19/Text/86` | 0.697531 | **APPENDIX** **GLOSSARY & ** |
| 10 | `PZO22001 Starfinder Player Core 442-464::/page/19/Text/87` | 0.495322 | **INDEX** **CHARACTER ** |

### Query 78
- Text: Summarize **Bretheda** A massive gas giant orbited by highly populated  moons, home to floating arcologies known for their biotech  science and artists. 33
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 442-464::/page/2/Text/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 442-464::/page/2/Text/5', 'PZO22001 Starfinder Player Core 442-464::/page/4/Text/1', 'PZO22001 Starfinder Player Core 442-464::/page/7/Text/44']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 442-464::/page/2/Text/5` | 1.041502 | **Bretheda** A massive gas giant orbited by highly populated  moons, home to floating arcologies known for their biotech  science and artists. 33 |
| 2 | `PZO22001 Starfinder Player Core 442-464::/page/4/Text/1` | 0.553340 | **Diaspora** An asteroid belt formed when the twin planets  Damiar and Iovo were destroyed, home to smugglers,  pirates, and sarcesians. 32 |
| 3 | `PZO22001 Starfinder Player Core 442-464::/page/7/Text/44` | 0.527713 | **Liavara** A gas giant which is home to dream prophets and an  above-average amount of psychic energy. 33 |
| 4 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/44` | 0.478466 | **Apostae** A hollow planetoid containing mysterious gateways to  tunnel networks and ancient mechanical complexes. 34 |
| 5 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/3` | 0.459995 | **Aballon** A rocky, sun-blasted planet of industry which is home to  intelligent machines created by the enigmatic First Ones. 31 |
| 6 | `PZO22001 Starfinder Player Core 442-464::/page/4/Text/52` | 0.450951 | **Eox **A radioactive wasteland of a planet ruled by the undead who  destroyed their once lush home world in a terrible disaster. 32 |
| 7 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/30` | 0.449781 | **Akiton** A red desert planet often defined by its economic  decline due to changes in starship technology. 32 |
| 8 | `PZO22001 Starfinder Player Core 442-464::/page/2/Text/18` | 0.428805 | **Castrovel** A jungle planet teeming with psychic energy which  is home to elves, lashunta, and formians. 31 |
| 9 | `PZO22001 Starfinder Player Core 442-464::/page/5/Text/58` | 0.422136 | **giant** (trait) Giants are massive humanoid creatures. |
| 10 | `PZO22001 Starfinder Player Core 442-464::/page/11/Text/46` | 0.419984 | **space** The space a creature's body occupies, and the squares  a creature takes up on a grid. 413–414 |

### Query 79
- Text: Summarize **bright light** Most creatures can see normally in bright light. 424 **broken** (condition) This item can't be used for its normal  function until repaired. 237, **435**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 442-464::/page/2/Text/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 442-464::/page/2/Text/6', 'PZO22001 Starfinder Player Core 442-464::/page/3/Text/34', 'PZO22001 Starfinder Player Core 442-464::/page/7/Text/56']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 442-464::/page/2/Text/6` | 1.025832 | **bright light** Most creatures can see normally in bright light. 424 **broken** (condition) This item can't be used for its normal  function until repaired. 237, **435** |
| 2 | `PZO22001 Starfinder Player Core 442-464::/page/3/Text/34` | 0.721754 | **darkness** Creatures and objects in darkness are hidden or  undetected, and creatures without darkvision have the  blinded condition in darkness. 424 |
| 3 | `PZO22001 Starfinder Player Core 442-464::/page/7/Text/56` | 0.688012 | **low-light vision** (sense) See in dim light as though it were  bright light. 425 |
| 4 | `PZO22001 Starfinder Player Core 442-464::/page/7/Text/6` | 0.608785 | **Investigate** (exploration activity) Study your surroundings. 431 **invisible** (condition) Creatures can't see you. 426, **438** |
| 5 | `PZO22001 Starfinder Player Core 442-464::/page/3/Text/36` | 0.602172 | **darkvision** (sense) See in black and white in darkness 424 **dazzled** (condition) Everything is concealed to you. 436 **DC (Difficulty Class)** *See also* Difficulty Class. 393 |
| 6 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/49` | 0.600904 | **blinded** (condition) You're unable to see. 435 |
| 7 | `PZO22001 Starfinder Player Core 442-464::/page/6/Text/24` | 0.589636 | **hidden** (condition) A creature knows your location but can't  see you. 425, **437** |
| 8 | `PZO22001 Starfinder Player Core 442-464::/page/8/Text/47` | 0.574300 | **observed** (condition) You're in clear view. 424, **438** |
| 9 | `PZO22001 Starfinder Player Core 442-464::/page/4/Text/9` | 0.557892 | **dim light** Creatures and objects in dim light are concealed. 424 **Diplomacy** (skill) Influence others. (Cha) 199–200 |
| 10 | `PZO22001 Starfinder Player Core 442-464::/page/6/Text/1` | 0.548088 | **glitching** (condition) Tech gear and tech creatures with the  glitching condition may not function properly. 437 |

### Query 80
- Text: Summarize **BT (Broken Threshold)** 236
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 442-464::/page/2/Text/8']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 442-464::/page/2/Text/8', 'PZO22001 Starfinder Player Core 442-464::/page/2/Text/7', 'PZO22001 Starfinder Player Core 442-464::/page/11/Text/66']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 442-464::/page/2/Text/8` | 1.017818 | **BT (Broken Threshold)** 236 |
| 2 | `PZO22001 Starfinder Player Core 442-464::/page/2/Text/7` | 0.827872 | **Broken Threshold (BT)** When an object's HP reaches this  number, it becomes broken. 236 |
| 3 | `PZO22001 Starfinder Player Core 442-464::/page/11/Text/66` | 0.514227 | basic saving throw 300, **396** |
| 4 | `PZO22001 Starfinder Player Core 442-464::/page/13/Text/34` | 0.455183 | **toolkit** 238–240 |
| 5 | `PZO22001 Starfinder Player Core 442-464::/page/2/Text/4` | 0.448815 | **breakdown** (weapon trait) 255 |
| 6 | `PZO22001 Starfinder Player Core 442-464::/page/2/Text/6` | 0.446212 | **bright light** Most creatures can see normally in bright light. 424 **broken** (condition) This item can't be used for its normal  function until repaired. 237, **435** |
| 7 | `PZO22001 Starfinder Player Core 442-464::/page/7/Text/16` | 0.444717 | item damage 236 |
| 8 | `PZO22001 Starfinder Player Core 442-464::/page/6/Text/28` | 0.433112 | item Hit Points 236, 402 |
| 9 | `PZO22001 Starfinder Player Core 442-464::/page/13/Text/32` | 0.428850 | **thrown** (weapon trait) 258 |
| 10 | `PZO22001 Starfinder Player Core 442-464::/page/13/Text/25` | 0.426780 | **tech gear** 238–243 |

### Query 81
- Text: Summarize burrow Speed 412
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 442-464::/page/2/Text/12']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 442-464::/page/2/Text/12', 'PZO22001 Starfinder Player Core 442-464::/page/2/Text/35', 'PZO22001 Starfinder Player Core 442-464::/page/5/Text/31']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 442-464::/page/2/Text/12` | 0.992539 | burrow Speed 412 |
| 2 | `PZO22001 Starfinder Player Core 442-464::/page/2/Text/35` | 0.714927 | climb Speed 412 |
| 3 | `PZO22001 Starfinder Player Core 442-464::/page/5/Text/31` | 0.711481 | fly Speed 412 |
| 4 | `PZO22001 Starfinder Player Core 442-464::/page/2/Text/11` | 0.663576 | **Burrow **[one-action] (specialty basic action) Move up to your burrow  Speed. 411 |
| 5 | `PZO22001 Starfinder Player Core 442-464::/page/11/Text/49` | 0.569125 | **Speed** A measure of the distance a character can move using a  single action, measured in feet. *See also* movement. 11, **412** burrow, climb, fly, and swim Speeds 412 |
| 6 | `PZO22001 Starfinder Player Core 442-464::/page/8/Text/29` | 0.502719 | special movement types 412 |
| 7 | `PZO22001 Starfinder Player Core 442-464::/page/8/Text/30` | 0.490849 | Speed (land Speed) 11, 19, **412** |
| 8 | `PZO22001 Starfinder Player Core 442-464::/page/8/Text/24` | 0.469760 | **movement** 412–414 |
| 9 | `PZO22001 Starfinder Player Core 442-464::/page/13/Text/41` | 0.461404 | **travel Speed** 430 |
| 10 | `PZO22001 Starfinder Player Core 442-464::/page/12/Text/1` | 0.456441 | Step and Stride actions 410 travel Speed 430 |

### Query 82
- Text: Summarize **burst** (area) 420
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 442-464::/page/2/Text/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 442-464::/page/2/Text/13', 'PZO22001 Starfinder Player Core 442-464::/page/7/Text/48', 'PZO22001 Starfinder Player Core 442-464::/page/4/Text/43']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 442-464::/page/2/Text/13` | 1.003550 | **burst** (area) 420 |
| 2 | `PZO22001 Starfinder Player Core 442-464::/page/7/Text/48` | 0.660965 | **line** (area) 420 |
| 3 | `PZO22001 Starfinder Player Core 442-464::/page/4/Text/43` | 0.656257 | **emanation** (area) 420 |
| 4 | `PZO22001 Starfinder Player Core 442-464::/page/2/Text/48` | 0.591671 | **cone** (area) 420 |
| 5 | `PZO22001 Starfinder Player Core 442-464::/page/12/Text/3` | 0.520203 | areas 420–421 |
| 6 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/7` | 0.478125 | **archetype** (trait) This feat belongs to an archetype. 174 **area** A specified shape and size of an effect. 298, 300, **420** **area (burst, cone, line)** (weapon trait) 255 |
| 7 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/8` | 0.460546 | **Area Fire **[two-actions] (specialty basic action) Hit each creature in a  designated area. 156, 255, **410** |
| 8 | `PZO22001 Starfinder Player Core 442-464::/page/11/Text/48` | 0.451379 | **special battles** mounted, aerial, and aquatic combat 429 **specialty basic action** 410–411 |
| 9 | `PZO22001 Starfinder Player Core 442-464::/page/6/Text/39` | 0.442054 | **Hustle** (exploration activity) Move at double your travel  Speed. 431 |
| 10 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/19` | 0.439805 | Strike (action) 410 |

### Query 83
- Text: Summarize **Castrovel** A jungle planet teeming with psychic energy which  is home to elves, lashunta, and formians. 31
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 442-464::/page/2/Text/18']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 442-464::/page/2/Text/18', 'PZO22001 Starfinder Player Core 442-464::/page/7/Text/44', 'PZO22001 Starfinder Player Core 442-464::/page/10/Text/10']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 442-464::/page/2/Text/18` | 1.040768 | **Castrovel** A jungle planet teeming with psychic energy which  is home to elves, lashunta, and formians. 31 |
| 2 | `PZO22001 Starfinder Player Core 442-464::/page/7/Text/44` | 0.545163 | **Liavara** A gas giant which is home to dream prophets and an  above-average amount of psychic energy. 33 |
| 3 | `PZO22001 Starfinder Player Core 442-464::/page/10/Text/10` | 0.535756 | **Pulonis** A recently liberated, low-gravity jungle world in the  Veskarium which recently became a member of the Pact  Worlds. 34 |
| 4 | `PZO22001 Starfinder Player Core 442-464::/page/9/Text/10` | 0.474949 | **Pact Worlds** The governing body of planets that make up the  core of the primary Starfinder setting. 30–34 |
| 5 | `PZO22001 Starfinder Player Core 442-464::/page/12/Text/38` | 0.473994 | **squox** Squoxes are tiny animals from Castrovel that resemble  a mix of a fox and a squirrel. |
| 6 | `PZO22001 Starfinder Player Core 442-464::/page/4/Text/1` | 0.473705 | **Diaspora** An asteroid belt formed when the twin planets  Damiar and Iovo were destroyed, home to smugglers,  pirates, and sarcesians. 32 |
| 7 | `PZO22001 Starfinder Player Core 442-464::/page/13/Text/47` | 0.472374 | **Triaxus** A planet defined by its long seasons and high  population of dragons. 33 |
| 8 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/3` | 0.466537 | **Aballon** A rocky, sun-blasted planet of industry which is home to  intelligent machines created by the enigmatic First Ones. 31 |
| 9 | `PZO22001 Starfinder Player Core 442-464::/page/14/Text/22` | 0.458184 | **Verces** A tidally locked planet which is half frozen and half desert,  with a world-spanning Ring of Nations between the two. 32 |
| 10 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/44` | 0.457275 | **Apostae** A hollow planetoid containing mysterious gateways to  tunnel networks and ancient mechanical complexes. 34 |

### Query 84
- Text: Summarize **circumstance bonus** A bonus due to a situation. 392
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 442-464::/page/2/Text/29']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 442-464::/page/2/Text/29', 'PZO22001 Starfinder Player Core 442-464::/page/2/Text/30', 'PZO22001 Starfinder Player Core 442-464::/page/12/Text/45']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 442-464::/page/2/Text/29` | 1.029665 | **circumstance bonus** A bonus due to a situation. 392 |
| 2 | `PZO22001 Starfinder Player Core 442-464::/page/2/Text/30` | 0.865887 | **circumstance penalty** A penalty due to a situation. 392 |
| 3 | `PZO22001 Starfinder Player Core 442-464::/page/12/Text/45` | 0.736079 | **status bonus** A bonus that typically comes from a spell or  condition and represents a beneficial status. 392 |
| 4 | `PZO22001 Starfinder Player Core 442-464::/page/2/Text/47` | 0.609264 | **condition** An ongoing effect that changes how a character  can act or alters some of their statistics. 10, 419, **435–441** redundant conditions 441 |
| 5 | `PZO22001 Starfinder Player Core 442-464::/page/12/Text/46` | 0.581318 | **status penalty** A penalty that typically comes from a spell or  condition and represents a detrimental status. 392 |
| 6 | `PZO22001 Starfinder Player Core 442-464::/page/7/Text/15` | 0.569504 | item bonus or penalty 392 |
| 7 | `PZO22001 Starfinder Player Core 442-464::/page/3/Text/7` | 0.541672 | **cover** When you're behind a physical obstacle, you get a +2  circumstance bonus to AC, Reflex saves vs. area effects,  and Stealth checks. This increases to +4 for greater cover.  Creatures can pro |
| 8 | `PZO22001 Starfinder Player Core 442-464::/page/12/Text/20` | 0.540416 | bonus + other bonuses + penalties) 395 |
| 9 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/50` | 0.533462 | **bludgeoning** (damage type) A type of physical damage. 401 **bonus** A positive value added to a calculation. Add only the  highest bonus of a single type (circumstance, item, status).  10, **392** |
| 10 | `PZO22001 Starfinder Player Core 442-464::/page/9/Text/25` | 0.512020 | **persistent damage** (condition) You keep taking damage every  round. 439 |

### Query 85
- Text: Summarize **circumstance penalty** A penalty due to a situation. 392
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 442-464::/page/2/Text/30']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 442-464::/page/2/Text/30', 'PZO22001 Starfinder Player Core 442-464::/page/2/Text/29', 'PZO22001 Starfinder Player Core 442-464::/page/12/Text/46']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 442-464::/page/2/Text/30` | 1.029339 | **circumstance penalty** A penalty due to a situation. 392 |
| 2 | `PZO22001 Starfinder Player Core 442-464::/page/2/Text/29` | 0.861640 | **circumstance bonus** A bonus due to a situation. 392 |
| 3 | `PZO22001 Starfinder Player Core 442-464::/page/12/Text/46` | 0.727346 | **status penalty** A penalty that typically comes from a spell or  condition and represents a detrimental status. 392 |
| 4 | `PZO22001 Starfinder Player Core 442-464::/page/9/Text/17` | 0.595291 | **penalty** A negative value added to a calculation. Add only  the worst penalty of a single type (circumstance, item,  status). 10, **392–393** |
| 5 | `PZO22001 Starfinder Player Core 442-464::/page/9/Text/3` | 0.592068 | **off-guard** (condition) You take a –2 circumstance penalty to  AC. 438 |
| 6 | `PZO22001 Starfinder Player Core 442-464::/page/14/Text/19` | 0.574006 | **untyped penalty** A penalty that doesn't list a type and is  cumulative with other untyped penalties. 392 |
| 7 | `PZO22001 Starfinder Player Core 442-464::/page/7/Text/15` | 0.563301 | item bonus or penalty 392 |
| 8 | `PZO22001 Starfinder Player Core 442-464::/page/2/Text/47` | 0.554982 | **condition** An ongoing effect that changes how a character  can act or alters some of their statistics. 10, 419, **435–441** redundant conditions 441 |
| 9 | `PZO22001 Starfinder Player Core 442-464::/page/9/Text/25` | 0.505316 | **persistent damage** (condition) You keep taking damage every  round. 439 |
| 10 | `PZO22001 Starfinder Player Core 442-464::/page/12/Text/45` | 0.499263 | **status bonus** A bonus that typically comes from a spell or  condition and represents a beneficial status. 392 |

### Query 86
- Text: Summarize climb Speed 412
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 442-464::/page/2/Text/35']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 442-464::/page/2/Text/35', 'PZO22001 Starfinder Player Core 442-464::/page/5/Text/31', 'PZO22001 Starfinder Player Core 442-464::/page/2/Text/12']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 442-464::/page/2/Text/35` | 0.991128 | climb Speed 412 |
| 2 | `PZO22001 Starfinder Player Core 442-464::/page/5/Text/31` | 0.794658 | fly Speed 412 |
| 3 | `PZO22001 Starfinder Player Core 442-464::/page/2/Text/12` | 0.734439 | burrow Speed 412 |
| 4 | `PZO22001 Starfinder Player Core 442-464::/page/8/Text/29` | 0.594740 | special movement types 412 |
| 5 | `PZO22001 Starfinder Player Core 442-464::/page/11/Text/49` | 0.580698 | **Speed** A measure of the distance a character can move using a  single action, measured in feet. *See also* movement. 11, **412** burrow, climb, fly, and swim Speeds 412 |
| 6 | `PZO22001 Starfinder Player Core 442-464::/page/8/Text/24` | 0.565018 | **movement** 412–414 |
| 7 | `PZO22001 Starfinder Player Core 442-464::/page/8/Text/30` | 0.552256 | Speed (land Speed) 11, 19, **412** |
| 8 | `PZO22001 Starfinder Player Core 442-464::/page/13/Text/41` | 0.546675 | **travel Speed** 430 |
| 9 | `PZO22001 Starfinder Player Core 442-464::/page/12/Text/54` | 0.542879 | **Stride **[one-action] (basic action) Move up to your Speed. 410 Speed 412 |
| 10 | `PZO22001 Starfinder Player Core 442-464::/page/12/Text/1` | 0.529902 | Step and Stride actions 410 travel Speed 430 |

### Query 87
- Text: Summarize **concealed** (condition) Low visibility makes you difficult to  target. 426, **435**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 442-464::/page/2/Text/44']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 442-464::/page/2/Text/44', 'PZO22001 Starfinder Player Core 442-464::/page/1/Text/49', 'PZO22001 Starfinder Player Core 442-464::/page/3/Text/36']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 442-464::/page/2/Text/44` | 1.030283 | **concealed** (condition) Low visibility makes you difficult to  target. 426, **435** |
| 2 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/49` | 0.680791 | **blinded** (condition) You're unable to see. 435 |
| 3 | `PZO22001 Starfinder Player Core 442-464::/page/3/Text/36` | 0.641532 | **darkvision** (sense) See in black and white in darkness 424 **dazzled** (condition) Everything is concealed to you. 436 **DC (Difficulty Class)** *See also* Difficulty Class. 393 |
| 4 | `PZO22001 Starfinder Player Core 442-464::/page/8/Text/47` | 0.592723 | **observed** (condition) You're in clear view. 424, **438** |
| 5 | `PZO22001 Starfinder Player Core 442-464::/page/6/Text/24` | 0.579112 | **hidden** (condition) A creature knows your location but can't  see you. 425, **437** |
| 6 | `PZO22001 Starfinder Player Core 442-464::/page/7/Text/6` | 0.577919 | **Investigate** (exploration activity) Study your surroundings. 431 **invisible** (condition) Creatures can't see you. 426, **438** |
| 7 | `PZO22001 Starfinder Player Core 442-464::/page/2/Text/49` | 0.566815 | **confused** (condition) You attack indiscriminately. 435 |
| 8 | `PZO22001 Starfinder Player Core 442-464::/page/5/Text/11` | 0.559397 | **fatigued** (condition) Your defenses are lower, and you can't  use exploration activities while traveling. 437 |
| 9 | `PZO22001 Starfinder Player Core 442-464::/page/14/Text/11` | 0.549904 | **undetected** (condition) A creature doesn't know your precise  location. 425–426, **441** |
| 10 | `PZO22001 Starfinder Player Core 442-464::/page/13/Text/5` | 0.542792 | **stupefied** (condition) Your can't access your full mental  faculties, and you have trouble casting spells. 440 |

### Query 88
- Text: Summarize **cone** (area) 420
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 442-464::/page/2/Text/48']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 442-464::/page/2/Text/48', 'PZO22001 Starfinder Player Core 442-464::/page/7/Text/48', 'PZO22001 Starfinder Player Core 442-464::/page/4/Text/43']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 442-464::/page/2/Text/48` | 0.989903 | **cone** (area) 420 |
| 2 | `PZO22001 Starfinder Player Core 442-464::/page/7/Text/48` | 0.717970 | **line** (area) 420 |
| 3 | `PZO22001 Starfinder Player Core 442-464::/page/4/Text/43` | 0.708405 | **emanation** (area) 420 |
| 4 | `PZO22001 Starfinder Player Core 442-464::/page/2/Text/13` | 0.602106 | **burst** (area) 420 |
| 5 | `PZO22001 Starfinder Player Core 442-464::/page/12/Text/3` | 0.569951 | areas 420–421 |
| 6 | `PZO22001 Starfinder Player Core 442-464::/page/11/Text/47` | 0.457543 | **speaking** 410 |
| 7 | `PZO22001 Starfinder Player Core 442-464::/page/14/Text/54` | 0.451706 | **zone** (trait) 168 |
| 8 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/7` | 0.444828 | **archetype** (trait) This feat belongs to an archetype. 174 **area** A specified shape and size of an effect. 298, 300, **420** **area (burst, cone, line)** (weapon trait) 255 |
| 9 | `PZO22001 Starfinder Player Core 442-464::/page/3/Text/3` | 0.442179 | **conventions** 391 |
| 10 | `PZO22001 Starfinder Player Core 442-464::/page/13/Text/10` | 0.438758 | **summon** (trait) 370 |

### Query 89
- Text: Summarize **conventions** 391
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 442-464::/page/3/Text/3']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 442-464::/page/3/Text/3', 'PZO22001 Starfinder Player Core 442-464::/page/5/Text/51', 'PZO22001 Starfinder Player Core 442-464::/page/8/Text/33']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 442-464::/page/3/Text/3` | 0.992563 | **conventions** 391 |
| 2 | `PZO22001 Starfinder Player Core 442-464::/page/5/Text/51` | 0.779516 | **game conventions** 391 |
| 3 | `PZO22001 Starfinder Player Core 442-464::/page/8/Text/33` | 0.684165 | **multiplying** 391 |
| 4 | `PZO22001 Starfinder Player Core 442-464::/page/11/Text/3` | 0.592539 | **rules overview** 390–391 |
| 5 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/33` | 0.585685 | **ambiguous rules** 391 |
| 6 | `PZO22001 Starfinder Player Core 442-464::/page/11/Text/1` | 0.582865 | **rounding** 391 |
| 7 | `PZO22001 Starfinder Player Core 442-464::/page/12/Text/20` | 0.522140 | bonus + other bonuses + penalties) 395 |
| 8 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/45` | 0.511080 | **baseline** 389 |
| 9 | `PZO22001 Starfinder Player Core 442-464::/page/2/Text/29` | 0.499063 | **circumstance bonus** A bonus due to a situation. 392 |
| 10 | `PZO22001 Starfinder Player Core 442-464::/page/4/Text/31` | 0.488919 | **duplicate effects** 391 |

### Query 90
- Text: Summarize **cost of living** **243**, 433
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 442-464::/page/3/Text/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 442-464::/page/3/Text/5', 'PZO22001 Starfinder Player Core 442-464::/page/8/Text/17', 'PZO22001 Starfinder Player Core 442-464::/page/3/Text/20']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 442-464::/page/3/Text/5` | 1.014549 | **cost of living** **243**, 433 |
| 2 | `PZO22001 Starfinder Player Core 442-464::/page/8/Text/17` | 0.526175 | **money** 233 |
| 3 | `PZO22001 Starfinder Player Core 442-464::/page/3/Text/20` | 0.514998 | **currency** 233 |
| 4 | `PZO22001 Starfinder Player Core 442-464::/page/8/Text/47` | 0.447687 | **observed** (condition) You're in clear view. 424, **438** |
| 5 | `PZO22001 Starfinder Player Core 442-464::/page/7/Text/47` | 0.436981 | **light and darkness** 299, **424–425** |
| 6 | `PZO22001 Starfinder Player Core 442-464::/page/10/Text/14` | 0.434517 | **range** 254, **418** |
| 7 | `PZO22001 Starfinder Player Core 442-464::/page/12/Text/7` | 0.430913 | counteracting 301, **423** |
| 8 | `PZO22001 Starfinder Player Core 442-464::/page/3/Text/14` | 0.426525 | **credits** 233 |
| 9 | `PZO22001 Starfinder Player Core 442-464::/page/7/Text/49` | 0.422702 | **line of effect** 300, **418–419** |
| 10 | `PZO22001 Starfinder Player Core 442-464::/page/8/Text/4` | 0.420500 | **medical items** 241–243 |

### Query 91
- Text: Summarize **credits** 233
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 442-464::/page/3/Text/14']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 442-464::/page/3/Text/14', 'PZO22001 Starfinder Player Core 442-464::/page/3/Text/20', 'PZO22001 Starfinder Player Core 442-464::/page/8/Text/17']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 442-464::/page/3/Text/14` | 0.979384 | **credits** 233 |
| 2 | `PZO22001 Starfinder Player Core 442-464::/page/3/Text/20` | 0.781314 | **currency** 233 |
| 3 | `PZO22001 Starfinder Player Core 442-464::/page/8/Text/17` | 0.776583 | **money** 233 |
| 4 | `PZO22001 Starfinder Player Core 442-464::/page/3/Text/15` | 0.646870 | credsticks 233 |
| 5 | `PZO22001 Starfinder Player Core 442-464::/page/12/Text/52` | 0.571642 | **stowed item** 234 |
| 6 | `PZO22001 Starfinder Player Core 442-464::/page/6/Text/19` | 0.555424 | **held item** 234 |
| 7 | `PZO22001 Starfinder Player Core 442-464::/page/8/Text/46` | 0.532867 | **object** *See also* item. 233–237 |
| 8 | `PZO22001 Starfinder Player Core 442-464::/page/14/Text/48` | 0.532369 | **worn item** 234 |
| 9 | `PZO22001 Starfinder Player Core 442-464::/page/4/Text/53` | 0.510174 | **equipment** *See also* items. 23, **233–293** |
| 10 | `PZO22001 Starfinder Player Core 442-464::/page/11/Text/26` | 0.475919 | **shoddy items** 237 |

### Query 92
- Text: Summarize credsticks 233
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 442-464::/page/3/Text/15']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 442-464::/page/3/Text/15', 'PZO22001 Starfinder Player Core 442-464::/page/3/Text/14', 'PZO22001 Starfinder Player Core 442-464::/page/3/Text/20']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 442-464::/page/3/Text/15` | 0.976126 | credsticks 233 |
| 2 | `PZO22001 Starfinder Player Core 442-464::/page/3/Text/14` | 0.681067 | **credits** 233 |
| 3 | `PZO22001 Starfinder Player Core 442-464::/page/3/Text/20` | 0.638700 | **currency** 233 |
| 4 | `PZO22001 Starfinder Player Core 442-464::/page/8/Text/17` | 0.546715 | **money** 233 |
| 5 | `PZO22001 Starfinder Player Core 442-464::/page/8/Text/46` | 0.475492 | **object** *See also* item. 233–237 |
| 6 | `PZO22001 Starfinder Player Core 442-464::/page/6/Text/19` | 0.450537 | **held item** 234 |
| 7 | `PZO22001 Starfinder Player Core 442-464::/page/7/Text/26` | 0.444297 | wearing toolkits 238 |
| 8 | `PZO22001 Starfinder Player Core 442-464::/page/13/Text/34` | 0.442865 | **toolkit** 238–240 |
| 9 | `PZO22001 Starfinder Player Core 442-464::/page/7/Text/41` | 0.440563 | item level 234 |
| 10 | `PZO22001 Starfinder Player Core 442-464::/page/7/Text/17` | 0.440563 | item level 234 |

### Query 93
- Text: Summarize critical hit (Strike) 410
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 442-464::/page/3/Text/18']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 442-464::/page/3/Text/18', 'PZO22001 Starfinder Player Core 442-464::/page/1/Text/19', 'PZO22001 Starfinder Player Core 442-464::/page/12/Text/55']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 442-464::/page/3/Text/18` | 1.011803 | critical hit (Strike) 410 |
| 2 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/19` | 0.798827 | Strike (action) 410 |
| 3 | `PZO22001 Starfinder Player Core 442-464::/page/12/Text/55` | 0.637388 | **Strike **[one-action] (basic action) Make an attack with a weapon or  unarmed attack. 410 |
| 4 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/14` | 0.587038 | Aid (reaction used to grant a bonus to an ally's attack roll) 408 critical hits **393**, 399, 410 |
| 5 | `PZO22001 Starfinder Player Core 442-464::/page/11/Text/47` | 0.540528 | **speaking** 410 |
| 6 | `PZO22001 Starfinder Player Core 442-464::/page/13/SectionHeader/27` | 0.533048 | **temporary Hit Points** 402 |
| 7 | `PZO22001 Starfinder Player Core 442-464::/page/10/Text/26` | 0.528960 | **Reactive Strike** [reaction] 414 |
| 8 | `PZO22001 Starfinder Player Core 442-464::/page/6/Text/29` | 0.494985 | temporary Hit Points 402 |
| 9 | `PZO22001 Starfinder Player Core 442-464::/page/12/Text/54` | 0.471992 | **Stride **[one-action] (basic action) Move up to your Speed. 410 Speed 412 |
| 10 | `PZO22001 Starfinder Player Core 442-464::/page/0/Text/16` | 0.450434 | basic actions 408–411 |

### Query 94
- Text: Summarize critical specialization effects (weapons) 258–259
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 442-464::/page/3/Text/19']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 442-464::/page/3/Text/19', 'PZO22001 Starfinder Player Core 442-464::/page/14/Text/36', 'PZO22001 Starfinder Player Core 442-464::/page/7/Text/25']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 442-464::/page/3/Text/19` | 1.028924 | critical specialization effects (weapons) 258–259 |
| 2 | `PZO22001 Starfinder Player Core 442-464::/page/14/Text/36` | 0.827336 | critical specialization 258–259 |
| 3 | `PZO22001 Starfinder Player Core 442-464::/page/7/Text/25` | 0.658940 | weapons 253–267 |
| 4 | `PZO22001 Starfinder Player Core 442-464::/page/3/Text/16` | 0.613057 | **critical** (weapon trait) 256 |
| 5 | `PZO22001 Starfinder Player Core 442-464::/page/13/Text/39` | 0.603650 | weapon traits 255–258 |
| 6 | `PZO22001 Starfinder Player Core 442-464::/page/14/Text/38` | 0.603650 | weapon traits 255–258 |
| 7 | `PZO22001 Starfinder Player Core 442-464::/page/14/Text/23` | 0.595557 | **versatile** (weapon trait) 258 |
| 8 | `PZO22001 Starfinder Player Core 442-464::/page/15/TableCell/211` | 0.591103 | Critical Specializations |
| 9 | `PZO22001 Starfinder Player Core 442-464::/page/13/Text/31` | 0.577168 | **thought** (weapon trait) 258 |
| 10 | `PZO22001 Starfinder Player Core 442-464::/page/14/Text/35` | 0.575745 | **weakness** Increases damage you take of a certain type. 400 **weapon** 253–267 |

### Query 95
- Text: Summarize **currency** 233
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 442-464::/page/3/Text/20']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 442-464::/page/3/Text/20', 'PZO22001 Starfinder Player Core 442-464::/page/8/Text/17', 'PZO22001 Starfinder Player Core 442-464::/page/3/Text/14']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 442-464::/page/3/Text/20` | 0.998622 | **currency** 233 |
| 2 | `PZO22001 Starfinder Player Core 442-464::/page/8/Text/17` | 0.857430 | **money** 233 |
| 3 | `PZO22001 Starfinder Player Core 442-464::/page/3/Text/14` | 0.801734 | **credits** 233 |
| 4 | `PZO22001 Starfinder Player Core 442-464::/page/3/Text/15` | 0.665940 | credsticks 233 |
| 5 | `PZO22001 Starfinder Player Core 442-464::/page/8/Text/46` | 0.621491 | **object** *See also* item. 233–237 |
| 6 | `PZO22001 Starfinder Player Core 442-464::/page/12/Text/52` | 0.584147 | **stowed item** 234 |
| 7 | `PZO22001 Starfinder Player Core 442-464::/page/6/Text/19` | 0.577116 | **held item** 234 |
| 8 | `PZO22001 Starfinder Player Core 442-464::/page/4/Text/53` | 0.572639 | **equipment** *See also* items. 23, **233–293** |
| 9 | `PZO22001 Starfinder Player Core 442-464::/page/14/Text/48` | 0.563667 | **worn item** 234 |
| 10 | `PZO22001 Starfinder Player Core 442-464::/page/7/Text/10` | 0.514810 | Bulk 234 |

### Query 96
- Text: Summarize **d4, d6, d8, d10, d12, d20, and d**% Notations for different sizes  of dice. "d20" is a twenty-sided die, for example. 6
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 442-464::/page/3/Text/22']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 442-464::/page/3/Text/22', 'PZO22001 Starfinder Player Core 442-464::/page/8/Text/39', 'PZO22001 Starfinder Player Core 442-464::/page/4/Text/2']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 442-464::/page/3/Text/22` | 1.037155 | **d4, d6, d8, d10, d12, d20, and d**% Notations for different sizes  of dice. "d20" is a twenty-sided die, for example. 6 |
| 2 | `PZO22001 Starfinder Player Core 442-464::/page/8/Text/39` | 0.645034 | **narrow surface** You must Balance to cross a narrow surface. 415 **natural 1, natural 20** When you roll a d20 and the number on  the die is a 1, decrease your degree of success by one step.  When t |
| 3 | `PZO22001 Starfinder Player Core 442-464::/page/4/Text/2` | 0.607013 | **dice (singular "die")** 6, 254 |
| 4 | `PZO22001 Starfinder Player Core 442-464::/page/10/Text/53` | 0.530787 | **roll** Any time you roll the dice, you're making a roll. The most  common type of roll is a check (comparing a d20 plus  modifiers against a DC). 8, 392–393 |
| 5 | `PZO22001 Starfinder Player Core 442-464::/page/4/Text/3` | 0.515269 | **die roll** Any time you roll the dice. 8, 392–393 |
| 6 | `PZO22001 Starfinder Player Core 442-464::/page/2/Text/24` | 0.487148 | **check** When you roll a d20 and add modifiers, bonuses, and  penalties, then compare your result to a Difficulty Class,  you're attempting a check. 10, **392–394** |
| 7 | `PZO22001 Starfinder Player Core 442-464::/page/2/Text/21` | 0.464017 | **character sheet** Formatted pages on which you can record  your character choices, statistics, feats, spells, and details.  20–21, **457–460** |
| 8 | `PZO22001 Starfinder Player Core 442-464::/page/5/Text/26` | 0.462193 | **flat check** A d20 roll that measures pure chance that can't have  any modifiers, bonuses, or penalties applied to it. 397 |
| 9 | `PZO22001 Starfinder Player Core 442-464::/page/5/Text/42` | 0.456601 | **fortune** (trait) A fortune effect beneficially alters how you roll  your dice. You can never have more than one fortune effect  alter a single roll. If multiple fortune effects would apply,  you ha |
| 10 | `PZO22001 Starfinder Player Core 442-464::/page/3/Text/45` | 0.456138 | **deity** Deities are powerful entities. 25, **35–39** |

### Query 97
- Text: Summarize doubling and halving 399
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 442-464::/page/3/Text/30']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 442-464::/page/3/Text/30', 'PZO22001 Starfinder Player Core 442-464::/page/11/Text/66', 'PZO22001 Starfinder Player Core 442-464::/page/3/Text/32']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 442-464::/page/3/Text/30` | 0.993540 | doubling and halving 399 |
| 2 | `PZO22001 Starfinder Player Core 442-464::/page/11/Text/66` | 0.474330 | basic saving throw 300, **396** |
| 3 | `PZO22001 Starfinder Player Core 442-464::/page/3/Text/32` | 0.471700 | nonlethal attack 399 |
| 4 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/17` | 0.429700 | nonlethal attack 399 |
| 5 | `PZO22001 Starfinder Player Core 442-464::/page/12/Text/15` | 0.411083 | ranges 298–299 |
| 6 | `PZO22001 Starfinder Player Core 442-464::/page/4/Text/31` | 0.401286 | **duplicate effects** 391 |
| 7 | `PZO22001 Starfinder Player Core 442-464::/page/12/Text/26` | 0.396032 | spontaneous 295 |
| 8 | `PZO22001 Starfinder Player Core 442-464::/page/11/Text/7` | 0.392970 | **save** saving throw 11, 24, 300, **396** |
| 9 | `PZO22001 Starfinder Player Core 442-464::/page/7/Text/49` | 0.386396 | **line of effect** 300, **418–419** |
| 10 | `PZO22001 Starfinder Player Core 442-464::/page/13/Text/23` | 0.380928 | spell targets 298, 300 |

### Query 98
- Text: Summarize **darkness** Creatures and objects in darkness are hidden or  undetected, and creatures without darkvision have the  blinded condition in darkness. 424
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 442-464::/page/3/Text/34']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 442-464::/page/3/Text/34', 'PZO22001 Starfinder Player Core 442-464::/page/3/Text/36', 'PZO22001 Starfinder Player Core 442-464::/page/2/Text/6']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 442-464::/page/3/Text/34` | 1.029894 | **darkness** Creatures and objects in darkness are hidden or  undetected, and creatures without darkvision have the  blinded condition in darkness. 424 |
| 2 | `PZO22001 Starfinder Player Core 442-464::/page/3/Text/36` | 0.764252 | **darkvision** (sense) See in black and white in darkness 424 **dazzled** (condition) Everything is concealed to you. 436 **DC (Difficulty Class)** *See also* Difficulty Class. 393 |
| 3 | `PZO22001 Starfinder Player Core 442-464::/page/2/Text/6` | 0.703420 | **bright light** Most creatures can see normally in bright light. 424 **broken** (condition) This item can't be used for its normal  function until repaired. 237, **435** |
| 4 | `PZO22001 Starfinder Player Core 442-464::/page/3/Text/35` | 0.653411 | **darkness** (trait) Darkness effects extinguish non-magical light  in the area and can counteract less powerful magical light.  You must usually target light magic with your darkness  magic directly |
| 5 | `PZO22001 Starfinder Player Core 442-464::/page/6/Text/24` | 0.635390 | **hidden** (condition) A creature knows your location but can't  see you. 425, **437** |
| 6 | `PZO22001 Starfinder Player Core 442-464::/page/7/Text/56` | 0.631978 | **low-light vision** (sense) See in dim light as though it were  bright light. 425 |
| 7 | `PZO22001 Starfinder Player Core 442-464::/page/7/Text/6` | 0.626315 | **Investigate** (exploration activity) Study your surroundings. 431 **invisible** (condition) Creatures can't see you. 426, **438** |
| 8 | `PZO22001 Starfinder Player Core 442-464::/page/14/Text/15` | 0.606188 | **unnoticed** (condition) A creature is entirely unaware you're  present. 426, **441** |
| 9 | `PZO22001 Starfinder Player Core 442-464::/page/14/Text/11` | 0.593385 | **undetected** (condition) A creature doesn't know your precise  location. 425–426, **441** |
| 10 | `PZO22001 Starfinder Player Core 442-464::/page/7/Text/46` | 0.589016 | **light** (trait) Light effects overcome non-magical darkness  in the area, and can counteract magical darkness. You  must usually target darkness magic with your light magic  directly to counteract t |

### Query 99
- Text: Summarize **death and dying** 402–404
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 442-464::/page/3/Text/39']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 442-464::/page/3/Text/39', 'PZO22001 Starfinder Player Core 442-464::/page/4/Text/35', 'PZO22001 Starfinder Player Core 442-464::/page/3/Text/40']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 442-464::/page/3/Text/39` | 1.013269 | **death and dying** 402–404 |
| 2 | `PZO22001 Starfinder Player Core 442-464::/page/4/Text/35` | 0.894383 | death and dying rules 402–404 |
| 3 | `PZO22001 Starfinder Player Core 442-464::/page/3/Text/40` | 0.751005 | instant death 403–404 |
| 4 | `PZO22001 Starfinder Player Core 442-464::/page/6/Text/13` | 0.617928 | **healing** 402 |
| 5 | `PZO22001 Starfinder Player Core 442-464::/page/2/Text/27` | 0.585019 | recovery check (while dying) 403 |
| 6 | `PZO22001 Starfinder Player Core 442-464::/page/3/Text/29` | 0.582178 | damage while dying 403 |
| 7 | `PZO22001 Starfinder Player Core 442-464::/page/7/Text/47` | 0.569086 | **light and darkness** 299, **424–425** |
| 8 | `PZO22001 Starfinder Player Core 442-464::/page/14/Text/8` | 0.566541 | **unconscious** (condition) You're asleep or knocked out. 440 death, dying, and unconscious rules 402–404 |
| 9 | `PZO22001 Starfinder Player Core 442-464::/page/4/Text/34` | 0.553070 | **dying** (condition) You have been reduced to 0 HP and are  nearing death. 436 |
| 10 | `PZO22001 Starfinder Player Core 442-464::/page/8/Text/24` | 0.552169 | **movement** 412–414 |

### Query 100
- Text: What are the requirements for **prerequisites** Many feats and other abilities can be taken  only if you meet their prerequisites. Prerequisites are often  feats or proficiency ranks. 16?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 442-464::/page/10/Text/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 442-464::/page/10/Text/4', 'PZO22001 Starfinder Player Core 442-464::/page/10/Text/42', 'PZO22001 Starfinder Player Core 442-464::/page/10/Text/8']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 442-464::/page/10/Text/4` | 1.008917 | **prerequisites** Many feats and other abilities can be taken  only if you meet their prerequisites. Prerequisites are often  feats or proficiency ranks. 16 |
| 2 | `PZO22001 Starfinder Player Core 442-464::/page/10/Text/42` | 0.792513 | **requirements** Some abilities can be used only if you meet  their requirements. 16 |
| 3 | `PZO22001 Starfinder Player Core 442-464::/page/10/Text/8` | 0.592756 | **proficiency** A measure of a character's aptitude at a specific  task or quality, with five ranks: untrained, trained, expert,  master, and legendary. Proficiency gives a proficiency  bonus. Being u |
| 4 | `PZO22001 Starfinder Player Core 442-464::/page/13/Text/37` | 0.549083 | **trained** (proficiency rank) Add your level + 2 to associated  rolls and DCs. Some skill actions and many other rules  require you to be trained. 8, 11, **392** |
| 5 | `PZO22001 Starfinder Player Core 442-464::/page/5/Text/13` | 0.548523 | **feat** An ability you gain or select for your character due to  their ancestry, background, class, general training, or skill  training. Some feats grant special actions. 10, 16 |
| 6 | `PZO22001 Starfinder Player Core 442-464::/page/5/Text/45` | 0.529653 | **frequency** An ability that can't be used at will might list a  frequency. 16 |
| 7 | `PZO22001 Starfinder Player Core 442-464::/page/5/Text/57` | 0.524006 | **general** (trait) A type of feat that any character can select,  regardless of ancestry and class, as long as they meet the  prerequisites. You can select a feat with this trait when  your class gra |
| 8 | `PZO22001 Starfinder Player Core 442-464::/page/2/Text/33` | 0.503644 | **class feature** Any ability granted by a class is a class feature.  These mainly consist of class feats and other abilities  specific to the class. 100 |
| 9 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/12` | 0.503563 | **Athletics** (skill) Perform deeds of physical prowess. (Str) 193–195 **attack** (trait) An ability with this trait involves an attack. For  each attack you make beyond the first on your turn, you  t |
| 10 | `PZO22001 Starfinder Player Core 442-464::/page/11/Text/35` | 0.494146 | **skill** (trait) A general feat with the skill trait improves your  skills and their actions or gives you new actions for a skill.  A feat with this trait can be selected when a class grants  a skill |

### Query 101
- Text: What does attacking with a spell 300, **394–395** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 442-464::/page/12/Text/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 442-464::/page/12/Text/4', 'PZO22001 Starfinder Player Core 442-464::/page/1/Text/18', 'PZO22001 Starfinder Player Core 442-464::/page/12/Text/56']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 442-464::/page/12/Text/4` | 0.957688 | attacking with a spell 300, **394–395** |
| 2 | `PZO22001 Starfinder Player Core 442-464::/page/1/Text/18` | 0.861493 | spell attack 394–395 |
| 3 | `PZO22001 Starfinder Player Core 442-464::/page/12/Text/56` | 0.755796 | attack rolls 394–395 |
| 4 | `PZO22001 Starfinder Player Core 442-464::/page/12/Text/18` | 0.682110 | spell attack modifier (spellcasting attribute modifier +  proficiency bonus + other bonuses + penalties) 394–395 |
| 5 | `PZO22001 Starfinder Player Core 442-464::/page/13/Text/23` | 0.619913 | spell targets 298, 300 |
| 6 | `PZO22001 Starfinder Player Core 442-464::/page/12/Text/30` | 0.598416 | **spell attack modifier** You attempt a spell attack roll when  targeting a creature with aimed magic. Your multiple  attack penalty applies. Spell attack modifier = spellcasting  attribute modifier + |
| 7 | `PZO22001 Starfinder Player Core 442-464::/page/7/Text/49` | 0.577704 | **line of effect** 300, **418–419** |
| 8 | `PZO22001 Starfinder Player Core 442-464::/page/8/Text/35` | 0.554257 | epiphany spells 116, **375–377** |
| 9 | `PZO22001 Starfinder Player Core 442-464::/page/12/Text/21` | 0.550057 | spell descriptions 313–387 |
| 10 | `PZO22001 Starfinder Player Core 442-464::/page/14/Text/44` | 0.548454 | warp spells 165, **377–380** |
