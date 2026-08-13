#!/usr/bin/env python3
"""Extended sub-progression search for EXSCET finite sub-coverings of
n=840K+1 (open class r=1).  Reuses the Salez 7-equation enumeration from
search_subprogression.py but over a wider grid of M and residues, and
aggregates the FOUND verified families.

Reports, for each modulus M, the set of residues c (K≡c mod M) covered, and
the exact union density over the lcm period.
"""
import sys, time
from math import gcd
from collections import defaultdict
from sympy import Symbol, simplify, Poly, isprime

sys.path.insert(0, '/workspace/code')
from search_subprogression import (quad_residue, is_poly_int_positive,
                                   verify_and_emit, try_14a, try_14b, try_14c,
                                   try_15a, try_15b, try_15c, try_15d,
                                   prime_factors)

k = Symbol('k')


def main():
    t0 = time.time()
    found = []
    seen = set()
    # Wider M grid: all M <= 60 plus primes and selected composites.
    Ms = set()
    for M in range(1, 61):
        Ms.add(M)
    for p in [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
              73, 79, 83, 89, 97, 101]:
        Ms.add(p)
    Ms = sorted(Ms)
    attempts = 0
    for M in Ms:
        a = 840 * M
        for j in range(M):
            b = 1 + 840 * j
            if gcd(b, M) != 1:
                continue
            if quad_residue(b, a):
                continue
            attempts += 1
            try_14a(a, b, found, seen)
            try_14b(a, b, found, seen)
            try_14c(a, b, found, seen)
            try_15a(a, b, found, seen)
            try_15b(a, b, found, seen)
            try_15c(a, b, found, seen)
            try_15d(a, b, found, seen)
    print(f"{len(found)} verified families over {attempts} (a,b) candidates "
          f"in {time.time()-t0:.1f}s", flush=True)

    # Aggregate residue coverage per modulus M (of K in n=840K+1)
    per = defaultdict(set)
    for (a, b, x, y, z, info) in found:
        M = a // 840
        r = b % 840
        assert r == 1, (a, b, r)
        c = (b - 1) // 840   # K ≡ c mod M
        per[M].add(c)
    total_res = 0
    total_mod = 0
    for M in sorted(per):
        nres = len(per[M])
        total_res += nres
        total_mod += M
        print(f"M={M:4}: {sorted(per[M])}  -> {nres}/{M} = {nres/M:.4f}")
    print(f"\nsum over moduli of covered-residue fraction: "
          f"{sum(len(s)/m for m,s in per.items()):.4f} "
          f"(upper bound on union density; overlaps due to CRT make union "
          f"potentially smaller)")

    # Exact union density over lcm period
    if per:
        L = 1
        for m in per:
            L = L // gcd(L, m) * m
        if L <= 5_000_000:
            covered = 0
            for K in range(L):
                if any(K % m in s for m, s in per.items()):
                    covered += 1
            print(f"EXACT union density over period L={L}: "
                  f"{covered}/{L} = {covered/L:.6f}")
        else:
            print(f"period L={L} too large for exact count; skipping")

    # Save families for downstream use
    import json
    fam = [{'a': a, 'b': b, 'M': a // 840, 'res': (b - 1) // 840,
            'x': str(x), 'y': str(y), 'z': str(z), 'shape': info}
           for (a, b, x, y, z, info) in found]
    json.dump(fam, open('code/out/subprogression_families.json', 'w'), indent=1)
    print(f"saved {len(fam)} families to code/out/subprogression_families.json")


if __name__ == '__main__':
    main()
