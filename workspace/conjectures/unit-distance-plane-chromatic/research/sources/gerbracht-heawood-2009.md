# Eleven unit distance embeddings of the Heawood graph — Gerbracht (2009)

**Source:** arxiv.org/abs/0912.5395
**Authors:** Eberhard H.-A. Gerbracht (2009)
**Full text:** NOT on disk — read via server-side read_sources over the arXiv
abs page (abstract); status **sourced via read_sources**.

## What this establishes — a large rigid exactly-certifiable test graph

- **The Heawood graph** (14 vertices, 21 edges; the point-line incidence graph
  of the Fano plane PG(2,2)) admits **unit-distance embeddings** in the plane:
  the paper exhibits **eleven** of them, with 15-digit coordinate
  approximations plus the defining algebraic equations, which suffice to
  calculate arbitrarily exact coordinates.
- This **refutes a suspicion of Chvátal** (1972, "Selected combinatorial
  research problems") that the Heawood graph might not be a unit-distance
  graph.
- Companion papers: Gerbracht 2006 "Minimal Polynomials for the Coordinates of
  the Harborth Graph" (arXiv math/0609360), Harris 2007 "Toward a Unit
  Distance Embedding for the Heawood graph" (arXiv 0711.1157).

## Why it matters here

The run's edge certifier `unit_graph(points)` needs test cases beyond the
7-vertex calibration graph. The Heawood graph is exactly the right kind:
14 vertices, 21 edges, rigid enough that its embeddings are algebraic but
explicitly given by polynomial equations. Its chromatic number is 2 (bipartite
incidence graph) — so it is a *negative* control for the colouring oracle (must
report 2-colourable, and never be mistaken for a 5-chromatic candidate), while
being a *stressful* exact case for the edge certifier (21 edges to certify at
distance exactly 1). Reconstructing one of the eleven embeddings from the
defining equations and certifying all 21 edges exactly is a strong independent
check of the oracle pipeline.

```claim
id: heawood-unit-distance-embeddings
statement: The Heawood graph (14 vertices, 21 edges) admits unit-distance embeddings in the plane; eleven are exhibited with coordinates given by algebraic equations, refuting Chvatal's 1972 suspicion.
hypotheses: plane embeddings, edges at distance exactly 1; coordinates algebraic.
holds-here: yes - a rigid 14-vertex/21-edge exact test graph for the edge certifier and a bipartite negative control (chi=2) for the colouring oracle.
status: sourced (Gerbracht arXiv 0912.5395, via read_sources; full text not on disk)
bearing: oracle stress-test beyond the 7-vertex calibration; negative colouring control.
anchor: research/sources/gerbracht-heawood-2009.md
```

## Note on download

Full text network-blocked (arxiv host unreachable). Status: **sourced via
read_sources; full text not on disk**.