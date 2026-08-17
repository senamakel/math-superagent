"""Diagnose the genuine-vs-vacuous recurrence fits for A_m (n=11 points).

Key issue: with n=11 points, an order-L recurrence has (n-L) consecutive
equations in L unknowns (L+1 for affine). The fit is a GENUINE constraint only
when the system is overdetermined: n-L > L  <=>  L < n/2 = 5.5. For L=6,7,8
the system is underdetermined and always solvable — those "fits" are vacuous.

Also debug the affine L=5 "fits but fails verify" anomaly from the main program.
"""
import os, sys
sys.path.insert(0, "/workspace/code")
M = 101001001
A = [1, 101, 20302, 2250400, 65706380, 60501668, 67421978,
     5792364, 65085883, 67821910, 53692412]
n = len(A)

from lib.recurrences import berlekamp_massey, verify_recurrence
from lib.recurrences import rational_reconstruct
from task_fib_subseq import has_recurrence, verify, solve_basic, gauss_rank  # local

def test(L, affine):
    rows = []
    for j in range(L, n):
        row = [A[j-1-i] for i in range(L)]
        if affine:
            row.append(1)
        row.append(A[j])
        rows.append(row)
    aug = gauss_rank(rows)
    hon = gauss_rank([r[:-1] for r in rows])
    return aug, hon, len(rows), L + (1 if affine else 0)

print("n =", n)
print("Overdetermined iff equations (n-L) > unknowns (L or L+1).")
print()
print("HOMOGENEOUS")
for L in range(1, 9):
    aug, hon, neq, ncol = test(L, False)
    over = neq > L
    print("  L=%2d: eqns=%2d unknowns=%2d  rank(aug)=%d rank(coef)=%d  "
          "consistent=%s  overdetermined=%s" % (L, neq, L, aug, hon, aug==hon, over))
print()
print("AFFINE")
for L in range(1, 9):
    aug, hon, neq, ncol = test(L, True)
    over = neq > ncol
    print("  L=%2d: eqns=%2d unknowns=%2d  rank(aug)=%d rank(coef)=%d  "
          "consistent=%s  overdetermined=%s" % (L, neq, ncol, aug, hon, aug==hon, over))
print()

# Debug affine L=5: is the system consistent, and does ANY solution verify?
L = 5
ok, sol = has_recurrence(A, L, affine=True)
print("affine L=5: has_recurrence consistent=", ok, " sol=", sol)
vok, bad = verify(A, sol, affine=True)
print("  verify:", vok, "bad idx", bad)
# print the individual residuals
coefs = sol[:-1]; d = sol[-1]
print("  coefs=", coefs, "d=", d)
for j in range(L, n):
    total = d
    for i in range(L):
        total = (total + coefs[i]*A[j-1-i]) % M
    if total != A[j] % M:
        print("   j=%d: pred=%d actual=%d  DIFF" % (j, total, A[j]%M))
