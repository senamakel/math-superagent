# Steiner chain — Wikipedia

[[research/sources/steiner-chain-wikipedia.full.md]] · source:
https://en.wikipedia.org/wiki/Steiner_chain

## What it establishes

A Steiner chain is a finite set of n circles each tangent to BOTH of two
non-intersecting given circles (an outer and an inner one). It is the exact
abstraction of the PE620 planet configuration: each planet is a circle tangent
independently to the outer ring C and the inner sun S.

Key results:

1. **Locus of centers.** When the smaller given circle lies *inside* the larger
   (our case: S inside C), the centers of all circles tangent to both lie on an
   **ellipse whose foci are the centers of the two given circles**. When the
   smaller circle is *outside* (disjoint), the locus is instead a hyperbola.
   — So PE620's planet-center locus is an ellipse with foci at C's center and
   S's center. This independently corroborates the Cut-the-Knot/AMM claim
   (`tangent_circle_center_ellipse`).

2. **Steiner's porism.** If one closed chain of n circles fits, infinitely many
   do (rotate the chain). Every circle tangent to both given circles belongs to
   some closed Steiner chain. This confirms there is a *continuous one-parameter
   family* of tangent positions; it is the discrete mesh condition that cuts it
   to a finite set in the gear problem.

3. Annular case: when the two given circles are concentric, the chain circles
   are equal and spaced by a uniform angular step 2π/n.

## Implication / gap

The continuous tangent circle centers form a 1-parameter family (the ellipse);
"which of these are meshing positions" is NOT decided by Steiner-chain theory —
that is answered by the least-mesh-angle (quantization) theorem from the gear
sources. The two facts compose: planet center = ellipse ∩ angular lattice
(multiples of β = 2π/(c+s)). This bibliography entry is the geometric half of
that composition.

## Cross-references

- Pappus chain (same library): explicit ellipse parametrization.
- Drivetrain/UTS/Handbook gear sources: least-mesh-angle quantization (the
  discrete half).
