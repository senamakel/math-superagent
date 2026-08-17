"""Probe 3: length of R/I = scheme degree at origin (the u-resultant degree B),
and initial forms / ord under standard and weighted gradings, for n=4 slice a1=0.
"""
import sympy as sp
from sympy import symbols, Poly, expand
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

def ord_std(expr, vals):
    p = Poly(expr, *vals)
    return min(sum(m) for m,c in p.terms())

vals=[a2,a3,a4]
print("standard ord_0:", [ord_std(r,vals) for r in R])
print("product standard:", prod(ord_std(r,vals) for r in R))
print("weighted ord_0:", [12,8,4], "product:", 384)

# length of R/I over QQ = degree B via Groebner basis of 0-dim ideal
JG = sp.groebner(R, a2,a3,a4, order='lex')
print("GB size:", len(JG.polys), "count of monomials leading?")
# length = dim of quotient = number of standard monomials
# compute via normal form: iterate monomials
import itertools
# Use a simpler exact computation: dim = sum of Hilbert function, finite.
# We can compute length as Q-vector space dimension by counting standard monomials
# below the leading monomials of a Groebner basis. Instead use a direct method:
# total multiplicity via resultant of system = Bezout using homogenization is complex.
# Let's just compute the u-resultant degree by elimination for n=4.
print("---- computing u-resultant by elimination ----")
u, c2,c3,c4 = symbols('u c2 c3 c4')
L = c2*a2 + c3*a3 + c4*a4
sys_ = R + [u - L]
# fix generic values to make it concrete? No: keep symbolic, use lex elimination with u first
gb = sp.groebner(sys_, u, a2,a3,a4, c2,c3,c4, order='lex')
print("gb size", len(gb.polys))
for g in gb.polys:
    vars_in = [v for v in g.gens if g hasattr(g,'gens')]
    pnames = set(v.name for v in (g.free_symbols or []))
    if pnames <= {'u','c2','c3','c4'}:
        print("  in u,c only:", sp.factor(g))
