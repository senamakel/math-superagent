"""Test the core lemma of the kummer-lucas-p-adic approach.

Candidate claim: "for any given prime p, the number of (n,k) pairs with the same
v_p(C(n,k)) and same Lucas residue grows at most logarithmically in the size of
the numbers."

If this is false, the mechanism has no engine. We count, for p=2 and p=3,
pairs (n,k), 0<=k<=n<=N, grouped by (v_p(C(n,k)), C(n,k) mod p), and report the
largest class size as N grows. A positive-density class defeats the lemma.
"""
from math import comb
from collections import defaultdict

def vp(n, p):
    c = 0
    while n % p == 0:
        n //= p
        c += 1
    return c

for p in (2, 3):
    print(f"=== prime p={p} ===")
    for N in (50, 100, 200, 400, 800):
        classes = defaultdict(int)
        total = 0
        for n in range(0, N+1):
            for k in range(0, n+1):
                c = comb(n, k)
                key = (vp(c, p), c % p)
                classes[key] += 1
                total += 1
        largest = max(classes.values())
        # fraction of pairs in the largest v_p=0,residue=1 class (the no-carry class)
        frac = largest / total if total else 0
        print(f"  N={N:4d}  total pairs={total:9d}  largest class={largest:9d}  "
              f"largest_class_frac={frac:.4f}  num_classes={len(classes)}")
