"""Recheck: length of R/I at n=4 slice a1=0 vs u-resultant degree.
Print u-resultant with correct elimination and count its degree; also recompute
length independently via a different method (LinearAlgebra rank / monomial basis).
"""
import sympy as sp
from sympy import symbols, Poly, expand, groebner, resultant, factor, degree
a1,a2,a3,a4,u = symbols('a_1 a_2 a_3 a_4 u')
x = symbols('x')
def hasse(f,x,i):
    p=Poly(sp.expand(f),x);c={j:p.coeff_monomial(x**j) for j in range(p.degree()+1)}
    return sum(sp.binomial(j,i)*cc*x**(j-i) for j,cc in c.items() if j>=i)
f=x**4+a1*x**3+a2*x**2+a3*x+a4
R=[sp.expand(resultant(f,hasse(f,x,i),x).subs(a1,0)) for i in (1,2,3)]

for name,L in [("u=a2+a3+a4",a2+a3+a4),("u=2a2+3a3+5a4",2*a2+3*a3+5*a4)]:
    sys_=R+[u-L]
    gb=groebner(sys_, a2,a3,a4,u, order='lex')
    uonly=None
    for g in gb.polys:
        if set(v.name for v in g.free_symbols)<={'u'}:
            uonly=g.as_expr()
    print(f"--- {name} ---")
    print("  u-only:", factor(uonly) if uonly is not None else None)
    if uonly is not None:
        print("  degree in u:", degree(uonly, u))
