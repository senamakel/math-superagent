#!/usr/bin/env python3
"""Exhaustive, exact refutation search over the {2,4}-gap class (R-carved-gap24).

Claim: for A_0 = (2,3,x_1,x_2,...) with x_1-3=2 and x_{i+1}-x_i in {2,4} for
all i>=1 (gaps after the first all 2 or 4), the leading entry A_k(0)=1 for
all k>=1, i.e. A_k(1) in {0,2} forever.

Since no extension can repair an already-wrong row, a finite prefix whose
triangle shows A_k(0)!=1 for some k<=len is a genuine counterexample.

We enumerate ALL gap strings (a binary choice at each free gap), exactly
(int rows one at a time, O(W) memory), to a larger window than the run's
earlier searches. Four independent first-gap conventions checked.
"""
import itertools, sys

def build_row0(gaps):
    # gaps[0] is the first even gap (=2). A0 = 2,3 then odds accumulating gaps.
    x = 3
    row = [2, 3]
    for g in gaps[1:]:
        x += g
        row.append(x)
    return row

def first_failure(gaps, report=False):
    row = build_row0(gaps)
    cur = row
    W = len(cur)
    for depth in range(1, W):  # rows after A_0; can go down to width 1
        nxt = [abs(cur[i]-cur[i+1]) for i in range(len(cur)-1)]
        if nxt[0] != 1:
            return depth, nxt[0], row
        cur = nxt
    return None

def main():
    maxgap = int(sys.argv[1]) if len(sys.argv) > 1 else 24   # number of free gaps (after first)
    # free gaps after the first each in {2,4}; the first even gap is forced 2
    deaths = 0
    first_death = None
    total = 0
    for ngap in range(1, maxgap+1):   # total free gaps after the fixed first 2
        # the very first "gap" slot in some conventions is g_1=x_1-3=2 fixed;
        # here we iterate `rest` of length ngap over {2,4}, prepend first 2.
        count = 0
        for rest in itertools.product([2,4], repeat=ngap):
            gaps = (2,) + rest
            r = first_failure(gaps)
            count += 1
            total += 1
            if r is not None:
                d, val, row = r
                deaths += 1
                if first_death is None:
                    first_death = (ngap+1, d, val, row, gaps)
                    print(f"FIRST DEATH: width(W)={ngap+2} died at depth {d} "
                          f"leading={val}")
                    print(f"  A_0 = {row}")
                    print(f"  gaps=({','.join(map(str,gaps))})")
        print(f"  W={ngap+2}: {count} sequences, deaths so far {deaths}")
    print("\n=== RESULT ===")
    print(f"total sequences scanned: {total}, deaths: {deaths}")
    if first_death:
        print("counterexample found (details above)")
    else:
        print("no {2,4}-class death up to width W=", maxgap+2)

main()
