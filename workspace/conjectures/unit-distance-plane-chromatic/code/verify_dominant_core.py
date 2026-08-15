#!/usr/bin/env python3
"""Verify that the dominant 7-vertex 11-edge core form is the Moser spindle,
and that the 'contains Moser' flag was a labelling artifact.

We rebuild the canonical adjacency bitstring of the Moser spindle (given its
edge list from explore_spindle.captured.txt) and compare to the dominant core
form found by analyze_cores_small.
"""
import itertools

def canonical_perm_bitstring(edges):
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

# Moser spindle edges: O=0,P1=1,P2=2,Q=3,P1'=4,P2'=5,Q'=6
moser=[(0,1),(0,2),(0,4),(0,5),(1,2),(1,3),(2,3),(3,6),(4,5),(4,6),(5,6)]
print("Moser spindle canonical bitstring:", canonical_perm_bitstring(moser))

# dominant core form found:
dom = (0,0,0,1,1,1,1,1,0,0,1,1,0,0,1,0,1,0,1,1,0)
print("Dominant core form:               ", dom)
print("MATCH:", canonical_perm_bitstring(moser)==dom)

# How many of the 73 occurrences are genuine Moser cores vs merely same bitstring
# (same count is fine; the bitstring IS canonical so equal => isomorphic)
