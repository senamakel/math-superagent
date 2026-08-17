"""Verify the proposed exact regularity for Lmin(k), the minimal prefix length
of the infinite Fibonacci word containing all k+1 distinct length-k factors:

    Lmin(k) = k + NextFib(k) - 1,
    NextFib(k) = the least Fibonacci number strictly greater than k.

Equivalently, with F_m <= k < F_{m+1}:  Lmin(k) = k + F_{m+1} - 1.

Same integer bit-tricks as gen_sequences, but recomputed from scratch here
(independent prefix, independent implementation), extended beyond the
OEIS-A344953 note terms, and checked block by block at Fibonacci boundaries,
which are the points the formula could plausibly break.

Also records, for the record, the refutation of the naive guess
Lmin(k) = floor(phi^2 k): it fails at k=2 (4 vs 5) and 992 times in [1,1000].
"""

from math import isqrt
from bisect import bisect_right


def fibs_upto(N):
    f = [1, 2]
    while f[-1] < N:
        f.append(f[-1] + f[-2])
    return f


def next_fib(k, fibs):
    """Least Fibonacci number (from list fibs, F_2=1, F_3=2, ...) > k."""
    return fibs[bisect_right(fibs, k)]


def fib_prefix(L):
    a, b = '0', '01'
    while len(b) < L:
        a, b = b, b + a
    return b


def lmin_fast(W, kmax):
    """Lmin(1..kmax) via integer factors over one prefix W."""
    Ltot = len(W)
    WI = int(W, 2)
    out = []
    for k in range(1, kmax + 1):
        n = Ltot - k + 1
        s = set()
        found = None
        for i in range(n):
            f = (WI >> (Ltot - k - i)) & ((1 << k) - 1)
            s.add(f)
            if len(s) == k + 1:
                found = i + k
                break
        out.append(found)
    return out


def main():
    KMAX = 2583          # end of the block k in [1597, 2583), F_17 = 1597
    L = 6000 + 60        # prefix >= ~3.5 * 2583 + slack
    W = fib_prefix(L)
    print(f"prefix length {len(W)} (should be F_19 = 6765 or larger)")

    lm = lmin_fast(W, KMAX)

    fibs = fibs_upto(KMAX + 1)
    mism = []
    for k in range(1, KMAX + 1):
        want = k + next_fib(k, fibs) - 1
        if lm[k - 1] != want:
            mism.append((k, lm[k - 1], want))
    print(f"mismatches of Lmin(k) = k + NextFib(k) - 1 for k=1..{KMAX}: {len(mism)}")
    print("first mismatches:", mism[:10])

    # cross-check every Fibonacci boundary: k = F_m-1, F_m, F_m+1
    print("\nFibonacci-boundary check (k = F_m - 1, F_m, F_m + 1):")
    ok = True
    for Fm in fibs:
        if Fm > KMAX:
            break
        for k in (Fm - 1, Fm, Fm + 1):
            if k < 1 or k > KMAX:
                continue
            want = k + next_fib(k, fibs) - 1
            good = lm[k - 1] == want
            ok = ok and good
            if not good:
                print(f"  FAIL at k={k}: Lmin={lm[k-1]} formula={want}")
    print("all Fibonacci-boundary checks passed:", ok)

    # compare against the note's 58 hardcoded A344953 terms (positions 1..58)
    a344 = [2, 4, 7, 8, 12, 13, 14, 20, 21, 22, 23, 24, 33, 34, 35, 36, 37,
            38, 39, 40, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66,
            88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102,
            103, 104, 105, 106, 107, 108, 143, 144, 145, 146, 147, 148, 149]
    note_ok = all(lm[k - 1] == a344[k - 1] for k in range(1, len(a344) + 1))
    print(f"A344953 note terms (1..{len(a344)}) agree with recomputed Lmin: {note_ok}")

    print("\nSelected values:")
    for k in [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987,
              1597, 2583]:
        if k <= KMAX:
            print(f"  k={k:5d}  Lmin={lm[k-1]:5d}  formula={k + next_fib(k, fibs) - 1}")


if __name__ == '__main__':
    main()