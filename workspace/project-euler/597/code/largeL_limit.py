#!/usr/bin/env python3
"""True large-L limit p(n,L) as L->inf by MC on the real Exp(1) dynamic
(brute engine). Compares against the flawed order-only enumeration to check
whether order-only dependence holds (it should NOT: magnitudes matter)."""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from brute import outcome_parity

def mc(n, L, N, seed=7):
    rng = random.Random(seed)
    even = 0
    for _ in range(N):
        v = [rng.expovariate(1.0) for _ in range(n)]
        if outcome_parity(n, L, v) == 0:
            even += 1
    return even/N

if __name__ == '__main__':
    N = int(sys.argv[1]) if len(sys.argv)>1 else 300000
    for n in (3,4,5,6):
        for L in (10**5, 10**8):
            m = mc(n, L, N, seed=31+n)
            print(f"n={n} L={L}  p={m:.6f}")
