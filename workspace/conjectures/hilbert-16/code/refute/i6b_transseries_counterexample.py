#!/usr/bin/env python3
"""Exact attack on the proposed finite-dimensional ECT reduction.

Theory: Theorem 2.3 of Rousseau--Shan--Zhu gives a second-type Dulac map
with a compensator and a remainder phi whose regularity is only C^{l-2}
in generalized monomials; property J is an asymptotic smallness condition,
not membership in a finite-dimensional ECT space.  A finite truncation
therefore cannot control the exact zero set without a separate uniform
zero-transfer hypothesis.

This is a symbolic transseries counterexample to the inference, not a
quadratic vector-field counterexample. complexity_class: polynomial;
oracle_bound: symbolic truncation order <= 4.
"""
import sympy as s
x, a, e = s.symbols('x a e', positive=True)

def main():
    print('RUN: exact transseries attack on finite-dimensional ECT closure')
    print('ORACLE: symbolic compensator plus flat/log remainder; exact derivatives and zeros')
    print('RANGE: x in (0,1), parameter a, truncation order <=4; no floating point')
    # At a=0, omega=-log x. Add a flat term invisible to every finite power-log jet.
    omega = -s.log(x)
    flat = s.exp(-1/x)
    delta = x + a*x*omega + flat*(s.sin(1/x))
    # The proposed finite-dimensional truncation sees only x+a*x*(-log x).
    trunc = x + a*x*omega
    remainder = s.simplify(delta-trunc)
    print('omega(a=0,x)=',omega)
    print('exact displacement at a=0=',delta.subs(a,0))
    print('finite truncation at a=0=',trunc.subs(a,0))
    print('remainder=',remainder)
    assert remainder == flat*s.sin(1/x)
    # Every derivative of exp(-1/x) sin(1/x) tends to 0 as x->0+;
    # verify the first four explicitly by substitution x=1/t and limits.
    for k in range(5):
        dk = s.diff(remainder, x, k).subs(a,0).subs(x,1/s.symbols('t', positive=True))
        lim = s.limit(dk, s.symbols('t', positive=True), s.oo)
        print(f'jet derivative k={k}: limit={lim}')
        assert lim == 0
    # Yet it has infinitely many exact zeros accumulating at 0.
    zeros = [1/(s.pi*s.Integer(n)) for n in range(1,6)]
    print('zeros of remainder component in (0,1):',zeros)
    assert all(s.simplify(remainder.subs({a:0,x:z})) == 0 for z in zeros)
    print('RESULT: finite jet/ECT data does not determine the exact displacement zero set')
    print('MISSING HYPOTHESIS: a parameter-uniform quasianalytic/Noetherian class closed under the four compositions, or an explicit zero-transfer theorem controlling the remainder; property J/C^k alone is insufficient')
    print('STATUS: symbolic counterexample to the reduction inference only; not a faithful I^1_6b dynamical counterexample')

if __name__ == '__main__': main()
