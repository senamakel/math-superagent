#!/usr/bin/env python3
"""For each N in 2..10 (data dumps), count how many configs realize each
distinct level-histogram. Print the multiset of 'configs per histogram'
values, so we can look for structure in how D(N) refines into histograms
(histogram count = A186085 = H(N), sum_of_counts-per-hist = D(N))."""
import glob, collections

def sorted_key(p):
    return int(p.split('level_')[1].split('.')[0])

for path in sorted(glob.glob('data/level_*.txt'), key=sorted_key):
    n = sorted_key(path)
    per = collections.Counter()
    for line in open(path):
        hist, M, bbox = line.rstrip().split('|')
        per[hist] += 1
    vals = sorted(per.values())
    # summarize: histogram count H(n), D(n), and the multiset of per-histogram multiplicities
    H = len(per)
    D = sum(per.values())
    # group multiplicities by value
    mdist = sorted(collections.Counter(per.values()).items())
    print(f"N={n}: H={H} D={D}  per-histogram multiset={mdist}")
