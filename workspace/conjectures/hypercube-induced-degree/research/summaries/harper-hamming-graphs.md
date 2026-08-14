# On an isoperimetric problem for Hamming graphs (Harper)

Source: L. H. Harper, "On an isoperimetric problem for Hamming graphs",
Discrete Applied Mathematics, 1999. URL: https://doi.org/10.1016/s0166-218x(99)00082-7

## What it establishes

Harper's vertex-isoperimetric theorem for the Hamming cube Q_n: among all
subsets A ⊆ {0,1}^n with |A| = k, the minimum vertex boundary is achieved when
A is a Hamming ball of the appropriate radius r, where
k = Σ_{i=0}^r C(n,i). For such a ball, the vertex boundary is the number of
edges from the ball to its complement, determined by the layer structure of the
cube.

Proof method: compression (shifting) operators that push a set toward the
"skyline"/ball form without increasing the vertex boundary; iterating produces a
fully compressed set that must be a Hamming ball. This is the classical
Harper-numbering / compression technique.

## Relevance to problem.md

This is the canonical primary source for the vertex-isoperimetric result on the
cube. Like all boundary results, it controls the *external* boundary of a set,
not the maximum *internal* degree that problem.md asks about. It is the right
tool to know and the wrong tool to apply directly — recording this is the point:
a compression argument on vertex boundary does not transfer to D(S) without a
separate new argument, because internal degree is not monotone under the same
compressions in the needed direction.
