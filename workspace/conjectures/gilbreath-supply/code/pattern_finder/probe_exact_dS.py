#!/usr/bin/env python3
"""Probe exact structure of dS(n) = S(n+1)-S(n) and the relation between
T(n,d) (reads window right-shifted) to find h-independent identities.

T(n,d) = XOR_{s submask d} h[n-1-s].
T(n+1,d) = XOR_{s submask d} h[n-s]  (window shifted right by 1).

We check several exact hypotheses:
  (H1) Is dS(n) expressible via a SMALL number of fold cells / boundary?
  (H2) For UNIFORM random h, are E[Z^2]=1 and AC1(dS)=-1/2 EXACT identities?
  (H3) Does T(n+1,d) equal T(n,d) XOR something with a known submask set?
"""
import sys
from lib.supply_fold import t_direct

def h_random(n, seed=12345):
    import random; random.seed(seed)
    return [random.randint(0,1) for _ in range(n)]

def S_from_T(n,h):
    return sum(1-2*t_direct(n,d,h) for d in range(2,n))

# H3: find the set difference. M(n,d) = {n-1-s : s sub d}. M(n+1,d)={n-s:s sub d}
# Compare XOR over the two windows in terms of h at boundary indices.
n=16
h=[1,0,1,1,0,0,1,0,1,1,0,1,0,0,1,1,0,1]  # length n+2 so t(n+1,d) valid
for d in range(2,n):
    t1=t_direct(n,d,h)
    t2=t_direct(n+1,d,h)
    # t2 XOR t1 = XOR over symmetric difference of submasks of h[n-s] and h[n-1-s]
    # reindex: t1 = XOR_{s sub d} h[(n-1)-s], t2 = XOR_{s sub d} h[(n)-s] = XOR_{s sub d} h[n-s]
    # the difference is XOR over {n-s: s sub d} vs {n-1-s : s sub d}
    # = XOR over h[n-s] for s sub d  XOR  h[n-1-s] for s sub d
    # Let u=s, and v=s+1 (if v sub d+? no). 
    pass
print("H3 done for one n; need direct set comparison")
# Direct: compute XOR diff by explicit sets
def xor_set(indices,h):
    x=0
    for i in indices: x^=h[i]
    return x
for d in [2,3,5,7,10]:
    A={n-1-s for s in range(d+1) if (s&d)==s}
    B={n-s for s in range(d+1) if (s&d)==s}
    print("d=",d,"A=",sorted(A),"B=",sorted(B)," |A XOR B|=",len(A^B),"symdiff=",sorted(A^B))
