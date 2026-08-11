# Fit Q_4, Q_5 polynomials using fresh N=13,14 data, and check the (N,M) model
# reproduces D(13), D(14) exactly from the Q-k polynomial decomposition.
from sympy import Rational, symbols, interpolate
n = symbols('n')

# Combined Q_k(N) = N(N,N-k)/3^(N-2k-1)  for all N=2..14
# from data dumps (N=2..12) and fresh histograms (N=13,14)
import collections
base = collections.defaultdict(dict)
for N in range(2,13):
    cnt = collections.Counter()
    with open(f"/workspace/data/level_{N}.txt") as f:
        for line in f:
            line=line.strip()
            if not line: continue
            parts=line.split('|'); cnt[int(parts[1].strip())]+=1
    for M,v in cnt.items():
        base[N][M]=v
fresh = {13:{7:612,8:9342,9:51678,10:172044,11:393660,12:590490,13:531441},
         14:{7:267,8:7122,9:54756,10:237897,11:688905,12:1417176,13:1948617,14:1594323}}
for N,hist in fresh.items():
    for M,v in hist.items():
        base[N][M]=v

# Build Q_k table
Q_tab = collections.defaultdict(dict)  # k -> {N: Q}
for N in sorted(base):
    for M,v in base[N].items():
        k=N-M
        if N-2*k-1>=0:
            Q_tab[k][N]=Rational(v,3**(N-2*k-1))

for k in sorted(Q_tab):
    row = Q_tab[k]
    print(f"k={k}: N->Q: {dict(sorted(row.items()))}")

# Fit each k as polynomial in N, report degree needed (finite differences constant?)
def poly_degree(vals):
    v=list(vals)
    d=0
    while len(set(v))>1:
        v=[b-a for a,b in zip(v,v[1:])]
        d+=1
    return d

print("\nDegrees needed:")
for k in sorted(Q_tab):
    print(f"  k={k}: degree {poly_degree(list(Q_tab[k].values()))}, npoints={len(Q_tab[k])}")

# Fit Q_4, Q_5
for k in [4,5]:
    pts = sorted(Q_tab[k].items())
    xs=[Rational(p[0]) for p in pts]; ys=[p[1] for p in pts]
    poly = interpolate(list(zip(xs,ys)), n)
    import sympy as sp
    poly = sp.simplify(poly)
    print(f"\nQ_{k}(N) interpolated: {poly}")
