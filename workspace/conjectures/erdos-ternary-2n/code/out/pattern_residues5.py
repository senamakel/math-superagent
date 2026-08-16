"""Confirm the exact claim: the classes of A_k mod 3^j are EXACTLY the elements
of [0,3^j) whose ternary digits lie in {0,1}, for k >= j (tested j,k ranges).
This is the survivor-residue regularity; verify it precisely.
"""
def survivor_sets(K):
    sets = {1: {0}}
    A = {0}
    cur = 1
    while cur < K:
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
        sets[cur] = A
    return sets

def digit01_set(mod):
    """all x in [0,mod) with ternary digits in {0,1}."""
    out = set()
    for x in range(mod):
        if all(d in (0,1) for d in ternary_digits(x)):
            out.add(x)
    return out

def ternary_digits(x):
    d = []
    if x == 0:
        return [0]
    while x:
        d.append(x % 3)
        x //= 3
    return d

K = 24
sets = survivor_sets(K)
bad = []
for j in range(1, 9):
    mod = 3 ** j
    expected = digit01_set(mod)
    for k in range(j, K + 1):
        got = {r % mod for r in sets[k]}
        if got != expected:
            bad.append((j, k))
print("classes mod 3^j == digit-{0,1} set for all j<=8, k in [j,24]:", not bad, bad[:8])

# also check mod 2*3^j (the real period-domain residue set)
print("=== same check on exponent domain: A_k mod 2*3^j ===")
bad2 = []
for j in range(1, 9):
    mod = 2 * 3 ** j
    # expected: which exponent residues mod 2*3^j are digits-{0,1} allowed.
    # These are 2^{r} mod 3^{j+1} with low j+1 ternary digits in {0,1}.
    exp_expected = set()
    for r in range(mod):
        v = pow(2, r, 3 ** (j + 1))
        if all(d in (0,1) for d in ternary_digits(v)):
            exp_expected.add(r % mod)
    for k in range(j, K + 1):
        got = {r % mod for r in sets[k]}
        if got != exp_expected:
            bad2.append((j, k))
print("exponent-domain classes match for all j<=8, k in [j,24]:", not bad2, bad2[:8])
