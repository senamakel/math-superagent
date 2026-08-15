# Coordinates of the 24-cell, 600-cell and their Coxeter/Petrie plane projections

**Subject:** Exact integer / quadratic-field coordinates of the regular
4-polytopes and their orthogonal projections to planes, giving regular-gon
shadows — the technique-tier foundation of the adopted
`projection-distance-equalization` approach
(`research/approaches/projection-distance-equalization.md`).

## Source (exact statements retrieved server-side; full text not held)

Retrieved via the server-side search/retrieval layer:
- **H. S. M. Coxeter, J. C. Fisher, J. B. Wilker,** "Coordinates for the
  Regular Complex Polygons", Proc. LMS (from the Cambridge Mathematical
  Journal lineage) — https://doi.org/10.1112/s0024610797004936 — real
  projections of the polytopes {3,3,4}, {3,4,3}, {3,3,5}; the 600-cell's
  Petrie/triacontagonal projection; coordinates for the 24-cell and 600-cell.
- **V. Elser, N. J. A. Sloane,** "A highly symmetric four-dimensional
  quasicrystal", J. Phys. A: Math. Gen. 20 (1987) 6161;
  https://doi.org/10.1088/0305-4470/20/18/016 — the 24-cell vertices as all
  24 permutations of (±1,±1,0,0); the 600-cell vertices as the 120 unit
  icosians (binary icosahedral group) in Q(√5); projections onto planes.
- **M. Al Ajmi, M. Koca, H. Bait Bu Salasel,** "Projection of polyhedra onto
  Coxeter planes described with quaternions", SQUJS 19(2) (2015) 77–90;
  https://doi.org/10.24200/squjs.vol19iss2pp77-90 — 24-cell as the binary
  tetrahedral group (24 quaternions), 600-cell as the binary icosahedral group
  (120 unit quaternions), the Coxeter plane defined by the simple roots, and
  vertices projecting to orbits of the dihedral group of order 2h.
- **"Binary Icosahedral Group and 600-Cell",** Symmetry (MDPI) 10(8):326,
  https://www.mdpi.com/2073-8994/10/8/326 — 2I as the vertex set of the 600-cell
  via the H4 Weyl group acting on unit quaternions.
- **J. C. Baez, "The Icosidodecahedron",** arXiv:2309.15774 — the 600-cell as
  the 120 unit quaternions forming the binary icosahedral group, coordinates in
  Q(√5) (the "unit icosians").

## What the sources establish (exact statements)

**24-cell.** The vertices are the 24 permutations of (±1, ±1, 0, 0) — exact
integers in Z^4. Symmetry group: binary tetrahedral group D4 Weyl group (order
1152). Dodecagonal projection: projecting {3,4,3} to a plane yields a regular
12-gon (Coxeter–Fisher–Wilker §; the 24-cell's Petrie polygon is a regular
12-gon).

**600-cell.** The vertices are the 120 unit icosians = the binary icosahedral
group 2I ⊂ unit quaternions (one of the two double covers of the icosahedral
rotation group A5). Their coordinates lie in Q(√5) (a + bi + cj + dk with each
of a,b,c,d of the form x + y√5, x,y ∈ Q). Symmetry group H4 of order 14400.
Petrie projection: the 600-cell projects to a **regular 30-gon** (triacontagon)
along a Petrie polygon (Coxeter–Fisher–Wilker; the frontispiece of Coxeter's
*Regular Polytopes* is exactly this triacontagonal projection).

**Projection mechanism.** A Coxeter plane is the (unique) plane fixed by the
Coxeter element c of the Coxeter group, on which c acts as rotation by 2π/h (h
= Coxeter number). Projecting any polytope vertex set orthogonally onto this
plane sends the vertices into an orbit of the dihedral group of order 2h. So a
single rank-2 orthogonal projection of a fixed 4D vertex set gives a regular-polygon
configuration in the plane. All edges are computed exactly: a pair's projected
squared distance is the rank-2 form Q_π(x) = (a·x)² + (b·x)² with a, b the two
projection rows.

## Bearing on this problem

These give the adopted projection-distance-equalization approach its exact
construction data:

1. The 24-cell (24 integer vertices, 96 edges, 1152 symmetries) and 600-cell
   (120 Q(√5) vertices, 720 edges, 14400 symmetries) are exactly-certifiable
   source sets in Z^4 / Q(√5) — no floats.
2. The rank-2 projection Q_π = (a·x)² + (b·x)² is not a homothety: it sends
   pairs of *different* source lengths to the *same* planar length (explicit
   24-cell example in the approach note: difference vectors (0,2,0,0) and
   (0,−1,1,0), source lengths 2 and √2, both project to squared norm 4 under
   rows a=(0,1,3,0), b=(0,0,0,1)). This is what makes a projected UDG genuinely
   new rather than a rescaling.
3. The chromatic question is open (no located source computes chi of these
   projected UDGs) — honest absence recorded.

## Sourced claim

```claim
id: regular-4-polytope-projections
statement: >
  The 24-cell has vertex set all 24 permutations of (±1,±1,0,0) (exact
  integers, binary tetrahedral / D4 symmetry, order 1152, dodecagonal Petrie
  projection). The 600-cell has vertex set the 120 unit icosians = the binary
  icosahedral group 2I embedded in the unit quaternions, coordinates in Q(√5)
  (H4 symmetry, order 14400), with a regular-30-gon (triacontagonal) Petrie
  projection. Orthogonal projection of any such set onto its Coxeter plane
  sends vertices to an orbit of the dihedral group of order 2h, and a rank-2
  projection is NOT a homothety (pairs of different source lengths can equalize
  to one planar length).
hypotheses: standard regular 4-polytope geometry and quaternionic / group
  representations, exact coordinate fields Z^4 and Q(√5).
holds-here: yes — these are the exact source point sets and projection mechanics
  the adopted projection-distance-equalization construction uses.
status: asserted (retrieved server-side from multiple mutually-confirming
  sources; not machine-checked here). The *equalization counterexample* (24-cell
  pair under rows a=(0,1,3,0), b=(0,0,0,1)) is set as the first-step machine
  verification of the adopted approach — it must reproduce symbolically.
bearing: supplies a genuinely new, dense, exactly-certifiable family of planar
  unit-distance graphs (24-cell / 600-cell projections) to feed the forced-pair
  SAT harness and the census — the adopted answer to the run's crux
  G-forced-pair-exists (shortage of richer base graphs).
anchor: research/sources/regular-4-polytope-projection-quaternions.md
falsifies: if the equalization counterexample does not reproduce symbolically at
  the first step, the projection line is dead at that step (per the approach's
  own stated attack surface).
```

## What could not be obtained

Full verbatim publisher texts (Coxeter LMS, Elser–Sloane J.Phys.A, Al Ajmi
SQUJS, MDPI) are blocked at the network boundary; direct download was refused.
Exact statements above were retrieved server-side and cross-confirmed across the
independent sources. In particular the vertex-coordinate facts (24-cell
integer permutations of (±1,±1,0,0); 600-cell in Q(√5)) are standard and
reproduced in multiple sources. Recorded so nobody re-attempts those hosts.
