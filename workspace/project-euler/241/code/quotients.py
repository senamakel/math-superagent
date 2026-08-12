import numpy as np


def factorize(n):
    f = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1
            n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f


def sigma_from_factors(f):
    s = 1
    for p, e in f.items():
        s *= (p ** (e + 1) - 1) // (p - 1)
    return s


def qualifying(N):
    sigma = np.zeros(N + 1, dtype=np.int64)
    for d in range(1, N + 1):
        sigma[d::d] += d
    res = []
    for n in range(1, N + 1):
        num = 2 * sigma[n]
        if num % n == 0 and (num // n) % 2 == 1:
            res.append(n)
    return res


if __name__ == "__main__":
    N = 100000000
    q = qualifying(N)
    print(f"{'n':>12} {'2*sigma/n':>10} {'k (p=k+1/2)':>14}  factorization")
    for n in q:
        f = factorize(n)
        s = sigma_from_factors(f)
        two = 2 * s // n
        k = (two - 1) // 2
        fac = " * ".join(f"{p}^{e}" if e > 1 else str(p) for p, e in sorted(f.items()))
        print(f"{n:>12} {two:>10} {k:>14}  {fac}")
