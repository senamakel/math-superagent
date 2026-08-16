"""Exact induced-C4 count on the small members by full brute force.
rook(3): 9 vertices, C(9,4)=126 subsets.
For each 4-subset, induced subgraph must be exactly a 4-cycle (4 edges, all deg 2).
"""
from lib.srg import rook, doily, gq24_graph
import itertools

def induced_c4_true(A):
    n = len(A)
    cnt = 0
    for sub in itertools.combinations(range(n), 4):
        verts = list(sub)
        deg = [sum(A[x][y] for y in verts if y != x) for x in verts]
        edges = sum(deg)//2
        if edges == 4 and all(d == 2 for d in deg):
            cnt += 1
    return cnt

def nonedges(A):
    n = len(A)
    return sum(1 for i in range(n) for j in range(i+1,n) if not A[i][j])

for name, A, mu in [("rook(3)", rook(3), 2), ("doily", doily(), 3), ("GQ(2,4)", gq24_graph(), 5)]:
    ic4 = induced_c4_true(A)
    ne = nonedges(A)
    print(f"{name:>8}: nonedges={ne} TRUE_inducedC4={ic4}  C(mu,2)*ne={mu*(mu-1)//2*ne}  half={mu*(mu-1)//2*ne//2}  ic4==half:{ic4==mu*(mu-1)//2*ne//2}")
