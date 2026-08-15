"""Independent verification of the run's claimed chain, written fresh for this
review. Does not read the run's own solver code, so it is a second route.

Chain to check:
  (1) Signed adjacency A_n (A_1=[[0,1],[1,0]], A_n=[[A_{n-1},I],[I,-A_{n-1}]])
      satisfies A_n^2 = n*I, zero diagonal, symmetric, entries {0,+-1}.
  (2) Cauchy interlacing: for any principal submatrix B on m=2^{n-1}+1 rows,
      lambda_max(B) >= sqrt(n).
  (3) lambda_max(B) <= max internal degree of the induced graph S.
Thus f(n) = min_S D(S) >= sqrt(n) for every n.

Also computes f(n) exactly for n<=4 by exhaustive enumeration and checks the
spectral bound against the true minimum.
"""
import itertools, math
import numpy as np

def A(n):
    if n == 1:
        return np.array([[0, 1], [1, 0]], dtype=float)
    A_ = A(n-1)
    N = A_.shape[0]
    top = np.hstack([A_, np.eye(N)])
    bot = np.hstack([np.eye(N), -A_])
    return np.vstack([top, bot])

print("== (1) A_n^2 = n I, zero diagonal, symmetric, {0,+/-1} entries ==")
for n in range(1, 8):
    M = A(n)
    sq = M @ M
    N = M.shape[0]
    assert np.allclose(sq, n*np.eye(N)), f"n={n} square failed"
    assert np.allclose(M, M.T), "not symmetric"
    assert np.allclose(np.diag(M), 0), "diagonal not zero"
    entries = set(M.flatten())
    assert entries <= {0.0, 1.0, -1.0}, entries
    # support is exactly the cube's edges: exactly n neighbours per vertex
    nbrs = (M != 0).sum(axis=1)
    assert np.all(nbrs == n), nbrs
    ev = np.linalg.eigvalsh(sq)  # squares of singular values? use direct
    evals = np.linalg.eigvalsh(M)
    # eigenvalues +sqrt(n) mult 2^{n-1}, -sqrt(n) mult 2^{n-1}
    pos = np.sum(np.abs(evals - math.sqrt(n)) < 1e-8)
    neg = np.sum(np.abs(evals + math.sqrt(n)) < 1e-8)
    assert pos == 2**(n-1) and neg == 2**(n-1), (n, pos, neg)
    print(f"n={n}: A^2=nI OK, symmetric OK, zero diag OK, entries{{0,+-1}} "
          f"OK, n-regular OK, spectrum +sqrt(n)x{pos}, -sqrt(n)x{neg}")

print()
print("== (2)+(3) interlacing and degree bound, exhaustive over ALL S for n=1..4 ==")
def vertices(n):
    return list(itertools.product([0,1], repeat=n))
def D_of(S, n):
    Sset = set(S)
    best = 0
    for v in S:
        d = 0
        for i in range(n):
            w = list(v); w[i] ^= 1; w = tuple(w)
            if w in Sset: d += 1
        best = max(best, d)
    return best

for n in range(1, 5):
    V = vertices(n)
    k = 2**(n-1) + 1
    M = A(n)
    idx = {v:i for i,v in enumerate(V)}
    f_true = None
    for S in itertools.combinations(V, k):
        d = D_of(S, n)
        if f_true is None or d < f_true:
            f_true = d
        # spectral bound on this S
        rows = [idx[v] for v in S]
        B = M[np.ix_(rows, rows)]
        lam = np.linalg.eigvalsh(B)[-1]
        assert lam >= math.sqrt(n) - 1e-9, (n, lam)
        assert lam <= d + 1e-9, (n, lam, d)
    print(f"n={n}: #S=C({2**n},{k})={len(list(itertools.combinations(range(2**n), k)))} (computed), "
          f"f_true={f_true}, sqrt(n)={math.sqrt(n):.3f}, all sets pass interlacing & degree bound")
