# Frid — Sturmian words: equivalent definitions (lecture slides, Aix-Marseille, Sept 2020)

<!-- source: https://www.i2m.univ-amu.fr/wiki/Combinatorics-on-Words-seminar/_media/lectures:lecture8slidessturmian.pdf | read 2026-08-19 -->

Full text: `research/sources/frid-sturmian-equivalent-definitions.full.md`

## What it establishes

A lecture-slide set (26 slides) on the equivalent definitions of Sturmian words, **in exactly PE1006's 0/1 convention** (morphism φ(0)=01, φ(1)=0, fixed point 0100101001001… = the problem's S_∞).

**Morse–Hedlund 1938.** An infinite word is either ultimately periodic (complexity ultimately constant) or satisfies p_u(n) ≥ n+1; a word with p_u(n) = n+1 is called Sturmian.

**Balanced.** w over {0,1} is balanced iff every two length-n factors x,y satisfy ||x|₁ − |y|₁| ≤ 1. Every balanced infinite word has a slope π(w) = lim |w[0..n−1]|₁/n; a balanced word is periodic iff its slope is rational. **The Fibonacci word has slope 1/τ² = (3−√5)/2 ≈ 0.382** (shown as lim F_{n−2}/F_n), matching PE1006's S_∞.

**Three equivalent definitions (theorem).** For a right-infinite binary word x: (i) p_x(n) = n+1 ∀n; (ii) x non-periodic balanced; (iii) x mechanical with irrational slope. Any such word is Sturmian.

**Mechanical/rotation coding.** w[n] = ⌊(n+1)σ+ρ⌋ − ⌊nσ+ρ⌋ (lower) or the ceiling version (upper); equivalently the coding of the rotation by σ with intercept ρ: w[k] = 1 iff −kσ < ρ < −(k+1)σ (mod 1). **The prefix of length k is determined by which of the k+1 intervals of the circle (cut at −kσ) contains ρ — hence p_w(k) = k+1** (slides 17-18). This is the run's arc/interval construction, source-pinned in PE1006's own convention.

**Properties used by the run.**
- A Sturmian word is **never k-automatic** (frequency of 1 = irrational slope; k-automatic words have rational frequencies). Directly corroborates `cobham-bes-frougny-multiplicatively-independent-conversion` (refutation of the Zeckendorf-automatic digit-DP route).
- **The set of factors of a Sturmian word depends only on its slope**, not the intercept — so one may take ρ = σ (characteristic word).
- The characteristic word c_σ is built from the continued fraction of σ: for σ = [0, m₁+1, m₂, m₃, …], c_σ = lim sₙ with s_{−1}=1, s₀=0, sₙ = s_{n−1}^{mₙ}s_{n−2}. **For the Fibonacci word, 1/τ² = [0, 2, 1, 1, 1, …] gives s₁=01, s₂=010, s₃=01001, s₄=01001010 = exactly the problem's S_n.**

## Why it matters for PE1006

- Confirms, in the problem's own 0/1 convention and its own S_n, the entire governing-theory chain: k+1 factors (Morse–Hedlund), the mechanical digit rule, the interval/arc construction of the k+1 factors, the slope 1/φ² = [0;2,1,1,…], and the non-automaticity (which kills the finite-automaton digit-DP route).
- The standard-word construction s_n = s_{n−1}^{m_n}s_{n−2} with directive sequence [0;2,1,1,…] is the exact finite-word ladder the run's contiguous-window/position theorems use.

## What it does NOT establish

- No Ψ(k), no decimal weighting, no floor-sum evaluation. Lecture slides: statements with proof sketches, not a journal-grade derivation.

## Claims anchored here

`governing-sturmian` (slope 1/φ², characteristic), `governing-factor-complexity` (Morse–Hedlund k+1), `mechanical-word-digit-rule` (interval construction, same-slope-same-factors), corroborates `cobham-bes-frougny-multiplicatively-independent-conversion` (Sturmian not k-automatic).
