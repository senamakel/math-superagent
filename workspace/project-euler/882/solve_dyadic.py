#!/usr/bin/env python3
"""Compute the full-size S(N)=ceil(G(N)) where G(N)=sum_{k<=N} k*g(k),
g(k) dyadic CGT value of single-number bit-deletion game.
Direct O(N log N) iteration (polynomial), so N=1e5 is cheap.
"""
from fractions import Fraction
import sys, time
sys.setrecursionlimit(10**8)

def eval_g(maxk):
    g = {0: Fraction(0)}
    for k in range(1, maxk+1):
        s = bin(k)[2:]
        Lmx = None; Rmn = None
        for i, ch in enumerate(s):
            t = s[:i]+s[i+1:]
            y = 0 if t=='' else int(t,2)
            if ch=='1':
                v = g[y]
                if Lmx is None or v>Lmx: Lmx=v
            else:
                v = g[y]
                if Rmn is None or v<Rmn: Rmn=v
        # simplest dyadic strictly between Lmx and Rmn
        lo = Lmx; hi = Rmn
        val=None
        for n in range(0, 40):
            den = 1<<n
            if lo is None: m0=-1
            else:
                m0=(lo*den).numerator//(lo*den).denominator+1
                while Fraction(m0,den)<=lo: m0+=1
            if hi is None: m1=1<<40
            else:
                m1=(hi*den).numerator//(hi*den).denominator
                while Fraction(m1,den)>=hi: m1-=1
            if m1>=m0:
                val=Fraction(m0,den); break
        g[k]=val
    return g

from math import ceil
N=int(sys.argv[1]) if len(sys.argv)>1 else 100000
t=time.time()
g=eval_g(N)
G=Fraction(0)
for k in range(1,N+1):
    G += k*g[k]
print(f"N={N}, G(N)={G} = {float(G):.4f}")
print(f"S(N)=ceil(G)={ceil(G)}")
print(f"time={time.time()-t:.1f}s")
# save S sequence for small n for checking
print("\nS(n) for n=1..30:")
S=[]
G2=Fraction(0)
for n in range(1,31):
    G2+=n*g[n]; S.append(ceil(G2))
print(S)
