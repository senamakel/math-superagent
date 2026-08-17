# Approach: star-complement reconstruction (the method that killed srg(57,14,1,4))

```approach
idea: Reconstruct a putative srg(99,14,1,2) from a star set / star complement for
  one of its eigenvalues using the Reconstruction Theorem of Cvetkovic-|
  Rowlinson-Simic, the exact technique that Milosevic 2008 used to REPROVE
  Wilbrink-Brouwer's nonexistence of srg(57,14,1,4) — the other k=14
  (lambda=1) member that does not exist. The spectrum of (99,14,1,2) is
  3^54, -4^44 (multiplicities 54 and 44), so a star set for eigenvalue 3 has
  54 vertices (star complement order 45) and for -4 has 44 vertices (order 55).
  The Compatibility Graph Comp(C, xi) is built from (0,1)-vectors b with
  <b,b>=xi and <b',b''> in {-1,0}; every realization of G with C as a star
  complement for xi is a CLIQUE in Comp(C, xi), so the whole space of graphs
  collapses to a finite clique search.
mechanism: For any srg(v,k,1,2) with xi not in {0,-1}, a star set X for xi is
  location-dominating; the Reconstruction Theorem pins the adjacency of the
  star part purely from the star complement C and the columns b_u of B via
  xi*I - A_X = B^T (xi*I - C)^-1 B. Lemma 3 (Milosevic, after CRS) guarantees
  ANY induced subgraph H avoiding xi extends to a star complement. The seed is
  the closed neighbourhood N[v0] plus one outer vertex v: in srg(99,14,1,2),
  N[v0] is the 7K2 windmill W15 (v0 + its 14 neighbours, no neighbour-neighbour
  edges because lambda=1), and v is at distance 2 with mu=2 common-neighbour
  structure into N[v0]. This is EXACTLY the seed shape that worked for 57
  (whose local graph is also 7K2, lambda=1), now at mu=2 instead of mu=4.
  TARGET EIGENVALUE: all published applications use a positive eigenvalue
  (xi=2 for the 57- and 75-cases), because the compatibility machinery
  enumerates (0,1)-vectors b_u with b_u^T b_u = xi = number of neighbours in C.
  For (99,14,1,2) the positive eigenvalue is xi=3 (multiplicity 54), so the
  star complement to search over has order 99-54 = 45. The 57-case is the
  decisive precedent: identical local graph, identical lambda, same seed,
  OTHER mu — so the mu=2 coupling must enter the reconstruction
  (outer-vertex common-neighbour count into the windmill).
status: refuted

## Killed by (inventor, converge round)

REFUTED in favour of 6vertex-condition-obstruction. The decisive obstruction is
honest scale, which research certified: every completed star-complement
nonexistence used star complements of order <= 19 — the (75,32,10,16) case needed
~5000 CPU-hours even at order 19 — while (99,14,1,2) requires order 45 (star set
54 for xi=3) with a 54-clique compatibility search. That is an order of magnitude
beyond any computed precedent, so on this machine the honest deliverable is a
deepest-reachable-level boundary (#6), not a theorem or construction. The
proposal's advertised separator (vt) is struck (research): star-set size is the
parameter-determined eigenvalue multiplicity and does no structural work — BvLS's
132/110 star sets are LARGER than 99's 54/44. The method also never touches the
run's central lever, n3 >= 1. It remains a live *literature* technique (the only
one that killed a k=14 sibling, 57) and is worth re-opening if a way to shrink
the complement to local segments is found — but as proposed it cannot decide 99.
killed-by: order-45 complement beyond every completed scale (~5000 CPU-h at
  order 19); vt-separator struck; no contact with the n3 lever.

  19-vertex complements of every completed application (57-case: 19; 75-case:
  19; 95-case: small fixed H), so the compatibility clique search is an order
  of magnitude beyond any star-complement computation actually performed; but
  the seed (windmill + 1 outer vertex) collapses the space exactly as in
  Milosevic, and this technique is the only one in the record that PROVED a
  k=14 sibling impossible.
precedent:
  - Milosevic, "An example of using star complements in classifying strongly
    regular graphs", Filomat 22:2 (2008) 53-57,
    https://doi.org/10.2298/fil0802053m -- REPROOF of Wilbrink-Brouwer
    nonexistence of srg(57,14,1,4) via a 19-vertex star complement for
    eigenvalue 2, built from the 16-vertex seed H = N[u] cup {v} (windmill W14
    + one distance-2 outer vertex), extended by Lemma 3 to 3720 non-isomorphic
    19-vertex star complements, compatibility graphs searched with Cliquer, no
    clique of size 38 (the multiplicity of 2). THE template this line copies
    verbatim; the seed shape is identical (7K2 local graph, lambda=1).
  - Cvetkovic, Rowlinson, Simic, "Eigenspaces of Graphs", CUP 1997,
    https://doi.org/10.1017/cbo9781139086547 -- the Reconstruction Theorem
    (Thm 7.4.1) and its converse (Thm 7.4.4): for an eigenvalue xi of
    multiplicity k, a k-set X is a star set for xi iff xi is not an eigenvalue
    of C = G-X and xi*I - A_X = B^T (xi*I - C)^-1 B, where B records the
    edges between X and C. Star sets exist for every eigenvalue; the machinery
    is finite when xi not in {-1,0}.
  - Rowlinson, "Star complements and maximal exceptional graphs", Filomat 18
    (2004) 25-32, https://doi.org/10.2298/pim0476025r -- Theorem 2.1 (the
    Reconstruction Theorem in statement form), star complements for -2,
    exceptional-graph applications.
  - Rowlinson & Tayfeh-Rezaie, "Star complements in regular graphs: old and
    new results", Linear Algebra Appl. 432 (2009) 2230-2242,
    https://www.sciencedirect.com/science/article/pii/S0024379509002444 --
    survey of the method; new results on stars and windmills as star
    complements; SRG applications incl. the spectral proof of uniqueness of
    srg(81,20,1,6) (Stevanovic-Milosevic).
  - Azarija & Marc, "There is no (75,32,10,16) strongly regular graph",
    Linear Algebra Appl. 557 (2018) 62-83, https://doi.org/10.1016/j.laa.2018.07.019
    -- star complements for xi=2 of order 19, sc(H)-extension, showed
    omega(Comp(sc(H),2)) < 56 for every candidate; ~5000 CPU hours of clique
    computation. The scale baseline: order-19 complements already needed
    thousands of CPU-hours.
  - Azarija & Marc, "There is no (95,40,12,20) strongly regular graph",
    J. Combin. Des. 28 (2020) 294-306, https://doi.org/10.1002/jcd.21696 --
    same technique, moderate computation; implies no (96,45,24,18), no regular
    two-graph on 96 vertices, no pg(4,9,2).
  - Wilbrink & Brouwer, "A (57,14,1) strongly regular graph does not exist",
    Indag. Math. 45 (1983) 117-121, https://doi.org/10.1016/1385-7258(83)90047-1
    -- the original nonexistence that the star-complement technique reproves.
  - Library claims: milosevic-starcomplement-5714-template (sourced summary of
    the 57-case), srg99-not-vertex-transitive (checked: 99 is provably not
    rank 3 via |Aut| | 4158 vs rank-3 requiring |G_x| >= 84) -- but see the
    correction below: this fact does NOT feed the star-complement machinery.
  - NO source found applying the star-complement technique to (99,14,1,2):
    the searches (literature + citation graph out of the Milosevic paper) turn
    up only 57, 75, 95 and signed/decomposition analogues. Stated as absence,
    not as refutation. Every completed application uses star complements of
    order <= 19; the 99-case needs order 45 — a scale no star-complement
    computation has reached.
first-step: (1) Verify in exact integer arithmetic that the 16-vertex seed
  H = N[v0] cup {v} (windmill W15 + one distance-2 outer vertex with its mu=2
  common-neighbour pattern) does NOT have xi=3 as an eigenvalue (compute char.
  poly in sympy). (2) Enumerate the compatibility vectors b with <b,b>=3 under
  the Riccati equation, build Comp(C,3) for the 45-vertex complement, and
  search for cliques of size 54 whose chosen star set reconstructs a graph G;
  feed each candidate adjacency matrix to code/lib.srg.is_srg and report
  PASS / FAIL. (3) Repeat the identical pipeline on rook(3) and bvls_graph()
  as the admissibility gate -- the pipeline MUST find an srg on both controls
  (star complements of order 5 and 111/133 for their positive eigenvalues)
  before any empty result at 99 is believed.
```

