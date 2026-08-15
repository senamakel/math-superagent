# L. H. Harper, "Optimal Assignments of Numbers to Vertices" (SIAM J. Appl. Math., 1964)

Source URL: https://doi.org/10.1137/0112012
Retrieved via `read_sources` (server-side); direct download blocked by the
network boundary (SIAM publisher host unreachable from the run).

Paper: L. H. Harper, *Optimal Assignments of Numbers to Vertices*, Journal of
the Society for Industrial and Applied Mathematics 12 (1964), 131–135.

## What this source establishes

Harper proves the edge-isoperimetric theorem for the hypercube Q_N = {0,1}^N.
Among all bijections assigning distinct numbers 1..2^N to the vertices, the
edge boundary of any initial segment of the numbering is minimised by the
coordinate-wise binary (lexicographic) numbering of vertices — equivalently,
the sets of minimum edge boundary at each size are the initial segments in the
binary order. This is the classical *edge-isoperimetric theorem on the cube*:
for fixed |S|, the number |∂_e(S)| of edges leaving S is minimised by an
initial segment I_m in the binary numbering.

Technique: compression/shifting on the cube. Harper shows that a shifting
operation does not increase the edge boundary, and iterating it transforms any
labelling into an initial segment of the binary order while never increasing
the boundary. Hence the edge-boundary-minimising sets are those initial
segments.

This is the primary reference behind the edge-isoperimetric half of
`survey-cube-isoperimetric-profile` (Harper/Lindsey/Bernstein/Hart attribution
in the Barber–Erde survey). The Berge/Harper sublattice nature of the extremal
sets (nested families of subcubes / "shadow" structure) is what connects the
edge profile to the Kruskal–Katona shadow machinery.

## Why it is here

The cube edge-isoperimetric theorem is one of the four classical techniques the
problem.md obstruction names; this is its original primary source. It bounds
the *edge boundary* |∂_e(S)| — an outer/average quantity — never the maximum
internal degree D(S). At |S| = 2^{n-1}+1 it gives only an average-type bound
(total internal edges), confirming the obstruction that isoperimetric profiles
do not reach D(S). It is the canonical reference for the extremal *shape* of
edge-minimal sets (subcube-like initial segments / shadows).

## Claim block

```claim
id: harper-optimal-assignments-1964
statement: Among subsets S of Q_N = {0,1}^N with |S| = m, the edge boundary
  |∂_e(S)| is minimised by the initial segment I_m of the binary (coordinate-wise
  lexicographic) numbering of vertices. The extremal sets of the edge
  isoperimetric problem are subcube-like / shadow-closed.
hypotheses: Q_N with the usual Hamming adjacency; fixed set size m.
holds-here: yes — applies at m = 2^{n-1}+1, but bounds only the outer edge
  boundary, an average-type total, not the max internal degree D(S).
status: asserted-by-source (Harper 1964, read via read_sources; primary).
bearing: canonical primary source for the cube edge-isoperimetric inequality;
  confirms the obstruction that the classical isoperimetric profile is an
  outer-boundary tool and cannot reach f(n).
falsifies: an S of size m whose edge boundary is strictly smaller than that of
  the binary initial segment.
anchor: https://doi.org/10.1137/0112012
```
