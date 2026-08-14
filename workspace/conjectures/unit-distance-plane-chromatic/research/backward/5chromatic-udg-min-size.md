# Skeleton — proved lower bound on the size of a 5-chromatic unit-distance graph

This sharpens `research/backward/5chromatic-size-lower-bound.md`. The added
value is `sharp-nbhd-local` (iii): in a unit-distance graph, two neighbours of
a vertex are adjacent *iff* their angular separation is exactly 60°, so each
vertex's neighbourhood induces a graph of maximum degree ≤ 2. The existing
skeleton's finite kernel (`S-universe-4color`) drops unit-distance
realisability almost entirely; the kernel here keeps this necessary condition,
so the enumeration is both sound and a much tighter superset of the UDGs.

```skeleton
goal: For a concrete integer N, pushed as large as the finite check reaches
      (start at N = 7, since the 7-vertex Moser spindle is 4-chromatic),
      every unit-distance graph in R^2 on at most N vertices is 4-colourable;
      equivalently every 5-chromatic unit-distance graph has at least N+1
      vertices.
implies: >
  By contraposition. Suppose H is a unit-distance graph on <= N vertices with
  chi(H) >= 5.
  (i)  sharp-critical-degree: H contains a 5-critical subgraph H'; being an
       induced subgraph of H, H' is a unit-distance graph on <= N vertices with
       minimum degree >= 4.
  (ii) sharp-nbhd-local applied to H': H' is K4-free, K_{2,3}-free, and every
       vertex's neighbourhood induces a graph of maximum degree <= 2.
  (iii) Therefore H' belongs to the class C_N defined in sharp-kernel-4color
        (graphs on <= N vertices with delta >= 4, K4-free, K_{2,3}-free, and
        every vertex-neighbourhood of maximum degree <= 2).
  (iv) sharp-kernel-4color states that every member of C_N is 4-colourable,
       so H' is 4-colourable — contradicting chi(H') = 5.
  Hence no 5-chromatic unit-distance graph on <= N vertices exists, i.e. every
  unit-distance graph on <= N vertices is 4-colourable. The quantifier order
  is explicit: the N in the conclusion is exactly the N the finite check in
  sharp-kernel-4color was completed for.
status: sketched
rests-on:
  - sat-k-colourability-encoding
  # the complete k-colourability oracle run inside sharp-kernel-4color;
  # asserted in CLAIMS.md and calibrated on the Moser spindle (chi=4) per
  # CONTEXT.md — the gating check has passed, so the oracle is a tool, not a gap
killed-by: ~
```

```gap
id: sharp-critical-degree
lemma: >
  Every graph G with chi(G) = k contains a k-critical (vertex-critical)
  subgraph, and every k-critical graph has minimum degree at least k-1. In
  particular a 5-chromatic graph contains a 5-critical subgraph H' with
  delta(H') >= 4. (Identical in content to
  `5chromatic-size-lower-bound/S-critical-degree`; CLAIMS.md has no row for it,
  so it is open.)
status: open
next: >
  theorem_prover: record as a claim with the three-line proof — (a) delete
  vertices (and then edges) until every proper subgraph is (k-1)-colourable;
  (b) if a vertex v had degree <= k-2, take a (k-1)-colouring of G - v and give
  v one of the k-1 colours unused on its neighbours, a contradiction. Hand
  lean_prover the statement "k-critical graph has minimum degree >= k-1"
  against mathlib's graph-colouring API. Pure graph theory: no geometry, no
  oracle run, no enumeration.
```

```gap
id: sharp-nbhd-local
lemma: >
  In any unit-distance graph in R^2: (i) no four vertices are pairwise at unit
  distance — three pairwise-unit points form a unit equilateral triangle, which
  admits no fourth point at distance 1 from all three — so the graph is K4-free;
  (ii) two distinct vertices have at most two common neighbours, since a common
  neighbour lies on the intersection of two unit circles (<= 2 points), so the
  graph is K_{2,3}-free; (iii) for any vertex v, two neighbours x,y of v are
  adjacent iff the angle xvy is exactly 60 degrees (|x-y|^2 = 2 - 2 cos theta
  = 1 iff cos theta = 1/2), so each neighbour of v is adjacent inside N(v) to at
  most two others and N(v) induces a graph of maximum degree <= 2 — a disjoint
  union of paths and 6-cycles, hence 2-colourable. (Sharpens
  `5chromatic-size-lower-bound/S-nbhd-bound`, which had only (i) and (ii).)
status: open
next: >
  symbolic_math: prove all three in exact arithmetic and emit a certificate.
  (i) Groebner basis over QQ of the system |x - a_i|^2 = 1, i = 1,2,3, with the
  a_i the vertices of a unit equilateral triangle, gives the empty variety;
  (ii) the system |x-u|^2 = |x-w|^2 = 1 has at most two solutions over QQbar
  (two unit-circle intersections); (iii) solve |x-y|^2 = 2 - 2 cos theta = 1
  symbolically to get theta = +-60 degrees and read off the degree bound.
  No floats anywhere; the certificate is a Groebner-basis / polynomial-ideal
  computation.
```

```gap
id: sharp-kernel-4color
lemma: >
  For the largest N the finite check reaches (start at N = 7), every graph on
  <= N vertices with minimum degree >= 4, K4-free, K_{2,3}-free, and every
  vertex-neighbourhood inducing a graph of maximum degree <= 2, is 4-colourable.
  (This is the sharpened version of
  `5chromatic-size-lower-bound/S-universe-4color`; the neighbourhood-max-degree
  constraint is the extra necessary UDG condition that keeps the kernel honest.)
status: open
next: >
  sat_solver + tool_builder: encode "there exists a 5-chromatic member of C_N"
  as SAT and refute it for each n <= N — either enumerate C_N (geng/nauty with a
  min-degree flag plus explicit K4 / K_{2,3} / neighbourhood-max-degree filters,
  feasible through n ~ 8-9), or write the direct CNF (colour variables for 4
  colours forced UNSAT). Run the calibrated oracle at k = 4 on every member;
  UNSAT over all of C_N is the theorem. Report N, the number of graphs tested,
  and store one witness colouring per graph. A 5-chromatic member found is not a
  dead end: it is a candidate UDG whose realizability (sharp-nbhd-local plus the
  edge certifier) is the next question.
```
