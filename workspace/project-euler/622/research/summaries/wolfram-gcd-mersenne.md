# Wolfram Functions — GCD formula 04.08.03.0007 (Mersenne gcd)

> Summary of `research/sources/wolfram-gcd-mersenne.full.md`
> Source: https://functions.wolfram.com/IntegerFunctions/GCD/03/01/0007/

## Statement

For positive integers m, n:

```
gcd(2^m − 1, 2^n − 1) = 2^gcd(m,n) − 1
```

Conditions: `m > 0`, `n > 0` (both integers). This is formula 04.08.03.0007.

## Relevance to PE622

This is the load-bearing `G-gcd-mersenne` rung of the Lean proof: the
inclusion-exclusion over the divisors of `N = 2^60 − 1` needs the gcd of
`2^a − 1` and `2^b − 1` for exponents a,b among {12,20,30,60} to compute the
pairwise/triple intersection terms. Now sourceable as a Cited axiom.

## Note

The identity holds more generally for any base c ≥ 2:
`gcd(c^a − 1, c^b − 1) = c^gcd(a,b) − 1`, but the plain c = 2 statement above
is what this formula page states and what the proof needs.

## Cross-references

- `eom-sum-of-divisors` (σ/τ divisor sums used in the same Lean chain)
- backward `riffle-order-60/G-gcd-mersenne`
