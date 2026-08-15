#!/usr/bin/env python3
"""Extended two-point measurement of the prime mod-4 switch bit.

Switch bit h[k] = 1 iff p_{k+1} - p_k == 2 (mod 4), over gaps g_3..g_N
(matching prior switch_autocorr_2pt.py: bits over k=3..N, so the ballot
e(n)=2w(n)-(n-2) runs over gates g_3..g_n).

This builds a memory-efficient SEGMENTED odd-only sieve (bytearray, streamed
segment by segment; no full list of primes is ever materialized) to reach the
TARGET-th prime (default 2e8, sieve limit ~4.4e9, well under 8 GiB).

Outputs (exact counts; floats only for the r_lag correlation values):
  (1) primes reached / switch-bit length
  (2) centered autocorrelations r_lag, lags 1..40
  (3) drift 2*E[h]-1
  (4) ballot e(n)=2w(n)-(n-2) >= 0 over ALL prefixes (exact integer cumsum)
  (5) falsifier verdict: lag-1 negative, drift positive, |r_lag|>0.005 at lag>=2

Mathematical basis: the centered autocovariance of a 0/1 sequence at lag L,
  sum_{j<n-L} (b_j - mu)(b_{j+L})
  = count11 - mu*(sum_x + sum_y) + mu^2*(n-L)
with count11 = sum b_j b_{j+L} (exact integer), sum_x = sum_{j<n-L} b_j,
sum_y = sum_{j>=L} b_j, and var = mu(1-mu) (Bernoulli). Slices are modern
numpy uint8 views/dot products; nothing but the final divisions is float.

Exact integers for every count (prime gaps, weight w, ballot). The balloon
e is a +/-1 prefix walk; e>=0 for all prefixes iff min of px-cumsum >= 0.

Complexity: sieve O(L loglog L + L) marking in C; the per-lag dot over the
bit array is O(n) each, 40 lags -> O(40 n) vectorized; peak memory the bit
array (n bytes) + one int64 cumsum (8n) transient + one segment buffer.
"""

import argparse
import math
import time

import numpy as np


