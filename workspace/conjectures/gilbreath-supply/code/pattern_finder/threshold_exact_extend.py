import math
from math import comb

def threshold_weight(n, w):
    """Return True iff mean_n(w) >= 0.40, exactly via integer arithmetic.

    mean_n(w) = (1/n) sum_{d=2}^{n-1} P_d(w)
    P_d(w) = (C(n,w) - A)/(2 C(n,w)), A = [z^w](1-z)^k(1+z)^{n-k}, k=2^popcount(d).
    Group by popcount. mean>=0.40  <=>  5*sum_p cnt(p)(C-A) >= 4*n*C.
    """
    nc = comb(n, w)
    target = 4 * n * nc
    total = 0
    for d in range(2, n):
        k = 1 << d.bit_count()
        A = 0
        wmax = min(k, w)
        nk = n - k
        for i in range(0, wmax + 1):
            j = w - i
            if 0 <= j <= nk:
                A += (comb(k, i) if i % 2 == 0 else -comb(k, i)) * comb(nk, j)
        total += (nc - A)
    return 5 * total >= target

def find_threshold(n):
    hi = 1
    while hi < n and not threshold_weight(n, hi):
        hi = min(hi * 2, n)
    lo = hi // 2
    # binary search (lo, hi]
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if threshold_weight(n, mid):
            hi = mid
        else:
            lo = mid
    return hi

if __name__ == "__main__":
    known = {8:3, 10:3, 12:3, 14:4, 16:3, 32:5, 64:7, 128:11, 256:16,
             512:24, 1024:35, 2048:52, 4096:77, 8192:112, 16384:164}
    for n, w in sorted(known.items()):
        got = find_threshold(n)
        print(f"  n={n:6d}  known w*={w:4d}  recomputed={got:4d}  {'OK' if got==w else 'MISMATCH'}")
