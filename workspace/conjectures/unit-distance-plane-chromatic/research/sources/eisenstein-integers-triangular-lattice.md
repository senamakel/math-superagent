# Coordinate fields: Eisenstein integers and the triangular lattice

**Subject:** The algebraic number field the run's exact coordinates are most
likely to live in. Task lead in `problem.md` (point sets with algebraic
structure / rings of integers).

## Source
- C. Aebi, G. Cairns, *Following in Yiu's Footsteps but on the Eisenstein
  Lattice*, arXiv:2309.13551 (2023). Surfaced via server-side search; direct
  arXiv download is blocked at the network boundary, so this record is a
  synthesis of the search passage.

## What it establishes (as derived from the passage)
- The **Eisenstein integers** are `Z[omega]` with `omega = e^{2 pi i / 3} =
  (-1 + i sqrt(3))/2`, a primitive cube root of unity.
- An Eisenstein integer `z = x + y omega` (x, y integers) — equivalently
  `a + b sqrt(-3)` up to the standard basis — has norm
  `N(z) = z z* = x^2 - xy + y^2`.
- `Z[omega]` is a Euclidean domain hence a PID, with unique factorization and
  six units {±1, ±omega, ±(1+omega)}.
- A rational prime `p` is a `Z[omega]`-prime iff `p ≡ 2 (mod 3)`. The primes
  are the rational primes `p ≡ 2 (mod 3)` and the Eisenstein primes whose norm
  is a rational prime.
- The geometry: `Z[omega]` sits on the **triangular lattice** (hexagonal
  lattice). The unit vectors of this lattice are `1, omega, omega^2, ...`,
  each of modulus 1, so the six directions `{1, omega, omega^2, omega^3,
  omega^4, omega^5}` (powers of a primitive 6th root of unity, or ±1 and
  rotations by 60°) connect lattice points at exactly distance 1. This makes
  the triangular lattice and its finite subsets the natural source of
  unit-distance graphs with abundant unit distances.

## Relevance
- `problem.md` and the standard construction tier both use rotations by pi/3
  (60°) — precisely the symmetries of the Eisenstein lattice. Rotating by 60°
  maps the lattice to itself, and the 7-vertex rhombus construction in
  `problem.md` uses unit (equilateral) rhombi, i.e. points on this lattice.
- Coordinates in `Q(sqrt(-3))` (or `Q(sqrt(3))`) with exact arithmetic give
  the field the oracle's edge-certifier should support first.

## Claim block
```claim
id: einstein-lattice-unit-distance
statement: The Eisenstein integers Z[omega], omega = e^{2 pi i /3}, form the
  triangular lattice; its unit vectors are the six powers of a primitive 6th
  root of unity, all of modulus 1, so adjacent lattice points differ by a unit
  vector and lie at Euclidean distance 1 exactly.
hypotheses: the standard embedding of Z[omega] in C with norm |z|.
holds-here: YES — gives exact coordinates in Q(sqrt(-3)) whose pairwise
  distances are exactly 1 whenever the difference is a unit vector, and
  graph edges are then provable symbolically (x^2 - xy + y^2 = 1 arithmetic).
status: asserted-by-source (standard, classical fact about the Eisenstein
  lattice; the Aebi–Cairns paper states the ring/norm/factorization facts).
bearing: the first coordinate field for exact-arithmetic construction; the
  60-degree rotations of the construction machinery are this lattice's
  symmetries.
anchor: research/sources/eisenstein-integers-triangular-lattice.md
falsifies: a correct claim that unit vectors of Z[omega] have modulus != 1 —
  would contradict the norm N(z) = |z|^2 = 1 for x^2-xy+y^2 = 1 (e.g. x=1,y=0).
```
