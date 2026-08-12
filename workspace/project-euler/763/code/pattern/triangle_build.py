#!/usr/bin/env python3
"""Build the max-level triangle R(N,M) and its column/diagonal sequences.

R(N,M) = # distinct reachable configs after N divisions with max level M.
From data/level_N.txt (N=2..12) + code/out/mhist_13_14.txt (N=13,14).
Also Q_k(N) = R(N,N-k)/3^(N-2k-1).
Print the diagonal R(N,N), and each column R(N,N-k) raw and as Q_k.
"""
import glob, collections, re, sys

hist = {}
for path in sorted(glob.glob('data/level_*.txt'), key=lambda p: int(p.split('_')[1].split('.')[0])):
    N = int(path.split('_')[1].split('.')[0])
    c = collections.Counter()
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line: continue
            c[int(line.split('|')[1].strip())] += 1
    hist[N] = c

for line in open('code/out/mhist_13_14.txt'):
    m = re.match(r'N=(\d+) M=(\d+): (\d+)', line.strip())
    if m:
        N, M, cnt = int(m.group(1)), int(m.group(2)), int(m.group(3))
        hist.setdefault(N, collections.Counter())[M] = cnt

import json
print("R(N,M) triangle (N rows, M columns)")
AllN = sorted(hist)
maxM = max(max(c) for c in hist.values())
print("N\\M " + " ".join(f"{m:>9d}" for m in range(3, maxM+1)))
for N in AllN:
    row = [hist[N].get(m, 0) for m in range(3, maxM+1)]
    print(f"{N:2d} " + " ".join(f"{v:>9d}" for v in row))

print("\nDiagonal R(N,N):", [hist[N].get(N, 0) for N in AllN if N in hist and N in hist[N]])

print("\nColumns by offset k=N-M; Q_k(N)=R(N,N-k)/3^(N-2k-1)")
from fractions import Fraction
for k in range(0, 5):
    pts = {}
    for N in AllN:
        if N-k in hist[N] and N-2*k-1 >= 0:
            pts[N] = Fraction(hist[N][N-k], 3**(N-2*k-1))
    print(f"k={k}: R_col={ {N: hist[N][N-k] for N in pts} }")
    print(f"     Q   ={ {N: str(pts[N]) for N in pts} }")
