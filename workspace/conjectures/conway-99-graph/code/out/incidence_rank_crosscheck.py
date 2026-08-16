"""Independent cross-check of the key incidence-rank values via the boundary
relation rank_3(A+rI) <= rank_3(N), and the SyLVESTER/rank-of-product sanity
bound, so the BvLS 3-rank (the big, credible-separation value) is not a lone
computation.

We recompute rank_3(N) for BvLS using a SECOND independent Gaussian-elimination
implementation (fraction-free pivot over GF(3) with a different row-pivot
order), and compare against rank_3(NN^T) = rank_3((k/2)I+A) as a lower bound.
"""
import numpy as np
from lib.srg import bvls_graph


def rank_gf3_v2(M):
    """Alternative GF(3) rank: transform to reduced row echelon using the
    incremental QR-free Gauss, pivot scanning columns with ties broken by the
    LAST row (opposite of the first implementation's first row)."""
    M = M.astype(object).copy() % 3
    H, W = M.shape
    r = 0
    for col in range(W):
        piv = -1
        for row in range(H - 1, r - 1, -1):
            if (M[row, col] % 3) != 0:
                piv = row
                break
        if piv == -1:
            continue
        if piv != r:
            M[[r, piv]] = M[[piv, r]]
        inv = pow(int(M[r, col] % 3), 1, 3)  # 1->1, 2->2 (self-inverse in GF3)
        # normalize: multiply row by inv so pivot becomes 1
        M[r] = (M[r] * inv) % 3
        for row in range(H):
            if row != r and (M[row, col] % 3) != 0:
                fac = int(M[row, col] % 3)
                M[row] = (M[row] - fac * M[r]) % 3
        r += 1
    return r


from incidence_p_rank import triangles_from, incidence

A = bvls_graph()
tris = triangles_from(A)
N = incidence(A, tris)
r3_v1 = rank_gf3_v2(N)  # independent implementation
print(f"BvLS N is {N.shape[0]}x{N.shape[1]}")
print(f"rank_3(N) [indep impl v2]      = {r3_v1}")

# original impl for comparison
from incidence_p_rank import rank_modp
print(f"rank_3(N) [original impl]      = {rank_modp(N.copy(), 3)}")

# NN^T = r I + A over GF(3), rank as lower bound
r = 22 // 2
NNt = (N @ N.T) % 3
print(f"rank_3(NN^T=(k/2)I+A) [lower bound] = {rank_gf3_v2(NNt)}")
print(f"consistency: rank_3(NN^T) <= rank_3(N)  => {rank_gf3_v2(NNt) <= r3_v1}")

# 2-rank independent
r2_v2 = rank_gf3_v2((N % 2).astype(object))  # reuse routine over GF(2)? inv=1; wrong for GF2 additions
# do GF2 separately
M2 = (N % 2).astype(object).copy()
H, W = M2.shape
rr = 0
for col in range(W):
    piv = -1
    for row in range(H - 1, rr - 1, -1):
        if (M2[row, col] % 2) != 0:
            piv = row
            break
    if piv == -1:
        continue
    if piv != rr:
        M2[[rr, piv]] = M2[[piv, rr]]
    for row in range(H):
        if row != rr and (M2[row, col] % 2) != 0:
            M2[row] = (M2[row] - M2[rr]) % 2
    rr += 1
print(f"rank_2(N) [indep impl]         = {rr}   (v={N.shape[0]}, full-rank? {rr==N.shape[0]})")
