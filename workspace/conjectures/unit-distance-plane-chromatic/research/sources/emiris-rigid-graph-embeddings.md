# Algebraic methods for counting Euclidean embeddings of rigid graphs

**Source:** doi:10.1007/978-3-642-11805-0_19 (Emiris, Tsigaridas, Varvitsiotis 2010)
**Related:** Bartzos–Emiris–Legerský–Tsigaridas, "On the Maximal Number of Real
Embeddings of Spatial Minimally Rigid Graphs" (2018), doi:10.1145/3208976.3208994.
**Full text:** not on disk; read via read_sources/abstracts.

## What this establishes (technique relevant to exact verification)

Rigidity theory gives the exact algebraic framework for deciding whether a set of
edge-length constraints has real solutions in the plane:

- **Laman graphs** are exactly the rigid graphs in R²: |E| = 2|V| − 3 and every
  induced subgraph on k < |V| vertices has ≤ 2k − 3 edges.
- Embeddings with fixed edge lengths are solutions of a square polynomial system
  of quadratic (squared-distance) equations — fixing coordinates removes
  translation/rotation, giving 2n−4 equations for planar Laman graphs.
- The number of complex solutions is bounded by Bézout / multihomogeneous
  Bézout / Bernstein (mixed-volume) bounds; the real solutions (actual
  embeddings) are what unit-distance constructions produce.
- **In R² the system is well-structured**, and the number of equivalent
  realisations of a rigid graph is an algebraic invariant c(G), the same for all
  generic realisations (related: Borcea–Streinu; Dewar–Grasegger for c_d(G)).

## Why it matters here

The run's oracle needs to *certify* an exact unit-distance graph: given claimed
coordinates, the edges are checked by exact arithmetic (|x−y|² = 1 symbolically).
The rigidity framework is the mathematical guarantee that a claimed dense rigid
subgraph is not a floating-point artefact: a Laman-sparse graph has finitely
many embeddings for generic edge lengths, so exact solutions are well-defined.
It also characterises when edge constraints overdetermine (redundant rigidity) —
the regime where spurious near-unit edges would force contradictions and could
be detected.

```claim
id: rigid-graph-algebraic-framework
statement: In R^2, Laman graphs (|E|=2|V|-3, all k-vertex induced subgraphs have <= 2k-3 edges) are exactly the rigid graphs. Embeddings at fixed edge lengths are solutions of a square system of quadratic equations; the number of real embeddings is finite for generic lengths and bounded by algebraic (Bézout/Bernstein) bounds.
hypotheses: Minimal rigidity in R^2; generic edge lengths.
holds-here: true — gives the exact-algebraic basis for certifying/analysing unit-distance embeddings and detecting overconstraint.
status: sourced (paper abstract/summary)
bearing: Theoretical underpinning for the exact-coordinate verifier: rigid subgraphs have finitely many exact embeddings, so exact (non-floating) verification is well-posed.
anchor: research/sources/emiris-rigid-graph-embeddings.md
```

## Note on download

Full text blocked at network layer. Content from abstract/search summaries.
Status: **sourced via abstracts; full text not on disk.**