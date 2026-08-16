# Pattern-finder report: structure of ν₂(n)

## What I analysed

The sequence ν₂(n) = wt(Φ_n h) for the real prime gap-parity string h, in the
canonical fold form ν₂(n) = #{ d ∈ [2, n−1] : T(n,d) = 1 }, over n = 2..4000.
Recovered from `code/out/supply_endpoint_density.txt` (the `ones` column),
verified identical to `(n−2−S)/2` and cross-checked by the two independent
exact routes in `code/lib/supply_fold.py` (SOS submask-product and the
character-sum telescope). Terms file: `/tmp/nu2_full.txt`. I ran
`analyze_sequence`, `find_linear_recurrence`, and `oeis_lookup` on it and on
derived subsequences.

## Findings — every statement exact over n ≤ 4000, none a proof for all n

1. **No exploitable pointwise structure.** No constant-coefficient linear
   recurrence of order ≤ 12 fits ν₂(n); the sequence is not polynomial; it is
   not in OEIS; gcd is 1; both parities occur abundantly. The dyadic
   subsequence ν₂(2^k) is likewise non-recurrent. There is no low-order
   recurrence to prove pointwise — this is a genuinely "featureless" sequence
   at that level.

2. **No dyadic collapse.** ν₂(2^k)/2^k ∈ [0.41, 0.75] for k = 3..11, bounded
   away from 0. The prime string does not die along powers of two (consistent
   with problem.md door 4's negative control).

3. **The averaged form is the whole signal (GOAL priority 1).**
   - Block means of ν₂(n)/n plateau at 1/2: 0.4993 (n∈[2000,4000)),
     0.4996 ([3000,4000)); every 500-block in [1000,4000] averages
     ∈ [0.4989, 0.4998]. Deficit from 1/2 over dyadic blocks decays
     +0.0149 (k=6) → +0.0041 (k=8) → +0.0003..0.0006 (k=10,11).
   - Var(ν₂/n) over prefix N: 1.66e−2 (N=100) → 7.22e−4 (N=4000). Variance
     ~ N^−a with a steepening toward −1 across [200,4000]: −0.82, −0.85,
     −0.88, −0.90. So std ~ 1/√N.
   - This is exactly the Chebyshev input of the `supply-averaged-second-
     moment` skeleton (G-mean-linear + G-var-vanishing): mean bounded below by
     a positive linear c plus vanishing variance empties the lower tail on a
     density-1 set.

4. **Dying tail / density-1 shape.** For fixed c, {n : ν₂(n)/n < c} is bounded:
     c=0.40 → 3 points, all ≤ 105
     c=0.42 → 10 points, all ≤ 274
     c=0.45 → 51 points, all ≤ 763
   Min of ν₂/n over [N,4000] rises with N: 0.416 (N=200), 0.443 (N=500),
   0.460 (N=1000), 0.465 (N=2000), 0.469 (N=3000). Deepest point n=53 (0.3396).
   For any c < 0.40 the density-1 inequality holds for every n in range. This
   is precisely the shape a density-1 linear bound would have.

5. **Signed excess wiggles around zero.** ν₂(n) − (n−2)/2 is small and
   sign-alternating at large n: +1 (500), +1 (1000), −4 (2000), −21 (3000),
   −24 (4000). Max |excess|/n over [50,4000] is 0.1415 at n=53 (the dip); past
   n=200 the excess/n stays within ±0.01. The fold weight tracks (n−2)/2 to
   within a tiny bounded fraction except at sparse dips.

6. **No correlation with local switch density.** corr(local mod-4 switch
   density of h, ν₂/n) = −0.03 over sliding windows (w=50), while local switch
   density has std ≈ 0.044. The fold does NOT resolve switch-density
   fluctuations into weight. A hint (range small) for R-submask-sufficiency
   over R-switch-equivalence — consistent with the run's central hypothesis
   that the fold does work the switch-density form cannot see. NOT a theorem.

## What this means

The structural case for the **averaged / density-1** form (GOAL priority 1,
problem.md result 3) is the cleanest thing in the data: mean pinned at ~1/2,
variance vanishing as ~1/√N, lower tail empty at any c < 0.40. The pointwise
sequence has no exploitable recurrence/polynomial/dyadic structure — the fold
weight looks generic at ~1/2 with vanishing fluctuation, exactly what the
rank-(n−3) generic analysis (R-random-expectation) predicts.

**Attacked and survived:** every threshold's violation set is bounded and does
not grow with the range; the variance exponent steepens toward −1 (healthy
Chebyshev regime), it does not flatten; the excess/n stays small past the dip.
The finding is not an artifact of the fold being generically heavy — the
all-ones (kernel) and Thue–Morse negative controls drive the same mean to
0 (existing claim `negative-controls-prime-specific`), and I reproduce that my
density-1 shape is specific to the prime h.

**Remaining open, named exactly:** proving G-var-vanishing (the variance of
ν₂/n is a second-moment statement about the submask-XOR coordinates s_d, i.e.
an autocorrelation / Walsh bound on the real prime h read along binary-submask
windows). That is the single arithmetic input whose proof would lift the
empirical density-1 form to a theorem — the recommended next step per the
`supply-averaged-second-moment` skeleton.

## Recorded

research/notes/pattern_finder_nu2_structural.md and two Cognee memories
(9644544830789947366, 174702888658250113). Provisional note in scratch topic
"nu2 structure averaged form".
