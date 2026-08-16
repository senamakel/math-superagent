import math, sys
from math import comb

def popcount_counts(n):
    """cnt[p] = #{d in [2,n-1] : popcount(d)=p}."""
    cnt = {}
    for d in range(2, n):
        p = d.bit_count()
        cnt[p] = cnt.get(p, 0) + 1
    return cnt

def A_coeff(n, w, k):
    """A = [z^w](1-z)^k (1+z)^{n-k}, exact integer."""
    A = 0
    wmax = min(k, w); nk = n - k
    for i in range(0, wmax + 1):
        j = w - i
        if 0 <= j <= nk:
            A += (comb(k, i) if i % 2 == 0 else -comb(k, i)) * comb(nk, j)
    return A

def first_threshold(n, num=2, den=5):
    """Smallest w with mean_n(w) >= num/den (default 0.40=2/5). Exact."""
    cnt = popcount_counts(n)
    for w in range(1, n):
        nc = comb(n, w)
        total = 0
        for p, c in cnt.items():
            k = 1 << p
            total += c * (nc - A_coeff(n, w, k))
        # mean = total/(2*n*nc) >= num/den <=> total*den >= num*2*n*nc
        if total * den >= num * 2 * n * nc:
            return w
    return None

if __name__ == "__main__":
    known = {8:3, 10:3, 12:3, 14:4, 16:3, 32:5, 64:7, 128:11, 256:16,
             512:24, 1024:35, 2048:52, 4096:77, 8192:112, 16384:164, 32768:239}
    ok = True
    for n, w in sorted(known.items()):
        got = first_threshold(n)
        print(f"  n={n:6d}  known w*={w:4d}  scan={got:4d}  {'OK' if got==w else 'MISMATCH'}")
        ok &= (got == w)
    print("ALL OK" if ok else "SOME MISMATCH")
