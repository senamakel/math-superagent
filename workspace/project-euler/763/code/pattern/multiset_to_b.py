#!/usr/bin/env python3
"""Build complete map: (multiset of level-counts) -> (n4, b) where
mult = 2^(2 n4) * 3^b.  Then print each distinct multiset with its b, so we
can hunt a closed form for b as a function of the multiset."""
import glob, collections
from lib.datafiles import sorted_key

def f23(v):
    a=b=0
    while v%2==0: v//=2; a+=1
    while v%3==0: v//=3; b+=1
    return a,b,v

seen=collections.OrderedDict()   # multiset -> (n4,b) (should be well-defined)
for path in sorted(glob.glob('data/level_*.txt'), key=sorted_key):
    n=sorted_key(path)
    per=collections.Counter()
    for line in open(path):
        hist,M,bbox=line.rstrip().split('|')
        per[hist.strip()]+=1
    for hist,m in per.items():
        vals=list(map(int,hist.split()))
        a,b,rest=f23(m)
        n4=vals.count(4)
        if rest==1 and a==2*n4:
            key=tuple(sorted(collections.Counter(vals).items()))
            seen[key]=(n4,b,hist)

# print with features: n1,n2,n3,n5,n6,n7, M(=len-1), b
print("multiset (value:count ...) | n1 n2 n3 n5 | b")
for key,(n4,b,hist) in seen.items():
    d=dict(key)
    n1=d.get(1,0);n2=d.get(2,0);n3=d.get(3,0);n5=d.get(5,0);n6=d.get(6,0);n7=d.get(7,0)
    vals=list(map(int,hist.split()))
    M=len(vals)-1
    print(f"{str(dict(key)):35s} | {n1:>2} {n2:>2} {n3:>2} {n5:>2} | M={M:>2} b={b}")
