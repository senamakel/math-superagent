#!/usr/bin/env python3
"""Minimal robust independent check of ord_0(R_i)=n(n-i) using sympy's built-in
reduced grevlex GB and its `.reduce` to count standard monomials with a
stabilizing degree bound.  This avoids hand-rolled monomial enumeration bugs."""
import sympy as sp
from sympy import symbols, Poly, resultant, groebner, expand, binomial
from math import factorial

def hasse(f, x, i):
    p = sp.Poly(expand(f), x)
    return sp.expand(sum(binomial(j, i)*c*x**(j-i)
                         for j, c in p.terms() if j >= i))

def run(n):
    a = symbols(f'a2:{n+1}')
    x = symbols('x')
    f = x**n + sum(a[k]*x**(n-2-k) for k in range(n-1))  # a2..an
    # check the coefficient positions: f = x^n + a2 x^{n-2} + ... + an
    f = x**n + sum((a[k])*x**(n-(k+2)) for k in range(n-1))
    R = []
    for i in range(1, n):
        Hi = hasse(f, x, i)
        Ri = resource = resultant(Poly(f, x), Poly(Hi, x))
        R.append(Ri)
    # weighted order
    weight = {a[k]: k+2 for k in range(n-1)}
    ords = []
    for Ri in R:
        P = Poly(Ri, *a)
        ords.append(min(sum(e*weight[v] for v, e in zip(P.gens, m))
                        for m_, c in P.terms() for m in [m_]))
    expected = [n*(n-i) for i in range(1, n)]
    ok_ord = ords == expected
    print(f"n={n}: orders {ords} == {expected} : {ok_ord}")

    G = groebner(R, *a, order='grevlex')
    # standard monomial count by reducing all monomials up to a bound
    # G.reduce(m) returns 0 iff m in leading ideal (m NOT standard)
    maxdeg = sum(expected)  # generous bound; stabilize anyway
    from itertools import product
    def std_count(bound):
        cnt = 0
        m = len(a)
        for total in range(bound+1):
            # enumerate compositions
            if m == 0:
                if total == 0: cnt += 1
                continue
            def rec(rem, idx, acc):
                pass
            # use itertools product over exponents with fixed sum
            def gen(idx, rem, acc):
                nonlocal cnt
                if idx == m-1:
                    exps = tuple(acc)+ (rem,)
                    mono = sp.Mul(*[v**e for v, e in zip(a, exps)])
                    # standard iff not reducing to 0
                    if G.reduce(mono) != 0:
                        cnt += 1
                    return
                for e in range(rem+1):
                    gen(idx+1, rem-e, acc+[e])
            gen(0, total, [])
        return cnt
    prev = None
    length = None
    for d in [maxdeg, maxdeg+3, maxdeg+6]:
        c = std_count(d)
        if prev is not None and c == prev:
            length = c; break
        prev = c
    if length is None: length = prev
    exp_len = n**(n-2)
    ok_len = length == exp_len
    print(f"n={n}: quotient length {length} == n^(n-2)={exp_len} : {ok_len}")
    # Samuel identity
    po = 1
    for o in ords: po *= o
    pw = factorial(n)  # prod w(a_j)=2*..*n = n!
    samuel = po // pw
    ok_sam = samuel == length
    print(f"n={n}: Samuel prod(ords)/n! = {samuel} == length : {ok_sam}")
    return ok_ord and ok_len and ok_sam

if __name__ == '__main__':
    ok = True
    for n in [3, 4, 5]:
        try:
            ok &= run(n)
        except Exception as e:
            print(f"n={n} error: {e}")
            ok = False
    print("ALL CHECKS PASSED" if ok else "SOME CHECK FAILED")
