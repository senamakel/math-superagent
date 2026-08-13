# Index — code/directive25

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `gap_trend_reconciliation.py` | Directive 25 compute: Part A (inter-giant gap trend, exact Fractions) — gaps among the genuine giants are 22,8,4,26,2,14,2,14,4,4,12: flat/mixed, Spearman rho(gap, prior b) = −0.141, R² ≈ 0.04–0.11; Part B (reconciliation, float fit) — observed rho = b_{i+1}/b_i at the 11 genuine pairs, sublinear expected rho_sub = 1 + C·b^(α−1) with α=0.388 (43-event OLS) and C pooled = 802.6, vs geometric factor 1.6816: sublinear MSE 0.140 vs geometric 0.154 — no decisive law on 12 points, but the order-of-magnitude reconciliation (ratio 3.9 at b=5939 → 1.49 at b=733575) tracks the sublinear decline, not the constant factor. Inputs: blocks_depth1000.json only. Independent re-derivation reproduces gaps/ratios to 4 decimals (see code/out/directive25_gap_trend.captured.txt). |
