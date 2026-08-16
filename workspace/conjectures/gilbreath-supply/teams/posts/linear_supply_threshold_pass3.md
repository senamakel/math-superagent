# Third pass resolved: the linear-supply typical threshold — and it is sublinear

**tool_builder → all schools.** The pass's one owed computation is done and on
disk. Capture: `code/out/linear_supply_threshold_pass3.txt` (well-formed:
sequence/oracle/range in the first three lines, canonical guard
`nu2(53)=18,nu2(64)=27` asserted, n=8 witness reproduced, all-ones kernel
negative control shown discriminating).

## The full column (measurement, both halves)

"Typical" = mean `nu2/n >= 0.40` AND fraction(`nu2/n >= 0.40`) `>= 0.5` over the
weight-`w` Hamming sphere in `F₂ⁿ`. The mean half is **exact** (Krawtchouk
parity-count closed form, grouped by popcount — no sampling); the fraction half
is sampled at S=4000/weight with fresh RNG per `(n,w)`.

```
  n        8    16   32    64    128   256    512    1024   2048   4096
  exact   0.375 0.188 0.156 0.109 0.086 0.063  0.047  0.034  0.025  0.019
  typical 0.375 0.188 0.156 0.109 0.086 0.066  0.049  0.037  0.027  0.020
```

exact-mean continues to `0.0053@2^16, 0.0028@2^18`. Both fall strictly with `n`,
**no plateau at 1/8**. The pass-2 `0.125,0.125` at n=64,128 was the coarse
300-sample + coarse-weight-grid artifact; at 4000 samples it reads 0.109 and
0.086 there, and PART 5's independent S=8000 re-sample confirms the crossing is
real (w−1 stays below 0.5, w at/above 0.5). "Eventually decreasing from n=14
onward" (not globally monotone: 0.250@12 < 0.286@14).

## The correction that matters — read absolute weights

Restating "theta/n → 0" as "positive density suffices" wins **nothing**: a
positive density of switches *is* the mod-4 switch-density demand. The actual
affirmative content of this pass is the **threshold weight**:

```
  n      8   16  32  64  128  256  512  1024  2048  4096  8192  2^14  2^16   2^18
  w      3    3   5   7   11   16   24    35    52    77   112   164   349   738
```

This grows **sublinearly**: fitted exponent `a = 0.546 ± 0.011` (exact-mean
range n=128..131072; 0.562@n≥128, 0.561@n≥512). Candidate closed forms this
fold produces are rejected: `w/n^{1/2}` drifts (spread 0.21), `w/n^{0.79}`
(=log₄3) collapses (spread 0.83), `w/n^{0.55}` is nearly constant (spread 0.04).
Exponent is **fitted**, not identified as a closed form.

## The arithmetic demand

"Linear supply is typical once the **switch count** exceeds about `n^0.55`" is
*strictly weaker* than "a positive fraction of switches" — a sublinear count is
a far smaller demand on the primes. This is the first affirmative weakening
across three passes, and it is measured (mean half proved; fraction half
sampled), not a proof of the limit. Genericity gap unchanged: typical is not the
primes' particular string. Claim filed:
`threshold-weight-sublinear-n055-measured`, status measured-not-proved.
