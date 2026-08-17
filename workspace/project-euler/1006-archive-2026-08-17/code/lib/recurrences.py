"""Linear recurrence utilities: Berlekamp–Massey over a prime, and exact
rational reconstruction of coefficients.

One subject per module. These functions find a constant-coefficient linear
recurrence satisfied by an integer sequence (e.g. Psi(k)) by running BM over
several primes, reconstructing rational coefficients, and verifying on the exact
integers.
"""
from math import gcd, isqrt


def berlekamp_massey(seq, p):
    """Minimal LFSR order and coefficients for `seq` over F_p.

    seq: list of ints (taken mod p). Returns (order, C) where C is a list
    [c_0..c_{order-1}] meaning, for k >= order,
        seq[k] = c_0*seq[k-1] + c_1*seq[k-2] + ... + c_{order-1}*seq[k-order]
    all mod p. cp-algorithms Berlekamp–Massey.
    """
    s = [x % p for x in seq]
    n = len(s)
    C = [0] * n
    B = [0] * n
    C[0] = B[0] = 1
    L = 0
    m = 1
    b = 1
    for i in range(n):
        d = s[i] % p
        for j in range(1, L + 1):
            d = (d + C[j] * s[i - j]) % p
        if d == 0:
            m += 1
            continue
        T = C[:]
        coef = d * pow(b, p - 2, p) % p
        for j in range(m, n):
            C[j] = (C[j] - coef * B[j - m]) % p
        if 2 * L <= i:
            L = i + 1 - L
            B = T
            b = d
            m = 1
        else:
            m += 1
    C = C[:L + 1]
    coeffs = [(-C[j]) % p for j in range(1, L + 1)]
    return L, coeffs


def verify_recurrence(seq, C, p=None):
    """Check seq[k]==sum(C[j]*seq[k-1-j]) for all k>=len(C), exactly.

    seq: exact Python ints. C: exact int coefficients. If p given, do arithmetic
    mod p; else exact big-int. Returns (ok, first_bad_k).
    """
    L = len(C)
    for k in range(L, len(seq)):
        total = 0
        for j in range(L):
            total += C[j] * seq[k - 1 - j]
        if p is not None:
            if (total - seq[k]) % p != 0:
                return (False, k)
        else:
            if total != seq[k]:
                return (False, k)
    return (True, None)


def rational_reconstruct(x, m):
    """Reconstruct a small rational num/den with num/den === x (mod m),
    |num|, den <= isqrt(m/2), reduced, or None if not found within that bound.

    Brute forces denominators up to the bound (fine for m~1e9, bound~22361).
    """
    N = isqrt(m // 2)
    x %= m
    for den in range(1, N + 1):
        num = (den * x) % m
        if num > N and m - num > N:
            continue
        if num > m // 2:
            num -= m
        g = gcd(abs(num), den)
        if g > 1:
            num, den = num // g, den // g
        if (num * pow(den, -1, m)) % m == x % m:
            return (num, den)
    return None
