#!/usr/bin/env python3
"""M-histograms at N=13 and N=14 for the 3D amoeba (Project Euler 763).

Drives the reachability BFS level by level from N=0 using the fixed-width
bitmask encoding from lib/amoeba.py (next_level_bits), exactly as
amoeba_extend.py does.  For the same configs this counts, it also records the
maximum level M = max(x+y+z) over the config's cubes, and prints/saves the
histogram of distinct configs grouped by M for N=13 and N=14.

Only the M-histogram is produced — the full config dumps are NOT written
(5.9M configs at N=14 would be tens of GiB).  The per-config M is computed
directly from the bitmask while iterating set bits, so no full decode/feature
objects are materialized.

Verification: the histogram totals must equal the independently established
D(13)=1749267 and D(14)=5949063.
"""

import sys
import time

from lib.amoeba import next_level_bits


def max_level_of(S, W):
    """Max level M = max(x+y+z) over the cubes of bitmask S (width W)."""
    W2 = W * W
    lv = 0
    m = S
    while m:
        low = m & -m
        i = low.bit_length() - 1
        m ^= low
        x, r = divmod(i, W2)
        y, z = divmod(r, W)
        k = x + y + z
        if k > lv:
            lv = k
    return lv


def main(max_n=14, hist_lo=13, hist_hi=14):
    W = max_n + 1  # fixed width; coords stay in [0,N] after N divisions
    level = {1}  # cube (0,0,0) at bit 0
    histograms = {}
    timings = {}
    total_start = time.time()
    for n in range(1, max_n + 1):
        t0 = time.time()
        level = next_level_bits(level, W)
        dt = time.time() - t0
        timings[n] = dt
        if hist_lo <= n <= hist_hi:
            h0 = time.time()
            hist = {}
            for S in level:
                M = max_level_of(S, W)
                hist[M] = hist.get(M, 0) + 1
            histograms[n] = hist
            dth = time.time() - h0
            total = sum(hist.values())
            print(f"N={n}: M-histogram computed in {dth:.1f}s, total {total}",
                  flush=True)
        else:
            print(f"D({n}) = {len(level):>12d}   (level in {dt:.2f}s)",
                  flush=True)
    total_elapsed = time.time() - total_start

    # Verify totals against independently established D(13), D(14).
    expected = {13: 1749267, 14: 5949063}
    lines = []
    for n in (hist_lo, hist_hi):
        hist = histograms[n]
        total = sum(hist.values())
        lines.append(f"N={n} total={total} expected={expected[n]} "
                     f"match={total == expected[n]}")
        for M in sorted(hist):
            lines.append(f"N={n} M={M}: {hist[M]}")
    lines.append(f"elapsed_total={total_elapsed:.2f}s")
    text = "\n".join(lines) + "\n"

    out_path = "/workspace/code/out/mhist_13_14.txt"
    with open(out_path, "w") as fh:
        fh.write(text)

    print("\n" + text)
    print("Level BFS timings (s):", {k: round(v, 3) for k, v in timings.items()})
    print(f"Wrote {out_path}")
    return histograms, timings, total_elapsed


if __name__ == "__main__":
    max_n = int(sys.argv[1]) if len(sys.argv) > 1 else 14
    histograms, timings, elapsed = main(max_n)
