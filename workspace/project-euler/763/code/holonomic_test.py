"""P-recursive (holonomic) extrapolation test for Project Euler 763 D(N).

Task:
  (2) Using the exact terms D(0..14), fit a P-recursive recurrence
      sum_j p_j(N) * D[N+j] = 0  with polynomial p_j of order m and degree d,
      exactly over the rationals using sympy.  For every fit with an exact
      nullspace, extrapolate the recurrence modulo 10^9 to compute
      D(20) mod 10^9 and D(100) mod 10^9, and compare to the known checks
      D(20)=9204559704  (=204559704 mod 10^9) and  D(100) last nine digits
      = 780166455.  Report which (m,d) reproduces BOTH checks and, for the
      best fit, D(10000) mod 10^9.

Extrapolation is done with exact rational (Fraction) arithmetic, so the
recurrence is not silently truncated.  If the fitted recurrence is correct
beyond the fitted window, every extrapolated D[N] comes out a whole integer
and (for the true recurrence) must reproduce D(20) and D(100).  For the
(overfitted) low-order recurrences we expect the extrapolation to break — that
is the point of the test.

D(N) growth ~3.4, so exact Fractions through N=100 (and even N=10000) are
cheap: big-integer arithmetic, thousands of steps, polynomial evaluation per
step.
"""

from fractions import Fraction

import sympy
from sympy import Matrix, Rational, symbols

from lib.holonomic import D_DEFAULT

MOD = 10 ** 9
D20_MOD_EXPECTED = 9204559704 % MOD   # 204559704
D100_MOD_EXPECTED = 780166455

D = [Rational(v) for v in D_DEFAULT]   # D(0..14) as exact rationals (integers)


def nullspace_for(m, d):
    """Exact-rational nullspace over D(0..14) for recurrence order m, poly degree d.

    Unknowns: a[j][t] for j=0..m, t=0..d  (coefficient of N^t in p_j).
    Equation per base index i=0..(len(D)-m-1):
        sum_{j,t} D[i+j] * i^t * a[j][t] = 0.
    Returns list of sympy vectors (each an independent solution).
    """
    ncols = (m + 1) * (d + 1)
    rows = len(D) - m
    A = Matrix.zeros(rows, ncols)
    for i in range(rows):
        col = 0
        for j in range(m + 1):
            v = D[i + j]
            for t in range(d + 1):
                A[i, col] = v * (i ** t)
                col += 1
    return A.nullspace()


def pj_as_lambda(vect, m, d):
    """Return list of functions p_j(N)->Fraction for this coefficient vector.

    subject to (m+1)*(d+1) coefficients a[j][t].
    """
    N = symbols('N')
    polys = []
    idx = 0
    for j in range(m + 1):
        expr = 0
        for t in range(d + 1):
            a = Rational(vect[idx])
            expr += a * N ** t
            idx += 1
        # closure over the polynomial value as a Fraction at integer N
        def pj_at(n, expr=expr):
            val = expr.subs(N, n)
            return Fraction(val.p, val.q)
        polys.append(pj_at)
    return polys


def extrapolate(m, d, pjlist, targets=(20, 100, 10000)):
    """Run the recurrence from seeds D(0..m-1) up to max(target), exactly.

    Returns (results, all_integer) where results = {N: Fraction(D[N])}.
    Raises on division-by-zero (p_m(N)==0) which would break the division.
    """
    maxN = max(targets)
    seq = [Fraction(0)] * (maxN + m + 1)
    for i in range(m):
        seq[i] = D[i]
    n = 0
    while n + m <= maxN:
        pm = pjlist[m](n)
        if pm == 0:
            return None, False
        s = Fraction(0)
        for j in range(m):
            s += pjlist[j](n) * seq[n + j]
        seq[n + m] = -s / pm
        n += 1
    all_int = all(seq[N].denominator == 1 for N in targets)
    return {N: seq[N] for N in targets}, all_int


def to_mod9(fr):
    """Return fraction reduced to a residue mod 10^9 (first 0..10^9-1) if integer."""
    if fr.denominator != 1:
        return None
    return fr.numerator % MOD


def main():
    print("=== P-recursive fit + extrapolation test (PE763) ===")
    print("D(0..14) =", [int(v) for v in D])
    print("Known checks: D(20) mod 10^9 =", D20_MOD_EXPECTED,
          " D(100) last nine =", D100_MOD_EXPECTED)
    print("-" * 78)

    best = None
    for m in range(2, 7):
        for d in range(0, 5):
            ns = nullspace_for(m, d)
            tag = f"(m={m},d={d})"
            if not ns:
                print(f"{tag}: nullspace empty (no exact fit) — skip")
                continue
            dim = len(ns)
            # try each independent solution; note dim>1 is underdetermined
            any_both = False
            for k, v in enumerate(ns):
                pj = pj_as_lambda(v, m, d)
                res, all_int = extrapolate(m, d, pj, (20, 100))
                if res is None:
                    print(f"{tag} sol{k}: division-by-zero during extrapolation")
                    continue
                d20 = to_mod9(res[20])
                d100 = to_mod9(res[100])
                ok20 = (d20 == D20_MOD_EXPECTED)
                ok100 = (d100 == D100_MOD_EXPECTED)
                both = ok20 and ok100
                if both:
                    any_both = True
                miss = ""
                if not ok20:
                    miss += f" D20={d20}!=204559704"
                if not ok100:
                    miss += f" D100={d100}!=780166455"
                print(f"{tag} sol{k}: dim={dim} integer_output={all_int}"
                      f" D20mod9={d20} D100mod9={d100}"
                      f"  {'BOTH MATCH' if both else 'no'}{miss}")
                if both:
                    best = (m, d, k, pj)
            if not any_both and dim == 1:
                print(f"{tag}: unique recurrence does NOT match both checks")
            elif not any_both:
                print(f"{tag}: dim={dim}>1 underdetermined; no basis solution "
                      "matches both checks")

    print("-" * 78)
    if best is None:
        print("RESULT: NO (m,d) recurrence fitted on D(0..14) reproduces BOTH "
              "the D(20) and D(100) checks -> P-recursive extrapolation to "
              "D(10000) is not viable from a low-order literal fit.")
    else:
        m, d, k, pj = best
        res, all_int = extrapolate(m, d, pj, (20, 100, 10000))
        d20 = to_mod9(res[20]); d100 = to_mod9(res[100])
        d10000 = to_mod9(res[10000])
        print(f"BEST fit (m={m},d={d},sol={k}):")
        print(f"  D(20)   mod 10^9 = {d20}  (expected {D20_MOD_EXPECTED})")
        print(f"  D(100)  mod 10^9 = {d100}  (expected {D100_MOD_EXPECTED})")
        print(f"  D(10000) mod 10^9 = {d10000}")


if __name__ == "__main__":
    main()
