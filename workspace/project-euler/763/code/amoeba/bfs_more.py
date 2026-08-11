"""Push the exact BFS for Project Euler 763 as far as feasible with bit encoding.

Reachability: an amoeba at p=(x,y,z) may divide into three at the positive-unit
neighbours (x+1,y,z), (x,y+1,z), (x,y,z+1) provided those three cubes are
empty; the parent disappears. After N divisions a config holds 2N+1 cubes,
each coordinate in [0,N]. D(N) = number of DISTINCT sets of occupied cubes
reachable after exactly N divisions.

Each configuration is a single Python int: bit index (x*W + y)*W + z. The
compact encoding lets W grow level by level (a config at level n uses W = n+1,
so every int is as short as it can be and no fixed maximum width is reserved).
A config at level n has coords in [0,n], so grid width W=n+1 always holds it,
and the parent cells of a level-n config never reach coordinate W.

We drive level-by-level from N=0 upward, stopping when a single level exceeds a
time budget or the frontier exceeds a state-count guard. We keep D(N) for every
N reached and write a fresh complete file D(0)..D(Nmax) to code/out/.

Correctness: this encoding must reproduce the established sequence D(0..14) =
1,1,3,9,30,99,336,1134,3855,13086,44499,151263,514419,1749267,5949063 (the
first two are the statement's worked examples D(2)=3, D(10)=44499) before any
level beyond 14 is reported. The fixed-width version was cross-checked against
the frozenset oracle for N=0..12; the compact and fixed-width versions must
agree on every level both can produce.

Memory note: at level n the frontier configs are Python ints of ~(n+1)^3 bits.
N=15 ~ 2e7 states (~10-12 GB), N=16 ~ 7e7 (~40 GB+) — the practical ceiling for
this representation is N=15 or 16 depending on RAM. State count, not wall time,
is the binding constraint past N=14.
"""

import os
import sys
import time

MAX_STATES = 40_000_000
TIME_BUDGET = 470.0

_HERE = os.path.dirname(os.path.abspath(__file__))
_OUT = os.path.join(_HERE, "..", "out", "d_values_more.txt")


def decode_cells(S, W):
    """Decode an int (grid width W) into a list of (x,y,z) tuples."""
    cells = []
    W2 = W * W
    m = S
    while m:
        low = m & -m
        i = low.bit_length() - 1
        m ^= low
        x, r = divmod(i, W2)
        y, z = divmod(r, W)
        cells.append((x, y, z))
    return cells


def next_level_compact(level, W):
    """One BFS step. `level` is a set of ints encoded with grid width W (all
    coords < W). Returns children encoded with grid width W+1.

    A parent cell p=(x,y,z) divides iff its three positive-unit neighbours are
    empty. A neighbour with any coordinate == W cannot be occupied (every cell
    has coords < W); one with all coords < W must be checked against the
    parent's own bits.
    """
    Wp = W + 1
    Wp2 = Wp * Wp
    W2 = W * W
    nxt = set()
    for S in level:
        cells = []
        m = S
        while m:
            low = m & -m
            i = low.bit_length() - 1
            m ^= low
            x, r = divmod(i, W2)
            y, z = divmod(r, W)
            cells.append((x, y, z))
        for (x, y, z) in cells:
            a = (x + 1, y, z)
            b = (x, y + 1, z)
            c = (x, y, z + 1)
            free = True
            for (nx, ny, nz) in (a, b, c):
                if nx < W and ny < W and nz < W and \
                   ((S >> (nx * W2 + ny * W + nz)) & 1):
                    free = False
                    break
            if not free:
                continue
            # child = parent cells (drop p) + the three neighbours, in Wp grid
            child = 1 << (a[0] * Wp2 + a[1] * Wp + a[2])
            child |= 1 << (b[0] * Wp2 + b[1] * Wp + b[2])
            child |= 1 << (c[0] * Wp2 + c[1] * Wp + c[2])
            for (cx, cy, cz) in cells:
                if (cx, cy, cz) == (x, y, z):
                    continue
                child |= 1 << (cx * Wp2 + cy * Wp + cz)
            nxt.add(child)
    return nxt


def main(max_n, budget, out_path, max_states):
    level = {1}            # cube (0,0,0), grid width W = 1
    W = 1
    results = [1]
    print("D(0) = 1", flush=True)
    stop_reason = "max_n reached"
    for n in range(1, max_n + 1):
        if len(level) > max_states:
            stop_reason = f"frontier {len(level)} at level {n-1} > {max_states}"
            break
        t0 = time.time()
        level = next_level_compact(level, W)   # level n encoded with W=n+1
        W += 1
        dt = time.time() - t0
        if not level:
            stop_reason = f"level {n} empty after {dt:.2f}s"
            break
        results.append(len(level))
        print(f"D({n}) = {len(level):>12,}   (level {n-1}->{n} took "
              f"{dt:8.2f}s, {len(level):,} states)", flush=True)
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
    out = sys.argv[4] if len(sys.argv) > 4 else _OUT
    main(max_n, budget, out, max_states)
