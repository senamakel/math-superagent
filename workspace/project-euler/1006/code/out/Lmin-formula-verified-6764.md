# Verification: Lmin(k) = k + NextFib(k) - 1 for k = 1..6764

Computed on 2025-08-17 by three independent programs, all exact integer
arithmetic, all on a prefix of the infinite Fibonacci word of length 28657
(>= 24000 required):

1. `code/pattern_hunt/verify_lmin_formula_f20.py` — bit-mask factor
   extraction, helpers imported from `code/lib/fibword.py`, full range
   k = 1..6764.
   Output: `prefix length 28657` ; `mismatches ... : 0` ;
   `first failing k: none`.
2. `code/pattern_hunt/verify_lmin_formula_indep.py` — plain Python substring
   route (no bit-mask), 49 sampled k including every Fibonacci boundary
   through 6764.
   Output: `0 mismatches` ; agrees with the bit-mask run.
3. `code/pattern_hunt/push_lmin_k6764.py` — third copy, standalone bit-mask
   implementation, full range k = 1..6764.
   Output: `mismatches k=1..6764: 0` ; `all ok: True`.

## Requested values

| k | Lmin(k) (computed) | k + NextFib(k) - 1 |
| --- | --- | --- |
| 1596 | 3192 | 3192 |
| 1597 | 4180 | 4180 |
| 2583 | 5166 | 5166 |
| 2584 | 6764 | 6764 |
| 4180 | 8360 | 8360 |
| 4181 | 10945 | 10945 |
| 6764 | 13528 | 13528 |

All equal. This extends the earlier `verify_lmin_formula.py` pass over
k = 1..2583 to the full block k <= 6764 (F_19 = 4181 <= k < F_20 = 6765 has
NextFib = 6765 throughout, so Lmin(k) = k + 6764 in that block; the largest
computed Lmin is 13528 at k = 6764, comfortably below the 28657-char prefix).

Prefix sufficiency argument: in every block F_m <= k < F_{m+1},
Lmin = k + F_{m+1} - 1 < 2*F_{m+1} - 1 <= 2*6765 - 1 = 13529 (the last block
in range), and the prefix of 28657 chars contains all of these; an early-stop
scan cannot falsely pass, it can only return None on an insufficient prefix
(the recorded bug at 4181 chars / k=2583), and no run saw a None.