"""Sieve-based sigma(n) up to N, then find qualifying n (2*sigma(n) odd multiple of n)."""
import sys
import numpy as np


def qualifying(N):
    # sigma sieve
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
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 10000000
    print("N =", N)
    q = qualifying(N)
    for n in q:
        print(n, end=" ")
    print()
    print("count:", len(q), "sum:", sum(q))
