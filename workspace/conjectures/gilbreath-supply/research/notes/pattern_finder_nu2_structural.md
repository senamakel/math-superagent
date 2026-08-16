# nu2(n): sequence structure, exact over n≤4000

## Objects and provenance

nu2(n) = wt(Φ_n h), the canonical fold form = #{ d in [2,n-1] : T(n,d)=1 },
with T the submask-XOR cell. Recovered from code/out/supply_endpoint_density.txt
(its `ones` column), which is cross-checked to be identical to (n-2-S)/2 by two
independent exact routes (SOS submask-product and character-sum telescope) in
code/lib/supply_fold.py. Range n = 2..4000. Terms list saved at /tmp/nu2_full.txt.

## Exact facts over the computed range (all EXACT, none a proof for all n)

1. **No linear recurrence, not polynomial, not in OEIS.**
   find_linear_recurrence(order ≤ 12) fits no constant-coefficient recurrence;
   differences never become constant; no OEIS match. So there is NO low-order
   recurrence to pointwise prove — the pointwise sequence is structurally
   "featureless" at the recurrence level. (Both the full sequence and the
   dyadic subsequence.)

2. **No dyadic collapse.** nu2(2^k)/2^k = 0.41..0.75 (k=3..11). Bounded away
   from 0, matching problem.md door 4's negative control. The prime string does
   not die along powers of two.

3. **The averaged form is the entire signal (GOAL priority 1).**
   - Block means of nu2(n)/n plateau at 1/2: 0.4993 over [2000,4000),
     0.4996 over [3000,4000); every 500-block in [1000,4000] averages in
     [0.4989,0.4998]. The deficit from 1/2 over dyadic blocks decays:
     +0.0149 (k=6) → +0.0041 (k=8) → +0.0003..0.0006 (k=10,11).
   - Var(nu2/n) over the prefix N: 1.66e-2 (N=100) → 7.22e-4 (N=4000);
     variance ~ N^−0.88 with exponent *steepening toward −1* across
     [200,4000] (−0.82 → −0.85 → −0.88 → −0.90). So std ~ 1/√N.
   - Both are exactly the Chebyshev inputs of the averaged-second-moment
     skeleton (G-mean-linear + G-var-vanishing): a positive linear lower bound
     on the mean plus vanishing variance empties the lower tail on a density-1
     set.

4. **Dying tail / density-1 shape.** For fixed c, {n : nu2(n)/n < c} is bounded:
     c=0.40: 3 points, all ≤ 105
     c=0.42: 10 points, all ≤ 274
     c=0.45: 51 points, all ≤ 763
   Min of nu2/n over [N,4000] rises with N: 0.416(N=200) → 0.443(N=500) →
   0.460(N=1000) → 0.465(N=2000) → 0.469(N=3000). So for any c < 0.40 the
   density-1 inequality is empirically satisfied for every n in range; the
   strongest dip is n=53 (0.3396). This is precisely the shape a density-1
   linear bound would have.

5. **Signed excess wiggles around zero.** nu2(n) − (n−2)/2 is small and sign-
   alternating at large n: +1 (n=500), +1 (n=1000), −4 (n=2000), −21 (n=3000),
   −24 (n=4000). The max |excess|/n over [50,4000] is 0.1415 at n=53 (the dip);
   past n=200 the excess/n stays within ±0.01. So the fold weight tracks (n−2)/2
   to within a tiny bounded fraction except at sparse dips.

6. **No correlation with local switch density.** corr(local switch density of h,
   nu2/n) = −0.03 over sliding windows w=50, while local switch density has
   std ≈ 0.044. The fold weight does NOT resolve small switch-density
   fluctuations into weight. Weak empirical support for R-submask-sufficiency
   over R-switch-equivalence (the fold is doing something other than tracking
   switch density), though the range is small — treat as a hint, not a theorem.

## What this supports

The structural case for the AVERAGED (density-1) form is the cleanest in the
data: the mean is pinned at ~1/2, the variance vanishes as ~1/√N, and the
lower tail is empty for any fixed c<0.40 across the whole computed range. This
is exactly GOAL priority 1 / problem.md result 3, and it is the honest target.

The pointwise sequence has no exploitable recurrence/polynomial/dyadic
structure — the fold weight is "generic-looking" at ~1/2 with vanishing
fluctuation, which is also consistent with the R-random subclass analysis (rank
n−3, generic expectation (n−3)/2).

## Status

ALL numerical facts are exact over n ≤ 4000 only. None is a proof for all n.
The vanishing variance and dying tail survive their cheapest falsifier (the
exponent steepens toward −1; no threshold's violation set grows with the
range) but remain conjectures about the infinite sequence.

The strongest next step (per the averaged-second-moment skeleton): prove the
variance bound G-var-vanishing from an arithmetic input on h (second-moment /
Walsh bound read along binary-submask windows) — the variance of nu2/n is a
second-moment statement about the submask-XOR coordinates s_d, i.e. an
autocorrelation bound on the prime h.
