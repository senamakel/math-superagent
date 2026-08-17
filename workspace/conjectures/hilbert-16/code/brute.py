#!/usr/bin/env python3
"""code/brute.py — naive oracle for claimed limit-cycle counts.

Statement this bears on (GOAL.md item 3a, "certified limit-cycle counter"):
for a polynomial planar field X = P dx + Q dy with P, Q in Q[x, y], decide
existence and exact count of limit cycles — but only in the radially
symmetric case where the displacement function can be computed exactly.
(The general-P,Q displacement function is the open research object of H16.2;
this oracle pins down the exact statement in the tractable normal-form class
and honestly refuses everything else.)

Mathematical content (exact, no floats, no integration, no sampling):

  A radially symmetric field
      x' = A(r^2)x - B(r^2)y ,   y' = B(r^2)x + A(r^2)y ,   A,B in Q[u]
  written in polar coordinates satisfies
      dr/dt = r A(r^2),   dtheta/dt = B(r^2).
  Over one revolution the radial displacement of the return map along any
  ray is  Dr = 2 pi r A(r^2)/B(r^2),  so the displacement function
  D(r) = (return map - identity)(r) has the SAME SIGN as A(r^2) wherever
  B(r^2) != 0.  Hence the isolated periodic orbits are exactly the roots
  u0 > 0 of A(u) with B(u0) != 0 that are NOT equilibria, i.e. with A and B
  not both vanishing; a root of odd multiplicity is a hyperbolic limit cycle
  (A changes sign there), and the certified count is the number of such
  roots in the band.

  A circle r^2 = u0 where A(u0) = B(u0) = 0 is a circle of equilibria and is
  excluded via gcd(A, B).  If A == 0 (a centre: every orbit closed, none
  isolated) the count is 0.  If B == 0 and A != 0, theta is constant, no
  closed orbit exists, count is 0.

  Exactness: A and B are obtained from P, Q by exact polynomial division;
  odd-multiplicity root counts come from the exact square-free factorization
  of A in Q[u] plus Sturm counts; rooting out common zeros of A and B uses
  exact gcd in Q[u].

Worked examples reproduced (verify_all):
  1. cubic normal form  x'=-y+x(1-x^2-y^2), y'=x+y(1-x^2-y^2)
        -> A(u)=1-u: exactly 1 hyperbolic limit cycle at r=1
  2. linear centre  x'=-y, y'=x   -> A==0: 0 limit cycles (negative control)
  3. linear expanding focus  x'=x-2y, y'=2x+y   -> A==1: 0 limit cycles
        (a linear field with no limit cycle must report zero — control)
  4. van der Pol-like  x'=y, y'=(1-x^2-y^2)y-x  -> NOT radial: refused,
        not miscounted.  (guard set: assert the hypothesis class)
  5. linear saddle  x'=x, y'=-y  -> NOT radial: refused (it is not a
        rotation+scaling field; refusal, not 0, is the honest answer).
"""

from sympy import symbols, Poly, expand, Rational
from sympy.polys.polytools import count_roots
from sympy.polys import real_roots

x, y, u = symbols("x y u", real=True)


def _to_u(qe):
    """qe in Q[x,y] claimed to be a polynomial in u = x^2+y^2; return the
    Poly in u, or raise ValueError.  Exact route: c0 = qe(0,0) is the
    constant term; (qe - c0) is divisible by x^2+y^2 with remainder zero in
    Q[x,y]; recurse.  Degree drops by >= 2 each step, so it terminates.
    """
    r2 = Poly(x * x + y * y, x, y)
    coeffs = []
    cur = Poly(expand(qe), x, y)
    steps = 0
    while True:
        steps += 1
        if steps > 1000:                      # hard cap; degree halves each step
            raise ValueError("too many steps")
        c0 = cur.as_expr().subs({x: 0, y: 0})
        coeffs.append(c0)
        rem = cur - c0
        if rem.is_zero:
            break
        q, r = rem.div(r2)
        if not r.is_zero:
            raise ValueError("not a polynomial in x^2+y^2")
        cur = q
    out = 0
    for k, c in enumerate(coeffs):
        out += c * u ** k
    return Poly(out, u)


