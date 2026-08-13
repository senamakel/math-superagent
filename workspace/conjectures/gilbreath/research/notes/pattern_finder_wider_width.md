# Wider-width extension of the live regime (pattern_finder, this session)

## Question answered

The depth-1000 / sieve-20M record (`code/out/blocks_depth1000.json`) runs out
of row width at row 161 — the block is glued to the finite right edge
(`intruder = None`) from row 162, and every jump measured there is a lower
bound. Directive 24's open question was whether the giant-jump tail persists
at larger widths. This run recomputed the rows **exactly** at sieve 300M
(16,252,325 primes, rows 1..300, one row at a time, int64, `numpy` diffs),
making the live (non-exhausted) regime rows **1..239**.

## Trustworthiness chain

- Oracle: rows 1..161 of the clean run **exactly equal**
  `blocks_depth1000.json` b (verified 161/161); the first five rows also
  reproduce problem.md's worked table (via `lib/gilbreath`).
- Step law verified **over every live transition** (rows 1..300): zero
  failures (`prediction = (b_{k+1} >= b_k) == (e_k==2 and c_k==4)`).
- Second entries: all 300 in {0,2}.
- **Corruption found and fixed**: the first wider-width run's saved
  b/intruder tail disagreed with a clean recomputation (saved b_239 =
  16,252,085 / intruder 6; truth = 16,252,084 / intruder 4). All numbers in
  this note come from `code/out/wider_width_b_clean.json` (the clean run) and
  from the hand-verified recomputation of rows 237-240.

## Results (exact integers, live regime rows 1..239, width = 300M sieve)

### 1. The row-161 cap is unveiled; the record jumps keep growing

- Row 161 jump: **4,323,712** (was "≥ 176,181" at width 20M).
- Row 175 jump: **5,237,310** (landing 10,655,286).
- Row 239 jump: **5,596,824** — the new largest jump in the run, landing
  16,252,084, still a new all-time maximum of b (the previous max was
  10,655,286). Rows 240..300 then erode one per row (the mechanical
  end-of-queue); the live regime genuinely ends at row 239.

### 2. The gap between large jumps grew, then shrank — MAX GAP 64 rows

Giants (jump > 1000) at rows:
`35, 57, 65, 69, 95, 97, 111, 113, 127, 131, 135, 147, 162, 175, 239`
(15 giants; rows here are 1-based; old-13 set + 162 + 175 + 239).
Gaps: `22, 8, 4, 26, 2, 14, 2, 14, 4, 4, 12, 15, 13, 64` — **max 64**
(row 175 → row 239), the longest drought in the computed record, and the
drought is followed by the new record *jump*. The empirical "giants keep
arriving" evidence across 238 rows: a jump > 1000 at least once every 64
rows, a jump > 10000 at least once every 64 rows, a jump > 100000 at least
once every 64 rows.

### 3. Every giant lands at a new all-time maximum of b

15/15 (verified). This is the strongest single structural observation: the
giants are a strictly increasing-record renewal process, not recovery of
lost ground. The step law + recharge identity make the all-time max of b
strictly equal to the running sum of the jump record, so this is the
"Σ(j_i+1) never falls behind" condition holding at every giant.

### 4. Geometric growth of the landing blocks CONTINUES and strengthens

Landing blocks: `2179, 5942, 23265, 31499, 92620, 103973, 141706, 271629,
325090, 515906, 733564, 1094273, 5417975, 10655286, 16252084`.
Geometric fit log(land) = a + m·x over 15 giants: **m = 0.5599, R² = 0.9607,
per-event factor e^m = 1.751** (was m = 0.5198, R² = 0.9439 over the old 12
genuine). Geomean per-interval ratio = 1.8907. Overall growth ×7458 over 238
rows. The new points (5.4M, 10.7M, 16.3M) sit exactly on the same log-linear
trend — the geometric law is not a 12-point artifact.

### 5. Landing blocks of giants are all ≡ 0 (mod 4) or ≡ 1,2,3... — NO mod-4 constraint

Lands mod 4: 3,2,1,3,0,1,2,1,2,2,0,1,3,2,0 — all four residues appear. The
hoped-for exact forcing "giant landing ≡ 0 (mod 4)" (which would be the mod-4
{0,2}-forcing strength) is **refuted**. The jumps themselves are all even
(as the step law's (2,4)-event demands) but nothing stronger.

### 6. OEIS misses — recorded so nobody re-searches

- jump sequence at giants `[1314, 1739, 17326, 8237, 61088, 11354, 37746,
  129923, 53470, 190810, 217657, 360698, 4323712, 5237310, 5596824]`:
  no OEIS entry.
- giant gaps `[1, 6, 2, 14, 2, 14, 4, 4, 12, 15, 64]` (from the 11-gap set):
  no OEIS entry.
- landing blocks (`above-sequence`): no OEIS entry.
- b-series itself has no constant-coefficient linear recurrence of order ≤ 8
  over the 161 genuine terms (analyze_sequence/find_linear_recurrence: not
  polynomial, no small linear recurrence).

## What this does NOT establish

- Gaps of 64 show the giants do **not** arrive at a uniform cadence; a proof
  of "gap ≤ T(J)" needs a bound, not this record.
- The geometric landing growth is a **description of 15 computed events**,
  not a proof. The recharge identity needs Σ(j_i+1) ≥ k−1−b_1 for ALL k;
  the record shows the surplus is carried by a handful of giants whose
  density (15 in 238 rows ≈ 6.3%) is not bounded below by any theorem.
- The 16.25M landing at row 239 is within ~2 positions of the 300M-sieve
  edge, so this width is *again nearly exhausted* at row 239, and the
  "queue of 2's at the end of the row" effect may be feeding the late
  giants. A wider sieve (1e9+ primes ~ 50M, or prime-tuple generation) is
  needed to see whether the pattern (record giant, 64-row gap, then the
  widest-yet block) repeats at substantially larger width.

## Files

- `code/pattern_finder/wider_width_clean.py` (the run), capture
  `code/out/wider_width_clean.captured.txt`, data
  `code/out/wider_width_b_clean.json`.
- `code/pattern_finder/verify_step_law_transition.py` (rows 237-240
  recomputation; first version OOM'd at ~15 GB because it stored all rows;
  the fixed one-row version is the trusted one), capture
  `code/out/verify_step_law_transition.captured.txt`.
- `code/pattern_finder/threshold_gap_table.py` (old-width threshold table),
  capture `code/out/pattern_finder_threshold_gaps.captured.txt`.
- `code/out/wider_width_extend.captured.txt` (the pre-fix run — superseded
  for its tail numbers, correct for rows 1..161).
- `code/out/directive24_geometric_growth.md` (previous 12-point analysis).