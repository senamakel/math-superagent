"""Consolidated verification of the mu=2-specific second-subconstituent nullity fact.

Fix vertex 0 of an srg(v,k,lambda,mu).  The SECOND SUBSTITUENT H is the induced
graph on the m = v-k-1 non-neighbours of 0, so m = k(k-lambda-1)/mu.

CLAIM (mu=2-specific): at mu=2 (and lambda=1) there are k/2 linearly independent
kernel vectors, one per matched edge of N(0)=7K2, namely
    x^{a,a'}_u = [a in P_u] - [a' in P_u]
where P_u is the 2-subset of N(0) that are the common neighbours of u and 0
(= the pair-label of u).  Then H x = 0.  On the existing mu=2 members this kernel
is EXACTLY the whole nullspace (0-eigenvalue multiplicity = k/2).  At mu != 2
there is no 0 eigenvalue (nullity 0).

We verify, in exact integer arithmetic:
  (1) H x^{a,a'} = 0  for every matched edge, on both mu=2 controls;
  (2) the k/2 vectors are linearly independent (over Q via mod-p rank, two primes);
  (3) the FULL 0-eigenvalue multiplicity is exactly k/2 (so the kernel is complete);
  (4) the mu!=2 members (doily mu=3, GQ(2,4) mu=5) have NO 0 eigenvalue.
"""
import numpy as np
import sympy as sp
from collections import Counter
from lib.srg import rook, bvls_graph, doily, gq24_graph

def second_subconstituent(A):
    A = np.asarray(A, dtype=np.int64)
    n = A.shape[0]
    outer = [j for j in range(n) if j != 0 and A[0][j] == 0]
    m = len(outer)
    H = np.zeros((m, m), dtype=np.int64)
    for i in range(m):
        for j in range(m):
            H[i, j] = A[outer[i], outer[j]]
    return H, outer

def matched_edges(A):
    A = np.asarray(A, dtype=np.int64)
    n = A.shape[0]
    N = [j for j in range(n) if j != 0 and A[0][j] == 1]
    rem = set(N)
    edges = []
    while rem:
        a = min(rem); rem.discard(a)
        b = [c for c in N if A[a][c] == 1][0]
        rem.discard(b)
        edges.append((a, b))
    return edges

def rank_modp(M, p):
    M = [list(r) for r in M]
    rows = len(M); cols = len(M[0]); r = 0
    for c in range(cols):
        piv = None
        for i in range(r, rows):
            if M[i][c] % p:
                piv = i; break
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        inv = pow(int(M[r][c]) % p, p-2, p)
        for cc in range(cols):
            M[r][cc] = (int(M[r][cc]) * inv) % p
        for i in range(rows):
            if i != r and M[i][c] % p:
                f = int(M[i][c]) % p
                for cc in range(cols):
                    M[i][cc] = (int(M[i][cc]) - f*int(M[r][cc])) % p
        r += 1
    return r

def analyze(name, A, k, lam, mu, expected_kernel_rank):
    A = np.asarray(A, dtype=np.int64)
    H, outer = second_subconstituent(A)
    m = len(outer)
    idx = {u: i for i, u in enumerate(outer)}
    edges = matched_edges(A)
    # pair-labels
    pr = {}
    for u in outer:
        pr[u] = tuple(sorted(c for c in range(A.shape[0]) if c != 0 and A[0][c] == 1 and A[u][c] == 1))
    # (1) kernel vectors
    vecs = []
    allkernel = True
    for (a, ap) in edges:
        x = np.zeros(m, dtype=int)
        for u in outer:
            Pu = pr[u]
            x[idx[u]] = (1 if a in Pu else 0) - (1 if ap in Pu else 0)
        if not np.all(H @ x == 0):
            allkernel = False
        vecs.append(x)
    # (2) independence via mod-p rank of the k/2 x m matrix
    V = np.array(vecs, dtype=object) if vecs else np.zeros((0, m), dtype=object)
    rks = []
    for p in (109, 101):
        rks.append(rank_modp([[int(z) % p for z in row] for row in V.tolist()], p) if len(vecs) else 0)
    # (3) full 0-eigenvalue multiplicity
    M = sp.Matrix(H.tolist())
    eig = M.eigenvals()
    mult0 = int(eig.get(0, 0)) if eig else 0
    # srg-ness, lambda/mu counts
    lamc, muc = Counter(), Counter()
    for i in range(m):
        for j in range(i+1, m):
            c = int((H[i] & H[j]).sum())
            if H[i, j]: lamc[c] += 1
            else: muc[c] += 1
    print(f"=== {name}  (v,k,lambda,mu)=({A.shape[0]},{k},{lam},{mu})  m={m}")
    print(f"    matched edges in N(0) = k/2 = {k//2};  kernel vecs built: {len(vecs)}")
    print(f"    (1) all H x^{{a,a'}} = 0 exactly: {allkernel}")
    print(f"    (2) rank of kernel-vector matrix mod p: {rks}   (k/2={k//2})")
    print(f"    (3) 0-eigenvalue multiplicity of H: {mult0}   (k/2={k//2})  nullity==k/2: {mult0==k//2}")
    print(f"    (4) H regular degree {int(H.sum(axis=1)[0])}, lambda {dict(lamc)}, mu {dict(muc)}")
    print()

for name, A, k, lam, mu in [("rook(3)", rook(3), 4, 1, 2),
                            ("bvls", bvls_graph(), 22, 1, 2),
                            ("doily", doily(), 6, 1, 3),
                            ("GQ(2,4)", gq24_graph(), 10, 1, 5)]:
    analyze(name, A, k, lam, mu, k//2)
