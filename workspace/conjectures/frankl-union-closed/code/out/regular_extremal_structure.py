"""What is the structure of a regular UC family (all present elements equal count c)?

We want to prove m <= 2c. Contributions to m: each member set S contributes
|S| to the total sum of degrees; sum of degrees = r*c. A union-closed family
need not contain all subsets, but the join-irreducibles generate it.

Key structural question: in a REGULAR UC family with r present elements and m
members, what is the MAXIMUM m for given (r, c) that is UC and regular?
From the exhaustive data we can tabulate (r,c) -> observed max m, and check
the structure of the extremal families (do they look like the "c-slice of
subcubes" interpretation, i.e. families whose members are the sets that contain
at least c... no). Let us inspect (r,c)->max m and the extremal family.

This is a search for the structure that PROVES m <= 2c, hence abundance in
every regular UC family. If max m == 2c exactly with a clean family structure,
a proof follows.
"""
from lib.uc import decide_union_closed, abundance


def enumerate_families(n):
    res = []
    for mask in range(1, 1 << (1 << n)):
        F = frozenset(s for s in range(1 << n) if (mask >> s) & 1)
        if decide_union_closed(F):
            res.append(F)
    return res


def m2s(F, n):
    return " ".join(
        "{" + ",".join(str(i + 1) for i in range(n) if (s >> i) & 1) + "}"
        for s in sorted(F))


n = 5
fams = enumerate_families(n)
by_rc = {}   # (r,c) -> (max_m, list of (m, family))
for F in fams:
    ab = abundance(F, n)
    present = [a for a in ab if a > 0]
    if len(set(present)) != 1 or not present:
        continue
    c, r = present[0], len(present)
    m = len(F)
    cur = by_rc.setdefault((r, c), [0, []])
    if m > cur[0]:
        cur[0] = m
        cur[1] = [(m, F)]
    elif m == cur[0]:
        cur[1].append((m, F))

print(f"n={n}: (r,c) -> max |F|, and whether 2c is attained, with examples")
for (r, c), (mx, fams) in sorted(by_rc.items()):
    ex = fams[0][1]
    print(f"  r={r} c={c}: max m={mx} (2c={2*c}, ratio {mx/(2*c):.3f})  "
          f"n_real={len([a for a in abundance(ex, n) if a>0])}")
    if mx == 2 * c:
        print(f"      extremal at 2c: {m2s(ex, n)}")