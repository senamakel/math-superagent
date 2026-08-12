<!-- source: https://www.zhygear.com/meshing-phase-calculation-of-spur-planetary-gear/ | converted from HTML -->

# Meshing phase calculation of spur planetary gears — ZHY Gear

## What the source says

For a planetary gear train (sun S, planets n = 1..N, internal ring R; planets evenly
spaced on the carrier at angles ψ_n), the meshing phases of the nth sun–planet and
planet–ring pairs are related to the planet position angle ψ_n and the tooth counts.

Key statements (as rendered from the page):

- γ_Sn = meshing phase between the sun gear and the nth planet; γ_Rn = meshing phase
  between the internal ring and the nth planet; ψ_n = circumferential angle of the nth
  planet relative to planet 1. Sign convention: "+" when the carrier rotates
  anticlockwise, "−" when clockwise.
- With three planets 120° apart, taking planet 1 as reference: ψ_1 = 0, ψ_2 = 2π/3,
  ψ_3 = 4π/3, and (carrier anticlockwise) γ_S1 = γ_R1 = 0, γ_S2 = γ_R2 = Z_r/3,
  γ_S3 = γ_R3 = 2Z_r/3 — i.e. the advance per planet equals the ring tooth count times
  the inter-planet angle in revolutions. (This is the same content as the
  least-mesh-angle / assembly-discreteness rule: each planet's phases advance by
  Z_r/N, taking planet 1 as reference: φ = 2π/N·something.)
- **Parity rule (the run's most relevant takeaway):** γ_SR, the phase difference
  between the nth sun–planet pair and the nth planet–ring pair (same planet), is
  *0 when the planet tooth count is even and 1/2 (one half of a mesh period) when
  the planet tooth count is odd.* This is exactly the quantity the run's surviving
  residue variant (σ = −1, η = −1, Q = 1/4 and 3/4) was trying to pin down for a
  *single* planet meshing both gears; this source states it directly for a standard
  train.
- TM = meshing period; inner and outer meshing pairs share the same meshing period.

## Bearing on PE620

The g(16,5,5,6) example has planets with tooth counts 5 (odd) and 6 (even). If the
same planet meshes the sun and the internal ring, its two mesh phases differ by
half a mesh period exactly when the planet tooth count is odd. Any per-planet
discreteness model that ignores this sun–ring phase mismatch (e.g. forcing both
phases to vanish together) will miscount; the parity rule is the correct constraint
linking the sun-mesh phase and the ring-mesh phase of one planet. The phase
difference does NOT depend on either central gear's tooth count parity.

## Status

Original page is a vendor (manufacturer) engineering explainer, not peer-reviewed;
but the γ_SR parity rule is corroborated structurally by the mesh-phasing sources in
the library (Guo 2011; ISMA 2016 Shweiki; Parker–Lin 2004 — same mesh-phase
framework, γ_rn = γ_sn for identical planets at the assembly positions, with the
Z_r-dependent offsets). Status: asserted (source), holds-here applied by the run in
the off-centre W-invariant residue variants.

```claim
id: planet_parity_sun_ring_phase_zhy
statement: For one planet meshing both the sun and the internal ring of a planetary
stage, the mesh-phase difference between its sun-mesh and its ring-mesh (the phase of
the sun-tooth alignment relative to the ring-tooth alignment, measured on the same
planet) is 0 when the planet tooth count is even and 1/2 of a mesh period when the
planet tooth count is odd. It does not depend on the sun's or the ring's tooth-count
parity.
hypotheses: standard single-pin planetary stage; X-zero spur gears; the two central
gears are the only meshing partners of the planet.
holds-here: yes — every PE620 planet meshes exactly the sun and the internal ring,
and the example g(16,5,5,6) has one odd (5) and one even (6) planet pair.
status: asserted (sourced; corroborated in structure by Guo 2011, ISMA 2016,
Parker–Lin 2004 mesh-phase formalism)
bearing: fixes the relative phase of the two mesh congruences on a single planet,
which is the piece the off-centre W-invariant residue variants (sigma=-1, eta=-1,
Q=1/4, 3/4) were exploring; a model that satisfies only the sun-mesh congruences and
ignores the ring-mesh phase offset is wrong.
anchor: research/sources/epicyclic-gearing-wikipedia.full.md
```