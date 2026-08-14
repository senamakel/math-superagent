#!/usr/bin/env python3
"""Re-extract subsequences of A063985(n) from the stored 200000-term prefix.

Reads code/out/seq_A063985.txt (one term per line, index n = line number),
verifies the recorded values from pe351-pattern-findings.md, and prints
fresh subsequences for the sequence tools:
  A(2^k)   k=0..17
  A(3^k)   k=0..11
  A(k^2)   k=1..20
  A(10^k)  k=0..8
  A(2^k*3) k=0..16  (not previously examined)
  A(2^k*5) k=0..15  (not previously examined)
"""
import math

with open("code/out/seq_A063985.txt") as f:
    A = [int(line) for line in f]
assert len(A) == 200000, len(A)
# index n -> A(n): file line 1 holds A(1) etc.  Build 1-based lookup.
A1 = [0] + A  # A1[n] = A(n)

def sub(fn, nmax=200000):
    out = []
    n = 1
    while n <= nmax:
        out.append((n, A1[n]))
        n = fn(n)
        if n == 1:
            break
    return out

p2 = sub(lambda k: 2 * k)
p3 = sub(lambda k: 3 * k)
sq = [(k, A1[k * k]) for k in range(1, 21)]
p10 = sub(lambda k: 10 * k)
p2t3 = sub(lambda k: 2 * k * 3 // (k // 2) if False else 2 * k * 3 // 2)  # placeholder replaced below

def pow2_3(k):
    return 2 ** k * 3

def pow2_5(k):
    return 2 ** k * 5

p23 = [(2 ** k * 3, A1[2 ** k * 3]) for k in range(0, 17)]
p25 = [(2 ** k * 5, A1[2 ** k * 5]) for k in range(0, 16)]

print("A(2^k)  k=0..17:", [v for _, v in p2])
print("A(3^k)  k=0..11:", [v for _, v in p3])
print("A(k^2)  k=1..20:", [v for _, v in sq])
print("A(10^k) k=0..8 :", [v for _, v in p10])
print("A(2^k*3) k=0..16:", [v for _, v in p23])
print("A(2^k*5) k=0..15:", [v for _, v in p25])

# recorded values from pe351-pattern-findings.md, cross-check
rec_2k = [0, 1, 4, 14, 56, 204, 820, 3234, 12948, 51476, 205836,
          822590, 3290636, 13156918, 52626582, 210499912, 842001490,
          3367894404]
rec_3k = [0, 2, 17, 148, 1301, 11590, 104317, 938082, 8440107,
          75950324, 683550231, 6151859350]
rec_sq = [0, 4, 17, 56, 125, 270, 471, 820]
got_2k = [v for _, v in p2]
got_3k = [v for _, v in p3]
got_sq = [v for _, v in sq]
assert got_2k == rec_2k, "A(2^k) mismatch"
assert got_3k == rec_3k, "A(3^k) mismatch"
assert got_sq[:8] == rec_sq, "A(k^2) mismatch"
print("OK: re-extracted subsequences match the recorded values.")
