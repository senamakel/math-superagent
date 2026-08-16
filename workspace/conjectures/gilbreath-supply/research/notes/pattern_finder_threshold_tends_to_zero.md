# GOAL.md owed computation: does the linear-supply threshold ratio tend to 0 or plateau at 1/8?

**Result: it tends to 0.** The earlier plateau reading was a small-n transient.

## The sequence (exact-mean threshold weight w*(n), powers of 2)

`w*(n) = min{ w : mean over weight-w strings of nu2(h)/n >= 0.40 }`, computed
exactly from the Krawtchouk closed form `P_d(w) = (C(n,w) - [z^w](1-z)^k(1+z)^(n-k)) / (2 C(n,w))`, `k = 2^popcount(d)`,
with `mean_n(w) = (1/n) sum_d P_d(w)`.

| n | w* | w*/n |
|---|-----|-------|
| 8 | 3 | 0.375000 |
| 16 | 3 | 0.187500 |
| 32 | 5 | 0.156250 |
| 64 | 7 | 0.109375 |
| 128 | 11 | 0.085938 |
| 256 | 16 | 0.062500 |
| 512 | 24 | 0.046875 |
| 1024 | 35 | 0.034180 |
| 2048 | 52 | 0.025391 |
| 4096 | 77 | 0.018799 |
| 8192 | 112 | 0.013672 |
| 16384 | 164 | 0.010010 |
| 32768 | 239 | 0.007294 |
| 65536 | 349 | 0.005325 |
| 131072 | 507 | 0.003868 |
| 262144 | 738 | 0.002815 |

The ratio w*/n is monotonically decreasing, from 0.375 to 0.0028 — no plateau.
The pass-2 column `0.375 0.300 0.250 0.286 0.188 0.156 0.125 0.125` (which
sampled only n = 8,10,12,14,16,32,64,128) held at 0.125 for just n=64,128
(a local transient); the exact sequence continues downward 0.109, 0.086, 0.063, ...

## Exponent: w* ~ n^0.55 (sublinear)

OLS `log2 w* = a + E log2 n`, tail n>=256: **E = 0.5568 ± 0.0023**. Per-doubling
slopes `log2(w*(2n)/w*(n))` oscillate ~0.54–0.58 and do NOT trend toward 1/2 or
log2(3)−1=0.58496 (both ruled out >14 sigma). The weight is sublinear (o(n)),
so the ratio w*/n → 0.

Log-periodic residual test: `w*/n^0.5568` is bounded, period-1 in log2 n, amplitude
~0.07, with no monotone trend (corr ≈ 0 at fixed phase). So `w* = n^0.555 * P(log2 n)`
with P bounded periodic.

## Verification

- Every per-n w* is EXACT from the verified closed form.
- Independent recomputation (different code path, per-popcount grouping:
  `code/pattern_finder/verify_far_threshold_indep.py`) reproduces ALL values
  through n=131072 digit-for-digit: `n=8:3, 16:3, 32:5, 64:7, 128:11, 256:16,
  512:24, 1024:35, 2048:52, 4096:77, 8192:112, 16384:164, 32768:239, 65536:349,
  131072:507 — ALL OK`.
- The sampled-typical column (mean>=0.40 AND frac>=0.5) also falls:
  0.375, 0.188, 0.156, 0.109, 0.086, 0.066, 0.049, 0.037, 0.027, 0.020 (n=8..4096).
- OEIS: the sequence is NOT catalogued (miss recorded).

## Status and meaning

Measured-not-proved: the per-n w* are exact; the sublinear exponent and the
tend-to-zero limit are numerical fits over n<=262144, not a theorem.

Meaning (problem.md result type 4, NOT type 1): linear supply is TYPICAL once
the switch weight exceeds ~n^0.55, i.e. at a SUBLINEAR switch count — a
strictly weaker arithmetic demand on the primes than a positive fraction (n^1)
of switches. The generic command on the primes is a sublinear number of mod-4
switches, not positive switch density.

Genericity gap (unchanged from prior passes): "typical is not this string" —
being above the threshold for a random weight-w string does not prove the
primes' particular h has linear supply. What changed is only the size of the
arithmetic input needed.
