# Switch-bit two-point structure (pattern_finder)

Computed by `code/pattern_finder/switch_autocorr_2pt.py`, sieve 1e8,
N = 1,000,000 consecutive prime gaps g_3..g_N. Exact integers.
Captured: `code/out/switch_autocorr_2pt.captured.txt`.

**Extended run (200x scale, this librarian cycle):** `code/pattern_finder/switch_autocorr_ext.py`,
sieve 4.4e9, N = 199,999,996 consecutive prime gaps, exact integers.
Captured: `code/out/switch_autocorr_ext.captured.txt`. This is the same
method at a 200x larger scale and confirms — it does not change — the
structural verdict below, so it is filed here as a banked claim rather than
reported as a new result.

## The quantity

`h[k] = 1 iff gap_k = p_{k+1} - p_k ≡ 2 (mod 4)` — the mod-4 switch bit.
This is the atomic bit whose Hamming weight `w(n)` feeds Granville's ν₂
transfer for Route B (`nu2 >= w/2` measured, `w >= c·n` the open leg). The
ballot walk `e(n) = 2w(n) - (n-2)` must stay `>= 0` for the supply bound.

## What is new

Prior claims measured the *density* `w/n ~ 0.56` and the *transfer ratio*
`nu2/w`, and refuted the Markov-mixing proof-strategy. None measured the
**autocorrelation spectrum** of the switch bit itself — the two-point
correlation structure that is exactly the LOS-2016 / ABGS-2011 open
hypothesis. This run measures it:

- **Near-whiteness.** Centered autocorrelations of the switch bit: lag 1
  `r = -0.0384`; lags 2..40 all `|r| < 0.0023`. The only persistent
  correlation is the small lag-1 anti-clustering.
- **Extended-scale confirmation (2e8 primes, N = 199,999,996 gaps).**
  lag-1 `r = -0.0261`, lag 2..40 all `|r| <= 0.0031` (max at lag 2);
  per-step drift `2E[h]-1 = +0.0964`; weight density `w/n = 0.548181`;
  ballot `e(n) = 2w-(n-2) >= 0` over ALL prefixes (global min e = 0);
  final `e = 19,272,272`. The falsifier tripped by neither scale: no
  lag>=2 `|r| > 0.005`. The lag-1 anti-clustering is scale-stable
  (|r| ∈ [0.026, 0.038] at both scales), drift positive at both.
- Joint consecutive counts over 999998 pairs: `#(1,1) = 307033`
  (vs `p² = 0.3165`, deficit), `#(0,0) = 181881` (vs `0.1913`, deficit),
  `#(1,0) = 255542`, `#(0,1) = 255541`.
- **Exact telescoping identity:** `#(1,0) - #(0,1) = 1` over any window —
  for a 2-state walk the off-diagonal counts differ by at most 1 (exact here,
  checked).
- **Per-step drift** of the ballot walk `e`: `2E[h] - 1 = +0.1252`.

## Interpretation (conjecture, not proof)

The e-walk that must stay `>= 0` is a positive-drift (+0.125) walk whose
steps are, to the measured scales, near-uncorrelated. Then a variance/LLN
argument would make it stay positive once past its small-n dips (e=0 at
n=4,6,8; min e/n → 0.0986). The two-point structure is consistent with the LOS bias living on
consecutive pairs only (lag-1 term), with no higher-lag correlation. All of this is **numerical** — 
near-whiteness is conjectured for the limit, not proved; the ABGS-2011 §9
result says the limit need not even exist unconditionally.

## Status

Verified exactly over the 999,998 terms supplied, and re-confirmed at 200x
scale over 199,999,996 terms (capture `switch_autocorr_ext.captured.txt`).
Sequence tools:
no low-order linear recurrence / polynomial on the ballot (already recorded in
`pattern_finder_switch_ballot.md`). This adds the autocorrelation
measurement to that record. Falsifier: any lag>=2 |r| above ~0.005 at
larger scale, or a drift that fails to stay positive. Untripped at both
scales.

```claim
id: switch-bit-two-point-autocorrelation-near-white
statement: The mod-4 switch bit h[k] = [gap_k ≡ 2 (mod 4)] over consecutive primes is near-white: its centered autocorrelation has a small negative lag-1 term only, and |r| <= 0.0031 for all lags 2..40. Verified exactly at two scales: (a) 1e8 sieve, N=1,000,000 gaps: r(lag1)=−0.0384, all lags 2..40 |r|<0.0023, drift 2E[h]−1=+0.1252, e(n)>=0 all prefixes; (b) 4.4e9 sieve, N=199,999,996 gaps: r(lag1)=−0.0261, all lags 2..40 |r|<=0.0031, drift +0.0964, weight density w/n=0.548181, ballot e(n)>=0 over ALL prefixes (global min e=0), final e=19,272,272. The only persistent correlation is the small lag-1 anti-clustering (|r| in [0.026,0.038] at both scales).
hypotheses: primes; switch bit h[k] = 1 iff p_{k+1} - p_k ≡ 2 (mod 4); centered autocorrelation over consecutive blocks; exact integer arithmetic (ballot/drift).
holds-here: yes
status: checked (verified-numerically at two scales, exact counts); near-whiteness of the LIMIT is conjectured, not proved — ABGS-2011 §9 says the limit need not even exist unconditionally.
bearing: the ballot walk e(n)=2w(n)−(n−2) that Route B's supply bound needs to stay >=0 is a positive-drift (+0.096..+0.125), near-uncorrelated walk whose steps are (to the measured scales) two-point-correlated only at lag 1 — consistent with the LOS-2016/ABGS-2011 speculation that the bias lives on consecutive pairs only. Numerical evidence toward G-supply (nu2 >= c·n), not a proof; the supply bound remains conditional at HL/LOS two-point level.
falsifier: any lag>=2 |r| > ~0.005 at a larger scale, or a drift that fails to stay positive; untripped at both 1e6 and 2e8 scales.
anchor: code/out/switch_autocorr_ext.captured.txt, code/out/switch_autocorr_2pt.captured.txt
```

```claim
id: switch-bit-two-point-scale-stable
statement: Pushing the switch-bit two-point structure from 1e6 to 2e8 consecutive prime gaps (200x) leaves the verdict unchanged: lag-1 anticorrelation and positive drift persist, and neither the lag>=2 near-whiteness nor the positivity of the ballot walk is disturbed. The extended run therefore confirms rather than revises the structural conclusion; it is the same method at a larger size and settles nothing the smaller run had open.
hypotheses: primes to 4.4e9 (N=199,999,996 switch bits vs 999,998 at 1e8); identical autocorrelation and ballot statistics.
holds-here: yes
status: checked (verified-numerically at two scales); explicitly NOT a new result — a scale extension that leaves the standing consensus and the named-open supply hypothesis unchanged.
bearing: prevents the extended capture from being reported as a fresh breakthrough; because the falsifier (lag>=2 |r|>0.005) was already untripped at 1e6 and ABGS-2011 §9 says the limit may not exist at all, no scale extension can settle it — the structural question (bounding the lag-1 term at HL/LOS two-point level) is where the work lies, not the sieve size.
anchor: code/out/switch_autocorr_ext.captured.txt
```
