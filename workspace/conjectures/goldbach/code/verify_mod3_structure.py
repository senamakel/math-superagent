#!/usr/bin/env python3
"""
Verify the exact congruence structure of Goldbach partitions by n mod 6.

Claim (elementary, to be formalised in Lean):
  For even n with n = 2 (mod 6), every prime p in every Goldbach partition
  n = p + q satisfies: p = 3, or p = 1 (mod 3)  [equivalently q = 3 or q = 1 mod 3].
  Proof: primes > 3 are +-1 mod 3; p + q = n = 2 mod 3 forces both 1, or one
  of them 0 mod 3 which forces it to equal 3.
  For even n with n = 4 (mod 6): same with 1 <-> 2.
  For n = 0 (mod 6): no constraint (one prime 1, the other 2 mod 3, or a 3).

Check numerically over n <= N, and check the minimal-Goldbach-prime version:
  n = 2 (mod 6), p(n) != 3  ==>  p(n) = 1 (mod 3)
  n = 4 (mod 6), p(n) != 3  ==>  p(n) = 2 (mod 3)
"""
from math import isqrt
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
    
    # Full-partition check: for every even n, every partition {p,q}, p,q > 3:
    #   n = 2 mod 6  =>  p = q = 1 mod 3
    #   n = 4 mod 6  =>  p = q = 2 mod 3
    #   n = 0 mod 6  =>  {p mod 3, q mod 3} = {1, 2}
    bad_part = []
    for n in range(4, N + 1, 2):
        r6 = n % 6
        for p in range(2, n//2 + 1):
            q = n - p
            if p in primes_set and q in primes_set and p > 3 and q > 3:
                rp, rq = p % 3, q % 3
                if r6 == 2 and not (rp == 1 and rq == 1):
                    bad_part.append((n, p, q))
                if r6 == 4 and not (rp == 2 and rq == 2):
                    bad_part.append((n, p, q))
                if r6 == 0 and not ({rp, rq} == {1, 2}):
                    bad_part.append((n, p, q))
    print(f"=== Full-partition mod-3 structure, n <= {N} ===")
    print(f"violations: {len(bad_part)}")
    if bad_part[:5]:
        print("first violations:", bad_part[:5])
    
    # Minimal-prime version
    bad_min = []
    for n in range(4, N + 1, 2):
        r6 = n % 6
        pmin = None
        for p in range(2, n//2 + 1):
            if p in primes_set and (n - p) in primes_set:
                pmin = p
                break
        if pmin is None or pmin == 3:
            continue
        if r6 == 2 and pmin % 3 != 1:
            bad_min.append((n, pmin))
        if r6 == 4 and pmin % 3 != 2:
            bad_min.append((n, pmin))
    print(f"=== Minimal-Goldbach-prime version ===")
    print(f"violations: {len(bad_min)}")
    if bad_min[:5]:
        print("first violations:", bad_min[:5])
    
    # And the exceptional partition {3, n-3}: when does the minimal prime
    # equal 3?  exactly when n - 3 is prime.
    ex3 = sum(1 for n in range(4, N + 1, 2) if (n - 3) in primes_set and n - 3 >= 3)
    print(f"n <= {N} with p(n) = 3 (n - 3 prime): {ex3}")

if __name__ == '__main__':
    main()