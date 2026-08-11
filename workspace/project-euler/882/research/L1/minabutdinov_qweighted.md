# Generalized Trollope–Delange for weighted digit sums — Minabutdinov (2018)

Source: https://arxiv.org/abs/1801.03120
A. R. Minabutdinov, *Limiting curves for the dyadic odometer and the
generalized Trollope–Delange formula*, arXiv:1801.03120 [math.DS] (2018, v3).
Full text at `research/L0/minabutdinov_qweighted.full.md`.

## What it establishes
Extends the classical **Trollope–Delange formula** (unweighted, [[trollopedelange]])
to the **weighted sum-of-binary-digits** function `s_q`, where the i-th bit of k
carries weight `q^{i+1}` (for integer weights this is exactly a positional-
weighted digit sum). For `1/2 < |q| < 1` the deviated partial sums converge to a
**Takagi–Landsberg** limiting curve `Ta` with `a = 1/(2q)`; the ordinary
Trollope–Delange fluctuation is the `q=1/2` case. The generalized formula has
the same main-term + 1-periodic Takagi-type fluctuation shape as the classical
one.

## Why it applies here
The arithmetic leg needs A(n)=Σ k·popcount(k) and B(n)=Σ k·zerocount(k) in
polylog time at n=10^5. Together with the companion 2024 note (a q-weighted
Trollope–Delange formula, ETH Research Collection) and [[flajolet_weighted_digitalsums]],
this establishes — from a primary, openly-available source — that **weighted**
binary digit sums (our k·-weighted A,B) retain the closed-form main-term plus
1-periodic-fluctuation (Takagi/Takagi–Landsberg family) structure, i.e. are in
the same polylog-computable class as the unweighted Trollope–Delange sums. It
corroborates [[weightedmom]] (abstract-only) and the fold
`L2/counting-arithmetic.md` with a locally-held proof, not just an abstract.

## Caveat
- The weight is positional (`q^{i+1}` per bit position), not the board's index
  weight; the run's exact A(n), B(n) come from the A000788/A059015-based
  bit-position decomposition ([[bitcount]], [[zerocount]]). This paper
  establishes the *structure* (polylog + Takagi-family fluctuation), not the
  run's specific sums.
- Primary anchor here is the unweighted [[trollopedelange]] (Girgensohn) for
  the actual recurrences; this and the Flajolet paper are the weighted
  generalization warrant.
