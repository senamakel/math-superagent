"""Compute P_N(x) = sum_k Q_k(N) x^k exactly, where Q_k(N)=R(N,N-k)/3^(N-2k-1),
and D(N)=3^(N-1)*P_N(1/9). Print P_N for N=2..14. Look for structure/recurrence."""
import collections

R = collections.defaultdict(dict)
for N in range(2, 13):
    with open(f"/workspace/data/level_{N}.txt") as f:
        for line in f:
            parts = line.strip().split('|')
            M = int(parts[1].strip())
            R[N][M] = R[N].get(M, 0) + 1
for line in open('/workspace/code/out/mhist_13_14.txt'):
    line = line.strip()
    if line.startswith('N=') and 'M=' in line and 'expected' not in line:
        lhs, val = line.replace(' ', '').split(':')
        N = int(lhs.split('M=')[0].replace('N=', ''))
        M = int(lhs.split('M=')[1])
        R.setdefault(N, collections.Counter())[M] = int(val)

D = {2:3,3:9,4:30,5:99,6:336,7:1134,8:3855,9:13086,10:44499,11:151263,
     12:514419,13:1749267,14:5949063}

# Q_k(N) where exponent e=2M-N-1 >= 0
from fractions import Fraction
P = {}  # N -> dict {k: Fraction}
for N in sorted(R):
    Pd = {}
    for M, c in R[N].items():
        k = N - M
        e = 2*M - N - 1
        if e >= 0:
            Pd[k] = Fraction(c, 3**e)
    P[N] = Pd

for N in sorted(P):
    maxk = max(P[N]) if P[N] else -1
    # polynomial as sum Q_k x^k
    # evaluate at 1/9 and check
    val = sum(P[N][k]*Fraction(1, 9)**k for k in P[N])
    total = 3**(N-1)*val
    coeffs = " ".join(f"Q{k}={P[N][k]}" for k in sorted(P[N]))
    print(f"N={N:2d}: D_check={total==D.get(N)}  P_N: {coeffs}")
