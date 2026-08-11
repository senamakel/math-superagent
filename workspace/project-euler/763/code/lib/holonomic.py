# Shared holonomic (P-recursive) fit routine for the PE763 D(N) sequence.
#
# The definition lived (identically, not diverged) in code/pattern/holonomic2.py,
# holonomic3.py, holonomic_diag.py and holonomic_fit.py. It was identical in all
# four copies, so consolidation chose no one over another.
#
# fit(m, d, D): builds the linear system for a P-recursive recurrence
#     sum_{j=0}^{m} p_j(N) * D[N+j] = 0
# with p_j(N) = sum_{t=0}^{d} a[j][t] * N^t, one equation per base index
# i = 0..(len(D)-m-1):
#     sum_{j,t} D[i+j] * i^t * a[j][t] = 0
# and returns the (exact rational) nullspace of the coefficient matrix — every
# independent set of polynomials fitting the given D(0..len-1) exactly.
#
# Correctness: reproduces the nullspace that each of the four predecessor
# programs computed for their own D(0..14) table over the same (m,d) sweep.
import sympy
from sympy import Matrix, Rational

D_DEFAULT = [1, 1, 3, 9, 30, 99, 336, 1134, 3855, 13086, 44499, 151263,
             514419, 1749267, 5949063]


def fit(m, d, D=None):
    """Nullspace of the holonomic-fit matrix for order m, degree d.

    Returns a list of sympy vectors; each is one independent polynomial
    coefficient set p_0..p_m fitted over the sequence D (default D(0..14)).
    """
    if D is None:
        D = D_DEFAULT
    ncols = (m + 1) * (d + 1)      # unknowns a[j][t]
    rows = len(D) - m              # one recurrence per base index i
    A = Matrix.zeros(rows, ncols)
    for i in range(rows):
        col = 0
        for j in range(m + 1):
            v = Rational(D[i + j])
            for t in range(d + 1):
                A[i, col] = v * (i ** t)
                col += 1
    return A.nullspace()
