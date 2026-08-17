"""Reconcile length of R/I (n=4 slice a1=0) with u-resultant degree."""
import sympy as sp
from sympy import symbols, Poly, expand, groebner, resultant, factor, degree, QQ
from sympy.polys.polytools import groebner as gb_fn
a1,a2,a3,a4,u = symbols('a_1 a_2 a_3 a_4 u')
x = symbols('x')
def hasse(f,x,i):
    p=Poly(sp.expand(f),x);c={j:p.coeff_monomial(x**j) for j in range(p.degree()+1)}
    return sum(sp.binomial(j,i)*cc*x**(j-i) for j,cc in c.items() if j>=i)
f=x**4+a1*x**3+a2*x**2+a3*x+a4
R=[sp.expand(resultant(f,hasse(f,x,i),x).subs(a1,0)) for i in (1,2,3)]

# length via standard monomials, reading lead terms from reduced GB over QQ
gb = gb_fn(R, a2,a3,a4, order='grevlex', domain=QQ)
print("grevlex GB size:", len(gb.polys))
# get leading monomials
def lm_exp(poly, sl):
    P = poly.as_poly(*sl, domain=QQ) if isinstance(poly, sp.Poly) else Poly(poly,*sl,domain=QQ)
    return P.LM()
LMs = [lm_exp(g, [a2,a3,a4]) for g in gb.polys]
print("lead terms:", LMs)
lve=[]
for lm in LMs:
    # lm is a Monomial; convert via as_expr
    ex = lm.as_expr()
    P = sp.Poly(ex, a2,a3,a4, domain=QQ)
    lve.append([P.degree(a2),P.degree(a3),P.degree(a4)])
print("LM exponent vectors:", lve)
# count standard monomials
def is_std(ev):
    return not any(all(e<=f for e,f in zip(lev,ev)) for lev in lve)
prev=None
for cap in range(1,80):
    cnt=0
    for i2 in range(cap):
        for i3 in range(cap):
            for i4 in range(cap):
                if is_std((i2,i3,i4)): cnt+=1
    if prev==cnt:
        print("length =", cnt, "at cap", cap); break
    prev=cnt

# eliminant degree via sympy eliminate
E = sp.eliminate(R+[u-(a2+a3+a4)], [a2,a3,a4])
print("eliminate result:", E)
if E:
    for poly in E:
        pu = sp.Poly(poly, u)
        print("   eliminant in u:", factor(pu.as_expr()), "| deg_u=", pu.degree())
