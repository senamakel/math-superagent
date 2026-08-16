#!/usr/bin/env python3
"""Refuter: attack the open gaps. Focus on the most-likely-false statements.

Current target: G-run-telescope C2 telescoping identity is claimed to hold for
any {0,1} sequence h with boundary r (h[j] = [r_{j+1} != r_j]). But the run
telescoping claims:

    XOR_{o in R} h[pos+o] == [ r_{pos+u} != r_{pos+v+1} ]

for a run R=[u,v]. This is XOR over consecutive positions of h, which equals
r-END toggling: XOR of h over [pos+u, pos+v] = (r[pos+v+1] != r[pos+u]). Let me
verify independently whether the down-set fold really telescopes run by run and
whether the run-decomposition converges issue (number of runs vs g) is correct.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))
from lib.submasks import and_subsets, downset_runs, trailing_ones, boundary_from_h


def fold_xor(h, d, pos):
    acc = 0
    for o in and_subsets(d):
        acc ^= h[pos + o]
    return acc


def main():
    import random
    random.seed(7)
    bad = 0
    for d in range(0, 300):
        brute = sorted(and_subsets(d))
        runs = downset_runs(d)
        flat = []
        for (u, v) in runs:
            assert v >= u and v - u + 1 == (1 << trailing_ones(d))
            flat.extend(range(u, v + 1))
        if sorted(flat) != brute:
            bad += 1
            print("RUN-DECOMP MISMATCH", d, brute, runs)
    print("run decomposition: checked d=0..300, mismatches =", bad)

    for L in (50, 200, 1000):
        bad = 0
        for _ in range(20):
            h = [random.randint(0, 1) for _ in range(L)]
            r = boundary_from_h(h)
            for d in range(0, 60):
                for pos in range(0, 40):
                    runs = downset_runs(d)
                    for (u, v) in runs:
                        acc = 0
                        for o in range(u, v + 1):
                            acc ^= h[pos + o]
                        tel = 1 if r[pos + u] != r[pos + v + 1] else 0
                        if acc != tel:
                            bad += 1
                            if bad < 5:
                                print("TELESCOPE MISMATCH", d, pos, (u, v), acc, tel)
        print(f"telescoping: L={L}, mismatches={bad}")


if __name__ == "__main__":
    main()
