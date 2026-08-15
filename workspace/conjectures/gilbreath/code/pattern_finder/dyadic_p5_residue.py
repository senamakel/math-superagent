#!/usr/bin/env python3
"""PATTERN-FINDER: P=5 word 00001 — residue-class structure of nu2(n).

Ask: is nu2(5k+r) an EXACT affine function of k for each residue r, with all
differences concentrated at periodic (block) positions?  Report per-residue
subsequences and their first differences (a clean slope per residue class =
exact closed form modulo the 5-periodic bit structure).
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
    q = build_seq(word, nmax + 1)
    out = {}
    for k, dd in enumerate(incremental_diagonals(q)):
        if k >= 2:
            out[k] = cycle_and_nu2(dd)[1]
    return out


def main():
    word = [0, 0, 0, 0, 1]
    nmax = 400
    vals = nu2_seq(word, nmax)

    print("P=5 word 00001: nu2(n) per residue class n mod 5, n=2..400")
    print("(each line: n values in that class and nu2 - 8n/15 residual)")
    from fractions import Fraction
    for r in range(5):
        ns = [n for n in range(2, nmax + 1) if n % 5 == r]
        first = ns[:12]
        pair = [(n, vals[n]) for n in first]
        subs = [vals[n] for n in ns]
        diffs = [subs[i] - subs[i - 1] for i in range(1, len(subs))]
        # residual of last few vs 8n/15
        res = [Fraction(vals[n]) - Fraction(8 * n, 15) for n in ns[-6:]]
        print(f"  r={r}: pairs {pair}")
        print(f"       diffs within class: {diffs[:12]}{'...' if len(diffs)>12 else ''}")
        print(f"       residual(nu2-8n/15) at last 6: {[str(x) for x in res]}")
    print()
    print("Overall: does nu2(n) = (8n/15) + O(1)?  == the per-residue diffs bounded?")


if __name__ == "__main__":
    main()