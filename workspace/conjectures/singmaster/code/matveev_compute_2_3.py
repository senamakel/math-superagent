"""Matveev 2000 Thm 2.2 / Thm 2.3(ii) explicit effective constants for the
(2,3) triangular=tetrahedral curve C(x,2)=C(y,3), i.e. 3x(x-1)=y(y-1)(y-2).

Deliverables (per task):
  1. direct-algebra verification of the reduction 6*C(x,2) - 6*C(y,3) ==
     3x(x-1) - y(y-1)(y-2) (sympy, exact);
  2. for the concrete solutions 120=C(16,2)=C(10,3), 1540=C(56,2)=C(22,3),
     7140=C(120,2)=C(36,3): factor a and the two-sided product equality
     P = 3x(x-1) = y(y-1)(y-2) = Q, exhibit the linear form in logs of primes
     Lambda = sum_j b_j ln p_j and confirm Lambda == 0 (P == Q forces every
     b_j = 0: unique factorization); n = 0 nonzero terms, so Theorem 2.2 does
     not apply to the true form -- stated explicitly, it is vacuous for exact
     solutions;
  3. the real content: DELTA forms ln(P_a) - ln(Q_b) for pairs of DIFFERENT
     solutions have Lambda = ln(a/b) != 0, i.e. n >= 2 nonzero coefficients;
     for those, compute the full Thm 2.2 constant machinery (K=Q real:
     D = D_K/kappa = 1, rho = rank_R{ln p_j} = 1, C3 = n/rho = n,
     A_j = h(p_j) = ln p_j, C1, C2 per (2.4), omega per (2.5), C0' per (2.15),
     B per (2.14)) and evaluate the lower bound
     ln|Lambda| > -112 * 2^n * C2 * C0' * D^2 * omega * ln(2 e B).
     Also the Thm 2.3(ii) improvement theta = 1/(2 - 2/(n e^{n+1})).
  4. the requested generic routine: given n = number of distinct primes of a,
     compute the constants for the sample a in {120, 1540, 7140, 3003, 24310}
     using the coefficient vector b_j = 1 (representative nonzero form
     Lambda = ln a; Theorem 2.2 needs Lambda != 0 and b_n != 0, which the
     true exact-solution form would not provide).
  5. exact verification of the Kummer condition (1.5) for the primes involved:
     [Q(sqrt(p1),...,sqrt(pn)):Q] = 2^n.  For distinct primes it holds
     automatically (no nonempty subset product is a square); checked by
     enumeration of all 2^n subsets with exact arithmetic.
  Also checked: the theorem's internal hypotheses (2.9)-(2.11) with
  C0 = 1.23*C0' and W0 = ln(2eB) as in the paper's proof of Thm 2.2 (§13),
  reported pass/fail per form.

Author's note on the parameter line in the task: "C3 = rho = n" is not
dimensionally right -- rho = 1 (logs are real numbers), C3 = n/rho = n.
D = 1.  The Kummer condition is *required* by Thm 2.2 but is automatic for
rational primes, which is what "no Kummer condition needed" means operationally.

All arithmetic exact except the final float evaluation of C1, C2, omega,
C0', B, exponent (doubles suffice: magnitudes ~1e25 in the exponent).
"""
from lib.matveev import (
    binomial_reduction_identity,
    two_sided_products,
    linear_form,
    kummer_subset_verification,
    matveev_constants,
)
import math

SOLUTIONS = [(16, 10), (56, 22), (120, 36)]   # C(x,2) = C(y,3) = a
A_VALUES = [120, 1540, 7140, 3003, 24310]     # sample a whose distinct-prime count n is used


