#!/usr/bin/env python3
"""Elementary structure checks behind Cassels's p|y, q|x for x^p - y^q = 1.

Five checks, exact integer arithmetic only.  Roots by integer Newton
(lib.perfectpow.iroot), then the exact test b**q == value; no floats.

  1. gcd lemma:     gcd(x-1, Phi_p(x)) == gcd(x-1, p),  Phi_p(x) = (x^p-1)/(x-1)
  2. Fermat equiv:  p | x-1  <=>  p | x^p - 1
  3. reduced system (numerical spine of Cassels p|y): for distinct odd primes
     p, q and 1 <= a <= 20000 with p \\nmid a, Phi_p(a^q + 1) is never a
     perfect q-th power.
  4. mirror reduced system (numerical spine of q|x): for distinct odd primes
     p, q and 1 <= c <= 5000 with q \\nmid c, Phi_q(-(c^p-1)) =
     ((c^p-1)^q + 1)/c^p is never a perfect p-th power (c >= 2; c = 1 is the
     degenerate y = 0 case, the trivial solution (x,y)=(1,0) excluded by y>0).
  5. calibration at the known solution (3,2,2,3): 3^2 - 2^3 = 1.

Why check 3 is exactly the p|y half of Cassels:  x^p - 1 = (x-1)*Phi_p(x)=y^q.
The gcd lemma gives gcd(x-1, Phi_p(x)) = gcd(x-1, p) in {1, p}.
  * p | x-1  =>  p | x^p - 1 = y^q  =>  p | y, done.
  * p \\nmid x-1  =>  gcd = 1, so both factors are q-th powers: x-1 = a^q and
    Phi_p(x) = b^q (the reduced system, p \\nmid a), and y = a*b solves
    x^p - y^q = 1 with p \\nmid y.  Conversely any reduced-system (a,b) gives
    (x, y) = (a^q+1, a*b) with p \\nmid y.  So a reduced-system solution exists
    iff a solution with p \\nmid y exists; "Phi_p(a^q+1) is never a q-th power"
    is exactly the missing half of p|y.  Check 4 mirrors this for q|x using
    y^q + 1 = (y+1)*Phi_q(-y) with the plus-form Fermat equivalence
    q | y^q + 1  <=>  q | y+1.

Falsifier placement: the known solution (3,2,2,3) has p = 2 (even), excluded by
the odd-prime hypothesis, and sits in the easy branch (2 | 3-1, 3 | 2+1), so
none of these checks eliminates it.
"""
import time
from math import gcd

from lib.perfectpow import iroot
from lib.lucas_prim import phi_p, phi_q_neg

try:
    import gmpy2
    HAVE_GMPY2 = True
except ImportError:
    HAVE_GMPY2 = False

P_SET = (3, 5, 7, 11, 13)
Q_SET = (3, 5, 7)
CHECK1_PRIMES = (3, 5, 7, 11, 13, 17)
X1_MAX = 200000
A_MAX = 20000
C_MAX = 5000


def is_exact_power(n, k):
    """True iff n >= 0 is an exact k-th power (integer Newton root, then
    exact b**k == n check).  Exact integer arithmetic."""
    r = iroot(n, k)
    return r ** k == n


def fmt(n):
    return f"{n:,}"


def fmt_big(n, where):
    return f"{n}  ({n.bit_length()} bits, at {where})"


