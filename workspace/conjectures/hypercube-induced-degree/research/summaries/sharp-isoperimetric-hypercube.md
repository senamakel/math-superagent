# Sharp isoperimetric inequalities on the hypercube

Source: David Beltrán, Paata Ivanisvili, José Madrid, "On sharp isoperimetric
inequalities on the hypercube", arXiv:2303.06738, 2023.
URL: https://arxiv.org/abs/2303.06738

## What it establishes

For A ⊆ {0,1}^n under the uniform measure µ, define the one-sided boundary
function h_A(x) = number of edges from x to A^c if x ∈ A, else 0, and the edge
boundary ∇A = {(x,y) : x ∈ A, y ∈ A^c}. Let µ(A)* = min(µ(A), 1−µ(A)).

Main results:
1. A sharp edge-isoperimetric inequality on the hypercube, with equality exactly
   at subcubes.
2. Lower bounds on Eh^β_A = E[h_A^β] in terms of µ(A) for all β ∈ [1/2, 1],
   improving prior results. In particular, a sharp inequality for
   Eh^0.53_A for all sets with µ(A) ≥ 1/2, refining a recent result of Kahn and
   Park on partitioning the hypercube.
3. Talagrand-type inequalities for Banach-valued functions f: {−1,1}^n → X with
   finite cotype, bounding ||Df||_p in terms of the cotype constant.

Technique: Hölder-type interpolation from E[h_A^β] to E[h_A^(β/α)] and the
vertex boundary, plus sharp envelope functions.

## Relevance to problem.md

The paper's §1.1 notes the relationship (via Hölder):

    Eh^β_A  <=  (Eh^(β/α)_A)^α · µ(∂A)^(1−α)

which ties a moment of the boundary function to the vertex boundary. At
µ(A) = 1/2 (exactly the regime of problem.md, where |S| = 2^{n-1}+1) it gets
sharp bounds for β ≥ 0.53. This is average-type information (expectations), so
it cannot by itself produce a maximum; but it gives the sharpest known control on
moments of boundary degree, which is the closest thing to the internal-degree
quantity that existing theory reaches directly.
