# Isoperimetry in integer lattices

Source: Ben Barber, Joshua Erde, "Isoperimetry in integer lattices", Discrete
Analysis, 2018. URL: https://doi.org/10.19086/da.3555

## What it establishes (as a survey)

For the d-dimensional hypercube Q_d ({0,1}^d, edges between strings differing in
one coordinate):

- **Edge isoperimetric problem:** the minimum edge boundary for a set of a given
  size is achieved by k-dimensional subcubes (fixing d−k coordinates) for the
  appropriate k. Attributed to Harper, Lindsey, Bernstein, and Hart.
- **Vertex isoperimetric problem:** the minimum vertex boundary is achieved by
  Hamming balls {strings with at most w ones}. Attributed to Harper.
- General inequality: ∂_v(S) ≤ ∂(S) ≤ Δ_in(G)·∂_v(S), where Δ_in(G) is the max
  in-degree. Here for the cube Δ_in = d = n.
- For large subsets the min boundaries scale roughly like
  d·vol(Z·n)^(1−1/d), the d-dimensional isoperimetric profile.

## Relevance to problem.md

Confirms the "obstruction" in problem.md at source level: the classical
hypercube isoperimetric results (subcubes for edge boundary, Hamming balls for
vertex boundary) control the **boundary** of a set, i.e. edges/vertices leaving
S to S^c. The problem.md quantity D(S) is the **maximum internal degree** — the
opposite direction. So the standard isoperimetric theory is about the wrong side
of the cut; this is precisely why averaging/boundary arguments get stuck at
log n. Also note the Survey is a good map of named results (Harper, Lindsey,
Bernstein, Hart, Bollobás–Leader) to chase for primary sources.
