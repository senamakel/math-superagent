# Balaji 2026 — 60-vertex bound for cubic bipartite counterexamples

Source: A. Balaji, "A 60-Vertex Lower Bound for Cubic Bipartite Counterexamples
to the Erdős–Gyárfás Conjecture", arXiv:2608.02675 (2026). Full text held at
`research/sources/balaji-bipartite-60-vertex.full.md`.

## Result (from full text)

- **Theorem 1**: every simple cubic bipartite graph on at most 58 vertices
  contains a cycle of length 4, 8, or 16.
- **Corollary 2**: any cubic bipartite counterexample to E-G has at least 60
  vertices. This improves the established published bound of 30 (Salehi
  Nowbandegani & Esfandiari 2011 / Wikipedia).
- Also: one of {C4, C8, C16} is forced — no 32-cycle is needed for a
  counterexample in this range.

## Method (certified)

1. Moore-bound observation: below 62 vertices, a cubic bipartite graph avoiding
   4- and 8-cycles must contain a 6-cycle.
2. Translate via the Levi-graph correspondence: a cubic bipartite graph is the
   Levi graph of a linear symmetric v3-configuration; the 6-cycle ↔ a Berge
   triangle in the configuration.
3. Up to symmetry there are only two rooted extensions; a complete
   restricted-growth search on at most 29 points closes both search trees.
4. The computation is checked by two separately implemented searches using
   different C16 oracles, and by a static witness certificate. Source code,
   certificates, and reproduction instructions are archived with the paper.

## What it means for this run

The **bipartite cubic class is explicitly open** per the held Wikipedia source.
This pushes the smallest possible cubic bipartite counterexample from ≥30 to
≥60 vertices. Because the proof is *certified* (two independent oracles + a
static witness), it is stronger evidence than the SMS general bound, which has
no formal certificate. It is the deepest verified bound held in the library for
an open class.

```claim
id: balaji-bipartite-60
statement: Every simple cubic bipartite graph on at most 58 vertices contains a cycle of length 4, 8, or 16; hence any cubic bipartite counterexample has at least 60 vertices.
hypotheses: simple cubic bipartite, n <= 58
holds-here: yes (bipartite cubic is an open class; this is its verified frontier)
status: asserted (certified computation; not independently re-derived here)
bearing: the strongest verified bound for the open bipartite cubic class; an oracle target
anchor: research/sources/balaji-bipartite-60-vertex.full.md
```
