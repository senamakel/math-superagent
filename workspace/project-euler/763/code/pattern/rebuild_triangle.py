#!/usr/bin/env python3
"""Reconstruct the full R(N,M) triangle (N=2..14) from raw data:
R(N,M) = number of distinct reachable configs at N divisions with max level M.

In-sample: data/level_*.txt lines 'hist | M | bbox'. The histogram's max level
M is stored explicitly. Cross-check: M == len(hist values)-1 (hist includes a_0).
Out-of-sample: code/out/per_hist_mult_13_14.txt, hist includes a_0, last nonzero
is 3, M = len(hist)-1 (strip trailing zeros with care: a_M=3 then zeros padded).

Sanity checks: sum_M R(N,M) == D(N); diagonal R(N,N) == 3^(N-1).
"""
import glob, collections

def sorted_key(p):
    return int(p.split('level_')[1].split('.')[0])

D = {2:3,3:9,4:30,5:99,6:336,7:1134,8:3855,9:13086,10:44499,11:151263,
     12:514419,13:1749267,14:5949063}

R = collections.defaultdict(dict)   # [N][M] = count

# in-sample
for path in sorted(glob.glob('data/level_*.txt'), key=sorted_key):
    n = sorted_key(path)
    for line in open(path):
        hist, M, bbox = line.rstrip().split('|')
        R[n][int(M)] = R[n].get(int(M), 0) + 1
# out-of-sample
for line in open('code/out/per_hist_mult_13_14.txt'):
    line = line.strip()
    if not line.startswith('N=') or 'mult=' not in line: continue
    n = int(line[2:line.index('hist=')].strip())
    h = line.index('hist='); m_i = line.index('mult=')
    hist_str = line[h+5:m_i].strip()
    vals = [int(x) for x in hist_str.split()]
    while vals and vals[-1] == 0: vals.pop()
    M = len(vals) - 1
    # each file line is ONE distinct histogram with mult=configs realizing it
    R[n][M] = R[n].get(M, 0) + mval

print("R(N,M) triangle (M rows increase downward; sum over M == D(N)):")
ok = True
for n in sorted(R):
    Ms = sorted(R[n])
    total = sum(R[n].values())
    if total != D[n]:
        ok = False
        print(f"  N={n}: SUM MISMATCH {total} vs D={D[n]}")
    print(f"  N={n:>2} {R[n]}")
    if R[n].get(n, None) != 3**(n-1):
        ok = False
        print(f"   -> diagonal R({n},{n}) = {R[n].get(n)} != 3^{n-1} = {3**(n-1)}")
print("\nAll sums match D(N) and all diagonal entries == 3^(N-1):", ok)

# Q_k table: Q_k(N) = R(N,N-k)/3^(N-2k-1), for N-2k-1 >= 0 and N-k >= 1
print("\nQ_k(N) = R(N,N-k)/3^(N-2k-1)  over valid N:")
for k in range(0, 7):
    cols = []
    for n in sorted(R):
        if n - 2*k - 1 < 0: continue
        if n - k not in R[n]: continue
        cols.append((n, R[n][n-k], 3**(n-2*k-1)))
    if cols:
        print(f"  k={k}: " + "  ".join(f"N={n}:{v}/{p}={v//p}" for n, v, p in cols))