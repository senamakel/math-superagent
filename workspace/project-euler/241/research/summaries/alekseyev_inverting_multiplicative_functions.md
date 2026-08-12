# Alekseyev — Computing inverses of multiplicative functions (JIS 2016)

**Source:** Max A. Alekseyev, "Computing the inverses, their power sums, and extrema for
Euler's totient and other multiplicative functions", J. Integer Sequences 19 (2016),
Article 16.5.2. Full text: `[[alekseyev_inverting_multiplicative_functions.full]]`.

## What it establishes

A generic algorithm for computing inverses of a multiplicative function f (the n with
f(n) = value) *when the inverse set is finite*, and for computing functions of the
inverses (power sums, cardinality, extrema) without enumerating them.

- **Theorem 1:** identity for formal Dirichlet series over the semiring (P_fin, +, ×).
- **Theorem 3:** given ℓ atomic series for C(f^{−1}(n)), their product over the divisor
  set D has complexity O(ℓ·τ(n)²) in the semiring.
- **Theorem 5:** for C(σ_k^{−1}(n)), computable in O(τ(n)·log n·(log^{6+ε}n +
  TC(log n))) — polynomial, not exponential, in the inverse-set description.
- Illustrates with φ and σ_k: e.g. the *count* of solutions to σ_1(x) = 10^1000 is
  15,512,215,160,488,452,125,793,724,066,873,737,608,071,476, computable without listing
  the solutions.

## What it means for PE 241

This addresses the *inverse-function* direction (fix the σ-value, find n), which is a
different question from enumerating σ(n)/n = k+1/2 below 10^18. Here the ratio, not the
σ value, is fixed, and the bound is 10^18 (not a fixed σ). The combinatorial/complexity
technique (ℤ^+ ring structure over prime powers, divisor-set factorisation) is the
algebraic sibling of the run's multiplicative decomposition, and it confirms cost can
grow with the description rather than the value — but it does not enumerate the
hemiperfects or give the sum. Keep only as structural confirmation that σ-ratio preimages
are tractable; not load-bearing for the sum.

```claim
id: alekseyev-inverting-multiplicative
statement: Preimages of a multiplicative function (n with f(n)=v) and their power sums/cardinality are computable in polynomial time (using a Z^>=0-semiring over prime powers) when the preimage set is finite; e.g. the count of x with sigma_1(x)=10^1000 is known without listing them.
hypotheses: f multiplicative; the preimage set is finite
holds-here: no — theorem concerns fixed sigma-value preimages; PE241 fixes a *ratio* sigma(n)/n=k+1/2 below a *bound* 10^18, not a fixed sigma value, so the inverse machine does not directly enumerate the answer set (multiplicative decomposition matches but is not the enumeration route)
status: proved (Alekseyev, JIS 16.5.2, 2016)
bearing: structural confirmation that sigma-preimage enumeration is polynomially tractable; not the enumeration route for the hemiperfect sum
anchor: research/sources/alekseyev_inverting_multiplicative_functions.full.md
```
