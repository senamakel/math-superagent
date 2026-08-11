#!/usr/bin/env python3
"""Naive BFS oracle for the 3D amoeba problem, capped at MAX depth."""
import sys
import time


def neighbors(cell):
    x, y, z = cell
    return ((x + 1, y, z), (x, y + 1, z), (x, y, z + 1))


def division_states(state):
    out = set()
    cell_set = set(state)
    for cell in state:
        n1, n2, n3 = neighbors(cell)
        if n1 in cell_set or n2 in cell_set or n3 in cell_set:
            continue
        new = cell_set - {cell}
        new.add(n1)
        new.add(n2)
        new.add(n3)
        out.add(frozenset(new))
    return out


def main(max_depth):
    frontier = {frozenset({(0, 0, 0)})}
    results = [1]
    times = [0.0]
    print(f"max_depth={max_depth}", flush=True)
    for N in range(1, max_depth + 1):
        t0 = time.time()
        nxt = set()
        for st in frontier:
            nxt |= division_states(st)
        dt = time.time() - t0
        times.append(dt)
        results.append(len(nxt))
        print(f"N={N:3d}  D={len(nxt):10d}  from {len(frontier):9d} states  {dt:.2f}s",
              flush=True)
        frontier = nxt
    print("DONE", flush=True)


if __name__ == "__main__":
    main(int(sys.argv[1]))
