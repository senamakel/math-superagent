# Wikipedia — Triangular lattice (hexagonal lattice)

<!-- source: https://en.wikipedia.org/wiki/Triangular_lattice -->

## What this entry fixes

The problem's "triangular lattice" (also called the **hexagonal lattice**) is one of
the five 2-dimensional Bravais lattices, with wallpaper-group symmetry p6m. Its
primitive translation vectors have equal length a and meet at 120°:

    |a1| = |a2| = a,  angle(a1, a2) = 120°.

This is exactly the lattice the PE 351 orchard is drawn on: the regular hexagon of
side n is the hexagon of this lattice, and the orchard's points are its lattice
points, 3n² + 3n + 1 of them (OEIS A003215, centered hexagonal numbers — the crystal
ball sequence for this lattice).

## Why the axial-coordinate model is sound

The run models the orchard as {(a,b) ∈ ℤ² : |a| ≤ n, |b| ≤ n, |a+b| ≤ n} in axial
coordinates. This is a faithful coordinate system for the triangular lattice: the
triangular lattice is the set of integer combinations of the two primitive vectors,
which is ℤ² under the (a,b) → a·e1 + b·e2 identification. The hexagon {|a|,|b|,|a+b| ≤ n}
is the order-n hexagon of that lattice, and the six neighbours of each point (the
degree-6 coordination) are the p6m signature. So:

- the point count 3n² + 3n + 1 is the centered hexagonal number A003215(n) = 3n(n+1)+1
  (crystal ball sequence for the A2 / hexagonal lattice), and
- visibility from the centre is governed by gcd(|a|,|b|) — the rank-2 lattice
  primitive-point criterion, since the axial coordinates form an integral basis.

## Claim for the ledger

```claim
id: orchard-lattice-triangular
statement: The hexagonal orchard of order n is the order-n hexagon of the triangular
(hexagonal) lattice, the 2D Bravais lattice with equal primitive vectors at 120° and
wallpaper group p6m. Its n-th point count is the centered hexagonal number
3n(n+1)+1 = 3n^2 + 3n + 1 (OEIS A003215), the crystal ball sequence of this lattice.
hypotheses: n >= 0; the orchard is the regular hexagon of side n on the triangular
lattice.
holds-here: yes — problem.md's "triangular lattice ... regular hexagon with side n";
code/brute.py asserts the count 3n^2+3n+1 on every run.
status: sourced (Wikipedia: Triangular lattice; OEIS A003215).
bearing: fixes the geometry: the axial-coordinate model {(a,b): |a|<=n, |b|<=n,
|a+b|<=n} is an integral basis for the lattice, so the gcd criterion applies and the
total point count is exact.
anchor: research/summaries/wikipedia-triangular-lattice.md
```
