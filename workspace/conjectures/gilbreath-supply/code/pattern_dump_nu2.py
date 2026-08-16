#!/usr/bin/env python3
"""Dump nu2(n) for n=2..N+1 from the exact submask-XOR DP (nu2_fast),
for feeding the sequence tools. Cross-checks brute force at small n."""
from math import isqrt

def primes_upto_index(n):
    ps, cand = [2], 3
    while len(ps) < n:
        ok = True; r = isqrt(cand)
        for p in ps:
            if p > r: break
            if cand % p == 0: ok = False; break
        if ok: ps.append(cand)
        cand += 2
    return ps

def hpow(d):
    m = 1
    while (m << 1) <= d: m <<= 1
    return m

def nu2_fast(N, h):
    rows = [None] * N
    rows[0] = [h[b] for b in range(N)]
    for d in range(1, N):
        m = hpow(d); d1 = d - m; r1 = rows[d1]; L = N - 1 - d
        new = [0] * (L + 1)
        for base in range(L + 1):
            new[base] = r1[base] ^ r1[base + m]
        rows[d] = new
    out = []
    for n in range(2, N + 1):
        cnt = 0
        for d in range(2, n):
            cnt += rows[d][n - 1 - d]
        out.append(cnt)
    return out

def nu2_brute(n, h):
    cnt = 0
    for d in range(2, n):
        t = 0; base = n - 1 - d; sub = d
        while True:
            t ^= h[base + sub]
            if sub == 0: break
            sub = (sub - 1) & d
        cnt += t
    return cnt

import sys
N = int(sys.argv[1]) if len(sys.argv) > 1 else 513
ps = primes_upto_index(N + 3)
h = [((ps[j + 1] - ps[j]) // 2) % 2 for j in range(N + 2)]
fast = nu2_fast(N, h)
for n in [2,3,5,8,13,21,34]:
    assert nu2_brute(n, h) == fast[n-2], n
print("brute cross-check OK")
# nu2(n) indexed by n: fast[i-2] = nu2(i)
seq = fast  # seq[n-2] = nu2(n), n=2..N
with open("code/out/nu2_terms.txt", "w") as f:
    for n in range(2, N + 1):
        f.write(f"{n} {seq[n-2]}\n")
print("wrote", N - 1, "terms n=2..", N)
print(seq[:40])
