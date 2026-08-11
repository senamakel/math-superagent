#!/usr/bin/env python3
"""Verify the two statement examples by Monte Carlo, and test the
structural hypothesis that the race outcome depends only on the rank order
of w_j = v_j/(L - p_j), not on the speed magnitudes.

w_j ~ Exp(lambda_j), lambda_j = L - 40*j (0-indexed j; lambda = L - p_j).
j catches k (k ahead) before either finishes  <=>  w_j > w_k.
Hypothesis H: the final parity is a function of the permutation sigma
(boats sorted by decreasing w) only.

Run: python3 verify_hypothesis.py [N]
"""
import random, sys
from collections import defaultdict
from brute import outcome_parity, simulate_order, parity_of_new_order

def w_order(n, L, speeds):
    """Return tuple of boat indices sorted by decreasing w_j = v_j/(L-p_j)."""
    w = [speeds[j] / (L - 40.0*j) for j in range(n)]
    return tuple(sorted(range(n), key=lambda j: -w[j]))

def check_consistency(n, L, N, seed=7):
    rng = random.Random(seed)
    buckets = defaultdict(set)
    for _ in range(N):
        speeds = [rng.expovariate(1.0) for _ in range(n)]
        sig = w_order(n, L, speeds)
        par = outcome_parity(n, L, speeds)
        buckets[sig].add(par)
    bad = [(s, p) for s, p in buckets.items() if len(p) > 1]
    print(f"n={n} L={L}: {N} samples, {len(buckets)} distinct w-orders seen, "
          f"{len(bad)} order(s) with inconsistent parity")
    return bad

def mc(n, L, N, seed=1):
    rng = random.Random(seed)
    even = 0
    for _ in range(N):
        speeds = [rng.expovariate(1.0) for _ in range(n)]
        even += outcome_parity(n, L, speeds) == 0
    return even / N

if __name__ == '__main__':
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 150000
    r1 = mc(3, 160, N, seed=11)
    r2 = mc(4, 400, N, seed=12)
    print(f"MC p(3,160)   = {r1:.6f}  (exact 4.15+4/27 = 56/135 = {56/135:.6f})")
    print(f"MC p(4,400)   = {r2:.6f}  (given 0.5107843137)")
    for (n, L) in [(3,160),(4,160),(4,400),(5,400),(5,1800)]:
        check_consistency(n, L, min(N, 60000))