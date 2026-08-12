#!/usr/bin/env python3
"""Fit Q_k(N) as exact polynomials in N and inspect coefficients/structure."""
from fractions import Fraction
import glob, collections, sympy

def sorted_key(path):
    return int(path.split('level_')[1].split('.')[0])

R = {}
for path in sorted(glob.glob('/workspace/data/level_*.txt'), key=sorted_key):
    N = int(path.split('level_')[1].split('.')[0])
    counts = collections.Counter()
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line: continue
            M = int(line.split('|')[1].strip())
            counts[M] += 1
    R[N] = counts
with open('/workspace/code/out/mhist_13_14.txt') as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith('N=') and 'expected' in line: continue
        if 'M=' in line and 'expected' not in line and 'total' not in line:
            lhs, val = line.replace(' ','').split(':')
            N = int(lhs.split('M=')[0].replace('N=',''))
            M = int(lhs.split('M=')[1])
            R.setdefault(N, collections.Counter())[M] = int(val)

Qcols = collections.defaultdict(dict)
for N in sorted(R):
    for M in sorted(R[N]):
        k = N - M
        if N - 2*k - 1 >= 0:
            Qcols[k][N] = Fraction(R[N][M]) / (3**(N-2*k-1))

n = sympy.symbols('n')
print("Q_k(n) polynomials (interpolate all measured points, exact):")
for k in sorted(Qcols):
    pts = sorted(Qcols[k].items())
    print(f"k={k}: points={pts}")
    if len(pts) >= k+1:
        # fit degree k polynomial through first k+1 points, verify all
        xs = [p[0] for p in pts[:k+1]]
        ys = [p[1] for p in pts[:k+1]]
        poly = sympy.interpolate(list(zip(xs, ys)), n).expand()
        # verify all points
        ok = all(poly.subs(n,N) == Qcols[k][N] for N,_ in pts)
        print(f"   poly={poly}")
        print(f"   verified on {len(pts)} points: {ok}")
