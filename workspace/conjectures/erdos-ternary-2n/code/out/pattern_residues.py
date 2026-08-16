"""Probe survivor residues for congruence-closure structure.

All survivors are even (n even forced by 2^n = 1 mod 3). The naive heuristic
thinks survivors spread like (2/3)^k over halves. Question: do the survivor
residues concentrate in particular classes mod small powers of 2? This is the
'statistic along n' the symbolic-invariant route wants.
"""

def survivors(k):
    A = {0}
    cur = 1
    while cur < k:
        L = 2 * 3 ** (cur - 1)
        next_mod = 3 ** (cur + 1)
        g = pow(2, L, next_mod)
        p3k = 3 ** cur
        Anext = set()
        for r in A:
            base = pow(2, r, next_mod)
            gp = 1
            for j in range(3):
                v = (base * gp) % next_mod
                d = (v // p3k) % 3
                if d in (0, 1):
                    Anext.add(r + j * L)
                gp = gp * g % next_mod
        A = Anext
        cur += 1
    return A

for k, mod in [(8, 4), (8, 8), (8, 16), (8, 32), (8, 64),
               (10, 16), (10, 32), (10, 128),
               (12, 8), (12, 16), (12, 256)]:
    S = survivors(k)
    from collections import Counter
    c = Counter(r % mod for r in S)
    # expected fraction vs actual spread
    vals = sorted(c.items())
    spread = c
    print(f"k={k} mod={mod}: {len(c)}/{mod} classes hit, "
          f"classes: {[(v, cnt) for v, cnt in vals]}")
