#!/usr/bin/env python3
"""Test whether the reachable-histogram language is LOCAL (a finite-state
automaton over consecutive level values). If the set of valid (a_k,a_{k+1})
consecutive pairs is small and fixed, then a weighted transfer DP over
historical sum (cells) can run in polynomial time to N=10000.

Report:
 1. The full set of consecutive transitions (a_k -> a_{k+1}) with multiplicities.
 2. Whether the valid-histogram set at each N can be reproduced by: a walk
    (0=a_0, ..., a_M=3) using ONLY the observed transition set. (Consistency
    test: are there walks using observed transitions but with wrong totals,
    i.e. is the transition set too loose / too tight?)
 3. Total cells constraint: sum = 2N+1. Are the end values always 3?
"""
import glob, collections

def sorted_key(p):
    return int(p.split('level_')[1].split('.')[0])

all_hists = {}   # N -> set of hist tuples
for path in sorted(glob.glob('data/level_*.txt'), key=sorted_key):
    n = sorted_key(path)
    hs = set()
    for line in open(path):
        hist, M, bbox = line.rstrip().split('|')
        hs.add(tuple(map(int, hist.strip().split())))
    all_hists[n] = hs

# 1. transition pairs
trans = collections.Counter()
for n, hs in all_hists.items():
    for h in hs:
        for k in range(len(h)-1):
            trans[(h[k], h[k+1])] += 1

print("Number of distinct consecutive (a_k,a_{k+1}) transitions:", len(trans))
print("Transitions (pair -> times):")
for p, c in sorted(trans.items()):
    print(f"   {p}  x{c}")

# start/end values
startv = collections.Counter()
endv = collections.Counter()
maxlen = 0
for n, hs in all_hists.items():
    for h in hs:
        startv[h[0]] += 1
        endv[h[-1]] += 1
        maxlen = max(maxlen, len(h))
print("\nstart values:", dict(startv))
print("end values:", dict(endv))
print("max histogram length (M+1):", maxlen)
