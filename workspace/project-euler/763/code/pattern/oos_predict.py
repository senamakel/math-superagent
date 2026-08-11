# DECISIVE test: fit Q_0..Q_5 polynomials using ONLY N=2..12 data,
# then predict N(N,M) for M=N-k at fresh N=13,14 and reconstruct D(N).
# This checks the column-polynomial model truly OUT-OF-SAMPLE.
from sympy import Rational, symbols, interpolate, simplify
import collections

n = symbols('n')

# build Q_k(N) from N<=12 only
base = collections.defaultdict(dict)
for N in range(2, 13):
    cnt = collections.Counter()
    with open(f"/workspace/data/level_{N}.txt") as f:
        for line in f:
            line=line.strip()
            if not line: continue
            parts=line.split('|'); cnt[int(parts[1].strip())]+=1
    for M,v in cnt.items(): base[N][M]=v

Q = collections.defaultdict(dict)
for N in sorted(base):
    for M,v in base[N].items():
        k=N-M
        if N-2*k-1>=0:
            Q[k][N]=Rational(v,3**(N-2*k-1))

# fit each k as a degree-k polynomial from available N<=12 points
poly = {}
for k in sorted(Q):
    pts = sorted(Q[k].items())
    xs=[Rational(p[0]) for p in pts]
    ys=[p[1] for p in pts]
    # fit polynomial of degree = (len-1) through all available points
    poly[k] = simplify(interpolate(list(zip(xs,ys)), n))
    print(f"Q_{k} (fit over N<={max(xs)}): {poly[k]}")

# Fresh N=13,14 histograms
fresh = {13:{7:612,8:9342,9:51678,10:172044,11:393660,12:590490,13:531441},
         14:{7:267,8:7122,9:54756,10:237897,11:688905,12:1417176,13:1948617,14:1594323}}

print("\nOUT-OF-SAMPLE prediction (fit on N<=12 only) at N=13,14:")
okall=True
for N, hist in fresh.items():
    predD = 0
    for M, vtrue in hist.items():
        k=N-M
        if k in poly:
            # predict N(N,M)=Q_k(N)*3^{N-2k-1}
            pred = poly[k].subs(n,N)*3**(N-2*k-1)
            match = (pred==Rational(vtrue))
            predD += pred
        else:
            predD += vtrue  # unknown deeper column -> use true (unavoidable)
            match = True
    # D(N) prediction: full sum needs columns we cannot predict; report partial
    pred_known = sum(poly[k].subs(n,N)*3**(N-2*k-1) for k in poly if (N-k) in hist)
    known = sum(vtrue for M,vtrue in hist.items() if (N-M) in poly)
    print(f"N={N}: model-predicted (known columns) sum={pred_known}, true-sum of those columns={known}, match={pred_known==known}")
    print(f"      full D_true={sum(hist.values())}")
    # show per-column match for the columns we CAN predict
    for M in sorted(hist):
        k=N-M
        if k in poly:
            pred = poly[k].subs(n,N)*3**(N-2*k-1)
            if pred != Rational(hist[M]):
                print(f"        MISMATCH M={M} k={k}: pred={pred} true={hist[M]}")
                okall=False

print("\nAll predicted columns match true:", okall)
