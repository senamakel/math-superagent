import time, sys
import sympy as sp
from sympy import symbols, Poly, expand, groebner, resultant, factor, QQ
from math import prod
x = symbols("x")
a1,a2,a3,a4 = symbols("a_1 a_2 a_3 a_4")
u = symbols("u")

def hasse(f,i):
    p=Poly(sp.expand(f),x);c={j:p.coeff_monomial(x**j) for j in range(p.degree()+1)}
    return sum(sp.binomial(j,i)*cc*x**(j-i) for j,cc in c.items() if j>=i)

f=x**4+a1*x**3+a2*x**2+a3*x+a4
t0=time.time()
R=[sp.expand(resultant(f,hasse(f,i),x)) for i in (1,2,3)]
print("construct resultants:", round(time.time()-t0,1),"s")

sl=[a1,a2,a3,a4]; W=[1,2,3,4]
def wdeg(poly):
    P=Poly(poly,*sl)
    return min(sum(e*w for e,w in zip(m,W)) for m,c in P.terms())
t0=time.time()
ords=[wdeg(r) for r in R]
print("weighted orders full:",ords,"prod=",prod(ords),"norm/(w1w2w3w4)=",prod(ords)//24)
print("wdeg time:",round(time.time()-t0,1),"s")

t0=time.time()
gb=groebner(R, a1,a2,a3,a4, order='grevlex')
print("grevlex GB size:",len(gb.polys),"time:",round(time.time()-t0,1),"s")
LMs=[]
for g in gb.polys:
    P=g.as_poly(a1,a2,a3,a4,domain=QQ)
    LMs.append([P.degree(v) for v in (a1,a2,a3,a4)])
print("LMs:",LMs)

def is_std(ev):
    return not any(all(e<=f for e,f in zip(ev,lev)) for lev in LMs)
length=0;cap=1
while True:
    cnt=0
    for e1 in range(cap):
        for e2 in range(cap):
            for e3 in range(cap):
                for e4 in range(cap):
                    if is_std((e1,e2,e3,e4)): cnt+=1
    if cnt==length: break
    length=cnt;cap+=1
print("length QQ[a1..a4]/I =",length,"(cap",cap,")")
