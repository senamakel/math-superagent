#!/usr/bin/env python3
"""Characterise which binary strings h of length n have LINEAR SUPPLY.

nu2(n) = wt(Phi_n h) = number of d in [2,n-1] with T(n,d)=1. "Linear supply"
means nu2(n) >= c*n for a fixed c>0. This program maps, as a function of
Hamming weight w, how typical it is (fraction and mean of nu2/n) for strings
of that weight to have linear supply, using the canonical floored fold oracle
(d in [2,n-1]). Weight alone is NOT supply: the all-ones string (max weight n)
is a kernel vector with nu2/n -> 0 (negative control).

Oracle: lib.supply_fold.s_sos(n,h) -> (S, ones=nu2(n)), cross-checked against
s_direct(n,h) on a random 5% sample of the exhaustive rows. Exact integers;
only display ratios are floats.

Complexity: Part1 exhaustive is O(sum_{n in {6..16}} 2^n * n log n), dominated
by n=16 (2^16=65536 strings); Part2/Part3 are O(300 * few weights * n log n).
All polynomial; no exponential search.
"""

import random
from itertools import combinations

from lib.supply_fold import s_sos, s_direct, s_single_one


def single_one(n, j):
    h = [0] * n
    h[j] = 1
    return h


def main():
    out = []
    add = out.append

    # ---------------------------------------------------------------- PART 0
    add("=" * 78)
    add("PART 0 - ORACLE CHECK")
    add("=" * 78)
    add("sequence = weight-w binary strings over F2^n (all-ones as control)")
    add("oracle = lib.supply_fold.s_sos cross-checked vs s_direct")
    add("range   = n in {6..16 exhaustive, 32/64/128 sampled}")
    add("")

    # (a) mechanism: h = e_{n-2} -> nu2 == count of odd d in [2,n-1]
    add("(a) h = e_{n-2} (single 1 at index n-2): nu2(n) == count of odd d in [2,n-1]")
    mech_ok = True
    for n in range(3, 41):
        h = single_one(n, n - 2)
        Ss, ones_s = s_sos(n, h)
        Sd, ones_d = s_direct(n, h)
        odd_count = sum(1 for d in range(2, n) if d % 2 == 1)
        if not (ones_s == ones_d == odd_count and Ss == Sd == (n - 2) - 2 * odd_count):
            mech_ok = False
            add(f"  MISMATCH n={n}: s_sos={ones_s} s_direct={ones_d} odd_count={odd_count}")
    add(f"  s_sos == s_direct == odd-count for every n in 3..40: {mech_ok}")

    # (b) imported n=8 witness
    add("")
    add("(b) imported n=8 witness (EXACT reproduction):")
    for j, (expS, expnu2) in ((6, (0, 3)), (5, (-2, 4))):
        h = single_one(8, j)
        Ss, ones_s = s_sos(8, h)
        Sd, ones_d = s_direct(8, h)
        ok = (Ss == Sd == expS and ones_s == ones_d == expnu2)
        add(f"  h=e_{j}: s_sos=({Ss},{ones_s}) s_direct=({Sd},{ones_d}) "
            f"expected=({expS},{expnu2}) S^2={Ss*Ss}  {('OK' if ok else 'FAIL')}")

    # ---------------------------------------------------------------- PART 1
    add("")
    add("=" * 78)
    add("PART 1 - EXHAUSTIVE small n, grouped by Hamming weight w")
    add("=" * 78)
    header = ("n  w  count    mean nu2/n   >=0.25  >=0.40  >=0.45")
    add(header)
    add("-" * len(header))
    exhaustion = {}
    ns1 = [6, 8, 10, 12, 14, 16]
    # threshold mapping table for part 3
    threshold_rows = []
    for n in ns1:
        grouped = {w: [] for w in range(n + 1)}   # w -> list of nu2
        N = 1 << n
        checked = 0
        xchecked = 0
        total_rows = N
        for mask in range(N):
            h = [(mask >> j) & 1 for j in range(n)]
            Ss, ones = s_sos(n, h)
            w = sum(h)
            grouped[w].append(ones)
            # random 5% cross-check against s_direct
            if random.random() < 0.05:
                Sd, ones_d = s_direct(n, h)
                assert Ss == Sd and ones == ones_d, (n, w, Ss, Sd, ones, ones_d)
                xchecked += 1
        # store for part 3 (mean and frac>=.40 per weight, exact)
        thres = {}
        for w in range(n + 1):
            lst = grouped[w]
            cnt = len(lst)
            if cnt == 0:
                continue
            tot = sum(lst)
            mean = tot / cnt / n
            f25 = sum(1 for x in lst if x / n >= 0.25) / cnt
            f40 = sum(1 for x in lst if x / n >= 0.40) / cnt
            f45 = sum(1 for x in lst if x / n >= 0.45) / cnt
            thres[w] = (tot / cnt / n, f40)  # (mean nu2/n, frac>=0.40)
            add(f"{n:>2} {w:>2} {cnt:>6}   {mean:.4f}     {f25:5.3f}  {f40:5.3f}  {f45:5.3f}")
            checked += cnt
        assert checked == N, (n, checked, N)
        add(f"  [n={n}: cross-checked {xchecked} rows against s_direct, all agree]")
        exhaustion[n] = thres
        add("")

    # ---------------------------------------------------------------- PART 2
    add("=" * 78)
    add("PART 2 - SAMPLED larger n, by exact weight (300 random strings each)")
    add("=" * 78)
    add(header2 := "n    w     mean nu2/n   >=0.40")
    add("-" * len(header2))
    sampled = {}
    for n in [32, 64, 128]:
        sample_rows = {}
        for w in list(dict.fromkeys([1, 2, 3, 4, 5, 8, 16, 32, n // 2, n])):
            if w > n:
                continue
            S = 300
            vals = []
            for _ in range(S):
                pos = random.sample(range(n), w)
                h = [0] * n
                for p in pos:
                    h[p] = 1
                _, ones = s_sos(n, h)
                vals.append(ones)
            tot = sum(vals)
            mean = tot / S / n
            f40 = sum(1 for x in vals if x / n >= 0.40) / S
            sample_rows[w] = (mean, f40)
            add(f"{n:>3} {w:>3}   {mean:.4f}      {f40:5.3f}")
        sampled[n] = sample_rows
        add("")

    # ---------------------------------------------------------------- PART 3
    add("=" * 78)
    add("PART 3 - THE ANSWER: min weight w at which LINEAR SUPPLY becomes typical")
    add("(typical := mean nu2/n >= 0.40 AND fraction(nu2/n>=0.40) >= 0.5)")
    add("=" * 78)
    add("")
    add("--- exhaustive n (all strings): ---")
    add(f"{'n':>3} {'first w':>7} {'w/n':>6} {'mean@w':>7} {'frac@w':>7}")
    for n in ns1:
        thres = exhaustion[n]
        for w in range(n + 1):
            if w in thres:
                mean, f40 = thres[w]
                if mean >= 0.40 and f40 >= 0.5:
                    add(f"{n:>3} {w:>7} {w/n:>6.3f} {mean:>7.4f} {f40:>7.3f}")
                    break
        else:
            add(f"{n:>3}   (none)")
    add("")
    add("--- sampled n (300 per weight): ---")
    add(f"{'n':>3} {'first w':>7} {'w/n':>6} {'mean@w':>7} {'frac@w':>7}")
    for n in [32, 64, 128]:
        rows = sampled[n]
        for w in sorted(rows):
            mean, f40 = rows[w]
            if mean >= 0.40 and f40 >= 0.5:
                add(f"{n:>3} {w:>7} {w/n:>6.3f} {mean:>7.4f} {f40:>7.3f}")
                break
        else:
            add(f"{n:>3}   (none)")
    add("")
    add("--- extremes: ---")
    add("weight-1 strings: the operator's e_{n-2} sits at nu2~n/2 (odd d count) but")
    add("is ONE position; near-min positional supply for w=1 is not typical overall.")
    # measure weight-1 mean at n=16 exhaustively (part1 has n=16 weight1 row) and at n=128 by sample
    for n in [16]:
        add(f"  n={n} exhaustive, w=1: mean nu2/n={exhaustion[n][1][0]:.4f}, "
            f"frac>=0.40={exhaustion[n][1][1]:.3f}")
    add("")

    # ------------------------------------------------------ NEGATIVE CONTROL
    add("=" * 78)
    add("NEGATIVE CONTROL - all-ones string (max weight n) is in the kernel")
    add("nu2/n must -> 0, proving the metric reads position-structure, not weight")
    add("=" * 78)
    add(f"{'n':>3} {'nu2(n)':>7} {'nu2/n':>7}")
    for n in range(6, 41):
        h = [1] * n
        _, ones = s_sos(n, h)
        add(f"{n:>3} {ones:>7} {ones/n:>7.4f}")

    print("\n".join(out))


if __name__ == "__main__":
    main()
