# abundance-profile-odd-filter-minmax

```skeleton
goal: Prove/verify: for every non-Boolean union-closed family F on [n], max-density(F) >= 2^{n-1}/(2^n-1). The VALUE is correct; the claimed "attained UNIQUELY by the odd filter 2^[n]\{∅}" is FALSE.
rests-on: half-density-max-eq-bool-subalgebra (max density = 1/2 implies Boolean, verified n<=5); uc verified n<=11; lib.uc oracle
status: refuted as stated (uniqueness); value confirmed
```

## Correction (this pass)

The value `2^{n-1}/(2^n-1)` is correct and verified (exhaustive n=2..4 by the
lib.uc oracle plus an independent inline route; structural fact exact to n=8).
But the **unique** minimizer is NOT the odd filter: the minimizers are exactly
**n+1** families for every n>=2 — the odd filter 2^[n]\{∅} plus the n
power-set-minus-singleton families 2^[n]\{{x}}, each of size m=2^n-1 with max
density 2^{n-1}/(2^n-1).

Claim `odd-filter-max-density-extremal-nonboolean` (filed, asserted) is the
authoritative record; capture `code/out/odd_filter_minmax.captured.txt`
(ALL CHECKS PASS, exit 0).

Do not re-open this as a uniqueness claim. The live abundance-profile work
belongs to the minimal-counterexample profile (parity |F|=2k+1, tight-witness,
no-degree-1) per `research/threads/abundance-profile.md`, not to this
min-max-density extremal (which concerns families whose max density is far
above 1/2 and is not a counterexample-relevant tightening).
