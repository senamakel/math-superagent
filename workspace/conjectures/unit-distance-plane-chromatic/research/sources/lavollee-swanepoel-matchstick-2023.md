# Matchstick and 1-planar unit-distance graphs — planar-embedded density walls

**Sources (all read via server-side search excerpts; full texts not on disk):**
- J. Lavollée, K. Swanepoel, "Bounding the Number of Edges of Matchstick
  Graphs", SIAM J. Discrete Math / DCG, doi.org/10.1137/21m1441134 (2022) and
  doi.org/10.1007/s00454-023-00530-z (2023): **Harborth's conjecture proved**
  — a plane unit-distance (matchstick) graph on n ≥ 1 vertices has at most
  u0(n) = ⌊3n − √(12n) − 3⌋ edges, tight on triangular-lattice constructions.
  Main tool: an isoperimetric inequality related to L'Huilier's inequality
  (Harborth 1981 introduced matchstick graphs).
- P. Gehér, G. Tóth, "1-Planar Unit Distance Graphs", LIPIcs GD 2024, doi.org/
  10.4230/lipics.gd.2024.6: u1(n) (1-planar UDGs, ≤ 1 crossing per edge) has
  u1(n) ≥ ⌊3n − √(12n) − 3⌋ (inherited from matchsticks) and
  u1(n) ≤ 3n − (2/√10)√n; general k-planar unit-distance: c·√(4kn) upper,
  2^{Ω(log k/log log k)}·n lower (Rote).
- E. Červenková, J. Kratochvíl, "1-Planar Unit Distance Graphs with More Edges
  Than Matchstick Graphs", LIPIcs GD 2025, doi.org/10.4230/lipics.gd.2025.26:
  **u1(n) > u0(n) for every n ≥ 16135** (gap can be made arbitrarily large;
  explicit 31-vertex 74-edge 1-planar UDG with u0(31) = 73).
- P. Gehér, J. Pach, K. Swanepoel, G. Tóth, "On the number of edges of
  restricted matchstick graphs", arXiv 2506.01589 (2025): triangle-free
  matchstick graphs have 2n − √2·√n − O(1) ≤ e(n) ≤ 2n − √2/5·√n; matchstick
  graphs in a fixed-radius disk have ≤ (2−ε(r))n.

## Why it matters here

These are the exact edge-count ceilings for the **plane-embedded** (non-crossing
and 1-planar) unit-distance classes. They sit below the general u(n) = O(n^{4/3})
ceiling and above the 5-critical floor e ≥ 2n; the comparison is what the run's
density reasoning should keep visible:

- A 5-critical unit-distance graph needs e ≥ 2n (G-crit). The triangle-free
  matchstick bound maxes near 2n − Θ(√n) — so a 5-critical graph that is
  plane-embedded with no triangles must sit at the very top of that class or
  leave it; the Harborth bound 3n − Θ(√n) shows triangular matchstick graphs
  have room above 2n, so the 2n floor is not itself an obstruction plane-side.
- The general (non-planar) unit-distance graph is where the density must
  actually come from — confirming problem.md: crossing-allowed algebraic
  constructions (Minkowski sums) genuinely exceed the plane-embedded ceiling.

```claim
id: matchstick-harborth-bound
statement: Harborth's conjecture is proved: a plane unit-distance (matchstick) graph on n >= 1 vertices has at most u0(n) = floor(3n - sqrt(12n) - 3) edges, tight on triangular-lattice constructions (Lavollee-Swanepoel).
hypotheses: plane embedding, edges are straight unit segments, no crossings.
holds-here: yes as a planar-embedded density wall: matchstick graphs have room above the 5-critical floor e >= 2n, so the plane-embedded class is not excluded by G-crit alone.
status: sourced (Lavollee-Swanepoel 2022/2023, via search excerpts)
bearing: places the planar-embedded ceiling (3n - Theta(sqrt n)) against the 5-critical floor (2n); the construction engine must leave the plane-embedded class to accumulate density.
anchor: research/sources/lavollee-swanepoel-matchstick-2023.md
```

## Note on download

Full texts network-blocked. Status: **sourced via search excerpts; full texts
not on disk**.