#!/usr/bin/env python3
"""Exact even-parity counts of the PURE-BUMP ordering model.

The pure-bump (no-finish) race outcome here is taken to depend only on the
speed ORDER (a reduced model used as a combinatorial probe). CAUTION: this
model is REFUTED as an exact description of the real torpids race for n>=3
(it gives p(3,inf)=1/3, p(4,inf)=13/24 vs true 7/18, 19/36 from the exact
arrangement solver + MC). We compute its even counts anyway as an independent
mathematical sequence, clearly labelled NOT the race parity.
"""
import sys, itertools
from fractions import Fraction as F
sys.path.insert(0, "/workspace/code")

def pure_bump_parity(n, speeds):
    from exact_race import parity_of_new_order as pno
    state = [0]*n
    pos = [F(40)*j for j in range(n)]
    edges = [[] for _ in range(n)]
    while True:
        rowing = [j for j in range(n) if state[j]==0]
        if not rowing:
            break
        best = None
        for j in rowing:
            k = None
            for kk in range(j+1,n):
                if state[kk]==0:
                    k=kk; break
            if k is not None and speeds[j] > speeds[k]:
                ct = (pos[k]-pos[j])/(speeds[j]-speeds[k])
                if best is None or ct < best[0]:
                    best = (ct,j,k)
        if best is None:
            break
        _,j,k = best
        state[j]=2; pos[j]=pos[k]; edges[j].append(k)
    above = [set() for _ in range(n)]
    for i in range(n):
        seen={i}; st=[i]
        while st:
            u=st.pop()
            for w in edges[u]:
                if w not in seen: seen.add(w); st.append(w)
        above[i]=seen-{i}
    par,_ = pno(n, above)
    return par

def even_count(n):
    ev = 0
    for order in itertools.permutations(range(n)):
        speeds = [F(n-r) for r in range(n)].copy()
        # assign speed value (n-rank+1)?? realize decreasing order
        v = [None]*n
        for r, boat in enumerate(order):
            v[boat] = F(n-r)
        ev += (1 - pure_bump_parity(n, v))
    return ev

if __name__=="__main__":
    lo = int(sys.argv[1]) if len(sys.argv)>1 else 2
    hi = int(sys.argv[2]) if len(sys.argv)>2 else 8
    from math import factorial
    for n in range(lo, hi+1):
        ev = even_count(n)
        tot = factorial(n)
        print(f"n={n}: even={ev}/{tot}  p={F(ev,tot)}  odd={tot-ev}")
