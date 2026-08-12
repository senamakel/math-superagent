"""Sieve-based check of PE241 structural regularities up to N (fast numpy)."""
import sys
import numpy as np
from collections import defaultdict

def run(N):
    # sigma sieve
    sigma = np.zeros(N + 1, dtype=np.int64)
    for d in range(1, N + 1):
        sigma[d::d] += d

    num = 2 * sigma
    valid = np.zeros(N + 1, dtype=bool)
    for n in range(1, N + 1):
        if num[n] % n == 0 and (num[n] // n) % 2 == 1:
            valid[n] = True

    ns = np.nonzero(valid)[0]
    print("qualifying n up to", N, ":", list(ns))

    perk = defaultdict(list)
    for n in ns:
        k = (2 * sigma[n] // n - 1) // 2
        a = 0
        t = n
        while t % 2 == 0:
            t //= 2
            a += 1
        perk[k].append(int(n))
    print("\nper-k (abundancy k+1/2) counts:")
    for k in sorted(perk):
        print(f"  k={k} (abund {2*k+1}/2): {len(perk[k])} members {perk[k]}")

if __name__ == "__main__":
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 3 * 10**7
    run(N)
