#!/usr/bin/env python3
"""Deliverables 1+2, incremental to n=1e5 (sieve 2e7, 1,270,607 primes).

Faithful diagonal convention (matches the task's definition): delta(q_n) has
length n, delta_k = A_k[n-k], terminal delta_{n-1} = A_{n-1}[0] (success bit).
0-2 cycle = maximal {0,2} suffix of (delta_2..delta_{n-2});  nu2 = count of 2s.

Reproduction link (checked in code/reproduce_lemma54_indexed.py): the operator's
recorded nu2 sample {26,42,98,203,389,785,1604,2048} equals count of 2s in the
maximal {0,2} suffix of d[2:-1] of delta(q_{n+1}) truncated — same 0-2-cycle
notion, off-by-one in the n label only.  Both give nu2/n ~ 0.5 and Lemma 5.4
hypothesis holding with huge margin, so the deliverable conclusions are robust
to the shift.

Reports nu2(n), nu2/n, signed fluctuation nu2-n/2, whether nu2 stays within
C*sqrt(n log n) of n/2 (LIL honest target), whether a lower bound nu2>n^beta
with beta>0.525 is plausibly supported, and the Lemma 5.4 hypothesis count.

O(N^2) abs-diffs, O(N) memory.  Exact integers.
"""
import time, math, sys
from lib.gilbreath import primes_up_to
from lib.rightdiag import cycle_and_nu2


def main():
    NMAX = 100_000
    SIEVE = 20_000_000
    t0 = time.time()
    P = primes_up_to(SIEVE)
    if len(P) < NMAX + 2:
        print("need", NMAX + 2, "primes, have", len(P)); sys.exit(1)
    t1 = time.time()

    # incremental diagonals, faithful: D = delta(q_n) length n
    assert P[0] == 2
    D = [P[0]]                     # delta(q_1), length 1
    gstar = P[1] - P[0]            # g_2 = max so far

    samples = [50, 100, 200, 400, 800, 1600, 3200, 3999,
               5000, 10000, 20000, 50000, 100000]
    stats = []
    band_ok = True; band_n = None
    max_fluc = 0.0; max_fluc_n = 0
    min_ratio_ge1000 = 1.0
    hyp_viol = 0; hyp_checked = 0
    success_count = 0

    for n in range(2, NMAX + 1):
        # nu2 of delta(q_{n-1}) = current D (budget supplier for q_n)
        _, nu2_budget = cycle_and_nu2(D)
        budget = 2 * nu2_budget + 2
        g = P[n - 1] - P[n - 2]          # g_n = q_n - q_{n-1}
        if g > gstar:
            gstar = g
        hyp_checked += 1
        if gstar > budget:
            hyp_viol += 1
        # extend D (= delta(q_{n-1}), length n-1) to delta(q_n), length n
        newD = [0] * n
        newD[0] = P[n - 1]
        for k in range(1, n):
            newD[k] = abs(newD[k - 1] - D[k - 1])
        D = newD

        if D[-1] == 1:
            success_count += 1

        # report nu2 of delta(q_n)
        _, nu2 = cycle_and_nu2(D)

        # fluctuation / band
        fluc = abs(nu2 - n / 2.0)
        if fluc > max_fluc:
            max_fluc = fluc; max_fluc_n = n
        if n >= 1000:
            r = nu2 / n
            if r < min_ratio_ge1000:
                min_ratio_ge1000 = r
            if fluc > 3.0 * math.sqrt(n * math.log(n)):
                band_ok = False; band_n = n

        if n in samples:
            stats.append((n, nu2, nu2 / n, nu2 - n / 2.0, gstar, budget, D[-1]))

    t2 = time.time()
    print("== nu2(n) incremental to n=%d  (sieve 2e7, %d primes) ==" % (NMAX, len(P)))
    print("sieve %.2fs, incremental diagonal %.2fs" % (t1 - t0, t2 - t1))
    print("%-8s %-8s %-7s %-11s %-7s %-9s %-6s %s" %
          ("n", "nu2", "nu2/n", "nu2-n/2", "g*", "2nu2+2", "term", "hyp"))
    for n, nu2, r, fl, g, b, term in stats:
        print("%-8d %-8d %-7.4f %-11.3f %-7d %-9d %-6d %s" %
              (n, nu2, r, fl, g, b, term, "OK" if g <= b else "VIOL"))
    print()
    print("nu2/n range over samples: %.4f .. %.4f" % (
        min(s[2] for s in stats), max(s[2] for s in stats)))
    print("min nu2/n for all n>=1000 (tracked): %.4f" % min_ratio_ge1000)
    print("max |nu2-n/2| = %.3f at n=%d" % (max_fluc, max_fluc_n))
    print("nu2 stays within 3*sqrt(n log n) of n/2 for all n in 1000..%d: %s" %
          (NMAX, "YES" if band_ok else "FAIL first at n=%d" % band_n))
    print("n^0.525 at n=%d = %.2f" % (NMAX, NMAX ** 0.525))
    low = all(nu2 > (n ** 0.55) for n, nu2, _, _, _, _, _ in stats)
    print("nu2 > n^0.55 at every sample: %s" % low)
    # weakest beta such that nu2 > n^beta across samples
    beta = min(math.log(nu2) / math.log(n) for n, nu2, _, _, _, _, _ in stats)
    print("weakest implied exponent min(log nu2/log n) = %.4f (>0.525 = enough for Lemma5.4 route)" % beta)
    print()
    print("== Deliverable 2: Lemma 5.4 hypothesis g*_n <= 2*nu2(n-1)+2 ==")
    print("checked over n=2..%d: %d violations of %d (%.5f%%)" %
          (NMAX, hyp_viol, hyp_checked, 100.0 * hyp_viol / hyp_checked))
    print("successes (terminal==1) at all n: %d of %d" % (success_count, NMAX - 1))

    return stats


if __name__ == "__main__":
    main()
