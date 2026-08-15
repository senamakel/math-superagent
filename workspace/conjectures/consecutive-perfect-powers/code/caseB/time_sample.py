#!/usr/bin/env python3
"""Time a sample of the expensive (c,p) computations to size the full run."""
import math, time

def is_odd_prime(n):
    if n < 2: return False
    if n % 2 == 0: return n == 2
    d = 3
    while d*d <= n:
        if n % d == 0: return False
        d += 2
    return True

primes = [p for p in range(3,501) if is_odd_prime(p)]
p1m4 = [p for p in primes if p % 4 == 1]
print(f"primes<=500: {len(primes)}, p==1 mod4: {len(p1m4)}")

# worst corner: large c, large p
def one(c, p):
    x = c*c+1
    T = (pow(x,p)-1)//(c*c)
    s = math.isqrt(T)
    return s*s == T

# time a representative sample stratified: small/mid p, small/mid/large c
cases = []
for c in [2, 100, 1000, 10000, 100000]:
    for p in [5, 61, 149, 257, 397, 499 if 499%4==1 else 491, 13, 29, 73]:
        if p in primes and p%4==1:
            cases.append((c,p))
t0=time.time()
n=0
for (c,p) in cases[:20]:
    one(c,p); n+=1
dt=(time.time()-t0)
per = dt/n
print(f"sample {n} ops in {dt:.2f}s  => {per*1e6:.1f} us/op (serial)")
tot = (100000//2)*len(p1m4)
serial = per*tot
print(f"surviving-class pairs ~ {tot:,}; serial est {serial/60:.1f} min")
print(f"with 28 cores ~ {serial/60/28:.1f} min")
