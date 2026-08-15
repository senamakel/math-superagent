#!/usr/bin/env python3
"""Push the mod-4 switch majority to n = 1,000,000 (sieve 1e8).

e(n) = 2*w(n) - (n-2)  is the excess of mod-4-switching consecutive prime
pairs over non-switching ones among gaps g_2..g_{n-1}.  Checks:
  (A) e(n) >= 0 for ALL n in [2, N]  (the pointwise majority conjecture)
  (B) worst excess over tails: min e(n) for n in [T, N], T in
      {17, 100, 1000, 10000, 100000}
  (C) the sequence e(n) at n=2..512 for the sequence tools, plus samples
  (D) how many n have e(n) < some levels (looseness of the bound)
Uses 1-indexed n: w(n) = sum of switch bits for gaps 2..n-1.
"""
import sys, time
from math import isqrt

LIMIT = int(sys.argv[1]) if len(sys.argv) > 1 else 100_000_000
N = int(sys.argv[2]) if len(sys.argv) > 2 else 1_000_000

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

hbits = [1 if ((primes[i + 1] - primes[i]) // 2) % 2 else 0
         for i in range(N + 1)]
pref = [0] * (len(hbits) + 1)
for i, b in enumerate(hbits):
    pref[i + 1] = pref[i] + b

def w(n):
    return pref[n] - pref[2]

# (A) pointwise majority, with running min of e(n)
emin = [10 ** 18] * (N + 1)   # emin[n] = min e over [2..n]
bad = []
first_bad = None
e_min_global = 10 ** 18; e_min_global_n = 0
for n in range(2, N + 1):
    e = 2 * w(n) - (n - 2)
    if e < 0:
        bad.append(n)
        if first_bad is None:
            first_bad = n
    if e < e_min_global:
        e_min_global = e; e_min_global_n = n
    emin[n] = e_min_global
print("(A) e(n) >= 0 for all n in [2,%d]: %s (violations %d, first %s)"
      % (N, "YES" if not bad else "NO", len(bad), first_bad))
print("    global min e = %d at n=%d" % (e_min_global, e_min_global_n))

# (B) min e over tails
print("(B) min e(n) over tails:")
for T in [17, 100, 1000, 10000, 100000]:
    m = 10 ** 18; mn = 0
    for n in range(T, N + 1):
        e = 2 * w(n) - (n - 2)
        if e < m:
            m = e; mn = n
    print("    T=%7d : min e = %d at n=%d" % (T, m, mn))

# (C) how tight: how many n with e(n) <= L for L in 0,1,2,5,10,100,1000
print("(C) count of n with small e:")
for L in [0, 1, 2, 5, 10, 100, 1000]:
    cnt = sum(1 for n in range(2, N + 1) if 2 * w(n) - (n - 2) <= L)
    print("    e <= %-5d : %d" % (L, cnt))

# (D) tail looseness: min e over [n/2, n] (local worst) at large n
print("(D) min e over [k, N] for k = N//2, N//4 :",
      min(2 * w(n) - (n - 2) for n in range(N // 2, N + 1)),
      min(2 * w(n) - (n - 2) for n in range(N // 4, N + 1)))

# (E) write e(n) first 512 for the tools
with open("code/out/pattern_finder_outputs/excess_e_first512.txt", "w") as f:
    f.write(" ".join(str(2 * w(n) - (n - 2)) for n in range(2, 514)))
print("(E) wrote excess_e_first512.txt (n=2..513)")
print("time %.1fs total" % (time.time() - t0))
