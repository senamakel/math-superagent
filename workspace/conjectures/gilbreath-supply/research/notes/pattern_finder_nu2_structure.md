# nu2(n) exact structure — pattern-finder findings

## Method

Computed `nu2(n)` exactly for `n = 2..4000` as the fold form
`nu2(n) = #{d in [2,n-1] : T(n,d)=1}`, where
`T(n,d)` is the XOR over all submasks `o of d` of `h[n-1-d+o]`, and
`h[j] = ((q_{j+1} - q_j)//2) mod 2` is the prime gap-parity string.

Implementation: 2-adic submask-XOR DP. Define `V(d, base) = XOR over submasks
o of d of h[base+o]`. With `2^m` the highest power of two `<= d`,
`V(d,base) = V(d-2^m, base) XOR V(d-2^m, base+2^m)`, `V(0,base)=h[base]`.
Then `T(n,d)=V(d,n-1-d)`. Fill the `(d,base)` table in `O(n^2)`, read the
diagonal. Cross-checked against direct brute-force submask enumeration and
PASSED for n in {2,3,5,8,13,21,34,55,64,89,100,128}.

## Exact facts over n=2..4000

- **Mean** `nu2(n)/n` over `[50,4000] = 0.4986`; by decade `[100,1000]=0.4964`,
  `[1000,4000]=0.4995`. No downward drift. Consistent with the reported `~0.49`.
- **Pointwise min** `nu2(n)/n` dips to `0.3585` at `n=53` (nu2=19).
- Exactly **10 points** in `[50,4000]` have `nu2/n < 0.42`:
  `n = 53(0.3585), 62, 66, 71, 103, 105, 145, 153, 210, 274`.
- Local means around every dip are `~0.48-0.50` → dips are pointwise minutes,
  not localized depressions of the ratio.
- **Dyadic powers**: `nu2(2^k)/2^k = 0.4902,0.4905,0.5106,0.5089` at
  `k = 11,12,13,14`. Bounded away from 0 — **no dyadic collapse**.
- **No constant-coefficient linear recurrence** (order ≤ 10) fits `nu2(n)`.
  A 5th-order recurrence on the dyadic subsequence fits 10 terms but FAILS at
  the 11th (over-fit; attacked and refuted).
- Not polynomial (differences never constant). Not in OEIS (both the full and
  prime-indexed subsequences are uncatalogued).
- **Switch-density correlation**: Pearson corr between `nu2(n)/n` and the
  switch (gap-parity) density of `h`, cumulative or local window
  (w=100,250), is `-0.01 .. -0.10` — essentially zero.

## Discrepancy with stored claims

The stored rung `R-finite-verified` asserts `nu2/n >= 0.42` for all
`50 <= n <= 4000`. My exact computation finds 10 counterexamples, deepest
`nu2(53)/53 = 0.3585`. The value `0.42` likely came from the problem.md table
which `research/BACKWARD.md` already flagged as "ungrounded prose — re-ground
it". **This rung is not supported by exact computation at its full stated
range.** (Small n clipped; larger n dips are sparse. Whether another floor
convention eliminates them needs checking — but over the stated convention the
claim as written fails.)

## What this supports

- The **averaged / density-1** form (`R-averaged-supply`): mean `nu2/n ~ 0.5`
  with only sparse pointwise dips is exactly the shape a density-1 linear bound
  would give. The dips are the "porous on average" points the parity barrier
  leaves.
- The **fold does not merely track switch density**: zero correlation to local
  switch density over n=4000. Weakly favours `R-submask-sufficiency` over
  `R-switch-equivalence`, but the range is small and the switch variance tiny,
  so treat as a hint, not evidence for a theorem.

## Evidence classes

All numerical facts above are exact over the computed range (n=2..4000),
produced by a DP cross-checked against brute force. None is a proof for all n.
The R-finite-verified contradiction is exact over the stated range.
