#!/usr/bin/env python3
"""Verify the conjectured closed form for per-histogram multiplicity:
  mult(hist) = 2^(2*n4) * 3^(n1 + n2 + n3 - 1)
where nk = number of entries equal to k in the level-histogram.
Check against ALL data N=2..12. Report every exception.
"""
import glob, collections

def sorted_key(p):
    return int(p.split('level_')[1].split('.')[0])

exceptions=[]
tot=0
for path in sorted(glob.glob('data/level_*.txt'), key=sorted_key):
    n=sorted_key(path)
    per=collections.Counter()
    for line in open(path):
        hist,M,bbox=line.rstrip().split('|')
        per[hist.strip()]+=1
    for hist,m in per.items():
        tot+=1
        vals=list(map(int,hist.split()))
        cnt=collections.Counter(vals)
        n1=cnt[1]; n2=cnt[2]; n3=cnt[3]; n4=cnt[4]
        pred=2**(2*n4) * 3**(n1+n2+n3-1)
        if pred!=m:
            exceptions.append((n,hist,m,pred))
print(f"Total histograms: {tot}; exceptions: {len(exceptions)}")
for e in exceptions:
    print("  ",e)
