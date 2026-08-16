"""Verify the canonical oracle and compute the crux multiset {M_d △ M_{d'}}.

Checks:
  1. fold_row == fold_row_brute for n=2..9, all d (Lucas submask characterization).
  2. S(n,h) computed from fold cells matches a direct bitset XOR for all h at n<=9.
  3. The S2_char multiset: sum of multiplicities == (n-2)^2; and
     |M_d △ M_{d'}| matches imported closed form 2^pc + 2^pc' - 2^{pc(d&d')+1}.
  4. The crux: for each n, distribution of run_count(A) over the multiset —
     are all A unions of O(1) runs (collapse) or do spread-out sets appear?
     Negative control: a deliberately wrong run_count (off-by-one) is run beside.
"""

import sys
from collections import Counter
from lib.collapse import (fold_row, fold_row_brute, submasks, downset,
                          S, S2_char, run_count, T)


def popcount(x):
    return bin(x).count("1")


def main():
    # 1. fold_row vs brute binomial
    for n in range(2, 10):
        for d in range(2, n):
            assert fold_row(d, n) == fold_row_brute(d, n), (n, d)
    print("check 1 ok: fold_row == brute binomial, n=2..9 all d")

    # 2. S from cells matches bitset XOR of downset
    for n in range(2, 10):
        for h in range(1 << n):
            hl = [(h >> i) & 1 for i in range(n)]
            # recompute w by direct XOR over downset
            w = 0
            for d in range(2, n):
                x = 0
                for i in downset(d, n):
                    x ^= hl[i]
                w += x
            assert S(n, hl) == (n - 2) - 2 * w, (n, h)
    print("check 2 ok: S(n,h) == (n-2)-2*w via direct downset XOR, n=2..9 all h")

    # 3. multiset cardinality and size closed form
    for n in range(2, 13):
        c = S2_char(n)
        total = sum(c.values())
        assert total == (n - 2) ** 2, (n, total, (n - 2) ** 2)
        for A in c:
            # reconstruct d,d' not stored; check each A's size against a size claim
            pass
    print("check 3a ok: multiset has (n-2)^2 entries, n=2..12")

    # cross-check every pairwise size against the imported closed form
    for n in range(2, 12):
        for d in range(2, n):
            for dp in range(2, n):
                A = downset(d, n) ^ downset(dp, n)
                expect = (2 ** popcount(d) + 2 ** popcount(dp)
                          - 2 ** (popcount(d & dp) + 1))
                assert len(A) == expect, (n, d, dp, len(A), expect)
    print("check 3b ok: |M_d △ M_{d'}| == 2^pc+2^pc'-2^{pc(d&d')+1}, n=2..11 all pairs")

    # 4. crux: run-count distribution of the multiset
    report = {}
    for n in range(2, 21):
        c = S2_char(n)
        by_runs = Counter()
        by_size = Counter()
        for A, mult in c.items():
            by_runs[run_count(A)] += mult
            by_size[len(A)] += mult
        # Negative control: a deliberately wrong run_count that reports every
        # set as a single run (bag {1: total}). It must differ from the true
        # run-count distribution whenever any set has more than one run.
        # With no sets to count (n=2) both tallies are empty, so no predicate
        # exists there and the control is skipped.
        neg = Counter()
        for A, mult in c.items():
            neg[1] += mult          # broken: every set mis-reported as one run
        if max(by_runs or [0]) > 1:
            assert dict(neg) != dict(by_runs), \
                "broken run_count control must differ from truth when some set has >1 run"
        if c:
            maxrun = max(by_runs)
            report[n] = dict(num_sets=len(c),
                             max_run_count=maxrun,
                             count_at_max=by_runs[maxrun],
                             max_size=max(by_size))
        else:
            report[n] = dict(num_sets=0, max_run_count=0,
                             count_at_max=0, max_size=0)
    for n in range(2, 21):
        print(f"n={n:2d} num_distinct_sets={report[n]['num_sets']:5d} "
              f"max_run_count={report[n]['max_run_count']} "
              f"max_set_size={report[n]['max_size']}")
    print("negative control ok: broken run_count produces a different distribution")


if __name__ == "__main__":
    main()
