"""Test R-random-pointwise: for h uniform on the domain of Phi_n, is
wt(Phi_n h) >= n/4 with probability 1 - exp(-Omega(n))?

Build the ACTUAL fold matrix matching nu2: row d (d in [2,n-1]) has a 1 in
column j = n-1-d+o for each bitwise submask o of d. Sample random h, measure
wt(Phi_n h) distribution, and check P(wt < n/4).

Also compute rank of this matrix over F2 to see the image dimension.
"""
import random


def submask_cols(d, n):
    cols = []
    for o in range(d + 1):
        if (o & d) == o:
            j = n - 1 - d + o
            if 0 <= j < n:
                cols.append(j)
    return cols


def build_matrix(n):
    rows = []
    for d in range(2, n):          # d in [2, n-1]
        rows.append(submask_cols(d, n))
    return rows


def gauss_rank(rows, ncols):
    mat = []
    for row in rows:
        x = 0
        for j in row:
            x |= (1 << j)
        mat.append(x)
    rank = 0
    for col in range(ncols - 1, -1, -1):
        piv = None
        for i in range(rank, len(mat)):
            if (mat[i] >> col) & 1:
                piv = i
                break
        if piv is None:
            continue
        mat[rank], mat[piv] = mat[piv], mat[rank]
        for i in range(len(mat)):
            if i != rank and ((mat[i] >> col) & 1):
                mat[i] ^= mat[rank]
        rank += 1
    return rank


def wt_image(rows, n, h):
    wt = 0
    for row in rows:
        s = 0
        for j in row:
            if j < len(h):
                s ^= h[j]
        wt += s
    return wt


for n in [16, 32, 64]:
    rows = build_matrix(n)
    nrows = len(rows)           # n-2
    rk = gauss_rank(rows, n)
    print(f"n={n:4d} rows={nrows:3d} rank={rk:3d} nullity={n-rk:2d}")
    # sample random h (dimension n), count wt(Phi h) < n/4
    S = 4000
    below = 0
    wts = []
    for _ in range(S):
        h = [random.getrandbits(1) for _ in range(n)]
        w = wt_image(rows, n, h)
        wts.append(w)
        if w < n / 4:
            below += 1
    mean_w = sum(wts) / S
    print(f"   mean wt={mean_w:.2f}  n/4={n/4}  P(wt<n/4)={below/S:.4f}  min_wt={min(wts)}")
