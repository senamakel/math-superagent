#!/usr/bin/env python3
"""DECISIVE: weighted d-sequence DP reproduces D(N)?

Model: reachable level histograms <-> d-sequences (d_0=1,...,d_{M-1}=1),
sum_k d_k = N, with interior level values a_k = 3 d_{k-1} - d_k in [1,7].
Per-interior-level weight: w(1)=w(2)=w(3)=3, w(4)=4, w(5)=1, w(6)=10/3,
w(7)=1 (verified 694/694 per-histogram).  Then
    D(N) = sum over feasible d-sequences of  prod_{interior k} w(a_k).

Use exact Fractions so w(6)=10/3 is exact.  DP state: (last d value, running
sum) -> accumulated weight.  Polynomial in N (d values bounded since
a_k in [1,7] => d_k in [3d_{k-1}-7, 3d_{k-1}-1]).
"""
from fractions import Fraction

D = {2:3,3:9,4:30,5:99,6:336,7:1134,8:3855,9:13086,10:44499,11:151263,
     12:514419,13:1749267,14:5949063}

def w(a):
    if a in (1,2,3): return Fraction(3)
    if a == 4: return Fraction(4)
    if a == 5: return Fraction(1)
    if a == 6: return Fraction(10,3)
    if a == 7: return Fraction(1)
    return None   # a outside [1,7] not allowed

def D_from_dseq(N):
    # dp[(last_d, s)] = total weight of prefixes ending at (last_d, s)
    dp = {(1, 1): Fraction(1)}     # d_0 = 1, sum so far = 1
    total = Fraction(0)
    # iterate lengths; d values are bounded, sum <= N
    for _ in range(N):
        ndp = {}
        for (last, s), wt in dp.items():
            # valid next d: a = 3*last - nxt in [1,7]
            for nxt in range(max(1, 3*last-7), 3*last):
                a = 3*last - nxt
                nw = wt * w(a)
                ns = s + nxt
                if ns > N: continue
                key = (nxt, ns)
                ndp[key] = ndp.get(key, Fraction(0)) + nw
        dp = ndp
        # close: sequences ending at (last=1, sum=N)
        total += dp.get((1, N), Fraction(0))
    return total

print("N  |  weighted d-seq DP  |  D(N)  |  match")
allok = True
for n in range(2, 15):
    val = D_from_dseq(n)
    ok = (val == D[n])
    allok = allok and ok
    print(f"{n:>2} | {val:>20} | {D[n]:>9} | {ok}")
print("\nALL N=2..14 MATCH:", allok)
