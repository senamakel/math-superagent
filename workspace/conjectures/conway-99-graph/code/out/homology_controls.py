"""Compute H1(Cl(G), Q) for the controls and check the Cioaba-Mim classification gate.

H1(Cl(G),F) = 0 iff the cycle space of G over F equals the span of the signed
triangle boundaries. So over Q:

  dim H1(Cl(G)) = dim(cycle space) - dim(triangle-boundary subspace intersect cycles)
                = (|E| - |V| + cc) - rank_boundary(C2 -> C1)

where rank_boundary is the rank of the boundary map on triangles (each triangle
is an oriented 3-cycle; we take the vector subspace of edge space spanned by the
triangle circuits).

This is the honest first step the directive-39 gate asks for: compute H1 of both
controls (rook(3) = lattice graph L2(3); BvLS srg(243,22,1,2)) and check whether
the classification theorem's list would separate 99 from them.
"""
import numpy as np
from lib.srg import rook, bvls_graph


def triangle_boundary_rank(A):
    """Rank over Q of the map C2 -> C1 sending each triangle to its 3-edge boundary."""
    n = len(A)
    # edges as (i,j) with i<j
    edges = [(i, j) for i in range(n) for j in range(i + 1, n) if A[i, j]]
    edge_idx = {e: t for t, e in enumerate(edges)}
    # triangles: 3-cliques, oriented
    adj = set()
    for i in range(n):
        for j in range(i + 1, n):
            if A[i, j]:
                adj.add((i, j))
    triangles = []
    for i in range(n):
        for j in range(i + 1, n):
            for l in range(j + 1, n):
                if A[i, j] and A[i, l] and A[j, l]:
                    triangles.append((i, j, l))
    # boundary matrix rows=edges, cols=triangles, entries in {-1,0,1}
    B = np.zeros((len(edges), len(triangles)), dtype=np.int64)
    for c, (a, b, d) in enumerate(triangles):
        # oriented triangle a->b->d->a; boundary edges (a,b),(b,d),(d,a) with signs +1,+1,+1
        B[edge_idx[tuple(sorted((a, b)))], c] = 1
        B[edge_idx[tuple(sorted((b, d)))], c] = 1
        B[edge_idx[tuple(sorted((a, d)))], c] = 1
    # rank over Q = rank over Z of integer matrix
    r = np.linalg.matrix_rank(B)
    return r, len(edges), len(triangles), B


def h1_over_q(A):
    n = len(A)
    deg = A.sum(axis=1)
    E = int(deg.sum()) // 2
    # connected components via numpy rounds (small graphs): use simple BFS
    seen = [False] * n
    cc = 0
    for s in range(n):
        if not seen[s]:
            cc += 1
            stack = [s]
            seen[s] = True
            while stack:
                u = stack.pop()
                for w in range(n):
                    if A[u, w] and not seen[w]:
                        seen[w] = True
                        stack.append(w)
    cycle_dim = E - n + cc
    r, E2, T, B = triangle_boundary_rank(A)
    # rank of triangle boundary map inside cycle space = rank(B) since every
    # triangle boundary is a cycle (in cycle space). So
    h1 = cycle_dim - r
    return h1, cycle_dim, r, E2, T


for name, A in [("rook(3) = lattice L2(3)", rook(3)),
                ("BvLS srg(243,22,1,2)", bvls_graph())]:
    h1, cdim, r, E2, T = h1_over_q(A)
    print(f"{name}: |V|={len(A)}  |E|={E2}  dim cycle space={cdim}  "
          f"#triangles={T}  rank(triangle boundaries)={r}  dim H1(Cl(.))={h1}")
