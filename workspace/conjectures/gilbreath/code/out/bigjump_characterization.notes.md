# The giant regeneration jumps are genuine prime-renewal dynamics — 12 of 13, depth 1000

**Question (Directive 23, TASKS item 1).** The recharge surplus
`S_1000 = 1,270,603` is carried almost entirely by a handful of giant jumps
(j > 1000): the largest are i=134 (j=217,657), i=146 (j=360,698), i=161
(j=176,181). Before building the "gap between consecutive large jumps" bound,
the thread must know whether these giants are genuine dynamics of the
infinite triangle or artifacts of the finite sieve width (the run is done on
1,270,607 primes, so row r has only W−r columns).

**Method.** Exact integer arithmetic, three-way verified:

1. The 13 events with j > 1000 were taken from
   `code/out/surplus_renewal_table.captured.txt`, and each jump recomputed
   from the `b` array of `code/out/blocks_depth1000.json` (depth 1000, sieve
   to 2·10⁷, W = 1,270,607 primes): all 13 match.
2. Event detection from the `b` array across all 999 transitions gives
   exactly the 60 known `(2,4)`-events; every event row's intruder is 4;
   every no-intruder row erodes to exactly b−1 (0 failures).
3. **Independent recompute**: a fresh sieve to 2·10⁷ (1,270,607 primes
   regenerated) and `rows_generator`/`block_profile` from `lib.gilbreath.py`
   reproduced every block length at rows 1–165, and for each of the 13 event
   rows the fresh row confirmed the `(edge, intruder)` pair is exactly
   `(2, 4)` (the JSON only stores the second entry, not the edge).

**Cap test.** Row *r* (1-based; A_0 = the primes) has `W − r` columns, of
which one holds the leading 1, so the block (positions 1..b) can reach at
most `max_block = W − r − 1`. Event i lands on row i+1, so
`max_block = W − (i+1) − 1 = W − i − 2`. Define
`floor_distance = max_block − b_{i+1}`:

- `floor_distance ≥ 1` ⟹ the `{0,2}` run ends strictly inside the row and
  the row has a first non-`{0,2}` entry past it — the recorded jump is the
  **true infinite jump**, complete at this depth. Verdict **GENUINE**.
