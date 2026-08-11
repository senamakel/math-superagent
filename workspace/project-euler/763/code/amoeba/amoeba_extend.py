#!/usr/bin/env python3
"""Extended BFS oracle + structural-feature dump for Project Euler 763.

Drives the reachability BFS level by level from N=0 upward using the fixed-
width bitmask encoding from lib/amoeba.py, recording D(N) at each level, and
stops when the frontier exceeds `cap` states (any level).  For each level N in
[dump_lo, dump_hi] it decodes every distinct config and writes its structural
features to /workspace/data/level_N.txt: one line per config with
   level_hist_as_spaced_list | M | dims
where dims = (dx, dy, dz) of the bounding box.

Features are what GOAL.md/MEMORY.md call for: the level histogram a_k (#cubes
with x+y+z == k), the bounding box dims, #cells per level, and max level M.

Use from lib import so the replay of the BFS and the feature extraction are
the same verified code in both the oracle and the data dumps.

Correctness: reproduces D(2)=3, D(10)=44499, D(12)=514419, D(13)=1749267.
"""

import os
import sys
import time

from lib.amoeba import decode_bits, next_level_bits, feature_record

OUT_DIR = "/workspace/data"


def dump_features(level, W, N):
    """Decode every config in `level` and write its feature record to file."""
    path = os.path.join(OUT_DIR, f"level_{N}.txt")
    t0 = time.time()
    with open(path, "w") as fh:
        for S in level:
            cells = decode_bits(S, W)
            a, M, dims = feature_record(cells)
            hist = " ".join(str(v) for v in a)
            fh.write(f"{hist} | {M} | {dims[0]} {dims[1]} {dims[2]}\n")
    dt = time.time() - t0
    print(f"  dumped {len(level)} configs -> {path} ({dt:.2f}s)", flush=True)


def main(max_n=16, cap=5_000_000, dump_hi=12, dump_lo=2):
    os.makedirs(OUT_DIR, exist_ok=True)
    W = max_n + 1  # fixed width; coords stay in [0,N] after N divisions
    level = {1}  # cube (0,0,0) at bit 0
    results = {0: 1}
    frontier_sizes = {0: 1}
    times = {}
    print(f"max_n={max_n} cap={cap} dump range [{dump_lo},{dump_hi}]", flush=True)
    print("D(0) = 1")
    stop_reason = "reached max_n"
    for n in range(1, max_n + 1):
        t0 = time.time()
        level = next_level_bits(level, W)
        dt = time.time() - t0
        times[n] = dt
        if not level:
            print(f"level {n}: empty after {dt:.2f}s", flush=True)
            stop_reason = f"empty at {n}"
            results[n] = 0
            break
        results[n] = len(level)
        frontier_sizes[n] = len(level)
        print(f"D({n}) = {len(level):>12d}   (level computed in {dt:.2f}s)",
              flush=True)
        if dump_lo <= n <= dump_hi:
            dump_features(level, W, n)
        if len(level) > cap:
            stop_reason = f"frontier {len(level)} > cap {cap} at level {n}"
            print(f"Stopping: {stop_reason}", flush=True)
            break
        sys.stdout.flush()
    print(f"\nStop reason: {stop_reason}", flush=True)
    return results, frontier_sizes, times, stop_reason


if __name__ == "__main__":
    max_n = int(sys.argv[1]) if len(sys.argv) > 1 else 16
    cap = int(sys.argv[2]) if len(sys.argv) > 2 else 5_000_000
    dump_hi = int(sys.argv[3]) if len(sys.argv) > 3 else 12
    dump_lo = int(sys.argv[4]) if len(sys.argv) > 4 else 2
    results, fs, times, reason = main(max_n, cap, dump_hi, dump_lo)
    print("\nD(N) sequence:", [results[i] for i in sorted(results) if i in results])
    print("Frontier sizes:", [fs[i] for i in sorted(fs)])
    print("Level times (s):", {k: round(v, 3) for k, v in times.items()})
