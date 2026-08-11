# Test Q_k(N) conjectures at FRESH out-of-sample points N=13, N=14.
# These were never in the N=2..12 fit data. If Q_k survives here, it is strong.
from sympy import Rational, symbols
n = symbols('n')
Q = {
    0: Rational(1),
    1: (n-3),
    2: (n-5)*(n+2)/2,
    3: (n**3 - 73*n + 168)/6,
}

# fresh M-histograms N=13,N=14 (from code/out/mhist_13_14.txt)
fresh = {
    13: {7:612, 8:9342, 9:51678, 10:172044, 11:393660, 12:590490, 13:531441},
    14: {7:267, 8:7122, 9:54756, 10:237897, 11:688905, 12:1417176, 13:1948617, 14:1594323},
}

ok = True
for N, hist in fresh.items():
    for M, v in hist.items():
        k = N - M
        if k in Q:
            pred = Q[k].subs(n, N) * 3**(N-2*k-1)
            match = (Rational(v) == pred)
            print(f"N={N} M={M} k={k}: v={v} pred={pred} {'MATCH' if match else 'MISMATCH'}")
            if not match: ok=False
print("\nAll in-sample-Q checks at fresh N=13,14:", ok)

# Also check the diagonal + subdiagonal count formulas at N=13,14
print("\nDiagonal count(M=N)=3^(N-1):")
for N, hist in fresh.items():
    v = hist[N]
    print(f"  N={N}: {v} vs 3^{N-1}={3**(N-1)} match={v==3**(N-1)}")
print("Sub-diag count(M=N-1)=(N-3)3^(N-3):")
for N, hist in fresh.items():
    v = hist[N-1]
    pred = (N-3)*3**(N-3)
    print(f"  N={N}: {v} vs {(N-3)}*3^{N-3}={pred} match={v==pred}")
