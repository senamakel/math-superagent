"""Cost probe for the n=8 exact Samuel route (construction of the 7 Hasse
resultants R_i = Res_x(f, H_i f) on the traceless slice a_1=0).

Only measures the construction; does not compute weighted orders or run
Singular. If the construction closes in a wall budget, extend_n8_capture.py
can be run in the same session.

Usage: python _probe_n8_cost.py
"""
import time, sys
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
    out = []
    for i in range(1, n):
        t0 = time.time()
        r = expand(resultant(f, hasse(f, i), x).subs(a[0], 0))
        out.append(r)
        print(f"  i={i}: {time.time()-t0:.1f}s, ops={r.count_ops()}")
    return out


if __name__ == "__main__":
    n = 8
    wall0 = time.time()
    R = slice_resultants(n)
    print(f"total construction: {time.time()-wall0:.1f}s")
    print("term-ops:", [r.count_ops() for r in R])