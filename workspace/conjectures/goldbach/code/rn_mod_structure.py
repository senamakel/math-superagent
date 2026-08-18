#!/usr/bin/env python3
"""
Test for mod-3 / mod-6 structure in r(n) = number of Goldbach partitions
(A045917), the partition-count sequence — to see if the mod-3 structure
extends to partition counts, or is confined to the minimal-prime function.

r(n) (n even) counts all pairs {p, q} with p <= q prime, p + q = n.
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
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 100000
    primes = primes_upto(N)
    P = set(primes)
    r = {}
    for n in range(4, N + 1, 2):
        cnt = sum(1 for p in range(2, n//2 + 1)
                  if p in P and (n - p) in P)
        r[n] = cnt
    
    # Distribution of r(n) mod 2 by n mod 6
    c = Counter()
    for n, v in r.items():
        c[(n % 6, v % 2)] += 1
    print(f"=== r(n) mod 2 by n mod 6, n <= {N} ===")
    for r6 in (0, 2, 4):
        print(f"n%6={r6}: r even {c[(r6,0)]}, r odd {c[(r6,1)]}")
    
    # r(n) mod 3
    c3 = Counter()
    for n, v in r.items():
        c3[(n % 6, v % 3)] += 1
    print(f"\n=== r(n) mod 3 by n mod 6 ===")
    for r6 in (0, 2, 4):
        print(f"n%6={r6}: r%3=0:{c3[(r6,0)]} 1:{c3[(r6,1)]} 2:{c3[(r6,2)]}")
    
    # Do zeros of r(n) (Goldbach counterexamples) exist?  (they must not, n <= 4e18)
    zeros = [n for n, v in r.items() if v == 0]
    print(f"\nzeros of r(n) up to {N}: {zeros}")

if __name__ == '__main__':
    main()