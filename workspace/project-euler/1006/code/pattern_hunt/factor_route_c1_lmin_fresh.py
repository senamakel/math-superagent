"""Fresh exact-integer audit of c1 and Lmin via Fibonacci-word factors.

The factor route builds one prefix containing all factors, then for each k
counts distinct k-windows beginning with 1.  The quadratic irrational floor is
computed from an exact integer inequality, avoiding floating point.
"""
from math import isqrt
from lib.fibword import fib_prefix, lmin_formula


def floor_alpha(k: int) -> int:
    # floor(k*(3-sqrt(5))/2).  Let t be the candidate.  t <= expression iff
    # (2t-3k)^2 >= 5 k^2, with 2t-3k < 0 in the relevant range.
    # Binary search is unnecessary: compute ceil(k*sqrt(5)) exactly.
    # floor((3k - k*sqrt(5))/2) = (3k-ceil(k*sqrt(5)))//2,
    # except parity is handled by integer division directly.
    s = isqrt(5 * k * k)
    ceil_s = s if s * s == 5 * k * k else s + 1
    return (3 * k - ceil_s) // 2


def next_fib_strict(k: int) -> int:
    a, b = 1, 2
    while b <= k:
        a, b = b, a + b
    return b


def main():
    K = 200_000
    # The strict Lmin maximum below K is < 2K; use a safe 3K prefix.
    W = fib_prefix(3 * K + 10)
    first_falsifier = None
    lmin_falsifier = None
    lmin_samples = {}
    for k in range(1, K + 1):
        factors = {W[i:i+k] for i in range(len(W)-k+1)}
        c1 = sum(word[0] == '1' for word in factors)
        expected = 1 + floor_alpha(k)
        if c1 != expected and first_falsifier is None:
            first_falsifier = (k, c1, expected)
        # Factor-route Lmin: shortest prefix whose windows have all k+1 factors.
        seen = set()
        end = None
        for i in range(len(W)-k+1):
            seen.add(W[i:i+k])
            if len(seen) == k + 1:
                end = i + k
                break
        expected_l = lmin_formula(k)
        if end != expected_l and lmin_falsifier is None:
            lmin_falsifier = (k, end, expected_l)
        if k in (1, 4181, 6764, 6765, 10000, K):
            lmin_samples[k] = (c1, end, next_fib_strict(k))
    print(f'K={K}, prefix_length={len(W)}')
    print('c1 first falsifier:', first_falsifier)
    print('Lmin first falsifier:', lmin_falsifier)
    print('samples (k: c1, Lmin, strict_next_Fibonacci):', lmin_samples)


if __name__ == '__main__':
    main()
