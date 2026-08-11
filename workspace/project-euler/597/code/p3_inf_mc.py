#!/usr/bin/env python3
"""Exact p(3, infinity): integrate over the unit simplex {v0,v1,v2>=0,
v0+v1+v2=1} with NO finishes (L=infinite), using the exact rational dynamic
on exact rational interior points of arrangement cells. Density 2 (n=3).

Bumps are the only events. Cell = region of constant outcome under all
separating lines (v_a=v_b and equality of catch times). We enumerate cells by
sampling many exact rational interior points -> but to be EXACT we partition
the triangle by the separating lines and sum cell areas. For n=3 there are only
3 catch events: 0->1, 1->2, 2(none), and 0->2 after 1 out. Equality of two
catch times is a line. We subdivide by these lines exactly.

Simpler exact approach for the limit: the outcome is piecewise constant; we
subdivide the triangle by the full line set and integrate each cell exactly as
in the finite-L case, using a huge L in the exact race? That cheats (L huge
still has finish lines). Instead we REWRITE the race with no finish: only bumps.
Use exact_race-like dynamics without finish candidates."""
import sys, os
from fractions import Fraction as F
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from brute import parity_of_new_order

def nofinish_parity(n, speeds):
    """Pure bump race, exact rationals, no finishes."""
    state=[0]*n; pos=[F(40)*j for j in range(n)]; edges=[[] for _ in range(n)]
    while True:
        rowing=[j for j in range(n) if state[j]==0]
        if not rowing: break
        best=None
        for j in rowing:
            k=None
            for kk in range(j+1,n):
                if state[kk]==0: k=kk; break
            if k is not None and speeds[j]>speeds[k]:
                ct=(pos[k]-pos[j])/(speeds[j]-speeds[k])
                if best is None or ct<best[0]: best=(ct,j,k)
        if best is None: break
        _,j,k=best
        state[j]=2; pos[j]=pos[k]; edges[j].append(k)
    above=[set() for _ in range(n)]
    for i in range(n):
        seen={i}; stack=[i]
        while stack:
            u=stack.pop()
            for w in edges[u]:
                if w not in seen: seen.add(w); stack.append(w)
        above[i]=seen-{i}
    par,_=parity_of_new_order(n, above)
    return par

def separating_times(n):
    """Candidate event times for no-finish race, as linear forms over
    (v0, v1) free coords (v2 = 1 - v0 - v1). Finish times absent.
    catch time 0->1: depends on v0,v1. 1->2 depends v1,v2(->v0,v1).
    0->2 (after 1 out): depends v0,v2."""
    pass

def main():
    # Monte Carlo exact-normalized check: sample speeds via uniform simplex,
    # run nofinish_parity exactly. Approximates p(3,inf).
    import random
    N=int(sys.argv[1]) if len(sys.argv)>1 else 200000
    rng=random.Random(42)
    even=0
    for _ in range(N):
        # uniform on simplex via normalized expovariates ~ uniform on simplex
        a=[rng.random()**0 for _ in range(3)]  # not uniform; use exponential
        import math
        e=[-math.log(rng.random()) for _ in range(3)]
        v=[F(e[i])/F(sum(e)) for i in range(3)]
        if nofinish_parity(3, v)==0: even+=1
    print(f"MC p(3,inf) over uniform-exp simplex: {even/N:.6f}")

if __name__=='__main__':
    main()
