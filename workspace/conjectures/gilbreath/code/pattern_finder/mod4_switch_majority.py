#!/usr/bin/env python3
"""Push the mod-4 switch-density check far beyond the nu2 data.

w(n) = # i in [2, n-1] with gap_i = (p_{i+1} - p_i) = 2 (mod 4)
      = # consecutive-prime pairs (p_i, p_{i+1}) up to index n-1 that SWITCH
        residue class mod 4 (odd primes are 1 or 3 mod 4; the switch happens
        exactly when the gap is 2 mod 4).

Checks, EXACTLY, over n = 2 .. N:
  (A) w(n) >= (n-2)/2           (switch majority at every n)
  (B) the running minimum of w(n)/(n-2)  (worst margin and where)
Also records the sequence w(n) at sparse samples for the tools.

Sieve to LIMIT; only O(LIMIT) memory (bytearray sieve) + prime list.  The
check is O(#primes) with prefix sums — no diagonal computation, so this can
go very large.
"""
import sys, time
from math import isqrt

LIMIT = int(sys.argv[1]) if len(sys.argv) > 1 else 10_000_000
N = int(sys.argv[2]) if len(sys.argv) > 2 else 100_000

t0 = time.time()
sieve = bytearray(b"\x01") * (LIMIT + 1)
sieve[0] = sieve[1] = 0
for i in range(2, isqrt(LIMIT) + 1):
    if sieve[i]:
        sieve[i * i::i] = b"\x00" * (((LIMIT - i * i) // i) + 1)
primes = [i for i in range(2, LIMIT + 1) if sieve[i]]
t1 = time.time()
print("sieve to %d : %d primes (%.1fs)" % (LIMIT, len(primes), t1 - t0))
if len(primes) < N + 2:
    print("need", N + 2, "primes, have", len(primes)); sys.exit(1)

# mod-4 switch bits
hbits = [1 if ((primes[i + 1] - primes[i]) // 2) % 2 else 0
         for i in range(N + 1)]
pref = [0] * (len(hbits) + 1)
for i, b in enumerate(hbits):
    pref[i + 1] = pref[i] + b

def w(n):
    return pref[n] - pref[2]   # hbits[2..n-1]

# (A) majority check
bad = []
min_margin = 1.0; min_margin_n = 0
for n in range(2, N + 1):
    wv = w(n)
    # margin = (2*wv - (n-2)) / (2*(n-2))  in [0,1)
    if 2 * wv < (n - 2):
        bad.append(n)
        if len(bad) <= 5:
            print("VIOLATION at n=%d w=%d (n-2)/2=%d" % (n, wv, (n - 2) // 2))
    denom = n - 2
    if denom > 0:
        m = wv / denom
        if m < min_margin:
            min_margin = m; min_margin_n = n
print("w(n) >= (n-2)/2 for ALL n in [2,%d]: %s (violations: %d, first %s)"
      % (N, "YES" if not bad else "NO", len(bad), bad[:5]))
print("min w(n)/(n-2) over n in [2,%d]: %.6f at n=%d" % (N, min_margin, min_margin_n))

# (B) w(n)/n range over the tail
print("w(n)/n at samples:", end=" ")
for n in [1000, 5000, 10000, 50000, 100000, N]:
    if n <= N:
        print("n=%d:%.4f" % (n, w(n) / n), end="  ")
print()

# sparse samples for the tools
print("\nw(n) samples n=2..%d:" % min(N, 60))
print([w(n) for n in range(2, min(N, 60) + 1)])
print("w(100000)=%d" % w(min(N, 100000)))

# (C) the theoretical threshold margin: does w(n) >= n/2 - something survive?
#     The combined bound needs w >= (n-2)/2; report how much slack:
slack = min(2 * w(n) - (n - 2) for n in range(2, N + 1))
print("min excess 2*w(n)-(n-2) over n in [2,%d]: %d" % (N, slack))
print("time %.1fs total" % (time.time() - t0))
