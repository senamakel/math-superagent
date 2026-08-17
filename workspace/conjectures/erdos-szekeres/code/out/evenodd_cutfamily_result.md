# evenodd_cutfamily — result (directive 17 part 2, EXECUTED)

**Answer:** the even/odd block bipartition of the verified `es_construct`
template at **n=7** is realized by an intersection of **exactly 3** open
half-plane sides — the minimum over all k ≥ 1. Not a single line (k=1: 0, and
0 valid single-line splits on this template), not a double wedge (k=2: 0
side-pairs), but a **triple** of lines.

## What was run

- Program: `code/out/evenodd_cutfamily.py` (607 lines; the first ever
  execution of this file — it had no capture before this run; two bugs fixed:
  a multi-line f-string conditional at line 528, and `sel_sides` indexing
  `sides` by a mask instead of by index at line 546).
- Capture: `code/out/evenodd_cutfamily.captured.txt` (command + `EXIT: 0`,
  23.5 s wall, 28 workers, exact integer/Fraction determinants via the
  verified `lib.es_geom` and `lib.es_construct`).
- Method (exact reduction, not brute force): only sides that are supersets of
  the target can appear in an intersection equal to it — 16 such sides per
  half.  An intersection of k superset sides equals the target iff their
  complementary masks cover the 16-point complement universe.  The exact
  minimum k over ALL k ≥ 1 is therefore the exact minimum set cover of a
  16-element universe, computed by the DP `dp[mask] = 1 + min dp[mask & ~d]`
  over the 65536 masks (numeric-predecessor argument makes the ascending sweep
  exact), with inclusion-maximal dominance reduction.

## Numbers

| check | evenHalf (T0∪T2∪T4) | oddHalf (T1∪T3∪T5) |
|---|---|---|
| k=1 (target among the 992 sides) | False (record reproduced) | False (record reproduced) |
| k=2 (pair control) | 0 of 120 side-pairs (record reproduced) | 0 of 120 |
| **min k (exact, all k≥1, by set-cover DP)** | **3** | **3** |
| exhaustive k=3 scan witness | (4, 14, 15) | (0, 10, 15) |
| witness direct check (o_i&o_j&o_k == 0) | True | True |
| direct frozenset verification (intersection == target) | True | True |
| realizing lines (a→b, kind = on-line points left) | 6→25 (kind 1), 26→30 (kind 3), 0→5 (kind 1) | 0→1 (kind 2), 16→30 (kind 1), 1→15 (kind 1) |

## Independent second check (counting cut)

Over all 992 ordered pairs, the strict-left open side has exactly 16 points in
38 cases; with no tie-break (any of the 4 inclusions, or the 4 deterministic
rank rules low/high/parity-even/parity-odd) does any directed line realize
evenHalf or oddHalf. Verdict: NO line + tie-break realizes either half (0 /
0), an independent confirmation of the k=1 record. This is a second code path
(it re-derives the side sets from `lib.es_geom.orient` and does not call
`ordered_pair_sides`).

## Scope

Strictly the verified `es_construct` template at n=7. Not a statement about
other extremal sets, not the general G-split lemma. It joins the recorded
chain: the even/odd split is not a half-plane (gsplit_phase2), not a
side-pair/double-wedge (wedge_evenodd_check), and is now shown to be a
**triple of open half-planes** — so among cut families by number of lines, its
minimum is 3.

## For the writing role

Task `evenodd-cutfamily-which-family-realizes` (directive 17 part 2) is
EXECUTED and can be closed with this reason. The result is the positive
min-k=3 answer above (a negative would have been "not a half-plane, not a
double wedge, not a triple"; the triple exists, so the run's framing "A
negative is a result here" does not apply — this is a positive, and it pins
the cut-family complexity of the even/odd split at exactly 3 sides).

Provenance: `$ python code/out/evenodd_cutfamily.py`; `EXIT: 0`;
python 3.11.2; numpy 2.4.6; 28 workers; 23.5 s wall; exact integer
determinants throughout.