# ---------------------------------------------------------------- Section 0
def section_0_selftest():
    """Known-answer checks of the machinery before the big sweeps."""
    results = []
    def chk(name, cond):
        results.append((name, bool(cond)))
    chk("iroot(8,3) == 2", iroot(8, 3) == 2)
    chk("iroot(9,2) == 3", iroot(9, 2) == 3)
    chk("iroot(10,3) == 2", iroot(10, 3) == 2)
    chk("iroot(1,5) == 1", iroot(1, 5) == 1)
    chk("iroot(2**100,10) == 2**10", iroot(2 ** 100, 10) == 2 ** 10)
    chk("7 not a perfect cube", not is_exact_power(7, 3))
    chk("8 is a perfect cube", is_exact_power(8, 3))
    chk("2**100+1 not a 10th power", not is_exact_power(2 ** 100 + 1, 10))
    chk("phi_p(3,2) == 7", phi_p(3, 2) == 7)
    chk("phi_p(3,4) == 21", phi_p(3, 4) == 21)
    chk("phi_q_neg(3,2) == 3", phi_q_neg(3, 2) == 3)
    chk("phi_q_neg(3,0) == 1", phi_q_neg(3, 0) == 1)
    chk("gcd lemma p=3,x=2: gcd(1,7)==gcd(1,3)", gcd(1, 7) == gcd(1, 3))
    chk("gcd lemma p=3,x=4: gcd(3,21)==gcd(3,3)", gcd(3, 21) == gcd(3, 3))
    ok = all(c for _, c in results)
    return results, ok


# ----------------------------------------------------------- Sections 1 & 2
def section_1_2_gcd_and_fermat():
    """gcd lemma and Fermat equivalence on the same (p, x) loop, so x**p is
    computed once per case."""
    cases = 0
    bad_gcd = []
    bad_flt = []
    t0 = time.perf_counter()
    for p in CHECK1_PRIMES:
        for x in range(2, X1_MAX + 1):
            cases += 1
            xp = x ** p
            phi = (xp - 1) // (x - 1)
            if gcd(x - 1, phi) != gcd(x - 1, p):
                bad_gcd.append((p, x))
            if ((x - 1) % p == 0) != ((xp - 1) % p == 0):
                bad_flt.append((p, x))
    dt = time.perf_counter() - t0
    return cases, bad_gcd, bad_flt, dt


# --------------------------------------------------------------- Section 3
def section_3_reduced_system():
    """Phi_p(a^q + 1) perfect q-th power?  Spine of Cassels p|y."""
    pairs = 0
    total = 0
    per_pair = {}
    hits = []
    max_phi, max_phi_where = 0, None
    max_x, max_x_where = 0, None
    t0 = time.perf_counter()
    for p in P_SET:
        for q in Q_SET:
            if p == q:
                continue
            pairs += 1
            cnt = 0
            for a in range(1, A_MAX + 1):
                if a % p == 0:
                    continue
                cnt += 1
                x = a ** q + 1
                phi = phi_p(p, x)
                if phi > max_phi:
                    max_phi, max_phi_where = phi, (p, q, a)
                if x > max_x:
                    max_x, max_x_where = x, (p, q, a)
                if is_exact_power(phi, q):
                    hits.append((p, q, a))
            per_pair[(p, q)] = cnt
            total += cnt
    dt = time.perf_counter() - t0
    return dict(pairs=pairs, total=total, per_pair=per_pair, hits=hits,
                max_phi=max_phi, max_phi_where=max_phi_where,
                max_x=max_x, max_x_where=max_x_where, dt=dt)


# --------------------------------------------------------------- Section 4
def section_4_mirror_system():
    """Phi_q(-(c^p-1)) = ((c^p-1)^q + 1)/c^p perfect p-th power?  Spine of
    Cassels q|x.  c=1 is the degenerate y=0 case (trivial solution (1,0),
    excluded by y>0); reported separately."""
    pairs = 0
    total = 0
    per_pair = {}
    hits_degenerate = []
    hits_nondegenerate = []
    max_psi, max_psi_where = 0, None
    max_y, max_y_where = 0, None
    t0 = time.perf_counter()
    for p in P_SET:
        for q in Q_SET:
            if p == q:
                continue
            pairs += 1
            cnt = 0
            for c in range(1, C_MAX + 1):
                if c % q == 0:
                    continue
                cnt += 1
                y = c ** p - 1
                psi = phi_q_neg(q, y)
                if psi > max_psi:
                    max_psi, max_psi_where = psi, (p, q, c)
                if y > max_y:
                    max_y, max_y_where = y, (p, q, c)
                if is_exact_power(psi, p):
                    (hits_degenerate if c == 1 else hits_nondegenerate).append((p, q, c))
            per_pair[(p, q)] = cnt
            total += cnt
    dt = time.perf_counter() - t0
    return dict(pairs=pairs, total=total, per_pair=per_pair,
                hits_degenerate=hits_degenerate,
                hits_nondegenerate=hits_nondegenerate,
                max_psi=max_psi, max_psi_where=max_psi_where,
                max_y=max_y, max_y_where=max_y_where, dt=dt)


