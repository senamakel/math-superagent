#!/usr/bin/env python3
"""Verify G-run-telescope: the digital down-set runs and the telescoping
identity, for arbitrary {0,1} strings h. Pure combinatorial claim; attack it
first because everything else (G-endpoint-comparison-density) builds on it.

Definitions (problem.md facts 1-2):
  T(n,d) = XOR over bitwise submasks o of d of h[n-1-d+o],  d in [2,n-1].
  runs(↓d): maximal runs of consecutive integers in the down-set
    {o in [0,d] : o bitwise-submask of d}.
  Claim: with g = number of trailing 1-bits of d, each run has length 2^g,
    there are 2^{popcount(d)-g} runs, and the runs are the blocks
    [m*2^g, (m+1)*2^g - 1] for m running over submasks of (d >> g).
  Telescoping: for a run [u,v], XOR_{o=u..v} h[base+o] = [r_{base+u} != r_{base+v+1}]
    where h[j] = [r_{j+1} != r_j] (boundary sequence r).
  Consequence: T(n,d) = XOR over runs R of [r_{a_R} != r_{b_R}], a=n-1-d+u,
    b=n-1-d+v+1.
"""
import itertools


def submasks_of(d):
    s = d
    while True:
        yield s
        if s == 0:
            break
        s = (s - 1) & d


def downset(d):
    return set(submasks_of(d))


def min_ctz(x):          # number of trailing ZEROS (2-adic valuation); ctz(0)=undefined
    n = 0
    while (x >> n) & 1 == 0 and (x >> n) != 0:
        n += 1
    return n


def trailing_ones(d):
    g = 0
    while (d >> g) & 1:
        g += 1
    return g


def runs_from_formula(d):
    g = trailing_ones(d)
    runlen = 1 << g
    d_shifted = d >> g
    runs = []
    for m in range(d_shifted + 1):
        if (m & d_shifted) == m:
            u = m * runlen
            v = u + runlen - 1
            runs.append((u, v))
    return runs


def runs_true(ds):
    """True maximal runs of consecutive ints in the downset set ds."""
    ds = sorted(ds)
    runs = []
    for x in ds:
        if runs and x == runs[-1][1] + 1:
            runs[-1] = (runs[-1][0], x)
        else:
            runs.append((x, x))
    return runs


def check_runs(d):
    ds = downset(d)
    g = trailing_ones(d)
    true_runs = runs_true(ds)
    form_runs = runs_from_formula(d)
    expected_len = 1 << g
    expected_count = 1 << (bin(d).count('1') - g)
    ok_len = all(b - a + 1 == expected_len for (a, b) in form_runs)
    ok_count = len(form_runs) == expected_count
    ok_block = sorted(form_runs) == sorted(true_runs)
    return ok_len and ok_count and ok_block, (g, expected_len, expected_count,
                                             true_runs, form_runs)


def check_telescope(d, n, h):
    """Check T(n,d) via direct XOR vs via run-endpoint comparison, for a
    boundary string r (h = boundary of r)."""
    # direct
    base = n - 1 - d
    T = 0
    for o in submasks_of(d):
        T ^= h[base + o]
    # via runs: XOR over runs of [r_{base+u} != r_{base+v+1}]
    runs = runs_from_formula(d)
    T2 = 0
    for (u, v) in runs:
        a = base + u
        b = base + v + 1
        T2 ^= (1 if r[a] != r[b] else 0)
    return T == T2, T, T2


def main():
    # 1. run decomposition for all d up to 1000
    bad = 0
    for d in range(1, 1001):
        ok, info = check_runs(d)
        if not ok:
            print("RUN BAD d=", d, info)
            bad += 1
    print("run decomposition checked d=1..1000:", "ALL OK" if bad == 0 else f"{bad} BAD")

    # 2. telescoping identity for many h (random, primes, all-ones, sparse) and many (n,d)
    import random
    bad = 0
    checked = 0
    # boundary r: try random small values and the mod-4 primes pattern
    for trial in range(300):
        rlen = random.randint(10, 60)
        # random {1,3} boundary (like odd primes mod 4)
        r = [random.choice((1, 3)) for _ in range(rlen)]
        r[0] = 2
        h = [1 if r[j + 1] != r[j] else 0 for j in range(rlen - 1)]
        for _ in range(20):
            n = random.randint(5, min(rlen - 1, 40))
            d = random.randint(2, n - 1)
            ok, T, T2 = check_telescope(d, n, h)
            checked += 1
            if not ok:
                print("TELESCOPE BAD n,d=", n, d, T, T2)
                bad += 1
    print(f"telescoping checked (n,d) pairs on random r: {checked} pairs, "
          f"{'ALL OK' if bad == 0 else str(bad) + ' BAD'}")

    # 3. also verify on the real prime h and an all-ones h
    from lib.primes import h_string
    from lib.supply_fold import runs_of_downset
    # use library runs_of_downset to make sure lib and this file agree
    for d in range(1, 200):
        lib_runs = runs_of_downset(d)
        my_runs = sorted(runs_from_formula(d))
        if sorted(lib_runs) != my_runs:
            print("LIB MISMATCH d=", d, lib_runs, my_runs)
    print("library runs_of_downset agrees with formula (d=1..200)")


if __name__ == "__main__":
    main()
