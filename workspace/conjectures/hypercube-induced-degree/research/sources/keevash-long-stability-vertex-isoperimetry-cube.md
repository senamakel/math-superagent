# Keevash–Long, "Stability for vertex isoperimetry in the cube" (arXiv:1807.09618)

Source URL: https://arxiv.org/abs/1807.09618
Authors: Peter Keevash, Eoin Long. 2018 (arXiv preprint).

## What this source establishes

Harper's vertex-isoperimetric inequality: for A ⊆ {0,1}^n with |A| = m, the
vertex boundary |∂v(A)| ≥ |∂v(I_m)| where I_m is the initial segment of size m
in the simplicial order (a "Hamming ball"-type set). This paper adds a
**stability** version: if |∂v(A)| is close to the minimum possible, then A is
close (in symmetric difference) to a generalised Hamming ball; plus a local
stability statement for ball-like sets.

It explicitly defines the two boundary notions on the cube:
- vertex boundary ∂v(A) = {x' ∉ A : x ~ x' for some x ∈ A}
- edge boundary ∂e(A) = {edges xy : x ∈ A, y ∉ A}.

## Why it is here

This pins down exactly what the vertex-isoperimetric inequality (one of the four
techniques named in problem.md's obstruction) bounds: the **vertex boundary**,
an average/outer quantity, min over sets of fixed size. It applies for m =
2^{n-1}+1 but bounds ∂v, not the maximum internal degree D(S). Harper's theorem
says the *smallest* vertex boundary for that size is achieved by a Hamming ball;
it does not say the *maximum internal degree* is at least anything.

Crucial negation for the noise-isoperimetric programmes (Beltrán et al.,
Durcik et al.): those bound E[h_A^β], an expectation over vertices of a
boundary-counting function. Even in sharpest form they give a statement about
average h_A, not max internal degree.

## Claim block

```claim
id: harper-vertex-isoperimetric-min-boundary
statement: Among subsets A ⊆ {0,1}^n of a given size m, the vertex boundary
  |∂v(A)| is minimised by an initial segment I_m in the simplicial order
  (Harper's theorem), and near-minimisers are close to generalised Hamming
  balls (stability, Keevash–Long).
hypotheses: A ⊆ {0,1}^n, arbitrary m = |A|.
holds-here: true as a statement about vertex boundary; but it bounds a boundary
  (outer) quantity, not the max internal degree D(S). For m = 2^{n-1}+1 the
  min-boundary set is a ball; that tells us nothing about D(S).
status: asserted-by-source.
bearing: confirms the obstruction — vertex-isoperimetry is an average-type
  outer-boundary tool and cannot, by itself, lower-bound the max internal
  degree of a set of size 2^{n-1}+1.
anchor: keevash-long-2018
```
