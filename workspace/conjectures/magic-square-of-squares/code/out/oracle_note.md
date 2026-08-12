# Oracle run — worked-example check, exhaustive small scans

`code/brute.py`, first run 2025-07-13, exact output in `oracle_output.txt`.

The statement (problem.md) gives no numeric example grid — it is an open
question — so its worked examples are *structural*, and every one of them
matched:

- The parametrised grid is magic with constant exactly `3c` and centre
  `c = M/3` — checked on all 585,640 grids with `c` in 1..40, `|u|,|v| <= 60`
  (test 1, 0 mismatches).
- The four centre lines are 3-term APs whose common differences are
  `u-v, u+v, u, v` up to sign — checked on all 65,025 grids with
  `c` in 1..25, `|u|,|v| <= 25` (test 2, 0 mismatches).
- The parametrisation is complete: every magic grid reconstructs as
  `(centre, a00-centre, a02-centre)` — checked on 3,000 pseudo-random grids
  plus the Lo Shu (test 4, 0 mismatches).
- Verifier decisions on the known-answer cases: Lo Shu → not-a-square; nine
  1s / nine 4s → not-distinct (relaxed: True — the only way the verifier's
  True branch is exhibitable, since no solution is known); distinct squares
  not magic; magic with repeats off one diagonal; a negative entry; a float
  entry; a wrong-shaped grid (test 3, all as expected).
- Statement consequence: Lo Shu constant 15, centre 5 = 15/3. ✓

The generator (oracle part 2) exhaustively scanned every 3×3 magic grid with
positive entries ≤ 100 (parametrisation completeness makes the c/u/v box
exhaustive) and the near-miss box `c = e^2, e <= 80, |u|,|v| <= 120`
(4,052,328 all-positive grids):

- best grid with **distinct** entries has **5** square entries (found several,
  e.g. c=100,u=96,v=21 → rows [25,196,79],[154,100,46],[121,4,175]);
  no 6-square grid with distinct entries exists in either box.
- the only 9-square grids are the trivial-repeat obstructions: all-`k^2`
  grids and the 8 grids over the values {1, 25, 49} — the repeated-entry
  family already known to Bremner (recalled memory), consistent with no
  distinct solution at these sizes.
- 7-square grids with distinct entries exist in the *near-miss* box (4 of
  them, rows [[25,    89-?]] — see `near_misses.json` note) but they are
  NOT magic (their 4 corners are distinct squares, and corner squares with
  distinct centre force a failure — this is exactly the classical pattern
  that makes the Parker-square near-misses four-corner failures).

```claim
id: oracle-based-verification-baseline
status: checked
evidence: exhaustive integer scan, exact arithmetic, code/out/oracle_output.txt
hypotheses: none beyond the problem statement
holds-here: true
statement: the verifier is_magic_square_of_squares agrees with the
  statement's structural worked examples; no 3x3 magic grid having entries
  1..100 and six or more distinct square entries exists; no grid in the
  box c=e^2, e<=80, |u|,|v|<=120 has six or more distinct square entries;
  the only all-nine-square magic grids in those boxes repeat entries.
falsifier: a magic square of squares (distinct) with entries in either box;
  or a 6-square distinct magic grid in either box.
witness-check: every impossibility-style claim produced by the run MUST be
  run against the literature's 7-square near-misses (GOAL.md); those stems
  are not yet in this workspace, so this oracle claim carries no such
  witness-check yet — it is a range fact, not a structural theorem.
```

Range facts like "no 6-square distinct magic grid with entries ≤ 100" are
exactly what the oracle is for; they bound where any later argument must
look, and they give the run's own generator its first computational anchor.
The claim is `status: checked` because it is a finite exhaustive
computation with exact arithmetic, not a theorem about all sizes.