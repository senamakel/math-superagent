# Colour-critical graphs: the structural backbone of the size-bound rung

**Subject:** The graph-colouring structural theory that the run's reachable
deliverable — "every unit-distance graph on at most N vertices is 4-colourable,
for the largest N provable" — rests on. The blueprint's `S-critical-degree`
lemma (every k-critical graph has minimum degree >= k-1) and `S-nbhd-bound`
(unit-distance neighbourhood structure) are the two structural inputs; this
source fixes the classical theory behind the first.

**Source URLs (retrieved via search passages, not full text):**
- A. Kostochka, *Color-critical graphs and hypergraphs with few edges: a
  survey*, in *Graphs and Discovery* (DIMACS 2004; Springer, 2006), DOI
  10.1007/978-3-540-32439-3_9.
- Toft, *Constructive methods in the theory of colour-critical graphs*,
  Discrete Math. (1991), DOI 10.1016/0012-365X(89)90210-0 and the colour
  criticals survey.

## Exact statements

**Definition.** A graph `G` is **k-critical** if `chi(G) = k` and every proper
proper subgraph has chromatic number < k. (Every `(k-1)`-colouring obstruction
of G is witnessed minimally by a k-critical subgraph.)

**Theorem (critical minimum degree).** If `G` is `k`-critical then
`delta(G) >= k - 1`.

Proof: if vertex `v` had degree `<= k-2`, a `(k-1)`-colouring of `G - v`
(which exists, since G-v is a proper subgraph and G is k-critical) could be
extended to `v` by choosing a colour unused among its `<= k-2` neighbours —
contradiction. Applied with k=5: **every minimal non-4-colourable (5-critical)
graph has minimum degree at least 4.**

**Corollary for the run.** Any 5-chromatic (minimal) unit-distance graph has
every vertex on at least 4 unit circles centred at other graph vertices, all
edges at distance exactly 1. Combined with the geometric fact that a vertex's
unit-distance neighbours lie on a circle and pairwise edges among them are
chords of length 1 subtending 60 degrees (an equilateral-triangle chord
structure), this forces strong local rigidity — the raw material for proving
4-colourability of small graphs.

**Gallai's structure (survey tier).** In a k-critical graph, vertices of degree
exactly k-1 ("low" vertices) induce a disjoint union of Gallai trees (blocks
that are complete graphs or odd cycles). This is the finer structure that
`S-universe-4color` can exploit to enumerate the small candidate universe.

## Why this matters

This is *technique*, not answer: it gives the theorem that every graph with a
vertex of degree <= 3 is 4-colourable only *if it is not 5-chromatic*, and the
min-degree >= 4 + neighbourhood-on-a-circle structure that bounds how a small
5-chromatic unit-distance graph could look. The size-bound rung reduces
"prove all unit-distance graphs on <= N vertices are 4-colourable" to a finite
enumeration over exactly this constrained universe. The bound N is what the run
extends by attacking the enumeration, and this theorem is why the enumeration is
over graphs with min-degree >= 4 rather than all graphs.

## Basis and status

- Statement and proof of `delta(k-critical) >= k-1` are elementary and
  standard; corroborated across sources. The Gallai-tree structure is the
  survey-tier citation.
- Not re-derived as a Lean/program artifact here — recorded as the sourced
  structural input the size-bound rung is built on.

## Claim block

```claim
id: critical-minimum-degree
statement: Every k-critical graph has minimum degree at least k-1; in particular
  every 5-critical (minimal non-4-colourable) graph has delta >= 4.
hypotheses: G a finite simple graph, k-critical (chi(G)=k, every proper
  subgraph < k).
holds-here: YES — a minimal 5-chromatic unit-distance graph, if one exists, is
  5-critical, so every vertex has degree >= 4 and hence lies on >= 4 unit
  circles centred at other vertices.
status: asserted-by-source (classical; declared in the degree survey and the
  blueprint's S-critical-degree row).
bearing: backbone of the size-bound rung: the universe to enumerate is graphs
  with min-degree >= 4 and the unit-distance neighbourhood constraint, and the
  purpose is proving every such small graph is 4-colourable.
anchor: research/sources/colour-critical-graphs-structure.md
falsifies: a 5-critical unit-distance graph with a degree-3 vertex — impossible
  by the theorem (a degree-3 vertex would extend any 4-colouring of the rest),
  and the theorem classifies that impossibility exactly.
```
