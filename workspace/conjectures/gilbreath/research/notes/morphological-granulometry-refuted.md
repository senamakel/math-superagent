# Morphological granulometry refuted for block-length certification

The approach `morphological-gradient-granulometry` proposes to use the monotone,
order-theoretic size distributions of mathematical morphology (granulometries)
as a certificate that the leading `{0,2}` block length `b_k` regenerates.

## What is true (the dictionary)
`|a-b| = max(a,b) - min(a,b)` = the 2-point morphological gradient
(dilation - erosion) over a flat structuring element (Matheron, Serra). The
Gilbreath row map is exactly the iterated morphological gradient. The leading
`{0,2}` block is the flat prefix / 1-Lipschitz prefix (the run's own block
characterization).

## Why the monotonicity transfer fails — two decisive grounds
**(1) The Granville map is not an increasing operator, and increasing+idempotent
is exactly the hypothesis that carries granulometry monotonicity.** Openings and
granulometries are increasing (filter property), anti-extensive, idempotent
filters; the monotone size-distribution / pattern-spectrum theory (Matheron 1975,
Serra 1982; Maragos TPAMI 1989 pattern spectrum; Urbach-Wilkinson "shape-only
granulometries") is built on that increasing property. The Gilbreath cell map
`T(f)(i) = |f(i)-f(i+1)|` is NOT increasing: `|a-4|` is not monotone in `a`
(level-set refutation, `S_4={A>=4}` not a monotone cluster — the candidate's own
flagged kill-risk, which transfers). A granulometry is a level-set (threshold)
construct, and the level predicate is precisely the non-monotone one.

**(2) The quantity to be certified, the block length `b_k`, is not monotone under
the gradient map.** The run's PROVED step law gives `b_{k+1} = b_k - 1` on
erosion — the flat prefix strictly shrinks by one window per erosion row. So a
"monotone functional certifying block length" is directly contradicted by the
step law on the very rows where the gradient is pure `|a-b|`.

## Disposition
`morphological-gradient-granulometry` — **refuted** (killed-by: non-increasing
operator + step law makes `b_k` decrease). The dictionary survives as a
re-description (the run's own block characterization); the monotonicity
certificate is impossible.
