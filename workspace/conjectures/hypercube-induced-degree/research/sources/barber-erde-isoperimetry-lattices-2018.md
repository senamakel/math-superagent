# Barber–Erde, "Isoperimetry in integer lattices" (Discrete Analysis, 2018)

Source URL: https://doi.org/10.19086/da.3555
(Retrieved via `read_sources`; direct download blocked by network boundary.)

## What this source establishes (survey)

For the d-dimensional hypercube Q_d = {0,1}^d (edges between Hamming-distance-1
strings):

- **Edge isoperimetric problem:** the minimum edge boundary for a set of given
  size is achieved by k-dimensional subcubes (fix d−k coordinates). Attributed
  to Harper, Lindsey, Bernstein, Hart.
- **Vertex isoperimetric problem:** the minimum vertex boundary is achieved by
  Hamming balls {strings with at most w ones}. Attributed to Harper.
- General inequality: ∂_v(S) ≤ ... boundary controlled by volume profile; for
  large S the min boundaries scale like the d-dimensional isoperimetric profile
  d·vol^(1−1/d).
- Covers (Z^d, l1) and ([k]^d, l1), Bollobás–Leader phase transitions, and
  Loomis–Whitney asymptotics.

## Why it is here

A concise survey mapping the named results (Harper, Lindsey, Bernstein, Hart,
Bollobás–Leader, Loomis–Whitney) for the cube, confirming that the classical
theory optimises *boundary* (outer) quantities, the opposite direction from the
max internal degree D(S). It is the map for chasing primary sources.

## Claim block

```claim
id: survey-cube-isoperimetric-profile
statement: On the hypercube, min edge boundary for fixed size is given by
  subcubes and min vertex boundary by Hamming balls (Harper/Lindsey/Bernstein/
  Hart); these optimise outer boundary, not internal max degree (survey).
hypotheses: Q_d, fixed set size.
holds-here: yes as a survey statement of the boundary theory; confirms the
  obstruction that isoperimetric profiles are outer-boundary tools.
status: asserted-by-source (survey).
bearing: names the canonical techniques and their extremal shapes; none of which
  directly bounds D(S).
anchor: barber-erde-2018
```
