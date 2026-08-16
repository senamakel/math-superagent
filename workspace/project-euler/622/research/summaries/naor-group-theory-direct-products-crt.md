# Naor — Group Theory notes (Section 6.1: direct products and CRT)

> Summary of `research/sources/naor-group-theory-direct-products-crt.full.md`
> Source: https://web.math.princeton.edu/~naor/homepage%20files/products.pdf (N. Naor / Princeton MATH 113 course notes on groups)

## Relevance to PE622

PE622 needs to decompose the multiplicative order of 2 mod n over the prime-power
factors of n. This notes packet supplies the two group-theoretic rungs of that
decomposition as clean, citable statements.

## The two rungs

1. **Exercise 6.1.20** — order in a direct product:
   For an element `x = (a, b)` in the direct product group `A × B`, the order is
   `o(x) = lcm(o(a), o(b))`. Proof: `x^m = e ⟺ a^m = e` and `b^m = e`; and in any
   group `g^m = e ⟺ m` is a multiple of `o(g)`. So `m` must be a common multiple of
   `o(a)` and `o(b)`, and the least such is the lcm. The hint makes clear the
   exercise extends to finitely many factors, giving
   `o((a_1,...,a_r)) = lcm(o(a_1),...,o(a_r))`.

2. **Theorem 6.1.32** — CRT unit-group isomorphism:
   If `m, n > 1` are relatively prime and `U_m, U_n, U_mn` are the multiplicative
   groups of units, then `(U_mn, ·) ≅ (U_m, ·) × (U_n, ·)`. Proof: the CRT
   bijection `ψ : Z_mn → Z_m × Z_n` is a ring isomorphism (intertwines + and ·),
   and ring isomorphisms send units to units; the units of a direct product ring
   are the product of the separate unit groups. (Text also gives `|U_mn| =
   |U_m|·|U_n|` as a consequence.)

## The decomposition it yields

Combining the two (extending 6.1.32 by induction to pairwise-coprime prime powers
`p_i^{a_i}`, and 6.1.20 to the resulting direct product):

For `n = ∏ p_i^{a_i}` with `p_i` distinct primes and `gcd(a, n) = 1`,

```
ord_n(a) = lcm( ord_{p_1^{a_1}}(a), ..., ord_{p_r^{a_r}}(a) )
```

This is the exact statement the Lean prime-power enumeration rung needs, and it is
now locally sourceable as a Cited axiom. Chappelon Prop 5 (already in library)
supplies the complementary divisibility `ord_{mn}(a) | lcm(ord_m(a), ord_n(a))`
for coprime m,n.

## Cross-references in library

- `chappelon-multiplicative-order-modulo-n` (Prop 5: order divides lcm for coprime moduli)
- `conrad-orders-units-modular-arithmetic` (Theorem 2.1: `a^k ≡ 1 mod m ⟺ n | k`; order of product)
- `diegonsis…` diaconis-graham-kantor Lemma 1 (out-shuffle order = order of 2 mod 2n−1)
