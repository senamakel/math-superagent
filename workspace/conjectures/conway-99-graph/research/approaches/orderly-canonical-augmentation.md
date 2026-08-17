# Approach: orderly canonical augmentation over the 231-line geometry

```approach
idea: Turn the triangle geometry (a partial Steiner triple system on 99 points,
  231 blocks of size 3, 7 blocks per point, whose collinearity graph is a
  putative srg(99,14,1,2)) into a FINITE decision via Read's orderly generation
  / McKay's canonical augmentation: build the geometry one line at a time,
  rejecting non-canonical extensions by an explicit isomorphism test, so that
  every partial system is visited once modulo isomorphism and the tree of
  extensions has a provable pruning. This is exactly the method problem.md names
  ("orderly generation / canonical augmentation on the triangle geometry") and
  the only route to a finite decision with a stated, checkable search space that
  the run has not actually attempted. The mu=2 collinearity condition becomes a
  per-line acceptance test: adding a line {a,b,c} is allowed iff, over the
  already-built geometry, a and b (resp. a,c; b,c) either are already on a
  common line (lambda=1 satisfied with the existing third point) or are
  non-collinear and the number of paths they would get stays <= 2 with exactly
  2 once the geometry is complete (mu=2).
mechanism: The geometry is a partial STS whose collinearity graph must be
  (99,14,1,2). Build the point-block incidence matrix N (99x231, column weight
  3, row weight 7) whose collinearity graph A satisfies A = NN^T - 7I. The
  orderly generator adds lines in Gray-code / canonical order and uses
  (i) a canonical label of the partial geometry (via a graph-canonical tool on
  the incidence bigraph) so only canonical representatives are extended; and
  (ii) the derived lambda/mu+degree constraints as a cheap utility prune:
  7 lines per point, every edge on exactly one line, every nonedge on exactly
  2 length-2 paths, total 231 lines, and the eigenvalue spectrum 3^54,-4^44
  computable in exact integers. The search space is the set of partial STS(99)
  extensions, pruned by canonicity (isomorphism classes) and by the mu=2
  acceptance test. Why this can fail on and only on the controls: rook(3)=srg
  (9,4,1,2) has 6 lines, bvls(243) has 891 lines but 243 points; the orderly
  tree of partial STS(9) with 6 lines must terminate finding the rook(3)
  completion, so the generator is validated by finding all 6-line partial
  systems; at 99 the tree either terminates empty (nonexistence, a genuine
  finite theorem with a stated search space) or grows to 231 lines
  (existence, an explicit certificate to certify through the oracle).
  The 99-specific number that bounds the honest frontier: 231 = 99*14/6
  lines, 7 per point, replication count 7, and the eigenvalue-at-each-extension
  integrality (spectrum 3^54,-4^44) is the exact, integer filter that an
  approximate-search or heuristic look-alike cannot fake.
status: refuted

## Killed by (inventor, converge round)

REFUTED in favour of 6vertex-condition-obstruction. The method is sound and
affectionately named (orderly generation / GCCP), but research certified its
honest boundary: the largest completed full STS classification is order 19
(Kaski-Ostergard, ~2 CPU-years); STS(21) is the smallest open case; a 99-point
partial STS with replication 7 is astronomically beyond any completed
enumeration. Even the two k=14 siblings that were settled (57 and 85) were NOT
settled by a global orderly generator — by star complements and by exhaustive
local-segment enumeration respectively. Therefore the deliverable on this machine
is a capped frontier (deepest canonical level, wall clock, prune counts), which
problem.md ranks as a boundary statement (#6), not an obstruction. It is also the
weakest of the three at lever contact — it is precisely the global enumeration the
run's own rules name as the standing temptation, and it makes no contact with the
n3 >= 1 lever that the adopted 6-vc line attacks. The machinery (canonical
labelling, GCCP) is still the right engineering for a *local* segment
enumeration, which is how the 85-case actually closed.
killed-by: 99-point partial-STS tree beyond the STS(v=19) frontier; siblings
  57/85 settled locally, not globally; no contact with n3 -- it is the global
  enumeration the run already rules out.

  and even canonical augmentation may not reach 231 lines on this machine; but
  that is precisely the honest boundary that is a reportable partial result
  (the deepest canonical partial system reached, wall-clock and space recorded),
  and the mu=2 + 7-per-point + spectrum prunes are unknown in strength a priori.
  A capped run is a legitimate deliverable in problem.md, not a guess.
precedent:
  - Read, "Every one a winner or how to avoid isomorphism search when
    cataloguing combinatorial configurations", Ann. Discrete Math. 2 (1978)
    107-120 -- the orderly-generation / canonical-labelling rejection scheme,
    the foundational method.
  - McKay, "Isomorph-free exhaustive generation" (J. Algorithms 26 (1998)
    306-324) -- canonical augmentation (GCCP): each object accepted iff its
    augmentation is the canonical inverse reduction; the modern standard the
    generator implements through a graph-canonical labelling.
  - Afzaly, "Generation of Graph Classes with Efficient Isomorph Rejection",
    ANU PhD thesis 2016, http://hdl.handle.net/1885/117453 -- orderly
    generation vs canonical-augmentation, systematic treatment with efficiency
    analysis.
  - Kaski & Ostergard, "The Steiner triple systems of order 19", Math. Comp.
    73 (2004) 2075-2092, https://doi.org/10.1090/s0025-5718-04-01626-6 -- the
    largest completed orderly classification of STS(v): 11,084,874,829
    nonisomorphic STS(19), ~2 CPU-years; seed + exact cover + nauty isomorph
    rejection; STS(21) is the smallest open full case (1.16e14 classes with
    sub-STS(7), Heinlein-Ostergard 2023). THE scale precedent: the full
    STS-classification frontier is v=19; a 99-point partial STS with
    replication 7 is astronomically beyond any completed enumeration — a
    statement of the honest boundary, and of how the run's deliverable at 99
    must be structural or a capped frontier, not a full enumeration.
  - Kokkala & Ostergard, "Sparse Steiner triple systems of order 21",
    J. Combin. Des. 28 (2020) https://doi.org/10.1002/jcd.21757 -- canonical
    augmentation + exact cover classification of 83,003,869 anti-Pasch
    STS(21) classes; the largest actual orderly search on a 21-point STS.
  - Shpectorov & Zhao, "Strongly regular graphs with parameters (85,14,3,2)
    do not exist", arXiv:2504.02449,
    https://doi.org/10.48550/arxiv.2504.02449 -- the other k=14 sibling
    settled by exhaustive enumeration of 478 local "segments" in 4 types
    around a max 3-clique; local graphs are the 39 good cubic graphs on 14
    vertices; it shows k=14 geometries DO admit complete local
    classifications (claim `shpectorov-zhao-85-nonexists-template`).
  - Keramatipour, "Approaching the Conway-99 problem using SAT solvers",
    arXiv:2604.23037 (2026), DOI 10.48550/arxiv.2604.23037 -- the same
    geometry as a SAT problem; reports a two-step "triangular view"
    construction, rules out Paley(9) patterns, notes SAT-solver inability at
    full scale; its partial-search frontier is the honest baseline this
    orderly generator must beat or honestly match.
  - Library claims: triangle-geometry-enumeration-closed (sourced: full STS
    classification stops at order 19; STS(21) is the smallest open case),
    c5 (neighbourhood = perfect matching 7K2, checked), integrality-five-members
    (checked: only five parameter sets in the srg(v,k,1,2) family).
first-step: (1) Implement the incidence-bigraph canonical labeller (build the
  bipartite point-line incidence graph, colour by side, canon = nauty-style
  canonical form). (2) Implement the 6-line generator for rook(3): enumerate
  all partial STS(9) with 6 lines, 4 per point, collinearity srg(9,4,1,2); the
  generator must terminate finding, up to isomorphism, the unique rook(3)
  geometry. (3) Then drive the same generator from 6 up toward 231 lines on 99
  points, recording the deepest canonical level reached, the prune counts
  (canonical rejection, mu-violation, degree-violation, spectrum-mismatch) at
  every level, the wall clock and the per-extension utility count. Report the
  boundary exactly -- that bound is a real result.
```

## Verdict (research, this round)

**Grounded.** The method is the named orderly generation / canonical
augmentation (Read 1978; McKay 1998 GCCP), and problem.md explicitly names it
as the design-theoretic finite-decision route. The precedent confirms both the
machinery and its honest scale: the largest completed STS-classification is
order 19 (Kaski-Ostergard 2004, ~2 CPU-years); STS(21) is open; a 99-point
partial STS with replication 7 is far beyond any completed enumeration, so the
deliverable is the capped frontier (deepest reachable canonical level, wall
clock, prune counts), exactly as the proposal says. Keramatipour's SAT work on
the same geometry is the existing baseline it must beat or honestly match. The
two k=14 siblings that WERE settled (57 and 85) were settled either by star
complements (Milosevic) or by exhaustive LOCAL-segment enumeration, not by a
global orderly generator — the 85-case is the closest structural precedent and
it already required a full cubic-graph classification as input. Nothing found
says anyone has completed or even published a capped orderly generation of the
partial-STS(99) tree; the deepest reachable level would be a new, honest data
point.