# Clean holonomic (P-recursive) test for D(N).
# Goal: find polynomials p_0..p_m with  sum_{j=0}^{m} p_j(N) D[N+j] = 0
# for all N, fit over D(0..14). Then EXTEND to D(20) and D(100) using the
# recurrence (assuming p_m(N) != 0), and check against statement values:
#   D(20)=9204559704,  D(100) mod 1e9 = 780166455.
# These held-out values are the falsifiers: any recurrence that misses them is dead.
from sympy import Rational, Matrix, symbols

D = [1, 1, 3, 9, 30, 99, 336, 1134, 3855, 13086, 44499, 151263,
     514419, 1749267, 5949063]
NTERM = len(D)   # 15 terms, indices 0..14
n = symbols('n')

def fit(m, d):
    # unknowns a[j][t] for j=0..m, t=0..d   (p_j(N)=sum_t a[j][t] N^t)
    # We fix p_m monic? Leave free; nullspace gives all solutions.
    ncols = (m+1)*(d+1)
    rows = NTERM - m        # recurrences for N = 0,1,...,NTERM-m-1
    A = Matrix.zeros(rows, ncols)
    for i in range(rows):
        col = 0
        for j in range(m+1):
            for t in range(d+1):
                A[i, col] = Rational(D[i+j]) * (i**t)
                col += 1
    return A.nullspace()

def extend_holonomic(m, d, sol):
    # p_j(N) = sum_t sol[j*(d+1)+t] N^t
    # recurrence: sum_{j=0}^{m} p_j(N) D[N+j] = 0  -> solve for D[N+m]
    seq = list(D)
    for N in range(0, 101):   # N value used in recurrence
        # want D[N+m] as next term; it is index N+m in seq
        if N + m <= len(seq)-1:
            continue
        if N + m > len(seq):
            break  # cannot fill (shouldn't happen)
        # next term is seq[len(seq)] = D[N+m] with N = len(seq)-m
        Ncur = len(seq) - m   # equivalent
        num = sum(sum(sol[j*(d+1)+t]*(Ncur**t) for t in range(d+1)) * Rational(seq[Ncur+j]) for j in range(m))
        den = sum(sol[m*(d+1)+t]*(Ncur**t) for t in range(d+1))
        val = -num/den
        if val.denominator != 1:
            return None   # non-integer -> refuted
        seq.append(val)
    return seq

found_any = False
for m in range(1, 7):
    for d in range(1, 5):
        ns = fit(m, d)
        if not ns:
            continue
        for sol in ns:
            found_any = True
            ext = extend_holonomic(m, d, sol)
            if ext is None:
                continue
            d20 = ext[20]
            d100m = ext[100] % (10**9)
            match20 = (d20 == 9204559704)
            match100 = (d100m == 780166455)
            tag = "*** MATCH BOTH ***" if (match20 and match100) else \
                  ("match20 only" if match20 else ("match100 only" if match100 else ""))
            print(f"m={m} d={d}: D20={d20} (match20={match20}), D100mod={d100m} (match100={match100}) {tag}")
            if match20 and match100:
                print("  polynomials:")
                for j in range(m+1):
                    pj = sum(sol[j*(d+1)+t]*n**t for t in range(d+1))
                    print(f"    p_{j} = {pj}")
print("done")
