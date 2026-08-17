"""Exact direct enumeration of cups and caps of a point set by DFS.

Builds cup and cap chains (x-sorted index sequences with strictly increasing /
decreasing consecutive Exact-rational slopes) by depth-first extension, storing
each chain as a frozenset of original point indices together with its
rightmost-by-x order rank.  Only true chains are generated — never the whole
2^N subset space — so it is far faster than testing every subset.

`chains_by_rightmost(pts, max_s)` returns (cups, caps); each is a dict mapping
rightmost-x-order-rank -> list of frozensets (the chains with that rightmost),
covering chain sizes 2..max_s.

Validated against an exhaustive subset test (`split_probe.py`, which tested all
C(N,s) subsets) on es_construct(5,6,7): every per-size cup and cap total
matches exactly.  At n=7 this runs in ~1.7s where the exhaustive subset test
took ~350s, at identical counts.
"""
from fractions import Fraction
from collections import Counter


def _frac_slope(a, b):
    """Exact dy/dx with a[0] < b[0] (x-order guaranteed by caller)."""
    return (Fraction(b[1]) - Fraction(a[1])) / (Fraction(b[0]) - Fraction(a[0]))


def chains_by_rightmost(pts, max_s):
    """(cups, caps): each a dict rightmost-by-x-order-rank -> list of
    frozensets of ORIGINAL point indices forming a (cup|cap) chain of size
    2..max_s with that rightmost point."""
    N = len(pts)
    # x-order rank -> original index
    xord = sorted(range(N), key=lambda i: Fraction(pts[i][0]))
    orank = {i: r for r, i in enumerate(xord)}   # original idx -> x-rank

    def dfs_all(compare):
        res = {}
        def dfs(cur_orig, last_slope):
            fs = frozenset(cur_orig)
            rm = orank[cur_orig[-1]]
            if len(cur_orig) >= 2:
                res.setdefault(rm, []).append(fs)
            if len(cur_orig) >= max_s:
                return
            last_rank = orank[cur_orig[-1]]
            for rr in range(last_rank + 1, N):
                nxt = xord[rr]
                s = _frac_slope(pts[cur_orig[-1]], pts[nxt])
                if last_slope is None or compare(last_slope, s):
                    dfs(cur_orig + (nxt,), s)
        for i in range(N):
            dfs((xord[i],), None)
        return res

    cups = dfs_all(lambda prev, cur: prev < cur)   # increasing slopes
    caps = dfs_all(lambda prev, cur: prev > cur)   # decreasing slopes
    return cups, caps


def chain_totals(cups, caps):
    """(cup_totals_by_size, cap_totals_by_size) as size->count dicts."""
    ct, cpt = Counter(), Counter()
    for lst in cups.values():
        for fs in lst:
            ct[len(fs)] += 1
    for lst in caps.values():
        for fs in lst:
            cpt[len(fs)] += 1
    return ct, cpt