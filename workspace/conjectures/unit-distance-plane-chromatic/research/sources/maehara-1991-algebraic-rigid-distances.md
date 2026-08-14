# Maehara 1991 — distances in rigid unit-distance graphs are algebraic

**Source:** Hiroshi Maehara, "Distances in a rigid unit-distance graph in the
plane", *Discrete Applied Mathematics* 31 (1991) 193–200.
https://www.sciencedirect.com/science/article/pii/0166218X9190070D. Companion:
M. Homma, H. Maehara, "Algebraic Distance Graphs and Rigidity", *Trans. Amer.
Math. Soc.* 319 (1990) 561–572, DOI https://doi.org/10.2307/2001254.

**How obtained:** server-side retrieval (`deep_research`) returned the theorem
statements and a secondary-thesis discussion of the proof.

## What it establishes

**Theorem (Maehara, with Homma/Kato).** A number `d > 0` can appear as the
Euclidean distance between two vertices of some *rigid* unit-distance graph in
the plane **if and only if** `d` is an algebraic number.

- Forward (`rigid graph distance => algebraic`): in a fixed gauge, the vertices
  of a rigid unit-distance graph are isolated solutions of a polynomial system
  with rational coefficients (each edge `|p_i - p_j| = 1` is a quadratic), so all
  coordinates and mutual distances are algebraic. Maehara derives it from a
  theorem on critical values of real-algebraic functions.
- Converse (`algebraic => occurs as a rigid-graph distance`): constructive, via
  classical Kempe linkages (antiparallelograms, reversers, n-fans,
  distance-modification gadgets) that multiply and divide distances. Hence the
  set of distances occurring in rigid unit-distance graphs is exactly the
  positive algebraic numbers.

**Theorem (Homma–Maehara, algebraic distance graphs).** For a finite set
`X ⊂ ℝⁿ`, the algebraic-distance graph on `X` (adjacent iff distance is
algebraic) is complete **iff** `X` is rigid. Consequence: a convex polygon whose
sides are algebraic has algebraic diagonals and circumradius.

## Why it matters for this problem

`problem.md` says "vertices will have coordinates in a field like
`Q(√3, √11, ...)`". Maehara's theorem is the justification for exact algebraic
coordinate arithmetic: the coordinates of any rigid construction are algebraic,
so symbolic `|x - y|² = 1` checks over a number field are the right oracle —
there is never a need for floating point, and floating point would fabricate
spurious edges. This is the sourced backing for the "exact arithmetic from the
first line" discipline in `GOAL.md`.

## Basis and status

- Statement = sourced (original papers, retrieved). Standard, accepted.
- Not verified computationally here; it is a cited theorem, not a computed one.
