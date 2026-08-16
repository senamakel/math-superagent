# Summary — Guruswami, Rudra, Sudan, "Essential Coding Theory" (textbook, relevant chapters)

Source: V. Guruswami, A. Rudra, M. Sudan, *Essential Coding Theory* (2018). Source URL: https://users.math.msu.edu/users/iwenmark/Teaching/MTH810/web-coding-book.pdf. Full text: [[research/sources/essential_coding_theory_guruswami_rudra_sudan_fulltext.full]] (808KB, 21015 lines — read by section, not whole).

## What this is

A standard full textbook of error-correcting codes (linear codes, Reed–Solomon, BCH, list decoding, polar codes, expander codes, LP bounds, Fourier-analytic coding). Its value for SUPPLY is concentrated in the chapters on **linear codes over `F_q`**, **weight distributions and the MacWilliams identity**, and the **LP / Krawtchouk bounds** — the same Walsh/Krawtchouk machinery as the Guruswami notes, digest, and MacWilliams 1963, at textbook depth with references. It is the deepest single local source for the transform-basis behind request `walsh-spectral-subset-b904`.

## What it establishes that bears on SUPPLY

The textbook presents, at full depth, the objects a Walsh/subset-sum bound on `wt(Φ_n h)` would be built from: linear maps on `F_q^n`, weight distributions, the MacWilliams identity and its Krawtchouk diagonalisation, and the Delsarte LP bound (the *dual positivity* mechanism — `Σ_i A_i K_j(i) ≥ 0` — that is the closest template shape for a submask-positive constraint on `Φ`). It also covers **Fourier analysis on the Boolean hypercube** (dual character sums `Σ_{c∈C}(−1)^{α·c} = |C|·1_{α∈C^⊥}`), which is exactly the coordinate system of the fold.

## Why it does not close the request

It is a textbook: it states the transform identities and size bounds (on `A(n,d)`), not a per-vector lower bound `wt(Φ_n h) ≥ c·n` for a fixed input like the prime string. The machinery it documents is the *toolbox*, and the specific input-dependent bound for the fold remains open.

## Evidence class / falsifier

Sourced (standard textbook). Would be misused as a source of an explicit fold-weight bound; it supplies the transform/LP machinery, not that bound.

```claim
id: essential-coding-theory-machinery
statement: The weight-distribution/MacWilliams/Krawtchouk/Delsarte-LP machinery on F_q^n is developed at textbook depth: weight enumerators transform by the Krawtchouk substitution, dual-positivity gives the linear constraints behind the LP (MRRW) bound, and Fourier analysis on the Boolean hypercube with dual-character sums is the underlying coordinate system.
hypotheses: linear (and general) codes over F_q; the standard Hamming metric; the transform identities.
holds-here: Yes as machinery — the F_2^n / Walsh-basis setting of the submask-XOR fold Φ is an instance.
status: sourced (textbook)
bearing: Deepest local reference for the Walsh/Krawtchouk/LP toolbox behind request walsh-spectral-subset-b904. Supplies the machinery, not a per-input bound on wt(Φ_n h); the input-dependent lower bound remains open.
anchor: research/sources/essential_coding_theory_guruswami_rudra_sudan_fulltext.full.md (see chapter headings via outline)
```
