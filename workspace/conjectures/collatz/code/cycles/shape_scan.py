"""Bounded exact scan of the Böhm--Sontacchi shape numerator.

This is an oracle only: it enumerates compositions for L<=16,m<=5 and
reports integer formula values. It does not address arbitrary Collatz cycles.
"""
from fractions import Fraction
from itertools import combinations

def compositions(L, m):
    for cuts in combinations(range(1, L), m-1):
        pts=(0,)+cuts+(L,)
        yield tuple(pts[i+1]-pts[i] for i in range(m))

def value(L,m,g):
    v=0; s=0
    for j in range(m):
        if j: s += g[j-1]
        v += 3**(m-1-j)*2**s
    return Fraction(v, 2**L-3**m)

hits=[]; total=0
for L in range(1,17):
    for m in range(1,min(5,L)+1):
        row=[]
        for g in compositions(L,m):
            total += 1
            x=value(L,m,g)
            if x.denominator==1:
                hits.append((L,m,g,int(x)))
        row.append((L,m))
print('shapes scanned:', total)
print('integer hits:', hits)
print('nontrivial positive hits:', [h for h in hits if h[3]>0 and h[3]!=1])
