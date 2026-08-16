---
id: p1-proof-order-two
kind: proof
---
Prove this in Lean 4, with a complete proof and no `sorry`:

> For every natural number `n ≥ 1`, `n` divides `2 ^ (n.totient) - 1` whenever
> `n` is odd.

State it as a `theorem odd_dvd_two_pow_totient_sub_one`. Search Mathlib for the
Euler–Fermat theorem rather than proving it from scratch. Finish with
`#print axioms odd_dvd_two_pow_totient_sub_one`.
