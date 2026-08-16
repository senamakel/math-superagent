# Encyclopedia of Mathematics — Sum of divisors (σ) and number of divisors (τ)

> Summary of `research/sources/eom-sum-of-divisors.full.md`
> Source: https://encyclopediaofmath.org/wiki/Sum_of_divisors

## Statement

The sum-of-divisors function σ (also σ_1) and number-of-divisors function τ
(also σ_0) are multiplicative arithmetic functions:

```
σ(n) = Σ_{d|n} d ,     τ(n) = σ_0(n) = #{d : d|n}
```

and `σ = σ_1`, `τ = σ_0`.

Key facts: they are multiplicative (σ(mn) = σ(m)σ(n) and τ(mn) = τ(m)τ(n) for
gcd(m,n) = 1), and have the Dirichlet series
`Σ σ_k(n) n^-s = Π_p (1-p^-s)(1-p^{k-s})^-1 = ζ(s)ζ(s-k)`.

Note: the page states multiplicativity explicitly ("These are multiplicative
arithmetic functions") and gives σ_k(1) = 1. The prime-power values
σ(p^a) = (p^{a+1}−1)/(p−1), τ(p^a) = a+1 are the standard consequence used in
the Lean chain.

## Relevance to PE622

This is the source for the `G-divisor-sums` rung: computing σ(N), τ(N) for
N = 2^60−1 and the other divisor sums from the inclusion-exclusion, via
multiplicativity over the prime-power factorization. Now sourceable as a Cited
axiom.

## Cross-references

- `wolfram-gcd-mersenne` (gcd rung of same Lean chain)
- backward `riffle-order-60/G-divisor-sums`
- Conrad's notes / DLMF §27.6 (divisor sums) for the multiplicative-structure
  background
