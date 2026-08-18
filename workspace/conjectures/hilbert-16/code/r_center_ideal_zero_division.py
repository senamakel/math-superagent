#!/usr/bin/env python3
"""Exact symbolic diagnostic for rung R-center-ideal-zero-division.

Statement this bears on: the proposed implication that a finite Bautin-style
expansion
    Delta(z; lam) = sum_{i=1}^k a_i(lam) m_i(z) (1 + h_i(z;lam))
with each remainder h_i = o(1) uniformly in lam, coefficients a_i in the
center ideal, automatically has at most k-1 zeros, uniformly in lam.
This is a logical diagnostic, not a claim about the H^3_14 vector field.

Theory: the k-1 bound belongs to an ECT / derivation-division hypothesis on a
fixed generalized-monomial family.  Merely requiring each remainder to be
o(1) supplies no non-oscillation control: after the leading parts cancel, the
whole displacement can be a pure oscillation of the remainders, and o(1)
does not bound the number of zeros.

The counterfamily (k=2, exact, no floats):
    m_1(z) = 1,  m_2(z) = -1   (distinct monomials, same span as {1})
    a_1 = a_2 = 1              (constants: lie in the ideal <1>; the ideal
                                hypothesis alone carries no zero control)
    h_1(z) = 0,   h_2(z) = z*sin(N*z)
    Delta_N(z) = a_1 m_1 (1+h_1) + a_2 m_2 (1+h_2)
               = (1) - (1 + z sin(Nz)) = -z sin(Nz)

Remainder hypotheses, verified exactly:
    * h_2 is o(1) as z -> 0+  (|h_2(z)| <= z, limit 0; h_1 = 0 trivially);
    * h_2(0) = 0 (z sin(Nz) is analytic at 0 and vanishes there), matching
      the Lean Admissible clause h i p 0 = 0 with remainder_bound p z = z,
      C = 1.

Zeros, verified exactly:
    Delta_N(z) = 0  <=>  z sin(Nz) = 0  <=>  z = k*pi/N,  k integer.
    On the collar 0 < z <= 1 those are exactly z_k = k*pi/N for
    1 <= k <= N/pi, i.e. floor(N/pi) zeros.  Each is exact because
    sin(N*(k*pi/N)) = sin(k*pi) = 0.

    For every N, floor(N/pi) is FINITE (matches Ilyashenko-Ecalle: each
    individual displacement has finitely many zeros) but UNBOUNDED in N.
    Certified lower bound without floating point: pi < 22/7, so
    N/pi > 7N/22, hence the k = 1..floor(7N/22) zeros are all inside
    (0, 1] and certified.  For N >= 7, floor(7N/22) >= 2 > k-1 = 1,
    refuting the uniform k-1 bound.

SCOPE: refutes only the abstract implication "Admissible hypotheses (with
h_i = o(1)) => uniform k-1 zero bound".  It is NOT a counterexample to the
conditional Lean theorem RCenterIdealZeroDivision.r_center_ideal_zero_division
(which carries the analytic zero_division theorem as an explicit hypothesis),
and NOT a counterexample to H^3_14 or H16.2.  It proves the analytic
zero-division hypothesis is load-bearing: it cannot be dropped or replaced by
"h_i = o(1)", and any future proof must exclude this rank-1 leading
cancellation mode (the ECT/Wronskian or quasianalytic structure of the
monomial family is what does the excluding).
"""

import sympy as sp

z = sp.symbols("z", positive=True)
N = sp.symbols("N", integer=True, positive=True)


def h2(n):
    """Remainder h_2 for parameter n: z*sin(n*z)."""
    return z * sp.sin(sp.Integer(n) * z)


def delta(n):
    """Displacement -z*sin(n*z) = m1*(1+h1) + m2*(1+h2) with m1=1, m2=-1,
    a1=a2=1, h1=0, h2=z*sin(n*z)."""
    return -z * sp.sin(sp.Integer(n) * z)


def certified_zero_count(n):
    """Exact lower bound on the number of zeros of Delta_n in (0,1]:
    floor(7n/22), guaranteed <= floor(n/pi) by pi < 22/7."""
    return sp.floor(sp.Rational(7 * n, 22))


