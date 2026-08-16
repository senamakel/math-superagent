"""Fresh structural probe of the survivor sets A_k (Erdos ternary).

Reproduces the standing facts to a larger k and probes what the earlier
passes did not: the survivor exponents' residue distribution mod powers of 3
(prior passes tested only mod 2^m), the exact path each witness takes, and
whether the survivors restrict/project cleanly onto lower levels.

Survivor lift is exact modular arithmetic (never builds 2^n big): A_{k+1}
is built from A_k by testing the three lifts r, r+L, r+2L (L=2*3^(k-1)),
keeping those whose k-th ternary digit of 2^r mod 3^(k+1) is in {0,1}.
"""
from collections import Counter

def survivor_sets(K):
    sets = {1: {0}}
    A = {0}
    cur = 1
    while cur < K:
        L = 2 * 3 ** (cur - 1)
        next_mod = 3 ** (cur + 1)
        g = pow(2, L, next_mod)   # 2^L mod 3^(cur+1)
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

# --- 1. count doubling + witnesses present ---
print("=== count doubling + witnesses ===")
bad = []
for k in range(1, K + 1):
    A = sets[k]
    expect = 2 ** (k - 1)
    if len(A) != expect:
        bad.append((k, len(A), expect))
    for w in (0, 2, 8):
        if w not in A:
            print(f"  witness {w} MISSING at k={k}")
print("all |A_k|==2^(k-1):", not bad, bad[:5])

# --- 2. all survivors even ---
print("all survivors even:", all(r % 2 == 0 for k in range(1, K+1) for r in sets[k]))

# --- 3. residue distribution mod 3, 9, 27 for K=24 ---
print("=== survivor residue distribution mod 3^j (k=24) ===")
A = sets[K]
for j in (1, 2, 3, 4):
    mod = 3 ** j
    c = Counter(r % mod for r in A)
    n_hit = len(c)
    # how many even residues are there mod mod
    print(f" mod {mod}: {n_hit} classes hit;"
          f" distribution(0..): {[c.get(i,0) for i in range(mod)[:min(mod,27)]]}")

# --- 4. projection onto lower level: A_k mod period(k-1) should equal A_{k-1} ---
print("=== projection of A_k onto A_{k-1} (mod 2*3^(k-2)) ===")
proj_bad = []
for k in range(2, K + 1):
    per_prev = 2 * 3 ** (k - 2)
    proj = {r % per_prev for r in sets[k]}
    if proj != sets[k - 1]:
        proj_bad.append(k)
print("projection equals lower set for all k:", not proj_bad, proj_bad[:10])

# --- 5. the path (j decisions) of each witness ---
print("=== witness lifting path (j_1,j_2,...,j_{K-1}) ===")
for wn in (0, 2, 8):
    path = []
    r = wn
    ok = True
    sets_w = {1: {0}}
    A0 = {0}
    for cur in range(1, K):
        L = 2 * 3 ** (cur - 1)
        next_mod = 3 ** (cur + 1)
        g = pow(2, L, next_mod)
        p3k = 3 ** cur
        # current r mod 2*3^(cur-1) must be in A_cur; find its j children
        base = pow(2, r % (2 * 3 ** (cur - 1)), next_mod)
        found = None
        gp = 1
        for j in range(3):
            v = (base * gp) % next_mod
            d = (v // p3k) % 3
            if d in (0, 1):
                # is r+jL the actual continuation of this witness?
                rj = (r % (2 * 3 ** (cur - 1))) + j * L
                if (rj % (2 * 3 ** cur)) == (wn % (2 * 3 ** cur)) and found is None:
                    found = j
            gp = gp * g % next_mod
        # simpler: which j gives r+jL == wn mod 2*3^cur
        cur_per = 2 * 3 ** cur
        jj = ((wn % cur_per) - (wn % (2 * 3 ** (cur - 1)))) // L
        path.append(jj)
        r = wn % cur_per
    print(f" witness {wn}: path[1..{K-1}] all-zero: {all(p==0 for p in path)};"
          f" nonzero entries: {[(t+1,p) for t,p in enumerate(path) if p!=0]}")

# --- 6. fresh number sequences for the pattern tools ---
print("=== min survivor >0 at each k (excluding 0,2,8? no, raw min) ===")
mins = [min(sets[k]) for k in range(1, 13)]
print("min survivor k=1..12:", mins)
print("=== max survivor k=1..12 ===")
maxs = [max(sets[k]) for k in range(1, 13)]
print("max survivor k=1..12:", maxs)
print("=== count of survivors < period/2 (below halfway) ===")
half = []
for k in range(2, 13):
    per = 2 * 3 ** (k - 1)
    half.append(sum(1 for r in sets[k] if r < per // 2))
print("count below period/2, k=2..12:", half)
