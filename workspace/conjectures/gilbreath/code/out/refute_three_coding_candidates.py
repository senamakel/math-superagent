#!/usr/bin/env python3
"""Grounding check for the three F2-supply candidates (nu2-code-minimum-distance,
f2-uncertainty-dyadic-spectral-mass, odometer-disjointness-subshift).

Computes, for n = 3..18, the transfer matrix Phi_n (rows k=2..n-2, cols j=2..n-1,
entry C(k-1, j-(n-k)) mod 2) and reports:
  - rank, nullity, kernel description
  - is the image the FULL output space F2^{n-3}? (i.e. full row rank)
  - d_min of the image code C_n = im(Phi_n)
  - min over h NOT in kernel of wt(Phi_n h)/wt(h)  (the "relative weight expansion"
    that candidate 1's refined target states, excluding the kernel)
  - whether the all-ones vector is in the LEFT nullspace (column sums).
"""
from itertools import product

def Cmod2(a, b):
    if b < 0 or b > a:
        return 0
    # C(a,b) mod 2 = 1 iff b & (a-b) == 0  (Lucas / Kummer no-carry)
    return 1 if (b & (a - b)) == 0 else 0

def phi_matrix(n):
    """rows k=2..n-2, cols j=2..n-1."""
    rows = []
    row_idx = []
    for k in range(2, n - 1):      # k = 2..n-2
        r = []
        for j in range(2, n):      # j = 2..n-1
            # entry C(k-1, j-(n-k)) mod 2 ; valid when 0 <= j-(n-k) <= k-1
            e = Cmod2(k-1, j-(n-k))
            r.append(e)
        rows.append(r)
        row_idx.append(k)
    return rows, row_idx

def rank_and_kernel(M):
    # Gaussian elimination over F2; M is list of rows (list of ints)
    # returns rank and a basis of the right kernel (in the column space)
    R = [list(r) for r in M]
    m = len(R)
    ncols = len(R[0]) if m else 0
    piv = []
    row = 0
    for col in range(ncols):
        # find pivot
        sel = None
        for i in range(row, m):
            if R[i][col] == 1:
                sel = i; break
        if sel is None:
            continue
        R[row], R[sel] = R[sel], R[row]
        for i in range(m):
            if i != row and R[i][col] == 1:
                for c in range(ncols):
                    R[i][c] ^= R[row][c]
        piv.append(col)
        row += 1
    rank = row
    # free columns -> kernel basis
    free = [c for c in range(ncols) if c not in piv]
    kernel = []
    for f in free:
        x = [0]*ncols
        x[f] = 1
        for pi, pr in zip(piv, R[:rank]):
            # R[pi][f] is 1 if free column appears in pivot row
            if pr[f] == 1:
                x[pi] = 1
        kernel.append(x)
    return rank, kernel

def min_ratio(rows, n):
    """min over nonzero h not in kernel of wt(Phi_n h)/wt(h)."""
    m = len(rows[0])  # number of cols = n-2
    import itertools
    best = None
    best_h = None
    # kernel = span(all-ones) per run; but compute generically by checking Phi h == 0
    for h in itertools.product([0,1], repeat=m):
        wh = sum(h)
        if wh == 0:
            continue
        out = [0]*len(rows)
        for i, r in enumerate(rows):
            out[i] = sum(r[j]*h[j] for j in range(m)) & 1
        if sum(out) == 0:
            continue  # in kernel
        ratio = sum(out)/wh
        if best is None or ratio < best:
            best = ratio; best_h = h
    return best, best_h

def min_code_distance(rows, n):
    """d_min of image code = min over nonzero codewords wt(c)."""
    import itertools
    m = len(rows[0])
    best = None
    for h in itertools.product([0,1], repeat=m):
        out = [0]*len(rows)
        for i, r in enumerate(rows):
            out[i] = sum(r[j]*h[j] for j in range(m)) & 1
        w = sum(out)
        if w == 0:
            continue
        if best is None or w < best:
            best = w
    return best

print("n | shape(rows) cols | rank | nullity | im=full? | d_min(img) | min ratio h!in ker")
for n in range(3, 17):
    rows, row_idx = phi_matrix(n)
    m = len(rows[0]) if rows else 0
    nr = len(rows)
    rank, kernel = rank_and_kernel(rows)
    nullity = m - rank
    im_full = (rank == nr) and (nr == m)   # square & full rank => full space
    # im is full output space iff rank == nr (number output coords)
    im_full = (rank == nr)
    dm = min_code_distance(rows, n)
    best_ratio, best_h = min_ratio(rows, n)
    print(f"{n} | {nr}x{m} | {rank} | {nullity} | {im_full} | {dm} | {best_ratio}")

# Also verify: is all-ones in LEFT nullspace for n=8, n=12?
for n in (8, 12):
    rows, _ = phi_matrix(n)
    # column sums
    cols = len(rows[0])
    colsum = [sum(rows[i][j] for i in range(len(rows))) & 1 for j in range(cols)]
    print(f"n={n}: column sums (all-ones in left nullspace) = {colsum}")
