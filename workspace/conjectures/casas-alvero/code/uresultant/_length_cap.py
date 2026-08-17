import time, sys
import sympy as sp
from sympy import symbols, Poly, expand, groebner, resultant, factor, QQ
from math import prod
x = symbols("x")
a1,a2,a3,a4 = symbols("a_1 a_2 a_3 a_4")

def hasse(f,i):
    p=Poly(sp.expand(f),x);c={j:p.coeff_monomial(x**j) for j in range(p.degree()+1)}
    return sum(sp.binomial(j,i)*cc*x**(j-i) for j,cc in c.items() if j>=i)

f=x**4+a1*x**3+a2*x**2+a3*x+a4
R=[sp.expand(resultant(f,hasse(f,i),x)) for i in (1,2,3)]

sl=[a1,a2,a3,a4]; W=[1,2,3,4]
gb=groebner(R, a1,a2,a3,a4, order='grevlex')
LMs=[]
for g in gb.polys:
    P=g.as_poly(a1,a2,a3,a4,domain=QQ)
    LMs.append([P.degree(v) for v in (a1,a2,a3,a4)])
# dedupe
LMs=list(set(tuple(l) for l in LMs))
print("num distinct LMs:",len(LMs))
for l in sorted(LMs): print("  ",l)

def is_std(ev):
    return not any(all(e<=f for e,f in zip(ev,lev)) for lev in LMs)

prev=None
for cap in [2,3,4,5,6,8,10,14,18]:
    cnt=0
    for e1 in range(cap):
        for e2 in range(cap):
            for e3 in range(cap):
                for e4 in range(cap):
                    if is_std((e1,e2,e3,e4)): cnt+=1
    print(f"cap={cap}: count={cnt}")
    prev=cnt
