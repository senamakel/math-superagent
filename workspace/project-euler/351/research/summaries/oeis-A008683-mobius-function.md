# OEIS A008683 — Möbius function

Source: https://oeis.org/A008683 — full text at
`research/sources/oeis-A008683-mobius-function.full.md`
[[oeis-A008683-mobius-function.full]]

## What this source establishes

**Definition.** μ(1)=1; μ(n) = (−1)^k if n is the product of k distinct
primes; μ(n) = 0 otherwise (n has a squared prime factor).

**Values.** 1, −1, −1, 0, −1, 1, −1, 0, 0, 1, −1, …

**Möbius inversion (the property the run uses).** f(n) = Σ_{d|n} g(d) for all n
⟺ g(n) = Σ_{d|n} μ(d)·f(n/d) for all n. With f = id (n ↦ n), g = φ, this is
the φ = μ ∗ id identity behind the summatory-totient Möbius formula.

**Note.** μ(0) is best left undefined (older Maple defined μ(0) = −1; unwise).

## Hypotheses

n ≥ 1 integer. Holds here.

## What it lets this run do

- Supplies the μ values (computed by the int8 sieve in verify_mobius.py) for
  the independent Möbius-inversion computation of Φ(10⁸), which agrees
  exactly with the direct totient sieve.

## What it does not settle

- No summatory values (that is A002321, the Mertens function).

## Claims

```claim
id: mobius-function-definition
statement: μ(1)=1; μ(n) = (−1)^k for n a product of k distinct primes,
μ(n) = 0 if n has a squared prime factor; φ(n) = Σ_{d|n} μ(d)·(n/d).
hypotheses: n ≥ 1 integer.
holds-here: yes — verify_mobius.py's int8 μ sieve and the Möbius-inversion
sum reproduce Φ(10^8) exactly.
status: sourced (OEIS A008683).
bearing: the function behind the second verification route to Φ(10^8).
anchor: research/summaries/oeis-A008683-mobius-function.md
```
