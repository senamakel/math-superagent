from math import comb

def A_int(n, w, k):
    nc = comb(n, w)
    A = 0
    wmax = min(k, w); nk = n - k
    for i in range(0, wmax + 1):
        j = w - i
        if 0 <= j <= nk:
            A += (comb(k, i) if i % 2 == 0 else -comb(k, i)) * comb(nk, j)
    return A

def mean_float(n, w):
    tot = 0.0
    nc = comb(n, w)
    for d in range(2, n):
        k = 1 << d.bit_count()
        A = A_int(n, w, k)
        tot += (nc - A) / (2 * nc)
    return tot / n

for n, w in [(8,1),(8,3),(16,1)]:
    print(f"n={n} w={w}  float mean={mean_float(n,w):.6f}")
# now dump per-d A for n=8, w=1
n,w=8,1
nc=comb(n,w)
for d in range(2,n):
    k=1<<d.bit_count()
    A=A_int(n,w,k)
    print(f"  d={d} pc={d.bit_count()} k={k} A={A} P={(nc-A)/(2*nc):.4f}")
