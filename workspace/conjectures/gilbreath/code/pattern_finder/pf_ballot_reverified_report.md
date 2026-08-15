# Pattern-finder report — balled regularity & the nu2 autocorrelation puzzle

## Bottom line

The one clean structural regularity of the whole investigation is the
**never-nonnegative mod-4 switch-majority ballot** `e(n)`, and this pass
confirms it *fresh* (independent sieve to 10^7 primes, not `lib.gilbreath`),
plus resolves what the `nu2_fluct_autocorr` capture *appeared* to show as an
anomaly. **No closed form / no linear recurrence exists in any supply-side
sequence** — the exploitable content is purely qualitative.

## 1. The ballot, re-verified from scratch (CONJECTURE, verified-numerically)

Definitions (`p_k` = k-th prime, `p_1=2`):
- `bit_k = 1` iff `p_{k+1} ≢ p_k (mod 4)`, i.e. iff prime gap `≡ 2 (mod 4)`
- `w(n) = Σ_{k∈[2,n-1]} bit_k` (Hamming weight of the {0,2}-tail ancestor window)
- `e(n) = (#switches) − (#nonswitches) = 2·w(n) − (n−2)`

Fresh run (`code/out/pf_ballot_fresh.captured.txt`, sieve to ~1.99e8, 10^7 primes):
```
e(n) >= 0 for all n in [2, 10^7]: YES, 0 violations
zeros of e ONLY at n in {2,4,6,8}; global min e = 1 elsewhere
final e(10^7) = 1,102,993 = 2·5,551,496 − 9,999,999   (identity exact)
e/N -> 0.11030
tail minima: n>=100:25, n>=1000:236, n>=10^4:1723, n>=10^5:14719, n>=10^6:125146
```
The identity `e(n)=2w(n)-(n-2)` was cross-checked termwise (exact).

**Why it matters.** With the two measured transfer legs (a) `ν₂ ≥ w/2` (holds on
every sample, min 0.5 contact at n=44) and (b) `w ≥ (n−2)/2` (exactly the
ballot), the ballot composes to the linear supply bound `ν₂ ≥ (n−2)/4`, and
`(n−2)/4 > n^0.525` from n=23 on. So **G-supply — the only open step of the
primary Route B — reduces to proving `e(n) ≥ 0`**, a two-point
(Hardy–Littlewood / Lemke-Oliver–Soundararajan level) statistic, named open in
the literature (`abgs-2011-s9-mod4-switch-limit-open`).

**Falsifier (stated, unhit to 10^7):** any n with more non-switch than switch
consecutive pairs among the first n.

**Sequence tools (negatives, exact over supplied terms):** `analyze_sequence`
on e and on `F=ν₂−⌊n/2⌋` finds no polynomial; `find_linear_recurrence`
(order ≤ 8) finds **no** constant-coefficient recurrence for e, F, or ν₂. These
are prime-number-theoretic — no arithmetic lever.

## 2. The nu2 autocorrelation "anomaly" is resolved

`code/out/nu2_fluct_autocorr.captured.txt` reports AC of
`I(n)=2ν₂(n+1)−2ν₂(n)−1` at lag 1 as **−0.503**. Taken naively this looks like
significant anti-persistence. Synthetic model (`code/out/pf_ac_models.captured.txt`):
- Model A (D=random walk): AC(I) ~ 0
- Model B (I=white): AC(I) ~ 0
- **Model C (I = first difference of white noise): AC(I) = −0.5003** ✓

So AC=−0.5 on a first-difference sequence is the *exact* signature of
`I(n)=ε(n+1)−ε(n)`, i.e. it is the standard −0.5 of the second-difference of a
random walk — **not new exploitable structure, and not white-noise drift either**.
It is the precise fingerprint of the documented Littlewood-style oscillation of
`D(n)=2ν₂−n` (max |D|=639 at n=27625, sign of D negative ~55% of the time).

**Conclusion:** there is no supply-side random-walk drift to harvest; the
oscillation is mean-reverting (which in fact *helps* the ballot stay ≥ 0 at
large scale but supplies no nonnegativity proof). Only the qualitative
never-negative ballot is exploitable.

## Status legend
- Ballot `e(n) ≥ 0`: **verified-numerically** to 10^7 (this pass) and 10^8
  (run's larger captures); **not proved**; named open in the literature.
- `ν₂ ≥ w/2`, `w ≥ (n−2)/2`, `ν₂ ≥ (n−2)/4`: verified-numerically; each a
  separate theorem needing proof.
- No closed form / recurrence anywhere in the supply sequences: exact negative
  on supplied terms (conjecture of non-existence, not a proof of it).
