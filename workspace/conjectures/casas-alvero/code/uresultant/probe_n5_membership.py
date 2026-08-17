"""Correct membership test: a_j^k in I_slice.  Validate on n=4 (ground truth:
quotient 0-dim length 16, so EVERY variable must have a power in I).  Then n=5.
"""
from sympy import symbols, Poly, expand, resultant, groebner, QQ, binomial
from sympy.polys.polytools import reduced

x = symbols("x")


def hasse(f, i):
    p = Poly(expand(f), x)
    c = {j: p.coeff_monomial(x ** j) for j in range(p.degree() + 1)}
    return sum(binomial(j, i) * cc * x ** (j - i)
               for j, cc in c.items() if j >= i)


def membership(n, kcaps=None):
    a = symbols(f"a_1:{n+1}")
    f = x ** n + sum(a[i] * x ** (n - 1 - i) for i in range(n))
    sl = list(a[1:])  # a2..an
    R = [expand(resultant(f, hasse(f, i), x).subs(a[0], 0))
         for i in range(1, n)]
    gb = groebner(R, *sl, order="grevlex")
    res = {}
    for vv in sl:
        ks = []
        for k in range(1, 25):
            # membership: reduced remainder is zero
            r, rem = reduced(Poly(vv ** k, *sl, domain=QQ), gb.polys, sl)
            if rem == 0:
                ks.append(k)
        res[vv] = ks
    return res


print("=== n=4 (must be 0-dim: each variable nilpotent) ===")
r4 = membership(4)
for vv, ks in r4.items():
    print(f"  {vv}: {vv}^k in I for k = {ks[:6]}... (count {len(ks)})")

print("=== n=5 ===")
r5 = membership(5)
for vv, ks in r5.items():
    print(f"  {vv}: {vv}^k in I for k = {ks[:8]}... (count {len(ks)})")
