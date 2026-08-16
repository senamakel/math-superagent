"""Verify: A_k contains no nontrivial pair {r, P_k - r}; the only element whose
reflection is also in A_k is r=0. Exact modular survivor lift to k=26.
Also double-check the reflection-hit is exactly 1 and equals r=0.""" 
from time import time

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

K = 26
t0=time()
sets = survivor_sets(K)
print(f"built to k={K} in {time()-t0:.1f}s")

print("=== reflection-avoidance: pairs {r, P-r} in A_k, and hit element ===")
bad = []
for k in range(2, K+1):
    P = 2*3**(k-1)
    A = sets[k]
    hits = [r for r in A if (P - r) % P in A]
    ok = (len(hits) == 1 and hits[0] == 0)
    if not ok: bad.append((k, hits))
    print(f" k={k:2d} |A|={len(A):7d} hits={hits}  (only r=0? {ok})")
print("all reflection-free (only trivial r=0):", not bad, bad[:3])

# independent second route over same data via the VALUE inverse:
# r in A_k and P-r in A_k  <=>  2^r and 2^(P-r)=2^-r both digit-{0,1}-free mod 3^k
print("\n=== independent: values 2^r and 2^-r both in digit-{0,1} set S, r in A_k ===")
bad2 = []
for k in range(2, K+1):
    mod = 3**k
    A = sets[k]
    invset = set()
    for r in A:
        v = pow(2, r, mod)
        v2 = pow(v, -1, mod)          # 2^-r = 2^(P-r)
        # digit-{0,1}-free mod 3^k?
        t = v2; okd = True
        for _ in range(k):
            if t % 3 == 2: okd=False; break
            t //= 3
        if okd:
            invset.add(r)
    # invset should be {0}
    if invset != {0}: bad2.append((k, sorted(invset)[:5]))
    print(f" k={k:2d} exponents r with BOTH 2^r,2^-r digit-free: {sorted(invset)[:4]}")
print("both-inverse-digifree == only {0} for all k:", not bad2, bad2[:2])
