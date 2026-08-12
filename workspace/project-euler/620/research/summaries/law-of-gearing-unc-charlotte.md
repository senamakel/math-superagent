# Law of Gearing — UNC Charlotte ISL

[[research/sources/law-of-gearing-unc-charlotte.md]] · source:
https://isl.charlotte.edu/law-of-gearing/

## What it establishes

Complete statement of the **law of gearing** (condition for constant velocity
ratio of toothed wheels):

For two meshing gears with fixed centers O₁, O₂ and teeth in contact at Q, the
common normal to the tooth profiles at Q must **always pass through the fixed
pitch point P** on the line of centers. Proof sketch: the velocity components
along the common normal must be equal for the teeth to stay in contact
(v₁cosθ₁ = v₂cosθ₂); from similar triangles O₁MP, O₂NP, ω₁/ω₂ = O₂P/O₁P, so a
constant ratio requires P fixed. Then:
- Angular velocity ratio is inversely proportional to the ratio of distances
  from P to the two centers: ω₂/ω₁ = O₁P/O₂P.
- Involute tooth profiles satisfy the law (their base/root circles are tangent
  to the common normal).
- Conjugate teeth: if one profile is chosen arbitrarily, the other is its
  conjugate; not commonly manufactured.
- Sliding velocity between teeth is proportional to distance of contact point
  from the pitch point: v_s = ω_rel · QP.

## Implication for PE620

This is the *first-principles justification* of the problem's "perfectly
meshing = constant angular-velocity ratio": gear teeth must be conjugate
(involute in practice) so the common normal at contact always passes through
the pitch point. The pitch circles (radii R₁, R₂ with ω₁R₁ = ω₂R₂ at the pitch
point) are the circles that roll without slipping — exactly the circles of
circumference c, s, p, q (1 cm pitch) used in the problem. The constant angular
velocity ratio among C, S, planets follows.

## Cross-references

- DANotes (UWA) involute conjugacy summary: the involute profile construction
  and why it guarantees the law.
- Willis equation summary: ratios in the 3-member (sun–planet–ring) train.
- code/lib/gears.py: the 8 phase-alignment equations implementing meshing.