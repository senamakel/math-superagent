#!/usr/bin/env python3
"""Aggregate the (N,M) max-level triangle fresh from raw data files.
Also print Q_k(N) = R(N,N-k)/3^(N-2k-1) columns as exact rationals.
"""
from fractions import Fraction
import glob, collections
from lib.datafiles import sorted_key

# collect R(N,M): max-level M histograms
R = {}  # N -> {M: count}
for path in sorted(glob.glob('/workspace/data/level_*.txt'), key=sorted_key):
    N = int(path.split('level_')[1].split('.')[0])
    counts = collections.Counter()
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line: continue
            parts = line.split('|')
            M = int(parts[1].strip())
            counts[M] += 1
    R[N] = counts

# add N=13,14 from mhist
with open('/workspace/code/out/mhist_13_14.txt') as f:
    for line in f:
        line = line.strip()
        if not line: continue
        if line.startswith('N=') and 'M=' in line and 'expected' not in line:
            # form: N=13 M=7: 612
            lhs, val = line.replace(' ','').split(':')
            N = int(lhs.split('M=')[0].replace('N=',''))
            M = int(lhs.split('M=')[1])
            R.setdefault(N, collections.Counter())[M] = int(val)

print("Raw max-level triangle R(N,M):")
for N in sorted(R):
    row = R[N]
    # also print Q_k for each offset k
    entries = []
    for M in sorted(row):
        entries.append(f"M={M}:{row[M]}")
    print(f"N={N:2d}  " + "  ".join(entries))

print("\nQ_k(N)=R(N,N-k)/3^(N-2k-1) table (exact fractions):")
# collect Q columns
Qcols = collections.defaultdict(dict)  # k -> {N: Fraction}
for N in sorted(R):
    for M in sorted(R[N]):
        k = N - M
        if N - 2*k - 1 >= 0:
            v = Fraction(R[N][M]) / (3**(N-2*k-1))
            Qcols[k][N] = v

for k in sorted(Qcols):
    seq = " ".join(f"{N}:{Qcols[k][N]}" for N in sorted(Qcols[k]))
    print(f"k={k}: {seq}")
