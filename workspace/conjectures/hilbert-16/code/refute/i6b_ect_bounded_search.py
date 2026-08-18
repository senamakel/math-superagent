#!/usr/bin/env python3
"""Bounded exact attack on the I^1_6b four-passage ECT shortcut.

Theory: an ECT system of k functions requires each initial Wronskian to be
nonzero throughout the open domain. This is only a falsifier of the proposed
reduction, not of I^1_6b itself. We enumerate fixed small integer coefficient
models for four second-type passage surrogates, compose two residual channels,
and test the resulting three-function derivation--division family exactly.
complexity_class: polynomial in the fixed coefficient-box size (symbolic
expressions have bounded degree); oracle_bound: coefficients in [-2,2].
"""
import itertools
import sympy as s

t,c,d,L=s.symbols('t c d L')

def W(fs):
    return s.factor(s.Matrix([[s.diff(f,t,j) for f in fs] for j in range(len(fs))]).det())

def main():
    # D_i = alpha*c + beta*d + gamma*t + delta*L.
    box=range(-2,3)
    checked=0; failures=[]
    # fixed passage templates, varying only signs/scales in a bounded box
    for coeffs in itertools.product(box, repeat=4):
        a,b,g,e=coeffs
        D1=a*c+b*d+g*t+e*L
        D2=b*c+a*d-g*t+e*L
        D3=g*c+e*d+a*t+b*L
        D4=e*c+g*d-a*t+b*L
        F=s.expand(D1+D2+D3*D4)
        G=s.expand(D1*D4-D2*D3)
        J=s.expand(s.diff(F,c)*s.diff(G,d)-s.diff(F,d)*s.diff(G,c))
        fs=[s.expand(z.subs({c:0,d:0})) for z in (F,G,J)]
        w3=s.factor(W(fs))
        checked+=1
        if w3==0:
            failures.append(coeffs)
            if len(failures)>=5: break
    print('RUN: bounded exact I^1_6b ECT falsifier')
    print('ORACLE: four affine second-type passage surrogates; residuals F,G; J=F_c G_d-F_d G_c')
    print('RANGE: coefficient box [-2,2]^4; stopped after first 5 exact W3 failures')
    print('PRECISION/WORKERS: SymPy exact integer arithmetic, 1 CPU, no floats')
    print('TESTED:',checked,'coefficient tuples')
    print('FIRST_FAILURES:',failures)
    assert failures
    print('RESULT: bounded toy family contains exact rank-loss cases (W3 identically zero)')
    print('STATUS: bounded failed search against shortcut only; not a faithful dynamical counterexample')
if __name__=='__main__': main()
