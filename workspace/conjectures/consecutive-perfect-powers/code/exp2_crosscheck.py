#!/usr/bin/env python3
"""exp2_crosscheck.py — INDEPENDENT exact-integer cross-check of the two
exponent-2 cases of Catalan's equation  x^p - y^q = 1.

Do NOT import from lib.perfectpow, lib.cond, or scholar_oracle.  This program
is a deliberately different code path:

  * root extraction uses gmpy2.iroot (exact integer arbitrary-precision),
    not the integer-Newton iroot in lib.perfectpow and not the
    set-enumeration of scholar_oracle.
  * enumeration loops the unbounded coordinate on one side and solves the
    perfect-power equation on the other side with an exact q-th / p-th root.
  * a pure-residue modular prefilter (a genuine q-th/p-th power is always a
    q-th/p-th power residue mod any modulus, so the filter never discards a
    real solution) cuts the number of expensive root calls without touching
    correctness.

Two cases:
  Task 1  x^p - y^2 = 1, p = ODD prime, q = 2.
          Iterate y in [2, M1]; m = y^2 + 1 must equal x^p.
          Expected: NO solution for any reachable M1.
  Task 2  x^2 - y^q = 1, q = ODD prime, p = 2.
          Iterate x in [2, M2]; m = x^2 - 1 must equal y^q.
          Expected: the single solution (x,y,q) = (3,2,3) only.

Exact integer arithmetic only: no floats, no math.pow, no logarithms.
"""
import time
import gmpy2


# ---------------------------------------------------------------------------
# Small number-theory helpers (exact integer)
# ---------------------------------------------------------------------------
def is_prime(n):
    """Exact trial division; n is small in every use here."""
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def prime_1mod_q(q, start):
    """Smallest prime r >= start with r == 1 (mod q)."""
    r = start
    while not (r % q == 1 and is_prime(r)):
        r += 1
    return r


def odd_primes_upto(limit):
    return [p for p in range(3, limit + 1) if is_prime(p)]


def perfect_radius_bound(bound):
    """Biggest candidate exponent e with 2^e <= bound (so a base >= 2 can
    produce an e-th power <= bound)."""
    e = 0
    while 2 ** (e + 1) <= bound:
        e += 1
    return e


# ---------------------------------------------------------------------------
# Residue prefilter (never discards a genuine solution)
# ---------------------------------------------------------------------------
def build_filters(primes):
    """For each prime q in `primes`, build two list-index residue indicators
    mod r1 and mod r2 (r_i prime, r_i == 1 mod q).  For any modulus r a true
    q-th power reduces to a q-th power residue, so if m is NOT a q-th power
    residue mod r_i it cannot be a genuine q-th power.  The two moduli are
    combined with AND, cheaply, before any expensive root call.

    For the candidate exponent q, the relevant residue set is { z^q mod r }:
    the q-th power residues.  Modi r_i == 1 (mod q) make the map z -> z^q
    genuinely non-surjective, so the filter rejects a large fraction of
    non-powers.

    Returns {q: (r1, arr1, r2, arr2)} where arr_i[x] == 1 iff x is a q-th
    power residue mod r_i.
    """
    filt = {}
    for q in primes:
        r1 = prime_1mod_q(q, 3)
        # find a second prime r2 == 1 mod q, distinct from r1
        r2 = prime_1mod_q(q, r1 + 1)
        a1 = [0] * r1
        a2 = [0] * r2
        for y in range(r1):
            a1[pow(y, q, r1)] = 1
        for y in range(r2):
            a2[pow(y, q, r2)] = 1
        filt[q] = (r1, a1, r2, a2)
    return filt


# ---------------------------------------------------------------------------
# Task 1:  x^p - y^2 = 1, p odd prime.  No solutions expected.
# ---------------------------------------------------------------------------
def search_xp_minus_y2(M1):
    """All (x, p, y) with 2 <= y <= M1, p odd prime, m = y^2+1 = x^p.

    Exposed so callers can confirm no x^p - y^2 = 1 (p odd) exists.
    """
    pmax = perfect_radius_bound(M1 * M1 + 1)
    primes = odd_primes_upto(pmax)
    if not primes:
        return []
    filt = build_filters(primes)
    found = []
    for y in range(2, M1 + 1):
        m = y * y + 1               # m = x^p must be an exact p-th power
        for p in primes:
            if 2 ** p > m:
                break               # primes ascending: no larger p can fit
            r1, a1, r2, a2 = filt[p]
            if not (a1[m % r1] and a2[m % r2]):
                continue
            x, ok = gmpy2.iroot(m, p)
            if ok:
                found.append((int(x), p, y))
    return sorted(found)


# ---------------------------------------------------------------------------
# Task 2:  x^2 - y^q = 1, q odd prime.  Expected single solution (3,2,3).
# ---------------------------------------------------------------------------
def search_x2_minus_yq(M2):
    """All (x, y, q) with 2 <= x <= M2, q odd prime, m = x^2-1 = y^q."""
    qmax = perfect_radius_bound(M2 * M2 - 1)
    primes = odd_primes_upto(qmax)
    if not primes:
        return []
    filt = build_filters(primes)
    found = []
    for x in range(2, M2 + 1):
        m = x * x - 1               # m = y^q must be an exact q-th power
        for q in primes:
            if 2 ** q > m:
                break
            r1, a1, r2, a2 = filt[q]
            if not (a1[m % r1] and a2[m % r2]):
                continue
            y, ok = gmpy2.iroot(m, q)
            if ok:
                found.append((x, int(y), q))
    return sorted(found)


def main():
    M1 = 10 ** 7     # task 1: y <= 10^7  (x^p = y^2+1 <= 10^14 + 1)
    M2 = 10 ** 8     # task 2: x <= 10^8  (y^q = x^2-1 <= 10^16 - 1)

    print("=" * 72)
    print("TASK 1: x^p - y^2 = 1, p ODD prime, iterate y in [2, M1]")
    print("        m = y^2+1 tested as an exact p-th power (gmpy2.iroot)")
    print("        Expected: NO solution.  M1 = %d" % M1)
    print("=" * 72)
    t0 = time.time()
    r1 = search_xp_minus_y2(M1)
    dt = time.time() - t0
    print("solutions (x, p, y):", r1)
    print("count:", len(r1))
    print("verdict:", "AGREE (none found)" if not r1 else "DISAGREE (solution found!)")
    print("runtime: %.3fs" % dt)

    print()
    print("=" * 72)
    print("TASK 2: x^2 - y^q = 1, q ODD prime, iterate x in [2, M2]")
    print("        m = x^2-1 tested as an exact q-th power (gmpy2.iroot)")
    print("        Expected: single solution (x,y,q)=(3,2,3).  M2 = %d" % M2)
    print("=" * 72)
    t0 = time.time()
    r2 = search_x2_minus_yq(M2)
    dt = time.time() - t0
    print("solutions (x, y, q):", r2)
    print("count:", len(r2))
    expected = [(3, 2, 3)]
    print("verdict:", "AGREE (exactly (3,2,3))" if r2 == expected else "DISAGREE")
    print("runtime: %.3fs" % dt)


if __name__ == "__main__":
    main()
