import sympy as sp
from sympy import symbols, Poly, expand, groebner, resultant, factor, QQ
x = symbols("x")
a1,a2,a3,a4,u = symbols("a_1 a_2 a_3 a_4 u")

def hasse(f,i):
    p=Poly(sp.expand(f),x);c={j:p.coeff_monomial(x**j) for j in range(p.degree()+1)}
    return sum(sp.binomial(j,i)*cc*x**(j-i) for j,cc in c.items() if j>=i)

f=x**4+a1*x**3+a2*x**2+a3*x+a4
R=[sp.expand(resultant(f,hasse(f,i),x).subs(a1,0)) for i in (1,2,3)]
print("R:",[factor(r) for r in R])

# full lex GB with u=a2+a3+a4 in order (a2,a3,a4,u)
sys_=R+[u-(a2+a3+a4)]
gb=groebner(sys_, a2,a3,a4,u, order='lex')
print("lex GB size:",len(gb.polys))
for g in gb.polys:
    print("  ", g.as_expr(), "| freesyms:", set(v.name for v in g.free_symbols))
