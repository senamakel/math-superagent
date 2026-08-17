"""u-resultant for n=4 slice a1=0, u = a2+a3+a4, elimination ideal in u
(lex with u LAST so the eliminated vars a2,a3,a4 are ordered first)."""
import sympy as sp
from sympy import symbols, Poly, expand, groebner, resultant, factor
a1,a2,a3,a4,u = symbols('a_1 a_2 a_3 a_4 u')
x = symbols('x')
def hasse(f,x,i):
    p=Poly(sp.expand(f),x);c={j:p.coeff_monomial(x**j) for j in range(p.degree()+1)}
    return sum(sp.binomial(j,i)*cc*x**(j-i) for j,cc in c.items() if j>=i)
f = x**4 + a1*x**3+a2*x**2+a3*x+a4
R=[sp.expand(resultant(f,hasse(f,x,i),x).subs(a1,0)) for i in (1,2,3)]
print("R_i (a1=0):",[factor(r) for r in R])
sys_ = R + [u - (a2+a3+a4)]
# elim to u: order a2,a3,a4 first (biggest), u last
gb = groebner(sys_, a2,a3,a4,u, order='lex')
print("lex order (a2,a3,a4,u); elements:")
for g in gb.polys:
    print("   ", sorted(v.name for v in g.free_symbols), ":", factor(g))
