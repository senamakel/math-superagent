"""Independent verification of the origin-connected (C1) counts.

Second, definitionally-different route: for small box sizes, enumerate ALL
subsets of [0,m-1]^d containing the origin and count those that are literally
origin-connected (every non-origin cell has a backward neighbour in S).

This checks the forward-growth enumeration in test_c1.py for small m without
sharing its logic.  Only usable for tiny m because subsets grow exponentially;
here it validates the generator on the exact small cases whose small m make
both 2D choices available.
"""

import sys
from itertools import combinations


def origin_connected(cells, dim):
    """Definitional test: every non-origin cell has a backward neighbour in S."""
    Sset = set(cells)
    for c in Sset:
        if c == (0,) * dim:
            continue
        ok = False
        for i in range(dim):
            pc = list(c)
            if pc[i] > 0:
                pc[i] -= 1
                if tuple(pc) in Sset:
                    ok = True
                    break
        if not ok:
            return False
    return True


def count_by_subsets(dim, m):
    """# origin-connected subsets of [0,m-1]^d of size m containing origin."""
    box = [(x, y) if dim == 2 else (x, y, z)
           for x in range(m) for y in range(m)
           for z in (range(m) if dim == 3 else [0])]
    origin = (0,) * dim
    rest = [c for c in box if c != origin]
    cnt = 0
    for extra in combinations(rest, m - 1):
        if origin_connected((origin,) + extra, dim):
            cnt += 1
    return cnt


def main():
    # 2D sizes m=1..6, 3D sizes m=1..4 (exhaustive subsets)
    print("dim m  by_subset  (generator values for comparison)")
    for dim, mlist in ((2, range(1, 7)), (3, range(1, 5))):
        for m in mlist:
            c = count_by_subsets(dim, m)
            print(f"{dim}  {m}  {c}")


if __name__ == "__main__":
    main()
