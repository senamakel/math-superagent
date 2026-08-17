"""Refuter: verify concrete asserted/computational claims on the controls.

Checks (each an exact integer computation off the adjacency matrix):
 1. keramatipour-trian-graph claim: C3(Gamma) of BvLS has nk/6 vertices,
    is (3k-6)/2-regular, every two adjacent triangles share k/2-2 common
    neighbours, non-adjacent triangles share at most 3.
 2. c8: number of induced hexagons (induced 6-cycles) in BvLS.
 3. n3 four-classical: rook/doily/gq24/bvls all have n3=0 (no two-edge-joined
    disjoint triangle pairs).
 4. c7: the two common neighbours of any non-adjacent pair are non-adjacent.
"""
import itertools
import numpy as np
from lib.srg import rook, doily, gq24_graph, bvls_graph, is_srg
from lib.triangles import triangle_graph


def count_triangles(A):
    n = A.shape[0]
    tris = []
    for a in range(n):
        adj_a = np.flatnonzero(A[a])
        for i in range(len(adj_a)):
            b = adj_a[i]
            if b <= a:
                continue
            nbs = np.flatnonzero(A[b])
            for c in adj_a[i:]:
                if c > b and A[b, c]:
                    tris.append(frozenset((int(a), int(b), int(c))))
    return list(set(tris))


def n3_count(A, tris):
    """Number of disjoint triangle pairs joined by EXACTLY two edges."""
    n = A.shape[0]
    tris = list(tris)
    t = len(tris)
    cnt = 0
    # store membership
    for i in range(t):
        Ti = tris[i]
        for j in range(i + 1, t):
            Tj = tris[j]
            if Ti & Tj:
                continue
            cross = 0
            for x in Ti:
                for y in Tj:
                    if A[x, y]:
                        cross += 1
            if cross == 2:
                cnt += 1
    return cnt


print("=== Claim tests ===")

# --- 1. Triangle graph C3 of BvLS ---
B = bvls_graph()
print("bvls is_srg(243,22,1,2):", is_srg(B, 243, 22, 1, 2))
C, tris = triangle_graph(B)
nt = C.shape[0]
pred_nt = 243 * 22 // 6
print(f"C3 vtx: actual {nt}, predicted nk/6={pred_nt}")
# degree
deg = C.sum(axis=1)
print("C3 regular?", (deg == deg[0]).all(), "degree", int(deg[0]),
      "predicted (3k-6)/2 =", (3 * 22 - 6) // 2)
# shared neighbours of adjacent / non-adjacent triangles in C3
C2 = C @ C
adj = C.astype(bool)
off = ~np.eye(nt, dtype=bool)
la = C2[adj & off]
non = C2[(~adj) & off]
print("adjacent triangles share:", "all", int(la.min()), "..", int(la.max()),
      "predicted k/2-2 =", 22 // 2 - 2)
print("non-adjacent triangles share: min", int(non.min()), "max", int(non.max()),
      "(claim: <= 3)")

tris_bvls = tris

# --- 3. n3 on the four classical lambda=1 graphs ---
for name, A in [("rook", rook(3)), ("doily", doily()),
                ("gq24", gq24_graph()), ("bvls", B)]:
    tris = count_triangles(A)
    n3 = n3_count(A, tris)
    print(f"n3 {name}: {n3}  (triangles={len(tris)})")

# --- 4. c7: common neighbours of non-adjacent pairs are non-adjacent ---
def c7_check(A):
    n = A.shape[0]
    A2 = A @ A
    adj = A.astype(bool)
    off = ~np.eye(n, dtype=bool)
    # non-adjacent pairs
    nz = np.argwhere((~adj) & off)
    for u, w in nz[:]:
        cn = np.flatnonzero((A[u] * A[w]) == 1)
        # check every pair in cn is non-adjacent
        for i in range(len(cn)):
            for j in range(i + 1, len(cn)):
                if A[cn[i], cn[j]]:
                    return False, (u, w, cn[i], cn[j])
    return True, None

for name, A in [("rook", rook(3)), ("bvls", B)]:
    ok, bad = c7_check(A)
    print(f"c7 {name}: common neighbours of non-adjacent pair non-adjacent = {ok}")

print("done")
