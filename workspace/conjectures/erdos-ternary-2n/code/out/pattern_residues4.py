"""Verify: (1) residue classes mod 3^j count, (2) half-count sequence to k=24,
(3) ATTACK: mixed-radix {0,1} characterization of survivor residues (expect refute).
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

# (1) classes mod 3^j
print("=== |A_k mod 3^j| for k=24, j=1..8 ===")
A = sets[K]
for j in range(1, 9):
    mod = 3 ** j
    c = len({r % mod for r in A})
    print(f"  j={j}: {c} classes (2^j={2**j})")

# also for k=12 vs k=24 check independence of k (j<=6)
print("=== |A_k mod 3^j| for k in {8,12,16,20,24}, j=4 ===")
for kk in (8,12,16,20,24):
    print(f"  k={kk}: {len({r % 81 for r in sets[kk]})} classes mod 81")

# (2) half-count
print("=== count below period/2, k=2..24 ===")
hc = []
for k in range(2, K + 1):
    per = 2 * 3 ** (k - 1)
    hc.append(sum(1 for r in sets[k] if 2 * r < per))
print(hc)
print("excess over 2^(k-2):", [hc[t] - 2**((t+2)-1-1) for t in range(len(hc))])

# (3) mixed-radix {0,1} attack
def mixed_radix_digits(r, k):
    # place values 2*3^(i-1), i=1..k-1, digits d_i in {0,1,2}
    digs = []
    for i in range(1, k):
        pv = 2 * 3 ** (i - 1)
        digs.append((r // pv) % 3)
    return digs
print("=== mixed-radix {0,1} attack ===")
viol = []
for k in range(2, K + 1):
    A = sets[k]
    bad = [r for r in A if any(d not in (0,1) for d in mixed_radix_digits(r, k))]
    if bad:
        viol.append((k, bad[:5]))
print("survivors with a mixed-radix digit 2 (should be [] if characterization holds):")
for k, b in viol[:8]:
    print(f"  k={k}: {b}")
