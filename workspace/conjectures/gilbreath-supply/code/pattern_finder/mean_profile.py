from math import comb

def mean(n, w):
    tot = 0.0
    for d in range(2, n):
        k = 1 << d.bit_count()
        nc = comb(n, w)
        A = 0
        wmax = min(k, w); nk = n - k
        for i in range(0, wmax + 1):
            j = w - i
            if 0 <= j <= nk:
                A += (comb(k, i) if i % 2 == 0 else -comb(k, i)) * comb(nk, j)
        tot += (nc - A) / (2 * nc)
    return tot / n

for n in [8, 16, 64]:
    print(f"n={n}: ", end="")
    vals = [mean(n, w) for w in range(1, n // 2 + 1)]
    print("  ".join(f"w{w}:{m:.4f}" for w, m in enumerate(vals, start=1)))
    print()
