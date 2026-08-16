#!/usr/bin/env python3
"""Independent check of the claimed closed form K*(n) = ceil(n/2).

Statement under attack (G-kstar-budget / R-budget-n32, a load-bearing rung of
this pass):

    K*(n) = min{K >= 1 : S^2 is constant on every C_K-fiber of F_2^n}
          = min{K : no pair h,h' with identical C_K(h)=C_K(h') but S^2(h)!=S^2(h')}
          = ceil(n/2)  for all n >= 6   (n=5 the sole exception: K*(5)=2).

where C_K(h) is the (K+1)-gram histogram of h (the order-K correlation vector:
counts of every binary word of length K+1 over the n-K overlapping windows),
and S(n) = sum_{d=2}^{n-1} (-1)^{T(n,d)} is the signed fold excess, T(n,d) the
fold cell, S^2 the squared excess.

I recompute K*(n) from scratch with the statement's OWN definition: the smallest
K at which no two strings sharing a C_K-fiber have different S^2. This is the
exact brute oracle (exponential 2^n over F_2^n), bounded to small n.

Also report floor(n/2), ceil(n/2) for comparison, and each n's value.
"""

import sys, itertools

sys.path.insert(0, "/workspace/code")
from lib.supply_fold import s_sos


def c_k(h, K):
    """Order-K correlation vector: (K+1)-gram histogram over n-K windows.
    Returned as a tuple (order-independent)."""
    n = len(h)
    counts = {}
    for start in range(n - K):
        w = 0
        for t in range(K + 1):
            w = (w << 1) | h[start + t]
        counts[w] = counts.get(w, 0) + 1
    # canonicalize: sorted tuple of (word,count)
    return tuple(sorted(counts.items()))


def s_squared(n, h):
    S, _ = s_sos(n, h)
    return S * S


def kstar(n):
    """min K>=1 such that no pair h,h' in F_2^n has C_K(h)=C_K(h') but
    different S^2. Returns (K*, also locks which K have a separating pair)."""
    strings = list(itertools.product([0, 1], repeat=n))
    s2 = {s: s_squared(n, s) for s in strings}
    separating = {}
    for K in range(1, n):
        fibers = {}
        for s in strings:
            key = c_k(s, K)
            fibers.setdefault(key, []).append(s)
        # is there a fiber with two different S^2 values?
        has = any(len({s2[s] for s in grp}) > 1 for grp in fibers.values())
        separating[K] = has
        if not has:
            return K, separating
    return None, separating


def main():
    nmax = int(sys.argv[1]) if len(sys.argv) > 1 else 14
    out = []
    out.append("K* check vs ceil(n/2) under the STATEMENT's own definition")
    out.append("(min K: no pair with identical C_K but different S^2)")
    out.append("oracle: lib.supply_fold.s_sos (canonical floored); n = 3..%d"
               % nmax)
    out.append("")
    header = ("%4s %8s %8s %8s %12s %s"
              % ("n", "K*", "floor", "ceil", "match-ceil", "separating K"))
    out.append(header)
    out.append("-" * len(header))
    for n in range(3, nmax + 1):
        K, sep = kstar(n)
        fl, ce = n // 2, (n + 1) // 2
        match = "YES" if K == ce else ("NO->floor" if K == fl else "NEITHER")
        seplist = ",".join(str(k) for k in range(1, n) if sep.get(k)) or "-"
        out.append("%4d %8s %8d %8d %12s %s" % (n, K, fl, ce, match, seplist))
    out.append("")
    out.append("NOTE: n=3 -> floor(3/2)=1, ceil(3/2)=2. The 'match-ceil' column")
    out.append("shows where K* == ceil(n/2). If K* == floor(n/2) at odd n, the")
    out.append("claimed closed form K* = ceil(n/2) is WRONG at those n.")
    print("\n".join(out))


if __name__ == "__main__":
    main()
