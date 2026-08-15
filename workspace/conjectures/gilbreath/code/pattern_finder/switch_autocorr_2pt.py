import sys
sys.path.insert(0, "/workspace")
from lib.gilbreath import primes_up_to
import time

N = 1_000_000
SIEVE = 100_000_000
t0 = time.time()
P = primes_up_to(SIEVE)
print("sieve %d : %d primes (%.1fs)" % (SIEVE, len(P), time.time()-t0))

# switch bit h[k] over gaps g_k, k=3..N (index into P list: gap_k = P[k]-P[k-1], 1-indexed primes)
# h[k] = 1 iff gap_k = 2 mod 4  (switch). We use k=3..N, 0-indexed position i=k-2 -> P[i], P[i+1]
# Let's just build the bit string over k=3..N.
bits = []
for k in range(3, N+1):
    g = P[k] - P[k-1]
    bits.append(1 if (g//2)%2==1 else 0)
bits = bits  # length N-2, position j corresponds to k=j+3, i.e. gaps g_3..g_N

n = len(bits)
print("switch-bit length", n)

# centered bits: mean, autocorrelation at lags 1..L
mean = sum(bits)/n
print("weight density w/n (over window 3..N): %.4f  (#1=%d)" % (mean, sum(bits)))

L = 40
print("\n== centered autocorrelation of switch bit, lags 1..%d ==" % L)
cm = [b-mean for b in bits]
var = sum(x*x for x in cm)/n
for lag in range(1, L+1):
    acc = sum(cm[j]*cm[j+lag] for j in range(n-lag))/(n-lag)
    print("lag %2d : r=%.4f" % (lag, acc/var if var else 0))

# also: joint probability P(h[j], h[j+1])  and  expected e-step drift
# switch-step is +1 when h=1, -1 when h=0 (since e = 2w-(n-2))
# drift per step = 2*P(h=1)-1 = 2*mean-1
print("\nper-step drift 2*w/n - 1 = %.4f" % (2*mean-1))

# correlation between consecutive e-steps (the ballot structure): E[h_j h_{j+1}] vs mean^2
import itertools
from collections import Counter
cnt = Counter(zip(bits[:-1], bits[1:]))
print("\njoint consecutive h: ", dict(cnt))
for a in (0,1):
    for b_ in (0,1):
        pass
# autocorr at lag1 in (0,1) terms:
c00,c01,c10,c11 = cnt[(0,0)],cnt[(0,1)],cnt[(1,0)],cnt[(1,1)]
tot = n-1
print("P(1,1)=%.4f P(1,0)=%.4f P(0,1)=%.4f P(0,0)=%.4f" % (c11/tot,c10/tot,c01/tot,c00/tot))
print("(P(1,1) vs mean^2=%.4f)" % (mean*mean))
print("total time %.1fs" % (time.time()-t0))
