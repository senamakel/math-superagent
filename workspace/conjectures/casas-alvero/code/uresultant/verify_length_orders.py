"""Verify length formula |QQ[a_2..a_n]/I| = n^{n-2} = prod_i ord_0(R_i)/n!, n=3,4,5.
Cheaper: use singular vdim on the quotient, plus weighted-order products.
"""
import sympy as sp
from math import factorial

def built(n):
    x = sp.symbols('x')
    a = [sp.Symbol('a%d' % j) for j in range(n + 1)]
    coeffs = [sp.Integer(1)] + [sp.Integer(0)] + [a[j] for j in range(2, n + 1)]
    f = sum(coeffs[j] * x ** (n - j) for j in range(n + 1))
    R = []
    for i in range(1, n):
        hi = sum(sp.binomial(n - j, i) * coeffs[j] * x ** (n - j - i)
                 for j in range(n + 1) if (n - j) >= i)
        R.append(sp.resultant(f, hi, x))
    return a, R

def order_in_t(poly, t, a):
    Rt = sp.expand(poly.subs({a[j]: a[j] * t ** j for j in range(2, len(a))}))
    return sp.Poly(Rt, t).terms()[0][0][0]

for n in [3, 4, 5]:
    a, R = built(n)
    t = sp.symbols('t')
    wo = [order_in_t(r, t, a) for r in R]
    pred = 1
    for o in wo: pred *= o
    pred //= factorial(n)
    print(f"n={n}: weighted orders={wo}  prod/n! = {pred}  n^(n-2)={n**(n-2)}")
