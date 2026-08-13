# Inter-giant gap trend, and the geometric-vs-sublinear reconciliation — depth 1000, exact

Executed this run: `code/directive25/gap_trend_reconciliation.py`, captured as
`code/out/directive25_gap_trend.captured.txt`. Inputs: only
`code/out/blocks_depth1000.json` (block lengths b[k-1] of rows k=1..1000,
sieve 2e7, W=1,270,607 primes). Row conventions cross-checked against the
characterization table (13/13 landing floors, anchors b_1=2, b_2=7, b_3=13,
cap row 161 = 1,270,444). Independent re-derivation reproduces the gaps and
all 11 ratios to 4 decimals (the captured file's final check).

## Part A — the inter-giant gap (Directive 25 item 3)

The 13 giants (j > 1000) sit at rows
`34, 56, 64, 68, 94, 96, 110, 112, 126, 130, 134, 146, 161`; the capped
i=161 (finite-width artifact) is excluded from every gap list.

- **genuine 12 inter-giant gaps (rows): 22, 8, 4, 26, 2, 14, 2, 14, 4, 4, 12**
  — mean 10.18, median 8, max 26.
- **no trend**: OLS gap ~ giant# slope −0.818 (R²=0.109), gap ~ prior-b
  slope ≈ 0 (R²=0.041), Spearman rho(gap, prior-b) = −0.141 (exact, no ties).
  The gaps are flat/mixed over b ranging 2,179 → 1,094,273, with the largest
  gap (26) at the *second* giant and a mild late clustering of 2–4-row gaps
  (i=110,112 and 126,130,134).
- **what this settles (numerical, depth 1000 only):** the gap between
  consecutive large jumps shows **no sign of growing with b or with event
  index** — it is compatible with "giants keep arriving at bounded spacing
  while j ~ b^0.388 → ∞", which is the mechanism that would make the
  recharge inequality trivial (per Directive 24, geometric growth reframing:
  giants need only arrive infinitely often). 12 data points; a width large
  enough for more giants is the only thing that would separate "bounded gap"
  from "slowly growing gap" — this run cannot.

## Part B — reconcile geometric growth with the sublinear exponent (Directive 25 item 4)

- observed ratio rho = b_{i+1}/b_i across the 11 consecutive genuine pairs:
  `2.73, 3.92, 1.35, 2.94, 1.12, 1.36, 1.92, 1.20, 1.59, 1.42, 1.49`
  (mean 1.91, matching directive24's per-step ratios exactly).
- sublinear law j = C·b^0.388 (alpha = 0.388, the 43-event OLS from
  surplus_renewal_structure) implies rho_sub = 1 + C·b^(alpha−1) → 1.
  Per-giant C_i = j_i/b_i^0.388 varies hugely (68 → 1911); pooled C = 802.6.
- **model comparison (MSE of log-residuals over the 11 pairs):**
  sublinear **0.140** vs geometric (const 1.6816) **0.154**. Neither wins
  decisively on 12 points; both leave large residuals (geometric misses the
  early 2.7/3.9 by +0.5..+0.8 in log terms; sublinear overshoots them).
- **the reconciliation that does hold:** the observed ratios *decline* toward
  1 with b (3.9 at b=5939 → 1.49 at b=733575), in the direction the
  sublinear law predicts and opposite to what a constant geometric factor
  would predict. The directive24 "×1.68/event" geometric description is a
  good *local* summary of 12 points and is **not** the asymptotic law; the
  two run findings are consistent in the limit once the ratio is seen to
  decay. This is numerical reconciliation, not a proof — the question is
  exactly the one Directive 25 names: whether the gap stays bounded while
  j → ∞.

## Bounds and status

- Exact integers for all gap/ratio/rank computations; floats only for the
  power-law fit (jarringly wrong `Fraction ** Fraction` in the first version
  fixed to float power — noted in git-less changelog above).
- The capped i=161 is excluded from every claim; jumps at row 162+ are lower
  bounds only (Directive 24, k* = 162).
- **Status: checked at depth 1000, numerical evidence only.** Both items
  are statements about 11–12 points in one finite triangle, not theorems.