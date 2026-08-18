#!/usr/bin/env python3
"""Exact minimal obstruction to sum-of-ECT inference.

Theory: an ECT pair requires a nonzero 2x2 Wronskian; addition of ECT
contributions does not preserve that property, and parameter specialization
can lower rank. This tests the algebraic inference only, not I^1_6b.
complexity_class: polynomial; oracle_bound: two affine pairs.
"""
import sympy as s
x,a=s.symbols('x a')
def wronskian(fs):
    return s.det(s.Matrix([[f,s.diff(f,x)] for f in fs])).factor()
def main():
    p=[1,x]; q=[-1,-x]
    assert wronskian(p)==1 and wronskian(q)==-1
    total=[s.expand(p[i]+q[i]) for i in range(2)]
    assert total==[0,0] and wronskian(total)==0
    family=[a,a*x]
    assert wronskian(family)==a**2 and wronskian([z.subs(a,0) for z in family])==0
    print('RUN: exact minimal ECT closure and specialization falsifier')
    print('ORACLE: two affine ECT pairs and one rank-scaled pair')
    print('RANGE: symbolic x,a; exact integer arithmetic; no floats')
    print('W(p)=',wronskian(p),'W(q)=',wronskian(q),'sum=',total,'W(sum)=',wronskian(total))
    print('W([a,a*x])=',wronskian(family),'at a=0 -> 0')
    print('RESULT: inference refuted algebraically; missing non-cancellation and stratum-uniform rank hypotheses')
    print('STATUS: not a dynamical counterexample')
if __name__=='__main__': main()
