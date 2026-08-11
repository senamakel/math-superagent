"""Push the exact BFS for Project Euler 763 as far as feasible with bit encoding.

Reachability: an amoeba at (x,y,z) divides into three at the positive-unit
neighbours, provided those three are empty; the parent disappears. After N
divisions there are 2N+1 amoebas. D(N) = number of DISTINCT sets of occupied
cubes reachable after exactly N divisions.

Each configuration is a single Python int: bit index (x*W + y)*W + z with a
FIXED W for every level, so a cube has the same bit regardless of level
(a config after n divisions has each coordinate in [0,n], so W = max_n+1
covers all levels and the encoding never changes).

The one-step successor next_level_bits is imported from lib/amoeba.py, the
single shelved definition; it is not duplicated here.

We drive level-by-level from N=0 upward, stopping when a single level exceeds
a time budget or the frontier exceeds a state-count guard. We keep D(N) for
every N reached and write a fresh complete file D(0)..D(Nmax).

Correctness: the bit encoding was cross-checked in brute_bits.py against the
frozenset oracle (brute_extended.py, validated on D(2)=3 and D(10)=44499) for
N=0..12; this run must reproduce D(0..13) before reporting anything beyond.

Memory note: each configuration is one Python int whose value has bit length
up to W^3 (W fixed across the run). At N=15 the frontier holds ~2e7 such ints
(~10-12 GB), at N=16 ~7e7 (~35 GB) which exceeds RAM, so N=15 is the practical
ceiling for this representation. State count, not wall time, is the binding
constraint once past N=14.
"""

import sys
import time

from lib.amoeba import next_level_bits

MAX_STATES = 40_000_000
TIME_BUDGET = 470.0


def main(max_n, budget, out_path):
    W = max_n + 1  # fixed grid width for every level
    level = {1}    # cube (0,0,0) at bit 0
    results = [1]  # D(0) = 1
    print("D(0) = 1", flush=True)

    stop_reason = "max_n reached"
    for n in range(1, max_n + 1):
        if len(level) > MAX_STATES:
            stop_reason = f"level {n-1} frontier {len(level)} > {MAX_STATES} states"
            break
        t0 = time.time()
        level = next_level_bits(level, W)
        dt = time.time() - t0
        if not level:
            stop_reason = f"level {n} empty (no states) after {dt:.2f}s"
            break
        results.append(len(level))
        print(f"D({n}) = {len(level)}   (level {n-1}->{n} in {dt:.2f}s, "
              f"{len(level)} states)", flush=True)
        if dt > budget:
            stop_reason = f"level {n} took {dt:.2f}s > budget {budget}s"
            break

    Nmax = len(results) - 1
    with open(out_path, "w") as f:
        for n, d in enumerate(results):
            f.write(f"D({n})={d}\n")
    print(f"\nStopped: {stop_reason}")
    print(f"Max N reached: {Nmax}")
    print("Full sequence D(0)..D(Nmax):", results)
    print(f"Wrote {out_path}", flush=True)
    return results


def next_level_compact(level, W):
    """One BFS step. `level` is a set of ints, each encoded with grid width W
    (coords in [0, W-1]). Returns children encoded with grid width W+1, so
    the encoding grows level by level — coords reach n only after n steps,
    keeping every int as short as it can be.

    A parent cell p may divide only if its three positive-unit neighbours are
    empty. Neighbours with any coordinate == W are automatically not occupied
    (a parent at level W-1 has all coords <= W-1... here W == n+1 for a state
    at level n, so no parent cell reaches coordinate W). A neighbour with all
    coords < W must be checked against the parent's own bits.
    """
    Wp = W + 1          # child grid width
    Wp2 = Wp * Wp
    W2 = W * W
    nxt = set()
    for S in level:
        # collect parent cells as (x,y,z)
        cells = []
        m = S
        while m:
            low = m & -m
            i = low.bit_length() - 1
            m ^= low
            x, r = divmod(i, W2)
            y, z = divmod(r, W)
            cells.append((x, y, z))
        # occupancy quick-lookup in parent's W encoding
        def occ(x, y, z):
            return (S >> (x * W2 + y * W + z)) & 1
        for (x, y, z) in cells:
            a = (x + 1, y, z)
            b = (x, y + 1, z)
            c = (x, y, z + 1)
            free = True
            for (nx, ny, nz) in (a, b, c):
                if nx < W and ny < W and nz < W and occ(nx, ny, nz):
                    free = False
                    break
            if not free:
                continue
            # rebuild child in Wp encoding: keep all parent cells except p,
            # add the three neighbours
            child = 0
            for (cx, cy, cz) in cells:
                if (cx, cy, cz) == (x, y, z):
                    continue
                child |= 1 << (cx * Wp2 + cy * Wp + cz)
            for (nx, ny, nz) in (a, b, c):
                child |= 1 << (nx * Wp2 + ny * Wp + nz)
            nxt.add(child)
    return nxt


def main_compact(max_n, budget, out_path, max_states):
    """Drives level-by-level using the compact per-level encoding."""
    level = {1}                 # cube (0,0,0), W = 1
    W = 1                       # grid width for level 0
    results = [1]
    print("D(0) = 1", flush=True)
    stop_reason = "max_n reached"
    for n in range(1, max_n + 1):
        if len(level) > max_states:
            stop_reason = f"frontier {len(level)} at level {n-1} > {max_states}"
            break
        t0 = time.time()
        level = next_level_compact(level, W)  # level n has grid width W = n
        W += 1
        dt = time.time() - t0
        if not level:
            stop_reason = f"level {n} empty after {dt:.2f}s"
            break
        results.append(len(level))
        print(f"D({n}) = {len(level)}   (level {n-1}->{n} in {dt:.2f}s, "
              f"{len(level)} states)", flush=True)
        if dt > budget:
            stop_reason = f"level {n} took {dt:.2f}s > budget {budget}s"
            break
        with open(out_path, "w") as f:
            for k, d in enumerate(results):
                f.write(f"D({k})={d}\n")
    Nmax = len(results) - 1
    with open(out_path, "w") as f:
        for k, d in enumerate(results):
            f.write(f"D({k})={d}\n")
    print(f"\nStopped: {stop_reason}")
    print(f"Max N reached: {Nmax}")
    print("Full sequence D(0)..D(Nmax):", results)
    print(f"Wrote {out_path}", flush=True)
    return results


if __name__ == "__main__":
    max_n = int(sys.argv[1]) if len(sys.argv) > 1 else 24
    budget = float(sys.argv[2]) if len(sys.argv) > 2 else TIME_BUDGET
    max_states = int(sys.argv[3]) if len(sys.argv) > 3 else MAX_STATES
    main_compact(max_n, budget, "out/d_values_more.txt", max_states)
