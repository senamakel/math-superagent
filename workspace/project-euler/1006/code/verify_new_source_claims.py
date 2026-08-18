#!/usr/bin/env python3
"""Verify the claim blocks filed for the 2026-08-19/20 library additions.

(a) de Luca 1981 -- palindrome factorisation of finite Fibonacci words:
    f_1=a, f_2=b, f_{n+1}=f_n f_{n-1}; for n>=4, f_n = p q with p, q
    palindromes of lengths F(n-1)-2 and F(n-2)+2; for n>3, f_n has a
    palindrome left factor of length |f_n|-2.
(b) Mignosi 1991 -- card(A_m) = 1 + sum_{i=1}^{m} (m-i+1) phi(i), where A_m is
    the set of length-m factors of all Sturmian words = balanced binary words.
    Brute-force balanced count for m=1..12 must match the totient formula.

These are oracle checks (exponential in m only), not the full-size method.
"""
import math

def fib_words(nmax):
    fs = {1: "a", 2: "b"}
    for n in range(3, nmax + 1):
        fs[n] = fs[n - 1] + fs[n - 2]
    return fs

def is_pal(w):
    return w == w[::-1]

def check_deluca(nmax=16):
    fs = fib_words(nmax)
    fib = [0, 1, 1] + [0] * nmax
    for n in range(3, nmax + 1):
        fib[n] = fib[n - 1] + fib[n - 2]
    print("de Luca 1981 palindrome factorisation (f_1=a, f_2=b, f_{n+1}=f_n f_{n-1})")
    all_ok = True
    for n in range(4, nmax + 1):
        w = fs[n]
        assert len(w) == fib[n], (n, len(w), fib[n])
        lp = fib[n - 1] - 2
        lq = fib[n - 2] + 2
        p, q = w[:lp], w[lp:]
        ok = is_pal(p) and is_pal(q) and len(q) == lq and p + q == w
        # Theorem 1 (Berstel): palindrome left factor of length |f_n|-2 for n>3
        plf = w[:len(w) - 2]
        ok1 = is_pal(plf)
        print(f"  n={n:2d} |f_n|={len(w):3d} p len {lp:2d} pal={is_pal(p)}"
              f" q len {lq:2d} pal={is_pal(q)} | pref-2 pal={ok1}")
        all_ok &= ok and ok1
    print("  ALL de Luca checks passed" if all_ok else "  FAILURE")
    return all_ok

def balanced_count(m):
    """Number of binary words of length m that are balanced (factors of some
    Sturmian word): for all pairs of factors of equal length, |1|-counts
    differ by at most 1."""
    cnt = 0
    for x in range(1 << m):
        w = [(x >> j) & 1 for j in range(m)]
        ok = True
        for L in range(1, m + 1):
            counts = [sum(w[i:i + L]) for i in range(m - L + 1)]
            if max(counts) - min(counts) > 1:
                ok = False
                break
        if ok:
            cnt += 1
    return cnt

def totient_formula(m):
    return 1 + sum((m - i + 1) * sum(1 for d in range(1, i + 1) if math.gcd(d, i) == 1)
                   for i in range(1, m + 1))

def check_mignosi(mmax=12):
    print("\nMignosi 1991 card(A_m) = 1 + sum (m-i+1) phi(i) vs brute-force balanced count")
    all_ok = True
    for m in range(1, mmax + 1):
        tf = totient_formula(m)
        bc = balanced_count(m)
        match = (tf == bc)
        all_ok &= match
        print(f"  m={m:2d} totient={tf:5d} balanced={bc:5d} match={match}")
    print("  ALL Mignosi checks passed" if all_ok else "  MISMATCH -- investigate")
    return all_ok

if __name__ == "__main__":
    a = check_deluca()
    b = check_mignosi()
    print("\nRESULT:", "ALL PASSED" if (a and b) else "SEE ABOVE")
