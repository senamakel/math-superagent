#!/usr/bin/env python3
"""For each histogram, compare multiplicity (#configs) vs number of distinct
bboxes.  Hypothesis to test: does the config-count-per-histogram equal the
count of distinct side-length tuples (i.e. is the shape's multiplicity the
number of realized bounding boxes)? Also tabulate the bbox multiset per hist."""
import glob, collections
from lib.datafiles import sorted_key

for path in sorted(glob.glob('data/level_*.txt'), key=sorted_key):
    n = sorted_key(path)
    per = collections.Counter()          # hist -> #configs
    bb = collections.defaultdict(collections.Counter)  # hist -> bbox -> count
    for line in open(path):
        hist, M, bbox = line.rstrip().split('|')
        per[hist] += 1
        bb[hist][bbox.strip()] += 1
    bad = 0
    print(f"===== N={n} =====")
    for hist, m in sorted(per.items(), key=lambda kv:-kv[1]):
        nbb = len(bb[hist])
        same = (nbb == m)
        if not same: bad += 1
        flag = "" if same else f"   <<< mult({m}) != #bbox({nbb})"
        if not same or n <= 6:
            print(f"  {hist.strip():30s} mult={m:6d}  nbbox={nbb}{flag}")
    if bad: print(f"  -- {bad}/{len(per)} histograms where mult != #bbox")
    print()
