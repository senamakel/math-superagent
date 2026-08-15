#!/usr/bin/env python3
"""Reproduce nu2(n) and w(n) from scratch and connect them to the
two's-complement carry bridge.

nu2(n) = number of 2s in the maximal {0,2} suffix of the prime right diagonal
through q_n (cell A_k[n-k], k=0..n-1), window tail diag[2:-1].
w(n)   = Hamming weight of the halved gap bits h_j = [gap_{j+1} ≡ 2 mod 4]
         over j in [2, n-1]  (h_j = (A_1[j]//2) mod 2, and A_1[j] = gap_{j+1}).

The diagonal is built with lib.gilbreath.rows_generator (the run's oracle
generator) one row at a time. All exact integers. Sieve to 1e6 (~78k primes).

Reports nu2/n and nu2/w ranges, and whether nu2 >= w/2 and nu2 >= 0.45*n hold
on EVERY computed n.
"""
from lib.gilbreath import primes_up_to

BOUND = 1_000_000
MAX_N = 5000        # columns to examine; need W > MAX_N primes
KEEP = MAX_N + 3


def main():
    P = primes_up_to(BOUND)
    W = len(P)
    print("sieve to %d : %d primes" % (BOUND, W))
    assert W > MAX_N + 3, "not enough primes for %d columns" % MAX_N
    P = P[:KEEP]                      # only need MAX_N+1 columns of width

    # halved gap bits h_j = (gap_{j+1}//2) mod 2, j=0..  (gap_{j+1} = P[j+1]-P[j])
    hbits = [((P[i + 1] - P[i]) // 2) % 2 for i in range(len(P) - 1)]

    # build rows one at a time, keep only what we need for diag: rows[k] width
    # shrinks; diag(n) needs rows[k][n-k] for k=0..n-1, i.e. columns 0..n-1 of
    # each row. Keep a window of the first MAX_N columns+2 across rows.
    rows = []
    cur = list(P)                     # A_0
    rows.append(cur)
    for k in range(1, MAX_N):
        cur = [abs(cur[i] - cur[i + 1]) for i in range(len(cur) - 1)]
        rows.append(cur)

    def diag(n):
        return [rows[k][n - k] for k in range(n)]

    rows1 = rows[1]

    def nu2_of(d):
        tail = d[2:-1]
        i = len(tail)
        while i > 0 and tail[i - 1] in (0, 2):
            i -= 1
        cyc = tail[i:]
        return cyc.count(2)

    worst_w = None       # (value, n) where nu2/w is smallest (nu2>=w/2 assert)
    worst_n = None
    first_fail_w2 = None
    first_fail_45 = None
    nu2renge = [10**9, 0]
    nurenge = [10**9, 0]
    wrenge = [10**9, 0]
    nu2renge17 = [10**9, 0]
    onset_w2 = None          # first n where nu2 >= w/2, with all later ok
    onset_45 = None
    first_fail_w2_17 = None
    first_fail_45_17 = None
    w2_failures = []         # all n where nu2 < w/2
    n45_failures = []        # all n where nu2 < 0.45*n
    last_fail_w2 = None
    last_fail_45 = None
    for n in range(2, MAX_N):
        d = diag(n)
        nu2 = nu2_of(d)
        w = sum(hbits[2:n])
        r_n = nu2 / n
        r_w = nu2 / w if w else float('inf')
        nu2renge[0] = min(nu2renge[0], r_n)
        nu2renge[1] = max(nu2renge[1], r_n)
        if n >= 17:
            nu2renge17[0] = min(nu2renge17[0], r_n)
            nu2renge17[1] = max(nu2renge17[1], r_n)
        nurenge[0] = min(nurenge[0], nu2)
        nurenge[1] = max(nurenge[1], nu2)
        wrenge[0] = min(wrenge[0], w)
        wrenge[1] = max(wrenge[1], w)
        if worst_w is None or r_w < worst_w[0]:
            worst_w = (r_w, n, nu2, w)
        if nu2 < w / 2 and first_fail_w2 is None:
            first_fail_w2 = (n, nu2, w)
        if nu2 < w / 2:
            w2_failures.append(n)
            last_fail_w2 = n
        if nu2 < 0.45 * n and first_fail_45 is None:
            first_fail_45 = (n, nu2)
        if nu2 < 0.45 * n:
            n45_failures.append(n)
            last_fail_45 = n
        if n >= 17 and nu2 < w / 2 and first_fail_w2_17 is None:
            first_fail_w2_17 = (n, nu2, w)
        if n >= 17 and nu2 < 0.45 * n and first_fail_45_17 is None:
            first_fail_45_17 = (n, nu2)
        # onset: the last startup failure (so "after onset, always true")
        if nu2 >= w / 2:
            if onset_w2 is None:
                onset_w2 = n
        if nu2 >= 0.45 * n:
            if onset_45 is None:
                onset_45 = n
    ns = MAX_N - 2
    print("\nn range checked: 2..%d (%d columns)" % (MAX_N - 1, ns))
    print("nu2 range: %d..%d ; w range: %d..%d"
          % (nurenge[0], nurenge[1], wrenge[0], wrenge[1]))
    print("nu2/n range: [%.4f, %.4f]" % (nu2renge[0], nu2renge[1]))
    print("nu2/n range over n>=17: [%.4f, %.4f]"
          % (nu2renge17[0], nu2renge17[1]))
    print("worst nu2/w = %.4f at n=%d (nu2=%d, w=%d)"
          % (worst_w[0], worst_w[1], worst_w[2], worst_w[3]))
    print("nu2 >= w/2 on every n : %s" % ("TRUE" if first_fail_w2 is None
          else "FALSE (first fail n=%d nu2=%d w=%d)" % first_fail_w2))
    print("nu2 >= 0.45*n on every n : %s" % ("TRUE"
          if first_fail_45 is None else "FALSE (first fail n=%d nu2=%d)"
          % first_fail_45))
    print("last startup failure for nu2>=w/2 : n=%d ; after n=%d both hold"
          % (last_fail_w2, max(last_fail_w2 or 0, last_fail_45 or 0) + 1))
    print("nu2 >= w/2 over n>=17 : %s" % ("TRUE"
          if first_fail_w2_17 is None
          else "FALSE (first fail n=%d nu2=%d w=%d)" % first_fail_w2_17))
    print("nu2 >= 0.45*n over n>=17 : %s" % ("TRUE"
          if first_fail_45_17 is None
          else "FALSE (first fail n=%d nu2=%d)" % first_fail_45_17))
    print("nu2>=w/2 violation set over 2..%d: %s (last n=%d)"
          % (MAX_N - 1, w2_failures, last_fail_w2))
    print("nu2>=0.45n violation set over 2..%d: %s (last n=%d)"
          % (MAX_N - 1, n45_failures, last_fail_45))
    # reproduce the sampled table of the earlier record
    print("\nsampled table (n, nu2, w, nu2/n, nu2/w):")
    for n in [50, 100, 200, 400, 800, 1600, 3200, 3999]:
        if n >= MAX_N:
            continue
        d = diag(n)
        nu2 = nu2_of(d)
        w = sum(hbits[2:n])
        print("  n=%-5d nu2=%-6d w=%-6d nu2/n=%.4f nu2/w=%.4f"
              % (n, nu2, w, nu2 / n, nu2 / w if w else 0))
    return (first_fail_w2 is None and first_fail_45 is None)


if __name__ == "__main__":
    main()
