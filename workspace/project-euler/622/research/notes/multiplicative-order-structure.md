# Multiplicative order structure for PE622

## The structural fact (finite enumeration)

For odd m = n-1, s(n) = ord_{n-1}(2) (claim `outshuffle-order-equals-ord` in
`perfect-out-shuffle.md`). Specializing:

```
ord_{n-1}(2) = 60   <=>   n - 1 divides 2^60 - 1  AND  no proper
                          divisor d of 60 has 2^d ≡ 1 (mod n - 1).
```

Why: `2^k ≡ 1 (mod m)` means `m | 2^k - 1` (Conrad Thm 2.1), and the exact
order is the certificate that 60 is the *smallest* k with m | 2^k - 1.
Equivalently the exact-order-60 divisors of 2^60-1 are those not dividing
2^d - 1 for any proper divisor d | 60. This makes the search finite
(divisors of 2^60-1), not an unbounded scan over n — the structural fact that
defeats enumeration.

## CRT / lcm decomposition

For pairwise-coprime moduli, multiplicative orders combine by CRT:

```
rad(m) = ∏ p_i,  m | 2^60 - 1,  so  ord_m(2) = lcm_i ord_{p_i^{a_i}}(2)
```

where p_i are the distinct primes of m. ord_{p^a}(2) | λ(p^a) = φ(p^a) for
odd p (Pomerance lecture: Gauss-Carmichael). So the exact prime-power orders
control the whole structure. Claim `order-lcm-over-prime-powers` in
`perfect-out-shuffle.md`.

## Sources

- Diaconis-Graham-Kantor Lemma 1: order of out-shuffle = ord of 2 mod 2n-1;
  order of in-shuffle = ord of 2 mod 2n+1. (The load-bearing reduction.)
- Packard Thm 2.1 / Cor 4.2: k-shuffle order and the Wieferich prime-power
  lift.
- Pomerance lecture: out-shuffle order = l(2n-1) = ord of 2 mod (2n-1); and
  ord_a(n) | λ(n), λ(prime-power)=φ(prime-power) for odd p (Gauss-Carmichael).
- Chappelon Prop 5: for coprime n1,n2, order mod n1·n2 divides lcm of the
  two orders (CRT machinery the enumeration uses).
- Conrad Thm 2.1 / Cor 2.2: n | k when a^k≡1 mod m (order n); and n | φ(m).
- OEIS A114894: a(n) = minimal k with a 2k deck restored after n out-shuffles.
  This is the inverse of s: cross-check for the s=8 value 412.

## Claim: the exact-order-60 criterion

```claim
id: order-equals-sixty-iff-divides-twosixty-minus-one
statement: For odd m >= 1, ord_m(2) = 60 if and only if m | 2^60 - 1 and no
  proper divisor d of 60 with 0 < d < 60 has 2^d ≡ 1 (mod m).
hypotheses: gcd(2, m) = 1 (true since m odd).
holds-here: yes (m = n-1 with n even, so m odd).
bearing: turns the "sum over n with s(n)=60" into a finite enumeration over
  divisors of 2^60-1 (plus exact-order minimality), rather than an unbounded
  scan over n. This is the structural reduction.
status: proved (elementary; follows directly from Conrad Thm 2.1, the
  definition of multiplicative order)
follows-from: order-divisibility-conrad
anchor: definition of multiplicative order (Wikipedia, MathWorld); Conrad Thm
  2.1. Not yet machine-checked.
```
