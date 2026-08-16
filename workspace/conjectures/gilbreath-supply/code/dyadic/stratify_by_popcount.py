#!/usr/bin/env python3
"""TASK A — Stratify S(n) = sum_{d=2}^{n-1} (-1)^{T(n,d)} by popcount(d).

This is the falsifier for the dyadic-gap-character route. The route's premise:
if the bulk of S(n) lives in LOW-popcount (few-run) strata, a pointwise
dyadic-gap correlation bound on chi(r) = (-1/q) can be applied, so the route is
live. If EVERY stratum carries full n-weight (uniform), the needed arithmetic
input is as strong as the mean and the route collapses to switch density.

For each n in {400, 1000, 4000} we compute per-depth terms t[d] = (-1)^{T(n,d)}
for d = 2..n-1 via the O(n log n) submask-product SOS transform
(lib.supply_fold.s_terms_sos), then group the partial sums by popcount(d). Use
the primes' real mod-4 residue string r (lib.primes.mod4_string), h = h_from_r
(lib.supply_fold). Cross-check the totals against s_sos and, on small n like
200, against s_direct and s_char_runs (independent routes). A control with a
fixed-seed random h is run to compare the stratum profile (the real-residue
string is NOT random — chi(r_j)=(-1/q_j) has Chebyshev bias, so the profile may
differ).

All arithmetic exact (+-1 ints); the only floats are the printed "share" ratios
and the density. Everything here is a MEASUREMENT of this finite input, not a
proof.
"""

import random
from lib.primes import mod4_string
from lib.supply_fold import (
    h_from_r, s_sos, s_direct, s_char_runs, s_terms_sos, runs_of_downset,
)


def popcount(x):
    return bin(x).count("1")


def stratify(n, terms):
    """Group per-depth terms (index 0 -> d=2) by popcount(d).

    Returns (strata, total). strata[p] = (cnt, partial_sum, abs_partial).
    total = sum of all terms = S(n).
    """
    strata = {}
    total = 0
    for i, t in enumerate(terms):
        d = i + 2
        p = popcount(d)
        cnt, s, _ = strata.get(p, (0, 0, 0))
        strata[p] = (cnt + 1, s + t, abs(s + t))
        total += t
    return strata, total


def max_popcount(n):
    # highest popcount among d in [2, n-1]; for n a power-of-2-ish bound this
    # is popcount of the largest d = n-2 (n-1 has all low bits set).
    return popcount(n - 2)


def run(n, r, label):
    h = h_from_r(r)
    terms = s_terms_sos(n, h)
    S, ones = s_sos(n, h)
    assert sum(terms) == S, (n, sum(terms), S)
    assert terms.count(-1) == ones, (n, terms.count(-1), ones)
    strata, total = stratify(n, terms)

    total_abs = abs(total)
    n_terms = n - 2

    lines = []
    lines.append(f"==== {label}: n={n} ====")
    lines.append(
        f"S(n) = {total}, |S(n)|/n = {total_abs/n:.4f}, "
        f"density(T=1) = {ones/n_terms:.4f}"
    )

    # cumulative share of n-weight (counts) and of |S|-weight by popcount
    lines.append("popcount  cnt    partial_sum   abs_sum  |sum|/n  cum_abs/n")
    cum = 0
    p_max = max(popcount(d) for d in range(2, n))
    for p in range(1, p_max + 1):
        if p not in strata:
            continue
        cnt, s, ab = strata[p]
        cum += ab
        lines.append(
            f"  {p:3d}  {cnt:6d}  {s:+12d}  {ab:10d}  "
            f"{ab/n:.4f}  {cum/n:.4f}"
        )
    lines.append("")
    # dominance summary: is the |S|-weight (sum of |partial|) concentrated in
    # low popcount, or spread like the count (n-weight)?
    p_max = max(popcount(d) for d in range(2, n))
    half = max(1, p_max // 2)
    low_count = sum(c for p, (c, _, _) in strata.items() if p <= half)
    low_abs = sum(ab for p, (_, _, ab) in strata.items() if p <= half)
    tot_count = sum(c for (c, _, _) in strata.values())
    tot_abs = sum(ab for (_, _, ab) in strata.values())
    cnt_share = low_count / tot_count if tot_count else 0
    abs_share = low_abs / tot_abs if tot_abs else 0
    max_pk = max((ab / n for _, (_, _, ab) in strata.items()), default=0)
    lines.append(
        f"SUMMARY: popcount<=half({half}) of range(1..{p_max}): "
        f"count-share={cnt_share:.3f}, |S|-weight-share={abs_share:.3f}; "
        f"max stratum |sum|/n = {max_pk:.4f}"
    )
    lines.append("")
    return lines, strata, total


def make_random_r(n, seed):
    """Fixed-seed random residue string over {1,3} (odd-prime-like support),
    length n+1 (r[0] arbitrary, matches r[j]=q_j mod 4 usage)."""
    rng = random.Random(seed)
    r = [1 if rng.random() < 0.5 else 3 for _ in range(n + 1)]
    return r


def main():
    # --- cross-checks on small n: three independent routes agree ---
    for n in [200]:
        r = mod4_string(n + 1)
        h = h_from_r(r)
        Ss, os_ = s_sos(n, h)
        Sd, od = s_direct(n, h)
        Sc, oc = s_char_runs(n, r)
        terms = s_terms_sos(n, h)
        print(f"cross-check n={n}: sos=({Ss},{os_}) dir=({Sd},{od}) "
              f"char=({Sc},{oc}) terms_sum={sum(terms)} "
              f"match={Ss==Sd==Sc==sum(terms) and os_==od==oc==terms.count(-1)}")

    big_ns = [400, 1000, 4000]
    for n in big_ns:
        r = mod4_string(n + 1)
        lines, strata, total = run(n, r, "PRIMES")
        print("\n".join(lines))

    # control: fixed-seed random h (random r over {1,3})
    for n in big_ns:
        r = make_random_r(n, seed=20240717)
        lines, strata, total = run(n, r, "RANDOM-{1,3}")
        print("\n".join(lines))


if __name__ == "__main__":
    main()
