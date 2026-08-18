#!/usr/bin/env python3
"""
Test two sourced claims from Oliveira e Silva's verification page against
freshly computed head-of-distribution data (n <= N).

Claim A (OeS page, ~line 211): "there exists a distinct difference of
behavior in the values of D(x;p) when p is a multiple of three plus one
(white dots) and when it is not (yellow dots)."
  D(x;p) = relative frequency of p as the minimal Goldbach prime among
  even n <= x.  Test: split minimal primes by p mod 3, compare frequencies.

Claim B (OeS page, ~line 200): for their empirical data,
  S_min(p) = 0.06 p^0.4 e^{p^0.4}  <=  S(p)  <=  S_max(p) = 11.05 p^0.4 e^{p^0.4},
and p is well approximated by 0.33 (log S(p) log log S(p))^2.
  Test both on the head data.

Both are empirical claims by the source; this run checks them over fresh,
independently computed data at the head of the distribution (not the same
regime OeS used — they had p up to ~10^4, S(p) up to 4e18).
"""
from math import isqrt, log, exp
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
    
    # minimal prime p(n) for each even n <= N
    pn = {}
    for n in range(4, N + 1, 2):
        found = None
        for p in range(2, n//2 + 1):
            if p in primes_set and (n - p) in primes_set:
                found = p
                break
        pn[n] = found  # found is not None (verification to 4e18, tiny N)
    
    # D(x;p) frequencies by p mod 3, for odd primes p > 3
    from collections import Counter
    freq = Counter(pn[n] for n in pn)
    # restrict to odd primes p != 3 (the mod-3 claim is about those)
    cnt_1 = sum(c for p, c in freq.items() if p > 3 and p % 3 == 1)
    cnt_2 = sum(c for p, c in freq.items() if p > 3 and p % 3 == 2)
    total_odd = sum(c for p, c in freq.items() if p > 3)
    print(f"=== Claim A: D(x;p) by p mod 3, x = {N} ===")
    print(f"even n in [4, {N}]: {len(pn)}")
    print(f"minimal partitions with p > 3: {total_odd}")
    print(f"  p ≡ 1 (mod 3): {cnt_1}  ({100*cnt_1/max(total_odd,1):.2f}%)")
    print(f"  p ≡ 2 (mod 3): {cnt_2}  ({100*cnt_2/max(total_odd,1):.2f}%)")
    
    # also: among the set of DISTINCT minimal primes, mod-3 split
    distinct = sorted(freq)
    d1 = [p for p in distinct if p > 3 and p % 3 == 1]
    d2 = [p for p in distinct if p > 3 and p % 3 == 2]
    print(f"distinct minimal primes p > 3: {len([p for p in distinct if p > 3])}")
    print(f"  of which p ≡ 1 mod 3: {len(d1)}, p ≡ 2 mod 3: {len(d2)}")
    
    # Frequency-weighted mean S(p) by residue class
    sp_map = {}
    for n in range(4, N + 1, 2):
        p = pn[n]
        if p not in sp_map:
            sp_map[p] = n
    from statistics import mean
    s1 = [sp_map[p] for p in distinct if p > 3 and p % 3 == 1]
    s2 = [sp_map[p] for p in distinct if p > 3 and p % 3 == 2]
    print(f"mean S(p) p≡1: {mean(s1):.1f}  vs p≡2: {mean(s2):.1f}")
    
    # ---- Claim B: S_min / S_max bounds ----
    print(f"\n=== Claim B: OeS empirical bounds on S(p) ===")
    bad_min = bad_max = 0
    for p in sorted(sp_map):
        sp = sp_map[p]
        p4 = p ** 0.4
        Smin = 0.06 * p4 * exp(p4)
        Smax = 11.05 * p4 * exp(p4)
        if sp < Smin:
            bad_min += 1
        if sp > Smax:
            bad_max += 1
    print(f"p range: {min(sp_map)}..{max(sp_map)}, S(p) range: {min(sp_map.values())}..{max(sp_map.values())}")
    print(f"violations of S_min: {bad_min}, violations of S_max: {bad_max}, out of {len(sp_map)}")
    
    # 0.33 (log S log log S)^2 approximation to p
    print(f"\n=== p ~ 0.33 (log S(p) log log S(p))^2 ===")
    errs = []
    for p in sorted(sp_map):
        sp = sp_map[p]
        if sp <= 16:  # log log S needs S > e
            continue
        approx = 0.33 * (log(sp) * log(log(sp))) ** 2
        errs.append((abs(approx - p)/p, p, sp, approx))
    errs.sort()
    print(f"median relative error: {errs[len(errs)//2][0]:.3f}")
    print(f"worst: {errs[-1]}")

if __name__ == '__main__':
    main()