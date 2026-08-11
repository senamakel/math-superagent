#!/usr/bin/env python3
"""Verify the derived exact closed form for n=2:  p(2,L) = L/(2L-40).
Boat0 (pos0) bumps boat1 (pos40) iff v0/v1 > L/(L-40), so
P(bump) = P(v0/v1 > L/(L-40)) = (L-40)/(2L-40) and p(2,L)=1-P(bump)=L/(2L-40).
Check against the brute oracle by high-N Exp(1) MC."""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from brute import outcome_parity

def exact(L):
    from fractions import Fraction as F
    return F(L, 2*L-40)

def mc(n, L, N, seed=7):
    rng = random.Random(seed)
    even = 0
    for _ in range(N):
        v = [rng.expovariate(1.0) for _ in range(n)]
        if outcome_parity(n, L, v) == 0:
            even += 1
    return even/N

if __name__ == '__main__':
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 400000
    for L in (48, 80, 160, 400, 900, 1800, 40000):
        ex = exact(L)
        m = mc(2, L, N, seed=123+L)
        print(f"L={L:6d}  exact p(2,L)={ex} = {float(ex):.6f}   MC={m:.6f}   diff={m-float(ex):.6f}")
