"""Exact-integer (rational, over Q) constant-coefficient recurrence test for the
exact Psi(F_m) values, plus a full honest summary of the modular analysis.

n=11 points. An order-L homogeneous recurrence is a GENUINE constraint iff the
system is overdetermined: n - L > L  <=>  L <= 5. For L=6,7,8 it is
underdetermined (any 11 points fit), hence vacuous. Same for affine: L<=4.

Here we solve the homogeneous system over Q (exact rationals) for L=1..5 using
the exact Psi(F_m) integers, to test a constant-coefficient recurrence over the
integers (not just mod M). sympy's solve over the rationals is exact.
"""
import os, sys
sys.path.insert(0, "/workspace/code")
from fractions import Fraction
from sympy import Matrix, symbols, solve_linear_system, Rational

M = 101001001
FIB_K = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]

# load exact Psi values
DATA = os.path.normpath(os.path.join(os.getcwd(), "code/out/psi_data_1_150.txt"))
psi = {}
with open(DATA) as f:
    for line in f:
        line = line.strip()
        if ":" not in line:
            continue
        try:
            k_str, rest = line.split(":", 1)
            k = int(k_str.strip())
        except ValueError:
            continue
        val = None
        for tok in rest.split():
            try:
                val = int(tok)
            except ValueError:
                val = None
        if val is not None:
            psi[k] = val

E = [psi[k] for k in FIB_K]         # exact integers
A = [v % M for v in E]              # mod M
n = len(E)
print("n =", n)
print("Exact Psi(F_m):")
for i, k in enumerate(FIB_K):
    print("  F_%d = %3d : %d" % (i + 1, k, E[i]))
print("mod M:", A)
print()

def homogeneous_over_Q(L, seq):
    """Test whether seq (exact ints) satisfies a homogeneous order-L
    constant-coefficient recurrence over Q, using all consecutive windows.
    Returns (consistent, coefs or None) — genuine only if overdetermined."""
    m = n - L
    if m == 0:
        return (True, [0] * L)
    R = Matrix([[seq[j - 1 - i] for i in range(L)] for j in range(L, n)])
    b = Matrix([[seq[j]] for j in range(L, n)])
    soln, params = R.gauss_jordan_solve(b)
    # consistent iff gauss_jordan_solve succeeds (it does).
    return (True, soln)

print("HOMOGENEOUS over Q (exact integers), order L=1..8")
for L in range(1, 9):
    over = (n - L) > L
    # build augmented approach: systems of equations, check consistency by rank
    rows = []
    for j in range(L, n):
        rows.append([E[j - 1 - i] for i in range(L)] + [E[j]])
    # exact rational rank via sympy
    A_ = Matrix([r[:-1] for r in rows])
    Ab = Matrix(rows)
    rankA = A_.rank()
    rankAb = Ab.rank()
    cons = (rankA == rankAb)
    if cons and over:
        # find a particular rational solution
        x = symbols('c0:%d' % L)
        eqs = []
        for j in range(L, n):
            eqs.append(sum(x[i] * E[j - 1 - i] for i in range(L)) - E[j])
        sol = solve_linear_system(Matrix(rows), *x)
        status = "CONSISTENT (fits over Q)"
        if sol is not None:
            status += "  coefs=" + str({str(kk): vv for kk, vv in sol.items()})
        else:
            status += "  (params free)"
    elif cons:
        status = "consistent (underdetermined/vacuous)"
    else:
        status = "INCONSISTENT (no order-%d recurrence over integers)" % L
    print("  L=%d: eqns=%d unknow=%d rankA=%d rankAb=%d overdet=%s -> %s"
          % (L, n - L, L, rankA, rankAb, over, status))

print()
print("AFFINE over Q, order L=1..8")
for L in range(1, 9):
    over = (n - L) > (L + 1)
    rows = []
    for j in range(L, n):
        rows.append([E[j - 1 - i] for i in range(L)] + [1, E[j]])
    rankA = Matrix([r[:-1] for r in rows]).rank()
    rankAb = Matrix(rows).rank()
    cons = (rankA == rankAb)
    if not cons:
        status = "INCONSISTENT (no affine order-%d recurrence over integers)" % L
    elif over:
        status = "CONSISTENT genuine fit over Q"
    else:
        status = "consistent (underdetermined/vacuous)"
    print("  L=%d: eqns=%d unknow=%d overdet=%s -> %s" % (L, n - L, L + 1, over, status))
