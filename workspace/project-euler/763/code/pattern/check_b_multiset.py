#!/usr/bin/env python3
"""Characterize b (the 3-exponent) in mult(hist)=2^(2*n4)*3^b.
1) Is b uniquely determined by the multiset of values (counts of 1,2,3,4,5)?
2) If two histograms share the same value-counts but differ in b, arrangement matters.
Print all (valuecounts -> set of b) where the set has size>1, i.e. arrangement matters."""
import glob, collections
from lib.datafiles import sorted_key

def f23(v):
    a=b=0
    while v%2==0: v//=2; a+=1
    while v%3==0: v//=3; b+=1
    return a,b,v

groups=collections.defaultdict(set)
examples=collections.defaultdict(list)
precise=[]   # (n, hist, b)
for path in sorted(glob.glob('data/level_*.txt'), key=sorted_key):
    n=sorted_key(path)
    per=collections.Counter()
    for line in open(path):
        hist,M,bbox=line.rstrip().split('|')
        per[hist.strip()]+=1
    for hist,m in per.items():
        a,b,rest=f23(m)
        if rest!=1:  # skip the 30 (has factor 5)
            continue
        vals=list(map(int,hist.split()))
        n4=vals.count(4)
        # check consistency: a should be 2*n4
        if a!=2*n4:
            continue
        key=tuple(sorted(collections.Counter(vals).items()))
        groups[key].add(b)
        examples[key].append((n,hist,b))
        precise.append((n,hist,b))

multi=[k for k,v in groups.items() if len(v)>1]
print(f"Distinct value-count multisets: {len(groups)}; those giving >1 different b (arrangement matters): {len(multi)}")
for k in multi[:30]:
    print("  ",k, sorted(groups[k]))
    for e in examples[k][:4]:
        print("      ",e)
