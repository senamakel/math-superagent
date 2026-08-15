#!/usr/bin/env python3
"""Check whether the Moser spindle contains a K4 subgraph, to correct/verify
the claim in the pattern note. (Moser has min degree 3, so in principle could
be K4-free; my note asserted it contains K4s. Verify.)
"""
import itertools
moser=[(0,1),(0,2),(0,4),(0,5),(1,2),(1,3),(2,3),(3,6),(4,5),(4,6),(5,6)]
eset=set(frozenset(e) for e in moser)
k4=[]
for quad in itertools.combinations(range(7),4):
    if all(frozenset({a,b}) in eset for a,b in itertools.combinations(quad,2)):
        k4.append(quad)
print("K4 subgraphs in Moser:", k4)
# also check min degree
deg=[0]*7
for a,b in moser: deg[a]+=1; deg[b]+=1
print("Moser degrees:", deg, "min:", min(deg))
