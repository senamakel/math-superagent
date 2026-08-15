#!/usr/bin/env python3
"""Post-process the dense nu2 run: clean large-n transfer constant + write
integer sequences for the sequence tools.

Reads code/out/nu2_dense.txt (n, nu2) and recomputes w(n) from the primes,
so the transfer ratio nu2/w is available at EVERY n with clean thresholding.
Also emits:
  - fluctuation sequence  F_n = nu2 - n//2   (integer, around 0)
  - rescaled transfer-ratio samples
"""
import math
from lib.gilbreath import primes_up_to

P = primes_up_to(1_000_000)
hbits = [((P[i+1] - P[i]) // 2) % 2 for i in range(len(P) - 1)]
hprefix = [0]*(len(hbits)+1)
for i, b in enumerate(hbits):
    hprefix[i+1] = hprefix[i] + b

nu2 = {}
with open("code/out/nu2_dense.txt") as f:
    for line in f:
        n, v = line.split()
        nu2[int(n)] = int(v)

N = max(nu2)
# w(n) = sum(hbits[2:n]) = sum_{j=2}^{n-1} hbits_j
def w(n):
    return sum(hbits[2:n])

# min transfer ratio over n>=T
for T in [50, 100, 500, 1000, 5000]:
    m = 1.0; mn = 0
    for n in range(T, N+1):
        wv = w(n)
        if wv > 0:
            r = nu2[n]/float(wv)
            if r < m:
                m = r; mn = n
    print("min nu2/w over n>=%5d : %.4f at n=%d" % (T, m, mn))

# does nu2 >= c*w hold for n>=T for c in {0.8,0.75,0.7}?
for T in [100, 1000]:
    for c in [0.85, 0.8, 0.75]:
        bad = [n for n in range(T, N+1)
               if w(n) > 0 and nu2[n] < c*w(n)]
        print("n>=%d: nu2 < %.2f*w : %d (first %s)" % (T, c, len(bad), bad[:3]))

# fluctuation sequence F_n = nu2 - n//2, integer
fluc_first = [nu2[n] - n//2 for n in range(1, 101)]
print("\nF_n = nu2 - n//2, n=1..100:")
print(fluc_first)
# store as one-per-line for the tools
with open("code/out/nu2_fluct_first100.txt","w") as f:
    f.write(" ".join(map(str, fluc_first)))
print("\nmin,max of F over n>=500:", min(nu2[n]-n//2 for n in range(500,N+1)),
      max(nu2[n]-n//2 for n in range(500,N+1)))

# F_n has a bias? F is ~centered on +-~: mean F over n in [1000,N]
import statistics
F = [nu2[n]-n//2 for n in range(1000, N+1)]
print("mean F (n>=1000):", "%.3f" % statistics.mean(F),
      " std:", "%.1f" % statistics.pstdev(F))
