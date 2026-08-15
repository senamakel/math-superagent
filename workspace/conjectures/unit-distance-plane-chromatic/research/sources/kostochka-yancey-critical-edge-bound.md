# Edge lower bounds for k-critical and clique-free critical graphs (Kostochka–Yancey and refinements)

**Subject:** The sharp general lower bound on the number of edges of a
k-critical graph, and what (if anything) is known for the K4-free 5-critical
restriction. This is the argument-tier source for the `clique-free-critical-size-bound`
approach (`research/approaches/clique-free-critical-size-bound.md`), whose
entire first step is to pin such a bound.

## Source (exact statements retrieved server-side; full text not held)

Retrieved via the server-side search/retrieval layer:
- **A. Kostochka, M. Yancey,** "Ore's conjecture on color-critical graphs is
  almost true", J. Combin. Theory Ser. B 109 (2014) 73–101;
  https://doi.org/10.48550/arxiv.1209.1050.
- **W. Gao, L. Postle,** "On the Minimal Edge Density of K4-free 6-critical
  Graphs", arXiv:1811.02940 (2018) — the same program's structural tools for
  the cases 6 ≤ k ≤ 32, with the K4-free 5-critical case left partial.
- **R. Gould, V. Larsen, L. Postle,** "Structure in sparse k-critical graphs",
  arXiv:2107.00976 (2021).
- **Kostochka, Yancey,** "Ore's conjecture for k=4 and Grötzsch's Theorem",
  Combinatorica 34 (2014) 323–329; https://doi.org/10.1007/s00493-014-3020-x.

## What the sources establish (exact statements)

**General k-critical edge bound (Kostochka–Yancey).** For every k ≥ 4, if G is
k-critical on n vertices then
`|E(G)| ≥ [ (k+1)(k−2)n − k(k−3) ] / [2(k−1)]`.
For **k = 5** this is `|E(G)| ≥ (9n − 5)/4`. The bound is asymptotically
tight, and equality is characterized by the class of **k-Ore graphs** (which
contain many large cliques). Ore's conjecture (the step function
`f_k(n + k−1) = f_k(n) + (k−1)(k−2)/2`) follows from the asymptotics.
Commonly cited equivalent form: `|E(G)| ≥ (k/2 − 1/(k−1))·n − k(k−3)/(2(k−1))`.

**K4-free / clique-free refinements (the key negative datum for this approach).**
- There is **no established closed-form lower bound** for the edge count of a
  K4-free 5-critical graph that strictly beats `(9n−5)/4`. The K4-free
  refinement is an explicitly cited **open/partial** problem: Gao–Postle's
  program ("The Minimal Edge Density of K4-free 6-critical Graphs") covers the
  indices 6 ≤ k ≤ 32 with structural tools, and the K4-free 5-critical case is
  left without a sharp closed form in these sources.
- The known strict strengthenings are for the *stronger* triangle-free (K3-free)
  restriction, not K4-free: **Postle** proved that a 5-critical graph with no
  K3 satisfies `|E(G)| ≥ (9/4 + 1/84)·n − 5/4` (i.e. ε = 1/84). Triangle-free is
  strictly stronger than K4-free, so this does not give a K4-free bound.
- For k ≥ 33, Kostochka–Yancey/Gould–Larsen–Postle give `ε_k > 0` with a
  K_{k}−-free k-critical graph satisfying
  `|E(G)| ≥ (k(k−3)/(2(k−1)))·n + ε_k·n − o(n)` — asymptotics only, and only
  for large k; it does not apply to the k=5, K4-free case at the small n this
  run cares about.

## Bearing on this problem

This is precisely the ingredient the `clique-free-critical-size-bound` approach
needs and currently lacks. The finding:

1. **The general bound** `f_5(n) ≥ (9n−5)/4` is confirmed (Kostochka–Yancey).
   The run's killed `discharging-minimal-counterexample` line already crossed
   this against the SST ceiling `u_2(n) ≤ C n^{4/3}` and it first stops forcing
   a contradiction at n = 10 (even with C=1), giving N ≤ 9 — below the census's
   n = 11. This is consistent with the available sources.
2. **The hoped-for K4-free 5-critical bound does not exist in closed form.**
   The approach's premise — that forbidding K4 (the plane's clique number ω ≤ 3
   makes a 5-critical UDG K4-free) sharpens the edge lower bound enough to push
   N past 9 — is NOT supported by the literature: the only strict sharpenings
   known are triangle-free (Postle, ε=1/84), a strictly stronger restriction
   that does not apply here (UDGs contain equilateral triangles). Without a
   sharp K4-free bound there is no way to beat the killed line's N = 9 by this
   route.
3. **Net effect:** this source RETIRES (as a literature gap) the specific
   "sharper K4-free lower bound" mechanism of the `clique-free-critical-size-bound`
   approach, unless an agent can *prove* a K4-free 5-critical edge bound
   themselves. The approach note records `speculation: whether the K4-free
   refinement of Kostochka–Yancey is strong enough to beat N = 9`; the
   literature answer is that no such sharp refinement is known/established, so
   the approach should be treated as blocked on a missing theorem rather than
   waiting for a lookup.

## Sourced claim

```claim
id: kostochka-yancey-critical-edge-bound
statement: >
  For every k >= 4 and every k-critical graph G on n vertices,
  |E(G)| >= [(k+1)(k-2)n - k(k-3)] / [2(k-1)]. For k = 5: |E(G)| >= (9n-5)/4.
  The bound is asymptotically tight, with equality characterized by the k-Ore
  graphs. There is NO established closed-form K4-free-5-critical edge bound
  strictly stronger than (9n-5)/4; the known strict strengthenings are for the
  triangle-free (K3-free) restriction (Postle: 5-critical, triangle-free,
  |E(G)| >= (9/4 + 1/84)n - 5/4), which is strictly stronger than K4-free and
  does not apply to unit-distance graphs (they contain equilateral triangles).
hypotheses: G k-critical (every proper subgraph (k-1)-colourable), k >= 4,
  finite simple graph.
holds-here: yes for the general bound (a 5-critical UDG on n vertices has
  >= (9n-5)/4 unit edges). The hoped-for K4-free sharpenings do NOT hold here
  as known results: the only strict one (Postle) needs triangle-freeness, which
  a UDG need not satisfy.
status: asserted (retrieved server-side from Kostochka–Yancey and Gao–Postle;
  the general bound is not machine-checked here but is classical). The specific
  K4-free gap is a *known unknown* recorded by the sources' own program.
bearing: retires the "sharper K4-free lower bound" premise of the
  clique-free-critical-size-bound approach as an unavailable lookup; the
  general bound (9n-5)/4 confirms the killed discharging line's N <= 9. The
  size-bound route must instead find a sharp K4-free 5-critical bound by proof,
  or abandon this mechanism.
anchor: research/sources/kostochka-yancey-critical-edge-bound.md
falsifies: a source giving a sharp closed-form K4-free 5-critical edge bound
  strictly above (9n-5)/4 would reopen the approach; a 5-critical UDG with
  fewer than (9n-5)/4 edges would falsify the general bound.
```

## What could not be obtained

Full verbatim publisher texts (JCTB Kostochka–Yancey, the arXiv Gao–Postle
body) are blocked at the network boundary; exact statements above were
retrieved server-side. The key negative datum — absence of a sharp K4-free
5-critical edge bound — is established from the sources' own framing (the open
program for 6 ≤ k ≤ 32 with the 5-critical case left partial, and only the
stronger triangle-free case solved). Recorded so nobody re-fetches these hosts.
