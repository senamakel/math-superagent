# Probe the bottom of the (N,M) triangle: min-M per N, and whether the
# Q_k = count/3^(N-2k-1) form extends into negative exponents (large k).
from fractions import Fraction
import glob, re
from collections import defaultdict

hist = {}
for path in sorted(glob.glob('data/level_*.txt'), key=lambda p: int(p.split('_')[1].split('.')[0])):
    N = int(path.split('_')[1].split('.')[0])
    c = {}
    for line in open(path):
        line=line.strip()
        if not line: continue
        M=int(line.split('|')[1].strip()); c[M]=c.get(M,0)+1
    hist[N]=c
for line in open('code/out/mhist_13_14.txt'):
    line=line.strip()
    if 'M=' in line:
        m=re.match(r'N=(\d+) M=(\d+): (\d+)',line)
        if m:
            hist.setdefault(int(m.group(1)),{})[int(m.group(2))]=int(m.group(3))

print("min-M per N (and whether near N/2):")
for N in sorted(hist):
    Mmin=min(hist[N]); Mmax=max(hist[N])
    print(f"  N={N}: M in [{Mmin},{Mmax}]  (N/2={N/2})")

# Check negative-exponent rows: does count/3^(N-2k-1) look like it could be a
# polynomial-in-N column too? Print Q_k (allowing negative exp -> Fraction).
print("\nFull Q_k including negative-exponent rows:")
Q=defaultdict(dict)
for N in sorted(hist):
    for M,cnt in hist[N].items():
        k=N-M; exp=N-2*k-1
        Q[k][N]=Fraction(cnt)/Fraction(3**exp)
for k in sorted(Q):
    pts=sorted(Q[k])
    print(f"  k={k}: {[(n,str(Q[k][n])) for n in pts]}")