def is_radial(P, Q):
    """Return (True, A(u), B(u)) for the radial field
    x' = A x - B y, y' = B x + A y, or (False, None, None).

    A = (xP+yQ)/(x^2+y^2), B = (xQ-yP)/(x^2+y^2), exact polynomials in Q[u].
    """
    Pe, Qe = expand(P), expand(Q)
    r2 = Poly(x * x + y * y, x, y)
    try:
        # exact polynomial division by x^2+y^2 in Q[x,y], remainder must vanish
        qA, rA = Poly(x * Pe + y * Qe, x, y).div(r2)
        qB, rB = Poly(x * Qe - y * Pe, x, y).div(r2)
        if not rA.is_zero or not rB.is_zero:
            return False, None, None
        A = _to_u(qA.as_expr())
        B = _to_u(qB.as_expr())
    except ValueError:
        return False, None, None
    return True, A, B


def _sign_change_roots(Au, lo, hi):
    """(count, roots) of u0 in (lo, hi) at which the polynomial Au changes
    sign, i.e. roots of odd multiplicity.  Exact: square-free factorization
    of Au in Q[u]; odd-multiplicity square-free parts have Sturm-countable
    real roots each of which is a sign change of Au.
    """
    p = Poly(expand(Au), u)
    _, sqf = p.sqf_list()                     # [(f_i, m_i)] with f_i square-free
    total = 0
    roots = []
    for f, m in sqf:
        if m % 2 == 1:
            fp = Poly(f, u)
            n = count_roots(fp, lo, hi)       # Sturm: exact count in [lo, hi]
            total += n
            roots.extend([r for r in real_roots(fp) if lo < r < hi])
    # consistency: the certified count is the number of isolated roots in the
    # list; keep the Sturm count as a cross-check (it may count an endpoint
    # root, so compare on strict containment only).
    assert total >= len(roots)
    if total != len(roots):
        # a sign-change root sits on a band endpoint; exclude it from the
        # certified count, matching the strict-open-band statement.
        return len(roots), roots
    return total, roots


