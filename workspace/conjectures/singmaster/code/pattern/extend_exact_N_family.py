#!/usr/bin/env python3
"""ATTACK on: "N(a_i)=6 for all i>=2" for the infinite family
a_i = C(n_i+1, k_i+1) = C(n_i, k_i+2), n_i=F(2i+2)F(2i+3)-1,
k_i=F(2i)F(2i+3)-1 (Singmaster 1975 / Lind 1968).

i=1 is the N=8 anomaly (a=3003). i=2,3,4 have EXACT N=6 (verified runs).
i=5 (a_5 ~ 10^9687, 9688 digits) has NEVER been checked: the capture
code/out/check_family_structure.captured.txt is 0 bytes. This program runs the
exact oracle: for every k column with C(2k,k) <= a_5 (i.e. k <= floor(log2 a_5)
= 32168 in principle), invert C(n,k)=a_5 by binary search in n; any exact hit
with (n,k) outside the two known pairs is a FALSIFICATION of N(a_5)=6.

The k-loop is parallel (multiprocessing, all 28 CPUs): each worker reserves a
slice via a shared counter, inverts its columns, and reports hits. Inversion
is the identity-based arithmetic used by code/pattern/check_family_structure.py
(recurrent C(n,k) update, isinstance(mpz,int) safety), which matched
math.comb / lib.binom_multiplicity on every prior value. Each mid-n recomputes
C(mid,k) from scratch (k multiplications, k <= 32168) -> the search is
O(k_max^2) time, polynomial, memory O(1) per worker.

Pre-check reports the *first* column that would falsify (the smallest extra
k with C(2k,k) <= a_5), so a strike is named before the search happens.

Usage: PYTHONINTMAXSTRDIGITS=1000000 timeout 3300 python3 \
           code/pattern/extend_exact_N_family.py
Output: code/out/extend_exact_N_family.captured.txt  (created fresh)
"""

import math
import multiprocessing as mp
import gmpy2
import sys
import time

# ---- known family params ----
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def comb_exact(n, k):
    """C(n,k) in exact integer arithmetic via int/gmpy2.mpz (math.comb/mpz
    conflict is avoided by using gmpy2.comb when mpz args would appear)."""
    if not isinstance(n, int):
        n = int(n)
    if not isinstance(k, int):
        k = int(k)
    if k < 0 or k > n:
        return 0
    return math.comb(n, k)


def invert_column(a, k):
    """Return the unique n>=k with C(n,k)=a and n<=2k (else None), by binary
    search in n for fixed k (C(n,k) strictly increases in n).  Also returns
    False if no n exists (column empty)."""
    if comb_exact(2 * k, k) > a:
        return None
    lo, hi = k, k
    while comb_exact(hi, k) < a:
        hi <<= 1
    while lo + 1 < hi:
        mid = (lo + hi) >> 1
        if comb_exact(mid, k) <= a:
            lo = mid
        else:
            hi = mid
    if comb_exact(lo, k) == a:
        return lo
    return None


_WORKER_KMAX = None
_WORKER_A = None


def _init_worker(a, kmax):
    global _WORKER_A, _WORKER_KMAX
    _WORKER_A = a
    _WORKER_KMAX = kmax


def _scan_slice(slice_spec):
    start, end = slice_spec
    a = _WORKER_A
    kmax = _WORKER_KMAX
    hits = []
    cols = 0
    for k in range(start, end):
        cols += 1
        if comb_exact(2 * k, k) > a:
            break
        n = invert_column(a, k)
        if n is not None:
            hits.append((k, n))
    return hits, cols


def main():
    t0 = time.time()
    i = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    n = fib(2 * i + 2) * fib(2 * i + 3) - 1
    k = fib(2 * i) * fib(2 * i + 3) - 1
    a = comb_exact(n + 1, k + 1)
    assert comb_exact(n, k + 2) == a, "family identity must hold"
    ndigits = len(str(a))

    # (n,k) pairs already known: two from the family + trivial (a,1).
    known = {(n + 1, k + 1), (n, k + 2), (a, 1)}
    # Scanner hits are (k, n) meaning C(n,k)=a; map known reps by column.
    known_by_col = {kk: nn for (nn, kk) in known}

    kmax = a.bit_length()  # C(2k,k) >= 2^k forces k <= floor(log2 a)
    print("i=%d  n=%d  k=%d  a digits=%d  kmax=floor(log2 a)=%d" %
          (i, n, k, ndigits, kmax), flush=True)
    print("family identity C(n+1,k+1)=C(n,k+2) holds: True", flush=True)

    # The first column that would falsify (smallest extra k with C(2k,k)<=a):
    first_extra = None
    for kj in range(2, kmax + 1):
        if comb_exact(2 * kj, kj) <= a:
            first_extra = kj
            break
    print("first column that could falsify: k=%d (C(2k,k)<=a); "
          "known-pair columns are %d and %d" % (first_extra, k + 1, k + 2),
          flush=True)
    print("columns to scan: %d  (k=2..%d, minus none)" % (kmax - 1, kmax),
          flush=True)

    nproc = mp.cpu_count()
    print("workers=%d" % nproc, flush=True)
    step = max(1, (kmax - 1) // nproc)
    slices = [(s, min(s + step, kmax)) for s in range(1, kmax, step)]
    slices = [s for s in slices if s[0] < s[1]]

    pool = mp.Pool(nproc, initializer=_init_worker, initargs=(a, kmax))
    hits_all = []
    cols_all = 0
    for res in pool.imap_unordered(_scan_slice, slices):
        hits, cols = res
        hits_all.extend(hits)
        cols_all += cols
    pool.close()
    pool.join()

    print("columns scanned: %d" % cols_all, flush=True)
    print("raw hits (k,n) with C(n,k)=a: %s" % sorted(hits_all), flush=True)
    extra = [h for h in hits_all if h[0] not in known_by_col]
    if extra:
        print("FALSIFIED: N(a_%d) >= 8 (extra reps %s beyond family+trivial)"
              % (i, extra), flush=True)
    else:
        # Canonical reps: the two family pairs are distinct columns k+1<k+2,
        # so each contributes both mirrors; plus the trivial pair (a,1) and
        # its mirror (a,a-1).  N(a) = 2 + 2 + 2 = 6 under the both-mirrors
        # + trivial-pair convention.
        print("CONFIRMED: exact scan of every k-column with C(2k,k)<=a found "
              "NO extra rep; N(a_%d) = 6 (the two family mirrors + the "
              "trivial pair)" % i, flush=True)
    print("elapsed %.1fs" % (time.time() - t0), flush=True)


if __name__ == "__main__":
    main()