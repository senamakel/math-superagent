"""Verify pc=3 support-structure law at TWO more degrees (n=19, n=28, plus
n=22,26,25) and pc=4 at n=25? no n=25 is pc=3.  Just enumerate pc=3 degrees
19,21,22,25,26,28 and compare to n=7,11,13 support profile {2:6,4:5,6:3}."""
from math import comb
from collections import Counter
from multiprocessing import Pool

def hasse_deriv(fbits, i):
    out = 0; j = 0; fb = fbits
    while fb:
        if fb & 1:
            if (i & j) == i: out |= 1 << (j - i)
        fb >>= 1; j += 1
    return out

def pmod(a, b):
    bl = b.bit_length()
    while a.bit_length() >= bl:
        a ^= b << (a.bit_length() - bl)
    return a

def pgcd(a, b):
    if a == 0: return b
    if b == 0: return a
    while b:
        a, b = b, pmod(a, b)
    return a

def is_ca_f2(fbits):
    n = fbits.bit_length() - 1
    for i in range(1, n):
        hi = hasse_deriv(fbits, i)
        if hi == 0: continue
        if pgcd(fbits, hi) == 1: return False
    return True

def Cparity(n, k):
    return (k & n) == k

def is_pure_f2(fbits, n):
    if fbits == (1 << n): return True
    bits = 0
    for j in range(n + 1):
        if Cparity(n, j): bits |= 1 << j
    return fbits == bits

def worker(args):
    n, lo, hi = args
    cnt = Counter()
    top = 1 << n
    for v in range(lo, hi):
        fb = top | v
        if is_ca_f2(fb) and not is_pure_f2(fb, n):
            cnt[fb.bit_count()] += 1
    return cnt

def analyze(n, workers=28, CH=1<<16):
    size = 1 << n
    bounds = [(n, lo, min(lo + CH, size)) for lo in range(0, size, CH)]
    total = Counter()
    with Pool(workers) as pool:
        for c in pool.imap_unordered(worker, bounds, chunksize=1):
            total.update(c)
    cesum = sum(total.values())
    print(f"n={n:2d} pc={bin(n).count('1')} ce={cesum} m={(cesum//2)+1} by-support={dict(sorted(total.items()))}")

if __name__ == "__main__":
    for n in (19, 21, 22, 25, 26):
        analyze(n, CH=1<<15)
