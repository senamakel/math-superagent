# The mod-4 switch-walk ballot — the exploitable structure on the supply side

## What world this problem is native to

The whole remaining open content of the primary route (Granville Lemma 5.4 →
Theorem 5.5, `granville-nu2-reduction`) is the **supply bound** `ν₂(q_n) ≥ c·n`.
The pattern-finder scan of the computed data shows this is NOT a statement
about the absolute-difference dynamics at all — it is a statement about the
**distribution of consecutive prime gaps modulo 4**. The object the problem is
really about, once the block/erosion/regeneration machinery is stripped away,
is the two-point statistic `bit_n = [p_{n+1} ≢ p_n (mod 4)]`, i.e. the
consecutive-prime **mod-4 class switch**. That is a problem native to
analytic number theory (Chebyshev-bias / Lemke-Oliver-Soundararajan machinery),
not to combinatorics.

## The ballot, stated exactly (which side it is on)

Define, over the gaps `g_3..g_n` (so the window has `n−2` gaps):

- `w(n)` = number of gaps `≡ 2 (mod 4)` (i.e. the number of mod-4 switches),
- `e(n) = 2·w(n) − (n−2)` = (# switches) − (# non-switches) = the **switch-walk
  excess**.

**Ballot (conjecture, verified-numerically):** `e(n) ≥ 0` for every `n` — in
every prefix at least half of the first `n−2` prime gaps are `≡ 2 (mod 4)`; the
walk never dips below 0. This is straightforwardly ONE-SIDED, in contrast to
the `ν₂` fluctuation `2ν₂−n`, which oscillates (dev negative on 55.3% of n) —
that oscillation is about a different, triangle-dependent statistic, and the
switch-walk ballot avoids it.

## What the tools established (all exact over computed terms)

Over `n ∈ [2, 17983]` (and streamed to 5e7 / 1e8): `e(n) ≥ 0` with **zero
violations**; steps are exactly `±1`; `e` returns to 0 only at `n ∈ {4,6,8}`
(last), to 1 last at `n=9`, and never below after. `e(n) = 2R(n) − n` exactly,
where `R(n)` = number of residue-runs of `p_3..p_{n+1}`. `analyze_sequence`
and `find_linear_recurrence` (order ≤ 10) find no polynomial, no constant-
coefficient recurrence; the record-gap structure is irregular. **OEIS: miss**
(`1,0,1,0,1,0,1,2,3,2,3,2,3,4,5,6` uncatalogued) — nobody should re-search it.

Chebyshev-bias reformulation: with `u_k = +1` if `p_k ≡ 1 (mod 4)`, `−1` if
`p_k ≡ 3 (mod 4)`, the ballot is `Σ_{k=2..n} u_k·u_{k+1} ≤ 0` for every
prefix — a negative lag-1 autocorrelation of the residue-sign sequence, in
every prefix.

## The transfer: how the ballot closes Route B (the supply side)

This was verified independently here under the run's exact convention
(`/tmp/e_seq` recompute + dense `nu2_dense.txt`):

- **leg (a)** `ν₂(n) ≥ w(n)/2` for `n ∈ [17,30000]`, **0 violations**,
  min ratio exactly **0.5** at `n=44` (touching, not loose — a tight contact).
- **leg (b)** `w(n) ≥ (n−2)/2` (the ballot) for `n ∈ [2,30000]`, **0
  violations**.
- **composed** `ν₂(n) ≥ (n−2)/4` for `n ≥ 17`, **0 violations**; min
  `ν₂/n^0.525 = 1.542` at `n=23`, well above the theorem's threshold `0.525`.

So a proof of the ballot — or even any positive-density lower bound on the
mod-4 switch count — closes Route B's supply side, converting the conditional
theorem into an unconditional one. This is why the ballot is the most likely
regularity to yield a derivation.

## The obstruction (why it is open, and honest)

Sequences tools return no closed form, and `oeis_lookup` is a miss: the
structure is not arithmetic at low order. The direct literature obstruction is
ABGS 2011 §9 (claim `abgs-2011-s9-mod4-switch-limit-open`): whether
`N(a,d,m,x)/π(x)` tends to any limit is open, so **no unconditional bound** on
the switch count exists. The ballot is therefore a genuine conjecture, not
something the data + tools can promote to a claim on this run's evidence.

## What would falsify it

The first `n` with `e(n) < 0`. **None found over 17983 dense terms and to 5e7
by streaming** — but a positive drift near `0.11·n` (marginal density ≈ 0.555)
makes a late dip unlikely yet not ruled out. This is the concrete falsifier to
compute toward if the run wants to push the ballot's range: `e` stays in
`[5,∞)` for `n ≥ 17`, so a violation requires an unusually long negative run
that contradicts the observed drift.

## Files

- This scan: `/tmp/e_seq.json` (e(n), n=3..17983), recompute script inline.
- Prior artifacts: `code/pattern_finder/switch_walk_ballot.md`,
  `switch_walk_extend.py`, `switch_majority_stream.py`, `switch_walk_linear.py`,
  captures `code/out/mod4_ballot_autocorr.captured.txt` (cross-checks to 1e6)
  and `switch_majority_stream_5e7.captured.txt` (to 5e7).
- Dense ν₂: `code/out/nu2_dense.txt` (n=1..30000).
