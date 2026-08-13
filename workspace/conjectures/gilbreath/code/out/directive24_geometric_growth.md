# Geometric growth of the giant-jump landing blocks — GEOMETRIC wins

`code/directive24/compute_width_degradation_and_growth.py` (captured `code/out/directive24_compute.captured.txt`),
verified independently via numpy `code/out/directive24_verify.captured.txt`
(slopes/R²/doubling reproduce to 6 decimals).

## Setup

- Giant events = rows i (1-based) with b_i → b_{i+1} and jump
  j = b_{i+1} − b_i > 1000, read from the b array via the step law
  (b[i] > b[i−1] in 0-based terms). The b array yields **43 strict-increase
  b-steps** in rows 1..1000 (the 60 regeneration events minus 17 jump-0
  events, which leave b unchanged); exactly 13 have jump > 1000, and they
  are precisely `{34,56,64,68,94,96,110,112,126,130,134,146,161}`.
- Post-jump block = b_{i+1} = JSON `b[i]` (row convention cross-checked:
  b[34] = 2179 after 865 at row 34, b[161] = 1,270,444 = cap).
- **Genuine 12** = the giants except i=161 (width artifact: landing row 162
  fills the whole finite row, true jump ≥ 176,181). Fit x = event index
  0..11 (resp. 0..12), y = post-jump block.
- Fits: least squares on (x, log y) = geometric/exponential; (x, y) =
  linear. Slopes/intercepts/R² computed as exact `Fraction`s; log taken only
  of the exact integer b (1-ulp doubles). Verification via `numpy.polyfit`.

## Result (genuine 12)

| fit | slope | intercept | R² | residuals |
| --- | --- | --- | --- | --- |
| GEOMETRIC log b = a + m·x | m = **+0.519764** | 8.591921 | **0.943852** | −0.905, −0.422, +0.423, +0.207, +0.765, +0.361, +0.151, +0.282, −0.058, −0.116, −0.284, −0.404 |
| LINEAR b = a + m·x | m = +84100.82 | −184084 | 0.783043 | +186263, +105925, +39147, −36720, −59699, −132447, −178815, −132993, −163633, −56917, +76640, +353248 |

**GEOMETRIC wins: R² 0.9439 vs 0.7830 (margin 0.161).** The linear residuals
are huge, monotone-sign, and end in +353k — a textbook misshape; the
geometric residuals are small and roughly balanced. **Growth rate =
exp(0.519764) = 1.6816× per event ≈ ×1.68/event; the doubling time in
events is ln2 / 0.519764 ≈ 1.33 events** (a block is ~1.7× bigger after
each giant; two giants multiply it ~2.8×).

Per-step ratios (consecutive post-jump blocks): 2179 → 5942 (2.727) →
23265 (3.915) → 31499 (1.354) → 92620 (2.940) → 103973 (1.123) → 141706
(1.363) → 271629 (1.917) → 325090 (1.197) → 515906 (1.587) → 733564 (1.422)
→ 1094273 (1.492). Geometric-mean ratio = (1094273/2179)^(1/11) = 1.751;
the LLS fit (which weights log-space evenly) gives 1.682.

## Robustness: all 13 (including capped i=161)

| fit | slope | intercept | R² |
| --- | --- | --- | --- |
| GEOMETRIC | +0.494241 | 8.685508 | 0.942088 |
| LINEAR | +98781.64 | −237914 | 0.807242 |

Geometric again wins (margin 0.135); the capped point 1,270,444 adds a
1.161 ratio but barely moves R². The verdict is not an artifact of dropping
i=161 — and note the i=161 point is a *lower bound* (true jump ≥ 176,181),
so the true all-13 fit is at least as geometric as reported. Geometric
robustness: the first four ratios (2.7, 3.9, 1.35, 2.94) alone already
reject a constant additive increment (they differ by up to 3×).

## Caveats

- 12 points is a small sample; the geometric fit is a **description of the
  computed record, not a proof of a growth law**. What survives the caveats:
  (i) on the data that exists, growth of the landing block is far better
  described by ×1.68/event than by +84,000/event; (ii) all 12 genuine
  events have flooring ≥ 536,885 > 1000, so none of these numbers is
  width-truncated (see `directive24_width_degradation.md`).
- "Doubling factor" here is per giant event (≈1.68×/event, doubling every
  ~1.33 events), NOT per row. It is also not a proof of unbounded growth:
  the observed self-similarity (giant jump ≈ current block, jumps grow
  sublinearly with b, log-log slope 0.388, per CONTEXT) is consistent with
  b_{next} ≈ C·b_{i}·(block-history), which compounds geometrically *if* the
  ratio C·(·) stays above 1 — exactly the "giants keep arriving" condition
  Directive 24 reduces the conjecture to.