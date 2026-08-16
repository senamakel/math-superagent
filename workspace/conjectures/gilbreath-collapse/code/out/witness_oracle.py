"""Brute-force oracle for the primary C_K fiber, to check witness_hunt.py.

C_K(h) = pair-correlation counts N_ab(k), k=1..K. Group by exact tuple (as the
definition demands), check S^2 constancy within fibers. Uses S in the oracle.
"""
import sys
from collections import defaultdict
from lib.collapse import S as Sen


def key(h, n, K):
    out = []
    for k in range(1, K + 1):
        sub = [0, 0, 0, 0]
        for i in range(n - k):
            a = (h >> i) & 1
            b = (h >> (i + k)) & 1
            sub[a * 2 + b] += 1
        out.extend(sub)
    return tuple(out)


def witness(n, K):
    N = 1 << n
    grp = defaultdict(set)
    for h in range(N):
        hl = [(h >> i) & 1 for i in range(n)]
        s2 = Sen(n, hl) ** 2
        grp[key(h, n, K)].add(s2)
    return any(len(v) > 1 for v in grp.values())


def main():
    for n in range(2, 11):
        maxK = n - 1
        kstar = None
        for K in range(1, maxK + 1):
            if not witness(n, K):
                kstar = K
                break
        w1 = witness(n, 1)
        w2 = witness(n, 2) if maxK >= 2 else None
        w3 = witness(n, 3) if maxK >= 3 else None
        wn1 = witness(n, maxK)
        print(f"n={n:2d} K*={kstar} w1={w1} w2={w2} w3={w3} w(n-1)={wn1}")


if __name__ == "__main__":
    main()
