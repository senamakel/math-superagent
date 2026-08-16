"""Parallel F2 Hasse-CA counterexample count (popcount study).

Extends extend_p2_multiplier.counts to n where 2^n enumeration needs the
28 CPUs.  Splits the v in [0, 2^n) space across workers, each counting
satisfiers and counterexamples locally, then sums.  Exact bit-arithmetic.
"""
import sys
from math import comb
from multiprocessing import Pool


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


def Cparity(n, k):
    return (k & n) == k


def is_pure_power_f2(fbits, n):
    if fbits == (1 << n):
        return True
    bits = 0
    for j in range(n + 1):
        if Cparity(n, j):
            bits |= 1 << j
    return fbits == bits


def worker(args):
    n, lo, hi = args
    sat = ce = 0
    top = (1 << n)
    for v in range(lo, hi):
        fbits = top | v
        if is_ca_f2(fbits):
            sat += 1
            if not is_pure_power_f2(fbits, n):
                ce += 1
    return sat, ce


def counts(n, nproc=28):
    total = 1 << n
    step = (total + nproc - 1) // nproc
    jobs = [(n, i, min(i + step, total)) for i in range(0, total, step)]
    tot_sat = tot_ce = 0
    with Pool(nproc) as p:
        for sat, ce in p.imap_unordered(worker, jobs, chunksize=1):
            tot_sat += sat
            tot_ce += ce
    return tot_sat, tot_ce


if __name__ == "__main__":
    nmax = int(sys.argv[1]) if len(sys.argv) > 1 else 27
    nproc = int(sys.argv[2]) if len(sys.argv) > 2 else 28
    for n in range(20, nmax + 1):
        if (1 << n) > 2 ** 30:
            print(f"n={n}: skip (2^n={1<<n} too large)")
            continue
        sat, ce = counts(n, nproc)
        pc = bin(n).count("1")
        print(f"n={n:2d} pc={pc} 2^n={1<<n:9d} sat={sat:9d} m={sat//2:6d} "
              f"ce={ce}", flush=True)
