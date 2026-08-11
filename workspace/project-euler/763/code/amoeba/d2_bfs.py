"""Clean exact BFS for the 2D amoeba (PE763 in d=2).

One step: an amoeba at (x,y) divides into two at (x+1,y) and (x,y+1) provided
both are empty; the parent disappears.  D2(N) = number of DISTINCT sets of
occupied cubes reachable after exactly N divisions.

Uses the compact per-level int-bitmask encoding from lib/amoeba2d (grid width
W = current level, so every int stays short).  State space in d=2 grows much
more slowly than d=3, so we can push well past the d=3 ceiling of N=14.

Validated at small N by hand and by a frozenset oracle before running large.
"""

import sys
import time

from lib.amoeba2d import next_level_bits2_compact


def main_2d(max_n, budget, out_path, max_states):
    level = {1}          # (0,0), grid width 1
    W = 1
    results = [1]        # D2(0) = 1
    print("D2(0) = 1", flush=True)
    stop_reason = "max_n reached"
    for n in range(1, max_n + 1):
        if len(level) > max_states:
            stop_reason = f"frontier {len(level)} at level {n-1} > {max_states}"
            break
        t0 = time.time()
        level = next_level_bits2_compact(level, W)
        W += 1
        dt = time.time() - t0
        if not level:
            stop_reason = f"level {n} empty after {dt:.2f}s"
            break
        results.append(len(level))
        print(f"D2({n}) = {len(level):>10}   (level {n-1}->{n} took "
              f"{dt:8.2f}s, {len(level):,} states)", flush=True)
        if dt > budget:
            stop_reason = f"level {n} took {dt:.2f}s > budget {budget}s"
            break
        with open(out_path, "w") as f:
            for k, d in enumerate(results):
                f.write(f"D2({k})={d}\n")
    Nmax = len(results) - 1
    with open(out_path, "w") as f:
        for k, d in enumerate(results):
            f.write(f"D2({k})={d}\n")
    print(f"\nStopped: {stop_reason}")
    print(f"Max N reached: {Nmax}")
    print("Full sequence D2(0)..D2(Nmax):", results)
    print(f"Wrote {out_path}", flush=True)
    return results


if __name__ == "__main__":
    max_n = int(sys.argv[1]) if len(sys.argv) > 1 else 50
    budget = float(sys.argv[2]) if len(sys.argv) > 2 else 600.0
    max_states = int(sys.argv[3]) if len(sys.argv) > 3 else 50_000_000
    out_path = sys.argv[4] if len(sys.argv) > 4 else "out/d2_values.txt"
    main_2d(max_n, budget, out_path, max_states)
