"""Extract the survivor-residue class structure A_k mod 3^j and its recursion.
The survivor lift keeps (r, r+L, r+2L) when the digit is in {0,1}. We want the
actual set of residue classes hit, to see the exact recursion and whether the
residues form a known self-similar set.
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

sets = survivor_sets(14)
A = sets[14]
print("total |A_14| =", len(A))
for j in (1,2,3,4,5,6):
    mod = 3**j
    classes = sorted({r % mod for r in A})
    print(f"mod 3^{j}={mod}: {len(classes)} classes -> {classes}")

# also mod 2*3^j for small j, the actual period residue set
print()
for j in (1,2,3):
    mod = 2*3**j
    classes = sorted({r % mod for r in A})
    print(f"mod 2*3^{j}={mod}: {len(classes)} classes -> {classes}")
