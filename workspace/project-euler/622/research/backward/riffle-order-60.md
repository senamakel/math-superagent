# Proof skeleton: sum of n with s(n) = 60 (Project Euler 622)

The goal is a sum over decks whose out-shuffle order is 60. The reduction
chain below turns the whole question into (i) one structural fact about the
out-shuffle, (ii) a divisibility criterion for the order being exactly 60,
(iii) an inclusion-exclusion over divisors, and (iv) two small finite
computations (one factorisation, one table of divisor sums).

```skeleton
goal: SUM_{n positive even, s(n)=60} n = 3010983666182123972
implies: s(n)=60 iff ord_{n-1}(2)=60 (G-shuffle-order); those m=n-1 are exactly the divisors of 2^60-1 not dividing 2^12-1, 2^20-1, 2^30-1 (G-ord-criterion); inclusion-exclusion with gcd intersections from G-gcd-mersenne gives S and C (G-inclusion-exclusion); G-factorization + G-divisor-sums evaluate them, and C + S = 3010983666182123972.
rests-on: none
status: sketched
```

All the arithmetic in the last two paragraphs is a fixed string of additions
and subtractions of naturals, so once G-factorization and G-divisor-sums supply
the literals it closes by `norm_num` — no `native_decide` anywhere. The literal
answer is stated here from hand arithmetic and must be re-derived by the
G-divisor-sums route (and independently by a brute-force check at small order)
before it is trusted.

```gap
id: G-shuffle-order
lemma: |
  For every even n >= 4, the out-shuffle (riffle shuffle that fixes the top and
  bottom cards) has order s(n) = ord_{n-1}(2), the multiplicative order of 2
  modulo n-1.  Concretely, reindex the moving cards by j = i-1 for i = 2..n-1:
  the shuffle sends j -> 2j mod (n-1), i.e. the card at position i lands at
  position (2i - 1) mod (n-1); cards 1 and n are fixed.  So the shuffle is the
  permutation "multiply by 2 in (Z/(n-1))^*" on the n-2 moving cards, whose order
  is ord_{n-1}(2).  (Edge case: n = 2 has no moving cards and s(2) = 1; it is
  handled separately and contributes nothing to the s(n) = 60 sum.)
status: open
next: |
  theorem_prover: state and prove in code/lean/Lib/Shuffle.lean the position-map
  lemma (card at position i, 2 <= i <= n-1, lands at position (2*i-1) mod (n-1);
  positions 1 and n fixed), then derive  shuffleOrder n = Nat.orderOf (2 : ZMod (n-1))
  for n >= 4.  In parallel tool_builder writes code/brute.py reproducing s(52)=8,
  s(86)=8, SUM{s(n)=8}=412 as the oracle confirming the out-vs-in reading.
```

```gap
id: G-ord-criterion
lemma: |
  For odd m,  ord_m(2) = 60  iff  ( m | 2^60 - 1  and  m !| 2^12 - 1  and
  m !| 2^20 - 1  and  m !| 2^30 - 1 ).
  Reason: 2^60 == 1 (mod m) iff ord_m(2) | 60; the proper divisors of 60 are
  exactly those d with d | 12 or d | 20 or d | 30, and m | 2^d - 1 iff
  ord_m(2) | d; a < b implies 2^a - 1 | 2^b - 1.
status: open
next: |
  theorem_prover: prove  orderOf (2 : ZMod m) = 60  <->  (m | 2^60-1 && m !| 2^12-1
  && m !| 2^20-1 && m !| 2^30-1)  for odd m, using  orderOf_dvd_iff /
  pow_eq_one_iff_dvd_orderOf and the finite divisibility fact {proper divisors of 60}
  <= union of divisors of {12,20,30} (checked by norm_num).
```

```gap
id: G-gcd-mersenne
lemma: |
  gcd(2^a - 1, 2^b - 1) = 2^gcd(a,b) - 1  for positive integers a, b.
status: open
next: |
  theorem_prover: prove in code/lean/Lib/Mersenne.lean (e.g. write 2^a-1 as a sum of
  powers of 2^gcd(a,b), or use  gcd(pow_sub_one, pow_sub_one)  if Mathlib has it);
  first grep Mathlib for  pow_sub_one  /  Nat.gcd  to avoid re-deriving a known lemma.
```

```gap
id: G-inclusion-exclusion
lemma: |
  With N = 2^60 - 1 and M = { m | N : m !| 2^12-1, m !| 2^20-1, m !| 2^30-1 }:

      S = SUM_{m in M} m
        = sigma(N) - sigma(2^12-1) - sigma(2^20-1) - sigma(2^30-1)
          + sigma(15) + sigma(63) + sigma(1023) - sigma(3),
      C = |M|
        = tau(N) - tau(2^12-1) - tau(2^20-1) - tau(2^30-1)
          + tau(15) + tau(63) + tau(1023) - tau(3),

  where sigma = sum of positive divisors, tau = number of positive divisors.
status: open
next: |
  theorem_prover: expand the indicator  1 - [m|2^12-1] - [m|2^20-1] - [m|2^30-1]
  + [m|15] + [m|63] + [m|1023] - [m|3]  over the divisor lattice of N, summing m (and
  summing 1 for C), with G-gcd-mersenne supplying the pairwise/triple gcds; state it
  as two Lean equalities about Finset.sum over (Nat.divisors N).
```

```gap
id: G-factorization
lemma: |
  2^60 - 1 = 3^2 * 5^2 * 7 * 11 * 13 * 31 * 41 * 61 * 151 * 331 * 1321,
  and each of 3,5,7,11,13,31,41,61,151,331,1321 is prime.
status: open
next: |
  tool_builder: verify the product equals 2^60-1 by one exact Python multiplication
  (certificate pattern — the search is external, the check is one multiply);
  theorem_prover: prove the product equality and each Nat.Prime by norm_num /
  decide (all factors <= 1321, small enough for the kernel).
```

```gap
id: G-divisor-sums
lemma: |
  sigma and tau are multiplicative over coprime arguments, with
  sigma(p^k) = (p^(k+1) - 1)/(p - 1)  and  tau(p^k) = k + 1.  Consequently,
  using G-factorization,
      sigma(N) = 3010983668199456768,  tau(N) = 4608,
      sigma(2^12-1) = 8736,  sigma(2^20-1) = 1999872,  sigma(2^30-1) = 2015330304,
      tau(2^12-1) = 24, tau(2^20-1) = 48, tau(2^30-1) = 96,
      sigma(15)=24, sigma(63)=104, sigma(1023)=1536, sigma(3)=4,
      tau(15)=4, tau(63)=6, tau(1023)=8, tau(3)=2.
status: open
next: |
  theorem_prover: prove multiplicativity (Mathlib ArithmeticFunction or
  Nat.sumDivisors) and sigma(p^k) = (p^(k+1)-1)/(p-1); then compute each explicit
  sigma/tau value with norm_num from the prime factorisations (2^12-1 = 3^2*5*7*13,
  2^20-1 = 3*5^2*11*31*41, 2^30-1 = 3^2*7*11*31*151*331).  This literal table is the
  certificate that turns the inclusion-exclusion into the final number.
```
