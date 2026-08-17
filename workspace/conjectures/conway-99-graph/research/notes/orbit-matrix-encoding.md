# Orbit-matrix feasibility under a fixed-point-free order-3 automorphism

## Method (names the theory first)

The orbit-matrix / Kramer–Mesner enumeration is the published tool applied to
exactly this parameter set by Crnković–Maksimović 2020, Behbahani–Lam 2011, and
Cesarz–Woldar 2025 (see `research/approaches/orbit-matrix-residual-group.md`).
Crnković–Maksimović proved an order-3 automorphism of a putative srg(99,14,1,2)
is FIXED-POINT-FREE, so it has exactly 99/3 = 33 point-orbits of size 3. The
vertex orbit matrix M is 33×33, symmetric, integer, and constant-on-orbits.

## What is being encoded

**Decision.** One integer variable M[i][j] for each unordered pair of size-3
orbits (0 ≤ i ≤ j < m), meaning the number of neighbours in orbit j of a fixed
vertex of orbit i. For an order-3 fixed-point-free action M[i][j] ∈ {0,1,2,3},
and the diagonal M[i][i] ∈ {0,2} (a size-3 orbit is an independent set or a
triangle; M[i][i]=1 is impossible under an automorphism). A satisfying
assignment is an *orbit-level* candidate: a matrix whose 3-lifts would be a
conway graph. It is **not** itself the graph.

**Constraints.** All derive from the srg defining equation A² = kI+λA+μ(J−I−A),
which I reduce to an orbit-level identity. Summing the (i,j) block over the 9
vertex pairs and using λ=1, μ=2, orbit size 3, and row-sum k=14 gives

    MM^T = 6J + (k−2) I − M

i.e. for 99 (k=14): MM^T = 6J + 12I − M. This one quadratic-integer identity
encodes the whole srg condition (both λ and μ, all 33×33 blocks), plus:
  - row sums = k (regularity);
  - diagonal M[i][i] ∈ {0,2} (orbit type);
  - off-diagonal M[i][j] ∈ {0..3} (orbit size 3);
  - symmetry M = M^T.
This identity is validated on the real orbit matrices of both controls:
rook(3) Z3 (3 orbits of size 3, k=4, c=2) and bvls Z3 (81 orbits, k=22, c=20)
--- both True (`code/out/orbit_matrix_verify_equations.py`).

**De Winter–Kamischke–Wang congruence.** For a fixed-point-free order-3
automorphism, g = #vertices mapped to an adjacent vertex = 3·T where T =
#triangle-orbits (each triangle-orbit contributes 3 edges-in-orbit = 3
vertices mapped to neighbours). The Benson trace congruence gives
4f + g ≡ 4 (mod 7) with f=0, so 3T ≡ 4 (mod 7) ⇒ T ≡ 6 (mod 7), T ≤ 33 ⇒
T ∈ {6, 13, 20, 27}. This is added as a hard constraint for 99.

## Size

For 99: m=33 orbits ⇒ n_vars = 33·34/2 = 561 integer variables (each a small
domain). The MM^T identity is enforced entrywise as the necessarily-satisfied
member M^2 = 6J+12I−M: m·m = 1089 quadratic constraints in ≤m adds each.
For BvLS: m=81 ⇒ n_vars = 81·82/2 = 3321, m² = 6561 constraints. Both small.

## What each verdict proves (stated before running)

- **BvLS feasible** validates the encoder (BvLS really admits order-3
  fixed-point-free automorphisms), using the DKW T ≡ 6 (mod 7), i.e.
  3T ≡ k−s (mod √Δ).
- **99 INFEASIBLE** ⇒ NO order-3 FIXED-POINT-FREE automorphism of a putative
  srg(99,14,1,2) exists at orbit level. Combined with the published elimination
  of Z2, this would give |Aut| = 1 (trivial group) *if a graph exists*. It does
  **NOT** prove srg(99,14,1,2) does not exist, and an orbit-level feasible
  matrix does not prove a graph exists either (it may not lift). The verdict is
  **orbit-level** feasibility/infeasibility, nothing stronger.
