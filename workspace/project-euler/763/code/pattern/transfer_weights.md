# PE763 transfer-DP: exact per-level weight and boundary structure

## Data provenance (read-only, no BFS run)

- `data/level_N.txt`, N=2..12: one line per **config** `hist|M|dims`; the
  per-histogram multiplicity is the number of config lines sharing `hist`.
- `code/out/per_hist_mult_13_14.txt`, N=13,14: distinct histogram → multiplicity
  (headers re-assert D(13)=1749267, D(14)=5949063).
- 694 distinct (histogram, multiplicity) rows total.
- Histogram convention **as stored**: `a_0..a_M`, `a_k` = # occupied cubes
  with `x+y+z = k`, `M` = max level. `a_0 = 0` in every row (the origin cell
  is always gone after ≥ 1 division); `a_M = 3` in every row.

## Result A — the multiplicity factors per level with constant weights

For every one of the 694 recorded histograms, **exactly** (exact `Fraction`
arithmetic, 0 mismatches):

```
mult(h) = C · ∏_{k=0}^{M} w(a_k),        C = 1/3
```

| level count k | w(k)   | occurrences | note |
| --- | --- | --- | --- |
| 0 | 1 | 694 | 1 per histogram |
| 1 | 3 | 1275 | each 1-cell level ×3 |
| 2 | 3 | 2583 | each 2-cell level ×3 |
| 3 | 3 | 780 | each 3-cell level ×3 (incl. top `a_M=3`) |
| 4 | 4 | 558 | each 4-cell level ×4 (= 2²) |
| 5 | 1 | 1275 | ×1 |
| **6** | **10/3** | 8 | **the only non-integer weight** |
| 7 | 1 | 86 | ×1 |

Equivalent branch form (identical, integer in each branch):

```
no 6-level   : mult = 2^(2·n4) · 3^(n1+n2+n3−1)
has 6-level  : mult = 10 · 2^(2·n4) · 3^(n1+n2+n3−2)
```

where `n_k` = # levels with exactly k cells (incl. top). Identity between the
forms: `w(1)=w(2)=w(3)=3` ⇒ 3^(n1+n2+n3); `w(4)=4=2²`; `w(6)=10/3`; then
`C·3^(n1+n2+n3)·4^n4·(10/3)^n6` collapses onto the branch form (with a 6:
`(1/3)·(10/3) = 10/9`, i.e. `10·3^(...−2)`). Counts 5 and 7 (and, per the
closed form, any ≥ 8) contribute weight 1.

## Does mult really factor per level? — YES, no extra state needed

- `w(k)` is a **constant** for every level-count that occurs; the `10/3` is
  genuinely per-level, so a transfer DP needs **no** "have seen a 6" boolean
  for the weight — the current level count already encodes it.
- The only level-count with a non-integer weight is **k = 6**.
- **Honest limit:** the data only contains level counts 0..7 (largest observed
  level has 7 cells; N ≤ 14). `w(k) = 1` for k ≥ 8 is what the closed form
  predicts (the branch form has no nₖ terms for k ≥ 8) but is **unverified**:
  a level with ≥ 8 cells at some N ≥ 15 would be the first falsifier of the
  constant-weight table (not reachable in this container).

## Boundary rules (verified 694/694)

- `a_0 = 0` always (stored origin level).
- **First nonzero level** `a_1 ∈ {1, 2}` — distribution {1: 276, 2: 418};
  `a_1 = 3` never occurs (level 1 is never the full triangle in this range).
- **Top / max level** `a_M = 3` always (top level is exactly the forward
  triangle of one parent cell).
- **Total** `Σ_k a_k = 2N+1` always (each division adds net +2 cells).
- `M` ranges 2..14 in the data (M distribution: N=2→1 hist with M=2, etc.).

## Transition structure (for the level-by-level DP)

Observed adjacent transitions `a_k → a_{k+1}` (counts over all 694 rows):

```
0→1(276) 0→2(418)                    (start)
1→3(66) 1→4(386) 1→5(823)
2→1(704) 2→2(1461) 2→3(418)
3→6(8) 3→7(78)
4→3(19) 4→4(153) 4→5(386)
5→1(295) 5→2(704) 5→3(276)
6→7(8)                                (6 always followed by 7)
7→3(1) 7→4(19) 7→5(66)                (toward the top)
```

- Max observed jump `|a_{k+1} − a_k| = 4` (the pair 7→3).
- All 8 six-level occurrences have context **(prev=3, next=7)** — substring
  "3 6 7"; at most one 6-level per histogram.
- **Caveat:** this is the OBSERVED transition set for N ≤ 14 — a necessary
  admissibility condition, not a proven-complete rule for all N. E.g. 1→2,
  5→4 never occur here but are not ruled out at larger N; the completeness of
  the table (and whether 6 can appear outside "3 6 7") is not decidable from
  this data.

## Consequence for the transfer DP

The weight of a histogram is a **local product** over its level counts: each
level contributes `w(a_k)`, global factor `1/3` fixed, boundary rules as
above, transitions constrained by the empirical table. The weight part of the
transfer is nailed exactly for every occurring level-count; the remaining open
piece is the transition rule's completeness at N > 14 (larger level counts,
and the "6" context question).

## Verification files created this pass (all read-only)

- `code/pattern/transfer_weights_exact.py` — exact-Fraction check: product
  form C·∏w(aₖ) and branch form, 0/694 mismatches; boundary/transition/6-ctx
  tables.
- `code/pattern/transfer_weights_final.py` — integer-weight probe: with
  w(6)=10 exactly the 8 six-containing rows fail, proving w(6)=10/3 is needed.
- `code/pattern/transfer_weights_check.py`, `transfer_structure.py`,
  `transfer_weights_table.py` — earlier read-only passes (same conclusion).