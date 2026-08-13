```approach
idea: polynomial-evolution-halved-triangle-over-gf2
mechanism: |
  The halved Gilbreath triangle (entries A_k(i)/2 for k ≥ 1, i ≥ 1) lives in
  the non-negative integers and evolves under the halved absolute-difference
  operator H: H(u,v) = |u − v| when u,v are halved values (but now NOT
  restricted to {0,1}). Inside the {0,2} block, H is XOR (Rule 90). Outside,
  H(u,v) = |u−v| involves carries.

  The standard generating-function approach to Rule 90 / linear CA is: encode
  the row as a polynomial over GF(2)[X]. Row k (halved, inside {0,1}) is
  P_k(X) = Σ h_k(i) X^i. Rule 90 evolution is then P_{k+1}(X) = (1+X) ·
  P_k(X) mod X^W (truncation at the block boundary). The d-step evolution is
  P_{k+d}(X) = (1+X)^d · P_k(X) mod X^{W−d}.

  Now the NEW representation: treat the FULL halved row (including the intruder
  and tail) not as a single generating function but as a **pair** (B_k, T_k)
  where B_k ∈ GF(2)[X] encodes the {0,1} block and T_k is the tail beyond the
  block. The boundary cell A_k(b_k)/2 is the constant term of a shifted
  polynomial. The drain law (y drops by 2 when the edge is 2, i.e. when the
  halved edge is 1) has a polynomial interpretation:

  When the halved edge is 1 (original A=2), the difference at the boundary
  is |2 − y| = y − 2, so the halved intruder drops by 1 (halved). When the
  halved edge is 0, the intruder passes through unchanged.

  This is exactly a **polynomial division with remainder** process. Treat the
  halved row as a formal power series; the absolute-difference operator at the
  boundary is a nonlinear operation that can be linearized by going to the
  ring Z_2[[X]] of 2-adic integers. In Z_2[[X]], |a−b| (when a,b are even
  integers halved) corresponds to an operation in the 2-adic completion that
  keeps track of carries through the 2-adic valuation.

  The key bijection: the valuation triangle V_k(i) = v_2(A_k(i)) is a
  deterministic automaton whose state at position (k,i) depends only on the
  valuations and odd parts of a small neighborhood. Over Z_2, the
  absolute-difference operator becomes the 2-adic metric, and the triangle
  becomes the iteration of the ultrametric triangle inequality.

  **Concrete theorem to aim for**: In the 2-adic completion, the halved
  triangle's left edge h_k = A_k(1)/2 satisfies a recurrence

      h_k = Σ_{j=0}^{k−1} C(k−1, j) · h_1(j+2)   (modulo carries)

  where the carries are governed by the 2-adic valuations of the partial sums.
  If the carries can be shown to always resolve to 0 at position 1 (i.e., the
  carry cascade never raises the valuation past 1), then h_k ∈ {0,1} for all k,
  proving the conjecture.

  Why this is different from p-adic-valuation-carry-dynamics (already proposed):
  that approach works with the valuation triangle as a discrete automaton and
  asks "does the carry cascade stay bounded?" — this one goes a level deeper:
  it works with the power series ring GF(2)[[X]] or Z_2[[X]] and asks for an
  ALGEBRAIC closure property. The difference: the p-adic approach is a
  computational/symbolic check of the carry rules at each cell; this approach
  is a structural theorem about the ring — that the operator (1+X) acting on
  the initial halved-gap series, with carries encoded in the 2-adic completion,
  has the property that its d-th power applied to the initial series has
  constant term in {0,1}.

  Specifically, in GF(2)[[X]], the operator T: f ↦ f + X·f (mod 2) is exactly
  Rule 90, and the entry at position 1 after d steps is the coefficient of X^0
  in (1+X)^d · f(X), which is Σ binom(d,j) f_j, always 0 or 1. But the REAL
  operator is NOT mod 2; the carries mean we need to lift from GF(2) to
  Z/2^t Z for ALL t simultaneously — i.e., to Z_2. The lifted operator is
  T(f) = f + X·f + 2 · (carry term), where the carry term is the correction
  from the min(a,b) in |a−b| = a+b − 2·min(a,b).

  The structural claim: the carry term, when pulled back to position 1, is
  ALWAYS EVEN (i.e., vanishes mod 2). That is: the correction to the linear
  (1+X) operator from the absolute-value branch never affects the parity of
  position 1. But parity at position 1 IS the conjecture (h_k ∈ {0,1}), so
  this is equivalent to the conjecture. The content of this approach is to
  prove the carry term has a SPECIFIC algebraic form — e.g., that it lies in
  the ideal (2, X) of the ring Z_2[[X]]/(X^W) — which would force it to
  vanish at the left edge.

  **Speculative**: whether the carry term lands in (2, X) for all rows is an
  algebraic statement about the operator T on Z_2[[X]]. If it can be proved
  by induction on the row index using only the 2-adic triangle inequality (the
  exact ultrametric law that the p-adic approach already grounds), then the
  conjecture follows as a corollary of a purely algebraic theorem about the
  ring Z_2[[X]].

  This is a genuinely different axis: it replaces the combinatorial block-
  tracking with algebraic closure in a power-series ring, and it replaces the
  "carry cascade" check with a structural property of an operator on a
  completion. The nearest literature is the BCZ (Bhat–Cobeli–Zaharescu 2023)
  program of studying PG triangles via F_2[[X]] rational generating functions
  — but BCZ work at the mod-2 level only; this approach asks for the lift to
  Z_2.
status: proposed
first-step: |
  Write the exact operator on Z_2[[X]]. Let the initial halved row be f(X) =
  Σ_{i≥0} a_i X^i where a_0 = A_1(1)/2 (which is 1 for primes: the halved
  gap 2/2=1) and a_i = A_1(i+1)/2 = gap_{i+1}/2. Define the operator T on
  Z_2[[X]] by: for f,g ∈ Z_2[[X]], the "halved difference" at position i is
  h_i = |f_i − g_i| (in Z, then mapped to Z_2). The one-step row update is
  (T f)(X) = Σ_i h_i X^i. In Z_2, |a−b| = a + b − 2·min(a,b) where min is
  taken in the total order of Z (not Z_2). The term a+b is linear in Z_2, but
  min(a,b) is not a ring operation. However, at the halved level, the entries
  are small (O(1) for the left region), so the min can be resolved by
  comparing the 2-adic expansions. Write a small program that, for the first
  20 rows of the prime triangle, computes T^k f in Z (exact integers) and
  checks whether the coefficient of X^0 in T^k f is always 0 or 1. Then
  compute the "error term" E_k = T^k f − (1+X)^k f (where (1+X)^k f is the
  pure Rule 90 evolution) and check whether E_k has zero constant term for
  all k. If yes, the approach has empirical support for the claim that the
  carry correction never affects position 1. Then formulate the algebraic
  induction hypothesis that would prove this.
```
