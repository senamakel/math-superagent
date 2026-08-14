# OEIS A000010 — Euler's totient function

Source: https://oeis.org/A000010 — full text at
`research/sources/oeis-A000010-euler-totient.full.md`
[[oeis-A000010-euler-totient.full]]

## What this source establishes

**Definition.** φ(n) = number of totatives of n (integers 1 ≤ k ≤ n with
gcd(k,n)=1), equivalently the degree of the n-th cyclotomic polynomial, the
number of generators of a cyclic group of order n, the number of primitive
n-th roots of unity.

**Values.** 1, 1, 2, 2, 4, 2, 6, 4, 6, 4, 10, … (matches the run's
`code/out/seq_phi.txt`).

**Asymptotic.** Σ_{k=1..n} φ(k) ~ (3/π²)n² (Steven Finch), the summatory
totient's growth, consistent with the run's Φ(10⁸)/10¹⁶ = 0.303964.

## Hypotheses

n ≥ 1 integer. Holds here.

## What it lets this run do

- Defines the arithmetic object whose summatory value Φ(10⁸) is the whole
  computational content of PE 351 (all other content is the geometric identity
  H(n) = 3n²+3n−6Φ(n)).

## What it does not settle

- No summatory values; no orchard geometry.

## Claims

```claim
id: totient-definition-and-growth
statement: φ(n) = #{1 ≤ k ≤ n : gcd(k,n)=1}; Σ_{k≤n} φ(k) ~ (3/π²)n².
hypotheses: n ≥ 1 integer.
holds-here: yes — φ values reproduced in seq_phi.txt; growth constant matches
Φ(10^8)/10^16 = 0.303964.
status: sourced (OEIS A000010).
bearing: defines Φ, the quantity PE 351 reduces to.
anchor: research/summaries/oeis-A000010-euler-totient.md
```
