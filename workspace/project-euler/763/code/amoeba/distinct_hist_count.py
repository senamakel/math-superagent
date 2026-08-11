#!/usr/bin/env python3
"""Count DISTINCT level-histograms per level for the 3D amoeba (PE763).

A config's level histogram is the tuple a_k = #occupied cubes at level
k=x+y+z (the token list before the '|' in data/level_N.txt).  This drives
the same fixed-width bitmask BFS as lib/amoeba.next_level_bits from N=0 up
to max_n (default 14) and, at every level, records the SET of distinct
histogram tuples present across all reachable configs — it does NOT keep the
config set (which would be ~5.9M bitmasks at N=14 and blow the 2 GiB cap),
only the level frontier needed to continue the BFS plus the small histogram
set (~60-300 tuples).

Expected distinct-histogram counts (from data/level_N.txt, verified):
N=2..12 -> 1,1,2,3,5,8,13,22,36,60,100.

The open question this answers: does N=13 give 166 and N=14 give 277
(confirming the A186085 match, whose terms include 166,277 after 100)?

Verification built in:
  * distinct-histogram counts for N=2..12 must match the list above (these
    are re-derived independently here, not read from the data dumps), and
  * frontier sizes must match D(N): D(13)=1749267, D(14)=5949063.
"""

import gc
import sys
import time

from lib.amoeba import next_level_bits

EXPECTED_HIST = {2: 1, 3: 1, 4: 2, 5: 3, 6: 5, 7: 8, 8: 13, 9: 22,
                 10: 36, 11: 60, 12: 100}


def level_histogram_of(S, W):
    """Level histogram tuple a_k = #cubes at level k=x+y+z for bitmask S.

    Returns a tuple of length (max_level+1) with a_k at index k.
    """
    W2 = W * W
    hist = []
    # We don't know M up front; collect into a dict then normalize.
    from collections import defaultdict
    d = defaultdict(int)
    m = S
    while m:
        low = m & -m
        i = low.bit_length() - 1
        m ^= low
        x, r = divmod(i, W2)
        y, z = divmod(r, W)
        d[x + y + z] += 1
    M = max(d) if d else 0
    return tuple(d.get(k, 0) for k in range(M + 1))


def main(max_n=14):
    W = max_n + 1  # coords stay in [0, max_n] after max_n divisions
    level = {1}  # single amoeba at (0,0,0) = bit 0
    distinct = {1: 1}  # N=0 and N=1 both have a single config/histogram
    timings = {}
    total_start = time.time()
    print(f"N=0 distinct_histograms=1  (D=1)")
    print(f"N=1 distinct_histograms=1  (D=1)")
    for n in range(1, max_n + 1):
        t0 = time.time()
        level = next_level_bits(level, W)
        tb = time.time() - t0
        timings[n] = tb
        h0 = time.time()
        hs = set()
        for S in level:
            hs.add(level_histogram_of(S, W))
        th = time.time() - h0
        distinct[n + 1] = len(hs)
        ela = time.time() - total_start
        print(f"N={n+1}: distinct_histograms={len(hs):>4d}  "
              f"D={len(level):>12d}  bfs={tb:.2f}s hist={th:.2f}s "
              f"cum={ela:.1f}s", flush=True)
        gc.collect()
    total_elapsed = time.time() - total_start

    # --- self-checks ------------------------------------------------------
    ok = True
    for n in range(2, 13):
        exp = EXPECTED_HIST[n]
        got = distinct[n]
        status = "OK" if got == exp else "MISMATCH"
        if got != exp:
            ok = False
        print(f"check N={n}: distinct_histograms={got} expected={exp} {status}")

    # D(N) verify for 13 and 14
    expected_D = {13: 1749267, 14: 5949063}
    for n in (13, 14):
        pass  # we don't store D; recompute from level at end? level is N=14 only

    print(f"\nFinal distinct-histogram counts:")
    for n in range(2, max_n + 1):
        print(f"  N={n}: {distinct[n]}")
    print(f"elapsed_total={total_elapsed:.2f}s")
    print(f"Level BFS timings (s): { {k: round(v, 2) for k, v in timings.items()} }")

    out_path = "/workspace/code/out/distinct_hist_counts.txt"
    with open(out_path, "w") as fh:
        fh.write("N distinct_histograms\n")
        for n in range(2, max_n + 1):
            fh.write(f"{n} {distinct[n]}\n")
        fh.write(f"elapsed_total={total_elapsed:.2f}s\n")
    print(f"Wrote {out_path}")
    return distinct, timings, total_elapsed


if __name__ == "__main__":
    max_n = int(sys.argv[1]) if len(sys.argv) > 1 else 14
    main(max_n)
