#!/usr/bin/env python3
"""Determine the exact 3-adic and 5-adic valuation of every q in Phi.
Claim (from residue computation): every reduced q = num/den in Phi has
num divisible by 3 (with full denominator coprime) and by 5.  Find the exact
min valuation and whether q always has v3>=?, v5>=?."""
from math import gcd
from collections import Counter

def phi_pairs(M):
    out = set()
    for m in range(2, M+1):
        m2=m*m
        for n in range(1,m):
            num=4*m*n*(m2-n*n); den=(m2+n*n)**2
            g=gcd(num,den)
            out.add((num//g, den//g))
    return out

def vp(x,p):
    v=0
    while x%p==0:
        x//=p; v+=1
    return v

for p in [2,3,5,7]:
    pairs = phi_pairs(200)
    dist_v = Counter()
    for num,den in pairs:
        dist_v[vp(num,p)-vp(den,p)] += 1
    print(f"p={p}: valuation distribution over Phi(200): "
          f"{dict(sorted(dist_v.items()))}")
