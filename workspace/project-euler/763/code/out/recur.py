import sympy as sp
import math

D = [1, 1, 3, 9, 30, 99, 336, 1134, 3855, 13086, 44499, 151263, 514419, 1749267, 5949063]
N = len(D)
n = sp.symbols('n')

print("n terms:", N)

# ---------- Task 1: constant-coefficient linear recurrence, orders 1..7 ----------
def det_constant(order):
    # Try to find c0..c_{order-1} with D[i+order] = sum c_j D[i+j] for all i -> overdetermined least squares exact
    # Build linear system A x = b where rows are (D[i],D[i+1],...,D[i+order-1]) and b=D[i+order]
    rows = N - order
    A = sp.zeros(rows, order)
    b = sp.zeros(rows, 1)
    for i in range(rows):
        for j in range(order):
            A[i, j] = D[i + j]
        b[i] = D[i + order]
    aug = A.row_join(b)
    r = aug.rref()
    rr = r[0]
    # Check consistency of rref
    for i in range(rows):
        if rr[i, order] != 0 and all(rr[i, j] == 0 for j in range(order)):
            return None  # inconsistent
    # consistent: solve
    sol = sp.linsolve((A, b))
    return sol

for order in range(1, 8):
    if N - order < 1:
        break
    sol = det_constant(order)
    print(f"order {order}: fits={sol != sp.EmptySet and sol is not None}", sol if (sol is not None and sol != sp.EmptySet) else "")

# Also solve with free variables - count if any solution exists
print("\nHand-check: any order-2..7 constant coeff recurrence with free vars?")
# For underdetermined check we can't easily; but overdetermined above suffices.

# ---------- Task 2: P-recursive (holonomic) recurrence ----------
# form: sum_{k=0}^{m} p_k(n) D[n+k] = 0 with p_k polynomial in n of degree d (at least one).
# Let's fit small total parameter counts. We'll solve a linear system over unknown coefficients
# of the p_k polynomials, using n from 0.. (N-2), requiring equation hold for each n.
# Choose m (order) and d (degree). Unknowns count = (m+1)*(d+1). Equations = N-m.
# We need (m+1)*(d+1) <= N-m roughly for a unique-ish fit, but holonomic needs flexible.

def fit_holonomic(m, d):
    # unknowns: coefficients a[k][j] for poly p_k(n)=sum_j a[k][j]*n^j
    # equation for n = n0: sum_k p_k(n0)*D[n0+k] = 0
    # Build matrix with (m+1)*(d+1) columns
    ncols = (m + 1) * (d + 1)
    rows_eq = N - m
    A = sp.zeros(rows_eq, ncols)
    for n0 in range(rows_eq):
        col = 0
        for k in range(m + 1):
            val = sp.Integer(D[n0 + k])
            for j in range(d + 1):
                A[n0, col] = val * (n0 ** j)
                col += 1
    # null space
    ns = A.nullspace()
    return ns

print("\n--- P-recursive search (order m, degree d) ---")
for m in range(1, 6):
    for d in range(0, 4):
        ns = fit_holonomic(m, d)
        if ns:
            dim = len(ns)
            print(f"order {m}, deg {d}: nullspace dim={dim}")
            if dim == 1:
                sol = ns[0]
                print("   solution coeffs:", list(sol))
        else:
            if m * d < 30:
                print(f"order {m}, deg {d}: no (trivial) solution")

# ---------- Task 3: asymptotic fit ----------
# Assume D(N) ~ C * r^N * N^alpha. Use pairs of ratios.
print("\n--- growth ratios ---")
for i in range(1, N):
    print(f"{D[i]}/{D[i-1]} = {D[i]/D[i-1]:.8f}")
