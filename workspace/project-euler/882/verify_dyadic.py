#!/usr/bin/env python3
"""Independent verification of G(N)=sum_{k<=N} k*g(k), separate code path."""
from fractions import Fraction
from math import ceil
import sys, time

def one_deletions(x):
    if x==0: return []
    s=bin(x)[2:]; out=set()
    for i,ch in enumerate(s):
        if ch=='1':
            t=s[:i]+s[i+1:]; out.add(0 if t=='' else int(t,2))
    return out
def zero_deletions(x):
    if x==0: return []
    s=bin(x)[2:]; out=set()
    for i,ch in enumerate(s):
        if ch=='0':
            t=s[:i]+s[i+1:]; out.add(0 if t=='' else int(t,2))
    return out

def eval_g2(maxk):
    g={0:Fraction(0)}
    for k in range(1,maxk+1):
        L=[g[j] for j in one_deletions(k)]
        R=[g[j] for j in zero_deletions(k)]
        lo=max(L) if L else None
        hi=min(R) if R else None
        for n in range(0,40):
            den=1<<n
            if lo is None: m0=0
            else:
                m0=(lo*den).numerator//(lo*den).denominator+1
                while Fraction(m0,den)<=lo: m0+=1
            if hi is None: m1=1<<60
            else:
                m1=(hi*den).numerator//(hi*den).denominator
                while Fraction(m1,den)>=hi: m1-=1
            if m1>=m0:
                g[k]=Fraction(m0,den); break
    return g

N=int(sys.argv[1])
t=time.time()
g=eval_g2(N)
tot=Fraction(0)
for k in range(1,N+1):
    tot+=k*g[k]
print(f"N={N}")
print(f"G(N) = {tot.numerator} / {tot.denominator}")
print(f"G(N) float = {float(tot):.4f}")
print(f"S(N)=ceil = {ceil(tot)}")
print(f"time={time.time()-t:.1f}s")
