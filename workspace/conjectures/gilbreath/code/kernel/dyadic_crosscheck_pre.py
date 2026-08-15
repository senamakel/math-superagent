#!/usr/bin/env python3
"""Quick cross-check that wt(Phi_n h) equals the direct-triangle maximal-{0,2}
suffix count-of-2s of diag(n) for random small h in the DPC convention
(matrix rows k=2..n-2, cols j=2..n-1, entry C(k-1,j-(n-k)) mod 2)."""
import random
from math import comb
from lib.gilbreath import rows_generator


def phi_entry(k, n, j):
    if not (n - k <= j <= n - 1):
        return 0
    return comb(k - 1, j - (n - k)) % 2


def wt_phi(h, m):
    n = m + 2
    cnt = 0
    for k in range(2, n - 1):      # tail rows 2..n-2
        x = 0
        for j in range(n - k, n):
            if phi_entry(k, n, j):
                x ^= h[j - 2]
        cnt += x
    return cnt


def direct_nu2(h, m):
    # build q with A_1[j] = 2/4 for j=2..n-1 (the columns Phi_n touches),
    # q_1=2, q_2=3, q_3=5 (A_1[1]=2 = the first odd gap shown by the primes).
    n = m + 2
    q = [2, 3, 5]
    # columns j=2..n-1: A_1[j] = 2 if h[j-2]==1 else 4
    for j in range(2, n):
        q.append(q[-1] + (2 if h[j - 2] == 1 else 4))
    # q now has length 3 + (n-2) = n+1 -> A_1 has length n (columns 0..n-1)
    rows = list(rows_generator(q, n))
    # diag(n): rows[k][n-k], k=0..n-1
    d = [rows[k][n - k] for k in range(n)]
    tail = d[2:-1]
    i = len(tail)
    while i > 0 and tail[i - 1] in (0, 2):
        i -= 1
    return tail[i:].count(2)


def main():
    random.seed(1)
    bad = 0
    for trial in range(60):
        m = random.choice([4, 6, 8, 10, 12])
        h = [random.randint(0, 1) for _ in range(m)]
        a = wt_phi(h, m)
        b = direct_nu2(h, m)
        if a != b:
            bad += 1
            print("MISMATCH m=%d h=%s wt=%d direct=%d" % (m, h, a, b))
    print("60 random (m,h): mismatches = %d" % bad)
    # also all-ones (consecutive-odds -> must be wt 0, kernel)
    for m in [4, 6, 8, 10, 12]:
        h = [1] * m
        print("all-ones m=%d: wt_phi=%d direct=%d" % (m, wt_phi(h, m), direct_nu2(h, m)))
    print("CROSSCHECK-PRE DONE")


if __name__ == "__main__":
    main()
