#!/usr/bin/env python3
"""Independent oracle for the B-column (nearest NON-constant 2^k-periodic
Hamming distance) of prime_antidyadic.py.

True brute force: enumerate all non-constant blocks in {0,1}^p (2^p - 2 of
them), compute Hamming distance to h[:n] directly, take the minimum.  For
small p (k<=4, p<=16) this is cheap and independent of the majority shortcut.

Checks the B value for n=100000, k=1..4 against the file's table (which
reports the non-constant nearest-periodic distance/n).
"""
import sys, time
from math import isqrt

SIEVE_LIMIT = 16_000_000
N = 100_000

t0 = time.time()
sieve = bytearray(b"\x01") * (SIEVE_LIMIT + 1)
sieve[0] = sieve[1] = 0
for i in range(2, isqrt(SIEVE_LIMIT) + 1):
    if sieve[i]:
        sieve[i * i::i] = b"\x00" * (((SIEVE_LIMIT - i * i) // i) + 1)
primes = [i for i in range(2, SIEVE_LIMIT + 1) if sieve[i]]
bits = [(p2 - p1) // 2 % 2 for p1, p2 in zip(primes, primes[1:])][:N]
print("built %d switch bits (%.1fs)" % (N, time.time() - t0))

def brute_nearest_nonconst(seq, p):
    n = len(seq)
    best = None
    for bval in range(1 << p):
        block = [(bval >> r) & 1 for r in range(p)]
        if len(set(block)) < 2:      # constant block: skip
            continue
        d = sum(1 for j in range(n) if seq[j] != block[j % p])
        if best is None or d < best[0]:
            best = (d, block)
    return best[0], best[1]

for k in range(1, 5):
    p = 1 << k
    d, block = brute_nearest_nonconst(bits, p)
    print("k=%d p=%d : brute B distance/n = %.6f  block=%s%s"
          % (k, p, d / N, block, " <- verify" * 0))
print("time %.1fs" % (time.time() - t0))
