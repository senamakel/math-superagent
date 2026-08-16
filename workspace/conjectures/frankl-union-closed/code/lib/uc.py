"""Exact oracle for Frankl's union-closed sets conjecture.

A family F of subsets of [n] is a `set` of integer bitmasks: element i (0-indexed)
is in set s iff bit i of s is 1. All arithmetic is exact integer arithmetic;
no floats anywhere.

Every later experiment on union-closure or abundance must call these routines —
this is the one canonical oracle. The functions were checked against the guards
in problem.md and against exhaustive enumeration for n <= 4 (see
code/out/uc_oracle_check.py and verify_uc_exhaustive below).

Functions
---------
decide_union_closed(F)        -> bool   F closed under bitwise OR
abundance(F, n)               -> list[int]  exact count per element i in [n]
abundant_elements(F, n)       -> list[int]  elements with count >= ceil(|F|/2)
closure(generators)           -> set[int]   smallest union-closed superset
verify_uc_exhaustive(n)       -> (count, counterexample) for n <= 4, oracle only
"""


def decide_union_closed(F):
    """True iff, for every A, B in F, their bitwise OR A|B is in F."""
    for a in F:
        for b in F:
            if (a | b) not in F:
                return False
    return True


def abundance(F, n):
    """Exact integer count, per element i in [n], of how many sets of F contain it.

    count for element i is the number of sets s in F with bit i set. Returns a
    list of n exact ints.
    """
    counts = [0] * n
    for s in F:
        for i in range(n):
            if (s >> i) & 1:
                counts[i] += 1
    return counts


def abundant_elements(F, n):
    """Elements present in at least ceil(|F|/2) of the sets (density >= 1/2).

    count >= |F|/2 exactly, i.e. 2*count >= |F|. A family that is not
    union-closed can still have abundant elements; this routine only reports
    abundances, it does not check closure.
    """
    if not F:
        return []
    m = len(F)
    counts = abundance(F, n)
    return [i for i, c in enumerate(counts) if 2 * c >= m]


def closure(generators):
    """Smallest union-closed superset of `generators` (its union-closure).

    Reachability: start from generators and repeatedly adjoin pairwise unions
    until the family is closed under OR. Returns the reached set (which is
    exactly the set of all unions of subfamilies of generators).
    """
    reached = set(generators)
    changed = True
    while changed:
        changed = False
        new = list(reached)
        for a in new:
            for b in new:
                u = a | b
                if u not in reached:
                    reached.add(u)
                    changed = True
    return reached


def verify_uc_exhaustive(n):
    """Brute force ONLY re usable as an oracle: for each union-closed family F
    over [n] (excluding {empty}), check F has an abundant element.

    n must be <= 4. The whole power set has 2^n masks, so there are 2^(2^n)
    subfamilies to consider (65536 at n=4). Returns (count_of_union_closed,
    first_counterexample_or_None). Exponential in the family count: this is the
    sanctioned brute-force exception, NOT a method for larger n.
    """
    assert n <= 4, "verify_uc_exhaustive is oracle-only; refuse n > 4"
    masks = range(1 << n)
    all_masks = list(masks)
    count = 0
    empty = 0  # bitmask of the empty family is 0 itself
    for sub in range(1 << len(all_masks)):
        fam = set()
        for i, mask in enumerate(all_masks):
            if (sub >> i) & 1:
                fam.add(mask)
        if not fam:
            continue  # exclude {empty} family
        if not decide_union_closed(fam):
            continue
        count += 1
        # exclude the family {empty} exactly: the single set whose mask is 0
        if fam == {0}:
            continue
        if not abundant_elements(fam, n):
            return count, fam
    return count, None
