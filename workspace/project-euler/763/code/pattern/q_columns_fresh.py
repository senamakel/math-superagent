# Extend the Q_k(N) column analysis with FRESH histogram data at N=13,14.
# Model: # configs after N divisions with max level M (offset k=N-M) satisfies
#   N(N, N-k) = Q_k(N) * 3^(N-2k-1),  Q_k a polynomial of degree k in N.
# Test: collect Q_k(N) exact rationals over ALL N for each k, including the
# fresh N=13,14 points, and check finite differences vanish after k levels
# (i.e. Q_k is a degree-k polynomial).
from fractions import Fraction
import glob

# Build (N, M) count table from data/level_N.txt and mhist_13_14.txt
hist = {}  # N -> {M: count}

for path in sorted(glob.glob('data/level_*.txt'), key=lambda p: int(p.split('_')[1].split('.')[0])):
    N = int(path.split('_')[1].split('.')[0])
    c = {}
    for line in open(path):
        line = line.strip()
        if not line:
            continue
        parts = line.split('|')
        M = int(parts[1].strip())
        c[M] = c.get(M, 0) + 1
    # sanity: total == D(N)
    hist[N] = c
    print(f"N={N} total={sum(c.values())}")

# N=13,14 from mhist file
for line in open('code/out/mhist_13_14.txt'):
    line = line.strip()
    if not line:
        continue
    if line.startswith('N=') and 'M=' not in line:
        pass
    if 'M=' in line:
        # parse "N=13 M=7: 612"
        import re
        m = re.match(r'N=(\d+) M=(\d+): (\d+)', line)
        if m:
            N, M, cnt = int(m.group(1)), int(m.group(2)), int(m.group(3))
            hist.setdefault(N, {})[M] = cnt

# Build Q_k(N) table
# Q_k(N) = N(N,N-k) / 3^(N-2k-1)
from collections import defaultdict
Q = defaultdict(dict)  # k -> {N: Fraction}
for N in sorted(hist):
    for M, cnt in hist[N].items():
        k = N - M
        exp = N - 2*k - 1
        if exp < 0:
            continue
        Q[k][N] = Fraction(cnt) / Fraction(3**exp)

print("\n=== Q_k(N) table (exact rationals) ===")
for k in sorted(Q):
    pts = sorted(Q[k])
    print(f"k={k}: ", {N: str(Q[k][N]) for N in pts})

print("\n=== finite-difference degree check for each column ===")
for k in sorted(Q):
    pts = sorted(Q[k])
    vals = [Q[k][N] for N in pts]
    # take differences up to 6 levels
    level = list(vals)
    degrees = []
    for d in range(1, 8):
        level = [level[i+1]-level[i] for i in range(len(level)-1)]
        if all(v == 0 for v in level):
            degrees.append(d)
            break
        if all(v == 0 for v in level) is False and len(level) <= 3:
            pass
    # count non-zero of last difference
    print(f"k={k}: {len(pts)} points {pts}")
    # print successive difference levels and how many remain
    lvl = list(vals)
    for d in range(1, 6):
        lvl = [lvl[i+1]-lvl[i] for i in range(len(lvl)-1)]
        print(f"    diff level {d}: nonzero={sum(1 for v in lvl if v!=0)}, vals={lvl}")
    print()
