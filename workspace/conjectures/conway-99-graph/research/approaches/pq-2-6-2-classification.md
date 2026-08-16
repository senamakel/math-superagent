# Approach: partial quadrangle PQ(2,6,2) — adopted as the vertex-condition-hierarchy filter

```approach
idea: Reformulate srg(99,14,1,2) as the collinearity graph of the partial
  quadrangle PQ(2,6,2) (Cameron 1975), and attack it through the
  t-vertex-condition hierarchy that the diamond-free / partial-quadrangle class
  makes available — NOT through a "classification of partial quadrangles at
  s=2", which does not exist (existence of PQ(2,6,2) is open and exactly
  equivalent to the problem).
mechanism: The 231 triangles are the lines of a partial linear space (3
  points/line, 7 lines/point). lambda=1 forces the diamond-free axiom (no point
  adjacent to two points of a line it does not lie on); mu=2 forces "every
  noncollinear pair has exactly 2 common collinear points". So the geometry is
  a partial quadrangle with s=2, t=6, mu=2; the whole family
  (9,4),(99,14),(243,22),(6273,112),(494019,994) is PQ(2,t,2) for
  t in {1,6,10,55,496}. The reformulation BUYS the vertex-condition programme:
  the collinearity graph of any PQ (indeed any lambda<=1 SRG) satisfies the
  4-vertex condition automatically with alpha=beta=0 (Brouwer-Ihringer-Kantor
  survey, Prop 2.1) — this is exactly the run's claim c7, and it is INERT
  (holds for 9, 99, 243 alike). The next rung, the 5-vertex condition, is NOT
  automatic, and a hypothetical 99-graph is provably non-rank-3 (see below),
  so it does not inherit the rank-3 free pass on all vertex conditions that its
  two controls likely enjoy. Therefore the 5-vertex condition is the first
  place in the hierarchy where a 99-graph could differ from the controls, and
  it is a FINITE, checkable necessary condition — a local linear-algebra
  question over the 34 graphs on <=5 vertices, not a search over 14-regular
  graphs on 99 vertices.
precedent:
  - Cameron, P. J., "Partial quadrangles", Quart. J. Math. 26 (1975) 61-74
    (the defining paper; cited as [10]/[38] across the PQ literature).
  - Mohammadian & Tayfeh-Rezaie, "On a family of diamond-free strongly regular
    graphs", arXiv:1303.0473. Exact equivalence: the collinearity graph of a
    PQ(s,t,mu) is a diamond-free SRG with v = 1 + s(t+1) + s^2 t(t+1)/mu,
    k = s(t+1), lambda = s-1, mu; conversely every diamond-free SRG is such a
    point graph. Checked at (99,14,1,2): s=2, t=6, mu=2, v=99.
  - Brouwer, Ihringer, Kantor, "Strongly regular graphs satisfying the
    4-vertex condition" (arXiv:2107.00076; FULL TEXT IN LIBRARY at
    research/sources/brouwer-ihringer-kantor-4vertex-condition.full.md):
    Prop 2.1 (Sims' criterion) and the sentence "It immediately follows that
    the collinearity graph of a ... partial quadrangle satisfies the 4-vertex
    condition ... The same holds for a graph Gamma with lambda <= 1."; Sec 3.4
    (Higman's theorem on STS block graphs meeting the 4-vertex condition).
    RESOLVES the earlier doubt below: lines 181-185 state "More generally the
    5-vertex condition holds for partial quadrangles" (asserted in the survey,
    no proof named; the GQ case is cited to Reichard [31]). So the 5-vertex
    condition IS a necessary condition on a PQ(2,6,2) collinearity graph, i.e.
    on a hypothetical srg(99,14,1,2) -- status `asserted`, claim
    `bik-5vertex-holds-for-pq`.
  - Pech, "On highly regular strongly regular graphs", Alg. Comb. (2021)
    alco.183 — the "highly regular"/vertex-condition programme. NOTE: the claim
    in the earlier draft that "point graphs of PQs satisfy the 5-vertex
    condition" is UNVERIFIED against the source and must be checked before it
    is relied on; the BIK survey only asserts the 4-vertex condition for PQs.
  - De Clerck/Durante/Thas, "Intriguing sets in partial quadrangles" (J. Combin.
    Des. 2010): known PQ parameter families and their GQ-minus-perp / hemisystem
    constructions; the known constructions all give parameter sets OTHER than
    s=2, which is exactly why PQ(2,6,2) is the open thin case.
status: adopted
grounding: The identification srg(99,14,1,2) = collinearity graph of PQ(2,6,2)
  is EXACT and named, verified by parameter substitution (s=2, t=6, mu=2, v=99).
  The reformulation does not by itself settle 99 (equivalence goes both ways).
  What it buys concretely, and what made it win over the other two candidates:
  it situates 99 inside the diamond-free class for which the 4-vertex condition
  is automatic but the 5-vertex condition is a live, finite constraint, and it
  exposes the parameter t=6 as the open rung between the two KNOWN members
  t=1 (rook(3) = PQ(2,1,2)) and t=10 (BvLS(243) = PQ(2,10,2)). The decisive
  new observation (from CLAIMS.md automorphism bounds): a hypothetical 99-graph
  is provably NOT rank 3, because |Aut| divides 2*3^3*7*11 = 4158 forces the
  point stabilizer order to divide 42, while rank-3 on 99 points requires the
  stabilizer to be transitive on 14 neighbours and 84 non-neighbours, i.e.
  order at least lcm(14,84) = 84. Rank-3 graphs satisfy every t-vertex
  condition for free; a 99-graph does not. So the 5-vertex condition is the
  first rung where the nonexistence argument has room to bite without also
  ruling out the controls.
first-step: (concrete, tool_builder can start today)
  (1) ADMISSIBILITY (lib/srg). Add partial_quadrangle_axioms(A) to
      code/lib/srg.py: enumerate triangles as lines; check (a) each
      neighbourhood is a disjoint union of cliques (diamond-free), (b)
      nonadjacent pairs have exactly 2 common neighbours, (c) each point lies
      on t+1 lines. Run on rook(3) and bvls_graph(); assert rook(3) ->
      (s,t,mu)=(2,1,2) and bvls -> (2,10,2). This pins the reformulation onto
      both controls and confirms 99 = t=6 sits between t=1 and t=10.
  (2) THE FILTER (the genuinely new computation). Add vertex_condition_4(A)
      (re-confirm alpha=beta=0, i.e. c7) and vertex_condition_5(A) to lib/srg:
      for each 5-vertex graph T with a distinguished ordered pair (x0,y0), check
      that the number of copies of T through a pair (x,y) depends only on
      adjacency of (x,y). Run on rook(3) and bvls_graph(); record whether the
      5-vertex condition holds on the controls (both may be rank 3, hence
      trivially pass — the check decides that too, without assuming it).
  (3) THE 99 QUESTION. For parameters (99,14,1,2), write down the linear
      equations the 5-vertex condition imposes on the order-5 subgraph counts:
      Reimbayev (research/sources/reimbayev-subgraphs-order-six-srg-l1-mu2)
      gives every total count of an induced subgraph on <=5 vertices as a
      function of (n,k) alone, so the equations are linear with known right-hand
      sides. Determine whether some pair-count is FORCED to vary across pairs
      of a given type; if any equation is inconsistent, that is a 99-only
      nonexistence step that the controls escape by their own t-values. State
      the search space (34 unlabelled graphs on 5 vertices x 2 pair types) and
      the exhaustiveness of the check before running it.
  (4) PARALLEL RESEARCH CHECK (one question, not a survey): does Pech 2021
      (alco.183) state that PQ point graphs satisfy the 5-vertex condition, and
      if so under which hypotheses? RESOLVED independently of Pech: BIK
      (lines 181-185) states "More generally the 5-vertex condition holds for
      partial quadrangles" (asserted, no proof named; GQ case cited to
      Reichard). So the 5-vertex condition is a NECESSARY condition a 99-graph
      must meet (claim `bik-5vertex-holds-for-pq`), and step (3) becomes a
      proof obligation to derive from the PQ axioms rather than an ad-hoc
      constraint. Ideally confirm Reichard's paper directly (second source for
      the asserted PQ part), but Pech is no longer needed to establish the fact.
killed-by: (none — adopted)
```

