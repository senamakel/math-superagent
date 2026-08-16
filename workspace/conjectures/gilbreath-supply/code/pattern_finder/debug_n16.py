from math import comb

def P(n, w, k):
    # Pr[XOR over k bits of uniform weight-w string is odd] = (C(n,w)-A)/(2 C(n,w))
    nc = comb(n, w)
    A = 0
    wmax = min(k, w)
    nk = n - k
    for i in range(0, wmax + 1):
        j = w - i
        if 0 <= j <= nk:
            A += (comb(k, i) if i % 2 == 0 else -comb(k, i)) * comb(nk, j)
    return (nc - A) / (2 * nc)

def mean(n, w):
    tot = 0.0
    cnt = 0
    for d in range(2, n):
        tot += P(n, w, 1 << d.bit_count())
        cnt += 1
    return tot / n, cnt  # mean of nu2/n, and number of d's

for n, w, expected in [(16,3,0.427902), (8,3,0.4464), (8,8,None)]:
    m, cnt = mean(n, w)
    print(f"n={n} w={w}  mean={m:.6f}  (expected {expected})  #d={cnt}")

# Try excluding d=1?  No, range is 2..n-1. But check what d-range gives 0.4279 at n=16.
# Maybe the operative formula averages over n-1 or n-2 depths, i.e. divides by (n-2)?
m,cnt = mean(16,3)
print("mean/(n) per capture is 0.4279; mean/(n-2) =", m*16/14)
