#!/usr/bin/env python3
"""Verify Huang's signed adjacency matrix recursion for Q_n.

A_1 = [[0,1],[1,0]]
A_n = [[A_{n-1}, I], [I, -A_{n-1}]]   (2^n x 2^n, signed adjacency of Q_n)

Check: (1) entries are in {0, +1, -1}; (2) the +1/-1 entries sit exactly on
hypercube edges (two labels, one coordinate differ); (3) A_n^2 = n I.

This is the construction, verified directly — not a search for an answer.
"""
import numpy as np

def A(n):
    if n == 1:
        return np.array([[0, 1], [1, 0]], dtype=object)
    m = 1 << (n - 1)
    I = np.eye(m, dtype=object)
    prev = A(n - 1)
    top = np.hstack([prev, I])
    bot = np.hstack([I, -prev])
    return np.vstack([top, bot])

def cube_edges(n):
    """All hypercube edges as unordered pairs (u,v) in {0,1}^n."""
    edges = set()
    for u in range(1 << n):
        for coord in range(n):
            v = u ^ (1 << coord)
            edges.add(frozenset((u, v)))
    return edges

for n in range(1, 9):
    M = A(n)
    sz = 1 << n
    assert M.shape == (sz, sz), M.shape
    # entries in {0, +-1}
    vals = set(np.unique(M))
    assert vals <= {0, 1, -1}, vals
    # nonzero entries sit exactly on cube edges, values +-1
    E = cube_edges(n)
    offdiag = np.argwhere(M != 0)
    for (i, j) in offdiag:
        assert i != j
        assert frozenset((i, j)) in E
    ondiag = np.argwhere(M == 0)
    for (i, j) in ondiag:
        assert i == j  # diagonal is zero; all nondiagonal are +-1 edges
    diag = np.diag(M)
    assert np.all(diag == 0)
    # A_n^2 = n I
    Msq = M @ M
    assert np.all(Msq == n * np.eye(sz, dtype=object)), n
    # each row: exactly n nonzero entries
    rowsumsq = [int((M[i] != 0).sum()) for i in range(sz)]
    assert rowsumsq == [n] * sz, (n, set(rowsumsq))
    print(n, "OK  |A^2 =", (Msq[0,0]), "I  | per-row nonzeros:", rowsumsq[0], "| eigengen:", )

# eigenvalues of A_n: +sqrt(n) and -sqrt(n), 2^{n-1} each
for n in range(1, 7):
    w = np.linalg.eigvalsh(A(n).astype(float))
    sq = round(n ** 0.5, 6)
    import collections
    cnt = collections.Counter([round(round(x,9),6) for x in w])
    print("n =", n, "distinct eigenvalues:", dict(cnt), "  expected +-", sq, "each x", (1 << (n-1)))
