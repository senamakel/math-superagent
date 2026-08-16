# Pattern-finder: nu2 and S structure, and the re-grounding of the averaged form

## What I re-verified (and what changes)

The prior pattern-finder note (`pattern_finder_nu2_structure.md`) already ran
the sequence tools over `nu2(n)` and reported: no constant-coefficient linear
recurrence (order ≤ 12), not a low-degree polynomial, OEIS miss, dyadic
subsequence bounded away from 0. I re-ran the tools over the exact on-disk
terms and these rejections stand over the supplied terms:

- `nu2(n)`, n = 2..513 (exact from `code/out/nu2_terms.txt`): no linear
  recurrence of order ≤ 8; differences never become constant (not polynomial).
- `S(n) = n-2-2*nu2(n)` (from `code/out/supply_endpoint_density.txt`): no
  linear recurrence of order ≤ 6; not polynomial; residues mod 2 periodic with
  period 2 (trivial parity).
- Both sequences are OEIS misses (not catalogued), so no looked-up closed form.

These confirm the prior rejections with the terms on disk; none is a proof for
all n. I did not dress any fit up as a proof.

## The finding that actually advances the averaged form

The equivalent-form quantity is the endpoint character-sum

    S(n) = sum_{d=2}^{n-1} (-1)^{T(n,d)} = n - 2 - 2*nu2(n),

so `nu2(n)/n = 1/2 - S(n)/(2n) - 1/n`. SUPPLY is then exactly: `S(n) <= (1-2c)n`
eventually — the endpoint character sum bounded above by a positive fraction of
n. Measured exactly over n ≤ 4000:

    running max of |S(n)|  over n ≤ N, ratio to N:
      N=100: 0.2300    N=500: 0.1200    N=1000: 0.1040
      N=2000: 0.0600   N=3000: 0.0593   N=4000: 0.0550
    absolute max |S| over n≤4000 = 220 (at n=3948)

So `max_{n≤N} |S(n)|/N -> 0` numerically, which would push `nu2(n)/n -> 1/2`
pointwise — strictly stronger than SUPPLY. Whether this sublinearity of |S(n)|
is provable (e.g. from an autocorrelation/variance bound on the prime-residue
string) is the most promising route toward GOAL priority 1 (the averaged / 
density-1 linear bound). Caveat: this is numerical evidence up to n=4000 only;
extending the measurement is the natural next step, via the O(n log n) SOS
transform (already streamed successfully to n=20000).

## Re-grounding the averaged form (answers the solver critique)

The one genuinely under-reported structural fact was that the negative
controls the solver said were "never run" ARE on disk. `code/out/
averaged_mean_capture.txt` separates the three input families cleanly — on the
MEAN, not the variance:

| family | M(100) | M(1000) | M(4000) | M(8000) | behaviour |
| --- | --- | --- | --- | --- | --- |
| primes | 0.4394 | 0.4906 | 0.4973 | 0.4985 | rising → 1/2 |
| all-ones (kernel) | 0.0000 | 0.0000 | 0.0000 | 0.0000 | exactly 0 |
| Thue–Morse | 0.2255 | 0.1080 | 0.0641 | 0.0489 | falling → 0 |

Here M(N) is the Cesàro mean of nu2(n)/n over n ≤ N. I re-computed all three
independently with a fresh `stream_stats` call, not trusting the stored file:

    primes     : final mu = 0.49543 @2000, 0.49738 @4000
    all-ones   : final mu = 0.00000 @2000, 0 @4000   (nu2 ≡ 0, kernel vector)
    thue-morse : final mu = 0.08367 @2000, 0.06416 @4000

All match the stored artifact. The separation is clean and is evidence for the
averaged/density-1 form: the primes' mean rises toward 1/2 while both controls'
means fall to 0. The prior claim "variance decays" proved nothing because
all-ones' variance also decays; the mean is the discriminating statistic, and
it separates the primes from the controls.

## Evidence classes

- Recurrence/polynomial rejections: exact over the supplied terms (the tools
  are exact), not a proof for all n.
- The S(n) sublinearity and the mean values: exact integer arithmetic over
  published ranges, independently reproduced; numerical, not a proof. The dying
  low-ratio tail (only sparse points below any fixed c, all at bounded n) is
  the shape a density-1 linear bound would have, but is not one.
