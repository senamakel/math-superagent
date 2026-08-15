#!/usr/bin/env python3
"""Independent oracle: confirm the rule-90 fold identity
fold_cell_bit(h,k,n) == (delta_k(q_n)//2) % 2 for the primes and a couple of
the q-built families, at a spread of (k,n) cells.  This is what makes
F_fold == F_diag structurally true.
"""
from lib.rightdiag import incremental_diagonals
from lib.gilbreath import primes_up_to


def halved_bits(q):
    return [((q[c + 1] - q[c]) // 2) % 2 for c in range(len(q) - 1)]


def fold_cell_bit(h, k, n):
    coeff = k - 1
    s = 0
    for i in range(k):
        if (i & coeff) == i:
            s ^= h[n - k + i]
    return s


def check(seq, label, maxn=400):
    h = halved_bits(seq)
    diags = incremental_diagonals(seq)
    cells = []
    bad = 0
    for n, d in enumerate(diags):
        if n == 0 or n > maxn:
            continue
        for k in range(2, n):
            if (d[k] % 2) != 0:
                # odd diagonal cell -> identity must not claim parity
                cells.append((n, k, 'ODD'))
                continue
            fold = fold_cell_bit(h, k, n)
            true = (d[k] // 2) % 2
            if fold != true:
                bad += 1
                cells.append((n, k, (fold, true)))
    print("%s: %d mismatch cells out of scanned (k=2..n-1, n<=%d)" %
          (label, bad, maxn))
    for c in cells[:8]:
        print("   ", c)
    return bad


def main():
    P = primes_up_to(400000)
    check(P[:401], "real-primes")
    # period-3
    w = [0, 0, 1]
    q = [2, 3]
    while len(q) < 401:
        j = len(q) - 1
        q.append(q[-1] + (2 if w[j % 3] else 4))
    check(q, "period3-001")
    # thue-morse
    q = [2, 3]
    j = 0
    while len(q) < 401:
        q.append(q[-1] + (2 if (bin(j).count("1") & 1) else 4))
        j += 1
    check(q, "thue-morse")
    print("DONE")


if __name__ == "__main__":
    main()
