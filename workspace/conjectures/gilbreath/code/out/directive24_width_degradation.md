# Width-degradation caveat — every measurement past k* = 162 is a lower bound

`code/directive24/compute_width_degradation_and_growth.py` (run captured as
`code/out/directive24_compute.captured.txt`, independently verified by
`code/out/directive24_verify.captured.txt`).

## Setup

- Data: `code/out/blocks_depth1000.json`, `b[r-1]` = leading `{0,2}` block
  length of row r (1-based), r = 1..1000. W = 1,270,607 primes (sieve 2e7).
- Row r has W − r columns (0-based 0..W−r−1). The block occupies positions
  1..b[r−1], so the free space past the block front is

  ```
  flooring(r) = (W − r − 1) − b[r−1]
  ```

  All arithmetic exact integers. Convention cross-checked: flooring(35) =
  1,268,392 and flooring(162) = 0 reproduce CONTEXT.md; landing-row floors
  (W − i − 2) − b[i] reproduce all 13 values of the characterization table
  `bigjump_characterization.captured.txt` exactly.

## Result

**k\* = 162**: the first row r with `flooring(r) < 1000` (J_min = 1000).
The degradation is NOT gradual — it is a drop from 176,182 (row 161) to
**exactly 0** (row 162), because the last genuine event (i=161, the capped
artifact) glues the block to the finite right edge: b[161] = 1,270,444 =
W − 162 − 1. From row 162 on the "block" is the whole remaining finite row
and retracts one column per row; **flooring(r) = 0 for every r = 162..1000**
(verified over all 839 rows). The bigjump table's "floor runs 1,268,392 →
0" is the floor 1,268,392 at the landing row 35 of the first genuine giant,
then one-column steps from genuinely huge spaces down to the i=161 cap.

## Implications (mark every measurement)

- **All block-length / jump / event measurements at rows r ≥ 162 are LOWER
  BOUNDS**: the finite width W truncates any jump that would have carried the
  block past the row's right edge. In particular the recorded jump at i=161
  is `≥ 176,181`, never exact (CONTEXT claim `bigjump-cap-characterization-1000`).
- **The 12 genuine giants all sit far above the threshold.** Event-row
  flooring for i=34..146 runs 1,269,707 → 536,885 (minimum 176,182 at the
  capped i=161; min among the genuine 12 is 536,885 at i=146, > 1000 by a
  factor of 536). **None of the genuine giants is width-limited** — the
  `genuine` verdicts of the characterization are re-confirmed at the flooring
  level.
- **First row past each giant with flooring < 1000 = row 162 for all 13** —
  there is no per-giant degradation: every giant is followed by ≥ 15 rows
  (i=146) of flooring ≥ 176,000 before the global cap.
- **Empirical complexity of the caveat:** the data is NOT continuously
  degraded; it is fully genuine through row 161 (flooring ≥ 176,182 > 1000)
  and fully capped from row 162 (flooring = 0). Any claim using rows ≥ 162
  from the depth-1000 record must state it is a lower bound; the live
  regime under J_min = 1000 is **exactly rows 1..161**.

## Numbers (exact)

| event row i | b_i | b_{i+1} | event-row flooring | landing-row flooring | genuine |
| --- | --- | --- | --- | --- | --- |
| 34  | 865 | 2,179 | 1,269,707 | 1,268,392 | yes |
| 56  | 4,203 | 5,942 | 1,266,347 | 1,264,607 | yes |
| 64  | 5,939 | 23,265 | 1,264,603 | 1,247,276 | yes |
| 68  | 23,262 | 31,499 | 1,247,276 | 1,239,038 | yes |
| 94  | 31,532 | 92,620 | 1,238,980 | 1,177,891 | yes |
| 96  | 92,619 | 103,973 | 1,177,891 | 1,166,536 | yes |
| 110 | 103,960 | 141,706 | 1,166,536 | 1,128,789 | yes |
| 112 | 141,706 | 271,629 | 1,128,788 | 998,864 | yes |
| 126 | 271,620 | 325,090 | 998,860 | 945,389 | yes |
| 130 | 325,096 | 515,906 | 945,380 | 754,569 | yes |
| 134 | 515,907 | 733,564 | 754,565 | 536,907 | yes |
| 146 | 733,575 | 1,094,273 | 536,885 | 176,186 | yes |
| 161 | 1,094,263 | 1,270,444 | 176,182 | 0 | **no (capped)** |

k\* = 162; rows with flooring < 1000: 162..1000 (839 rows, all with
flooring = 0). Landing-row floors match
`code/out/bigjump_characterization.captured.txt` exactly (13/13).