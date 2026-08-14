# Census of Minkowski sums of the calibrated 7-vertex spindle

`code/spindle_minkowski_census.py` (run on levels 2..6, each captured in
`code/out/spindle_minkowski_census_k{2..6}.captured.txt`, all `EXIT_CODE=0`);
growth analysis in `code/minkowski_growth_fit.py`
(`code/out/minkowski_growth_fit.captured.txt`). Level 1 is the calibration
graph itself, re-captured verbatim in `code/out/brute.captured.txt`
(fresh sha256 79e80710ac27ee198100c2326ad969544f5a86e2444807d96f9961a8bd7587c9;
the hash f73f3724... in `code/out/commands.log` and `code/check_scholar.py`
belongs to an earlier overwritten capture and is stale).

## Measured (exact arithmetic, double-verified)

A = the 7-vertex Moser-spindle graph of problem.md (7 points,
11 unit edges, chi = 4 — calibrated oracle). A^k = k-fold Minkowski sum.

| k | n (distinct points) | e (unit edges) | chi | edge engines agree | colour engines agree |
| --- | --- | --- | --- | --- | --- |
| 1 | 7 | 11 | 4 | (calibration) | (calibration) |
| 2 | 26 | 69 | 4 | brute = sympy (69) | DSATUR = plain (4, not 3) |
| 3 | 70 | 240 | 4 | brute = sympy (240) | DSATUR = plain (4, not 3) |
| 4 | 155 | 628 | 4 | brute = sympy (628) | DSATUR = plain (4, not 3) |
| 5 | 301 | 1375 | 4 | brute = sympy (1375) | DSATUR = plain (4, not 3) |
| 6 | 532 | 2659 | 4 | brute = sympy (2659) | DSATUR = plain (4, not 3) |

Every edge certified `|p - q|^2 == 1` by TWO independent arithmetic engines:
(1) the calibrated hand-written exact field Q(sqrt3,sqrt11) oracle
(`brute.unit_graph`), and (2) a sympy route (sqrt objects, expansion,
coefficient zero-test against the Q-linearly independent basis
{1, sqrt3, sqrt11, sqrt33}). The two edge lists are identical for every
level. 4-colourability is decided by TWO independent complete tests
(DSATUR-style exhaustive backtracking in `lattice_census.chromatic`, and the
plain symmetry-broken backtracking of `brute.coloring_test`); both return
proper 4-colour witnesses (re-verified against the edge list) and both
report not-3-colourable. So chi(A^k) = 4 for k = 1..6.

Proved structural input: A embeds into A^k via a |-> a + 0 + ... + 0, so
chi(A^k) >= 4 = chi(A) for every k. The census establishes the upper side:
4 colours suffice for all six levels.

## Growth of the point count |A^k|

The exact counts n(k) = 7, 26, 70, 155, 301, 532 satisfy the quartic
polynomial

    n(k) = (k^4 + 6k^3 + 14k^2 + 15k + 6) / 6   for k = 1..6,

verified two ways: (a) the quartic fitted through k=1..5 predicts n(6) = 532
exactly (out-of-sample match), and (b) the degree-5 interpolation through
all six points has k^5 coefficient exactly 0. The edge count is NOT quartic:
its fifth finite difference over k=1..6 is -2 (degree-5 fitting coefficient
-1/60), so e(k) is slightly sub-quartic in this range; e/n rises monotonically
and reaches 4.9981 at k=6 (average degree 9.996, well above the n^{1/3}
random-point scale but below the extremal O(n^{4/3}) curve, consistent with
the density constraint). These are computed-and-checked statements about the
measured levels only; the quartic law for all k is not proved.

## Feasibility boundary

The colouring test completed instantly at every level (worst 8.0 s at
k=5, 301 vertices, DSATUR; 0.05 s at k=6, 532 vertices). The census did not
reach infeasibility: the search stayed easy even at 532 vertices because the
graphs are only average-degree ~10 and 4-colourable. Construction cost is
exact field operations over 7^k raw candidates (117649 at k=6, 0.03 s).

## Note on claim duplication

This measured census is recorded authoritatively by the claim
`minkowski-power-census` in
`research/summaries/minkowski_power_census.md` (the scholar session
independently wrote the same claim id there, including the extend run's
k=7 counts n=876, e=4694 and the full reconciliation of both census programs
and both capture sets: k=1..6 colour-tested two ways, k=7 counts-only, and
the quartic n(k) = (k^4 + 6k^3 + 14k^2 + 15k + 6)/6 confirmed out-of-sample
at k=7). The ledger keeps one row per claim, so this file carries no claim
block of its own; it stands as the record of the calibration-hash detail
below, which the scholar's file does not contain.

## Calibration capture hash

`code/out/brute.captured.txt` was re-run fresh in this session:
18 lines, sha256 `79e80710ac27ee198100c2326ad969544f5a86e2444807d96f9961a8bd7587c9`,
EXIT_CODE=0, ending `CALIBRATION PASSED: 7 points, 11 certified unit edges,
chi = 4 and not 3.` The sha256 `f73f3724...` that appeared in
`code/out/commands.log` and was hard-coded as the expected hash in
`code/check_scholar.py` belongs to an earlier capture that has since been
overwritten — it is stale, and `check_scholar.py` has been updated to the
current hash (its checks re-pass).