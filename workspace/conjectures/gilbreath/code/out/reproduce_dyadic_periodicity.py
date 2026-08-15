#!/usr/bin/env python3
"""Reproduce Directive 58 stage-1 numbers: nu2 of the right diagonal for
periodic halved-gap bit strings h, gap = 2 if bit else 4.

Setup: 2-then-odds sequence q, q_1=2, q_2=3 (gap 2), and for n>=2
q_{n+1} = q_n + gap where gap = 2 if h[n]==1 else 4  (h is the periodic
halved-gap bit string, one bit per gap).

Right diagonal delta(q_n) via the incremental recurrence; nu2 = #2s in the
maximal {0,2} suffix before the terminal entry (cycle_and_nu2 convention).
"""
import sys
sys.path.insert(0, '/workspace/code')
from lib.rightdiag import incremental_diagonals, cycle_and_nu2


def build_seq(h_pattern, n_terms):
    """q_1..q_{n_terms} from periodic bit pattern h_pattern (list of 0/1),
    one bit per gap; gap = 2 if bit else 4.  q_1=2, q_2=3 always."""
    q = [2, 3]
    period = len(h_pattern)
    while len(q) < n_terms:
        bit = h_pattern[len(q) - 2]  # h[1] is the first gap bit (q_2->q_3)
        gap = 2 if bit else 4
        q.append(q[-1] + gap)
    return q[:n_terms]


def nu2_for(period_word, n):
    q = build_seq(period_word, n + 1)
    diags = list(incremental_diagonals(q))
    d = diags[n]
    tau, nu2 = cycle_and_nu2(d)
    return nu2, d[-1]


def main():
    tests = [
        ("period 1 h=1", [1], [200, 400, 800, 1200], [1, 1, 1, 1]),
        ("period 2 h=01", [0, 1], [200, 400, 800, 1200], [2, 2, 2, 2]),
        ("period 4 h=0001", [0, 0, 0, 1], [200, 400, 800, 1200], [2, 2, 2, 2]),
        ("period 8 h=00000001", [0, 0, 0, 0, 0, 0, 0, 1], [200, 400, 800, 1200],
         [2, 2, 2, 2]),
        ("period 3 h=001", [0, 0, 1], [200, 400, 800, 1200], [133, 264, 533, 798]),
        ("period 5 h=00001", [0, 0, 0, 0, 1], [200, 400, 800, 1200], [104, 210, 424, 638]),
        ("period 6 h=000001", [0, 0, 0, 0, 0, 1], [200, 400, 800, 1200], [134, 264, 534, 796]),
        ("period 7 h=0000001", [0, 0, 0, 0, 0, 0, 1], [200, 400, 800, 1200], [112, 112, 685, 684]),
    ]
    all_ok = True
    for name, word, ns, expected in tests:
        got = [nu2_for(word, n)[0] for n in ns]
        match = got == expected
        all_ok &= match
        print(f"{name}: got {got}  expected {expected}  match={match}")
    print("ALL MATCH:", all_ok)


if __name__ == "__main__":
    main()
