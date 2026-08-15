#!/usr/bin/env python3
"""Extended exact-integer verification that T(c,p) = (x^p-1)/(x-1), x=c^2+1,
is never a perfect square, for c in [1, cmax] and every odd prime p in [3,pmax].

Prior state: c<=2000, odd prime p<=101 (50000 pairs, 0 squares).
This run extends to cmax=10^5, pmax=500, parallelised over 28 CPUs.

Every arithmetic step is exact integers (pow + integer isqrt). No floats.
Each job is a contiguous range of c values (so few jobs, small pickle).
"""
import math
import multiprocessing as mp
import time
import sys


def is_odd_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def check_c_range(c_start, c_end, primes):
    """Return list of square findings (c,p,T) for c in [c_start, c_end)."""
    found = []
    for c in range(c_start, c_end):
        x = c * c + 1
        xm1 = c * c
        for p in primes:
            T = (pow(x, p) - 1) // xm1
            s = math.isqrt(T)
            if s * s == T:
                found.append((c, p, T))
    return found


def worker(args):
    c_start, c_end, primes = args
    return check_c_range(c_start, c_end, primes)


def main():
    cmax = 100_000
    pmax = 500
    primes = [p for p in range(3, pmax + 1) if is_odd_prime(p)]
    nprimes = len(primes)
    total_pairs = cmax * nprimes
    p1m4 = [p for p in primes if p % 4 == 1]
    surviving = (cmax // 2) * len(p1m4)

    print(f"Extended verification: T(c,p) not a square")
    print(f"  c in [1,{cmax}], odd prime p in [3,{pmax}] ({nprimes} primes)")
    print(f"  total (c,p) pairs: {total_pairs:,}")
    print(f"  surviving class (c even, p==1 mod4): {surviving:,}")
    print(f"  parallel over {mp.cpu_count()} CPUs; exact integer arithmetic")

    t0 = time.time()
    ncpu = mp.cpu_count()
    ncores = min(ncpu, 28)
    # one job per c range, sized so there are ~8x cores jobs
    RANGESZ = 2000
    c_ranges = [(start, min(start + RANGESZ, cmax + 1))
                for start in range(1, cmax + 1, RANGESZ)]
    jobs = [(s, e, primes) for (s, e) in c_ranges]

    n_squares = 0
    all_squares = []
    done = 0
    with mp.Pool(ncores) as pool:
        for res in pool.imap_unordered(worker, jobs):
            for sq in res:
                n_squares += 1
                all_squares.append(sq)
            done += 1
            if done % 8 == 0:
                csofar = done * RANGESZ
                print(f"  ... {csofar:,}/{cmax:,} c el, {time.time()-t0:.1f}s, "
                      f"squares {n_squares}", flush=True)
    dt = time.time() - t0

    print(f"\nFINAL: pairs checked {total_pairs:,}  runtime {dt:.1f}s")
    print(f"  squares found: {n_squares}")
    for sq in all_squares:
        print(f"     SQUARE: c={sq[0]} p={sq[1]}")
    ok = n_squares == 0
    print(f"  RESULT: {'0 squares over '+format(total_pairs,',')+' pairs' if ok else 'SQUARES FOUND'}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
