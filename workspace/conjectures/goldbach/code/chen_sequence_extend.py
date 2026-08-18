"""
Extend the all-even Chen-pair failure census and test derived structure.

Definitions (exact):
  Chen prime p: p prime and p+2 prime or semiprime.
  n fails  <=>  no prime pair (p,q), p<=q, p+q=n, both Chen.

Derived characterization for n == 2 (mod 6)  (checked against the 27-term
census in this program):
  - any prime pair p+q=n with n==2 mod 6 has p==q==1 (mod 3)  [both odd and
    both 1 mod 3], EXCEPT the pair (3, n-3) when n-3 is prime (3 is Chen).
  - for p == 1 (mod 3): p Chen  <=>  (p+2)/3 is prime   (p+2 = 3u, u>=3;
    3u prime impossible, 3u semiprime <=> u prime).
  - hence with B = {u prime : 3u-2 prime}, and m = (n+4)/3, the (1,1) pairs
    give: n = p+q <=> m = u+v with u,v in B.
  So for n == 2 (mod 6): n fails <=> n-3 is not a Chen prime AND m not in B+B.
  For n == 0, 4 (mod 6): census-only (no known congruence obstruction).

Output: failure list to bound, m-space list, residue analysis mod 6/30/10,
cross-check of the 27-term <= 10^6 census.
"""
import sys, time
from math import isqrt
from bisect import bisect_right

def sieve(limit):
    prime = bytearray(b'\x01') * (limit + 1)
    if limit >= 0: prime[0] = 0
    if limit >= 1: prime[1] = 0
    for p in range(2, isqrt(limit) + 1):
        if prime[p]:
            prime[p*p:limit+1:p] = b'\x00' * (((limit - p*p)//p) + 1)
    return prime

def chen_flags(bound):
    prime = sieve(bound + 2)
    semiprime = bytearray(bound + 3)
    small_primes = [p for p in range(2, isqrt(bound + 2) + 1) if prime[p]]
    all_primes = [p for p in range(2, bound + 3) if prime[p]]
    for f in small_primes:
        for g in all_primes:
            prod = f * g
            if prod > bound + 2: break
            semiprime[prod] = 1
    chen = bytearray(bound + 1)
    for p in range(2, bound + 1):
        chen[p] = prime[p] and (prime[p + 2] or semiprime[p + 2])
    return prime, chen

def census(bound):
    """All-even failure census. Returns failures (list), and counts by n mod 6."""
    prime, chen = chen_flags(bound)
    chen_list = [p for p in range(2, bound + 1) if chen[p]]
    failures = []
    mod0_fail = mod2_fail = mod4_fail = 0
    for n in range(4, bound + 1, 2):
        hi = bisect_right(chen_list, n // 2)
        ok = False
        for idx in range(hi):
            p = chen_list[idx]
            if chen[n - p]:
                ok = True; break
        if not ok:
            failures.append(n)
            if n % 6 == 0: mod0_fail += 1
            elif n % 6 == 2: mod2_fail += 1
            else: mod4_fail += 1
    return failures, mod0_fail, mod2_fail, mod4_fail

def main():
    B = int(sys.argv[1]) if len(sys.argv) > 1 else 10**6
    t0 = time.perf_counter()
    failures, m0, m2, m4 = census(B)
    print(f"bound: {B}")
    print(f"failures: {len(failures)}")
    print(f"by n mod 6 -> n==0: {m0}, n==2: {m2}, n==4: {m4}")
    print(f"first 50: {failures[:50]}")
    print(f"last 10: {failures[-10:]}")
    ms = [(n + 4) // 3 for n in failures]
    print(f"m = (n+4)/3 first 50: {ms[:50]}")
    print(f"m mod 10 histogram: {sorted({x: ms.count(x) for x in set(m % 10 for m in ms)}.items())}")
    from collections import Counter
    print(f"n mod 30 residues: {sorted({n % 30 for n in failures})}")
    print(f"n mod 30 histogram: {sorted(Counter(n % 30 for n in failures).items())}")
    print(f"wall_time_seconds: {time.perf_counter() - t0:.3f}")

if __name__ == '__main__':
    main()
