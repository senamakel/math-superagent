# CRT / lcm decomposition of multiplicative orders — clean sourceable statement

Fills request `clean-sourceable-statement-9a7c`: a clean, citable statement
(with hypotheses) that for coprime m, n and gcd(a, mn) = 1,

```
ord_{mn}(a) = lcm(ord_m(a), ord_n(a))
```

## The two-rung statement

**Rung 1 — CRT group isomorphism.** For coprime m, n the multiplicative
groups of units decompose:

```
(Z/mn)^× ≅ (Z/m)^× × (Z/n)^×
```

Anchor: TCD course notes, *The Chinese Remainder Theorem* (ch05.pdf),
Theorem 5.4 (`research/sources/tcd-crt-orders-course-notes.full.md`)
— "If gcd(m,n)=1 then (Z/mn)^× = (Z/m)^× × (Z/n)^×". Built on the ring
isomorphism Z/(mn) ≅ Z/(m) × Z/(n) (Theorem 5.2). Same fact is Naor
Theorem 6.1.32 (already in library).

**Rung 2 — order in a direct product is the lcm.** For elements a ∈ A,
b ∈ B, the order of (a, b) in the product group A × B is
lcm(o(a), o(b)).

Anchor: Naor, Princeton group-theory notes, Exercise 6.1.20
(`research/sources/naor-group-theory-direct-products-crt.full.md`
line ~359): "Prove that the order o(x) of an element x = (a, b) in the
direct product group A × B is the least common multiple lcm(o(a), o(b))"
with hint x^m = e ⇔ a^m = e and b^m = e. Extends to several factors by
induction.

## Claim

```claim
id: order-lcm-crt-sourceable
statement: For coprime positive integers m, n and any a with
  gcd(a, mn) = 1, the multiplicative order of a modulo mn is
  ord_{mn}(a) = lcm(ord_m(a), ord_n(a)).
  More generally, for pairwise coprime n_1,...,n_r and gcd(a, n_1·...·n_r) = 1,
  ord_{n_1·...·n_r}(a) = lcm_i ord_{n_i}(a).
  In particular for odd m = ∏ p_i^{a_i}, ord_m(2) = lcm_i ord_{p_i^{a_i}}(2).
hypotheses: gcd(m, n) = 1 (for the two-factor form); gcd(a, mn) = 1.
holds-here: yes (the prime-power factors p_i^{a_i} of odd m are pairwise
  coprime, and gcd(2, m) = 1 since m odd).
bearing: This is the rung of the Lean proof that decomposes ord_{n-1}(2)
  over the prime powers of n-1, connecting the prime-power order
  computation to the full modulus. Cited as a Cited axiom with a real source.
status: proved
anchor: TCD Theorem 5.4 (group isomorphism via CRT) + Naor Exercise 6.1.20
  (order in a direct product is lcm of the factors' orders).
answers: clean-sourceable-statement-9a7c
```

## Why each hypothesis is needed

- The pair must be coprime for the CRT ring/group isomorphism to hold. If
  gcd(m, n) > 1, the decomposition fails (e.g. ord_4 vs. the two copies of 2).
- gcd(a, mn) = 1 is what makes a a unit in each factor, so ord_m(a) and
  ord_n(a) are defined. This holds here because m = n−1 is odd, gcd(2, m) = 1.
