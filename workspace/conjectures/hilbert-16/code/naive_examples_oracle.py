"""Naive exact oracle for the worked radial examples in problem.md.
Claim bearing: the definition/example consistency portion of H16.2; not a
full limit-cycle solver. For X=(x A(r^2), y A(r^2)), cycles correspond to
positive simple roots of A(u); repeated roots are not isolated cycles."""
from fractions import Fraction
import sympy as sp

u = sp.symbols('u')

def naive_count(coeffs):
    """Count positive roots of A(u), excluding repeated roots, exactly."""
    p = sp.Poly(sum(sp.Rational(c) * u**i for i, c in enumerate(coeffs)), u)
    if p.is_zero or p.degree() == 0:
        return 0
    roots = sp.polys.polytools.intervals(p, eps=sp.Rational(1, 10)**8)
    return sum(1 for (a, b), mult in roots if a > 0 and b > 0 and mult == 1)

def main():
    cases = {
        'cubic A=1-u': ([1, -1], 1),
        'linear centre A=0': ([0], 0),
        'linear expanding focus A=1': ([1], 0),
        'two cycles A=(1-u)(2-u)': ([2, -3, 1], 2),
        'semi-stable A=(1-u)^2(2-u)': ([2, -5, 4, -1], 1),
    }
    for name, (coeffs, expected) in cases.items():
        got = naive_count(coeffs)
        print(f'{name}: got={got}, expected={expected}, check={got == expected}')
        assert got == expected
    print('ALL WORKED EXAMPLES PASS')

if __name__ == '__main__':
    main()
