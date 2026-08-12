#!/usr/bin/env python3
"""Dump the distinct level-histograms of the 3D amoeba for N in 2..10.

A config's level histogram is a_k = #cubes at level k=x+y+z.  We drive the
same fixed-width bitmask BFS as lib/amoeba.next_level_bits and, per level,
print every distinct histogram tuple.  This is a small sidecar to study the
structure behind the finding that distinct-histogram counts match OEIS
A186085 (1D smooth/sandpile compositions).

Correctness: same BFS semantics as distinct_hist_count.py; the histogram
tuple here equals the token list before '|' in data/level_N.txt records.
"""

from lib.amoeba import next_level_bits


def hist_of(S, W):
    from collections import defaultdict
    d = defaultdict(int)
    W2 = W * W
    m = S
    while m:
        low = m & -m
        i = low.bit_length() - 1
        m ^= low
        x, r = divmod(i, W2)
        y, z = divmod(r, W)
        d[x + y + z] += 1
    M = max(d) if d else 0
    return tuple(d.get(k, 0) for k in range(M + 1))


def main(max_n=10):
    W = max_n + 1
    level = {1}
    print("N=0:", [(1,)])
    for n in range(1, max_n + 1):
        level = next_level_bits(level, W)
        hs = {hist_of(S, W) for S in level}
        print(f"N={n}: count={len(hs)}")
        for h in sorted(hs):
            print("   ", h, "  sum=", sum(h))


if __name__ == "__main__":
    main()
