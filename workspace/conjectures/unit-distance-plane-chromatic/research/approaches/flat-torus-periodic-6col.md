# Periodic 6-colourings as distance graphs on flat tori

```approach
idea: Attack the *upper* bound by reformulating "colour every point of R^2" as
  "colour the flat torus R^2/Lambda for a period lattice Lambda". A
  Lambda-periodic n-colouring of the plane is proper iff the induced colouring
  of the torus puts no two points x, y with some lift at Euclidean distance
  exactly 1 in the same class. The finite object is NOT the torus itself (it is
  a continuum) but the *separation graph* F(Lambda, rho) on lattice points:
  colour a Lambda-periodic tiling with cell radius rho, and join two cell centres
  u, v iff |u-v| <= 1 + 2 rho. A k-colouring of the finite quotient of F is a
  proper k-colouring of the whole plane.
mechanism: A Lambda-periodic k-colouring of R^2, constant on the cells of a
  Lambda-periodic tiling whose cells have radius rho (max |point - centre|),
  is proper iff for every pair of same-coloured cells the exact lattice
  inequality |u - v| > 1 + 2 rho holds (then no point of one cell can be at
  distance 1 from any point of the other, and cells of diameter 2 rho < 1 kill
  the within-cell case). So the search object is genuinely finite:
  (lattice basis, rho, colouring of the finite quotient of the separation graph
  F(Lambda, rho)), with correctness a set of exact norm-squared inequalities in
  Q(sqrt3) — no floats. The two layers, which the literature did not connect:
  (1) DISCRETE SPINE — Barajas-Serra's circulant reduction says the chromatic
  number of a *lattice-point* distance graph is attained periodically and equals
  the minimum over finite quotients, so the spine is a finite SAT object;
  (2) THICKENING LEMMA — a colouring of the lattice points with discrete margin
  > 1 + 2 rho lifts to a proper colouring of all of R^2 via radius-rho tiles.
  Named mathematics: distance graphs on flat tori, lattice packings/coverings,
  the A2 hexagonal tiling's exact margin, Barajas-Serra 2005 circulant reduction.
status: adopted
first-step: Build code/lib/torus_margin.py: (1) separation_graph(basis, rho, n)
  returning the exact finite graph F on the n x n quotient of the lattice, edges
  decided by exact norm^2 <= (1+2 rho)^2 in Q(sqrt3); (2) a SAT k-colouring check
  on F via the run's calibrated oracle; (3) calibration that re-derives the A2
  hexagon 7-colouring margin EXACTLY — expected from a hand derivation to verify:
  same-colour centre distance is sqrt(21)*L (the record's "sqrt(7)*L" is lattice
  norm without the sqrt3 centre-spacing conversion), valid hexagon side-length
  window 1/(sqrt21-2) < L < 1/2, min same-colour separation L(sqrt21-2) -> up to
  ~1.291 at L -> 1/2. Then confirm F(A2, rho) is NOT 6-colourable in that window
  (machine-verified chi=7 for the hexagonal tiling), and sweep a parametrised
  family of lattices (rational rotations / sublattices of A2) at k=6 to either
  find a 6-colouring or accumulate a periodic-impossibility census.
precedent:
  - Streinu & Theran, "Sparse hypergraphs and pebble game algorithms" is not
    the relevant branch here. The relevant lattice/torus literature:
  - "Distance graphs with maximum chromatic number", Barajas–Serra, DMTCS 2005,
    https://doi.org/10.46298/dmtcs.3391 — for integral distance sets D, chi(G(D))
    equals the minimum over n of chi of the finite circulant reduction; a global
    colouring that is *periodic* always attains chi(G(D)). This is the strongest
    published evidence that, at least for lattice/periodic distance graphs, a
    periodic colouring suffices to reach the chromatic number.
  - "FROM RAINBOW TO THE LONELY RUNNER: A SURVEY ON COLORING PARAMETERS OF
    DISTANCE GRAPHS", D.D.-F. Liu, Taiwanese J. Math. 2008,
    https://doi.org/10.11650/twjm/1500404981 — survey: the plane unit-distance
    colouring problem is the 4<=chi<=7 open problem; notes periodic/integral
    distance graph work and the plane problem's ties to it. Confirms this
    candidate is attacking the recorded "unstructured" upper-bound side.
  - X. Zhu, "Pattern periodic coloring of distance graphs", JCTB 1998,
    https://www.sciencedirect.com/science/article/pii/S0095895698918317,
    doi:10.1006/jctb.1998.1831 — **single author Xuding Zhu** (the earlier
    draft of this note said "Liu & Zhu"; corrected). Introduces pattern periodic
    colorings for integral distance graphs G(Z, D) and completely determines
    chi(G(Z,D_{m,[2,k']})). Primary record now in the library
    (`zhu-1998-pattern-periodic-coloring-distance-graphs.md`). Confirms the
    periodic-colouring search is a named, literature-studied technique.
grounded-by: periodic-coloring-attains-chromatic-number-for-lattice-distance-graphs
```

