#!/usr/bin/env python3
"""Attack R-dyadic-periodicity-dichotomy at its named falsifier.

Prediction (Directive 57): for eventually-periodic halved-gap bit string h with
MINIMAL period P,  nu2(q_n) = O(1)  when P is a power of 2, and  nu2 ~ c*n
when P has an odd factor.  The named falsifier: if a period-3 or period-5
family gives nu2 = O(1), the dyadic story is wrong.

Faithful construction.  h[j] = (gap_{j+1}/2) mod 2 = [gap_{j+1} == 2 mod 4].
So for a periodic h we build gaps as literals: h_j = 1 -> gap = 2 (==2 mod 4),
h_j = 0 -> gap = 4 (==0 mod 4).  Sequence A_0 = (2,3,x_1,...) with
x_1 - 3 = 2 (first gap 2), then gaps follow the periodic h.  Then we compute
the exact integer right-diagonal incrementally (lib.rightdiag) and nu2(n) =
count of 2s in the maximal {0,2} suffix of delta(q_n) via cycle_and_nu2.

This is the same quantity SC-supply-nu2-linear / GN-supply-nu2-density talk
about.  Small, exact, O(N^2) diffs total.
"""
import sys
from lib.rightdiag import incremental_diagonals, cycle_and_nu2


def build_sequence(h_period, P, Nmax):
    """Sequence q with q[0]=2,q[1]=3, first gap 2, then gaps following
    periodic bits h of minimal period P.  Return list with >= Nmax+2 entries."""
    seq = [2, 3]
    x = 3
    # first gap = 2 (h_1 irrelevant to the first gap, which is fixed)
    x += 2
    seq.append(x)
    j = 0
    while len(seq) < Nmax + 2:
        g = 2 if h_period[j % P] == 1 else 4
        x += g
        seq.append(x)
        j += 1
    return seq


def nu2_series(seq, n_lo, n_hi):
    out = []
    for D in incremental_diagonals(seq):
        n = len(D) - 1  # delta(q_n) has length n+1
        if n < n_lo:
            continue
        tau, nu2 = cycle_and_nu2(D)
        out.append((n, nu2))
        if n >= n_hi:
            break
    return out


def report(name, h_period, P, n_lo, n_hi):
    seq = build_sequence(h_period, P, n_hi)
    series = nu2_series(seq, n_lo, n_hi)
    # group at sampled n
    print(f"--- {name}: minimal period P={P}, h={h_period[:P]}")
    for n, nu2 in series:
        if n in (200, 500, 1000, 2000, n_hi) or n % 500 == 0:
            print(f"   n={n:6d}  nu2={nu2:6d}  nu2/n={nu2/max(n,1):.4f}")
    mx = max((nu2 for _, nu2 in series), default=0)
    print(f"   max nu2 over n in [{n_lo},{n_hi}] = {mx}")
    return mx


def main():
    n_lo, n_hi = 200, 2000
    res = {}
    # power-of-2 periods (predicted collapse -> bounded nu2)
    for P, name in [(1, "P=1 all-ones"), (2, "P=2 10"), (4, "P=4 1000"),
                    (8, "P=8 10000000")]:
        if name == "P=1 all-ones":
            h = [1]
        elif name == "P=2 10":
            h = [1, 0]
        elif name == "P=4 1000":
            h = [1, 0, 0, 0]
        else:
            h = [1] + [0] * 7
        res[name] = report(name, h, P, n_lo, n_hi)
    print()
    # odd-factor periods (predicted growth -> nu2 ~ c*n)
    for P, name in [(3, "P=3 100"), (5, "P=5 10000"), (6, "P=6 100000"),
                    (7, "P=7 1000000")]:
        h = [1] + [0] * (P - 1)
        res[name] = report(name, h, P, n_lo, n_hi)
    print()
    # verdict
    pow2 = [res[k] for k in res if k.startswith("P=") and k[2] in "1248"]
    # crude: identify odd-factor growth vs power-of-2 collapse
    print("max nu2 for dyadic (P in {1,2,4,8}):", pow2)
    for name in ["P=3 100", "P=5 10000", "P=6 100000", "P=7 1000000"]:
        print(f"  {name} max nu2 = {res[name]}")


if __name__ == "__main__":
    main()
