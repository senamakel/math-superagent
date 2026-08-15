#!/usr/bin/env python3
from functools import lru_cache
from sympy import symbols, expand, factor
k=symbols('k')

def chrom_poly(n, edges):
    edges=tuple(sorted(tuple(sorted(e)) for e in edges))
    @lru_cache(maxsize=None)
    def rec(n, edges):
        edges=tuple(edges)
        if not edges:
            return k**n
        e=edges[0]
        rest=edges[1:]
        # G - e
        pe=rec(n, rest)
        # G / e
        a,b=e
        # remap: contracted vertex gets id n (current max), then shrink
        new_edges=[]
        for (u,v) in rest:
            uu = n if (u==a or u==b) else u
            vv = n if (v==a or v==b) else v
            if uu!=vv:
                new_edges.append(tuple(sorted((uu,vv))))
        # dedupe
        new_edges=tuple(sorted(set(new_edges)))
        pc=rec(n-1, new_edges)
        return pe - pc
    return expand(rec(n, edges))

# K3 triangle: P(k)=k(k-1)(k-2)
tri=chrom_poly(3, [(0,1),(0,2),(1,2)])
print("K3:", factor(tri), "expect k(k-1)(k-2)")
# C5 cycle
c5=chrom_poly(5, [(0,1),(1,2),(2,3),(3,4),(4,0)])
print("C5:", expand(c5), "(expect (k-1)^5-(k-1) = k^5-5k^4+10k^3-10k^2+5k-1 -k +1)")
# Moser
moser=[(0,1),(0,2),(0,4),(0,5),(1,2),(1,3),(2,3),(3,6),(4,5),(4,6),(5,6)]
p=chrom_poly(7,moser)
print("Moser:", expand(p))
print("Moser factor:", factor(p))
