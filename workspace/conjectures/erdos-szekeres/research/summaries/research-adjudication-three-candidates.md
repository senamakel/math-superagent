# Adjudication of three candidate approaches against the literature

Research specialist report. Date: run of the Erdős–Szekeres investigation.

Three candidates proposed by the inventor were taken to the literature and each
adjudicated to `grounded` or `refuted` on evidence, with the approach file under
`research/approaches/<slug>.md` updated.

## 1. `convexity-complex-fvector` — REFUTED

- **What it is called.** The complex of convex-position (hereditary) subsets of a
  point set is the **free-set complex of a convex geometry / antimatroid**. This is
  real and standard: Edelman–Reiner–Welker, "Convex, Acyclic, and Free Sets of an
  Oriented Matroid", DCG 27 (2002) 429–453 (doi 10.1007/s00454-001-0055-6);
  Edelman–Reiner, "Counting the Interior Points of a Point Configuration", DCG 23
  (2000) 155–168 (doi 10.1007/pl00009483); Edelman–Jamison, Geom. Dedicata 19
  (1985). Jonathan Beagley, "On the Order Dimension of Convex Geometries", Order 30
  (2013) 515–530 (doi 10.1007/s11083-012-9280-2), explicitly rephrases the ES
  conjecture as order-dimension growth of the closed-set lattice.
- **Why it is refuted.** The load-bearing step — a shadow / Kruskal–Katona estimate
  "N ≤ 2^{(facet size)}" — is false as a pure-combinatorial statement: a simplicial
  complex of dimension n−2 can have arbitrarily many vertices with no face of size
  n (disjoint (n−1)-cliques). KK gives a *lower* bound on shadow size,
  never an *upper* bound on vertices from the absence of large faces. The whole
  bound must come from the oriented-matroid / anti-exchange structure, which is
  exactly the conjecture restated. The restatement is faithful but not a reduction.
  No published f-vector theorem for these complexes delivers 2^{n-2}.

## 2. `same-type-tverberg-wedge-split` — GROUNDED

- **What it is called.** Replacing the single-line separator by a radial fan /
  wedge / sector separator, anchored on the same-type lemma (Bárány–Valtr) and
  Tverberg/Radon pieces. The radial-fan structure is literally the ES lower-bound
  construction (blocks T_0..T_{n−2}, |T_i| = C(n−2,i), near circle angles):
  claim `es-lower`, `es61-lower-bound`, ROOT.md §2.
- **Support.** The line-split failure at n=7 is the run's own computed fact
  (claim `gsplit-enum-completeness-and-n7-zero`). The strongest exact-threshold
  corroboration is Baek–Balko SoCG 2025 (doi 10.4230/LIPIcs.SoCG.2025.13): the
  **split k-gon** relaxation has threshold exactly 2^{k-2}+1, and ES holds for
  **decomposable** sets — the phenomenon that a split/relaxed separator recovers
  the exact constant (asserted-by-source; full text not held).
- **Caveat (grounded, not proven).** Only a *2-way* bipartition (two halves, each
  2^{n-3} and (n−1)-avoiding) recovers 2^{n-2}; a k-way fan with k≥3 does not. The
  claim that every extremal set admits such a wedge decomposition is not in the
  literature. The arbiter is a wedge (ray-pair) enumerator on es_construct at n=7:
  does a 2-way sector split the 32 points into two 16-point, 6-avoiding halves?
- **Thin evidence note.** The same-type/Tverberg constants (Bárány–Valtr, claim
  `barany-valtr-positive-fraction`) are asymptotically loose and cannot by
  themselves give an exact 2^{n-2}. The wedge-split recursion itself is not a
  named published theorem; I found no paper doing exactly this. That is a fact
  about the (thin) search, not a refutation.

## 3. `radon-circuit-no-radon-4set` — REFUTED (central premise false)

- **What it relies on.** Oriented-matroid circuits = minimal Radon partitions
  (Ramírez Alfonsín, DCG 22 (1999) 117–127; standard oriented-matroid theory).
- **Why it is refuted.** In rank-3 affine geometry *every 4-subset* of a
  general-position planar set is a circuit: 4 points are always affinely dependent
  (lifted 4×4 determinant of (x,y,1) rows = 0) and, by general position, no 3 are
  collinear, so each 4-set is a minimal dependent set. Hence the circuit hypergraph
  of every planar general-position set is the COMPLETE 4-uniform hypergraph and
  carries no convexity information. "Every n-subset contains a circuit 4-subset" is
  vacuously true. The convex/non-convex distinction lived in my assessment not in
  circuit *membership* but in the Radon-partition *signing* (2+2 vs 1+3), which is
  orientation/chirotope data, not the circuit hypergraph — that is exactly the
  already-held 4-point criterion (`es35-four-criterion`) restated, with no new
  bound. Preparation: `code/out/radon_rank_check.py` (exact) written and indexed,
  ready for tool_builder/coder to run.

## Deliverables written

- `research/approaches/convexity-complex-fvector.md` — killed-by recorded.
- `research/approaches/same-type-tverberg-wedge-split.md` — precedent + caveat,
  status grounded.
- `research/approaches/radon-circuit-no-radon-4set.md` — killed-by recorded.
- `code/out/radon_rank_check.py` (indexed).
- Durable memory notes stored (oriented-matroid rank-3 fact, convex-geometry
  restatement-not-reduction, radial-fan/wedge grounded direction).
