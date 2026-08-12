#!/usr/bin/env python3
"""Precisely characterize K(n) structure and its deviations, exact sympy.
K(n) = largest integer with sin(K*pi/n) - (K+n)*tan(pi/n)*cos(K*pi/n) < 0.
Questions:
 1. First n where K(n) != floor(3n/7)  (FALSIFIER of that conjecture).
 2. Full pattern of K(n) - floor(3n/7) over a range.
 3. Where first-difference differs from period-7 template [0,1,0,1,0,0,1].
 4. Is there a clean description: beats/losses sequence.
"""
import sympy as sp

def K_of_n(n):
    th = sp.pi / n
    tan_th = sp.tan(th)
    best = 0
    for k in range(0, n):
        if sp.sin(k*th) - (k+n)*tan_th*sp.cos(k*th) < 0:
            best = k
    return best

N = 1000
Ks = [K_of_n(n) for n in range(3, N+1)]
fl = [3*n//7 for n in range(3, N+1)]

# 1 & 2: deviation
dev = [(n, Ks[i]-fl[i]) for i,n in enumerate(range(3,N+1)) if Ks[i]!=fl[i]]
print("n where K(n)!=floor(3n/7): count=%d" % len(dev))
print("first 12:", dev[:12])
print("last 8:", dev[-8:])
md = max(d for _,d in dev)
print("max deviation:", md)

# group deviations by value
from collections import defaultdict
g = defaultdict(list)
for n,d in dev:
    g[d].append(n)
for d in sorted(g):
    print("deviation +%d at n=%s ..." % (d, g[d][:15]))

# 3: first-difference deviations from period-7 template
TEMPLATE=[0,1,0,1,0,0,1]
diffs=[Ks[i]-Ks[i-1] for i in range(1,len(Ks))]
ddev=[(n, diffs[i-1], TEMPLATE[(n-4)%7]) for i,n in enumerate(range(4,N+1)) if diffs[i-1]!=TEMPLATE[(n-4)%7]]
print("\nfirst-difference deviations from period-7 (n, actual, template):")
print("first 20:", ddev[:20])
print("count:", len(ddev))

# 4: characterize deviating n: is there arithmetic pattern? print gaps
devn=[n for n,_ in dev]
gaps=[devn[i+1]-devn[i] for i in range(len(devn)-1)]
print("\ndeviating-n gaps:", gaps[:60])
