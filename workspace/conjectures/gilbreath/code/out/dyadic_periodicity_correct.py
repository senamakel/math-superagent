#!/usr/bin/env python3
"""
CORRECT oracle for the dyadic-periodicity dichotomy (Directives 57/58).

Fixes the two bugs in the earlier scripts:
  1. reproduce_dyadic_periodicity.py: build_seq indexed h_pattern[len(q)-2]
     WITHOUT wrapping modulo the period -> IndexError.  Here we wrap.
  2. dyadic_periodic_check.py: make_input_gaps added a leading gap 1 for the
     2->3 difference AND build_triangle prepended [1], yielding
     A_1 = (1,1,2,4,...) with an ODD second entry -> broken triangle, nu2=0
     everywhere.  Here A_1 = (1, then even gaps), second entry is even.

Construction (Directive 58): 2-then-odds q, q_1=2, q_2=3, and for n>=2
  q_{n+1} = q_n + gap,  gap = 2 if h[n]==1 else 4,
  where h[j] = ( (q_{j+3}-q_{j+2})/2 ) mod 2 is the periodic halved-gap bit
  string with period P.  h[0] governs the gap 3->5.

nu2(q_n) = # of 2s in the maximal {0,2} suffix of the right diagonal
  delta(q_n) = [A_0[n], A_1[n-1], ..., A_n[0]], using the standard
  cycle_and_nu2 convention (body = diag[:-1], maximal {0,2} suffix).
"""
import sys
sys.path.insert(0, '/workspace/code')
from lib.rightdiag import incremental_diagonals, cycle_and_nu2


def build_seq(h_pattern, n_terms):
    """q_1..q_{n_terms}.  Bit h[j] governs gap q_{j+2}->q_{j+3} (j>=0);
    gap = 2 if bit else 4.  q_1=2, q_2=3 always."""
    q = [2, 3]
    period = len(h_pattern)
    while len(q) < n_terms:
        m = len(q)               # we are appending q_{m+1}; gap is q_m->q_{m+1}
        j = m - 2                # bit index for this gap (h[0] = gap 3->5)
        bit = h_pattern[j % period]
        gap = 2 if bit else 4
        q.append(q[-1] + gap)
    return q[:n_terms]


def nu2_for(period_word, n):
    q = build_seq(period_word, n + 1)
    diags = list(incremental_diagonals(q))
    d = diags[n]
    tau, nu2 = cycle_and_nu2(d)
    return nu2


def reproduce_stage1():
    """Directive 58 stage-1 numbers as a falsifiable prediction."""
    tests = [
        ("period 1 h=1",        [1],                 [200, 400, 800, 1200], [1, 1, 1, 1]),
        ("period 2 h=01",       [0, 1],              [200, 400, 800, 1200], [2, 2, 2, 2]),
        ("period 4 h=0001",     [0, 0, 0, 1],        [200, 400, 800, 1200], [2, 2, 2, 2]),
        ("period 8 h=00000001", [0, 0, 0, 0, 0, 0, 0, 1], [200, 400, 800, 1200], [2, 2, 2, 2]),
        ("period 3 h=001",      [0, 0, 1],           [200, 400, 800, 1200], [133, 264, 533, 798]),
        ("period 5 h=00001",    [0, 0, 0, 0, 1],     [200, 400, 800, 1200], [104, 210, 424, 638]),
        ("period 6 h=000001",   [0, 0, 0, 0, 0, 1],  [200, 400, 800, 1200], [134, 264, 534, 796]),
        ("period 7 h=0000001",  [0, 0, 0, 0, 0, 0, 1], [200, 400, 800, 1200], [112, 112, 685, 684]),
    ]
    all_ok = True
    for name, word, ns, expected in tests:
        got = [nu2_for(word, n) for n in ns]
        match = (got == expected)
        all_ok &= match
        print(f"{name}: got {got}  expected {expected}  match={match}")
    print("ALL MATCH:", all_ok)
    return all_ok


def extend_periods(ns=(200, 500, 1000, 2000, 4000)):
    """Extend beyond stage 1: periods 9..16 and non-constant words of the
    same period.  The claim is about the PERIOD, not the specific word, so we
    test both a 'tail-1' word and a generic word for each period."""
    print("\n=== Extension: periods 9..16, two words each ===")
    print(f"{'P':>3} {'word':>10} " + "".join(f"n={n:<8}" for n in ns))
    for P in range(9, 17):
        # word1 = [0,...,0,1] (one 1 at the end)
        w1 = [0] * (P - 1) + [1]
        # word2 = a generic near-balanced word, e.g. 1 at positions with index%2 etc
        w2 = [(1 if (i % 2 == 0) else 0) for i in range(P)]
        for wtag, w in (("tail1", w1), ("alt", w2)):
            vals = [nu2_for(w, n) for n in ns]
            print(f"{P:>3} {wtag:>10} " + "".join(f"{v:<8}" for v in vals))
    print("\n=== Reference: periods 1..8 (both words), for contrast ===")
    for P in range(1, 9):
        w1 = [0] * (P - 1) + [1]
        w2 = [(1 if (i % 2 == 0) else 0) for i in range(P)]
        for wtag, w in (("tail1", w1), ("alt", w2)):
            vals = [nu2_for(w, n) for n in ns]
            print(f"{P:>3} {wtag:>10} " + "".join(f"{v:<8}" for v in vals))


if __name__ == "__main__":
    ok = reproduce_stage1()
    print("\nstage-1 reproduction:", "GOOD" if ok else "BAD")
    extend_periods()
