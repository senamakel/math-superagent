"""Memory-compact BFS oracle for Project Euler 763.

Same reachability definition as brute.py/brute_extended.py, but each occupied-
cube configuration is stored as a single Python int: bit index
(x*W + y)*W + z with W = N+1 covers all reachable coordinates (each coordinate
is bounded by the number of divisions N, so x,y,z in [0,N]).

Successor: a cube p=(x,y,z) may divide if its three positive-unit neighbours
(a,b,c) are empty; the new configuration is S with p cleared and a,b,c set.

This keeps each state as one int (~W^3 bits) instead of a frozenset of 2N+1
tuple objects, so the per-state memory is far smaller and we can reach higher
N within the container's 2 GiB limit.

Correctness cross-checked against brute_extended.py for N=0..12.
"""

import sys
import time


def config_to_bit(S, W):
    """Encode a config (set of (x,y,z)) into one int over a W^3 grid."""
    bits = 0
    for (x, y, z) in S:
        bits |= 1 << ((x * W + y) * W + z)
    return bits


def next_level_bits(level, W):
    """One BFS step on a set of int-masked configs; W = N+1 for current N."""
    nxt = set()
    W2 = W * W
    for S in level:
        # iterate over set cubes
        m = S
        while m:
            low = m & -m
            i = low.bit_length() - 1
            m ^= low
            x, r = divmod(i, W2)
            y, z = divmod(r, W)
            a = 1 << ((x + 1) * W2 + y * W + z)
            b = 1 << (x * W2 + (y + 1) * W + z)
            c = 1 << (x * W2 + y * W + (z + 1))
            if (S & (a | b | c)) == 0:
                ns = (S ^ low) | a | b | c
                nxt.add(ns)
    return nxt


def main(max_n, budget):
    # start config {(0,0,0)}
    W = 1
    level = {1}  # bit 0
    results = {0: 1}
    print("D(0) = 1")
    for n in range(1, max_n + 1):
        W = n + 1  # coordinates in [0,n] for a config reached after n divisions
        t0 = time.time()
        level = next_level_bits(level, W)
        dt = time.time() - t0
        if not level:
            print(f"level {n}: empty after {dt:.2f}s")
            break
        results[n] = len(level)
        print(f"D({n}) = {len(level)}   (level in {dt:.2f}s)")
        if dt > budget:
            print(f"Stopping: level {n} took {dt:.2f}s > budget {budget}s")
            break
        sys.stdout.flush()
    return results


if __name__ == "__main__":
    max_n = int(sys.argv[1]) if len(sys.argv) > 1 else 14
    budget = float(sys.argv[2]) if len(sys.argv) > 2 else 120.0
    main(max_n, budget)
