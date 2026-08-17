"""Probe 4b: exact length of R/I (u-resultant degree B) at n=4 slice a1=0,
via standard-monomial count and via direct elimination (the u-resultant).
B' = prod(weighted orders) and prod(standard orders) computed for comparison.
"""
import sympy as sp
from sympy import symbols, Poly, expand, groebner, resultant, factor
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
print("weighted orders:", [wdeg(r) for r in R], "B'_w=prod:", prod(wdeg(r) for r in R))
def sdeg(poly):
    P = Poly(poly, *sl)
    return min(sum(m) for m,c in P.terms())
print("standard orders:", [sdeg(r) for r in R], "B'_s=prod:", prod(sdeg(r) for r in R))

# standard monomial count (length of R/I over QQ): only need a2,a3 exponents
# since a4's LM is a4 (so a4^0 only). Count (p,q) standard.
LMs=[(4,0),(3,2),(1,4),(0,6)]  # a4 contributes factor of 1 (a4^0)
prev=None; B_len=None
for cap in range(0,60):
    cnt=0
    for p in range(cap):
        for q in range(cap):
            if any(p>=a and q>=b for (a,b) in LMs):
                continue
            cnt+=1
    if prev is not None and cnt==prev:
        B_len=cnt; print("length B (standard monomials, a2,a3) =", cnt); break
    prev=cnt

# u-resultant: eliminate a2,a3,a4 with u = a2+a3+a4, factor over QQ
u = symbols('u')
sys_ = R + [u - (a2+a3+a4)]
print("computing u-resultant by lex elimination ...")
gb2 = groebner(sys_, u, a2, a3, a4, order='lex')
ures=None
for g in gb2.polys:
    if set(v.name for v in g.free_symbols) <= {'u'}:
        print("  u-only poly found:", factor(g))
        ures=g
print("u-resultant factor:", factor(ures) if ures is not None else "NONE")