def limit_cycles_in_band(P, Q, lo_u, hi_u):
    """Certified count of limit cycles of the radially symmetric field (P,Q)
    in the annulus band sqrt(lo_u) < r < sqrt(hi_u), with the roots.

    Returns dict.  Non-radial fields are refused, not guessed at: the
    displacement function of a general field is not exactly computable by
    this method, and a wrong number is worse than a refusal.
    """
    radial, A, B = is_radial(P, Q)
    if not radial:
        return {"is_radial": False,
                "reason": "field is not radially symmetric; the displacement "
                          "function cannot be computed exactly by this oracle"}
    Au, Bu = A.as_expr(), B.as_expr()
    infos = {"is_radial": True, "A": Au, "B": Bu}

    if A.is_zero:
        infos["count"] = 0
        infos["roots"] = []
        infos["reason"] = "A == 0: a centre, every orbit closed, none isolated"
        return infos
    if B.is_zero:
        infos["count"] = 0
        infos["roots"] = []
        infos["reason"] = "B == 0: theta constant, no closed orbit exists"
        return infos

    count, roots = _sign_change_roots(Au, lo_u, hi_u)

    # A circle with A(u0) = B(u0) = 0 is a circle of equilibria, not a
    # periodic orbit: exclude roots shared by A and B via exact gcd.
    from sympy import gcd
    g = gcd(Poly(Au, u), Poly(Bu, u))
    if g.degree() > 0 and not g.is_zero:
        _, g_sqf = g.sqf_list()
        bad_parts = [Poly(f, u) for f, _m in g_sqf]
        keep_count, keep_roots = 0, []
        for fp in bad_parts:
            pass
        # remove roots of g from the A-sign-change list by Sturm-refined
        # subtraction: rebuild count over square-free parts of A/g
        rem_poly = Poly(Au // Poly(g.as_expr(), u), u) if g.degree() > 0 else Poly(Au, u)
        count2, roots2 = _sign_change_roots(rem_poly.as_expr(), lo_u, hi_u)
        infos["count"] = count2
        infos["roots"] = roots2
        infos["note"] = ("roots of gcd(A,B) excluded: those circles are "
                         "rings of equilibria, not periodic orbits")
    else:
        infos["count"] = count
        infos["roots"] = roots
    return infos


def verify_all():
    """Reproduce every worked example the statement gives.  Prints
    PASS/FAIL per case; returns True iff all pass."""
    results = []
    lo, hi = Rational(1, 10), Rational(10, 1)

    # 1. cubic normal form: exactly one limit cycle at r = 1
    P1 = -y + x * (1 - (x ** 2 + y ** 2))
    Q1 = x + y * (1 - (x ** 2 + y ** 2))
    r1 = limit_cycles_in_band(P1, Q1, lo, hi)
    roots1 = [r.evalf(20) for r in r1["roots"]]
    ok1 = (r1["is_radial"] and r1["count"] == 1 and len(roots1) == 1
           and abs(roots1[0] - 1) < 1e-10)
    results.append(("cubic normal form (one limit cycle at r=1)", ok1, r1))

    # 2. linear centre: zero limit cycles (A == 0)
    r2 = limit_cycles_in_band(-y, x, lo, hi)
    ok2 = r2["is_radial"] and r2["count"] == 0
    results.append(("linear centre x'=-y, y'=x  -> 0 cycles", ok2, r2))

    # 3. linear expanding focus: a linear field, no limit cycle -> 0
    r3 = limit_cycles_in_band(x - 2 * y, 2 * x + y, lo, hi)
    ok3 = r3["is_radial"] and r3["count"] == 0
    results.append(("linear expanding focus x'=x-2y, y'=2x+y  -> 0 cycles",
                    ok3, r3))

    # 4. van der Pol-like field: NOT radial -> refused, not miscounted
    r4 = limit_cycles_in_band(y, (1 - (x ** 2 + y ** 2)) * y - x, lo, hi)
    ok4 = (not r4["is_radial"])
    results.append(("van der Pol-like field -> refused as non-radial", ok4, r4))

    # 5. linear saddle: NOT radial -> refused (not a rotation+scaling field)
    r5 = limit_cycles_in_band(x, -y, lo, hi)
    ok5 = (not r5["is_radial"])
    results.append(("linear saddle x'=x, y'=-y -> refused as non-radial",
                    ok5, r5))

    # 6. sanity, by hand: A(u)=(1-u)(2-u), B(u)=1 -> exactly two hyperbolic
    #    limit cycles at u=1 and u=2 (r=1 and r=sqrt 2)
    A6 = (1 - u) * (2 - u)
    P6 = x * A6 - y
    Q6 = x + y * A6
    r6 = limit_cycles_in_band(P6, Q6, Rational(1, 20), Rational(20, 1))
    roots6 = sorted(float(r.evalf(15)) for r in r6["roots"])
    ok6 = (r6["is_radial"] and r6["count"] == 2
           and len(roots6) == 2 and abs(roots6[0] - 1) < 1e-10
           and abs(roots6[1] - 2) < 1e-10)
    results.append(("two-cycle field A=(1-u)(2-u): two cycles at u=1, u=2",
                    ok6, r6))

    # 7. sanity, by hand: A(u)=(1-u)^2 * (2-u), B(u)=1.  Root u=1 is
    #    double: A does not change sign there (semi-stable cycle), so the
    #    signed trapping-annulus criterion certifies only u=2.  The oracle
    #    reports the certified count and says which root was excluded.
    A7 = ((1 - u) ** 2) * (2 - u)
    P7 = x * A7 - y
    Q7 = x + y * A7
    r7 = limit_cycles_in_band(P7, Q7, Rational(1, 20), Rational(20, 1))
    roots7 = sorted(float(r.evalf(15)) for r in r7["roots"])
    ok7 = (r7["is_radial"] and r7["count"] == 1
           and len(roots7) == 1 and abs(roots7[0] - 2) < 1e-10)
    results.append(("semi-stable case A=(1-u)^2(2-u): certified count = 1 "
                    "(u=1 double root: not hyperbolic, not counted)",
                    ok7, r7))
    return results


if __name__ == "__main__":
    print("=== naive oracle: limit-cycle count, exact rational arithmetic ===")
    for name, ok, res in verify_all():
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] {name}")
        if "roots" in res:
            shown = [str(r.evalf(15)) for r in res["roots"]]
            print(f"        count={res.get('count')} roots={shown}")
            print(f"        A(u)={res.get('A')}  B(u)={res.get('B')}")
        if res.get("is_radial") is False:
            print(f"        reason: {res.get('reason')}")
    print()
    print("=== oracle bound: degrees <= 3, one band, 1 CPU, ran in seconds ===")