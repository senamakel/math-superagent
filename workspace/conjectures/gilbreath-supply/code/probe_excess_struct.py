#!/usr/bin/env python3
"""Probe structure of the excess E2(n) = 2*nu2(n)-(n-2) = -S(n):
1. growth of max|E2| over dyadic prefixes vs sqrt(n) and n^a
2. values at dyadic points n=2^k and n=2^k+1 (boundary-spike mechanism)
3. residue-period structure of E2
"""
import sys, math
sys.path.insert(0, "/workspace/code")
data = {}
for line in open("out/excess_seq.txt"):
    n, nu2, e2 = map(int, line.split())
    data[n] = e2

N = max(data)
print("=== dyadic prefix growth of max|E2| ===")
for k in range(2, int(math.log2(N)) + 1):
    m = 1 << k
    if m > N: break
    M = max(abs(data[n]) for n in range(2, m + 1))
    print(f"  n<=2^{k}={m:6d}: max|E2|={M:5d}  sqrt(m)={math.sqrt(m):7.1f}  "
          f"max|E2|/sqrt(m)={M/math.sqrt(m):5.2f}  max/n={M/m:.4f}")

print("=== E2 at dyadic points ===")
for k in range(2, int(math.log2(N)) + 1):
    m = 1 << k
    if m <= N:
        print(f"  2^{k}={m}: E2={data.get(m)}  2^{k}+1={m+1}: E2={data.get(m+1)}  "
              f"2^{k}-1={m-1}: E2={data.get(m-1)}")

print("=== where does max|E2| occur ===")
amax = max(data, key=lambda n: abs(data[n]))
print(f"  max|E2|={data[amax]} at n={amax}  ({amax- (1<<int(math.log2(amax)))}) above 2^floor")

print("=== residue-period of |E2| mod small bases ===")
for base in (2, 4, 8):
    # test if E2 mod base is periodic with some period <= 4*base
    for P in (base, 2*base, 4*base, 8*base):
        ok = all(data[n] % base == data[n-P] % base for n in range(P+2, N+1))
        if ok:
            print(f"  E2 mod {base} period {P}: YES (all n in [2,{N}])")
            break
    else:
        print(f"  E2 mod {base}: no period <= {8*base}")

print("=== sign structure: fraction of n where S and E2 flip sign across dyadic windows ===")
winsign = []
for k in range(2, int(math.log2(N)) + 1):
    lo, hi = 1 << k, min(1 << (k+1), N+1)
    if hi - lo < 4: continue
    pos = sum(1 for n in range(lo, hi) if data[n] > 0)
    neg = sum(1 for n in range(lo, hi) if data[n] < 0)
    print(f"  [{lo},{hi}): pos={pos} neg={neg} zero={hi-lo-pos-neg}")
