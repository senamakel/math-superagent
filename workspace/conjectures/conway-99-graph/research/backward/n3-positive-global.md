# The n₃⁺ branch, decomposed — what would close the last open lemma

Reduction of the run's single open lemma. The goal "no srg(99,14,1,2)" was already
split by the live skeleton `n3-dichotomy` into **n₃ = 0** (DISCHARGED — Makhnev Thm 2's
closure of a triangle forces the parameter-infeasible srg(33,12,1,6); claims
`makhnev1988-condstar-theorems`, `makhnev99-shorter-proof-integrality`, gate
`makhnev-condstar-gate-passed`) and **n₃ ≥ 1** (OPEN: gap `G-n3-positive` of that
skeleton). So the whole problem is the n₃ ≥ 1 branch, and this file decomposes exactly
that branch: what would suffice, if proved, to close `G-n3-positive`.

Already held upstream (do not restate as open):

- **n₃ ≥ 1 at any putative Γ, sharpened to n₃ ∈ {3,6,9,…}** — `n3-99-forced-at-least-3`
  (checked), from Makhnev's contrapositive plus the order-6 residue n₃ ≡ 0 (mod 3)
  (`order6-n3-not-forced`, checked).
- **No local obstruction at any radius** — `G-n3-no-local-obstruction` (formalised on the
  kernel: `code/lean/n3_dichotomy_G_n3_no_local_obstruction.lean`). Built into every gap
  below: no finite-radius shell can close the seed; only a global move can.
- **Order-≤7 count identities cannot force n₃ into an empty range** —
  `order6-n3-not-forced` (checked); the order-7 Hamiltonian counts carry a second free
  variable (claim `reimbayev-order7-counts-two-free-vars`), closing that route too.
- **Forced-structure reduction at a fixed vertex 0** — `c5` (checked): N(0) = 7K₂;
  `forced-structure-reduction-conway99` (asserted): the 84 distance-2 vertices biject to
  the 84 non-matching pairs of N(0), inner–outer adjacency is fully forced, and the
  entire remaining freedom of Γ is a 12-regular graph H on those 84 pair-vertices.
- **Standalone interlacing on H is NOT an obstruction** — a necessary condition the true
  H satisfies by construction (approach `interlacing-84-vertex-rigidity`, refuted); it is
  kept below only as a tightening constraint inside `G-H-unsat`.
- **The seed-shell incidence ledger is absorbable** (route 7): 223–227 residual lines,
  669–681 residual incidences, no parity break (`code/out/n3_global_ledger.captured.txt`).
  Consequence: an over-subscription, if real, arises only in the cross-patch closure
  through all 99 points — stated as such in `G-budget-oversubscription`.

```skeleton
goal: no srg(99,14,1,2) exists
implies: n3 = 0 branch discharged (Makhnev -> srg(33,12,1,6) infeasible); a putative Gamma has n3 >= 1 (n3-99-forced-at-least-3) so contains the n3 seed. Diameter 2 + N(0)=7K2 + forced-structure-reduction-conway99 reduce Gamma to a 12-regular H on the 84 non-matching-pair vertices. G-seed-forces-S-in-H: the seed pins one of finitely many induced S_i in H. G-H-unsat: no pair-rule 12-regular interlacing-compliant H contains any S_i. Independent carrier: G-budget-oversubscription closes the seed's design closure against the exact 231-line/693-incidence/99-point budget. Either closes the n3>=1 branch; both branches cut => no Gamma. Conditional: G-h1-nonzero-99 + off-list parameter position would also close it (gate first).
killed-by: 
rests-on: makhnev1988-condstar-theorems, makhnev99-shorter-proof-integrality, makhnev-condstar-gate-passed, n3-99-forced-at-least-3, order6-n3-not-forced, c5, forced-structure-reduction-conway99
status: live
```

