# Claim: Fibonacci word Sturmian, complexity n+1, uniform density 1/phi^2, balance bound

Additional anchor for `citable-statement-theorem-039a` (already closed by
`fibonacci-sturmian-complexity` and `req-close-factor-complexity`), and a new
source-backed quantitative fact for the mechanical-word route: the uniform
density and balance of the Fibonacci word.

```claim
id: fibonacci-word-sturmian-density-balance
statement: The infinite Fibonacci word F (substitution 0 -> 01, 1 -> 0, the S_n limit of
PE1006) is a Sturmian word with factor complexity p_F(n) = n + 1 for every n >= 0,
and every length-n factor has a number of 1's within 1 of n/phi^2 (uniform density
1/phi^2, balance bound |#1s(F factor) - n/phi^2| <= 1). The ratio of 0's to 1's in
the whole word converges to phi = (1+sqrt5)/2.
hypotheses: F is the infinite Fibonacci word (substitution 0->01, 1->0); phi = (1+sqrt5)/2.
holds-here: true — exactly the word whose length-k factors the problem calls Fibonacci
subwords; the balance bound is the Sturmian balance property.
status: sourced
bearing: Confirms the Sturmian/complexity foundation (p(k)=k+1) and quantifies the
density and balance, which the mechanical-word construction (slope 2-phi, arc-midpoint
reps) uses. Independent of the factor-listing source: a second route to "exactly k+1
factors, each length-k factor balanced".
anchor: research/sources/hal-05026908-fibonacci-word-complexity-survey.full.md
(https://hal.science/hal-05026908v1/document, Def 1.1 factor complexity p_w(k),
Def 2.3 density 1/phi^2, Prop 2.1 balance bound |#1s/n - 1/phi^2| <= 1/n, the
Sturmian/trellis statement "all infinite words with exactly n+1 distinct subwords
of length n belong to the family of Sturmian words").
```

## What the source establishes

**Hamoud & Abdullah, "Improvement ergodic theory for the infinite word F on
Fibonacci density"** (HAL hal-05026908, 2025, CC-BY-4.0) — a survey of
combinatorial complexity of the Fibonacci word:

- **Definition 1.1** — factor complexity p_w(k) = number of distinct factors of
  length k. The Fibonacci word is Sturmian: "All infinite words with exactly
  n+1 distinct subwords of length n belong to the family of Sturmian words."
- **Definition 2.3** — "The Fibonacci word exhibits a precise asymptotic density
  of 1's equal to 1/phi^2, where phi = (1+sqrt5)/2. This arises because the
  ratio of 0's to 1's converges to phi."
- **Proposition 2.1** — balance bound: for any length-n substring, the fraction
  of 1's is within 1/n of 1/phi^2, i.e. |#1s/n − 1/phi^2| ≤ 1/n. This is the
  Sturmian balance property in quantitative form.

## Why it matters for PE1006

The problem's "there are only k+1 different Fibonacci subwords of length k" is
exactly p_F(k) = k+1. The mechanical-word construction (directive 2) models the
k+1 factors as arc-midpoint representatives on a circle cut by the irrational
slope; the balance bound here is the same structural fact as the factors being
balanced (the mechanical/Sturmian equivalence), so this is an independent
confirmation of the foundation claim and of the slope-2-phi mechanical formula
already on disk (Perrin Lecture 2; Berstel DLT'95).

Note: memory server was unhealthy at write time, so this is recorded on disk;
the source itself is stored at research/sources/hal-05026908-fibonacci-word-complexity-survey.full.md.