#!/usr/bin/env python3
"""verify_foundations.py

Exact-integer verification foundation for the consecutive-perfect-powers (
Catalan) run. Five sections; every comparison is exact integer arithmetic
(no floats, no logarithms, no math.pow).

  1. ORACLE: perfect_powers_upto / solutions(N) == exactly {(3,2,2,3)} for
     every reachable N >= 9.
  2. EXP2-xq: x^2 - y^q = 1, q prime  ->  unique (3,2,3) in range.
  3. EXP2-yp: x^p - y^2 = 1, p prime  ->  none in range.
  4. PRIME-REDUCTION: composite p=a*P, q=b*Q (P,Q prime) gives
     (x^a)^P - (y^b)^Q = x^p - y^q (exact identity) on a few dozen cases.
  5. DOUBLE-WIEFERICH: for distinct odd primes p,q <= 200, both congruences
     p^(q-1) mod q^2 and q^(p-1) mod p^2, via pow(base, exp, mod).
"""
import time
from math import isqrt


def is_prime(n):
    """Trial division, exact integers; n small in all uses here."""
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


def perfect_powers_upto(N):
    """value -> [(base, exp)] for all perfect powers n=base^exp, 2<=base, 2<=exp,
    with n <= N. Exact integer arithmetic only."""
    powers = {}
    x = 2
    while x * x <= N:
        v = x * x
        e = 2
        while v <= N:
            powers.setdefault(v, []).append((x, e))
            v *= x
            e += 1
        x += 1
    return powers


def solutions(N):
    """All (x,p,y,q), x^p,y^q<=N, x^p - y^q = 1. Exact arithmetic."""
    powers = perfect_powers_upto(N)
    result = set()
    for u in powers:  # u = x^p
        if u - 1 in powers:  # u - 1 = y^q
            for (x, p) in powers[u]:
                for (y, q) in powers[u - 1]:
                    if x ** p - y ** q == 1:
                        result.add((x, p, y, q))
    return sorted(result)


def exp2_xq_solutions(N):
    """x^2 - y^q = 1, x,y>0, q>1 prime, with x^2,y^q <= N. Exact arithmetic."""
    powers = perfect_powers_upto(N)
    result = set()
    for u in powers:
        if u - 1 in powers:
            for (x, p) in powers[u]:
                if p == 2:            # the x-side exponent must be 2
                    for (y, q) in powers[u - 1]:
                        if q > 1 and is_prime(q):
                            if x ** p - y ** q == 1:
                                result.add((x, p, y, q))
    return sorted(result)


def exp2_yp_solutions(N):
    """x^p - y^2 = 1, x,y>0, p>1 prime, with x^p,y^2 <= N. Exact arithmetic."""
    powers = perfect_powers_upto(N)
    result = set()
    for u in powers:
        if u - 1 in powers:
            for (x, p) in powers[u]:
                if p > 1 and is_prime(p):
                    for (y, q) in powers[u - 1]:
                        if q == 2:    # the y-side exponent must be 2
                            if x ** p - y ** q == 1:
                                result.add((x, p, y, q))
    return sorted(result)


def prime_reduction_cases(n_cases=40, seed=12345):
    """Concrete composite-exponent cases: choose x,y, primes P,Q and
    multipliers a,b; form p=a*P, q=b*Q and verify the exact identity
    (x^a)^P - (y^b)^Q == x^p - y^q."""
    import random
    rng = random.Random(seed)
    primes_small = [t for t in range(2, 50) if is_prime(t)]
    cases = []
    for _ in range(n_cases):
        x = rng.randint(2, 20)
        y = rng.randint(1, 20)
        P = rng.choice(primes_small)
        Q = rng.choice(primes_small)
        a = rng.randint(2, 6)
        b = rng.randint(2, 6)
        p = a * P
        q = b * Q
        reduced = (x ** a) ** P - (y ** b) ** Q
        original = x ** p - y ** q
        assert reduced == original, (x, P, a, y, Q, b)
        cases.append({
            "x": x, "p": p, "y": y, "q": q,
            "a": a, "P": P, "b": b, "Q": Q,
            "reduced": reduced, "original": original,
        })
    return cases


def double_wieferich_stats(N=200):
    """For distinct odd primes p,q <= N:
    c1 = p^(q-1) = 1 mod q^2   (base p with prime q)
    c2 = q^(p-1) = 1 mod p^2   (base q with prime p)
    An unordered pair {p,q} is a double-Wieferich pair iff both hold.
    Returns ordered pairs satisfying both, plus count of unordered pairs
    satisfying at least one of the two congruences."""
    primes = [t for t in range(3, N + 1) if is_prime(t)]
    both = []          # ordered (p,q) with p != q satisfying BOTH
    at_least_one = set()  # frozenset{p,q} satisfying at least one
    for p in primes:
        for q in primes:
            if p == q:
                continue
            c1 = pow(p, q - 1, q * q) == 1
            c2 = pow(q, p - 1, p * p) == 1
            if c1 and c2:
                both.append((p, q))
            if c1 or c2:
                at_least_one.add(frozenset((p, q)))
    # unordered representatives (p<q) of double-Wieferich pairs
    unordered = sorted({frozenset(t) for t in both}, key=lambda f: (min(f), max(f)))
    reps = [(min(f), max(f)) for f in unordered]
    return primes, both, reps, len(at_least_one)


