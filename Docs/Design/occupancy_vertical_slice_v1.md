# Occupancy Vertical Slice v1 — sourced 2024 rule

**Status:** Active correction to `occupancy_vertical_slice_v0.md` for RLH-02 onward.
**Ruleset ID:** `dnd5e_2024_occupancy_v1`.
**Source:** [D&D SRD 5.2.1, Moving around Other Creatures, printed page 14](https://media.dndbeyond.com/compendium-images/srd/5.2/SRD_CC_v5.2.1.pdf), also published in the [official 2024 Basic Rules](https://www.dndbeyond.com/sources/dnd/br-2024/playing-the-game).

The source rule prohibits a creature from willingly ending a move in another creature's space. It separately says a creature that somehow ends a turn sharing a space becomes Prone unless the creature is Tiny or larger than the other creature. Passing through an ally's space is allowed during movement; it does not create an end-of-move exception. The source does not grant an exception for a prone ally.

## Grounding questions

1. `ground_occ_2024_001`: What source text prohibits willingly ending a move in another creature's space?
2. `ground_occ_2024_002`: What source text describes the Prone consequence if a turn somehow ends in a shared space, and its size exclusions?

The two questions may resolve to the same EvidenceUnit. That unit must preserve the source document, printed page, section heading, page fingerprint, exact text, and Stage B identity. A model-generated statement is never a substitute for that unit.

## Human gold for the semantic pilot

| Claim | Human disposition | Source relationship |
| --- | --- | --- |
| Voluntarily ending a move in another creature's space is prohibited. | accept | Direct default restriction. |
| If a turn somehow ends in a shared space, the actor becomes Prone unless Tiny or larger than the other creature. | accept | Separate consequence with explicit exclusions. |
| A prone ally permits voluntarily ending a move in the ally's space. | reject | Contradicts the unrestricted prohibition; no such exception appears in the cited section. |

The pilot may propose other candidates, but each accepted candidate needs an exact EvidenceUnit reference. Ambiguous candidates stay review or unresolved. The human decisions above are the frozen comparison target for RLH-02.

## Runtime scope for later slices

The first deterministic evaluator only needs to decide voluntary end-of-move placement for ordinary creatures:

- occupied target space: reject, regardless of alliance or the occupant's Prone state;
- unoccupied target space: accept, subject to other rules outside this slice.

The shared-space end-of-turn Prone consequence is a separate rule path and is not an override of voluntary placement. Tiny and relative-size exclusions apply to that consequence, not to the default end-of-move prohibition. RLH-09 through RLH-11 must not encode an ally-prone placement allowance.

## Source and scope limits

The checked-in fixture for RLH-02 is a minimal Stage B unit generated from a faithful structural transcript of the public SRD page. It is an SRD evidence fixture, not a claim that a 2024 PHB ingestion run exists. Any later PHB-specific publication or artifact must first obtain and verify PHB EvidenceUnits. The v0 design's ally-prone branch, related accept fixture, and PHB provenance assumptions are superseded by this correction.
