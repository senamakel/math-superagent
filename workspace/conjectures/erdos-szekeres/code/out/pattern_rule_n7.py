#!/usr/bin/env python3
"""Test the characterization conjecture for FULL block patterns at n=7.

Conjecture: a block-count pattern of an (n-1)-subset of es_construct(n) is FULL
(every realizing subset convex) IFF every point-taking >=2 occupies only blocks
1 or n-3 (the interior blocks adjacent to the endpoint singletons); blocks
2..n-4 take at most 1.  (With a switch for whether a >=3 take in block 1/n-3 is
also FULL.)

We enumerate EVERY block-count pattern (not just those with a convex realization)
and test FULL (all realizations convex) vs the rule, so we catch patterns the
earlier counter dropped (zero convex realizations).
"""
from itertools import product
from math import comb as C
from time import time

from lib.es_construct import es_set_blocks
from lib.es_geom import in_convex_position


def all_by_pattern(sizes, pat, pts):
    """Yield every (n-1)-subset realization with block pattern pat."""
    import itertools as it
    nb = len(sizes)
    off = 0
    pos = []
    for s in sizes:
        pos.append(list(range(off, off + s)))
        off += s
    choice_lists = [list(it.combinations(pos[i], pat[i])) for i in range(nb)]
    for combo in it.product(*choice_lists):
        idxs = [x for g in combo for x in g]
        yield [pts[j] for j in idxs]


def rule(pat, sizes):
    """Characterization conjecture: interior blocks 2..n-4 take at most 1;
    blocks 1 and n-3 take at most 2.  Return (satisfies, reason)."""
    nb = len(sizes)
    for i in range(nb):
        if 2 <= i <= nb - 3:         # strictly interior
            if pat[i] >= 2:
                return False, f"interior block {i} takes {pat[i]}"
    return True, "ok"


def main():
    n = 7
    pts, blocks = es_set_blocks(n)
    sizes = [len(b) for b in blocks]
    nb = len(sizes)
    r = n - 1
    print(f"n={n} sizes={sizes}")

    # enumerate all patterns (sum = r, pat[i] <= sizes[i])
    def gen_pats(i, rem, cur):
        if i == nb:
            if rem == 0:
                yield tuple(cur)
            return
        mx = min(sizes[i], rem)
        for v in range(mx + 1):
            cur.append(v)
            yield from gen_pats(i + 1, rem - v, cur)
            cur.pop()

    mismatches = []
    t0 = time()
    npats = 0
    for pat in gen_pats(0, r, []):
        npats += 1
        # compute total realizations
        tot = 1
        for i in range(nb):
            tot *= C(sizes[i], pat[i])
        pred = rule(pat, sizes)[0]
        # test FULL: all realizations convex
        is_full = True
        for sub in all_by_pattern(sizes, pat, pts):
            if not in_convex_position(sub):
                is_full = False
                break
        if pred != is_full:
            mismatches.append((pat, pred, is_full, tot))
    print(f"patterns enumerated: {npats}  time {time()-t0:.1f}s")
    if not mismatches:
        print("NO MISMATCH: FULL  <=>  interior blocks 2..n-4 take at most 1 "
              "(blocks 1, n-3 unrestricted so far).")
    else:
        print(f"MISMATCHES ({len(mismatches)}):")
        for m in mismatches[:40]:
            print("   ", m)
        # also report counts
        only_false_neg = [m for m in mismatches if m[1] and not m[2]]
        only_false_pos = [m for m in mismatches if not m[1] and m[2]]
        print("rule-true-but-not-full (false negatives):", len(only_false_neg))
        print("rule-false-but-full (false positives):", len(only_false_pos))
        for m in only_false_pos[:20]:
            print("   FP:", m)


if __name__ == "__main__":
    main()