- `floor_distance = 0` ⟹ the block runs to the finite row's right edge;
  the recorded jump is a **lower bound** on the true jump. Verdict
  **CAPPED-ARTIFACT** (equivalently: landing row's intruder is null).

## Verdict table

Event i = 1-based row of the `(2,4)`-event; row i+1 is the landing row.
`cols` = columns of row i+1; `landIntr` = first entry past the block in the
landing row (None ⟺ capped).

```
   i        j       b_i   b_{i+1} edge intr landIntr      cols    maxblk     floor  verdict
  34    1,314       865     2,179    2    4        4 1,270,572 1,270,571 1,268,392  GENUINE
  56    1,739     4,203     5,942    2    4        4 1,270,550 1,270,549 1,264,607  GENUINE
  64   17,326     5,939    23,265    2    4        6 1,270,542 1,270,541 1,247,276  GENUINE
  68    8,237    23,262    31,499    2    4        6 1,270,538 1,270,537 1,239,038  GENUINE
  94   61,088    31,532    92,620    2    4        4 1,270,512 1,270,511 1,177,891  GENUINE
  96   11,354    92,619   103,973    2    4       14 1,270,510 1,270,509 1,166,536  GENUINE
 110   37,746   103,960   141,706    2    4        4 1,270,496 1,270,495 1,128,789  GENUINE
 112  129,923   141,706   271,629    2    4       14 1,270,494 1,270,493   998,864  GENUINE
 126   53,470   271,620   325,090    2    4        4 1,270,480 1,270,479   945,389  GENUINE
 130  190,810   325,096   515,906    2    4        4 1,270,476 1,270,475   754,569  GENUINE
 134  217,657   515,907   733,564    2    4        4 1,270,472 1,270,471   536,907  GENUINE
 146  360,698   733,575 1,094,273    2    4       12 1,270,460 1,270,459   176,186  GENUINE
 161  176,181 1,094,263 1,270,444    2    4     None 1,270,445 1,270,444         0  CAPPED-ARTIFACT
```

## Result

- **12 of 13 giant jumps (j > 1000) are GENUINE**; the finite width caps only
  **i=161**. The heavy tail (j > 10⁴) is 9 genuine of 10 — including the two
  largest measured jumps, i=146 (j=360,698, landing 176,186 columns short of
  the finite edge — the smallest floor among the genuine set, still far from
  truncation) and i=134 (j=217,657, floor 536,907).
- **The one capped event's recorded jump is a lower bound**: i=161 lands at
  b₁₆₂ = 1,270,444 = max_block exactly (the JSON intruder list turns null at
  row 162); the true infinite jump is ≥ 176,181. This is the known
  width-exhaustion artifact, and every row k ≥ 162 of the record is the
  artifact tail (block retracting one column per row by construction of the
  finite difference triangle) — already flagged in the regeneration analysis.
- **The heavy tail is NOT a width effect.** Genuine giants carry
  1,091,362 of the 1,270,603 surplus (86.1% of the total; the 13 giants
  together carry 99.76% of S_1000, so surplus is tail-dominated, and of that
  tail 86.1% is complete genuine measurement). A width artifact strong
  enough to explain S_1000 would show up as landings clustered at max_block;
  the genuine landings span floors 176,186..1,268,392 with no proximity to
  the edge, and every genuine landing row has a non-`{0,2}` intruder
  (∈ {4,6,12,14}) beyond the block.
- Every event row's `(edge, intruder)` is exactly `(2,4)` (step law), and the
  landing block's own value past the run is always a *small* even number —
  the block ends on a small, "renewal-typical" intruder, not on a pile-up at
  the boundary.

**What this does NOT establish.** Genuine at depth 1000 means the recorded
jump is the complete jump of the infinite triangle *up to that row* — the run
that produced it ends inside the measured row with a witness entry past it.
It does not bound the true jump at i=161 (≥ 176,181, unknown), and it says
nothing about whether later giants occur at larger widths; the surplus
statement "b_1000 = 1.27M ≫ 1" remains a fact about depth 1000, not a trend.
It *does* settle the directive's decision point: the reframing in
`research/threads/regeneration.md` (the object is the gap between consecutive
large jumps) is riding on a real effect.

**Cost.** O(W × 165) time for the recompute (W = 1,270,607) plus O(D) for the
table; ~130 s wall under `timeout 540`; one worker; exact integer arithmetic
throughout (`lib.gilbreath.py`, no floats).

```claim
id: bigjump-cap-characterization-1000
statement: Of the 13 (2,4)-events with jump j > 1000 in the prime Gilbreath
  triangle to depth 1000 (sieve 2e7, W = 1270607 primes), 12 are genuine
  dynamics and 1 is a finite-width artifact. Genuine means the landing block
  b_{i+1} ends strictly inside row i+1, i.e. floor_distance = (W - i - 2) -
  b_{i+1} >= 1 and the landing row has a non-{0,2} intruder past the block
  ({4,6,12,14} in all 12 cases), so the recorded jump is the complete jump of
  the infinite triangle at that row. The capped event is i=161:
  b_162 = 1270444 = W - 162 - 1 = max_block, landing-row intruder null, so
  the true jump is >= 176181 (recorded). The 12 genuine giants carry
  1091362 of the full surplus S_1000 = 1270603 (86.1%); the 13 giants carry
  99.76% of S_1000. The heavy tail (j > 10^4) is 9 genuine of 10, including
  the two largest measured jumps i=146 (j=360698, floor 176186) and i=134
  (j=217657, floor 536907); floor distances of genuine landings span
  176186..1268392 with no clustering at the width edge. Hence the surplus
  heavy tail is genuine prime-renewal structure, not a finite-width effect;
  the i=161 recorded jump is a lower bound and rows k >= 162 are the known
  width-exhaustion artifact.
hypotheses: rows are iterated absolute differences of primes below 2e7
  (W = 1270607), 1-based rows with row r having W - r columns, block length
  b_k measured from position 1, event rows identified by the step law
  (edge, intruder) = (2, 4), depth 1000
holds-here: yes (depth 1000, exact)
status: checked
bearing: decides Directive 23's fork: the giant jumps (and hence the
  heavy-tailed surplus) are a genuine feature of the primes' renewal
  structure, so the regeneration thread's target object is the gap between
  consecutive large jumps, not a mean event rate; i=161 must be quoted as
  j >= 176181 and never as an exact jump.
anchor: code/out/bigjump_characterization.captured.txt, code/pattern/bigjump_characterization.py
source: operator-computation
```