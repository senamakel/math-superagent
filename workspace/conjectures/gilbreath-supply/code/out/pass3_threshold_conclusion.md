# Third pass — conclusion: the weight-threshold computation

**The one computation this pass owed is done.** The minimum weight ratio `w/n` at
which linear supply becomes *typical* (`mean ν₂/n ≥ 0.40` AND `frac ≥ 0.5`)
**tends to 0**; it does **not** plateau near 1/8.

## The column (exact mean; frac sampled at S = 4000 per (n,w), fresh RNG)

```
n      8     16    32    64    128   256   512   1024  2048  4096  8192  16384  32768
theta  0.375 0.188 0.156 0.109 0.086 0.063 0.047 0.034 0.025 0.019 0.014 0.010  0.0073
```

The exact-mean half is **proved per-n** (no sampling): it is the closed form
`mean_n(w) = (1/n) Σ_{d=2}^{n−1} P_d(w)` with
`P_d(w) = ( C(n,w) − [z^w](1−z)^k(1+z)^{n−k} ) / (2 C(n,w))`, `k = 2^popcount(d)`
— the mean of `ν₂/n` over all weight-`w` strings. Verified by a fully
independent code path (direct hypergeometric odd-count + literal brute `s_sos`),
digit-for-digit to n=16384, extended to n=32768.

The 1/8 plateau at n=64,128 was a **sampling-resolution artifact**: the exact
mean at n=64 is already 0.1094 and keeps falling.

## The exponent (operator directive, executed)

Log-log regression of `w*` vs `n` over the tail n≥256:
**E = 0.55678 ± 0.00225** — the threshold *weight* grows like `n^0.56`
(sublinear), settling in the 0.54–0.58 band per doubling.

- `|E − 1/2| = 0.057`, `|E − log_4(3)=0.7925| = 0.236` — it is **neither** clean constant; it is a **fitted** value, not a closed form.
- Per-doubling slopes settle: 0.585, 0.544, 0.571, 0.566, 0.541, 0.550, 0.543.

## The arithmetic demand it reduces to

Linear supply is typical once the switch count exceeds **~n^0.56**. That is
**strictly weaker** than pointwise mod-4 switch density (which asks for a
*positive fraction*, i.e. `Θ(n)` switch pairs): a sublinear switch count is a far
smaller demand on the primes. That sublinear count is this workspace's **first
affirmative weakening** across three passes — the required input drops from a
positive fraction of switches to a sublinear `~n^0.56` switch count plus
non-adversariality.

## Honest bounds on the claim

- The per-n `w*` and `theta` values are **exact** for each n.
- The **limit** (tends-to-0) and the **exponent** are **fitted** from the measured
  range n ≤ 32768 — supporting data, not a theorem. The measured range does not
  rule out an eventual plateau at a smaller positive `c`, but it decisively
  removes the concrete "plateaus at 1/8" hypothesis.
- One-sentence genericity gap: **"typical is not this string"** — being above the
  threshold does not prove the primes' particular `h` has linear supply.

## Corrections carried from the steering directive

(1) `theta` is **decreasing from n=14 onward**; it is NOT monotone decreasing
from the start (0.2500 at n=12 rises to 0.2857 at n=14). All statements say
"eventually decreasing."

(2) The result is stated in **absolute weights**, not ratios: the threshold
weight `w* = 3,3,3,4,3,5,7,11,16,24,35,52,77,112,164,239` for n=8..32768 grows
like `n^0.56`, **sublinear**. "Positive density suffices" would be a restatement
of switch density and wins nothing; "about n^0.56 switches suffice" is the
genuine weakening.

## Captures

- `code/out/linear_supply_threshold_pass3.txt` (7668 B, real capture — was 0 bytes)
- `code/out/threshold_exact_mean_independent.txt` (7101 B, independent route)
- `code/out/threshold_limit_exact.txt` (prior exact-mean, cross-checked)
- `code/out/threshold_exponent_fit_pass3.txt` (exponent fit)
- `code/out/threshold_exponent_pass3.md` (claim block
  `weight-threshold-tends-to-zero-sublinear-exponent`, measured-not-proved)
