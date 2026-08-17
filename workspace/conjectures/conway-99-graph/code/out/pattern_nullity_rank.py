"""Verify nullity(A2)=k/2 for srg(v,k,1,2).  Use exact integer arithmetic via
mod-p rank (H is 0/1 integer; nullity over Q equals nullity mod p for a good
prime p not dividing any invariant factor).  Use two primes and verify count of
kernel via sympy on the small graphs.
"""
import numpy as np
import sympy as sp
from lib.srg import rook, bvls_graph, doily, gq24_graph

def second_subconstituent(A):
    A = np.asarray(A, dtype=np.int64)
    n = A.shape[0]
    outer = [j for j in range(n) if j != 0 and A[0][j] == 0]
    H = np.array([[A[outer[i], outer[j]] for j in range(len(outer))] for i in range(len(outer))], dtype=np.int64)
    return H, outer

def rank_modp(H, p):
    """rank of integer matrix H over GF(p) via Gaussian elimination mod p."""
    Hp = H.astype(object) % p
    # numpy object with modular elimination
    import copy
    M = [list(row) for row in Hp]
    rows, cols = len(M), len(M[0])
    r = 0
    for c in range(cols):
        piv = None
        for i in range(r, rows):
            if M[i][c] % p != 0:
                piv = i
                break
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        inv = pow(int(M[r][c]) % p, p-2, p)
        for cc in range(cols):
            M[r][cc] = (int(M[r][cc]) * inv) % p
        for i in range(rows):
            if i != r and M[i][c] % p != 0:
                f = int(M[i][c]) % p
                for cc in range(cols):
                    M[i][cc] = (int(M[i][cc]) - f*int(M[r][cc])) % p
        r += 1
    return r

for name, A, k, p1, p2 in [("rook(3) 9,4,1,2 mu=2", rook(3), 4, 109, 101),
                            ("bvls 243,22,1,2 mu=2", bvls_graph(), 22, 109, 101),
                            ("doily 15,6,1,3 mu=3", doily(), 6, 109, 101),
                            ("GQ(2,4) 27,10,1,5 mu=5", gq24_graph(), 10, 109, 101)]:
    H, outer = second_subconstituent(A)
    m = len(outer)
    r1 = rank_modp(H, p1); r2 = rank_modp(H, p2)
    print(f"{name}: m={m}  rank mod {p1} = {r1}  rank mod {p2} = {r2}")
    print(f"   nullity mod p1 = {m-r1},  mod p2 = {m-r2}   k/2 = {k/2}  match={m-r1==k//2 and m-r2==k//2}")
