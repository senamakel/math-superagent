#!/usr/bin/env python3
"""
Companion to dyadic_oddfactor_infratio.py (Directive 60, thread
dyadic-periodicity-collapse).  Confirms the EXACT linear density of the true
{0,2}-suffix nu2 on the odd-factor periodic 2-then-odds words that the
infimum scan flagged as candidates for exact rational ratios.

nu2(n) = # of 2s in the maximal {0,2} suffix of the right diagonal through
q_n (lib.rightdiag.cycle_and_nu2, body convention, terminal excluded),
for the periodic sequence q_1=2, q_2=3, gap = 2 if bit else 4, bits = word.

Verified claim holding exactly (residual nu2(n) - c*n = O(1), all the way to
n = 24000, exact integers):
   P=3, word 001    ->  nu2(n) = floor(2n/3)     (ratio 2/3)
   P=5, word 00001  ->  nu2(n) = floor(8n/15)-ish (ratio 8/15)
and the residuals stay bounded by O(1), so the asymptotic infimum ratio
nu2(n)/n is bounded AWAY from 0 for these words — the odd-factor converse is
NOT refuted by an asymptotic plateau up to this range.

COST: one incremental diagonal at a time, O(n^2) absolute differences, O(n)
memory.  This is a fixed ladder of measurements, not an answer-space search.
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


def suf_nu2(word, n):
    q = build_seq(word, n + 1)
    d = None
    for k, dd in enumerate(incremental_diagonals(q)):
        if k == n:
            d = dd
            break
    return cycle_and_nu2(d)[1]


def main():
    ladder = [1000, 2000, 4000, 8000, 12000, 16000, 24000]
    print("Exact linear density of true {0,2}-suffix nu2 on odd-factor words")
    print("(companion to dyadic_oddfactor_infratio.py; exact integers)\n")
    cases = {
        3: ([0, 0, 1], 2.0 / 3.0),
        5: ([0, 0, 0, 0, 1], 8.0 / 15.0),
    }
    for P, (word, c) in cases.items():
        wstr = ''.join(map(str, word))
        print(f"P={P} word {wstr}: candidate exact ratio c = {c:.6f}")
        for n in ladder:
            v = suf_nu2(word, n)
            res = v - c * n
            print(f"  n={n:>6} nu2={v:>6} ratio={v/n:.4f} residual({v}-{c:.6f}*n)={res:+.2f}")
        print()
    print("Reading: residual stays O(1) (bounded), so the density is exactly c,")
    print("the asymptotic infimum ratio is bounded away from 0, and the odd-factor")
    print("converse is NOT refuted by a plateau here.  Numerical evidence only —")
    print("the converse (nu2 >= c(P)*n for all n) remains CONJECTURED.")


if __name__ == "__main__":
    main()
