#!/usr/bin/env python3
"""
Level-structure analysis of the 3D PE763 amoeba from data/level_N.txt.

Data format (one line per reachable config at step N):
    'level-histogram | maxlevel M | bbox dx dy dz'
where the histogram is h_0 .. h_M (count of cells at level k=x+y+z).

Fired-per-level f: f_0 = 1,  h_l = 3*f_{l-1} - f_l  (l>=1),  f_M = 0.
Interpretation: f_l = number of cells at level l that fired (divided); each
fired cell at level l-1 produces 3 children at level l, of which f_l fire again
(disappear) so h_l = 3 f_{l-1} - f_l stays occupied.
Consequences: sum_l f_l = N (one division per fired cell), sum_l h_l = 2N+1.

Tasks:
 (a) confirm h_M = 3 always (max level holds exactly 3 cells).
 (b) build histogram-shape -> count table for N=2..12.
 (c) analyse whether per-histogram config count tensorizes / follows a
     transfer-matrix recurrence across levels.
"""
import sys
import os
from collections import defaultdict
from fractions import Fraction

def parse_line(line):
    hs, ms, bs = line.split('|')
    hist = tuple(int(x) for x in hs.split())
    M = int(ms)
    bbox = tuple(int(x) for x in bs.split())
    return hist, M, bbox

def fired_from_hist(hist):
    """Recover f_0..f_M from h, with f_0 = 1 and f_M = 0 check.
    f_0=1, h_l = 3 f_{l-1} - f_l  =>  f_l = 3 f_{l-1} - h_l."""
    M = len(hist) - 1
    f = [1]
    for l in range(1, M + 1):
        f.append(3 * f[l-1] - hist[l])
    return f  # f[M] should be 0

def main():
    Ns = range(2, 13)
    big_tables = {}

    for N in Ns:
        path = f"data/level_{N}.txt"
        if not os.path.exists(path):
            print(f"[skip] {path} missing")
            continue
        # (hist -> count), (hist -> set of bboxes / count), hist->M check
        hcount = defaultdict(int)
        hM_bad = 0
        hE_bad = 0   # fired relation violations
        hsum_bad = 0 # sum f != N, sum h != 2N+1
        hline = 0
        with open(path) as fh:
            for line in fh:
                line = line.strip()
                if not line:
                    continue
                hist, M, bbox = parse_line(line)
                hline += 1
                if hist[M] != 3:
                    hM_bad += 1
                f = fired_from_hist(hist)
                if f[M] != 0:
                    hE_bad += 1
                if sum(f) != N or sum(hist) != 2*N + 1:
                    hsum_bad += 1
                hcount[hist] += 1
        n_configs = hline  # should equal D(N)
        big_tables[N] = hcount
        print(f"== N={N}: {n_configs} configs, {len(hcount)} distinct histograms")
        print(f"   h_M==3 violations: {hM_bad}; fired-relation violations: {hE_bad}; "
              f"sum-f/sum-h violations: {hsum_bad}")
        # save the hist->count table
        out = f"data/hist_counts_{N}.txt"
        with open(out, "w") as fh:
            for hist in sorted(hcount):
                fh.write(f"{' '.join(map(str,hist))}  count={hcount[hist]}\n")
        print(f"   wrote {out}")

    # Print the raw tables for a few representative small N
    print("\n===== RAW hist->count tables (small N) =====")
    for N in [3, 4, 5]:
        print(f"\n-- N={N} --")
        for hist in sorted(big_tables[N]):
            print(f"   h={' '.join(map(str,hist))}  count={big_tables[N][hist]}")

if __name__ == "__main__":
    main()
