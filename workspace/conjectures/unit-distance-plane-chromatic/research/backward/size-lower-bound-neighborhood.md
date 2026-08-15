# Skeleton: size lower bound via the unit-circle neighbourhood structure

This is a sharpening of the GOAL.md-reachable result — "every unit-distance
graph on at most N vertices is 4-colourable" — that replaces the *combinatorial*
universe of `5chromatic-size-lower-bound` with the *geometric* constraint a
unit-distance graph actually satisfies. The combinatorial skeleton's universe
`U_N = {graphs : min degree >= 4, K4-free, K_{2,3}-free}` is too weak to carry
the bound: triangle-free 5-chromatic graphs exist (the 23-vertex Mycielski
graph is triangle-free, hence K4-free), so K4-freeness does not begin to force
4-colourability, and the K4/K_{2,3} filters are the wrong ones. The
unit-distance-specific fact — the neighbourhood of a vertex lives on a unit
circle, where two neighbours are adjacent iff their central angle is 60°, so
the induced neighbourhood graph is a disjoint union of paths and 6-cycles — is
the constraint that actually distinguishes a unit-distance graph from an
arbitrary K4-free graph. This skeleton makes that constraint a lemma and puts
the finite check on the right (much smaller) universe.

```skeleton
goal: For a concrete integer N (target >= 7, the calibrated baseline), every
unit-distance graph in R^2 on at most N vertices is 4-colourable; equivalently,
every 5-chromatic unit-distance graph has at least N+1 vertices. By
debruijn-erdos-1951, any finite unit-distance graph witnessing chi(R^2) >= 5
would have >= N+1 vertices.
implies: Suppose H is a 5-chromatic unit-distance graph on <= N vertices. Pass
to a vertex-critical (5-critical) subgraph H' of H by repeatedly deleting
vertices while the chromatic number stays 5; the minimal survivor is 5-critical
and is still a unit-distance graph on <= N vertices (a subgraph of a
unit-distance graph is a unit-distance graph). By N-critical-degree, H' has
minimum degree >= 4. By N-nbhd-circle, applied to every vertex v of H', the
subgraph induced by N(v) is a disjoint union of paths and 6-cycles. Hence H' is
a member of the finite set
W_N = { graphs on <= N vertices : minimum degree >= 4, every neighbourhood a
disjoint union of paths and 6-cycles }.
By N-universe-4color every member of W_N is 4-colourable, so H' is
4-colourable, contradicting chi(H') = 5. Therefore no 5-chromatic
unit-distance graph on <= N vertices exists. The three lemmas are jointly
exhaustive: the degree bound and the neighbourhood bound are exactly the
structural constraints a 5-critical unit-distance graph must satisfy, and the
universe check is where the geometry collapses to a finite enumeration — the
neighbourhood constraint is what makes W_N small enough to enumerate past the
combinatorial skeleton's failure point.
status: sketched
rests-on: debruijn-erdos-1951, sat-k-colourability-encoding
```

```gap
id: N-critical-degree
lemma: Every vertex-critical graph with chromatic number k has minimum degree at
least k-1; in particular every 5-critical graph has minimum degree >= 4. (If v
had degree <= 3: by criticality colour G - v with 4 colours, then v has at most
3 neighbours and one of the 4 colours is free, a contradiction.)
status: open
next: theorem_prover: record this as a checked claim with the four-line proof
(delete v, extend a 4-colouring of G - v, a colour is free on N(v)); hand
lean_prover the formal statement "k-critical graph has minimum degree >= k-1"
against mathlib's graph-colouring API. Pure graph theory, no geometry. This is
the same lemma as `S-critical-degree` in 5chromatic-size-lower-bound, so
discharging one discharges the other.
```

