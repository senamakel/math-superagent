# Lane Clark — Multiplicities of integer arrays (INTEGERS 10 (2010) #A14)

Source: Lane Clark, "Multiplicities of integer arrays," INTEGERS 10 (2010) 187–199.
URL: https://emis.muni.cz/journals/INTEGERS/papers/k14/k14.pdf  (full text held at
`research/sources/lane-clark-array-multiplicity.full.md`)

## What this source is

A **general abstract framework** for bounding the multiplicity of a value in a
triangular integer array, applied to binomial coefficients, Narayana numbers,
Eulerian numbers, and quasi-Eulerian numbers. It is not a new bound for
Singmaster — for binomials it *re-derives* Singmaster's `N(a) = O(log a)` as a
corollary of a general theorem. Its value to this run is structural: it states
*the exact template that produces a logarithmically-growing bound*, which is
precisely the mechanism Singmaster's conjecture says can be pushed to `O(1)`.

## The framework (normal arrays)

An array `a(n,k)` is **normal** if it satisfies, with parameters
`(d, f, r, Δ, g)`:

- **semi-triangular**: `a(n,k) ≠ 0 ⇔ 0 ≤ k ≤ d(n)` for strictly increasing `d`
- **increasing**: `a(n+1,k) > a(n,k)` for `1 ≤ k ≤ d(n)` (values grow down a column)
- **semi-unimodal**: peak column `f(n)`; each row is non-decreasing up to `f(n)`
- **multiplicity `r`**: any identical value occurs in at most `r` distinct
  columns per row (for binomials `r = 2`, the two mirrors `k` and `n−k`)
- **Δ-bounded**: `f(n) ≤ f(n−1) + Δ` (peak column creeps by at most Δ per row)
- **growth function `g`**: strictly increasing, `g(f(n)) ≤ a(n,f(n))` — the
  value at the peak column of row `n` is at least `g(f(n))`

**Theorem 2 (main):** for a normal array `a = (a,d,f,r,Δ,g)`,
`N_a(t) < r(g⁻¹(t) + Δ)` for all `t ≥ 2`, where `g⁻¹` inverts the growth function.

**Corollary 3:** if `g(x) = τ^{x−c}` (exponential growth), then
`N_a(t) < r(log_τ t + c + Δ) = O(log t)`.
**Corollary 4:** if `g(x) = Ω(τ^x)`, then `N_a(t) = O(log_τ t)`.

**Best-possible:** Examples 5 and 6 (explicitly constructed normal arrays with
polynomial and exponential growth) achieve `N_a(t) = (2/3)t^{1/s}` and
`N_a(t) = (2/3)log_s t` respectively for infinitely many `t` — so the
`O(log t)` shape cannot be improved *within the general theorem*: the only way
a better bound appears is via special structure of a particular array (exactly
what Kane's 2007 refinement and MRSTT's interior theorem add for binomials).

## The binomial case (Example 7)

The binomial array is normal with `d(n)=n`, `f(n)=⌊n/2⌋`, `g(x)=2^x` (since
`C(n,⌊n/2⌋) ≥ 2^{⌊n/2⌋}`), `r=2` (two mirrors), `Δ=1`. `g⁻¹(x)=log₂x`, so
Theorem 2 gives:

> **`N(a) < 2 log₂ a + 2` for `a ≥ 2`** — exactly Singmaster's bound.

This is a clean, self-contained reproof of the O(log a) bound with an explicit
constant, and a good independent cross-check on the run's `best-unconditional-bound`
history claim. The reduction is transparent: the log arises because the peak of
row `n` is `C(n,⌊n/2⌋) ≥ 2^{n/2}`, so any `a` can appear only in rows `n ≤ 2 log₂ a`.

Clark also records the standard facts (all attested by held primaries):
Singmaster's search to `2^48` (`N(a)≤8`, `N=6` for {120,210,1540,7140,11628,24310},
`N=8` only for 3003), the infinite `N(a)≥6` family, Singmaster's two conjectures
(`O(1)` and `N(a)≤10`), and Abbott–Erdős–Hanson's `O(log a/log log a)` via
Ingham's prime-gap theorem.

## Bearing on this problem

- Gives the **structural mechanism** behind every log bound (peak growth `g`,
  mirror multiplicity `r`, unimodality): the conjecture is equivalent to a
  normal-array bound becoming constant, which the general Theorem 2 proves
  impossible to obtain from the template alone. Improvement needs *binomial-specific*
  structure — this is the same wall MRSTT/Kane/effective-curve methods hit, now
  seen as a theorem about the template.
- Confirms the counting-convention sensitivity: `r=2` is exactly the two-mirrors
  multiplicity, so `N(a) < 2 log₂ a + 2` is in the "both mirrors" convention.
- Adds array-theory context to the frontier's "general theorems about
  multiplicities" angle (adjacent to the multinomial generalization
  De Koninck–Doyon–Verreault 2021).

```claim
id: lane-clark-normal-array-bound
statement: For any normal integer array a=(a,d,f,r,Δ,g) (semi-triangular, increasing,
  semi-unimodal, multiplicity r, Δ-bounded peak, growth function g), N_a(t) <
  r(g^{-1}(t)+Δ) for t>=2; if g(x)=τ^{x-c} then N_a(t) < r(log_τ t + c + Δ). For the
  binomial array (d(n)=n, f(n)=⌊n/2⌋, g(x)=2^x, r=2, Δ=1) this gives N(a) < 2 log_2 a + 2,
  exactly Singmaster's bound. The O(log t) shape is best possible within the general
  template (Examples 5,6 achieve Θ(t^{1/s}) and Θ(log_s t) for infinitely many t), so
  a constant bound requires binomial-specific structure beyond normality.
hypotheses: "normal array" as defined in the paper; binomial case uses the two-mirror
  counting convention (k and n-k distinct), each row's peak C(n,⌊n/2⌋)>=2^{⌊n/2⌋}.
holds-here: yes
status: checked (independent re-derivation against code/out/witnesses.json and brute
  force over 2<=a<=60, both pass; fresh operator run captured at
  code/out/verify_lane_clark_bound.newcaptured.txt, EXIT_CODE=0, 2025; prior capture
  code/out/verify_lane_clark_bound.captured.txt deliberately NOT adopted as evidence)
effective: yes (the bound is an explicit inequality N(a) < 2 log₂ a + 2 with
  a computable constant; it does NOT inherit from Faltings or Siegel)
uniform-in-k: yes (same bound holds regardless of which (k1,k2) pairs produce the
  collisions; it bounds total multiplicity without distinguishing columns — but it
  grows with a, so it is uniform-in-k without being O(1))
bearing: gives a self-contained structural reproof of the O(log a) bound and names
  the exact template-level obstruction: within any normal-array bound the log is
  irreducible, so constancy must come from binomial-specific structure. Corroborates
  best-unconditional-bound and singmaster-bounds-history; supports the
  effective-methods-wall uniformity argument.
anchor: research/summaries/lane-clark-array-multiplicity.md
```
