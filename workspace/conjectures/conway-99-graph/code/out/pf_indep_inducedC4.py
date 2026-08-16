"""Verify the general induced-C4 identity for ALL lambda=1 SRG members:
induced C4 = C(mu,2) * #nonedges, from c7 (common neighbours of a nonedge
are pairwise nonadjacent => each unordered pair gives one induced C4).
Exact, from adjacency matrices via lib.srg / lib.triangles.
"""
from lib.srg import rook, doily, gq24_graph, bvls_graph
import itertools

def induced_c4_count(A):
    n = len(A)
    cnt = 0
    for a, b, c, d in itertools.combinations(range(n), 4):
        verts = [a, b, c, d]
        deg = [sum(A[x][y] for y in verts if y != x) for x in verts]
        # an induced C4 = exactly 4 edges and every vertex has degree 2 inside
        if all(dd == 2 for dd in deg):
            cnt += 1
    return cnt

def nonedges(A):
    n = len(A)
    return sum(1 for i in range(n) for j in range(i+1, n) if not A[i][j])

for name, G, mu in [("rook(3)", rook(3), 2), ("doily", doily(), 3),
                    ("GQ(2,4)", gq24_graph(), 5), ("BvLS", bvls_graph(), 2)]:
    A = G
    ne = nonedges(A)
    ic4 = induced_c4_count(A)
    pred = (mu*(mu-1)//2) * ne
    print(f"{name:>8}: mu={mu} nonedges={ne} inducedC4={ic4} C(mu,2)*ne={pred} match={ic4==pred}")
