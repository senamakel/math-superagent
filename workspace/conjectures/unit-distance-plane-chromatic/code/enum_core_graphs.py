#!/usr/bin/env python3
"""Verify which 7-vertex 11-edge 4-critical graph the dominant kernel core is.

The Moser spindle has an explicit edge list from the calibrated coordinates
(explore_spindle). Two edge lists appeared in my scripts; check whether they
are isomorphic, and whether the canonical core equals the true Moser spindle.
Also enumerate ALL non-isomorphic 7-vertex 11-edge 4-critical graphs to see
which one(s) occur as kernel cores.
"""
import itertools

# Moser spindle, from explore_spindle.captured.txt.
# O=0,P1=1,P2=2,Q=3,P1'=4,P2'=5,Q'=6
moser = [(0,1),(0,2),(0,4),(0,5),(1,2),(1,3),(2,3),(3,6),(4,5),(4,6),(5,6)]

# The edge list used in the (buggy) moser_subgraph check:
moser2 = [(0,1),(0,2),(0,3),(0,4),(1,2),(1,5),(2,5),(5,6),(3,4),(3,6),(4,6)]

def canon(edges):
    n=7
    adj=[[0]*n for _ in range(n)]
    for a,b in edges: adj[a][b]=adj[b][a]=1
    best=None
    for perm in itertools.permutations(range(n)):
        bits=[]
        for i in range(n):
            for j in range(i+1,n):
                bits.append(adj[perm[i]][perm[j]])
        t=tuple(bits)
        if best is None or t<best: best=t
    return best

c1=canon(moser); c2=canon(moser2)
print("canon(moser) =", c1)
print("canon(moser2)=", c2)
print("isomorphic:", c1==c2)

# Build all graphs on 7 vertices with 11 edges via the vector space of edges
# is C(21,11) = 352716, feasible. Filter: 4-chromatic & 4-critical (deleting
# any edge drops chi to 3).
n=7
edges_all=[(a,b) for a in range(n) for b in range(a+1,n)]
def is_4col(es):
    # backtracking 4-colorability, small
    adj=[set() for _ in range(n)]
    for a,b in es: adj[a].add(b); adj[b].add(a)
    col=[-1]*n
    def bt(v):
        if v==n: return True
        used={col[u] for u in adj[v] if col[u]>=0}
        for c in range(4):
            if c not in used:
                col[v]=c
                if bt(v+1): return True
                col[v]=-1
        return False
    return bt(0)
def is_3col(es):
    adj=[set() for _ in range(n)]
    for a,b in es: adj[a].add(b); adj[b].add(a)
    col=[-1]*n
    def bt(v):
        if v==n: return True
        used={col[u] for u in adj[v] if col[u]>=0}
        for c in range(3):
            if c not in used:
                col[v]=c
                if bt(v+1): return True
                col[v]=-1
        return False
    return bt(0)
def is_4critical(es):
    if not is_4col(es): return False
    if is_3col(es): return False
    for i in range(len(es)):
        if is_4col(es[:i]+es[i+1:]): return False  # edge not critical-removable
    return True

distinct_core_forms=set()
moser_form=c1
moser_in=0
for combo in itertools.combinations(edges_all, 11):
    if is_4critical(combo):
        cf=canon(list(combo))
        distinct_core_forms.add(cf)
        if cf==moser_form: moser_in+=1
print("total distinct 7v/11e 4-critical graphs:", len(distinct_core_forms))
print("canonical forms:")
for cf in sorted(distinct_core_forms):
    print("   ", cf, "  ==moser:", cf==moser_form)
print("(moser_is_a_4critical_7v11e existed in: always, it IS one; count of listing hits:", moser_in, ")")
