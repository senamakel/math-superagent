# Szemerédi–Trotter theorem: the incidence bound under the unit-distance O(n^{4/3}) bound

**Subject:** The foundational combinatorial-geometry incidence bound that the
Spencer–Szemerédi–Trotter O(n^{4/3}) unit-distance bound is derived from. The
run holds the O(n^{4/3}) unit-distance claim; this is the theorem underneath
it, so its exact statement and hypotheses belong in the library.

**Source URL:** E. Szemerédi, W.T. Trotter, *Extremal problems in discrete
geometry*, Combinatorica 3 (1983) 381–392. Retrieved via search passages; the
canonical statement is corroborated by the Kaplan–Matoušek–Sharir survey
"Simple Proofs of Classical Theorems in Discrete Geometry via the Guth–Katz
Polynomial Partitioning Technique" (arXiv:1102.5391) and the Guth–Silier
"Sharp Szemerédi–Trotter Constructions in the Plane" (Electron. J. Combin.
32(1), 2025, #P1.9, DOI 10.37236/10899).

## Exact statement

Let `P` be a set of `m` distinct points and `L` a set of `n` distinct lines in
the plane `R^2`. Let `I(P, L)` be the number of *incidences* — pairs `(p, l)`
with `p in P`, `l in L`, and `p` lying on `l`. Then

    I(P, L) = O( m^{2/3} n^{2/3} + m + n ).

**Equivalent r-rich formulation.** For a set `P` of `n` points, let `L_r` be the
set of lines containing at least `r` points of `P`. Then

    |L_r| = O( n^2 r^{-3} + n r^{-1} ).

The symmetric case m = n = N gives `I = O(N^{4/3})`, which is the exact shape
of the unit-distance bound.

## Why this matters

The unit-distance bound `u_2(n) = O(n^{4/3})` (Spencer–Szemerédi–Trotter 1984)
is obtained by reducing unit distances to incidences between points and unit
circles and bounding those via the Szemerédi–Trotter machinery. So the
O(n^{4/3}) density ceiling the run relies on ("density cannot be bought"; rigid
high-chromatic graphs must come from algebraic coincidence) ultimately rests on
this theorem. It is a control on how many unit distances a plane point set can
have, and a tight bound at that — lattice/cell-decomposition constructions
achieve the exponent (Erdős's `[sqrt n] x [sqrt n]` grid construction gives
Omega(n^{1+c/log log n}) unit distances; the Katz–Silier structural analysis
gives a parameterised recipe for extremal configurations).

## Basis and status

- Statement and hypotheses corroborated across the search-returned sources
  (original 1983 paper record, two independent surveys/constructions). Standard,
  accepted theorem; not re-derived here.
- Not the published answer to `problem.md`: it bounds incidence *counts*, not
  chromatic numbers.

## Claim block

```claim
id: szemeredi-trotter-incidence
statement: For m points and n lines in the plane, I(P,L) = O(m^{2/3} n^{2/3} + m + n);
  equivalently the number of r-rich lines through n points is O(n^2 r^{-3} + n r^{-1}).
hypotheses: P finite point set, L finite line set, both in R^2, ordinary
  Euclidean geometry.
holds-here: YES — it is the upper-bound machinery under the O(n^{4/3})
  unit-distance bound, i.e. under the claim "density cannot be bought", which
  the run uses to steer construction toward algebraic structure.
status: asserted-by-source (Szemerédi–Trotter 1983; corroborated by two surveys).
bearing: the exact control that limits how dense a unit-distance graph can be;
  tells the search rigidity must come from algebraic coincidence, not from
  packing many unit distances randomly.
anchor: research/sources/szemeredi-trotter-incidence-theorem.md
falsifies: a plane point/line configuration violating the incidence bound —
  none known; the theorem is classical and accepted.
```
