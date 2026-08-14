# The Erdős unit distance problem for small point sets

**Source:** arxiv.org/abs/2412.11914
**Authors:** Boris V. Alexeev, Dustin G. Mixon, Hans Parshall
**Full text:** research/sources/alexeev-mixon-parshall-unit-distance-small.full.md (download blocked; see note)

## What this paper establishes (technique relevance to Hadwiger–Nelson)

- **Forbidden-subgraph enumeration:** uses Globus–Parshall's set of minimal
  forbidden subgraphs for unit-distance graphs on up to 9 vertices to enumerate
  candidate dense unit-distance graphs (via nauty). Computes upper bounds
  u(n) for n ≤ 21, and relates them to best known lower bounds.
- **Totally unfaithful unit-distance graphs:** substructures where two
  distinguished non-adjacent vertices must be at unit distance in EVERY
  embedding. Any graph with such a substructure, where adding that edge would
  exceed the max edge count, cannot be unit-distance. Powerful pruning tool.
- **Custom embeddability solver:** a specialised algorithm that decides whether
  a given graph admits a unit-distance embedding using elementary Euclidean
  geometry and linear algebra moves, faster than general semialgebraic/cylindrical
  algebraic decomposition methods. Returns a unit-distance embedding, "not
  unit-distance", or "don't know".
- **Dense unit-distance graphs explicitly use Minkowski sums, wheels, and
  spindles** — confirming that these are the natural construction engines for
  rigid/dense unit-distance graphs (matching problem.md's construction leads).

## Why it matters here

This is directly the computational machinery the run needs: exact geometry-based
embedding/verification rather than floating-point, and the algebraic-structure
realisations (Minkowski sums, spindles) that build dense unit-distance graphs.
The "totally unfaithful" idea is relevant to how accumulated rigidity forces
chromatic number.

```claim
id: ud-forbidden-subgraphs
statement: There is a set F of minimal forbidden subgraphs characterising unit-distance graphs on at most 9 vertices (Globus–Parshall), usable to enumerate and prune candidate dense unit-distance graphs.
hypotheses: Graphs on <= 9 vertices; F-free is necessary for unit-distance.
holds-here: true — gives a certificate/combinatorial filter for whether a small graph is unit-distance.
status: sourced (Alexeev–Mixon–Parshall, arxiv 2412.11914, building on Globus–Parshall)
bearing: A small-graph oracle: the run can test whether a candidate graph is unit-distance by forbidden-subgraph and embeddability checks, complementary to exact coordinate verification.
anchor: research/sources/alexeev-mixon-parshall-unit-distance-small.md
```

```claim
id: ud-minkowski-spindle-engines
statement: Dense unit-distance graphs for small n are realised by Minkowski sums, wheels, and spindles of simple shapes — the standard construction engines.
hypotheses: Dense unit-distance embeddings in the plane.
holds-here: true — directly validates problem.md's construction leads (Minkowski sums, spindling).
status: sourced (Alexeev–Mixon–Parshall, arxiv 2412.11914)
bearing: The search over constructions should concentrate on Minkowski sums and spindles of algebraic point sets.
anchor: research/sources/alexeev-mixon-parshall-unit-distance-small.md
```

```claim
id: amp-totally-unfaithful
statement: A totally unfaithful unit-distance substructure is one in which two distinguished non-adjacent vertices are at unit distance in EVERY unit-distance embedding; any graph containing such a substructure, where adding the forced edge would exceed the maximum edge count for its size, cannot be a unit-distance graph.
hypotheses: the distinguished pair is non-adjacent in the abstract graph; an upper bound on the number of unit distances for that n (e.g. the computed u(n)) is available.
holds-here: yes — a rigidity-based pruning certificate: forced unit pairs show how algebraic rigidity accumulates, and the criterion converts "pair forced to distance 1" into "graph not unit-distance".
status: asserted (technique stated in the excerpt; the precise definition and proof require the primary text)
evidence: research/sources/alexeev-mixon-parshall-unit-distance-small.md (librarian excerpt; primary text not on disk)
bearing: pruning in the construction search (G-five-chromatic-graph) and in G-exhaust; complements exact coordinate verification by unit_graph.
anchor: research/sources/alexeev-mixon-parshall-unit-distance-small.md
```

```claim
id: amp-ud-bound-n21
statement: Alexeev–Mixon–Parshall compute upper bounds for u(n), the maximum number of unit distances among n points in the plane, for every n <= 21, by forbidden-subgraph enumeration and an exact embeddability solver for unit-distance graphs.
hypotheses: n <= 21; distances measured exactly (squared distance 1 in R^2).
holds-here: yes — a minimal 5-chromatic unit-distance graph on n vertices is 5-critical and hence has at least 2n edges (gap G-crit); wherever a computed bound lies below 2n, that n cannot host a minimal counterexample, which pins the starting point of the size-lower-bound sweep (request largest-which-currently-5018).
status: asserted (the bound VALUES are not in the excerpt; nothing can be inferred from them until the primary text supplies the numbers)
evidence: research/sources/alexeev-mixon-parshall-unit-distance-small.md
bearing: edge-count ceilings for n <= 21; note the ceiling bounds edges, not chromatic number — it supports the size-lower-bound route only through 5-criticality.
anchor: research/sources/alexeev-mixon-parshall-unit-distance-small.md
```

## Note on download

Full text download (arxiv.org/html/2412.11914) failed at the network layer in
this run. read_sources summary is the basis for content above.
Status: **sourced via read_sources; full text not on disk**.
