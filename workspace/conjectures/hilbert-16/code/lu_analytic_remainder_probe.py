"""Bounded exact/symbolic probe of the analytic-remainder gap in Lu H^3_14.

Claim bearing: drr-lu-claims-h14-3. This does not prove Lu's theorem. It
checks, in a deliberately finite regime, whether the algebraic focal ideal
relations can force a nonzero analytic remainder to have a unique local zero.
The probe uses exact rational polynomials and Taylor truncations only.
"""
import sympy as sp

z, a, b = sp.symbols('z a b')

def probe(max_degree=10):
    # A model displacement: algebraic Bautin part plus analytic remainder R.
    # The smallest nonzero Taylor coefficient is the exact order of vanishing.
    rows = []
    for order in range(1, max_degree + 1):
        R = z**order * (1 + z)  # exact analytic polynomial remainder
        d = sp.expand(R)
        roots = sp.solve(sp.Eq(d, 0), z)
        local = [r for r in roots if r == 0 or (r.is_number and abs(complex(r)) < 1)]
        rows.append((order, sp.Poly(d, z).coeff_monomial(z**order), roots, local))
    return rows

def main():
    print('RUN: bounded exact Taylor probe for Lu H^3_14 analytic remainder')
    print('RANGE: vanishing orders 1..10; rational polynomial truncations; no full-size search')
    rows = probe(10)
    for order, lead, roots, local in rows:
        print(f'order={order} leading={lead} roots={roots} local_roots={local}')
        assert lead == 1 and 0 in roots
    # Counterexample to the stronger, unjustified inference “nonzero remainder => unique zero”.
    R = z**2 * (1-z**2)
    roots = sp.solve(sp.Eq(R, 0), z)
    print(f'counterprobe R=z^2*(1-z^2): roots={roots}')
    assert set(roots) == {-1, 0, 1}
    print('RESULT: finite Taylor data confirms order bookkeeping, but refutes')
    print('the inference that analyticity plus a nonzero remainder alone gives uniqueness.')
    print('STATUS: analytic-remainder issue remains unresolved; Lu theorem not verified.')

if __name__ == '__main__':
    main()
