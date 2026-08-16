# Pricing the "bounded autocorrelation of h" input (GOAL priority 2/4)

```claim
id: bounded-raw-autocorr-not-discriminating
statement: >
  The fold second-moment ratio E[S(n)^2]/(n-2) (S(n) the signed excess of the
  floored submask fold; density-1 SUPPLY holds iff this is O(1)) stays at the
  uniform level ~1 for iid random input (p=0.5: 0.80-1.11; primes 0.97-1.12;
  iid at p=0.569: ~1.1) but grows ~ n for Thue-Morse (~4000-8400) and
  alternating 0101 (~n). Hence "bounded (or small) autocorrelation of the raw
  gap-parity string h" is NOT the discriminating arithmetic input: iid has
  essentially zero centred autocorrelation and already passes, so the primes
  are not special in that family.
hypotheses: canonical floored fold nu2=wt(Phi_n h); S=(n-2)-2nu2 exact;
  iid-uniform E[S^2]=n-2 exact (enumerated n=3..7); SOS cross-checked vs
  brute oracle.
holds-here: yes (measured; new computations of iid/thue/alternating and markov
  chain, primes from guard-checked N=40000 JSON).
status: measured-not-proved — the O(1) vs O(n) verdicts are exact on the
  computed ranges but conjectural for all n.
bearing: >
  Prices GOAL priority 2's "bounded autocorrelation of h" candidate: it is
  satisfied trivially by iid, so it cannot be the weakest input that separates
  the primes from collapse. The separation is instead the submask-window
  cross-correlation sum inside E[S^2]=O(n), which is the object the density-1
  form actually reduces to.
anchor: research/notes/pattern_finder_price_autocorr_input.md
```

```claim
id: anticorrelation-margin-of-the-fold
statement: >
  For two-state Markov chains in h (switching prob a, autocorrelation
  (1-2a)^k), the fold second moment E[S(n)^2]/(n-2) stays O(1) (density-1
  SUPPLY) for all anti-correlation up to 1-2a ~ -0.74 (a ~ 0.87), growing
  superlinearly only beyond |1-2a| >~ 0.75 and collapsing near -0.9.
  Measured prefix-mean ratios: 0.94 (a=0.5) -> 1.39 (a=0.8) -> 2.85 (a=0.86)
  -> 3.85 (a=0.88) -> 5.24 (a=0.90) -> 38.98 (a=0.95), n in [1024,49152].
hypotheses: two-state Markov inputs, balanced (p=1/2), canonical fold.
holds-here: yes (measured over the stated family and range).
status: measured-not-proved — boundary is empirical for the Markov family only.
bearing: >
  The primes' centred lag-1 autocorrelation ~ -0.04 (a ~ 0.52) sits at
  1-2a ~ -0.08, giving a ~9x empirical margin before the fold's balancing
  degrades. So any proof of E[S^2]=O(n) for the primes has substantial slack,
  and the weakest required input is bounded-variance submask-window
  autocorrelation, not raw-h autocorrelation.
anchor: research/notes/pattern_finder_price_autocorr_input.md
```

Role: pattern-recognition specialist. All numbers are exact integer/ratio
arithmetic (`lib.supply_fold.s_sos`, the submask-product SOS, cross-checked
against the brute submask-XOR oracle; canonical guard values ν₂(53)=18,
ν₂(64)=27, ν₂(4000)=1975 reproduce from the authoritative
`code/out/nu2_primes_xor_40000.json`). Nothing here is a proof for all n —
every claim is a conjecture / exact measurement.

## Setup

The whole averaged (density-1) form of SUPPLY reduces, via
`E[S(n)²] = O(n)` for the prime gap-parity string h, to a **second-moment
input** on h (GOAL priority 2). Specifically:

```
S(n) = Σ_{d=2}^{n-1} (−1)^{T(n,d)},   T(n,d) = ⊕_{s⊆d} h[n-1-s]
ν₂(n) = (n−2−S(n))/2        [exact]
density-1 SUPPLY  ⟸  E[S(n)²] = O(n)   [Markov/Chebyshev tail]
```

Condition (C) (fold geometry: A₂=O(n^0.68), F_n(1−2p)=O(n)) is already settled
on disk; the single open arithmetic step is `E[S²]=O(n)` for the *real prime h*.

## The candidate priced here: does "bounded autocorrelation of h" suffice?

