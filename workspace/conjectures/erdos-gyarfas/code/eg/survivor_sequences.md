# Survivor sequences for EG barriers

Computed by `code/eg/fast_girth_survivors.py` (polynomial BFS girth) and verified
against `code/count_mindeg3.py` / OEIS A007112 for the totals.

`S_g(n)` = number of connected min-degree>=3 graphs on n vertices (nauty-geng
isomorphism classes) with girth >= g. A graph that survives the EG first barrier
(no 4-cycle) is exactly one with girth >= 5; clearing the second (no 8-cycle)
is girth >= 9; etc.

## total (A007112) — min-degree>=3 connected graphs by order
n:        4   5   6    7     8       9       10        11
total:    1,  3,  19,  150,  2589,   84242,  5203110,  577076528

## S5(n) = girth>=5 (survives "no 4-cycle" barrier)
n:       4 5 6 7 8 9  10
S5:      0 0 0 0 0 0  1

The lone n=10 survivor is the Petersen (cubic, girth 5, cycles {5,6,8,9}).
It has an 8-cycle, so it is NOT an EG counterexample; it is the first graph
that even reaches the first barrier.

## Moore bound (min-degree 3): smallest n that can possibly survive
girth barrier g  =>  min n = 1 + 3*sum_{i=0}^{floor((g-1)/2)-1} 2^i
girth>=5  -> n>=10   (realized: Petersen)
girth>=9  -> n>=46   (next EG barrier: no 8-cycle)
girth>=17 -> n>=  ?  (no 16-cycle barrier)
