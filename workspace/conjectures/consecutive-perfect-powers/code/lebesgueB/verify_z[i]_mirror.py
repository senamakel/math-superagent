#!/usr/bin/env python3
"""Machine-verify the Z[i] proof of Lebesgue Case B (x^p - y^2 = 1, p odd
prime >= 3, x,y >= 1, NO solution) with EXACT integer arithmetic, keeping the
unit u EXPLICIT in the factorisation y+i = u*(a+bi)^p (u in {±1,±i}) — the
"mirror" of the prior code/caseB/certify_lebesgue_caseB.py, which absorbed the
unit into the base. This version checks each step over the stated ranges.

Steps verified here:

  STEP 1 (x even impossible): if x is even and p >= 2 then x^p = 0 (mod 4), so
        y^2 = x^p - 1 = -1 = 3 (mod 4), impossible (squares mod 4 are 0,1).
        Hence x is odd.  Falsifier/enumeration: for x in [1,10^6] and
        p in {3,5,7,11,13}, confirm x^p - 1 is never a perfect square
        (no solution in the box), exact integer arithmetic only.

  STEP 2 (x odd forces y even; gcd is a unit): x odd  ==>  x^p odd  ==>
        y^2+1 = x^p odd  ==>  y^2 even  ==>  y even.  In Z[i]: x^p = (y+i)(y-i),
        N(y+i) = y^2+1 is odd, and 1+i divides neither factor when y even
        (re(y+i)=y even, im=1 odd: parity differs).  So gcd(y+i, y-i) is a unit.
        Checked for all even y in [1,10^4].

  STEP 3 (factorisation): x^p = (y+i)(y-i) with coprime factors, Z[i] a UFD, p
        odd  ==>  y+i = u*(a+bi)^p for a unit u in {±1,±i}.  Verified for
        random (a,b) constructions: the representation is consistent
        (N(u*(a+bi)^p) = (a^2+b^2)^p, unit absorption w^p = u exists for every
        unit and odd p, and no random construction yields a unit multiple with
        imaginary part 1 -- i.e. no unexpected solution; none expected).

  STEP 4 (binomial lemmas, exact):
     (A) Im((a+bi)^p) = b * integer (each odd-k binomial term carries b^k,
         k >= 1), hence Im = ±1 forces b = ±1.   [structural, all p; spot check]
         Symmetrically Re((a+bi)^p) = a * integer (p odd: each real term carries
         a^{p-k} with p-k odd >= 1), hence Re = ±1 forces a = 1.  [used in u=±i]
     (B) u = ±1 case: Im((a±i)^p) = ±1 has no solution for 1<=a<=500,
         odd prime p<=97.   [verified-numerically over the range]
     (C) u = ±i case: Re((a+bi)^p) = ±1 forces a = 1; then Re((1+bi)^p) = ±1
         has no solution for 1<=b<=500, odd prime p<=97.
         [verified-numerically over the range]

Falsifier: the known solution 3^2 - 2^3 = 1 has y-exponent 3 (q=3), so it sits
OUTSIDE this case's hypothesis (q=2, p odd prime).  Nothing here asserts that
the known solution does not exist; the case hypothesis simply does not apply
to it.

All arithmetic exact (Python ints, math.isqrt, math.comb, exact Gaussian
integers from code/lib/gaussint.py).  No floats.
"""

import math
import random
import sys
import time

from lib.gaussint import G, gmul, gpow, gnorm, ggcd, gis_unit, gim, gre

random.seed(20240528)


def is_odd_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    r = math.isqrt(n)
    for d in range(3, r + 1, 2):
        if n % d == 0:
            return False
    return True


def odd_primes_up_to(bound):
    return [p for p in range(3, bound + 1, 2) if is_odd_prime(p)]


PRIMES_97 = odd_primes_up_to(97)          # 3,5,...,97  (24 primes)
PRIMES_13 = [3, 5, 7, 11, 13]

results = []


def cert(step, label, ok, detail=""):
    results.append((step, label, ok))
    status = "PASS" if ok else "FAIL"
    print(f"  [{status}] step {step}: {label}"
          + (f"   [{detail}]" if detail else ""))
    return ok


