# Weighted Digital Sums — Cheung, Flajolet, Golin & Lee (2010)

Source: https://arxiv.org/abs/1003.0150
Y. K. Cheung, P. Flajolet, M. Golin, C. Y. J. Lee, *Multidimensional
Divide-and-Conquer and Weighted Digital Sums*, arXiv:1003.0150 [cs.DS] (2010).
Full text at `research/L0/flajolet_weighted_digitalsums.full.md`.

## What it establishes
Three exact structured evaluations via Mellin-transform analysis:
1. **MDC recurrences** — solutions have the form
   `λ_d·n·lg^{d-1}n + Σ_{m=0}^{d-2} (n·lg^m n)·A_{d,m}(lg n) + c_d`, periodic
   `A_{d,m}` given by absolutely-convergent Fourier series.
2. **Weighted digital sums of the first type** `S_M(n)=Σ_t t^M·b_t·2^t` and
   their average `TS_M(n)=(1/n)Σ_{j<n}S_M(j)` — same closed form with `d=M+1`.
3. **Variant** `W_M(n)=Σ_t t^M·2^{i_t}` (positions of 1-bits) and
   `TW_M(n)` — solution `n·G_M(lg n) + d_M·lg^M n + Σ_{d=0}^{M-1} lg^d n·G_{M,d}(lg n)`,
   again with periodic-1 Fourier components.

Core message: **weighted** binary digital sums (terms `t^M·(bit term)`) admit
exact expressions of a main-term-plus-1-periodic-fluctuation type, not
term-by-term iteration — i.e. they are computable in **O(16^M /fit) polylog**
time. The fluctuation functions `A_{d,m}`, `G_M`, `G_{M,d}` are all continuous
period-1 functions given by absolutely convergent Fourier series (Takagi-family
analogues of the Trollope–Delange fluctuation).

## Why it applies here
The run's arithmetic engine needs, at n=10^5,
- A(n) = Σ_{k=1..n} k·popcount(k) — total 1-bits over "k copies of k",
- B(n) = Σ_{k=1..n} k·zerocount(k) — total 0-bits.

Both are **first-moment, k·-weighted sums of binary digit-count functions**.
This paper is the primary, openly-accessible (arXiv full text) treatment that
*weighted digit sums — not just the unweighted Trollope–Delange case of
[[trollopedelange]] — have exactly this polylog closed-form + periodic-
fluctuation structure*. It upgrades the counting-arithmetic warrant from the
abstract-only [[weightedmom]] (Larcher–Pillichshammer, subscription-gated) to a
locally-held full text with explicit solution forms. The specific O(log n)
recurrences the run actually executes come from [[bitcount]] (A000788) and
[[zerocount]] (A059015); this paper is the structural proof that the weighted
objects live in the same closed-form family.

## Caveat
- The paper's weight is **positional** (`t^M` times a bit at position t), while
  the board's weight is the **index k** (k copies of k). Both are "first moment
  of a digit-sum function" and share the Takagi/Delange structure, but the
  paper's exact formulas are not directly the run's sums. The run's A(n), B(n)
  still come from the bit-position decomposition built on A000788/A059015.
- It establishes the *form/structure* of weighted digital sums; the specific
  numerics are the run's own recurrence evaluation.
