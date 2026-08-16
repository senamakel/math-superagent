"""Identify the survivor exponent classes mod 3^j (the 2^j distinct classes)."""
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

K = 20
sets = survivor_sets(K)

for j in range(1, 7):
    mod = 3 ** j
    A = sets[K]
    classes = sorted({r % mod for r in A})
    print(f"j={j} mod {mod}: {classes}")
