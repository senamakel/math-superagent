"""Probe 2: u-resultant at n=4 in the centroid-fixed slice a_1=0.

System: after setting a_1=0, I = (R_1,R_2,R_3) in QQ[a_2,a_3,a_4], ht 3,
V(I) = {0}.  Generic linear form u = c_2 a_2 + c_3 a_3 + c_4 a_4.
Eliminant Res_u = elimination of a_2,a_3,a_4 from (R_1,R_2,R_3, u - L).
Compare its degree B with B' = prod ord_0(R_i) in the slice,
weights w(a_j)=j.
"""
import sympy as sp
from sympy import symbols, Poly, resultant, expand, groebner
from math import prod

def hasse(f, x, i):
    p = Poly(sp.expand(f), x)
    coeffs = {j: p.coeff_monomial(x**j) for j in range(p.degree()+1)}
    return sum(sp.binomial(j, i)*c*x**(j-i) for j, c in coeffs.items() if j >= i)

def rigi(n, a):
    x = symbols('x')
    f = x**n + sum(a[i]*x**(n-1-i) for i in range(n))
    return [resultant(f, hasse(f, x, i), x) for i in range(1, n)]

a1,a2,a3,a4 = symbols('a_1 a_2 a_3 a_4')
Rs = rigi(4, [a1,a2,a3,a4])
# slice a_1=0
R = [sp.expand(r.subs(a1,0)) for r in Rs]

# ord_0 in slice, weights w(a_j)=j
def ord_slice(expr, vals, weights):
    p = Poly(expr, *vals)
    best = None
    for monom, coeff in p.terms():
        w = sum(e*wt for e, wt in zip(monom, weights))
        best = w if best is None else min(best, w)
    return best

vals = [a2,a3,a4]; weights=[2,3,4]
ords = [ord_slice(r, vals, weights) for r in R]
print("ord_0 in slice (a2,a3,a4):", ords)
print("B' = prod ord_0 =", prod(ords))

# u-resultant for a generic linear form: eliminate a2,a3,a4
u, c2,c3,c4 = symbols('u c2 c3 c4')
L = c2*a2 + c3*a3 + c4*a4
sys_ = R + [u - L]
syms = [a2,a3,a4,u,c2,c3,c4]
print("eliminating over QQ[a2,a3,a4,u,c2,c3,c4] ...")
gb = groebner(sys_, *syms, order='lex')
# find polynomial involving only u,c2,c3,c4
ures = None
for g in gb.polys:
    gens_set = set(g.gens)
    # g.gens is the whole symbol list; find vars present
    if all(v.name in ('u','c2','c3','c4') for v in g.gens if v != g:
        pass
print("done, #poly in basis:", len(gb.polys))
