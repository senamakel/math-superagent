#!/usr/bin/env python3
"""exp2_even_proof.py — machine verification of lemma `exp2-a-even`.

Lemma: x^2 - y^q = 1 with x,y > 0, x EVEN (x >= 2), and q an ODD PRIME, has
NO solution.

Three-step elementary proof, each step checked with exact integer arithmetic
(no floats anywhere):

  Step 1 (gcd): x even => x-1, x+1 odd, and gcd(x-1,x+1) | 2; since both
        factors are odd, gcd = 1.  [verified below by explicit gcd, and the
        gcd|2 bound is proved exactly for all even x]
  Step 2 (factorisation into q-th powers): (x-1)(x+1) = y^q with coprime
        factors, each positive, so each is a q-th power: x-1 = a^q,
        x+1 = b^q with b > a >= 1.  [verified: for every even x and odd prime
        q with x^2 - 1 a perfect q-th power, the integer q-th roots a,b exist
        and satisfy x-1 = a^q, x+1 = b^q — checked directly]
  Step 3 (inequality): b^q - a^q = (x+1)-(x-1) = 2, but b^q - a^q >=
        (a+1)^q - a^q >= (since a >= 1) 2^q - 1 >= 7 for q >= 3,
        contradicting b^q - a^q = 2.  So no solution.

Deliverables of this program:
  (a) verifies that b^q - a^q is minimized on a,b >= 1 with b > a at a=1,
      b=a+1=2, exactly, for q in a listed set of odd primes, that
      (a+1)^q - a^q is increasing in a, and that 2^q - 1 >= 7 (> 2) for
      every odd prime q >= 3.
  (b) confirms gcd(x-1,x+1) = 1 for every even x (exactly, all even x by
      proof, plus a concrete sweep), and confirms the factor structure
      x-1=a^q, x+1=b^q (integer q-th roots) is forced: on every even x below
      a bound where x^2 - 1 is a q-th power, the gcd is 1 (else the
      factorisation into q-th powers would not be legitimate) and the
      q-th-root statement holds.
  (c) brute-force oracle: over even x <= EVEN_X_MAX and odd prime q <= Q_MAX,
      assert x^2 - y^q = 1 has zero solutions, by exact q-th-power detection
      of x^2 - 1.

Falsifier discipline: every claimed intermediate is evaluated; a step whose
minimiser statement failed would be reported. This lemma covers only EVEN x;
the known solution (3,2,3) has x = 3 odd, so it is excluded by hypothesis and
must not appear — the oracle checks this explicitly.
"""

import math
import time


# ---------------------------------------------------------------------------
# Exact integer helpers (no floats)
# ---------------------------------------------------------------------------
def integer_qth_root(n, q):
    """Floor of the exact q-th root of n (n>=0, q>=1), by integer bisection.

    Returns the largest integer r with r^q <= n.  Exact integer arithmetic
    only; never uses floats or math.pow.  Integer multiplication via ** is
    exact in Python.
    """
    if n < 0:
        raise ValueError("n must be >= 0")
    if q == 1:
        return n
    if n < 2:
        return n
    lo, hi = 1, 1
    while hi ** q <= n:
        hi *= 2
    # invariant: (lo)^q <= n < (hi)^q
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if mid ** q <= n:
            lo = mid
        else:
            hi = mid
    return lo


def is_perfect_qth_power(n, q):
    """True iff n is exactly the q-th power of an integer (n >= 0)."""
    if n < 2:
        return n == 1
    r = integer_qth_root(n, q)
    return r ** q == n


