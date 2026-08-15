"""Verify the Barber balanced-independent-set formula against brute force.

Barber (arXiv:1210.4029), Ramras's conjecture proved: the largest *balanced*
independent set of Q_n (half even, half odd parity, independent) has size
  2^{n-1} - 2^{n-3}(n-2)  (n even)      [formula E]
  2^{n-1} - 2^{n-2}(n-1)   (n odd)      [formula A, source-file prose]
  2^{n-1} - 2^{n-2}(n-1)/2 (n odd)      [formula B, claim-block]
Two transcriptions of the odd-n value disagree by factor 2. Brute force the
true max for small n and see which is right.
"""
from itertools import combinations

def parity(x):
    return bin(x).count('1') % 2

def adjacent(a, b):
    return bin(a ^ b).count('1') == 1

def max_balanced_independent(n):
    N = 1 << n
    even = [v for v in range(N) if parity(v) == 0]
    odd  = [v for v in range(N) if parity(v) == 1]
    # independent edge test
    boundary = [set() for _ in range(N)]
    for a in range(N):
        for b in range(a+1, N):
            if adjacent(a, b):
                boundary[a].add(b); boundary[b].add(a)
    best = 0
    # balanced: |A in even| == |A in odd| == k
    # enumerate k-subset of even and k-subset of odd, independent combined
    import itertools
    for k in range(0, len(even)+1):
        found = False
        for E in itertools.combinations(even, k):
            Es = set(E)
            okE = all(not (boundary[a] & Es - {a}) for a in E)
            if not okE: continue
            for O in itertools.combinations(odd, k):
                Os = set(O)
                # no even-odd edges, no odd-odd edges
                ok = True
                for v in O:
                    if boundary[v] & Es:
                        ok = False; break
                    if boundary[v] & (Os - {v}):
                        ok = False; break
                if ok:
                    found = True
                    break
            if found: break
        if found:
            best = 2*k
    return best

for n in range(2, 5):
    m = max_balanced_independent(n)
    if n % 2 == 0:
        fE = (1 << (n-1)) - (1 << (n-3))*(n-2)
        print(f"n={n} (even): brute={m}  formulaE={fE}")
    else:
        fA = (1 << (n-1)) - (1 << (n-2))*(n-1)
        fB = (1 << (n-1)) - (1 << (n-2))*(n-1)//2
        print(f"n={n} (odd): brute={m}  formulaA(prose)={fA}  formulaB(claim)={fB}")