def base_primes(lim):
    """Primes up to lim, odd-only bytearray sieve with slice assignment."""
    if lim < 2:
        return []
    sieve = bytearray(b"\x01") * (lim + 1)
    sieve[0] = sieve[1] = 0
    for i in range(2, math.isqrt(lim) + 1):
        if sieve[i]:
            sieve[i * i::i] = b"\x00" * (((lim - i * i) // i) + 1)
    return [i for i in range(2, lim + 1) if sieve[i]]


def segment_odd_primes(lo, hi, base_odd):
    """Odd primes in [lo, hi). Returns numpy int64 array (empty if none).

    Only odd numbers in [lo,hi) are stored: position j represents O0+2j where
    O0 is the first odd >= lo. Multiples of each base prime p (odd) are
    crossed off, starting from the first ODD multiple of p that is
    >= max(p*p, O0) and stepping by p in index space (=2p in number space).
    """
    if lo >= hi:
        return np.empty(0, dtype=np.int64)
    O0 = lo | 1                  # first odd >= lo (works for even and odd lo)
    size = (hi - O0 + 1) // 2
    if size <= 0:
        return np.empty(0, dtype=np.int64)
    buf = bytearray(b"\x01") * size
    for p in base_odd:
        pp = p * p
        if pp >= hi:
            break  # no composite multiple of p in this segment
        X = pp if pp > O0 else O0
        k = (X + p - 1) // p
        if k % 2 == 0:
            k += 1  # odd multiple of odd p
        start = (p * k - O0) // 2
        if start < size:
            buf[start::p] = b"\x00" * (((size - 1 - start) // p) + 1)
    idx = np.nonzero(np.frombuffer(buf, dtype=np.uint8))[0]
    return O0 + 2 * idx


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--target", type=int, default=200_000_000,
                    help="number of primes to reach")
    ap.add_argument("--limit", type=int, default=4_400_000_000,
                    help="sieve limit (must be > target-th prime)")
    ap.add_argument("--seg", type=int, default=100_000_000,
                    help="numeric span per segment")
    ap.add_argument("--small", action="store_true",
                    help="smoke test: target 1_000_002 primes")
    args = ap.parse_args()

    target = args.target if not args.small else 1_000_002
    LIMIT = args.limit
    SEG = args.seg

    bsqrt = math.isqrt(LIMIT)
    t0 = time.time()
    base = base_primes(bsqrt)
    base_odd = [p for p in base if p >= 3]
    print("base primes up to sqrt(%d)=%d : %d  (%.1fs)"
          % (LIMIT, bsqrt, len(base), time.time() - t0))

    # small primes 2,3,5 handled manually; stream from lo=6 (odd 7) onward.
    gap_bits = bytearray()  # gap bits for ALL consecutive prime gaps, incl 1,2
    init = np.array([2, 3, 5], dtype=np.int64)
    dinit = np.diff(init)
    gap_bits += ((dinit // 2) & 1).astype(np.uint8).tobytes()
    prev = 5
    prime_count = 2  # gaps emitted so far (for 3 and 5)

    lo = 6
    while lo <= LIMIT and len(gap_bits) < target - 2:
        hi = min(lo + SEG, LIMIT + 1)
        pseg = segment_odd_primes(lo, hi, base_odd)
        if len(pseg):
            room = (target - 2) - len(gap_bits)
            if len(pseg) > room:
                pseg = pseg[:room]
            withp = np.concatenate(([prev], pseg))
            dseg = np.diff(withp)
            gap_bits += ((dseg // 2) & 1).astype(np.uint8).tobytes()
            prev = int(pseg[-1])
            prime_count += len(pseg)
        lo = hi

    # bits over gaps g_3..g_N : drop the first two gap bits (gap_1, gap_2)
    bits = gap_bits[2:]
    n = len(bits)
    print("primes consumed (gaps emitted incl 1,2): %d" % (prime_count + 2))
    print("switch-bit length n = %d  (target %d)" % (n, target - 2))

    arr = np.frombuffer(bits, dtype=np.uint8)
    w = int(arr.sum())
    mu = w / n
    drift = 2 * mu - 1
    print("weight w = %d  (density %.6f)" % (w, mu))
    print("per-step drift 2*E[h]-1 = %.4f" % drift)

    # ---- (4) ballot over ALL prefixes, exact ----
    steps = 2 * arr.astype(np.int8) - 1          # +1 on switch(1), -1 on stay(0)
    csum = np.cumsum(steps, dtype=np.int64)
    emin = int(csum.min()) if n else 0
    ballot_ok = emin >= 0
    print("ballot e(n)=2w(n)-(n-2) >= 0 over all prefixes: %s (global min e = %d)"
          % ("YES" if ballot_ok else "NO", emin))
    print("final e(n) = 2*w - (n-2) = %d" % (2 * w - (n - 2)))

    # ---- (2) centered autocorrelations, lags 1..40 ----
    var = mu * (1 - mu)                          # Bernoulli variance, exact formula
    LMAX = 40
    print("\n== centered autocorrelation of switch bit, lags 1..%d ==" % LMAX)
    table = []
    for L in range(1, LMAX + 1):
        x = arr[:-L]
        y = arr[L:]
        # uint8 dot would overflow its accumulator; cast to int64 for an
        # exact integer count.
        count11 = int(np.dot(x.astype(np.int64), y.astype(np.int64)))
        sx = int(x.sum())
        sy = int(y.sum())
        num = count11 - mu * (sx + sy) + mu * mu * (n - L)
        r = (num / (n - L)) / var if var else 0.0
        table.append(r)
        print("lag %2d : r=%.4f" % (L, r))

    # ---- (5) falsifier verdict ----
    lag1 = table[0]
    max_ge2 = max((abs(r) for r in table[1:]), default=0.0)
    ge2_exceed = max_ge2 > 0.005
    ge2_lag = max(range(2, LMAX + 1), key=lambda L: abs(table[L - 1]))
    print("\n-- falsifier verdict --")
    print("lag-1 negative (anti-clustering)? %s (r=%.4f)"
          % ("YES" if lag1 < 0 else "NO", lag1))
    print("drift positive? %s (2E[h]-1=%.4f)" % ("YES" if drift > 0 else "NO", drift))
    print("any lag>=2 |r| > 0.005? %s (max %.4f at lag %d)"
          % ("YES" if ge2_exceed else "NO", max_ge2,
             ge2_lag))
    print("total time %.1fs" % (time.time() - t0))


if __name__ == "__main__":
    main()