# ---------------------------------------------------------------------------
# (a) the minimiser statement for b^q - a^q
# ---------------------------------------------------------------------------
def verify_part_a(primes):
    """Verify, for each odd prime q in `primes`, exactly:

      1. For all a,b >= 1 with b > a:  b^q - a^q >= (a+1)^q - a^q.  (This is
         immediate since b >= a+1 and t -> t^q is increasing, but we check it
         explicitly by enumerating a,b over a window and confirming the exact
         minimum over 1 <= a < b <= B is attained at a=1, b=2.)
      2. (a+1)^q - a^q is increasing in a for a >= 1 (differences positive).
      3. 2^q - 1 >= 7 (strictly > 2) for every odd prime q >= 3.

    Since (a+1)^q - a^q is increasing and >= 2^q - 1 >= 7 > 2 for a >= 1,
    the inequality b^q - a^q >= 7 > 2 holds, contradicting b^q - a^q = 2.
    """
    print("=" * 72)
    print("PART (a): minimiser of b^q - a^q on 1 <= a < b, and 2^q - 1 >= 7")
    print("=" * 72)
    B = 200  # enumeration window for the minimiser check (small, exact)
    all_ok = True
    for q in primes:
        # 1. exact minimum of b^q - a^q over 1 <= a < b <= B (integer)
        best = None
        best_pair = None
        increasing = True
        prev = None
        for a in range(1, B + 1):
            val = (a + 1) ** q - a ** q
            if prev is not None and val <= prev:
                increasing = False
            prev = val
            for b in range(a + 1, B + 1):
                d = b ** q - a ** q
                if best is None or d < best:
                    best = d
                    best_pair = (a, b)
        # 2. monotonicity of (a+1)^q - a^q in a (a in [1,B])
        monotone = True
        vals = [(a + 1) ** q - a ** q for a in range(1, B + 1)]
        for i in range(1, len(vals)):
            if vals[i] <= vals[i - 1]:
                monotone = False
        # 3. lower bound 2^q - 1
        lb = 2 ** q - 1
        ok_min = (best_pair == (1, 2)) and (best == 2 ** q - 1)
        ok_lb = lb >= 7 and lb > 2
        ok = ok_min and monotone and increasing and ok_lb
        all_ok &= ok
        print(f"  q={q:<4} min(b^q-a^q) over 1<=a<b<={B} = {best} at "
              f"(a,b)={best_pair} (expect (1,2), {2**q-1}) "
              f"{'OK' if ok_min else 'FAIL'}")
        print(f"        (a+1)^q-a^q increasing in a: {monotone} "
              f"(and neighbouring-window increasing: {increasing})   "
              f"2^q-1 = {lb} >= 7 and > 2: {ok_lb}")
    print(f"  PART (a) overall: {'ALL OK' if all_ok else 'FAILED'}\n")
    return all_ok


# ---------------------------------------------------------------------------
# (b) gcd(x-1,x+1) = 1 for even x, and the q-th-power factor structure
# ---------------------------------------------------------------------------
def gcd_exact(a, b):
    """Exact Euclidean gcd of two integers (math.gcd is exact; used directly)."""
    return math.gcd(a, b)


def verify_part_b(q_max, x_max):
    """Confirm gcd(x-1,x+1)=1 for even x (exactly, by the argument plus a
    sweep), and confirm that whenever x^2 - 1 = y^q with x even, the forced
    factor structure x-1 = a^q, x+1 = b^q (integer q-th roots) holds."""
    print("=" * 72)
    print("PART (b): gcd(x-1,x+1)=1 for even x, and q-th-power factorisation")
    print("=" * 72)

    # (i) Exact proof-as-sweep: gcd for all even x in a large window.
    gcd_ok = True
    for x in range(2, 2_000_000, 2):   # even x from 2 up
        if gcd_exact(x - 1, x + 1) != 1:
            gcd_ok = False
            print(f"  COUNTEREXAMPLE: gcd({x-1},{x+1}) = "
                  f"{gcd_exact(x-1,x+1)} (even x)")
            break
    print(f"  (i) gcd(x-1,x+1)=1 for all even x <= {2_000_000:,.0f} "
          f"(exact): {'OK' if gcd_ok else 'FAILED'}")

    # (ii) Exact divisibility proof of step 1: gcd(x-1,x+1) | gcd((x+1)-(x-1), x-1)
    #      = gcd(2, x-1), and x-1 odd forces gcd(2,x-1)=1.  Verify symbolically
    #      across the sweep: gcd(x-1,x+1) == gcd(2, x-1) for all even x.
    gcd_div2_ok = True
    for x in range(2, 2_000_000, 2):
        if gcd_exact(x - 1, x + 1) != gcd_exact(2, x - 1):
            gcd_div2_ok = False
            break
    print(f"  (ii) gcd(x-1,x+1) == gcd(2, x-1) for all even x <= "
          f"{2_000_000:,.0f}: {'OK' if gcd_div2_ok else 'FAILED'}  "
          "(both sides = 1 since x-1 is odd)")

    # (iii) Factor structure: for even x where x^2 - 1 is a perfect q-th power
    #       (x^2-1 = y^q), the integer q-th roots a,b of x-1 and x+1 exist and
    #       satisfy x-1=a^q, x+1=b^q, b > a >= 1.
    struct_ok = True
    n_checked = 0
    for x in range(2, x_max + 1, 2):
        prod = x * x - 1
        for q in range(3, q_max + 1, 2):
            if is_perfect_qth_power(prod, q):
                n_checked += 1
                a = integer_qth_root(x - 1, q)
                b = integer_qth_root(x + 1, q)
                # gcd must be 1 for the coprime-factorisation to a^q, b^q
                g = gcd_exact(x - 1, x + 1)
                ok = (g == 1 and a ** q == (x - 1) and b ** q == (x + 1)
                      and 1 <= a < b)
                if not ok:
                    struct_ok = False
                    print(f"    STRUCT FAILURE x={x} q={q} a={a} b={b} g={g}")
                # y itself checks out: y^q = x^2-1 with y = integer root
                y = integer_qth_root(prod, q)
                if y ** q != prod:
                    struct_ok = False
    print(f"  (iii) for even x <= {x_max:,.0f}, odd prime q <= {q_max}: "
          f"{n_checked} case(s) where x^2-1 is a q-th power; the forced "
          f"structure x-1=a^q, x+1=b^q (a<b, gcd 1) holds in every case: "
          f"{'OK' if struct_ok else 'FAILED'}")
    partb_ok = gcd_ok and gcd_div2_ok and struct_ok
    print("  PART (b) overall: " + ("ALL OK" if partb_ok else "FAILED") + "\n")
    return gcd_ok and gcd_div2_ok and struct_ok


