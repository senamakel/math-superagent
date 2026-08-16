# Directive 45 — threshold-weight exponent fit, from the operator's theta column

Data (directive 45): exact-mean threshold weight `w(n) = min w : mean_n(w) >= 0.40`,
as **theta*n**, theta = 7,11,16,24,35,52,77,112,164,239 / n for
n = 64..32768 (powers of 2, 2^6..2^15).

```
n          64   128   256   512   1024  2048  4096  8192  16384  32768
w           7    11    16    24    35    52    77   112    164    239
log2(n)     6     7     8     9     10    11    12    13     14     15
log2(w)  2.807 3.459 4.000 4.585 5.129 5.700 6.267 6.807  7.358  7.901
```

## Per-doubling slope of log2(w) per log2(n)

```
0.652  0.541  0.585  0.544  0.571  0.567  0.540  0.551  0.543
```
(aggregate of the last three = 0.545; the top-of-range slope is still ~0.543,
so the local slope is hovering in 0.54..0.57 and is NOT collapsing toward 1/2
within the measured range — each of the top doublings still adds ~3% to w/sqrt(n).)

## 1) Pure power  w ~ C·n^a   (log-log OLS)

- over n >= 256 (the pass-3 authoritative tail): a = 0.5569
  (= 23.389/42, Sxy/Sxx over x = log2 n = 8..15) — matches the pass-3
  0.55678 ± 0.00225.
- over n >= 1024: a = 0.5536 (= 9.688/17.5) — still in the 0.55 band.
- over the whole table (n >= 64): a = 0.5624 (= 46.394/82.5).

  The band 0.553..0.562 brackets whatever tail you choose; the residual
  scatter is ~0.7% of log2(w) — an excellent pure-power fit, far better than
  any closed-form candidate below.

Separation from 1/2: |a − 1/2| ≈ 0.05 everywhere, ≈ 20 × the OLS standard
error (~0.0023). As a **pure power** the data strongly prefers ~0.55, not 1/2.

## 2) Hypothesis w = c·sqrt(n): tabulate w/sqrt(n)

```
n       64    128   256   512   1024  2048  4096  8192  16384  32768
w/sqrt 0.875 0.972 1.000 1.061 1.094 1.149 1.203 1.237 1.281  1.320
```
**NOT flat.** Rises 0.875 → 1.320, +51% across the range, +15% over the tail
(n>=1024), and the per-doubling ratio at the top is still ~1.03 (each top
doubling adds ~3%). A column that keeps rising through the top of the range is
not flattening toward a constant: pure exponent 1/2 is **rejected** by the
measured data, not just not-separated.

## 3) Hypothesis w = c·sqrt(n)·ln(n): tabulate w/(sqrt(n)·ln n)

```
n       64    128   256   512   1024  2048  4096  8192  16384  32768
col    0.210 0.200 0.180 0.170 0.158 0.151 0.145 0.137 0.132  0.127
```
**NOT flat either** — monotonically decreasing, −20% over the tail. sqrt·ln n
with β ≈ 1 is rejected.

## 4) Hypothesis w = C·n^(log_4 3)  (exponent 0.7925)

|0.5534 − 0.7925| = 0.239, far outside any error bar. **Rejected** — the data
is nowhere near the 0.79 exponent.

## What the data prefers, and by how much

- **Best single model: pure power `w*(n) ~ n^0.55`** (0.5568 over the full
  table, 0.5534 over n>=1024), residual scatter ~0.7%. That is the fitted
  value, **not a closed form** — it is not 1/2, not log_4(3), not a clean
  constant the data can name.
- It is **not 1/2**: the w/sqrt(n) column rises by 51% across the range and is
  still rising ~3% per doubling at the top, so 1/2 is rejected as the exponent
  by a wide margin (≈0.053, >17σ), and the local slope does not fall to 1/2
  inside the measured range.
- **Caveat the directive asked for:** a *pure* 1/2 is rejected, but an
  *asymptotic* 1/2 with a slowly-varying (ln n)^β factor is NOT excluded by
  n ≤ 32768 — the w/sqrt column rising as it does is exactly the signature of
  a power slightly above 1/2 that an undetermined β could bend back to 1/2 at
  far larger n. The measured range cannot separate "pure n^0.55" from
  "C·sqrt(n)·(ln n)^β with β ≈ 0.5–0.6". No clean derivation behind 1/2 is
  supported by this column; the honest statement is an exponent in the
  0.54–0.58 band, best-fit 0.553, drifting slowly down.

## Bottom line (directive's test, answered)

The w/sqrt(n) column is **not flat** — it is rising and still rising at the top
of the range — so the answer is **NO, not the clean 1/2**, by a wide margin as
a pure power. The data prefers `~n^0.55`. This still delivers the directive's
headline weakening: linear supply becomes typical once the switch count exceeds
about `n^0.55`, which is **sublinear** — dramatically weaker than a positive
fraction of switches. But "about sqrt(n)" is not what this column shows.

Fitted, not proved. Exact per-n w and theta are exact; the exponent is an OLS
fit over n ≤ 32768. Everything above is computed from the directive's own
numbers by hand; the arithmetic (log2 w, slopes, OLS, flatness columns) is in
`code/out/theta45_fit.py`.
