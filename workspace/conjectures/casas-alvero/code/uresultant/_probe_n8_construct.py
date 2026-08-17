"""Probe: wall time for the n=8 traceless-slice Hasse resultant construction.

No Singular, no capture write. Measures slice_resultants(n=8) term-ops and the
weighted-order pass, so extend_n8_capture.py can be planned with a real budget.

Usage: python uresultant/_probe_n8_construct.py
"""
import time
from sympy import symbols, Poly, expand, resultant, binomial
from sympy import QQ as sympy_QQ


def hasse(f, i):
    p = Poly(expand(f), x)
    c = {j: p.coeff_monomial(x ** j) for j in range(p.degree() + 1)}
    return sum(binomial(j, i) * cc * x ** (j - i)
               for j, cc in c.items() if j >= i)


def slice_resultants(n):
    a = symbols(f"a_1:{n+1}")
    f = x ** n + sum(a[i] * x ** (n - 1 - i) for i in range(n))
    return [expand(resultant(f, hasse(f, i), x).subs(a[0], 0)) for i in range(1, n)]


def weighted_order(poly, n):
    a = symbols(f"a_1:{n+1}")
    sl = list(a[1:])
    W = list(range(2, n + 1))
    P = Poly(poly, *sl, domain=sympy_QQ)
    return min(sum(e * w for e, w in zip(m, W)) for m, c in P.terms())


if __name__ == "__main__":
    x = symbols("x")
    n = 8
    t0 = time.time()
    R = slice_resultants(n)
    t1 = time.time()
    print(f"n={n}: construction {t1 - t0:.1f}s; term-ops={[r.count_ops() for r in R]}")
    t2 = time.time()
    ords = [weighted_order(r, n) for r in R]
    t3 = time.time()
    print(f"n={n}: weighted orders {t3 - t2:.1f}s; ords={ords}; expected={[n*(n-i) for i in range(1, n)]}")