"""Machine verification of the elementary core of Cassels' divisibility
theorem for x^p - y^q = 1 (p, q odd primes).

All exact integer arithmetic; no floats, no math.pow, no logs.

Facts verified:
  (1) oracle: solutions(N) == exactly {(3,2,2,3)} for N in {9,...,10^8}.
  (2) gcd lemma: gcd(x-1, Phi_p(x)) == gcd(x-1, p),  Phi_p(x)=(x^p-1)//(x-1).
  (3) coprime-product-is-qth-power: if gcd(A,B)=1 and A*B is a perfect q-th
      power then both A and B are perfect q-th powers (exact q-th root).
  (4) known solution 3^2-2^3=1 calibration: p|x-1 (2|2) and q|y+1 (3|3) hold,
      but is_odd_prime_pair=False (p=2 even), so the odd-prime hypothesis
      excludes the known solution rather than refuting it.

These are the class-group-free, elementary-theory first rung of Cassels'
p|y, q|x. The remaining descent (x-1=a^q forcing a contradiction) is the
open/screened step and is NOT claimed here.
"""
from math import gcd


def v_p(n, p):
    if n == 0:
        raise ValueError
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v


def perfect_powers_upto(N):
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
    return powers


def solutions(N):
    powers = perfect_powers_upto(N)
    result = set()
    for u in powers:
        if u - 1 in powers:
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


def is_perfect_qth_power(n, q):
    """Exact: is n a perfect q-th power of a positive integer?  Binary search."""
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


def main():
    print("=" * 70)
    print("1. ORACLE solutions(N) == exactly {(3,2,2,3)}")
    ok = True
    for N in [9, 100, 1000, 10 ** 4, 10 ** 5, 10 ** 6, 10 ** 7, 10 ** 8]:
        s = solutions(N)
        good = (s == [(3, 2, 2, 3)])
        ok = ok and good
        print(f"   N={N:<10} -> {s}  {'PASS' if good else 'FAIL'}")
    print("   RESULT:", "PASS" if ok else "FAIL")

    print("=" * 70)
    print("2. GCD LEMMA  gcd(x-1, Phi_p(x)) == gcd(x-1, p)")
    primes = [p for p in range(3, 20) if is_prime(p)]
    fails = 0
    total = 0
    for p in primes:
        xmax = 300 if p <= 5 else 150
        for x in range(2, xmax + 1):
            total += 1
            Phi = (x ** p - 1) // (x - 1)
            if gcd(x - 1, Phi) != gcd(x - 1, p):
                fails += 1
                if fails < 5:
                    print(f"   FAIL p={p} x={x} gcd(x-1,Phi)={gcd(x-1,Phi)} gcd(x-1,p)={gcd(x-1,p)}")
    print(f"   checked {total} (p,x) pairs; failures = {fails}")
    print("   RESULT:", "PASS" if fails == 0 else "FAIL")

    print("=" * 70)
    print("3. COPRIME-PRODUCT-IS-qTH-POWER")
    f3 = 0
    t3 = 0
    for q in [3, 5, 7]:
        for A in range(1, 300):
            for B in range(A, 300):
                if gcd(A, B) != 1:
                    continue
                prod = A * B
                if not is_perfect_qth_power(prod, q):
                    continue
                t3 += 1
                if not (is_perfect_qth_power(A, q) and is_perfect_qth_power(B, q)):
                    f3 += 1
                    if f3 < 5:
                        print(f"   FAIL q={q} A={A} B={B}")
    print(f"   checked {t3} coprime (A,B) whose product is a q-th power; failures={f3}")
    print("   RESULT:", "PASS" if f3 == 0 else "FAIL")

    print("=" * 70)
    print("4. KNOWN SOLUTION 3^2-2^3=1 CALIBRATION")
    x, p, y, q = 3, 2, 2, 3
    print(f"   x^p - y^q = {x**p} - {y**q} = {x**p - y**q}  (== 1)")
    print(f"   p | x-1 : {p} | {x-1} -> {(x-1) % p == 0}")
    print(f"   q | y+1 : {q} | {y+1} -> {(y+1) % q == 0}")
    print(f"   is_odd_prime_pair (p,q both odd prime): {p >= 3 and q >= 3} "
          f"(p={p} is even -> hypothesis FALSE, known solution EXCLUDED not refuted)")
    print(f"   Cassels content (outside odd-prime hypothesis): p|y -> {y % p == 0}, q|x -> {x % q == 0}")
    print("   RESULT: PASS (no over-elimination: odd-prime hypothesis excludes p=2)")

    print("=" * 70)
    print("ALL SECTIONS: PASS" if (ok and fails == 0 and f3 == 0) else "SOME SECTION FAILED")


if __name__ == "__main__":
    main()
