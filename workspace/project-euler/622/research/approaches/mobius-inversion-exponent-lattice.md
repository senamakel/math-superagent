# Möbius inversion on the exponent lattice

A route that proves the *general* identity for every k and specialises to
k=60, instead of the skeleton's use of the coincidental fact that every proper
divisor of 60 divides 12, 20, or 30. Same number-theoretic family as the
skeleton, different (stronger) theorem and different Lean tree.

```approach
idea: Möbius inversion on the divisor lattice of the *exponent* k: for every
  k, C(k) = Σ_{d|k} μ(k/d)(τ(2^d−1)−1) and S(k) = Σ_{d|k} μ(k/d)(σ(2^d−1)−1),
  proved once as a general theorem, then evaluated at k=60 over its twelve
  divisors {1,2,3,4,5,6,10,12,15,20,30,60}.
mechanism: The order-divisibility bijection (ord_m(2) | d ⟺ m | 2^d−1, Conrad
  Thm 2.1) turns "exact order k" into a Möbius inversion over d|k — the dual
  of the skeleton, which inverts over divisors of the *modulus* 2^60−1. Here
  the Möbius inversion lives on the small lattice of divisors of 60, and the
  final number is a linear combination over the twelve independent values
  σ(2^d−1), each evaluated from the small factorizations 2^d−1 (down to
  2^1−1=1). At k=60 the only nonzero μ(60/d) terms are d ∈
  {60,30,20,12,10,6,4,2}, so S(60) is a signed sum of eight σ-values — a
  longer but fully uniform computation, and a theorem true for all k rather
  than a fact special to 60.
status: adopted
first-step: Prove the general Möbius inversion in Lean via Mathlib's
  `Nat.sum_mul_moebius`, then the order-divisibility bijection
  ord_m(2)|d ⟺ m|2^d−1, giving S(k)=Σ_{d|k}μ(k/d)(σ(2^d−1)−1) and
  C(k)=Σ_{d|k}μ(k/d)(τ(2^d−1)−1). Specialise k=60: μ(60/d)≠0 only for
  d∈{60,30,20,12,10,6,4,2}, so S(60) and C(60) are 8-term signed sums.
  Then the certificate: each σ(2^d−1)/τ(2^d−1) is computed from the
  factorization of 2^d−1 into small primes + multiplicativity + the geometric
  sum σ(p^a)=(p^{a+1}−1)/(p−1), and each product is a norm_num/ring-checked
  literal (2^60−1=3²·5²·7·11·13·31·41·61·151·331·1321 gives
  σ(2^60−1)=13·31·8·12·14·32·42·62·152·332·1322). Conclude
  ANSWER=S(60)+C(60)=3010983666182123972 as an equality of naturals, no
  native_decide.
precedent: "The general theorem is Möbius inversion (Rota's poset Möbius
  inversion in finitary arithmetic form): F(n)=sum_{d|n}f(d) for all n iff
  f(n)=sum_{d|n}mu(n/d)F(d). Applied via ord_m(2)|d iff m|2^d-1 (Conrad Thm
  2.1): C(k)=sum_{d|k}mu(k/d)(tau(2^d-1)-1), S(k)=sum_{d|k}mu(k/d)
  (sigma(2^d-1)-1). This is claim mobius-inversion-sourceable, already proved
  and sourced (Stanford pbc Möbius-inversion notes,
  crypto.stanford.edu/pbc/notes/numbertheory/mobius.html; conjunction with
  Conrad Thm 2.1), and machine-verified for k=1..60 in code/pe622/
  verify_answer.py. 'Extract exact order from order-divides-d over d|k' is the
  canonical order-counting Möbius trick; see the generalised-totient / order-
  distribution literature (McCarthy, Combinatorial Aspects of the Generalized
  Euler's Totient, https://onlinelibrary.wiley.com/doi/10.1155/2010/648165;
  Moree, On the distribution of the order over residue classes,
  https://doi.org/10.1090/s1079-6762-06-00168-5). Hypotheses (m odd, gcd(2,m)
  =1) hold. Honest proximity confirmed by the literature: same number-theoretic
  family as the skeleton's divisor-lattice weighting (both are a divisor-
  lattice convolution), so not orthogonal — but it is a fully general, valid,
  independently-verifiable route.
killed-by: none.
```

## The synthesis research made possible (why this is adopted)

The grounding surfaced the fact that changes the choice: **Mathlib already
carries Möbius inversion** (`Nat.sum_mul_moebius`), so the general theorem
`f(n) = Σ_{d|n} μ(n/d)·F(d)` does *not* need to be re-derived — it is a
one-line appeal to a kernel-checked Mathlib result. That removes the only
previously-flagged weakness of this route (that a full poset-Möbius theorem
would be a large proof tree). The remaining Lean work is exactly two rungs:

1. the order-divisibility bijection `ord_m(2) | d ⟺ m | 2^d−1` (Conrad Thm 2.1,
   already claimed as `order-divisibility-conrad`, `status: proved`), applied to
   the count `C` and sum `S`;
2. a certificate: the eight σ/τ values `σ(2^d−1)`, `τ(2^d−1)` for
   `d ∈ {60,30,20,12,10,6,4,2}` (the only `d` with `μ(60/d)≠0`), each checked
   by a single factorization + geometric-sum + product of literals.

## Decisive fact: the Möbius sum and the skeleton coincide term-for-term at k=60

`60 = 2²·3·5`, so `μ(60/d) ≠ 0 ⟺ 60/d` squarefree ⟺ the `2`-exponent of `60/d`
is `≤ 1` ⟺ `d` is **even**. The 8 surviving `d` are the even divisors
`{2,4,6,10,12,20,30,60}`, with sign `μ(60/d) = +1` for
`d ∈ {4,6,10,60}` (then `60/d ∈ {15,10,6,1}`, products of 0 or 2 primes) and
`μ(60/d) = −1` for `d ∈ {2,12,20,30}` (then `60/d ∈ {30,5,3,2}`, products of
1 or 3 primes). So this route's 8-term sum is *identical* to the skeleton's
inclusion-exclusion table (whose three forbidden moduli 2^12−1, 2^20−1,
2^30−1 and their pairwise/triple gcds resolve to exactly these eight σ-values
via `gcd(2^a−1,2^b−1)=2^{gcd(a,b)}−1`). Adopting this route does not abandon
the skeleton's computation — it *re-derives the same table from a general
theorem* with a `formalised`-capable proof tree, and the skeleton's already-
computed numbers become the independent second check of the certificate.
