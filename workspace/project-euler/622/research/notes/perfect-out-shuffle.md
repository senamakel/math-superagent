# The perfect out-shuffle and PE622

## Source-backed claim: the shuffle-order reduction

```claim
id: outshuffle-order-equals-ord
statement: The number of consecutive perfect out-shuffles (out-faro / riffle
  shuffle, top and bottom cards fixed) needed to restore an even deck of size n
  to its original order is s(n) = ord_{n-1}(2) — the multiplicative order of 2
  modulo the odd number n-1.
hypotheses: n even, n >= 2.
holds-here: yes (n in this problem is even; n-1 odd so gcd(2,n-1)=1).
bearing: This is the entire reduction: the target "sum of n with s(n)=60"
  becomes "sum of even n with ord_{n-1}(2)=60", i.e. over odd m=n-1.
status: proved
anchor: Diaconis-Graham-Kantor (research/sources/diaconis-graham-kantor-perfect-shuffles.full.md) Lemma 1, verified at line ~140; Packard Thm 2.1 (packard-order-perfect-kshuffle.full.md); Pomerance lecture; MathWorld Out-Shuffle; OEIS A002326; Susam.
```

## Why the out-shuffle, not the in-shuffle

The statement's riffle shuffle preserves the location of the top and bottom
card, i.e. it is the **out**-shuffle. (The in-shuffle moves the top card to
second; its order would be ord of 2 mod n+1 — the wrong variant.) DGK Lemma 1
gives both: order of out-shuffle = ord of 2 (mod 2n-1); order of in-shuffle =
ord of 2 (mod 2n+1). Confirmed verbatim at
`research/sources/diaconis-graham-kantor-perfect-shuffles.full.md` line ~140.

Reproduced against statement examples: s(52)=8 because 2^8≡1 mod 51,
s(86)=8 because 2^8≡1 mod 85. The set of even n with s(n)=8 is
{n-1 ∈ {17,51,85,255}} giving n = 18,52,86,256, sum 412 — matching the
statement. (Oracle `code/pe622/oracle_check.py` re-checks mechanically.)

## Consequence for the target

s(n) = 60  <=>  ord_{n-1}(2) = 60.  With m = n-1 (odd), if m = ∏ p_i^{a_i}
then ord_m(2) = lcm_i ord_{p_i^{a_i}}(2).  This enumeration is the scholar's
job, not the library's; the library supplies the theorem.

## Divisibility structure (the computation engine)

```claim
id: order-divisibility-conrad
statement: For a unit a mod m with order n, a^k ≡ 1 (mod m) iff n | k, and
  n | φ(m). Hence ord_m(2) = 60 iff m | 2^60 - 1 and no proper divisor d of 60
  (0 < d < 60) has 2^d ≡ 1 (mod m).
hypotheses: (a, m) = 1.
holds-here: yes (m = n-1 odd, so gcd(2,m)=1).
bearing: turns "sum over n with s(n)=60" into a finite enumeration over the
  divisors of 2^60-1 (m | 2^60-1) with exact-order minimality, rather than an
  unbounded scan over n. This is what defeats enumeration.
status: proved
anchor: Conrad, "Orders of units in modular arithmetic", Theorem 2.1 and
  Corollary 2.2 (kconrad.math.uconn.edu/blurbs/ugradnumthy/ordersmodm.pdf),
  verified at lines 108, 125 of conrad-orders-units-modular-arithmetic.full.md.
  Corollary: ord_m(2)=60 forces each ord_{p^a}(2) | 60, so m | 2^60-1.
```

```claim
id: order-lcm-over-prime-powers
statement: For coprime moduli n1, n2 the standard multiplicative order of a
  unit satisfies ord_{n1·n2}(a) = lcm(ord_{n1}(a), ord_{n2}(a)). In particular,
  for odd m = ∏ p_i^{a_i}, ord_m(2) = lcm_i ord_{p_i^{a_i}}(2).
hypotheses: gcd(a, n1·n2) = 1.
holds-here: yes (the p_i^{a_i} are pairwise coprime).
bearing: reduces the exact-order-60 computation over m to independent
  computations over each prime power p_i^{a_i}: every ord_{p_i^{a_i}}(2) must
  divide 60 and the lcm must be exactly 60.
status: proved
anchor: Two rungs. (i) Naor, Princeton group-theory notes, "products.pdf",
  Thm 6.1.32 (research/sources/naor-group-theory-direct-products-crt.full.md
  ~line 590): for coprime m,n, (U_mn,·) ≅ (U_m,·)×(U_n,·) via the CRT ring
  isomorphism; Ex 6.1.20 (~line 359): order of (a,b) in a direct product is
  lcm(o(a),o(b)), extending to finitely many factors. Together these give
  ord_{n1·n2}(a) = lcm(ord_{n1}(a), ord_{n2}(a)) exactly. (ii) Chappelon,
  "On the Multiplicative Order of a Modulo n", Prop. 5
  (research/sources/chappelon-multiplicative-order-modulo-n.full.md): the
  complementary divisibility α_{n1·n2}(a) | lcm(α_{n1}(a), α_{n2}(a)) for
  coprime moduli.
answers: clean-sourceable-statement-9a7c
```

```claim
id: wieferich-lift-order
statement: If b = ord_p(2) with p an odd prime, then for a>=1 the order of 2
  mod p^a divides b·p^{a-1}, with equality whenever p^b ≢ 1 (mod p^2) (i.e.
  p is not Wieferich-lifting). Equivalently ord_{p^a}(2) = b·p^{a-1}
  for a <= k0+1 where k0 is the largest integer with 2^b ≡ 1 (mod p^{k0}).
hypotheses: p odd prime, a >= 1.
holds-here: yes (applies to the prime-power factors of 2^60-1).
bearing: lets each prime-power order be read off once ord_p(2) is known,
  via the highest power of p dividing 2^ord_p(2)-1. This is ladder rung R-lift.
status: proved
anchor: Packard, "The Order of a Perfect k-Shuffle", Corollary 4.2
  (research/sources/packard-order-perfect-kshuffle.full.md line 795); the
  exact "order = d for k<=k0, dp^{k-k0} for k>=k0" form is Chappelon
  Theorem 3.6.
```
