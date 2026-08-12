#!/usr/bin/env python3
"""Verify: #distinct level-histograms at N == OEIS A186085(N) for N=2..14.
Distinct histograms from raw data (N=2..12) + bitmask run (N=13,14 in
code/out/distinct_hist_counts.txt).
A186085 via the Heinz b(n,i) recurrence (smooth compositions / 1D sandpiles):
b(0,1)=1; b(n,i)=b(n-i,i-1)+b(n-i,i)+b(n-i,i+1); a(n)=b(n-1,1) for n>=1.
"""
from functools import lru_cache
import glob, collections

@lru_cache(maxsize=None)
def b(n, i):
    if n == 0:
        return 1 if i == 1 else 0
    if n < 0 or i < 1:
        return 0
    return b(n-i, i-1) + b(n-i, i) + b(n-i, i+1)

def a186085(n):
    if n == 0: return 1
    return b(n-1, 1)

A = {n: a186085(n) for n in range(2, 16)}

# distinct histograms per N from data files
counts = {}
for path in glob.glob('/workspace/data/level_*.txt'):
    N = int(path.split('level_')[1].split('.')[0])
    hs = set()
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line: continue
            hs.add(line.split('|')[0].strip())
    counts[N] = len(hs)

# N=13,14 from the bitmask run
with open('/workspace/code/out/distinct_hist_counts.txt') as f:
    for line in f:
        line = line.strip()
        if not line: continue
        parts = line.split()
        if parts[0].startswith('N') and len(parts) == 2:
            N = int(parts[0].split()[0].split('_')[0][1:]) if False else int(parts[0].replace('N',''))
            counts[N] = int(parts[1])

all_ok = True
for N in range(2, 15):
    a = A[N]
    c = counts.get(N)
    ok = (c == a)
    all_ok = all_ok and ok
    print(f"N={N}: distinct_hist={c}  A186085({N})={a}  match={ok}")
print("\nALL N=2..14 match:", all_ok)
print("First falsifier (would need N=15): A186085(15)=", A[15], "(N=15 unreachable by BFS)")
