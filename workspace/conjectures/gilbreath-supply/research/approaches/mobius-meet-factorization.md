# Meet-semilattice Möbius factorization of the second moment

```approach
idea: >
  Factor the one open arithmetic input — E[S(n)²] = O(n) for the prime string,
  equivalently Σ_{d,d'} ∏_{j ∈ M_d △ M_{d'}} u_j = O(n) with
  u_j = χ(q_j)χ(q_{j+1}) the switch sign — over the meet-semilattice of the
  fold's windows using Rota's Möbius inversion on the Boolean lattice. By the
  proved meet formula M_d ∩ M_{d'} = M_{d∧d'} (claim
  downset-row-intersection-meet-formula), the symmetric difference is the
  disjoint union M_d △ M_{d'} = (M_d ∖ M_j) ⊔ (M_{d'} ∖ M_j), j = d∧d'. Each
  piece M_d ∖ M_j is a union of subcubes indexed by the set bits of d ∖ j on
  the m = ⌈log₂ n⌉-bit lattice. Inclusion–exclusion (subcube Möbius inversion)
  should therefore write the monomial ∏_{M_d△M_{d'}} u_j as a product over the
  set bits of d △ d' of per-bit factors; then the constraint d∧d' = j makes the
  double sum an INDEPENDENCE POLYNOMIAL of a disjointness graph on m bit
  positions: Σ_{d,d' : d∧d'=j} (monomial) = ∏_{b ∉ j} (1 + 2λ_b(j)) up to the
  meet-j sum. This would reduce the second moment to a first-moment (two-point)
  input per bit — a candidate arithmetic input strictly weaker than positive
  mod-4 switch density (GOAL priority 2/4).
mechanism: >
  Named machinery: Rota's Möbius function μ(x,y) of the subset lattice, subcube
  inclusion–exclusion, and the independence polynomial (the hard-core/transfer
  structure) of the disjointness graph on the depth-index bits. This is NOT the
  refuted ANF/Reed–Muller route (which reads the FIRST moment's Möbius transform
  and was inert as a relabeling) and NOT the spectral diagonalization of
  meet-join-parseval-self-duality (which proved geometry carries no pointwise
  force): it is a combinatorial factorization of the SECOND-moment monomial into
  a product over the m depth bits, converting a coupled double sum into an
  independence-polynomial evaluation. The load-bearing conjecture is that
  M_d ∖ M_j is a disjoint union of subcubes whose character product is
  per-bit-multiplicative; the first step exists to prove or kill exactly that.
status: proposed
first-step: >
  tool_builder, exact F₂/integer arithmetic, no number theory (the prime string
  is not needed). (1) For every pair (d, j) with j ⊆ d and d ≤ n−1, n ≤ 64,
  compute the reflected-downset difference M_d ∖ M_j, its maximal runs, and
  test whether the runs are subcubes in the reflected index — i.e. whether
  ∏_{runs} χ(r_a)χ(r_b) factorizes as a product over the set bits of d ∖ j.
  (2) For each j, compute the double sum C(j) = Σ_{d,d' : d∧d'=j} ∏_{M_d△M_{d'}} u_j
  as a polynomial in the switch signs and test the independence-polynomial
  identity against it. FALSIFIER: if M_d ∖ M_j has a run that is not a subcube
  (interleaving across two set bits), the per-bit factorization fails; the route
  then records the exact interleaving obstruction as a priced negative instead of
  forcing the factorization.
falsifies: >
  (a) a non-subcube run in M_d ∖ M_j (the factorization is false and the exact
  obstruction is the deliverable); (b) the independence-polynomial identity
  fails in degree or in the λ_b(j) dependence (then the meet factorization does
  not decouple, and the second moment is genuinely a non-product object); (c) the
  resulting per-bit λ_b(j) quantities turn out to need the switch density itself
  (then the route collapses to the parity barrier, i.e. priority 5 is the truth).
```
