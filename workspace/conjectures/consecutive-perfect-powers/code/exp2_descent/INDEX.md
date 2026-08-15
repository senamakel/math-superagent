# Index — code/exp2_descent

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `backward.p` | _(undescribed)_ |
| `consistency.p` | _(undescribed)_ |
| `forward_minus.p` | _(undescribed)_ |
| `forward_plus.p` | _(undescribed)_ |
| `min.p` | _(undescribed)_ |
| `verify_direction_split.py` | _(undescribed)_ |
| `verify_equivalence.py` | _(undescribed)_ |
| `verify_equivalence_bounded.py` | Corrected, bounded, terminating verifier of the round-trip bijection between the descent subclaim r^q - 2^(mq-2) s^q = ±1 and the Lebesgue case x^2 - y^q = 1, on the finite box x<=300000, m<=8, r,s<=300. Fixes the unbounded/infinite original (2·S^q was astronomically large); first successful capture equivalence_bounded.captured.txt confirms the bijection for all odd primes q in {3..37} and calibration (x,y)=(3,2) at q=3 (the known solution 3^2-2^3=1). |
| `verify_subclaim.py` | Two-route exact-integer verification of the Case-A descent sub-claim r^q - 2^{mq-2}s^q=±1 over q<=37, m<=8, r,s<=500 (route 1 direct sweep, route 2 via Lebesgue x^2-y^q=1), with cross-check; settled only (3,1,1,1). Correctness: cross-check restricted route-1 image == route-2 full image reported True (both {(3,3,2)}); the "0 found / calibration []" lines are cosmetic — route1_direct filters out (3,1,1,1) before appending, so 0 means zero counterexamples; confirmed by direct instrumentation replicating (3,1,1,1) from the unfiltered equation. |
