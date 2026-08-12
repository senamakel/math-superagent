# Single Planetary Mechanism Teeth Matching Conditions — Zou, Wei, Chang, Zhou (ICAMIA 2015, Atlantis Press)

[[research/sources/single-planetary-teeth-matching-zou-2015.full.md]] · source:
https://www.atlantis-press.com/article/25846284.pdf

## What it establishes

Four teeth-matching conditions for single-pin planetary mechanisms (2K-H: sun gear +
ring gear + planet carrier), derived from first principles:

- **Concentric condition**: 2·Z_g = Z_R − Z_S (X-zero gears). The centre distances of
  the sun–planet and planet–ring meshes must be equal — this is the pitch-radius
  relation; note PE620 fixes `c = s + p + q` (ring circumference = sun + planet
  circumferences) as the tangency condition instead.
- **Homogeneity distribution condition — derived from a phase-alignment argument**:
  evenly distribute n_b planets at spacing α_H = 2π/n_b; fix the ring, rotate the
  carrier by α_H and require the sun to end up an integer number of teeth from where
  it started; substituting the sun's rotation into the kinematic equation yields
  **`(Z_R + Z_S) / n_b = N`, N integer** (eq. 4: "the sum of ring gear and sun gear
  teeth must be an integral multiple of number of planetary gears").
- **Neighbour condition**: centre distance of neighbouring planets ≥ tip diameter
  (interference bound).
- **Gear ratio condition**: actual vs theoretical ratio within tolerance.

- Dual-pin case: homogeneity condition is `(Z_R − Z_S)/n_b = N` (sign flips because
  the second mesh reverses the phase accumulation) — consistent with Guo eq. (5.25)
  where d_i = 2 gives denominator Z_R − Z_S.

## Implication for PE620

This is the *derivation-level* source for the equal-spacing assembly condition and its
underlying phase-alignment mechanism (fix one member, rotate the carrier, the other
member must advance an integer number of teeth). It corroborates Guo eq. (5.21) —
which extends the same idea to arbitrary (not just equal) spacing: planets lie at
multiples of 2π/(Z_R+Z_S). The mismatch between the pe620 layout (off-centre S, planets
not on a rigid carrier) and the design-guide statements is resolved exactly as in the
`assembly_condition_simple_planetary_guo` claim: each planet is its own d_i = 1 train.

```claim
id: homogeneity_condition_zou
statement: For evenly spaced identical planets in a single-pin planetary mechanism,
  the assembly condition is (Z_R + Z_S)/n_b = N with N integer; it is derived by
  fixing the ring gear, rotating the carrier by the inter-planet angle alpha_H =
  2*pi/n_b, and requiring the sun gear to have advanced by an integer number of teeth.
hypotheses: X-zero (unmodified) gears; ideal geometry; equally spaced identical planets.
holds-here: partially — equal spacing is the special case of PE620 where two or more
  planets coincide in allowable phase; the general (unequal) step is 2*pi/(Z_R+Z_S)
  from Guo (5.21), of which this is the n_b-fold-restricted version.
status: sourced (Zou et al. 2015, ICAMIA 2015, Atlantis Press, open access).
bearing: corroborates the discreteness theorem at derivation level and gives a worked
  phase-alignment argument; supports the pattern that the least-mesh-angle rule is
  derived, not asserted.
anchor: research/sources/single-planetary-teeth-matching-zou-2015.full.md
```