# Cranston–Rabern: edge lower bounds for list-critical graphs, via discharging

**Subject:** Discharging as the method for edge-count lower bounds on
k-critical graphs, explicitly not relying on planarity or the four-colour
theorem. This is the source the discharging approach
(`research/approaches/discharging-minimal-counterexample.md`) cited for the
mechanism correction: the viable discharging for a non-planar 5-critical graph
is the Gallai-forest route (Kostochka–Yancey / Cranston–Rabern), not Euler's
formula on a planar embedding.

## Source
- D. W. Cranston, L. Rabern, *Edge lower bounds for list critical graphs, via
  discharging*, Electron. J. Combin. 24(1) (2017) #P1.42; arXiv:1602.02589
  (2016 preprint). Retrieved via server-side retrieval (`read_sources`); the
  full text is blocked at this run's network boundary.
- Source URL: https://arxiv.org/abs/1602.02589

## Exact statements

- The paper improves the best known lower bound on the number of edges in a
  **k-list-critical** graph, and the k-AT-critical / online list-critical
  variants, **using the discharging method** where the preceding work
  (Kierstead–Rabern) used a global averaging argument.
- Model result (average-degree form, k-AT-critical, G != K_k):
  - `k >= 7`:  `d(G) >= k-1 + (k-3)(2k-5)/(k^3 + k^2 - 15k + 15)`
  - `k in {5,6}`: `d(G) >= k-1 + (k-3)(2k-5)/(k^3 + 2k^2 - 18k + 15)`
- Builds on Gallai's structure theorem (`d(G) > k-1 + (k-3)/(k^2-3)` for
  k-AT-critical G, G != K_k) and Kostochka–Yancey's foundational edge bounds.

## Method and its significance for THIS run

The discharging argument: each vertex `v` has initial charge `d_G(v)`. Each
`k`-vertex gives charge `(k-1)/(k^2-3)` to each of its `(k-1)`-neighbours; the
components of the subgraph induced by `(k-1)`-vertices share charge; a new
measure on the average degree of Gallai trees is the key refinement. The
auxiliary bipartite graph `B_k(G)` is shown 2-degenerate, controlling how much
charge k-vertices can distribute.

**The decisive fact for the run (the mechanism correction):** this is *non-
planar* discharging. It does not use Euler's formula or a planar embedding —
which matters because a 5-chromatic graph is necessarily non-planar (four-
colour theorem). The approach file records the correction: the viable
discharging on the minimal 5-critical unit-distance graph is the Gallai-forest
route this paper exemplifies, not the "face-angle/Euler" mechanism the original
approach sketch wrongly assumed.

## Why it matters here
The size-bound rung's analytical route needs the edge-count lower bound on a
5-critical graph; the discharging literature provides the technique and the
Kostochka–Yancey bound is the sharpest result of that form. Cranston–Rabern
supplies the *methodological* warrant that discharging is legitimate on
non-planar k-critical graphs, which is exactly the objection the approach file
answered with its `caveat`. The run's own computation showed the resulting edge
bounds still cannot extend the size bound past n=9, but that is a fact about the
*unit-distance density* ceiling, not about discharging.

## Basis and status
- Statements retrieved verbatim from the abstract/result bullets via
  server-side retrieval.
- Not machine-re-derived here (general graph theory; the k-columns table of
  Gallai / Kriv / KS / KY / KR bounds is quoted from the source).

## Claim block
```claim
id: cranston-rabern-2016-list-critical-discharging
statement: Discharging yields improved edge-count lower bounds on k-list-
  critical graphs (and k-AT-critical / online list-critical variants), e.g.
  d(G) >= k-1 + (k-3)(2k-5)/(k^3 + k^2 - 15k + 15) for k >= 7 (average degree),
  and the method does NOT rely on planarity or the four-colour theorem.
hypotheses: G finite list-critical / AT-critical graph, k >= 5, following the
  Gallai-forest (k-Gallai tree) structural decomposition.
holds-here: YES methodological — a minimal 5-chromatic unit-distance graph is
  non-planar, and this is the published proof that discharging still applies;
  the edge bounds tighten the size-bound rung's edge-lower-bound ingredient.
status: asserted-by-source (Cranston–Rabern 2017, arXiv:1602.02589, EJC).
bearing: the methodological warrant for non-planar discharging on the minimal
  5-critical UDG (Gallai-forest route), and the edge-bound refinements on the
  Kostochka–Yancey spine.
anchor: research/sources/cranston-rabern-2016-list-critical-discharging.md
falsifies: a discharging proof for k-critical graphs that turns out to require
  planarity after all — contradicted by this paper's explicit non-planar
  derivation (and by Kostochka–Yancey).
```
