#!/usr/bin/env python3
"""Scholar verification of the two OEIS template summaries.

A006339: least hypotenuse of n distinct Pythagorean triangles.
A046112: smallest integral radius of a circle centred at (0,0) having 8n-4
         lattice points on its circumference (i.e. 4(2n-1) points).

Both are governed by the same arithmetic: for h with prime factorisation
h = prod p_i^{a_i}, the number of unordered representations of h^2 as a sum
of two squares including the degenerate (0,h) one is
    reps(h^2) = ( prod_{p_i = 1 mod 4} (2 a_i + 1) + 1 ) / 2,
and the number of non-degenerate unordered representations is
    R(h) = ( prod (2 a_i + 1) - 1 ) / 2.
This is exactly the run's |S(e)| formula: R(h) = |S(h)|, the count of d > 0
with h^2 +/- d both squares (CONTEXT.md, ap_structure2.py).

So  A006339(n) = min h with R(h) >= n-1,  and
    A046112(n) = min h with R(h) = n-1 (equivalently prod(2a+1) = 2n-1).

Route A: multiplicative-structure search over primes p = 1 mod 4 (a prime
         p = 3 mod 4 or 2 would multiply h without raising prod(2a+1), so it
         can never be in a minimal h).
Route B: independent brute force: enumerate primitive Pythagorean triples
         (u^2-v^2, 2uv, u^2+v^2) and count how many multiples s | h each
         h <= N admits; R(h) = #{ primitive u,v with u^2+v^2 | h }.
Cross-check both routes against each other and against the term lists in the
two summary files (which are read as *expected literals*, not inputs).
"""
import math
from functools import lru_cache

# ---- primes = 1 mod 4 ----
def primes_1mod4(limit):
    out = []
    for p in range(5, limit + 1, 4):
        if all(p % q for q in range(3, math.isqrt(p) + 1, 2)):
            out.append(p)
    return out

PRIMES = primes_1mod4(400)

# ---------- Route A: minimal h with prod(2a+1) >= T (A006339) ----------
def min_h_product_at_least(T):
    """min h (product of primes 1 mod 4) with prod_{p^a||h} (2a+1) >= T."""
    best = [None]
    def rec(idx, h, prod):
        if prod >= T:
            if best[0] is None or h < best[0]:
                best[0] = h
            return
        if best[0] is not None and h >= best[0]:
            return
        for j in range(idx, len(PRIMES)):
            p = PRIMES[j]
            if best[0] is not None and h * p >= best[0]:
                break  # primes increase; adding any more only grows h
            hh, a = h * p, 1
            while True:
                rec(j + 1, hh, prod * (2 * a + 1))
                hh *= p
                a += 1
                if best[0] is not None and hh >= best[0]:
                    break
                if hh > 1 << 80:
                    break
    rec(0, 1, 1)
    return best[0]

def min_h_product_exact(T):
    """min h with prod(2a+1) == T, or None."""
    best = [None]
    def rec(idx, h, prod):
        if prod == T:
            if best[0] is None or h < best[0]:
                best[0] = h
            return
        if prod > T:
            return
        if best[0] is not None and h >= best[0]:
            return
        for j in range(idx, len(PRIMES)):
            p = PRIMES[j]
            if h * p > (1 << 80):
                break
            hh, a = h * p, 1
            while hh <= (1 << 80) and prod * (2 * a + 1) <= T:
                rec(j + 1, hh, prod * (2 * a + 1))
                hh *= p
                a += 1
    rec(0, 1, 1)
    return best[0]

def routeA(N=30):
    a006339 = [min_h_product_at_least(2 * n - 1) for n in range(1, N + 1)]
    a046112 = []
    for n in range(1, N + 1):
        v = min_h_product_exact(2 * n - 1)
        a046112.append(v)
    return a006339, a046112

# ---------- Route B: brute force via primitive triples, h <= NB ----------
def routeB(NB):
    """R(h) for all h <= NB via primitive Pythagorean (u,v) triples."""
    R = [0] * (NB + 1)
    umax = math.isqrt(NB)
    for u in range(2, umax + 1):
        for v in range(1, u):
            if (u - v) % 2 == 0 or math.gcd(u, v) != 1:
                continue
            s = u * u + v * v
            if s > NB:
                break
            for k in range(s, NB + 1, s):
                R[k] += 1
    return R

