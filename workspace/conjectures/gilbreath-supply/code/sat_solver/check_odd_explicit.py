#!/usr/bin/env python3
"""Independent explicit-witness check at odd n: exhibit a pair with equal
C_1..C_{floor(n/2)-1} and different S^2, and confirm NONE at K=floor(n/2).
Confirms K*(n)=floor(n/2) (largest witness K = floor(n/2)-1).
"""
import sys, os
from itertools import product
from lib.supply_fold import s_sos

def hist(h,L):
    n=len(h); size=1<<L; cnt=[0]*size
    for p in range(n-L+1):
        w=0
        for b in range(L): w=(w<<1)|h[p+b]
        cnt[w]+=1
    return tuple(cnt)
def CK(h,K): return tuple(hist(h,L) for L in range(2,K+2))
def S2(n,h): S,_=s_sos(n,list(h)); return S*S

for n in [7,9,11,13]:
    strings=[tuple(x) for x in product([0,1],repeat=n)]
    s2v={h:S2(n,h) for h in strings}
    Kmax= n//2 - 1   # expected largest witness K
    # exhibit witness at Kmax
    g={}
    for h in strings: g.setdefault(CK(h,Kmax),[]).append(h)
    shown=0
    for fsig,members in g.items():
        sset={s2v[h] for h in members}
        if len(sset)>1:
            a=members[0]
            for b in members:
                if s2v[b]!=s2v[a]:
                    print("n=%d K=%d witness S2: %d vs %d"%(n,Kmax,s2v[a],s2v[b]))
                    print("   h=%s  h'=%s" % ("".join(map(str,a)),"".join(map(str,b))))
                    shown+=1; break
        if shown: break
    # confirm no witness at Kmax+1
    Kc=Kmax+1
    g2={}
    for h in strings: g2.setdefault(CK(h,Kc),set()).add(s2v[h])
    const=all(len(v)==1 for v in g2.values())
    print("n=%d  largest-witness-K=%d (exhibited)  no-witness-at-K=%d (const): %s"
          %(n,Kmax,Kc,const))
    print()
