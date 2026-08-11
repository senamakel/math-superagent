# Extract full triangular array Q[k][N] = N(N,N-k)/3^(N-2k-1) for all k.
# N(N,M)=count of configs with max level M.  offset k=N-M>=0.
import collections
from sympy import Rational

T = {}
for N in range(2, 13):
    cnt = collections.Counter()
    with open(f"/workspace/data/level_{N}.txt") as f:
        for line in f:
            line=line.strip()
            if not line: continue
            parts=line.split('|')
            cnt[int(parts[1].strip())]+=1
    T[N]=cnt

# Q[k][N] = N(N,N-k)/3^(N-2k-1)
# build dict k -> {N: Q}
Qk = collections.defaultdict(dict)
for N in sorted(T):
    for M, v in T[N].items():
        k = N-M
        if N-2*k-1 >= 0:
            Qk[k][N] = Rational(v, 3**(N-2*k-1))

maxk = max(Qk)
print("k:  N -> Q_k(N)  (rows over available N)")
for k in range(0, maxk+1):
    if k in Qk:
        row = sorted(Qk[k].items())
        s = ", ".join(f"N={n}:{q}" for n,q in row)
        print(f"k={k}: {s}")

# save full triangular array to file for OEIS-style analysis
print("\n--- Triangular array Q_k(N) by (row=N, col=k) ---")
for N in sorted(T):
    row = []
    for k in range(0, N):  # M from N-k
        M = N-k
        if M in T[N]:
            v = T[N][M]
            q = Rational(v, 3**(N-2*k-1))
            row.append(str(q))
        else:
            row.append(".")
    print(f"N={N}: " + "  ".join(row))
