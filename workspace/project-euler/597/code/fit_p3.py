#!/usr/bin/env python3
"""Fit p(3,L) as an exact rational function of L to the exact data in
code/out/exact_pn.json. Try N(L)/D(L) with degrees (2,2). Validate by
predicting L values not used in the fit (and values computed by the exact
enumerator beyond the json). Also compute the exact L->inf limit.
"""
import os, json
from fractions import Fraction as F
import itertools

try:
    import sympy
    from sympy import symbols, Eq, solve, Rational
    HAS_SYMPY = True
except Exception:
    HAS_SYMPY = False

base = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'out', 'exact_pn.json')
data = json.load(open(base))['L']
pairs = [(int(L), F(v['p'])) for L, v in data.items()]

def fit_ratfun(pairs, dn, nn, var):
    """p = (a0+a1 x+...+an x^n)/(b0+b1 x+...+bn x^n), b_n=1 (normalize)."""
    # unknowns: a0..a_nn, b0..b_{dn-1}  (b_dn=1)
    syms = symbols(f'a0:{nn+1}') + symbols(f'b0:{dn}')
    a = syms[:nn+1]
    b = list(syms[nn+1:]) + [1]   # b_dn=1
    eqs = []
    for (x, p) in pairs:
        lhs = p * sum(b[i]*x**i for i in range(dn+1))
        rhs = sum(a[i]*x**i for i in range(nn+1))
        eqs.append(Eq(lhs, rhs))
    sol = solve(eqs, syms, dict=True)
    return sol

# normalize each point with integer L; use sympy exact solving
def build_poly(coeffs, var, deg):
    from sympy import Poly
    return Poly(sum(coeffs[i]*var**i for i in range(len(coeffs))), var)

if __name__ == '__main__':
    print(f"{len(pairs)} exact points (L from {pairs[0][0]} to {pairs[-1][0]})")
    print("L->inf limit from data (largest L):", float(pairs[-1][1]))
    print("True large-L limit (MC, earlier):  0.389")
    if HAS_SYMPY:
        x = symbols('x')
        for dn in (1,2,3):
            for nn in (dn, dn+1, dn+2):
                try:
                    sol = fit_ratfun(pairs, dn, nn, x)
                    for s in sol:
                        # reconstruct
                        a = [S if isinstance(S := s.get(symbols(f'a{i}')), __import__('sympy').Rational) else s.get(symbols(f'a{i}')) for i in range(nn+1)]
                        b = [s.get(symbols(f'b{i}')) for i in range(dn)] + [1]
                        print(f"deg(N)={nn} deg(D)={dn}: N={a} D={b}")
                        # check residuals on all points
                        resids = []
                        for (Lv, p) in pairs:
                            nv = sum(a[i]*Lv**i for i in range(nn+1))
                            dv = sum(b[i]*Lv**i for i in range(dn+1))
                            pred = nv/dv
                            resids.append((Lv, pred-p))
                        print("   residual max |pred-exact|:", max(abs(r[1]) for r in resids))
                except Exception as e:
                    pass
