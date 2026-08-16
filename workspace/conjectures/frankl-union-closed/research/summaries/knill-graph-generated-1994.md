# Knill, "Graph generated union-closed families of sets" (arXiv:math/9409215v1, 1994)

**Source URL:** https://arxiv.org/pdf/math/9409215v1 (downloaded; full text at
`research/sources/knill-graph-generated-1994.full.md`)

## What it is
E. Knill, an early (1994) treatment of union-closed families generated from a
graph: the "maximal-independent-set family" construction. Cited by the
Bruhn–Schaudt survey and by Das–Wu as the combinatorial base they combine with
Gilmer's entropy.

## Why it matters to this run
- Forms half of the engine in Das–Wu (Knill-type combinatorial argument +
  Gilmer entropy).
- It is the ancestor of the **graph formulation** of the conjecture
  (later made canonical by Bruhn–Charbit–Schaudt–Telle, EJC 2015, already in
  the library).
- Being 1994, its bounds are pre-entropy (logarithmic/small-family regime).
  Relevant to the Ruled-out question of what the combinatorial line alone was
  able to achieve.

## Status
Sourced (arXiv preprint, 1994). The full text was not yet read in detail; the
digest is structural only. Read the full text only if a later pass needs Knill's
exact combinatorial lemma.

```claim
id: knill-log-bound
statement: Every union-closed family F_{\not=\emptyset} has an element in at least (|F|−1)/log₂|F| sets (Knill 1994), the constant later improved by Wójcik; the maximal-independent-set-family construction.
hypotheses: union-closed, finite
holds-here: yes (pre-entropy; asymptotically weaker than Gilmer's constant but the graph-family construction is the ancestor of the graph formulation)
status: asserted (theorem in source; not re-checked here)
bearing: the graph-generated family construction is the combinatorial half of Das–Wu and the ancestor of Bruhn–Charbit–Schaudt–Telle's graph formulation.
anchor: research/sources/knill-graph-generated-1994.full.md
```

## Bearing
Knill's (|F|−1)/log₂|F| is superseded by Gilmer's constant in the large-|F|
regime; its value to this run is the construction, not the bound.
