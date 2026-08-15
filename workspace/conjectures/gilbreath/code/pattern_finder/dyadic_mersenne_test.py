#!/usr/bin/env python3
"""
PATTERN-FINDER attack on the conjecture:

    nu2(n) is per-residue affine (mod P) for the tail-1 word [0]*(P-1)+[1]
    iff P is a Mersenne number 2^k - 1.

Model: q_1=2, q_2=3, gap = 2 if bit else 4, bits tail-1 word.
nu2(n) = #2s in maximal {0,2} suffix of right diagonal delta(q_n)
(lib.rightdiag.cycle_and_nu2, body convention).

The affine survey (dyadic_affine_survey.py) found affine at {3,7,15,31} and
non-affine at {5,9,11,13,17,21,23,25,27,33,35,39,45} over n in [300,1200].
This extends to larger Mersenne periods and a wider non-Mersenne spread, over a
WIDER window, to attack (confirm or refute) the Mersenne-only classification.

Cost: incremental-diagonal recurrence is O(N^2) diffs / O(N) memory for one P.
N=4000 -> 16M diffs, a few seconds per P.
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


def per_residue_affine(vals, P, nmin, nmax):
    cs = []
    ok = True
    for r in range(P):
        diffs = {vals[n + P] - vals[n] for n in range(nmin, nmax - P + 1)
                 if n % P == r}
        if len(diffs) != 1:
            ok = False
            cs.append(None)
        else:
            cs.append(diffs.pop())
    return ok, cs


def is_mersenne(P):
    k = P + 1
    return k > 0 and (k & (k - 1)) == 0


def main():
    N = 4000
    nmin = 500
    # Mersenne positive candidates (2^k-1), k>=2, extending past 31
    mers = [63, 127, 255]
    # wide non-Mersenne odd spread, skipping those survey already cleared
    nonmers = [19, 29, 37, 41, 43, 47, 49, 51, 53, 57, 59, 61, 65, 69,
               71, 73, 75, 81, 85, 87, 89, 91, 95, 97, 99, 111, 119,
               123, 125, 129, 131, 133, 135, 137, 139, 141, 143]
    Ps = mers + nonmers
    print("Mersenne classification attack (tail-1 word), n in [%d,%d]" % (nmin, N))
    print("=" * 80)
    mismatches = 0
    for P in Ps:
        word = [0] * (P - 1) + [1]
        vals = nu2_seq(word, N)
        affine, cs = per_residue_affine(vals, P, nmin, N)
        mers = is_mersenne(P)
        flag = ""
        if affine != mers:
            flag = "  <-- CONTRADICTS MERSENNE-ONLY"
            mismatches += 1
        if affine:
            print("P=%3d Mersenne=%-3s AFFINE  min c=%d" % (P, mers, min(cs)), flag)
        else:
            print("P=%3d Mersenne=%-3s not affine" % (P, mers), flag)
    print("=" * 80)
    print("contradictions to Mersenne-only: %d" % mismatches)


if __name__ == "__main__":
    main()
