#!/usr/bin/env python3
"""Exact brute-force verification of the iid-fair-model claim for SUPPLY.

Claim: for an iid fair binary string h (each bit 0/1, prob 1/2, independent),
each fold cell

    T(n,d) = XOR over bitwise submasks s of d of h[n-1-s]

is a XOR of 2^{popcount(d)} >= 2 independent fair bits, hence itself fair.
Therefore E[nu2(n)] = #{d in [2,n-1]} / 2 = (n-2)/2 and the empirical
distribution of nu2(n) over all 2^n strings is symmetric about (n-2)/2.

This program verifies the claim EXACTLY by enumeration: for each n in 2..12 it
lists all 2^n binary strings, computes nu2(n) = #{d in [2,n-1] : T(n,d)=1}
per string (using the literal submask-XOR definition via lib.supply_fold.t_direct),
forms the exact empirical distribution, and checks
  (1) the empirical mean equals (n-2)/2 exactly (exact fractions, not floats);
  (2) the distribution is symmetric about (n-2)/2.

This is a forbidden-size-independent brute-force oracle check kept small
(2^12 = 4096 strings max) purely to validate the model claim. Exact integer
arithmetic throughout.

Output: code/out/fair_model_exact.txt
"""

import sys
import os
from collections import Counter

from lib.supply_fold import t_direct

from fractions import Fraction


def verify(n):
    """Return dict of results for a single n (exact)."""
    nd = n - 2                      # number of d values in [2, n-1]
    expected = Fraction(nd, 2)      # (n-2)/2 exactly

    counts = Counter()              # nu2 value -> number of strings giving it
    total_nu2 = 0

    for mask in range(1 << n):
        # h[j] = bit j of mask (j = 0..n-1). h indexed 0..n-1 as t_direct needs.
        h = [1 if (mask >> j) & 1 else 0 for j in range(n)]
        nu2 = 0
        for d in range(2, n):
            if t_direct(n, d, h) == 1:
                nu2 += 1
        counts[nu2] += 1
        total_nu2 += nu2

    num_strings = 1 << n
    mean = Fraction(total_nu2, num_strings)

    mean_ok = (mean == expected)

    # symmetry: count[x] == count[nd - x] for all x
    sym_ok = True
    for x, c in counts.items():
        if counts.get(nd - x, 0) != c:
            sym_ok = False
            break

    return dict(n=n, nd=nd, expected=str(expected), mean=str(mean),
                mean_ok=mean_ok, sym_ok=sym_ok, num_strings=num_strings,
                distribution=sorted(counts.items()))


def main():
    results = [verify(n) for n in range(2, 13)]

    lines = []
    lines.append("Exact brute-force verification of the iid-fair-model claim for SUPPLY")
    lines.append("T(n,d) = XOR over bitwise submasks s of d of h[n-1-s],  nu2(n) = #{d in [2,n-1] : T(n,d)=1}")
    lines.append("")
    lines.append(f"{'n':>3} {'#d':>3} {'2^n strings':>11} {'mean(nu2)':>12} {'(n-2)/2':>9} {'mean==exp':>9} {'symmetric':>9}")
    lines.append("-" * 75)
    all_ok = True
    for r in results:
        lines.append(f"{r['n']:>3} {r['nd']:>3} {r['num_strings']:>11} {r['mean']:>12} {r['expected']:>9} "
                     f"{str(r['mean_ok']):>9} {str(r['sym_ok']):>9}")
        if not (r['mean_ok'] and r['sym_ok']):
            all_ok = False

    lines.append("-" * 75)
    lines.append("")

    # exact equality table and distribution tables
    lines.append("Exact equality table (empirical mean vs (n-2)/2):")
    for r in results:
        lines.append(f"  n={r['n']:>2}: mean = {r['mean']}  expected = {r['expected']}  "
                     f"equal={'YES' if r['mean_ok'] else 'NO'}")
    lines.append("")
    lines.append("Empirical distributions (nu2 value -> #strings, showing symmetry about (n-2)/2):")
    for r in results:
        lines.append(f"  n={r['n']:>2} (nd={r['nd']}, center={r['expected']}):")
        lines.append(f"      {r['distribution']}")

    lines.append("")
    lines.append("OVERALL: " + ("ALL CHECKS PASS (mean exact and distribution symmetric for every n)."
                                if all_ok else "FAILURE — some n disagrees."))

    text = "\n".join(lines) + "\n"
    outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "out")
    outdir = os.path.normpath(outdir)
    os.makedirs(outdir, exist_ok=True)
    outpath = os.path.join(outdir, "fair_model_exact.txt")
    with open(outpath, "w") as f:
        f.write(text)

    print(text)
    return all_ok


if __name__ == "__main__":
    ok = main()
    sys.exit(0 if ok else 1)
