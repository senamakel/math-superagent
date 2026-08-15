<!-- source: http://www.numbertheory.org/php/neuclid.html | nearest integer Euclidean algorithm; primary text preserved from summary (captured 2025, page last modified 26 Jan 2009) -->

# Nearest integer Euclidean algorithm

If r is a real number, by [r] we mean the *nearest integer to r*. Thus
|r - [r]| ≤ 1/2 and if r = t + 1/2, where t is an integer, then [r] = t + 1.
Alternatively, [r] = ⌊ r + 1/2 ⌋, the integer part of r + 1/2. Hence
[r] = r + θ, where -1/2 < θ ≤ 1/2.

Then if m and n are integers, n > 0 and q = [m/n], we have m/n = q + θ, where
-1/2 < θ ≤ 1/2. Hence m = nq + nθ, where -n/2 < nθ ≤ n/2. Hence m = nq + es,
where -n/2 < es ≤ n/2 and s is an integer, 0 ≤ s ≤ n/2 and e = 1 if θ ≥ 0,
while e = -1 if θ < 0. We write e = e(m,n).

Then with r₀ = m and r₁ = n > 0, we define rₖ recursively for 2 ≤ k ≤ l+1,
rₖ > 0 and eₖ₊₁ = e(rₖ₋₁, rₖ), where qₖ = [rₖ₋₁ / rₖ] for 1 ≤ k ≤ l:

    r₀      = r₁ q₁ + e₂ r₂        (-r₁/2 < e₂ r₂ ≤ r₁/2)
    r₁      = r₂ q₂ + e₃ r₃        (-r₂/2 < e₃ r₃ ≤ r₂/2)
    ...
    rₖ₋₁    = rₖ qₖ + eₖ₊₁ rₖ₊₁   (-rₖ/2 < eₖ₊₁ rₖ₊₁ ≤ rₖ/2)
    ...
    rₗ₋₁    = rₗ qₗ

Then rₗ = gcd(m, n).

The sₖ and tₖ are also printed in tabular form, where it is convenient to define
e₀ = 1 = e₁ and

    s₀ = 1, s₁ = 0,  eₖ sₖ = sₖ₋₂ – qₖ₋₁ sₖ₋₁,
    t₀ = 0, t₁ = 1,  eₖ tₖ = tₖ₋₂ – qₖ₋₁ tₖ₋₁,    k = 2, ..., l+1.

Then rₖ = sₖ m + tₖ n for 0 ≤ k ≤ l+1, where rₗ₊₁ = 0. The number of steps is
no greater than the number in Euclid's algorithm.

(Based on Exercise 5, page 67, *Elementary Number Theory and its Applications*,
by Ken Rosen. Also see Chapter 39 (Kettenbrüche nach nächsten Ganzen), page 168,
*Kettenbrüche*, by Oscar Perron, Chelsea 1950.)

We print the nearest integer continued fraction expansion
m/n = q₁ + e₂/q₂ + ⋯ + eₗ/qₗ.

x₀ = m/n, xₙ = aₙ - 1/xₙ₊₁, where aₙ = [xₙ], n ≥ 0.
This gives a continued fraction m/n = a₀ - 1/a₁ - ⋯ - 1/aₗ, where |aᵢ| ≥ 2 for
all i ≥ 1. The notation m/n = (a₀, a₁, ..., aₗ) goes back to A. Hurwitz,
Werke, Seite 85.

*Last modified 26 January 2009.*
