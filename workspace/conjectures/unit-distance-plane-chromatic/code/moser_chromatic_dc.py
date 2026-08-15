#!/usr/bin/env python3
"""Verify the Moser chromatic polynomial by a SECOND independent route:
deletion-contraction recursion P(G) = P(G-e) - P(G/e). Returns the factored
polynomial. Cross-check against the interpolation result
k(k-1)(k-2)^2(k-3)(k^2-3k+4).
"""
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
        # find an edge to delete/contract
        e=edges[0]
        rest=edges[1:]
        # G - e
        pe=rec(n, rest)
        # G / e : contract e -> remove both endpoints, add new vertex connected
        # to their neighbour sets
        a,b=e
        nbr_a={u for (u,v) in edges if u==a or v==a}
        nbr_a={u if u!=a else None for u in nbr_a if u!=b}
        nbr_b={u for (u,v) in edges if u==b or v==b}
        nbr_b={u if u!=b else None for u in nbr_b if u!=a}
        # new vertex id n
        new=n
        nbr_set=(nbr_a|nbr_b)-{None}
        new_edges=[]
        for (u,v) in rest:
            uu = n if (u==a or u==b) else u
            vv = n if (v==a or v==b) else v
            if uu!=vv:
                new_edges.append((uu,vv))
        for w in nbr_set:
            new_edges.append((new,w))
        m=n-1
        pc=rec(m, tuple(sorted(tuple(sorted(e)) for e in new_edges)))
        return pe - pc
    return rec(n, edges)

moser=[(0,1),(0,2),(0,4),(0,5),(1,2),(1,3),(2,3),(3,6),(4,5),(4,6),(5,6)]
p=chrom_poly(7, moser)
p=expand(p)
print("deletion-contraction result:")
print(p)
print("factorised:",factor(p))
print("matches interpolation (k-3)(k-2)^2(k-1)k(k^2-3k+4)? ",
      factor(p)==k*(k-1)*(k-2)**2*(k-3)*(k**2-3*k+4))
