import sympy as sp
from sympy import symbols, Poly, expand, groebner, resultant, factor, QQ
x = symbols("x")
a1,a2,a3,a4,u = symbols("a_1 a_2 a_3 a_4 u")

def hasse(f,i):
    p=Poly(sp.expand(f),x);c={j:p.coeff_monomial(x**j) for j in range(p.degree()+1)}
    return sum(sp.binomial(j,i)*cc*x**(j-i) for j,cc in c.items() if j>=i)

f=x**4+a1*x**3+a2*x**2+a3*x+a4
R=[sp.expand(resultant(f,hasse(f,i),x)) for i in (1,2,3)]

from math import prod
sl=[a1,a2,a3,a4]; W=[1,2,3,4]
def wdeg(poly):
    P=Poly(poly,*sl)
    return min(sum(e*w for e,w in zip(m,W)) for m,c in P.terms())
ords=[wdeg(r) for r in R]
print("weighted orders (full scheme):",ords,"prod=",prod(ords),
      "norm /(w1w2w3w4):",prod(ords)//prod(W))

for name,L in [("u=a1+a2+a3+a4",a1+a2+a3+a4),("u=a1+2a2+3a3+4a4",a1+2*a2+3*a3+4*a4),
               ("u=2a1+3a2+5a3+7a4",2*a1+3*a2+5*a3+7*a4)]:
    sys_=R+[u-L]
    gb=groebner(sys_, a1,a2,a3,a4,u, order='lex')
    uonly=None
    for g in gb.polys:
        if set(v.name for v in g.free_symbols).issubset({'u'}):
            uonly=g.as_expr();break
    d= uonly.as_poly(u).degree() if uonly is not None else None
    print(f"{name}: u-only={factor(uonly) if uonly is not None else None}  deg={d}")
