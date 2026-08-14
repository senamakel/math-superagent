# Wikipedia — Möbius function

Source: https://en.wikipedia.org/wiki/M%C3%B6bius_function — full text at
`research/sources/wikipedia-mobius-function.full.md`
[[wikipedia-mobius-function.full]]

## What this source establishes

**Definition.** μ(1) = 1; μ(n) = (−1)^k if n is the product of k distinct
primes; μ(n) = 0 if n has a squared prime factor. μ is multiplicative; the
Mertens function is its partial sums. First values 1, −1, −1, 0, −1, 1, −1, 0,
0, 1, … (OEIS A008683).

**Möbius inversion.** f(n) = Σ_{d|n} g(d) ⟺ g(n) = Σ_{d|n} μ(d) f(n/d); with
f = id, g = φ this gives φ(n) = Σ_{d|n} μ(d)·(n/d), the identity behind the
run's Möbius-inversion computation of Φ(10⁸).

## Hypotheses

n ≥ 1 integer. Holds here.

## What it lets this run do

- Independent (non-OEIS) source for the definition and inversion formula used
  by verify_mobius.py.

## What it does not settle

- No summatory values; no algorithm.

## Claims

```claim
id: mobius-inversion-formula
statement: f(n) = Σ_{d|n} g(d) for all n ⟺ g(n) = Σ_{d|n} μ(d) f(n/d); hence
φ(n) = Σ_{d|n} μ(d)·(n/d) and Φ(N) = (1/2)Σ_{d≤N} μ(d)⌊N/d⌋(1+⌊N/d⌋).
hypotheses: n ≥ 1 integer.
holds-here: yes — the summatory form reproduces Φ(10^8) exactly in
verify_mobius.py.
status: sourced (Wikipedia Möbius function).
bearing: second-source backing for the independent verification route.
anchor: research/summaries/wikipedia-mobius-function.md
```
