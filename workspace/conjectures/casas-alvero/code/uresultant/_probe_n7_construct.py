"""Probe the cost of constructing n=7 (and n=8) Hasse resultants on the
traceless slice (a1=0). Measures only sympy construction, before Singular.
"""
import time
from sympy import symbols, Poly, expand, resultant, binomial, sstr

x = symbols("x")


def hasse(f, i):
    p = Poly(expand(f), x)
    c = {j: p.coeff_monomial(x ** j) for j in range(p.degree() + 1)}
    return sum(binomial(j, i) * cc * x ** (j - i)
               for j, cc in c.items() if j >= i)


def slice_resultants(n):
    a = symbols(f"a_1:{n+1}")
    f = x ** n + sum(a[i] * x ** (n - 1 - i) for i in range(n))
    return [expand(resultant(f, hasse(f, i), x).subs(a[0], 0)) for i in range(1, n)]


for n in (7, 8):
    t0 = time.time()
    try:
        R = slice_resultants(n)
        ops = [r.count_ops() for r in R]
        print(f"n={n}: constructed {len(R)} resultants in {time.time()-t0:.1f}s; "
              f"term-ops={ops}")
    except Exception as e:
        print(f"n={n}: CONSTRUCTION raised {type(e).__name__}: {e} in {time.time()-t0:.1f}s")
        break
