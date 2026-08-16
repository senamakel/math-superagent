"""Determine the ACTUAL SUPPLY fold matrix from the definition in problem.md and
check its rank and image weight against measured nu2.

Definition: fold cell at depth d (d in [2, n-1]) over h indexed 0..n-1 is
    T(n,d) = XOR over bitwise submasks o of d of  h[n-1-d+o].
So row d has a 1 in column j = n-1-d+o for each submask o of d.
Columns j in 0..n-1.
"""
import itertools


def parity_comb(nn, rr):
    return (rr & ~nn) == 0


def submask_cols(d, n):
    """columns j in 0..n-1 where row d has a 1."""
    cols = []
    for o in range(d + 1):
        if (o & d) == o:
            j = n - 1 - d + o
            if 0 <= j < n:
                cols.append(j)
    return cols


def build_matrix(n, dlo, dhi):
    rows = []  # each row a set of column indices
    for d in range(dlo, dhi):
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


# measured nu2 for a few n (from nu2_terms.txt, floor-at-2 convention)
import numpy as np

def prime_gaps_mod2(N):
    # h[j] = ((q_{j+2} - q_{j+1})/2) mod 2 for j=0..N-1 (need primes up to enough)
    # use simple sieve
    limit = 20000
    sieve = bytearray(b'\x01')*(limit+1)
    sieve[0]=sieve[1]=0
    for i in range(2,int(limit**0.5)+1):
        if sieve[i]:
            sieve[i*i::i]=b'\x00'*(((limit-i*i)//i)+1)
    primes=[i for i in range(2,limit+1) if sieve[i]]
    h=[]
    for j in range(N):
        gp = primes[j+1]-primes[j]
        h.append((gp//2)%2)
    return h

for n in [8, 16, 32, 64, 100, 200, 400, 800]:
    rows = build_matrix(n, 2, n)  # d in [2, n-1]
    ncols = n
    rk = gauss_rank(rows, ncols)
    h = prime_gaps_mod2(n)
    wt = wt_image(rows, n, h)
    print(f"n={n:4d} rows(d=2..n-1)={len(rows):3d} rank={rk:3d} nullity={n-rk:2d} wt(Phi h)={wt:4d} nu2/n={wt/n:.3f}")

print()
print("Measured nu2 (from nu2_terms.txt): n=8:1 n=16:11 n=32:14 n=64:28 n=100:43 n=200:100")
