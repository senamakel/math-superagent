# Approach: the 6-vertex condition as the rank-3 boundary of the PQ hierarchy

```approach
idea: Push the t-vertex-condition hierarchy (Hestenes-Higman; Reichard; Pech;
  Brouwer-Ihringer-Kantor) up to t = 6 and run it as a 99-vs-controls filter.
  The 4- and 5-vertex conditions are INERT for partial-quadrangle
  (equivalently diamond-free, mu-fixed) collinearity graphs -- claim
  5vertex-pq-inert-6vertex-live proves 5-vertex holds for EVERY PQ and records
  that 6-vertex is where the family first becomes discriminating. A putative
  srg(99,14,1,2) is the collinearity graph of the partial quadrangle PQ(2,6,2)
  (Cameron 1975, adopted approach pq-2-6-2-classification), and it is provably
  NOT vertex-transitive (claim srg99-not-vertex-transitive), whereas BOTH
  controls rook(3)=GQ(2,1) and BvLS(243) are rank-3 / vertex-transitive and so
  satisfy every t-vertex condition trivially. Therefore the 6-vertex condition
  is the FIRST rung of the hierarchy at which a hypothetical PQ(2,6,2) can
  violate a universal PQ property without also eliminating 9 or 243 -- an
  obstruction here is 99-specific by construction.
mechanism: A t-vertex condition (Hestenes-Higman; Pech; BIK) fixes a hypothesis
  graph S on t vertices with two distinguished vertices and requires the count
  of embeddings of S in the collinearity graph with the distinguished pair
  mapped to (x,y) to depend only on whether x~y. The 4-vertex condition is
  exactly the PQ equation alpha=C(lambda,2)=0, beta=0 (claim
  bik-5vertex-holds-for-pq); the 5-vertex condition is inert for all PQs (two
  types only, counts (s-1)(s-2) and (s-1)(s-2)(s-3) both constant); the
  6-vertex condition introduces summing pairs of mu-graphs and is where the
  s (line-size) and t (spread) parameters of the PQ enter non-trivially.
  The 99-specific value: s = 2, t = 6 for PQ(2,6,2) (since k = s(t+1) = 14,
  s = k/(t+1) with t = mu spread), and the six-vertex subgraph of interest is
  two triangles joined by two edges -- exactly the n3 configuration that runs
  the whole n3-forced thread. Concretely: the 6-vertex condition phrased over
  the n3 seed (two disjoint triangles {a,b,c},{d,e,f} with exactly two cross
  edges, say a~d, b~e, no a~e etc., and the forced closure from lambda=1/mu=2)
  asks whether any two such d-joined triangle pairs induce different counts of
  common neighbours -- and computing those forced counts in exact integer
  arithmetic over rook(3) and bvls(243) gives the two no-obstruction controls
  while the n3-saturated configuration at (99,14,1,2) with its 7-per-point
  replication and 231 lines is exactly where the count can overdetermine.
  The rung that the CLAIM FILE ITSELF calls the first live one: 6-vertex holds
  for the two rank-3 controls trivially (vertex-transitivity collapses every
  t-vertex count of every type to a single number), so a 6-vertex violation at
  99 is the cleanest 99-specific local obstruction one can state -- the controls
  cannot refute it by construction.
status: adopted

## Decision (inventor, converge round)

ADOPTED over `star-complement-reconstruction` and `orderly-canonical-augmentation`.
Why it beats the others:
- **It is the only candidate whose success is a theorem (#3), not a capped-search
  frontier (#6).** Star-complement needs complements of order 45 (every completed
  application used order <= 19, and the 75-case's order-19 already cost ~5000
  CPU-hours); orderly augmentation of a 99-point partial STS is astronomically
  beyond the completed STS(v=19) frontier. On this machine both honest
  deliverables are a deepest-reachable-level boundary, not an obstruction.
  A 6-vertex overdetermination over the n3 seed, if it bites, is a proof.
- **It attacks the run's central open lever directly.** n3 >= 1 at 99 (Makhnev
  Thm 2, re-derived: claim n3-99-forced-at-least-3, checked) means a putative
  graph contains the n3 configuration — two disjoint triangles joined by exactly
  two edges — which *is* a 6-vertex type. The 6-vertex condition over that type
  is where the mu=2 Conway geometry could overdetermine, converting the run's
  hard-won n3>=1 conditional into a contradiction.
- **It is control-immune by construction.** Both controls rook(3) and BvLS are
  rank-3 / vertex-transitive (claim srg99-not-vertex-transitive, checked), so
  they satisfy every t-vertex condition trivially. A 6-vc violation at 99 is the
  only one of the three lines the 9/243 test cannot refute — it must NOT be
  re-validated on the controls because the controls pass every rung by symmetry.
- **The research correction strengthens it.** Pech's proven 6-vc family is
  PQ(q-1,q^2,q^2-q) = (81,20,1,6), NOT PQ(2,6,2); so the 6-vc for the mu=2
  Conway geometry is open and must be COMPUTED over the n3 type — a genuine new
  result in either direction, not an import from Pech.

killed-by for the refuted alternatives:
- star-complement-reconstruction: honest scale. Every completed star-complement
  nonexistence used order-<=19 complements (order-19 already ~5000 CPU-hours for
  (75,32,10,16)); the 99-case needs order 45 and a 54-clique compatibility
  search — an order of magnitude beyond precedent, so its deliverable on this
  machine is a capped frontier (#6), not a theorem. The vt-separator is struck
  (star-set size is the parameter-determined eigenvalue multiplicity — BvLS's
  132 > 99's 54 — and does no structural work). It also does not touch the run's
  n3 lever.
- orderly-canonical-augmentation: honest scale. Full STS classification stops at
  v=19 (Kaski-Ostergard, ~2 CPU-years); a 99-point partial STS with replication
  7 is astronomically beyond any completed enumeration, so the deliverable is the
  deepest canonical level reached, not a decision. Even the two k=14 siblings
  that WERE settled (57, 85) were not settled by a global orderly generator but
  by star complements and exhaustive local-segment enumeration. Weakest lever
  contact of the three — it is the same enumeration the run already ruled out as
  the standing temptation.

speculative: medium -- 6-vertex is a real barrier (the number of 6-vertex
  hypothesis types that must be force-counted is large, and overdetermination
  is not guaranteed to bite at (99,14,1,2)); but the n3 seed IS a 6-vertex
  configuration and the run has already established that n3 >= 1 is forced at
  99 (claim n3-99-forced-at-least-3), so the 6-vertex condition over the n3
  subgraph is the natural algebraic home of the run's own central open lever.
precedent:
  - Pech, "On highly regular strongly regular graphs", Algebraic Combinatorics
    4 (2021) 1211-1242, https://doi.org/10.5802/alco.183 -- the t-vertex
    condition / k-isoregularity framework; Thm 5.7: the point graph of a
    partial quadrangle satisfies the 5-vertex condition (PROVED in library,
    claim 5vertex-pq-inert-6vertex-live); Prop 5.8: for a PQ point graph the
    6-vertex condition reduces to 8 graph types. Corollary: point graphs of
    PQ(s,t,mu) = (q-1,q^2,q^2-q) satisfy the 6-vertex condition. NOTE: the
    (q-1,q^2,q^2-q) family is GQ(2,9)-derived and gives (81,20,1,6) at q=3,
    NOT PQ(2,6,2); it is the Brouwer-Haemers (81,20,1,6) family of claim
    bondarenko-radchenko-lambda1-gk. The proposal's identification of the
    "6-vertex live family" with PQ(2,6,2) is NOT what Pech proves; the
    6-vc family is a different mu, and PQ(2,6,2) sits at mu=2.
  - Reichard, "Strongly regular graphs with the 7-vertex condition", J.
    Algebraic Combin. 41 (2015) 817-842, https://doi.org/10.1007/s10801-014-0554-1
    -- point graphs of GQs satisfy the 5-vertex condition (Thm 1); point graphs
    of GQ(s,s^2) satisfy the 7-vertex condition (Thm 2; also the 6-vc for
    GQ(q,q^2), per the Pech-BIK chronology). The origin of the GQ(s,s^2) high
    regularity; Klin-conjecture context.
  - Reichard, "A criterion for the t-vertex condition of graphs", JCTA 90
    (2000) 304-314, https://www.sciencedirect.com/science/article/pii/S0097316599930455
    -- the two infinite series of Brouwer-Ivanov-Klin graphs (non-rank-3)
    satisfy the 5-vertex condition; the t-vc/iso-regularity criterion.
  - Brouwer, Ihringer, Kantor, "Strongly regular graphs satisfying the
    4-vertex condition", arXiv:2107.00076,
    https://doi.org/10.48550/arxiv.2107.00076 -- 4-vc with parameters
    (alpha,beta); for PQ/GQ collinearity graphs alpha=C(lambda,2), beta=0;
    Sec 3.4 classification of STS block graphs satisfying the 4-vc;
    asserts 5-vc for PQs (lines 181-185).
  - Cameron, "Partial quadrangles", Quart. J. Math. 26 (1975) 61-74 -- the
    defining paper for PQ(2,6,2) and its collinearity-graph parameters; the
    adopted pq-2-6-2-classification line rests on it.
  - Hestenes & Higman, "Rank 3 graphs and strongly regular graphs", SIAM-AMS
    Proc. 4 (1971) 141-160 -- origin of the t-vertex condition; rank-3 graphs
    satisfy it for all t.
  - Library claims: 5vertex-pq-inert-6vertex-live (asserted, PROVED in
    library), bik-5vertex-holds-for-pq (asserted), srg99-not-vertex-transitive
    (checked), n3-99-forced-at-least-3 (checked), n3-seed-locally-consistent-radius1
    (checked), bondarenko-radchenko-lambda1-gk (sourced: the (81,20,1,6)
    family = PQ(2,9,6), the ACTUAL Pech 6-vc family).
first-step (converged, tool_builder-startable today): (0) Precisely, on the n3
  type S = two disjoint triangles {a,b,c},{d,e,f} joined by exactly 2 edges
  (say a~d, b~e, all other cross pairs nonadjacent). In any srg(v,k,1,2) the
  lambda=1/mu=2 counts force the common-neighbour of each cross pair:
  a,d have 1; a,e have 2; etc. (1) Enumerate, in exact integer arithmetic, all
  isomorphisms types of induced 7-vertex overgraphs of S consistent with
  lambda=1, mu=2, and, for each, count the number of ways a 7th vertex x can
  attach to the 6 so that NO lambda or mu constraint is violated — this is the
  6-vertex-condition "embedding count of type T_{x0,y0}" for the PQ point graph.
  (2) Derive the claimed fixed value F(S) the 6-vc demands (a linear function of
  the lambda,mu counts only) and verify the computed embedding counts equal F(S)
  on rook(3)=srg(9,4,1,2) and bvls_graph()=srg(243,22,1,2) — where vertex
  transitivity forces equality trivially (the control check, must pass). (3)
  Using the run's already-computed forced geometry of a hypothetical
  (99,14,1,2) and n3 >= 1 (claim n3-99-forced-at-least-3), compute the 6-vc
  embedding count for S at (99,14,1,2) in exact integers and check whether the
  lambda/mu counts can be met simultaneously — if they cannot, the n3 configuration
  itself violates the 6-vc and srg(99,14,1,2) cannot exist (a #3 theorem,
  control-immune because both controls satisfy every t-vc by rank-3 symmetry).
  Concrete sub-task 0: build the 8-vertex forced closure of the n3 seed once more
  (lib already has the n3-seed radius-0/1 enumeration, claim
  n3-seed-locally-consistent-radius1) and, of its satisfying assignments, count
  the induced 6-vertex-overgraph embedding multiplicities against the formula
  F(S); any two assignments giving different counts for the SAME 6-type at fixed
  (x0,y0) adjacency is a contradiction. Run the counter on rook(3) and bvls first
  (both must give constant counts), then on the n3-saturated 99 geometry.

```