## Why this beat the other two candidates

- `macwilliams-binary-code-arc` and `higman-module-restriction` are both
  **parameter-determined invariants**: the two-weight code enumerator and the
  Smith normal form / critical group of an SRG are fixed by (v,k,λ,μ) alone
  (Delsarte 1972; Lorenzini killing theorem; Ducey et al. 2021). Every such
  invariant survives unchanged on the 9 and 243 controls and therefore cannot
  conclude anything about 99 — the exact admissibility failure GOAL.md forbids.
  The PQ / vertex-condition route is the opposite kind of object: the
  5-vertex condition is a *local uniformity* statement that is not fixed by the
  parameters, and it is exactly where a non-rank-3 graph can differ from the
  rank-3 controls.
- The PQ reformulation is not "re-labelling": it names the class (diamond-free
  SRGs / partial quadrangles) whose vertex-condition hierarchy is the studied
  weakening of rank 3, and it supplies the one fact that makes the hierarchy
  bite — 99 is provably not rank 3 while the problem's two witnesses sit at
  t=1 and t=10 on either side.

## Discipline (unchanged from GOAL.md)

Every nonexistence step derived from the 5-vertex condition must be run against
rook(3) and BvLS(243) through `code/lib/srg`, and the step that fails for them
must be named. Step (2) is that check, done first. The 5-vertex condition is a
*necessary* condition only if the Pech claim in step (4) checks out; until then
it is a computed fact about the controls and a set of linear equations any
99-graph must satisfy, stated as such.
