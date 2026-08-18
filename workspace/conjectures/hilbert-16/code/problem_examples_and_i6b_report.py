"""Exact reproduction of problem.md worked examples and I^1_6b gate.

Claim/evidence: worked-example consistency and the precise blocker for the
slow-divergence/ECT route. The radial oracle is an intentionally bounded
oracle, not a solver for H16.2. The I^1_6b part does not instantiate the
actual RR family: it checks only whether the adopted ECT inference is valid
without its missing Dulac-map data.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from naive_examples_oracle import naive_count
from i6b_four_passage_oracle import wronskian
import sympy as sp

x, a = sp.symbols('x a')

def reproduce_examples():
    cases = {
        'cubic A=1-u': ([1, -1], 1),
        'linear centre A=0': ([0], 0),
        'linear expanding focus A=1': ([1], 0),
        'two cycles A=(1-u)(2-u)': ([2, -3, 1], 2),
        'semi-stable A=(1-u)^2(2-u)': ([2, -5, 4, -1], 1),
    }
    for name, (coeffs, expected) in cases.items():
        got = naive_count(coeffs)
        print(f'EXAMPLE {name}: got={got}, expected={expected}, check={got == expected}')
        assert got == expected

def ect_gate():
    # Exact algebraic counterexample to the proposed closure inference.
    p = [sp.Integer(1), x]
    q = [-sp.Integer(1), -x]
    wp, wq = wronskian(p), wronskian(q)
    summed = [sp.expand(p[i] + q[i]) for i in range(2)]
    ws = wronskian(summed)
    print(f'ECT gate: W(p)={wp}, W(q)={wq}, W(p+q)={ws}')
    assert wp != 0 and wq != 0 and ws == 0
    # Exact rank collapse on a vanishing leading-coefficient stratum.
    fam = [a, a*x]
    wf = wronskian(fam)
    wb = wronskian([f.subs(a, 0) for f in fam])
    print(f'boundary gate: W(a,a*x)={wf}, W|a=0={wb}')
    assert sp.expand(wf-a**2) == 0 and wb == 0

def main():
    print('RUN: exact worked-example reproduction plus I^1_6b ECT gate')
    print('ORACLE: naive_count; exact polynomial Wronskians')
    print('RANGE: five radial examples; ECT surrogates over Q[a,x], boundary a=0')
    print('PRECISION: exact integers/rationals/symbolics; no floating point')
    reproduce_examples()
    ect_gate()
    print('RESULT: examples reproduced; ECT shortcut blocked, not a dynamical refutation')
    print('BLOCKER: exact RR four second-type Dulac maps, uniform remainder class, and stratum-wise zero theorem are unavailable')

if __name__ == '__main__':
    main()
