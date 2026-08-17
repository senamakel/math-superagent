"""Probe 3b: length of R/I at the origin = u-resultant degree B, for n=4 slice a1=0.
Computed exactly as the number of standard monomials of a 0-dim ideal (monic
lex/grlex Groebner basis leading monomials). Cross-check B' = prod ord_0.
"""
import sympy as sp
from sympy import symbols, Poly, expand, groebner, resultant
from math import prod, floor

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

def ord_std(expr, vals):
    p = Poly(expr, *vals)
    return min(sum(m) for m,c in p.terms())

vals=[a2,a3,a4]
print("standard ord_0:", [ord_std(r,vals) for r in R], "prod:", prod(ord_std(r,vals) for r in R))
print("weighted ord_0: [12,8,4] prod: 384")

# length of R/I via standard monomials
gb = groebner(R, a2,a3,a4, order='lex')
lms = []
for g in gb.polys:
    lms.append(g.LM)
print("leading monomials:", lms)
# count monomials a2^i a3^j a4^k not divisible by any LM


def count_std(lms, maxdeg):
    # lms is list of monomials (a2^p a3^q a4^r)
    cnt=0
    std=[]
    de = [v for v in (a2,a3,a4)]
    for i in range(maxdeg):
        for j in range(maxdeg):
            for k in range(maxdeg):
                mon = a2**i*a3**j*a4**k
                if i+j+k > maxdeg: continue
                divby=False
                for lm in lms:
                    if _divides(lm, mon, de):
                        divby=True;break
                if not divby:
                    cnt+=1
    return cnt

def _divides(lm, mon, de):
    # lm divides mon ?
    plm = Poly(lm, *de)
    pmon = Poly(mon, *de)
    for v in de:
        e_lm = plm.degree(v)
        e_mon = pmon.degree(v)
        if e_lm>e_mon: return False
    return True

# bounded enumeration: length is finite; iterate up to some degree cap until stable
prev=None
for cap in range(0, 40):
    c = count_std(lms, cap)
    if prev is not None and c==prev:
        print("standard-monomial length (u-resultant degree B) stabilises at", c, "cap", cap)
        break
    prev=c
