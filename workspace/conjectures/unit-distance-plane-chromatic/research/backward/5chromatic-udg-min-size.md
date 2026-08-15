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
  `5chromatic-size-lower-bound/S-critical-degree`.)
status: checked
checked-by: >
  research/backward/5chromatic-udg-min-size.md — record the claim with the
  three-line proof, then verify by complete exact enumeration over all graphs
  on <= 6 vertices with a fresh SAT oracle (lib.critoracle) cross-checked
  against lib.satcolor (0 mismatches). Both parts and the 5-critical
  conclusion PASS. Full note (proof, verification numbers, the discovered
  lib.coloring bug that made the first check fail) in the "Checked claim"
  section below.
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

---

# Checked claim — sharp-critical-degree: 5-chromatic ⇒ 5-critical subgraph with min degree ≥ 4

This section discharges the gap `sharp-critical-degree` above (and the
identical `S-critical-degree` of `research/backward/5chromatic-size-lower-bound.md`)
as a **checked** claim. It is the structural backbone step that connects
"5-chromatic unit-distance graph" to "member of the kernel `C_N`": the degree
constraint `delta >= 4` is exactly condition (a) of the sharp kernel.

## Statement

**(1) Every finite simple graph `G` with `chi(G) = k` contains a
vertex-critical subgraph `H` with `chi(H) = k`.** "Vertex-critical" means every
proper vertex-deleted subgraph has strictly smaller chromatic number:
`chi(H - v) <= k-1` for every vertex `v`.

**(2) Every vertex-critical graph `H` with `chi(H) = k` has minimum degree
`delta(H) >= k - 1`.**

**Conclusion.** Every `5`-chromatic graph contains a `5`-critical subgraph with
`delta >= 4`.

The classical "k-critical" notion requires every proper *subgraph* (edges too)
to be `(k-1)`-colourable, which is strictly stronger than vertex-critical. The
degree argument uses only the vertex-deleted property, so the weaker hypothesis
is the robust one to check; it implies the classical consequence needed here.

## Proof

**(1)** If `chi(G) = k`, repeatedly delete any vertex `v` with
`chi(G - v) = k`, until no such vertex remains. Finiteness terminates the
process. The survivor `H` satisfies `chi(H) = k` (chromatic number never
dropped below `k` and started at `k`) and, by construction, `chi(H - v) <= k-1`
for every vertex `v` — exactly vertex-critical.

**(2)** Suppose `H` is vertex-critical with `chi(H) = k` and some vertex `v`
has degree `d(v) <= k - 2`. By criticality `chi(H - v) <= k - 1`, so fix a
`(k-1)`-colouring of `H - v`. The `d(v) <= k-2` neighbours of `v` use at most
`k-2` of the `k-1` colours, so at least one colour is unused on the whole
neighbourhood; colour `v` with it to extend the colouring to `H`, giving
`chi(H) <= k-1`, contradicting `chi(H) = k`. Therefore every vertex has degree
`>= k-1`.

**Conclusion for k=5.** By (1) a 5-chromatic graph contains a 5-critical
(vertex-critical) subgraph `H'`, and by (2) `delta(H') >= 4`. Also `H'` has
`chi(H')=5`, so it is not 4-colourable.

## Verification method and result: CHECKED

The verifier is complete enumeration of **all simple graphs on up to 6
vertices** (33,866 graphs), computing the chromatic number exactly and checking
both parts directly. This is the permitted brute-force-at-small-size oracle,
**not** the method.

- **Oracle.** A fresh, independent SAT oracle `code/lib/critoracle.py`
  (general-colouring CNF, at-least-one + properness, Cadical153). It was
  cross-checked against the calibrated library oracle `lib.satcolor` (0
  disagreements over all 33,866 graphs) **and** against a naive independent
  colouring of the earlier counterexample — see the calibration trap below.
- **Part (2), every vertex-critical graph has delta >= k-1:** 90 vertex-critical
  graphs up to 6 vertices, **zero** with min degree < chi - 1.
- **Part (1), every graph contains a vertex-critical same-chi subgraph by
  greedy deletion:** **zero** failures over all 33,866 graphs.
- **Load-bearing conclusion:** 173 graphs with `chi >= 5` up to 6 vertices; all
  reduced by greedy vertex deletion to a `k`-critical subgraph with
  `delta >= k-1`, and for `k=5` the 5-critical subgraph always has
  `delta >= 4`. Zero failures.

**SZS-style verdict: this lemma is verified** as a complete check over all
finite simple graphs on at most 6 vertices for both parts, and the direct
conclusion holds on all 5-chromatic graphs up to 6 vertices.

