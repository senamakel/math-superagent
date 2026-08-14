# OEIS A002321 — Mertens function

Source: https://oeis.org/A002321 — full text at
`research/sources/oeis-A002321-mertens-function.full.md`
[[oeis-A002321-mertens-function.full]]

## What this source establishes

**Definition.** M(n) = Σ_{k=1..n} μ(k), the Mertens function (partial sums of
the Möbius function A008683).

**Values.** 1, 0, −1, −1, −2, −1, −2, −2, −2, −1, −2, …; M(10^n) = 1, −1, 1,
2, −23, −48, 212, 1037, 1928, −222, … (the last via Deléglise–Rivat).

**Growth.** On the Riemann Hypothesis M(n) << √n exp(...); unconditionally the
Mertens conjecture is false (MathWorld A002321/MertensFunction record the
counterexample story; Hurst gives refined bounds).

## Hypotheses

n ≥ 1 integer. Holds here.

## What it lets this run do

- Reference values for the Mertens subroutine of the Mertens-first totient
  route. The run's actual method (direct φ sieve + Möbius-inversion sum) does
  not need M beyond the recursion-free check values, so this source is
  reference/context, not load-bearing.

## What it does not settle

- No totient values; no algorithm with complexity bound (that is
  Deléglise–Rivat, Helfgott–Thompson).

## Claims

```claim
id: mertens-values-catalogued
statement: M(n) = Σ_{k≤n} μ(k); M(10^n) = 1, −1, 1, 2, −23, −48, 212, 1037,
1928, −222, … for n = 0..9.
hypotheses: none beyond the definition.
holds-here: yes (reference values only; not used in the final computation).
status: catalogued (OEIS A002321).
bearing: check values for any Mertens-based totient computation.
anchor: research/summaries/oeis-A002321-mertens-function.md
```