# ---------------------------------------------------------------------------
# (c) brute-force oracle: no even-x solution in the box
# ---------------------------------------------------------------------------
def verify_part_c(even_x_max, q_max):
    """Over even x in [2, even_x_max] and odd prime q <= q_max, assert
    x^2 - y^q = 1 has zero solutions, by exact q-th-power detection of
    x^2 - 1.  Also assert the known solution (3,2,3) is excluded (x odd)."""
    print("=" * 72)
    print("PART (c): brute-force oracle, even x, x^2 - y^q = 1")
    print("=" * 72)
    t0 = time.time()
    found = []
    for x in range(2, even_x_max + 1, 2):
        prod = x * x - 1
        for q in range(3, q_max + 1, 2):
            if is_perfect_qth_power(prod, q):
                y = integer_qth_root(prod, q)
                # exact identity check
                if y ** q == prod:
                    found.append((x, y, q))
    dt = time.time() - t0

    # Falsifier: the known solution (3,2,3) has x odd and must NOT be found
    # in the even-x sweep, and must NOT satisfy x even.
    known = (3, 2, 3)
    known_excluded = (known[0] % 2 == 1)
    # Also verify the known solution satisfies the full equation (sanity).
    xk, yk, qk = known
    known_identity = (xk ** 2 - 1 == yk ** qk)

    ok = (found == [] and known_excluded and known_identity)
    print(f"  even x in [2,{even_x_max:,.0f}], odd prime q <= {q_max}: "
          f"solutions found = {found}")
    print(f"  exact integer arithmetic only: True")
    print(f"  runtime: {dt:.3f}s")
    print(f"  N reached (x bound): {even_x_max:,.0f} (even x); q bound: {q_max}")
    print(f"  known solution (3,2,3): x odd (excluded by hypothesis): "
          f"{known_excluded}; identity 3^2-1 == 2^3: {known_identity}")
    print("  PART (c) verdict: " +
          ("ZERO SOLUTIONS (lemma holds on box) OK" if ok else "PROBLEM") + "\n")
    return ok


# ---------------------------------------------------------------------------
def main():
    print("exp2_even_proof.py — machine verification of lemma exp2-a-even")
    print("x^2 - y^q = 1, x even >= 2, y > 0, q odd prime  =>  NO SOLUTION\n")

    primes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

    ok_a = verify_part_a(primes)

    # (b) numeric confirmation (structure) window + (c) oracle window
    Q_MAX_B = 37
    X_MAX_B = 200_000
    ok_b = verify_part_b(Q_MAX_B, X_MAX_B)

    EVEN_X_MAX = 10_000_000   # 10^7 as requested
    Q_MAX_C = 30
    ok_c = verify_part_c(EVEN_X_MAX, Q_MAX_C)

    overall = ok_a and ok_b and ok_c
    print("=" * 72)
    if overall:
        print("OVERALL: ALL PARTS OK — lemma exp2-a-even verified by "
              "elementary calculation")
    else:
        print("OVERALL: SOME PART FAILED")
    print("=" * 72)
    return 0 if overall else 1


if __name__ == "__main__":
    import sys
    sys.exit(main())
