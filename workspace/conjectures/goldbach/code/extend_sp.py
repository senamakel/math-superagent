#!/usr/bin/env python3
"""
Extend the S(p) first-appearance computation to much larger n, and test
Oliveira e Silva's sourced mod-3 structure conjecture exactly.

Definition (OeS, sweet.ua.pt/tos/goldbach.html): S(p) = least even n whose
minimal Goldbach partition has least prime p.  The minimal Goldbach partition
is the one with the smallest possible prime p(n) = p(n;1).

Also test:
  1. whether S(p) mod 3 correlates with p mod 3 over the head of the
     distribution (OeS observed D(x;p) differs by p mod 3),
  2. whether r(n) parity / residues obey any periodic pattern over a long run.
"""
from math import isqrt
import sys, time

def primes_upto(n):
    """Sieve of Eratosthenes, bytearray.  Exact."""
    sieve = bytearray(b'\x01') * (n + 1)
    if n >= 0:
        sieve[0] = 0
    if n >= 1:
        sieve[1] = 0
    for i in range(2, isqrt(n) + 1):
        if sieve[i]:
            sieve[i*i:n+1:i] = b'\x00' * ((n - i*i)//i + 1)
    return [i for i, v in enumerate(sieve) if v]

def minimal_goldbach_prime(n, primes_set):
    """Smallest prime p in a Goldbach partition of n; 0 if none."""
    if n < 4 or n % 2:
        return 0
    for p in range(2, n//2 + 1):
        if p in primes_set and (n - p) in primes_set:
            return p
    return 0

def main():
    limit = int(sys.argv[1]) if len(sys.argv) > 1 else 50000
    print(f"=== S(p) extension up to n={limit} ===", file=sys.stderr)
    t0 = time.time()
    
    primes = primes_upto(limit)
    primes_set = set(primes)
    print(f"primes <= {limit}: {len(primes)}  ({time.time()-t0:.1f}s)", file=sys.stderr)
    
    # First appearance of each minimal prime
    sp_map = {}
    minprime_by_n = {}
    for n in range(4, limit + 1, 2):
        p = minimal_goldbach_prime(n, primes_set)
        minprime_by_n[n] = p
        if p > 0 and p not in sp_map:
            sp_map[p] = n
    
    sorted_p = sorted(sp_map.keys())
    sp_vals = [sp_map[p] for p in sorted_p]
    
    print(f"\n=== S(p) for all {len(sorted_p)} minimal primes up to n={limit} ===")
    print(f"p    S(p)   (count of distinct minimal primes)")
    for p, sp in zip(sorted_p, sp_vals):
        print(f"{p:6d} {sp:10d}")
    print(f"\ntotal distinct minimal primes up to {limit}: {len(sorted_p)}")
    
    # The head of the sequence, in order of FIRST APPEARANCE (this is the
    # natural order for a sequence: the values as they are discovered)
    by_appearance = sorted(sp_map.items(), key=lambda x: x[1])
    print(f"\n=== First-appearance order: (p, S(p)) ===")
    for p, sp in by_appearance:
        print(f"({p}, {sp})")
    print(f"\nfirst_appearance_p = {[p for p,_ in by_appearance]}")
    print(f"first_appearance_S = {[sp for _,sp in by_appearance]}")
    
    # --- Test 1: mod-3 structure of S(p) values ---
    # OeS observed D(x;p) behaves differently for p = 1 (mod 3) vs p = 2 (mod 3).
    # Check whether the S(p) VALUES show a mod-3 bias.
    p1 = [(p, sp) for p, sp in sp_map.items() if p % 3 == 1]
    p2 = [(p, sp) for p, sp in sp_map.items() if p % 3 == 2]
    p0 = [(p, sp) for p, sp in sp_map.items() if p % 3 == 0]
    print(f"\n=== Mod-3 breakdown (distinct minimal primes, n<={limit}) ===")
    print(f"p ≡ 0 (mod 3): {len(p0)}  (e.g. p=3 only for small primes)")
    print(f"p ≡ 1 (mod 3): {len(p1)}")
    print(f"p ≡ 2 (mod 3): {len(p2)}")
    
    import statistics
    if p1 and p2:
        s1 = [sp for _, sp in p1]; s2 = [sp for _, sp in p2]
        print(f"S(p) mean for p≡1: {statistics.mean(s1):.1f},  p≡2: {statistics.mean(s2):.1f}")
        print(f"S(p) max  for p≡1: {max(s1)},  p≡2: {max(s2)}")
    
    # --- Test 2: are the minimal primes all ≡ 1 mod 3 after a point? ---
    # (If so, the OeS "white dots" = p ≡ 1 mod 3 might dominate the tail.)
    big = [p for p in sorted_p if p > 100]
    big1 = [p for p in big if p % 3 == 1]
    big2 = [p for p in big if p % 3 == 2]
    print(f"\n=== Minimal primes p > 100: {len(big)} total, {len(big1)} ≡1 mod 3, {len(big2)} ≡2 mod 3 ===")
    print(f"list (sorted): {big}")
    
    # --- Test 3: r(n) over the same range, saved for sequence tools ---
    r_vals = []
    for n in range(4, limit + 1, 2):
        cnt = 0
        for p in range(2, n//2 + 1):
            if p in primes_set and (n-p) in primes_set:
                cnt += 1
        r_vals.append(cnt)
    print(f"\n=== r(n) terms ({len(r_vals)}), n=4..{limit} ===")
    print(repr(r_vals))
    
    # Save to files
    with open(f'/workspace/code/out/seq_rn_{limit}.txt', 'w') as f:
        f.write('\n'.join(str(v) for v in r_vals))
    with open(f'/workspace/code/out/seq_sp_{limit}.txt', 'w') as f:
        f.write('\n'.join(f"{p} {sp}" for p, sp in by_appearance))
    print(f"\nwrote seq_rn_{limit}.txt and seq_sp_{limit}.txt", file=sys.stderr)
    print(f"total time {time.time()-t0:.1f}s", file=sys.stderr)

if __name__ == '__main__':
    main()