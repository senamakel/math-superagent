# Colour-critical graph structure and Hajós construction

**Subject:** The structural theory of `k`-critical graphs — the load-bearing
machinery for the run's `R-size-bound` direction, which argues that a minimal
`5`-chromatic unit-distance graph has minimum degree at least `4`, hence enough
unit edges to bound it away from small sizes.

## Sources (retrieved via `read_sources`; direct download blocked)

- B. Braun, J. Vega, *Hajós-Type Constructions and Neighborhood Complexes*,
  SIAM J. Discrete Math. 34 (2020), DOI 10.1137/19m1243476.
- M. Krivelevich, *An improved bound on the minimal number of edges in
  color-critical graphs*, Electron. J. Combin. 4 (1997), DOI 10.37236/1342.
- C. Luo, J. Ma, T. Yang, *On the maximum number of edges in k-critical
  graphs*, arXiv:2301.01656 (2023).
- Underlying: G. Hajós (1961) *Über eine Konstruktion nicht n-färbbarer
  Graphen* (Hajós construction); Gallai (1963), Dirac, Toft foundational work.

## What it establishes

### k-critical graphs
`G` is **k-critical** if `chi(G) = k` but every proper subgraph (equivalently,
every proper edge/vertex deletion) has `chi < k`. Facts:

- **Every vertex of a k-critical graph has degree at least k-1** (if some vertex
  had degree `<= k-2`, a `(k-1)`-colouring of `G - v` would extend to `v`, since
  at most `k-2` colours appear on its neighbours). Hence `|E(G)| >= (k-1)/2 * |V|`.
- Low-degree vertex subgraph `L(G)` = vertices of degree exactly `k-1`
  (a k-Gallai forest), high-degree `H(G)` = degree `>= k`. Gallai's structure
  improves the edge bound to `|E(G)| >= ((k-1)/2 + (k-3)/(2(k^2-3))) |V|`;
  Krivelevich improves the constant further to `(k-3)/(2(k^2-2k-1))`.
- Upper bound (Luo–Ma–Yang, after Stiebitz 1987): a dense n-vertex k-critical
  graph has fewer edges than the balanced complete (k-2)-partite graph for
  large n. The Toft graph is the best-known dense 4-critical example, with
  ~(1/16)n^2 + (1/2)n edges.

### The Hajós construction
Hajós (1961): a graph has chromatic number at least `k` **iff** it contains a
**k-constructible** subgraph, i.e. one obtainable from `K_k` by repeatedly
applying:
- **Hajós merge** (Hajós sum): given two graphs with edges `xy` and `x'y'`,
  delete those two edges, identify `x` with `x'`, and add edge `y y'`;
- **vertex identification** of non-adjacent vertices.
Urquhart sharpened this: every k-chromatic graph is constructible with all
intermediate graphs of chromatic number `<= k` (Ore merge); and there exist
`k`-critical graphs (k >= 4) with no Hajós sequence staying k-critical
throughout (Jensen–Royle; Braun–Vega).

## Why it matters here

- The `R-size-bound` direction (`GOAL.md`, `research/backward/5chromatic-size-lower-bound.md`)
  argues: a minimal 5-chromatic unit-distance graph would contain a 5-critical
  subgraph, whose vertices all have degree at least 4, so it must have `>= 2n`
  unit edges. This source is the precise, cited statement of that min-degree
  fact (degree `>= k-1` for k-critical) and its edge-count refinements.
- It also records the constructive framing against which spindling is an
  instance: the 7-vertex spindle is a 4-critical unit-distance graph, and
  higher-chromatic candidates must likewise arise from iterated gluings of
  critical graphs — the same structural accumulation problem the Minkowski-sum
  route faces.
- Hajós gives the general "how to build k-chromatic graphs" classification, but
  it is **not** unit-distance-preserving in general: the known operations
  (merges, identifications) do not obviously keep all edges at length 1. That
  divergence is precisely why the run needs its own exact-arithmetic
  construction engine rather than being able to import Hajós directly.

## Basis and status

- Statements = sourced (retrieved verbatim). Classical, standard results
  (Hajós 1961, Gallai 1963, Dirac; modern refinements Krivelevich 1997,
  Luo–Ma–Yang 2023).
- Not re-verified computationally here (general graph theory); the run's own
  exact oracle verifies the unit-distance extension.

## Claim block

```claim
id: k-critical-minimum-degree
statement: Every k-critical graph has minimum degree at least k-1, hence at
  least ((k-1)/2)n edges on n vertices; if a graph has chromatic number at
  least k it contains a k-critical subgraph. Consequently any 5-chromatic
  graph contains a 5-critical subgraph with minimum degree at least 4 and at
  least 2n unit edges.
hypotheses: G a finite simple graph; k-critical means chi=k and every proper
  subgraph is (k-1)-colourable.
holds-here: YES — the run's target (a 5-chromatic unit-distance graph) would
  contain a 5-critical subgraph, so the minimum-degree and edge-count lower
  bounds apply verbatim to unit-distance graphs.
status: asserted-by-source (classical: degree >= k-1 follows from the
  k-colouring-extension argument; Hajós; Gallai; Krivelevich/Luo-Ma-Yang for
  refinements).
bearing: the structural backbone of the R-size-bound direction — a minimal
  5-chromatic UDG must have all degrees >= 4, which forces a minimum edge
  density (>= 2n) that, combined with the unit-distance O(n^{4/3}) upper bound
  and the fact that each unit-distance neighbourhood is a unit-circle chord-1
  pattern, bounds how small such a graph can be.
anchor: research/sources/colour-critical-hajos-construction.md
falsifies: a 5-chromatic graph with a vertex of degree < 4 — would contradict
  the classical k-critical min-degree fact; none exists (it is a proof-level
  truth for general graphs, not a conjecture).
```
