"""Rigorous n=4 vertical check: length B = u-resultant degree, cross-verified
by two independent linear forms, against B' = prod ord_0(R_i).
Also verify quasihomogeneity of R_i and CA via the oracle, and the
char-p break (Res_u mod p not a pure power).
"""
import sympy as sp
from sympy import symbols, Poly, expand, groebner, resultant, factor, factorint, GF, QQ
from math import prod
from lib.casas_alvero import is_ca, is_ca_hasse, is_pure_power, charp_witness

x = symbols('x')

def hasse(f,x,i):
    p=Poly(sp.expand(f),x);c={j:p.coeff_monomial(x**j) for j in range(p.degree()+1)}
    return sum(sp.binomial(j,i)*cc*x**(j-i) for j,cc in c.items() if j>=i)

def rigi(n, a):
    f = x**n + sum(a[i]*x**(n-1-i) for i in range(len(a)))
    return [resultant(f, hasse(f,x,i), x) for i in range(1,n)]

n=4
a1,a2,a3,a4 = symbols('a_1 a_2 a_3 a_4')
R=[sp.expand(r.subs(a1,0)) for r in rigi(n,[a1,a2,a3,a4])]
print("R_i (a1=0):",[factor(r) for r in R])

# quasihomogeneity check: weights w(a_j)=j
sl=[a2,a3,a4]; W=[2,3,4]
for i,r in enumerate(R,1):
    P=Poly(r,*sl)
    dg=set(sum((e*w) for e,w in zip(m,W)) for m,c in P.terms())
    print(f"R_{i}: weighted degrees present = {dg}  (quasihomogeneous iff size 1)")

# u-resultant with two generic linear forms
def uresultant(R, form):
    u=form
    gb=groebner(R+[variables[-1] if False else u - form], a2,a3,a4, order='lex')
    for g in gb.polys:
        if set(v.name for v in g.free_symbols)<={'u'}:
            return sp.factor(g)
    return None

u=sp.symbols('u')
for name,L in [("u=a2+a3+a4", a2+a3+a4), ("u=a2-a3+2a4", a2-a3+2*a4)]:
    gb=groebner(R+[u-L], u,a2,a3,a4, order='lex')
    resid=None
    for g in gb.polys:
        if set(v.name for v in g.free_symbols)<={'u'}:
            resid=g;break
    print(f"u-resultant for {name}: {factor(resid)}")

# B' = prod ord_0 weighted
def wdeg(poly):
    P=Poly(poly,*sl);return min(sum(e*w for e,w in zip(m,W)) for m,c in P.terms())
ords=[wdeg(r) for r in R]
print("weighted orders:",ords,"B'_w=prod:",prod(ords),"normalised (/(w1 w2 w3)):",prod(ords)//prod(W))

# oracle: (x-1)^4 is CA pure power; char-p witness
print("oracle (x-1)^4: is_ca=",is_ca((x-1)**4,0)," pure=",is_pure_power((x-1)**4,0))
for p in (2,3,5,7):
    fw=charp_witness(p)
    print(f"charp witness p={p}: is_ca={is_ca(fw,p)} pure={is_pure_power(fw,p)}")
