# Verify exact closed forms for offset columns Q_k(N) in N(N,N-k) = Q_k(N)*3^(N-2k-1)
from sympy import Rational, symbols

n = symbols('n')
Q = {
    0: Rational(1),
    1: (n-3),
    2: (n-5)*(n+2)/2,
    3: (n**3 - 73*n + 168)/6,
}
# check Q_2 expands: (n-5)(n+2)/2 = (n^2-3n-10)/2 -> at n=6: (36-18-10)/2=4 ok
# check Q_3 at n=8: (512-584+168)/6 = 96/6=16 ok

import collections
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

ok=True
for k in [0,1,2,3]:
    for N in sorted(T):
        v=T[N].get(N-k)
        if v is not None:
            pred = Q[k].subs(n,N)*3**(N-2*k-1)
            match = (pred==v)
            if not match:
                print(f"MISMATCH k={k} N={N}: v={v} pred={pred}")
                ok=False
print("All match:" ,ok)

# Now reconstruct D(N) = sum_M N(N,M) predicted by the model over computed N and compare.
print("\nD(N) = sum_k Q_k(N) 3^(N-2k-1) over computed range (model vs true):")
Dtrue=[1,1,3,9,30,99,336,1134,3855,13086,44499,151263,514419,1749267,5949063]
for N in range(2,13):
    s=0
    for k in [0,1,2,3]:
        v=T[N].get(N-k)
        if v is not None: s+=v
    print(f"N={N}: submodel_sum={s} D_true={Dtrue[N]} equal={s==Dtrue[N]}")
