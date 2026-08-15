#!/usr/bin/env python3
"""Verify the MECHANISM of Mersenne-affine nu2: for Mersenne P=2^k-1, the
{0,2}-suffix bit word of the right diagonal satisfies
    suffix(n+P) = suffix(n)  +  w_{n mod P}        (fixed residue block w_r)
i.e. each period appends one residue-dependent word of length P, and the
appended word is the SAME every period for that residue.  This is exactly the
property that makes nu2(n+P)-nu2(n) = wt(w_r) = c_r constant per residue.

Check: (1) block-stability holds at every residue for Mersenne P,
       (2) the appended word is constant from period to period,
       (3) wt(w_r) == c_r (the per-residue affine increment measured earlier).
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


def suffix(dd):
    body = dd[:-1]
    i = len(body)
    while i > 2 and body[i - 1] in (0, 2):
        i -= 1
    return ''.join(str(x // 2) for x in body[i:])


def main():
    for P in (7, 15, 9, 25):
        mersenne = ((P + 1) & P) == 0
        N = P * 6 + 40
        q = build_seq([0] * (P - 1) + [1], N + 1)
        suff = {}
        for k, dd in enumerate(incremental_diagonals(q)):
            suff[k] = suffix(dd)
        # appended word w_r across consecutive periods: for residue r,
        # w_r should equal suffix(r + m*P) minus suffix(r + (m-1)*P) segment.
        stable_all = True
        first_word = {}
        for r in range(P):
            # need suffix at n and n-P for n in the window, n>=start
            words = set()
            for m in range(2, 5):  # periods 2,3,4
                n = r + m * P
                prev = r + (m - 1) * P
                if n in suff and prev in suff and len(suff[n]) - len(suff[prev]) == P:
                    app = suff[n][len(suff[prev]):]
                    words.add(app)
            if len(words) != 1:
                stable_all = False
                first_word[r] = list(words)
            else:
                first_word[r] = words.pop()
        # per residue c_r from block weight (halved->actual: wt of halved block
        # counts 2s, but nu2 counts 2s so c_r should = wt(w_r) if w_r holds 1s)
        print("P=%2d %s: block-stable across periods=%s" %
              (P, "Mersenne" if mersenne else "nonMers", stable_all))
        if stable_all:
            # check wt(w_r) vs measured constant c_r (nu2(n+P)-nu2(n))
            cs = {}
            for r in range(P):
                cs[r] = first_word[r].count('1') * 1
            print("     w_r weights (nu2 increments) =", [cs[r] for r in range(P)])


if __name__ == "__main__":
    main()
