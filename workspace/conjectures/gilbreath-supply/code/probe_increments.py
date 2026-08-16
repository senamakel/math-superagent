#!/usr/bin/env python3
"""Probe the increment sequence dE2(n)=E2(n)-E2(n-1) (=-dS): is it a fair,
near-uncorrelated 'walk'? And dyadic self-similarity of the excess."""
import sys, math, collections
data = {}
for line in open("out/excess_seq.txt"):
    n, nu2, e2 = map(int, line.split())
    data[n] = e2
N = max(data)
inc = {n: data[n] - data[n-1] for n in range(3, N+1)}
vals = list(inc.values())
mean = sum(vals)/len(vals)
v0 = sum((x-mean)**2 for x in vals)/len(vals)
# lag-1 autocorr
c1 = sum((vals[i]-mean)*(vals[i+1]-mean) for i in range(len(vals)-1))/len(vals)
print(f"N={N} inc count={len(vals)} mean={mean:.4f} var={v0:.4f} lag1={c1/v0:.4f}")

# magnitude distribution
cnt = collections.Counter(abs(x) for x in vals)
print("inc magnitude counts (top 12):", sorted(cnt.items())[:12])
print("  fraction |inc|<=3:", sum(v for k,v in cnt.items() if k<=3)/len(vals))
print("  max |inc|:", max(abs(x) for x in vals), "at", [n for n in inc if abs(inc[n])==max(abs(x) for x in vals)][:5])

# running max of |S| = |E2| and of partial sums of inc (should match |E2|)
# partial sums of inc from n=3 onward = E2(n)-E2(2)
# E2(2)=0 so partial sum = E2(n). verify
acc = 0
bad = 0
for n in range(3, N+1):
    acc += inc[n]
    if acc != data[n]:
        bad += 1
print(f"partial-sum==E2 mismatches: {bad}")

# Dyadic self-similarity: ratio E2(2^k)/E2(2^{k-1})? and E2(2^k+1)-E2(2^k)
print("dyadic excess values:")
for k in range(2, int(math.log2(N))+1):
    m = 1 << k
    if m <= N:
        print(f"  E2(2^{k})={data[m]}  delta from prev dyad E2(2^{k})-E2(2^{k-1}) = "
              f"{data[m]-data[m//2]}")
