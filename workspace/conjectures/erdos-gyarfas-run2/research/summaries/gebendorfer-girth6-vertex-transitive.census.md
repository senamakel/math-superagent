# Gebendorfer 2026 — E–G conjecture for cubic vertex-transitive bipartite girth-6 graphs

Source: J. J. Gebendorfer, "The Erdős–Gyárfás Conjecture for Cubic
Vertex-Transitive Bipartite Graphs of Girth Six: A Complete Census Verification
with Structural Analysis", Zenodo 18505377 (2026-02-06), doi:10.5281/zenodo.18505377.
Full text: `research/sources/gebendorfer-girth6-vertex-transitive.census.full.md`
(41 KB; PDF). arXiv: none indexed.

## What it establishes (computational + structural)

- **Theorem 1.2 (Main census)**: every cubic bipartite vertex-transitive graph
  of girth 6 in the CVT census (Potočnik–Spiga–Verret, all such graphs up to
  1280 vertices) contains a cycle of length a power of two; specifically
  `kmin(G) ≤ 5`, i.e. an 8-, 16-, or 32-cycle.
- **Dyadic trichotomy** (58,438 graphs): 55,556 have `kmin = 4` (a 16-cycle,
  but no 8-cycle); 2,868 have `kmin = 3` (an 8-cycle); exactly **14** have
  `kmin = 5` (a 32-cycle but **no** 8- or 16-cycle).
- The 14 extremal cases are precisely the PV(b) and PV(c) truncations
  (13 type PV(b), 1 type PV(c)) in the census. For each, `C8 = C16 = ∅`
  is proven computationally, with an explicit 32-cycle witness.
- Structural apparatus: vertex-transitive cycle-propagation (Lemma 3.1: in a
  vertex-transitive graph, if a simple L-cycle exists then every vertex lies on
  an L-cycle); matching-edge decompositions with a balance equation and port
  minima that exclude short cycles.

## What it means for this run

A **new restricted class settled** for the E–G conjecture: the cubic
**bipartite vertex-transitive** girth-6 class up to 1280 vertices. It is far
from `min-degree-3` general (vertex-transitive + cubic + bipartite + girth 6 is
a very tight symmetric class), but it is a genuine addition to the settled-class
inventory and shows 32-cycles can be the *only* power-of-two cycle while 8 and
16 are both absent — the same behaviour Bensmail's construction exhibits
(arbitrarily large cubic graphs whose power-of-two cycles are 4-only or 8-only).
For the run it is evidence that a structural argument forcing 4, 8, or 16 at
min-degree 3 must handle the case where only larger powers survive.

```claim
id: gebendorfer-cvt-g6-census
statement: Every cubic bipartite vertex-transitive graph of girth 6 with at most 1280 vertices contains a cycle of length 8, 16, or 32 (kmin <= 5).
hypotheses: cubic, bipartite, vertex-transitive, girth 6, |V| <= 1280
holds-here: yes (a settled restricted class, computationally verified over the complete PSV census)
status: verified-numerically (complete census up to 1280 vertices; not independently re-run here)
bearing: new settled restricted class; extremal instances have C8=C16=empty with a 32-cycle witness
anchor: research/sources/gebendorfer-girth6-vertex-transitive.census.full.md
contradicts: none
```

Caveat: both this and its companion record come from a single-author 2026
preprint (same author as the claimed full proof of E–G that the library holds
as unverified). The census claim is a direct computation over an existing
census, so it is more trustable than the full-proof abstract, but it is not
independently re-run here.
