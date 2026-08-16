"""Independent BvLS route: explicit Cayley graph on Z3^5, translation = automorphism.

The BvLS graph is the Cayley graph of the abelian group Z3^5 with connection
set {+-c_1, ..., +-c_11} where c_j are the 11 pairwise non-proportional
columns of the ternary Golay parity-check matrix H. As a coset graph of an
abelian group it is vertex-transitive: every translation x -> x+a is an
automorphism. Here we verify a handful of translations literally preserve
adjacency, an independent structural check that does not call is_srg at all.
"""
import itertools
import numpy as np


def cayley_bvls():
    # parity-check columns of the ternary Golay code (pairwise non-collinear)
    H = [
        [1, 0, 1, 2, 2, 2, 1, 0, 0, 0, 0],
        [1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0],
        [2, 1, 0, 2, 1, 2, 0, 0, 1, 0, 0],
        [1, 2, 2, 2, 1, 0, 0, 0, 0, 1, 0],
        [0, 1, 2, 2, 2, 1, 0, 0, 0, 0, 1],
    ]
    H = np.array(H, dtype=np.int64) % 3
    cols = [H[:, j] for j in range(11)]
    conn = set()
    for c in cols:
        for coeff in (1, 2):
            conn.add(tuple(int((coeff * x) % 3) for x in c))
    assert len(conn) == 22
    elts = list(itertools.product([0, 1, 2], repeat=5))
    idx = {e: t for t, e in enumerate(elts)}
    n = len(elts)
    A = np.zeros((n, n), dtype=np.int64)
    for e, i in idx.items():
        for d in conn:
            t = tuple((e[j] + d[j]) % 3 for j in range(5))
            A[i, idx[t]] = 1
    np.fill_diagonal(A, 0)
    return A, elts, idx


def check_translations(A, elts, idx, a):
    """Translation x -> x+a must preserve adjacency: A[u,v]==A[u+a,v+a]."""
    n = len(elts)
    img = [idx[tuple((elts[i][j] + a[j]) % 3 for j in range(5))] for i in range(n)]
    # permuted matrix
    P = np.zeros((n, n), dtype=np.int64)
    for i in range(n):
        for j in range(n):
            P[img[i], img[j]] = A[i, j]
    return bool(np.array_equal(P, A))


if __name__ == "__main__":
    A, elts, idx = cayley_bvls()
    print("Cayley Z3^5 graph: n=%d, edges=%d, degree 22 uniform: %s"
          % (A.shape[0], int(A.sum() // 2),
             bool(np.all(A.sum(axis=1) == 22))))
    print("Construction independent of is_srg; next check translations only.")
    ok = True
    for a in [(1, 0, 0, 0, 0), (0, 0, 2, 1, 0), (2, 2, 2, 2, 2), (1, 2, 0, 2, 1)]:
        r = check_translations(A, elts, idx, a)
        ok &= r
        print("  translation +%s preserves adjacency: %s" % (str(a), r))
    print("vertex-transitive by construction (all translations automorphisms):", ok)
