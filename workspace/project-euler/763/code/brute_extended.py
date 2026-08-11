"""Extended BFS oracle for Project Euler 763.

Same definition as brute.py: an amoeba at p divides into three at the three
positive-unit neighbours, provided those are empty; the parent disappears.
D(N) = number of DISTINCT sets of occupied cubes reachable after exactly N
divisions.

This drives the BFS level by level from N=0 upward, recording D(N) for each
level, and stops when a single level takes longer than a time budget (or
grows too large). Exact set arithmetic; states are frozensets of cube tuples.

Correctness established by reproducing D(2)=3 and D(10)=44499 from the
statement before extending.
"""

import sys
import time

from lib.amoeba import next_level_fs

def main(max_n, level_time_budget):
    level = {frozenset({(0, 0, 0)})}
    results = {0: 1}
    print(f"D(0) = 1")
    for n in range(1, max_n + 1):
        t0 = time.time()
        level = next_level_fs(level)
        dt = time.time() - t0
        if not level:
            print(f"level {n}: empty (no states) after {dt:.2f}s")
            break
        results[n] = len(level)
        print(f"D({n}) = {len(level)}   (level computed in {dt:.2f}s)")
        if dt > level_time_budget:
            print(f"Stopping: level {n} took {dt:.2f}s > budget {level_time_budget}s")
            break
        sys.stdout.flush()
    return results


if __name__ == "__main__":
    max_n = int(sys.argv[1]) if len(sys.argv) > 1 else 12
    budget = float(sys.argv[2]) if len(sys.argv) > 2 else 60.0
    main(max_n, budget)
