#!/usr/bin/env python3
"""Sparse-image curve of the rectangular fold Phi_n: max_{wt(h) <= k} wt(Phi_n h).

SUPPLY (problem.md): nu2(n) = wt(Phi_n h) over F2, h the prime gap-parity string,
Phi_n the Pascal-mod-2 / Rule-90 fold with entries C(k-1, j-(n-k)) mod 2. By Lucas
(C(d,i) odd iff i submask of d), the depth-d image cell is the XOR of the input
over binary submasks of d.

This is the shared first move of the two RIVAL gaps in problem.md:
  - G-weak-input-strictness (weak-input-fold.md): does some k-sparse h (wt(h)<=k
    with k=o(n)) still fold to wt(Phi_n h) >= eps n ?  If yes -> the fold does work
    the frequency form cannot see.
  - G-eq-sparse-fold-is-sublinear (switch-equivalence.md): is max_{wt(h)<=k} wt(Phi_n h)
    = o(n) as k=delta n -> 0 ?  If yes -> SUPPLY is equivalent to switch density.

Both directions are the SAME finite computation: the curve
    f_n(k) = max { wt(Phi_n h) : h in F2^m, wt(h) <= k },
with the exact matrix Phi_n (entries C(row, col) mod 2) and exact image weights.

Cost: brute-force is exponential in the domain dimension (2^m inputs per n), so
this is an ORACLE only, kept at small n (domain m <= 16).
complexity_class: exponential, oracle_bound: m <= 16 (n <= 18).

Also computes the rank / nullity of Phi_n directly over F2 (gaussian elimination),
to check the imported fact rank = n-3, nullity 1, and to test whether Bacher's
symmetric-Pascal determinant/LU structure (bacher-pascal-det-mod2) transfers to
the rectangular offset Phi_n: we compare rank(Phi_n) against the rank of the
symmetric Pascal matrix P(D) of matching size.
"""
import itertools


def parity_comb(nn, rr):
    """C(nn,rr) odd iff rr is a bitwise submask of nn (Lucas p=2)."""
    return (rr & ~nn) == 0


def phi_rows_lucas(n):
    """Phi_n rows via Lucas (parity_comb) - the fast, independent route. nrows=n-1,
    columns j=0..n-1 with C(k-1, j-(n-k)) odd."""
    rows = []
    for k in range(1, n):
        row = {}
        for j in range(n):
            r = j - (n - k)
            if 0 <= r <= k - 1 and parity_comb(k - 1, r):
                row[j] = 1
        rows.append(row)
    return rows


def image_weight(n, h):
    """wt(Phi_n h) for a domain vector h (list of bits indexed by the column set
    0..ncols-1). Uses the matrix built by phi_rows_lucas, exact."""
    rows = phi_rows_lucas(n)
    wt = 0
    for row in rows:
        s = 0
        for j in row:
            if j < len(h):
                s ^= h[j]
        wt += s
    return wt


def max_weight_sparse(n, k):
    """max wt(Phi_n h) over h in F2^m with wt(h) <= k. Brute force over domain."""
    m = n - 2  # domain dimension (imported: rank+nullity = n-2, nullity 1)
    best = 0
    besth = None
    for bits in itertools.product([0, 1], repeat=m):
        if sum(bits) <= k:
            w = image_weight(n, bits)
            if w > best:
                best = w
                besth = bits
    return best, besth


def gauss_rank(rows, ncols):
    """F2 rank of the (nrows x ncols) matrix given as list of row dicts.
    Returns the number of pivot columns found. Also returns the nullity if we
    know the domain dim."""
    # build a dense columnmaj = list of row ints
    mat = []
    for row in rows:
        x = 0
        for j in row:
            x |= (1 << j)
        mat.append(x)
    nrows = len(mat)
    rank = 0
    # reduce rows
    for col in range(ncols - 1, -1, -1):
        piv = None
        for i in range(rank, nrows):
            if (mat[i] >> col) & 1:
                piv = i
                break
        if piv is None:
            continue
        mat[rank], mat[piv] = mat[piv], mat[rank]
        for i in range(nrows):
            if i != rank and ((mat[i] >> col) & 1):
                mat[i] ^= mat[rank]
        rank += 1
    return rank


def symmetric_pascal_rank(D):
    """rank over F2 of symmetric Pascal P(D) entries C(s+t, s) mod 2, 0<=s,t<D."""
    import math
    rows = []
    for s in range(D):
        row = {}
        for t in range(D):
            if math.comb(s + t, s) % 2 == 1:
                row[t] = 1
        rows.append(row)
    return gauss_rank(rows, D)


if __name__ == "__main__":
    import math
    print("=== Phi_n rank/nullity (over F2), and symmetric-Pascal comparison ===")
    print(f"{'n':>3} {'nrows':>5} {'ncols':>5} {'rank':>5} {'nullity':>7} {'sum':>3} {'P-rank':>6}")
    for n in range(4, 15):
        rows = phi_rows_lucas(n)
        ncols = n
        rk = gauss_rank(rows, ncols)
        dom = n - 2
        nullity = dom - rk
        # compare to symmetric Pascal of size D = min(nrows, ncols)
        D = min(n - 1, ncols)
        prk = symmetric_pascal_rank(D)
        print(f"{n:>3} {n-1:>5} {ncols:>5} {rk:>5} {nullity:>7} {rk+nullity:>3} {prk:>6}")

    print()
    print("=== Sparse-image curve: max_{wt(h)<=k} wt(Phi_n h) ===")
    print(f"{'n':>3} {'m':>3} |   k=0   k=ceil(m/8)   k=ceil(m/4)   k=floor(m/2)   m")
    for n in range(4, 17):
        m = n - 2
        nrows = n - 1
        cells = []
        for k in [0, max(1, m // 8), max(1, m // 4), m // 2, m]:
            best, _ = max_weight_sparse(n, k)
            cells.append(best)
        print(f"{n:>3} {m:>3} |   {cells[0]:<4}  {cells[1]:<12}  {cells[2]:<12}  {cells[3]:<12}  {cells[4]}")
