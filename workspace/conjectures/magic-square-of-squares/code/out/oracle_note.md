# Oracle run — worked-example check, exhaustive small scans

`code/brute.py`, first run 2025-07-13, exact output in `oracle_output.txt`,
plus `code/check_near_misses.py` (exact integer arithmetic), whose fresh
worked-example rerun and near-miss construction output the statements below.

The statement (problem.md) gives no numeric example grid — it is an open
question — so its *structural* worked examples were rerun fresh by
`check_near_misses.py` and every one matched:

- The parametrised grid is magic with constant exactly `3c` and centre
  `c = M/3` — checked on all 585,640 grids with `c` in 1..40, `|u|,|v| <= 60`
  (0 mismatches).
- The parametrisation is complete: every magic grid reconstructs exactly as
  `(centre, a00-centre, a02-centre)` — checked on 68,026 grids plus the Lo Shu
  (0 mismatches).
- The four centre lines are 3-term APs whose common differences are
  `u-v, u+v, u, v` up to sign — checked on all 65,025 grids with
  `c` in 1..25, `|u|,|v| <= 25` (0 mismatches).
- Verifier decisions on the known-answer cases: Lo Shu → not-a-square; nine
  1s → not-distinct (relaxed: True — the only way the True branch is
  exhibitable, since no distinct solution is known); distinct squares not
  magic; a parametrised magic grid that is not all squares; a float entry; a
  wrong-shaped grid (all as expected). Statement consequence: Lo Shu constant
  15, centre 5 = 15/3. ✓

## "The space of magic assignments has dimension 4" is NOT what the incidence algebra gives

The 8 lines × 9 cells incidence matrix over Q was built and its rank computed
exactly (Fraction Gaussian elimination in `code/lib/mss.py`), and re-derived
independently with sympy. Both agree:

- **rank = 7**, not 5. The eight line equations have exactly one Q-relation,
  the trivial double-counting `col1+col2+col3 = row1+row2+row3`
  (coefficients `[-1,-1,-1,+1,+1,+1,0,0]` on the eight lines in order
  rows, cols, principal diag, non-principal diag). The diagonals are free.
- So the **zero-sum kernel** (all eight line sums 0) has dimension `9 - 7 = 2`,
  spanned exactly by the grid patterns of `u` and `v`.
- The **affine space of magic assignments** (all eight line sums equal, no
  zero constraint) has dimension `9 - rank(L2-L1,..,L8-L1) = 9 - 6 = 3`,
  spanned by the constant grid, the u-grid and the v-grid — exactly the
  `(c, u, v)` parametrisation.

The task brief's "dimension 4 with (c,u,v) basis" is therefore self-
contradictory (three parameters (c,u,v) and three linearly independent grid
patterns give dimension 3). This run reports the computed value **3** and
flags the discrepancy rather than asserting 4. The parametrisation itself is
untouched: completeness holds in both directions.

## The two known seven-square near-misses, reproduced and verified

`check_near_misses.py` constructs both from the printed grids in Bremner,
"On squares of squares", *Acta Arithmetica* 88 (1999), p. 290 (local copy
`research/sources/bremner-on-squares-of-squares-1999.full.md`), with exact
integer verification; full output is in `code/out/near_misses.json`.

- **Sallows LS1** — printed orientation rows `[58², 46², 127²; 94², 113², 2²;
  97², 82², 74²]` (the user's `[127,46,58; 2,113,94; 74,82,97]` is its
  transpose): all 9 entries distinct squares; **7 of 8** line sums equal
  `147² = 21609`; fails at the non-principal diagonal with sum `38307`. ✓
- **Bremner's magic square** — rows `[373², 289², 565²; 360721, 425², 23²;
  205², 527², 222121]`: **all 8 line sums equal `541875`**; centre `= 425² =
  M/3`; **exactly 7 square entries**; the two non-squares are exactly
  `360721` and `222121`. ✓

These two grids are the witness set under GOAL.md: every impossibility lemma
this run produces must be run against both via a `refutes(witness)` check.

## The (c, u, v) extraction and the four centre-line differences

From the entries of Bremner's grid, `(c, u, v) = (180625, -41496, 138600)`
with `c = M/3 = 425²`. For each `d in {u, v, u+v, u-v}` the program asks
whether BOTH `c+d` and `c-d` are perfect squares, and finds **exactly two**
true — the corrected expectation (the steering note replaced the original
"exactly one" which was wrong):

| d        | value    | c+d            | c−d            | both squares |
|----------|----------|----------------|----------------|--------------|
| u        | −41496   | 139129 = 373²  | 222121 (non-sq)| **False**    |
| v        | 138600   | 319225 = 565²  | 42025 = 205²  | **True**     |
| u+v      | 97104    | 277729 = 527²  | 83521 = 289²  | **True**     |
| u−v      | −180096  | 529 = 23²      | 360721 (non-sq)| **False**    |

The two realized relations arise from Pythagorean splits of `c = 425²`:
`(385, 180)` gives `385²+180² = 425²` and `2·385·180 = 138600 = v`;
`(408, 119)` gives `408²+119² = 425²` and `2·408·119 = 97104 = u+v`. The
full split list of `c` is `[(420,65),(416,87),(408,119),(385,180),(375,200),
(340,255),(304,297)]`; exactly `v` and `u+v` are of the form `2xy` with
`x²+y² = c` among them.

## The generator ranges

`brute.py` scanned every 3×3 magic grid with positive entries ≤ 100 and the
near-miss box `c = e², e ≤ 80, |u|,|v| ≤ 120` (4,052,328 grids): best grid
with distinct entries has 5 square entries; no 6-square distinct magic grid
exists in either box; the only all-nine-square magic grids repeat entries
(the trivial family already known to Bremner). These are range facts about a
finite box, not structural theorems (no witness-check is attached to them;
the witness set above is for structural impossibility claims).

```claim
id: near-miss-baseline-and-incidence
status: checked
evidence: code/check_near_misses.py and code/lib/mss.py, exact integer /
  Fraction arithmetic, sympy cross-check in code/scratch_rank_probe.py (deleted
  after cross-check); near-misses constructed from the printed grids in the
  local Bremner source.
hypotheses: the two grids as printed in Bremner 1999 are what they say.
holds-here: yes
statement: the parametrisation identity and completeness hold on the rerun;
  Sallows LS1 has 7 of 8 line sums 21609 failing the non-principal diagonal
  38307; Bremner's grid is a true magic square (all 8 sums 541875, centre
  425² = M/3) with exactly 7 square entries and non-squares 360721, 222121;
  the incidence matrix has rank 7 over Q (kernel dim 2, line-relation
  col-sums == row-sums) and the affine magic space has dimension 3 = (c,u,v);
  the four differenced booleans in step (5) are [F, T, T, F].
falsifier: any of the verified identities found false; a 4-dimensional magic
  assignment space over Q; a distinct 6-square magic grid in either scanned box.
witness-check: these two grids ARE the witness set; every impossibility lemma
  the run produces must be refuted or confirmed against both (GOAL.md).
```
