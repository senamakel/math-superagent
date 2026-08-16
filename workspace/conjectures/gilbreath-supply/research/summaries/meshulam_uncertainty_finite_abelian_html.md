# Summary — Meshulam, an uncertainty inequality for finite abelian groups (HTML mirror)

Source: Roy Meshulam, "An Uncertainty Inequality for Finite Abelian Groups",
arXiv:math.CO/0312407 (2003) / *European J. Combin.* 27 (2006) 37–63.
URL: https://arxiv.org/html/math/0312407v1. Full text:
[[research/sources/meshulam_uncertainty_finite_abelian_html.full.md]].

**This is the HTML mirror of the same paper digested at
`research/summaries/meshulam_uncertainty_finite_abelian.md` (the PDF digest,
which carries the claim block). Read that first; this note records the extra
detail the PDF digest skipped and confirms the two mirrors agree.**

## What this mirror adds beyond the PDF digest

The HTML full text preserves the **complete proofs** (the PDF digest quoted only
the statements):

- **Prop 1.3** (subgroup/factor reduction `θ(G,k) ≥ θ(H,s)·θ(G/H,t)`): the
  proof via Claim 2.1 — for `F_η(ȳ) = f̂_y(η)η̃(−y)` restricted to a coset
  decomposition of H, `supp f̂ = Σ_η |supp F̂_η| ≥ θ(H,s)·θ(G/H,t)` with
  `st ≤ k` by averaging over cosets.
- **Prop 1.4** (submultiplicativity `u(d,s)·u(n/d,t) ≥ u(n,st)`): a three-case
  convexity argument in `s` on the interval `m_1 = max{a_1, k/b_2} ≤ s ≤
  min{a_2, k/b_1} = m_2`.
- **Theorem 4.1** (the non-abelian extension, attributed to Meshulam 1992):
  for finite G with irreps `ρ_i` of dimension `d_i` and
  `μ(f) = Σ_i d_i·rank f̂(ρ_i)`, `|supp f|·μ(f) ≥ |G|`.

**Theorem 1.2 is identical to the PDF digest:** for `0 ≠ f ∈ L(G)`, `|G| = n`,
`k = |supp f|`, `d_1` largest divisor of n ≤ k, `d_2` smallest ≥ k:
`|supp f̂| ≥ (n/(d_1 d_2))(d_1 + d_2 − k)`. The convex-hull remark (the lattice
point `(|supp f|, |supp f̂|)` lies above the convex hull of `{(|H|,|G/H|)}` over
subgroups H) is verbatim, lines 61–63.

The (Z/2)^n specialization recorded in the PDF digest is correct: divisors of
`2^n` are `2^j`, so the bound becomes
`|supp f̂| ≥ 2^{n−j−1}(3·2^j − k)` for `2^j ≤ k ≤ 2^{j+1}` (divide by
`2^j·2^{j+1}`), equality cases subgroup/affine-subspace indicators.

## Correlation with the library

- Confirms `meshulam-finite-abelian-divisor-bound` (the claim already on disk)
  exactly; no discrepancy between the HTML and PDF mirrors was found.
- The claim's `holds-here` and bearing stand as written: the Walsh-basis bound
  is directional, not a lower bound on `wt(Φ_n h)`; the extremals are the
  structured low-weight inputs the five closed doors forbid.

## Why this file exists / what it settles

The earlier stub digest ("digest only — read this first … Replace this digest")
was an unfinished template. This note replaces it. No new theorem, no change to
any claim: same content as the PDF digest, plus the proofs of Prop 1.3/1.4 and
Thm 4.1 for whoever needs the induction mechanism (which is the engine one
would adapt if attempting a Walsh-side bound on `Φ`'s image weight).