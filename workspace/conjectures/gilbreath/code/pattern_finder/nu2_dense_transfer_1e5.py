#!/usr/bin/env python3
"""Dense nu2 <-> w transfer check extended to n = 100000.

Extends code/pattern_finder/nu2_dense_transfer.py (which ran to N=30000) using
the same reference machinery: exact-integer incremental right diagonal through
q_n (cycle_and_nu2 from lib.rightdiag) and the mod-4 gap bits hbit[i] =
((P[i+1]-P[i])//2) % 2 over the fixed ancestor window i in [2, n-1]
(prefix-summed so w(n) is O(1)):

   nu2(n) = #2s in the maximal {0,2} suffix of delta(q_n);
   w(n)   = Hamming weight of the halved mod-4 gap bits in [2, n-1].

This is the supply side of Granville Route B (G-supply): nu2 >= c*w is a
two-point prime-gap-mod-4 correlation lower bound.  The falsification checks
here are EXACT-integer (2*nu2 >= w  for the 0.5 bound, 4*nu2 >= 3*w for 0.75;
no floats in the falsification, so a reported violation is a fact).

Reports:
  (1) does nu2 >= 0.5*w hold for ALL n in [17, 100000]?  first falsifier and
      count over [1, 100000].
  (2) does nu2 >= 0.75*w hold for all n >= 4000 in [4000, 100000]?
  (3) exact min ratio nu2/w over n >= 17 and over n >= 4000 (did the n=44
      tight 0.5 survive; did the n=1005 0.75 violation remain the last?).
  (4) worst |2*nu2 - n| / sqrt(n*log n) and where.

Exact integers for every falsification; floats only for the reported min-ratio
and the fluct statistic.  O(N^2) absolute differences, O(N) memory
(incremental diagonal), O(N) prefix-sum for w.
"""
import time, math, sys
from lib.gilbreath import primes_up_to
from lib.rightdiag import cycle_and_nu2


def main():
    NMAX = 100000
    SIEVE = 1_500_000          # > 100002 primes (1300000 gives 100021)
    t0 = time.time()
    P = primes_up_to(SIEVE)
    if len(P) < NMAX + 2:
        print("need", NMAX + 2, "primes, have", len(P)); sys.exit(1)
    t1 = time.time()

    # mod-4 gap bits: hbit[i] is bit of gap g_{i+1} (P[i+1]-P[i]).
    hbits = [((P[i + 1] - P[i]) // 2) % 2 for i in range(len(P) - 1)]
    # prefix sums so w(n) = WS[n] - WS[2]  == sum over i in [2, n-1]
    # (matches the reference sum(hbits[2:n]) exactly).
    WS = [0] * (len(hbits) + 1)
    for i in range(len(hbits)):
        WS[i + 1] = WS[i] + hbits[i]

    def w(n):
        # n >= 2 ; sum of hbits[i] for i in [2, n-1]
        return WS[n] - WS[2]

    # incremental diagonal
    D = [P[0]]
    min_rw_17 = float('inf'); min_rw_17_n = 0
    min_rw_4000 = float('inf'); min_rw_4000_n = 0
    first_bad_50 = None          # first n in [17,N] with 2*nu2 < w
    count_bad_50_17 = 0          # count over [17, N]
    count_bad_50_full = 0        # count over [1, N]
    count_bad_75_4000 = 0        # count over [4000, N] with 4*nu2 < 3*w
    first_bad_75_4000 = None
    worst_fluc = 0.0; worst_fluc_n = 0
    worst_fluc_val = 0

    for n in range(1, NMAX + 1):
        if n >= 2:
            newD = [0] * n
            newD[0] = P[n - 1]
            for k in range(1, n):
                newD[k] = abs(newD[k - 1] - D[k - 1])
            D = newD
        _, nu2 = cycle_and_nu2(D)

        if n >= 2:
            wn = w(n)
            if wn > 0:
                # exact-integer falsifications (no floats here)
                if 2 * nu2 < wn:                       # nu2 < 0.5*w
                    count_bad_50_full += 1
                    if n >= 17:
                        count_bad_50_17 += 1
                        if first_bad_50 is None:
                            first_bad_50 = (n, nu2, wn)
                if n >= 4000 and 4 * nu2 < 3 * wn:     # nu2 < 0.75*w
                    count_bad_75_4000 += 1
                    if first_bad_75_4000 is None:
                        first_bad_75_4000 = (n, nu2, wn)
                # min ratio (float only for the reported value)
                r = nu2 / float(wn)
                if n >= 17 and r < min_rw_17:
                    min_rw_17 = r; min_rw_17_n = n
                if n >= 4000 and r < min_rw_4000:
                    min_rw_4000 = r; min_rw_4000_n = n

        # (4) worst |2*nu2 - n| / sqrt(n log n)
        if n >= 3:
            denom = math.sqrt(n * math.log(n))
            fluc = abs(2 * nu2 - n) / denom
            if fluc > worst_fluc:
                worst_fluc = fluc; worst_fluc_n = n
                worst_fluc_val = abs(2 * nu2 - n)

        if n % 5000 == 0:
            wn = w(n) if n >= 2 else 0
            print("n=%6d nu2=%6d  w=%6d  nu2/w=%.3f  fluc/denom=%.3f" %
                  (n, nu2, wn, nu2 / float(wn) if wn else 0,
                   abs(2 * nu2 - n) / math.sqrt(n * math.log(n))),
                  flush=True)

    t2 = time.time()
    print("\n== dense nu2<->w transfer to N=%d (sieve %d, %d primes) ==" %
          (NMAX, SIEVE, len(P)))
    print("sieve %.1fs, incremental diagonal %.1fs" % (t1 - t0, t2 - t1))

    print("\n(1) nu2 >= 0.5*w for n in [17, %d]: %s  first falsifier: %s"
          % (NMAX, "YES" if first_bad_50 is None else "NO", first_bad_50))
    print("    count nu2<0.5*w over [1,%d] = %d ; over [17,%d] = %d" %
          (NMAX, count_bad_50_full, NMAX, count_bad_50_17))

    print("\n(2) nu2 >= 0.75*w for n in [4000, %d]: %s  first falsifier: %s"
          % (NMAX, "YES" if first_bad_75_4000 is None else "NO",
             first_bad_75_4000))
    print("    count nu2<0.75*w over [4000,%d] = %d" %
          (NMAX, count_bad_75_4000))

    print("\n(3) min nu2/w over n>=17       = %.6f at n=%d" %
          (min_rw_17, min_rw_17_n))
    print("    min nu2/w over n>=4000     = %.6f at n=%d" %
          (min_rw_4000, min_rw_4000_n))

    print("\n(4) worst |2*nu2 - n|/sqrt(n log n) = %.6f at n=%d"
          "  (|2*nu2-n| = %d)" % (worst_fluc, worst_fluc_n, worst_fluc_val))


if __name__ == "__main__":
    main()
