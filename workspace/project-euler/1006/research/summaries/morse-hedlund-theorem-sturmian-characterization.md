# Wojcik, "Formal Intercept of Sturmian Words" (2018) — Morse–Hedlund background

<!-- source: https://hal.science/hal-01827511/document | arXiv 1803.02073 -->

Research note on the formal intercept (Ostrowski-expansion sequence) of Sturmian words.
Sections 1–2 recall with proofs the basics of Sturmian words, which is the banner source
here for the Morse–Hedlund theorem that the problem's stated FACT rests on.

## What it establishes (relevant to PE1006)
- **Theorem 1 (Morse–Hedlund)**: an infinite word x over A is ultimately periodic iff there
  exists n>=1 with p(x,n) <= n. Equivalently **an aperiodic word has p(x,n) >= n+1 for all n**.
- **Theorem 2(1)**: a **balanced** word satisfies p(x,n) <= n+1 for all n.
- **Theorem 3(1)**: a balanced word is Sturmian iff its slope is irrational.
- Balanced = every two equal-length factors differ in # of 1s (b's) by at most 1.

## Why this produces the k+1 FACT
The infinite Fibonacci word F is aperiodic (slope 1/φ² irrational) and balanced (Sturmian =>
balanced). Morse–Hedlund gives p >= k+1; balance gives p <= k+1; hence p = k+1 exactly for
every k. This is precisely the problem's stated "only k+1 different Fibonacci subwords of
length k".

## Hypotheses check for this problem
`holds-here: yes` — F is aperiodic and balanced, both the required hypotheses hold.

## Full text
[[morse-hedlund-theorem-sturmian-characterization.full]]

```claim
id: MH-kplus1-factors
statement: An aperiodic word has p(n) >= n+1 for all n; a balanced word has p(n) <= n+1; hence a balanced aperiodic word (a Sturmian word) has exactly n+1 distinct factors of length n.
hypotheses: word aperiodic and balanced (factor complexity p, all n>=1).
holds-here: yes — infinite Fibonacci word is aperiodic (irrational slope 1/phi^2) and balanced.
status: proved (in source, Morse–Hedlund)
bearing: gives the problem's exactly-k+1-factors FACT directly.
anchor: research/summaries/morse-hedlund-theorem-sturmian-characterization.md
```
