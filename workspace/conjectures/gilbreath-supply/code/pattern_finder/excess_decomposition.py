#!/usr/bin/env python3
"""Decompose E[S(n)^2] structurally to find the arithmetic input that would
prove E[S^2]=O(n) for the primes.

S(n) = sum_{d=2}^{n-1} chi_d(n),  chi_d(n) = (-1)^{T(n,d)}, and
T(n,d) = XOR_{s submask of d} h[n-1-s].

E[S^2] = sum_{d1,d2} E[chi_{d1} chi_{d2}]
       = sum_{d1=d2} 1  +  sum_{d1!=d2} rho(d1,d2)

where rho(d1,d2) = E[(-1)^{T_{d1}}( -1)^{T_{d2}}].  Under iid-uniform h the
diagonal gives (n-2) and cross terms vanish (rho=0 when the submask sets
differ, as they always do for distinct d -- the downset determines d).

For the primes h is DETERMINISTIC, so 'E' is a Cesaro/past-average.  The
cross-term rho(d1,d2) = E_h[(-1)^{T_{d1}}( -1)^{T_{d2}} ] = E[(-1)^{T_{d1} xor T_{d2}}],
a character sum over the SYMMETRIC DIFFERENCE of the two submask windows.
This is precisely an autocorrelation of h read along the binary-submask sets.

We compute, for the real prime h over the measured range, the actual
cross-term contribution:  E[S(n)^2] - (n-2)  =  sum_{d1!=d2} rho(d1,d2).
If this excess is O(1) or slowly growing, then E[S^2] = n-2 + o(n) and the
second moment is a pure 'diagonal' statement - no cross-term growth.  If it is
O(n) or worse, the cross terms are the difficulty.

Also measure: does the excess track something like the morphism/autocorr of h?
"""
import sys
sys.path.insert(0, '/workspace/code')
import numpy as np

# Real prime h: reconstruct from S (we only have S, not h here). Instead use
# the second-moment ratio directly from the E2 capture: Excess vs n-2 is
# already measured.  We compute the empirical excess curve.

val = [int(t) for t in open('/workspace/code/out/excess_E2_30000.txt').read().split()]
S = {}
for i in range(0, len(val), 2):
    S[int(val[i])] = -int(val[i+1])   # S = -E2

print("Excess over uniform: E[S^2]-(n-2), by n (exact integers from E2 capture):")
for n in [100, 200, 400, 800, 1000, 2000, 3000, 4000, 5000, 8000, 10000, 20000, 30000]:
    # empirical 'instantaneous' excess at a single n
    exc = S[n]**2 - (n-2)
    print(f"  n={n}: S(n)^2={S[n]**2}  excess=S^2-(n-2)={exc}  Excess/n={exc/n:.3f}")

# The meaningful statistic: is the cross-term sum of order n, sqrt(n), or O(1)?
# We use the prefix mean of S^2 - (n-2):
print("\nPrefix mean of (S(n)^2-(n-2)) [instantaneous excess at n] vs n:")
for N in [1000, 2000, 4000, 8000, 12000, 20000, 30000]:
    excs = [S[n]**2-(n-2) for n in range(50, N+1) if n-2 > 0]
    print(f"  N={N}: mean instantaneous excess = {np.mean(excs):.3f}  (vs n)")
