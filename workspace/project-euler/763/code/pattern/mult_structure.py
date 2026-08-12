#!/usr/bin/env python3
"""Study per-histogram multiplicities:
1) list distinct histograms and multiplicities
2) check whether ALL multiplicities are 2^a*3^b (pure smooth) or whether other
   primes appear; tabulate non-3-smooth ones.
3) for subdiagonal M=N-1, list histograms + multiplicities, sum vs R(N,N-1).
"""
import glob, collections
from math import gcd
from lib.datafiles import sorted_key

def plist(v):
    d=2; f=collections.Counter()
    while d*d<=v:
        while v%d==0: v//=d; f[d]+=1
        d+=1
    if v>1: f[v]+=1
    return f

seen_non235 = []
for path in sorted(glob.glob('data/level_*.txt'), key=sorted_key):
    n=sorted_key(path)
    per=collections.Counter()
    for line in open(path):
        hist,M,bbox=line.rstrip().split('|')
        per[(hist,int(M))]+=1
    # group by M
    byM=collections.defaultdict(list)
    for (hist,M),m in per.items():
        byM[M].append((hist,m))
    print(f"===== N={n}  D={sum(per.values())} =====")
    for M in sorted(byM):
        tot=sum(m for _,m in byM[M])
        print(f"  M={M}: {len(byM[M])} histograms, total={tot}")
        if M==n-1:  # subdiagonal detail
            for hist,m in sorted(byM[M]):
                fac=plist(m); other=[p for p in fac if p not in (2,3)]
                print(f"      {hist} -> {m}  {dict(fac)}{'  <<<NON235 '+str(other) if other else ''}")
    # non-2,3 primes anywhere
    for (hist,M),m in per.items():
        fac=plist(m)
        if any(p not in (2,3) for p in fac):
            seen_non235.append((n,hist,m,dict(fac)))
print("\n===== ALL multiplicities with a prime factor other than 2 or 3 =====")
for row in seen_non235:
    print(" ", row)
