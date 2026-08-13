#!/usr/bin/env python3
"""Verify the analytic proof that every q = f(m,n) = 4mn(m^2-n^2)/(m^2+n^2)^2
in Phi has v2(q) >= 3 and v3(q) >= 1 (for primitive m>n>=1), and confirm the
bound numerators/denominators combinatorially over all primitive pairs.

Proof sketch:
  numerator N = 4mn(m^2-n^2).  Denominator D = (m^2+n^2)^2.
  For primitive m>n, m,n not both odd?  Primitive means gcd(m,n)=1.
  v2: if one of m,n even (they can't both be even, primitive), say n even,
      then 4mn has v2 = 2 + v2(n) >= 3, and D is odd in that case (m odd,
      n even -> m^2+n^2 odd).  So v2(N/D) >= 3.  If both m,n odd (primitive,
      both odd is allowed), then m^2-n^2 is even: (odd)^2-(odd)^2 divisible by
      8 (difference of squares of odds = mult of 8); 4mn has v2=2, m^2-n^2
      has v2>=3, D = (m^2+n^2)^2 with m^2+n^2 even (odd+odd) -> v2(D) = 2*v2(m^2+n^2).
      N has v2 = 2 + v2(m^2-n^2) >= 2+3 = 5, D has v2 = 2*v2(m^2+n^2).  Need
      v2(N)-v2(D) >= 3.  For both odd: m^2+n^2 ≡ 2 mod 4, so v2(m^2+n^2)=1,
      D v2 = 2.  N v2 >= 5 -> v2(N/D) >= 3.  Good.
  v3: N = 4mn(m-n)(m+n).  Among m,n,m-n,m+n (mod 3), for primitive pair: if 3|m
      then 3∤n and factor m has 3 (need m^2-n^2 = (m-n)(m+n) not zero mod 3,
      which it isn't since m≠±n mod 3 when 3|m,3∤n); if 3∤m,3∤n then either
      m≡n or m≡-n -> one of (m-n),(m+n) div by 3.  Either way N div by 3.
      D = (m^2+n^2)^2: is m^2+n^2 ever div by 3 for primitive pair?  Squares
      mod 3 ∈{0,1}; m^2+n^2≡0 mod3 requires both div by 3, impossible primitive
      (would mean 3|m,3|n).  So 3∤D.  Hence v3(N/D) = v3(N) >= 1.
These are proofs.  This script just confirms the valuations numerically."""
from math import gcd
from fractions import Fraction
from collections import Counter

def vp(x,p):
    c=0
    while x%p==0:
        x//=p; c+=1
    return c

def f_frac(m,n):
    num=4*m*n*(m*m-n*n); den=(m*m+n*n)**2
    g=gcd(num,den)
    return Fraction(num//g, den//g)

M=400
minv2=10**9; minv3=10**9
all_v2_ge3=True; all_v3_ge1=True
checked=0
v2dist=Counter(); v3dist=Counter()
for m in range(2,M+1):
    for n in range(1,m):
        if gcd(m,n)!=1:
            continue
        q=f_frac(m,n)
        num,den=q.numerator,q.denominator
        v2=v2dist if False else (vp(num,2)-vp(den,2))
        v3v=vp(num,3)-vp(den,3)
        v2dist[vp(num,2)-vp(den,2)]+=1
        v3dist[v3v]+=1
        if v2<3: all_v2_ge3=False
        if v3v<1: all_v3_ge1=False
        checked+=1
print(f"primitive pairs m<=n<=400 checked: {checked}")
print(f"ALL q in Phi have v2(q)>=3: {all_v2_ge3}   (min v2 = {min(v2dist)}), "
      f"v2 distribution: {dict(sorted(v2dist.items()))}")
print(f"ALL q in Phi have v3(q)>=1: {all_v3_ge1}   (min v3 = {min(v3dist)}), "
      f"v3 distribution: {dict(sorted(v3dist.items()))}")