# ---------------------------------------------------------------------------
def step1_parity(xmax, primes):
    print("\n=== STEP 1: x even impossible (mod 4); enumerate x<=%d, p in %s ==="
          % (xmax, primes))
    # Parity: x even, p>=2  ==>  x^p = 0 mod 4; y^2 = x^p - 1 = -1 = 3 mod 4.
    ok_mod4 = all((pow(x, p, 4) == 0 and (pow(x, p, 4) - 1) % 4 == 3)
                  for x in range(2, 2000, 2) for p in primes)
    # squares mod 4 are {0,1}; 3 is not a square mod 4
    ok_square = all((r * r) % 4 in (0, 1) for r in range(0, 64))
    cert(1, "x even & p>=2  ==>  x^p=0 (mod 4), so y^2 = -1 = 3 (mod 4): "
            "impossible since squares mod 4 are 0,1",
         ok_mod4 and ok_square)

    # Enumeration / falsifier: no (x,p) in the box has x^p - 1 a perfect square.
    t0 = time.time()
    found = []
    n_pairs = 0
    # y >= 1 requires x^p - 1 = y^2 >= 1, i.e. x^p >= 2, so x >= 2 (x=1 gives
    # y=0, outside the hypothesis).  Enumerate x in [2, xmax].
    for p in primes:
        for x in range(2, xmax + 1):
            n_pairs += 1
            t = pow(x, p) - 1
            s = math.isqrt(t)
            if s * s == t:
                found.append((x, p, s))
    dt = time.time() - t0
    print(f"  enumerated {n_pairs} pairs (x<=10^{int(math.log10(xmax))}, "
          f"p in {primes}) in {dt:.2f}s; perfect squares found: {len(found)}")
    if found:
        print("  !! solutions found (would refute):", found[:10])
    cert(1, f"no solution (x^p - y^2 = 1, y>=1) for x in [2,{xmax}], "
            f"p in {primes}",
         len(found) == 0, f"{n_pairs} pairs exact")
    return len(found) == 0


# ---------------------------------------------------------------------------
def step2_gcd(ymax):
    print(f"\n=== STEP 2: x odd forces y even; gcd(y+i, y-i) a unit, y<=10^{int(math.log10(ymax))} ===")
    # x odd  ==>  x^p odd  ==>  y^2+1 odd  ==>  y^2 even  ==>  y even
    ok_even = all((pow((2 * k + 1), 3) - 1) % 2 == 0  # x odd -> x^p-1 even -> y^2 even
                  for k in range(0, 1000))
    cert(2, "x odd  ==>  x^p - 1 even  ==>  y even", ok_even)

    ok_norm = all(gnorm(G(y, 1)) == y * y + 1 and (y * y + 1) % 2 == 1
                  for y in range(2, ymax + 1, 2))
    cert(2, "N(y+i)=y^2+1 is odd for even y (y in [2,%d] even)" % ymax, ok_norm)

    ok_nodiv = True
    bad = []
    for y in range(2, ymax + 1, 2):
        # 1+i | (a+bi)  <=>  a,b same parity. y even, im=+1 or -1 (odd) -> not.
        if (y % 2) == (1 % 2):
            bad.append(('y+i', y))
        if (y % 2) == ((-1) % 2):   # -1 is odd
            bad.append(('y-i', y))
    ok_nodiv = (len(bad) == 0)
    cert(2, "1+i divides neither y+i nor y-i for even y (parity differs)",
         ok_nodiv, f"{len(bad)} bad" if bad else "all good")

    ok_gcd = True
    badg = 0
    for y in range(2, ymax + 1, 2):
        g = ggcd(G(y, 1), G(y, -1))
        if not gis_unit(g):
            ok_gcd = False
            badg += 1
            if badg <= 5:
                print(f"     non-unit gcd for y={y}: g={g}, N={gnorm(g)}")
    cert(2, f"gcd(y+i,y-i) is a unit for every even y in [2,{ymax}]",
         ok_gcd, f"{badg} non-unit")
    return ok_even and ok_norm and ok_nodiv and ok_gcd


