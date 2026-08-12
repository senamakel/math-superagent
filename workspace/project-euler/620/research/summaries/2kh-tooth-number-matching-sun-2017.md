# Tooth Number Matching and Its Software Development for 2KH Planetary Gear Mechanism — Sun et al., MME 2016 (Atlantis Press)

[[research/sources/2kh-tooth-number-matching-sun-2017.full.md]] · source:
https://www.atlantis-press.com/article/25871492.pdf

## What it establishes

A primary, openly-licensed derivation of the four restrictive conditions for tooth
number matching in 2K-H planetary gear mechanisms (four types: NGW, WW, NW, NN;
N = internal gear, W = external gear, G = compound):

- **Transmission ratio condition**: Z_a, Z_b ratio fixed by the required ratio
  (from `i = 1 − Z_b/Z_a` for NGW-type; `±` variant for dual-gear types).
- **Concentricity condition**: the two meshing centre distances are equal; for
  X-zero gears this reduces to `2·Z_g = Z_b − Z_a` (single-pin NGW case) — the
  pitch-radius relation.
- **Condition for Fitting** (the assembly condition — the paper's own term):
  - *Dual-gear (2KH-NW/WW/NN) case*: `(Z_a ± Z_f ∓ Z_g − Z_b)/q = n` an integer
    (the ± signs encode the internal/external mesh signs), where Z_f, Z_g are the
    two planet-gear tooth counts divided by their common divisor m.
  - *Single-pin (2KH-NGW) case (Z_f = Z_g)**: `(Z_a + Z_b)/q = n` — an integer —
    "the condition for fitting" (their eq. 3-7). Here Z_a is the sun (or a-ring)
    tooth count, Z_b the other central gear, q the number of planets.
  - This is exactly the equal-spacing homogeneity condition: evenly distributing
    q planets requires (Z_sun + Z_ring)/q ∈ ℤ.
- **Adjacency condition**: centre distance of neighbouring planets > planet tip
  diameter (L > d_ag) — the collision-avoidance bound (PE620 *permits* planet
  overlap, so this is explicitly relaxed in the problem).
- Implements tooth-matching in VC2008 software; worked NGW example: ratio 4.55,
  q=4 planets, Z_b=78 (ring), planet 28, Z_a=22 (sun) — 22+78=100 = 4·25 ✓.

## Implication for PE620

Fourth independent derivation-level confirmation of the assembly condition:
`(Z_sun + Z_ring)/n_planets ∈ ℤ` for equal spacing. Consistent with Guo
eq. (5.21) (positions at multiples of 2π/(Z_r+Z_s), of which equal spacing is the
n-planet-restricted case) and with Zou 2015's homogeneity condition. The adjacency
condition is explicitly *not* applied by PE620 (planets may overlap).

```claim
id: fitting_condition_2kh_sun2017
statement: For a single-pin 2KH-NGW planetary gear train the condition for fitting
  (evenly placing q planets between the two central gears) is (Z_a + Z_b)/q = n with
  n integer, where Z_a and Z_b are the central gear tooth counts; concentricity for
  X-zero gears is 2*Z_g = Z_b - Z_a. For dual-gear (NW/WW/NN) types the fitting
  condition generalizes to (Z_a ± Z_f ∓ Z_g - Z_b)/q = n.
hypotheses: 2K-H planetary gear mechanism; equal spacing; ideal (X-zero) geometry;
  integer tooth counts.
holds-here: true-directly — PE620's S (s teeth) and C (c teeth) are the two central
  gears; equal spacing is the sub-case of the general quantization 2*pi/(c+s) from
  Guo (5.21) where several planets coincide in phase. PE620 relaxes the adjacency
  condition (planets may overlap).
status: sourced (Sun et al., MME 2016, Atlantis Press, open access CC BY-NC).
bearing: independent derivation-level corroboration of the (Z_sun+Z_ring) divisibility
  condition; part of the four-condition teeth-matching toolkit (ratio, concentricity,
  fitting, adjacency).
anchor: research/sources/2kh-tooth-number-matching-sun-2017.full.md
```