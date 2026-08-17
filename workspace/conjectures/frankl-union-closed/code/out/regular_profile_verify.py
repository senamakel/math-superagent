"""Verify the regular-profile regularity and find realizing families.

Regular UC family = all present elements have equal abundance count c.
REG(n) = # distinct regular profiles over all UC families on [n].
Conjecture from n=1..5 data: for fixed r (number of present elements) the
achievable degrees are exactly {1,...,2^{r-1}}, so REG(n) = sum_{r=1}^n 2^{r-1}
= 2^n - 1.

We enumerate n=1..4 exhaustively via lib.uc (guarded vs A121921), compute all
regular profiles, the per-r achievable-degree sets, and PRINT one realizing
family for each distinct profile so the structure is visible (esp. the
non-threshold degrees like (2,2,2)).
"""
from lib.uc import decide_union_closed, abundance


def popcount(x):
    return bin(x).count("1")


def enumerate_families(n):
    """All nonempty union-closed families on [n] as frozensets of masks."""
    res = []
    for mask in range(1, 1 << (1 << n)):  # nonempty subfamily
        F = frozenset(s for s in range(1 << n) if (mask >> s) & 1)
        if decide_union_closed(F):
            res.append(F)
    return res


GUARD = {1: 3, 2: 13, 3: 121, 4: 4959}  # A121921 counts incl. trivial {empty}; r=0 filtered below

for n in range(1, 5):
    fams = enumerate_families(n)
    assert len(fams) == GUARD[n], (n, len(fams), GUARD[n])
    by_r = {}          # r -> set of achievable degrees c
    example = {}       # (r,c) -> one realizing family (sorted masks)
    for F in fams:
        ab = abundance(F, n)
        present = [a for a in ab if a > 0]
        if len(set(present)) != 1:
            continue
        c = present[0]
        r = len(present)
        if r == 0:
            continue
        by_r.setdefault(r, set()).add(c)
        example.setdefault((r, c), sorted(F))
    print(f"n={n}: UC families={len(fams)}")
    total = 0
    for r in sorted(by_r):
        degs = sorted(by_r[r])
        assert degs == list(range(1, 2 ** (r - 1) + 1)), (n, r, degs)
        print(f"  r={r}: achievable degrees = {degs}  "
              f"({len(degs)} = 2^{r-1} = {2**(r-1)})")
        total += len(degs)
    print(f"  REG(n) = sum_r 2^(r-1) = {total} == 2^n-1 = {2**n-1}: {total == 2**n-1}")
    # print a realizing family for a non-threshold degree to see structure
    for (r, c), fam in sorted(example.items()):
        if r >= 2 and c not in (1, 2 ** (r - 1)):
            print(f"    e.g. profile r={r} c={c}: family masks={fam}")
            break
