# Pattern-finder deliverable 5: the mod-4 switch bias is real, persists, and is fold-inert

**Role:** pattern-recognition specialist. All exact integers; only ratios are
floats. Guided by the canonical oracle (`code/out/nu2_primes_xor_40000.json`,
guards ν₂(53)=18, ν₂(64)=27, ν₂(4000)=1975, ν₂(40000)=20081 reproduced) and
`lib.supply_fold.s_sos` (cross-checked vs brute oracle). Every structural fact
is a **conjecture** for all n, labelled `measured`.

## The cleanest atom: the mod-4 consecutive-pair table

`h[j] = [q_{j+1} ≠ q_j mod 4]` is the whole input to SUPPLY's fold. Its atoms
are the consecutive-pair classes mod 4. Exact counts over the first N primes:

| N | (1,1) | (1,3) | (3,1) | (3,3) | switch | equal |
| --- | --- | --- | --- | --- | --- | --- |
| 40000 | 0.2096 | 0.2894 | 0.2894 | 0.2115 | 0.5788 | 0.4211 |

`switch = (1,3)+(3,1) = 0.5788`, matching the h density 0.5789. The switch
classes dominate the equal classes — the mod-4 **switch preference**.

## Result 1 (measured): the lag-1 anticorrelation of h is a persistent systematic signal

`corr(h_j, h_{j+1})` over the prime gap-parity string:

| N | lag-1 corr | \|corr\|·√N |
| --- | --- | --- |
| 500 | −0.152 | 3.4 |
| 4000 | −0.093 | 5.9 |
| 40000 | −0.0555 | 11.1 |
| 128000 | −0.047 | 16.9 |
| 256000 | −0.0416 | 21.1 |

**The discriminator:** if the anticorrelation were finite-sample noise,
`|corr|·√N` would stay ≈ constant (≈1). It climbs 3.4 → 21.1, so the signal is
**persistent and systematic**, not noise. All higher dyadic lags (2,4,8,…,4096)
are ≈ 0, so the structure is concentrated at lag 1.

## Result 2 (measured, cross-checked against a sourced claim): the bias decays at the LOS scale

The switch excess `p(N) − 1/2` over `[N=4000, 10⁶]` satisfies
`(p−1/2)/(loglog N / log N) ≈ 0.33–0.38`, essentially constant. This is
exactly the **loglog/log slow-decay scale** predicted by Lemke–Oliver–
Soundararajan for the equal/switch imbalance in consecutive-prime residues
mod 4 (claim `los-scale-bias-slowdecay`, asserted there). So the measured
signal is not an artifact — it is the real, expected mod-4 bias, and it decays
toward 0 (so it never by itself forces a positive constant switch density;
that rests on the LOS conjecture that the sign never reverses).

## Result 3 (measured, the decisive one): the bias is FOLD-INERT

The question that matters for SUPPLY is whether this lag-1 anticorrelation does
any work **under the fold Φ**. Answer: it does not.

- primes: `E[S(n)²]/(n−2) = 1.004` over n ∈ [1024, 20000].
- iid at the same switch density p=0.579: `E[S²]/(n−2) = O(1)`, same level.
- 2-state Markov with the primes' exact (p, lag-1 ac1): `E[S²]/(n−2)` stays
  O(1) ≈ 1 across n = 1024..16384.

So an input with **zero** lag-1 anticorrelation (iid) already achieves the same
uniform second-moment level as the primes. The primes' measurable switch bias,
however real and persistent, provides **no** second-moment advantage over the
fold — exactly the `bounded-raw-autocorr-not-discriminating` conclusion
reached earlier, now pinned to a concrete persistent measurement rather than
to iid's formal zero.

## Result 4 (measured, refines fold-genericity): asymptotic bias outlook

Because the switch excess decays to 0 (LOS scale), the lag-1 autocorrelation
also decays to 0 as N → ∞. The *direction* of the bias (switch-dominant,
off-diagonal-dominant) is the robust robustly-measured fact on every finite
range; the *magnitude* is lower-order. This is precisely why the switch-density
reduction says "positive density" (any c>0), not "density ≥ 1/2": the positive-
density claim would follow from the LOS conjecture, but is not itself proved.

