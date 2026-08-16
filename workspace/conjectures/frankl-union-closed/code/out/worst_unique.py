"""Count, over all union-closed families on [n] (n<=4), how many achieve the
worst min-element-frequency 1/(2^{n-1}+1), and report their structures.
Tests uniqueness of the near-k-cube as extremal."""

from lib.uc import decide_union_closed, abundance
from itertools import permutations


def canonical(fam, n):
    """Canonical form of a family under relabeling of [n]."""
    best = None
    for perm in permutations(range(n)):
        mapped = frozenset(tuple(sorted((1 << perm[i]) for i in range(n) if (s >> i) & 1)) for s in fam)
        # simpler: map bitmask via permutation
        mapped = set()
        for s in fam:
            new = 0
            for i in range(n):
                if (s >> i) & 1:
                    new |= 1 << perm[i]
            mapped.add(new)
        key = tuple(sorted(mapped))
        if best is None or key < best:
            best = key
    return best


for n in range(1, 5):
    worst_target = 1.0 / (2 ** (n - 1) + 1)
    all_masks = list(range(1 << n))
    achievers = []
    for sub in range(1 << len(all_masks)):
        fam = set()
        for i, mask in enumerate(all_masks):
            if (sub >> i) & 1:
                fam.add(mask)
        if not fam or fam == {0}:
            continue
        if not decide_union_closed(fam):
            continue
        m = len(fam)
        counts = abundance(fam, n)
        present = [c for c in counts if c > 0]
        if not present:
            continue
        if abs(min(present) / m - worst_target) < 1e-12:
            achievers.append(canonical(fam, n))
    distinct = set(achievers)
    print(f"n={n}: #achieving families = {len(achievers)}, "
          f"#distinct up to isomorphism = {len(distinct)}")
    for c in sorted(distinct):
        print(f"    {list(c)}")
