#!/usr/bin/env python3
"""Count DISTINCT level-histograms directly from data/level_N.txt files.

Each line: "a_0 a_1 ... a_M | M | dims".  The token list before the first
'|' IS the level histogram (tuple of #cubes at each level).  Count distinct
histograms per N from the raw feature dumps.  This re-derives the
distinct-histogram sequence independently of any BFS, straight from the
files on disk.
"""
import glob, collections
from lib.datafiles import sorted_key

for path in sorted(glob.glob('data/level_*.txt'), key=sorted_key):
    N = int(path.split('_')[1].split('.')[0])
    hs = set()
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            hist = line.split('|')[0].strip()
            hs.add(hist)
    print(f"N={N}: distinct_histograms={len(hs)}")
    if N <= 6:
        for h in sorted(hs):
            print("   ", h)
