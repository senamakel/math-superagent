"""Push the exact BFS for Project Euler 763 as far as feasible with compact bit encoding.

Reachability: an amoeba at (x,y,z) divides into three at the positive-unit
neighbours, provided those three cubes are empty; the parent disappears. After
N divisions there are 2N+1 amoebas. D(N) = number of DISTINCT sets of occupied
cubes reachable after exactly N divisions.

Compact bit encoding: each configuration is a Python int whose bits index
cells by (x*W + y)*W + z with W = (current level)+1. Because a config reached
after n divisions has every coordinate in [0,n], the per-level width W=n+1
keeps every int as small as possible (vs a fixed max width, which wastes
~K^3 bits per state at large K). Children are re-encoded at width W+1.

We drive level-by-level from N=0 upward, stopping on a time budget (~300s
per level) or a state-count cap. D(N) for every N reached is written to a
fresh complete file D(0)..D(Nmax).

Correctness: reproduces the established sequence D(2)=3, D(10)=44499,
D(13)=1749267 and extends D(14)=5949063, exactly matching the fixed-width
bit oracle for N=0..14.
"""

import sys
import time

DEFAULT_MAX = 14
DEFAULT_BUDGET = 300.0
DEFAULT_MAX_STATES = 3_000_000


def next_level_compact(level, W):
    """One BFS step. `level` is a set of int state-masks, each encoded with
    grid width W (cells with coords in [0, W-1]). Returns the children encoded
    with grid width W+1, so the encoding grows with the level and every int
    stays as short as possible.
    """
    Wp = W + 1
    Wp2 = Wp * Wp
    W2 = W * W
    nxt = set()
    for S in level:
        # gather parent cells (x, y, z)
        cells = []
        m = S
        while m:
            low = m & -m
            i = low.bit_length() - 1
            m ^= low
            x, r = divmod(i, W2)
            y, z = divmod(r, W)
            cells.append((x, y, z))

        def occ(x, y, z):
            return (S >> (x * W2 + y * W + z)) & 1

        for (x, y, z) in cells:
            a = (x + 1, y, z)
            b = (x, y + 1, z)
            c = (x, y, z + 1)
            free = True
            for (nx, ny, nz) in (a, b, c):
                # a neighbour with any coord == W is outside the parent grid
                # (cannot be occupied); otherwise check the parent's bits
                if nx < W and ny < W and nz < W and occ(nx, ny, nz):
                    free = False
                    break
            if not free:
                continue
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
    """Drive level-by-level with the compact per-level encoding."""
    level = {1}           # cube (0,0,0), grid width 1
    W = 1
    results = [1]         # D(0) = 1
    print("D(0) = 1", flush=True)
    stop_reason = "max_n reached"
    for n in range(1, max_n + 1):
        if len(level) > max_states:
            stop_reason = f"frontier {len(level)} at level {n-1} > {max_states}"
            break
        t0 = time.time()
        level = next_level_compact(level, W)   # level n uses grid width W = n
        W += 1
        dt = time.time() - t0
        if not level:
            stop_reason = f"level {n} empty after {dt:.2f}s"
            break
        results.append(len(level))
        print(f"D({n}) = {len(level):>10}   (level {n-1}->{n} took "
              f"{dt:8.2f}s, {len(level):,} states)", flush=True)
        if dt > budget:
            stop_reason = f"level {n} took {dt:.2f}s > budget {budget}s"
            break
        # write incrementally so a crash keeps what has been reached
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
    max_n = int(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_MAX
    budget = float(sys.argv[2]) if len(sys.argv) > 2 else DEFAULT_BUDGET
    max_states = int(sys.argv[3]) if len(sys.argv) > 3 else DEFAULT_MAX_STATES
    main_compact(max_n, budget, "out/d_values_more.txt", max_states)
