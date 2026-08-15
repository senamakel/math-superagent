"""Cross-prime minus-class-number divisibility sweep.

For every pair of distinct odd primes p, q <= LIMIT, compute exactly
    q | h^-(Q(zeta_p))   and   p | h^-(Q(zeta_q))
by exact integer division of the analytic minus class number
    h^-(Q(zeta_p)) = 2p * prod_{chi odd} (-1/2 * B_{1,chi})
(computed in exact cyclotomic arithmetic, no floats — see lib.cyclo.h_minus).

The h^- computation for primes near 300 is the expensive part (polynomial in
p, with heavy exact cyclotomic reduction), so it is parallelised across the
28 CPUs with a multiprocessing pool.  The divisibility matrix itself is then
a cheap O(n^2) exact-integer pass.

Output: every surviving pair (p, q) with BOTH divisibilities, plus the known
double-Wieferich pairs (83, 4871) and (2903, 18787) and their intersection.
"""
import sys, time
from fractions import Fraction
from multiprocessing import Pool

from lib.cond import crossprime_condition, is_odd_prime, odd_primes_upto, double_wieferich_pairs
from lib.cyclo import h_minus


def _compute(p):
    return (p, h_minus(p))


def sweep(limit, processes=28):
    t0 = time.time()
    primes = odd_primes_upto(limit)
    n = len(primes)

    # Compute h^- for every odd prime <= limit, in parallel (exact integers).
    th = time.time()
    with Pool(processes=processes) as pool:
        rows = pool.map(_compute, primes, chunksize=1)
    hminus = dict(rows)
    t_hminus = time.time() - th
    print("computed h^- for %d odd primes <= %d in %.1fs" % (n, limit, t_hminus), flush=True)

    # Show the first terms to confirm the routine (oracle check).
    print("h^- sequence (p -> h^-):")
    for p in primes:
        print("  p=%3d  h^-=%d" % (p, hminus[p]), flush=True)

    # Cross-prime divisibility matrix: exact integer division, O(n^2).
    tm = time.time()
    surviving = []
    for i, p in enumerate(primes):
        for q in primes[i + 1:]:
            c = crossprime_condition(p, q, hminus=hminus)
            if c["satisfied"]:
                surviving.append((p, q))
    t_matrix = time.time() - tm
    total = time.time() - t0

    print("matrix built in %.2fs (exact integer division)" % t_matrix)
    print("SURVIVING pairs (both q | h^-(p) and p | h^-(q)), p < q <= %d:" % limit)
    for (p, q) in surviving:
        print("  (%d, %d)" % (p, q))
    print("count surviving = %d" % len(surviving))

    # Intersection with known double-Wieferich pairs (values authoritative
    # regardless of whether they are within the sweep limit).
    known_dw = [(83, 4871), (2903, 18787)]
    dw_within = [(p, q) for (p, q) in known_dw if p <= limit and q <= limit]
    print("known double-Wieferich pairs:", known_dw)
    print("  within bound (both <= %d): %s" % (limit, dw_within))
    survivor_set = set(surviving)
    inter = [(p, q) for (p, q) in known_dw if (p, q) in survivor_set]
    print("intersection of survivors with known double-Wieferich pairs:", inter)
    print("(p,q)=(2,3) known solution excluded-by-hypothesis (p even): ",
          crossprime_condition(2, 3, hminus=hminus)["satisfied"] is None)

    # Partial evaluation of DW pair (83, 4871): 4871 | h^-(Q(zeta_83)) is
    # computable (p=83 is cheap); 83 | h^-(Q(zeta_4871)) would need p=4871,
    # astronomically out of reach, so that half is reported as infeasible.
    if 83 <= limit:
        h83 = hminus[83]
        print("partial DW evaluation (83, 4871): 4871 | h^-(83) =",
              (h83 % 4871 == 0), "  (83 | h^-(4871): infeasible, p=4871)")

    print("TOTAL runtime %.2fs" % total)
    return surviving, inter


if __name__ == "__main__":
    limit = int(sys.argv[1]) if len(sys.argv) > 1 else 300
    sweep(limit)
