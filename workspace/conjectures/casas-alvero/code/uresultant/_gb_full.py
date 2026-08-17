import sympy as sp
from sympy import symbols, Poly, expand, groebner, resultant, factor, QQ, GF
from sympy.polys.rings import ring
x = symbols("x")
a1,a2,a3,a4 = symbols("a_1 a_2 a_3 a_4")
u = symbols("u")
def hasse(f,i):
    p=Poly(sp.expand(f),x);c={j:p.coeff_monomial(x**j) for j in range(p.degree()+1)}
    return sum(sp.binomial(j,i)*cc*x**(j-i) for j,cc in c.items() if j>=i)
f=x**4+a1*x**3+a2*x**2+a3*x+a4
R=[sp.expand(resultant(f,hasse(f,i),x).subs(a1,0)) for i in (1,2,3)]
print("R:",[factor(r) for r in R])
gb=groebner(R, a2,a3,a4, order='grevlex')
print("GB size:",len(gb.polys))
for g in gb.polys:
    print("   ",g.as_expr())
