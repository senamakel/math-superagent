"""Verify the full kernel theorem for srg(v,k,1,2) (mu=2 family):

The k/2 diff-of-matching vectors x^{a,a'}  (x_u = [a in P_u] - [a' in P_u],
P_u = pair of N(0)-neighbours of u) are linearly independent, are all in
kernel(A2), and span it (count = k/2 = nullity over Q).

Over-Q nullity: we exhibited k/2 independent integral kernel vectors => nullity_Q >= k/2.
mod-p rank (two primes) gives nullity <= k/2.  Combined => nullity_Q = k/2 exactly.

Here verify the LINEAR INDEPENDENCE of the k/2 vectors (the one gap), over Q
via exact integer Gaussian elimination on the (k/2 x M) matrix of stacked vectors.
"""
import numpy as np
from lib.srg import rook, bvls_graph

def setup(A):
    A = np.asarray(A, dtype=np.int64)
    n = A.shape[0]
    N = [j for j in range(n) if j != 0 and A[0][j] == 1]
    R = [j for j in range(n) if j != 0 and A[0][j] == 0]
    H = np.array([[A[r1, r2] for r2 in R] for r1 in R], dtype=np.int64)
    # matched edges of N(0)
    edges = []
    rem = set(N)
    while rem:
        a = min(rem); rem.discard(a)
        b = [c for c in N if A[a][c]==1][0]
        rem.discard(b)
        edges.append((a,b))
    pr = {}
    for u in R:
        pr[u] = tuple(sorted(c for c in N if A[u][c]==1))
    return H, N, R, edges, pr

def rank_int(mat):
    """exact rank over Q of integer matrix via fraction-free Gaussian elim."""
    from fractions import Fraction
    M = [[Fraction(int(x)) for x in row] for row in mat]
    rows, cols = len(M), len(M[0])
    r = 0
    for c in range(cols):
        piv = next((i for i in range(r, rows) if M[i][c] != 0), None)
        if piv is None: continue
        M[r], M[piv] = M[piv], M[r]
        inv = 1/M[r][c]
        M[r] = [v*inv for v in M[r]]
        for i in range(rows):
            if i != r and M[i][c] != 0:
                f = M[i][c]
                M[i] = [M[i][j]-f*M[r][j] for j in range(cols)]
        r += 1
    return r

for name, A, k in [("rook", rook(3), 4), ("bvls", bvls_graph(), 22)]:
    H, N, R, edges, pr = setup(A)
    idx = {u:i for i,u in enumerate(R)}
    vecs = []
    for (a,ap) in edges:
        x = [0]*len(R)
        for u in R:
            Pu = pr[u]
            x[idx[u]] = (1 if a in Pu else 0) - (1 if ap in Pu else 0)
        vecs.append(x)
    # matrix (k/2 x M)
    mat = vecs
    rk = rank_int(mat)
    print(f"{name}: k={k}, k/2={k//2}, #edges={len(edges)}, rank of diff-vecs over Q = {rk}  independent={rk==k//2}")
