#!/usr/bin/env python3
"""Efficient brute-force K*(n) table (exhaustive F_2^n, exact).

K*(n) := min{K>=1 : S^2 constant on every C_K-fiber}. S^2 = (sum_{d=2}^{n-1}
(-1)^{T(n,d)})^2 via the canonical s_sos. C_K(h) = (K+1)-gram histogram tuple.

Method per n: enumerate all 2^n strings once, compute S^2 for each (cheap, one
s_sos), and cache C_K(h) lazily. For the 'is S^2 constant on every C_K-fiber'
test at order K, group the 2^n S^2-values by their C_K key and check each fiber
has a single value. Because C_{K+1} refines C_K (marginalise a gram), the first K
with no witness is a single crossing point.

This is the brute oracle (exponential 2^n, bounded to n<=20). Pure combinatorics
of Phi_n over F_2^n, no primes.
"""
import sys, itertools, time
sys.path.insert(0, "/workspace/code")
from lib.supply_fold import s_sos


def c_k_key(h, K, L_prev=None):
    """(K+1)-gram histogram as a sortable tuple key."""
    n = len(h)
    d = {}
    for st in range(n - K):
        w = 0
        for t in range(K + 1):
            w = (w << 1) | h[st + t]
        d[w] = d.get(w, 0) + 1
    return tuple(d.get(i, 0) for i in range(1 << (K + 1)))


def s2(n, h):
    S, _ = s_sos(n, h)
    return S * S


def kstar_brute(n):
    allstr = list(itertools.product([0, 1], repeat=n))
    s2v = {s: s2(n, s) for s in allstr}
    flags = {}
    for K in range(1, n):
        fibers = {}
        for s in allstr:
            key = c_k_key(s, K)
            fibers.setdefault(key, set()).add(s2v[s])
        hasw = any(len(v) > 1 for v in fibers.values())
        flags[K] = hasw
        if not hasw:
            return K, flags
    return n - 1, flags


def main():
    out = []
    start_all = time.time()
    for n in range(4, 21):
        t0 = time.time()
        kstar, flags = kstar_brute(n)
        flagstr = "".join("T" if flags.get(K) else "." for K in range(1, n))
        imp = IMPORTED.get(n, "?")
        match = "OK" if imp == "?" or kstar == imp else "MISMATCH-imported"
        out.append(f"n={n:3d} K*_brute={kstar:3d} imported={imp:3d} "
                   f"witness_flags={flagstr} {match}  ({time.time()-t0:.1f}s)")
        print(f"n={n:3d} K*={kstar:3d} imported={imp:3d} {match} ({time.time()-t0:.1f}s)")
    out.append(f"(total {time.time()-start_all:.1f}s)")
    with open("/workspace/code/out/kstar_brute_table.txt", "w") as f:
        f.write("\n".join(out) + "\n")
    print("\n".join(out))


IMPORTED = {2: 1, 3: 1, 4: 2, 5: 2, 6: 3, 7: 4, 8: 4, 9: 5, 10: 5, 11: 6, 12: 6,
            13: 7, 14: 7, 15: 8, 16: 8, 17: 9, 18: 9, 19: 10, 20: 10}

if __name__ == "__main__":
    main()
