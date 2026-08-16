# Fold second moment as a transfer-matrix / Lyapunov-exponent problem

```approach
idea: >
  Read S(n) = sum_{d=2}^{n-1} eps_d as a partition function over the binary
  decision tree of the depth index d. The exact disjoint-union recursion
  downset(2^k + d') = downset(d') ⊔ (2^k + downset(d')) gives a genuine
  2-way product recursion eps_{2^k+d'} = eps_{d'} · eps'_{d'} where the two
  factors live in disjoint index intervals. Hence S(n)^2 = sum over pairs of
  paths of a binary tree = a trace of a product of small transfer matrices
  whose local entries are two-point residue products chi_4(q_a) chi_4(q_b).
  The second moment E[S(n)^2] is governed by the top Lyapunov exponent of a
  transfer cocycle over the residue string r_j = chi_4(q_j). The arithmetic
  input is then: that cocycle's Lyapunov exponent is <= 0, which is priced
  against one-point equidistribution rather than adjacent-pair switch density.
mechanism: >
  Named machinery: transfer matrices / matrix-product states (statistical
  mechanics) and Furstenberg-Kesten-Oseledets theory (Lyapunov exponents of
  products of matrices). This is NOT the refuted
  dyadic-renormalization-selfsimilar route (no fixed-point equation) and NOT
  the refuted dyadic-martingale-azuma route (a martingale over a probability
  space); here the object is a deterministic cocycle whose growth is a
  Lyapunov exponent. The self-similarity used is the exact Sierpinski
  submask-lattice recursion, which is load-bearing and machine-checkable.
status: proposed
first-step: >
  tool_builder, exact ±1 arithmetic. (1) Verify the exact boundary form
  eps_d = prod_{t in ∂↓d} chi_4(q_t) against the brute submask-XOR oracle for
  n <= 64, all d. (2) Build the transfer matrix of the disjoint-union
  recursion and verify S(n) and S(n)^2 match trace formulas for n <= 512.
  (3) Estimate the Lyapunov exponent of the cocycle on the real residue
  string r_j = chi_4(q_j) and print its sign. FALSIFIER: if the transfer
  matrix bond dimension is not O(1) in n, the recursion does not factorize
  and the Lyapunov framing is inert.
falsifies: >
  (a) the boundary product form eps_d fails against the oracle; (b) bond
  dimension grows with n (no constant transfer matrix); (c) the Lyapunov
  exponent of the prime-residue cocycle is > 0, so the second moment is
  superlinear and the route's input is as hard as switch density.
```
