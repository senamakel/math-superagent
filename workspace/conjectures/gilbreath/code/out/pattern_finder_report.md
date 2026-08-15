# Pattern-finder report: exact regularities in the Gilbreath row data

Data read: `code/out/blocks_depth1000.json` (sieve 2e7, 1270607 primes, D=1000,
b_k = leading {0,2} block length, s = second entries) and
`code/out/pattern_finder_outputs/giants_1e9.json` (sieve 1e9, 50,847,534 primes,
D=400, 16 giants with jumps/landing blocks/pre-jump blocks/gaps).

All statements below are **exact over the terms supplied** (checked by program,
output reproduced). None is a proof that the pattern continues; each is labelled
conjecture / verified-numerically as appropriate.

## 1. Recharge identity — EXACT, re-verified here (already proved by the run)

With events = transitions where `b_{k+1} >= b_k` (the (2,4) events; 60 of them
in 999 transitions = 43 strict-growth + 17 zero-jump stalls), and `j_i =
b_{i+1} - b_i`:

    b_k = b_1 + Σ_{events i < k} (j_i + 1) − (k−1)

holds with **zero failures over all 1000 rows**. This is the proved deposit law;
re-verification here confirms the indexing (60 events) and the constant 1.

## 2. Block length never falls below its value at k=1 — EXACT over depth 1000

`min_k b_k = 2 = b_1` (achieved only at k=1). The recharge surplus
`T_k = b_k − b_1 = Σ(j_i+1) − (k−1)` has min 0 over 1000 rows. So in these
rows the block is never consumed below its starting length — the surplus is
monotone nondecreasing and strictly increases exactly at the 60 events.
(Consistent with `surplus-renewal-structure-1000` in CONTEXT; re-verified.)

## 3. Inter-event gap structure — verified-numerically, NO procedure found

59 gaps between the 60 events: max 14, mean ~2.8, median 1. Events cluster
(runs test z=−3.94 reported). `find_linear_recurrence` finds no constant-
coefficient recurrence of order ≤10; `analyze_sequence` finds no low-degree
polynomial. The gap sequence is irregular.

## 4. The ratio bound gap/(j+1) — the strongest empirical regularity, verified

Over the 14 genuine inter-giant gaps at 1e9: `gap_i ≤ j_i+1` holds always, and
`gap_i/(j_i+1) ≤ 0.0126` (max 22/1739). Over all positive-jump events at depth
1000, `gap/j ≤ 0.13`. Crucially, this survives two width doublings (6e8 → 1e9):
**max gap stays 64 while the pre-jump block grows from 865 to 23,163,290
(a factor 27,000).** So the empirical claim is not merely "gap ≤ jump" (which
is trivially true here since jumps ≫ gaps): it is that inter-giant gaps remain
small (≤64) while block length grows geometrically. This is the quantity the
board's regeneration argument needs as a bound; it is verified-numerically, not
proved. The growth law itself (log-b vs row, R²=0.946, ~×2 per 14 rows) is a
fit over 15 giants and is NOT a law (claim `directive25-gap-trend-and-
reconciliation` already flags it unsettled).

## 5. Event parity — weak signal, not a law

60 events at depth 1000: 36 even-row / 24 odd-row (two-sided p=0.077). Of 15
genuine giants at 1e9, 13 have even 0-based pre-jump row (only 161,247 odd)
— base-rate p=0.0052 reported. A real directional bias but small n; do not
promote to a law without more data.

## 6. OEIS misses — record, do not re-search

- Block-profile prefix `2,7,13,13,24,23,22,21,24,58,97,96`: **no OEIS match.**
- Second-entry sequence (100 terms): no order-≤10 constant-coefficient
  recurrence.
- Confirmed shift `block_profile(k) = A000232(k) − 1` already recorded.

## What this suggests is most likely to yield a derivation

The open quantity is the **event rate / jump-mass lower bound** (CONTEXT Gaps,
`surplus-renewal-structure`). The strongest empirical signal available is #4:
inter-giant gaps stay ≤ 64 while the block grows by thousands of times. If this
"gaps stay bounded while b → ∞" were proved (under stated hypotheses), the
recharge identity would give b_k → ∞ and the conjecture would follow for that
class. No mechanism for it is known (CONTEXT: `gap-bounds-cannot-force-block-
growth` shows no gap-size theorem forces it; Eppstein kills uniform bounded-gap
classes). The right framing remains non-concentration of the prime gaps — but
the board should know that the *empirical* gap-vs-scale separation is
overwhelming (64 at b=23M), even though no proof exists.
