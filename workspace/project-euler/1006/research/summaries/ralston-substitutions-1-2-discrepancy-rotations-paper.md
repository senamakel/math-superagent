# Ralston, "Substitutions and 1/2-Discrepancy of {nθ+x}" (arXiv:1105.5810)

Source: https://ar5iv.labs.arxiv.org/html/1105.5810 (full text) and https://arxiv.org/abs/1105.5810 (abstract page). Full text at `research/sources/ralston-substitutions-1-2-discrepancy-rotations-paper.full.md` (85 KB; the smaller file `ralston-substitutions-1-2-discrepancy-rotations.full.md` is the abstract landing page only).

## What it establishes

For an irrational θ and x ∈ [0,1), the **1/2-discrepancy sums** of the rotation orbit are

  D_n(x) = Σ_{i=0}^{n−1} f(x + iθ mod 1),   f = χ_{[0,1/2)} − χ_{[1/2,1)}.

The central result (Theorem 1.1) realises the sequence of values f(x+iθ) — equivalently the discrepancy sums — through a **sequence of substitutions on a three-symbol alphabet** {A,B,C} with partition A=[0,1/2), B=[1/2,1−θ), C=[1−θ,1), driven by a renormalisation (Gauss-map-like continued-fraction) procedure: the infinite word ω_0 σ_0(ω_1 σ_1(ω_2 σ_2(⋯))) encodes the orbit, up to at most two endpoint changes. The substitution sequence is **eventually periodic iff θ is quadratic irrational** (Corollary); for badly approximable θ and any x, the range of discrepancy values over i=0..n−1 grows like log n — stronger than the Denjoy–Koksma inequality. Any growth rate not trivially forbidden can be realised (Theorem 1.2).

## Why it is in the library for PE1006

This is the continued-fraction **renormalisation engine** the adopted Ostrowski route (`pe1006-ostrowski-sawtooth-closed-form`) names as the engine for fractional-part sums of rotations ("continued-fraction renormalisation of fractional-part sums — J. Number Theory 1985; Ralston arXiv:1105.5810"). The Fibonacci slope θ = 1/φ² is quadratic irrational, so its substitution/renormalisation sequence is eventually periodic — the structural fact that would make an O(log k) (indeed O(1)-coefficient) evaluation of the rotated-sum data possible. It gives the symbolic-dynamics (substitution) realisation of the orbit sums, complementary to the arithmetic (Zeckendorf/continued-fraction) closed forms of Brown–Shiue and Pinner.

## Caveats

- The paper studies the ±1-signed indicator sum (1/2-discrepancy), i.e. counts of orbit points in two halves of the circle, not the decimal-weighted second moment Ψ(k). The bridge from discrepancy counts to floor-difference digits of mechanical words is standard (the digits are the interval-code of the same rotation), but the 10^j-weighting and squaring remain the run's own work.
- Theorem statements in the auto-digest are empty placeholders; the full text file has the real statements and proofs (verified: the file contains the full paper body with Lemma/Proposition/Theorem labels and proofs).
- For PE1006 the relevant orbit is {−m·a mod 1}, m=0..k, a = F(n−2)/F(n) → 1/φ², with the intercept set being the k+1 arc midpoints; matching Ralston's encoding to that specific set is the run's bridge to build.
