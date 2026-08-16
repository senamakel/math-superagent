# Summary — Tao, an uncertainty principle for cyclic groups of prime order (HTML mirror)

Source: Terence Tao, "An uncertainty principle for cyclic groups of prime
order", *Math. Res. Lett.* 12 (2005) 121–127; arXiv:math/0308286v6.
URL: https://arxiv.org/html/math/0308286v6. Full text:
[[research/sources/tao_uncertainty_cyclic_prime_html.full.md]].

**This is the HTML mirror of the same paper digested at
`research/summaries/tao_uncertainty_cyclic_prime.md` (the PDF digest, which
carries the claim block `tao-additive-uncertainty-prime-cyclic`). Read that
first; this note records the proof detail the PDF digest skipped and confirms
the two mirrors agree.**

## What this mirror adds beyond the PDF digest

The HTML text preserves **all proofs**:

- **Lemma 1.2** (cyclotomic-integer lemma): if a polynomial P with integer
  coefficients vanishes at n p-th roots of unity `ω_1,…,ω_n`, then P(1,…,1) is
  a multiple of p. Proof by reduction to a single variable mod `z^p − 1` and
  the minimal polynomial `1 + z + … + z^{p−1}` of ω.
- **Lemma 1.3 (Chebotarëv's theorem)**: every minor of the prime-order Fourier
  matrix is non-zero. The proof factors the determinant
  `D(z_1,…,z_n) = P·∏(z_j − z_{j'})`, shows `P(1,…,1) ≡ det(ξ_k^{j−1})
  = ±∏(ξ_k − ξ_{k'}) ≢ 0 mod p` (Vandermonde), and applies Lemma 1.2.
  History note: Chebotarëv 1926 first; later proofs by Rešetnyak, Dieudonné,
  Newman, Evans–Stark, Frenkel, Goldstein–Guralnick–Isaacs.
- **Corollary 1.4** (the engine of the theorem): for `|A| = |Ã|`, the
  restricted Fourier map `T: ℓ²(A) → ℓ²(Ã)` is invertible — a restatement of
  the minors being non-zero.
- **Theorem 1.1** proven from Cor 1.4 (both directions: the support-sum bound
  and the converse realization of any A, B with `|A|+|B| ≥ p+1`).
- Then **Cauchy–Davenport** (`|A+B| ≥ min(|A|+|B|−1, p)`) as a convolution
  corollary of Theorem 1.1.

The (Z/p)^n iteration attributed to Meshulam is quoted at the end (lines
141–146): `p^j|supp f| + p^{n−j−1}|supp f̂| ≥ p^n + p^{n−1}`, with the convex
hull reading over the points `(p^j, p^{n−j})` — the subgroup indicators. With
p=2 this is the Boolean-cube additive bound in the exact coordinate system of
the fold Φ.

## Correlation with the library

- Confirms `tao-additive-uncertainty-prime-cyclic` exactly; no discrepancy
  between the HTML and PDF mirrors was found.
- The `holds-here` and bearing of the claim stand: directional Walsh-side
  trade-off on (Z/2)^n; equality cases = subgroup indicators = the structured
  low-weight inputs the closed doors forbid; it is not a lower bound on
  `wt(Φ_n h)` by itself.

## Why this file exists / what it settles

The earlier stub digest ("digest only — read this first … Replace this digest")
was an unfinished template. This note replaces it. No new theorem; the added
value is the Chebotarëv/minor-nonzero proof (Lemma 1.3), which is the cleanest
statement in the library of why the Fourier basis is "totally skew" on Z/pZ —
the structural fact any Walsh-side argument on the fold would rest on.