"""Probe: ord_0(R_i) under weighted order w(a_j)=j, and eliminant feasibility at n=4."""
import sympy as sp
from sympy import symbols, Poly, resultant, expand

def hasse(f, x, i):
    p = Poly(sp.expand(f), x)
    coeffs = {j: p.coeff_monomial(x**j) for j in range(p.degree()+1)}
    return sum(sp.binomial(j, i) * c * x**(j-i) for j, c in coeffs.items() if j >= i)

def rigi(n, a):
    x = symbols('x')
    f = x**n + sum(a[i]*x**(n-1-i) for i in range(n))
    Rs = []
    for i in range(1, n):
        Rs.append(resultant(f, hasse(f, x, i), x))
    return f, Rs

def ord_weighted(expr, a, weights):
    p = Poly(expand(expr), *a)
    best = None
    for monom, coeff in p.terms():
        w = 0
        for ai, aj in zip(monom, a):
            pass
        w = sum(exp * wt for exp, wt in zip(monom, weights))
        if best is None or w < best:
            best = w
    return best

aa = symbols('a_1 a_2 a_3 a_4')
f, Rs = rigi(4, aa)
weights = [1, 2, 3, 4]
for i, R in enumerate(Rs, 1):
    print(f"R_{i}: total_deg={Poly(R,*aa).total_degree()}  ord_0={ord_weighted(R, aa, weights)}")

# product of orders
from math import prod
ords = [ord_weighted(R, aa, weights) for R in Rs]
print("B = prod ord_0 =", prod(ords), ords)
