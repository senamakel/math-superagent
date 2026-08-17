"""Probe 4: exact length of R/I (u-resultant degree B) at n=4 slice a1=0,
computed three independent ways:
  (a) standard-monomial count of the 0-dim lex Groebner ideal,
  (b) weighted-multiplicity formula  prod(weighted orders)/prod(weights),
  (c) the actual u-resultant (elimination of a2,a3,a4 for u=a2+a3+a4), factored.
Also compute B' = prod weighted orders and the standard product.
"""
import sympy as sp
from sympy import symbols, Poly, expand, groebner, resultant, factor, factor_list
from math import prod

def hasse(f, x, i):
    p = Poly(sp.expand(f), x)
    coeffs = {j: p.coeff_monomial(x**j) for j in range(p.degree()+1)}
    return sum(sp.binomial(j,i)*c*x**(j-i) for j,c in coeffs.items() if j>=i)

def rigi(n, a):
    x = symbols('x')
    f = x**n + sum(a[i]*x**(n-1-i) for i in range(n))
    return [resultant(f, hasse(f,x,i), x) for i in range(1,n)]

a1,a2,a3,a4 = symbols('a_1 a_2 a_3 a_4')
Rs = rigi(4,[a1,a2,a3,a4])
R = [sp.expand(r.subs(a1,0)) for r in Rs]
sl = [a2,a3,a4]; W=[2,3,4]

def wdeg(poly):
    P = Poly(poly, *sl)
    return min(sum(e*w for e,w in zip(m,W)) for m,c in P.terms())

ords_w = [wdeg(r) for r in R]
print("weighted orders:", ords_w, "B'=prod:", prod(ords_w))
print("prod weights:", prod(W), "  B'(normalised)=prod_ord/prod_w =",
      prod(ords_w)//prod(W))

def sdeg(poly):
    P = Poly(poly, *sl)
    return min(sum(m) for m,c in P.terms())
print("standard orders:", [sdeg(r) for r in R], "prod:", prod(sdeg(r) for r in R))

# (a) standard monomial count
gb = groebner(R, a2,a3,a4, order='lex')
lms = [g.LM() for g in gb.polys]
print("lex leading monomials:", [str(lm) for lm in lms])
def divides(lm, mon):
    for v,(el,em) in zip(sl, zip(Poly(lm,*sl).monoms()[0] if False else [],[])):
        pass
# express each lm as exponent vector
def expvec(poly):
    P = Poly(poly,*sl)
    return P.monoms()[0]
lve = [expvec(lm) for lm in lms]
print("LM exponent vectors:", lve)
def divides_lm(ev, emv):
    return all(e<=f for e,f in zip(ev,emv))
prev=None
for cap in range(0,30):
    cnt=0
    for i in range(cap):
        for j in range(cap):
            for k in range(cap):
                emv=(i,j,k)
                if any(divides_lm(ev,emv) for ev in lve):
                    continue
                cnt+=1
    if prev is not None and cnt==prev:
        print("length B (standard monomials) =", cnt); break
    prev=cnt

# (c) u-resultant: eliminate a2,a3,a4 with u=a2+a3+a4
u = symbols('u')
sys_ = R + [u - (a2+a3+a4)]
print("computing u-resultant by elimination (lex)...")
gb2 = groebner(sys_, u, a2, a3, a4, order='lex')
ures=None
for g in gb2.polys:
    if set(v.name for v in g.free_symbols) <= {'u'}:
        ures=g
print("u-resultant:", factor(ures))
