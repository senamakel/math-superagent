"""Bisect the C(k)=len(Psi(k))-(2k-1) transitions in (25684, 30000) and beyond

C(k) is monotone nondecreasing, staircase.  Known steps: k=23 (0->1),
k=256 (1->2), k=2568 (2->3).  This run:
  * finds every transition point = min{k : C(k) >= c} for c = 4, 5, 6, ...
    by binary search within a growing window, exact Psi via the validated
    sliding-window route (program differs from probe_exact_psi_extended.py
    only in the k-grid, which is determined here by search);
  * tests each transition point against {floor(j*phi^2)} for integer
    candidates j, and records j and the ratio t = j / 10^(len(j)-1).
"""
import sys
import time

sys.set_int_max_str_digits(300000)
M = 101001001

_nextfib_cache = {}


def next_fib_strict(k):
    if k in _nextfib_cache:
        return _nextfib_cache[k]
    a, b = 0, 1
    while True:
        a, b = b, a + b
        if b > k:
            _nextfib_cache[k] = b
            return b


def fib_prefix(L):
    a, b = "0", "01"
    while len(b) < L:
        a, b = b, b + a
    return b[:L]


def c1(k):
    from math import isqrt
    N = isqrt(5 * k * k)
    t = 3 * k - N
    return 1 + ((t - 1) // 2 if t % 2 == 1 else t // 2 - 1)


def psi_class(k):
    """Return C(k) = len(Psi(k)) - (2k-1), exact."""
    L = k + next_fib_strict(k) - 1
    y = fib_prefix(L)
    p10k = 10 ** k
    v = int(y[:k])
    s = v * v
    for r in range(L - k):
        v = 10 * v - (1 if y[r] == '1' else 0) * p10k \
            + (1 if y[r + k] == '1' else 0)
        s += v * v
    return len(str(s)) - (2 * k - 1)


def main():
    # sanity: reproduce the three known step points
    print("known step checks (expect C=1,2,3):")
    for k, want in [(24, 1), (257, 2), (2569, 3)]:
        got = psi_class(k)
        print(f"  k={k}: C={got} want={want} {'OK' if got == want else 'MISMATCH'}")
        assert got == want

    # find min k with C(k) >= c for c = 4, 5, 6 by bisection in expanding windows
    t0 = time.time()
    lo = 25684  # C(25684) = 3 (verified)
    for c in (4, 5, 6):
        hi = lo * 2
        while psi_class(hi) < c:
            hi *= 2
            if hi > 200000:
                break
        # binary search for the first k with C(k) >= c
        a, b = lo, hi
        while b - a > 1:
            m = (a + b) // 2
            if psi_class(m) >= c:
                b = m
            else:
                a = m
        print(f"\nC >= {c} first at k = {b}  (C({b})={psi_class(b)}, "
              f"C({b}-1)={psi_class(b - 1)})")

        # Wythoff candidate test: for j in a neighbourhood, is b == floor(j*phi^2)?
        phi2 = (3 + 5 ** 0.5) / 2
        jcand = round(b / phi2)
        for j in range(max(1, jcand - 3), jcand + 4):
            s = int(j * phi2)
            if s == b:
                print(f"    b == floor({j}*phi^2)  (j={j})")
        print(f"    ratio j/10^(len-1) = {jcand / 10 ** (len(str(jcand)) - 1):.9f}")
        lo = b
    print(f"\ntotal time {time.time() - t0:.0f}s")


if __name__ == "__main__":
    main()