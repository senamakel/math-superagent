"""Print realizing families for regular UC families to find a construction pattern.
Each present element has the same count c; r present elements. Aim: understand
how to build regular families for every c in 1..2^{r-1} (achievability half),
which would make the regularity a theorem rather than a conjecture.
"""
from lib.uc import decide_union_closed, abundance


def popcount(x):
    return bin(x).count("1")


def enumerate_families(n):
    res = []
    for mask in range(1, 1 << (1 << n)):
        F = frozenset(s for s in range(1 << n) if (mask >> s) & 1)
        if decide_union_closed(F):
            res.append(F)
    return res


def m2s(F, n):
    """masks -> human-readable subset strings of [n]."""
    out = []
    for s in sorted(F):
        out.append("{" + ",".join(str(i + 1) for i in range(n) if (s >> i) & 1) + "}")
    return " ".join(out)


n = 4
fams = enumerate_families(n)
examples = {}
for F in fams:
    ab = abundance(F, n)
    present = [a for a in ab if a > 0]
    if len(set(present)) != 1 or not present:
        continue
    c, r = present[0], len(present)
    examples.setdefault((r, c), []).append(F)

for r in range(1, n + 1):
    for c in range(1, 2 ** (r - 1) + 1):
        famlist = examples.get((r, c), [])
        # show up to 3 non-isomorphic-looking ones (different size)
        shown = []
        seen_sizes = set()
        for F in famlist:
            if len(F) not in seen_sizes:
                seen_sizes.add(len(F))
                shown.append(F)
        print(f"r={r} c={c}: {len(famlist)} regular families; "
              f"sizes={sorted(len(F) for F in famlist)} |F|")
        for F in shown[:3]:
            print(f"     |F|={len(F)}: {m2s(F, n)}")
