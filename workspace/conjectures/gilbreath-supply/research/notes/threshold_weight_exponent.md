# Threshold-weight exponent for linear supply — measured and fitted

## What the pass's head question asked

>`Does the minimum weight ratio at which linear supply becomes typical tend to 0`,
>`or plateau near 1/8?`

The answer, over the **exact mean** over all weight-`w` strings (Krawtchouk
closed form `P_d(w) = (C(n,w) - [z^w](1-z)^{2^pc}(1+z)^{n-2^pc}) / (2C(n,w))`,
cross-checked against exhaustive `s_sos` on small n, and validated again here),
is:

## The ratio tends to 0 — resolved

`theta = w*/n` (first `w` with mean `nu2/n >= 0.40`), n = 8..32768:

| n | w* | theta=w/n |
| --- | --- | --- |
| 8 | 3 | 0.3750 |
| 10 | 3 | 0.3000 |
| 12 | 3 | 0.2500 |
| 14 | 4 | 0.2857 |
| 16 | 3 | 0.1875 |
| 32 | 5 | 0.1562 |
| 64 | 7 | 0.1094 |
| 128 | 11 | 0.0859 |
| 256 | 16 | 0.0625 |
| 512 | 24 | 0.0469 |
| 1024 | 35 | 0.0342 |
| 2048 | 52 | 0.0254 |
| 4096 | 77 | 0.0188 |
| 8192 | 112 | 0.0137 |
| 16384 | 164 | 0.0100 |
| 32768 | 239 | 0.0073 |

**theta is NOT monotone-decreasing from the start** (it rises 0.2500 at n=12
to 0.2857 at n=14), but **it is strictly decreasing from n=14 onward** and falls
well below 1/8 (0.1875 at n=16 is the only value near 1/8, then it keeps
falling). So the plateau-at-1/8 reading is REJECTED: the ratio → 0.

## The exact mean threshold weight, read absolutely

`w*(n) = 3,3,3,4,3,5,7,11,16,24,35,52,77,112,164,239` for
`n = 8..32768`. Not in the OEIS (checked, 16 terms). No catalogued closed form.

### Exponent fit (log-log least squares, error bars)

- all large-n rows (n=256..32768, 8 pts): **alpha = 0.557 ± 0.002**
- n=512..32768 (7 pts): 0.554 ± 0.002
- n=1024..32768 (6 pts): 0.553 ± 0.003
- n=2048..32768 (5 pts): 0.549 ± 0.002
- n=4096..32768 (4 pts): 0.545 ± 0.001

Per-doubling log2(w*)/log2(n) slopes between consecutive doublings of n,
from 16→32 onward: 0.737, 0.485, 0.652, 0.541, 0.585, 0.544, 0.571, 0.566,
0.541, 0.550, 0.543 — clustering **0.54–0.57**, gently drifting down.

### Model comparison (n=128..32768)

- **Pure power `C n^alpha`**: alpha ≈ 0.549–0.557, residuals small & structured
  (alpha drifts down as more large-n points are included).
- **`n^{1/2} (log n)^beta`**: beta ≈ 0.42, predicts w*(32768)=237.8 (actual 239) —
  fits essentially as well as the pure power at the top end.
- **`n^alpha (log n)^beta`**: alpha≈0.53, beta≈0.20 (beta not significant,
  se≈0.10).

**A pure power and `n^{1/2}(log n)^{0.4}` are numerically indistinguishable
over n ≤ 32768.** The data cannot decide between alpha→1/2 (with a log
correction) and alpha→≈0.55; what is excluded is clean: the growth is strictly
above `n^{1/2}` and strictly below `log_4(3)≈0.793` over the whole measured
range (predicted w*(32768) under 0.793 would be ≈395, actual 239; under 1/2
≈215, actual 239; both outside any reasonable error bar).

## The arithmetic demand, stated plainly

**About `n^0.55` switches (a sublinear count) suffice** for linear supply to be
*typical* (mean `nu2/n >= 0.40` over the weight-`w` layer). That is:

- strictly **weaker** than positive mod-4 switch density (~`c·n` switches), and
- strictly **weaker** than a positive *fraction* of switches — a sublinear
  count like `n^0.55` ≪ `n` is a far smaller demand on the primes.

## Status / caveats — read before using

- **measured-not-proved**: the closed form `P_d(w)` is exact (validated vs
  brute on n≤12); the *threshold* and the *exponent* are fits over the finite
  n-list, NOT proofs of a limit. The 1/8 plateau and the monotone-to-0 claims
  are data-supported, not theorems.
- **This is the MEAN half of "typical".** The "fraction >= 0.5" half of the
  definition was only sampled (n=256,512 in
  `threshold_limit_exact.txt`); the mean-half conclusion above is exact.
- **The mean over the weight-w layer is about *weight only*.** It says nothing
  about where the `w` switches sit. The primes are a *specific* string, not a
  random one, and being above the weight threshold does not prove the prime
  string has linear supply (the known "typical ≠ this string" gap).
- **No clean closed form** among `1/2`, `log_4(3)`, `ln2/ln3`, `0.55`, `0.565`
  is established; over the measured range `n^{1/2}(log n)^{0.4}` and `n^{0.55}`
  are both consistent. Say "fitted exponent ≈ 0.55", not a conjured constant.

## Handling the directive's two corrections

1. **theta monotonicity**: not "monotone decreasing toward 0" (fails at
   n=12→14, 0.2500→0.2857). Correct wording: "theta is decreasing from n=14
   onward".
2. **Sublinearity is the result**: read absolute weights. `w*(n)` grows like
   `n^0.55` (fitted), so the threshold *weight* is sublinear, and THAT is the
   strictly-weaker-than-switch-density statement.

**Claim block:** the authoritative claim for this result is filed by the
executing role in `code/out/threshold_exponent_pass3.md` as
`weight-threshold-tends-to-zero-sublinear-exponent` (fitted exponent
0.55678 ± 0.00225 over the tail n=256..32768, per-n w* exact from the verified
`P_d(w)` formula). Do not duplicate it; cite that id.
