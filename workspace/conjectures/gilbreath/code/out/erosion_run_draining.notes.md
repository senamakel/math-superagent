# Erosion-run draining check — REG-intruder-drains, machine-confirmed

Tool: `code/backward/erosion_runs.py`; capture `code/out/erosion_run_draining.captured.txt`.

## What was checked

Every erosion run (maximal stretch of rows with `b_{k+1} = b_k − 1`) was
extracted from three prime-triangle records, all built from an exact-int64
re-generation of the triangle (one row alive at a time, `O(depth × width)`
time, `O(width)` memory):

- depth-1000 record (sieve 2e7), real regime `A_1..A_247` while an intruder
  exists;
- 6e8 record (sieve 6e8), `A_1..A_247`;
- 1e9 record (sieve 1e9), `A_1..A_247`.

The generator is an oracle first: it reproduces the stored
`blocks_depth1000.json` `b` and `intruder` arrays with zero mismatches on
`A_1..A_247` (aligned `ref[i] = A_{i+1}`), so we are reading the same triangle
as the record. `edge = A_k(b_k)` (last in-block entry, in {0,2}) and
`nonzero` = the leading block `A_k(1..b_k)` contains a value ≠ 0 are computed
from the regenerated row (the stored JSON does not carry edge / block content).

For each run: initial intruder `y_0`, final intruder `y_f`, edge-2 flip count
(number of erosion steps where `A_k(b_k) = 2`), run length `d`, initial block
length `b_0`, and block-nonzero at the run's last row.

## Check (i) — drain-law identity (sanity)

`flips == (y_0 − y_f)/2` on every run.

- depth-1000: 26 runs, 0 violations
- 6e8: 32 runs, 0 violations
- 1e9: 32 runs, 0 violations

The intruder is exactly non-increasing, dropping by 2 at each erosion step
whose edge reads 2. Sanity confirmed exactly.

## Check (ii) — REG-intruder-drains target

`y_f = 4` with `b ≥ 1` and nonzero block in every run.

- depth-1000: 26/26 runs reach `y_f = 4`, 0 violations (all nonzero)
- 6e8: 32/32 runs reach `y_f = 4`, 0 violations
- 1e9: 32/32 runs reach `y_f = 4`, 0 violations

Every erosion run descends to intruder 4 against a still-nonzero,
b ≥ 1 block — the REG-intruder-drains hypothesis holds at every erosion run
of these records, with zero violations. (The 6e8 and 1e9 run lists are
bit-identical on rows 1..247, an independent cross-check of the two sieves.)

## Max intruder and flip count

- depth-1000 record (A_1..A_247): max `y_0 = 14`, so the deepest real-regime
  run needs **at most 5 edge-2 flips** — the depth-1000 gap is a claim about
  ≤ 5 flips per run, exactly as the note predicted.
- 6e8 / 1e9 wider records: max `y_0 = 54`, max flips = 25. The single run with
  `y_0 = 54` is the post-giant erosion run at `A_175` (block 10,655,286, d = 48,
  y_f = 4, nonzero). So the "≤ 5 flips" bound is specific to the depth-1000
  regime; the wider records contain a deeper intruder needing 25 flips, and
  that too drains to 4 within its run.

So REG-intruder-drains is **machine-confirmed over all 26 + 32 erosion runs**
(rows to 247), with the caveat that the per-run flip budget grows from 5
(depth-1000) to 25 (the A_175 giant region). This does not prove the open
lemma — it validates the structural claim that the intruder always drains to 4
before the block dies, exactly the precondition Step 3 of the skeleton needs.

## Status

CONFIRMED over the stated range (rows 1..247 of the 2e7, 6e8, 1e9 records):
0 drain-law violations, 0 REG-intruder-drains violations, every run reaches
y_f = 4 with a nonzero block. Exact integer arithmetic only.