```gap
id: G-seed-forces-S-in-H
lemma: Let Γ be a putative srg(99,14,1,2), n3(Γ) >= 1, and T the n3 seed. Fix any vertex
  0 with N(0) = 7K2 and let H be the 12-regular outer graph on the 84 non-matching-pair
  vertices. Then in one of finitely many placements of T (Γ has diameter 2, so each of
  the six seed vertices is at distance 0, 1, or 2 from 0: it is 0, a neighbour, or a
  pair-vertex of H; enumerate the finitely many consistent label types), the seed and its
  mu=2/lambda=1 forced witnesses pin a finite induced subgraph S_i of H — every
  pair-edge among the involved pair-vertices that the common-neighbour counts force.
  Hence Γ ⊇ T forces (∃i) S_i ⊆ H; contrapositive for the skeleton: if no S_i embeds in
  any pair-rule-compliant H, no such Γ exists. Note the seed need not lie near 0 — the
  placement enumeration covers distance profiles 0/1/2 uniformly.
status: open
next: tool_builder labels the run's bounded forced structures against a fixed 0: take the
  19 radius-6 survivors / R8 branches of code/out/n3_grow_radius.py, compute each
  vertex's distance to 0 and its neighbour set inside N(0) (pair-vertex label where
  applicable), and print the forced S_i for every label type (exact integers, one
  capture). Control pass in the same script (extend code/out/research_pair_label_gate.py,
  currently gate-free): the same labelling machinery seeded by a configuration the
  controls DO contain — a triangle at rook(3) and a triangle at bvls — must reproduce
  the true outer graphs rook(3) (4 pair-vertices, 2-regular H = C4) and bvls (220
  pair-vertices, 20-regular H); a mislabelled control declares the machinery unsound and
  no S_i is believed until it is fixed.
```

```gap
id: G-H-unsat
lemma: For every forced seed subgraph S_i of G-seed-forces-S-in-H (i = 1..t, t finite),
  there is no graph H on the 84 pair-vertices of K14-minus-a-matching that (a) is
  12-regular, (b) obeys the mu=2/lambda=1 pair-adjacency rule (common-neighbour counts
  of every pair of pair-vertices against the inner structure), (c) has the
  interlacing-forced spectrum — Perron 12, exactly 39 eigenvalues equal to 3, 15
  eigenvalues in [-4,3] summing to -13, exactly 29 eigenvalues equal to -4 (exact trace:
  12 + 39*3 + (-13) + 29*(-4) = 0), and (d) contains S_i as an induced subgraph. Hence
  the n3 >= 1 branch admits no graph and no srg(99,14,1,2) exists.
status: open
next: CP-SAT on <= 84 pair-vertices: 12-regular + pair-rule, constrained to CONTAIN S_i,
  solved for each i; every solution is checked exactly — spectrum with sympy over exact
  integers, and the decoded 99-vertex graph through lib.srg.is_srg (a certified solution
  is a CONSTRUCTION and refutes the goal; UNSAT for every i is the death of the branch).
  HARD GATE FIRST (directive 40, task gate-pair-labeling-84): the encoder must find the
  true outer H on both controls — 2-regular on 4 pair-vertices at rook(3), 20-regular on
  220 at bvls — before any 99 UNSAT is admissible. The interlacing constraint (c) is an
  a-posteriori exact check on solutions, not a linear constraint.
```

```gap
id: G-budget-oversubscription
lemma: There is no partial Steiner triple system on 99 points, 231 lines of size 3,
  7 lines through every point (693 point-line incidences), containing the n3 seed and
  satisfying mu=2. Equivalently: the COMPLETE closure of the seed — all 99 points
  placed, 7 lines per point, every non-collinear pair sharing exactly 2 collinear
  points — over-subscribes the exact budget (>231 distinct lines, or >693 incidences,
  or a point on >7 lines) before it closes. Route 7 (code/out/n3_global_ledger.
  captured.txt) already shows the radius-6 seed-shell ledger is absorbable (223–227
  residual lines, 669–681 residual incidences, no parity break), so the
  over-subscription, if it exists, arises only in the cross-patch closure through all
  99 points — precisely what this lemma asserts, and the run's named live finish.
status: open
next: directive-39 SECOND task (incidence-budget-ledger-controls), carried to the full
  closure: run the exact ledger (points used, lines used, incidences used, per-point
  line count vs 7, per-degree vs 14). CONTROL PASS FIRST: seed the ledger with
  configurations the controls contain — a triangle at rook(3) must report exactly
  6 lines / 18 incidences and no over-subscription; a triangle at bvls exactly
  891 / 2673 — a control failure declares the ledger method unsound (it measures the
  family) and no 99 verdict from it is admissible. Only then close the 99 seed ledger
  through all 99 points. Parallel formulation (approach n3-seed-fisher-replication,
  adopted): CP-SAT with hard caps (99 points, 231 lines, 693 incidences) and the seed
  fixed; seed-present UNSAT with seed-free controls SAT is the k=14-specific
  contradiction. Exact integers everywhere.
```

