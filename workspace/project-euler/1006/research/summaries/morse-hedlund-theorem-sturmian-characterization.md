# Formal intercept of Sturmian words (Wojcik) — Morse–Hedlund background

<!-- source: https://hal.science/hal-01827511/document | converted from PDF -->

**Digest replaced.** C. Wojcik, "Formal intercept of Sturmian words" (arXiv:1803.02073,
2018). Introduces the formal intercept (Ostrowski-expansion sequence). Its Sections 1–2
recall with proofs the basics of Sturmian words, which is the banner source for the
Morse–Hedlund theory this problem rests on.

## Key statements

- **Theorem 1 (Morse–Hedlund)**: An infinite word `x` over `A` is ultimately periodic iff
  there exists `n >= 1` with `p(x,n) <= n` (factor complexity `p(x,n)` = number of distinct
  length-`n` factors). Equivalently, an aperiodic word has `p(x,n) >= n+1` for all `n`.
- **Theorem 2(1)** : a balanced infinite word satisfies `p(x,n) <= n+1` for all `n`.
- **Theorem 3(1)** : a balanced word is Sturmian iff its slope is irrational.
- Balanced iff every two equal-length factors differ in number of `1`s by at most 1.

## Bearing on this problem

This is the primary statement of the exact theorem producing the problem's "exactly `k+1`
distinct length-`k` factors" fact: the infinite Fibonacci word is aperiodic (slope
irrational), so Morse–Hedlund gives `p >= k+1`, and it is balanced so `p <= k+1`, hence
`p = k+1`. Full text: `research/sources/morse-hedlund-theorem-sturmian-characterization.full.md`.
