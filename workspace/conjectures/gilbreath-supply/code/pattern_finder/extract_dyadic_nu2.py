#!/usr/bin/env python3
"""Extract structured subsequences of nu2(n) from the canonical JSON and save."""
import json, sys
sys.path.insert(0, "/workspace/code")

with open("/workspace/code/out/nu2_primes_xor_40000.json") as f:
    nu2 = json.load(f)   # list indexed by n

# sanity guards
assert nu2[53] == 18, nu2[53]
assert nu2[64] == 27, nu2[64]
assert nu2[4000] == 1975, nu2[4000]

# dyadic subsequence
dyad = [nu2[k] for k in range(0, 16) if (1 << k) <= 40000]
# 2^k
wy = [(1 << k, nu2[1 << k]) for k in range(1, 16) if (1 << k) <= 40000]
# S at 2^k too
S_dyad = [(1 << k, (1 << k) - 2 - 2 * nu2[1 << k]) for k in range(1, 16) if (1 << k) <= 40000]
# record-low n values (first time a new low of nu2/n is set?) - not here
# primorial-type? no.

print("== nu2(2^k), k=1..15 ==")
for k, v in wy:
    ratio = v / (1 << k)
    print("k=%2d n=%6d nu2=%6d nu2/n=%.4f" % (k, 1 << k, v, ratio))
print()
print("== S(2^k) = (n-2)-2*nu2 ==")
for k, v in S_dyad:
    print("k=%2d n=%6d S=%6d S/n=%.4f S/sqrt(n)=%.3f" % (k, v[0], v[1], v[1]/v[0], v[1]/(v[0]**0.5)))

# also nu2/n near dyadic - the max |S|/sqrt(n) scaled behavior
import math
vals = []
for n in range(2, 40001):
    vals.append(nu2[n])
# record where nu2/n is largest and smallest overall
mx = max(range(2, 40001), key=lambda n: nu2[n]/n)
mn = min(range(2, 40001), key=lambda n: nu2[n]/n)
print()
print("max nu2/n at n=%d: %.4f" % (mx, nu2[mx]/mx))
print("min nu2/n at n=%d: %.4f" % (mn, nu2[mn]/mn))

# dyadic ratios of nu2(2^k)/nu2(2^(k-1))
w = [v for _, v in wy]
print("nu2(2^k):", w)
print("ratios:", [w[i]/w[i-1] for i in range(1, len(w))])

# save dyadic
with open("/workspace/code/out/nu2_dyadic_seq.txt", "w") as f:
    for k, v in wy:
        f.write("%d %d\n" % (k, v))
print("saved nu2_dyadic_seq.txt")
