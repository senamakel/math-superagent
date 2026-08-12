#!/usr/bin/env python3
"""Per-histogram multiplicities at N=13 and N=14 for the 3D amoeba (PE763).

Drives the reachability BFS level by level from N=0 using the fixed-width
bitmask encoding from lib/amoeba.py (next_level_bits), exactly as
amoeba_extend.py / mhist_13_14.py do.  For each config in the N=13 and N=14
frontiers it computes the LEVEL HISTOGRAM a_k = #cubes at level k=x+y+z
and accumulates a Counter mapping histogram-tuple -> number of configs that
realize it.  The full histograms AND their multiplicities are written to
/workspace/code/out/per_hist_mult_13_14.txt.

The level histogram is computed directly from the bitmask by iterating set
bits (no full decode/feature objects materialized), so the only held state
beyond the frontier is the small Counter (<= 277 distinct histograms at
N=14, matching the A186085 distinct-histogram count).

Verification: the sum of multiplicities per N must equal the independently
established D(13)=1749267 and D(14)=5949063.
"""

import sys
import gc
import time
from collections import Counter

from lib.amoeba import next_level_bits


def level_hist_of(S, W):
    """Level histogram a_k = #cubes at level k=x+y+z of bitmask S (width W).

    Iterates the set bits of S, adding 1 to hist[x+y+z].  Since every
    reachable N-config has cells only at levels 0..N, the tuple is
    hist[0..max_present] — but we return it as a full-length tuple
    hist[0..N] via the caller passing W-1, so histograms of different configs
    share one common length and hash consistently.  (The caller passes
    max_level = W-1 to normalise length.)
    """
    W2 = W * W
    hist = [0] * (W)  # caller passes W = max_level+1 so indices 0..max_level
    m = S
    while m:
        low = m & -m
        i = low.bit_length() - 1
        m ^= low
        x, r = divmod(i, W2)
        y, z = divmod(r, W)
        hist[x + y + z] += 1
    return tuple(hist)


def main(max_n=14, hist_lo=13, hist_hi=14):
    W = max_n + 1  # fixed width; coords stay in [0,N] after N divisions
    level = {1}  # cube (0,0,0) at bit 0
    histograms = {}   # n -> Counter(histogram_tuple -> multiplicity)
    timings = {}      # n -> BFS step seconds
    hist_timings = {} # n -> histogram-pass seconds
    total_start = time.time()

    for n in range(1, max_n + 1):
        t0 = time.time()
        level = next_level_bits(level, W)
        dt = time.time() - t0
        timings[n] = dt

        if hist_lo <= n <= hist_hi:
            h0 = time.time()
            cnt = Counter()
            for S in level:
                h = level_hist_of(S, W)
                cnt[h] += 1
            histograms[n] = cnt
            dth = time.time() - h0
            hist_timings[n] = dth
            total = sum(cnt.values())
            print(f"N={n}: {total} configs -> "
                  f"{len(cnt)} distinct histograms in {dth:.1f}s",
                  flush=True)
        else:
            print(f"D({n}) = {len(level):>12d}   (level in {dt:.2f}s)",
                  flush=True)

        # Free the previous level's histogram (if any) and collect transient
        # garbage from the step transition to keep peak memory under the
        # container's ~2 GiB cgroup cap during the N=14 frontier (5.9M).
        gc.collect()

    total_elapsed = time.time() - total_start

    # Verify totals against independently established D(13), D(14).
    expected = {13: 1749267, 14: 5949063}
    lines = []
    for n in (hist_lo, hist_hi):
        cnt = histograms[n]
        total = sum(cnt.values())
        ok = total == expected[n]
        lines.append(f"N={n} total={total} expected={expected[n]} "
                     f"match={ok} n_distinct_hist={len(cnt)}")
        for h in sorted(cnt):
            lines.append(f"N={n} hist={' '.join(map(str, h))} "
                         f"mult={cnt[h]}")
    lines.append(f"elapsed_total={total_elapsed:.2f}s")
    text = "\n".join(lines) + "\n"

    out_path = "/workspace/code/out/per_hist_mult_13_14.txt"
    with open(out_path, "w") as fh:
        fh.write(text)

    print("\n" + text)
    print("Level BFS timings (s):", {k: round(v, 3) for k, v in timings.items()})
    print("Histogram-pass timings (s):",
          {k: round(v, 3) for k, v in hist_timings.items()})
    print(f"Wrote {out_path}")
    return histograms, timings, hist_timings, total_elapsed


if __name__ == "__main__":
    max_n = int(sys.argv[1]) if len(sys.argv) > 1 else 14
    histograms, timings, hist_timings, elapsed = main(max_n)
