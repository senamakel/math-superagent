<!-- source: https://www.ams.org/journals/mcom/1990-54-189/S0025-5718-1990-0993927-5/S0025-5718-1990-0993927-5.pdf | converted from PDF -->

# Cohen (1990), *On an integer's infinitary divisors*, Math. Comp. 54(189) 395–411

Full text: [[cohen-1990-infinitary-divisors.full]] (AMS PDF, clean).

**Setup.** `k`-ary divisors by induction: 1-ary = unitary; `k`-ary for `k ≥ 2`
iff `gcd_k−1(d, n/d) = 1`; infinitary = limit `k → ∞`. On prime powers
`p^x |_∞ p^y` iff the binary expansions of `x` and `y` are disjoint.

## Statements (proved in the paper)

- Theorem 1: `p^x |_k p^y` iff `k > y−1` implies `x ≤ y` (refinement rules).
- Theorems 2–13: complete description of infinitary divisors of `p^y`
  (binary-expansion criterion), multiplicativity, and counting.
- Theorem 14: if `σ_∞(n) = q·n` with `q` prime and `q^{2a} ∥ n`, then
  `σ_∞(q^n)...` (divisibility propagation).
- **Theorem 16: the only infinitary perfect numbers not divisible by 8 are
  `6, 60, 90`.**

## Bearing on this run

Theorem 16 is the classification of a *different* divisor family: infinitary
perfect numbers include 90 but exclude 87360 (which is unitary-but-not-
infinitary perfect: `87360` is `2^6·3·5·7·13`, and infinitary rules differ).
Because the run's target class (unitary) is a strict subfamily of the
infinitary family on the divisor-hierarchy ladder, Theorem 16 is *adjacent
evidence*, not a constraint: it classifies `{6,60,90}` for infinitary
perfection but says nothing about the `σ*(n) = 2n` question beyond those three
happening to be both. The adjacent-divisor-classes note
(`research/notes/adjacent-divisor-classes-classified.md`) records the
cohen1990 claim already; this digest adds the precise setup and Theorem 14.

```claim
id: cohen1990-infinitary-divisor-classified
statement: k-ary/infinitary divisor structure on prime powers is governed by
  binary-expansion disjointness; the only infinitary perfect numbers not
  divisible by 8 are 6, 60, 90 (Theorem 16).
hypotheses: sigma_inf(n) = 2n, 8 ∤ n
holds-here: yes but only as adjacent-divisor background -- unitary perfect is a
  different (more restrictive) hierarchy of perfect numbers; 87360 is not
  infinitary perfect
status: asserted
bearing: context for the adjacent divisor classes; no constraint on a sixth
  unitary perfect number
anchor: research/sources/cohen-1990-infinitary-divisors.full.md
answers: whether-cohen1990-constrains-sixth-upn
```