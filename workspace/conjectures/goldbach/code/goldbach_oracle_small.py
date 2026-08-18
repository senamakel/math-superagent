"""Naive oracle required by the method policy.
Objects: even n > 2; primes p,q; representation n=p+q.
complexity_class: exponential (oracle only); oracle_bound: 100000.
The real checker is_prime/goldbach_partitions and is retained as the small-instance oracle.
"""
from math import isqrt


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d <= isqrt(n):
        if n % d == 0:
            return False
        d += 2
    return True


def goldbach_partitions(n: int):
    return [(p, n-p) for p in range(2, n+1) if is_prime(p) and is_prime(n-p)]


def satisfies_goldbach(n: int) -> bool:
    return n > 2 and n % 2 == 0 and bool(goldbach_partitions(n))


if __name__ == "__main__":
    examples = {4: [(2, 2)], 2: [], 1: []}
    for n, expected in examples.items():
        got = goldbach_partitions(n)
        assert got == expected, (n, got, expected)
    assert all(satisfies_goldbach(n) for n in range(4, 1001, 2))
    print("worked examples: 4 ->", goldbach_partitions(4), "; 2 ->", goldbach_partitions(2), "; 1 ->", goldbach_partitions(1))
    print("oracle check: all even n in [4,1000] pass")
