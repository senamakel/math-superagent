# Keevash–Long, "Stability for vertex isoperimetry in the cube" (arXiv:1807.09618)

URL: https://arxiv.org/abs/1807.09618

## What it establishes

- Harper's vertex-isoperimetric theorem: for A ⊆ {0,1}^n with |A| = m, the
  vertex boundary |∂_v(A)| ≥ |∂_v(I_m)| where I_m is the initial segment of
  size m in the simplicial order (a Hamming-ball-type set).
- **Stability version (new):** if |∂_v(A)| is close to the minimum, then A is
  close (in symmetric difference) to a generalised Hamming ball; plus a local
  stability statement for ball-like sets.
- Defines the two boundary notions explicitly: vertex boundary
  ∂_v(A) = {x' ∉ A : x ~ x' for some x ∈ A}; edge boundary
  ∂_e(A) = {edges xy : x ∈ A, y ∉ A}.

## Why it is here / relevance

Pins down exactly what the vertex-isoperimetric inequality bounds: the *outer*
vertex boundary, an average-sized outer quantity, min over sets of fixed size. It
applies at m = 2^{n-1}+1 but bounds ∂_v, not the maximum internal degree D(S).
Harper says the *smallest* vertex boundary at that size is achieved by a Hamming
ball; it does not say the *largest internal degree* is anything. This is the most
explicit statement in the library that the isoperimetric machinery is the wrong
side of the cut for D(S), and the stability version only refines the boundary, so
it adds nothing to bounding D(S).

## claim block

```claim
id: harper-vertex-isoperimetric-min-boundary
statement: Among subsets A of {0,1}^n of size m, |∂_v(A)| is minimised by an
  initial segment I_m in the simplicial order (Harper), and near-minimisers are
  close to generalised Hamming balls (stability, Keevash–Long).
hypotheses: A ⊆ cube, arbitrary m = |A|.
holds-here: true as a vertex-boundary statement; it bounds an outer quantity,
  not max internal degree D(S). At m = 2^{n-1}+1 the min-boundary set is a
  ball; that says nothing about D(S).
status: asserted-by-source
bearing: confirms the obstruction — vertex-isoperimetry (even with stability)
  is an average/outer tool and cannot by itself lower-bound the max internal
  degree of a set of size 2^{n-1}+1.
anchor: research/sources/keevash-long-stability-vertex-isoperimetry-cube.md
```

**Does not help** for the D(S) bound; a map/confirmation of the obstruction
only.
