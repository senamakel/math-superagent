import sympy as sp
from sympy import symbols, Poly, expand, groebner, resultant, factor, QQ
from math import prod
x = symbols("x")
a1,a2,a3,a4,u = symbols("a_1 a_2 a_3 a_4 u")

def hasse(f,i):
    p=Poly(sp.expand(f),x);c={j:p.coeff_monomial(x**j) for j in range(p.degree()+1)}
    return sum(sp.binomial(j,i)*cc*x**(j-i) for j,cc in c.items() if j>=i)

f=x**4+a1*x**3+a2*x**2+a3*x+a4
Rfull=[sp.expand(resultant(f,hasse(f,i),x)) for i in (1,2,3)]
R=[sp.expand(r.subs(a1,0)) for r in Rfull]
print("R (a1=0):",[factor(r) for r in R])

sl=[a2,a3,a4]; W=[2,3,4]
def wdeg(poly):
    P=Poly(poly,*sl)
    return min(sum(e*w for e,w in zip(m,W)) for m,c in P.terms())
ords=[wdeg(r) for r in R]
print("ords:",ords,"prod=",prod(ords),"norm/(w2w3w4):",prod(ords)//24)

gb=groebner(R, a2,a3,a4, order='grevlex')
LMs=list(set(tuple(g.as_poly(a2,a3,a4,domain=QQ).LM().as_expr().as_poly(a2,a3,a4).degree(v) for v in (a2,a3,a4)) for g in gb.polys))
print("reduced grevlex LMs:",sorted(LMs))

def is_std(ev):
    return not any(all(e<=f for e,f in zip(ev,lev)) for lev in LMs)
prev=None
for cap in [2,3,4,5,6,8,10]:
    cnt=0
    for e2 in range(cap):
        for e3 in range(cap):
            for e4 in range(cap):
                if is_std((e2,e3,e4)): cnt+=1
    print(f"cap={cap}: count={cnt}")
