"""Ground the librarian's literature hunt: compute the core objects of COLLAPSE."""
import itertools

def submasks(d):
    """All binary submasks of d."""
    s = d
    out = []
    while True:
        out.append(s)
        if s == 0:
            break
        s = (s-1) & d
    return out

def M(n, d):
    """Down-set translate M_d = {n-1-d + o : o submask of d}."""
    return {n-1-d + o for o in submasks(d)}

def symmetric_difference_size(n, d, dp):
    a = M(n, d); b = M(n, dp)
    return len(a ^ b)

for n in [8, 12]:
    print(f"n={n}")
    # multiset of symmetric difference sizes
    from collections import Counter
    sizes = Counter()
    for d in range(2, n):
        for dp in range(2, n):
            sizes[symmetric_difference_size(n, d, dp)] += 1
    print("  size multiset:", dict(sorted(sizes.items())))
    print("  (n-2)^2 =", (n-2)**2, " sum =", sum(sizes.values()))
