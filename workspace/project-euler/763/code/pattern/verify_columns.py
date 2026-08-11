import sympy
from collections import Counter

n = sympy.Symbol('n')

# Build N(N,M) table: N=2..12 from data files, N=13,14 from mhist_13_14.txt
table = {}  # N -> {M: count}
for N in range(2, 13):
    with open(f"data/level_{N}.txt") as f:
        lines = f.read().splitlines()
    c = Counter()
    for ln in lines:
        M = int(ln.split("|")[1].strip())
        c[M] += 1
    assert sum(c.values()) == len(lines)
    table[N] = dict(c)

# N=13,14 from mhist (fresh, never used in fitting)
for N in (13, 14):
    # reuse mhist recomputation from data is impossible (dump only to 12);
    # hardcode the fresh measured values recorded in code/out/mhist_13_14.txt
    table[N] = {7:612,8:9342,9:51678,10:172044,11:393660,12:590490,13:531441} if N==13 else \
               {7:267,8:7122,9:54756,10:237897,11:688905,12:1417176,13:1948617,14:1594323}

def Q(N, M):
    """v = N(N,M)/3^(N-2k-1), k=N-M"""
    k = N - M
    return table[N][M], k

# For each offset k, collect pairs (N, R) where R=N(N,N-k)/3^(N-2k-1)
# over all N where that M appears. Determine polynomial degree via finite differences.
data_by_k = {}
for N in sorted(table):
    for M, cnt in table[N].items():
        k = N - M
        R = sympy.Rational(cnt, 3**(N-2*k-1))
        data_by_k.setdefault(k, []).append((N, R))

"""
# determine degree: finite difference order where values become identically the poly
nmax = max(sorted(data_by_k))
"""
print("offset k:  (N, R=N(N,N-k)/3^(N-2k-1))  ...")
for k in sorted(data_by_k):
    pts = sorted(data_by_k[k])
    vals = [v for _, v in pts]
    # finite differences exact
    diffs = list(vals)
    order = 0
    while diffs and not all(d == diffs[0] for d in diffs):
        diffs = [diffs[i+1]-diffs[i] for i in range(len(diffs)-1)]
        order += 1
    # After first-difference becomes constant, the polynomial degree is that order
    # (number of differencing steps until constant).
    ns = [p for p, _ in pts]
    print(f"k={k}: N-range={min(ns)}..{max(ns)} R-values={sorted([(p,str(v)) for p,v in pts])}")
    print(f"     degree by finite differences: {order} (need {order+1} points; have {len(pts)})")
