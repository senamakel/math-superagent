# Approach: pair-labeling reduction of the 84-vertex second subconstituent

```approach
idea: Fix a vertex 0 of a putative srg(99,14,1,2). Its neighbourhood N(0)=7K2 is
  a perfect matching on the 14 neighbours (c5), and each of the 84 distance-2
  vertices is adjacent to exactly two neighbours of 0 (mu=2 and the degree
  count). Hence the 84 outer vertices are in natural bijection with the 84
  NON-matching pairs of the 14-set: label them by unordered pairs {i,j} with
  1<=i,j<=14 and {i,j} not an edge of the 7K2 matching, where outer vertex
  {i,j} connects to neighbours i and j of 0. The ENTIRE remaining freedom of
  srg(99,14,1,2) is a 12-regular graph H on these 84 pair-vertices (each already
  has degree 2 into N(0), so needs 12 more), and mu=2 + lambda=1 translate into
  explicit constraints on the PAIR-adjacency of H: for two outer vertices
  {i,j},{k,l} the number of common neighbours must obey a rule read off the
  intersection structure of the pairs. This is the Keramatipour pair-reduction,
  made into a finite object: existence of srg(99,14,1,2) <=> existence of a
  12-regular graph H on the 84 pairs of K14-minus-a-matching satisfying the
  mu=2/lambda=1 pair-adjacency rule.
mechanism: The intersection of pairs {i,j} and {k,l} (share 0, 1, or 2
  neighbours of 0) determines their contribution to common-neighbour counts
  against N(0), and mu=2 fixes the count against all vertices. This forces a
  sharp, largely deterministic adjacency rule among the 84 vertices -- most of
  H is forced combinatorially, and the residual free part is a FAR smaller
  search space than 99 vertices (84 vertices with heavy forced structure rather
  than a free 14-regular graph on 99). The named theory is the theory of the
  second subconstituent / the "outer" co-local graph of an SRG, combined with
  explicit pair/intersection counting. Crucially the controls fit the same
  picture (rook: 5/6 outer; BvLS: 220 outer pairs of 22-neighbours minus
  matching), so the admissibility gate is native to the statement: the rule must
  admit a 12-regular H at 9 and 243 too, and any contradiction must be the
  a=14/84-specific one. The honest deliverable is a bounded exhaustive sub-search
  on the 84-vertex pair space (a legitimate result #4 in problem.md), or a proof
  that the pair-adjacency rule alone is satisfiable -- either way it pins the
  frontier that the previous 99-vertex searches could not close.
first-step: (concrete, exact, can start today) (1) From code/lib.srg, for a fixed
  vertex 0 of each control, build the 84/220 outer pair-labeling and print the
  induced outer graph H with its adjacency matrix. (2) Derive the pair-adjacency
  rule (which pair-pairs are forced adjacent / forced non-adjacent by
  mu=2-vs-lambda=1 plus the existing edges into N(0)) and VERIFY it reproduces H
  exactly on rook(3) and bvls_graph(). (3) State the residual free parameter at
  99 (how few bits of H are not forced), hand it to sat_solver as a bounded
  CP-SAT on <=84 vertices, and record the honest frontier. The mu=2 lambda=1
  rule that fails to be realisable at 84 is the a=7/14-specific result.
status: adopted
```

## Decision (inventor, converge round)

ADOPTED. Research's check timed out and returned no refutation and no new
synthesis, so this decision rests on the documented closed routes and the
arithmetic.

Why it beats its siblings and the closed lines:
- It is the **only** candidate that genuinely changes the representation: a
  99-vertex free 14-regular search becomes a *labeled* 84-vertex 12-regular
  graph H on the explicit pair space (the 84 non-matching 2-subsets of the
  14-set of neighbours of 0), forced pair-adjacency rule from mu=2/lambda=1.
  That is a bounded finite object, not a 99-vertex search.
- It is **immediately checkable**: build the 84/220 outer pair-labeling from
  lib.srg for both controls, derive the pair-adjacency rule and verify it
  reproduces H exactly on rook(3) and bvls_graph(). The native admissibility
  gate is inside the statement.
- Distinct from every closed route: g-reduce (abstract outer design that does
  not recurse as an srg) builds NO explicit pair space; star-complement (order-45
  reconstruction, killed on scale) does not reduce to a labeled 84-vertex H;
  terwilliger (T(x)-algebra modules, killed as likely-null) is algebraic, not a
  combinatorial pair rule.
- The interlacing rigidity (companion approach) folds IN as an extra constraint
  on the CP-SAT for H (12-regular ⇒ trace 0; forced β₂..₄₀=3, β₅₆..₈₄=−4,
  banded 15 summing to −13), tightening the search rather than standing alone.

first-step: (1) From code/lib.srg, fix vertex 0 of each control, build the
  84/220 outer pair-labeling (bijection to non-matching pairs of the
  neigbourhood), print the induced outer graph H. (2) Derive the pair-adjacency
  rule (which pair-pairs are forced adjacent / non-adjacent by mu=2-vs-lambda=1
  plus existing edges into N(0)) and VERIFY it reproduces H exactly on rook(3)
  and bvls_graph(). (3) Feed the residual 12-regular + pair-rule + interlacing
  constraints as a bounded CP-SAT on <= 84 vertices (sat_solver) and record the
  honest frontier; require the encoder to FIND the true H on both controls first. Distinct from the closed
g-reduce (which built an *abstract outer design* and asked whether it recurses as
an srg -- answer no); this fixes the *explicit pair space K14\matching* and
derives a forced pair-adjacency rule, giving a real 84-vertex object to saturate.
Distinct from k14-l1-local thread (which is the Wilbrink-Brouwer GD-group
structure). The deliverable is an honest frontier on 84 vertices -- a problem.md
result class concurrently with a genuine reduction of the search space by the
pair intersection structure.
