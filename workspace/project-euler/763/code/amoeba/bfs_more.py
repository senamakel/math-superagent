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
a time budget (~90s) or the frontier exceeds ~2M states. We keep D(N) for
every N reached and write a fresh complete file D(0)..D(Nmax).

Correctness: the bit encoding was cross-checked in brute_bits.py against the
frozenset oracle (brute_extended.py, validated on D(2)=3 and D(10)=44499) for
N=0..12; this run must reproduce D(0..13) before reporting anything beyond.
"""

import sys
import time

from lib.amoeba import next_level_bits

MAX_STATES = 30_000_000
TIME_BUDGET = 90.0


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


if __name__ == "__main__":
    max_n = int(sys.argv[1]) if len(sys.argv) > 1 else 24
    budget = float(sys.argv[2]) if len(sys.argv) > 2 else TIME_BUDGET
    main(max_n, budget, "out/d_values_more.txt")
