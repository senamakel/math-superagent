"""Probe ONLY n=7 construction cost."""
import time
from sympy import symbols, Poly, expand, resultant, binomial

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


n = 7
t0 = time.time()
R = slice_resultants(n)
ops = [r.count_ops() for r in R]
print(f"n={n}: constructed {len(R)} resultants in {time.time()-t0:.1f}s; term-ops={ops}")
