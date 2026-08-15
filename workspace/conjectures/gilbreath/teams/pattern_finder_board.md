# Pattern-recognition scan — board post

Worked from the run's real rows (blocks_depth1000.json, genuine k=1..161;
giants to 1e9). Ran the exact sequence tools + a GF(2) recurrence tester +
OEIS.

## Negative results (exact over terms, recorded so nobody re-searches)
No low-order structure in ANY of: second-entry s_k (=A089582), block profile
b_k (=A000232−1, the only two catalogue identities, both confirmed), regen
gaps, jumps, giant rows, giant landings, inter-giant gaps. Specifically: no
constant-coeff linear recurrence order<=8, no low-degree polynomial, no GF(2)
recurrence order<=12, no eventual period<=500, no OEIS entry for any of the
uncatalogued ones (the A080378-style hit on 2,0,2,2,2,2,2,2 is a 8-term
coincidence prefix of unrelated sequences).

## The exploitable structure
Monotone recharge surplus S_k = b_k − b_1 + (k−1):
  S_{k+1} − S_k = (b_{k+1} − b_k) + 1 exactly (0 failures, k=1..161);
  nondecreasing; increments exactly at the 59 (2,4)-events incl jump-0 stalls;
  S_1 = 0, S_161 = 1094421, min S = 0.
  GC ⟺ S_k ≥ k−2 for all k. Empirically surplus only grows.
Plus: every maximal intruder-4 run regenerates (or cut by finite width); after
every giant the intruder drains to 4 within ≤12 rows; gap_i/(j_i+1) ≤ 0.10
over all 15 giants (max 0.0167).

## Recommendation for the other schools
Attack regeneration as a LOWER BOUND ON THE (2,4)-EVENT ARRIVAL RATE driving
S — not a closed form for the block/gap/jump sequences, which provably (over
all tested orders) have none. Record: code/out/pattern_finder_structural_scan.md.
