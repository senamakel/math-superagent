#!/usr/bin/env python3
"""Characterize the reachable-histogram structure: consecutive differences,
start/end values, and whether a simple 'smooth composition' transfer rule
reproduces the histogram set exactly."""
import glob, collections

def sorted_key(p):
    return int(p.split('level_')[1].split('.')[0])

all_hists = {}   # N -> set of hist tuple (a_0=0,...,a_M)
for path in sorted(glob.glob('data/level_*.txt'), key=sorted_key):
    n = sorted_key(path)
    hs = set()
    for line in open(path):
        hist, M, bbox = line.rstrip().split('|')
        t = tuple(map(int, hist.strip().split()))
        hs.add(t)
    all_hists[n] = hs

print("== start/end values and max-jump analysis over all reachable histograms N=2..12")
maxjump_global = 0
maxval_global = 0
for n in sorted(all_hists):
    hs = all_hists[n]
    maxjump = 0
    maxval = 0
    ends = collections.Counter()
    for h in hs:
        assert h[0] == 0, h
        ends[h[-1]] += 1
        maxval = max(maxval, max(h))
        for k in range(len(h)-1):
            maxjump = max(maxjump, abs(h[k+1]-h[k]))
    maxjump_global = max(maxjump_global, maxjump)
    maxval_global = max(maxval_global, maxval)
    print(f"N={n}: #hists={len(hs)}  max_jump={maxjump}  max_levelval={maxval}  end_values={dict(ends)}")

print("\nGlobal max jump over consecutive levels:", maxjump_global)
print("Global max level-value:", maxval_global)

# For each histogram, list the positive jumps (up-steps) allowed.
print("\n== sample histograms and their consecutive differences (N=6)")
hs6 = sorted(all_hists[6])
for h in hs6:
    diffs = [h[k+1]-h[k] for k in range(len(h)-1)]
    print(" ", h, " diffs=", diffs)
