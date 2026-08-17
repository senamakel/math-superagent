# Encyclopedia of Mathematics — "Resultant"

Source URL: https://encyclopediaofmath.org/wiki/Resultant
Full text: `research/sources/eom_resultant.full.md`.

## What it establishes

The classical resultant `R(f,g)` of two univariate polynomials — definition via
the Sylvester determinant, the fundamental property `R(f,g)=0 ⟺ f,g share a
common root or the leading coefficient of one of them vanishes`, and the
factorisation over the roots: if `f = a ∏(x−α_i)`, `g = b ∏(x−β_j)` then
`R(f,g) = a^m b^n ∏_{i,j}(α_i − β_j)` (with degrees n, m). Includes the
Poisson product formula and the discriminant as the resultant of `f` and `f'`.

## Bearing on the run

- The run's central objects are `R_i = Res_x(f, H_i(f))` over the coefficient
  ring `ℤ[a_1,…,a_n]` (Schaub–Spivakovsky formulation). This reference fixes
  the definition, the root-factorisation identity (used in the run's
  `root-difference-identity-verified` note), and the weighted-homogeneity
  context (each term of the Sylvester determinant carries the weighted degree
  `n·(n−i)` — the `ord_0(R_i) = n(n−i)` proof's Theorem A).
- The "or the leading coefficient vanishes" clause matters for the char-p and
  normalisation handling: over `F_p`, `R_{n−1} = (−1)^n n^n a_n` vanishes
  identically when `p | n` — the bad-prime content degeneracy.

Claim status: reference-level definitions (proved classical facts, used as
such by the run's held primaries).