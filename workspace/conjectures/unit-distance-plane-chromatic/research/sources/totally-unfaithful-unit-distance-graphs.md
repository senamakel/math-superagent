# Totally unfaithful unit-distance graphs — non-embeddability certificates

**Source:** Globus & Parshall, "A lower bound for the number of edges in
totally unfaithful unit distance graphs" (and companions); expounded in:
Boris V. Alexeev, Dustin G. Mixon, Hans Parshall, "The Erdős unit distance
problem for small point sets", arXiv:2412.11914 (2024),
https://arxiv.org/abs/2412.11914.

**How obtained:** server-side retrieval (`deep_research` and `exa_search`
excerpts) returned the definition and usage verbatim.

## Definition (retrieved verbatim)

A unit-distance graph is **totally unfaithful** if it has a pair of
*non-adjacent* vertices such that, in **every** unit-distance embedding of the
graph, those two vertices are at unit distance apart.

## How it is used

If a graph on `n` vertices contains a totally unfaithful pair as a non-edge,
then it *cannot* be a unit-distance graph with `u(n)` edges: were it embeddable,
the forced unit distance would let one add that edge and get a unit-distance
graph with more than `u(n)` edges, contradicting the maximum. So totally
unfaithful graphs are forbidden-subgraph obstacles that prune the space of
candidate unit-distance graphs.

The prototypes are small graphs where rhombi / equilateral triangles force the
distinguished pair apart by exactly 1 (the paper exhibits six such graphs, five
used by Globus–Parshall).

## Why it matters here

`problem.md` proposes Minkowski sums and rotations as the construction engine.
Totally unfaithful graphs are a *certificate* tool in the opposite direction:
they bound which graphs *cannot* be unit-distance, independently of any
embedding, giving the run a way to know a construction is impossible without
searching the continuum of embeddings. Relevant to the "construction engine with
proved properties" deliverable in `GOAL.md`.

## Basis and status

- Definition and usage = sourced (arXiv paper), retrieved verbatim.
- Not verified computationally here.
