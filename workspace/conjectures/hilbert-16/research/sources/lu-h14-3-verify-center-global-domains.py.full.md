<!-- source: https://arxiv.org/src/2607.13785v2/anc/h14_3_reproducibility/certificates/verify_h14_center_global_domains.py | converted from plain text -->

#!/usr/bin/env python3
"""Exact symbolic checks for the two global H14 center components."""

import sympy as sp

x, y, B, m, a = sp.symbols("x y B m a", real=True)
z = sp.symbols("z", positive=True)

def check_reversible_component() -> None:
    p = -y + B * x**2 + m * y**2
    q = x * (1 + y)

    # H_x and H_y follow from H=(1/2)z^(-2B)x^2+V(z),
    # V_z=z^(-2B-1)((z-1)-m(z-1)^2).
    h_x = z ** (-2 * B) * x
    h_y = (
        -B * z ** (-2 * B - 1) * x**2
        + z ** (-2 * B - 1) * ((z - 1) - m * (z - 1) ** 2)
    )
    lie = sp.factor((h_x * p + h_y * q).subs(y, z - 1))
    assert lie == 0

    z_s = 1 + 1 / m
    potential_second = sp.factor(
        z * sp.diff(z ** (-2 * B) * (z - 1) * (1 - m * (z - 1)), z)
    )
    at_saddle = sp.factor(potential_second.subs(z, z_s))
    assert sp.simplify(
        at_saddle + (m + 1) / (m * (1 + 1 / m) ** (2 * B))
    ) == 0

    omega = (z ** (-2 * B) - 1) / (2 * B)
    potential = (
        (1 + m) * omega
        + (1 + 2 * m) * (z ** (1 - 2 * B) - 1) / (1 - 2 * B)
        - m * (z ** (2 - 2 * B) - 1) / (2 - 2 * B)
    )
    potential_minus = (
        -(1 + m) / (2 * B)
        - (1 + 2 * m) / (1 - 2 * B)
        + m / (2 - 2 * B)
    )
    barrier_difference = sp.factor(
        potential_minus - potential.subs(z, z_s)
    )
    expected_difference = (
        2
        * (B + m)
        / ((-2 * B) * (1 - 2 * B) * (2 - 2 * B))
        * ((1 + m) / m) ** (1 - 2 * B)
    )
    assert sp.simplify(barrier_difference - expected_difference) == 0

    print("reversible first-integral Lie derivative: OK")
    print("reversible extra critical point: (x,y)=(0,1/m)")
    print("reversible potential second derivative at gate:", at_saddle)
    print("reversible source-minus-saddle barrier identity: OK")

def check_quadratic_component() -> None:
    p = -y + B * x**2 - B * y**2 + a * x
    q = (1 + y) * (x - a * y)

    k = (
        B**2 * x**2
        - B**2 * y**2
        + B * a * x * y
        + 2 * B * a * x
        - B * x**2
        - 2 * B * y
        + a**2 * y
        + a**2
        - a * x
        - 1
    )
    inverse_factor = (1 + y) * k / (a**2 - 1)
    inverse_factor_identity = sp.factor(
        p * sp.diff(inverse_factor, x)
        + q * sp.diff(inverse_factor, y)
        - (sp.diff(p, x) + sp.diff(q, y)) * inverse_factor
    )
    assert inverse_factor_identity == 0

    gate = {x: -a / B, y: -1 / B}
    assert sp.factor(p.subs(gate)) == 0
    assert sp.factor(q.subs(gate)) == 0
    assert sp.factor(k.subs(gate)) == 0

    jacobian = sp.Matrix([[sp.diff(p, x), sp.diff(p, y)], [sp.diff(q, x), sp.diff(q, y)]])
    gate_det = sp.factor(jacobian.det().subs(gate))
    assert gate_det == (B - 1) * (a - 1) * (a + 1) / B

    axis_factor = sp.factor(k.subs(x, a * y))
    assert axis_factor == (a - 1) * (a + 1) * (B * y + 1) ** 2

    print("quadratic-center inverse integrating factor: OK")
    print("quadratic-center extra critical point: (x,y)=(-a/B,-1/B)")
    print("quadratic-center gate determinant:", gate_det)
    print("invariant-conic restriction to x=a*y:", axis_factor)

if __name__ == "__main__":
    check_reversible_component()
    check_quadratic_component()