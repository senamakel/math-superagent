#!/usr/bin/env python3
"""Exact slow-divergence / ECT reconnaissance for the published DF2a chart.

Statement/evidence target: drr-df1a-df2a-cyclicity-sourced and GOAL.md item 4.
Theory: the slow-divergence integral is a parameter integral of the divergence
along a singular/periodic skeleton. For the elementary DF2a validation chart
we test the algebraic prerequisite only: logarithmic passage channels form an
ECT family precisely when their exact Wronskian is nonzero. This is not a
cyclicity proof.

The chart used here is an explicit local validation model, not a transcription
of the paper's full global quadratic normal form:
  f0(t)=1, f1(t)=t, f2(t)=t^2, f3(t)=t^2 log(t), t>0.
The first three are the ordinary slow-divergence polynomial channels; f3 is a
second-type logarithmic channel. Exact differentiation gives Wronskians.
A vanishing Wronskian at a boundary is a mechanical obstruction to blindly
applying ordinary ECT there, while positivity on a compact subinterval is an
exact certificate for this toy family only.
"""
import sympy as sp
from pathlib import Path


def wronskian(fs, t):
    return sp.factor(sp.det(sp.Matrix([[sp.diff(f, t, j) for f in fs]
                                       for j in range(len(fs))])))


def run():
    t = sp.symbols('t', positive=True)
    L = sp.symbols('L', real=True)  # formal symbol for log(t)
    fs = [sp.Integer(1), t, t**2, t**2 * L]
    ws = [wronskian(fs[:k], t) for k in range(1, 5)]
    # The derivative operator must include d(log t)/dt=1/t.
    # Recompute the genuine log channel with SymPy's log for the final test.
    genuine = [sp.Integer(1), t, t**2, t**2 * sp.log(t)]
    genuine_ws = [wronskian(genuine[:k], t) for k in range(1, 5)]
    return t, fs, ws, genuine_ws


def guard_naive_examples():
    from brute import verify_all
    results = verify_all()
    assert all(ok for _name, ok, _res in results)
    return len(results)


if __name__ == '__main__':
    print('RUN: exact DF2a slow-divergence/ECT symbolic validation model')
    print('ORACLE: brute.verify_all; then exact Wronskians for 1,t,t^2,t^2 log(t)')
    print('RANGE: t>0 symbolic; compact test interval 1<=t<=2; no parameter enumeration')
    print('PRECISION: exact SymPy arithmetic; log differentiated symbolically; no floats')
    n = guard_naive_examples()
    print(f'GUARD: reproduced {n} problem.md worked examples: PASS')
    t, fs, ws, genuine_ws = run()
    for i, w in enumerate(ws, 1):
        print(f'FORMAL_W{i}={w}')
    for i, w in enumerate(genuine_ws, 1):
        print(f'EXACT_LOG_W{i}={w}')
    print(f'RESULT: exact logarithmic channel gives W4={genuine_ws[3]}; hence nonzero on t>0')
    assert sp.simplify(genuine_ws[3] - 4/t) == 0
    print('LIMITATION: this certifies only the displayed local ECT toy, not DF2a global cyclicity')
    print('LIMITATION: no paper-specific normal form, transition maps, parameter domain, or zero bound was encoded')
