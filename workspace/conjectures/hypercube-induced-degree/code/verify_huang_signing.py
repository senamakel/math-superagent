#!/usr/bin/env python3
"""Verify Huang's signed adjacency matrix recursion for Q_n."""
import numpy as np
import collections

def A(n):
    if n == 1:
        return np.array([[0, 1], [1, 0]], dtype=object)
    m = 1 << (n - 1)
    I = np.eye(m, dtype=object)
    prev = A(n - 1)
    return np.vstack([np.hstack([prev, I]), np.hstack([I, -prev])])

def cube_edges(n):
    edges = set()
    for u in range(1 << n):
        for coord in range(n):
            edges.add(frozenset((u, u ^ (1 << coord))))
    return edges

for n in range(1, 10):
    M = A(n); sz = 1 << n
    assert M.shape == (sz, sz)
    assert set(np.unique(M)) <= {0, 1, -1}
    E = cube_edges(n)
    for (i, j) in np.argwhere(M != 0):
        assert i != j and frozenset((i, j)) in E
    assert np.all(np.diag(M) == 0)
    Msq = M @ M
    assert np.all(Msq == n * np.eye(sz, dtype=object))
    cnt = collections.Counter(int((M[i] != 0).sum()) for i in range(sz))
    assert cnt == {n: sz}
    print("n=%d OK: A^2=%dI, all %d rows have exactly %d nonzero edge entries" % (n, n, sz, n))

print("\nEigenvalues (+-sqrt(n), multiplicity 2^(n-1)):")
for n in range(1, 8):
    w = np.round(np.linalg.eigvalsh(A(n).astype(float)), 6)
    print(" n=%d: %s  (expect +-%.4f each x %d)" % (n, collections.Counter(w.tolist()), n**0.5, 1<<(n-1)))
