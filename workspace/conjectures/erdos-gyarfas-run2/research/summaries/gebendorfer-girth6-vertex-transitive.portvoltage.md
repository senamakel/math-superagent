# Gebendorfer 2026 — power-of-two cycles in cubic bipartite VT girth-6 graphs (port-voltage proof)

Source: J. J. Gebendorfer, "Power-of-Two Cycles in Cubic Bipartite
Vertex-Transitive Graphs of Girth Six", Zenodo 18526153 (2026-02-08 v3),
doi:10.5281/zenodo.18526153. Full text:
`research/sources/gebendorfer-girth6-vertex-transitive.portvoltage.full.md`
(55 KB; PDF).

This is the structural companion to the census record above; both cover the
same graph class and disagree on no claim. This one carries the proof mechanism.

## Theorem statements

- **Theorem 2.1 (main, census version)**: every cubic bipartite vertex-transitive
  graph of girth 6 with ≤ 1280 vertices has a cycle of length `2^k`, `k ∈ {3,4,5}`
  (8, 16, or 32).
- **Trichotomy** (Thm 2.2): `kmin=3` graphs have an 8-cycle; `kmin=4` graphs
  have a 16-cycle but no 8-cycle; exactly 14 graphs have `kmin=5` (a 32-cycle,
  no 8- or 16-cycle) — the PV(b)/PV(c) truncations.
- **Thm 2.4**: a PV(b) truncation with ring length ℓ ≥ 7, or a PV(c) truncation
  with ℓ = 6, with simplicial quotient triangulation, has **no** 8-cycle.
- **Prop 6.2**: in the PSV census, the 14 extremals satisfy `C8 = C16 = ∅`.

## Method (structural)

Permutation–voltage framework decomposing a CVT-G6 graph into an ℓ-cycle "ring"
factor and an ℓ-regular quotient endowed with a cyclic voltage labelling.
Corner-cost / isoperimetric / face-shift lemmas (4.1, 4.4, 4.5, 5.1) exclude
8-cycles and partially exclude 16-cycles by showing no balanced closed walk of
the right cost projects. For the 14 extremals, the mechanism is different: each
is the truncation of an orientable regular map `{3,ℓ}_r`, and a canonical
"ground-state" walk in the quotient lifts to a simple 32-cycle (Thm 2.6 mixed-hole
certificates: a word over generators of weight 32 equals the identity in Aut(M)).

## What it means for this run

Same settled class as the census record. The structural blocking of 8- and
16-cycles in the extremals is a concrete demonstration of *why* short
power-of-two cycles (8, 16) can all fail while a 32-cycle still exists — the
balance/corner-cost machinery is the shape of what a proof for the general
min-degree-3 case would need. Not portable to general min-degree 3 (the
framework is heavily vertex-transitivity-specific), so it is a settled-class
addition, not a new general method.

```claim
id: gebendorfer-cvt-g6-extremals
statement: The 14 cubic bipartite vertex-transitive girth-6 graphs with kmin=5 (the PV(b)/PV(c) truncations) have C8=C16=empty and contain an explicit 32-cycle; hence a 32-cycle can be the only power-of-two cycle in a settled-class graph.
hypotheses: cubic, bipartite, vertex-transitive, girth 6, PSV census <= 1280 vertices
holds-here: yes
status: asserted (single-author 2026 preprint; structural exclusions + census support, not independently re-run here)
bearing: sharp example that larger-only powers (32) can survive when 8 and 16 are both absent — parallels Bensmail's near-counterexample behaviour
anchor: research/sources/gebendorfer-girth6-vertex-transitive.portvoltage.full.md
```
