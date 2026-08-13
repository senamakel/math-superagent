#!/usr/bin/env python3
"""Sharpened version of check_edge_zero_run.py: the nontrivial statement.

The edge sequence e_0..e_{n-1} of a halved {0,2} block h[0..n-1] under pure
erosion is the Rule-90 (Pascal mod 2) convolution
    e_d = XOR_{j=0}^{d} [C(d,j) mod 2] * h[(n-1-d)+j],   d = 0..n-1.
e_d = 0 means the block's edge reads 0 after d erosion rows, during which NO
(2,4)-regeneration is possible even if the intruder is 4 (boundary pair
(0,4) gives |0-4| = 4, erosion continues).  So the longest zero-run of
(e_0..e_{n-1}) is how long regeneration is *structurally blocked* by the
block's own interior pattern, independent of the intruder.

The predecessor run showed the bound "worst zero-run <= 2n" holds for ALL
2^n patterns only vacuously (the sequence has n entries; the only pattern
achieving a run of length n is the all-zero block).  This program settles
the real question: among NONZERO blocks, what is the worst-case zero-run,
and which patterns achieve it?

Two independent routes:
  R1 (comb / Lucas): e_d = XOR over j with C(d,j) odd.
  R2 (direct simulation): build the full unhalved row [1] + [2*h_i] and
      simulate d literal |a-b| erosion steps, reading the edge each time.
R1 and R2 must agree for every pattern.
"""
import sys
from math import comb
from itertools import product


def route1_edge_sequence(h):
    n = len(h)
    e = []
    for d in range(n):
        val = 0
        for j in range(d + 1):
            if comb(d, j) % 2:
                val ^= h[(n - 1 - d) + j]
        e.append(val)
    return e


def route2_edge_sequence(h):
    """Literal absolute-difference simulation on the unhalved row."""
    n = len(h)
    row = [1] + [2 * x for x in h]          # leading 1 + {0,2} block at cols 1..n
    e = []
    for d in range(n):
        # edge of the current row's {0,2} block = position n - d (1-based col)
        e.append(row[n - d] // 2)
        row = [abs(row[i] - row[i + 1]) for i in range(len(row) - 1)]
    return e


def longest_zero_run(seq):
    m = cur = 0
    for x in seq:
        cur = cur + 1 if x == 0 else 0
        m = max(m, cur)
    return m


def main():
    max_n = int(sys.argv[1]) if len(sys.argv) > 1 else 18
    print("two routes: R1 = Pascal-mod-2 convolution, R2 = literal |a-b| erosion")
    agree_all = True
    worst = {}
    for n in range(1, max_n + 1):
        w = 0
        wpat = None
        wcount = 0
        total = 1 << n
        for mask in range(1, total):        # mask 0 = all-zero block, excluded
            h = [(mask >> b) & 1 for b in range(n)]
            e1 = route1_edge_sequence(h)
            e2 = route2_edge_sequence(h)
            if e1 != e2:
                agree_all = False
                print(f"  MISMATCH n={n} h={h} R1={e1} R2={e2}")
            r = longest_zero_run(e1)
            if r > w:
                w = r
                wpat = h
                wcount = 1
            elif r == w:
                wcount += 1
        worst[n] = (w, wpat, wcount)
        print(f"n={n}: nonzero patterns={total-1}  worst zero-run={w}  "
              f"(< n: {w < n})  achieving pattern h={wpat}  count={wcount}")
    print("\nroutes agree on every pattern:", agree_all)
    print("\nSummary (nonzero blocks only): worst zero-run vs n vs 2n")
    for n in range(1, max_n + 1):
        w, wpat, wcount = worst[n]
        print(f"  n={n}: worst={w}  2n={2*n}  is it the all-1 block? "
              f"{wpat == [1]*n}")
    return 0 if agree_all else 1


if __name__ == "__main__":
    sys.exit(main())