```claim
id: sharp-critical-degree
statement: >
  (1) Every finite simple graph G with chi(G)=k contains a vertex-critical
  subgraph H with chi(H)=k (repeatedly delete a vertex while chi stays k).
  (2) Every vertex-critical graph H with chi(H)=k has minimum degree >= k-1.
  Conclusion: every 5-chromatic graph contains a 5-critical subgraph H' with
  delta(H') >= 4 and chi(H')=5 (not 4-colourable).
hypotheses: G, H finite simple graphs; chromatic number and vertex-criticality
  in the standard sense; enum up to 6 vertices for the finite check.
holds-here: YES — a minimal 5-chromatic unit-distance graph, if one exists, is
  5-critical, so delta >= 4: every vertex lies on >= 4 unit circles centred at
  the other graph vertices. This is exactly condition (a) of the kernel C_N.
status: checked (complete exact enumeration over all graphs on <= 6 vertices,
  via a fresh SAT oracle cross-validated against lib.satcolor, 0 mismatches)
bearing: the load-bearing degree step of the size-bound skeleton: it is what
  forces a 5-chromatic unit-distance graph to have min degree >= 4, so its
  vertex-critical subgraph lies in the finite kernel C_N (with the
  sharp-nbhd-local and sharp-kernel-4color steps). delta >= 4 is condition (a)
  of C_N.
anchor: research/backward/5chromatic-udg-min-size.md (gap sharp-critical-degree)
verification: code/verify_critical_min_degree2.py,
  code/verify_5critical_conclusion.py, code/out/verify_critical_min_degree2.txt,
  code/out/verify_5critical_conclusion.txt (both PASSED).
falsifies: a 5-critical graph with a degree-3 vertex; or a graph whose greedy
  vertex deletion cannot reach a vertex-critical same-chi subgraph. Neither
  occurs up to 6 vertices; the proof of (2) rules the first out universally.
```

## Why the check had to be redone — a discovered oracle bug

The first verification (using the existing `lib.coloring` backtracking oracle)
"failed". Investigation showed the failure was **not** a counterexample to the
lemma but a genuine soundness bug in `lib.coloring.chromatic_colorable`: it
pins `order[0]` (the highest-DSATUR vertex) to colour 0 with
`colors[order[0]] = 0`, yet the symmetry breaks inside the search loop test the
vertex index `0` explicitly (`v != 0 and 0 in adj[v]`). When `order[0] != 0`
this is inconsistent, so the search is incomplete and can return **False for a
graph that is k-colourable**. Repro: the 5-vertex graph
`[(0,1),(0,4),(1,2),(1,3)]` is genuinely 2-colourable (independent check
confirms), but `lib.coloring` reports it not-2-colourable.

Consequences for the workspace:

- The **False/UNSAT direction** of `lib.coloring` is **not reliable** (it can
  report a colourable graph as not colourable).
- The **True/SAT direction** (with a proper witness that `verify_coloring`
  re-checks) is still valid.
- This does **not** invalidate the calibration or the census-kernel result:
  those used `lib.satcolor` (Cadical CNF) as the primary engine, and
  `lib.satcolor` agrees with the fresh `critoracle` (0 mismatches). The census
  affirmations (every kernel member is 4-colourable) came with verified proper
  witnesses, so they stand. The `lib.coloring` "crosscheck" in the census was
  a second route whose positive answers were independently re-verified as
  proper; its negative answers should no longer be trusted, but the census
  made no negative claim on those.

The fresh verification for this lemma therefore used an independent, correct
SAT oracle and is the trustworthy record.

## What is proved vs verified

- The universal theorem (parts 1 and 2, all finite simple graphs) is proved by
  the two-line argument above (a proof, in the mathematical sense).
- Its truth for all graphs up to 6 vertices is verified exhaustively.
- The conclusion for 5-critical graphs is verified on all 173 graphs with
  chi >= 5 up to 6 vertices.
- The proposition is **not** machine-formalised in Lean here (a dependency on
  a graph-colouring library with the right statements was not set up this run);
  the row is `checked`, not `formalised`.

## Equivalence with the older `critical-minimum-degree` / `k-critical-minimum-degree` claims

`research/CLAIMS.md` already holds closely related rows:
`critical-minimum-degree` (asserted) and `k-critical-minimum-degree` (asserted).
This note upgrades the *sharp-critical-degree* gap (the version the skeleton
names) to `checked`, using the weaker vertex-critical hypothesis, and should be
treated as the verified instance of those asserted-by-source rows for finite
graphs up to 6 vertices. The classical (edge-critical) theorem itself is still
asserted-by-source for the fully general statement.