## Verdict and corrections (research, this round)

**Grounded — the reformulation is the named star-complement/star-set method
(CRS Reconstruction Theorem), and the 57-case is a verbatim-template precedent:
identical local graph (7K2), identical lambda=1, same windmill-plus-outer-vertex
seed, different mu.** The literature search confirms the exact mechanism the
proposal describes, and the arXiv/literature record shows no one has applied it
to (99,14,1,2). Three corrections to the proposal as written:

1. **The vertex-transitivity lever is struck.** The proposal claims "9 and 243
   are rank-3, tiny symmetric star complements, star-set size 4 and 132/110,
   while a putative 99 is provably not vertex-transitive". Star-set size is the
   eigenvalue multiplicity — a parameter-determined number, not a symmetry
   statement: rook(3) has star sets of size 4 (xi=1 or -2), BvLS has size 132
   (xi=4) / 110 (xi=-5) — TWO TO THREE TIMES LARGER than 99's 54/44, not tiny.
   No source connects vertex-transitivity to star-complement structure, and
   the star-complement machinery runs on any graph regardless of symmetry.
   The claim `srg99-not-vertex-transitive` is a real, checked fact, but it
   does no work in this method and must not be advertised as the separator.

2. **Hypotheses of the Reconstruction Theorem hold here.** xi=3 (multiplicity
   54, star complement order 45) and xi=-4 (44, order 55) both lie outside
   {-1,0}, so the finite compatibility-vector machinery applies in principle.
   All published applications use a positive eigenvalue (xi=2), which is the
   (0,1)-vector regime b_u^T b_u = 3; xi=3 is therefore the natural target.

3. **The honest scale question is the milestone.** Every completed
   star-complement nonexistence used complements of order <= 19; the 75-case
   took ~5000 CPU hours at that size. Order 45 with a 54-clique search is an
   order of magnitude beyond precedent. The reportable result is the deepest
   reachable level of that clique search with the scale logged — not the
   vt-contrast.