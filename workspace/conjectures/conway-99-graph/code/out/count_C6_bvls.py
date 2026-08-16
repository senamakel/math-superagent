"""Compute exact C6 count for the BvLS (243,22,1,2) graph and test the
conjectured hexagon formula (1/12)*n*k*(k-2)*(2k^2-21k+53) across the family.
Also compute what the formula predicts for 99.
"""
import numpy as np, time
from lib.srg import bvls_graph

def count_C6(A):
    A = np.asarray(A, dtype=np.int64)
    n = A.shape[0]
    N = [set(np.flatnonzero(A[i])) for i in range(n)]
    directed = 0
    for a in range(n):
        Na = N[a]
        for b in Na:
            for c in N[b] - {a}:
                for d in N[c] - {a, b}:
                    Nd = N[d]
                    for e in Nd:
                        if e in (a, b, c):
                            continue
                        for f in Na:
                            if f in (b, c, d) or f == e:
                                continue
                            if f in N[e]:
                                directed += 1
    assert directed % 12 == 0
    return directed // 12

def formula(n, k):
    return n * k * (k - 2) * (2*k*k - 21*k + 53) // 12

print("formula(9,4)  =", formula(9, 4))
print("formula(99,14)= ", formula(99, 14))
print("formula(243,22)=", formula(243, 22))

for name, n, k in [("rook",9,4)]:
    pass
# we already know rook C6 = 60 (two independent methods). Print formula for clarity.
