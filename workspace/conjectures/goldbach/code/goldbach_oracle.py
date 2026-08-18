#!/usr/bin/env python3
"""Naive oracle for binary Goldbach, used only on small bounds.

Statement checked: Goldbach.IsGoldbach in code/lean/Lib/Statement.lean.
Complexity: O(B^2/log B) elementary primality checks in the naive version;
space O(B) for the prime table. This is an oracle, not the full-size method.
"""

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True

def naive_goldbach(n: int) -> bool:
    return any(is_prime(p) and is_prime(n-p) for p in range(2, n))

def sieve(limit: int) -> bytearray:
    a = bytearray(b'\x01') * (limit + 1)
    a[:2] = b'\x00\x00'
    for p in range(2, int(limit**0.5) + 1):
        if a[p]:
            a[p*p:limit+1:p] = b'\x00' * (((limit-p*p)//p)+1)
    return a

def fast_goldbach(n: int, prime: bytearray) -> bool:
    return any(prime[p] and prime[n-p] for p in range(2, n//2+1))

def main() -> None:
    examples = {4: True, 6: True, 8: True, 10: True, 12: True, 2: False}
    for n, expected in examples.items():
        got = naive_goldbach(n)
        assert got == expected, (n, got, expected)
    limit = 1000
    prime = sieve(limit)
    for n in range(4, limit+1, 2):
        assert naive_goldbach(n) == fast_goldbach(n, prime), n
    print('worked examples:', {n: naive_goldbach(n) for n in examples})
    print('naive/fast agree for every even n in [4,1000]')

if __name__ == '__main__':
    main()
