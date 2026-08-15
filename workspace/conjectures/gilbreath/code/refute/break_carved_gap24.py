#!/usr/bin/env python3
"""Try to break R-carved-gap24: every 2-then-odds sequence A_0=(2,3,x1,x2,...)
with x1-3=2 and x_{i+1}-x_i in {2,4} for all i>=1 has leading entry 1 forever.

A finite prefix of length N (N odds after 3, so N+1 even gaps each in {2,4},
first forced 2) that produces any leading entry != 1 within depth <= N is a
counterexample to the infinite claim, because no extension can retroactively
fix an already-wrong row.

We enumerate over the free gaps (positions >=2, each in {2,4}) and run the
triangle. Report the first death.
"""
import itertools

def death(gap_list):
    """gap_list[0]=2 (first even gap), rest in {2,4}. Build A_0 and iterate."""
    # A_0: 2,3, then odds x1,x2,... with x1-3=gap0, x_{i+1}-x_i=gaps[i+1]
    row = [2, 3]
    x = 3
    for g in gap_list:
        x += g
        row.append(x)
    # iterate absolute differences; check leading entry of each row
    cur = row
    for depth in range(1, len(cur)):  # can go up to len-1 rows
        nxt = [abs(cur[i] - cur[i+1]) for i in range(len(cur)-1)]
        if nxt[0] != 1:
            return depth, nxt[0], row
        cur = nxt
    return None

def main():
    # first free even gap is 2 (x_1 - 3 = 2). Enumerate remaining N-1 gaps in {2,4}.
    for N in range(2, 17):  # total number of even gaps
        count = 0
        for rest in itertools.product([2,4], repeat=N-1):
            gaps = (2,) + rest
            res = death(list(gaps))
            if res is not None:
                d, val, row = res
                print(f"DEATH N={N}: depth={d} leading={val}")
                print(f"  A_0 = {row}")
                # print the prefix that was odd
                return
            count += 1
        print(f"N={N}: {count} sequences, all survive to depth {N}")
    print("NO DEATH found in exhaustive search of {2,4}-gap class up to N=16")

main()
