"""Exact triangle (3-clique) graph C3(Gamma) of a simple graph, made exact.

Two triangles are adjacent in the triangle graph iff they are DISTINCT and
share exactly one vertex.  For a lambda=1 graph this is the only possible
non-trivial sharing (lambda=1 puts every edge in exactly one triangle, so no
two distinct triangles share an edge; sharing two vertices = sharing the edge,
impossible; sharing three = same triangle).  So for lambda=1 the convention
'reach exactly two vertices in common' is automatic.

count_triangles / triangle_graph:
  - triangle_graph(A) -> (C3_adjacency, triangle list)
    triangle list: list of frozensets, one per 3-clique.
    C3 adjacency[i,j]=1 iff triangles i,j distinct and share >= 1 vertex.
  Works exactly on the integer 0/1 adjacency matrix; no floats.

The spectrum prediction (Phillips 2026 eq. 4.3, for a lambda=1 srg with
clique graph C3) is supplied separately as c3_spectrum_prediction so the
verification script can compare prediction against the exact computed
spectrum without any linear-algebra shortcut.
"""
import itertools
import numpy as np


def _triangles(A):
    """All 3-cliques of the graph as a list of frozensets, exact."""
    n = A.shape[0]
    A = np.asarray(A, dtype=np.int64)
    tris = []
    for a in range(n):
        adj_a = np.flatnonzero(A[a])
        if a % 50 == 0:
            pass
        for i in range(len(adj_a)):
            b = adj_a[i]
            if b <= a:
                continue
            nbs = np.flatnonzero(A[b])
            cvals = np.intersect1d(adj_a[i:], nbs)  # c > b for c in adj_a[i:]
            for c in cvals:
                if A[b, c] and A[a, c]:
                    tr = frozenset((int(a), int(b), int(c)))
                    if tr not in tris:
                        tris.append(tr)
    return tris


def triangle_graph(A):
    """Triangle graph C3: vertices = 3-cliques; two adjacent iff distinct and
    sharing at least one vertex. Returns (adjacency int matrix, triangle list)."""
    A = np.asarray(A, dtype=np.int64)
    tris = _triangles(A)
    nt = len(tris)
    C = np.zeros((nt, nt), dtype=np.int64)
    for i in range(nt):
        for j in range(i + 1, nt):
            if tris[i] & tris[j]:
                C[i, j] = C[j, i] = 1
    return C, tris


def c3_spectrum_prediction(v, k, r, s, m_r, m_s, lam=1, mu=2):
    """Phillips eq 4.3 predicted spectrum of the triangle graph of
    srg(v,k,lam,mu):
      d^1, (k/2 + r - 3)^m_r, (k/2 + s - 3)^m_s, (-3)^(nT - v)
    where nT = vk/6 (number of triangles), d = 3(k/2 - 1).
    Returns ([(eig, mult), ...], d, nT)."""
    nT = v * k // 6
    d = 3 * (k // 2 - 1)
    spec = [(d, 1),
            (k // 2 + r - 3, m_r),
            (k // 2 + s - 3, m_s),
            (-3, nT - v)]
    return spec, d, nT
