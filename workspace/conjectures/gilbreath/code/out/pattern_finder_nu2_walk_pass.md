# Pattern-finder pass: nu2 walk increments and remaining dead-ends

Status: all exact over the supplied terms; none is a proof beyond them.

## 1. NEW: nu2 is not a bounded-step walk — supply-bound route closed

The Route B supply quantity `nu2(q_n)` (= #2s in the maximal `{0,2}` suffix
of the prime right diagonal, the entire open content of Route B) has, over the
exact series `code/out/nu2_dense.txt` (n=1..30000, sieve 1e6):

- single-step increments `|nu2(n+1)-nu2(n)|` reaching max **468**,
  6571 steps > 100, 968 steps > 200, 90 steps > 300 in magnitude;
- yet the running deviation `|2*nu2(n)-n|` never exceeds **639**
  (matches the previously recorded max |dev| = 639 at n=27625).

Ratio max_inc/max_dev = 0.732. **Consequence:** the concentration of `nu2`
around `n/2` is NOT produced by small steps, so no bounded-difference,
martingale, or LIL-style argument on nu2's own increments can deliver the
`nu2 = n/2 + O(n^{1/2+eps})` bound that would prove G-supply (`nu2 >= c*n`).
The cancellation must come from correlated XOR-fold structure across large
deltas (the two-point mod-4 switch bit), not from step-size bounds. This is
distinct from the already-refuted anticlustering/Markov-mixing route (which
attacked the switch bit, not nu2 itself). Exact over the supplied 30000 terms;
a conjecture for the full sequence, and a negative (dead-end-marking) finding.

Computed by `code/pattern_finder/nu2_walk_increments.py`; full distribution in
`code/out/nu2_walk_increments.captured.txt`.

## 2. OEIS miss on giant gaps (confirmed, recorded)

The inter-giant gaps [22,8,4,26,2,14,2,14,4,4,12,15,13,64] have NO OEIS entry.
Uncatalogued — no lookup closed form; the gap growth is problem-internal.

## 3. S-surplus monotonicity — re-confirmed exactly

`S_k = b_k - b_1 + (k-1)` over the genuine regime k=1..161:
nondecreasing, `S_1=0`, `S_161=1094421`, exactly 59 increases,
`Delta_k = S_{k+1}-S_k = (b_{k+1}-b_k)+1` verified at 160/160 transitions.
Matches the earlier `pattern-finder-no-loworder-plus-surplus` claim exactly.

## 4. Negative results re-confirmed (no re-derivation)

Second-entry, block-profile, regen-gap, jump, giant-row, giant-landing,
inter-giant-gap sequences: no constant-coefficient linear recurrence
(order <= 8), no low-degree polynomial, no GF(2) recurrence (order <= 12),
no eventual period. OEIS confirms only `s_k = A089582` and `b_k = A000232-1`.

## What is exploitable

The monotone recharge surplus S (proved form of the recharge identity; the
conjecture is exactly `S_k >= k-2` never returning to zero). The most likely
derivation lever remains a lower bound on the (2,4)-event arrival rate, NOT
any low-order arithmetic of nu2/block/gap/jump — those are all empty at low
order, and the supply side nu2 additionally has no bounded-step concentration.