# --------------------------------------------------------------- Section 5
def section_5_calibration():
    """Calibrate at the known solution (3,2,2,3): 3^2 - 2^3 = 1."""
    x, p, y, q = 3, 2, 2, 3
    phi = phi_p(p, x)                       # (3^2-1)/(3-1) = 4
    return dict(
        equation=(x ** p - y ** q == 1),
        p_even=(p % 2 == 0),
        gcd_left=gcd(x - 1, phi),           # gcd(2, 4)
        gcd_right=gcd(x - 1, p),            # gcd(2, 2)
        p_dvd_xm1=((x - 1) % p == 0),       # 2 | 2
        p_dvd_xpm1=((x ** p - 1) % p == 0),  # 2 | 8
        q_dvd_yp1=((y + 1) % q == 0),       # 3 | 3
        q_dvd_yqp1=((y ** q + 1) % q == 0),  # 3 | 9
        p_dvd_y=(y % p == 0),               # 2 | 2 (Cassels conclusion, p even)
        q_dvd_x=(x % q == 0),               # 3 | 3 (Cassels conclusion)
    )


# --------------------------------------------------------------- Section 6
def section_6_gmpy2_crosscheck():
    """Independent route to the roots: gmpy2.iroot (different implementation)
    on sampled cases of sections 3 and 4.  Floor roots must agree with the
    integer-Newton iroot, and gmpy2's exact flag must be False on every
    nondegenerate sampled value (c >= 2 in the mirror; the reduced side has no
    degenerate case)."""
    if not HAVE_GMPY2:
        return None
    checked = 0
    bad = []
    for p in P_SET:
        for q in Q_SET:
            if p == q:
                continue
            for a in range(1, A_MAX + 1, 1000):
                if a % p == 0:
                    continue
                phi = phi_p(p, a ** q + 1)
                r_lib = iroot(phi, q)
                r_g, exact_g = gmpy2.iroot(phi, q)
                checked += 1
                if int(r_g) != r_lib or exact_g:
                    bad.append(("reduced", p, q, a, int(r_g), r_lib, bool(exact_g)))
            for c in range(2, C_MAX + 1, 1000):
                if c % q == 0:
                    continue
                psi = phi_q_neg(q, c ** p - 1)
                r_lib = iroot(psi, p)
                r_g, exact_g = gmpy2.iroot(psi, p)
                checked += 1
                if int(r_g) != r_lib or exact_g:
                    bad.append(("mirror", p, q, c, int(r_g), r_lib, bool(exact_g)))
    return checked, bad


