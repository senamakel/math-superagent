# Skeleton: a proved lower bound on the size of any 5-chromatic unit-distance graph

This is the GOAL.md-listed reachable result — "a theorem that all unit-distance
graphs on at most N vertices are 4-colourable, for the largest N you can
actually establish" — decomposed into two elementary lemmas and one finite
combinatorial check. The point of the reduction is that **all the geometry
collapses into two one-line facts**, and everything left is a finite
4-colourability check the run's already-calibrated oracle can perform. The
oracle (`sat-k-colourability-encoding`, workspace-calibrated on the Moser
spindle) is not a gap: it is listed in `rests-on`, not restated here.

```skeleton
goal: For a concrete integer N, to be pushed as large as the finite check allows
(starting from the calibrated 7-vertex baseline), every unit-distance graph in R^2
on at most N vertices is 4-colourable; equivalently, every 5-chromatic
unit-distance graph has at least N+1 vertices. By debruijn-erdos-1951 this is a
lower bound on the size of any finite unit-distance graph whose existence would
prove chi(R^2) >= 5.
implies: Suppose a 5-chromatic unit-distance graph H on <= N vertices exists.
Pass to a vertex-critical (5-critical) subgraph H' of H: repeatedly delete
vertices while the chromatic number stays 5, and the minimal survivor is
5-critical. A subgraph of a unit-distance graph is a unit-distance graph, so H'
is a unit-distance graph on <= N vertices. Then (S-critical-degree) H' has
minimum degree >= 4, and (S-nbhd-bound, applied to the unit-distance graph H')
H' is K4-free and K_{2,3}-free. Hence H' is a member of the finite set
U_N = { graphs on <= N vertices : min degree >= 4, K4-free, K_{2,3}-free }.
By (S-universe-4color) every member of U_N is 4-colourable, so H' is
4-colourable, contradicting chi(H') = 5. Therefore no 5-chromatic unit-distance
graph on <= N vertices exists. The three lemmas are jointly exhaustive for this
conclusion: the degree and forbidden-subgraph conditions are exactly the
structural constraints a 5-critical unit-distance graph must satisfy, and the
universe check is where the geometry-turned-combinatorics enumeration happens —
nowhere else does a geometric object enter the argument.
status: sketched
rests-on: sat-k-colourability-encoding, debruijn-erdos-1951
```

```gap
id: S-critical-degree
lemma: Every vertex-critical graph with chromatic number k has minimum degree at
least k-1; in particular every 5-critical graph has no vertex of degree <= 3.
(If v had degree <= 3: by criticality colour G - v with 4 colours, then v has at
most 3 neighbours and one of the 4 colours is free, a contradiction.)
status: open
next: theorem_prover: record this as a checked claim with the four-line proof
(delete v, extend a 4-colouring) and hand lean_prover the formal statement
"k-critical graph has min degree >= k-1" against mathlib's graph-colouring API.
Pure graph theory, no geometry, no tool run beyond recording the proof.
```

```gap
id: S-nbhd-bound
lemma: In any unit-distance graph in R^2: (i) two distinct vertices have at most
two common neighbours, because a common neighbour lies on the intersection of
two unit circles, which has size <= 2 — so the graph is K_{2,3}-free; and (ii)
no four vertices are pairwise at unit distance, because three pairwise-unit
points form a unit equilateral triangle and admit no fourth point at distance 1
from all three — so the graph is K4-free. (The two facts are independent: K4 is
K_{2,3}-free, so K4-freeness must be stated separately.)
status: open
next: symbolic_math: prove both in exact arithmetic and emit a certificate.
(i) the system |x-u|^2 = |x-w|^2 = 1 has at most two solutions over QQbar (two
unit-circle intersections); (ii) the system |x-a_i|^2 = 1, i = 1,2,3, with the
a_i the vertices of a unit equilateral triangle, is inconsistent — a sympy
Groebner-basis computation over QQ gives the empty variety. No floats anywhere.
```

```gap
id: S-universe-4color
lemma: For the largest N the finite check reaches (target >= 7), every graph on
<= N vertices with minimum degree >= 4, K4-free and K_{2,3}-free is
4-colourable — certified by the complete k-colourability oracle, with a witness
colouring stored per graph and the number of graphs tested recorded.
status: open
next: sat_solver + tool_builder: generate U_N = { graphs on <= N vertices :
min degree >= 4, K4-free, K_{2,3}-free } (geng with a min-degree flag plus an
explicit K4/K_{2,3} post-filter; combinatorially finite, at most 2^{C(n,2)}
graphs per n, feasible through n ~ 8-9 with pruning), then run the calibrated
oracle at k=4 on every member. Report the largest N with all members
4-colourable, the number tested, and one witness per graph. A failure is not a
dead end: any 5-chromatic member of U_N is a candidate 5-chromatic graph to test
for unit-distance realizability, which is the whole lower bound.
```
