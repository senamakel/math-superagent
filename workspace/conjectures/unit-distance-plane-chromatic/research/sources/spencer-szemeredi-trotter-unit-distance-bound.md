# Unit distances: the O(n^{4/3}) upper bound

**Subject:** The extremal bound that says unit-distance density cannot be
bought; high-chromatic graphs must be rigid. Task input to `problem.md`.

## Source
- **Primary:** J. Spencer, E. Szemerédi, W.T. Trotter, *Unit distances in the
  Euclidean plane*, in *Graph Theory and Combinatorics* (B. Bollobás, ed.),
  Academic Press, New York, 1984. (nyuscholars NYU record, 134 citations.)
- Concrete application: via Szemerédi–Trotter incidence bound
  I(P,L) = O(m^{2/3} n^{2/3} + m + n): for n plane points the number of unit
  distances is O(n^{4/3}).
- Modern survey of the connection and rigidity programme: J. Pach, O.E. Raz,
  J. Solymosi, *Erdős's unit distance problem and rigidity*, SoCG 2026, DOI
  10.4230/lipics.socg.2026.83.
- Pedagogical proof of the underlying incidence bound: H. Kaplan, J. Matoušek,
  M. Sharir, *Simple Proofs of Classical Theorems in Discrete Geometry via the
  Guth–Katz Polynomial Partitioning Technique*, arXiv:1102.5391 (2011).

## What it establishes
- Let `u_2(n)` be the maximum number of unit-distance pairs among `n` points
  of the plane. Then `u_2(n) = O(n^{4/3})` (Spencer–Szemerédi–Trotter).
- The bound is proved by counting point-circle incidences, dominated by the
  Szemerédi–Trotter point-line incidence theorem; a newer route is Guth–Katz
  polynomial partitioning.
- Erdős's lower bound is `u_2(n) = n^{1+O(1/log log n)}` (near-linear, given by
  the integer square grid); the gap between ~linear and n^{4/3} is wide open and
  the rigidity programme (Pach–Raz–Solymosi) is the current frontier.
- Consequence for colouring the plane: a unit-distance graph on `n` vertices
  has at most O(n^{4/3}) edges, so density per vertex shrinks; to force a high
  chromatic number the unit distances must be highly *coincidental*, which only
  happens for point sets with algebraic structure.

## Claim block
```claim
id: unit-distance-upper-bound
statement: u_2(n), the maximum number of unit distances among n plane points,
  is O(n^{4/3}).
hypotheses: points in the Euclidean plane R^2, distinct; edge iff distance 1.
holds-here: YES — the graphs the run constructs are unit-distance graphs on
  finitely many plane points, so each has O(n^{4/3}) edges.
status: asserted-by-source (Spencer–Szemerédi–Trotter 1984; a standard theorem).
bearing: tells us density cannot be bought; drives the search toward rigid,
  algebraically structured point sets, matching problem.md's framing.
anchor: research/sources/spencer-szemeredi-trotter-unit-distance-bound.md
follows-from: szemeredi-trotter-incidence
falsifies: a construction of n plane points with > C n^{4/3} unit distances
  for all C -- would contradict a classical theorem; none known.
```
