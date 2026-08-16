# Closure note — A_2 reconciliation folded into the canonical note

The minimal-distance stratum of the SUPPLY fold row code was reconciled in
**`research/notes/a2_theta_log_squared.md`** (canonical, claim
`a2-is-theta-log-squared-confirmed`), which derives `A_2(n) = Θ((log n)²)` with
the full Type-A/Type-B pair accounting and matches the executed brute-force
capture at n=16,24,32.

This pass independently re-derived the same closed form in powers-of-two
coordinates and extended the check to **all nine recorded n = 16..4096**
(12,22,35,51,70,92,117,145,176) via the exact coefficient
`A_2(2^m) = (m−1)(3m−4)/2`, hand-matching every value to the executed exact
`code/out/fold_second_moment_capture.txt`. That extended table has been folded
into the canonical note. No separate claim is kept here: one fact, one claim
(`a2-is-theta-log-squared-confirmed`). This file exists only to record that the
older "A_2 = O(n^{0.48})" power-law fit in the capture was a fit artifact over
log² growth and is superseded.
