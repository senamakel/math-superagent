"""ord_0(R_i) = n(n-i) for n=6, computed exactly via weighted substitution.
Also confirm the leading weighted coefficient is nonzero.
"""
import sympy as sp

def order_n(n):
    x, t = sp.symbols('x t')
    a = [sp.Symbol('a%d' % j) for j in range(n + 1)]
    coeffs = [sp.Integer(1)] + [sp.Integer(0)] + [a[j] for j in range(2, n + 1)]
    f = sum(coeffs[j] * x ** (n - j) for j in range(n + 1))
    res = {}
    for i in range(1, n):
        hi = sum(sp.binomial(n - j, i) * coeffs[j] * x ** (n - j - i)
                 for j in range(n + 1) if (n - j) >= i)
        R = sp.resultant(f, hi, x)
        Rt = sp.expand(R.subs({a[j]: a[j] * t ** j for j in range(2, n + 1)}))
        # lowest term
        P = sp.Poly(Rt, t)
        e0, c0 = P.terms()[0]
        res[i] = (e0[0], sp.simplify(c0) != 0)
    return res

res = order_n(6)
target = {i: 6 * (6 - i) for i in range(1, 6)}
ok = all(res[i][0] == target[i] and res[i][1] for i in target)
print("n=6 ord_0(R_i):", {i: res[i][0] for i in res})
print("target:", target)
print("leading coeff nonzero:", {i: res[i][1] for i in res})
print("ALL OK" if ok else "FAIL")