## Verdict and critical correction (research, this round)

**Grounded — as a named, live hierarchy; with ONE critical correction to the
proposal's key claim.** The t-vertex-condition hierarchy is exactly as
described, and the rung status is right: 4- and 5-vc are inert for all partial
quadrangles (Pech Thm 5.7), and 6-vc is the first potentially discriminating
rung for a non-rank-3 proper PQ (Pech Prop 5.8 reduces the 6-vc for a PQ to
8 hypothesis types). Both controls are rank-3 and pass every rung trivially,
and a 99-graph is provably not rank 3 (`srg99-not-vertex-transitive`,
checked) — so an obstruction found here is 99-specific by construction.
The n3 seed (two triangles joined by exactly two edges) is a genuine 6-vertex
configuration, and the run already forces n3 >= 1 at 99 (n3-99-forced-at-least-3).
BUT: the correction. **Pech's 6-vc result is for PQ(q-1, q^2, q^2-q) — a
family whose collinearity graphs include the Brouwer-Haemers (81,20,1,6) at
q=3 — NOT for PQ(2,6,2).** The proposal's "6-vertex condition is where Pech's
family becomes discriminating... PQ(2,6,2)" overreaches: the 6-vc family Pech
exhibits is a DIFFERENT parameter family (mu = q^2-q = 6 at q=3), not the
mu=2 Conway geometry. So the literature does NOT already show that PQ(2,6,2)
is at a "first live rung"; it shows the 6-vc is a live rung for the broader PQ
class, and it must be COMPUTED for the n3 type at (99,14,1,2) (the proposal's
first-step) rather than imported from Pech. With that correction the approach
stands: the 6-vc over the n3 seed is still the natural algebraic home of the
n3 lever, and an overdetermination there would be new. No source applies the
6-vc to (99,14,1,2) directly — stated as absence, not refutation.

