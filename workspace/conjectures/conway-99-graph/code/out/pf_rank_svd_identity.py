"""Fresh independent cross-check: NN^T = (k/2)I + A and N^TN = 3I + C3 for the
point x triangle incidence matrix N of the mu=2 family members.

Exact numpy integer arithmetic for products (no floats); the identity is a
symbolically-exact matrix equality. For k=14 (99 candidate), 7I+A has
eigenvalues 7+{14,3,-4} = {21,10,3} all nonzero, so rank_Q(NN^T)=99=rank_Q(N)
(full row rank). This is PARAMETER-DETERMINED (holds for BvLS k=22 too), so it
is NOT a 99 separator -- recorded as an exact cross-check, not a claim about 99.
"""
import numpy as np
from lib.srg import rook, bvls_graph

def triangle_list(A):
    n = len(A)
    tris = []
    for i in range(n):
        for j in range(i + 1, n):
            if A[i][j] == 0:
                continue
            for l in range(j + 1, n):
                if A[i][l] and A[j][l]:
                    tris.append(frozenset((i, j, l)))
    return list(set(tris))  # dedupe

def run(name, A, v, k):
    A = np.asarray(A, dtype=np.int64)
    T = triangle_list(A)
    nT = len(T)
    cols = list(T)
    # incidence N: rows points, cols triangles
    N = np.zeros((v, nT), dtype=np.int64)
    for ci, tri in enumerate(cols):
        for p in tri:
            N[p, ci] = 1
    NNT = N @ N.T
    expect = (k // 2) * np.eye(v, dtype=np.int64) + A
    ok1 = np.array_equal(NNT, expect)
    # N^TN = 3I + C3
    NTN = N.T @ N
    C3 = np.zeros((nT, nT), dtype=np.int64)
    for i in range(nT):
        for j in range(nT):
            if i != j and len(cols[i] & cols[j]) == 1:
                C3[i, j] = 1
    ok2 = np.array_equal(NTN, 3 * np.eye(nT, dtype=np.int64) + C3)
    # nonzero diagonal of NNT (it equals (k/2)I+A, invertible iff A has no
    # eigenvalue -(k/2))
    spec_A = np.round(np.linalg.eigvalsh(A)).astype(int)  # for check only
    print(f"[{name}] v={v} k={k} nT={nT}")
    print(f"  NN^T == (k/2)I + A  : {ok1}")
    print(f"  N^TN == 3I + C3     : {ok2}")
    if k == 14:
        print("  k=14 => 7I+A eigenvalues {21,10,3} nonzero => rank_Q(N)=99 (full row rank)")
    print(f"  min(v,nT)={min(v, nT)}; A spectrum(row) ~ {sorted(set(spec_A.tolist()))}")

if __name__ == "__main__":
    run("rook(3)", rook(3), 9, 4)
    print()
    run("bvls", bvls_graph(), 243, 22)
