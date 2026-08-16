# Directive 45 — is the threshold-weight exponent 1/2? (librarian hand-check)

The operator's hypothesis (after the extended data): "1/2 is now in range."
Directive 45 asks to test `w = c·sqrt(n)` directly by tabulating `w/sqrt(n)` —
if that column is flat the exponent is exactly 1/2.

This note is **hand arithmetic over the 10 listed values** (exact, small
integers; no program was run — I hold no execution tool). It must be confirmed
by the coder's mechanical run (`code/out/librarian_directive45_discriminate.py`,
whose `w/sqrt(n)` table it anticipates). Label: exact-by-hand, **not** program
output.

## The data (operator's theta column, n = 64 .. 32768)

    n      64   128   256   512  1024  2048  4096  8192  16384  32768
    w       7    11    16    24    35    52    77   112    164    239

## w / sqrt(n)   (the clean 1/2 test)

    n      64   128   256   512  1024   2048   4096    8192   16384   32768
    sqrt    8  11.31  16   22.63  32   45.25    64    90.51   128    181.02
    w/sqrt .875 .972  1.000 1.061 1.094 1.149  1.203   1.237  1.281  1.320

**Not flat — monotonically RISING from 0.875 to 1.320, a ~51% climb.** A flat
`w/sqrt(n)` column is what `w = c sqrt(n)` (exponent 1/2) requires; a steadily
rising column is the signature of an exponent strictly above 1/2. So on the
operator's own flatness test, **1/2 is rejected by this data**, not "in range".

## Companion candidates (same hand test, relative rise over the range)

    w/(sqrt(n)·ln n)    : 0.210 @64 -> 0.127 @32768   (falls ~40%)  → rejects
    w / n^log_4(3)      : 0.259 @64 -> 0.063 @32768   (falls ~76%)  → rejects
    w / n^0.55          : 0.711 @64 -> 0.785 @32768   (rise ~10%)   → best fit

The 0.55 power is the flat column; 1/2, sqrt·log, and log_4(3) all drift by
40–76%. This agrees with the on-disk fitted captures
(`code/out/threshold_exponent_fit_pass3.txt`, `E = 0.55678 ± 0.00225` over
n≥256; per-doubling slopes in the large-n tail 0.5406,0.5443,0.5712,0.5663,
0.5406,0.5502,0.5433 — the last four are 0.5663,0.5406,0.5502,0.5433, mean
≈0.550, so the local slope is ~0.55 and mildly drifting, not settling up at
0.57). The operator's earlier 0.57 was from the shorter range; the per-doubling
slope over the last four doublings is ≈0.550.

## Verdict

Directive 45's "1/2 is now in range" is **refuted by the flatness test**: the
`w/sqrt(n)` column climbs monotonically by ~51%, which is exactly the same
drift that made the existing captures reject 1/2 (rel spread 0.21). The
exponent is fitted at `~0.55`, not a clean closed form; neither `1/2`,
`sqrt·log`, nor `log_4(3)` is supported. The honest statement stays:
**linear supply is typical once the switch weight exceeds ~n^0.55** —
sublinear, strictly weaker than a positive fraction — with the exponent a
numerical fit over n ≤ 32768, not a proven asymptotic law, and the
"typical is not this string" genericity gap to the primes' own h intact.

Caveat I checked: `w/sqrt(n)` rising could in principle be `w = c sqrt(n)·(log n)^b`;
the companion `w/(sqrt(n) ln n)` column falls, so a pure log factor overshoots;
`model_compare.py` already showed the pure power and `n^0.5 (ln n)^b` fit
equally over n=128..32768 and neither closed form is decided. So "flatness
rejects 1/2" is the hard finding; which sublinear family wins is not resolved
by hand data.
