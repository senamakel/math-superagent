"""Exact oracle for a finite algebraic ECT claim and its obstruction.

Claim ID: h16-i6b-four-passage-ect-obstruction.
The proposed shortcut is: if each of four passage contributions is an ECT
pair, then their sum is an ECT system. This is false algebraically: cancellation
can destroy even rank. We test exact polynomial representatives, not dynamics.
"""
import sympy as sp
from naive_examples_oracle import naive_count

x, a = sp.symbols('x a')

def wronskian(fs):
    return sp.simplify(sp.det(sp.Matrix([[sp.diff(f, x, j) for f in fs] for j in range(len(fs))])))

def run():
    print('RUN: exact four-passage/ECT oracle with naive worked-example guard')
    print('ORACLE: naive_count for problem.md examples; exact Wronskians over Q[a,x]')
    print('PARAMETERS: x symbolic; a in {0,1}; polynomial representatives degree <=2')
    print('PRECISION: exact SymPy rationals/symbolics; no floating point')

    # Required oracle reproduction, explicitly serving as a guard.
    cases = {
        'cubic A=1-u': ([1, -1], 1),
        'linear centre A=0': ([0], 0),
        'linear expanding focus A=1': ([1], 0),
        'two cycles A=(1-u)(2-u)': ([2, -3, 1], 2),
        'semi-stable A=(1-u)^2(2-u)': ([2, -5, 4, -1], 1),
    }
    for name, (coeffs, expected) in cases.items():
        got = naive_count(coeffs)
        print(f'GUARD {name}: got={got}, expected={expected}, check={got == expected}')
        assert got == expected

    # Each pair separately has nonzero Wronskian, but the four-passage sum can cancel.
    pair1 = [sp.Integer(1), x]
    pair2 = [-sp.Integer(1), -x]
    w1, w2 = wronskian(pair1), wronskian(pair2)
    summed = [sp.expand(pair1[i] + pair2[i]) for i in range(2)]
    ws = wronskian(summed)
    print(f'W(pair1)={w1}; W(pair2)={w2}; summed={summed}; W(sum)={ws}')
    assert w1 != 0 and w2 != 0 and ws == 0

    # Boundary parameter demonstrates rank loss at the exact boundary a=0.
    family = [a, a*x]
    wf = wronskian(family)
    boundary = [f.subs(a, 0) for f in family]
    wb = wronskian(boundary)
    print(f'family={family}; W(family)={wf}; boundary a=0={boundary}; W(boundary)={wb}')
    assert sp.expand(wf - a**2) == 0 and wb == 0
    print('RESULT: proposed ECT closure under four-passage addition is REFUTED')
    print('SCOPE: obstruction is algebraic/logical, not a faithful I^1_6b dynamical counterexample')

if __name__ == '__main__':
    run()
