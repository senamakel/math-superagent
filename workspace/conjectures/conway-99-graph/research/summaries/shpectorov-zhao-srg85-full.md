# Shpectorov & Zhao, "Strongly regular graphs with parameters (85,14,3,2) do not exist" (arXiv:2504.02449) — FULL TEXT

<!-- source: https://arxiv.org/pdf/2504.02449 | full text at research/sources/shpectorov-zhao-srg85.full.md -->

## What the paper proves

**Theorem 1.1: There is no srg(85,14,3,2).** This is the second-smallest
unresolved feasible parameter set among v ≤ 100 (smallest being the Conway
(99,14,1,2), which remains open), resolved Feb-2025. Among v ≤ 100, nine
parameter sets were unresolved; this resolves the (85,14,3,2) one, leaving
(99,14,1,2) and others.

## The method — the attack template that worked

This is the direct, successful model for the type of attack GOAL.md endorses for
(99,14,1,2). Step by step:

1. **Fix a vertex x; the local subgraph G1(x) is cubic of order 14.** Use the
   known classification of cubic graphs on 14 vertices: only 39 "good" cubic
   graphs can occur (Lemma 3.2, Prop 3.2), restricted by a combinatorial lemma
   (Lemma 3.1: two non-adjacent vertices of G1(x) have at most one common
   neighbour in G1(x)).
   - *Contrast with 99:* for (99,14,1,2), G1(x) is forced to be 7K₂ (7 disjoint
     edges) — a much smaller, rigid local shape. So the 14-vertex local graph
     is *easier* for 99.

2. **Every edge lies in a maximal 3-clique** (Prop 3.4). For λ=3, a 3-clique
   can extend in a controlled way. Fix a maximal 3-clique Q = {x,y,z}.

3. **Segment model.** For each edge yz of the cubic local graph not in a
   triangle, delete it: the "segment" S = subgraph on (local graph − yz) with
   two *handles* (the neighbour-pairs). Up to isomorphism there are only
   **478 segments**: 19/78/78/303 of four types (Prop 4.3). This is the
   finite, enumerable search space. Lemma 4.4/4.6 give the core structure
   (6 vertices if handle is an edge, 4 if non-edge).

4. **Euclidean representation.** Embed the graph in R^34 (the eigenspace of the
   eigenvalue 4, dimension 34 = v−1−50). Lemma 5.1: sum over the 14 neighbours
   of x equals 4x. Building the 34-dim representation of the three vertices of
   Q, then constraining segments around them (Lemma 5.3: Sx ∩ Sy is a handle),
   reduces to a finite case analysis on the 478 segments and their interactions
   in triples.

5. **Verification by complete enumeration.** All combinations of 2 and 3
   segments around Q are enumerated and checked against (a) the λ=3, μ=2
   combinatorial conditions and (b) the Euclidean/linear-algebra conditions.
   Every case yields a contradiction. The paper states the enumeration is
   exhaustive (finite search space of segments/types) — the exhaustiveness
   argument is an explicit finite case analysis, and the numbers (478 segments,
   types) are the stated space.

## Why this belongs in the 99 library

- It is the **closest successful nonexistence proof by local-configuration
  enumeration** to the (99,14,1,2) case: same k=14, same μ=2, only λ differs
  (3 vs 1). The mechanism is NOT spectral integrality (which is why it could
  not have been refuted on arrival) — it is a genuine combinatorial +
  Euclidean-representation case analysis.
- For (99,14,1,2), the local graph is 7K₂ (forced), so the analogous segment
  count is far smaller than 478. The natural analogue: take two triangles; the
  parameter n_3 (Reimbayev) counts pairs of triangles joined by two edges; the
  union of two intersecting triangles and its forced extensions is exactly the
  segment-like local configuration to exhaust.
- It shows the "fix a small forced sub-configuration, prove by complete search
  it does not extend" attack CAN close a k=14, μ=2 case. Whether it transfers
  to 99 is open, but the template is now in the library.

## Status / caution
- Preprint (arXiv:2504.02449, April 2025), **not yet peer-reviewed** at capture;
  the enumeration is claimed complete with stated space (478 segments, 4 types),
  but the run has not re-verified it.
- The Euclidean-representation part (Sx projections in R^34) is the part a naive
  replica could get wrong; the combinatorial segment counts are the checkable
  core.

## Connection to the run's geometry leads
- The 478 segments arise from cubic local graphs; for (99,14,1,2) the local
  graph 7K₂ gives a much smaller segment/extension space — the analogue
  enumeration is smaller, which is why it is worth attempting at all.
- The paper's "every edge in a maximal 3-clique" + segment decomposition is the
  structural analogue of the Reimbayev n_3 pivot (pairs of triangles sharing an
  edge). Both point at the union-of-intersecting-triangles configuration that
  GOAL.md names.

```claim
id: shpectorov-zhao-85-nonexists-template
statement: srg(85,14,3,2) does not exist, proved by exhaustive enumeration of
  local configurations (segments around a maximal 3-clique; 478 segments in 4
  types; local graphs are the 39 good cubic graphs on 14 vertices) checked
  against combinatorics (lambda=3, mu=2) and the 34-dim Euclidean
  representation. Same k=14, mu=2 as (99,14,1,2) but lambda=3.
hypotheses: srg(85,14,3,2) existence assumed then contradicted; classification
  of cubic graphs on 14 vertices; Euclidean representation of the 4-eigenspace.
holds-here: partially — provides the successful method template for 99; the
  local graph 7K2 of (99,14,1,2) makes the analogous segment space smaller than
  478. Does not itself decide 99.
status: asserted-by-source (arXiv preprint, not peer-reviewed; enumeration
  claimed complete with stated finite space, not re-verified here).
bearing: the closest successful nonexistence-by-local-enumeration precedent; the
  model for attacking the forced union-of-intersecting-triangles configurations
  / n_3 parameter in (99,14,1,2).
anchor: research/sources/shpectorov-zhao-srg85.full.md
```
