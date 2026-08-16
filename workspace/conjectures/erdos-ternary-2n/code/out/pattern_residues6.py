"""Pin down the two exact survivor-residue facts precisely:
(1) for k > j, the residue classes of A_k mod 2*3^j equal A_j exactly (nesting).
(2) for k > j, |A_k mod 3^j| = 2^j (= |A_j| value-image).
Also count mixed-radix-violating survivors per k (the refutation).
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

K = 24
sets = survivor_sets(K)

# (1) nesting on exponent domain: A_k mod 2*3^j == A_j for k>j
print("=== A_k mod 2*3^j == A_j ? (k>j) ===")
bad = []
for j in range(1, 9):
    mod = 2 * 3 ** j
    for k in range(j + 1, K + 1):
        got = {r % mod for r in sets[k]}
        if got != sets[j]:
            bad.append((j, k))
print("holds for all j<=8, k in (j,24]:", not bad, bad[:8])

# (2) value classes
print("=== |A_k mod 3^j| = 2^j for k>j ===")
bad2 = []
for j in range(1, 9):
    mod = 3 ** j
    for k in range(j + 1, K + 1):
        if len({r % mod for r in sets[k]}) != 2 ** j:
            bad2.append((j, k))
print("holds for all j<=8, k in (j,24]:", not bad2, bad2[:8])

# (3) mixed-radix violation counts
def mixed_violations(A, k):
    cnt = 0
    for r in A:
        d = []
        for i in range(1, k):
            d.append((r // (2 * 3 ** (i - 1))) % 3)
        if any(x == 2 for x in d):
            cnt += 1
    return cnt

print("=== survivors violating mixed-radix {0,1} (count / |A|) k=2..16 ===")
for k in range(2, 17):
    print(f"  k={k}: {mixed_violations(sets[k], k)}/{len(sets[k])}")