```gap
id: G-h1-nonzero-99
lemma: Every srg(99,14,1,2) has H1(Cl(Γ); F) != 0 over at least one of F = F_1009,
  F_65537, where Cl is the 2-dimensional clique complex (99 vertices, 693 edges, 231
  triangles). COMBINED with the sourced classification (library summary
  cioaba-mim-clique-homology-srg: H1 != 0 only for Petersen, Shrikhande, complete
  bipartite graphs, conference graphs on <= 255 vertices, the lattice graphs L2(m), and
  the finite exceptional families E_m) and the parameter-position check that
  (99,14,1,2) lies on none of the DECIDED families — v = 99 = 4·24+3 is not a conference
  order; lambda = 1 forces a lattice graph to be L2(3) = the 9-vertex rook's graph; mu =
  2 excludes complete bipartite; s = -4 = -m with m=4 FALLS IN the exceptional family
  E_4 bucket (an allowed nonzero-H1 position, NOT excluded by the classification) —
  the contradiction would need to rule out E_4, which the classification does not do, so
  no such conclusion follows.
status: closed — the directive-39 gate REFUTED this line as a separator, and the
  classification phrasing behind it was overstated. H1(Cl) is nonzero on BOTH
  controls (dim H1 = 4 for rook(3), 1540 for bvls; code/out/pf_h1_closed_form.py,
  pattern-finder round 33), so Cioaba's H1!=0 criterion carries no 99-vs-243
  separation. CORRECTION to this lemma's stated mechanism: the classification
  (Cioaba-Mim Thm 8.4) does NOT force H1 = 0 at 99 — a putative (99,14,1,2) has
  lambda_min = -4 and falls in the finite EXCEPTIONAL family E_4 bucket, an
  ALLOWED nonzero-H1 position (only the parameters rule out conference, complete
  bipartite, and lattice families; E_4 remains undecided). The refutation rests on
  the controls (H1 nonzero on both), not on the classification forcing H1(99)=0.
  The gap as stated ("identifies the classification forces H1=0") is vacuous.
next: none — closed. Do NOT compute H1 for 99.
  parameter-determined, the gate passes, and G-h1-nonzero-99 becomes the genuine
  a=7-specific positive geometric theorem to seek.
```

## Discipline this skeleton imposes

- **Controls, in every gap.** The two existing members must pass each move in a named
  way. `G-seed-forces-S-in-H` and `G-H-unsat` carry their control passes inside their
  `next` (the labels/encoder must reproduce the true outer H at rook(3) and bvls).
  `G-budget-oversubscription`'s first step IS the control pass (6/18 and 891/2673
  budgets, no over-subscription). `G-h1-nonzero-99` is controlled by the gate itself:
  rook(3) sits on the classification list, bvls does not — the controls are run before
  anything at 99.
- **The dead ends are absorbed, not re-fought.** Local shells (G-n3-no-local-
  obstruction), order-≤7 identities (`order6-n3-not-forced`), standalone interlacing
  (approach refuted), and the seed-shell ledger (route 7) are closed; every gap here is
  global or gated.
- **What kills the skeleton:** nothing currently recorded. `G-seed-forces-S-in-H`
  refuted would make `G-H-unsat` unanchored (the seed would force no fixed S_i — a
  genuinely surprising outcome given μ=2's per-pair two-witness force). A control
  failure in either CP-SAT or the ledger would declare the corresponding gap's method
  unsound and must be filed before any 99 result from it is read.