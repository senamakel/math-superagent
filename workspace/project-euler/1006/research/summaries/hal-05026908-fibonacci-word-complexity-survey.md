# Hamoud & Abdullah — Improvement ergodic theory for the infinite word F on Fibonacci density (HAL hal-05026908) — summary

<!-- source: https://hal.science/hal-05026908v1/document | converted from PDF -->

## What it is

A 2025 survey (CC-BY-4.0, HAL hal-05026908, Jasem Hamoud & Duaa Abdullah) of the
combinatorial complexity of the infinite Fibonacci word F (substitution 0->01,
1->0 — exactly the PE1006 S_n limit). It collects the standard definitions —
factor complexity, arithmetic complexity, uniform frequency, Pisot substitution
— and proves the Fibonacci word's complexity and density results.

## What it establishes (statements)

- **Def 1.1** — factor complexity p_w(k) = number of distinct factors of length k.
  "All infinite words with exactly n+1 distinct subwords of length n belong to
  the family of Sturmian words." → the Fibonacci word is Sturmian, p_F(n) = n+1.
- **Def 2.3** — the Fibonacci word has asymptotic density of 1's equal to 1/phi^2
  (phi = (1+sqrt5)/2), since the ratio of 0's to 1's converges to phi.
- **Prop 2.1** — balance bound: |#ones(factor of length n)/n − 1/phi^2| ≤ 1/n,
  i.e. every length-n factor has #ones within 1 of n/phi^2. This is the
  Sturmian balance property in quantitative form.
- **Thm 3.2** — the factor complexity and the arithmetic complexity of the
  infinite Fibonacci word are both full in the studied generalisation.
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