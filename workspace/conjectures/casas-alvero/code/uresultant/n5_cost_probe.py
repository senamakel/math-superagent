"""Measure the n=5 feasibility of the u-resultant route: construction of
R_i (Hasse resultants) and a timed lex/grevlex GB, to state the projected
cost honestly (directive: validate at n=4, state projected n=5 cost, stop).
"""
import time, sys
import sympy as sp
from sympy import symbols, Poly, expand, resultant, groebner, QQ, GF

x = symbols("x")
def hasse(f, i):
    p = Poly(sp.expand(f), x)
    c = {j: p.coeff_monomial(x ** j) for j in range(p.degree() + 1)}
    return sum(sp.binomial(j, i) * cc * x ** (j - i)
               for j, cc in c.items() if j >= i)

n = 5
a = symbols("a_1:%d" % (n + 1))
f = x ** n + sum(a[i] * x ** (n - 1 - i) for i in range(n))
t0 = time.time()
R = [sp.expand(resultant(f, hasse(f, i), x).subs(a[0], 0)) for i in (1, 2, 3, 4)]
t_construct = time.time() - t0
print(f"n=5 R_i (a1=0) construction: {t_construct:.1f}s")
for i, r in enumerate(R, 1):
    print(f"  R_{i}: {r.count_ops()} ops")

sl = list(a[1:])
t0 = time.time()
try:
    gb = groebner(R, *sl, order="grevlex")
    nGB = len(gb.polys)
    t_grevlex = time.time() - t0
    print(f"n=5 a1=0 grevlex GB: {nGB} polys in {t_grevlex:.1f}s")
except Exception as e:
    print(f"n=5 grevlex GB failed: {e}")

# eliminant (lex) with a cap
u = symbols("u")
L = sum(sl)
t0 = time.time()
try:
    gb2 = groebner([*R, u - L], *sl, u, order="lex")
    uonly = next((g.as_expr() for g in gb2.polys
                  if set(v.name for v in g.free_symbols).issubset({"u"})), None)
    t_lex = time.time() - t0
    d = uonly.as_poly(u).degree() if uonly is not None else None
    print(f"n=5 lex eliminant: {t_lex:.1f}s, u-only degree={d}")
except Exception as e:
    print(f"n=5 lex eliminant failed: {e}")
