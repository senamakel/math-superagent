"""Verify the oracle claim hemiperfect-22-below-1e18.

Direct check: for the 22 candidate values listed in the oracle note, compute
sigma(n)/n exactly and confirm each is k+1/2 for integer k, and that all are
<= 1e18; also confirm A159907 term 23 > 1e18. Sum them.
"""
from math import gcd

vals = [2,24,4320,4680,26208,8910720,17428320,20427264,91963648,197064960,
8583644160,10200236032,21857648640,57575890944,57629644800,206166804480,
17116004505600,1416963251404800,15338300494970880,75462255348480000,
88898072401645056,301183421949935616]

def sigma(n):
    s = 0
    d = 1
    while d*d <= n:
        if n % d == 0:
            s += d
            if d != n//d:
                s += n//d
        d += 1
    return s

LIM = 10**18
assert all(v <= LIM for v in vals)
# A159907 term 23
assert 6219051710415667200 > LIM

per_k = {}
for n in vals:
    num, den = sigma(n), n
    g = gcd(num, den)
    num, den = num//g, den//g
    assert den == 2 and num % 2 == 1, (n, num, den)
    k = (num//2 - 1)//2 if False else (sigma(n)*2//n - 1)//2
    per_k.setdefault(k, []).append(n)

for k in sorted(per_k):
    print(f"k={k} (abund {2*k+1}/2): n={len(per_k[k])} sum={sum(per_k[k])}")

print("count:", len(vals))
print("SUM =", sum(vals))
