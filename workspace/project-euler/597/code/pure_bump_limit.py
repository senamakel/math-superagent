#!/usr/bin/env python3
"""Pure-bump cascade (L -> infinity, no finishes ever intervene) for small n.
Outcome depends only on the speed ORDER. Enumerate all n! orderings, run the
pure-bump race (finishes removed) with an exact rational speed vector realizing
each strict ordering, and count even-parity orderings -> p(n,inf).
Also compare with the large-L exact arrangement trend."""
import sys, os, itertools
from fractions import Fraction as F
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def pure_bump_parity(n, speeds, huge_L=10**60):
    """Race with L so large nobody finishes: only bumps. One boat bumps at most
    once (becomes OUT). Use exact rationals. Return parity (0 even)."""
    from exact_race import simulate_order_exact, parity_of_new_order
    from brute import parity_of_new_order as pno
    # bump-only dynamics: boat j bumps nearest ROWING boat ahead it can catch.
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
                    best = (ct, j, k)
        if best is None:
            break   # no further bumps possible; rest finish trivially
        _, j, k = best
        state[j]=2; pos[j]=pos[k]; edges[j].append(k)
    above = [set() for _ in range(n)]
    for i in range(n):
        seen={i}; stack=[i]
        while stack:
            u=stack.pop()
            for w in edges[u]:
                if w not in seen: seen.add(w); stack.append(w)
        above[i]=seen-{i}
    par,_ = pno(n, above)
    return par

def ordering_speeds(n, order):
    """A speed vector realizing speeds[order[0]] > speeds[order[1]] > ... .
    e.g. choose speeds = (-order index) + small decreasing epsilons, as exact
    rationals strictly sorted by `order`."""
    v = [None]*n
    # speeds decreasing along `order`: assign value = (n - rank) exactly
    vals = [F(n - r) for r in range(n)]   # decreasing
    for r, boat in enumerate(order):
        v[boat] = vals[r]
    return v

def main():
    n = int(sys.argv[1]) if len(sys.argv)>1 else 3
    even=0; total=0
    odd_orderings=[]
    for order in itertools.permutations(range(n)):
        speeds = ordering_speeds(n, order)
        p = pure_bump_parity(n, speeds)
        even += (p==0); total += 1
        if p==1:
            odd_orderings.append(order)
    print(f"n={n}: p(n,inf) = {even}/{total} = {F(even,total)}")
    if odd_orderings:
        print("odd orderings (speed decreasing order of bump):", odd_orderings)

if __name__=='__main__':
    main()