## First step EXECUTED (tool_builder): the 6-vc embedding checker at the controls

`code/out/six_vc_n3_type.py` implements `count_induced_embeddings(G, S_adj,
x0, y0, x, y)` exactly per Reichard Def 4 — the number of INJECTIVE INDUCED
embeddings of a 6-vertex graph type over a distinguished ordered pair. Run on
both rank-3/vertex-transitive controls, so every type must be constant per
adjacency class (the mandatory control pass).

Validated two independent ways:
- CONTROL PASS: every type constant per adjacency class on rook(3) and bvls.
- The C6 type reproduces the independently-established induced-hexagon totals
  exactly: rook(3) per-edge count 2 (x18 edges / 6 = 6 hexagons, matches brute
  force); bvls per-edge count 11180 (x2673 / 6 = 4,980,690, matches claim
  c8-induced-hexagon-count-bvls). This cross-checks the induced-embedding
  machinery against a number the run already holds.

Results (capture: code/out/six_vc_n3_type.captured.txt):
- n3 type (two disjoint triangles joined by exactly 2 edges): embedding count
  0 on BOTH controls, on both the adjacent pair (a,d) and non-adjacent pair
  (a,e). Reason: both rook(3) and bvls have n3=0 (established), so the type
  does not embed at all — a degenerate control for the n3 type.
