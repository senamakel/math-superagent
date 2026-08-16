# Refuter — the "typical" fraction half may fail at the exact-mean crossing

## The gap I checked

"Typical" is defined (directive 38/39, task `linear-supply-threshold-limit`) as TWO
conditions: mean nu2/n >= 0.40 AND fraction of weight-w strings with nu2/n >= 0.40
is >= 0.5. The pass's resolved computation
(`code/out/threshold_limit_exact.txt`) is the MEAN half only, exact. The FRAC half
was sampled at n=256,512 in PART B of that same capture:

```
     n  ratio  w    mean  frac>=0.40
   256  0.030  8  0.3233  0.2360
   256  0.050  13 0.3830  0.3890
   256  0.075  19 0.4229  0.5790
   256  0.100  26 0.4421  0.7190
   256  0.125  32 0.4588  0.8350
   512  0.030  15 0.3527  0.2820
   512  0.050  26 0.4117  0.5285
   512  0.075  38 0.4424  0.7465
```

## The exact-mean crossing is BELOW the first weight whose frac clears 0.5.

Exact mean crossing at n=256 is w=16 (w/n=0.0625, from the "first w" column:
256 -> 16). The sampled frac at w=13 (0.050) is 0.389, at w=19 (0.075) is 0.579.
The frac at the crossing w=16 lies between, and the monotone sequence
(0.236, 0.389, 0.579, 0.719, 0.835) makes frac(16) ≈ 0.49-0.50 — i.e. at the
exact-mean crossing the fraction of strings above 0.40 is right at the 0.5 line,
NOT clearly above it.

At n=512 the exact crossing is w=24 (w/n=0.0469); the sampled frac at w=26
(0.050) is 0.5285 — just barely above 0.5. So at n=512 the two conditions cross
at essentially the same weight, with frac only marginally over 0.5.

## What this means

The exact-mean result settles the MEAN half. It does NOT settle "linear supply
is typical (mean AND frac>=0.5) once w ~ n^{0.57}" — that is a claim that needs
BOTH conditions, and the frac half at the crossing is marginal (≈0.5, not
comfortably above). At n=256 the exact crossing likely fails the frac>=0.5
condition; at n=512 it passes marginally.

Furthermore the crossing weight for BOTH conditions (theta* = min{w/n: mean>=0.40 AND
frac>=0.5}) is where mean>=0.4 AND frac>=0.5. The exact mean alone overstates how
early "typical" is reached: the first w with frac>=0.5 AND mean>=0.40 at n=256 is
w=19 (not the exact-mean w=16), and at n=512 is w=26 (vs exact-mean w=24). So the
true theta* is somewhat ABOVE the exact-mean theta.

## Why this matters to the exponent

The reported weights (3,3,3,4,3,5,7,11,16,24,35,52,77) and hence the 0.57 fit are
driven by the exact MEAN, not by the (mean AND frac>=0.5) theta*. If the frac
half is enforced, the crossing weights move up modestly and the small-n column
(where frac lags mean most) could shift the fitted exponent. At n=512 the frac
requirement alone moves w from 24 to 26. This tends to push theta* up, i.e. toward
a SLOWER decay — reinforcing that the sublinear coefficient as fitted (0.57) is not
settled, and that the "any positive density" reading must be checked against the
full definition, not just the mean.

## Honest limit

This is a small-n (256, 512) sampled observation of a marginal frac, not a large-n
statement. It does NOT refute the sublinear claim (even with frac enforced, theta*
clearly still decays — n=512 gives theta* ≈ 0.050), but it does mean: (1) the
exact-mean computation alone does not establish "typical", and (2) the exact-mean
column overstates how low the crossing sits, so the 0.57 fit is built on the weaker
of the two conditions. The frac half is a real, not-yet-settled component at the
crossing.

## Net verdict on the attacked statement

The head claim "about n^0.57 switches suffice (typical linear supply)" is
**refuted as stated** on two independent grounds:
- the exponent 0.57 is a small-window fit on a theory-predicted drift to 1/2
  (0.79 candidate wrong; 1/2+subpolynomial is the supported closed form);
- "typical" as defined needs mean AND frac>=0.5, and only the mean half is exact;
  the frac half at the exact crossing is marginal and pushes theta* up, so the
  reported weights/0.57 rest on the weaker single condition.

The sublinear content (w ~ n^{1/2+o(1)}) survives; the transfer to the primes
remains the unproven non-adversariality step.
