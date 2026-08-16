#!/usr/bin/env python3
"""Direct check at n=8: is there a pair with equal C_1..C_4 (cumulative) and
different S^2?  Imported table says K*(8)=4 => NO such pair.  Also print the
known e_6/e_5 witness and check its C vectors.
"""
import os, sys
from itertools import product
from lib.supply_fold import s_sos

def hist(h,L):
    n=len(h); size=1<<L; cnt=[0]*size
    for p in range(n-L+1):
        w=0
        for b in range(L): w=(w<<1)|h[p+b]
        cnt[w]+=1
    return tuple(cnt)

def S2(n,h):
    S,_=s_sos(n,h); return S*S

n=8
strings=[tuple(x) for x in product([0,1],repeat=n)]
s2={h:S2(n,list(h)) for h in strings}

# cumulative grouping
for K in [4,5]:
    g={}
    for h in strings:
        fsig=tuple(hist(h,L) for L in range(2,K+1))
        g.setdefault(fsig,set()).add(s2[h])
    const=all(len(v)==1 for v in g.values())
    nwitness=sum(1 for v in g.values() if len(v)>1)
    print("n=8 K=%d cumulative: const=%s witness-fibers=%d total-cells=%d"%(K,const,nwitness,len(g)))

# find an actual witness at K=4 if any
K=4
g={}
for h in strings:
    fsig=tuple(hist(h,L) for L in range(2,K+1))
    g.setdefault(fsig,[]).append((h,s2[h]))
for fsig,members in g.items():
    if len(set(s for _,s in members))>1:
        print("FOUND witness K=4: ", fsig)
        for h,ss in members[:6]: print("   h=", "".join(map(str,h)), "S2=", ss)
        break
else:
    print("NO witness at K=4 (const)")

# e6 vs e5
h=tuple([0,0,0,0,0,0,1,0]); hp=tuple([0,0,0,0,0,1,0,0])
print("e6 S2=", s2[h], "e5 S2=", s2[hp])
print("e6 C1..C4=", [hist(h,L) for L in range(2,5)])
print("e5 C1..C4=", [hist(hp,L) for L in range(2,5)])
