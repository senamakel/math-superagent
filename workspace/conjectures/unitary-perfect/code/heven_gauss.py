#!/usr/bin/env python3
"""Gaussian factorization of 2^p + i, quartic characters, H_even divisor data.

TASK: first concrete step of the adopted approach
research/approaches/biquadratic-character-divisors.md: factor 2^p + i in
Z[i] for small odd primes p, tabulate the quartic character (2/pi)_4 of
each Gaussian prime factor pi (rational norm r) against p mod 8 and the
Aurifeuillean half (L_p or M_p) containing r.

Math (exact, all integer arithmetic; no floats anywhere):
  - 2^{2p}+1 = L_p * M_p,  L_p = 2^p - 2^((p+1)/2) + 1,
    M_p = 2^p + 2^((p+1)/2) + 1;  L_p, M_p coprime and odd.
  - Every prime divisor q of 2^{2p}+1 is q = 1 (mod 4); 5 always divides
    2^{2p}+1 for odd p.
  - ORD STRUCTURE (elementary): 2^{2p} = -1 (mod q) and 2^{4p} = 1 give
    ord_q(2) | 4p with ord_q(2) !| 2p, so ord_q(2) in {4, 4p}; ord = 4
    forces q | 2^4 - 1 = 15, i.e. q = 5 (q = 3 never divides 2^{2p}+1).
    By LTE v_5(2^{2p}+1) = 1 + v_5(p), so the factor 5 in 2^{2p}+1 = 5*Phi
    is v_5(p); hence EVERY prime divisor of Phi_{4p}(2) = (2^{2p}+1)/5 is
    primitive (ord = 4p) and q = 1 (mod 4p), with the single exception
    q = 5 for p = 5 (5 | 4p, ord_5(2) = 4).  Verified exactly below (C4/C6).
  - QUARTIC CHARACTER: for a primitive divisor r | 2^{2p}+1 and a
    primitive root g mod r with 2 = g^j, ord = 4p forces
    gcd(j, r-1) = (r-1)/4p = t and j = t*u with u odd (gcd(u, 4p) = 1),
    so  (2/r)_4 = 1  <==>  4 | j  <==>  4 | t  <==>  16p | r-1
    <==>  v2(r-1) >= 4  <==>  r = 1 (mod 16).
  - (2/pi)_4 for the Gaussian prime pi = su + sv*i dividing 2^p + i,
    N(pi) = r prime: computed in F_r via c = 2^((r-1)/4) mod r (a rational
    integer), with the class of i in F_r = Z[i]/(pi) fixed by
    i = -su * sv^{-1} (mod r).

Checks performed (exact; all must PASS for the run to exit 0):
  C1. Gaussian factorization product == 2^p + i up to a unit of Z[i].
  C2. L_p * M_p == 2^{2p}+1 and gcd(L_p, M_p) == 1.
  C3. every q | 2^{2p}+1 is = 1 mod 4;  q = 5  <==>  ord_q(2) = 4.
  C4. q != 5  ==>  q = 1 (mod 4p)  (the ord = 4p structural fact).
  C5. (char == +1)  ==  (16 | r-1)  for every prime divisor (the mod-16
      coin flip of Conjecture 29, at the divisor level).
  C6. prod over q != 5 of q^e == (2^{2p}+1)//5 == Phi_{4p}(2).
  C7. every q divides exactly one of L_p, M_p.
  C8. full exact 3-Higgs status of q whenever q-1 <= 10^12
      (else "v2-only": v2(q-1) >= 4 already proves q non-3-Higgs).

Output: per-p divisor table, heads (r = 1 mod 16, i.e. v2(r-1) >= 4,
necessarily non-3-Higgs) list, non-Higgs witness report for every
3-Higgs p <= 61, char distribution by (p mod 8, Aurifeuillean half).

Usage:  timeout 540 python3 code/heven_gauss.py [PMAX]
  PMAX default 61: all odd primes 3 <= p <= 61, every 2^{2p}+1 fully
  factored (max 37 digits at p = 61).  Range covered and what was left
  unfactored (nothing, by construction) are stated in the final block.
"""
import sys
from math import gcd, isqrt
from collections import defaultdict

from sympy import factorint, isprime

# ---------------------------------------------------------------------------
# exact Gaussian integer helpers
# ---------------------------------------------------------------------------


def gmul(u, v, s, t):
    """(u + v*i) * (s + t*i) in Z[i], exact."""
    return (u * s - v * t, u * t + v * s)


def v2_of(n):
    """v_2(n), exact; n >= 1."""
    return (n & -n).bit_length() - 1


def cornacchia(q, x):
    """q prime = 1 mod 4, x^2 = -1 (mod q) -> (u, v) with u^2+v^2 = q, v > 0."""
    a, b = q, x % q
    while b * b > q:
        a, b = b, a % b
    u = b
    vv2 = q - u * u
    v = isqrt(vv2)
    if v * v == vv2 and v > 0:
        return (u, v)
    # safety: scan a tiny neighbourhood; the standard algorithm is
    # guaranteed to produce the representation for prime q, so this
    # fallback exists only to turn a silent bad u into a loud error.
    for uu in range(max(1, u - 2), u + 3):
        w2 = q - uu * uu
        w = isqrt(w2)
        if w * w == w2 and w > 0:
            return (uu, w)
    raise AssertionError("cornacchia: no representation for q=%d" % q)


