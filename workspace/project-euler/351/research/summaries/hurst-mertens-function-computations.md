# Hurst, "Computations of the Mertens function and improved bounds on the Mertens conjecture" (2016)

Source: https://arxiv.org/pdf/1610.08551 — full text at
`research/sources/hurst-mertens-function-computations.full.md`.

## What this source establishes

- The Mertens conjecture |M(x)/√x| < 1 is false (1985); improved bounds
  −1.837625 and 1.826054 for liminf/limsup of M(x)/√x.
- M(x) computed for all x ≤ 10^16 (extrema, zeros, 10⁸ sampled values) and
  for all powers of two up to 2^73, using an O(x^{2/3+ε}) algorithm.

## Hypotheses

None beyond Mertens-function computation. Holds here.

## What it lets this run do

- Reference context for Mertens-function computations; the O(x^{2/3}) claim
  corroborates the complexity tier of the DR/HT/Brown algorithms.

## What it does not settle

- No totient values; not load-bearing for the final answer (the run computes
  Φ directly by sieve + Möbius sum, without a Mertens subroutine).

## Claims

```claim
id: mertens-computation-context
statement: M(x) can be computed for all x ≤ 10^16 and powers of two to 2^73;
Mertens conjecture false; |M(x)/√x| bounds ±1.8376/1.8261.
hypotheses: none.
holds-here: yes (context only).
status: catalogued (Hurst 2016).
bearing: corroborates feasibility of Mertens-based totient methods; not used
in the final computation.
anchor: research/summaries/hurst-mertens-function-computations.md
```
