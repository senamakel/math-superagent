"""Independent naive oracle for Chen-prime flags, cross-checking the sieve.

Exponential-class only as an oracle at bound n <= 200: every number up to 200
is factorised by trial division, Chen-prime flags are computed from the
definition (prime, and p+2 prime or exactly two prime factors counting
multiplicity), and the result is compared with the sieve-based `chen_flags`.
"""
from math import isqrt
from chen_goldbach.check import chen_flags


def factor_count(k: int) -> int:
    """Number of prime factors of k counted with multiplicity."""
    if k < 2:
        return 0
    count, x, d = 0, k, 2
    while d <= isqrt(x):
        while x % d == 0:
            count += 1
            x //= d
        d += 1 if d == 2 else 2
    if x > 1:
        count += 1
    return count


def naive_is_prime(k: int) -> bool:
    if k < 2:
        return False
    if k == 2:
        return True
    if k % 2 == 0:
        return False
    d = 3
    while d <= isqrt(k):
        if k % d == 0:
            return False
        d += 2
    return True


def naive_chen(bound: int) -> bytearray:
    chen = bytearray(bound + 1)
    for p in range(2, bound + 1):
        if naive_is_prime(p) and (naive_is_prime(p + 2) or factor_count(p + 2) == 2):
            chen[p] = 1
    return chen


def main():
    bound = 200
    _, chen = chen_flags(bound)
    naive = naive_chen(bound)
    assert list(chen) == list(naive), [
        i for i in range(bound + 1) if chen[i] != naive[i]
    ]
    print(f"chen oracle cross-check vs trial-division definition: PASS for p <= {bound}")
    print("Chen primes up to 50:", [p for p in range(2, 51) if chen[p]])

    # All-even first-failure check by the naive oracle itself, to 302
    bound2 = 302
    chen2 = naive_chen(bound2)
    failures = []
    for n in range(4, bound2 + 1, 2):
        ok = any(chen2[p] and chen2[n - p] for p in range(2, n // 2 + 1))
        if not ok:
            failures.append(n)
    assert failures == [302], f"oracle all-even failures <= 302: {failures}"
    print(f"oracle all-even Chen-pair check: first failure = 302, failures <= 302 = {failures}: PASS")


if __name__ == "__main__":
    main()
