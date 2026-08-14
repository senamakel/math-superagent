# Backward: proving chi(G) <= 6

The upper-bound direction of the plane-colouring conjecture. A genuine
6-colouring of the plane is a construction, not a finite object, so the gaps
here are about a region family and an exact margin computation.

```skeleton
goal: chi(G) <= 6, where G is the unit-distance graph on R^2.
implies: >
  By definition chi(G) <= 6 iff there is a proper 6-colouring of R^2, i.e. a
  cover of the plane by six colour classes C_1,...,C_6 with no two points of a
  single class at distance exactly 1. U6-region-design supplies a region family
  (tiling) and a colour assignment; U6-covering proves the regions cover R^2
  and that boundary ties are broken consistently, so six well-defined classes
  C_i arise; U6-margin proves inf_{i} inf_{x,y in C_i} |x-y| > 1 (strictly,
  computed exactly — the forbidden distance is exactly 1, so a margin of exactly
  1 does not suffice). Then each C_i is unit-distance-free and the six classes
  cover the plane, giving a proper 6-colouring, so chi(G) <= 6.
status: sketched
rests-on: none
```

```gap
id: U6-region-design
lemma: >
  There is a family of plane regions and a 6-colour assignment of them such that
  any two points in regions of the same colour are at distance > 1 apart. (The
  known hexagonal tiling needs 7 colours, so the design must genuinely break
  that barrier.)
status: open
next: >
  inventor + symbolic_math: parameterise the hexagonal tiling (side length
  slightly below 1) and prove its exact 7-colour margin first, as the baseline
  the 6-colour design must beat; then propose a candidate region family (tiling
  with fewer colours, e.g. a different tile shape) as a symbolic parameter
  search.
```

```gap
id: U6-covering
lemma: >
  The region family of U6-region-design covers the plane, and the boundary
  tie-break is consistent (each point assigned exactly one colour class).
status: open
next: >
  tool_builder: for a given candidate region family, verify covering and
  consistency — express each tile as a finite set of linear/polynomial
  inequalities and check the union covers R^2 and the tie-break is a partition.
```

```gap
id: U6-margin
lemma: >
  For the colour classes of U6-region-design + U6-covering, the exact minimum
  distance between two points in the same class is > 1.
status: open
next: >
  symbolic_math: compute min_{same-colour region pair} inf |x-y| exactly as a
  constrained optimisation over the region polytopes (LP/SDP with exact
  coefficients), and certify the result is strictly greater than 1.
```
