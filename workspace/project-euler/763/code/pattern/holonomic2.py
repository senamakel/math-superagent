# Search for a holonomic (P-recursive) recurrence for D(N):
#   sum_{j=0}^{m} p_j(N) D[N+j] = 0,  p_j polynomial in N of degree d.
# Fit on D(0..14), then PREDICT D(15..20) and compare D(20) against the
# statement's held-out 9204559704; and D(100) mod 1e9 vs 780166455.
# Any candidate that reproduces D(20) exactly (and D(100) mod 1e9) is
# a decisive structural result. A fit that misses D(20) is refuted.
from sympy import Rational, Matrix, symbols, linsolve, simplify

D = [1, 1, 3, 9, 30, 99, 336, 1134, 3855, 13086, 44499, 151263,
     514419, 1749267, 5949063]
NTERM = len(D)
n = symbols('n')

def fit(m, d):
    # unknowns a[j][t], j=0..m, t=0..d : p_j(N)=sum_t a[j][t]*N^t
    # equations: for i in 0..(NTERM-m-1): sum_j p_j(i)*D[i+j] = 0
    ncols = (m+1)*(d+1)
    rows = NTERM - m
    A = Matrix.zeros(rows, ncols)
    for i in range(rows):
        col = 0
        for j in range(m+1):
            v = Rational(D[i+j])
            for t in range(d+1):
                A[i,col] = v * (i**t)
                col += 1
    ns = A.nullspace()
    return ns

def make_polys(sol, m, d):
    p = []
    for j in range(m+1):
        poly = 0
        for t in range(d+1):
            poly += sol[j*(d+1)+t]*n**t
        p.append(poly)
    return p

def solve_for_newn(seq, m, p):
    # given last m values (seq ends at index idx), D[idx+1] solves
    # sum_{j=0}^{m} p_j(idx+1) D[idx+1+j] = 0  -> leading D[idx+m] term
    # Actually equation: sum_j p_j(N) D[N+j]=0 with N = current index-m+1?
    # Use: to extend seq to next value, we need one equation whose unknown is
    # the new last value. Take N = (len-1)-m+1 such that index of D[N+m] is last+1.
    pass

def extend(seq, m, d, p, target):
    # recurrence valid for N = 0.. ; D[N+m]= -(sum_{j<m} p_j(N)D[N+j])/p_m(N)
    out = list(seq)
    for N in range(0, target - m + 1):
        # index of D[N+m] = N+m ; we need this to be the NEXT element
        if N + m < len(out):
            continue
        if N + m > len(out):
            continue
        if N + m != len(out):
            continue
        num = sum(p[j].subs(n,N)*Rational(out[N+j]) for j in range(m))
        den = p[m].subs(n,N)
        val = -num/den
        # must be integer
        if val.denominator != 1:
            return None  # not integer
        out.append(val)
    return out

results = []
for m in range(1,6):
    for d in range(1,5):
        ns = fit(m,d)
        for sol in ns:
            p = make_polys(sol,m,d)
            # extend to D(20)
            ext = extend(list(D), m, d, p, 20)
            if ext is None:
                # try: recurrence may not produce integer at some step -> refuted
                continue
            d20 = ext[20]
            match20 = (d20 == 9204559704)
            # also extend to 100 for mod check
            ext100 = extend(list(D), m, d, p, 100)
            d100m = (ext100[100] % (10**9)) if ext100 is not None else None
            match100 = (d100m == 780166455)
            results.append((m,d,simplify(p[0]) is not None, match20, match100, d20 if not match20 else 'D20-ok'))
            print(f"m={m} d={d} (params={(m+1)*(d+1)}): D20={d20} match20={match20} D100mod={d100m} match100={match100}")

print("\nDone. Concise summary (only HOLONOMIC candidates that reproduce D(20)):")
if not results:
    pass
