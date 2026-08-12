"""PE241 brute-force oracle: numbers n with sigma(n)/n = k + 1/2 (2*sigma(n)/n odd integer)."""
from math import isqrt

def sigma(n):
    s = 1
    d = 2
    while d*d <= n:
        if n % d == 0:
            p = 1  # power of d
            while n % d == 0:
                n //= d
                p *= d
            s *= (p*d - 1)//(d - 1)
        d += 1 if d == 2 else 2
    if n > 1:
        s *= (1 + n)
    return s

def is_pe241(n):
    # 2*sigma(n)/n is an odd integer
    num = 2*sigma(n)
    return num % n == 0 and (num // n) % 2 == 1

LIM = 2*10**6
res = [n for n in range(1, LIM+1) if is_pe241(n)]
print("count", len(res))
print(res)
