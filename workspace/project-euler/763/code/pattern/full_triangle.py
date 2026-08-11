# Full (N,M) raw triangle and normalized Q_k rows, now including N=13,14.
import collections
from sympy import Rational

# N=2..12 from dumps, 13..14 fresh
base = collections.defaultdict(dict)
for N in range(2,13):
    cnt = collections.Counter()
    with open(f"/workspace/data/level_{N}.txt") as f:
        for line in f:
            line=line.strip()
            if not line: continue
            parts=line.split('|'); cnt[int(parts[1].strip())]+=1
    for M,v in cnt.items(): base[N][M]=v
fresh = {13:{7:612,8:9342,9:51678,10:172044,11:393660,12:590490,13:531441},
         14:{7:267,8:7122,9:54756,10:237897,11:688905,12:1417176,13:1948617,14:1594323}}
for N,hist in fresh.items():
    for M,v in hist.items(): base[N][M]=v

print("Raw triangle N(N,M): rows N=2..14, columns M (increasing)")
for N in sorted(base):
    ms = sorted(base[N])
    print(f"N={N:2d}: " + "  ".join(f"M{m}:{base[N][m]}" for m in ms))

print("\n--- Column ratios along offset k=M-N: from N to N+1 ---")
# normalized Q_k(N)=N(N,N-k)/3^{N-2k-1}
Q = collections.defaultdict(dict)
for N in sorted(base):
    for M,v in base[N].items():
        k=N-M
        if N-2*k-1>=0:
            Q[k][N]=Rational(v,3**(N-2*k-1))
for k in sorted(Q):
    print(f"k={k}: " + ", ".join(f"{N}:{Q[k][N]}" for N in sorted(Q[k])))
