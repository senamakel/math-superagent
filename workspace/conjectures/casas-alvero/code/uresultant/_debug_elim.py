"""Debug: why did u-resultant elimination return no univariate poly in u?"""
import sympy as sp
from sympy import symbols, Poly, expand, groebner, resultant, factor
from sympy import QQ

a1,a2,a3,a4,u = symbols('a_1 a_2 a_3 a_4 u')

def hasse(f, x, i):
    p = Poly(sp.expand(f), x)
    coeffs = {j: p.coeff_monomial(x**j) for j in range(p.degree()+1)}
    return sum(sp.binomial(j,i)*c*x**(j-i) for j,c in coeffs.items() if j>=i)

x = symbols('x')
f = x**4 + a1*x**3 + a2*x**2 + a3*x + a4
R=[resultant(f, hasse(f,x,i), x) for i in range(1,4)]
R=[sp.expand(r.subs(a1,0)) for r in R]
print("R in slice:")
for r in R: print("  ", factor(r))
sys_ = R + [u - (a2+a3+a4)]
gb = groebner(sys_, u, a2,a3,a4, order='lex')
print("lex groebner size:", len(gb.polys), "over", gb.domain)
for g in gb.polys:
    fs = g.free_symbols
    print("  poly in", sorted(v.name for v in fs), ":", factor(g))
