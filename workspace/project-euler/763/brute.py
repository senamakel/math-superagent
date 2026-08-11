#!/usr/bin/env python3
"""Naive but obviously-correct BFS oracle for the 3D amoeba problem.

Amoeba at (0,0,0). A division picks one occupied cell (x,y,z), and if the
three forward neighbors (x+1,y,z), (x,y+1,z), (x,y,z+1) are all empty,
removes that cell and adds the three. After N divisions there are 2N+1 cells.

We BFS over sets of occupied cells (frozensets), depth by depth, discarding
duplicates, and record the number of distinct states reachable at each depth N.
"""

from collections import defaultdict
import time


def neighbors(cell):
    x, y, z = cell
    return ((x + 1, y, z), (x, y + 1, z), (x, y, z + 1))


def division_states(state):
    """Return all distinct states reachable from `state` by one division."""
    out = set()
    cell_set = set(state)
    for cell in state:
        n1, n2, n3 = neighbors(cell)
        if n1 in cell_set or n2 in cell_set or n3 in cell_set:
            continue  # a forward neighbor is occupied, division not allowed
        new = cell_set - {cell}
        new.add(n1)
        new.add(n2)
        new.add(n3)
        out.add(frozenset(new))
    return out


def main():
    start = {(0, 0, 0)}
    frontier = {frozenset(start)}  # states at current depth
    results = [1]                  # D(0) = 1
    times = [0.0]

    N = 0
    while frontier:
        t0 = time.time()
        N += 1
        nxt = set()
        for st in frontier:
            nxt |= division_states(st)
        dt = time.time() - t0
        times.append(dt)
        results.append(len(nxt))
        print(f"N={N:3d}  D={len(nxt):10d}  (from {len(frontier):10d} "
              f"states, frontier time {dt:.2f}s, total states explored {sum(len(_) for _ in [])})")
        frontier = nxt
        if len(nxt) == 0:
            break

    print("\nFull sequence D(N):")
    for n, d in enumerate(results):
        print(f"  D({n:2d}) = {d}")

    print("\nChecks:")
    print(f"  D(2)  = {results[2]}  (expected 3)      -> {'OK' if results[2] == 3 else 'FAIL'}")
    if len(results) > 10:
        print(f"  D(10) = {results[10]}  (expected 44499) -> {'OK' if results[10] == 44499 else 'FAIL'}")


if __name__ == "__main__":
    main()