def theorem_conditions_check(c):
    """Check hypotheses (2.9)-(2.11) of Thm 2.1 (verified in §13 for Thm 2.2)
    with C0 = 1.23*C0' and W0 = ln(2eB), rho=1, D=1, theta, E as stored.
    Returns list of (label, value, ok)."""
    n, C1, C2, C3, D, omega, An = c["n"], c["C1"], c["C2"], c["C3"], c["D"], c["omega"], c["A"][-1]
    theta, E = c["theta"], c["E"]
    C0 = 1.23 * c["C0prime"]
    W0 = math.log(2 * math.e * c["B"])
    m = min(C0, W0)
    checks = []
    # (2.9): D*omega*min(C0,W0)/(2*C3) >= 1
    v = D * omega * m / (2 * C3)
    checks.append(("(2.9) D*omega*min(C0,W0)/(2*C3) >= 1", v, v >= 1))
    # (2.10): omega/(C1*theta*A_j) * min(C0,W0)/(2*C3) >= 1 for all j
    for j, a in enumerate(c["A"]):
        v = omega / (C1 * theta * a) * m / (2 * C3)
        checks.append((f"(2.10) j={j} omega/(C1*theta*A_j)*min(C0,W0)/(2*C3) >= 1", v, v >= 1))
    # (2.11): 3*(C1*D*theta)^(n-1)*D*Omega/A_j * (C3 exp(C3) E e^{2theta})^(rho-1) * C0/C3 >= 1
    rho = c["rho"]
    factor = 3 * (C1 * D * theta) ** (n - 1) * D * (C3 * math.exp(C3) * E * math.exp(2 * theta)) ** (rho - 1) * (C0 / C3)
    for j, a in enumerate(c["A"]):
        v = factor * c["Omega"] / a
        checks.append((f"(2.11) j={j}", v, v >= 1))
    return checks


