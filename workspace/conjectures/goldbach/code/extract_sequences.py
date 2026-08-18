#!/usr/bin/env python3
"""
Extract and analyze integer sequences from Goldbach computation data.

Sequences:
1. r(n): number of Goldbach partitions for even n (partition count)
2. g(n): the smallest prime in a Goldbach partition of n (minimal Goldbach prime)
3. The OeS "least prime" sequence: primes p where S(p) is defined
4. S(p): the smallest n whose minimal Goldbach partition has least prime p
"""
from math import isqrt
import sys

def primes_upto(n):
    """Sieve of Eratosthenes."""
    sieve = bytearray(b'\x01') * (n + 1)
    sieve[0:2] = b'\x00\x00'
    for i in range(2, isqrt(n) + 1):
        if sieve[i]:
            step = i
            start = i * i
            sieve[start:n+1:step] = b'\x00' * ((n - start)//step + 1)
    return [i for i, v in enumerate(sieve) if v]

def goldbach_partition_count(n, primes_set):
    """Count Goldbach partitions of even n: p+q=n with p<=q, both prime."""
    if n < 4 or n % 2:
        return 0
    cnt = 0
    for p in range(2, n//2 + 1):
        if p in primes_set and (n - p) in primes_set:
            cnt += 1
    return cnt

def minimal_goldbach_prime(n, primes_set):
    """Smallest prime p in a Goldbach partition of n; 0 if none."""
    if n < 4 or n % 2:
        return 0
    for p in range(2, n//2 + 1):
        if p in primes_set and (n - p) in primes_set:
            return p
    return 0

def main():
    limit = 2000
    if len(sys.argv) > 1:
        limit = int(sys.argv[1])
    
    print(f"=== Goldbach analysis up to n={limit} ===", file=sys.stderr)
    
    primes = primes_upto(limit)
    primes_set = set(primes)
    print(f"Prime count: {len(primes)}", file=sys.stderr)
    
    # Sequence 1: r(n) for even n
    r_vals = []
    for n in range(4, limit + 1, 2):
        r_vals.append(goldbach_partition_count(n, primes_set))
    
    print("\n=== SEQUENCE 1: r(n) = Goldbach partition count for even n ===")
    print(f"n range: 4 to {limit} (step 2)")
    print(f"Terms ({len(r_vals)}):")
    print(r_vals)
    
    # Sequence 2: g(n) = minimal Goldbach prime
    g_vals = []
    for n in range(4, limit + 1, 2):
        g_vals.append(minimal_goldbach_prime(n, primes_set))
    
    print("\n=== SEQUENCE 2: g(n) = minimal prime in Goldbach partition of n ===")
    print(f"Terms ({len(g_vals)}):")
    print(g_vals)
    
    # Sequence 3: first occurrence of each minimal prime p
    # S(p) = smallest n where minimal Goldbach partition has least prime p
    # Derived from the OeS table structure
    sp_map = {}
    for n in range(4, limit + 1, 2):
        p = minimal_goldbach_prime(n, primes_set)
        if p > 0 and p not in sp_map:
            sp_map[p] = n
    
    # Sort by p
    sorted_p = sorted(sp_map.keys())
    sp_vals = [sp_map[p] for p in sorted_p]
    
    print("\n=== SEQUENCE 3: S(p) minimal n for each minimal prime p ===")
    print(f"p values ({len(sorted_p)}): {sorted_p}")
    print(f"S(p) values: {sp_vals}")
    
    # Find the largest p values (the "top" ones)
    # Sort by S(p) descending
    by_sp = sorted(sp_map.items(), key=lambda x: -x[1])
    print("\n=== Top 20 by S(p) (largest n where a new minimal prime appears) ===")
    for p, sp in by_sp[:20]:
        print(f"  p={p:5d}, S(p)={sp:8d}")
    
    # Sequence 4: All primes that appear as minimal primes, in order of first appearance
    first_appearance_order = sorted(sp_map.items(), key=lambda x: x[1])
    print("\n=== SEQUENCE 4: Primes in order of first appearance as minimal Goldbach prime ===")
    print("(p, first_n)")
    for p, n in first_appearance_order[:30]:
        print(f"  p={p:5d}, first_n={n:8d}")
    print(f"  ... ({len(first_appearance_order)} total)")
    
    # Sequence 5: r(n) for n where a new minimal prime appears
    print("\n=== SEQUENCE 5: r(n) at first-appearance n ===")
    for p, n in first_appearance_order[:30]:
        r = goldbach_partition_count(n, primes_set)
        print(f"  p={p:5d}, n={n:8d}, r(n)={r:4d}")
    print(f"  ... ({len(first_appearance_order)} total)")
    
    # Write the sequences to files for the sequence tools
    with open('/workspace/code/out/seq_rn.txt', 'w') as f:
        f.write('\n'.join(str(v) for v in r_vals))
    with open('/workspace/code/out/seq_gn.txt', 'w') as f:
        f.write('\n'.join(str(v) for v in g_vals))
    with open('/workspace/code/out/seq_sp.txt', 'w') as f:
        f.write('\n'.join(str(v) for v in sp_vals))
    with open('/workspace/code/out/seq_p_sorted.txt', 'w') as f:
        f.write('\n'.join(str(v) for v in sorted_p))
    
    print(f"\nFiles written to code/out/", file=sys.stderr)

if __name__ == '__main__':
    main()