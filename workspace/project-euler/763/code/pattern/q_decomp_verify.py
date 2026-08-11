"""Verify max-level decomposition fresh from raw data, collect Q_k(N) values.

R(N,M) = # configs after N divisions with max level M (raw M-histograms).
Claim: for offset k=N-M, R(N,N-k) = Q_k(N) * 3**(N-2k-1) where Q_k is a
degree-k polynomial in N (only meaningful/defined when N-2k-1 >= 0).

We gather R from data/level_N.txt (N=2..12) and code/out/mhist_13_14.txt.
"""
import collections
import os

R = collections.defaultdict(dict)  # R[N][M] = count

# from raw per-config dumps
for N in range(2, 13):
    path = f"data/level_{N}.txt"
    with open(path) as f:
        for line in f:
            parts = line.strip().split("|")
            M = int(parts[1].strip())
            R[N][M] = R[N].get(M, 0) + 1

# from mhist file (fresh N=13,14)
with open("code/out/mhist_13_14.txt") as f:
    for line in f:
        line = line.strip()
        if line.startswith("N="):
            continue
        if "M=" in line:
            # format like: N=13 M=7: 612   (from file)
            pass
# Actually mhist file format: 'N=13 M=7: 612'
with open("code/out/mhist_13_14.txt") as f:
    for line in f:
        line = line.strip()
        if not line.startswith("N=") or "M=" not in line:
            continue
        # e.g. 'N=14 M=8: 7122'
        lhs, rhs = line.split(": ")
        # lhs = 'N=14 M=8'
        tok = lhs.split()
        N = int(tok[0][2:])
        M = int(tok[1][2:])
        R[N][M] = int(rhs)

# sanity: totals match D(N)
D = {2:3,3:9,4:30,5:99,6:336,7:1134,8:3855,9:13086,10:44499,11:151263,
     12:514419,13:1749267,14:5949063}
for N in sorted(R):
    tot = sum(R[N].values())
    print(f"N={N}: total={tot} D={D[N]} match={tot==D[N]}")

# For each (N,M) with k=N-M, exponent e=N-2k-1 = N-2(N-M)-1 = 2M-N-1
# e>=0 <-> M >= (N+1)/2. Q_k = R / 3**e
print("\nQ_k(N) = R(N,N-k)/3**(2M-N-1)  [only where e>=0]")
Q = collections.defaultdict(dict)
for N in sorted(R):
    for M, c in sorted(R[N].items()):
        k = N - M
        e = 2*M - N - 1
        if e >= 0:
            Q[k][N] = c // (3**e)
            rem = c % (3**e)
            if rem != 0:
                print(f"  DIVISIBILITY FAIL k={k} N={N} M={M} c={c} 3**{e}={3**e}")
print()
for k in sorted(Q):
    ns = sorted(Q[k])
    vals = [Q[k][n] for n in ns]
    print(f"k={k}: N={ns} Q_k={vals}")
