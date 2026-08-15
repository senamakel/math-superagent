#!/usr/bin/env python3
"""Complete Case-B closure of Catalan's equation via the Nagell-Ljunggren
theorem, made exact for this slice.

Case B of Catalan:  x^p - y^2 = 1  with p an odd prime (>= 3), x, y > 0.

Established in-workspace (machine-certified, claims exp2-case-B-reduction and
exp2-caseB-t-mod8-classification):
  * the reduction forces  x = c^2 + 1,  y = c*m,  m^2 = T(c,p), where
        T(c,p) = sum_{k=0}^{p-1} (c^2+1)^k = ((c^2+1)^p - 1) / (c^2).
  * T(c,p) mod 8 is a proven non-square for every (c,p) EXCEPT possibly
    c even AND p == 1 (mod 8).  The residual class is exactly
    {c even, p == 1 mod 8}.

This program completes that residual class (and redundantly all classes) by
applying the classical Nagell-Ljunggren theorem:
        (X^n - 1)/(X - 1) = Y^2  has, for n > 2, exactly the solutions
        (n, X, Y) = (4, 7, 20) and (5, 3, 11).
Nagell-Ljunggren is a classical PROVED theorem; it is NOT re-proved here.
What this program does is (a) state our slice and verify the slice cleanly
excludes both exceptions by exact assertions, (b) run an independent exact
oracle that T(c,p) is not a square over a real box, and (c) run an
independent small-box direct enumeration of (X^n-1)/(X-1) as a square to
confirm the two exceptions are the only ones in the relevant indices.

Our slice:  n = p an odd prime (>= 3),  X = c^2+1 >= 5 (odd), and for the
residual class c even => X = c^2+1 == 1 (mod 4).

Exclusion of the two Nagell-Ljunggren exceptions:
  * (n, X, Y) = (4, 7, 20):  n = 4 is EVEN, so it is excluded because our
    slice has n = p an odd prime.
  * (n, X, Y) = (5, 3, 11):  n = 5 is odd (in range), but X = 3 requires
    c^2 + 1 = 3, i.e. c^2 = 2, impossible for integer c.  Independently,
    X = 3 fails the congruence X == 1 (mod 4) that c even forces.
  * X = 7 (of the n=4 exception) also fails X == 1 (mod 4).

Every assertion is printed as an exact boolean check.

Exact integer arithmetic only — no floats anywhere.  isqrt from math is
exact on Python ints; T(c,p) is computed by the integer formula
((c^2+1)^p - 1) // (c^2) using pow for the p-th power.
"""
import math
import time
from concurrent.futures import ProcessPoolExecutor

# ---------------------------------------------------------------------------
# exact tools
# ---------------------------------------------------------------------------
def is_odd_prime(n):
    if n < 3 or n % 2 == 0:
        return False
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def T_exact(c, p):
    """T(c,p) = sum_{k=0}^{p-1} (c^2+1)^k = ((c^2+1)^p - 1) / c^2,
    computed over exact integers.  c >= 1, p >= 1."""
    x = c * c + 1
    return (pow(x, p) - 1) // (c * c)


def is_perfect_square(v):
    """Exact integer square test via isqrt (exact on Python ints)."""
    r = math.isqrt(v)
    return r * r == v


# ---------------------------------------------------------------------------
# point 3 worker: scan all even c for a single prime p
# ---------------------------------------------------------------------------
def _scan_prime(p, cmax):
    """Exact scan over even c in [2, cmax] for one odd prime p.
    Returns (p, count_scanned, n_squares, first_hit)."""
    n = 0
    bad = 0
    first = None
    for c in range(2, cmax + 1, 2):
        t = T_exact(c, p)
        n += 1
        if is_perfect_square(t):
            bad += 1
            if first is None:
                first = (c, t)
    return (p, n, bad, first)


# ---------------------------------------------------------------------------
# point 4 support: direct enumeration
# ---------------------------------------------------------------------------
def solve_NL(n, Xmax):
    """Directly enumerate X in [2, Xmax] and return the (X, Y) with
    Y^2 = (X^n - 1)/(X - 1).  Exact isqrt; n >= 2 allowed (n even too)."""
    sols = []
    for X in range(2, Xmax + 1):
        v = (pow(X, n) - 1) // (X - 1)
        if is_perfect_square(v):
            sols.append((X, math.isqrt(v)))
    return sols


