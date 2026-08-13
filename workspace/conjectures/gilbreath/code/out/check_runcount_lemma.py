#!/usr/bin/env python3
"""Check the elementary lemma behind the total-variation-oscillation-potential
approach: r(T(x)) <= r(x), where r = number of maximal constant runs and
T(x)_i = |x_i - x_{i+1}| (the absolute-difference map on a finite string,
non-cyclic). Also check the second candidate: t(T(x)) <= t(x) where t =
number of strict turning points.

Small exhaustive check only (values in a small range, short lengths) — this is
a counterexample hunt for a lemma the approach would rest on, not a search for
a solution. If a counterexample exists it kills the lemma as stated.

Run: python3 check_runcount_lemma.py
"""
import itertools
import sys


def runs(seq):
    """Number of maximal constant runs; empty sequence has 0."""
    if not seq:
        return 0
    n = 1
    for i in range(1, len(seq)):
        if seq[i] != seq[i - 1]:
            n += 1
    return n


def turning_points(seq):
    """Number of strict local extrema (interior positions where the sequence
    changes direction)."""
    if len(seq) < 3:
        return 0
    t = 0
    for i in range(1, len(seq) - 1):
        if (seq[i] - seq[i - 1]) * (seq[i + 1] - seq[i]) < 0:
            t += 1
    return t


def T(seq):
    return [abs(seq[i] - seq[i + 1]) for i in range(len(seq) - 1)]


def main():
    max_len = 8
    max_val = 6
    worst_r = (0, None)
    worst_t = (0, None)
    counterexample_r = None
    counterexample_t = None
    total = 0
    for n in range(1, max_len + 1):
        for seq in itertools.product(range(max_val + 1), repeat=n):
            total += 1
            tseq = T(seq)
            r_before, r_after = runs(seq), runs(tseq)
            if r_after > r_before:
                counterexample_r = (seq, r_before, r_after, tseq)
            if r_after - r_before > worst_r[0]:
                worst_r = (r_after - r_before, seq)
            t_before, t_after = turning_points(seq), turning_points(tseq)
            if t_after > t_before:
                counterexample_t = (seq, t_before, t_after, tseq)
            if t_after - t_before > worst_t[0]:
                worst_t = (t_after - t_before, seq)
    print(f"checked {total} sequences (len 1..{max_len}, values 0..{max_val})")
    print(f"r(T(x)) <= r(x) counterexample: {counterexample_r}")
    print(f"worst run-count increase: {worst_r}")
    print(f"t(T(x)) <= t(x) counterexample: {counterexample_t}")
    print(f"worst turning-point increase: {worst_t}")
    # Also verify r(T) can be much SMALLER than r(x) (the approach needs strict
    # decrease in non-rigid cases) — print best-case drops for constant-T trivia.
    if counterexample_r is None:
        print("LEMMA r(T(x)) <= r(x): NO COUNTEREXAMPLE FOUND in range")
    else:
        print("LEMMA r(T(x)) <= r(x): REFUTED (see above)")
        sys.exit(1)
    if counterexample_t is None:
        print("LEMMA t(T(x)) <= t(x): NO COUNTEREXAMPLE FOUND in range")
    else:
        print("LEMMA t(T(x)) <= t(x): REFUTED (see above)")
        sys.exit(1)


if __name__ == "__main__":
    main()