"""Debug the affine L=5 consistency/solver anomaly.
"""
import sys
sys.path.insert(0, "/workspace/code")
M = 101001001
A = [1, 101, 20302, 2250400, 65706380, 60501668, 67421978,
     5792364, 65085883, 67821910, 53692412]
n = 11
L = 5
from task_fib_subseq import has_recurrence, verify, solve_basic, gauss_rank, inv

# Build rows directly
rows = []
for j in range(L, n):
    row = [A[j-1-i] for i in range(L)]
    row.append(1)  # d column
    row.append(A[j])  # rhs
    rows.append(row)

print("n-L =", n-L, "equations, unknowns =", L+1)
print("rank(coef) =", gauss_rank([r[:-1] for r in rows]))
print("rank(aug)  =", gauss_rank(rows))

# Try sympy exact rational solution to the SAME system (as rationals, the
# integer values, to see if consistent over Q)
from sympy import Matrix, symbols, solve_linear_system
coef_cols = [r[:-1] for r in rows]
rhs = [r[-1] for r in rows]

# Solve over Q exactly
def exact_consistent():
    Aq = Matrix(coef_cols)
    Ab = Matrix(rows)
    return Aq.rank() == Ab.rank()
print("consistent over Q:", exact_consistent())

# Solve the square system mod M via direct linear solve
def solve_square(mat, rhs_v):
    # Gaussian solve
    Mx = len(mat)
    A_ = [row[:] for row in mat]
    b = rhs_v[:]
    for col in range(Mx):
        piv = None
        for r in range(col, Mx):
            if A_[r][col] % M != 0:
                piv = r; break
        if piv is None:
            return None
        A_[col], A_[piv] = A_[piv], A_[col]
        b[col], b[piv] = b[piv], b[col]
        pinv = inv(A_[col][col])
        for c in range(col, Mx):
            A_[col][c] = A_[col][c]*pinv % M
        b[col] = b[col]*pinv % M
        for r in range(Mx):
            if r != col and A_[r][col] % M != 0:
                f = A_[r][col] % M
                for c in range(col, Mx):
                    A_[r][c] = (A_[r][c] - f*A_[col][c]) % M
                b[r] = (b[r] - f*b[col]) % M
    x = [0]*Mx
    for i in range(Mx):
        x[i] = b[i] % M
    return x

# The 6 equations form a 6x6 square system (5 coefs + d). Solve it.
sq_mat = coef_cols
sq_rhs = rhs
sol = solve_square(sq_mat, sq_rhs)
print("direct square-system solution:", sol)

if sol is not None:
    coefs = sol[:5]; d = sol[5]
    print("verify direct solution:")
    for j in range(L, n):
        total = d
        for i in range(5):
            total = (total + coefs[i]*A[j-1-i]) % M
        print("  j=%d: pred=%d actual=%d %s" % (j, total, A[j]%M, "OK" if total==A[j]%M else "FAIL"))

# Now compare with solve_basic output
ok, sol2 = has_recurrence(A, L, affine=True)
print("has_recurrence sol:", sol2)
