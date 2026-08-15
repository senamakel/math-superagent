#!/usr/bin/env python3
"""Dense test of the nu2 <-> w transfer bound (supply side of Granville Route B).

nu2(n) = count of 2s in the maximal {0,2} suffix of the prime right diagonal
         through q_n.  w(n) = Hamming weight of the mod-4 gap bits in the
         ancestor window: hb[i] = ((P[i+1]-P[i])//2) % 2  (bit == 1 iff gap
         g_{i+1} == 2 mod 4), summed over i in [2, n-1] (mirrors the reference
         nu2_vs_gap_parity.py window hbits[2:n]).

For EVERY n in 2..N:
  - transfer ratio nu2/w and min over all n
  - does nu2 >= c*w hold for c in {0.6, 0.5}?
  - nu2/n and the supply-beta check nu2 > n^0.525 for n>=4000

Exact integers. O(N^2) abs-diffs, O(N) memory, incremental diagonal.
"""
import time, math, sys
from lib.gilbreath import primes_up_to
from lib.rightdiag import cycle_and_nu2


def main():
    NMAX = 30000
    SIEVE = 1_000_000
    t0 = time.time()
    P = primes_up_to(SIEVE)
    if len(P) < NMAX + 2:
        print("need", NMAX + 2, "primes, have", len(P)); sys.exit(1)
    t1 = time.time()

    # mod-4 gap bits, faithful to nu2_vs_gap_parity.py: hbits[i]=bit of gap g_{i+1}
    hbits = [((P[i+1] - P[i]) // 2) % 2 for i in range(len(P) - 1)]

    # incremental diagonal
    D = [P[0]]
    min_rw = 1.0; min_rw_n = 0
    min_rn = 1.0; min_rn_n = 0
    beta_min = 1.0
    max_fluc = 0.0; max_fluc_n = 0
    store_nu2 = []
    bad60 = []; bad50 = []
    for n in range(1, NMAX + 1):
        if n >= 2:
            newD = [0]*n
            newD[0] = P[n-1]
            for k in range(1, n):
                newD[k] = abs(newD[k-1] - D[k-1])
            D = newD
        _, nu2 = cycle_and_nu2(D)
        store_nu2.append(nu2)
        if n >= 2:
            w = sum(hbits[2:n])
            if w > 0:
                r = nu2 / float(w)
                if r < min_rw:
                    min_rw = r; min_rw_n = n
                if nu2 < 0.6*w:
                    bad60.append(n)
                if nu2 < 0.5*w:
                    bad50.append(n)
        if n >= 1000:
            rn = nu2 / float(n)
            if rn < min_rn:
                min_rn = rn; min_rn_n = n
            be = math.log(nu2)/math.log(n)
            if be < beta_min:
                beta_min = be
        fluc = abs(nu2 - n/2.0)
        if fluc > max_fluc:
            max_fluc = fluc; max_fluc_n = n
        if n % 2500 == 0:
            w = sum(hbits[2:n]) if n >= 2 else 0
            print("n=%6d nu2=%6d w=%6d nu2/w=%.3f nu2/n=%.4f" %
                  (n, nu2, w, nu2/w if w else 0, nu2/n), flush=True)

    t2 = time.time()
    print("\n== dense transfer to N=%d (sieve %d, %d primes) ==" % (NMAX, SIEVE, len(P)))
    print("sieve %.1fs, diagonal %.1fs" % (t1 - t0, t2 - t1))
    print("min nu2/w over ALL n in [2,%d]: %.4f at n=%d" % (NMAX, min_rw, min_rw_n))
    print("  -> smallest c with nu2>=c*w on every n = %.4f" % min_rw)
    print("min nu2/n over n>=1000: %.4f at n=%d" % (min_rn, min_rn_n))
    print("weakest implied beta (min log nu2/log n, n>=1000): %.4f" % beta_min)
    print("max |nu2-n/2| = %.1f at n=%d" % (max_fluc, max_fluc_n))
    print("n with nu2 < 0.6*w : %d  first: %s" % (len(bad60), bad60[:5]))
    print("n with nu2 < 0.5*w : %d  first: %s" % (len(bad50), bad50[:5]))
    below = [n for n in range(4000, NMAX+1) if store_nu2[n-1] <= n**0.525]
    print("n in [4000,%d] with nu2 <= n^0.525 : %d first: %s" %
          (NMAX, len(below), below[:5]))

    with open("code/out/nu2_dense.txt", "w") as f:
        for i, v in enumerate(store_nu2, 1):
            f.write("%d %d\n" % (i, v))
    print("wrote code/out/nu2_dense.txt (%d terms)" % len(store_nu2))
    return store_nu2


if __name__ == "__main__":
    main()
