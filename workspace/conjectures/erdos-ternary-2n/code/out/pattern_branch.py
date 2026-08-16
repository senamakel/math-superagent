"""Survivor-lift structure: nesting of A_k and the excluded-child pattern.

For each survivor r at level k (mod 2*3^(k-1)), the three lifts r, r+L, r+2L
(L=2*3^(k-1)) are candidates at level k+1; exactly 2 have new digit in {0,1}.
Which of the 3 is EXCLUDED (gets ternary digit 2) is the branch-deletion.

Probe:
1. Does A_k nest into A_{k+1} (j=0 lift always survives)?  => confirms doubling.
2. For each survivor, record which of j=0,1,2 is excluded; is there structure
   (e.g. excluded index tied to residue class mod something)?
"""
import sys
from collections import Counter

def survivor_sets(k):
    A = {0}
    sets = {1: A}
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
        sets[cur] = A
    return sets

K = int(sys.argv[1]) if len(sys.argv) > 1 else 14
sets = survivor_sets(K)

# nesting: does max(A_k) < 2*3^(k-1) (period) and is every j=0 lift in A_{k+1}?
nested = True
for k in range(1, K):
    Ak = sets[k]
    Ak1 = sets[k+1]
    for r in Ak:
        if r not in Ak1:
            nested = False
            print("nesting FAILED at", k, r)
print(f"K={K}  A_k nests in A_{{k+1}} (j=0 lifts survive): {nested}")

# which child (j) is excluded for each survivor at each level?
# excluded = the j whose digit d at position k equals 2
print()
print("excluded-child count by level:")
for k in range(1, K):
    L = 2 * 3 ** (k - 1)
    next_mod = 3 ** (k + 1)
    g = pow(2, L, next_mod)
    p3k = 3 ** k
    exc = Counter()
    per = collections_Counter = None
    for r in sets[k]:
        base = pow(2, r, next_mod)
        gp = 1
        for j in range(3):
            v = (base * gp) % next_mod
            d = (v // p3k) % 3
            if d == 2:
                exc[j] += 1
            gp = gp * g % next_mod
    print(f"  k={k}: excluded-child distribution {dict(exc)}  (should sum to |A_k|={len(sets[k])})")

# Is the excluded index a function of (r mod power of 2)? quick check at k=8
# look at excluded j vs r mod 8
print()
k = 8
L = 2 * 3 ** (k - 1)
next_mod = 3 ** (k + 1)
g = pow(2, L, next_mod)
p3k = 3 ** k
from collections import defaultdict
excl_by_rmod8 = defaultdict(Counter)
for r in sets[k]:
    base = pow(2, r, next_mod)
    gp = 1
    for j in range(3):
        v = (base * gp) % next_mod
        d = (v // p3k) % 3
        if d == 2:
            excl_by_rmod8[r % 8][j] += 1
        gp = gp * g % next_mod
print("at k=8, excluded-child distribution grouped by r mod 8:")
for rc in sorted(excl_by_rmod8):
    print("  r mod 8 =", rc, dict(excl_by_rmod8[rc]))
