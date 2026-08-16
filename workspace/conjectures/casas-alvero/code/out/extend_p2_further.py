"""Exact p=2 Hasse-CA satisfier count for monic degree-n polys over F2,
extending the multiplier sequence m(n,2)=sat/2 to test the popcount
conjecture at fresh n beyond those already on disk.

Conjecture under test (from extend_p2_popcount.py):
    m(n,2) depends only on popcount(n); population so far:
      pc=1 -> 1 ; pc=2 -> 2 ; pc=3 -> 8 ; pc=4 -> 457 BUT n=23 gives 466
      (popcount hypothesis ALREADY FALSIFIED at pc=4: 457 vs 466).
New questions:
  - n=25,26 (pc=3): does pc=3 stay at 8?
  - n=27 (pc=4): a THIRD pc=4 point; does it give 457, 466, or a new value?
  - n=28 (pc=3), n=29,30 (pc=4), n=31 (pc=5, first!).
Exact bit-arithmetic; oracle-checked against lib at small n.

This is an EXPONENTIAL oracle (enumerates all 2^n monic polys), used only at
bounded n to test a structural conjecture (rule 9).
"""
from multiprocessing import Pool
import sys


def hasse_deriv(fbits, i):
    out = 0
    j = 0
    fb = fbits
    while fb:
        if fb & 1:
            if (i & j) == i:
                out |= 1 << (j - i)
        fb >>= 1
        j += 1
    return out


def pmod(a, b):
    bl = b.bit_length()
    while a.bit_length() >= bl:
        a ^= b << (a.bit_length() - bl)
    return a


def pgcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    while b:
        a, b = b, pmod(a, b)
    return a


def is_ca_f2(fbits):
    n = fbits.bit_length() - 1
    for i in range(1, n):
        hi = hasse_deriv(fbits, i)
        if hi == 0:
            continue
        if pgcd(fbits, hi) == 1:
            return False
    return True


def _count_chunk(args):
    n, lo, hi = args
    total = 0
    for v in range(lo, hi):
        fbits = (1 << n) | v
        if is_ca_f2(fbits):
            total += 1
    return total


def sat_count(n, workers):
    size = 1 << n
    CH = 1 << 18
    bounds = [(n, lo, min(lo + CH, size)) for lo in range(0, size, CH)]
    with Pool(workers) as pool:
        parts = pool.map(_count_chunk, bounds, chunksize=1)
    return sum(parts)


if __name__ == "__main__":
    nlist = [int(x) for x in sys.argv[1].split(",")]
    workers = int(sys.argv[2]) if len(sys.argv) > 2 else 28
    for n in nlist:
        if n > 27:
            print(f"n={n}: refusing (2^n={1<<n} too large for exhaustive oracle)")
            continue
        sat = sat_count(n, workers)
        m = sat // 2
        pop = bin(n).count("1")
        print(f"n={n:2d} 2^n={1<<n:9d} popcount={pop} sat={sat:9d} m=sat/2={m:6d}", flush=True)
