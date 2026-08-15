#!/usr/bin/env python3
"""Probe Mersenne-affine mechanism: print the {0,2} suffix bit pattern of the
right diagonal delta(q_n) at successive n for a Mersenne period (P=7) and a
non-Mersenne period (P=9). Look for whether the suffix pattern is itself
shift-periodic in n."""
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
    while i > 2 and body[i-1] in (0, 2):
        i -= 1
    return [x // 2 for x in body[i:]], len(body) - i


def main():
    for P in (7, 9):
        print("=" * 40, "P =", P)
        N = P * 5 + 20
        q = build_seq([0]*(P-1)+[1], N + 1)
        for k, dd in enumerate(incremental_diagonals(q)):
            if k < P * 2:
                continue
            suff, L = suffix(dd)
            print("n=%3d  L=%3d  suffix=%s" % (k, L, ''.join(map(str, suff))))


if __name__ == "__main__":
    main()
