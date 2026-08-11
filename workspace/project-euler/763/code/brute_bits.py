"""Memory-compact BFS oracle for Project Euler 763.

Same reachability definition as brute.py / brute_extended.py, but each
occupied-cube configuration is stored as a single Python int: bit index
(x*W + y)*W + z with a FIXED W (>= max coordinate) used for every level, so a
given cube maps to the same bit regardless of level.

A config reached after exactly n divisions has 2n+1 cubes, each coordinate in
[0,n]. So W = max_n + 1 covers all levels 0..max_n, and crucially the encoding
does NOT change between levels.

Successor: a cube p=(x,y,z) may divide if its three positive-unit neighbours
(a,b,c) are empty; the new configuration is S with p cleared and a,b,c set.

The one-step successor next_level_bits is imported from lib/amoeba.py, the
single shelved definition; it is not duplicated here.

Correctness cross-checked against brute_extended.py (the frozenset oracle, itself
validated on D(2)=3 and D(10)=44499) for N=0..12.
"""

import sys
import time

from lib.amoeba import next_level_bits


def main(max_n, budget):
    W = max_n + 1  # fixed grid width for all levels
    level = {1}  # cube (0,0,0) at bit 0
    results = {0: 1}
    print("D(0) = 1")
    for n in range(1, max_n + 1):
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
