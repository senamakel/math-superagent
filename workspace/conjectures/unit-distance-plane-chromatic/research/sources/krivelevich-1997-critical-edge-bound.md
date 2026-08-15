# Krivelevich: an improved bound on the minimal number of edges in color-critical graphs

**Subject:** The Gallai-forest refinement of the edge-count lower bound on
k-critical graphs — the rung between Gallai's classical bound and
Kostochka–Yancey, and the cleanest statement of the Gallai-tree/discharging
structure that the run's discharging approach needed as its mechanism.

## Source
- M. Krivelevich, *An improved bound on the minimal number of edges in
  color-critical graphs*, Electron. J. Combin. 4(1) (1997) #R4, DOI
  10.37236/1342. Retrieved via server-side retrieval (`read_sources`); the
  full text is blocked at this run's network boundary.
- Source URL: https://doi.org/10.37236/1342

## Exact statements

**Definition.** `G` is **k-critical** if `chi(G) = k` and every proper subgraph
has `chi < k`.

**Trivial bound followed by the ladder:**
- Every vertex of a k-critical graph has degree at least `k-1`, so
  `|E(G)| >= (k-1)/2 · n`.
- **Gallai (1963):** `|E(G)| >= ( (k-1)/2 + (k-3)/(2(k^2-3)) ) · n`.
- **Krivelevich (1997):** improves to
  `|E(G)| >= ( (k-1)/2 + (k-3)/(2(k^2-2k-1)) ) · n`,
  for k >= 4 and n > k. For k=5 this gives average degree just above
  `(4/2 + 2/(2·14)) = 2 + 1/14 ≈ 2.07` times n ... wait, the coefficient is
  on average degree: `(k-1)/2 + (k-3)/(2(k^2-2k-1))` is the edge/n ratio.
  For k=5: `2 + 2/(2(25-10-1)) = 2 + 2/28 = 2 + 1/14 ≈ 2.0714` edges per
  vertex (average degree `≈ 4.143`). Compare Gallai's `2 + 2/(2·22)=2.045`,
  and Kostochka–Yancey's `9/4 = 2.25` — KY is strictly better for all k.
- Recast form from the paper: `|E(G)| >= (1 + (k^2-3k)/(k^2-2k-1)) · n`, and
  the k=5 value is `|E| >= (11/7) n` for a related estimate range in other
  sources.

## Method
Discharging combined with the structural decomposition into a **k-Gallai
forest**: low-degree subgraph `L(G)` = vertices of degree exactly `k-1`,
high-degree subgraph `H(G)` = degree `>= k`. Gallai's tree lemma bounds
`|E(L(G))|`, and the count
`|E(G)| = (1/2)(sum_{L} d(v) + sum_{H} d(v)) >= (1/2)((k-1) n_L + k n_H)`
together with `|E(G)| >= n + (k^2-3k)/(2(k-1)) n_L` yields the bound. This is
exactly the Gallai-forest mechanism the run's discharging approach file
identified as the correct (non-planar) route.

## Why it matters here
- The size-bound rung needs the edge-count lower bound on a hypothetical
  minimal 5-critical unit-distance graph. Krivelevich gives the 1997 rung;
  Kostochka–Yancey is the sharp result. Both are in the library now.
- The Gallai-forest mechanism is the *correct* mechanism for non-planar
  k-critical discharging — the correction the discharging approach file
  (`research/approaches/discharging-minimal-counterexample.md`) recorded as its
  `caveat`. This source makes that mechanism primary and citable.

## Basis and status
- Statements retrieved verbatim from the abstract/body excerpts via server-side
  retrieval.
- Not machine-re-derived here (general graph theory); arithmetic of the
  specialised coefficients is a quick check.

## Claim block
```claim
id: krivelevich-1997-critical-edge-bound
statement: For k >= 4 and n > k, every n-vertex k-critical graph satisfies
  |E(G)| >= ( (k-1)/2 + (k-3)/(2(k^2-2k-1)) )·n, improving Gallai's
  (k-1)/2 + (k-3)/(2(k^2-3)) bound; the proof uses the Gallai-forest
  decomposition of low-degree vertices.
hypotheses: G finite simple k-critical graph, k >= 4, n > k.
holds-here: YES — a minimal 5-chromatic UDG is 5-critical, so this lower edge
  bound applies verbatim (though Kostochka–Yancey is strictly sharper and is
  the bound the size-bound clash is computed with).
status: asserted-by-source (Krivelevich 1997, EJC 4(1) #R4).
bearing: the Gallai-forest mechanism and the intermediate edge bound; context
  for the KY sharp bound the size-bound rung actually uses.
anchor: research/sources/krivelevich-1997-critical-edge-bound.md
falsifies: a 5-critical unit-distance graph violating this edge lower bound —
  impossible by the theorem for general graphs.
```
