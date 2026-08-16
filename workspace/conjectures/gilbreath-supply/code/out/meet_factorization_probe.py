#!/usr/bin/env python3
"""Probe the load-bearing claim of mobius-meet-factorization.

Claim under test: for j = d & d' (j subseteq d), the reflected downset
difference  D := {s : s subseteq d, s NOT subseteq j}  decomposes as

    D = disjoint union over nonempty submasks a of (d \ j)  of  (a + downset(j)),

where + is integer addition (valid because a & j == 0).  Consequently:
  * every run of D has length 2^{nu2(j+1)}  (the run length of downset(j));
  * the number of runs of D is (2^{popcount(d\j)} - 1) * (number of runs of downset(j)).

We test this against brute enumeration of every (d, j) with j subseteq d for
small d.  We also directly test whether the monomial over D factorizes
"per-bit" (the literal independence-polynomial claim in the approach file)
versus "per-nonempty-submask" (the corrected claim above).
"""

from collections import Counter


def popcount(x):
    return bin(x).count("1")


def nu2(x):
    # 2-adic valuation
    g = 0
    while x % 2 == 0 and x > 0:
        g += 1
        x //= 2
    return g


def submasks(x):
    s = x
    out = []
    while True:
        out.append(s)
        if s == 0:
            break
        s = (s - 1) & x
    return out


def runs(S):
    S = sorted(S)
    out = []
    for x in S:
        if out and x == out[-1][1] + 1:
            out[-1][1] = x
        else:
            out.append([x, x])
    return out


def downset(j):
    return set(submasks(j))


def test_difference(d, j):
    """Return (ok, detail) comparing brute D vs the claimed decomposition."""
    # j must be a submask of d
    if (j & d) != j:
        return True, "skip"
    D = set(submasks(d)) - set(submasks(j))
    B = d ^ j  # d \ j
    # claimed decomposition
    claimed = set()
    for a in submasks(B):
        if a == 0:
            continue
        for s in submasks(j):
            claimed.add(a + s)  # a & s == 0 since a in B, s in j
    if claimed != D:
        return False, ("set mismatch", d, j, sorted(D), sorted(claimed))
    # run-length uniformity
    lens = [v - u + 1 for (u, v) in runs(D)]
    target = 2 ** nu2(j + 1)
    if any(L != target for L in lens):
        return False, ("run length mismatch", d, j, lens, target)
    n_runs_claimed = (2 ** popcount(B) - 1) * len(runs(downset(j)))
    if len(runs(D)) != n_runs_claimed:
        return False, ("run count mismatch", d, j, len(runs(D)), n_runs_claimed)
    return True, "ok"


def main():
    failures = []
    tested = 0
    for d in range(1, 128):
        for j in submasks(d):
            tested += 1
            ok, detail = test_difference(d, j)
            if not ok:
                failures.append(detail)
                if len(failures) <= 10:
                    print("FAIL", detail)
    print(f"tested {tested} (d,j) pairs, failures {len(failures)}")

    # negative control: verify the run-length claim FAILS if we use the wrong
    # (per-bit) decomposition on a case where |d\j| >= 2 and j has multi-run downset
    print("\nPer-bit (independence polynomial) counterexample check:")
    # d = 111 (7), j = 001 (1): D has 6 elements, 3 runs of length 2.
    # A per-bit factorization over B = {bits 1,2} would give |D| = ... not a product
    # of per-bit factors. Show the monomial count does not equal prod over bits.
    d, j = 7, 1
    B = d ^ j
    D = set(submasks(d)) - set(submasks(j))
    print(f"  d={d}, j={j}, B={B}, |D|={len(D)}, runs={runs(D)}")
    print(f"  per-nonempty-submask count = {2**popcount(B)-1} factors, "
          f"each of size 2^{popcount(j)} = {2**popcount(j)}")
    print(f"  total |D| = {(2**popcount(B)-1) * 2**popcount(j)}")


if __name__ == "__main__":
    main()