## What this bounds for the run

1. **No new arithmetic handle.** The pattern-finder's exhaustive sequence work
   (`deliverable_3_fold_genericity`) is now complete at the atomic level: the
   one persistent prime-specific raw-input statistic — the mod-4 switch bias —
   is fold-inert. The fold Φ produces no measurable work that the
   switch-density form cannot see, at every statistic examined.

2. **The single open arithmetic step remains (A):** `E[S(n)²]=O(n)` for the
   real prime h. My measurement gives primes `E[S²]/(n−2) ≈ 1.004`, iid at the
   same p the same, Markov with the primes' params the same — all O(1). This is
   strong *measured* evidence that (A) is true and generic, but none of it is a
   proof; the unconditional second-moment bound for the specific prime string
   is the whole remaining barrier and is untouched by any sequence measurement.

3. **The ~9× margin** documented in `pattern_finder_price_autocorr_input.md`
   (fold stays O(1) up to anticorr 1−2a ≈ −0.74, primes at ≈ −0.08) is
   *consistent* with — and now corroborated by — the primes' measured lag-1
   anticorr ≈ −0.05..−0.15 over the examined ranges. Any proof of (A) has
   substantial slack before the balancing degrades.

## Honest status

- All four results are **measured** (exact arithmetic over the stated finite
  ranges), labelled conjectures for all n. Neither the persistence of the bias
  beyond N=10⁶ nor its LOS-scale decay is proved here; the LOS correspondence is
  a cross-check against a *sourced* claim (`los-scale-bias-slowdecay`), not a
  derivation.
- The fold-inertness verdict is the robust one: iid achieves the same second
  moment, which is exact for uniform h (`E[S²]=n−2`, claim
  `fair-model-exact-binomial` proved from rank). So the conclusion does not
  depend on the exact bias boundary.
- This does NOT close SUPPLY and does not reopen any of the five closed doors.
  It refines the honest negative frame: the last candidate prime-specific
  signal (mod-4 switch bias) is real but fold-inert.

## Files
- measurements here (exact); generated via `lib.primes`, canonical JSON, `s_sos`.
- `code/out/w_switch_terms.txt` — cumulative switch-count sequence (structureless, no recurrence).

## Claim block

```claim
id: mod4-switch-bias-real-persistent-fold-inert
statement: >
  The mod-4 consecutive-pair classes of the primes show a persistent,
  systematic switch preference: over the first N primes,
  switch density p(N) = ((1,3)+(3,1))-mass = 0.579@40000, with lag-1
  autocorrelation of the gap-parity string corr(h_j,h_{j+1}) = -0.0555@40000,
  -0.0416@256000, and |corr|*sqrt(N) growing 3.4->21.1 (so the signal is
  persistent, not noise). The switch excess p-1/2 decays at the LOS
  loglog/log scale (ratio 0.33-0.38, cross-checked vs claimed
  los-scale-bias-slowdecay). Yet the fold is inert to this bias: E[S(n)^2]/(n-2)
  = 1.004 for the primes, and O(1) identically for iid at the same p and for a
  2-state Markov with the primes' exact (p, ac1) - so the primes' measurable
  switch bias confers no second-moment advantage under Phi, confirming
  bounded-raw-autocorr-not-discriminating at the atomic level.
hypotheses: canonical floored fold; prime h from exact primes; iid/Markov
  controls at the measured primes' parameters; finite ranges quoted.
holds-here: yes (measured; exact arithmetic over the stated N).
status: checked (measurement; not a proof of the LOS decay or of SUPPLY)
bearing: >
  closes the last candidate prime-specific raw-input signal (mod-4 switch bias)
  as fold-inert, completing the fold-genericity frame at the atomic level; the
  single open step E[S^2]=O(n) for the real prime h is measured-true and
  generic but remains an unconditional arithmetic theorem. Consistent with the
  ~9x Markov margin.
anchor: code/out/pattern_finder_deliverable_5_mod4_switch_bias.md
```
