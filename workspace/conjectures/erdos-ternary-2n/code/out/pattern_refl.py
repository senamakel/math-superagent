"""Test reflection invariance of A_k about period/2, and exact half behaviour."""
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

sets = survivor_sets(22)
print("=== reflection invariance: r in A_k <=> P_k - r in A_k? (P_k=period) ===")
for k in range(2, 22):
    P = 2*3**(k-1)
    A = sets[k]
    # reflect; but P-r for r in [0,P). map into [0,P)
    refl = { (P - r) % P for r in A }
    print(f" k={k:2d} P={P:7d} |A|={len(A):5d} reflection==A: {refl==A} "
          f" symmetric-r-hit: {sum(1 for r in A if (P-r)%P in A)}/{len(A)}")
