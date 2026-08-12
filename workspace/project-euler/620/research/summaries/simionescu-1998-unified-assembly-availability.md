# Simionescu — Unified Approach to the Assembly Condition of Epicyclic Gears (1998) — abstract + availability record

[[research/sources/simionescu-publications-page.full.md]] · original:
P. A. Simionescu, "A Unified Approach to the Assembly Condition of Epicyclic Gears",
ASME Journal of Mechanical Design, 120(3):448-452, 1998, DOI 10.1115/1.2829172.

## Accessibility status (recorded as of this run)

**Full text not in the library.** ASME paywall; academia.edu page returned HTTP 403
to the downloader. No repository copy surfaced in searches (no CiteSeerX, no
institutional PDF). The publication-list page (Simionescu, TAMUCC) confirms the exact
citation but hosts no PDF. **Do not retry** the academia.edu route; a copy would have
to come from ASME or document delivery.

## What the search result established (verbatim abstract, provenance = exa search)

> A general method for determining the assembly condition of epicyclic gear trains,
> irrespective of the structure or gear type, is presented. An associated mechanism
> is considered, having a single arm carrier and a split planet. The assembly
> condition of the gear train is satisfied when obtaining identical superposition of
> the teeth of the two half-planets after rotating the arm to the next position. By
> writing simple kinematic relations between some partial transmitting ratios,
> general formulae are obtained which can be applied to specific epicyclic gear sets
> as functions of teeth numbers. The same approach allows the determination of the
> necessary angles between the arms of the carrier, or the offset angles between the
> wheels of the compound planets, as alternative solutions for the case in which
> equidistant assembly of identical planets is not possible.

## Implication for PE620

The split-planet/superposition method is the *derivation-level* source that the
coaxial least-mesh-angle rule (Guo 5.21) rests on: the arm rotates by the inter-planet
angle and the teeth of the two half-planets must superpose identically, which gives
the 2π/(Z_ring+Z_sun) step. But — like every coaxial treatment — it assumes a *shared
carrier* and identical/equidistant planets; PE620's planets are free-standing and
unconstrained in angle, so the unified condition is the coaxial baseline the off-centre
W-model must reduce to, not the off-centre count itself. The abstract confirms the
method's generality within coaxial epicyclics (unequal spacings handled via
carrier-arm/offset angles) but says nothing about an off-centre sun; the off-centre
case is covered by Kurasov 2020 (now full text on disk).

## Cross-references

- Guo 2011 eq. (5.21)-(5.25): the same assembly condition derived in thesis form,
  on disk.
- Kurasov 2020 (full text on disk): the off-centre (eccentric) analogue.
- Zou 2015, Sun 2017, UTS 1162/1165: the coaxial tooth-count-matching rules that
  descend from this unified method.