## Literature verdict

The reformulation itself is **established and correctly named**: a Λ-periodic
colouring of the plane is an n-colouring of the finite *torus distance graph*
R²/Λ (edge iff some lift is at unit distance), and the margin condition is exact
over the lattice. This is standard and the candidate states it correctly.

The key open question the approach hinges on — *can a periodic colouring reach
the plane's chromatic number, i.e. can the 7 be beaten by a periodic 6-colouring,
or must the best colouring be aperiodic?* — is **not settled and is genuinely
open in the literature.** The survey (Liu 2008) and the Barajas–Serra paper give
strong but for-the-integer-lattice-analog evidence: for integral distance graphs
G(D) ⊂ Z, the chromatic number *is* always attained by a periodic colouring
(chi(G(D)) = min_n chi of the finite circulant reduction). This is the exact
periodic-suffices mechanism the candidate needs, and it holds in the lattice
setting. But the flat plane R² with the full unit circle as the distance set is
not the Z-line, and the strongest search found no theorem either (a) constructing
a periodic 6-colouring of the plane, or (b) proving periodic colourings cannot
beat 7. The literature leaves both open.

## Decision — adopted, with the synthesis the gap demanded

**The gap.** My original mechanism said "the search object becomes finite (a
lattice + a colouring of fundamental-domain tiles)." It does not, as stated: the
torus ℝ²/Λ is a continuum, so colouring it is still an infinite problem unless
one imposes tile-constancy, and the literature's periodic-suffices theorem
(Barajas–Serra) is proved for *lattice-point* distance graphs, not the continuous
plane. Neither side alone gives a finite, exact, machine-checkable search object.

**The synthesis (neither of us named it as one thing).** Split the continuum
reduction into two layers and connect them with an explicit lifting lemma:

1. **Discrete spine** — the *lattice-point* distance graph on Λ, whose
   k-colourability (with a discrete margin) is, by Barajas–Serra, attained
   periodically and equals a minimum over finite quotients: a finite SAT object.
2. **Thickening** — a colouring of the lattice points with margin `> 1 + 2ρ`
   extends to a proper colouring of all of ℝ² by colouring each cell of radius ρ
   by its centre's colour (cells of diameter `2ρ < 1` handle the within-cell
   case; the margin handles the across-cell case). The lift is an exact
   lattice-norm inequality, so correctness is exact arithmetic, not floats.

The combined object is the **separation graph F(Λ, ρ)**: vertices = cell centres
(lattice points mod a finite-index sublattice), edge iff `|u−v| ≤ 1 + 2ρ`.
A k-colouring of F is exactly a Λ-periodic k-colouring of the plane by radius-ρ
tiles. This is finite, exact, and directly SAT-testable by the run's calibrated
oracle — the thing the flat-torus idea promised but did not deliver, now delivered
by the lattice-point reduction the literature actually establishes.

**Why this beat the other two.** Hajós and Alon–Tarsi are both closed at the
source: Hajós by ∃R-complete realizability (harder than the original search) plus
a join/merge that does not preserve unit-distance realizability; Alon–Tarsi by
direction (EE≠EO certifies 4-*colourability*, not non-colourability). This one is
the only candidate whose mechanism the literature *strengthens* rather than
refutes, and it attacks the side the record calls unstructured (the upper bound),
so it does not collide with the already-adopted Lovász-theta lower-bound line.

**What the first result is.** The A2 hexagonal tiling is the extremal object for
the upper bound, and the run's record carries a margin (`sqrt(7)·L`) that a hand
derivation says is off by a factor of √3 — the correct same-colour centre distance
is `√21·L` in physical units. Machine-verifying the exact margin and proving
`χ(F(A2, ρ)) = 7` in the valid window (`1/(√21−2) < L < 1/2`) is the first
artifact: *"the hexagonal tiling provably needs 7 colours; any 6-colouring must be
non-hexagonal or aperiodic."* Then the sweep over rational rotations and
sublattices of A2 at k=6 is the search for a 6-colouring, with the negative case
accumulating a periodic-impossibility census. Both are exactly what GOAL.md lists
as machine-verifiable deliverables.

**Flagged for verification, not asserted:** the `√21·L` margin and the window are
a hand derivation made here and must be reproduced by the exact-arithmetic
oracle before anything rests on them (the record's `√7·L` is itself unverified
scratch, so both numbers are open until `torus_margin.py` computes them).
