# Epicyclic Gearing — Wikipedia (encyclopedic tier)

[[research/sources/epicyclic-gearing-wikipedia.full.md]] · source:
https://en.wikipedia.org/wiki/Epicyclic_gearing

## What it establishes

Fixes the standard terminology and kinematic equations for epicyclic (planetary) gear
trains:

- Structure: sun gear (central), planets in a carrier, ring (annulus). Pitch circles
  roll without slip. A planet meshes with both sun and ring.
- **Fixed-carrier train ratio**: with the carrier held fixed the train acts as an
  idler gear train; the sun-to-ring speed ratio is
  `ω_r/ω_s = −N_s/N_r` (sign from the internal-ring convention), i.e.
  `ω_s·N_s = −ω_r·N_r` (eq. in "Gear speed ratios" / "Fixed carrier train ratio").
- **Gear-speed ratios**: for a conventional epicyclic set with carrier speed n_c,
  sun speed n_s, ring speed n_r: `n_c = (n_r·N_r + n_s·N_s)/(N_r + N_s)` — the
  **sum `N_r + N_s` appears as the denominator of the carrier speed formula**, the
  same sum that appears in the planet-position quantization step 2π/(N_r+N_s).
- Torque ratios and accelerations: static torque balance; input/output/reaction
  element conventions.
- Non-interference: planets' outer diameters and adjacent spacing constraints.

## Implication for PE620

- The ring is an *internal* gear: its tooth count contributes positively to the
  carrier speed denominator, consistent with the least-mesh-angle step
  2π/(Z_ring + Z_sun) (ring teeth count positively, sun teeth positively).
- PE620's condition "perfectly meshing = constant angular-velocity ratio + teeth
  align with grooves" is exactly the rolling-without-slip of pitch circles in this
  entry plus the tooth-perfect alignment that the assembly condition
  (Guo 5.21) converts to quantization.
- The `(N_r + N_s)` denominator is a second, independent place (besides Guo's
  assembly-condition derivation) where the run's magic sum appears in the standard
  kinematic equations.

```claim
id: wiktionary_epicyclic_carrier_speed_denominator
statement: In a conventional epicyclic gear set the carrier speed is
  n_c = (n_r*N_r + n_s*N_s)/(N_r + N_s); the sum of ring and sun tooth counts is the
  denominator of the carrier-speed formula. Ring (internal) tooth count enters
  positively, sun positively.
hypotheses: conventional epicyclic set; rolling without slip; internal ring gear.
holds-here: true — PE620's C (ring, c teeth) and S (sun, s teeth); the same
  denominator c+s appears in the planet-position quantization 2*pi/(c+s).
status: sourced (Wikipedia "Epicyclic gearing", encyclopedic tier; consistent with
  tec-science Willis equation and MIT OCW 2.000 notes).
bearing: fixes terminology; corroborates that the sum c+s is the system's fundamental
  tooth-count scale.
anchor: research/sources/epicyclic-gearing-wikipedia.full.md
```