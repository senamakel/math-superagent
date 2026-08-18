#!/usr/bin/env python3
"""
Closed form of the mod-3 bias in D(x;p) (minimal Goldbach prime frequency).

From the exact congruence:
  n = 2 (mod 6), p(n) != 3  =>  p(n) = 1 (mod 3)      [and n-3 prime gives p(n)=3]
  n = 4 (mod 6), p(n) != 3  =>  p(n) = 2 (mod 3)
  n = 0 (mod 6): no residue constraint.

So among even n <= x with n = 2 (mod 6) and n - 3 not prime, ALL minimal
partitions have minimal prime = 1 (mod 3); among n = 4 (mod 6) with n-3 not
prime, ALL have p = 2 (mod 3).  The residual bias in the p=1 class comes from
the n = 0 (mod 6) numbers, where minimal primes can be 1 or 2 mod 3.

Closed form:  #(n<=x, n=2 mod 6, minimal prime > 3, p=1 mod 3) is EXACTLY
  #{even n <= x : n = 2 (mod 6), n - 3 composite}
  (with n-3 = 1 excluded, i.e. n = 4),  because every such n has ALL
  non-3 partitions in the 1-mod-3 class.

Check this exact identity numerically, and measure the 0-mod-6 contribution.
"""
from math import isqrt
from collections import Counter
import sys

def primes_upto(n):
    sieve = bytearray(b'\x01') * (n + 1)
    sieve[0] = 0
    if n >= 1:
        sieve[1] = 0
    for i in range(2, isqrt(n) + 1):
        if sieve[i]:
            sieve[i*i:n+1:i] = b'\x00' * ((n - i*i)//i + 1)
    return [i for i, v in enumerate(sieve) if v]

def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 50000
    primes = primes_upto(N)
    primes_set = set(primes)
    
    pmin = {}
    for n in range(4, N + 1, 2):
        for p in range(2, n//2 + 1):
            if p in primes_set and (n - p) in primes_set:
                pmin[n] = p
                break
    
    # Counts by (n mod 6, p(n) mod 3), p(n) > 3
    C = Counter()
    for n, p in pmin.items():
        if p > 3:
            C[(n % 6, p % 3)] += 1
    
    print(f"=== Contingency: (n mod 6, minimal-prime mod 3), n <= {N} ===")
    print(f"{'n%6':>4} {'p%3=1':>8} {'p%3=2':>8}")
    for r6 in (0, 2, 4):
        print(f"{r6:>4} {C[(r6,1)]:>8} {C[(r6,2)]:>8}")
    
    # Exact identity: for n = 2 (mod 6), count of n with n-3 composite (and
    # n-3 >= 5, i.e. n >= 8) must equal C[(2,1)].
    # n-3 composite: n-3 not in primes_set and n-3 != 1.  Note n-3 = n-3 is
    # even when n = 2 mod 6?  n = 2 mod 6 => n even, n-3 odd; could be prime
    # or composite or 1 (n=4).
    c21 = C[(2, 1)]
    comp = sum(1 for n in range(8, N + 1, 6) if (n - 3) not in primes_set)
    print(f"\nC[(2,1)] = {c21};  #(n<=N, n=2 mod 6, n>=8, n-3 composite) = {comp}")
    print(f"identity holds: {c21 == comp}")
    
    # And C[(2,2)] must be 0
    print(f"C[(2,2)] = {C[(2,2)]} (must be 0)")
    
    # C[(4,1)] must be 0
    print(f"C[(4,1)] = {C[(4,1)]} (must be 0)")
    
    # 0 mod 6: total in each residue
    c0 = C[(0,1)] + C[(0,2)]
    print(f"\n0-mod-6 numbers: p=1: {C[(0,1)]}, p=2: {C[(0,2)]} (total {c0})")

if __name__ == '__main__':
    main()