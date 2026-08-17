# Hamoud & Abdullah — Improvement ergodic theory for the infinite word F on Fibonacci density (HAL hal-05026908) — summary

<!-- source: https://hal.science/hal-05026908v1/document | converted from PDF -->

## What it is

A 2025 survey (CC-BY-4.0, HAL hal-05026908, Jasem Hamoud & Duaa Abdullah) of the
combinatorial complexity of the infinite Fibonacci word F (substitution 0->01,
1->0 — exactly the PE1006 S_n limit). It collects the standard definitions —
factor complexity, arithmetic complexity, uniform frequency, Pisot substitution
— and proves the Fibonacci word's complexity and density results.

## Convention caveat (contradiction within the source)

Definition 2.3 and Proposition 2.1 give the density of 1's as 1/φ² ≈ 0.382 —
**the problem's convention**, matching Perrin–Restivo/Berstel. However the
same paper's **Theorem 3.3** states the letter density converges to
lim F(n)/F(n+1) = φ − 1 ≈ 0.618. These two statements concern different words:
1/φ² is the ones-density of the problem's S (substitution 0→01, 1→0); φ−1 = 1/φ
is the frequency of the *other* letter / the complement (rabbit) word. **Do not
use Thm 3.3's 0.618 as the slope of the problem's word** — it is the complement
convention, whose factor set differs. Same 0↔1 trap as MathWorld, Sivasankar–Rama,
Wikipedia notes.

## What it establishes (statements)

- **Def 1.1 / §3** — factor complexity p_w(k) = number of distinct factors of
  length k; "all infinite words with exactly n+1 distinct subwords of length n
  belong to the family of Sturmian words" → the Fibonacci word is Sturmian,
  p_F(n) = n+1.
- **Def 2.3** — the Fibonacci word has asymptotic density of 1's equal to 1/φ²
  (φ = (1+√5)/2), since the ratio of 0's to 1's converges to φ. Uniform:
  every length-m substring has proportion of 1's → 1/φ².
- **Prop 2.1** — balance bound: |#ones(factor of length n)/n − 1/φ²| ≤ 1/n,
  i.e. every length-n factor has #ones within 1 of n/φ². The Sturmian balance
  property in quantitative form.
- **Thm 3.2** — factor/arithmetic complexity of the *base-b concatenation word*
  F_b (concatenation of b-expansions of n!, a different object from the
  substitution word of Def 2.3) are full (b^k). **Do not cite Thm 3.2 for
  PE1006's k+1; the word studied there is not the problem's word.**
- Also: Fibonacci sequence period modulo p (π(p), α(p)), Lucas zeros, Pisot
  substitution material (not needed for PE1006).

## Why it matters for PE1006

The problem's "there are only k+1 different Fibonacci subwords of length k" is
exactly p_F(k) = k+1, which this source states as the Sturmian defining
property. The balance bound is the same structural fact as the mechanical-word
factors being balanced (slope 2-phi, Perrin Lecture 2; Berstel DLT'95) — an
independent confirmation of the factor-complexity foundation and the density
the run's mechanical-word construction implicitly relies on (k+1 factors, each
with ~k/phi^2 ones, so the digit strings are not degenerate).

Full text: `research/sources/hal-05026908-fibonacci-word-complexity-survey.full.md`
(28.7 KB). Claim: `fibonacci-word-sturmian-density-balance`.