# ---------- Expected terms from the two summary files (comparison only) ----------
A006339_LISTED = [1,5,25,125,65,3125,15625,325,390625,1953125,1625,48828125,
    4225,1105,6103515625,30517578125,40625,21125,3814697265625,203125,
    95367431640625,476837158203125,5525,11920928955078125,274625,5078125,
    1490116119384765625,528125,25390625,186264514923095703125]
A046112_LISTED = [1,5,25,125,65,3125,15625,325,390625,1953125,1625,48828125,
    4225,1105,6103515625,30517578125,40625,21125,3814697265625,203125,
    95367431640625,476837158203125,5525,11920928955078125,274625]

def main():
    a6, a4 = routeA(30)
    print("A006339 route A (n=1..30):")
    print(a6)
    ok6 = (a6 == A006339_LISTED)
    print("matches listed terms:", ok6)
    for i, (c, l) in enumerate(zip(a6, A006339_LISTED), 1):
        if c != l:
            print(f"  mismatch at n={i}: computed {c}, listed {l}")
    print("A046112 route A (n=1..25): computed first 25, compare with listed")
    a4c = a4[:25]
    print(a4c)
    ok4 = (a4c == A046112_LISTED)
    print("matches listed terms:", ok4)
    for i, (c, l) in enumerate(zip(a4c, A046112_LISTED), 1):
        if c != l:
            print(f"  mismatch at n={i}: computed {c}, listed {l}")

    # Route B cross-check: R(h) counted by triple-enumeration vs formula
    NB = 50000
    R = routeB(NB)
    # formula for R(h)
    def R_formula(h):
        prod = 1
        x = h
        d = 2
        while d * d <= x:
            if x % d == 0:
                a = 0
                while x % d == 0:
                    x //= d
                    a += 1
                if d % 4 == 1:
                    prod *= 2 * a + 1
            d += 1
        if x > 1 and x % 4 == 1:
            prod *= 3
        return (prod - 1) // 2
    bad = [h for h in range(1, NB + 1) if R[h] != R_formula(h)]
    print("Route B vs formula, h<=%d: mismatches: %d" % (NB, len(bad)))
    if bad[:10]:
        print("  first mismatches:", bad[:10])

    # Cross-check the minimal-h claims on the brute-force range
    # A006339(n) = min h with R(h) >= n-1; A046112(n) = min h with R(h) = n-1
    min_ge = {}
    min_eq = {}
    for h in range(1, NB + 1):
        r = R[h]
        if r not in min_eq:
            min_eq[r] = h
        for n in range(1, 31):
            t = n - 1
            if r >= t and t not in min_ge:
                min_ge[t] = h
    print("Brute-force cross-check (terms with min h <= %d):" % NB)
    for n in range(1, 31):
        if min_ge.get(n - 1) == a6[n - 1]:
            print(f"  A006339({n}) = {a6[n-1]} OK")
        elif min_ge.get(n - 1) is not None and min_ge.get(n - 1) != a6[n - 1]:
            print(f"  A006339({n}) = {a6[n-1]} vs brute {min_ge.get(n-1)} MISMATCH")
    for n in range(1, 26):
        if min_eq.get(n - 1) == a4c[n - 1]:
            print(f"  A046112({n}) = {a4c[n-1]} OK")
        elif min_eq.get(n - 1) is not None and min_eq.get(n - 1) != a4c[n - 1]:
            print(f"  A046112({n}) = {a4c[n-1]} vs brute {min_eq.get(n-1)} MISMATCH")

    # Relationship to the run's |S(e)|: |S(65)| should be 4, |S(325)| = 7,
    # |S(e)| max claim at e = 9,773,725 (from CONTEXT.md) is 202: check.
    for e in (65, 325, 9773725):
        r = R_formula(e)
        print(f"|S({e})| = R({e}) = {r}")
    # record centres: first e with |S(e)| >= 5 is 325
    print("A006339(6)=3125 => |S(3125)| =", R_formula(3125))

if __name__ == "__main__":
    main()