"""Check directive-9 Claim 1 (the load-bearing set identity for the O(log) route):

   "the k+1 DISTINCT length-k Fibonacci factors are exactly the k+1 CONTIGUOUS
    windows at positions r = F_n-k-1 .. F_n-1 of the doubled standard word q_n q_n,
    as sets, for ANY n with F_n > k."

Mechanical construction in solution.py uses slope a = F_n/F_{n+2}, n minimal with
F_{n+2} > k, and q_n is the standard word with |q_n| = F_n.  In that convention the
arc-midpoint word set == brute distinct factors (P1, verified k=1..150).

But directive 9 claims the identity for ANY n with F_n > k, not just the minimal
one.  Test: for each k and each n with F_n > k, do the k+1 windows at positions
F_n-k-1..F_n-1 of q_n q_n, read as decimals, EQUAL the brute distinct factors?
Also: are the window WORDS (digit strings) equal to the factor strings?
"""
from fractions import Fraction


def standard_word(n):
    if n == 0:
        return '0'
    if n == 1:
        return '01'
    a, b = '0', '01'
    for _ in range(2, n + 1):
        a, b = b, b + a
    return b


def fibs_upto(limit):
    f = [0, 1]
    while f[-1] <= limit:
        f.append(f[-1] + f[-2])
    return f


def fib_word(min_len):
    a, b = '0', '01'
    while len(b) < min_len:
        a, b = b, b + a
    return b


def distinct_factors(word, k):
    return {word[i:i + k] for i in range(len(word) - k + 1)}


def claim1_check(k_max, n_min, n_max):
    F = fibs_upto(n_max * 2)
    bad = []           # window WORDS != factor strings
    badval = []        # window decimal VALUES != factor decimal values
    tested = 0
    for k in range(1, k_max + 1):
        brute_f = distinct_factors(fib_word(4 * k + 8), k)
        for n in range(n_min, n_max + 1):
            if F[n] <= k:
                continue
            q = standard_word(n)
            qq = q + q
            # positions r = F_n-k-1 .. F_n-1  (k+1 windows)
            r0 = F[n] - k - 1
            r1 = F[n] - 1
            wins = [qq[r:r + k] for r in range(r0, r1 + 1)]
            # window words must equal the factor strings
            tested += 1
            if set(wins) != brute_f:
                bad.append((k, n, F[n], sorted(wins), sorted(brute_f)))
                if len(bad) >= 3:
                    return bad, badval, tested
            # window decimal values must equal factor decimal values
            if {int(w) for w in wins} != {int(f) for f in brute_f}:
                badval.append((k, n, F[n], sorted({int(w) for w in wins}),
                               sorted({int(f) for f in brute_f})))
                if len(badval) >= 3:
                    return bad, badval, tested
    return bad, badval, tested


if __name__ == "__main__":
    bad, badval, tested = claim1_check(15, 3, 14)
    print(f"Claim 1 test: k=1..15, n=3..14 with F_n>k  ({tested} (k,n) pairs)")
    if bad:
        print("WORD-SET MISMATCHES:")
        for k, n, Fn, wins, brute in bad[:3]:
            print(f"  k={k} n={n} F_n={Fn}")
            print(f"    windows = {wins}")
            print(f"    brute   = {brute}")
    else:
        print("  all window WORD sets == brute distinct factor strings")
    if badval:
        print("VALUE-SET MISMATCHES (windows as decimals differ from brute):")
        for k, n, Fn, wv, bv in badval[:3]:
            print(f"  k={k} n={n} F_n={Fn}")
            print(f"    window vals = {wv}")
            print(f"    brute vals  = {bv}")
    else:
        print("  all window decimal-VALUE sets == brute factor decimal values")
    if not bad and not badval:
        print("CLAIM 1 HOLDS for the tested range (every n with F_n>k).")
