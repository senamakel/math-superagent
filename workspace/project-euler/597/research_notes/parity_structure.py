#!/usr/bin/env python3
"""Explore the structure of the Torpids bump-race parity.

Questions:
 (1) Does the parity (even/odd) depend only on the ORDER of a finite set of
     exponential-ratio comparisons (i.e., v_i/v_j vs constants) ?
 (2) Reproduce p(3,160)=56/135 and p(4,400)=0.5107843137 by high-N Exp MC
     with the corrected parity engine.
 (3) First check: is P(v_i/v_j > c) = 1/(1+c) for iid Exp(1)? (memoryless
     exact-integration kernel).
"""
import random, math
from fractions import Fraction as F
from brute import outcome_parity

def ratio_prob(c):
    """P(v1 > c*v2) for v1,v2 iid Exp(1). Analytic: integral P(v1>c v2) =
    int e^{-c v} e^{-v} dv = 1/(1+c)."""
    return 1.0/(1.0+c)

def mc_parity(N, n, L, seed=7):
    rng = random.Random(seed)
    even=0
    for _ in range(N):
        v=[rng.expovariate(1.0) for _ in range(n)]
        if outcome_parity(n,L,v)==0: even+=1
    return even/N

if __name__=='__main__':
    print("P(v_i/v_j>c)=1/(1+c) checks:")
    for c in (0.5,1.0,2.0,3.0):
        print(f"  c={c}: analytic={ratio_prob(c):.6f}")
    N=200000
    print(f"MC p(3,160)  = {mc_parity(N,3,160):.6f}  (exact 56/135={56/135:.6f})")
    print(f"MC p(4,400)  = {mc_parity(N,4,400):.6f}  (given 0.5107843137)")
