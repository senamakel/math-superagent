"""Support-size structure of F2 Hasse-CA counterexamples across popcount
classes.  Tests the finding that small monomial-support counts are constant
per popcount class while large-support counts vary with n.

pc=2: n in {5,6,9,10,12,17,18,20,24}
pc=3: n in {7,11,13,19,21,22,25,26,28}
Only small n enumerated exactly (parallel over subsets)."""
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

def analyze(n, workers=28):
    size = 1 << n
    CH = 1 << 16
    bounds = [(n, lo, min(lo + CH, size)) for lo in range(0, size, CH)]
    total = Counter()
    with Pool(workers) as pool:
        for c in pool.imap_unordered(worker, bounds, chunksize=1):
            total.update(c)
    cesum = sum(total.values())
    print(f"n={n:2d} pc={bin(n).count('1')} ce={cesum} m={(cesum//2)+1} by-support={dict(sorted(total.items()))}")

if __name__ == "__main__":
    for n in (5, 6, 7, 9, 10, 11, 13):
        analyze(n)
