"""Project Euler 1006 (naive/brute oracle).

Definitions:
    S_0 = '0'
    S_1 = '01'
    S_n = S_{n-1} + S_{n-2}

A Fibonacci subword is a contiguous substring of some S_n.  For a given length
k, we collect all distinct length-k factors of the infinite Fibonacci word by
building S_n until len(S_n) >= 2k (a safe lower bound) and then taking all
length-k substrings of that finite word's tail.  Each collected word is
interpreted as a decimal integer ignoring leading zeros (int('001') == 1 does
this in Python).  Psi(k) = sum of the squares of these integers.

Outputs (must match the problem's known values):
    (a) the distinct length-3 subwords and Psi(3) == 20302
    (b) Psi(1)..Psi(20) plus Psi(10) mod 101001001 == 10699667
    (c) number of distinct length-k subwords for k=1..20 == k+1
"""

M = 101001001


def build_fib(n_tail):
    """Return a long-enough prefix of the infinite Fibonacci word.

    We need every length-k factor to appear.  A standard safe choice is to
    return a Fibonacci word whose length is >= 2k (well inside the region
    where all length-k factors of the infinite word occur).
    """
    s0, s1 = '0', '01'
    # keep generating until the latest word is long enough
    a, b = s0, s1
    while len(b) < 2 * n_tail + 4:
        a, b = b, b + a
    return b


def distinct_factors(word, k):
    """All distinct length-k substrings of word (as a set)."""
    return {word[i:i + k] for i in range(len(word) - k + 1)}


def psi(word_all, k):
    """Psi(k): sum of squares of distinct length-k factors as integers."""
    factors = distinct_factors(word_all, k)
    return sum(int(f) ** 2 for f in factors), factors


def main():
    print("(a) distinct length-3 subwords and Psi(3)")
    word3 = build_fib(3)
    p3, f3 = psi(word3, 3)
    words_sorted = sorted(f3)
    print("    length-3 subwords:", words_sorted)
    print("    Psi(3) =", p3, " (expected 20302)")
    print("    match:", p3 == 20302)
    print()

    print("(b) Psi(1)..Psi(20)")
    for k in range(1, 21):
        wk = build_fib(k)
        pk, _ = psi(wk, k)
        print(f"    Psi({k:2d}) = {pk}")
    p10 = psi(build_fib(10), 10)[0]
    print("    Psi(10) mod", M, "=", p10 % M, " (expected 10699667)")
    print("    match:", p10 % M == 10699667)
    print()

    print("(c) count of distinct length-k subwords for k=1..20 (must equal k+1)")
    for k in range(1, 21):
        wk = build_fib(k)
        factors = distinct_factors(wk, k)
        print(f"    k={k:2d}  count={len(factors):3d}  (k+1={k + 1})  "
              f"match={len(factors) == k + 1}")


if __name__ == "__main__":
    main()
