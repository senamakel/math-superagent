# Survivor sequences for EG barriers (updated with new no-4 counts)

Computed by `code/eg/survivor_no4_n14.py`, `code/eg/survivor_girth5_n14.py`
(geng `-f` native C4-free generation, BFS girth, polynomial), and checked for
8-cycles by `code/eg/check_no8_survivors.py`, `code/eg/check_no8_n14.py`,
`code/eg/check_no8_n16.py`.

## total (A007112) — min-degree>=3 connected graphs by order
n:        4   5   6    7     8       9       10        11        12          13         14
total:    1,  3,  19,  150,  2589,   84242,  5203110,  577076528, ...        ...        ...

## NO4(n) = connected min-degree>=3, no 4-cycle (exact first EG barrier)
Generated natively by geng -f (a 4-cycle is itself a forbidden 2-power cycle,
so no counterexample is lost). Triangles allowed.
n:        4 5 6 7 8 9  10  11  12   13    14     15       16
NO4:      0 0 0 0 0 0  5   9   57  503  6059   91433   1655659

This sequence is NOT in OEIS (lookup of 5,9,57,503,6059 missed; 11-term
lookup also missed). No low-order structure found by analyze_sequence /
find_linear_recurrence.

## Every NO4 survivor for n<=16 has an 8-cycle (checked, exact)
n=10..16 survivors: 5, 9, 57, 503, 6059, 91433, 1655659 — each and every one
contains a cycle of length exactly 8 (exact bounded DFS for length 8).
So NO counterexample to EG exists on n<=16, re-verifying the literature floor
(>=17 vertices) computationally on the exact class (min-degree-3, no 4-cycle)
that could be one. The first no-4 survivor at n=10 is the Petersen graph
(has 8-cycle, so NOT a counterexample).

## S5(n) = girth>=5 (no 4-cycle AND no triangle — stricter)
n:       4 5 6 7 8 9  10  11  12  13  14
S5:      0 0 0 0 0 0  1   0   2   4  23
[From earlier run; girth>=5 forbids both 4-cycles and triangles. The exact
first EG barrier is "no 4-cycle" only, so NO4 above is the right sequence;
S5 is the cubic/girth regime that leads to the Moore bound.]

## Moore-bound threshold (d=3): smallest n that can possibly survive
avoiding all 2-powers <= 2^m requires girth >= 2^m+1, Moore min n =
3*2^(2^(m-1)) - 2:
m=2 (no 4): 10   (realized: Petersen, but it has an 8-cycle)
m=3 (no 8): 46   (next EG barrier)
m=4 (no 16): 766
m=5 (no 32): 196606
m=6 (no 64): 12884901886

## What this says for the run
The girth regime is NOT where a counterexample hides at accessible n: clearing
the 4-barrier is possible from n=10, but every graph that clears it below n=17
has an 8-cycle, and clearing the 8-barrier needs n>=46, far above the
verification floor of 17. The structural fight is in low-girth cubic-dominated
graphs (the admissible-cycles / consecutive-lengths machinery), not in the
girth regime.