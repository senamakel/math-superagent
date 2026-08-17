import sympy as sp
from sympy import symbols, Poly, expand, groebner, resultant, factor, QQ, GF
x = symbols("x")
a1,a2,a3,a4 = symbols("a_1 a_2 a_3 a_4")
u = symbols("u")
def hasse(f,i):
    p=Poly(sp.expand(f),x);c={j:p.coeff_monomial(x**j) for j in range(p.degree()+1)}
    return sum(sp.binomial(j,i)*cc*x**(j-i) for j,cc in c.items() if j>=i)
f=x**4+a1*x**3+a2*x**2+a3*x+a4
R=[sp.expand(resultant(f,hasse(f,i),x).subs(a1,0)) for i in (1,2,3)]

for p in (2,3,5,7):
    Rp=[Poly(r,a2,a3,a4,domain=GF(p)).as_expr() for r in R]
    print(f"=== p={p} ===")
    print("  Rp:",[factor(r) for r in Rp])
    gb2=groebner([*Rp,u-(a2+a3+a4)],a2,a3,a4,u,order='lex',domain=GF(p))
    print("  lex GB size:",len(gb2.polys))
    for g in gb2.polys:
        fs=set(v.name for v in g.free_symbols)
        print(f"    frees={fs}: {g.as_expr()}")
    # alternatice: eliminate via Groebner of ideal in a-vars then check common zeros
