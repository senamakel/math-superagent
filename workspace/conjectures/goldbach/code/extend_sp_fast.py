#!/usr/bin/env python3
"""
Efficient extended computation of S(p) = least even n whose minimal Goldbach
partition has least prime p.

Key fact (verified in code/verify_mod3_structure.py, and elementary):
  minimal Goldbach primes grow slowly: for n <= 200000, max p(n) ~ 310.
So iterate candidate primes p in increasing order and assign each unassigned
even n = p + q (q prime, q >= p) its minimal prime p(n).  Cost is
O(pi(p_max) * pi(N)) ~ 10^6 for N = 200000.

Then test the data conjecture:
  p > 3, p = 1 (mod 3)  ==>  S(p) = 2 (mod 6)
  p > 3, p = 2 (mod 3)  ==>  S(p) = 4 (mod 6)
and the theorem:
  n = 2 (mod 6) ==> p(n) = 3 or p(n) = 1 (mod 3)
  n = 4 (mod 6) ==> p(n) = 3 or p(n) = 2 (mod 3)
"""
from math import isqrt
import sys, time

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
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 200000
    maxp = int(sys.argv[2]) if len(sys.argv) > 2 else 2000
    t0 = time.time()
    primes = primes_upto(N)
    P = set(primes)
    print(f"N={N}, pi(N)={len(primes)}, sieve {time.time()-t0:.1f}s", file=sys.stderr)
    
    # p(n) = minimal Goldbach prime; None until assigned
    pn = {n: None for n in range(4, N + 1, 2)}
    for p in [p for p in primes if p <= maxp]:
        # q >= p prime, n = p + q <= N; n even only (same parity as p)
        step = 1 if p == 2 else 2
        for q in [q for q in primes if q >= p and p + q <= N]:
            n = p + q
            if n in pn and pn[n] is None:
                pn[n] = p
    
    unassigned = [n for n, p in pn.items() if p is None]
    print(f"unassigned n <= {N} with p(n) > {maxp}: {len(unassigned)}", file=sys.stderr)
    if unassigned:
        print(f"  first: {unassigned[:10]}", file=sys.stderr)
    
    # S(p)
    sp_map = {}
    for n in sorted(pn):
        p = pn[n]
        if p is not None and p not in sp_map:
            sp_map[p] = n
    
    print(f"distinct minimal primes: {len(sp_map)} ({time.time()-t0:.1f}s)", file=sys.stderr)
    
    # ---- Theorem check: mod-3 congruence ----
    bad_thm = 0
    for n, p in pn.items():
        if p is None or p == 3:
            continue
        r6 = n % 6
        if r6 == 2 and p % 3 != 1:
            bad_thm += 1
        if r6 == 4 and p % 3 != 2:
            bad_thm += 1
    print(f"=== Theorem (mod-3 congruence) violations: {bad_thm} ===")
    
    # ---- Conjecture check: S(p) mod 6 ----
    bad_cj = []
    for p in sorted(sp_map):
        if p == 2 or p == 3:
            continue
        sp = sp_map[p]
        if p % 3 == 1 and sp % 6 != 2:
            bad_cj.append((p, sp))
        if p % 3 == 2 and sp % 6 != 4:
            bad_cj.append((p, sp))
    print(f"=== Conjecture (S(p) mod 6) violations: {len(bad_cj)} ===")
    if bad_cj:
        print(f"  first: {bad_cj[:10]}")
    else:
        print(f"  holds for all {len([p for p in sp_map if p > 3])} primes p > 3 with S(p) <= {N}")
    
    # ---- Full sequence output ----
    by_appearance = sorted(sp_map.items(), key=lambda x: x[1])
    print(f"\n=== (p, S(p)) in first-appearance order, {len(by_appearance)} terms ===")
    print("first_appearance_p =", [p for p, _ in by_appearance])
    print("first_appearance_S =", [s for _, s in by_appearance])
    
    # ---- S_min/S_max bound check (OeS empirical) ----
    import math
    bad_min = bad_max = 0
    for p, sp in sp_map.items():
        p4 = p ** 0.4
        Smin = 0.06 * p4 * math.exp(p4)
        Smax = 11.05 * p4 * math.exp(p4)
        if sp < Smin:
            bad_min += 1
        if sp > Smax:
            bad_max += 1
    print(f"\n=== OeS bounds: S_min violations {bad_min}, S_max violations {bad_max} of {len(sp_map)} ===")
    
    # save
    with open(f'/workspace/code/out/seq_sp_eff_{N}.txt', 'w') as f:
        for p, s in by_appearance:
            f.write(f"{p} {s}\n")
    print(f"saved seq_sp_eff_{N}.txt", file=sys.stderr)

if __name__ == '__main__':
    main()