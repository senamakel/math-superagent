"""Settle the C3 triangle-graph spectrum multiplicity pairing on BvLS and
rook by direct exact/numerical spectrum computation, so the closed-form
labels (which C3 eigenvalue carries which multiplicity) are correct."""
import numpy as np
from lib.srg import rook, bvls_graph
from lib.triangles import triangle_graph

def spectrum_multiset(A):
    A = np.asarray(A, dtype=np.float64)
    w = np.linalg.eigvalsh(A)
    # round to integers, count multiset
    from collections import Counter
    c = Counter()
    for x in w:
        c[round(float(x))] += 1
    return dict(c)

for name, A, v, k in [("rook(3)", rook(3), 9, 4), ("BvLS", bvls_graph(), 243, 22)]:
    C, tris = triangle_graph(A)
    spec = spectrum_multiset(C)
    nT = v*k//6
    d = 3*(k//2 - 1)
    print(f"{name}: v={v} k={k} nT={nT} d={d}")
    print("   C3 numerical spectrum multiset:", spec)
    print("   nT-v (negative -3 count) =", nT - v, "  (-3 multiplicity expectation)")
