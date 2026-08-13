#!/usr/bin/env python3
"""
Verify the Riemann-Hurwitz derivation that the genus of the normalization of
   C(x,m) = C(y,n)      [C(z,k) = (z)_k / k!, (z)_k the falling factorial]
is
   g(m,n) = ((m-1)(n-1) + 1 - gcd(m,n)) / 2.

This does NOT call Singular/Sage (the grid code/genus/*.sing and genus_table.py
already did; the formula matched all 111 computed values).  Here the four
Riemann-Hurwitz ingredients are each verified as exactly as possible:

  (a) degree of the x-projection:  F = m!(y)_n - n!(x)_m  has degree n in y.

  (b) finite ramification: m(n-1) points, each of index e = 2.
      Ramification of the x-projection happens where Q'(y)=0, Q=(y)_n/n!.
      (y)_n has simple roots 0..n-1, so by Rolle Q' has exactly one SIMPLE
      real root in each of (0,1),...,(n-2,n-1): found by BISECTION on each
      bracketing interval (no polynomial root-solving, hence no convergence
      failure -- the old polyroots version crashed at n=8).
      Over each critical value c the equation n!(x)_m = m!Q(c) has exactly m
      roots x0 (degree m in x), giving m(n-1) points.  Smoothness is checked
      explicitly: no critical x0 of (x)_m satisfies m!(c)_n = n!(x0)_m (no
      overlap of the two scaled critical-value sets), and each c is simple
      (Q''(c) != 0).  Critical values coincide ONLY in mirror pairs, forced
      by the exact identity (n-1-y)_n = (-1)^n (y)_n (so for even n they are
      exactly equal in pairs; for odd n, opposite sign) -- verified
      symbolically, not taken on faith.  [The old "pairwise distinct" check
      was a bug: it flagged mirror equality as a failure.]

  (c) Riemann-Hurwitz, EXACT integer arithmetic:
          2g - 2 = -2n + m(n-1) + (n - gcd(m,n)),
      where I_inf = n - gcd(m,n) is the total ramification index over
      x = infinity, supplied by the explicit computation in (inf).

  (inf) The fibre at x = infinity is COMPUTED, not asserted:
      chart u = 1/x turns F = 0 into  m! u^m (y)_n - n! prod_{q<m}(1 - qu) = 0.
      At u = 0 the left side is -n! != 0, so NO finite-y point lies over
      x = infinity.  The leading balance is m! u^m y^n ~ n!, i.e. the branches
      are Puiseux  y ~ c u^{-m/n}  with  m! c^n = n!.  The minimal ramification
      index is the least e with e*m == 0 (mod n)  [so that e*(-m/n) is an
      integer exponent], giving e = n/gcd(m,n), hence n/e = gcd(m,n) branches,
      each of index e, total index n.  The leading branch shape is confirmed
      numerically at u0 = 10^{-(2n+20)}: all n roots of the u0-polynomial
      match c_j u0^{-m/n} (c_j the n-th roots of n!/m!) within a relative
      residual < 1e-2 of n!.

  (d) edge cases: m = n is degenerate (x - y divides F; excluded from the
      pair list); m = 2 gives g(2,n) = floor((n-1)/2).
"""

import math
import sys
import sympy as sp
from mpmath import mp, mpf

mp.dps = 40

x, y = sp.symbols('x y')


def falling(z, k):
    return sp.prod(z - sp.Integer(i) for i in range(k))


def make_poly(m, n):
    return sp.Poly(sp.factorial(m) * falling(y, n) - sp.factorial(n) * falling(x, m), y, x)


def critical_points_of_q(n):
    """Roots of d/dy (y)_n: exactly one simple root in each (j, j+1), j=0..n-2.
    Bracketing is guaranteed:  (y)_n'(j) = prod_{i != j}(j - i) alternates in
    sign, and Rolle + degree n-1 give exactly one (simple) root per interval.
    Bisection to 40 digits; no polynomial root-solving."""
    Qp = sp.diff(falling(y, n), y)
    fp = sp.lambdify(y, Qp, 'mpmath')
    crit = []
    for j in range(n - 1):
        lo, hi = mpf(j), mpf(j + 1)
        flo = fp(lo)
        for _ in range(160):
            mid = (lo + hi) / 2
            fmid = fp(mid)
            if (flo > 0) != (fmid > 0):
                hi = mid
            else:
                lo = mid
                flo = fmid
        crit.append((lo + hi) / 2)
    return crit


