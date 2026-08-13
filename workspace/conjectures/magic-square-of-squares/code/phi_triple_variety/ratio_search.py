#!/usr/bin/env python3
"""code/phi_triple_variety/ratio_search.py — (A) ratio-form fast no-triple search.

Search for an additive triple q1, q2, q1+q2 with q1>q2>0 all in Phi, using
the ratio parametrisation f(m,n)=f(t=n/m) collapsed to DISTINCT values and
the exact membership machinery from code/lib/phi.py.

Cost model (exact): |Phi(M)| ~ 0.2 M^2 distinct values from m <= M, so the
full q1>q2 pair loop is ~0.5|Phi|^2 ~ 0.02 M^4 pairs.  Every pair first
passes a NECESSARY prefilter (0 < sum < 1 AND both 1±sum RATIONAL SQUARES,
reduced correctly via gcd — necessary for sum in Phi, so it never
false-negatives a candidate); only survivors hit the authoritative uncapped
in_phi test.  The prefilter is ~all-selective, so expensive tests are few;
the cost is dominated by the O(Phi^2) cheap pair enumeration.

Usage: python3 code/phi_triple_variety/ratio_search.py [M ...] [--timeout S]
"""
import sys
import time
from math import gcd, isqrt
from lib.phi import phi_pairs, in_phi, rational_square


def _sum_in_phi_necessary(A1, B1, A2, B2):
    """Correct NECESSARY-condition test that A1/B1+A2/B2 might be in Phi.
    Returns (A3,B3) reduced sum and whether both 1±(A3/B3) are rational
    squares (each then confirmed by the authoritative in_phi)."""
    num = A1 * B2 + A2 * B1
    den = B1 * B2
    g = gcd(num, den)
    A3, B3 = num // g, den // g
    if A3 <= 0 or A3 >= B3:
        return (A3, B3), False
    dm, dp = B3 - A3, B3 + A3
    g1 = gcd(dm, B3)
    g2 = gcd(dp, B3)
    ok = (rational_square(dm // g1, B3 // g1)
          and rational_square(dp // g2, B3 // g2))
    return (A3, B3), ok


def search(M, budget):
    t0 = time.time()
    Phi = phi_pairs(M)
    pairs = sorted(Phi, key=lambda nd: nd[0] * 1.0 / nd[1])
    P = len(pairs)
    triples = []
    n_valid = 0
    n_survive_pre = 0
    n_exact = 0
    for i in range(P):
        A1, B1 = pairs[i]
        for j in range(i):
            A2, B2 = pairs[j]
            # quick reject on sum >= 1 without full gcd:
            if A1 * B2 + A2 * B1 >= B1 * B2:
                continue
            (A3, B3), survive = _sum_in_phi_necessary(A1, B1, A2, B2)
            n_valid += 1
            if not survive:
                continue
            n_survive_pre += 1
            n_exact += 1
            if in_phi(A3, B3):
                triples.append(((A1, B1), (A2, B2), (A3, B3)))
            if time.time() - t0 > budget:
                print(f"[M={M}] budget {budget:.0f}s exhausted mid-scan "
                      f"i={i}/{P}; none so far")
                return None, (M, P, n_valid, n_survive_pre, n_exact,
                              time.time() - t0)
    print(f"[M={M}] |Phi|={P}, pairs sum<1: {n_valid}, survived "
          f"necessary-prefilter: {n_survive_pre}, exact tests: {n_exact}, "
          f"triples: {len(triples)}, {time.time()-t0:.0f}s")
    return triples, (M, P, n_valid, n_survive_pre, n_exact, time.time() - t0)


def main():
    args = sys.argv[1:]
    Ms, budget = [], 590.0
    i = 0
    while i < len(args):
        a = args[i]
        if a.startswith("--timeout"):
            budget = float(a.split("=")[1]) if "=" in a else float(args[i + 1])
            i += 2
        elif a.isdigit():
            Ms.append(int(a)); i += 1
        else:
            i += 1
    if not Ms:
        Ms = [600]
    print(f"Searching additive triples in Phi over M in {Ms}, "
          f"budget {budget:.0f}s per M\n", flush=True)
    total = 0
    for M in Ms:
        triples, stat = search(M, budget)
        if triples is None and stat is None:
            continue
        if triples:
            (A1, B1), (A2, B2), (A3, B3) = triples[0]
            print(f"  *** TRIPLE at M={M}: {A1}/{B1}+{A2}/{B2}={A3}/{B3}")
            total += 1
        else:
            Mx, P, nv, npre, nex, dt = stat
            print(f"  => NO additive triple for primitive m,n <= {Mx} "
                  f"pairs-sum<1: {nv} survived-pre: {npre} exact: {nex} "
                  f"({dt:.0f}s)", flush=True)
    print(f"\nSUMMARY: triples found overall = {total}")


if __name__ == "__main__":
    main()
