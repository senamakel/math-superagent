#!/usr/bin/env python3
"""Search for a counterexample to R-carved-gap24 / R-gaps-24:
A_0 = (2,3,x_1,x_2,...), x_1 - 3 = 2, x_{i+1} - x_i in {2,4} for all i >= 1
=> A_k(1) in {0,2} for all k (equivalently A_k(0) = 1).

The corner argument settles this if A_2 becomes the all-{0,2} corner. But the
{2,4} class allows long blocks of the SAME gap value or alternating, and the
block only erodes at rate 1 while new {0,2} must be regenerated below.  The
empirical claim is "0 deaths among 48 sequences". Let's search harder over
longer gap strings (exact oracle) to see if ANY finite prefix dies.

A finite prefix producing A_k(1) not in {0,2} within depth <= len is a
genuine counterexample to the infinite class claim (no extension can repair
an already-wrong row).
"""
import itertools


def first_failure(gaps):
    """gaps: tuple with gaps[0]=2 (x1-3), rest in {2,4}. Return (depth,val,row)
    if any row k>=1 has leading entry != 1, else None."""
    x = 3
    row0 = [2, 3]
    for g in gaps[1:]:
        x += g
        row0.append(x)
    cur = row0
    W = len(cur)
    for depth in range(1, W):
        nxt = [abs(cur[i] - cur[i + 1]) for i in range(len(cur) - 1)]
        if nxt[0] != 1:
            return depth, nxt[0], row0
        cur = nxt
    return None


def main():
    max_free = int(INPUT_MAXFREE)
    deaths = 0
    first = None
    total = 0
    for nfree in range(1, max_free + 1):
        for rest in itertools.product([2, 4], repeat=nfree):
            gaps = (2,) + rest
            r = first_failure(gaps)
            total += 1
            if r is not None:
                deaths += 1
                if first is None:
                    first = (nfree + 1, r[0], r[1], gaps)
    print(f"scanned {total} gap strings (2 + {max_free} free each in {{2,4}})")
    print(f"deaths (leading != 1 at some row): {deaths}")
    if first:
        print("first: width(W)=", first[0], "died at depth", first[1],
              "leading", first[2], "gaps", first[3])
    else:
        print("no death in the {2,4} class up to width", max_free + 2)


if __name__ == "__main__":
    INPUT_MAXFREE = "22"
    main()