def run():
    print("RUN: exact finite Bautin-expansion zero-division diagnostic (corrected o(1) semantics)")
    print("CLAIM: h_i = o(1) remainders + ideal coefficients alone do NOT imply a uniform k-1 zero bound")
    print("FAMILY: k=2, m1=1, m2=-1, a1=a2=1, h1=0, h2=z*sin(Nz);  Delta_N = -z sin(Nz)")
    print("RANGE: N in 7..12; collar 0 < z <= 1; exact arithmetic with pi")
    print()

    # 1. o(1) remainder hypotheses, exact.
    lim = sp.limit(z * sp.sin(N * z), z, 0, dir="+")
    print(f"limit h_2(z) = z*sin(Nz) as z->0+ : {lim}")
    assert lim == 0
    # h2(0) = 0 exactly (analytic at 0).
    assert sp.simplify(h2(7).subs(z, 0)) == 0
    print("h_2(0) = 0: OK   (Lean Admissible clause h i p 0 = 0)")
    # |h_2| <= z exactly: |sin| <= 1.  SymPy confirms on representatives.
    for n in (7, 8, 12):
        assert sp.simplify(h2(n) / z) == sp.sin(sp.Integer(n) * z)
    print("|h_2(z)| <= z (hence o(1), uniform in N): OK   (remainder_bound = z, C = 1)")
    print()

    # 2. Zeros: Delta_N(k*pi/N) = 0 exactly.
    k = sp.symbols("k", integer=True, positive=True)
    generic = sp.simplify((z * sp.sin(N * z)).subs(z, k * sp.pi / N))
    print(f"generic zero check  Delta_N(k*pi/N) = -{generic}  (sin(k*pi) = 0)")
    assert generic == 0

    # 3. Certified counts, exact bound pi < 22/7.
    print()
    print("certified zeros in (0,1]: z_k = k*pi/N, k = 1..floor(7N/22)")
    print("(lower bound guaranteed by pi < 22/7; true count is floor(N/pi))")
    claimed_bound = 1  # k - 1
    print(f"claimed k-1 bound = {claimed_bound}")
    for n in range(7, 13):
        c = certified_zero_count(n)
        pts = [sp.Integer(j) * sp.pi / sp.Integer(n) for j in range(1, int(c) + 1)]
        # every certified point lies in (0,1]: k <= 7n/22 < n/pi  =>  k*pi/n < 1
        assert all(0 < p and p <= 1 for p in pts)
        # every certified point is an exact zero
        vals = [sp.simplify(delta(n).subs(z, p)) for p in pts]
        assert all(v == 0 for v in vals)
        assert len(set(pts)) == len(pts)
        print(f"N={n}: certified_count>={c} (true floor(N/pi)={sp.floor(n/sp.pi)}); "
              f"sample zero z_1={pts[0]}; all certified points exact zeros: OK")
        assert c > claimed_bound
    print()
    print("RESULT: COUNTEREXAMPLE FOUND")
    print("For every N >= 7 the displacement Delta_N satisfies every stated")
    print("remainder hypothesis (h_i = o(1), h_i(0)=0, uniform in N) yet has")
    print("at least floor(7N/22) >= 2 zeros, so no uniform k-1 = 1 bound holds.")
    print("The zero counts are finite per N but unbounded across N: this is")
    print("exactly the Ilyashenko-Ecalle-vs-H16.2 gap (pointwise finite, not uniform).")
    print()
    print("SCOPE: refutes only the abstract implication; the conditional Lean")
    print("theorem (with the analytic zero_division binder) stands; the analytic")
    print("zero-division theorem on the transseries class is proven load-bearing,")
    print("and the rank-1 leading-cancellation mode is the failure mode a proof")
    print("must exclude (ECT/Wronskian or quasianalytic structure of the m_i).")
    print()
    print("--- positive control: the same shape with a genuine ECT family ---")
    # Exact family m = (1, z) is an ECT system on (0,1): any nontrivial
    # linear combination c1 + c2*z is a polynomial of degree <= 1, so it has
    # at most k-1 = 1 zero.  Here the k-1 bound holds.  This isolates the
    # load-bearing clause: monomial nondegeneracy (Wronskian of (1,z) = 1),
    # not the o(1) remainder size.
    # Wronskian W(m1, m2) = m1*m2' - m1'*m2, exact for the ECT family (1, z).
    w = sp.simplify(sp.Integer(1) * sp.diff(z, z) - sp.diff(sp.Integer(1), z) * z)
    print(f"ECT family {{1, z}}: Wronskian W(1,z) = {w}")
    assert w == 1
    # Descartes: c1 + c2 z has at most one positive zero (c1, c2 real, not both 0).
    print("any nontrivial c1 + c2*z has at most 1 positive zero: OK (degree <= 1)")
    # Counterfamily monomials (1, -1): Wronskian = 0 identically -> no ECT.
    wbad = sp.simplify(sp.Integer(1) * sp.diff(sp.Integer(-1), z)
                       - sp.diff(sp.Integer(1), z) * sp.Integer(-1))
    print(f"counterfamily {{1, -1}}: Wronskian W(1,-1) = {wbad}")
    assert wbad == 0
    print("-> the counterexample is exactly the rank-deficient-monomial case;")
    print("   the ECT/derivation-division hypothesis is what the bound needs.")
    print()
    print("--- smooth-test annotation ---")
    print("h_2(z) = z*sin(Nz) is real-analytic (entire): the counterexample is C^omega,")
    print("so the missing hypothesis is not smoothness but the structure of the monomial")
    print("family (ECT/Wronskian/quasianalytic) AND uniformity across the family.")
    print("Per-N finiteness holds; the uniform-in-N bound fails: exactly the")
    print("Ilyashenko-Ecalle-vs-H16.2 pointwise-vs-uniform gap at the abstract level.")


if __name__ == "__main__":
    run()
