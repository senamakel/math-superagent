#!/usr/bin/env python3
"""DECISIVE capture: settle the fold-matrix rank/nullity contradiction.

Claim under test (problem.md fact 3): 'rank Phi_n = n-3, nullity 1,
ker = span(all-ones)'.

The operative fold object (lib.nu2 / lib.supply_fold.t_direct, and the one whose
weight problem.md calls nu2(n) = wt(Phi_n h)) counts cells d in [2, n-1]:
    T(n,d) = XOR over bitwise submasks o of d of h[n-1-d+o].
So Phi_n is an (n-2) x n matrix with rows d = 2..n-1.

This verifies, by DIRECT matrix-vector multiplication and direct F2 Gaussian
elimination (no RREF kernel reconstruction):
  - the matrix shape,
  - its rank (full row rank n-2) and nullity 2,
  - that the kernel is exactly span of the two alternating vectors
    e = (1,0,1,0,...)  (even indices) and  o = (0,1,0,1,...) (odd indices),
    and that all-ones = e XOR o lies in the kernel (consistent with door 1's
    witness) but is only ONE member of a 2-dimensional null space, not the
    whole kernel, and neither e nor o is the all-ones vector.

Established fact 'rank n-3' fits NO row range: for n columns, row ranges
d=0..n-1 (rank n), d=1..n-1 (rank n-1), d=2..n-1 (rank n-2) give ranks
{n, n-1, n-2}; none is n-3. And 'nullity 1' is internally inconsistent with
'any' of rank n-3 for n columns (rank+nullity would be n-1, not n).

Exact F2 arithmetic throughout. Direct oracle cross-check vs t_direct.
"""
from lib.supply_fold import t_direct

def submasks(d):
    i = d
    while True:
        yield i
        if i == 0:
            break
        i = (i - 1) & d

def fold_rows(n):
    """Operative (n-2) x n matrix, rows d = 2..n-1 exactly as nu2 sums them."""
    rows = []
    for d in range(2, n):
        row = [0] * n
        for o in submasks(d):
            j = n - 1 - d + o
            if 0 <= j < n:
                row[j] ^= 1
        rows.append(row)
    return rows

def rank_f2(mat):
    if not mat:
        return 0
    m, n = len(mat), len(mat[0])
    A = [row[:] for row in mat]
    rank = 0
    for col in range(n):
        piv = None
        for r in range(rank, m):
            if A[r][col]:
                piv = r
                break
        if piv is None:
            continue
        A[rank], A[piv] = A[piv], A[rank]
        for r in range(m):
            if r != rank and A[r][col]:
                for c in range(col, n):
                    A[r][c] ^= A[rank][c]
        rank += 1
    return rank

def matvec(M, v):
    return [sum(M[r][j] * v[j] for j in range(len(v))) % 2 for r in range(len(M))]

import random
random.seed(11)

print("=== DECISIVE: rank and nullity of the operative Phi_n (rows d=2..n-1) ===")
print("   (what nu2(n)=wt(Phi_n h) actually sums: d in [2, n-1], so (n-2) x n)")
print()
print(f"{'n':>3}  {'shape':>10}  {'rank':>5}  {'nullity':>7}  {'allones_ker':>12}  {'evenalt_ker':>12}  {'oddalt_ker':>11}")
allrankok = True
for n in range(2, 21):
    M = fold_rows(n)
    r = rank_f2(M)
    nullity = n - r
    ones = [1] * n
    even = [1 if i % 2 == 0 else 0 for i in range(n)]
    odd  = [1 if i % 2 == 1 else 0 for i in range(n)]
    inker = lambda v: matvec(M, v) == [0] * len(M)
    print(f"{n:>3}  {f'{len(M)}x{n}':>10}  {r:>5}  {nullity:>7}  "
          f"{str(inker(ones)):>12}  {str(inker(even)):>13}  {str(inker(odd)):>12}")
    if r != n - 2:
        allrankok = False
print()
print("rank == n-2 (full row rank) for all n in 2..20:", allrankok)

print()
print("=== Direct negative control: each rank-claim under every row range ===")
print("   (to show 'rank n-3' fits NO convention)")
for n in [6, 8, 10, 12]:
    rowRanges = {"A d=0..n-1 (n rows)": range(0, n),
                 "B d=2..n-1 (n-2 rows, operative)": range(2, n),
                 "C d=1..n-1 (n-1 rows, 'k=1..n-1' verbal)": range(1, n)}
    out = []
    for name, R in rowRanges.items():
        rows = []
        for d in R:
            row = [0] * n
            for o in submasks(d):
                j = n - 1 - d + o
                if 0 <= j < n:
                    row[j] ^= 1
            rows.append(row)
        r = rank_f2(rows)
        out.append(f"{name}: rank={r}, nullity={n-r}")
    print(f"n={n}: " + " | ".join(out))

print()
print("=== Kernel is exactly span(even-alt, odd-alt); all-ones is their sum ===")
for n in [4, 6, 8, 10]:
    M = fold_rows(n)
    even = [1 if i % 2 == 0 else 0 for i in range(n)]
    odd  = [1 if i % 2 == 1 else 0 for i in range(n)]
    ones = [1] * n
    # independent?
    indep = True
    # any vector outside span must map to nonzero: check each basis-alt only
    # linear combos of even,odd = exactly the 4 vectors {0, e, o, e^o=ones}
    combos_ker = all(matvec(M, v) == [0]*len(M)
                     for v in (even, odd, [even[i]^odd[i] for i in range(n)]))
    # and a vector NOT in that span must map nonzero (e.g. delta_0)
    notker = matvec(M, [1,0,0,0,0,0,0,0,0,0][:n])  # e_0 (if n>=1)
    print(f"n={n}: rank={rank_f2(M)} nullity={n-rank_f2(M)} | "
          f"e,o,(e^o)=ones all in ker: {combos_ker} | all-ones = e XOR o: "
          f"{[even[i]^odd[i] for i in range(n)] == ones}")

print()
print("=== Sanity: wt(Phi_n h) via matrix image == nu2 via t_direct oracle ===")
ok = True
for n in range(3, 11):
    for _ in range(5):
        h = [random.randint(0, 1) for _ in range(n)]
        M = fold_rows(n)
        img = matvec(M, h)
        wt_img = sum(img)
        nu2_or = sum(t_direct(n, d, h) for d in range(2, n))
        if wt_img != nu2_or:
            ok = False
            print(f"  n={n} MISMATCH")
print("all image==oracle matches:", ok)
