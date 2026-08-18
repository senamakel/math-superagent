#!/usr/bin/env python3
"""Diagnostic attack on the I^1_6b slow-divergence/ECT shortcut.

Theory: ECT is a Wronskian property of one specified function family; it is
not preserved by adding independently ECT families, and first-order control
requires a nonzero leading coefficient (here the slow-divergence coefficient).
This is an exact toy diagnostic, not an I^1_6b vector-field counterexample.
complexity_class: polynomial; oracle_bound: symbolic degree <= 2.
"""
import sympy as s
x, eps = s.symbols('x eps')

def wronskian(fs):
    return s.factor(s.Matrix([[s.diff(f,x,j) for f in fs]
                              for j in range(len(fs))]).det())

def main():
    print('RUN: exact diagnostic for four second-type Dulac passages and vanishing slow divergence')
    print('ORACLE: exact Wronskians and first-order coefficient test; four passage blocks represented by two ECT pairs')
    print('RANGE: symbolic x, eps; polynomial degree <=2; no floating point')
    A=[1,x]; B=[-1,-x]
    print('W(A)=',wronskian(A),'W(B)=',wronskian(B),'W(A+B)=',wronskian([A[i]+B[i] for i in range(2)]))
    assert wronskian(A)!=0 and wronskian(B)!=0 and wronskian([A[i]+B[i] for i in range(2)])==0
    # A displacement with vanishing first-order slow-divergence coefficient.
    D=eps**2*(x-1)+eps**3*(x-2)**2
    first=s.diff(D,eps).subs(eps,0)
    second=s.diff(D,eps,2).subs(eps,0)/2
    print('D(eps,x)=',D,'; first-order coefficient=',first,'; second=',second)
    assert first==0 and second==(x-2)**2
    print('RESULT: naive closure and nonzero-first-order assumptions are both refuted in the toy model')
    print('STATUS: diagnostic only; no faithful dynamical counterexample and no conclusion about I^1_6b finiteness')
if __name__=='__main__': main()