def main():
    print("=" * 78)
    print("Matveev 2000 Thm 2.2 / 2.3(ii) explicit constants, (2,3) curve")
    print("C(x,2)=C(y,3)  <=>  3x(x-1) = y(y-1)(y-2)  (K=Q real: D=1, rho=1, C3=n)")
    print("=" * 78)

    # ---- 1. reduction by direct algebra ------------------------------------
    ok, cx2, cy3, lhs, rhs = binomial_reduction_identity()
    print("\n[1] Direct algebra: 6*(C(x,2)-C(y,3)) expanded == 3x(x-1)-y(y-1)(y-2)?")
    print(f"    C(x,2) = {cx2}")
    print(f"    C(y,3) = {cy3}")
    print(f"    6C(x,2)-6C(y,3) = {lhs}")
    print(f"    3x(x-1)-y(y-1)(y-2) = {rhs}")
    from sympy import expand, symbols
    _x, _y = symbols("x y")
    ok1 = expand(6 * cx2) == expand(3 * _x * (_x - 1))
    ok2 = expand(6 * cy3) == expand(_y * (_y - 1) * (_y - 2))
    print(f"    6*C(x,2) == 3x(x-1): {ok1},  6*C(y,3) == y(y-1)(y-2): {ok2}")
    print(f"    identity holds: {ok}   (multiplying by 6, C(x,2)=C(y,3) iff 3x(x-1)=y(y-1)(y-2))")

    # ---- 2. exact solutions: two-sided products, factors, Lambda=0 ---------
    print("\n[2] Concrete solutions: P = 3x(x-1), Q = y(y-1)(y-2), a = C(x,2) = C(y,3)")
    all_sol_primes = set()
    for (x, y) in SOLUTIONS:
        from sympy import binomial
        a = binomial(x, 2)
        assert binomial(y, 3) == a, (x, y, a)
        P, Q, fP, fQ = two_sided_products(x, y)
        assert P == Q and fP == fQ, (x, y)
        primes, bs, L = linear_form(fP, fQ)
        all_sol_primes |= set(fP)
        print(f"    C({x},2)=C({y},3)={a}:  P=Q={P};  factors={fP}")
        print(f"       linear form over union of primes: n_nonzero={len(primes)}, bs={bs}, "
              f"Lambda = {L!r} (==0 exactly because P==Q and both sides have identical factorizations)")
        print(f"       exact check Lambda==0: {L == 0.0}")

    # ---- 3. Kummer condition for the solution primes ------------------------
    print("\n[3] Kummer condition (1.5) for the primes of the three solutions,")
    print("    K=Q, alpha_j = distinct primes:")
    okk, det = kummer_subset_verification(sorted(all_sol_primes))
    print(f"    primes = {sorted(all_sol_primes)}")
    print(f"    {det}")
    print(f"    ok = {okk}")

    # ---- 4. nonzero DELTA forms (real content of Thm 2.2) -------------------
    print("\n[4] Nonzero delta forms: Lambda = ln(P_a) - ln(Q_b) for pairs of DIFFERENT")
    print("    solutions (a != b).  These have Lambda != 0, so Thm 2.2 genuinely applies.")
    pairs = [((16, 10), (56, 22)), ((16, 10), (120, 36)), ((56, 22), (120, 36)), ((120, 36), (16, 10))]
    results = []
    for (x1, y1), (x2, y2) in pairs:
        from sympy import binomial
        P1, Q1, fP1, fQ1 = two_sided_products(x1, y1)
        P2, Q2, fP2, fQ2 = two_sided_products(x2, y2)
        a1, a2 = binomial(x1, 2), binomial(x2, 2)
        # form: b_j = v_{p}(P1) - v_{p}(Q2)   => Lambda = ln(P1/Q2)
        primes, bs, L = linear_form(fP1, fQ2)
        # direct float cross-check: ln(P1) - ln(Q2)
        Ldirect = math.log(P1) - math.log(Q2)
        agree = abs(L - Ldirect) < 1e-12 * max(1.0, abs(Ldirect))
        assert bs and bs[-1] != 0
        print(f"    a1={a1} (x={x1}), a2={a2} (y={y2}):  P1={P1}, Q2={Q2}")
        print(f"       Lambda = {' + '.join(f'({b})ln {p}' for p, b in zip(primes, bs))}"
              f"  = ln({P1}/{Q2}) = ln({math.prod(p**b for p, b in zip(primes, bs))})  approx {L:.10f}")
        print(f"       cross-check ln(P1)-ln(Q2) = {Ldirect:.10f}, agree={agree}")
        okk2, det2 = kummer_subset_verification(primes)
        print(f"       Kummer condition on these {len(primes)} primes: {det2}, ok={okk2}")
        results.append((primes, bs, L, math.log(abs(L)) if L != 0 else None))

    # ---- 5. Thm 2.2 constants for the nonzero delta forms -------------------
    print("\n[5] Matveev Thm 2.2 constants for the nonzero delta forms")
    print("    (theta = 1: Thm 2.2;  theta = 1/(2-2/(n e^{n+1})): Thm 2.3(ii), K=Q, A_j=ln alpha_j)")
    for (x1, y1), (x2, y2) in pairs:
        from sympy import binomial
        P1, _, fP1, _ = two_sided_products(x1, y1)
        _, Q2, _, fQ2 = two_sided_products(x2, y2)
        a1, a2 = binomial(x1, 2), binomial(x2, 2)
        primes, bs, L = linear_form(fP1, fQ2)
        tab = "    | {:<26} {:>16} {:>16} {:>16} {:>16}"
        print(f"\n    --- delta form ln(P({x1},2)) - ln(Q({y2},3)) = ln({a1}/{a2}), "
              f"n = {len(primes)}, primes {primes}, bs {bs}")
        for theta_tag, theta in (("Thm2.2 theta=1", 1.0),
                                 ("Thm2.3(ii) theta", 1.0 / (2.0 - 2.0 / (len(primes) * math.e ** (len(primes) + 1))))):
            c = matveev_constants(primes, bs, theta=theta, Eval=1.0)
            c["theta"], c["E"] = theta, 1.0
            checks = theorem_conditions_check(c)
            okc = all(o for _, _, o in checks)
            print(f"    {theta_tag} = {theta!r}:  C1={c['C1']:.6e}  C2={c['C2']:.6e}  C3={c['C3']:.6f}  D={c['D']}  rho={c['rho']}")
            print(f"       A_j (ln p_j) = {['%.6f' % a for a in c['A']]},  Omega=prod A_j = {c['Omega']:.6e}")
            print(f"       omega (2.5) = {c['omega']:.6e}")
            print(f"       C0' = ln(C2*D*omega/(C1*A_n)) (2.15) = {c['C0prime']:.6f}")
            print(f"       B = max|b_j|A_j/A_n (2.14) = {c['B']:.6f}")
            print(f"       (2.16) ln|Lambda| > {c['exponent']:.6e}   i.e.  |Lambda| > 10^({c['log10_bound']:.6e})")
            # task-form line: same exponent with Omega in place of omega (2.5)
            exp_Omega = -112 * 2 ** c["n"] * c["C2"] * c["C0prime"] * c["D"] ** 2 * c["Omega"] * math.log(2 * math.e * c["B"])
            print(f"       [task line] -112*2^n*C2*C0'*D^2*Omega*ln(2eB) = {exp_Omega:.6e}  "
                  f"(uses Omega=prod A_j instead of omega; omega {c['omega']:.1e} is the theorem's (2.5) quantity)")
            print(f"       actual |Lambda| = {abs(L):.10f} (known: the bound is satisfied a fortiori)")
            print(f"       hypotheses (2.9)-(2.11) with C0=1.23*C0', W0=ln(2eB): "
                  f"{'ALL PASS' if okc else 'SOME FAIL'}")
            for lab, v, o in checks:
                if not o:
                    print(f"         FAIL {lab}: {v:.6e}")
            results.append(("constants", theta_tag, c))

    # ---- 6. generic routine: constants from n = #distinct primes of a -----
    print("\n[6] Generic routine: given n = number of distinct primes of a, compute the full")
    print("    constant set.  Representative nonzero coefficient vector b_j = 1 for all j")
    print("    (Lambda = sum ln p_j = ln a != 0; the true Lambda of an exact solution is")
    print("    identically zero and Thm 2.2 does not apply to it -- see [2]).")
    from sympy import factorint, primefactors
    for a in A_VALUES:
        pf = sorted(primefactors(a))
        n = len(pf)
        bs_gen = [1] * n
        c = matveev_constants(pf, bs_gen, theta=1.0, Eval=1.0)
        c["theta"], c["E"] = 1.0, 1.0
        checks = theorem_conditions_check(c)
        okc = all(o for _, _, o in checks)
        print(f"\n    a = {a}:  n = {n} distinct primes {pf}")
        print(f"       C1={c['C1']:.6e}  C2={c['C2']:.6e}  C3={c['C3']:.6f}  D={c['D']}  rho={c['rho']}")
        print(f"       A_j = {['%.6f' % a_ for a_ in c['A']]},  Omega = {c['Omega']:.6e},  omega = {c['omega']:.6e}")
        print(f"       C0' = {c['C0prime']:.6f}   (needs >= 2n = {2 * n} for the theorem's use; see §13)")
        print(f"       B = {c['B']:.6f}")
        print(f"       (2.16) ln|Lambda| > {c['exponent']:.6e}  i.e. |Lambda| > 10^({c['log10_bound']:.6e})")
        exp_Omega = -112 * 2 ** c["n"] * c["C2"] * c["C0prime"] * c["D"] ** 2 * c["Omega"] * math.log(2 * math.e * c["B"])
        print(f"       [task line] -112*2^n*C2*C0'*D^2*Omega*ln(2eB) = {exp_Omega:.6e}")
        print(f"       actual |Lambda| = ln a = {math.log(a):.10e}")
        print(f"       hypotheses (2.9)-(2.11): {'ALL PASS' if okc else 'SOME FAIL'}")
        for lab, v, o in checks:
            if not o:
                print(f"         FAIL {lab}: {v:.6e}")
        c23 = matveev_constants(pf, bs_gen, theta=1.0 / (2.0 - 2.0 / (n * math.e ** (n + 1))), Eval=1.0)
        print(f"       Thm 2.3(ii) theta=1/(2-2/(n e^(n+1))): "
              f"C0'={c23['C0prime']:.6f}, omega={c23['omega']:.6e}, "
              f"ln|Lambda| > {c23['exponent']:.6e} (10^({c23['log10_bound']:.6e}))")

    # ---- 7. summary statement ----------------------------------------------
    print("\n" + "=" * 78)
    print("STATUS: this is Matveev's Theorem 2.2 with K = Q.")
    print("  D = D_K/kappa = 1 (Q subset R, kappa = 1);  rho = rank_R{ln p_j} = 1;")
    print("  C3 = n/rho = n;  A_j = h(p_j) = ln p_j (positive integers, Thm 2.3(ii) applies).")
    print("  The Kummer condition (1.5) is required by the theorem and is AUTOMATIC for")
    print("  distinct primes: [Q(sqrt(p1),...,sqrt(pn)):Q] = 2^n because no nonempty")
    print("  subset product is a perfect square (verified exactly above).")
    print("  For exact solutions C(x,2)=C(y,3)=a the linear form Lambda = ln P - ln Q is")
    print("  IDENTICALLY zero (n=0 nonzero terms): an equality of two factorizations is")
    print("  not an object Thm 2.2 constrains.  The theorem applies to NEAR-misses")
    print("  (unequal products), where it yields the printed explicit lower bounds.")
    print("=" * 78)


if __name__ == "__main__":
    main()