```gap
id: N-nbhd-circle
lemma: In any unit-distance graph in R^2, for every vertex v the subgraph
induced by the neighbourhood N(v) is a disjoint union of paths and 6-cycles.
Proof sketch: every neighbour lies on the unit circle centred at v; two
neighbours are adjacent iff their central angle is 60° (the chord of a unit
circle has length 1 iff the central angle is 60° or 300°). Each neighbour is
therefore adjacent to at most two others (the points at angle ±60°), so the
neighbourhood graph has maximum degree <= 2; a cycle closes only after six
60°-steps (net rotation a multiple of 360°, and backtracking revisits a
vertex), so every cycle is a 6-cycle. In particular every neighbourhood is
bipartite, and this is strictly stronger than K4-freeness / K_{2,3}-freeness.
status: open
next: symbolic_math: prove in exact arithmetic that the system
x^2 + y^2 = 1, (x-1)^2 + y^2 = 1 has exactly the two solutions (1/2, ±sqrt(3)/2)
— i.e. chord length 1 on the unit circle iff central angle is exactly 60° — and
that a point on the circle has at most two points at chord distance 1 (a sympy
Groebner/elimination certificate over QQ). Then verify the lemma on the Moser
spindle's coordinates: compute N(v) for each of the 7 vertices in
Q(sqrt3,sqrt11,sqrt33) and confirm each induced neighbourhood graph is a path
or 6-cycle fragment. No floats anywhere.
```

```gap
id: N-universe-4color
lemma: For the largest N the finite check reaches (target >= 7), every graph on
<= N vertices with minimum degree >= 4 and every neighbourhood a disjoint union
of paths and 6-cycles is 4-colourable — certified by the calibrated complete
k-colourability oracle, with a witness colouring stored per graph and the
number of graphs tested recorded.
status: open
next: sat_solver + tool_builder: generate W_N = { graphs on <= N vertices :
min degree >= 4, every neighbourhood a disjoint union of paths and 6-cycles }
(geng with a min-degree flag plus an explicit per-vertex neighbourhood filter;
combinatorially finite, far smaller than the K4/K_{2,3}-filtered universe, and
feasible through n ~ 9-10 with pruning), then run the calibrated oracle at k=4
on every member. Report the largest N with all members 4-colourable, the count
tested, and one witness per graph. First concrete check (also the attack on the
old skeleton): determine whether any K4-free / triangle-free 5-chromatic graph
on <= 23 vertices survives the neighbourhood filter — the expectation is that
none do, which is precisely what the geometric constraint buys over the
combinatorial one.
```

## Attack surface — what breaks this skeleton

- **N-nbhd-circle must not be imported from a measurable-colour-class variant.**
  It is pure metric geometry (points on a circle, chord length), independent of
  any colouring hypothesis; verify it only as stated. The neighbourhood of a
  vertex is the set of points at distance exactly 1, all on the unit circle —
  no continuity or measurability assumption anywhere.
- **The combinatorial skeleton's universe is the falsifier to check first.**
  `5chromatic-size-lower-bound` claims its `S-universe-4color` over
  `{min degree >= 4, K4-free, K_{2,3}-free}`. That claim is suspect: a
  triangle-free 5-chromatic graph exists on 23 vertices (the Mycielski graph of
  the Grötzsch graph), hence is K4-free, so K4-freeness cannot imply
  4-colourability. Whether such a graph is also K_{2,3}-free is exactly the
  finite check that decides whether the old universe already fails — and the
  reason this skeleton's geometric universe must carry the bound.
- **The subgraph step uses that unit-distance-ness is hereditary.** Deleting
  vertices from a unit-distance graph leaves a unit-distance graph, so the
  5-critical reduction stays inside the class. This is automatic but must not
  be dropped.
- **The boundary of the finite check is honest, not optimised in advance.**
  If N-universe-4color finds a 5-chromatic member of W_N, that is not a dead
  end for the skeleton: it is a candidate 5-critical unit-distance graph (or a
  proof that the neighbourhood constraint needs one more geometric refinement),
  and it should be fed to the realizability test — the whole lower-bound
  direction. If the oracle instead exhausts W_N for N up to the infeasibility
  ceiling, the ceiling is the result and must be reported as such.
