#!/usr/bin/env python3
"""Negative-control verification for refuting approach walsh-subset-sum-fold-structure.

Candidate 2 claims a structural (Walsh / subset-sum) lower bound on
wt(Phi_n x) from Phi's geometry alone, valid for x not 'complicated' in the
five closed-door senses. Closed door 4 says there EXIST balanced AND anti-dyadic
strings with wt(Phi_m h) in {1,2} for m = 8,16,24,32 -- i.e. structurally rich,
max-weight inputs whose fold image is tiny.

This program does NOT reopen the door: it verifies, for the small n where
exhaustion is free, that the *kind* of obstruction door 4 names is real --
that many balanced (weight floor(n/2)) strings have fold weight far below n/2,
so no structural bound from Phi alone (with no complexity hypothesis on x) can
hold. It is a negative control on the refutation's premise, not a new witness.

Use the fold's own exact weight (lib.supply_fold.s_sos -> count of T=1), which
is the same computable object as nu2(n) = wt(Phi_n h).
"""
from itertools import combinations
from lib.supply_fold import s_sos


def fold_weight(n, hbits):
    """wt(Phi_n x): count of d in [2, n-1] with T(n,d)=1 (numeric parity string)."""
    # s_sos expects h[j] in {0,1}, indexed 0..n-1
    S, ones = s_sos(n, [int(b) for b in hbits])
    return ones


def main():
    for n in (8, 16, 24):
        half = n // 2
        total = 0
        nonzero = 0
        min_w = n + 1
        best = None
        # Balanced strings = choose 'half' of the n positions to be 1.
        # For n=24, C(24,12)=2.7e6 -- too many to brute with an O(n log n)
        # per string. So for n=24 we go PARTIAL (subsample) and say so.
        combs = combinations(range(n), half)
        from itertools import islice
        if n <= 16:
            iterable = combs
            cap = None
        else:
            iterable = islice(combs, 200)   # subsample for n=24
            cap = 200
        count = 0
        seen_min = n + 1
        seen_best = None
        for ones_pos in iterable:
            h = [0] * n
            for p in ones_pos:
                h[p] = 1
            w = fold_weight(n, h)
            if w < seen_min:
                seen_min = w
                seen_best = h
            count += 1
        label = f"min over {count} balanced strings (subsample)" if cap else \
                f"min over ALL {count} balanced strings"
        print(f"n={n}: {label}: min wt(Phi_n x) = {seen_min}  (n/2 = {n//2})")
        print(f"    witness (first letters of 0/1 string): {''.join(map(str,seen_best))}")


if __name__ == "__main__":
    main()
