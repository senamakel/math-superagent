#!/usr/bin/env python3
"""Probe the second-moment structure of S(n) for the SUPPLY fold.

S(n) = sum_{d=2}^{n-1} (-1)^{T(n,d)}, T(n,d) = XOR over submasks s of d of
h[n-1-s]  (reversed-window digital submask XOR; the canonical fold cell).

Structural conjecture (orthonormal-coordinate): for iid uniform h, the cells
T(n,d) are pairwise uncorrelated because the submask sets of distinct d are
distinct (downset determines d), so the symmetric difference is nonempty and
E[(-1)^{T1}(-1)^{T2}] = E[(-1)^{T1 xor T2}] = 0.  Hence
E[S(n)^2] = sum_{d1,d2} delta_{d1,d2} = n-2  EXACTLY, and
Var(nu2/n) = Var(S)/(4n^2) = (n-2)/(4n^2) ~ 1/(4n).

We verify this against random iid h (Monte Carlo) and measure the empirical
prime ratio E[S(n)^2]/(n-2) to see how far the primes are from the exact
uniform prediction.

Exact arithmetic via the SOS submask-product path from lib.supply_fold.
"""
import sys, math
sys.path.insert(0, '/workspace/code')
from lib.supply_fold import s_sos

def random_h(n, p=0.5):
    import random
    return [1 if random.random() < p else 0 for _ in range(n)]

# ---- Uniform-h Monte Carlo: average S(n)^2 over trials ----
def mc_uniform_second_moment(n, trials):
    tot = 0.0
    for _ in range(trials):
        h = random_h(n)
        S, _ = s_sos(n, h)
        tot += S * S
    return tot / trials

print("Uniform-h Monte Carlo E[S(n)^2] vs exact n-2:")
for n in [16, 32, 64, 128, 256]:
    est = mc_uniform_second_moment(n, trials=400)
    print(f"  n={n}: MC E[S^2]={est:.2f}   exact n-2={n-2}   ratio={est/(n-2):.4f}")

# ---- Prime-h empirical second moment ----
# S(n) from the E2 file: S(n) = -E2(n)
E2 = [int(tok) for tok in open('/workspace/code/out/excess_E2_30000.txt').read().split()]
S = lambda n: -E2[2*(n-2)]   # file rows "n value" pairs; index 2*(n-2)
# but simpler: build dict
Sd = {}
it = iter(E2)
for n in range(2, 30001):
    Sd[n] = E2[2*(n-2)+1] * -1   # E2 stored, S = -E2
# actually E2 list is flat [n1, v1, n2, v2, ...]
vals = [int(tok) for tok in open('/workspace/code/out/excess_E2_30000.txt').read().split()]
Sval = {}
for i in range(0, len(vals), 2):
    Sval[int(vals[i])] = -int(vals[i+1])  # S = -E2

print("\nPrime-h empirical E[S(n)^2] over prefix, ratio to (n-2):")
import numpy as np
csum = 0.0
for N in [1000, 4000, 10000, 20000, 30000]:
    s2sum = sum(Sval[n]**2 for n in range(50, N+1))
    cnt = N - 49
    # average ratio of S(n)^2/(n-2)
    avg_ratio = np.mean([Sval[n]**2/(n-2) for n in range(50, N+1)]) if N>=50 else 0
    print(f"  N={N}: mean S^2 over prefix={s2sum/cnt:.1f}   mean(S^2/(n-2))={avg_ratio:.3f}")
