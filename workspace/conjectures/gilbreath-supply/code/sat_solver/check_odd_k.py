#!/usr/bin/env python3
"""Verify the odd-n discrepancy: does the largest K with a witness pair equal
K*-1 where K* = min const on C_1..C_K fiber?

For each n, find directly the LARGEST K with a witness pair (equal C_1..C_K,
different S^2), by scanning K downward from n-2.  This is independent of the
'constancy' phrasing and directly exhibits pairs.
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

def CK(h,K):
    return tuple(hist(h,L) for L in range(2,K+2))

def S2(n,h):
    S,_=s_sos(n,list(h)); return S*S

def run():
    print("n : minConstK  largestWitnessK (=minConst-1 expected)  ceil(n/2)")
    for n in range(4, 14):
        strings=[tuple(x) for x in product([0,1],repeat=n)]
        s2v={h:S2(n,h) for h in strings}
        # min K const
        minconst=None
        for K in range(1,n):
            g={}
            for h in strings: g.setdefault(CK(h,K),set()).add(s2v[h])
            if all(len(v)==1 for v in g.values()): minconst=K; break
        # largest K with a witness pair (scan down)
        maxwit=None
        for K in range(n-2,0,-1):
            g={}
            for h in strings: g.setdefault(CK(h,K),set()).add(s2v[h])
            if any(len(v)>1 for v in g.values()): maxwit=K; break
        print("n=%2d  minConst=%s  largestWitnessK=%s   ceil=%d" %
              (n,minconst,maxwit,(n+1)//2))
    return 0

if __name__=="__main__":
    sys.exit(run())
