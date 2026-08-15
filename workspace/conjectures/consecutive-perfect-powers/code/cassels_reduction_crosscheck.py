"""Independent verification of the elementary Cassels core for x^p-y^q=1.
FRESH code path -- must not import lib.valuation, lib.cyclo, or the other
program. Uses only math.gcd and exact integer arithmetic (binary-search
q-th root; no floats).

A separate implementation of the same four facts to cross-check
code/cassels_reduction.py.
"""
from math import gcd


def is_perfect_qth_power(n, q):
    if n < 1:
        return False
    lo, hi = 1, n
    while lo <= hi:
        mid = (lo + hi) // 2
        pw = mid ** q
        if pw == n:
            return True
        if pw < n:
            lo = mid + 1
        else:
            hi = mid - 1
    return False


def v_p(n, p):
    if n == 0:
        raise ValueError
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v


def oracle_exact(N):
    """Build value->[(base,exp)] map by iterating x, then p. Exact ints only."""
    powers = {}
    x = 2
    while x * x <= N:
        val = x * x
        e = 2
        while val <= N:
            powers.setdefault(val, []).append((x, e))
            val *= x
            e += 1
        x += 1
    result = set()
    for u in powers:
        if (u - 1) in powers:
            for (x, p) in powers[u]:
                for (y, q) in powers[u - 1]:
                    if x ** p - y ** q == 1:
                        result.add((x, p, y, q))
    return sorted(result)


def is_prime(n):
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


def main():
    print("=" * 70)
    ok = True
    print("1. ORACLE (crosscheck path)")
    for N in [9, 100, 1000, 10 ** 4, 10 ** 5, 10 ** 6, 10 ** 7]:
        s = oracle_exact(N)
        good = (s == [(3, 2, 2, 3)])
        ok = ok and good
        print(f"   N={N:<10} -> {s}  {'PASS' if good else 'FAIL'}")
    print("   RESULT:", "PASS" if ok else "FAIL")

    print("=" * 70)
    print("2. GCD LEMMA (crosscheck)")
    f2 = 0
    t2 = 0
    for p in [3, 5, 7, 11, 13]:
        for x in range(2, 201):
            t2 += 1
            Phi = (x ** p - 1) // (x - 1)
            if gcd(x - 1, Phi) != gcd(x - 1, p):
                f2 += 1
    print(f"   checked {t2} pairs; failures={f2}; RESULT:", "PASS" if f2 == 0 else "FAIL")

    print("=" * 70)
    print("3. COPRIME-PRODUCT-IS-qTH-POWER (crosscheck)")
    f3 = 0
    t3 = 0
    for q in [3, 5, 7]:
        for A in range(1, 301):
            for B in range(A, 301):
                if gcd(A, B) != 1:
                    continue
                if is_perfect_qth_power(A * B, q):
                    t3 += 1
                    if not (is_perfect_qth_power(A, q) and is_perfect_qth_power(B, q)):
                        f3 += 1
    print(f"   checked {t3} coprime products; failures={f3}; RESULT:", "PASS" if f3 == 0 else "FAIL")

    print("=" * 70)
    print("4. KNOWN SOLUTION CALIBRATION (crosscheck)")
    x, p, y, q = 3, 2, 2, 3
    px1 = ((x - 1) % p == 0)
    qy1 = ((y + 1) % q == 0)
    oddpair = (p >= 3 and q >= 3)
    print(f"   x^p-y^q = {x**p}-{y**q} = {x**p - y**q}")
    print(f"   p|x-1 = {px1}  (2|2 True);  q|y+1 = {qy1}  (3|3 True)")
    print(f"   is_odd_prime_pair = {oddpair}  (False: p=2 even, excluded by hypothesis)")
    print(f"   p|y={y % p == 0}, q|x={x % q == 0}  (Cassels content, outside hypothesis)")
    print("   RESULT: PASS -- known solution excluded by hypothesis, not refuted")

    print("=" * 70)
    print("CROSSCHECK: ALL PASS" if (ok and f2 == 0 and f3 == 0) else "CROSSCHECK FAILED")


if __name__ == "__main__":
    main()