def main():
    ok = True
    t_start = time.time()
    print("=" * 78)
    print("COMPLETE CASE-B CLOSURE via Nagell-Ljunggren, exact for the slice")
    print("=" * 78)

    # ------------------------------------------------------------------
    # Point 1: state the slice
    # ------------------------------------------------------------------
    print("\n[1] STATE OF THE SLICE")
    print("    Case B: x^p - y^2 = 1, p an odd prime (>=3).")
    print("    Reduction (machine-certified in-workspace): x = c^2+1,")
    print("    y = c*m, m^2 = T(c,p) = sum_{k=0}^{p-1} (c^2+1)^k.")
    print("    Nagell-Ljunggren slice: n = p (odd prime >= 3),")
    print("    X = c^2 + 1 (>= 5, odd), and for the residual class c even:")
    print("    X == 1 (mod 4).")
    print("    The whole Case-B obstruction is: is T(c,p) ever a square?")
    print("    mod-8 (proved) already eliminates every class except")
    print("    c even AND p == 1 (mod 8).")

    # ------------------------------------------------------------------
    # Point 2: verify the two Nagell-Ljunggren exceptions are excluded
    # ------------------------------------------------------------------
    print("\n[2] EXCEPTIONS OF NAGEL-LJUNGGREN, CHECKED EXACTLY")
    # classic theorem: (X^n-1)/(X-1) = Y^2, n>2 => (n,X,Y) = (4,7,20),(5,3,11)
    exc = [(4, 7, 20), (5, 3, 11)]
    for (n, X, Y) in exc:
        lhs = (pow(X, n) - 1) // (X - 1)
        assert lhs == Y * Y, (n, X, Y, lhs, Y * Y)
        print(f"    exception check (n={n}, X={X}, Y={Y}): "
              f"(X^n-1)/(X-1) == Y^2 -> {lhs == Y * Y}")

    # (4,7,20): n even => excluded since p is an odd prime
    n_even_excluded = (exc[0][0] % 2 == 0)
    print(f"    (4,7,20) has n=4 EVEN -> excluded (our n=p is an odd prime): {n_even_excluded}")

    # (5,3,11): X=3 requires c^2+1=3 i.e. c^2=2, impossible for integer c
    c2_impossible = all(c * c != 2 for c in range(0, 5))
    print(f"    (5,3,11) has X=3, requires c^2+1=3 i.e. c^2=2 (integer c): impossible = {c2_impossible}")

    # X=3 and X=7 fail the congruence X == 1 (mod 4) that c even forces
    X3_mod4 = (3 % 4 == 1)
    X7_mod4 = (7 % 4 == 1)
    print(f"    X=3 mod 4 == 1 (would be needed for c even)? {X3_mod4}  "
          f"-> so X=3 EXCLUDED by residue: {not X3_mod4}")
    print(f"    X=7 mod 4 == 1 (would be needed for c even)? {X7_mod4}  "
          f"-> so X=7 EXCLUDED by residue: {not X7_mod4}")

    ok = ok and n_even_excluded and c2_impossible and (not X3_mod4) and (not X7_mod4)

    # ------------------------------------------------------------------
    # Point 3: independent exact oracle over c even in [2,200000],
    #          odd primes p in [3,199]
    # ------------------------------------------------------------------
    print("\n[3] EXACT ORACLE: T(c,p) not a square, c even in [2,200000],")
    print("    odd primes p in [3,199] (independent of Nagell-Ljunggren)")
    primes = [p for p in range(3, 200) if is_odd_prime(p)]
    cmax = 200000
    n_c = cmax // 2   # even c: 2,4,...,200000 -> 100000 values
    print(f"    primes used (odd p in [3,199]): {primes}")
    print(f"    even c count: {n_c}; total pairs to test: {n_c * len(primes)}")

    t3 = time.time()
    # distribute over primes, one worker each
    with ProcessPoolExecutor(max_workers=max(1, min(28, len(primes)))) as ex:
        results = list(ex.map(_scan_prime, primes, [cmax] * len(primes)))
    t3 = time.time() - t3

    total_pairs = 0
    total_hits = 0
    for (p, n, bad, first) in results:
        total_pairs += n
        total_hits += bad
    print(f"    pairs tested exactly: {total_pairs}")
    print(f"    perfect squares found: {total_hits}   (expected 0)")
    print(f"    box runtime (parallel, {min(28, len(primes))} workers): {t3:.3f}s")
    if total_hits == 0:
        print("    RESULT: NO squares of T(c,p) in box -> consistent with")
        print("    Nagell-Ljunggren (0 squares in the residual and all classes).")
    else:
        print("    RESULT: squares found (would contradict Nagell-Ljunggren!)")
        for (p, n, bad, first) in results:
            if bad:
                print(f"      p={p}: first hit c={first[0]}, T={first[1]}")
    ok = ok and (total_hits == 0)

    # honesty note about what this box settles
    print("\n    NOTE: this box (c<=200000, p<=199) is a WIDER confirmation than")
    print("    the prior verify_bundle box (c<=1e5, p<=251) for the small-c side,")
    print("    and than the mod-8 box (c<=4000, p<=43).  It settles NOTHING new:")
    print("    it is a large-sample confirmation consistent with the classical")
    print("    theorem, not a proof.  (A smaller c but larger p range was already")
    print("    covered by verify_bundle; the true bound is far beyond any box.)")

    # ------------------------------------------------------------------
    # Point 4: direct enumeration of (X^n-1)/(X-1) as a square for
    #          n in {2,3,4,5}, X in [2, 10^6]
    # ------------------------------------------------------------------
    print("\n[4] DIRECT ENUMERATION: Y^2 = (X^n-1)/(X-1), n in {2,3,4,5},")
    print("    X in [2, 10^6]  (n even allowed here)")
    Xmax = 10 ** 6
    t4 = time.time()
    found_by_n = {}
    for n in (2, 3, 4, 5):
        sols = solve_NL(n, Xmax)
        found_by_n[n] = sols
        print(f"    n={n}: solutions (X,Y) with X in [2,{Xmax}]: {sols if sols else 'none'}")
    t4 = time.time() - t4
    print(f"    enumeration runtime: {t4:.3f}s")

    # confirm both exceptions are found
    has_4_7_20 = (4, 7, 20) in [(n, X, Y) for n in (2, 3, 4, 5)
                                for (X, Y) in found_by_n[n]]
    has_5_3_11 = (5, 3, 11) in [(n, X, Y) for n in (2, 3, 4, 5)
                                 for (X, Y) in found_by_n[n]]
    print(f"    both Nagell-Ljunggren exceptions found by enumeration: "
          f"(4,7,20)={has_4_7_20}, (5,3,11)={has_5_3_11}")
    ok = ok and has_4_7_20 and has_5_3_11

    # no OTHER solution in the odd indices n=3 and n=5 (relevant to our slice,
    # where n=p is an odd prime)
    extra_odd = []
    for n in (3, 5):
        for (X, Y) in found_by_n[n]:
            if (n, X, Y) != (5, 3, 11):
                extra_odd.append((n, X, Y))
    print(f"    odd-index solutions other than (5,3,11) (n in {{3,5}}): "
          f"{extra_odd if extra_odd else 'NONE'}")
    ok = ok and (len(extra_odd) == 0)

    # ------------------------------------------------------------------
    # Verdict section
    # ------------------------------------------------------------------
    print("\n" + "=" * 78)
    print("VERDICT")
    print("=" * 78)
    print("Step 1 (reduction x=c^2+1, y=c*m, m^2=T(c,p)): PROVED in-workspace")
    print("  (machine-certified, claim exp2-case-B-reduction).")
    print("Step 2 (mod-8 classification): PROVED in-workspace (claim")
    print("  exp2-caseB-t-mod8-classification); leaves only c even & p==1 mod 8.")
    print("Step 3 (all-class & residual non-squareness of T): ASSERTED by the")
    print("  classical Nagell-Ljunggren theorem (PROVED classically, NOT")
    print("  re-proved here); confirmed NUMERICALLY in-workspace to the box")
    print("  c<=200000 even, p<=199 (0 squares).")
    print("Step 4 (slice excludes both exceptions): PROVED by exact assertions")
    print("  here (n=4 even excluded; X=3 impossible as c^2=2; X=3,7 fail")
    print("  X==1 mod 4), confirmed by direct enumeration to X<=10^6.")
    print()
    print("  -- PROVED in this workspace:  reduction; mod-8 classification;")
    print("     exclusion of Nagell-Ljunggren exceptions from the slice;")
    print("     numerical agreement of the oracle over the stated box.")
    print("  -- ASSERTED CLASSICAL (not re-proved here): the Nagell-Ljunggren")
    print("     theorem itself, i.e. that (X^n-1)/(X-1)=Y^2 for n>2 has only")
    print("     the two solutions (4,7,20),(5,3,11).")
    print()
    print("Conclusion: within the Case-B slice, T(c,p) is never a perfect")
    print("square, so x^p - y^2 = 1 (p odd prime) has no solution.  The one")
    print("load-bearing classical fact is Nagell-Ljunggren.")
    total = time.time() - t_start
    print(f"\nTOTAL runtime: {total:.3f}s")
    print("RESULT:", "ALL CHECKS PASS" if ok else "FAILED")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
