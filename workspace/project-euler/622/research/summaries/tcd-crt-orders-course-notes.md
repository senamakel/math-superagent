# TCD course notes — The Chinese Remainder Theorem (ch05)

Source: https://www.maths.tcd.ie/pub/Maths/Courseware/NumberTheory/ch05.pdf · full text: [[tcd-crt-orders-course-notes.full]]

## What it establishes

Lecture notes on the CRT and multiplicative functions. The loading facts:

- **Theorem 5.1 (CRT, coprime moduli):** if gcd(m,n)=1 then for any residues r mod m, s mod n there is N with N≡r (mod m), N≡s (mod n), unique mod mn.
- **Theorem 5.2 (ring iso):** gcd(m,n)=1 ⟹ Z/(mn) ≅ Z/(m) × Z/(n) as rings.
- **Corollary 5.1:** gcd(N,mn)=1 ⟺ gcd(N,m)=1 and gcd(N,n)=1.
- **Theorem 5.3 (φ multiplicative):** gcd(m,n)=1 ⟹ φ(mn)=φ(m)φ(n); φ(p^e)=p^{e−1}(p−1).
- **Theorem 5.4 (multiplicative group iso):** if gcd(m,n)=1 then (Z/mn)^× = (Z/m)^× × (Z/n)^×. This is the statement the run's CRT/lcm order decomposition is built on.
- **Proposition 5.3 (multiple moduli):** pairwise coprime n_1..n_r, given residues, unique solution mod n_1···n_r.
- **Section 5.6:** σ(n) (sum of divisors), d(n)=τ(n), μ(n) are multiplicative.

## Consequences for this problem

Theorem 5.4 is Rung 1 of the clean CRT/lcm statement recorded in `research/notes/crt-lcm-order-decomposition.md` (request `clean-sourceable-statement-9a7c`): it turns "ord_{mn}(2) = lcm(ord_m(2), ord_n(2))" for coprime m,n into the fact that the order of 2 mod mn is the order of the element (2 mod m, 2 mod n) in a direct product, which equals the lcm (Rung 2 = Naor Exercise 6.1.20). Together they give the prime-power decomposition ord_m(2) = lcm_i ord_{p_i^{a_i}}(2) that the Lean proof uses to enumerate m = n−1 with ord_m(2)=60. Section 5.6's multiplicativity of σ and τ is a second anchor for `divisor-sums-gcd-mersenne-sourceable`.

## Does not settle

Only the group/ring isomorphism (existence and uniqueness) — not the prime-power order *lift* (that is Packard/Chappelon/Kiriu), and not any numerical value.

## Status

Standard textbook material, proved in the notes; hypotheses (coprime moduli, gcd(2,m)=1 for odd m) hold here.

```claim
id: crt-multiplicative-group-iso
statement: If gcd(m,n) = 1 then the units modulo mn form the direct product
  (Z/mn)^x = (Z/m)^x × (Z/n)^x via the CRT map. Consequently the order of a
  unit a mod mn is lcm(ord_m(a), ord_n(a)); for pairwise coprime n_1..n_r and
  gcd(a, n_1···n_r) = 1, ord_{n_1···n_r}(a) = lcm_i ord_{n_i}(a).
hypotheses: gcd(m,n) = 1; gcd(a, mn) = 1.
holds-here: yes (m = n-1 odd, so gcd(2,m)=1; prime-power factors of n-1 are
  pairwise coprime).
status: proved
bearing: rung connecting prime-power order computation to the full modulus in
  the Lean proof of the ord_m(2)=60 enumeration.
anchor: research/sources/tcd-crt-orders-course-notes.full.md Theorem 5.4 (+
  Naor Ex 6.1.20 for order-in-direct-product = lcm)
answers: clean-sourceable-statement-9a7c
follows-from: order-lcm-over-prime-powers
```
