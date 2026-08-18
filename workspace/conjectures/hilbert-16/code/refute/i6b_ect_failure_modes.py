#!/usr/bin/env python3
"""Exact falsifier for the proposed finite-ECT inference.

Theory: an ECT system of k functions requires every initial Wronskian to be
nonzero on the domain.  This program checks two failure modes: (i) sums of
individually ECT contributions can cancel; (ii) a parameter-dependent leading
slow-divergence coefficient can vanish, making the limiting family lose rank.
This is an oracle for the logical implication only, not a model of the exact
quadratic vector field.
"""
import sympy as s
x, a = s.symbols('x a')

def W(fs):
    return s.factor(s.Matrix([[s.diff(f,x,j) for f in fs] for j in range(len(fs))]).det())

# Each pair is an ECT pair, but their sum cancels exactly.
u1, u2 = 1, x
v1, v2 = -1, -x
sum_family = [s.expand(u1+v1), s.expand(u2+v2)]
# A rank-two family for a != 0 collapses at the vanishing slow-divergence stratum.
vanishing_family = [a, a*x]
print('oracle: exact symbolic ECT failure-mode probe')
print('range: x symbolic; parameter a, with boundary stratum a=0')
print('precision/workers: SymPy exact arithmetic, 1 CPU, no floats')
print('individual W(1,x) =', W([u1,u2]))
print('individual W(-1,-x) =', W([v1,v2]))
print('sum family =', sum_family, ' W =', W(sum_family))
print('vanishing family =', vanishing_family, ' W =', W(vanishing_family))
print('boundary a=0 family =', [f.subs(a,0) for f in vanishing_family],
      ' W =', W(vanishing_family).subs(a,0))
assert W([u1,u2]) != 0 and W([v1,v2]) != 0
assert W(sum_family) == 0
assert W(vanishing_family).subs(a,0) == 0
print('RESULT: both naive ECT inferences fail exactly')
print('STATUS: logical obstruction only; no faithful I^1_6b dynamical counterexample')
