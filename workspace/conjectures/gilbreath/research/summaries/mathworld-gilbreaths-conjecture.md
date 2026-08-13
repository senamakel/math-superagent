# MathWorld — Gilbreath's Conjecture (Weisstein)

**Full text:** the summary file IS the complete page (MathWorld HTML; a separate `.full.md` was not created because the fetch stored the text here; a re-download is refused as a duplicate).
**Source URL:** https://mathworld.wolfram.com/GilbreathsConjecture.html

## What it establishes

Encyclopedic tier. A short entry asserting:

- **Definition:** `d_n = p_{n+1} − p_n`; `d_n^k` the iterated absolute
  difference; Gilbreath claimed `d_1^k = 1` for all k (Guy 1994).
- **Verification:** "In 1959, the claim was verified for k<63419. In 1993,
  Odlyzko extended the claim to all primes up to π(10^13)" — consistent with
  K–R 1959 and Odlyzko 1993 in the library (the "63419" digit is the same
  minor rounding as elsewhere; K–R's own count is 63,419).
- **Equivalent triangle form:** the array
  `2,3,5,7,11,... / 1,2,2,4,2,... / 1,0,2,2,... / ...` always has leading term
  1 after the first row (OEIS A036262) — exactly the run's `A_1..A_5` rows.
- **Block-length sequence:** number of terms before the first > 2 in the n-th
  row given by 3, 8, 14, 14, 25, 23, 22, 25, ... (OEIS A000232). Note the
  **6th term here reads 23 where A000232's b-file reads 24** — MathWorld's list
  is truncated/miscopied at that point; the OEIS b-file and Debono's data are
  the authoritative values, and the run's block profile `A000232−1` matches the
  b-file, not this display.
- References: Caldwell, Debono, Gardner 1980, Guy §A10, K–R 1959, Odlyzko 1993,
  Proth 1878, OEIS A000232/A036262.

## Hypotheses / bearing

Corroborates the statement, the 1959/1993 verification bounds, and the
A036262/A000232 connection — all already sourced in the library. The only
deviations to be aware of: the A000232 row misprint above, and the mildly
rounded verification counts. No theorem content; nothing new to support or
refute. **No help beyond corroboration.**

## Source status

MathWorld (Wolfram), encyclopedic tier; cites the primaries the library already
holds.