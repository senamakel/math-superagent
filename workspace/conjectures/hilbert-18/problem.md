# Hilbert's 18th problem — tilings, and the open combinatorics under it

## The three questions Hilbert asked

1. Are there, in each dimension `n`, only finitely many crystallographic groups
   of motions? **Yes** — Bieberbach (1910).
2. Is there a polyhedron tiling `R³` that is **not** the fundamental domain of
   any group of motions? **Yes** — Reinhardt (1928), and Heesch (1935) in the
   plane. Such a tile is *anisohedral*.
3. What is the densest packing of congruent spheres? **Kepler's conjecture** for
   `R³` — Hales (1998/2017, with a formal proof in HOL Light and Isabelle);
   dimensions 8 and 24 settled by Viazovska and by Cohn–Kumar–Miller–Radchenko–
   Viazovska (2016).

All three are answered as asked. The **open combinatorial descendants** of
question 2 are this workspace's target, because they are finite, decidable
case by case, and every answer is a certificate a machine can check.

## The target: Heesch numbers and isohedral numbers

For a shape `T` that does **not** tile the plane, the **Heesch number** `H(T)`
is the largest `k` such that `T` admits `k` "coronas": a patch of copies of `T`
surrounding a central copy, then a second layer surrounding that, and so on `k`
times, with no gaps or overlaps. A tile that tiles the plane has `H = ∞`.

> **(H18.H)** Which values does the Heesch number take? Is it unbounded on
> shapes that do not tile the plane?

Recalled status — **to be confirmed or struck against sources**: examples are
known with Heesch number up to 5 or 6 (Bašić's example raising the record is the
most recent one to check), and it is **unknown whether the Heesch number is
bounded**. If it were bounded by a computable `k`, the plane-tiling problem for a
single shape would be decidable — and that decidability is itself open, so this
is not a curiosity but the crux.

Alongside it:

> **(H18.I)** For every `k`, is there a tile whose **isohedral number** is
> exactly `k` — a tile that tiles the plane, but only with `k` orbits of tiles
> under the symmetry group of the tiling?

Recalled: examples are known for small `k` and the general question of which `k`
occur is open. Both questions are about finite patches of finitely many copies
of one polygon, which makes them SAT- and CP-shaped: a corona either exists or
does not, and UNSAT on the encoding is a theorem.

Also in scope, and adjacent:

- **Decidability of the single-tile plane-tiling problem** (the *einstein* /
  domino-problem circle). The aperiodic monotile ("hat", 2023) settled the
  existence of an aperiodic single tile; decidability of whether a given
  polyomino tiles the plane remains open in general.
- **Densest packings** in dimensions other than 1, 2, 3, 8, 24 — open, with
  linear-programming upper bounds (Cohn–Elkies) that are computable and where a
  numerically certified improvement is a real result.

## The cheap tests every candidate must pass first

1. **The tiling test.** A claimed Heesch number `k` for a shape `T` requires
   proving `T` does **not** tile the plane. That is the hard half and it is
   where every wrong claim lives: a shape that tiles has `H = ∞`, so a search
   that found `k` coronas and stopped has measured its own search bound, not the
   Heesch number. Non-tiling must be established by an argument, not by failure
   to find a tiling.
2. **The exhaustiveness test.** A claim that no `(k+1)`-th corona exists is an
   *exhaustive* statement over placements. It must come from a complete search —
   UNSAT from a solver on a faithful encoding, or an exhaustive enumeration with
   its bound stated — and the encoding must be validated on shapes with known
   Heesch numbers before it is believed.
3. **The encoding test.** Every SAT/CP encoding of a tiling question must be
   round-tripped: a satisfying assignment must be decoded back into an actual
   geometric patch and verified geometrically, with exact arithmetic. An
   encoding bug produces beautiful, wrong answers in both directions.

## What is genuinely unknown

- Whether Heesch numbers are bounded on non-tiling shapes. Open.
- The maximum Heesch number achieved by any known shape — a record to be
  confirmed and, ideally, beaten.
- Which isohedral numbers are realised.
- Decidability of whether a given polyomino tiles the plane.
- Densest sphere packings in dimensions 4–7, 9–23, and beyond 24, where only
  bounds are known.
- Whether an aperiodic monotile exists under stricter conditions than the 2023
  construction (no reflections was itself resolved — check what remains).

## What counts as a result

In descending order of value.

1. A shape with a Heesch number **larger than the published record**, with the
   coronas exhibited and the non-tiling proved, not merely searched for.
2. A proof that the Heesch number is bounded, or unbounded, for a stated class
   of shapes (polyominoes, polyiamonds, polyhexes) — a class result is real and
   is far more reachable than the general question.
3. An exhaustive determination of the Heesch numbers of a complete class — every
   polyomino up to `n` cells, say — with the enumeration bound stated and the
   solver's UNSAT results reproduced.
4. A new isohedral number realised, with the tiling exhibited and its orbit
   count proved.
5. A certified improvement to a Cohn–Elkies-style packing bound in a named
   dimension, with the certificate exact or interval-verified.
6. A refutation, with a witness, of a published claim or a folklore expectation
   about which values occur.

**Do not claim a Heesch number from a search that stopped.** Report the largest
corona found, the search bound, and whether non-tiling was proved — three
separate facts, three separate labels.
