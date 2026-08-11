"""Analyze bivariate structure P_N(x) = sum_k Q_k(N) x^k, so
D(N) = 3^{N-1} P_N(1/9). Look for a pattern/recurrence in N.
"""
import collections

R = collections.defaultdict(dict)
for N in range(2, 13):
    with open(f"data/level_{N}.txt") as f:
        for line in f:
            parts = line.strip().split("|")
            M = int(parts[1].strip())
            R[N][M] = R[N].get(M, 0) + 1
with open("code/out/mhist_13_14.txt") as f:
    for line in f:
        line = line.strip()
        if not line.startswith("N=") or "M=" not in line:
            continue
        lhs, rhs = line.split(": ")
        tok = lhs.split()
        N = int(tok[0][2:]); M = int(tok[1][2:])
        R[N][M] = int(rhs)

D = {2:3,3:9,4:30,5:99,6:336,7:1134,8:3855,9:13086,10:44499,11:151263,
     12:514419,13:1749267,14:5949063}

# collect Q_k
Q = collections.defaultdict(dict)
for N in sorted(R):
    for M, c in sorted(R[N].items()):
        k = N - M; e = 2*M - N - 1
        if e >= 0:
            Q[k][N] = c // (3**e)

# P_N(x): build poly coeffs (index k -> coeff Q_k(N))
from fractions import Fraction
for N in sorted(R):
    maxk = max(k for k in Q if N in Q[k])
    coeffs = [(k, Q[k][N]) for k in range(maxk+1) if N in Q[k]]
    print(f"N={N}: P_N coeffs (k:Q_k) = {coeffs}")

# Check leading coefficients: Q_k leading coeff = 1/k! ?
print("\nLeading coefficients check (fit Q_k as poly in N, get leading coeff):")
import numpy as np
for k in sorted(Q):
    ns = sorted(Q[k])
    if len(ns) < k+1:
        print(f"k={k}: need {k+1} pts, have {len(ns)}  (NOT full degree yet)"); continue
    vals = [Q[k][n] for n in ns]
    # fit degree-k poly
    c = np.polyfit(ns[-k-1:], vals[-k-1:], k)
    lead = c[0]
    from fractions import Fraction
    from decimal import Decimal
    # express as fraction approximation
    f = Fraction(Decimal(str(lead))).limit_denominator(1000000)
    expected = Fraction(1, 1)
    for i in range(1, k+1):
        expected *= Fraction(1, i)
    print(f"k={k}: leading coeff ~ {f}, 1/k! = {expected}, match={f==expected}")