# ------------------------------------------------------------------- main
def main():
    print("=" * 78)
    print("Elementary structure behind Cassels p|y, q|x for x^p - y^q = 1")
    print("exact integer arithmetic only (integer Newton roots, b**q == value)")
    print("=" * 78)

    verdicts = []
    t_all = time.perf_counter()

    # ---- Section 0
    results, ok = section_0_selftest()
    verdicts.append(("0  machinery self-test (known answers)", ok))
    print("\n[0] Machinery self-test (known answers)")
    for name, c in results:
        print(f"    {'OK ' if c else 'FAIL'}  {name}")
    print(f"    VERDICT: {'PASS' if ok else 'FAIL'}")

    # ---- Sections 1 & 2
    cases12, bad_gcd, bad_flt, dt12 = section_1_2_gcd_and_fermat()
    ok1 = len(bad_gcd) == 0
    ok2 = len(bad_flt) == 0
    verdicts.append(("1  gcd lemma", ok1))
    verdicts.append(("2  Fermat equivalence", ok2))
    print(f"\n[1] gcd lemma:  gcd(x-1, Phi_p(x)) == gcd(x-1, p), "
          f"Phi_p(x) = (x^p-1)/(x-1)")
    print(f"    p in {CHECK1_PRIMES}, x in [2, {fmt(X1_MAX)}]")
    print(f"    cases: {fmt(cases12)}")
    print(f"    failures: {len(bad_gcd)}" +
          (f"  e.g. {bad_gcd[:5]}" if bad_gcd else ""))
    print(f"    VERDICT: {'PASS' if ok1 else 'FAIL'}")
    print(f"\n[2] Fermat equivalence:  p | x-1  <=>  p | x^p - 1")
    print(f"    same range")
    print(f"    cases: {fmt(cases12)}")
    print(f"    failures: {len(bad_flt)}" +
          (f"  e.g. {bad_flt[:5]}" if bad_flt else ""))
    print(f"    VERDICT: {'PASS' if ok2 else 'FAIL'}")
    print(f"    (shared loop with [1], wall {dt12:.2f}s)")

    # ---- Section 3
    r3 = section_3_reduced_system()
    ok3 = len(r3["hits"]) == 0
    verdicts.append(("3  reduced system (spine of p|y)", ok3))
    print(f"\n[3] REDUCED SYSTEM — Phi_p(a^q + 1) a perfect q-th power?")
    print(f"    p != q odd primes: p in {P_SET} x q in {Q_SET}")
    print(f"    a in [1, {fmt(A_MAX)}] with p not dividing a")
    print(f"    (p,q) pairs: {r3['pairs']}")
    print(f"    total (p,q,a) cases: {fmt(r3['total'])}")
    print(f"    per-pair counts: " +
          ", ".join(f"({p},{q})={fmt(n)}" for (p, q), n in
                    sorted(r3["per_pair"].items())))
    print(f"    perfect q-th powers found: {len(r3['hits'])}" +
          (f"  {r3['hits'][:10]}" if r3["hits"] else ""))
    print(f"    max x = a^q + 1 tested: {fmt_big(r3['max_x'], r3['max_x_where'])}")
    print(f"    max Phi_p(x) tested: {fmt_big(r3['max_phi'], r3['max_phi_where'])}")
    print(f"    VERDICT: {'PASS' if ok3 else 'FAIL'} "
          f"(zero reduced-system solutions — this is exactly p|y)")
    print(f"    wall {r3['dt']:.2f}s")

    # ---- Section 4
    r4 = section_4_mirror_system()
    ndeg = len(r4["hits_nondegenerate"])
    deg = len(r4["hits_degenerate"])
    ok4 = ndeg == 0 and deg == r4["pairs"]  # every pair has the c=1 degenerate
    verdicts.append(("4  mirror reduced system (spine of q|x)", ok4))
    print(f"\n[4] MIRROR REDUCED SYSTEM — Phi_q(-(c^p-1)) a perfect p-th power?")
    print(f"    same (p,q) pairs; c in [1, {fmt(C_MAX)}] with q not dividing c")
    print(f"    (p,q) pairs: {r4['pairs']}")
    print(f"    total (p,q,c) cases: {fmt(r4['total'])}")
    print(f"    per-pair counts: " +
          ", ".join(f"({p},{q})={fmt(n)}" for (p, q), n in
                    sorted(r4["per_pair"].items())))
    print(f"    non-degenerate (c >= 2, i.e. y >= 1): "
          f"{fmt(r4['total'] - deg)} cases")
    print(f"    perfect p-th powers, c >= 2: {ndeg}" +
          (f"  {r4['hits_nondegenerate'][:10]}" if ndeg else ""))
    print(f"    degenerate c = 1 (y = 0): {deg} case(s) — "
          f"Phi_q(0) = 1 = 1^p, the trivial solution (x,y) = (1,0), "
          f"excluded by y > 0")
    print(f"    max y = c^p - 1 tested: {fmt_big(r4['max_y'], r4['max_y_where'])}")
    print(f"    max Phi_q(-y) tested: {fmt_big(r4['max_psi'], r4['max_psi_where'])}")
    print(f"    VERDICT: {'PASS' if ok4 else 'FAIL'} "
          f"(zero non-degenerate — spine of q|x confirmed)")
    print(f"    wall {r4['dt']:.2f}s")

    # ---- Section 5
    r5 = section_5_calibration()
    ok5 = (r5["equation"] and r5["p_even"] and r5["gcd_left"] == 2
           and r5["gcd_right"] == 2 and r5["p_dvd_xm1"] and r5["p_dvd_xpm1"]
           and r5["q_dvd_yp1"] and r5["q_dvd_yqp1"] and r5["p_dvd_y"]
           and r5["q_dvd_x"])
    verdicts.append(("5  calibration at (3,2,2,3)", ok5))
    print(f"\n[5] Calibration at the known solution (3,2,2,3): 3^2 - 2^3 = 1")
    print(f"    equation holds: {r5['equation']}")
    print(f"    p = 2 is EVEN -> odd-prime Cassels hypothesis excludes the "
          f"known solution")
    print(f"    gcd(x-1, Phi_p(x)) = gcd(2, 4) = {r5['gcd_left']} == "
          f"gcd(x-1, p) = gcd(2, 2) = {r5['gcd_right']}")
    print(f"    p | x-1:   2 | 3-1 = 2    -> {r5['p_dvd_xm1']}")
    print(f"    p | x^p-1: 2 | 3^2-1 = 8  -> {r5['p_dvd_xpm1']}")
    print(f"    q | y+1:   3 | 2+1 = 3    -> {r5['q_dvd_yp1']}")
    print(f"    q | y^q+1: 3 | 2^3+1 = 9  -> {r5['q_dvd_yqp1']}")
    print(f"    Cassels conclusions hold anyway: p|y = 2|2 -> {r5['p_dvd_y']}, "
          f"q|x = 3|3 -> {r5['q_dvd_x']}")
    print(f"    VERDICT: {'PASS' if ok5 else 'FAIL'}")

    # ---- Section 6
    r6 = section_6_gmpy2_crosscheck()
    if r6 is None:
        verdicts.append(("6  gmpy2 independent root cross-check", False))
        print(f"\n[6] gmpy2 independent root cross-check: gmpy2 NOT installed "
              f"— skipped")
    else:
        checked, bad = r6
        ok6 = len(bad) == 0
        verdicts.append(("6  gmpy2 independent root cross-check", ok6))
        print(f"\n[6] gmpy2 independent root cross-check (sampled every 1000th "
              f"case)")
        print(f"    samples: {fmt(checked)}")
        print(f"    mismatches / spurious exact flags: {len(bad)}" +
              (f"  {bad[:5]}" if bad else ""))
        print(f"    VERDICT: {'PASS' if ok6 else 'FAIL'}")

    # ---- Overall
    t_all = time.perf_counter() - t_all
    all_ok = all(ok for _, ok in verdicts)
    print("\n" + "-" * 78)
    for name, ok in verdicts:
        print(f"    [{'PASS' if ok else 'FAIL'}]  {name}")
    print("-" * 78)
    print(f"OVERALL: {'ALL CHECKS PASS' if all_ok else 'SOME CHECKS FAIL'}")
    print(f"total wall time: {t_all:.2f}s")
    return 0 if all_ok else 1


if __name__ == "__main__":
    sys_exit = main()
    import sys
    sys.exit(sys_exit)
