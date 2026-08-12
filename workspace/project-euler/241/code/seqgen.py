"""Generate qualifying n (p(n)=sigma(n)/n = k+1/2) up to a bound, using
prime factorization for speed.  Validates against code/brute.py logic."""
import math
from itertools import count


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
    res = []
    for n in range(1, N + 1):
        f = factorize(n)
        s = sigma_from_factors(f)
        num = 2 * s
        if num % n == 0 and (num // n) % 2 == 1:
            res.append(n)
    return res


if __name__ == "__main__":
    N = 200000
    q = qualifying(N)
    print("count up to", N, ":", len(q))
    print("terms:", q)
