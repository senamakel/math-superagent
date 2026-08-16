import math
from math import comb

def popcount_counts(n):
    cnt = {}
    for d in range(2, n):
        p = d.bit_count()
        cnt[p] = cnt.get(p, 0) + 1
    return cnt

def A_coeff(n, w, k):
    A = 0
    wmax = min(k, w); nk = n - k
    for i in range(0, wmax + 1):
        j = w - i
        if 0 <= j <= nk:
            A += (comb(k, i) if i % 2 == 0 else -comb(k, i)) * comb(nk, j)
    return A

def first_threshold(n, num=2, den=5):
    cnt = popcount_counts(n)
    pcs = list(cnt.items())
    for w in range(1, n):
        nc = comb(n, w)
        total = 0
        for p, c in pcs:
            k = 1 << p
            total += c * (nc - A_coeff(n, w, k))
        if total * den >= num * 2 * n * nc:
            return w
    return None

if __name__ == "__main__":
    E1 = 0.5568
    E2 = math.log(3)/math.log(2) - 1  # log2(3)-1 = 0.58496
    log43 = math.log(3)/math.log(4)
    nlist = [256,512,768,1024,1536,2048,3072,4096,5120,6144,8192,10240,
             12288,16384,20480,24576,32768,40960,49152,65536]
    print("n        log2n   frac    w*   w/n^E1     w/n^E2     w/n^log43")
    print("-"*90)
    for n in nlist:
        w = first_threshold(n)
        l2 = math.log2(n)
        frac = n / math.pow(2, math.floor(l2))
        print(f"{n:6d}  {l2:7.3f}  {frac:5.3f}  {w:5d}  {w/n**E1:8.4f}  {w/n**E2:8.4f}  {w/n**log43:8.4f}")
