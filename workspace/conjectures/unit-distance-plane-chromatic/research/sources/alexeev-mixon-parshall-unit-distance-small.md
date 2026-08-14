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

## Note on download

Full text download (arxiv.org/html/2412.11914) failed at the network layer in
this run. read_sources summary is the basis for content above.
Status: **sourced via read_sources; full text not on disk**.