def main():
    print("=" * 70)
    print("1. ORACLE: solutions(N) for N in {9,100,1000,...,10^8}")
    print("=" * 70)
    ladder = [9, 100, 1000, 10 ** 4, 10 ** 5, 10 ** 6, 10 ** 7, 10 ** 8]
    expected = {(3, 2, 2, 3)}
    all_ok = True
    for N in ladder:
        t0 = time.time()
        r = solutions(N)
        dt = time.time() - t0
        ok = set(r) == expected
        all_ok = all_ok and ok
        print(f"N={N:<10} result={r}  {'OK' if ok else 'MISMATCH'}  {dt:.3f}s")
    largest = ladder[-1]
    print(f"Largest N reached: {largest}")
    print(f"ORACLE exact-match (=={{(3,2,2,3)}}) for every N>=9 reached: "
          f"{'PASS' if all_ok else 'FAIL'}")

    print()
    print("=" * 70)
    print("2. EXP2-xq: x^2 - y^q = 1, q prime, x^2,y^q <= N")
    print("=" * 70)
    for N in ladder:
        t0 = time.time()
        r = exp2_xq_solutions(N)
        dt = time.time() - t0
        ok = set(r) == {(3, 2, 2, 3)}   # tuple (x,p,y,q)=(3,2,2,3) means (x,y,q)=(3,2,3)
        print(f"N={N:<10} result={r}  {'OK' if ok else 'MISMATCH'}  {dt:.3f}s")

    print()
    print("=" * 70)
    print("3. EXP2-yp: x^p - y^2 = 1, p prime, x^p,y^2 <= N")
    print("=" * 70)
    for N in ladder:
        t0 = time.time()
        r = exp2_yp_solutions(N)
        dt = time.time() - t0
        ok = (r == [])
        print(f"N={N:<10} result={r}  {'OK(none)' if ok else 'FOUND'}  {dt:.3f}s")

    print()
    print("=" * 70)
    print("4. PRIME-REDUCTION: composite p=a*P, q=b*Q (P,Q prime)")
    print("     (x^a)^P - (y^b)^Q == x^p - y^q")
    print("=" * 70)
    cases = prime_reduction_cases()
    print(f"Generated and checked {len(cases)} concrete composite cases; "
          f"every reduced==original identity held.")
    for c in cases[:6]:
        print(f"  x={c['x']:<3} y={c['y']:<3} p=a*P={c['a']}*{c['P']}={c['p']:<4} "
              f"q=b*Q={c['b']}*{c['Q']}={c['q']:<4} "
              f"val={c['original']}")

    print()
    print("=" * 70)
    print("5. DOUBLE-WIEFERICH structure for distinct odd primes p,q <= 200")
    print("=" * 70)
    primes, both, reps, n_atleast = double_wieferich_stats(200)
    print(f"Number of odd primes <= 200: {len(primes)}")
    print(f"Number of ordered distinct pairs: {len(primes)*(len(primes)-1)}")
    # orderings: by (p,q) sorted ascending first-element, then the swap
    both_sorted = sorted(both, key=lambda t: (t[0], t[1]))
    print("Double-Wieferich ordered pairs (p,q) satisfying BOTH congruences:")
    if both_sorted:
        shown = both_sorted[:20]
        for p, q in shown:
            print(f"  (p={p}, q={q}): p^(q-1)={pow(p, q-1, q*q):<6} (mod {q*q}), "
                  f"q^(p-1)={pow(q, p-1, p*p):<6} (mod {p*p})")
        if len(both_sorted) > 20:
            print(f"  ... and {len(both_sorted)-20} more")
        # smallest under each of the two orderings
        s1 = both_sorted[0]
        s1_swap = (s1[1], s1[0])
        print(f"Smallest ordered pair under (p,q) with both: {s1}")
        print(f"  its swap under the reverse ordering (q,p): {s1_swap}")
    else:
        print("  NONE found within p,q <= 200.")
    print(f"Unordered pairs {{p,q}}, p<q, satisfying at least one of the two "
          f"congruences: {n_atleast}")
    print(f"Unordered double-Wieferich pairs (both): {len(reps)} -> {reps}")


if __name__ == "__main__":
    main()
