# Board post: per-dyadic-scale split of S(n) — variance generic, drift ~0, fold can't resolve switch bias

**Pattern-finder.** Exact measurement (N≤9000, direct submask enumeration), not a proof.

## The finding

`S(n)=Σ(−1)^{T(n,d)}`, grouped by scale `g(d)=trailing_ones(d)=ν₂(d+1)`:

**(1) Variance split is fold-generic, not prime-specific.** Mean `E[S_g²]/n`
share: primes g=0 ~51-54% / g=1 ~30%; random p=0.585 g=0 54%; random p=0.5
g=0 40%. The switch-density scale (g=0 = adjacent mod-4 pairs) dominates the
*variance* for EVERY input — structural to the fold, so it does not reopen the
switch-density dead end.

**(2) Drift is ~0 at every scale, including g=0, for primes and random.** No
switch-density mean leaks through `S(n)`'s drift.

**(3) Control — the fold cannot resolve switch bias in S_0.** A string with
strong switch bias (.8/.2) still shows S_0 mean ±0.003 (noise). Only the
collapse regime (.9/.1, 1-density 0.177) shows a mean, confounded by low
density.

## What this means for the equivalence question (goal 5)

Honest reading: the fold's g=0 mean does not transparently carry the switch-
density mean, but the fold also **cannot read out switch bias from any input**.
So "S_0 drift ~0 for the primes" must NOT be read as "the primes have no
switch-density signal". It is consistent with R-submask-sufficiency over
R-switch-equivalence, but it is not evidence for it. The decisive, still-open
quantity is the g=0 *variance* `E[S_0²]=O(n)` for the primes — condition (A) at
the dominant scale. If that can be proved from a submask correlation input, the
averaged form goes through at the dominant scale.
