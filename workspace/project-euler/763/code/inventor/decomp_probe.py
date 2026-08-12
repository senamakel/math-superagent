#!/usr/bin/env python3
"""Full structural decomposition of 3D amoeba reachable configs, N=2..12.

For each N it lists, per reachable config, the structural features needed to
build a compressed counting DP:
  - max level M
  - f(C) = #dividable cells (cells with none of their children in C)
  - level histogram a_k = #cells at level k
Then it tabulates the decomposition of D(N) by
  (a) M, (b) f, (c) joint (M,f), (d) level histogram count/distribution.

Uses the memory-compact bitmask BFS (fixed width W=N+1) from lib/amoeba
next_level_bits to reach N=12; configs are decoded transiently for feature
extraction so it fits under the 2 GiB cgroup cap.

Exact arithmetic.  Output goes to /workspace/scratchpad/structure_probe.txt
and is also printed.

Complexity: forward BFS over distinct configs -- exponential state set (the
oracle), bounded here at N=12 (~514k states).
"""
import time
from collections import defaultdict

from lib.amoeba import next_level_bits, decode_bits, children, lvl, f_of


def hist_key(S):
    f = {}
    M = 0
    for p in S:
        k = sum(p)
        f[k] = f.get(k, 0) + 1
        if k > M:
            M = k
    return tuple(f.get(k, 0) for k in range(M + 1)), M


def main(max_n=12):
    W = max_n + 1
    level = {1}
    out_lines = []
    print(f"{'N':>2} {'D(N)':>9} {'#A1bad':>7} {'#A2bad':>7} {'#A3bad':>7} "
          f"{'Bmatch':>7}")
    for n in range(0, max_n + 1):
        if n == 0:
            D = 1
            level = {1}
        else:
            t0 = time.time()
            level = next_level_bits(level, W)
        # decode once per config
        features = []
        for S in level:
            cells = decode_bits(S, W)
            features.append(cells)
        D = len(features)
        print(f"  decoded level {n}: D={D}", flush=True)

        if n == 0:
            continue

        # ---- claim checks (A1,A2,A3) on this level ----
        a1bad = a2bad = a3bad = 0
        for cells in features:
            Sset = set(cells)
            M = max(lvl(p) for p in Sset)
            top = [p for p in Sset if lvl(p) == M]
            if len(top) != 3:
                a1bad += 1
            # A2: top == full child triangle of a single EMPTY point p at M-1
            caps = [p for p in Sset if lvl(p) == M - 1 and
                    set(children(p, 3)) == set(top)]
            if len(caps) != 1:
                a2bad += 1
            # A3: deterministic cap-collapse to {origin} in n steps
            ok, steps = collapse_to_origin(cells, M)
            if not ok or steps != n:
                a3bad += 1

        # ---- decomposition ----
        M_counts = defaultdict(int)
        f_counts = defaultdict(int)
        joint = defaultdict(int)
        hist_counts = defaultdict(int)
        for cells in features:
            Sset = set(cells)
            M = max(lvl(p) for p in Sset)
            fv = f_of(cells)
            hk, _ = hist_key(cells)
            M_counts[M] += 1
            f_counts[fv] += 1
            joint[(M, fv)] += 1
            hist_counts[hk] += 1

        seg = []
        seg.append(f"N={n} D={D} A1bad={a1bad} A2bad={a2bad} A3bad={a3bad}")
        seg.append(f"  by M: {dict(sorted(M_counts.items()))}")
        seg.append(f"  by f: {dict(sorted(f_counts.items()))}")
        seg.append("  joint (M,f):")
        for (M, fv) in sorted(joint):
            seg.append(f"    M={M} f={fv}: {joint[(M,fv)]}")
        seg.append(f"  #distinct histograms={len(hist_counts)}")
        seg.append("  most frequent histograms (hist->count):")
        for h, c in sorted(hist_counts.items(), key=lambda kv: -kv[1])[:10]:
            seg.append(f"    {h}: {c}")
        seg.append("")
        text = "\n".join(seg)
        print(text)
        out_lines.append(text)

    with open('/workspace/scratchpad/structure_probe.txt', 'w') as fh:
        fh.write("\n".join(out_lines) + "\n")
    print("\nWrote /workspace/scratchpad/structure_probe.txt")


def collapse_to_origin(cells, M0=None):
    """Deterministic unique-cap collapse to {origin}; return (ok, steps)."""
    Sset = set(cells)
    steps = 0
    while Sset != {(0, 0, 0)}:
        M = max(lvl(p) for p in Sset)
        top = [p for p in Sset if lvl(p) == M]
        caps = [p for p in Sset if lvl(p) == M - 1 and
                set(children(p, 3)) == set(top)]
        if len(caps) != 1:
            return False, steps
        p = caps[0]
        Sset = (Sset - set(children(p, 3))) | {p}
        steps += 1
    return True, steps


if __name__ == "__main__":
    main()