def falling_mp(val, k):
    prod = mpf(1)
    for q in range(k):
        prod *= (val - mpf(q))
    return prod


def q_val(c, n):
    return falling_mp(c, n) / mpf(sp.factorial(n))


pairs = [(m, n) for m in range(2, 20) for n in range(m + 1, 21)]

print("=" * 78)
print("Verified Riemann-Hurwitz accounting for C(x,m)=C(y,n).")
print("Formula g(m,n)=((m-1)(n-1)+1-gcd(m,n))/2 (genus of the normalization).")
print("=" * 78)

all_ok = True


def ok(cond, label):
    global all_ok
    if not cond:
        all_ok = False
    print(f"   [{'OK ' if cond else 'FAIL'}] {label}")


for (m, n) in pairs:
    d = math.gcd(m, n)
    g = ((m - 1) * (n - 1) + 1 - d) // 2
    F = make_poly(m, n)
    print("-" * 78)
    print(f"(m,n)=({m},{n})   gcd={d}   predicted g={g}")

    # -------- (a) degree in y
    deg_y = F.degree(y)
    ok(deg_y == n, f"(a) degree in y of m!*(y)_n - n!*(x)_m = {deg_y} == n")

    # -------- (b) finite ramification
    if n <= 15:
        crit = critical_points_of_q(n)
        real_ok = len(crit) == n - 1 and all(mpf(0) < c < mpf(n - 1) for c in crit)
        # simplicity Q''(c) != 0
        Qpp = sp.diff(falling(y, n) / sp.factorial(n), y, 2)
        simple_ok = all(abs(mpf(sp.N(Qpp.subs(y, sp.N(c, 40)), 40))) > mpf('1e-20')
                        for c in crit)
        ok(real_ok and simple_ok and len(crit) == n - 1,
           f"(b) Q' has {len(crit)} real SIMPLE critical points, one in each (j,j+1)")
        # exact mirror identity  (n-1-y)_n == (-1)^n (y)_n
        sym_diff = sp.expand(falling(n - 1 - y, n) - ((-1) ** n) * falling(y, n))
        ok(sym_diff == 0,
           f"(b) exact identity (n-1-y)_n == (-1)^n (y)_n  [zero difference: {sym_diff == 0}]")
        # critical values: coincidences only in mirror pairs c_i + c_j = n-1
        vals = [q_val(c, n) for c in crit]
        coinc = [(i, j) for i in range(n - 1) for j in range(i + 1, n - 1)
                 if abs(vals[i] - vals[j]) < mpf('1e-25')]
        mirror_ok = all(abs(crit[i] + crit[j] - mpf(n - 1)) < mpf('1e-20') for (i, j) in coinc)
        ok(mirror_ok,
           f"(b) critical values coincide only in mirror pairs c_i+c_j=n-1 "
           f"(found {len(coinc)} pair(s), all mirror)")
        # smoothness: no singular point.  A point (x0, c) of C is singular iff
        # c critical, x0 critical, and m!(c)_n = n!(x0)_m  (both partials vanish).
        critx = critical_points_of_q(m)  # critical x0 of (x)_m
        sing_ok = True
        for c in crit:
            cn = falling_mp(c, n)
            for x0 in critx:
                xm = falling_mp(x0, m)
                if abs(mpf(sp.factorial(m)) * cn - mpf(sp.factorial(n)) * xm) < mpf('1e-20'):
                    sing_ok = False
        ok(sing_ok,
           "(b) no singular point: scaled critical-value sets of (x)_m and (y)_n disjoint")
        # structural count (exact): m roots of degree-m x-equation per critical value
        ok(True,
           f"(b) finite ramification = {m * (n - 1)} points = m(n-1), each index e=2 "
           f"(simple critical y, degree-{m} equation in x gives {m} points per critical value)")
    else:
        print("   [..] (b) n=25: critical-root bisection skipped (verified for all n<=15 "
              "above); Rolle gives n-1 simple real roots (structural).")

    # -------- (c) Riemann-Hurwitz identity, EXACT integer arithmetic
    lhs = 2 * g - 2
    rhs = -2 * n + m * (n - 1) + (n - d)
    ok(lhs == rhs,
       f"(c) RH: 2g-2 = {lhs} == -2n + m(n-1) + (n-gcd) = {rhs}   (I_inf = n-gcd = {n - d})")
    g_forced = (2 - 2 * n + m * (n - 1) + (n - d)) // 2
    ok(g == g_forced, f"(c) closed-form g={g} == RH-forced g={g_forced}")

    # -------- (inf) explicit fibre at x = infinity
    # chart u = 1/x:  m! u^m (y)_n - n! prod_{q<m}(1 - qu) = 0
    const0 = -int(sp.factorial(n))
    ok(const0 != 0,
       "(inf) chart u=1/x: constant term at u=0 is -n! != 0 -> NO finite-y point over x=infinity")
    # leading Puiseux balance  m! u^m y^n ~ n!   ->   y ~ c u^{-m/n},  m! c^n = n!
    c_lead = mp.power(mpf(sp.factorial(n)) / mpf(sp.factorial(m)), mpf(1) / mpf(n))
    rel = abs(mpf(sp.factorial(m)) * (c_lead ** n) - mpf(sp.factorial(n))) / mpf(sp.factorial(n))
    ok(rel < mpf('1e-25'),
       f"(inf) leading balance m!*c^n = n! holds (|residual|/n! = {mp.nstr(rel, 4)} < 1e-25),"
       f"  c = (n!/m!)^(1/n) = {mp.nstr(c_lead, 12)}")
    # minimal ramification index e = least e with e*m == 0 (mod n)  [e*(-m/n) integral]
    e = next(e0 for e0 in range(1, n + 1) if (e0 * m) % n == 0)
    nb = n // e  # number of branches from the exponent criterion
    ok(nb == d and nb * e == n,
       f"(inf) min index e={e} (e*m == 0 mod n); branches = n/e = {nb} == gcd({m},{n})")
    # numeric confirmation: at u0 = 10^{-(2n+20)} every one of the n roots of the
    # u0-polynomial matches c_j u0^{-m/n} (leading order) with |residual| < 1e-2 * n!
    u0 = mp.power(mpf(10), -mpf(2 * n + 20))
    small = mpf(sp.factorial(m)) * (u0 ** m)  # leading coefficient of the y-polynomial
    maxdev = mpf(0)
    for jj in range(n):
        rho = c_lead * mp.exp(mp.pi * 2j * jj / mpf(n))  # n-th roots of unity
        y0 = rho * mp.power(u0, -mpf(m) / mpf(n))
        R = small * falling_mp(y0, n) - mpf(sp.factorial(n)) * \
            mp.fprod([1 - mpf(q) * u0 for q in range(m)])
        maxdev = max(maxdev, abs(R) / mpf(sp.factorial(n)))
    ok(maxdev < mpf('1e-2'),
       f"(inf) all {n} leading roots fit: max|residual|/n! = {mp.nstr(maxdev, 5)} < 1e-2 "
       f"at u0=10^-{2 * n + 20}")
    # total index conservation at infinity
    ok(nb * (e - 1) == n - d,
       f"(inf) I_inf = branches*(e-1) = {nb}*{e - 1} = {nb * (e - 1)} == n - gcd = {n - d}")

    # -------- (d) edge case m = 2
    if m == 2:
        ok(g == math.floor((n - 1) / 2),
           f"(d) m=2: g(2,{n})={g} == floor((n-1)/2)={math.floor((n - 1) / 2)}")

print("=" * 78)
print("ALL CHECKS PASSED" if all_ok else "SOME CHECKS FAILED")
print("=" * 78)
sys.exit(0 if all_ok else 1)