def quartic_char(p, q, su, sv):
    """(2/pi)_4 in {(1,0),(-1,0),(0,1),(0,-1)} (complex), pi = su+sv*i.

    pi divides 2^p + i, N(pi) = q prime = 1 mod 4.  c = 2^((q-1)/4) mod q
    is a rational integer; the class of i in F_q = Z[i]/(pi) is
    -su * sv^{-1} (mod q).  Asserts c is one of 1, -1, +/-i_class.
    """
    c = pow(2, (q - 1) // 4, q)
    if c == 1:
        return (1, 0)
    if c == q - 1:
        return (-1, 0)
    i_cls = (-su * pow(sv, q - 2, q)) % q
    assert (i_cls * i_cls) % q == q - 1
    if c == i_cls:
        return (0, 1)
    assert c == (q - i_cls) % q
    return (0, -1)


def gauss_factor(p):
    """Exact factorization of 2^p + i in Z[i].

    Returns (rows, N) with rows = [(q, e, su, sv)] meaning
    (su + sv*i)^e || 2^p + i, q = su^2 + sv^2 prime, N = 2^{2p} + 1.
    Full verification: the product equals 2^p + i up to a unit of Z[i].
    """
    a = 2 ** p
    z = (a, 1)
    N = a * a + 1
    fN = factorint(N)
    rows = []
    for q, e in sorted(fN.items()):
        q = int(q)
        assert q % 4 == 1, (p, q)
        x = a % q
        assert (x * x) % q == q - 1
        u, v = cornacchia(q, x)
        assert u * u + v * v == q
        # pi = u + v*i divides z  <==>  q | (a*u + v) and q | (u - a*v)
        pi_div = ((a * u + v) % q == 0) and ((u - a * v) % q == 0)
        # pi_bar = u - v*i divides z  <==>  q | (a*u - v) and q | (a*v + u)
        pb_div = ((a * u - v) % q == 0) and ((a * v + u) % q == 0)
        assert pi_div != pb_div, (p, q)
        su, sv = (u, v) if pi_div else (u, -v)
        rows.append((q, e, su, sv))
    pr = (1, 0)
    for _q, e, su, sv in rows:
        for _ in range(e):
            pr = gmul(pr[0], pr[1], su, sv)
    ok = any(gmul(pr[0], pr[1], uu[0], uu[1]) == z
             for uu in ((1, 0), (-1, 0), (0, 1), (0, -1)))
    if not ok:
        raise AssertionError("Gaussian product != 2^p + i for p=%d" % p)
    return rows, N


# ---------------------------------------------------------------------------
# exact 3-Higgs status, bounded to q-1 <= 1e12 (caller's guarantee)
# ---------------------------------------------------------------------------

_HIGGS_MEMO = {2: True}


def higgs_exact(n):
    """Exact 3-Higgs predicate for prime n with n-1 <= 1e12 (asserted)."""
    n = int(n)
    if n in _HIGGS_MEMO:
        return _HIGGS_MEMO[n]
    assert isprime(n), n
    assert n - 1 <= 10 ** 12, n
    fs = factorint(n - 1)
    ok = all(e <= 3 and higgs_exact(q) for q, e in fs.items())
    _HIGGS_MEMO[n] = ok
    return ok


# ---------------------------------------------------------------------------

P3_MEMO = {}


def p3(n):
    """Exact 3-Higgs status of prime n (n small here, n-1 factors trivially)."""
    n = int(n)
    if n not in P3_MEMO:
        P3_MEMO[n] = higgs_exact(n)
    return P3_MEMO[n]


def fmt_char(c):
    return {1: "+1", -1: "-1", 2: "+i", -2: "-i"}[(c[0] or 0) + (2 * c[1])]


def main():
    pmax = int(sys.argv[1]) if len(sys.argv) > 1 else 61
    primes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53,
              59, 61, 67, 71, 73, 79, 83, 89, 97]
    picked = [p for p in primes if p <= pmax]
    assert picked, "PMAX too small (need >= 3)"
    sys.setrecursionlimit(10000)

    check_counts = defaultdict(int)   # C1..C8 -> number of times verified
    rows_all = []                     # (p, q, e, half, ord, v2, char, head, higgs)
    dist = defaultdict(lambda: defaultdict(int))   # (p%8, half) -> char -> count

    for p in picked:
        s = pow(2, (p + 1) // 2)
        L = 2 ** p - s + 1
        M = 2 ** p + s + 1
        N2 = 2 ** (2 * p) + 1
        assert L * M == N2
        assert gcd(L, M) == 1
        assert N2 % 5 == 0
        check_counts["C2"] += 1

        rows, N = gauss_factor(p)
        assert N == N2
        check_counts["C1"] += 1

        Phi = N // 5
        prod_phi = 1
        print("\np=%d  (3-Higgs %s)  bits(Phi_{4p}(2))=%d  L_p*M_p check ok"
              % (p, "yes" if p3(p) else "no", (2 * p + 1).bit_length()))
        for q, e, su, sv in sorted(rows):
            in_L = L % q == 0
            in_M = M % q == 0
            assert in_L != in_M, (p, q)
            check_counts["C7"] += 1
            half = "L" if in_L else "M"
            assert (q - 1) % 4 == 0          # C3 part
            check_counts["C3"] += 1
            assert pow(2, 2 * p, q) == q - 1
            ordq = 4 if q == 5 else 4 * p
            assert (q == 5) == (pow(2, 4, q) == 1)
            check_counts["C4"] += 1
            if q != 5:
                assert q % (4 * p) == 1, (p, q, q % (4 * p))
                t = (q - 1) // (4 * p)
                v2t = v2_of(t)
            else:
                t = None
                v2t = None
            v2q = v2_of(q - 1)
            char = quartic_char(p, q, su, sv)
            head = (v2q >= 4)
            if (char == (1, 0)) != ((q - 1) % 16 == 0):
                print("C5 FAIL p=%d q=%d char=%s q-1 mod 16=%d"
                      % (p, q, fmt_char(char), (q - 1) % 16))
                sys.exit(1)
            check_counts["C5"] += 1
            if q != 5:
                prod_phi *= q ** e
            if q - 1 <= 10 ** 12:
                hq = higgs_exact(q)
                hidx = "P3" if hq else "non-3H"
            else:
                hq = None
                hidx = "v2-only(%d)" % v2q
            rows_all.append((p, q, e, half, ordq, v2q, char, head, hq))
            dist[(p % 8, half)][fmt_char(char)] += 1
            print("  r=%-14d %s^%d ord=%-4d v2(r-1)=%d t=%s"
                  " (2/r)_4=%s r%%16=%d %s%s"
                  % (q, half, e, ordq, v2q,
                     "." if t is None else str(t),
                     fmt_char(char), q % 16,
                     "HEAD" if head else "   ", hidx))
        assert prod_phi == Phi
        check_counts["C6"] += 1

    # ------------------------------------------------------------- summary
    heads = [(p, q, e, half) for (p, q, e, half, _o, _v, _c, h, _g) in rows_all
             if h]
    print("\n" + "=" * 72)
    print("SUMMARY  (p in odd primes 3..%d, every 2^{2p}+1 fully factored,"
          % pmax)
    print("         max %d digits; nothing left unfactored in range)" % (len(str(2 ** (2 * pmax) + 1))))
    print("checks: " + ", ".join("%s x%d" % (k, v)
                                 for k, v in sorted(check_counts.items())))

    print("\nHEADS (prime divisor r | Phi_{4p}(2) with v2(r-1) >= 4, i.e."
          " r = 1 mod 16, necessarily NON-3-Higgs):")
    if not heads:
        print("  none in range")
    for p, q, e, half in sorted(heads):
        print("  p=%d  r=%d = %s_%d^%d   r = 1 (mod 16) -> 2p=%d killed"
              % (p, q, half, p, e, 2 * p))

    print("\nVERIFIED H_even members with prime p (Thm 8: 2p in {6,10,26,46,"
          "62,82,122}):")
    for p in [3, 5, 13, 23, 31, 41, 61]:
        sub = [r for r in rows_all if r[0] == p]
        heads_p = [r for r in sub if r[7]]
        v2s = sorted(r[5] for r in sub)
        nolarge = all(r[8] is not None for r in sub)
        allH = all(r[8] for r in sub)
        print("  p=%d: r's=%s v2(r-1)=%s heads=%d full-Higgs-all=%s"
              % (p, [r[1] for r in sub], v2s, len(heads_p),
                 "yes" if nolarge and allH else ("not-all-small" if not nolarge else "no")))

    print("\nTHREE-HIGGS p <= 61 with 2p NOT in H_even, witness found in this"
          " table:")
    for p in picked:
        if not p3(p):
            continue
        if 2 * p in (6, 10, 26, 46, 62, 82, 122):
            continue
        sub = [r for r in rows_all if r[0] == p]
        wit = []
        for p0, q, e, half, ordq, v2q, char, head, hq in sub:
            if head:
                wit.append("r=%d v2(r-1)=%d>=4" % (q, v2q))
            elif hq is False:
                wit.append("r=%d not 3-Higgs (exact check of r-1)" % q)
        print("  p=%d (2p=%d): %s" % (p, 2 * p, "; ".join(wit) if wit
                                       else "NO WITNESS in table (undecided here)"))

    print("\nCHARACTER DISTRIBUTION by (p mod 8, Aurifeuillean half):")
    for key in sorted(dist):
        print("  p%%8=%d %s: %s" % (key[0], key[1],
                                    dict(sorted(dist[key].items()))))

    print("\nStructural facts verified exactly for the range:")
    print("  F1. every prime divisor of Phi_{4p}(2) is = 1 (mod 4p)  [ord=4p]")
    print("  F2. (2/r)_4 = +1  <==>  r = 1 (mod 16) for every r | 2^{2p}+1")
    print("DONE")
    sys.exit(0)


if __name__ == "__main__":
    main()