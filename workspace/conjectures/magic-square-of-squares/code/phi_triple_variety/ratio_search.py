#!/usr/bin/env python3
"""code/phi_triple_variety/ratio_search.py — (A) ratio-form fast no-triple search.

Search for an additive triple q1, q2, q1+q2 with q1>q2>0 all in Phi,
using the ratio parametrisation f(m,n) = f(t=n/m) and the exact
membership test from code/lib/phi.py.

Cost model (exact): the set of distinct Phi values from primitive m <= M has
size |Phi(M)| ~ 0.2 M^2, so the full q1>q2 pair loop is ~0.5*|Phi|^2 ~
0.02 M^4 pairs.  Every pair that survives the cheap NECESSARY prefilter
(0 < sum < 1 AND both 1±sum rational squares — no candidate can be a Phi
member without both) is then confirmed by the authoritative uncapped
in_phi test.  The prefilter is ~all-selective, so the expensive tests are
few; the cost is dominated by the O(Phi^2) pair enumeration with cheap
per-pair arithmetic.

Usage:  python3 code/phi_triple_variety/ratio_search.py [M ...] [--timeout S]
Reaches M well past 400 (prior bound) if the O(Phi^2) pass-rate holds.
"""
import sys
import time
from math import gcd, isqrt
from lib.phi import phi_pairs, in_phi, sum_in_phi_prefilter

# aliases kept local for speed
_gcd = gcd


def count_membership_tests_estimator(M):
    """Return |Phi(M)| for the reporting line."""
    return len(phi_pairs(M))


def search(M, budget):
    t0 = time.time()
    Phi = phi_pairs(M)
    # sort by value (reduced positive fractions: smaller num/den = smaller value)
    pairs = sorted(Phi, key=lambda nd: nd[0] * 1.0 / nd[1])
    P = len(pairs)
    triples = []
    n_valid = 0          # pairs with 0 < q1+q2 < 1
    n_survive_pre = 0    # survived the (necessary) two-sided prefilter
    n_exact = 0          # reached the authoritative in_phi test
    for i in range(P):
        A1, B1 = pairs[i]
        for j in range(i):
            A2, B2 = pairs[j]
            num = A1 * B2 + A2 * B1
            if num >= B1 * B2:      # sum >= 1
                continue
            n_valid += 1
            den = B1 * B2
            g = _gcd(num, den)
            A3, B3 = num // g, den // g
            # necessary prefilter: both 1±(A3/B3) rational squares
            dm = B3 - A3
            dp = B3 + A3
            if dm <= 0 or dp <= 0:
                continue
            if not (_issq(dm) and _issq(B3) and _issq(dp)):
                continue
            n_survive_pre += 1
            n_exact += 1
            if in_phi(A3, B3):
                triples.append(((A1, B1), (A2, B2), (A3, B3)))
            if time.time() - t0 > budget:
                print(f"[M={M}] budget {budget:.0f}s exhausted mid-scan: "
                      f"i={i}/{P}; no triple so far")
                return None, (M, P, n_valid, n_survive_pre, n_exact, time.time() - t0)
    print(f"[M={M}] |Phi|={P}, pairs with sum<1: {n_valid}, "
          f"survived prefilter: {n_survive_pre}, exact tests: {n_exact}, "
          f"triples: {len(triples)}, {time.time()-t0:.0f}s")
    return triples, (M, P, n_valid, n_survive_pre, n_exact, time.time() - t0)


def _issq(x):
    r = isqrt(x)
    return r * r == x


def main():
    args = sys.argv[1:]
    Ms = []
    budget = 600.0
    for a in args:
        if a.startswith("--timeout"):
            budget = float(a.split("=")[1]) if "=" in a else float(args[args.index(a) + 1])
        elif a.isdigit():
            Ms.append(int(a))
    if not Ms:
        Ms = [500, 700, 1000]
    print(f"Searching additive triples in Phi over M in {Ms}, "
          f"budget {budget}s per M")
    overall = 0
    for M in Ms:
        triples, stat = search(M, budget)
        if triples is None and stat is None:
            continue
        Mx, P, nv, npre, nexact, dt = stat
        if triples:
            print(f"  *** TRIPLE FOUND at M={Mx}: "
                  f"{triples[0][0][0]}/{triples[0][0][1]} + "
                  f"{triples[0][1][0]}/{triples[0][1][1]} = "
                  f"{triples[0][2][0]}/{triples[0][2][1]}")
            overall += 1
        else:
            print(f"  => NO additive triple for any pair from primitive "
                  f"m,n <= {Mx} (pairs sum<1: {nv}; survived prefilter "
                  f"{npre}; exact tests {nexact}; {dt:.0f}s)")
    print("\nSUMMARY: triples found overall =", overall)


if __name__ == "__main__":
    main()