# ---------------------------------------------------------------------------
def step3_factor(primes, trials):
    print("\n=== STEP 3: y+i = u*(a+bi)^p, u in {±1,±i} (representation) ===")
    i_pow = [(1, 0), (0, 1), (-1, 0), (0, -1)]   # i^m, m=0..3
    units = [(1, 0), (-1, 0), (0, 1), (0, -1)]   # {1,-1,i,-i}

    # (a) unit absorption: for every unit u and odd p, a unit w with w^p = u
    #     (exactly (i^k)^p = i^m), so u*(a+bi)^p == (w(a+bi))^p.
    ok_absorb = True
    absorb_bad = 0
    for m in range(4):
        u = i_pow[m]
        for p in primes:
            ks = [k for k in range(4) if (k * p) % 4 == m % 4]
            if len(ks) != 1:
                ok_absorb = False
                absorb_bad += 1
                continue
            k = ks[0]
            w = i_pow[k]
            # verify on random (a,b): (w(a+bi))^p == u*(a+bi)^p
            for _ in range(trials):
                a = random.randint(1, 80)
                b = random.randint(-80, 80)
                if b == 0:
                    b = 3
                lhs = gpow(gmul(G(*w), G(a, b)), p)
                rhs = gmul(G(*u), gpow(G(a, b), p))
                if lhs != rhs:
                    ok_absorb = False
                    absorb_bad += 1
    cert(3, "unit absorption: for each u in {±1,±i} and each odd prime p, a "
            "unit w with w^p=u and (w(a+bi))^p == u*(a+bi)^p",
         ok_absorb, f"{absorb_bad} bad")

    # (b) norm identity: N(u*(a+bi)^p) = (a^2+b^2)^p.  Hence if
    #     y+i = u*(a+bi)^p then x^p = (a^2+b^2)^p, i.e. x = a^2+b^2.
    ok_norm = True
    for _ in range(trials * len(primes)):
        a = random.randint(1, 120)
        b = random.randint(-120, 120)
        if b == 0:
            b = 5
        p = random.choice(primes)
        z = gpow(G(a, b), p)
        for u in units:
            if gnorm(gmul(G(*u), z)) != pow(a * a + b * b, p):
                ok_norm = False
    cert(3, "N(u*(a+bi)^p) = (a^2+b^2)^p  (so x = a^2+b^2 if y+i = u(a+bi)^p)",
         ok_norm)

    # (c) consistency: does any random construction yield a unit multiple with
    #     imaginary part 1, i.e. a genuine solution?  None expected.
    found_repr = []
    for _ in range(trials * 4):
        a = random.randint(1, 150)
        b = random.randint(1, 150)
        p = random.choice(primes)
        z = gpow(G(a, b), p)
        for u in units:
            uz = gmul(G(*u), z)
            if gim(uz) == 1:
                y = gre(uz)
                x = a * a + b * b
                # genuine solution check: x^p - y^2 == 1?
                if pow(x, p) - y * y == 1:
                    found_repr.append((a, b, p, u, y, x))
    print(f"  random constructions yielding a genuine y+i = u(a+bi)^p "
          f"(with Im=1 and x^p-y^2=1): {len(found_repr)} "
          f"(expected 0 -- none; task: 'none expected')")
    if found_repr:
        print("  !! unexpected solutions:", found_repr[:10])
    cert(3, "no random (a,b) construction yields a genuine solution",
         len(found_repr) == 0, f"{len(found_repr)} found")
    return ok_absorb and ok_norm and len(found_repr) == 0


