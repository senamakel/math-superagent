"""Parallel exact F2 Hasse-CA satisfier count, extending the multiplier
sequence m(n,2)=sat(n,2)/2 to test the popcount conjecture:

    CONJECTURE: m(n,2) depends only on popcount(n) = number of set bits of n.
      popcount 1 -> m=1 ; 2 -> 2 ; 3 -> 8 ; 4 -> 457 ; 5 -> ?

Polynomial over F2 stored as int (bit j = coeff of x^j).  i-th Hasse derivative
H_i has coeff of x^j = C(j,i) mod 2 = 1 iff (i & j) == i (Lucas).  gcd by
Euclid on bit-polynomials.  Hasse-CA iff gcd(f,H_i) non-constant for all
i=1..n-1 (gcd(f,0)=f trivially non-constant -> a vanishing H_i passes).

This is an EXPONENTIAL oracle (enumerates all 2^n monic polys) used only to
verify/test a structural conjecture at bounded n.  The value at one n answers:
does m(n,2) match the value already known for popcount(n)?
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


def _count_chunk(args):
    n, lo, hi = args
    total = 0
    for v in range(lo, hi):
        fbits = (1 << n) | v
        ok = True
        for i in range(1, n):
            hi_ = hasse_deriv(fbits, i)
            if hi_ == 0:
                continue
            if pgcd(fbits, hi_) == 1:
                ok = False
                break
        if ok:
            total += 1
    return total


def sat_count(n, workers):
    size = 1 << n
    CH = 1 << 18          # chunk ~262144
    bounds = [(n, lo, min(lo + CH, size)) for lo in range(0, size, CH)]
    with Pool(workers) as pool:
        parts = pool.map(_count_chunk, bounds, chunksize=1)
    return sum(parts)


if __name__ == "__main__":
    workers = int(sys.argv[2]) if len(sys.argv) > 2 else 28
    n = int(sys.argv[1])
    if n > 28:
        print(f"refusing n={n}: 2^n too large for exhaustive oracle")
        sys.exit(2)
    sat = sat_count(n, workers)
    m = sat // 2
    pop = bin(n).count("1")
    print(f"n={n} 2^n={1<<n} popcount={pop} sat={sat} m=sat/2={m}")
