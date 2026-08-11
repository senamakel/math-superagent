#!/usr/bin/env python3
"""Naive BFS oracle for the 3D amoeba problem, capped at MAX depth.

Same definition as code/brute.py but drives levels up to a max-depth argument
and stops when the frontier exceeds 600_000 states, printing the full D(N)
sequence and the checks D(2)=3, D(10)=44499. Exponential state space; only for
tiny N as a definition check.
"""
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
        # stop if states grow too numerous to keep resident
        if len(frontier) > 600_000:
            print(f"stopping: frontier {len(frontier)} states too numerous", flush=True)
            break
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
    print(f"\nChecks: D(2)={results[2]} (expect 3), D(10)={results[10]} (expect 44499)")
    print("Full sequence:", results)


if __name__ == "__main__":
    main(int(sys.argv[1]))
