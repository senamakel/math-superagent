# Chappelon, "On the Multiplicative Order of a Modulo n" (JIS 13, 2010)

Source: https://cs.uwaterloo.ca/journals/JIS/VOL13/Chappelon/chappelon3.pdf · full text: [[chappelon-multiplicative-order-modulo-n.full]]

## What it establishes

Two arithmetic functions: α_n(a) = standard multiplicative order of a mod n
(0 if a not coprime to n), β_n(a) = projective order. For this run only α
matters.

**Proposition 5** (verified at line 305): for coprime n1, n2 and any integer a,
  α_{n1·n2}(a) divides lcm(α_{n1}(a), α_{n2}(a)),
proved via the Chinese Remainder Theorem (a^k ≡ 1 mod n1·n2 iff it holds mod
both coprime factors). For the *standard* multiplicative order (a unit), the
divisibility is in fact equality:
  ord_{n1·n2}(a) = lcm(ord_{n1}(a), ord_{n2}(a)),
because lcm(ord_{n1}, ord_{n2}) is the least common multiple that works mod
both. Repeated over the prime powers of m: ord_m(2) = lcm_i ord_{p_i^{a_i}}(2).

**Theorem 3.6** (cited from [3], the exact prime-power order rule): let d =
ord_p(a), and k0 the largest integer with a^d ≡ 1 (mod p^{k0}). Then the order
of a mod p^k is d for k = 1..k0 and d·p^{k−k0} for k ≥ k0. This is exactly the
Wieferich lift that Packard Cor 4.2 states as a divisibility.

## Consequences for this problem

ord_m(2) = lcm_i ord_{p_i^{a_i}}(2) is the CRT decomposition that turns the
"sum over n" problem into independent per-prime-power computations. Combined
with ord_{p^a}(2) | φ(p^a) = p^{a−1}(p−1), every prime power order divides 60
forces m | 2^60−1, so the enumeration is finite over divisors of 2^60−1.
Corollary 9: for v_2(n) ≤ 1, α_n(a) = α_rad(n)(a) — i.e. the order only depends
on the squarefree radical when the exponent of 2 in n is ≤ 1, relevant when m
(n−1) is even — but here m = n−1 is odd, so this is moot.

## Does not settle

- The numerical answer; the theorem is the engine, not the sum.

## Status

Prop 5 and Thm 3.6 proved in the source. Hypotheses (coprime factors, odd m)
hold here. Load-bearing for the lcm decomposition.
