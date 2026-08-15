# Switch-bit two-point structure (pattern_finder)

Computed by `code/pattern_finder/switch_autocorr_2pt.py`, sieve 1e8,
N = 1,000,000 consecutive prime gaps g_3..g_N. Exact integers.
Captured: `code/out/switch_autocorr_2pt.captured.txt`.

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

Verified exactly over the 999,998 terms supplied. Sequence tools:
no low-order linear recurrence / polynomial on the ballot (already recorded in
`pattern_finder_switch_ballot.md`). This adds the autocorrelation
measurement to that record. Falsifier: any lag>=2 |r| above ~0.005 at
larger scale, or a drift that fails to stay positive.
