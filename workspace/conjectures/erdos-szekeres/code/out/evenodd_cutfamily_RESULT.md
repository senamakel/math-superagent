# evenodd_cutfamily — captured result (this run)

**Capture:** `code/out/evenodd_cutfamily.captured.txt`, EXIT 0,
`cd /workspace && { echo "$ python code/out/evenodd_cutfamily.py"; timeout 550 python code/out/evenodd_cutfamily.py; echo "EXIT: $?"; } > code/out/evenodd_cutfamily.captured.txt 2>&1`.

**Question:** which cut family, if any, realizes the even/odd block bipartition
of the verified `es_construct` ES construction at n=7?

## Answer

The even/odd bipartition **is** realizable as an intersection of **three** open
half-plane sides. The minimum k over all k≥1 is **exactly 3** for each half,
and each half has **exactly one** realizing triple among the C(16,3)=560
superset-side triples (|A| = 16 sides that are supersets of the target).

## Numbers (all exact, verified by direct frozenset intersection == target)

- evenHalf = T0∪T2∪T4 = [0, 6..15, 26..30]; oddHalf = T1∪T3∪T5 = [1..5, 16..25, 31];
  sizes 16/16; both halves 6-avoiding (largest_convex_subset = 5 each). Gate PASS.
- 992 = N(N−1) open half-plane sides (validated ordered-pair enumerator).
- |A_even| = |A_odd| = 16 (sides superset of the target).
- k=1: not a side. k=2 (double-wedge): 0 pairs (control FAILS as required,
  reproducing the recorded double-wedge exclusion).
- **evenHalf min k=3** witness: lines 6→25 (kind 1, size 22), 26→30 (kind 3, size 31),
  0→5 (kind 1, size 27). Triple intersection == evenHalf.
- **oddHalf min k=3** witness: lines 0→1 (kind 2, size 31), 16→30 (kind 1, size 27),
  1→15 (kind 1, size 22). Triple intersection == oddHalf.
- steering counts (k=3): 560 triples considered; exactly 1 of them gives a
  3-side intersection of size 16, for each target (and that one is the target).
- counting cut (independent second check): NO directed line through two set
  points with a tie-break (any of 4 inclusions, or rank rules low/high/parity)
  yields either half — 0 hits over 992 ordered pairs; only 38 ordered pairs have
  a strict-left side of exactly 16 points and none equals either half.

## What this settles

Within the open-half-plane-side intersection family on this template:
k=1 fails, k=2 fails (known), k=3 **succeeds, exactly and uniquely per half**.
The even/odd split is geometrically realizable by a 3-line convex region
(intersection of three open half-planes = a possibly-unbounded convex cell)
on `es_construct` at n=7, even though no single line and no double wedge
realizes it. The k=4+ and counting-cut questions are moot: min k = 3.

## Method (exact, polynomial)

A side in an intersection equal to target T must be a superset of T. With
b(S) = S∩complement(T), requiring S1∩...∩Sk == T is equivalent to the
complements of the b(S) covering the 16-point universe. Minimum set cover over
2^16 masks, dominance-reduced, exact DP (self-test PASS). Corroborated by
exhaustive C(16,3)=560 k=3 scan and by direct frozenset verification of each
DP-selected triple, and independently re-derived from the (a,b,kind)
descriptions in a second exact run.

**Scope:** verified `es_construct` template at n=7 only. No Horton sets, no
empty polygons, no general G-split lemma.

## Placeholders

Tool CPU/status lines were not shown in this transcript, so elapsed wall
(24.3 s), worker count (28), python 3.11.2 and numpy 2.4.6 come from the
capture file itself; nothing else was claimed about the environment.