"""Confirm: the max-level Q_k decomposition D(N)=sum_k Q_k(N)3^(N-2k-1)
(only k with exponent 2M-N-1>=0) FAILS to reproduce D(N) at N=12 and N=14.
These are configs with max level M=N/2 (offset k=N/2), excluded because their
exponent would be negative. Print the failing sums vs true D(N)."""
from fractions import Fraction
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

print("Q-decomposition sum test (only M with 2M-N-1>=0 i.e. M>=(N+1)/2):")
for N in sorted(R):
    s = sum(R[N][M] for M in R[N] if 2*M-N-1 >= 0)
    print(f"N={N:2d}: sum={s}  D={D.get(N)}  match={s==D.get(N)}  "
          f"missing={D.get(N,0)-s}")