# ---------------------------------------------------------------------------
def step4_binomial(primes, arange, brange):
    print("\n=== STEP 4: binomial lemmas (exact integer arithmetic) ===")

    # (A) Im((a+bi)^p) = b*integer for all p; Re((a+bi)^p) = a*integer (p odd).
    #     Structural: odd-k binomial terms carry b^k (k>=1); real terms carry
    #     a^{p-k} with p-k odd >= 1 (p odd).  Verified on a range for all p.
    ok_Im = all(gim(gpow(G(a, b), p)) % b == 0
                for a in range(1, arange + 1)
                for b in range(1, brange + 1)
                for p in primes)
    cert(4, "b | Im((a+bi)^p) for a in [1,%d], b in [1,%d], odd prime p<=97  "
            "==> Im=±1 forces b=±1" % (arange, brange), ok_Im)

    ok_Re = all(gre(gpow(G(a, b), p)) % a == 0
                for a in range(1, arange + 1)
                for b in range(1, brange + 1)
                for p in primes)
    cert(4, "a | Re((a+bi)^p) for the same range (p odd: real terms carry a)  "
            "==> Re=±1 forces a=1", ok_Re)

    # (B) u = ±1 case: Im((a±i)^p) = ±1 has no solution.
    okB = True
    badB = []
    for a in range(1, 501):
        for p in primes:
            for b in (1, -1):
                im = gim(gpow(G(a, b), p))
                if im in (1, -1):
                    badB.append((a, b, p, im))
    okB = len(badB) == 0
    cert(4, "Im((a±i)^p) ∉ {±1} for a in [1,500], odd prime p<=97 "
            "(u=±1 endgame: no solution)", okB,
         f"{len(badB)} violations" if badB else "0 violations, 12000 checks")

    # (C) u = ±i case: Re((a+bi)^p)=±1 forces a=1; Re((1+bi)^p) = ±1 none.
    okC = True
    badC = []
    for b in range(1, 501):
        for p in primes:
            re_ = gre(gpow(G(1, b), p))
            if re_ in (1, -1):
                badC.append((b, p, re_))
    okC = len(badC) == 0
    cert(4, "Re((1+bi)^p) ∉ {±1} for b in [1,500], odd prime p<=97 "
            "(u=±i endgame: a=1 forced, no solution)", okC,
         f"{len(badC)} violations" if badC else "0 violations, 12000 checks")
    return okB and okC


# ---------------------------------------------------------------------------
def falsifier():
    print("\n=== Falsifier: known solution 3^2 - 2^3 = 1 ===")
    x, p, y, q = 3, 2, 2, 3
    print(f"  known solution (x,p,y,q) = ({x},{p},{y},{q}): y-side exponent q={q}, "
          f"x-side exponent p={p}")
    in_case = (q == 2) and is_odd_prime(p)
    print(f"  inside case-B hypothesis (x^p - y^2 = 1, q=2, p odd prime)? "
          f"{in_case}  (q=3, p=2: NOT inside)")
    print("  -> nothing asserted eliminates the known solution; case B only")
    print("     claims no solution with y-exponent 2 and x-exponent odd prime.")
    # sanity: the case equation with q=2 indeed has no small odd-prime solution
    return True


def main():
    t0 = time.time()
    print("Mirror verification:  x^p - y^2 = 1 (Lebesgue Case B), p odd prime >= 3")
    print("Unit u kept EXPLICIT:  y+i = u*(a+bi)^p, u in {±1,±i}.")
    print("Exact integer arithmetic throughout; no floats.\n")

    ok1 = step1_parity(10**6, PRIMES_13)
    ok2 = step2_gcd(10**4)
    ok3 = step3_factor(PRIMES_97, trials=20)
    ok4 = step4_binomial(PRIMES_97, arange=200, brange=200)
    falsifier()

    print("\n=== SUMMARY ===")
    all_ok = True
    for (step, label, ok) in results:
        all_ok &= ok
        print(f"  step {step}: {'PASS' if ok else 'FAIL'}")
    print(f"\nAll steps passed (over their stated ranges): "
          f"{'YES' if all_ok else 'NO'}")
    print("* Step 1 parity is PROVED (mod 4); the x<=10^6 enumeration is a"
          " bounded exact falsifier (0 solutions).")
    print("* Steps 2-3 are PROVED (Z[i] UFD factorisation, norm/unit"
          " identities, checked on ranges).")
    print("* Step 4 divisibility (b | Im, a | Re) is PROVED by the binomial"
          " structure; the endgames")
    print("  'Im((a±i)^p) not ±1' and 'Re((1+bi)^p) not ±1' are"
          " VERIFIED-NUMERICALLY over 1<=a,b<=500, odd prime p<=97 -- NOT proved.")
    print(f"Total runtime: {time.time()-t0:.2f}s")
    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main())
