"""Verify R_i = Res_x(f, H_i f) is EXACTLY weighted-homogeneous of weight n(n-i).

This is the cleanest rigorous route (classical resultant weighted-homogeneity,
de Frutos Mar'in 2013 x1.3.1): if every monomial term of R_i has weighted
degree n(n-i) under w(a_j)=j, and R_i != 0, then ord_0(R_i) = n(n-i) EXACTLY
(no nonvanishing-product ambiguity). Here we check that ALL monomial terms of
the true resultant share the single weighted degree n(n-i).

f = x^n + sum_{j=2}^n a_j x^{n-j}  (monic traceless, a_0=1, a_1=0), w(a_j)=j.
H_i(f) = sum_j C(n-j,i) a_j x^{n-j-i}  (Hasse derivative).
"""
import sympy as sp

def hasse(coeffs, i, n, x):
    out = sp.Integer(0)
    for j, c in enumerate(coeffs):
        deg = n - j
        if deg >= i and c != 0:
            out += sp.binomial(deg, i) * c * x**(deg - i)
    return sp.expand(out)

def check(n):
    x = sp.symbols('x')
    a = [sp.Symbol('a%d' % j) if j >= 2 else (sp.Integer(1) if j == 0 else sp.Integer(0))
         for j in range(n + 1)]
    f = sum(a[j] * x**(n - j) for j in range(n + 1))
    results = {}
    for i in range(1, n):
        hi = hasse(a, i, n, x)
        R = sp.expand(sp.resultant(f, hi, x))
        # decompose into monomials; weight of a_j is j
        P = sp.Poly(R, *[sp.Symbol('a%d' % j) for j in range(2, n + 1)])
        weights = set()
        for mono, coeff in P.terms():
            exps = mono  # exponents of a_2..a_n in order
            wt = sum((j + 2) * e for j, e in enumerate(exps))
            weights.add(wt)
        homogeneous = (len(weights) == 1)
        results[i] = (weights, homogeneous)
    return results

if __name__ == '__main__':
    allok = True
    for n in [3, 4, 5]:
        r = check(n)
        target = {i: n*(n-i) for i in range(1, n)}
        ok = all(r[i][1] and r[i][0] == {target[i]} for i in r)
        allok = allok and ok
        print(f"n={n}: { {i: (sorted(r[i][0]), r[i][1]) for i in r} }  target {target}  -> {'OK' if ok else 'FAIL'}")
    print("ALL HOMOGENEITY CHECKS PASS" if allok else "FAILURES PRESENT")
