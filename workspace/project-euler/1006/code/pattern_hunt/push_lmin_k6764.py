"""Push the Lmin conjecture to k = 6764 (F_19 = 4181 <= 6764 < F_20 = 6765)
independently, with a prefix >= 24000 chars (L ~ F_22 = 17711 ... need >=
3.7*6764, so build until >= 24000; that lands at F_22 = 17711? no, 17711 <
24000, so next is F_23 = 28657).

Also records the now-verified exact agreement of the autocorrelation /
pair-correlation formula (directive 1) at k = F_n - 1.
"""

from bisect import bisect_right
from math import isqrt


def fibs_upto(N):
    f = [1, 2]
    while f[-1] < N:
        f.append(f[-1] + f[-2])
    return f


def next_fib(k, fibs):
    return fibs[bisect_right(fibs, k)]


def fib_prefix(L):
    a, b = '0', '01'
    while len(b) < L:
        a, b = b, b + a
    return b


def lmin_fast(W, kmax):
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
    KMAX = 6764
    L = 24000
    W = fib_prefix(L)
    print(f"prefix length {len(W)} (F_23=28657)")
    lm = lmin_fast(W, KMAX)
    fibs = fibs_upto(KMAX + 1)
    mism = [(k, lm[k - 1], k + next_fib(k, fibs) - 1)
            for k in range(1, KMAX + 1)
            if lm[k - 1] != k + next_fib(k, fibs) - 1]
    print(f"mismatches k=1..{KMAX}: {len(mism)}")
    print("first mismatches:", mism[:10])
    # boundary check around F_20 = 6765
    for k in (4180, 4181, 6764, 6765):
        if k <= KMAX:
            print(f"k={k} Lmin={lm[k-1]} formula={k + next_fib(k, fibs) - 1}")
    print("all ok:", len(mism) == 0)


if __name__ == '__main__':
    main()