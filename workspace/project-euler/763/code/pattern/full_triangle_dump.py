"""Build full R(N,M) max-level triangle and print column sequences + Q_k columns.
Checks: diagonal R(N,N)=3^(N-1); D(N)=sum_M R(N,M).
Also prints, for each fixed max-level M, the column R(N,M) as N varies,
so the solver can look for transfer structure per column.
"""
import collections, glob
from lib.datafiles import sorted_key

R = {}
for path in sorted(glob.glob('/workspace/data/level_*.txt'), key=sorted_key):
    N = int(path.split('level_')[1].split('.')[0])
    c = collections.Counter()
    for line in open(path):
        parts = line.strip().split('|')
        M = int(parts[1].strip())
        c[M] += 1
    R[N] = c
for line in open('/workspace/code/out/mhist_13_14.txt'):
    line = line.strip()
    if line.startswith('N=') and 'M=' in line and 'expected' not in line:
        lhs, val = line.replace(' ', '').split(':')
        N = int(lhs.split('M=')[0].replace('N=', ''))
        M = int(lhs.split('M=')[1])
        R.setdefault(N, collections.Counter())[M] = int(val)

D = {2:3,3:9,4:30,5:99,6:336,7:1134,8:3855,9:13086,10:44499,11:151263,
     12:514419,13:1749267,14:5949063}

print("Full R(N,M) triangle (rows N, columns M):")
maxM = 14
print("   N |", " ".join(f"{m:>9}" for m in range(7, maxM+1)))
for N in sorted(R):
    row = [R[N].get(m, 0) for m in range(7, maxM+1)]
    tot = sum(R[N].values())
    print(f"{N:4d} |", " ".join(f"{v:>9}" for v in row), f"  tot={tot} D={D.get(N)} match={tot==D.get(N)}")

print("\n=== Diagonal R(N,N) vs 3^(N-1) ===")
for N in sorted(R):
    print(f"N={N}: R(N,N)={R[N].get(N)} 3^(N-1)={3**(N-1)} match={R[N].get(N)==3**(N-1)}")

print("\n=== Columns R(N,M) for each fixed M ===")
cols = collections.defaultdict(dict)
for N in sorted(R):
    for M, v in R[N].items():
        cols[M][N] = v
for M in sorted(cols):
    seq = " ".join(f"{N}:{cols[M][N]}" for N in sorted(cols[M]))
    print(f"M={M:2d}: {seq}")
