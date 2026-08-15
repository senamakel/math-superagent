#!/usr/bin/env python3
"""Exact residue of T(c,p) = sum_{k=0}^{p-1}(c^2+1)^k mod 8, computed exactly
(then reduced), to lock down which (c,p) residue classes can be a square.

Claim to verify:
  * c odd  (c^2+1 = 2 mod 8): T = 7 mod 8 for every odd prime p>=3  -> not a
    square (squares mod 8 are 0,1,4).
  * c even (c^2+1 = 1 mod 4): T mod 8 depends on p mod 4; classify.

All arithmetic exact (Python ints). No floats, no modular-inverse trick that
could fail when r-1 is not invertible -- compute T exactly then take mod 8.
"""


def T_exact(c, p):
    x = c * c + 1
    # (x^p - 1)//(x - 1) -- exact integer, x>=2
    return (x ** p - 1) // (x - 1)


def is_odd_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


SQR8 = {0, 1, 4}

print("=== T(c,p) mod 8 (exact), by c mod 4, p mod 4 ===")
from collections import defaultdict
byclass = defaultdict(set)
for c in range(1, 200):
    for p in range(3, 120):
        if not is_odd_prime(p):
            continue
        cls = (c % 4, p % 4)
        byclass[cls].add(T_exact(c, p) % 8)

for (c4, p4) in sorted(byclass):
    res = sorted(byclass[(c4, p4)])
    sq = [r for r in res if r in SQR8]
    nonsq = [r for r in res if r not in SQR8]
    verdict = "ALL NON-SQUARE" if not sq else f"could-be-square {sq}"
    print(f"  c={c4} mod4, p={p4} mod4: residues {res}  -> {verdict}")

# c odd always?
print("\n=== c odd: is T(c,p) = 7 mod 8 always? ===")
odd_ok = all(T_exact(c, p) % 8 == 7
             for c in range(1, 500, 2) for p in [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37])
print(f"  all odd c in [1,500), sampled primes: T(c,p) mod 8 == 7? {odd_ok}")
