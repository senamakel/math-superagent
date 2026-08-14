# Small unit-distance graphs in the plane — Globus and Parshall

**Source:** arXiv:1905.07829 (2019); published as Bull. ICA 90 (2020)
**Authors:** Aidan Globus, Hans Parshall
**Full text:** not on disk; read via read_sources (arXiv abstract page).

## What this establishes — the exact small-graph classification

The complete classification of unit-distance graphs on few vertices. This is
the combinatorial backbone of the run's small-graph oracle:

- **≤ 5 vertices:** a graph is unit-distance realisable iff it contains neither
  K4 nor K2,3 as a subgraph. These are the two minimal forbidden graphs in this
  range.
- **≤ 7 vertices (Chilakamarri–Mahoney 1995):** there is a complete set F≤7 of
  SIX minimal forbidden graphs; a graph on at most 7 vertices is forbidden iff
  it contains a subgraph isomorphic to one of them. (This is the list problem.md's
  7-vertex Moser-spindle-type graph must be checked against.)
- **≤ 9 vertices (this paper):** the complete set F≤9 consists of 74 graphs —
  the six F≤7 plus 13 eight-vertex and 55 nine-vertex graphs, labelled
  F(n,m,i) in the Chilakamarri–Mahoney notation. **Theorem 1:** a graph on at
  most 9 vertices is forbidden iff it contains a subgraph isomorphic to an
  element of F≤9.
- Paper includes the full list in Appendix A and coordinates for embedded
  unit-distance graphs in Appendix B.

## Why it matters here

The run's verifier needs to know quickly whether a candidate small graph is a
genuine unit-distance graph. This classification gives a certificate-level
combinatorial filter: F-freeness is necessary (and on ≤ 9 vertices,
characteristic) for unit-distance realizability. Together with the exact
coordinate verifier (the `unit_graph` oracle), this is the small-graph
decision layer. It also confirms the run's construction engines: dense
unit-distance graphs on small vertex counts are exactly those avoiding 74
specific obstructions, so Minkowski sums/spindles of algebraic point sets are
the way to grow past 9 vertices without hitting F.

```claim
id: globus-parshall-F9-classification
statement: A graph on at most 9 vertices is a unit-distance graph iff it contains no subgraph isomorphic to any of the 74 minimal forbidden graphs F<=9 (six on <=7 vertices per Chilakamarri-Mahoney, 13 eight-vertex, 55 nine-vertex). On <= 5 vertices the two forbidden subgraphs are exactly K4 and K2,3.
hypotheses: Plane unit-distance embeddings; graphs on n <= 9 vertices; "forbidden" = not embeddable with all edges unit.
holds-here: true — gives the run's small-graph oracle a complete combinatorial classification for n <= 9, exactly the range where the search starts.
status: sourced (Globus–Parshall 2019/2020; Theorem 1, F<=9 of 74 graphs)
bearing: Certifies small graphs by F-freeness; pins the boundary where coordinate-based exact verification takes over from classification.
anchor: research/sources/globus-parshall-small-unit-distance.md
```

## Note on download

Full text blocked at network layer. Status: **sourced via read_sources (arXiv
abstract + classification excerpt); full text not on disk.**