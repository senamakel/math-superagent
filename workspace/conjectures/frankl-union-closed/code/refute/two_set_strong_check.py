"""Refuter check: for a UC family containing a 2-set {x,y}, is one of x,y
abundant (the strong form of settled rung R-uc-with-two-set)? Test on all UC
families over [n], n<=4, using the canonical oracle's own exhaustive enum.

We enumerate UC families exactly as the oracle does and test the STRONG claim:
some 2-set {x,y} in F has max(c_x, c_y) >= |F|/2. Since a UC family may contain
many 2-sets, the strong claim only needs ONE of its 2-sets to satisfy this; a
family is a counterexample to the STRONG form if NO 2-set in it has an abundant
element. (The rung itself is weaker: some element anywhere abundant.)
"""
from itertools import combinations
from lib.uc import decide_union_closed, abundance


def all_uc_families(n):
    masks = list(range(1 << n))
    out = []
    for sub in range(1 << len(masks)):
        fam = set()
        for i, m in enumerate(masks):
            if (sub >> i) & 1:
                fam.add(m)
        if fam in (set(), {0}):
            continue
        if decide_union_closed(fam):
            out.append(fam)
    return out


def two_sets_in(F, n):
    """all 2-element masks present in F, as (x,y) element indices"""
    res = []
    for x, y in combinations(range(n), 2):
        if (1 << x) | (1 << y) in F:
            res.append((x, y))
    return res


def main():
    for n in range(1, 5):
        fams = all_uc_families(n)
        with_2set = 0
        strong_viol = []  # family contains a 2-set but NO 2-set has an abundant element
        for F in fams:
            ts = two_sets_in(F, n)
            if not ts:
                continue
            with_2set += 1
            m = len(F)
            counts = abundance(F, n)
            ok = any(2 * counts[x] >= m or 2 * counts[y] >= m for (x, y) in ts)
            if not ok:
                strong_viol.append((sorted(F), [(x, y, counts[x], counts[y]) for x, y in ts], m))
        print(f"n={n}: {len(fams)} UC fams, {with_2set} contain a 2-set, "
              f"{len(strong_viol)} contain a 2-set but NONE of their 2-sets has an abundant element")
        for fam, tsinfo, m in strong_viol[:5]:
            print("   VIOL:", fam, "m=", m, "2-sets(counts):", tsinfo)


if __name__ == "__main__":
    main()
