#!/usr/bin/env python3
"""Refute-or-support R-leftmost-decides (spike-propagation-ladder).

Claim: 2-then-odds sequence with first even gap g_1 = 2, every gap in
{2,4,6}, finitely many 6s, and the LEFTMOST non-2 gap is a 4  ==> the
leading 1 survives forever (A_k(0) = 1 for all k).

The reverse direction is hand-supported by ONE worked example (the ladder
says so) and is NOT machine-checked. Here we brute-force: build 2-then-odds
sequences from finite gap patterns {g_1=2, g_2..g_m in {2,4,6}}, then all
2s after position m (so finitely many 6s). Enforce leftmost non-2 (after
position 1) is a 4. Compute rows exactly (small width), detect first
failure A_k(1) notin {0,2} which kills A_{k+1}(0) != 1. This is the naive
oracle for small instances: declared exponential on the pattern length m.

A surviving sequence to width W with a first failure before W rows is a
refutation.
"""
import itertools
import sys

def build_from_gaps(gaps, W):
    """gaps: list starting [2, ...]. A_0 = (2,3,5,...) with consecutive
    odd adds of gap values. Return top row extended until >= W entries."""
    row = [2, 3]
    for g in gaps[1:]:
        row.append(row[-1] + g)
    # extend with 2s to reach width W
    while len(row) < W:
        row.append(row[-1] + 2)
    return row

def diff_row(row):
    return [abs(row[i] - row[i+1]) for i in range(len(row)-1)]

def first_failure_row(gaps, W):
    """Return the row index (0-based in A) where A_k(1) notin {0,2}, i.e.
    the first failure, or None if A_k(1) in {0,2} for all computed rows.
    Note: every row shrinks by 1, so we need the top row wide enough that
    the block reaches depth. We check A_k(1) for k = 1.. until width runs
    out."""
    row = build_from_gaps(gaps, W)
    width = len(row)
    for k in range(1, width):  # A_k has width-1 entries... A_k(1) exists
        row = diff_row(row)
        if len(row) <= 1:
            return None  # exhausted width, survived all reachable rows
        if row[1] not in (0, 2):
            return k, row[1]
    return None

def main():
    maxm = int(sys.argv[1]) if len(sys.argv) > 1 else 5  # positions after g_1
    W = int(sys.argv[2]) if len(sys.argv) > 2 else 40     # width of top row
    deaths = 0
    survivors = 0
    checked = 0
    first_death = None
    # g_1 = 2 fixed. For each assignment of gaps[2..maxm] in {2,4,6}.
    for tail in itertools.product([2, 4, 6], repeat=maxm):
        gaps = [2] + list(tail)
        # leftmost non-2 among positions >= 2 is a 4
        nz = [g for g in gaps[1:] if g != 2]
        if not nz or nz[0] != 4:
            continue
        checked += 1
        fr = first_failure_row(gaps, W)
        if fr is not None:
            deaths += 1
            if first_death is None:
                first_death = (gaps, fr)
            if deaths <= 15:
                print(f"DEATH gaps={gaps} first_failure_at_row={fr}")
        else:
            survivors += 1
    print("=" * 60)
    print(f"m={maxm} (trailing gap positions), W={W}")
    print(f"sequences checked (leftmost non-2 = 4): {checked}")
    print(f"survived to depth {W}: {survivors}")
    print(f"DEATHS: {deaths}")
    if first_death:
        print(f"first death: gaps={first_death[0]} at {first_death[1]}")
    else:
        print("no death found in this family/width")

if __name__ == "__main__":
    main()
