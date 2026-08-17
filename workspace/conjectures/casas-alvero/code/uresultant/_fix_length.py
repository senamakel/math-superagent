import sympy as sp
from sympy import (symbols, Poly, expand, groebner, resultant, factor,
                   QQ, GF)
from math import prod
x = symbols("x")
a1,a2,a3,a4 = symbols("a_1 a_2 a_3 a_4")
u = symbols("u")
def hasse(f,i):
    p=Poly(sp.expand(f),x);c={j:p.coeff_monomial(x**j) for j in range(p.degree()+1)}
    return sum(sp.binomial(j,i)*cc*x**(j-i) for j,cc in c.items() if j>=i)
f=x**4+a1*x**3+a2*x**2+a3*x+a4
R=[sp.expand(resultant(f,hasse(f,i),x).subs(a1,0)) for i in (1,2,3)]
gb=groebner(R, a2,a3,a4, order='grevlex')
LMs=[]
for g in gb.polys:
    lm=g.as_poly(a2,a3,a4,domain=QQ).LM().as_expr()
    lp=sp.Poly(lm,a2,a3,a4,domain=QQ)
    LMs.append((lp.degree(a2),lp.degree(a3),lp.degree(a4)))
print("LM exponent vectors:",LMs)
def is_std(ev):
    return not any(all(e<=f for e,f in zip(ev,lev)) for lev in LMs)
std=[]
for e2 in range(10):
    for e3 in range(10):
        for e4 in range(2):
            if is_std((e2,e3,e4)): std.append((e2,e3,e4))
print("length =",len(std))
print("standard monomials:",sorted(std))

# mod p eliminant debug: lex GB mod p, print u-only
W=[2,3,4]
def wdeg(poly):
    P=Poly(poly,a2,a3,a4);return min(sum(e*w for e,w in zip(m,W)) for m,c in P.terms())
ords=[wdeg(r) for r in R]
print("ords:",ords,"prod:",prod(ords),"norm:",prod(ords)//24)

for p in (2,3,5,7,11,13,17):
    Rp=[Poly(r,a2,a3,a4,domain=GF(p)).as_expr() for r in R]
    gb2=groebner([*Rp,u-(a2+a3+a4)],a2,a3,a4,u,order='lex',domain=GF(p))
    uonly=None
    for g in gb2.polys:
        if set(v.name for v in g.free_symbols).issubset({'u'}):
            uonly=g.as_expr();break
    print(f"p={p}: uonly={factor(uonly) if uonly is not None else None}")
