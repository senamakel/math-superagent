# Test whether D(N) is holonomic (P-recursive): find a recurrence
#   sum_{j=0}^{m} p_j(N) D[N+j] = 0  with p_j polynomials in N
# fitted over D(0..14), then PREDICT D(20) and D(100) mod 10^9 and check
# against the statement's held-out values (perfect falsifiers).
from sympy import Rational, symbols, Matrix, linsolve

D = [1, 1, 3, 9, 30, 99, 336, 1134, 3855, 13086, 44499, 151263,
     514419, 1749267, 5949063]
N = len(D)  # 15 terms: D[0..14]

n = symbols('n')

def fit_holonomic(m, d):
    # unknown coefficients a[j][t] for p_j(N)=sum_t a[j][t] N^t, j=0..m
    # equation for each base index i: sum_j p_j(i) D[i+j] = 0, i=0..N-m-1
    ncols = (m+1)*(d+1)
    rows = N - m
    A = Matrix.zeros(rows, ncols)
    for i in range(rows):
        col = 0
        for j in range(m+1):
            for t in range(d+1):
                A[i, col] = Rational(D[i+j]) * (i**t)
                col += 1
    ns = A.nullspace()
    return ns, A, rows, ncols

best = None
for m in [1,2,3,4]:
    for d in [1,2,3,4]:
        ns, A, rows, ncols = fit_holonomic(m, d)
        if ns:
            print(f"order m={m} deg d={d}: nullspace dim={len(ns)} (cols={ncols}, rows={rows})")
            if len(ns) == 1:
                best = (m, d, ns[0])
# take a single-nullspace solution if found
if best is None:
    # pick lowest-order solution even if multidimensional; use it directly
    for m in [1,2,3,4]:
        for d in [1,2,3,4]:
            ns, A, rows, ncols = fit_holonomic(m,d)
            if ns:
                best=(m,d,ns[0])
                break
        if best: break

m,d,sol = best
print(f"\nUsing order m={m}, deg d={d}, coeff vector (p_0..p_{m} stacked by degree):")
print(list(sol))
# rebuild p_j(N)
p = []
for j in range(m+1):
    poly = 0
    for t in range(d+1):
        poly += sol[j*(d+1)+t]*n**t
    p.append(poly)
print("polynomials p_j(N):")
for j,pol in enumerate(p):
    print(f"  p_{j} = {pol}")

# Now extend sequence using this recurrence, from base terms
def extend(seq, target):
    out = list(seq)
    for i in range(len(seq)-m-1, target+1):
        if i >= len(out)-m-1... 