- C6 type (a,b adjacent): rook=2, bvls=11180 per edge — NONZERO, distinct.
- T2 type (two triangles joined by exactly one edge, a,d adjacent):
  rook=0, bvls=360/edge (90 distinct subgraphs, |Aut fix (a,d)|=4) — the
  nonzero one-edge-joined twin.
- T2-nonzero and C6-nonzero are the live validation types (they exist at the
  controls); the n3 type itself is zero at both controls and is therefore the
  99-specific quantity.

DIRECTIVE'S FIRST TEST (parameter-determined?): the 6-vc embedding count is a
SUBGRAPH-COUNT structural invariant, NOT parameter-determined. The C6 count
differs between the two controls (2 vs 11180) although both are srg(*,*,1,2);
the n3-type count is 0 at both purely because n3=0 there. At a hypothetical
(99,14,1,2) with n3>=1 forced (Makhnev Thm 2), the n3-type 6-vc count is
nonzero and carried by the free n3 shift in the Reimbayev hexagon identity —
which the parameters provably do NOT fix (claim order6-n3-not-forced). So this
line does NOT die on parameter-determinism the way the incidence p-rank might;
it stays LIVE for approach step (3): compute the n3-type 6-vc embedding count
on the hypothetical 99 geometry and ask whether the lambda/mu counts can be
met simultaneously. The zero-value at both controls is the stated limit of the
control for this particular type; the next step needs a positive n3>0 control
(none of the in-family mu=2 SRGs has n3>0) or the hypothetical 99 geometry
itself.