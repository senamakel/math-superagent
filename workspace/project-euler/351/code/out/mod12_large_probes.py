"""Break-attempt: does the mod-12 period-4 law hold at n far beyond the
200000-term prefix that suggested it?

Law (proven by parity: phi(k) even for k>=3): for n >= 2,
    H(n) mod 12 == 6  iff  n mod 4 in {1,2},  else 0.
Falsifying term: any n >= 2 with (H(n) mod 12) != 6*((n+1)//2 mod 2).

A063985(n) computed exactly by Chai Wah Wu's recursion (verified against the
sieve at probes up to 10^8); H = 6*A.  Probe n up to 10^8, including all
n = 10^k + r near each power of 10 and random large n.
"""
from functools import lru_cache
import random

@lru_cache(maxsize=None)
def A063985_rec(n):
    if n == 0:
        return 0
    c, j = 0, 2
    k1 = n // j
    while k1 > 1:
        j2 = n // k1 + 1
        c += (j2 - j) * (k1 * (k1 + 1) - 2 * A063985_rec(k1) - 1)
        j, k1 = j2, n // j2
    return (2 * n + c - j) // 2

random.seed(351)
probes = set()
for k in range(2, 9):                     # 10^2 .. 10^8
    base = 10 ** k
    for r in (0, 1, 2, 3, 10**k - 1, 10**k - 2, 7, 8):
        if 2 <= base + r <= 10**8:
            probes.add(base + r)
probes |= {random.randint(2, 10**8) for _ in range(30)}
probes |= {10**8}

bad = []
for n in sorted(probes):
    A = A063985_rec(n)
    H6 = A                       # H(n)/6 == A(n)
    law = (H6 % 2) == (((n + 1) // 2) % 2)     # H mod 12 == 6*(ceil(n/2) mod 2)
    if not law:
        bad.append((n, A, H6 % 2))
print(f"probes: {len(probes)}  violations: {len(bad)}")
if bad:
    print("first violations:", bad[:5])
else:
    print("mod-12 law holds at every probe up to 10^8 "
          "(incl. n=10^8: H(10^8) mod 12 =", (6 * (A063985_rec(10**8) % 2)) % 12, ")")
