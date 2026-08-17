"""Does the n=5 traceless-slice ideal I=(R_1..R_4) have Q[a2..a5]/I 0-dim?

Membership a_j^k in I tested by exact reduction against the grevlex GB.
If every variable has a power in I, quotient is 0-dim; if some (a3) has
none, the traceless slice is NOT 0-dimensional -- a striking degeneracy
that would conflict with CA_5 being settled, so we also hunt elsewhere.
"""
from sympy import symbols, Poly, expand, resultant, groebner, QQ, binomial

x = symbols("x")
a1, a2, a3, a4, a5 = symbols("a_1 a_2 a_3 a_4 a_5")
a = [a1, a2, a3, a4, a5]


def hasse(f, i):
    p = Poly(expand(f), x)
    c = {j: p.coeff_monomial(x ** j) for j in range(p.degree() + 1)}
    return sum(binomial(j, i) * cc * x ** (j - i)
               for j, cc in c.items() if j >= i)


n = 5
f = x ** n + sum(a[i] * x ** (n - 1 - i) for i in range(n))
sl = [a2, a3, a4, a5]
R = [expand(resultant(f, hasse(f, i), x).subs(a1, 0)) for i in (1, 2, 3, 4)]
gb = groebner(R, *sl, order="grevlex")
print(f"GB size: {len(gb.polys)}")

# Reduction-based membership: a_j^k in I iff reduce(poly)==0
def inI(expr):
    p = Poly(expand(expr), *sl, domain=QQ)
    # reduce by the grevlex basis via sympy's poly reduction
    r = p.rem(gb.polys)  # multivariate rem: remainder in the ideal iff 0
    return r == 0

for vv, name in [(a2, "a2"), (a3, "a3"), (a4, "a4"), (a5, "a5")]:
    ks = [k for k in range(1, 30) if inI(vv ** k)]
    print(f"{name}: {name}^k in I for k = {ks}")
