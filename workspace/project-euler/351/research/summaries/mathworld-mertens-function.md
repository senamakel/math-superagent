# MathWorld — Mertens function

Source: https://mathworld.wolfram.com/MertensFunction.html — full text at
`research/sources/mathworld-mertens-function.full.md`
[[mathworld-mertens-function.full]]

## What this source establishes

**Definition.** M(n) = Σ_{k=1..n} μ(k). Values 1, 0, −1, −1, −2, −1, −2, …
(OEIS A002321). M(n) is the determinant of the n×n Redheffer matrix.
M(10^n) = 1, −1, 1, 2, −23, −48, 212, 1037, 1928, −222, … (n = 0..9, via
Deléglise–Rivat 1996).

## Hypotheses

n ≥ 1 integer. Holds here.

## What it lets this run do

- Reference for the Mertens function used in the Mertens-first totient
  formula (Brown Algorithm 1); check values for any Mertens-based route. The
  run's chosen method (direct totient sieve + Möbius sum) does not need M, so
  this is reference/context.

## What it does not settle

- No totient values; no algorithm with complexity bound.

## Claims

```claim
id: mertens-function-reference
statement: M(n) = Σ_{k≤n} μ(k); M(10^n) = 1, −1, 1, 2, −23, −48, 212, 1037,
1928, −222, … for n = 0..9.
hypotheses: none beyond the definition.
holds-here: yes (reference values only; not used in the final computation).
status: catalogued (MathWorld, after Deléglise–Rivat).
bearing: check values for Mertens-based totient computations.
anchor: research/summaries/mathworld-mertens-function.md
```
