# K*(n) as a de Bruijn cycle-space rank computation

```approach
idea: >
  Characterize K*(n) — the least K such that S² is constant on every C_K-fiber —
  as the first K at which the fold functional lies in the COBOUNDARY (cut) space
  of the order-K de Bruijn graph B_K. The run's own C_K is literally the
  (K+1)-gram histogram, which is the edge-visitation vector of the length-(n-K)
  walk of h on B_K (vertices = K-words, edges = (K+1)-words). So "S² is a
  function of C_K" means: S², as a function on {±1}^n, is constant on the fibres
  of the edge-count map. The fibre of a fixed edge-count vector is an
  Eulerian-trail polytope whose tangent space is the cycle space of B_K
  (dimension 2^K + 1 for the connected B_K on 2^K vertices, 2^{K+1} edges).
  Hence S² is a function of C_K iff the functional S² is annihilated by the
  cycle space — equivalently it lies in the coboundary (cut) space of dimension
  2^K - 1. This converts the exponential 2^n pair-search for K* into a RANK
  computation on matrices of size ~2^K × (n-2)^2, and K*(n) = ⌈n/2⌉ would emerge
  as the first K at which the (n-2)^2 fold monomials are spanned by the 2^K - 1
  cut functionals. Speculative: the exact value ⌈n/2⌉ is a hypothesis, not a
  claim, until the rank test reproduces the measured table.

mechanism: >
  Named machinery: the de Bruijn graph and its cycle space / coboundary (cut)
  space; the BEST theorem and the matrix-tree theorem for the structure of
  Eulerian trails with prescribed edge counts. Why this problem suits it: the
  run already observed the hard fact that K* is much smaller than the naive
  symmetric-difference width bound (n-1 vs ⌈n/2⌉) because monomials cancel
  across the d,d' sum. That cancellation is a linear-dependence statement, and
  "depends only on edge counts" is exactly "orthogonal to the cycle space" —
  the natural, named linear-algebraic home for the cancellation. This is NOT the
  refuted orderk-kstar-sat route (which encodes the witness search as CP-SAT and
  keeps exponential branching): it replaces the search by a dimension/rank
  computation whose cost is 2^K · poly(n), exponential only in the ORDER K being
  probed, not in the string length n.
status: grounded
precedent: >
  MACHINERY IS REAL AND NAMED; the load-bearing equivalence and the floor(n/2)
  closed form are NOT sourced and must be established by the run's own rank test.
  - de Bruijn graph cycle/cut space as a canonical basis for k-mer count vectors:
    Philippakis, Mallinar, Pandit, Belkin, "Eigenvectors of the De Bruijn Graph
    Laplacian: A Natural Basis for the Cut and Cycle Space", arXiv:2410.07622
    (2024) — derives explicit Laplacian eigenvectors that form natural orthogonal
    bases for both the cut and cycle space of de Bruijn graphs, and explicitly
    interprets k-mer count vectors / bag-of-words as living in this cycle space
    (eigenvalues known since Delorme–Tillich 1998). This is the stated home of
    "a function of C_K" as "a vector constant on cycle directions".
  - k-mer spectrum ↔ Eulerian trail, and ambiguity = distinct trails differing by
    cycles: Pevzner, Tang, Waterman, "An Eulerian path approach to DNA fragment
    assembly", PNAS 98 (2001) — distinct Eulerian trails of the same edge-count
    (k-mer multiset) yield different reconstructions; Medvedev & Pop, "What do
    Eulerian and Hamiltonian cycles have to do with genome assembly?", PLoS
    Comput. Biol. 2021 — multiple cycles in one graph give multiple data-consistent
    strings; Bals et al., ESA 2025 (arXiv) — NP-completeness of c-respecting
    Eulerian trails in binary dBGs. These establish that the C_K-fibers (strings
    with a given (K+1)-gram histogram) are larger than one point, and that the
    differences between strings in one fiber are carried by the cycle space —
    precisely the "monomials cancel across the d,d' sum" the candidate attributes
    to the cycle space.
  - In-workspace: claim `kstar-exact-floor` (K*(n)=floor(n/2), n=2..18, five
    captures, two independent cumulative implementations — supersedes the ⌈n/2⌉
    table and RESOLVES the n=5 "exception": floor(5/2)=2. This is the closed form
    the rank test must reproduce). approach `orderk-kstar-sat` (the CP-SAT
    encoding this route replaces).
  CAVEAT (must be priced by the run, not taken from a source): the clean
  statement "a nonlinear functional S² is constant on every C_K-fiber iff it lies
  in the coboundary space" is NOT a sourced theorem for a nonlinear S². "Constant
  on fibers of a linear map" is a nonlinear condition (annihilated by every cycle
  direction, including nonlinear pull-backs); whether it is captured by the
  linear coboundary-space rank test is exactly the first-step falsifier. No
  literature computes K*(n) for the SUPPLY fold; the rank-test ⟺ K* bill is
  novel and open. Status grounded for the machinery, with the mechanism transfer
  explicitly unproven.
first-step: >
  (tool_builder, exact integer/±1 arithmetic, no primes) For n = 4..20:
  (1) build B_K for each K = 1..n-2, its vertex-edge incidence matrix, and the
  cycle/coboundary spaces; (2) expand S²(h) = Σ_{d,d'} ∏_{j ∈ M_d△M_{d'}} x_j
  with x_j = (−1)^{h_j} as a signed sum of monomials; (3) compute the smallest K
  such that S² lies in the coboundary space of B_K (rank test of the monomial
  matrix against the cut space) and compare to the measured K* = floor(n/2) table.
  FALSIFIER: if the rank test yields a K* differing from the measured table at
  any n (including n=5, where floor(5/2)=2), the coboundary characterization is
  wrong and the exact reason (which non-cut monomial fails to cancel) is recorded.
falsifies: >
  (a) a K from the rank test that disagrees with the measured K*=floor(n/2) table
  (the coboundary characterization is then false, and the obstructing monomial
  class is the deliverable); (b) the coboundary-space dimension estimate of B_K
  being wrong for the directed/multigraph structure actually in play (a
  bookkeeping defect in the de Bruijn incidence matrix); (c) the rank test
  reproducing floor(n/2) only up to n=18 but failing to extend structurally (then
  the closed form is still open and the rank computation must be lifted to a
  dimension formula over all K,n); (d) the nonlinear leap failing — if S² is
  constant on every C_K-fiber at some K where it is NOT in the coboundary space
  (or vice versa), the "constant-on-fibers ⟺ coboundary" equivalence is false and
  the run must find the correct algebraic condition.
```
