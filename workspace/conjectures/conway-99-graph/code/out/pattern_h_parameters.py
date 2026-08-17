"""Extract exact structural facts about the outer pair-labeling graph H
from the actual control graphs rook(3) and bvls_graph().

Reduction (adopted): fix vertex 0, N(0) = (k/2)K2.  Each distance-2 vertex u
corresponds bijectively to a NON-matching pair {a,b} of N(0) (u adjacent to both,
and a,b share 0 and u as their two common neighbours).  Outer graph H: vertices =
the distance-2 vertices (pair-labels), adjacency = induced on vertices at dist 2
from 0.

Prior rounds gated the reduction (round 31: rule holds) but did NOT extract H's
own srg parameters.  Question: is H an srg, and are its (v',k',lambda',mu')
parameter-determined (following from (n,k,1,2) alone) or does it vary / separate?

Exact integer arithmetic throughout.
"""
from lib.srg import rook, bvls_graph
from collections import Counter

def outer_H(A, k):
    n = len(A)
    N0 = [j for j in range(n) if A[0][j]]
    assert len(N0) == k
    # label for distance-2 vertex = pair of neighbours of 0 it attaches to
    # but we just compute H directly on the dist-2 vertices.
    dist2 = sorted(j for j in range(n) if j != 0 and A[0][j] == 0 and j != 0)
    # actually dist-2 = non-neighbours of 0 (other than 0 itself)
    dist2 = [j for j in range(n) if j != 0 and A[0][j] == 0]
    dist2set = set(dist2)
    m = len(dist2)
    # H adjacency
    adj = [[0]*m for _ in range(m)]
    deg = [0]*m
    for i in range(m):
        u = dist2[i]
        for j in range(i+1, m):
            v = dist2[j]
            if A[u][v]:
                adj[i][j] = adj[j][i] = 1
    for i in range(m):
        deg[i] = sum(adj[i])
    degc = Counter(deg)
    print(f"k={k}  outer vertices m={m}")
    print(f"  H degree distribution: {dict(degc)}")
    # check common-neighbour constancy for srg candidates
    lamc = Counter(); muc = Counter()
    for i in range(m):
        for j in range(m):
            if i==j: continue
            c = sum(1 for t in range(m) if adj[i][t] and adj[j][t])
            if adj[i][j]: lamc[c]+=1
            else: muc[c]+=1
    print(f"  H: lambda common-neighbour counts: {dict(lamc)}")
    print(f"  H: mu    common-neighbour counts: {dict(muc)}")
    return dist2

A = rook(3)
outer_H(A, 4)
print()
A = bvls_graph()
outer_H(A, 22)
