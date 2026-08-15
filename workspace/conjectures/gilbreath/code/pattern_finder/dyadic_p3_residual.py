#!/usr/bin/env python3
"""PATTERN-FINDER: exact residual structure of nu2(n) for the P=3 tail-1 word.

Model (locked to the run's dyadic oracle): q_1=2, q_2=3, gap = 2 if bit else 4,
bits periodic word [0,0,1] (period 3).  nu2(n) = #2s in the maximal {0,2}
suffix of the right diagonal delta(q_n) (body convention, terminal excluded,
lib.rightdiag.cycle_and_nu2).

Prior run (code/out/dyadic_oddfactor_density_exact.captured.txt) measured
nu2(n) ~ (2/3)n with O(1) residual at n = 1000..24000.  This program recomputes
the FULL exact sequence nu2(n) for n = 2..ceil and reports:
  - the exact sequence (to identify residual periodicity / closed form)
  - residual r(n) = nu2(n) - (2/3)n  (as exact fractions)
  - propose closed forms and count exact matches:
       A: nu2 = floor(2n/3)
       B: nu2 = floor(2n/3) - [n%3 == 0]   (subtract 1 at multiples of 3)
       C: nu2 = floor((2n-2)/3)
  - OEIS-friendly first terms.

Exact integer arithmetic; O(n^2) diffs, O(n) memory.
"""
import sys
sys.path.insert(0, '/workspace/code')
from lib.rightdiag import incremental_diagonals, cycle_and_nu2


def build_seq(word, n_terms):
    q = [2, 3]
    per = len(word)
    while len(q) < n_terms:
        bit = word[(len(q) - 2) % per]
        q.append(q[-1] + (2 if bit else 4))
    return q[:n_terms]


def nu2_seq(word, nmax):
    """nu2(n) for n=2..nmax, exact, via one incremental diagonal pass."""
    q = build_seq(word, nmax + 1)
    out = {}
    for k, dd in enumerate(incremental_diagonals(q)):
        if k >= 2:
            out[k] = cycle_and_nu2(dd)[1]
    return out


def main():
    word = [0, 0, 1]
    nmax = 120
    vals = nu2_seq(word, nmax)
    seq = [vals[n] for n in range(2, nmax + 1)]
    print("P=3 word 001: exact nu2(n), n=2..", nmax)
    print("first 60 terms (n=2..61):")
    print(seq[:60])
    print()

    # residual vs (2/3)n as exact fractions
    from fractions import Fraction
    print("residual r(n) = nu2(n) - 2n/3 (exact fraction):")
    for n in range(2, 40):
        r = Fraction(vals[n]) - Fraction(2 * n, 3)
        print(f"  n={n:3d} nu2={vals[n]:3d}  r={r}")
    print()

    # candidate closed forms
    def cA(n): return (2 * n) // 3
    def cB(n): return (2 * n) // 3 - (1 if n % 3 == 0 else 0)
    def cC(n): return (2 * n - 2) // 3
    okA = okB = okC = 0
    badA = badB = badC = []
    for n in range(2, nmax + 1):
        v = vals[n]
        if cA(n) == v: okA += 1
        else: badA.append((n, v, cA(n)))
        if cB(n) == v: okB += 1
        else: badB.append((n, v, cB(n)))
        if cC(n) == v: okC += 1
        else: badC.append((n, v, cC(n)))
    print(f"closed-form matches over n=2..{nmax}:")
    print(f"  A floor(2n/3)            : {okA}/{nmax-1}  first bad {badA[:3]}")
    print(f"  B floor(2n/3)-[3|n]      : {okB}/{nmax-1}  first bad {badB[:3]}")
    print(f"  C floor((2n-2)/3)        : {okC}/{nmax-1}  first bad {badC[:3]}")
    print()
    print("residue classes of n mod 3:")
    for r in (0, 1, 2):
        sub = [(n, vals[n]) for n in range(2, nmax + 1) if n % 3 == r]
        dn = [vals[n] - vals[n - 3] for n in range(5, nmax + 1) if n % 3 == r]
        print(f"  n%3={r}: n in {[s[0] for s in sub[:10]]}, increments nu2(n)-nu2(n-3): {dn[:12]}")
    print()
    print("first 24 terms for OEIS (n=2..25):", seq[:24])


if __name__ == "__main__":
    main()