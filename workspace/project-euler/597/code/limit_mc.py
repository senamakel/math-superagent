#!/usr/bin/env python3
"""MC for the large-L limit p(n,inf) = pure-race final-order parity.
At L large enough that all bumps complete before any finish, p(n,L) -> pure
race parity. Compare with exact limits 1/2, 7/18, 19/36 for n=2,3,4."""
import random, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from brute import outcome_parity

def mc(n, L, N, seed):
    rng = random.Random(seed)
    even = 0
    for _ in range(N):
        v = [rng.expovariate(1.0) for _ in range(n)]
        if outcome_parity(n, L, v) == 0:
            even += 1
    return even / N

if __name__ == '__main__':
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 400000
    for n in range(2, 10):
        for L in (10**6, 10**9):
            print(f"n={n} L={L}  p={mc(n,L,N,seed=100+n):.6f}")
