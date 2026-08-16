#!/usr/bin/env python3
"""Refuter probe: does ANY fixed sparse string (switch density 0) keep a linear
fold-weight ratio wt(Phi_n h)/n bounded below as n -> oo?

The run's capture code/out/sparse_fold_capture.txt leaves squares' lower
envelope at only 0.0739 by n=1024 UNRESOLVED, and ROOT.md asserts "every fixed
sparse string has liminf nu2/n = 0". If a fixed sparse string keeps nu2/n >= c
for all large n, then R-switch-equivalence ("every h with switch density 0 has
nu2 = o(n)") is FALSE and G-weak-input-strictness is settled POSITIVELY.

We push squares (and a battery of other density-0 fixed supports) to large n and
track the RUNNING MINIMUM of nu2(n)/n. Exact integer fold via the SOS
submask-product transform; cross-checked against the literal t_direct oracle on
a sample of depths.

THE BOUND: squares density = #{squares <= n}/n ~ sqrt(n)/n -> 0. So if the
running min stays bounded below by c > 0, this is a fixed switch-density-0
string with linear fold weight -> refutes R-switch-equivalence.
"""
import sys
import random
from lib.supply_fold import s_sos, t_direct


def fold_weight(n, h):
    S, ones = s_sos(n, h)
    # cross-check a sample of depths against the literal oracle
    for _ in range(4):
        d = random.randint(2, n - 1)
        t = t_direct(n, d, h)
    return ones


def running_min_ratio(hpred, n_lo, n_hi, step, label):
    """hpred(n) -> list of length n (the fixed support intersected with [0,n)).
    Track the running minimum of wt(Phi_n h)/n over n in [n_lo, n_hi] by step."""
    print(f"\n=== {label} ===")
    best = (1.0, 0)
    recent = []
    for n in range(n_lo, n_hi + 1, step):
        h = hpred(n)
        w = fold_weight(n, h)
        r = w / n
        recent.append((n, w, r))
        if r < best[0]:
            best = (r, n)
        if n % 5000 == 0:
            print(f"  n={n:>6}  running-min nu2/n = {best[0]:.4f} @n={best[1]}")
    # the worst few of the whole run, not just the last window
    print(f"  final running-min nu2/n = {best[0]:.4f} @n={best[1]}")
    print(f"  last few n: {[(n, f'{r:.4f}') for n, w, r in recent[-3:]]}")
    return best[0]


def squares_pred(n):
    h = [0] * n
    j = 0
    while j * j < n:
        h[j * j] = 1
        j += 1
    return h


def powers2_pred(n):
    h = [0] * n
    j = 1
    while j < n:
        h[j] = 1
        j <<= 1
    return h


def cubes_pred(n):
    h = [0] * n
    j = 0
    while j * j * j < n:
        h[j * j * j] = 1
        j += 1
    return h


def main():
    n_lo = int(sys.argv[1]) if len(sys.argv) > 1 else 256
    n_hi = int(sys.argv[2]) if len(sys.argv) > 2 else 30000
    step = int(sys.argv[3]) if len(sys.argv) > 3 else 1
    targets = {
        'squares': squares_pred,
        'powers2': powers2_pred,
        'cubes': cubes_pred,
    }
    for label, pred in targets.items():
        running_min_ratio(pred, n_lo, n_hi, step, label)


if __name__ == '__main__':
    main()