This run's GOAL priority 2 lists "bounded autocorrelation of h" as one weaker
arithmetic input worth pricing. The clean test: does the fold second-moment
ratio `E[S(n)²]/(n−2)` stay O(1) (density-1 SUPPLY) for inputs that differ
only in their lag-1 autocorrelation?

| input | centred lag-1 autocorr | prefix-mean E[S²]/(n−2) | verdict |
| --- | --- | --- | --- |
| primes | ≈ −0.04 | 0.97–1.12 | O(1) — density-1 holds |
| iid p=0.5 | ≈ 0 (±noise) | 0.80–1.11 | O(1) — density-1 holds |
| iid at p=0.569 | ≈ 0 | ~1.1 | O(1) |
| Thue–Morse | decaying, non-summing | ~4000–8400 | collapses |
| alternating 0101… | −1.0 | ~n | collapses (kernel-adjacent) |

**Key negative (the pricing).** iid random input — which has essentially *zero*
centred autocorrelation — passes at the uniform level just like the primes.
So **"bounded autocorrelation of h" is not the discriminating hypothesis**:
it is satisfied trivially by iid, which the fold already handles. The primes'
tiny anti-correlation is not what makes them good; iid is good with none.

What actually separates good (primes, iid) from bad (Thue–Morse, alternating)
is whether the *submask-window cross-correlation sum* in `E[S²]` dies — which
is the very object `E[S²]=O(n)` names. So the pricing confirms the run's
working hypothesis: the weakest input is a submask-window second-moment /
Walsh bound, not a bare autocorrelation of raw h.

## The quantitative boundary (new, the useful part)

To make the "weakest input" concrete, price how much *anti-correlation* a
balanced aperiodic input can carry before the fold's second moment breaks.
Two-state Markov chains of switching probability a have autocorrelation
`(1−2a)^k`; a finite autocorrelation sum requires a away from 0, and the
anti-correlated side (`a>1/2`, i.e. `1−2a<0`) is the regime relevant to the
primes (a ≈ 0.52).

Prefix-mean of `E[S(n)²]/(n−2)` over n ∈ [1024, 49152]:

```
a   (1−2a)   mean_ratio   max_ratio
0.50  0.000      0.94         8.5
0.70 −0.400      1.20         8.0
0.80 −0.600      1.39        16.0
0.84 −0.680      2.16        24.5
0.86 −0.720      2.85        45.7
0.87 −0.740      2.62        31.0
0.88 −0.760      3.85        72.7
0.90 −0.800      5.24        67.6
0.95 −0.900     38.98       173.7
```

**Empirical boundary:** `E[S²]=O(n)` (density-1 SUPPLY) survives all the way
to anti-correlation `1−2a ≈ −0.74` (switching prob a ≈ 0.87), and only grows
superlinearly beyond `|1−2a| ≳ 0.75`, collapsing outright near −0.9.
The primes sit at `1−2a ≈ −0.08` (a ≈ 0.52), giving a **~9× margin** before
the fold's balancing degrades.

## Honest status and what it bounds

- Exact measurements over the stated ranges (`n ≤ 49152`, iid/thue/markov new
  computations; primes from the guard-checked N=40000 JSON and fresh SOS).
- Conjectures, not proofs: the boundary (`|1−2a| ≲ 0.74` keeps E[S²]=O(n)) and
  the primes' margin are empirical, for two-state Markov inputs only.
- The *negative* (iid passes ⇒ bounded-autocorrelation of raw h is not the
  discriminating input) is robust: it does not rely on the exact boundary, only
  on iid reproducing the uniform second moment, which is exact
  (`E[S²]=n−2` for uniform h, verified by full enumeration).

## What this does and does not give

- **Does not** prove density-1 SUPPLY — `E[S²]=O(n)` for the real prime h
  remains open, and a finite autocorrelation sum on raw h is insufficient even
  as a hypothesis (iid has none and passes).
- **Does** sharpen the target: the weakest input is the submask-window
  second-moment / Walsh bound on h, and the primes have a large empirical
  margin (≈9×) to the collapse boundary, so a proof with any reasonable
  constant has slack. This is GOAL priority 2/4 territory: it prices the
  candidate rather than leaving it open-ended, and it records that the marketing
  "bounded autocorrelation" phrasing is not the right hypothesis to prove.
