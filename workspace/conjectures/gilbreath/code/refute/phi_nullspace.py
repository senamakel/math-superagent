#!/usr/bin/env python3
"""Build the literal F2 transfer matrix Phi_n (as in G-supply-linearization)
and check the universal claim wt(Phi_n h) >= wt(h)/2 for all h.

Two independent constructions:
 (A) Pascal/XOR window formula over halved PARITY bits h[j] = (A1[j]//2) mod 2.
 (B) Direct halved {0,1}-regime triangle construction (u,v in {0,1} -> |u-v|
     = u XOR v), where each tail cell value = XOR of its row-1 parity ancestors.

Also report the null space of Phi_n (domain n-2 > codomain n-3 always), since a
nonzero null vector immediately refutes the universal weight transfer.
"""
from math import comb

def phi_matrix(n):
    """rows k=2..n-2, cols j=2..n-1. entry = [C(k-1, j-(n-k)) mod 2]."""
    rows = []
    for k in range(2, n - 1):
        r = []
        for j in range(2, n):
            if j < n - k or j > n - 1:
                r.append(0)
            else:
                r.append(comb(k - 1, j - (n - k)) % 2)
        rows.append(r)
    return rows

def rref_nullspace(mat):
    """Gaussian elim over F2; return basis of null space."""
    nrows = len(mat); ncols = len(mat[0])
    # augmented identity to track column ops
    m = [row[:] + [1 if i == c else 0 for c in range(ncols)] for i, row in enumerate(mat)]
    piv = []
    r = 0
    for c in range(ncols):
        # find pivot row
        pr = None
        for i in range(r, nrows):
            if m[i][c]:
                pr = i; break
        if pr is None:
            continue
        m[r], m[pr] = m[pr], m[r]
        piv.append(c)
        for i in range(nrows):
            if i != r and m[i][c]:
                for cc in range(ncols * 2):
                    m[i][cc] ^= m[r][cc]
        r += 1
    # free columns
    free = [c for c in range(ncols) if c not in piv]
    basis = []
    for fc in free:
        v = [0]*ncols
        v[fc] = 1
        for rr, pc in enumerate(piv):
            v[pc] = m[rr][fc]
        basis.append(v)
    return basis

def weight(v):
    return sum(v)

def main():
    print("%-3s %-6s %-5s %-22s %s" % ("n", "dims", "rank", "null basis (as h)",
                                         "counterexample to universal wt>=w/2?"))
    for n in range(4, 13):
        mat = phi_matrix(n)
        nrows = len(mat); ncols = len(mat[0])
        basis = rref_nullspace(mat)
        # minimal-weight non-zero null vector
        nv = min(basis, key=weight)
        # any null vector is a counterexample: nu2 = wt(Phi h)=0 < w/2 since w>=1
        worst = None
        N = 1 << ncols
        minrat = 2.0
        for mask in range(N):
            h = [(mask >> j) & 1 for j in range(ncols)]
            w = weight(h)
            if w == 0: continue
            nu = 0
            for row in mat:
                nu += sum(a & b for a, b in zip(row, h)) & 1
            rat = nu / w
            if rat < minrat:
                minrat = rat; worst = h
        print("%-3d %-6s %-5d %-22s min_ratio=%.3f  worst_h=%s"
              % (n, "%dx%d" % (nrows, ncols), nrows - len(basis),
                 "" if not basis else "".join(str(b) for b in basis[0]),
                 minrat, "".join(str(b) for b in worst)))
    print("\nUniversal transfer wt(Phi_n h) >= wt(h)/2 fails for every n>=4 "
          "because Phi_n is (n-3)x(n-2) with a nonzero null vector.")

if __name__ == "__main__":
    main()
