#!/usr/bin/env python3
"""Measure the scaling law of nu2(n) - n/2 over the dense nu2 data (nu2_dense.txt).

CONTEXT claims: max |2*nu2-n| = 624 at n=27625; fluctuation never < -5*sqrt(n);
min nu2/n over n>=1000 = 0.4587; implied exponent min log nu2/log n = 0.7658.
Verify these directly and probe the true fluctuation scaling: is |2*nu2-n| = O(sqrt n)?
"""
import math

nu2 = {}
with open("code/out/nu2_dense.txt") as f:
    for line in f:
        p = line.split()
        if len(p) == 2:
            nu2[int(p[0])] = int(p[1])

Ns = sorted(nu2.keys())
print("terms:", len(Ns), "range n =", Ns[0], "..", Ns[-1])

# dev(n) = 2*nu2(n) - n
maxabs = 0
maxabs_n = None
min_dev = None
min_dev_n = None
min_ratio_sqrt = 10**9  # dev / sqrt(n) minimum (most negative)
min_ratio_n = None
# track where (2nu2-n) goes most negative relative to sqrt(n)
for n in Ns:
    dev = 2*nu2[n] - n
    if abs(dev) > maxabs:
        maxabs, maxabs_n = abs(dev), n
    if min_dev is None or dev < min_dev:
        min_dev, min_dev_n = dev, n
    if abs(dev) > 0:
        r = dev / math.sqrt(n)
        if r < min_ratio_sqrt:
            min_ratio_sqrt, min_ratio_n = r, n

print("max |2*nu2-n| =", maxabs, "at n =", maxabs_n)
print("min  2*nu2-n  =", min_dev, "at n =", min_dev_n)
print("most negative dev/sqrt(n) = %.4f at n=%d" % (min_ratio_sqrt, min_ratio_n))
print("so dev >= %.2f*sqrt(n) throughout" % min_ratio_sqrt)

# Also check the positive excursion: max dev/sqrt(n)
max_ratio = -10**9; max_ratio_n=None
for n in Ns:
    dev = 2*nu2[n]-n
    if abs(dev)>0:
        r = dev/math.sqrt(n)
        if r > max_ratio:
            max_ratio, max_ratio_n = r, n
print("most positive dev/sqrt(n) = %.4f at n=%d" % (max_ratio, max_ratio_n))

# implied exponent: min over n of log(nu2)/log(n)
min_exp = None; min_exp_n=None
for n in Ns:
    if nu2[n] > 1:
        e = math.log(nu2[n])/math.log(n)
        if min_exp is None or e < min_exp:
            min_exp, min_exp_n = e, n
print("min log(nu2)/log(n) = %.4f at n=%d (threshold beta=0.525; want >0.525)" % (min_exp, min_exp_n))

# min nu2/n over n>=1000
sub=[(n,nu2[n]) for n in Ns if n>=1000]
mn = min(nu2[n]/n for n,_x in sub)
mn_n = min(sub, key=lambda t:t[1]/t[0])[0]
print("min nu2/n over n>=1000 = %.4f at n=%d" % (mn, mn_n))

# distribution of dev/sqrt(n) - is it bounded (constant order) or grow/shrink?
# report at a few representative n
for n in [100, 1000, 5000, 10000, 20000, 30000]:
    if n in nu2:
        dev = 2*nu2[n]-n
        print("  n=%-6d nu2=%-6d dev=%-5d dev/sqrt(n)=%+.3f" % (n, nu2[n], dev, dev/math.sqrt(n)))
