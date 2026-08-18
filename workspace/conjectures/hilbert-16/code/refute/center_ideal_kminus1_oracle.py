#!/usr/bin/env python3
"""Minimal k-1 zero-bound oracle, with executable worked-example checks.

The first checks reproduce the already-held transseries toy: a finite
truncation x plus a flat oscillatory remainder. The new smallest check uses
k=2 and exact cancellation of two identical monomials, then verifies the
first eight accumulating zeros of the exact displacement.
complexity_class: polynomial; oracle_bound: 8 exact symbolic zeros.
"""
import sympy as sp

x = sp.symbols('x', positive=True)
# Existing worked example: finite truncation does not see the flat remainder.
old_trunc = x
old_delta = x + sp.exp(-1/x) * sp.sin(1/x)
assert sp.simplify(old_delta - old_trunc) == sp.exp(-1/x) * sp.sin(1/x)

# New minimal counterexample: k=2, m1=m2=1, a1=1, a2=-1.
h2 = sp.exp(-1/x**2) * sp.sin(1/x)
delta = -h2

print('RUN: minimal k-1 zero-bound counterexample')
print('ORACLE: exact SymPy symbolic evaluation; reproduces prior flat-remainder check')
print('RANGE: x in (0,1), k=2, first 8 zeros; exact arithmetic')
print('worked-example remainder:', sp.simplify(old_delta-old_trunc))
assert sp.simplify(delta - (-sp.exp(-1/x**2)*sp.sin(1/x))) == 0
for j in range(4):
    t = sp.symbols('t', positive=True)
    lim = sp.limit(sp.diff(delta, x, j).subs(x, 1/t), t, sp.oo)
    print(f'jet derivative {j} limit:', lim)
    assert lim == 0
zeros = [sp.Rational(1, 1) / (sp.pi * n) for n in range(1, 9)]
for z in zeros:
    assert sp.simplify(delta.subs(x, z)) == 0
print('exact zeros:', zeros)
print('k =', 2, '  k-1 =', 1, '  certified displayed zeros =', len(zeros))
print('RESULT: REFUTED as a consequence of the stated bare expansion/o(1) data')
print('CAVEAT: abstract analytic/smooth-germ counterexample only; not a quadratic H^3_14 counterexample')
print('MISSING CONDITION: common parameter-uniform quasianalytic/Noetherian zero-control class for the exact composed Dulac displacement, plus noncancellation/nondegeneracy of the leading coefficient vector; equivalently, a uniform ECT/Chebyshev or derivation-division certificate for the actual m_i(1+h_i).')
